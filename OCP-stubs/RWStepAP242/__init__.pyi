import OCP.RWStepAP242
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepAP242
import OCP.StepData
import OCP.Interface
__all__  = [
"RWStepAP242_RWDraughtingModelItemAssociation",
"RWStepAP242_RWGeometricItemSpecificUsage",
"RWStepAP242_RWIdAttribute",
"RWStepAP242_RWItemIdentifiedRepresentationUsage"
]
class RWStepAP242_RWDraughtingModelItemAssociation():
    """
    Read & Write Module for DraughtingModelItemAssociation
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP242.StepAP242_DraughtingModelItemAssociation) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP242.StepAP242_DraughtingModelItemAssociation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP242.StepAP242_DraughtingModelItemAssociation) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP242_RWGeometricItemSpecificUsage():
    """
    Read & Write Module for GeometricItemSpecificUsage
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP242.StepAP242_GeometricItemSpecificUsage) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP242.StepAP242_GeometricItemSpecificUsage,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP242.StepAP242_GeometricItemSpecificUsage) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP242_RWIdAttribute():
    """
    Read & Write Module for IdAttribute
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP242.StepAP242_IdAttribute) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP242.StepAP242_IdAttribute,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP242.StepAP242_IdAttribute) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepAP242_RWItemIdentifiedRepresentationUsage():
    """
    Read & Write Module for ItemIdentifiedRepresentationUsage
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepAP242.StepAP242_ItemIdentifiedRepresentationUsage) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepAP242.StepAP242_ItemIdentifiedRepresentationUsage,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepAP242.StepAP242_ItemIdentifiedRepresentationUsage) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
