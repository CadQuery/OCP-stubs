import OCP.StepData
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.TCollection
import io
import OCP.Message
import OCP.Interface
import OCP.Resource
import OCP.Standard
__all__  = [
"StepData",
"StepData_Array1OfField",
"StepData_GeneralModule",
"StepData_Described",
"StepData_EDescr",
"StepData_ECDescr",
"StepData_ESDescr",
"StepData_Field",
"StepData_FieldList",
"StepData_FieldList1",
"StepData_FieldListD",
"StepData_FieldListN",
"StepData_Protocol",
"StepData_FileRecognizer",
"StepData_FreeFormEntity",
"StepData_DefaultGeneral",
"StepData_GlobalNodeOfWriterLib",
"StepData_HArray1OfField",
"StepData_Logical",
"StepData_NodeOfWriterLib",
"StepData_PDescr",
"StepData_Plex",
"StepData_FileProtocol",
"StepData_ReadWriteModule",
"StepData_SelectMember",
"StepData_SelectInt",
"StepData_SelectNamed",
"StepData_SelectArrReal",
"StepData_SelectReal",
"StepData_SelectType",
"StepData_Simple",
"StepData_StepDumper",
"StepData_StepModel",
"StepData_StepReaderData",
"StepData_StepReaderTool",
"StepData_StepWriter",
"StepData_UndefinedEntity",
"StepData_WriterLib",
"StepData_LFalse",
"StepData_LTrue",
"StepData_LUnknown"
]
class StepData():
    """
    Gives basic data definition for Step Interface. Any class of a data model described in EXPRESS Language is candidate to be managed by a Step Interface
    """
    @staticmethod
    def AddHeaderProtocol_s(headerproto : StepData_Protocol) -> None: 
        """
        Adds a new Header Protocol to the Header Definition
        """
    @staticmethod
    def HeaderProtocol_s() -> StepData_Protocol: 
        """
        Returns the recorded HeaderProtocol, which can be : - a Null Handle if no Header Protocol was yet defined - a simple Protocol if only one was defined - a FileProtocol if more than one Protocol was yet defined
        """
    @staticmethod
    def Init_s() -> None: 
        """
        Prepares General Data required to work with this package, which are the Protocol and Modules to be loaded into Libraries
        """
    @staticmethod
    def Protocol_s() -> StepData_Protocol: 
        """
        Returns a Protocol from StepData (avoids to create it)
        """
    def __init__(self) -> None: ...
    pass
