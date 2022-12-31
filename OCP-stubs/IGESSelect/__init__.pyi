import OCP.IGESSelect
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IFGraph
import OCP.IFSelect
import OCP.TCollection
import OCP.IGESData
import OCP.Interface
import OCP.Standard
import OCP.TColStd
import io
__all__  = [
"IGESSelect",
"IGESSelect_Activator",
"IGESSelect_FileModifier",
"IGESSelect_ModelModifier",
"IGESSelect_AutoCorrect",
"IGESSelect_ChangeLevelList",
"IGESSelect_ChangeLevelNumber",
"IGESSelect_ComputeStatus",
"IGESSelect_CounterOfLevelNumber",
"IGESSelect_DispPerDrawing",
"IGESSelect_DispPerSingleView",
"IGESSelect_Dumper",
"IGESSelect_EditDirPart",
"IGESSelect_EditHeader",
"IGESSelect_AddFileComment",
"IGESSelect_FloatFormat",
"IGESSelect_IGESName",
"IGESSelect_IGESTypeForm",
"IGESSelect_AddGroup",
"IGESSelect_RebuildDrawings",
"IGESSelect_RebuildGroups",
"IGESSelect_RemoveCurves",
"IGESSelect_SelectBasicGeom",
"IGESSelect_SelectBypassGroup",
"IGESSelect_SelectBypassSubfigure",
"IGESSelect_SelectDrawingFrom",
"IGESSelect_SelectFaces",
"IGESSelect_SelectFromDrawing",
"IGESSelect_SelectFromSingleView",
"IGESSelect_SelectLevelNumber",
"IGESSelect_SelectName",
"IGESSelect_SelectPCurves",
"IGESSelect_SelectSingleViewFrom",
"IGESSelect_SelectSubordinate",
"IGESSelect_SelectVisibleStatus",
"IGESSelect_SetGlobalParameter",
"IGESSelect_SetLabel",
"IGESSelect_SetVersion5",
"IGESSelect_SignColor",
"IGESSelect_SignLevelNumber",
"IGESSelect_SignStatus",
"IGESSelect_SplineToBSpline",
"IGESSelect_UpdateCreationDate",
"IGESSelect_UpdateFileName",
"IGESSelect_UpdateLastChange",
"IGESSelect_ViewSorter",
"IGESSelect_WorkLibrary"
]
class IGESSelect():
    """
    This package defines the library of the most used tools for IGES Files : Selections & Modifiers specific to the IGES norm, and the most needed converters
    """
    @staticmethod
    def Run_s() -> None: 
        """
        Simply gives a prompt for a conversational action on standard input/output. Returns the status of a
        """
    @staticmethod
    def WhatIges_s(ent : OCP.IGESData.IGESData_IGESEntity,G : OCP.Interface.Interface_Graph,sup : OCP.IGESData.IGESData_IGESEntity,index : int) -> int: 
        """
        Gives a quick analysis of an IGES Entity in the context of a model (i.e. a File) described by a Graph. Returned values are : : the most meaningful super entity, if any (else Null) <index> : meaningful index relating to super entity, if any <returned> : a status which helps exploitation of , by giving a case (normally, types of <ent> and should suffice to known the case)
        """
    def __init__(self) -> None: ...
    pass
