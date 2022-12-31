import OCP.StepAP209
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepElement
import OCP.StepBasic
import OCP.StepData
import OCP.STEPConstruct
import OCP.StepFEA
import OCP.Interface
import OCP.XSControl
import OCP.Transfer
import OCP.StepRepr
import OCP.StepShape
__all__  = [
"StepAP209_Construct"
]
class StepAP209_Construct(OCP.STEPConstruct.STEPConstruct_Tool):
    """
    Basic tool for working with AP209 model
    """
    def CreateAP203Structure(self) -> OCP.StepData.StepData_StepModel: 
        """
        Create AP203 structure from existing AP209 structure
        """
    def CreateAdding203Entities(self,PD : OCP.StepBasic.StepBasic_ProductDefinition,aModel : OCP.StepData.StepData_StepModel) -> bool: 
        """
        Create approval.. , date.. , time.. , person.. and organization.. entities for 203 structure
        """
    def CreateAddingEntities(self,AnaPD : OCP.StepBasic.StepBasic_ProductDefinition) -> bool: 
        """
        Create approval.. , date.. , time.. , person.. and organization.. entities for analysis structure
        """
    def CreateAnalysStructure(self,Prod : OCP.StepBasic.StepBasic_Product) -> bool: 
        """
        Create empty structure for idealized_analysis_shape
        """
    def CreateFeaStructure(self,Prod : OCP.StepBasic.StepBasic_Product) -> bool: 
        """
        Create fea structure
        """
    @overload
    def FeaModel(self,PDS : OCP.StepRepr.StepRepr_ProductDefinitionShape) -> OCP.StepFEA.StepFEA_FeaModel: 
        """
        None

        None

        None

        None
        """
    @overload
    def FeaModel(self,PDF : OCP.StepBasic.StepBasic_ProductDefinitionFormation) -> OCP.StepFEA.StepFEA_FeaModel: ...
    @overload
    def FeaModel(self,PD : OCP.StepBasic.StepBasic_ProductDefinition) -> OCP.StepFEA.StepFEA_FeaModel: ...
    @overload
    def FeaModel(self,Prod : OCP.StepBasic.StepBasic_Product) -> OCP.StepFEA.StepFEA_FeaModel: ...
    def FinderProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns FinderProcess (writing; Null if not loaded)

        Returns FinderProcess (writing; Null if not loaded)
        """
    def GetCurElemSection(self,ElemRepr : OCP.StepFEA.StepFEA_Curve3dElementRepresentation) -> OCP.StepElement.StepElement_HSequenceOfCurveElementSectionDefinition: 
        """
        Getting list of curve_element_section_definitions for given element_representation
        """
    def GetElemGeomRelat(self) -> OCP.StepFEA.StepFEA_HSequenceOfElementGeometricRelationship: 
        """
        None
        """
    def GetElementMaterial(self) -> OCP.StepElement.StepElement_HSequenceOfElementMaterial: 
        """
        None
        """
    def GetElements1D(self,theFeaModel : OCP.StepFEA.StepFEA_FeaModel) -> OCP.StepFEA.StepFEA_HSequenceOfElementRepresentation: 
        """
        None
        """
    def GetElements2D(self,theFEAModel : OCP.StepFEA.StepFEA_FeaModel) -> OCP.StepFEA.StepFEA_HSequenceOfElementRepresentation: 
        """
        None
        """
    def GetElements3D(self,theFEAModel : OCP.StepFEA.StepFEA_FeaModel) -> OCP.StepFEA.StepFEA_HSequenceOfElementRepresentation: 
        """
        None
        """
    def GetFeaAxis2Placement3d(self,theFeaModel : OCP.StepFEA.StepFEA_FeaModel) -> OCP.StepFEA.StepFEA_FeaAxis2Placement3d: 
        """
        None
        """
    def GetShReprForElem(self,ElemRepr : OCP.StepFEA.StepFEA_ElementRepresentation) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        None
        """
    @overload
    def Graph(self,recompute : bool=False) -> OCP.Interface.Interface_Graph: 
        """
        Returns current graph (recomputing if necessary)

        Returns current graph (recomputing if necessary)
        """
    @overload
    def Graph(self,recompute : bool) -> OCP.Interface.Interface_Graph: ...
    @overload
    def IdealShape(self,PDF : OCP.StepBasic.StepBasic_ProductDefinitionFormation) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        None

        None

        None

        None
        """
    @overload
    def IdealShape(self,PD : OCP.StepBasic.StepBasic_ProductDefinition) -> OCP.StepShape.StepShape_ShapeRepresentation: ...
    @overload
    def IdealShape(self,PDS : OCP.StepRepr.StepRepr_ProductDefinitionShape) -> OCP.StepShape.StepShape_ShapeRepresentation: ...
    @overload
    def IdealShape(self,Prod : OCP.StepBasic.StepBasic_Product) -> OCP.StepShape.StepShape_ShapeRepresentation: ...
    def Init(self,WS : OCP.XSControl.XSControl_WorkSession) -> bool: 
        """
        Initializes tool; returns True if succeeded
        """
    def IsAnalys(self,PD : OCP.StepBasic.StepBasic_ProductDefinitionFormation) -> bool: 
        """
        None
        """
    def IsDesing(self,PD : OCP.StepBasic.StepBasic_ProductDefinitionFormation) -> bool: 
        """
        None
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns current model (Null if not loaded)

        Returns current model (Null if not loaded)
        """
    @overload
    def NominShape(self,Prod : OCP.StepBasic.StepBasic_Product) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        None

        None
        """
    @overload
    def NominShape(self,PDF : OCP.StepBasic.StepBasic_ProductDefinitionFormation) -> OCP.StepShape.StepShape_ShapeRepresentation: ...
    def ReplaceCcDesingToApplied(self) -> bool: 
        """
        Put into model entities Applied... for AP209 instead of entities CcDesing... from AP203.
        """
    def TransientProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns TransientProcess (reading; Null if not loaded)

        Returns TransientProcess (reading; Null if not loaded)
        """
    def WS(self) -> OCP.XSControl.XSControl_WorkSession: 
        """
        Returns currently loaded WorkSession

        Returns currently loaded WorkSession
        """
    @overload
    def __init__(self,WS : OCP.XSControl.XSControl_WorkSession) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
