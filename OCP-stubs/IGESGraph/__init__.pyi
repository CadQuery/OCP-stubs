import OCP.IGESGraph
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.Standard
import OCP.IGESData
import OCP.gp
import OCP.IGESBasic
import OCP.Message
import OCP.TColStd
import OCP.Interface
__all__  = [
"IGESGraph",
"IGESGraph_Array1OfColor",
"IGESGraph_Array1OfTextDisplayTemplate",
"IGESGraph_Array1OfTextFontDef",
"IGESGraph_Color",
"IGESGraph_DefinitionLevel",
"IGESGraph_DrawingSize",
"IGESGraph_DrawingUnits",
"IGESGraph_GeneralModule",
"IGESGraph_HArray1OfColor",
"IGESGraph_HArray1OfTextDisplayTemplate",
"IGESGraph_HArray1OfTextFontDef",
"IGESGraph_HighLight",
"IGESGraph_IntercharacterSpacing",
"IGESGraph_LineFontDefPattern",
"IGESGraph_LineFontDefTemplate",
"IGESGraph_LineFontPredefined",
"IGESGraph_NominalSize",
"IGESGraph_Pick",
"IGESGraph_Protocol",
"IGESGraph_ReadWriteModule",
"IGESGraph_SpecificModule",
"IGESGraph_TextDisplayTemplate",
"IGESGraph_TextFontDef",
"IGESGraph_ToolColor",
"IGESGraph_ToolDefinitionLevel",
"IGESGraph_ToolDrawingSize",
"IGESGraph_ToolDrawingUnits",
"IGESGraph_ToolHighLight",
"IGESGraph_ToolIntercharacterSpacing",
"IGESGraph_ToolLineFontDefPattern",
"IGESGraph_ToolLineFontDefTemplate",
"IGESGraph_ToolLineFontPredefined",
"IGESGraph_ToolNominalSize",
"IGESGraph_ToolPick",
"IGESGraph_ToolTextDisplayTemplate",
"IGESGraph_ToolTextFontDef",
"IGESGraph_ToolUniformRectGrid",
"IGESGraph_UniformRectGrid"
]
class IGESGraph():
    """
    This package contains the group of classes necessary to define Graphic data among Structure Entities. (e.g., Fonts, Colors, Screen management ...)
    """
    @staticmethod
    def Init_s() -> None: 
        """
        Prepares dynamic data (Protocol, Modules) for this package
        """
    @staticmethod
    def Protocol_s() -> IGESGraph_Protocol: 
        """
        Returns the Protocol for this Package
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_Array1OfColor():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESGraph_Array1OfColor) -> IGESGraph_Array1OfColor: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESGraph_Color: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGraph_Color: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGraph_Color: 
        """
        Variable value access
        """
    def First(self) -> IGESGraph_Color: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESGraph_Color) -> None: 
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
    def Last(self) -> IGESGraph_Color: 
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
    def Move(self,theOther : IGESGraph_Array1OfColor) -> IGESGraph_Array1OfColor: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGraph_Color) -> None: 
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
    def Value(self,theIndex : int) -> IGESGraph_Color: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : IGESGraph_Array1OfColor) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : IGESGraph_Color,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESGraph_Array1OfTextDisplayTemplate():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESGraph_Array1OfTextDisplayTemplate) -> IGESGraph_Array1OfTextDisplayTemplate: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESGraph_TextDisplayTemplate: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGraph_TextDisplayTemplate: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGraph_TextDisplayTemplate: 
        """
        Variable value access
        """
    def First(self) -> IGESGraph_TextDisplayTemplate: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESGraph_TextDisplayTemplate) -> None: 
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
    def Last(self) -> IGESGraph_TextDisplayTemplate: 
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
    def Move(self,theOther : IGESGraph_Array1OfTextDisplayTemplate) -> IGESGraph_Array1OfTextDisplayTemplate: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGraph_TextDisplayTemplate) -> None: 
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
    def Value(self,theIndex : int) -> IGESGraph_TextDisplayTemplate: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : IGESGraph_TextDisplayTemplate,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IGESGraph_Array1OfTextDisplayTemplate) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESGraph_Array1OfTextFontDef():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESGraph_Array1OfTextFontDef) -> IGESGraph_Array1OfTextFontDef: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESGraph_TextFontDef: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGraph_TextFontDef: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGraph_TextFontDef: 
        """
        Variable value access
        """
    def First(self) -> IGESGraph_TextFontDef: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESGraph_TextFontDef) -> None: 
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
    def Last(self) -> IGESGraph_TextFontDef: 
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
    def Move(self,theOther : IGESGraph_Array1OfTextFontDef) -> IGESGraph_Array1OfTextFontDef: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGraph_TextFontDef) -> None: 
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
    def Value(self,theIndex : int) -> IGESGraph_TextFontDef: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : IGESGraph_Array1OfTextFontDef) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : IGESGraph_TextFontDef,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESGraph_Color(OCP.IGESData.IGESData_ColorEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESColor, Type <314> Form <0> in package IGESGraphdefines IGESColor, Type <314> Form <0> in package IGESGraphdefines IGESColor, Type <314> Form <0> in package IGESGraph
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
    def CMYIntensity(self) -> Tuple[float, float, float]: 
        """
        None
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def ColorName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        if HasColorName() is True returns the Verbal description of the Color.
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
    def HLSPercentage(self) -> Tuple[float, float, float]: 
        """
        None
        """
    def HasColorName(self) -> bool: 
        """
        returns True if optional character string is assigned, False otherwise.
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
    def Init(self,red : float,green : float,blue : float,aColorName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        This method is used to set the fields of the class Color - red : Red color intensity (range 0.0 to 100.0) - green : Green color intensity (range 0.0 to 100.0) - blue : Blue color intensity (range 0.0 to 100.0) - aColorName : Name of the color (optional)
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
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def RGBIntensity(self) -> Tuple[float, float, float]: 
        """
        None
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
class IGESGraph_DefinitionLevel(OCP.IGESData.IGESData_LevelListEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESDefinitionLevel, Type <406> Form <1> in package IGESGraphdefines IGESDefinitionLevel, Type <406> Form <1> in package IGESGraphdefines IGESDefinitionLevel, Type <406> Form <1> in package IGESGraph
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
    def IGESType(self) -> OCP.IGESData.IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,allLevelNumbers : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        This method is used to set the fields of the class DefinitionLevel - allLevelNumbers : Values of Level Numbers
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
    def LevelNumber(self,LevelIndex : int) -> int: 
        """
        returns the Level Number of <me> indicated by <LevelIndex> raises an exception if LevelIndex is <= 0 or LevelIndex > NbPropertyValues
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
    def NbLevelNumbers(self) -> int: 
        """
        Must return the count of levels (== NbPropertyValues)
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values in <me>
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
class IGESGraph_DrawingSize(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESDrawingSize, Type <406> Form <16> in package IGESGraphdefines IGESDrawingSize, Type <406> Form <16> in package IGESGraphdefines IGESDrawingSize, Type <406> Form <16> in package IGESGraph
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
    def Init(self,nbProps : int,aXSize : float,aYSize : float) -> None: 
        """
        This method is used to set the fields of the class DrawingSize - nbProps : Number of property values (NP = 2) - aXSize : Extent of Drawing along positive XD axis - aYSize : Extent of Drawing along positive YD axis
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
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values in <me> (NP = 2)
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
    def XSize(self) -> float: 
        """
        returns the extent of Drawing along positive XD axis
        """
    def YSize(self) -> float: 
        """
        returns the extent of Drawing along positive YD axis
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
class IGESGraph_DrawingUnits(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESDrawingUnits, Type <406> Form <17> in package IGESGraphdefines IGESDrawingUnits, Type <406> Form <17> in package IGESGraphdefines IGESDrawingUnits, Type <406> Form <17> in package IGESGraph
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
    def Flag(self) -> int: 
        """
        returns the drawing space units of <me>
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
    def Init(self,nbProps : int,aFlag : int,aUnit : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        This method is used to set the fields of the class DrawingUnits - nbProps : Number of property values (NP = 2) - aFlag : DrawingUnits Flag - aUnit : DrawingUnits Name
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
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values in <me>
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
    def Unit(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the name of the drawing space units of <me>
        """
    def UnitValue(self) -> float: 
        """
        Computes the value of the unit, in meters, according Flag (same values as for GlobalSection from IGESData)
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
class IGESGraph_GeneralModule(OCP.IGESData.IGESData_GeneralModule, OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    Definition of General Services for IGESGraph (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESGraph (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESGraph (specific part) This Services comprise : Shared & Implied Lists, Copy, Check
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" For IGES, answer is always True
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> int: 
        """
        Returns a category number which characterizes an entity Drawing for all
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
class IGESGraph_HArray1OfColor(IGESGraph_Array1OfColor, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESGraph_Array1OfColor: 
        """
        None
        """
    def Assign(self,theOther : IGESGraph_Array1OfColor) -> IGESGraph_Array1OfColor: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESGraph_Array1OfColor: 
        """
        None
        """
    def ChangeFirst(self) -> IGESGraph_Color: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGraph_Color: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGraph_Color: 
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
    def First(self) -> IGESGraph_Color: 
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
    def Init(self,theValue : IGESGraph_Color) -> None: 
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
    def Last(self) -> IGESGraph_Color: 
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
    def Move(self,theOther : IGESGraph_Array1OfColor) -> IGESGraph_Array1OfColor: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGraph_Color) -> None: 
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
    def Value(self,theIndex : int) -> IGESGraph_Color: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESGraph_Color) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IGESGraph_Array1OfColor) -> None: ...
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
class IGESGraph_HArray1OfTextDisplayTemplate(IGESGraph_Array1OfTextDisplayTemplate, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESGraph_Array1OfTextDisplayTemplate: 
        """
        None
        """
    def Assign(self,theOther : IGESGraph_Array1OfTextDisplayTemplate) -> IGESGraph_Array1OfTextDisplayTemplate: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESGraph_Array1OfTextDisplayTemplate: 
        """
        None
        """
    def ChangeFirst(self) -> IGESGraph_TextDisplayTemplate: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGraph_TextDisplayTemplate: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGraph_TextDisplayTemplate: 
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
    def First(self) -> IGESGraph_TextDisplayTemplate: 
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
    def Init(self,theValue : IGESGraph_TextDisplayTemplate) -> None: 
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
    def Last(self) -> IGESGraph_TextDisplayTemplate: 
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
    def Move(self,theOther : IGESGraph_Array1OfTextDisplayTemplate) -> IGESGraph_Array1OfTextDisplayTemplate: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGraph_TextDisplayTemplate) -> None: 
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
    def Value(self,theIndex : int) -> IGESGraph_TextDisplayTemplate: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESGraph_TextDisplayTemplate) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IGESGraph_Array1OfTextDisplayTemplate) -> None: ...
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
class IGESGraph_HArray1OfTextFontDef(IGESGraph_Array1OfTextFontDef, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESGraph_Array1OfTextFontDef: 
        """
        None
        """
    def Assign(self,theOther : IGESGraph_Array1OfTextFontDef) -> IGESGraph_Array1OfTextFontDef: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESGraph_Array1OfTextFontDef: 
        """
        None
        """
    def ChangeFirst(self) -> IGESGraph_TextFontDef: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGraph_TextFontDef: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGraph_TextFontDef: 
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
    def First(self) -> IGESGraph_TextFontDef: 
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
    def Init(self,theValue : IGESGraph_TextFontDef) -> None: 
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
    def Last(self) -> IGESGraph_TextFontDef: 
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
    def Move(self,theOther : IGESGraph_Array1OfTextFontDef) -> IGESGraph_Array1OfTextFontDef: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGraph_TextFontDef) -> None: 
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
    def Value(self,theIndex : int) -> IGESGraph_TextFontDef: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESGraph_TextFontDef) -> None: ...
    @overload
    def __init__(self,theOther : IGESGraph_Array1OfTextFontDef) -> None: ...
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
class IGESGraph_HighLight(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESHighLight, Type <406> Form <20> in package IGESGraphdefines IGESHighLight, Type <406> Form <20> in package IGESGraphdefines IGESHighLight, Type <406> Form <20> in package IGESGraph
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
    def HighLightStatus(self) -> int: 
        """
        returns 0 if <me> is not highlighted(default), 1 if <me> is highlighted
        """
    def IGESType(self) -> OCP.IGESData.IGESData_IGESType: 
        """
        gives IGES typing info (includes "Type" and "Form" data)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,nbProps : int,aHighLightStatus : int) -> None: 
        """
        This method is used to set the fields of the class HighLight - nbProps : Number of property values (NP = 1) - aHighLightStatus : HighLight Flag
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
    def IsHighLighted(self) -> bool: 
        """
        returns True if entity is highlighted
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
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values in <me>
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
class IGESGraph_IntercharacterSpacing(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESIntercharacterSpacing, Type <406> Form <18> in package IGESGraphdefines IGESIntercharacterSpacing, Type <406> Form <18> in package IGESGraphdefines IGESIntercharacterSpacing, Type <406> Form <18> in package IGESGraph
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
    def ISpace(self) -> float: 
        """
        returns the Intercharacter Space of <me> in percentage of the text height (Range = 0..100)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,nbProps : int,anISpace : float) -> None: 
        """
        This method is used to set the fields of the class IntercharacterSpacing - nbProps : Number of property values (NP = 1) - anISpace : Intercharacter spacing percentage
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
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values in <me>
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
class IGESGraph_LineFontDefPattern(OCP.IGESData.IGESData_LineFontEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESLineFontDefPattern, Type <304> Form <2> in package IGESGraphdefines IGESLineFontDefPattern, Type <304> Form <2> in package IGESGraphdefines IGESLineFontDefPattern, Type <304> Form <2> in package IGESGraph
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
    def DisplayPattern(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the string indicating which segments of the basic pattern are visible and which are blanked. e.g: theNbSegments = 5 and if Bit Pattern = 10110, which means that segments 2, 3 and 5 are visible, whereas segments 1 and 4 are blank. The method returns "2H16" as the HAsciiString. Note: The bits are right justified. (16h = 10110)
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
    def Init(self,allSegLength : OCP.TColStd.TColStd_HArray1OfReal,aPattern : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        This method is used to set the fields of the class LineFontDefPattern - allSegLength : Containing lengths of respective segments - aPattern : HAsciiString indicating visible-blank segments
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
    def IsVisible(self,Index : int) -> bool: 
        """
        The Display Pattern is decrypted to return True if the Index'th basic pattern is Visible, False otherwise. If Index > NbSegments or Index <= 0 then return value is False.
        """
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Length(self,Index : int) -> float: 
        """
        returns the Length of Index'th segment of the basic pattern raises exception if Index <= 0 or Index > NbSegments
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
    def NbSegments(self) -> int: 
        """
        returns the number of segments in the visible-blank pattern
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
class IGESGraph_LineFontDefTemplate(OCP.IGESData.IGESData_LineFontEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESLineFontDefTemplate, Type <304> Form <1> in package IGESGraphdefines IGESLineFontDefTemplate, Type <304> Form <1> in package IGESGraphdefines IGESLineFontDefTemplate, Type <304> Form <1> in package IGESGraph
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
    def Distance(self) -> float: 
        """
        returns the Distance between any two Template figures on the anchoring curve.
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
    def Init(self,anOrientation : int,aTemplate : OCP.IGESBasic.IGESBasic_SubfigureDef,aDistance : float,aScale : float) -> None: 
        """
        This method is used to set the fields of the class LineFontDefTemplate - anOrientation : Orientation of Template figure on anchoring curve - aTemplate : SubfigureDef entity used as Template figure - aDistance : Distance between the neighbouring Template figures - aScale : Scale factor applied to the Template figure
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
    def Orientation(self) -> int: 
        """
        if return value = 0, Each Template display is oriented by aligning the axis of the SubfigureDef with the axis of the definition space of the anchoring curve. = 1, Each Template display is oriented by aligning X-axis of the SubfigureDef with the tangent vector of the anchoring curve at the point of incidence of the curve and the origin of subfigure. Similarly Z-axis is aligned.
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
    def Scale(self) -> float: 
        """
        returns the Scaling factor applied to SubfigureDef to form Template figure.
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
    def TemplateEntity(self) -> OCP.IGESBasic.IGESBasic_SubfigureDef: 
        """
        returns SubfigureDef as the Entity used as Template figure.
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
class IGESGraph_LineFontPredefined(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESLineFontPredefined, Type <406> Form <19> in package IGESGraphdefines IGESLineFontPredefined, Type <406> Form <19> in package IGESGraphdefines IGESLineFontPredefined, Type <406> Form <19> in package IGESGraph
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
    def Init(self,nbProps : int,aLineFontPatternCode : int) -> None: 
        """
        This method is used to set the fields of the class LineFontPredefined - nbProps : Number of property values (NP = 1) - aLineFontPatternCode : Line Font Pattern Code
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
    def LineFontPatternCode(self) -> int: 
        """
        returns the Line Font Pattern Code of <me>
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
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values in <me>
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
class IGESGraph_NominalSize(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESNominalSize, Type <406> Form <13> in package IGESGraphdefines IGESNominalSize, Type <406> Form <13> in package IGESGraphdefines IGESNominalSize, Type <406> Form <13> in package IGESGraph
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
    def HasStandardName(self) -> bool: 
        """
        returns True if an engineering Standard is defined for <me> else, returns False
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
    def Init(self,nbProps : int,aNominalSizeValue : float,aNominalSizeName : OCP.TCollection.TCollection_HAsciiString,aStandardName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        This method is used to set the fields of the class NominalSize - nbProps : Number of property values (2 or 3) - aNominalSizeValue : NominalSize Value - aNominalSizeName : NominalSize Name - aStandardName : Name of relevant engineering standard
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
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values in <me>
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def NominalSizeName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the name of <me>
        """
    def NominalSizeValue(self) -> float: 
        """
        returns the value of <me>
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
    def StandardName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the name of the relevant engineering standard of <me>
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
class IGESGraph_Pick(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESPick, Type <406> Form <21> in package IGESGraphdefines IGESPick, Type <406> Form <21> in package IGESGraphdefines IGESPick, Type <406> Form <21> in package IGESGraph
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
    def Init(self,nbProps : int,aPickStatus : int) -> None: 
        """
        This method is used to set the fields of the class Pick - nbProps : Number of property values (NP = 1) - aPickStatus : Pick Flag
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
    def IsPickable(self) -> bool: 
        """
        returns True if thePick is 0.
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
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values in <me>.
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def PickFlag(self) -> int: 
        """
        returns 0 if <me> is pickable(default), 1 if <me> is not pickable.
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
class IGESGraph_Protocol(OCP.IGESData.IGESData_Protocol, OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    Description of Protocol for IGESGraphDescription of Protocol for IGESGraphDescription of Protocol for IGESGraph
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
        Gives the count of Resource Protocol. Here, one (Protocol from IGESBasic)
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
class IGESGraph_ReadWriteModule(OCP.IGESData.IGESData_ReadWriteModule, OCP.Interface.Interface_ReaderModule, OCP.Standard.Standard_Transient):
    """
    Defines Graph File Access Module for IGESGraph (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.Defines Graph File Access Module for IGESGraph (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.Defines Graph File Access Module for IGESGraph (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.
    """
    def CaseIGES(self,typenum : int,formnum : int) -> int: 
        """
        Defines Case Numbers for Entities of IGESGraph
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
    def ReadOwnParams(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file for an Entity of IGESGraph
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
class IGESGraph_SpecificModule(OCP.IGESData.IGESData_SpecificModule, OCP.Standard.Standard_Transient):
    """
    Defines Services attached to IGES Entities : Dump & OwnCorrect, for IGESGraphDefines Services attached to IGES Entities : Dump & OwnCorrect, for IGESGraphDefines Services attached to IGES Entities : Dump & OwnCorrect, for IGESGraph
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
    def OwnCorrect(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Performs non-ambiguous Corrections on Entities which support them (DrawingSize,DrawingUnits,HighLight,IntercharacterSpacing, LineFontPredefined,NominalSize,Pick,UniformRectGrid)
        """
    def OwnDump(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Specific Dump (own parameters) for IGESGraph
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
class IGESGraph_TextDisplayTemplate(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES TextDisplayTemplate Entity, Type <312>, form <0, 1> in package IGESGraphdefines IGES TextDisplayTemplate Entity, Type <312>, form <0, 1> in package IGESGraphdefines IGES TextDisplayTemplate Entity, Type <312>, form <0, 1> in package IGESGraph
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
    def BoxHeight(self) -> float: 
        """
        returns Character Box Height.
        """
    def BoxWidth(self) -> float: 
        """
        returns Character Box Width.
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
    def FontCode(self) -> int: 
        """
        returns the font code.
        """
    def FontEntity(self) -> IGESGraph_TextFontDef: 
        """
        returns Text Font Definition Entity used to define the font.
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
    def Init(self,aWidth : float,aHeight : float,aFontCode : int,aFontEntity : IGESGraph_TextFontDef,aSlantAngle : float,aRotationAngle : float,aMirrorFlag : int,aRotationFlag : int,aCorner : OCP.gp.gp_XYZ) -> None: 
        """
        This method is used to set the fields of the class TextDisplayTemplate - aWidth : Character box width - aHeight : Character box height - afontCode : Font code - aFontEntity : Text Font Definition Entity - aSlantAngle : Slant angle - aRotationAngle : Rotation angle - aMirrorFlag : Mirror Flag - aRotationFlag : Rotate internal text flag - aCorner : Lower left corner coordinates(Form No. 0), Increments from coordinates (Form No. 1)
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
    def IsFontEntity(self) -> bool: 
        """
        returns False if theFontEntity is Null, True otherwise.
        """
    def IsIncremental(self) -> bool: 
        """
        returns True if entity is Incremental (Form 1). False if entity is Absolute (Form 0).
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
    def MirrorFlag(self) -> int: 
        """
        returns Mirror flag Mirror flag : 0 = no mirroring. 1 = mirror axis perpendicular to text base line. 2 = mirror axis is text base line.
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
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def RotateFlag(self) -> int: 
        """
        returns Rotate internal text flag. Rotate internal text flag : 0 = text horizontal. 1 = text vertical.
        """
    def RotationAngle(self) -> float: 
        """
        returns Rotation angle of text block in radians.
        """
    def SetIncremental(self,mode : bool) -> None: 
        """
        Sets <me> to be Incremental (Form 1) if <mode> is True, or Basolute (Form 0) else
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
    def SlantAngle(self) -> float: 
        """
        returns slant angle of character in radians.
        """
    def StartingCorner(self) -> OCP.gp.gp_Pnt: 
        """
        If IsIncremental() returns False, gets coordinates of lower left corner of first character box. If IsIncremental() returns True, gets increments from X, Y, Z coordinates found in parent entity.
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
    def TransformedStartingCorner(self) -> OCP.gp.gp_Pnt: 
        """
        If IsIncremental() returns False, gets coordinates of lower left corner of first character box. If IsIncremental() returns True, gets increments from X, Y, Z coordinates found in parent entity.
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
class IGESGraph_TextFontDef(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Text Font Definition Entity, Type <310> in package IGESGraphdefines IGES Text Font Definition Entity, Type <310> in package IGESGraphdefines IGES Text Font Definition Entity, Type <310> in package IGESGraph
    """
    def ASCIICode(self,Chnum : int) -> int: 
        """
        returns the ASCII code of Chnum'th character. Exception OutOfRange is raised if Chnum <= 0 or Chnum > NbCharacters
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
    def FontCode(self) -> int: 
        """
        returns the font code.
        """
    def FontName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the font name.
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
    def Init(self,aFontCode : int,aFontName : OCP.TCollection.TCollection_HAsciiString,aSupersededFont : int,aSupersededEntity : IGESGraph_TextFontDef,aScale : int,allASCIICodes : OCP.TColStd.TColStd_HArray1OfInteger,allNextCharX : OCP.TColStd.TColStd_HArray1OfInteger,allNextCharY : OCP.TColStd.TColStd_HArray1OfInteger,allPenMotions : OCP.TColStd.TColStd_HArray1OfInteger,allPenFlags : OCP.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger,allMovePenToX : OCP.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger,allMovePenToY : OCP.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger) -> None: 
        """
        This method is used to set the fields of the class TextFontDef - aFontCode : Font Code - aFontName : Font Name - aSupersededFont : Number of superseded font - aSupersededEntity : Text Definition Entity - aScale : No. of grid units = 1 text height unit - allASCIICodes : ASCII codes for characters - allNextCharX & Y : Grid locations of the next character's origin (Integer vals) - allPenMotions : No. of pen motions for the characters - allPenFlags : Pen up/down flags, 0 = Down (default), 1 = Up - allMovePenToX & Y : Grid locations the pen will move to This method initializes the fields of the class TextFontDef. An exception is raised if the lengths of allASCIICodes, allNextChars, allPenMotions, allPenFlags and allMovePenTo are not same.
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
    def IsPenUp(self,Chnum : int,Motionnum : int) -> bool: 
        """
        returns pen status(True if 1, False if 0) of Motionnum'th motion of Chnum'th character. Exception raised if Chnum <= 0 or Chnum > NbCharacters or Motionnum <= 0 or Motionnum > NbPenMotions
        """
    def IsSupersededFontEntity(self) -> bool: 
        """
        True if this definition supersedes another TextFontDefinition Entity, False if it supersedes value.
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
    def NbCharacters(self) -> int: 
        """
        returns the number of characters in this definition.
        """
    def NbPenMotions(self,Chnum : int) -> int: 
        """
        returns number of pen motions for Chnum'th character. Exception OutOfRange is raised if Chnum <= 0 or Chnum > NbCharacters
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
    def NextCharOrigin(self,Chnum : int) -> Tuple[int, int]: 
        """
        returns grid location of origin of character next to Chnum'th char. Exception OutOfRange is raised if Chnum <= 0 or Chnum > NbCharacters
        """
    def NextPenPosition(self,Chnum : int,Motionnum : int) -> Tuple[int, int]: 
        """
        None
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
    def Scale(self) -> int: 
        """
        returns the number of grid units which equal one text height unit.
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
    def SupersededFontCode(self) -> int: 
        """
        returns the font number which this entity modifies.
        """
    def SupersededFontEntity(self) -> IGESGraph_TextFontDef: 
        """
        returns the font entity which this entity modifies.
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
class IGESGraph_ToolColor():
    """
    Tool to work on a Color. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_Color) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_Color,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_Color,entto : IGESGraph_Color,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGraph_Color,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_Color,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Color <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_Color,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_Color,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolDefinitionLevel():
    """
    Tool to work on a DefinitionLevel. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_DefinitionLevel) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_DefinitionLevel,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_DefinitionLevel,entto : IGESGraph_DefinitionLevel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGraph_DefinitionLevel,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_DefinitionLevel,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a DefinitionLevel <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_DefinitionLevel,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_DefinitionLevel,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolDrawingSize():
    """
    Tool to work on a DrawingSize. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_DrawingSize) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_DrawingSize,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_DrawingSize,entto : IGESGraph_DrawingSize,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGraph_DrawingSize) -> bool: 
        """
        Sets automatic unambiguous Correction on a DrawingSize (NbPropertyValues forced to 2)
        """
    def OwnDump(self,ent : IGESGraph_DrawingSize,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_DrawingSize,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a DrawingSize <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_DrawingSize,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_DrawingSize,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolDrawingUnits():
    """
    Tool to work on a DrawingUnits. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_DrawingUnits) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_DrawingUnits,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_DrawingUnits,entto : IGESGraph_DrawingUnits,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGraph_DrawingUnits) -> bool: 
        """
        Sets automatic unambiguous Correction on a DrawingUnits (NbPropertyValues forced to 2)
        """
    def OwnDump(self,ent : IGESGraph_DrawingUnits,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_DrawingUnits,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a DrawingUnits <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_DrawingUnits,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_DrawingUnits,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolHighLight():
    """
    Tool to work on a HighLight. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_HighLight) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_HighLight,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_HighLight,entto : IGESGraph_HighLight,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGraph_HighLight) -> bool: 
        """
        Sets automatic unambiguous Correction on a HighLight (NbPropertyValues forced to 1)
        """
    def OwnDump(self,ent : IGESGraph_HighLight,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_HighLight,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a HighLight <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_HighLight,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_HighLight,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolIntercharacterSpacing():
    """
    Tool to work on a IntercharacterSpacing. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_IntercharacterSpacing) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_IntercharacterSpacing,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_IntercharacterSpacing,entto : IGESGraph_IntercharacterSpacing,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGraph_IntercharacterSpacing) -> bool: 
        """
        Sets automatic unambiguous Correction on a IntercharacterSpacing (NbPropertyValues forced to 1)
        """
    def OwnDump(self,ent : IGESGraph_IntercharacterSpacing,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_IntercharacterSpacing,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a IntercharacterSpacing <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_IntercharacterSpacing,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_IntercharacterSpacing,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolLineFontDefPattern():
    """
    Tool to work on a LineFontDefPattern. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_LineFontDefPattern) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_LineFontDefPattern,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_LineFontDefPattern,entto : IGESGraph_LineFontDefPattern,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGraph_LineFontDefPattern,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_LineFontDefPattern,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a LineFontDefPattern <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_LineFontDefPattern,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_LineFontDefPattern,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolLineFontDefTemplate():
    """
    Tool to work on a LineFontDefTemplate. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_LineFontDefTemplate) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_LineFontDefTemplate,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_LineFontDefTemplate,entto : IGESGraph_LineFontDefTemplate,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGraph_LineFontDefTemplate,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_LineFontDefTemplate,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a LineFontDefTemplate <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_LineFontDefTemplate,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_LineFontDefTemplate,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolLineFontPredefined():
    """
    Tool to work on a LineFontPredefined. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_LineFontPredefined) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_LineFontPredefined,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_LineFontPredefined,entto : IGESGraph_LineFontPredefined,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGraph_LineFontPredefined) -> bool: 
        """
        Sets automatic unambiguous Correction on a LineFontPredefined (NbPropertyValues forced to 1)
        """
    def OwnDump(self,ent : IGESGraph_LineFontPredefined,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_LineFontPredefined,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a LineFontPredefined <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_LineFontPredefined,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_LineFontPredefined,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolNominalSize():
    """
    Tool to work on a NominalSize. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_NominalSize) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_NominalSize,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_NominalSize,entto : IGESGraph_NominalSize,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGraph_NominalSize) -> bool: 
        """
        Sets automatic unambiguous Correction on a NominalSize (NbPropertyValues forced to 2 or 3 according HasStandardName)
        """
    def OwnDump(self,ent : IGESGraph_NominalSize,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_NominalSize,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a NominalSize <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_NominalSize,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_NominalSize,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolPick():
    """
    Tool to work on a Pick. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_Pick) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_Pick,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_Pick,entto : IGESGraph_Pick,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGraph_Pick) -> bool: 
        """
        Sets automatic unambiguous Correction on a Pick (NbPropertyValues forced to 1)
        """
    def OwnDump(self,ent : IGESGraph_Pick,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_Pick,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Pick <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_Pick,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_Pick,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolTextDisplayTemplate():
    """
    Tool to work on a TextDisplayTemplate. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_TextDisplayTemplate) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_TextDisplayTemplate,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_TextDisplayTemplate,entto : IGESGraph_TextDisplayTemplate,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGraph_TextDisplayTemplate,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_TextDisplayTemplate,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a TextDisplayTemplate <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_TextDisplayTemplate,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_TextDisplayTemplate,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolTextFontDef():
    """
    Tool to work on a TextFontDef. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_TextFontDef) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_TextFontDef,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_TextFontDef,entto : IGESGraph_TextFontDef,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGraph_TextFontDef,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_TextFontDef,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a TextFontDef <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_TextFontDef,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_TextFontDef,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_ToolUniformRectGrid():
    """
    Tool to work on a UniformRectGrid. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGraph_UniformRectGrid) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGraph_UniformRectGrid,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGraph_UniformRectGrid,entto : IGESGraph_UniformRectGrid,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGraph_UniformRectGrid) -> bool: 
        """
        Sets automatic unambiguous Correction on a UniformRectGrid (NbPropertyValues forced to 9)
        """
    def OwnDump(self,ent : IGESGraph_UniformRectGrid,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGraph_UniformRectGrid,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a UniformRectGrid <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGraph_UniformRectGrid,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGraph_UniformRectGrid,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGraph_UniformRectGrid(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESUniformRectGrid, Type <406> Form <22> in package IGESGraphdefines IGESUniformRectGrid, Type <406> Form <22> in package IGESGraphdefines IGESUniformRectGrid, Type <406> Form <22> in package IGESGraph
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
    def GridPoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns coordinates of lower left corner, if <me> is a finite grid, coordinates of an arbitrary point, if <me> is an infinite grid.
        """
    def GridSpacing(self) -> OCP.gp.gp_Vec2d: 
        """
        returns the grid-spacing in drawing coordinates.
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
    def Init(self,nbProps : int,finite : int,line : int,weighted : int,aGridPoint : OCP.gp.gp_XY,aGridSpacing : OCP.gp.gp_XY,pointsX : int,pointsY : int) -> None: 
        """
        This method is used to set the fields of the class UniformRectGrid - nbProps : Number of property values (NP = 9) - finite : Finite/Infinite grid flag - line : Line/Point grid flag - weighted : Weighted/Unweighted grid flag - aGridPoint : Point on the grid - aGridSpacing : Grid spacing - pointsX : No. of points/lines in X Direction - pointsY : No. of points/lines in Y Direction
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
    def IsFinite(self) -> bool: 
        """
        returns False if <me> is an infinite grid, True if <me> is a finite grid.
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
    def IsLine(self) -> bool: 
        """
        returns False if <me> is a Point grid, True if <me> is a Line grid.
        """
    def IsWeighted(self) -> bool: 
        """
        returns False if <me> is a Weighted grid, True if <me> is not a Weighted grid.
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
    def NbPointsX(self) -> int: 
        """
        returns the no. of points/lines in X direction (only applicable if IsFinite() = 1, i.e: a finite grid).
        """
    def NbPointsY(self) -> int: 
        """
        returns the no. of points/lines in Y direction (only applicable if IsFinite() = 1, i.e: a finite grid).
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbPropertyValues(self) -> int: 
        """
        returns the number of property values in <me>.
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