class IGESSelect_Activator(OCP.IFSelect.IFSelect_Activator, OCP.Standard.Standard_Transient):
    """
    Performs Actions specific to IGESSelect, i.e. creation of IGES Selections and Dispatches, plus dumping specific to IGESPerforms Actions specific to IGESSelect, i.e. creation of IGES Selections and Dispatches, plus dumping specific to IGESPerforms Actions specific to IGESSelect, i.e. creation of IGES Selections and Dispatches, plus dumping specific to IGES
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
    def Adding_s(actor : OCP.IFSelect.IFSelect_Activator,number : int,command : str,mode : int) -> None: 
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
    def Do(self,number : int,pilot : OCP.IFSelect.IFSelect_SessionPilot) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Executes a Command Line for IGESSelect
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
        Sends a short help message for IGESSelect commands
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
    def Select_s(command : str,number : int,actor : OCP.IFSelect.IFSelect_Activator) -> bool: 
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
class IGESSelect_FileModifier(OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a short text which defines the operation performed
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextWrite,writer : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Perform the action specific to each class of File Modifier <ctx> is the ContextWrite, which brings : the model, the protocol, the file name, plus the object AppliedModifiers (not used here) and the CheckList Remark that the model has to be casted for specific access
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
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
class IGESSelect_ModelModifier(OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a short text which defines the operation performed
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform, without Protocol. If Performing with Protocol is redefined, Performing without Protocol must though be defined to do nothing (not called, but demanded by the linker)
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
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
class IGESSelect_AutoCorrect(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Does the absolutely effective corrections on IGES Entity. That is to say : regarding the norm in details, some values have mandatory values, or set of values with constraints. When such values/constraints are univoque, they can be forced. Also nullifies items of Directory Part, Associativities, and Properties, which are not (or not longer) in <target> Model.Does the absolutely effective corrections on IGES Entity. That is to say : regarding the norm in details, some values have mandatory values, or set of values with constraints. When such values/constraints are univoque, they can be forced. Also nullifies items of Directory Part, Associativities, and Properties, which are not (or not longer) in <target> Model.Does the absolutely effective corrections on IGES Entity. That is to say : regarding the norm in details, some values have mandatory values, or set of values with constraints. When such values/constraints are univoque, they can be forced. Also nullifies items of Directory Part, Associativities, and Properties, which are not (or not longer) in <target> Model.
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Auto-correction of IGES Entities"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : corrects entities when it is absolutely obvious, i.e. non equivoque (by DirChecker and specific service OwnCorrect) : works with a protocol.
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_ChangeLevelList(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Changes Level List (in directory part) to a new single value Only entities attached to a LevelListEntity are considered If OldNumber is defined, only entities whose LevelList contains its Value are processed. Else all LevelLists are.Changes Level List (in directory part) to a new single value Only entities attached to a LevelListEntity are considered If OldNumber is defined, only entities whose LevelList contains its Value are processed. Else all LevelLists are.Changes Level List (in directory part) to a new single value Only entities attached to a LevelListEntity are considered If OldNumber is defined, only entities whose LevelList contains its Value are processed. Else all LevelLists are.
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
    def HasNewNumber(self) -> bool: 
        """
        Returns True if NewNumber is defined : then, it gives the new value for Level Number. Else, the first value of the LevelList is used as new Level Number.
        """
    def HasOldNumber(self) -> bool: 
        """
        Returns True if OldNumber is defined : then, only entities which have a LevelList which contains the value are processed. Else, all entities attached to a LevelList are.
        """
    def HasSelection(self) -> bool: 
        """
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which begins by "Changes Level Lists containing <old>", or "Changes all Level Lists in D.E.", and ends by " to Number <new>" or " to Number = first value in List"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def NewNumber(self) -> OCP.IFSelect.IFSelect_IntParam: 
        """
        Returns the parameter for NewNumber. If not defined (Null Handle), it will be interpreted as "new value 0"
        """
    def OldNumber(self) -> OCP.IFSelect.IFSelect_IntParam: 
        """
        Returns the parameter for OldNumber. If not defined (Null Handle), it will be interpreted as "all level lists"
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : considers selected target entities : If OldNumber is not defined, all entities attached to a Level List If OldNumber is defined (value not negative), entities with a Level List which contains this value Attaches all these entities to value given by NewNumber, or the first value of the Level List
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetNewNumber(self,param : OCP.IFSelect.IFSelect_IntParam) -> None: 
        """
        Sets a parameter for NewNumber
        """
    def SetOldNumber(self,param : OCP.IFSelect.IFSelect_IntParam) -> None: 
        """
        Sets a parameter for OldNumber
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_ChangeLevelNumber(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Changes Level Number (as null or single) to a new single value Entities attached to a LevelListEntity are ignored Entities considered can be, either all Entities but those attached to a LevelListEntity, or Entities attached to a specific Level Number (0 for not defined).Changes Level Number (as null or single) to a new single value Entities attached to a LevelListEntity are ignored Entities considered can be, either all Entities but those attached to a LevelListEntity, or Entities attached to a specific Level Number (0 for not defined).Changes Level Number (as null or single) to a new single value Entities attached to a LevelListEntity are ignored Entities considered can be, either all Entities but those attached to a LevelListEntity, or Entities attached to a specific Level Number (0 for not defined).
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
    def HasOldNumber(self) -> bool: 
        """
        Returns True if OldNumber is defined : then, only entities attached to the value of OldNumber will be considered. Else, all entities but those attached to a Level List will be.
        """
    def HasSelection(self) -> bool: 
        """
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Changes Level Number <old> to <new>" , or "Changes all Levels Numbers positive and zero to <new>"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def NewNumber(self) -> OCP.IFSelect.IFSelect_IntParam: 
        """
        Returns the parameter for NewNumber. If not defined (Null Handle), it will be interpreted as "new value 0"
        """
    def OldNumber(self) -> OCP.IFSelect.IFSelect_IntParam: 
        """
        Returns the parameter for OldNumber. If not defined (Null Handle), it will be interpreted as "all level numbers"
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : considers selected target entities : If OldNumber is not defined, all entities but those attached to a Level List If OldNumber is defined (value not negative), entities with a defined Level Number (can be zero) Attaches all these entities to value given by NewNumber, or zero if not defined
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetNewNumber(self,param : OCP.IFSelect.IFSelect_IntParam) -> None: 
        """
        Sets a parameter for NewNumber
        """
    def SetOldNumber(self,param : OCP.IFSelect.IFSelect_IntParam) -> None: 
        """
        Sets a parameter for OldNumber
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_ComputeStatus(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Computes Status of IGES Entities for a whole IGESModel. This concerns SubordinateStatus and UseFlag, which must have some definite values according the way they are referenced. (see definitions of Logical use, Physical use, etc...)Computes Status of IGES Entities for a whole IGESModel. This concerns SubordinateStatus and UseFlag, which must have some definite values according the way they are referenced. (see definitions of Logical use, Physical use, etc...)Computes Status of IGES Entities for a whole IGESModel. This concerns SubordinateStatus and UseFlag, which must have some definite values according the way they are referenced. (see definitions of Logical use, Physical use, etc...)
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Compute Subordinate Status and Use Flag"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : it first evaluates the required values for Subordinate Status and Use Flag (in Directory Part of each IGES Entity). Then it corrects them, for the whole target. Works with a Protocol. Implementation uses BasicEditor
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_CounterOfLevelNumber(OCP.IFSelect.IFSelect_SignCounter, OCP.IFSelect.IFSelect_SignatureList, OCP.Standard.Standard_Transient):
    """
    This class gives information about Level Number. It counts entities according level number, considering also the multiple level (see the class LevelList) for which an entity is attached to each of the listed levels.This class gives information about Level Number. It counts entities according level number, considering also the multiple level (see the class LevelList) for which an entity is attached to each of the listed levels.This class gives information about Level Number. It counts entities according level number, considering also the multiple level (see the class LevelList) for which an entity is attached to each of the listed levels.
    """
    def Add(self,ent : OCP.Standard.Standard_Transient,sign : str) -> None: 
        """
        Adds an entity with its signature, i.e. : - counts an item more for <sign> - if record-list status is set, records the entity Accepts a null entity (the signature is then for the global model). But if the string is empty, counts a Null item.
        """
    def AddEntity(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Adds an entity by considering its signature, which is given by call to method AddSign Returns True if added, False if already in the map (and map control status set)
        """
    def AddFromSelection(self,sel : OCP.IFSelect.IFSelect_Selection,G : OCP.Interface.Interface_Graph) -> None: 
        """
        Adds the result determined by a Selection from a Graph Remark : does not impact at all data from SetSelection & Co
        """
    def AddLevel(self,ent : OCP.Standard.Standard_Transient,level : int) -> None: 
        """
        The internal action to record a new level number, positive, null (no level) or negative (level list)
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
        Adds an entity by considering its lrvrl number(s) A level is added both in numeric and alphanumeric form, i.e. LevelList gives "LEVEL LIST", others (no level or positive level) displays level number on 7 digits (C : %7d) Remark : an entity attached to a Level List is added for " LEVEL LIST", and for each of its constituent levels
        """
    def AddWithGraph(self,list : OCP.TColStd.TColStd_HSequenceOfTransient,graph : OCP.Interface.Interface_Graph) -> None: 
        """
        Adds a list of entities in the context given by the graph Default just call basic AddList Can be redefined to get a signature computed with the graph
        """
    def Clear(self) -> None: 
        """
        Resets already memorized information : also numeric data
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
    def HighestLevel(self) -> int: 
        """
        Returns the highest value found for a level number
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
    def LastValue(self) -> str: 
        """
        Returns the last value recorded by Add (only if SignMode set) Cleared by Clear or Init
        """
    def Levels(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Returns the ordered list of used positive Level numbers
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
    def NbTimesLevel(self,level : int) -> int: 
        """
        Returns the number of times a level is used, 0 if it has not been recorded at all <level> = 0 counts entities attached to no level <level> < 0 counts entities attached to a LevelList
        """
    def PrintCount(self,S : io.BytesIO) -> None: 
        """
        Prints the counts of items (not the list) then the Highest Level Number recorded
        """
    def PrintList(self,S : io.BytesIO,model : OCP.Interface.Interface_InterfaceModel,mod : OCP.IFSelect.IFSelect_PrintCount=IFSelect_PrintCount.IFSelect_ListByItem) -> None: 
        """
        Prints the lists of items, if they are present (else, prints a message "no list available") Uses <model> to determine for each entity to be listed, its number, and its specific identifier (by PrintLabel) <mod> gives a mode for printing : - CountByItem : just count (as PrintCount) - ShortByItem : minimum i.e. count plus 5 first entity numbers - ShortByItem(D) complete list of entity numbers (0: "Global") - EntitiesByItem : list of (entity number/PrintLabel from the model) other modes are ignored
        """
    def PrintSum(self,S : io.BytesIO) -> None: 
        """
        Prints a summary Item which has the greatest count of entities For items which are numeric values : their count, maximum, minimum values, cumul, average
        """
    def SelMode(self) -> int: 
        """
        Returns the mode of working with the selection
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
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
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection as input : this causes content to be cleared then the Selection to be ready to compute (but not immediately)
        """
    def Sign(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Determines and returns the value of the signature for an entity as an HAsciiString. Redefined, gives the same result as AddSign, see this method ("LEVEL LIST" or "nnnnnnn")
        """
    def Signature(self) -> OCP.IFSelect.IFSelect_Signature: 
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
        Returns modifiable the SignOnly Mode If False (D), the counter normally counts If True, the counting work is turned off, Add only fills the LastValue, which can be used as signature, when a counter works from data which are not available from a Signature

        :type: bool
        """
    @ModeSignOnly.setter
    def ModeSignOnly(self, arg1: bool) -> None:
        """
        Returns modifiable the SignOnly Mode If False (D), the counter normally counts If True, the counting work is turned off, Add only fills the LastValue, which can be used as signature, when a counter works from data which are not available from a Signature
        """
    pass
class IGESSelect_DispPerDrawing(OCP.IFSelect.IFSelect_Dispatch, OCP.Standard.Standard_Transient):
    """
    This type of dispatch defines sets of entities attached to distinct drawings. This information is taken from attached views which appear in the Directory Part. Also Drawing Frames are considered when Drawings are part of input list.This type of dispatch defines sets of entities attached to distinct drawings. This information is taken from attached views which appear in the Directory Part. Also Drawing Frames are considered when Drawings are part of input list.This type of dispatch defines sets of entities attached to distinct drawings. This information is taken from attached views which appear in the Directory Part. Also Drawing Frames are considered when Drawings are part of input list.
    """
    def CanHaveRemainder(self) -> bool: 
        """
        Returns True, because of entities attached to no view.
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
    def FinalSelection(self) -> OCP.IFSelect.IFSelect_Selection: 
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
        Returns as Label, "One File per Drawing"
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
        Computes the list of produced Packets. Packets are computed by a ViewSorter (SortDrawings with also frames).
        """
    def Remainder(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Remainder which is a set of Entities. It is supposed to be called once Packets has been called.
        """
    def RootName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Root Name for files produced by this dispatch It is empty if it has not been set or if it has been reset
        """
    def Selections(self) -> OCP.IFSelect.IFSelect_SelectionIterator: 
        """
        Returns the complete list of source Selections (starting from FinalSelection)
        """
    def SetFinalSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: ...
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
class IGESSelect_DispPerSingleView(OCP.IFSelect.IFSelect_Dispatch, OCP.Standard.Standard_Transient):
    """
    This type of dispatch defines sets of entities attached to distinct single views. This information appears in the Directory Part. Drawings are taken into account too, because of their frames (proper lists of annotations)This type of dispatch defines sets of entities attached to distinct single views. This information appears in the Directory Part. Drawings are taken into account too, because of their frames (proper lists of annotations)This type of dispatch defines sets of entities attached to distinct single views. This information appears in the Directory Part. Drawings are taken into account too, because of their frames (proper lists of annotations)
    """
    def CanHaveRemainder(self) -> bool: 
        """
        Returns True, because of entities attached to no view.
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
    def FinalSelection(self) -> OCP.IFSelect.IFSelect_Selection: 
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
        Returns as Label, "One File per single View or Drawing Frame"
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
        Computes the list of produced Packets. Packets are computed by a ViewSorter (SortSingleViews with also frames).
        """
    def Remainder(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Remainder which is a set of Entities. It is supposed to be called once Packets has been called.
        """
    def RootName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Root Name for files produced by this dispatch It is empty if it has not been set or if it has been reset
        """
    def Selections(self) -> OCP.IFSelect.IFSelect_SelectionIterator: 
        """
        Returns the complete list of source Selections (starting from FinalSelection)
        """
    def SetFinalSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: ...
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
class IGESSelect_Dumper(OCP.IFSelect.IFSelect_SessionDumper, OCP.Standard.Standard_Transient):
    """
    Dumper from IGESSelect takes into account, for SessionFile, the classes defined in the package IGESSelect : Selections, Dispatches, ModifiersDumper from IGESSelect takes into account, for SessionFile, the classes defined in the package IGESSelect : Selections, Dispatches, ModifiersDumper from IGESSelect takes into account, for SessionFile, the classes defined in the package IGESSelect : Selections, Dispatches, Modifiers
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
    def First_s() -> OCP.IFSelect.IFSelect_SessionDumper: 
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
    def Next(self) -> OCP.IFSelect.IFSelect_SessionDumper: 
        """
        Returns the Next SesionDumper in the Library. Returns a Null Handle at the End.
        """
    def ReadOwn(self,file : OCP.IFSelect.IFSelect_SessionFile,type : OCP.TCollection.TCollection_AsciiString,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Recognizes and Read Own Parameters for Types of package IGESSelect. Returns True if done and <item> created, False else
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteOwn(self,file : OCP.IFSelect.IFSelect_SessionFile,item : OCP.Standard.Standard_Transient) -> bool: 
        """
        Write the Own Parameters of Types defined in package IGESSelect Returns True if <item> has been processed, False else
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
class IGESSelect_EditDirPart(OCP.IFSelect.IFSelect_Editor, OCP.Standard.Standard_Transient):
    """
    This class is aimed to display and edit the Directory Part of an IGESEntityThis class is aimed to display and edit the Directory Part of an IGESEntityThis class is aimed to display and edit the Directory Part of an IGESEntity
    """
    def Apply(self,form : OCP.IFSelect.IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
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
    def EditMode(self,num : int) -> OCP.IFSelect.IFSelect_EditValue: 
        """
        Returns the edit mode of a Value
        """
    def Form(self,readonly : bool,undoable : bool=True) -> OCP.IFSelect.IFSelect_EditForm: 
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
    def IsList(self,num : int) -> bool: 
        """
        Tells if a parameter is a list
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def ListEditor(self,num : int) -> OCP.IFSelect.IFSelect_ListEditor: 
        """
        Returns a ListEditor for a parameter which is a List Default returns a basic ListEditor for a List, a Null Handle if <num> is not for a List. Can be redefined
        """
    def ListValue(self,form : OCP.IFSelect.IFSelect_EditForm,num : int) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the value of an EditForm as a List, for a given item If not a list, a Null Handle should be returned Default returns a Null Handle, because many Editors have no list to edit. To be redefined as required
        """
    def Load(self,form : OCP.IFSelect.IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
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
    def PrintDefs(self,S : io.BytesIO,labels : bool=False) -> None: 
        """
        None
        """
    def PrintNames(self,S : io.BytesIO) -> None: 
        """
        None
        """
    def Recognize(self,form : OCP.IFSelect.IFSelect_EditForm) -> bool: 
        """
        None
        """
    def SetList(self,num : int,max : int=0) -> None: 
        """
        Sets a parameter to be a List max < 0 : not for a list (set when starting) max = 0 : list with no length limit (default for SetList) max > 0 : list limited to <max> items
        """
    def SetValue(self,num : int,typval : OCP.Interface.Interface_TypedValue,shortname : str='',accessmode : OCP.IFSelect.IFSelect_EditValue=IFSelect_EditValue.IFSelect_Editable) -> None: 
        """
        Sets a Typed Value for a given ident and short name, with an Edit Mode
        """
    def StringValue(self,form : OCP.IFSelect.IFSelect_EditForm,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Update(self,form : OCP.IFSelect.IFSelect_EditForm,num : int,newval : OCP.TCollection.TCollection_HAsciiString,enforce : bool) -> bool: 
        """
        None
        """
    def UpdateList(self,form : OCP.IFSelect.IFSelect_EditForm,num : int,newlist : OCP.TColStd.TColStd_HSequenceOfHAsciiString,enforce : bool) -> bool: 
        """
        Acts as Update, but when the value is a list
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
class IGESSelect_EditHeader(OCP.IFSelect.IFSelect_Editor, OCP.Standard.Standard_Transient):
    """
    This class is aimed to display and edit the Header of an IGES Model : Start Section and Global SectionThis class is aimed to display and edit the Header of an IGES Model : Start Section and Global SectionThis class is aimed to display and edit the Header of an IGES Model : Start Section and Global Section
    """
    def Apply(self,form : OCP.IFSelect.IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
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
    def EditMode(self,num : int) -> OCP.IFSelect.IFSelect_EditValue: 
        """
        Returns the edit mode of a Value
        """
    def Form(self,readonly : bool,undoable : bool=True) -> OCP.IFSelect.IFSelect_EditForm: 
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
    def IsList(self,num : int) -> bool: 
        """
        Tells if a parameter is a list
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def ListEditor(self,num : int) -> OCP.IFSelect.IFSelect_ListEditor: 
        """
        Returns a ListEditor for a parameter which is a List Default returns a basic ListEditor for a List, a Null Handle if <num> is not for a List. Can be redefined
        """
    def ListValue(self,form : OCP.IFSelect.IFSelect_EditForm,num : int) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the value of an EditForm as a List, for a given item If not a list, a Null Handle should be returned Default returns a Null Handle, because many Editors have no list to edit. To be redefined as required
        """
    def Load(self,form : OCP.IFSelect.IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
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
    def PrintDefs(self,S : io.BytesIO,labels : bool=False) -> None: 
        """
        None
        """
    def PrintNames(self,S : io.BytesIO) -> None: 
        """
        None
        """
    def Recognize(self,form : OCP.IFSelect.IFSelect_EditForm) -> bool: 
        """
        None
        """
    def SetList(self,num : int,max : int=0) -> None: 
        """
        Sets a parameter to be a List max < 0 : not for a list (set when starting) max = 0 : list with no length limit (default for SetList) max > 0 : list limited to <max> items
        """
    def SetValue(self,num : int,typval : OCP.Interface.Interface_TypedValue,shortname : str='',accessmode : OCP.IFSelect.IFSelect_EditValue=IFSelect_EditValue.IFSelect_Editable) -> None: 
        """
        Sets a Typed Value for a given ident and short name, with an Edit Mode
        """
    def StringValue(self,form : OCP.IFSelect.IFSelect_EditForm,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Update(self,form : OCP.IFSelect.IFSelect_EditForm,num : int,newval : OCP.TCollection.TCollection_HAsciiString,enforce : bool) -> bool: 
        """
        None
        """
    def UpdateList(self,form : OCP.IFSelect.IFSelect_EditForm,num : int,newlist : OCP.TColStd.TColStd_HSequenceOfHAsciiString,enforce : bool) -> bool: 
        """
        Acts as Update, but when the value is a list
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
class IGESSelect_AddFileComment(IGESSelect_FileModifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    This class allows to add comment lines on writing an IGES File These lines are added to Start Section, instead of the only one blank line written by default.This class allows to add comment lines on writing an IGES File These lines are added to Start Section, instead of the only one blank line written by default.This class allows to add comment lines on writing an IGES File These lines are added to Start Section, instead of the only one blank line written by default.
    """
    def AddLine(self,line : str) -> None: 
        """
        Adds a line for file comment Remark : Lines are limited to 72 useful char.s . A line of more than 72 char.s will be splited into several ones of 72 max each.
        """
    def AddLines(self,lines : OCP.TColStd.TColStd_HSequenceOfHAsciiString) -> None: 
        """
        Adds a list of lines for file comment Each of them must comply with demand of AddLine
        """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
        """
        Returns True if a Model obtained from the Dispatch <disp> is to be treated (apart from the Selection criterium) If Dispatch(me) is Null, returns True. Else, checks <disp>
        """
    def Clear(self) -> None: 
        """
        Clears the list of file comment lines already stored
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns specific Label, which is "Add <nn> Comment Lines (Start Section)"
        """
    def Line(self,num : int) -> str: 
        """
        Returns a stored line given its rank
        """
    def Lines(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the complete list of lines in once
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def NbLines(self) -> int: 
        """
        Returns the count of stored lines
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextWrite,writer : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Sends the comment lines to the file (Start Section)
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_FloatFormat(IGESSelect_FileModifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    This class gives control out format for floatting values : ZeroSuppress or no, Main Format, Format in Range (for values around 1.), as IGESWriter allows to manage it. Formats are given under C-printf formThis class gives control out format for floatting values : ZeroSuppress or no, Main Format, Format in Range (for values around 1.), as IGESWriter allows to manage it. Formats are given under C-printf formThis class gives control out format for floatting values : ZeroSuppress or no, Main Format, Format in Range (for values around 1.), as IGESWriter allows to manage it. Formats are given under C-printf form
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
        """
        Returns the Dispatch to be matched, Null if not set
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Format(self,mainform : OCP.TCollection.TCollection_AsciiString,forminrange : OCP.TCollection.TCollection_AsciiString) -> Tuple[bool, bool, float, float]: 
        """
        Returns all recorded parameters : zerosup : ZeroSuppress status mainform : Main Format (which applies out of the range, or for every real if no range is set) hasrange : True if a FormatInRange is set, False else (following parameters do not apply if it is False) forminrange : Secondary Format (it applies inside the range) rangemin, rangemax : the range in which the secondary format applies
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSelection(self) -> bool: 
        """
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns specific Label : for instance, "Float Format [ZeroSuppress] %E [, in range R1-R2 %f]"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextWrite,writer : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Sets the Floatting Formats of IGESWriter to the recorded parameters
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDefault(self,digits : int=0) -> None: 
        """
        Sets FloatFormat to default value (see Create) but if <digits> is given positive, it commands Formats (main and range) to ensure <digits> significant digits to be displayed
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetFormat(self,format : str='%E') -> None: 
        """
        Sets Main Format to a new value Remark : SetFormat, SetZeroSuppress and SetFormatForRange are independent
        """
    def SetFormatForRange(self,format : str='%f',Rmin : float=0.1,Rmax : float=1000.0) -> None: 
        """
        Sets Format for Range to a new value with its range of application. To cancel it, give format as "" (empty string) Remark that if the condition (0. < Rmin < Rmax) is not verified, this secondary format will be ignored. Moreover, this secondary format is intended to be used in a range around 1.
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
        """
    def SetZeroSuppress(self,mode : bool) -> None: 
        """
        Sets ZeroSuppress mode to a new value
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
class IGESSelect_IGESName(OCP.IFSelect.IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    IGESName is a Signature specific to IGESNorm : it considers the Name of an IGESEntity as being its ShortLabel (some sending systems use name, not to identify entities, but ratjer to classify them)IGESName is a Signature specific to IGESNorm : it considers the Name of an IGESEntity as being its ShortLabel (some sending systems use name, not to identify entities, but ratjer to classify them)IGESName is a Signature specific to IGESNorm : it considers the Name of an IGESEntity as being its ShortLabel (some sending systems use name, not to identify entities, but ratjer to classify them)
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
        Returns the ShortLabel as being the Name of an IGESEntity If <ent> has no name, it returns empty string ""
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
class IGESSelect_IGESTypeForm(OCP.IFSelect.IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    IGESTypeForm is a Signature specific to the IGES Norm : it gives the signature under two possible forms : - as "mmm nnn", with "mmm" as IGES Type Number, and "nnn" as IGES From Number (even if = 0) [Default] - as "mmm" alone, which gives only the IGES Type NumberIGESTypeForm is a Signature specific to the IGES Norm : it gives the signature under two possible forms : - as "mmm nnn", with "mmm" as IGES Type Number, and "nnn" as IGES From Number (even if = 0) [Default] - as "mmm" alone, which gives only the IGES Type NumberIGESTypeForm is a Signature specific to the IGES Norm : it gives the signature under two possible forms : - as "mmm nnn", with "mmm" as IGES Type Number, and "nnn" as IGES From Number (even if = 0) [Default] - as "mmm" alone, which gives only the IGES Type Number
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
    def SetForm(self,withform : bool) -> None: 
        """
        Changes the mode for giving the Form Number
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
        Returns the signature for IGES, "mmm nnn" or "mmm" according creation choice (Type & Form or Type only)
        """
    def __init__(self,withform : bool=True) -> None: ...
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
class IGESSelect_AddGroup(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Adds a Group to contain the entities designated by the Selection. If no Selection is given, nothing is doneAdds a Group to contain the entities designated by the Selection. If no Selection is given, nothing is doneAdds a Group to contain the entities designated by the Selection. If no Selection is given, nothing is done
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Add Group"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : Adds a new group
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_RebuildDrawings(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Rebuilds Drawings which were bypassed to produce new models. If a set of entities, all put into a same IGESModel, were attached to a same Drawing in the starting Model, this Modifier rebuilds the original Drawing, but only with the transferred entities. This includes that all its views are kept too, but empty; and annotations are not kept. Drawing Name is renewed.Rebuilds Drawings which were bypassed to produce new models. If a set of entities, all put into a same IGESModel, were attached to a same Drawing in the starting Model, this Modifier rebuilds the original Drawing, but only with the transferred entities. This includes that all its views are kept too, but empty; and annotations are not kept. Drawing Name is renewed.Rebuilds Drawings which were bypassed to produce new models. If a set of entities, all put into a same IGESModel, were attached to a same Drawing in the starting Model, this Modifier rebuilds the original Drawing, but only with the transferred entities. This includes that all its views are kept too, but empty; and annotations are not kept. Drawing Name is renewed.
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Rebuild Drawings"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : Rebuilds the original Drawings
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_RebuildGroups(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Rebuilds Groups which were bypassed to produce new models. If a set of entities, all put into a same IGESModel, were part of a same Group in the starting Model, this Modifier rebuilds the original group, but only with the transferred entities. The distinctions (Ordered or not, "WithoutBackP" or not) are renewed, also the name of the group.Rebuilds Groups which were bypassed to produce new models. If a set of entities, all put into a same IGESModel, were part of a same Group in the starting Model, this Modifier rebuilds the original group, but only with the transferred entities. The distinctions (Ordered or not, "WithoutBackP" or not) are renewed, also the name of the group.Rebuilds Groups which were bypassed to produce new models. If a set of entities, all put into a same IGESModel, were part of a same Group in the starting Model, this Modifier rebuilds the original group, but only with the transferred entities. The distinctions (Ordered or not, "WithoutBackP" or not) are renewed, also the name of the group.
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Rebuild Groups"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : Rebuilds the original groups
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_RemoveCurves(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Removes Curves UV or 3D (not both !) from Faces, those designated by the Selection. No Selection means all the fileRemoves Curves UV or 3D (not both !) from Faces, those designated by the Selection. No Selection means all the fileRemoves Curves UV or 3D (not both !) from Faces, those designated by the Selection. No Selection means all the file
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Remove Curves UV on Face" or "Remove Curves 3D on Face"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : Removes the Curves
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,UV : bool) -> None: ...
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
class IGESSelect_SelectBasicGeom(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection returns the basic geometric elements contained in an IGES Entity Intended to run a "quick" transfer. I.E. : - for a Group, considers its Elements - for a Trimmed or Bounded Surface or a Face (BREP), considers the 3D curves of each of its loops - for a Plane (108), considers its Bounding Curve - for a Curve itself, takes itThis selection returns the basic geometric elements contained in an IGES Entity Intended to run a "quick" transfer. I.E. : - for a Group, considers its Elements - for a Trimmed or Bounded Surface or a Face (BREP), considers the 3D curves of each of its loops - for a Plane (108), considers its Bounding Curve - for a Curve itself, takes itThis selection returns the basic geometric elements contained in an IGES Entity Intended to run a "quick" transfer. I.E. : - for a Group, considers its Elements - for a Trimmed or Bounded Surface or a Face (BREP), considers the 3D curves of each of its loops - for a Plane (108), considers its Bounding Curve - for a Curve itself, takes it
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
        Explores an entity, to take its contained Curves 3d Works recursively
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Curves 3d" or "Basic Geometry"
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
    @staticmethod
    def SubCurves_s(ent : OCP.IGESData.IGESData_IGESEntity,explored : OCP.Interface.Interface_EntityIterator) -> bool: 
        """
        This method can be called from everywhere to get the curves as sub-elements of a given curve : CompositeCurve : explored lists its subs + returns True Any Curve : explored is not filled but returned is True Other : returned is False
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    def __init__(self,mode : int) -> None: ...
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
class IGESSelect_SelectBypassGroup(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    Selects a list built as follows : Groups are entities type 402, forms 1,7,14,15 (Group, Ordered or not, "WithoutBackPointer" or not)Selects a list built as follows : Groups are entities type 402, forms 1,7,14,15 (Group, Ordered or not, "WithoutBackPointer" or not)Selects a list built as follows : Groups are entities type 402, forms 1,7,14,15 (Group, Ordered or not, "WithoutBackPointer" or not)
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
        Explores an entity : for a Group, gives its elements Else, takes the entity itself
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Content of Group"
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    def __init__(self,level : int=0) -> None: ...
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
class IGESSelect_SelectBypassSubfigure(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    Selects a list built as follows : Subfigures correspond to * Definition (basic : type 308, or Network : type 320) * Instance (Singular : type 408, or Network : 420, or patterns : 412,414)Selects a list built as follows : Subfigures correspond to * Definition (basic : type 308, or Network : type 320) * Instance (Singular : type 408, or Network : 420, or patterns : 412,414)Selects a list built as follows : Subfigures correspond to * Definition (basic : type 308, or Network : type 320) * Instance (Singular : type 408, or Network : 420, or patterns : 412,414)
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
        Explores an entity : for a Subfigure, gives its elements Else, takes the entity itself
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Content of Subfigure"
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    def __init__(self,level : int=0) -> None: ...
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
class IGESSelect_SelectDrawingFrom(OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection gets the Drawings attached to its input IGES entities. They are read through thr Single Views, referenced in Directory Parts of the entitiesThis selection gets the Drawings attached to its input IGES entities. They are read through thr Single Views, referenced in Directory Parts of the entitiesThis selection gets the Drawings attached to its input IGES entities. They are read through thr Single Views, referenced in Directory Parts of the entities
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
        Returns the label, with is "Drawings attached"
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Selects the Drawings attached (through Single Views in Directory Part) to input entities
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IGESSelect_SelectFaces(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection returns the faces contained in an IGES Entity or itself if it is a Face Face means : - Face (510) of a ManifoldSolidBrep - TrimmedSurface (144) - BoundedSurface (143) - Plane with a Bounding Curve (108, form not 0) - Also, any Surface which is not in a TrimmedSurface, a BoundedSurface, or a Face (FREE Surface) -> i.e. a Face for which Natural Bounds will be consideredThis selection returns the faces contained in an IGES Entity or itself if it is a Face Face means : - Face (510) of a ManifoldSolidBrep - TrimmedSurface (144) - BoundedSurface (143) - Plane with a Bounding Curve (108, form not 0) - Also, any Surface which is not in a TrimmedSurface, a BoundedSurface, or a Face (FREE Surface) -> i.e. a Face for which Natural Bounds will be consideredThis selection returns the faces contained in an IGES Entity or itself if it is a Face Face means : - Face (510) of a ManifoldSolidBrep - TrimmedSurface (144) - BoundedSurface (143) - Plane with a Bounding Curve (108, form not 0) - Also, any Surface which is not in a TrimmedSurface, a BoundedSurface, or a Face (FREE Surface) -> i.e. a Face for which Natural Bounds will be considered
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
        Explores an entity, to take its faces Works recursively
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Faces"
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IGESSelect_SelectFromDrawing(OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection gets in all the model, the entities which are attached to the drawing(s) given as input. This includes : - Drawing Frame (Annotations directky referenced by Drawings) - Entities attached to the single Views referenced by DrawingsThis selection gets in all the model, the entities which are attached to the drawing(s) given as input. This includes : - Drawing Frame (Annotations directky referenced by Drawings) - Entities attached to the single Views referenced by DrawingsThis selection gets in all the model, the entities which are attached to the drawing(s) given as input. This includes : - Drawing Frame (Annotations directky referenced by Drawings) - Entities attached to the single Views referenced by Drawings
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
        Returns the label, with is "Entities attached to Drawing"
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Selects the Entities which are attached to the Drawing(s) present in the Input
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IGESSelect_SelectFromSingleView(OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection gets in all the model, the entities which are attached to the views given as input. Only Single Views are considered. This information is kept from Directory Part (View Item).This selection gets in all the model, the entities which are attached to the views given as input. Only Single Views are considered. This information is kept from Directory Part (View Item).This selection gets in all the model, the entities which are attached to the views given as input. Only Single Views are considered. This information is kept from Directory Part (View Item).
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
        Returns the label, with is "Entities attached to single View"
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Selects the Entities which are attached to the Single View(s) present in the Input
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IGESSelect_SelectLevelNumber(OCP.IFSelect.IFSelect_SelectExtract, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection looks at Level Number of IGES Entities : it considers items attached, either to a single level with a given value, or to a level list which contains this valueThis selection looks at Level Number of IGES Entities : it considers items attached, either to a single level with a given value, or to a level list which contains this valueThis selection looks at Level Number of IGES Entities : it considers items attached, either to a single level with a given value, or to a level list which contains this value
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
        Returns the Selection criterium : "IGES Entity, Level Number admits <nn>" (if nn > 0) or "IGES Entity attached to no Level" (if nn = 0)
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
    def LevelNumber(self) -> OCP.IFSelect.IFSelect_IntParam: 
        """
        Returns the Level criterium. NullHandle if not yet set (interpreted as Level = 0 : no level number attached)
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetLevelNumber(self,levnum : OCP.IFSelect.IFSelect_IntParam) -> None: 
        """
        Sets a Parameter as Level criterium
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True if <ent> is an IGES Entity with Level Number admits the criterium (= value if single level, or one of the attached level numbers = value if level list)
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
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IGESSelect_SelectName(OCP.IFSelect.IFSelect_SelectExtract, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    Selects Entities which have a given name. Consider Property Name if present, else Short Label, but not the Subscript Number First version : keeps exact name Later : regular expressionSelects Entities which have a given name. Consider Property Name if present, else Short Label, but not the Subscript Number First version : keeps exact name Later : regular expressionSelects Entities which have a given name. Consider Property Name if present, else Short Label, but not the Subscript Number First version : keeps exact name Later : regular expression
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
        Returns the Selection criterium : "IGES Entity, Name : <name>"
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Name used as Filter
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a Name as a criterium : IGES Entities which have this name are kept (without regular expression, there should be at most one). <name> can be regarded as a Text Parameter
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True if Name of Entity complies with Name Filter
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
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IGESSelect_SelectPCurves(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This Selection returns the pcurves which lie on a face In two modes : global (i.e. a CompositeCurve is not explored) or basic (all the basic curves are listed)This Selection returns the pcurves which lie on a face In two modes : global (i.e. a CompositeCurve is not explored) or basic (all the basic curves are listed)This Selection returns the pcurves which lie on a face In two modes : global (i.e. a CompositeCurve is not explored) or basic (all the basic curves are listed)
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
        Explores an entity, to take its contained PCurves An independent curve is IGNORED : only faces are explored
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Basic PCurves" or "Global PCurves"
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    def __init__(self,basic : bool) -> None: ...
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
class IGESSelect_SelectSingleViewFrom(OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection gets the Single Views attached to its input IGES entities. Single Views themselves or Drawings as passed as such (Drawings, for their Annotations)This selection gets the Single Views attached to its input IGES entities. Single Views themselves or Drawings as passed as such (Drawings, for their Annotations)This selection gets the Single Views attached to its input IGES entities. Single Views themselves or Drawings as passed as such (Drawings, for their Annotations)
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
        Returns the label, with is "Single Views attached"
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Selects the Single Views attached (in Directory Part) to input entities
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IGESSelect_SelectSubordinate(OCP.IFSelect.IFSelect_SelectExtract, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selections uses Subordinate Status as sort criterium It is an integer number which can be : 0 Independent 1 Physically Dependent 2 Logically Dependent 3 Both (recorded) + to sort : 4 : 1 or 3 -> at least Physically 5 : 2 or 3 -> at least Logically 6 : 1 or 2 or 3 -> any kind of dependence (corresponds to 0 reversed)This selections uses Subordinate Status as sort criterium It is an integer number which can be : 0 Independent 1 Physically Dependent 2 Logically Dependent 3 Both (recorded) + to sort : 4 : 1 or 3 -> at least Physically 5 : 2 or 3 -> at least Logically 6 : 1 or 2 or 3 -> any kind of dependence (corresponds to 0 reversed)This selections uses Subordinate Status as sort criterium It is an integer number which can be : 0 Independent 1 Physically Dependent 2 Logically Dependent 3 Both (recorded) + to sort : 4 : 1 or 3 -> at least Physically 5 : 2 or 3 -> at least Logically 6 : 1 or 2 or 3 -> any kind of dependence (corresponds to 0 reversed)
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
        Returns the Selection criterium : "IGES Entity, Independent" etc...
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True if <ent> is an IGES Entity with Subordinate Status matching the criterium
        """
    def SortInGraph(self,rank : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph) -> bool: 
        """
        Works as Sort but works on the Graph Default directly calls Sort, but it can be redefined If SortInGraph is redefined, Sort should be defined even if not called (to avoid deferred methods in a final class)
        """
    def Status(self) -> int: 
        """
        Returns the status used for sorting
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    def __init__(self,status : int) -> None: ...
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
class IGESSelect_SelectVisibleStatus(OCP.IFSelect.IFSelect_SelectExtract, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection looks at Blank Status of IGES Entities Direct selection keeps Visible Entities (Blank = 0), Reverse selection keeps Blanked Entities (Blank = 1)This selection looks at Blank Status of IGES Entities Direct selection keeps Visible Entities (Blank = 0), Reverse selection keeps Blanked Entities (Blank = 1)This selection looks at Blank Status of IGES Entities Direct selection keeps Visible Entities (Blank = 0), Reverse selection keeps Blanked Entities (Blank = 1)
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
        Returns the Selection criterium : "IGES Entity, Status Visible"
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
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Sort on each input Entity : the Entity is kept as output if Sort returns the same value as Direct status
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True if <ent> is an IGES Entity with Blank Status = 0
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
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class IGESSelect_SetGlobalParameter(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Sets a Global (Header) Parameter to a new value, directly given Controls the form of the parameter (Integer, Real, String with such or such form), but not the consistence of the new value regarding the rest of the file.Sets a Global (Header) Parameter to a new value, directly given Controls the form of the parameter (Integer, Real, String with such or such form), but not the consistence of the new value regarding the rest of the file.Sets a Global (Header) Parameter to a new value, directly given Controls the form of the parameter (Integer, Real, String with such or such form), but not the consistence of the new value regarding the rest of the file.
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
    def GlobalNumber(self) -> int: 
        """
        Returns the global parameter number to which this modifiers applies
        """
    def HasSelection(self) -> bool: 
        """
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Sets Global Parameter <numpar> to <new value>"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : only <target> is used : the form of the new value is checked regarding the parameter number (given at creation time).
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
        """
    def SetValue(self,text : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a Text Parameter for the new value
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the value to set to the global parameter (Text Param)
        """
    def __init__(self,numpar : int) -> None: ...
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
class IGESSelect_SetLabel(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Sets/Clears Short Label of Entities, those designated by the Selection. No Selection means all the fileSets/Clears Short Label of Entities, those designated by the Selection. No Selection means all the fileSets/Clears Short Label of Entities, those designated by the Selection. No Selection means all the file
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Clear Short Label" or "Set Label to DE" With possible additional information " (enforced)"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : Sets or Clears the Label
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,mode : int,enforce : bool) -> None: ...
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
class IGESSelect_SetVersion5(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Sets IGES Version (coded in global parameter 23) to be at least IGES 5.1 . If it is older, it is set to IGES 5.1, and LastChangeDate (new Global n0 25) is added (current time) Else, it does nothing (i.e. changes neither IGES Version nor LastChangeDate)Sets IGES Version (coded in global parameter 23) to be at least IGES 5.1 . If it is older, it is set to IGES 5.1, and LastChangeDate (new Global n0 25) is added (current time) Else, it does nothing (i.e. changes neither IGES Version nor LastChangeDate)Sets IGES Version (coded in global parameter 23) to be at least IGES 5.1 . If it is older, it is set to IGES 5.1, and LastChangeDate (new Global n0 25) is added (current time) Else, it does nothing (i.e. changes neither IGES Version nor LastChangeDate)
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Update IGES Version to 5.1"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : only <target> is used : IGES Version (coded) is upgraded to 5.1 if it is older, and it this case the new global parameter 25 (LastChangeDate) is set to current time
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_SignColor(OCP.IFSelect.IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    Gives Color attached to an entity Several forms are possible, according to <mode> 1 : number : "Dnn" for entity, "Snn" for standard, "(none)" for 0 2 : name : Of standard color, or of the color entity, or "(none)" (if the color entity has no name, its label is taken) 3 : RGB values, form R:nn,G:nn,B:nn 4 : RED value : an integer 5 : GREEN value : an integer 6 : BLUE value : an integer Other computable values can be added if needed : CMY values, Percentages for Hue, Lightness, SaturationGives Color attached to an entity Several forms are possible, according to <mode> 1 : number : "Dnn" for entity, "Snn" for standard, "(none)" for 0 2 : name : Of standard color, or of the color entity, or "(none)" (if the color entity has no name, its label is taken) 3 : RGB values, form R:nn,G:nn,B:nn 4 : RED value : an integer 5 : GREEN value : an integer 6 : BLUE value : an integer Other computable values can be added if needed : CMY values, Percentages for Hue, Lightness, SaturationGives Color attached to an entity Several forms are possible, according to <mode> 1 : number : "Dnn" for entity, "Snn" for standard, "(none)" for 0 2 : name : Of standard color, or of the color entity, or "(none)" (if the color entity has no name, its label is taken) 3 : RGB values, form R:nn,G:nn,B:nn 4 : RED value : an integer 5 : GREEN value : an integer 6 : BLUE value : an integer Other computable values can be added if needed : CMY values, Percentages for Hue, Lightness, Saturation
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
        Returns the value (see above)
        """
    def __init__(self,mode : int) -> None: ...
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
class IGESSelect_SignLevelNumber(OCP.IFSelect.IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    Gives D.E. Level Number under two possible forms : * for counter : "LEVEL nnnnnnn", " NO LEVEL", " LEVEL LIST" * for selection : "/nnn/", "/0/", "/1/2/nnn/"Gives D.E. Level Number under two possible forms : * for counter : "LEVEL nnnnnnn", " NO LEVEL", " LEVEL LIST" * for selection : "/nnn/", "/0/", "/1/2/nnn/"Gives D.E. Level Number under two possible forms : * for counter : "LEVEL nnnnnnn", " NO LEVEL", " LEVEL LIST" * for selection : "/nnn/", "/0/", "/1/2/nnn/"
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
        Returns the value (see above)
        """
    def __init__(self,countmode : bool) -> None: ...
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
class IGESSelect_SignStatus(OCP.IFSelect.IFSelect_Signature, OCP.Interface.Interface_SignType):
    """
    Gives D.E. Status under the form i,j,k,l (4 figures) i for BlankStatus j for SubordinateStatus k for UseFlag l for HierarchyGives D.E. Status under the form i,j,k,l (4 figures) i for BlankStatus j for SubordinateStatus k for UseFlag l for HierarchyGives D.E. Status under the form i,j,k,l (4 figures) i for BlankStatus j for SubordinateStatus k for UseFlag l for Hierarchy
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
        Performs the match rule (see above)
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
        Returns the value (see above)
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
class IGESSelect_SplineToBSpline(OCP.IFSelect.IFSelect_Transformer, OCP.Standard.Standard_Transient):
    """
    This type of Transformer allows to convert Spline Curves (IGES type 112) and Surfaces (IGES Type 126) to BSpline Curves (IGES type 114) and Surfac (IGES Type 128). All other entities are rebuilt as identical but on the basis of this conversion.This type of Transformer allows to convert Spline Curves (IGES type 112) and Surfaces (IGES Type 126) to BSpline Curves (IGES type 114) and Surfac (IGES Type 128). All other entities are rebuilt as identical but on the basis of this conversion.This type of Transformer allows to convert Spline Curves (IGES type 112) and Surfaces (IGES Type 126) to BSpline Curves (IGES type 114) and Surfac (IGES Type 128). All other entities are rebuilt as identical but on the basis of this conversion.
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
        Returns a text which defines the way a Transformer works : "Conversion Spline to BSpline" and as opted, " trying to upgrade continuity"
        """
    def OptionTryC2(self) -> bool: 
        """
        Returns the option TryC2 given at creation time
        """
    def Perform(self,G : OCP.Interface.Interface_Graph,protocol : OCP.Interface.Interface_Protocol,checks : OCP.Interface.Interface_CheckIterator,newmod : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Performs the transformation, if there is at least one Spline Curve (112) or Surface (126). Does nothing if there is none.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Updated(self,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns the transformed entities. If original data contained no Spline Curve or Surface, the result is identity : <entto> = <entfrom> Else, the copied counterpart is returned : for a Spline Curve or Surface, it is a converted BSpline Curve or Surface. Else, it is the result of general service Copy (rebuilt as necessary by BSPlines replacing Splines).
        """
    def __init__(self,tryC2 : bool) -> None: ...
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
class IGESSelect_UpdateCreationDate(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Allows to Change the Creation Date indication in the Header (Global Section) of IGES File. It is taken from the operating system (time of application of the Modifier). The Selection of the Modifier is not used : it simply acts as a criterium to select IGES Files to touch upAllows to Change the Creation Date indication in the Header (Global Section) of IGES File. It is taken from the operating system (time of application of the Modifier). The Selection of the Modifier is not used : it simply acts as a criterium to select IGES Files to touch upAllows to Change the Creation Date indication in the Header (Global Section) of IGES File. It is taken from the operating system (time of application of the Modifier). The Selection of the Modifier is not used : it simply acts as a criterium to select IGES Files to touch up
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Update IGES Header Creation Date"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : only <target> is used : the system Date is set to Global Section Item n0 18.
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_UpdateFileName(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Sets the File Name in Header to be the actual name of the file If new file name is unknown, the former one is kept Remark : this works well only when it is Applied and send time If it is run immediately, new file name is unknown and nothing is done The Selection of the Modifier is not used : it simply acts as a criterium to select IGES Files to touch upSets the File Name in Header to be the actual name of the file If new file name is unknown, the former one is kept Remark : this works well only when it is Applied and send time If it is run immediately, new file name is unknown and nothing is done The Selection of the Modifier is not used : it simply acts as a criterium to select IGES Files to touch upSets the File Name in Header to be the actual name of the file If new file name is unknown, the former one is kept Remark : this works well only when it is Applied and send time If it is run immediately, new file name is unknown and nothing is done The Selection of the Modifier is not used : it simply acts as a criterium to select IGES Files to touch up
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Updates IGES File Name to new current one"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : only <target> is used : the system Date is set to Global Section Item n0 18.
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_UpdateLastChange(IGESSelect_ModelModifier, OCP.IFSelect.IFSelect_Modifier, OCP.IFSelect.IFSelect_GeneralModifier, OCP.Standard.Standard_Transient):
    """
    Allows to Change the Last Change Date indication in the Header (Global Section) of IGES File. It is taken from the operating system (time of application of the Modifier). The Selection of the Modifier is not used : it simply acts as a criterium to select IGES Files to touch up. Remark : IGES Models noted as version before IGES 5.1 are in addition changed to 5.1Allows to Change the Last Change Date indication in the Header (Global Section) of IGES File. It is taken from the operating system (time of application of the Modifier). The Selection of the Modifier is not used : it simply acts as a criterium to select IGES Files to touch up. Remark : IGES Models noted as version before IGES 5.1 are in addition changed to 5.1Allows to Change the Last Change Date indication in the Header (Global Section) of IGES File. It is taken from the operating system (time of application of the Modifier). The Selection of the Modifier is not used : it simply acts as a criterium to select IGES Files to touch up. Remark : IGES Models noted as version before IGES 5.1 are in addition changed to 5.1
    """
    def Applies(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> bool: 
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
    def Dispatch(self) -> OCP.IFSelect.IFSelect_Dispatch: 
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
        Returns True if a Selection is set as an additional criterium
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text which is "Update IGES Header Last Change Date"
        """
    def MayChangeGraph(self) -> bool: 
        """
        Returns True if this modifier may change the graph of dependences (aknowledged at creation time)
        """
    def Perform(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        The inherited Perform does the required cast (and refuses to go further if cast has failed) then calls the instantiated Performing
        """
    def PerformProtocol(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,proto : OCP.IGESData.IGESData_Protocol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Perform with Protocol. It is defined to let the Protocol unused and to call Performing without Protocol (most current case). It can be redefined if specific action requires Protocol.
        """
    def Performing(self,ctx : OCP.IFSelect.IFSelect_ContextModif,target : OCP.IGESData.IGESData_IGESModel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific action : only <target> is used : the system Date is set to Global Section Item n0 25. Also sets IGES Version (Item n0 23) to IGES5 if it was older.
        """
    def ResetSelection(self) -> None: 
        """
        Resets the Selection : this criterium is not longer active
        """
    def Selection(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Selection, or a Null Handle if not set
        """
    def SetDispatch(self,disp : OCP.IFSelect.IFSelect_Dispatch) -> None: 
        """
        Attaches to a Dispatch. If <disp> is Null, Resets it (to apply the Modifier on every Dispatch)
        """
    def SetSelection(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Sets a Selection : a Model is treated if it contains one or more Entities designated by the Selection
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
class IGESSelect_ViewSorter(OCP.Standard.Standard_Transient):
    """
    Sorts IGES Entities on the views and drawings. In a first step, it splits a set of entities according the different views they are attached to. Then, packets according single views (+ drawing frames), or according drawings (which refer to the views) can be determinedSorts IGES Entities on the views and drawings. In a first step, it splits a set of entities according the different views they are attached to. Then, packets according single views (+ drawing frames), or according drawings (which refer to the views) can be determinedSorts IGES Entities on the views and drawings. In a first step, it splits a set of entities according the different views they are attached to. Then, packets according single views (+ drawing frames), or according drawings (which refer to the views) can be determined
    """
    def Add(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Adds an item according its type : AddEntity,AddList,AddModel
        """
    def AddEntity(self,igesent : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Adds an IGES entity. Records the view it is attached to. Records directly <ent> if it is a ViewKindEntity or a Drawing Returns True if added, False if already in the map
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Adds a list of entities by adding each of the items
        """
    def AddModel(self,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Adds all the entities contained in a Model
        """
    def Clear(self) -> None: 
        """
        Clears recorded data
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
    def NbEntities(self) -> int: 
        """
        Returns the count of already recorded
        """
    def NbSets(self,final : bool) -> int: 
        """
        Returns the count of sets recorded, one per distinct item. The Remaining List is not counted. If <final> is False, the sets are attached to distinct views determined by the method Add. If <final> is True, they are the sets determined by the last call to, either SortSingleViews, or SortDrawings.
        """
    def SetItem(self,num : int,final : bool) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Item which is attached to a set of entities For <final> and definition of sets, see method NbSets. This item can be a kind of View or a Drawing
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Sets the Model (for PacketList)
        """
    def Sets(self,final : bool) -> OCP.IFSelect.IFSelect_PacketList: 
        """
        Returns the complete content of the determined Sets, which include Duplicated and Remaining (duplication 0) lists For <final> and definition of sets, see method NbSets.
        """
    def SortDrawings(self,G : OCP.Interface.Interface_Graph) -> None: 
        """
        Prepares the result to the sets attached to Drawings : All the single views referenced by a Drawing become bound to the set for this Drawing
        """
    def SortSingleViews(self,alsoframes : bool) -> None: 
        """
        Prepares the result to keep only sets attached to Single Views If <alsoframes> is given True, it keeps also the Drawings as specific sets, in order to get their frames. Entities attached to no single view are put in Remaining List.
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
class IGESSelect_WorkLibrary(OCP.IFSelect.IFSelect_WorkLibrary, OCP.Standard.Standard_Transient):
    """
    Performs Read and Write an IGES File with an IGES ModelPerforms Read and Write an IGES File with an IGES ModelPerforms Read and Write an IGES File with an IGES Model
    """
    def CopyModel(self,original : OCP.Interface.Interface_InterfaceModel,newmodel : OCP.Interface.Interface_InterfaceModel,list : OCP.Interface.Interface_EntityIterator,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Performs the copy of entities from an original model to a new one. It must also copy headers if any. Returns True when done. The provided default works by copying the individual entities designated in the list, by using the general service class CopyTool. It can be redefined for a norm which, either implements Copy by another way (do not forget to Bind each copied result with its original entity in TC) and returns True, or does not know how to copy and returns False
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @staticmethod
    def DefineProtocol_s() -> OCP.IGESData.IGESData_Protocol: 
        """
        Defines a protocol to be adequate for IGES (encompasses ALL the IGES norm including IGESSolid, IGESAppli)
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpEntity(self,model : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol,entity : OCP.Standard.Standard_Transient,S : io.BytesIO,level : int) -> None: 
        """
        Dumps an IGES Entity with an IGES Dumper. <level> is the one used by IGESDumper.
        """
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
    def ReadFile(self,name : str,model : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol) -> int: 
        """
        Reads a IGES File and returns a IGES Model (into <mod>), or lets <mod> "Null" in case of Error Returns 0 if OK, 1 if Read Error, -1 if File not opened
        """
    def ReadStream(self,theName : str,theIStream : io.BytesIO,model : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol) -> int: 
        """
        Interface to read a data from the specified stream.
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
    def WriteFile(self,ctx : OCP.IFSelect.IFSelect_ContextWrite) -> bool: 
        """
        Writes a File from a IGES Model (brought by <ctx>) Returns False (and writes no file) if <ctx> is not for IGES
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
