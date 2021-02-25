import OCP.XSControl
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.TColStd
import OCP.TCollection
import io
import OCP.Transfer
import OCP.OpenGl
import OCP.IFSelect
import OCP.gp
import OCP.Interface
import OCP.TopoDS
import OCP.Standard
import OCP.TopAbs
__all__  = [
"XSControl",
"XSControl_ConnectedShapes",
"XSControl_Controller",
"XSControl_FuncShape",
"XSControl_Functions",
"XSControl_Reader",
"XSControl_SelectForTransfer",
"XSControl_SignTransferStatus",
"XSControl_TransferReader",
"XSControl_TransferWriter",
"XSControl_Utils",
"XSControl_Vars",
"XSControl_WorkSession",
"XSControl_Writer"
]
class XSControl():
    """
    This package provides complements to IFSelect & Co for control of a session
    """
    @staticmethod
    def Session_s(pilot : OCP.IFSelect.IFSelect_SessionPilot) -> XSControl_WorkSession: 
        """
        Returns the WorkSession of a SessionPilot, but casts it as from XSControl : it then gives access to Control & Transfers
        """
    @staticmethod
    def Vars_s(pilot : OCP.IFSelect.IFSelect_SessionPilot) -> XSControl_Vars: 
        """
        Returns the Vars of a SessionPilot, it is brought by Session it provides access to external variables
        """
    def __init__(self) -> None: ...
    pass
