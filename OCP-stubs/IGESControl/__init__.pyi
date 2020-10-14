import OCP.IGESControl
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.ShapeExtend
import OCP.XSControl
import OCP.IFSelect
import OCP.IGESData
import OCP.Transfer
import OCP.Standard
import OCP.TopoDS
import OCP.IGESToBRep
import OCP.Interface
import OCP.gp
__all__  = [
"IGESControl_ActorWrite",
"IGESControl_AlgoContainer",
"IGESControl_Controller",
"IGESControl_IGESBoundary",
"IGESControl_Reader",
"IGESControl_ToolContainer",
"IGESControl_Writer"
]
class IGESControl_ActorWrite(OCP.Transfer.Transfer_ActorOfFinderProcess, OCP.Transfer.Transfer_ActorOfProcessForFinder, OCP.Standard.Standard_Transient):
    """
    Actor to write Shape to IGESActor to write Shape to IGESActor to write Shape to IGES
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
        Recognizes a ShapeMapper
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetNext(self,next : OCP.Transfer.Transfer_ActorOfProcessForFinder) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transfer(self,start : OCP.Transfer.Transfer_Finder,FP : OCP.Transfer.Transfer_FinderProcess) -> OCP.Transfer.Transfer_Binder: 
        """
        Transfers Shape to IGES Entities
        """
    def TransferTransient(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_FinderProcess) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Transferring(self,start : OCP.Transfer.Transfer_Finder,TP : OCP.Transfer.Transfer_ProcessForFinder) -> OCP.Transfer.Transfer_Binder: 
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
class IGESControl_AlgoContainer(OCP.IGESToBRep.IGESToBRep_AlgoContainer, OCP.Standard.Standard_Transient):
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
    def SetToolContainer(self,TC : OCP.IGESToBRep.IGESToBRep_ToolContainer) -> None: 
        """
        Sets ToolContainer

        Sets ToolContainer
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToolContainer(self) -> OCP.IGESToBRep.IGESToBRep_ToolContainer: 
        """
        Returns ToolContainer

        Returns ToolContainer
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
class IGESControl_Controller(OCP.XSControl.XSControl_Controller, OCP.Standard.Standard_Transient):
    """
    Controller for IGES-5.1Controller for IGES-5.1Controller for IGES-5.1
    """
    def ActorRead(self,model : OCP.Interface.Interface_InterfaceModel) -> OCP.Transfer.Transfer_ActorOfTransientProcess: 
        """
        Returns the Actor for Read attached to the pair (norm,appli) It is an Actor from IGESToBRep, adapted from an IGESModel : Unit, tolerances
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
        Standard Initialisation. It creates a Controller for IGES and records it to various names, available to select it later Returns True when done, False if could not be done Also, it creates and records an Adaptor for FNES
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
        Returns a name, as given when initializing : rsc = False (D) : True Name attached to the Norm (long name) rsc = True : Name of the ressource set (i.e. short name)
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Creates a new empty Model ready to receive data of the Norm. It is taken from IGES Template Model
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
    def TransferWriteShape(self,shape : OCP.TopoDS.TopoDS_Shape,FP : OCP.Transfer.Transfer_FinderProcess,model : OCP.Interface.Interface_InterfaceModel,modetrans : int=0) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Takes one Shape and transfers it to the InterfaceModel (already created by NewModel for instance) <modetrans> is to be interpreted by each kind of XstepAdaptor Returns a status : 0 OK 1 No result 2 Fail -1 bad modeshape -2 bad model (requires an IGESModel) modeshape : 0 groupe of face (version < 5.1) 1 BREP-version 5.1 of IGES
        """
    def TransferWriteTransient(self,obj : OCP.Standard.Standard_Transient,FP : OCP.Transfer.Transfer_FinderProcess,model : OCP.Interface.Interface_InterfaceModel,modetrans : int=0) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Takes one Transient Object and transfers it to an InterfaceModel (already created, e.g. by NewModel) (result is recorded in the model by AddWithRefs) FP records produced results and checks
        """
    def WorkLibrary(self) -> OCP.IFSelect.IFSelect_WorkLibrary: 
        """
        Returns the WorkLibrary attached to the Norm. Remark that it has to be in phase with the Protocol (read from field)
        """
    def __init__(self,modefnes : bool=False) -> None: ...
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
class IGESControl_IGESBoundary(OCP.IGESToBRep.IGESToBRep_IGESBoundary, OCP.Standard.Standard_Transient):
    """
    Translates IGES boundary entity (types 141, 142 and 508) in Advanced Data Exchange. Redefines translation and treatment methods from inherited open class IGESToBRep_IGESBoundary.Translates IGES boundary entity (types 141, 142 and 508) in Advanced Data Exchange. Redefines translation and treatment methods from inherited open class IGESToBRep_IGESBoundary.Translates IGES boundary entity (types 141, 142 and 508) in Advanced Data Exchange. Redefines translation and treatment methods from inherited open class IGESToBRep_IGESBoundary.
    """
    def Check(self,result : bool,checkclosure : bool,okCurve3d : bool,okCurve2d : bool) -> None: 
        """
        Checks result of translation of IGES boundary entities (types 141, 142 or 508). Checks consistency of 2D and 3D representations and keeps only one if they are inconsistent. Checks the closure of resulting wire and if it is not closed, checks 2D and 3D representation and updates the resulting wire to contain only closed representation.
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
    def Init(self,CS : OCP.IGESToBRep.IGESToBRep_CurveAndSurface,entity : OCP.IGESData.IGESData_IGESEntity,face : OCP.TopoDS.TopoDS_Face,trans : OCP.gp.gp_Trsf2d,uFact : float,filepreference : int) -> None: 
        """
        Inits the object with parameters common for all types of IGES boundaries. <CS>: object to be used for retrieving translation parameters and sending messages, <entity>: boundary entity to be processed, <face>, <trans>, <uFact>: as for IGESToBRep_TopoCurve <filepreference>: preferred representation (2 or 3) given in the IGES file
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transfer(self,okCurve : bool,okCurve3d : bool,okCurve2d : bool,curve3d : OCP.ShapeExtend.ShapeExtend_WireData,curves2d : OCP.IGESData.IGESData_HArray1OfIGESEntity,toreverse2d : bool,number : int,lsewd : OCP.ShapeExtend.ShapeExtend_WireData) -> bool: 
        """
        Translates 141 and 142 entities. Returns True if the curve has been successfully translated, otherwise returns False. <okCurve..>: flags that indicate whether corresponding representation has been successfully translated (must be set to True before first call), <curve3d>: model space curve for 142 and current model space curve for 141, <toreverse3d>: False for 142 and current orientation flag for 141, <curves2d>: 1 parameter space curve for 142 or list of them for current model space curves for 141, <number>: 1 for 142 and rank number of model space curve for 141.

        Translates 508 entity. Returns True if the curve has been successfully translated, otherwise returns False. Input object IGESBoundary must be created and initialized before. <okCurve..>: flags that indicate whether corresponding representation has been successfully translated (must be set to True before first call), <curve3d>: result of translation of current edge, <curves2d>: list of parameter space curves for edge, <toreverse2d>: orientation flag of current edge in respect to its model space curve, <number>: rank number of edge, <lsewd>: returns the result of translation of current edge.
        """
    @overload
    def Transfer(self,okCurve : bool,okCurve3d : bool,okCurve2d : bool,curve3d : OCP.IGESData.IGESData_IGESEntity,toreverse3d : bool,curves2d : OCP.IGESData.IGESData_HArray1OfIGESEntity,number : int) -> bool: ...
    def WireData(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        Returns the resulting wire

        Returns the resulting wire
        """
    def WireData2d(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        Returns the the wire from 2D curves (edges contain pcurves only)

        Returns the the wire from 2D curves (edges contain pcurves only)
        """
    def WireData3d(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        Returns the wire from 3D curves (edges contain 3D curves and may contain pcurves)

        Returns the wire from 3D curves (edges contain 3D curves and may contain pcurves)
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,CS : OCP.IGESToBRep.IGESToBRep_CurveAndSurface) -> None: ...
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
class IGESControl_Reader(OCP.XSControl.XSControl_Reader):
    """
    Reads IGES files, checks them and translates their contents into Open CASCADE models. The IGES data can be that of a whole model or that of a specific list of entities in the model. As in XSControl_Reader, you specify the list using a selection. For translation of iges files it is possible to use the following sequence: To change parameters of translation class Interface_Static should be used before the beginning of translation (see IGES Parameters and General Parameters) Creation of reader IGESControl_Reader reader; To load a file in a model use method: reader.ReadFile("filename.igs") To check a loading file use method Check: reader.Check(failsonly); where failsonly is equal to Standard_True or Standard_False; To print the results of load: reader.PrintCheckLoad(failsonly,mode) where mode is equal to the value of enumeration IFSelect_PrintCount To transfer entities from a model the following methods can be used: for the whole model reader.TransferRoots(onlyvisible); where onlyvisible is equal to Standard_True or Standard_False; To transfer a list of entities: reader.TransferList(list); To transfer one entity reader.TransferEntity(ent) or reader.Transfer(num); To obtain a result the following method can be used: reader.IsDone() reader.NbShapes() and reader.Shape(num); or reader.OneShape(); To print the results of transfer use method: reader.PrintTransferInfo(failwarn,mode); where printfail is equal to the value of enumeration IFSelect_PrintFail, mode see above. Gets correspondence between an IGES entity and a result shape obtained therefrom. reader.TransientProcess(); TopoDS_Shape shape = TransferBRep::ShapeResult(reader.TransientProcess(),ent);
    """
    def ClearShapes(self) -> None: 
        """
        Clears the list of shapes that may have accumulated in calls to TransferOne or TransferRoot.C
        """
    def GetReadVisible(self) -> bool: 
        """
        None

        None
        """
    def GetStatsTransfer(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> Tuple[int, int, int]: 
        """
        Gives statistics about Transfer
        """
    @overload
    def GiveList(self,first : str='',second : str='') -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns a list of entities from the IGES or STEP file according to the following rules: - if first and second are empty strings, the whole file is selected. - if first is an entity number or label, the entity referred to is selected. - if first is a list of entity numbers/labels separated by commas, the entities referred to are selected, - if first is the name of a selection in the worksession and second is not defined, the list contains the standard output for that selection. - if first is the name of a selection and second is defined, the criterion defined by second is applied to the result of the first selection. A selection is an operator which computes a list of entities from a list given in input according to its type. If no list is specified, the selection computes its list of entities from the whole model. A selection can be: - A predefined selection (xst-transferrable-mode) - A filter based on a signature A Signature is an operator which returns a string from an entity according to its type. For example: - "xst-type" (CDL) - "iges-level" - "step-type". For example, if you wanted to select only the advanced_faces in a STEP file you would use the following code: Example Reader.GiveList("xst-transferrable-roots","step-type(ADVANCED_FACE)"); Warning If the value given to second is incorrect, it will simply be ignored.

        Computes a List of entities from the model as follows <first> beeing a Selection, <ent> beeing an entity or a list of entities (as a HSequenceOfTransient) : the standard result of this selection applied to this list if <first> is erroneous, a null handle is returned
        """
    @overload
    def GiveList(self,first : str,ent : OCP.Standard.Standard_Transient) -> OCP.TColStd.TColStd_HSequenceOfTransient: ...
    def IGESModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the model as a IGESModel. It can then be consulted (header, product)
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the model. It can then be consulted (header, product)
        """
    def NbRootsForTransfer(self) -> int: 
        """
        Determines the list of root entities from Model which are candidate for a transfer to a Shape (type of entities is PRODUCT) <theReadOnlyVisible> is taken into account to define roots
        """
    def NbShapes(self) -> int: 
        """
        Returns the number of shapes produced by translation.
        """
    def OneShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns all of the results in a single shape which is: - a null shape if there are no results, - a shape if there is one result, - a compound containing the resulting shapes if there are more than one.
        """
    def PrintCheckLoad(self,failsonly : bool,mode : OCP.IFSelect.IFSelect_PrintCount) -> None: 
        """
        Prints the check list attached to loaded data, on the Standard Trace File (starts at std::cout) All messages or fails only, according to <failsonly> mode = 0 : per entity, prints messages mode = 1 : per message, just gives count of entities per check mode = 2 : also gives entity numbers
        """
    def PrintCheckTransfer(self,failsonly : bool,mode : OCP.IFSelect.IFSelect_PrintCount) -> None: 
        """
        Displays check results for the last translation of IGES or STEP entities to Open CASCADE entities. Only fail messages are displayed if failsonly is true. All messages are displayed if failsonly is false. mode determines the contents and the order of the messages according to the terms of the IFSelect_PrintCount enumeration.
        """
    def PrintStatsTransfer(self,what : int,mode : int=0) -> None: 
        """
        Displays the statistics for the last translation. what defines the kind of statistics that are displayed as follows: - 0 gives general statistics (number of translated roots, number of warnings, number of fail messages), - 1 gives root results, - 2 gives statistics for all checked entities, - 3 gives the list of translated entities, - 4 gives warning and fail messages, - 5 gives fail messages only. The use of mode depends on the value of what. If what is 0, mode is ignored. If what is 1, 2 or 3, mode defines the following: - 0 lists the numbers of IGES or STEP entities in the respective model - 1 gives the number, identifier, type and result type for each IGES or STEP entity and/or its status (fail, warning, etc.) - 2 gives maximum information for each IGES or STEP entity (i.e. checks) - 3 gives the number of entities per type of IGES or STEP entity - 4 gives the number of IGES or STEP entities per result type and/or status - 5 gives the number of pairs (IGES or STEP or result type and status) - 6 gives the number of pairs (IGES or STEP or result type and status) AND the list of entity numbers in the IGES or STEP model. If what is 4 or 5, mode defines the warning and fail messages as follows: - if mode is 0 all warnings and checks per entity are returned - if mode is 2 the list of entities per warning is returned. If mode is not set, only the list of all entities per warning is given.
        """
    def PrintTransferInfo(self,failwarn : OCP.IFSelect.IFSelect_PrintFail,mode : OCP.IFSelect.IFSelect_PrintCount) -> None: 
        """
        Prints Statistics and check list for Transfer
        """
    def ReadFile(self,filename : str) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Loads a file and returns the read status Zero for a Model which compies with the Controller
        """
    def RootForTransfer(self,num : int=1) -> OCP.Standard.Standard_Transient: 
        """
        Returns an IGES or STEP root entity for translation. The entity is identified by its rank in a list.
        """
    def SetNorm(self,norm : str) -> bool: 
        """
        Sets a specific norm to <me> Returns True if done, False if <norm> is not available
        """
    def SetReadVisible(self,ReadRoot : bool) -> None: 
        """
        Set the transion of ALL Roots (if theReadOnlyVisible is False) or of Visible Roots (if theReadOnlyVisible is True)

        Set the transion of ALL Roots (if theReadOnlyVisible is False) or of Visible Roots (if theReadOnlyVisible is True)
        """
    def SetWS(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: 
        """
        Sets a specific session to <me>
        """
    def Shape(self,num : int=1) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape resulting from a translation and identified by the rank num. num equals 1 by default. In other words, the first shape resulting from the translation is returned.
        """
    def TransferEntity(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Translates an IGES or STEP entity in the model. true is returned if a shape is produced; otherwise, false is returned.
        """
    def TransferList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> int: 
        """
        Translates a list of entities. Returns the number of IGES or STEP entities that were successfully translated. The list can be produced with GiveList. Warning - This function does not clear the existing output shapes.
        """
    def TransferOne(self,num : int) -> bool: 
        """
        Translates an IGES or STEP entity identified by the rank num in the model. false is returned if no shape is produced.
        """
    def TransferOneRoot(self,num : int=1) -> bool: 
        """
        Translates a root identified by the rank num in the model. false is returned if no shape is produced.
        """
    def TransferRoots(self) -> int: 
        """
        Translates all translatable roots and returns the number of successful translations. Warning - This function clears existing output shapes first.
        """
    def WS(self) -> OCP.XSControl.XSControl_WorkSession: 
        """
        Returns the session used in <me>
        """
    @overload
    def __init__(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IGESControl_ToolContainer(OCP.IGESToBRep.IGESToBRep_ToolContainer, OCP.Standard.Standard_Transient):
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
    def IGESBoundary(self) -> OCP.IGESToBRep.IGESToBRep_IGESBoundary: 
        """
        Returns IGESControl_IGESBoundary
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
class IGESControl_Writer():
    """
    This class creates and writes IGES files from CAS.CADE models. An IGES file can be written to an existing IGES file or to a new one. The translation can be performed in one or several operations. Each translation operation outputs a distinct root entity in the IGES file. To write an IGES file it is possible to use the following sequence: To modify the IGES file header or to change translation parameters it is necessary to use class Interface_Static (see IGESParameters and GeneralParameters).
    """
    def AddEntity(self,ent : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Adds an IGES entity (and the ones it references) to the model
        """
    def AddGeom(self,geom : OCP.Standard.Standard_Transient) -> bool: 
        """
        Translates a Geometry (Surface or Curve) to IGES Entities and adds them to the model Returns True if done, False if geom is neither a Surface or a Curve suitable for IGES or is null
        """
    def AddShape(self,sh : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Translates a Shape to IGES Entities and adds them to the model Returns True if done, False if Shape not suitable for IGES or null
        """
    def ComputeModel(self) -> None: 
        """
        Computes the entities found in the model, which is ready to be written. This contrasts with the default computation of headers only.
        """
    def Model(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the IGES model to be written in output.
        """
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        Returns/Sets the TransferProcess : it contains final results and if some, check messages
        """
    def TransferProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        None
        """
    @overload
    def Write(self,file : str,fnes : bool=False) -> bool: 
        """
        Computes then writes the model to an OStream Returns True when done, false in case of error

        Prepares and writes an IGES model either to an OStream, S or to a file name,CString. Returns True if the operation was performed correctly and False if an error occurred (for instance, if the processor could not create the file).
        """
    @overload
    def Write(self,S : Any,fnes : bool=False) -> bool: ...
    @overload
    def __init__(self,model : OCP.IGESData.IGESData_IGESModel,modecr : int=0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,unit : str,modecr : int=0) -> None: ...
    pass
