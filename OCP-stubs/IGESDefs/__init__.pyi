import OCP.IGESDefs
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IGESBasic
import OCP.TCollection
import OCP.IGESData
import OCP.gp
import OCP.IGESGraph
import OCP.Interface
import OCP.Standard
import OCP.TColStd
import io
__all__  = [
"IGESDefs",
"IGESDefs_Array1OfTabularData",
"IGESDefs_AssociativityDef",
"IGESDefs_AttributeDef",
"IGESDefs_AttributeTable",
"IGESDefs_GeneralModule",
"IGESDefs_GenericData",
"IGESDefs_HArray1OfHArray1OfTextDisplayTemplate",
"IGESDefs_HArray1OfTabularData",
"IGESDefs_MacroDef",
"IGESDefs_Protocol",
"IGESDefs_ReadWriteModule",
"IGESDefs_SpecificModule",
"IGESDefs_TabularData",
"IGESDefs_ToolAssociativityDef",
"IGESDefs_ToolAttributeDef",
"IGESDefs_ToolAttributeTable",
"IGESDefs_ToolGenericData",
"IGESDefs_ToolMacroDef",
"IGESDefs_ToolTabularData",
"IGESDefs_ToolUnitsData",
"IGESDefs_UnitsData"
]
class IGESDefs():
    """
    To embody general definitions of Entities (Parameters, Tables ...)
    """
    @staticmethod
    def Init_s() -> None: 
        """
        Prepares dynamic data (Protocol, Modules) for this package
        """
    @staticmethod
    def Protocol_s() -> IGESDefs_Protocol: 
        """
        Returns the Protocol for this Package
        """
    def __init__(self) -> None: ...
    pass
