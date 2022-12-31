import OCP.Interface
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.NCollection
import OCP.Message
import OCP.Standard
import OCP.TColStd
import OCP.Resource
import io
__all__  = [
"Interface_Array1OfFileParameter",
"Interface_Array1OfHAsciiString",
"Interface_BitMap",
"Interface_Category",
"Interface_Check",
"Interface_CheckFailure",
"Interface_CheckIterator",
"Interface_CheckStatus",
"Interface_CheckTool",
"Interface_CopyControl",
"Interface_CopyMap",
"Interface_CopyTool",
"Interface_DataMapOfTransientInteger",
"Interface_DataState",
"Interface_EntityCluster",
"Interface_EntityIterator",
"Interface_EntityList",
"Interface_FileParameter",
"Interface_FileReaderData",
"Interface_FileReaderTool",
"Interface_FloatWriter",
"Interface_GTool",
"Interface_GeneralLib",
"Interface_GeneralModule",
"Interface_GlobalNodeOfGeneralLib",
"Interface_GlobalNodeOfReaderLib",
"Interface_Graph",
"Interface_GraphContent",
"Interface_HArray1OfHAsciiString",
"Interface_HGraph",
"Interface_SequenceOfCheck",
"Interface_IndexedMapOfAsciiString",
"Interface_IntList",
"Interface_IntVal",
"Interface_InterfaceError",
"Interface_InterfaceMismatch",
"Interface_InterfaceModel",
"Interface_LineBuffer",
"Interface_MSG",
"Interface_MapAsciiStringHasher",
"Interface_NodeOfGeneralLib",
"Interface_NodeOfReaderLib",
"Interface_ParamList",
"Interface_ParamSet",
"Interface_ParamType",
"Interface_Protocol",
"Interface_ReaderLib",
"Interface_ReaderModule",
"Interface_ReportEntity",
"Interface_STAT",
"Interface_HSequenceOfCheck",
"Interface_ShareFlags",
"Interface_ShareTool",
"Interface_SignLabel",
"Interface_SignType",
"Interface_TypedValue",
"Interface_Static",
"Interface_UndefinedContent",
"Interface_VectorOfFileParameter",
"Interface_CheckAny",
"Interface_CheckFail",
"Interface_CheckMessage",
"Interface_CheckNoFail",
"Interface_CheckOK",
"Interface_CheckWarning",
"Interface_DataFail",
"Interface_DataWarning",
"Interface_LoadFail",
"Interface_LoadWarning",
"Interface_ParamBinary",
"Interface_ParamEnum",
"Interface_ParamHexa",
"Interface_ParamIdent",
"Interface_ParamInteger",
"Interface_ParamLogical",
"Interface_ParamMisc",
"Interface_ParamReal",
"Interface_ParamSub",
"Interface_ParamText",
"Interface_ParamVoid",
"Interface_StateOK",
"Interface_StateUnknown",
"Interface_StateUnloaded"
]
class Interface_Array1OfFileParameter():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Interface_Array1OfFileParameter) -> Interface_Array1OfFileParameter: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Interface_FileParameter: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Interface_FileParameter: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Interface_FileParameter: 
        """
        Variable value access
        """
    def First(self) -> Interface_FileParameter: 
        """
        Returns first element
        """
    def Init(self,theValue : Interface_FileParameter) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> Interface_FileParameter: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : Interface_Array1OfFileParameter) -> Interface_Array1OfFileParameter: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Interface_FileParameter) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> Interface_FileParameter: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : Interface_FileParameter,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Interface_Array1OfFileParameter) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Interface_Array1OfHAsciiString():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Interface_Array1OfHAsciiString) -> Interface_Array1OfHAsciiString: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Variable value access
        """
    def First(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : Interface_Array1OfHAsciiString) -> Interface_Array1OfHAsciiString: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Interface_Array1OfHAsciiString) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.TCollection.TCollection_HAsciiString,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Interface_BitMap():
    """
    A bit map simply allows to associate a boolean flag to each item of a list, such as a list of entities, etc... numbered between 1 and a positive count nbitems
    """
    def AddFlag(self,name : str='') -> int: 
        """
        Adds a flag, a name can be attached to it Returns its flag number Makes required reservation
        """
    def AddSomeFlags(self,more : int) -> int: 
        """
        Adds several flags (<more>) with no name Returns the number of last added flag
        """
    def CFalse(self,item : int,flag : int=0) -> bool: 
        """
        Returns the former value for a flag and sets it to False (before : value returned; after : False)
        """
    def CTrue(self,item : int,flag : int=0) -> bool: 
        """
        Returns the former value for a flag and sets it to True (before : value returned; after : True)
        """
    def Clear(self) -> None: 
        """
        Clear all field of bit map
        """
    def FlagName(self,num : int) -> str: 
        """
        Returns the name recorded for a flag, or an empty string
        """
    def FlagNumber(self,name : str) -> int: 
        """
        Returns the number or a flag given its name, or zero
        """
    def Init(self,val : bool,flag : int=0) -> None: 
        """
        Initialises all the values of Flag Number <flag> to a given value <val>
        """
    @overload
    def Initialize(self,nbitems : int,resflags : int=0) -> None: 
        """
        Initialize empty bit by <nbitems> items One flag is defined, n0 0 <resflags> prepares allocation for <resflags> more flags Flags values start at false

        Initialize a BitMap from another one
        """
    @overload
    def Initialize(self,other : Interface_BitMap,copied : bool=False) -> None: ...
    def Length(self) -> int: 
        """
        Returns the count of items (i.e. the length of the bitmap)
        """
    def NbFlags(self) -> int: 
        """
        Returns the count of flags (flag 0 not included)
        """
    def RemoveFlag(self,num : int) -> bool: 
        """
        Removes a flag given its number. Returns True if done, false if num is out of range
        """
    def Reservate(self,moreflags : int) -> None: 
        """
        Reservates for a count of more flags
        """
    def SetFalse(self,item : int,flag : int=0) -> None: 
        """
        Sets a flag to False
        """
    def SetFlagName(self,num : int,name : str) -> bool: 
        """
        Sets a name for a flag, given its number name can be empty (to erase the name of a flag) Returns True if done, false if : num is out of range, or name non-empty already set to another flag
        """
    def SetLength(self,nbitems : int) -> None: 
        """
        Sets for a new count of items, which can be either less or greater than the former one For new items, their flags start at false
        """
    def SetTrue(self,item : int,flag : int=0) -> None: 
        """
        Sets a flag to True
        """
    def SetValue(self,item : int,val : bool,flag : int=0) -> None: 
        """
        Sets a new value for a flag
        """
    def Value(self,item : int,flag : int=0) -> bool: 
        """
        Returns the value (true/false) of a flag, from : - the number of the item - the flag number, by default 0
        """
    @overload
    def __init__(self,other : Interface_BitMap,copied : bool=False) -> None: ...
    @overload
    def __init__(self,nbitems : int,resflags : int=0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Interface_Category():
    """
    This class manages categories A category is defined by a name and a number, and can be seen as a way of rough classification, i.e. less precise than a cdl type. Hence, it is possible to dispatch every entity in about a dozen of categories, twenty is a reasonable maximum.
    """
    @staticmethod
    def AddCategory_s(theName : str) -> int: 
        """
        Records a new Category defined by its names, produces a number New if not yet recorded
        """
    def CatNum(self,theEnt : OCP.Standard.Standard_Transient,theShares : Interface_ShareTool) -> int: 
        """
        Determines the Category Number for an entity in its context, by using general service CategoryNumber
        """
    def ClearNums(self) -> None: 
        """
        Clears the recorded list of category numbers for a Model
        """
    def Compute(self,theModel : Interface_InterfaceModel,theShares : Interface_ShareTool) -> None: 
        """
        Computes the Category Number for each entity and records it, in an array (ent.number -> category number) Hence, it can be queried by the method Num. The Model itself is not recorded, this method is intended to be used in a wider context (which detains also a Graph, etc)
        """
    @staticmethod
    def Init_s() -> None: 
        """
        Default initialisation (protected against several calls : passes only once)
        """
    @staticmethod
    def Name_s(theNum : int) -> str: 
        """
        Returns the name of a category, according to its number
        """
    @staticmethod
    def NbCategories_s() -> int: 
        """
        Returns the count of recorded categories
        """
    def Num(self,theNumEnt : int) -> int: 
        """
        Returns the category number recorded for an entity number Returns 0 if out of range
        """
    @staticmethod
    def Number_s(theName : str) -> int: 
        """
        Returns the number of a category, according to its name
        """
    def SetProtocol(self,theProtocol : Interface_Protocol) -> None: 
        """
        Sets/Changes Protocol
        """
    @overload
    def __init__(self,theProtocol : Interface_Protocol) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theGTool : Interface_GTool) -> None: ...
    pass
class Interface_Check(OCP.Standard.Standard_Transient):
    """
    Defines a Check, as a list of Fail or Warning Messages under a literal form, which can be empty. A Check can also bring an Entity, which is the Entity to which the messages apply (this Entity may be any Transient Object).Defines a Check, as a list of Fail or Warning Messages under a literal form, which can be empty. A Check can also bring an Entity, which is the Entity to which the messages apply (this Entity may be any Transient Object).Defines a Check, as a list of Fail or Warning Messages under a literal form, which can be empty. A Check can also bring an Entity, which is the Entity to which the messages apply (this Entity may be any Transient Object).
    """
    @overload
    def AddFail(self,amess : str,orig : str='') -> None: 
        """
        Records a new Fail message

        Records a new Fail message under two forms : final,original

        Records a new Fail message given as "error text" directly If <orig> is given, a distinct original form is recorded else (D), the original form equates <amess>

        Records a new Fail from the definition of a Msg (Original+Value)
        """
    @overload
    def AddFail(self,amsg : OCP.Message.Message_Msg) -> None: ...
    @overload
    def AddFail(self,amess : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    @overload
    def AddFail(self,amess : OCP.TCollection.TCollection_HAsciiString,orig : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    @overload
    def AddWarning(self,amess : OCP.TCollection.TCollection_HAsciiString,orig : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Records a new Warning message

        Records a new Warning message under two forms : final,original

        Records a Warning message given as "warning message" directly If <orig> is given, a distinct original form is recorded else (D), the original form equates <amess>

        Records a new Warning from the definition of a Msg (Original+Value)
        """
    @overload
    def AddWarning(self,amess : str,orig : str='') -> None: ...
    @overload
    def AddWarning(self,amsg : OCP.Message.Message_Msg) -> None: ...
    @overload
    def AddWarning(self,amess : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def CFail(self,num : int,final : bool=True) -> str: 
        """
        Same as above, but returns a CString (to be printed ...) Final form by default, Original form if <final> is False
        """
    def CInfoMsg(self,num : int,final : bool=True) -> str: 
        """
        Same as above, but returns a CString (to be printed ...) Final form by default, Original form if <final> is False
        """
    def CWarning(self,num : int,final : bool=True) -> str: 
        """
        Same as above, but returns a CString (to be printed ...) Final form by default, Original form if <final> is False
        """
    def Clear(self) -> None: 
        """
        Clears a check, in order to receive information from transfer (Messages and Entity)
        """
    def ClearFails(self) -> None: 
        """
        Clears the Fail Messages (for instance to keep only Warnings)
        """
    def ClearInfoMsgs(self) -> None: 
        """
        Clears the Info Messages
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the Warning Messages (for instance to keep only Fails)
        """
    @overload
    def Complies(self,status : Interface_CheckStatus) -> bool: 
        """
        Tells if Check Status complies with a given one (i.e. also status for query)

        Tells if a message is brought by a Check, as follows : <incl> = 0 : <mess> exactly matches one of the messages <incl> < 0 : <mess> is contained by one of the messages <incl> > 0 : <mess> contains one of the messages For <status> : for CheckWarning and CheckFail, considers only resp. Warning or Check messages. for CheckAny, considers all other values are ignored (answer will be false)
        """
    @overload
    def Complies(self,mess : OCP.TCollection.TCollection_HAsciiString,incl : int,status : Interface_CheckStatus) -> bool: ...
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
    def Entity(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the entity on which the Check has been defined
        """
    def Fail(self,num : int,final : bool=True) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Fail Message as a String Final form by default, Original form if <final> is False
        """
    def Fails(self,final : bool=True) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of Fails, for a frontal-engine logic Final forms by default, Original forms if <final> is False Can be empty
        """
    def GetAsWarning(self,other : Interface_Check,failsonly : bool) -> None: 
        """
        Copies messages converted into Warning messages If failsonly is true, only Fails are taken, and converted else, Warnings are taken too. Does not regard Entity Used to keep Fail messages as Warning, after a recovery
        """
    def GetEntity(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        same as SetEntity (old form kept for compatibility) Warning : Does nothing if Entity field is not yet clear
        """
    def GetMessages(self,other : Interface_Check) -> None: 
        """
        Copies messages stored in another Check, cumulating Does not regard other's Entity. Used to cumulate messages
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasEntity(self) -> bool: 
        """
        Returns True if a Check is devoted to an entity; else, it is global (for InterfaceModel's storing of global error messages)
        """
    def HasFailed(self) -> bool: 
        """
        Returns True if Check brings at least one Fail Message
        """
    def HasWarnings(self) -> bool: 
        """
        Returns True if Check brings at least one Warning Message
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InfoMsg(self,num : int,final : bool=True) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns information message as a String
        """
    def InfoMsgs(self,final : bool=True) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of Info Msg, for a frontal-engine logic Final forms by default, Original forms if <final> is False Can be empty
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
    def Mend(self,pref : str,num : int=0) -> bool: 
        """
        Mends messages, according <pref> and <num> According to <num>, works on the whole list of Fails if = 0(D) or only one Fail message, given its rank If <pref> is empty, converts Fail(s) to Warning(s) Else, does the conversion but prefixes the new Warning(s) but <pref> followed by a semi-column Some reserved values of <pref> are : "FM" : standard prefix "Mended" (can be translated) "CF" : clears Fail(s) "CW" : clears Warning(s) : here, <num> refers to Warning list "CA" : clears all messages : here, <num> is ignored
        """
    def NbFails(self) -> int: 
        """
        Returns count of recorded Fails
        """
    def NbInfoMsgs(self) -> int: 
        """
        Returns the count of recorded information messages
        """
    def NbWarnings(self) -> int: 
        """
        Returns count of recorded Warning messages
        """
    def Print(self,S : io.BytesIO,level : int,final : int=1) -> None: 
        """
        Prints the messages of the check to an Messenger <level> = 1 : only fails <level> = 2 : fails and warnings <level> = 3 : all (fails, warnings, info msg) <final> : if positive (D) prints final values of messages if negative, prints originals if null, prints both forms
        """
    def Remove(self,mess : OCP.TCollection.TCollection_HAsciiString,incl : int,status : Interface_CheckStatus) -> bool: 
        """
        Removes the messages which comply with <mess>, as follows : <incl> = 0 : <mess> exactly matches one of the messages <incl> < 0 : <mess> is contained by one of the messages <incl> > 0 : <mess> contains one of the messages For <status> : for CheckWarning and CheckFail, considers only resp. Warning or Check messages. for CheckAny, considers all other values are ignored (nothing is done) Returns True if at least one message has been removed, False else
        """
    def SendFail(self,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddFail (Msg)
        """
    def SendMsg(self,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records an information message This does not change the status of the Check
        """
    def SendWarning(self,amsg : OCP.Message.Message_Msg) -> None: 
        """
        New name for AddWarning
        """
    def SetEntity(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Receives an entity result of a Transfer
        """
    def Status(self) -> Interface_CheckStatus: 
        """
        Returns the Check Status : OK, Warning or Fail
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trace(self,level : int=-1,final : int=1) -> None: 
        """
        Prints the messages of the check to the default trace file By default, according to the default standard level Else, according level (see method Print)
        """
    def Warning(self,num : int,final : bool=True) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Warning message as a String Final form by default, Original form if <final> is False
        """
    def Warnings(self,final : bool=True) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of Warnings, for a frontal-engine logic Final forms by default, Original forms if <final> is False Can be empty
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,anentity : OCP.Standard.Standard_Transient) -> None: ...
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
class Interface_CheckFailure(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Interface', '__weakref__': <attribute '__weakref__' of 'Interface_CheckFailure' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Interface_CheckFailure' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Interface_CheckIterator():
    """
    Result of a Check operation (especially from InterfaceModel)
    """
    def Add(self,ach : Interface_Check,num : int=0) -> None: 
        """
        Adds a Check to the list to be iterated This Check is Accompanied by Entity Number in the Model (0 for Global Check or Entity unknown in the Model), if 0 and Model is recorded in <me>, it is computed
        """
    @overload
    def CCheck(self,num : int) -> Interface_Check: 
        """
        Returns the Check bound to an Entity Number (0 : Global) in order to be consulted or completed on the spot I.e. returns the Check if is already exists, or adds it then returns the new empty Check

        Returns the Check bound to an Entity, in order to be consulted or completed on the spot I.e. returns the Check if is already exists, or adds it then returns the new empty Check
        """
    @overload
    def CCheck(self,ent : OCP.Standard.Standard_Transient) -> Interface_Check: ...
    @overload
    def Check(self,num : int) -> Interface_Check: 
        """
        Returns the Check which was attached to an Entity given its Number in the Model. <num>=0 is for the Global Check. If no Check was recorded for this Number, returns an empty Check. Remark : Works apart from the iteration methods (no interference)

        Returns the Check attached to an Entity If no Check was recorded for this Entity, returns an empty Check. Remark : Works apart from the iteration methods (no interference)
        """
    @overload
    def Check(self,ent : OCP.Standard.Standard_Transient) -> Interface_Check: ...
    def Checkeds(self,failsonly : bool,global_ : bool) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the list of entities concerned by a Check Only fails if <failsonly> is True, else all non-empty checks If <global> is true, adds the model for a global check Else, global check is ignored
        """
    def Clear(self) -> None: 
        """
        Clears the list of checks
        """
    def Complies(self,status : Interface_CheckStatus) -> bool: 
        """
        Tells if this check list complies with a given status : OK (i.e. empty), Warning (at least one Warning, but no Fail), Fail (at least one), Message (not OK), NoFail, Any
        """
    def Destroy(self) -> None: 
        """
        Clears data of iteration
        """
    @overload
    def Extract(self,status : Interface_CheckStatus) -> Interface_CheckIterator: 
        """
        Returns a CheckIterator which contains the checks which comply with a given status Each check is added completely (no split Warning/Fail)

        Returns a CheckIterator which contains the check which comply with a message, plus some conditions as follows : <incl> = 0 : <mess> exactly matches one of the messages <incl> < 0 : <mess> is contained by one of the messages <incl> > 0 : <mess> contains one of the messages For <status> : for CheckWarning and CheckFail, considers only resp. Warning or Check messages. for CheckAny, considers all other values are ignored (answer will be false) Each Check which complies is entirely taken
        """
    @overload
    def Extract(self,mess : str,incl : int,status : Interface_CheckStatus) -> Interface_CheckIterator: ...
    def IsEmpty(self,failsonly : bool) -> bool: 
        """
        Returns True if : no Fail has been recorded if <failsonly> is True, no Check at all if <failsonly> is False
        """
    def Merge(self,other : Interface_CheckIterator) -> None: 
        """
        Merges another CheckIterator into <me>, i.e. adds each of its Checks. Content of <other> remains unchanged. Takes also the Model but not the Name
        """
    def Model(self) -> Interface_InterfaceModel: 
        """
        Returns the stored model (can be a null handle)
        """
    def More(self) -> bool: 
        """
        Returns True if there are more Checks to get
        """
    def Name(self) -> str: 
        """
        Returns the recorded name (can be empty)
        """
    def Next(self) -> None: 
        """
        Sets Iteration to next Item
        """
    def Number(self) -> int: 
        """
        Returns Number of Entity for the Check currently iterated or 0 for GlobalCheck
        """
    @overload
    def Print(self,S : io.BytesIO,failsonly : bool,final : int=0) -> None: 
        """
        Prints the list of Checks with their attached Numbers If <failsonly> is True, prints only Fail messages If <failsonly> is False, prints all messages If <final> = 0 (D), prints also original messages if different If <final> < 0, prints only original messages If <final> > 0, prints only final messages It uses the recorded Model if it is defined Remark : Works apart from the iteration methods (no interference)

        Works as Print without a model, but for entities which have no attached number (Number not positive), tries to compute this Number from <model> and displays "original" or "computed"
        """
    @overload
    def Print(self,S : io.BytesIO,model : Interface_InterfaceModel,failsonly : bool,final : int=0) -> None: ...
    def Remove(self,mess : str,incl : int,status : Interface_CheckStatus) -> bool: 
        """
        Removes the messages of all Checks, under these conditions : <incl> = 0 : <mess> exactly matches one of the messages <incl> < 0 : <mess> is contained by one of the messages <incl> > 0 : <mess> contains one of the messages For <status> : for CheckWarning and CheckFail, considers only resp. Warning or Check messages. for CheckAny, considers all other values are ignored (nothing is done) Returns True if at least one message has been removed, False else
        """
    def SetModel(self,model : Interface_InterfaceModel) -> None: 
        """
        Defines a Model, used to locate entities (not required, if it is absent, entities are simply less documented)
        """
    def SetName(self,name : str) -> None: 
        """
        Sets / Changes the name
        """
    def Start(self) -> None: 
        """
        Starts Iteration. Thus, it is possible to restart it Remark : an iteration may be done with a const Iterator While its content is modified (through a pointer), this allows to give it as a const argument to a function
        """
    def Status(self) -> Interface_CheckStatus: 
        """
        Returns worst status among : OK, Warning, Fail
        """
    def Value(self) -> Interface_Check: 
        """
        Returns Check currently Iterated It brings all other information (status, messages, ...) The Number of the Entity in the Model is given by Number below
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,name : str) -> None: ...
    pass
class Interface_CheckStatus():
    """
    Classifies checks OK : check is empty Warning : Warning, no Fail Fail : Fail Others to query : Any : any status Message : Warning/Fail NoFail : Warning/OK

    Members:

      Interface_CheckOK

      Interface_CheckWarning

      Interface_CheckFail

      Interface_CheckAny

      Interface_CheckMessage

      Interface_CheckNoFail
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
    Interface_CheckAny: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckAny: 3>
    Interface_CheckFail: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckFail: 2>
    Interface_CheckMessage: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckMessage: 4>
    Interface_CheckNoFail: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckNoFail: 5>
    Interface_CheckOK: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckOK: 0>
    Interface_CheckWarning: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckWarning: 1>
    __entries: dict # value = {'Interface_CheckOK': (<Interface_CheckStatus.Interface_CheckOK: 0>, None), 'Interface_CheckWarning': (<Interface_CheckStatus.Interface_CheckWarning: 1>, None), 'Interface_CheckFail': (<Interface_CheckStatus.Interface_CheckFail: 2>, None), 'Interface_CheckAny': (<Interface_CheckStatus.Interface_CheckAny: 3>, None), 'Interface_CheckMessage': (<Interface_CheckStatus.Interface_CheckMessage: 4>, None), 'Interface_CheckNoFail': (<Interface_CheckStatus.Interface_CheckNoFail: 5>, None)}
    __members__: dict # value = {'Interface_CheckOK': <Interface_CheckStatus.Interface_CheckOK: 0>, 'Interface_CheckWarning': <Interface_CheckStatus.Interface_CheckWarning: 1>, 'Interface_CheckFail': <Interface_CheckStatus.Interface_CheckFail: 2>, 'Interface_CheckAny': <Interface_CheckStatus.Interface_CheckAny: 3>, 'Interface_CheckMessage': <Interface_CheckStatus.Interface_CheckMessage: 4>, 'Interface_CheckNoFail': <Interface_CheckStatus.Interface_CheckNoFail: 5>}
    pass
class Interface_CheckTool():
    """
    Performs Checks on Entities, using General Service Library and Modules to work. Works on one Entity or on a complete Model
    """
    def AnalyseCheckList(self) -> Interface_CheckIterator: 
        """
        Returns list of errors detected at Analyse time (syntactic) (note that GlobalCheck is not in this list)
        """
    def Check(self,num : int) -> Interface_Check: 
        """
        Returns the Check associated to an Entity identified by its Number in a Model.
        """
    def CheckList(self) -> Interface_CheckIterator: 
        """
        Returns list of all Errors detected Note that presence of Unknown Entities is not an error Cumulates : GlobalCheck if error + AnalyseCheckList + VerifyCheckList
        """
    def CheckSuccess(self,reset : bool=False) -> None: 
        """
        Checks if any Error has been detected (CheckList not empty) Returns normally if none, raises exception if some exists. It reuses the last computations from other checking methods, unless the argument <reset> is given True
        """
    def CompleteCheckList(self) -> Interface_CheckIterator: 
        """
        Returns list of all "remarkable" information, which include : - GlobalCheck, if not empty - Error Checks, for all Errors (Verify + Analyse) - also Corrected Entities - and Unknown Entities : for those, each Unknown Entity is associated to an empty Check (it is neither an Error nor a Correction, but a remarkable information)
        """
    def FillCheck(self,ent : OCP.Standard.Standard_Transient,sh : Interface_ShareTool,ach : Interface_Check) -> Any: 
        """
        Fills as required a Check with the Error and Warning messages produced by Checking a given Entity. For an Erroneous or Corrected Entity : Check build at Analyse time; else, Check computed for Entity (Verify integrity), can use a Graph as required to control context
        """
    @overload
    def Print(self,list : Interface_CheckIterator,S : io.BytesIO) -> None: 
        """
        Utility method which Prints the content of a Check

        Simply Lists all the Checks and the Content (messages) and the Entity, if there is, of each Check (if all Checks are OK, nothing is Printed)
        """
    @overload
    def Print(self,ach : Interface_Check,S : io.BytesIO) -> None: ...
    def UnknownEntities(self) -> Interface_EntityIterator: 
        """
        Returns list of Unknown Entities Note that Error and Erroneous Entities are not considered as Unknown
        """
    def VerifyCheckList(self) -> Interface_CheckIterator: 
        """
        Returns list of integrity constraints errors (semantic) (note that GlobalCheck is not in this list)
        """
    def WarningCheckList(self) -> Interface_CheckIterator: 
        """
        Returns list of Corrections (includes GlobalCheck if corrected)
        """
    @overload
    def __init__(self,model : Interface_InterfaceModel) -> None: ...
    @overload
    def __init__(self,graph : Interface_Graph) -> None: ...
    @overload
    def __init__(self,model : Interface_InterfaceModel,protocol : Interface_Protocol) -> None: ...
    @overload
    def __init__(self,hgraph : Interface_HGraph) -> None: ...
    pass
class Interface_CopyControl(OCP.Standard.Standard_Transient):
    """
    This deferred class describes the services required by CopyTool to work. They are very simple and correspond basically to the management of an indexed map. But they can be provided by various classes which can control a Transfer. Each Starting Entity have at most one Result (Mapping one-one)This deferred class describes the services required by CopyTool to work. They are very simple and correspond basically to the management of an indexed map. But they can be provided by various classes which can control a Transfer. Each Starting Entity have at most one Result (Mapping one-one)This deferred class describes the services required by CopyTool to work. They are very simple and correspond basically to the management of an indexed map. But they can be provided by various classes which can control a Transfer. Each Starting Entity have at most one Result (Mapping one-one)
    """
    def Bind(self,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Bind a Result to a Starting Entity identified by its Number
        """
    def Clear(self) -> None: 
        """
        Clears List of Copy Results. Gets Ready to begin another Copy Process.
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
        Searches for the Result bound to a Startingf Entity identified by its Number. If Found, returns True and fills <res> Else, returns False and nullifies <res>
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
class Interface_CopyMap(Interface_CopyControl, OCP.Standard.Standard_Transient):
    """
    Manages a Map for the need of single Transfers, such as Copies In such transfer, Starting Entities are read from a unique Starting Model, and each transferred Entity is bound to one and only one Result, which cannot be changed later.Manages a Map for the need of single Transfers, such as Copies In such transfer, Starting Entities are read from a unique Starting Model, and each transferred Entity is bound to one and only one Result, which cannot be changed later.Manages a Map for the need of single Transfers, such as Copies In such transfer, Starting Entities are read from a unique Starting Model, and each transferred Entity is bound to one and only one Result, which cannot be changed later.
    """
    def Bind(self,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> None: 
        """
        Binds a Starting Entity identified by its Number <num> in the Starting Model, to a Result of Transfer <res>
        """
    def Clear(self) -> None: 
        """
        Clears Transfer List. Gets Ready to begin another Transfer
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
    def Model(self) -> Interface_InterfaceModel: 
        """
        Returns the InterfaceModel used at Creation time
        """
    def Search(self,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> bool: 
        """
        Search for the result of a Starting Object (i.e. an Entity, identified by its Number <num> in the Starting Model) Returns True if a Result is Bound (and fills <res>) Returns False if no result is Bound (and nullifies <res>)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,amodel : Interface_InterfaceModel) -> None: ...
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
class Interface_CopyTool():
    """
    Performs Deep Copies of sets of Entities Allows to perform Copy of Interface Entities from a Model to another one. Works by calling general services GetFromAnother and GetImplied. Uses a CopyMap to bind a unique Result to each Copied Entity
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
    def CompleteResult(self,withreports : bool=False) -> Interface_EntityIterator: 
        """
        Returns the complete list of copied Entities If <withreports> is given True, the entities which were reported in the Starting Model are replaced in the list by the copied ReportEntities
        """
    def Control(self) -> Interface_CopyControl: 
        """
        Returns the object used for Control
        """
    def Copy(self,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,mapped : bool,errstat : bool) -> bool: 
        """
        Creates the CounterPart of an Entity (by ShallowCopy), Binds it, then Copies the content of the former Entity to the other one (same Type), by call to the General Service Library It may command the Copy of Referenced Entities Then, its returns True.
        """
    def FillModel(self,bmodel : Interface_InterfaceModel) -> None: 
        """
        Fills a Model with the result of the transfer (TransferList) Commands copy of Header too, and calls RenewImpliedRefs
        """
    def LastCopiedAfter(self,numfrom : int,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns an copied Entity and its Result which were operated after last call to ClearLastFlags. It returns the first "Last Copied Entity" which Number follows <numfrom>, Zero if none. It is used in a loop as follow : Integer num = 0; while ( (num = CopyTool.LastCopiedAfter(num,ent,res)) ) { .. Process Starting <ent> and its Result <res> }
        """
    def Model(self) -> Interface_InterfaceModel: 
        """
        Returns the Model on which the CopyTool works
        """
    def RenewImpliedRefs(self) -> None: 
        """
        Renews the Implied References. These References do not involve Copying of referenced Entities. For such a Reference, if the Entity which defines it AND the referenced Entity are both copied, then this Reference is renewed. Else it is deleted in the copied Entities. Remark : this concerns only some specific references, such as "back pointers".
        """
    def RootResult(self,withreports : bool=False) -> Interface_EntityIterator: 
        """
        Returns the list of Root copied Entities (those which were asked for copy by the user of CopyTool, not by copying another Entity)
        """
    def Search(self,ent : OCP.Standard.Standard_Transient,res : OCP.Standard.Standard_Transient) -> bool: 
        """
        Search for the result of a Starting Object (i.e. an Entity) Returns True if a Result is Bound (and fills "result") Returns False if no result is Bound
        """
    def SetControl(self,othermap : Interface_CopyControl) -> None: 
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
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,lib : Interface_GeneralLib) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,protocol : Interface_Protocol) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel) -> None: ...
    pass
class Interface_DataMapOfTransientInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Interface_DataMapOfTransientInteger) -> Interface_DataMapOfTransientInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.Standard.Standard_Transient,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.Standard.Standard_Transient,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.Standard.Standard_Transient) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.Standard.Standard_Transient) -> int: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : Interface_DataMapOfTransientInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.Standard.Standard_Transient) -> int: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.Standard.Standard_Transient,theValue : int) -> bool: ...
    def IsBound(self,theKey : OCP.Standard.Standard_Transient) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.Standard.Standard_Transient) -> int: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.Standard.Standard_Transient) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Interface_DataMapOfTransientInteger) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Interface_DataState():
    """
    validity state of anentity's content (see InterfaceModel)

    Members:

      Interface_StateOK

      Interface_LoadWarning

      Interface_LoadFail

      Interface_DataWarning

      Interface_DataFail

      Interface_StateUnloaded

      Interface_StateUnknown
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
    Interface_DataFail: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_DataFail: 4>
    Interface_DataWarning: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_DataWarning: 3>
    Interface_LoadFail: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_LoadFail: 2>
    Interface_LoadWarning: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_LoadWarning: 1>
    Interface_StateOK: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_StateOK: 0>
    Interface_StateUnknown: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_StateUnknown: 6>
    Interface_StateUnloaded: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_StateUnloaded: 5>
    __entries: dict # value = {'Interface_StateOK': (<Interface_DataState.Interface_StateOK: 0>, None), 'Interface_LoadWarning': (<Interface_DataState.Interface_LoadWarning: 1>, None), 'Interface_LoadFail': (<Interface_DataState.Interface_LoadFail: 2>, None), 'Interface_DataWarning': (<Interface_DataState.Interface_DataWarning: 3>, None), 'Interface_DataFail': (<Interface_DataState.Interface_DataFail: 4>, None), 'Interface_StateUnloaded': (<Interface_DataState.Interface_StateUnloaded: 5>, None), 'Interface_StateUnknown': (<Interface_DataState.Interface_StateUnknown: 6>, None)}
    __members__: dict # value = {'Interface_StateOK': <Interface_DataState.Interface_StateOK: 0>, 'Interface_LoadWarning': <Interface_DataState.Interface_LoadWarning: 1>, 'Interface_LoadFail': <Interface_DataState.Interface_LoadFail: 2>, 'Interface_DataWarning': <Interface_DataState.Interface_DataWarning: 3>, 'Interface_DataFail': <Interface_DataState.Interface_DataFail: 4>, 'Interface_StateUnloaded': <Interface_DataState.Interface_StateUnloaded: 5>, 'Interface_StateUnknown': <Interface_DataState.Interface_StateUnknown: 6>}
    pass
class Interface_EntityCluster(OCP.Standard.Standard_Transient):
    """
    Auxiliary class for EntityList. An EntityList designates an EntityCluster, which brings itself an fixed maximum count of Entities. If it is full, it gives access to another cluster ("Next"). This class is intended to give a good compromise between access time (faster than a Sequence, good for little count) and memory use (better than a Sequence in any case, overall for little count, better than an Array for a very little count. It is designed for a light management. Remark that a new Item may not be Null, because this is the criterium used for "End of List"Auxiliary class for EntityList. An EntityList designates an EntityCluster, which brings itself an fixed maximum count of Entities. If it is full, it gives access to another cluster ("Next"). This class is intended to give a good compromise between access time (faster than a Sequence, good for little count) and memory use (better than a Sequence in any case, overall for little count, better than an Array for a very little count. It is designed for a light management. Remark that a new Item may not be Null, because this is the criterium used for "End of List"Auxiliary class for EntityList. An EntityList designates an EntityCluster, which brings itself an fixed maximum count of Entities. If it is full, it gives access to another cluster ("Next"). This class is intended to give a good compromise between access time (faster than a Sequence, good for little count) and memory use (better than a Sequence in any case, overall for little count, better than an Array for a very little count. It is designed for a light management. Remark that a new Item may not be Null, because this is the criterium used for "End of List"
    """
    def Append(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Appends an Entity to the Cluster. If it is not full, adds the entity directly inside itself. Else, transmits to its Next and Creates it if it does not yet exist
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
    def FillIterator(self,iter : Interface_EntityIterator) -> None: 
        """
        Fills an Iterator with designated Entities (includes Next)
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
        Returns total count of Entities (including Next)
        """
    @overload
    def Remove(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Removes an Entity from the Cluster. If it is not found, calls its Next one to do so. Returns True if it becomes itself empty, False else (thus, a Cluster which becomes empty is deleted from the list)

        Removes an Entity from the Cluster, given its rank. If <num> is greater than NbLocal, calls its Next with (num - NbLocal), Returns True if it becomes itself empty, False else
        """
    @overload
    def Remove(self,num : int) -> bool: ...
    def SetValue(self,num : int,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Changes an Entity given its rank.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Entity identified by its rank in the list (including Next)
        """
    @overload
    def __init__(self,ant : OCP.Standard.Standard_Transient,ec : Interface_EntityCluster) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,ent : OCP.Standard.Standard_Transient) -> None: ...
    @overload
    def __init__(self,ec : Interface_EntityCluster) -> None: ...
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
class Interface_EntityIterator():
    """
    Defines an Iterator on Entities. Allows considering of various criteria
    """
    def AddItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds to the iteration list a defined entity
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Gets a list of entities and adds its to the iteration list
        """
    def Content(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the content of the Iterator, accessed through a Handle to be used by a frontal-engine logic Returns an empty Sequence if the Iterator is empty Calls Start if not yet done
        """
    def Destroy(self) -> None: 
        """
        Clears data of iteration
        """
    def GetOneItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        same as AddItem (kept for compatibility)
        """
    def More(self) -> bool: 
        """
        Says if there are other entities (vertices) to iterate the first time, calls Start
        """
    def NbEntities(self) -> int: 
        """
        Returns count of entities which will be iterated on Calls Start if not yet done
        """
    def NbTyped(self,type : OCP.Standard.Standard_Type) -> int: 
        """
        Returns count of entities of a given type (kind of)
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next entity (vertex) to give
        """
    def SelectType(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects entities with are Kind of a given type, keep only them (is keep is True) or reject only them (if keep is False)
        """
    def Start(self) -> None: 
        """
        Allows re-iteration (useless for the first iteration)
        """
    def Typed(self,type : OCP.Standard.Standard_Type) -> Interface_EntityIterator: 
        """
        Returns the list of entities of a given type (kind of)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current Entity iterated, to be used by Interface tools
        """
    @overload
    def __init__(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Interface_EntityList():
    """
    This class defines a list of Entities (Transient Objects), it can be used as a field of other Transient classes, with these features : - oriented to define a little list, that is, slower than an Array or a Map of Entities for a big count (about 100 and over), but faster than a Sequence - allows to work as a Sequence, limited to Clear, Append, Remove, Access to an Item identified by its rank in the list - space saving, compared to a Sequence, especially for little amounts; better than an Array for a very little amount (less than 10) but less good for a greater amount
    """
    def Add(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an Entity to the list, that is, with NO REGARD about the order (faster than Append if count becomes greater than 10)
        """
    def Append(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Appends an Entity, that is to the END of the list (keeps order, but works slowerly than Add, see below)
        """
    def Clear(self) -> None: 
        """
        Clears the List
        """
    def FillIterator(self,iter : Interface_EntityIterator) -> None: 
        """
        fills an Iterator with the content of the list (normal way to consult a list which has been filled with Add)
        """
    def IsEmpty(self) -> bool: 
        """
        Returns True if the list is empty
        """
    def NbEntities(self) -> int: 
        """
        Returns count of recorded Entities
        """
    def NbTypedEntities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        Returns count of Entities of a given Type (0 : none)
        """
    @overload
    def Remove(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Removes an Entity from the list, if it is there

        Removes an Entity from the list, given its rank
        """
    @overload
    def Remove(self,num : int) -> None: ...
    def SetValue(self,num : int,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Returns an Item given its number. Beware about the way the list was filled (see above, Add and Append)
        """
    def TypedEntity(self,atype : OCP.Standard.Standard_Type,num : int=0) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Entity which is of a given type. If num = 0 (D), there must be ONE AND ONLY ONE If num > 0, returns the num-th entity of this type
        """
    def Value(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns an Item given its number. Beware about the way the list was filled (see above, Add and Append)
        """
    def __init__(self) -> None: ...
    pass
class Interface_FileParameter():
    """
    Auxiliary class to store a literal parameter in a file intermediate directory or in an UndefinedContent : a reference type Parameter detains an Integer which is used to address a record in the directory. FileParameter is intended to be stored in a ParamSet : hence memory management is performed by ParamSet, which calls Clear to work, while the Destructor (see Destroy) does nothing. Also a FileParameter can be read for consultation only, not to be read from a Structure to be included into another one.
    """
    def CValue(self) -> str: 
        """
        Same as above, but as a CString (for immediate exploitation) was C++ : return const
        """
    def Clear(self) -> None: 
        """
        Clears stored data : frees memory taken for the String Value
        """
    def Destroy(self) -> None: 
        """
        Destructor. Does nothing because Memory is managed by ParamSet
        """
    def EntityNumber(self) -> int: 
        """
        Returns value set by SetEntityNumber
        """
    @overload
    def Init(self,val : OCP.TCollection.TCollection_AsciiString,typ : Interface_ParamType) -> None: 
        """
        Fills fields (with Entity Number set to zero)

        Same as above, but builds the Value from a CString
        """
    @overload
    def Init(self,val : str,typ : Interface_ParamType) -> None: ...
    def ParamType(self) -> Interface_ParamType: 
        """
        Returns the type of the parameter
        """
    def SetEntityNumber(self,num : int) -> None: 
        """
        Allows to set a reference to an Entity in a numbered list
        """
    def __init__(self) -> None: ...
    pass
class Interface_FileReaderData(OCP.Standard.Standard_Transient):
    """
    This class defines services which permit to access Data issued from a File, in a form which does not depend of physical format : thus, each Record has an attached ParamList (to be managed) and resulting Entity.This class defines services which permit to access Data issued from a File, in a form which does not depend of physical format : thus, each Record has an attached ParamList (to be managed) and resulting Entity.This class defines services which permit to access Data issued from a File, in a form which does not depend of physical format : thus, each Record has an attached ParamList (to be managed) and resulting Entity.
    """
    @overload
    def AddParam(self,num : int,aval : str,atype : Interface_ParamType,nument : int=0) -> None: 
        """
        Adds a parameter to record no "num" and fills its fields (EntityNumber is optional) Warning : <aval> is assumed to be memory-managed elsewhere : it is NOT copied. This gives a best speed : strings remain stored in pages of characters

        Same as above, but gets a AsciiString from TCollection Remark that the content of the AsciiString is locally copied (because its content is most often lost after using)

        Same as above, but gets a complete FileParameter Warning : Content of <FP> is NOT copied : its original address and space in memory are assumed to be managed elsewhere (see ParamSet)
        """
    @overload
    def AddParam(self,num : int,FP : Interface_FileParameter) -> None: ...
    @overload
    def AddParam(self,num : int,aval : OCP.TCollection.TCollection_AsciiString,atype : Interface_ParamType,nument : int=0) -> None: ...
    def BindEntity(self,num : int,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Binds an entity to a record
        """
    def BoundEntity(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the entity bound to a record, set by SetEntities
        """
    def ChangeParam(self,num : int,nump : int) -> Interface_FileParameter: 
        """
        Same as above, but in order to be modified on place
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Destroy(self) -> None: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def Fastof_s(str : str) -> float: 
        """
        Same spec.s as standard <atof> but 5 times faster
        """
    def FindNextRecord(self,num : int) -> int: 
        """
        Determines the record number defining an Entity following a given record number. Specific to each sub-class of FileReaderData. Returning zero means no record found
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitParams(self,num : int) -> None: 
        """
        attaches an empty ParamList to a Record
        """
    def IsErrorLoad(self) -> bool: 
        """
        Returns True if the status "Error Load" has been set (to True or False)
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
    def IsParamDefined(self,num : int,nump : int) -> bool: 
        """
        Returns True if parameter "nump" of record "num" is defined (it is not if its type is ParamVoid)
        """
    def NbEntities(self) -> int: 
        """
        Returns the count of entities. Depending of each norm, records can be Entities or SubParts (SubList in STEP, SubGroup in SET ...). NbEntities counts only Entities, not Subs Used for memory reservation in InterfaceModel Default implementation uses FindNextRecord Can be redefined into a more performant way
        """
    def NbParams(self,num : int) -> int: 
        """
        Returns count of parameters attached to record "num" If <num> = 0, returns the total recorded count of parameters
        """
    def NbRecords(self) -> int: 
        """
        Returns the count of registered records That is, value given for Initialization (can be redefined)
        """
    def Param(self,num : int,nump : int) -> Interface_FileParameter: 
        """
        Returns parameter "nump" of record "num", as a complete FileParameter
        """
    def ParamCValue(self,num : int,nump : int) -> str: 
        """
        Same as above, but as a CString was C++ : return const
        """
    def ParamEntity(self,num : int,nump : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the StepEntity referenced by a parameter Error if none
        """
    def ParamFirstRank(self,num : int) -> int: 
        """
        Returns the absolute rank of the beginning of a record (its list is from ParamFirstRank+1 to ParamFirstRank+NbParams)
        """
    def ParamNumber(self,num : int,nump : int) -> int: 
        """
        Returns record number of an entity referenced by a parameter of type Ident; 0 if no EntityNumber has been determined Note that it is used to reference Entities but also Sublists (sublists are not objects, but internal descriptions)
        """
    def ParamType(self,num : int,nump : int) -> Interface_ParamType: 
        """
        Returns type of parameter "nump" of record "num" Returns literal value of parameter "nump" of record "num" was C++ : return const &
        """
    def Params(self,num : int) -> Interface_ParamList: 
        """
        Returns the complete ParamList of a record (read only) num = 0 to return the whole param list for the file
        """
    def ResetErrorLoad(self) -> bool: 
        """
        Returns the former value of status "Error Load" then resets it Used to read the status then ensure it is reset
        """
    def SetErrorLoad(self,val : bool) -> None: 
        """
        Sets the status "Error Load" on, to overside check fails <val> True : declares unloaded <val> False : declares loaded If not called before loading (see FileReaderTool), check fails give the status IsErrorLoad says if SetErrorLoad has been called by user ResetErrorLoad resets it (called by FileReaderTool) This allows to specify that the currently loaded entity remains unloaded (because of syntactic fail)
        """
    def SetParam(self,num : int,nump : int,FP : Interface_FileParameter) -> None: 
        """
        Sets a new value for a parameter of a record, given by : num : record number; nump : parameter number in the record
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
class Interface_FileReaderTool():
    """
    Defines services which are required to load an InterfaceModel from a File. Typically, it may firstly transform a system file into a FileReaderData object, then work on it, not longer considering file contents, to load an Interface Model. It may also work on a FileReaderData already loaded.
    """
    def AnalyseRecord(self,num : int,anent : OCP.Standard.Standard_Transient,acheck : Interface_Check) -> bool: 
        """
        Fills an Entity, given record no; specific to each Interface, called by AnalyseFile from InterfaceModel (which manages its calling arguments) To work, each Interface can define a method in its proper Transient class, like this (given as an example) : AnalyseRecord (me : mutable; FR : in out FileReaderTool; num : Integer; acheck : in out Check) returns Boolean; and call it from AnalyseRecord
        """
    def BeginRead(self,amodel : Interface_InterfaceModel) -> None: 
        """
        Fills model's header; each Interface defines for its Model its own file header; this method fills it from FileReaderTool.+ It is called by AnalyseFile from InterfaceModel
        """
    def Clear(self) -> None: 
        """
        Clear fields
        """
    def Data(self) -> Interface_FileReaderData: 
        """
        Returns the FileReaderData which is used to work
        """
    def EndRead(self,amodel : Interface_InterfaceModel) -> None: 
        """
        Ends file reading after reading all the entities default is doing nothing; redefinable as necessary
        """
    def ErrorHandle(self) -> bool: 
        """
        Returns ErrorHandle flag
        """
    def LoadModel(self,amodel : Interface_InterfaceModel) -> None: 
        """
        Reads and fills Entities from the FileReaderData set by SetData to an InterfaceModel. It enchains required operations, the specific ones correspond to deferred methods (below) to be defined for each Norm. It manages also error recovery and trace. Remark : it calls SetModel. It Can raise any error which can occur during a load operation, unless Error Handling is set. This method can also be redefined if judged necessary.
        """
    def LoadedEntity(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Reads, Fills and Returns one Entity read from a Record of the FileReaderData. This Method manages also case of Fail or Warning, by producing a ReportEntyty plus , for a Fail, a literal Content (as an UnknownEntity). Performs also Trace
        """
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns Messenger used for outputting messages. The returned object is guaranteed to be non-null; default is Message::Messenger().
        """
    def Model(self) -> Interface_InterfaceModel: 
        """
        Returns the stored Model
        """
    def NewModel(self) -> Interface_InterfaceModel: 
        """
        Creates an empty Model of the norm. Uses Protocol to do it
        """
    def Protocol(self) -> Interface_Protocol: 
        """
        Returns the Protocol given at creation time
        """
    def Recognize(self,num : int,ach : Interface_Check,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Recognizes a record, given its number. Specific to each Interface; called by SetEntities. It can call the basic method RecognizeByLib. Returns False if recognition has failed, True else. <ach> has not to be filled if simply Recognition has failed : it must record true error messages : RecognizeByLib can generate error messages if NewRead is called
        """
    def RecognizeByLib(self,num : int,glib : Interface_GeneralLib,rlib : Interface_ReaderLib,ach : Interface_Check,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Recognizes a record with the help of Libraries. Can be used to implement the method Recognize. <rlib> is used to find Protocol and CaseNumber to apply <glib> performs the creation (by service NewVoid, or NewRead if NewVoid gave no result) <ach> is a check, which is transmitted to NewRead if it is called, gives a result but which is false <ent> is the result Returns False if recognition has failed, True else
        """
    def SetData(self,reader : Interface_FileReaderData,protocol : Interface_Protocol) -> None: 
        """
        Sets Data to a FileReaderData. Works with a Protocol
        """
    def SetEntities(self) -> None: 
        """
        Fills records with empty entities; once done, each entity can ask the FileReaderTool for any entity referenced through an identifier. Calls Recognize which is specific to each specific type of FileReaderTool
        """
    def SetErrorHandle(self,err : bool) -> None: 
        """
        Allows controlling whether exception raisings are handled If err is False, they are not (hence, dbx can take control) If err is True, they are, and they are traced (by putting on messenger Entity's Number and file record num) Default given at Model's creation time is True
        """
    def SetMessenger(self,messenger : OCP.Message.Message_Messenger) -> None: 
        """
        Sets Messenger used for outputting messages
        """
    def SetModel(self,amodel : Interface_InterfaceModel) -> None: 
        """
        Stores a Model. Used when the Model has been loaded
        """
    def SetTraceLevel(self,tracelev : int) -> None: 
        """
        Sets trace level used for outputting messages - 0: no trace at all - 1: errors - 2: errors and warnings - 3: all messages Default is 1 : Errors traced
        """
    def TraceLevel(self) -> int: 
        """
        Returns trace level used for outputting messages.
        """
    def UnknownEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Provides an unknown entity, specific to the Interface called by SetEntities when Recognize has failed (Unknown alone) or by LoadModel when an Entity has caused a Fail on reading (to keep at least its literal description) Uses Protocol to do it
        """
    pass
class Interface_FloatWriter():
    """
    This class converts a floating number (Real) to a string It can be used if the standard C-C++ output functions (sprintf or std::cout<<) are not convenient. That is to say : - to suppress trailing '0' and 'E+00' (if desired) - to control exponent output and floating point output
    """
    @staticmethod
    def Convert_s(val : float,text : str,zerosup : bool,Range1 : float,Range2 : float,mainform : str,rangeform : str) -> int: 
        """
        This class method converts a Real Value to a string, given options given as arguments. It can be called independently. Warning : even if declared in, content of <text> will be modified
        """
    def FormatForRange(self) -> str: 
        """
        Returns the format for range, if set Meaningful only if <range> from Options is True was C++ : return const
        """
    def MainFormat(self) -> str: 
        """
        Returns the main format was C++ : return const
        """
    def Options(self) -> Tuple[bool, bool, float, float]: 
        """
        Returns active options : <zerosup> is the option ZeroSuppress, <range> is True if a range is set, False else R1,R2 give the range (if it is set)
        """
    def SetDefaults(self,chars : int=0) -> None: 
        """
        Sets again options to the defaults given by Create
        """
    def SetFormat(self,form : str,reset : bool=True) -> None: 
        """
        Sets a specific Format for Sending Reals (main format) (Default from Creation is "%E") If <reset> is given True (default), this call clears effects of former calls to SetFormatForRange and SetZeroSuppress
        """
    def SetFormatForRange(self,form : str,R1 : float,R2 : float) -> None: 
        """
        Sets a secondary Format for Real, to be applied between R1 and R2 (in absolute values). A Call to SetRealForm cancels this secondary form if <reset> is True. (Default from Creation is "%f" between 0.1 and 1000.) Warning : if the condition (0. <= R1 < R2) is not fulfilled, this secondary form is canceled.
        """
    def SetZeroSuppress(self,mode : bool) -> None: 
        """
        Sets Sending Real Parameters to suppress trailing Zeros and Null Exponent ("E+00"), if <mode> is given True, Resets this mode if <mode> is False (in addition to Real Forms) A call to SetRealFrom resets this mode to False ig <reset> is given True (Default from Creation is True)
        """
    def Write(self,val : float,text : str) -> int: 
        """
        Writes a Real value <val> to a string <text> by using the options. Returns the useful Length of produced string. It calls the class method Convert. Warning : <text> is assumed to be wide enough (20-30 is correct) And, even if declared in, its content will be modified
        """
    def __init__(self,chars : int=0) -> None: ...
    pass
class Interface_GTool(OCP.Standard.Standard_Transient):
    """
    GTool - General Tool for a Model Provides the functions performed by Protocol/GeneralModule for entities of a Model, and recorded in a GeneralLib Optimized : once an entity has been queried, the GeneralLib is not longer queried Shareable between several users : as a HandleGTool - General Tool for a Model Provides the functions performed by Protocol/GeneralModule for entities of a Model, and recorded in a GeneralLib Optimized : once an entity has been queried, the GeneralLib is not longer queried Shareable between several users : as a HandleGTool - General Tool for a Model Provides the functions performed by Protocol/GeneralModule for entities of a Model, and recorded in a GeneralLib Optimized : once an entity has been queried, the GeneralLib is not longer queried Shareable between several users : as a Handle
    """
    def ClearEntities(self) -> None: 
        """
        Clears the maps which record, for each already recorded entity its Module and Case Number
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
    def Lib(self) -> Interface_GeneralLib: 
        """
        Returns the GeneralLib itself
        """
    def Protocol(self) -> Interface_Protocol: 
        """
        Returns the Protocol. Warning : it can be Null
        """
    def Reservate(self,nb : int,enforce : bool=False) -> None: 
        """
        Reservates maps for a count of entities <enforce> False : minimum count <enforce> True : clears former reservations Does not clear the maps
        """
    def Select(self,ent : OCP.Standard.Standard_Transient,gmod : Interface_GeneralModule,CN : int,enforce : bool=False) -> bool: 
        """
        Selects for an entity, its Module and Case Number It is optimised : once done for each entity, the result is mapped and the GeneralLib is not longer queried <enforce> True overpasses this optimisation
        """
    def SetProtocol(self,proto : Interface_Protocol,enforce : bool=False) -> None: 
        """
        Sets a new Protocol if <enforce> is False and the new Protocol equates the old one then nothing is done
        """
    def SetSignType(self,sign : Interface_SignType) -> None: 
        """
        Sets a new SignType
        """
    def SignName(self) -> str: 
        """
        Returns the Name of the SignType, or "Class Name"
        """
    def SignType(self) -> Interface_SignType: 
        """
        Returns the SignType. Can be null
        """
    def SignValue(self,ent : OCP.Standard.Standard_Transient,model : Interface_InterfaceModel) -> str: 
        """
        Returns the Signature for a Transient Object in a Model It calls SignType to do that If SignType is not defined, return ClassName of <ent>
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,proto : Interface_Protocol,nbent : int=0) -> None: ...
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
class Interface_GeneralLib():
    """
    None
    """
    def AddProtocol(self,aprotocol : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds a couple (Module-Protocol) to the Library, given the class of a Protocol. Takes Resources into account. (if <aprotocol> is not of type TheProtocol, it is not added)
        """
    def Clear(self) -> None: 
        """
        Clears the list of Modules of a library (can be used to redefine the order of Modules before action : Clear then refill the Library by calls to AddProtocol)
        """
    def Module(self) -> Interface_GeneralModule: 
        """
        Returns the current Module in the Iteration
        """
    def More(self) -> bool: 
        """
        Returns True if there are more Modules to iterate on
        """
    def Next(self) -> None: 
        """
        Iterates by getting the next Module in the list If there is none, the exception will be raised by Value
        """
    def Protocol(self) -> Interface_Protocol: 
        """
        Returns the current Protocol in the Iteration
        """
    def Select(self,obj : OCP.Standard.Standard_Transient,module : Interface_GeneralModule,CN : int) -> bool: 
        """
        Selects a Module from the Library, given an Object. Returns True if Select has succeeded, False else. Also Returns (as arguments) the selected Module and the Case Number determined by the associated Protocol. If Select has failed, <module> is Null Handle and CN is zero. (Select can work on any criterium, such as Object DynamicType)
        """
    def SetComplete(self) -> None: 
        """
        Sets a library to be defined with the complete Global list (all the couples Protocol/Modules recorded in it)
        """
    @staticmethod
    def SetGlobal_s(amodule : Interface_GeneralModule,aprotocol : Interface_Protocol) -> None: 
        """
        Adds a couple (Module-Protocol) into the global definition set for this class of Library.
        """
    def Start(self) -> None: 
        """
        Starts Iteration on the Modules (sets it on the first one)
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aprotocol : Interface_Protocol) -> None: ...
    pass
class Interface_GeneralModule(OCP.Standard.Standard_Transient):
    """
    This class defines general services, which must be provided for each type of Entity (i.e. of Transient Object processed by an Interface) : Shared List, Check, Copy, Delete, CategoryThis class defines general services, which must be provided for each type of Entity (i.e. of Transient Object processed by an Interface) : Shared List, Check, Copy, Delete, CategoryThis class defines general services, which must be provided for each type of Entity (i.e. of Transient Object processed by an Interface) : Shared List, Check, Copy, Delete, Category
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" Remark that it should be in phase with the implementation of NewVoid+CopyCase/NewCopyCase Default returns always False, can be redefined
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : Interface_ShareTool) -> int: 
        """
        Returns a category number which characterizes an entity Category Numbers are managed by the class Category <shares> can be used to evaluate this number in the context Default returns 0 which means "unspecified"
        """
    def CheckCase(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : Interface_ShareTool,ach : Interface_Check) -> Any: 
        """
        Specific Checking of an Entity <ent> Can check context queried through a ShareTool, as required
        """
    def CopyCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : Interface_CopyTool) -> None: 
        """
        Specific Copy ("Deep") from <entfrom> to <entto> (same type) by using a CopyTool which provides its working Map. Use method Transferred from CopyTool to work
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : Interface_CopyTool) -> bool: 
        """
        Dispatches an entity Returns True if it works by copy, False if it just duplicates the starting Handle
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FillShared(self,model : Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : Interface_EntityIterator) -> None: 
        """
        Specific filling of the list of Entities shared by an Entity <ent>, according a Case Number <CN> (formerly computed by CaseNum), considered in the context of a Model <model> Default calls FillSharedCase (i.e., ignores the model) Can be redefined to use the model for working
        """
    def FillSharedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : Interface_EntityIterator) -> None: 
        """
        Specific filling of the list of Entities shared by an Entity <ent>, according a Case Number <CN> (formerly computed by CaseNum). Can use the internal utility method Share, below
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
    def ListImplied(self,model : Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> considered in the context of a Model <model> : i.e. the Entities which are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillShared + ListImplied give the complete list of References Default calls ListImpliedCase (i.e. ignores the model) Can be redefined to use the model for working
        """
    def ListImpliedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> (see above) are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillSharedCase + ListImpliedCase give the complete list of Referenced Entities The provided default method does nothing (Implied References are specific of a little amount of Entity Classes).
        """
    def Name(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : Interface_ShareTool) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Determines if an entity brings a Name (or widerly, if a Name can be attached to it, through the ShareTool By default, returns a Null Handle (no name can be produced) Can be redefined
        """
    def NewCopiedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : Interface_CopyTool) -> bool: 
        """
        Specific operator (create+copy) defaulted to do nothing. It can be redefined : When it is not possible to work in two steps (NewVoid then CopyCase). This can occur when there is no default constructor : hence the result <entto> must be created with an effective definition. Remark : if NewCopiedCase is defined, CopyCase has nothing to do Returns True if it has produced something, false else
        """
    def NewVoid(self,CN : int,entto : OCP.Standard.Standard_Transient) -> bool: 
        """
        Creates a new void entity <entto> according to a Case Number This entity remains to be filled, by reading from a file or by copying from another entity of same type (see CopyCase)
        """
    def RenewImpliedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : Interface_CopyTool) -> None: 
        """
        Specific Copying of Implied References A Default is provided which does nothing (must current case !) Already copied references (by CopyFrom) must remain unchanged Use method Search from CopyTool to work
        """
    def Share(self,iter : Interface_EntityIterator,shared : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an Entity to a Shared List (uses GetOneItem on <iter>)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WhenDeleteCase(self,CN : int,ent : OCP.Standard.Standard_Transient,dispatched : bool) -> None: 
        """
        Prepares an entity to be deleted. What does it mean : Basically, any class of entity may define its own destructor By default, it does nothing but calling destructors on fields With the Memory Manager, it is useless to call destructor, it is done automatically when the Handle is nullified(cleared) BUT this is ineffective in looping structures (whatever these are "Implied" references or not).
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
class Interface_GlobalNodeOfGeneralLib(OCP.Standard.Standard_Transient):
    def Add(self,amodule : Interface_GeneralModule,aprotocol : Interface_Protocol) -> None: 
        """
        Adds a Module bound with a Protocol to the list : does nothing if already in the list, THAT IS, Same Type (exact match) and Same State (that is, IsEqual is not required) Once added, stores its attached Protocol in correspondence
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
    def Module(self) -> Interface_GeneralModule: 
        """
        Returns the Module stored in a given GlobalNode
        """
    def Next(self) -> Interface_GlobalNodeOfGeneralLib: 
        """
        Returns the Next GlobalNode. If none is defined, returned value is a Null Handle
        """
    def Protocol(self) -> Interface_Protocol: 
        """
        Returns the attached Protocol stored in a given GlobalNode
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
class Interface_GlobalNodeOfReaderLib(OCP.Standard.Standard_Transient):
    def Add(self,amodule : Interface_ReaderModule,aprotocol : Interface_Protocol) -> None: 
        """
        Adds a Module bound with a Protocol to the list : does nothing if already in the list, THAT IS, Same Type (exact match) and Same State (that is, IsEqual is not required) Once added, stores its attached Protocol in correspondence
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
    def Module(self) -> Interface_ReaderModule: 
        """
        Returns the Module stored in a given GlobalNode
        """
    def Next(self) -> Interface_GlobalNodeOfReaderLib: 
        """
        Returns the Next GlobalNode. If none is defined, returned value is a Null Handle
        """
    def Protocol(self) -> Interface_Protocol: 
        """
        Returns the attached Protocol stored in a given GlobalNode
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
class Interface_Graph():
    """
    Gives basic data structure for operating and storing graph results (usage is normally internal) Entities are Mapped according their Number in the Model
    """
    def BitMap(self) -> Interface_BitMap: 
        """
        Returns the Bit Map in order to read or edit flag values
        """
    def CBitMap(self) -> Interface_BitMap: 
        """
        Returns the Bit Map in order to edit it (add new flags)
        """
    def ChangeStatus(self,oldstat : int,newstat : int) -> None: 
        """
        Changes all status which value is oldstat to new value newstat
        """
    def Entity(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns mapped Entity given its no (if it is present)
        """
    def EntityNumber(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the Number of the entity in the Map, computed at creation time (Entities loaded from the Model) Returns 0 if <ent> not contained by Model used to create <me> (that is, <ent> is unknown from <me>)
        """
    @overload
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient,shared : bool,newstat : int,overlapstat : int,cumul : bool) -> None: 
        """
        Gets an Entity, plus its shared ones (at every level) if "shared" is True. New items are set to status "newstat" Items already present in graph remain unchanged Of course, redefinitions of Shared lists are taken into account if there are some

        Gets an Entity, plus its shared ones (at every level) if "shared" is True. New items are set to status "newstat". Items already present in graph are processed as follows : - if they already have status "newstat", they remain unchanged - if they have another status, this one is modified : if cumul is True, to former status + overlapstat (cumul) if cumul is False, to overlapstat (enforce)
        """
    @overload
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient,shared : bool,newstat : int=0) -> None: ...
    @overload
    def GetFromGraph(self,agraph : Interface_Graph,stat : int) -> None: 
        """
        Gets all present items from another graph

        Gets items from another graph which have a specific Status
        """
    @overload
    def GetFromGraph(self,agraph : Interface_Graph) -> None: ...
    @overload
    def GetFromIter(self,iter : Interface_EntityIterator,newstat : int,overlapstat : int,cumul : bool) -> None: 
        """
        Gets Entities given by an EntityIterator. Entities which were not yet present in the graph are mapped with status "newstat" Entities already present remain unchanged

        Gets Entities given by an EntityIterator and distinguishes those already present in the Graph : - new entities added to the Graph with status "newstst" - entities already present with status = "newstat" remain unchanged - entities already present with status different form "newstat" have their status modified : if cumul is True, to former status + overlapstat (cumul) if cumul is False, to overlapstat (enforce) (Note : works as GetEntity, shared = False, for each entity)
        """
    @overload
    def GetFromIter(self,iter : Interface_EntityIterator,newstat : int) -> None: ...
    def GetFromModel(self) -> None: 
        """
        Loads Graph with all Entities contained in the Model
        """
    def GetShareds(self,ent : OCP.Standard.Standard_Transient) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the sequence of Entities Shared by an Entity
        """
    def GetSharings(self,ent : OCP.Standard.Standard_Transient) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the sequence of Entities Sharings by an Entity
        """
    def HasShareErrors(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> or the list of entities shared by <ent> (not redefined) contains items unknown from this Graph Remark : apart from the status HasShareError, these items are ignored
        """
    @overload
    def IsPresent(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is noted as present in the graph (See methods Get... which determine this status) Returns False if <num> is out of range too

        Same as above but directly on an Entity <ent> : if it is not contained in the Model, returns False. Else calls IsPresent(num) with <num> given by EntityNumber
        """
    @overload
    def IsPresent(self,num : int) -> bool: ...
    def ModeStat(self) -> bool: 
        """
        Returns mode responsible for computation of statuses;
        """
    def Model(self) -> Interface_InterfaceModel: 
        """
        Returns the Model with which this Graph was created
        """
    def Name(self,ent : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Determines the name attached to an entity, by using the general service Name in GeneralModule Returns a null handle if no name could be computed or if the entity is not in the model
        """
    def NbStatuses(self) -> int: 
        """
        Returns size of array of statuses
        """
    def RemoveItem(self,num : int) -> None: 
        """
        Clears Entity and sets Status to 0, for a numero
        """
    def RemoveStatus(self,stat : int) -> None: 
        """
        Removes all items of which status has a given value stat
        """
    def Reset(self) -> None: 
        """
        Erases data, making graph ready to rebegin from void (also resets Shared lists redefinitions)
        """
    def ResetStatus(self) -> None: 
        """
        Erases Status (Values and Flags of Presence), making graph ready to rebegin from void. Does not concerns Shared lists
        """
    def RootEntities(self) -> Interface_EntityIterator: 
        """
        Returns the Entities which are not Shared (their Sharing List is empty) in the Model
        """
    def SetStatus(self,num : int,stat : int) -> None: 
        """
        Modifies Status associated to a numero
        """
    def Shareds(self,ent : OCP.Standard.Standard_Transient) -> Interface_EntityIterator: 
        """
        Returns the list of Entities Shared by an Entity, as recorded by the Graph. That is, by default Basic Shared List, else it can be redefined by methods SetShare, SetNoShare ... see below
        """
    def SharingTable(self) -> OCP.TColStd.TColStd_HArray1OfListOfInteger: 
        """
        Returns the Table of Sharing lists. Used to Create another Graph from <me>
        """
    def Sharings(self,ent : OCP.Standard.Standard_Transient) -> Interface_EntityIterator: 
        """
        Returns the list of Entities which Share an Entity, computed from the Basic or Redefined Shared Lists
        """
    def Size(self) -> int: 
        """
        Returns size (max nb of entities, i.e. Model's nb of entities)
        """
    def Status(self,num : int) -> int: 
        """
        Returns Status associated to a numero (only to read it)
        """
    def TypedSharings(self,ent : OCP.Standard.Standard_Transient,type : OCP.Standard.Standard_Type) -> Interface_EntityIterator: 
        """
        Returns the list of sharings entities, AT ANY LEVEL, which are kind of a given type. A sharing entity kind of this type ends the exploration of its branch
        """
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,theModeStats : bool=True) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,protocol : Interface_Protocol,theModeStats : bool=True) -> None: ...
    @overload
    def __init__(self,agraph : Interface_Graph,copied : bool=False) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,gtool : Interface_GTool,theModeStats : bool=True) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,lib : Interface_GeneralLib,theModeStats : bool=True) -> None: ...
    pass
class Interface_GraphContent(Interface_EntityIterator):
    """
    Defines general form for classes of graph algorithms on Interfaces, this form is that of EntityIterator Each sub-class fills it according to its own algorithm This also allows to combine any graph result to others, all being given under one unique form
    """
    def AddItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds to the iteration list a defined entity
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Gets a list of entities and adds its to the iteration list
        """
    def Begin(self) -> None: 
        """
        Does the Evaluation before starting the iteration itself (in out)
        """
    def Content(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the content of the Iterator, accessed through a Handle to be used by a frontal-engine logic Returns an empty Sequence if the Iterator is empty Calls Start if not yet done
        """
    def Destroy(self) -> None: 
        """
        Clears data of iteration
        """
    def Evaluate(self) -> None: 
        """
        Evaluates list of Entities to be iterated. Called by Start Default is set to doing nothing : intended to be redefined by each sub-class
        """
    @overload
    def GetFromGraph(self,agraph : Interface_Graph,stat : int) -> None: 
        """
        Gets all Entities designated by a Graph (once created), adds them to those already recorded

        Gets entities from a graph which have a specific Status value (one created), adds them to those already recorded
        """
    @overload
    def GetFromGraph(self,agraph : Interface_Graph) -> None: ...
    def GetOneItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        same as AddItem (kept for compatibility)
        """
    def More(self) -> bool: 
        """
        Says if there are other entities (vertices) to iterate the first time, calls Start
        """
    def NbEntities(self) -> int: 
        """
        Returns count of entities which will be iterated on Calls Start if not yet done
        """
    def NbTyped(self,type : OCP.Standard.Standard_Type) -> int: 
        """
        Returns count of entities of a given type (kind of)
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next entity (vertex) to give
        """
    def Result(self) -> Interface_EntityIterator: 
        """
        Returns Result under the exact form of an EntityIterator : Can be used when EntityIterator itself is required (as a returned value for instance), without way for a sub-class
        """
    def SelectType(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects entities with are Kind of a given type, keep only them (is keep is True) or reject only them (if keep is False)
        """
    def Start(self) -> None: 
        """
        Allows re-iteration (useless for the first iteration)
        """
    def Typed(self,type : OCP.Standard.Standard_Type) -> Interface_EntityIterator: 
        """
        Returns the list of entities of a given type (kind of)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current Entity iterated, to be used by Interface tools
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,agraph : Interface_Graph,ent : OCP.Standard.Standard_Transient) -> None: ...
    @overload
    def __init__(self,agraph : Interface_Graph) -> None: ...
    @overload
    def __init__(self,agraph : Interface_Graph,stat : int) -> None: ...
    pass
class Interface_HArray1OfHAsciiString(Interface_Array1OfHAsciiString, OCP.Standard.Standard_Transient):
    def Array1(self) -> Interface_Array1OfHAsciiString: 
        """
        None
        """
    def Assign(self,theOther : Interface_Array1OfHAsciiString) -> Interface_Array1OfHAsciiString: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Interface_Array1OfHAsciiString: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Variable value access
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
    def First(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : Interface_Array1OfHAsciiString) -> Interface_Array1OfHAsciiString: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Interface_Array1OfHAsciiString) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class Interface_HGraph(OCP.Standard.Standard_Transient):
    """
    This class allows to store a redefinable Graph, via a Handle (useful for an Object which can work on several successive Models, with the same general conditions)This class allows to store a redefinable Graph, via a Handle (useful for an Object which can work on several successive Models, with the same general conditions)This class allows to store a redefinable Graph, via a Handle (useful for an Object which can work on several successive Models, with the same general conditions)
    """
    def CGraph(self) -> Interface_Graph: 
        """
        Same as above, but for Read-Write Operations Then, The Graph will be modified in the HGraph itself
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
    def Graph(self) -> Interface_Graph: 
        """
        Returns the Graph contained in <me>, for Read Only Operations Remark that it is returns as "const &" Getting it in a new variable instead of a reference would be a pity, because all the graph's content would be duplicated
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
    @overload
    def __init__(self,agraph : Interface_Graph) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,gtool : Interface_GTool,theModeStats : bool=True) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,theModeStats : bool=True) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,protocol : Interface_Protocol,theModeStats : bool=True) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,lib : Interface_GeneralLib,theModeStats : bool=True) -> None: ...
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
class Interface_SequenceOfCheck(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Interface_SequenceOfCheck) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Interface_Check) -> None: ...
    def Assign(self,theOther : Interface_SequenceOfCheck) -> Interface_SequenceOfCheck: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Interface_Check: 
        """
        First item access
        """
    def ChangeLast(self) -> Interface_Check: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Interface_Check: 
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
    def First(self) -> Interface_Check: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Interface_SequenceOfCheck) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Interface_Check) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Interface_Check) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Interface_SequenceOfCheck) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Interface_Check: 
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
    def Prepend(self,theItem : Interface_Check) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Interface_SequenceOfCheck) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Interface_Check) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Interface_SequenceOfCheck) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Interface_Check: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Interface_SequenceOfCheck) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Interface_IndexedMapOfAsciiString(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Interface_IndexedMapOfAsciiString) -> Interface_IndexedMapOfAsciiString: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : Interface_IndexedMapOfAsciiString) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,theExtent : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theOther : Interface_IndexedMapOfAsciiString) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class Interface_IntList():
    """
    This class detains the data which describe a Graph. A Graph has two lists, one for shared refs, one for sharing refs (the reverses). Each list comprises, for each Entity of the Model of the Graph, a list of Entities (shared or sharing). In fact, entities are identified by their numbers in the Model or Graph : this gives better performances.
    """
    def Add(self,ref : int) -> None: 
        """
        Adds a reference (as an integer value, an entity number) to the current entity number. Zero is ignored
        """
    def AdjustSize(self,margin : int=0) -> None: 
        """
        Resizes lists to exact sizes. For list of refs, a positive margin can be added.
        """
    def Clear(self) -> None: 
        """
        Clears all data, hence each entity number has an empty list
        """
    def Initialize(self,nbe : int) -> None: 
        """
        Initialize IntList by number of entities.
        """
    def Internals(self,ents : OCP.TColStd.TColStd_HArray1OfInteger,refs : OCP.TColStd.TColStd_HArray1OfInteger) -> Tuple[int]: 
        """
        Returns internal values, used for copying
        """
    def IsRedefined(self,num : int=0) -> bool: 
        """
        Returns True if the list for a number (default is taken as current) is "redefined" (useful for empty list)
        """
    def Length(self) -> int: 
        """
        Returns the count of refs attached to current entity number
        """
    def List(self,number : int,copied : bool=False) -> Interface_IntList: 
        """
        Returns an IntList, identical to <me> but set to a specified entity Number By default, not copied (in order to be read) Specified <copied> to produce another list and edit it
        """
    def NbEntities(self) -> int: 
        """
        Returns count of entities to be aknowledged
        """
    def Number(self) -> int: 
        """
        Returns the current entity number
        """
    def Remove(self,num : int) -> bool: 
        """
        Removes an item in the list for current number, given its rank Returns True if done, False else
        """
    def Reservate(self,count : int) -> None: 
        """
        Makes a reservation for <count> references to be later attached to the current entity. If required, it increases the size of array used to store refs. Remark that if count is less than two, it does nothing (because immediate storing)
        """
    def SetNbEntities(self,nbe : int) -> None: 
        """
        Changes the count of entities (ignored if decreased)
        """
    def SetNumber(self,number : int) -> None: 
        """
        Sets an entity number as current (for read and fill)
        """
    def SetRedefined(self,mode : bool) -> None: 
        """
        Sets current entity list to be redefined or not This is used in a Graph for redefinition list : it can be disable (no redefinition, i.e. list is cleared), or enabled (starts as empty). The original list has not to be "redefined"
        """
    def Value(self,num : int) -> int: 
        """
        Returns a reference number in the list for current number, according to its rank
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,other : Interface_IntList,copied : bool) -> None: ...
    @overload
    def __init__(self,nbe : int) -> None: ...
    pass
class Interface_IntVal(OCP.Standard.Standard_Transient):
    """
    An Integer through a Handle (i.e. managed as TShared)An Integer through a Handle (i.e. managed as TShared)An Integer through a Handle (i.e. managed as TShared)
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> int: 
        """
        None
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
    def CValue(self) -> int:
        """
        None

        :type: int
        """
    @CValue.setter
    def CValue(self, arg1: int) -> None:
        """
        None
        """
    pass
class Interface_InterfaceError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Interface', '__weakref__': <attribute '__weakref__' of 'Interface_InterfaceError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Interface_InterfaceError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Interface_InterfaceMismatch(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Interface', '__weakref__': <attribute '__weakref__' of 'Interface_InterfaceMismatch' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Interface_InterfaceMismatch' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Interface_InterfaceModel(OCP.Standard.Standard_Transient):
    """
    Defines an (Indexed) Set of data corresponding to a complete Transfer by a File Interface, i.e. File Header and Transient Entities (Objects) contained in a File. Contained Entities are identified in the Model by unique and consecutive Numbers.Defines an (Indexed) Set of data corresponding to a complete Transfer by a File Interface, i.e. File Header and Transient Entities (Objects) contained in a File. Contained Entities are identified in the Model by unique and consecutive Numbers.Defines an (Indexed) Set of data corresponding to a complete Transfer by a File Interface, i.e. File Header and Transient Entities (Objects) contained in a File. Contained Entities are identified in the Model by unique and consecutive Numbers.
    """
    def AddEntity(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Internal method for adding an Entity. Used by file reading (defined by each Interface) and Transfer tools. It adds the entity required to be added, not its refs : see AddWithRefs. If <anentity> is a ReportEntity, it is added to the list of Reports, its Concerned Entity (Erroneous or Corrected, else Unknown) is added to the list of Entities. That is, the ReportEntity must be created before Adding
        """
    def AddReportEntity(self,rep : Interface_ReportEntity,semantic : bool=False) -> bool: 
        """
        Adds a ReportEntity as such. Returns False if the concerned entity is not recorded in the Model Else, adds it into, either the main report list or the list for semantic checks, then returns True
        """
    @overload
    def AddWithRefs(self,anent : OCP.Standard.Standard_Transient,lib : Interface_GeneralLib,level : int=0,listall : bool=False) -> None: 
        """
        Adds to the Model, an Entity with all its References, as they are defined by General Services FillShared and ListImplied. Process is recursive (any sub-levels) if <level> = 0 (Default) Else, adds sub-entities until the required sub-level. Especially, if <level> = 1, adds immediate subs and that's all

        Same as above, but works with the Protocol of the Model

        Same as above, but works with an already created GeneralLib
        """
    @overload
    def AddWithRefs(self,anent : OCP.Standard.Standard_Transient,proto : Interface_Protocol,level : int=0,listall : bool=False) -> None: ...
    @overload
    def AddWithRefs(self,anent : OCP.Standard.Standard_Transient,level : int=0,listall : bool=False) -> None: ...
    def CategoryNumber(self,num : int) -> int: 
        """
        Returns the recorded category number for a given entity number 0 if none was defined for this entity
        """
    def ChangeOrder(self,oldnum : int,newnum : int,count : int=1) -> None: 
        """
        Changes the Numbers of some Entities : <oldnum> is moved to <newnum>, same for <count> entities. Thus : 1,2 ... newnum-1 newnum ... oldnum .. oldnum+count oldnum+count+1 .. gives 1,2 ... newnum-1 oldnum .. oldnum+count newnum ... oldnum+count+1 (can be seen as a circular permutation)
        """
    def Check(self,num : int,syntactic : bool) -> Interface_Check: 
        """
        Returns the check attached to an entity, designated by its Number. 0 for global check <semantic> True : recorded semantic check <semantic> False : recorded syntactic check (see ReportEntity) If no check is recorded for <num>, returns an empty Check
        """
    @staticmethod
    def ClassName_s(typnam : str) -> str: 
        """
        From a CDL Type Name, returns the Class part (package dropped) WARNING : buffered, to be immediately copied or printed
        """
    def Clear(self) -> None: 
        """
        Erases contained data; used when a Model is copied to others : the new copied ones begin from clear Clear calls specific method ClearHeader (see below)
        """
    def ClearEntities(self) -> None: 
        """
        Clears the entities; uses the general service WhenDelete, in addition to the standard Memory Manager; can be redefined
        """
    def ClearHeader(self) -> None: 
        """
        Clears Model's header : specific to each norm
        """
    def ClearLabels(self) -> None: 
        """
        Erases information about labels, if any : specific to each norm
        """
    def ClearReportEntity(self,num : int) -> bool: 
        """
        Removes the ReportEntity attached to Entity <num>. Returns True if done, False if no ReportEntity was attached to <num>. Warning : the caller must assume that this clearing is meaningful
        """
    def Contains(self,anentity : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if a Model contains an Entity (for a ReportEntity, looks for the ReportEntity itself AND its Concerned Entity)
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Destroy(self) -> None: 
        """
        Clears the list of entities (service WhenDelete)
        """
    def DumpHeader(self,S : io.BytesIO,level : int=0) -> None: 
        """
        Dumps Header in a short, easy to read, form, onto a Stream <level> allows to print more or less parts of the header, if necessary. 0 for basic print
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Entities(self) -> Interface_EntityIterator: 
        """
        Returns the list of all Entities, as an Iterator on Entities (the Entities themselves, not the Reports)
        """
    def EntityState(self,num : int) -> Interface_DataState: 
        """
        Returns the State of an entity, given its number
        """
    def FillIterator(self,iter : Interface_EntityIterator) -> None: 
        """
        Allows an EntityIterator to get a list of Entities
        """
    def FillSemanticChecks(self,checks : Interface_CheckIterator,clear : bool=True) -> None: 
        """
        Fills the list of semantic checks. This list is computed (by CheckTool). Hence, it can be stored in the model for later queries <clear> True (D) : new list replaces <clear> False : new list is cumulated
        """
    def GTool(self) -> Interface_GTool: 
        """
        Returns the GTool, set by SetProtocol or by SetGTool
        """
    def GetFromAnother(self,other : Interface_InterfaceModel) -> None: 
        """
        Gets header (data specific of a defined Interface) from another InterfaceModel; called from TransferCopy
        """
    def GetFromTransfer(self,aniter : Interface_EntityIterator) -> None: 
        """
        Gets contents from an EntityIterator, prepared by a Transfer tool (e.g TransferCopy). Starts from clear
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlobalCheck(self,syntactic : bool=True) -> Interface_Check: 
        """
        Returns the GlobalCheck, which memorizes messages global to the file (not specific to an Entity), especially Header
        """
    def HasSemanticChecks(self) -> bool: 
        """
        Returns True if semantic checks have been filled
        """
    @staticmethod
    def HasTemplate_s(name : str) -> bool: 
        """
        Returns true if a template is attached to a given name
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsErrorEntity(self,num : int) -> bool: 
        """
        Returns True if <num> identifies an Error Entity : in this case, a ReportEntity brings Fail Messages and possibly an "undefined" Content, see IsRedefinedEntity
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
    def IsRedefinedContent(self,num : int) -> bool: 
        """
        Returns True if <num> identifies an Entity which content is redefined through a ReportEntity (i.e. with literal data only) This happens when an entity is syntactically erroneous in the way that its basic content remains empty. For more details (such as content itself), see ReportEntity
        """
    def IsReportEntity(self,num : int,semantic : bool=False) -> bool: 
        """
        Returns True if <num> identifies a ReportEntity in the Model Hence, ReportEntity can be called.
        """
    def IsUnknownEntity(self,num : int) -> bool: 
        """
        Returns True if <num> identifies an Unknown Entity : in this case, a ReportEntity with no Check Messages designates it.
        """
    @staticmethod
    def ListTemplates_s() -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the complete list of names attached to template models
        """
    def NbEntities(self) -> int: 
        """
        Returns count of contained Entities
        """
    def NbTypes(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the count of DISTINCT types under which an entity may be processed. Defined by the Protocol, which gives default as 1 (dynamic Type).
        """
    def NewEmptyModel(self) -> Interface_InterfaceModel: 
        """
        Returns a New Empty Model, same type as <me> (whatever its Type); called to Copy parts a Model into other ones, then followed by a call to GetFromAnother (Header) then filling with specified Entities, themselves copied
        """
    def NextNumberForLabel(self,label : str,lastnum : int=0,exact : bool=True) -> int: 
        """
        Searches a label which matches with one entity. Begins from <lastnum>+1 (default:1) and scans the entities until <NbEntities>. For the first which matches <label>, this method returns its Number. Returns 0 if nothing found Can be called recursively (labels are not specified as unique) <exact> : if True (default), exact match is required else, checks the END of entity label
        """
    def Number(self,anentity : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the Number of an Entity in the Model if it contains it. Else returns 0. For a ReportEntity, looks at Concerned Entity. Returns the Directory entry Number of an Entity in the Model if it contains it. Else returns 0. For a ReportEntity, looks at Concerned Entity.
        """
    def Print(self,ent : OCP.Standard.Standard_Transient,s : io.BytesIO,mode : int=0) -> None: 
        """
        Prints identification of a given entity in <me>, in order to be printed in a list or phrase <mode> < 0 : prints only its number <mode> = 1 : just calls PrintLabel <mode> = 0 (D) : prints its number plus '/' plus PrintLabel If <ent> == <me>, simply prints "Global" If <ent> is unknown, prints "??/its type"
        """
    def PrintLabel(self,ent : OCP.Standard.Standard_Transient,S : io.BytesIO) -> None: 
        """
        Prints label specific to each norm, for a given entity. Must only print label itself, in order to be included in a phrase. Can call the result of StringLabel, but not obliged.
        """
    def PrintToLog(self,ent : OCP.Standard.Standard_Transient,S : io.BytesIO) -> None: 
        """
        Prints label specific to each norm in log format, for a given entity. By default, just calls PrintLabel, can be redefined
        """
    def Protocol(self) -> Interface_Protocol: 
        """
        Returns the Protocol which has been set by SetProtocol, or AddWithRefs with Protocol
        """
    def Redefineds(self) -> Interface_EntityIterator: 
        """
        Returns the list of ReportEntities which redefine data (generally, if concerned entity is "Error", a literal content is added to it : this is a "redefined entity"
        """
    def ReplaceEntity(self,nument : int,anent : OCP.Standard.Standard_Transient) -> None: 
        """
        Replace Entity with Number=nument on other entity - "anent"
        """
    def ReportEntity(self,num : int,semantic : bool=False) -> Interface_ReportEntity: 
        """
        Returns a ReportEntity identified by its number in the Model, or a Null Handle If <num> does not identify a ReportEntity.
        """
    def Reports(self,semantic : bool=False) -> Interface_EntityIterator: 
        """
        Returns the list of all ReportEntities, i.e. data about Entities read with Error or Warning information (each item has to be casted to Report Entity then it can be queried for Concerned Entity, Content, Check ...) By default, returns the main reports, is <semantic> is True it returns the list for semantic checks
        """
    def Reservate(self,nbent : int) -> None: 
        """
        Does a reservation for the List of Entities (for optimized storage management). If it is not called, storage management can be less efficient. <nbent> is the expected count of Entities to store
        """
    def ReverseOrders(self,after : int=0) -> None: 
        """
        Reverses the Numbers of the Entities, between <after> and the total count of Entities. Thus, the entities : 1,2 ... after, after+1 ... nb-1, nb become numbered as : 1,2 ... after, nb, nb-1 ... after+1 By default (after = 0) the whole list of Entities is reversed
        """
    def SetCategoryNumber(self,num : int,val : int) -> bool: 
        """
        Records a category number for an entity number Returns True when done, False if <num> is out of range
        """
    def SetGTool(self,gtool : Interface_GTool) -> None: 
        """
        Sets a GTool for this model, which already defines a Protocol
        """
    def SetGlobalCheck(self,ach : Interface_Check) -> None: 
        """
        Allows to modify GlobalCheck, after getting then completing it Remark : it is SYNTACTIC check. Semantics, see FillChecks
        """
    def SetProtocol(self,proto : Interface_Protocol) -> None: 
        """
        Sets a Protocol for this Model It is also set by a call to AddWithRefs with Protocol It is used for : DumpHeader (as required), ClearEntities ...
        """
    def SetReportEntity(self,num : int,rep : Interface_ReportEntity) -> bool: 
        """
        Sets or Replaces a ReportEntity for the Entity <num>. Returns True if Report is replaced, False if it has been replaced Warning : the caller must assume that this setting is meaningful
        """
    @staticmethod
    def SetTemplate_s(name : str,model : Interface_InterfaceModel) -> bool: 
        """
        Records a new template model with a name. If the name was already recorded, the corresponding template is replaced by the new one. Then, WARNING : test HasTemplate to avoid surprises
        """
    def StringLabel(self,ent : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a string with the label attached to a given entity. Warning : While this string may be edited on the spot, if it is a read field, the returned value must be copied before.
        """
    @staticmethod
    def Template_s(name : str) -> Interface_InterfaceModel: 
        """
        Returns the template model attached to a name, or a Null Handle
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self,ent : OCP.Standard.Standard_Transient,num : int=1) -> OCP.Standard.Standard_Type: 
        """
        Returns a type, given its rank : defined by the Protocol (by default, the first one)
        """
    def TypeName(self,ent : OCP.Standard.Standard_Transient,complete : bool=True) -> str: 
        """
        Returns the type name of an entity, from the list of types (one or more ...) <complete> True (D) gives the complete type, else packages are removed WARNING : buffered, to be immediately copied or printed
        """
    def Value(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns an Entity identified by its number in the Model Each sub-class of InterfaceModel can define its own method Entity to return its specific class of Entity (e.g. for VDA, VDAModel returns a VDAEntity), working by calling Value Remark : For a Reported Entity, (Erroneous, Corrected, Unknown), this method returns this Reported Entity. See ReportEntity for other questions.
        """
    def VerifyCheck(self,ach : Interface_Check) -> Any: 
        """
        Minimum Semantic Global Check on data in model (header) Can only check basic Data. See also GlobalCheck from Protocol for a check which takes the Graph into account Default does nothing, can be redefined
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
    @property
    def DispatchStatus(self) -> bool:
        """
        Returns the Dispatch Status, either for get or set A Model which is produced from Dispatch may share entities with the original (according to the Protocol), hence these non-copied entities should not be deleted

        :type: bool
        """
    @DispatchStatus.setter
    def DispatchStatus(self, arg1: bool) -> None:
        """
        Returns the Dispatch Status, either for get or set A Model which is produced from Dispatch may share entities with the original (according to the Protocol), hence these non-copied entities should not be deleted
        """
    pass
class Interface_LineBuffer():
    """
    Simple Management of a Line Buffer, to be used by Interface File Writers. While a String is suitable to do that, this class ensures an optimised Memory Management, because this is a hard point of File Writing.
    """
    @overload
    def Add(self,text : str) -> None: 
        """
        Adds a text as a CString. Its Length is evaluated from the text (by C function strlen)

        Adds a text as a CString. Its length is given as <lntext>

        Adds a text as a AsciiString from TCollection

        Adds a text made of only ONE Character
        """
    @overload
    def Add(self,text : str,lntext : int) -> None: ...
    @overload
    def Add(self,text : OCP.TCollection.TCollection_AsciiString) -> None: ...
    def CanGet(self,more : int) -> bool: 
        """
        Returns True if there is room enough to add <more> characters Else, it is required to Dump the Buffer before refilling it <more> is recorded to manage SetKeep status
        """
    def Clear(self) -> None: 
        """
        Clears completely the LineBuffer
        """
    def Content(self) -> str: 
        """
        Returns the Content of the LineBuffer
        """
    def FreezeInitial(self) -> None: 
        """
        Inhibits effect of SetInitial until the next Move (i.e. Keep) Then Prepare will not insert initial blanks, but further ones will. This allows to cancel initial blanks on an internal Split A call to SetInitial has no effect on this until Move
        """
    def Length(self) -> int: 
        """
        Returns the Length of the LineBuffer
        """
    @overload
    def Move(self,str : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Fills a AsciiString <str> with the Content of the Line Buffer, then Clears the LineBuffer

        Same as above, but <str> is known through a Handle
        """
    @overload
    def Move(self,str : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def Moved(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Same as above, but generates the HAsciiString
        """
    def SetInitial(self,initial : int) -> None: 
        """
        Sets an Initial reservation for Blank characters (this reservation is counted in the size of the current Line)
        """
    def SetKeep(self) -> None: 
        """
        Sets a Keep Status at current Length. It means that at next Move, the new line will begin by characters between Keep + 1 and current Length
        """
    def SetMax(self,max : int) -> None: 
        """
        Changes Maximum allowed size of Buffer. If <max> is Zero, Maximum size is set to the initial size.
        """
    def __init__(self,size : int=10) -> None: ...
    pass
class Interface_MSG():
    """
    This class gives a set of functions to manage and use a list of translated messages (messagery)
    """
    @staticmethod
    @overload
    def Blanks_s(count : int) -> str: 
        """
        Returns a blank string, of length between 0 and <max>, to fill the printing of a numeric value <val>, i.e. : If val < 10 , max-1 blanks If val between 10 and 99, max-2 blanks ... etc...

        Returns a blank string, to complete a given string <val> up to <max> characters : If strlen(val) is 0, max blanks If strlen(val) is 5, max-5 blanks etc...

        Returns a blank string of <count> blanks (mini 0, maxi 76)
        """
    @staticmethod
    @overload
    def Blanks_s(val : int,max : int) -> str: ...
    @staticmethod
    @overload
    def Blanks_s(val : str,max : int) -> str: ...
    @staticmethod
    def CDate_s(text1 : str,text2 : str) -> int: 
        """
        Returns a value about comparison of two dates 0 : equal. <0 text1 anterior. >0 text1 posterior
        """
    def Destroy(self) -> None: 
        """
        Optimised destructor (applies for additional forms of Create)
        """
    @staticmethod
    def Intervalled_s(val : float,order : int=3,upper : bool=False) -> float: 
        """
        Returns an "intervalled" value from a starting real <val> : i.e. a value which is rounded on an interval limit Interval limits are defined to be in a coarsely "geometric" progression (two successive intervals are inside a limit ratio)
        """
    @staticmethod
    def IsKey_s(mess : str) -> bool: 
        """
        Returns True if a given message is surely a key (according to the form adopted for keys) (before activating messages, answer is false)
        """
    @staticmethod
    def NDate_s(text : str,yy : int,mm : int,dd : int,hh : int,mn : int,ss : int) -> bool: 
        """
        Decodes a date to numeric integer values Returns True if OK, False if text does not fit with required format. Incomplete forms are allowed (for instance, for only YYYY-MM-DD, hour is zero)
        """
    @staticmethod
    def PrintTrace_s(S : io.BytesIO) -> None: 
        """
        Prints the recorded errors (without title; can be empty, this is the normally expected case)
        """
    @staticmethod
    def Print_s(S : io.BytesIO,val : str,max : int,just : int=-1) -> None: 
        """
        Prints a String on an Output Stream, as follows : Accompanied with blanks, to give up to <max> charis at all, justified according just : -1 (D) : left 0 : center 1 : right Maximum 76 characters
        """
    @staticmethod
    @overload
    def Read_s(file : str) -> int: 
        """
        Reads a list of messages from a stream, returns read count 0 means empty file, -1 means error

        Reads a list of messages from a file defined by its name
        """
    @staticmethod
    @overload
    def Read_s(S : io.BytesIO) -> int: ...
    @staticmethod
    def Record_s(key : str,item : str) -> None: 
        """
        Fills the dictionary with a couple (key-item) If a key is already recorded, it is possible to : - keep the last definition, and activate the trace system
        """
    @staticmethod
    def SetMode_s(running : bool,raising : bool) -> None: 
        """
        Sets the main modes for MSG : - if <running> is True, translation works normally - if <running> is False, translated item equate keys - if <raising> is True, errors (from Record or Translate) cause MSG to raise an exception - if <raising> is False, MSG runs without exception, then see also Trace Modes above
        """
    @staticmethod
    def SetTrace_s(toprint : bool,torecord : bool) -> None: 
        """
        Sets the trace system to work when activated, as follow : - if <toprint> is True, print immediately on standard output - if <torecord> is True, record it for further print
        """
    @staticmethod
    def TDate_s(text : str,yy : int,mm : int,dd : int,hh : int,mn : int,ss : int,format : str='') -> None: 
        """
        Codes a date as a text, from its numeric value (-> seconds) : YYYY-MM-DD:HH-MN-SS fixed format, completed by leading zeros Another format can be provided, as follows : C:%d ... C like format, preceded by C: S:... format to call system (not yet implemented)
        """
    @staticmethod
    def Translated_s(key : str) -> str: 
        """
        Returns the item recorded for a key. Returns the key itself if : - it is not recorded (then, the trace system is activated) - MSG has been required to be hung on
        """
    def Value(self) -> str: 
        """
        Returns the translated message, in a functional form with operator () was C++ : return const
        """
    @staticmethod
    def Write_s(S : io.BytesIO,rootkey : str='') -> int: 
        """
        Writes the list of messages recorded to be translated, to a stream. Writes all the list (Default) or only keys which begin by <rootkey>. Returns the count of written messages
        """
    @overload
    def __init__(self,key : str,r1 : float,intervals : int=-1) -> None: ...
    @overload
    def __init__(self,key : str,i1 : int) -> None: ...
    @overload
    def __init__(self,key : str) -> None: ...
    @overload
    def __init__(self,key : str,ival : int,str : str) -> None: ...
    @overload
    def __init__(self,key : str,i1 : int,i2 : int) -> None: ...
    @overload
    def __init__(self,key : str,str : str) -> None: ...
    pass
class Interface_MapAsciiStringHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(theAsciiString : OCP.TCollection.TCollection_AsciiString,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given ASCII string, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(K1 : OCP.TCollection.TCollection_AsciiString,K2 : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Interface_NodeOfGeneralLib(OCP.Standard.Standard_Transient):
    def AddNode(self,anode : Interface_GlobalNodeOfGeneralLib) -> None: 
        """
        Adds a couple (Module,Protocol), that is, stores it into itself if not yet done, else creates a Next Node to do it
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
    def Module(self) -> Interface_GeneralModule: 
        """
        Returns the Module designated by a precise Node
        """
    def Next(self) -> Interface_NodeOfGeneralLib: 
        """
        Returns the Next Node. If none was defined, returned value is a Null Handle
        """
    def Protocol(self) -> Interface_Protocol: 
        """
        Returns the Protocol designated by a precise Node
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
class Interface_NodeOfReaderLib(OCP.Standard.Standard_Transient):
    def AddNode(self,anode : Interface_GlobalNodeOfReaderLib) -> None: 
        """
        Adds a couple (Module,Protocol), that is, stores it into itself if not yet done, else creates a Next Node to do it
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
    def Module(self) -> Interface_ReaderModule: 
        """
        Returns the Module designated by a precise Node
        """
    def Next(self) -> Interface_NodeOfReaderLib: 
        """
        Returns the Next Node. If none was defined, returned value is a Null Handle
        """
    def Protocol(self) -> Interface_Protocol: 
        """
        Returns the Protocol designated by a precise Node
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
class Interface_ParamList(OCP.Standard.Standard_Transient):
    def ChangeValue(self,Index : int) -> Interface_FileParameter: 
        """
        return the value of the <Index>th element of the array.
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
    def Length(self) -> int: 
        """
        Returns the number of elements of <me>.

        Returns the number of elements of <me>.
        """
    def Lower(self) -> int: 
        """
        Returns the lower bound. Warning

        Returns the lower bound. Warning
        """
    def SetValue(self,Index : int,Value : Interface_FileParameter) -> None: 
        """
        Assigns the value <Value> to the <Index>-th item of this array.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Returns the upper bound. Warning

        Returns the upper bound. Warning
        """
    def Value(self,Index : int) -> Interface_FileParameter: 
        """
        Return the value of the <Index>th element of the array.
        """
    def __init__(self,theIncrement : int=256) -> None: ...
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
class Interface_ParamSet(OCP.Standard.Standard_Transient):
    """
    Defines an ordered set of FileParameters, in a way to be efficient as in memory requirement or in speedDefines an ordered set of FileParameters, in a way to be efficient as in memory requirement or in speedDefines an ordered set of FileParameters, in a way to be efficient as in memory requirement or in speed
    """
    @overload
    def Append(self,FP : Interface_FileParameter) -> int: 
        """
        Adds a parameter defined as its Value (CString and length) and Type. Optional EntityNumber (for FileReaderData) can be given Allows a better memory management than Appending a complete FileParameter If <lnval> < 0, <val> is assumed to be managed elsewhere : its address is stored as such. Else, <val> is copied in a locally (quickly) managed Page of Characters Returns new count of recorded Parameters

        Adds a parameter at the end of the ParamSet (transparent about reservation and "Next") Returns new count of recorded Parameters
        """
    @overload
    def Append(self,val : str,lnval : int,typ : Interface_ParamType,nument : int) -> int: ...
    def ChangeParam(self,num : int) -> Interface_FileParameter: 
        """
        Same as above, but in order to be modified on place
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Destroy(self) -> None: ...
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
    def NbParams(self) -> int: 
        """
        Returns the total count of parameters (including nexts)
        """
    def Param(self,num : int) -> Interface_FileParameter: 
        """
        Returns a parameter identified by its number
        """
    def Params(self,num : int,nb : int) -> Interface_ParamList: 
        """
        Builds and returns the sub-list corresponding to parameters, from "num" included, with count "nb" If <num> and <nb> are zero, returns the whole list
        """
    def SetParam(self,num : int,FP : Interface_FileParameter) -> None: 
        """
        Changes a parameter identified by its number
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,nres : int,nst : int=1) -> None: ...
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
class Interface_ParamType():
    """
    None

    Members:

      Interface_ParamMisc

      Interface_ParamInteger

      Interface_ParamReal

      Interface_ParamIdent

      Interface_ParamVoid

      Interface_ParamText

      Interface_ParamEnum

      Interface_ParamLogical

      Interface_ParamSub

      Interface_ParamHexa

      Interface_ParamBinary
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
    Interface_ParamBinary: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamBinary: 10>
    Interface_ParamEnum: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamEnum: 6>
    Interface_ParamHexa: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamHexa: 9>
    Interface_ParamIdent: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamIdent: 3>
    Interface_ParamInteger: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamInteger: 1>
    Interface_ParamLogical: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamLogical: 7>
    Interface_ParamMisc: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamMisc: 0>
    Interface_ParamReal: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamReal: 2>
    Interface_ParamSub: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamSub: 8>
    Interface_ParamText: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamText: 5>
    Interface_ParamVoid: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamVoid: 4>
    __entries: dict # value = {'Interface_ParamMisc': (<Interface_ParamType.Interface_ParamMisc: 0>, None), 'Interface_ParamInteger': (<Interface_ParamType.Interface_ParamInteger: 1>, None), 'Interface_ParamReal': (<Interface_ParamType.Interface_ParamReal: 2>, None), 'Interface_ParamIdent': (<Interface_ParamType.Interface_ParamIdent: 3>, None), 'Interface_ParamVoid': (<Interface_ParamType.Interface_ParamVoid: 4>, None), 'Interface_ParamText': (<Interface_ParamType.Interface_ParamText: 5>, None), 'Interface_ParamEnum': (<Interface_ParamType.Interface_ParamEnum: 6>, None), 'Interface_ParamLogical': (<Interface_ParamType.Interface_ParamLogical: 7>, None), 'Interface_ParamSub': (<Interface_ParamType.Interface_ParamSub: 8>, None), 'Interface_ParamHexa': (<Interface_ParamType.Interface_ParamHexa: 9>, None), 'Interface_ParamBinary': (<Interface_ParamType.Interface_ParamBinary: 10>, None)}
    __members__: dict # value = {'Interface_ParamMisc': <Interface_ParamType.Interface_ParamMisc: 0>, 'Interface_ParamInteger': <Interface_ParamType.Interface_ParamInteger: 1>, 'Interface_ParamReal': <Interface_ParamType.Interface_ParamReal: 2>, 'Interface_ParamIdent': <Interface_ParamType.Interface_ParamIdent: 3>, 'Interface_ParamVoid': <Interface_ParamType.Interface_ParamVoid: 4>, 'Interface_ParamText': <Interface_ParamType.Interface_ParamText: 5>, 'Interface_ParamEnum': <Interface_ParamType.Interface_ParamEnum: 6>, 'Interface_ParamLogical': <Interface_ParamType.Interface_ParamLogical: 7>, 'Interface_ParamSub': <Interface_ParamType.Interface_ParamSub: 8>, 'Interface_ParamHexa': <Interface_ParamType.Interface_ParamHexa: 9>, 'Interface_ParamBinary': <Interface_ParamType.Interface_ParamBinary: 10>}
    pass
class Interface_Protocol(OCP.Standard.Standard_Transient):
    """
    General description of Interface Protocols. A Protocol defines a set of Entity types. This class provides also the notion of Active Protocol, as a working context, defined once then exploited by various Tools and Libraries.General description of Interface Protocols. A Protocol defines a set of Entity types. This class provides also the notion of Active Protocol, as a working context, defined once then exploited by various Tools and Libraries.General description of Interface Protocols. A Protocol defines a set of Entity types. This class provides also the notion of Active Protocol, as a working context, defined once then exploited by various Tools and Libraries.
    """
    @staticmethod
    def Active_s() -> Interface_Protocol: 
        """
        Returns the Active Protocol, if defined (else, returns a Null Handle, which means "no defined active protocol")
        """
    def CaseNumber(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns a unique positive CaseNumber for each Recognized Object. By default, recognition is based on Type(1) By default, calls the following one which is deferred.
        """
    @staticmethod
    def ClearActive_s() -> None: 
        """
        Erases the Active Protocol (hence it becomes undefined)
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
    def GlobalCheck(self,G : Interface_Graph,ach : Interface_Check) -> bool: 
        """
        Evaluates a Global Check for a model (with its Graph) Returns True when done, False if data in model do not apply
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDynamicType(self,obj : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if type of <obj> is that defined from CDL This is the default but it may change according implementation
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
    def IsSuitableModel(self,model : Interface_InterfaceModel) -> bool: 
        """
        Returns True if <model> is a Model of the considered Norm
        """
    def IsUnknownEntity(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e. same Type as them created by method UnknownEntity (for an Entity out of the Norm, answer can be unpredicable)
        """
    def NbResources(self) -> int: 
        """
        Returns count of Protocol used as Resources (level one)
        """
    def NbTypes(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the count of DISTINCT types under which an entity may be processed. Each one is candidate to be recognized by TypeNumber, <obj> is then processed according it By default, returns 1 (the DynamicType)
        """
    def NewModel(self) -> Interface_InterfaceModel: 
        """
        Creates an empty Model of the considered Norm
        """
    def Resource(self,num : int) -> Interface_Protocol: 
        """
        Returns a Resource, given its rank (between 1 and NbResources)
        """
    @staticmethod
    def SetActive_s(aprotocol : Interface_Protocol) -> None: 
        """
        Sets a given Protocol to be the Active one (for the users of Active, see just above). Applies to every sub-type of Protocol
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self,obj : OCP.Standard.Standard_Transient,nt : int=1) -> OCP.Standard.Standard_Type: 
        """
        Returns a type under which <obj> can be recognized and processed, according its rank in its definition list (see NbTypes). By default, returns DynamicType
        """
    def TypeNumber(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        Returns a unique positive CaseNumber for each Recognized Type, Returns Zero for "<type> not recognized"
        """
    def UnknownEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Creates a new Unknown Entity for the considered Norm
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
class Interface_ReaderLib():
    """
    None
    """
    def AddProtocol(self,aprotocol : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds a couple (Module-Protocol) to the Library, given the class of a Protocol. Takes Resources into account. (if <aprotocol> is not of type TheProtocol, it is not added)
        """
    def Clear(self) -> None: 
        """
        Clears the list of Modules of a library (can be used to redefine the order of Modules before action : Clear then refill the Library by calls to AddProtocol)
        """
    def Module(self) -> Interface_ReaderModule: 
        """
        Returns the current Module in the Iteration
        """
    def More(self) -> bool: 
        """
        Returns True if there are more Modules to iterate on
        """
    def Next(self) -> None: 
        """
        Iterates by getting the next Module in the list If there is none, the exception will be raised by Value
        """
    def Protocol(self) -> Interface_Protocol: 
        """
        Returns the current Protocol in the Iteration
        """
    def Select(self,obj : OCP.Standard.Standard_Transient,module : Interface_ReaderModule,CN : int) -> bool: 
        """
        Selects a Module from the Library, given an Object. Returns True if Select has succeeded, False else. Also Returns (as arguments) the selected Module and the Case Number determined by the associated Protocol. If Select has failed, <module> is Null Handle and CN is zero. (Select can work on any criterium, such as Object DynamicType)
        """
    def SetComplete(self) -> None: 
        """
        Sets a library to be defined with the complete Global list (all the couples Protocol/Modules recorded in it)
        """
    @staticmethod
    def SetGlobal_s(amodule : Interface_ReaderModule,aprotocol : Interface_Protocol) -> None: 
        """
        Adds a couple (Module-Protocol) into the global definition set for this class of Library.
        """
    def Start(self) -> None: 
        """
        Starts Iteration on the Modules (sets it on the first one)
        """
    @overload
    def __init__(self,aprotocol : Interface_Protocol) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Interface_ReaderModule(OCP.Standard.Standard_Transient):
    """
    Defines unitary operations required to read an Entity from a File (see FileReaderData, FileReaderTool), under control of a FileReaderTool. The initial creation is performed by a GeneralModule (set in GeneralLib). Then, which remains is Loading data from the FileReaderData to the EntityDefines unitary operations required to read an Entity from a File (see FileReaderData, FileReaderTool), under control of a FileReaderTool. The initial creation is performed by a GeneralModule (set in GeneralLib). Then, which remains is Loading data from the FileReaderData to the EntityDefines unitary operations required to read an Entity from a File (see FileReaderData, FileReaderTool), under control of a FileReaderTool. The initial creation is performed by a GeneralModule (set in GeneralLib). Then, which remains is Loading data from the FileReaderData to the Entity
    """
    def CaseNum(self,data : Interface_FileReaderData,num : int) -> int: 
        """
        Translates the type of record <num> in <data> to a positive Case Number. If Recognition fails, must return 0
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
    def NewRead(self,casenum : int,data : Interface_FileReaderData,num : int,ach : Interface_Check,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific operator (create+read) defaulted to do nothing. It can be redefined when it is not possible to work in two steps (NewVoid then Read). This occurs when no default constructor is defined : hence the result <ent> must be created with an effective definition from the reader. Remark : if NewRead is defined, Copy has nothing to do.
        """
    def Read(self,casenum : int,data : Interface_FileReaderData,num : int,ach : Interface_Check,ent : OCP.Standard.Standard_Transient) -> Any: 
        """
        Performs the effective loading from <data>, record <num>, to the Entity <ent> formerly created In case of Error or Warning, fills <ach> with messages Remark that the Case Number comes from translating a record
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
class Interface_ReportEntity(OCP.Standard.Standard_Transient):
    """
    A ReportEntity is produced to aknowledge and memorize the binding between a Check and an Entity. The Check can bring Fails (+ Warnings if any), or only Warnings. If it is empty, the Report Entity is for an Unknown Entity.A ReportEntity is produced to aknowledge and memorize the binding between a Check and an Entity. The Check can bring Fails (+ Warnings if any), or only Warnings. If it is empty, the Report Entity is for an Unknown Entity.A ReportEntity is produced to aknowledge and memorize the binding between a Check and an Entity. The Check can bring Fails (+ Warnings if any), or only Warnings. If it is empty, the Report Entity is for an Unknown Entity.
    """
    def CCheck(self) -> Interface_Check: 
        """
        Returns the stored Check in order to change it
        """
    def Check(self) -> Interface_Check: 
        """
        Returns the stored Check
        """
    def Concerned(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the stored Concerned Entity. It equates the Content in the case of an Unknown Entity
        """
    def Content(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the stored Content, or a Null Handle Remark that it must be an "Unknown Entity" suitable for the norm of the containing Model
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
    def HasContent(self) -> bool: 
        """
        Returns True if a Content is stored (it can equate Concerned)
        """
    def HasNewContent(self) -> bool: 
        """
        Returns True if a Content is stored AND differs from Concerned (i.e. redefines content) : used when Concerned could not be loaded
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsError(self) -> bool: 
        """
        Returns True for an Error Entity, i.e. if the Check brings at least one Fail message
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
    def IsUnknown(self) -> bool: 
        """
        Returns True for an Unknown Entity, i,e. if the Check is empty and Concerned equates Content
        """
    def SetContent(self,content : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets a Content : it brings non interpreted data which belong to the Concerned Entity. It can be empty then loaded later. Remark that for an Unknown Entity, Content is set by Create.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,acheck : Interface_Check,concerned : OCP.Standard.Standard_Transient) -> None: ...
    @overload
    def __init__(self,unknown : OCP.Standard.Standard_Transient) -> None: ...
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
class Interface_STAT():
    """
    This class manages statistics to be queried asynchronously. Way of use : An operator describes a STAT form then fills it according to its progression. This produces a state of advancement of the process. This state can then be queried asynchronously : typically it is summarised as a percentage. There are also an identification of the current state, and information on processed volume.
    """
    def AddPhase(self,weight : float,name : str='') -> None: 
        """
        Adds a new phase to the description. The first one after Create replaces the default unique one
        """
    def AddStep(self,weight : float=1.0) -> None: 
        """
        Adds a new step for the last added phase, the default unique one if no AddPhase has already been added Warning : AddStep before the first AddPhase are cancelled
        """
    @staticmethod
    def End_s() -> None: 
        """
        Commands to declare the process ended (hence, advancement is forced to 100 %)
        """
    def Internals(self,tit : OCP.TCollection.TCollection_HAsciiString,phn : OCP.TColStd.TColStd_HSequenceOfAsciiString,phw : OCP.TColStd.TColStd_HSequenceOfReal,phdeb : OCP.TColStd.TColStd_HSequenceOfInteger,phfin : OCP.TColStd.TColStd_HSequenceOfInteger,stw : OCP.TColStd.TColStd_HSequenceOfReal) -> Tuple[float]: 
        """
        Returns fields in once, without copying them, used for copy when starting
        """
    @staticmethod
    def NextCycle_s(items : int) -> None: 
        """
        Commands to resume the preceding cycle and start a new one, with a count of items Ignored if count of cycles is already passed Then, first step is started (or default one) NextItem can be called for the first step, or NextStep to pass to the next one
        """
    @staticmethod
    def NextItem_s(nbitems : int=1) -> None: 
        """
        Commands to add an item in the current step of the current cycle of the current phase By default, one item per call, can be overpassed Ignored if count of items of this cycle is already passed
        """
    @staticmethod
    def NextPhase_s(items : int,cycles : int=1) -> None: 
        """
        Commands to resume the preceding phase and start a new one <items> and <cycles> as for Start, but for this new phase Ignored if count of phases is already passed If <cycles> is more than one, the first Cycle must then be started by NextCycle (NextStep/NextItem are ignored). If it is one, NextItem/NextStep can then be called
        """
    @staticmethod
    def NextStep_s() -> None: 
        """
        Commands to resume the preceding step of the cycle Ignored if count of steps is already passed NextItem can be called for this step, NextStep passes to next
        """
    @staticmethod
    def Percent_s(phase : bool=False) -> int: 
        """
        Returns the advancement as a percentage : <phase> True : inside the current phase <phase> False (D) : relative to the whole process
        """
    @staticmethod
    def SetPhase_s(items : int,cycles : int=1) -> None: 
        """
        Changes the parameters of the phase to start To be used before first counting (i.e. just after NextPhase) Can be used by an operator which has to reajust counts on run
        """
    def Start(self,items : int,cycles : int=1) -> None: 
        """
        Starts a STAT on its first phase (or its default one) <items> gives the total count of items, <cycles> the count of cycles If <cycles> is more than one, the first Cycle must then be started by NextCycle (NextStep/NextItem are ignored). If it is one, NextItem/NextStep can then be called
        """
    @staticmethod
    def StartCount_s(items : int,title : str='') -> None: 
        """
        Starts a default STAT, with no phase, no step, ready to just count items. <items> gives the total count of items Hence, NextItem is available to directly count
        """
    def Step(self,num : int) -> float: 
        """
        Returns weight of a Step, related to the cumul given for the phase. <num> is given by <n0step> + i, i between 1 and <nbsteps> (default gives n0step < 0 then weight is one)
        """
    @staticmethod
    def Where_s(phase : bool=True) -> str: 
        """
        Returns an identification of the STAT : <phase> True (D) : the name of the current phase <phase> False : the title of the current STAT
        """
    @overload
    def __init__(self,other : Interface_STAT) -> None: ...
    @overload
    def __init__(self,title : str='') -> None: ...
    pass
class Interface_HSequenceOfCheck(Interface_SequenceOfCheck, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Interface_Check) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : Interface_SequenceOfCheck) -> None: ...
    def Assign(self,theOther : Interface_SequenceOfCheck) -> Interface_SequenceOfCheck: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Interface_Check: 
        """
        First item access
        """
    def ChangeLast(self) -> Interface_Check: 
        """
        Last item access
        """
    def ChangeSequence(self) -> Interface_SequenceOfCheck: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> Interface_Check: 
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
    def First(self) -> Interface_Check: 
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
    def InsertAfter(self,theIndex : int,theSeq : Interface_SequenceOfCheck) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Interface_Check) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Interface_Check) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Interface_SequenceOfCheck) -> None: ...
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
    def Last(self) -> Interface_Check: 
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
    def Prepend(self,theItem : Interface_Check) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Interface_SequenceOfCheck) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def Sequence(self) -> Interface_SequenceOfCheck: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : Interface_Check) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Interface_SequenceOfCheck) -> None: 
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
    def Value(self,theIndex : int) -> Interface_Check: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Interface_SequenceOfCheck) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class Interface_ShareFlags():
    """
    This class only says for each Entity of a Model, if it is Shared or not by one or more other(s) of this Model It uses the General Service "Shared".
    """
    def IsShared(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> is Shared by one or more other Entity(ies) of the Model
        """
    def Model(self) -> Interface_InterfaceModel: 
        """
        Returns the Model used for the evaluation
        """
    def NbRoots(self) -> int: 
        """
        Returns the count of root entities
        """
    def Root(self,num : int=1) -> OCP.Standard.Standard_Transient: 
        """
        Returns a root entity according its rank in the list of roots By default, it returns the first one
        """
    def RootEntities(self) -> Interface_EntityIterator: 
        """
        Returns the Entities which are not Shared (see their flags)
        """
    @overload
    def __init__(self,amodel : Interface_InterfaceModel) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,lib : Interface_GeneralLib) -> None: ...
    @overload
    def __init__(self,agraph : Interface_Graph) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,protocol : Interface_Protocol) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,gtool : Interface_GTool) -> None: ...
    pass
class Interface_ShareTool():
    """
    Builds the Graph of Dependencies, from the General Service "Shared" -> builds for each Entity of a Model, the Shared and Sharing Lists, and gives access to them. Allows to complete with Implied References (which are not regarded as Shared Entities, but are nevertheless Referenced), this can be useful for Reference Checking
    """
    def All(self,ent : OCP.Standard.Standard_Transient,rootlast : bool=True) -> Interface_EntityIterator: 
        """
        Returns the complete list of entities shared by <ent> at any level, including <ent> itself If <ent> is the Model, considers the concatenation of AllShared for each root If <rootlast> is True (D), the list starts with lower level entities and ends by the root. Else, the root is first and the lower level entities are at end
        """
    def Graph(self) -> Interface_Graph: 
        """
        Returns the data used by the ShareTool to work Can then be used directly (read only)
        """
    def IsShared(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> is Shared by other Entities in the Model
        """
    def Model(self) -> Interface_InterfaceModel: 
        """
        Returns the Model used for Creation (directly or for Graph)
        """
    def NbTypedSharings(self,ent : OCP.Standard.Standard_Transient,atype : OCP.Standard.Standard_Type) -> int: 
        """
        Returns the count of Sharing Entities of an Entity, which are Kind of a given Type
        """
    def Print(self,iter : Interface_EntityIterator,S : io.BytesIO) -> None: 
        """
        Utility method which Prints the content of an iterator (by their Numbers)
        """
    def RootEntities(self) -> Interface_EntityIterator: 
        """
        Returns the Entities which are not Shared (their Sharing List is empty) in the Model
        """
    def Shareds(self,ent : OCP.Standard.Standard_Transient) -> Interface_EntityIterator: 
        """
        Returns the List of Entities Shared by a given Entity <ent>
        """
    def Sharings(self,ent : OCP.Standard.Standard_Transient) -> Interface_EntityIterator: 
        """
        Returns the List of Entities Sharing a given Entity <ent>
        """
    def TypedSharing(self,ent : OCP.Standard.Standard_Transient,atype : OCP.Standard.Standard_Type) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Sharing Entity of an Entity, which is Kind of a given Type. Allows to access a Sharing Entity of a given type when there is one and only one (current case)
        """
    @overload
    def __init__(self,amodel : Interface_InterfaceModel) -> None: ...
    @overload
    def __init__(self,ahgraph : Interface_HGraph) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,lib : Interface_GeneralLib) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,protocol : Interface_Protocol) -> None: ...
    @overload
    def __init__(self,amodel : Interface_InterfaceModel,gtool : Interface_GTool) -> None: ...
    @overload
    def __init__(self,agraph : Interface_Graph) -> None: ...
    pass
class Interface_SignLabel():
    """
    Signature to give the Label from the ModelSignature to give the Label from the ModelSignature to give the Label from the Model
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Name(self) -> str: 
        """
        Returns "Entity Label"
        """
    def Text(self,ent : OCP.Standard.Standard_Transient,context : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Considers context as an InterfaceModel and returns the Label computed by it
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
class Interface_SignType():
    """
    Provides the basic service to get a type name, according to a norm It can be used for other classes (general signatures ...)Provides the basic service to get a type name, according to a norm It can be used for other classes (general signatures ...)Provides the basic service to get a type name, according to a norm It can be used for other classes (general signatures ...)
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
    def Text(self,ent : OCP.Standard.Standard_Transient,context : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an identification of the Signature (a word), given at initialization time Specialised to consider context as an InterfaceModel
        """
    def Value(self,ent : OCP.Standard.Standard_Transient,model : Interface_InterfaceModel) -> str: 
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
class Interface_TypedValue():
    """
    Now strictly equivalent to TypedValue from MoniTool, except for ParamType which remains for compatibility reasonsNow strictly equivalent to TypedValue from MoniTool, except for ParamType which remains for compatibility reasonsNow strictly equivalent to TypedValue from MoniTool, except for ParamType which remains for compatibility reasons
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def ParamTypeToValueType_s(typ : Interface_ParamType) -> MoniTool_ValueType: 
        """
        Correspondence ParamType from Interface to ValueType from MoniTool
        """
    def Type(self) -> Interface_ParamType: 
        """
        Returns the type I.E. calls ValueType then makes correspondence between ParamType from Interface (which remains for compatibility reasons) and ValueType from MoniTool
        """
    @staticmethod
    def ValueTypeToParamType_s(typ : MoniTool_ValueType) -> Interface_ParamType: 
        """
        Correspondence ParamType from Interface to ValueType from MoniTool
        """
    def __init__(self,name : str,type : Interface_ParamType=Interface_ParamType.Interface_ParamText,init : str='') -> None: ...
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
class Interface_Static(Interface_TypedValue):
    """
    This class gives a way to manage meaningful static variables, used as "global" parameters in various procedures.This class gives a way to manage meaningful static variables, used as "global" parameters in various procedures.This class gives a way to manage meaningful static variables, used as "global" parameters in various procedures.
    """
    @staticmethod
    def CDef_s(name : str,part : str) -> str: 
        """
        Returns a part of the definition of a Static, as a CString The part is designated by its name, as a CString If the required value is not a string, it is converted to a CString then returned If <name> is not present, or <part> not defined for <name>, this function returns an empty string
        """
    @staticmethod
    def CVal_s(name : str) -> str: 
        """
        Returns the value of the parameter identified by the string name. If the specified parameter does not exist, an empty string is returned. Example Interface_Static::CVal("write.step.schema"); which could return: "AP214"
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Family(self) -> str: 
        """
        Returns the family. It can be : a resource name for applis, an internal name between : $e (environment variables), $l (other, purely local)
        """
    @staticmethod
    def FillMap_s(theMap : OCP.Resource.Resource_DataMapOfAsciiStringAsciiString) -> None: 
        """
        Fills given string-to-string map with all static data
        """
    @staticmethod
    def IDef_s(name : str,part : str) -> int: 
        """
        Returns a part of the definition of a Static, as an Integer The part is designated by its name, as a CString If the required value is not a string, returns zero For a Boolean, 0 for false, 1 for true If <name> is not present, or <part> not defined for <name>, this function returns zero
        """
    @staticmethod
    def IVal_s(name : str) -> int: 
        """
        Returns the integer value of the translation parameter identified by the string name. Returns the value 0 if the parameter does not exist. Example Interface_Static::IVal("write.step.schema"); which could return: 3
        """
    @staticmethod
    @overload
    def Init_s(family : str,name : str,type : str,init : str='') -> bool: 
        """
        Declares a new Static (by calling its constructor) If this name is already taken, does nothing and returns False Else, creates it and returns True For additional definitions, get the Static then edit it

        As Init with ParamType, but type is given as a character This allows a simpler call Types : 'i' Integer, 'r' Real, 't' Text, 'e' Enum, 'o' Object '=' for same definition as, <init> gives the initial Static Returns False if <type> does not match this list
        """
    @staticmethod
    @overload
    def Init_s(family : str,name : str,type : Interface_ParamType,init : str='') -> bool: ...
    @staticmethod
    def IsPresent_s(name : str) -> bool: 
        """
        Returns True if a Static named <name> is present, False else
        """
    @staticmethod
    def IsSet_s(name : str,proper : bool=True) -> bool: 
        """
        Returns True if <name> is present AND set <proper> True (D) : considers this item only <proper> False : if not set and attached to a wild-card, considers this wild-card
        """
    @staticmethod
    def IsUpdated_s(name : str) -> bool: 
        """
        Returns the status "uptodate" from a Static Returns False if <name> is not present
        """
    @staticmethod
    def Items_s(mode : int=0,criter : str='') -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns a list of names of statics : <mode> = 0 (D) : criter is for family <mode> = 1 : criter is regexp on names, takes final items (ignore wild cards) <mode> = 2 : idem but take only wilded, not final items <mode> = 3 : idem, take all items matching criter idem + 100 : takes only non-updated items idem + 200 : takes only updated items criter empty (D) : returns all names else returns names which match the given criter Remark : families beginning by '$' are not listed by criter "" they are listed only by criter "$"
        """
    @staticmethod
    def ParamTypeToValueType_s(typ : Interface_ParamType) -> MoniTool_ValueType: 
        """
        Correspondence ParamType from Interface to ValueType from MoniTool
        """
    def PrintStatic(self,S : io.BytesIO) -> None: 
        """
        Writes the properties of a parameter in the diagnostic file. These include: - Name - Family, - Wildcard (if it has one) - Current status (empty string if it was updated or if it is the original one) - Value
        """
    @staticmethod
    def RVal_s(name : str) -> float: 
        """
        Returns the value of a static translation parameter identified by the string name. Returns the value 0.0 if the parameter does not exist.
        """
    @staticmethod
    def SetCVal_s(name : str,val : str) -> bool: 
        """
        Modifies the value of the parameter identified by name. The modification is specified by the string val. false is returned if the parameter does not exist. Example Interface_Static::SetCVal ("write.step.schema","AP203") This syntax specifies a switch from the default STEP 214 mode to STEP 203 mode.
        """
    @staticmethod
    def SetIVal_s(name : str,val : int) -> bool: 
        """
        Modifies the value of the parameter identified by name. The modification is specified by the integer value val. false is returned if the parameter does not exist. Example Interface_Static::SetIVal ("write.step.schema", 3) This syntax specifies a switch from the default STEP 214 mode to STEP 203 mode.S
        """
    @staticmethod
    def SetRVal_s(name : str,val : float) -> bool: 
        """
        Modifies the value of a translation parameter. false is returned if the parameter does not exist. The modification is specified by the real number value val.
        """
    def SetUptodate(self) -> None: 
        """
        Records a Static has "uptodate", i.e. its value has been taken into account by a reinitialisation procedure This flag is reset at each successful SetValue
        """
    def SetWild(self,wildcard : Interface_Static) -> None: 
        """
        Sets a "wild-card" static : its value will be considered if <me> is not properly set. (reset by set a null one)
        """
    @staticmethod
    def Standards_s() -> None: 
        """
        Initializes all standard static parameters, which can be used by every function. statics specific of a norm or a function must be defined around it
        """
    @staticmethod
    def Static_s(name : str) -> Interface_Static: 
        """
        Returns a Static from its name. Null Handle if not present
        """
    def Type(self) -> Interface_ParamType: 
        """
        Returns the type I.E. calls ValueType then makes correspondence between ParamType from Interface (which remains for compatibility reasons) and ValueType from MoniTool
        """
    @staticmethod
    def Update_s(name : str) -> bool: 
        """
        Sets a Static to be "uptodate" Returns False if <name> is not present This status can be used by a reinitialisation procedure to rerun if a value has been changed
        """
    def UpdatedStatus(self) -> bool: 
        """
        Returns the status "uptodate"
        """
    @staticmethod
    def ValueTypeToParamType_s(typ : MoniTool_ValueType) -> Interface_ParamType: 
        """
        Correspondence ParamType from Interface to ValueType from MoniTool
        """
    def Wild(self) -> Interface_Static: 
        """
        Returns the wildcard static, which can be (is most often) null
        """
    @overload
    def __init__(self,family : str,name : str,type : Interface_ParamType=Interface_ParamType.Interface_ParamText,init : str='') -> None: ...
    @overload
    def __init__(self,family : str,name : str,other : Interface_Static) -> None: ...
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
class Interface_UndefinedContent(OCP.Standard.Standard_Transient):
    """
    Defines resources for an "Undefined Entity" : such an Entity is used to describe an Entity which complies with the Norm, but of an Unknown Type : hence it is kept under a literal form (avoiding to loose data). UndefinedContent offers a way to store a list of Parameters, as literals or references to other EntitiesDefines resources for an "Undefined Entity" : such an Entity is used to describe an Entity which complies with the Norm, but of an Unknown Type : hence it is kept under a literal form (avoiding to loose data). UndefinedContent offers a way to store a list of Parameters, as literals or references to other EntitiesDefines resources for an "Undefined Entity" : such an Entity is used to describe an Entity which complies with the Norm, but of an Unknown Type : hence it is kept under a literal form (avoiding to loose data). UndefinedContent offers a way to store a list of Parameters, as literals or references to other Entities
    """
    def AddEntity(self,ptype : Interface_ParamType,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds a Parameter which references an Entity
        """
    def AddLiteral(self,ptype : Interface_ParamType,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Adds a literal Parameter to the list
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
    def EntityList(self) -> Interface_EntityList: 
        """
        Returns globally the list of param entities. Note that it can be used as shared entity list for the UndefinedEntity
        """
    def GetFromAnother(self,other : Interface_UndefinedContent,TC : Interface_CopyTool) -> None: 
        """
        Copies contents of undefined entities; deigned to be called by GetFromAnother method from Undefined entity of each Interface (the basic operation is the same regardless the norm)
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
    def IsParamEntity(self,num : int) -> bool: 
        """
        Returns True if a Parameter is recorded as an entity Error if num is not between 1 and NbParams
        """
    def NbLiterals(self) -> int: 
        """
        Gives count of Literal Parameters
        """
    def NbParams(self) -> int: 
        """
        Gives count of recorded parameters
        """
    def ParamData(self,num : int,ptype : Interface_ParamType,ent : OCP.Standard.Standard_Transient,val : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        Returns data of a Parameter : its type, and the entity if it designates en entity ("ent") or its literal value else ("str") Returned value (Boolean) : True if it is an Entity, False else
        """
    def ParamEntity(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns Entity corresponding to a Param, given its rank
        """
    def ParamType(self,num : int) -> Interface_ParamType: 
        """
        Returns the ParamType of a Param, given its rank Error if num is not between 1 and NbParams
        """
    def ParamValue(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns literal value of a Parameter, given its rank
        """
    def RemoveParam(self,num : int) -> None: 
        """
        Removes a Parameter given its rank
        """
    def Reservate(self,nb : int,nblit : int) -> None: 
        """
        Manages reservation for parameters (internal use) (nb : total count of parameters, nblit : count of literals)
        """
    @overload
    def SetEntity(self,num : int,ptype : Interface_ParamType,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets a new value for the Parameter <num>, to reference an Entity. To simply change the Entity, see the variant below

        Changes the Entity referenced by the Parameter <num> (with same ParamType)
        """
    @overload
    def SetEntity(self,num : int,ent : OCP.Standard.Standard_Transient) -> None: ...
    def SetLiteral(self,num : int,ptype : Interface_ParamType,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets a new value for the Parameter <num>, to a literal value (if it referenced formerly an Entity, this Entity is removed)
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
class Interface_VectorOfFileParameter(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : Interface_FileParameter) -> Interface_FileParameter: 
        """
        Append
        """
    def Appended(self) -> Interface_FileParameter: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : Interface_VectorOfFileParameter,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> Interface_FileParameter: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Interface_FileParameter: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Interface_FileParameter: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> Interface_FileParameter: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Interface_FileParameter: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : Interface_FileParameter) -> Interface_FileParameter: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Interface_FileParameter: 
        """
        None
        """
    @overload
    def __init__(self,theOther : Interface_VectorOfFileParameter) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
Interface_CheckAny: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckAny: 3>
Interface_CheckFail: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckFail: 2>
Interface_CheckMessage: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckMessage: 4>
Interface_CheckNoFail: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckNoFail: 5>
Interface_CheckOK: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckOK: 0>
Interface_CheckWarning: OCP.Interface.Interface_CheckStatus # value = <Interface_CheckStatus.Interface_CheckWarning: 1>
Interface_DataFail: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_DataFail: 4>
Interface_DataWarning: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_DataWarning: 3>
Interface_LoadFail: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_LoadFail: 2>
Interface_LoadWarning: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_LoadWarning: 1>
Interface_ParamBinary: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamBinary: 10>
Interface_ParamEnum: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamEnum: 6>
Interface_ParamHexa: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamHexa: 9>
Interface_ParamIdent: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamIdent: 3>
Interface_ParamInteger: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamInteger: 1>
Interface_ParamLogical: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamLogical: 7>
Interface_ParamMisc: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamMisc: 0>
Interface_ParamReal: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamReal: 2>
Interface_ParamSub: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamSub: 8>
Interface_ParamText: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamText: 5>
Interface_ParamVoid: OCP.Interface.Interface_ParamType # value = <Interface_ParamType.Interface_ParamVoid: 4>
Interface_StateOK: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_StateOK: 0>
Interface_StateUnknown: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_StateUnknown: 6>
Interface_StateUnloaded: OCP.Interface.Interface_DataState # value = <Interface_DataState.Interface_StateUnloaded: 5>
