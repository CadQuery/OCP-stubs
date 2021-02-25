import OCP.STEPConstruct
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Transfer
import OCP.StepBasic
import OCP.StepAP203
import OCP.StepRepr
import OCP.StepVisual
import OCP.TopoDS
import OCP.StepGeom
import OCP.Standard
import OCP.Quantity
import OCP.TCollection
import OCP.TColStd
import OCP.gp
import OCP.Interface
import OCP.StepShape
import OCP.XSControl
import OCP.TopLoc
import OCP.StepData
__all__  = [
"STEPConstruct",
"STEPConstruct_AP203Context",
"STEPConstruct_Assembly",
"STEPConstruct_ContextTool",
"STEPConstruct_Tool",
"STEPConstruct_Part",
"STEPConstruct_PointHasher",
"STEPConstruct_Styles",
"STEPConstruct_ExternRefs",
"STEPConstruct_UnitContext",
"STEPConstruct_ValidationProps"
]
class STEPConstruct():
    """
    Defines tools for creation and investigation STEP constructs used for representing various kinds of data, such as product and assembly structure, unit contexts, associated information The creation of these structures is made according to currently active schema (AP203 or AP214 CD2 or DIS) This is taken from parameter write.step.schema
    """
    @staticmethod
    def FindCDSR_s(ComponentBinder : OCP.Transfer.Transfer_Binder,AssemblySDR : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,ComponentCDSR : OCP.StepShape.StepShape_ContextDependentShapeRepresentation) -> bool: 
        """
        Find CDSR correcponding to the component in the specified assembly
        """
    @staticmethod
    @overload
    def FindEntity_s(FinderProcess : OCP.Transfer.Transfer_FinderProcess,Shape : OCP.TopoDS.TopoDS_Shape) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        Returns STEP entity of the (sub)type of RepresentationItem which is a result of the tranalation of the Shape, or Null if no result is recorded

        The same as above, but in the case if item not found, repeats search on the same shape without location. The Loc corresponds to the location with which result is found (either location of the Shape, or Null)
        """
    @staticmethod
    @overload
    def FindEntity_s(FinderProcess : OCP.Transfer.Transfer_FinderProcess,Shape : OCP.TopoDS.TopoDS_Shape,Loc : OCP.TopLoc.TopLoc_Location) -> OCP.StepRepr.StepRepr_RepresentationItem: ...
    @staticmethod
    def FindShape_s(TransientProcess : OCP.Transfer.Transfer_TransientProcess,item : OCP.StepRepr.StepRepr_RepresentationItem) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns Shape resulting from given STEP entity (Null if not mapped)
        """
    def __init__(self) -> None: ...
    pass