class XSControl_ConnectedShapes(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    From a TopoDS_Shape, or from the entity which has produced it, searches for the shapes, and the entities which have produced them in last transfer, which are adjacent to it by VERTICESFrom a TopoDS_Shape, or from the entity which has produced it, searches for the shapes, and the entities which have produced them in last transfer, which are adjacent to it by VERTICESFrom a TopoDS_Shape, or from the entity which has produced it, searches for the shapes, and the entities which have produced them in last transfer, which are adjacent to it by VERTICES
    """
    @staticmethod
    def AdjacentEntities_s(ashape : OCP.TopoDS.TopoDS_Shape,TP : OCP.Transfer.Transfer_TransientProcess,type : OCP.TopAbs.TopAbs_ShapeEnum) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        This functions considers a shape from a transfer and performs the search function explained above
        """
    def Alternate(self) -> OCP.IFSelect.IFSelect_SelectPointed: 
        """
        Returns the Alternate Definition It is returned modifiable, hence an already defined SelectPointed can be used But if it was not yet defined, it is created the first time
        """
    def CompleteResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities involved by a Selection, i.e. UniqueResult plus the shared entities (directly or not)
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
    def Explore(self,level : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph,explored : OCP.Interface.Interface_EntityIterator) -> bool: 
        """
        Explores an entity : entities from which are connected to that produced by this entity, including itself
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium. "Connected Entities through produced Shapes"
        """
    def FillIterator(self,iter : OCP.IFSelect.IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasAlternate(self) -> bool: 
        """
        Tells if an Alternate List has been set, i.e. : the Alternate Definition is present and set
        """
    def HasInput(self) -> bool: 
        """
        Returns True if the Input Selection is defined, False else
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text saying "(Recursive)" or "(Level nn)" plus specific criterium returned by ExploreLabel (see below)
        """
    def Level(self) -> int: 
        """
        Returns the required exploring level
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Explore on each input entity : it can be rejected, taken for output, or to explore. If the maximum level has not yet been attained, or if no max level is specified, entities to be explored are themselves used as if they were input
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetReader(self,TR : XSControl_TransferReader) -> None: 
        """
        Sets a TransferReader to sort entities : it brings the TransferProcess which may change, while the TransferReader does not
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,TR : XSControl_TransferReader) -> None: ...
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
class XSControl_Controller(OCP.Standard.Standard_Transient):
    """
    This class allows a general X-STEP engine to run generic functions on any interface norm, in the same way. It includes the transfer operations. I.e. it gathers the already available general modules, the engine has just to know itThis class allows a general X-STEP engine to run generic functions on any interface norm, in the same way. It includes the transfer operations. I.e. it gathers the already available general modules, the engine has just to know itThis class allows a general X-STEP engine to run generic functions on any interface norm, in the same way. It includes the transfer operations. I.e. it gathers the already available general modules, the engine has just to know it
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
    def Customise(self,WS : XSControl_WorkSession) -> Any: 
        """
        Customises a WorkSession, by adding to it the recorded items (by AddSessionItem)
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
        Creates a new empty Model ready to receive data of the Norm Used to write data from Imagine to an interface file
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
    def Recorded_s(name : str) -> XSControl_Controller: 
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
        Takes one Shape and transfers it to an InterfaceModel (already created, e.g. by NewModel) Default uses ActorWrite; can be redefined as necessary Returned value is a status, as follows : Done OK , Void : No Result , Fail : Fail (e.g. exception) Error : bad conditions , bad model or null model
        """
    def TransferWriteTransient(self,obj : OCP.Standard.Standard_Transient,FP : OCP.Transfer.Transfer_FinderProcess,model : OCP.Interface.Interface_InterfaceModel,modetrans : int=0,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Takes one Transient Object and transfers it to an InterfaceModel (already created, e.g. by NewModel) (result is recorded in the model by AddWithRefs) FP records produced results and checks
        """
    def WorkLibrary(self) -> OCP.IFSelect.IFSelect_WorkLibrary: 
        """
        Returns the WorkLibrary attached to the Norm. Remark that it has to be in phase with the Protocol (read from field)
        """
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
class XSControl_FuncShape():
    """
    Defines additionnal commands for XSControl to : - control of initialisation (xinit, xnorm, newmodel) - analyse of the result of a transfer (recorded in a TransientProcess for Read, FinderProcess for Write) : statistics, various lists (roots,complete,abnormal), what about one specific entity, producing a model with the abnormal result
    """
    @staticmethod
    def FileAndVar_s(session : XSControl_WorkSession,file : str,var : str,def_ : str,resfile : OCP.TCollection.TCollection_AsciiString,resvar : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Analyses given file name and variable name, with a default name for variables. Returns resulting file name and variable name plus status "file to read"(True) or "already read"(False) In the latter case, empty resfile means no file available
        """
    @staticmethod
    def Init_s() -> None: 
        """
        Defines and loads all functions which work on shapes for XSControl (as ActFunc)
        """
    @staticmethod
    def MoreShapes_s(session : XSControl_WorkSession,list : OCP.TopTools.TopTools_HSequenceOfShape,name : str) -> int: 
        """
        Analyses a name as designating Shapes from a Vars or from XSTEP transfer (last Transfer on Reading). <name> can be : "*" : all the root shapes produced by last Transfer (Read) i.e. considers roots of the TransientProcess a name : a name of a variable DRAW
        """
    def __init__(self) -> None: ...
    pass
class XSControl_Functions():
    """
    Functions from XSControl gives access to actions which can be commanded with the resources provided by XSControl: especially Controller and Transfer
    """
    @staticmethod
    def Init_s() -> None: 
        """
        Defines and loads all functions for XSControl (as ActFunc)
        """
    def __init__(self) -> None: ...
    pass
class XSControl_Reader():
    """
    A groundwork to convert a shape to data which complies with a particular norm. This data can be that of a whole model or that of a specific list of entities in the model. You specify the list using a single selection or a combination of selections. A selection is an operator which computes a list of entities from a list given in input. To specify the input, you can use: - A predefined selection such as "xst-transferrable-roots" - A filter based on a signature. A signature is an operator which returns a string from an entity according to its type. For example: - "xst-type" (CDL) - "iges-level" - "step-type". A filter can be based on a signature by giving a value to be matched by the string returned. For example, "xst-type(Curve)". If no list is specified, the selection computes its list of entities from the whole model. To use this class, you have to initialize the transfer norm first, as shown in the example below. Example: Control_Reader reader; IFSelect_ReturnStatus status = reader.ReadFile (filename.); When using IGESControl_Reader or STEPControl_Reader - as the above example shows - the reader initializes the norm directly. Note that loading the file only stores the data. It does not translate this data. Shapes are accumulated by successive transfers. The last shape is cleared by: - ClearShapes which allows you to handle a new batch - TransferRoots which restarts the list of shapes from scratch.
    """
    def ClearShapes(self) -> None: 
        """
        Clears the list of shapes that may have accumulated in calls to TransferOne or TransferRoot.C
        """
    def GetStatsTransfer(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> Tuple[int, int, int]: 
        """
        Gives statistics about Transfer
        """
    @overload
    def GiveList(self,first : str,ent : OCP.Standard.Standard_Transient) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns a list of entities from the IGES or STEP file according to the following rules: - if first and second are empty strings, the whole file is selected. - if first is an entity number or label, the entity referred to is selected. - if first is a list of entity numbers/labels separated by commas, the entities referred to are selected, - if first is the name of a selection in the worksession and second is not defined, the list contains the standard output for that selection. - if first is the name of a selection and second is defined, the criterion defined by second is applied to the result of the first selection. A selection is an operator which computes a list of entities from a list given in input according to its type. If no list is specified, the selection computes its list of entities from the whole model. A selection can be: - A predefined selection (xst-transferrable-mode) - A filter based on a signature A Signature is an operator which returns a string from an entity according to its type. For example: - "xst-type" (CDL) - "iges-level" - "step-type". For example, if you wanted to select only the advanced_faces in a STEP file you would use the following code: Example Reader.GiveList("xst-transferrable-roots","step-type(ADVANCED_FACE)"); Warning If the value given to second is incorrect, it will simply be ignored.

        Computes a List of entities from the model as follows <first> beeing a Selection, <ent> beeing an entity or a list of entities (as a HSequenceOfTransient) : the standard result of this selection applied to this list if <first> is erroneous, a null handle is returned
        """
    @overload
    def GiveList(self,first : str='',second : str='') -> OCP.TColStd.TColStd_HSequenceOfTransient: ...
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the model. It can then be consulted (header, product)
        """
    def NbRootsForTransfer(self) -> int: 
        """
        Determines the list of root entities which are candidate for a transfer to a Shape, and returns the number of entities in the list
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
    def PrintStatsTransfer(self,what : int,mode : int=0) -> None: 
        """
        Displays the statistics for the last translation. what defines the kind of statistics that are displayed as follows: - 0 gives general statistics (number of translated roots, number of warnings, number of fail messages), - 1 gives root results, - 2 gives statistics for all checked entities, - 3 gives the list of translated entities, - 4 gives warning and fail messages, - 5 gives fail messages only. The use of mode depends on the value of what. If what is 0, mode is ignored. If what is 1, 2 or 3, mode defines the following: - 0 lists the numbers of IGES or STEP entities in the respective model - 1 gives the number, identifier, type and result type for each IGES or STEP entity and/or its status (fail, warning, etc.) - 2 gives maximum information for each IGES or STEP entity (i.e. checks) - 3 gives the number of entities per type of IGES or STEP entity - 4 gives the number of IGES or STEP entities per result type and/or status - 5 gives the number of pairs (IGES or STEP or result type and status) - 6 gives the number of pairs (IGES or STEP or result type and status) AND the list of entity numbers in the IGES or STEP model. If what is 4 or 5, mode defines the warning and fail messages as follows: - if mode is 0 all warnings and checks per entity are returned - if mode is 2 the list of entities per warning is returned. If mode is not set, only the list of all entities per warning is given.

        Displays the statistics for the last translation.
        """
    @overload
    def PrintStatsTransfer(self,theStream : io.BytesIO,what : int,mode : int=0) -> None: ...
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
    def SetWS(self,WS : XSControl_WorkSession,scratch : bool=True) -> None: 
        """
        Sets a specific session to <me>
        """
    def Shape(self,num : int=1) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape resulting from a translation and identified by the rank num. num equals 1 by default. In other words, the first shape resulting from the translation is returned.
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
    def TransferRoots(self,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int: 
        """
        Translates all translatable roots and returns the number of successful translations. Warning - This function clears existing output shapes first.
        """
    def WS(self) -> XSControl_WorkSession: 
        """
        Returns the session used in <me>
        """
    @overload
    def __init__(self,norm : str) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,WS : XSControl_WorkSession,scratch : bool=True) -> None: ...
    pass
class XSControl_SelectForTransfer(OCP.IFSelect.IFSelect_SelectExtract, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection selects the entities which are recognised for transfer by an Actor for Read : current one or another one.This selection selects the entities which are recognised for transfer by an Actor for Read : current one or another one.This selection selects the entities which are recognised for transfer by an Actor for Read : current one or another one.
    """
    def Actor(self) -> OCP.Transfer.Transfer_ActorOfTransientProcess: 
        """
        Returns the Actor used as precised one. Returns a Null Handle for a creation from a TransferReader without any further setting
        """
    def Alternate(self) -> OCP.IFSelect.IFSelect_SelectPointed: 
        """
        Returns the Alternate Definition It is returned modifiable, hence an already defined SelectPointed can be used But if it was not yet defined, it is created the first time
        """
    def CompleteResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities involved by a Selection, i.e. UniqueResult plus the shared entities (directly or not)
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
    def ExtractLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Recognized for Transfer [(current actor)]"
        """
    def FillIterator(self,iter : OCP.IFSelect.IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasAlternate(self) -> bool: 
        """
        Tells if an Alternate List has been set, i.e. : the Alternate Definition is present and set
        """
    def HasInput(self) -> bool: 
        """
        Returns True if the Input Selection is defined, False else
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
        """
    def IsDirect(self) -> bool: 
        """
        Returns True if Sort criterium is Direct, False if Reverse
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text saying "Picked" or "Removed", plus the specific criterium returned by ExtractLabel (see below)
        """
    def Reader(self) -> XSControl_TransferReader: 
        """
        Returns the Reader (if created with a Reader) Returns a Null Handle if not created with a Reader
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetActor(self,act : OCP.Transfer.Transfer_ActorOfTransientProcess) -> None: 
        """
        Sets a precise actor to sort entities This definition oversedes the creation with a TransferReader
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetReader(self,TR : XSControl_TransferReader) -> None: 
        """
        Sets a TransferReader to sort entities : it brings the Actor, which may change, while the TransferReader does not
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True for an Entity which is recognized by the Actor, either the precised one, or the one defined by TransferReader
        """
    def SortInGraph(self,rank : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph) -> bool: 
        """
        Works as Sort but works on the Graph Default directly calls Sort, but it can be redefined If SortInGraph is redefined, Sort should be defined even if not called (to avoid deferred methods in a final class)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    @overload
    def __init__(self,TR : XSControl_TransferReader) -> None: ...
    @overload
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
class XSControl_SignTransferStatus(OCP.IFSelect.IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    This Signatures gives the Transfer Status of an entity, as recorded in a TransferProcess. It can be : - Void : not recorded, or recorded as void with no message (attributes are not taken into account) - Warning : no result, warning message(s), no fail - Fail : no result, fail messages (with or without warning) - Result.. : result, no message (neither warning nor fail) Result.. i.e. Result:TypeName of the result - Result../Warning : result, with warning but no fail - Result../Fail : result, with fail (.e. bad result) - Fail on run : no result yet recorded, no message, but an exception occurred while recording the result (this should not appear and indicates a programming error)This Signatures gives the Transfer Status of an entity, as recorded in a TransferProcess. It can be : - Void : not recorded, or recorded as void with no message (attributes are not taken into account) - Warning : no result, warning message(s), no fail - Fail : no result, fail messages (with or without warning) - Result.. : result, no message (neither warning nor fail) Result.. i.e. Result:TypeName of the result - Result../Warning : result, with warning but no fail - Result../Fail : result, with fail (.e. bad result) - Fail on run : no result yet recorded, no message, but an exception occurred while recording the result (this should not appear and indicates a programming error)This Signatures gives the Transfer Status of an entity, as recorded in a TransferProcess. It can be : - Void : not recorded, or recorded as void with no message (attributes are not taken into account) - Warning : no result, warning message(s), no fail - Fail : no result, fail messages (with or without warning) - Result.. : result, no message (neither warning nor fail) Result.. i.e. Result:TypeName of the result - Result../Warning : result, with warning but no fail - Result../Fail : result, with fail (.e. bad result) - Fail on run : no result yet recorded, no message, but an exception occurred while recording the result (this should not appear and indicates a programming error)
    """
    def AddCase(self,acase : str) -> None: 
        """
        Adds a possible case To be called when creating, IF the list of possible cases for Value is known when starting For instance, for CDL types, rather do not fill this, but for a specific enumeration (such as a status), can be used
        """
    def CaseList(self) -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        Returns the predefined list of possible cases, filled by AddCase Null Handle if no predefined list (hence, to be counted) Useful to filter on really possible vase, for instance, or for a help
        """
    @staticmethod
    def ClassName_s(typnam : str) -> str: 
        """
        From a CDL Type Name, returns the Class part (package dropped) WARNING : buffered, to be immediately copied or printed
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def IntValue_s(val : int) -> str: 
        """
        This procedure converts an Integer to a CString It is a convenient way when the value of a signature has the form of a simple integer value The value is to be used immediately (one buffer only, no copy)
        """
    def IsIntCase(self,hasmin : bool,valmin : int,hasmax : bool,valmax : int) -> bool: 
        """
        Tells if this Signature gives integer values and returns values from SetIntCase if True
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        The label of a Signature uses its name as follow : "Signature : <name>"
        """
    def Map(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the TransientProcess used as precised one Returns a Null Handle for a creation from a TransferReader without any further setting
        """
    @staticmethod
    def MatchValue_s(val : str,text : OCP.TCollection.TCollection_AsciiString,exact : bool) -> bool: 
        """
        Default procedure to tell if a value <val> matches a text with a criterium <exact>. <exact> = True requires equality, else only contained (no reg-exp)
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel,text : OCP.TCollection.TCollection_AsciiString,exact : bool) -> bool: 
        """
        Tells if the value for <ent> in <model> matches a text, with a criterium <exact>. The default definition calls MatchValue Can be redefined
        """
    def Name(self) -> str: 
        """
        Returns an identification of the Signature (a word), given at initialization time Returns the Signature for a Transient object. It is specific of each sub-class of Signature. For a Null Handle, it should provide "" It can work with the model which contains the entity
        """
    def Reader(self) -> XSControl_TransferReader: 
        """
        Returns the Reader (if created with a Reader) Returns a Null Handle if not created with a Reader
        """
    def SetIntCase(self,hasmin : bool,valmin : int,hasmax : bool,valmax : int) -> None: 
        """
        Sets the information data to tell "integer cases" with possible min and max values To be called when creating
        """
    def SetMap(self,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        Sets a precise map to sign entities This definition oversedes the creation with a TransferReader
        """
    def SetReader(self,TR : XSControl_TransferReader) -> None: 
        """
        Sets a TransferReader to work
        """
    def Text(self,ent : OCP.Standard.Standard_Transient,context : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an identification of the Signature (a word), given at initialization time Specialised to consider context as an InterfaceModel
        """
    def Value(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> str: 
        """
        Returns the Signature for a Transient object, as its transfer status
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,TR : XSControl_TransferReader) -> None: ...
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
class XSControl_TransferReader(OCP.Standard.Standard_Transient):
    """
    A TransferReader performs, manages, handles results of, transfers done when reading a file (i.e. from entities of an InterfaceModel, to objects for Imagine)A TransferReader performs, manages, handles results of, transfers done when reading a file (i.e. from entities of an InterfaceModel, to objects for Imagine)A TransferReader performs, manages, handles results of, transfers done when reading a file (i.e. from entities of an InterfaceModel, to objects for Imagine)
    """
    def Actor(self) -> OCP.Transfer.Transfer_ActorOfTransientProcess: 
        """
        Returns the Actor, determined by the Controller, or if this one is unknown, directly set. Once it has been defined, it can then be edited.
        """
    def BeginTransfer(self) -> bool: 
        """
        Defines a new TransferProcess for reading transfer Returns True if done, False if data are not properly defined (the Model, the Actor for Read)
        """
    def CheckList(self,theEnt : OCP.Standard.Standard_Transient,theLevel : int=0) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the CheckList resulting from transferring <ent>, i.e. stored in its recorded form ResultFromModel (empty if transfer successful or not recorded ...)
        """
    def CheckedList(self,theEnt : OCP.Standard.Standard_Transient,WithCheck : OCP.Interface.Interface_CheckStatus=Interface_CheckStatus.Interface_CheckAny,theResult : bool=True) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of starting entities to which a given check status is attached, IN FINAL RESULTS <ent> can be an entity, or the model to query all entities Below, "entities" are, either <ent> plus its sub-transferred, or all the entities of the model
        """
    def Clear(self,theMode : int) -> None: 
        """
        Clears data, according mode : -1 all 0 nothing done +1 final results +2 working data (model, context, transfer process)
        """
    def ClearResult(self,theEnt : OCP.Standard.Standard_Transient,theMode : int) -> bool: 
        """
        Clears recorded result for an entity, according mode <mode> = -1 : true, complete, clearing (erasing result) <mode> >= 0 : simple "stripping", see ResultFromModel, in particular, 0 for simple internal strip, 10 for all but final result, 11 for all : just label, status and filename are kept Returns True when done, False if nothing was to clear
        """
    def Context(self) -> Any: ...
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
    def EntitiesFromShapeList(self,theRes : OCP.TopTools.TopTools_HSequenceOfShape,theMode : int=0) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities from which some shapes were produced : it corresponds to a loop on EntityFromShapeResult, but is optimised
        """
    def EntityFromResult(self,theRes : OCP.Standard.Standard_Transient,theMode : int=0) -> OCP.Standard.Standard_Transient: 
        """
        Returns an entity from which a given result was produced. If <mode> = 0 (D), searches in last root transfers If <mode> = 1, searches in last (root & sub) transfers If <mode> = 2, searches in root recorded results If <mode> = 3, searches in all (root & sub) recordeds <res> can be, either a transient object (result itself) or a binder. For a binder of shape, calls EntityFromShapeResult Returns a Null Handle if <res> not recorded
        """
    def EntityFromShapeResult(self,theRes : OCP.TopoDS.TopoDS_Shape,theMode : int=0) -> OCP.Standard.Standard_Transient: 
        """
        Returns an entity from which a given shape result was produced Returns a Null Handle if <res> not recorded or not a Shape
        """
    def FileName(self) -> str: 
        """
        Returns actual value of file name
        """
    def FinalEntityLabel(self,theEnt : OCP.Standard.Standard_Transient) -> str: 
        """
        Returns the label attached to an entity recorded for final, or an empty string if not recorded
        """
    def FinalEntityNumber(self,theEnt : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the number attached to the entity recorded for final, or zero if not recorded (looks in the ResultFromModel)
        """
    def FinalResult(self,theEnt : OCP.Standard.Standard_Transient) -> OCP.Transfer.Transfer_ResultFromModel: 
        """
        Returns the final result recorded for an entity, as such
        """
    def GetContext(self,theName : str,theType : OCP.Standard.Standard_Type,theCtx : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns the Context attached to a name, if set and if it is Kind of the type, else a Null Handle Returns True if OK, False if no Context
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasChecks(self,theEnt : OCP.Standard.Standard_Transient,FailsOnly : bool) -> bool: 
        """
        Returns True if an entity (with a final result) has checks : - failsonly = False : any kind of check message - failsonly = True : fails only Returns False if <ent> is not recorded
        """
    def HasResult(self,theEnt : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if a final result is recorded AND BRINGS AN EFFECTIVE RESULT (else, it brings only fail messages)
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
    def IsMarked(self,theEnt : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an entity has been asked for transfert, hence it is marked, as : Recorded (a computation has ran, with or without an effective result), or Skipped (case ignored)
        """
    def IsRecorded(self,theEnt : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if a final result is recorded for an entity Remark that it can bring no effective result if transfer has completely failed (FinalResult brings only fail messages ...)
        """
    def IsSkipped(self,theEnt : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an entity is noted as skipped
        """
    def LastCheckList(self) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the CheckList resulting from last TransferRead i.e. from TransientProcess itself, recorded from last Clear
        """
    def LastTransferList(self,theRoots : bool) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities recorded as lastly transferred i.e. from TransientProcess itself, recorded from last Clear If <roots> is True , considers only roots of transfer If <roots> is False, considers all entities bound with result
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the currently set InterfaceModel
        """
    def PrintStats(self,theStream : io.BytesIO,theWhat : int,theMode : int=0) -> None: 
        """
        Prints statistics on current Trace File, according <what> and <mode>. See PrintStatsProcess for details
        """
    @staticmethod
    def PrintStatsOnList_s(theTP : OCP.Transfer.Transfer_TransientProcess,theList : OCP.TColStd.TColStd_HSequenceOfTransient,theWhat : int,theMode : int=0) -> None: 
        """
        Works as PrintStatsProcess, but displays data only on the entities which are in <list> (filter)
        """
    @staticmethod
    def PrintStatsProcess_s(theTP : OCP.Transfer.Transfer_TransientProcess,theWhat : int,theMode : int=0) -> None: 
        """
        This routines prints statistics about a TransientProcess It can be called, by a TransferReader, or isolately Prints are done on the default trace file <what> defines what kind of statistics are to be printed : 0 : basic figures 1 : root results 2 : all recorded (roots, intermediate, checked entities) 3 : abnormal records 4 : check messages (warnings and fails) 5 : fail messages
        """
    def Recognize(self,theEnt : OCP.Standard.Standard_Transient) -> bool: 
        """
        Tells if an entity is recognized as a valid candidate for Transfer. Calls method Recognize from the Actor (if known)
        """
    def RecordResult(self,theEnt : OCP.Standard.Standard_Transient) -> bool: 
        """
        Records a final result of transferring an entity This result is recorded as a ResultFromModel, taken from the TransientProcess Returns True if a result is available, False else
        """
    def RecordedList(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities to which a final result is attached (i.e. processed by RecordResult)
        """
    def ResultFromNumber(self,theNum : int) -> OCP.Transfer.Transfer_ResultFromModel: 
        """
        Returns the final result recorded for a NUMBER of entity (internal use). Null if out of range
        """
    def SetActor(self,theActor : OCP.Transfer.Transfer_ActorOfTransientProcess) -> None: 
        """
        Sets the Actor directly : this value will be used if the Controller is not set
        """
    def SetContext(self,theName : str,theCtx : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets a Context : according to receiving appli, to be interpreted by the Actor
        """
    def SetController(self,theControl : XSControl_Controller) -> None: 
        """
        Sets a Controller. It is required to generate the Actor. Elsewhere, the Actor must be provided directly
        """
    def SetFileName(self,theName : str) -> None: 
        """
        Sets a new value for (loaded) file name
        """
    def SetGraph(self,theGraph : OCP.Interface.Interface_HGraph) -> None: 
        """
        Sets a Graph and its InterfaceModel (calls SetModel)
        """
    def SetModel(self,theModel : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Sets an InterfaceModel. This causes former results, computed from another one, to be lost (see also Clear)
        """
    def SetTransientProcess(self,theTP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        Forces the TransientProcess Remark : it also changes the Model and the Actor, from those recorded in the new TransientProcess
        """
    def ShapeResult(self,theEnt : OCP.Standard.Standard_Transient) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the resulting object as a Shape Null Shape if no result or result not a shape
        """
    def ShapeResultList(self,theRec : bool) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        Returns a list of result Shapes If <rec> is True , sees RecordedList If <rec> is False, sees LastTransferList (last ROOT transfers) For each one, if it is a Shape, it is cumulated to the list If no Shape is found, returns an empty Sequence
        """
    def Skip(self,theEnt : OCP.Standard.Standard_Transient) -> bool: 
        """
        Note that an entity has been required for transfer but no result at all is available (typically : case not implemented) It is not an error, but it gives a specific status : Skipped Returns True if done, False if <ent> is not in starting model
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransferClear(self,theEnt : OCP.Standard.Standard_Transient,theLevel : int=0) -> None: 
        """
        Clears the results attached to an entity if <ents> equates the starting model, clears all results
        """
    def TransferList(self,theList : OCP.TColStd.TColStd_HSequenceOfTransient,theRec : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int: 
        """
        Commands the transfer on reading for a list of entities to data for Imagine, using the selected Actor for Read Returns count of transferred entities, ok or with fails (0/1) If <rec> is True (D), the results are recorded by RecordResult
        """
    def TransferOne(self,theEnt : OCP.Standard.Standard_Transient,theRec : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int: 
        """
        Commands the transfer on reading for an entity to data for Imagine, using the selected Actor for Read Returns count of transferred entities, ok or with fails (0/1) If <rec> is True (D), the result is recorded by RecordResult
        """
    def TransferRoots(self,theGraph : OCP.Interface.Interface_Graph,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int: 
        """
        Transfers the content of the current Interface Model to data handled by Imagine, starting from its Roots (determined by the Graph <G>), using the selected Actor for Read Returns the count of performed root transfers (i.e. 0 if none) or -1 if no actor is defined
        """
    def TransientProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the currently used TransientProcess It is computed from the model by TransferReadRoots, or by BeginTransferRead
        """
    def TransientResult(self,theEnt : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: 
        """
        Returns the resulting object as a Transient Null Handle if no result or result not transient
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
class XSControl_TransferWriter(OCP.Standard.Standard_Transient):
    """
    TransferWriter gives help to control transfer to write a file after having converted data from Cascade/ImagineTransferWriter gives help to control transfer to write a file after having converted data from Cascade/ImagineTransferWriter gives help to control transfer to write a file after having converted data from Cascade/Imagine
    """
    def CheckList(self) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the check-list of last transfer (write), i.e. the check-list currently recorded in the FinderProcess
        """
    def Clear(self,theMode : int) -> None: 
        """
        Clears recorded data according a mode 0 clears FinderProcess (results, checks) -1 create a new FinderProcess
        """
    def Controller(self) -> XSControl_Controller: 
        """
        Returns the currently used Controller
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
    def FinderProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns the FinderProcess itself
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
    def PrintStats(self,theWhat : int,theMode : int=0) -> None: 
        """
        Prints statistics on current Trace File, according what,mode See PrintStatsProcess for details
        """
    def RecognizeShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Tells if a Shape is valid for a transfer to a model Asks the Controller (RecognizeWriteShape)
        """
    def RecognizeTransient(self,theObj : OCP.Standard.Standard_Transient) -> bool: 
        """
        Tells if a transient object (from an application) is a valid candidate for a transfer to a model Asks the Controller (RecognizeWriteTransient) If <obj> is a HShape, calls RecognizeShape
        """
    def ResultCheckList(self,theModel : OCP.Interface.Interface_InterfaceModel) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the check-list of last transfer (write), but tries to bind to each check, the resulting entity in the model instead of keeping the original Mapper, whenever known
        """
    def SetController(self,theCtl : XSControl_Controller) -> None: 
        """
        Sets a new Controller, also sets a new FinderProcess
        """
    def SetFinderProcess(self,theFP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        Sets a new FinderProcess and forgets the former one
        """
    def SetTransferMode(self,theMode : int) -> None: 
        """
        Changes the Transfer Mode
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransferMode(self) -> int: 
        """
        Returns the current Transfer Mode (an Integer) It will be interpreted by the Controller to run Transfers This call form could be later replaced by more specific ones (parameters suited for each norm / transfer case)
        """
    def TransferWriteShape(self,theModel : OCP.Interface.Interface_InterfaceModel,theShape : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Transfers a Shape from CasCade to a model of current norm, according to the last call to SetTransferMode Works by calling the Controller Returns status : =0 if OK, >0 if error during transfer, <0 if transfer badly initialised
        """
    def TransferWriteTransient(self,theModel : OCP.Interface.Interface_InterfaceModel,theObj : OCP.Standard.Standard_Transient,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Transfers a Transient object (from an application) to a model of current norm, according to the last call to SetTransferMode Works by calling the Controller Returns status : =0 if OK, >0 if error during transfer, <0 if transfer badly initialised
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
class XSControl_Utils():
    """
    This class provides various useful utility routines, to facilitate handling of most common data structures : transients (type, type name ...), strings (ascii or extended, pointed or handled or ...), shapes (reading, writing, testing ...), sequences & arrays (of strings, of transients, of shapes ...), ...
    """
    def AppendCStr(self,seqval : OCP.TColStd.TColStd_HSequenceOfHAsciiString,strval : str) -> None: 
        """
        None
        """
    def AppendEStr(self,seqval : OCP.TColStd.TColStd_HSequenceOfHExtendedString,strval : str) -> None: 
        """
        None
        """
    def AppendShape(self,seqv : OCP.TopTools.TopTools_HSequenceOfShape,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AppendTra(self,seqval : OCP.TColStd.TColStd_HSequenceOfTransient,traval : OCP.Standard.Standard_Transient) -> None: 
        """
        None
        """
    def ArrToSeq(self,arr : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def AsciiToExtended(self,str : str) -> str: 
        """
        None
        """
    def BinderShape(self,tr : OCP.Standard.Standard_Transient) -> OCP.TopoDS.TopoDS_Shape: 
        """
        From a Transient, returns a Shape. In fact, recognizes ShapeBinder ShapeMapper and HShape
        """
    def CStrValue(self,list : OCP.Standard.Standard_Transient,num : int) -> str: 
        """
        None
        """
    def CompoundFromSeq(self,seqval : OCP.TopTools.TopTools_HSequenceOfShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Converts a list of Shapes to a Compound (a kind of Shape)
        """
    def DateString(self,yy : int,mm : int,dd : int,hh : int,mn : int,ss : int) -> str: 
        """
        None
        """
    def DateValues(self,text : str) -> Tuple[int, int, int, int, int, int]: 
        """
        None
        """
    def EStrValue(self,list : OCP.Standard.Standard_Transient,num : int) -> str: 
        """
        None
        """
    def ExtendedToAscii(self,str : str) -> str: 
        """
        None
        """
    def IsAscii(self,str : str) -> bool: 
        """
        None
        """
    def IsKind(self,item : OCP.Standard.Standard_Transient,what : OCP.Standard.Standard_Type) -> bool: 
        """
        None
        """
    def NewSeqCStr(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        None
        """
    def NewSeqEStr(self) -> OCP.TColStd.TColStd_HSequenceOfHExtendedString: 
        """
        None
        """
    def NewSeqShape(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        None
        """
    def NewSeqTra(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        None
        """
    def SeqIntValue(self,list : OCP.TColStd.TColStd_HSequenceOfInteger,num : int) -> int: 
        """
        None
        """
    def SeqLength(self,list : OCP.Standard.Standard_Transient) -> int: 
        """
        None
        """
    def SeqToArr(self,seq : OCP.Standard.Standard_Transient,first : int=1) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def ShapeBinder(self,shape : OCP.TopoDS.TopoDS_Shape,hs : bool=True) -> OCP.Standard.Standard_Transient: 
        """
        Creates a Transient Object from a Shape : it is either a Binder (used by functions which require a Transient but can process a Shape, such as viewing functions) or a HShape (according to hs) Default is a HShape
        """
    def ShapeType(self,shape : OCP.TopoDS.TopoDS_Shape,compound : bool) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the type of a Shape : true type if <compound> is False If <compound> is True and <shape> is a Compound, iterates on its items. If all are of the same type, returns this type. Else, returns COMPOUND. If it is empty, returns SHAPE For a Null Shape, returns SHAPE
        """
    def ShapeValue(self,seqv : OCP.TopTools.TopTools_HSequenceOfShape,num : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def SortedCompound(self,shape : OCP.TopoDS.TopoDS_Shape,type : OCP.TopAbs.TopAbs_ShapeEnum,explore : bool,compound : bool) -> OCP.TopoDS.TopoDS_Shape: 
        """
        From a Shape, builds a Compound as follows : explores it level by level If <explore> is False, only COMPOUND items. Else, all items Adds to the result, shapes which comply to <type> + if <type> is WIRE, considers free edges (and makes wires) + if <type> is SHELL, considers free faces (and makes shells) If <compound> is True, gathers items in compounds which correspond to starting COMPOUND,SOLID or SHELL containers, or items directly contained in a Compound
        """
    def ToAString(self,strcon : str) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    @overload
    def ToCString(self,strval : OCP.TCollection.TCollection_HAsciiString) -> str: 
        """
        None

        None
        """
    @overload
    def ToCString(self,strval : OCP.TCollection.TCollection_AsciiString) -> str: ...
    @overload
    def ToEString(self,strval : OCP.TCollection.TCollection_HExtendedString) -> str: 
        """
        None

        None
        """
    @overload
    def ToEString(self,strval : OCP.TCollection.TCollection_ExtendedString) -> str: ...
    @overload
    def ToHString(self,strcon : str) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None

        None
        """
    @overload
    def ToHString(self,strcon : str) -> OCP.TCollection.TCollection_HExtendedString: ...
    def ToXString(self,strcon : str) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def TraValue(self,list : OCP.Standard.Standard_Transient,num : int) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def TraceLine(self,line : str) -> None: 
        """
        Just prints a line into the current Trace File. This allows to better characterise the various trace outputs, as desired.
        """
    def TraceLines(self,lines : OCP.Standard.Standard_Transient) -> None: 
        """
        Just prints a line or a set of lines into the current Trace File. <lines> can be a HAscii/ExtendedString (produces a print without ending line) or a HSequence or HArray1 Of .. (one new line per item)
        """
    def TypeName(self,item : OCP.Standard.Standard_Transient,nopk : bool=False) -> str: 
        """
        Returns the name of the dynamic type of an object, i.e. : If it is a Type, its Name If it is a object not a type, the Name of its DynamicType If it is Null, an empty string If <nopk> is False (D), gives complete name If <nopk> is True, returns class name without package
        """
    def __init__(self) -> None: ...
    pass
class XSControl_Vars(OCP.Standard.Standard_Transient):
    """
    Defines a receptacle for externally defined variables, each one has a nameDefines a receptacle for externally defined variables, each one has a nameDefines a receptacle for externally defined variables, each one has a name
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
    def Set(self,name : str,val : OCP.Standard.Standard_Transient) -> None: 
        """
        None
        """
    def SetPoint(self,name : str,val : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def SetPoint2d(self,name : str,val : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    def SetShape(self,name : str,val : OCP.TopoDS.TopoDS_Shape) -> None: 
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
class XSControl_WorkSession(OCP.IFSelect.IFSelect_WorkSession, OCP.Standard.Standard_Transient):
    """
    This WorkSession completes the basic one, by adding : - use of Controller, with norm selection... - management of transfers (both ways) with auxiliary classes TransferReader and TransferWriter -> these transfers may work with a Context List : its items are given by the user, according to the transfer to be i.e. it is interpreted by the Actors Each item is accessed by a NameThis WorkSession completes the basic one, by adding : - use of Controller, with norm selection... - management of transfers (both ways) with auxiliary classes TransferReader and TransferWriter -> these transfers may work with a Context List : its items are given by the user, according to the transfer to be i.e. it is interpreted by the Actors Each item is accessed by a NameThis WorkSession completes the basic one, by adding : - use of Controller, with norm selection... - management of transfers (both ways) with auxiliary classes TransferReader and TransferWriter -> these transfers may work with a Context List : its items are given by the user, according to the transfer to be i.e. it is interpreted by the Actors Each item is accessed by a Name
    """
    def AddItem(self,item : OCP.Standard.Standard_Transient,active : bool=True) -> int: 
        """
        Adds an Item and returns its attached Ident. Does nothing if <item> is already recorded (and returns its attached Ident) <active> if True commands call to SetActive (see below) Remark : the determined Ident is used if <item> is a Dispatch, to fill the ShareOut
        """
    def AddNamedItem(self,name : str,item : OCP.Standard.Standard_Transient,active : bool=True) -> int: 
        """
        Adds an Item with an attached Name. If the Name is already known in the WorkSession, the older item losts it Returns Ident if Done, 0 else, i.e. if <item> is null If <name> is empty, works as AddItem (i.e. with no name) If <item> is already known but with no attached Name, this method tries to attached a Name to it <active> if True commands call to SetActive (see below)
        """
    def AppliedDispatches(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Returns the ordered list of dispatches stored by the ShareOut
        """
    def BeginSentFiles(self,record : bool) -> None: 
        """
        Commands file sending to clear the list of already sent files, commands to record a new one if <record> is True This list is managed by the ModelCopier when SendSplit is called It allows a global exploitation of the set of sent files
        """
    def CategoryName(self,ent : OCP.Standard.Standard_Transient) -> str: 
        """
        Returns the Category Name determined for an entity it is computed by the class Category Remark : an unknown entity gives an empty string
        """
    def CategoryNumber(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the Category Number determined for an entity it is computed by the class Category An unknown entity (number 0) gives a value -1
        """
    def ChangeModifierRank(self,formodel : bool,before : int,after : int) -> bool: 
        """
        Changes the Rank of a Modifier in the Session : Model Modifiers if <formodel> is True, File Modifiers else the Modifier n0 <before> is put to n0 <after> Return True if Done, False if <before> or <after> out of range
        """
    def CheckOne(self,ent : OCP.Standard.Standard_Transient,complete : bool=True) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns a Check for a single entity, under the form of a CheckIterator (this gives only one form for the user) if <ent> is Null or equates the current Model, it gives the Global Check, else the Check for the given entity <complete> as for ModelCheckList
        """
    def ClearContext(self) -> None: 
        """
        Clears the whole current Context (nullifies it)
        """
    def ClearData(self,theMode : int) -> None: 
        """
        In addition to basic ClearData, clears Transfer and Management for interactive use, for mode = 0,1,2 and over 4 Plus : mode = 5 to clear Transfers (both ways) only mode = 6 to clear enforced results mode = 7 to clear transfers, results
        """
    def ClearFile(self) -> None: 
        """
        Erases all stored data from the File Evaluation (i.e. ALL former naming informations are lost)
        """
    def ClearFinalModifiers(self) -> None: 
        """
        Removes all the Modifiers active in the ModelCopier : they become inactive and they are removed from the Session
        """
    def ClearItems(self) -> None: 
        """
        Clears all the recorded Items : Selections, Dispatches, Modifiers, and Strings & IntParams, with their Idents & Names. Remark that if a Model has been loaded, it is not cleared.
        """
    def ClearShareOut(self,onlydisp : bool) -> None: 
        """
        Clears the list of Dispatches recorded by the ShareOut if <only> disp is True, tha's all. Else, clears also the lists of Modifiers recorded by the ShareOut
        """
    def CombineAdd(self,selcomb : OCP.IFSelect.IFSelect_Selection,seladd : OCP.IFSelect.IFSelect_Selection,atnum : int=0) -> int: 
        """
        Adds an input selection to a SelectCombine (Union or Inters.). Returns new count of inputs for this SelectCombine if Done or 0 if <sel> is not kind of SelectCombine, or if <seladd> or <sel> is not in the WorkSession By default, adding is done at the end of the list Else, it is an insertion to rank <atnum> (usefull for Un-ReDo)
        """
    def CombineRemove(self,selcomb : OCP.IFSelect.IFSelect_Selection,selrem : OCP.IFSelect.IFSelect_Selection) -> bool: 
        """
        Removes an input selection from a SelectCombine (Union or Intersection). Returns True if done, False if <selcomb> is not kind of SelectCombine or <selrem> is not source of <selcomb>
        """
    def ComputeCheck(self,enforce : bool=False) -> bool: 
        """
        Computes the CheckList for the Model currently loaded It can then be used for displays, querries ... Returns True if OK, False else (i.e. no Protocol set, or Model absent). If <enforce> is False, works only if not already done or if a new Model has been loaded from last call. Remark : computation is enforced by every call to SetModel or RunTransformer
        """
    def ComputeCounter(self,counter : OCP.IFSelect.IFSelect_SignCounter,forced : bool=False) -> bool: 
        """
        Computes the content of a SignCounter when it is defined with a Selection, then returns True Returns False if the SignCounter is not defined with a Selection, or if its Selection Mode is inhibited <forced> to work around optimisations
        """
    def ComputeCounterFromList(self,counter : OCP.IFSelect.IFSelect_SignCounter,list : OCP.TColStd.TColStd_HSequenceOfTransient,clear : bool=True) -> bool: 
        """
        Computes the content of a SignCounter from an input list If <list> is Null, uses internal definition of the Counter : a Selection, else the whole Model (recomputation forced) If <clear> is True (D), starts from scratch Else, cumulates computations
        """
    def ComputeGraph(self,enforce : bool=False) -> bool: 
        """
        Computes the Graph used for Selections, Displays ... If a HGraph is already set, with same model as given by method Model, does nothing. Else, computes a new Graph. If <enforce> is given True, computes a new Graph anyway. Remark that a call to ClearGraph will cause ComputeGraph to really compute a new Graph Returns True if Graph is OK, False else (i.e. if no Protocol is set, or if Model is absent or empty).
        """
    def Context(self) -> Any: 
        """
        Returns the current Context List, Null if not defined The Context is given to the TransientProcess for TransferRead
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultFileRoot(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the defined Default File Root. It is used for Dispatches which have no specific root attached. Null Handle if not defined
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self,id : int) -> OCP.IFSelect.IFSelect_Dispatch: 
        """
        Returns a Dispatch, given its Ident in the Session Null result if <id> is not suitable for a Dispatch (undefined, or defined for another kind of variable)
        """
    def DispatchRank(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> int: 
        """
        Returns the rank of a Dispatch in the ShareOut, or 0 if <disp> is not in the ShareOut or not in the WorkSession
        """
    def DumpEntity(self,ent : OCP.Standard.Standard_Transient,level : int,S : io.BytesIO) -> None: 
        """
        Dumps a starting entity according to the current norm. To do this, it calls DumpEntity from WorkLibrary. <level> is to be interpreted for each norm : see specific classes of WorkLibrary for it. Generally, 0 if for very basic (only type ...), greater values give more and more details.
        """
    def DumpModel(self,level : int,S : io.BytesIO) -> None: 
        """
        Lists the content of the Input Model (if there is one) According level : 0 -> gives only count of Entities and Roots 1 -> Lists also Roots; 2 -> Lists all Entities (by TraceType) 3 -> Performs a call to CheckList (Fails) and lists the result 4 -> as 3 but all CheckList (Fails + Warnings) 5,6,7 : as 3 but resp. Count,List,Labels by Fail 8,9,10 : as 4 but resp. Count,List,Labels by message
        """
    def DumpSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Lists a Selection and its Sources (see SelectionIterator), given its rank in the list
        """
    def DumpShare(self) -> None: 
        """
        Dumps contents of the ShareOut (on "cout")
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EntityLabel(self,ent : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label for <ent>, as the Model does If <ent> is not in the Model or if no Model is loaded, a Null Handle is returned
        """
    def EntityName(self,ent : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Name of an Entity This Name is computed by the general service Name Returns a Null Handle if fails
        """
    def ErrorHandle(self) -> bool: 
        """
        Returns the Error Handler status
        """
    def EvalSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> OCP.Interface.Interface_EntityIterator: 
        """
        Evaluates the effect of a Selection applied on the input Model Returned Result remains empty if no input Model has been set
        """
    def EvalSplit(self) -> OCP.IFSelect.IFSelect_PacketList: 
        """
        Returns an Evaluation of the whole ShareOut definition : i.e. how the entities of the starting model are forecast to be sent to various files : list of packets according the dispatches, effective lists of roots for each packet (which determine the content of the corresponding file); plus evaluation of which entities are : forgotten (sent into no file), duplicated (sent into more than one file), sent into a given file. See the class PacketList for more details.
        """
    def EvaluateComplete(self,mode : int=0) -> None: 
        """
        Displays the effect of applying the ShareOut on the input Model. <mode> = 0 (default) : displays only roots for each packet, <mode> = 1 : displays all entities for each packet, plus duplicated entities <mode> = 2 : same as <mode> = 1, plus displays forgotten entities (which are in no packet at all)
        """
    def EvaluateDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch,mode : int=0) -> None: 
        """
        Displays the result of applying a Dispatch on the input Model (also shows Remainder if there is) <mode> = 0 (default), displays nothing else <mode> = 1 : displays also duplicated entities (because of this dispatch) <mode> = 2 : displays the entities of the starting Model which are not taken by this dispatch (forgotten entities) <mode> = 3 : displays both duplicated and forgotten entities Remark : EvaluateComplete displays these data evaluated for for all the dispatches, if there are several
        """
    def EvaluateFile(self) -> None: 
        """
        Performs and stores a File Evaluation. The Results are a List of produced Models and a List of names (Strings), in parallel Fills LastRunCheckList
        """
    def EvaluateSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Displays the list of Entities selected by a Selection (i.e. the result of EvalSelection).
        """
    def FileExtension(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the defined File Extension. Null Handle if not defined
        """
    def FileModel(self,num : int) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns a Model, given its rank in the Evaluation List
        """
    def FileName(self,num : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of a file corresponding to a produced Model, given its rank in the Evaluation List
        """
    def FilePrefix(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the defined File Prefix. Null Handle if not defined
        """
    def FileRoot(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the File Root defined for a Dispatch. Null if no Root Name is defined for it (hence, no File will be produced)
        """
    def FinalModifierIdents(self,formodel : bool) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Fills a Sequence with a list of Idents, those attached to the Modifiers applied to final sending. Model Modifiers if <formodel> is True, File Modifiers else This list is given in the order in which they will be applied (which takes into account the Changes to Modifier Ranks)
        """
    def GeneralModifier(self,id : int) -> OCP.IFSelect.IFSelect_GeneralModifier: 
        """
        Returns a Modifier, given its Ident in the Session Null result if <id> is not suitable for a Modifier (undefined, or defined for another kind of variable)
        """
    def GetModeStat(self) -> bool: 
        """
        Return value of mode defining of filling selection during loading
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GiveFileComplete(self,file : str) -> str: 
        """
        Completes a file name as required, with Prefix and Extension (if defined; for a non-defined item, completes nothing)
        """
    def GiveFileRoot(self,file : str) -> str: 
        """
        Extracts File Root Name from a given complete file name (uses OSD_Path)
        """
    @overload
    def GiveList(self,obj : OCP.Standard.Standard_Transient) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Determines a list of entities from an object : <obj> already HSequenceOfTransient : returned itself <obj> Selection : its Result of Evaluation is returned <obj> an entity of the Model : a HSequence which contains it else, an empty HSequence <obj> the Model it self : ALL its content (not only the roots)

        Computes a List of entities from two alphanums, first and second, as follows : if <first> is a Number or Label of an entity : this entity if <first> is a list of Numbers/Labels : the list of entities if <first> is the name of a Selection in <WS>, and <second> not defined, the standard result of this Selection else, let's consider "first second" : this whole phrase is splitted by blanks, as follows (RECURSIVE CALL) : - the leftest term is the final selection - the other terms define the result of the selection - and so on (the "leftest minus one" is a selection, of which the input is given by the remaining ...)
        """
    @overload
    def GiveList(self,first : str,second : str='') -> OCP.TColStd.TColStd_HSequenceOfTransient: ...
    def GiveListCombined(self,l1 : OCP.TColStd.TColStd_HSequenceOfTransient,l2 : OCP.TColStd.TColStd_HSequenceOfTransient,mode : int) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Combines two lists and returns the result, according to mode : <mode> < 0 : entities in <l1> AND NOT in <l2> <mode> = 0 : entities in <l1> AND in <l2> <mode> > 0 : entities in <l1> OR in <l2>
        """
    def GiveListFromList(self,selname : str,ent : OCP.Standard.Standard_Transient) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Computes a List of entities from the model as follows <first> beeing a Selection or a combination of Selections, <ent> beeing an entity or a list of entities (as a HSequenceOfTransient) : the standard result of this selection applied to this list if <ent> is Null, the standard definition of the selection is used (which contains a default input selection) if <selname> is erroneous, a null handle is returned
        """
    def GiveSelection(self,selname : str) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns a Selection from a Name : - the name of a Selection : this Selection - the name of a Signature + criteria between (..) : a new Selection from this Signature - an entity or a list of entities : a new SelectPointed Else, returns a Null Handle
        """
    def Graph(self) -> OCP.Interface.Interface_Graph: 
        """
        Returns the Computed Graph, for Read only
        """
    def HGraph(self) -> OCP.Interface.Interface_HGraph: 
        """
        Returns the Computed Graph as HGraph (Null Handle if not set)
        """
    def HasModel(self) -> bool: 
        """
        Returns True is a Model has been set
        """
    def HasName(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Item of the WorkSession has an attached Name
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitTransferReader(self,theMode : int) -> None: 
        """
        Sets a Transfer Reader, by internal ways, according mode : 0 recreates it clear, 1 clears it (does not recreate) 2 aligns Roots of TransientProcess from final Results 3 aligns final Results from Roots of TransientProcess 4 begins a new transfer (by BeginTransfer) 5 recreates TransferReader then begins a new transfer
        """
    def IntParam(self,id : int) -> OCP.IFSelect.IFSelect_IntParam: 
        """
        Returns an IntParam, given its Ident in the Session Null result if <id> is not suitable for an IntParam (undefined, or defined for another kind of variable)
        """
    def IntValue(self,it : OCP.IFSelect.IFSelect_IntParam) -> int: 
        """
        Returns Integer Value of an IntParam
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
    def IsLoaded(self) -> bool: 
        """
        Returns True if a Model is defined and really loaded (not empty), a Protocol is set and a Graph has been computed. In this case, the WorkSession can start to work
        """
    def IsReversedSelectExtract(self,sel : OCP.IFSelect.IFSelect_Selection) -> bool: 
        """
        Returns True if <sel> a Reversed SelectExtract, False else
        """
    def Item(self,id : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns an Item, given its Ident. Returns a Null Handle if no Item corresponds to this Ident.
        """
    def ItemIdent(self,item : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the Ident attached to an Item in the WorkSession, or Zero if it is unknown
        """
    def ItemIdents(self,type : OCP.Standard.Standard_Type) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Fills a Sequence with the List of Idents attached to the Items of which Type complies with (IsKind) <type> (alphabetic order) Remark : <type> = TYPE(Standard_Transient) gives all the Idents which are suitable in the WorkSession
        """
    def ItemLabel(self,id : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a Label which illustrates the content of an Item, given its Ident. This Label is : - for a Text Parameter, "Text:<text value>" - for an Integer Parameter, "Integer:<integer value>" - for a Selection, a Dispatch or a Modifier, its Label (see these classes) - for any other kind of Variable, its cdl type
        """
    def ItemNames(self,type : OCP.Standard.Standard_Type) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Fills a Sequence with the list of the Names attached to Items of which Type complies with (IsKind) <type> (alphabetic order) Remark : <type> = TYPE(Standard_Transient) gives all the Names
        """
    def ItemNamesForLabel(self,label : str) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Fills a Sequence with the NAMES of the control items, of which the label matches <label> (contain it) : see NextIdentForLabel Search mode is fixed to "contained" If <label> is empty, returns all Names
        """
    def ItemSelection(self,item : OCP.Standard.Standard_Transient) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection of a Dispatch or a GeneralModifier. Returns a Null Handle if none is defined or <item> not good type
        """
    def LastRunCheckList(self) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the Check List produced by the last execution of either : EvaluateFile(for Split), SendSplit, SendAll, SendSelected, RunTransformer-RunModifier Cleared by SetModel or ClearData(1) The field is protected, hence a specialized WorkSession may fill it
        """
    def ListEntities(self,iter : OCP.Interface.Interface_EntityIterator,mode : int,S : io.BytesIO) -> None: 
        """
        Internal method which displays an EntityIterator <mode> 0 gives short display (only entity numbers) 1 gives a more complete trace (1 line per Entity) (can be used each time a trace has to be output from a list) 2 gives a form suitable for givelist : (n1,n2,n3...)
        """
    def ListFinalModifiers(self,formodel : bool) -> None: 
        """
        Lists the Modifiers of the session (for each one, displays its Label). Listing is done following Ranks (Modifiers are invoked following their ranks) Model Modifiers if <formodel> is True, File Modifiers else
        """
    def ListItems(self,label : str='') -> None: 
        """
        Lists the Labels of all Items of the WorkSession If <label> is defined, lists labels which contain it
        """
    def LoadedFile(self) -> str: 
        """
        Returns the filename used to load current model empty if unknown
        """
    def MapReader(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the TransientProcess(internal data for TransferReader)
        """
    def MaxIdent(self) -> int: 
        """
        Returns the Maximum Value for an Item Identifier. It can be greater to the count of known Items, because some can have been removed
        """
    def MaxSendingCount(self) -> int: 
        """
        Returns the greater count of different files in which any of the starting entities could be sent. Before any file output, this count is 0. Ideal count is 1. More than 1 means that duplications occur.
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model of the Work Session (Null Handle if none) should be C++ : return const &
        """
    def ModelCheckList(self,complete : bool=True) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the Check List for the Model currently loaded : <complete> = True : complete (syntactic & semantic messages), computed if not yet done <complete> = False : only syntactic (check file form)
        """
    def ModelCopier(self) -> OCP.IFSelect.IFSelect_ModelCopier: 
        """
        Gives access to the complete ModelCopier
        """
    def ModelModifier(self,id : int) -> OCP.IFSelect.IFSelect_Modifier: 
        """
        Returns a Model Modifier, given its Ident in the Session, i.e. typed as a Modifier (not simply a GeneralModifier) Null result if <id> is not suitable for a Modifier (undefined, or defined for another kind of variable)
        """
    def ModifierRank(self,item : OCP.IFSelect.IFSelect_GeneralModifier) -> int: 
        """
        Returns the Rank of a Modifier given its Ident. Model or File Modifier according its type (ModelModifier or not) Remember that Modifiers are applied sequencially following their Rank : first Model Modifiers then File Modifiers Rank is given by rank of call to AddItem and can be changed by ChangeModifierRank
        """
    def Name(self,item : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Name attached to an Item as a Variable of this WorkSession. If <item> is Null or not recorded, returns an empty string.
        """
    def NameIdent(self,name : str) -> int: 
        """
        Returns the Ident attached to a Name, 0 if name not recorded
        """
    @overload
    def NamedItem(self,name : OCP.TCollection.TCollection_HAsciiString) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Item which corresponds to a Variable, given its Name (whatever the type of this Item). Returns a Null Handle if this Name is not recorded

        Same as above, but <name> is given through a Handle Especially Usefull with methods SelectionNames, etc...
        """
    @overload
    def NamedItem(self,name : str) -> OCP.Standard.Standard_Transient: ...
    def NbFiles(self) -> int: 
        """
        Returns the count of produced Models
        """
    def NbFinalModifiers(self,formodel : bool) -> int: 
        """
        Returns the count of Modifiers applied to final sending Model Modifiers if <formodel> is True, File Modifiers else (i.e. Modifiers which apply once the Models have been filled)
        """
    def NbSources(self,sel : OCP.IFSelect.IFSelect_Selection) -> int: 
        """
        Returns the count of Input Selections known for a Selection, or 0 if <sel> not in the WorkSession. This count is one for a SelectDeduct / SelectExtract kind, two for SelectControl kind, variable for a SelectCombine (Union/Intersection), zero else
        """
    def NbStartingEntities(self) -> int: 
        """
        Returns the count of Entities stored in the Model, or 0
        """
    def NewIntParam(self,name : str='') -> OCP.IFSelect.IFSelect_IntParam: 
        """
        Creates a new IntParam. A Name can be set (Optional) Returns the created IntParam, or a Null Handle in case of Failure (see AddItem/AddNamedItem)
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        produces and returns a new Model well conditionned It is produced by the Norm Controller It can be Null (if this function is not implemented)
        """
    def NewParamFromStatic(self,statname : str,name : str='') -> OCP.Standard.Standard_Transient: 
        """
        Creates a parameter as being bound to a Static If the Static is Integer, this creates an IntParam bound to it by its name. Else this creates a String which is the value of the Static. Returns a null handle if <statname> is unknown as a Static
        """
    def NewSelectPointed(self,list : OCP.TColStd.TColStd_HSequenceOfTransient,name : str) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Creates a new Selection, of type SelectPointed, its content starts with <list>. A name must be given (can be empty)
        """
    def NewTextParam(self,name : str='') -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Creates a new (empty) TextParam. A Name can be set (Optional) Returns the created TextParam (as an HAsciiString), or a Null Handle in case of Failure (see AddItem/AddNamedItem)
        """
    def NewTransformStandard(self,copy : bool,name : str='') -> OCP.IFSelect.IFSelect_Transformer: 
        """
        Creates and returns a TransformStandard, empty, with its Copy Option (True = Copy, False = On the Spot) and an optional name. To a TransformStandard, the method SetAppliedModifier applies
        """
    def NextIdentForLabel(self,label : str,id : int,mode : int=0) -> int: 
        """
        For query by Label with possible iterations Searches the Ident of which Item has a Label which matches a given one, the search starts from an initial Ident. Returns the first found Ident which follows <id>, or ZERO
        """
    def NormAdaptor(self) -> XSControl_Controller: 
        """
        Returns the norm controller itself
        """
    def NumberFromLabel(self,val : str,afternum : int=0) -> int: 
        """
        From a given label in Model, returns the corresponding number Starts from first entity by Default, may start after a given number : this number may be given negative, its absolute value is then considered. Hence a loop on NumberFromLabel may be programmed (stop test is : returned value positive or null)
        """
    def PrintCheckList(self,S : io.BytesIO,checklist : OCP.Interface.Interface_CheckIterator,failsonly : bool,mode : OCP.IFSelect.IFSelect_PrintCount) -> None: 
        """
        Prints a CheckIterator to the current Trace File, controlled with the current Model complete or fails only, according to <failsonly> <mode> defines the mode of printing 0 : sequential, according entities; else with a CheckCounter 1 : according messages, count of entities 2 : id but with list of entities, designated by their numbers 3 : as 2 but with labels of entities
        """
    def PrintEntityStatus(self,ent : OCP.Standard.Standard_Transient,S : io.BytesIO) -> None: 
        """
        Prints main informations about an entity : its number, type, validity (and checks if any), category, shareds and sharings.. mutable because it can recompute checks as necessary
        """
    def PrintSignatureList(self,S : io.BytesIO,signlist : OCP.IFSelect.IFSelect_SignatureList,mode : OCP.IFSelect.IFSelect_PrintCount) -> None: 
        """
        Prints a SignatureList to the current Trace File, controlled with the current Model <mode> defines the mode of printing (see SignatureList)
        """
    def PrintTransferStatus(self,theNum : int,theWri : bool,theS : io.BytesIO) -> bool: 
        """
        Prints the transfer status of a transferred item, as beeing the Mapped n0 <num>, from MapWriter if <wri> is True, or from MapReader if <wri> is False Returns True when done, False else (i.e. num out of range)
        """
    def Protocol(self) -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Protocol. Null Handle if not yet set should be C++ : return const &
        """
    def QueryCheckList(self,chl : OCP.Interface.Interface_CheckIterator) -> None: 
        """
        Loads data from a check iterator to query status on it
        """
    def QueryCheckStatus(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Determines check status for an entity regarding last call to QueryCheckList : -1 : <ent> unknown in the model, ignored 0 : no check at all, immediate or inherited thru Graph 1 : immediate warning (no fail), no inherited check 2 : immediate fail, no inherited check +10 : idem but some inherited warning (no fail) +20 : idem but some inherited fail
        """
    def QueryParent(self,entdad : OCP.Standard.Standard_Transient,entson : OCP.Standard.Standard_Transient) -> int: 
        """
        Determines if <entdad> is parent of <entson> (in the graph), returns : -1 if no; 0 if <entdad> = <entson> 1 if immediate parent, > 1 if parent, gives count of steps
        """
    def ReadFile(self,filename : str) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Reads a file with the WorkLibrary (sets Model and LoadedFile) Returns a integer status which can be : RetDone if OK, RetVoid if no Protocol not defined, RetError for file not found, RetFail if fail during read
        """
    def ReadStream(self,theName : str,theIStream : io.BytesIO) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Reads a file from stream with the WorkLibrary (sets Model and LoadedFile) Returns a integer status which can be : RetDone if OK, RetVoid if no Protocol not defined, RetError for file not found, RetFail if fail during read
        """
    def RemoveItem(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Removes an Item given its Ident. Returns False if <id> is attached to no Item in the WorkSession. For a Named Item, also removes its Name.
        """
    def RemoveName(self,name : str) -> bool: 
        """
        Removes a Name without removing the Item Returns True if Done, False else (Name not recorded)
        """
    def RemoveNamedItem(self,name : str) -> bool: 
        """
        Removes an Item from the Session, given its Name Returns True if Done, False else (Name not recorded) (Applies only on Item which are Named)
        """
    def ResetAppliedModifier(self,modif : OCP.IFSelect.IFSelect_GeneralModifier) -> bool: 
        """
        Resets a GeneralModifier to be applied Returns True if done, False if <modif> was not applied
        """
    def ResetItemSelection(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Resets input Selection which was set by SetItemSelection Same conditions as for SetItemSelection Returns True if done, False if <item> is not in the WorkSession
        """
    def Result(self,theEnt : OCP.Standard.Standard_Transient,theMode : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the result attached to a starting entity If <mode> = 0, returns Final Result If <mode> = 1, considers Last Result If <mode> = 2, considers Final, else if absent, Last returns it as Transient, if result is not transient returns the Binder <mode> = 10,11,12 idem but returns the Binder itself (if it is not, e.g. Shape, returns the Binder) <mode> = 20, returns the ResultFromModel
        """
    def RunModifier(self,modif : OCP.IFSelect.IFSelect_Modifier,copy : bool) -> int: 
        """
        Runs a Modifier on Starting Model. It can modify entities, or add new ones. But the Model or the Protocol is unchanged. The Modifier is applied on each entity of the Model. See also RunModifierSelected Fills LastRunCheckList
        """
    def RunModifierSelected(self,modif : OCP.IFSelect.IFSelect_Modifier,sel : OCP.IFSelect.IFSelect_Selection,copy : bool) -> int: 
        """
        Acts as RunModifier, but the Modifier is applied on the list determined by a Selection, rather than on the whole Model If the selection is a null handle, the whole model is taken
        """
    def RunTransformer(self,transf : OCP.IFSelect.IFSelect_Transformer) -> int: 
        """
        Runs a Transformer on starting Model, which can then be edited or replaced by a new one. The Protocol can also be changed. Fills LastRunCheckList
        """
    def SelectNorm(self,theNormName : str) -> bool: 
        """
        Selects a Norm defined by its name. A Norm is described and handled by a Controller Returns True if done, False if <normname> is unknown
        """
    def SelectedNorm(self,theRsc : bool=False) -> str: 
        """
        Returns the name of the last Selected Norm. If none is defined, returns an empty string By default, returns the complete name of the norm If <rsc> is True, returns the short name used for resource
        """
    def Selection(self,id : int) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns a Selection, given its Ident in the Session Null result if <id> is not suitable for a Selection (undefined, or defined for another kind of variable)
        """
    def SelectionResult(self,sel : OCP.IFSelect.IFSelect_Selection) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the result of a Selection, computed by EvalSelection (see above) under the form of a HSequence (hence, it can be used by a frontal-engine logic). It can be empty Returns a Null Handle if <sel> is not in the WorkSession
        """
    def SelectionResultFromList(self,sel : OCP.IFSelect.IFSelect_Selection,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the result of a Selection, by forcing its input with a given list <list> (unless <list> is Null). RULES : <list> applies only for a SelectDeduct kind Selection : its Input is considered : if it is a SelectDeduct kind Selection, its Input is considered, etc... until an Input is not a Deduct/Extract : its result is replaced by <list> and all the chain of deductions is applied
        """
    def SendAll(self,filename : str,computegraph : bool=False) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Sends the starting Model into one file, without splitting, managing remaining data or anything else. <computegraph> true commands the Graph to be recomputed before sending : required when a Model is filled in several steps
        """
    def SendSelected(self,filename : str,sel : OCP.IFSelect.IFSelect_Selection,computegraph : bool=False) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Sends a part of the starting Model into one file, without splitting. But remaining data are managed. <computegraph> true commands the Graph to be recomputed before sending : required when a Model is filled in several steps
        """
    def SendSplit(self) -> bool: 
        """
        Performs creation of derived files from the input Model Takes its data (sub-models and names), from result EvaluateFile if active, else by dynamic Evaluation (not stored) After SendSplit, result of EvaluateFile is Cleared Fills LastRunCheckList
        """
    def SentFiles(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of recorded sent files, or a Null Handle is recording has not been enabled
        """
    def SentList(self,count : int=-1) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of Entities sent in files, accourding the count of files each one has been sent (these counts are reset by SetModel or SetRemaining(Forget) ) stored in Graph Status <count> = -1 (default) is for ENtities sent at least once <count> = 0 is for the Remaining List (entities not yet sent) <count> = 1 is for entities sent in one and only one file (the ideal case) Remaining Data are computed on each Sending/Copying output files (see methods EvaluateFile and SendSplit) Graph Status is 0 for Remaining Entity, <count> for Sent into <count> files This status is set to 0 (not yet sent) for all by SetModel and by SetRemaining(mode=Forget,Display)
        """
    def SetActive(self,item : OCP.Standard.Standard_Transient,mode : bool) -> bool: 
        """
        Following the type of <item> : - Dispatch : Adds or Removes it in the ShareOut & FileNaming - GeneralModifier : Adds or Removes it for final sending (i.e. in the ModelCopier) Returns True if it did something, False else (state unchanged)
        """
    def SetAllContext(self,theContext : Any) -> None: 
        """
        Sets the current Context List, as a whole Sets it to the TransferReader
        """
    def SetAppliedModifier(self,modif : OCP.IFSelect.IFSelect_GeneralModifier,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Sets a GeneralModifier to be applied to an item : - item = ShareOut : applies for final sending (all dispatches) - item is a Dispatch : applies for this dispatch only Returns True if done, False if <modif> or <item> not in <me>
        """
    def SetControl(self,sel : OCP.IFSelect.IFSelect_Selection,sc : OCP.IFSelect.IFSelect_Selection,formain : bool=True) -> bool: 
        """
        Sets an Input Selection, Main if <formain> is True, Second else (as <sc>) to a SelectControl (as <sel>). Returns True if Done, False if <sel> is not a SelectControl, or <sc> or <sel> is not in the WorkSession
        """
    def SetController(self,theCtl : XSControl_Controller) -> None: 
        """
        Selects a Norm defined by its Controller itself
        """
    def SetDefaultFileRoot(self,name : str) -> bool: 
        """
        Defines a Default File Root Name. Clears it is <name> = "" Returns True if OK, False if <name> already set for a Dispatch
        """
    def SetErrorHandle(self,toHandle : bool) -> None: 
        """
        Changes the Error Handler status (by default, it is not set)
        """
    def SetFileExtension(self,name : str) -> None: 
        """
        Defines a File Extension
        """
    def SetFilePrefix(self,name : str) -> None: 
        """
        Defines a File Prefix
        """
    def SetFileRoot(self,disp : OCP.IFSelect.IFSelect_Dispatch,name : str) -> bool: 
        """
        Defines a Root for a Dispatch If <name> is empty, clears Root Name This has as effect to inhibit the production of File by <disp> Returns False if <disp> is not in the WorkSession or if a root name is already defined for it
        """
    def SetInputSelection(self,sel : OCP.IFSelect.IFSelect_Selection,input : OCP.IFSelect.IFSelect_Selection) -> bool: 
        """
        Sets an Input Selection (as <input>) to a SelectExtract or a SelectDeduct (as <sel>). Returns True if Done, False if <sel> is neither a SelectExtract nor a SelectDeduct, or not in the WorkSession
        """
    def SetIntValue(self,it : OCP.IFSelect.IFSelect_IntParam,val : int) -> bool: 
        """
        Changes the Integer Value of an IntParam Returns True if Done, False if <it> is not in the WorkSession
        """
    def SetItemSelection(self,item : OCP.Standard.Standard_Transient,sel : OCP.IFSelect.IFSelect_Selection) -> bool: 
        """
        Sets a Selection as input for an item, according its type : if <item> is a Dispatch : as Final Selection if <item> is a GeneralModifier (i.e. any kind of Modifier) : as Selection used to filter entities to modify <sel> Null causes this Selection to be nullified Returns False if <item> is not of a suitable type, or <item> or <sel> is not in the WorkSession
        """
    def SetLibrary(self,theLib : OCP.IFSelect.IFSelect_WorkLibrary) -> None: 
        """
        Sets a WorkLibrary, which will be used to Read and Write Files
        """
    def SetLoadedFile(self,theFileName : str) -> None: 
        """
        Stores the filename used for read for setting the model It is cleared by SetModel and ClearData(1)
        """
    def SetMapReader(self,theTP : OCP.Transfer.Transfer_TransientProcess) -> bool: 
        """
        Changes the Map Reader, i.e. considers that the new one defines the relevant read results (forgets the former ones) Returns True when done, False in case of bad definition, i.e. if Model from TP differs from that of Session
        """
    def SetMapWriter(self,theFP : OCP.Transfer.Transfer_FinderProcess) -> bool: 
        """
        Changes the Map Reader, i.e. considers that the new one defines the relevant read results (forgets the former ones) Returns True when done, False if <FP> is Null
        """
    def SetModeStat(self,theMode : bool) -> None: 
        """
        Set value of mode responsible for precence of selections after loading If mode set to true that different selections will be accessible after loading else selections will be not accessible after loading( for economy memory in applicatios)
        """
    def SetModel(self,model : OCP.Interface.Interface_InterfaceModel,clearpointed : bool=True) -> None: 
        """
        Sets a Model as input : this will be the Model from which the ShareOut will work if <clearpointed> is True (default) all SelectPointed items are cleared, else they must be managed by the caller Remark : SetModel clears the Graph, recomputes it if a Protocol is set and if the Model is not empty, of course
        """
    def SetModelContent(self,sel : OCP.IFSelect.IFSelect_Selection,keep : bool) -> bool: 
        """
        Defines a new content from the former one If <keep> is True, it is given by entities selected by Selection <sel> (and all shared entities) Else, it is given by all the former content but entities selected by the Selection <sel> (and properly shared ones) Returns True if done. Returns False if the selected list (from <sel>) is empty, hence nothing is done
        """
    def SetModelCopier(self,copier : OCP.IFSelect.IFSelect_ModelCopier) -> None: 
        """
        Sets a new ModelCopier. Fills Items which its content
        """
    def SetParams(self,params : Any,uselist : OCP.OpenGl.OpenGl_ColorFormats) -> None: 
        """
        Sets a list of Parameters, i.e. TypedValue, to be handled through an Editor The two lists are parallel, if <params> is longer than <uses>, surnumeral parameters are for general use
        """
    def SetProtocol(self,protocol : OCP.Interface.Interface_Protocol) -> None: 
        """
        Sets a Protocol, which will be used to determine Graphs, to Read and to Write Files
        """
    def SetRemaining(self,mode : OCP.IFSelect.IFSelect_RemainMode) -> bool: 
        """
        Processes Remaining data (after having sent files), mode : Forget : forget remaining info (i.e. clear all "Sent" status) Compute : compute and keep remaining (does nothing if : remaining is empty or if no files has been sent) Display : display entities recorded as remaining Undo : restore former state of data (after Remaining(1) ) Returns True if OK, False else (i.e. mode = 2 and Remaining List is either empty or takes all the entities, or mode = 3 and no former computation of remaining data was done)
        """
    def SetSelectPointed(self,sel : OCP.IFSelect.IFSelect_Selection,list : OCP.TColStd.TColStd_HSequenceOfTransient,mode : int) -> bool: 
        """
        Changes the content of a Selection of type SelectPointed According <mode> : 0 set <list> as new content (clear former) 1 : adds <list> to actual content -1 : removes <list> from actual content Returns True if done, False if <sel> is not a SelectPointed
        """
    def SetShareOut(self,shareout : OCP.IFSelect.IFSelect_ShareOut) -> None: 
        """
        Sets a new ShareOut. Fills Items which its content Warning : data from the former ShareOut are lost
        """
    def SetSignType(self,signtype : OCP.IFSelect.IFSelect_Signature) -> None: 
        """
        Sets a specific Signature to be the SignType, i.e. the Signature which will determine TypeName from the Model (basic function). It is recorded in the GTool This Signature is also set as "xst-sign-type" (reserved name)
        """
    def SetTextValue(self,par : OCP.TCollection.TCollection_HAsciiString,val : str) -> bool: 
        """
        Changes the Text Value of a TextParam (an HAsciiString) Returns True if Done, False if <it> is not in the WorkSession
        """
    def SetTransferReader(self,theTR : XSControl_TransferReader) -> None: 
        """
        Sets a Transfer Reader, which manages transfers on reading
        """
    def SetVars(self,theVars : XSControl_Vars) -> None: 
        """
        None
        """
    def ShareOut(self) -> OCP.IFSelect.IFSelect_ShareOut: 
        """
        Returns the ShareOut defined at creation time
        """
    def Shareds(self,ent : OCP.Standard.Standard_Transient) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities shared by <ent> (can be empty) Returns a null Handle if <ent> is unknown
        """
    def Sharings(self,ent : OCP.Standard.Standard_Transient) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities sharing <ent> (can be empty) Returns a null Handle if <ent> is unknown
        """
    def SignCounter(self,id : int) -> OCP.IFSelect.IFSelect_SignCounter: 
        """
        Returns a SignCounter from its ident in the Session Null result if <id> is not suitable for a SignCounter (undefined, or defined for another kind of variable)
        """
    def SignType(self) -> OCP.IFSelect.IFSelect_Signature: 
        """
        Returns the current SignType
        """
    def SignValue(self,sign : OCP.IFSelect.IFSelect_Signature,ent : OCP.Standard.Standard_Transient) -> str: 
        """
        Returns the Value computed by a Signature for an Entity Returns an empty string if the entity does not belong to the loaded model
        """
    def Signature(self,id : int) -> OCP.IFSelect.IFSelect_Signature: 
        """
        Returns a Signature, given its Ident in the Session Null result if <id> is not suitable for a Signature (undefined, or defined for another kind of variable)
        """
    def Source(self,sel : OCP.IFSelect.IFSelect_Selection,num : int=1) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the <num>th Input Selection of a Selection (see NbSources). Returns a Null Handle if <sel> is not in the WorkSession or if <num> is out of the range <1-NbSources> To obtain more details, see the method Sources
        """
    def Sources(self,sel : OCP.IFSelect.IFSelect_Selection) -> OCP.IFSelect.IFSelect_SelectionIterator: 
        """
        Returns the Selections which are source of Selection, given its rank in the List of Selections (see SelectionIterator) Returned value is empty if <num> is out of range or if <sel> is not in the WorkSession
        """
    def StartingEntity(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns an Entity stored in the Model of the WorkSession (Null Handle is no Model or num out of range)
        """
    def StartingNumber(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the Number of an Entity in the Model (0 if no Model set or <ent> not in the Model)
        """
    def TextParam(self,id : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a TextParam, given its Ident in the Session Null result if <id> is not suitable for a TextParam (undefined, or defined for another kind of variable)
        """
    def TextValue(self,par : OCP.TCollection.TCollection_HAsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Text Value of a TextParam (a String) or an empty string if <it> is not in the WorkSession
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToggleSelectExtract(self,sel : OCP.IFSelect.IFSelect_Selection) -> bool: 
        """
        Toggles the Sense (Direct <-> Reversed) of a SelectExtract Returns True if Done, False if <sel> is not a SelectExtract or is not in the WorkSession
        """
    def TraceDumpEntity(self,ent : OCP.Standard.Standard_Transient,level : int) -> None: 
        """
        Dumps an entity from the current Model as inherited DumpEntity on currently defined Default Trace File (<level> interpreted according to the Norm, see WorkLibrary)
        """
    def TraceDumpModel(self,mode : int) -> None: 
        """
        Dumps the current Model (as inherited DumpModel), on currently defined Default Trace File (default is standard output)
        """
    def TraceStatics(self,use : int,mode : int=0) -> None: 
        """
        Traces the Statics attached to a given use number If <use> is given positive (normal), the trace is embedded with a header and a trailer If <use> is negative, just values are printed (this allows to make compositions) Remark : use number 5 commands use -2 to be traced Remark : use numbers 4 and 6 command use -3 to be traced
        """
    def TransferReadOne(self,theEnts : OCP.Standard.Standard_Transient,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int: 
        """
        Commands the transfer of, either one entity, or a list I.E. calls the TransferReader after having analysed <ents> It is cumulated from the last BeginTransfer <ents> is processed by GiveList, hence : - <ents> a Selection : its SelectionResult - <ents> a HSequenceOfTransient : this list - <ents> the Model : in this specific case, all the roots, with no cumulation of former transfers (TransferReadRoots)
        """
    def TransferReadRoots(self,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> int: 
        """
        Commands the transfer of all the root entities of the model i.e. calls TransferRoot from the TransferReader with the Graph No cumulation with former calls to TransferReadOne
        """
    def TransferReader(self) -> XSControl_TransferReader: 
        """
        Returns the Transfer Reader, Null if not set
        """
    def TransferWriteCheckList(self) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the check-list of last transfer (write) It is recorded in the FinderProcess, but it must be bound with resulting entities (in the resulting file model) rather than with original objects (in fact, their mappers)
        """
    def TransferWriteShape(self,theShape : OCP.TopoDS.TopoDS_Shape,theCompGraph : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Transfers a Shape from CasCade to a model of current norm, according to the last call to SetModeWriteShape Returns status :Done if OK, Fail if error during transfer, Error if transfer badly initialised
        """
    def TransferWriter(self) -> XSControl_TransferWriter: 
        """
        Returns the Transfer Reader, Null if not set
        """
    def Transformer(self,id : int) -> OCP.IFSelect.IFSelect_Transformer: 
        """
        Returns a Transformer, given its Ident in the Session Null result if <id> is not suitable for a Transformer (undefined, or defined for another kind of variable)
        """
    def UsesAppliedModifier(self,modif : OCP.IFSelect.IFSelect_GeneralModifier) -> OCP.Standard.Standard_Transient: 
        """
        Returns the item on which a GeneralModifier is applied : the ShareOut, or a given Dispatch Returns a Null Handle if <modif> is not applied
        """
    def ValidityName(self,ent : OCP.Standard.Standard_Transient) -> str: 
        """
        Returns the Validity Name determined for an entity it is computed by the class SignValidity Remark : an unknown entity gives an empty string
        """
    def Vars(self) -> XSControl_Vars: 
        """
        None
        """
    def WorkLibrary(self) -> OCP.IFSelect.IFSelect_WorkLibrary: 
        """
        Returns the WorkLibrary. Null Handle if not yet set should be C++ : return const &
        """
    @overload
    def WriteFile(self,filename : str) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Writes the current Interface Model globally to a File, and returns a write status which can be : Done OK, Fail file could not be written, Error no norm is selected Remark : It is a simple, one-file writing, other operations are available (such as splitting ...) which calls SendAll

        Writes a sub-part of the current Interface Model to a File, as defined by a Selection <sel>, recomputes the Graph, and returns a write status which can be : Done OK, Fail file could not be written, Error no norm is selected Remark : It is a simple, one-file writing, other operations are available (such as splitting ...) which calls SendSelected
        """
    @overload
    def WriteFile(self,filename : str,sel : OCP.IFSelect.IFSelect_Selection) -> OCP.IFSelect.IFSelect_ReturnStatus: ...
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
class XSControl_Writer():
    """
    This class gives a simple way to create then write a Model compliant to a given norm, from a Shape The model can then be edited by tools by other appropriate tools
    """
    def Model(self,newone : bool=False) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the produced model. Produces a new one if not yet done or if <newone> is True This method allows for instance to edit product or header data before writing
        """
    def PrintStatsTransfer(self,what : int,mode : int=0) -> None: 
        """
        Prints Statistics about Transfer
        """
    def SetNorm(self,norm : str) -> bool: 
        """
        Sets a specific norm to <me> Returns True if done, False if <norm> is not available
        """
    def SetWS(self,WS : XSControl_WorkSession,scratch : bool=True) -> None: 
        """
        Sets a specific session to <me>
        """
    def TransferShape(self,sh : OCP.TopoDS.TopoDS_Shape,mode : int=0,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Transfers a Shape according to the mode
        """
    def WS(self) -> XSControl_WorkSession: 
        """
        Returns the session used in <me>
        """
    def WriteFile(self,filename : str) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Writes the produced model
        """
    @overload
    def __init__(self,norm : str) -> None: ...
    @overload
    def __init__(self,WS : XSControl_WorkSession,scratch : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