class IGESDefs_Array1OfTabularData():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESDefs_Array1OfTabularData) -> IGESDefs_Array1OfTabularData: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESDefs_TabularData: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESDefs_TabularData: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESDefs_TabularData: 
        """
        Variable value access
        """
    def First(self) -> IGESDefs_TabularData: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESDefs_TabularData) -> None: 
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
    def Last(self) -> IGESDefs_TabularData: 
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
    def Move(self,theOther : IGESDefs_Array1OfTabularData) -> IGESDefs_Array1OfTabularData: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESDefs_TabularData) -> None: 
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
    def Value(self,theIndex : int) -> IGESDefs_TabularData: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : IGESDefs_Array1OfTabularData) -> None: ...
    @overload
    def __init__(self,theBegin : IGESDefs_TabularData,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class IGESDefs_AssociativityDef(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Associativity Definition Entity, Type <302> Form <5001 - 9999> in package IGESDefs. This class permits the preprocessor to define an associativity schema. i.e., by using it preprocessor defines the type of relationship.defines IGES Associativity Definition Entity, Type <302> Form <5001 - 9999> in package IGESDefs. This class permits the preprocessor to define an associativity schema. i.e., by using it preprocessor defines the type of relationship.defines IGES Associativity Definition Entity, Type <302> Form <5001 - 9999> in package IGESDefs. This class permits the preprocessor to define an associativity schema. i.e., by using it preprocessor defines the type of relationship.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Associate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BackPointerReq(self,ClassNum : int) -> int: 
        """
        returns 1 or 2 raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def ClassOrder(self,ClassNum : int) -> int: 
        """
        returns 1 or 2 raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
        """
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
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
    def DefColor(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def IGESType(self) -> OCP.IGESData.IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,requirements : OCP.TColStd.TColStd_HArray1OfInteger,orders : OCP.TColStd.TColStd_HArray1OfInteger,numItems : OCP.TColStd.TColStd_HArray1OfInteger,items : OCP.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger) -> None: 
        """
        This method is used to set the fields of the class AssociativityDef - requirements : Back Pointers requirements - orders : Class Orders - numItems : Number of Items per Class - items : Items in each class raises exception if lengths of the arrays are not the same.
        """
    def InitColor(self,ent : OCP.IGESData.IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : OCP.IGESData.IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : OCP.IGESData.IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : OCP.IGESData.IGESData_IGESEntity,lab : OCP.IGESData.IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : OCP.IGESData.IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
        """
    def IsBackPointerReq(self,ClassNum : int) -> bool: 
        """
        returns 1 if the theBackPointerReqs(ClassNum) = 1 returns 0 if the theBackPointerReqs(ClassNum) = 2 raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
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
    def IsOrdered(self,ClassNum : int) -> bool: 
        """
        returns 1 if theClassOrders(ClassNum) = 1 (ordered class) returns 0 if theClassOrders(ClassNum) = 2 (unordered class) raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
        """
    def Item(self,ClassNum : int,ItemNum : int) -> int: 
        """
        returns ItemNum'th Item of ClassNum'th Class raises exception if ClassNum <= 0 or ClassNum > NbClassDefs() ItemNum <= 0 or ItemNum > NbItemsPerClass(ClassNum)
        """
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> OCP.IGESData.IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> OCP.IGESData.IGESData_LineFontEntity: 
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
    def NbClassDefs(self) -> int: 
        """
        returns the Number of class definitions
        """
    def NbItemsPerClass(self,ClassNum : int) -> int: 
        """
        returns no. of items per class entry raises exception if ClassNum <= 0 or ClassNum > NbClassDefs()
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
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetFormNumber(self,form : int) -> None: 
        """
        None
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
    def SingleView(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def View(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
class IGESDefs_AttributeDef(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Attribute Table Definition Entity, Type <322> Form [0, 1, 2] in package IGESDefs. This is class is used to support the concept of well defined collection of attributes, whether it is a table or a single row of attributes.defines IGES Attribute Table Definition Entity, Type <322> Form [0, 1, 2] in package IGESDefs. This is class is used to support the concept of well defined collection of attributes, whether it is a table or a single row of attributes.defines IGES Attribute Table Definition Entity, Type <322> Form [0, 1, 2] in package IGESDefs. This is class is used to support the concept of well defined collection of attributes, whether it is a table or a single row of attributes.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Associate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def AttributeAsEntity(self,AttrNum : int,ValueNum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Entity Error if Indices out of Range, or no Value defined, or not a Entity
        """
    def AttributeAsInteger(self,AttrNum : int,ValueNum : int) -> int: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Integer Error if Indices out of Range, or no Value defined, or not an Integer
        """
    def AttributeAsLogical(self,AttrNum : int,ValueNum : int) -> bool: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as a Boolean Error if Indices out of Range, or no Value defined, or not a Logical
        """
    def AttributeAsReal(self,AttrNum : int,ValueNum : int) -> float: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as a Real Error if Indices out of Range, or no Value defined, or not a Real
        """
    def AttributeAsString(self,AttrNum : int,ValueNum : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Integer
        """
    def AttributeList(self,AttrNum : int) -> OCP.Standard.Standard_Transient: 
        """
        Returns the List of Attributes <AttrNum>, as a Transient. Its effective Type depends of the Type of Attribute : HArray1OfInteger for Integer, Logical(0-1), HArray1OfReal for Real, HArray1OfHSaciiString for String, HArray1OfIGESEntity for Entity (Pointer) See methods AttributeAs... for an accurate access
        """
    def AttributeTextDisplay(self,AttrNum : int,PointerNum : int) -> OCP.IGESGraph.IGESGraph_TextDisplayTemplate: 
        """
        None
        """
    def AttributeType(self,num : int) -> int: 
        """
        returns the num'th Attribute Type raises exception if num <= 0 or num > NbAttributes()
        """
    def AttributeValueCount(self,num : int) -> int: 
        """
        returns the num'th Attribute value count raises exception if num <= 0 or num > NbAttributes()
        """
    def AttributeValueDataType(self,num : int) -> int: 
        """
        returns the num'th Attribute value data type raises exception if num <= 0 or num > NbAttributes()
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
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
    def DefColor(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def HasTableName(self) -> bool: 
        """
        Returns True if a Table Name is defined
        """
    def HasTextDisplay(self) -> bool: 
        """
        returns false if TextDisplays are defined (i.e. for Form = 2)
        """
    def HasTransf(self) -> bool: 
        """
        Returns True if a Transformation Matrix is defined
        """
    def HasValues(self) -> bool: 
        """
        returns false if Values are defined (i.e. for Form = 1 or 2)
        """
    def HierarchyStatus(self) -> int: 
        """
        gives Hierarchy status (0-1-2)
        """
    def IGESType(self) -> OCP.IGESData.IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aListType : int,attrTypes : OCP.TColStd.TColStd_HArray1OfInteger,attrValueDataTypes : OCP.TColStd.TColStd_HArray1OfInteger,attrValueCounts : OCP.TColStd.TColStd_HArray1OfInteger,attrValues : OCP.TColStd.TColStd_HArray1OfTransient,attrValuePointers : IGESDefs_HArray1OfHArray1OfTextDisplayTemplate) -> None: 
        """
        None
        """
    def InitColor(self,ent : OCP.IGESData.IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : OCP.IGESData.IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : OCP.IGESData.IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : OCP.IGESData.IGESData_IGESEntity,lab : OCP.IGESData.IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : OCP.IGESData.IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> OCP.IGESData.IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> OCP.IGESData.IGESData_LineFontEntity: 
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
    def ListType(self) -> int: 
        """
        returns the Attribute List Type
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
    def NbAttributes(self) -> int: 
        """
        returns the Number of Attributes
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
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def SingleView(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def TableName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the Attribute Table name, or comment (default = null, no name : seeHasTableName)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def View(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
class IGESDefs_AttributeTable(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Attribute Table, Type <422> Form <0, 1> in package IGESDefs This class is used to represent an occurrence of Attribute Table. This Class may be independent or dependent or pointed at by other Entities.defines IGES Attribute Table, Type <422> Form <0, 1> in package IGESDefs This class is used to represent an occurrence of Attribute Table. This Class may be independent or dependent or pointed at by other Entities.defines IGES Attribute Table, Type <422> Form <0, 1> in package IGESDefs This class is used to represent an occurrence of Attribute Table. This Class may be independent or dependent or pointed at by other Entities.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Associate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def AttributeAsEntity(self,AtNum : int,Rownum : int,ValNum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns Attribute Value <AtNum, Rownum, rank ValNum> as an Entity Error if Indices out of Range, or no Value defined, or not an Entity
        """
    def AttributeAsInteger(self,AtNum : int,Rownum : int,ValNum : int) -> int: 
        """
        Returns Attribute Value <AtNum, Rownum, rank ValNum> as an Integer Error if Indices out of Range, or no Value defined, or not an Integer
        """
    def AttributeAsLogical(self,AtNum : int,Rownum : int,ValNum : int) -> bool: 
        """
        Returns Attribute Value <AtNum, Rownum, rank ValNum> as a Boolean Error if Indices out of Range, or no Value defined, or not a Logical
        """
    def AttributeAsReal(self,AtNum : int,Rownum : int,ValNum : int) -> float: 
        """
        Returns Attribute Value <AtNum, Rownum, rank ValNum> as a Real Error if Indices out of Range, or no Value defined, or not a Real
        """
    def AttributeAsString(self,AtNum : int,Rownum : int,ValNum : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Attribute Value <AtNum, Rownum, rank ValNum> as an Integer
        """
    def AttributeList(self,Attribnum : int,Rownum : int) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DataType(self,Atnum : int) -> int: 
        """
        returns the Type of an Attribute, given its No. : it is read in the Definition. (1 : Integer, 2 : Real, 3 : String, 4 : Entity, 6 : Logical)
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Definition(self) -> IGESDefs_AttributeDef: 
        """
        Return the Structure information in Directory Entry, casted as an AttributeDef
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def IGESType(self) -> OCP.IGESData.IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,attributes : OCP.TColStd.TColStd_HArray2OfTransient) -> None: 
        """
        This method is used to set the fields of the class AttributeTable - attributes : Attribute instances, created as (1,NbAttributes,1,NbRows) - NbRows = 1 is a particular case (Form 0)
        """
    def InitColor(self,ent : OCP.IGESData.IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : OCP.IGESData.IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : OCP.IGESData.IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : OCP.IGESData.IGESData_IGESEntity,lab : OCP.IGESData.IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : OCP.IGESData.IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> OCP.IGESData.IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> OCP.IGESData.IGESData_LineFontEntity: 
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
    def NbAttributes(self) -> int: 
        """
        returns Number of Attributes
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbRows(self) -> int: 
        """
        returns Number of Rows. Remark that it is always 1 if Form = 0 It means that the list of Attributes (by their number, and for each one its type and ValueCount) is repeated <NbRows> times
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
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetDefinition(self,def_ : IGESDefs_AttributeDef) -> None: 
        """
        Sets a Definition as Structure information (works by calling InitMisc)
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
    def SingleView(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def ValueCount(self,Atnum : int) -> int: 
        """
        returns the Count of Value for an Attribute, given its No. : it is read in the Definition.
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
class IGESDefs_GeneralModule(OCP.IGESData.IGESData_GeneralModule, OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    Definition of General Services for IGESDefs (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESDefs (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESDefs (specific part) This Services comprise : Shared & Implied Lists, Copy, Check
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" For IGES, answer is always True
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> int: 
        """
        Returns a category number which characterizes an entity Auxiliary for all
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
    def DirChecker(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity) -> OCP.IGESData.IGESData_DirChecker: 
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
    def OwnCheckCase(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check for each type of Entity
        """
    def OwnCopyCase(self,CN : int,entfrom : OCP.IGESData.IGESData_IGESEntity,entto : OCP.IGESData.IGESData_IGESEntity,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies parameters which are specific of each Type of Entity
        """
    def OwnDeleteCase(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Specific preparation for delete, acts on own parameters Default does nothing, to be redefined as required
        """
    def OwnImpliedCase(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific list of Entities implied by a given IGESEntity <ent> (in addition to Associativities). By default, there are none, but this method can be redefined as required
        """
    def OwnRenewCase(self,CN : int,entfrom : OCP.IGESData.IGESData_IGESEntity,entto : OCP.IGESData.IGESData_IGESEntity,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Renews parameters which are specific of each Type of Entity : the provided default does nothing, but this method may be redefined as required
        """
    def OwnSharedCase(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
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
class IGESDefs_GenericData(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Generic Data, Type <406> Form <27> in package IGESDefs Used to communicate information defined by the system operator while creating the model. The information is system specific and does not map into one of the predefined properties or associativities. Properties and property values can be defined by multiple instances of this property.defines IGES Generic Data, Type <406> Form <27> in package IGESDefs Used to communicate information defined by the system operator while creating the model. The information is system specific and does not map into one of the predefined properties or associativities. Properties and property values can be defined by multiple instances of this property.defines IGES Generic Data, Type <406> Form <27> in package IGESDefs Used to communicate information defined by the system operator while creating the model. The information is system specific and does not map into one of the predefined properties or associativities. Properties and property values can be defined by multiple instances of this property.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Associate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
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
    def DefColor(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def IGESType(self) -> OCP.IGESData.IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,nbPropVal : int,aName : OCP.TCollection.TCollection_HAsciiString,allTypes : OCP.TColStd.TColStd_HArray1OfInteger,allValues : OCP.TColStd.TColStd_HArray1OfTransient) -> None: 
        """
        This method is used to set the fields of the class GenericData - nbPropVal : Number of property values - aName : Property Name - allTypes : Property Types - allValues : Property Values
        """
    def InitColor(self,ent : OCP.IGESData.IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : OCP.IGESData.IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : OCP.IGESData.IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : OCP.IGESData.IGESData_IGESEntity,lab : OCP.IGESData.IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : OCP.IGESData.IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> OCP.IGESData.IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> OCP.IGESData.IGESData_LineFontEntity: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns property name
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
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values
        """
    def NbTypeValuePairs(self) -> int: 
        """
        returns the number of TYPE/VALUE pairs
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
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def SingleView(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def Type(self,Index : int) -> int: 
        """
        returns the Index'th property value data type raises exception if Index <= 0 or Index > NbTypeValuePairs()
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def Value(self,Index : int) -> OCP.Standard.Standard_Transient: ...
    def ValueAsEntity(self,ValueNum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Entity Error if Index out of Range, or not a Entity
        """
    def ValueAsInteger(self,ValueNum : int) -> int: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Integer Error if Index out of Range, or not an Integer
        """
    def ValueAsLogical(self,ValueNum : int) -> bool: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as a Boolean Error if Index out of Range, or not a Logical
        """
    def ValueAsReal(self,ValueNum : int) -> float: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as a Real Error if Index out of Range, or not a Real
        """
    def ValueAsString(self,ValueNum : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Attribute Value <AttrNum, rank ValueNum> as an Integer
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
class IGESDefs_HArray1OfHArray1OfTextDisplayTemplate(OCP.Standard.Standard_Transient):
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
        None
        """
    def Lower(self) -> int: 
        """
        None
        """
    def SetValue(self,num : int,val : OCP.IGESGraph.IGESGraph_HArray1OfTextDisplayTemplate) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        None
        """
    def Value(self,num : int) -> OCP.IGESGraph.IGESGraph_HArray1OfTextDisplayTemplate: 
        """
        None
        """
    def __init__(self,low : int,up : int) -> None: ...
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
class IGESDefs_HArray1OfTabularData(IGESDefs_Array1OfTabularData, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESDefs_Array1OfTabularData: 
        """
        None
        """
    def Assign(self,theOther : IGESDefs_Array1OfTabularData) -> IGESDefs_Array1OfTabularData: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESDefs_Array1OfTabularData: 
        """
        None
        """
    def ChangeFirst(self) -> IGESDefs_TabularData: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESDefs_TabularData: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESDefs_TabularData: 
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
    def First(self) -> IGESDefs_TabularData: 
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
    def Init(self,theValue : IGESDefs_TabularData) -> None: 
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
    def Last(self) -> IGESDefs_TabularData: 
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
    def Move(self,theOther : IGESDefs_Array1OfTabularData) -> IGESDefs_Array1OfTabularData: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESDefs_TabularData) -> None: 
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
    def Value(self,theIndex : int) -> IGESDefs_TabularData: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IGESDefs_Array1OfTabularData) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESDefs_TabularData) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
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
class IGESDefs_MacroDef(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Macro Definition Entity, Type <306> Form <0> in package IGESDefs This Class specifies the action of a specific MACRO. After specification MACRO can be used as necessary by means of MACRO class instance entity.defines IGES Macro Definition Entity, Type <306> Form <0> in package IGESDefs This Class specifies the action of a specific MACRO. After specification MACRO can be used as necessary by means of MACRO class instance entity.defines IGES Macro Definition Entity, Type <306> Form <0> in package IGESDefs This Class specifies the action of a specific MACRO. After specification MACRO can be used as necessary by means of MACRO class instance entity.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Associate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
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
    def DefColor(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ENDMACRO(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the ENDM(Literal)
        """
    def EntityTypeID(self) -> int: 
        """
        returns the Entity Type ID
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
    def IGESType(self) -> OCP.IGESData.IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,macro : OCP.TCollection.TCollection_HAsciiString,entityTypeID : int,langStatements : OCP.Interface.Interface_HArray1OfHAsciiString,endMacro : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        This method is used to set the fields of the class MacroDef - macro : MACRO - entityTypeID : Entity Type ID - langStatements : Language Statements - endMacro : END MACRO
        """
    def InitColor(self,ent : OCP.IGESData.IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : OCP.IGESData.IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : OCP.IGESData.IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : OCP.IGESData.IGESData_IGESEntity,lab : OCP.IGESData.IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : OCP.IGESData.IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def LanguageStatement(self,StatNum : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> OCP.IGESData.IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> OCP.IGESData.IGESData_LineFontEntity: 
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
    def MACRO(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the MACRO(Literal)
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
    def NbStatements(self) -> int: 
        """
        returns the number of language statements
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
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def SingleView(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def View(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
class IGESDefs_Protocol(OCP.IGESData.IGESData_Protocol, OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    Description of Protocol for IGESDefsDescription of Protocol for IGESDefsDescription of Protocol for IGESDefs
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
        Returns True if <model> is a Model of IGES Norm
        """
    def IsUnknownEntity(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if <ent> is an Unknown Entity for the Norm, i.e. Type UndefinedEntity, status Unknown
        """
    def NbResources(self) -> int: 
        """
        Gives the count of Resource Protocol. Here, one (Protocol from IGESGraph)
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
        Returns a Resource, given a rank.
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
        Returns a Case Number, specific of each recognized Type This Case Number is then used in Libraries : the various Modules attached to this class of Protocol must use them in accordance (for a given value of TypeNumber, they must consider the same Type as the Protocol defines)
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
class IGESDefs_ReadWriteModule(OCP.IGESData.IGESData_ReadWriteModule, OCP.Interface.Interface_ReaderModule, OCP.Standard.Standard_Transient):
    """
    Defines Defs File Access Module for IGESDefs (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.Defines Defs File Access Module for IGESDefs (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.Defines Defs File Access Module for IGESDefs (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.
    """
    def CaseIGES(self,typenum : int,formnum : int) -> int: 
        """
        Defines Case Numbers for Entities of IGESDefs
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
        General Read Function. See IGESReaderTool for more info
        """
    def ReadOwnParams(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file for an Entity of IGESDefs
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteOwnParams(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
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
class IGESDefs_SpecificModule(OCP.IGESData.IGESData_SpecificModule, OCP.Standard.Standard_Transient):
    """
    Defines Services attached to IGES Entities : Dump, for IGESDefsDefines Services attached to IGES Entities : Dump, for IGESDefsDefines Services attached to IGES Entities : Dump, for IGESDefs
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
    def OwnCorrect(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Specific Automatic Correction on own Parameters of an Entity. It works by setting in accordance redundant data, if there are when there is no ambiguity (else, it does nothing). Remark that classic Corrections on Directory Entry (to set void data) are taken into account alsewhere.
        """
    def OwnDump(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Specific Dump (own parameters) for IGESDefs
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
class IGESDefs_TabularData(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    Defines IGES Tabular Data, Type <406> Form <11>, in package IGESDefs This Class is used to provide a Structure to accommodate point form data.Defines IGES Tabular Data, Type <406> Form <11>, in package IGESDefs This Class is used to provide a Structure to accommodate point form data.Defines IGES Tabular Data, Type <406> Form <11>, in package IGESDefs This Class is used to provide a Structure to accommodate point form data.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Associate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def ComputedNbPropertyValues(self) -> int: 
        """
        determines the number of property values required
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefColor(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DependentValue(self,variablenum : int,valuenum : int) -> float: 
        """
        None
        """
    def DependentValues(self,num : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def DirFieldEntity(self,fieldnum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def IGESType(self) -> OCP.IGESData.IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IndependentValue(self,variablenum : int,valuenum : int) -> float: 
        """
        None
        """
    def Init(self,nbProps : int,propType : int,typesInd : OCP.TColStd.TColStd_HArray1OfInteger,nbValuesInd : OCP.TColStd.TColStd_HArray1OfInteger,valuesInd : OCP.IGESBasic.IGESBasic_HArray1OfHArray1OfReal,valuesDep : OCP.IGESBasic.IGESBasic_HArray1OfHArray1OfReal) -> None: 
        """
        This method is used to set the fields of the class TabularData - nbProps : Number of property values - propType : Property Type - typesInd : Type of independent variables - nbValuesInd : Number of values of independent variables - valuesInd : Values of independent variables - valuesDep : Values of dependent variables raises exception if lengths of typeInd and nbValuesInd are not same
        """
    def InitColor(self,ent : OCP.IGESData.IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : OCP.IGESData.IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : OCP.IGESData.IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : OCP.IGESData.IGESData_IGESEntity,lab : OCP.IGESData.IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : OCP.IGESData.IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> OCP.IGESData.IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> OCP.IGESData.IGESData_LineFontEntity: 
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
    def NbDependents(self) -> int: 
        """
        returns the number of dependent variables
        """
    def NbIndependents(self) -> int: 
        """
        returns the number of independent variables
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values (recorded)
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def NbValues(self,num : int) -> int: 
        """
        returns the number of different values of the num'th indep. variable raises exception if num <= 0 or num > NbIndependents()
        """
    def OwnCorrect(self) -> bool: 
        """
        checks, and correct as necessary, the number of property values. Returns True if corrected, False if already OK
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def PropertyType(self) -> int: 
        """
        returns the property type
        """
    def RankColor(self) -> int: 
        """
        Returns the color definition as an integer value if the color was defined as a rank. Warning A negative value is returned if the color was defined as an entity.
        """
    def RankLineFont(self) -> int: 
        """
        Returns LineFont definition as an Integer (if defined as Rank) If LineFont is defined as an Entity, returns a negative value
        """
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def SingleView(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypeOfIndependents(self,num : int) -> int: 
        """
        returns the type of the num'th independent variable raises exception if num <= 0 or num > NbIndependents()
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def View(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
class IGESDefs_ToolAssociativityDef():
    """
    Tool to work on a AssociativityDef. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDefs_AssociativityDef) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDefs_AssociativityDef,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDefs_AssociativityDef,entto : IGESDefs_AssociativityDef,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDefs_AssociativityDef,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDefs_AssociativityDef,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a AssociativityDef <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDefs_AssociativityDef,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDefs_AssociativityDef,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDefs_ToolAttributeDef():
    """
    Tool to work on a AttributeDef. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDefs_AttributeDef) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDefs_AttributeDef,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDefs_AttributeDef,entto : IGESDefs_AttributeDef,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDefs_AttributeDef,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDefs_AttributeDef,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a AttributeDef <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDefs_AttributeDef,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDefs_AttributeDef,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDefs_ToolAttributeTable():
    """
    Tool to work on a AttributeTable. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDefs_AttributeTable) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDefs_AttributeTable,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDefs_AttributeTable,entto : IGESDefs_AttributeTable,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDefs_AttributeTable,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDefs_AttributeTable,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a AttributeTable <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDefs_AttributeTable,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDefs_AttributeTable,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDefs_ToolGenericData():
    """
    Tool to work on a GenericData. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDefs_GenericData) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDefs_GenericData,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDefs_GenericData,entto : IGESDefs_GenericData,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDefs_GenericData,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDefs_GenericData,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a GenericData <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDefs_GenericData,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDefs_GenericData,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDefs_ToolMacroDef():
    """
    Tool to work on a MacroDef. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDefs_MacroDef) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDefs_MacroDef,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDefs_MacroDef,entto : IGESDefs_MacroDef,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDefs_MacroDef,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDefs_MacroDef,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a MacroDef <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDefs_MacroDef,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDefs_MacroDef,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDefs_ToolTabularData():
    """
    Tool to work on a TabularData. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDefs_TabularData) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDefs_TabularData,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDefs_TabularData,entto : IGESDefs_TabularData,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDefs_TabularData,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDefs_TabularData,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a TabularData <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDefs_TabularData,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDefs_TabularData,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDefs_ToolUnitsData():
    """
    Tool to work on a UnitsData. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDefs_UnitsData) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDefs_UnitsData,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDefs_UnitsData,entto : IGESDefs_UnitsData,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDefs_UnitsData,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDefs_UnitsData,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a UnitsData <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDefs_UnitsData,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDefs_UnitsData,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDefs_UnitsData(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES UnitsData Entity, Type <316> Form <0> in package IGESDefs This class stores data about a model's fundamental units.defines IGES UnitsData Entity, Type <316> Form <0> in package IGESDefs This class stores data about a model's fundamental units.defines IGES UnitsData Entity, Type <316> Form <0> in package IGESDefs This class stores data about a model's fundamental units.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Associate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
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
    def DefColor(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of Color.
        """
    def DefLevel(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of Level
        """
    def DefLineFont(self) -> OCP.IGESData.IGESData_DefType: 
        """
        Returns the definition status of LineFont
        """
    def DefView(self) -> OCP.IGESData.IGESData_DefList: 
        """
        Returns the definition status of the view. This can be: none, one or several.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirFieldEntity(self,fieldnum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def IGESType(self) -> OCP.IGESData.IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,unitTypes : OCP.Interface.Interface_HArray1OfHAsciiString,unitValues : OCP.Interface.Interface_HArray1OfHAsciiString,unitScales : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        This method is used to set the fields of the class UnitsData - unitTypes : Types of the units being defined - unitValues : Unit Values of the units - unitScales : Multiplicative Scale Factors raises exception if lengths of unitTypes, unitValues and unitScale are not same
        """
    def InitColor(self,ent : OCP.IGESData.IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitLevel(self,ent : OCP.IGESData.IGESData_LevelListEntity,val : int=0) -> None: 
        """
        Initializes Level : if <ent> is not Null, it gives LevelList, else <val> gives or erases (if zero) unique Level
        """
    def InitLineFont(self,ent : OCP.IGESData.IGESData_LineFontEntity,rank : int=0) -> None: 
        """
        Initializes LineFont : if <ent> is not Null, it gives LineFont, else <rank> gives or erases (if zero) RankLineFont
        """
    def InitMisc(self,str : OCP.IGESData.IGESData_IGESEntity,lab : OCP.IGESData.IGESData_LabelDisplayEntity,weightnum : int) -> None: 
        """
        Initializes various data (those not yet seen above), or erases them if they are given as Null (Zero for <weightnum>) : <str> for Structure, <lab> for LabelDisplay, and <weightnum> for WeightNumber
        """
    def InitStatus(self,blank : int,subordinate : int,useflag : int,hierarchy : int) -> None: 
        """
        Initializes the Status of Directory Part
        """
    def InitTransf(self,ent : OCP.IGESData.IGESData_TransfEntity) -> None: 
        """
        Initializes Transf, or erases it if <ent> is given Null
        """
    def InitView(self,ent : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
        """
        Initializes View, or erases it if <ent> is given Null
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
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Level(self) -> int: 
        """
        Returns the level the entity belongs to. Returns -1 if the entity belongs to more than one level.
        """
    def LevelList(self) -> OCP.IGESData.IGESData_LevelListEntity: 
        """
        Returns LevelList if Level is defined as a list. Returns a null handle if DefLevel is not DefSeveral.
        """
    def LineFont(self) -> OCP.IGESData.IGESData_LineFontEntity: 
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
    def NbUnits(self) -> int: 
        """
        returns the Number of units defined by this entity
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
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def ScaleFactor(self,UnitNum : int) -> float: 
        """
        returns the multiplicative scale factor to be applied to the UnitNum'th unit being defined raises exception if UnitNum <= 0 or UnitNum > NbUnits()
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
    def SingleView(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view as a single view if it was defined as such and not as a list of views. Warning A null handle is returned if DefView does not have the value DefOne.
        """
    def Structure(self) -> OCP.IGESData.IGESData_IGESEntity: 
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
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TypeNumber(self) -> int: 
        """
        gives IGES Type Number (often coupled with Form Number)
        """
    def TypedAssociativity(self,atype : OCP.Standard.Standard_Type) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Associativity of a given Type (if only one exists) Error if none or more than one
        """
    def TypedProperty(self,atype : OCP.Standard.Standard_Type,anum : int=0) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Property of a given Type Error if none or more than one
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UnitType(self,UnitNum : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the Type of the UnitNum'th unit being defined raises exception if UnitNum <= 0 or UnitNum > NbUnits()
        """
    def UnitValue(self,UnitNum : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the Units of the UnitNum'th unit being defined raises exception if UnitNum <= 0 or UnitNum > NbUnits()
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VectorLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location considered for Vectors, i.e. without its Translation Part. As Location, it gives local definition.
        """
    def View(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity. This view can be a single view or a list of views. Warning A null handle is returned if the view is not defined.
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
