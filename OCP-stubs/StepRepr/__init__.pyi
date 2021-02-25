import OCP.StepRepr
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.NCollection
import OCP.StepBasic
import OCP.StepShape
import OCP.Standard
import OCP.StepData
__all__  = [
"StepRepr_ShapeAspect",
"StepRepr_DerivedShapeAspect",
"StepRepr_Array1OfMaterialPropertyRepresentation",
"StepRepr_Array1OfPropertyDefinitionRepresentation",
"StepRepr_Array1OfRepresentationItem",
"StepRepr_Array1OfShapeAspect",
"StepRepr_ProductDefinitionUsage",
"StepRepr_AssemblyComponentUsageSubstitute",
"StepRepr_CompositeShapeAspect",
"StepRepr_CentreOfSymmetry",
"StepRepr_CharacterizedDefinition",
"StepRepr_Representation",
"StepRepr_CompShAspAndDatumFeatAndShAsp",
"StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp",
"StepRepr_CompositeGroupShapeAspect",
"StepRepr_ContinuosShapeAspect",
"StepRepr_RepresentationItem",
"StepRepr_ConfigurationDesign",
"StepRepr_ConfigurationDesignItem",
"StepRepr_ConfigurationEffectivity",
"StepRepr_ConfigurationItem",
"StepRepr_ConstructiveGeometryRepresentation",
"StepRepr_RepresentationRelationship",
"StepRepr_BetweenShapeAspect",
"StepRepr_DataEnvironment",
"StepRepr_DefinitionalRepresentation",
"StepRepr_Apex",
"StepRepr_DescriptiveRepresentationItem",
"StepRepr_Extension",
"StepRepr_ExternallyDefinedRepresentation",
"StepRepr_ShapeAspectRelationship",
"StepRepr_FunctionallyDefinedTransformation",
"StepRepr_GeometricAlignment",
"StepRepr_RepresentationContext",
"StepRepr_GlobalUnitAssignedContext",
"StepRepr_HArray1OfMaterialPropertyRepresentation",
"StepRepr_HArray1OfPropertyDefinitionRepresentation",
"StepRepr_HArray1OfRepresentationItem",
"StepRepr_HArray1OfShapeAspect",
"StepRepr_SequenceOfMaterialPropertyRepresentation",
"StepRepr_SequenceOfRepresentationItem",
"StepRepr_IntegerRepresentationItem",
"StepRepr_ItemDefinedTransformation",
"StepRepr_MakeFromUsageOption",
"StepRepr_MappedItem",
"StepRepr_MaterialDesignation",
"StepRepr_PropertyDefinition",
"StepRepr_PropertyDefinitionRepresentation",
"StepRepr_MeasureRepresentationItem",
"StepRepr_AssemblyComponentUsage",
"StepRepr_ParallelOffset",
"StepRepr_ParametricRepresentationContext",
"StepRepr_PerpendicularTo",
"StepRepr_ProductConcept",
"StepRepr_ProductDefinitionShape",
"StepRepr_NextAssemblyUsageOccurrence",
"StepRepr_PromissoryUsageOccurrence",
"StepRepr_MaterialProperty",
"StepRepr_PropertyDefinitionRelationship",
"StepRepr_MaterialPropertyRepresentation",
"StepRepr_QuantifiedAssemblyComponentUsage",
"StepRepr_ReprItemAndMeasureWithUnit",
"StepRepr_ReprItemAndMeasureWithUnitAndQRI",
"StepRepr_ReprItemAndLengthMeasureWithUnit",
"StepRepr_ReprItemAndLengthMeasureWithUnitAndQRI",
"StepRepr_ReprItemAndPlaneAngleMeasureWithUnit",
"StepRepr_ReprItemAndPlaneAngleMeasureWithUnitAndQRI",
"StepRepr_CharacterizedRepresentation",
"StepRepr_GlobalUncertaintyAssignedContext",
"StepRepr_CompoundRepresentationItem",
"StepRepr_RepresentationMap",
"StepRepr_ConstructiveGeometryRepresentationRelationship",
"StepRepr_ShapeRepresentationRelationship",
"StepRepr_RepresentedDefinition",
"StepRepr_HSequenceOfMaterialPropertyRepresentation",
"StepRepr_HSequenceOfRepresentationItem",
"StepRepr_AllAroundShapeAspect",
"StepRepr_ShapeAspectDerivingRelationship",
"StepRepr_FeatureForDatumTargetRelationship",
"StepRepr_ShapeAspectTransition",
"StepRepr_ShapeDefinition",
"StepRepr_RepresentationRelationshipWithTransformation",
"StepRepr_ShapeRepresentationRelationshipWithTransformation",
"StepRepr_SpecifiedHigherUsageOccurrence",
"StepRepr_StructuralResponseProperty",
"StepRepr_StructuralResponsePropertyDefinitionRepresentation",
"StepRepr_SuppliedPartRelationship",
"StepRepr_Tangent",
"StepRepr_Transformation",
"StepRepr_ValueRange",
"StepRepr_ValueRepresentationItem"
]
class StepRepr_ShapeAspect(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_DerivedShapeAspect(StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_Array1OfMaterialPropertyRepresentation():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepRepr_Array1OfMaterialPropertyRepresentation) -> StepRepr_Array1OfMaterialPropertyRepresentation: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Variable value access
        """
    def First(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Returns first element
        """
    def Init(self,theValue : StepRepr_MaterialPropertyRepresentation) -> None: 
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
    def Last(self) -> StepRepr_MaterialPropertyRepresentation: 
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
    def Move(self,theOther : StepRepr_Array1OfMaterialPropertyRepresentation) -> StepRepr_Array1OfMaterialPropertyRepresentation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_MaterialPropertyRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepRepr_Array1OfMaterialPropertyRepresentation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepRepr_MaterialPropertyRepresentation,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepRepr_Array1OfPropertyDefinitionRepresentation():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepRepr_Array1OfPropertyDefinitionRepresentation) -> StepRepr_Array1OfPropertyDefinitionRepresentation: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepRepr_PropertyDefinitionRepresentation: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepRepr_PropertyDefinitionRepresentation: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_PropertyDefinitionRepresentation: 
        """
        Variable value access
        """
    def First(self) -> StepRepr_PropertyDefinitionRepresentation: 
        """
        Returns first element
        """
    def Init(self,theValue : StepRepr_PropertyDefinitionRepresentation) -> None: 
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
    def Last(self) -> StepRepr_PropertyDefinitionRepresentation: 
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
    def Move(self,theOther : StepRepr_Array1OfPropertyDefinitionRepresentation) -> StepRepr_Array1OfPropertyDefinitionRepresentation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_PropertyDefinitionRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_PropertyDefinitionRepresentation: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepRepr_Array1OfPropertyDefinitionRepresentation) -> None: ...
    @overload
    def __init__(self,theBegin : StepRepr_PropertyDefinitionRepresentation,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepRepr_Array1OfRepresentationItem():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepRepr_Array1OfRepresentationItem) -> StepRepr_Array1OfRepresentationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepRepr_RepresentationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepRepr_RepresentationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_RepresentationItem: 
        """
        Variable value access
        """
    def First(self) -> StepRepr_RepresentationItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepRepr_RepresentationItem) -> None: 
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
    def Last(self) -> StepRepr_RepresentationItem: 
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
    def Move(self,theOther : StepRepr_Array1OfRepresentationItem) -> StepRepr_Array1OfRepresentationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_RepresentationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_RepresentationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepRepr_Array1OfRepresentationItem) -> None: ...
    @overload
    def __init__(self,theBegin : StepRepr_RepresentationItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepRepr_Array1OfShapeAspect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepRepr_Array1OfShapeAspect) -> StepRepr_Array1OfShapeAspect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepRepr_ShapeAspect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepRepr_ShapeAspect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_ShapeAspect: 
        """
        Variable value access
        """
    def First(self) -> StepRepr_ShapeAspect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepRepr_ShapeAspect) -> None: 
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
    def Last(self) -> StepRepr_ShapeAspect: 
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
    def Move(self,theOther : StepRepr_Array1OfShapeAspect) -> StepRepr_Array1OfShapeAspect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_ShapeAspect) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_ShapeAspect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepRepr_ShapeAspect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepRepr_Array1OfShapeAspect) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepRepr_ProductDefinitionUsage(OCP.StepBasic.StepBasic_ProductDefinitionRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ProductDefinitionUsageRepresentation of STEP entity ProductDefinitionUsageRepresentation of STEP entity ProductDefinitionUsage
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,aRelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,aRelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: ...
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatedProductDefinition
        """
    def RelatedProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatedProductDefinition in AP242
        """
    def RelatingProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatingProductDefinition
        """
    def RelatingProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatingProductDefinition in AP242
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatedProductDefinition

        Set field RelatedProductDefinition in AP242
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatingProductDefinition

        Set field RelatingProductDefinition in AP242
        """
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
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
class StepRepr_AssemblyComponentUsageSubstitute(OCP.Standard.Standard_Transient):
    def Base(self) -> StepRepr_AssemblyComponentUsage: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDef : OCP.TCollection.TCollection_HAsciiString,aBase : StepRepr_AssemblyComponentUsage,aSubs : StepRepr_AssemblyComponentUsage) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetBase(self,aBase : StepRepr_AssemblyComponentUsage) -> None: 
        """
        None
        """
    def SetDefinition(self,aDef : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSubstitute(self,aSubstitute : StepRepr_AssemblyComponentUsage) -> None: 
        """
        None
        """
    def Substitute(self) -> StepRepr_AssemblyComponentUsage: 
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
class StepRepr_CompositeShapeAspect(StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_CentreOfSymmetry(StepRepr_DerivedShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_CharacterizedDefinition(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type CharacterizedDefinition
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of CharacterizedDefinition select type 1 -> CharacterizedObject from StepBasic 2 -> ProductDefinition from StepBasic 3 -> ProductDefinitionRelationship from StepBasic 4 -> ProductDefinitionShape from StepRepr 5 -> ShapeAspect from StepRepr 6 -> ShapeAspectRelationship from StepRepr 7 -> DocumentFile from StepBasic 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CharacterizedObject(self) -> OCP.StepBasic.StepBasic_CharacterizedObject: 
        """
        Returns Value as CharacterizedObject (or Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DocumentFile(self) -> OCP.StepBasic.StepBasic_DocumentFile: 
        """
        Returns Value as DocumentFile (or Null if another type)
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns Value as ProductDefinition (or Null if another type)
        """
    def ProductDefinitionRelationship(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
        """
        Returns Value as ProductDefinitionRelationship (or Null if another type)
        """
    def ProductDefinitionShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        Returns Value as ProductDefinitionShape (or Null if another type)
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
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
    def ShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns Value as ShapeAspect (or Null if another type)
        """
    def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: 
        """
        Returns Value as ShapeAspectRelationship (or Null if another type)
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepRepr_Representation(OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> StepRepr_RepresentationContext: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : StepRepr_HArray1OfRepresentationItem,aContextOfItems : StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_CompShAspAndDatumFeatAndShAsp(StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_CompGroupShAspAndCompShAspAndDatumFeatAndShAsp(StepRepr_CompShAspAndDatumFeatAndShAsp, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_CompositeGroupShapeAspect(StepRepr_CompositeShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_ContinuosShapeAspect(StepRepr_CompositeShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_RepresentationItem(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_ConfigurationDesign(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ConfigurationDesignRepresentation of STEP entity ConfigurationDesignRepresentation of STEP entity ConfigurationDesign
    """
    def Configuration(self) -> StepRepr_ConfigurationItem: 
        """
        Returns field Configuration
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Design(self) -> StepRepr_ConfigurationDesignItem: 
        """
        Returns field Design
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
    def Init(self,aConfiguration : StepRepr_ConfigurationItem,aDesign : StepRepr_ConfigurationDesignItem) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetConfiguration(self,Configuration : StepRepr_ConfigurationItem) -> None: 
        """
        Set field Configuration
        """
    def SetDesign(self,Design : StepRepr_ConfigurationDesignItem) -> None: 
        """
        Set field Design
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
class StepRepr_ConfigurationDesignItem(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type ConfigurationDesignItem
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of ConfigurationDesignItem select type 1 -> ProductDefinition from StepBasic 2 -> ProductDefinitionFormation from StepBasic 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def ProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns Value as ProductDefinition (or Null if another type)
        """
    def ProductDefinitionFormation(self) -> OCP.StepBasic.StepBasic_ProductDefinitionFormation: 
        """
        Returns Value as ProductDefinitionFormation (or Null if another type)
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
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
    def __init__(self) -> None: ...
    pass
class StepRepr_ConfigurationEffectivity(OCP.StepBasic.StepBasic_ProductDefinitionEffectivity, OCP.StepBasic.StepBasic_Effectivity, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ConfigurationEffectivityRepresentation of STEP entity ConfigurationEffectivityRepresentation of STEP entity ConfigurationEffectivity
    """
    def Configuration(self) -> StepRepr_ConfigurationDesign: 
        """
        Returns field Configuration
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
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aEffectivity_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionEffectivity_Usage : OCP.StepBasic.StepBasic_ProductDefinitionRelationship,aConfiguration : StepRepr_ConfigurationDesign) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetConfiguration(self,Configuration : StepRepr_ConfigurationDesign) -> None: 
        """
        Set field Configuration
        """
    def SetId(self,aid : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetUsage(self,aUsage : OCP.StepBasic.StepBasic_ProductDefinitionRelationship) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Usage(self) -> OCP.StepBasic.StepBasic_ProductDefinitionRelationship: 
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
class StepRepr_ConfigurationItem(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ConfigurationItemRepresentation of STEP entity ConfigurationItemRepresentation of STEP entity ConfigurationItem
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def HasPurpose(self) -> bool: 
        """
        Returns True if optional field Purpose is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aItemConcept : StepRepr_ProductConcept,hasPurpose : bool,aPurpose : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def ItemConcept(self) -> StepRepr_ProductConcept: 
        """
        Returns field ItemConcept
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def Purpose(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Purpose
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetItemConcept(self,ItemConcept : StepRepr_ProductConcept) -> None: 
        """
        Set field ItemConcept
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetPurpose(self,Purpose : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Purpose
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
class StepRepr_ConstructiveGeometryRepresentation(StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> StepRepr_RepresentationContext: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : StepRepr_HArray1OfRepresentationItem,aContextOfItems : StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_RepresentationRelationship(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aRep1 : StepRepr_Representation,aRep2 : StepRepr_Representation) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Rep1(self) -> StepRepr_Representation: 
        """
        None
        """
    def Rep2(self) -> StepRepr_Representation: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRep1(self,aRep1 : StepRepr_Representation) -> None: 
        """
        None
        """
    def SetRep2(self,aRep2 : StepRepr_Representation) -> None: 
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
class StepRepr_BetweenShapeAspect(StepRepr_ContinuosShapeAspect, StepRepr_CompositeShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_DataEnvironment(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DataEnvironmentRepresentation of STEP entity DataEnvironmentRepresentation of STEP entity DataEnvironment
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Elements(self) -> StepRepr_HArray1OfPropertyDefinitionRepresentation: 
        """
        Returns field Elements
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aElements : StepRepr_HArray1OfPropertyDefinitionRepresentation) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetElements(self,Elements : StepRepr_HArray1OfPropertyDefinitionRepresentation) -> None: 
        """
        Set field Elements
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
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
class StepRepr_DefinitionalRepresentation(StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> StepRepr_RepresentationContext: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : StepRepr_HArray1OfRepresentationItem,aContextOfItems : StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_Apex(StepRepr_DerivedShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_DescriptiveRepresentationItem(StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_Extension(StepRepr_DerivedShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_ExternallyDefinedRepresentation(StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> StepRepr_RepresentationContext: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : StepRepr_HArray1OfRepresentationItem,aContextOfItems : StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_ShapeAspectRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ShapeAspectRelationshipRepresentation of STEP entity ShapeAspectRelationshipRepresentation of STEP entity ShapeAspectRelationship
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingShapeAspect : StepRepr_ShapeAspect,aRelatedShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns field RelatedShapeAspect
        """
    def RelatingShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns field RelatingShapeAspect
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedShapeAspect(self,RelatedShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatedShapeAspect
        """
    def SetRelatingShapeAspect(self,RelatingShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatingShapeAspect
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
class StepRepr_FunctionallyDefinedTransformation(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_GeometricAlignment(StepRepr_DerivedShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_RepresentationContext(OCP.Standard.Standard_Transient):
    def ContextIdentifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ContextType(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def SetContextIdentifier(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetContextType(self,aContextType : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_GlobalUnitAssignedContext(StepRepr_RepresentationContext, OCP.Standard.Standard_Transient):
    def ContextIdentifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ContextType(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString,aUnits : OCP.StepBasic.StepBasic_HArray1OfNamedUnit) -> None: 
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
    def NbUnits(self) -> int: 
        """
        None
        """
    def SetContextIdentifier(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetContextType(self,aContextType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetUnits(self,aUnits : OCP.StepBasic.StepBasic_HArray1OfNamedUnit) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Units(self) -> OCP.StepBasic.StepBasic_HArray1OfNamedUnit: 
        """
        None
        """
    def UnitsValue(self,num : int) -> OCP.StepBasic.StepBasic_NamedUnit: 
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
class StepRepr_HArray1OfMaterialPropertyRepresentation(StepRepr_Array1OfMaterialPropertyRepresentation, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepRepr_Array1OfMaterialPropertyRepresentation: 
        """
        None
        """
    def Assign(self,theOther : StepRepr_Array1OfMaterialPropertyRepresentation) -> StepRepr_Array1OfMaterialPropertyRepresentation: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepRepr_Array1OfMaterialPropertyRepresentation: 
        """
        None
        """
    def ChangeFirst(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_MaterialPropertyRepresentation: 
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
    def First(self) -> StepRepr_MaterialPropertyRepresentation: 
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
    def Init(self,theValue : StepRepr_MaterialPropertyRepresentation) -> None: 
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
    def Last(self) -> StepRepr_MaterialPropertyRepresentation: 
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
    def Move(self,theOther : StepRepr_Array1OfMaterialPropertyRepresentation) -> StepRepr_Array1OfMaterialPropertyRepresentation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_MaterialPropertyRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepRepr_Array1OfMaterialPropertyRepresentation) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepRepr_MaterialPropertyRepresentation) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class StepRepr_HArray1OfPropertyDefinitionRepresentation(StepRepr_Array1OfPropertyDefinitionRepresentation, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepRepr_Array1OfPropertyDefinitionRepresentation: 
        """
        None
        """
    def Assign(self,theOther : StepRepr_Array1OfPropertyDefinitionRepresentation) -> StepRepr_Array1OfPropertyDefinitionRepresentation: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepRepr_Array1OfPropertyDefinitionRepresentation: 
        """
        None
        """
    def ChangeFirst(self) -> StepRepr_PropertyDefinitionRepresentation: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepRepr_PropertyDefinitionRepresentation: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_PropertyDefinitionRepresentation: 
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
    def First(self) -> StepRepr_PropertyDefinitionRepresentation: 
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
    def Init(self,theValue : StepRepr_PropertyDefinitionRepresentation) -> None: 
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
    def Last(self) -> StepRepr_PropertyDefinitionRepresentation: 
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
    def Move(self,theOther : StepRepr_Array1OfPropertyDefinitionRepresentation) -> StepRepr_Array1OfPropertyDefinitionRepresentation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_PropertyDefinitionRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_PropertyDefinitionRepresentation: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepRepr_PropertyDefinitionRepresentation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepRepr_Array1OfPropertyDefinitionRepresentation) -> None: ...
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
class StepRepr_HArray1OfRepresentationItem(StepRepr_Array1OfRepresentationItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepRepr_Array1OfRepresentationItem: 
        """
        None
        """
    def Assign(self,theOther : StepRepr_Array1OfRepresentationItem) -> StepRepr_Array1OfRepresentationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepRepr_Array1OfRepresentationItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepRepr_RepresentationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepRepr_RepresentationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_RepresentationItem: 
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
    def First(self) -> StepRepr_RepresentationItem: 
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
    def Init(self,theValue : StepRepr_RepresentationItem) -> None: 
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
    def Last(self) -> StepRepr_RepresentationItem: 
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
    def Move(self,theOther : StepRepr_Array1OfRepresentationItem) -> StepRepr_Array1OfRepresentationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_RepresentationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_RepresentationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepRepr_Array1OfRepresentationItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepRepr_RepresentationItem) -> None: ...
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
class StepRepr_HArray1OfShapeAspect(StepRepr_Array1OfShapeAspect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepRepr_Array1OfShapeAspect: 
        """
        None
        """
    def Assign(self,theOther : StepRepr_Array1OfShapeAspect) -> StepRepr_Array1OfShapeAspect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepRepr_Array1OfShapeAspect: 
        """
        None
        """
    def ChangeFirst(self) -> StepRepr_ShapeAspect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepRepr_ShapeAspect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_ShapeAspect: 
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
    def First(self) -> StepRepr_ShapeAspect: 
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
    def Init(self,theValue : StepRepr_ShapeAspect) -> None: 
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
    def Last(self) -> StepRepr_ShapeAspect: 
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
    def Move(self,theOther : StepRepr_Array1OfShapeAspect) -> StepRepr_Array1OfShapeAspect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_ShapeAspect) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_ShapeAspect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepRepr_ShapeAspect) -> None: ...
    @overload
    def __init__(self,theOther : StepRepr_Array1OfShapeAspect) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class StepRepr_SequenceOfMaterialPropertyRepresentation(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : StepRepr_MaterialPropertyRepresentation) -> None: ...
    def Assign(self,theOther : StepRepr_SequenceOfMaterialPropertyRepresentation) -> StepRepr_SequenceOfMaterialPropertyRepresentation: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        First item access
        """
    def ChangeLast(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_MaterialPropertyRepresentation: 
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
    def First(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepRepr_MaterialPropertyRepresentation) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepRepr_MaterialPropertyRepresentation) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepRepr_MaterialPropertyRepresentation: 
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
    def Prepend(self,theItem : StepRepr_MaterialPropertyRepresentation) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StepRepr_MaterialPropertyRepresentation) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StepRepr_SequenceOfRepresentationItem(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : StepRepr_SequenceOfRepresentationItem) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : StepRepr_RepresentationItem) -> None: ...
    def Assign(self,theOther : StepRepr_SequenceOfRepresentationItem) -> StepRepr_SequenceOfRepresentationItem: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepRepr_RepresentationItem: 
        """
        First item access
        """
    def ChangeLast(self) -> StepRepr_RepresentationItem: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_RepresentationItem: 
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
    def First(self) -> StepRepr_RepresentationItem: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepRepr_SequenceOfRepresentationItem) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepRepr_RepresentationItem) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepRepr_RepresentationItem) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepRepr_SequenceOfRepresentationItem) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepRepr_RepresentationItem: 
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
    def Prepend(self,theItem : StepRepr_RepresentationItem) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepRepr_SequenceOfRepresentationItem) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StepRepr_RepresentationItem) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepRepr_SequenceOfRepresentationItem) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepRepr_RepresentationItem: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : StepRepr_SequenceOfRepresentationItem) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StepRepr_IntegerRepresentationItem(StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theValue : int) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetValue(self,theValue : int) -> None: 
        """
        None
        """
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
    pass
class StepRepr_ItemDefinedTransformation(OCP.Standard.Standard_Transient):
    """
    Added from StepRepr Rev2 to Rev4Added from StepRepr Rev2 to Rev4Added from StepRepr Rev2 to Rev4
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aTransformItem1 : StepRepr_RepresentationItem,aTransformItem2 : StepRepr_RepresentationItem) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTransformItem1(self,aItem : StepRepr_RepresentationItem) -> None: 
        """
        None
        """
    def SetTransformItem2(self,aItem : StepRepr_RepresentationItem) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformItem1(self) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def TransformItem2(self) -> StepRepr_RepresentationItem: 
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
class StepRepr_MakeFromUsageOption(StepRepr_ProductDefinitionUsage, OCP.StepBasic.StepBasic_ProductDefinitionRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity MakeFromUsageOptionRepresentation of STEP entity MakeFromUsageOptionRepresentation of STEP entity MakeFromUsageOption
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,aRanking : int,aRankingRationale : OCP.TCollection.TCollection_HAsciiString,aQuantity : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,aRanking : int,aRankingRationale : OCP.TCollection.TCollection_HAsciiString,aQuantity : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: ...
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def Quantity(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Quantity
        """
    def Ranking(self) -> int: 
        """
        Returns field Ranking
        """
    def RankingRationale(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field RankingRationale
        """
    def RelatedProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatedProductDefinition
        """
    def RelatedProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatedProductDefinition in AP242
        """
    def RelatingProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatingProductDefinition
        """
    def RelatingProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatingProductDefinition in AP242
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetQuantity(self,Quantity : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Quantity
        """
    def SetRanking(self,Ranking : int) -> None: 
        """
        Set field Ranking
        """
    def SetRankingRationale(self,RankingRationale : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field RankingRationale
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatedProductDefinition

        Set field RelatedProductDefinition in AP242
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatingProductDefinition

        Set field RelatingProductDefinition in AP242
        """
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
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
class StepRepr_MappedItem(StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aMappingSource : StepRepr_RepresentationMap,aMappingTarget : StepRepr_RepresentationItem) -> None: 
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
    def MappingSource(self) -> StepRepr_RepresentationMap: 
        """
        None
        """
    def MappingTarget(self) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMappingSource(self,aMappingSource : StepRepr_RepresentationMap) -> None: 
        """
        None
        """
    def SetMappingTarget(self,aMappingTarget : StepRepr_RepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_MaterialDesignation(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOfDefinition : StepRepr_CharacterizedDefinition) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfDefinition(self) -> StepRepr_CharacterizedDefinition: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfDefinition(self,aOfDefinition : StepRepr_CharacterizedDefinition) -> None: 
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
class StepRepr_PropertyDefinition(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity PropertyDefinitionRepresentation of STEP entity PropertyDefinitionRepresentation of STEP entity PropertyDefinition
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepRepr_CharacterizedDefinition: 
        """
        Returns field Definition
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aDefinition : StepRepr_CharacterizedDefinition) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDefinition(self,Definition : StepRepr_CharacterizedDefinition) -> None: 
        """
        Set field Definition
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
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
class StepRepr_PropertyDefinitionRepresentation(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity PropertyDefinitionRepresentationRepresentation of STEP entity PropertyDefinitionRepresentationRepresentation of STEP entity PropertyDefinitionRepresentation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepRepr_RepresentedDefinition: 
        """
        Returns field Definition
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
    def Init(self,aDefinition : StepRepr_RepresentedDefinition,aUsedRepresentation : StepRepr_Representation) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetDefinition(self,Definition : StepRepr_RepresentedDefinition) -> None: 
        """
        Set field Definition
        """
    def SetUsedRepresentation(self,UsedRepresentation : StepRepr_Representation) -> None: 
        """
        Set field UsedRepresentation
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UsedRepresentation(self) -> StepRepr_Representation: 
        """
        Returns field UsedRepresentation
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
class StepRepr_MeasureRepresentationItem(StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Implements a measure_representation_item entity which is used for storing validation properties (e.g. area) for shapesImplements a measure_representation_item entity which is used for storing validation properties (e.g. area) for shapesImplements a measure_representation_item entity which is used for storing validation properties (e.g. area) for shapes
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aValueComponent : OCP.StepBasic.StepBasic_MeasureValueMember,aUnitComponent : OCP.StepBasic.StepBasic_Unit) -> None: 
        """
        Init all fields
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
    def Measure(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMeasure(self,Measure : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_AssemblyComponentUsage(StepRepr_ProductDefinitionUsage, OCP.StepBasic.StepBasic_ProductDefinitionRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity AssemblyComponentUsageRepresentation of STEP entity AssemblyComponentUsageRepresentation of STEP entity AssemblyComponentUsage
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def HasReferenceDesignator(self) -> bool: 
        """
        Returns True if optional field ReferenceDesignator is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,hasReferenceDesignator : bool,aReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,hasReferenceDesignator : bool,aReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: ...
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def ReferenceDesignator(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field ReferenceDesignator
        """
    def RelatedProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatedProductDefinition
        """
    def RelatedProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatedProductDefinition in AP242
        """
    def RelatingProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatingProductDefinition
        """
    def RelatingProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatingProductDefinition in AP242
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetReferenceDesignator(self,ReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field ReferenceDesignator
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatedProductDefinition

        Set field RelatedProductDefinition in AP242
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatingProductDefinition

        Set field RelatingProductDefinition in AP242
        """
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
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
class StepRepr_ParallelOffset(StepRepr_DerivedShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theOfShape : StepRepr_ProductDefinitionShape,theProductDefinitional : OCP.StepData.StepData_Logical,theOffset : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def Offset(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Offset
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetOffset(self,theOffset : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Offset
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_ParametricRepresentationContext(StepRepr_RepresentationContext, OCP.Standard.Standard_Transient):
    def ContextIdentifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ContextType(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def SetContextIdentifier(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetContextType(self,aContextType : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_PerpendicularTo(StepRepr_DerivedShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_ProductConcept(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ProductConceptRepresentation of STEP entity ProductConceptRepresentation of STEP entity ProductConcept
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aMarketContext : OCP.StepBasic.StepBasic_ProductConceptContext) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def MarketContext(self) -> OCP.StepBasic.StepBasic_ProductConceptContext: 
        """
        Returns field MarketContext
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetMarketContext(self,MarketContext : OCP.StepBasic.StepBasic_ProductConceptContext) -> None: 
        """
        Set field MarketContext
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
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
class StepRepr_ProductDefinitionShape(StepRepr_PropertyDefinition, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ProductDefinitionShapeRepresentation of STEP entity ProductDefinitionShapeRepresentation of STEP entity ProductDefinitionShape
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepRepr_CharacterizedDefinition: 
        """
        Returns field Definition
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aDefinition : StepRepr_CharacterizedDefinition) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDefinition(self,Definition : StepRepr_CharacterizedDefinition) -> None: 
        """
        Set field Definition
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
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
class StepRepr_NextAssemblyUsageOccurrence(StepRepr_AssemblyComponentUsage, StepRepr_ProductDefinitionUsage, OCP.StepBasic.StepBasic_ProductDefinitionRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NextAssemblyUsageOccurrenceRepresentation of STEP entity NextAssemblyUsageOccurrenceRepresentation of STEP entity NextAssemblyUsageOccurrence
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def HasReferenceDesignator(self) -> bool: 
        """
        Returns True if optional field ReferenceDesignator is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,hasReferenceDesignator : bool,aReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,hasReferenceDesignator : bool,aReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: ...
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def ReferenceDesignator(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field ReferenceDesignator
        """
    def RelatedProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatedProductDefinition
        """
    def RelatedProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatedProductDefinition in AP242
        """
    def RelatingProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatingProductDefinition
        """
    def RelatingProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatingProductDefinition in AP242
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetReferenceDesignator(self,ReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field ReferenceDesignator
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatedProductDefinition

        Set field RelatedProductDefinition in AP242
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatingProductDefinition

        Set field RelatingProductDefinition in AP242
        """
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
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
class StepRepr_PromissoryUsageOccurrence(StepRepr_AssemblyComponentUsage, StepRepr_ProductDefinitionUsage, OCP.StepBasic.StepBasic_ProductDefinitionRelationship, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def HasReferenceDesignator(self) -> bool: 
        """
        Returns True if optional field ReferenceDesignator is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,hasReferenceDesignator : bool,aReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,hasReferenceDesignator : bool,aReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: ...
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def ReferenceDesignator(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field ReferenceDesignator
        """
    def RelatedProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatedProductDefinition
        """
    def RelatedProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatedProductDefinition in AP242
        """
    def RelatingProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatingProductDefinition
        """
    def RelatingProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatingProductDefinition in AP242
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetReferenceDesignator(self,ReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field ReferenceDesignator
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatedProductDefinition

        Set field RelatedProductDefinition in AP242
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatingProductDefinition

        Set field RelatingProductDefinition in AP242
        """
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
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
class StepRepr_MaterialProperty(StepRepr_PropertyDefinition, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity MaterialPropertyRepresentation of STEP entity MaterialPropertyRepresentation of STEP entity MaterialProperty
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepRepr_CharacterizedDefinition: 
        """
        Returns field Definition
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aDefinition : StepRepr_CharacterizedDefinition) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDefinition(self,Definition : StepRepr_CharacterizedDefinition) -> None: 
        """
        Set field Definition
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
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
class StepRepr_PropertyDefinitionRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity PropertyDefinitionRelationshipRepresentation of STEP entity PropertyDefinitionRelationshipRepresentation of STEP entity PropertyDefinitionRelationship
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingPropertyDefinition : StepRepr_PropertyDefinition,aRelatedPropertyDefinition : StepRepr_PropertyDefinition) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedPropertyDefinition(self) -> StepRepr_PropertyDefinition: 
        """
        Returns field RelatedPropertyDefinition
        """
    def RelatingPropertyDefinition(self) -> StepRepr_PropertyDefinition: 
        """
        Returns field RelatingPropertyDefinition
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedPropertyDefinition(self,RelatedPropertyDefinition : StepRepr_PropertyDefinition) -> None: 
        """
        Set field RelatedPropertyDefinition
        """
    def SetRelatingPropertyDefinition(self,RelatingPropertyDefinition : StepRepr_PropertyDefinition) -> None: 
        """
        Set field RelatingPropertyDefinition
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
class StepRepr_MaterialPropertyRepresentation(StepRepr_PropertyDefinitionRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity MaterialPropertyRepresentationRepresentation of STEP entity MaterialPropertyRepresentationRepresentation of STEP entity MaterialPropertyRepresentation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepRepr_RepresentedDefinition: 
        """
        Returns field Definition
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DependentEnvironment(self) -> StepRepr_DataEnvironment: 
        """
        Returns field DependentEnvironment
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
    def Init(self,aPropertyDefinitionRepresentation_Definition : StepRepr_RepresentedDefinition,aPropertyDefinitionRepresentation_UsedRepresentation : StepRepr_Representation,aDependentEnvironment : StepRepr_DataEnvironment) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetDefinition(self,Definition : StepRepr_RepresentedDefinition) -> None: 
        """
        Set field Definition
        """
    def SetDependentEnvironment(self,DependentEnvironment : StepRepr_DataEnvironment) -> None: 
        """
        Set field DependentEnvironment
        """
    def SetUsedRepresentation(self,UsedRepresentation : StepRepr_Representation) -> None: 
        """
        Set field UsedRepresentation
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UsedRepresentation(self) -> StepRepr_Representation: 
        """
        Returns field UsedRepresentation
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
class StepRepr_QuantifiedAssemblyComponentUsage(StepRepr_AssemblyComponentUsage, StepRepr_ProductDefinitionUsage, OCP.StepBasic.StepBasic_ProductDefinitionRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity QuantifiedAssemblyComponentUsageRepresentation of STEP entity QuantifiedAssemblyComponentUsageRepresentation of STEP entity QuantifiedAssemblyComponentUsage
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def HasReferenceDesignator(self) -> bool: 
        """
        Returns True if optional field ReferenceDesignator is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,hasAssemblyComponentUsage_ReferenceDesignator : bool,aAssemblyComponentUsage_ReferenceDesignator : OCP.TCollection.TCollection_HAsciiString,aQuantity : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,hasAssemblyComponentUsage_ReferenceDesignator : bool,aAssemblyComponentUsage_ReferenceDesignator : OCP.TCollection.TCollection_HAsciiString,aQuantity : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: ...
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def Quantity(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Quantity
        """
    def ReferenceDesignator(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field ReferenceDesignator
        """
    def RelatedProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatedProductDefinition
        """
    def RelatedProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatedProductDefinition in AP242
        """
    def RelatingProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatingProductDefinition
        """
    def RelatingProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatingProductDefinition in AP242
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetQuantity(self,Quantity : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Quantity
        """
    def SetReferenceDesignator(self,ReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field ReferenceDesignator
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatedProductDefinition

        Set field RelatedProductDefinition in AP242
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatingProductDefinition

        Set field RelatingProductDefinition in AP242
        """
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
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
class StepRepr_ReprItemAndMeasureWithUnit(StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Base class for complex types (MEASURE_REPRESENTATION_ITEM, MEASURE_WITH_UNIT, REPRESENTATION_ITEM, LENGTH_MEASURE_WITH_UNIT/PLANE_ANGLE_MEASURE_WITH_UNIT).Base class for complex types (MEASURE_REPRESENTATION_ITEM, MEASURE_WITH_UNIT, REPRESENTATION_ITEM, LENGTH_MEASURE_WITH_UNIT/PLANE_ANGLE_MEASURE_WITH_UNIT).Base class for complex types (MEASURE_REPRESENTATION_ITEM, MEASURE_WITH_UNIT, REPRESENTATION_ITEM, LENGTH_MEASURE_WITH_UNIT/PLANE_ANGLE_MEASURE_WITH_UNIT).
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
    def GetMeasureRepresentationItem(self) -> StepRepr_MeasureRepresentationItem: 
        """
        None
        """
    def GetMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRepresentationItem(self) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit,aRI : StepRepr_RepresentationItem) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMeasureWithUnit(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_ReprItemAndMeasureWithUnitAndQRI(StepRepr_ReprItemAndMeasureWithUnit, StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Base class for complex types (MEASURE_REPRESENTATION_ITEM, MEASURE_WITH_UNIT, QUALIFIED_REPRESENTATION_ITEM REPRESENTATION_ITEM, LENGTH_MEASURE_WITH_UNIT/PLANE_ANGLE_MEASURE_WITH_UNIT).Base class for complex types (MEASURE_REPRESENTATION_ITEM, MEASURE_WITH_UNIT, QUALIFIED_REPRESENTATION_ITEM REPRESENTATION_ITEM, LENGTH_MEASURE_WITH_UNIT/PLANE_ANGLE_MEASURE_WITH_UNIT).Base class for complex types (MEASURE_REPRESENTATION_ITEM, MEASURE_WITH_UNIT, QUALIFIED_REPRESENTATION_ITEM REPRESENTATION_ITEM, LENGTH_MEASURE_WITH_UNIT/PLANE_ANGLE_MEASURE_WITH_UNIT).
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
    def GetMeasureRepresentationItem(self) -> StepRepr_MeasureRepresentationItem: 
        """
        None
        """
    def GetMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        None
        """
    def GetQualifiedRepresentationItem(self) -> OCP.StepShape.StepShape_QualifiedRepresentationItem: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRepresentationItem(self) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit,aRI : StepRepr_RepresentationItem,aQRI : OCP.StepShape.StepShape_QualifiedRepresentationItem) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMeasureWithUnit(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetQualifiedRepresentationItem(self,aQRI : OCP.StepShape.StepShape_QualifiedRepresentationItem) -> None: 
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
class StepRepr_ReprItemAndLengthMeasureWithUnit(StepRepr_ReprItemAndMeasureWithUnit, StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def GetLengthMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        None
        """
    def GetMeasureRepresentationItem(self) -> StepRepr_MeasureRepresentationItem: 
        """
        None
        """
    def GetMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRepresentationItem(self) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit,aRI : StepRepr_RepresentationItem) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetLengthMeasureWithUnit(self,aLMWU : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        None
        """
    def SetMeasureWithUnit(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_ReprItemAndLengthMeasureWithUnitAndQRI(StepRepr_ReprItemAndMeasureWithUnitAndQRI, StepRepr_ReprItemAndMeasureWithUnit, StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def GetLengthMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        None
        """
    def GetMeasureRepresentationItem(self) -> StepRepr_MeasureRepresentationItem: 
        """
        None
        """
    def GetMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        None
        """
    def GetQualifiedRepresentationItem(self) -> OCP.StepShape.StepShape_QualifiedRepresentationItem: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRepresentationItem(self) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit,aRI : StepRepr_RepresentationItem,aQRI : OCP.StepShape.StepShape_QualifiedRepresentationItem) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetLengthMeasureWithUnit(self,aLMWU : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        None
        """
    def SetMeasureWithUnit(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetQualifiedRepresentationItem(self,aQRI : OCP.StepShape.StepShape_QualifiedRepresentationItem) -> None: 
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
class StepRepr_ReprItemAndPlaneAngleMeasureWithUnit(StepRepr_ReprItemAndMeasureWithUnit, StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def GetMeasureRepresentationItem(self) -> StepRepr_MeasureRepresentationItem: 
        """
        None
        """
    def GetMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        None
        """
    def GetPlaneAngleMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRepresentationItem(self) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit,aRI : StepRepr_RepresentationItem) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMeasureWithUnit(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPlaneAngleMeasureWithUnit(self,aLMWU : OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit) -> None: 
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
class StepRepr_ReprItemAndPlaneAngleMeasureWithUnitAndQRI(StepRepr_ReprItemAndMeasureWithUnitAndQRI, StepRepr_ReprItemAndMeasureWithUnit, StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def GetMeasureRepresentationItem(self) -> StepRepr_MeasureRepresentationItem: 
        """
        None
        """
    def GetMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        None
        """
    def GetPlaneAngleMeasureWithUnit(self) -> OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit: 
        """
        None
        """
    def GetQualifiedRepresentationItem(self) -> OCP.StepShape.StepShape_QualifiedRepresentationItem: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRepresentationItem(self) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit,aRI : StepRepr_RepresentationItem,aQRI : OCP.StepShape.StepShape_QualifiedRepresentationItem) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMeasureWithUnit(self,aMWU : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPlaneAngleMeasureWithUnit(self,aLMWU : OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit) -> None: 
        """
        None
        """
    def SetQualifiedRepresentationItem(self,aQRI : OCP.StepShape.StepShape_QualifiedRepresentationItem) -> None: 
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
class StepRepr_CharacterizedRepresentation(StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> StepRepr_RepresentationContext: 
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
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theItems : StepRepr_HArray1OfRepresentationItem,theContextOfItems : StepRepr_RepresentationContext) -> None: 
        """
        Returns a CharacterizedRepresentation
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
    def Items(self) -> StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetItems(self,aItems : StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_GlobalUncertaintyAssignedContext(StepRepr_RepresentationContext, OCP.Standard.Standard_Transient):
    def ContextIdentifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ContextType(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString,aUncertainty : OCP.StepBasic.StepBasic_HArray1OfUncertaintyMeasureWithUnit) -> None: 
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
    def NbUncertainty(self) -> int: 
        """
        None
        """
    def SetContextIdentifier(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetContextType(self,aContextType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetUncertainty(self,aUncertainty : OCP.StepBasic.StepBasic_HArray1OfUncertaintyMeasureWithUnit) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Uncertainty(self) -> OCP.StepBasic.StepBasic_HArray1OfUncertaintyMeasureWithUnit: 
        """
        None
        """
    def UncertaintyValue(self,num : int) -> OCP.StepBasic.StepBasic_UncertaintyMeasureWithUnit: 
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
class StepRepr_CompoundRepresentationItem(StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,item_element : StepRepr_HArray1OfRepresentationItem) -> None: 
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
    def ItemElement(self) -> StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemElementValue(self,num : int) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItemElement(self) -> int: 
        """
        None
        """
    def SetItemElement(self,item_element : StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetItemElementValue(self,num : int,anelement : StepRepr_RepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_RepresentationMap(OCP.Standard.Standard_Transient):
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
    def Init(self,aMappingOrigin : StepRepr_RepresentationItem,aMappedRepresentation : StepRepr_Representation) -> None: 
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
    def MappedRepresentation(self) -> StepRepr_Representation: 
        """
        None
        """
    def MappingOrigin(self) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def SetMappedRepresentation(self,aMappedRepresentation : StepRepr_Representation) -> None: 
        """
        None
        """
    def SetMappingOrigin(self,aMappingOrigin : StepRepr_RepresentationItem) -> None: 
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
class StepRepr_ConstructiveGeometryRepresentationRelationship(StepRepr_RepresentationRelationship, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aRep1 : StepRepr_Representation,aRep2 : StepRepr_Representation) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Rep1(self) -> StepRepr_Representation: 
        """
        None
        """
    def Rep2(self) -> StepRepr_Representation: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRep1(self,aRep1 : StepRepr_Representation) -> None: 
        """
        None
        """
    def SetRep2(self,aRep2 : StepRepr_Representation) -> None: 
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
class StepRepr_ShapeRepresentationRelationship(StepRepr_RepresentationRelationship, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aRep1 : StepRepr_Representation,aRep2 : StepRepr_Representation) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Rep1(self) -> StepRepr_Representation: 
        """
        None
        """
    def Rep2(self) -> StepRepr_Representation: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRep1(self,aRep1 : StepRepr_Representation) -> None: 
        """
        None
        """
    def SetRep2(self,aRep2 : StepRepr_Representation) -> None: 
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
class StepRepr_RepresentedDefinition(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type RepresentedDefinition
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of RepresentedDefinition select type 1 -> GeneralProperty from StepBasic 2 -> PropertyDefinition from StepRepr 3 -> PropertyDefinitionRelationship from StepRepr 4 -> ShapeAspect from StepRepr 5 -> ShapeAspectRelationship from StepRepr 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def GeneralProperty(self) -> OCP.StepBasic.StepBasic_GeneralProperty: 
        """
        Returns Value as GeneralProperty (or Null if another type)
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def PropertyDefinition(self) -> StepRepr_PropertyDefinition: 
        """
        Returns Value as PropertyDefinition (or Null if another type)
        """
    def PropertyDefinitionRelationship(self) -> StepRepr_PropertyDefinitionRelationship: 
        """
        Returns Value as PropertyDefinitionRelationship (or Null if another type)
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
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
    def ShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns Value as ShapeAspect (or Null if another type)
        """
    def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: 
        """
        Returns Value as ShapeAspectRelationship (or Null if another type)
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepRepr_HSequenceOfMaterialPropertyRepresentation(StepRepr_SequenceOfMaterialPropertyRepresentation, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepRepr_MaterialPropertyRepresentation) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: ...
    def Assign(self,theOther : StepRepr_SequenceOfMaterialPropertyRepresentation) -> StepRepr_SequenceOfMaterialPropertyRepresentation: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        First item access
        """
    def ChangeLast(self) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepRepr_SequenceOfMaterialPropertyRepresentation: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_MaterialPropertyRepresentation: 
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
    def First(self) -> StepRepr_MaterialPropertyRepresentation: 
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
    def InsertAfter(self,theIndex : int,theSeq : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepRepr_MaterialPropertyRepresentation) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepRepr_MaterialPropertyRepresentation) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: ...
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
    def Last(self) -> StepRepr_MaterialPropertyRepresentation: 
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
    def Prepend(self,theItem : StepRepr_MaterialPropertyRepresentation) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: ...
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
    def Sequence(self) -> StepRepr_SequenceOfMaterialPropertyRepresentation: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_MaterialPropertyRepresentation) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_MaterialPropertyRepresentation: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StepRepr_SequenceOfMaterialPropertyRepresentation) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class StepRepr_HSequenceOfRepresentationItem(StepRepr_SequenceOfRepresentationItem, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : StepRepr_SequenceOfRepresentationItem) -> None: ...
    def Assign(self,theOther : StepRepr_SequenceOfRepresentationItem) -> StepRepr_SequenceOfRepresentationItem: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepRepr_RepresentationItem: 
        """
        First item access
        """
    def ChangeLast(self) -> StepRepr_RepresentationItem: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepRepr_SequenceOfRepresentationItem: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepRepr_RepresentationItem: 
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
    def First(self) -> StepRepr_RepresentationItem: 
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
    def InsertAfter(self,theIndex : int,theSeq : StepRepr_SequenceOfRepresentationItem) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepRepr_RepresentationItem) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepRepr_RepresentationItem) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepRepr_SequenceOfRepresentationItem) -> None: ...
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
    def Last(self) -> StepRepr_RepresentationItem: 
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
    def Prepend(self,theItem : StepRepr_RepresentationItem) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepRepr_SequenceOfRepresentationItem) -> None: ...
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
    def Sequence(self) -> StepRepr_SequenceOfRepresentationItem: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepRepr_RepresentationItem) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepRepr_SequenceOfRepresentationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepRepr_RepresentationItem: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepRepr_SequenceOfRepresentationItem) -> None: ...
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
class StepRepr_AllAroundShapeAspect(StepRepr_ContinuosShapeAspect, StepRepr_CompositeShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_ShapeAspectDerivingRelationship(StepRepr_ShapeAspectRelationship, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingShapeAspect : StepRepr_ShapeAspect,aRelatedShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns field RelatedShapeAspect
        """
    def RelatingShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns field RelatingShapeAspect
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedShapeAspect(self,RelatedShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatedShapeAspect
        """
    def SetRelatingShapeAspect(self,RelatingShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatingShapeAspect
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
class StepRepr_FeatureForDatumTargetRelationship(StepRepr_ShapeAspectRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DimensionalLocationRepresentation of STEP entity DimensionalLocationRepresentation of STEP entity DimensionalLocation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingShapeAspect : StepRepr_ShapeAspect,aRelatedShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns field RelatedShapeAspect
        """
    def RelatingShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns field RelatingShapeAspect
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedShapeAspect(self,RelatedShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatedShapeAspect
        """
    def SetRelatingShapeAspect(self,RelatingShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatingShapeAspect
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
class StepRepr_ShapeAspectTransition(StepRepr_ShapeAspectRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ShapeAspectTransitionRepresentation of STEP entity ShapeAspectTransitionRepresentation of STEP entity ShapeAspectTransition
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingShapeAspect : StepRepr_ShapeAspect,aRelatedShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns field RelatedShapeAspect
        """
    def RelatingShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        Returns field RelatingShapeAspect
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedShapeAspect(self,RelatedShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatedShapeAspect
        """
    def SetRelatingShapeAspect(self,RelatingShapeAspect : StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatingShapeAspect
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
class StepRepr_ShapeDefinition(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a ShapeDefinition Kind Entity that is : 1 -> ProductDefinitionShape 2 -> ShapeAspect 3 -> ShapeAspectRelationship 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def ProductDefinitionShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        returns Value as a ProductDefinitionShape (Null if another type)
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
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
    def ShapeAspect(self) -> StepRepr_ShapeAspect: 
        """
        returns Value as a ShapeAspect (Null if another type)
        """
    def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: 
        """
        returns Value as a ShapeAspectRelationship (Null if another type)
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepRepr_RepresentationRelationshipWithTransformation(StepRepr_ShapeRepresentationRelationship, StepRepr_RepresentationRelationship, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aRep1 : StepRepr_Representation,aRep2 : StepRepr_Representation,aTransf : StepRepr_Transformation) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Rep1(self) -> StepRepr_Representation: 
        """
        None
        """
    def Rep2(self) -> StepRepr_Representation: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRep1(self,aRep1 : StepRepr_Representation) -> None: 
        """
        None
        """
    def SetRep2(self,aRep2 : StepRepr_Representation) -> None: 
        """
        None
        """
    def SetTransformationOperator(self,aTrans : StepRepr_Transformation) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformationOperator(self) -> StepRepr_Transformation: 
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
class StepRepr_ShapeRepresentationRelationshipWithTransformation(StepRepr_RepresentationRelationshipWithTransformation, StepRepr_ShapeRepresentationRelationship, StepRepr_RepresentationRelationship, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aRep1 : StepRepr_Representation,aRep2 : StepRepr_Representation,aTransf : StepRepr_Transformation) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Rep1(self) -> StepRepr_Representation: 
        """
        None
        """
    def Rep2(self) -> StepRepr_Representation: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRep1(self,aRep1 : StepRepr_Representation) -> None: 
        """
        None
        """
    def SetRep2(self,aRep2 : StepRepr_Representation) -> None: 
        """
        None
        """
    def SetTransformationOperator(self,aTrans : StepRepr_Transformation) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformationOperator(self) -> StepRepr_Transformation: 
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
class StepRepr_SpecifiedHigherUsageOccurrence(StepRepr_AssemblyComponentUsage, StepRepr_ProductDefinitionUsage, OCP.StepBasic.StepBasic_ProductDefinitionRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SpecifiedHigherUsageOccurrenceRepresentation of STEP entity SpecifiedHigherUsageOccurrenceRepresentation of STEP entity SpecifiedHigherUsageOccurrence
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def HasReferenceDesignator(self) -> bool: 
        """
        Returns True if optional field ReferenceDesignator is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,hasAssemblyComponentUsage_ReferenceDesignator : bool,aAssemblyComponentUsage_ReferenceDesignator : OCP.TCollection.TCollection_HAsciiString,aUpperUsage : StepRepr_AssemblyComponentUsage,aNextUsage : StepRepr_NextAssemblyUsageOccurrence) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,aProductDefinitionRelationship_Id : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasProductDefinitionRelationship_Description : bool,aProductDefinitionRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aProductDefinitionRelationship_RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,aProductDefinitionRelationship_RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,hasAssemblyComponentUsage_ReferenceDesignator : bool,aAssemblyComponentUsage_ReferenceDesignator : OCP.TCollection.TCollection_HAsciiString,aUpperUsage : StepRepr_AssemblyComponentUsage,aNextUsage : StepRepr_NextAssemblyUsageOccurrence) -> None: ...
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def NextUsage(self) -> StepRepr_NextAssemblyUsageOccurrence: 
        """
        Returns field NextUsage
        """
    def ReferenceDesignator(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field ReferenceDesignator
        """
    def RelatedProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatedProductDefinition
        """
    def RelatedProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatedProductDefinition in AP242
        """
    def RelatingProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatingProductDefinition
        """
    def RelatingProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatingProductDefinition in AP242
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetNextUsage(self,NextUsage : StepRepr_NextAssemblyUsageOccurrence) -> None: 
        """
        Set field NextUsage
        """
    def SetReferenceDesignator(self,ReferenceDesignator : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field ReferenceDesignator
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatedProductDefinition

        Set field RelatedProductDefinition in AP242
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatingProductDefinition

        Set field RelatingProductDefinition in AP242
        """
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
    def SetUpperUsage(self,UpperUsage : StepRepr_AssemblyComponentUsage) -> None: 
        """
        Set field UpperUsage
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpperUsage(self) -> StepRepr_AssemblyComponentUsage: 
        """
        Returns field UpperUsage
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
class StepRepr_StructuralResponseProperty(StepRepr_PropertyDefinition, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity StructuralResponsePropertyRepresentation of STEP entity StructuralResponsePropertyRepresentation of STEP entity StructuralResponseProperty
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepRepr_CharacterizedDefinition: 
        """
        Returns field Definition
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aDefinition : StepRepr_CharacterizedDefinition) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDefinition(self,Definition : StepRepr_CharacterizedDefinition) -> None: 
        """
        Set field Definition
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
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
class StepRepr_StructuralResponsePropertyDefinitionRepresentation(StepRepr_PropertyDefinitionRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity StructuralResponsePropertyDefinitionRepresentationRepresentation of STEP entity StructuralResponsePropertyDefinitionRepresentationRepresentation of STEP entity StructuralResponsePropertyDefinitionRepresentation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepRepr_RepresentedDefinition: 
        """
        Returns field Definition
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
    def Init(self,aDefinition : StepRepr_RepresentedDefinition,aUsedRepresentation : StepRepr_Representation) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetDefinition(self,Definition : StepRepr_RepresentedDefinition) -> None: 
        """
        Set field Definition
        """
    def SetUsedRepresentation(self,UsedRepresentation : StepRepr_Representation) -> None: 
        """
        Set field UsedRepresentation
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UsedRepresentation(self) -> StepRepr_Representation: 
        """
        Returns field UsedRepresentation
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
class StepRepr_SuppliedPartRelationship(OCP.StepBasic.StepBasic_ProductDefinitionRelationship, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def Id(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Id
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition,aRelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: 
        """
        Initialize all fields (own and inherited)

        Initialize all fields (own and inherited)
        """
    @overload
    def Init(self,aId : OCP.TCollection.TCollection_HAsciiString,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference,aRelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: ...
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def RelatedProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatedProductDefinition
        """
    def RelatedProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatedProductDefinition in AP242
        """
    def RelatingProductDefinition(self) -> OCP.StepBasic.StepBasic_ProductDefinition: 
        """
        Returns field RelatingProductDefinition
        """
    def RelatingProductDefinitionAP242(self) -> OCP.StepBasic.StepBasic_ProductDefinitionOrReference: 
        """
        Returns field RelatingProductDefinition in AP242
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetId(self,Id : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Id
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatedProductDefinition

        Set field RelatedProductDefinition in AP242
        """
    @overload
    def SetRelatedProductDefinition(self,RelatedProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinitionOrReference) -> None: 
        """
        Set field RelatingProductDefinition

        Set field RelatingProductDefinition in AP242
        """
    @overload
    def SetRelatingProductDefinition(self,RelatingProductDefinition : OCP.StepBasic.StepBasic_ProductDefinition) -> None: ...
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
class StepRepr_Tangent(StepRepr_DerivedShapeAspect, StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def OfShape(self) -> StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOfShape(self,aOfShape : StepRepr_ProductDefinitionShape) -> None: 
        """
        None
        """
    def SetProductDefinitional(self,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
class StepRepr_Transformation(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a Transformation Kind Entity that is : 1 -> ItemDefinedTransformation 2 -> FunctionallyDefinedTransformation 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def FunctionallyDefinedTransformation(self) -> StepRepr_FunctionallyDefinedTransformation: 
        """
        returns Value as a FunctionallyDefinedTransformation (Null if another type)
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
    def ItemDefinedTransformation(self) -> StepRepr_ItemDefinedTransformation: 
        """
        returns Value as a ItemDefinedTransformation (Null if another type)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
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
    def __init__(self) -> None: ...
    pass
class StepRepr_ValueRange(StepRepr_CompoundRepresentationItem, StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,item_element : StepRepr_HArray1OfRepresentationItem) -> None: 
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
    def ItemElement(self) -> StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemElementValue(self,num : int) -> StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItemElement(self) -> int: 
        """
        None
        """
    def SetItemElement(self,item_element : StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetItemElementValue(self,num : int,anelement : StepRepr_RepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepRepr_ValueRepresentationItem(StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theValueComponentMember : OCP.StepBasic.StepBasic_MeasureValueMember) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetValueComponentMember(self,theValueComponentMember : OCP.StepBasic.StepBasic_MeasureValueMember) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ValueComponentMember(self) -> OCP.StepBasic.StepBasic_MeasureValueMember: 
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
