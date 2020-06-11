import OCP.IFSelect
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.OpenGl
import OCP.TCollection
import OCP.Standard
import OCP.Message
import OCP.TColStd
import OCP.Interface
import OCP.IFGraph
__all__  = [
"IFSelect",
"IFSelect_Activator",
"IFSelect_Act",
"IFSelect_AppliedModifiers",
"IFSelect_SessionDumper",
"IFSelect_SignatureList",
"IFSelect_ContextModif",
"IFSelect_ContextWrite",
"IFSelect_Dispatch",
"IFSelect_DispPerCount",
"IFSelect_DispPerFiles",
"IFSelect_DispPerOne",
"IFSelect_DispPerSignature",
"IFSelect_DispGlobal",
"IFSelect_EditForm",
"IFSelect_EditValue",
"IFSelect_Editor",
"IFSelect_Functions",
"IFSelect_GeneralModifier",
"IFSelect_SignCounter",
"IFSelect_TSeqOfSelection",
"IFSelect_IntParam",
"IFSelect_ListEditor",
"IFSelect_ModelCopier",
"IFSelect_Modifier",
"IFSelect_ModifReorder",
"IFSelect_ModifEditForm",
"IFSelect_PacketList",
"IFSelect_ParamEditor",
"IFSelect_PrintCount",
"IFSelect_PrintFail",
"IFSelect_RemainMode",
"IFSelect_ReturnStatus",
"IFSelect_Selection",
"IFSelect_SelectDeduct",
"IFSelect_SelectBase",
"IFSelect_SelectCombine",
"IFSelect_SelectControl",
"IFSelect_SelectAnyList",
"IFSelect_SelectDiff",
"IFSelect_SelectEntityNumber",
"IFSelect_SelectExtract",
"IFSelect_SelectExplore",
"IFSelect_SelectAnyType",
"IFSelect_SelectFlag",
"IFSelect_SelectInList",
"IFSelect_SelectIncorrectEntities",
"IFSelect_SelectIntersection",
"IFSelect_SelectModelEntities",
"IFSelect_SelectModelRoots",
"IFSelect_SelectPointed",
"IFSelect_SelectRange",
"IFSelect_SelectRootComps",
"IFSelect_SelectRoots",
"IFSelect_SelectSent",
"IFSelect_SelectShared",
"IFSelect_SelectSharing",
"IFSelect_SelectSignature",
"IFSelect_SelectSignedShared",
"IFSelect_SelectSignedSharing",
"IFSelect_SelectSuite",
"IFSelect_SelectType",
"IFSelect_SelectUnion",
"IFSelect_SelectUnknownEntities",
"IFSelect_SelectErrorEntities",
"IFSelect_SelectionIterator",
"IFSelect_SequenceOfAppliedModifiers",
"IFSelect_SequenceOfGeneralModifier",
"IFSelect_SequenceOfInterfaceModel",
"IFSelect_BasicDumper",
"IFSelect_SessionFile",
"IFSelect_SessionPilot",
"IFSelect_ShareOut",
"IFSelect_ShareOutResult",
"IFSelect_Signature",
"IFSelect_SignCategory",
"IFSelect_GraphCounter",
"IFSelect_SignMultiple",
"IFSelect_SignType",
"IFSelect_SignValidity",
"IFSelect_SignAncestor",
"IFSelect_CheckCounter",
"IFSelect_TSeqOfDispatch",
"IFSelect_HSeqOfSelection",
"IFSelect_Transformer",
"IFSelect_TransformStandard",
"IFSelect_WorkLibrary",
"IFSelect_WorkSession",
"IFSelect_CountByItem",
"IFSelect_CountSummary",
"IFSelect_EditComputed",
"IFSelect_EditDynamic",
"IFSelect_EditProtected",
"IFSelect_EditRead",
"IFSelect_Editable",
"IFSelect_EntitiesByItem",
"IFSelect_FailAndWarn",
"IFSelect_FailOnly",
"IFSelect_GeneralInfo",
"IFSelect_ItemsByEntity",
"IFSelect_ListByItem",
"IFSelect_Mapping",
"IFSelect_Optional",
"IFSelect_RemainCompute",
"IFSelect_RemainDisplay",
"IFSelect_RemainForget",
"IFSelect_RemainUndo",
"IFSelect_ResultCount",
"IFSelect_RetDone",
"IFSelect_RetError",
"IFSelect_RetFail",
"IFSelect_RetStop",
"IFSelect_RetVoid",
"IFSelect_ShortByItem"
]
class IFSelect():
    """
    Gives tools to manage Selecting a group of Entities processed by an Interface, for instance to divide up an original Model (from a File) to several smaller ones They use description of an Interface Model as a graph
    """
    @staticmethod
    def RestoreSession_s(WS : IFSelect_WorkSession,file : str) -> bool: 
        """
        Restore the state of a WorkSession from IFSelect, by using a SessionFile from IFSelect. Returns True if Done, False in case of Error on Writing. <file> gives the name of the File to be used (this avoids to export the class SessionFile).
        """
    @staticmethod
    def SaveSession_s(WS : IFSelect_WorkSession,file : str) -> bool: 
        """
        Saves the state of a WorkSession from IFSelect, by using a SessionFile from IFSelect. Returns True if Done, False in case of Error on Writing. <file> gives the name of the File to be produced (this avoids to export the class SessionFile).
        """
    def __init__(self) -> None: ...
    pass
