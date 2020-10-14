import OCP.ShapeProcess
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Resource
import OCP.TCollection
import OCP.TopAbs
import OCP.ShapeExtend
import OCP.GeomAbs
import OCP.Message
import OCP.TopTools
import OCP.Standard
import OCP.TopoDS
import OCP.ShapeBuild
import OCP.BRepTools
__all__  = [
"ShapeProcess",
"ShapeProcess_Context",
"ShapeProcess_OperLibrary",
"ShapeProcess_Operator",
"ShapeProcess_ShapeContext",
"ShapeProcess_UOperator"
]
class ShapeProcess():
    """
    Shape Processing module allows to define and apply general Shape Processing as a customizable sequence of Shape Healing operators. The customization is implemented via user-editable resource file which defines sequence of operators to be executed and their parameters.
    """
    @staticmethod
    def FindOperator_s(name : str,op : ShapeProcess_Operator) -> bool: 
        """
        Finds operator by its name
        """
    @staticmethod
    def Perform_s(context : ShapeProcess_Context,seq : str) -> bool: 
        """
        Performs a specified sequence of operators on Context Resource file and other data should be already loaded to Context (including description of sequence seq)
        """
    @staticmethod
    def RegisterOperator_s(name : str,op : ShapeProcess_Operator) -> bool: 
        """
        Registers operator to make it visible for Performer
        """
    def __init__(self) -> None: ...
    pass