class STEPConstruct_AP203Context():
    """
    Maintains context specific for AP203 (required data and management information such as persons, dates, approvals etc.) It contains static entities (which can be shared), default values for person and organisation, and also provides tool for creating management entities around specific part (SDR).
    """
    def Clear(self) -> None: 
        """
        Clears all fields describing entities specific to each part
        """
    def DefaultApproval(self) -> OCP.StepBasic.StepBasic_Approval: 
        """
        Returns default approval entity which is used when no other data are available
        """
    def DefaultDateAndTime(self) -> OCP.StepBasic.StepBasic_DateAndTime: 
        """
        Returns default date_and_time entity which is used when no other data are available
        """
    def DefaultPersonAndOrganization(self) -> OCP.StepBasic.StepBasic_PersonAndOrganization: 
        """
        Returns default person_and_organization entity which is used when no other data are available
        """
    def DefaultSecurityClassificationLevel(self) -> OCP.StepBasic.StepBasic_SecurityClassificationLevel: 
        """
        Returns default security_classification_level entity which is used when no other data are available
        """
    def GetApproval(self) -> OCP.StepAP203.StepAP203_CcDesignApproval: 
        """
        None
        """
    def GetApprovalDateTime(self) -> OCP.StepBasic.StepBasic_ApprovalDateTime: 
        """
        None
        """
    def GetApprover(self) -> OCP.StepBasic.StepBasic_ApprovalPersonOrganization: 
        """
        None
        """
    def GetClassificationDate(self) -> OCP.StepAP203.StepAP203_CcDesignDateAndTimeAssignment: 
        """
        None
        """
    def GetClassificationOfficer(self) -> OCP.StepAP203.StepAP203_CcDesignPersonAndOrganizationAssignment: 
        """
        None
        """
    def GetCreationDate(self) -> OCP.StepAP203.StepAP203_CcDesignDateAndTimeAssignment: 
        """
        None
        """
    def GetCreator(self) -> OCP.StepAP203.StepAP203_CcDesignPersonAndOrganizationAssignment: 
        """
        None
        """
    def GetDesignOwner(self) -> OCP.StepAP203.StepAP203_CcDesignPersonAndOrganizationAssignment: 
        """
        None
        """
    def GetDesignSupplier(self) -> OCP.StepAP203.StepAP203_CcDesignPersonAndOrganizationAssignment: 
        """
        None
        """
    def GetProductCategoryRelationship(self) -> OCP.StepBasic.StepBasic_ProductCategoryRelationship: 
        """
        Return entities (roots) instantiated for the part by method Init
        """
    def GetSecurity(self) -> OCP.StepAP203.StepAP203_CcDesignSecurityClassification: 
        """
        None
        """
    @overload
    def Init(self,sdr : OCP.StepShape.StepShape_ShapeDefinitionRepresentation) -> None: 
        """
        Takes SDR (part) which brings all standard data around part (common for AP203 and AP214) and creates all the additional entities required for AP203

        Takes tool which describes standard data around part (common for AP203 and AP214) and creates all the additional entities required for AP203

        Takes NAUO which describes assembly link to component and creates the security_classification entity associated to it as required by the AP203
        """
    @overload
    def Init(self,nauo : OCP.StepRepr.StepRepr_NextAssemblyUsageOccurrence) -> None: ...
    @overload
    def Init(self,SDRTool : STEPConstruct_Part) -> None: ...
    def InitApprovalRequisites(self) -> None: 
        """
        Initializes Approver and ApprovalDateTime entities according to Approval entity
        """
    def InitAssembly(self,nauo : OCP.StepRepr.StepRepr_NextAssemblyUsageOccurrence) -> None: 
        """
        Initializes all missing data which are required for assembly
        """
    def InitRoles(self) -> None: 
        """
        Initializes constant fields (shared entities)
        """
    def InitSecurityRequisites(self) -> None: 
        """
        Initializes ClassificationOfficer and ClassificationDate entities according to Security entity
        """
    def RoleApprover(self) -> OCP.StepBasic.StepBasic_ApprovalRole: 
        """
        Return predefined PersonAndOrganizationRole and DateTimeRole entities named 'creator', 'design owner', 'design supplier', 'classification officer', 'creation date', 'classification date', 'approver'
        """
    def RoleClassificationDate(self) -> OCP.StepBasic.StepBasic_DateTimeRole: 
        """
        None
        """
    def RoleClassificationOfficer(self) -> OCP.StepBasic.StepBasic_PersonAndOrganizationRole: 
        """
        None
        """
    def RoleCreationDate(self) -> OCP.StepBasic.StepBasic_DateTimeRole: 
        """
        None
        """
    def RoleCreator(self) -> OCP.StepBasic.StepBasic_PersonAndOrganizationRole: 
        """
        None
        """
    def RoleDesignOwner(self) -> OCP.StepBasic.StepBasic_PersonAndOrganizationRole: 
        """
        None
        """
    def RoleDesignSupplier(self) -> OCP.StepBasic.StepBasic_PersonAndOrganizationRole: 
        """
        None
        """
    def SetDefaultApproval(self,app : OCP.StepBasic.StepBasic_Approval) -> None: 
        """
        Sets default approval
        """
    def SetDefaultDateAndTime(self,dt : OCP.StepBasic.StepBasic_DateAndTime) -> None: 
        """
        Sets default date_and_time entity
        """
    def SetDefaultPersonAndOrganization(self,po : OCP.StepBasic.StepBasic_PersonAndOrganization) -> None: 
        """
        Sets default person_and_organization entity
        """
    def SetDefaultSecurityClassificationLevel(self,sc : OCP.StepBasic.StepBasic_SecurityClassificationLevel) -> None: 
        """
        Sets default security_classification_level
        """
    def __init__(self) -> None: ...
    pass
