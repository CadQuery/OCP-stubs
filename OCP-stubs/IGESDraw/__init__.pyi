import OCP.IGESDraw
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IGESDimen
import OCP.TColgp
import OCP.IGESData
import io
import OCP.gp
import OCP.Standard
import OCP.IGESBasic
import OCP.IGESGeom
import OCP.Interface
import OCP.IGESGraph
import OCP.TCollection
import OCP.TColStd
__all__  = [
"IGESDraw",
"IGESDraw_Array1OfConnectPoint",
"IGESDraw_Array1OfViewKindEntity",
"IGESDraw_CircArraySubfigure",
"IGESDraw_ConnectPoint",
"IGESDraw_Drawing",
"IGESDraw_DrawingWithRotation",
"IGESDraw_GeneralModule",
"IGESDraw_HArray1OfConnectPoint",
"IGESDraw_HArray1OfViewKindEntity",
"IGESDraw_LabelDisplay",
"IGESDraw_NetworkSubfigure",
"IGESDraw_NetworkSubfigureDef",
"IGESDraw_PerspectiveView",
"IGESDraw_Planar",
"IGESDraw_Protocol",
"IGESDraw_ReadWriteModule",
"IGESDraw_RectArraySubfigure",
"IGESDraw_SegmentedViewsVisible",
"IGESDraw_SpecificModule",
"IGESDraw_ToolCircArraySubfigure",
"IGESDraw_ToolConnectPoint",
"IGESDraw_ToolDrawing",
"IGESDraw_ToolDrawingWithRotation",
"IGESDraw_ToolLabelDisplay",
"IGESDraw_ToolNetworkSubfigure",
"IGESDraw_ToolNetworkSubfigureDef",
"IGESDraw_ToolPerspectiveView",
"IGESDraw_ToolPlanar",
"IGESDraw_ToolRectArraySubfigure",
"IGESDraw_ToolSegmentedViewsVisible",
"IGESDraw_ToolView",
"IGESDraw_ToolViewsVisible",
"IGESDraw_ToolViewsVisibleWithAttr",
"IGESDraw_View",
"IGESDraw_ViewsVisible",
"IGESDraw_ViewsVisibleWithAttr"
]
class IGESDraw():
    """
    This package contains the group of classes necessary for Structure Entities implied in Drawings and Structured Graphics (Sets for drawing, Drawings and Views).
    """
    @staticmethod
    def Init_s() -> None: 
        """
        Prepares dynamic data (Protocol, Modules) for this package
        """
    @staticmethod
    def Protocol_s() -> IGESDraw_Protocol: 
        """
        Returns the Protocol for this Package
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_Array1OfConnectPoint():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESDraw_Array1OfConnectPoint) -> IGESDraw_Array1OfConnectPoint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESDraw_ConnectPoint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESDraw_ConnectPoint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESDraw_ConnectPoint: 
        """
        Variable value access
        """
    def First(self) -> IGESDraw_ConnectPoint: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESDraw_ConnectPoint) -> None: 
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
    def Last(self) -> IGESDraw_ConnectPoint: 
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
    def Move(self,theOther : IGESDraw_Array1OfConnectPoint) -> IGESDraw_Array1OfConnectPoint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESDraw_ConnectPoint) -> None: 
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
    def Value(self,theIndex : int) -> IGESDraw_ConnectPoint: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : IGESDraw_Array1OfConnectPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : IGESDraw_ConnectPoint,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class IGESDraw_Array1OfViewKindEntity():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESDraw_Array1OfViewKindEntity) -> IGESDraw_Array1OfViewKindEntity: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Variable value access
        """
    def First(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
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
    def Last(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
    def Move(self,theOther : IGESDraw_Array1OfViewKindEntity) -> IGESDraw_Array1OfViewKindEntity: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
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
    def Value(self,theIndex : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : IGESDraw_Array1OfViewKindEntity) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.IGESData.IGESData_ViewKindEntity,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class IGESDraw_CircArraySubfigure(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    Defines IGES Circular Array Subfigure Instance Entity, Type <414> Form Number <0> in package IGESDrawDefines IGES Circular Array Subfigure Instance Entity, Type <414> Form Number <0> in package IGESDrawDefines IGES Circular Array Subfigure Instance Entity, Type <414> Form Number <0> in package IGESDraw
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
    def BaseEntity(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the base entity, copies of which are produced
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def CenterPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the center of the imaginary circle
        """
    def CircleRadius(self) -> float: 
        """
        returns the radius of the imaginary circle
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
    def DeltaAngle(self) -> float: 
        """
        returns the delta angle in radians
        """
    def DirFieldEntity(self,fieldnum : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Entity which has been recorded for a given Field Number, i.e. without any cast. Maps with : 3 : Structure 4 : LineFont 5 : LevelList 6 : View 7 : Transf(ormation Matrix) 8 : LabelDisplay 13 : Color. Other values give a null handle It can then be of any kind, while specific items have a Type
        """
    def DisplayFlag(self) -> bool: 
        """
        returns True if (ListCount = 0) all elements are to be displayed
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DoDontFlag(self) -> bool: 
        """
        returns 0 if half or fewer of the elements of the array are defined 1 if half or more of the elements are defined
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
    def Init(self,aBase : OCP.IGESData.IGESData_IGESEntity,aNumLocs : int,aCenter : OCP.gp.gp_XYZ,aRadius : float,aStAngle : float,aDelAngle : float,aFlag : int,allNumPos : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        This method is used to set the fields of the class CircArraySubfigure - aBase : Base entity - aNumLocs : Total number of possible instance locations - aCenter : Coordinates of Center of imaginary circle - aRadius : Radius of imaginary circle - aStAngle : Start angle in radians - aDelAngle : Delta angle in radians - aFlag : DO-DON'T flag to control which portion to display - allNumPos : All position to be or not to be processed
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def ListCount(self) -> int: 
        """
        returns 0 if all elements to be displayed
        """
    def ListPosition(self,Index : int) -> int: 
        """
        returns the Index'th value position raises exception if Index <= 0 or Index > ListCount().
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
    def NbLocations(self) -> int: 
        """
        returns total number of possible instance locations
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
    def PositionNum(self,Index : int) -> bool: 
        """
        returns whether Index is to be processed (DO) or not to be processed(DON'T) if (ListCount = 0) return theDoDontFlag raises exception if Index <= 0 or Index > ListCount().
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
    def StartAngle(self) -> float: 
        """
        returns the start angle in radians
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
    def TransformedCenterPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the Transformed center of the imaginary circle
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
class IGESDraw_ConnectPoint(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESConnectPoint, Type <132> Form Number <0> in package IGESDrawdefines IGESConnectPoint, Type <132> Form Number <0> in package IGESDrawdefines IGESConnectPoint, Type <132> Form Number <0> in package IGESDraw
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
    def DisplaySymbol(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        if display symbol specified returns display symbol geometric entity else returns NULL Handle
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
    def FunctionCode(self) -> int: 
        """
        returns the Connect Point Function Code
        """
    def FunctionFlag(self) -> int: 
        """
        returns Function Code that specifies a particular function for the ECO576 connection : e.g., Function Flag = 0 : Unspecified(default) = 1 : Electrical Signal = 2 : Fluid flow Signal
        """
    def FunctionIdentifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        return HAsciiString identifying Pin Number or Nozzle Label etc.
        """
    def FunctionName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Connection Point Function Name
        """
    def FunctionTemplate(self) -> OCP.IGESGraph.IGESGraph_TextDisplayTemplate: 
        """
        if Text Display Template for the Function Name is defined, returns TestDisplayTemplate else returns NULL Handle
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDisplaySymbol(self) -> bool: 
        """
        returns True if Display symbol is specified else returns False
        """
    def HasFunctionTemplate(self) -> bool: 
        """
        returns True if Text Display Template is specified for Function Name else returns False
        """
    def HasIdentifierTemplate(self) -> bool: 
        """
        returns True if Text Display Template is specified for Identifier else returns False
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
    def HasOwnerSubfigure(self) -> bool: 
        """
        returns True if Network Subfigure Instance/Definition Entity is specified else returns False
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
    def IdentifierTemplate(self) -> OCP.IGESGraph.IGESGraph_TextDisplayTemplate: 
        """
        if Text Display Template for the Function Identifier is defined, returns TestDisplayTemplate else returns NULL Handle
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aPoint : OCP.gp.gp_XYZ,aDisplaySymbol : OCP.IGESData.IGESData_IGESEntity,aTypeFlag : int,aFunctionFlag : int,aFunctionIdentifier : OCP.TCollection.TCollection_HAsciiString,anIdentifierTemplate : OCP.IGESGraph.IGESGraph_TextDisplayTemplate,aFunctionName : OCP.TCollection.TCollection_HAsciiString,aFunctionTemplate : OCP.IGESGraph.IGESGraph_TextDisplayTemplate,aPointIdentifier : int,aFunctionCode : int,aSwapFlag : int,anOwnerSubfigure : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        This method is used to set the fields of the class ConnectPoint - aPoint : A Coordinate point - aDisplaySymbol : Display symbol Geometry - aTypeFlag : Type of the connection - aFunctionFlag : Function flag for the connection - aFunctionIdentifier : Connection Point Function Identifier - anIdentifierTemplate : Connection Point Function Template - aFunctionName : Connection Point Function Name - aFunctionTemplate : Connection Point Function Template - aPointIdentifier : Unique Connect Point Identifier - aFunctionCode : Connect Point Function Code - aSwapFlag : Connect Point Swap Flag - anOwnerSubfigure : Pointer to the "Owner" Entity
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def OwnerSubfigure(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns "owner" Network Subfigure Instance Entity, or Network Subfigure Definition Entity, or NULL Handle.
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        returns the coordinate of the connection point
        """
    def PointIdentifier(self) -> int: 
        """
        returns the Unique Connect Point Identifier
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
    def SwapFlag(self) -> bool: 
        """
        return value = 0 : Connect point may be swapped(default) = 1 : Connect point may not be swapped
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TransformedPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the Transformed coordinate of the connection point
        """
    def TypeFlag(self) -> int: 
        """
        return value specifies a particular type of connection : Type Flag = 0 : Not Specified(default) 1 : Nonspecific logical point of connection 2 : Nonspecific physical point of connection 101 : Logical component pin 102 : Logical part connector 103 : Logical offpage connector 104 : Logical global signal connector 201 : Physical PWA surface mount pin 202 : Physical PWA blind pin 203 : Physical PWA thru-pin 5001-9999 : Implementor defined.
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
class IGESDraw_Drawing(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESDrawing, Type <404> Form <0> in package IGESDrawdefines IGESDrawing, Type <404> Form <0> in package IGESDrawdefines IGESDrawing, Type <404> Form <0> in package IGESDraw
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def Annotation(self,AnnotationIndex : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Annotation entity in this Drawing, indicated by the AnnotationIndex raises an exception if AnnotationIndex <= 0 or AnnotationIndex > NbAnnotations().
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
    def DrawingSize(self,X : float,Y : float) -> bool: 
        """
        Returns the Drawing Size if it is specified (by a specific property entity) If not specified, returns False, and X,Y as zero : unit to consider is then the model unit in GlobalSection
        """
    def DrawingUnit(self,value : float) -> bool: 
        """
        Returns the Drawing Unit Value if it is specified (by a specific property entity) If not specified, returns False, and val as zero : unit to consider is then the model unit in GlobalSection
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
    def Init(self,allViews : IGESDraw_HArray1OfViewKindEntity,allViewOrigins : OCP.TColgp.TColgp_HArray1OfXY,allAnnotations : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
        """
        This method is used to set the fields of the class Drawing - allViews : Pointers to DEs of View entities - allViewOrigins : Origin coordinates of transformed Views - allAnnotations : Pointers to DEs of Annotation entities raises exception if Lengths of allViews and allViewOrigins are not same.
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def NbAnnotations(self) -> int: 
        """
        returns the number of Annotation entities in <me>
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
        returns the number of view pointers in <me>
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
    def ViewItem(self,ViewIndex : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        returns the ViewKindEntity indicated by ViewIndex raises an exception if ViewIndex <= 0 or ViewIndex > NbViews().
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
        """
    def ViewOrigin(self,TViewIndex : int) -> OCP.gp.gp_Pnt2d: 
        """
        returns the Drawing space coordinates of the origin of the Transformed view indicated by TViewIndex raises an exception if TViewIndex <= 0 or TViewIndex > NbViews().
        """
    def ViewToDrawing(self,NumView : int,ViewCoords : OCP.gp.gp_XYZ) -> OCP.gp.gp_XY: 
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
    pass
class IGESDraw_DrawingWithRotation(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESDrawingWithRotation, Type <404> Form <1> in package IGESDrawdefines IGESDrawingWithRotation, Type <404> Form <1> in package IGESDrawdefines IGESDrawingWithRotation, Type <404> Form <1> in package IGESDraw
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def Annotation(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Annotation entity in this Drawing, indicated by Index raises an exception if Index <= 0 or Index > NbAnnotations().
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
    def DrawingSize(self,X : float,Y : float) -> bool: 
        """
        Returns the Drawing Size if it is specified (by a specific property entity) If not specified, returns False, and X,Y as zero : unit to consider is then the model unit in GlobalSection
        """
    def DrawingUnit(self,value : float) -> bool: 
        """
        Returns the Drawing Unit Value if it is specified (by a specific property entity) If not specified, returns False, and val as zero : unit to consider is then the model unit in GlobalSection
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
    def Init(self,allViews : IGESDraw_HArray1OfViewKindEntity,allViewOrigins : OCP.TColgp.TColgp_HArray1OfXY,allOrientationAngles : OCP.TColStd.TColStd_HArray1OfReal,allAnnotations : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
        """
        This method is used to set the fields of the class DrawingWithRotation - allViews : Pointers to View entities - allViewOrigins : Origin coords of transformed views - allOrientationAngles : Orientation angles of transformed views - allAnnotations : Pointers to Annotation entities raises exception if Lengths of allViews, allViewOrigins and allOrientationAngles are not same.
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def NbAnnotations(self) -> int: 
        """
        returns the number of Annotation entities in <me>
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
        returns the number of view pointers in <me>
        """
    def OrientationAngle(self,Index : int) -> float: 
        """
        returns the Orientation angle for the Transformed view indicated by Index raises an exception if Index <= 0 or Index > NbViews().
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
    def ViewItem(self,Index : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        returns the View entity indicated by Index raises an exception if Index <= 0 or Index > NbViews().
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
        """
    def ViewOrigin(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        returns the Drawing space coordinates of the origin of the Transformed view indicated by Index raises an exception if Index <= 0 or Index > NbViews().
        """
    def ViewToDrawing(self,NumView : int,ViewCoords : OCP.gp.gp_XYZ) -> OCP.gp.gp_XY: 
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
    pass
class IGESDraw_GeneralModule(OCP.IGESData.IGESData_GeneralModule, OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    Definition of General Services for IGESDraw (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESDraw (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESDraw (specific part) This Services comprise : Shared & Implied Lists, Copy, Check
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" For IGES, answer is always True
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> int: 
        """
        Returns a category number which characterizes an entity Planar : Auxiliary Subfigures and ConnectPoint : Structure others : Drawing
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
        Clears parameters with can cause looping structures : redefined for ViewsVisible ... (clears the implied ref.s)
        """
    def OwnImpliedCase(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Specific list of Entities implied by an IGESEntity <ent> (in addition to Associativities). Redefined for ViewsVisible ...
        """
    def OwnRenewCase(self,CN : int,entfrom : OCP.IGESData.IGESData_IGESEntity,entto : OCP.IGESData.IGESData_IGESEntity,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Renews parameters which are specific of each Type of Entity : redefined for ViewsVisible ... (takes only the implied ref.s which have also been copied)
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
class IGESDraw_HArray1OfConnectPoint(IGESDraw_Array1OfConnectPoint, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESDraw_Array1OfConnectPoint: 
        """
        None
        """
    def Assign(self,theOther : IGESDraw_Array1OfConnectPoint) -> IGESDraw_Array1OfConnectPoint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESDraw_Array1OfConnectPoint: 
        """
        None
        """
    def ChangeFirst(self) -> IGESDraw_ConnectPoint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESDraw_ConnectPoint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESDraw_ConnectPoint: 
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
    def First(self) -> IGESDraw_ConnectPoint: 
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
    def Init(self,theValue : IGESDraw_ConnectPoint) -> None: 
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Last(self) -> IGESDraw_ConnectPoint: 
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
    def Move(self,theOther : IGESDraw_Array1OfConnectPoint) -> IGESDraw_Array1OfConnectPoint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESDraw_ConnectPoint) -> None: 
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
    def Value(self,theIndex : int) -> IGESDraw_ConnectPoint: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESDraw_ConnectPoint) -> None: ...
    @overload
    def __init__(self,theOther : IGESDraw_Array1OfConnectPoint) -> None: ...
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
class IGESDraw_HArray1OfViewKindEntity(IGESDraw_Array1OfViewKindEntity, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESDraw_Array1OfViewKindEntity: 
        """
        None
        """
    def Assign(self,theOther : IGESDraw_Array1OfViewKindEntity) -> IGESDraw_Array1OfViewKindEntity: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESDraw_Array1OfViewKindEntity: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
    def First(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
    def Init(self,theValue : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Last(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
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
    def Move(self,theOther : IGESDraw_Array1OfViewKindEntity) -> IGESDraw_Array1OfViewKindEntity: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.IGESData.IGESData_ViewKindEntity) -> None: 
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
    def Value(self,theIndex : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.IGESData.IGESData_ViewKindEntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IGESDraw_Array1OfViewKindEntity) -> None: ...
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
class IGESDraw_LabelDisplay(OCP.IGESData.IGESData_LabelDisplayEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESLabelDisplay, Type <402> Form <5> in package IGESDrawdefines IGESLabelDisplay, Type <402> Form <5> in package IGESDrawdefines IGESLabelDisplay, Type <402> Form <5> in package IGESDraw
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
    def DisplayedEntity(self,EntityIndex : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the entity indicated by EntityIndex raises an exception if EntityIndex <= 0 or EntityIndex > NbLabels().
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
    def Init(self,allViews : IGESDraw_HArray1OfViewKindEntity,allTextLocations : OCP.TColgp.TColgp_HArray1OfXYZ,allLeaderEntities : OCP.IGESDimen.IGESDimen_HArray1OfLeaderArrow,allLabelLevels : OCP.TColStd.TColStd_HArray1OfInteger,allDisplayedEntities : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
        """
        This method is used to set the fields of the class LabelDisplay - allViews : Pointers to View Entities - allTextLocations : Coordinates of text locations in the views - allLeaderEntities : Pointers to Leader Entities in the views - allLabelLevels : Entity label level numbers in the views - allDisplayedEntities : Pointers to the entities being displayed raises exception if Lengths of allViews, allTextLocations, allLeaderEntities, allLabelLevels and allDisplayedEntities are not same.
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def LabelLevel(self,ViewIndex : int) -> int: 
        """
        returns the Entity label level number in the view indicated by ViewIndex raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
        """
    def LeaderEntity(self,ViewIndex : int) -> OCP.IGESDimen.IGESDimen_LeaderArrow: 
        """
        returns the Leader entity in the view indicated by ViewIndex raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
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
    def NbLabels(self) -> int: 
        """
        returns the number of label placements in <me>
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
    def TextLocation(self,ViewIndex : int) -> OCP.gp.gp_Pnt: 
        """
        returns the 3d-Point coordinates of the text location, in the view indicated by ViewIndex raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TransformedTextLocation(self,ViewIndex : int) -> OCP.gp.gp_Pnt: 
        """
        returns the transformed 3d-Point coordinates of the text location, in the view indicated by ViewIndex raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
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
    def ViewItem(self,ViewIndex : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        returns the View entity indicated by ViewIndex raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
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
class IGESDraw_NetworkSubfigure(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES Network Subfigure Instance Entity, Type <420> Form Number <0> in package IGESDrawdefines IGES Network Subfigure Instance Entity, Type <420> Form Number <0> in package IGESDrawdefines IGES Network Subfigure Instance Entity, Type <420> Form Number <0> in package IGESDraw
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
    def ConnectPoint(self,Index : int) -> IGESDraw_ConnectPoint: 
        """
        returns the Index'th associated Connect point Entity raises exception if Index <= 0 or Index > NbConnectPoints()
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
    def DesignatorTemplate(self) -> OCP.IGESGraph.IGESGraph_TextDisplayTemplate: 
        """
        returns primary reference designator Text Display Template Entity, or null. If null, no Text Display Template Entity specified
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
    def HasDesignatorTemplate(self) -> bool: 
        """
        returns True if Text Display Template Entity is specified, else False
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
    def Init(self,aDefinition : IGESDraw_NetworkSubfigureDef,aTranslation : OCP.gp.gp_XYZ,aScaleFactor : OCP.gp.gp_XYZ,aTypeFlag : int,aDesignator : OCP.TCollection.TCollection_HAsciiString,aTemplate : OCP.IGESGraph.IGESGraph_TextDisplayTemplate,allConnectPoints : IGESDraw_HArray1OfConnectPoint) -> None: 
        """
        This method is used to set the fields of the class NetworkSubfigure - aDefinition : Network Subfigure Definition Entity - aTranslation : Translation data relative to the model space or the definition space - aScaleFactor : Scale factors in the definition space - aTypeFlag : Type flag - aDesignator : Primary reference designator - aTemplate : Primary reference designator Text display Template Entity - allConnectPoints : Associated Connect Point Entities
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def NbConnectPoints(self) -> int: 
        """
        returns the number of associated Connect Point Entities
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
    def ReferenceDesignator(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns the primary reference designator
        """
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def ScaleFactors(self) -> OCP.gp.gp_XYZ: 
        """
        returns Scale factor in definition space(x, y, z axes)
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
    def SubfigureDefinition(self) -> IGESDraw_NetworkSubfigureDef: 
        """
        returns Network Subfigure Definition Entity specified by this entity
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
    def TransformedTranslation(self) -> OCP.gp.gp_XYZ: 
        """
        returns the Transformed Translation Data relative to either model space or to the definition space of a referring entity
        """
    def Translation(self) -> OCP.gp.gp_XYZ: 
        """
        returns Translation Data relative to either model space or to the definition space of a referring entity
        """
    def TypeFlag(self) -> int: 
        """
        returns Type Flag which implements the distinction between Logical design and Physical design data,and is required if both are present. Type Flag = 0 : Not specified (default) = 1 : Logical = 2 : Physical
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
class IGESDraw_NetworkSubfigureDef(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESNetworkSubfigureDef, Type <320> Form Number <0> in package IGESDrawdefines IGESNetworkSubfigureDef, Type <320> Form Number <0> in package IGESDrawdefines IGESNetworkSubfigureDef, Type <320> Form Number <0> in package IGESDraw
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
    def Depth(self) -> int: 
        """
        returns Depth of Subfigure(indication the amount of nesting) Note : The Depth is inclusive of both Network Subfigure Definition Entity and the Ordinary Subfigure Definition Entity. Thus, the two may be nested.
        """
    def Designator(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Primary Reference Designator
        """
    def DesignatorTemplate(self) -> OCP.IGESGraph.IGESGraph_TextDisplayTemplate: 
        """
        if Text Display Template specified then return TextDisplayTemplate else return NULL Handle
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
    def Entity(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Index'th IGESEntity in subfigure exclusive of primary reference designator and Control Points raises exception if Index <=0 or Index > NbEntities()
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDesignatorTemplate(self) -> bool: 
        """
        returns True if Text Display Template is specified for primary designator else returns False
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
    def HasPointEntity(self,Index : int) -> bool: 
        """
        returns True is Index'th Associated Connect Point Entity is present else returns False raises exception if Index is out of bound
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
    def Init(self,aDepth : int,aName : OCP.TCollection.TCollection_HAsciiString,allEntities : OCP.IGESData.IGESData_HArray1OfIGESEntity,aTypeFlag : int,aDesignator : OCP.TCollection.TCollection_HAsciiString,aTemplate : OCP.IGESGraph.IGESGraph_TextDisplayTemplate,allPointEntities : IGESDraw_HArray1OfConnectPoint) -> None: 
        """
        This method is used to set fields of the class NetworkSubfigureDef - aDepth : Depth of Subfigure (indicating the amount of nesting) - aName : Subfigure Name - allEntities : Associated subfigures Entities exclusive of primary reference designator and Control Points. - aTypeFlag : Type flag determines which Entity belongs in which design (Logical design or Physical design) - aDesignator : Designator HAsciiString and its Template - allPointEntities : Associated Connect Point Entities
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
        returns the Subfigure Name
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbEntities(self) -> int: 
        """
        returns Number of Associated(child) entries in subfigure exclusive of primary reference designator and Control Points
        """
    def NbPointEntities(self) -> int: 
        """
        returns the Number Of Associated(child) Connect Point Entities
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
    def PointEntity(self,Index : int) -> IGESDraw_ConnectPoint: 
        """
        returns the Index'th Associated Connect Point Entity raises exception if Index <= 0 or Index > NbPointEntities()
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
    def TypeFlag(self) -> int: 
        """
        return value = 0 : Not Specified = 1 : Logical design = 2 : Physical design
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
class IGESDraw_PerspectiveView(OCP.IGESData.IGESData_ViewKindEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESPerspectiveView, Type <410> Form <1> in package IGESDrawdefines IGESPerspectiveView, Type <410> Form <1> in package IGESDrawdefines IGESPerspectiveView, Type <410> Form <1> in package IGESDraw
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
    def BackPlaneDistance(self) -> float: 
        """
        returns the View coordinate denoting the location of the back clipping plane
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def BottomRight(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the bottom right point of the clipping window
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def CenterOfProjection(self) -> OCP.gp.gp_Pnt: 
        """
        returns the Center Of Projection (model space)
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
    def DepthClip(self) -> int: 
        """
        returns the Depth clipping indicator 0 = No depth clipping 1 = Back clipping plane ON 2 = Front clipping plane ON 3 = Back and front clipping planes ON
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
    def FrontPlaneDistance(self) -> float: 
        """
        returns the View coordinate denoting the location of the front clipping plane
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
    def Init(self,aViewNumber : int,aScaleFactor : float,aViewNormalVector : OCP.gp.gp_XYZ,aViewReferencePoint : OCP.gp.gp_XYZ,aCenterOfProjection : OCP.gp.gp_XYZ,aViewUpVector : OCP.gp.gp_XYZ,aViewPlaneDistance : float,aTopLeft : OCP.gp.gp_XY,aBottomRight : OCP.gp.gp_XY,aDepthClip : int,aBackPlaneDistance : float,aFrontPlaneDistance : float) -> None: 
        """
        This method is used to set the fields of the class PerspectiveView - aViewNumber : The desired view - aScaleFactor : Scale factor - aViewNormalVector : View plane normal vector (model space) - aViewReferencePoint : View reference point (model space) - aCenterOfProjection : Center Of Projection (model space) - aViewUpVector : View up vector (model space) - aViewPlaneDistance : View plane distance (model space) - aTopLeft : Top-left point of clipping window - aBottomRight : Bottom-right point of clipping window - aDepthClip : Depth clipping indicator - aBackPlaneDistance : Distance of back clipping plane - aFrontPlaneDistance : Distance of front clipping plane
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsSingle(self) -> bool: 
        """
        Returns True (for a single view)
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
    def ModelToView(self,coords : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        returns XYX from the Model space to the View space by applying the View Matrix
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
        Returns 1 (single view)
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
    def ScaleFactor(self) -> float: 
        """
        returns the scale factor associated with <me>
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
    def TopLeft(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the top left point of the clipping window
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
    def ViewItem(self,num : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        For a single view, returns <me> whatever <num>
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
        """
    def ViewMatrix(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        returns the Transformation Matrix
        """
    def ViewNormalVector(self) -> OCP.gp.gp_Vec: 
        """
        returns the View plane normal vector (model space)
        """
    def ViewNumber(self) -> int: 
        """
        returns the view number associated with <me>
        """
    def ViewPlaneDistance(self) -> float: 
        """
        returns the View plane distance (model space)
        """
    def ViewReferencePoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the View reference point (model space)
        """
    def ViewUpVector(self) -> OCP.gp.gp_Vec: 
        """
        returns the View up vector (model space)
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
class IGESDraw_Planar(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESPlanar, Type <402> Form <16> in package IGESDrawdefines IGESPlanar, Type <402> Form <16> in package IGESDrawdefines IGESPlanar, Type <402> Form <16> in package IGESDraw
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
    def Entity(self,EntityIndex : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Entity on the specified plane, indicated by EntityIndex raises an exception if EntityIndex <= 0 or EntityIndex > NbEntities()
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
    def Init(self,nbMats : int,aTransformationMatrix : OCP.IGESGeom.IGESGeom_TransformationMatrix,allEntities : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
        """
        This method is used to set the fields of the class Planar - nbMats : Number of Transformation matrices - aTransformationMatrix : Pointer to the Transformation matrix - allEntities : Pointers to the entities specified
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
    def IsIdentityMatrix(self) -> bool: 
        """
        returns True if TransformationMatrix is Identity Matrix, i.e:- No Matrix defined.
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def NbEntities(self) -> int: 
        """
        returns the number of Entities in the plane pointed to by this associativity
        """
    def NbMatrices(self) -> int: 
        """
        returns the number of Transformation matrices in <me>
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
    def TransformMatrix(self) -> OCP.IGESGeom.IGESGeom_TransformationMatrix: 
        """
        returns the Transformation matrix moving data from the XY plane into space or zero
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
class IGESDraw_Protocol(OCP.IGESData.IGESData_Protocol, OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    Description of Protocol for IGESDrawDescription of Protocol for IGESDrawDescription of Protocol for IGESDraw
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
        Gives the count of Resource Protocol. Here, one (Protocol from IGESDimen)
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
class IGESDraw_ReadWriteModule(OCP.IGESData.IGESData_ReadWriteModule, OCP.Interface.Interface_ReaderModule, OCP.Standard.Standard_Transient):
    """
    Defines Draw File Access Module for IGESDraw (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.Defines Draw File Access Module for IGESDraw (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.Defines Draw File Access Module for IGESDraw (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.
    """
    def CaseIGES(self,typenum : int,formnum : int) -> int: 
        """
        Defines Case Numbers for Entities of IGESDraw
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
        Reads own parameters from file for an Entity of IGESDraw
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
class IGESDraw_RectArraySubfigure(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    Defines IGES Rectangular Array Subfigure Instance Entity, Type <412> Form Number <0> in package IGESDraw Used to produce copies of object called the base entity, arranging them in equally spaced rows and columnsDefines IGES Rectangular Array Subfigure Instance Entity, Type <412> Form Number <0> in package IGESDraw Used to produce copies of object called the base entity, arranging them in equally spaced rows and columnsDefines IGES Rectangular Array Subfigure Instance Entity, Type <412> Form Number <0> in package IGESDraw Used to produce copies of object called the base entity, arranging them in equally spaced rows and columns
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
    def BaseEntity(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the base entity, copies of which are produced
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
    def ColumnSeparation(self) -> float: 
        """
        returns horizontal distance between columns
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
    def DisplayFlag(self) -> bool: 
        """
        returns True if (ListCount = 0) i.e., all elements to be displayed
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DoDontFlag(self) -> bool: 
        """
        returns 0 if half or fewer of the elements of the array are defined 1 if half or more of the elements are defined
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
    def Init(self,aBase : OCP.IGESData.IGESData_IGESEntity,aScale : float,aCorner : OCP.gp.gp_XYZ,nbCols : int,nbRows : int,hDisp : float,vtDisp : float,rotationAngle : float,doDont : int,allNumPos : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        This method is used to set the fields of the class RectArraySubfigure - aBase : a base entity which is replicated - aScale : Scale Factor - aCorner : lower left hand corner for the entire array - nbCols : Number of columns of the array - nbRows : Number of rows of the array - hDisp : Column separations - vtDisp : Row separation - rotationAngle : Rotation angle specified in radians - allDont : DO-DON'T flag to control which portion to display - allNumPos : List of positions to be or not to be displayed
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def ListCount(self) -> int: 
        """
        returns 0 if all replicated entities to be displayed
        """
    def ListPosition(self,Index : int) -> int: 
        """
        returns the Index'th value position raises exception if Index <= 0 or Index > ListCount()
        """
    def Location(self) -> OCP.gp.gp_GTrsf: 
        """
        Returns Location given by Transf in Directory Part (see above) It must be considered for local definition : if the Entity is set in a "Parent", that one can add its one Location, but this is not taken in account here : see CompoundLocation for that. If no Transf is defined, returns Identity If Transf is itself compound, gives the final result
        """
    def LowerLeftCorner(self) -> OCP.gp.gp_Pnt: 
        """
        returns coordinates of lower left hand corner for the entire array
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbColumns(self) -> int: 
        """
        returns number of columns in the array
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbRows(self) -> int: 
        """
        returns number of rows in the array
        """
    def NbTypedAssociativities(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Associativities have a given type
        """
    def NbTypedProperties(self,atype : OCP.Standard.Standard_Type) -> int: 
        """
        gives how many Properties have a given type
        """
    def PositionNum(self,Index : int) -> bool: 
        """
        returns whether Index is to be processed (DO) or not to be processed(DON'T) if (ListCount = 0) return theDoDontFlag
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
    def RotationAngle(self) -> float: 
        """
        returns rotation angle in radians
        """
    def RowSeparation(self) -> float: 
        """
        returns vertical distance between rows
        """
    def ScaleFactor(self) -> float: 
        """
        returns the scale factor
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
    def TransformedLowerLeftCorner(self) -> OCP.gp.gp_Pnt: 
        """
        returns Transformed coordinates of lower left corner for the array
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
class IGESDraw_SegmentedViewsVisible(OCP.IGESData.IGESData_ViewKindEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESSegmentedViewsVisible, Type <402> Form <19> in package IGESDrawdefines IGESSegmentedViewsVisible, Type <402> Form <19> in package IGESDrawdefines IGESSegmentedViewsVisible, Type <402> Form <19> in package IGESDraw
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
    def BreakpointParameter(self,BreakpointIndex : int) -> float: 
        """
        returns the parameter of the breakpoint indicated by BreakpointIndex raises an exception if BreakpointIndex <= 0 or BreakpointIndex > NbSegmentBlocks().
        """
    def CResValues(self,res1 : str,res2 : str) -> bool: 
        """
        returns "reserved" alphanumeric values res1 and res2 res1 and res2 have to be reserved as Character[9 at least] (remark : their content is changed) returned values are ended by null character in 9th returned Boolean is False if res1 and res2 are blank, true else
        """
    def Color(self) -> OCP.IGESData.IGESData_ColorEntity: 
        """
        Returns the IGES entity which describes the color of the entity. Returns a null handle if this entity was defined as an integer.
        """
    def ColorDefinition(self,ColorIndex : int) -> OCP.IGESGraph.IGESGraph_Color: 
        """
        returns the Color definition entity indicated by ColorIndex raises an exception if ColorIndex <= 0 or ColorIndex > NbSegmentBlocks().
        """
    def ColorValue(self,ColorIndex : int) -> int: 
        """
        returns the Color value indicated by ColorIndex raises an exception if ColorIndex <= 0 or ColorIndex > NbSegmentBlocks().
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
    def DisplayFlag(self,FlagIndex : int) -> int: 
        """
        returns the Display flag indicated by FlagIndex raises an exception if FlagIndex <= 0 or FlagIndex > NbSegmentBlocks().
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
    def Init(self,allViews : IGESDraw_HArray1OfViewKindEntity,allBreakpointParameters : OCP.TColStd.TColStd_HArray1OfReal,allDisplayFlags : OCP.TColStd.TColStd_HArray1OfInteger,allColorValues : OCP.TColStd.TColStd_HArray1OfInteger,allColorDefinitions : OCP.IGESGraph.IGESGraph_HArray1OfColor,allLineFontValues : OCP.TColStd.TColStd_HArray1OfInteger,allLineFontDefinitions : OCP.IGESBasic.IGESBasic_HArray1OfLineFontEntity,allLineWeights : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        This method is used to set the fields of the class SegmentedViewsVisible - allViews : Pointers to View Entities - allBreakpointParameters : Parameters of breakpoints - allDisplayFlags : Display flags - allColorValues : Color Values - allColorDefinitions : Color Definitions - allLineFontValues : LineFont values - allLineFontDefinitions : LineFont Definitions - allLineWeights : Line weights raises exception if Lengths of allViews, allBreakpointParameters, allDisplayFlags, allColorValues, allColorDefinitions, allLineFontValues, allLineFontDefinitions and allLineWeights are not same.
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
    def IsColorDefinition(self,ColorIndex : int) -> bool: 
        """
        returns True if the ColorIndex'th value of the "theColorDefinitions" field of <me> is a pointer raises an exception if ColorIndex <= 0 or ColorIndex > NbSegmentBlocks().
        """
    def IsFontDefinition(self,FontIndex : int) -> bool: 
        """
        returns True if the FontIndex'th value of the "theLineFontDefinitions" field of <me> is a pointer raises an exception if FontIndex <= 0 or FontIndex > NbSegmentBlocks().
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsSingle(self) -> bool: 
        """
        Returns False (for a complex view)
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
    def LineFontDefinition(self,FontIndex : int) -> OCP.IGESData.IGESData_LineFontEntity: 
        """
        returns the LineFont definition entity indicated by FontIndex raises an exception if FontIndex <= 0 or FontIndex > NbSegmentBlocks().
        """
    def LineFontValue(self,FontIndex : int) -> int: 
        """
        returns the LineFont value indicated by FontIndex raises an exception if FontIndex <= 0 or FontIndex > NbSegmentBlocks().
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightItem(self,WeightIndex : int) -> int: 
        """
        returns the LineWeight value indicated by WeightIndex raises an exception if WeightIndex <= 0 or WeightIndex > NbSegmentBlocks().
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
    def NbSegmentBlocks(self) -> int: 
        """
        returns the number of view/segment blocks in <me> Similar to NbViews but has a more general significance
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
        Returns the count of Views referenced by <me> (inherited)
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
    def ViewItem(self,ViewIndex : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        returns the View entity indicated by ViewIndex raises an exception if ViewIndex <= 0 or ViewIndex > NbSegmentBlocks()
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
class IGESDraw_SpecificModule(OCP.IGESData.IGESData_SpecificModule, OCP.Standard.Standard_Transient):
    """
    Defines Services attached to IGES Entities : Dump & OwnCorrect, for IGESDrawDefines Services attached to IGES Entities : Dump & OwnCorrect, for IGESDrawDefines Services attached to IGES Entities : Dump & OwnCorrect, for IGESDraw
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def OwnCorrect(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Performs non-ambiguous Corrections on Entities which support them (Planar)
        """
    def OwnDump(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Specific Dump (own parameters) for IGESDraw
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
class IGESDraw_ToolCircArraySubfigure():
    """
    Tool to work on a CircArraySubfigure. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_CircArraySubfigure) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_CircArraySubfigure,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_CircArraySubfigure,entto : IGESDraw_CircArraySubfigure,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDraw_CircArraySubfigure,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_CircArraySubfigure,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a CircArraySubfigure <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_CircArraySubfigure,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_CircArraySubfigure,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolConnectPoint():
    """
    Tool to work on a ConnectPoint. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_ConnectPoint) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_ConnectPoint,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_ConnectPoint,entto : IGESDraw_ConnectPoint,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDraw_ConnectPoint,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_ConnectPoint,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a ConnectPoint <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_ConnectPoint,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_ConnectPoint,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolDrawing():
    """
    Tool to work on a Drawing. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_Drawing) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_Drawing,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_Drawing,entto : IGESDraw_Drawing,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDraw_Drawing) -> bool: 
        """
        Sets automatic unambiguous Correction on a Drawing (Null Views are removed from list)
        """
    def OwnDump(self,ent : IGESDraw_Drawing,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_Drawing,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Drawing <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_Drawing,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_Drawing,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolDrawingWithRotation():
    """
    Tool to work on a DrawingWithRotation. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_DrawingWithRotation) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_DrawingWithRotation,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_DrawingWithRotation,entto : IGESDraw_DrawingWithRotation,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDraw_DrawingWithRotation) -> bool: 
        """
        Sets automatic unambiguous Correction on a DrawingWithRotation (Null Views are removed from list)
        """
    def OwnDump(self,ent : IGESDraw_DrawingWithRotation,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_DrawingWithRotation,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a DrawingWithRotation <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_DrawingWithRotation,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_DrawingWithRotation,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolLabelDisplay():
    """
    Tool to work on a LabelDisplay. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_LabelDisplay) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_LabelDisplay,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_LabelDisplay,entto : IGESDraw_LabelDisplay,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDraw_LabelDisplay,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_LabelDisplay,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a LabelDisplay <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_LabelDisplay,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_LabelDisplay,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolNetworkSubfigure():
    """
    Tool to work on a NetworkSubfigure. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_NetworkSubfigure) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_NetworkSubfigure,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_NetworkSubfigure,entto : IGESDraw_NetworkSubfigure,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDraw_NetworkSubfigure,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_NetworkSubfigure,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a NetworkSubfigure <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_NetworkSubfigure,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_NetworkSubfigure,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolNetworkSubfigureDef():
    """
    Tool to work on a NetworkSubfigureDef. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_NetworkSubfigureDef) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_NetworkSubfigureDef,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_NetworkSubfigureDef,entto : IGESDraw_NetworkSubfigureDef,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDraw_NetworkSubfigureDef,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_NetworkSubfigureDef,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a NetworkSubfigureDef <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_NetworkSubfigureDef,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_NetworkSubfigureDef,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolPerspectiveView():
    """
    Tool to work on a PerspectiveView. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_PerspectiveView) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_PerspectiveView,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_PerspectiveView,entto : IGESDraw_PerspectiveView,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDraw_PerspectiveView,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_PerspectiveView,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a PerspectiveView <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_PerspectiveView,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_PerspectiveView,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolPlanar():
    """
    Tool to work on a Planar. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_Planar) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_Planar,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_Planar,entto : IGESDraw_Planar,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESDraw_Planar) -> bool: 
        """
        Sets automatic unambiguous Correction on a Planar (NbMatrices forced to 1)
        """
    def OwnDump(self,ent : IGESDraw_Planar,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_Planar,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Planar <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_Planar,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_Planar,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolRectArraySubfigure():
    """
    Tool to work on a RectArraySubfigure. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_RectArraySubfigure) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_RectArraySubfigure,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_RectArraySubfigure,entto : IGESDraw_RectArraySubfigure,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDraw_RectArraySubfigure,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_RectArraySubfigure,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a RectArraySubfigure <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_RectArraySubfigure,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_RectArraySubfigure,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolSegmentedViewsVisible():
    """
    Tool to work on a SegmentedViewsVisible. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_SegmentedViewsVisible) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_SegmentedViewsVisible,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_SegmentedViewsVisible,entto : IGESDraw_SegmentedViewsVisible,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDraw_SegmentedViewsVisible,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_SegmentedViewsVisible,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a SegmentedViewsVisible <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_SegmentedViewsVisible,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_SegmentedViewsVisible,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolView():
    """
    Tool to work on a View. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_View) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_View,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_View,entto : IGESDraw_View,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESDraw_View,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESDraw_View,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a View <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESDraw_View,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_View,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolViewsVisible():
    """
    Tool to work on a ViewsVisible. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_ViewsVisible) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_ViewsVisible,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_ViewsVisible,entto : IGESDraw_ViewsVisible,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters shared not implied, i.e. all but the Displayed Entities
        """
    def OwnCorrect(self,ent : IGESDraw_ViewsVisible) -> bool: 
        """
        Sets automatic unambiguous Correction on a ViewsVisible (all displayed entities must refer to <ent> in directory part, else the list is cleared)
        """
    def OwnDump(self,ent : IGESDraw_ViewsVisible,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnImplied(self,ent : IGESDraw_ViewsVisible,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a ViewsVisible <ent>, from its specific (own) implied parameters : the Displayed Entities
        """
    def OwnRenew(self,entfrom : IGESDraw_ViewsVisible,entto : IGESDraw_ViewsVisible,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific implied Parameters : the Displayed Entities which have already been copied
        """
    def OwnShared(self,ent : IGESDraw_ViewsVisible,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a ViewsVisible <ent>, from its specific (own) parameters shared not implied (the Views)
        """
    def OwnWhenDelete(self,ent : IGESDraw_ViewsVisible) -> None: 
        """
        Clears specific implied parameters, which cause looping structures; required for deletion
        """
    def ReadOwnParams(self,ent : IGESDraw_ViewsVisible,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_ViewsVisible,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_ToolViewsVisibleWithAttr():
    """
    Tool to work on a ViewsVisibleWithAttr. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESDraw_ViewsVisibleWithAttr) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESDraw_ViewsVisibleWithAttr,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESDraw_ViewsVisibleWithAttr,entto : IGESDraw_ViewsVisibleWithAttr,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters shared not implied, i.e. all but the Displayed Entities
        """
    def OwnCorrect(self,ent : IGESDraw_ViewsVisibleWithAttr) -> bool: 
        """
        Sets automatic unambiguous Correction on a ViewsVisibleWithAttr (all displayed entities must refer to <ent> in directory part, else the list is cleared)
        """
    def OwnDump(self,ent : IGESDraw_ViewsVisibleWithAttr,dumper : OCP.IGESData.IGESData_IGESDumper,S : io.BytesIO,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnImplied(self,ent : IGESDraw_ViewsVisibleWithAttr,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a ViewsVisible <ent>, from its specific (own) implied parameters : the Displayed Entities
        """
    def OwnRenew(self,entfrom : IGESDraw_ViewsVisibleWithAttr,entto : IGESDraw_ViewsVisibleWithAttr,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific implied Parameters : the Displayed Entities which have already been copied
        """
    def OwnShared(self,ent : IGESDraw_ViewsVisibleWithAttr,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a ViewsVisibleWithAttr <ent>, from its specific (own) parameters shared not implied, i.e. all but the Displayed Entities
        """
    def OwnWhenDelete(self,ent : IGESDraw_ViewsVisibleWithAttr) -> None: 
        """
        Clears specific implied parameters, which cause looping structures; required for deletion
        """
    def ReadOwnParams(self,ent : IGESDraw_ViewsVisibleWithAttr,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESDraw_ViewsVisibleWithAttr,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESDraw_View(OCP.IGESData.IGESData_ViewKindEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGES View Entity, Type <410> Form <0> in package IGESDrawdefines IGES View Entity, Type <410> Form <0> in package IGESDrawdefines IGES View Entity, Type <410> Form <0> in package IGESDraw
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
    def BackPlane(self) -> OCP.IGESGeom.IGESGeom_Plane: 
        """
        returns the back of view volume, or null handle
        """
    def BlankStatus(self) -> int: 
        """
        gives Blank Status (0 visible, 1 blanked)
        """
    def BottomPlane(self) -> OCP.IGESGeom.IGESGeom_Plane: 
        """
        returns the bottom of view volume, or null handle
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
    def FrontPlane(self) -> OCP.IGESGeom.IGESGeom_Plane: 
        """
        returns the front of view volume, or null handle
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBackPlane(self) -> bool: 
        """
        returns False if back of view volume is not present
        """
    def HasBottomPlane(self) -> bool: 
        """
        returns False if bottom of view volume is not present
        """
    def HasFrontPlane(self) -> bool: 
        """
        returns False if front of view volume is not present
        """
    def HasLabelDisplay(self) -> bool: 
        """
        Returns True if a LabelDisplay mode is defined for this entity
        """
    def HasLeftPlane(self) -> bool: 
        """
        returns False if left side of view volume is not present
        """
    def HasName(self) -> bool: 
        """
        says if a Name is defined, as Short Label or as Name Property (Property is looked first, else ShortLabel is considered)
        """
    def HasOneParent(self) -> bool: 
        """
        Returns True if an entity has one and only one parent, defined by a SingleParentEntity Type Associativity (explicit sharing). Thus, implicit sharing remains defined at model level (see class ToolLocation)
        """
    def HasRightPlane(self) -> bool: 
        """
        returns False if right side of view volume is not present
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
    def HasTopPlane(self) -> bool: 
        """
        returns False if top of view volume is not present
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
    def Init(self,aViewNum : int,aScale : float,aLeftPlane : OCP.IGESGeom.IGESGeom_Plane,aTopPlane : OCP.IGESGeom.IGESGeom_Plane,aRightPlane : OCP.IGESGeom.IGESGeom_Plane,aBottomPlane : OCP.IGESGeom.IGESGeom_Plane,aBackPlane : OCP.IGESGeom.IGESGeom_Plane,aFrontPlane : OCP.IGESGeom.IGESGeom_Plane) -> None: 
        """
        This method is used to set fields of the class View - aViewNum : View number - aScale : Scale factor - aLeftPlane : Left plane of view volume - aTopPlane : Top plane of view volume - aRightPlane : Right plane of view volume - aBottomPlane : Bottom plane of view volume - aBackPlane : Back plane of view volume - aFrontPlane : Front plane of view volume
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsSingle(self) -> bool: 
        """
        Returns True (for a single view)
        """
    def LabelDisplay(self) -> OCP.IGESData.IGESData_LabelDisplayEntity: 
        """
        Returns the Label Display Associativity Entity if there is one. Returns a null handle if there is none.
        """
    def LeftPlane(self) -> OCP.IGESGeom.IGESGeom_Plane: 
        """
        returns the left side of view volume, or null handle
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
    def ModelToView(self,coords : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        returns XYZ from the Model space to the View space by applying the View Matrix
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
        Returns 1 (single view)
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
    def RightPlane(self) -> OCP.IGESGeom.IGESGeom_Plane: 
        """
        returns the right side of view volume, or null handle
        """
    def ScaleFactor(self) -> float: 
        """
        returns the scale factor(Default = 1.0)
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
    def TopPlane(self) -> OCP.IGESGeom.IGESGeom_Plane: 
        """
        returns the top of view volume, or null handle
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
    def ViewItem(self,num : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        For a single view, returns <me> whatever <num>
        """
    def ViewList(self) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        Returns the view of this IGES entity as a list. Warning A null handle is returned if the definition status does not have the value DefSeveral.
        """
    def ViewMatrix(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        returns the Transformation Matrix
        """
    def ViewNumber(self) -> int: 
        """
        returns integer number identifying view orientation
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
class IGESDraw_ViewsVisible(OCP.IGESData.IGESData_ViewKindEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    Defines IGESViewsVisible, Type <402>, Form <3> in package IGESDrawDefines IGESViewsVisible, Type <402>, Form <3> in package IGESDrawDefines IGESViewsVisible, Type <402>, Form <3> in package IGESDraw
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
    def DisplayedEntity(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the Index'th entity whose display is being specified by this associativity instance raises exception if Index <= 0 or Index > NbEntityDisplayed()
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
    def Init(self,allViewEntities : IGESDraw_HArray1OfViewKindEntity,allDisplayEntity : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
        """
        This method is used to set the fields of the class ViewsVisible - allViewEntities : All View kind entities - allDisplayEntity : All entities whose display is specified
        """
    def InitColor(self,ent : OCP.IGESData.IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitImplied(self,allDisplayEntity : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
        """
        Changes only the list of Displayed Entities (Null allowed)
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsSingle(self) -> bool: 
        """
        Returns False (for a complex view)
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
    def NbDisplayedEntities(self) -> int: 
        """
        returns the number of entities displayed in the Views or zero if no Entities specified in these Views
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
        returns the Number of views visible
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
    def ViewItem(self,Index : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        returns the Index'th ViewKindEntity Entity raises exception if Index <= 0 or Index > NbViewsVisible()
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
class IGESDraw_ViewsVisibleWithAttr(OCP.IGESData.IGESData_ViewKindEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESViewsVisibleWithAttr, Type <402>, Form <4> in package IGESDrawdefines IGESViewsVisibleWithAttr, Type <402>, Form <4> in package IGESDrawdefines IGESViewsVisibleWithAttr, Type <402>, Form <4> in package IGESDraw
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
    def ColorDefinition(self,Index : int) -> OCP.IGESGraph.IGESGraph_Color: 
        """
        returns the Index'th Color Definition Entity raises exception if Index <= 0 or Index > NbViews()
        """
    def ColorValue(self,Index : int) -> int: 
        """
        returns the Index'th Color number value raises exception if Index <= 0 or Index > NbViews()
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
    def DisplayedEntity(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns Index'th Display entity with this particular characteristics raises exception if Index <= 0 or Index > NbEntities()
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FontDefinition(self,Index : int) -> OCP.IGESData.IGESData_LineFontEntity: 
        """
        returns the Index'th Line Font Definition Entity or NULL(0) raises exception if Index <= 0 or Index > NbViews()
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
    def Init(self,allViewEntities : IGESDraw_HArray1OfViewKindEntity,allLineFonts : OCP.TColStd.TColStd_HArray1OfInteger,allLineDefinitions : OCP.IGESBasic.IGESBasic_HArray1OfLineFontEntity,allColorValues : OCP.TColStd.TColStd_HArray1OfInteger,allColorDefinitions : OCP.IGESGraph.IGESGraph_HArray1OfColor,allLineWeights : OCP.TColStd.TColStd_HArray1OfInteger,allDisplayEntities : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
        """
        This method is used to set fields of the class ViewsVisibleWithAttr - allViewEntities : All View kind entities - allLineFonts : All Line Font values or zero(0) - allLineDefinitions : Line Font Definition (if Line Font value = 0) - allColorValues : All Color values - allColorDefinitions : All Color Definition Entities - allLineWeights : All Line Weight values - allDisplayEntities : Entities which are member of this associativity raises exception if Lengths of allViewEntities, allLineFonts, allColorValues,allColorDefinitions, allLineWeights are not same
        """
    def InitColor(self,ent : OCP.IGESData.IGESData_ColorEntity,rank : int=0) -> None: 
        """
        Initializes Color data : if <ent> is not Null, it gives Color, else <rank> gives or erases (if zero) RankColor
        """
    def InitDirFieldEntity(self,fieldnum : int,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Initializes a directory field as an Entiy of any kind See DirFieldEntity for more details
        """
    def InitImplied(self,allDisplayEntity : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
        """
        Changes only the list of Displayed Entities (Null allowed)
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
    def IsColorDefinition(self,Index : int) -> bool: 
        """
        returns True if Index'th Color Definition is specified else returns False raises exception if Index <= 0 or Index > NbViews()
        """
    def IsFontDefinition(self,Index : int) -> bool: 
        """
        returns True if the Index'th Line Font Definition is specified else returns False raises exception if Index <= 0 or Index > NbViews()
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsSingle(self) -> bool: 
        """
        Returns False (for a complex view)
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
    def LineFontValue(self,Index : int) -> int: 
        """
        returns the Index'th Line font value or zero raises exception if Index <= 0 or Index > NbViews()
        """
    def LineWeight(self) -> float: 
        """
        Returns the true Line Weight, computed from LineWeightNumber and Global Parameter in the Model by call to SetLineWeight
        """
    def LineWeightItem(self,Index : int) -> int: 
        """
        returns the Index'th Color Line Weight raises exception if Index <= 0 or Index > NbViews()
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
    def NbDisplayedEntities(self) -> int: 
        """
        returns the number of entities which have this particular set of display characteristic, or zero if no Entities specified
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
        returns the number of Views containing the view visible, line font, color number, and line weight information
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
    def ViewItem(self,Index : int) -> OCP.IGESData.IGESData_ViewKindEntity: 
        """
        returns the Index'th ViewKindEntity entity raises exception if Index <= 0 or Index > NbViews()
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
