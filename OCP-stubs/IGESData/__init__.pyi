import OCP.IGESData
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.Standard
import OCP.gp
import OCP.Message
import OCP.TColStd
import OCP.Interface
__all__  = [
"IGESData",
"IGESData_Array1OfDirPart",
"IGESData_Array1OfIGESEntity",
"IGESData_BasicEditor",
"IGESData_IGESEntity",
"IGESData_DefList",
"IGESData_DefSwitch",
"IGESData_DefType",
"IGESData_GeneralModule",
"IGESData_SpecificModule",
"IGESData_DirChecker",
"IGESData_DirPart",
"IGESData_Protocol",
"IGESData_FileRecognizer",
"IGESData_UndefinedEntity",
"IGESData_DefaultGeneral",
"IGESData_GlobalNodeOfSpecificLib",
"IGESData_GlobalNodeOfWriterLib",
"IGESData_GlobalSection",
"IGESData_HArray1OfIGESEntity",
"IGESData_IGESDumper",
"IGESData_ColorEntity",
"IGESData_IGESModel",
"IGESData_IGESReaderData",
"IGESData_IGESReaderTool",
"IGESData_IGESType",
"IGESData_IGESWriter",
"IGESData_LabelDisplayEntity",
"IGESData_LevelListEntity",
"IGESData_LineFontEntity",
"IGESData_NameEntity",
"IGESData_NodeOfSpecificLib",
"IGESData_NodeOfWriterLib",
"IGESData_ParamCursor",
"IGESData_ParamReader",
"IGESData_FileProtocol",
"IGESData_ReadStage",
"IGESData_ReadWriteModule",
"IGESData_SingleParentEntity",
"IGESData_SpecificLib",
"IGESData_DefaultSpecific",
"IGESData_Status",
"IGESData_ToolLocation",
"IGESData_TransfEntity",
"IGESData_FreeFormatEntity",
"IGESData_ViewKindEntity",
"IGESData_WriterLib",
"IGESData_DefAny",
"IGESData_DefNone",
"IGESData_DefOne",
"IGESData_DefReference",
"IGESData_DefSeveral",
"IGESData_DefValue",
"IGESData_DefVoid",
"IGESData_EntityError",
"IGESData_EntityOK",
"IGESData_ErrorOne",
"IGESData_ErrorRef",
"IGESData_ErrorSeveral",
"IGESData_ErrorVal",
"IGESData_ReadAssocs",
"IGESData_ReadDir",
"IGESData_ReadEnd",
"IGESData_ReadOwn",
"IGESData_ReadProps",
"IGESData_ReferenceError",
"IGESData_TypeError"
]
class IGESData():
    """
    basic description of an IGES Interface
    """
    @staticmethod
    def Init_s() -> None: 
        """
        Prepares General dynamic data used for IGESData specifically : Protocol and Modules, which treat UndefinedEntity
        """
    @staticmethod
    def Protocol_s() -> IGESData_Protocol: 
        """
        Returns a Protocol from IGESData (avoids to create it)
        """
    def __init__(self) -> None: ...
    pass
class IGESData_Array1OfDirPart():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESData_Array1OfDirPart) -> IGESData_Array1OfDirPart: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESData_DirPart: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESData_DirPart: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESData_DirPart: 
        """
        Variable value access
        """
    def First(self) -> IGESData_DirPart: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESData_DirPart) -> None: 
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
    def Last(self) -> IGESData_DirPart: 
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
    def Move(self,theOther : IGESData_Array1OfDirPart) -> IGESData_Array1OfDirPart: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESData_DirPart) -> None: 
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
    def Value(self,theIndex : int) -> IGESData_DirPart: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : IGESData_Array1OfDirPart) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : IGESData_DirPart,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESData_Array1OfIGESEntity():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESData_Array1OfIGESEntity) -> IGESData_Array1OfIGESEntity: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESData_IGESEntity: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESData_IGESEntity: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESData_IGESEntity: 
        """
        Variable value access
        """
    def First(self) -> IGESData_IGESEntity: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESData_IGESEntity) -> None: 
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
    def Last(self) -> IGESData_IGESEntity: 
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
    def Move(self,theOther : IGESData_Array1OfIGESEntity) -> IGESData_Array1OfIGESEntity: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESData_IGESEntity) -> None: 
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
    def Value(self,theIndex : int) -> IGESData_IGESEntity: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : IGESData_IGESEntity,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IGESData_Array1OfIGESEntity) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESData_BasicEditor():
    """
    This class provides various functions of basic edition, such as : - setting header unit (WARNING : DOES NOT convert entities) - computation of the status (Subordinate, UseFlag) of entities of IGES Entities on a whole model - auto correction of IGES Entities, defined both by DirChecker and by specific service AutoCorrect (this auto correction performs non-ambigious, rather logic, editions)
    """
    def ApplyUnit(self,enforce : bool=False) -> None: 
        """
        Applies unit value to convert header data : Resolution, MaxCoord, MaxLineWeight Applies unit only once after SetUnit... has been called, if <enforce> is given as True. It can be called just before writing the model to a file, i.e. when definitive values are finally known
        """
    def AutoCorrect(self,ent : IGESData_IGESEntity) -> bool: 
        """
        Performs auto-correction on an IGESEntity Returns True if something has changed, False if nothing done.
        """
    def AutoCorrectModel(self) -> int: 
        """
        Performs auto-correction on the whole Model Returns the count of modified entities
        """
    def ComputeStatus(self) -> None: 
        """
        Performs the re-computation of status on the whole model (Subordinate Status and Use Flag of each IGES Entity), which can have required values according the way they are referenced (see definitions of Logical use, Physical use, etc...)
        """
    @staticmethod
    def DraftingMax_s() -> int: 
        """
        Returns the maximum allowed value for Drafting Flag
        """
    @staticmethod
    def DraftingName_s(flag : int) -> str: 
        """
        From the flag of drafting standard, returns name, "" if incorrect
        """
    @staticmethod
    def IGESVersionMax_s() -> int: 
        """
        Returns the maximum allowed value for IGESVersion Flag
        """
    @staticmethod
    def IGESVersionName_s(flag : int) -> str: 
        """
        From the flag of IGES version, returns name, "" if incorrect
        """
    @overload
    def Init(self,model : IGESData_IGESModel,protocol : IGESData_Protocol) -> None: 
        """
        Initialize a Basic Editor, with a new IGESModel, ready to run

        Initialize a Basic Editor for IGES Data, ready to run
        """
    @overload
    def Init(self,protocol : IGESData_Protocol) -> None: ...
    def Model(self) -> IGESData_IGESModel: 
        """
        Returns the designated model
        """
    def SetUnitFlag(self,flag : int) -> bool: 
        """
        Sets a new unit from its flag (param 14 of Global Section) Returns True if done, False if <flag> is incorrect
        """
    def SetUnitName(self,name : str) -> bool: 
        """
        Sets a new unit from its name (param 15 of Global Section) Returns True if done, False if <name> is incorrect Remark : if <flag> has been set to 3 (user defined), <name> is then free
        """
    def SetUnitValue(self,val : float) -> bool: 
        """
        Sets a new unit from its value in meters (rounded to the closest one, max gap 1%) Returns True if done, False if <val> is too far from a suitable value
        """
    @staticmethod
    def UnitFlagName_s(flag : int) -> str: 
        """
        From the flag of unit, determines its name, "" if incorrect
        """
    @staticmethod
    def UnitFlagValue_s(flag : int) -> float: 
        """
        From the flag of unit, determines value in MM, 0 if incorrect
        """
    @staticmethod
    def UnitNameFlag_s(name : str) -> int: 
        """
        From the name of unit, computes flag number, 0 if incorrect (in this case, user defined entity remains possible)
        """
    @overload
    def __init__(self,model : IGESData_IGESModel,protocol : IGESData_Protocol) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,protocol : IGESData_Protocol) -> None: ...
    pass
class IGESData_IGESEntity(OCP.Standard.Standard_Transient):
    """
    defines root of IGES Entity definition, including Directory Part, lists of (optionnal) Properties and Associativitiesdefines root of IGES Entity definition, including Directory Part, lists of (optionnal) Properties and Associativitiesdefines root of IGES Entity definition, including Directory Part, lists of (optionnal) Properties and Associativities
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        Returns true if a subscript number is defined. A subscript number is an integer used to identify a label.
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
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
class IGESData_DefList():
    """
    Some fields of an IGES entity may be - Undefined - Defined as a single item - Defined as a list of items. A typical example, which presents this kind of variation, is a level number. This enumeration allows you to identify which of the above is the case. The semantics of the terms is as follows: - DefNone indicates that the list is empty (there is not even a single item). - DefOne indicates that the list contains a single item. - DefSeveral indicates that the list contains several items. - ErrorOne indicates that the list contains one item, but that this item is incorrect - ErrorSeveral indicates that the list contains several items, but that at least one of them is incorrect.

    Members:

      IGESData_DefNone

      IGESData_DefOne

      IGESData_DefSeveral

      IGESData_ErrorOne

      IGESData_ErrorSeveral
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IGESData_DefNone: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_DefNone
    IGESData_DefOne: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_DefOne
    IGESData_DefSeveral: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_DefSeveral
    IGESData_ErrorOne: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_ErrorOne
    IGESData_ErrorSeveral: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_ErrorSeveral
    __entries: dict # value = {'IGESData_DefNone': (IGESData_DefList.IGESData_DefNone, None), 'IGESData_DefOne': (IGESData_DefList.IGESData_DefOne, None), 'IGESData_DefSeveral': (IGESData_DefList.IGESData_DefSeveral, None), 'IGESData_ErrorOne': (IGESData_DefList.IGESData_ErrorOne, None), 'IGESData_ErrorSeveral': (IGESData_DefList.IGESData_ErrorSeveral, None)}
    __members__: dict # value = {'IGESData_DefNone': IGESData_DefList.IGESData_DefNone, 'IGESData_DefOne': IGESData_DefList.IGESData_DefOne, 'IGESData_DefSeveral': IGESData_DefList.IGESData_DefSeveral, 'IGESData_ErrorOne': IGESData_DefList.IGESData_ErrorOne, 'IGESData_ErrorSeveral': IGESData_DefList.IGESData_ErrorSeveral}
    pass
class IGESData_DefSwitch():
    """
    description of a directory componant which can be either undefined (let Void), defined as a Reference to an entity, or as a Rank, integer value adressing a builtin table The entity reference is not included here, only reference status is kept (because entity type must be adapted)
    """
    def DefType(self) -> IGESData_DefType: 
        """
        returns DefType status (Void,Reference,Rank)
        """
    def SetRank(self,val : int) -> None: 
        """
        sets DefSwitch to "Rank" with a Value (in file : Integer > 0)
        """
    def SetReference(self) -> None: 
        """
        sets DefSwitch to "Reference" Status (in file : Integer < 0)
        """
    def SetVoid(self) -> None: 
        """
        sets DefSwitch to "Void" status (in file : Integer = 0)
        """
    def Value(self) -> int: 
        """
        returns Value as Integer (sensefull for a Rank)
        """
    def __init__(self) -> None: ...
    pass
