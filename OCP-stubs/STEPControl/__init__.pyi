import OCP.STEPControl
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepShape
import OCP.XSControl
import OCP.IFSelect
import OCP.TopoDS
import OCP.gp
import OCP.Interface
import OCP.Standard
import OCP.StepGeom
import OCP.TColStd
import OCP.Transfer
import OCP.StepRepr
import OCP.StepData
import io
__all__  = [
"STEPControl_ActorRead",
"STEPControl_ActorWrite",
"STEPControl_Controller",
"STEPControl_Reader",
"STEPControl_StepModelType",
"STEPControl_Writer",
"STEPControl_AsIs",
"STEPControl_BrepWithVoids",
"STEPControl_FacetedBrep",
"STEPControl_FacetedBrepAndBrepWithVoids",
"STEPControl_GeometricCurveSet",
"STEPControl_Hybrid",
"STEPControl_ManifoldSolidBrep",
"STEPControl_ShellBasedSurfaceModel"
]
class STEPControl_ActorRead(OCP.Transfer.Transfer_ActorOfTransientProcess, OCP.Transfer.Transfer_ActorOfProcessForTransient, OCP.Standard.Standard_Transient):
    """
    This class performs the transfer of an Entity from AP214 and AP203, either Geometric or Topologic.This class performs the transfer of an Entity from AP214 and AP203, either Geometric or Topologic.This class performs the transfer of an Entity from AP214 and AP203, either Geometric or Topologic.
    """
    def ComputeSRRWT(self,SRR : OCP.StepRepr.StepRepr_RepresentationRelationship,TP : OCP.Transfer.Transfer_TransientProcess,Trsf : OCP.gp.gp_Trsf) -> bool: 
        """
        Computes transformation defined by given REPRESENTATION_RELATIONSHIP_WITH_TRANSFORMATION
        """
    def ComputeTransformation(self,Origin : OCP.StepGeom.StepGeom_Axis2Placement3d,Target : OCP.StepGeom.StepGeom_Axis2Placement3d,OrigContext : OCP.StepRepr.StepRepr_Representation,TargContext : OCP.StepRepr.StepRepr_Representation,TP : OCP.Transfer.Transfer_TransientProcess,Trsf : OCP.gp.gp_Trsf) -> bool: 
        """
        Computes transformation defined by two axis placements (in MAPPED_ITEM or ITEM_DEFINED_TRANSFORMATION) taking into account their representation contexts (i.e. units, which may be different) Returns True if transformation is computed and is not an identity.
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
    def IsLast(self) -> bool: 
        """
        Returns the Last status (see SetLast).
        """
    def Next(self) -> OCP.Transfer.Transfer_ActorOfProcessForTransient: 
        """
        Returns the Actor defined as Next, or a Null Handle
        """
    def NullResult(self) -> OCP.Transfer.Transfer_Binder: 
        """
        Returns a Binder for No Result, i.e. a Null Handle
        """
    def PrepareUnits(self,rep : OCP.StepRepr.StepRepr_Representation,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        set units and tolerances context by given ShapeRepresentation
        """
    def Recognize(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        None
        """
    def ResetUnits(self) -> None: 
        """
        reset units and tolerances context to default (mm, radians, read.precision.val, etc.)
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetNext(self,next : OCP.Transfer.Transfer_ActorOfProcessForTransient) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transfer(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_TransientProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferShape(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_TransientProcess,isManifold : bool=True,theUseTrsf : bool=False,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        theUseTrsf - special flag for using Axis2Placement from ShapeRepresentation for transform root shape
        """
    def TransferTransient(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_TransientProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Transferring(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_ProcessForTransient,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransientResult(self,res : OCP.Standard.Standard_Transient) -> OCP.Transfer.Transfer_SimpleBinderOfTransient: 
        """
        Prepares and Returns a Binder for a Transient Result Returns a Null Handle if <res> is itself Null
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
class STEPControl_ActorWrite(OCP.Transfer.Transfer_ActorOfFinderProcess, OCP.Transfer.Transfer_ActorOfProcessForFinder, OCP.Standard.Standard_Transient):
    """
    This class performs the transfer of a Shape from TopoDS to AP203 or AP214 (CD2 or DIS)This class performs the transfer of a Shape from TopoDS to AP203 or AP214 (CD2 or DIS)This class performs the transfer of a Shape from TopoDS to AP203 or AP214 (CD2 or DIS)
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
    def GroupMode(self) -> int: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAssembly(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Customizable method to check whether shape S should be written as assembly or not Default implementation uses flag GroupMode and analyses the shape itself NOTE: this method can modify shape
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
    def IsLast(self) -> bool: 
        """
        Returns the Last status (see SetLast).
        """
    def Mode(self) -> STEPControl_StepModelType: 
        """
        None
        """
    def Next(self) -> OCP.Transfer.Transfer_ActorOfProcessForFinder: 
        """
        Returns the Actor defined as Next, or a Null Handle
        """
    def NullResult(self) -> OCP.Transfer.Transfer_Binder: 
        """
        Returns a Binder for No Result, i.e. a Null Handle
        """
    def Recognize(self,start : OCP.Transfer.Transfer_Finder) -> bool: 
        """
        None
        """
    def SetGroupMode(self,mode : int) -> None: 
        """
        None
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetMode(self,M : STEPControl_StepModelType) -> None: 
        """
        None
        """
    def SetNext(self,next : OCP.Transfer.Transfer_ActorOfProcessForFinder) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transfer(self,start : OCP.Transfer.Transfer_Finder,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferCompound(self,start : OCP.Transfer.Transfer_Finder,SDR : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferShape(self,start : OCP.Transfer.Transfer_Finder,SDR : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,FP : OCP.Transfer.Transfer_FinderProcess,shapeGroup : OCP.TopTools.TopTools_HSequenceOfShape=None,isManifold : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferSubShape(self,start : OCP.Transfer.Transfer_Finder,SDR : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,AX1 : OCP.StepGeom.StepGeom_Axis2Placement3d,FP : OCP.Transfer.Transfer_FinderProcess,shapeGroup : OCP.TopTools.TopTools_HSequenceOfShape=None,isManifold : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferTransient(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Transferring(self,start : OCP.Transfer.Transfer_Finder,TP : OCP.Transfer.Transfer_ProcessForFinder,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransientResult(self,res : OCP.Standard.Standard_Transient) -> OCP.Transfer.Transfer_SimpleBinderOfTransient: 
        """
        Prepares and Returns a Binder for a Transient Result Returns a Null Handle if <res> is itself Null
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
    @property
    def ModeTrans(self) -> int:
        """
        Returns the Transfer Mode, modifiable

        :type: int
        """
    @ModeTrans.setter
    def ModeTrans(self, arg1: int) -> None:
        """
        Returns the Transfer Mode, modifiable
        """
    pass
class STEPControl_Controller(OCP.XSControl.XSControl_Controller, OCP.Standard.Standard_Transient):
    """
    defines basic controller for STEP processordefines basic controller for STEP processordefines basic controller for STEP processor
    """
    def ActorRead(self,model : OCP.Interface.Interface_InterfaceModel) -> OCP.Transfer.Transfer_ActorOfTransientProcess: 
        """
        Returns the Actor for Read attached to the pair (norm,appli) It can be adapted for data of the input Model, as required Can be read from field then adapted with Model as required
        """
    def ActorWrite(self) -> OCP.Transfer.Transfer_ActorOfFinderProcess: 
        """
        Returns the Actor for Write attached to the pair (norm,appli) Read from field. Can be redefined
        """
    def AdaptorSession(self) -> Any: 
        """
        None
        """
    def AddSessionItem(self,theItem : OCP.Standard.Standard_Transient,theName : str,toApply : bool=False) -> None: 
        """
        Records a Session Item, to be added for customisation of the Work Session. It must have a specific name. <setapplied> is used if <item> is a GeneralModifier, to decide If set to true, <item> will be applied to the hook list "send". Else, it is not applied to any hook list. Remark : this method is to be called at Create time, the recorded items will be used by Customise Warning : if <name> conflicts, the last recorded item is kept
        """
    def AutoRecord(self) -> None: 
        """
        Records <me> is a general dictionary under Short and Long Names (see method Name)
        """
    def Customise(self,WS : OCP.XSControl.XSControl_WorkSession) -> Any: 
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
    @staticmethod
    def Init_s() -> bool: 
        """
        Standard Initialisation. It creates a Controller for STEP and records it to various names, available to select it later Returns True when done, False if could not be done
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
    def IsModeWrite(self,modetrans : int,shape : bool=True) -> bool: 
        """
        Tells if a value of <modetrans> is a good value(within bounds) Actually only for shapes
        """
    def ModeWriteBounds(self,modemin : int,modemax : int,shape : bool=True) -> bool: 
        """
        Returns recorded min and max values for modetrans (write) Actually only for shapes Returns True if bounds are set, False else (then, free value)
        """
    def ModeWriteHelp(self,modetrans : int,shape : bool=True) -> str: 
        """
        Returns the help line recorded for a value of modetrans empty if help not defined or not within bounds or if values are free
        """
    def Name(self,rsc : bool=False) -> str: 
        """
        Returns a name, as given when initializing : rsc = False (D) : True Name attached to the Norm (long name) rsc = True : Name of the resource set (i.e. short name)
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Creates a new empty Model ready to receive data of the Norm. It is taken from STEP Template Model
        """
    def Protocol(self) -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Protocol attached to the Norm (from field)
        """
    def RecognizeWriteShape(self,shape : OCP.TopoDS.TopoDS_Shape,modetrans : int=0) -> bool: 
        """
        Tells if a shape is valid for a transfer to a model Asks the ActorWrite (through a ShapeMapper)
        """
    def RecognizeWriteTransient(self,obj : OCP.Standard.Standard_Transient,modetrans : int=0) -> bool: 
        """
        Tells if <obj> (an application object) is a valid candidate for a transfer to a Model. By default, asks the ActorWrite if known (through a TransientMapper). Can be redefined
        """
    def Record(self,name : str) -> None: 
        """
        Records <me> in a general dictionary under a name Error if <name> already used for another one
        """
    @staticmethod
    def Recorded_s(name : str) -> OCP.XSControl.XSControl_Controller: 
        """
        Returns the Controller attached to a given name Returns a Null Handle if <name> is unknown
        """
    def SessionItem(self,theName : str) -> OCP.Standard.Standard_Transient: 
        """
        Returns an item given its name to record in a Session If <name> is unknown, returns a Null Handle
        """
    def SetModeWrite(self,modemin : int,modemax : int,shape : bool=True) -> None: 
        """
        Sets mininum and maximum values for modetrans (write) Erases formerly recorded bounds and values Actually only for shape Then, for each value a little help can be attached
        """
    def SetModeWriteHelp(self,modetrans : int,help : str,shape : bool=True) -> None: 
        """
        Attaches a short line of help to a value of modetrans (write)
        """
    def SetNames(self,theLongName : str,theShortName : str) -> None: 
        """
        Changes names if a name is empty, the formerly set one remains Remark : Does not call Record or AutoRecord
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransferWriteShape(self,shape : OCP.TopoDS.TopoDS_Shape,FP : OCP.Transfer.Transfer_FinderProcess,model : OCP.Interface.Interface_InterfaceModel,modetrans : int=0,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Takes one Shape and transfers it to the InterfaceModel (already created by NewModel for instance) <modeshape> is to be interpreted by each kind of XstepAdaptor Returns a status : 0 OK 1 No result 2 Fail -1 bad modeshape -2 bad model (requires a StepModel) modeshape : 1 Facetted BRep, 2 Shell, 3 Manifold Solid
        """
    def TransferWriteTransient(self,obj : OCP.Standard.Standard_Transient,FP : OCP.Transfer.Transfer_FinderProcess,model : OCP.Interface.Interface_InterfaceModel,modetrans : int=0,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Takes one Transient Object and transfers it to an InterfaceModel (already created, e.g. by NewModel) (result is recorded in the model by AddWithRefs) FP records produced results and checks
        """
    def WorkLibrary(self) -> OCP.IFSelect.IFSelect_WorkLibrary: 
        """
        Returns the WorkLibrary attached to the Norm. Remark that it has to be in phase with the Protocol (read from field)
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
class STEPControl_Reader(OCP.XSControl.XSControl_Reader):
    """
    Reads STEP files, checks them and translates their contents into Open CASCADE models. The STEP data can be that of a whole model or that of a specific list of entities in the model. As in XSControl_Reader, you specify the list using a selection. For the translation of iges files it is possible to use next sequence: To change translation parameters class Interface_Static should be used before beginning of translation (see STEP Parameters and General Parameters) Creation of reader - STEPControl_Reader reader; To load s file in a model use method reader.ReadFile("filename.stp") To print load results reader.PrintCheckLoad(failsonly,mode) where mode is equal to the value of enumeration IFSelect_PrintCount For definition number of candidates : Standard_Integer nbroots = reader. NbRootsForTransfer(); To transfer entities from a model the following methods can be used: for the whole model - reader.TransferRoots(); to transfer a list of entities: reader.TransferList(list); to transfer one entity Handle(Standard_Transient) ent = reader.RootForTransfer(num); reader.TransferEntity(ent), or reader.TransferOneRoot(num), or reader.TransferOne(num), or reader.TransferRoot(num) To obtain the result the following method can be used: reader.NbShapes() and reader.Shape(num); or reader.OneShape(); To print the results of transfer use method: reader.PrintCheckTransfer(failwarn,mode); where printfail is equal to the value of enumeration IFSelect_PrintFail, mode see above; or reader.PrintStatsTransfer(); Gets correspondence between a STEP entity and a result shape obtained from it. Handle(XSControl_WorkSession) WS = reader.WS(); if ( WS->TransferReader()->HasResult(ent) ) TopoDS_Shape shape = WS->TransferReader()->ShapeResult(ent);
    """
    def ClearShapes(self) -> None: 
        """
        Clears the list of shapes that may have accumulated in calls to TransferOne or TransferRoot.C
        """
    def FileUnits(self,theUnitLengthNames : OCP.TColStd.TColStd_SequenceOfAsciiString,theUnitAngleNames : OCP.TColStd.TColStd_SequenceOfAsciiString,theUnitSolidAngleNames : OCP.TColStd.TColStd_SequenceOfAsciiString) -> None: 
        """
        Returns sequence of all unit names for shape representations found in file
        """
    def GetStatsTransfer(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> Tuple[int, int, int]: 
        """
        Gives statistics about Transfer
        """
    @overload
    def GiveList(self,first : str='',second : str='') -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns a list of entities from the IGES or STEP file according to the following rules: - if first and second are empty strings, the whole file is selected. - if first is an entity number or label, the entity referred to is selected. - if first is a list of entity numbers/labels separated by commas, the entities referred to are selected, - if first is the name of a selection in the worksession and second is not defined, the list contains the standard output for that selection. - if first is the name of a selection and second is defined, the criterion defined by second is applied to the result of the first selection. A selection is an operator which computes a list of entities from a list given in input according to its type. If no list is specified, the selection computes its list of entities from the whole model. A selection can be: - A predefined selection (xst-transferrable-mode) - A filter based on a signature A Signature is an operator which returns a string from an entity according to its type. For example: - "xst-type" (CDL) - "iges-level" - "step-type". For example, if you wanted to select only the advanced_faces in a STEP file you would use the following code: Example Reader.GiveList("xst-transferrable-roots","step-type(ADVANCED_FACE)"); Warning If the value given to second is incorrect, it will simply be ignored.

        Computes a List of entities from the model as follows <first> being a Selection, <ent> being an entity or a list of entities (as a HSequenceOfTransient) : the standard result of this selection applied to this list if <first> is erroneous, a null handle is returned
        """
    @overload
    def GiveList(self,first : str,ent : OCP.Standard.Standard_Transient) -> OCP.TColStd.TColStd_HSequenceOfTransient: ...
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the model. It can then be consulted (header, product)
        """
    def NbRootsForTransfer(self) -> int: 
        """
        Determines the list of root entities from Model which are candidate for a transfer to a Shape (type of entities is PRODUCT)
        """
    def NbShapes(self) -> int: 
        """
        Returns the number of shapes produced by translation.
        """
    def OneShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns all of the results in a single shape which is: - a null shape if there are no results, - a shape if there is one result, - a compound containing the resulting shapes if there are more than one.
        """
    @overload
    def PrintCheckLoad(self,theStream : io.BytesIO,failsonly : bool,mode : OCP.IFSelect.IFSelect_PrintCount) -> None: 
        """
        Prints the check list attached to loaded data, on the Standard Trace File (starts at std::cout) All messages or fails only, according to <failsonly> mode = 0 : per entity, prints messages mode = 1 : per message, just gives count of entities per check mode = 2 : also gives entity numbers

        Prints the check list attached to loaded data.
        """
    @overload
    def PrintCheckLoad(self,failsonly : bool,mode : OCP.IFSelect.IFSelect_PrintCount) -> None: ...
    @overload
    def PrintCheckTransfer(self,failsonly : bool,mode : OCP.IFSelect.IFSelect_PrintCount) -> None: 
        """
        Displays check results for the last translation of IGES or STEP entities to Open CASCADE entities. Only fail messages are displayed if failsonly is true. All messages are displayed if failsonly is false. mode determines the contents and the order of the messages according to the terms of the IFSelect_PrintCount enumeration.

        Displays check results for the last translation of IGES or STEP entities to Open CASCADE entities.
        """
    @overload
    def PrintCheckTransfer(self,theStream : io.BytesIO,failsonly : bool,mode : OCP.IFSelect.IFSelect_PrintCount) -> None: ...
    @overload
    def PrintStatsTransfer(self,theStream : io.BytesIO,what : int,mode : int=0) -> None: 
        """
        Displays the statistics for the last translation. what defines the kind of statistics that are displayed as follows: - 0 gives general statistics (number of translated roots, number of warnings, number of fail messages), - 1 gives root results, - 2 gives statistics for all checked entities, - 3 gives the list of translated entities, - 4 gives warning and fail messages, - 5 gives fail messages only. The use of mode depends on the value of what. If what is 0, mode is ignored. If what is 1, 2 or 3, mode defines the following: - 0 lists the numbers of IGES or STEP entities in the respective model - 1 gives the number, identifier, type and result type for each IGES or STEP entity and/or its status (fail, warning, etc.) - 2 gives maximum information for each IGES or STEP entity (i.e. checks) - 3 gives the number of entities per type of IGES or STEP entity - 4 gives the number of IGES or STEP entities per result type and/or status - 5 gives the number of pairs (IGES or STEP or result type and status) - 6 gives the number of pairs (IGES or STEP or result type and status) AND the list of entity numbers in the IGES or STEP model. If what is 4 or 5, mode defines the warning and fail messages as follows: - if mode is 0 all warnings and checks per entity are returned - if mode is 2 the list of entities per warning is returned. If mode is not set, only the list of all entities per warning is given.

        Displays the statistics for the last translation.
        """
    @overload
    def PrintStatsTransfer(self,what : int,mode : int=0) -> None: ...
    def ReadFile(self,filename : str) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Loads a file and returns the read status Zero for a Model which compies with the Controller
        """
    def ReadStream(self,theName : str,theIStream : io.BytesIO) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Loads a file from stream and returns the read status
        """
    def RootForTransfer(self,num : int=1) -> OCP.Standard.Standard_Transient: 
        """
        Returns an IGES or STEP root entity for translation. The entity is identified by its rank in a list.
        """
    def SetNorm(self,norm : str) -> bool: 
        """
        Sets a specific norm to <me> Returns True if done, False if <norm> is not available
        """
    def SetSystemLengthUnit(self,theLengthUnit : float) -> None: 
        """
        Sets system length unit used by transfer process
        """
    def SetWS(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: 
        """
        Sets a specific session to <me>
        """
    def Shape(self,num : int=1) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape resulting from a translation and identified by the rank num. num equals 1 by default. In other words, the first shape resulting from the translation is returned.
        """
    def StepModel(self) -> OCP.StepData.StepData_StepModel: 
        """
        Returns the model as a StepModel. It can then be consulted (header, product)
        """
    def SystemLengthUnit(self) -> float: 
        """
        Returns system length unit used by transfer process
        """
    def TransferEntity(self,start : OCP.Standard.Standard_Transient,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Translates an IGES or STEP entity in the model. true is returned if a shape is produced; otherwise, false is returned.
        """
    def TransferList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int: 
        """
        Translates a list of entities. Returns the number of IGES or STEP entities that were successfully translated. The list can be produced with GiveList. Warning - This function does not clear the existing output shapes.
        """
    def TransferOne(self,num : int,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Translates an IGES or STEP entity identified by the rank num in the model. false is returned if no shape is produced.
        """
    def TransferOneRoot(self,num : int=1,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Translates a root identified by the rank num in the model. false is returned if no shape is produced.
        """
    def TransferRoot(self,num : int=1,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Transfers a root given its rank in the list of candidate roots Default is the first one Returns True if a shape has resulted, false else Same as inherited TransferOneRoot, kept for compatibility
        """
    def TransferRoots(self,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int: 
        """
        Translates all translatable roots and returns the number of successful translations. Warning - This function clears existing output shapes first.
        """
    def WS(self) -> OCP.XSControl.XSControl_WorkSession: 
        """
        Returns the session used in <me>
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: ...
    pass
class STEPControl_StepModelType():
    """
    Gives you the choice of translation mode for an Open CASCADE shape that is being translated to STEP. - STEPControl_AsIs translates an Open CASCADE shape to its highest possible STEP representation. - STEPControl_ManifoldSolidBrep translates an Open CASCADE shape to a STEP manifold_solid_brep or brep_with_voids entity. - STEPControl_FacetedBrep translates an Open CASCADE shape into a STEP faceted_brep entity. - STEPControl_ShellBasedSurfaceModel translates an Open CASCADE shape into a STEP shell_based_surface_model entity. - STEPControl_GeometricCurveSet translates an Open CASCADE shape into a STEP geometric_curve_set entity.

    Members:

      STEPControl_AsIs

      STEPControl_ManifoldSolidBrep

      STEPControl_BrepWithVoids

      STEPControl_FacetedBrep

      STEPControl_FacetedBrepAndBrepWithVoids

      STEPControl_ShellBasedSurfaceModel

      STEPControl_GeometricCurveSet

      STEPControl_Hybrid
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self,value : int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self,other : object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self,state : int) -> None: ...
    @property
    def name(self) -> None:
        """
        :type: None
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    STEPControl_AsIs: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_AsIs: 0>
    STEPControl_BrepWithVoids: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_BrepWithVoids: 2>
    STEPControl_FacetedBrep: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_FacetedBrep: 3>
    STEPControl_FacetedBrepAndBrepWithVoids: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_FacetedBrepAndBrepWithVoids: 4>
    STEPControl_GeometricCurveSet: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_GeometricCurveSet: 6>
    STEPControl_Hybrid: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_Hybrid: 7>
    STEPControl_ManifoldSolidBrep: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_ManifoldSolidBrep: 1>
    STEPControl_ShellBasedSurfaceModel: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_ShellBasedSurfaceModel: 5>
    __entries: dict # value = {'STEPControl_AsIs': (<STEPControl_StepModelType.STEPControl_AsIs: 0>, None), 'STEPControl_ManifoldSolidBrep': (<STEPControl_StepModelType.STEPControl_ManifoldSolidBrep: 1>, None), 'STEPControl_BrepWithVoids': (<STEPControl_StepModelType.STEPControl_BrepWithVoids: 2>, None), 'STEPControl_FacetedBrep': (<STEPControl_StepModelType.STEPControl_FacetedBrep: 3>, None), 'STEPControl_FacetedBrepAndBrepWithVoids': (<STEPControl_StepModelType.STEPControl_FacetedBrepAndBrepWithVoids: 4>, None), 'STEPControl_ShellBasedSurfaceModel': (<STEPControl_StepModelType.STEPControl_ShellBasedSurfaceModel: 5>, None), 'STEPControl_GeometricCurveSet': (<STEPControl_StepModelType.STEPControl_GeometricCurveSet: 6>, None), 'STEPControl_Hybrid': (<STEPControl_StepModelType.STEPControl_Hybrid: 7>, None)}
    __members__: dict # value = {'STEPControl_AsIs': <STEPControl_StepModelType.STEPControl_AsIs: 0>, 'STEPControl_ManifoldSolidBrep': <STEPControl_StepModelType.STEPControl_ManifoldSolidBrep: 1>, 'STEPControl_BrepWithVoids': <STEPControl_StepModelType.STEPControl_BrepWithVoids: 2>, 'STEPControl_FacetedBrep': <STEPControl_StepModelType.STEPControl_FacetedBrep: 3>, 'STEPControl_FacetedBrepAndBrepWithVoids': <STEPControl_StepModelType.STEPControl_FacetedBrepAndBrepWithVoids: 4>, 'STEPControl_ShellBasedSurfaceModel': <STEPControl_StepModelType.STEPControl_ShellBasedSurfaceModel: 5>, 'STEPControl_GeometricCurveSet': <STEPControl_StepModelType.STEPControl_GeometricCurveSet: 6>, 'STEPControl_Hybrid': <STEPControl_StepModelType.STEPControl_Hybrid: 7>}
    pass
class STEPControl_Writer():
    """
    This class creates and writes STEP files from Open CASCADE models. A STEP file can be written to an existing STEP file or to a new one. Translation can be performed in one or several operations. Each translation operation outputs a distinct root entity in the STEP file.
    """
    def Model(self,newone : bool=False) -> OCP.StepData.StepData_StepModel: 
        """
        Returns the produced model. Produces a new one if not yet done or if <newone> is True This method allows for instance to edit product or header data before writing.
        """
    def PrintStatsTransfer(self,what : int,mode : int=0) -> None: 
        """
        Displays the statistics for the last translation. what defines the kind of statistics that are displayed: - 0 gives general statistics (number of translated roots, number of warnings, number of fail messages), - 1 gives root results, - 2 gives statistics for all checked entities, - 3 gives the list of translated entities, - 4 gives warning and fail messages, - 5 gives fail messages only. mode is used according to the use of what. If what is 0, mode is ignored. If what is 1, 2 or 3, mode defines the following: - 0 lists the numbers of STEP entities in a STEP model, - 1 gives the number, identifier, type and result type for each STEP entity and/or its status (fail, warning, etc.), - 2 gives maximum information for each STEP entity (i.e. checks), - 3 gives the number of entities by the type of a STEP entity, - 4 gives the number of of STEP entities per result type and/or status, - 5 gives the number of pairs (STEP or result type and status), - 6 gives the number of pairs (STEP or result type and status) AND the list of entity numbers in the STEP model.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        Sets a length-measure value that will be written to uncertainty-measure-with-unit when the next shape is translated.
        """
    def SetWS(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: 
        """
        Sets a specific session to <me>
        """
    def Transfer(self,sh : OCP.TopoDS.TopoDS_Shape,mode : STEPControl_StepModelType,compgraph : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Translates shape sh to a STEP entity. mode defines the STEP entity type to be output: - STEPControlStd_AsIs translates a shape to its highest possible STEP representation. - STEPControlStd_ManifoldSolidBrep translates a shape to a STEP manifold_solid_brep or brep_with_voids entity. - STEPControlStd_FacetedBrep translates a shape into a STEP faceted_brep entity. - STEPControlStd_ShellBasedSurfaceModel translates a shape into a STEP shell_based_surface_model entity. - STEPControlStd_GeometricCurveSet translates a shape into a STEP geometric_curve_set entity.
        """
    def UnsetTolerance(self) -> None: 
        """
        Unsets the tolerance formerly forced by SetTolerance
        """
    def WS(self) -> OCP.XSControl.XSControl_WorkSession: 
        """
        Returns the session used in <me>
        """
    def Write(self,theFileName : str) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Writes a STEP model in the file identified by filename.
        """
    def WriteStream(self,theOStream : io.BytesIO) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Writes a STEP model in the std::ostream.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: ...
    pass
STEPControl_AsIs: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_AsIs: 0>
STEPControl_BrepWithVoids: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_BrepWithVoids: 2>
STEPControl_FacetedBrep: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_FacetedBrep: 3>
STEPControl_FacetedBrepAndBrepWithVoids: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_FacetedBrepAndBrepWithVoids: 4>
STEPControl_GeometricCurveSet: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_GeometricCurveSet: 6>
STEPControl_Hybrid: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_Hybrid: 7>
STEPControl_ManifoldSolidBrep: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_ManifoldSolidBrep: 1>
STEPControl_ShellBasedSurfaceModel: OCP.STEPControl.STEPControl_StepModelType # value = <STEPControl_StepModelType.STEPControl_ShellBasedSurfaceModel: 5>
