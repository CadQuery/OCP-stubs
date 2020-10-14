import OCP.Transfer
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.Message
import OCP.Standard
import OCP.NCollection
import OCP.Interface
__all__  = [
"Transfer_ActorOfProcessForTransient",
"Transfer_ActorOfProcessForFinder",
"Transfer_ActorOfFinderProcess",
"Transfer_ActorOfTransientProcess",
"Transfer_ActorDispatch",
"Transfer_Binder",
"Transfer_SimpleBinderOfTransient",
"Transfer_DataInfo",
"Transfer_DispatchControl",
"Transfer_FindHasher",
"Transfer_Finder",
"Transfer_ProcessForFinder",
"Transfer_SequenceOfBinder",
"Transfer_SequenceOfFinder",
"Transfer_TransferIterator",
"Transfer_IteratorOfProcessForTransient",
"Transfer_MapContainer",
"Transfer_MultipleBinder",
"Transfer_FinderProcess",
"Transfer_ProcessForTransient",
"Transfer_ResultFromModel",
"Transfer_ResultFromTransient",
"Transfer_HSequenceOfBinder",
"Transfer_HSequenceOfFinder",
"Transfer_BinderOfTransientInteger",
"Transfer_StatusExec",
"Transfer_StatusResult",
"Transfer_TransferDeadLoop",
"Transfer_TransferDispatch",
"Transfer_TransferFailure",
"Transfer_TransferInput",
"Transfer_IteratorOfProcessForFinder",
"Transfer_TransferOutput",
"Transfer_TransientListBinder",
"Transfer_TransientMapper",
"Transfer_TransientProcess",
"Transfer_UndefMode",
"Transfer_VoidBinder",
"Transfer_StatusDefined",
"Transfer_StatusDone",
"Transfer_StatusError",
"Transfer_StatusInitial",
"Transfer_StatusLoop",
"Transfer_StatusRun",
"Transfer_StatusUsed",
"Transfer_StatusVoid",
"Transfer_UndefContent",
"Transfer_UndefFailure",
"Transfer_UndefIgnore",
"Transfer_UndefUser"
]
class Transfer_ActorOfProcessForTransient(OCP.Standard.Standard_Transient):
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
    def Next(self) -> Transfer_ActorOfProcessForTransient: 
        """
        Returns the Actor defined as Next, or a Null Handle
        """
    def NullResult(self) -> Transfer_Binder: 
        """
        Returns a Binder for No Result, i.e. a Null Handle
        """
    def Recognize(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Prerequesite for Transfer : the method Transfer is called on a starting object only if Recognize has returned True on it This allows to define a list of Actors, each one processing a definite kind of data TransferProcess calls Recognize on each one before calling Transfer. But even if Recognize has returned True, Transfer can reject by returning a Null Binder (afterwards rejection), the next actor is then invoked
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetNext(self,next : Transfer_ActorOfProcessForTransient) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transferring(self,start : OCP.Standard.Standard_Transient,TP : Transfer_ProcessForTransient) -> Transfer_Binder: 
        """
        Specific action of Transfer. The Result is stored in the returned Binder, or a Null Handle for "No result" (Default defined as doing nothing; should be deffered) "mutable" allows the Actor to record intermediate information, in addition to those of TransferProcess
        """
    def TransientResult(self,res : OCP.Standard.Standard_Transient) -> Transfer_SimpleBinderOfTransient: 
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
class Transfer_ActorOfProcessForFinder(OCP.Standard.Standard_Transient):
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
    def Next(self) -> Transfer_ActorOfProcessForFinder: 
        """
        Returns the Actor defined as Next, or a Null Handle
        """
    def NullResult(self) -> Transfer_Binder: 
        """
        Returns a Binder for No Result, i.e. a Null Handle
        """
    def Recognize(self,start : Transfer_Finder) -> bool: 
        """
        Prerequesite for Transfer : the method Transfer is called on a starting object only if Recognize has returned True on it This allows to define a list of Actors, each one processing a definite kind of data TransferProcess calls Recognize on each one before calling Transfer. But even if Recognize has returned True, Transfer can reject by returning a Null Binder (afterwards rejection), the next actor is then invoked
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetNext(self,next : Transfer_ActorOfProcessForFinder) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transferring(self,start : Transfer_Finder,TP : Transfer_ProcessForFinder) -> Transfer_Binder: 
        """
        Specific action of Transfer. The Result is stored in the returned Binder, or a Null Handle for "No result" (Default defined as doing nothing; should be deffered) "mutable" allows the Actor to record intermediate information, in addition to those of TransferProcess
        """
    def TransientResult(self,res : OCP.Standard.Standard_Transient) -> Transfer_SimpleBinderOfTransient: 
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
class Transfer_ActorOfFinderProcess(Transfer_ActorOfProcessForFinder, OCP.Standard.Standard_Transient):
    """
    The original class was renamed. Compatibility onlyThe original class was renamed. Compatibility onlyThe original class was renamed. Compatibility only
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
    def Next(self) -> Transfer_ActorOfProcessForFinder: 
        """
        Returns the Actor defined as Next, or a Null Handle
        """
    def NullResult(self) -> Transfer_Binder: 
        """
        Returns a Binder for No Result, i.e. a Null Handle
        """
    def Recognize(self,start : Transfer_Finder) -> bool: 
        """
        Prerequesite for Transfer : the method Transfer is called on a starting object only if Recognize has returned True on it This allows to define a list of Actors, each one processing a definite kind of data TransferProcess calls Recognize on each one before calling Transfer. But even if Recognize has returned True, Transfer can reject by returning a Null Binder (afterwards rejection), the next actor is then invoked
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetNext(self,next : Transfer_ActorOfProcessForFinder) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transfer(self,start : Transfer_Finder,TP : Transfer_FinderProcess) -> Transfer_Binder: 
        """
        None
        """
    def TransferTransient(self,start : OCP.Standard.Standard_Transient,TP : Transfer_FinderProcess) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Transferring(self,start : Transfer_Finder,TP : Transfer_ProcessForFinder) -> Transfer_Binder: 
        """
        None
        """
    def TransientResult(self,res : OCP.Standard.Standard_Transient) -> Transfer_SimpleBinderOfTransient: 
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
class Transfer_ActorOfTransientProcess(Transfer_ActorOfProcessForTransient, OCP.Standard.Standard_Transient):
    """
    The original class was renamed. Compatibility onlyThe original class was renamed. Compatibility onlyThe original class was renamed. Compatibility only
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
    def Next(self) -> Transfer_ActorOfProcessForTransient: 
        """
        Returns the Actor defined as Next, or a Null Handle
        """
    def NullResult(self) -> Transfer_Binder: 
        """
        Returns a Binder for No Result, i.e. a Null Handle
        """
    def Recognize(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Prerequesite for Transfer : the method Transfer is called on a starting object only if Recognize has returned True on it This allows to define a list of Actors, each one processing a definite kind of data TransferProcess calls Recognize on each one before calling Transfer. But even if Recognize has returned True, Transfer can reject by returning a Null Binder (afterwards rejection), the next actor is then invoked
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetNext(self,next : Transfer_ActorOfProcessForTransient) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transfer(self,start : OCP.Standard.Standard_Transient,TP : Transfer_TransientProcess) -> Transfer_Binder: 
        """
        None
        """
    def TransferTransient(self,start : OCP.Standard.Standard_Transient,TP : Transfer_TransientProcess) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Transferring(self,start : OCP.Standard.Standard_Transient,TP : Transfer_ProcessForTransient) -> Transfer_Binder: 
        """
        None
        """
    def TransientResult(self,res : OCP.Standard.Standard_Transient) -> Transfer_SimpleBinderOfTransient: 
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
class Transfer_ActorDispatch(Transfer_ActorOfTransientProcess, Transfer_ActorOfProcessForTransient, OCP.Standard.Standard_Transient):
    """
    This class allows to work with a TransferDispatch, i.e. to transfer entities from a data set to another one defined by the same interface norm, with the following features : - ActorDispatch itself acts as a default actor, i.e. it copies entities with the general service Copy, as CopyTool does - it allows to add other actors for specific ways of transfer, which may include data modifications, conversions ... - and other features from TransferDispatch (such as mapping other than one-one)This class allows to work with a TransferDispatch, i.e. to transfer entities from a data set to another one defined by the same interface norm, with the following features : - ActorDispatch itself acts as a default actor, i.e. it copies entities with the general service Copy, as CopyTool does - it allows to add other actors for specific ways of transfer, which may include data modifications, conversions ... - and other features from TransferDispatch (such as mapping other than one-one)This class allows to work with a TransferDispatch, i.e. to transfer entities from a data set to another one defined by the same interface norm, with the following features : - ActorDispatch itself acts as a default actor, i.e. it copies entities with the general service Copy, as CopyTool does - it allows to add other actors for specific ways of transfer, which may include data modifications, conversions ... - and other features from TransferDispatch (such as mapping other than one-one)
    """
    def AddActor(self,actor : Transfer_ActorOfTransientProcess) -> None: 
        """
        Utility which adds an actor to the default <me> (it calls SetActor from the TransientProcess)
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
    def Next(self) -> Transfer_ActorOfProcessForTransient: 
        """
        Returns the Actor defined as Next, or a Null Handle
        """
    def NullResult(self) -> Transfer_Binder: 
        """
        Returns a Binder for No Result, i.e. a Null Handle
        """
    def Recognize(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Prerequesite for Transfer : the method Transfer is called on a starting object only if Recognize has returned True on it This allows to define a list of Actors, each one processing a definite kind of data TransferProcess calls Recognize on each one before calling Transfer. But even if Recognize has returned True, Transfer can reject by returning a Null Binder (afterwards rejection), the next actor is then invoked
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetNext(self,next : Transfer_ActorOfProcessForTransient) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transfer(self,start : OCP.Standard.Standard_Transient,TP : Transfer_TransientProcess) -> Transfer_Binder: 
        """
        Specific action : it calls the method Transfer from CopyTool i.e. the general service Copy, then returns the Binder produced by the TransientProcess
        """
    def TransferDispatch(self) -> Transfer_TransferDispatch: 
        """
        Returns the TransferDispatch, which does the work, records the intermediate data, etc... See TransferDispatch & CopyTool, to see the available methods
        """
    def TransferTransient(self,start : OCP.Standard.Standard_Transient,TP : Transfer_TransientProcess) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Transferring(self,start : OCP.Standard.Standard_Transient,TP : Transfer_ProcessForTransient) -> Transfer_Binder: 
        """
        None
        """
    def TransientResult(self,res : OCP.Standard.Standard_Transient) -> Transfer_SimpleBinderOfTransient: 
        """
        Prepares and Returns a Binder for a Transient Result Returns a Null Handle if <res> is itself Null
        """
    @overload
    def __init__(self,amodel : OCP.Interface.Interface_InterfaceModel,lib : OCP.Interface.Interface_GeneralLib) -> None: ...
    @overload
    def __init__(self,amodel : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol) -> None: ...
    @overload
    def __init__(self,amodel : OCP.Interface.Interface_InterfaceModel) -> None: ...
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
class Transfer_Binder(OCP.Standard.Standard_Transient):
    """
    A Binder is an auxiliary object to Map the Result of the Transfer of a given Object : it records the Result of the Unitary Transfer (Resulting Object), status of progress and error (if any) of the ProcessA Binder is an auxiliary object to Map the Result of the Transfer of a given Object : it records the Result of the Unitary Transfer (Resulting Object), status of progress and error (if any) of the ProcessA Binder is an auxiliary object to Map the Result of the Transfer of a given Object : it records the Result of the Unitary Transfer (Resulting Object), status of progress and error (if any) of the Process
    """
    def AddFail(self,mess : str,orig : str='') -> None: 
        """
        Used to declare an individual transfer as beeing erroneous (Status is set to Void, StatusExec is set to Error, <errmess> is added to Check's list of Fails) It is possible to record several messages of error
        """
    def AddResult(self,next : Transfer_Binder) -> None: 
        """
        Adds a next result (at the end of the list) Remark : this information is not processed by Merge
        """
    def AddWarning(self,mess : str,orig : str='') -> None: 
        """
        Used to attach a Warning Message to an individual Transfer It has no effect on the Status
        """
    def CCheck(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages, in order to modify it (adding messages, or replacing it)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages Note that no Entity is associated in this Check
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
    def HasResult(self) -> bool: 
        """
        Returns True if a Result is available (StatusResult = Defined) A Unique Result will be gotten by Result (which must be defined in each sub-class according to result type) For a Multiple Result, see class MultipleBinder For other case, specific access has to be forecast
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
    def IsMultiple(self) -> bool: 
        """
        Returns True if a Binder has several results, either by itself or because it has next results Can be defined by sub-classes.
        """
    def Merge(self,other : Transfer_Binder) -> None: 
        """
        Merges basic data (Check, ExecStatus) from another Binder but keeps its result. Used when a binder is replaced by another one, this allows to keep messages
        """
    def NextResult(self) -> Transfer_Binder: 
        """
        Returns the next result, Null if none
        """
    def ResultType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type which characterizes the Result (if known)
        """
    def ResultTypeName(self) -> str: 
        """
        Returns the Name of the Type which characterizes the Result Can be returned even if ResultType itself is unknown
        """
    def SetAlreadyUsed(self) -> None: 
        """
        Declares that result is now used by another one, it means that it cannot be modified (by Rebind)
        """
    def SetStatusExec(self,stat : Transfer_StatusExec) -> None: 
        """
        Modifies execution status; called by TransferProcess only (for StatusError, rather use SetError, below)
        """
    def Status(self) -> Transfer_StatusResult: 
        """
        Returns status, which can be Initial (not yet done), Made (a result is recorded, not yet shared), Used (it is shared and cannot be modified)
        """
    def StatusExec(self) -> Transfer_StatusExec: 
        """
        Returns execution status
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
class Transfer_SimpleBinderOfTransient(Transfer_Binder, OCP.Standard.Standard_Transient):
    """
    An adapted instantiation of SimpleBinder for Transient Result, i.e. ResultType can be computed from the Result itself, instead of being staticAn adapted instantiation of SimpleBinder for Transient Result, i.e. ResultType can be computed from the Result itself, instead of being staticAn adapted instantiation of SimpleBinder for Transient Result, i.e. ResultType can be computed from the Result itself, instead of being static
    """
    def AddFail(self,mess : str,orig : str='') -> None: 
        """
        Used to declare an individual transfer as beeing erroneous (Status is set to Void, StatusExec is set to Error, <errmess> is added to Check's list of Fails) It is possible to record several messages of error
        """
    def AddResult(self,next : Transfer_Binder) -> None: 
        """
        Adds a next result (at the end of the list) Remark : this information is not processed by Merge
        """
    def AddWarning(self,mess : str,orig : str='') -> None: 
        """
        Used to attach a Warning Message to an individual Transfer It has no effect on the Status
        """
    def CCheck(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages, in order to modify it (adding messages, or replacing it)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages Note that no Entity is associated in this Check
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
    @staticmethod
    def GetTypedResult_s(bnd : Transfer_Binder,atype : OCP.Standard.Standard_Type,res : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns a transient result according to its type (IsKind) i.e. the result itself if IsKind(atype), else searches in NextResult, until first found, then returns True If not found, returns False (res is NOT touched)
        """
    def HasResult(self) -> bool: 
        """
        Returns True if a Result is available (StatusResult = Defined) A Unique Result will be gotten by Result (which must be defined in each sub-class according to result type) For a Multiple Result, see class MultipleBinder For other case, specific access has to be forecast
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
    def IsMultiple(self) -> bool: 
        """
        Returns True if a Binder has several results, either by itself or because it has next results Can be defined by sub-classes.
        """
    def Merge(self,other : Transfer_Binder) -> None: 
        """
        Merges basic data (Check, ExecStatus) from another Binder but keeps its result. Used when a binder is replaced by another one, this allows to keep messages
        """
    def NextResult(self) -> Transfer_Binder: 
        """
        Returns the next result, Null if none
        """
    def Result(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the defined Result, if there is one
        """
    def ResultType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Result (Standard_Transient if no Result is defined)
        """
    def ResultTypeName(self) -> str: 
        """
        Returns the Effective Name of (Dynamic) Type of the Result (void) if no result is defined
        """
    def SetAlreadyUsed(self) -> None: 
        """
        Declares that result is now used by another one, it means that it cannot be modified (by Rebind)
        """
    def SetResult(self,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Defines the Result
        """
    def SetStatusExec(self,stat : Transfer_StatusExec) -> None: 
        """
        Modifies execution status; called by TransferProcess only (for StatusError, rather use SetError, below)
        """
    def Status(self) -> Transfer_StatusResult: 
        """
        Returns status, which can be Initial (not yet done), Made (a result is recorded, not yet shared), Used (it is shared and cannot be modified)
        """
    def StatusExec(self) -> Transfer_StatusExec: 
        """
        Returns execution status
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
class Transfer_DataInfo():
    """
    Gives informations on an object Used as template to instantiate Mapper and SimpleBinder This class is for Transient
    """
    @staticmethod
    def TypeName_s(ent : OCP.Standard.Standard_Transient) -> str: 
        """
        Returns Type Name (string) Allows to name type of non-handled objects
        """
    @staticmethod
    def Type_s(ent : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type attached to an object Here, the Dynamic Type of a Transient. Null Type if unknown
        """
    def __init__(self) -> None: ...
    pass
class Transfer_DispatchControl(OCP.Interface.Interface_CopyControl, OCP.Standard.Standard_Transient):
    """
    This is an auxiliary class for TransferDispatch, which allows to record simple copies, as CopyControl from Interface, but based on a TransientProcess. Hence, it allows in addition more actions (such as recording results of adaptations)This is an auxiliary class for TransferDispatch, which allows to record simple copies, as CopyControl from Interface, but based on a TransientProcess. Hence, it allows in addition more actions (such as recording results of adaptations)This is an auxiliary class for TransferDispatch, which allows to record simple copies, as CopyControl from Interface, but based on a TransientProcess. Hence, it allows in addition more actions (such as recording results of adaptations)
    """
    def Bind(self,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Binds a (Transient) Result to a (Transient) Starting Entity
        """
    def Clear(self) -> None: 
        """
        Clears the List of Copied Results
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
    def Search(self,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> bool: 
        """
        Searches for the Result bound to a Starting Entity If Found, returns True and fills <res> Else, returns False and nullifies <res>
        """
    def StartingModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model from which the transfer is to be done
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransientProcess(self) -> Transfer_TransientProcess: 
        """
        Returns the content of the DispatchControl : it can be used for a direct call, if the basic methods do not suffice
        """
    def __init__(self,model : OCP.Interface.Interface_InterfaceModel,TP : Transfer_TransientProcess) -> None: ...
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
class Transfer_FindHasher():
    """
    FindHasher defines HashCode for Finder, which is : ask a Finder its HashCode ! Because this is the Finder itself which brings the HashCode for its Key
    """
    @staticmethod
    def HashCode_s(theFinder : Transfer_Finder,theUpperBound : int) -> int: 
        """
        Returns hash code for the given finder, in the range [1, theUpperBound]. Asks the finder its hash code, then transforms it to be in the required range
        """
    @staticmethod
    def IsEqual_s(K1 : Transfer_Finder,K2 : Transfer_Finder) -> bool: 
        """
        Returns True if two keys are the same. The test does not work on the Finders themselves but by calling their methods Equates
        """
    def __init__(self) -> None: ...
    pass
class Transfer_Finder(OCP.Standard.Standard_Transient):
    """
    a Finder allows to map any kind of object as a Key for a Map. This works by defining, for a Hash Code, that of the real Key, not of the Finder which acts only as an intermediate. When a Map asks for the HashCode of a Finder, this one returns the code it has determined at creation timea Finder allows to map any kind of object as a Key for a Map. This works by defining, for a Hash Code, that of the real Key, not of the Finder which acts only as an intermediate. When a Map asks for the HashCode of a Finder, this one returns the code it has determined at creation timea Finder allows to map any kind of object as a Key for a Map. This works by defining, for a Hash Code, that of the real Key, not of the Finder which acts only as an intermediate. When a Map asks for the HashCode of a Finder, this one returns the code it has determined at creation time
    """
    def AttrList(self) -> Any: 
        """
        Returns the exhaustive list of attributes
        """
    def Attribute(self,name : str) -> OCP.Standard.Standard_Transient: 
        """
        Returns an attribute from its name. Null Handle if not recorded (whatever Transient, Integer, Real ...)
        """
    def AttributeType(self,name : str) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the type of an attribute : ParamInt , ParamReal , ParamText (String) , ParamIdent (any) or ParamVoid (not recorded)
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
    def Equates(self,other : Transfer_Finder) -> bool: 
        """
        Specific testof equallity : to be defined by each sub-class, must be False if Finders have not the same true Type, else their contents must be compared
        """
    def GetAttribute(self,name : str,type : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns an attribute from its name, filtered by a type If no attribute has this name, or if it is not kind of this type, <val> is Null and returned value is False Else, it is True
        """
    def GetAttributes(self,other : Transfer_Finder,fromname : str='',copied : bool=True) -> None: 
        """
        Gets the list of attributes from <other>, by copying it By default, considers all the attributes from <other> If <fromname> is given, considers only the attributes with name beginning by <fromname>
        """
    def GetHashCode(self) -> int: 
        """
        Returns the HashCode which has been stored by SetHashCode (remark that HashCode could be deferred then be defined by sub-classes, the result is the same)
        """
    def GetIntegerAttribute(self,name : str,val : int) -> bool: 
        """
        Returns an attribute from its name, as integer If no attribute has this name, or not an integer, <val> is 0 and returned value is False Else, it is True
        """
    def GetRealAttribute(self,name : str,val : float) -> bool: 
        """
        Returns an attribute from its name, as real If no attribute has this name, or not a real <val> is 0.0 and returned value is False Else, it is True
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IntegerAttribute(self,name : str) -> int: 
        """
        Returns an integer attribute from its name. 0 if not recorded
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
    def RealAttribute(self,name : str) -> float: 
        """
        Returns a real attribute from its name. 0.0 if not recorded
        """
    def RemoveAttribute(self,name : str) -> bool: 
        """
        Removes an attribute Returns True when done, False if this attribute did not exist
        """
    def SameAttributes(self,other : Transfer_Finder) -> None: 
        """
        Gets the list of attributes from <other>, as such, i.e. not copied : attributes are shared, any attribute edited, added, or removed in <other> is also in <me> and vice versa The former list of attributes of <me> is dropped
        """
    def SetAttribute(self,name : str,val : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an attribute with a given name (replaces the former one with the same name if already exists)
        """
    def SetIntegerAttribute(self,name : str,val : int) -> None: 
        """
        Adds an integer value for an attribute
        """
    def SetRealAttribute(self,name : str,val : float) -> None: 
        """
        Adds a real value for an attribute
        """
    def SetStringAttribute(self,name : str,val : str) -> None: 
        """
        Adds a String value for an attribute
        """
    def StringAttribute(self,name : str) -> str: 
        """
        Returns a String attribute from its name. "" if not recorded
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ValueType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type of the Value. By default, returns the DynamicType of <me>, but can be redefined
        """
    def ValueTypeName(self) -> str: 
        """
        Returns the name of the Type of the Value. Default is name of ValueType, unless it is for a non-handled object
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
class Transfer_ProcessForFinder(OCP.Standard.Standard_Transient):
    def AbnormalResult(self) -> Transfer_IteratorOfProcessForFinder: 
        """
        Returns Binders which are neither "Done" nor "Initial", that is Error,Loop or Run (abnormal states at end of Transfer) Starting Objects are given in correspondance in the iterator
        """
    def Actor(self) -> Transfer_ActorOfProcessForFinder: 
        """
        Returns the defined Actor. Returns a Null Handle if not set.
        """
    def AddError(self,start : Transfer_Finder,mess : str,orig : str='') -> None: 
        """
        (other name of AddFail, maintained for compatibility)
        """
    @overload
    def AddFail(self,start : Transfer_Finder,mess : str,orig : str='') -> None: 
        """
        Adds an Error message to a starting entity (to the check of its Binder of category 0, as a Fail)

        Adds an Error Message to a starting entity from the definition of a Msg (Original+Value)
        """
    @overload
    def AddFail(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: ...
    def AddMultiple(self,start : Transfer_Finder,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an item to a list of results bound to a starting object. Considers a category number, by default 0, for all results
        """
    @overload
    def AddWarning(self,start : Transfer_Finder,mess : str,orig : str='') -> None: 
        """
        Adds a Warning message to a starting entity (to the check of its Binder of category 0)

        Adds a Warning Message to a starting entity from the definition of a Msg (Original+Value)
        """
    @overload
    def AddWarning(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: ...
    def Bind(self,start : Transfer_Finder,binder : Transfer_Binder) -> None: 
        """
        Creates a Link a starting Object with a Binder. This Binder can either bring a Result (effective Binding) or none (it can be set later : pre-binding). Considers a category number, by default 0
        """
    def BindMultiple(self,start : Transfer_Finder) -> None: 
        """
        Prepares an object <start> to be bound with several results. If no Binder is yet attached to <obj>, a MultipleBinder is created, empty. If a Binder is already set, it must accept Multiple Binding. Considers a category number, by default 0
        """
    def BindTransient(self,start : Transfer_Finder,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Binds a starting object with a Transient Result. Uses a SimpleBinderOfTransient to work. If there is already one but with no Result set, sets its Result. Considers a category number, by default 0
        """
    def Check(self,start : Transfer_Finder) -> OCP.Interface.Interface_Check: 
        """
        Returns the Check attached to a starting entity. If <start> is unknown, returns an empty Check Adds a case name to a starting entity Adds a case value to a starting entity Returns the complete case list for an entity. Null Handle if empty In the list of mapped items (between 1 and NbMapped), searches for the first item which follows <num0>(not included) and which has an attribute named <name> Attributes are brought by Binders Hence, allows such an iteration
        """
    def CheckList(self,erronly : bool) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns a CheckList as a list of Check : each one is for a starting entity which have either check (warning or fail) messages are attached, or are in abnormal state : that case gives a specific message If <erronly> is True, checks with Warnings only are ignored
        """
    def CheckListOne(self,start : Transfer_Finder,level : int,erronly : bool) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns a CheckList for one starting object <level> interpreted as by ResultOne If <erronly> is True, checks with Warnings only are ignored
        """
    def CheckNum(self,start : Transfer_Finder) -> int: 
        """
        Computes a number to be associated to a starting object in a check or a check-list By default, returns 0; can be redefined
        """
    def Clean(self) -> None: 
        """
        Rebuilds the Map and the roots to really remove Unbound items Because Unbind keeps the entity in place, even if not bound Hence, working by checking new items is meaningless if a formerly unbound item is rebound
        """
    def Clear(self) -> None: 
        """
        Resets a TransferProcess as ready for a completely new work. Clears general data (roots) and the Map
        """
    def CompleteResult(self,withstart : bool=False) -> Transfer_IteratorOfProcessForFinder: 
        """
        Returns, as an Iterator, the entire log of transfer (list of created objects and Binders which can bring errors) If withstart is given True, Starting Objets are also returned
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
    def ErrorHandle(self) -> bool: 
        """
        Returns error handling flag
        """
    def Find(self,start : Transfer_Finder) -> Transfer_Binder: 
        """
        Returns the Binder which is linked with a starting Object It can either bring a Result (Transfer done) or none (for a pre-binding). If no Binder is linked with <start>, returns a Null Handle Considers a category number, by default 0
        """
    def FindElseBind(self,start : Transfer_Finder) -> Transfer_Binder: 
        """
        Returns a Binder for a starting entity, as follows : Tries to Find the already bound one If none found, creates a VoidBinder and Binds it
        """
    def FindTransient(self,start : Transfer_Finder) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Result of the Transfer of an object <start> as a Transient Result. Returns a Null Handle if there is no Transient Result Considers a category number, by default 0 Warning : Supposes that Binding is done with a SimpleBinderOfTransient
        """
    def FindTypedTransient(self,start : Transfer_Finder,atype : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Searches for a transient result attached to a starting object, according to its type, by criterium IsKind(atype)
        """
    def GetProgress(self) -> OCP.Message.Message_ProgressIndicator: 
        """
        Gets Progress indicator
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTypedTransient(self,binder : Transfer_Binder,atype : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Searches for a transient result recorded in a Binder, whatever this Binder is recorded or not in <me>
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAlreadyUsed(self,start : Transfer_Finder) -> bool: 
        """
        Returns True if the result of the transfer of an object is already used in other ones. If it is, Rebind cannot change it. Considers a category number, by default 0
        """
    def IsBound(self,start : Transfer_Finder) -> bool: 
        """
        Returns True if a Result (whatever its form) is Bound with a starting Object. I.e., if a Binder with a Result set, is linked with it Considers a category number, by default 0
        """
    def IsCheckListEmpty(self,start : Transfer_Finder,level : int,erronly : bool) -> bool: 
        """
        Returns True if no check message is attached to a starting object. <level> interpreted as by ResultOne If <erronly> is True, checks with Warnings only are ignored
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
    def IsLooping(self,alevel : int) -> bool: 
        """
        Returns True if we are surely in a DeadLoop. Evaluation is not exact, it is a "majorant" which must be computed fast. This "majorant" is : <alevel> greater than NbMapped.
        """
    def MapIndex(self,start : Transfer_Finder) -> int: 
        """
        Returns the Index value bound to a Starting Object, 0 if none
        """
    def MapItem(self,num : int) -> Transfer_Binder: 
        """
        Returns the Binder bound to an Index Considers a category number, by default 0
        """
    def Mapped(self,num : int) -> Transfer_Finder: 
        """
        Returns the Starting Object bound to an Index,
        """
    def Mend(self,start : Transfer_Finder,pref : str='') -> None: 
        """
        None
        """
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns Messenger used for outputting messages. The returned object is guaranteed to be non-null; default is Message::Messenger().
        """
    def NbMapped(self) -> int: 
        """
        Returns the maximum possible value for Map Index (no result can be bound with a value greater than it)
        """
    def NbRoots(self) -> int: 
        """
        Returns the count of recorded Roots
        """
    def NestingLevel(self) -> int: 
        """
        Returns Nesting Level of Transfers (managed by methods TranscriptWith & Co). Starts to zero. If no automatic Transfer is used, it remains to zero. Zero means Root Level.
        """
    def PrintTrace(self,start : Transfer_Finder,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints a short information on a starting object. By default prints its Dynamic Type. Can be redefined
        """
    def Rebind(self,start : Transfer_Finder,binder : Transfer_Binder) -> None: 
        """
        Changes the Binder linked with a starting Object for its unitary transfer. This it can be useful when the exact form of the result is known once the transfer is widely engaged. This can be done only on first transfer. Considers a category number, by default 0
        """
    def Recognize(self,start : Transfer_Finder) -> bool: 
        """
        Tells if <start> has been recognized as good candidate for Transfer. i.e. queries the Actor and its Nexts
        """
    def RemoveResult(self,start : Transfer_Finder,level : int,compute : bool=True) -> None: 
        """
        Removes Results attached to (== Unbinds) a given object and, according <level> : <level> = 0 : only it <level> = 1 : it plus its immediately owned sub-results(scope) <level> = 2 : it plus all its owned sub-results(scope)
        """
    def ResetNestingLevel(self) -> None: 
        """
        Resets Nesting Level of Transfers to Zero (Root Level), whatever its current value.
        """
    def Resize(self,nb : int) -> None: 
        """
        Resizes the Map as required (if a new reliable value has been determined). Acts only if <nb> is greater than actual NbMapped
        """
    def ResultOne(self,start : Transfer_Finder,level : int,withstart : bool=False) -> Transfer_IteratorOfProcessForFinder: 
        """
        Returns, as an Iterator, the log of transfer for one object <level> = 0 : this object only and if <start> is a scope owner (else, <level> is ignored) : <level> = 1 : object plus its immediate scoped ones <level> = 2 : object plus all its scoped ones
        """
    def Root(self,num : int) -> Transfer_Finder: 
        """
        Returns a Root Entity given its number in the list (1-NbRoots)
        """
    def RootIndex(self,start : Transfer_Finder) -> int: 
        """
        Returns the index in the list of roots for a starting item, or 0 if it is not recorded as a root
        """
    def RootItem(self,num : int) -> Transfer_Binder: 
        """
        Returns the Binder bound with a Root Entity given its number Considers a category number, by default 0
        """
    def RootResult(self,withstart : bool=False) -> Transfer_IteratorOfProcessForFinder: 
        """
        Returns, as an iterator, the log of root transfer, i.e. the created objects and Binders bound to starting roots If withstart is given True, Starting Objets are also returned
        """
    def SendFail(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddFail (Msg)
        """
    def SendMsg(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Adds an information message Trace is filled if trace level is at least 3
        """
    def SendWarning(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddWarning (Msg)
        """
    def SetActor(self,actor : Transfer_ActorOfProcessForFinder) -> None: 
        """
        Defines an Actor, which is used for automatic Transfer If already defined, the new Actor is cumulated (see SetNext from Actor)
        """
    def SetErrorHandle(self,err : bool) -> None: 
        """
        Allows controls if exceptions will be handled Transfer Operations <err> False : they are not handled with try {} catch {} <err> True : they are Default is False: no handling performed
        """
    def SetMessenger(self,messenger : OCP.Message.Message_Messenger) -> None: 
        """
        Sets Messenger used for outputting messages.
        """
    def SetProgress(self,theProgress : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Sets Progress indicator
        """
    def SetRoot(self,start : Transfer_Finder) -> None: 
        """
        Declares <obj> (and its Result) as Root. This status will be later exploited by RootResult, see below (Result can be produced at any time)
        """
    def SetRootManagement(self,stat : bool) -> None: ...
    def SetTraceLevel(self,tracelev : int) -> None: 
        """
        Sets trace level used for outputting messages: <trace> = 0 : no trace at all <trace> = 1 : handled exceptions and calls to AddError <trace> = 2 : also calls to AddWarning <trace> = 3 : also traces new Roots (uses method ErrorTrace). Default is 1 : Errors traced
        """
    def StartTrace(self,binder : Transfer_Binder,start : Transfer_Finder,level : int,mode : int) -> None: 
        """
        Method called when trace is asked Calls PrintTrace to display information relevant for starting objects (which can be redefined) <level> is Nesting Level of Transfer (0 = root) <mode> controls the way the trace is done : 0 neutral, 1 for Error, 2 for Warning message, 3 for new Root
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceLevel(self) -> int: 
        """
        Returns trace level used for outputting messages.
        """
    def Transfer(self,start : Transfer_Finder) -> bool: 
        """
        Same as Transferring but does not return the Binder. Simply returns True in case of success (for user call)
        """
    def Transferring(self,start : Transfer_Finder) -> Transfer_Binder: 
        """
        Performs the Transfer of a Starting Object, by calling the method TransferProduct (see below). Mapping and Roots are managed : nothing is done if a Result is already Bound, an exception is raised in case of error.
        """
    def Unbind(self,start : Transfer_Finder) -> bool: 
        """
        Removes the Binder linked with a starting object If this Binder brings a non-empty Check, it is replaced by a VoidBinder. Also removes from the list of Roots as required. Returns True if done, False if <start> was not bound Considers a category number, by default 0
        """
    @overload
    def __init__(self,nb : int=10000) -> None: ...
    @overload
    def __init__(self,printer : OCP.Message.Message_Messenger,nb : int=10000) -> None: ...
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
class Transfer_SequenceOfBinder(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Transfer_SequenceOfBinder) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Transfer_Binder) -> None: ...
    def Assign(self,theOther : Transfer_SequenceOfBinder) -> Transfer_SequenceOfBinder: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Transfer_Binder: 
        """
        First item access
        """
    def ChangeLast(self) -> Transfer_Binder: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Transfer_Binder: 
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
    def First(self) -> Transfer_Binder: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Transfer_SequenceOfBinder) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Transfer_Binder) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Transfer_Binder) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Transfer_SequenceOfBinder) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Transfer_Binder: 
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
    def Prepend(self,theSeq : Transfer_SequenceOfBinder) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Transfer_Binder) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Transfer_Binder) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Transfer_SequenceOfBinder) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Transfer_Binder: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Transfer_SequenceOfBinder) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Transfer_SequenceOfFinder(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Transfer_Finder) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Transfer_SequenceOfFinder) -> None: ...
    def Assign(self,theOther : Transfer_SequenceOfFinder) -> Transfer_SequenceOfFinder: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Transfer_Finder: 
        """
        First item access
        """
    def ChangeLast(self) -> Transfer_Finder: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Transfer_Finder: 
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
    def First(self) -> Transfer_Finder: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Transfer_SequenceOfFinder) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Transfer_Finder) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Transfer_SequenceOfFinder) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Transfer_Finder) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Transfer_Finder: 
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
    def Prepend(self,theItem : Transfer_Finder) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Transfer_SequenceOfFinder) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Transfer_Finder) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Transfer_SequenceOfFinder) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Transfer_Finder: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Transfer_SequenceOfFinder) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Transfer_TransferIterator():
    """
    Defines an Iterator on the result of a Transfer Available for Normal Results or not (Erroneous Transfer) It gives several kinds of Informations, and allows to consider various criteria (criteria are cumulative)
    """
    def AddItem(self,atr : Transfer_Binder) -> None: 
        """
        Adds a Binder to the iteration list (construction)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check associated to current Binder (in case of error, it brings Fail messages) (in case of warnings, it brings Warning messages)
        """
    def HasFails(self) -> bool: 
        """
        Returns True if Fail Messages are recorded with the current Binder. They can then be read through Check (see below)
        """
    def HasResult(self) -> bool: 
        """
        Returns True if current Item brings a Result, Transient (Handle) or not or Multiple. That is to say, if it corresponds to a normally acheived Transfer, Transient Result is read by specific TransientResult below. Other kind of Result must be read specifically from its Binder
        """
    def HasTransientResult(self) -> bool: 
        """
        Returns True if the current Item has a Transient Unique Result (if yes, use TransientResult to get it)
        """
    def HasUniqueResult(self) -> bool: 
        """
        Returns True if Current Item has a Unique Result
        """
    def HasWarnings(self) -> bool: 
        """
        Returns True if Warning Messages are recorded with the current Binder. They can then be read through Check (see below)
        """
    def More(self) -> bool: 
        """
        Returns True if there are other Items to iterate
        """
    def Next(self) -> None: 
        """
        Sets Iteration to the next Item
        """
    def Number(self) -> int: 
        """
        Returns count of Binders to be iterated
        """
    def ResultType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type of the Result of the current Item, if Unique. If No Unique Result (Error Transfert or Multiple Result), returns a Null Handle The Type is : the Dynamic Type for a Transient Result, the Type defined by the Binder Class else
        """
    def SelectBinder(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects Items on the Type of Binder : keep only Binders which are of a given Type (if keep is True) or reject only them (if keep is False)
        """
    def SelectItem(self,num : int,keep : bool) -> None: 
        """
        Selects/Unselect (according to <keep> an item designated by its rank <num> in the list Used by sub-classes which have specific criteria
        """
    def SelectResult(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects Items on the Type of Result. Considers only Unique Results. Considers Dynamic Type for Transient Result, Static Type (the one given to define the Binder) else.
        """
    def SelectUnique(self,keep : bool) -> None: 
        """
        Select Items according Unicity : keep only Unique Results (if keep is True) or keep only Multiple Results (if keep is False)
        """
    def Start(self) -> None: 
        """
        Clears Iteration in progress, to allow it to be restarted
        """
    def Status(self) -> Transfer_StatusExec: 
        """
        Returns Execution Status of current Binder Normal transfer corresponds to StatusDone
        """
    def TransientResult(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Transient Result of the current Item if there is (else, returns a null Handle) Supposes that Binding is done by a SimpleBinderOfTransient
        """
    def Value(self) -> Transfer_Binder: 
        """
        Returns the current Binder
        """
    def __init__(self) -> None: ...
    pass
class Transfer_IteratorOfProcessForTransient(Transfer_TransferIterator):
    """
    None
    """
    @overload
    def Add(self,binder : Transfer_Binder,start : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds a Binder to the iteration list (construction) with no corresponding Starting Object (note that Result is brought by Binder)

        Adds a Binder to the iteration list, associated with its corresponding Starting Object "start" Starting Object is ignored if not required at Creation time
        """
    @overload
    def Add(self,binder : Transfer_Binder) -> None: ...
    def AddItem(self,atr : Transfer_Binder) -> None: 
        """
        Adds a Binder to the iteration list (construction)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check associated to current Binder (in case of error, it brings Fail messages) (in case of warnings, it brings Warning messages)
        """
    def Filter(self,list : OCP.TColStd.TColStd_HSequenceOfTransient,keep : bool=True) -> None: 
        """
        After having added all items, keeps or rejects items which are attached to starting data given by <only> <keep> = True (D) : keeps. <keep> = False : rejects Does nothing if <withstarts> was False
        """
    def HasFails(self) -> bool: 
        """
        Returns True if Fail Messages are recorded with the current Binder. They can then be read through Check (see below)
        """
    def HasResult(self) -> bool: 
        """
        Returns True if current Item brings a Result, Transient (Handle) or not or Multiple. That is to say, if it corresponds to a normally acheived Transfer, Transient Result is read by specific TransientResult below. Other kind of Result must be read specifically from its Binder
        """
    def HasStarting(self) -> bool: 
        """
        Returns True if Starting Object is available (defined at Creation Time)
        """
    def HasTransientResult(self) -> bool: 
        """
        Returns True if the current Item has a Transient Unique Result (if yes, use TransientResult to get it)
        """
    def HasUniqueResult(self) -> bool: 
        """
        Returns True if Current Item has a Unique Result
        """
    def HasWarnings(self) -> bool: 
        """
        Returns True if Warning Messages are recorded with the current Binder. They can then be read through Check (see below)
        """
    def More(self) -> bool: 
        """
        Returns True if there are other Items to iterate
        """
    def Next(self) -> None: 
        """
        Sets Iteration to the next Item
        """
    def Number(self) -> int: 
        """
        Returns count of Binders to be iterated
        """
    def ResultType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type of the Result of the current Item, if Unique. If No Unique Result (Error Transfert or Multiple Result), returns a Null Handle The Type is : the Dynamic Type for a Transient Result, the Type defined by the Binder Class else
        """
    def SelectBinder(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects Items on the Type of Binder : keep only Binders which are of a given Type (if keep is True) or reject only them (if keep is False)
        """
    def SelectItem(self,num : int,keep : bool) -> None: 
        """
        Selects/Unselect (according to <keep> an item designated by its rank <num> in the list Used by sub-classes which have specific criteria
        """
    def SelectResult(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects Items on the Type of Result. Considers only Unique Results. Considers Dynamic Type for Transient Result, Static Type (the one given to define the Binder) else.
        """
    def SelectUnique(self,keep : bool) -> None: 
        """
        Select Items according Unicity : keep only Unique Results (if keep is True) or keep only Multiple Results (if keep is False)
        """
    def Start(self) -> None: 
        """
        Clears Iteration in progress, to allow it to be restarted
        """
    def Starting(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns corresponding Starting Object
        """
    def Status(self) -> Transfer_StatusExec: 
        """
        Returns Execution Status of current Binder Normal transfer corresponds to StatusDone
        """
    def TransientResult(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Transient Result of the current Item if there is (else, returns a null Handle) Supposes that Binding is done by a SimpleBinderOfTransient
        """
    def Value(self) -> Transfer_Binder: 
        """
        Returns the current Binder
        """
    def __init__(self,withstarts : bool) -> None: ...
    pass
class Transfer_MapContainer(OCP.Standard.Standard_Transient):
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
    def GetMapObjects(self) -> Any: 
        """
        Get map already translated geometry objects.
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
    def SetMapObjects(self,theMapObjects : Any) -> None: 
        """
        Set map already translated geometry objects.
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
class Transfer_MultipleBinder(Transfer_Binder, OCP.Standard.Standard_Transient):
    """
    Allows direct binding between a starting Object and the Result of its transfer, when it can be made of several Transient Objects. Compared to a Transcriptor, it has no Transfer ActionAllows direct binding between a starting Object and the Result of its transfer, when it can be made of several Transient Objects. Compared to a Transcriptor, it has no Transfer ActionAllows direct binding between a starting Object and the Result of its transfer, when it can be made of several Transient Objects. Compared to a Transcriptor, it has no Transfer Action
    """
    def AddFail(self,mess : str,orig : str='') -> None: 
        """
        Used to declare an individual transfer as beeing erroneous (Status is set to Void, StatusExec is set to Error, <errmess> is added to Check's list of Fails) It is possible to record several messages of error
        """
    def AddResult(self,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds a new Item to the Multiple Result
        """
    def AddWarning(self,mess : str,orig : str='') -> None: 
        """
        Used to attach a Warning Message to an individual Transfer It has no effect on the Status
        """
    def CCheck(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages, in order to modify it (adding messages, or replacing it)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages Note that no Entity is associated in this Check
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
    def HasResult(self) -> bool: 
        """
        Returns True if a Result is available (StatusResult = Defined) A Unique Result will be gotten by Result (which must be defined in each sub-class according to result type) For a Multiple Result, see class MultipleBinder For other case, specific access has to be forecast
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
    def IsMultiple(self) -> bool: 
        """
        Returns True if a starting object is bound with SEVERAL results : Here, returns allways True
        """
    def Merge(self,other : Transfer_Binder) -> None: 
        """
        Merges basic data (Check, ExecStatus) from another Binder but keeps its result. Used when a binder is replaced by another one, this allows to keep messages
        """
    def MultipleResult(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the Multiple Result, if it is defined (at least one Item). Else, returns a Null Handle
        """
    def NbResults(self) -> int: 
        """
        Returns the actual count of recorded (Transient) results
        """
    def NextResult(self) -> Transfer_Binder: 
        """
        Returns the next result, Null if none
        """
    def ResultType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type permitted for Results, i.e. here Transient
        """
    def ResultTypeName(self) -> str: 
        """
        Returns the Name of the Type which characterizes the Result Here, returns "(list)"
        """
    def ResultValue(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the value of the recorded result n0 <num>
        """
    def SetAlreadyUsed(self) -> None: 
        """
        Declares that result is now used by another one, it means that it cannot be modified (by Rebind)
        """
    def SetMultipleResult(self,mulres : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Defines a Binding with a Multiple Result, given as a Sequence Error if a Unique Result has yet been defined
        """
    def SetStatusExec(self,stat : Transfer_StatusExec) -> None: 
        """
        Modifies execution status; called by TransferProcess only (for StatusError, rather use SetError, below)
        """
    def Status(self) -> Transfer_StatusResult: 
        """
        Returns status, which can be Initial (not yet done), Made (a result is recorded, not yet shared), Used (it is shared and cannot be modified)
        """
    def StatusExec(self) -> Transfer_StatusExec: 
        """
        Returns execution status
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
class Transfer_FinderProcess(Transfer_ProcessForFinder, OCP.Standard.Standard_Transient):
    """
    Adds specific features to the generic definition : PrintTrace is adaptedAdds specific features to the generic definition : PrintTrace is adaptedAdds specific features to the generic definition : PrintTrace is adapted
    """
    def AbnormalResult(self) -> Transfer_IteratorOfProcessForFinder: 
        """
        Returns Binders which are neither "Done" nor "Initial", that is Error,Loop or Run (abnormal states at end of Transfer) Starting Objects are given in correspondance in the iterator
        """
    def Actor(self) -> Transfer_ActorOfProcessForFinder: 
        """
        Returns the defined Actor. Returns a Null Handle if not set.
        """
    def AddError(self,start : Transfer_Finder,mess : str,orig : str='') -> None: 
        """
        (other name of AddFail, maintained for compatibility)
        """
    @overload
    def AddFail(self,start : Transfer_Finder,mess : str,orig : str='') -> None: 
        """
        Adds an Error message to a starting entity (to the check of its Binder of category 0, as a Fail)

        Adds an Error Message to a starting entity from the definition of a Msg (Original+Value)
        """
    @overload
    def AddFail(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: ...
    def AddMultiple(self,start : Transfer_Finder,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an item to a list of results bound to a starting object. Considers a category number, by default 0, for all results
        """
    @overload
    def AddWarning(self,start : Transfer_Finder,mess : str,orig : str='') -> None: 
        """
        Adds a Warning message to a starting entity (to the check of its Binder of category 0)

        Adds a Warning Message to a starting entity from the definition of a Msg (Original+Value)
        """
    @overload
    def AddWarning(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: ...
    def Bind(self,start : Transfer_Finder,binder : Transfer_Binder) -> None: 
        """
        Creates a Link a starting Object with a Binder. This Binder can either bring a Result (effective Binding) or none (it can be set later : pre-binding). Considers a category number, by default 0
        """
    def BindMultiple(self,start : Transfer_Finder) -> None: 
        """
        Prepares an object <start> to be bound with several results. If no Binder is yet attached to <obj>, a MultipleBinder is created, empty. If a Binder is already set, it must accept Multiple Binding. Considers a category number, by default 0
        """
    def BindTransient(self,start : Transfer_Finder,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Binds a starting object with a Transient Result. Uses a SimpleBinderOfTransient to work. If there is already one but with no Result set, sets its Result. Considers a category number, by default 0
        """
    def Check(self,start : Transfer_Finder) -> OCP.Interface.Interface_Check: 
        """
        Returns the Check attached to a starting entity. If <start> is unknown, returns an empty Check Adds a case name to a starting entity Adds a case value to a starting entity Returns the complete case list for an entity. Null Handle if empty In the list of mapped items (between 1 and NbMapped), searches for the first item which follows <num0>(not included) and which has an attribute named <name> Attributes are brought by Binders Hence, allows such an iteration
        """
    def CheckList(self,erronly : bool) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns a CheckList as a list of Check : each one is for a starting entity which have either check (warning or fail) messages are attached, or are in abnormal state : that case gives a specific message If <erronly> is True, checks with Warnings only are ignored
        """
    def CheckListOne(self,start : Transfer_Finder,level : int,erronly : bool) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns a CheckList for one starting object <level> interpreted as by ResultOne If <erronly> is True, checks with Warnings only are ignored
        """
    def CheckNum(self,start : Transfer_Finder) -> int: 
        """
        Computes a number to be associated to a starting object in a check or a check-list By default, returns 0; can be redefined
        """
    def Clean(self) -> None: 
        """
        Rebuilds the Map and the roots to really remove Unbound items Because Unbind keeps the entity in place, even if not bound Hence, working by checking new items is meaningless if a formerly unbound item is rebound
        """
    def Clear(self) -> None: 
        """
        Resets a TransferProcess as ready for a completely new work. Clears general data (roots) and the Map
        """
    def CompleteResult(self,withstart : bool=False) -> Transfer_IteratorOfProcessForFinder: 
        """
        Returns, as an Iterator, the entire log of transfer (list of created objects and Binders which can bring errors) If withstart is given True, Starting Objets are also returned
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
    def ErrorHandle(self) -> bool: 
        """
        Returns error handling flag
        """
    def Find(self,start : Transfer_Finder) -> Transfer_Binder: 
        """
        Returns the Binder which is linked with a starting Object It can either bring a Result (Transfer done) or none (for a pre-binding). If no Binder is linked with <start>, returns a Null Handle Considers a category number, by default 0
        """
    def FindElseBind(self,start : Transfer_Finder) -> Transfer_Binder: 
        """
        Returns a Binder for a starting entity, as follows : Tries to Find the already bound one If none found, creates a VoidBinder and Binds it
        """
    def FindTransient(self,start : Transfer_Finder) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Result of the Transfer of an object <start> as a Transient Result. Returns a Null Handle if there is no Transient Result Considers a category number, by default 0 Warning : Supposes that Binding is done with a SimpleBinderOfTransient
        """
    def FindTypedTransient(self,start : Transfer_Finder,atype : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Searches for a transient result attached to a starting object, according to its type, by criterium IsKind(atype)
        """
    def GetProgress(self) -> OCP.Message.Message_ProgressIndicator: 
        """
        Gets Progress indicator
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTypedTransient(self,binder : Transfer_Binder,atype : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Searches for a transient result recorded in a Binder, whatever this Binder is recorded or not in <me>
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAlreadyUsed(self,start : Transfer_Finder) -> bool: 
        """
        Returns True if the result of the transfer of an object is already used in other ones. If it is, Rebind cannot change it. Considers a category number, by default 0
        """
    def IsBound(self,start : Transfer_Finder) -> bool: 
        """
        Returns True if a Result (whatever its form) is Bound with a starting Object. I.e., if a Binder with a Result set, is linked with it Considers a category number, by default 0
        """
    def IsCheckListEmpty(self,start : Transfer_Finder,level : int,erronly : bool) -> bool: 
        """
        Returns True if no check message is attached to a starting object. <level> interpreted as by ResultOne If <erronly> is True, checks with Warnings only are ignored
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
    def IsLooping(self,alevel : int) -> bool: 
        """
        Returns True if we are surely in a DeadLoop. Evaluation is not exact, it is a "majorant" which must be computed fast. This "majorant" is : <alevel> greater than NbMapped.
        """
    def MapIndex(self,start : Transfer_Finder) -> int: 
        """
        Returns the Index value bound to a Starting Object, 0 if none
        """
    def MapItem(self,num : int) -> Transfer_Binder: 
        """
        Returns the Binder bound to an Index Considers a category number, by default 0
        """
    def Mapped(self,num : int) -> Transfer_Finder: 
        """
        Returns the Starting Object bound to an Index,
        """
    def Mend(self,start : Transfer_Finder,pref : str='') -> None: 
        """
        None
        """
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns Messenger used for outputting messages. The returned object is guaranteed to be non-null; default is Message::Messenger().
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model which can be used for context
        """
    def NbMapped(self) -> int: 
        """
        Returns the maximum possible value for Map Index (no result can be bound with a value greater than it)
        """
    def NbRoots(self) -> int: 
        """
        Returns the count of recorded Roots
        """
    def NestingLevel(self) -> int: 
        """
        Returns Nesting Level of Transfers (managed by methods TranscriptWith & Co). Starts to zero. If no automatic Transfer is used, it remains to zero. Zero means Root Level.
        """
    def NextMappedWithAttribute(self,name : str,num0 : int) -> int: 
        """
        In the list of mapped items (between 1 and NbMapped), searches for the first mapped item which follows <num0> (not included) and which has an attribute named <name> The considered Attributes are those brought by Finders,i.e. by Input data. While NextItemWithAttribute works on Result data (Binders)
        """
    def PrintStats(self,mode : int,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints statistics on a given output, according mode
        """
    def PrintTrace(self,start : Transfer_Finder,S : OCP.Message.Message_Messenger) -> None: 
        """
        Specific printing to trace a Finder (by its method ValueType)
        """
    def Rebind(self,start : Transfer_Finder,binder : Transfer_Binder) -> None: 
        """
        Changes the Binder linked with a starting Object for its unitary transfer. This it can be useful when the exact form of the result is known once the transfer is widely engaged. This can be done only on first transfer. Considers a category number, by default 0
        """
    def Recognize(self,start : Transfer_Finder) -> bool: 
        """
        Tells if <start> has been recognized as good candidate for Transfer. i.e. queries the Actor and its Nexts
        """
    def RemoveResult(self,start : Transfer_Finder,level : int,compute : bool=True) -> None: 
        """
        Removes Results attached to (== Unbinds) a given object and, according <level> : <level> = 0 : only it <level> = 1 : it plus its immediately owned sub-results(scope) <level> = 2 : it plus all its owned sub-results(scope)
        """
    def ResetNestingLevel(self) -> None: 
        """
        Resets Nesting Level of Transfers to Zero (Root Level), whatever its current value.
        """
    def Resize(self,nb : int) -> None: 
        """
        Resizes the Map as required (if a new reliable value has been determined). Acts only if <nb> is greater than actual NbMapped
        """
    def ResultOne(self,start : Transfer_Finder,level : int,withstart : bool=False) -> Transfer_IteratorOfProcessForFinder: 
        """
        Returns, as an Iterator, the log of transfer for one object <level> = 0 : this object only and if <start> is a scope owner (else, <level> is ignored) : <level> = 1 : object plus its immediate scoped ones <level> = 2 : object plus all its scoped ones
        """
    def Root(self,num : int) -> Transfer_Finder: 
        """
        Returns a Root Entity given its number in the list (1-NbRoots)
        """
    def RootIndex(self,start : Transfer_Finder) -> int: 
        """
        Returns the index in the list of roots for a starting item, or 0 if it is not recorded as a root
        """
    def RootItem(self,num : int) -> Transfer_Binder: 
        """
        Returns the Binder bound with a Root Entity given its number Considers a category number, by default 0
        """
    def RootResult(self,withstart : bool=False) -> Transfer_IteratorOfProcessForFinder: 
        """
        Returns, as an iterator, the log of root transfer, i.e. the created objects and Binders bound to starting roots If withstart is given True, Starting Objets are also returned
        """
    def SendFail(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddFail (Msg)
        """
    def SendMsg(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Adds an information message Trace is filled if trace level is at least 3
        """
    def SendWarning(self,start : Transfer_Finder,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddWarning (Msg)
        """
    def SetActor(self,actor : Transfer_ActorOfProcessForFinder) -> None: 
        """
        Defines an Actor, which is used for automatic Transfer If already defined, the new Actor is cumulated (see SetNext from Actor)
        """
    def SetErrorHandle(self,err : bool) -> None: 
        """
        Allows controls if exceptions will be handled Transfer Operations <err> False : they are not handled with try {} catch {} <err> True : they are Default is False: no handling performed
        """
    def SetMessenger(self,messenger : OCP.Message.Message_Messenger) -> None: 
        """
        Sets Messenger used for outputting messages.
        """
    def SetModel(self,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Sets an InterfaceModel, which can be used during transfer for instance if a context must be managed, it is in the Model
        """
    def SetProgress(self,theProgress : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Sets Progress indicator
        """
    def SetRoot(self,start : Transfer_Finder) -> None: 
        """
        Declares <obj> (and its Result) as Root. This status will be later exploited by RootResult, see below (Result can be produced at any time)
        """
    def SetRootManagement(self,stat : bool) -> None: ...
    def SetTraceLevel(self,tracelev : int) -> None: 
        """
        Sets trace level used for outputting messages: <trace> = 0 : no trace at all <trace> = 1 : handled exceptions and calls to AddError <trace> = 2 : also calls to AddWarning <trace> = 3 : also traces new Roots (uses method ErrorTrace). Default is 1 : Errors traced
        """
    def StartTrace(self,binder : Transfer_Binder,start : Transfer_Finder,level : int,mode : int) -> None: 
        """
        Method called when trace is asked Calls PrintTrace to display information relevant for starting objects (which can be redefined) <level> is Nesting Level of Transfer (0 = root) <mode> controls the way the trace is done : 0 neutral, 1 for Error, 2 for Warning message, 3 for new Root
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceLevel(self) -> int: 
        """
        Returns trace level used for outputting messages.
        """
    def Transfer(self,start : Transfer_Finder) -> bool: 
        """
        Same as Transferring but does not return the Binder. Simply returns True in case of success (for user call)
        """
    def Transferring(self,start : Transfer_Finder) -> Transfer_Binder: 
        """
        Performs the Transfer of a Starting Object, by calling the method TransferProduct (see below). Mapping and Roots are managed : nothing is done if a Result is already Bound, an exception is raised in case of error.
        """
    def TransientMapper(self,obj : OCP.Standard.Standard_Transient) -> Transfer_TransientMapper: 
        """
        Returns a TransientMapper for a given Transient Object Either <obj> is already mapped, then its Mapper is returned Or it is not, then a new one is created then returned, BUT it is not mapped here (use Bind or FindElseBind to do this)
        """
    def Unbind(self,start : Transfer_Finder) -> bool: 
        """
        Removes the Binder linked with a starting object If this Binder brings a non-empty Check, it is replaced by a VoidBinder. Also removes from the list of Roots as required. Returns True if done, False if <start> was not bound Considers a category number, by default 0
        """
    def __init__(self,nb : int=10000) -> None: ...
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
class Transfer_ProcessForTransient(OCP.Standard.Standard_Transient):
    """
    Manages Transfer of Transient Objects. Produces also ActorOfTransientProcess (deferred class), IteratorOfTransientProcess (for Results), TransferMapOfTransientProcess (internally used) Normally uses as TransientProcess, which adds some specificsManages Transfer of Transient Objects. Produces also ActorOfTransientProcess (deferred class), IteratorOfTransientProcess (for Results), TransferMapOfTransientProcess (internally used) Normally uses as TransientProcess, which adds some specificsManages Transfer of Transient Objects. Produces also ActorOfTransientProcess (deferred class), IteratorOfTransientProcess (for Results), TransferMapOfTransientProcess (internally used) Normally uses as TransientProcess, which adds some specifics
    """
    def AbnormalResult(self) -> Transfer_IteratorOfProcessForTransient: 
        """
        Returns Binders which are neither "Done" nor "Initial", that is Error,Loop or Run (abnormal states at end of Transfer) Starting Objects are given in correspondance in the iterator
        """
    def Actor(self) -> Transfer_ActorOfProcessForTransient: 
        """
        Returns the defined Actor. Returns a Null Handle if not set.
        """
    def AddError(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: 
        """
        (other name of AddFail, maintained for compatibility)
        """
    @overload
    def AddFail(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: 
        """
        Adds an Error message to a starting entity (to the check of its Binder of category 0, as a Fail)

        Adds an Error Message to a starting entity from the definition of a Msg (Original+Value)
        """
    @overload
    def AddFail(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: ...
    def AddMultiple(self,start : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an item to a list of results bound to a starting object. Considers a category number, by default 0, for all results
        """
    @overload
    def AddWarning(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Adds a Warning message to a starting entity (to the check of its Binder of category 0)

        Adds a Warning Message to a starting entity from the definition of a Msg (Original+Value)
        """
    @overload
    def AddWarning(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: ...
    def Bind(self,start : OCP.Standard.Standard_Transient,binder : Transfer_Binder) -> None: 
        """
        Creates a Link a starting Object with a Binder. This Binder can either bring a Result (effective Binding) or none (it can be set later : pre-binding). Considers a category number, by default 0
        """
    def BindMultiple(self,start : OCP.Standard.Standard_Transient) -> None: 
        """
        Prepares an object <start> to be bound with several results. If no Binder is yet attached to <obj>, a MultipleBinder is created, empty. If a Binder is already set, it must accept Multiple Binding. Considers a category number, by default 0
        """
    def BindTransient(self,start : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Binds a starting object with a Transient Result. Uses a SimpleBinderOfTransient to work. If there is already one but with no Result set, sets its Result. Considers a category number, by default 0
        """
    def Check(self,start : OCP.Standard.Standard_Transient) -> OCP.Interface.Interface_Check: 
        """
        Returns the Check attached to a starting entity. If <start> is unknown, returns an empty Check Adds a case name to a starting entity Adds a case value to a starting entity Returns the complete case list for an entity. Null Handle if empty In the list of mapped items (between 1 and NbMapped), searches for the first item which follows <num0>(not included) and which has an attribute named <name> Attributes are brought by Binders Hence, allows such an iteration
        """
    def CheckList(self,erronly : bool) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns a CheckList as a list of Check : each one is for a starting entity which have either check (warning or fail) messages are attached, or are in abnormal state : that case gives a specific message If <erronly> is True, checks with Warnings only are ignored
        """
    def CheckListOne(self,start : OCP.Standard.Standard_Transient,level : int,erronly : bool) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns a CheckList for one starting object <level> interpreted as by ResultOne If <erronly> is True, checks with Warnings only are ignored
        """
    def CheckNum(self,start : OCP.Standard.Standard_Transient) -> int: 
        """
        Computes a number to be associated to a starting object in a check or a check-list By default, returns 0; can be redefined
        """
    def Clean(self) -> None: 
        """
        Rebuilds the Map and the roots to really remove Unbound items Because Unbind keeps the entity in place, even if not bound Hence, working by checking new items is meaningless if a formerly unbound item is rebound
        """
    def Clear(self) -> None: 
        """
        Resets a TransferProcess as ready for a completely new work. Clears general data (roots) and the Map
        """
    def CompleteResult(self,withstart : bool=False) -> Transfer_IteratorOfProcessForTransient: 
        """
        Returns, as an Iterator, the entire log of transfer (list of created objects and Binders which can bring errors) If withstart is given True, Starting Objets are also returned
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
    def ErrorHandle(self) -> bool: 
        """
        Returns error handling flag
        """
    def Find(self,start : OCP.Standard.Standard_Transient) -> Transfer_Binder: 
        """
        Returns the Binder which is linked with a starting Object It can either bring a Result (Transfer done) or none (for a pre-binding). If no Binder is linked with <start>, returns a Null Handle Considers a category number, by default 0
        """
    def FindElseBind(self,start : OCP.Standard.Standard_Transient) -> Transfer_Binder: 
        """
        Returns a Binder for a starting entity, as follows : Tries to Find the already bound one If none found, creates a VoidBinder and Binds it
        """
    def FindTransient(self,start : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Result of the Transfer of an object <start> as a Transient Result. Returns a Null Handle if there is no Transient Result Considers a category number, by default 0 Warning : Supposes that Binding is done with a SimpleBinderOfTransient
        """
    def FindTypedTransient(self,start : OCP.Standard.Standard_Transient,atype : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Searches for a transient result attached to a starting object, according to its type, by criterium IsKind(atype)
        """
    def GetProgress(self) -> OCP.Message.Message_ProgressIndicator: 
        """
        Gets Progress indicator
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTypedTransient(self,binder : Transfer_Binder,atype : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Searches for a transient result recorded in a Binder, whatever this Binder is recorded or not in <me>
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAlreadyUsed(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the result of the transfer of an object is already used in other ones. If it is, Rebind cannot change it. Considers a category number, by default 0
        """
    def IsBound(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if a Result (whatever its form) is Bound with a starting Object. I.e., if a Binder with a Result set, is linked with it Considers a category number, by default 0
        """
    def IsCheckListEmpty(self,start : OCP.Standard.Standard_Transient,level : int,erronly : bool) -> bool: 
        """
        Returns True if no check message is attached to a starting object. <level> interpreted as by ResultOne If <erronly> is True, checks with Warnings only are ignored
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
    def IsLooping(self,alevel : int) -> bool: 
        """
        Returns True if we are surely in a DeadLoop. Evaluation is not exact, it is a "majorant" which must be computed fast. This "majorant" is : <alevel> greater than NbMapped.
        """
    def MapIndex(self,start : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the Index value bound to a Starting Object, 0 if none
        """
    def MapItem(self,num : int) -> Transfer_Binder: 
        """
        Returns the Binder bound to an Index Considers a category number, by default 0
        """
    def Mapped(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Starting Object bound to an Index,
        """
    def Mend(self,start : OCP.Standard.Standard_Transient,pref : str='') -> None: 
        """
        None
        """
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns Messenger used for outputting messages. The returned object is guaranteed to be non-null; default is Message::Messenger().
        """
    def NbMapped(self) -> int: 
        """
        Returns the maximum possible value for Map Index (no result can be bound with a value greater than it)
        """
    def NbRoots(self) -> int: 
        """
        Returns the count of recorded Roots
        """
    def NestingLevel(self) -> int: 
        """
        Returns Nesting Level of Transfers (managed by methods TranscriptWith & Co). Starts to zero. If no automatic Transfer is used, it remains to zero. Zero means Root Level.
        """
    def PrintTrace(self,start : OCP.Standard.Standard_Transient,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints a short information on a starting object. By default prints its Dynamic Type. Can be redefined
        """
    def Rebind(self,start : OCP.Standard.Standard_Transient,binder : Transfer_Binder) -> None: 
        """
        Changes the Binder linked with a starting Object for its unitary transfer. This it can be useful when the exact form of the result is known once the transfer is widely engaged. This can be done only on first transfer. Considers a category number, by default 0
        """
    def Recognize(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Tells if <start> has been recognized as good candidate for Transfer. i.e. queries the Actor and its Nexts
        """
    def RemoveResult(self,start : OCP.Standard.Standard_Transient,level : int,compute : bool=True) -> None: 
        """
        Removes Results attached to (== Unbinds) a given object and, according <level> : <level> = 0 : only it <level> = 1 : it plus its immediately owned sub-results(scope) <level> = 2 : it plus all its owned sub-results(scope)
        """
    def ResetNestingLevel(self) -> None: 
        """
        Resets Nesting Level of Transfers to Zero (Root Level), whatever its current value.
        """
    def Resize(self,nb : int) -> None: 
        """
        Resizes the Map as required (if a new reliable value has been determined). Acts only if <nb> is greater than actual NbMapped
        """
    def ResultOne(self,start : OCP.Standard.Standard_Transient,level : int,withstart : bool=False) -> Transfer_IteratorOfProcessForTransient: 
        """
        Returns, as an Iterator, the log of transfer for one object <level> = 0 : this object only and if <start> is a scope owner (else, <level> is ignored) : <level> = 1 : object plus its immediate scoped ones <level> = 2 : object plus all its scoped ones
        """
    def Root(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns a Root Entity given its number in the list (1-NbRoots)
        """
    def RootIndex(self,start : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the index in the list of roots for a starting item, or 0 if it is not recorded as a root
        """
    def RootItem(self,num : int) -> Transfer_Binder: 
        """
        Returns the Binder bound with a Root Entity given its number Considers a category number, by default 0
        """
    def RootResult(self,withstart : bool=False) -> Transfer_IteratorOfProcessForTransient: 
        """
        Returns, as an iterator, the log of root transfer, i.e. the created objects and Binders bound to starting roots If withstart is given True, Starting Objets are also returned
        """
    def SendFail(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddFail (Msg)
        """
    def SendMsg(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Adds an information message Trace is filled if trace level is at least 3
        """
    def SendWarning(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddWarning (Msg)
        """
    def SetActor(self,actor : Transfer_ActorOfProcessForTransient) -> None: 
        """
        Defines an Actor, which is used for automatic Transfer If already defined, the new Actor is cumulated (see SetNext from Actor)
        """
    def SetErrorHandle(self,err : bool) -> None: 
        """
        Allows controls if exceptions will be handled Transfer Operations <err> False : they are not handled with try {} catch {} <err> True : they are Default is False: no handling performed
        """
    def SetMessenger(self,messenger : OCP.Message.Message_Messenger) -> None: 
        """
        Sets Messenger used for outputting messages.
        """
    def SetProgress(self,theProgress : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Sets Progress indicator
        """
    def SetRoot(self,start : OCP.Standard.Standard_Transient) -> None: 
        """
        Declares <obj> (and its Result) as Root. This status will be later exploited by RootResult, see below (Result can be produced at any time)
        """
    def SetRootManagement(self,stat : bool) -> None: ...
    def SetTraceLevel(self,tracelev : int) -> None: 
        """
        Sets trace level used for outputting messages: <trace> = 0 : no trace at all <trace> = 1 : handled exceptions and calls to AddError <trace> = 2 : also calls to AddWarning <trace> = 3 : also traces new Roots (uses method ErrorTrace). Default is 1 : Errors traced
        """
    def StartTrace(self,binder : Transfer_Binder,start : OCP.Standard.Standard_Transient,level : int,mode : int) -> None: 
        """
        Method called when trace is asked Calls PrintTrace to display information relevant for starting objects (which can be redefined) <level> is Nesting Level of Transfer (0 = root) <mode> controls the way the trace is done : 0 neutral, 1 for Error, 2 for Warning message, 3 for new Root
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceLevel(self) -> int: 
        """
        Returns trace level used for outputting messages.
        """
    def Transfer(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Same as Transferring but does not return the Binder. Simply returns True in case of success (for user call)
        """
    def Transferring(self,start : OCP.Standard.Standard_Transient) -> Transfer_Binder: 
        """
        Performs the Transfer of a Starting Object, by calling the method TransferProduct (see below). Mapping and Roots are managed : nothing is done if a Result is already Bound, an exception is raised in case of error.
        """
    def Unbind(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Removes the Binder linked with a starting object If this Binder brings a non-empty Check, it is replaced by a VoidBinder. Also removes from the list of Roots as required. Returns True if done, False if <start> was not bound Considers a category number, by default 0
        """
    @overload
    def __init__(self,nb : int=10000) -> None: ...
    @overload
    def __init__(self,printer : OCP.Message.Message_Messenger,nb : int=10000) -> None: ...
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
class Transfer_ResultFromModel(OCP.Standard.Standard_Transient):
    """
    ResultFromModel is used to store a final result stored in a TransientProcess, respectfully to its structuration in scopes by using a set of ResultFromTransient Hence, it can be regarded as a passive equivalent of the stored data in the TransientProcess, while an Iterator gives a flat view of it.ResultFromModel is used to store a final result stored in a TransientProcess, respectfully to its structuration in scopes by using a set of ResultFromTransient Hence, it can be regarded as a passive equivalent of the stored data in the TransientProcess, while an Iterator gives a flat view of it.ResultFromModel is used to store a final result stored in a TransientProcess, respectfully to its structuration in scopes by using a set of ResultFromTransient Hence, it can be regarded as a passive equivalent of the stored data in the TransientProcess, while an Iterator gives a flat view of it.
    """
    def CheckList(self,erronly : bool,level : int=2) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the check-list of this set of results <erronly> true : only fails are considered <level> = 0 : considers only main binder <level> = 1 : considers main binder plus immediate subs <level> = 2 (D) : considers all checks
        """
    def CheckStatus(self) -> OCP.Interface.Interface_CheckStatus: 
        """
        Returns the check status with corresponds to the content of this ResultFromModel; considers all levels of transfer (worst status). Returns CheckAny if not yet computed Reads it from recorded status if already computed, else recomputes one
        """
    def CheckedList(self,check : OCP.Interface.Interface_CheckStatus,result : bool) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of starting entities to which a check status is attached. <check> = -2 , all entities whatever the check (see result) <check> = -1 , entities with no fail (warning allowed) <check> = 0 , entities with no check at all <check> = 1 , entities with warning but no fail <check> = 2 , entities with fail <result> : if True, only entities with an attached result Remark : result True and check=0 will give an empty list
        """
    def ComputeCheckStatus(self,enforce : bool) -> OCP.Interface.Interface_CheckStatus: 
        """
        Computes and records check status (see CheckStatus) Does not computes it if already done and <enforce> False
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
    def FileName(self) -> str: 
        """
        Returns starting File Name (empty if not set)
        """
    def Fill(self,TP : Transfer_TransientProcess,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Fills from a TransientProcess, with the result attached to a starting entity. Considers its Model if it is set. This action produces a structured set of ResultFromTransient, considering scopes, starting by that of <ent>. If <ent> has no recorded result, it remains empty Returns True if a result is recorded, False else
        """
    def FillBack(self,TP : Transfer_TransientProcess) -> None: 
        """
        Fills back a TransientProcess from the structured set of binders. Also sets the Model.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasResult(self) -> bool: 
        """
        Returns True if a Result is recorded
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
    def MainLabel(self) -> str: 
        """
        Returns the label in starting model attached to main entity (updated by Fill or SetMainResult, if Model is known)
        """
    def MainNumber(self) -> int: 
        """
        Returns the label in starting model attached to main entity
        """
    def MainResult(self) -> Transfer_ResultFromTransient: 
        """
        Returns the main recorded ResultFromTransient, or a null
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns starting Model (null if not set)
        """
    def ResultFromKey(self,start : OCP.Standard.Standard_Transient) -> Transfer_ResultFromTransient: 
        """
        Searches for a key (starting entity) and returns its result Returns a null handle if not found
        """
    def Results(self,level : int) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Internal method which returns the list of ResultFromTransient, according level (2:complete; 1:sub-level 1; 0:main only)
        """
    def SetFileName(self,filename : str) -> None: 
        """
        Sets starting File Name
        """
    def SetMainResult(self,amain : Transfer_ResultFromTransient) -> None: 
        """
        Sets a new value for the main recorded ResultFromTransient
        """
    def SetModel(self,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Sets starting Model
        """
    def Strip(self,mode : int) -> None: 
        """
        Clears some data attached to binders used by TransientProcess, which become useless once the transfer has been done, by calling Strip on its ResultFromTransient
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransferredList(self,level : int=2) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of recorded starting entities, ending by the root. Entities with check but no transfer result are ignored <level> = 2 (D), considers the complete list <level> = 1 considers the main result plus immediate subs <level> = 0 just the main result
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
class Transfer_ResultFromTransient(OCP.Standard.Standard_Transient):
    """
    This class, in conjunction with ResultFromModel, allows to record the result of a transfer initially stored in a TransientProcess.This class, in conjunction with ResultFromModel, allows to record the result of a transfer initially stored in a TransientProcess.This class, in conjunction with ResultFromModel, allows to record the result of a transfer initially stored in a TransientProcess.
    """
    def AddSubResult(self,sub : Transfer_ResultFromTransient) -> None: 
        """
        Adds a sub-result
        """
    def Binder(self) -> Transfer_Binder: 
        """
        Returns the binder
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns the check (or an empty one if no binder)
        """
    def CheckStatus(self) -> OCP.Interface.Interface_CheckStatus: 
        """
        Returns the check status
        """
    def ClearSubs(self) -> None: 
        """
        Clears the list of (immediate) sub-results
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
    def Fill(self,TP : Transfer_TransientProcess) -> None: 
        """
        Fills from a TransientProcess, with the starting entity which must have been set before. It works with scopes, calls Fill on each of its sub-results
        """
    def FillBack(self,TP : Transfer_TransientProcess) -> None: 
        """
        Fills back a TransientProcess with definition of a ResultFromTransient, respectfully to its structuration in scopes
        """
    def FillMap(self,map : OCP.TColStd.TColStd_IndexedMapOfTransient) -> None: 
        """
        This method is used by ResultFromModel to collate the list of ResultFromTransient, avoiding duplications with a map Remark : <me> is already in the map and has not to be bound
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasResult(self) -> bool: 
        """
        Returns True if a result is recorded
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
    def NbSubResults(self) -> int: 
        """
        Returns the count of recorded sub-results
        """
    def ResultFromKey(self,key : OCP.Standard.Standard_Transient) -> Transfer_ResultFromTransient: 
        """
        Returns the ResultFromTransient attached to a given starting entity (the key). Returns a null handle if not found
        """
    def SetBinder(self,binder : Transfer_Binder) -> None: 
        """
        Sets Binder (for result plus individual check)
        """
    def SetStart(self,start : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets starting entity
        """
    def Start(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the starting entity
        """
    def Strip(self) -> None: 
        """
        Clears some data attached to binders used by TransientProcess, which become useless once the transfer has been done : the list of sub-scoped binders, which is now recorded as sub-results
        """
    def SubResult(self,num : int) -> Transfer_ResultFromTransient: 
        """
        Returns a sub-result, given its rank
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
class Transfer_HSequenceOfBinder(Transfer_SequenceOfBinder, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : Transfer_SequenceOfBinder) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : Transfer_Binder) -> None: ...
    def Assign(self,theOther : Transfer_SequenceOfBinder) -> Transfer_SequenceOfBinder: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Transfer_Binder: 
        """
        First item access
        """
    def ChangeLast(self) -> Transfer_Binder: 
        """
        Last item access
        """
    def ChangeSequence(self) -> Transfer_SequenceOfBinder: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> Transfer_Binder: 
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
    def First(self) -> Transfer_Binder: 
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
    def InsertAfter(self,theIndex : int,theSeq : Transfer_SequenceOfBinder) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Transfer_Binder) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Transfer_Binder) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Transfer_SequenceOfBinder) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> Transfer_Binder: 
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
    def Prepend(self,theSeq : Transfer_SequenceOfBinder) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Transfer_Binder) -> None: ...
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
    def Sequence(self) -> Transfer_SequenceOfBinder: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : Transfer_Binder) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Transfer_SequenceOfBinder) -> None: 
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
    def Value(self,theIndex : int) -> Transfer_Binder: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Transfer_SequenceOfBinder) -> None: ...
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
class Transfer_HSequenceOfFinder(Transfer_SequenceOfFinder, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Transfer_Finder) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : Transfer_SequenceOfFinder) -> None: ...
    def Assign(self,theOther : Transfer_SequenceOfFinder) -> Transfer_SequenceOfFinder: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Transfer_Finder: 
        """
        First item access
        """
    def ChangeLast(self) -> Transfer_Finder: 
        """
        Last item access
        """
    def ChangeSequence(self) -> Transfer_SequenceOfFinder: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> Transfer_Finder: 
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
    def First(self) -> Transfer_Finder: 
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
    def InsertAfter(self,theIndex : int,theSeq : Transfer_SequenceOfFinder) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Transfer_Finder) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Transfer_SequenceOfFinder) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Transfer_Finder) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> Transfer_Finder: 
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
    def Prepend(self,theItem : Transfer_Finder) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Transfer_SequenceOfFinder) -> None: ...
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
    def Sequence(self) -> Transfer_SequenceOfFinder: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : Transfer_Finder) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Transfer_SequenceOfFinder) -> None: 
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
    def Value(self,theIndex : int) -> Transfer_Finder: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Transfer_SequenceOfFinder) -> None: ...
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
class Transfer_BinderOfTransientInteger(Transfer_SimpleBinderOfTransient, Transfer_Binder, OCP.Standard.Standard_Transient):
    """
    This type of Binder allows to attach as result, besides a Transient Object, an Integer Value, which can be an Index in the Object if it defines a List, for instanceThis type of Binder allows to attach as result, besides a Transient Object, an Integer Value, which can be an Index in the Object if it defines a List, for instanceThis type of Binder allows to attach as result, besides a Transient Object, an Integer Value, which can be an Index in the Object if it defines a List, for instance
    """
    def AddFail(self,mess : str,orig : str='') -> None: 
        """
        Used to declare an individual transfer as beeing erroneous (Status is set to Void, StatusExec is set to Error, <errmess> is added to Check's list of Fails) It is possible to record several messages of error
        """
    def AddResult(self,next : Transfer_Binder) -> None: 
        """
        Adds a next result (at the end of the list) Remark : this information is not processed by Merge
        """
    def AddWarning(self,mess : str,orig : str='') -> None: 
        """
        Used to attach a Warning Message to an individual Transfer It has no effect on the Status
        """
    def CCheck(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages, in order to modify it (adding messages, or replacing it)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages Note that no Entity is associated in this Check
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
    @staticmethod
    def GetTypedResult_s(bnd : Transfer_Binder,atype : OCP.Standard.Standard_Type,res : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns a transient result according to its type (IsKind) i.e. the result itself if IsKind(atype), else searches in NextResult, until first found, then returns True If not found, returns False (res is NOT touched)
        """
    def HasResult(self) -> bool: 
        """
        Returns True if a Result is available (StatusResult = Defined) A Unique Result will be gotten by Result (which must be defined in each sub-class according to result type) For a Multiple Result, see class MultipleBinder For other case, specific access has to be forecast
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Integer(self) -> int: 
        """
        Returns the value set for the integer part
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
    def IsMultiple(self) -> bool: 
        """
        Returns True if a Binder has several results, either by itself or because it has next results Can be defined by sub-classes.
        """
    def Merge(self,other : Transfer_Binder) -> None: 
        """
        Merges basic data (Check, ExecStatus) from another Binder but keeps its result. Used when a binder is replaced by another one, this allows to keep messages
        """
    def NextResult(self) -> Transfer_Binder: 
        """
        Returns the next result, Null if none
        """
    def Result(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the defined Result, if there is one
        """
    def ResultType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Result (Standard_Transient if no Result is defined)
        """
    def ResultTypeName(self) -> str: 
        """
        Returns the Effective Name of (Dynamic) Type of the Result (void) if no result is defined
        """
    def SetAlreadyUsed(self) -> None: 
        """
        Declares that result is now used by another one, it means that it cannot be modified (by Rebind)
        """
    def SetInteger(self,value : int) -> None: 
        """
        Sets a value for the integer part
        """
    def SetResult(self,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Defines the Result
        """
    def SetStatusExec(self,stat : Transfer_StatusExec) -> None: 
        """
        Modifies execution status; called by TransferProcess only (for StatusError, rather use SetError, below)
        """
    def Status(self) -> Transfer_StatusResult: 
        """
        Returns status, which can be Initial (not yet done), Made (a result is recorded, not yet shared), Used (it is shared and cannot be modified)
        """
    def StatusExec(self) -> Transfer_StatusExec: 
        """
        Returns execution status
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
class Transfer_StatusExec():
    """
    execution status of an individual transfer (see Transcriptor)

    Members:

      Transfer_StatusInitial

      Transfer_StatusRun

      Transfer_StatusDone

      Transfer_StatusError

      Transfer_StatusLoop
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Transfer_StatusDone: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusDone
    Transfer_StatusError: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusError
    Transfer_StatusInitial: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusInitial
    Transfer_StatusLoop: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusLoop
    Transfer_StatusRun: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusRun
    __entries: dict # value = {'Transfer_StatusInitial': (Transfer_StatusExec.Transfer_StatusInitial, None), 'Transfer_StatusRun': (Transfer_StatusExec.Transfer_StatusRun, None), 'Transfer_StatusDone': (Transfer_StatusExec.Transfer_StatusDone, None), 'Transfer_StatusError': (Transfer_StatusExec.Transfer_StatusError, None), 'Transfer_StatusLoop': (Transfer_StatusExec.Transfer_StatusLoop, None)}
    __members__: dict # value = {'Transfer_StatusInitial': Transfer_StatusExec.Transfer_StatusInitial, 'Transfer_StatusRun': Transfer_StatusExec.Transfer_StatusRun, 'Transfer_StatusDone': Transfer_StatusExec.Transfer_StatusDone, 'Transfer_StatusError': Transfer_StatusExec.Transfer_StatusError, 'Transfer_StatusLoop': Transfer_StatusExec.Transfer_StatusLoop}
    pass
class Transfer_StatusResult():
    """
    result status of transferring an entity (see Transcriptor)

    Members:

      Transfer_StatusVoid

      Transfer_StatusDefined

      Transfer_StatusUsed
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Transfer_StatusDefined: OCP.Transfer.Transfer_StatusResult # value = Transfer_StatusResult.Transfer_StatusDefined
    Transfer_StatusUsed: OCP.Transfer.Transfer_StatusResult # value = Transfer_StatusResult.Transfer_StatusUsed
    Transfer_StatusVoid: OCP.Transfer.Transfer_StatusResult # value = Transfer_StatusResult.Transfer_StatusVoid
    __entries: dict # value = {'Transfer_StatusVoid': (Transfer_StatusResult.Transfer_StatusVoid, None), 'Transfer_StatusDefined': (Transfer_StatusResult.Transfer_StatusDefined, None), 'Transfer_StatusUsed': (Transfer_StatusResult.Transfer_StatusUsed, None)}
    __members__: dict # value = {'Transfer_StatusVoid': Transfer_StatusResult.Transfer_StatusVoid, 'Transfer_StatusDefined': Transfer_StatusResult.Transfer_StatusDefined, 'Transfer_StatusUsed': Transfer_StatusResult.Transfer_StatusUsed}
    pass
class Transfer_TransferDeadLoop(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Transfer', '__weakref__': <attribute '__weakref__' of 'Transfer_TransferDeadLoop' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Transfer_TransferDeadLoop' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Transfer_TransferDispatch(OCP.Interface.Interface_CopyTool):
    """
    A TransferDispatch is aimed to dispatch Entities between two Interface Models, by default by copying them, as CopyTool, but with more capabilities of adapting : Copy is redefined to firstly pass the hand to a TransferProcess. If this gives no result, standard Copy is called.
    """
    def Bind(self,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Defines a Result for the Transfer of a Starting object. Used by method Transferred (which performs a normal Copy), but can also be called to enforce a result : in the latter case, the enforced result must be compatible with the other Transfers which are performed
        """
    def Clear(self) -> None: 
        """
        Clears Transfer List. Gets Ready to begin another Transfer
        """
    def ClearLastFlags(self) -> None: 
        """
        Clears LastFlags only. This allows to know what Entities are copied after its call (see method LastCopiedAfter). It can be used when copies are done by increments, which must be distinghished. ClearLastFlags is also called by Clear.
        """
    def CompleteResult(self,withreports : bool=False) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the complete list of copied Entities If <withreports> is given True, the entities which were reported in the Starting Model are replaced in the list by the copied ReportEntities
        """
    def Control(self) -> OCP.Interface.Interface_CopyControl: 
        """
        Returns the object used for Control
        """
    def Copy(self,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,mapped : bool,errstat : bool) -> bool: 
        """
        Copies an Entity by calling the method Transferring from the TransferProcess. If this called produces a Null Binder, then the standard, inherited Copy is called
        """
    def FillModel(self,bmodel : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Fills a Model with the result of the transfer (TransferList) Commands copy of Header too, and calls RenewImpliedRefs
        """
    def LastCopiedAfter(self,numfrom : int,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns an copied Entity and its Result which were operated after last call to ClearLastFlags. It returns the first "Last Copied Entity" which Number follows <numfrom>, Zero if none. It is used in a loop as follow : Integer num = 0; while ( (num = CopyTool.LastCopiedAfter(num,ent,res)) ) { .. Process Starting <ent> and its Result <res> }
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model on which the CopyTool works
        """
    def RenewImpliedRefs(self) -> None: 
        """
        Renews the Implied References. These References do not involve Copying of referenced Entities. For such a Reference, if the Entity which defines it AND the referenced Entity are both copied, then this Reference is renewed. Else it is deleted in the copied Entities. Remark : this concerns only some specific references, such as "back pointers".
        """
    def RootResult(self,withreports : bool=False) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of Root copied Entities (those which were asked for copy by the user of CopyTool, not by copying another Entity)
        """
    def Search(self,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> bool: 
        """
        Search for the result of a Starting Object (i.e. an Entity) Returns True if a Result is Bound (and fills "result") Returns False if no result is Bound
        """
    def SetControl(self,othermap : OCP.Interface.Interface_CopyControl) -> None: 
        """
        Changes the Map of Result for another one. This allows to work with a more sophisticated Mapping Control than the Standard one which is CopyMap (e.g. TransferProcess from Transfer)
        """
    def TransferEntity(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Transfers one Entity and records result into the Transfer List Calls method Transferred
        """
    def Transferred(self,ent : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: 
        """
        Transfers one Entity, if not yet bound to a result Remark : For an Entity which is reported in the Starting Model, the ReportEntity will also be copied with its Content if it has one (at least ShallowCopy; Complete Copy if the Protocol recognizes the Content : see method Copy)
        """
    def TransientProcess(self) -> Transfer_TransientProcess: 
        """
        Returns the content of Control Object, as a TransientProcess
        """
    @overload
    def __init__(self,amodel : OCP.Interface.Interface_InterfaceModel,lib : OCP.Interface.Interface_GeneralLib) -> None: ...
    @overload
    def __init__(self,amodel : OCP.Interface.Interface_InterfaceModel) -> None: ...
    @overload
    def __init__(self,amodel : OCP.Interface.Interface_InterfaceModel,protocol : OCP.Interface.Interface_Protocol) -> None: ...
    pass
class Transfer_TransferFailure(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Transfer', '__weakref__': <attribute '__weakref__' of 'Transfer_TransferFailure' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Transfer_TransferFailure' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Transfer_TransferInput():
    """
    A TransferInput is a Tool which fills an InterfaceModel with the result of the Transfer of CasCade Objects, once determined The Result comes from a TransferProcess, either from Transient (the Complete Result is considered, it must contain only Transient Objects)
    """
    def Entities(self,list : Transfer_TransferIterator) -> OCP.Interface.Interface_EntityIterator: 
        """
        Takes the transient items stored in a TransferIterator
        """
    @overload
    def FillModel(self,proc : Transfer_TransientProcess,amodel : OCP.Interface.Interface_InterfaceModel,proto : OCP.Interface.Interface_Protocol,roots : bool=True) -> None: 
        """
        Fills an InterfaceModel with the Complete Result of a Transfer stored in a TransientProcess (Starting Objects are Transient) The complete result is exactly added to the model

        Fills an InterfaceModel with results of the Transfer recorded in a TransientProcess (Starting Objects are Transient) : Root Result if <roots> is True (Default), Complete Result else The entities added to the model are determined from the result by by adding the referenced entities

        Fills an InterfaceModel with the Complete Result of a Transfer stored in a TransientProcess (Starting Objects are Transient) The complete result is exactly added to the model

        Fills an InterfaceModel with results of the Transfer recorded in a TransientProcess (Starting Objects are Transient) : Root Result if <roots> is True (Default), Complete Result else The entities added to the model are determined from the result by by adding the referenced entities
        """
    @overload
    def FillModel(self,proc : Transfer_FinderProcess,amodel : OCP.Interface.Interface_InterfaceModel) -> None: ...
    @overload
    def FillModel(self,proc : Transfer_TransientProcess,amodel : OCP.Interface.Interface_InterfaceModel) -> None: ...
    @overload
    def FillModel(self,proc : Transfer_FinderProcess,amodel : OCP.Interface.Interface_InterfaceModel,proto : OCP.Interface.Interface_Protocol,roots : bool=True) -> None: ...
    def __init__(self) -> None: ...
    pass
class Transfer_IteratorOfProcessForFinder(Transfer_TransferIterator):
    """
    None
    """
    @overload
    def Add(self,binder : Transfer_Binder) -> None: 
        """
        Adds a Binder to the iteration list (construction) with no corresponding Starting Object (note that Result is brought by Binder)

        Adds a Binder to the iteration list, associated with its corresponding Starting Object "start" Starting Object is ignored if not required at Creation time
        """
    @overload
    def Add(self,binder : Transfer_Binder,start : Transfer_Finder) -> None: ...
    def AddItem(self,atr : Transfer_Binder) -> None: 
        """
        Adds a Binder to the iteration list (construction)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check associated to current Binder (in case of error, it brings Fail messages) (in case of warnings, it brings Warning messages)
        """
    def Filter(self,list : Transfer_HSequenceOfFinder,keep : bool=True) -> None: 
        """
        After having added all items, keeps or rejects items which are attached to starting data given by <only> <keep> = True (D) : keeps. <keep> = False : rejects Does nothing if <withstarts> was False
        """
    def HasFails(self) -> bool: 
        """
        Returns True if Fail Messages are recorded with the current Binder. They can then be read through Check (see below)
        """
    def HasResult(self) -> bool: 
        """
        Returns True if current Item brings a Result, Transient (Handle) or not or Multiple. That is to say, if it corresponds to a normally acheived Transfer, Transient Result is read by specific TransientResult below. Other kind of Result must be read specifically from its Binder
        """
    def HasStarting(self) -> bool: 
        """
        Returns True if Starting Object is available (defined at Creation Time)
        """
    def HasTransientResult(self) -> bool: 
        """
        Returns True if the current Item has a Transient Unique Result (if yes, use TransientResult to get it)
        """
    def HasUniqueResult(self) -> bool: 
        """
        Returns True if Current Item has a Unique Result
        """
    def HasWarnings(self) -> bool: 
        """
        Returns True if Warning Messages are recorded with the current Binder. They can then be read through Check (see below)
        """
    def More(self) -> bool: 
        """
        Returns True if there are other Items to iterate
        """
    def Next(self) -> None: 
        """
        Sets Iteration to the next Item
        """
    def Number(self) -> int: 
        """
        Returns count of Binders to be iterated
        """
    def ResultType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type of the Result of the current Item, if Unique. If No Unique Result (Error Transfert or Multiple Result), returns a Null Handle The Type is : the Dynamic Type for a Transient Result, the Type defined by the Binder Class else
        """
    def SelectBinder(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects Items on the Type of Binder : keep only Binders which are of a given Type (if keep is True) or reject only them (if keep is False)
        """
    def SelectItem(self,num : int,keep : bool) -> None: 
        """
        Selects/Unselect (according to <keep> an item designated by its rank <num> in the list Used by sub-classes which have specific criteria
        """
    def SelectResult(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects Items on the Type of Result. Considers only Unique Results. Considers Dynamic Type for Transient Result, Static Type (the one given to define the Binder) else.
        """
    def SelectUnique(self,keep : bool) -> None: 
        """
        Select Items according Unicity : keep only Unique Results (if keep is True) or keep only Multiple Results (if keep is False)
        """
    def Start(self) -> None: 
        """
        Clears Iteration in progress, to allow it to be restarted
        """
    def Starting(self) -> Transfer_Finder: 
        """
        Returns corresponding Starting Object
        """
    def Status(self) -> Transfer_StatusExec: 
        """
        Returns Execution Status of current Binder Normal transfer corresponds to StatusDone
        """
    def TransientResult(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Transient Result of the current Item if there is (else, returns a null Handle) Supposes that Binding is done by a SimpleBinderOfTransient
        """
    def Value(self) -> Transfer_Binder: 
        """
        Returns the current Binder
        """
    def __init__(self,withstarts : bool) -> None: ...
    pass
class Transfer_TransferOutput():
    """
    A TransferOutput is a Tool which manages the transfer of entities created by an Interface, stored in an InterfaceModel, into a set of Objects suitable for an Application Objects to be transferred are given, by method Transfer (which calls Transfer from TransientProcess) A default action is available to get all roots of the Model Result is given as a TransferIterator (see TransferProcess) Also, it is possible to pilot directly the TransientProcess
    """
    def ListForStatus(self,normal : bool,roots : bool=True) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of Starting Entities with these criteria : - <normal> False, gives the entities bound with ABNORMAL STATUS (e.g. : Fail recorded, Exception raised during Transfer) - <normal> True, gives Entities with or without a Result, but with no Fail, no Exception (Warnings are not counted) - <roots> False, considers all entities recorded (either for Result, or for at least one Fail or Warning message) - <roots> True (Default), considers only roots of Transfer (the Entities recorded at highest level) This method is based on AbnormalResult from TransferProcess
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Starting Model
        """
    def ModelForStatus(self,protocol : OCP.Interface.Interface_Protocol,normal : bool,roots : bool=True) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Fills a Model with the list determined by ListForStatus This model starts from scratch (made by NewEmptyModel from the current Model), then is filled by AddWithRefs
        """
    def Transfer(self,obj : OCP.Standard.Standard_Transient) -> None: 
        """
        Transfer checks that all taken Entities come from the same Model, then calls Transfer from TransientProcess
        """
    @overload
    def TransferRoots(self) -> None: 
        """
        Runs transfer on the roots of the Interface Model The Roots are computed with a ShareFlags created from a Protocol given as Argument

        Runs transfer on the roots defined by a Graph of dependences (which detains also a Model and its Entities) Roots are computed with a ShareFlags created from the Graph

        Runs transfer on the roots of the Interface Model Remark : the Roots are computed with a ShareFlags created from the Active Protocol
        """
    @overload
    def TransferRoots(self,protocol : OCP.Interface.Interface_Protocol) -> None: ...
    @overload
    def TransferRoots(self,G : OCP.Interface.Interface_Graph) -> None: ...
    def TransientProcess(self) -> Transfer_TransientProcess: 
        """
        Returns the TransientProcess used to work
        """
    @overload
    def __init__(self,proc : Transfer_TransientProcess,amodel : OCP.Interface.Interface_InterfaceModel) -> None: ...
    @overload
    def __init__(self,actor : Transfer_ActorOfTransientProcess,amodel : OCP.Interface.Interface_InterfaceModel) -> None: ...
    pass
class Transfer_TransientListBinder(Transfer_Binder, OCP.Standard.Standard_Transient):
    """
    This binder binds several (a list of) Transients with a starting entity, when this entity itself corresponds to a simple list of Transients. Each part is not seen as a sub-result of an independant componant, but as an item of a built-in listThis binder binds several (a list of) Transients with a starting entity, when this entity itself corresponds to a simple list of Transients. Each part is not seen as a sub-result of an independant componant, but as an item of a built-in listThis binder binds several (a list of) Transients with a starting entity, when this entity itself corresponds to a simple list of Transients. Each part is not seen as a sub-result of an independant componant, but as an item of a built-in list
    """
    def AddFail(self,mess : str,orig : str='') -> None: 
        """
        Used to declare an individual transfer as beeing erroneous (Status is set to Void, StatusExec is set to Error, <errmess> is added to Check's list of Fails) It is possible to record several messages of error
        """
    def AddResult(self,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an item to the result list
        """
    def AddWarning(self,mess : str,orig : str='') -> None: 
        """
        Used to attach a Warning Message to an individual Transfer It has no effect on the Status
        """
    def CCheck(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages, in order to modify it (adding messages, or replacing it)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages Note that no Entity is associated in this Check
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
    def HasResult(self) -> bool: 
        """
        Returns True if a Result is available (StatusResult = Defined) A Unique Result will be gotten by Result (which must be defined in each sub-class according to result type) For a Multiple Result, see class MultipleBinder For other case, specific access has to be forecast
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
    def IsMultiple(self) -> bool: 
        """
        None
        """
    def Merge(self,other : Transfer_Binder) -> None: 
        """
        Merges basic data (Check, ExecStatus) from another Binder but keeps its result. Used when a binder is replaced by another one, this allows to keep messages
        """
    def NbTransients(self) -> int: 
        """
        None
        """
    def NextResult(self) -> Transfer_Binder: 
        """
        Returns the next result, Null if none
        """
    def Result(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        None
        """
    def ResultType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ResultTypeName(self) -> str: 
        """
        None
        """
    def SetAlreadyUsed(self) -> None: 
        """
        Declares that result is now used by another one, it means that it cannot be modified (by Rebind)
        """
    def SetResult(self,num : int,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Changes an already defined sub-result
        """
    def SetStatusExec(self,stat : Transfer_StatusExec) -> None: 
        """
        Modifies execution status; called by TransferProcess only (for StatusError, rather use SetError, below)
        """
    def Status(self) -> Transfer_StatusResult: 
        """
        Returns status, which can be Initial (not yet done), Made (a result is recorded, not yet shared), Used (it is shared and cannot be modified)
        """
    def StatusExec(self) -> Transfer_StatusExec: 
        """
        Returns execution status
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transient(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: ...
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
class Transfer_TransientMapper(Transfer_Finder, OCP.Standard.Standard_Transient):
    def AttrList(self) -> Any: 
        """
        Returns the exhaustive list of attributes
        """
    def Attribute(self,name : str) -> OCP.Standard.Standard_Transient: 
        """
        Returns an attribute from its name. Null Handle if not recorded (whatever Transient, Integer, Real ...)
        """
    def AttributeType(self,name : str) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the type of an attribute : ParamInt , ParamReal , ParamText (String) , ParamIdent (any) or ParamVoid (not recorded)
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
    def Equates(self,other : Transfer_Finder) -> bool: 
        """
        Specific testof equallity : defined as False if <other> has not the same true Type, else contents are compared (by C++ operator ==)
        """
    def GetAttribute(self,name : str,type : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns an attribute from its name, filtered by a type If no attribute has this name, or if it is not kind of this type, <val> is Null and returned value is False Else, it is True
        """
    def GetAttributes(self,other : Transfer_Finder,fromname : str='',copied : bool=True) -> None: 
        """
        Gets the list of attributes from <other>, by copying it By default, considers all the attributes from <other> If <fromname> is given, considers only the attributes with name beginning by <fromname>
        """
    def GetHashCode(self) -> int: 
        """
        Returns the HashCode which has been stored by SetHashCode (remark that HashCode could be deferred then be defined by sub-classes, the result is the same)
        """
    def GetIntegerAttribute(self,name : str,val : int) -> bool: 
        """
        Returns an attribute from its name, as integer If no attribute has this name, or not an integer, <val> is 0 and returned value is False Else, it is True
        """
    def GetRealAttribute(self,name : str,val : float) -> bool: 
        """
        Returns an attribute from its name, as real If no attribute has this name, or not a real <val> is 0.0 and returned value is False Else, it is True
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IntegerAttribute(self,name : str) -> int: 
        """
        Returns an integer attribute from its name. 0 if not recorded
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
    def RealAttribute(self,name : str) -> float: 
        """
        Returns a real attribute from its name. 0.0 if not recorded
        """
    def RemoveAttribute(self,name : str) -> bool: 
        """
        Removes an attribute Returns True when done, False if this attribute did not exist
        """
    def SameAttributes(self,other : Transfer_Finder) -> None: 
        """
        Gets the list of attributes from <other>, as such, i.e. not copied : attributes are shared, any attribute edited, added, or removed in <other> is also in <me> and vice versa The former list of attributes of <me> is dropped
        """
    def SetAttribute(self,name : str,val : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an attribute with a given name (replaces the former one with the same name if already exists)
        """
    def SetIntegerAttribute(self,name : str,val : int) -> None: 
        """
        Adds an integer value for an attribute
        """
    def SetRealAttribute(self,name : str,val : float) -> None: 
        """
        Adds a real value for an attribute
        """
    def SetStringAttribute(self,name : str,val : str) -> None: 
        """
        Adds a String value for an attribute
        """
    def StringAttribute(self,name : str) -> str: 
        """
        Returns a String attribute from its name. "" if not recorded
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the contained value
        """
    def ValueType(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Type of the Value. By default, returns the DynamicType of <me>, but can be redefined
        """
    def ValueTypeName(self) -> str: 
        """
        Returns the name of the Type of the Value. Default is name of ValueType, unless it is for a non-handled object
        """
    def __init__(self,akey : OCP.Standard.Standard_Transient) -> None: ...
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
class Transfer_TransientProcess(Transfer_ProcessForTransient, OCP.Standard.Standard_Transient):
    """
    Adds specific features to the generic definition : TransientProcess is intended to work from an InterfaceModel to a set of application objects.Adds specific features to the generic definition : TransientProcess is intended to work from an InterfaceModel to a set of application objects.Adds specific features to the generic definition : TransientProcess is intended to work from an InterfaceModel to a set of application objects.
    """
    def AbnormalResult(self) -> Transfer_IteratorOfProcessForTransient: 
        """
        Returns Binders which are neither "Done" nor "Initial", that is Error,Loop or Run (abnormal states at end of Transfer) Starting Objects are given in correspondance in the iterator
        """
    def Actor(self) -> Transfer_ActorOfProcessForTransient: 
        """
        Returns the defined Actor. Returns a Null Handle if not set.
        """
    def AddError(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: 
        """
        (other name of AddFail, maintained for compatibility)
        """
    @overload
    def AddFail(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: 
        """
        Adds an Error message to a starting entity (to the check of its Binder of category 0, as a Fail)

        Adds an Error Message to a starting entity from the definition of a Msg (Original+Value)
        """
    @overload
    def AddFail(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: ...
    def AddMultiple(self,start : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an item to a list of results bound to a starting object. Considers a category number, by default 0, for all results
        """
    @overload
    def AddWarning(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Adds a Warning message to a starting entity (to the check of its Binder of category 0)

        Adds a Warning Message to a starting entity from the definition of a Msg (Original+Value)
        """
    @overload
    def AddWarning(self,start : OCP.Standard.Standard_Transient,mess : str,orig : str='') -> None: ...
    def Bind(self,start : OCP.Standard.Standard_Transient,binder : Transfer_Binder) -> None: 
        """
        Creates a Link a starting Object with a Binder. This Binder can either bring a Result (effective Binding) or none (it can be set later : pre-binding). Considers a category number, by default 0
        """
    def BindMultiple(self,start : OCP.Standard.Standard_Transient) -> None: 
        """
        Prepares an object <start> to be bound with several results. If no Binder is yet attached to <obj>, a MultipleBinder is created, empty. If a Binder is already set, it must accept Multiple Binding. Considers a category number, by default 0
        """
    def BindTransient(self,start : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Binds a starting object with a Transient Result. Uses a SimpleBinderOfTransient to work. If there is already one but with no Result set, sets its Result. Considers a category number, by default 0
        """
    def Check(self,start : OCP.Standard.Standard_Transient) -> OCP.Interface.Interface_Check: 
        """
        Returns the Check attached to a starting entity. If <start> is unknown, returns an empty Check Adds a case name to a starting entity Adds a case value to a starting entity Returns the complete case list for an entity. Null Handle if empty In the list of mapped items (between 1 and NbMapped), searches for the first item which follows <num0>(not included) and which has an attribute named <name> Attributes are brought by Binders Hence, allows such an iteration
        """
    def CheckList(self,erronly : bool) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns a CheckList as a list of Check : each one is for a starting entity which have either check (warning or fail) messages are attached, or are in abnormal state : that case gives a specific message If <erronly> is True, checks with Warnings only are ignored
        """
    def CheckListOne(self,start : OCP.Standard.Standard_Transient,level : int,erronly : bool) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns a CheckList for one starting object <level> interpreted as by ResultOne If <erronly> is True, checks with Warnings only are ignored
        """
    def CheckNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Specific number of a starting object for check-list : Number in model
        """
    def Clean(self) -> None: 
        """
        Rebuilds the Map and the roots to really remove Unbound items Because Unbind keeps the entity in place, even if not bound Hence, working by checking new items is meaningless if a formerly unbound item is rebound
        """
    def Clear(self) -> None: 
        """
        Resets a TransferProcess as ready for a completely new work. Clears general data (roots) and the Map
        """
    def CompleteResult(self,withstart : bool=False) -> Transfer_IteratorOfProcessForTransient: 
        """
        Returns, as an Iterator, the entire log of transfer (list of created objects and Binders which can bring errors) If withstart is given True, Starting Objets are also returned
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
    def ErrorHandle(self) -> bool: 
        """
        Returns error handling flag
        """
    def Find(self,start : OCP.Standard.Standard_Transient) -> Transfer_Binder: 
        """
        Returns the Binder which is linked with a starting Object It can either bring a Result (Transfer done) or none (for a pre-binding). If no Binder is linked with <start>, returns a Null Handle Considers a category number, by default 0
        """
    def FindElseBind(self,start : OCP.Standard.Standard_Transient) -> Transfer_Binder: 
        """
        Returns a Binder for a starting entity, as follows : Tries to Find the already bound one If none found, creates a VoidBinder and Binds it
        """
    def FindTransient(self,start : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Result of the Transfer of an object <start> as a Transient Result. Returns a Null Handle if there is no Transient Result Considers a category number, by default 0 Warning : Supposes that Binding is done with a SimpleBinderOfTransient
        """
    def FindTypedTransient(self,start : OCP.Standard.Standard_Transient,atype : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Searches for a transient result attached to a starting object, according to its type, by criterium IsKind(atype)
        """
    def GetContext(self,name : str,type : OCP.Standard.Standard_Type,ctx : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns the Context attached to a name, if set and if it is Kind of the type, else a Null Handle Returns True if OK, False if no Context
        """
    def GetProgress(self) -> OCP.Message.Message_ProgressIndicator: 
        """
        Gets Progress indicator
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTypedTransient(self,binder : Transfer_Binder,atype : OCP.Standard.Standard_Type,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Searches for a transient result recorded in a Binder, whatever this Binder is recorded or not in <me>
        """
    def Graph(self) -> OCP.Interface.Interface_Graph: 
        """
        None
        """
    def HGraph(self) -> OCP.Interface.Interface_HGraph: 
        """
        None
        """
    def HasGraph(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAlreadyUsed(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the result of the transfer of an object is already used in other ones. If it is, Rebind cannot change it. Considers a category number, by default 0
        """
    def IsBound(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if a Result (whatever its form) is Bound with a starting Object. I.e., if a Binder with a Result set, is linked with it Considers a category number, by default 0
        """
    def IsCheckListEmpty(self,start : OCP.Standard.Standard_Transient,level : int,erronly : bool) -> bool: 
        """
        Returns True if no check message is attached to a starting object. <level> interpreted as by ResultOne If <erronly> is True, checks with Warnings only are ignored
        """
    def IsDataFail(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Tells if an entity fails on data checking (load time, syntactic, or semantic check). Normally, should answer False. It is not prudent to try transferring an entity which fails on data checking
        """
    def IsDataLoaded(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Tells if an entity is well loaded from file (even if its data fail on checking, they are present). Mostly often, answers True. Else, there was a syntactic error in the file. A non-loaded entity MAY NOT BE transferred, unless its Report (in the model) is interpreted
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
    def IsLooping(self,alevel : int) -> bool: 
        """
        Returns True if we are surely in a DeadLoop. Evaluation is not exact, it is a "majorant" which must be computed fast. This "majorant" is : <alevel> greater than NbMapped.
        """
    def MapIndex(self,start : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the Index value bound to a Starting Object, 0 if none
        """
    def MapItem(self,num : int) -> Transfer_Binder: 
        """
        Returns the Binder bound to an Index Considers a category number, by default 0
        """
    def Mapped(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Starting Object bound to an Index,
        """
    def Mend(self,start : OCP.Standard.Standard_Transient,pref : str='') -> None: 
        """
        None
        """
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns Messenger used for outputting messages. The returned object is guaranteed to be non-null; default is Message::Messenger().
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model used for StartTrace
        """
    def NbMapped(self) -> int: 
        """
        Returns the maximum possible value for Map Index (no result can be bound with a value greater than it)
        """
    def NbRoots(self) -> int: 
        """
        Returns the count of recorded Roots
        """
    def NestingLevel(self) -> int: 
        """
        Returns Nesting Level of Transfers (managed by methods TranscriptWith & Co). Starts to zero. If no automatic Transfer is used, it remains to zero. Zero means Root Level.
        """
    def PrintStats(self,mode : int,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints statistics on a given output, according mode
        """
    def PrintTrace(self,start : OCP.Standard.Standard_Transient,S : OCP.Message.Message_Messenger) -> None: 
        """
        Specific printing to trace an entity : prints label and type (if model is set)
        """
    def Rebind(self,start : OCP.Standard.Standard_Transient,binder : Transfer_Binder) -> None: 
        """
        Changes the Binder linked with a starting Object for its unitary transfer. This it can be useful when the exact form of the result is known once the transfer is widely engaged. This can be done only on first transfer. Considers a category number, by default 0
        """
    def Recognize(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Tells if <start> has been recognized as good candidate for Transfer. i.e. queries the Actor and its Nexts
        """
    def RemoveResult(self,start : OCP.Standard.Standard_Transient,level : int,compute : bool=True) -> None: 
        """
        Removes Results attached to (== Unbinds) a given object and, according <level> : <level> = 0 : only it <level> = 1 : it plus its immediately owned sub-results(scope) <level> = 2 : it plus all its owned sub-results(scope)
        """
    def ResetNestingLevel(self) -> None: 
        """
        Resets Nesting Level of Transfers to Zero (Root Level), whatever its current value.
        """
    def Resize(self,nb : int) -> None: 
        """
        Resizes the Map as required (if a new reliable value has been determined). Acts only if <nb> is greater than actual NbMapped
        """
    def ResultOne(self,start : OCP.Standard.Standard_Transient,level : int,withstart : bool=False) -> Transfer_IteratorOfProcessForTransient: 
        """
        Returns, as an Iterator, the log of transfer for one object <level> = 0 : this object only and if <start> is a scope owner (else, <level> is ignored) : <level> = 1 : object plus its immediate scoped ones <level> = 2 : object plus all its scoped ones
        """
    def Root(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns a Root Entity given its number in the list (1-NbRoots)
        """
    def RootIndex(self,start : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the index in the list of roots for a starting item, or 0 if it is not recorded as a root
        """
    def RootItem(self,num : int) -> Transfer_Binder: 
        """
        Returns the Binder bound with a Root Entity given its number Considers a category number, by default 0
        """
    def RootResult(self,withstart : bool=False) -> Transfer_IteratorOfProcessForTransient: 
        """
        Returns, as an iterator, the log of root transfer, i.e. the created objects and Binders bound to starting roots If withstart is given True, Starting Objets are also returned
        """
    def RootsForTransfer(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        None
        """
    def SendFail(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddFail (Msg)
        """
    def SendMsg(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Adds an information message Trace is filled if trace level is at least 3
        """
    def SendWarning(self,start : OCP.Standard.Standard_Transient,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddWarning (Msg)
        """
    def SetActor(self,actor : Transfer_ActorOfProcessForTransient) -> None: 
        """
        Defines an Actor, which is used for automatic Transfer If already defined, the new Actor is cumulated (see SetNext from Actor)
        """
    def SetContext(self,name : str,ctx : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets a Context : according to receiving appli, to be interpreted by the Actor
        """
    def SetErrorHandle(self,err : bool) -> None: 
        """
        Allows controls if exceptions will be handled Transfer Operations <err> False : they are not handled with try {} catch {} <err> True : they are Default is False: no handling performed
        """
    def SetGraph(self,HG : OCP.Interface.Interface_HGraph) -> None: 
        """
        Sets a Graph : superseedes SetModel if already done
        """
    def SetMessenger(self,messenger : OCP.Message.Message_Messenger) -> None: 
        """
        Sets Messenger used for outputting messages.
        """
    def SetModel(self,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Sets an InterfaceModel, used by StartTrace, CheckList, queries on Integrity, to give informations significant for each norm.
        """
    def SetProgress(self,theProgress : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Sets Progress indicator
        """
    def SetRoot(self,start : OCP.Standard.Standard_Transient) -> None: 
        """
        Declares <obj> (and its Result) as Root. This status will be later exploited by RootResult, see below (Result can be produced at any time)
        """
    def SetRootManagement(self,stat : bool) -> None: ...
    def SetTraceLevel(self,tracelev : int) -> None: 
        """
        Sets trace level used for outputting messages: <trace> = 0 : no trace at all <trace> = 1 : handled exceptions and calls to AddError <trace> = 2 : also calls to AddWarning <trace> = 3 : also traces new Roots (uses method ErrorTrace). Default is 1 : Errors traced
        """
    def StartTrace(self,binder : Transfer_Binder,start : OCP.Standard.Standard_Transient,level : int,mode : int) -> None: 
        """
        Method called when trace is asked Calls PrintTrace to display information relevant for starting objects (which can be redefined) <level> is Nesting Level of Transfer (0 = root) <mode> controls the way the trace is done : 0 neutral, 1 for Error, 2 for Warning message, 3 for new Root
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceLevel(self) -> int: 
        """
        Returns trace level used for outputting messages.
        """
    def Transfer(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Same as Transferring but does not return the Binder. Simply returns True in case of success (for user call)
        """
    def Transferring(self,start : OCP.Standard.Standard_Transient) -> Transfer_Binder: 
        """
        Performs the Transfer of a Starting Object, by calling the method TransferProduct (see below). Mapping and Roots are managed : nothing is done if a Result is already Bound, an exception is raised in case of error.
        """
    def TypedSharings(self,start : OCP.Standard.Standard_Transient,type : OCP.Standard.Standard_Type) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of sharings entities, AT ANY LEVEL, which are kind of a given type. Calls TypedSharings from Graph Returns an empty list if the Graph has not been aknowledged
        """
    def Unbind(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Removes the Binder linked with a starting object If this Binder brings a non-empty Check, it is replaced by a VoidBinder. Also removes from the list of Roots as required. Returns True if done, False if <start> was not bound Considers a category number, by default 0
        """
    def __init__(self,nb : int=10000) -> None: ...
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
class Transfer_UndefMode():
    """
    used on processing Undefined Entities (see TransferOutput)

    Members:

      Transfer_UndefIgnore

      Transfer_UndefFailure

      Transfer_UndefContent

      Transfer_UndefUser
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Transfer_UndefContent: OCP.Transfer.Transfer_UndefMode # value = Transfer_UndefMode.Transfer_UndefContent
    Transfer_UndefFailure: OCP.Transfer.Transfer_UndefMode # value = Transfer_UndefMode.Transfer_UndefFailure
    Transfer_UndefIgnore: OCP.Transfer.Transfer_UndefMode # value = Transfer_UndefMode.Transfer_UndefIgnore
    Transfer_UndefUser: OCP.Transfer.Transfer_UndefMode # value = Transfer_UndefMode.Transfer_UndefUser
    __entries: dict # value = {'Transfer_UndefIgnore': (Transfer_UndefMode.Transfer_UndefIgnore, None), 'Transfer_UndefFailure': (Transfer_UndefMode.Transfer_UndefFailure, None), 'Transfer_UndefContent': (Transfer_UndefMode.Transfer_UndefContent, None), 'Transfer_UndefUser': (Transfer_UndefMode.Transfer_UndefUser, None)}
    __members__: dict # value = {'Transfer_UndefIgnore': Transfer_UndefMode.Transfer_UndefIgnore, 'Transfer_UndefFailure': Transfer_UndefMode.Transfer_UndefFailure, 'Transfer_UndefContent': Transfer_UndefMode.Transfer_UndefContent, 'Transfer_UndefUser': Transfer_UndefMode.Transfer_UndefUser}
    pass
class Transfer_VoidBinder(Transfer_Binder, OCP.Standard.Standard_Transient):
    """
    a VoidBinder is used to bind a starting item with a status, error or warning messages, but no result It is interpreted by TransferProcess, which admits a VoidBinder to be over-written, and copies its check to the new Bindera VoidBinder is used to bind a starting item with a status, error or warning messages, but no result It is interpreted by TransferProcess, which admits a VoidBinder to be over-written, and copies its check to the new Bindera VoidBinder is used to bind a starting item with a status, error or warning messages, but no result It is interpreted by TransferProcess, which admits a VoidBinder to be over-written, and copies its check to the new Binder
    """
    def AddFail(self,mess : str,orig : str='') -> None: 
        """
        Used to declare an individual transfer as beeing erroneous (Status is set to Void, StatusExec is set to Error, <errmess> is added to Check's list of Fails) It is possible to record several messages of error
        """
    def AddResult(self,next : Transfer_Binder) -> None: 
        """
        Adds a next result (at the end of the list) Remark : this information is not processed by Merge
        """
    def AddWarning(self,mess : str,orig : str='') -> None: 
        """
        Used to attach a Warning Message to an individual Transfer It has no effect on the Status
        """
    def CCheck(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages, in order to modify it (adding messages, or replacing it)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        Returns Check which stores Fail messages Note that no Entity is associated in this Check
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
    def HasResult(self) -> bool: 
        """
        Returns True if a Result is available (StatusResult = Defined) A Unique Result will be gotten by Result (which must be defined in each sub-class according to result type) For a Multiple Result, see class MultipleBinder For other case, specific access has to be forecast
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
    def IsMultiple(self) -> bool: 
        """
        Returns True if a Binder has several results, either by itself or because it has next results Can be defined by sub-classes.
        """
    def Merge(self,other : Transfer_Binder) -> None: 
        """
        Merges basic data (Check, ExecStatus) from another Binder but keeps its result. Used when a binder is replaced by another one, this allows to keep messages
        """
    def NextResult(self) -> Transfer_Binder: 
        """
        Returns the next result, Null if none
        """
    def ResultType(self) -> OCP.Standard.Standard_Type: 
        """
        while a VoidBinder admits no Result, its ResultType returns the type of <me>
        """
    def ResultTypeName(self) -> str: 
        """
        Returns "(void)"
        """
    def SetAlreadyUsed(self) -> None: 
        """
        Declares that result is now used by another one, it means that it cannot be modified (by Rebind)
        """
    def SetStatusExec(self,stat : Transfer_StatusExec) -> None: 
        """
        Modifies execution status; called by TransferProcess only (for StatusError, rather use SetError, below)
        """
    def Status(self) -> Transfer_StatusResult: 
        """
        Returns status, which can be Initial (not yet done), Made (a result is recorded, not yet shared), Used (it is shared and cannot be modified)
        """
    def StatusExec(self) -> Transfer_StatusExec: 
        """
        Returns execution status
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
Transfer_StatusDefined: OCP.Transfer.Transfer_StatusResult # value = Transfer_StatusResult.Transfer_StatusDefined
Transfer_StatusDone: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusDone
Transfer_StatusError: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusError
Transfer_StatusInitial: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusInitial
Transfer_StatusLoop: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusLoop
Transfer_StatusRun: OCP.Transfer.Transfer_StatusExec # value = Transfer_StatusExec.Transfer_StatusRun
Transfer_StatusUsed: OCP.Transfer.Transfer_StatusResult # value = Transfer_StatusResult.Transfer_StatusUsed
Transfer_StatusVoid: OCP.Transfer.Transfer_StatusResult # value = Transfer_StatusResult.Transfer_StatusVoid
Transfer_UndefContent: OCP.Transfer.Transfer_UndefMode # value = Transfer_UndefMode.Transfer_UndefContent
Transfer_UndefFailure: OCP.Transfer.Transfer_UndefMode # value = Transfer_UndefMode.Transfer_UndefFailure
Transfer_UndefIgnore: OCP.Transfer.Transfer_UndefMode # value = Transfer_UndefMode.Transfer_UndefIgnore
Transfer_UndefUser: OCP.Transfer.Transfer_UndefMode # value = Transfer_UndefMode.Transfer_UndefUser
