import OCP.IGESGeom
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.TCollection
import OCP.IGESData
import OCP.IGESBasic
import OCP.Message
import OCP.TColgp
import OCP.Standard
import OCP.Interface
import OCP.gp
__all__  = [
"IGESGeom",
"IGESGeom_Array1OfBoundary",
"IGESGeom_Array1OfCurveOnSurface",
"IGESGeom_Array1OfTransformationMatrix",
"IGESGeom_BSplineCurve",
"IGESGeom_BSplineSurface",
"IGESGeom_Boundary",
"IGESGeom_BoundedSurface",
"IGESGeom_CircularArc",
"IGESGeom_CompositeCurve",
"IGESGeom_ConicArc",
"IGESGeom_CopiousData",
"IGESGeom_CurveOnSurface",
"IGESGeom_Direction",
"IGESGeom_Flash",
"IGESGeom_GeneralModule",
"IGESGeom_HArray1OfBoundary",
"IGESGeom_HArray1OfCurveOnSurface",
"IGESGeom_HArray1OfTransformationMatrix",
"IGESGeom_Line",
"IGESGeom_OffsetCurve",
"IGESGeom_OffsetSurface",
"IGESGeom_Plane",
"IGESGeom_Point",
"IGESGeom_Protocol",
"IGESGeom_ReadWriteModule",
"IGESGeom_RuledSurface",
"IGESGeom_SpecificModule",
"IGESGeom_SplineCurve",
"IGESGeom_SplineSurface",
"IGESGeom_SurfaceOfRevolution",
"IGESGeom_TabulatedCylinder",
"IGESGeom_ToolBSplineCurve",
"IGESGeom_ToolBSplineSurface",
"IGESGeom_ToolBoundary",
"IGESGeom_ToolBoundedSurface",
"IGESGeom_ToolCircularArc",
"IGESGeom_ToolCompositeCurve",
"IGESGeom_ToolConicArc",
"IGESGeom_ToolCopiousData",
"IGESGeom_ToolCurveOnSurface",
"IGESGeom_ToolDirection",
"IGESGeom_ToolFlash",
"IGESGeom_ToolLine",
"IGESGeom_ToolOffsetCurve",
"IGESGeom_ToolOffsetSurface",
"IGESGeom_ToolPlane",
"IGESGeom_ToolPoint",
"IGESGeom_ToolRuledSurface",
"IGESGeom_ToolSplineCurve",
"IGESGeom_ToolSplineSurface",
"IGESGeom_ToolSurfaceOfRevolution",
"IGESGeom_ToolTabulatedCylinder",
"IGESGeom_ToolTransformationMatrix",
"IGESGeom_ToolTrimmedSurface",
"IGESGeom_TransformationMatrix",
"IGESGeom_TrimmedSurface"
]
class IGESGeom():
    """
    This package consists of B-Rep and CSG Solid entities
    """
    @staticmethod
    def Init_s() -> None: 
        """
        Prepares dymanic data (Protocol, Modules) for this package
        """
    @staticmethod
    def Protocol_s() -> IGESGeom_Protocol: 
        """
        Returns the Protocol for this Package
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_Array1OfBoundary():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESGeom_Array1OfBoundary) -> IGESGeom_Array1OfBoundary: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESGeom_Boundary: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGeom_Boundary: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGeom_Boundary: 
        """
        Variable value access
        """
    def First(self) -> IGESGeom_Boundary: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESGeom_Boundary) -> None: 
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
    def Last(self) -> IGESGeom_Boundary: 
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
    def Move(self,theOther : IGESGeom_Array1OfBoundary) -> IGESGeom_Array1OfBoundary: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGeom_Boundary) -> None: 
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
    def Value(self,theIndex : int) -> IGESGeom_Boundary: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : IGESGeom_Boundary,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IGESGeom_Array1OfBoundary) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESGeom_Array1OfCurveOnSurface():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESGeom_Array1OfCurveOnSurface) -> IGESGeom_Array1OfCurveOnSurface: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESGeom_CurveOnSurface: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGeom_CurveOnSurface: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGeom_CurveOnSurface: 
        """
        Variable value access
        """
    def First(self) -> IGESGeom_CurveOnSurface: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESGeom_CurveOnSurface) -> None: 
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
    def Last(self) -> IGESGeom_CurveOnSurface: 
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
    def Move(self,theOther : IGESGeom_Array1OfCurveOnSurface) -> IGESGeom_Array1OfCurveOnSurface: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGeom_CurveOnSurface) -> None: 
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
    def Value(self,theIndex : int) -> IGESGeom_CurveOnSurface: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : IGESGeom_Array1OfCurveOnSurface) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : IGESGeom_CurveOnSurface,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESGeom_Array1OfTransformationMatrix():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : IGESGeom_Array1OfTransformationMatrix) -> IGESGeom_Array1OfTransformationMatrix: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> IGESGeom_TransformationMatrix: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGeom_TransformationMatrix: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGeom_TransformationMatrix: 
        """
        Variable value access
        """
    def First(self) -> IGESGeom_TransformationMatrix: 
        """
        Returns first element
        """
    def Init(self,theValue : IGESGeom_TransformationMatrix) -> None: 
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
    def Last(self) -> IGESGeom_TransformationMatrix: 
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
    def Move(self,theOther : IGESGeom_Array1OfTransformationMatrix) -> IGESGeom_Array1OfTransformationMatrix: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGeom_TransformationMatrix) -> None: 
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
    def Value(self,theIndex : int) -> IGESGeom_TransformationMatrix: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IGESGeom_Array1OfTransformationMatrix) -> None: ...
    @overload
    def __init__(self,theBegin : IGESGeom_TransformationMatrix,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IGESGeom_BSplineCurve(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESBSplineCurve, Type <126> Form <0-5> in package IGESGeom A parametric equation obtained by dividing two summations involving weights (which are real numbers), the control points, and B-Spline basis functionsdefines IGESBSplineCurve, Type <126> Form <0-5> in package IGESGeom A parametric equation obtained by dividing two summations involving weights (which are real numbers), the control points, and B-Spline basis functionsdefines IGESBSplineCurve, Type <126> Form <0-5> in package IGESGeom A parametric equation obtained by dividing two summations involving weights (which are real numbers), the control points, and B-Spline basis functions
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
    def Degree(self) -> int: 
        """
        returns the degree of basis functions
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
    def Init(self,anIndex : int,aDegree : int,aPlanar : bool,aClosed : bool,aPolynom : bool,aPeriodic : bool,allKnots : OCP.TColStd.TColStd_HArray1OfReal,allWeights : OCP.TColStd.TColStd_HArray1OfReal,allPoles : OCP.TColgp.TColgp_HArray1OfXYZ,aUmin : float,aUmax : float,aNorm : OCP.gp.gp_XYZ) -> None: 
        """
        This method is used to set the fields of the class BSplineCurve. Beware about indexation of arrays - anIndex : Upper index of the sum - aDegree : Degree of basis functions - aPlanar : 0 = nonplanar curve, 1 = planar curve - aClosed : 0 = open curve, 1 = closed curve - aPolynom : 0 = rational, 1 = polynomial - aPeriodic : 0 = nonperiodic, 1 = periodic - allKnots : Knot sequence values [-Degree,Index+1] - allWeights : Array of weights [0,Index] - allPoles : X, Y, Z coordinates of all control points [0,Index] - aUmin, aUmax : Starting and ending parameter values - aNorm : Unit normal (if the curve is planar) raises exception if allWeights & allPoles are not of same size.
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
    def IsClosed(self) -> bool: 
        """
        returns True if the curve is closed, False if open
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
    def IsPeriodic(self) -> bool: 
        """
        returns True if the curve is periodic, False otherwise
        """
    def IsPlanar(self) -> bool: 
        """
        returns True if the curve is Planar, False if non-planar
        """
    def IsPolynomial(self,flag : bool=False) -> bool: 
        """
        returns True if the curve is polynomial, False if rational <flag> False (D) : computed from the list of weights (all must be equal) <flag> True : as recorded
        """
    def Knot(self,anIndex : int) -> float: 
        """
        returns the knot referred to by anIndex, inside the range [-Degree,UpperIndex+1] raises exception if anIndex < -Degree() or anIndex > (NbKnots() - Degree()) Note : Knots are numbered from -Degree (not from 1)
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
    def NbKnots(self) -> int: 
        """
        returns the number of knots (i.e. Degree + UpperIndex + 2)
        """
    def NbPoles(self) -> int: 
        """
        returns number of poles (i.e. UpperIndex + 1)
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
    def Normal(self) -> OCP.gp.gp_XYZ: 
        """
        if the curve is nonplanar then (0, 0, 0) is returned
        """
    def Pole(self,anIndex : int) -> OCP.gp.gp_Pnt: 
        """
        returns the pole referred to by anIndex, in [0,UpperIndex] raises exception if anIndex < 0 or anIndex > UpperIndex()
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
        Changes FormNumber (indicates the Shape of the Curve) Error if not in range [0-5]
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
    def TransformedPole(self,anIndex : int) -> OCP.gp.gp_Pnt: 
        """
        returns the anIndex'th pole after applying Transf. Matrix raises exception if an Index < 0 or an Index > UpperIndex()
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
    def UMax(self) -> float: 
        """
        returns ending parameter value
        """
    def UMin(self) -> float: 
        """
        returns starting parameter value
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UpperIndex(self) -> int: 
        """
        returns the upper index of the sum (see Knots,Poles)
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
    def Weight(self,anIndex : int) -> float: 
        """
        returns the weight referred to by anIndex, in [0,UpperIndex] raises exception if anIndex < 0 or anIndex > UpperIndex()
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
class IGESGeom_BSplineSurface(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESBSplineSurface, Type <128> Form <0-9> in package IGESGeom A parametric equation obtained by dividing two summations involving weights (which are real numbers), the control points, and B-Spline basis functionsdefines IGESBSplineSurface, Type <128> Form <0-9> in package IGESGeom A parametric equation obtained by dividing two summations involving weights (which are real numbers), the control points, and B-Spline basis functionsdefines IGESBSplineSurface, Type <128> Form <0-9> in package IGESGeom A parametric equation obtained by dividing two summations involving weights (which are real numbers), the control points, and B-Spline basis functions
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
    def DegreeU(self) -> int: 
        """
        returns degree of first set of basis functions
        """
    def DegreeV(self) -> int: 
        """
        returns degree of second set of basis functions
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
    def Init(self,anIndexU : int,anIndexV : int,aDegU : int,aDegV : int,aCloseU : bool,aCloseV : bool,aPolynom : bool,aPeriodU : bool,aPeriodV : bool,allKnotsU : OCP.TColStd.TColStd_HArray1OfReal,allKnotsV : OCP.TColStd.TColStd_HArray1OfReal,allWeights : OCP.TColStd.TColStd_HArray2OfReal,allPoles : OCP.TColgp.TColgp_HArray2OfXYZ,aUmin : float,aUmax : float,aVmin : float,aVmax : float) -> None: 
        """
        This method is used to set the fields of the class BSplineSurface - anIndexU : Upper index of first sum - anIndexV : Upper index of second sum - aDegU, aDegV : Degrees of first and second sets of basis functions - aCloseU, aCloseV : 1 = Closed in U, V directions 0 = open in U, V directions - aPolynom : 0 = Rational, 1 = polynomial - aPeriodU, aPeriodV : 0 = Non periodic in U or V direction 1 = Periodic in U or V direction - allKnotsU, allKnotsV : Knots in U and V directions - allWeights : Array of weights - allPoles : XYZ coordinates of all control points - aUmin : Starting value of U direction - aUmax : Ending value of U direction - aVmin : Starting value of V direction - aVmax : Ending value of V direction raises exception if allWeights & allPoles are not of same size.
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
    def IsClosedU(self) -> bool: 
        """
        True if closed in U direction else False
        """
    def IsClosedV(self) -> bool: 
        """
        True if closed in V direction else False
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
    def IsPeriodicU(self) -> bool: 
        """
        True if periodic in U direction else False
        """
    def IsPeriodicV(self) -> bool: 
        """
        True if periodic in V direction else False
        """
    def IsPolynomial(self,flag : bool=False) -> bool: 
        """
        True if polynomial, False if rational <flag> False (D) : computed from Weights <flag> True : recorded
        """
    def KnotU(self,anIndex : int) -> float: 
        """
        returns the value of knot referred to by anIndex in U direction raises exception if anIndex < -DegreeU() or anIndex > (NbKnotsU() - DegreeU())
        """
    def KnotV(self,anIndex : int) -> float: 
        """
        returns the value of knot referred to by anIndex in V direction raises exception if anIndex < -DegreeV() or anIndex > (NbKnotsV() - DegreeV())
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
    def NbKnotsU(self) -> int: 
        """
        returns number of knots in U direction KnotsU are numbered from -DegreeU
        """
    def NbKnotsV(self) -> int: 
        """
        returns number of knots in V direction KnotsV are numbered from -DegreeV
        """
    def NbPolesU(self) -> int: 
        """
        returns number of poles in U direction
        """
    def NbPolesV(self) -> int: 
        """
        returns number of poles in V direction
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
    def Pole(self,anIndex1 : int,anIndex2 : int) -> OCP.gp.gp_Pnt: 
        """
        returns the control point referenced by anIndex1, anIndex2 raises exception if anIndex1 <= 0 or anIndex1 > NbPolesU() or if anIndex2 <= 0 or anIndex2 > NbPolesV()
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
        Changes FormNumber (indicates the Shape of the Surface) Error if not in range [0-9]
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
    def TransformedPole(self,anIndex1 : int,anIndex2 : int) -> OCP.gp.gp_Pnt: 
        """
        returns the control point referenced by anIndex1, anIndex2 after applying the Transf.Matrix raises exception if anIndex1 <= 0 or anIndex1 > NbPolesU() or if anIndex2 <= 0 or anIndex2 > NbPolesV()
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
    def UMax(self) -> float: 
        """
        returns ending value in the U direction
        """
    def UMin(self) -> float: 
        """
        returns starting value in the U direction
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UpperIndexU(self) -> int: 
        """
        returns the upper index of the first sum (U)
        """
    def UpperIndexV(self) -> int: 
        """
        returns the upper index of the second sum (V)
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VMax(self) -> float: 
        """
        returns ending value in the V direction
        """
    def VMin(self) -> float: 
        """
        returns starting value in the V direction
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
    def Weight(self,anIndex1 : int,anIndex2 : int) -> float: 
        """
        returns the weight referred to by anIndex1, anIndex2 raises exception if anIndex1 <= 0 or anIndex1 > NbPolesU() or if anIndex2 <= 0 or anIndex2 > NbPolesV()
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
class IGESGeom_Boundary(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESBoundary, Type <141> Form <0> in package IGESGeom A boundary entity identifies a surface boundary consisting of a set of curves lying on the surfacedefines IGESBoundary, Type <141> Form <0> in package IGESGeom A boundary entity identifies a surface boundary consisting of a set of curves lying on the surfacedefines IGESBoundary, Type <141> Form <0> in package IGESGeom A boundary entity identifies a surface boundary consisting of a set of curves lying on the surface
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
    def BoundaryType(self) -> int: 
        """
        returns type of bounded surface representation 0 = Boundary entities may only reference model space trimming curves. Associated surface representation may be parametric 1 = Boundary entities must reference model space curves and associated parameter space curve collections. Associated surface must be a parametric representation
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
    def Init(self,aType : int,aPreference : int,aSurface : OCP.IGESData.IGESData_IGESEntity,allModelCurves : OCP.IGESData.IGESData_HArray1OfIGESEntity,allSenses : OCP.TColStd.TColStd_HArray1OfInteger,allParameterCurves : OCP.IGESBasic.IGESBasic_HArray1OfHArray1OfIGESEntity) -> None: 
        """
        This method is used to set the fields of the class Boundary - aType : Type of bounded surface representation - aPreference : Preferred representation of Trimming Curve - aSurface : Untrimmed surface to be bounded - allModelCurves : Model Space Curves - allSenses : Orientation flags of all Model Space Curves - allParameterCurves : Parameter Space Curves raises exception if allSenses, allModelCurves and allParameterCurves do not have same dimensions
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
    def ModelSpaceCurve(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns Model Space Curve raises exception if Index <= 0 or Index > NbModelSpaceCurves()
        """
    def NameValue(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        returns Name value as a String (Property Name or ShortLabel) if SubNumber is defined, it is concatenated after ShortLabel as follows label(number). Ignored with a Property Name
        """
    def NbAssociativities(self) -> int: 
        """
        gives number of recorded associativities (0 no list defined)
        """
    def NbModelSpaceCurves(self) -> int: 
        """
        returns the number of model space curves
        """
    def NbParameterCurves(self,Index : int) -> int: 
        """
        returns the number of parameter curves associated with one model space curve referred to by Index raises exception if Index <= 0 or Index > NbModelSpaceCurves()
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
    def ParameterCurve(self,Index : int,Num : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns an individual parameter curve raises exception if Index or Num is out of range
        """
    def ParameterCurves(self,Index : int) -> OCP.IGESData.IGESData_HArray1OfIGESEntity: 
        """
        returns an array of parameter space curves associated with a model space curve referred to by the Index raises exception if Index <= 0 or Index > NbModelSpaceCurves()
        """
    def PreferenceType(self) -> int: 
        """
        returns preferred representation of trimming curves 0 = Unspecified 1 = Model space 2 = Parameter space 3 = Representations are of equal preference
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
    def Sense(self,Index : int) -> int: 
        """
        returns the sense of a particular model space curve 1 = model curve direction does not need reversal 2 = model curve direction needs to be reversed raises exception if Index <= 0 or Index > NbModelSpaceCurves()
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
    def Surface(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the surface to be bounded
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
class IGESGeom_BoundedSurface(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines BoundedSurface, Type <143> Form <0> in package IGESGeom A bounded surface is used to communicate trimmed surfaces. The surface and trimming curves are assumed to be represented parametrically.defines BoundedSurface, Type <143> Form <0> in package IGESGeom A bounded surface is used to communicate trimmed surfaces. The surface and trimming curves are assumed to be represented parametrically.defines BoundedSurface, Type <143> Form <0> in package IGESGeom A bounded surface is used to communicate trimmed surfaces. The surface and trimming curves are assumed to be represented parametrically.
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
    def Boundary(self,Index : int) -> IGESGeom_Boundary: 
        """
        returns boundary entity raises exception if Index <= 0 or Index > NbBoundaries()
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
    def Init(self,aType : int,aSurface : OCP.IGESData.IGESData_IGESEntity,allBounds : IGESGeom_HArray1OfBoundary) -> None: 
        """
        This method is used to set the fields of the class BoundedSurface - aType : Type of bounded surface representation - aSurface : Surface entity to be bounded - allBounds : Array of boundary entities
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
    def NbBoundaries(self) -> int: 
        """
        returns the number of boundaries
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
    def RepresentationType(self) -> int: 
        """
        returns the type of Bounded surface representation 0 = The boundary entities may only reference model space curves 1 = The boundary entities may reference both model space curves and associated parameter space curve representations
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
    def Surface(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the bounded surface
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
class IGESGeom_CircularArc(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESCircularArc, Type <100> Form <0> in package IGESGeom A circular arc is a connected portion of a parent circle which consists of more than one point. The definition space coordinate system is always chosen so that the circular arc remains in a plane either coincident with or parallel to the XT, YT plane.defines IGESCircularArc, Type <100> Form <0> in package IGESGeom A circular arc is a connected portion of a parent circle which consists of more than one point. The definition space coordinate system is always chosen so that the circular arc remains in a plane either coincident with or parallel to the XT, YT plane.defines IGESCircularArc, Type <100> Form <0> in package IGESGeom A circular arc is a connected portion of a parent circle which consists of more than one point. The definition space coordinate system is always chosen so that the circular arc remains in a plane either coincident with or parallel to the XT, YT plane.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def Angle(self) -> float: 
        """
        returns the angle subtended by the arc at the center in radians
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
    def Axis(self) -> OCP.gp.gp_Dir: 
        """
        Z-Axis of circle (i.e. [0,0,1])
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
        returns the center of the circle of which arc forms a part
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
    def EndPoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the end point of the arc
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
    def Init(self,aZT : float,aCenter : OCP.gp.gp_XY,aStart : OCP.gp.gp_XY,anEnd : OCP.gp.gp_XY) -> None: 
        """
        This method is used to set the fields of the class CircularArc - aZT : Shift above the Z plane - aCenter : Center of the circle of which the arc forms a part - aStart : Starting point of the circular arc - anEnd : Ending point of the circular arc
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
    def IsClosed(self) -> bool: 
        """
        True if StartPoint = EndPoint
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
    def Properties(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Property List under the form of an EntityIterator
        """
    def Radius(self) -> float: 
        """
        returns the radius of the circle of which arc forms a part
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
    def StartPoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the start point of the arc
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
    def TransformedAxis(self) -> OCP.gp.gp_Dir: 
        """
        Z-Axis after applying Trans. Matrix
        """
    def TransformedCenter(self) -> OCP.gp.gp_Pnt: 
        """
        returns the center of the circle of which arc forms a part after applying Transf. Matrix
        """
    def TransformedEndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the end point of the arc after applying Transf. Matrix
        """
    def TransformedStartPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the start point of the arc after applying Transf. Matrix
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
    def ZPlane(self) -> float: 
        """
        returns the parallel displacement of the plane containing the arc from the XT, YT plane
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
class IGESGeom_CompositeCurve(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESCompositeCurve, Type <102> Form <0> in package IGESGeom A composite curve is defined as an ordered list of entities consisting of a point, connect point and parametrised curve entities (excluding the CompositeCurve entity).defines IGESCompositeCurve, Type <102> Form <0> in package IGESGeom A composite curve is defined as an ordered list of entities consisting of a point, connect point and parametrised curve entities (excluding the CompositeCurve entity).defines IGESCompositeCurve, Type <102> Form <0> in package IGESGeom A composite curve is defined as an ordered list of entities consisting of a point, connect point and parametrised curve entities (excluding the CompositeCurve entity).
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
    def Curve(self,Index : int) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns Component of the CompositeCurve (a curve or a point) raises exception if Index <= 0 or Index > NbCurves()
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
    def Init(self,allEntities : OCP.IGESData.IGESData_HArray1OfIGESEntity) -> None: 
        """
        This method is used to set the fields of the class CompositeCurve - allEntities : Constituent Entities of the composite curve
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
    def NbCurves(self) -> int: 
        """
        returns the number of curves contained in the CompositeCurve
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
class IGESGeom_ConicArc(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESConicArc, Type <104> Form <0-3> in package IGESGeom A conic arc is a bounded connected portion of a parent conic curve which consists of more than one point. The parent conic curve is either an ellipse, a parabola, or a hyperbola. The definition space coordinate system is always chosen so that the conic arc lies in a plane either coincident with or parallel to XT, YT plane. Within such a plane a conic is defined by the six coefficients in the following equation. A*XT^2 + B*XT*YT + C*YT^2 + D*XT + E*YT + F = 0defines IGESConicArc, Type <104> Form <0-3> in package IGESGeom A conic arc is a bounded connected portion of a parent conic curve which consists of more than one point. The parent conic curve is either an ellipse, a parabola, or a hyperbola. The definition space coordinate system is always chosen so that the conic arc lies in a plane either coincident with or parallel to XT, YT plane. Within such a plane a conic is defined by the six coefficients in the following equation. A*XT^2 + B*XT*YT + C*YT^2 + D*XT + E*YT + F = 0defines IGESConicArc, Type <104> Form <0-3> in package IGESGeom A conic arc is a bounded connected portion of a parent conic curve which consists of more than one point. The parent conic curve is either an ellipse, a parabola, or a hyperbola. The definition space coordinate system is always chosen so that the conic arc lies in a plane either coincident with or parallel to XT, YT plane. Within such a plane a conic is defined by the six coefficients in the following equation. A*XT^2 + B*XT*YT + C*YT^2 + D*XT + E*YT + F = 0
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
    def Axis(self) -> OCP.gp.gp_Dir: 
        """
        Z-Axis of conic (i.e. [0,0,1])
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
    def ComputedDefinition(self) -> Tuple[float, float, float, float, float, float]: 
        """
        Computes and returns the coordinates of the definition of a comic from its equation. Used by Definition & TransformedDefinition, or may be called directly if needed
        """
    def ComputedFormNumber(self) -> int: 
        """
        Computes the Form Number according to the equation 1 for Ellipse, 2 for Hyperbola, 3 for Parabola
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
    def Definition(self,Center : OCP.gp.gp_Pnt,MainAxis : OCP.gp.gp_Dir) -> Tuple[float, float]: 
        """
        Returns a Definition computed from equation, easier to use <Center> : the center of the the conic (meaningless for a parabola) (defined with Z displacement) <MainAxis> : the Main Axis of the conic (for a Circle, arbitrary the X Axis) <Rmin,Rmax> : Minor and Major Radii of the conic For a Circle, Rmin = Rmax, For a Parabola, Rmin = Rmax = the Focal Warning : the basic definition (by equation) is not very stable, limit cases may be approximative
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
    def EndPoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the end point of the arc
        """
    def Equation(self) -> Tuple[float, float, float, float, float, float]: 
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
    def Init(self,A : float,B : float,C : float,D : float,E : float,F : float,ZT : float,aStart : OCP.gp.gp_XY,anEnd : OCP.gp.gp_XY) -> None: 
        """
        This method is used to set the fields of the class ConicalArc - A, B, C, D, E, F : Coefficients of the equation defining conic arc - ZT : Parallel ZT displacement of the arc from XT, YT plane. - aStart : Starting point of the conic arc - anEnd : End point of the conic arc
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
    def IsClosed(self) -> bool: 
        """
        returns True if StartPoint = EndPoint
        """
    def IsFromEllipse(self) -> bool: 
        """
        returns True if parent conic curve is an ellipse
        """
    def IsFromHyperbola(self) -> bool: 
        """
        returns True if parent conic curve is a hyperbola
        """
    def IsFromParabola(self) -> bool: 
        """
        returns True if parent conic curve is a parabola
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
    def OwnCorrect(self) -> bool: 
        """
        sets the Form Number equal to ComputedFormNumber, returns True if changed
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
    def StartPoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the starting point of the arc
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
    def TransformedAxis(self) -> OCP.gp.gp_Dir: 
        """
        Z-Axis after applying Trans. Matrix
        """
    def TransformedDefinition(self,Center : OCP.gp.gp_Pnt,MainAxis : OCP.gp.gp_Dir) -> Tuple[float, float]: 
        """
        Same as Definition, but the Location is applied on the Center and the MainAxis
        """
    def TransformedEndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the end point of the arc after applying Transf. Matrix
        """
    def TransformedStartPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the starting point of the arc after applying Transf. Matrix
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
    def ZPlane(self) -> float: 
        """
        returns the Z displacement of the arc from XT, YT plane
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
class IGESGeom_CopiousData(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESCopiousData, Type <106> Form <1-3,11-13,63> in package IGESGeom This entity stores data points in the form of pairs, triples, or sextuples. An interpretation flag value signifies which of these forms is being used.defines IGESCopiousData, Type <106> Form <1-3,11-13,63> in package IGESGeom This entity stores data points in the form of pairs, triples, or sextuples. An interpretation flag value signifies which of these forms is being used.defines IGESCopiousData, Type <106> Form <1-3,11-13,63> in package IGESGeom This entity stores data points in the form of pairs, triples, or sextuples. An interpretation flag value signifies which of these forms is being used.
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
    def Data(self,NumPoint : int,NumData : int) -> float: 
        """
        Returns an individual Data, given the N0 of the Point and the B0 of the Coordinate (according DataType)
        """
    def DataType(self) -> int: 
        """
        returns data type 1 = XY ( with common Z given by plane) 2 = XYZ ( point) 3 = XYZ + Vec(XYZ) (point + normal vector)
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
    def Init(self,aDataType : int,aZPlane : float,allData : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        This method is used to set the fields of the class CopiousData - aDataType : Specifies whether data is a pair or a triple or a sextuple. - aZPlane : Common Z value for all points if datatype = 1 - allData : Data to be read in groups of 2, 3 or 6
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
    def IsClosedPath2D(self) -> bool: 
        """
        Returns True if <me> is a Closed Path 2D (Form 63)
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
    def IsPointSet(self) -> bool: 
        """
        Returns True if <me> is a Set of Points (Form 1-2-3)
        """
    def IsPolyline(self) -> bool: 
        """
        Returns True if <me> is a Polyline (Form 11-12-13)
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
    def NbPoints(self) -> int: 
        """
        returns the number of tuples
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
    def Point(self,anIndex : int) -> OCP.gp.gp_Pnt: 
        """
        returns the coordinates of the point specified by the anIndex raises exception if anIndex <= 0 or anIndex > NbPoints()
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
    def SetClosedPath2D(self) -> None: 
        """
        Sets Copious Data to be a Closed Path 2D (Form 63) Warning : DataType is not checked and must be set to ONE by Init
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def SetPolyline(self,mode : bool) -> None: 
        """
        Sets Copious Data to be a Polyline if <mode> is True (Form = 11-12-13) or a Set of Points else (Form 1-2-3)
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
    def TransformedPoint(self,anIndex : int) -> OCP.gp.gp_Pnt: 
        """
        returns the coordinates of the point specified by the anIndex after applying Transf. Matrix raises exception if anIndex <= 0 or anIndex > NbPoints()
        """
    def TransformedVector(self,anIndex : int) -> OCP.gp.gp_Vec: 
        """
        returns transformed vector if 3-tuple else returns (0, 0, 0) raises exception if anIndex <= 0 or anIndex > NbPoints()
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
    def Vector(self,anIndex : int) -> OCP.gp.gp_Vec: 
        """
        returns i, j, k values if 3-tuple else returns (0, 0, 0) raises exception if anIndex <= 0 or anIndex > NbPoints()
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
    def ZPlane(self) -> float: 
        """
        If datatype = 1, then returns common z value for all data else returns 0
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
class IGESGeom_CurveOnSurface(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESCurveOnSurface, Type <142> Form <0> in package IGESGeom A curve on a parametric surface entity associates a given curve with a surface and identifies the curve as lying on the surface.defines IGESCurveOnSurface, Type <142> Form <0> in package IGESGeom A curve on a parametric surface entity associates a given curve with a surface and identifies the curve as lying on the surface.defines IGESCurveOnSurface, Type <142> Form <0> in package IGESGeom A curve on a parametric surface entity associates a given curve with a surface and identifies the curve as lying on the surface.
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
    def CreationMode(self) -> int: 
        """
        returns the mode in which the curve is created on the surface 0 = Unspecified 1 = Projection of a given curve on the surface 2 = Intersection of two surfaces 3 = Isoparametric curve, i.e:- either a `u` parametric or a `v` parametric curve
        """
    def Curve3D(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns curve C
        """
    def CurveUV(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns curve S
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
    def Init(self,aMode : int,aSurface : OCP.IGESData.IGESData_IGESEntity,aCurveUV : OCP.IGESData.IGESData_IGESEntity,aCurve3D : OCP.IGESData.IGESData_IGESEntity,aPreference : int) -> None: 
        """
        This method is used to set the fields of the class CurveOnSurface - aMode : Way the curve on the surface has been created - aSurface : Surface on which the curve lies - aCurveUV : Curve S (UV) - aCurve3D : Curve C (3D) - aPreference : 0 = Unspecified 1 = S o B is preferred 2 = C is preferred 3 = C and S o B are equally preferred
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
    def PreferenceMode(self) -> int: 
        """
        returns preference mode 0 = Unspecified 1 = S o B is preferred 2 = C is preferred 3 = C and S o B are equally preferred
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
    def Surface(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the surface on which the curve lies
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
class IGESGeom_Direction(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESDirection, Type <123> Form <0> in package IGESGeom A direction entity is a non-zero vector in Euclidean 3-space that is defined by its three components (direction ratios) with respect to the coordinate axes. If x, y, z are the direction ratios then (x^2 + y^2 + z^2) > 0defines IGESDirection, Type <123> Form <0> in package IGESGeom A direction entity is a non-zero vector in Euclidean 3-space that is defined by its three components (direction ratios) with respect to the coordinate axes. If x, y, z are the direction ratios then (x^2 + y^2 + z^2) > 0defines IGESDirection, Type <123> Form <0> in package IGESGeom A direction entity is a non-zero vector in Euclidean 3-space that is defined by its three components (direction ratios) with respect to the coordinate axes. If x, y, z are the direction ratios then (x^2 + y^2 + z^2) > 0
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
    def Init(self,aDirection : OCP.gp.gp_XYZ) -> None: 
        """
        This method is used to set the fields of the class Direction - aDirection : Direction ratios, Z is 0 by default
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
    def TransformedValue(self) -> OCP.gp.gp_Vec: 
        """
        returns the Direction value after applying Transformation matrix
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
    def Value(self) -> OCP.gp.gp_Vec: 
        """
        None
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
class IGESGeom_Flash(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESFlash, Type <125> Form <0 - 4> in package IGESGeom A flash entity is a point in the ZT=0 plane that locates a particular closed area. That closed area can be defined in one of two ways. First, it can be an arbitrary closed area defined by any entity capable of defining a closed area. The points of this entity must all lie in the ZT=0 plane. Second, it can be a member of a predefined set of flash shapes.defines IGESFlash, Type <125> Form <0 - 4> in package IGESGeom A flash entity is a point in the ZT=0 plane that locates a particular closed area. That closed area can be defined in one of two ways. First, it can be an arbitrary closed area defined by any entity capable of defining a closed area. The points of this entity must all lie in the ZT=0 plane. Second, it can be a member of a predefined set of flash shapes.defines IGESFlash, Type <125> Form <0 - 4> in package IGESGeom A flash entity is a point in the ZT=0 plane that locates a particular closed area. That closed area can be defined in one of two ways. First, it can be an arbitrary closed area defined by any entity capable of defining a closed area. The points of this entity must all lie in the ZT=0 plane. Second, it can be a member of a predefined set of flash shapes.
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
    def Dimension1(self) -> float: 
        """
        returns first flash sizing parameter
        """
    def Dimension2(self) -> float: 
        """
        returns second flash sizing parameter
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
    def HasReferenceEntity(self) -> bool: 
        """
        returns True if referenced entity is present.
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
    def Init(self,aPoint : OCP.gp.gp_XY,aDim : float,anotherDim : float,aRotation : float,aReference : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        This method is used to set the fields of the class Flash - aPoint : Reference of flash - aDim : First flash sizing parameter - anotherDim : Second flash sizing parameter - aRotation : Rotation of flash about reference point in radians - aReference : Pointer to the referenced entity or Null
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
    def ReferenceEntity(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the referenced entity or Null handle.
        """
    def ReferencePoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        returns the referenced point, Z = 0 always
        """
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def Rotation(self) -> float: 
        """
        returns the angle in radians of the rotation of flash about the reference point
        """
    def SetFormNumber(self,form : int) -> None: 
        """
        Changes FormNumber (indicates the Nature of the Flash : 0 Unspecified, then given by Reference, 1->4 various Specialisations (Circle,Rectangle, etc...) ) Error if not in range [0-4]
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
    def TransformedReferencePoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the referenced point after applying Transf. Matrix
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
class IGESGeom_GeneralModule(OCP.IGESData.IGESData_GeneralModule, OCP.Interface.Interface_GeneralModule, OCP.Standard.Standard_Transient):
    """
    Definition of General Services for IGESGeom (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESGeom (specific part) This Services comprise : Shared & Implied Lists, Copy, CheckDefinition of General Services for IGESGeom (specific part) This Services comprise : Shared & Implied Lists, Copy, Check
    """
    def CanCopy(self,CN : int,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Specific answer to the question "is Copy properly implemented" For IGES, answer is always True
        """
    def CategoryNumber(self,CN : int,ent : OCP.Standard.Standard_Transient,shares : OCP.Interface.Interface_ShareTool) -> int: 
        """
        Returns a category number which characterizes an entity Shape for all, but Drawing for : Flash; Point with a symbol; Plane with a symbol
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
class IGESGeom_HArray1OfBoundary(IGESGeom_Array1OfBoundary, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESGeom_Array1OfBoundary: 
        """
        None
        """
    def Assign(self,theOther : IGESGeom_Array1OfBoundary) -> IGESGeom_Array1OfBoundary: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESGeom_Array1OfBoundary: 
        """
        None
        """
    def ChangeFirst(self) -> IGESGeom_Boundary: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGeom_Boundary: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGeom_Boundary: 
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
    def First(self) -> IGESGeom_Boundary: 
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
    def Init(self,theValue : IGESGeom_Boundary) -> None: 
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
    def Last(self) -> IGESGeom_Boundary: 
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
    def Move(self,theOther : IGESGeom_Array1OfBoundary) -> IGESGeom_Array1OfBoundary: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGeom_Boundary) -> None: 
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
    def Value(self,theIndex : int) -> IGESGeom_Boundary: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IGESGeom_Array1OfBoundary) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESGeom_Boundary) -> None: ...
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
class IGESGeom_HArray1OfCurveOnSurface(IGESGeom_Array1OfCurveOnSurface, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESGeom_Array1OfCurveOnSurface: 
        """
        None
        """
    def Assign(self,theOther : IGESGeom_Array1OfCurveOnSurface) -> IGESGeom_Array1OfCurveOnSurface: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESGeom_Array1OfCurveOnSurface: 
        """
        None
        """
    def ChangeFirst(self) -> IGESGeom_CurveOnSurface: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGeom_CurveOnSurface: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGeom_CurveOnSurface: 
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
    def First(self) -> IGESGeom_CurveOnSurface: 
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
    def Init(self,theValue : IGESGeom_CurveOnSurface) -> None: 
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
    def Last(self) -> IGESGeom_CurveOnSurface: 
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
    def Move(self,theOther : IGESGeom_Array1OfCurveOnSurface) -> IGESGeom_Array1OfCurveOnSurface: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGeom_CurveOnSurface) -> None: 
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
    def Value(self,theIndex : int) -> IGESGeom_CurveOnSurface: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESGeom_CurveOnSurface) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : IGESGeom_Array1OfCurveOnSurface) -> None: ...
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
class IGESGeom_HArray1OfTransformationMatrix(IGESGeom_Array1OfTransformationMatrix, OCP.Standard.Standard_Transient):
    def Array1(self) -> IGESGeom_Array1OfTransformationMatrix: 
        """
        None
        """
    def Assign(self,theOther : IGESGeom_Array1OfTransformationMatrix) -> IGESGeom_Array1OfTransformationMatrix: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> IGESGeom_Array1OfTransformationMatrix: 
        """
        None
        """
    def ChangeFirst(self) -> IGESGeom_TransformationMatrix: 
        """
        Returns first element
        """
    def ChangeLast(self) -> IGESGeom_TransformationMatrix: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> IGESGeom_TransformationMatrix: 
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
    def First(self) -> IGESGeom_TransformationMatrix: 
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
    def Init(self,theValue : IGESGeom_TransformationMatrix) -> None: 
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
    def Last(self) -> IGESGeom_TransformationMatrix: 
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
    def Move(self,theOther : IGESGeom_Array1OfTransformationMatrix) -> IGESGeom_Array1OfTransformationMatrix: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : IGESGeom_TransformationMatrix) -> None: 
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
    def Value(self,theIndex : int) -> IGESGeom_TransformationMatrix: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IGESGeom_Array1OfTransformationMatrix) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : IGESGeom_TransformationMatrix) -> None: ...
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
class IGESGeom_Line(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESLine, Type <110> Form <0> in package IGESGeom A line is a bounded, connected portion of a parent straight line which consists of more than one point. A line is defined by its end points.defines IGESLine, Type <110> Form <0> in package IGESGeom A line is a bounded, connected portion of a parent straight line which consists of more than one point. A line is defined by its end points.defines IGESLine, Type <110> Form <0> in package IGESGeom A line is a bounded, connected portion of a parent straight line which consists of more than one point. A line is defined by its end points.
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
    def EndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the end point of the line
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
    def Infinite(self) -> int: 
        """
        Returns the Infinite status i.e. the Form Number : 0 1 2
        """
    def Init(self,aStart : OCP.gp.gp_XYZ,anEnd : OCP.gp.gp_XYZ) -> None: 
        """
        This method is used to set the fields of the class Line - aStart : Start point of the line - anEnd : End point of the line
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
    def SetInfinite(self,status : int) -> None: 
        """
        Sets the Infinite status Does nothing if <status> is not 0 1 or 2
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
    def StartPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the start point of the line
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
    def TransformedEndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the end point of the line after applying Transf. Matrix
        """
    def TransformedStartPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns the start point of the line after applying Transf. Matrix
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
class IGESGeom_OffsetCurve(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESOffsetCurve, Type <130> Form <0> in package IGESGeom An OffsetCurve entity contains the data necessary to determine the offset of a given curve C. This entity points to the base curve to be offset and contains offset distance and other pertinent information.defines IGESOffsetCurve, Type <130> Form <0> in package IGESGeom An OffsetCurve entity contains the data necessary to determine the offset of a given curve C. This entity points to the base curve to be offset and contains offset distance and other pertinent information.defines IGESOffsetCurve, Type <130> Form <0> in package IGESGeom An OffsetCurve entity contains the data necessary to determine the offset of a given curve C. This entity points to the base curve to be offset and contains offset distance and other pertinent information.
    """
    def AddProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Adds a Property in the list
        """
    def ArcLength1(self) -> float: 
        """
        returns arc length or parameter value (depending on value of offset distance flag) of first offset distance (only used if OffsetType() = 2)
        """
    def ArcLength2(self) -> float: 
        """
        returns arc length or parameter value (depending on value of offset distance flag) of second offset distance (only used if OffsetType() = 2)
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
    def BaseCurve(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the curve to be offset
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
    def EndParameter(self) -> float: 
        """
        returns End Parameter value of the offset curve
        """
    def FirstOffsetDistance(self) -> float: 
        """
        returns first offset distance (only used if OffsetType() = 1 or 2)
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def Function(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the function defining the offset if at all the offset is described as a function or Null Handle.
        """
    def FunctionParameter(self) -> int: 
        """
        returns particular coordinate of the curve which describes offset as a function of its parameters. (only used if OffsetType() = 3)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFunction(self) -> bool: 
        """
        returns True if function defining the offset is present.
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
    def Init(self,aBaseCurve : OCP.IGESData.IGESData_IGESEntity,anOffsetType : int,aFunction : OCP.IGESData.IGESData_IGESEntity,aFunctionCoord : int,aTaperedOffsetType : int,offDistance1 : float,arcLength1 : float,offDistance2 : float,arcLength2 : float,aNormalVec : OCP.gp.gp_XYZ,anOffsetParam : float,anotherOffsetParam : float) -> None: 
        """
        This method is used to set the fields of the class OffsetCurve - aBaseCurve : The curve entity to be offset - anOffsetType : Offset distance flag 1 = Single value, uniform distance 2 = Varying linearly 3 = As a specified function - aFunction : Curve entity, one coordinate of which describes offset as a function of its parameter (0 unless OffsetType = 3) - aFunctionCoord : Particular coordinate of curve describing offset as function of its parameters. (used if OffsetType = 3) - aTaperedOffsetType : Tapered offset type flag 1 = Function of arc length 2 = Function of parameter (Only used if OffsetType = 2 or 3) - offDistance1 : First offset distance (Only used if OffsetType = 1 or 2) - arcLength1 : Arc length or parameter value of first offset distance (Only used if OffsetType = 2) - offDistance2 : Second offset distance - arcLength2 : Arc length or parameter value of second offset distance (Only used if OffsetType = 2) - aNormalVec : Unit vector normal to plane containing curve to be offset - anOffsetParam : Start parameter value of offset curve - anotherOffsetParam : End parameter value of offset curve
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
    def NormalVector(self) -> OCP.gp.gp_Vec: 
        """
        returns unit vector normal to plane containing curve to be offset
        """
    def OffsetType(self) -> int: 
        """
        returns the offset distance flag 1 = Single value offset (uniform distance) 2 = Offset distance varying linearly 3 = Offset distance specified as a function
        """
    def Parameters(self) -> Tuple[float, float]: 
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
    def SecondOffsetDistance(self) -> float: 
        """
        returns the second offset distance
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
    def StartParameter(self) -> float: 
        """
        returns Start Parameter value of the offset curve
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
    def TaperedOffsetType(self) -> int: 
        """
        returns tapered offset type flag (only used if OffsetType() = 2 or 3) 1 = Function of arc length 2 = Function of parameter
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TransformedNormalVector(self) -> OCP.gp.gp_Vec: 
        """
        returns unit vector normal to plane containing curve to be offset after applying Transf. Matrix
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
class IGESGeom_OffsetSurface(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESOffsetSurface, Type <140> Form <0> in package IGESGeom An offset surface is a surface defined in terms of an already existing surface.If S(u, v) is a parametrised regular surface and N(u, v) is a differential field of unit normal vectors defined on the whole surface, and "d" a fixed non zero real number, then offset surface to S is a parametrised surface S(u, v) given by O(u, v) = S(u, v) + d * N(u, v); u1 <= u <= u2; v1 <= v <= v2;defines IGESOffsetSurface, Type <140> Form <0> in package IGESGeom An offset surface is a surface defined in terms of an already existing surface.If S(u, v) is a parametrised regular surface and N(u, v) is a differential field of unit normal vectors defined on the whole surface, and "d" a fixed non zero real number, then offset surface to S is a parametrised surface S(u, v) given by O(u, v) = S(u, v) + d * N(u, v); u1 <= u <= u2; v1 <= v <= v2;defines IGESOffsetSurface, Type <140> Form <0> in package IGESGeom An offset surface is a surface defined in terms of an already existing surface.If S(u, v) is a parametrised regular surface and N(u, v) is a differential field of unit normal vectors defined on the whole surface, and "d" a fixed non zero real number, then offset surface to S is a parametrised surface S(u, v) given by O(u, v) = S(u, v) + d * N(u, v); u1 <= u <= u2; v1 <= v <= v2;
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
        returns the distance by which surface is offset
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
    def Init(self,anIndicatoR : OCP.gp.gp_XYZ,aDistance : float,aSurface : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        This method is used to set the fields of the class OffsetSurface - anIndicator : Offset indicator - aDistance : Offset distance - aSurface : Surface that is offset
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
    def OffsetIndicator(self) -> OCP.gp.gp_Vec: 
        """
        returns the offset indicator
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
    def Surface(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the surface that has been offset
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TransformedOffsetIndicator(self) -> OCP.gp.gp_Vec: 
        """
        returns the offset indicator after applying Transf. Matrix
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
class IGESGeom_Plane(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESPlane, Type <108> Form <-1,0,1> in package IGESGeom A plane entity can be used to represent unbounded plane, as well as bounded portion of a plane. In either of the above cases the plane is defined within definition space by means of coefficients A, B, C, D where at least one of A, B, C is non-zero and A * XT + B * YT + C * ZT = Ddefines IGESPlane, Type <108> Form <-1,0,1> in package IGESGeom A plane entity can be used to represent unbounded plane, as well as bounded portion of a plane. In either of the above cases the plane is defined within definition space by means of coefficients A, B, C, D where at least one of A, B, C is non-zero and A * XT + B * YT + C * ZT = Ddefines IGESPlane, Type <108> Form <-1,0,1> in package IGESGeom A plane entity can be used to represent unbounded plane, as well as bounded portion of a plane. In either of the above cases the plane is defined within definition space by means of coefficients A, B, C, D where at least one of A, B, C is non-zero and A * XT + B * YT + C * ZT = D
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
    def BoundingCurve(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns Optional Bounding Curve, can be positive (normal clipping) or negative (hole) according to Form Number
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
    def Equation(self) -> Tuple[float, float, float, float]: 
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
    def HasBoundingCurve(self) -> bool: 
        """
        returns True if there exists a bounding curve
        """
    def HasBoundingCurveHole(self) -> bool: 
        """
        returns True if bounding curve exists and bounded portion is negative
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
    def HasSymbolAttach(self) -> bool: 
        """
        returns True if SymbolSize() > 0, False if SymbolSize() = 0
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
    def Init(self,A : float,B : float,C : float,D : float,aCurve : OCP.IGESData.IGESData_IGESEntity,attach : OCP.gp.gp_XYZ,aSize : float) -> None: 
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
    def RemoveProperty(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Removes a Property from the list
        """
    def SetFormNumber(self,form : int) -> None: 
        """
        Changes FormNumber (indicates the Type of Bound : 0 no Bound, 1 (External) Bound, -1 Hole) Remark that Init keeps this Value and must be consistent : aCurve Null if FormNumber = 0, Non-Null else Error if not in ranges [0-1] or [10-12]
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
    def SymbolAttach(self) -> OCP.gp.gp_Pnt: ...
    def SymbolSize(self) -> float: 
        """
        Size of optional display symbol
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transf(self) -> OCP.IGESData.IGESData_TransfEntity: 
        """
        Returns the Transformation Matrix (under IGES definition) Returns a Null Handle if there is none for a more complete use, see Location & CompoundLocation
        """
    def TransformedEquation(self) -> Tuple[float, float, float, float]: 
        """
        None
        """
    def TransformedSymbolAttach(self) -> OCP.gp.gp_Pnt: ...
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
class IGESGeom_Point(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESPoint, Type <116> Form <0> in package IGESGeomdefines IGESPoint, Type <116> Form <0> in package IGESGeomdefines IGESPoint, Type <116> Form <0> in package IGESGeom
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
    def DisplaySymbol(self) -> OCP.IGESBasic.IGESBasic_SubfigureDef: 
        """
        returns display symbol entity if it exists
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
    def HasDisplaySymbol(self) -> bool: 
        """
        returns True if symbol exists
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
    def Init(self,aPoint : OCP.gp.gp_XYZ,aSymbol : OCP.IGESBasic.IGESBasic_SubfigureDef) -> None: 
        """
        This method is used to set the fields of the class Point - aPoint : Coordinates of point - aSymbol : SubfigureDefinition entity specifying the display symbol if there exists one, or zero
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
    def TransformedValue(self) -> OCP.gp.gp_Pnt: 
        """
        returns co-ordinates of the point after applying Transf. Matrix
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
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        returns co-ordinates of the point
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
class IGESGeom_Protocol(OCP.IGESData.IGESData_Protocol, OCP.Interface.Interface_Protocol, OCP.Standard.Standard_Transient):
    """
    Description of Protocol for IGESGeomDescription of Protocol for IGESGeomDescription of Protocol for IGESGeom
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
class IGESGeom_ReadWriteModule(OCP.IGESData.IGESData_ReadWriteModule, OCP.Interface.Interface_ReaderModule, OCP.Standard.Standard_Transient):
    """
    Defines Geom File Access Module for IGESGeom (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.Defines Geom File Access Module for IGESGeom (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.Defines Geom File Access Module for IGESGeom (specific parts) Specific actions concern : Read and Write Own Parameters of an IGESEntity.
    """
    def CaseIGES(self,typenum : int,formnum : int) -> int: 
        """
        Defines Case Numbers for Entities of IGESGeom
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
        Reads own parameters from file for an Entity of IGESGeom
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
class IGESGeom_RuledSurface(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESRuledSurface, Type <118> Form <0-1> in package IGESGeom A ruled surface is formed by moving a line connecting points of equal relative arc length or equal relative parametric value on two parametric curves from a start point to a terminate point on the curves. The parametric curves may be points, lines, circles, conics, rational B-splines, parametric splines or any parametric curve defined in the IGES specification.defines IGESRuledSurface, Type <118> Form <0-1> in package IGESGeom A ruled surface is formed by moving a line connecting points of equal relative arc length or equal relative parametric value on two parametric curves from a start point to a terminate point on the curves. The parametric curves may be points, lines, circles, conics, rational B-splines, parametric splines or any parametric curve defined in the IGES specification.defines IGESRuledSurface, Type <118> Form <0-1> in package IGESGeom A ruled surface is formed by moving a line connecting points of equal relative arc length or equal relative parametric value on two parametric curves from a start point to a terminate point on the curves. The parametric curves may be points, lines, circles, conics, rational B-splines, parametric splines or any parametric curve defined in the IGES specification.
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
    def DirectionFlag(self) -> int: 
        """
        return the sense of direction 0 = Join first to first, last to last 1 = Join first to last, last to first
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
        returns the first curve
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
    def Init(self,aCurve : OCP.IGESData.IGESData_IGESEntity,anotherCurve : OCP.IGESData.IGESData_IGESEntity,aDirFlag : int,aDevFlag : int) -> None: 
        """
        This method is used to set the fields of the class RuledSurface - aCurve : First parametric curve - anotherCurve : Second parametric curve - aDirFlag : Direction Flag 0 = Join first to first, last to last 1 = Join first to last, last to first - aDevFlag : Developable Surface Flag 1 = Developable 0 = Possibly not
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
    def IsDevelopable(self) -> bool: 
        """
        returns True if developable else False
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
    def IsRuledByParameter(self) -> bool: 
        """
        Returns True if Form is 1
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
    def SecondCurve(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the second curve
        """
    def SetLabel(self,label : OCP.TCollection.TCollection_HAsciiString,sub : int=-1) -> None: 
        """
        Sets a new Label to an IGES Entity If is given, it sets value of SubScriptNumber else, SubScriptNumber is erased
        """
    def SetLineWeight(self,defw : float,maxw : float,gradw : int) -> None: 
        """
        computes and sets "true" line weight according IGES rules from global data MaxLineWeight (maxv) and LineWeightGrad (gradw), or sets it to defw (Default) if LineWeightNumber is null
        """
    def SetRuledByParameter(self,mode : bool) -> None: 
        """
        Sets <me> to be Ruled by Parameter (Form 1) if <mode> is True, or Ruled by Length (Form 0) else
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
class IGESGeom_SpecificModule(OCP.IGESData.IGESData_SpecificModule, OCP.Standard.Standard_Transient):
    """
    Defines Services attached to IGES Entities : Dump & OwnCorrect, for IGESGeomDefines Services attached to IGES Entities : Dump & OwnCorrect, for IGESGeomDefines Services attached to IGES Entities : Dump & OwnCorrect, for IGESGeom
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
        Performs non-ambiguous Correction on Entities which support them (Boundary,ConicArc,Flash,OffsetCurve,TransformationMatrix)
        """
    def OwnDump(self,CN : int,ent : OCP.IGESData.IGESData_IGESEntity,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Specific Dump (own parameters) for IGESGeom
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
class IGESGeom_SplineCurve(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    Defines IGESSplineCurve, Type <112> Form <0> in package IGESGeom The parametric spline is a sequence of parametric polynomial segments. The curve could be of the type Linear, Quadratic, Cubic, Wilson-Fowler, Modified Wilson-Fowler, B-Spline. The N polynomial segments are delimited by the break points T(1), T(2), T(3), ..., T(N+1).Defines IGESSplineCurve, Type <112> Form <0> in package IGESGeom The parametric spline is a sequence of parametric polynomial segments. The curve could be of the type Linear, Quadratic, Cubic, Wilson-Fowler, Modified Wilson-Fowler, B-Spline. The N polynomial segments are delimited by the break points T(1), T(2), T(3), ..., T(N+1).Defines IGESSplineCurve, Type <112> Form <0> in package IGESGeom The parametric spline is a sequence of parametric polynomial segments. The curve could be of the type Linear, Quadratic, Cubic, Wilson-Fowler, Modified Wilson-Fowler, B-Spline. The N polynomial segments are delimited by the break points T(1), T(2), T(3), ..., T(N+1).
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
    def BreakPoint(self,Index : int) -> float: 
        """
        returns breakpoint of piecewise polynomial raises exception if Index <= 0 or Index > NbSegments() + 1
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
    def Degree(self) -> int: 
        """
        returns the degree of the curve
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
    def Init(self,aType : int,aDegree : int,nbDimensions : int,allBreakPoints : OCP.TColStd.TColStd_HArray1OfReal,allXPolynomials : OCP.TColStd.TColStd_HArray2OfReal,allYPolynomials : OCP.TColStd.TColStd_HArray2OfReal,allZPolynomials : OCP.TColStd.TColStd_HArray2OfReal,allXvalues : OCP.TColStd.TColStd_HArray1OfReal,allYvalues : OCP.TColStd.TColStd_HArray1OfReal,allZvalues : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        This method is used to set the fields of the class SplineCurve - aType : Spline Type 1 = Linear 2 = Quadratic 3 = Cubic 4 = Wilson-Fowler 5 = Modified Wilson-Fowler 6 = B Spline - aDegree : Degree of continuity w.r.t. arc length - nbDimensions : Number of dimensions 2 = Planar 3 = Non-planar - allBreakPoints : Array of break points - allXPolynomials : X coordinate polynomials of segments - allYPolynomials : Y coordinate polynomials of segments - allZPolynomials : Z coordinate polynomials of segments - allXValues : Values of 1st, 2nd, 3rd derivatives of X polynomials at the terminate point and values of X at terminate point - allYValues : Values of 1st, 2nd, 3rd derivatives of Y polynomials at the terminate point and values of Y at terminate point - allZvalues : Values of 1st, 2nd, 3rd derivatives of Z polynomials at the terminate point and values of Z at terminate point raises exception if allXPolynomials, allYPolynomials & allZPolynomials are not of same size OR allXValues, allYValues & allZValues are not of size 4
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
    def NbDimensions(self) -> int: 
        """
        returns the number of dimensions 2 = Planar 3 = Non-planar
        """
    def NbProperties(self) -> int: 
        """
        Gives number of recorded properties (0 no list defined)
        """
    def NbSegments(self) -> int: 
        """
        returns the number of segments
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
    def SplineType(self) -> int: 
        """
        returns the type of Spline curve
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
    def XCoordPolynomial(self,Index : int) -> Tuple[float, float, float, float]: 
        """
        returns X coordinate polynomial for segment referred to by Index raises exception if Index <= 0 or Index > NbSegments()
        """
    def XValues(self) -> Tuple[float, float, float, float]: 
        """
        returns the value of X polynomial, the values of 1st, 2nd and 3rd derivatives of the X polynomial at the terminate point
        """
    def YCoordPolynomial(self,Index : int) -> Tuple[float, float, float, float]: 
        """
        returns Y coordinate polynomial for segment referred to by Index raises exception if Index <= 0 or Index > NbSegments()
        """
    def YValues(self) -> Tuple[float, float, float, float]: 
        """
        returns the value of Y polynomial, the values of 1st, 2nd and 3rd derivatives of the Y polynomial at the termminate point
        """
    def ZCoordPolynomial(self,Index : int) -> Tuple[float, float, float, float]: 
        """
        returns Z coordinate polynomial for segment referred to by Index raises exception if Index <= 0 or Index > NbSegments()
        """
    def ZValues(self) -> Tuple[float, float, float, float]: 
        """
        returns the value of Z polynomial, the values of 1st, 2nd and 3rd derivatives of the Z polynomial at the termminate point
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
class IGESGeom_SplineSurface(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESSplineSurface, Type <114> Form <0> in package IGESGeom A parametric spline surface is a grid of polynomial patches. Patch could be of the type Linear, Quadratic, Cubic, Wilson-Fowler, Modified Wilson-Fowler, B-Spline The M * N grid of patches is defined by the 'u' break points TU(1), TU(2), ..., TU(M+1) and the 'v' break points TV(1), TV(2), TV(3) ..., TV(N+1).defines IGESSplineSurface, Type <114> Form <0> in package IGESGeom A parametric spline surface is a grid of polynomial patches. Patch could be of the type Linear, Quadratic, Cubic, Wilson-Fowler, Modified Wilson-Fowler, B-Spline The M * N grid of patches is defined by the 'u' break points TU(1), TU(2), ..., TU(M+1) and the 'v' break points TV(1), TV(2), TV(3) ..., TV(N+1).defines IGESSplineSurface, Type <114> Form <0> in package IGESGeom A parametric spline surface is a grid of polynomial patches. Patch could be of the type Linear, Quadratic, Cubic, Wilson-Fowler, Modified Wilson-Fowler, B-Spline The M * N grid of patches is defined by the 'u' break points TU(1), TU(2), ..., TU(M+1) and the 'v' break points TV(1), TV(2), TV(3) ..., TV(N+1).
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
    def BoundaryType(self) -> int: 
        """
        returns boundary type
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
    def Init(self,aBoundaryType : int,aPatchType : int,allUBreakpoints : OCP.TColStd.TColStd_HArray1OfReal,allVBreakpoints : OCP.TColStd.TColStd_HArray1OfReal,allXCoeffs : OCP.IGESBasic.IGESBasic_HArray2OfHArray1OfReal,allYCoeffs : OCP.IGESBasic.IGESBasic_HArray2OfHArray1OfReal,allZCoeffs : OCP.IGESBasic.IGESBasic_HArray2OfHArray1OfReal) -> None: 
        """
        This method is used to set the fields of the class SplineSurface - aBoundaryType : Type of Spline boundary 1 = Linear 2 = Quadratic 3 = Cubic 4 = Wilson-Fowler 5 = Modified Wilson-Fowler 6 = B-spline - aPatchType : Type of patch contained in the grid 1 = Cartesian Product 0 = Unspecified - allUBreakpoints : u values of grid lines - allVBreakpoints : v values of grid lines - allXCoeffs : X coefficients of M x N patches - allYCoeffs : Y coefficients of M x N patches - allZCoeffs : Z coefficients of M x N patches raises exception if allXCoeffs, allYCoeffs & allZCoeffs are not of the same size. or if the size of each element of the double array is not 16
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
    def NbUSegments(self) -> int: 
        """
        returns the number of U segments
        """
    def NbVSegments(self) -> int: 
        """
        returns the number of V segments
        """
    def PatchType(self) -> int: 
        """
        returns patch type
        """
    def Polynomials(self,XCoef : OCP.IGESBasic.IGESBasic_HArray2OfHArray1OfReal,YCoef : OCP.IGESBasic.IGESBasic_HArray2OfHArray1OfReal,ZCoef : OCP.IGESBasic.IGESBasic_HArray2OfHArray1OfReal) -> Any: 
        """
        returns in one all the polynomial values "in bulk" usefull for massive treatements
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
    def UBreakPoint(self,anIndex : int) -> float: 
        """
        returns U break point of the grid line referred to by anIndex raises exception if anIndex <= 0 or anIndex > NbUSegments() + 1
        """
    def UniqueParent(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the Unique Parent (in the sense given by HasOneParent) Error if there is none or several
        """
    def UseFlag(self) -> int: 
        """
        gives Entity's Use Flag (0 to 5)
        """
    def VBreakPoint(self,anIndex : int) -> float: 
        """
        returns V break point of the grid line referred to by anIndex raises exception if anIndex <= 0 or anIndex > NbVSegments() + 1
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
    def XPolynomial(self,anIndex1 : int,anIndex2 : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns X polynomial of patch referred to by anIndex1, anIndex2 raises exception if anIndex1 <= 0 or anIndex1 > NbUSegments() or anIndex2 <= 0 or anIndex2 > NbVSegments()
        """
    def YPolynomial(self,anIndex1 : int,anIndex2 : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns Y polynomial of patch referred to by anIndex1, anIndex2 raises exception if anIndex1 <= 0 or anIndex1 > NbUSegments() or anIndex2 <= 0 or anIndex2 > NbVSegments()
        """
    def ZPolynomial(self,anIndex1 : int,anIndex2 : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns Z polynomial of patch referred to by anIndex1, anIndex2 raises exception if anIndex1 <= 0 or anIndex1 > NbUSegments() or anIndex2 <= 0 or anIndex2 > NbVSegments()
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
class IGESGeom_SurfaceOfRevolution(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESSurfaceOfRevolution, Type <120> Form <0> in package IGESGeom A surface of revolution is defined by an axis of rotation a generatrix, and start and terminate rotation angles. The surface is created by rotating the generatrix about the axis of rotation through the start and terminate rotation angles.defines IGESSurfaceOfRevolution, Type <120> Form <0> in package IGESGeom A surface of revolution is defined by an axis of rotation a generatrix, and start and terminate rotation angles. The surface is created by rotating the generatrix about the axis of rotation through the start and terminate rotation angles.defines IGESSurfaceOfRevolution, Type <120> Form <0> in package IGESGeom A surface of revolution is defined by an axis of rotation a generatrix, and start and terminate rotation angles. The surface is created by rotating the generatrix about the axis of rotation through the start and terminate rotation angles.
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
    def AxisOfRevolution(self) -> IGESGeom_Line: 
        """
        returns the axis of revolution
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
    def EndAngle(self) -> float: 
        """
        returns end angle of revolution
        """
    def FormNumber(self) -> int: 
        """
        Returns the form number for that type of an IGES entity. The default form number is 0.
        """
    def Generatrix(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the curve which is revolved about the axis
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
    def Init(self,anAxis : IGESGeom_Line,aGeneratrix : OCP.IGESData.IGESData_IGESEntity,aStartAngle : float,anEndAngle : float) -> None: 
        """
        This method is used to set the fields of the class Line - anAxis : Axis of revolution - aGeneratrix : The curve which is revolved about the axis - aStartAngle : Start angle of the surface of revolution - anEndAngle : End angle of the surface of revolution
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
        returns start angle of revolution
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
class IGESGeom_TabulatedCylinder(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESTabulatedCylinder, Type <122> Form <0> in package IGESGeom A tabulated cylinder is a surface formed by moving a line segment called generatrix parallel to itself along a curve called directrix. The curve may be a line, circular arc, conic arc, parametric spline curve, rational B-spline curve or composite curve.defines IGESTabulatedCylinder, Type <122> Form <0> in package IGESGeom A tabulated cylinder is a surface formed by moving a line segment called generatrix parallel to itself along a curve called directrix. The curve may be a line, circular arc, conic arc, parametric spline curve, rational B-spline curve or composite curve.defines IGESTabulatedCylinder, Type <122> Form <0> in package IGESGeom A tabulated cylinder is a surface formed by moving a line segment called generatrix parallel to itself along a curve called directrix. The curve may be a line, circular arc, conic arc, parametric spline curve, rational B-spline curve or composite curve.
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
    def Directrix(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the directrix curve of the tabulated cylinder
        """
    def Dissociate(self,ent : OCP.IGESData.IGESData_IGESEntity) -> None: 
        """
        Resets "me" from the Associativity list of another Entity
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns end point of generatrix of the tabulated cylinder
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
    def Init(self,aDirectrix : OCP.IGESData.IGESData_IGESEntity,anEnd : OCP.gp.gp_XYZ) -> None: 
        """
        This method is used to set the fields of the class TabulatedCylinder - aDirectrix : Directrix Curve of the tabulated cylinder - anEnd : Coordinates of the terminate point of the generatrix The start point of the directrix is identical to the start point of the generatrix
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
    def TransformedEndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        returns end point of generatrix of the tabulated cylinder after applying Transf. Matrix
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
class IGESGeom_ToolBSplineCurve():
    """
    Tool to work on a BSplineCurve. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_BSplineCurve) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_BSplineCurve,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_BSplineCurve,entto : IGESGeom_BSplineCurve,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_BSplineCurve,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_BSplineCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a BSplineCurve <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_BSplineCurve,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_BSplineCurve,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolBSplineSurface():
    """
    Tool to work on a BSplineSurface. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_BSplineSurface) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_BSplineSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_BSplineSurface,entto : IGESGeom_BSplineSurface,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_BSplineSurface,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_BSplineSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a BSplineSurface <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_BSplineSurface,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_BSplineSurface,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolBoundary():
    """
    Tool to work on a Boundary. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_Boundary) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_Boundary,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_Boundary,entto : IGESGeom_Boundary,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGeom_Boundary) -> bool: 
        """
        Sets automatic unambiguous Correction on a Boundary (if BoundaryType = 0, Nullify all ParameterCurves)
        """
    def OwnDump(self,ent : IGESGeom_Boundary,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_Boundary,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Boundary <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_Boundary,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_Boundary,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolBoundedSurface():
    """
    Tool to work on a BoundedSurface. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_BoundedSurface) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_BoundedSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_BoundedSurface,entto : IGESGeom_BoundedSurface,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_BoundedSurface,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_BoundedSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a BoundedSurface <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_BoundedSurface,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_BoundedSurface,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolCircularArc():
    """
    Tool to work on a CircularArc. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_CircularArc) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_CircularArc,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_CircularArc,entto : IGESGeom_CircularArc,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_CircularArc,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_CircularArc,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a CircularArc <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_CircularArc,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_CircularArc,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolCompositeCurve():
    """
    Tool to work on a CompositeCurve. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_CompositeCurve) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_CompositeCurve,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_CompositeCurve,entto : IGESGeom_CompositeCurve,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_CompositeCurve,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_CompositeCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a CompositeCurve <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_CompositeCurve,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_CompositeCurve,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolConicArc():
    """
    Tool to work on a ConicArc. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_ConicArc) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_ConicArc,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_ConicArc,entto : IGESGeom_ConicArc,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGeom_ConicArc) -> bool: 
        """
        Sets automatic unambiguous Correction on a ConicArc (FormNumber recomputed according case Ellips-Parab-Hyperb)
        """
    def OwnDump(self,ent : IGESGeom_ConicArc,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_ConicArc,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a ConicArc <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_ConicArc,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_ConicArc,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolCopiousData():
    """
    Tool to work on a CopiousData. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_CopiousData) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_CopiousData,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_CopiousData,entto : IGESGeom_CopiousData,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_CopiousData,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_CopiousData,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a CopiousData <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_CopiousData,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_CopiousData,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolCurveOnSurface():
    """
    Tool to work on a CurveOnSurface. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_CurveOnSurface) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_CurveOnSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_CurveOnSurface,entto : IGESGeom_CurveOnSurface,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGeom_CurveOnSurface) -> bool: 
        """
        Sets automatic unambiguous Correction on a CurveOnSurface (its CurveUV must have UseFlag at 5)
        """
    def OwnDump(self,ent : IGESGeom_CurveOnSurface,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_CurveOnSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a CurveOnSurface <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_CurveOnSurface,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_CurveOnSurface,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolDirection():
    """
    Tool to work on a Direction. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_Direction) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_Direction,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_Direction,entto : IGESGeom_Direction,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_Direction,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_Direction,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Direction <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_Direction,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_Direction,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolFlash():
    """
    Tool to work on a Flash. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_Flash) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_Flash,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_Flash,entto : IGESGeom_Flash,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGeom_Flash) -> bool: 
        """
        Sets automatic unambiguous Correction on a Flash (LineFont in Directory Entry forced to Rank = 1)
        """
    def OwnDump(self,ent : IGESGeom_Flash,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_Flash,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Flash <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_Flash,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_Flash,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolLine():
    """
    Tool to work on a Line. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_Line) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_Line,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_Line,entto : IGESGeom_Line,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_Line,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_Line,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Line <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_Line,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_Line,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolOffsetCurve():
    """
    Tool to work on a OffsetCurve. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_OffsetCurve) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_OffsetCurve,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_OffsetCurve,entto : IGESGeom_OffsetCurve,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGeom_OffsetCurve) -> bool: 
        """
        Sets automatic unambiguous Correction on a OffsetCurve (if OffsetType is not 3, OffsetFunction is cleared)
        """
    def OwnDump(self,ent : IGESGeom_OffsetCurve,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_OffsetCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a OffsetCurve <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_OffsetCurve,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_OffsetCurve,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolOffsetSurface():
    """
    Tool to work on a OffsetSurface. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_OffsetSurface) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_OffsetSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_OffsetSurface,entto : IGESGeom_OffsetSurface,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_OffsetSurface,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_OffsetSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a OffsetSurface <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_OffsetSurface,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_OffsetSurface,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolPlane():
    """
    Tool to work on a Plane. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_Plane) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_Plane,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_Plane,entto : IGESGeom_Plane,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_Plane,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_Plane,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Plane <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_Plane,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_Plane,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolPoint():
    """
    Tool to work on a Point. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_Point) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_Point,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_Point,entto : IGESGeom_Point,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_Point,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_Point,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a Point <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_Point,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_Point,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolRuledSurface():
    """
    Tool to work on a RuledSurface. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_RuledSurface) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_RuledSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_RuledSurface,entto : IGESGeom_RuledSurface,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_RuledSurface,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_RuledSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a RuledSurface <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_RuledSurface,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_RuledSurface,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolSplineCurve():
    """
    Tool to work on a SplineCurve. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_SplineCurve) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_SplineCurve,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_SplineCurve,entto : IGESGeom_SplineCurve,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_SplineCurve,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_SplineCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a SplineCurve <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_SplineCurve,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_SplineCurve,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolSplineSurface():
    """
    Tool to work on a SplineSurface. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_SplineSurface) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_SplineSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_SplineSurface,entto : IGESGeom_SplineSurface,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_SplineSurface,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_SplineSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a SplineSurface <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_SplineSurface,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_SplineSurface,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolSurfaceOfRevolution():
    """
    Tool to work on a SurfaceOfRevolution. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_SurfaceOfRevolution) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_SurfaceOfRevolution,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_SurfaceOfRevolution,entto : IGESGeom_SurfaceOfRevolution,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_SurfaceOfRevolution,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_SurfaceOfRevolution,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a SurfaceOfRevolution <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_SurfaceOfRevolution,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_SurfaceOfRevolution,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolTabulatedCylinder():
    """
    Tool to work on a TabulatedCylinder. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_TabulatedCylinder) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_TabulatedCylinder,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_TabulatedCylinder,entto : IGESGeom_TabulatedCylinder,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_TabulatedCylinder,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_TabulatedCylinder,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a TabulatedCylinder <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_TabulatedCylinder,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_TabulatedCylinder,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolTransformationMatrix():
    """
    Tool to work on a TransformationMatrix. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_TransformationMatrix) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_TransformationMatrix,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_TransformationMatrix,entto : IGESGeom_TransformationMatrix,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnCorrect(self,ent : IGESGeom_TransformationMatrix) -> bool: 
        """
        Sets automatic unambiguous Correction on a TransformationMatrix (FormNumber if 0 or 1, recomputed according Positive/Negative)
        """
    def OwnDump(self,ent : IGESGeom_TransformationMatrix,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_TransformationMatrix,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a TransformationMatrix <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_TransformationMatrix,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_TransformationMatrix,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_ToolTrimmedSurface():
    """
    Tool to work on a TrimmedSurface. Called by various Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """
    def DirChecker(self,ent : IGESGeom_TrimmedSurface) -> OCP.IGESData.IGESData_DirChecker: 
        """
        Returns specific DirChecker
        """
    def OwnCheck(self,ent : IGESGeom_TrimmedSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        Performs Specific Semantic Check
        """
    def OwnCopy(self,entfrom : IGESGeom_TrimmedSurface,entto : IGESGeom_TrimmedSurface,TC : OCP.Interface.Interface_CopyTool) -> None: 
        """
        Copies Specific Parameters
        """
    def OwnDump(self,ent : IGESGeom_TrimmedSurface,dumper : OCP.IGESData.IGESData_IGESDumper,S : OCP.Message.Message_Messenger,own : int) -> None: 
        """
        Dump of Specific Parameters
        """
    def OwnShared(self,ent : IGESGeom_TrimmedSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Lists the Entities shared by a TrimmedSurface <ent>, from its specific (own) parameters
        """
    def ReadOwnParams(self,ent : IGESGeom_TrimmedSurface,IR : OCP.IGESData.IGESData_IGESReaderData,PR : OCP.IGESData.IGESData_ParamReader) -> None: 
        """
        Reads own parameters from file. <PR> gives access to them, <IR> detains parameter types and values
        """
    def WriteOwnParams(self,ent : IGESGeom_TrimmedSurface,IW : OCP.IGESData.IGESData_IGESWriter) -> None: 
        """
        Writes own parameters to IGESWriter
        """
    def __init__(self) -> None: ...
    pass
class IGESGeom_TransformationMatrix(OCP.IGESData.IGESData_TransfEntity, OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESTransformationMatrix, Type <124> Form <0> in package IGESGeom The transformation matrix entity transforms three-row column vectors by means of matrix multiplication and then a vector addition. This entity can be considered as an "operator" entity in that it starts with the input vector, operates on it as described above, and produces the output vector.defines IGESTransformationMatrix, Type <124> Form <0> in package IGESGeom The transformation matrix entity transforms three-row column vectors by means of matrix multiplication and then a vector addition. This entity can be considered as an "operator" entity in that it starts with the input vector, operates on it as described above, and produces the output vector.defines IGESTransformationMatrix, Type <124> Form <0> in package IGESGeom The transformation matrix entity transforms three-row column vectors by means of matrix multiplication and then a vector addition. This entity can be considered as an "operator" entity in that it starts with the input vector, operates on it as described above, and produces the output vector.
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
    def Data(self,I : int,J : int) -> float: 
        """
        returns individual Data Errro if I not in [1-3] or J not in [1-4]
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
    def Init(self,aMatrix : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        This method is used to set the fields of the class TransformationMatrix - aMatrix : 3 x 4 array containing elements of the transformation matrix raises exception if aMatrix is not 3 x 4 array
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
        Changes FormNumber (indicates the Type of Transf : Transformation 0-1 or Coordinate System 10-11-12) Error if not in ranges [0-1] or [10-12]
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
    def Value(self) -> OCP.gp.gp_GTrsf: 
        """
        returns the transformation matrix 4th row elements of GTrsf will always be 0, 0, 0, 1 (not defined)
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
class IGESGeom_TrimmedSurface(OCP.IGESData.IGESData_IGESEntity, OCP.Standard.Standard_Transient):
    """
    defines IGESTrimmedSurface, Type <144> Form <0> in package IGESGeom A simple closed curve in Euclidean plane divides the plane in to two disjoint, open connected components; one bounded, one unbounded. The bounded one is called the interior region to the curve. Unbounded component is called exterior region to the curve. The domain of the trimmed surface is defined as the interior of the outer boundaries and exterior of the inner boundaries and includes the boundary curves.defines IGESTrimmedSurface, Type <144> Form <0> in package IGESGeom A simple closed curve in Euclidean plane divides the plane in to two disjoint, open connected components; one bounded, one unbounded. The bounded one is called the interior region to the curve. Unbounded component is called exterior region to the curve. The domain of the trimmed surface is defined as the interior of the outer boundaries and exterior of the inner boundaries and includes the boundary curves.defines IGESTrimmedSurface, Type <144> Form <0> in package IGESGeom A simple closed curve in Euclidean plane divides the plane in to two disjoint, open connected components; one bounded, one unbounded. The bounded one is called the interior region to the curve. Unbounded component is called exterior region to the curve. The domain of the trimmed surface is defined as the interior of the outer boundaries and exterior of the inner boundaries and includes the boundary curves.
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
    def HasOuterContour(self) -> bool: 
        """
        returns True if outer contour exists
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
    def Init(self,aSurface : OCP.IGESData.IGESData_IGESEntity,aFlag : int,anOuter : IGESGeom_CurveOnSurface,allInners : IGESGeom_HArray1OfCurveOnSurface) -> None: 
        """
        This method is used to set the fields of the class TrimmedSurface - aSurface : Surface to be trimmed - aFlag : Outer boundary type False = The outer boundary is the boundary of rectangle D which is the domain of the surface to be trimmed True = otherwise - anOuter : Closed curve which constitutes outer boundary - allInners : Array of closed curves which constitute the inner boundary
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
    def InnerContour(self,Index : int) -> IGESGeom_CurveOnSurface: 
        """
        returns the Index'th inner contour raises exception if Index <= 0 or Index > NbInnerContours()
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
    def NbInnerContours(self) -> int: 
        """
        returns the number of inner boundaries
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
    def OuterBoundaryType(self) -> int: 
        """
        returns the outer contour type of the trimmed surface 0 : The outer boundary is the boundary of D 1 : otherwise
        """
    def OuterContour(self) -> IGESGeom_CurveOnSurface: 
        """
        returns the outer contour of the trimmed surface
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
    def Surface(self) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        returns the surface to be trimmed
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