class IFSelect_Activator(OCP.Standard.Standard_Transient):
    """
    Defines the general frame for working with a SessionPilot. Each Activator treats a set of Commands. Commands are given as alphanumeric strings. They can be of two main forms : - classic, to list, evaluate, enrich the session (by itself) : no specific remark, its complete execution must be described - creation of a new item : instead of creatinf it plus adding it to the session (which is a classic way), it is possible to create it and make it recorded by the SessionPilot : then, the Pilot will add it to the session; this way allows the Pilot to manage itself named itemsDefines the general frame for working with a SessionPilot. Each Activator treats a set of Commands. Commands are given as alphanumeric strings. They can be of two main forms : - classic, to list, evaluate, enrich the session (by itself) : no specific remark, its complete execution must be described - creation of a new item : instead of creatinf it plus adding it to the session (which is a classic way), it is possible to create it and make it recorded by the SessionPilot : then, the Pilot will add it to the session; this way allows the Pilot to manage itself named itemsDefines the general frame for working with a SessionPilot. Each Activator treats a set of Commands. Commands are given as alphanumeric strings. They can be of two main forms : - classic, to list, evaluate, enrich the session (by itself) : no specific remark, its complete execution must be described - creation of a new item : instead of creatinf it plus adding it to the session (which is a classic way), it is possible to create it and make it recorded by the SessionPilot : then, the Pilot will add it to the session; this way allows the Pilot to manage itself named items
    """
    def Add(self,number : int,command : str) -> None: 
        """
        Allows a self-definition by an Activator of the Commands it processes, call the class method Adding (mode 0)
        """
    def AddSet(self,number : int,command : str) -> None: 
        """
        Same as Add but specifies that this command is candidate for xset (creation of items, xset : named items; mode 1)
        """
    @staticmethod
    def Adding_s(actor : IFSelect_Activator,number : int,command : str,mode : int) -> None: 
        """
        Records, in a Dictionary available for all the Activators, the command title an Activator can process, attached with its number, proper for this Activator <mode> allows to distinguish various execution modes 0: default mode; 1 : for xset
        """
    @staticmethod
    def Commands_s(mode : int=-1,command : str='') -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        Returns, for a root of command title, the list of possible commands. <mode> : -1 (D) for all commands if <commands> is empty -1 + command : about a Group , >= 0 see Adding By default, it returns the whole list of known commands.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Do(self,number : int,pilot : IFSelect_SessionPilot) -> IFSelect_ReturnStatus: 
        """
        Tries to execute a Command Line. <number> is the number of the command for this Activator. It Must forecast to record the result of the execution, for need of Undo-Redo Must Returns : 0 for a void command (not to be recorded), 1 if execution OK, -1 if command incorrect, -2 if error on execution
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def File(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Group(self) -> str: 
        """
        None
        """
    def Help(self,number : int) -> str: 
        """
        Sends a short help message for a given command identified by it number for this Activator (must take one line max)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    @staticmethod
    def Mode_s(command : str) -> int: 
        """
        Returns mode recorded for a command. -1 if not found
        """
    @staticmethod
    def Remove_s(command : str) -> None: 
        """
        Removes a Command, if it is recorded (else, does nothing)
        """
    @staticmethod
    def Select_s(command : str,number : int,actor : IFSelect_Activator) -> bool: 
        """
        Selects, for a Command given by its title, an actor with its command number. Returns True if found, False else
        """
    def SetForGroup(self,group : str,file : str='') -> None: 
        """
        Group and SetGroup define a "Group of commands" which correspond to an Activator. Default is "XSTEP" Also a file may be attached
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class IFSelect_Act(IFSelect_Activator, OCP.Standard.Standard_Transient):
    """
    Act gives a simple way to define and add functions to be ran from a SessionPilot, as follows :Act gives a simple way to define and add functions to be ran from a SessionPilot, as follows :Act gives a simple way to define and add functions to be ran from a SessionPilot, as follows :
    """
    def Add(self,number : int,command : str) -> None: 
        """
        Allows a self-definition by an Activator of the Commands it processes, call the class method Adding (mode 0)
        """
    @staticmethod
    def AddFSet_s(name : str,help : str,func : Any) -> None: 
        """
        AddFSet_s(name: str, help: str, func: IFSelect_ReturnStatus (opencascade::handle<IFSelect_SessionPilot> const&)) -> None

        Adds a function with its name and help : creates an Act then records it as function for XSET (i.e. to create control item)
        """
    @staticmethod
    def AddFunc_s(name : str,help : str,func : Any) -> None: 
        """
        AddFunc_s(name: str, help: str, func: IFSelect_ReturnStatus (opencascade::handle<IFSelect_SessionPilot> const&)) -> None

        Adds a function with its name and help : creates an Act then records it as normal function
        """
    def AddSet(self,number : int,command : str) -> None: 
        """
        Same as Add but specifies that this command is candidate for xset (creation of items, xset : named items; mode 1)
        """
    @staticmethod
    def Adding_s(actor : IFSelect_Activator,number : int,command : str,mode : int) -> None: 
        """
        Records, in a Dictionary available for all the Activators, the command title an Activator can process, attached with its number, proper for this Activator <mode> allows to distinguish various execution modes 0: default mode; 1 : for xset
        """
    @staticmethod
    def Commands_s(mode : int=-1,command : str='') -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        Returns, for a root of command title, the list of possible commands. <mode> : -1 (D) for all commands if <commands> is empty -1 + command : about a Group , >= 0 see Adding By default, it returns the whole list of known commands.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Do(self,number : int,pilot : IFSelect_SessionPilot) -> IFSelect_ReturnStatus: 
        """
        Execution of Command Line. remark that <number> is senseless because each Act brings one and only one function
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def File(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Group(self) -> str: 
        """
        None
        """
    def Help(self,number : int) -> str: 
        """
        Short Help for commands : returns the help given to create
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    @staticmethod
    def Mode_s(command : str) -> int: 
        """
        Returns mode recorded for a command. -1 if not found
        """
    @staticmethod
    def Remove_s(command : str) -> None: 
        """
        Removes a Command, if it is recorded (else, does nothing)
        """
    @staticmethod
    def Select_s(command : str,number : int,actor : IFSelect_Activator) -> bool: 
        """
        Selects, for a Command given by its title, an actor with its command number. Returns True if found, False else
        """
    def SetForGroup(self,group : str,file : str='') -> None: 
        """
        Group and SetGroup define a "Group of commands" which correspond to an Activator. Default is "XSTEP" Also a file may be attached
        """
    @staticmethod
    def SetGroup_s(group : str,file : str='') -> None: 
        """
        Changes the default group name for the following Acts group empty means to come back to default from Activator Also a file name can be precised (to query by getsource)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,name : str,help : str,func : Any) -> None: 
        """
        __init__(self: OCP.IFSelect.IFSelect_Act, name: str, help: str, func: IFSelect_ReturnStatus (opencascade::handle<IFSelect_SessionPilot> const&)) -> None
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
class IFSelect_AppliedModifiers(OCP.Standard.Standard_Transient):
    """
    This class allows to memorize and access to the modifiers which are to be applied to a file. To each modifier, is bound a list of integers (optionnal) : if this list is absent, the modifier applies to all the file. Else, it applies to the entities designated by these numbers in the produced file.This class allows to memorize and access to the modifiers which are to be applied to a file. To each modifier, is bound a list of integers (optionnal) : if this list is absent, the modifier applies to all the file. Else, it applies to the entities designated by these numbers in the produced file.This class allows to memorize and access to the modifiers which are to be applied to a file. To each modifier, is bound a list of integers (optionnal) : if this list is absent, the modifier applies to all the file. Else, it applies to the entities designated by these numbers in the produced file.
    """
    def AddModif(self,modif : IFSelect_GeneralModifier) -> bool: 
        """
        Records a modifier. By default, it is to apply on all a produced file. Further calls to AddNum will restrict this. Returns True if done, False if too many modifiers are already recorded
        """
    def AddNum(self,nument : int) -> bool: 
        """
        Adds a number of entity of the output file to be applied on. If a sequence of AddNum is called after AddModif, this Modifier will be applied on the list of designated entities. Else, it will be applied on all the file Returns True if done, False if no modifier has yet been added
        """
    def Count(self) -> int: 
        """
        Returns the count of recorded modifiers
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
    def IsForAll(self) -> bool: 
        """
        Returns True if the applied modifier queried by last call to Item is to be applied to all the produced file. Else, <entcount> returned by Item gives the count of entity numbers, each one is queried by ItemNum
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self,num : int,modif : IFSelect_GeneralModifier,entcount : int) -> bool: 
        """
        Returns the description for applied modifier n0 <num> : the modifier itself, and the count of entities to be applied on. If no specific list of number has been defined, returns the total count of entities of the file If this count is zero, then the modifier applies to all the file (see below). Else, the numbers are then queried by calls to ItemNum between 1 and <entcount> Returns True if OK, False if <num> is out of range
        """
    def ItemList(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Returns the list of entities to be applied on (see Item) as a HSequence (IsForAll produces the complete list of all the entity numbers of the file
        """
    def ItemNum(self,nument : int) -> int: 
        """
        Returns a numero of entity to be applied on, given its rank in the list. If no list is defined (i.e. for all the file), returns <nument> itself, to give all the entities of the file Returns 0 if <nument> out of range
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,nbmax : int,nbent : int) -> None: ...
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
class IFSelect_SessionDumper(OCP.Standard.Standard_Transient):
    """
    A SessionDumper is called by SessionFile. It takes into account a set of classes (such as Selections, Dispatches ...). SessionFile writes the Type (as defined by cdl) of each Item and its general Parameters. It manages the names of the Items.A SessionDumper is called by SessionFile. It takes into account a set of classes (such as Selections, Dispatches ...). SessionFile writes the Type (as defined by cdl) of each Item and its general Parameters. It manages the names of the Items.A SessionDumper is called by SessionFile. It takes into account a set of classes (such as Selections, Dispatches ...). SessionFile writes the Type (as defined by cdl) of each Item and its general Parameters. It manages the names of the Items.
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
    @staticmethod
    def First_s() -> IFSelect_SessionDumper: 
        """
        Returns the First item of the Library of Dumper. The Next ones are then obtained by Next on the returned items
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Next(self) -> IFSelect_SessionDumper: 
        """
        Returns the Next SesionDumper in the Library. Returns a Null Handle at the End.
        """
    def ReadOwn(self,file : IFSelect_SessionFile,type : OCP.TCollection.TCollection_AsciiString,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Recognizes a Type (given as <type>) then Creates an Item of this Type with the Own Parameter, as required. Returns True if it has recognized the Type (in this case, it is assumed to have created the Item, returned as <item>), False else : in that case, SessionFile will try another SessionDumper in the Library. ReadOwn can use these methods from SessionFile to access Own Parameters : NbOwnParams, IsVoid, IsText, TextValue, ItemValue
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteOwn(self,file : IFSelect_SessionFile,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Writes the Own Parameters of a given Item, if it forecast to manage its Type. Returns True if it has recognized the Type of the Item (in this case, it is assumed to have written the Own Parameters if there are some), False else : in that case, SessionFile will try another SessionDumper in the Library. WriteOwn can use these methods from SessionFile : SendVoid, SendItem, SendText, and if necessary, WorkSession.
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
class IFSelect_SignatureList(OCP.Standard.Standard_Transient):
    """
    A SignatureList is given as result from a Counter (any kind) It gives access to a list of signatures, with counts, and optionally with list of corresponding entitiesA SignatureList is given as result from a Counter (any kind) It gives access to a list of signatures, with counts, and optionally with list of corresponding entitiesA SignatureList is given as result from a Counter (any kind) It gives access to a list of signatures, with counts, and optionally with list of corresponding entities
    """
    def Add(self,ent : OCP.Standard.Standard_Transient,sign : str) -> None: 
        """
        Adds an entity with its signature, i.e. : - counts an item more for <sign> - if record-list status is set, records the entity Accepts a null entity (the signature is then for the global model). But if the string is empty, counts a Null item.
        """
    def Clear(self) -> None: 
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
    def Entities(self,sign : str) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities attached to a signature It is empty if <sign> has not been recorded It is a Null Handle if the list of entities is not known
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasEntities(self) -> bool: 
        """
        Returns True if the list of Entities is aknowledged, else the method Entities will always return a Null Handle
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,name : str,count : Any,list : Any,nbnuls : int) -> None: 
        """
        Aknowledges the list in once. Name identifies the Signature
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def LastValue(self) -> str: 
        """
        Returns the last value recorded by Add (only if SignMode set) Cleared by Clear or Init
        """
    def List(self,root : str='') -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of signatures, as a sequence of strings (but without their respective counts). It is ordered. By default, for all the signatures. If <root> is given non empty, for the signatures which begin by <root>
        """
    def Name(self) -> str: 
        """
        Returns the recorded Name. Remark : default is "..." (no SetName called)
        """
    def NbNulls(self) -> int: 
        """
        Returns the count of null entities
        """
    def NbTimes(self,sign : str) -> int: 
        """
        Returns the number of times a signature was counted, 0 if it has not been recorded at all
        """
    def PrintCount(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints the counts of items (not the list)
        """
    def PrintList(self,S : OCP.Message.Message_Messenger,model : OCP.Interface.Interface_InterfaceModel,mod : IFSelect_PrintCount=IFSelect_PrintCount.IFSelect_ListByItem) -> None: 
        """
        Prints the lists of items, if they are present (else, prints a message "no list available") Uses <model> to determine for each entity to be listed, its number, and its specific identifier (by PrintLabel) <mod> gives a mode for printing : - CountByItem : just count (as PrintCount) - ShortByItem : minimum i.e. count plus 5 first entity numbers - ShortByItem(D) complete list of entity numbers (0: "Global") - EntitiesByItem : list of (entity number/PrintLabel from the model) other modes are ignored
        """
    def PrintSum(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints a summary Item which has the greatest count of entities For items which are numeric values : their count, maximum, minimum values, cumul, average
        """
    def SetList(self,withlist : bool) -> None: 
        """
        Changes the record-list status. The list is not cleared but its use changes
        """
    def SetName(self,name : str) -> None: 
        """
        Defines a name for a SignatureList (used to print it)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,withlist : bool=False) -> None: ...
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
    def ModeSignOnly(self) -> bool:
        """
        :type: bool
        """
    @ModeSignOnly.setter
    def ModeSignOnly(self, arg1: bool) -> None:
        pass
    pass
class IFSelect_ContextModif():
    """
    This class gathers various informations used by Model Modifiers apart from the target model itself, and the CopyTool which must be passed directly.
    """
    def AddCheck(self,check : OCP.Interface.Interface_Check) -> None: 
        """
        Adds a Check to the CheckList. If it is empty, nothing is done If it concerns an Entity from the Original Model (by SetEntity) to which another Check is attached, it is merged to it. Else, it is added or merged as to GlobalCheck.
        """
    def AddFail(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: 
        """
        Adds a Fail Message for an Entity from the original Model If <start> is not an Entity from the original model (e.g. the model itself) this message is added to Global Check.
        """
    def AddWarning(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: 
        """
        Adds a Warning Message for an Entity from the original Model If <start> is not an Entity from the original model (e.g. the model itself) this message is added to Global Check.
        """
    @overload
    def CCheck(self,num : int=0) -> OCP.Interface.Interface_Check: 
        """
        Returns a Check given an Entity number (in the original Model) by default a Global Check. Creates it the first time. It can then be acknowledged on the spot, in condition that the caller works by reference ("Interface_Check& check = ...")

        Returns a Check attached to an Entity from the original Model It can then be acknowledged on the spot, in condition that the caller works by reference ("Interface_Check& check = ...")
        """
    @overload
    def CCheck(self,start : OCP.Standard.Standard_Transient) -> OCP.Interface.Interface_Check: ...
    def CheckList(self) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the complete CheckList
        """
    def Control(self) -> OCP.Interface.Interface_CopyControl: 
        """
        Returns the map for a direct use, if required
        """
    def FileName(self) -> str: 
        """
        Returns File Name (can be empty)
        """
    def HasFileName(self) -> bool: 
        """
        Returns True if a non empty file name has been defined
        """
    def IsForAll(self) -> bool: 
        """
        Returns True if no filter is defined : a Modifier has to work on all entities of the resulting (target) model
        """
    def IsForNone(self) -> bool: 
        """
        Returns True if Select has determined that a Modifier may not be run (filter defined and empty)
        """
    def IsSelected(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if a starting item has been transferred and selected
        """
    def IsTransferred(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if a starting item has been transferred
        """
    def More(self) -> bool: 
        """
        Returns True until the iteration has finished
        """
    def Next(self) -> None: 
        """
        Advances the iteration
        """
    def OriginalGraph(self) -> OCP.Interface.Interface_Graph: 
        """
        Returns the original Graph (compared to OriginalModel, it gives more query capabilitites)
        """
    def OriginalModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the original model
        """
    def Protocol(self) -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Protocol (Null if not set)
        """
    def Select(self,list : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        This method requires ContextModif to be applied with a filter. If a ModelModifier is defined with a Selection criterium, the result of this Selection is used as a filter : - if none of its items has been transferred, the modification does not apply at all - else, the Modifier can query for what entities were selected and what are their results - if this method is not called before working, the Modifier has to work on the whole Model
        """
    def SelectedCount(self) -> int: 
        """
        Returns the count of selected and transferred items
        """
    def SelectedOriginal(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of original selected items. See also the iteration
        """
    def SelectedResult(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of resulting counterparts of selected items. See also the iteration
        """
    def SetProtocol(self,proto : OCP.Interface.Interface_Protocol) -> None: 
        """
        Allows to transmit a Protocol as part of a ContextModif
        """
    def Start(self) -> None: 
        """
        Starts an iteration on selected items. It takes into account IsForAll/IsForNone, by really iterating on all selected items.
        """
    def Trace(self,mess : str='') -> None: 
        """
        Traces the modification of the current entity (see above, ValueOriginal and ValueResult) for default trace level >= 2. To be called on each indivudual entity really modified <mess> is an optionnal additional message
        """
    def TraceModifier(self,modif : IFSelect_GeneralModifier) -> None: 
        """
        Traces the application of a Modifier. Works with default trace File and Level. Fills the trace if default trace level is at least 1. Traces the Modifier (its Label) and its Selection if there is one (its Label). To be called after Select (because status IsForAll is printed) Worths to trace a global modification. See also Trace below
        """
    def ValueOriginal(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current selected item in the original model
        """
    def ValueResult(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the result counterpart of current selected item (in the target model)
        """
    @overload
    def __init__(self,graph : OCP.Interface.Interface_Graph,filename : str='') -> None: ...
    @overload
    def __init__(self,graph : OCP.Interface.Interface_Graph,TC : OCP.Interface.Interface_CopyTool,filename : str='') -> None: ...
    pass
class IFSelect_ContextWrite():
    """
    This class gathers various informations used by File Modifiers apart from the writer object, which is specific of the norm and of the physical format
    """
    def AddCheck(self,check : OCP.Interface.Interface_Check) -> None: 
        """
        Adds a Check to the CheckList. If it is empty, nothing is done If it concerns an Entity from the Model (by SetEntity) to which another Check is attached, it is merged to it. Else, it is added or merged as to GlobalCheck.
        """
    def AddFail(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: 
        """
        Adds a Fail Message for an Entity from the Model If <start> is not an Entity from the model (e.g. the model itself) this message is added to Global Check.
        """
    def AddWarning(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: 
        """
        Adds a Warning Message for an Entity from the Model If <start> is not an Entity from the model (e.g. the model itself) this message is added to Global Check.
        """
    def AppliedModifiers(self) -> IFSelect_AppliedModifiers: 
        """
        Returns the object AppliedModifiers
        """
    @overload
    def CCheck(self,start : OCP.Standard.Standard_Transient) -> OCP.Interface.Interface_Check: 
        """
        Returns a Check given an Entity number (in the Model) by default a Global Check. Creates it the first time. It can then be acknowledged on the spot, in condition that the caller works by reference ("Interface_Check& check = ...")

        Returns a Check attached to an Entity from the Model It can then be acknowledged on the spot, in condition that the caller works by reference ("Interface_Check& check = ...")
        """
    @overload
    def CCheck(self,num : int=0) -> OCP.Interface.Interface_Check: ...
    def CheckList(self) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the complete CheckList
        """
    def FileModifier(self) -> IFSelect_GeneralModifier: 
        """
        Returns the currently active File Modifier. Cast to be done Null if not properly set : must be test IsNull after casting
        """
    def FileName(self) -> str: 
        """
        Returns the File Name
        """
    def Graph(self) -> OCP.Interface.Interface_Graph: 
        """
        Returns the Graph, either given when created, else created the first time it is queried
        """
    def IsForAll(self) -> bool: 
        """
        Returns True if the current modifier is to be applied to the whole model. Else, a restricted list of selected entities is defined, it can be exploited by the File Modifier
        """
    def IsForNone(self) -> bool: 
        """
        Returns True if no modifier is currently set
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model
        """
    def More(self) -> bool: 
        """
        Returns True until the iteration has finished
        """
    def NbEntities(self) -> int: 
        """
        Returns the total count of selected entities
        """
    def NbModifiers(self) -> int: 
        """
        Returns the count of recorded File Modifiers
        """
    def Next(self) -> None: 
        """
        Advances the iteration
        """
    def Protocol(self) -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Protocol;
        """
    def SetModifier(self,numod : int) -> bool: 
        """
        Sets active the File Modifier n0 <numod> Then, it prepares the list of entities to consider, if any Returns False if <numod> out of range
        """
    def Start(self) -> None: 
        """
        Starts an iteration on selected items. It takes into account IsForAll/IsForNone, by really iterating on all selected items.
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current selected entity in the model
        """
    @overload
    def __init__(self,model : OCP.Interface.Interface_InterfaceModel,proto : OCP.Interface.Interface_Protocol,applieds : IFSelect_AppliedModifiers,filename : str) -> None: ...
    @overload
    def __init__(self,hgraph : OCP.Interface.Interface_HGraph,proto : OCP.Interface.Interface_Protocol,applieds : IFSelect_AppliedModifiers,filename : str) -> None: ...
    pass
class IFSelect_Dispatch(OCP.Standard.Standard_Transient):
    """
    This class allows to describe how a set of Entities has to be dispatched into resulting Packets : a Packet is a sub-set of the initial set of entities.This class allows to describe how a set of Entities has to be dispatched into resulting Packets : a Packet is a sub-set of the initial set of entities.This class allows to describe how a set of Entities has to be dispatched into resulting Packets : a Packet is a sub-set of the initial set of entities.
    """
    def CanHaveRemainder(self) -> bool: 
        """
        Returns True if a Dispatch can have a Remainder, i.e. if its criterium can let entities apart. It is a potential answer, remainder can be empty at run-time even if answer is True. (to attach a RemainderFromDispatch Selection is not allowed if answer is True). Default answer given here is False (can be redefined)
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
    def FinalSelection(self) -> IFSelect_Selection: 
        """
        Returns the Final Selection of a Dispatch we 'd like : C++ : return const &
        """
    def GetEntities(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Gets Unique Root Entities from the Final Selection, given an input Graph This the starting step for an Evaluation (Packets - Remainder)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasRootName(self) -> bool: 
        """
        Returns True if a specific Root Name has been set (else, the Default Root Name has to be used)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which defines the way a Dispatch produces packets (which will become files) from its Input
        """
    def LimitedMax(self,nbent : int,max : int) -> bool: 
        """
        Returns True if a Dispatch generates a count of Packets always less than or equal to a maximum value : it can be computed from the total count of Entities to be dispatched : <nbent>. If answer is False, no limited maximum is expected for account If answer is True, expected maximum is given in argument <max> Default answer given here is False (can be redefined)
        """
    def Packeted(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of all Input Entities (see GetEntities) which are put in a Packet. That is, Entities listed in GetEntities but not in Remainder (see below). Input is given as a Graph.
        """
    def Packets(self,G : OCP.Interface.Interface_Graph,packs : OCP.IFGraph.IFGraph_SubPartsIterator) -> None: 
        """
        Returns the list of produced Packets into argument <pack>. Each Packet corresponds to a Part, the Entities listed are the Roots given by the Selection. Input is given as a Graph. Thus, to create a file from a packet, it suffices to take the entities listed in a Part of Packets (that is, a Packet) without worrying about Shared entities This method can raise an Exception if data are not coherent
        """
    def Remainder(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Remainder which is a set of Entities. Can be empty. Default evaluation is empty (has to be redefined if CanHaveRemainder is redefined to return True).
        """
    def RootName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Root Name for files produced by this dispatch It is empty if it has not been set or if it has been reset
        """
    def Selections(self) -> IFSelect_SelectionIterator: 
        """
        Returns the complete list of source Selections (starting from FinalSelection)
        """
    def SetFinalSelection(self,sel : IFSelect_Selection) -> None: ...
    def SetRootName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a Root Name as an HAsciiString To reset it, give a Null Handle (then, a ShareOut will have to define the Default Root Name)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class IFSelect_DispPerCount(IFSelect_Dispatch, OCP.Standard.Standard_Transient):
    """
    A DispPerCount gathers all the input Entities into one or several Packets, each containing a defined count of Entity This count is a Parameter of the DispPerCount, given as an IntParam, thus allowing external control of its ValueA DispPerCount gathers all the input Entities into one or several Packets, each containing a defined count of Entity This count is a Parameter of the DispPerCount, given as an IntParam, thus allowing external control of its ValueA DispPerCount gathers all the input Entities into one or several Packets, each containing a defined count of Entity This count is a Parameter of the DispPerCount, given as an IntParam, thus allowing external control of its Value
    """
    def CanHaveRemainder(self) -> bool: 
        """
        Returns True if a Dispatch can have a Remainder, i.e. if its criterium can let entities apart. It is a potential answer, remainder can be empty at run-time even if answer is True. (to attach a RemainderFromDispatch Selection is not allowed if answer is True). Default answer given here is False (can be redefined)
        """
    def Count(self) -> IFSelect_IntParam: 
        """
        Returns the Count Parameter used for splitting
        """
    def CountValue(self) -> int: 
        """
        Returns the effective value of the count parameter (if Count Parameter not Set or value not positive, returns 1)
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
    def FinalSelection(self) -> IFSelect_Selection: 
        """
        Returns the Final Selection of a Dispatch we 'd like : C++ : return const &
        """
    def GetEntities(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Gets Unique Root Entities from the Final Selection, given an input Graph This the starting step for an Evaluation (Packets - Remainder)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasRootName(self) -> bool: 
        """
        Returns True if a specific Root Name has been set (else, the Default Root Name has to be used)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns as Label, "One File per <count> Input Entities"
        """
    def LimitedMax(self,nbent : int,max : int) -> bool: 
        """
        Returns True, maximum count is given as <nbent>
        """
    def Packeted(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of all Input Entities (see GetEntities) which are put in a Packet. That is, Entities listed in GetEntities but not in Remainder (see below). Input is given as a Graph.
        """
    def Packets(self,G : OCP.Interface.Interface_Graph,packs : OCP.IFGraph.IFGraph_SubPartsIterator) -> None: 
        """
        Computes the list of produced Packets. It defines Packets in order to have at most <Count> Entities per Packet, Entities are given by RootResult from the Final Selection.
        """
    def Remainder(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Remainder which is a set of Entities. Can be empty. Default evaluation is empty (has to be redefined if CanHaveRemainder is redefined to return True).
        """
    def RootName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Root Name for files produced by this dispatch It is empty if it has not been set or if it has been reset
        """
    def Selections(self) -> IFSelect_SelectionIterator: 
        """
        Returns the complete list of source Selections (starting from FinalSelection)
        """
    def SetCount(self,count : IFSelect_IntParam) -> None: 
        """
        Sets a new Parameter for Count
        """
    def SetFinalSelection(self,sel : IFSelect_Selection) -> None: ...
    def SetRootName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a Root Name as an HAsciiString To reset it, give a Null Handle (then, a ShareOut will have to define the Default Root Name)
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
class IFSelect_DispPerFiles(IFSelect_Dispatch, OCP.Standard.Standard_Transient):
    """
    A DispPerFiles produces a determined count of Packets from the input Entities. It divides, as equally as possible, the input list into a count of files. This count is the parameter of the DispPerFiles. If the input list has less than this count, of course there will be one packet per input entity. This count is a Parameter of the DispPerFiles, given as an IntParam, thus allowing external control of its ValueA DispPerFiles produces a determined count of Packets from the input Entities. It divides, as equally as possible, the input list into a count of files. This count is the parameter of the DispPerFiles. If the input list has less than this count, of course there will be one packet per input entity. This count is a Parameter of the DispPerFiles, given as an IntParam, thus allowing external control of its ValueA DispPerFiles produces a determined count of Packets from the input Entities. It divides, as equally as possible, the input list into a count of files. This count is the parameter of the DispPerFiles. If the input list has less than this count, of course there will be one packet per input entity. This count is a Parameter of the DispPerFiles, given as an IntParam, thus allowing external control of its Value
    """
    def CanHaveRemainder(self) -> bool: 
        """
        Returns True if a Dispatch can have a Remainder, i.e. if its criterium can let entities apart. It is a potential answer, remainder can be empty at run-time even if answer is True. (to attach a RemainderFromDispatch Selection is not allowed if answer is True). Default answer given here is False (can be redefined)
        """
    def Count(self) -> IFSelect_IntParam: 
        """
        Returns the Count Parameter used for splitting
        """
    def CountValue(self) -> int: 
        """
        Returns the effective value of the count parameter (if Count Parameter not Set or value not positive, returns 1)
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
    def FinalSelection(self) -> IFSelect_Selection: 
        """
        Returns the Final Selection of a Dispatch we 'd like : C++ : return const &
        """
    def GetEntities(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Gets Unique Root Entities from the Final Selection, given an input Graph This the starting step for an Evaluation (Packets - Remainder)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasRootName(self) -> bool: 
        """
        Returns True if a specific Root Name has been set (else, the Default Root Name has to be used)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns as Label, "Maximum <count> Files"
        """
    def LimitedMax(self,nbent : int,max : int) -> bool: 
        """
        Returns True, maximum count is given as CountValue
        """
    def Packeted(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of all Input Entities (see GetEntities) which are put in a Packet. That is, Entities listed in GetEntities but not in Remainder (see below). Input is given as a Graph.
        """
    def Packets(self,G : OCP.Interface.Interface_Graph,packs : OCP.IFGraph.IFGraph_SubPartsIterator) -> None: 
        """
        Computes the list of produced Packets. It defines Packets in order to have <Count> Packets, except if the input count of Entities is lower. Entities are given by RootResult from the Final Selection.
        """
    def Remainder(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Remainder which is a set of Entities. Can be empty. Default evaluation is empty (has to be redefined if CanHaveRemainder is redefined to return True).
        """
    def RootName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Root Name for files produced by this dispatch It is empty if it has not been set or if it has been reset
        """
    def Selections(self) -> IFSelect_SelectionIterator: 
        """
        Returns the complete list of source Selections (starting from FinalSelection)
        """
    def SetCount(self,count : IFSelect_IntParam) -> None: 
        """
        Sets a new Parameter for Count
        """
    def SetFinalSelection(self,sel : IFSelect_Selection) -> None: ...
    def SetRootName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a Root Name as an HAsciiString To reset it, give a Null Handle (then, a ShareOut will have to define the Default Root Name)
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
class IFSelect_DispPerOne(IFSelect_Dispatch, OCP.Standard.Standard_Transient):
    """
    A DispPerOne gathers all the input Entities into as many Packets as there Root Entities from the Final Selection, that is, one Packet per EntityA DispPerOne gathers all the input Entities into as many Packets as there Root Entities from the Final Selection, that is, one Packet per EntityA DispPerOne gathers all the input Entities into as many Packets as there Root Entities from the Final Selection, that is, one Packet per Entity
    """
    def CanHaveRemainder(self) -> bool: 
        """
        Returns True if a Dispatch can have a Remainder, i.e. if its criterium can let entities apart. It is a potential answer, remainder can be empty at run-time even if answer is True. (to attach a RemainderFromDispatch Selection is not allowed if answer is True). Default answer given here is False (can be redefined)
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
    def FinalSelection(self) -> IFSelect_Selection: 
        """
        Returns the Final Selection of a Dispatch we 'd like : C++ : return const &
        """
    def GetEntities(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Gets Unique Root Entities from the Final Selection, given an input Graph This the starting step for an Evaluation (Packets - Remainder)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasRootName(self) -> bool: 
        """
        Returns True if a specific Root Name has been set (else, the Default Root Name has to be used)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns as Label, "One File per Input Entity"
        """
    def LimitedMax(self,nbent : int,max : int) -> bool: 
        """
        Returns True, maximum limit is given as <nbent>
        """
    def Packeted(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of all Input Entities (see GetEntities) which are put in a Packet. That is, Entities listed in GetEntities but not in Remainder (see below). Input is given as a Graph.
        """
    def Packets(self,G : OCP.Interface.Interface_Graph,packs : OCP.IFGraph.IFGraph_SubPartsIterator) -> None: 
        """
        Returns the list of produced Packets. It defines one Packet per Entity given by RootResult from the Final Selection.
        """
    def Remainder(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Remainder which is a set of Entities. Can be empty. Default evaluation is empty (has to be redefined if CanHaveRemainder is redefined to return True).
        """
    def RootName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Root Name for files produced by this dispatch It is empty if it has not been set or if it has been reset
        """
    def Selections(self) -> IFSelect_SelectionIterator: 
        """
        Returns the complete list of source Selections (starting from FinalSelection)
        """
    def SetFinalSelection(self,sel : IFSelect_Selection) -> None: ...
    def SetRootName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a Root Name as an HAsciiString To reset it, give a Null Handle (then, a ShareOut will have to define the Default Root Name)
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
class IFSelect_DispPerSignature(IFSelect_Dispatch, OCP.Standard.Standard_Transient):
    """
    A DispPerSignature sorts input Entities according to a Signature : it works with a SignCounter to do this.A DispPerSignature sorts input Entities according to a Signature : it works with a SignCounter to do this.A DispPerSignature sorts input Entities according to a Signature : it works with a SignCounter to do this.
    """
    def CanHaveRemainder(self) -> bool: 
        """
        Returns True if a Dispatch can have a Remainder, i.e. if its criterium can let entities apart. It is a potential answer, remainder can be empty at run-time even if answer is True. (to attach a RemainderFromDispatch Selection is not allowed if answer is True). Default answer given here is False (can be redefined)
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
    def FinalSelection(self) -> IFSelect_Selection: 
        """
        Returns the Final Selection of a Dispatch we 'd like : C++ : return const &
        """
    def GetEntities(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Gets Unique Root Entities from the Final Selection, given an input Graph This the starting step for an Evaluation (Packets - Remainder)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasRootName(self) -> bool: 
        """
        Returns True if a specific Root Name has been set (else, the Default Root Name has to be used)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns as Label, "One File per Signature <name>"
        """
    def LimitedMax(self,nbent : int,max : int) -> bool: 
        """
        Returns True, maximum count is given as <nbent>
        """
    def Packeted(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of all Input Entities (see GetEntities) which are put in a Packet. That is, Entities listed in GetEntities but not in Remainder (see below). Input is given as a Graph.
        """
    def Packets(self,G : OCP.Interface.Interface_Graph,packs : OCP.IFGraph.IFGraph_SubPartsIterator) -> None: 
        """
        Computes the list of produced Packets. It defines Packets from the SignCounter, which sirts the input Entities per Signature (specific of the SignCounter).
        """
    def Remainder(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Remainder which is a set of Entities. Can be empty. Default evaluation is empty (has to be redefined if CanHaveRemainder is redefined to return True).
        """
    def RootName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Root Name for files produced by this dispatch It is empty if it has not been set or if it has been reset
        """
    def Selections(self) -> IFSelect_SelectionIterator: 
        """
        Returns the complete list of source Selections (starting from FinalSelection)
        """
    def SetFinalSelection(self,sel : IFSelect_Selection) -> None: ...
    def SetRootName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a Root Name as an HAsciiString To reset it, give a Null Handle (then, a ShareOut will have to define the Default Root Name)
        """
    def SetSignCounter(self,sign : IFSelect_SignCounter) -> None: 
        """
        Sets a SignCounter for sort Remark : it is set to record lists of entities, not only counts
        """
    def SignCounter(self) -> IFSelect_SignCounter: 
        """
        Returns the SignCounter used for splitting
        """
    def SignName(self) -> str: 
        """
        Returns the name of the SignCounter, which caracterises the sorting criterium for this Dispatch
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
class IFSelect_DispGlobal(IFSelect_Dispatch, OCP.Standard.Standard_Transient):
    """
    A DispGlobal gathers all the input Entities into only one global PacketA DispGlobal gathers all the input Entities into only one global PacketA DispGlobal gathers all the input Entities into only one global Packet
    """
    def CanHaveRemainder(self) -> bool: 
        """
        Returns True if a Dispatch can have a Remainder, i.e. if its criterium can let entities apart. It is a potential answer, remainder can be empty at run-time even if answer is True. (to attach a RemainderFromDispatch Selection is not allowed if answer is True). Default answer given here is False (can be redefined)
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
    def FinalSelection(self) -> IFSelect_Selection: 
        """
        Returns the Final Selection of a Dispatch we 'd like : C++ : return const &
        """
    def GetEntities(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Gets Unique Root Entities from the Final Selection, given an input Graph This the starting step for an Evaluation (Packets - Remainder)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasRootName(self) -> bool: 
        """
        Returns True if a specific Root Name has been set (else, the Default Root Name has to be used)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns as Label, "One File for all Input"
        """
    def LimitedMax(self,nbent : int,max : int) -> bool: 
        """
        Returns True : maximum equates 1
        """
    def Packeted(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of all Input Entities (see GetEntities) which are put in a Packet. That is, Entities listed in GetEntities but not in Remainder (see below). Input is given as a Graph.
        """
    def Packets(self,G : OCP.Interface.Interface_Graph,packs : OCP.IFGraph.IFGraph_SubPartsIterator) -> None: 
        """
        Computes the list of produced Packets. It is made of only ONE Packet, which gets the RootResult from the Final Selection. Remark : the inherited exception raising is never activated.
        """
    def Remainder(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Remainder which is a set of Entities. Can be empty. Default evaluation is empty (has to be redefined if CanHaveRemainder is redefined to return True).
        """
    def RootName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Root Name for files produced by this dispatch It is empty if it has not been set or if it has been reset
        """
    def Selections(self) -> IFSelect_SelectionIterator: 
        """
        Returns the complete list of source Selections (starting from FinalSelection)
        """
    def SetFinalSelection(self,sel : IFSelect_Selection) -> None: ...
    def SetRootName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a Root Name as an HAsciiString To reset it, give a Null Handle (then, a ShareOut will have to define the Default Root Name)
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
class IFSelect_EditForm(OCP.Standard.Standard_Transient):
    """
    An EditForm is the way to apply an Editor on an Entity or on the Model It gives read-only or read-write access, with or without undoAn EditForm is the way to apply an Editor on an Entity or on the Model It gives read-only or read-write access, with or without undoAn EditForm is the way to apply an Editor on an Entity or on the Model It gives read-only or read-write access, with or without undo
    """
    def Apply(self) -> bool: 
        """
        Applies modifications to own data Calls ApplyData then Clears Status according EditKeepStatus
        """
    def ApplyData(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Applies modifications to data Default uses Editor. Can be redefined
        """
    def ClearData(self) -> None: 
        """
        None
        """
    def ClearEdit(self,num : int=0) -> None: 
        """
        Clears modification status : by default all, or one by its numbers (in the Editor)
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
    def EditedList(self,num : int) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the Edited Value as a list If IsModified is False, returns OriginalValue Null with IsModified True : means that this value is not defined or has been removed For a single parameter, gives a Null Handle
        """
    def EditedValue(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Edited (i.e. Modified) Value (string for single) <num> reports to the EditForm If IsModified is False, returns OriginalValue Null with IsModified True : means that this value is not defined or has been removed It is for a single parameter. For a list, gives a Null Handle
        """
    def Editor(self) -> IFSelect_Editor: 
        """
        None
        """
    def Entity(self) -> OCP.Standard.Standard_Transient: 
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
    def IsComplete(self) -> bool: 
        """
        Tells if an EditForm is complete or is an extract from Editor
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsLoaded(self) -> bool: 
        """
        Tells if the EditForm is loaded now
        """
    def IsModified(self,num : int) -> bool: 
        """
        Tells if a Value (of the EditForm) is modified (directly or through touching by Update)
        """
    def IsTouched(self,num : int) -> bool: 
        """
        Tells if a Value (of the EditForm) has been touched, i.e. not modified directly but by the modification of another one (by method Update from the Editor)
        """
    def Label(self) -> str: 
        """
        None
        """
    def ListEditor(self,num : int) -> IFSelect_ListEditor: 
        """
        Returns a ListEditor to edit the parameter <num> of the EditForm, if it is a List The Editor created it (by ListEditor) then loads it (by ListValue) For a single parameter, returns a Null Handle ...
        """
    @overload
    def LoadData(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Loads modifications to data Default uses Editor. Can be redefined Remark that <ent> and/or <model> may be null, according to the kind of Editor. Shortcuts are available for these cases, but they finally call LoadData (hence, just ignore non-used args)

        Shortcut when both <ent> and <model> are not used (when the Editor works on fully static or global data)
        """
    @overload
    def LoadData(self) -> bool: ...
    def LoadDefault(self) -> None: 
        """
        For a read-write undoable EditForm, loads original values from defaults stored in the Editor
        """
    def LoadEntity(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Shortcut for LoadData when <model> is not used
        """
    def LoadList(self,num : int,list : OCP.TColStd.TColStd_HSequenceOfHAsciiString) -> None: 
        """
        Loads an original value as a list. Called by the Editor only
        """
    def LoadModel(self,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Shortcut for LoadData when only the model is concerned
        """
    def LoadValue(self,num : int,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Loads an original value (single). Called by the Editor only
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        None
        """
    def Modify(self,num : int,newval : OCP.TCollection.TCollection_HAsciiString,enforce : bool=False) -> bool: 
        """
        Gives a new value for the item <num> of the EditForm, if it is a single parameter (for a list, just returns False) Null means to Remove it <enforce> True to overpass Protected or Computed Access Mode Calls the method Update from the Editor, which can touch other parameters (see NbTouched) Returns True if well recorded, False if this value is not allowed Warning : Does not apply immediately : will be applied by the method Apply
        """
    def ModifyList(self,num : int,edited : IFSelect_ListEditor,enforce : bool=False) -> bool: 
        """
        Changes the value of an item of the EditForm, if it is a List (else, just returns False) The ListEditor contains the edited values of the list If no edition was recorded, just returns False Calls the method Update from the Editor, which can touch other parameters (see NbTouched) Returns True if well recorded, False if this value is not allowed Warning : Does not apply immediately : will be applied by the method Apply
        """
    def ModifyListValue(self,num : int,list : OCP.TColStd.TColStd_HSequenceOfHAsciiString,enforce : bool=False) -> bool: 
        """
        As ModifyList but the new value is given as such Creates a ListEditor, Loads it, then calls ModifyList
        """
    def NameNumber(self,name : str) -> int: 
        """
        Returns the Value Number in the Editor for a given Name i.e. the true ValueNumber which can be used in various methods of EditForm If it is not complete, for a recorded (in the Editor) but non-loaded name, returns negative value (- number)
        """
    def NameRank(self,name : str) -> int: 
        """
        Returns the Rank of Value in the EditForm for a given Name i.e. if it is not complete, for a recorded (in the Editor) but non-loaded name, returns 0
        """
    def NbValues(self,editable : bool) -> int: 
        """
        Returns the count of values <editable> True : count of editable values, i.e. For a complete EditForm, it is given by the Editor Else, it is the length of the extraction map <editable> False : all the values from the Editor
        """
    def NumberFromRank(self,rank : int) -> int: 
        """
        Returns the Value Number in the Editor from a given Rank in the EditForm For a complete EditForm, both are equal Else, it is given by the extraction map Returns 0 if <rank> exceeds the count of editable values,
        """
    def OriginalList(self,num : int) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns an original value, as a list <num> is for the EditForm, not the Editor For a single parameter, gives a Null Handle
        """
    def OriginalValue(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        From an edited value, returns its ... value (original one) Null means that this value is not defined <num> is for the EditForm, not the Editor It is for a single parameter. For a list, gives a Null Handle
        """
    def PrintDefs(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints Definitions, relative to the Editor
        """
    def PrintValues(self,S : OCP.Message.Message_Messenger,what : int,names : bool,alsolist : bool=False) -> None: 
        """
        Prints Values, according to what and alsolist <names> True : prints Long Names; False : prints Short Names <what> < 0 : prints Original Values (+ flag Modified) <what> > 0 : prints Final Values (+flag Modified) <what> = 0 : prints Modified Values (Original + Edited) <alsolist> False (D) : lists are printed only as their count <alsolist> True : lists are printed for all their items
        """
    def RankFromNumber(self,number : int) -> int: 
        """
        Returns the Rank in the EditForm from a given Number of Value for the Editor For a complete EditForm, both are equal Else, it is given by the extraction map Returns 0 if <number> is not forecast to be edited, or is out of range
        """
    def Recognize(self) -> bool: 
        """
        Tells if this EditForm can work with its Editor and its actual Data (Entity and Model) Default uses Editor. Can be redefined
        """
    def SetData(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        None
        """
    def SetEntity(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        None
        """
    def SetModel(self,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Touch(self,num : int,newval : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        Gives a new value computed by the Editor, if another parameter commands the value of <num> It is generally the case for a Computed Parameter for instance Increments the counter of touched parameters Warning : it gives no protection for ReadOnly etc... while it is the internal way of touching parameters Does not work (returns False) if <num> is for a list
        """
    def TouchList(self,num : int,newlist : OCP.TColStd.TColStd_HSequenceOfHAsciiString) -> bool: 
        """
        Acts as Touch but for a list Does not work (returns False) if <num> is for a single param
        """
    def Undo(self) -> bool: 
        """
        For an undoable EditForm, Applies ... origibal values ! and clears modified ones Can be run only once
        """
    @overload
    def __init__(self,editor : IFSelect_Editor,readonly : bool,undoable : bool,label : str='') -> None: ...
    @overload
    def __init__(self,editor : IFSelect_Editor,nums : OCP.TColStd.TColStd_SequenceOfInteger,readonly : bool,undoable : bool,label : str='') -> None: ...
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
    def EditKeepStatus(self) -> bool:
        """
        :type: bool
        """
    @EditKeepStatus.setter
    def EditKeepStatus(self, arg1: bool) -> None:
        pass
    pass
class IFSelect_EditValue():
    """
    Controls access on Values by an Editor EditOptional : normal access, in addition may be removed Editable : normal access, must be present EditProtected : access must be validated EditComputed : why write it ? it will be recomputed EditRead : no way to write it, only for read EditDynamic : not a field, only to be displayed

    Members:

      IFSelect_Optional

      IFSelect_Editable

      IFSelect_EditProtected

      IFSelect_EditComputed

      IFSelect_EditRead

      IFSelect_EditDynamic
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IFSelect_EditComputed: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_EditComputed
    IFSelect_EditDynamic: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_EditDynamic
    IFSelect_EditProtected: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_EditProtected
    IFSelect_EditRead: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_EditRead
    IFSelect_Editable: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_Editable
    IFSelect_Optional: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_Optional
    __entries: dict # value = {'IFSelect_Optional': (IFSelect_EditValue.IFSelect_Optional, None), 'IFSelect_Editable': (IFSelect_EditValue.IFSelect_Editable, None), 'IFSelect_EditProtected': (IFSelect_EditValue.IFSelect_EditProtected, None), 'IFSelect_EditComputed': (IFSelect_EditValue.IFSelect_EditComputed, None), 'IFSelect_EditRead': (IFSelect_EditValue.IFSelect_EditRead, None), 'IFSelect_EditDynamic': (IFSelect_EditValue.IFSelect_EditDynamic, None)}
    __members__: dict # value = {'IFSelect_Optional': IFSelect_EditValue.IFSelect_Optional, 'IFSelect_Editable': IFSelect_EditValue.IFSelect_Editable, 'IFSelect_EditProtected': IFSelect_EditValue.IFSelect_EditProtected, 'IFSelect_EditComputed': IFSelect_EditValue.IFSelect_EditComputed, 'IFSelect_EditRead': IFSelect_EditValue.IFSelect_EditRead, 'IFSelect_EditDynamic': IFSelect_EditValue.IFSelect_EditDynamic}
    pass
class IFSelect_Editor(OCP.Standard.Standard_Transient):
    """
    An Editor defines a set of values and a way to edit them, on an entity or on the model (e.g. on its header)An Editor defines a set of values and a way to edit them, on an entity or on the model (e.g. on its header)An Editor defines a set of values and a way to edit them, on an entity or on the model (e.g. on its header)
    """
    def Apply(self,form : IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Applies modified values of the EditForm with some data Remark: <ent> may be Null, this means all <model> is concerned Also <model> may be Null, if no context applies for <ent> And both <ent> and <model> may be Null, for a full static editor
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
    def EditMode(self,num : int) -> IFSelect_EditValue: 
        """
        Returns the edit mode of a Value
        """
    def Form(self,readonly : bool,undoable : bool=True) -> IFSelect_EditForm: 
        """
        Builds and Returns an EditForm, empty (no data yet) Can be redefined to return a specific type of EditForm
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsList(self,num : int) -> bool: 
        """
        Tells if a parameter is a list
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the specific label
        """
    def ListEditor(self,num : int) -> IFSelect_ListEditor: 
        """
        Returns a ListEditor for a parameter which is a List Default returns a basic ListEditor for a List, a Null Handle if <num> is not for a List. Can be redefined
        """
    def ListValue(self,form : IFSelect_EditForm,num : int) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the value of an EditForm as a List, for a given item If not a list, a Null Handle should be returned Default returns a Null Handle, because many Editors have no list to edit. To be redefined as required
        """
    def Load(self,form : IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Loads original values from some data, to an EditForm Remark: <ent> may be Null, this means all <model> is concerned Also <model> may be Null, if no context applies for <ent> And both <ent> and <model> may be Null, for a full static editor
        """
    def MaxList(self,num : int) -> int: 
        """
        Returns max length allowed for a list = 0 means : list with no limit < 0 means : not a list
        """
    def MaxNameLength(self,what : int) -> int: 
        """
        Returns the MaxLength of, according to what : <what> = -1 : length of short names <what> = 0 : length of complete names <what> = 1 : length of values labels
        """
    def Name(self,num : int,isshort : bool=False) -> str: 
        """
        Returns the name of a Value (complete or short) from its ident Short Name can be empty
        """
    def NameNumber(self,name : str) -> int: 
        """
        Returns the number (ident) of a Value, from its name, short or complete. If not found, returns 0
        """
    def NbValues(self) -> int: 
        """
        Returns the count of Typed Values
        """
    def PrintDefs(self,S : OCP.Message.Message_Messenger,labels : bool=False) -> None: 
        """
        None
        """
    def PrintNames(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        None
        """
    def Recognize(self,form : IFSelect_EditForm) -> bool: 
        """
        Tells if this Editor can work on this EditForm and its content (model, entity ?)
        """
    def SetList(self,num : int,max : int=0) -> None: 
        """
        Sets a parameter to be a List max < 0 : not for a list (set when starting) max = 0 : list with no length limit (default for SetList) max > 0 : list limited to <max> items
        """
    def SetValue(self,num : int,typval : OCP.Interface.Interface_TypedValue,shortname : str='',accessmode : IFSelect_EditValue=IFSelect_EditValue.IFSelect_Editable) -> None: 
        """
        Sets a Typed Value for a given ident and short name, with an Edit Mode
        """
    def StringValue(self,form : IFSelect_EditForm,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the value of an EditForm, for a given item (if not a list. for a list, a Null String may be returned)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypedValue(self,num : int) -> OCP.Interface.Interface_TypedValue: 
        """
        Returns a Typed Value from its ident
        """
    def Update(self,form : IFSelect_EditForm,num : int,newval : OCP.TCollection.TCollection_HAsciiString,enforce : bool) -> bool: 
        """
        Updates the EditForm when a parameter is modified I.E. default does nothing, can be redefined, as follows : Returns True when done (even if does nothing), False in case of refuse (for instance, if the new value is not suitable) <num> is the rank of the parameter for the EDITOR itself <enforce> True means that protected parameters can be touched
        """
    def UpdateList(self,form : IFSelect_EditForm,num : int,newlist : OCP.TColStd.TColStd_HSequenceOfHAsciiString,enforce : bool) -> bool: 
        """
        Acts as Update, but when the value is a list
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
class IFSelect_Functions():
    """
    Functions gives access to all the actions which can be commanded with the resources provided by IFSelect : especially WorkSession and various types of Selections and Dispatches
    """
    @staticmethod
    def GiveDispatch_s(WS : IFSelect_WorkSession,name : str,mode : bool=True) -> IFSelect_Dispatch: 
        """
        Evaluates and returns a Dispatch, from data of a WorkSession if <mode> is False, searches for exact name of Dispatch in WS Else (D), allows a parameter between brackets : ex.: dispatch_name(parameter) The parameter can be: an integer for DispPerCount or DispPerFiles or the name of a Signature for DispPerSignature Returns Null Handle if not found not well evaluated
        """
    @staticmethod
    def GiveEntityNumber_s(WS : IFSelect_WorkSession,name : str='') -> int: 
        """
        Same as GetEntity, but returns the number in the model of the entity. Returns 0 for null handle
        """
    @staticmethod
    def GiveEntity_s(WS : IFSelect_WorkSession,name : str='') -> OCP.Standard.Standard_Transient: 
        """
        Takes the name of an entity, either as argument, or (if <name> is empty) on keybord, and returns the entity name can be a label or a number (in alphanumeric), it is searched by NumberFromLabel from WorkSession. If <name> doesn't match en entity, a Null Handle is returned
        """
    @staticmethod
    def GiveList_s(WS : IFSelect_WorkSession,first : str='',second : str='') -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Computes a List of entities from a WorkSession and two idents, first and second, as follows : if <first> is a Number or Label of an entity : this entity if <first> is the name of a Selection in <WS>, and <second> not defined, the standard result of this Selection if <first> is for a Selection and <second> is defined, the standard result of this selection from the list computed with <second> (an entity or a selection) If <second> is erroneous, it is ignored
        """
    @staticmethod
    def Init_s() -> None: 
        """
        Defines and loads all basic functions (as ActFunc)
        """
    def __init__(self) -> None: ...
    pass
class IFSelect_GeneralModifier(OCP.Standard.Standard_Transient):
    """
    This class gives a frame for Actions which modify the effect of a Dispatch, i.e. : By Selections and Dispatches, an original Model can be splitted into one or more "target" Models : these Models contain Entities copied from the original one (that is, a part of it). Basically, these dispatched Entities are copied as identical to their original counterparts. Also the copied Models reproduce the Header of the original one.This class gives a frame for Actions which modify the effect of a Dispatch, i.e. : By Selections and Dispatches, an original Model can be splitted into one or more "target" Models : these Models contain Entities copied from the original one (that is, a part of it). Basically, these dispatched Entities are copied as identical to their original counterparts. Also the copied Models reproduce the Header of the original one.This class gives a frame for Actions which modify the effect of a Dispatch, i.e. : By Selections and Dispatches, an original Model can be splitted into one or more "target" Models : these Models contain Entities copied from the original one (that is, a part of it). Basically, these dispatched Entities are copied as identical to their original counterparts. Also the copied Models reproduce the Header of the original one.
    """
    def Applies(self,disp : IFSelect_Dispatch) -> bool: 
        """
        Returns True if a Model obtained from the Dispatch <disp> is to be treated (apart from the Selection criterium) If Dispatch(me) is Null, returns True. Else, checks <disp>
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self) -> IFSelect_Dispatch: 
        """
        Returns the Dispatch to be matched, Null if not set
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSelection(self) -> bool: 
        """
        Returns True if a Selection is set as an additionnal criterium
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a short text which defines the operation performed
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class IFSelect_SignCounter(IFSelect_SignatureList, OCP.Standard.Standard_Transient):
    """
    SignCounter gives the frame to count signatures associated with entities, deducted from them. Ex.: their Dynamic Type.SignCounter gives the frame to count signatures associated with entities, deducted from them. Ex.: their Dynamic Type.SignCounter gives the frame to count signatures associated with entities, deducted from them. Ex.: their Dynamic Type.
    """
    def Add(self,ent : OCP.Standard.Standard_Transient,sign : str) -> None: 
        """
        Adds an entity with its signature, i.e. : - counts an item more for <sign> - if record-list status is set, records the entity Accepts a null entity (the signature is then for the global model). But if the string is empty, counts a Null item.
        """
    def AddEntity(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Adds an entity by considering its signature, which is given by call to method AddSign Returns True if added, False if already in the map (and map control status set)
        """
    def AddFromSelection(self,sel : IFSelect_Selection,G : OCP.Interface.Interface_Graph) -> None: 
        """
        Adds the result determined by a Selection from a Graph Remark : does not impact at all data from SetSelection & Co
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Adds a list of entities by adding each of the items
        """
    def AddModel(self,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Adds all the entities contained in a Model
        """
    def AddSign(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Adds an entity (already filtered by Map) with its signature. This signature can be computed with the containing model. Its value is provided by the object Signature given at start, if no Signature is defined, it does nothing.
        """
    def AddWithGraph(self,list : OCP.TColStd.TColStd_HSequenceOfTransient,graph : OCP.Interface.Interface_Graph) -> None: 
        """
        Adds a list of entities in the context given by the graph Default just call basic AddList Can be redefined to get a signature computed with the graph
        """
    def Clear(self) -> None: 
        """
        None
        """
    def ComputeSelected(self,G : OCP.Interface.Interface_Graph,forced : bool=False) -> bool: 
        """
        Computes from the selection result, if selection is active (mode 2). If selection is not defined (mode 0) or is inhibited (mode 1) does nothing. Returns True if computation is done (or optimised), False else This method is called by ComputeCounter from WorkSession
        """
    def ComputedSign(self,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph) -> str: 
        """
        Applies AddWithGraph on one entity, and returns the Signature Value which has been recorded To do this, Add is called with SignOnly Mode True during the call, the returned value is LastValue
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
    def Entities(self,sign : str) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities attached to a signature It is empty if <sign> has not been recorded It is a Null Handle if the list of entities is not known
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasEntities(self) -> bool: 
        """
        Returns True if the list of Entities is aknowledged, else the method Entities will always return a Null Handle
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,name : str,count : Any,list : Any,nbnuls : int) -> None: 
        """
        Aknowledges the list in once. Name identifies the Signature
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def LastValue(self) -> str: 
        """
        Returns the last value recorded by Add (only if SignMode set) Cleared by Clear or Init
        """
    def List(self,root : str='') -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of signatures, as a sequence of strings (but without their respective counts). It is ordered. By default, for all the signatures. If <root> is given non empty, for the signatures which begin by <root>
        """
    def Name(self) -> str: 
        """
        Returns the recorded Name. Remark : default is "..." (no SetName called)
        """
    def NbNulls(self) -> int: 
        """
        Returns the count of null entities
        """
    def NbTimes(self,sign : str) -> int: 
        """
        Returns the number of times a signature was counted, 0 if it has not been recorded at all
        """
    def PrintCount(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints the counts of items (not the list)
        """
    def PrintList(self,S : OCP.Message.Message_Messenger,model : OCP.Interface.Interface_InterfaceModel,mod : IFSelect_PrintCount=IFSelect_PrintCount.IFSelect_ListByItem) -> None: 
        """
        Prints the lists of items, if they are present (else, prints a message "no list available") Uses <model> to determine for each entity to be listed, its number, and its specific identifier (by PrintLabel) <mod> gives a mode for printing : - CountByItem : just count (as PrintCount) - ShortByItem : minimum i.e. count plus 5 first entity numbers - ShortByItem(D) complete list of entity numbers (0: "Global") - EntitiesByItem : list of (entity number/PrintLabel from the model) other modes are ignored
        """
    def PrintSum(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints a summary Item which has the greatest count of entities For items which are numeric values : their count, maximum, minimum values, cumul, average
        """
    def SelMode(self) -> int: 
        """
        Returns the mode of working with the selection
        """
    def Selection(self) -> IFSelect_Selection: 
        """
        Returns the selection, or a null Handle
        """
    def SetList(self,withlist : bool) -> None: 
        """
        Changes the record-list status. The list is not cleared but its use changes
        """
    def SetMap(self,withmap : bool) -> None: 
        """
        Changes the control status. The map is not cleared, simply its use changes
        """
    def SetName(self,name : str) -> None: 
        """
        Defines a name for a SignatureList (used to print it)
        """
    def SetSelMode(self,selmode : int) -> None: 
        """
        Changes the mode of working with the selection : -1 just clears optimisation data and nothing else 0 clears it 1 inhibits it for computing (but no clearing) 2 sets it active for computing Default at creation is 0, after SetSelection (not null) is 2
        """
    def SetSelection(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection as input : this causes content to be cleared then the Selection to be ready to compute (but not immediatly)
        """
    def Sign(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Determines and returns the value of the signature for an entity as an HAsciiString. This method works exactly as AddSign, which is optimized
        """
    def Signature(self) -> IFSelect_Signature: 
        """
        Returns the Signature used to count entities. It can be null.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,withmap : bool=True,withlist : bool=False) -> None: ...
    @overload
    def __init__(self,matcher : IFSelect_Signature,withmap : bool=True,withlist : bool=False) -> None: ...
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
    def ModeSignOnly(self) -> bool:
        """
        :type: bool
        """
    @ModeSignOnly.setter
    def ModeSignOnly(self, arg1: bool) -> None:
        pass
    pass
class IFSelect_TSeqOfSelection(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : IFSelect_TSeqOfSelection) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : IFSelect_Selection) -> None: ...
    def Assign(self,theOther : IFSelect_TSeqOfSelection) -> IFSelect_TSeqOfSelection: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IFSelect_Selection: 
        """
        First item access
        """
    def ChangeLast(self) -> IFSelect_Selection: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IFSelect_Selection: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> IFSelect_Selection: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IFSelect_TSeqOfSelection) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IFSelect_Selection) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IFSelect_Selection) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IFSelect_TSeqOfSelection) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IFSelect_Selection: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theSeq : IFSelect_TSeqOfSelection) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IFSelect_Selection) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : IFSelect_Selection) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IFSelect_TSeqOfSelection) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IFSelect_Selection: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IFSelect_TSeqOfSelection) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IFSelect_IntParam(OCP.Standard.Standard_Transient):
    """
    This class simply allows to access an Integer value through a Handle, as a String can be (by using HString). Hence, this value can be accessed : read and modified, without passing through the specific object which detains it. Thus, parameters of a Selection or a Dispatch (according its type) can be controlled directly from the ShareOut which contains themThis class simply allows to access an Integer value through a Handle, as a String can be (by using HString). Hence, this value can be accessed : read and modified, without passing through the specific object which detains it. Thus, parameters of a Selection or a Dispatch (according its type) can be controlled directly from the ShareOut which contains themThis class simply allows to access an Integer value through a Handle, as a String can be (by using HString). Hence, this value can be accessed : read and modified, without passing through the specific object which detains it. Thus, parameters of a Selection or a Dispatch (according its type) can be controlled directly from the ShareOut which contains them
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetStaticName(self,statname : str) -> None: 
        """
        Commands this IntParam to be bound to a Static Hence, Value will return the value if this Static if it is set Else, Value works on the locally stored value SetValue also will set the value of the Static This works only for a present static of type integer or enum Else, it is ignored
        """
    def SetValue(self,val : int) -> None: 
        """
        Sets a new Integer Value for the IntParam. If a StaticName is defined and the Static is set, also sets the value of the static
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> int: 
        """
        Reads Integer Value of the IntParam. If a StaticName is defined and the Static is set, looks in priority the value of the static
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
class IFSelect_ListEditor(OCP.Standard.Standard_Transient):
    """
    A ListEditor is an auxiliary operator for Editor/EditForm I.E. it works on parameter values expressed as stringsA ListEditor is an auxiliary operator for Editor/EditForm I.E. it works on parameter values expressed as stringsA ListEditor is an auxiliary operator for Editor/EditForm I.E. it works on parameter values expressed as strings
    """
    def AddValue(self,val : OCP.TCollection.TCollection_HAsciiString,atnum : int=0) -> bool: 
        """
        Adds a new item. By default appends (at the end of the list) Can insert before a given rank <num>, if positive Returns True when done. False if MaxLength may be overpassed or if <val> does not satisfy the definition
        """
    def ClearEdit(self) -> None: 
        """
        Clears all editions already recorded
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
    def EditedValues(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the result of the edition
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAdded(self,num : int) -> bool: 
        """
        Tells if a value (in edited list) has been added (new one)
        """
    def IsChanged(self,num : int) -> bool: 
        """
        Tells if a value (in edited list) has been changed, i.e. either modified-value, or added
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsModified(self,num : int) -> bool: 
        """
        Tells if a value (in edited list) has been modified-value (not added)
        """
    def IsTouched(self) -> bool: 
        """
        Tells if at least one edition (SetValue-AddValue-Remove) has been recorded
        """
    def LoadEdited(self,list : OCP.TColStd.TColStd_HSequenceOfHAsciiString) -> bool: 
        """
        Loads a new list to replace the older one, in once ! By default (can be redefined) checks the length of the list and the value of each item according to the def Items are all recorded as Modified
        """
    def LoadModel(self,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Loads a Model. It is used to check items of type Entity(Ident)
        """
    def LoadValues(self,vals : OCP.TColStd.TColStd_HSequenceOfHAsciiString) -> None: 
        """
        Loads the original values for the list Remark : If its length is mor then MaxLength, editions remain allowed, except Add
        """
    def NbValues(self,edited : bool=True) -> int: 
        """
        Returns count of values, edited (D) or original
        """
    def OriginalValues(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the value from which the edition started
        """
    def Remove(self,num : int=0,howmany : int=1) -> bool: 
        """
        Removes items from the list By default removes one item. Else, count given by <howmany> Remove from rank <num> included. By default, from the end Returns True when done, False (and does not work) if case of out of range of if <howmany> is greater than current length
        """
    def SetTouched(self) -> None: 
        """
        Declares this ListEditor to have been touched (whatever action)
        """
    def SetValue(self,num : int,val : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        Sets a new value for the item <num> (in edited list) <val> may be a Null Handle, then the value will be cleared but not removed Returns True when done. False if <num> is out of range or if <val> does not satisfy the definition
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,num : int,edited : bool=True) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a value given its rank. Edited (D) or Original A Null String means the value is cleared but not removed
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,def_ : OCP.Interface.Interface_TypedValue,max : int=0) -> None: ...
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
class IFSelect_ModelCopier(OCP.Standard.Standard_Transient):
    """
    This class performs the Copy operations involved by the description of a ShareOut (evaluated by a ShareOutResult) plus, if there are, the Modifications on the results, with the help of Modifiers. Each Modifier can work on one or more resulting packets, accoding its criteria : it operates on a Model once copied and filled with the content of the packet.This class performs the Copy operations involved by the description of a ShareOut (evaluated by a ShareOutResult) plus, if there are, the Modifications on the results, with the help of Modifiers. Each Modifier can work on one or more resulting packets, accoding its criteria : it operates on a Model once copied and filled with the content of the packet.This class performs the Copy operations involved by the description of a ShareOut (evaluated by a ShareOutResult) plus, if there are, the Modifications on the results, with the help of Modifiers. Each Modifier can work on one or more resulting packets, accoding its criteria : it operates on a Model once copied and filled with the content of the packet.
    """
    def AddFile(self,filename : OCP.TCollection.TCollection_AsciiString,content : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Records a new File to be sent, as a couple (Name as AsciiString, Content as InterfaceModel) Returns True if Done, False if <filename> is already attached to another File
        """
    def AddSentFile(self,filename : str) -> None: 
        """
        Adds the name of a just sent file, if BeginSentFiles has commanded recording; else does nothing It is called by methods SendCopied Sending
        """
    def AppliedModifiers(self,num : int) -> IFSelect_AppliedModifiers: 
        """
        Returns the list of File Modifiers to be applied on a file when it will be sent, as computed by CopiedModel : If it is a null handle, no File Modifier has to be applied.
        """
    def BeginSentFiles(self,sho : IFSelect_ShareOut,record : bool) -> None: 
        """
        Begins a sequence of recording the really sent files <sho> : the default file numbering is cleared If <record> is False, clears the list and stops recording If <record> is True, clears the list and commands recording Creation time corresponds to "stop recording"
        """
    def ClearAppliedModifiers(self,num : int) -> bool: 
        """
        Clears the list of File Modifiers to be applied on a file
        """
    def ClearFile(self,num : int) -> bool: 
        """
        Clears the Name attached to a File which was formerly defined by a call to AddFile. This Clearing can be undone by a call to NameFile (with same <num>) Returns True if Done, False else : if <num> is out of range
        """
    def ClearResult(self) -> None: 
        """
        Clears the list of produced Models
        """
    def CopiedRemaining(self,G : OCP.Interface.Interface_Graph,WL : IFSelect_WorkLibrary,TC : OCP.Interface.Interface_CopyTool,newmod : OCP.Interface.Interface_InterfaceModel) -> Any: 
        """
        Produces a Model copied from the Remaining List as <newmod> <newmod> is a Null Handle if this list is empty <WL> performs the copy by using <TC> <TC> is assumed to have been defined with the starting model same as defined by <G>.
        """
    def Copy(self,eval : IFSelect_ShareOutResult,WL : IFSelect_WorkLibrary,protocol : OCP.Interface.Interface_Protocol) -> OCP.Interface.Interface_CheckIterator: 
        """
        Performs the Copy Operations, which include the Modifications defined by the list of Modifiers. Memorizes the result, as a list of InterfaceModels with the corresponding FileNames They can then be sent, by the method Send, or queried Copy calls internal method Copying. Returns the produced CheckList
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
    def FileModel(self,num : int) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the content of a file before sending, under the form of an InterfaceModel, given its rank
        """
    def FileName(self,num : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the File Name for a file given its rank It is empty after a call to ClearFile on same <num>
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NameFile(self,num : int,filename : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Changes the Name attached to a File which was formerly defined by a call to AddFile Returns True if Done, False else : if <num> out of range or if the new <filename> is already attached to another File Remark : Giving an empty File Name is equivalent to ClearFile
        """
    def NbFiles(self) -> int: 
        """
        Returns the count of Files produced, i.e. the count of Models memorized (produced by the mmethod Copy) with their file names
        """
    def Send(self,eval : IFSelect_ShareOutResult,WL : IFSelect_WorkLibrary,protocol : OCP.Interface.Interface_Protocol) -> OCP.Interface.Interface_CheckIterator: 
        """
        Performs the Copy Operations (which include the Modifications) and Sends the result on files, without memorizing it. (the memorized result is ignored : neither queried not filled)
        """
    def SendAll(self,filename : str,G : OCP.Interface.Interface_Graph,WL : IFSelect_WorkLibrary,protocol : OCP.Interface.Interface_Protocol) -> OCP.Interface.Interface_CheckIterator: 
        """
        Sends a model (defined in <G>) into one file, without managing remaining data, already sent files, etc. Applies the Model and File Modifiers. Returns True if well done, False else
        """
    def SendCopied(self,WL : IFSelect_WorkLibrary,protocol : OCP.Interface.Interface_Protocol) -> OCP.Interface.Interface_CheckIterator: 
        """
        Sends the formerly defined results (see method Copy) to files, then clears it Remark : A Null File Name cause file to be not produced
        """
    def SendSelected(self,filename : str,G : OCP.Interface.Interface_Graph,WL : IFSelect_WorkLibrary,protocol : OCP.Interface.Interface_Protocol,iter : OCP.Interface.Interface_EntityIterator) -> OCP.Interface.Interface_CheckIterator: 
        """
        Sends a part of a model into one file. Model is gotten from <G>, the part is defined in <iter>. Remaining data are managed and can be later be worked on. Returns True if well done, False else
        """
    def SentFiles(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of recorded names of sent files. Can be empty (if no file has been sent). Returns a Null Handle if BeginSentFiles has stopped recording.
        """
    def SetAppliedModifiers(self,num : int,applied : IFSelect_AppliedModifiers) -> bool: 
        """
        Sets a list of File Modifiers to be applied on a file
        """
    def SetRemaining(self,CG : OCP.Interface.Interface_Graph) -> bool: 
        """
        Updates Graph status for remaining data, for each entity : - Entities just Sent to file or Copied (by CopiedRemaining) have their status set to 1 - the other keep their former status (1 for Send/Copied, 0 for Remaining) These status are computed by Copying/Sending/CopiedRemaining Then, SetRemaining updates graph status, and mustr be called just after one of these method has been called Returns True if done, False if remaining info if not in phase which the Graph (not same counts of items)
        """
    def SetShareOut(self,sho : IFSelect_ShareOut) -> None: 
        """
        Sets the ShareOut, which is used to define Modifiers to apply
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
class IFSelect_Modifier(IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    This class gives a frame for Actions which can work globally on a File once completely defined (i.e. afterwards)This class gives a frame for Actions which can work globally on a File once completely defined (i.e. afterwards)This class gives a frame for Actions which can work globally on a File once completely defined (i.e. afterwards)
    """
    def Applies(self,disp : IFSelect_Dispatch) -> bool: 
        """
        Returns True if a Model obtained from the Dispatch <disp> is to be treated (apart from the Selection criterium) If Dispatch(me) is Null, returns True. Else, checks <disp>
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self) -> IFSelect_Dispatch: 
        """
        Returns the Dispatch to be matched, Null if not set
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSelection(self) -> bool: 
        """
        Returns True if a Selection is set as an additionnal criterium
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a short text which defines the operation performed
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        This deferred method defines the action specific to each class of Modifier. It is called by a ModelCopier, once the Model generated and filled. ModelCopier has already checked the criteria (Dispatch, Model Rank, Selection) before calling it.
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class IFSelect_ModifReorder(IFSelect_Modifier, IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    This modifier reorders a whole model from its roots, i.e. according to <rootlast> status, it considers each of its roots, then it orders all its shared entities at any level, the result begins by the lower level entities ... ends by the roots.This modifier reorders a whole model from its roots, i.e. according to <rootlast> status, it considers each of its roots, then it orders all its shared entities at any level, the result begins by the lower level entities ... ends by the roots.This modifier reorders a whole model from its roots, i.e. according to <rootlast> status, it considers each of its roots, then it orders all its shared entities at any level, the result begins by the lower level entities ... ends by the roots.
    """
    def Applies(self,disp : IFSelect_Dispatch) -> bool: 
        """
        Returns True if a Model obtained from the Dispatch <disp> is to be treated (apart from the Selection criterium) If Dispatch(me) is Null, returns True. Else, checks <disp>
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self) -> IFSelect_Dispatch: 
        """
        Returns the Dispatch to be matched, Null if not set
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSelection(self) -> bool: 
        """
        Returns True if a Selection is set as an additionnal criterium
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Label as "Reorder, Roots (last or first)"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Acts by computing orders (by method All from ShareTool) then forcing them in the model. Remark that selection is ignored : ALL the model is processed in once
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,rootlast : bool=True) -> None: ...
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
class IFSelect_ModifEditForm(IFSelect_Modifier, IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    This modifier applies an EditForm on the entities selectedThis modifier applies an EditForm on the entities selectedThis modifier applies an EditForm on the entities selected
    """
    def Applies(self,disp : IFSelect_Dispatch) -> bool: 
        """
        Returns True if a Model obtained from the Dispatch <disp> is to be treated (apart from the Selection criterium) If Dispatch(me) is Null, returns True. Else, checks <disp>
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self) -> IFSelect_Dispatch: 
        """
        Returns the Dispatch to be matched, Null if not set
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EditForm(self) -> IFSelect_EditForm: 
        """
        Returns the EditForm
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSelection(self) -> bool: 
        """
        Returns True if a Selection is set as an additionnal criterium
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Label as "Apply EditForm <+ label of EditForm>"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Acts by applying an EditForm to entities, selected or all model
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,editform : IFSelect_EditForm) -> None: ...
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
class IFSelect_PacketList(OCP.Standard.Standard_Transient):
    """
    This class gives a simple way to return then consult a list of packets, determined from the content of a Model, by various criteria.This class gives a simple way to return then consult a list of packets, determined from the content of a Model, by various criteria.This class gives a simple way to return then consult a list of packets, determined from the content of a Model, by various criteria.
    """
    def Add(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an entity from the Model into the current packet for Add
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Adds an list of entities into the current packet for Add
        """
    def AddPacket(self) -> None: 
        """
        Declares a new Packet, ready to be filled The entities to be added will be added to this Packet
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Duplicated(self,count : int,andmore : bool) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns a list of entities duplicated : <count> times, if <andmore> is False, or <count> or more times, if <andmore> is True Hence, count=2 & andmore=True gives all duplicated entities count=1 gives non-duplicated entities (in only one packet) count=0 gives remaining entities (in no packet at all)
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Entities(self,numpack : int) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the content of a Packet given its rank Null Handle if <numpack> is out of range
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HighestDuplicationCount(self) -> int: 
        """
        Returns the highest number of packets which know a same entity For no duplication, should be one
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model of reference
        """
    def Name(self) -> str: 
        """
        Returns the recorded name for a packet list
        """
    def NbDuplicated(self,count : int,andmore : bool) -> int: 
        """
        Returns the count of entities duplicated : <count> times, if <andmore> is False, or <count> or more times, if <andmore> is True See Duplicated for more details
        """
    def NbEntities(self,numpack : int) -> int: 
        """
        Returns the count of entities in a Packet given its rank, or 0
        """
    def NbPackets(self) -> int: 
        """
        Returns the count of non-empty packets
        """
    def SetName(self,name : str) -> None: 
        """
        Sets a name to a packet list : this makes easier a general routine to print it. Default is "Packets"
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,model : OCP.Interface.Interface_InterfaceModel) -> None: ...
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
class IFSelect_ParamEditor(IFSelect_Editor, OCP.Standard.Standard_Transient):
    """
    A ParamEditor gives access for edition to a list of TypedValue (i.e. of Static too) Its definition is made of the TypedValue to edit themselves, and can add some constants, which can then be displayed but not changed (for instance, system name, processor version ...)A ParamEditor gives access for edition to a list of TypedValue (i.e. of Static too) Its definition is made of the TypedValue to edit themselves, and can add some constants, which can then be displayed but not changed (for instance, system name, processor version ...)A ParamEditor gives access for edition to a list of TypedValue (i.e. of Static too) Its definition is made of the TypedValue to edit themselves, and can add some constants, which can then be displayed but not changed (for instance, system name, processor version ...)
    """
    def AddConstantText(self,val : str,shortname : str,completename : str='') -> None: 
        """
        Adds a Constant Text, it will be Read Only By default, its long name equates its shortname
        """
    def AddValue(self,val : OCP.Interface.Interface_TypedValue,shortname : str='') -> None: 
        """
        Adds a TypedValue By default, its short name equates its complete name, it can be explicited
        """
    def Apply(self,form : IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
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
    def EditMode(self,num : int) -> IFSelect_EditValue: 
        """
        Returns the edit mode of a Value
        """
    def Form(self,readonly : bool,undoable : bool=True) -> IFSelect_EditForm: 
        """
        Builds and Returns an EditForm, empty (no data yet) Can be redefined to return a specific type of EditForm
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsList(self,num : int) -> bool: 
        """
        Tells if a parameter is a list
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def ListEditor(self,num : int) -> IFSelect_ListEditor: 
        """
        Returns a ListEditor for a parameter which is a List Default returns a basic ListEditor for a List, a Null Handle if <num> is not for a List. Can be redefined
        """
    def ListValue(self,form : IFSelect_EditForm,num : int) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the value of an EditForm as a List, for a given item If not a list, a Null Handle should be returned Default returns a Null Handle, because many Editors have no list to edit. To be redefined as required
        """
    def Load(self,form : IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        None
        """
    def MaxList(self,num : int) -> int: 
        """
        Returns max length allowed for a list = 0 means : list with no limit < 0 means : not a list
        """
    def MaxNameLength(self,what : int) -> int: 
        """
        Returns the MaxLength of, according to what : <what> = -1 : length of short names <what> = 0 : length of complete names <what> = 1 : length of values labels
        """
    def Name(self,num : int,isshort : bool=False) -> str: 
        """
        Returns the name of a Value (complete or short) from its ident Short Name can be empty
        """
    def NameNumber(self,name : str) -> int: 
        """
        Returns the number (ident) of a Value, from its name, short or complete. If not found, returns 0
        """
    def NbValues(self) -> int: 
        """
        Returns the count of Typed Values
        """
    def PrintDefs(self,S : OCP.Message.Message_Messenger,labels : bool=False) -> None: 
        """
        None
        """
    def PrintNames(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        None
        """
    def Recognize(self,form : IFSelect_EditForm) -> bool: 
        """
        None
        """
    def SetList(self,num : int,max : int=0) -> None: 
        """
        Sets a parameter to be a List max < 0 : not for a list (set when starting) max = 0 : list with no length limit (default for SetList) max > 0 : list limited to <max> items
        """
    def SetValue(self,num : int,typval : OCP.Interface.Interface_TypedValue,shortname : str='',accessmode : IFSelect_EditValue=IFSelect_EditValue.IFSelect_Editable) -> None: 
        """
        Sets a Typed Value for a given ident and short name, with an Edit Mode
        """
    @staticmethod
    def StaticEditor_s(list : OCP.TColStd.TColStd_HSequenceOfHAsciiString,label : str='') -> IFSelect_ParamEditor: 
        """
        Returns a ParamEditor to work on the Static Parameters of which names are listed in <list> Null Handle if <list> is null or empty
        """
    def StringValue(self,form : IFSelect_EditForm,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypedValue(self,num : int) -> OCP.Interface.Interface_TypedValue: 
        """
        Returns a Typed Value from its ident
        """
    def Update(self,form : IFSelect_EditForm,num : int,newval : OCP.TCollection.TCollection_HAsciiString,enforce : bool) -> bool: 
        """
        Updates the EditForm when a parameter is modified I.E. default does nothing, can be redefined, as follows : Returns True when done (even if does nothing), False in case of refuse (for instance, if the new value is not suitable) <num> is the rank of the parameter for the EDITOR itself <enforce> True means that protected parameters can be touched
        """
    def UpdateList(self,form : IFSelect_EditForm,num : int,newlist : OCP.TColStd.TColStd_HSequenceOfHAsciiString,enforce : bool) -> bool: 
        """
        Acts as Update, but when the value is a list
        """
    def __init__(self,nbmax : int=100,label : str='') -> None: ...
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
class IFSelect_PrintCount():
    """
    Lets you choose the manner in which you want to analyze an IGES or STEP file. Your analysis can be either message-oriented or entity-oriented. The specific values are as follows: - ItemsByEntity is a sequential list of all messages per entity of the defined type - CountByItem is the number of entities of the defined type, with their rank number per message - ShortByItem is the number of entities of the defined type, with their types per message; displays the rank numbers of the first five entities of the defined type per message - ListByItem is the number of entities of the defined type per message and the numbers of the entities - EntitiesByItem is the number of entities of the defined type, with their types, rank numbers and Directory Entry numbers per message - GeneralInfo is general information on transfer such as: - number of entities - number of roots - number of resulting Open CASCADE shapes - number of warnings and failures - CountSummary summary statistics for counters and signatures - ResultCount information that contains the number of roots in the IGES file and the number of resulting Open CASCADE shapes. - Mapping of the IGES root entities to the resulting Open CASCADE shape (including type and form of the IGES entity and type of the resulting shape).

    Members:

      IFSelect_ItemsByEntity

      IFSelect_CountByItem

      IFSelect_ShortByItem

      IFSelect_ListByItem

      IFSelect_EntitiesByItem

      IFSelect_CountSummary

      IFSelect_GeneralInfo

      IFSelect_Mapping

      IFSelect_ResultCount
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IFSelect_CountByItem: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_CountByItem
    IFSelect_CountSummary: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_CountSummary
    IFSelect_EntitiesByItem: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_EntitiesByItem
    IFSelect_GeneralInfo: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_GeneralInfo
    IFSelect_ItemsByEntity: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_ItemsByEntity
    IFSelect_ListByItem: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_ListByItem
    IFSelect_Mapping: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_Mapping
    IFSelect_ResultCount: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_ResultCount
    IFSelect_ShortByItem: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_ShortByItem
    __entries: dict # value = {'IFSelect_ItemsByEntity': (IFSelect_PrintCount.IFSelect_ItemsByEntity, None), 'IFSelect_CountByItem': (IFSelect_PrintCount.IFSelect_CountByItem, None), 'IFSelect_ShortByItem': (IFSelect_PrintCount.IFSelect_ShortByItem, None), 'IFSelect_ListByItem': (IFSelect_PrintCount.IFSelect_ListByItem, None), 'IFSelect_EntitiesByItem': (IFSelect_PrintCount.IFSelect_EntitiesByItem, None), 'IFSelect_CountSummary': (IFSelect_PrintCount.IFSelect_CountSummary, None), 'IFSelect_GeneralInfo': (IFSelect_PrintCount.IFSelect_GeneralInfo, None), 'IFSelect_Mapping': (IFSelect_PrintCount.IFSelect_Mapping, None), 'IFSelect_ResultCount': (IFSelect_PrintCount.IFSelect_ResultCount, None)}
    __members__: dict # value = {'IFSelect_ItemsByEntity': IFSelect_PrintCount.IFSelect_ItemsByEntity, 'IFSelect_CountByItem': IFSelect_PrintCount.IFSelect_CountByItem, 'IFSelect_ShortByItem': IFSelect_PrintCount.IFSelect_ShortByItem, 'IFSelect_ListByItem': IFSelect_PrintCount.IFSelect_ListByItem, 'IFSelect_EntitiesByItem': IFSelect_PrintCount.IFSelect_EntitiesByItem, 'IFSelect_CountSummary': IFSelect_PrintCount.IFSelect_CountSummary, 'IFSelect_GeneralInfo': IFSelect_PrintCount.IFSelect_GeneralInfo, 'IFSelect_Mapping': IFSelect_PrintCount.IFSelect_Mapping, 'IFSelect_ResultCount': IFSelect_PrintCount.IFSelect_ResultCount}
    pass
class IFSelect_PrintFail():
    """
    Indicates whether there will be information on warnings as well as on failures. The terms of this enumeration have the following semantics: - IFSelect_FailOnly gives information on failures only - IFSelect_FailAndWarn gives information on both failures and warnings. used to pilot PrintCheckList

    Members:

      IFSelect_FailOnly

      IFSelect_FailAndWarn
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IFSelect_FailAndWarn: OCP.IFSelect.IFSelect_PrintFail # value = IFSelect_PrintFail.IFSelect_FailAndWarn
    IFSelect_FailOnly: OCP.IFSelect.IFSelect_PrintFail # value = IFSelect_PrintFail.IFSelect_FailOnly
    __entries: dict # value = {'IFSelect_FailOnly': (IFSelect_PrintFail.IFSelect_FailOnly, None), 'IFSelect_FailAndWarn': (IFSelect_PrintFail.IFSelect_FailAndWarn, None)}
    __members__: dict # value = {'IFSelect_FailOnly': IFSelect_PrintFail.IFSelect_FailOnly, 'IFSelect_FailAndWarn': IFSelect_PrintFail.IFSelect_FailAndWarn}
    pass
class IFSelect_RemainMode():
    """
    None

    Members:

      IFSelect_RemainForget

      IFSelect_RemainCompute

      IFSelect_RemainDisplay

      IFSelect_RemainUndo
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IFSelect_RemainCompute: OCP.IFSelect.IFSelect_RemainMode # value = IFSelect_RemainMode.IFSelect_RemainCompute
    IFSelect_RemainDisplay: OCP.IFSelect.IFSelect_RemainMode # value = IFSelect_RemainMode.IFSelect_RemainDisplay
    IFSelect_RemainForget: OCP.IFSelect.IFSelect_RemainMode # value = IFSelect_RemainMode.IFSelect_RemainForget
    IFSelect_RemainUndo: OCP.IFSelect.IFSelect_RemainMode # value = IFSelect_RemainMode.IFSelect_RemainUndo
    __entries: dict # value = {'IFSelect_RemainForget': (IFSelect_RemainMode.IFSelect_RemainForget, None), 'IFSelect_RemainCompute': (IFSelect_RemainMode.IFSelect_RemainCompute, None), 'IFSelect_RemainDisplay': (IFSelect_RemainMode.IFSelect_RemainDisplay, None), 'IFSelect_RemainUndo': (IFSelect_RemainMode.IFSelect_RemainUndo, None)}
    __members__: dict # value = {'IFSelect_RemainForget': IFSelect_RemainMode.IFSelect_RemainForget, 'IFSelect_RemainCompute': IFSelect_RemainMode.IFSelect_RemainCompute, 'IFSelect_RemainDisplay': IFSelect_RemainMode.IFSelect_RemainDisplay, 'IFSelect_RemainUndo': IFSelect_RemainMode.IFSelect_RemainUndo}
    pass
class IFSelect_ReturnStatus():
    """
    Qualifies an execution status : RetVoid : normal execution which created nothing, or no data to process RetDone : normal execution with a result RetError : error in command or input data, no execution RetFail : execution was run and has failed RetStop : indicates end or stop (such as Raise)

    Members:

      IFSelect_RetVoid

      IFSelect_RetDone

      IFSelect_RetError

      IFSelect_RetFail

      IFSelect_RetStop
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IFSelect_RetDone: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetDone
    IFSelect_RetError: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetError
    IFSelect_RetFail: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetFail
    IFSelect_RetStop: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetStop
    IFSelect_RetVoid: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetVoid
    __entries: dict # value = {'IFSelect_RetVoid': (IFSelect_ReturnStatus.IFSelect_RetVoid, None), 'IFSelect_RetDone': (IFSelect_ReturnStatus.IFSelect_RetDone, None), 'IFSelect_RetError': (IFSelect_ReturnStatus.IFSelect_RetError, None), 'IFSelect_RetFail': (IFSelect_ReturnStatus.IFSelect_RetFail, None), 'IFSelect_RetStop': (IFSelect_ReturnStatus.IFSelect_RetStop, None)}
    __members__: dict # value = {'IFSelect_RetVoid': IFSelect_ReturnStatus.IFSelect_RetVoid, 'IFSelect_RetDone': IFSelect_ReturnStatus.IFSelect_RetDone, 'IFSelect_RetError': IFSelect_ReturnStatus.IFSelect_RetError, 'IFSelect_RetFail': IFSelect_ReturnStatus.IFSelect_RetFail, 'IFSelect_RetStop': IFSelect_ReturnStatus.IFSelect_RetStop}
    pass
class IFSelect_Selection(OCP.Standard.Standard_Transient):
    """
    A Selection allows to define a set of Interface Entities. Entities to be put on an output file should be identified in a way as independant from such or such execution as possible. This permits to handle comprehensive criteria, and to replay them when a new variant of an input file has to be processed.A Selection allows to define a set of Interface Entities. Entities to be put on an output file should be identified in a way as independant from such or such execution as possible. This permits to handle comprehensive criteria, and to replay them when a new variant of an input file has to be processed.A Selection allows to define a set of Interface Entities. Entities to be put on an output file should be identified in a way as independant from such or such execution as possible. This permits to handle comprehensive criteria, and to replay them when a new variant of an input file has to be processed.
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends (there can be zero, or one, or a list). Specific to each class of Selection
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which defines the criterium applied by a Selection (can be used to be printed, displayed ...) Specific to each class
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, computed from Input given as a Graph. Specific to each class of Selection Note that uniqueness of each entity is not required here This method can raise an exception as necessary
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectDeduct(IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectDeduct determines a list of Entities from an Input Selection, by a computation : Output list is not obliged to be a sub-list of Input list (for more specific, see SelectExtract for filtered sub-lists, and SelectExplore for recurcive exploration)A SelectDeduct determines a list of Entities from an Input Selection, by a computation : Output list is not obliged to be a sub-list of Input list (for more specific, see SelectExtract for filtered sub-lists, and SelectExplore for recurcive exploration)A SelectDeduct determines a list of Entities from an Input Selection, by a computation : Output list is not obliged to be a sub-list of Input list (for more specific, see SelectExtract for filtered sub-lists, and SelectExplore for recurcive exploration)
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which defines the criterium applied by a Selection (can be used to be printed, displayed ...) Specific to each class
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, computed from Input given as a Graph. Specific to each class of Selection Note that uniqueness of each entity is not required here This method can raise an exception as necessary
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectBase(IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    SelectBase works directly from an InterfaceModel : it is the first base for other Selections.SelectBase works directly from an InterfaceModel : it is the first base for other Selections.SelectBase works directly from an InterfaceModel : it is the first base for other Selections.
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list is empty for all SelectBase type Selections
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which defines the criterium applied by a Selection (can be used to be printed, displayed ...) Specific to each class
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, computed from Input given as a Graph. Specific to each class of Selection Note that uniqueness of each entity is not required here This method can raise an exception as necessary
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectCombine(IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectCombine type Selection defines algebraic operations between results of several Selections It is a deferred class : sub-classes will have to define precise what operator is to be appliedA SelectCombine type Selection defines algebraic operations between results of several Selections It is a deferred class : sub-classes will have to define precise what operator is to be appliedA SelectCombine type Selection defines algebraic operations between results of several Selections It is a deferred class : sub-classes will have to define precise what operator is to be applied
    """
    def Add(self,sel : IFSelect_Selection,atnum : int=0) -> None: 
        """
        Adds a Selection to the filling list By default, adds it to the end of the list A Positive rank less then NbInputs gives an insertion rank (InsertBefore : the new <atnum>th item of the list is <sel>)
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends That is to say, the list of Input Selections
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self,num : int) -> IFSelect_Selection: 
        """
        Returns an Input Selection, given its rank in the list
        """
    def InputRank(self,sel : IFSelect_Selection) -> int: 
        """
        Returns the rank of an input Selection, 0 if not in the list. Most generally, its value is meaningless, except for testing the presence of an input Selection : - == 0 if <sel> is not an input for <me> - > 0 if <sel> is an input for <me>
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which defines the criterium applied by a Selection (can be used to be printed, displayed ...) Specific to each class
        """
    def NbInputs(self) -> int: 
        """
        Returns the count of Input Selections
        """
    @overload
    def Remove(self,num : int) -> bool: 
        """
        Removes an input Selection. Returns True if Done, False, if <sel> is not an input for <me>

        Removes an input Selection, given its rank in the list Returns True if Done, False if <num> is out of range
        """
    @overload
    def Remove(self,sel : IFSelect_Selection) -> bool: ...
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, computed from Input given as a Graph. Specific to each class of Selection Note that uniqueness of each entity is not required here This method can raise an exception as necessary
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectControl(IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectControl kind Selection works with two input Selections in a dissymmetric way : the Main Input which gives an input list of Entities, to be processed, and the Second Input which gives another list, to be used to filter the main input.A SelectControl kind Selection works with two input Selections in a dissymmetric way : the Main Input which gives an input list of Entities, to be processed, and the Second Input which gives another list, to be used to filter the main input.A SelectControl kind Selection works with two input Selections in a dissymmetric way : the Main Input which gives an input list of Entities, to be processed, and the Second Input which gives another list, to be used to filter the main input.
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends That is to say, the list of Input Selections
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSecondInput(self) -> bool: 
        """
        Returns True if a Control Input is defined Thus, Result can be computed differently if there is a Control Input or if there is none
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which defines the criterium applied by a Selection (can be used to be printed, displayed ...) Specific to each class
        """
    def MainInput(self) -> IFSelect_Selection: 
        """
        Returns the Main Input Selection
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, computed from Input given as a Graph. Specific to each class of Selection Note that uniqueness of each entity is not required here This method can raise an exception as necessary
        """
    def SecondInput(self) -> IFSelect_Selection: 
        """
        Returns the Control Input Selection, or a Null Handle
        """
    def SetMainInput(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection to be the Main Input
        """
    def SetSecondInput(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection to be the Control Input
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectAnyList(IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectAnyList kind Selection selects a List of an Entity, as well as this Entity contains some. A List contains sub-entities as one per Item, or several (for instance if an Entity binds couples of sub-entities, each item is one of these couples). Remark that only Entities are taken into account (neither Reals, nor Strings, etc...)A SelectAnyList kind Selection selects a List of an Entity, as well as this Entity contains some. A List contains sub-entities as one per Item, or several (for instance if an Entity binds couples of sub-entities, each item is one of these couples). Remark that only Entities are taken into account (neither Reals, nor Strings, etc...)A SelectAnyList kind Selection selects a List of an Entity, as well as this Entity contains some. A List contains sub-entities as one per Item, or several (for instance if an Entity binds couples of sub-entities, each item is one of these couples). Remark that only Entities are taken into account (neither Reals, nor Strings, etc...)
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def FillResult(self,n1 : int,n2 : int,ent : OCP.Standard.Standard_Transient,res : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Puts into <res>, the sub-entities of the list, from n1 to n2 included. Remark that adequation with Entity's type and length of list has already been made at this stage Called by RootResult
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
    def HasLower(self) -> bool: 
        """
        Returns True if a Lower limit is defined
        """
    def HasUpper(self) -> bool: 
        """
        Returns True if a Lower limit is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def KeepInputEntity(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Keeps Input Entity, as having required type. It works by keeping in <iter>, only suitable Entities (SelectType can be used). Called by RootResult (which waits for ONE ENTITY MAX)
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Componants of List " then Specific List Label, then, following cases : " From .. Until .." or "From .." or "Until .." or "Rank no .." Specific type is given by deferred method ListLabel
        """
    def ListLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the specific label for the list, which is included as a part of Label
        """
    def Lower(self) -> IFSelect_IntParam: 
        """
        Returns Lower limit (if there is; else, value is senseless)
        """
    def LowerValue(self) -> int: 
        """
        Returns Integer Value of Lower Limit (0 if none)
        """
    def NbItems(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns count of Items in the list in the Entity <ent> If <ent> has not required type, returned value must be Zero
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities (list of entities complying with rank criterium) Error if the input list has more than one Item
        """
    def SetFrom(self,rankfrom : IFSelect_IntParam) -> None: 
        """
        Sets a Lower limit but no upper limit
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetOne(self,rank : IFSelect_IntParam) -> None: 
        """
        Sets a unique number (only one Entity will be sorted as True)
        """
    def SetRange(self,rankfrom : IFSelect_IntParam,rankto : IFSelect_IntParam) -> None: 
        """
        Sets a Range for numbers, with a lower and a upper limits
        """
    def SetUntil(self,rankto : IFSelect_IntParam) -> None: 
        """
        Sets an Upper limit but no lower limit (equivalent to lower 1)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    def Upper(self) -> IFSelect_IntParam: 
        """
        Returns Upper limit (if there is; else, value is senseless)
        """
    def UpperValue(self) -> int: 
        """
        Returns Integer Value of Upper Limit (0 if none)
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
class IFSelect_SelectDiff(IFSelect_SelectControl, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectDiff keeps the entities from a Selection, the Main Input, which are not listed by the Second InputA SelectDiff keeps the entities from a Selection, the Main Input, which are not listed by the Second InputA SelectDiff keeps the entities from a Selection, the Main Input, which are not listed by the Second Input
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends That is to say, the list of Input Selections
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSecondInput(self) -> bool: 
        """
        Returns True if a Control Input is defined Thus, Result can be computed differently if there is a Control Input or if there is none
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Difference"
        """
    def MainInput(self) -> IFSelect_Selection: 
        """
        Returns the Main Input Selection
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities : they are the Entities gotten from the Main Input but not from the Diff Input
        """
    def SecondInput(self) -> IFSelect_Selection: 
        """
        Returns the Control Input Selection, or a Null Handle
        """
    def SetMainInput(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection to be the Main Input
        """
    def SetSecondInput(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection to be the Control Input
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectEntityNumber(IFSelect_SelectBase, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectEntityNumber gets in an InterfaceModel (through a Graph), the Entity which has a specified Number (its rank of adding into the Model) : there can be zero (if none) or one. The Number is not directly defined as an Integer, but as a Parameter, which can be externally controledA SelectEntityNumber gets in an InterfaceModel (through a Graph), the Entity which has a specified Number (its rank of adding into the Model) : there can be zero (if none) or one. The Number is not directly defined as an Integer, but as a Parameter, which can be externally controledA SelectEntityNumber gets in an InterfaceModel (through a Graph), the Entity which has a specified Number (its rank of adding into the Model) : there can be zero (if none) or one. The Number is not directly defined as an Integer, but as a Parameter, which can be externally controled
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list is empty for all SelectBase type Selections
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Entity Number ..."
        """
    def Number(self) -> IFSelect_IntParam: 
        """
        Returns specified Number (as a Parameter)
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities : the Entity having the specified Number (this result assures naturally uniqueness)
        """
    def SetNumber(self,num : IFSelect_IntParam) -> None: 
        """
        Sets Entity Number to be taken (initially, none is set : 0)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectExtract(IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectExtract determines a list of Entities from an Input Selection, as a sub-list of the Input Result It works by applying a sort criterium on each Entity of the Input. This criterium can be applied Direct to Pick Items (default case) or Reverse to Remove ItemA SelectExtract determines a list of Entities from an Input Selection, as a sub-list of the Input Result It works by applying a sort criterium on each Entity of the Input. This criterium can be applied Direct to Pick Items (default case) or Reverse to Remove ItemA SelectExtract determines a list of Entities from an Input Selection, as a sub-list of the Input Result It works by applying a sort criterium on each Entity of the Input. This criterium can be applied Direct to Pick Items (default case) or Reverse to Remove Item
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium for extraction
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True for an Entity if it satisfies the Sort criterium It receives : - <rank>, the rank of the Entity in the Iteration, - <ent> , the Entity itself, and - <model>, the Starting Model Hence, the Entity to check is "model->Value(num)" (but an InterfaceModel allows other checks) This method is specific to each class of SelectExtract
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
class IFSelect_SelectExplore(IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectExplore determines from an input list of Entities, a list obtained by a way of exploration. This implies the possibility of recursive exploration : the output list is itself reused as input, etc... Examples : Shared Entities, can be considered at one level (immediate shared) or more, or max levelA SelectExplore determines from an input list of Entities, a list obtained by a way of exploration. This implies the possibility of recursive exploration : the output list is itself reused as input, etc... Examples : Shared Entities, can be considered at one level (immediate shared) or more, or max levelA SelectExplore determines from an input list of Entities, a list obtained by a way of exploration. This implies the possibility of recursive exploration : the output list is itself reused as input, etc... Examples : Shared Entities, can be considered at one level (immediate shared) or more, or max level
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Analyses and, if required, Explores an entity, as follows : The explored list starts as empty, it has to be filled by this method. If it returns False, <ent> is rejected for result (this is to be used only as safety) If it returns True and <explored> remains empty, <ent> is taken itself for result, not explored If it returns True and <explored> is not empty, the content of this list is considered : If maximum level is attained, it is taken for result Else (or no max), each of its entity will be itself explored
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the way of exploration
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectAnyType(IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectAnyType sorts the Entities of which the Type is Kind of a given Type : this Type for Match is specific of each class of SelectAnyTypeA SelectAnyType sorts the Entities of which the Type is Kind of a given Type : this Type for Match is specific of each class of SelectAnyTypeA SelectAnyType sorts the Entities of which the Type is Kind of a given Type : this Type for Match is specific of each class of SelectAnyType
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium for extraction
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True for an Entity (model->Value(num)) which is kind of the choosen type, given by the method TypeForMatch. Criterium is IsKind.
        """
    def SortInGraph(self,rank : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph) -> bool: 
        """
        Works as Sort but works on the Graph Default directly calls Sort, but it can be redefined If SortInGraph is redefined, Sort should be defined even if not called (to avoid deferred methods in a final class)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeForMatch(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type which has to be matched for select
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectFlag(IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectFlag queries a flag noted in the bitmap of the Graph. The Flag is designated by its Name. Flag Names are defined by Work Session and, as necessary, other functional objectsA SelectFlag queries a flag noted in the bitmap of the Graph. The Flag is designated by its Name. Flag Names are defined by Work Session and, as necessary, other functional objectsA SelectFlag queries a flag noted in the bitmap of the Graph. The Flag is designated by its Name. Flag Names are defined by Work Session and, as necessary, other functional objects
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium, includes the flag name
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def FlagName(self) -> str: 
        """
        Returns the name of the flag
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. It is redefined to work on the graph itself (not queried by sort)
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns always False because RootResult has done the work
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
    def __init__(self,flagname : str) -> None: ...
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
class IFSelect_SelectInList(IFSelect_SelectAnyList, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectInList kind Selection selects a List of an Entity, which is composed of single Entities To know the list on which to work, SelectInList has two deferred methods : NbItems (inherited from SelectAnyList) and ListedEntity (which gives an item as an Entity) which must be defined to get a List in an Entity of the required Type (and consider that list is empty if Entity has not required Type)A SelectInList kind Selection selects a List of an Entity, which is composed of single Entities To know the list on which to work, SelectInList has two deferred methods : NbItems (inherited from SelectAnyList) and ListedEntity (which gives an item as an Entity) which must be defined to get a List in an Entity of the required Type (and consider that list is empty if Entity has not required Type)A SelectInList kind Selection selects a List of an Entity, which is composed of single Entities To know the list on which to work, SelectInList has two deferred methods : NbItems (inherited from SelectAnyList) and ListedEntity (which gives an item as an Entity) which must be defined to get a List in an Entity of the required Type (and consider that list is empty if Entity has not required Type)
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def FillResult(self,n1 : int,n2 : int,ent : OCP.Standard.Standard_Transient,result : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Puts into the result, the sub-entities of the list, from n1 to n2 included. Remark that adequation with Entity's type and length of list has already been made at this stage Called by RootResult; calls ListedEntity (see below)
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
    def HasLower(self) -> bool: 
        """
        Returns True if a Lower limit is defined
        """
    def HasUpper(self) -> bool: 
        """
        Returns True if a Lower limit is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def KeepInputEntity(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Keeps Input Entity, as having required type. It works by keeping in <iter>, only suitable Entities (SelectType can be used). Called by RootResult (which waits for ONE ENTITY MAX)
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Componants of List " then Specific List Label, then, following cases : " From .. Until .." or "From .." or "Until .." or "Rank no .." Specific type is given by deferred method ListLabel
        """
    def ListLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the specific label for the list, which is included as a part of Label
        """
    def ListedEntity(self,num : int,ent : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: 
        """
        Returns an Entity, given its rank in the list
        """
    def Lower(self) -> IFSelect_IntParam: 
        """
        Returns Lower limit (if there is; else, value is senseless)
        """
    def LowerValue(self) -> int: 
        """
        Returns Integer Value of Lower Limit (0 if none)
        """
    def NbItems(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns count of Items in the list in the Entity <ent> If <ent> has not required type, returned value must be Zero
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities (list of entities complying with rank criterium) Error if the input list has more than one Item
        """
    def SetFrom(self,rankfrom : IFSelect_IntParam) -> None: 
        """
        Sets a Lower limit but no upper limit
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetOne(self,rank : IFSelect_IntParam) -> None: 
        """
        Sets a unique number (only one Entity will be sorted as True)
        """
    def SetRange(self,rankfrom : IFSelect_IntParam,rankto : IFSelect_IntParam) -> None: 
        """
        Sets a Range for numbers, with a lower and a upper limits
        """
    def SetUntil(self,rankto : IFSelect_IntParam) -> None: 
        """
        Sets an Upper limit but no lower limit (equivalent to lower 1)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    def Upper(self) -> IFSelect_IntParam: 
        """
        Returns Upper limit (if there is; else, value is senseless)
        """
    def UpperValue(self) -> int: 
        """
        Returns Integer Value of Upper Limit (0 if none)
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
class IFSelect_SelectIncorrectEntities(IFSelect_SelectFlag, IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectIncorrectEntities sorts the Entities which have been noted as Incorrect in the Graph of the Session (flag "Incorrect") It can find a result only if ComputeCheck has formerly been called on the WorkSession. Else, its result will be empty.A SelectIncorrectEntities sorts the Entities which have been noted as Incorrect in the Graph of the Session (flag "Incorrect") It can find a result only if ComputeCheck has formerly been called on the WorkSession. Else, its result will be empty.A SelectIncorrectEntities sorts the Entities which have been noted as Incorrect in the Graph of the Session (flag "Incorrect") It can find a result only if ComputeCheck has formerly been called on the WorkSession. Else, its result will be empty.
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium, includes the flag name
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def FlagName(self) -> str: 
        """
        Returns the name of the flag
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. It is redefined to work on the graph itself (not queried by sort)
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns always False because RootResult has done the work
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
class IFSelect_SelectIntersection(IFSelect_SelectCombine, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectIntersection filters the Entities issued from several other Selections as Intersection of results : "AND" operatorA SelectIntersection filters the Entities issued from several other Selections as Intersection of results : "AND" operatorA SelectIntersection filters the Entities issued from several other Selections as Intersection of results : "AND" operator
    """
    def Add(self,sel : IFSelect_Selection,atnum : int=0) -> None: 
        """
        Adds a Selection to the filling list By default, adds it to the end of the list A Positive rank less then NbInputs gives an insertion rank (InsertBefore : the new <atnum>th item of the list is <sel>)
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends That is to say, the list of Input Selections
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self,num : int) -> IFSelect_Selection: 
        """
        Returns an Input Selection, given its rank in the list
        """
    def InputRank(self,sel : IFSelect_Selection) -> int: 
        """
        Returns the rank of an input Selection, 0 if not in the list. Most generally, its value is meaningless, except for testing the presence of an input Selection : - == 0 if <sel> is not an input for <me> - > 0 if <sel> is an input for <me>
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Intersection (AND)"
        """
    def NbInputs(self) -> int: 
        """
        Returns the count of Input Selections
        """
    @overload
    def Remove(self,num : int) -> bool: 
        """
        Removes an input Selection. Returns True if Done, False, if <sel> is not an input for <me>

        Removes an input Selection, given its rank in the list Returns True if Done, False if <num> is out of range
        """
    @overload
    def Remove(self,sel : IFSelect_Selection) -> bool: ...
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected Entities, which is the common part of results from all input selections. Uniqueness is guaranteed.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectModelEntities(IFSelect_SelectBase, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectModelEntities gets all the Entities of an InterfaceModel.A SelectModelEntities gets all the Entities of an InterfaceModel.A SelectModelEntities gets all the Entities of an InterfaceModel.
    """
    def CompleteResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        The complete list of Entities (including shared ones) ... is exactly identical to RootResults in this case
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list is empty for all SelectBase type Selections
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Model Entities"
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities : the Entities of the Model (note that this result assures naturally uniqueness)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectModelRoots(IFSelect_SelectBase, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectModelRoots gets all the Root Entities of an InterfaceModel. Remember that a "Root Entity" is defined as having no Sharing Entity (if there is a Loop between Entities, none of them can be a "Root").A SelectModelRoots gets all the Root Entities of an InterfaceModel. Remember that a "Root Entity" is defined as having no Sharing Entity (if there is a Loop between Entities, none of them can be a "Root").A SelectModelRoots gets all the Root Entities of an InterfaceModel. Remember that a "Root Entity" is defined as having no Sharing Entity (if there is a Loop between Entities, none of them can be a "Root").
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list is empty for all SelectBase type Selections
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Model Roots"
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities : the Roots of the Model (note that this result assures naturally uniqueness)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectPointed(IFSelect_SelectBase, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This type of Selection is intended to describe a direct selection without an explicit criterium, for instance the result of picking viewed entities on a graphic screenThis type of Selection is intended to describe a direct selection without an explicit criterium, for instance the result of picking viewed entities on a graphic screenThis type of Selection is intended to describe a direct selection without an explicit criterium, for instance the result of picking viewed entities on a graphic screen
    """
    def Add(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Adds an item. Returns True if Done, False if <item> is already in the selected list
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> bool: 
        """
        Adds all the items defined in a list. Returns True if at least one item has been added, False else
        """
    def Clear(self) -> None: 
        """
        Clears the list of selected items Also says the list is unset All Add* methods and SetList say the list is set
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list is empty for all SelectBase type Selections
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsSet(self) -> bool: 
        """
        Tells if the list has been set. Even if empty
        """
    def Item(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns an item given its rank, or a Null Handle
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which identifies the type of selection made. It is "Pointed Entities"
        """
    def NbItems(self) -> int: 
        """
        Returns the count of selected items
        """
    def Rank(self,item : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the rank of an item in the selected list, or 0.
        """
    def Remove(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Removes an item. Returns True if Done, False if <item> was not in the selected list
        """
    def RemoveList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> bool: 
        """
        Removes all the items defined in a list. Returns True if at least one item has been removed, False else
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected items. Only the selected entities which are present in the graph are given (this result assures uniqueness).
        """
    def SetEntity(self,item : OCP.Standard.Standard_Transient) -> None: 
        """
        As SetList but with only one entity If <ent> is Null, the list is said as being set but is empty
        """
    def SetList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Sets a given list to define the list of selected items <list> can be empty or null : in this case, the list is said as being set, but it is empty
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Toggle(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Toggles status of an item : adds it if not pointed or removes it if already pointed. Returns the new status (Pointed or not)
        """
    def ToggleList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> bool: 
        """
        Toggles status of all the items defined in a list : adds it if not pointed or removes it if already pointed.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    @overload
    def Update(self,control : OCP.Interface.Interface_CopyControl) -> None: 
        """
        Rebuilds the selected list. Any selected entity which has a bound result is replaced by this result, else it is removed.

        Rebuilds the selected list, by querying a Transformer (same principle as from a CopyControl)
        """
    @overload
    def Update(self,trf : IFSelect_Transformer) -> None: ...
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
class IFSelect_SelectRange(IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectRange keeps or rejects a sub-set of the input set, that is the Entities of which rank in the iteration list is in a given range (for instance form 2nd to 6th, etc...)A SelectRange keeps or rejects a sub-set of the input set, that is the Entities of which rank in the iteration list is in a given range (for instance form 2nd to 6th, etc...)A SelectRange keeps or rejects a sub-set of the input set, that is the Entities of which rank in the iteration list is in a given range (for instance form 2nd to 6th, etc...)
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium : following cases, " From .. Until .." or "From .." or "Until .." or "Rank no .."
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def HasLower(self) -> bool: 
        """
        Returns True if a Lower limit is defined
        """
    def HasUpper(self) -> bool: 
        """
        Returns True if a Lower limit is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def Lower(self) -> IFSelect_IntParam: 
        """
        Returns Lower limit (if there is; else, value is senseless)
        """
    def LowerValue(self) -> int: 
        """
        Returns Value of Lower Limit (0 if none is defined)
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetFrom(self,rankfrom : IFSelect_IntParam) -> None: 
        """
        Sets a Lower limit but no upper limit
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetOne(self,rank : IFSelect_IntParam) -> None: 
        """
        Sets a unique number (only one Entity will be sorted as True)
        """
    def SetRange(self,rankfrom : IFSelect_IntParam,rankto : IFSelect_IntParam) -> None: 
        """
        Sets a Range for numbers, with a lower and a upper limits Error if rankto is lower then rankfrom
        """
    def SetUntil(self,rankto : IFSelect_IntParam) -> None: 
        """
        Sets an Upper limit but no lower limit (equivalent to lower 1)
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True for an Entity of which occurence number in the iteration is inside the selected Range (considers <rank>)
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
    def Upper(self) -> IFSelect_IntParam: 
        """
        Returns Upper limit (if there is; else, value is senseless)
        """
    def UpperValue(self) -> int: 
        """
        Returns Value of Upper Limit (0 if none is defined)
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
class IFSelect_SelectRootComps(IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectRootComps sorts the Entities which are part of Strong Componants, local roots of a set of Entities : they can be Single Componants (containing one Entity) or Cycles This class gives a more secure result than SelectRoots (which considers only Single Componants) but is longer to work : it can be used when there can be or there are cycles in a Model For each cycle, one Entity is given arbitrarily Reject works as for SelectRoots : Strong Componants defined in the input list which are not local roots are givenA SelectRootComps sorts the Entities which are part of Strong Componants, local roots of a set of Entities : they can be Single Componants (containing one Entity) or Cycles This class gives a more secure result than SelectRoots (which considers only Single Componants) but is longer to work : it can be used when there can be or there are cycles in a Model For each cycle, one Entity is given arbitrarily Reject works as for SelectRoots : Strong Componants defined in the input list which are not local roots are givenA SelectRootComps sorts the Entities which are part of Strong Componants, local roots of a set of Entities : they can be Single Componants (containing one Entity) or Cycles This class gives a more secure result than SelectRoots (which considers only Single Componants) but is longer to work : it can be used when there can be or there are cycles in a Model For each cycle, one Entity is given arbitrarily Reject works as for SelectRoots : Strong Componants defined in the input list which are not local roots are given
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium : "Local Root Componants"
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of local root strong componants, by one Entity par componant. It is redefined for a purpose of effeciency : calling a Sort routine for each Entity would cost more ressource than to work in once using a Map RootResult takes in account the Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns always True, because RootResult has done work
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
class IFSelect_SelectRoots(IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectRoots sorts the Entities which are local roots of a set of Entities (not shared by other Entities inside this set, even if they are shared by other Entities outside it)A SelectRoots sorts the Entities which are local roots of a set of Entities (not shared by other Entities inside this set, even if they are shared by other Entities outside it)A SelectRoots sorts the Entities which are local roots of a set of Entities (not shared by other Entities inside this set, even if they are shared by other Entities outside it)
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium : "Local Root Entities"
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of local roots. It is redefined for a purpose of effeciency : calling a Sort routine for each Entity would cost more ressource than to work in once using a Map RootResult takes in account the Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns always True, because RootResult has done work
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
class IFSelect_SelectSent(IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This class returns entities according sending to a file Once a model has been loaded, further sendings are recorded as status in the graph (for each value, a count of sendings)This class returns entities according sending to a file Once a model has been loaded, further sendings are recorded as status in the graph (for each value, a count of sendings)This class returns entities according sending to a file Once a model has been loaded, further sendings are recorded as status in the graph (for each value, a count of sendings)
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
        """
        Returns the Alternate Definition It is returned modifiable, hence an already defined SelectPointed can be used But if it was not yet defined, it is created the first time
        """
    def AtLeast(self) -> bool: 
        """
        Returns the <atleast> status, True for sending at least the sending count, False for sending exactly the sending count Remark : if SentCount is 0, AtLeast is ignored
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
        Returns a text defining the criterium : query : SentCount = 0 -> "Remaining (non-sent) entities" SentCount = 1, AtLeast = True -> "Sent entities" SentCount = 1, AtLeast = False -> "Sent once (no duplicated)" SentCount = 2, AtLeast = True -> "Sent several times entities" SentCount = 2, AtLeast = False -> "Sent twice entities" SentCount > 2, AtLeast = True -> "Sent at least <count> times entities" SentCount > 2, AtLeast = False -> "Sent <count> times entities"
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. It is redefined to work on the graph itself (not queried by sort)
        """
    def SentCount(self) -> int: 
        """
        Returns the queried count of sending
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns always False because RootResult has done the work
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
    def __init__(self,sentcount : int=1,atleast : bool=True) -> None: ...
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
class IFSelect_SelectShared(IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectShared selects Entities which are directly Shared by the Entities of the Input listA SelectShared selects Entities which are directly Shared by the Entities of the Input listA SelectShared selects Entities which are directly Shared by the Entities of the Input list
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Shared (one level)"
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities (list of entities shared by those of input list)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectSharing(IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectSharing selects Entities which directly Share (Level One) the Entities of the Input list Remark : if an Entity of the Input List directly shares another one, it is of course present in the Result ListA SelectSharing selects Entities which directly Share (Level One) the Entities of the Input list Remark : if an Entity of the Input List directly shares another one, it is of course present in the Result ListA SelectSharing selects Entities which directly Share (Level One) the Entities of the Input list Remark : if an Entity of the Input List directly shares another one, it is of course present in the Result List
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Sharing (one level)"
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities (list of entities which share (level one) those of input list)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectSignature(IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectSignature sorts the Entities on a Signature Matching. The signature to match is given at creation time. Also, the required match is given at creation time : exact (IsEqual) or contains (the Type's Name must contain the criterium Text)A SelectSignature sorts the Entities on a Signature Matching. The signature to match is given at creation time. Also, the required match is given at creation time : exact (IsEqual) or contains (the Type's Name must contain the criterium Text)A SelectSignature sorts the Entities on a Signature Matching. The signature to match is given at creation time. Also, the required match is given at creation time : exact (IsEqual) or contains (the Type's Name must contain the criterium Text)
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
        """
        Returns the Alternate Definition It is returned modifiable, hence an already defined SelectPointed can be used But if it was not yet defined, it is created the first time
        """
    def CompleteResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities involved by a Selection, i.e. UniqueResult plus the shared entities (directly or not)
        """
    def Counter(self) -> IFSelect_SignCounter: 
        """
        Returns the used SignCounter. Can be used as alternative for Signature
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
        Returns a text defining the criterium. (it refers to the text and exact flag to be matched, and is qualified by the Name provided by the Signature)
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsExact(self) -> bool: 
        """
        Returns True if match must be exact
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Signature(self) -> IFSelect_Signature: 
        """
        Returns the used Signature, then it is possible to access it, modify it as required. Can be null, hence see Counter
        """
    def SignatureText(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Text used to Sort Entity on its Signature or SignCounter
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Not called, defined only to remove a deferred method here
        """
    def SortInGraph(self,rank : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph) -> bool: 
        """
        Returns True for an Entity (model->Value(num)) of which the signature matches the text given as creation time May also work with a Counter from the Graph
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
    def __init__(self,matcher : IFSelect_Signature,signtext : OCP.TCollection.TCollection_AsciiString,exact : bool=True) -> None: ...
    @overload
    def __init__(self,matcher : IFSelect_Signature,signtext : str,exact : bool=True) -> None: ...
    @overload
    def __init__(self,matcher : IFSelect_SignCounter,signtext : str,exact : bool=True) -> None: ...
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
class IFSelect_SelectSignedShared(IFSelect_SelectExplore, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    In the graph, explore the Shareds of the input entities, until it encounters some which match a given Signature (for a limited level, filters the returned list) By default, fitted for any levelIn the graph, explore the Shareds of the input entities, until it encounters some which match a given Signature (for a limited level, filters the returned list) By default, fitted for any levelIn the graph, explore the Shareds of the input entities, until it encounters some which match a given Signature (for a limited level, filters the returned list) By default, fitted for any level
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Explores an entity : its Shared entities <ent> to take if it matches the Signature At level max, filters the result. Else gives all Shareds
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium. (it refers to the text and exact flag to be matched, and is qualified by the Name provided by the Signature)
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
        """
    def IsExact(self) -> bool: 
        """
        Returns True if match must be exact
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
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Signature(self) -> IFSelect_Signature: 
        """
        Returns the used Signature, then it is possible to access it, modify it as required
        """
    def SignatureText(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Text used to Sort Entity on its Signature
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    def __init__(self,matcher : IFSelect_Signature,signtext : str,exact : bool=True,level : int=0) -> None: ...
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
class IFSelect_SelectSignedSharing(IFSelect_SelectExplore, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    In the graph, explore the sharings of the input entities, until it encounters some which match a given Signature (for a limited level, filters the returned list) By default, fitted for any levelIn the graph, explore the sharings of the input entities, until it encounters some which match a given Signature (for a limited level, filters the returned list) By default, fitted for any levelIn the graph, explore the sharings of the input entities, until it encounters some which match a given Signature (for a limited level, filters the returned list) By default, fitted for any level
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Explores an entity : its sharing entities <ent> to take if it matches the Signature At level max, filters the result. Else gives all sharings
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium. (it refers to the text and exact flag to be matched, and is qualified by the Name provided by the Signature)
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
        """
    def IsExact(self) -> bool: 
        """
        Returns True if match must be exact
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
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Signature(self) -> IFSelect_Signature: 
        """
        Returns the used Signature, then it is possible to access it, modify it as required
        """
    def SignatureText(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Text used to Sort Entity on its Signature
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    def __init__(self,matcher : IFSelect_Signature,signtext : str,exact : bool=True,level : int=0) -> None: ...
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
class IFSelect_SelectSuite(IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectSuite can describe a suite of SelectDeduct as a unique one : in other words, it can be seen as a "macro selection"A SelectSuite can describe a suite of SelectDeduct as a unique one : in other words, it can be seen as a "macro selection"A SelectSuite can describe a suite of SelectDeduct as a unique one : in other words, it can be seen as a "macro selection"
    """
    def AddInput(self,item : IFSelect_Selection) -> bool: 
        """
        Adds an input selection. I.E. : If <item> is a SelectDeduct, adds it as Previous, not as Input Else, sets it as Input Returns True when done Returns False and refuses to work if Input is already defined
        """
    def AddNext(self,item : IFSelect_SelectDeduct) -> None: 
        """
        Adds a new last item (prepends to the list) If <item> is null, does nothing
        """
    def AddPrevious(self,item : IFSelect_SelectDeduct) -> None: 
        """
        Adds a new first item (prepends to the list). The Input is not touched If <item> is null, does nothing
        """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self,num : int) -> IFSelect_SelectDeduct: 
        """
        Returns an item from its rank in the list (the Input is always apart)
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the Label Either it has been defined by SetLabel, or it will give "Suite of nn Selections"
        """
    def NbItems(self) -> int: 
        """
        Returns the count of Items
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities To do this, once InputResult has been taken (if Input or Alternate has been defined, else the first Item gives it) : this result is set as alternate input for the first item, which computes its result : this result is set as alternate input for the second item, etc...
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetLabel(self,lab : str) -> None: 
        """
        Sets a value for the Label
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectType(IFSelect_SelectAnyType, IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectType keeps or rejects Entities of which the Type is Kind of a given Cdl TypeA SelectType keeps or rejects Entities of which the Type is Kind of a given Cdl TypeA SelectType keeps or rejects Entities of which the Type is Kind of a given Cdl Type
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium. (should by gotten from Type of Entity used for instantiation)
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetType(self,atype : OCP.Standard.Standard_Type) -> None: 
        """
        Sets a TYpe for filter
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True for an Entity (model->Value(num)) which is kind of the choosen type, given by the method TypeForMatch. Criterium is IsKind.
        """
    def SortInGraph(self,rank : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph) -> bool: 
        """
        Works as Sort but works on the Graph Default directly calls Sort, but it can be redefined If SortInGraph is redefined, Sort should be defined even if not called (to avoid deferred methods in a final class)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeForMatch(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type to be matched for select : this is the type given at instantiation time
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,atype : OCP.Standard.Standard_Type) -> None: ...
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
class IFSelect_SelectUnion(IFSelect_SelectCombine, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectUnion cumulates the Entities issued from several other Selections (union of results : "OR" operator)A SelectUnion cumulates the Entities issued from several other Selections (union of results : "OR" operator)A SelectUnion cumulates the Entities issued from several other Selections (union of results : "OR" operator)
    """
    def Add(self,sel : IFSelect_Selection,atnum : int=0) -> None: 
        """
        Adds a Selection to the filling list By default, adds it to the end of the list A Positive rank less then NbInputs gives an insertion rank (InsertBefore : the new <atnum>th item of the list is <sel>)
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
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends That is to say, the list of Input Selections
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self,num : int) -> IFSelect_Selection: 
        """
        Returns an Input Selection, given its rank in the list
        """
    def InputRank(self,sel : IFSelect_Selection) -> int: 
        """
        Returns the rank of an input Selection, 0 if not in the list. Most generally, its value is meaningless, except for testing the presence of an input Selection : - == 0 if <sel> is not an input for <me> - > 0 if <sel> is an input for <me>
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Union (OR)"
        """
    def NbInputs(self) -> int: 
        """
        Returns the count of Input Selections
        """
    @overload
    def Remove(self,num : int) -> bool: 
        """
        Removes an input Selection. Returns True if Done, False, if <sel> is not an input for <me>

        Removes an input Selection, given its rank in the list Returns True if Done, False if <num> is out of range
        """
    @overload
    def Remove(self,sel : IFSelect_Selection) -> bool: ...
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected Entities, which is the addition result from all input selections. Uniqueness is guaranteed.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them beeing unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IFSelect_SelectUnknownEntities(IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectUnknownEntities sorts the Entities which are qualified as "Unknown" (their Type has not been recognized)A SelectUnknownEntities sorts the Entities which are qualified as "Unknown" (their Type has not been recognized)A SelectUnknownEntities sorts the Entities which are qualified as "Unknown" (their Type has not been recognized)
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium : "Recognized Entities"
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True for an Entity which is qualified as "Unknown", i.e. if <model> known <ent> (through its Number) as Unknown
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
class IFSelect_SelectErrorEntities(IFSelect_SelectExtract, IFSelect_SelectDeduct, IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    A SelectErrorEntities sorts the Entities which are qualified as "Error" (their Type has not been recognized) during reading a File. This does not concern Entities which are syntactically correct, but with incorrect data (for integrity constraints).A SelectErrorEntities sorts the Entities which are qualified as "Error" (their Type has not been recognized) during reading a File. This does not concern Entities which are syntactically correct, but with incorrect data (for integrity constraints).A SelectErrorEntities sorts the Entities which are qualified as "Error" (their Type has not been recognized) during reading a File. This does not concern Entities which are syntactically correct, but with incorrect data (for integrity constraints).
    """
    def Alternate(self) -> IFSelect_SelectPointed: 
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
        Returns a text defining the criterium : "Error Entities"
        """
    def FillIterator(self,iter : IFSelect_SelectionIterator) -> None: 
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
    def Input(self) -> IFSelect_Selection: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True for an Entity which is qualified as "Error", i.e. if <model> explicitly knows <ent> (through its Number) as Erroneous
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
class IFSelect_SelectionIterator():
    """
    Defines an Iterator on a list of Selections
    """
    def AddFromIter(self,iter : IFSelect_SelectionIterator) -> None: 
        """
        Adds to an iterator the content of another one (each selection is present only once in the result)
        """
    def AddItem(self,sel : IFSelect_Selection) -> None: 
        """
        Adds a Selection to an iterator (if not yet noted)
        """
    def AddList(self,list : IFSelect_TSeqOfSelection) -> None: 
        """
        Adds a list of Selections to an iterator (this list comes from the description of a Selection or a Dispatch, etc...)
        """
    def More(self) -> bool: 
        """
        Returns True if there are more Selections to get
        """
    def Next(self) -> None: 
        """
        Sets iterator to the next item
        """
    def Value(self) -> IFSelect_Selection: 
        """
        Returns the current Selction beeing iterated Error if count of Selection has been passed
        """
    @overload
    def __init__(self,sel : IFSelect_Selection) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IFSelect_SequenceOfAppliedModifiers(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : IFSelect_SequenceOfAppliedModifiers) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : IFSelect_AppliedModifiers) -> None: ...
    def Assign(self,theOther : IFSelect_SequenceOfAppliedModifiers) -> IFSelect_SequenceOfAppliedModifiers: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IFSelect_AppliedModifiers: 
        """
        First item access
        """
    def ChangeLast(self) -> IFSelect_AppliedModifiers: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IFSelect_AppliedModifiers: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> IFSelect_AppliedModifiers: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IFSelect_AppliedModifiers) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IFSelect_SequenceOfAppliedModifiers) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IFSelect_SequenceOfAppliedModifiers) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IFSelect_AppliedModifiers) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IFSelect_AppliedModifiers: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theSeq : IFSelect_SequenceOfAppliedModifiers) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IFSelect_AppliedModifiers) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : IFSelect_AppliedModifiers) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IFSelect_SequenceOfAppliedModifiers) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IFSelect_AppliedModifiers: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : IFSelect_SequenceOfAppliedModifiers) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IFSelect_SequenceOfGeneralModifier(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IFSelect_GeneralModifier) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IFSelect_SequenceOfGeneralModifier) -> None: ...
    def Assign(self,theOther : IFSelect_SequenceOfGeneralModifier) -> IFSelect_SequenceOfGeneralModifier: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IFSelect_GeneralModifier: 
        """
        First item access
        """
    def ChangeLast(self) -> IFSelect_GeneralModifier: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IFSelect_GeneralModifier: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> IFSelect_GeneralModifier: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IFSelect_GeneralModifier) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IFSelect_SequenceOfGeneralModifier) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IFSelect_SequenceOfGeneralModifier) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IFSelect_GeneralModifier) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IFSelect_GeneralModifier: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : IFSelect_GeneralModifier) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : IFSelect_SequenceOfGeneralModifier) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : IFSelect_GeneralModifier) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IFSelect_SequenceOfGeneralModifier) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IFSelect_GeneralModifier: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IFSelect_SequenceOfGeneralModifier) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IFSelect_SequenceOfInterfaceModel(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IFSelect_SequenceOfInterfaceModel) -> None: ...
    def Assign(self,theOther : IFSelect_SequenceOfInterfaceModel) -> IFSelect_SequenceOfInterfaceModel: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IFSelect_SequenceOfInterfaceModel) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IFSelect_SequenceOfInterfaceModel) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Interface.Interface_InterfaceModel) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theSeq : IFSelect_SequenceOfInterfaceModel) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.Interface.Interface_InterfaceModel) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IFSelect_SequenceOfInterfaceModel) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : IFSelect_SequenceOfInterfaceModel) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IFSelect_BasicDumper(IFSelect_SessionDumper, OCP.Standard.Standard_Transient):
    """
    BasicDumper takes into account, for SessionFile, all the classes defined in the package IFSelect : Selections, Dispatches (there is no Modifier)BasicDumper takes into account, for SessionFile, all the classes defined in the package IFSelect : Selections, Dispatches (there is no Modifier)BasicDumper takes into account, for SessionFile, all the classes defined in the package IFSelect : Selections, Dispatches (there is no Modifier)
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
    @staticmethod
    def First_s() -> IFSelect_SessionDumper: 
        """
        Returns the First item of the Library of Dumper. The Next ones are then obtained by Next on the returned items
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Next(self) -> IFSelect_SessionDumper: 
        """
        Returns the Next SesionDumper in the Library. Returns a Null Handle at the End.
        """
    def ReadOwn(self,file : IFSelect_SessionFile,type : OCP.TCollection.TCollection_AsciiString,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Recognizes and Read Own Parameters for Types of package IFSelect. Returns True if done and <item> created, False else
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteOwn(self,file : IFSelect_SessionFile,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Write the Own Parameters of Types defined in package IFSelect Returns True if <item> has been processed, False else
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
class IFSelect_SessionFile():
    """
    A SessionFile is intended to manage access between a WorkSession and an Ascii Form, to be considered as a Dump. It allows to write the File from the WorkSession, and later read the File to the WorkSession, by keeping required descriptions (such as dependances).
    """
    def AddItem(self,item : OCP.Standard.Standard_Transient,active : bool=True) -> None: 
        """
        Adds an Item to the WorkSession, taken as Name the first item of the read Line. If this Name is not a Name but a Number or if this Name is already recorded in the WorkSession, it adds the Item but with no Name. Then the Name is recorded in order to be used by the method ItemValue <active> commands to make <item> active or not in the session
        """
    def AddLine(self,line : str) -> None: 
        """
        Adds a line to the list of recorded lines
        """
    def ClearLines(self) -> None: 
        """
        Clears the lines recorded whatever for writing or for reading
        """
    def Destroy(self) -> None: 
        """
        Specific Destructor (closes the File if not yet done)
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the last Read or Write operation has been corectly performed. ELse returns False.
        """
    def IsText(self,num : int) -> bool: 
        """
        Returns True if a Parameter, in the Own List (see NbOwnParams) is a Text (between "..."). Else it is an Item (Parameter, Selection, Dispatch ...), which can be Void.
        """
    def IsVoid(self,num : int) -> bool: 
        """
        Returns True if a Parameter, given its rank in the Own List (see NbOwnParams), is Void. Returns also True if <num> is out of range (undefined parameters)
        """
    def ItemValue(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns a Parameter as an Item. Returns a Null Handle if the Parameter is a Text, or if it is defined as Void
        """
    def Line(self,num : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a line given its rank in the list of recorded lines
        """
    def NbLines(self) -> int: 
        """
        Returns the count of recorded lines
        """
    def NbParams(self) -> int: 
        """
        During a Read operation, SessionFile processes sequencially the Items to read. For each one, it gives access to the list of its Parameters : they were defined by calls to SendVoid/SendParam/SendText during Writing the File. NbParams returns the count of Parameters for the line currently read.
        """
    def NewItem(self,ident : int,par : OCP.Standard.Standard_Transient) -> None: 
        """
        At beginning of writing an Item, writes its basics : - either its name in the session if it has one - or its relative number of item in the file, else (preceeded by a '_') - then, its Dynamic Type (in the sense of cdl : pk_class) This basic description can be followed by the parameters which are used in the definition of the item.
        """
    def ParamValue(self,num : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a Parameter (alphanumeric item of a line) as it has been read
        """
    def Read(self,filename : str) -> int: 
        """
        Performs a Read Operation from a file to a WorkSession i.e. calls ReadFile, then ReadSession and ReadEnd Returned Value is : 0 for OK, -1 File could not be opened, >0 Error during Read (see WriteSession) IsDone can be called too (will return True for OK)
        """
    def ReadEnd(self) -> int: 
        """
        Reads the end of a file (its last line). Returns 0 if OK, status >0 in case of error (not a suitable end line).
        """
    def ReadFile(self,name : str) -> bool: 
        """
        Reads the recorded lines from a file named <name>, after having cleared the list (stops if RecognizeFile fails) Returns False (with no clearing) if the file could not be read
        """
    def ReadLine(self) -> bool: 
        """
        Reads a Line and splits it into a set of alphanumeric items, which can then be queried by NbParams/ParamValue ...
        """
    def ReadOwn(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Tries to Read an Item, by calling the Library of Dumpers Sets the list of parameters of the line to be read from the first own one
        """
    def ReadSession(self) -> int: 
        """
        Performs a Read Operation from a File to a WorkSession, i.e. reads the list of line (which must have already been loaded, by ReadFile or by calls to AddLine) Important Remark : this excludes the reading of the last line, which is performed by ReadEnd Returns 0 for OK, >0 status for Read Error (not a suitable File, or WorkSession given as Immutable at Creation Time) IsDone can be called too (will return True for OK)
        """
    def RecognizeFile(self,headerline : str) -> bool: 
        """
        Recognizes the header line. returns True if OK, False else
        """
    def RemoveLastLine(self) -> None: 
        """
        Removes the last line. Can be called recursively. Does nothing if the list is empty
        """
    def SendItem(self,par : OCP.Standard.Standard_Transient) -> None: 
        """
        During a Write action, commands to send the identification of a Parameter : if it is Null (undefined) it is send as Void ($) if it is Named in the WorkSession, its Name is sent preceeded by ':', else a relative Ident Number is sent preceeded by '#' (relative to the present Write, i.e. starting at one, without skip, and counted part from Named Items)
        """
    def SendText(self,text : str) -> None: 
        """
        During a Write action, commands to send a Text without interpretation. It will be sent as well
        """
    def SendVoid(self) -> None: 
        """
        During a Write action, commands to send a Void Parameter i.e. a Parameter which is present but undefined Its form will be the dollar sign : $
        """
    def SetLastGeneral(self,lastgen : int) -> None: 
        """
        Sets the rank of Last General Parameter to a new value. It is followed by the Fist Own Parameter of the item. Used by SessionFile after reading general parameters.
        """
    def SetOwn(self,mode : bool) -> None: 
        """
        Sets Parameters to be sent as Own if <mode> is True (their Name or Number or Void Mark or Text Value is preceeded by a Column sign ':') else they are sent normally Hence, the Own Parameter are clearly identified in the File
        """
    def SplitLine(self,line : str) -> None: 
        """
        Internal routine which processes a line into words and prepares its exploration
        """
    def TextValue(self,num : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the content of a Text Parameter (without the quotes). Returns an empty string if the Parameter is not a Text.
        """
    def WorkSession(self) -> IFSelect_WorkSession: 
        """
        Returns the WorkSession on which a SessionFile works. Remark that it is returned as Immutable.
        """
    def Write(self,filename : str) -> int: 
        """
        Performs a Write Operation from a WorkSession to a File i.e. calls WriteSession then WriteEnd, and WriteFile Returned Value is : 0 for OK, -1 File could not be created, >0 Error during Write (see WriteSession) IsDone can be called too (will return True for OK)
        """
    def WriteEnd(self) -> int: 
        """
        Writes the trailing line. It is separate from WriteSession, in order to allow to redefine WriteSession without touching WriteEnd (WriteSession defines the body of the file) WriteEnd fills the list of lines. Returns a status of error, 0 if OK, >0 else
        """
    def WriteFile(self,name : str) -> bool: 
        """
        Writes the recorded lines to a file named <name> then clears the list of lines. Returns False (with no clearing) if the file could not be created
        """
    def WriteLine(self,line : str,follow : str='\x00') -> None: 
        """
        Writes a line to the File. If <follow> is given, it is added at the following of the line. '' must be added for the end.
        """
    def WriteOwn(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Writes the Parameters own to each type of Item. Uses the Library of SessionDumpers Returns True if Done, False if <item> could not be treated (hence it remains written with no Own Parameter)
        """
    def WriteSession(self) -> int: 
        """
        Prepares the Write operation from a WorkSession (IFSelect) to a File, i.e. fills the list of lines (the file itself remains to be written; or NbLines/Line may be called) Important Remark : this excludes the reading of the last line, which is performed by WriteEnd Returns 0 if OK, status > 0 in case of error
        """
    @overload
    def __init__(self,WS : IFSelect_WorkSession) -> None: ...
    @overload
    def __init__(self,WS : IFSelect_WorkSession,filename : str) -> None: ...
    pass
class IFSelect_SessionPilot(IFSelect_Activator, OCP.Standard.Standard_Transient):
    """
    A SessionPilot is intended to make easier the use of a WorkSession. It receives commands, under alphanumeric form, then calls a library of Activators to interprete and run them.A SessionPilot is intended to make easier the use of a WorkSession. It receives commands, under alphanumeric form, then calls a library of Activators to interprete and run them.A SessionPilot is intended to make easier the use of a WorkSession. It receives commands, under alphanumeric form, then calls a library of Activators to interprete and run them.
    """
    def Add(self,number : int,command : str) -> None: 
        """
        Allows a self-definition by an Activator of the Commands it processes, call the class method Adding (mode 0)
        """
    def AddSet(self,number : int,command : str) -> None: 
        """
        Same as Add but specifies that this command is candidate for xset (creation of items, xset : named items; mode 1)
        """
    @staticmethod
    def Adding_s(actor : IFSelect_Activator,number : int,command : str,mode : int) -> None: 
        """
        Records, in a Dictionary available for all the Activators, the command title an Activator can process, attached with its number, proper for this Activator <mode> allows to distinguish various execution modes 0: default mode; 1 : for xset
        """
    def Arg(self,num : int) -> str: 
        """
        Returns a word given its rank, as a CString. As for Word, begins at 0 (the command name), etc...
        """
    def Clear(self) -> None: 
        """
        Clears the recorded informations (commands, objects)
        """
    def Command(self,num : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a recorded Command, given its rank (from 1)
        """
    def CommandLine(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the Command Line to be interpreted
        """
    def CommandPart(self,numarg : int=0) -> str: 
        """
        Returns the part of the command line which begins at argument <numarg> between 0 and NbWords-1 (by default, all the line) Empty string if out of range
        """
    @staticmethod
    def Commands_s(mode : int=-1,command : str='') -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        Returns, for a root of command title, the list of possible commands. <mode> : -1 (D) for all commands if <commands> is empty -1 + command : about a Group , >= 0 see Adding By default, it returns the whole list of known commands.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Do(self,number : int,session : IFSelect_SessionPilot) -> IFSelect_ReturnStatus: 
        """
        Processes specific commands, which are : x or exit for end of session ? or help for help messages xcommand to control command lines (Record Mode, List, Clear, File Output ...) xsource to execute a command file (no nesting allowed), in case of error, source is stopped and keyword recovers xstep is a simple prefix (useful in a wider environment, to avoid conflicts on command names) xset control commands which create items with names
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Execute(self,command : OCP.TCollection.TCollection_AsciiString) -> IFSelect_ReturnStatus: 
        """
        Sets the Command then tries to execute it. Return value : same as for Perform
        """
    def ExecuteAlias(self,aliasname : OCP.TCollection.TCollection_AsciiString) -> IFSelect_ReturnStatus: 
        """
        Executes the Commands, except that the command name (word 0) is aliased. The rest of the command line is unchanged If <alias> is empty, Executes with no change
        """
    def ExecuteCounter(self,counter : IFSelect_SignCounter,numword : int,mode : IFSelect_PrintCount=IFSelect_PrintCount.IFSelect_CountByItem) -> IFSelect_ReturnStatus: 
        """
        Executes a Counter in a general way If <numword> is greater than count of command words, it counts all the model. Else it considers the word <numword> as the identifier of a Selection <mode> gives the mode of printing results, default is CountByItem
        """
    def File(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Group(self) -> str: 
        """
        None
        """
    def Help(self,number : int) -> str: 
        """
        Help for specific commands (apart from general command help)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Library(self) -> IFSelect_WorkLibrary: 
        """
        Returns the WorKlibrary (Null if not set). WorkLibrary is used to Read and Write Files, according to the Norm
        """
    @staticmethod
    def Mode_s(command : str) -> int: 
        """
        Returns mode recorded for a command. -1 if not found
        """
    def NbCommands(self) -> int: 
        """
        Returns the count of recorded Commands
        """
    def NbWords(self) -> int: 
        """
        Returns the count of words of the Command Line, separated by blanks : 0 if empty, one if a command without args, else it gives the count of args minus one. Warning : limited to 10 (command title + 9 args)
        """
    def Number(self,val : str) -> int: 
        """
        Interprets a string value as an entity number : if it gives an integer, returns its value else, considers it as ENtityLabel (preferably case sensitive) in case of failure, returns 0
        """
    def Perform(self) -> IFSelect_ReturnStatus: 
        """
        Executes the Command, itself (for built-in commands, which have priority) or by using the list of Activators. The value returned is : RetVoid if nothing done (void command) RetDone if execution OK, RetEnd if END OF SESSION, RetError if command unknown or incorrect, RetFail if error on execution If execution is OK and RecordMode is set, this Command Line is recorded to the list (see below).
        """
    def ReadScript(self,file : str='') -> IFSelect_ReturnStatus: 
        """
        Reads commands from a Script File, named <file>. By default (file = ""), reads from standard input with a prompt Else (reading from a file), the read commands are displayed onto standard output. Allows nested reads. Reading is stopped either by command x or exit, or by reaching end of file Return Value follows the rules of Do : RetEnd for normal end, RetFail if script could not be opened
        """
    def RecordItem(self,item : OCP.Standard.Standard_Transient) -> IFSelect_ReturnStatus: 
        """
        Allows to associate a Transient Value with the last execution as a partial result Returns RetDone if item is not Null, RetFail if item is Null Remark : it is nullified for each Perform
        """
    def RecordMode(self) -> bool: 
        """
        Returns the Record Mode for Commands. Default is False.
        """
    def RecordedItem(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Transient Object which was recorded with the current Line Command. If none was, returns a Null Handle
        """
    def RemoveWord(self,num : int) -> bool: 
        """
        Removes a word given its rank. Returns True if Done, False if <num> is out of range
        """
    @staticmethod
    def Remove_s(command : str) -> None: 
        """
        Removes a Command, if it is recorded (else, does nothing)
        """
    @staticmethod
    def Select_s(command : str,number : int,actor : IFSelect_Activator) -> bool: 
        """
        Selects, for a Command given by its title, an actor with its command number. Returns True if found, False else
        """
    def Session(self) -> IFSelect_WorkSession: 
        """
        Returns the WorkSession which is worked on
        """
    def SetCommandLine(self,command : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the value of the Command Line to be interpreted Also prepares the interpretation (splitting by blanks)
        """
    def SetForGroup(self,group : str,file : str='') -> None: 
        """
        Group and SetGroup define a "Group of commands" which correspond to an Activator. Default is "XSTEP" Also a file may be attached
        """
    def SetLibrary(self,WL : IFSelect_WorkLibrary) -> None: 
        """
        Sets a WorkLibrary
        """
    def SetRecordMode(self,mode : bool) -> None: 
        """
        Changes the RecordMode.
        """
    def SetSession(self,WS : IFSelect_WorkSession) -> None: 
        """
        Sets a WorkSession to be worked on
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Word(self,num : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a word given its rank in the Command Line. Begins at 0 which is the Command Title, 1 is the 1st arg., etc...
        """
    def __init__(self,prompt : str='') -> None: ...
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
class IFSelect_ShareOut(OCP.Standard.Standard_Transient):
    """
    This class gathers the informations required to produce one or several file(s) from the content of an InterfaceModel (passing through the creation of intermediate Models).This class gathers the informations required to produce one or several file(s) from the content of an InterfaceModel (passing through the creation of intermediate Models).This class gathers the informations required to produce one or several file(s) from the content of an InterfaceModel (passing through the creation of intermediate Models).
    """
    def AddDispatch(self,disp : IFSelect_Dispatch) -> None: 
        """
        Adds a Dispatch to the list
        """
    def AddModif(self,modifier : IFSelect_GeneralModifier,formodel : bool,atnum : int=0) -> None: 
        """
        Adds a Modifier to the list of Modifiers : Model Modifiers if <formodel> is True, File Modifiers else (internal).
        """
    @overload
    def AddModifier(self,modifier : IFSelect_GeneralModifier,atnum : int) -> None: 
        """
        Sets a Modifier to be applied on all Dispatches to be run If <modifier> is a ModelModifier, adds it to the list of Model Modifiers; else to the list of File Modifiers By default (atnum = 0) at the end of the list, else at <atnum> Each Modifier is used, after each copy of a packet of Entities into a Model : its criteria are checked and if they are OK, the method Perform of this Modifier is run.

        Sets a Modifier to be applied on the Dispatch <dispnum> If <modifier> is a ModelModifier, adds it to the list of Model Modifiers; else to the list of File Modifiers This is the same list as for all Dispatches, but the Modifier is qualified to be applied to one Dispatch only Then, <atnum> refers to the entire list By default (atnum = 0) at the end of the list, else at <atnum> Remark : if the Modifier was already in the list and if <atnum> = 0, the Modifier is not moved, but only qualified for a Dispatch
        """
    @overload
    def AddModifier(self,modifier : IFSelect_GeneralModifier,dispnum : int,atnum : int) -> None: ...
    def ChangeModifierRank(self,formodel : bool,befor : int,after : int) -> bool: 
        """
        Changes the rank of a modifier in the list : Model Modifiers if <formodel> is True, File Modifiers else from <before> to <after> Returns True if done, False else (before or after out of range)
        """
    def Clear(self,onlydisp : bool) -> None: 
        """
        Removes in one operation all the Dispatches with their Idents Also clears all informations about Names, and all Results but naming informations which are : - kept if <onlydisp> is True. - cleared if <onlydisp> is False (complete clearing) If <onlydisp> is True, that's all. Else, clears also Modifiers
        """
    def ClearResult(self,alsoname : bool) -> None: 
        """
        Clears all data produced (apart from Dispatches, etc...) if <alsoname> is True, all is cleared. Else, informations about produced Names are kept (to maintain unicity of naming across clearings)
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultRootName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Default Root Name. Can be empty.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self,num : int) -> IFSelect_Dispatch: 
        """
        Returns a Dispatch, given its rank in the list
        """
    def DispatchRank(self,disp : IFSelect_Dispatch) -> int: 
        """
        Returns the Rank of a Dispatch, given its Value (Handle). Returns 0 if the Dispatch is unknown in the ShareOut
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Extension(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the general Extension. Can be empty (not recommanded)
        """
    def FileName(self,dnum : int,pnum : int,nbpack : int=0) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Computes the complete file name for a Packet of a Dispatch, given Dispatch Number (Rank), Packet Number, and Count of Packets generated by this Dispatch (0 if unknown)
        """
    def GeneralModifier(self,formodel : bool,num : int) -> IFSelect_GeneralModifier: 
        """
        Returns a Modifier of the list, given its rank : Model Modifiers if <formodel> is True, File Modifiers else
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasRootName(self,num : int) -> bool: 
        """
        Returns True if the Dispatch of rank <num> has an attached Root Name. False else, or if num is out of range
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def LastRun(self) -> int: 
        """
        Returns the rank of last run item (ClearResult resets it to 0)
        """
    def ModelModifier(self,num : int) -> IFSelect_Modifier: 
        """
        Returns a Modifier of the list of Model Modifiers, duely casted
        """
    def ModifierRank(self,modifier : IFSelect_GeneralModifier) -> int: 
        """
        Gives the rank of a Modifier in the list, 0 if not in the list Model Modifiers if <modifier> is kind of ModelModifer, File Modifiers else
        """
    def NbDispatches(self) -> int: 
        """
        Returns the count of Dispatches
        """
    def NbModifiers(self,formodel : bool) -> int: 
        """
        Returns count of Modifiers (which apply to complete Models) : Model Modifiers if <formodel> is True, File Modifiers else
        """
    def Prefix(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the general Prefix. Can be empty.
        """
    def RemoveDispatch(self,rank : int) -> bool: 
        """
        Removes a Dispatch, given its rank in the list Returns True if done, False if rank is not between (LastRun + 1) and (NbDispatches)
        """
    def RemoveItem(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Removes an item, which can be, either a Dispatch (removed from the list of Dispatches), or a GeneralModifier (removed from the list of Model Modifiers or from the list of File Modifiers according to its type). Returns True if done, False if has not been found or if it is neither a Dispatch, nor a Modifier.
        """
    def RemoveModifier(self,formodel : bool,num : int) -> bool: 
        """
        Removes a Modifier, given it rank in the list : Model Modifiers if <formodel> is True, File Modifiers else Returns True if done, False if <num> is out of range
        """
    def RootName(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Root bound to a Dispatch, given its rank Returns a Null Handle if not defined
        """
    def RootNumber(self,name : OCP.TCollection.TCollection_HAsciiString) -> int: 
        """
        Returns an integer value about a given root name : - positive : it's the rank of the Dispatch which has this name - null : this root name is unknown - negative (-1) : this root name is the default root name
        """
    def SetDefaultRootName(self,defrt : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        Defines or Changes the Default Root Name to a new value (which is used for dispatches which have no attached root name). If this method is not called, DefaultRootName remains empty Returns True if OK, False if this Name is already attached, for a Dispatch or for Default
        """
    def SetExtension(self,ext : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Defines or Changes the general Extension (which is appended to complete file name generated). If this method is not call, Extension remains empty
        """
    def SetLastRun(self,last : int) -> None: 
        """
        Records a new alue for the rank of last run item
        """
    def SetPrefix(self,pref : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Defines or Changes the general Prefix (which is prepended to complete file name generated). If this method is not call, Prefix remains empty
        """
    def SetRootName(self,num : int,name : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        Attaches a Root Name to a Dispatch given its rank, as an HAsciiString (standard form). A Null Handle resets this name. Returns True if OK, False if this Name is already attached, for a Dispatch or for Default, or <num> out of range
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
class IFSelect_ShareOutResult():
    """
    This class gives results computed from a ShareOut : simulation before transfer, helps to list entities ... Transfer itself will later be performed, either by a TransferCopy to simply divide up a file, or a TransferDispatch which can be parametred with more details
    """
    def Dispatch(self) -> IFSelect_Dispatch: 
        """
        Returns the current Dispatch
        """
    def DispatchRank(self) -> int: 
        """
        Returns the Rank of the current Dispatch in the ShareOut Returns Zero if there is none (iteration finished)
        """
    def Evaluate(self) -> None: 
        """
        Evaluates the result of a ShareOut : determines Entities to be forgotten by the ShareOut, Entities to be transferred several times (duplicated), prepares an iteration on the packets to be produced Called the first time anyone question is asked, or after a call to Reset. Works by calling the method Prepare.
        """
    def FileName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the File Name which corresponds to current Packet (computed by ShareOut) If current Packet has no associated name (see ShareOut), the returned value is Null
        """
    def Graph(self) -> OCP.Interface.Interface_Graph: 
        """
        Returns the Graph used to create theShareOutResult
        """
    def More(self) -> bool: 
        """
        Returns True if there is more packets in the current Dispatch, else if there is more Dispatch in the ShareOut
        """
    def NbPackets(self) -> int: 
        """
        Returns the total count of produced non empty packets (in out : calls Evaluate as necessary)
        """
    def Next(self) -> None: 
        """
        Passes to the next Packet in the current Dispatch, or if there is none, to the next Dispatch in the ShareOut
        """
    def NextDispatch(self) -> None: 
        """
        Passes to the next Dispatch, regardless about remaining packets
        """
    def PacketContent(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the complete content of the current Packet (i.e. with shared entities, which will also be put in the file)
        """
    def PacketRoot(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of Roots of the current Packet (never empty) (i.e. the Entities to be themselves asked for transfer) Error if there is none (iteration finished)
        """
    def Packets(self,complete : bool=True) -> IFSelect_PacketList: 
        """
        Returns the list of recorded Packets, under two modes : - <complete> = False, the strict definition of Packets, i.e. for each one, the Root Entities, to be explicitely sent - <complete> = True (Default), the completely evaluated list, i.e. which really gives the destination of each entity : this mode allows to evaluate duplications Remark that to send packets, iteration remains preferable (file names are managed)
        """
    def PacketsInDispatch(self) -> Tuple[int, int]: 
        """
        Returns Number (rank) of current Packet in current Dispatch, and total count of Packets in current Dispatch, as arguments
        """
    def Prepare(self) -> None: 
        """
        Prepares the iteration on the packets This method is called by Evaluate, but can be called anytime The iteration consists in taking each Dispatch of the ShareOut beginning by the first one, compute its packets, then iterate on these packets. Once all these packets are iterated, the iteration passes to the next Dispatch, or stops. For a creation from a unique Dispatch, same but with only this Dispatch. Each packet can be listed, or really transferred (producing a derived Model, from which a file can be generated)
        """
    def Reset(self) -> None: 
        """
        Erases computed data, in order to command a new Evaluation
        """
    def ShareOut(self) -> IFSelect_ShareOut: 
        """
        Returns the ShareOut used to create the ShareOutResult if creation from a Dispatch, returns a Null Handle
        """
    @overload
    def __init__(self,disp : IFSelect_Dispatch,mod : OCP.Interface.Interface_InterfaceModel) -> None: ...
    @overload
    def __init__(self,sho : IFSelect_ShareOut,mod : OCP.Interface.Interface_InterfaceModel) -> None: ...
    @overload
    def __init__(self,disp : IFSelect_Dispatch,G : OCP.Interface.Interface_Graph) -> None: ...
    @overload
    def __init__(self,sho : IFSelect_ShareOut,G : OCP.Interface.Interface_Graph) -> None: ...
    pass
class IFSelect_Signature(OCP.Interface.Interface_SignType):
    """
    Signature provides the basic service used by the classes SelectSignature and Counter (i.e. Name, Value), which is : - for an entity in a model, give a characteristic string, its signature This string has not to be unique in the model, but gives a value for such or such important feature. Exemples : Dynamic Type; Category; etcSignature provides the basic service used by the classes SelectSignature and Counter (i.e. Name, Value), which is : - for an entity in a model, give a characteristic string, its signature This string has not to be unique in the model, but gives a value for such or such important feature. Exemples : Dynamic Type; Category; etcSignature provides the basic service used by the classes SelectSignature and Counter (i.e. Name, Value), which is : - for an entity in a model, give a characteristic string, its signature This string has not to be unique in the model, but gives a value for such or such important feature. Exemples : Dynamic Type; Category; etc
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
    def SetIntCase(self,hasmin : bool,valmin : int,hasmax : bool,valmax : int) -> None: 
        """
        Sets the information data to tell "integer cases" with possible min and max values To be called when creating
        """
    def Text(self,ent : OCP.Standard.Standard_Transient,context : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an identification of the Signature (a word), given at initialization time Specialised to consider context as an InterfaceModel
        """
    def Value(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> str: 
        """
        Returns the Signature for a Transient object. It is specific of each sub-class of Signature. For a Null Handle, it should provide "" It can work with the model which contains the entity
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
class IFSelect_SignCategory(IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    This Signature returns the Category of an entity, as recorded in the modelThis Signature returns the Category of an entity, as recorded in the modelThis Signature returns the Category of an entity, as recorded in the model
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
    def SetIntCase(self,hasmin : bool,valmin : int,hasmax : bool,valmax : int) -> None: 
        """
        Sets the information data to tell "integer cases" with possible min and max values To be called when creating
        """
    def Text(self,ent : OCP.Standard.Standard_Transient,context : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an identification of the Signature (a word), given at initialization time Specialised to consider context as an InterfaceModel
        """
    def Value(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> str: 
        """
        Returns the Signature for a Transient object, as its Category recorded in the model
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
class IFSelect_GraphCounter(IFSelect_SignCounter, IFSelect_SignatureList, OCP.Standard.Standard_Transient):
    """
    A GraphCounter computes values to be sorted with the help of a Graph. I.E. not from a SignatureA GraphCounter computes values to be sorted with the help of a Graph. I.E. not from a SignatureA GraphCounter computes values to be sorted with the help of a Graph. I.E. not from a Signature
    """
    def Add(self,ent : OCP.Standard.Standard_Transient,sign : str) -> None: 
        """
        Adds an entity with its signature, i.e. : - counts an item more for <sign> - if record-list status is set, records the entity Accepts a null entity (the signature is then for the global model). But if the string is empty, counts a Null item.
        """
    def AddEntity(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Adds an entity by considering its signature, which is given by call to method AddSign Returns True if added, False if already in the map (and map control status set)
        """
    def AddFromSelection(self,sel : IFSelect_Selection,G : OCP.Interface.Interface_Graph) -> None: 
        """
        Adds the result determined by a Selection from a Graph Remark : does not impact at all data from SetSelection & Co
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Adds a list of entities by adding each of the items
        """
    def AddModel(self,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Adds all the entities contained in a Model
        """
    def AddSign(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Adds an entity (already filtered by Map) with its signature. This signature can be computed with the containing model. Its value is provided by the object Signature given at start, if no Signature is defined, it does nothing.
        """
    def AddWithGraph(self,list : OCP.TColStd.TColStd_HSequenceOfTransient,graph : OCP.Interface.Interface_Graph) -> None: 
        """
        Adds a list of entities in the context given by the graph Default takes the count of entities selected by the applied selection, when it is given each entity of the list Can be redefined
        """
    def Applied(self) -> IFSelect_SelectDeduct: 
        """
        Returns the applied selection
        """
    def Clear(self) -> None: 
        """
        None
        """
    def ComputeSelected(self,G : OCP.Interface.Interface_Graph,forced : bool=False) -> bool: 
        """
        Computes from the selection result, if selection is active (mode 2). If selection is not defined (mode 0) or is inhibited (mode 1) does nothing. Returns True if computation is done (or optimised), False else This method is called by ComputeCounter from WorkSession
        """
    def ComputedSign(self,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph) -> str: 
        """
        Applies AddWithGraph on one entity, and returns the Signature Value which has been recorded To do this, Add is called with SignOnly Mode True during the call, the returned value is LastValue
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
    def Entities(self,sign : str) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities attached to a signature It is empty if <sign> has not been recorded It is a Null Handle if the list of entities is not known
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasEntities(self) -> bool: 
        """
        Returns True if the list of Entities is aknowledged, else the method Entities will always return a Null Handle
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,name : str,count : Any,list : Any,nbnuls : int) -> None: 
        """
        Aknowledges the list in once. Name identifies the Signature
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def LastValue(self) -> str: 
        """
        Returns the last value recorded by Add (only if SignMode set) Cleared by Clear or Init
        """
    def List(self,root : str='') -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of signatures, as a sequence of strings (but without their respective counts). It is ordered. By default, for all the signatures. If <root> is given non empty, for the signatures which begin by <root>
        """
    def Name(self) -> str: 
        """
        Returns the recorded Name. Remark : default is "..." (no SetName called)
        """
    def NbNulls(self) -> int: 
        """
        Returns the count of null entities
        """
    def NbTimes(self,sign : str) -> int: 
        """
        Returns the number of times a signature was counted, 0 if it has not been recorded at all
        """
    def PrintCount(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints the counts of items (not the list)
        """
    def PrintList(self,S : OCP.Message.Message_Messenger,model : OCP.Interface.Interface_InterfaceModel,mod : IFSelect_PrintCount=IFSelect_PrintCount.IFSelect_ListByItem) -> None: 
        """
        Prints the lists of items, if they are present (else, prints a message "no list available") Uses <model> to determine for each entity to be listed, its number, and its specific identifier (by PrintLabel) <mod> gives a mode for printing : - CountByItem : just count (as PrintCount) - ShortByItem : minimum i.e. count plus 5 first entity numbers - ShortByItem(D) complete list of entity numbers (0: "Global") - EntitiesByItem : list of (entity number/PrintLabel from the model) other modes are ignored
        """
    def PrintSum(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints a summary Item which has the greatest count of entities For items which are numeric values : their count, maximum, minimum values, cumul, average
        """
    def SelMode(self) -> int: 
        """
        Returns the mode of working with the selection
        """
    def Selection(self) -> IFSelect_Selection: 
        """
        Returns the selection, or a null Handle
        """
    def SetApplied(self,sel : IFSelect_SelectDeduct) -> None: 
        """
        Sets a new applied selection
        """
    def SetList(self,withlist : bool) -> None: 
        """
        Changes the record-list status. The list is not cleared but its use changes
        """
    def SetMap(self,withmap : bool) -> None: 
        """
        Changes the control status. The map is not cleared, simply its use changes
        """
    def SetName(self,name : str) -> None: 
        """
        Defines a name for a SignatureList (used to print it)
        """
    def SetSelMode(self,selmode : int) -> None: 
        """
        Changes the mode of working with the selection : -1 just clears optimisation data and nothing else 0 clears it 1 inhibits it for computing (but no clearing) 2 sets it active for computing Default at creation is 0, after SetSelection (not null) is 2
        """
    def SetSelection(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection as input : this causes content to be cleared then the Selection to be ready to compute (but not immediatly)
        """
    def Sign(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Determines and returns the value of the signature for an entity as an HAsciiString. This method works exactly as AddSign, which is optimized
        """
    def Signature(self) -> IFSelect_Signature: 
        """
        Returns the Signature used to count entities. It can be null.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,withmap : bool=True,withlist : bool=False) -> None: ...
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
    def ModeSignOnly(self) -> bool:
        """
        :type: bool
        """
    @ModeSignOnly.setter
    def ModeSignOnly(self, arg1: bool) -> None:
        pass
    pass
class IFSelect_SignMultiple(IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    Multiple Signature : ordered list of other Signatures It concatenates on a same line the result of its sub-items separated by sets of 3 blanks It is possible to define tabulations between sub-items Moreover, match rules are specificMultiple Signature : ordered list of other Signatures It concatenates on a same line the result of its sub-items separated by sets of 3 blanks It is possible to define tabulations between sub-items Moreover, match rules are specificMultiple Signature : ordered list of other Signatures It concatenates on a same line the result of its sub-items separated by sets of 3 blanks It is possible to define tabulations between sub-items Moreover, match rules are specific
    """
    def Add(self,subsign : IFSelect_Signature,width : int=0,maxi : bool=False) -> None: 
        """
        Adds a Signature. Width, if given, gives the tabulation If <maxi> is True, it is a forced tabulation (overlength is replaced by a final dot) If <maxi> is False, just 3 blanks follow an overlength
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
    @staticmethod
    def MatchValue_s(val : str,text : OCP.TCollection.TCollection_AsciiString,exact : bool) -> bool: 
        """
        Default procedure to tell if a value <val> matches a text with a criterium <exact>. <exact> = True requires equality, else only contained (no reg-exp)
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel,text : OCP.TCollection.TCollection_AsciiString,exact : bool) -> bool: 
        """
        Specialized Match Rule If <exact> is False, simply checks if at least one sub-item matches If <exact> is True, standard match with Value (i.e. tabulations must be respected)
        """
    def Name(self) -> str: 
        """
        Returns an identification of the Signature (a word), given at initialization time Returns the Signature for a Transient object. It is specific of each sub-class of Signature. For a Null Handle, it should provide "" It can work with the model which contains the entity
        """
    def SetIntCase(self,hasmin : bool,valmin : int,hasmax : bool,valmax : int) -> None: 
        """
        Sets the information data to tell "integer cases" with possible min and max values To be called when creating
        """
    def Text(self,ent : OCP.Standard.Standard_Transient,context : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an identification of the Signature (a word), given at initialization time Specialised to consider context as an InterfaceModel
        """
    def Value(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> str: 
        """
        Concatenates the values of sub-signatures, with their tabulations
        """
    def __init__(self,name : str) -> None: ...
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
class IFSelect_SignType(IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    This Signature returns the cdl Type of an entity, under two forms : - complete dynamic type (package and class) - class type, without package nameThis Signature returns the cdl Type of an entity, under two forms : - complete dynamic type (package and class) - class type, without package nameThis Signature returns the cdl Type of an entity, under two forms : - complete dynamic type (package and class) - class type, without package name
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
    def SetIntCase(self,hasmin : bool,valmin : int,hasmax : bool,valmax : int) -> None: 
        """
        Sets the information data to tell "integer cases" with possible min and max values To be called when creating
        """
    def Text(self,ent : OCP.Standard.Standard_Transient,context : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an identification of the Signature (a word), given at initialization time Specialised to consider context as an InterfaceModel
        """
    def Value(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> str: 
        """
        Returns the Signature for a Transient object, as its Dynamic Type, with or without package name, according starting option
        """
    def __init__(self,nopk : bool=False) -> None: ...
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
class IFSelect_SignValidity(IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    This Signature returns the Validity Status of an entity, as deducted from data in the model : it can be "OK" "Unknown" "Unloaded" "Syntactic Fail"(but loaded) "Syntactic Warning" "Semantic Fail" "Semantic Warning"This Signature returns the Validity Status of an entity, as deducted from data in the model : it can be "OK" "Unknown" "Unloaded" "Syntactic Fail"(but loaded) "Syntactic Warning" "Semantic Fail" "Semantic Warning"This Signature returns the Validity Status of an entity, as deducted from data in the model : it can be "OK" "Unknown" "Unloaded" "Syntactic Fail"(but loaded) "Syntactic Warning" "Semantic Fail" "Semantic Warning"
    """
    def AddCase(self,acase : str) -> None: 
        """
        Adds a possible case To be called when creating, IF the list of possible cases for Value is known when starting For instance, for CDL types, rather do not fill this, but for a specific enumeration (such as a status), can be used
        """
    @staticmethod
    def CVal_s(ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> str: 
        """
        Returns the Signature for a Transient object, as a validity deducted from data (reports) stored in the model. Class method, can be called by any one
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
    def SetIntCase(self,hasmin : bool,valmin : int,hasmax : bool,valmax : int) -> None: 
        """
        Sets the information data to tell "integer cases" with possible min and max values To be called when creating
        """
    def Text(self,ent : OCP.Standard.Standard_Transient,context : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an identification of the Signature (a word), given at initialization time Specialised to consider context as an InterfaceModel
        """
    def Value(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> str: 
        """
        Returns the Signature for a Transient object, as a validity deducted from data (reports) stored in the model Calls the class method CVal
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
class IFSelect_SignAncestor(IFSelect_SignType, IFSelect_Signature, OCP.Interface.Interface_SignType):
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
    @staticmethod
    def MatchValue_s(val : str,text : OCP.TCollection.TCollection_AsciiString,exact : bool) -> bool: 
        """
        Default procedure to tell if a value <val> matches a text with a criterium <exact>. <exact> = True requires equality, else only contained (no reg-exp)
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel,text : OCP.TCollection.TCollection_AsciiString,exact : bool) -> bool: 
        """
        None
        """
    def Name(self) -> str: 
        """
        Returns an identification of the Signature (a word), given at initialization time Returns the Signature for a Transient object. It is specific of each sub-class of Signature. For a Null Handle, it should provide "" It can work with the model which contains the entity
        """
    def SetIntCase(self,hasmin : bool,valmin : int,hasmax : bool,valmax : int) -> None: 
        """
        Sets the information data to tell "integer cases" with possible min and max values To be called when creating
        """
    def Text(self,ent : OCP.Standard.Standard_Transient,context : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an identification of the Signature (a word), given at initialization time Specialised to consider context as an InterfaceModel
        """
    def Value(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> str: 
        """
        Returns the Signature for a Transient object, as its Dynamic Type, with or without package name, according starting option
        """
    def __init__(self,nopk : bool=False) -> None: ...
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
class IFSelect_CheckCounter(IFSelect_SignatureList, OCP.Standard.Standard_Transient):
    """
    A CheckCounter allows to see a CheckList (i.e. CheckIterator) not per entity, its messages, but per message, the entities attached (count and list). Because many messages can be repeated if they are due to systematic errorsA CheckCounter allows to see a CheckList (i.e. CheckIterator) not per entity, its messages, but per message, the entities attached (count and list). Because many messages can be repeated if they are due to systematic errorsA CheckCounter allows to see a CheckList (i.e. CheckIterator) not per entity, its messages, but per message, the entities attached (count and list). Because many messages can be repeated if they are due to systematic errors
    """
    def Add(self,ent : OCP.Standard.Standard_Transient,sign : str) -> None: 
        """
        Adds an entity with its signature, i.e. : - counts an item more for <sign> - if record-list status is set, records the entity Accepts a null entity (the signature is then for the global model). But if the string is empty, counts a Null item.
        """
    def Analyse(self,list : OCP.Interface.Interface_CheckIterator,model : OCP.Interface.Interface_InterfaceModel,original : bool=False,failsonly : bool=False) -> None: 
        """
        Analyses a CheckIterator according a Model (which detains the entities for which the CheckIterator has messages), i.e. counts messages for entities If <original> is True, does not consider final messages but those before interpretation (such as inserting variables : integers, reals, strings) If <failsonly> is True, only Fails are considered Remark : global messages are recorded with a Null entity
        """
    def Clear(self) -> None: 
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
    def Entities(self,sign : str) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities attached to a signature It is empty if <sign> has not been recorded It is a Null Handle if the list of entities is not known
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasEntities(self) -> bool: 
        """
        Returns True if the list of Entities is aknowledged, else the method Entities will always return a Null Handle
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,name : str,count : Any,list : Any,nbnuls : int) -> None: 
        """
        Aknowledges the list in once. Name identifies the Signature
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def LastValue(self) -> str: 
        """
        Returns the last value recorded by Add (only if SignMode set) Cleared by Clear or Init
        """
    def List(self,root : str='') -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of signatures, as a sequence of strings (but without their respective counts). It is ordered. By default, for all the signatures. If <root> is given non empty, for the signatures which begin by <root>
        """
    def Name(self) -> str: 
        """
        Returns the recorded Name. Remark : default is "..." (no SetName called)
        """
    def NbNulls(self) -> int: 
        """
        Returns the count of null entities
        """
    def NbTimes(self,sign : str) -> int: 
        """
        Returns the number of times a signature was counted, 0 if it has not been recorded at all
        """
    def PrintCount(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints the counts of items (not the list)
        """
    def PrintList(self,S : OCP.Message.Message_Messenger,model : OCP.Interface.Interface_InterfaceModel,mod : IFSelect_PrintCount=IFSelect_PrintCount.IFSelect_ListByItem) -> None: 
        """
        Prints the lists of items, if they are present (else, prints a message "no list available") Uses <model> to determine for each entity to be listed, its number, and its specific identifier (by PrintLabel) <mod> gives a mode for printing : - CountByItem : just count (as PrintCount) - ShortByItem : minimum i.e. count plus 5 first entity numbers - ShortByItem(D) complete list of entity numbers (0: "Global") - EntitiesByItem : list of (entity number/PrintLabel from the model) other modes are ignored
        """
    def PrintSum(self,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints a summary Item which has the greatest count of entities For items which are numeric values : their count, maximum, minimum values, cumul, average
        """
    def SetList(self,withlist : bool) -> None: 
        """
        Changes the record-list status. The list is not cleared but its use changes
        """
    def SetName(self,name : str) -> None: 
        """
        Defines a name for a SignatureList (used to print it)
        """
    def SetSignature(self,sign : MoniTool_SignText) -> None: 
        """
        Sets a specific signature Else, the current SignType (in the model) is used
        """
    def Signature(self) -> MoniTool_SignText: 
        """
        Returns the Signature;
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,withlist : bool=False) -> None: ...
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
    def ModeSignOnly(self) -> bool:
        """
        :type: bool
        """
    @ModeSignOnly.setter
    def ModeSignOnly(self, arg1: bool) -> None:
        pass
    pass
class IFSelect_TSeqOfDispatch(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IFSelect_Dispatch) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IFSelect_TSeqOfDispatch) -> None: ...
    def Assign(self,theOther : IFSelect_TSeqOfDispatch) -> IFSelect_TSeqOfDispatch: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IFSelect_Dispatch: 
        """
        First item access
        """
    def ChangeLast(self) -> IFSelect_Dispatch: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IFSelect_Dispatch: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> IFSelect_Dispatch: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IFSelect_TSeqOfDispatch) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IFSelect_Dispatch) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IFSelect_Dispatch) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IFSelect_TSeqOfDispatch) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IFSelect_Dispatch: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : IFSelect_Dispatch) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : IFSelect_TSeqOfDispatch) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : IFSelect_Dispatch) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IFSelect_TSeqOfDispatch) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IFSelect_Dispatch: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : IFSelect_TSeqOfDispatch) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IFSelect_HSeqOfSelection(IFSelect_TSeqOfSelection, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : IFSelect_TSeqOfSelection) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : IFSelect_Selection) -> None: ...
    def Assign(self,theOther : IFSelect_TSeqOfSelection) -> IFSelect_TSeqOfSelection: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IFSelect_Selection: 
        """
        First item access
        """
    def ChangeLast(self) -> IFSelect_Selection: 
        """
        Last item access
        """
    def ChangeSequence(self) -> IFSelect_TSeqOfSelection: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> IFSelect_Selection: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
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
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> IFSelect_Selection: 
        """
        First item access
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
    def InsertAfter(self,theIndex : int,theSeq : IFSelect_TSeqOfSelection) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IFSelect_Selection) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IFSelect_Selection) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IFSelect_TSeqOfSelection) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> IFSelect_Selection: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theSeq : IFSelect_TSeqOfSelection) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IFSelect_Selection) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def Sequence(self) -> IFSelect_TSeqOfSelection: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : IFSelect_Selection) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IFSelect_TSeqOfSelection) -> None: 
        """
        Split in two sequences
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IFSelect_Selection: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : IFSelect_TSeqOfSelection) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
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
class IFSelect_Transformer(OCP.Standard.Standard_Transient):
    """
    A Transformer defines the way an InterfaceModel is transformed (without sending it to a file). In order to work, each type of Transformer defines it method Perform, it can be parametred as needed.A Transformer defines the way an InterfaceModel is transformed (without sending it to a file). In order to work, each type of Transformer defines it method Perform, it can be parametred as needed.A Transformer defines the way an InterfaceModel is transformed (without sending it to a file). In order to work, each type of Transformer defines it method Perform, it can be parametred as needed.
    """
    def ChangeProtocol(self,newproto : OCP.Interface.Interface_Protocol) -> bool: 
        """
        This methods allows to declare that the Protocol applied to the new Model has changed. It applies to the last call to Perform.
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
        Returns a text which defines the way a Transformer works (to identify the transformation it performs)
        """
    def Perform(self,G : OCP.Interface.Interface_Graph,protocol : OCP.Interface.Interface_Protocol,checks : OCP.Interface.Interface_CheckIterator,newmod : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Performs a Transformation (defined by each sub-class) : <G> gives the input data (especially the starting model) and can be used for queries (by Selections, etc...) <protocol> allows to work with General Services as necessary (it applies to input data) If the change corresponds to a conversion to a new protocol, see also the method ChangeProtocol <checks> stores produced checks messages if any <newmod> gives the result of the transformation : - if it is Null (i.e. has not been affected), the transformation has been made on the spot, it is assumed to cause no change to the graph of dependances - if it equates the starting Model, it has been transformed on the spot (possibiliy some entities were replaced inside it) - if it is new, it corresponds to a new data set which replaces the starting one
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Updated(self,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient) -> bool: 
        """
        This method allows to know what happened to a starting entity after the last Perform. If <entfrom> (from starting model) has one and only one known item which corresponds in the new produced model, this method must return True and fill the argument <entto>. Else, it returns False.
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
class IFSelect_TransformStandard(IFSelect_Transformer, OCP.Standard.Standard_Transient):
    """
    This class runs transformations made by Modifiers, as the ModelCopier does when it produces files (the same set of Modifiers can then be used, as to transform the starting Model, as at file sending time).This class runs transformations made by Modifiers, as the ModelCopier does when it produces files (the same set of Modifiers can then be used, as to transform the starting Model, as at file sending time).This class runs transformations made by Modifiers, as the ModelCopier does when it produces files (the same set of Modifiers can then be used, as to transform the starting Model, as at file sending time).
    """
    def AddModifier(self,modif : IFSelect_Modifier,atnum : int=0) -> bool: 
        """
        Adds a Modifier to the list : - <atnum> = 0 (default) : at the end of the list - <atnum> > 0 : at rank <atnum> Returns True if done, False if <atnum> is out of range
        """
    def ApplyModifiers(self,G : OCP.Interface.Interface_Graph,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool,checks : OCP.Interface.Interface_CheckIterator,newmod : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Applies the modifiers sequencially. For each one, prepares required data (if a Selection is associated as a filter). For the option OnTheSpot, it determines if the graph may be changed and updates <newmod> if required If a Modifier causes an error (check "HasFailed"), ApplyModifier stops : the following Modifiers are ignored
        """
    def ChangeProtocol(self,newproto : OCP.Interface.Interface_Protocol) -> bool: 
        """
        This methods allows to declare that the Protocol applied to the new Model has changed. It applies to the last call to Perform.
        """
    def Copy(self,G : OCP.Interface.Interface_Graph,TC : OCP.Interface.Interface_CopyTool,newmod : OCP.Interface.Interface_InterfaceModel) -> Any: 
        """
        This the first operation. It calls StandardCopy or OnTheSpot according the option
        """
    def CopyOption(self) -> bool: 
        """
        Returns the Copy option
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
        Returns a text which defines the way a Transformer works : "On the spot edition" or "Standard Copy" followed by "<nn> Modifiers"
        """
    def Modifier(self,num : int) -> IFSelect_Modifier: 
        """
        Returns a Modifier given its rank in the list
        """
    def ModifierRank(self,modif : IFSelect_Modifier) -> int: 
        """
        Returns the rank of a Modifier in the list, 0 if unknown
        """
    def NbModifiers(self) -> int: 
        """
        Returns the count of recorded Modifiers
        """
    def OnTheSpot(self,G : OCP.Interface.Interface_Graph,TC : OCP.Interface.Interface_CopyTool,newmod : OCP.Interface.Interface_InterfaceModel) -> Any: 
        """
        This is the OnTheSpot action : each entity is bound with ... itself. The produced model is the same as the starting one.
        """
    def Perform(self,G : OCP.Interface.Interface_Graph,protocol : OCP.Interface.Interface_Protocol,checks : OCP.Interface.Interface_CheckIterator,newmod : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Performs the Standard Transformation, by calling Copy then ApplyModifiers (which can return an error status)
        """
    @overload
    def RemoveModifier(self,num : int) -> bool: 
        """
        Removes a Modifier from the list Returns True if done, False if <modif> not in the list

        Removes a Modifier from the list, given its rank Returns True if done, False if <num> is out of range
        """
    @overload
    def RemoveModifier(self,modif : IFSelect_Modifier) -> bool: ...
    def Selection(self) -> IFSelect_Selection: 
        """
        Returns the Selection, Null by default
        """
    def SetCopyOption(self,option : bool) -> None: 
        """
        Sets the Copy option to a new value : - True for StandardCopy - False for OnTheSpot
        """
    def SetSelection(self,sel : IFSelect_Selection) -> None: 
        """
        Sets a Selection (or unsets if Null) This Selection then defines the list of entities on which the Modifiers will be applied If it is set, it has priority on Selections of Modifiers Else, for each Modifier its Selection is evaluated By default, all the Model is taken
        """
    def StandardCopy(self,G : OCP.Interface.Interface_Graph,TC : OCP.Interface.Interface_CopyTool,newmod : OCP.Interface.Interface_InterfaceModel) -> Any: 
        """
        This is the standard action of Copy : its takes into account only the remaining entities (noted by Graph Status positive) and their proper dependances of course. Produces a new model.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Updated(self,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient) -> bool: 
        """
        This methods allows to know what happened to a starting entity after the last Perform. It reads result from the map which was filled by Perform.
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
class IFSelect_WorkLibrary(OCP.Standard.Standard_Transient):
    """
    This class defines the (empty) frame which can be used to enrich a XSTEP set with new capabilities In particular, a specific WorkLibrary must give the way for Reading a File into a Model, and Writing a Model to a File Thus, it is possible to define several Work Libraries for each norm, but recommanded to define one general class for each one : this general class will define the Read and Write methods.This class defines the (empty) frame which can be used to enrich a XSTEP set with new capabilities In particular, a specific WorkLibrary must give the way for Reading a File into a Model, and Writing a Model to a File Thus, it is possible to define several Work Libraries for each norm, but recommanded to define one general class for each one : this general class will define the Read and Write methods.This class defines the (empty) frame which can be used to enrich a XSTEP set with new capabilities In particular, a specific WorkLibrary must give the way for Reading a File into a Model, and Writing a Model to a File Thus, it is possible to define several Work Libraries for each norm, but recommanded to define one general class for each one : this general class will define the Read and Write methods.
    """
    def CopyModel(self,original : OCP.Interface.Interface_InterfaceModel,newmodel : OCP.Interface.Interface_InterfaceModel,list : OCP.Interface.Interface_EntityIterator,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Performs the copy of entities from an original model to a new one. It must also copy headers if any. Returns True when done. The provided default works by copying the individual entities designated in the list, by using the general service class CopyTool. It can be redefined for a norm which, either implements Copy by another way (do not forget to Bind each copied result with its original entity in TC) and returns True, or does not know how to copy and returns False
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
    def DumpEntity(self,model : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,entity : OCP.Standard.Standard_Transient,S : OCP.Message.Message_Messenger) -> None: 
        """
        Gives the way of dumping an entity under a form comprehensive for each norm. <model> helps to identify, number ... entities. <level> is to be interpreted for each norm (because of the formats which can be very different)

        Calls deferred DumpEntity with the recorded default level
        """
    @overload
    def DumpEntity(self,model : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,entity : OCP.Standard.Standard_Transient,S : OCP.Message.Message_Messenger,level : int) -> None: ...
    def DumpHelp(self,level : int) -> str: 
        """
        Returns the help line recorded for <level>, or an empty string
        """
    def DumpLevels(self) -> Tuple[int, int]: 
        """
        Returns the recorded default and maximum dump levels If none was recorded, max is returned negative, def as zero
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def ReadFile(self,name : str,model : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol) -> int: 
        """
        Gives the way to Read a File and transfer it to a Model <mod> is the resulting Model, which has to be created by this method. In case of error, <mod> must be returned Null Return value is a status with free values. Simply, 0 is for "Execution OK" The Protocol can be used to work (e.g. create the Model, read and recognize the Entities)
        """
    def SetDumpHelp(self,level : int,help : str) -> None: 
        """
        Records a short line of help for a level (0 - max)
        """
    def SetDumpLevels(self,def_ : int,max : int) -> None: 
        """
        Records a default level and a maximum value for level level for DumpEntity can go between 0 and <max> default value will be <def>
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteFile(self,ctx : IFSelect_ContextWrite) -> bool: 
        """
        Gives the way to Write a File from a Model. <ctx> contains all necessary informations : the model, the protocol, the file name, and the list of File Modifiers to be applied, also with restricted list of selected entities for each one, if required. In return, it brings the produced check-list
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
class IFSelect_WorkSession(OCP.Standard.Standard_Transient):
    """
    This class can be used to simply manage a process such as splitting a file, extracting a set of Entities ... It allows to manage different types of Variables : Integer or Text Parameters, Selections, Dispatches, in addition to a ShareOut. To each of these variables, a unique Integer Identifier is attached. A Name can be attached too as desired.This class can be used to simply manage a process such as splitting a file, extracting a set of Entities ... It allows to manage different types of Variables : Integer or Text Parameters, Selections, Dispatches, in addition to a ShareOut. To each of these variables, a unique Integer Identifier is attached. A Name can be attached too as desired.This class can be used to simply manage a process such as splitting a file, extracting a set of Entities ... It allows to manage different types of Variables : Integer or Text Parameters, Selections, Dispatches, in addition to a ShareOut. To each of these variables, a unique Integer Identifier is attached. A Name can be attached too as desired.
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
    def ClearData(self,mode : int) -> None: 
        """
        Clears recorded data (not the items) according mode : 1 : all Data : Model, Graph, CheckList, + ClearData 4 2 : Graph and CheckList (they will then be recomputed later) 3 : CheckList (it will be recomputed by ComputeCheck) 4 : just content of SelectPointed and Counters Plus 0 : does nothing but called by SetModel ClearData is virtual, hence it can be redefined to clear other data of a specialised Work Session
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
    def CombineAdd(self,selcomb : IFSelect_Selection,seladd : IFSelect_Selection,atnum : int=0) -> int: 
        """
        Adds an input selection to a SelectCombine (Union or Inters.). Returns new count of inputs for this SelectCombine if Done or 0 if <sel> is not kind of SelectCombine, or if <seladd> or <sel> is not in the WorkSession By default, adding is done at the end of the list Else, it is an insertion to rank <atnum> (usefull for Un-ReDo)
        """
    def CombineRemove(self,selcomb : IFSelect_Selection,selrem : IFSelect_Selection) -> bool: 
        """
        Removes an input selection from a SelectCombine (Union or Intersection). Returns True if done, False if <selcomb> is not kind of SelectCombine or <selrem> is not source of <selcomb>
        """
    def ComputeCheck(self,enforce : bool=False) -> bool: 
        """
        Computes the CheckList for the Model currently loaded It can then be used for displays, querries ... Returns True if OK, False else (i.e. no Protocol set, or Model absent). If <enforce> is False, works only if not already done or if a new Model has been loaded from last call. Remark : computation is enforced by every call to SetModel or RunTransformer
        """
    def ComputeCounter(self,counter : IFSelect_SignCounter,forced : bool=False) -> bool: 
        """
        Computes the content of a SignCounter when it is defined with a Selection, then returns True Returns False if the SignCounter is not defined with a Selection, or if its Selection Mode is inhibited <forced> to work around optimisations
        """
    def ComputeCounterFromList(self,counter : IFSelect_SignCounter,list : OCP.TColStd.TColStd_HSequenceOfTransient,clear : bool=True) -> bool: 
        """
        Computes the content of a SignCounter from an input list If <list> is Null, uses internal definition of the Counter : a Selection, else the whole Model (recomputation forced) If <clear> is True (D), starts from scratch Else, cumulates computations
        """
    def ComputeGraph(self,enforce : bool=False) -> bool: 
        """
        Computes the Graph used for Selections, Displays ... If a HGraph is already set, with same model as given by method Model, does nothing. Else, computes a new Graph. If <enforce> is given True, computes a new Graph anyway. Remark that a call to ClearGraph will cause ComputeGraph to really compute a new Graph Returns True if Graph is OK, False else (i.e. if no Protocol is set, or if Model is absent or empty).
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
    def Dispatch(self,id : int) -> IFSelect_Dispatch: 
        """
        Returns a Dispatch, given its Ident in the Session Null result if <id> is not suitable for a Dispatch (undefined, or defined for another kind of variable)
        """
    def DispatchRank(self,disp : IFSelect_Dispatch) -> int: 
        """
        Returns the rank of a Dispatch in the ShareOut, or 0 if <disp> is not in the ShareOut or not in the WorkSession
        """
    def DumpEntity(self,ent : OCP.Standard.Standard_Transient,level : int,S : OCP.Message.Message_Messenger) -> None: 
        """
        Dumps a starting entity according to the current norm. To do this, it calls DumpEntity from WorkLibrary. <level> is to be interpreted for each norm : see specific classes of WorkLibrary for it. Generally, 0 if for very basic (only type ...), greater values give more and more details.
        """
    def DumpModel(self,level : int,S : OCP.Message.Message_Messenger) -> None: 
        """
        Lists the content of the Input Model (if there is one) According level : 0 -> gives only count of Entities and Roots 1 -> Lists also Roots; 2 -> Lists all Entities (by TraceType) 3 -> Performs a call to CheckList (Fails) and lists the result 4 -> as 3 but all CheckList (Fails + Warnings) 5,6,7 : as 3 but resp. Count,List,Labels by Fail 8,9,10 : as 4 but resp. Count,List,Labels by message
        """
    def DumpSelection(self,sel : IFSelect_Selection) -> None: 
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
    def EvalSelection(self,sel : IFSelect_Selection) -> OCP.Interface.Interface_EntityIterator: 
        """
        Evaluates the effect of a Selection applied on the input Model Returned Result remains empty if no input Model has been set
        """
    def EvalSplit(self) -> IFSelect_PacketList: 
        """
        Returns an Evaluation of the whole ShareOut definition : i.e. how the entities of the starting model are forecast to be sent to various files : list of packets according the dispatches, effective lists of roots for each packet (which determine the content of the corresponding file); plus evaluation of which entities are : forgotten (sent into no file), duplicated (sent into more than one file), sent into a given file. See the class PacketList for more details.
        """
    def EvaluateComplete(self,mode : int=0) -> None: 
        """
        Displays the effect of applying the ShareOut on the input Model. <mode> = 0 (default) : displays only roots for each packet, <mode> = 1 : displays all entities for each packet, plus duplicated entities <mode> = 2 : same as <mode> = 1, plus displays forgotten entities (which are in no packet at all)
        """
    def EvaluateDispatch(self,disp : IFSelect_Dispatch,mode : int=0) -> None: 
        """
        Displays the result of applying a Dispatch on the input Model (also shows Remainder if there is) <mode> = 0 (default), displays nothing else <mode> = 1 : displays also duplicated entities (because of this dispatch) <mode> = 2 : displays the entities of the starting Model which are not taken by this dispatch (forgotten entities) <mode> = 3 : displays both duplicated and forgotten entities Remark : EvaluateComplete displays these data evaluated for for all the dispatches, if there are several
        """
    def EvaluateFile(self) -> None: 
        """
        Performs and stores a File Evaluation. The Results are a List of produced Models and a List of names (Strings), in parallel Fills LastRunCheckList
        """
    def EvaluateSelection(self,sel : IFSelect_Selection) -> None: 
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
    def FileRoot(self,disp : IFSelect_Dispatch) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the File Root defined for a Dispatch. Null if no Root Name is defined for it (hence, no File will be produced)
        """
    def FinalModifierIdents(self,formodel : bool) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Fills a Sequence with a list of Idents, those attached to the Modifiers applied to final sending. Model Modifiers if <formodel> is True, File Modifiers else This list is given in the order in which they will be applied (which takes into account the Changes to Modifier Ranks)
        """
    def GeneralModifier(self,id : int) -> IFSelect_GeneralModifier: 
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
    def GiveSelection(self,selname : str) -> IFSelect_Selection: 
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
    def IntParam(self,id : int) -> IFSelect_IntParam: 
        """
        Returns an IntParam, given its Ident in the Session Null result if <id> is not suitable for an IntParam (undefined, or defined for another kind of variable)
        """
    def IntValue(self,it : IFSelect_IntParam) -> int: 
        """
        Returns Integer Value of an IntParam
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
    def IsReversedSelectExtract(self,sel : IFSelect_Selection) -> bool: 
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
    def ItemSelection(self,item : OCP.Standard.Standard_Transient) -> IFSelect_Selection: 
        """
        Returns the Selection of a Dispatch or a GeneralModifier. Returns a Null Handle if none is defined or <item> not good type
        """
    def LastRunCheckList(self) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the Check List produced by the last execution of either : EvaluateFile(for Split), SendSplit, SendAll, SendSelected, RunTransformer-RunModifier Cleared by SetModel or ClearData(1) The field is protected, hence a specialized WorkSession may fill it
        """
    def ListEntities(self,iter : OCP.Interface.Interface_EntityIterator,mode : int) -> None: 
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
    def ModelCopier(self) -> IFSelect_ModelCopier: 
        """
        Gives access to the complete ModelCopier
        """
    def ModelModifier(self,id : int) -> IFSelect_Modifier: 
        """
        Returns a Model Modifier, given its Ident in the Session, i.e. typed as a Modifier (not simply a GeneralModifier) Null result if <id> is not suitable for a Modifier (undefined, or defined for another kind of variable)
        """
    def ModifierRank(self,item : IFSelect_GeneralModifier) -> int: 
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
    def NbSources(self,sel : IFSelect_Selection) -> int: 
        """
        Returns the count of Input Selections known for a Selection, or 0 if <sel> not in the WorkSession. This count is one for a SelectDeduct / SelectExtract kind, two for SelectControl kind, variable for a SelectCombine (Union/Intersection), zero else
        """
    def NbStartingEntities(self) -> int: 
        """
        Returns the count of Entities stored in the Model, or 0
        """
    def NewIntParam(self,name : str='') -> IFSelect_IntParam: 
        """
        Creates a new IntParam. A Name can be set (Optional) Returns the created IntParam, or a Null Handle in case of Failure (see AddItem/AddNamedItem)
        """
    def NewParamFromStatic(self,statname : str,name : str='') -> OCP.Standard.Standard_Transient: 
        """
        Creates a parameter as being bound to a Static If the Static is Integer, this creates an IntParam bound to it by its name. Else this creates a String which is the value of the Static. Returns a null handle if <statname> is unknown as a Static
        """
    def NewSelectPointed(self,list : OCP.TColStd.TColStd_HSequenceOfTransient,name : str) -> IFSelect_Selection: 
        """
        Creates a new Selection, of type SelectPointed, its content starts with <list>. A name must be given (can be empty)
        """
    def NewTextParam(self,name : str='') -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Creates a new (empty) TextParam. A Name can be set (Optional) Returns the created TextParam (as an HAsciiString), or a Null Handle in case of Failure (see AddItem/AddNamedItem)
        """
    def NewTransformStandard(self,copy : bool,name : str='') -> IFSelect_Transformer: 
        """
        Creates and returns a TransformStandard, empty, with its Copy Option (True = Copy, False = On the Spot) and an optional name. To a TransformStandard, the method SetAppliedModifier applies
        """
    def NextIdentForLabel(self,label : str,id : int,mode : int=0) -> int: 
        """
        For query by Label with possible iterations Searches the Ident of which Item has a Label which matches a given one, the search starts from an initial Ident. Returns the first found Ident which follows <id>, or ZERO
        """
    def NumberFromLabel(self,val : str,afternum : int=0) -> int: 
        """
        From a given label in Model, returns the corresponding number Starts from first entity by Default, may start after a given number : this number may be given negative, its absolute value is then considered. Hence a loop on NumberFromLabel may be programmed (stop test is : returned value positive or null)
        """
    def PrintCheckList(self,checklist : OCP.Interface.Interface_CheckIterator,failsonly : bool,mode : IFSelect_PrintCount) -> None: 
        """
        Prints a CheckIterator to the current Trace File, controlled with the current Model complete or fails only, according to <failsonly> <mode> defines the mode of printing 0 : sequential, according entities; else with a CheckCounter 1 : according messages, count of entities 2 : id but with list of entities, designated by their numbers 3 : as 2 but with labels of entities
        """
    def PrintEntityStatus(self,ent : OCP.Standard.Standard_Transient,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints main informations about an entity : its number, type, validity (and checks if any), category, shareds and sharings.. mutable because it can recompute checks as necessary
        """
    def PrintSignatureList(self,signlist : IFSelect_SignatureList,mode : IFSelect_PrintCount) -> None: 
        """
        Prints a SignatureList to the current Trace File, controlled with the current Model <mode> defines the mode of printing (see SignatureList)
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
    def ReadFile(self,filename : str) -> IFSelect_ReturnStatus: 
        """
        Reads a file with the WorkLibrary (sets Model and LoadedFile) Returns a integer status which can be : RetDone if OK, RetVoid if no Protocol not defined, RetError for file not found, RetFail if fail during read
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
    def ResetAppliedModifier(self,modif : IFSelect_GeneralModifier) -> bool: 
        """
        Resets a GeneralModifier to be applied Returns True if done, False if <modif> was not applied
        """
    def ResetItemSelection(self,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Resets input Selection which was set by SetItemSelection Same conditions as for SetItemSelection Returns True if done, False if <item> is not in the WorkSession
        """
    def RunModifier(self,modif : IFSelect_Modifier,copy : bool) -> int: 
        """
        Runs a Modifier on Starting Model. It can modify entities, or add new ones. But the Model or the Protocol is unchanged. The Modifier is applied on each entity of the Model. See also RunModifierSelected Fills LastRunCheckList
        """
    def RunModifierSelected(self,modif : IFSelect_Modifier,sel : IFSelect_Selection,copy : bool) -> int: 
        """
        Acts as RunModifier, but the Modifier is applied on the list determined by a Selection, rather than on the whole Model If the selection is a null handle, the whole model is taken
        """
    def RunTransformer(self,transf : IFSelect_Transformer) -> int: 
        """
        Runs a Transformer on starting Model, which can then be edited or replaced by a new one. The Protocol can also be changed. Fills LastRunCheckList
        """
    def Selection(self,id : int) -> IFSelect_Selection: 
        """
        Returns a Selection, given its Ident in the Session Null result if <id> is not suitable for a Selection (undefined, or defined for another kind of variable)
        """
    def SelectionResult(self,sel : IFSelect_Selection) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the result of a Selection, computed by EvalSelection (see above) under the form of a HSequence (hence, it can be used by a frontal-engine logic). It can be empty Returns a Null Handle if <sel> is not in the WorkSession
        """
    def SelectionResultFromList(self,sel : IFSelect_Selection,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the result of a Selection, by forcing its input with a given list <list> (unless <list> is Null). RULES : <list> applies only for a SelectDeduct kind Selection : its Input is considered : if it is a SelectDeduct kind Selection, its Input is considered, etc... until an Input is not a Deduct/Extract : its result is replaced by <list> and all the chain of deductions is applied
        """
    def SendAll(self,filename : str,computegraph : bool=False) -> IFSelect_ReturnStatus: 
        """
        Sends the starting Model into one file, without splitting, managing remaining data or anything else. <computegraph> true commands the Graph to be recomputed before sending : required when a Model is filled in several steps
        """
    def SendSelected(self,filename : str,sel : IFSelect_Selection,computegraph : bool=False) -> IFSelect_ReturnStatus: 
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
    def SetAppliedModifier(self,modif : IFSelect_GeneralModifier,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Sets a GeneralModifier to be applied to an item : - item = ShareOut : applies for final sending (all dispatches) - item is a Dispatch : applies for this dispatch only Returns True if done, False if <modif> or <item> not in <me>
        """
    def SetControl(self,sel : IFSelect_Selection,sc : IFSelect_Selection,formain : bool=True) -> bool: 
        """
        Sets an Input Selection, Main if <formain> is True, Second else (as <sc>) to a SelectControl (as <sel>). Returns True if Done, False if <sel> is not a SelectControl, or <sc> or <sel> is not in the WorkSession
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
    def SetFileRoot(self,disp : IFSelect_Dispatch,name : str) -> bool: 
        """
        Defines a Root for a Dispatch If <name> is empty, clears Root Name This has as effect to inhibit the production of File by <disp> Returns False if <disp> is not in the WorkSession or if a root name is already defined for it
        """
    def SetInputSelection(self,sel : IFSelect_Selection,input : IFSelect_Selection) -> bool: 
        """
        Sets an Input Selection (as <input>) to a SelectExtract or a SelectDeduct (as <sel>). Returns True if Done, False if <sel> is neither a SelectExtract nor a SelectDeduct, or not in the WorkSession
        """
    def SetIntValue(self,it : IFSelect_IntParam,val : int) -> bool: 
        """
        Changes the Integer Value of an IntParam Returns True if Done, False if <it> is not in the WorkSession
        """
    def SetItemSelection(self,item : OCP.Standard.Standard_Transient,sel : IFSelect_Selection) -> bool: 
        """
        Sets a Selection as input for an item, according its type : if <item> is a Dispatch : as Final Selection if <item> is a GeneralModifier (i.e. any kind of Modifier) : as Selection used to filter entities to modify <sel> Null causes this Selection to be nullified Returns False if <item> is not of a suitable type, or <item> or <sel> is not in the WorkSession
        """
    def SetLibrary(self,theLib : IFSelect_WorkLibrary) -> None: 
        """
        Sets a WorkLibrary, which will be used to Read and Write Files
        """
    def SetLoadedFile(self,theFileName : str) -> None: 
        """
        Stores the filename used for read for setting the model It is cleared by SetModel and ClearData(1)
        """
    def SetModeStat(self,theMode : bool) -> None: 
        """
        Set value of mode responsible for precence of selections after loading If mode set to true that different selections will be accessible after loading else selections will be not accessible after loading( for economy memory in applicatios)
        """
    def SetModel(self,model : OCP.Interface.Interface_InterfaceModel,clearpointed : bool=True) -> None: 
        """
        Sets a Model as input : this will be the Model from which the ShareOut will work if <clearpointed> is True (default) all SelectPointed items are cleared, else they must be managed by the caller Remark : SetModel clears the Graph, recomputes it if a Protocol is set and if the Model is not empty, of course
        """
    def SetModelContent(self,sel : IFSelect_Selection,keep : bool) -> bool: 
        """
        Defines a new content from the former one If <keep> is True, it is given by entities selected by Selection <sel> (and all shared entities) Else, it is given by all the former content but entities selected by the Selection <sel> (and properly shared ones) Returns True if done. Returns False if the selected list (from <sel>) is empty, hence nothing is done
        """
    def SetModelCopier(self,copier : IFSelect_ModelCopier) -> None: 
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
    def SetRemaining(self,mode : IFSelect_RemainMode) -> bool: 
        """
        Processes Remaining data (after having sent files), mode : Forget : forget remaining info (i.e. clear all "Sent" status) Compute : compute and keep remaining (does nothing if : remaining is empty or if no files has been sent) Display : display entities recorded as remaining Undo : restore former state of data (after Remaining(1) ) Returns True if OK, False else (i.e. mode = 2 and Remaining List is either empty or takes all the entities, or mode = 3 and no former computation of remaining data was done)
        """
    def SetSelectPointed(self,sel : IFSelect_Selection,list : OCP.TColStd.TColStd_HSequenceOfTransient,mode : int) -> bool: 
        """
        Changes the content of a Selection of type SelectPointed According <mode> : 0 set <list> as new content (clear former) 1 : adds <list> to actual content -1 : removes <list> from actual content Returns True if done, False if <sel> is not a SelectPointed
        """
    def SetShareOut(self,shareout : IFSelect_ShareOut) -> None: 
        """
        Sets a new ShareOut. Fills Items which its content Warning : data from the former ShareOut are lost
        """
    def SetSignType(self,signtype : IFSelect_Signature) -> None: 
        """
        Sets a specific Signature to be the SignType, i.e. the Signature which will determine TypeName from the Model (basic function). It is recorded in the GTool This Signature is also set as "xst-sign-type" (reserved name)
        """
    def SetTextValue(self,par : OCP.TCollection.TCollection_HAsciiString,val : str) -> bool: 
        """
        Changes the Text Value of a TextParam (an HAsciiString) Returns True if Done, False if <it> is not in the WorkSession
        """
    def ShareOut(self) -> IFSelect_ShareOut: 
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
    def SignCounter(self,id : int) -> IFSelect_SignCounter: 
        """
        Returns a SignCounter from its ident in the Session Null result if <id> is not suitable for a SignCounter (undefined, or defined for another kind of variable)
        """
    def SignType(self) -> IFSelect_Signature: 
        """
        Returns the current SignType
        """
    def SignValue(self,sign : IFSelect_Signature,ent : OCP.Standard.Standard_Transient) -> str: 
        """
        Returns the Value computed by a Signature for an Entity Returns an empty string if the entity does not belong to the loaded model
        """
    def Signature(self,id : int) -> IFSelect_Signature: 
        """
        Returns a Signature, given its Ident in the Session Null result if <id> is not suitable for a Signature (undefined, or defined for another kind of variable)
        """
    def Source(self,sel : IFSelect_Selection,num : int=1) -> IFSelect_Selection: 
        """
        Returns the <num>th Input Selection of a Selection (see NbSources). Returns a Null Handle if <sel> is not in the WorkSession or if <num> is out of the range <1-NbSources> To obtain more details, see the method Sources
        """
    def Sources(self,sel : IFSelect_Selection) -> IFSelect_SelectionIterator: 
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
    def ToggleSelectExtract(self,sel : IFSelect_Selection) -> bool: 
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
    def Transformer(self,id : int) -> IFSelect_Transformer: 
        """
        Returns a Transformer, given its Ident in the Session Null result if <id> is not suitable for a Transformer (undefined, or defined for another kind of variable)
        """
    def UsesAppliedModifier(self,modif : IFSelect_GeneralModifier) -> OCP.Standard.Standard_Transient: 
        """
        Returns the item on which a GeneralModifier is applied : the ShareOut, or a given Dispatch Returns a Null Handle if <modif> is not applied
        """
    def ValidityName(self,ent : OCP.Standard.Standard_Transient) -> str: 
        """
        Returns the Validity Name determined for an entity it is computed by the class SignValidity Remark : an unknown entity gives an empty string
        """
    def WorkLibrary(self) -> IFSelect_WorkLibrary: 
        """
        Returns the WorkLibrary. Null Handle if not yet set should be C++ : return const &
        """
    @overload
    def WriteFile(self,filename : str,sel : IFSelect_Selection) -> IFSelect_ReturnStatus: 
        """
        Writes the current Interface Model globally to a File, and returns a write status which can be : Done OK, Fail file could not be written, Error no norm is selected Remark : It is a simple, one-file writing, other operations are available (such as splitting ...) which calls SendAll

        Writes a sub-part of the current Interface Model to a File, as defined by a Selection <sel>, recomputes the Graph, and returns a write status which can be : Done OK, Fail file could not be written, Error no norm is selected Remark : It is a simple, one-file writing, other operations are available (such as splitting ...) which calls SendSelected
        """
    @overload
    def WriteFile(self,filename : str) -> IFSelect_ReturnStatus: ...
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
IFSelect_CountByItem: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_CountByItem
IFSelect_CountSummary: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_CountSummary
IFSelect_EditComputed: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_EditComputed
IFSelect_EditDynamic: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_EditDynamic
IFSelect_EditProtected: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_EditProtected
IFSelect_EditRead: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_EditRead
IFSelect_Editable: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_Editable
IFSelect_EntitiesByItem: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_EntitiesByItem
IFSelect_FailAndWarn: OCP.IFSelect.IFSelect_PrintFail # value = IFSelect_PrintFail.IFSelect_FailAndWarn
IFSelect_FailOnly: OCP.IFSelect.IFSelect_PrintFail # value = IFSelect_PrintFail.IFSelect_FailOnly
IFSelect_GeneralInfo: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_GeneralInfo
IFSelect_ItemsByEntity: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_ItemsByEntity
IFSelect_ListByItem: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_ListByItem
IFSelect_Mapping: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_Mapping
IFSelect_Optional: OCP.IFSelect.IFSelect_EditValue # value = IFSelect_EditValue.IFSelect_Optional
IFSelect_RemainCompute: OCP.IFSelect.IFSelect_RemainMode # value = IFSelect_RemainMode.IFSelect_RemainCompute
IFSelect_RemainDisplay: OCP.IFSelect.IFSelect_RemainMode # value = IFSelect_RemainMode.IFSelect_RemainDisplay
IFSelect_RemainForget: OCP.IFSelect.IFSelect_RemainMode # value = IFSelect_RemainMode.IFSelect_RemainForget
IFSelect_RemainUndo: OCP.IFSelect.IFSelect_RemainMode # value = IFSelect_RemainMode.IFSelect_RemainUndo
IFSelect_ResultCount: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_ResultCount
IFSelect_RetDone: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetDone
IFSelect_RetError: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetError
IFSelect_RetFail: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetFail
IFSelect_RetStop: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetStop
IFSelect_RetVoid: OCP.IFSelect.IFSelect_ReturnStatus # value = IFSelect_ReturnStatus.IFSelect_RetVoid
IFSelect_ShortByItem: OCP.IFSelect.IFSelect_PrintCount # value = IFSelect_PrintCount.IFSelect_ShortByItem