class StepData_Array1OfField():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepData_Array1OfField) -> StepData_Array1OfField: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepData_Field: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepData_Field: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepData_Field: 
        """
        Variable value access
        """
    def First(self) -> StepData_Field: 
        """
        Returns first element
        """
    def Init(self,theValue : StepData_Field) -> None: 
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
    def Last(self) -> StepData_Field: 
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
    def Move(self,theOther : StepData_Array1OfField) -> StepData_Array1OfField: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepData_Field) -> None: 
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
    def Value(self,theIndex : int) -> StepData_Field: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepData_Field,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepData_Array1OfField) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepData_GeneralModule(OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    Specific features for General Services adapted to STEPSpecific features for General Services adapted to STEPSpecific features for General Services adapted to STEP
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" Remark that it should be in phase with the implementation of NewVoid+CopyCase/NewCopyCase Default returns always False, can be redefined
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> int: 
        """
        Returns a category number which characterizes an entity Category Numbers are managed by the class Category <shares> can be used to evaluate this number in the context Default returns 0 which means "unspecified"
        """
    def CheckCase(self,casenum : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Specific Checking of an Entity <ent>
        """
    def CopyCase(self,casenum : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Copy ("Deep") from <entfrom> to <entto> (same type) by using a TransferControl which provides its working Map. Use method Transferred from TransferControl to work Specific Copying of Implied References A Default is provided which does nothing (must current case !) Already copied references (by CopyFrom) must remain unchanged Use method Search from TransferControl to work
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Dispatches an entity Returns True if it works by copy, False if it just duplicates the starting Handle
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FillShared(self,model : OCP.Interface.Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific filling of the list of Entities shared by an Entity <ent>, according a Case Number <CN> (formerly computed by CaseNum), considered in the context of a Model <model> Default calls FillSharedCase (i.e., ignores the model) Can be redefined to use the model for working
        """
    def FillSharedCase(self,casenum : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific filling of the list of Entities shared by an Entity <ent>. Can use the internal utility method Share, below
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
    def ListImplied(self,model : OCP.Interface.Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> considered in the context of a Model <model> : i.e. the Entities which are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillShared + ListImplied give the complete list of References Default calls ListImpliedCase (i.e. ignores the model) Can be redefined to use the model for working
        """
    def ListImpliedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> (see above) are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillSharedCase + ListImpliedCase give the complete list of Referenced Entities The provided default method does nothing (Implied References are specific of a little amount of Entity Classes).
        """
    def Name(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Determines if an entity brings a Name (or widerly, if a Name can be attached to it, through the ShareTool By default, returns a Null Handle (no name can be produced) Can be redefined
        """
    def NewCopiedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Specific operator (create+copy) defaulted to do nothing. It can be redefined : When it is not possible to work in two steps (NewVoid then CopyCase). This can occur when there is no default constructor : hence the result <entto> must be created with an effective definition. Remark : if NewCopiedCase is defined, CopyCase has nothing to do Returns True if it has produced something, false else
        """
    def NewVoid(self,CN : int,entto : OCP.Standard.Standard_Transient) -> bool: 
        """
        Creates a new void entity <entto> according to a Case Number This entity remains to be filled, by reading from a file or by copying from another entity of same type (see CopyCase)
        """
    def RenewImpliedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Copying of Implied References A Default is provided which does nothing (must current case !) Already copied references (by CopyFrom) must remain unchanged Use method Search from CopyTool to work
        """
    def Share(self,iter : OCP.Interface.Interface_EntityIterator,shared : OCP.Standard.Standard_Transient) -> None: 
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
class StepData_Described(OCP.Standard.Standard_Transient):
    """
    General frame to describe entities with Description (Simple or Complex)General frame to describe entities with Description (Simple or Complex)General frame to describe entities with Description (Simple or Complex)
    """
    def As(self,steptype : str) -> StepData_Simple: 
        """
        Returns a Simple Entity which matches with a Type in <me> : For a Simple Entity : me if it matches, else a null handle For a Complex Entity : the member which matches, else null
        """
    def CField(self,name : str) -> StepData_Field: 
        """
        Returns a Field from its name; read or write
        """
    def Check(self,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Fills a Check by using its Description
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> StepData_EDescr: 
        """
        Returns the Description used to define this entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Field(self,name : str) -> StepData_Field: 
        """
        Returns a Field from its name; read-only
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasField(self,name : str) -> bool: 
        """
        Tells if a Field brings a given name
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsComplex(self) -> bool: 
        """
        Tells if a described entity is complex
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
    def Matches(self,steptype : str) -> bool: 
        """
        Tells if a step type is matched by <me> For a Simple Entity : own type or super type For a Complex Entity : one of the members
        """
    def Shared(self,list : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills an EntityIterator with entities shared by <me>
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
class StepData_EDescr(OCP.Standard.Standard_Transient):
    """
    This class is intended to describe the authorized form for an entity, either Simple or PlexThis class is intended to describe the authorized form for an entity, either Simple or PlexThis class is intended to describe the authorized form for an entity, either Simple or Plex
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
    def IsComplex(self) -> bool: 
        """
        Tells if a EDescr is complex (ECDescr) or simple (ESDescr)
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
    def Matches(self,steptype : str) -> bool: 
        """
        Tells if a ESDescr matches a step type : exact or super type
        """
    def NewEntity(self) -> StepData_Described: 
        """
        Creates a described entity (i.e. a simple one)
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
class StepData_ECDescr(StepData_EDescr, OCP.Standard.Standard_Transient):
    """
    Describes a Complex Entity (Plex) as a list of Simple onesDescribes a Complex Entity (Plex) as a list of Simple onesDescribes a Complex Entity (Plex) as a list of Simple ones
    """
    def Add(self,member : StepData_ESDescr) -> None: 
        """
        Adds a member Warning : members are added in alphabetic order
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
    def IsComplex(self) -> bool: 
        """
        Returns True
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
    def Matches(self,steptype : str) -> bool: 
        """
        Tells if a ESDescr matches a step type : exact or super type
        """
    def Member(self,num : int) -> StepData_ESDescr: 
        """
        Returns a Member from its rank
        """
    def NbMembers(self) -> int: 
        """
        Returns the count of members
        """
    def NewEntity(self) -> StepData_Described: 
        """
        Creates a described entity (i.e. a complex one, made of one simple entity per member)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeList(self) -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        Returns the ordered list of types
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
class StepData_ESDescr(StepData_EDescr, OCP.Standard.Standard_Transient):
    """
    This class is intended to describe the authorized form for a Simple (not Plex) Entity, as a list of fieldsThis class is intended to describe the authorized form for a Simple (not Plex) Entity, as a list of fieldsThis class is intended to describe the authorized form for a Simple (not Plex) Entity, as a list of fields
    """
    def Base(self) -> StepData_ESDescr: 
        """
        Returns the basic ESDescr, null if <me> is not derived
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
    def Field(self,num : int) -> StepData_PDescr: 
        """
        Returns the PDescr for the field <num> (or Null)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsComplex(self) -> bool: 
        """
        Returns False
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
    def IsSub(self,other : StepData_ESDescr) -> bool: 
        """
        Tells if <me> is sub-type of (or equal to) another one
        """
    def Matches(self,steptype : str) -> bool: 
        """
        Tells if a ESDescr matches a step type : exact or super type
        """
    def Name(self,num : int) -> str: 
        """
        Returns the name of a field from its rank. empty if outofrange
        """
    def NamedField(self,name : str) -> StepData_PDescr: 
        """
        Returns the PDescr for the field named <name> (or Null)
        """
    def NbFields(self) -> int: 
        """
        Returns the count of fields
        """
    def NewEntity(self) -> StepData_Described: 
        """
        Creates a described entity (i.e. a simple one)
        """
    def Rank(self,name : str) -> int: 
        """
        Returns the rank of a field from its name. 0 if unknown
        """
    def SetBase(self,base : StepData_ESDescr) -> None: 
        """
        Sets an ESDescr as based on another one Hence, if there are inherited fields, the derived ESDescr cumulates all them, while the base just records its own ones
        """
    def SetField(self,num : int,name : str,descr : StepData_PDescr) -> None: 
        """
        Sets a PDescr to describe a field A Field is designated by its rank and name
        """
    def SetNbFields(self,nb : int) -> None: 
        """
        Sets a new count of fields Each one is described by a PDescr
        """
    def SetSuper(self,super : StepData_ESDescr) -> None: 
        """
        Sets an ESDescr as "super-type". Applies an a base (non derived) ESDescr
        """
    def StepType(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the type name as an AsciiString
        """
    def Super(self) -> StepData_ESDescr: 
        """
        Returns the super-type ESDescr, null if <me> is root
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeName(self) -> str: 
        """
        Returns the type name given at creation time
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
class StepData_Field():
    """
    Defines a generally defined Field for STEP data : can be used either in any kind of entity to implement it or in free format entities in a "late-binding" mode A field can have : no value (or derived), a single value of any kind, a list of value : single or double list
    """
    def Arity(self) -> int: 
        """
        None
        """
    def Boolean(self,n1 : int=1,n2 : int=1) -> bool: 
        """
        None
        """
    def Clear(self,kind : int=0) -> None: 
        """
        Clears the field, to set it as "no value defined" Just before SetList, predeclares it as "any" A Kind can be directly set here to declare a type
        """
    def ClearItem(self,num : int) -> None: 
        """
        Declares an item of the list as undefined (ignored if list not defined as String,Entity or Any)
        """
    def CopyFrom(self,other : StepData_Field) -> None: 
        """
        Gets the copy of the values of another field
        """
    def Entity(self,n1 : int=1,n2 : int=1) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Enum(self,n1 : int=1,n2 : int=1) -> int: 
        """
        None
        """
    def EnumText(self,n1 : int=1,n2 : int=1) -> str: 
        """
        None
        """
    def Int(self) -> int: 
        """
        None
        """
    def Integer(self,n1 : int=1,n2 : int=1) -> int: 
        """
        None
        """
    def IsSet(self,n1 : int=1,n2 : int=1) -> bool: 
        """
        None
        """
    def ItemKind(self,n1 : int=1,n2 : int=1) -> int: 
        """
        Returns the kind of an item in a list or double list It is the kind of the list, except if it is "Any", in such a case the true kind is determined and returned
        """
    def Kind(self,type : bool=True) -> int: 
        """
        Returns the kind of the field <type> True (D) : returns only the type itself else, returns the complete kind
        """
    def Length(self,index : int=1) -> int: 
        """
        None
        """
    def Logical(self,n1 : int=1,n2 : int=1) -> StepData_Logical: 
        """
        None
        """
    def Lower(self,index : int=1) -> int: 
        """
        None
        """
    def Real(self,n1 : int=1,n2 : int=1) -> float: 
        """
        None
        """
    def Set(self,val : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets an undetermined value : can be String, SelectMember, HArray(1-2) ... else, an Entity In case of an HArray, determines and records its size(s)
        """
    @overload
    def SetBoolean(self,num : int,val : bool) -> None: 
        """
        Sets a Boolean value (or predeclares a list as boolean)

        None
        """
    @overload
    def SetBoolean(self,val : bool=False) -> None: ...
    def SetDerived(self) -> None: 
        """
        Codes a Field as derived (no proper value)
        """
    @overload
    def SetEntity(self,num : int,val : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets an Entity Value

        Predeclares a list as of entity

        None
        """
    @overload
    def SetEntity(self,val : OCP.Standard.Standard_Transient) -> None: ...
    @overload
    def SetEntity(self) -> None: ...
    @overload
    def SetEnum(self,val : int=-1,text : str='') -> None: 
        """
        Sets an Enum Value (as its integer counterpart) (or predeclares a list as Enum) If <text> is given , also sets its textual expression <val> negative means unknown (known values begin at 0)

        Sets an Enum Value (Integer counterpart), also its text expression if known (if list has been set as "any")
        """
    @overload
    def SetEnum(self,num : int,val : int,text : str='') -> None: ...
    @overload
    def SetInt(self,val : int) -> None: 
        """
        Directly sets the Integer value, if its Kind matches Integer, Boolean, Logical, or Enum (does not change Kind)

        Internal access to an Integer Value for a list, plus its kind
        """
    @overload
    def SetInt(self,num : int,val : int,kind : int) -> None: ...
    @overload
    def SetInteger(self,num : int,val : int) -> None: 
        """
        Sets an Integer value (before SetList* declares it as Integer)

        Sets an Integer Value for a list (rank num) (recognizes a SelectMember)
        """
    @overload
    def SetInteger(self,val : int=0) -> None: ...
    def SetList(self,size : int,first : int=1) -> None: 
        """
        Declares a field as a list, with an initial size Initial lower is defaulted as 1, can be defined The list starts empty, typed by the last Set* If no Set* before, sets it as "any" (transient/select)
        """
    def SetList2(self,siz1 : int,siz2 : int,f1 : int=1,f2 : int=1) -> None: 
        """
        Declares a field as an homogeneous square list, with initial sizes, and initial lowers
        """
    @overload
    def SetLogical(self,val : StepData_Logical=StepData_Logical.StepData_LFalse) -> None: 
        """
        Sets a Logical Value (or predeclares a list as logical)

        None
        """
    @overload
    def SetLogical(self,num : int,val : StepData_Logical) -> None: ...
    @overload
    def SetReal(self,num : int,val : float) -> None: 
        """
        Sets a Real Value (or predeclares a list as Real);

        None
        """
    @overload
    def SetReal(self,val : float=0.0) -> None: ...
    def SetSelectMember(self,val : StepData_SelectMember) -> None: 
        """
        Sets a SelectMember (for Integer,Boolean,Enum,Real,Logical) Hence, the value of the field is accessed through this member
        """
    @overload
    def SetString(self,val : str='') -> None: 
        """
        Sets a String Value (or predeclares a list as String) Does not redefine the Kind if it is alread String or Enum

        None
        """
    @overload
    def SetString(self,num : int,val : str) -> None: ...
    def String(self,n1 : int=1,n2 : int=1) -> str: 
        """
        None
        """
    def Transient(self) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    @overload
    def __init__(self,other : StepData_Field,copy : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class StepData_FieldList():
    """
    Describes a list of fields, in a general way This basic class is for a null size list Subclasses are for 1, N (fixed) or Dynamic sizes
    """
    def CField(self,num : int) -> StepData_Field: 
        """
        Returns the field n0 <num> between 1 and NbFields, in order to modify its content
        """
    def Field(self,num : int) -> StepData_Field: 
        """
        Returns the field n0 <num> between 1 and NbFields (read only)
        """
    def FillShared(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills an iterator with the entities shared by <me>
        """
    def NbFields(self) -> int: 
        """
        Returns the count of fields. Here, returns 0
        """
    def __init__(self) -> None: ...
    pass
class StepData_FieldList1(StepData_FieldList):
    """
    Describes a list of ONE field
    """
    def CField(self,num : int) -> StepData_Field: 
        """
        Returns the field n0 <num> between 1 and NbFields, in order to modify its content
        """
    def Field(self,num : int) -> StepData_Field: 
        """
        Returns the field n0 <num> between 1 and NbFields (read only)
        """
    def FillShared(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills an iterator with the entities shared by <me>
        """
    def NbFields(self) -> int: 
        """
        Returns the count of fields. Here, returns 1
        """
    def __init__(self) -> None: ...
    pass
class StepData_FieldListD(StepData_FieldList):
    """
    Describes a list of fields, in a general way This basic class is for a null size list Subclasses are for 1, N (fixed) or Dynamic sizes
    """
    def CField(self,num : int) -> StepData_Field: 
        """
        Returns the field n0 <num> between 1 and NbFields, in order to modify its content
        """
    def Field(self,num : int) -> StepData_Field: 
        """
        Returns the field n0 <num> between 1 and NbFields (read only)
        """
    def FillShared(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills an iterator with the entities shared by <me>
        """
    def NbFields(self) -> int: 
        """
        Returns the count of fields. Here, returns starting <nb>
        """
    def SetNb(self,nb : int) -> None: 
        """
        Sets a new count of Fields. Former contents are lost
        """
    def __init__(self,nb : int) -> None: ...
    pass
class StepData_FieldListN(StepData_FieldList):
    """
    Describes a list of fields, in a general way This basic class is for a null size list Subclasses are for 1, N (fixed) or Dynamic sizes
    """
    def CField(self,num : int) -> StepData_Field: 
        """
        Returns the field n0 <num> between 1 and NbFields, in order to modify its content
        """
    def Field(self,num : int) -> StepData_Field: 
        """
        Returns the field n0 <num> between 1 and NbFields (read only)
        """
    def FillShared(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills an iterator with the entities shared by <me>
        """
    def NbFields(self) -> int: 
        """
        Returns the count of fields. Here, returns starting <nb>
        """
    def __init__(self,nb : int) -> None: ...
    pass
class StepData_Protocol(OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    Description of Basic Protocol for Step The class Protocol from StepData itself describes a default Protocol, which recognizes only UnknownEntities. Sub-classes will redefine CaseNumber and, if necessary, NbResources and Resources.Description of Basic Protocol for Step The class Protocol from StepData itself describes a default Protocol, which recognizes only UnknownEntities. Sub-classes will redefine CaseNumber and, if necessary, NbResources and Resources.Description of Basic Protocol for Step The class Protocol from StepData itself describes a default Protocol, which recognizes only UnknownEntities. Sub-classes will redefine CaseNumber and, if necessary, NbResources and Resources.
    """
    @staticmethod
    def Active_s() -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Active Protocol, if defined (else, returns a Null Handle, which means "no defined active protocol")
        """
    def AddBasicDescr(self,esdescr : StepData_ESDescr) -> None: 
        """
        Records an ESDescr, intended to build complex descriptions
        """
    def AddDescr(self,adescr : StepData_EDescr,CN : int) -> None: 
        """
        Records an EDescr with its case number Also records its name for an ESDescr (simple type): an ESDescr is then used, for case number, or for type name
        """
    def AddPDescr(self,pdescr : StepData_PDescr) -> None: 
        """
        Records an PDescr
        """
    def BasicDescr(self,name : str,anylevel : bool=True) -> StepData_EDescr: 
        """
        Returns a basic description according to its name <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    def CaseNumber(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns a unique positive number for any recognized entity Redefined to work by calling both TypeNumber and, for a Described Entity (late binding) DescrNumber
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
    @overload
    def Descr(self,name : str,anylevel : bool=True) -> StepData_EDescr: 
        """
        Returns the description attached to a case number, or null

        Returns a description according to its name <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    @overload
    def Descr(self,num : int) -> StepData_EDescr: ...
    def DescrNumber(self,adescr : StepData_EDescr) -> int: 
        """
        Returns a unique positive CaseNumber for types described by an EDescr (late binding) Warning : TypeNumber and DescrNumber must give together a unique positive case number for each distinct case, type or descr
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ECDescr(self,names : OCP.TColStd.TColStd_SequenceOfAsciiString,anylevel : bool=True) -> StepData_ECDescr: 
        """
        Returns a complex description according to list of names <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    def ESDescr(self,name : str,anylevel : bool=True) -> StepData_ESDescr: 
        """
        Idem as Descr but cast to simple description
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlobalCheck(self,G : OCP.Interface.Interface_Graph,ach : OCP.Interface.Interface_Check) -> bool: 
        """
        Evaluates a Global Check for a model (with its Graph) Returns True when done, False if data in model do not apply
        """
    def HasDescr(self) -> bool: 
        """
        Tells if a Protocol brings at least one ESDescr, i.e. if it defines at least one entity description by ESDescr mechanism
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
    def IsSuitableModel(self,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True if <model> is a Model of Step Norm
        """
    def IsUnknownEntity(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e. Type UndefinedEntity, status Unknown
        """
    def NbResources(self) -> int: 
        """
        Gives the count of Protocols used as Resource (can be zero) Here, No resource
        """
    def NbTypes(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the count of DISTINCT types under which an entity may be processed. Each one is candidate to be recognized by TypeNumber, <obj> is then processed according it By default, returns 1 (the DynamicType)
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Creates an empty Model for Step Norm
        """
    def PDescr(self,name : str,anylevel : bool=True) -> StepData_PDescr: 
        """
        Returns a parameter description according to its name <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    def Resource(self,num : int) -> OCP.Interface.Interface_Protocol: 
        """
        Returns a Resource, given a rank. Here, none
        """
    def SchemaName(self) -> str: 
        """
        Returns the Schema Name attached to each class of Protocol To be redefined by each sub-class Here, SchemaName returns "(DEFAULT)" was C++ : return const
        """
    @staticmethod
    def SetActive_s(aprotocol : OCP.Interface.Interface_Protocol) -> None: 
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
        Returns a Case Number, specific of each recognized Type Here, only Unknown Entity is recognized
        """
    def UnknownEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Creates a new Unknown Entity for Step (UndefinedEntity)
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
class StepData_FileRecognizer(OCP.Standard.Standard_Transient):
    def Add(self,reco : StepData_FileRecognizer) -> None: 
        """
        Adds a new Recognizer to the Compound, at the end Several calls to Add work by adding in the order of calls : Hence, when Eval has failed to recognize, Evaluate will call Evaluate from the first added Recognizer if there is one, and to the second if there is still no result, and so on
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
    def Evaluate(self,akey : OCP.TCollection.TCollection_AsciiString,res : OCP.Standard.Standard_Transient) -> bool: 
        """
        Evaluates if recognition has a result, returns it if yes In case of success, Returns True and puts result in "res" In case of Failure, simply Returns False Works by calling deferred method Eval, and in case of failure, looks for Added Recognizers to work
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
    def Result(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns result of last recognition (call of Evaluate)
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
class StepData_FreeFormEntity(OCP.Standard.Standard_Transient):
    """
    A Free Form Entity allows to record any kind of STEP parameters, in any way of typing It is implemented with an array of fields A Complex entity can be defined, as a chain of FreeFormEntity (see Next and As)A Free Form Entity allows to record any kind of STEP parameters, in any way of typing It is implemented with an array of fields A Complex entity can be defined, as a chain of FreeFormEntity (see Next and As)A Free Form Entity allows to record any kind of STEP parameters, in any way of typing It is implemented with an array of fields A Complex entity can be defined, as a chain of FreeFormEntity (see Next and As)
    """
    def CField(self,num : int) -> StepData_Field: 
        """
        Returns a field from its rank, in order to modify it
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
    def Field(self,num : int) -> StepData_Field: 
        """
        Returns a field from its rank, for read-only use
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsComplex(self) -> bool: 
        """
        Returns True if a FreeFormEntity is Complex (i.e. has Next)
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
    def NbFields(self) -> int: 
        """
        Returns the count of fields
        """
    def Next(self) -> StepData_FreeFormEntity: 
        """
        Returns the next member of a Complex entity (remark : the last member has none)
        """
    @staticmethod
    def Reorder_s(ent : StepData_FreeFormEntity) -> bool: 
        """
        Reorders a Complex entity if required, i.e. if member types are not in alphabetic order Returns False if nothing done (order was OK or simple entity), True plus modified <ent> if <ent> has been reordered
        """
    def SetNbFields(self,nb : int) -> None: 
        """
        Sets a count of Fields, from scratch
        """
    def SetNext(self,next : StepData_FreeFormEntity,last : bool=True) -> None: 
        """
        Sets a next member, in order to define or complete a Complex entity If <last> is True (D), this next will be set as last of list Else, it is inserted just as next of <me> If <next> is Null, Next is cleared
        """
    def SetStepType(self,typenam : str) -> None: 
        """
        Sets the type of an entity For a complex one, the type of this member
        """
    def StepType(self) -> str: 
        """
        Returns the recorded StepType For a complex one, the type of this member
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeList(self) -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        Returns the list of types (one type for a simple entity), as is (non reordered)
        """
    def Typed(self,typenam : str) -> StepData_FreeFormEntity: 
        """
        Returns the member of a FreeFormEntity of which the type name is given (exact match, no sub-type)
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
class StepData_DefaultGeneral(StepData_GeneralModule, OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    DefaultGeneral defines a GeneralModule which processes Unknown Entity from StepData onlyDefaultGeneral defines a GeneralModule which processes Unknown Entity from StepData onlyDefaultGeneral defines a GeneralModule which processes Unknown Entity from StepData only
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" Remark that it should be in phase with the implementation of NewVoid+CopyCase/NewCopyCase Default returns always False, can be redefined
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> int: 
        """
        Returns a category number which characterizes an entity Category Numbers are managed by the class Category <shares> can be used to evaluate this number in the context Default returns 0 which means "unspecified"
        """
    def CheckCase(self,casenum : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Specific Checking of an Entity <ent>
        """
    def CopyCase(self,casenum : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Copy ("Deep") from <entfrom> to <entto> (same type) by using a CopyTool which provides its working Map. Use method Transferred from TransferControl to work
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dispatch(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Dispatches an entity Returns True if it works by copy, False if it just duplicates the starting Handle
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FillShared(self,model : OCP.Interface.Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific filling of the list of Entities shared by an Entity <ent>, according a Case Number <CN> (formerly computed by CaseNum), considered in the context of a Model <model> Default calls FillSharedCase (i.e., ignores the model) Can be redefined to use the model for working
        """
    def FillSharedCase(self,casenum : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific filling of the list of Entities shared by an Entity <ent>, which is an UnknownEntity from StepData.
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
    def ListImplied(self,model : OCP.Interface.Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> considered in the context of a Model <model> : i.e. the Entities which are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillShared + ListImplied give the complete list of References Default calls ListImpliedCase (i.e. ignores the model) Can be redefined to use the model for working
        """
    def ListImpliedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> (see above) are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillSharedCase + ListImpliedCase give the complete list of Referenced Entities The provided default method does nothing (Implied References are specific of a little amount of Entity Classes).
        """
    def Name(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Determines if an entity brings a Name (or widerly, if a Name can be attached to it, through the ShareTool By default, returns a Null Handle (no name can be produced) Can be redefined
        """
    def NewCopiedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Specific operator (create+copy) defaulted to do nothing. It can be redefined : When it is not possible to work in two steps (NewVoid then CopyCase). This can occur when there is no default constructor : hence the result <entto> must be created with an effective definition. Remark : if NewCopiedCase is defined, CopyCase has nothing to do Returns True if it has produced something, false else
        """
    def NewVoid(self,CN : int,entto : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific creation of a new void entity
        """
    def RenewImpliedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Specific Copying of Implied References A Default is provided which does nothing (must current case !) Already copied references (by CopyFrom) must remain unchanged Use method Search from CopyTool to work
        """
    def Share(self,iter : OCP.Interface.Interface_EntityIterator,shared : OCP.Standard.Standard_Transient) -> None: 
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
class StepData_GlobalNodeOfWriterLib(OCP.Standard.Standard_Transient):
    def Add(self,amodule : StepData_ReadWriteModule,aprotocol : StepData_Protocol) -> None: 
        """
        Adds a Module bound with a Protocol to the list : does nothing if already in the list, THAT IS, Same Type (exact match) and Same State (that is, IsEqual is not required) Once added, stores its attached Protocol in correspondance
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
    def Module(self) -> StepData_ReadWriteModule: 
        """
        Returns the Module stored in a given GlobalNode
        """
    def Next(self) -> StepData_GlobalNodeOfWriterLib: 
        """
        Returns the Next GlobalNode. If none is defined, returned value is a Null Handle
        """
    def Protocol(self) -> StepData_Protocol: 
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
class StepData_HArray1OfField(StepData_Array1OfField, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepData_Array1OfField: 
        """
        None
        """
    def Assign(self,theOther : StepData_Array1OfField) -> StepData_Array1OfField: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepData_Array1OfField: 
        """
        None
        """
    def ChangeFirst(self) -> StepData_Field: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepData_Field: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepData_Field: 
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
    def First(self) -> StepData_Field: 
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
    def Init(self,theValue : StepData_Field) -> None: 
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
    def Last(self) -> StepData_Field: 
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
    def Move(self,theOther : StepData_Array1OfField) -> StepData_Array1OfField: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepData_Field) -> None: 
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
    def Value(self,theIndex : int) -> StepData_Field: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepData_Array1OfField) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepData_Field) -> None: ...
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
class StepData_Logical():
    """
    A Standard Definition for STEP (which knows Boolean too)

    Members:

      StepData_LFalse

      StepData_LTrue

      StepData_LUnknown
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    StepData_LFalse: OCP.StepData.StepData_Logical # value = <StepData_Logical.StepData_LFalse: 0>
    StepData_LTrue: OCP.StepData.StepData_Logical # value = <StepData_Logical.StepData_LTrue: 1>
    StepData_LUnknown: OCP.StepData.StepData_Logical # value = <StepData_Logical.StepData_LUnknown: 2>
    __entries: dict # value = {'StepData_LFalse': (<StepData_Logical.StepData_LFalse: 0>, None), 'StepData_LTrue': (<StepData_Logical.StepData_LTrue: 1>, None), 'StepData_LUnknown': (<StepData_Logical.StepData_LUnknown: 2>, None)}
    __members__: dict # value = {'StepData_LFalse': <StepData_Logical.StepData_LFalse: 0>, 'StepData_LTrue': <StepData_Logical.StepData_LTrue: 1>, 'StepData_LUnknown': <StepData_Logical.StepData_LUnknown: 2>}
    pass
class StepData_NodeOfWriterLib(OCP.Standard.Standard_Transient):
    def AddNode(self,anode : StepData_GlobalNodeOfWriterLib) -> None: 
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
    def Module(self) -> StepData_ReadWriteModule: 
        """
        Returns the Module designated by a precise Node
        """
    def Next(self) -> StepData_NodeOfWriterLib: 
        """
        Returns the Next Node. If none was defined, returned value is a Null Handle
        """
    def Protocol(self) -> StepData_Protocol: 
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
class StepData_PDescr(OCP.Standard.Standard_Transient):
    """
    This class is intended to describe the authorized form for a parameter, as a type or a value for a fieldThis class is intended to describe the authorized form for a parameter, as a type or a value for a fieldThis class is intended to describe the authorized form for a parameter, as a type or a value for a field
    """
    def AddArity(self,arity : int=1) -> None: 
        """
        Adds an arity count to <me>, by default 1 1 : a simple field passes to a LIST/ARRAY etc or a LIST to a LIST OF LIST 2 : a simple field passes to a LIST OF LIST
        """
    def AddEnumDef(self,enumdef : str) -> None: 
        """
        Adds an enum value as a string
        """
    def AddMember(self,member : StepData_PDescr) -> None: 
        """
        Adds a member to a SELECT description
        """
    def Arity(self) -> int: 
        """
        Returns the arity of <me>
        """
    def Check(self,afild : StepData_Field,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Semantic Check of a Field : does it complies with the given description ?
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DescrName(self) -> str: 
        """
        Returns the description (type name) to match, for a Described (else, empty string)
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnumMax(self) -> int: 
        """
        Returns the maximum integer for a suitable value (count - 1)
        """
    def EnumText(self,val : int) -> str: 
        """
        Returns the text which corresponds to a numeric value, between 0 and EnumMax. It is limited by dots
        """
    def EnumValue(self,name : str) -> int: 
        """
        Returns the numeric value found for an enum text The text must be in capitals and limited by dots A non-suitable text gives a negative value to be returned
        """
    def FieldName(self) -> str: 
        """
        None
        """
    def FieldRank(self) -> int: 
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
    def IsBoolean(self) -> bool: 
        """
        Tells if <me> is for a Boolean value (false,true)
        """
    def IsDerived(self) -> bool: 
        """
        Tells if <me> is Derived
        """
    def IsDescr(self,descr : StepData_EDescr) -> bool: 
        """
        Tells if <me> is for a Described entity of a given EDescr (does this EDescr match description name ?). For late-bnd (works for <me> + nexts if <me> is a Select)
        """
    def IsEntity(self) -> bool: 
        """
        Tells if <me> is for an Entity, either Described or CDL Type
        """
    def IsEnum(self) -> bool: 
        """
        Tells if <me> is for an Enum value Then, call AddEnumDef ordered from the first one (value 0) Managed by an EnumTool
        """
    def IsField(self) -> bool: 
        """
        Tells if <me> is a Field. Else it is a Type
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInteger(self) -> bool: 
        """
        Tells if <me> is for an Integer
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsLogical(self) -> bool: 
        """
        Tells if <me> is for a Logical value (false,true,unknown)
        """
    def IsOptional(self) -> bool: 
        """
        Tells if <me> is Optional
        """
    def IsReal(self) -> bool: 
        """
        Tells if <me> is for a Real value
        """
    def IsSelect(self) -> bool: 
        """
        Tells if <me> is for a SELECT
        """
    def IsString(self) -> bool: 
        """
        Tells if <me> is for a String value
        """
    def IsType(self,atype : OCP.Standard.Standard_Type) -> bool: 
        """
        Tells if <me> is for an entity of a given CDL type (early-bnd) (works for <me> + nexts if <me> is a Select)
        """
    def Member(self,name : str) -> StepData_PDescr: 
        """
        For a SELECT, returns the member whose name matches <name> To this member, the following question can then be asked Null Handle if <name> not matched or <me> not a SELECT
        """
    def Name(self) -> str: 
        """
        None
        """
    def SetArity(self,arity : int=1) -> None: 
        """
        Directly sets the arity count 0 : simple field 1 : LIST or ARRAY etc 2 : LIST OF LIST
        """
    def SetBoolean(self) -> None: 
        """
        Sets <me> for a Boolean value (false,true)
        """
    def SetDerived(self,der : bool=True) -> None: 
        """
        Sets/Unsets <me> to be for a derived field
        """
    def SetDescr(self,dscnam : str) -> None: 
        """
        Sets <me> for a Described Entity, whose Description must match the type name <dscnam>
        """
    def SetEnum(self) -> None: 
        """
        Sets <me> for an Enum value Then, call AddEnumDef ordered from the first one (value 0)
        """
    def SetField(self,name : str,rank : int) -> None: 
        """
        Sets <me> to describe a field of an entity With a name and a rank
        """
    def SetFrom(self,other : StepData_PDescr) -> None: 
        """
        Sets <me> as <other> but duplicated Hence, some definition may be changed
        """
    def SetInteger(self) -> None: 
        """
        Sets <me> for an Integer value
        """
    def SetLogical(self) -> None: 
        """
        Sets <me> for a Logical value (false,true,unknown)
        """
    def SetMemberName(self,memname : str) -> None: 
        """
        Sets a name for SELECT member. To be used if a member is for an immediate type
        """
    def SetName(self,name : str) -> None: 
        """
        None
        """
    def SetOptional(self,opt : bool=True) -> None: 
        """
        Sets/Unsets <me> to accept undefined values
        """
    def SetReal(self) -> None: 
        """
        Sets <me> for a Real value
        """
    def SetSelect(self) -> None: 
        """
        Declares this PDescr to be a Select, hence to have members <me> itself can be the first member
        """
    def SetString(self) -> None: 
        """
        Sets <me> for a String value
        """
    def SetType(self,atype : OCP.Standard.Standard_Type) -> None: 
        """
        Sets <me> for an Entity which must match a Type (early-bound)
        """
    def Simple(self) -> StepData_PDescr: 
        """
        For a LIST or LIST OF LIST, Returns the PDescr for the simpler PDescr. Else, returns <me> This allows to have different attributes for Optional for instance, on a field, and on the parameter of a LIST : [OPTIONAL] LIST OF [OPTIONAL] ...
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the type to match (IsKind), for a CDL Entity (else, null handle)
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
class StepData_Plex(StepData_Described, OCP.Standard.Standard_Transient):
    """
    A Plex (for Complex) Entity is defined as a list of Simple Members ("external mapping") The types of these members must be in alphabetic orderA Plex (for Complex) Entity is defined as a list of Simple Members ("external mapping") The types of these members must be in alphabetic orderA Plex (for Complex) Entity is defined as a list of Simple Members ("external mapping") The types of these members must be in alphabetic order
    """
    def Add(self,member : StepData_Simple) -> None: 
        """
        Adds a member to <me>
        """
    def As(self,steptype : str) -> StepData_Simple: 
        """
        Returns a Simple Entity which matches with a Type in <me> : For a Simple Entity : me if it matches, else a null handle For a Complex Entity : the member which matches, else null
        """
    def CField(self,name : str) -> StepData_Field: 
        """
        Returns a Field from its name; read or write
        """
    def Check(self,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Fills a Check by using its Description
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> StepData_EDescr: 
        """
        Returns the Description used to define this entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ECDescr(self) -> StepData_ECDescr: 
        """
        Returns the Description as for a Plex
        """
    def Field(self,name : str) -> StepData_Field: 
        """
        Returns a Field from its name; read-only
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasField(self,name : str) -> bool: 
        """
        Tells if a Field brings a given name
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsComplex(self) -> bool: 
        """
        Returns False
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
    def Matches(self,steptype : str) -> bool: 
        """
        Tells if a step type is matched by <me> For a Simple Entity : own type or super type For a Complex Entity : one of the members
        """
    def Member(self,num : int) -> StepData_Simple: 
        """
        Returns a simple member from its rank
        """
    def NbMembers(self) -> int: 
        """
        Returns the count of simple members
        """
    def Shared(self,list : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills an EntityIterator with entities shared by <me>
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypeList(self) -> OCP.TColStd.TColStd_HSequenceOfAsciiString: 
        """
        Returns the actual list of members types
        """
    def __init__(self,descr : StepData_ECDescr) -> None: ...
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
class StepData_FileProtocol(StepData_Protocol, OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    A FileProtocol is defined as the addition of several already existing Protocols. It corresponds to the definition of a SchemaName with several Names, each one being attached to a specific Protocol. Thus, a File defined with a compound Schema is processed as any other one, once built the equivalent compound Protocol, a FileProtocolA FileProtocol is defined as the addition of several already existing Protocols. It corresponds to the definition of a SchemaName with several Names, each one being attached to a specific Protocol. Thus, a File defined with a compound Schema is processed as any other one, once built the equivalent compound Protocol, a FileProtocolA FileProtocol is defined as the addition of several already existing Protocols. It corresponds to the definition of a SchemaName with several Names, each one being attached to a specific Protocol. Thus, a File defined with a compound Schema is processed as any other one, once built the equivalent compound Protocol, a FileProtocol
    """
    @staticmethod
    def Active_s() -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Active Protocol, if defined (else, returns a Null Handle, which means "no defined active protocol")
        """
    def Add(self,protocol : StepData_Protocol) -> None: 
        """
        Adds a Protocol to the definition list of the FileProtocol But ensures that each class of Protocol is present only once in this list
        """
    def AddBasicDescr(self,esdescr : StepData_ESDescr) -> None: 
        """
        Records an ESDescr, intended to build complex descriptions
        """
    def AddDescr(self,adescr : StepData_EDescr,CN : int) -> None: 
        """
        Records an EDescr with its case number Also records its name for an ESDescr (simple type): an ESDescr is then used, for case number, or for type name
        """
    def AddPDescr(self,pdescr : StepData_PDescr) -> None: 
        """
        Records an PDescr
        """
    def BasicDescr(self,name : str,anylevel : bool=True) -> StepData_EDescr: 
        """
        Returns a basic description according to its name <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    def CaseNumber(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns a unique positive number for any recognized entity Redefined to work by calling both TypeNumber and, for a Described Entity (late binding) DescrNumber
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
    @overload
    def Descr(self,name : str,anylevel : bool=True) -> StepData_EDescr: 
        """
        Returns the description attached to a case number, or null

        Returns a description according to its name <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    @overload
    def Descr(self,num : int) -> StepData_EDescr: ...
    def DescrNumber(self,adescr : StepData_EDescr) -> int: 
        """
        Returns a unique positive CaseNumber for types described by an EDescr (late binding) Warning : TypeNumber and DescrNumber must give together a unique positive case number for each distinct case, type or descr
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ECDescr(self,names : OCP.TColStd.TColStd_SequenceOfAsciiString,anylevel : bool=True) -> StepData_ECDescr: 
        """
        Returns a complex description according to list of names <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    def ESDescr(self,name : str,anylevel : bool=True) -> StepData_ESDescr: 
        """
        Idem as Descr but cast to simple description
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlobalCheck(self,G : OCP.Interface.Interface_Graph,ach : OCP.Interface.Interface_Check) -> bool: 
        """
        Calls GlobalCheck for each of its recorded ressources
        """
    def HasDescr(self) -> bool: 
        """
        Tells if a Protocol brings at least one ESDescr, i.e. if it defines at least one entity description by ESDescr mechanism
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
    def IsSuitableModel(self,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True if <model> is a Model of Step Norm
        """
    def IsUnknownEntity(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e. Type UndefinedEntity, status Unknown
        """
    def NbResources(self) -> int: 
        """
        Gives the count of Protocols used as Resource (can be zero) i.e. the count of Protocol recorded by calling the method Add
        """
    def NbTypes(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the count of DISTINCT types under which an entity may be processed. Each one is candidate to be recognized by TypeNumber, <obj> is then processed according it By default, returns 1 (the DynamicType)
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Creates an empty Model for Step Norm
        """
    def PDescr(self,name : str,anylevel : bool=True) -> StepData_PDescr: 
        """
        Returns a parameter description according to its name <anylevel> True (D) : for <me> and its resources <anylevel> False : for <me> only
        """
    def Resource(self,num : int) -> OCP.Interface.Interface_Protocol: 
        """
        Returns a Resource, given a rank. Here, rank of calling Add
        """
    def SchemaName(self) -> str: 
        """
        Returns the Schema Name attached to each class of Protocol To be redefined by each sub-class Here, SchemaName returns "" (empty String) was C++ : return const
        """
    @staticmethod
    def SetActive_s(aprotocol : OCP.Interface.Interface_Protocol) -> None: 
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
        Returns a Case Number, specific of each recognized Type Here, NO Type at all is recognized properly : all Types are recognized by the resources
        """
    def UnknownEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Creates a new Unknown Entity for Step (UndefinedEntity)
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
class StepData_ReadWriteModule(OCP.Interface.Interface_ReaderModule, OCP.Standard.Standard_Transient):
    """
    Defines basic File Access Module (Recognize, Read, Write) That is : ReaderModule (Recognize & Read) + Write for StepWriter (for a more centralized description) Warning : A sub-class of ReadWriteModule, which belongs to a particular Protocol, must use the same definition for Case Numbers (give the same Value for a StepType defined as a String from a File as the Protocol does for the corresponding Entity)Defines basic File Access Module (Recognize, Read, Write) That is : ReaderModule (Recognize & Read) + Write for StepWriter (for a more centralized description) Warning : A sub-class of ReadWriteModule, which belongs to a particular Protocol, must use the same definition for Case Numbers (give the same Value for a StepType defined as a String from a File as the Protocol does for the corresponding Entity)Defines basic File Access Module (Recognize, Read, Write) That is : ReaderModule (Recognize & Read) + Write for StepWriter (for a more centralized description) Warning : A sub-class of ReadWriteModule, which belongs to a particular Protocol, must use the same definition for Case Numbers (give the same Value for a StepType defined as a String from a File as the Protocol does for the corresponding Entity)
    """
    def CaseNum(self,data : OCP.Interface.Interface_FileReaderData,num : int) -> int: 
        """
        Translate the Type of record <num> in <data> to a positive Case Number, or 0 if failed. Works with a StepReaderData, in which the Type of an Entity is defined as a String : Reads the RecordType <num> then calls CaseNum (this type) Warning : The methods CaseStep, StepType and Recognize, must be in phase (triplets CaseNum-StepType-Type of Object)
        """
    @overload
    def CaseStep(self,atype : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        Defines Case Numbers corresponding to the recognized Types Called by CaseNum (data,num) above for a Simple Type Entity Warning : CaseStep must give the same Value as Protocol does for the Entity type which corresponds to this Type given as a String

        Same a above but for a Complex Type Entity ("Plex") The provided Default recognizes nothing
        """
    @overload
    def CaseStep(self,types : OCP.TColStd.TColStd_SequenceOfAsciiString) -> int: ...
    def ComplexType(self,CN : int,types : OCP.TColStd.TColStd_SequenceOfAsciiString) -> bool: 
        """
        Function specific to STEP, which delivers the list of types which corresponds to a complex type. If <CN> is not for a complex type, this method returns False. Else it returns True and fills the list in alphabetic order. The default returns False. To be redefined as required.
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
    def IsComplex(self,CN : int) -> bool: 
        """
        Returns True if the Case Number corresponds to a Complex Type ("Plex"). Remember that all possible combinations must be aknowledged to be processed Default is False for all cases. For a Protocol which defines possible Plexes, this method must be redefined.
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
    def NewRead(self,casenum : int,data : OCP.Interface.Interface_FileReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific operator (create+read) defaulted to do nothing. It can be redefined when it is not possible to work in two steps (NewVoid then Read). This occurs when no default constructor is defined : hence the result <ent> must be created with an effective definition from the reader. Remark : if NewRead is defined, Copy has nothing to do.
        """
    def Read(self,CN : int,data : OCP.Interface.Interface_FileReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> Any: 
        """
        General Read Function, calls ReadStep
        """
    def ReadStep(self,CN : int,data : StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> Any: 
        """
        Specific Read Function. Works with StepReaderData
        """
    def ShortType(self,CN : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Function specific to STEP. Some STEP Types have a short form This method can be redefined to fill it By default, returns an empty string, which is then interpreted to take normal form from StepType
        """
    def StepType(self,CN : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Function specific to STEP, which delivers the StepType as it is recorded in and read from a File compliant with STEP. This method is symmetric to the method CaseStep. StepType can be different from Dynamic Type's name, but belongs to the same class of Object. Returns an empty String if <CN> is zero. Warning : For a Complex Type Entity, returns an Empty String (Complex Type must be managed by users)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteStep(self,CN : int,SW : StepData_StepWriter,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Write Function, switched by CaseNum
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
class StepData_SelectMember(OCP.Standard.Standard_Transient):
    """
    The general form for a Select Member. A Select Member can, either define a value of a basic type (such as an integer) with an additional information : a name or list of names which precise the meaning of this value or be an alternate value in a select, which also accepts an entity (in this case, the name is not mandatory)The general form for a Select Member. A Select Member can, either define a value of a basic type (such as an integer) with an additional information : a name or list of names which precise the meaning of this value or be an alternate value in a select, which also accepts an entity (in this case, the name is not mandatory)The general form for a Select Member. A Select Member can, either define a value of a basic type (such as an integer) with an additional information : a name or list of names which precise the meaning of this value or be an alternate value in a select, which also accepts an entity (in this case, the name is not mandatory)
    """
    def Boolean(self) -> bool: 
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
    def Enum(self) -> int: 
        """
        None
        """
    def EnumText(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        Tells if a SelectMember has a name. Default is False
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
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
    def Kind(self) -> int: 
        """
        None
        """
    def Logical(self) -> StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        Returns the name of a SelectMember. Default is empty
        """
    def ParamType(self) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the Kind of the SelectMember, under the form of an enum ParamType
        """
    def Real(self) -> float: 
        """
        None
        """
    def SetBoolean(self,val : bool) -> None: 
        """
        None
        """
    def SetEnum(self,val : int,text : str='') -> None: 
        """
        None
        """
    def SetEnumText(self,val : int,text : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it)
        """
    def SetInteger(self,val : int) -> None: 
        """
        None
        """
    def SetKind(self,kind : int) -> None: 
        """
        None
        """
    def SetLogical(self,val : StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        Sets the name of a SelectMember, returns True if done, False if no name is allowed Default does nothing and returns False
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def String(self) -> str: 
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
class StepData_SelectInt(StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    A SelectInt is a SelectMember specialised for a basic integer type in a select which also accepts entities : this one has NO NAME. For a named select, see SelectNamedA SelectInt is a SelectMember specialised for a basic integer type in a select which also accepts entities : this one has NO NAME. For a named select, see SelectNamedA SelectInt is a SelectMember specialised for a basic integer type in a select which also accepts entities : this one has NO NAME. For a named select, see SelectNamed
    """
    def Boolean(self) -> bool: 
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
    def Enum(self) -> int: 
        """
        None
        """
    def EnumText(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        Tells if a SelectMember has a name. Default is False
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        None
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
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
    def Kind(self) -> int: 
        """
        None
        """
    def Logical(self) -> StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        Returns the name of a SelectMember. Default is empty
        """
    def ParamType(self) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the Kind of the SelectMember, under the form of an enum ParamType
        """
    def Real(self) -> float: 
        """
        None
        """
    def SetBoolean(self,val : bool) -> None: 
        """
        None
        """
    def SetEnum(self,val : int,text : str='') -> None: 
        """
        None
        """
    def SetEnumText(self,val : int,text : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        None
        """
    def SetInteger(self,val : int) -> None: 
        """
        None
        """
    def SetKind(self,kind : int) -> None: 
        """
        None
        """
    def SetLogical(self,val : StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        Sets the name of a SelectMember, returns True if done, False if no name is allowed Default does nothing and returns False
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def String(self) -> str: 
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
class StepData_SelectNamed(StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    This select member can be of any kind, and be named But its takes more memory than some specialised ones This class allows one name for the instanceThis select member can be of any kind, and be named But its takes more memory than some specialised ones This class allows one name for the instanceThis select member can be of any kind, and be named But its takes more memory than some specialised ones This class allows one name for the instance
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CField(self) -> StepData_Field: 
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
    def Enum(self) -> int: 
        """
        None
        """
    def EnumText(self) -> str: 
        """
        None
        """
    def Field(self) -> StepData_Field: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
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
    def Kind(self) -> int: 
        """
        None
        """
    def Logical(self) -> StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        None
        """
    def ParamType(self) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the Kind of the SelectMember, under the form of an enum ParamType
        """
    def Real(self) -> float: 
        """
        None
        """
    def SetBoolean(self,val : bool) -> None: 
        """
        None
        """
    def SetEnum(self,val : int,text : str='') -> None: 
        """
        None
        """
    def SetEnumText(self,val : int,text : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it)
        """
    def SetInteger(self,val : int) -> None: 
        """
        None
        """
    def SetKind(self,kind : int) -> None: 
        """
        None
        """
    def SetLogical(self,val : StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        None
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def String(self) -> str: 
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
class StepData_SelectArrReal(StepData_SelectNamed, StepData_SelectMember, OCP.Standard.Standard_Transient):
    def ArrReal(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CField(self) -> StepData_Field: 
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
    def Enum(self) -> int: 
        """
        None
        """
    def EnumText(self) -> str: 
        """
        None
        """
    def Field(self) -> StepData_Field: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
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
    def Kind(self) -> int: 
        """
        None
        """
    def Logical(self) -> StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        None
        """
    def ParamType(self) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the Kind of the SelectMember, under the form of an enum ParamType
        """
    def Real(self) -> float: 
        """
        None
        """
    def SetArrReal(self,arr : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def SetBoolean(self,val : bool) -> None: 
        """
        None
        """
    def SetEnum(self,val : int,text : str='') -> None: 
        """
        None
        """
    def SetEnumText(self,val : int,text : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it)
        """
    def SetInteger(self,val : int) -> None: 
        """
        None
        """
    def SetKind(self,kind : int) -> None: 
        """
        None
        """
    def SetLogical(self,val : StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        None
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def String(self) -> str: 
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
class StepData_SelectReal(StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    A SelectReal is a SelectMember specialised for a basic real type in a select which also accepts entities : this one has NO NAME For a named select, see SelectNamedA SelectReal is a SelectMember specialised for a basic real type in a select which also accepts entities : this one has NO NAME For a named select, see SelectNamedA SelectReal is a SelectMember specialised for a basic real type in a select which also accepts entities : this one has NO NAME For a named select, see SelectNamed
    """
    def Boolean(self) -> bool: 
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
    def Enum(self) -> int: 
        """
        None
        """
    def EnumText(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        Tells if a SelectMember has a name. Default is False
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
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
    def Kind(self) -> int: 
        """
        None
        """
    def Logical(self) -> StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        Returns the name of a SelectMember. Default is empty
        """
    def ParamType(self) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the Kind of the SelectMember, under the form of an enum ParamType
        """
    def Real(self) -> float: 
        """
        None
        """
    def SetBoolean(self,val : bool) -> None: 
        """
        None
        """
    def SetEnum(self,val : int,text : str='') -> None: 
        """
        None
        """
    def SetEnumText(self,val : int,text : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it)
        """
    def SetInteger(self,val : int) -> None: 
        """
        None
        """
    def SetKind(self,kind : int) -> None: 
        """
        None
        """
    def SetLogical(self,val : StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        Sets the name of a SelectMember, returns True if done, False if no name is allowed Default does nothing and returns False
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def String(self) -> str: 
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
class StepData_SelectType():
    """
    SelectType is the basis used for SELECT_TYPE definitions from the EXPRESS form. A SELECT_TYPE in EXPRESS is an enumeration of Types, it corresponds in a way to a Super-Type, but with no specific Methods, and no exclusivity (a given Type can be member of several SELECT_TYPES, plus be itself a SUB_TYPE).
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes the Type of an Entity. Returns a positive Number which identifies the Type in the definition List of the SelectType. Returns Zero if its Type in not in this List.
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    pass
class StepData_Simple(StepData_Described, OCP.Standard.Standard_Transient):
    """
    A Simple Entity is defined by a type (which can heve super types) and a list of parametersA Simple Entity is defined by a type (which can heve super types) and a list of parametersA Simple Entity is defined by a type (which can heve super types) and a list of parameters
    """
    def As(self,steptype : str) -> StepData_Simple: 
        """
        Returns a Simple Entity which matches with a Type in <me> : For a Simple Entity : me if it matches, else a null handle For a Complex Entity : the member which matches, else null
        """
    def CField(self,name : str) -> StepData_Field: 
        """
        Returns a Field from its name; read or write
        """
    def CFieldNum(self,num : int) -> StepData_Field: 
        """
        Returns a field from its rank, in order to modify it
        """
    def CFields(self) -> StepData_FieldListN: 
        """
        Returns the entire field list, read or write
        """
    def Check(self,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Fills a Check by using its Description
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> StepData_EDescr: 
        """
        Returns the Description used to define this entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ESDescr(self) -> StepData_ESDescr: 
        """
        Returns description, as for simple
        """
    def Field(self,name : str) -> StepData_Field: 
        """
        Returns a Field from its name; read-only
        """
    def FieldNum(self,num : int) -> StepData_Field: 
        """
        Returns a field from its rank, for read-only use
        """
    def Fields(self) -> StepData_FieldListN: 
        """
        Returns the entire field list, read-only
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasField(self,name : str) -> bool: 
        """
        Tells if a Field brings a given name
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsComplex(self) -> bool: 
        """
        Returns False
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
    def Matches(self,steptype : str) -> bool: 
        """
        Tells if a step type is matched by <me> For a Simple Entity : own type or super type For a Complex Entity : one of the members
        """
    def NbFields(self) -> int: 
        """
        Returns the count of fields
        """
    def Shared(self,list : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills an EntityIterator with entities shared by <me>
        """
    def StepType(self) -> str: 
        """
        Returns the recorded StepType (TypeName of its ESDescr)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,descr : StepData_ESDescr) -> None: ...
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
class StepData_StepDumper():
    """
    Provides a way to dump entities processed through STEP, with these features : - same form as for writing a STEP File (because it is clear and compact enough, even if the names of the fields do not appear) : thus, no additionnal resource is required - possibility to look for an entity itself (only its Type or with its content), an entity and it shared items (one level) or all the entities its refers to, directly or recursively.
    """
    @overload
    def Dump(self,S : io.BytesIO,ent : OCP.Standard.Standard_Transient,level : int) -> bool: 
        """
        Dumps a Entity on an Messenger. Returns True if sucess, False, if the entity to dump has not been recognized by the Protocol. <level> can have one of these values : - 0 : prints the TYPE only, as known in STEP Files (StepType) If <ent> has not been regognized by the Protocol, or if its type is Complex, the StepType is replaced by the display of the cdl type. Complex Type are well processed by level 1. - 1 : dumps the entity, completely (whatever it has simple or complex type) but alone. - 2 : dumps the entity completely, plus the item its refers to at first level (a header message designates the starting entity of the dump) <Lists Shared and Implied> - 3 : dumps the entity and its refered items at any levels

        Works as Dump with a Transient, but directly takes the entity designated by its number in the Model Returns False, also if <num> is out of range
        """
    @overload
    def Dump(self,S : io.BytesIO,num : int,level : int) -> bool: ...
    def StepWriter(self) -> StepData_StepWriter: 
        """
        Gives an access to the tool which is used to work : this allow to acts on some parameters : Floating Format, Scopes ...
        """
    def __init__(self,amodel : StepData_StepModel,protocol : StepData_Protocol,mode : int=0) -> None: ...
    pass
class StepData_StepModel(OCP.Interface.Interface_InterfaceModel, OCP.Standard.Standard_Transient):
    """
    Gives access to - entities in a STEP file, - the STEP file header.Gives access to - entities in a STEP file, - the STEP file header.Gives access to - entities in a STEP file, - the STEP file header.
    """
    def AddEntity(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Internal method for adding an Entity. Used by file reading (defined by each Interface) and Transfer tools. It adds the entity required to be added, not its refs : see AddWithRefs. If <anentity> is a ReportEntity, it is added to the list of Reports, its Concerned Entity (Erroneous or Corrected, else Unknown) is added to the list of Entities. That is, the ReportEntity must be created before Adding
        """
    def AddHeaderEntity(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds an Entity to the Header
        """
    def AddReportEntity(self,rep : OCP.Interface.Interface_ReportEntity,semantic : bool=False) -> bool: 
        """
        Adds a ReportEntity as such. Returns False if the concerned entity is not recorded in the Model Else, adds it into, either the main report list or the list for semantic checks, then returns True
        """
    @overload
    def AddWithRefs(self,anent : OCP.Standard.Standard_Transient,proto : OCP.Interface.Interface_Protocol,level : int=0,listall : bool=False) -> None: 
        """
        Adds to the Model, an Entity with all its References, as they are defined by General Services FillShared and ListImplied. Process is recursive (any sub-levels) if <level> = 0 (Default) Else, adds sub-entities until the required sub-level. Especially, if <level> = 1, adds immediate subs and that's all

        Same as above, but works with the Protocol of the Model

        Same as above, but works with an already created GeneralLib
        """
    @overload
    def AddWithRefs(self,anent : OCP.Standard.Standard_Transient,level : int=0,listall : bool=False) -> None: ...
    @overload
    def AddWithRefs(self,anent : OCP.Standard.Standard_Transient,lib : OCP.Interface.Interface_GeneralLib,level : int=0,listall : bool=False) -> None: ...
    def CategoryNumber(self,num : int) -> int: 
        """
        Returns the recorded category number for a given entity number 0 if none was defined for this entity
        """
    def ChangeOrder(self,oldnum : int,newnum : int,count : int=1) -> None: 
        """
        Changes the Numbers of some Entities : <oldnum> is moved to <newnum>, same for <count> entities. Thus : 1,2 ... newnum-1 newnum ... oldnum .. oldnum+count oldnum+count+1 .. gives 1,2 ... newnum-1 oldnum .. oldnum+count newnum ... oldnum+count+1 (can be seen as a circular permutation)
        """
    def Check(self,num : int,syntactic : bool) -> OCP.Interface.Interface_Check: 
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
        Clears the Header
        """
    def ClearLabels(self) -> None: 
        """
        erases specific labels, i.e. clears the map (entity-ident)
        """
    def ClearReportEntity(self,num : int) -> bool: 
        """
        Removes the ReportEntity attached to Entity <num>. Returns True if done, False if no ReportEntity was attached to <num>. Warning : the caller must assume that this clearing is meaningfull
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
        Dumps the Header, with the Header Protocol of StepData. If the Header Protocol is not defined, for each Header Entity, prints its Type. Else sends the Header under the form of HEADER Section of an Ascii Step File <level> is not used because Header is not so big
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Entities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of all Entities, as an Iterator on Entities (the Entities themselves, not the Reports)
        """
    def Entity(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        returns entity given its rank. Same as InterfaceEntity, but with a shorter name
        """
    def EntityState(self,num : int) -> OCP.Interface.Interface_DataState: 
        """
        Returns the State of an entity, given its number
        """
    def FillIterator(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Allows an EntityIterator to get a list of Entities
        """
    def FillSemanticChecks(self,checks : OCP.Interface.Interface_CheckIterator,clear : bool=True) -> None: 
        """
        Fills the list of semantic checks. This list is computed (by CheckTool). Hence, it can be stored in the model for later queries <clear> True (D) : new list replaces <clear> False : new list is cumulated
        """
    def GTool(self) -> OCP.Interface.Interface_GTool: 
        """
        Returns the GTool, set by SetProtocol or by SetGTool
        """
    def GetFromAnother(self,other : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        gets header from another Model (uses Header Protocol)
        """
    def GetFromTransfer(self,aniter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Gets contents from an EntityIterator, prepared by a Transfer tool (e.g TransferCopy). Starts from clear
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlobalCheck(self,syntactic : bool=True) -> OCP.Interface.Interface_Check: 
        """
        Returns the GlobalCheck, which memorizes messages global to the file (not specific to an Entity), especially Header
        """
    def HasHeaderEntity(self,atype : OCP.Standard.Standard_Type) -> bool: 
        """
        says if a Header entity has a specifed type
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
    def Header(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        returns Header entities under the form of an iterator
        """
    def HeaderEntity(self,atype : OCP.Standard.Standard_Type) -> OCP.Standard.Standard_Transient: 
        """
        Returns Header entity with specified type, if there is
        """
    def IdentLabel(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        returns the label ident attached to an entity, 0 if not in me
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
    def NewEmptyModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns a New Empty Model, same type as <me>, i.e. StepModel
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
        Prints label specific to STEP norm for a given entity, i.e. if a LabelIdent has been recorded, its value with '#', else the number in the model with '#' and between ()
        """
    def PrintToLog(self,ent : OCP.Standard.Standard_Transient,S : io.BytesIO) -> None: 
        """
        Prints label specific to each norm in log format, for a given entity. By default, just calls PrintLabel, can be redefined
        """
    def Protocol(self) -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Protocol which has been set by SetProtocol, or AddWithRefs with Protocol
        """
    def Redefineds(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of ReportEntities which redefine data (generally, if concerned entity is "Error", a literal content is added to it : this is a "redefined entity"
        """
    def ReplaceEntity(self,nument : int,anent : OCP.Standard.Standard_Transient) -> None: 
        """
        Replace Entity with Number=nument on other entity - "anent"
        """
    def ReportEntity(self,num : int,semantic : bool=False) -> OCP.Interface.Interface_ReportEntity: 
        """
        Returns a ReportEntity identified by its number in the Model, or a Null Handle If <num> does not identify a ReportEntity.
        """
    def Reports(self,semantic : bool=False) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of all ReportEntities, i.e. data about Entities read with Error or Warning informations (each item has to be casted to Report Entity then it can be queried for Concerned Entity, Content, Check ...) By default, returns the main reports, is <semantic> is True it returns the list for sematic checks
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
    def SetGTool(self,gtool : OCP.Interface.Interface_GTool) -> None: 
        """
        Sets a GTool for this model, which already defines a Protocol
        """
    def SetGlobalCheck(self,ach : OCP.Interface.Interface_Check) -> None: 
        """
        Allows to modify GlobalCheck, after getting then completing it Remark : it is SYNTACTIC check. Semantics, see FillChecks
        """
    def SetIdentLabel(self,ent : OCP.Standard.Standard_Transient,ident : int) -> None: 
        """
        Attaches an ident to an entity to produce a label (does nothing if <ent> is not in <me>)
        """
    def SetProtocol(self,proto : OCP.Interface.Interface_Protocol) -> None: 
        """
        Sets a Protocol for this Model It is also set by a call to AddWithRefs with Protocol It is used for : DumpHeader (as required), ClearEntities ...
        """
    def SetReportEntity(self,num : int,rep : OCP.Interface.Interface_ReportEntity) -> bool: 
        """
        Sets or Replaces a ReportEntity for the Entity <num>. Returns True if Report is replaced, False if it has been replaced Warning : the caller must assume that this setting is meaningfull
        """
    def SetSourceCodePage(self,theCode : OCP.Resource.Resource_FormatType) -> None: 
        """
        Return the encoding of STEP file for converting names into UNICODE.
        """
    @staticmethod
    def SetTemplate_s(name : str,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Records a new template model with a name. If the name was already recorded, the corresponding template is replaced by the new one. Then, WARNING : test HasTemplate to avoid surprises
        """
    def SourceCodePage(self) -> OCP.Resource.Resource_FormatType: 
        """
        Return the encoding of STEP file for converting names into UNICODE. Initialized from "read.step.codepage" variable by constructor, which is Resource_UTF8 by default.
        """
    def StringLabel(self,ent : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a string with the label attached to a given entity, same form as for PrintLabel
        """
    @staticmethod
    def Template_s(name : str) -> OCP.Interface.Interface_InterfaceModel: 
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
    def VerifyCheck(self,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Specific Check, checks Header Items with HeaderProtocol
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
class StepData_StepReaderData(OCP.Interface.Interface_FileReaderData, OCP.Standard.Standard_Transient):
    """
    Specific FileReaderData for Step Contains litteral description of entities (for each one : type as a string, ident, parameter list) provides references evaluation, plus access to litteral data and specific access methods (Boolean, XY, XYZ)Specific FileReaderData for Step Contains litteral description of entities (for each one : type as a string, ident, parameter list) provides references evaluation, plus access to litteral data and specific access methods (Boolean, XY, XYZ)Specific FileReaderData for Step Contains litteral description of entities (for each one : type as a string, ident, parameter list) provides references evaluation, plus access to litteral data and specific access methods (Boolean, XY, XYZ)
    """
    @overload
    def AddParam(self,num : int,FP : OCP.Interface.Interface_FileParameter) -> None: 
        """
        Adds a parameter to record no "num" and fills its fields (EntityNumber is optional) Warning : <aval> is assumed to be memory-managed elsewhere : it is NOT copied. This gives a best speed : strings remain stored in pages of characters

        Same as above, but gets a AsciiString from TCollection Remark that the content of the AsciiString is locally copied (because its content is most often lost after using)

        Same as above, but gets a complete FileParameter Warning : Content of <FP> is NOT copied : its original address and space in memory are assumed to be managed elsewhere (see ParamSet)
        """
    @overload
    def AddParam(self,num : int,aval : OCP.TCollection.TCollection_AsciiString,atype : OCP.Interface.Interface_ParamType,nument : int=0) -> None: ...
    @overload
    def AddParam(self,num : int,aval : str,atype : OCP.Interface.Interface_ParamType,nument : int=0) -> None: ...
    def AddStepParam(self,num : int,aval : str,atype : OCP.Interface.Interface_ParamType,nument : int=0) -> None: 
        """
        Fills the fields of a parameter of a record. This is a variant of AddParam, Adapted to STEP (optimized for specific values)
        """
    def BindEntity(self,num : int,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Binds an entity to a record
        """
    def BoundEntity(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the entity bound to a record, set by SetEntities
        """
    def CType(self,num : int) -> str: 
        """
        Returns Record Type as a CString was C++ : return const
        """
    def ChangeParam(self,num : int,nump : int) -> OCP.Interface.Interface_FileParameter: 
        """
        Same as above, but in order to be modified on place
        """
    def CheckDerived(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,errstat : bool=False) -> bool: 
        """
        Checks if parameter <nump> of record <num> is given as Derived If this Check is successful (i.e. Param = "*"), returns True Else, fills <ach> with a Message which contains <mess> and returns False. According to <errstat>, this message is Warning if errstat is False (Default), Fail if errstat is True
        """
    def CheckNbParams(self,num : int,nbreq : int,ach : OCP.Interface.Interface_Check,mess : str='') -> bool: 
        """
        Checks Count of Parameters of record <num> to equate <nbreq> If this Check is successful, returns True Else, fills <ach> with an Error Message then returns False <mess> is included in the Error message if given non empty
        """
    def ComplexType(self,num : int,types : OCP.TColStd.TColStd_SequenceOfAsciiString) -> None: 
        """
        Returns the List of Types which correspond to a Complex Type Entity. If not Complex, there is just one Type in it For a SubList or a Scope mark, <types> remains empty
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
    def FailEnumValue(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Fills a check with a fail message if enumeration value does match parameter definition Just a help to centralize message definitions
        """
    @staticmethod
    def Fastof_s(str : str) -> float: 
        """
        Same spec.s as standard <atof> but 5 times faster
        """
    def FindNextHeaderRecord(self,num : int) -> int: 
        """
        determine first suitable record of Header works as FindNextRecord, but treats only Header records
        """
    def FindNextRecord(self,num : int) -> int: 
        """
        determines the first suitable record following a given one that is, skips SCOPE,ENDSCOPE and SUBLIST records Note : skips Header records, which are accessed separately
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlobalCheck(self) -> OCP.Interface.Interface_Check: 
        """
        Returns the Global Check. It can record Fail messages about Undefined References (detected by SetEntityNumbers)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitParams(self,num : int) -> None: 
        """
        attaches an empty ParamList to a Record
        """
    def IsComplex(self,num : int) -> bool: 
        """
        Returns True if <num> corresponds to a Complex Type Entity (as can be defined by ANDOR Express clause)
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
    @overload
    def NamedForComplex(self,theName : str,theShortName : str,num0 : int,num : int,ach : OCP.Interface.Interface_Check) -> bool: 
        """
        Determines the first component which brings a given name, for a Complex Type Entity <num0> is the very first record of this entity <num> is given the last NextNamedForComplex, starts at zero it is returned as the newly found number Hence, in the normal case, NextNamedForComplex starts by num0 if <num> is zero, else by NextForComplex(num) If the alphabetic order is not respected, it restarts from num0 and loops on NextForComplex until finding <name> In case of "non-alphabetic order", <ach> is filled with a Warning for this name In case of "not-found at all", <ach> is filled with a Fail, and <num> is returned as zero

        Determines the first component which brings a given name, or short name for a Complex Type Entity <num0> is the very first record of this entity <num> is given the last NextNamedForComplex, starts at zero it is returned as the newly found number Hence, in the normal case, NextNamedForComplex starts by num0 if <num> is zero, else by NextForComplex(num) If the alphabetic order is not respected, it restarts from num0 and loops on NextForComplex until finding <name> In case of "non-alphabetic order", <ach> is filled with a Warning for this name In case of "not-found at all", <ach> is filled with a Fail, and <num> is returned as zero
        """
    @overload
    def NamedForComplex(self,name : str,num0 : int,num : int,ach : OCP.Interface.Interface_Check) -> bool: ...
    def NbEntities(self) -> int: 
        """
        Returns total count of Entities (including Header)
        """
    def NbParams(self,num : int) -> int: 
        """
        Returns count of parameters attached to record "num" If <num> = 0, returns the total recorded count of parameters
        """
    def NbRecords(self) -> int: 
        """
        Returns the count of registered records That is, value given for Initialization (can be redefined)
        """
    def NextForComplex(self,num : int) -> int: 
        """
        Returns the Next "Componant" for a Complex Type Entity, of which <num> is already a Componant (the first one or a next one) Returns 0 for a Simple Type or for the last Componant
        """
    def Param(self,num : int,nump : int) -> OCP.Interface.Interface_FileParameter: 
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
        Returns the absolute rank of the beginning of a record (its lsit is from ParamFirstRank+1 to ParamFirstRank+NbParams)
        """
    def ParamNumber(self,num : int,nump : int) -> int: 
        """
        Returns record number of an entity referenced by a parameter of type Ident; 0 if no EntityNumber has been determined Note that it is used to reference Entities but also Sublists (sublists are not objects, but internal descriptions)
        """
    def ParamType(self,num : int,nump : int) -> OCP.Interface.Interface_ParamType: 
        """
        Returns type of parameter "nump" of record "num" Returns literal value of parameter "nump" of record "num" was C++ : return const &
        """
    def Params(self,num : int) -> OCP.Interface.Interface_ParamList: 
        """
        Returns the complete ParamList of a record (read only) num = 0 to return the whole param list for the file
        """
    def PrepareHeader(self) -> None: 
        """
        Works as SetEntityNumbers but for Header : more simple because there are no Reference, only Sub-Lists
        """
    def ReadAny(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,descr : StepData_PDescr,val : OCP.Standard.Standard_Transient) -> bool: 
        """
        Reads parameter <nump> of record <num> into a Transient Value according to the type of the parameter : Named for Integer,Boolean,Logical,Enum,Real : SelectNamed Immediate Integer,Boolean,Logical,Enum,Real : SelectInt/Real Text : HAsciiString Ident : the referenced Entity Sub-List not processed, see ReadSub This value is controlled by a Parameter Descriptor (PDescr), which controls its allowed type and value <ach> is filled if the read parameter does not match its description (the select is nevertheless created if possible)
        """
    def ReadBoolean(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,flag : bool) -> bool: 
        """
        reads parameter <nump> of record <num> as a Boolean Return value and Check managed as by ReadReal (demands a Boolean enum, i.e. text ".T." for True or ".F." for False)
        """
    @overload
    def ReadEntity(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,sel : StepData_SelectType) -> bool: 
        """
        Reads parameter <nump> of record <num> as a single Entity. Return value and Check managed as by ReadReal (demands a reference to an Entity). In Addition, demands read Entity to be Kind of a required Type <atype>. Remark that returned status is False and <ent> is Null if parameter is not an Entity, <ent> remains Not Null is parameter is an Entity but is not Kind of required type

        Same as above, but a SelectType checks Type Matching, and records the read Entity (see method Value from SelectType)
        """
    @overload
    def ReadEntity(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,atype : OCP.Standard.Standard_Type,ent : OCP.Standard.Standard_Transient) -> bool: ...
    def ReadEnum(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,enumtool : StepData_EnumTool,val : int) -> bool: 
        """
        Reads parameter <nump> of record <num> as an Enumeration (text between dots) and converts it to an integer value, by an EnumTool. Returns True if OK, false if : this parameter is not enumeration, or is not recognized by the EnumTool (with fail)
        """
    def ReadField(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,descr : StepData_PDescr,fild : StepData_Field) -> bool: 
        """
        reads parameter <nump> of record <num> into a Field, controlled by a Parameter Descriptor (PDescr), which controls its allowed type(s) and value <ach> is filled if the read parameter does not match its description (but the field is read anyway) If the description is not defined, no control is done Returns True when done
        """
    def ReadInteger(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,val : int) -> bool: 
        """
        reads parameter <nump> of record <num> as a single Integer. Return value & Check managed as by ReadXY (demands an Integer)
        """
    def ReadList(self,num : int,ach : OCP.Interface.Interface_Check,descr : StepData_ESDescr,list : StepData_FieldList) -> bool: 
        """
        reads a list of fields controlled by an ESDescr
        """
    def ReadLogical(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,flag : StepData_Logical) -> bool: 
        """
        reads parameter <nump> of record <num> as a Logical Return value and Check managed as by ReadBoolean (demands a Logical enum, i.e. text ".T.", ".F.", or ".U.")
        """
    def ReadMember(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,val : StepData_SelectMember) -> bool: 
        """
        Reads parameter <nump> of record <num> into a SelectMember, self-sufficient (no Description needed) If <val> is already created, it will be filled, as possible And if reading does not match its own description, the result will be False If <val> is not it not yet created, it will be (SelectNamed) Usefull if a field is defined as a SelectMember, directly (SELECT with no Entity as member) But SelectType also manages SelectMember (for SELECT with some members as Entity, some other not)
        """
    def ReadReal(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,val : float) -> bool: 
        """
        reads parameter <nump> of record <num> as a single Real value. Return value and Check managed as by ReadXY (demands a Real)
        """
    def ReadString(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,val : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        reads parameter <nump> of record <num> as a String (text between quotes, quotes are removed by the Read operation) Return value and Check managed as by ReadXY (demands a String)
        """
    def ReadSub(self,numsub : int,mess : str,ach : OCP.Interface.Interface_Check,descr : StepData_PDescr,val : OCP.Standard.Standard_Transient) -> int: 
        """
        reads the content of a sub-list into a transient : SelectNamed, or HArray1 of Integer,Real,String,Transient ... recursive call if list of list ... If a sub-list has mixed types, an HArray1OfTransient is produced, it may contain SelectMember Intended to be called by ReadField The returned status is : negative if failed, 0 if empty. Else the kind to be recorded in the field
        """
    def ReadSubList(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,numsub : int,optional : bool=False,lenmin : int=0,lenmax : int=0) -> bool: 
        """
        reads parameter <nump> of record <num> as a sub-list (may be typed, see ReadTypedParameter in this case) Returns True if OK. Else (not a LIST), returns false and feeds Check with appropriate check If <optional> is True and Param is not defined, returns True with <ach> not filled and <numsub> returned as 0 Works with SubListNumber with <aslast> false (no specific case for last parameter)
        """
    def ReadTypedParam(self,num : int,nump : int,mustbetyped : bool,mess : str,ach : OCP.Interface.Interface_Check,numr : int,numrp : int,typ : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Resolves a parameter which can be enclosed in a type def., as TYPE(val). The parameter must then be read normally according its type. Parameter to be resolved is <nump> of record <num> <mustbetyped> True demands a typed parameter <mustbetyped> False accepts a non-typed parameter as option mess and ach as usual <numr>,<numrp> are the resolved record and parameter numbers = num,nump if no type, else numrp=1 <typ> returns the recorded type, or empty string Remark : a non-typed list is considered as "non-typed"
        """
    def ReadXY(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,X : float,Y : float) -> bool: 
        """
        reads parameter <nump> of record <num> as a sub-list of two Reals X,Y. Returns True if OK. Else, returns false and feeds Check with appropriate Fails (parameter not a sub-list, not two Reals in the sub-list) composed with "mess" which gives the name of the parameter
        """
    def ReadXYZ(self,num : int,nump : int,mess : str,ach : OCP.Interface.Interface_Check,X : float,Y : float,Z : float) -> bool: 
        """
        reads parameter <nump> of record <num> as a sub-list of three Reals X,Y,Z. Return value and Check managed as by ReadXY (demands a sub-list of three Reals)
        """
    def RecordIdent(self,num : int) -> int: 
        """
        Returns record identifier (Positive number) If returned ident is not positive : Sub-List or Scope mark
        """
    def RecordType(self,num : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns Record Type
        """
    def ResetErrorLoad(self) -> bool: 
        """
        Returns the former value of status "Error Load" then resets it Used to read the status then ensure it is reset
        """
    def SetEntityNumbers(self,withmap : bool=True) -> None: 
        """
        determines reference numbers in EntityNumber fields called by Prepare from StepReaderTool to prepare later using by a StepModel. This method is attached to StepReaderData because it needs a massive amount of data accesses to work
        """
    def SetErrorLoad(self,val : bool) -> None: 
        """
        Sets the status "Error Load" on, to overside check fails <val> True : declares unloaded <val> False : declares loaded If not called before loading (see FileReaderTool), check fails give the status IsErrorLoad says if SetErrorLoad has been called by user ResetErrorLoad resets it (called by FileReaderTool) This allows to specify that the currently loaded entity remains unloaded (because of syntactic fail)
        """
    def SetParam(self,num : int,nump : int,FP : OCP.Interface.Interface_FileParameter) -> None: 
        """
        Sets a new value for a parameter of a record, given by : num : record number; nump : parameter number in the record
        """
    def SetRecord(self,num : int,ident : str,type : str,nbpar : int) -> None: 
        """
        Fills the fields of a record
        """
    def SubListNumber(self,num : int,nump : int,aslast : bool) -> int: 
        """
        Returns SubList numero designated by a parameter (nump) in a record (num), or zero if the parameter does not exist or is not a SubList address. Zero too If aslast is True and nump is not for the last parameter
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,nbheader : int,nbtotal : int,nbpar : int,theSourceCodePage : OCP.Resource.Resource_FormatType=Resource_FormatType.Resource_FormatType_UTF8) -> None: ...
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
class StepData_StepReaderTool(OCP.Interface.Interface_FileReaderTool):
    """
    Specific FileReaderTool for Step; works with FileReaderData provides references evaluation, plus access to litteral data and specific methods defined by FileReaderTool Remarks : works with a ReaderLib to load Entities
    """
    def AnalyseRecord(self,num : int,anent : OCP.Standard.Standard_Transient,acheck : OCP.Interface.Interface_Check) -> bool: 
        """
        fills an entity, given record no; works by using a ReaderLib to load each entity, which must be a Transient Actually, returned value is True if no fail, False else
        """
    def BeginRead(self,amodel : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        fills model's header; that is, gives to it Header entities and commands their loading. Also fills StepModel's Global Check from StepReaderData's GlobalCheck
        """
    def Clear(self) -> None: 
        """
        Clear filelds
        """
    def Data(self) -> OCP.Interface.Interface_FileReaderData: 
        """
        Returns the FileReaderData which is used to work
        """
    def EndRead(self,amodel : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        Ends file reading after reading all the entities Here, it binds in the model, Idents to Entities (for checks)
        """
    def ErrorHandle(self) -> bool: 
        """
        Returns ErrorHandle flag
        """
    def LoadModel(self,amodel : OCP.Interface.Interface_InterfaceModel) -> None: 
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
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the stored Model
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Creates an empty Model of the norm. Uses Protocol to do it
        """
    @overload
    def Prepare(self,reco : StepData_FileRecognizer,optimize : bool=True) -> None: 
        """
        Bounds empty entities to records, uses default Recognition provided by ReaderLib and ReaderModule. Also calls computation of references (SetEntityNumbers from StepReaderData) Works only on data entities (skips header) <optimize> given False allows to test some internal algorithms which are normally avoided (see also StepReaderData)

        Bounds empty entities to records, works with a specific FileRecognizer, stored and later used in Recognize Works only on data entities (skips header) <optimize : same as above
        """
    @overload
    def Prepare(self,optimize : bool=True) -> None: ...
    def PrepareHeader(self,reco : StepData_FileRecognizer) -> None: 
        """
        bounds empty entities and sub-lists to header records works like Prepare + SetEntityNumbers, but for header (N.B.: in Header, no Ident and no reference) FileRecognizer is to specify Entities which are allowed to be defined in the Header (not every type can be)
        """
    def Protocol(self) -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Protocol given at creation time
        """
    def Recognize(self,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        recognizes records, by asking either ReaderLib (default) or FileRecognizer (if defined) to do so. <ach> is to call RecognizeByLib
        """
    def RecognizeByLib(self,num : int,glib : OCP.Interface.Interface_GeneralLib,rlib : OCP.Interface.Interface_ReaderLib,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Recognizes a record with the help of Libraries. Can be used to implement the method Recognize. <rlib> is used to find Protocol and CaseNumber to apply <glib> performs the creation (by service NewVoid, or NewRead if NewVoid gave no result) <ach> is a check, which is transmitted to NewRead if it is called, gives a result but which is false <ent> is the result Returns False if recognition has failed, True else
        """
    def SetData(self,reader : OCP.Interface.Interface_FileReaderData,protocol : OCP.Interface.Interface_Protocol) -> None: 
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
    def SetModel(self,amodel : OCP.Interface.Interface_InterfaceModel) -> None: 
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
    def __init__(self,reader : StepData_StepReaderData,protocol : StepData_Protocol) -> None: ...
    pass
class StepData_StepWriter():
    """
    manages atomic file writing, under control of StepModel (for general organisation of file) and each class of Transient (for its own parameters) : prepares text to be written then writes it A stream cannot be used because Step limits line length at 72 In more, a specific object offers more appropriate functions
    """
    def AddParam(self) -> None: 
        """
        prepares adding a parameter (that is, adds ',' except for first one); normally for internal use; can be used to send a totally empty parameter (with no litteral value)
        """
    def CheckList(self) -> OCP.Interface.Interface_CheckIterator: 
        """
        Returns the check-list, which has received possible checks : for unknown entities, badly loaded ones, null or unknown references
        """
    def CloseSub(self) -> None: 
        """
        closes a sublist by a ')'
        """
    def Comment(self,mode : bool) -> None: 
        """
        sets a comment mark : if mode is True, begins Comment zone, if mode is False, ends Comment zone (if one is begun)
        """
    def EndComplex(self) -> None: 
        """
        sends the end of a complex entity : a simple closed bracket It must be called AFTER sending all the componants and BEFORE the final call to EndEntity
        """
    def EndEntity(self) -> None: 
        """
        sends end of entity (closing bracket plus ';') Error if count of opened-closed brackets is not null
        """
    def EndFile(self) -> None: 
        """
        sets end of file; error is EndSec was not set
        """
    def EndSec(self) -> None: 
        """
        sets end of section; to be done before passing to next one
        """
    def FloatWriter(self) -> OCP.Interface.Interface_FloatWriter: 
        """
        Returns the embedded FloatWriter, which controls sending Reals Use this method to access FloatWriter in order to consult or change its options (MainFormat, FormatForRange,ZeroSuppress), because it is returned as the address of its field
        """
    def Indent(self,onent : bool) -> None: 
        """
        asks that further indentations will begin at position of entity first opening bracket; else they begin at zero (def) for each sublist level, two more blancks are added at beginning (except for text continuation, which must begin at true zero)
        """
    def IsInScope(self,num : int) -> bool: 
        """
        Returns True if an Entity identified by its Number is in a Scope
        """
    def JoinLast(self,newline : bool) -> None: 
        """
        joins current line to last one, only if new length is 72 max if newline is True, a new current line begins; else, current line is set to the last line (once joined) itself an can be completed
        """
    def Line(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a Line given its rank in the File
        """
    def NbLines(self) -> int: 
        """
        Returns count of Lines
        """
    def NewLine(self,evenempty : bool) -> None: 
        """
        flushes current line; if empty, flushes it (defines a new empty line) if evenempty is True; else, skips it
        """
    def OpenSub(self) -> None: 
        """
        open a sublist by a '('
        """
    def OpenTypedSub(self,subtype : str) -> None: 
        """
        open a sublist with its type then a '('
        """
    def Print(self,S : io.BytesIO) -> bool: 
        """
        writes result on an output defined as an OStream then clears it
        """
    @overload
    def Send(self,val : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        sends an integer parameter

        sends a real parameter (wroks with FloatWriter)

        sends a text given as string (it will be set between '...')

        sends a reference to an entity (its identifier with '#') REMARK 1 : a Null <val> is interpreted as "Undefined" REMARK 2 : for an HAsciiString which is not recorded in the Model, it is send as its String Content, between quotes
        """
    @overload
    def Send(self,val : int) -> None: ...
    @overload
    def Send(self,val : OCP.Standard.Standard_Transient) -> None: ...
    @overload
    def Send(self,val : float) -> None: ...
    def SendArrReal(self,anArr : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        sends an array of real
        """
    def SendBoolean(self,val : bool) -> None: 
        """
        sends a Boolean as .T. for True or .F. for False (it is an useful case of Enum, which is built-in)
        """
    @overload
    def SendComment(self,text : str) -> None: 
        """
        sends a comment. Error if we are not inside a comment zone

        same as above but accepts a CString (ex.: "..." directly)
        """
    @overload
    def SendComment(self,text : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def SendData(self) -> None: 
        """
        Begins data section; error if EndSec was not set
        """
    def SendDerived(self) -> None: 
        """
        sends a "Derived" parameter (by '*'). A Derived Parameter has been inherited from a Super-Type then redefined as being computed by a function. Hence its value in file is senseless.
        """
    def SendEndscope(self) -> None: 
        """
        sets an end of Scope (on a separate line)
        """
    def SendEntity(self,nument : int,lib : StepData_WriterLib) -> None: 
        """
        Send an Entity of the Data Section. If it corresponds to a Scope, also Sends the Scope informations and contained Items
        """
    @overload
    def SendEnum(self,val : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        sends an enum given by String (litteral expression) adds '.' around it if not done Remark : val can be computed by class EnumTool from StepData: StepWriter.SendEnum (myenum.Text(enumval));

        sends an enum given by String (litteral expression) adds '.' around it if not done
        """
    @overload
    def SendEnum(self,val : str) -> None: ...
    def SendField(self,fild : StepData_Field,descr : StepData_PDescr) -> None: 
        """
        Sends the content of a field, controlled by its descriptor If the descriptor is not defined, follows the description detained by the field itself
        """
    def SendHeader(self) -> None: 
        """
        Begins model header
        """
    def SendIdent(self,ident : int) -> None: 
        """
        begins an entity with an ident plus '=' (at beginning of line) entity ident is its Number given by the containing Model Warning : <ident> must be, either Number or Label, according LabelMode
        """
    def SendList(self,list : StepData_FieldList,descr : StepData_ESDescr) -> None: 
        """
        Send the content of an entity as being a FieldList controlled by its descriptor. This includes start and end brackets but not the entity type
        """
    def SendLogical(self,val : StepData_Logical) -> None: 
        """
        sends a Logical as .T. or .F. or .U. according its Value (it is a standard case of Enum for Step, and is built-in)
        """
    def SendModel(self,protocol : StepData_Protocol,headeronly : bool=False) -> None: 
        """
        Sends the complete Model, included HEADER and DATA Sections Works with a WriterLib defined through a Protocol If <headeronly> is given True, only the HEADER Section is sent (used to Dump the Header of a StepModel)
        """
    def SendScope(self) -> None: 
        """
        sets a begin of Scope (ends this line)
        """
    def SendSelect(self,sm : StepData_SelectMember,descr : StepData_PDescr) -> None: 
        """
        Sends a SelectMember, which cab be named or not
        """
    @overload
    def SendString(self,val : str) -> None: 
        """
        sends a string exactly as it is given

        sends a string exactly as it is given
        """
    @overload
    def SendString(self,val : OCP.TCollection.TCollection_AsciiString) -> None: ...
    def SendUndef(self) -> None: 
        """
        sends an undefined (optionnal absent) parameter (by '$')
        """
    def SetScope(self,numscope : int,numin : int) -> None: 
        """
        Declares the Entity Number <numscope> to correspond to a Scope which contains the Entity Number <numin>. Several calls to the same <numscope> add Entities in this Scope, in this order. Error if <numin> is already declared in the Scope Warning : the declaration of the Scopes is assumed to be consistent, i.e. <numin> is not referenced from outside this Scope (not checked here)
        """
    def StartComplex(self) -> None: 
        """
        sends the start of a complex entity, which is a simple open bracket (without increasing braket level) It must be called JUST AFTER SendEntity and BEFORE sending componants, each one begins by StartEntity
        """
    def StartEntity(self,atype : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        sets entity's StepType, opens brakets, starts param no to 0 params are separated by comma Remark : for a Multiple Type Entity (see Express ANDOR clause) StartComplex must be called before sending componants, then each "Componant" must be send separately (one call to StartEntity for each one) : the Type which preceeds is then automaticaly closed. Once all the componants have been sent, EndComplex must be called, then and only then EndEntity
        """
    def __init__(self,amodel : StepData_StepModel) -> None: ...
    @property
    def LabelMode(self) -> int:
        """
        ModeLabel controls how to display entity ids : 0 (D) gives entity number in the model 1 gives the already recorded label (else, its number) Warning : conflicts are not controlled

        :type: int
        """
    @LabelMode.setter
    def LabelMode(self, arg1: int) -> None:
        """
        ModeLabel controls how to display entity ids : 0 (D) gives entity number in the model 1 gives the already recorded label (else, its number) Warning : conflicts are not controlled
        """
    @property
    def TypeMode(self) -> int:
        """
        TypeMode controls the type form to use : 0 (D) for normal long form 1 for short form (if a type name has no short form, normal long form is then used)

        :type: int
        """
    @TypeMode.setter
    def TypeMode(self, arg1: int) -> None:
        """
        TypeMode controls the type form to use : 0 (D) for normal long form 1 for short form (if a type name has no short form, normal long form is then used)
        """
    pass
class StepData_UndefinedEntity(OCP.Standard.Standard_Transient):
    """
    Undefined entity specific to Step Interface, in which StepType is defined at each instance, or is a SubList of another one Uses an UndefinedContent, that from Interface is suitable. Also an Entity defined by STEP can be "Complex Type" (see ANDOR clause in Express).Undefined entity specific to Step Interface, in which StepType is defined at each instance, or is a SubList of another one Uses an UndefinedContent, that from Interface is suitable. Also an Entity defined by STEP can be "Complex Type" (see ANDOR clause in Express).Undefined entity specific to Step Interface, in which StepType is defined at each instance, or is a SubList of another one Uses an UndefinedContent, that from Interface is suitable. Also an Entity defined by STEP can be "Complex Type" (see ANDOR clause in Express).
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
    def FillShared(self,list : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills the list of shared entities
        """
    def GetFromAnother(self,other : StepData_UndefinedEntity,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        reads another UndefinedEntity from StepData
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsComplex(self) -> bool: 
        """
        Returns True if <me> defines a Multiple Type Entity (see ANDOR)
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
    def IsSub(self) -> bool: 
        """
        Returns True if an Unndefined Entity is SubPart of another one
        """
    def Next(self) -> StepData_UndefinedEntity: 
        """
        For a Multiple Type Entity, returns the Next "Componant" For more than two Types, iterative definition (Next->Next...) Returns a Null Handle for the end of the List
        """
    def ReadRecord(self,SR : StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        reads data from StepReaderData (i.e. from file), by filling StepType and parameters stored in the UndefinedContent
        """
    def StepType(self) -> str: 
        """
        gives entity type, read from file For a Complex Type Entity, gives the first Type read, each "Next" gives its "partial" type was C++ : return const
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UndefinedContent(self) -> OCP.Interface.Interface_UndefinedContent: 
        """
        Returns the UndefinedContent which brings the Parameters
        """
    def WriteParams(self,SW : StepData_StepWriter) -> None: 
        """
        write data to StepWriter, taken from UndefinedContent
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,issub : bool) -> None: ...
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
class StepData_WriterLib():
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
    def Module(self) -> StepData_ReadWriteModule: 
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
    def Protocol(self) -> StepData_Protocol: 
        """
        Returns the current Protocol in the Iteration
        """
    def Select(self,obj : OCP.Standard.Standard_Transient,module : StepData_ReadWriteModule,CN : int) -> bool: 
        """
        Selects a Module from the Library, given an Object. Returns True if Select has succeeded, False else. Also Returns (as arguments) the selected Module and the Case Number determined by the associated Protocol. If Select has failed, <module> is Null Handle and CN is zero. (Select can work on any criterium, such as Object DynamicType)
        """
    def SetComplete(self) -> None: 
        """
        Sets a library to be defined with the complete Global list (all the couples Protocol/Modules recorded in it)
        """
    @staticmethod
    def SetGlobal_s(amodule : StepData_ReadWriteModule,aprotocol : StepData_Protocol) -> None: 
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
    def __init__(self,aprotocol : StepData_Protocol) -> None: ...
    pass
StepData_LFalse: OCP.StepData.StepData_Logical # value = <StepData_Logical.StepData_LFalse: 0>
StepData_LTrue: OCP.StepData.StepData_Logical # value = <StepData_Logical.StepData_LTrue: 1>
StepData_LUnknown: OCP.StepData.StepData_Logical # value = <StepData_Logical.StepData_LUnknown: 2>
