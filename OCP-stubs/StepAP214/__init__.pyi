import OCP.StepAP214
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.StepBasic
import OCP.StepData
import OCP.StepVisual
import OCP.Interface
import OCP.Standard
import OCP.StepGeom
import OCP.TColStd
import OCP.StepRepr
import OCP.StepShape
__all__  = [
"StepAP214",
"StepAP214_AppliedApprovalAssignment",
"StepAP214_AppliedDateAndTimeAssignment",
"StepAP214_AppliedDateAssignment",
"StepAP214_AppliedDocumentReference",
"StepAP214_AppliedExternalIdentificationAssignment",
"StepAP214_AppliedGroupAssignment",
"StepAP214_AppliedOrganizationAssignment",
"StepAP214_AppliedPersonAndOrganizationAssignment",
"StepAP214_AppliedPresentedItem",
"StepAP214_AppliedSecurityClassificationAssignment",
"StepAP214_ApprovalItem",
"StepAP214_Array1OfApprovalItem",
"StepAP214_Array1OfAutoDesignDateAndPersonItem",
"StepAP214_Array1OfAutoDesignDateAndTimeItem",
"StepAP214_Array1OfAutoDesignDatedItem",
"StepAP214_Array1OfAutoDesignGeneralOrgItem",
"StepAP214_Array1OfAutoDesignGroupedItem",
"StepAP214_Array1OfAutoDesignPresentedItemSelect",
"StepAP214_Array1OfAutoDesignReferencingItem",
"StepAP214_Array1OfDateAndTimeItem",
"StepAP214_Array1OfDateItem",
"StepAP214_Array1OfDocumentReferenceItem",
"StepAP214_Array1OfExternalIdentificationItem",
"StepAP214_Array1OfGroupItem",
"StepAP214_Array1OfOrganizationItem",
"StepAP214_Array1OfPersonAndOrganizationItem",
"StepAP214_Array1OfPresentedItemSelect",
"StepAP214_Array1OfSecurityClassificationItem",
"StepAP214_AutoDesignActualDateAndTimeAssignment",
"StepAP214_AutoDesignActualDateAssignment",
"StepAP214_AutoDesignApprovalAssignment",
"StepAP214_AutoDesignDateAndPersonAssignment",
"StepAP214_AutoDesignDateAndPersonItem",
"StepAP214_AutoDesignDateAndTimeItem",
"StepAP214_AutoDesignDatedItem",
"StepAP214_AutoDesignDocumentReference",
"StepAP214_AutoDesignGeneralOrgItem",
"StepAP214_AutoDesignGroupAssignment",
"StepAP214_AutoDesignGroupedItem",
"StepAP214_AutoDesignNominalDateAndTimeAssignment",
"StepAP214_AutoDesignNominalDateAssignment",
"StepAP214_AutoDesignOrganizationAssignment",
"StepAP214_AutoDesignOrganizationItem",
"StepAP214_AutoDesignPersonAndOrganizationAssignment",
"StepAP214_AutoDesignPresentedItem",
"StepAP214_AutoDesignPresentedItemSelect",
"StepAP214_AutoDesignReferencingItem",
"StepAP214_AutoDesignSecurityClassificationAssignment",
"StepAP214_Class",
"StepAP214_DateAndTimeItem",
"StepAP214_DateItem",
"StepAP214_DocumentReferenceItem",
"StepAP214_ExternalIdentificationItem",
"StepAP214_ExternallyDefinedClass",
"StepAP214_ExternallyDefinedGeneralProperty",
"StepAP214_GroupItem",
"StepAP214_HArray1OfApprovalItem",
"StepAP214_HArray1OfAutoDesignDateAndPersonItem",
"StepAP214_HArray1OfAutoDesignDateAndTimeItem",
"StepAP214_HArray1OfAutoDesignDatedItem",
"StepAP214_HArray1OfAutoDesignGeneralOrgItem",
"StepAP214_HArray1OfAutoDesignGroupedItem",
"StepAP214_HArray1OfAutoDesignPresentedItemSelect",
"StepAP214_HArray1OfAutoDesignReferencingItem",
"StepAP214_HArray1OfDateAndTimeItem",
"StepAP214_HArray1OfDateItem",
"StepAP214_HArray1OfDocumentReferenceItem",
"StepAP214_HArray1OfExternalIdentificationItem",
"StepAP214_HArray1OfGroupItem",
"StepAP214_HArray1OfOrganizationItem",
"StepAP214_HArray1OfPersonAndOrganizationItem",
"StepAP214_HArray1OfPresentedItemSelect",
"StepAP214_HArray1OfSecurityClassificationItem",
"StepAP214_OrganizationItem",
"StepAP214_PersonAndOrganizationItem",
"StepAP214_PresentedItemSelect",
"StepAP214_Protocol",
"StepAP214_RepItemGroup",
"StepAP214_SecurityClassificationItem"
]
class StepAP214():
    """
    Complete AP214 CC1 , Revision 4 Upgrading from Revision 2 to Revision 4 : 26 Mar 1997 Splitting in sub-schemas : 5 Nov 1997
    """
    @staticmethod
    def Protocol_s() -> StepAP214_Protocol: 
        """
        creates a Protocol
        """
    def __init__(self) -> None: ...
    pass