class STEPConstruct_Assembly():
    """
    This operator creates and checks an item of an assembly, from its basic data : a ShapeRepresentation, a Location ...
    """
    @staticmethod
    def CheckSRRReversesNAUO_s(theGraph : OCP.Interface.Interface_Graph,CDSR : OCP.StepShape.StepShape_ContextDependentShapeRepresentation) -> bool: 
        """
        Checks whether SRR's definition of assembly and component contradicts with NAUO definition or not, according to model schema (AP214 or AP203)
        """
    def GetNAUO(self) -> OCP.StepRepr.StepRepr_NextAssemblyUsageOccurrence: 
        """
        Returns NAUO object describing the assembly link
        """
    def Init(self,aSR : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,SDR0 : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,Ax0 : OCP.StepGeom.StepGeom_Axis2Placement3d,Loc : OCP.StepGeom.StepGeom_Axis2Placement3d) -> None: 
        """
        Initialises with starting values Ax0 : origin axis (typically, standard XYZ) Loc : location to which place the item Makes a MappedItem Resulting Value is returned by ItemValue
        """
    def ItemLocation(self) -> OCP.StepGeom.StepGeom_Axis2Placement3d: 
        """
        Returns the location of the item, computed from starting aLoc
        """
    def ItemValue(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Value If no Make... has been called, returns the starting SR
        """
    def MakeRelationship(self) -> None: 
        """
        Make a (ShapeRepresentationRelationship,...WithTransformation) Resulting Value is returned by ItemValue
        """
    def __init__(self) -> None: ...
    pass
class STEPConstruct_ContextTool():
    """
    Maintains global context tool for writing. Gives access to Product Definition Context (one per Model) Maintains ApplicationProtocolDefinition entity (common for all products) Also maintains context specific for AP203 and provides set of methods to work with various STEP constructs as required by Actor
    """
    def AP203Context(self) -> STEPConstruct_AP203Context: 
        """
        Returns tool which maintains context specific for AP203
        """
    def AddAPD(self,enforce : bool=False) -> None: 
        """
        None
        """
    def GetACname(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetACschemaName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetACstatus(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetACyear(self) -> int: 
        """
        None
        """
    def GetAPD(self) -> OCP.StepBasic.StepBasic_ApplicationProtocolDefinition: 
        """
        None
        """
    def GetDefaultAxis(self) -> OCP.StepGeom.StepGeom_Axis2Placement3d: 
        """
        Returns a default axis placement
        """
    def GetProductName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Generates a product name basing on write.step.product.name parameter and current position in the assembly structure
        """
    def GetRootsForAssemblyLink(self,assembly : STEPConstruct_Assembly) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Produces and returns a full list of root entities required for assembly link identified by assembly (including NAUO and CDSR)
        """
    def GetRootsForPart(self,SDRTool : STEPConstruct_Part) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Produces and returns a full list of root entities required for part identified by SDRTool (including SDR itself)
        """
    def Index(self) -> int: 
        """
        Returns current index of assembly component on current level
        """
    def IsAP203(self) -> bool: 
        """
        Returns True if APD.schema_name is config_control_design
        """
    def IsAP214(self) -> bool: 
        """
        Returns True if APD.schema_name is automotive_design
        """
    def IsAP242(self) -> bool: 
        """
        Returns True if APD.schema_name is ap242_managed_model_based_3d_engineering
        """
    def Level(self) -> int: 
        """
        Returns current assembly level
        """
    def NextIndex(self) -> None: 
        """
        None
        """
    def NextLevel(self) -> None: 
        """
        None
        """
    def PrevIndex(self) -> None: 
        """
        None
        """
    def PrevLevel(self) -> None: 
        """
        None
        """
    def SetACname(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetACschemaName(self,schemaName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetACstatus(self,status : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetACyear(self,year : int) -> None: 
        """
        None
        """
    def SetIndex(self,ind : int) -> None: 
        """
        Changes current index of assembly component on current level
        """
    def SetLevel(self,lev : int) -> None: 
        """
        Changes current assembly level
        """
    def SetModel(self,aStepModel : OCP.StepData.StepData_StepModel) -> None: 
        """
        Initialize ApplicationProtocolDefinition by the first entity of that type found in the model
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aStepModel : OCP.StepData.StepData_StepModel) -> None: ...
    pass
class STEPConstruct_Tool():
    """
    Provides basic functionalities for tools which are intended for encoding/decoding specific STEP constructs
    """
    def FinderProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns FinderProcess (writing; Null if not loaded)

        Returns FinderProcess (writing; Null if not loaded)
        """
    @overload
    def Graph(self,recompute : bool) -> OCP.Interface.Interface_Graph: 
        """
        Returns current graph (recomputing if necessary)

        Returns current graph (recomputing if necessary)
        """
    @overload
    def Graph(self,recompute : bool=False) -> OCP.Interface.Interface_Graph: ...
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns current model (Null if not loaded)

        Returns current model (Null if not loaded)
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,WS : OCP.XSControl.XSControl_WorkSession) -> None: ...
    pass
class STEPConstruct_Part():
    """
    Provides tools for creating STEP structures associated with part (SDR), such as PRODUCT, PDF etc., as requied by current schema Also allows to investigate and modify this data
    """
    def AC(self) -> OCP.StepBasic.StepBasic_ApplicationContext: 
        """
        None
        """
    def ACapplication(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def MakeSDR(self,aShape : OCP.StepShape.StepShape_ShapeRepresentation,aName : OCP.TCollection.TCollection_HAsciiString,AC : OCP.StepBasic.StepBasic_ApplicationContext) -> None: 
        """
        None
        """
    def PC(self) -> OCP.StepBasic.StepBasic_ProductContext: 
        """
        None
        """
    def PCdisciplineType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PCname(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PD(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        None
        """
    def PDC(self) -> OCP.StepBasic.StepBasic_ProductDefinitionContext: 
        """
        None
        """
    def PDCname(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PDCstage(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PDF(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        None
        """
    def PDFdescription(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PDFid(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PDS(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def PDSdescription(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PDSname(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PDdescription(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PRPC(self) -> OCP.StepBasic.StepBasic_ProductRelatedProductCategory: 
        """
        None
        """
    def PRPCdescription(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def PRPCname(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Pdescription(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Pid(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Pname(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Product(self) -> OCP.StepBasic.StepBasic_Product: 
        """
        None
        """
    def ReadSDR(self,aShape : OCP.StepShape.StepShape_ShapeDefinitionRepresentation) -> None: 
        """
        None
        """
    def SDRValue(self) -> OCP.StepShape.StepShape_ShapeDefinitionRepresentation: 
        """
        Returns SDR or Null if not done
        """
    def SRValue(self) -> OCP.StepShape.StepShape_ShapeRepresentation: 
        """
        Returns SDR->UsedRepresentation() or Null if not done
        """
    def SetACapplication(self,text : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPCdisciplineType(self,label : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPCname(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPDCname(self,label : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPDCstage(self,label : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPDFdescription(self,text : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPDFid(self,id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPDSdescription(self,text : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPDSname(self,label : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPDdescription(self,text : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPRPCdescription(self,text : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPRPCname(self,label : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPdescription(self,text : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPid(self,id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPname(self,label : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class STEPConstruct_PointHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(thePoint : OCP.gp.gp_Pnt,theUpperBound : int) -> int: 
        """
        Computes a hash code for the point, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(Point1 : OCP.gp.gp_Pnt,Point2 : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns True when the two keys are the same. Two same keys must have the same hashcode, the contrary is not necessary.
        """
    def __init__(self) -> None: ...
    pass
class STEPConstruct_Styles(STEPConstruct_Tool):
    """
    Provides a mechanism for reading and writing shape styles (such as color) to and from the STEP file This tool maintains a list of styles, either taking them from STEP model (reading), or filling it by calls to AddStyle or directly (writing). Some methods deal with general structures of styles and presentations in STEP, but there are methods which deal with particular implementation of colors (as described in RP)
    """
    @overload
    def AddStyle(self,item : OCP.StepRepr.StepRepr_RepresentationItem,PSA : OCP.StepVisual.StepVisual_PresentationStyleAssignment,Override : OCP.StepVisual.StepVisual_StyledItem) -> OCP.StepVisual.StepVisual_StyledItem: 
        """
        Adds a style to a sequence

        Create a style linking giving PSA to the item, and add it to the sequence of stored styles. If Override is not Null, then the resulting style will be of the subtype OverridingStyledItem.

        Create a style linking giving PSA to the Shape, and add it to the sequence of stored styles. If Override is not Null, then the resulting style will be of the subtype OverridingStyledItem. The Sape is used to find corresponding STEP entity by call to STEPConstruct::FindEntity(), then previous method is called.
        """
    @overload
    def AddStyle(self,Shape : OCP.TopoDS.TopoDS_Shape,PSA : OCP.StepVisual.StepVisual_PresentationStyleAssignment,Override : OCP.StepVisual.StepVisual_StyledItem) -> OCP.StepVisual.StepVisual_StyledItem: ...
    @overload
    def AddStyle(self,style : OCP.StepVisual.StepVisual_StyledItem) -> None: ...
    def ClearStyles(self) -> None: 
        """
        Clears all defined styles and PSA sequence
        """
    def CreateMDGPR(self,Context : OCP.StepRepr.StepRepr_RepresentationContext,MDGPR : OCP.StepVisual.StepVisual_MechanicalDesignGeometricPresentationRepresentation) -> bool: 
        """
        Create MDGPR, fill it with all the styles previously defined, and add it to the model
        """
    def CreateNAUOSRD(self,Context : OCP.StepRepr.StepRepr_RepresentationContext,CDSR : OCP.StepShape.StepShape_ContextDependentShapeRepresentation,initPDS : OCP.StepRepr.StepRepr_ProductDefinitionShape) -> bool: 
        """
        Create MDGPR, fill it with all the styles previously defined, and add it to the model IMPORTANT: <initPDS> must be null when use for NAUO colors <initPDS> initialised only for SHUO case.
        """
    @staticmethod
    def DecodeColor_s(Colour : OCP.StepVisual.StepVisual_Colour,Col : OCP.Quantity.Quantity_Color) -> bool: 
        """
        Decodes STEP color and fills the Quantity_Color. Returns True if OK or False if color is not recognized
        """
    @staticmethod
    @overload
    def EncodeColor_s(Col : OCP.Quantity.Quantity_Color,DPDCs : Any,ColRGBs : Any) -> OCP.StepVisual.StepVisual_Colour: 
        """
        Create STEP color entity by given Quantity_Color The analysis is performed for whether the color corresponds to one of standard colors predefined in STEP. In that case, PredefinedColour entity is created instead of RGBColour

        Create STEP color entity by given Quantity_Color The analysis is performed for whether the color corresponds to one of standard colors predefined in STEP. In that case, PredefinedColour entity is created instead of RGBColour
        """
    @staticmethod
    @overload
    def EncodeColor_s(Col : OCP.Quantity.Quantity_Color) -> OCP.StepVisual.StepVisual_Colour: ...
    def FindContext(self,Shape : OCP.TopoDS.TopoDS_Shape) -> OCP.StepRepr.StepRepr_RepresentationContext: 
        """
        Searches the STEP model for the RepresentationContext in which given shape is defined. This context (if found) can be used then in call to CreateMDGPR()
        """
    def FinderProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns FinderProcess (writing; Null if not loaded)

        Returns FinderProcess (writing; Null if not loaded)
        """
    def GetColorPSA(self,item : OCP.StepRepr.StepRepr_RepresentationItem,Col : OCP.StepVisual.StepVisual_Colour) -> OCP.StepVisual.StepVisual_PresentationStyleAssignment: 
        """
        Returns a PresentationStyleAssignment entity which defines surface and curve colors as Col. This PSA is either created or taken from internal map where all PSAs created by this method are remembered.
        """
    def GetColors(self,style : OCP.StepVisual.StepVisual_StyledItem,SurfCol : OCP.StepVisual.StepVisual_Colour,BoundCol : OCP.StepVisual.StepVisual_Colour,CurveCol : OCP.StepVisual.StepVisual_Colour,RenderCol : OCP.StepVisual.StepVisual_Colour,RenderTransp : float,IsComponent : bool) -> bool: 
        """
        Extract color definitions from the style entity For each type of color supported, result can be either NULL if it is not defined by that style, or last definition (if they are 1 or more)
        """
    @overload
    def Graph(self,recompute : bool) -> OCP.Interface.Interface_Graph: 
        """
        Returns current graph (recomputing if necessary)

        Returns current graph (recomputing if necessary)
        """
    @overload
    def Graph(self,recompute : bool=False) -> OCP.Interface.Interface_Graph: ...
    def Init(self,WS : OCP.XSControl.XSControl_WorkSession) -> bool: 
        """
        Initializes tool; returns True if succeeded
        """
    def LoadInvisStyles(self,InvSyles : OCP.TColStd.TColStd_HSequenceOfTransient) -> bool: 
        """
        Searches the STEP model for the INISIBILITY enteties (which bring styles) and fills out sequence of styles
        """
    def LoadStyles(self) -> bool: 
        """
        Searches the STEP model for the MDGPR or DM entities (which bring styles) and fills sequence of styles
        """
    def MakeColorPSA(self,item : OCP.StepRepr.StepRepr_RepresentationItem,SurfCol : OCP.StepVisual.StepVisual_Colour,CurveCol : OCP.StepVisual.StepVisual_Colour,RenderCol : OCP.StepVisual.StepVisual_Colour,RenderTransp : float,isForNAUO : bool=False) -> OCP.StepVisual.StepVisual_PresentationStyleAssignment: 
        """
        Create a PresentationStyleAssignment entity which defines two colors (for filling surfaces and curves) if isForNAUO true then returns PresentationStyleByContext
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns current model (Null if not loaded)

        Returns current model (Null if not loaded)
        """
    def NbStyles(self) -> int: 
        """
        Returns number of defined styles
        """
    def Style(self,i : int) -> OCP.StepVisual.StepVisual_StyledItem: 
        """
        Returns style with given index
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
class STEPConstruct_ExternRefs(STEPConstruct_Tool):
    """
    Provides a tool for analyzing (reading) and creating (writing) references to external files in STEP
    """
    def AddExternRef(self,filename : str,PD : OCP.StepBasic.StepBasic_ProductDefinition,format : str) -> int: 
        """
        Create a new external reference with specified attributes attached to a given SDR <format> can be Null string, in that case this information is not written. Else, it can be "STEP AP214" or "STEP AP203" Returns index of a new extern ref
        """
    def Clear(self) -> None: 
        """
        Clears internal fields (list of defined extern refs)
        """
    def DocFile(self,num : int) -> OCP.StepBasic.StepBasic_DocumentFile: 
        """
        Returns DocumentFile to which numth extern reference is associated. Returns Null if cannot be detected.
        """
    def FileName(self,num : int) -> str: 
        """
        Returns filename for numth extern reference Returns Null if FileName is not defined or bad
        """
    def FinderProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns FinderProcess (writing; Null if not loaded)

        Returns FinderProcess (writing; Null if not loaded)
        """
    def Format(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns format identification string for the extern document Returns Null handle if format is not defined
        """
    def GetAP214APD(self) -> OCP.StepBasic.StepBasic_ApplicationProtocolDefinition: 
        """
        Returns the ApplicationProtocolDefinition of the PDM schema NOTE: if not defined then create new APD with new Application Context
        """
    @overload
    def Graph(self,recompute : bool) -> OCP.Interface.Interface_Graph: 
        """
        Returns current graph (recomputing if necessary)

        Returns current graph (recomputing if necessary)
        """
    @overload
    def Graph(self,recompute : bool=False) -> OCP.Interface.Interface_Graph: ...
    def Init(self,WS : OCP.XSControl.XSControl_WorkSession) -> bool: 
        """
        Initializes tool; returns True if succeeded
        """
    def LoadExternRefs(self) -> bool: 
        """
        Searches current STEP model for external references and loads them to the internal data structures NOTE: does not clear data structures before loading
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns current model (Null if not loaded)

        Returns current model (Null if not loaded)
        """
    def NbExternRefs(self) -> int: 
        """
        Returns number of defined extern references
        """
    def ProdDef(self,num : int) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns ProductDefinition to which numth extern reference is associated. Returns Null if cannot be detected or if extern reference is not associated to SDR in a proper way.
        """
    def SetAP214APD(self,APD : OCP.StepBasic.StepBasic_ApplicationProtocolDefinition) -> None: 
        """
        Set the ApplicationProtocolDefinition of the PDM schema
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
    def WriteExternRefs(self,num : int) -> int: 
        """
        Adds all the currently defined external refs to the model Returns number of written extern refs
        """
    @overload
    def __init__(self,WS : OCP.XSControl.XSControl_WorkSession) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def checkAP214Shared(self) -> None: ...
    pass
class STEPConstruct_UnitContext():
    """
    Tool for creation (encoding) and decoding (for writing and reading accordingly) context defining units and tolerances (uncerntanties)
    """
    def AreaDone(self) -> bool: 
        """
        Returns true if areaFactor is computed
        """
    def AreaFactor(self) -> float: 
        """
        Returns the areaFactor
        """
    @overload
    def ComputeFactors(self,aContext : OCP.StepRepr.StepRepr_GlobalUnitAssignedContext) -> int: 
        """
        Computes the length, plane angle and solid angle conversion factor . Returns a status, 0 if OK

        None
        """
    @overload
    def ComputeFactors(self,aUnit : OCP.StepBasic.StepBasic_NamedUnit) -> int: ...
    def ComputeTolerance(self,aContext : OCP.StepRepr.StepRepr_GlobalUncertaintyAssignedContext) -> int: 
        """
        Computes the uncertainty value (for length)
        """
    @staticmethod
    def ConvertSiPrefix_s(aPrefix : OCP.StepBasic.StepBasic_SiPrefix) -> float: 
        """
        Convert SI prefix defined by enumertaion to corresponding real factor (e.g. 1e6 for mega)
        """
    def HasUncertainty(self) -> bool: 
        """
        Tells if a Uncertainty (for length) is recorded
        """
    def Init(self,Tol3d : float) -> None: 
        """
        Creates new context (units are MM and radians, uncertainty equal to Tol3d)
        """
    def IsDone(self) -> bool: 
        """
        Returns True if Init was called successfully
        """
    def LengthDone(self) -> bool: 
        """
        Returns true if ComputeFactors has calculated a LengthFactor
        """
    def LengthFactor(self) -> float: 
        """
        Returns the lengthFactor
        """
    def PlaneAngleDone(self) -> bool: 
        """
        Returns true if ComputeFactors has calculated a PlaneAngleFactor
        """
    def PlaneAngleFactor(self) -> float: 
        """
        Returns the planeAngleFactor
        """
    def SolidAngleDone(self) -> bool: 
        """
        Returns true if ComputeFactors has calculated a SolidAngleFactor
        """
    def SolidAngleFactor(self) -> float: 
        """
        Returns the solidAngleFactor
        """
    def StatusMessage(self,status : int) -> str: 
        """
        Returns a message for a given status (0 - empty) This message can then be added as warning for transfer
        """
    def Uncertainty(self) -> float: 
        """
        Returns the Uncertainty value (for length) It has been converted with LengthFactor
        """
    def Value(self) -> OCP.StepGeom.StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx: 
        """
        Returns context (or Null if not done)
        """
    def VolumeDone(self) -> bool: 
        """
        Returns true if volumeFactor is computed
        """
    def VolumeFactor(self) -> float: 
        """
        Returns the volumeFactor
        """
    def __init__(self) -> None: ...
    pass
class STEPConstruct_ValidationProps(STEPConstruct_Tool):
    """
    This class provides tools for access (write and read) the validation properties on shapes in the STEP file. These are surface area, solid volume and centroid.
    """
    def AddArea(self,Shape : OCP.TopoDS.TopoDS_Shape,Area : float) -> bool: 
        """
        Adds surface area property for given shape (already mapped). Returns True if success, False in case of fail
        """
    def AddCentroid(self,Shape : OCP.TopoDS.TopoDS_Shape,Pnt : OCP.gp.gp_Pnt,instance : bool=False) -> bool: 
        """
        Adds centroid property for given shape (already mapped). Returns True if success, False in case of fail If instance is True, then centroid is assigned to an instance of component in assembly
        """
    @overload
    def AddProp(self,target : OCP.StepRepr.StepRepr_CharacterizedDefinition,Context : OCP.StepRepr.StepRepr_RepresentationContext,Prop : OCP.StepRepr.StepRepr_RepresentationItem,Descr : str) -> bool: 
        """
        General method for adding (writing) a validation property for shape which should be already mapped on writing itself. It uses FindTarget() to find target STEP entity resulting from given shape, and associated context Returns True if success, False in case of fail

        General method for adding (writing) a validation property for shape which should be already mapped on writing itself. It takes target and Context entities which correspond to shape Returns True if success, False in case of fail
        """
    @overload
    def AddProp(self,Shape : OCP.TopoDS.TopoDS_Shape,Prop : OCP.StepRepr.StepRepr_RepresentationItem,Descr : str,instance : bool=False) -> bool: ...
    def AddVolume(self,Shape : OCP.TopoDS.TopoDS_Shape,Vol : float) -> bool: 
        """
        Adds volume property for given shape (already mapped). Returns True if success, False in case of fail
        """
    def FindTarget(self,S : OCP.TopoDS.TopoDS_Shape,target : OCP.StepRepr.StepRepr_CharacterizedDefinition,Context : OCP.StepRepr.StepRepr_RepresentationContext,instance : bool=False) -> bool: 
        """
        Finds target STEP entity to which validation props should be assigned, and corresponding context, starting from shape Returns True if success, False in case of fail
        """
    def FinderProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns FinderProcess (writing; Null if not loaded)

        Returns FinderProcess (writing; Null if not loaded)
        """
    def GetPropNAUO(self,PD : OCP.StepRepr.StepRepr_PropertyDefinition) -> OCP.StepRepr.StepRepr_NextAssemblyUsageOccurrence: 
        """
        Returns CDSR associated with given PpD or NULL if not found (when, try GetPropSDR)
        """
    def GetPropPD(self,PD : OCP.StepRepr.StepRepr_PropertyDefinition) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns SDR associated with given PpD or NULL if not found (when, try GetPropCDSR)
        """
    def GetPropPnt(self,item : OCP.StepRepr.StepRepr_RepresentationItem,Context : OCP.StepRepr.StepRepr_RepresentationContext,Pnt : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns value of Centriod property (or False if it is not)
        """
    def GetPropReal(self,item : OCP.StepRepr.StepRepr_RepresentationItem,Val : float,isArea : bool) -> bool: 
        """
        Returns value of Real-Valued property (Area or Volume) If Property is neither Area nor Volume, returns False Else returns True and isArea indicates whether property is area or volume
        """
    @overload
    def GetPropShape(self,PD : OCP.StepRepr.StepRepr_PropertyDefinition) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns Shape associated with given SDR or Null Shape if not found

        Returns Shape associated with given PpD or Null Shape if not found
        """
    @overload
    def GetPropShape(self,ProdDef : OCP.StepBasic.StepBasic_ProductDefinition) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def Graph(self,recompute : bool) -> OCP.Interface.Interface_Graph: 
        """
        Returns current graph (recomputing if necessary)

        Returns current graph (recomputing if necessary)
        """
    @overload
    def Graph(self,recompute : bool=False) -> OCP.Interface.Interface_Graph: ...
    def Init(self,WS : OCP.XSControl.XSControl_WorkSession) -> bool: 
        """
        Load worksession; returns True if succeeded
        """
    def LoadProps(self,seq : OCP.TColStd.TColStd_SequenceOfTransient) -> bool: 
        """
        Searches for entities of the type PropertyDefinitionRepresentation in the model and fills the sequence by them
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns current model (Null if not loaded)

        Returns current model (Null if not loaded)
        """
    def SetAssemblyShape(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets current assembly shape SDR (for FindCDSR calls)
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