class IGESData_DefType():
    """
    Some fields of an IGES entity may be - Undefined - Defined as a positive integer - Defined as a reference to a specialized entity. A typical example of this kind of variation is color. This enumeration allows you to identify which of the above is the case. The semantics of the terms are as follows: - DefVoid indicates that the item contained in the field is undefined - DefValue indicates that the item is defined as an immediate positive integer value (i.e. not a pointer) - DefReference indicates that the item is defined as an entity - DefAny indicates the item could not be determined - ErrorVal indicates that the item is defined as an integer but its value is incorrect (it could be out of range, for example) - ErrorRef indicates that the item is defined as an entity but is not of the required type.

    Members:

      IGESData_DefVoid

      IGESData_DefValue

      IGESData_DefReference

      IGESData_DefAny

      IGESData_ErrorVal

      IGESData_ErrorRef
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IGESData_DefAny: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_DefAny
    IGESData_DefReference: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_DefReference
    IGESData_DefValue: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_DefValue
    IGESData_DefVoid: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_DefVoid
    IGESData_ErrorRef: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_ErrorRef
    IGESData_ErrorVal: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_ErrorVal
    __entries: dict # value = {'IGESData_DefVoid': (IGESData_DefType.IGESData_DefVoid, None), 'IGESData_DefValue': (IGESData_DefType.IGESData_DefValue, None), 'IGESData_DefReference': (IGESData_DefType.IGESData_DefReference, None), 'IGESData_DefAny': (IGESData_DefType.IGESData_DefAny, None), 'IGESData_ErrorVal': (IGESData_DefType.IGESData_ErrorVal, None), 'IGESData_ErrorRef': (IGESData_DefType.IGESData_ErrorRef, None)}
    __members__: dict # value = {'IGESData_DefVoid': IGESData_DefType.IGESData_DefVoid, 'IGESData_DefValue': IGESData_DefType.IGESData_DefValue, 'IGESData_DefReference': IGESData_DefType.IGESData_DefReference, 'IGESData_DefAny': IGESData_DefType.IGESData_DefAny, 'IGESData_ErrorVal': IGESData_DefType.IGESData_ErrorVal, 'IGESData_ErrorRef': IGESData_DefType.IGESData_ErrorRef}
    pass
class IGESData_GeneralModule(OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    Definition of General Services adapted to IGES. This Services comprise : Shared & Implied Lists, Copy, Check They are adapted according to the organisation of IGES Entities : Directory Part, Lists of Associativities and Properties are specifically processedDefinition of General Services adapted to IGES. This Services comprise : Shared & Implied Lists, Copy, Check They are adapted according to the organisation of IGES Entities : Directory Part, Lists of Associativities and Properties are specifically processedDefinition of General Services adapted to IGES. This Services comprise : Shared & Implied Lists, Copy, Check They are adapted according to the organisation of IGES Entities : Directory Part, Lists of Associativities and Properties are specifically processed
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" For IGES, answer is always True
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> int: 
        """
        Returns a category number which characterizes an entity Category Numbers are managed by the class Category <shares> can be used to evaluate this number in the context Default returns 0 which means "unspecified"
        """
    def CheckCase(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Semantic Checking of an IGESEntity. Performs general Checks, which use DirChecker, then call OwnCheck which does a check specific for each type of Entity
        """
    def CopyCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirChecker(self,CN : int,ent : IGESData_IGESEntity) -> IGESData_DirChecker: 
        """
        Returns a DirChecker, specific for each type of Entity (identified by its Case Number) : this DirChecker defines constraints which must be respected by the DirectoryPart
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
    def FillSharedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills the list of Entities shared by an IGESEntity <ent>, according a Case Number <CN> (formerly computed by CaseNum). Considers Properties and Directory Part, and calls OwnSharedCase (which is adapted to each Type of Entity)
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
    def ListImplied(self,model : OCP.Interface.Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> considered in the context of a Model <model> : i.e. the Entities which are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillShared + ListImplied give the complete list of References Default calls ListImpliedCase (i.e. ignores the model) Can be redefined to use the model for working
        """
    def ListImpliedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Implied References of <ent>. Here, these are the Associativities, plus the Entities defined by OwnSharedCase
        """
    def Name(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of an IGES Entity (its NameValue) Can be redefined for an even more specific case ...
        """
    def NewCopiedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Specific operator (create+copy) defaulted to do nothing. It can be redefined : When it is not possible to work in two steps (NewVoid then CopyCase). This can occur when there is no default constructor : hence the result <entto> must be created with an effective definition. Remark : if NewCopiedCase is defined, CopyCase has nothing to do Returns True if it has produced something, false else
        """
    def NewVoid(self,CN : int,entto : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific creation of a new void entity
        """
    def OwnCheckCase(self,CN : int,ent : IGESData_IGESEntity,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check for each type of Entity
        """
    def OwnCopyCase(self,CN : int,entfrom : IGESData_IGESEntity,entto : IGESData_IGESEntity,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies parameters which are specific of each Type of Entity
        """
    def OwnDeleteCase(self,CN : int,ent : IGESData_IGESEntity) -> None: 
        """
        Specific preparation for delete, acts on own parameters Default does nothing, to be redefined as required
        """
    def OwnImpliedCase(self,CN : int,ent : IGESData_IGESEntity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific list of Entities implied by a given IGESEntity <ent> (in addition to Associativities). By default, there are none, but this method can be redefined as required
        """
    def OwnRenewCase(self,CN : int,entfrom : IGESData_IGESEntity,entto : IGESData_IGESEntity,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Renews parameters which are specific of each Type of Entity : the provided default does nothing, but this method may be redefined as required
        """
    def OwnSharedCase(self,CN : int,ent : IGESData_IGESEntity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a given IGESEntity <ent>, from its specific parameters : specific for each type
        """
    def RenewImpliedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Renewing of Implied References. For IGESEntities, Copies general data(List of Associativities) and calls OwnRenewCase
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
        Prepares an IGES Entity for delete : works on directory part then calls OwnDeleteCase While dispatch requires to copy the entities, <dispatched> is ignored, entities are cleared in any case
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
class IGESData_SpecificModule(OCP.Standard.Standard_Transient):
    """
    This class defines some Services which are specifically attached to IGES Entities : DumpThis class defines some Services which are specifically attached to IGES Entities : DumpThis class defines some Services which are specifically attached to IGES Entities : Dump
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
    def OwnCorrect(self,CN : int,ent : IGESData_IGESEntity) -> bool: 
        """
        Specific Automatic Correction on own Parameters of an Entity. It works by setting in accordance redundant data, if there are when there is no ambiguity (else, it does nothing). Remark that classic Corrections on Directory Entry (to set void data) are taken into account alsewhere.
        """
    def OwnDump(self,CN : int,ent : IGESData_IGESEntity,dumper : IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Specific Dump for each type of IGES Entity : it concerns only own parameters, the general data (Directory Part, Lists) are taken into account by the IGESDumper See class IGESDumper for the rules to follow for <own> and <attached> level
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
class IGESData_DirChecker():
    """
    This class centralizes general Checks upon an IGES Entity's Directory Part. That is : such field Ignored or Required, or Required with a given Value (for an Integer field) More precise checks can be performed as necessary, by each Entity (method OwnCheck).
    """
    def BlankStatusIgnored(self) -> None: 
        """
        Sets Blank Status to be ignored (should not be defined, or its value should be 0)
        """
    def BlankStatusRequired(self,val : int) -> None: 
        """
        Sets Blank Status to be required at a given value
        """
    def Check(self,ach : OCP.Interface.Interface_Check,ent : IGESData_IGESEntity) -> Any: 
        """
        Performs the Checks on an IGESEntity, according to the recorded criteria In addition, does minimal Checks, such as admitted range for Status, or presence of Error status in some data (Color, ...)
        """
    def CheckTypeAndForm(self,ach : OCP.Interface.Interface_Check,ent : IGESData_IGESEntity) -> Any: 
        """
        Performs a Check only on Values of Type Number and Form Number This allows to do a check on an Entity not yet completely filled but of which Type and Form Number have been already set
        """
    def Color(self,crit : IGESData_DefType) -> None: 
        """
        Sets Color criterium If crit is DefVoid, Ignored : should not be defined If crit is DefAny, Required : must be defined (value or ref) Other values are not taken in account
        """
    def Correct(self,ent : IGESData_IGESEntity) -> bool: 
        """
        Corrects the Directory Entry of an IGES Entity as far as it is possible according recorded criteria without any ambiguity : - if a numeric Status is required a given value, this value is enforced - if an item is required to be Void, or if it recorded as Erroneous, it is cleared (set to Void) - Type Number is enforced - finally Form Number is enforced only if one and only Value is admitted (no range, see Constructors of DirChecker)
        """
    def GraphicsIgnored(self,hierarchy : int=-1) -> None: 
        """
        Sets Graphics data (LineFont, LineWeight, Color, Level, View) to be ignored according value of Hierarchy status : If hierarchy is not given, they are Ignored any way (that is, they should not be defined) If hierarchy is given, Graphics are Ignored if the Hierarchy status has the value given in argument "hierarchy"
        """
    def HierarchyStatusIgnored(self) -> None: 
        """
        Sets Hierarchy Status to be ignored (should not be defined, or its value should be 0)
        """
    def HierarchyStatusRequired(self,val : int) -> None: 
        """
        Sets Hierarchy Status to be required at a given value
        """
    def IsSet(self) -> bool: 
        """
        Returns True if at least one criterium has already been set Allows user to store a DirChecker (static variable) then ask if it has been set before setting it
        """
    def LineFont(self,crit : IGESData_DefType) -> None: 
        """
        Sets LineFont criterium If crit is DefVoid, Ignored : should not be defined If crit is DefAny, Required : must be defined (value or ref) If crit is DefValue, Required as a Value (error if Reference) Other values are not taken in account
        """
    def LineWeight(self,crit : IGESData_DefType) -> None: 
        """
        Sets LineWeight criterium If crit is DefVoid, Ignored : should not be defined If crit is DefValue, Required Other values are not taken in account
        """
    def SetDefault(self) -> None: 
        """
        Sets a DirChecker with most current criteria, that is : Structure Ignored ( worths call Structure(crit = DefVoid) )
        """
    def Structure(self,crit : IGESData_DefType) -> None: 
        """
        Sets Structure criterium. If crit is DefVoid, Ignored : should not be defined If crit is DefReference, Required : must be defined Other values are not taken in account
        """
    def SubordinateStatusIgnored(self) -> None: 
        """
        Sets Subordinate Status to be ignored (should not be defined, or its value should be 0)
        """
    def SubordinateStatusRequired(self,val : int) -> None: 
        """
        Sets Subordinate Status to be required at a given value
        """
    def UseFlagIgnored(self) -> None: 
        """
        Sets Blank Status to be ignored (should not be defined, or its value should be 0)
        """
    def UseFlagRequired(self,val : int) -> None: 
        """
        Sets Blank Status to be required at a given value Give -1 to demand UseFlag not zero (but no precise value req.)
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,atype : int,aform : int) -> None: ...
    @overload
    def __init__(self,atype : int) -> None: ...
    @overload
    def __init__(self,atype : int,aform1 : int,aform2 : int) -> None: ...
    pass
class IGESData_DirPart():
    """
    litteral/numeric description of an entity's directory section, taken from file
    """
    def Init(self,i1 : int,i2 : int,i3 : int,i4 : int,i5 : int,i6 : int,i7 : int,i8 : int,i9 : int,i19 : int,i11 : int,i12 : int,i13 : int,i14 : int,i15 : int,i16 : int,i17 : int,res1 : str,res2 : str,label : str,subscript : str) -> None: 
        """
        fills DirPart with consistant data read from file
        """
    def Type(self) -> IGESData_IGESType: 
        """
        returns "type" and "form" info, used to recognize the entity
        """
    def Values(self,res1 : str,res2 : str,label : str,subscript : str) -> Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int]: 
        """
        returns values recorded in DirPart (content of cstrings are modified)
        """
    def __init__(self) -> None: ...
    pass
class IGESData_Protocol(OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    Description of basic Protocol for IGES This comprises treatement of IGESModel and Recognition of Undefined-FreeFormat-EntityDescription of basic Protocol for IGES This comprises treatement of IGESModel and Recognition of Undefined-FreeFormat-EntityDescription of basic Protocol for IGES This comprises treatement of IGESModel and Recognition of Undefined-FreeFormat-Entity
    """
    @staticmethod
    def Active_s() -> OCP.Interface.Interface_Protocol: 
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
    def GlobalCheck(self,G : OCP.Interface.Interface_Graph,ach : OCP.Interface.Interface_Check) -> bool: 
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
    def IsSuitableModel(self,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True if <model> is a Model of IGES Norm
        """
    def IsUnknownEntity(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e. Type UndefinedEntity, status Unknown
        """
    def NbResources(self) -> int: 
        """
        Gives the count of Resource Protocol. Here, none
        """
    def NbTypes(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the count of DISTINCT types under which an entity may be processed. Each one is candidate to be recognized by TypeNumber, <obj> is then processed according it By default, returns 1 (the DynamicType)
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Creates an empty Model for IGES Norm
        """
    def Resource(self,num : int) -> OCP.Interface.Interface_Protocol: 
        """
        Returns a Resource, given a rank. Here, none
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
        Returns a Case Number, specific of each recognized Type Here, Undefined and Free Format Entities have the Number 1.
        """
    def UnknownEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Creates a new Unknown Entity for IGES (UndefinedEntity)
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
class IGESData_FileRecognizer(OCP.Standard.Standard_Transient):
    def Add(self,reco : IGESData_FileRecognizer) -> None: 
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
    def Evaluate(self,akey : IGESData_IGESType,res : IGESData_IGESEntity) -> bool: 
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
    def Result(self) -> IGESData_IGESEntity: 
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
class IGESData_UndefinedEntity(IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    undefined (unknown or error) entity specific of IGES DirPart can be correct or not : if it is not, a flag indicates it, and each corrupted field has an associated error flagundefined (unknown or error) entity specific of IGES DirPart can be correct or not : if it is not, a flag indicates it, and each corrupted field has an associated error flagundefined (unknown or error) entity specific of IGES DirPart can be correct or not : if it is not, a flag indicates it, and each corrupted field has an associated error flag
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def ChangeableContent(self) -> OCP.Interface.Interface_UndefinedContent: 
        """
        Returns own data as an UndefinedContent, in order to touch it
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        returns Error status if necessary, else calls original method
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        returns Error status if necessary, else calls original method
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        returns Error status if necessary, else calls original method
        """
    def DefView(self) -> IGESData_DefList: 
        """
        returns Error status if necessary, else calls original method
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def DirStatus(self) -> int: 
        """
        returns Directory Error Status (used for Copy)
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        returns Error status if necessary, else calls original method (that is, if SubScript field is not blank or positive integer)
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def IsOKDirPart(self) -> bool: 
        """
        says if DirPart is OK or not (if not, it is erroneous) Note that if it is not, Def* methods can return Error status
        """
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def ReadDir(self,IR : IGESData_IGESReaderData,DP : IGESData_DirPart,ach : OCP.Interface.Interface_Check) -> bool: 
        """
        Computes the Directory Error Status, to be called before standard ReadDir from IGESReaderTool Returns True if OK (hence, Directory can be loaded), Else returns False and the DirPart <DP> is modified (hence, Directory Error Status is non null; and standard Read will work with an acceptable DirectoryPart)
        """
    def ReadOwnParams(self,IR : IGESData_IGESReaderData,PR : IGESData_ParamReader) -> None: 
        """
        reads own parameters from file; PR gives access to them, IR detains parameter types and values Here, reads all parameters, integers are considered as entity reference unless they cannot be; no list interpretation No property or associativity list is managed
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def SetNewContent(self,cont : OCP.Interface.Interface_UndefinedContent) -> None: 
        """
        Redefines a completely new UndefinedContent Used by a Copy which begins by ShallowCopy, for instance
        """
    def SetOKDirPart(self) -> None: 
        """
        Erases the Directory Error Status Warning : Be sure that data are consistent to call this method ...
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UndefinedContent(self) -> OCP.Interface.Interface_UndefinedContent: 
        """
        Returns own data as an UndefinedContent
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
        """
    def WriteOwnParams(self,IW : IGESData_IGESWriter) -> None: 
        """
        writes parameters to IGESWriter, taken from UndefinedContent
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
class IGESData_DefaultGeneral(IGESData_GeneralModule, OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    Processes the specific case of UndefinedEntity from IGESData (Case Number 1)Processes the specific case of UndefinedEntity from IGESData (Case Number 1)Processes the specific case of UndefinedEntity from IGESData (Case Number 1)
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" For IGES, answer is always True
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> int: 
        """
        Returns a category number which characterizes an entity Category Numbers are managed by the class Category <shares> can be used to evaluate this number in the context Default returns 0 which means "unspecified"
        """
    def CheckCase(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Semantic Checking of an IGESEntity. Performs general Checks, which use DirChecker, then call OwnCheck which does a check specific for each type of Entity
        """
    def CopyCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirChecker(self,CN : int,ent : IGESData_IGESEntity) -> IGESData_DirChecker: 
        """
        Returns a DirChecker, specific for each type of Entity Here, Returns an empty DirChecker (no constraint to check)
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
    def FillSharedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills the list of Entities shared by an IGESEntity <ent>, according a Case Number <CN> (formerly computed by CaseNum). Considers Properties and Directory Part, and calls OwnSharedCase (which is adapted to each Type of Entity)
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
    def ListImplied(self,model : OCP.Interface.Interface_InterfaceModel,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        List the Implied References of <ent> considered in the context of a Model <model> : i.e. the Entities which are Referenced while not considered as Shared (not copied if <ent> is, references not renewed by CopyCase but by ImpliedCase, only if referenced Entities have been Copied too) FillShared + ListImplied give the complete list of References Default calls ListImpliedCase (i.e. ignores the model) Can be redefined to use the model for working
        """
    def ListImpliedCase(self,CN : int,ent : OCP.Standard.Standard_Transient,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Implied References of <ent>. Here, these are the Associativities, plus the Entities defined by OwnSharedCase
        """
    def Name(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of an IGES Entity (its NameValue) Can be redefined for an even more specific case ...
        """
    def NewCopiedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> bool: 
        """
        Specific operator (create+copy) defaulted to do nothing. It can be redefined : When it is not possible to work in two steps (NewVoid then CopyCase). This can occur when there is no default constructor : hence the result <entto> must be created with an effective definition. Remark : if NewCopiedCase is defined, CopyCase has nothing to do Returns True if it has produced something, false else
        """
    def NewVoid(self,CN : int,entto : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific creation of a new void entity (UndefinedEntity only)
        """
    def OwnCheckCase(self,CN : int,ent : IGESData_IGESEntity,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check for each type of Entity Here, does nothing (no constraint to check)
        """
    def OwnCopyCase(self,CN : int,entfrom : IGESData_IGESEntity,entto : IGESData_IGESEntity,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies parameters which are specific of each Type of Entity
        """
    def OwnDeleteCase(self,CN : int,ent : IGESData_IGESEntity) -> None: 
        """
        Specific preparation for delete, acts on own parameters Default does nothing, to be redefined as required
        """
    def OwnImpliedCase(self,CN : int,ent : IGESData_IGESEntity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific list of Entities implied by a given IGESEntity <ent> (in addition to Associativities). By default, there are none, but this method can be redefined as required
        """
    def OwnRenewCase(self,CN : int,entfrom : IGESData_IGESEntity,entto : IGESData_IGESEntity,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Renews parameters which are specific of each Type of Entity : the provided default does nothing, but this method may be redefined as required
        """
    def OwnSharedCase(self,CN : int,ent : IGESData_IGESEntity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by an IGESEntity, which must be an UndefinedEntity
        """
    def RenewImpliedCase(self,CN : int,entfrom : OCP.Standard.Standard_Transient,entto : OCP.Standard.Standard_Transient,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Renewing of Implied References. For IGESEntities, Copies general data(List of Associativities) and calls OwnRenewCase
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
        Prepares an IGES Entity for delete : works on directory part then calls OwnDeleteCase While dispatch requires to copy the entities, <dispatched> is ignored, entities are cleared in any case
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
class IGESData_GlobalNodeOfSpecificLib(OCP.Standard.Standard_Transient):
    def Add(self,amodule : IGESData_SpecificModule,aprotocol : IGESData_Protocol) -> None: 
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
    def Module(self) -> IGESData_SpecificModule: 
        """
        Returns the Module stored in a given GlobalNode
        """
    def Next(self) -> IGESData_GlobalNodeOfSpecificLib: 
        """
        Returns the Next GlobalNode. If none is defined, returned value is a Null Handle
        """
    def Protocol(self) -> IGESData_Protocol: 
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
class IGESData_GlobalNodeOfWriterLib(OCP.Standard.Standard_Transient):
    def Add(self,amodule : IGESData_ReadWriteModule,aprotocol : IGESData_Protocol) -> None: 
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
    def Module(self) -> IGESData_ReadWriteModule: 
        """
        Returns the Module stored in a given GlobalNode
        """
    def Next(self) -> IGESData_GlobalNodeOfWriterLib: 
        """
        Returns the Next GlobalNode. If none is defined, returned value is a Null Handle
        """
    def Protocol(self) -> IGESData_Protocol: 
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
class IGESData_GlobalSection():
    """
    Description of a global section (corresponds to file header) used as well in IGESModel, IGESReader and IGESWriter Warning : From IGES-5.1, a parameter is added : LastChangeDate (concerns transferred set of data, not the file itself) Of course, it can be absent if read from earlier versions (a default is then to be set to current date) From 5.3, one more : ApplicationProtocol (optional)
    """
    def ApplicationProtocol(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def AuthorName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of the IGES file author.
        """
    def CompanyName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of the company where the IGES file was written.
        """
    def CopyRefs(self) -> None: 
        """
        Copies data referenced by Handle (that is, Strings) usefull to "isolate" a GlobalSection after copy by "=" (from a Model to another Model for instance)
        """
    def Date(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the IGES file creation date.
        """
    def DraftingStandard(self) -> int: 
        """
        None
        """
    def EndMark(self) -> str: 
        """
        Returns the record delimiter character.
        """
    def FileName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of the IGES file.
        """
    def HasApplicationProtocol(self) -> bool: 
        """
        None
        """
    def HasLastChangeDate(self) -> bool: 
        """
        Returns True if the date and time when the model was created or last modified are specified, i.e. not defaulted to NULL.
        """
    def HasMaxCoord(self) -> bool: 
        """
        Returns True if the approximate maximum coordinate value found in the model is greater than 0.
        """
    def IGESVersion(self) -> int: 
        """
        Returns the IGES version that the IGES file was written in.
        """
    def Init(self,params : OCP.Interface.Interface_ParamSet,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Fills GlobalSection from a ParamSet (i.e. taken from file) undefined parameters do not change default values when defined Fills Check about Corrections or Fails
        """
    def IntegerBits(self) -> int: 
        """
        Returns the number of binary bits for integer representations.
        """
    def InterfaceVersion(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of the pre-processor used to write the IGES file.
        """
    def LastChangeDate(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the date and time when the model was created or last modified (for IGES 5.1 and later).
        """
    def LineWeightGrad(self) -> int: 
        """
        Returns the maximum number of line weight gradations.
        """
    def MaxCoord(self) -> float: 
        """
        Returns the approximate maximum coordinate value found in the model.
        """
    def MaxDigitsDouble(self) -> int: 
        """
        None
        """
    def MaxDigitsSingle(self) -> int: 
        """
        None
        """
    def MaxLineWeight(self) -> float: 
        """
        Returns the of maximum line weight width in IGES file units.
        """
    def MaxMaxCoord(self,val : float=0.0) -> None: 
        """
        None
        """
    def MaxMaxCoords(self,xyz : OCP.gp.gp_XYZ) -> None: 
        """
        None
        """
    def MaxPower10Double(self) -> int: 
        """
        Returns the maximum power of a decimal representation of a double-precision floating point number in the sending system.
        """
    def MaxPower10Single(self) -> int: 
        """
        Returns the maximum power of a decimal representation of a single-precision floating point number in the sending system.
        """
    @staticmethod
    @overload
    def NewDateString_s(date : OCP.TCollection.TCollection_HAsciiString,mode : int=1) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a string built from year, month, day, hour, minute and second values. The form of the resulting string is defined as follows: - -1: YYMMDD.HHNNSS, - 0: YYYYMMDD.HHNNSS, - 1: YYYY-MM-DD:HH-NN-SS, where: - YYYY or YY is 4 or 2 digit year, - HH is hour (00-23), - MM is month (01-12), - NN is minute (00-59) - DD is day (01-31), - SS is second (00-59).

        Converts the string given in the form YYMMDD.HHNNSS or YYYYMMDD.HHNNSS to either YYMMDD.HHNNSS, YYYYMMDD.HHNNSS or YYYY-MM-DD:HH-NN-SS.
        """
    @staticmethod
    @overload
    def NewDateString_s(year : int,month : int,day : int,hour : int,minut : int,second : int,mode : int=-1) -> OCP.TCollection.TCollection_HAsciiString: ...
    def Params(self) -> OCP.Interface.Interface_ParamSet: 
        """
        Returns all contained data in the form of a ParamSet Remark : Strings are given under Hollerith form
        """
    def ReceiveName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of the receiving system.
        """
    def Resolution(self) -> float: 
        """
        Returns the resolution used in the IGES file.
        """
    def Scale(self) -> float: 
        """
        Returns the scale used in the IGES file.
        """
    def SendName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of the sending system.
        """
    def Separator(self) -> str: 
        """
        Returns the parameter delimiter character.
        """
    def SetApplicationProtocol(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetAuthorName(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetCompanyName(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetDate(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetDraftingStandard(self,val : int) -> None: 
        """
        None
        """
    def SetEndMark(self,val : str) -> None: 
        """
        None
        """
    def SetFileName(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetIGESVersion(self,val : int) -> None: 
        """
        None
        """
    def SetIntegerBits(self,val : int) -> None: 
        """
        None
        """
    def SetInterfaceVersion(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    @overload
    def SetLastChangeDate(self) -> None: 
        """
        None

        None
        """
    @overload
    def SetLastChangeDate(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def SetLineWeightGrad(self,val : int) -> None: 
        """
        None
        """
    def SetMaxCoord(self,val : float=0.0) -> None: 
        """
        None
        """
    def SetMaxDigitsDouble(self,val : int) -> None: 
        """
        None
        """
    def SetMaxDigitsSingle(self,val : int) -> None: 
        """
        None
        """
    def SetMaxLineWeight(self,val : float) -> None: 
        """
        None
        """
    def SetMaxPower10Double(self,val : int) -> None: 
        """
        None
        """
    def SetMaxPower10Single(self,val : int) -> None: 
        """
        None
        """
    def SetReceiveName(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetResolution(self,val : float) -> None: 
        """
        None
        """
    def SetScale(self,val : float) -> None: 
        """
        None
        """
    def SetSendName(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSeparator(self,val : str) -> None: 
        """
        None
        """
    def SetSystemId(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetUnitFlag(self,val : int) -> None: 
        """
        None
        """
    def SetUnitName(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SystemId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the Native System ID of the system that created the IGES file.
        """
    def TranslatedFromHollerith(self,astr : OCP.TCollection.TCollection_HAsciiString) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a string withpout its Hollerith marks (nnnH ahead). Remark : all strings stored in GlobalSection are expurged from Hollerith informations (without nnnH) If <astr> is not Hollerith form, it is simply copied
        """
    def UnitFlag(self) -> int: 
        """
        Returns the unit flag that was used to write the IGES file.
        """
    def UnitName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the name of the unit the IGES file was written in.
        """
    def UnitValue(self) -> float: 
        """
        Returns the unit value (in meters) that the IGES file was written in.
        """
    def __init__(self) -> None: ...
    pass
class IGESData_HArray1OfIGESEntity(IGESData_Array1OfIGESEntity, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESData_Array1OfIGESEntity: 
        """
        None
        """
    def Assign(self,theOther : IGESData_Array1OfIGESEntity) -> IGESData_Array1OfIGESEntity: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESData_Array1OfIGESEntity: 
        """
        None
        """
    def ChangeFirst(self) -> IGESData_IGESEntity: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESData_IGESEntity: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESData_IGESEntity: 
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
    def First(self) -> IGESData_IGESEntity: 
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
    def Init(self,theValue : IGESData_IGESEntity) -> None: 
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
    def Last(self) -> IGESData_IGESEntity: 
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
    def Move(self,theOther : IGESData_Array1OfIGESEntity) -> IGESData_Array1OfIGESEntity: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESData_IGESEntity) -> None: 
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
    def Value(self,theIndex : int) -> IGESData_IGESEntity: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IGESData_Array1OfIGESEntity) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESData_IGESEntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class IGESData_IGESDumper():
    """
    Provides a way to obtain a clear Dump of an IGESEntity (distinct from normalized output). It works with tools attached to Entities, as for normalized Reade and Write
    """
    def Dump(self,ent : IGESData_IGESEntity,S : OCP.Message.Message_Messenger,own : int,attached : int=-1) -> None: 
        """
        None
        """
    def OwnDump(self,ent : IGESData_IGESEntity,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Specific Dump for each IGES Entity, call by Dump (just above) <own> is the parameter <own> from Dump
        """
    def PrintDNum(self,ent : IGESData_IGESEntity,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints onto an output, the "Number of Directory Entry" which corresponds to an IGESEntity in the IGESModel, under the form "D#nnn" (a Null Handle gives D#0)
        """
    def PrintShort(self,ent : IGESData_IGESEntity,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints onto an output, the "Number of Directory Entry" (see PrintDNum) plus IGES Type and Form Numbers, which gives "D#nnn Type nnn Form nnn"
        """
    def __init__(self,model : IGESData_IGESModel,protocol : IGESData_Protocol) -> None: ...
    pass
class IGESData_ColorEntity(IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines required type for Color in directory part an effective Color entity must inherits itdefines required type for Color in directory part an effective Color entity must inherits itdefines required type for Color in directory part an effective Color entity must inherits it
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        Returns true if a subscript number is defined. A subscript number is an integer used to identify a label.
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
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
class IGESData_IGESModel(OCP.Interface.Interface_InterfaceModel, OCP.Standard.Standard_Transient):
    """
    Defines the file header and entities for IGES files. These headers and entities result from a complete data translation using the IGES data exchange processor. Each entity is contained in a single model only and has a unique identifier. You can access this identifier using the method Number. Gives an access to the general data in the Start and the Global sections of an IGES file. The IGES file includes the following sections: -Start, -Global, -Directory Entry, -Parameter Data, -TerminateDefines the file header and entities for IGES files. These headers and entities result from a complete data translation using the IGES data exchange processor. Each entity is contained in a single model only and has a unique identifier. You can access this identifier using the method Number. Gives an access to the general data in the Start and the Global sections of an IGES file. The IGES file includes the following sections: -Start, -Global, -Directory Entry, -Parameter Data, -TerminateDefines the file header and entities for IGES files. These headers and entities result from a complete data translation using the IGES data exchange processor. Each entity is contained in a single model only and has a unique identifier. You can access this identifier using the method Number. Gives an access to the general data in the Start and the Global sections of an IGES file. The IGES file includes the following sections: -Start, -Global, -Directory Entry, -Parameter Data, -Terminate
    """
    def AddEntity(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Internal method for adding an Entity. Used by file reading (defined by each Interface) and Transfer tools. It adds the entity required to be added, not its refs : see AddWithRefs. If <anentity> is a ReportEntity, it is added to the list of Reports, its Concerned Entity (Erroneous or Corrected, else Unknown) is added to the list of Entities. That is, the ReportEntity must be created before Adding
        """
    def AddReportEntity(self,rep : OCP.Interface.Interface_ReportEntity,semantic : bool=False) -> bool: 
        """
        Adds a ReportEntity as such. Returns False if the concerned entity is not recorded in the Model Else, adds it into, either the main report list or the list for semantic checks, then returns True
        """
    def AddStartLine(self,line : str,atnum : int=0) -> None: 
        """
        Adds a new string to the existing Start section at the end if atnum is 0 or not given, or before atnumth line.
        """
    @overload
    def AddWithRefs(self,anent : OCP.Standard.Standard_Transient,level : int=0,listall : bool=False) -> None: 
        """
        Adds to the Model, an Entity with all its References, as they are defined by General Services FillShared and ListImplied. Process is recursive (any sub-levels) if <level> = 0 (Default) Else, adds sub-entities until the required sub-level. Especially, if <level> = 1, adds immediate subs and that's all

        Same as above, but works with the Protocol of the Model

        Same as above, but works with an already created GeneralLib
        """
    @overload
    def AddWithRefs(self,anent : OCP.Standard.Standard_Transient,lib : OCP.Interface.Interface_GeneralLib,level : int=0,listall : bool=False) -> None: ...
    @overload
    def AddWithRefs(self,anent : OCP.Standard.Standard_Transient,proto : OCP.Interface.Interface_Protocol,level : int=0,listall : bool=False) -> None: ...
    def ApplyStatic(self,param : str='') -> bool: 
        """
        Sets some of the Global section parameters with the values defined by the translation parameters. param may be: - receiver (value read in XSTEP.iges.header.receiver), - author (value read in XSTEP.iges.header.author), - company (value read in XSTEP.iges.header.company). The default value for param is an empty string. Returns True when done and if param is given, False if param is unknown or empty. Note: Set the unit in the IGES file Global section via IGESData_BasicEditor class.
        """
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
        Erases all data specific to IGES file Header (Start + Global)
        """
    def ClearLabels(self) -> None: 
        """
        erases specific labels, i.e. does nothing
        """
    def ClearReportEntity(self,num : int) -> bool: 
        """
        Removes the ReportEntity attached to Entity <num>. Returns True if done, False if no ReportEntity was attached to <num>. Warning : the caller must assume that this clearing is meaningfull
        """
    def ClearStartSection(self) -> None: 
        """
        Clears the IGES file Start Section
        """
    def Contains(self,anentity : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if a Model contains an Entity (for a ReportEntity, looks for the ReportEntity itself AND its Concerned Entity)
        """
    def DNum(self,ent : IGESData_IGESEntity) -> int: 
        """
        Returns the equivalent DE Number for an Entity, i.e. 2*Number(ent)-1 , or 0 if <ent> is unknown from <me> This DE Number is used for File Writing for instance
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
    def DumpHeader(self,S : OCP.Message.Message_Messenger,level : int=0) -> None: 
        """
        Prints the IGES file header (Start and Global Sections) to the log file. The integer parameter is intended to be used as a level indicator but is not used at present.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Entities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of all Entities, as an Iterator on Entities (the Entities themselves, not the Reports)
        """
    def Entity(self,num : int) -> IGESData_IGESEntity: 
        """
        Returns an IGES entity given by its rank number.
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
        gets Header (GlobalSection) from another Model
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
    def GlobalSection(self) -> IGESData_GlobalSection: 
        """
        Returns the Global section of the IGES file.
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
    def NbStartLines(self) -> int: 
        """
        Returns the count of recorded Start Lines
        """
    def NbTypes(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the count of DISTINCT types under which an entity may be processed. Defined by the Protocol, which gives default as 1 (dynamic Type).
        """
    def NewEmptyModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns a New Empty Model, same type as <me> i.e. IGESModel
        """
    def NextNumberForLabel(self,label : str,lastnum : int=0,exact : bool=True) -> int: 
        """
        Searches a label which matches with one entity. Begins from <lastnum>+1 (default:1) and scans the entities until <NbEntities>. For the first which matches <label>, this method returns its Number. Returns 0 if nothing found Can be called recursively (labels are not specified as unique) <exact> : if True (default), exact match is required else, checks the END of entity label
        """
    def Number(self,anentity : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the Number of an Entity in the Model if it contains it. Else returns 0. For a ReportEntity, looks at Concerned Entity. Returns the Directory entry Number of an Entity in the Model if it contains it. Else returns 0. For a ReportEntity, looks at Concerned Entity.
        """
    def Print(self,ent : OCP.Standard.Standard_Transient,s : OCP.Message.Message_Messenger,mode : int=0) -> None: 
        """
        Prints identification of a given entity in <me>, in order to be printed in a list or phrase <mode> < 0 : prints only its number <mode> = 1 : just calls PrintLabel <mode> = 0 (D) : prints its number plus '/' plus PrintLabel If <ent> == <me>, simply prints "Global" If <ent> is unknown, prints "??/its type"
        """
    def PrintInfo(self,ent : OCP.Standard.Standard_Transient,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints label specific to IGES norm for a given entity, i.e. its directory entry number (2*Number-1)
        """
    def PrintLabel(self,ent : OCP.Standard.Standard_Transient,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints label specific to IGES norm for a given entity, i.e. its directory entry number (2*Number-1)
        """
    def PrintToLog(self,ent : OCP.Standard.Standard_Transient,S : OCP.Message.Message_Messenger) -> None: 
        """
        Prints label specific to IGES norm for a given -- -- entity, i.e. its directory entry number (2*Number-1) in the log file format.
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
    def SetGlobalSection(self,header : IGESData_GlobalSection) -> None: 
        """
        Sets the Global section of the IGES file.
        """
    def SetLineWeights(self,defw : float) -> None: 
        """
        Sets LineWeights of contained Entities according header data (MaxLineWeight and LineWeightGrad) or to a default value for undefined weights
        """
    def SetProtocol(self,proto : OCP.Interface.Interface_Protocol) -> None: 
        """
        Sets a Protocol for this Model It is also set by a call to AddWithRefs with Protocol It is used for : DumpHeader (as required), ClearEntities ...
        """
    def SetReportEntity(self,num : int,rep : OCP.Interface.Interface_ReportEntity) -> bool: 
        """
        Sets or Replaces a ReportEntity for the Entity <num>. Returns True if Report is replaced, False if it has been replaced Warning : the caller must assume that this setting is meaningfull
        """
    def SetStartSection(self,list : OCP.TColStd.TColStd_HSequenceOfHAsciiString,copy : bool=True) -> None: 
        """
        Sets a new Start section from a list of strings. If copy is false, the Start section will be shared. Any modifications made to the strings later on, will have an effect on the Start section. If copy is true (default value), an independent copy of the strings is created and used as the Start section. Any modifications made to the strings later on, will have no effect on the Start section.
        """
    @staticmethod
    def SetTemplate_s(name : str,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Records a new template model with a name. If the name was already recorded, the corresponding template is replaced by the new one. Then, WARNING : test HasTemplate to avoid surprises
        """
    def StartLine(self,num : int) -> str: 
        """
        Returns a line from the IGES file Start section by specifying its number. An empty string is returned if the number given is out of range, the range being from 1 to NbStartLines.
        """
    def StartSection(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns Model's Start Section (list of comment lines)
        """
    def StringLabel(self,ent : OCP.Standard.Standard_Transient) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a string with the label attached to a given entity, i.e. a string "Dnn" with nn = directory entry number (2*N-1)
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
        Checks that the IGES file Global section contains valid data that conforms to the IGES specifications.
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
        :type: bool
        """
    @DispatchStatus.setter
    def DispatchStatus(self, arg1: bool) -> None:
        pass
    pass
class IGESData_IGESReaderData(OCP.Interface.Interface_FileReaderData, OCP.Standard.Standard_Transient):
    """
    specific FileReaderData for IGES contains header as GlobalSection, and for each Entity, its directory part as DirPart, list of Parameters as ParamSet Each Item has a DirPart, plus classically a ParamSet and the correspondant recognized Entity (inherited from FileReaderData) Parameters are accessed through specific objects, ParamReadersspecific FileReaderData for IGES contains header as GlobalSection, and for each Entity, its directory part as DirPart, list of Parameters as ParamSet Each Item has a DirPart, plus classically a ParamSet and the correspondant recognized Entity (inherited from FileReaderData) Parameters are accessed through specific objects, ParamReadersspecific FileReaderData for IGES contains header as GlobalSection, and for each Entity, its directory part as DirPart, list of Parameters as ParamSet Each Item has a DirPart, plus classically a ParamSet and the correspondant recognized Entity (inherited from FileReaderData) Parameters are accessed through specific objects, ParamReaders
    """
    def AddGlobal(self,atype : OCP.Interface.Interface_ParamType,aval : str) -> None: 
        """
        adds a parameter to global section's parameter list
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
    def AddStartLine(self,aval : str) -> None: 
        """
        adds a start line to start section
        """
    def BindEntity(self,num : int,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Binds an entity to a record
        """
    def BoundEntity(self,num : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the entity bound to a record, set by SetEntities
        """
    def ChangeParam(self,num : int,nump : int) -> OCP.Interface.Interface_FileParameter: 
        """
        Same as above, but in order to be modified on place
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultLineWeight(self) -> float: 
        """
        Returns the recorded Default Line Weight, if there is (else, returns 0)
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Destroy(self) -> None: ...
    def DirPart(self,num : int) -> IGESData_DirPart: 
        """
        returns DirPart identified by record no (half Dsect number)
        """
    def DirType(self,num : int) -> IGESData_IGESType: 
        """
        returns "type" and "form" info from a directory part
        """
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
        determines next suitable record from num; that is num+1 except for last one which gives 0
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlobalCheck(self) -> OCP.Interface.Interface_Check: 
        """
        Returns the recorded Global Check
        """
    def GlobalSection(self) -> IGESData_GlobalSection: 
        """
        returns header as GlobalSection
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
    def IsParamDefined(self,num : int,nump : int) -> bool: 
        """
        Returns True if parameter "nump" of record "num" is defined (it is not if its type is ParamVoid)
        """
    def NbEntities(self) -> int: 
        """
        Returns count of recorded Entities (i.e. size of Directory)
        """
    def NbParams(self,num : int) -> int: 
        """
        Returns count of parameters attached to record "num" If <num> = 0, returns the total recorded count of parameters
        """
    def NbRecords(self) -> int: 
        """
        Returns the count of registered records That is, value given for Initialization (can be redefined)
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
    def ResetErrorLoad(self) -> bool: 
        """
        Returns the former value of status "Error Load" then resets it Used to read the status then ensure it is reset
        """
    def SetDefaultLineWeight(self,defw : float) -> None: 
        """
        allows to set a default line weight, will be later applied at load time, on Entities which have no specified line weight
        """
    def SetDirPart(self,num : int,i1 : int,i2 : int,i3 : int,i4 : int,i5 : int,i6 : int,i7 : int,i8 : int,i9 : int,i10 : int,i11 : int,i12 : int,i13 : int,i14 : int,i15 : int,i16 : int,i17 : int,res1 : str,res2 : str,label : str,subs : str) -> None: 
        """
        fills a DirPart, designated by its rank (that is, (N+1)/2 if N is its first number in section D)
        """
    def SetEntityNumbers(self) -> None: 
        """
        determines reference numbers in EntityNumber fields (called by SetEntities from IGESReaderTool) works on "Integer" type Parameters, because IGES does not distinguish Integer and Entity Refs : every Integer which is odd and less than twice NbRecords can be an Entity Ref ... (Ref Number is then (N+1)/2 if N is the Integer Value)
        """
    def SetErrorLoad(self,val : bool) -> None: 
        """
        Sets the status "Error Load" on, to overside check fails <val> True : declares unloaded <val> False : declares loaded If not called before loading (see FileReaderTool), check fails give the status IsErrorLoad says if SetErrorLoad has been called by user ResetErrorLoad resets it (called by FileReaderTool) This allows to specify that the currently loaded entity remains unloaded (because of syntactic fail)
        """
    def SetGlobalSection(self) -> None: 
        """
        reads header (as GlobalSection) content from the ParamSet after it has been filled by successive calls to AddGlobal
        """
    def SetParam(self,num : int,nump : int,FP : OCP.Interface.Interface_FileParameter) -> None: 
        """
        Sets a new value for a parameter of a record, given by : num : record number; nump : parameter number in the record
        """
    def StartSection(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the Start Section in once
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,nbe : int,nbp : int) -> None: ...
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
class IGESData_IGESReaderTool(OCP.Interface.Interface_FileReaderTool):
    """
    specific FileReaderTool for IGES Parameters are accessed through specific objects, ParamReaders
    """
    def AnalyseRecord(self,num : int,anent : OCP.Standard.Standard_Transient,acheck : OCP.Interface.Interface_Check) -> bool: 
        """
        fills an entity, given record no; works by calling ReadDirPart then ReadParams (with help of a ParamReader), then if required ReadProps and ReadAssocs, from IGESEntity Returns True if no fail has been recorded
        """
    def BeginRead(self,amodel : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        fills model's header, that is, its GlobalSection
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
        after reading entities, true line weights can be computed
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
    def Prepare(self,reco : IGESData_FileRecognizer) -> None: 
        """
        binds empty entities to records, works with the Protocol (from IGESData) stored and later used RQ : Actually, sets DNum into IGES Entities Also loads the list of parameters for ParamReader
        """
    def Protocol(self) -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Protocol given at creation time
        """
    def ReadAssocs(self,ent : IGESData_IGESEntity,IR : IGESData_IGESReaderData,PR : IGESData_ParamReader) -> None: 
        """
        Reads Associativity List, if there is (if not, does nothing) criterium is : current parameter of PR remains inside params list, and Stage is "Own" Same conditions as above; in addition, no parameter must be let after the list once read Note that "Associated" entities are not declared "Shared"
        """
    def ReadDir(self,ent : IGESData_IGESEntity,IR : IGESData_IGESReaderData,DP : IGESData_DirPart,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Reads directory part componants from file; DP is the litteral directory part, IR detains entities referenced by DP
        """
    def ReadOwnParams(self,ent : IGESData_IGESEntity,IR : IGESData_IGESReaderData,PR : IGESData_ParamReader) -> None: 
        """
        Performs Reading of own Parameters for each IGESEntity Works with the ReaderLib loaded with ReadWriteModules for IGES In case of failure, tries UndefinedEntity from IGES
        """
    def ReadProps(self,ent : IGESData_IGESEntity,IR : IGESData_IGESReaderData,PR : IGESData_ParamReader) -> None: 
        """
        Reads Property List, if there is (if not, does nothing) criterium is : current parameter of PR remains inside params list, and Stage is "Own" Current parameter must be a positive integer, which value gives the length of the list; else, a Fail is produced (into Check of PR) and reading process is stopped
        """
    def Recognize(self,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        recognizes records by asking Protocol (on data of DirType)
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
    def __init__(self,reader : IGESData_IGESReaderData,protocol : IGESData_Protocol) -> None: ...
    pass
class IGESData_IGESType():
    """
    taken from directory part of an entity (from file or model), gives "type" and "form" data, used to recognize entity's type
    """
    def Form(self) -> int: 
        """
        returns "form" data
        """
    def IsEqual(self,another : IGESData_IGESType) -> bool: 
        """
        compares two IGESTypes, avoiding comparing their fields
        """
    def Nullify(self) -> None: 
        """
        resets fields (usefull when an IGESType is stored as mask)
        """
    def Type(self) -> int: 
        """
        returns "type" data
        """
    @overload
    def __init__(self,atype : int,aform : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IGESData_IGESWriter():
    """
    manages atomic file writing, under control of IGESModel : prepare text to be sent then sends it takes into account distinction between successive Sections
    """
    def Associativities(self,anent : IGESData_IGESEntity) -> None: 
        """
        sends associativity list, as complement of parameters list error if not in sections DP or Stage not "Associativity"
        """
    def DirPart(self,anent : IGESData_IGESEntity) -> None: 
        """
        translates directory part of an Entity into a litteral DirPart Some infos are computed after sending parameters Error if not in sections DP or Stage not "Dir"
        """
    def EndEntity(self) -> None: 
        """
        declares end of sending an entity (ends param list by ';')
        """
    def FloatWriter(self) -> OCP.Interface.Interface_FloatWriter: 
        """
        Returns the embedded FloatWriter, which controls sending Reals Use this method to access FloatWriter in order to consult or change its options (MainFormat, FormatForRange,ZeroSuppress), because it is returned as the address of its field
        """
    def OwnParams(self,anent : IGESData_IGESEntity) -> None: 
        """
        sends own parameters of the entity, by sending firstly its type, then calling specific method WriteOwnParams Error if not in sections DP or Stage not "Own"
        """
    def Print(self,S : Any) -> bool: 
        """
        Writes result on an output defined as an OStream resolves stored infos at this time; in particular, numbers of lines used to adress P-section from D-section and final totals Takes WriteMode into account
        """
    def Properties(self,anent : IGESData_IGESEntity) -> None: 
        """
        sends property list, as complement of parameters list error if not in sections DP or Stage not "Property"
        """
    def SectionG(self,header : IGESData_GlobalSection) -> None: 
        """
        prepares sending of header, from a GlobalSection (stores it) error if SectionS was not called just before takes in account special characters (Separator, EndMark)
        """
    def SectionS(self) -> None: 
        """
        declares sending of S section (only a declaration) error if state is not initial
        """
    def SectionStrings(self,numsec : int) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the list of strings for a section given its rank 1 : Start (if not empty) 2 : Global 3 or 4 : Parameters RQ: no string list for Directory section An empty section gives a null handle
        """
    def SectionT(self) -> None: 
        """
        declares sending of T section (only a declaration) error if does not follow Entities sending
        """
    def SectionsDP(self) -> None: 
        """
        prepares sending of list of entities, as Sections D (directory list) and P (Parameters lists, one per entity) Entities will be then processed, one after the other error if SectionG has not be called just before
        """
    @overload
    def Send(self,val : OCP.gp.gp_XYZ) -> None: 
        """
        sends an Integer parameter

        sends a Real parameter. Works with FloatWriter

        sends a Text parameter under Hollerith form

        sends a Reference to an Entity (if its Number is N, its pointer is 2*N-1) If <val> is Null, "0" will be sent If <negative> is True, "Pointer" is sent as negative

        Sends a XY, interpreted as a couple of 2 Reals (X & Y)

        Sends a XYZ, interpreted as a couple of 2 Reals (X , Y & Z)
        """
    @overload
    def Send(self,val : int) -> None: ...
    @overload
    def Send(self,val : OCP.gp.gp_XY) -> None: ...
    @overload
    def Send(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    @overload
    def Send(self,val : IGESData_IGESEntity,negative : bool=False) -> None: ...
    @overload
    def Send(self,val : float) -> None: ...
    def SendBoolean(self,val : bool) -> None: 
        """
        sends a Boolean parameter as an Integer value 0(False)/1(True)
        """
    def SendModel(self,protocol : IGESData_Protocol) -> None: 
        """
        Sends the complete IGESModel (Global Section, Entities as Directory Entries & Parameter Lists, etc...) i.e. fills a list of texts. Once filled, it can be sent by method Print
        """
    def SendStartLine(self,startline : str) -> None: 
        """
        Sends an additionnal Starting Line : this is the way used to send comments in an IGES File (at beginning of the file). If the line is more than 72 char.s long, it is splited into as many lines as required to send it completely
        """
    def SendString(self,val : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        sends a parameter under its exact form given as a string
        """
    def SendVoid(self) -> None: 
        """
        sends a void parameter, that is null text
        """
    @overload
    def __init__(self,other : IGESData_IGESWriter) -> None: ...
    @overload
    def __init__(self,amodel : IGESData_IGESModel) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @property
    def WriteMode(self) -> int:
        """
        :type: int
        """
    @WriteMode.setter
    def WriteMode(self, arg1: int) -> None:
        pass
    pass
class IGESData_LabelDisplayEntity(IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines required type for LabelDisplay in directory part an effective LabelDisplay entity must inherits itdefines required type for LabelDisplay in directory part an effective LabelDisplay entity must inherits itdefines required type for LabelDisplay in directory part an effective LabelDisplay entity must inherits it
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        Returns true if a subscript number is defined. A subscript number is an integer used to identify a label.
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
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
class IGESData_LevelListEntity(IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines required type for LevelList in directory part an effective LevelList entity must inherits itdefines required type for LevelList in directory part an effective LevelList entity must inherits itdefines required type for LevelList in directory part an effective LevelList entity must inherits it
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasLevelNumber(self,level : int) -> bool: 
        """
        returns True if <level> is in the list
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        Returns true if a subscript number is defined. A subscript number is an integer used to identify a label.
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LevelNumber(self,num : int) -> int: 
        """
        returns the Level Number of <me>, indicated by <num> raises an exception if num is out of range
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbLevelNumbers(self) -> int: 
        """
        Must return the count of levels
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
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
class IGESData_LineFontEntity(IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines required type for LineFont in directory part an effective LineFont entity must inherits itdefines required type for LineFont in directory part an effective LineFont entity must inherits itdefines required type for LineFont in directory part an effective LineFont entity must inherits it
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        Returns true if a subscript number is defined. A subscript number is an integer used to identify a label.
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
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
class IGESData_NameEntity(IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    a NameEntity is a kind of IGESEntity which can provide a Name under alphanumeric (String) form, from Properties list an effective Name entity must inherit ita NameEntity is a kind of IGESEntity which can provide a Name under alphanumeric (String) form, from Properties list an effective Name entity must inherit ita NameEntity is a kind of IGESEntity which can provide a Name under alphanumeric (String) form, from Properties list an effective Name entity must inherit it
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        Returns true if a subscript number is defined. A subscript number is an integer used to identify a label.
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def Value(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Retyrns the alphanumeric value of the Name, to be defined
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
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
class IGESData_NodeOfSpecificLib(OCP.Standard.Standard_Transient):
    def AddNode(self,anode : IGESData_GlobalNodeOfSpecificLib) -> None: 
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
    def Module(self) -> IGESData_SpecificModule: 
        """
        Returns the Module designated by a precise Node
        """
    def Next(self) -> IGESData_NodeOfSpecificLib: 
        """
        Returns the Next Node. If none was defined, returned value is a Null Handle
        """
    def Protocol(self) -> IGESData_Protocol: 
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
class IGESData_NodeOfWriterLib(OCP.Standard.Standard_Transient):
    def AddNode(self,anode : IGESData_GlobalNodeOfWriterLib) -> None: 
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
    def Module(self) -> IGESData_ReadWriteModule: 
        """
        Returns the Module designated by a precise Node
        """
    def Next(self) -> IGESData_NodeOfWriterLib: 
        """
        Returns the Next Node. If none was defined, returned value is a Null Handle
        """
    def Protocol(self) -> IGESData_Protocol: 
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
class IGESData_ParamCursor():
    """
    Auxiliary class for ParamReader. It stores commands for a ParamReader to manage the current parameter number. Used by methods Read... from ParamReader. It allows to define the following commands : - read a parameter specified by a precise Number (basic case) - read a parameter then set Current Number to follow its number - read the current parameter (with Current Number) then advance Current Number by one - idem with several : read "nb" parameters from one specified, included, with or without setting Current Number to follow last parameter read - read several parameter from the current one, then advance Current Number to follow the last one read - Read several parameters (as above) but in interlaced lists, i.e. from complex items (each one including successively for instance, an Integer, a Real, an Entity ...)
    """
    def Advance(self) -> bool: 
        """
        Returns True if Advance command has been set

        Returns True if Advance command has been set
        """
    def Count(self) -> int: 
        """
        Returns required count of items to be read

        Returns required count of items to be read
        """
    def ItemSize(self) -> int: 
        """
        Returns length of item (count of parameters per item)

        Returns length of item (count of parameters per item)
        """
    def Limit(self) -> int: ...
    def Offset(self) -> int: 
        """
        Returns offset from which current term must be read in item

        Returns offset from which current term must be read in item
        """
    def SetAdvance(self,advance : bool) -> None: 
        """
        Changes command to advance current cursor after reading parameters. If "advance" True, sets advance, if "False", resets it. ParamCursor is created by default with True.
        """
    def SetOne(self,autoadv : bool=True) -> None: 
        """
        Defines a term of one Parameter (very current case)
        """
    def SetTerm(self,size : int,autoadv : bool=True) -> None: 
        """
        Defines the size of a term to read in the item : this commands ParamReader to read "size" parameters for each item, then skip the remainder of the item to the same term of next Item (that is, skip "item size" - "term size")
        """
    def SetXY(self,autoadv : bool=True) -> None: 
        """
        Defines a term of two Parameters for a XY (current case)
        """
    def SetXYZ(self,autoadv : bool=True) -> None: 
        """
        Defines a term of three Parameters for XYZ (current case)
        """
    def Start(self) -> int: ...
    def TermSize(self) -> int: 
        """
        Returns length of current term (count of parameters) in item

        Returns length of current term (count of parameters) in item
        """
    @overload
    def __init__(self,num : int) -> None: ...
    @overload
    def __init__(self,num : int,nb : int,size : int=1) -> None: ...
    pass
class IGESData_ParamReader():
    """
    access to a list of parameters, with management of read stage (owned parameters, properties, associativities) and current parameter number, read errors (which feed a Check), plus convenient facilities to read parameters, in particular : - first parameter is ignored (it repeats entity type), hence number 1 gives 2nd parameter, etc... - lists are not explicit, list-reading methods are provided which manage a current param. number - interpretation is made as possible (texts, reals, entities ...) (in particular, Reading a Real accepts an Integer)
    """
    @overload
    def AddFail(self,afail : str,bfail : str='') -> None: 
        """
        None

        feeds the Check with a new fail (as a String or as a CString)
        """
    @overload
    def AddFail(self,af : OCP.TCollection.TCollection_HAsciiString,bf : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    @overload
    def AddWarning(self,awarn : str,bwarn : str='') -> None: 
        """
        None

        feeds the Check with a new Warning message
        """
    @overload
    def AddWarning(self,aw : OCP.TCollection.TCollection_HAsciiString,bw : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def CCheck(self) -> OCP.Interface.Interface_Check: 
        """
        returns the check in a way which allows to work on it directly (i.e. messages added to the Check are added to ParamReader too)
        """
    def Check(self) -> OCP.Interface.Interface_Check: 
        """
        returns the Check Note that any error signaled above is also recorded into it
        """
    def Clear(self) -> None: 
        """
        resets state (stage, current param number, check with no fail)
        """
    def Current(self) -> IGESData_ParamCursor: 
        """
        Creates a ParamCursor from the Current Number, to read one parameter, and to advance Current Number after reading
        """
    def CurrentList(self,nb : int,size : int=1) -> IGESData_ParamCursor: 
        """
        Creates a ParamCursor from the Current Number, to read a list of "nb" items, and to advance Current Number after reading By default, each item is made of one parameter If size is given, it precises the number of params per item
        """
    def CurrentNumber(self) -> int: 
        """
        returns the current parameter number This notion is involved by the organisation of an IGES list of parameter : it can be ended by two lists (Associativities and Properties), which can be empty, or even absent. Hence, it is necessary to know, at the end of specific reading, how many parameters have been read : the optionnal lists follow
        """
    def DefinedElseSkip(self) -> bool: 
        """
        Allows to simply process a parameter which can be defaulted. Waits on the Current Number a defined parameter or skips it : If the parameter <num> is defined, changes nothing and returns True Hence, the next reading with current cursor will concern <num> If it is void, advances Current Position by one, and returns False The next reading will concern <num+1> (except if <num> = NbParams)
        """
    def EndAll(self) -> None: 
        """
        passes directly to the end of reading process
        """
    def EntityNumber(self) -> int: 
        """
        Returns the entity number in the file
        """
    def HasFailed(self) -> bool: 
        """
        says if fails have been recorded into the Check
        """
    def IsCheckEmpty(self) -> bool: 
        """
        Returns True if the Check is Empty Else, it has to be recorded with the Read Entity
        """
    def IsParamDefined(self,num : int) -> bool: 
        """
        says if a parameter is defined (not void) See also DefinedElseSkip
        """
    def IsParamEntity(self,num : int) -> bool: 
        """
        says if a parameter can be regarded as an entity reference (see Prepare from IGESReaderData for more explanation) Note that such a parameter can seen as be a plain Integer too
        """
    def Mend(self,pref : str='') -> None: 
        """
        None
        """
    def NbParams(self) -> int: 
        """
        returns number of parameters (minus the first one) following method skip the first parameter (1 gives the 2nd)
        """
    def NextStage(self) -> None: 
        """
        passes to next stage (must be linked with setting Current)
        """
    def ParamEntity(self,IR : IGESData_IGESReaderData,num : int) -> IGESData_IGESEntity: 
        """
        directly returns entity referenced by a parameter
        """
    def ParamNumber(self,num : int) -> int: 
        """
        returns entity number corresponding to a parameter if there is otherwise zero (according criterium IsParamEntity)
        """
    def ParamType(self,num : int) -> OCP.Interface.Interface_ParamType: 
        """
        returns type of parameter; note that "Ident" or "Sub" cannot be encountered, they correspond to "Integer", see also below
        """
    def ParamValue(self,num : int) -> str: 
        """
        returns litteral value of a parameter, as it was in file
        """
    @overload
    def ReadBoolean(self,PC : IGESData_ParamCursor,mess : str,val : bool,exact : bool=True) -> bool: 
        """
        None

        Reads a Boolean value from parameter "num" A Boolean is given as an Integer value 0 (False) or 1 (True) Anyway, an Integer is demanded (else, Check is filled) If exact is given True, those precise values are demanded Else, Correction is done, as False for 0 or <0, True for >0 (with a Warning error message, and return is True) In case of error (not an Integer, or not 0/1 and exact True), Check is filled with a Fail (using mess) and return is False
        """
    @overload
    def ReadBoolean(self,PC : IGESData_ParamCursor,amsg : OCP.Message.Message_Msg,val : bool,exact : bool=True) -> bool: ...
    @overload
    def ReadEntList(self,IR : IGESData_IGESReaderData,PC : IGESData_ParamCursor,amsg : OCP.Message.Message_Msg,val : OCP.Interface.Interface_EntityList,ord : bool=True) -> bool: 
        """
        None

        Reads a list of Entities defined by PC Same conditions as for ReadEnts, for PC The list is given as an EntityList (index has no meaning; the EntityList starts from clear) If "ord" is given True (default), entities will be added to the list in their original order Remark : Negative or Null Pointers are ignored Else ("ord" False), order is not garanteed (faster mode) If all params cannot be read as Entities, same as above Warning Give "ord" to False ONLY if order is not significant
        """
    @overload
    def ReadEntList(self,IR : IGESData_IGESReaderData,PC : IGESData_ParamCursor,mess : str,val : OCP.Interface.Interface_EntityList,ord : bool=True) -> bool: ...
    @overload
    def ReadEntity(self,IR : IGESData_IGESReaderData,PC : IGESData_ParamCursor,mess : str,val : IGESData_IGESEntity,canbenul : bool=False) -> bool: 
        """
        None

        Reads an IGES entity from parameter "num" An Entity is known by its reference, which has the form of an odd Integer Value (a number in the Directory) If <canbenul> is given True, a Reference can also be Null : in this case, the result is a Null Handle with no Error If <canbenul> is False, a Null Reference causes an Error If the parameter cannot refer to an entity (or null), fills Check with a Fail (using mess) and returns False

        None

        Works as ReadEntity without Type, but in addition checks the Type of the Entity, which must be "kind of" a given <type> Then, gives the same fail cases as ReadEntity without Type, plus the case "Incorrect Type" (in such a case, returns False and givel <val> = Null)
        """
    @overload
    def ReadEntity(self,IR : IGESData_IGESReaderData,PC : IGESData_ParamCursor,aStatus : IGESData_Status,type : OCP.Standard.Standard_Type,val : IGESData_IGESEntity,canbenul : bool=False) -> bool: ...
    @overload
    def ReadEntity(self,IR : IGESData_IGESReaderData,PC : IGESData_ParamCursor,mess : str,type : OCP.Standard.Standard_Type,val : IGESData_IGESEntity,canbenul : bool=False) -> bool: ...
    @overload
    def ReadEntity(self,IR : IGESData_IGESReaderData,PC : IGESData_ParamCursor,aStatus : IGESData_Status,val : IGESData_IGESEntity,canbenul : bool=False) -> bool: ...
    @overload
    def ReadEnts(self,IR : IGESData_IGESReaderData,PC : IGESData_ParamCursor,amsg : OCP.Message.Message_Msg,val : IGESData_HArray1OfIGESEntity,index : int=1) -> bool: 
        """
        None

        Reads a list of Entities defined by PC Same conditions as for ReadInts, for PC and index The list is given as a HArray1, numered from "index" If all params cannot be read as Entities, Check is filled (using mess) and return value is False Remark : Null references are accepted, they are ignored (negative pointers too : they provoke a Warning message) If the caller wants to check them, a loop on ReadEntity should be used
        """
    @overload
    def ReadEnts(self,IR : IGESData_IGESReaderData,PC : IGESData_ParamCursor,mess : str,val : IGESData_HArray1OfIGESEntity,index : int=1) -> bool: ...
    @overload
    def ReadInteger(self,PC : IGESData_ParamCursor,mess : str,val : int) -> bool: 
        """
        None

        Reads an Integer value designated by PC The method Current designates the current parameter and advances the Current Number by one after reading Note that if a count (not 1) is given, it is ignored If it is not an Integer, fills Check with a Fail (using mess) and returns False
        """
    @overload
    def ReadInteger(self,PC : IGESData_ParamCursor,val : int) -> bool: ...
    @overload
    def ReadInts(self,PC : IGESData_ParamCursor,mess : str,val : OCP.TColStd.TColStd_HArray1OfInteger,index : int=1) -> bool: 
        """
        None

        Reads a list of Integer values, defined by PC (with a count of parameters). PC can start from Current Number and command it to advance after reading (use method CurrentList to do this) The list is given as a HArray1, numered from "index" If all params are not Integer, Check is filled (using mess) and return value is False
        """
    @overload
    def ReadInts(self,PC : IGESData_ParamCursor,amsg : OCP.Message.Message_Msg,val : OCP.TColStd.TColStd_HArray1OfInteger,index : int=1) -> bool: ...
    @overload
    def ReadReal(self,PC : IGESData_ParamCursor,mess : str,val : float) -> bool: 
        """
        None

        Reads a Real value from parameter "num" An Integer is accepted (Check is filled with a Warning message) and causes return to be True (as normal case) In other cases, Check is filled with a Fail and return is False
        """
    @overload
    def ReadReal(self,PC : IGESData_ParamCursor,val : float) -> bool: ...
    @overload
    def ReadReals(self,PC : IGESData_ParamCursor,amsg : OCP.Message.Message_Msg,val : OCP.TColStd.TColStd_HArray1OfReal,index : int=1) -> bool: 
        """
        None

        Reads a list of Real values defined by PC Same conditions as for ReadInts, for PC and index An Integer parameter is accepted, if at least one parameter is Integer, Check is filled with a "Warning" message If all params are neither Real nor Integer, Check is filled (using mess) and return value is False
        """
    @overload
    def ReadReals(self,PC : IGESData_ParamCursor,mess : str,val : OCP.TColStd.TColStd_HArray1OfReal,index : int=1) -> bool: ...
    @overload
    def ReadText(self,PC : IGESData_ParamCursor,mess : str,val : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        None

        Reads a Text value from parameter "num", as a String from Collection, that is, Hollerith text without leading "nnnH" If it is not a String, fills Check with a Fail (using mess) and returns False
        """
    @overload
    def ReadText(self,PC : IGESData_ParamCursor,amsg : OCP.Message.Message_Msg,val : OCP.TCollection.TCollection_HAsciiString) -> bool: ...
    @overload
    def ReadTexts(self,PC : IGESData_ParamCursor,mess : str,val : OCP.Interface.Interface_HArray1OfHAsciiString,index : int=1) -> bool: 
        """
        None

        Reads a list of Hollerith Texts, defined by PC Texts are read as Hollerith texts without leading "nnnH" Same conditions as for ReadInts, for PC and index If all params are not Text, Check is filled (using mess) and return value is False
        """
    @overload
    def ReadTexts(self,PC : IGESData_ParamCursor,amsg : OCP.Message.Message_Msg,val : OCP.Interface.Interface_HArray1OfHAsciiString,index : int=1) -> bool: ...
    @overload
    def ReadXY(self,PC : IGESData_ParamCursor,mess : str,val : OCP.gp.gp_XY) -> bool: 
        """
        None

        Reads a couple of Real values (X,Y) from parameter "num" Integers are accepted (Check is filled with a Warning message) and cause return to be True (as normal case) In other cases, Check is filled with a Fail and return is False
        """
    @overload
    def ReadXY(self,PC : IGESData_ParamCursor,amsg : OCP.Message.Message_Msg,val : OCP.gp.gp_XY) -> bool: ...
    @overload
    def ReadXYZ(self,PC : IGESData_ParamCursor,amsg : OCP.Message.Message_Msg,val : OCP.gp.gp_XYZ) -> bool: 
        """
        None

        Reads a triplet of Real values (X,Y,Z) from parameter "num" Integers are accepted (Check is filled with a Warning message) and cause return to be True (as normal case) In other cases, Check is filled with a Fail and return is False For Message
        """
    @overload
    def ReadXYZ(self,PC : IGESData_ParamCursor,mess : str,val : OCP.gp.gp_XYZ) -> bool: ...
    @overload
    def ReadingEntityNumber(self,num : int,mess : str,val : int) -> bool: 
        """
        None

        Routine which reads an Entity Number (which allows to read the Entity in the IGESReaderData by BoundEntity), given its number in the list of Parameters Same conditions as ReadEntity for mess, val, and return value In particular, returns True and val to zero means Null Entity, and val not zero means Entity read by BoundEntity
        """
    @overload
    def ReadingEntityNumber(self,num : int,val : int) -> bool: ...
    @overload
    def ReadingReal(self,num : int,val : float) -> bool: 
        """
        None

        Routine which reads a Real parameter, given its number Same conditions as ReadReal for mess, val, and return value
        """
    @overload
    def ReadingReal(self,num : int,mess : str,val : float) -> bool: ...
    def SendFail(self,amsg : OCP.Message.Message_Msg) -> None: 
        """
        None
        """
    def SendWarning(self,amsg : OCP.Message.Message_Msg) -> None: 
        """
        None
        """
    def SetCurrentNumber(self,num : int) -> None: 
        """
        sets current parameter number to a new value must be done at end of each step : set on first parameter following last read one; is done by some Read... methods (must be done directly if these method are not used) num greater than NbParams means that following lists are empty If current num is not managed, it remains at 1, which probably will cause error when successive steps of reading are made
        """
    def Stage(self) -> IGESData_ReadStage: 
        """
        gives current stage (Own-Props-Assocs-End, begins at Own)
        """
    def __init__(self,list : OCP.Interface.Interface_ParamList,ach : OCP.Interface.Interface_Check,base : int=1,nbpar : int=0,num : int=0) -> None: ...
    pass
class IGESData_FileProtocol(IGESData_Protocol, OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    This class allows to define complex protocols, in order to treat various sub-sets (or the complete set) of the IGES Norm, such as Solid + Draw (which are normally independant), etc... While it inherits Protocol from IGESData, it admits UndefinedEntity tooThis class allows to define complex protocols, in order to treat various sub-sets (or the complete set) of the IGES Norm, such as Solid + Draw (which are normally independant), etc... While it inherits Protocol from IGESData, it admits UndefinedEntity tooThis class allows to define complex protocols, in order to treat various sub-sets (or the complete set) of the IGES Norm, such as Solid + Draw (which are normally independant), etc... While it inherits Protocol from IGESData, it admits UndefinedEntity too
    """
    @staticmethod
    def Active_s() -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Active Protocol, if defined (else, returns a Null Handle, which means "no defined active protocol")
        """
    def Add(self,protocol : IGESData_Protocol) -> None: 
        """
        Adds a resource
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
    def GlobalCheck(self,G : OCP.Interface.Interface_Graph,ach : OCP.Interface.Interface_Check) -> bool: 
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
    def IsSuitableModel(self,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True if <model> is a Model of IGES Norm
        """
    def IsUnknownEntity(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e. Type UndefinedEntity, status Unknown
        """
    def NbResources(self) -> int: 
        """
        Gives the count of Resources : the count of Added Protocols
        """
    def NbTypes(self,obj : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns the count of DISTINCT types under which an entity may be processed. Each one is candidate to be recognized by TypeNumber, <obj> is then processed according it By default, returns 1 (the DynamicType)
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Creates an empty Model for IGES Norm
        """
    def Resource(self,num : int) -> OCP.Interface.Interface_Protocol: 
        """
        Returns a Resource, given a rank (rank of call to Add)
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
        Returns a Case Number, specific of each recognized Type Here, Undefined and Free Format Entities have the Number 1.
        """
    def UnknownEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Creates a new Unknown Entity for IGES (UndefinedEntity)
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
class IGESData_ReadStage():
    """
    gives successive stages of reading an entity (see ParamReader)

    Members:

      IGESData_ReadDir

      IGESData_ReadOwn

      IGESData_ReadAssocs

      IGESData_ReadProps

      IGESData_ReadEnd
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IGESData_ReadAssocs: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadAssocs
    IGESData_ReadDir: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadDir
    IGESData_ReadEnd: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadEnd
    IGESData_ReadOwn: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadOwn
    IGESData_ReadProps: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadProps
    __entries: dict # value = {'IGESData_ReadDir': (IGESData_ReadStage.IGESData_ReadDir, None), 'IGESData_ReadOwn': (IGESData_ReadStage.IGESData_ReadOwn, None), 'IGESData_ReadAssocs': (IGESData_ReadStage.IGESData_ReadAssocs, None), 'IGESData_ReadProps': (IGESData_ReadStage.IGESData_ReadProps, None), 'IGESData_ReadEnd': (IGESData_ReadStage.IGESData_ReadEnd, None)}
    __members__: dict # value = {'IGESData_ReadDir': IGESData_ReadStage.IGESData_ReadDir, 'IGESData_ReadOwn': IGESData_ReadStage.IGESData_ReadOwn, 'IGESData_ReadAssocs': IGESData_ReadStage.IGESData_ReadAssocs, 'IGESData_ReadProps': IGESData_ReadStage.IGESData_ReadProps, 'IGESData_ReadEnd': IGESData_ReadStage.IGESData_ReadEnd}
    pass
class IGESData_ReadWriteModule(OCP.Interface.Interface_ReaderModule, OCP.Standard.Standard_Transient):
    """
    Defines basic File Access Module, under the control of IGESReaderTool for Reading and IGESWriter for Writing : Specific actions concern : Read and Write Own Parameters of an IGESEntity. The common parts (Directory Entry, Lists of Associativities and Properties) are processed by IGESReaderTool & IGESWriterDefines basic File Access Module, under the control of IGESReaderTool for Reading and IGESWriter for Writing : Specific actions concern : Read and Write Own Parameters of an IGESEntity. The common parts (Directory Entry, Lists of Associativities and Properties) are processed by IGESReaderTool & IGESWriterDefines basic File Access Module, under the control of IGESReaderTool for Reading and IGESWriter for Writing : Specific actions concern : Read and Write Own Parameters of an IGESEntity. The common parts (Directory Entry, Lists of Associativities and Properties) are processed by IGESReaderTool & IGESWriter
    """
    def CaseIGES(self,typenum : int,formnum : int) -> int: 
        """
        Defines Case Numbers corresponding to the Entity Types taken into account by a sub-class of ReadWriteModule (hence, each sub-class of ReadWriteModule has to redefine this method) Called by CaseNum. Its result will then be used to call Read, etc ...
        """
    def CaseNum(self,data : OCP.Interface.Interface_FileReaderData,num : int) -> int: 
        """
        Translates the Type of record <num> in <data> to a positive Case Number, or 0 if failed. Works with IGESReaderData which provides Type & Form Numbers, and calls CaseIGES (see below)
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
    def NewRead(self,casenum : int,data : OCP.Interface.Interface_FileReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific operator (create+read) defaulted to do nothing. It can be redefined when it is not possible to work in two steps (NewVoid then Read). This occurs when no default constructor is defined : hence the result <ent> must be created with an effective definition from the reader. Remark : if NewRead is defined, Copy has nothing to do.
        """
    def Read(self,CN : int,data : OCP.Interface.Interface_FileReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.Standard.Standard_Transient) -> Any: 
        """
        General Read Function. See IGESReaderTool for more info
        """
    def ReadOwnParams(self,CN : int,ent : IGESData_IGESEntity,IR : IGESData_IGESReaderData,PR : IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file for an Entity; <PR> gives access to them, <IR> detains parameter types and values For each class, there must be a specific action provided Note that Properties and Associativities Lists are Read by specific methods (see below), they are called under control of reading process (only one call) according Stage recorded in ParamReader
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteOwnParams(self,CN : int,ent : IGESData_IGESEntity,IW : IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter; defined for each class (to be redefined for other IGES ReadWriteModules) Warning : Properties and Associativities are directly managed by WriteIGES, must not be sent by this method
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
class IGESData_SingleParentEntity(IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    a SingleParentEntity is a kind of IGESEntity which can refer to a (Single) Parent, from Associativities list of an Entity a effective SingleParent definition entity must inherit ita SingleParentEntity is a kind of IGESEntity which can refer to a (Single) Parent, from Associativities list of an Entity a effective SingleParent definition entity must inherit ita SingleParentEntity is a kind of IGESEntity which can refer to a (Single) Parent, from Associativities list of an Entity a effective SingleParent definition entity must inherit it
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Child(self,num : int) -> IGESData_IGESEntity: 
        """
        Returns a Child given its rank
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        Returns true if a subscript number is defined. A subscript number is an integer used to identify a label.
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbChildren(self) -> int: 
        """
        Returns the count of Entities designated as children
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleParent(self) -> IGESData_IGESEntity: 
        """
        Returns the parent designated by the Entity, if only one !
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
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
class IGESData_SpecificLib():
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
    def Module(self) -> IGESData_SpecificModule: 
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
    def Protocol(self) -> IGESData_Protocol: 
        """
        Returns the current Protocol in the Iteration
        """
    def Select(self,obj : IGESData_IGESEntity,module : IGESData_SpecificModule,CN : int) -> bool: 
        """
        Selects a Module from the Library, given an Object. Returns True if Select has succeeded, False else. Also Returns (as arguments) the selected Module and the Case Number determined by the associated Protocol. If Select has failed, <module> is Null Handle and CN is zero. (Select can work on any criterium, such as Object DynamicType)
        """
    def SetComplete(self) -> None: 
        """
        Sets a library to be defined with the complete Global list (all the couples Protocol/Modules recorded in it)
        """
    @staticmethod
    def SetGlobal_s(amodule : IGESData_SpecificModule,aprotocol : IGESData_Protocol) -> None: 
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
    def __init__(self,aprotocol : IGESData_Protocol) -> None: ...
    pass
class IGESData_DefaultSpecific(IGESData_SpecificModule, OCP.Standard.Standard_Transient):
    """
    Specific IGES Services for UndefinedEntity, FreeFormatEntitySpecific IGES Services for UndefinedEntity, FreeFormatEntitySpecific IGES Services for UndefinedEntity, FreeFormatEntity
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
    def OwnCorrect(self,CN : int,ent : IGESData_IGESEntity) -> bool: 
        """
        Specific Automatic Correction on own Parameters of an Entity. It works by setting in accordance redundant data, if there are when there is no ambiguity (else, it does nothing). Remark that classic Corrections on Directory Entry (to set void data) are taken into account alsewhere.
        """
    def OwnDump(self,CN : int,ent : IGESData_IGESEntity,dumper : IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Specific Dump for UndefinedEntity : it concerns only own parameters, the general data (Directory Part, Lists) are taken into account by the IGESDumper
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
class IGESData_Status():
    """
    None

    Members:

      IGESData_EntityOK

      IGESData_EntityError

      IGESData_ReferenceError

      IGESData_TypeError
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IGESData_EntityError: OCP.IGESData.IGESData_Status # value = IGESData_Status.IGESData_EntityError
    IGESData_EntityOK: OCP.IGESData.IGESData_Status # value = IGESData_Status.IGESData_EntityOK
    IGESData_ReferenceError: OCP.IGESData.IGESData_Status # value = IGESData_Status.IGESData_ReferenceError
    IGESData_TypeError: OCP.IGESData.IGESData_Status # value = IGESData_Status.IGESData_TypeError
    __entries: dict # value = {'IGESData_EntityOK': (IGESData_Status.IGESData_EntityOK, None), 'IGESData_EntityError': (IGESData_Status.IGESData_EntityError, None), 'IGESData_ReferenceError': (IGESData_Status.IGESData_ReferenceError, None), 'IGESData_TypeError': (IGESData_Status.IGESData_TypeError, None)}
    __members__: dict # value = {'IGESData_EntityOK': IGESData_Status.IGESData_EntityOK, 'IGESData_EntityError': IGESData_Status.IGESData_EntityError, 'IGESData_ReferenceError': IGESData_Status.IGESData_ReferenceError, 'IGESData_TypeError': IGESData_Status.IGESData_TypeError}
    pass
class IGESData_ToolLocation(OCP.Standard.Standard_Transient):
    """
    This Tool determines and gives access to effective Locations of IGES Entities as defined by the IGES Norm. These Locations can be for each Entity : - on one part, explicitly defined by a Transf in Directory Part (this Transf can be itself compound); if not defined, no proper Transformation is defined - on the other part, implicitly defined by a reference from another Entity : its Parent Both implicit and explicit locations are combinable.This Tool determines and gives access to effective Locations of IGES Entities as defined by the IGES Norm. These Locations can be for each Entity : - on one part, explicitly defined by a Transf in Directory Part (this Transf can be itself compound); if not defined, no proper Transformation is defined - on the other part, implicitly defined by a reference from another Entity : its Parent Both implicit and explicit locations are combinable.This Tool determines and gives access to effective Locations of IGES Entities as defined by the IGES Norm. These Locations can be for each Entity : - on one part, explicitly defined by a Transf in Directory Part (this Transf can be itself compound); if not defined, no proper Transformation is defined - on the other part, implicitly defined by a reference from another Entity : its Parent Both implicit and explicit locations are combinable.
    """
    def AnalyseLocation(self,loc : OCP.gp.gp_GTrsf,result : OCP.gp.gp_Trsf) -> bool: 
        """
        Analysis a Location given as a GTrsf, by trying to convert it to a Trsf (i.e. to a True Location of which effect is described by an Isometry or a Similarity) Works with the Precision given by default or by SetPrecision Calls ConvertLocation (see below)
        """
    @staticmethod
    def ConvertLocation_s(prec : float,loc : OCP.gp.gp_GTrsf,result : OCP.gp.gp_Trsf,uni : float=1.0) -> bool: 
        """
        Convertion of a Location, from GTrsf form to Trsf form Works with a precision given as argument. Returns True if the Conversion is possible, (hence, <result> contains the converted location), False else <unit>, if given, indicates the unit in which <loc> is defined in meters. It concerns the translation part (to be converted.
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
    def EffectiveLocation(self,ent : IGESData_IGESEntity) -> OCP.gp.gp_GTrsf: 
        """
        Returns the effective Location of an Entity, i.e. the composition of its proper Transformation Matrix (returned by Transf) and its Parent's Location (returned by ParentLocation)
        """
    def ExplicitLocation(self,ent : IGESData_IGESEntity) -> OCP.gp.gp_GTrsf: 
        """
        Returns the Explicit Location defined by the Transformation Matrix of <ent>. Identity if there is none
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasParent(self,ent : IGESData_IGESEntity) -> bool: 
        """
        Returns True if <ent> is dependent from one and only one other Entity, either by Reference or by Associativity
        """
    def HasParentByAssociativity(self,ent : IGESData_IGESEntity) -> bool: 
        """
        Returns True if the Parent, if there is one, is defined by a SingleParentEntity Associativity Else, if HasParent is True, it is by Reference
        """
    def HasTransf(self,ent : IGESData_IGESEntity) -> bool: 
        """
        Returns True if <ent> has a Transformation Matrix in proper (referenced from its Directory Part)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAmbiguous(self,ent : IGESData_IGESEntity) -> bool: 
        """
        Returns True if more than one Parent has been determined for <ent>, by adding direct References and Associativities
        """
    def IsAssociativity(self,ent : IGESData_IGESEntity) -> bool: 
        """
        Returns True if <ent> is an Associativity (IGES Type 402). Then, Location does not apply.
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
    def IsTransf(self,ent : IGESData_IGESEntity) -> bool: 
        """
        Returns True if <ent> is kind of TransfEntity. Then, it has no location, while it can be used to define a Location)
        """
    def Load(self) -> None: 
        """
        Does the effective work of determining Locations of Entities
        """
    def Parent(self,ent : IGESData_IGESEntity) -> IGESData_IGESEntity: 
        """
        Returns the unique Parent recorded for <ent>. Returns a Null Handle if there is none
        """
    def ParentLocation(self,ent : IGESData_IGESEntity) -> OCP.gp.gp_GTrsf: 
        """
        Returns the effective Location of the Parent of <ent>, if there is one : this Location is itself given as compound according dependences on the Parent, if there are some. Returns an Identity Transformation if no Parent is recorded.
        """
    def ResetDependences(self,child : IGESData_IGESEntity) -> None: 
        """
        Resets all informations about dependences for <child>
        """
    def SetOwnAsDependent(self,ent : IGESData_IGESEntity) -> None: 
        """
        Unitary action which defines Entities referenced by <ent> (except those in Directory Part and Associativities List) as Dependent (their Locations are related to that of <ent>)
        """
    def SetParentAssoc(self,parent : IGESData_IGESEntity,child : IGESData_IGESEntity) -> None: 
        """
        Sets the "Associativity" information for <child> as being <parent> (it must be the Parent itself, not the Associativity)
        """
    def SetPrecision(self,prec : float) -> None: 
        """
        Sets a precision for the Analysis of Locations (default by constructor is 1.E-05)
        """
    def SetReference(self,parent : IGESData_IGESEntity,child : IGESData_IGESEntity) -> None: 
        """
        Sets the "Reference" information for <child> as being <parent> Sets an Error Status if already set (see method IsAmbiguous)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,amodel : IGESData_IGESModel,protocol : IGESData_Protocol) -> None: ...
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
class IGESData_TransfEntity(IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines required type for Transf in directory part an effective Transf entity must inherits itdefines required type for Transf in directory part an effective Transf entity must inherits itdefines required type for Transf in directory part an effective Transf entity must inherits it
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        Returns true if a subscript number is defined. A subscript number is an integer used to identify a label.
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def Value(self) -> OCP.gp.gp_GTrsf: 
        """
        gives value of the transformation, as a GTrsf To be defined by an effective class of Transformation Entity Warning : Must take in account Composition : if a TransfEntity has in its Directory Part, a Transf, this means that it is Compound, Value must return the global result
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
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
class IGESData_FreeFormatEntity(IGESData_UndefinedEntity, IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    This class allows to create IGES Entities in a literal form : their definition is free, but they are not recognized as instances of specific classes.This class allows to create IGES Entities in a literal form : their definition is free, but they are not recognized as instances of specific classes.This class allows to create IGES Entities in a literal form : their definition is free, but they are not recognized as instances of specific classes.
    """
    def AddEntities(self,ents : IGESData_HArray1OfIGESEntity) -> None: 
        """
        Adds a set of Entities, given as a HArray1OfIGESEntity Causes creation of : an Integer Parameter which gives count of Entities, then the list of Entities of the Array Error if an Entity is not an IGESEntity All these Entities will be interpreted as "Positive Pointers" by IGESWriter
        """
    def AddEntity(self,ptype : OCP.Interface.Interface_ParamType,ent : IGESData_IGESEntity,negative : bool=False) -> None: 
        """
        Adds a Parameter which references an Entity. If the Entity is Null, the added parameter will define a "Null Pointer" (0) If <negative> is given True, this will command Sending to File (see IGESWriter) to produce a "Negative Pointer" (Default is False)
        """
    @overload
    def AddLiteral(self,ptype : OCP.Interface.Interface_ParamType,val : str) -> None: 
        """
        Adds a literal Parameter to the list (as such)

        Adds a literal Parameter to the list (builds an HAsciiString)
        """
    @overload
    def AddLiteral(self,ptype : OCP.Interface.Interface_ParamType,val : OCP.TCollection.TCollection_HAsciiString) -> None: ...
    def AddNegativePointers(self,list : OCP.TColStd.TColStd_HSequenceOfInteger) -> None: 
        """
        Adds a list of Ranks of Parameters to be noted as Negative Pointers (this will be taken into account for Parameters which are Entities)
        """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def ChangeableContent(self) -> OCP.Interface.Interface_UndefinedContent: 
        """
        Returns own data as an UndefinedContent, in order to touch it
        """
    def ClearNegativePointers(self) -> None: 
        """
        Clears all informations about Negative Pointers, hence every Entity kind Parameter will be send normally, as Positive
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        returns Error status if necessary, else calls original method
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        returns Error status if necessary, else calls original method
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        returns Error status if necessary, else calls original method
        """
    def DefView(self) -> IGESData_DefList: 
        """
        returns Error status if necessary, else calls original method
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def DirStatus(self) -> int: 
        """
        returns Directory Error Status (used for Copy)
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        returns Error status if necessary, else calls original method (that is, if SubScript field is not blank or positive integer)
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def IsNegativePointer(self,num : int) -> bool: 
        """
        Returns True if <num> is noted as for a "Negative Pointer" (see AddEntity for details). Senseful only if IsParamEntity answers True for <num>, else returns False.
        """
    def IsOKDirPart(self) -> bool: 
        """
        says if DirPart is OK or not (if not, it is erroneous) Note that if it is not, Def* methods can return Error status
        """
    def IsParamEntity(self,num : int) -> bool: 
        """
        Returns True if a Parameter is recorded as an entity Error if num is not between 1 and NbParams
        """
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbParams(self) -> int: 
        """
        Gives count of recorded parameters
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def NegativePointers(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Returns the complete list of Ramks of Parameters which have been noted as Negative Pointers Warning : It is returned as a Null Handle if none was noted
        """
    def ParamData(self,num : int,ptype : OCP.Interface.Interface_ParamType,ent : IGESData_IGESEntity,val : OCP.TCollection.TCollection_HAsciiString) -> bool: 
        """
        Returns data of a Parameter : its type, and the entity if it designates en entity ("ent") or its literal value else ("str") Returned value (Boolean) : True if it is an Entity, False else
        """
    def ParamEntity(self,num : int) -> IGESData_IGESEntity: 
        """
        Returns Entity corresponding to a Param, given its rank Error if out of range or if Param num does not designate an Entity
        """
    def ParamType(self,num : int) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the ParamType of a Param, given its rank Error if num is not between 1 and NbParams
        """
    def ParamValue(self,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns litteral value of a Parameter, given its rank Error if num is out of range, or if Parameter is not literal
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def ReadDir(self,IR : IGESData_IGESReaderData,DP : IGESData_DirPart,ach : OCP.Interface.Interface_Check) -> bool: 
        """
        Computes the Directory Error Status, to be called before standard ReadDir from IGESReaderTool Returns True if OK (hence, Directory can be loaded), Else returns False and the DirPart <DP> is modified (hence, Directory Error Status is non null; and standard Read will work with an acceptable DirectoryPart)
        """
    def ReadOwnParams(self,IR : IGESData_IGESReaderData,PR : IGESData_ParamReader) -> None: 
        """
        reads own parameters from file; PR gives access to them, IR detains parameter types and values Here, reads all parameters, integers are considered as entity reference unless they cannot be; no list interpretation No property or associativity list is managed
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetFormNumber(self,formnum : int) -> None: 
        """
        Sets Form Number to a new Value (to called after SetTypeNumber)
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def SetNewContent(self,cont : OCP.Interface.Interface_UndefinedContent) -> None: 
        """
        Redefines a completely new UndefinedContent Used by a Copy which begins by ShallowCopy, for instance
        """
    def SetOKDirPart(self) -> None: 
        """
        Erases the Directory Error Status Warning : Be sure that data are consistent to call this method ...
        """
    def SetTypeNumber(self,typenum : int) -> None: 
        """
        Sets Type Number to a new Value, and Form Number to Zero
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UndefinedContent(self) -> OCP.Interface.Interface_UndefinedContent: 
        """
        Returns own data as an UndefinedContent
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
        """
    def WriteOwnParams(self,IW : IGESData_IGESWriter) -> None: 
        """
        WriteOwnParams is redefined for FreeFormatEntity to take into account the supplementary information "Negative Pointer"
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
class IGESData_ViewKindEntity(IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines required type for ViewKind in directory part that is, Single view or Multiple view An effective ViewKind entity must inherit it and define IsSingle (True for Single, False for List of Views), NbViews and ViewItem (especially for a List)defines required type for ViewKind in directory part that is, Single view or Multiple view An effective ViewKind entity must inherit it and define IsSingle (True for Single, False for List of Views), NbViews and ViewItem (especially for a List)defines required type for ViewKind in directory part that is, Single view or Multiple view An effective ViewKind entity must inherit it and define IsSingle (True for Single, False for List of Views), NbViews and ViewItem (especially for a List)
    """
    def AddProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArePresentAssociativities(self) -> bool: 
        """
        Returns True if the Entity is defined with an Associativity list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list.
        """
    def ArePresentProperties(self) -> bool: 
        """
        Returns True if the Entity is defined with a Property list, even empty (that is, file contains its length 0) Else, the file contained NO idencation at all about this list
        """
    def Associate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasShortLabel(self) -> bool: 
        """
        Returns true if a short label is defined. A short label is a non-blank 8-character string.
        """
    def HasStructure(self) -> bool: 
        """
        returns True if an IGESEntity is defined with a Structure (it is normally reserved for certain classes, such as Macros)
        """
    def HasSubScriptNumber(self) -> bool: 
        """
        Returns true if a subscript number is defined. A subscript number is an integer used to identify a label.
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitColor(self,ent : IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : IGESData_IGESEntity,lab : IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def IsSingle(self) -> bool: 
        """
        says if "me" is a Single View (True) or a List of Views (False)
        """
    def LabelDisplay(self) -> IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> IGESData_LineFontEntity: 
        """
        Returns LineFont as an Entity (if defined as Reference) Returns a Null Handle if DefLineFont is not "DefReference"
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightNumber(self) -> int: 
        """
        Returns the LineWeight Number (0 not defined), see also LineWeight
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def NbViews(self) -> int: 
        """
        Returns the count of Views for a List of Views. For a Single View, may return simply 1
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def ShortLabel(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the label value for this IGES entity as a string. Warning If the label is blank, this string is null.
        """
    def SingleView(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> IGESData_IGESEntity: 
        """
        Returns Structure (used by some types of IGES Entities only) Returns a Null Handle if Structure is not defined
        """
    def SubScriptNumber(self) -> int: 
        """
        Returns the integer subscript number used to identify this IGES entity. Warning 0 is returned if no subscript number is defined for this IGES entity.
        """
    def SubordinateStatus(self) -> int: 
        """
        gives Subordinate Switch (0-1-2-3)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewItem(self,num : int) -> IGESData_ViewKindEntity: 
        """
        Returns the View n0. <num> for a List of Views. For a Single Views, may return <me> itself
        """
    def ViewList(self) -> IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
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
class IGESData_WriterLib():
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
    def Module(self) -> IGESData_ReadWriteModule: 
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
    def Protocol(self) -> IGESData_Protocol: 
        """
        Returns the current Protocol in the Iteration
        """
    def Select(self,obj : IGESData_IGESEntity,module : IGESData_ReadWriteModule,CN : int) -> bool: 
        """
        Selects a Module from the Library, given an Object. Returns True if Select has succeeded, False else. Also Returns (as arguments) the selected Module and the Case Number determined by the associated Protocol. If Select has failed, <module> is Null Handle and CN is zero. (Select can work on any criterium, such as Object DynamicType)
        """
    def SetComplete(self) -> None: 
        """
        Sets a library to be defined with the complete Global list (all the couples Protocol/Modules recorded in it)
        """
    @staticmethod
    def SetGlobal_s(amodule : IGESData_ReadWriteModule,aprotocol : IGESData_Protocol) -> None: 
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
    def __init__(self,aprotocol : IGESData_Protocol) -> None: ...
    pass
IGESData_DefAny: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_DefAny
IGESData_DefNone: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_DefNone
IGESData_DefOne: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_DefOne
IGESData_DefReference: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_DefReference
IGESData_DefSeveral: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_DefSeveral
IGESData_DefValue: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_DefValue
IGESData_DefVoid: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_DefVoid
IGESData_EntityError: OCP.IGESData.IGESData_Status # value = IGESData_Status.IGESData_EntityError
IGESData_EntityOK: OCP.IGESData.IGESData_Status # value = IGESData_Status.IGESData_EntityOK
IGESData_ErrorOne: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_ErrorOne
IGESData_ErrorRef: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_ErrorRef
IGESData_ErrorSeveral: OCP.IGESData.IGESData_DefList # value = IGESData_DefList.IGESData_ErrorSeveral
IGESData_ErrorVal: OCP.IGESData.IGESData_DefType # value = IGESData_DefType.IGESData_ErrorVal
IGESData_ReadAssocs: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadAssocs
IGESData_ReadDir: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadDir
IGESData_ReadEnd: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadEnd
IGESData_ReadOwn: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadOwn
IGESData_ReadProps: OCP.IGESData.IGESData_ReadStage # value = IGESData_ReadStage.IGESData_ReadProps
IGESData_ReferenceError: OCP.IGESData.IGESData_Status # value = IGESData_Status.IGESData_ReferenceError
IGESData_TypeError: OCP.IGESData.IGESData_Status # value = IGESData_Status.IGESData_TypeError