class StepAP214_AppliedApprovalAssignment(OCP.StepBasic.StepBasic_ApprovalAssignment, OCP.Standard.Standard_Transient):
    def AssignedApproval(self) -> OCP.StepBasic.StepBasic_Approval: 
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
    def Init(self,aAssignedApproval : OCP.StepBasic.StepBasic_Approval,aItems : StepAP214_HArray1OfApprovalItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfApprovalItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_ApprovalItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetAssignedApproval(self,aAssignedApproval : OCP.StepBasic.StepBasic_Approval) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfApprovalItem) -> None: 
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
class StepAP214_AppliedDateAndTimeAssignment(OCP.StepBasic.StepBasic_DateAndTimeAssignment, OCP.Standard.Standard_Transient):
    def AssignedDateAndTime(self) -> OCP.StepBasic.StepBasic_DateAndTime: 
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
    def Init(self,aAssignedDateAndTime : OCP.StepBasic.StepBasic_DateAndTime,aRole : OCP.StepBasic.StepBasic_DateTimeRole,aItems : StepAP214_HArray1OfDateAndTimeItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfDateAndTimeItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_DateAndTimeItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_DateTimeRole: 
        """
        None
        """
    def SetAssignedDateAndTime(self,aAssignedDateAndTime : OCP.StepBasic.StepBasic_DateAndTime) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfDateAndTimeItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_DateTimeRole) -> None: 
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
class StepAP214_AppliedDateAssignment(OCP.StepBasic.StepBasic_DateAssignment, OCP.Standard.Standard_Transient):
    def AssignedDate(self) -> OCP.StepBasic.StepBasic_Date: 
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
    def Init(self,aAssignedDate : OCP.StepBasic.StepBasic_Date,aRole : OCP.StepBasic.StepBasic_DateRole,aItems : StepAP214_HArray1OfDateItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfDateItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_DateItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_DateRole: 
        """
        None
        """
    def SetAssignedDate(self,aAssignedDate : OCP.StepBasic.StepBasic_Date) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfDateItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_DateRole) -> None: 
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
class StepAP214_AppliedDocumentReference(OCP.StepBasic.StepBasic_DocumentReference, OCP.Standard.Standard_Transient):
    def AssignedDocument(self) -> OCP.StepBasic.StepBasic_Document: 
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
    def Init(self,aAssignedDocument : OCP.StepBasic.StepBasic_Document,aSource : OCP.TCollection.TCollection_HAsciiString,aItems : StepAP214_HArray1OfDocumentReferenceItem) -> None: 
        """
        None
        """
    def Init0(self,aAssignedDocument : OCP.StepBasic.StepBasic_Document,aSource : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfDocumentReferenceItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_DocumentReferenceItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetAssignedDocument(self,aAssignedDocument : OCP.StepBasic.StepBasic_Document) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfDocumentReferenceItem) -> None: 
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
class StepAP214_AppliedExternalIdentificationAssignment(OCP.StepBasic.StepBasic_ExternalIdentificationAssignment, OCP.StepBasic.StepBasic_IdentificationAssignment, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity AppliedExternalIdentificationAssignmentRepresentation of STEP entity AppliedExternalIdentificationAssignmentRepresentation of STEP entity AppliedExternalIdentificationAssignment
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
    def Init(self,aIdentificationAssignment_AssignedId : OCP.TCollection.TCollection_HAsciiString,aIdentificationAssignment_Role : OCP.StepBasic.StepBasic_IdentificationRole,aExternalIdentificationAssignment_Source : OCP.StepBasic.StepBasic_ExternalSource,aItems : StepAP214_HArray1OfExternalIdentificationItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfExternalIdentificationItem: 
        """
        Returns field Items
        """
    def Role(self) -> OCP.StepBasic.StepBasic_IdentificationRole: 
        """
        Returns field Role
        """
    def SetAssignedId(self,AssignedId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field AssignedId
        """
    def SetItems(self,Items : StepAP214_HArray1OfExternalIdentificationItem) -> None: 
        """
        Set field Items
        """
    def SetRole(self,Role : OCP.StepBasic.StepBasic_IdentificationRole) -> None: 
        """
        Set field Role
        """
    def SetSource(self,Source : OCP.StepBasic.StepBasic_ExternalSource) -> None: 
        """
        Set field Source
        """
    def Source(self) -> OCP.StepBasic.StepBasic_ExternalSource: 
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
class StepAP214_AppliedGroupAssignment(OCP.StepBasic.StepBasic_GroupAssignment, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity AppliedGroupAssignmentRepresentation of STEP entity AppliedGroupAssignmentRepresentation of STEP entity AppliedGroupAssignment
    """
    def AssignedGroup(self) -> OCP.StepBasic.StepBasic_Group: 
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
    def Init(self,aGroupAssignment_AssignedGroup : OCP.StepBasic.StepBasic_Group,aItems : StepAP214_HArray1OfGroupItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfGroupItem: 
        """
        Returns field Items
        """
    def SetAssignedGroup(self,AssignedGroup : OCP.StepBasic.StepBasic_Group) -> None: 
        """
        Set field AssignedGroup
        """
    def SetItems(self,Items : StepAP214_HArray1OfGroupItem) -> None: 
        """
        Set field Items
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
class StepAP214_AppliedOrganizationAssignment(OCP.StepBasic.StepBasic_OrganizationAssignment, OCP.Standard.Standard_Transient):
    def AssignedOrganization(self) -> OCP.StepBasic.StepBasic_Organization: 
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
    def Init(self,aAssignedOrganization : OCP.StepBasic.StepBasic_Organization,aRole : OCP.StepBasic.StepBasic_OrganizationRole,aItems : StepAP214_HArray1OfOrganizationItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfOrganizationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_OrganizationItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_OrganizationRole: 
        """
        None
        """
    def SetAssignedOrganization(self,aAssignedOrganization : OCP.StepBasic.StepBasic_Organization) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfOrganizationItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_OrganizationRole) -> None: 
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
class StepAP214_AppliedPersonAndOrganizationAssignment(OCP.StepBasic.StepBasic_PersonAndOrganizationAssignment, OCP.Standard.Standard_Transient):
    def AssignedPersonAndOrganization(self) -> OCP.StepBasic.StepBasic_PersonAndOrganization: 
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
    def Init(self,aAssignedPersonAndOrganization : OCP.StepBasic.StepBasic_PersonAndOrganization,aRole : OCP.StepBasic.StepBasic_PersonAndOrganizationRole,aItems : StepAP214_HArray1OfPersonAndOrganizationItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfPersonAndOrganizationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_PersonAndOrganizationItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_PersonAndOrganizationRole: 
        """
        None
        """
    def SetAssignedPersonAndOrganization(self,aAssignedPersonAndOrganization : OCP.StepBasic.StepBasic_PersonAndOrganization) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfPersonAndOrganizationItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_PersonAndOrganizationRole) -> None: 
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
class StepAP214_AppliedPresentedItem(OCP.StepVisual.StepVisual_PresentedItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aItems : StepAP214_HArray1OfPresentedItemSelect) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfPresentedItemSelect: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_PresentedItemSelect: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfPresentedItemSelect) -> None: 
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
class StepAP214_AppliedSecurityClassificationAssignment(OCP.StepBasic.StepBasic_SecurityClassificationAssignment, OCP.Standard.Standard_Transient):
    def AssignedSecurityClassification(self) -> OCP.StepBasic.StepBasic_SecurityClassification: 
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
    def Init(self,aAssignedSecurityClassification : OCP.StepBasic.StepBasic_SecurityClassification,aItems : StepAP214_HArray1OfSecurityClassificationItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfSecurityClassificationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_SecurityClassificationItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetAssignedSecurityClassification(self,aAssignedSecurityClassification : OCP.StepBasic.StepBasic_SecurityClassification) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfSecurityClassificationItem) -> None: 
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
class StepAP214_ApprovalItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AssemblyComponentUsageSubstitute(self) -> OCP.StepRepr.StepRepr_AssemblyComponentUsageSubstitute: 
        """
        returns Value as a AssemblyComponentUsageSubstitute (Null if another type)
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
        Recognizes a ApprovalItem Kind Entity that is : 1 -> AssemblyComponentUsageSubstitute 2 -> DocumentFile 3 -> MaterialDesignation 4 -> MechanicalDesignGeometricPresentationRepresentation 5 -> PresentationArea 6 -> Product 7 -> ProductDefinition 8 -> ProductDefinitionFormation 9 -> ProductDefinitionRelationship 10 -> PropertyDefinition 11 -> ShapeRepresentation 12 -> SecurityClassification 13 -> ConfigurationItem 14 -> Date 15 -> Document 16 -> Effectivity 17 -> Group 18 -> GroupRelationship 19 -> ProductDefinitionFormationRelationship 20 -> Representation 21 -> ShapeAspectRelationship 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def ConfigurationItem(self) -> OCP.StepRepr.StepRepr_ConfigurationItem: 
        """
        returns Value as a ConfigurationItem (Null if another type)
        """
    def Date(self) -> OCP.StepBasic.StepBasic_Date: 
        """
        returns Value as a Date (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Document(self) -> OCP.StepBasic.StepBasic_Document: 
        """
        returns Value as a Document (Null if another type)
        """
    def DocumentFile(self) -> OCP.StepBasic.StepBasic_DocumentFile: 
        """
        returns Value as a DocumentFile (Null if another type)
        """
    def Effectivity(self) -> OCP.StepBasic.StepBasic_Effectivity: 
        """
        returns Value as a Effectivity (Null if another type)
        """
    def Group(self) -> OCP.StepBasic.StepBasic_Group: 
        """
        returns Value as a Group (Null if another type)
        """
    def GroupRelationship(self) -> OCP.StepBasic.StepBasic_GroupRelationship: 
        """
        returns Value as a GroupRelationship (Null if another type)
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
    def MaterialDesignation(self) -> OCP.StepRepr.StepRepr_MaterialDesignation: 
        """
        returns Value as a MaterialDesignation (Null if another type)
        """
    def MechanicalDesignGeometricPresentationRepresentation(self) -> OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation: 
        """
        returns Value as a MechanicalDesignGeometricPresentationRepresentation (Null if another type)
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
    def PresentationArea(self) -> OCP.StepVisual.StepVisual_PresentationArea: 
        """
        returns Value as a PresentationArea (Null if another type)
        """
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        returns Value as a Product (Null if another type)
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        returns Value as a ProductDefinitionFormation (Null if another type)
        """
    def ProductDefinitionFormationRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormationRelationship: 
        """
        returns Value as a ProductDefinitionFormationRelationship (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as aProductDefinitionRelationship (Null if another type)
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
    def SecurityClassification(self) -> OCP.StepBasic.StepBasic_SecurityClassification: 
        """
        returns Value as a SecurityClassification (Null if another type)
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
    def ShapeAspectRelationship(self) -> OCP.StepRepr.StepRepr_ShapeAspectRelationship: 
        """
        returns Value as a ShapeAspectRelationship (Null if another type)
        """
    def ShapeRepresentation(self) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        returns Value as a ShapeRepresentation (Null if another type)
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
class StepAP214_Array1OfApprovalItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfApprovalItem) -> StepAP214_Array1OfApprovalItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_ApprovalItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_ApprovalItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_ApprovalItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_ApprovalItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_ApprovalItem) -> None: 
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
    def Last(self) -> StepAP214_ApprovalItem: 
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
    def Move(self,theOther : StepAP214_Array1OfApprovalItem) -> StepAP214_Array1OfApprovalItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_ApprovalItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_ApprovalItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfApprovalItem) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_ApprovalItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfAutoDesignDateAndPersonItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignDateAndPersonItem) -> StepAP214_Array1OfAutoDesignDateAndPersonItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignDateAndPersonItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignDateAndPersonItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignDateAndPersonItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_AutoDesignDateAndPersonItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_AutoDesignDateAndPersonItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignDateAndPersonItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignDateAndPersonItem) -> StepAP214_Array1OfAutoDesignDateAndPersonItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignDateAndPersonItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignDateAndPersonItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignDateAndPersonItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_AutoDesignDateAndPersonItem,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfAutoDesignDateAndTimeItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignDateAndTimeItem) -> StepAP214_Array1OfAutoDesignDateAndTimeItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_AutoDesignDateAndTimeItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignDateAndTimeItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignDateAndTimeItem) -> StepAP214_Array1OfAutoDesignDateAndTimeItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignDateAndTimeItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepAP214_AutoDesignDateAndTimeItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignDateAndTimeItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfAutoDesignDatedItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignDatedItem) -> StepAP214_Array1OfAutoDesignDatedItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignDatedItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignDatedItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignDatedItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_AutoDesignDatedItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_AutoDesignDatedItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignDatedItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignDatedItem) -> StepAP214_Array1OfAutoDesignDatedItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignDatedItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignDatedItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepAP214_AutoDesignDatedItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignDatedItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfAutoDesignGeneralOrgItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignGeneralOrgItem) -> StepAP214_Array1OfAutoDesignGeneralOrgItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_AutoDesignGeneralOrgItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignGeneralOrgItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignGeneralOrgItem) -> StepAP214_Array1OfAutoDesignGeneralOrgItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignGeneralOrgItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_AutoDesignGeneralOrgItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignGeneralOrgItem) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfAutoDesignGroupedItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignGroupedItem) -> StepAP214_Array1OfAutoDesignGroupedItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignGroupedItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignGroupedItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignGroupedItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_AutoDesignGroupedItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_AutoDesignGroupedItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignGroupedItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignGroupedItem) -> StepAP214_Array1OfAutoDesignGroupedItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignGroupedItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignGroupedItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignGroupedItem) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_AutoDesignGroupedItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfAutoDesignPresentedItemSelect():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignPresentedItemSelect) -> StepAP214_Array1OfAutoDesignPresentedItemSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignPresentedItemSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignPresentedItemSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignPresentedItemSelect: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_AutoDesignPresentedItemSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_AutoDesignPresentedItemSelect) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignPresentedItemSelect: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignPresentedItemSelect) -> StepAP214_Array1OfAutoDesignPresentedItemSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignPresentedItemSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignPresentedItemSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_AutoDesignPresentedItemSelect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignPresentedItemSelect) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfAutoDesignReferencingItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignReferencingItem) -> StepAP214_Array1OfAutoDesignReferencingItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignReferencingItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignReferencingItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignReferencingItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_AutoDesignReferencingItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_AutoDesignReferencingItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignReferencingItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignReferencingItem) -> StepAP214_Array1OfAutoDesignReferencingItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignReferencingItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignReferencingItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_AutoDesignReferencingItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignReferencingItem) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfDateAndTimeItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfDateAndTimeItem) -> StepAP214_Array1OfDateAndTimeItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_DateAndTimeItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_DateAndTimeItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_DateAndTimeItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_DateAndTimeItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_DateAndTimeItem) -> None: 
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
    def Last(self) -> StepAP214_DateAndTimeItem: 
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
    def Move(self,theOther : StepAP214_Array1OfDateAndTimeItem) -> StepAP214_Array1OfDateAndTimeItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_DateAndTimeItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_DateAndTimeItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfDateAndTimeItem) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_DateAndTimeItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfDateItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfDateItem) -> StepAP214_Array1OfDateItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_DateItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_DateItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_DateItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_DateItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_DateItem) -> None: 
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
    def Last(self) -> StepAP214_DateItem: 
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
    def Move(self,theOther : StepAP214_Array1OfDateItem) -> StepAP214_Array1OfDateItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_DateItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_DateItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepAP214_DateItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfDateItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfDocumentReferenceItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfDocumentReferenceItem) -> StepAP214_Array1OfDocumentReferenceItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_DocumentReferenceItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_DocumentReferenceItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_DocumentReferenceItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_DocumentReferenceItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_DocumentReferenceItem) -> None: 
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
    def Last(self) -> StepAP214_DocumentReferenceItem: 
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
    def Move(self,theOther : StepAP214_Array1OfDocumentReferenceItem) -> StepAP214_Array1OfDocumentReferenceItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_DocumentReferenceItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_DocumentReferenceItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfDocumentReferenceItem) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_DocumentReferenceItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfExternalIdentificationItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfExternalIdentificationItem) -> StepAP214_Array1OfExternalIdentificationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_ExternalIdentificationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_ExternalIdentificationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_ExternalIdentificationItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_ExternalIdentificationItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_ExternalIdentificationItem) -> None: 
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
    def Last(self) -> StepAP214_ExternalIdentificationItem: 
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
    def Move(self,theOther : StepAP214_Array1OfExternalIdentificationItem) -> StepAP214_Array1OfExternalIdentificationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_ExternalIdentificationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_ExternalIdentificationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepAP214_Array1OfExternalIdentificationItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_ExternalIdentificationItem,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfGroupItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfGroupItem) -> StepAP214_Array1OfGroupItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_GroupItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_GroupItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_GroupItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_GroupItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_GroupItem) -> None: 
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
    def Last(self) -> StepAP214_GroupItem: 
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
    def Move(self,theOther : StepAP214_Array1OfGroupItem) -> StepAP214_Array1OfGroupItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_GroupItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_GroupItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfGroupItem) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_GroupItem,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfOrganizationItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfOrganizationItem) -> StepAP214_Array1OfOrganizationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_OrganizationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_OrganizationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_OrganizationItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_OrganizationItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_OrganizationItem) -> None: 
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
    def Last(self) -> StepAP214_OrganizationItem: 
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
    def Move(self,theOther : StepAP214_Array1OfOrganizationItem) -> StepAP214_Array1OfOrganizationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_OrganizationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_OrganizationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfOrganizationItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_OrganizationItem,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfPersonAndOrganizationItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfPersonAndOrganizationItem) -> StepAP214_Array1OfPersonAndOrganizationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_PersonAndOrganizationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_PersonAndOrganizationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_PersonAndOrganizationItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_PersonAndOrganizationItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_PersonAndOrganizationItem) -> None: 
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
    def Last(self) -> StepAP214_PersonAndOrganizationItem: 
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
    def Move(self,theOther : StepAP214_Array1OfPersonAndOrganizationItem) -> StepAP214_Array1OfPersonAndOrganizationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_PersonAndOrganizationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_PersonAndOrganizationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_PersonAndOrganizationItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfPersonAndOrganizationItem) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfPresentedItemSelect():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfPresentedItemSelect) -> StepAP214_Array1OfPresentedItemSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_PresentedItemSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_PresentedItemSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_PresentedItemSelect: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_PresentedItemSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_PresentedItemSelect) -> None: 
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
    def Last(self) -> StepAP214_PresentedItemSelect: 
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
    def Move(self,theOther : StepAP214_Array1OfPresentedItemSelect) -> StepAP214_Array1OfPresentedItemSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_PresentedItemSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_PresentedItemSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepAP214_Array1OfPresentedItemSelect) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_PresentedItemSelect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_Array1OfSecurityClassificationItem():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepAP214_Array1OfSecurityClassificationItem) -> StepAP214_Array1OfSecurityClassificationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepAP214_SecurityClassificationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_SecurityClassificationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_SecurityClassificationItem: 
        """
        Variable value access
        """
    def First(self) -> StepAP214_SecurityClassificationItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepAP214_SecurityClassificationItem) -> None: 
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
    def Last(self) -> StepAP214_SecurityClassificationItem: 
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
    def Move(self,theOther : StepAP214_Array1OfSecurityClassificationItem) -> StepAP214_Array1OfSecurityClassificationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_SecurityClassificationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_SecurityClassificationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepAP214_SecurityClassificationItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfSecurityClassificationItem) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepAP214_AutoDesignActualDateAndTimeAssignment(OCP.StepBasic.StepBasic_DateAndTimeAssignment, OCP.Standard.Standard_Transient):
    def AssignedDateAndTime(self) -> OCP.StepBasic.StepBasic_DateAndTime: 
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
    def Init(self,aAssignedDateAndTime : OCP.StepBasic.StepBasic_DateAndTime,aRole : OCP.StepBasic.StepBasic_DateTimeRole,aItems : StepAP214_HArray1OfAutoDesignDateAndTimeItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignDateAndTimeItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_DateTimeRole: 
        """
        None
        """
    def SetAssignedDateAndTime(self,aAssignedDateAndTime : OCP.StepBasic.StepBasic_DateAndTime) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignDateAndTimeItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_DateTimeRole) -> None: 
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
class StepAP214_AutoDesignActualDateAssignment(OCP.StepBasic.StepBasic_DateAssignment, OCP.Standard.Standard_Transient):
    def AssignedDate(self) -> OCP.StepBasic.StepBasic_Date: 
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
    def Init(self,aAssignedDate : OCP.StepBasic.StepBasic_Date,aRole : OCP.StepBasic.StepBasic_DateRole,aItems : StepAP214_HArray1OfAutoDesignDatedItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignDatedItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignDatedItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_DateRole: 
        """
        None
        """
    def SetAssignedDate(self,aAssignedDate : OCP.StepBasic.StepBasic_Date) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignDatedItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_DateRole) -> None: 
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
class StepAP214_AutoDesignApprovalAssignment(OCP.StepBasic.StepBasic_ApprovalAssignment, OCP.Standard.Standard_Transient):
    def AssignedApproval(self) -> OCP.StepBasic.StepBasic_Approval: 
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
    def Init(self,aAssignedApproval : OCP.StepBasic.StepBasic_Approval,aItems : StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignGeneralOrgItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetAssignedApproval(self,aAssignedApproval : OCP.StepBasic.StepBasic_Approval) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: 
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
class StepAP214_AutoDesignDateAndPersonAssignment(OCP.StepBasic.StepBasic_PersonAndOrganizationAssignment, OCP.Standard.Standard_Transient):
    def AssignedPersonAndOrganization(self) -> OCP.StepBasic.StepBasic_PersonAndOrganization: 
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
    def Init(self,aAssignedPersonAndOrganization : OCP.StepBasic.StepBasic_PersonAndOrganization,aRole : OCP.StepBasic.StepBasic_PersonAndOrganizationRole,aItems : StepAP214_HArray1OfAutoDesignDateAndPersonItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignDateAndPersonItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignDateAndPersonItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_PersonAndOrganizationRole: 
        """
        None
        """
    def SetAssignedPersonAndOrganization(self,aAssignedPersonAndOrganization : OCP.StepBasic.StepBasic_PersonAndOrganization) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignDateAndPersonItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_PersonAndOrganizationRole) -> None: 
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
class StepAP214_AutoDesignDateAndPersonItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AutoDesignDocumentReference(self) -> StepAP214_AutoDesignDocumentReference: 
        """
        None
        """
    def AutoDesignOrganizationAssignment(self) -> StepAP214_AutoDesignOrganizationAssignment: 
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
        Recognizes a AutoDesignDateAndPersonItem Kind Entity that is : 1 AutoDesignOrganizationAssignment from StepAP214, 2 Product from StepBasic, 3 ProductDefinition from StepBasic, 4 ProductDefinitionFormation from StepBasic, 5 Representation from StepRepr, 6 AutoDesignDocumentReference from StepAP214, 7 ExternallyDefinedRepresentation from StepRepr, 8 ProductDefinitionRelationship from StepBasic, 9 ProductDefinitionWithAssociatedDocuments from StepBasic 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def ExternallyDefinedRepresentation(self) -> OCP.StepRepr.StepRepr_ExternallyDefinedRepresentation: 
        """
        None
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
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        None
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        None
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        None
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        None
        """
    def ProductDefinitionWithAssociatedDocuments(self) -> OCP.StepBasic.StepBasic_ProductDefinitionWithAssociatedDocuments: 
        """
        None
        """
    def Real(self) -> float: 
        """
        None
        """
    def Representation(self) -> OCP.StepRepr.StepRepr_Representation: 
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
class StepAP214_AutoDesignDateAndTimeItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def ApprovalPersonOrganization(self) -> OCP.StepBasic.StepBasic_ApprovalPersonOrganization: 
        """
        returns Value as a ApprovalPersonOrganization (Null if another type)
        """
    def AutoDesignDateAndPersonAssignment(self) -> StepAP214_AutoDesignDateAndPersonAssignment: 
        """
        returns Value as a AutoDesignDateAndPersonAssignment (Null if another type)
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
        Recognizes a AutoDesignDateAndTimeItem Kind Entity that is : 1 -> ApprovalPersonOrganization 2 -> AutoDesignDateAndPersonAssignment 0 else
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
    def ProductDefinitionEffectivity(self) -> OCP.StepBasic.StepBasic_ProductDefinitionEffectivity: 
        """
        None
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
class StepAP214_AutoDesignDatedItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def ApprovalPersonOrganization(self) -> OCP.StepBasic.StepBasic_ApprovalPersonOrganization: 
        """
        returns Value as a ApprovalPersonOrganization (Null if another type)
        """
    def AutoDesignDateAndPersonAssignment(self) -> StepAP214_AutoDesignDateAndPersonAssignment: 
        """
        returns Value as a AutoDesignDateAndPersonAssignment (Null if another type)
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
        Recognizes a AutoDesignDatedItem Kind Entity that is : 1 -> ApprovalPersonOrganization 2 -> AutoDesignDateAndPersonAssignment 0 else
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
    def ProductDefinitionEffectivity(self) -> OCP.StepBasic.StepBasic_ProductDefinitionEffectivity: 
        """
        returns Value as a ProductDefinitionEffectivity
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
class StepAP214_AutoDesignDocumentReference(OCP.StepBasic.StepBasic_DocumentReference, OCP.Standard.Standard_Transient):
    def AssignedDocument(self) -> OCP.StepBasic.StepBasic_Document: 
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
    def Init(self,aAssignedDocument : OCP.StepBasic.StepBasic_Document,aSource : OCP.TCollection.TCollection_HAsciiString,aItems : StepAP214_HArray1OfAutoDesignReferencingItem) -> None: 
        """
        None
        """
    def Init0(self,aAssignedDocument : OCP.StepBasic.StepBasic_Document,aSource : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignReferencingItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignReferencingItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetAssignedDocument(self,aAssignedDocument : OCP.StepBasic.StepBasic_Document) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignReferencingItem) -> None: 
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
class StepAP214_AutoDesignGeneralOrgItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AutoDesignDocumentReference(self) -> StepAP214_AutoDesignDocumentReference: 
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
        Recognizes a AutoDesignGeneralOrgItem Kind Entity that is : 1 Product from StepBasic, 2 ProductDefinition from StepBasic, 3 ProductDefinitionFormation from StepBasic, 4 ProductDefinitionRelationship from StepBasic, 5 ProductDefinitionWithAssociatedDocuments from StepBasic, 6 Representation from StepRepr 7 ExternallyDefinedRepresentation from StepRepr, 8 AutoDesignDocumentReference from StepAP214, 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def ExternallyDefinedRepresentation(self) -> OCP.StepRepr.StepRepr_ExternallyDefinedRepresentation: 
        """
        returns Value as a Representation (Null if another type)
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
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        returns Value as a Product (Null if another type)
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        returns Value as a ProductDefinitionFormation (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as a ProductDefinitionRelationship (Null if another type)
        """
    def ProductDefinitionWithAssociatedDocuments(self) -> OCP.StepBasic.StepBasic_ProductDefinitionWithAssociatedDocuments: 
        """
        returns Value as a ProductDefinitionWithAssociatedDocuments (Null if another type)
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
class StepAP214_AutoDesignGroupAssignment(OCP.StepBasic.StepBasic_GroupAssignment, OCP.Standard.Standard_Transient):
    def AssignedGroup(self) -> OCP.StepBasic.StepBasic_Group: 
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
    def Init(self,aAssignedGroup : OCP.StepBasic.StepBasic_Group,aItems : StepAP214_HArray1OfAutoDesignGroupedItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignGroupedItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignGroupedItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetAssignedGroup(self,AssignedGroup : OCP.StepBasic.StepBasic_Group) -> None: 
        """
        Set field AssignedGroup
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignGroupedItem) -> None: 
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
class StepAP214_AutoDesignGroupedItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AdvancedBrepShapeRepresentation(self) -> OCP.StepShape.StepShape_AdvancedBrepShapeRepresentation: 
        """
        returns Value as a AdvancedBrepShapeRepresentation (Null if another type)
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
        Recognizes a AutoDesignGroupedItem Kind Entity that is : 1 -> AdvancedBrepShapeRepresentation 2 -> CsgShapeRepresentation 3 -> FacetedBrepShapeRepresentation 4 -> GeometricallyBoundedSurfaceShapeRepresentation 5 -> GeometricallyBoundedWireframeShapeRepresentation 6 -> ManifoldSurfaceShapeRepresentation 7 -> Representation 8 -> RepresentationItem 9 -> ShapeAspect 10 -> ShapeRepresentation 11 -> TemplateInstance 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CsgShapeRepresentation(self) -> OCP.StepShape.StepShape_CsgShapeRepresentation: 
        """
        returns Value as a CsgShapeRepresentation (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def FacetedBrepShapeRepresentation(self) -> OCP.StepShape.StepShape_FacetedBrepShapeRepresentation: 
        """
        returns Value as a FacetedBrepShapeRepresentation (Null if another type)
        """
    def GeometricallyBoundedSurfaceShapeRepresentation(self) -> OCP.StepShape.StepShape_GeometricallyBoundedSurfaceShapeRepresentation: 
        """
        returns Value as a GeometricallyBoundedSurfaceShapeRepresentation (Null if another type)
        """
    def GeometricallyBoundedWireframeShapeRepresentation(self) -> OCP.StepShape.StepShape_GeometricallyBoundedWireframeShapeRepresentation: 
        """
        returns Value as a GeometricallyBoundedWireframeShapeRepresentation (Null if another type)
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
    def ManifoldSurfaceShapeRepresentation(self) -> OCP.StepShape.StepShape_ManifoldSurfaceShapeRepresentation: 
        """
        returns Value as a ManifoldSurfaceShapeRepresentation (Null if another type)
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
    def Representation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        returns Value as a Representation (Null if another type)
        """
    def RepresentationItem(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        returns Value as a RepresentationItem (Null if another type)
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
    def ShapeRepresentation(self) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        returns Value as a ShapeRepresentation (Null if another type)
        """
    def TemplateInstance(self) -> OCP.StepVisual.StepVisual_TemplateInstance: 
        """
        returns Value as a TemplateInstance (Null if another type)
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
class StepAP214_AutoDesignNominalDateAndTimeAssignment(OCP.StepBasic.StepBasic_DateAndTimeAssignment, OCP.Standard.Standard_Transient):
    def AssignedDateAndTime(self) -> OCP.StepBasic.StepBasic_DateAndTime: 
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
    def Init(self,aAssignedDateAndTime : OCP.StepBasic.StepBasic_DateAndTime,aRole : OCP.StepBasic.StepBasic_DateTimeRole,aItems : StepAP214_HArray1OfAutoDesignDateAndTimeItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignDateAndTimeItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_DateTimeRole: 
        """
        None
        """
    def SetAssignedDateAndTime(self,aAssignedDateAndTime : OCP.StepBasic.StepBasic_DateAndTime) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignDateAndTimeItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_DateTimeRole) -> None: 
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
class StepAP214_AutoDesignNominalDateAssignment(OCP.StepBasic.StepBasic_DateAssignment, OCP.Standard.Standard_Transient):
    def AssignedDate(self) -> OCP.StepBasic.StepBasic_Date: 
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
    def Init(self,aAssignedDate : OCP.StepBasic.StepBasic_Date,aRole : OCP.StepBasic.StepBasic_DateRole,aItems : StepAP214_HArray1OfAutoDesignDatedItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignDatedItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignDatedItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_DateRole: 
        """
        None
        """
    def SetAssignedDate(self,aAssignedDate : OCP.StepBasic.StepBasic_Date) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignDatedItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_DateRole) -> None: 
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
class StepAP214_AutoDesignOrganizationAssignment(OCP.StepBasic.StepBasic_OrganizationAssignment, OCP.Standard.Standard_Transient):
    def AssignedOrganization(self) -> OCP.StepBasic.StepBasic_Organization: 
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
    def Init(self,aAssignedOrganization : OCP.StepBasic.StepBasic_Organization,aRole : OCP.StepBasic.StepBasic_OrganizationRole,aItems : StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignGeneralOrgItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_OrganizationRole: 
        """
        None
        """
    def SetAssignedOrganization(self,aAssignedOrganization : OCP.StepBasic.StepBasic_Organization) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_OrganizationRole) -> None: 
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
class StepAP214_AutoDesignOrganizationItem(StepAP214_AutoDesignGeneralOrgItem, OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AutoDesignDocumentReference(self) -> StepAP214_AutoDesignDocumentReference: 
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
        None
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Document(self) -> OCP.StepBasic.StepBasic_Document: 
        """
        None
        """
    def ExternallyDefinedRepresentation(self) -> OCP.StepRepr.StepRepr_ExternallyDefinedRepresentation: 
        """
        returns Value as a Representation (Null if another type)
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
    def PhysicallyModeledProductDefinition(self) -> OCP.StepBasic.StepBasic_PhysicallyModeledProductDefinition: 
        """
        None
        """
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        returns Value as a Product (Null if another type)
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        returns Value as a ProductDefinitionFormation (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as a ProductDefinitionRelationship (Null if another type)
        """
    def ProductDefinitionWithAssociatedDocuments(self) -> OCP.StepBasic.StepBasic_ProductDefinitionWithAssociatedDocuments: 
        """
        returns Value as a ProductDefinitionWithAssociatedDocuments (Null if another type)
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
class StepAP214_AutoDesignPersonAndOrganizationAssignment(OCP.StepBasic.StepBasic_PersonAndOrganizationAssignment, OCP.Standard.Standard_Transient):
    def AssignedPersonAndOrganization(self) -> OCP.StepBasic.StepBasic_PersonAndOrganization: 
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
    def Init(self,aAssignedPersonAndOrganization : OCP.StepBasic.StepBasic_PersonAndOrganization,aRole : OCP.StepBasic.StepBasic_PersonAndOrganizationRole,aItems : StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignGeneralOrgItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def Role(self) -> OCP.StepBasic.StepBasic_PersonAndOrganizationRole: 
        """
        None
        """
    def SetAssignedPersonAndOrganization(self,aAssignedPersonAndOrganization : OCP.StepBasic.StepBasic_PersonAndOrganization) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: 
        """
        None
        """
    def SetRole(self,aRole : OCP.StepBasic.StepBasic_PersonAndOrganizationRole) -> None: 
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
class StepAP214_AutoDesignPresentedItem(OCP.StepVisual.StepVisual_PresentedItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aItems : StepAP214_HArray1OfAutoDesignPresentedItemSelect) -> None: 
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
    def Items(self) -> StepAP214_HArray1OfAutoDesignPresentedItemSelect: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepAP214_AutoDesignPresentedItemSelect: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetItems(self,aItems : StepAP214_HArray1OfAutoDesignPresentedItemSelect) -> None: 
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
class StepAP214_AutoDesignPresentedItemSelect(OCP.StepData.StepData_SelectType):
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
        Recognizes a AutoDesignPresentedItemSelect Kind Entity that is : 1 -> ProductDefinition, 2 -> ProductDefinitionRelationship, 3 -> ProductDefinitionShape 4 -> RepresentationRelationship 5 -> ShapeAspect 6 -> DocumentRelationship, 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DocumentRelationship(self) -> OCP.StepBasic.StepBasic_DocumentRelationship: 
        """
        returns Value as a DocumentRelationship (Null if another type)
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
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as a ProductDefinitionRelationship (Null if another type)
        """
    def ProductDefinitionShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
        """
        returns Value as a ProductDefinitionShape (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def RepresentationRelationship(self) -> OCP.StepRepr.StepRepr_RepresentationRelationship: 
        """
        returns Value as a RepresentationRelationship (Null if another type)
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
class StepAP214_AutoDesignReferencingItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Approval(self) -> OCP.StepBasic.StepBasic_Approval: 
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
        Recognizes a AutoDesignReferencingItem Kind Entity that is : 1 Approval from StepBasic, 2 DocumentRelationship from StepBasic, 3 ExternallyDefinedRepresentation from StepRepr, 4 MappedItem from StepRepr, 5 MaterialDesignation from StepRepr, 6 PresentationArea from StepVisual, 7 PresentationView from StepVisual, 8 ProductCategory from StepBasic, 9 ProductDefinition from StepBasic, 10 ProductDefinitionRelationship from StepBasic, 11 PropertyDefinition from StepBasic, 12 Representation from StepRepr, 13 RepresentationRelationship from StepRepr, 14 ShapeAspect from StepRepr 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DocumentRelationship(self) -> OCP.StepBasic.StepBasic_DocumentRelationship: 
        """
        None
        """
    def ExternallyDefinedRepresentation(self) -> OCP.StepRepr.StepRepr_ExternallyDefinedRepresentation: 
        """
        None
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
    def MappedItem(self) -> OCP.StepRepr.StepRepr_MappedItem: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def MaterialDesignation(self) -> OCP.StepRepr.StepRepr_MaterialDesignation: 
        """
        None
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
    def PresentationArea(self) -> OCP.StepVisual.StepVisual_PresentationArea: 
        """
        None
        """
    def PresentationView(self) -> OCP.StepVisual.StepVisual_PresentationView: 
        """
        None
        """
    def ProductCategory(self) -> OCP.StepBasic.StepBasic_ProductCategory: 
        """
        None
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        None
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        None
        """
    def PropertyDefinition(self) -> OCP.StepRepr.StepRepr_PropertyDefinition: 
        """
        None
        """
    def Real(self) -> float: 
        """
        None
        """
    def Representation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        None
        """
    def RepresentationRelationship(self) -> OCP.StepRepr.StepRepr_RepresentationRelationship: 
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
        None
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
class StepAP214_AutoDesignSecurityClassificationAssignment(OCP.StepBasic.StepBasic_SecurityClassificationAssignment, OCP.Standard.Standard_Transient):
    def AssignedSecurityClassification(self) -> OCP.StepBasic.StepBasic_SecurityClassification: 
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
    def Init(self,aAssignedSecurityClassification : OCP.StepBasic.StepBasic_SecurityClassification,aItems : OCP.StepBasic.StepBasic_HArray1OfApproval) -> None: 
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
    def Items(self) -> OCP.StepBasic.StepBasic_HArray1OfApproval: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepBasic.StepBasic_Approval: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetAssignedSecurityClassification(self,aAssignedSecurityClassification : OCP.StepBasic.StepBasic_SecurityClassification) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepBasic.StepBasic_HArray1OfApproval) -> None: 
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
class StepAP214_Class(OCP.StepBasic.StepBasic_Group, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ClassRepresentation of STEP entity ClassRepresentation of STEP entity Class
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
class StepAP214_DateAndTimeItem(StepAP214_ApprovalItem, OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: 
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """
    def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment: 
        """
        returns Value as a AppliedDateAndPersonAssignment (Null if another type)
        """
    def ApprovalPersonOrganization(self) -> OCP.StepBasic.StepBasic_ApprovalPersonOrganization: 
        """
        returns Value as a ApprovalPersonOrganization (Null if another type)
        """
    def AssemblyComponentUsageSubstitute(self) -> OCP.StepRepr.StepRepr_AssemblyComponentUsageSubstitute: 
        """
        returns Value as a AssemblyComponentUsageSubstitute (Null if another type)
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
        Recognizes a DateAndTimeItem Kind Entity that is : 1 -> ApprovalPersonOrganization 2 -> AppliedDateAndPersonAssignment 3 -> AppliedOrganizationAssignment 4 -> AssemblyComponentUsageSubstitute 5 -> DocumentFile 6 -> Effectivity 7 -> MaterialDesignation 8 -> MechanicalDesignGeometricPresentationRepresentation 9 -> PresentationArea 10 -> Product 11 -> ProductDefinition 12 -> ProductDefinitionFormation 13 -> ProductDefinitionRelationship 14 -> PropertyDefinition 15 -> ShapeRepresentation 16 -> SecurityClassification 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def ConfigurationItem(self) -> OCP.StepRepr.StepRepr_ConfigurationItem: 
        """
        returns Value as a ConfigurationItem (Null if another type)
        """
    def Date(self) -> OCP.StepBasic.StepBasic_Date: 
        """
        returns Value as a Date (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Document(self) -> OCP.StepBasic.StepBasic_Document: 
        """
        returns Value as a Document (Null if another type)
        """
    def DocumentFile(self) -> OCP.StepBasic.StepBasic_DocumentFile: 
        """
        returns Value as a DocumentFile (Null if another type)
        """
    def Effectivity(self) -> OCP.StepBasic.StepBasic_Effectivity: 
        """
        returns Value as a Effectivity (Null if another type)
        """
    def Group(self) -> OCP.StepBasic.StepBasic_Group: 
        """
        returns Value as a Group (Null if another type)
        """
    def GroupRelationship(self) -> OCP.StepBasic.StepBasic_GroupRelationship: 
        """
        returns Value as a GroupRelationship (Null if another type)
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
    def MaterialDesignation(self) -> OCP.StepRepr.StepRepr_MaterialDesignation: 
        """
        returns Value as a MaterialDesignation (Null if another type)
        """
    def MechanicalDesignGeometricPresentationRepresentation(self) -> OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation: 
        """
        returns Value as a MechanicalDesignGeometricPresentationRepresentation (Null if another type)
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
    def PresentationArea(self) -> OCP.StepVisual.StepVisual_PresentationArea: 
        """
        returns Value as a PresentationArea (Null if another type)
        """
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        returns Value as a Product (Null if another type)
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        returns Value as a ProductDefinitionFormation (Null if another type)
        """
    def ProductDefinitionFormationRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormationRelationship: 
        """
        returns Value as a ProductDefinitionFormationRelationship (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as aProductDefinitionRelationship (Null if another type)
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
    def SecurityClassification(self) -> OCP.StepBasic.StepBasic_SecurityClassification: 
        """
        returns Value as a SecurityClassification (Null if another type)
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
    def ShapeAspectRelationship(self) -> OCP.StepRepr.StepRepr_ShapeAspectRelationship: 
        """
        returns Value as a ShapeAspectRelationship (Null if another type)
        """
    def ShapeRepresentation(self) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        returns Value as a ShapeRepresentation (Null if another type)
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
class StepAP214_DateItem(StepAP214_ApprovalItem, OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: 
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """
    def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment: 
        """
        returns Value as a AppliedDateAndPersonAssignment (Null if another type)
        """
    def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment: 
        """
        returns Value as a AppliedSecurityClassificationAssignment (Null if another type)
        """
    def ApprovalPersonOrganization(self) -> OCP.StepBasic.StepBasic_ApprovalPersonOrganization: 
        """
        returns Value as a ApprovalPersonOrganization (Null if another type)
        """
    def AssemblyComponentUsageSubstitute(self) -> OCP.StepRepr.StepRepr_AssemblyComponentUsageSubstitute: 
        """
        returns Value as a AssemblyComponentUsageSubstitute (Null if another type)
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
        Recognizes a DateItem Kind Entity that is : 1 -> ApprovalPersonOrganization 2 -> AppliedDateAndPersonAssignment 3 -> AppliedOrganizationAssignment 4 -> AssemblyComponentUsageSubstitute 5 -> DocumentFile 6 -> Effectivity 7 -> MaterialDesignation 8 -> MechanicalDesignGeometricPresentationRepresentation 9 -> PresentationArea 10 -> Product 11 -> ProductDefinition 12 -> ProductDefinitionFormation 13 -> ProductDefinitionRelationship 14 -> PropertyDefinition 15 -> ShapeRepresentation 16 -> AppliedSecurityClassificationAssignment 17 -> Document 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def ConfigurationItem(self) -> OCP.StepRepr.StepRepr_ConfigurationItem: 
        """
        returns Value as a ConfigurationItem (Null if another type)
        """
    def Date(self) -> OCP.StepBasic.StepBasic_Date: 
        """
        returns Value as a Date (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Document(self) -> OCP.StepBasic.StepBasic_Document: 
        """
        returns Value as a Document (Null if another type)
        """
    def DocumentFile(self) -> OCP.StepBasic.StepBasic_DocumentFile: 
        """
        returns Value as a DocumentFile (Null if another type)
        """
    def Effectivity(self) -> OCP.StepBasic.StepBasic_Effectivity: 
        """
        returns Value as a Effectivity (Null if another type)
        """
    def Group(self) -> OCP.StepBasic.StepBasic_Group: 
        """
        returns Value as a Group (Null if another type)
        """
    def GroupRelationship(self) -> OCP.StepBasic.StepBasic_GroupRelationship: 
        """
        returns Value as a GroupRelationship (Null if another type)
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
    def MaterialDesignation(self) -> OCP.StepRepr.StepRepr_MaterialDesignation: 
        """
        returns Value as a MaterialDesignation (Null if another type)
        """
    def MechanicalDesignGeometricPresentationRepresentation(self) -> OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation: 
        """
        returns Value as a MechanicalDesignGeometricPresentationRepresentation (Null if another type)
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
    def PresentationArea(self) -> OCP.StepVisual.StepVisual_PresentationArea: 
        """
        returns Value as a PresentationArea (Null if another type)
        """
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        returns Value as a Product (Null if another type)
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        returns Value as a ProductDefinitionFormation (Null if another type)
        """
    def ProductDefinitionFormationRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormationRelationship: 
        """
        returns Value as a ProductDefinitionFormationRelationship (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as aProductDefinitionRelationship (Null if another type)
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
    def SecurityClassification(self) -> OCP.StepBasic.StepBasic_SecurityClassification: 
        """
        returns Value as a SecurityClassification (Null if another type)
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
    def ShapeAspectRelationship(self) -> OCP.StepRepr.StepRepr_ShapeAspectRelationship: 
        """
        returns Value as a ShapeAspectRelationship (Null if another type)
        """
    def ShapeRepresentation(self) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        returns Value as a ShapeRepresentation (Null if another type)
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
class StepAP214_DocumentReferenceItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AppliedExternalIdentificationAssignment(self) -> StepAP214_AppliedExternalIdentificationAssignment: 
        """
        returns Value as a AppliedExternalIdentificationAssignment (Null if another type)
        """
    def Approval(self) -> OCP.StepBasic.StepBasic_Approval: 
        """
        returns Value as a Approval (Null if another type)
        """
    def AssemblyComponentUsage(self) -> OCP.StepRepr.StepRepr_AssemblyComponentUsage: 
        """
        returns Value as a AssemblyComponentUsage (Null if another type)
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
        Recognizes a DocumentReferenceItem Kind Entity that is :
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CharacterizedObject(self) -> OCP.StepBasic.StepBasic_CharacterizedObject: 
        """
        returns Value as a CharacterizedObject (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DescriptiveRepresentationItem(self) -> OCP.StepRepr.StepRepr_DescriptiveRepresentationItem: 
        """
        returns Value as a (Null if another type)
        """
    def DimensionalSize(self) -> OCP.StepShape.StepShape_DimensionalSize: 
        """
        returns Value as a DimensionalSize (Null if another type)
        """
    def ExternallyDefinedItem(self) -> OCP.StepBasic.StepBasic_ExternallyDefinedItem: 
        """
        returns Value as a ExternallyDefinedItem (Null if another type)
        """
    def Group(self) -> OCP.StepBasic.StepBasic_Group: 
        """
        returns Value as a Group (Null if another type)
        """
    def GroupRelationship(self) -> OCP.StepBasic.StepBasic_GroupRelationship: 
        """
        returns Value as a GroupRelationship (Null if another type)
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
    def MaterialDesignation(self) -> OCP.StepRepr.StepRepr_MaterialDesignation: 
        """
        returns Value as a MaterialDesignation (Null if another type)
        """
    def MeasureRepresentationItem(self) -> OCP.StepRepr.StepRepr_MeasureRepresentationItem: 
        """
        returns Value as a MeasureRepresentationItem (Null if another type)
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
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionContext(self) -> OCP.StepBasic.StepBasic_ProductDefinitionContext: 
        """
        returns Value as a ProductDefinitionContext (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as aProductDefinitionRelationship (Null if another type)
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
    def RepresentationItem(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        returns Value as a RepresentationItem (Null if another type)
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
class StepAP214_ExternalIdentificationItem(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type ExternalIdentificationItem
    """
    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: 
        """
        Returns Value as AppliedOrganizationAssignment (or Null if another type)
        """
    def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment: 
        """
        Returns Value as AppliedPersonAndOrganizationAssignment (or Null if another type)
        """
    def Approval(self) -> OCP.StepBasic.StepBasic_Approval: 
        """
        Returns Value as Approval (or Null if another type)
        """
    def ApprovalStatus(self) -> OCP.StepBasic.StepBasic_ApprovalStatus: 
        """
        Returns Value as ApprovalStatus (or Null if another type)
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
        Recognizes a kind of ExternalIdentificationItem select type 1 -> DocumentFile from StepBasic 2 -> ExternallyDefinedClass from StepAP214 3 -> ExternallyDefinedGeneralProperty from StepAP214 4 -> ProductDefinition from StepBasic 5 -> AppliedOrganizationAssignment from AP214 6 -> AppliedPersonAndOrganizationAssignment from AP214 7 -> Approval from StepBasic 8 -> ApprovalStatus from StepBasic 9 -> ExternalSource from StepBasic 10 -> OrganizationalAddress from StepBasic 11 -> SecurityClassification from StepBasic 12 -> TrimmedCurve from StepGeom 13 -> VersionedActionRequest from StepBasic 14 -> DateAndTimeAssignment from StepBasic 15 -> DateAssignment from StepBasic 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def DateAndTimeAssignment(self) -> OCP.StepBasic.StepBasic_DateAndTimeAssignment: 
        """
        Returns Value as DateAndTimeAssignment (or Null if another type)
        """
    def DateAssignment(self) -> OCP.StepBasic.StepBasic_DateAssignment: 
        """
        Returns Value as DateAssignment (or Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DocumentFile(self) -> OCP.StepBasic.StepBasic_DocumentFile: 
        """
        Returns Value as DocumentFile (or Null if another type)
        """
    def ExternalSource(self) -> OCP.StepBasic.StepBasic_ExternalSource: 
        """
        Returns Value as ExternalSource (or Null if another type)
        """
    def ExternallyDefinedClass(self) -> StepAP214_ExternallyDefinedClass: 
        """
        Returns Value as ExternallyDefinedClass (or Null if another type)
        """
    def ExternallyDefinedGeneralProperty(self) -> StepAP214_ExternallyDefinedGeneralProperty: 
        """
        Returns Value as ExternallyDefinedGeneralProperty (or Null if another type)
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
    def OrganizationalAddress(self) -> OCP.StepBasic.StepBasic_OrganizationalAddress: 
        """
        Returns Value as OrganizationalAddress (or Null if another type)
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns Value as ProductDefinition (or Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def SecurityClassification(self) -> OCP.StepBasic.StepBasic_SecurityClassification: 
        """
        Returns Value as SecurityClassification (or Null if another type)
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
    def TrimmedCurve(self) -> OCP.StepGeom.StepGeom_TrimmedCurve: 
        """
        Returns Value as TrimmedCurve (or Null if another type)
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def VersionedActionRequest(self) -> OCP.StepBasic.StepBasic_VersionedActionRequest: 
        """
        Returns Value as VersionedActionRequest (or Null if another type)
        """
    def __init__(self) -> None: ...
    pass
class StepAP214_ExternallyDefinedClass(StepAP214_Class, OCP.StepBasic.StepBasic_Group, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ExternallyDefinedClassRepresentation of STEP entity ExternallyDefinedClassRepresentation of STEP entity ExternallyDefinedClass
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
    def ExternallyDefinedItem(self) -> OCP.StepBasic.StepBasic_ExternallyDefinedItem: 
        """
        Returns data for supertype ExternallyDefinedItem
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
    def Init(self,aGroup_Name : OCP.TCollection.TCollection_HAsciiString,hasGroup_Description : bool,aGroup_Description : OCP.TCollection.TCollection_HAsciiString,aExternallyDefinedItem_ItemId : OCP.StepBasic.StepBasic_SourceItem,aExternallyDefinedItem_Source : OCP.StepBasic.StepBasic_ExternalSource) -> None: 
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
    def SetExternallyDefinedItem(self,ExternallyDefinedItem : OCP.StepBasic.StepBasic_ExternallyDefinedItem) -> None: 
        """
        Set data for supertype ExternallyDefinedItem
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
class StepAP214_ExternallyDefinedGeneralProperty(OCP.StepBasic.StepBasic_GeneralProperty, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ExternallyDefinedGeneralPropertyRepresentation of STEP entity ExternallyDefinedGeneralPropertyRepresentation of STEP entity ExternallyDefinedGeneralProperty
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
    def ExternallyDefinedItem(self) -> OCP.StepBasic.StepBasic_ExternallyDefinedItem: 
        """
        Returns data for supertype ExternallyDefinedItem
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
    def Init(self,aGeneralProperty_Id : OCP.TCollection.TCollection_HAsciiString,aGeneralProperty_Name : OCP.TCollection.TCollection_HAsciiString,hasGeneralProperty_Description : bool,aGeneralProperty_Description : OCP.TCollection.TCollection_HAsciiString,aExternallyDefinedItem_ItemId : OCP.StepBasic.StepBasic_SourceItem,aExternallyDefinedItem_Source : OCP.StepBasic.StepBasic_ExternalSource) -> None: 
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
    def SetExternallyDefinedItem(self,ExternallyDefinedItem : OCP.StepBasic.StepBasic_ExternallyDefinedItem) -> None: 
        """
        Set data for supertype ExternallyDefinedItem
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
class StepAP214_GroupItem(OCP.StepData.StepData_SelectType):
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
        Recognizes a GroupItem Kind Entity that is : 1 -> GeometricRepresentationItem 2 -> GroupRelationship 3 -> MappedItem 4 -> ProductDefinition 5 -> ProductDefinitionFormation 6 -> PropertyDefinitionRepresentation 7 -> Representation 8 -> RepresentationItem 9 -> RepresentationRelationshipWithTransformation 10 -> ShapeAspect 11 -> ShapeAspectRelationship 12 -> ShapeRepresentationRelationship 13 -> StyledItem 14 -> TopologicalRepresentationItem 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def GeometricRepresentationItem(self) -> OCP.StepGeom.StepGeom_GeometricRepresentationItem: 
        """
        returns Value as a GeometricRepresentationItem (Null if another type)
        """
    def GroupRelationship(self) -> OCP.StepBasic.StepBasic_GroupRelationship: 
        """
        returns Value as a GroupRelationship (Null if another type)
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
    def MappedItem(self) -> OCP.StepRepr.StepRepr_MappedItem: 
        """
        returns Value as a MappedItem (Null if another type)
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
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        returns Value as a ProductDefinitionFormation (Null if another type)
        """
    def PropertyDefinitionRepresentation(self) -> OCP.StepRepr.StepRepr_PropertyDefinitionRepresentation: 
        """
        returns Value as a PropertyDefinitionRepresentation (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def Representation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        returns Value as a Representation (Null if another type)
        """
    def RepresentationItem(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        returns Value as a RepresentationItem (Null if another type)
        """
    def RepresentationRelationshipWithTransformation(self) -> OCP.StepRepr.StepRepr_RepresentationRelationshipWithTransformation: 
        """
        returns Value as a RepresentationRelationshipWithTransformation (Null if another type)
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
    def ShapeRepresentationRelationship(self) -> OCP.StepRepr.StepRepr_ShapeRepresentationRelationship: 
        """
        returns Value as a ShapeRepresentationRelationship (Null if another type)
        """
    def StyledItem(self) -> OCP.StepVisual.StepVisual_StyledItem: 
        """
        returns Value as a StyledItem (Null if another type)
        """
    def TopologicalRepresentationItem(self) -> OCP.StepShape.StepShape_TopologicalRepresentationItem: 
        """
        returns Value as a TopologicalRepresentationItem (Null if another type)
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
class StepAP214_HArray1OfApprovalItem(StepAP214_Array1OfApprovalItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfApprovalItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfApprovalItem) -> StepAP214_Array1OfApprovalItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfApprovalItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_ApprovalItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_ApprovalItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_ApprovalItem: 
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
    def First(self) -> StepAP214_ApprovalItem: 
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
    def Init(self,theValue : StepAP214_ApprovalItem) -> None: 
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
    def Last(self) -> StepAP214_ApprovalItem: 
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
    def Move(self,theOther : StepAP214_Array1OfApprovalItem) -> StepAP214_Array1OfApprovalItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_ApprovalItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_ApprovalItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfApprovalItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_ApprovalItem) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfAutoDesignDateAndPersonItem(StepAP214_Array1OfAutoDesignDateAndPersonItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfAutoDesignDateAndPersonItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignDateAndPersonItem) -> StepAP214_Array1OfAutoDesignDateAndPersonItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfAutoDesignDateAndPersonItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignDateAndPersonItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignDateAndPersonItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignDateAndPersonItem: 
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
    def First(self) -> StepAP214_AutoDesignDateAndPersonItem: 
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
    def Init(self,theValue : StepAP214_AutoDesignDateAndPersonItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignDateAndPersonItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignDateAndPersonItem) -> StepAP214_Array1OfAutoDesignDateAndPersonItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignDateAndPersonItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignDateAndPersonItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignDateAndPersonItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_AutoDesignDateAndPersonItem) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfAutoDesignDateAndTimeItem(StepAP214_Array1OfAutoDesignDateAndTimeItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfAutoDesignDateAndTimeItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignDateAndTimeItem) -> StepAP214_Array1OfAutoDesignDateAndTimeItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfAutoDesignDateAndTimeItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignDateAndTimeItem: 
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
    def First(self) -> StepAP214_AutoDesignDateAndTimeItem: 
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
    def Init(self,theValue : StepAP214_AutoDesignDateAndTimeItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignDateAndTimeItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignDateAndTimeItem) -> StepAP214_Array1OfAutoDesignDateAndTimeItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignDateAndTimeItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignDateAndTimeItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_AutoDesignDateAndTimeItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignDateAndTimeItem) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfAutoDesignDatedItem(StepAP214_Array1OfAutoDesignDatedItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfAutoDesignDatedItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignDatedItem) -> StepAP214_Array1OfAutoDesignDatedItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfAutoDesignDatedItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignDatedItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignDatedItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignDatedItem: 
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
    def First(self) -> StepAP214_AutoDesignDatedItem: 
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
    def Init(self,theValue : StepAP214_AutoDesignDatedItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignDatedItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignDatedItem) -> StepAP214_Array1OfAutoDesignDatedItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignDatedItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignDatedItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_AutoDesignDatedItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignDatedItem) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfAutoDesignGeneralOrgItem(StepAP214_Array1OfAutoDesignGeneralOrgItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfAutoDesignGeneralOrgItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignGeneralOrgItem) -> StepAP214_Array1OfAutoDesignGeneralOrgItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfAutoDesignGeneralOrgItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignGeneralOrgItem: 
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
    def First(self) -> StepAP214_AutoDesignGeneralOrgItem: 
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
    def Init(self,theValue : StepAP214_AutoDesignGeneralOrgItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignGeneralOrgItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignGeneralOrgItem) -> StepAP214_Array1OfAutoDesignGeneralOrgItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignGeneralOrgItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignGeneralOrgItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignGeneralOrgItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_AutoDesignGeneralOrgItem) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfAutoDesignGroupedItem(StepAP214_Array1OfAutoDesignGroupedItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfAutoDesignGroupedItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignGroupedItem) -> StepAP214_Array1OfAutoDesignGroupedItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfAutoDesignGroupedItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignGroupedItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignGroupedItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignGroupedItem: 
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
    def First(self) -> StepAP214_AutoDesignGroupedItem: 
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
    def Init(self,theValue : StepAP214_AutoDesignGroupedItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignGroupedItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignGroupedItem) -> StepAP214_Array1OfAutoDesignGroupedItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignGroupedItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignGroupedItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignGroupedItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_AutoDesignGroupedItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfAutoDesignPresentedItemSelect(StepAP214_Array1OfAutoDesignPresentedItemSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfAutoDesignPresentedItemSelect: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignPresentedItemSelect) -> StepAP214_Array1OfAutoDesignPresentedItemSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfAutoDesignPresentedItemSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignPresentedItemSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignPresentedItemSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignPresentedItemSelect: 
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
    def First(self) -> StepAP214_AutoDesignPresentedItemSelect: 
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
    def Init(self,theValue : StepAP214_AutoDesignPresentedItemSelect) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignPresentedItemSelect: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignPresentedItemSelect) -> StepAP214_Array1OfAutoDesignPresentedItemSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignPresentedItemSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignPresentedItemSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_AutoDesignPresentedItemSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignPresentedItemSelect) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfAutoDesignReferencingItem(StepAP214_Array1OfAutoDesignReferencingItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfAutoDesignReferencingItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfAutoDesignReferencingItem) -> StepAP214_Array1OfAutoDesignReferencingItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfAutoDesignReferencingItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_AutoDesignReferencingItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_AutoDesignReferencingItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_AutoDesignReferencingItem: 
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
    def First(self) -> StepAP214_AutoDesignReferencingItem: 
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
    def Init(self,theValue : StepAP214_AutoDesignReferencingItem) -> None: 
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
    def Last(self) -> StepAP214_AutoDesignReferencingItem: 
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
    def Move(self,theOther : StepAP214_Array1OfAutoDesignReferencingItem) -> StepAP214_Array1OfAutoDesignReferencingItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_AutoDesignReferencingItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_AutoDesignReferencingItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_AutoDesignReferencingItem) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfAutoDesignReferencingItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfDateAndTimeItem(StepAP214_Array1OfDateAndTimeItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfDateAndTimeItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfDateAndTimeItem) -> StepAP214_Array1OfDateAndTimeItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfDateAndTimeItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_DateAndTimeItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_DateAndTimeItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_DateAndTimeItem: 
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
    def First(self) -> StepAP214_DateAndTimeItem: 
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
    def Init(self,theValue : StepAP214_DateAndTimeItem) -> None: 
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
    def Last(self) -> StepAP214_DateAndTimeItem: 
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
    def Move(self,theOther : StepAP214_Array1OfDateAndTimeItem) -> StepAP214_Array1OfDateAndTimeItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_DateAndTimeItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_DateAndTimeItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfDateAndTimeItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_DateAndTimeItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfDateItem(StepAP214_Array1OfDateItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfDateItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfDateItem) -> StepAP214_Array1OfDateItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfDateItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_DateItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_DateItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_DateItem: 
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
    def First(self) -> StepAP214_DateItem: 
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
    def Init(self,theValue : StepAP214_DateItem) -> None: 
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
    def Last(self) -> StepAP214_DateItem: 
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
    def Move(self,theOther : StepAP214_Array1OfDateItem) -> StepAP214_Array1OfDateItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_DateItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_DateItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_DateItem) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfDateItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfDocumentReferenceItem(StepAP214_Array1OfDocumentReferenceItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfDocumentReferenceItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfDocumentReferenceItem) -> StepAP214_Array1OfDocumentReferenceItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfDocumentReferenceItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_DocumentReferenceItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_DocumentReferenceItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_DocumentReferenceItem: 
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
    def First(self) -> StepAP214_DocumentReferenceItem: 
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
    def Init(self,theValue : StepAP214_DocumentReferenceItem) -> None: 
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
    def Last(self) -> StepAP214_DocumentReferenceItem: 
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
    def Move(self,theOther : StepAP214_Array1OfDocumentReferenceItem) -> StepAP214_Array1OfDocumentReferenceItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_DocumentReferenceItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_DocumentReferenceItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfDocumentReferenceItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_DocumentReferenceItem) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfExternalIdentificationItem(StepAP214_Array1OfExternalIdentificationItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfExternalIdentificationItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfExternalIdentificationItem) -> StepAP214_Array1OfExternalIdentificationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfExternalIdentificationItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_ExternalIdentificationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_ExternalIdentificationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_ExternalIdentificationItem: 
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
    def First(self) -> StepAP214_ExternalIdentificationItem: 
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
    def Init(self,theValue : StepAP214_ExternalIdentificationItem) -> None: 
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
    def Last(self) -> StepAP214_ExternalIdentificationItem: 
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
    def Move(self,theOther : StepAP214_Array1OfExternalIdentificationItem) -> StepAP214_Array1OfExternalIdentificationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_ExternalIdentificationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_ExternalIdentificationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_ExternalIdentificationItem) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfExternalIdentificationItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfGroupItem(StepAP214_Array1OfGroupItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfGroupItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfGroupItem) -> StepAP214_Array1OfGroupItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfGroupItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_GroupItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_GroupItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_GroupItem: 
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
    def First(self) -> StepAP214_GroupItem: 
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
    def Init(self,theValue : StepAP214_GroupItem) -> None: 
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
    def Last(self) -> StepAP214_GroupItem: 
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
    def Move(self,theOther : StepAP214_Array1OfGroupItem) -> StepAP214_Array1OfGroupItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_GroupItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_GroupItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepAP214_Array1OfGroupItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_GroupItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfOrganizationItem(StepAP214_Array1OfOrganizationItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfOrganizationItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfOrganizationItem) -> StepAP214_Array1OfOrganizationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfOrganizationItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_OrganizationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_OrganizationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_OrganizationItem: 
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
    def First(self) -> StepAP214_OrganizationItem: 
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
    def Init(self,theValue : StepAP214_OrganizationItem) -> None: 
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
    def Last(self) -> StepAP214_OrganizationItem: 
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
    def Move(self,theOther : StepAP214_Array1OfOrganizationItem) -> StepAP214_Array1OfOrganizationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_OrganizationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_OrganizationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepAP214_Array1OfOrganizationItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_OrganizationItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfPersonAndOrganizationItem(StepAP214_Array1OfPersonAndOrganizationItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfPersonAndOrganizationItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfPersonAndOrganizationItem) -> StepAP214_Array1OfPersonAndOrganizationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfPersonAndOrganizationItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_PersonAndOrganizationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_PersonAndOrganizationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_PersonAndOrganizationItem: 
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
    def First(self) -> StepAP214_PersonAndOrganizationItem: 
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
    def Init(self,theValue : StepAP214_PersonAndOrganizationItem) -> None: 
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
    def Last(self) -> StepAP214_PersonAndOrganizationItem: 
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
    def Move(self,theOther : StepAP214_Array1OfPersonAndOrganizationItem) -> StepAP214_Array1OfPersonAndOrganizationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_PersonAndOrganizationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_PersonAndOrganizationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_PersonAndOrganizationItem) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfPersonAndOrganizationItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfPresentedItemSelect(StepAP214_Array1OfPresentedItemSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfPresentedItemSelect: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfPresentedItemSelect) -> StepAP214_Array1OfPresentedItemSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfPresentedItemSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_PresentedItemSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_PresentedItemSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_PresentedItemSelect: 
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
    def First(self) -> StepAP214_PresentedItemSelect: 
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
    def Init(self,theValue : StepAP214_PresentedItemSelect) -> None: 
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
    def Last(self) -> StepAP214_PresentedItemSelect: 
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
    def Move(self,theOther : StepAP214_Array1OfPresentedItemSelect) -> StepAP214_Array1OfPresentedItemSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_PresentedItemSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_PresentedItemSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfPresentedItemSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_PresentedItemSelect) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_HArray1OfSecurityClassificationItem(StepAP214_Array1OfSecurityClassificationItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepAP214_Array1OfSecurityClassificationItem: 
        """
        None
        """
    def Assign(self,theOther : StepAP214_Array1OfSecurityClassificationItem) -> StepAP214_Array1OfSecurityClassificationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepAP214_Array1OfSecurityClassificationItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepAP214_SecurityClassificationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepAP214_SecurityClassificationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepAP214_SecurityClassificationItem: 
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
    def First(self) -> StepAP214_SecurityClassificationItem: 
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
    def Init(self,theValue : StepAP214_SecurityClassificationItem) -> None: 
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
    def Last(self) -> StepAP214_SecurityClassificationItem: 
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
    def Move(self,theOther : StepAP214_Array1OfSecurityClassificationItem) -> StepAP214_Array1OfSecurityClassificationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepAP214_SecurityClassificationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepAP214_SecurityClassificationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepAP214_Array1OfSecurityClassificationItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepAP214_SecurityClassificationItem) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class StepAP214_OrganizationItem(StepAP214_ApprovalItem, OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: 
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """
    def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment: 
        """
        returns Value as a AppliedSecurityClassificationAssignment (Null if another type)
        """
    def Approval(self) -> OCP.StepBasic.StepBasic_Approval: 
        """
        returns Value as a Approval (Null if another type)
        """
    def AssemblyComponentUsageSubstitute(self) -> OCP.StepRepr.StepRepr_AssemblyComponentUsageSubstitute: 
        """
        returns Value as a AssemblyComponentUsageSubstitute (Null if another type)
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
        Recognizes a OrganizationItem Kind Entity that is :
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def ConfigurationItem(self) -> OCP.StepRepr.StepRepr_ConfigurationItem: 
        """
        returns Value as a ConfigurationItem (Null if another type)
        """
    def Date(self) -> OCP.StepBasic.StepBasic_Date: 
        """
        returns Value as a Date (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Document(self) -> OCP.StepBasic.StepBasic_Document: 
        """
        returns Value as a Document (Null if another type)
        """
    def DocumentFile(self) -> OCP.StepBasic.StepBasic_DocumentFile: 
        """
        returns Value as a DocumentFile (Null if another type)
        """
    def Effectivity(self) -> OCP.StepBasic.StepBasic_Effectivity: 
        """
        returns Value as a Effectivity (Null if another type)
        """
    def Group(self) -> OCP.StepBasic.StepBasic_Group: 
        """
        returns Value as a Group (Null if another type)
        """
    def GroupRelationship(self) -> OCP.StepBasic.StepBasic_GroupRelationship: 
        """
        returns Value as a GroupRelationship (Null if another type)
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
    def MaterialDesignation(self) -> OCP.StepRepr.StepRepr_MaterialDesignation: 
        """
        returns Value as a MaterialDesignation (Null if another type)
        """
    def MechanicalDesignGeometricPresentationRepresentation(self) -> OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation: 
        """
        returns Value as a MechanicalDesignGeometricPresentationRepresentation (Null if another type)
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
    def PresentationArea(self) -> OCP.StepVisual.StepVisual_PresentationArea: 
        """
        returns Value as a PresentationArea (Null if another type)
        """
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        returns Value as a Product (Null if another type)
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        returns Value as a ProductDefinitionFormation (Null if another type)
        """
    def ProductDefinitionFormationRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormationRelationship: 
        """
        returns Value as a ProductDefinitionFormationRelationship (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as aProductDefinitionRelationship (Null if another type)
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
    def SecurityClassification(self) -> OCP.StepBasic.StepBasic_SecurityClassification: 
        """
        returns Value as a SecurityClassification (Null if another type)
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
    def ShapeAspectRelationship(self) -> OCP.StepRepr.StepRepr_ShapeAspectRelationship: 
        """
        returns Value as a ShapeAspectRelationship (Null if another type)
        """
    def ShapeRepresentation(self) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        returns Value as a ShapeRepresentation (Null if another type)
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
class StepAP214_PersonAndOrganizationItem(StepAP214_ApprovalItem, OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: 
        """
        returns Value as a AppliedOrganizationAssignment (Null if another type)
        """
    def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment: 
        """
        returns Value as a AppliedSecurityClassificationAssignment (Null if another type)
        """
    def Approval(self) -> OCP.StepBasic.StepBasic_Approval: 
        """
        returns Value as a Approval (Null if another type)
        """
    def AssemblyComponentUsageSubstitute(self) -> OCP.StepRepr.StepRepr_AssemblyComponentUsageSubstitute: 
        """
        returns Value as a AssemblyComponentUsageSubstitute (Null if another type)
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
        Recognizes a APersonAndOrganizationItem Kind Entity that is : 1 -> AppliedOrganizationAssignment 2 -> AssemblyComponentUsageSubstitute 3 -> DocumentFile 4 -> MaterialDesignation 5 -> MechanicalDesignGeometricPresentationRepresentation 6 -> PresentationArea 7 -> Product 8 -> ProductDefinition 9 -> ProductDefinitionFormation 10 -> ProductDefinitionRelationship 11 -> PropertyDefinition 12 -> ShapeRepresentation 13 -> SecurityClassification 14 -> AppliedSecurityClassificationAssignment 15 -> Approval 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def ConfigurationItem(self) -> OCP.StepRepr.StepRepr_ConfigurationItem: 
        """
        returns Value as a ConfigurationItem (Null if another type)
        """
    def Date(self) -> OCP.StepBasic.StepBasic_Date: 
        """
        returns Value as a Date (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Document(self) -> OCP.StepBasic.StepBasic_Document: 
        """
        returns Value as a Document (Null if another type)
        """
    def DocumentFile(self) -> OCP.StepBasic.StepBasic_DocumentFile: 
        """
        returns Value as a DocumentFile (Null if another type)
        """
    def Effectivity(self) -> OCP.StepBasic.StepBasic_Effectivity: 
        """
        returns Value as a Effectivity (Null if another type)
        """
    def Group(self) -> OCP.StepBasic.StepBasic_Group: 
        """
        returns Value as a Group (Null if another type)
        """
    def GroupRelationship(self) -> OCP.StepBasic.StepBasic_GroupRelationship: 
        """
        returns Value as a GroupRelationship (Null if another type)
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
    def MaterialDesignation(self) -> OCP.StepRepr.StepRepr_MaterialDesignation: 
        """
        returns Value as a MaterialDesignation (Null if another type)
        """
    def MechanicalDesignGeometricPresentationRepresentation(self) -> OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation: 
        """
        returns Value as a MechanicalDesignGeometricPresentationRepresentation (Null if another type)
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
    def PresentationArea(self) -> OCP.StepVisual.StepVisual_PresentationArea: 
        """
        returns Value as a PresentationArea (Null if another type)
        """
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        returns Value as a Product (Null if another type)
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        returns Value as a ProductDefinitionFormation (Null if another type)
        """
    def ProductDefinitionFormationRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormationRelationship: 
        """
        returns Value as a ProductDefinitionFormationRelationship (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as aProductDefinitionRelationship (Null if another type)
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
    def SecurityClassification(self) -> OCP.StepBasic.StepBasic_SecurityClassification: 
        """
        returns Value as a SecurityClassification (Null if another type)
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
    def ShapeAspectRelationship(self) -> OCP.StepRepr.StepRepr_ShapeAspectRelationship: 
        """
        returns Value as a ShapeAspectRelationship (Null if another type)
        """
    def ShapeRepresentation(self) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        returns Value as a ShapeRepresentation (Null if another type)
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
class StepAP214_PresentedItemSelect(OCP.StepData.StepData_SelectType):
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
        Recognizes a PresentedItemSelect Kind Entity that is : 1 -> ProductDefinition, 2 -> ProductDefinitionRelationship, 0 else
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
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as a ProductDefinitionRelationship (Null if another type)
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
class StepAP214_Protocol(OCP.StepData.StepData_Protocol, OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    Protocol for StepAP214 Entities It requires StepAP214 as a ResourceProtocol for StepAP214 Entities It requires StepAP214 as a ResourceProtocol for StepAP214 Entities It requires StepAP214 as a Resource
    """
    @staticmethod
    def Active_s() -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Active Protocol, if defined (else, returns a Null Handle, which means "no defined active protocol")
        """
    def AddBasicDescr(self,esdescr : OCP.StepData.StepData_ESDescr) -> None: 
        """
        Records an ESDescr, intended to build complex descriptions
        """
    def AddDescr(self,adescr : OCP.StepData.StepData_EDescr,CN : int) -> None: 
        """
        Records an EDescr with its case number Also records its name for an ESDescr (simple type): an ESDescr is then used, for case number, or for type name
        """
    def AddPDescr(self,pdescr : OCP.StepData.StepData_PDescr) -> None: 
        """
        Records an PDescr
        """
    def BasicDescr(self,name : str,anylevel : bool=True) -> OCP.StepData.StepData_EDescr: 
        """
        Returns a basic description according to its name <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    def CaseNumber(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns a unique positive number for any recognized entity Redefined to work by calling both TypeNumber and, for a Described Entity (late binding) DescrNumber
        """
    @staticmethod
    def ClearActive_s() -> None: 
        """
        Erases the Active Protocol (hence it becomes undefined)
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Descr(self,num : int) -> OCP.StepData.StepData_EDescr: 
        """
        Returns the description attached to a case number, or null

        Returns a description according to its name <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    @overload
    def Descr(self,name : str,anylevel : bool=True) -> OCP.StepData.StepData_EDescr: ...
    def DescrNumber(self,adescr : OCP.StepData.StepData_EDescr) -> int: 
        """
        Returns a unique positive CaseNumber for types described by an EDescr (late binding) Warning : TypeNumber and DescrNumber must give together a unique positive case number for each distinct case, type or descr
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ECDescr(self,names : OCP.TColStd.TColStd_SequenceOfAsciiString,anylevel : bool=True) -> OCP.StepData.StepData_ECDescr: 
        """
        Returns a complex description according to list of names <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    def ESDescr(self,name : str,anylevel : bool=True) -> OCP.StepData.StepData_ESDescr: 
        """
        Idem as Descr but cast to simple description
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlobalCheck(self,G : OCP.Interface.Interface_Graph,ach : OCP.Interface.Interface_Check) -> bool: 
        """
        Evaluates a Global Check for a model (with its Graph) Returns True when done, False if data in model do not apply
        """
    def HasDescr(self) -> bool: 
        """
        Tells if a Protocol brings at least one ESDescr, i.e. if it defines at least one entity description by ESDescr mechanism
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDynamicType(self,obj : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if type of <obj> is that defined from CDL This is the default but it may change according implementation
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
    def IsSuitableModel(self,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True if <model> is a Model of Step Norm
        """
    def IsUnknownEntity(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e. Type UndefinedEntity, status Unknown
        """
    def NbResources(self) -> int: 
        """
        Returns count of Protocol used as Resources (level one)
        """
    def NbTypes(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the count of DISTINCT types under which an entity may be processed. Each one is candidate to be recognized by TypeNumber, <obj> is then processed according it By default, returns 1 (the DynamicType)
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Creates an empty Model for Step Norm
        """
    def PDescr(self,name : str,anylevel : bool=True) -> OCP.StepData.StepData_PDescr: 
        """
        Returns a parameter description according to its name <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    def Resource(self,num : int) -> OCP.Interface.Interface_Protocol: 
        """
        Returns a Resource, given its rank (between 1 and NbResources)
        """
    def SchemaName(self) -> str: 
        """
        None
        """
    @staticmethod
    def SetActive_s(aprotocol : OCP.Interface.Interface_Protocol) -> None: 
        """
        Sets a given Protocol to be the Active one (for the users of Active, see just above). Applies to every sub-type of Protocol
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self,obj : OCP.Standard.Standard_Transient,nt : int=1) -> OCP.Standard.Standard_Type: 
        """
        Returns a type under which <obj> can be recognized and processed, according its rank in its definition list (see NbTypes). By default, returns DynamicType
        """
    def TypeNumber(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        Returns a Case Number for each of the StepAP214 Entities
        """
    def UnknownEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Creates a new Unknown Entity for Step (UndefinedEntity)
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
class StepAP214_RepItemGroup(OCP.StepBasic.StepBasic_Group, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity RepItemGroupRepresentation of STEP entity RepItemGroupRepresentation of STEP entity RepItemGroup
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
    def Init(self,aGroup_Name : OCP.TCollection.TCollection_HAsciiString,hasGroup_Description : bool,aGroup_Description : OCP.TCollection.TCollection_HAsciiString,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def RepresentationItem(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        Returns data for supertype RepresentationItem
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRepresentationItem(self,RepresentationItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        Set data for supertype RepresentationItem
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
class StepAP214_SecurityClassificationItem(StepAP214_ApprovalItem, OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Action(self) -> OCP.StepBasic.StepBasic_Action: 
        """
        returns Value as a Action (Null if another type)
        """
    def AssemblyComponentUsage(self) -> OCP.StepRepr.StepRepr_AssemblyComponentUsage: 
        """
        returns Value as a AssemblyComponentUsage (Null if another type)
        """
    def AssemblyComponentUsageSubstitute(self) -> OCP.StepRepr.StepRepr_AssemblyComponentUsageSubstitute: 
        """
        returns Value as a AssemblyComponentUsageSubstitute (Null if another type)
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
        Recognizes a SecurityClassificationItem Kind Entity that is : 1 -> Action 2 -> AssemblyComponentUsage 3 -> AssemblyComponentUsageSubstitute 4 -> ConfigurationDesign 5 -> ConfigurationEffectivity 6 -> Document 7 -> DocumentFile 8 -> DraughtingModel 9 -> GeneralProperty 10 -> MakeFromUsageOption 11 -> MaterialDesignation 12 -> MechanicalDesignGeometricPresentationRepresentation 13 -> PresentationArea 14 -> Product 15 -> ProductConcept 16 -> ProductDefinition 17 -> ProductDefinitionFormation 18 -> ProductDefinitionRelationship 19 -> ProductDefinitionUsage 20 -> PropertyDefinition 21 -> ShapeRepresentation 22 -> VersionedActionRequest 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def ConfigurationDesign(self) -> OCP.StepRepr.StepRepr_ConfigurationDesign: 
        """
        returns Value as a ConfigurationDesign (Null if another type)
        """
    def ConfigurationEffectivity(self) -> OCP.StepRepr.StepRepr_ConfigurationEffectivity: 
        """
        returns Value as a ConfigurationEffectivity (Null if another type)
        """
    def ConfigurationItem(self) -> OCP.StepRepr.StepRepr_ConfigurationItem: 
        """
        returns Value as a ConfigurationItem (Null if another type)
        """
    def Date(self) -> OCP.StepBasic.StepBasic_Date: 
        """
        returns Value as a Date (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Document(self) -> OCP.StepBasic.StepBasic_Document: 
        """
        returns Value as a Document (Null if another type)
        """
    def DocumentFile(self) -> OCP.StepBasic.StepBasic_DocumentFile: 
        """
        returns Value as a DocumentFile (Null if another type)
        """
    def DraughtingModel(self) -> OCP.StepVisual.StepVisual_DraughtingModel: 
        """
        returns Value as a DraughtingModel (Null if another type)
        """
    def Effectivity(self) -> OCP.StepBasic.StepBasic_Effectivity: 
        """
        returns Value as a Effectivity (Null if another type)
        """
    def GeneralProperty(self) -> OCP.StepBasic.StepBasic_GeneralProperty: 
        """
        returns Value as a GeneralProperty (Null if another type)
        """
    def Group(self) -> OCP.StepBasic.StepBasic_Group: 
        """
        returns Value as a Group (Null if another type)
        """
    def GroupRelationship(self) -> OCP.StepBasic.StepBasic_GroupRelationship: 
        """
        returns Value as a GroupRelationship (Null if another type)
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
    def MakeFromUsageOption(self) -> OCP.StepRepr.StepRepr_MakeFromUsageOption: 
        """
        returns Value as a MakeFromUsageOption (Null if another type)
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def MaterialDesignation(self) -> OCP.StepRepr.StepRepr_MaterialDesignation: 
        """
        returns Value as a MaterialDesignation (Null if another type)
        """
    def MechanicalDesignGeometricPresentationRepresentation(self) -> OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation: 
        """
        returns Value as a MechanicalDesignGeometricPresentationRepresentation (Null if another type)
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
    def PresentationArea(self) -> OCP.StepVisual.StepVisual_PresentationArea: 
        """
        returns Value as a PresentationArea (Null if another type)
        """
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        returns Value as a Product (Null if another type)
        """
    def ProductConcept(self) -> OCP.StepRepr.StepRepr_ProductConcept: 
        """
        returns Value as a ProductConcept (Null if another type)
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        returns Value as a ProductDefinition (Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        returns Value as a ProductDefinitionFormation (Null if another type)
        """
    def ProductDefinitionFormationRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormationRelationship: 
        """
        returns Value as a ProductDefinitionFormationRelationship (Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        returns Value as aProductDefinitionRelationship (Null if another type)
        """
    def ProductDefinitionUsage(self) -> OCP.StepRepr.StepRepr_ProductDefinitionUsage: 
        """
        returns Value as a ProductDefinitionUsage (Null if another type)
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
    def SecurityClassification(self) -> OCP.StepBasic.StepBasic_SecurityClassification: 
        """
        returns Value as a SecurityClassification (Null if another type)
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
    def ShapeAspectRelationship(self) -> OCP.StepRepr.StepRepr_ShapeAspectRelationship: 
        """
        returns Value as a ShapeAspectRelationship (Null if another type)
        """
    def ShapeRepresentation(self) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        returns Value as a ShapeRepresentation (Null if another type)
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def VersionedActionRequest(self) -> OCP.StepBasic.StepBasic_VersionedActionRequest: 
        """
        returns Value as a VersionedActionRequest (Null if another type)
        """
    def __init__(self) -> None: ...
    pass
