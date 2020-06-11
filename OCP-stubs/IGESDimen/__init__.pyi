import OCP.IGESDimen
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.Standard
import OCP.IGESData
import OCP.IGESGeom
import OCP.gp
import OCP.IGESGraph
import OCP.TColgp
import OCP.Message
import OCP.TColStd
import OCP.Interface
__all__  = [
"IGESDimen",
"IGESDimen_AngularDimension",
"IGESDimen_Array1OfGeneralNote",
"IGESDimen_Array1OfLeaderArrow",
"IGESDimen_BasicDimension",
"IGESDimen_CenterLine",
"IGESDimen_CurveDimension",
"IGESDimen_DiameterDimension",
"IGESDimen_DimensionDisplayData",
"IGESDimen_DimensionTolerance",
"IGESDimen_DimensionUnits",
"IGESDimen_DimensionedGeometry",
"IGESDimen_FlagNote",
"IGESDimen_GeneralLabel",
"IGESDimen_GeneralModule",
"IGESDimen_GeneralNote",
"IGESDimen_GeneralSymbol",
"IGESDimen_HArray1OfGeneralNote",
"IGESDimen_HArray1OfLeaderArrow",
"IGESDimen_LeaderArrow",
"IGESDimen_LinearDimension",
"IGESDimen_NewDimensionedGeometry",
"IGESDimen_NewGeneralNote",
"IGESDimen_OrdinateDimension",
"IGESDimen_PointDimension",
"IGESDimen_Protocol",
"IGESDimen_RadiusDimension",
"IGESDimen_ReadWriteModule",
"IGESDimen_Section",
"IGESDimen_SectionedArea",
"IGESDimen_SpecificModule",
"IGESDimen_ToolAngularDimension",
"IGESDimen_ToolBasicDimension",
"IGESDimen_ToolCenterLine",
"IGESDimen_ToolCurveDimension",
"IGESDimen_ToolDiameterDimension",
"IGESDimen_ToolDimensionDisplayData",
"IGESDimen_ToolDimensionTolerance",
"IGESDimen_ToolDimensionUnits",
"IGESDimen_ToolDimensionedGeometry",
"IGESDimen_ToolFlagNote",
"IGESDimen_ToolGeneralLabel",
"IGESDimen_ToolGeneralNote",
"IGESDimen_ToolGeneralSymbol",
"IGESDimen_ToolLeaderArrow",
"IGESDimen_ToolLinearDimension",
"IGESDimen_ToolNewDimensionedGeometry",
"IGESDimen_ToolNewGeneralNote",
"IGESDimen_ToolOrdinateDimension",
"IGESDimen_ToolPointDimension",
"IGESDimen_ToolRadiusDimension",
"IGESDimen_ToolSection",
"IGESDimen_ToolSectionedArea",
"IGESDimen_ToolWitnessLine",
"IGESDimen_WitnessLine"
]
class IGESDimen():
    """
    This package represents Entities applied to Dimensions ie. Annotation Entities and attached Properties and Associativities.
    """
    @staticmethod
    def Init_s() -> None: 
        """
        Prepares dynamic data (Protocol, Modules) for this package
        """
    @staticmethod
    def Protocol_s() -> IGESDimen_Protocol: 
        """
        Returns the Protocol for this Package
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_AngularDimension(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines AngularDimension, Type <202> Form <0> in package IGESDimen Used to dimension anglesdefines AngularDimension, Type <202> Form <0> in package IGESDimen Used to dimension anglesdefines AngularDimension, Type <202> Form <0> in package IGESDimen Used to dimension angles
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
    def FirstLeader(self) -> IGESDimen_LeaderArrow: 
        """
        returns the First Leader Entity.
        """
    def FirstWitnessLine(self) -> IGESDimen_WitnessLine: 
        """
        returns the First Witness Line Entity or Null Handle.
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstWitnessLine(self) -> bool: 
        """
        returns False if theFirstWitnessLine is Null Handle.
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
    def HasSecondWitnessLine(self) -> bool: 
        """
        returns False if theSecondWitnessLine is Null Handle.
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
    def Init(self,aNote : IGESDimen_GeneralNote,aLine : IGESDimen_WitnessLine,anotherLine : IGESDimen_WitnessLine,aVertex : OCP.gp.gp_XY,aRadius : float,aLeader : IGESDimen_LeaderArrow,anotherLeader : IGESDimen_LeaderArrow) -> None: 
        """
        This method is used to set the fields of the class AngularDimension - aNote : General Note Entity - aLine : First Witness Line Entity or Null Handle - anotherLine : Second Witness Line Entity or Null Handle - aVertex : Coordinates of vertex point - aRadius : Radius of leader arcs - aLeader : First Leader Entity - anotherLeader : Second Leader Entity
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
    def Note(self) -> IGESDimen_GeneralNote: 
        """
        returns the General Note Entity of the Dimension.
        """
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def Radius(self) -> float: 
        """
        returns the Radius of the Leader arcs.
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
    def SecondLeader(self) -> IGESDimen_LeaderArrow: 
        """
        returns the Second Leader Entity.
        """
    def SecondWitnessLine(self) -> IGESDimen_WitnessLine: 
        """
        returns the Second Witness Line Entity or Null Handle.
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
    def TransformedVertex(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the co-ordinates of the Vertex point as Pnt2d from gp after Transformation. (Z = 0.0 for Transformation)
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
    def Vertex(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the co-ordinates of the Vertex point as Pnt2d from gp.
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
class IGESDimen_Array1OfGeneralNote():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESDimen_Array1OfGeneralNote) -> IGESDimen_Array1OfGeneralNote: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESDimen_GeneralNote: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESDimen_GeneralNote: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESDimen_GeneralNote: 
        """
        Variable value access
        """
    def First(self) -> IGESDimen_GeneralNote: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESDimen_GeneralNote) -> None: 
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
    def Last(self) -> IGESDimen_GeneralNote: 
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
    def Move(self,theOther : IGESDimen_Array1OfGeneralNote) -> IGESDimen_Array1OfGeneralNote: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESDimen_GeneralNote) -> None: 
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
    def Value(self,theIndex : int) -> IGESDimen_GeneralNote: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : IGESDimen_GeneralNote,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IGESDimen_Array1OfGeneralNote) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESDimen_Array1OfLeaderArrow():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESDimen_Array1OfLeaderArrow) -> IGESDimen_Array1OfLeaderArrow: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESDimen_LeaderArrow: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESDimen_LeaderArrow: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESDimen_LeaderArrow: 
        """
        Variable value access
        """
    def First(self) -> IGESDimen_LeaderArrow: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESDimen_LeaderArrow) -> None: 
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
    def Last(self) -> IGESDimen_LeaderArrow: 
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
    def Move(self,theOther : IGESDimen_Array1OfLeaderArrow) -> IGESDimen_Array1OfLeaderArrow: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESDimen_LeaderArrow) -> None: 
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
    def Value(self,theIndex : int) -> IGESDimen_LeaderArrow: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IGESDimen_Array1OfLeaderArrow) -> None: ...
    @overload
    def __init__(self,theBegin : IGESDimen_LeaderArrow,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESDimen_BasicDimension(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    Defines IGES Basic Dimension, Type 406, Form 31, in package IGESDimen The basic Dimension Property indicates that the referencing dimension entity is to be displayed with a box around text.Defines IGES Basic Dimension, Type 406, Form 31, in package IGESDimen The basic Dimension Property indicates that the referencing dimension entity is to be displayed with a box around text.Defines IGES Basic Dimension, Type 406, Form 31, in package IGESDimen The basic Dimension Property indicates that the referencing dimension entity is to be displayed with a box around text.
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
    def Init(self,nbPropVal : int,lowerLeft : OCP.gp.gp_XY,lowerRight : OCP.gp.gp_XY,upperRight : OCP.gp.gp_XY,upperLeft : OCP.gp.gp_XY) -> None: 
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
    def LowerLeft(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns coordinates of lower left corner
        """
    def LowerRight(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns coordinates of lower right corner
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
        returns the number of properties = 8
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
    def UpperLeft(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns coordinates of upper left corner
        """
    def UpperRight(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns coordinates of upper right corner
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
class IGESDimen_CenterLine(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines CenterLine, Type <106> Form <20-21> in package IGESDimen Is an entity appearing as crosshairs or as a construction between 2 positionsdefines CenterLine, Type <106> Form <20-21> in package IGESDimen Is an entity appearing as crosshairs or as a construction between 2 positionsdefines CenterLine, Type <106> Form <20-21> in package IGESDimen Is an entity appearing as crosshairs or as a construction between 2 positions
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
    def Datatype(self) -> int: 
        """
        returns Interpretation Flag : IP = 1.
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
    def Init(self,aDataType : int,aZdisp : float,dataPnts : OCP.TColgp.TColgp_HArray1OfXY) -> None: 
        """
        This method is used to set the fields of the class CenterLine - aDataType : Interpretation Flag, always = 1 - aZDisplacement : Common z displacement - dataPnts : Data points (x and y)
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
    def IsCrossHair(self) -> bool: 
        """
        returns True if Form is 20.
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
    def NbPoints(self) -> int: 
        """
        returns Number of Data Points.
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
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns the data point as Pnt from gp. raises exception if Index <= 0 or Index > NbPoints()
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
    def SetCrossHair(self,mode : bool) -> None: 
        """
        Sets FormNumber to 20 if <mode> is True, 21 else
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
    def TransformedPoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns the data point as Pnt from gp after Transformation. raises exception if Index <= 0 or Index > NbPoints()
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
    def ZDisplacement(self) -> float: 
        """
        returns Common Z displacement.
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
class IGESDimen_CurveDimension(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines CurveDimension, Type <204> Form <0> in package IGESDimen Used to dimension curves Consists of one tail segment of nonzero length beginning with an arrowhead and which serves to define the orientationdefines CurveDimension, Type <204> Form <0> in package IGESDimen Used to dimension curves Consists of one tail segment of nonzero length beginning with an arrowhead and which serves to define the orientationdefines CurveDimension, Type <204> Form <0> in package IGESDimen Used to dimension curves Consists of one tail segment of nonzero length beginning with an arrowhead and which serves to define the orientation
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
    def FirstCurve(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the First curve Entity
        """
    def FirstLeader(self) -> IGESDimen_LeaderArrow: 
        """
        returns the First Leader Entity
        """
    def FirstWitnessLine(self) -> IGESDimen_WitnessLine: 
        """
        returns the First Witness Line Entity or a Null Handle.
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstWitnessLine(self) -> bool: 
        """
        returns False if theFirstWitnessLine is a Null Handle.
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
    def HasSecondCurve(self) -> bool: 
        """
        returns False if theSecondCurve is a Null Handle.
        """
    def HasSecondWitnessLine(self) -> bool: 
        """
        returns False if theSecondWitnessLine is a Null Handle.
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
    def Init(self,aNote : IGESDimen_GeneralNote,aCurve : OCP.IGESData.IGESData_IGESEntity,anotherCurve : OCP.IGESData.IGESData_IGESEntity,aLeader : IGESDimen_LeaderArrow,anotherLeader : IGESDimen_LeaderArrow,aLine : IGESDimen_WitnessLine,anotherLine : IGESDimen_WitnessLine) -> None: 
        """
        This method is used to set the fields of the class CurveDimension - aNote : General Note Entity - aCurve : First Curve Entity - anotherCurve : Second Curve Entity or a Null Handle - aLeader : First Leader Entity - anotherLeader : Second Leader Entity - aLine : First Witness Line Entity or a Null Handle - anotherLine : Second Witness Line Entity or a Null Handle
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
    def Note(self) -> IGESDimen_GeneralNote: 
        """
        returns the General Note Entity
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
    def SecondCurve(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Second curve Entity or a Null Handle.
        """
    def SecondLeader(self) -> IGESDimen_LeaderArrow: 
        """
        returns the Second Leader Entity
        """
    def SecondWitnessLine(self) -> IGESDimen_WitnessLine: 
        """
        returns the Second Witness Line Entity or a Null Handle.
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
class IGESDimen_DiameterDimension(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines DiameterDimension, Type <206> Form <0> in package IGESDimen Used for dimensioning diametersdefines DiameterDimension, Type <206> Form <0> in package IGESDimen Used for dimensioning diametersdefines DiameterDimension, Type <206> Form <0> in package IGESDimen Used for dimensioning diameters
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
    def Center(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the Arc Center co-ordinates as Pnt2d from package gp
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
    def FirstLeader(self) -> IGESDimen_LeaderArrow: 
        """
        returns the First Leader Entity
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
    def HasSecondLeader(self) -> bool: 
        """
        returns False if theSecondleader is a Null Handle.
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
    def Init(self,aNote : IGESDimen_GeneralNote,aLeader : IGESDimen_LeaderArrow,anotherLeader : IGESDimen_LeaderArrow,aCenter : OCP.gp.gp_XY) -> None: 
        """
        This method is used to set the fields of the class DiameterDimension - aNote : General Note Entity - aLeader : First Leader Entity - anotherLeader : Second Leader Entity or a Null Handle. - aCenter : Arc center coordinates
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
    def Note(self) -> IGESDimen_GeneralNote: 
        """
        returns the General Note Entity
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
    def SecondLeader(self) -> IGESDimen_LeaderArrow: 
        """
        returns the Second Leader Entity
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
    def TransformedCenter(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the Arc Center co-ordinates as Pnt2d from package gp after Transformation. (Z = 0.0 for Transformation)
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
class IGESDimen_DimensionDisplayData(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    Defines IGES Dimension Display Data, Type <406> Form <30>, in package IGESDimen The Dimensional Display Data Property is optional but when present must be referenced by a dimension entity. The information it contains could be extracted from the text, leader and witness line data with difficulty.Defines IGES Dimension Display Data, Type <406> Form <30>, in package IGESDimen The Dimensional Display Data Property is optional but when present must be referenced by a dimension entity. The information it contains could be extracted from the text, leader and witness line data with difficulty.Defines IGES Dimension Display Data, Type <406> Form <30>, in package IGESDimen The Dimensional Display Data Property is optional but when present must be referenced by a dimension entity. The information it contains could be extracted from the text, leader and witness line data with difficulty.
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
    def ArrowHeadOrientation(self) -> int: 
        """
        returns the arrowhead orientation
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
    def CharacterSet(self) -> int: 
        """
        returns the character set interpretation
        """
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def DecimalSymbol(self) -> int: 
        """
        None
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
    def DimensionType(self) -> int: 
        """
        returns the dimension type
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
    def EndIndex(self,Index : int) -> int: 
        """
        returns the Index'th note end index raises exception if Index <= 0 or Index > NbSupplemetaryNotes()
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
    def Init(self,numProps : int,aDimType : int,aLabelPos : int,aCharSet : int,aString : OCP.TCollection.TCollection_HAsciiString,aSymbol : int,anAng : float,anAlign : int,aLevel : int,aPlace : int,anOrient : int,initVal : float,notes : OCP.TColStd.TColStd_HArray1OfInteger,startInd : OCP.TColStd.TColStd_HArray1OfInteger,endInd : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
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
    def InitialValue(self) -> float: 
        """
        returns the primary dimension initial value
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
    def LString(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns e.g., 8HDIAMETER
        """
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def LabelPosition(self) -> int: 
        """
        returns the preferred label position
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
        returns the number of property values (14)
        """
    def NbSupplementaryNotes(self) -> int: 
        """
        returns the number of supplementary notes or zero
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
    def StartIndex(self,Index : int) -> int: 
        """
        returns the Index'th note start index raises exception if Index <= 0 or Index > NbSupplementaryNotes()
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
    def SupplementaryNote(self,Index : int) -> int: 
        """
        returns the Index'th supplementary note raises exception if Index <= 0 or Index > NbSupplementaryNotes()
        """
    def TextAlignment(self) -> int: 
        """
        returns the text alignment
        """
    def TextLevel(self) -> int: 
        """
        returns the text level
        """
    def TextPlacement(self) -> int: 
        """
        returns the preferred text placement
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
    def WitnessLineAngle(self) -> float: 
        """
        returns the witness line angle in radians
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
class IGESDimen_DimensionTolerance(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines Dimension Tolerance, Type <406>, Form <29> in package IGESDimen Provides tolerance information for a dimension which can be used by the receiving system to regenerate the dimension.defines Dimension Tolerance, Type <406>, Form <29> in package IGESDimen Provides tolerance information for a dimension which can be used by the receiving system to regenerate the dimension.defines Dimension Tolerance, Type <406>, Form <29> in package IGESDimen Provides tolerance information for a dimension which can be used by the receiving system to regenerate the dimension.
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
    def FractionFlag(self) -> int: 
        """
        returns the Fraction Flag
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
    def Init(self,nbPropVal : int,aSecTolFlag : int,aTolType : int,aTolPlaceFlag : int,anUpperTol : float,aLowerTol : float,aSignFlag : bool,aFracFlag : int,aPrecision : int) -> None: 
        """
        This method is used to set the fields of the class DimensionTolerance - nbPropVal : Number of property values, default = 8 - aSecTolFlag : Secondary Tolerance Flag 0 = Applies to primary dimension 1 = Applies to secondary dimension 2 = Display values as fractions - aTolType : Tolerance Type 1 = Bilateral 2 = Upper/Lower 3 = Unilateral Upper 4 = Unilateral Lower 5 = Range - min before max 6 = Range - min after max 7 = Range - min above max 8 = Range - min below max 9 = Nominal + Range - min above max 10 = Nominal + Range - min below max - aTolPlaceFlag : Tolerance Placement Flag 1 = Before nominal value 2 = After nominal value 3 = Above nominal value 4 = Below nominal value - anUpperTol : Upper Tolerance - aLowerTol : Lower Tolerance - aSignFlag : Sign Suppression Flag - aFracFlag : Fraction Flag 0 = Display values as decimal numbers 1 = Display values as mixed fractions 2 = Display values as fractions - aPrecision : Precision Value
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
    def LowerTolerance(self) -> float: 
        """
        returns the Lower Tolerance Value
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
        returns the number of property values, always = 8
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def Precision(self) -> int: 
        """
        returns the Precision for Value Display
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
    def SecondaryToleranceFlag(self) -> int: 
        """
        returns the Secondary Tolerance Flag
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
    def SignSuppressionFlag(self) -> bool: 
        """
        returns the Sign Suppression Flag
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
    def TolerancePlacementFlag(self) -> int: 
        """
        returns the Tolerance Placement Flag, default = 2
        """
    def ToleranceType(self) -> int: 
        """
        returns the Tolerance Type
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
    def UpperTolerance(self) -> float: 
        """
        returns the Upper or Bilateral Tolerance Value
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
class IGESDimen_DimensionUnits(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines Dimension Units, Type <406>, Form <28> in package IGESDimen Describes the units and formatting details of the nominal value of a dimension.defines Dimension Units, Type <406>, Form <28> in package IGESDimen Describes the units and formatting details of the nominal value of a dimension.defines Dimension Units, Type <406>, Form <28> in package IGESDimen Describes the units and formatting details of the nominal value of a dimension.
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
    def CharacterSet(self) -> int: 
        """
        returns the character set interpretation
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
    def FormatString(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the string used in formatting value
        """
    def FractionFlag(self) -> int: 
        """
        returns the fraction flag
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
    def Init(self,nbPropVal : int,aSecondPos : int,aUnitsInd : int,aCharSet : int,aFormat : OCP.TCollection.TCollection_HAsciiString,aFracFlag : int,aPrecision : int) -> None: 
        """
        This method is used to set the fields of the class DimensionUnits - nbPropVal : Number of property values, always = 6 - aSecondPos : Secondary Dimension Position 0 = This is the main text 1 = Before primary dimension 2 = After primary dimension 3 = Above primary dimension 4 = Below primary dimension - aUnitsInd : Units Indicator - aCharSet : Character Set used - aFormat : Format HAsciiString 1 = Standard ASCII 1001 = Symbol Font 1 1002 = Symbol Font 2 1003 = Drafting Font - aFracFlag : Fraction Flag 0 = Display values as decimal numbers 1 = Display values as fractions - aPrecision : Precision Value
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
        returns the number of property values
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def PrecisionOrDenominator(self) -> int: 
        """
        returns the precision/denominator number of decimal places when FractionFlag() = 0 denominator of fraction when FractionFlag() = 1
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
    def SecondaryDimenPosition(self) -> int: 
        """
        returns position of secondary dimension w.r.t. primary dimension
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
    def UnitsIndicator(self) -> int: 
        """
        returns the units indicator
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
class IGESDimen_DimensionedGeometry(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    Defines IGES Dimensioned Geometry, Type <402> Form <13>, in package IGESDimen This entity has been replaced by the new form of Dimensioned Geometry Associativity Entity (Type 402, Form 21) and should no longer be used by preprocessors.Defines IGES Dimensioned Geometry, Type <402> Form <13>, in package IGESDimen This entity has been replaced by the new form of Dimensioned Geometry Associativity Entity (Type 402, Form 21) and should no longer be used by preprocessors.Defines IGES Dimensioned Geometry, Type <402> Form <13>, in package IGESDimen This entity has been replaced by the new form of Dimensioned Geometry Associativity Entity (Type 402, Form 21) and should no longer be used by preprocessors.
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
    def DimensionEntity(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Dimension entity
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
    def GeometryEntity(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the num'th Geometry entity raises exception if Index <= 0 or Index > NbGeometryEntities()
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
    def Init(self,nbDims : int,aDimension : OCP.IGESData.IGESData_IGESEntity,entities : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
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
    def NbDimensions(self) -> int: 
        """
        returns the number of dimensions
        """
    def NbGeometryEntities(self) -> int: 
        """
        returns the number of associated geometry entities
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
class IGESDimen_FlagNote(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines FlagNote, Type <208> Form <0> in package IGESDimen Is label information formatted in different waysdefines FlagNote, Type <208> Form <0> in package IGESDimen Is label information formatted in different waysdefines FlagNote, Type <208> Form <0> in package IGESDimen Is label information formatted in different ways
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def Angle(self) -> float: 
        """
        returns Rotation angle in radians
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
    def CharacterHeight(self) -> float: 
        """
        returns the Character Height (from General Note)
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
    def Height(self) -> float: 
        """
        returns Height computed by the formula : Height = 2 * CH where CH is from theNote
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
    def Init(self,leftCorner : OCP.gp.gp_XYZ,anAngle : float,aNote : IGESDimen_GeneralNote,someLeaders : IGESDimen_HArray1OfLeaderArrow) -> None: 
        """
        This method is used to set the fields of the class FlagNote - leftCorner : Lower left corner of the Flag - anAngle : Rotation angle in radians - aNote : General Note Entity - someLeaders : Leader Entities
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
    def Leader(self,Index : int) -> IGESDimen_LeaderArrow: 
        """
        returns Leader Entity raises exception if Index <= 0 or Index > NbLeaders()
        """
    def Length(self) -> float: 
        """
        returns Length computed by the formula : Length = TW + 0.4*CH where CH is from theNote and TW is from theNote
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
    def LowerLeftCorner(self) -> OCP.gp.gp_Pnt: 
        """
        returns Lower Left coordinate of Flag as Pnt from package gp
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbLeaders(self) -> int: 
        """
        returns number of Arrows (Leaders) or zero
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
    def Note(self) -> IGESDimen_GeneralNote: 
        """
        returns General Note Entity
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
    def TextWidth(self) -> float: 
        """
        returns the Text Width (from General Note)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TipLength(self) -> float: 
        """
        returns TipLength computed by the formula : TipLength = 0.5 * H / tan 35(deg) where H is Height()
        """
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TransformedLowerLeftCorner(self) -> OCP.gp.gp_Pnt: 
        """
        returns Lower Left coordinate of Flag as Pnt from package gp after Transformation.
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
class IGESDimen_GeneralLabel(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines GeneralLabel, Type <210> Form <0> in package IGESDimen Used for general labeling with leadersdefines GeneralLabel, Type <210> Form <0> in package IGESDimen Used for general labeling with leadersdefines GeneralLabel, Type <210> Form <0> in package IGESDimen Used for general labeling with leaders
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
    def Init(self,aNote : IGESDimen_GeneralNote,someLeaders : IGESDimen_HArray1OfLeaderArrow) -> None: 
        """
        This method is used to set the fields of the class GeneralLabel - aNote : General Note Entity - someLeaders : Associated Leader Entities
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
    def Leader(self,Index : int) -> IGESDimen_LeaderArrow: 
        """
        returns Leader Entity raises exception if Index <= 0 or Index > NbLeaders()
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
    def NbLeaders(self) -> int: 
        """
        returns Number of Leaders
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
    def Note(self) -> IGESDimen_GeneralNote: 
        """
        returns General Note Entity
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
class IGESDimen_GeneralModule(OCP.IGESData.IGESData_GeneralModule, OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    Definition of General Services for IGESDimen (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESDimen (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESDimen (specific part) This Services comprise : Shared & Implied Lists, Copy, Check
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
class IGESDimen_GeneralNote(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines GeneralNote, Type <212> Form <0-8, 100-200, 105> in package IGESDimen Used for formatting boxed text in different waysdefines GeneralNote, Type <212> Form <0-8, 100-200, 105> in package IGESDimen Used for formatting boxed text in different waysdefines GeneralNote, Type <212> Form <0-8, 100-200, 105> in package IGESDimen Used for formatting boxed text in different ways
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
    def BoxHeight(self,Index : int) -> float: 
        """
        returns Box height of string raises exception if Index <= 0 or Index > NbStrings()
        """
    def BoxWidth(self,Index : int) -> float: 
        """
        returns Box width of string raises exception if Index <= 0 or Index > NbStrings()
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
    def FontCode(self,Index : int) -> int: 
        """
        returns Font code (default = 1) of string returns 0 if IsFontEntity () is True raises exception if Index <= 0 or Index > NbStrings()
        """
    def FontEntity(self,Index : int) -> OCP.IGESGraph.IGESGraph_TextFontDef: 
        """
        returns Text Font Definition Entity of string returns a Null Handle if IsFontEntity () returns False raises exception if Index <= 0 or Index > NbStrings()
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
    def Init(self,nbChars : OCP.TColStd.TColStd_HArray1OfInteger,widths : OCP.TColStd.TColStd_HArray1OfReal,heights : OCP.TColStd.TColStd_HArray1OfReal,fontCodes : OCP.TColStd.TColStd_HArray1OfInteger,fonts : OCP.IGESGraph.IGESGraph_HArray1OfTextFontDef,slants : OCP.TColStd.TColStd_HArray1OfReal,rotations : OCP.TColStd.TColStd_HArray1OfReal,mirrorFlags : OCP.TColStd.TColStd_HArray1OfInteger,rotFlags : OCP.TColStd.TColStd_HArray1OfInteger,start : OCP.TColgp.TColgp_HArray1OfXYZ,texts : OCP.Interface.Interface_HArray1OfHAsciiString) -> None: 
        """
        This method is used to set the fields of the class GeneralNote - nNbChars : number of chars strings - widths : Box widths - heights : Box heights - fontCodes : Font codes, default = 1 - fonts : Text Font Definition Entities - slants : Slant angles in radians - rotations : Rotation angles in radians - mirrorFlags : Mirror flags - rotFlags : Rotation internal text flags - start : Text start points - texts : Text strings raises exception if there is mismatch between the various Array Lengths.
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
    def IsFontEntity(self,Index : int) -> bool: 
        """
        returns False if Value, True if Entity raises exception if Index <= 0 or Index > NbStrings()
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
    def MirrorFlag(self,Index : int) -> int: 
        """
        returns Mirror Flag of string 0 = no mirroring 1 = mirror axis is perpendicular to the text base line 2 = mirror axis is text base line raises exception if Index <= 0 or Index > NbStrings()
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbCharacters(self,Index : int) -> int: 
        """
        returns number of characters of string or zero raises exception if Index <= 0 or Index > NbStrings()
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbStrings(self) -> int: 
        """
        returns number of text strings in General Note
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
    def RotateFlag(self,Index : int) -> int: 
        """
        returns Rotate internal text Flag of string 0 = text horizontal 1 = text vertical raises exception if Index <= 0 or Index > NbStrings()
        """
    def RotationAngle(self,Index : int) -> float: 
        """
        returns Rotation angle of string in radians raises exception if Index <= 0 or Index > NbStrings()
        """
    def SetFormNumber(self,form : int) -> None: 
        """
        Changes FormNumber (indicates Graphical Representation) Error if not in ranges [0-8] or [100-102] or 105
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
    def SlantAngle(self,Index : int) -> float: 
        """
        returns Slant angle of string in radians default value = PI/2 raises exception if Index <= 0 or Index > NbStrings()
        """
    def StartPoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns text start point of Index'th string raises exception if Index <= 0 or Index > NbStrings()
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
    def Text(self,Index : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns text string raises exception if Index <= 0 or Index > NbStrings()
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TransformedStartPoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns text start point of Index'th string after Transformation raises exception if Index <= 0 or Index > NbStrings()
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
    def ZDepthStartPoint(self,Index : int) -> float: 
        """
        returns distance from Start Point plane of string raises exception if Index <= 0 or Index > NbStrings()
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
class IGESDimen_GeneralSymbol(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines General Symbol, Type <228>, Form <0-3,5001-9999> in package IGESDimen Consists of zero or one (Form 0) or one (all other forms), one or more geometry entities which define a symbol, and zero, one or more associated leaders.defines General Symbol, Type <228>, Form <0-3,5001-9999> in package IGESDimen Consists of zero or one (Form 0) or one (all other forms), one or more geometry entities which define a symbol, and zero, one or more associated leaders.defines General Symbol, Type <228>, Form <0-3,5001-9999> in package IGESDimen Consists of zero or one (Form 0) or one (all other forms), one or more geometry entities which define a symbol, and zero, one or more associated leaders.
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
    def GeomEntity(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Index'th Geometry Entity raises exception if Index <= 0 or Index > NbGeomEntities()
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
    def HasNote(self) -> bool: 
        """
        returns True if there is associated General Note Entity
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
    def Init(self,aNote : IGESDimen_GeneralNote,allGeoms : OCP.IGESData.IGESData_HArray1OfIGESEntity,allLeaders : IGESDimen_HArray1OfLeaderArrow) -> None: 
        """
        This method is used to set the fields of the class GeneralSymbol - aNote : General Note, null for form 0 - allGeoms : Geometric Entities - allLeaders : Leader Arrows
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
    def LeaderArrow(self,Index : int) -> IGESDimen_LeaderArrow: 
        """
        returns the Index'th Leader Arrow raises exception if Index <= 0 or Index > NbLeaders()
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
    def NbGeomEntities(self) -> int: 
        """
        returns number of Geometry Entities
        """
    def NbLeaders(self) -> int: 
        """
        returns number of Leaders or zero if not specified
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
    def Note(self) -> IGESDimen_GeneralNote: 
        """
        returns Null handle for form 0 only
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
        Changes FormNumber (indicates the Nature of the Symbole) Error if not in ranges [0-3] or [> 5000]
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
class IGESDimen_HArray1OfGeneralNote(IGESDimen_Array1OfGeneralNote, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESDimen_Array1OfGeneralNote: 
        """
        None
        """
    def Assign(self,theOther : IGESDimen_Array1OfGeneralNote) -> IGESDimen_Array1OfGeneralNote: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESDimen_Array1OfGeneralNote: 
        """
        None
        """
    def ChangeFirst(self) -> IGESDimen_GeneralNote: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESDimen_GeneralNote: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESDimen_GeneralNote: 
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
    def First(self) -> IGESDimen_GeneralNote: 
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
    def Init(self,theValue : IGESDimen_GeneralNote) -> None: 
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
    def Last(self) -> IGESDimen_GeneralNote: 
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
    def Move(self,theOther : IGESDimen_Array1OfGeneralNote) -> IGESDimen_Array1OfGeneralNote: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESDimen_GeneralNote) -> None: 
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
    def Value(self,theIndex : int) -> IGESDimen_GeneralNote: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : IGESDimen_Array1OfGeneralNote) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESDimen_GeneralNote) -> None: ...
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
class IGESDimen_HArray1OfLeaderArrow(IGESDimen_Array1OfLeaderArrow, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESDimen_Array1OfLeaderArrow: 
        """
        None
        """
    def Assign(self,theOther : IGESDimen_Array1OfLeaderArrow) -> IGESDimen_Array1OfLeaderArrow: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESDimen_Array1OfLeaderArrow: 
        """
        None
        """
    def ChangeFirst(self) -> IGESDimen_LeaderArrow: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESDimen_LeaderArrow: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESDimen_LeaderArrow: 
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
    def First(self) -> IGESDimen_LeaderArrow: 
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
    def Init(self,theValue : IGESDimen_LeaderArrow) -> None: 
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
    def Last(self) -> IGESDimen_LeaderArrow: 
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
    def Move(self,theOther : IGESDimen_Array1OfLeaderArrow) -> IGESDimen_Array1OfLeaderArrow: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESDimen_LeaderArrow) -> None: 
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
    def Value(self,theIndex : int) -> IGESDimen_LeaderArrow: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IGESDimen_Array1OfLeaderArrow) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESDimen_LeaderArrow) -> None: ...
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
class IGESDimen_LeaderArrow(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines LeaderArrow, Type <214> Form <1-12> in package IGESDimen Consists of one or more line segments except when leader is part of an angular dimension, with links to presumed text itemdefines LeaderArrow, Type <214> Form <1-12> in package IGESDimen Consists of one or more line segments except when leader is part of an angular dimension, with links to presumed text itemdefines LeaderArrow, Type <214> Form <1-12> in package IGESDimen Consists of one or more line segments except when leader is part of an angular dimension, with links to presumed text item
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
    def ArrowHead(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns ArrowHead co-ordinates
        """
    def ArrowHeadHeight(self) -> float: 
        """
        returns ArrowHead height
        """
    def ArrowHeadWidth(self) -> float: 
        """
        returns ArrowHead width
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
    def Init(self,height : float,width : float,depth : float,position : OCP.gp.gp_XY,segments : OCP.TColgp.TColgp_HArray1OfXY) -> None: 
        """
        This method is used to set the fields of the class LeaderArrow - height : ArrowHead height - width : ArrowHead width - depth : Z Depth - position : ArrowHead coordinates - segments : Segment tail coordinate pairs
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
    def NbSegments(self) -> int: 
        """
        returns number of segments
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
    def SegmentTail(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        returns segment tail co-ordinates. raises exception if Index <= 0 or Index > NbSegments
        """
    def SetFormNumber(self,form : int) -> None: 
        """
        Changes FormNumber (indicates the Shape of the Arrow) Error if not in range [0-12]
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
    def TransformedArrowHead(self) -> OCP.gp.gp_Pnt: 
        """
        returns ArrowHead co-ordinates after Transformation
        """
    def TransformedSegmentTail(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns segment tail co-ordinates after Transformation. raises exception if Index <= 0 or Index > NbSegments
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
    def ZDepth(self) -> float: 
        """
        returns Z depth
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
class IGESDimen_LinearDimension(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines LinearDimension, Type <216> Form <0> in package IGESDimen Used for linear dimensioningdefines LinearDimension, Type <216> Form <0> in package IGESDimen Used for linear dimensioningdefines LinearDimension, Type <216> Form <0> in package IGESDimen Used for linear dimensioning
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
    def FirstLeader(self) -> IGESDimen_LeaderArrow: 
        """
        returns first Leader Entity
        """
    def FirstWitness(self) -> IGESDimen_WitnessLine: 
        """
        returns first Witness Line Entity or a Null Handle
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstWitness(self) -> bool: 
        """
        returns False if no first witness line
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
    def HasSecondWitness(self) -> bool: 
        """
        returns False if no second witness line
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
    def Init(self,aNote : IGESDimen_GeneralNote,aLeader : IGESDimen_LeaderArrow,anotherLeader : IGESDimen_LeaderArrow,aWitness : IGESDimen_WitnessLine,anotherWitness : IGESDimen_WitnessLine) -> None: 
        """
        This method is used to set the fields of the class LinearDimension - aNote : General Note Entity - aLeader : First Leader Entity - anotherLeader : Second Leader Entity - aWitness : First Witness Line Entity or a Null Handle - anotherWitness : Second Witness Line Entity or a Null Handle
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
    def Note(self) -> IGESDimen_GeneralNote: 
        """
        returns General Note Entity
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
    def SecondLeader(self) -> IGESDimen_LeaderArrow: 
        """
        returns second Leader Entity
        """
    def SecondWitness(self) -> IGESDimen_WitnessLine: 
        """
        returns second Witness Line Entity or a Null Handle
        """
    def SetFormNumber(self,form : int) -> None: 
        """
        Changes FormNumber (indicates the Nature of the Dimension Unspecified, Diameter or Radius) Error if not in range [0-2]
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
class IGESDimen_NewDimensionedGeometry(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines New Dimensioned Geometry, Type <402>, Form <21> in package IGESDimen Links a dimension entity with the geometry entities it is dimensioning, so that later, in the receiving database, the dimension can be automatically recalculated and redrawn should the geometry be changed.defines New Dimensioned Geometry, Type <402>, Form <21> in package IGESDimen Links a dimension entity with the geometry entities it is dimensioning, so that later, in the receiving database, the dimension can be automatically recalculated and redrawn should the geometry be changed.defines New Dimensioned Geometry, Type <402>, Form <21> in package IGESDimen Links a dimension entity with the geometry entities it is dimensioning, so that later, in the receiving database, the dimension can be automatically recalculated and redrawn should the geometry be changed.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def AngleValue(self) -> float: 
        """
        returns the angle value
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
    def DimensionEntity(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the dimension entity
        """
    def DimensionLocationFlag(self,Index : int) -> int: 
        """
        returns the Index'th geometry entity's dimension location flag raises exception if Index <= 0 or Index > NbGeometries()
        """
    def DimensionOrientationFlag(self) -> int: 
        """
        returns the dimension orientation flag
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
    def GeometryEntity(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Index'th geometry entity raises exception if Index <= 0 or Index > NbGeometries()
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
    def Init(self,nbDimens : int,aDimen : OCP.IGESData.IGESData_IGESEntity,anOrientation : int,anAngle : float,allEntities : OCP.IGESData.IGESData_HArray1OfIGESEntity,allLocations : OCP.TColStd.TColStd_HArray1OfInteger,allPoints : OCP.TColgp.TColgp_HArray1OfXYZ) -> None: 
        """
        This method is used to set the fields of the class NewDimensionedGeometry - nbDimen : Number of Dimensions, default = 1 - aDimen : Dimension Entity - anOrientation : Dimension Orientation Flag - anAngle : Angle Value - allEntities : Geometric Entities - allLocations : Dimension Location Flags - allPoints : Points on the Geometry Entities exception raised if lengths of entities, locations, points are not the same
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
    def NbDimensions(self) -> int: 
        """
        returns the number of dimensions
        """
    def NbGeometries(self) -> int: 
        """
        returns the number of associated geometry entities
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
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        coordinate of point on Index'th geometry entity raises exception if Index <= 0 or Index > NbGeometries()
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
    def TransformedPoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        coordinate of point on Index'th geometry entity after Transformation raises exception if Index <= 0 or Index > NbGeometries()
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
class IGESDimen_NewGeneralNote(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines NewGeneralNote, Type <213> Form <0> in package IGESDimen Further attributes for formatting text stringsdefines NewGeneralNote, Type <213> Form <0> in package IGESDimen Further attributes for formatting text stringsdefines NewGeneralNote, Type <213> Form <0> in package IGESDimen Further attributes for formatting text strings
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
    def AreaLocation(self) -> OCP.gp.gp_Pnt: 
        """
        returns Text containment area Location point
        """
    def AreaRotationAngle(self) -> float: 
        """
        returns rotation angle of text containment area in radians
        """
    def Associate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Sets "me" in the Associativity list of another Entity
        """
    def Associativities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Associativity List under the form of an EntityIterator.
        """
    def BaseLinePosition(self) -> OCP.gp.gp_Pnt: 
        """
        returns position of first base line
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def BoxHeight(self,Index : int) -> float: 
        """
        returns Box height of string raises exception if Index <= 0 or Index > NbStrings()
        """
    def BoxWidth(self,Index : int) -> float: 
        """
        returns Box width of string raises exception if Index <= 0 or Index > NbStrings()
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def CharSetCode(self,Index : int) -> int: 
        """
        returns Character Set Interpretation (default = 1) of string returns 0 if IsCharSetEntity () is True 1 = Standard ASCII 1001 = Symbol Font1 1002 = Symbol Font2 1003 = Symbol Font3 raises exception if Index <= 0 or Index > NbStrings()
        """
    def CharSetEntity(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns Character Set Interpretation of string returns a Null Handle if IsCharSetEntity () is False raises exception if Index <= 0 or Index > NbStrings()
        """
    def CharacterAngle(self,Index : int) -> float: 
        """
        returns CharacterAngle of string Angle returned will be between 0 and 2PI raises exception if Index <= 0 or Index > NbStrings()
        """
    def CharacterDisplay(self,Index : int) -> int: 
        """
        returns Fixed/Variable width character display of string 0 = Fixed 1 = Variable raises exception if Index <= 0 or Index > NbStrings()
        """
    def CharacterHeight(self,Index : int) -> float: 
        """
        returns Character Height of string raises exception if Index <= 0 or Index > NbStrings()
        """
    def CharacterWidth(self,Index : int) -> float: 
        """
        returns Character Width of string raises exception if Index <= 0 or Index > NbStrings()
        """
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompoundLocation(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location by taking in account a Parent which has its own Location : that one will be combined to that of <me> The Parent is considered only if HasOneParent is True, else it is ignored and CompoundLocation = Location
        """
    def ControlCodeString(self,Index : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns ControlCodeString of string raises exception if Index <= 0 or Index > NbStrings()
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
    def FontStyle(self,Index : int) -> int: 
        """
        returns FontStyle of string raises exception if Index <= 0 or Index > NbStrings()
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
    def Init(self,width : float,height : float,justifyCode : int,areaLoc : OCP.gp.gp_XYZ,areaRotationAngle : float,baseLinePos : OCP.gp.gp_XYZ,normalInterlineSpace : float,charDisplays : OCP.TColStd.TColStd_HArray1OfInteger,charWidths : OCP.TColStd.TColStd_HArray1OfReal,charHeights : OCP.TColStd.TColStd_HArray1OfReal,interCharSpc : OCP.TColStd.TColStd_HArray1OfReal,interLineSpc : OCP.TColStd.TColStd_HArray1OfReal,fontStyles : OCP.TColStd.TColStd_HArray1OfInteger,charAngles : OCP.TColStd.TColStd_HArray1OfReal,controlCodeStrings : OCP.Interface.Interface_HArray1OfHAsciiString,nbChars : OCP.TColStd.TColStd_HArray1OfInteger,boxWidths : OCP.TColStd.TColStd_HArray1OfReal,boxHeights : OCP.TColStd.TColStd_HArray1OfReal,charSetCodes : OCP.TColStd.TColStd_HArray1OfInteger,charSetEntities : OCP.IGESData.IGESData_HArray1OfIGESEntity,slAngles : OCP.TColStd.TColStd_HArray1OfReal,rotAngles : OCP.TColStd.TColStd_HArray1OfReal,mirrorFlags : OCP.TColStd.TColStd_HArray1OfInteger,rotateFlags : OCP.TColStd.TColStd_HArray1OfInteger,startPoints : OCP.TColgp.TColgp_HArray1OfXYZ,texts : OCP.Interface.Interface_HArray1OfHAsciiString) -> None: 
        """
        This method is used to set the fields of the class NewGeneralNote - width : Width of text containment area - height : Height of text containment area - justifyCode : Justification code - areaLoc : Text containment area location - areaRotationAngle : Text containment area rotation - baseLinePos : Base line position - normalInterlineSpace : Normal interline spacing - charDisplays : Character display type - charWidths : Character width - charHeights : Character height - interCharSpc : Intercharacter spacing - interLineSpc : Interline spacing - fontStyles : Font style - charAngles : Character angle - controlCodeStrings : Control Code string - nbChars : Number of characters in string - boxWidths : Box width - boxHeights : Box height - charSetCodes : Character Set Interpretation - charSetEntities : Character Set Font - slAngles : Slant angle of text in radians - rotAngles : Rotation angle of text in radians - mirrorFlags : Type of mirroring - rotateFlags : Rotate internal text flag - startPoints : Text start point - texts : Text strings raises exception if there is mismatch between the various Array Lengths.
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
    def InterCharacterSpace(self,Index : int) -> float: 
        """
        returns Inter-character spacing of string raises exception if Index <= 0 or Index > NbStrings()
        """
    def InterlineSpace(self,Index : int) -> float: 
        """
        returns Interline spacing of string raises exception if Index <= 0 or Index > NbStrings()
        """
    def IsCharSetEntity(self,Index : int) -> bool: 
        """
        returns False if Value, True if Pointer (Entity) raises exception if Index <= 0 or Index > NbStrings()
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
    def IsMirrored(self,Index : int) -> bool: 
        """
        returns False if MirrorFlag = 0. ie. no mirroring else returns True raises exception if Index <= 0 or Index > NbStrings()
        """
    def IsVariable(self,Index : int) -> bool: 
        """
        returns False if Character display width is Fixed optional method, if required raises exception if Index <= 0 or Index > NbStrings()
        """
    def JustifyCode(self) -> int: 
        """
        returns Justification code of all strings within the note 0 = no justification 1 = right justified 2 = center justified 3 = left justified
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
    def MirrorFlag(self,Index : int) -> int: 
        """
        returns Mirror Flag of string 0 = no mirroring 1 = mirror axis is perpendicular to the text base line 2 = mirror axis is text base line raises exception if Index <= 0 or Index > NbStrings()
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbCharacters(self,Index : int) -> int: 
        """
        returns number of characters in string or zero raises exception if Index <= 0 or Index > NbStrings()
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbStrings(self) -> int: 
        """
        returns number of text HAsciiStrings
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def NormalInterlineSpace(self) -> float: 
        """
        returns Normal Interline Spacing
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
    def RotateFlag(self,Index : int) -> int: 
        """
        returns Rotate internal text Flag of string 0 = text horizontal 1 = text vertical raises exception if Index <= 0 or Index > NbStrings()
        """
    def RotationAngle(self,Index : int) -> float: 
        """
        returns Rotation angle of string in radians raises exception if Index <= 0 or Index > NbStrings()
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
    def SlantAngle(self,Index : int) -> float: 
        """
        returns Slant angle of string in radians default value = PI/2 raises exception if Index <= 0 or Index > NbStrings()
        """
    def StartPoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns text start point of string raises exception if Index <= 0 or Index > NbStrings()
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
    def Text(self,Index : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns text string raises exception if Index <= 0 or Index > NbStrings()
        """
    def TextHeight(self) -> float: 
        """
        returns height of text containment area of all strings in the note
        """
    def TextWidth(self) -> float: 
        """
        returns width of text containment area of all strings in the note
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TransformedAreaLocation(self) -> OCP.gp.gp_Pnt: 
        """
        returns Text containment area Location point after Transformation
        """
    def TransformedBaseLinePosition(self) -> OCP.gp.gp_Pnt: 
        """
        returns position of first base line after Transformation
        """
    def TransformedStartPoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns text start point of string after Transformation raises exception if Index <= 0 or Index > NbStrings()
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
    def ZDepthAreaLocation(self) -> float: 
        """
        returns distance from the containment area plane
        """
    def ZDepthBaseLinePosition(self) -> float: 
        """
        returns distance from the Base line position plane
        """
    def ZDepthStartPoint(self,Index : int) -> float: 
        """
        returns distance from the start point plane raises exception if Index <= 0 or Index > NbStrings()
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
class IGESDimen_OrdinateDimension(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Ordinate Dimension, Type <218> Form <0, 1>, in package IGESDimen Note : The ordinate dimension entity is used to indicate dimensions from a common base line. Dimensioning is only permitted along the XT or YT axis.defines IGES Ordinate Dimension, Type <218> Form <0, 1>, in package IGESDimen Note : The ordinate dimension entity is used to indicate dimensions from a common base line. Dimensioning is only permitted along the XT or YT axis.defines IGES Ordinate Dimension, Type <218> Form <0, 1>, in package IGESDimen Note : The ordinate dimension entity is used to indicate dimensions from a common base line. Dimensioning is only permitted along the XT or YT axis.
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
    def Init(self,aNote : IGESDimen_GeneralNote,aType : bool,aLine : IGESDimen_WitnessLine,anArrow : IGESDimen_LeaderArrow) -> None: 
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
    def IsLeader(self) -> bool: 
        """
        returns True if Leader and False if Witness Line (only for Form 0)
        """
    def IsLine(self) -> bool: 
        """
        returns True if Witness Line and False if Leader (only for Form 0)
        """
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def Leader(self) -> IGESDimen_LeaderArrow: 
        """
        returns the Leader associated or Null handle
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
    def Note(self) -> IGESDimen_GeneralNote: 
        """
        returns the General Note entity associated.
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
    def WitnessLine(self) -> IGESDimen_WitnessLine: 
        """
        returns the Witness Line associated or Null handle
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
class IGESDimen_PointDimension(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Point Dimension, Type <220> Form <0>, in package IGESDimen A Point Dimension Entity consists of a leader, text, and an optional circle or hexagon enclosing the text IGES specs for this entity mention SimpleClosedPlanarCurve Entity(106/63)which is not listed in LIST.Text In the sequel we have ignored this & considered only the other two entity for representing the hexagon or circle enclosing the text.defines IGES Point Dimension, Type <220> Form <0>, in package IGESDimen A Point Dimension Entity consists of a leader, text, and an optional circle or hexagon enclosing the text IGES specs for this entity mention SimpleClosedPlanarCurve Entity(106/63)which is not listed in LIST.Text In the sequel we have ignored this & considered only the other two entity for representing the hexagon or circle enclosing the text.defines IGES Point Dimension, Type <220> Form <0>, in package IGESDimen A Point Dimension Entity consists of a leader, text, and an optional circle or hexagon enclosing the text IGES specs for this entity mention SimpleClosedPlanarCurve Entity(106/63)which is not listed in LIST.Text In the sequel we have ignored this & considered only the other two entity for representing the hexagon or circle enclosing the text.
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
    def CircularArc(self) -> OCP.IGESGeom.IGESGeom_CircularArc: 
        """
        returns Null handle if GeomCase(me) .ne. 1
        """
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def CompositeCurve(self) -> OCP.IGESGeom.IGESGeom_CompositeCurve: 
        """
        returns Null handle if GeomCase(me) .ne. 2
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
    def Geom(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Geometry Entity, Null handle if GeomCase(me) .eq. 0
        """
    def GeomCase(self) -> int: 
        """
        returns the type of geometric entity. 0 if no hexagon or circle encloses the text 1 if CircularArc 2 if CompositeCurve 3 otherwise
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
    def Init(self,aNote : IGESDimen_GeneralNote,anArrow : IGESDimen_LeaderArrow,aGeom : OCP.IGESData.IGESData_IGESEntity) -> None: 
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
    def LeaderArrow(self) -> IGESDimen_LeaderArrow: 
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
    def Note(self) -> IGESDimen_GeneralNote: 
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
class IGESDimen_Protocol(OCP.IGESData.IGESData_Protocol, OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    Description of Protocol for IGESDimenDescription of Protocol for IGESDimenDescription of Protocol for IGESDimen
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
        Gives the count of Resource Protocol. Here, two (Protocols from IGESGraph and IGESGeom)
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
class IGESDimen_RadiusDimension(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    Defines IGES Radius Dimension, type <222> Form <0, 1>, in package IGESDimen. A Radius Dimension Entity consists of a General Note, a leader, and an arc center point. A second form of this entity accounts for the occasional need to have two leader entities referenced.Defines IGES Radius Dimension, type <222> Form <0, 1>, in package IGESDimen. A Radius Dimension Entity consists of a General Note, a leader, and an arc center point. A second form of this entity accounts for the occasional need to have two leader entities referenced.Defines IGES Radius Dimension, type <222> Form <0, 1>, in package IGESDimen. A Radius Dimension Entity consists of a General Note, a leader, and an arc center point. A second form of this entity accounts for the occasional need to have two leader entities referenced.
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
    def Center(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the coordinates of the Arc Center
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
    def HasLeader2(self) -> bool: 
        """
        returns True if form is 1, False if 0
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
    def Init(self,aNote : IGESDimen_GeneralNote,anArrow : IGESDimen_LeaderArrow,arcCenter : OCP.gp.gp_XY,anotherArrow : IGESDimen_LeaderArrow) -> None: 
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
    def InitForm(self,form : int) -> None: 
        """
        Allows to change Form Number (1 admits null arrow)
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
    def Leader(self) -> IGESDimen_LeaderArrow: 
        """
        returns the Leader Arrow entity
        """
    def Leader2(self) -> IGESDimen_LeaderArrow: 
        """
        returns Null handle if Form is 0
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
    def Note(self) -> IGESDimen_GeneralNote: 
        """
        returns the General Note entity
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
    def TransformedCenter(self) -> OCP.gp.gp_Pnt: 
        """
        returns the coordinates of the Arc Center after Transformation (Z coord taken from ZDepth of Leader Entity)
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
class IGESDimen_ReadWriteModule(OCP.IGESData.IGESData_ReadWriteModule, OCP.Interface.Interface_ReaderModule, OCP.Standard.Standard_Transient):
    """
    Defines Dimen File Access Module for IGESDimen (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntityDefines Dimen File Access Module for IGESDimen (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntityDefines Dimen File Access Module for IGESDimen (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity
    """
    def CaseIGES(self,typenum : int,formnum : int) -> int: 
        """
        Defines Case Numbers for Entities of IGESDimen
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
        Reads own parameters from file for an Entity of IGESDimen
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
class IGESDimen_Section(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines Section, Type <106> Form <31-38> in package IGESDimen Contains information to display sectioned sidesdefines Section, Type <106> Form <31-38> in package IGESDimen Contains information to display sectioned sidesdefines Section, Type <106> Form <31-38> in package IGESDimen Contains information to display sectioned sides
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
    def Datatype(self) -> int: 
        """
        returns Interpretation Flag, always = 1
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
    def Init(self,dataType : int,aDisp : float,dataPoints : OCP.TColgp.TColgp_HArray1OfXY) -> None: 
        """
        This method is used to set the fields of the class Section - dataType : Interpretation Flag, always = 1 - aDisp : Common z displacement - dataPoints : Data points
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
    def NbPoints(self) -> int: 
        """
        returns number of Data Points
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
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns Index'th data point raises exception if Index <= 0 or Index > NbPoints()
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
        Changes FormNumber (indicates the Type of the Hatches) Error if not in range [31-38]
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
    def TransformedPoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns Index'th data point after Transformation raises exception if Index <= 0 or Index > NbPoints()
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
    def ZDisplacement(self) -> float: 
        """
        returns common Z displacement
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
class IGESDimen_SectionedArea(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Sectioned Area, Type <230> Form <0>, in package IGESDimen A sectioned area is a portion of a design which is to be filled with a pattern of lines. Ordinarily, this entity is used to reveal or expose shape or material characteri- stics defined by other entities. It consists of a pointer to an exterior definition curve, a specification of the pattern of lines, the coordinates of a point on a pattern line, the distance between the pattern lines, the angle between the pattern lines and the X-axis of definition space, and the specification of any enclosed definition curves (commonly known as islands).defines IGES Sectioned Area, Type <230> Form <0>, in package IGESDimen A sectioned area is a portion of a design which is to be filled with a pattern of lines. Ordinarily, this entity is used to reveal or expose shape or material characteri- stics defined by other entities. It consists of a pointer to an exterior definition curve, a specification of the pattern of lines, the coordinates of a point on a pattern line, the distance between the pattern lines, the angle between the pattern lines and the X-axis of definition space, and the specification of any enclosed definition curves (commonly known as islands).defines IGES Sectioned Area, Type <230> Form <0>, in package IGESDimen A sectioned area is a portion of a design which is to be filled with a pattern of lines. Ordinarily, this entity is used to reveal or expose shape or material characteri- stics defined by other entities. It consists of a pointer to an exterior definition curve, a specification of the pattern of lines, the coordinates of a point on a pattern line, the distance between the pattern lines, the angle between the pattern lines and the X-axis of definition space, and the specification of any enclosed definition curves (commonly known as islands).
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def Angle(self) -> float: 
        """
        returns the angle of lines with XT axis
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
        returns the normal distance between lines
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExteriorCurve(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the exterior definition curve
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
    def Init(self,aCurve : OCP.IGESData.IGESData_IGESEntity,aPattern : int,aPoint : OCP.gp.gp_XYZ,aDistance : float,anAngle : float,someIslands : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsInverted(self) -> bool: 
        """
        Returns True if cross hatches as Inverted, else they are Standard (Inverted : Form=1, Standard : Form=0)
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IslandCurve(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the interior definition curves, returns Null Handle exception raised if Index <= 0 or Index > NbIslands()
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
    def NbIslands(self) -> int: 
        """
        returns the number of island curves
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
    def PassingPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns point thru which line should pass
        """
    def Pattern(self) -> int: 
        """
        returns fill pattern code
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
    def SetInverted(self,mode : bool) -> None: 
        """
        Sets the cross hatches to be inverted or not, according value of <mode> (corresponds to FormNumber)
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
    def TransformedPassingPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns point thru which line should pass after Transformation
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
    def ZDepth(self) -> float: 
        """
        returns the Z depth
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
class IGESDimen_SpecificModule(OCP.IGESData.IGESData_SpecificModule, OCP.Standard.Standard_Transient):
    """
    Defines Services attached to IGES Entities : Dump & OwnCorrect, for IGESDimenDefines Services attached to IGES Entities : Dump & OwnCorrect, for IGESDimenDefines Services attached to IGES Entities : Dump & OwnCorrect, for IGESDimen
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
        Performs non-ambiguous Corrections on Entities which support them (BasicDimension,CenterLine,DimensionDisplayData, DimensionTolerance,DimensionUnits,DimensionedGeometry, NewDimensionedGeometry,Section,WitnessLine)
        """
    def OwnDump(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Specific Dump (own parameters) for IGESDimen
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
class IGESDimen_ToolAngularDimension():
    """
    Tool to work on a AngularDimension. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_AngularDimension) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_AngularDimension,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_AngularDimension,entto : IGESDimen_AngularDimension,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_AngularDimension,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_AngularDimension,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a AngularDimension <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_AngularDimension,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_AngularDimension,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolBasicDimension():
    """
    Tool to work on a BasicDimension. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_BasicDimension) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_BasicDimension,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_BasicDimension,entto : IGESDimen_BasicDimension,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDimen_BasicDimension) -> bool: 
        """
        Sets automatic unambiguous Correction on a BasicDimension (NbPropertyValues forced to 8)
        """
    def OwnDump(self,ent : IGESDimen_BasicDimension,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_BasicDimension,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a BasicDimension <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_BasicDimension,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_BasicDimension,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolCenterLine():
    """
    Tool to work on a CenterLine. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_CenterLine) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_CenterLine,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_CenterLine,entto : IGESDimen_CenterLine,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDimen_CenterLine) -> bool: 
        """
        Sets automatic unambiguous Correction on a CenterLine (LineFont forced to Rank = 1, DataType forced to 1)
        """
    def OwnDump(self,ent : IGESDimen_CenterLine,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_CenterLine,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a CenterLine <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_CenterLine,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_CenterLine,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolCurveDimension():
    """
    Tool to work on a CurveDimension. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_CurveDimension) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_CurveDimension,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_CurveDimension,entto : IGESDimen_CurveDimension,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_CurveDimension,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_CurveDimension,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a CurveDimension <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_CurveDimension,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_CurveDimension,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolDiameterDimension():
    """
    Tool to work on a DiameterDimension. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_DiameterDimension) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_DiameterDimension,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_DiameterDimension,entto : IGESDimen_DiameterDimension,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_DiameterDimension,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_DiameterDimension,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a DiameterDimension <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_DiameterDimension,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_DiameterDimension,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolDimensionDisplayData():
    """
    Tool to work on a DimensionDisplayData. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_DimensionDisplayData) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_DimensionDisplayData,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_DimensionDisplayData,entto : IGESDimen_DimensionDisplayData,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDimen_DimensionDisplayData) -> bool: 
        """
        Sets automatic unambiguous Correction on a DimensionDisplayData (NbPropertyValues forced to 14)
        """
    def OwnDump(self,ent : IGESDimen_DimensionDisplayData,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_DimensionDisplayData,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a DimensionDisplayData <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_DimensionDisplayData,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_DimensionDisplayData,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolDimensionTolerance():
    """
    Tool to work on a DimensionTolerance. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_DimensionTolerance) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_DimensionTolerance,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_DimensionTolerance,entto : IGESDimen_DimensionTolerance,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDimen_DimensionTolerance) -> bool: 
        """
        Sets automatic unambiguous Correction on a DimensionTolerance (NbPropertyValues forced to 8)
        """
    def OwnDump(self,ent : IGESDimen_DimensionTolerance,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_DimensionTolerance,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a DimensionTolerance <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_DimensionTolerance,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_DimensionTolerance,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolDimensionUnits():
    """
    Tool to work on a DimensionUnits. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_DimensionUnits) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_DimensionUnits,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_DimensionUnits,entto : IGESDimen_DimensionUnits,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDimen_DimensionUnits) -> bool: 
        """
        Sets automatic unambiguous Correction on a DimensionUnits (NbPropertyValues forced to 6)
        """
    def OwnDump(self,ent : IGESDimen_DimensionUnits,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_DimensionUnits,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a DimensionUnits <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_DimensionUnits,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_DimensionUnits,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolDimensionedGeometry():
    """
    Tool to work on a DimensionedGeometry. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_DimensionedGeometry) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_DimensionedGeometry,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_DimensionedGeometry,entto : IGESDimen_DimensionedGeometry,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDimen_DimensionedGeometry) -> bool: 
        """
        Sets automatic unambiguous Correction on a DimensionedGeometry (NbDimensions forced to 1)
        """
    def OwnDump(self,ent : IGESDimen_DimensionedGeometry,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_DimensionedGeometry,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a DimensionedGeometry <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_DimensionedGeometry,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_DimensionedGeometry,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolFlagNote():
    """
    Tool to work on a FlagNote. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_FlagNote) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_FlagNote,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_FlagNote,entto : IGESDimen_FlagNote,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_FlagNote,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_FlagNote,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a FlagNote <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_FlagNote,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_FlagNote,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolGeneralLabel():
    """
    Tool to work on a GeneralLabel. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_GeneralLabel) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_GeneralLabel,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_GeneralLabel,entto : IGESDimen_GeneralLabel,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_GeneralLabel,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_GeneralLabel,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a GeneralLabel <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_GeneralLabel,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_GeneralLabel,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolGeneralNote():
    """
    Tool to work on a GeneralNote. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_GeneralNote) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_GeneralNote,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_GeneralNote,entto : IGESDimen_GeneralNote,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_GeneralNote,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_GeneralNote,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a GeneralNote <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_GeneralNote,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_GeneralNote,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolGeneralSymbol():
    """
    Tool to work on a GeneralSymbol. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_GeneralSymbol) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_GeneralSymbol,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_GeneralSymbol,entto : IGESDimen_GeneralSymbol,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_GeneralSymbol,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_GeneralSymbol,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a GeneralSymbol <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_GeneralSymbol,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_GeneralSymbol,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolLeaderArrow():
    """
    Tool to work on a LeaderArrow. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_LeaderArrow) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_LeaderArrow,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_LeaderArrow,entto : IGESDimen_LeaderArrow,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_LeaderArrow,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_LeaderArrow,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a LeaderArrow <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_LeaderArrow,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_LeaderArrow,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolLinearDimension():
    """
    Tool to work on a LinearDimension. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_LinearDimension) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_LinearDimension,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_LinearDimension,entto : IGESDimen_LinearDimension,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_LinearDimension,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_LinearDimension,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a LinearDimension <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_LinearDimension,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_LinearDimension,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolNewDimensionedGeometry():
    """
    Tool to work on a NewDimensionedGeometry. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_NewDimensionedGeometry) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_NewDimensionedGeometry,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_NewDimensionedGeometry,entto : IGESDimen_NewDimensionedGeometry,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDimen_NewDimensionedGeometry) -> bool: 
        """
        Sets automatic unambiguous Correction on a NewDimensionedGeometry (NbDimensions forced to 1, Transf Nullified in D.E.)
        """
    def OwnDump(self,ent : IGESDimen_NewDimensionedGeometry,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_NewDimensionedGeometry,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a NewDimensionedGeometry <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_NewDimensionedGeometry,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_NewDimensionedGeometry,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolNewGeneralNote():
    """
    Tool to work on a NewGeneralNote. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_NewGeneralNote) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_NewGeneralNote,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_NewGeneralNote,entto : IGESDimen_NewGeneralNote,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_NewGeneralNote,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_NewGeneralNote,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a NewGeneralNote <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_NewGeneralNote,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_NewGeneralNote,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolOrdinateDimension():
    """
    Tool to work on a OrdinateDimension. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_OrdinateDimension) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_OrdinateDimension,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_OrdinateDimension,entto : IGESDimen_OrdinateDimension,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_OrdinateDimension,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_OrdinateDimension,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a OrdinateDimension <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_OrdinateDimension,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_OrdinateDimension,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolPointDimension():
    """
    Tool to work on a PointDimension. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_PointDimension) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_PointDimension,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_PointDimension,entto : IGESDimen_PointDimension,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_PointDimension,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_PointDimension,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a PointDimension <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_PointDimension,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_PointDimension,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolRadiusDimension():
    """
    Tool to work on a RadiusDimension. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_RadiusDimension) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_RadiusDimension,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_RadiusDimension,entto : IGESDimen_RadiusDimension,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_RadiusDimension,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_RadiusDimension,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a RadiusDimension <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_RadiusDimension,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_RadiusDimension,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolSection():
    """
    Tool to work on a Section. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_Section) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_Section,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_Section,entto : IGESDimen_Section,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDimen_Section) -> bool: 
        """
        Sets automatic unambiguous Correction on a Section (LineFont forced to Rank = 1, DataType forced to 1)
        """
    def OwnDump(self,ent : IGESDimen_Section,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_Section,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Section <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_Section,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_Section,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolSectionedArea():
    """
    Tool to work on a SectionedArea. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_SectionedArea) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_SectionedArea,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_SectionedArea,entto : IGESDimen_SectionedArea,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDimen_SectionedArea,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_SectionedArea,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a SectionedArea <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_SectionedArea,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_SectionedArea,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_ToolWitnessLine():
    """
    Tool to work on a WitnessLine. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDimen_WitnessLine) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDimen_WitnessLine,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDimen_WitnessLine,entto : IGESDimen_WitnessLine,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDimen_WitnessLine) -> bool: 
        """
        Sets automatic unambiguous Correction on a WitnessLine (LineFont forced to Rank = 1, DataType forced to 1)
        """
    def OwnDump(self,ent : IGESDimen_WitnessLine,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDimen_WitnessLine,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a WitnessLine <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDimen_WitnessLine,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDimen_WitnessLine,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDimen_WitnessLine(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines WitnessLine, Type <106> Form <40> in package IGESDimen Contains one or more straight line segments associated with drafting entities of various typesdefines WitnessLine, Type <106> Form <40> in package IGESDimen Contains one or more straight line segments associated with drafting entities of various typesdefines WitnessLine, Type <106> Form <40> in package IGESDimen Contains one or more straight line segments associated with drafting entities of various types
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
    def Datatype(self) -> int: 
        """
        returns Interpretation Flag, always = 1
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
    def Init(self,dataType : int,aDisp : float,dataPoints : OCP.TColgp.TColgp_HArray1OfXY) -> None: 
        """
        This method is used to set the fields of the class WitnessLine - dataType : Interpretation Flag, always = 1 - aDispl : Common z displacement - dataPoints : Data points
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
    def NbPoints(self) -> int: 
        """
        returns number of Data Points
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
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns Index'th. data point raises exception if Index <= 0 or Index > NbPoints
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
    def TransformedPoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        returns data point after Transformation. raises exception if Index <= 0 or Index > NbPoints
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
    def ZDisplacement(self) -> float: 
        """
        returns common Z displacement
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
