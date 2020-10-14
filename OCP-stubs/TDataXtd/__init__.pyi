import OCP.TDataXtd
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.Poly
import OCP.Quantity
import OCP.TShort
import OCP.Standard
import OCP.TopoDS
import OCP.TNaming
import OCP.TDataStd
import OCP.gp
__all__  = [
"TDataXtd",
"TDataXtd_Array1OfTrsf",
"TDataXtd_Axis",
"TDataXtd_Constraint",
"TDataXtd_ConstraintEnum",
"TDataXtd_Geometry",
"TDataXtd_GeometryEnum",
"TDataXtd_HArray1OfTrsf",
"TDataXtd_Pattern",
"TDataXtd_PatternStd",
"TDataXtd_Placement",
"TDataXtd_Plane",
"TDataXtd_Point",
"TDataXtd_Position",
"TDataXtd_Presentation",
"TDataXtd_Shape",
"TDataXtd_Triangulation",
"TDataXtd_ALIGN_AXES",
"TDataXtd_ALIGN_FACES",
"TDataXtd_ANGLE",
"TDataXtd_ANY_GEOM",
"TDataXtd_AXES_ANGLE",
"TDataXtd_AXIS",
"TDataXtd_CIRCLE",
"TDataXtd_COINCIDENT",
"TDataXtd_CONCENTRIC",
"TDataXtd_CYLINDER",
"TDataXtd_DIAMETER",
"TDataXtd_DISTANCE",
"TDataXtd_ELLIPSE",
"TDataXtd_EQUAL_DISTANCE",
"TDataXtd_EQUAL_RADIUS",
"TDataXtd_FACES_ANGLE",
"TDataXtd_FIX",
"TDataXtd_FROM",
"TDataXtd_LINE",
"TDataXtd_MAJOR_RADIUS",
"TDataXtd_MATE",
"TDataXtd_MIDPOINT",
"TDataXtd_MINOR_RADIUS",
"TDataXtd_OFFSET",
"TDataXtd_PARALLEL",
"TDataXtd_PERPENDICULAR",
"TDataXtd_PLANE",
"TDataXtd_POINT",
"TDataXtd_RADIUS",
"TDataXtd_RIGID",
"TDataXtd_ROUND",
"TDataXtd_SPLINE",
"TDataXtd_SYMMETRY",
"TDataXtd_TANGENT"
]
class TDataXtd():
    """
    This package defines extension of standard attributes for modelling (mainly for work with geometry).
    """
    @staticmethod
    def IDList_s(anIDList : OCP.TDF.TDF_IDList) -> None: 
        """
        Appends to <anIDList> the list of the attributes IDs of this package. CAUTION: <anIDList> is NOT cleared before use. Print of TDataExt enumeration =============================
        """
    @staticmethod
    @overload
    def Print_s(CTR : TDataXtd_ConstraintEnum,S : Any) -> Any: 
        """
        Prints the name of the geometry dimension <GEO> as a String on the Stream <S> and returns <S>.

        Prints the name of the constraint <CTR> as a String on the Stream <S> and returns <S>.
        """
    @staticmethod
    @overload
    def Print_s(GEO : TDataXtd_GeometryEnum,S : Any) -> Any: ...
    def __init__(self) -> None: ...
    pass
