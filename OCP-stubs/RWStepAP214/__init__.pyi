import OCP.RWStepAP214
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepAP214
import OCP.Standard
import OCP.Interface
import OCP.StepData
import OCP.TCollection
import OCP.TColStd
__all__  = [
"RWStepAP214",
"RWStepAP214_GeneralModule",
"RWStepAP214_RWAppliedApprovalAssignment",
"RWStepAP214_RWAppliedDateAndTimeAssignment",
"RWStepAP214_RWAppliedDateAssignment",
"RWStepAP214_RWAppliedDocumentReference",
"RWStepAP214_RWAppliedExternalIdentificationAssignment",
"RWStepAP214_RWAppliedGroupAssignment",
"RWStepAP214_RWAppliedOrganizationAssignment",
"RWStepAP214_RWAppliedPersonAndOrganizationAssignment",
"RWStepAP214_RWAppliedPresentedItem",
"RWStepAP214_RWAppliedSecurityClassificationAssignment",
"RWStepAP214_RWAutoDesignActualDateAndTimeAssignment",
"RWStepAP214_RWAutoDesignActualDateAssignment",
"RWStepAP214_RWAutoDesignApprovalAssignment",
"RWStepAP214_RWAutoDesignDateAndPersonAssignment",
"RWStepAP214_RWAutoDesignDocumentReference",
"RWStepAP214_RWAutoDesignGroupAssignment",
"RWStepAP214_RWAutoDesignNominalDateAndTimeAssignment",
"RWStepAP214_RWAutoDesignNominalDateAssignment",
"RWStepAP214_RWAutoDesignOrganizationAssignment",
"RWStepAP214_RWAutoDesignPersonAndOrganizationAssignment",
"RWStepAP214_RWAutoDesignPresentedItem",
"RWStepAP214_RWAutoDesignSecurityClassificationAssignment",
"RWStepAP214_RWClass",
"RWStepAP214_RWExternallyDefinedClass",
"RWStepAP214_RWExternallyDefinedGeneralProperty",
"RWStepAP214_RWRepItemGroup",
"RWStepAP214_ReadWriteModule"
]
class RWStepAP214():
    """
    None
    """
    @staticmethod
    def Init_s() -> None: 
        """
        enforced the initialisation of the libraries
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_GeneralModule(OCP.StepData.StepData_GeneralModule, OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    Defines General Services for StepAP214 Entities (Share,Check,Copy; Trace already inherited) Depends (for case numbers) of Protocol from StepAP214Defines General Services for StepAP214 Entities (Share,Check,Copy; Trace already inherited) Depends (for case numbers) of Protocol from StepAP214Defines General Services for StepAP214 Entities (Share,Check,Copy; Trace already inherited) Depends (for case numbers) of Protocol from StepAP214
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" Remark that it should be in phase with the implementation of NewVoid+CopyCase/NewCopyCase Default returns always False, can be redefined
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> int: 
        """
        None
        """
    def CheckCase(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Specific Checking of an Entity <ent>
        """
    def CopyCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Copy ("Deep") from <entfrom> to <entto> (same type) by using a CopyTool which provides its working Map. Use method Transferred from CopyTool to work
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Dispatches an entity Returns True if it works by copy, False if it just duplicates the starting Handle
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FillShared(self,model : OCP.Interface.Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific filling of the list of Entities shared by an Entity <ent>, according a Case Number <CN> (formerly computed by CaseNum), considered in the context of a Model <model> Default calls FillSharedCase (i.e., ignores the model) Can be redefined to use the model for working
        """
    def FillSharedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific filling of the list of Entities shared by an Entity <ent>, according to a Case Number <CN> (provided by StepAP214 Protocol).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
    def ListImplied(self,model : OCP.Interface.Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> considered in the context of a Model <model> : i.e. the Entities which are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillShared + ListImplied give the complete list of References Default calls ListImpliedCase (i.e. ignores the model) Can be redefined to use the model for working
        """
    def ListImpliedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> (see above) are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillSharedCase + ListImpliedCase give the complete list of Referenced Entities The provided default method does nothing (Implied References are specific of a little amount of Entity Classes).
        """
    def Name(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of a STEP Entity according to its type
        """
    def NewCopiedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Specific operator (create+copy) defaulted to do nothing. It can be redefined : When it is not possible to work in two steps (NewVoid then CopyCase). This can occur when there is no default constructor : hence the result <entto> must be created with an effective definition. Remark : if NewCopiedCase is defined, CopyCase has nothing to do Returns True if it has produced something, false else
        """
    def NewVoid(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        None
        """
    def RenewImpliedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Copying of Implied References A Default is provided which does nothing (must current case !) Already copied references (by CopyFrom) must remain unchanged Use method Search from CopyTool to work
        """
    def Share(self,iter : OCP.Interface.Interface_EntityIterator,shared : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an Entity to a Shared List (uses GetOneItem on <iter>)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WhenDeleteCase(self,CN : int,ent : OCP.Standard.Standard_Transient,dispatched : bool) -> None: 
        """
        Prepares an entity to be deleted. What does it mean : Basically, any class of entity may define its own destructor By default, it does nothing but calling destructors on fields With the Memory Manager, it is useless to call destructor, it is done automatically when the Handle is nullified(cleared) BUT this is ineffective in looping structures (whatever these are "Implied" references or not).
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
class RWStepAP214_RWAppliedApprovalAssignment():
    """
    Read & Write Module for AppliedApprovalAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedApprovalAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedApprovalAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedApprovalAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAppliedDateAndTimeAssignment():
    """
    Read & Write Module for AppliedDateAndTimeAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedDateAndTimeAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedDateAndTimeAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedDateAndTimeAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAppliedDateAssignment():
    """
    Read & Write Module for AppliedDateAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedDateAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedDateAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedDateAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAppliedDocumentReference():
    """
    Read & Write Module for AppliedDocumentReference
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedDocumentReference) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedDocumentReference,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedDocumentReference) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAppliedExternalIdentificationAssignment():
    """
    Read & Write tool for AppliedExternalIdentificationAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedExternalIdentificationAssignment) -> Any: 
        """
        Reads AppliedExternalIdentificationAssignment
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedExternalIdentificationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedExternalIdentificationAssignment) -> None: 
        """
        Writes AppliedExternalIdentificationAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAppliedGroupAssignment():
    """
    Read & Write tool for AppliedGroupAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedGroupAssignment) -> Any: 
        """
        Reads AppliedGroupAssignment
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedGroupAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedGroupAssignment) -> None: 
        """
        Writes AppliedGroupAssignment
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAppliedOrganizationAssignment():
    """
    Read & Write Module for AppliedOrganizationAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedOrganizationAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedOrganizationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedOrganizationAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAppliedPersonAndOrganizationAssignment():
    """
    Read & Write Module for AppliedPersonAndOrganizationAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedPersonAndOrganizationAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedPersonAndOrganizationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedPersonAndOrganizationAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAppliedPresentedItem():
    """
    Read & Write Module for AppliedPresentedItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedPresentedItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedPresentedItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedPresentedItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAppliedSecurityClassificationAssignment():
    """
    None
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AppliedSecurityClassificationAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AppliedSecurityClassificationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AppliedSecurityClassificationAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignActualDateAndTimeAssignment():
    """
    Read & Write Module for AutoDesignActualDateAndTimeAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignActualDateAndTimeAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignActualDateAndTimeAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignActualDateAndTimeAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignActualDateAssignment():
    """
    Read & Write Module for AutoDesignActualDateAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignActualDateAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignActualDateAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignActualDateAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignApprovalAssignment():
    """
    Read & Write Module for AutoDesignApprovalAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignApprovalAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignApprovalAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignApprovalAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignDateAndPersonAssignment():
    """
    Read & Write Module for AutoDesignDateAndPersonAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignDateAndPersonAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignDateAndPersonAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignDateAndPersonAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignDocumentReference():
    """
    Read & Write Module for AutoDesignDocumentReference
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignDocumentReference) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignDocumentReference,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignDocumentReference) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignGroupAssignment():
    """
    Read & Write Module for AutoDesignGroupAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignGroupAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignGroupAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignGroupAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignNominalDateAndTimeAssignment():
    """
    Read & Write Module for AutoDesignNominalDateAndTimeAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignNominalDateAndTimeAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignNominalDateAndTimeAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignNominalDateAndTimeAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignNominalDateAssignment():
    """
    Read & Write Module for AutoDesignNominalDateAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignNominalDateAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignNominalDateAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignNominalDateAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignOrganizationAssignment():
    """
    Read & Write Module for AutoDesignOrganizationAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignOrganizationAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignOrganizationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignOrganizationAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignPersonAndOrganizationAssignment():
    """
    Read & Write Module for AutoDesignPersonAndOrganizationAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignPersonAndOrganizationAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignPersonAndOrganizationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignPersonAndOrganizationAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignPresentedItem():
    """
    Read & Write Module for AutoDesignPresentedItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignPresentedItem) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignPresentedItem,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignPresentedItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWAutoDesignSecurityClassificationAssignment():
    """
    Read & Write Module for AutoDesignSecurityClassificationAssignment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_AutoDesignSecurityClassificationAssignment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_AutoDesignSecurityClassificationAssignment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_AutoDesignSecurityClassificationAssignment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWClass():
    """
    Read & Write tool for Class
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_Class) -> Any: 
        """
        Reads Class
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_Class,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_Class) -> None: 
        """
        Writes Class
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWExternallyDefinedClass():
    """
    Read & Write tool for ExternallyDefinedClass
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_ExternallyDefinedClass) -> Any: 
        """
        Reads ExternallyDefinedClass
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_ExternallyDefinedClass,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_ExternallyDefinedClass) -> None: 
        """
        Writes ExternallyDefinedClass
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWExternallyDefinedGeneralProperty():
    """
    Read & Write tool for ExternallyDefinedGeneralProperty
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_ExternallyDefinedGeneralProperty) -> Any: 
        """
        Reads ExternallyDefinedGeneralProperty
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_ExternallyDefinedGeneralProperty,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_ExternallyDefinedGeneralProperty) -> None: 
        """
        Writes ExternallyDefinedGeneralProperty
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_RWRepItemGroup():
    """
    Read & Write tool for RepItemGroup
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP214.StepAP214_RepItemGroup) -> Any: 
        """
        Reads RepItemGroup
        """
    def Share(self,ent : OCP.StepAP214.StepAP214_RepItemGroup,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP214.StepAP214_RepItemGroup) -> None: 
        """
        Writes RepItemGroup
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP214_ReadWriteModule(OCP.StepData.StepData_ReadWriteModule, OCP.Interface.Interface_ReaderModule, OCP.Standard.Standard_Transient):
    """
    General module to read and write StepAP214 entitiesGeneral module to read and write StepAP214 entitiesGeneral module to read and write StepAP214 entities
    """
    def CaseNum(self,data : OCP.Interface.Interface_FileReaderData,num : int) -> int: 
        """
        Translate the Type of record <num> in <data> to a positive Case Number, or 0 if failed. Works with a StepReaderData, in which the Type of an Entity is defined as a String : Reads the RecordType <num> then calls CaseNum (this type) Warning : The methods CaseStep, StepType and Recognize, must be in phase (triplets CaseNum-StepType-Type of Object)
        """
    @overload
    def CaseStep(self,types : OCP.TColStd.TColStd_SequenceOfAsciiString) -> int: 
        """
        associates a positive Case Number to each type of StepAP214 entity, given as a String defined in the EXPRESS form

        associates a positive Case Number to each type of StepAP214 Complex entity, given as a String defined in the EXPRESS form
        """
    @overload
    def CaseStep(self,atype : OCP.TCollection.TCollection_AsciiString) -> int: ...
    def ComplexType(self,CN : int,types : OCP.TColStd.TColStd_SequenceOfAsciiString) -> bool: 
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
    def IsComplex(self,CN : int) -> bool: 
        """
        returns True if the Case Number corresponds to a Complex Type
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
    def NewRead(self,casenum : int,data : OCP.Interface.Interface_FileReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific operator (create+read) defaulted to do nothing. It can be redefined when it is not possible to work in two steps (NewVoid then Read). This occurs when no default constructor is defined : hence the result <ent> must be created with an effective definition from the reader. Remark : if NewRead is defined, Copy has nothing to do.
        """
    def Read(self,CN : int,data : OCP.Interface.Interface_FileReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> Any: 
        """
        General Read Function, calls ReadStep
        """
    def ReadStep(self,CN : int,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> Any: 
        """
        None
        """
    def ShortType(self,CN : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Function specific to STEP. Some STEP Types have a short form This method can be redefined to fill it By default, returns an empty string, which is then interpreted to take normal form from StepType
        """
    def StepType(self,CN : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a StepType (defined in EXPRESS form which belongs to a Type of Entity, identified by its CaseNumber determined by Protocol
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteStep(self,CN : int,SW : OCP.StepData.StepData_StepWriter,ent : OCP.Standard.Standard_Transient) -> None: 
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