class ShapeProcess_Context(OCP.Standard.Standard_Transient):
    """
    Provides convenient interface to resource file Allows to load resource file and get values of attributes starting from some scope, for example if scope is defined as "ToV4" and requested parameter is "exec.op", value of "ToV4.exec.op" parameter from the resource file will be returnedProvides convenient interface to resource file Allows to load resource file and get values of attributes starting from some scope, for example if scope is defined as "ToV4" and requested parameter is "exec.op", value of "ToV4.exec.op" parameter from the resource file will be returnedProvides convenient interface to resource file Allows to load resource file and get values of attributes starting from some scope, for example if scope is defined as "ToV4" and requested parameter is "exec.op", value of "ToV4.exec.op" parameter from the resource file will be returned
    """
    def BooleanVal(self,param : str,def_ : bool) -> bool: 
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
    def GetBoolean(self,param : str,val : bool) -> bool: 
        """
        None
        """
    def GetInteger(self,param : str,val : int) -> bool: 
        """
        None
        """
    def GetReal(self,param : str,val : float) -> bool: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetString(self,param : str,val : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Get value of parameter as being of specific type Returns False if parameter is not defined or has a wrong type
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,file : str,scope : str='') -> bool: 
        """
        Initialises a tool by loading resource file and (if specified) sets starting scope Returns False if resource file not found
        """
    def IntegerVal(self,param : str,def_ : int) -> int: 
        """
        None
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
    def IsParamSet(self,param : str) -> bool: 
        """
        Returns True if parameter is defined in the resource file
        """
    def LoadResourceManager(self,file : str) -> OCP.Resource.Resource_Manager: 
        """
        Loading Resource_Manager object if this object not equal internal static Resource_Manager object or internal static Resource_Manager object is null
        """
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns Messenger used for outputting messages.
        """
    def Progress(self) -> OCP.Message.Message_ProgressIndicator: 
        """
        Returns Progress Indicator.
        """
    def RealVal(self,param : str,def_ : float) -> float: 
        """
        None
        """
    def ResourceManager(self) -> OCP.Resource.Resource_Manager: 
        """
        Returns internal Resource_Manager object
        """
    def SetMessenger(self,messenger : OCP.Message.Message_Messenger) -> None: 
        """
        Sets Messenger used for outputting messages.
        """
    def SetProgress(self,theProgress : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Sets Progress Indicator.
        """
    def SetScope(self,scope : str) -> None: 
        """
        Set a new (sub)scope
        """
    def SetTraceLevel(self,tracelev : int) -> None: 
        """
        Sets trace level used for outputting messages - 0: no trace at all - 1: errors - 2: errors and warnings - 3: all messages Default is 1 : Errors traced
        """
    def StringVal(self,param : str,def_ : str) -> str: 
        """
        Get value of parameter as being of specific type If parameter is not defined or does not have expected type, returns default value as specified
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceLevel(self) -> int: 
        """
        Returns trace level used for outputting messages.
        """
    def UnSetScope(self) -> None: 
        """
        Go out of current scope
        """
    @overload
    def __init__(self,file : str,scope : str='') -> None: ...
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
class ShapeProcess_OperLibrary():
    """
    Provides a set of following operators
    """
    @staticmethod
    def ApplyModifier_s(S : OCP.TopoDS.TopoDS_Shape,context : ShapeProcess_ShapeContext,M : OCP.BRepTools.BRepTools_Modification,map : OCP.TopTools.TopTools_DataMapOfShapeShape,msg : OCP.ShapeExtend.ShapeExtend_MsgRegistrator=None,theMutableInput : bool=False) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Applies BRepTools_Modification to a shape, taking into account sharing of components of compounds. if theMutableInput vat is set to true then imput shape S can be modified during the modification process.
        """
    @staticmethod
    def Init_s() -> None: 
        """
        Registers all the operators
        """
    def __init__(self) -> None: ...
    pass
class ShapeProcess_Operator(OCP.Standard.Standard_Transient):
    """
    Abstract Operator class providing a tool to perform an operation on ContextAbstract Operator class providing a tool to perform an operation on ContextAbstract Operator class providing a tool to perform an operation on Context
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
    def Perform(self,context : ShapeProcess_Context) -> bool: 
        """
        Performs operation and eventually records changes in the context
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
class ShapeProcess_ShapeContext(ShapeProcess_Context, OCP.Standard.Standard_Transient):
    """
    Extends Context to handle shapes Contains map of shape-shape, and messages attached to shapesExtends Context to handle shapes Contains map of shape-shape, and messages attached to shapesExtends Context to handle shapes Contains map of shape-shape, and messages attached to shapes
    """
    def AddMessage(self,S : OCP.TopoDS.TopoDS_Shape,msg : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Warning) -> None: 
        """
        Record a message for shape S Shape S should be one of subshapes of original shape (or whole one), but not one of intermediate shapes Records only if Message() is not Null
        """
    def BooleanVal(self,param : str,def_ : bool) -> bool: 
        """
        None
        """
    def ContinuityVal(self,param : str,def_ : OCP.GeomAbs.GeomAbs_Shape) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Get value of parameter as being of the type GeomAbs_Shape If parameter is not defined or does not have expected type, returns default value as specified
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
    def GetBoolean(self,param : str,val : bool) -> bool: 
        """
        None
        """
    def GetContinuity(self,param : str,val : OCP.GeomAbs.GeomAbs_Shape) -> bool: 
        """
        Get value of parameter as being of the type GeomAbs_Shape Returns False if parameter is not defined or has a wrong type
        """
    def GetDetalisation(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Set and get value for detalisation level Only shapes of types from TopoDS_COMPOUND and until specified detalisation level will be recorded in maps To cancel mapping, use TopAbs_SHAPE To force full mapping, use TopAbs_VERTEX The default level is TopAbs_FACE
        """
    def GetInteger(self,param : str,val : int) -> bool: 
        """
        None
        """
    def GetReal(self,param : str,val : float) -> bool: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetString(self,param : str,val : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Get value of parameter as being of specific type Returns False if parameter is not defined or has a wrong type
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes tool by a new shape and clears all results
        """
    def IntegerVal(self,param : str,def_ : int) -> int: 
        """
        None
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
    def IsNonManifold(self) -> bool: 
        """
        Get NonManifold flag
        """
    def IsParamSet(self,param : str) -> bool: 
        """
        Returns True if parameter is defined in the resource file
        """
    def LoadResourceManager(self,file : str) -> OCP.Resource.Resource_Manager: 
        """
        Loading Resource_Manager object if this object not equal internal static Resource_Manager object or internal static Resource_Manager object is null
        """
    def Map(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns map of replacements shape -> shape This map is not recursive
        """
    def Messages(self) -> OCP.ShapeExtend.ShapeExtend_MsgRegistrator: 
        """
        None

        Returns messages recorded during shape processing It can be nullified before processing in order to avoid recording messages
        """
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns Messenger used for outputting messages.
        """
    def PrintStatistics(self) -> None: 
        """
        Prints statistics on Shape Processing onto the current Messenger.
        """
    def Progress(self) -> OCP.Message.Message_ProgressIndicator: 
        """
        Returns Progress Indicator.
        """
    def RealVal(self,param : str,def_ : float) -> float: 
        """
        None
        """
    @overload
    def RecordModification(self,sh : OCP.TopoDS.TopoDS_Shape,repl : OCP.BRepTools.BRepTools_Modifier,msg : OCP.ShapeExtend.ShapeExtend_MsgRegistrator=None) -> None: 
        """
        None

        None

        None

        Records modifications and resets result accordingly NOTE: modification of resulting shape should be explicitly defined in the maps along with modifications of subshapes
        """
    @overload
    def RecordModification(self,repl : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: ...
    @overload
    def RecordModification(self,repl : OCP.ShapeBuild.ShapeBuild_ReShape,msg : OCP.ShapeExtend.ShapeExtend_MsgRegistrator) -> None: ...
    @overload
    def RecordModification(self,repl : OCP.TopTools.TopTools_DataMapOfShapeShape,msg : OCP.ShapeExtend.ShapeExtend_MsgRegistrator=None) -> None: ...
    def ResourceManager(self) -> OCP.Resource.Resource_Manager: 
        """
        Returns internal Resource_Manager object
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns current result
        """
    def SetDetalisation(self,level : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        None
        """
    def SetMessenger(self,messenger : OCP.Message.Message_Messenger) -> None: 
        """
        Sets Messenger used for outputting messages.
        """
    def SetNonManifold(self,theNonManifold : bool) -> None: 
        """
        Set NonManifold flag
        """
    def SetProgress(self,theProgress : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Sets Progress Indicator.
        """
    def SetResult(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets a new result shape NOTE: this method should be used very carefully to keep consistency of modifications It is recommended to use RecordModification() methods with explicit definition of mapping from current result to a new one
        """
    def SetScope(self,scope : str) -> None: 
        """
        Set a new (sub)scope
        """
    def SetTraceLevel(self,tracelev : int) -> None: 
        """
        Sets trace level used for outputting messages - 0: no trace at all - 1: errors - 2: errors and warnings - 3: all messages Default is 1 : Errors traced
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns shape being processed
        """
    def StringVal(self,param : str,def_ : str) -> str: 
        """
        Get value of parameter as being of specific type If parameter is not defined or does not have expected type, returns default value as specified
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceLevel(self) -> int: 
        """
        Returns trace level used for outputting messages.
        """
    def UnSetScope(self) -> None: 
        """
        Go out of current scope
        """
    @overload
    def __init__(self,file : str,seq : str='') -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,file : str,seq : str='') -> None: ...
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
class ShapeProcess_UOperator(ShapeProcess_Operator, OCP.Standard.Standard_Transient):
    """
    Defines operator as container for static function OperFunc. This allows user to create new operators without creation of new classesDefines operator as container for static function OperFunc. This allows user to create new operators without creation of new classesDefines operator as container for static function OperFunc. This allows user to create new operators without creation of new classes
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
    def Perform(self,context : ShapeProcess_Context) -> bool: 
        """
        Performs operation and records changes in the context
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,func : Any) -> None: 
        """
        __init__(self: OCP.ShapeProcess.ShapeProcess_UOperator, func: bool (opencascade::handle<ShapeProcess_Context> const&)) -> None
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