class TDataXtd_Array1OfTrsf():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TDataXtd_Array1OfTrsf) -> TDataXtd_Array1OfTrsf: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.gp.gp_Trsf: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.gp.gp_Trsf: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_Trsf: 
        """
        Variable value access
        """
    def First(self) -> OCP.gp.gp_Trsf: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.gp.gp_Trsf) -> None: 
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
    def Last(self) -> OCP.gp.gp_Trsf: 
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
    def Move(self,theOther : TDataXtd_Array1OfTrsf) -> TDataXtd_Array1OfTrsf: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_Trsf) -> None: 
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
    def Value(self,theIndex : int) -> OCP.gp.gp_Trsf: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDataXtd_Array1OfTrsf) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.gp.gp_Trsf,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TDataXtd_Axis(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    The basis to define an axis attribute.The basis to define an axis attribute.The basis to define an axis attribute.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods ============= Returns the GUID for an axis.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,L : OCP.gp.gp_Lin) -> TDataXtd_Axis: 
        """
        Finds or creates an axis attribute defined by the label. In the case of a creation of an axis, a compatible named shape should already be associated with label. Exceptions Standard_NullObject if no compatible named shape is associated with the label.

        Find, or create, an Axis attribute and set <P> as generated in the associated NamedShape. Axis methods ============
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataXtd_Axis: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TDataXtd_Constraint(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    The groundwork to define constraint attributes. The constraint attribute contains the following sorts of data: - Type whether the constraint attribute is a geometric constraint or a dimension - Value the real number value of a numeric constraint such as an angle or a radius - Geometries to identify the geometries underlying the topological attributes which define the constraint (up to 4) - Plane for 2D constraints.The groundwork to define constraint attributes. The constraint attribute contains the following sorts of data: - Type whether the constraint attribute is a geometric constraint or a dimension - Value the real number value of a numeric constraint such as an angle or a radius - Geometries to identify the geometries underlying the topological attributes which define the constraint (up to 4) - Plane for 2D constraints.The groundwork to define constraint attributes. The constraint attribute contains the following sorts of data: - Type whether the constraint attribute is a geometric constraint or a dimension - Value the real number value of a numeric constraint such as an angle or a radius - Geometries to identify the geometries underlying the topological attributes which define the constraint (up to 4) - Plane for 2D constraints.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def ClearGeometries(self) -> None: 
        """
        Removes the geometries involved in the constraint or dimension from the array of topological attributes where they are stored.
        """
    @staticmethod
    def CollectChildConstraints_s(aLabel : OCP.TDF.TDF_Label,TheList : OCP.TDF.TDF_LabelList) -> None: 
        """
        collects constraints on Childs for label <aLabel>
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetGeometry(self,Index : int) -> OCP.TNaming.TNaming_NamedShape: 
        """
        Returns the integer index Index used to access the array of the constraint or stored geometries of a dimension Index has a value between 1 and 4. methods to write constraint fields (use builder) ==================================
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the GUID for constraints.
        """
    def GetPlane(self) -> OCP.TNaming.TNaming_NamedShape: 
        """
        Returns the topological attribute of the plane used for planar - i.e., 2D - constraints. This plane is attached to another label. If the constraint is not planar, in other words, 3D, this function will return a null handle.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetType(self) -> TDataXtd_ConstraintEnum: 
        """
        Returns the type of constraint. This will be an element of the TDataXtd_ConstraintEnum enumeration.
        """
    def GetValue(self) -> OCP.TDataStd.TDataStd_Real: 
        """
        Returns the value of a dimension. This value is a reference to a TDataStd_Real attribute. If the attribute is not a dimension, this value will be 0. Use IsDimension to test this condition.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Inverted(self,status : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Inverted(self) -> bool: ...
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsDimension(self) -> bool: 
        """
        Returns true if this constraint attribute is a dimension, and therefore has a value.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsPlanar(self) -> bool: 
        """
        Returns true if this constraint attribute is two-dimensional.
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NbGeometries(self) -> int: 
        """
        Returns the number of geometry attributes in this constraint attribute. This number will be between 1 and 4.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,DS : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def Reversed(self,status : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Reversed(self) -> bool: ...
    @overload
    def Set(self,type : TDataXtd_ConstraintEnum,G1 : OCP.TNaming.TNaming_NamedShape,G2 : OCP.TNaming.TNaming_NamedShape,G3 : OCP.TNaming.TNaming_NamedShape,G4 : OCP.TNaming.TNaming_NamedShape) -> None: 
        """
        Finds or creates the constraint attribute defined by the topological attribute G1 and the constraint type type.

        Finds or creates the constraint attribute defined by the topological attributes G1 and G2, and by the constraint type type.

        Finds or creates the constraint attribute defined by the topological attributes G1, G2 and G3, and by the constraint type type.

        Finds or creates the constraint attribute defined by the topological attributes G1, G2, G3 and G4, and by the constraint type type. methods to read constraint fields =================================
        """
    @overload
    def Set(self,type : TDataXtd_ConstraintEnum,G1 : OCP.TNaming.TNaming_NamedShape) -> None: ...
    @overload
    def Set(self,type : TDataXtd_ConstraintEnum,G1 : OCP.TNaming.TNaming_NamedShape,G2 : OCP.TNaming.TNaming_NamedShape) -> None: ...
    @overload
    def Set(self,type : TDataXtd_ConstraintEnum,G1 : OCP.TNaming.TNaming_NamedShape,G2 : OCP.TNaming.TNaming_NamedShape,G3 : OCP.TNaming.TNaming_NamedShape) -> None: ...
    def SetGeometry(self,Index : int,G : OCP.TNaming.TNaming_NamedShape) -> None: 
        """
        Finds or creates the underlying geometry of the constraint defined by the topological attribute G and the integer index Index.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetPlane(self,plane : OCP.TNaming.TNaming_NamedShape) -> None: 
        """
        Finds or creates the plane of the 2D constraint attribute, defined by the planar topological attribute plane.
        """
    def SetType(self,CTR : TDataXtd_ConstraintEnum) -> None: 
        """
        Finds or creates the type of constraint CTR.
        """
    def SetValue(self,V : OCP.TDataStd.TDataStd_Real) -> None: 
        """
        Finds or creates the real number value V of the dimension constraint attribute.
        """
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataXtd_Constraint: 
        """
        Finds or creates the 2D constraint attribute defined by the planar topological attribute plane and the label label. Constraint methods ==================
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    @overload
    def Verified(self) -> bool: 
        """
        Returns true if this constraint attribute is valid. By default, true is returned. When the value of a dimension is changed or when a geometry is moved, false is returned until the solver sets it back to true.

        Returns true if this constraint attribute defined by status is valid. By default, true is returned. When the value of a dimension is changed or when a geometry is moved, false is returned until the solver sets it back to true. If status is false, Verified is set to false.
        """
    @overload
    def Verified(self,status : bool) -> None: ...
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
class TDataXtd_ConstraintEnum():
    """
    The terms of this enumeration define the types of available constraint. ==================

    Members:

      TDataXtd_RADIUS

      TDataXtd_DIAMETER

      TDataXtd_MINOR_RADIUS

      TDataXtd_MAJOR_RADIUS

      TDataXtd_TANGENT

      TDataXtd_PARALLEL

      TDataXtd_PERPENDICULAR

      TDataXtd_CONCENTRIC

      TDataXtd_COINCIDENT

      TDataXtd_DISTANCE

      TDataXtd_ANGLE

      TDataXtd_EQUAL_RADIUS

      TDataXtd_SYMMETRY

      TDataXtd_MIDPOINT

      TDataXtd_EQUAL_DISTANCE

      TDataXtd_FIX

      TDataXtd_RIGID

      TDataXtd_FROM

      TDataXtd_AXIS

      TDataXtd_MATE

      TDataXtd_ALIGN_FACES

      TDataXtd_ALIGN_AXES

      TDataXtd_AXES_ANGLE

      TDataXtd_FACES_ANGLE

      TDataXtd_ROUND

      TDataXtd_OFFSET
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
    TDataXtd_ALIGN_AXES: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_ALIGN_AXES
    TDataXtd_ALIGN_FACES: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_ALIGN_FACES
    TDataXtd_ANGLE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_ANGLE
    TDataXtd_AXES_ANGLE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_AXES_ANGLE
    TDataXtd_AXIS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_AXIS
    TDataXtd_COINCIDENT: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_COINCIDENT
    TDataXtd_CONCENTRIC: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_CONCENTRIC
    TDataXtd_DIAMETER: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_DIAMETER
    TDataXtd_DISTANCE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_DISTANCE
    TDataXtd_EQUAL_DISTANCE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_EQUAL_DISTANCE
    TDataXtd_EQUAL_RADIUS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_EQUAL_RADIUS
    TDataXtd_FACES_ANGLE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_FACES_ANGLE
    TDataXtd_FIX: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_FIX
    TDataXtd_FROM: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_FROM
    TDataXtd_MAJOR_RADIUS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_MAJOR_RADIUS
    TDataXtd_MATE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_MATE
    TDataXtd_MIDPOINT: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_MIDPOINT
    TDataXtd_MINOR_RADIUS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_MINOR_RADIUS
    TDataXtd_OFFSET: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_OFFSET
    TDataXtd_PARALLEL: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_PARALLEL
    TDataXtd_PERPENDICULAR: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_PERPENDICULAR
    TDataXtd_RADIUS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_RADIUS
    TDataXtd_RIGID: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_RIGID
    TDataXtd_ROUND: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_ROUND
    TDataXtd_SYMMETRY: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_SYMMETRY
    TDataXtd_TANGENT: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_TANGENT
    __entries: dict # value = {'TDataXtd_RADIUS': (TDataXtd_ConstraintEnum.TDataXtd_RADIUS, None), 'TDataXtd_DIAMETER': (TDataXtd_ConstraintEnum.TDataXtd_DIAMETER, None), 'TDataXtd_MINOR_RADIUS': (TDataXtd_ConstraintEnum.TDataXtd_MINOR_RADIUS, None), 'TDataXtd_MAJOR_RADIUS': (TDataXtd_ConstraintEnum.TDataXtd_MAJOR_RADIUS, None), 'TDataXtd_TANGENT': (TDataXtd_ConstraintEnum.TDataXtd_TANGENT, None), 'TDataXtd_PARALLEL': (TDataXtd_ConstraintEnum.TDataXtd_PARALLEL, None), 'TDataXtd_PERPENDICULAR': (TDataXtd_ConstraintEnum.TDataXtd_PERPENDICULAR, None), 'TDataXtd_CONCENTRIC': (TDataXtd_ConstraintEnum.TDataXtd_CONCENTRIC, None), 'TDataXtd_COINCIDENT': (TDataXtd_ConstraintEnum.TDataXtd_COINCIDENT, None), 'TDataXtd_DISTANCE': (TDataXtd_ConstraintEnum.TDataXtd_DISTANCE, None), 'TDataXtd_ANGLE': (TDataXtd_ConstraintEnum.TDataXtd_ANGLE, None), 'TDataXtd_EQUAL_RADIUS': (TDataXtd_ConstraintEnum.TDataXtd_EQUAL_RADIUS, None), 'TDataXtd_SYMMETRY': (TDataXtd_ConstraintEnum.TDataXtd_SYMMETRY, None), 'TDataXtd_MIDPOINT': (TDataXtd_ConstraintEnum.TDataXtd_MIDPOINT, None), 'TDataXtd_EQUAL_DISTANCE': (TDataXtd_ConstraintEnum.TDataXtd_EQUAL_DISTANCE, None), 'TDataXtd_FIX': (TDataXtd_ConstraintEnum.TDataXtd_FIX, None), 'TDataXtd_RIGID': (TDataXtd_ConstraintEnum.TDataXtd_RIGID, None), 'TDataXtd_FROM': (TDataXtd_ConstraintEnum.TDataXtd_FROM, None), 'TDataXtd_AXIS': (TDataXtd_ConstraintEnum.TDataXtd_AXIS, None), 'TDataXtd_MATE': (TDataXtd_ConstraintEnum.TDataXtd_MATE, None), 'TDataXtd_ALIGN_FACES': (TDataXtd_ConstraintEnum.TDataXtd_ALIGN_FACES, None), 'TDataXtd_ALIGN_AXES': (TDataXtd_ConstraintEnum.TDataXtd_ALIGN_AXES, None), 'TDataXtd_AXES_ANGLE': (TDataXtd_ConstraintEnum.TDataXtd_AXES_ANGLE, None), 'TDataXtd_FACES_ANGLE': (TDataXtd_ConstraintEnum.TDataXtd_FACES_ANGLE, None), 'TDataXtd_ROUND': (TDataXtd_ConstraintEnum.TDataXtd_ROUND, None), 'TDataXtd_OFFSET': (TDataXtd_ConstraintEnum.TDataXtd_OFFSET, None)}
    __members__: dict # value = {'TDataXtd_RADIUS': TDataXtd_ConstraintEnum.TDataXtd_RADIUS, 'TDataXtd_DIAMETER': TDataXtd_ConstraintEnum.TDataXtd_DIAMETER, 'TDataXtd_MINOR_RADIUS': TDataXtd_ConstraintEnum.TDataXtd_MINOR_RADIUS, 'TDataXtd_MAJOR_RADIUS': TDataXtd_ConstraintEnum.TDataXtd_MAJOR_RADIUS, 'TDataXtd_TANGENT': TDataXtd_ConstraintEnum.TDataXtd_TANGENT, 'TDataXtd_PARALLEL': TDataXtd_ConstraintEnum.TDataXtd_PARALLEL, 'TDataXtd_PERPENDICULAR': TDataXtd_ConstraintEnum.TDataXtd_PERPENDICULAR, 'TDataXtd_CONCENTRIC': TDataXtd_ConstraintEnum.TDataXtd_CONCENTRIC, 'TDataXtd_COINCIDENT': TDataXtd_ConstraintEnum.TDataXtd_COINCIDENT, 'TDataXtd_DISTANCE': TDataXtd_ConstraintEnum.TDataXtd_DISTANCE, 'TDataXtd_ANGLE': TDataXtd_ConstraintEnum.TDataXtd_ANGLE, 'TDataXtd_EQUAL_RADIUS': TDataXtd_ConstraintEnum.TDataXtd_EQUAL_RADIUS, 'TDataXtd_SYMMETRY': TDataXtd_ConstraintEnum.TDataXtd_SYMMETRY, 'TDataXtd_MIDPOINT': TDataXtd_ConstraintEnum.TDataXtd_MIDPOINT, 'TDataXtd_EQUAL_DISTANCE': TDataXtd_ConstraintEnum.TDataXtd_EQUAL_DISTANCE, 'TDataXtd_FIX': TDataXtd_ConstraintEnum.TDataXtd_FIX, 'TDataXtd_RIGID': TDataXtd_ConstraintEnum.TDataXtd_RIGID, 'TDataXtd_FROM': TDataXtd_ConstraintEnum.TDataXtd_FROM, 'TDataXtd_AXIS': TDataXtd_ConstraintEnum.TDataXtd_AXIS, 'TDataXtd_MATE': TDataXtd_ConstraintEnum.TDataXtd_MATE, 'TDataXtd_ALIGN_FACES': TDataXtd_ConstraintEnum.TDataXtd_ALIGN_FACES, 'TDataXtd_ALIGN_AXES': TDataXtd_ConstraintEnum.TDataXtd_ALIGN_AXES, 'TDataXtd_AXES_ANGLE': TDataXtd_ConstraintEnum.TDataXtd_AXES_ANGLE, 'TDataXtd_FACES_ANGLE': TDataXtd_ConstraintEnum.TDataXtd_FACES_ANGLE, 'TDataXtd_ROUND': TDataXtd_ConstraintEnum.TDataXtd_ROUND, 'TDataXtd_OFFSET': TDataXtd_ConstraintEnum.TDataXtd_OFFSET}
    pass
class TDataXtd_Geometry(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    This class is used to model construction geometry. The specific geometric construction of the attribute is defined by an element of the enumeration TDataXtd_GeometryEnum. This attribute may also be used to qualify underlying geometry of the associated NamedShape. for Constructuion element by example.This class is used to model construction geometry. The specific geometric construction of the attribute is defined by an element of the enumeration TDataXtd_GeometryEnum. This attribute may also be used to qualify underlying geometry of the associated NamedShape. for Constructuion element by example.This class is used to model construction geometry. The specific geometric construction of the attribute is defined by an element of the enumeration TDataXtd_GeometryEnum. This attribute may also be used to qualify underlying geometry of the associated NamedShape. for Constructuion element by example.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    @staticmethod
    @overload
    def Axis_s(L : OCP.TDF.TDF_Label,G : OCP.gp.gp_Ax1) -> bool: 
        """
        Returns the axis attribute defined by the label L and the axis G.

        Returns the axis attribute defined by the topological attribute S and the axis G.
        """
    @staticmethod
    @overload
    def Axis_s(S : OCP.TNaming.TNaming_NamedShape,G : OCP.gp.gp_Ax1) -> bool: ...
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    @staticmethod
    @overload
    def Circle_s(L : OCP.TDF.TDF_Label,G : OCP.gp.gp_Circ) -> bool: 
        """
        Returns the circle attribute defined by the label L and the circle G.

        Returns the circle attribute defined by the topological attribute S and the circle G.
        """
    @staticmethod
    @overload
    def Circle_s(S : OCP.TNaming.TNaming_NamedShape,G : OCP.gp.gp_Circ) -> bool: ...
    @staticmethod
    @overload
    def Cylinder_s(L : OCP.TDF.TDF_Label,G : OCP.gp.gp_Cylinder) -> bool: 
        """
        Returns the cylinder attribute defined by the label L and the cylinder G.

        Returns the cylinder attribute defined by the topological attribute S and the cylinder G.
        """
    @staticmethod
    @overload
    def Cylinder_s(S : OCP.TNaming.TNaming_NamedShape,G : OCP.gp.gp_Cylinder) -> bool: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    @overload
    def Ellipse_s(S : OCP.TNaming.TNaming_NamedShape,G : OCP.gp.gp_Elips) -> bool: 
        """
        Returns the ellipse attribute defined by the label L and the ellipse G.

        Returns the ellipse attribute defined by the topological attribute S and the ellipse G.
        """
    @staticmethod
    @overload
    def Ellipse_s(L : OCP.TDF.TDF_Label,G : OCP.gp.gp_Elips) -> bool: ...
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the GUID for geometry attributes.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetType(self) -> TDataXtd_GeometryEnum: 
        """
        Returns the type of geometric construction.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    @staticmethod
    @overload
    def Line_s(S : OCP.TNaming.TNaming_NamedShape,G : OCP.gp.gp_Lin) -> bool: 
        """
        Returns the line attribute defined by the label L and the line G.

        Returns the line attribute defined by the topological attribute S and the line G.
        """
    @staticmethod
    @overload
    def Line_s(L : OCP.TDF.TDF_Label,G : OCP.gp.gp_Lin) -> bool: ...
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def Plane_s(S : OCP.TNaming.TNaming_NamedShape,G : OCP.gp.gp_Pln) -> bool: 
        """
        Returns the plane attribute defined by the label L and the plane G.

        Returns the plane attribute defined by the topological attribute S and the plane G.
        """
    @staticmethod
    @overload
    def Plane_s(L : OCP.TDF.TDF_Label,G : OCP.gp.gp_Pln) -> bool: ...
    @staticmethod
    @overload
    def Point_s(S : OCP.TNaming.TNaming_NamedShape,G : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns the point attribute defined by the label L and the point G.

        Returns the point attribute defined by the topological attribute S and the point G.
        """
    @staticmethod
    @overload
    def Point_s(L : OCP.TDF.TDF_Label,G : OCP.gp.gp_Pnt) -> bool: ...
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetType(self,T : TDataXtd_GeometryEnum) -> None: 
        """
        Returns the type of geometric construction T of this attribute. T will be a value of the enumeration TDataXtd_GeometryEnum.
        """
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataXtd_Geometry: 
        """
        API class methods ================= Finds, or creates, a Geometry attribute defined by the label label. The default type of geometry is the value ANY_GEOM of the enumeration TDataXtd_GeometryEnum. To specify another value of this enumeration, use the function SetType.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    @staticmethod
    @overload
    def Type_s(L : OCP.TDF.TDF_Label) -> TDataXtd_GeometryEnum: 
        """
        Returns the label L used to define the type of geometric construction for the geometry attribute.

        Returns the topological attribute S used to define the type of geometric construction for the geometry attribute.
        """
    @staticmethod
    @overload
    def Type_s(S : OCP.TNaming.TNaming_NamedShape) -> TDataXtd_GeometryEnum: ...
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TDataXtd_GeometryEnum():
    """
    The terms of this enumeration define the types of geometric shapes available.

    Members:

      TDataXtd_ANY_GEOM

      TDataXtd_POINT

      TDataXtd_LINE

      TDataXtd_CIRCLE

      TDataXtd_ELLIPSE

      TDataXtd_SPLINE

      TDataXtd_PLANE

      TDataXtd_CYLINDER
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
    TDataXtd_ANY_GEOM: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_ANY_GEOM
    TDataXtd_CIRCLE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_CIRCLE
    TDataXtd_CYLINDER: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_CYLINDER
    TDataXtd_ELLIPSE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_ELLIPSE
    TDataXtd_LINE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_LINE
    TDataXtd_PLANE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_PLANE
    TDataXtd_POINT: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_POINT
    TDataXtd_SPLINE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_SPLINE
    __entries: dict # value = {'TDataXtd_ANY_GEOM': (TDataXtd_GeometryEnum.TDataXtd_ANY_GEOM, None), 'TDataXtd_POINT': (TDataXtd_GeometryEnum.TDataXtd_POINT, None), 'TDataXtd_LINE': (TDataXtd_GeometryEnum.TDataXtd_LINE, None), 'TDataXtd_CIRCLE': (TDataXtd_GeometryEnum.TDataXtd_CIRCLE, None), 'TDataXtd_ELLIPSE': (TDataXtd_GeometryEnum.TDataXtd_ELLIPSE, None), 'TDataXtd_SPLINE': (TDataXtd_GeometryEnum.TDataXtd_SPLINE, None), 'TDataXtd_PLANE': (TDataXtd_GeometryEnum.TDataXtd_PLANE, None), 'TDataXtd_CYLINDER': (TDataXtd_GeometryEnum.TDataXtd_CYLINDER, None)}
    __members__: dict # value = {'TDataXtd_ANY_GEOM': TDataXtd_GeometryEnum.TDataXtd_ANY_GEOM, 'TDataXtd_POINT': TDataXtd_GeometryEnum.TDataXtd_POINT, 'TDataXtd_LINE': TDataXtd_GeometryEnum.TDataXtd_LINE, 'TDataXtd_CIRCLE': TDataXtd_GeometryEnum.TDataXtd_CIRCLE, 'TDataXtd_ELLIPSE': TDataXtd_GeometryEnum.TDataXtd_ELLIPSE, 'TDataXtd_SPLINE': TDataXtd_GeometryEnum.TDataXtd_SPLINE, 'TDataXtd_PLANE': TDataXtd_GeometryEnum.TDataXtd_PLANE, 'TDataXtd_CYLINDER': TDataXtd_GeometryEnum.TDataXtd_CYLINDER}
    pass
class TDataXtd_HArray1OfTrsf(TDataXtd_Array1OfTrsf, OCP.Standard.Standard_Transient):
    def Array1(self) -> TDataXtd_Array1OfTrsf: 
        """
        None
        """
    def Assign(self,theOther : TDataXtd_Array1OfTrsf) -> TDataXtd_Array1OfTrsf: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TDataXtd_Array1OfTrsf: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.gp.gp_Trsf: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.gp.gp_Trsf: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_Trsf: 
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
    def First(self) -> OCP.gp.gp_Trsf: 
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
    def Init(self,theValue : OCP.gp.gp_Trsf) -> None: 
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
    def Last(self) -> OCP.gp.gp_Trsf: 
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
    def Move(self,theOther : TDataXtd_Array1OfTrsf) -> TDataXtd_Array1OfTrsf: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_Trsf) -> None: 
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
    def Value(self,theIndex : int) -> OCP.gp.gp_Trsf: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TDataXtd_Array1OfTrsf) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.gp.gp_Trsf) -> None: ...
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
class TDataXtd_Pattern(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    a general pattern modela general pattern modela general pattern model
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def ComputeTrsfs(self,Trsfs : TDataXtd_Array1OfTrsf) -> None: 
        """
        Give the transformations
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NbTrsfs(self) -> int: 
        """
        Give the number of transformation
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty attribute from the good end type. It is used by the copy algorithm.
        """
    def Paste(self,intoAttribute : OCP.TDF.TDF_Attribute,aRelocationTable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is different from the "Copy" one, because it is used when copying an attribute from a source structure into a target structure. This method may paste the contents of <me> into <intoAttribute>.
        """
    def PatternID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,anAttribute : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the backuped contents from <anAttribute> into this one. It is used when aborting a transaction.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TDataXtd_PatternStd(TDataXtd_Pattern, OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    to create a PatternStd (LinearPattern, CircularPattern, RectangularPattern, RadialCircularPattern, MirrorPattern)to create a PatternStd (LinearPattern, CircularPattern, RectangularPattern, RadialCircularPattern, MirrorPattern)to create a PatternStd (LinearPattern, CircularPattern, RectangularPattern, RadialCircularPattern, MirrorPattern)
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    @overload
    def Axis1(self,Axis1 : OCP.TNaming.TNaming_NamedShape) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Axis1(self) -> OCP.TNaming.TNaming_NamedShape: ...
    @overload
    def Axis1Reversed(self,Axis1Reversed : bool) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Axis1Reversed(self) -> bool: ...
    @overload
    def Axis2(self,Axis2 : OCP.TNaming.TNaming_NamedShape) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Axis2(self) -> OCP.TNaming.TNaming_NamedShape: ...
    @overload
    def Axis2Reversed(self) -> bool: 
        """
        None

        None

        None
        """
    @overload
    def Axis2Reversed(self,Axis2Reversed : bool) -> None: ...
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def ComputeTrsfs(self,Trsfs : TDataXtd_Array1OfTrsf) -> None: 
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
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    def GetPatternID_s() -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    @overload
    def Mirror(self) -> OCP.TNaming.TNaming_NamedShape: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,plane : OCP.TNaming.TNaming_NamedShape) -> None: ...
    @overload
    def NbInstances1(self) -> OCP.TDataStd.TDataStd_Integer: 
        """
        None

        None

        None
        """
    @overload
    def NbInstances1(self,NbInstances1 : OCP.TDataStd.TDataStd_Integer) -> None: ...
    @overload
    def NbInstances2(self,NbInstances2 : OCP.TDataStd.TDataStd_Integer) -> None: 
        """
        None

        None

        None
        """
    @overload
    def NbInstances2(self) -> OCP.TDataStd.TDataStd_Integer: ...
    def NbTrsfs(self) -> int: 
        """
        None
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def PatternID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataXtd_PatternStd: 
        """
        Find, or create, a PatternStd attribute
        """
    @overload
    def Signature(self,signature : int) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Signature(self) -> int: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    @overload
    def Value1(self) -> OCP.TDataStd.TDataStd_Real: 
        """
        None

        None

        None
        """
    @overload
    def Value1(self,value : OCP.TDataStd.TDataStd_Real) -> None: ...
    @overload
    def Value2(self,value : OCP.TDataStd.TDataStd_Real) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Value2(self) -> OCP.TDataStd.TDataStd_Real: ...
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
class TDataXtd_Placement(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods =============
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataXtd_Placement: 
        """
        Find, or create, an Placement attribute. the Placement attribute is returned. Placement methods =================
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TDataXtd_Plane(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    The basis to define a plane attribute. Warning: Use TDataXtd_Geometry attribute to retrieve the gp_Pln of the Plane attributeThe basis to define a plane attribute. Warning: Use TDataXtd_Geometry attribute to retrieve the gp_Pln of the Plane attributeThe basis to define a plane attribute. Warning: Use TDataXtd_Geometry attribute to retrieve the gp_Pln of the Plane attribute
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods =============
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,P : OCP.gp.gp_Pln) -> TDataXtd_Plane: 
        """
        Finds or creates the plane attribute defined by the label label. Warning If you are creating the attribute with this syntax, a planar face should already be associated with label.

        Finds, or creates, a Plane attribute and sets <P> as generated the associated NamedShape. Plane methods =============
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataXtd_Plane: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TDataXtd_Point(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    The basis to define a point attribute. The topological attribute must contain a vertex. You use this class to create reference points in a design.The basis to define a point attribute. The topological attribute must contain a vertex. You use this class to create reference points in a design.The basis to define a point attribute. The topological attribute must contain a vertex. You use this class to create reference points in a design.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods =============
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,With : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label) -> TDataXtd_Point: 
        """
        Sets the label Label as a point attribute. If no object is found, a point attribute is created.

        Sets the label Label as a point attribute containing the point P. If no object is found, a point attribute is created. Point methods =============
        """
    @staticmethod
    @overload
    def Set_s(label : OCP.TDF.TDF_Label,P : OCP.gp.gp_Pnt) -> TDataXtd_Point: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TDataXtd_Position(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Position of a LabelPosition of a LabelPosition of a Label
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
        """
    def GetPosition(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(aLabel : OCP.TDF.TDF_Label,aPos : OCP.gp.gp_Pnt) -> bool: 
        """
        Search label <aLabel) for the TDataXtd_Position attribute and get its position if found returns True
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty attribute from the good end type. It is used by the copy algorithm.
        """
    def Paste(self,intoAttribute : OCP.TDF.TDF_Attribute,aRelocTationable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is different from the "Copy" one, because it is used when copying an attribute from a source structure into a target structure. This method pastes the current attribute to the label corresponding to the insertor. The pasted attribute may be a brand new one or a new version of the previous one.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,anAttribute : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the contents from <anAttribute> into this one. It is used when aborting a transaction.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetPosition(self,aPos : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def Set_s(aLabel : OCP.TDF.TDF_Label) -> TDataXtd_Position: 
        """
        Create if not found the TDataXtd_Position attribute set its position to <aPos>

        Find an existing, or create an empty, Position. the Position attribute is returned.
        """
    @staticmethod
    @overload
    def Set_s(aLabel : OCP.TDF.TDF_Label,aPos : OCP.gp.gp_Pnt) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TDataXtd_Presentation(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    Attribute containing parameters of presentation of the shape, e.g. the shape attached to the same label and displayed using TPrsStd tools (see TPrsStd_AISPresentation).Attribute containing parameters of presentation of the shape, e.g. the shape attached to the same label and displayed using TPrsStd tools (see TPrsStd_AISPresentation).Attribute containing parameters of presentation of the shape, e.g. the shape attached to the same label and displayed using TPrsStd tools (see TPrsStd_AISPresentation).
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AddSelectionMode(self,theSelectionMode : int,theTransaction : bool=True) -> None: 
        """
        None
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Color(self) -> OCP.Quantity.Quantity_NameOfColor: 
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
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetDriverGUID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the GUID of the driver managing display of associated AIS object
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
        """
    def GetNbSelectionModes(self) -> int: 
        """
        Returns the number of selection modes of the attribute. It starts with 1 .. GetNbSelectionModes().
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasOwnColor(self) -> bool: 
        """
        None
        """
    def HasOwnMaterial(self) -> bool: 
        """
        None
        """
    def HasOwnMode(self) -> bool: 
        """
        None
        """
    def HasOwnSelectionMode(self) -> bool: 
        """
        None
        """
    def HasOwnTransparency(self) -> bool: 
        """
        None
        """
    def HasOwnWidth(self) -> bool: 
        """
        None
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the attribute.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsDisplayed(self) -> bool: 
        """
        None
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def MaterialIndex(self) -> int: 
        """
        None
        """
    def Mode(self) -> int: 
        """
        None
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        Returns an new empty attribute from the good end type. It is used by the copy algorithm.
        """
    def Paste(self,intoAttribute : OCP.TDF.TDF_Attribute,aRelocTationable : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        This method is different from the "Copy" one, because it is used when copying an attribute from a source structure into a target structure. This method pastes the current attribute to the label corresponding to the insertor. The pasted attribute may be a brand new one or a new version of the previous one.
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,anAttribute : OCP.TDF.TDF_Attribute) -> None: 
        """
        Restores the contents from <anAttribute> into this one. It is used when aborting a transaction.
        """
    def SelectionMode(self,index : int=1) -> int: 
        """
        None
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_NameOfColor) -> None: 
        """
        None
        """
    def SetDisplayed(self,theIsDisplayed : bool) -> None: 
        """
        None
        """
    def SetDriverGUID(self,theGUID : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets the GUID of the driver managing display of associated AIS object
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetMaterialIndex(self,theMaterialIndex : int) -> None: 
        """
        None
        """
    def SetMode(self,theMode : int) -> None: 
        """
        None
        """
    def SetSelectionMode(self,theSelectionMode : int,theTransaction : bool=True) -> None: 
        """
        Sets selection mode. If "theTransaction" flag is OFF, modification of the attribute doesn't influence the transaction mechanism (the attribute doesn't participate in undo/redo because of this modification). Certainly, if any other data of the attribute is modified (display mode, color, ...), the attribute will be included into undo/redo.
        """
    def SetTransparency(self,theValue : float) -> None: 
        """
        None
        """
    def SetWidth(self,theWidth : float) -> None: 
        """
        None
        """
    @staticmethod
    def Set_s(theLabel : OCP.TDF.TDF_Label,theDriverId : OCP.Standard.Standard_GUID) -> TDataXtd_Presentation: 
        """
        Create if not found the TDataXtd_Presentation attribute and set its driver GUID
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def Transparency(self) -> float: 
        """
        None
        """
    def UnsetColor(self) -> None: 
        """
        None
        """
    def UnsetMaterial(self) -> None: 
        """
        None
        """
    def UnsetMode(self) -> None: 
        """
        None
        """
    def UnsetSelectionMode(self) -> None: 
        """
        None
        """
    def UnsetTransparency(self) -> None: 
        """
        None
        """
    def UnsetWidth(self) -> None: 
        """
        None
        """
    @staticmethod
    def Unset_s(theLabel : OCP.TDF.TDF_Label) -> None: 
        """
        Remove attribute of this type from the label
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def Width(self) -> float: 
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
class TDataXtd_Shape(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    A Shape is associated in the framework with : a NamedShape attributeA Shape is associated in the framework with : a NamedShape attributeA Shape is associated in the framework with : a NamedShape attribute
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    @staticmethod
    def Find_s(current : OCP.TDF.TDF_Label,S : TDataXtd_Shape) -> bool: 
        """
        class methods ============= try to retrieve a Shape attribute at <current> label or in fathers label of <current>. Returns True if found and set <S>.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Shape methods ============
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s(label : OCP.TDF.TDF_Label) -> OCP.TopoDS.TopoDS_Shape: 
        """
        the Shape from associated NamedShape attribute is returned.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    @staticmethod
    def New_s(label : OCP.TDF.TDF_Label) -> TDataXtd_Shape: 
        """
        Find, or create, a Shape attribute. the Shape attribute is returned. Raises if <label> has attribute.
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,DS : OCP.TDF.TDF_DataSet) -> None: 
        """
        None
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    @staticmethod
    def Set_s(label : OCP.TDF.TDF_Label,shape : OCP.TopoDS.TopoDS_Shape) -> TDataXtd_Shape: 
        """
        Create or update associated NamedShape attribute. the Shape attribute is returned.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
class TDataXtd_Triangulation(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    An Ocaf attribute containing a mesh (Poly_Triangulation). It duplicates all methods from Poly_Triangulation. It is highly recommended to modify the mesh through the methods of this attribute, but not directly via the underlying Poly_Triangulation object. In this case Undo/Redo will work fine and robust.An Ocaf attribute containing a mesh (Poly_Triangulation). It duplicates all methods from Poly_Triangulation. It is highly recommended to modify the mesh through the methods of this attribute, but not directly via the underlying Poly_Triangulation object. In this case Undo/Redo will work fine and robust.An Ocaf attribute containing a mesh (Poly_Triangulation). It duplicates all methods from Poly_Triangulation. It is highly recommended to modify the mesh through the methods of this attribute, but not directly via the underlying Poly_Triangulation object. In this case Undo/Redo will work fine and robust.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @overload
    def Deflection(self) -> float: 
        """
        Returns the deflection of this triangulation.

        Sets the deflection of this triangulation to theDeflection. See more on deflection in Polygon2D
        """
    @overload
    def Deflection(self,theDeflection : float) -> None: ...
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : Any) -> Any: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : Any,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mecanisms. Be carefull that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be carefull that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def Get(self) -> OCP.Poly.Poly_Triangulation: 
        """
        Returns the underlying triangulation.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the ID of the triangulation attribute.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasNormals(self) -> bool: 
        """
        Returns Standard_True if nodal normals are defined.
        """
    def HasUVNodes(self) -> bool: 
        """
        Returns Standard_True if 2D nodes are associated with 3D nodes for this triangulation.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        Inherited attribute methods
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NbNodes(self) -> int: 
        """
        Returns the number of nodes for this triangulation.
        """
    def NbTriangles(self) -> int: 
        """
        Returns the number of triangles for this triangulation.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Node(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns node at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def Normal(self,theIndex : int) -> OCP.gp.gp_Dir: 
        """
        Returns normal at the given index. Raises Standard_OutOfRange exception.
        """
    def Paste(self,Into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def RemoveUVNodes(self) -> None: 
        """
        Deallocates the UV nodes.
        """
    def Restore(self,theAttribute : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def Set(self,theTriangulation : OCP.Poly.Poly_Triangulation) -> None: 
        """
        Sets the triangulation.
        """
    @overload
    def SetID(self) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: ...
    def SetNode(self,theIndex : int,theNode : OCP.gp.gp_Pnt) -> None: 
        """
        The method differs from Poly_Triangulation! Sets a node at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def SetNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: 
        """
        Changes normal at the given index. Raises Standard_OutOfRange exception.
        """
    def SetNormals(self,theNormals : OCP.TShort.TShort_HArray1OfShortReal) -> None: 
        """
        Sets the table of node normals. Raises exception if length of theNormals != 3 * NbNodes
        """
    def SetTriangle(self,theIndex : int,theTriangle : OCP.Poly.Poly_Triangle) -> None: 
        """
        The method differs from Poly_Triangulation! Sets a triangle at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbTriangles.
        """
    def SetUVNode(self,theIndex : int,theUVNode : OCP.gp.gp_Pnt2d) -> None: 
        """
        The method differs from Poly_Triangulation! Sets a UVNode at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label) -> TDataXtd_Triangulation: 
        """
        Finds or creates a triangulation attribute.

        Finds or creates a triangulation attribute. Initializes the attribute by a Poly_Triangulation object.
        """
    @staticmethod
    @overload
    def Set_s(theLabel : OCP.TDF.TDF_Label,theTriangulation : OCP.Poly.Poly_Triangulation) -> TDataXtd_Triangulation: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def Triangle(self,theIndex : int) -> OCP.Poly.Poly_Triangle: 
        """
        Returns triangle at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbTriangles.
        """
    def UVNode(self,theIndex : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns UVNode at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
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
TDataXtd_ALIGN_AXES: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_ALIGN_AXES
TDataXtd_ALIGN_FACES: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_ALIGN_FACES
TDataXtd_ANGLE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_ANGLE
TDataXtd_ANY_GEOM: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_ANY_GEOM
TDataXtd_AXES_ANGLE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_AXES_ANGLE
TDataXtd_AXIS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_AXIS
TDataXtd_CIRCLE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_CIRCLE
TDataXtd_COINCIDENT: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_COINCIDENT
TDataXtd_CONCENTRIC: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_CONCENTRIC
TDataXtd_CYLINDER: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_CYLINDER
TDataXtd_DIAMETER: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_DIAMETER
TDataXtd_DISTANCE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_DISTANCE
TDataXtd_ELLIPSE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_ELLIPSE
TDataXtd_EQUAL_DISTANCE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_EQUAL_DISTANCE
TDataXtd_EQUAL_RADIUS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_EQUAL_RADIUS
TDataXtd_FACES_ANGLE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_FACES_ANGLE
TDataXtd_FIX: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_FIX
TDataXtd_FROM: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_FROM
TDataXtd_LINE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_LINE
TDataXtd_MAJOR_RADIUS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_MAJOR_RADIUS
TDataXtd_MATE: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_MATE
TDataXtd_MIDPOINT: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_MIDPOINT
TDataXtd_MINOR_RADIUS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_MINOR_RADIUS
TDataXtd_OFFSET: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_OFFSET
TDataXtd_PARALLEL: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_PARALLEL
TDataXtd_PERPENDICULAR: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_PERPENDICULAR
TDataXtd_PLANE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_PLANE
TDataXtd_POINT: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_POINT
TDataXtd_RADIUS: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_RADIUS
TDataXtd_RIGID: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_RIGID
TDataXtd_ROUND: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_ROUND
TDataXtd_SPLINE: OCP.TDataXtd.TDataXtd_GeometryEnum # value = TDataXtd_GeometryEnum.TDataXtd_SPLINE
TDataXtd_SYMMETRY: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_SYMMETRY
TDataXtd_TANGENT: OCP.TDataXtd.TDataXtd_ConstraintEnum # value = TDataXtd_ConstraintEnum.TDataXtd_TANGENT
