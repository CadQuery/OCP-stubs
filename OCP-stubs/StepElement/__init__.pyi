import OCP.StepElement
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.NCollection
import OCP.StepData
import OCP.Interface
import OCP.Standard
import OCP.StepRepr
import OCP.TColStd
__all__  = [
"StepElement_AnalysisItemWithinRepresentation",
"StepElement_Array1OfCurveElementEndReleasePacket",
"StepElement_Array1OfCurveElementSectionDefinition",
"StepElement_Array1OfHSequenceOfCurveElementPurposeMember",
"StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember",
"StepElement_Array1OfMeasureOrUnspecifiedValue",
"StepElement_Array1OfSurfaceSection",
"StepElement_Array1OfVolumeElementPurpose",
"StepElement_Array1OfVolumeElementPurposeMember",
"StepElement_Array2OfCurveElementPurposeMember",
"StepElement_Array2OfSurfaceElementPurpose",
"StepElement_Array2OfSurfaceElementPurposeMember",
"StepElement_ElementDescriptor",
"StepElement_CurveEdge",
"StepElement_CurveElementEndReleasePacket",
"StepElement_CurveElementFreedom",
"StepElement_CurveElementFreedomMember",
"StepElement_CurveElementPurpose",
"StepElement_CurveElementPurposeMember",
"StepElement_CurveElementSectionDefinition",
"StepElement_CurveElementSectionDerivedDefinitions",
"StepElement_Element2dShape",
"StepElement_ElementAspect",
"StepElement_ElementAspectMember",
"StepElement_Curve3dElementDescriptor",
"StepElement_ElementMaterial",
"StepElement_ElementOrder",
"StepElement_ElementVolume",
"StepElement_EnumeratedCurveElementFreedom",
"StepElement_EnumeratedCurveElementPurpose",
"StepElement_EnumeratedSurfaceElementPurpose",
"StepElement_EnumeratedVolumeElementPurpose",
"StepElement_HArray1OfCurveElementEndReleasePacket",
"StepElement_HArray1OfCurveElementSectionDefinition",
"StepElement_HArray1OfHSequenceOfCurveElementPurposeMember",
"StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember",
"StepElement_HArray1OfMeasureOrUnspecifiedValue",
"StepElement_HArray1OfSurfaceSection",
"StepElement_HArray1OfVolumeElementPurpose",
"StepElement_HArray1OfVolumeElementPurposeMember",
"StepElement_HArray2OfCurveElementPurposeMember",
"StepElement_HArray2OfSurfaceElementPurpose",
"StepElement_HArray2OfSurfaceElementPurposeMember",
"StepElement_SequenceOfCurveElementPurposeMember",
"StepElement_SequenceOfCurveElementSectionDefinition",
"StepElement_SequenceOfElementMaterial",
"StepElement_SequenceOfSurfaceElementPurposeMember",
"StepElement_MeasureOrUnspecifiedValue",
"StepElement_MeasureOrUnspecifiedValueMember",
"StepElement_HSequenceOfCurveElementPurposeMember",
"StepElement_HSequenceOfCurveElementSectionDefinition",
"StepElement_HSequenceOfElementMaterial",
"StepElement_HSequenceOfSurfaceElementPurposeMember",
"StepElement_Surface3dElementDescriptor",
"StepElement_SurfaceElementProperty",
"StepElement_SurfaceElementPurpose",
"StepElement_SurfaceElementPurposeMember",
"StepElement_SurfaceSection",
"StepElement_SurfaceSectionField",
"StepElement_SurfaceSectionFieldConstant",
"StepElement_SurfaceSectionFieldVarying",
"StepElement_UniformSurfaceSection",
"StepElement_UnspecifiedValue",
"StepElement_Volume3dElementDescriptor",
"StepElement_Volume3dElementShape",
"StepElement_VolumeElementPurpose",
"StepElement_VolumeElementPurposeMember",
"StepElement_Axial",
"StepElement_BendingDirect",
"StepElement_BendingTorsion",
"StepElement_Cubic",
"StepElement_ElementEdge",
"StepElement_Hexahedron",
"StepElement_Linear",
"StepElement_MembraneDirect",
"StepElement_MembraneShear",
"StepElement_None",
"StepElement_NormalToPlaneShear",
"StepElement_Pyramid",
"StepElement_Quadratic",
"StepElement_Quadrilateral",
"StepElement_StressDisplacement",
"StepElement_Tetrahedron",
"StepElement_Torsion",
"StepElement_Triangle",
"StepElement_Unspecified",
"StepElement_Volume",
"StepElement_Warp",
"StepElement_Warping",
"StepElement_Wedge",
"StepElement_XRotation",
"StepElement_XTranslation",
"StepElement_XYShear",
"StepElement_XZShear",
"StepElement_YRotation",
"StepElement_YTranslation",
"StepElement_YYBending",
"StepElement_ZRotation",
"StepElement_ZTranslation",
"StepElement_ZZBending"
]
class StepElement_AnalysisItemWithinRepresentation(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity AnalysisItemWithinRepresentationRepresentation of STEP entity AnalysisItemWithinRepresentationRepresentation of STEP entity AnalysisItemWithinRepresentation
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aItem : OCP.StepRepr.StepRepr_RepresentationItem,aRep : OCP.StepRepr.StepRepr_Representation) -> None: 
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
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        Returns field Item
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def Rep(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        Returns field Rep
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetItem(self,Item : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        Set field Item
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRep(self,Rep : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        Set field Rep
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
class StepElement_Array1OfCurveElementEndReleasePacket():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepElement_Array1OfCurveElementEndReleasePacket) -> StepElement_Array1OfCurveElementEndReleasePacket: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepElement_CurveElementEndReleasePacket: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_CurveElementEndReleasePacket: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_CurveElementEndReleasePacket: 
        """
        Variable value access
        """
    def First(self) -> StepElement_CurveElementEndReleasePacket: 
        """
        Returns first element
        """
    def Init(self,theValue : StepElement_CurveElementEndReleasePacket) -> None: 
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
    def Last(self) -> StepElement_CurveElementEndReleasePacket: 
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
    def Move(self,theOther : StepElement_Array1OfCurveElementEndReleasePacket) -> StepElement_Array1OfCurveElementEndReleasePacket: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_CurveElementEndReleasePacket) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_CurveElementEndReleasePacket: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepElement_CurveElementEndReleasePacket,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfCurveElementEndReleasePacket) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepElement_Array1OfCurveElementSectionDefinition():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepElement_Array1OfCurveElementSectionDefinition) -> StepElement_Array1OfCurveElementSectionDefinition: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepElement_CurveElementSectionDefinition: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_CurveElementSectionDefinition: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_CurveElementSectionDefinition: 
        """
        Variable value access
        """
    def First(self) -> StepElement_CurveElementSectionDefinition: 
        """
        Returns first element
        """
    def Init(self,theValue : StepElement_CurveElementSectionDefinition) -> None: 
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
    def Last(self) -> StepElement_CurveElementSectionDefinition: 
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
    def Move(self,theOther : StepElement_Array1OfCurveElementSectionDefinition) -> StepElement_Array1OfCurveElementSectionDefinition: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_CurveElementSectionDefinition) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_CurveElementSectionDefinition: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfCurveElementSectionDefinition) -> None: ...
    @overload
    def __init__(self,theBegin : StepElement_CurveElementSectionDefinition,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepElement_Array1OfHSequenceOfCurveElementPurposeMember():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepElement_Array1OfHSequenceOfCurveElementPurposeMember) -> StepElement_Array1OfHSequenceOfCurveElementPurposeMember: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepElement_HSequenceOfCurveElementPurposeMember: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_HSequenceOfCurveElementPurposeMember: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_HSequenceOfCurveElementPurposeMember: 
        """
        Variable value access
        """
    def First(self) -> StepElement_HSequenceOfCurveElementPurposeMember: 
        """
        Returns first element
        """
    def Init(self,theValue : StepElement_HSequenceOfCurveElementPurposeMember) -> None: 
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
    def Last(self) -> StepElement_HSequenceOfCurveElementPurposeMember: 
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
    def Move(self,theOther : StepElement_Array1OfHSequenceOfCurveElementPurposeMember) -> StepElement_Array1OfHSequenceOfCurveElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_HSequenceOfCurveElementPurposeMember) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_HSequenceOfCurveElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepElement_HSequenceOfCurveElementPurposeMember,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfHSequenceOfCurveElementPurposeMember) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember) -> StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
        """
        Variable value access
        """
    def First(self) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
        """
        Returns first element
        """
    def Init(self,theValue : StepElement_HSequenceOfSurfaceElementPurposeMember) -> None: 
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
    def Last(self) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
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
    def Move(self,theOther : StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember) -> StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_HSequenceOfSurfaceElementPurposeMember) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepElement_HSequenceOfSurfaceElementPurposeMember,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepElement_Array1OfMeasureOrUnspecifiedValue():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepElement_Array1OfMeasureOrUnspecifiedValue) -> StepElement_Array1OfMeasureOrUnspecifiedValue: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Variable value access
        """
    def First(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns first element
        """
    def Init(self,theValue : StepElement_MeasureOrUnspecifiedValue) -> None: 
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
    def Last(self) -> StepElement_MeasureOrUnspecifiedValue: 
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
    def Move(self,theOther : StepElement_Array1OfMeasureOrUnspecifiedValue) -> StepElement_Array1OfMeasureOrUnspecifiedValue: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_MeasureOrUnspecifiedValue) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepElement_Array1OfMeasureOrUnspecifiedValue) -> None: ...
    @overload
    def __init__(self,theBegin : StepElement_MeasureOrUnspecifiedValue,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepElement_Array1OfSurfaceSection():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepElement_Array1OfSurfaceSection) -> StepElement_Array1OfSurfaceSection: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepElement_SurfaceSection: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_SurfaceSection: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_SurfaceSection: 
        """
        Variable value access
        """
    def First(self) -> StepElement_SurfaceSection: 
        """
        Returns first element
        """
    def Init(self,theValue : StepElement_SurfaceSection) -> None: 
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
    def Last(self) -> StepElement_SurfaceSection: 
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
    def Move(self,theOther : StepElement_Array1OfSurfaceSection) -> StepElement_Array1OfSurfaceSection: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_SurfaceSection) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_SurfaceSection: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfSurfaceSection) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepElement_SurfaceSection,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepElement_Array1OfVolumeElementPurpose():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepElement_Array1OfVolumeElementPurpose) -> StepElement_Array1OfVolumeElementPurpose: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepElement_VolumeElementPurpose: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_VolumeElementPurpose: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_VolumeElementPurpose: 
        """
        Variable value access
        """
    def First(self) -> StepElement_VolumeElementPurpose: 
        """
        Returns first element
        """
    def Init(self,theValue : StepElement_VolumeElementPurpose) -> None: 
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
    def Last(self) -> StepElement_VolumeElementPurpose: 
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
    def Move(self,theOther : StepElement_Array1OfVolumeElementPurpose) -> StepElement_Array1OfVolumeElementPurpose: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_VolumeElementPurpose) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_VolumeElementPurpose: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepElement_Array1OfVolumeElementPurpose) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepElement_VolumeElementPurpose,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepElement_Array1OfVolumeElementPurposeMember():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepElement_Array1OfVolumeElementPurposeMember) -> StepElement_Array1OfVolumeElementPurposeMember: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepElement_VolumeElementPurposeMember: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_VolumeElementPurposeMember: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_VolumeElementPurposeMember: 
        """
        Variable value access
        """
    def First(self) -> StepElement_VolumeElementPurposeMember: 
        """
        Returns first element
        """
    def Init(self,theValue : StepElement_VolumeElementPurposeMember) -> None: 
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
    def Last(self) -> StepElement_VolumeElementPurposeMember: 
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
    def Move(self,theOther : StepElement_Array1OfVolumeElementPurposeMember) -> StepElement_Array1OfVolumeElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_VolumeElementPurposeMember) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_VolumeElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepElement_VolumeElementPurposeMember,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfVolumeElementPurposeMember) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepElement_Array2OfCurveElementPurposeMember():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : StepElement_Array2OfCurveElementPurposeMember) -> StepElement_Array2OfCurveElementPurposeMember: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepElement_CurveElementPurposeMember: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : StepElement_CurveElementPurposeMember) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : StepElement_Array2OfCurveElementPurposeMember) -> StepElement_Array2OfCurveElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> StepElement_CurveElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepElement_Array2OfCurveElementPurposeMember) -> None: ...
    @overload
    def __init__(self,theBegin : StepElement_CurveElementPurposeMember,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class StepElement_Array2OfSurfaceElementPurpose():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : StepElement_Array2OfSurfaceElementPurpose) -> StepElement_Array2OfSurfaceElementPurpose: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepElement_SurfaceElementPurpose: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : StepElement_SurfaceElementPurpose) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : StepElement_Array2OfSurfaceElementPurpose) -> StepElement_Array2OfSurfaceElementPurpose: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : StepElement_SurfaceElementPurpose) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> StepElement_SurfaceElementPurpose: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepElement_SurfaceElementPurpose,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array2OfSurfaceElementPurpose) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class StepElement_Array2OfSurfaceElementPurposeMember():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : StepElement_Array2OfSurfaceElementPurposeMember) -> StepElement_Array2OfSurfaceElementPurposeMember: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepElement_SurfaceElementPurposeMember: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : StepElement_Array2OfSurfaceElementPurposeMember) -> StepElement_Array2OfSurfaceElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> StepElement_SurfaceElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepElement_SurfaceElementPurposeMember,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array2OfSurfaceElementPurposeMember) -> None: ...
    pass
class StepElement_ElementDescriptor(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ElementDescriptorRepresentation of STEP entity ElementDescriptorRepresentation of STEP entity ElementDescriptor
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
    def Init(self,aTopologyOrder : StepElement_ElementOrder,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetTopologyOrder(self,TopologyOrder : StepElement_ElementOrder) -> None: 
        """
        Set field TopologyOrder
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TopologyOrder(self) -> StepElement_ElementOrder: 
        """
        Returns field TopologyOrder
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
class StepElement_CurveEdge():
    """
    None

    Members:

      StepElement_ElementEdge
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
    StepElement_ElementEdge: OCP.StepElement.StepElement_CurveEdge # value = <StepElement_CurveEdge.StepElement_ElementEdge: 0>
    __entries: dict # value = {'StepElement_ElementEdge': (<StepElement_CurveEdge.StepElement_ElementEdge: 0>, None)}
    __members__: dict # value = {'StepElement_ElementEdge': <StepElement_CurveEdge.StepElement_ElementEdge: 0>}
    pass
class StepElement_CurveElementEndReleasePacket(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveElementEndReleasePacketRepresentation of STEP entity CurveElementEndReleasePacketRepresentation of STEP entity CurveElementEndReleasePacket
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
    def Init(self,aReleaseFreedom : StepElement_CurveElementFreedom,aReleaseStiffness : float) -> None: 
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
    def ReleaseFreedom(self) -> StepElement_CurveElementFreedom: 
        """
        Returns field ReleaseFreedom
        """
    def ReleaseStiffness(self) -> float: 
        """
        Returns field ReleaseStiffness
        """
    def SetReleaseFreedom(self,ReleaseFreedom : StepElement_CurveElementFreedom) -> None: 
        """
        Set field ReleaseFreedom
        """
    def SetReleaseStiffness(self,ReleaseStiffness : float) -> None: 
        """
        Set field ReleaseStiffness
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
class StepElement_CurveElementFreedom(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type CurveElementFreedom
    """
    def ApplicationDefinedDegreeOfFreedom(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Value as ApplicationDefinedDegreeOfFreedom (or Null if another type)
        """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a items of select member CurveElementFreedomMember 1 -> EnumeratedCurveElementFreedom 2 -> ApplicationDefinedDegreeOfFreedom 0 else
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of CurveElementFreedom select type return 0
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def EnumeratedCurveElementFreedom(self) -> StepElement_EnumeratedCurveElementFreedom: 
        """
        Returns Value as EnumeratedCurveElementFreedom (or Null if another type)
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
        Returns a new select member the type CurveElementFreedomMember
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
    def SetApplicationDefinedDegreeOfFreedom(self,aVal : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set Value for ApplicationDefinedDegreeOfFreedom
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetEnumeratedCurveElementFreedom(self,aVal : StepElement_EnumeratedCurveElementFreedom) -> None: 
        """
        Set Value for EnumeratedCurveElementFreedom
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
class StepElement_CurveElementFreedomMember(OCP.StepData.StepData_SelectNamed, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Representation of member for STEP SELECT type CurveElementFreedomRepresentation of member for STEP SELECT type CurveElementFreedomRepresentation of member for STEP SELECT type CurveElementFreedom
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CField(self) -> OCP.StepData.StepData_Field: 
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
    def Field(self) -> OCP.StepData.StepData_Field: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        Returns True if has name
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one;
        """
    def Name(self) -> str: 
        """
        Returns set name
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        Set name
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
class StepElement_CurveElementPurpose(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type CurveElementPurpose
    """
    def ApplicationDefinedElementPurpose(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Value as ApplicationDefinedElementPurpose (or Null if another type)
        """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a items of select member CurveElementPurposeMember 1 -> EnumeratedCurveElementPurpose 2 -> ApplicationDefinedElementPurpose 0 else
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of CurveElementPurpose select type return 0
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def EnumeratedCurveElementPurpose(self) -> StepElement_EnumeratedCurveElementPurpose: 
        """
        Returns Value as EnumeratedCurveElementPurpose (or Null if another type)
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
        Returns a new select member the type CurveElementPurposeMember
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
    def SetApplicationDefinedElementPurpose(self,aVal : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set Value for ApplicationDefinedElementPurpose
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetEnumeratedCurveElementPurpose(self,aVal : StepElement_EnumeratedCurveElementPurpose) -> None: 
        """
        Set Value for EnumeratedCurveElementPurpose
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
class StepElement_CurveElementPurposeMember(OCP.StepData.StepData_SelectNamed, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Representation of member for STEP SELECT type CurveElementPurposeRepresentation of member for STEP SELECT type CurveElementPurposeRepresentation of member for STEP SELECT type CurveElementPurpose
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CField(self) -> OCP.StepData.StepData_Field: 
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
    def Field(self) -> OCP.StepData.StepData_Field: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        Returns True if has name
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one;
        """
    def Name(self) -> str: 
        """
        Returns set name
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        Set name
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
class StepElement_CurveElementSectionDefinition(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveElementSectionDefinitionRepresentation of STEP entity CurveElementSectionDefinitionRepresentation of STEP entity CurveElementSectionDefinition
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
    def Init(self,aDescription : OCP.TCollection.TCollection_HAsciiString,aSectionAngle : float) -> None: 
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
    def SectionAngle(self) -> float: 
        """
        Returns field SectionAngle
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetSectionAngle(self,SectionAngle : float) -> None: 
        """
        Set field SectionAngle
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
class StepElement_CurveElementSectionDerivedDefinitions(StepElement_CurveElementSectionDefinition, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveElementSectionDerivedDefinitionsRepresentation of STEP entity CurveElementSectionDerivedDefinitionsRepresentation of STEP entity CurveElementSectionDerivedDefinitions
    """
    def CrossSectionalArea(self) -> float: 
        """
        Returns field CrossSectionalArea
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
    def Init(self,aCurveElementSectionDefinition_Description : OCP.TCollection.TCollection_HAsciiString,aCurveElementSectionDefinition_SectionAngle : float,aCrossSectionalArea : float,aShearArea : StepElement_HArray1OfMeasureOrUnspecifiedValue,aSecondMomentOfArea : OCP.TColStd.TColStd_HArray1OfReal,aTorsionalConstant : float,aWarpingConstant : StepElement_MeasureOrUnspecifiedValue,aLocationOfCentroid : StepElement_HArray1OfMeasureOrUnspecifiedValue,aLocationOfShearCentre : StepElement_HArray1OfMeasureOrUnspecifiedValue,aLocationOfNonStructuralMass : StepElement_HArray1OfMeasureOrUnspecifiedValue,aNonStructuralMass : StepElement_MeasureOrUnspecifiedValue,aPolarMoment : StepElement_MeasureOrUnspecifiedValue) -> None: 
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
    def LocationOfCentroid(self) -> StepElement_HArray1OfMeasureOrUnspecifiedValue: 
        """
        Returns field LocationOfCentroid
        """
    def LocationOfNonStructuralMass(self) -> StepElement_HArray1OfMeasureOrUnspecifiedValue: 
        """
        Returns field LocationOfNonStructuralMass
        """
    def LocationOfShearCentre(self) -> StepElement_HArray1OfMeasureOrUnspecifiedValue: 
        """
        Returns field LocationOfShearCentre
        """
    def NonStructuralMass(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field NonStructuralMass
        """
    def PolarMoment(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field PolarMoment
        """
    def SecondMomentOfArea(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns field SecondMomentOfArea
        """
    def SectionAngle(self) -> float: 
        """
        Returns field SectionAngle
        """
    def SetCrossSectionalArea(self,CrossSectionalArea : float) -> None: 
        """
        Set field CrossSectionalArea
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetLocationOfCentroid(self,LocationOfCentroid : StepElement_HArray1OfMeasureOrUnspecifiedValue) -> None: 
        """
        Set field LocationOfCentroid
        """
    def SetLocationOfNonStructuralMass(self,LocationOfNonStructuralMass : StepElement_HArray1OfMeasureOrUnspecifiedValue) -> None: 
        """
        Set field LocationOfNonStructuralMass
        """
    def SetLocationOfShearCentre(self,LocationOfShearCentre : StepElement_HArray1OfMeasureOrUnspecifiedValue) -> None: 
        """
        Set field LocationOfShearCentre
        """
    def SetNonStructuralMass(self,NonStructuralMass : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field NonStructuralMass
        """
    def SetPolarMoment(self,PolarMoment : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field PolarMoment
        """
    def SetSecondMomentOfArea(self,SecondMomentOfArea : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Set field SecondMomentOfArea
        """
    def SetSectionAngle(self,SectionAngle : float) -> None: 
        """
        Set field SectionAngle
        """
    def SetShearArea(self,ShearArea : StepElement_HArray1OfMeasureOrUnspecifiedValue) -> None: 
        """
        Set field ShearArea
        """
    def SetTorsionalConstant(self,TorsionalConstant : float) -> None: 
        """
        Set field TorsionalConstant
        """
    def SetWarpingConstant(self,WarpingConstant : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field WarpingConstant
        """
    def ShearArea(self) -> StepElement_HArray1OfMeasureOrUnspecifiedValue: 
        """
        Returns field ShearArea
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TorsionalConstant(self) -> float: 
        """
        Returns field TorsionalConstant
        """
    def WarpingConstant(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field WarpingConstant
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
class StepElement_Element2dShape():
    """
    None

    Members:

      StepElement_Quadrilateral

      StepElement_Triangle
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
    StepElement_Quadrilateral: OCP.StepElement.StepElement_Element2dShape # value = <StepElement_Element2dShape.StepElement_Quadrilateral: 0>
    StepElement_Triangle: OCP.StepElement.StepElement_Element2dShape # value = <StepElement_Element2dShape.StepElement_Triangle: 1>
    __entries: dict # value = {'StepElement_Quadrilateral': (<StepElement_Element2dShape.StepElement_Quadrilateral: 0>, None), 'StepElement_Triangle': (<StepElement_Element2dShape.StepElement_Triangle: 1>, None)}
    __members__: dict # value = {'StepElement_Quadrilateral': <StepElement_Element2dShape.StepElement_Quadrilateral: 0>, 'StepElement_Triangle': <StepElement_Element2dShape.StepElement_Triangle: 1>}
    pass
class StepElement_ElementAspect(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type ElementAspect
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a items of select member ElementAspectMember 1 -> ElementVolume 2 -> Volume3dFace 3 -> Volume2dFace 4 -> Volume3dEdge 5 -> Volume2dEdge 6 -> Surface3dFace 7 -> Surface2dFace 8 -> Surface3dEdge 9 -> Surface2dEdge 10 -> CurveEdge 0 else
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of ElementAspect select type return 0
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CurveEdge(self) -> StepElement_CurveEdge: 
        """
        Returns Value as CurveEdge (or Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def ElementVolume(self) -> StepElement_ElementVolume: 
        """
        Returns Value as ElementVolume (or Null if another type)
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
        Returns a new select member the type ElementAspectMember
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
    def SetCurveEdge(self,aVal : StepElement_CurveEdge) -> None: 
        """
        Set Value for CurveEdge
        """
    def SetElementVolume(self,aVal : StepElement_ElementVolume) -> None: 
        """
        Set Value for ElementVolume
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
    def SetSurface2dEdge(self,aVal : int) -> None: 
        """
        Set Value for Surface2dEdge
        """
    def SetSurface2dFace(self,aVal : int) -> None: 
        """
        Set Value for Surface2dFace
        """
    def SetSurface3dEdge(self,aVal : int) -> None: 
        """
        Set Value for Surface3dEdge
        """
    def SetSurface3dFace(self,aVal : int) -> None: 
        """
        Set Value for Surface3dFace
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def SetVolume2dEdge(self,aVal : int) -> None: 
        """
        Set Value for Volume2dEdge
        """
    def SetVolume2dFace(self,aVal : int) -> None: 
        """
        Set Value for Volume2dFace
        """
    def SetVolume3dEdge(self,aVal : int) -> None: 
        """
        Set Value for Volume3dEdge
        """
    def SetVolume3dFace(self,aVal : int) -> None: 
        """
        Set Value for Volume3dFace
        """
    def Surface2dEdge(self) -> int: 
        """
        Returns Value as Surface2dEdge (or Null if another type)
        """
    def Surface2dFace(self) -> int: 
        """
        Returns Value as Surface2dFace (or Null if another type)
        """
    def Surface3dEdge(self) -> int: 
        """
        Returns Value as Surface3dEdge (or Null if another type)
        """
    def Surface3dFace(self) -> int: 
        """
        Returns Value as Surface3dFace (or Null if another type)
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def Volume2dEdge(self) -> int: 
        """
        Returns Value as Volume2dEdge (or Null if another type)
        """
    def Volume2dFace(self) -> int: 
        """
        Returns Value as Volume2dFace (or Null if another type)
        """
    def Volume3dEdge(self) -> int: 
        """
        Returns Value as Volume3dEdge (or Null if another type)
        """
    def Volume3dFace(self) -> int: 
        """
        Returns Value as Volume3dFace (or Null if another type)
        """
    def __init__(self) -> None: ...
    pass
class StepElement_ElementAspectMember(OCP.StepData.StepData_SelectNamed, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Representation of member for STEP SELECT type ElementAspectRepresentation of member for STEP SELECT type ElementAspectRepresentation of member for STEP SELECT type ElementAspect
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CField(self) -> OCP.StepData.StepData_Field: 
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
    def Field(self) -> OCP.StepData.StepData_Field: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        Returns True if has name
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one;
        """
    def Name(self) -> str: 
        """
        Returns set name
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        Set name
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
class StepElement_Curve3dElementDescriptor(StepElement_ElementDescriptor, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity Curve3dElementDescriptorRepresentation of STEP entity Curve3dElementDescriptorRepresentation of STEP entity Curve3dElementDescriptor
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
    def Init(self,aElementDescriptor_TopologyOrder : StepElement_ElementOrder,aElementDescriptor_Description : OCP.TCollection.TCollection_HAsciiString,aPurpose : StepElement_HArray1OfHSequenceOfCurveElementPurposeMember) -> None: 
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
    def Purpose(self) -> StepElement_HArray1OfHSequenceOfCurveElementPurposeMember: 
        """
        Returns field Purpose
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetPurpose(self,Purpose : StepElement_HArray1OfHSequenceOfCurveElementPurposeMember) -> None: 
        """
        Set field Purpose
        """
    def SetTopologyOrder(self,TopologyOrder : StepElement_ElementOrder) -> None: 
        """
        Set field TopologyOrder
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TopologyOrder(self) -> StepElement_ElementOrder: 
        """
        Returns field TopologyOrder
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
class StepElement_ElementMaterial(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ElementMaterialRepresentation of STEP entity ElementMaterialRepresentation of STEP entity ElementMaterial
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
    def Init(self,aMaterialId : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aProperties : OCP.StepRepr.StepRepr_HArray1OfMaterialPropertyRepresentation) -> None: 
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
    def MaterialId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field MaterialId
        """
    def Properties(self) -> OCP.StepRepr.StepRepr_HArray1OfMaterialPropertyRepresentation: 
        """
        Returns field Properties
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMaterialId(self,MaterialId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field MaterialId
        """
    def SetProperties(self,Properties : OCP.StepRepr.StepRepr_HArray1OfMaterialPropertyRepresentation) -> None: 
        """
        Set field Properties
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
class StepElement_ElementOrder():
    """
    None

    Members:

      StepElement_Linear

      StepElement_Quadratic

      StepElement_Cubic
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
    StepElement_Cubic: OCP.StepElement.StepElement_ElementOrder # value = <StepElement_ElementOrder.StepElement_Cubic: 2>
    StepElement_Linear: OCP.StepElement.StepElement_ElementOrder # value = <StepElement_ElementOrder.StepElement_Linear: 0>
    StepElement_Quadratic: OCP.StepElement.StepElement_ElementOrder # value = <StepElement_ElementOrder.StepElement_Quadratic: 1>
    __entries: dict # value = {'StepElement_Linear': (<StepElement_ElementOrder.StepElement_Linear: 0>, None), 'StepElement_Quadratic': (<StepElement_ElementOrder.StepElement_Quadratic: 1>, None), 'StepElement_Cubic': (<StepElement_ElementOrder.StepElement_Cubic: 2>, None)}
    __members__: dict # value = {'StepElement_Linear': <StepElement_ElementOrder.StepElement_Linear: 0>, 'StepElement_Quadratic': <StepElement_ElementOrder.StepElement_Quadratic: 1>, 'StepElement_Cubic': <StepElement_ElementOrder.StepElement_Cubic: 2>}
    pass
class StepElement_ElementVolume():
    """
    None

    Members:

      StepElement_Volume
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
    StepElement_Volume: OCP.StepElement.StepElement_ElementVolume # value = <StepElement_ElementVolume.StepElement_Volume: 0>
    __entries: dict # value = {'StepElement_Volume': (<StepElement_ElementVolume.StepElement_Volume: 0>, None)}
    __members__: dict # value = {'StepElement_Volume': <StepElement_ElementVolume.StepElement_Volume: 0>}
    pass
class StepElement_EnumeratedCurveElementFreedom():
    """
    None

    Members:

      StepElement_XTranslation

      StepElement_YTranslation

      StepElement_ZTranslation

      StepElement_XRotation

      StepElement_YRotation

      StepElement_ZRotation

      StepElement_Warp

      StepElement_None
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
    StepElement_None: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_None: 7>
    StepElement_Warp: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_Warp: 6>
    StepElement_XRotation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_XRotation: 3>
    StepElement_XTranslation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_XTranslation: 0>
    StepElement_YRotation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_YRotation: 4>
    StepElement_YTranslation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_YTranslation: 1>
    StepElement_ZRotation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_ZRotation: 5>
    StepElement_ZTranslation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_ZTranslation: 2>
    __entries: dict # value = {'StepElement_XTranslation': (<StepElement_EnumeratedCurveElementFreedom.StepElement_XTranslation: 0>, None), 'StepElement_YTranslation': (<StepElement_EnumeratedCurveElementFreedom.StepElement_YTranslation: 1>, None), 'StepElement_ZTranslation': (<StepElement_EnumeratedCurveElementFreedom.StepElement_ZTranslation: 2>, None), 'StepElement_XRotation': (<StepElement_EnumeratedCurveElementFreedom.StepElement_XRotation: 3>, None), 'StepElement_YRotation': (<StepElement_EnumeratedCurveElementFreedom.StepElement_YRotation: 4>, None), 'StepElement_ZRotation': (<StepElement_EnumeratedCurveElementFreedom.StepElement_ZRotation: 5>, None), 'StepElement_Warp': (<StepElement_EnumeratedCurveElementFreedom.StepElement_Warp: 6>, None), 'StepElement_None': (<StepElement_EnumeratedCurveElementFreedom.StepElement_None: 7>, None)}
    __members__: dict # value = {'StepElement_XTranslation': <StepElement_EnumeratedCurveElementFreedom.StepElement_XTranslation: 0>, 'StepElement_YTranslation': <StepElement_EnumeratedCurveElementFreedom.StepElement_YTranslation: 1>, 'StepElement_ZTranslation': <StepElement_EnumeratedCurveElementFreedom.StepElement_ZTranslation: 2>, 'StepElement_XRotation': <StepElement_EnumeratedCurveElementFreedom.StepElement_XRotation: 3>, 'StepElement_YRotation': <StepElement_EnumeratedCurveElementFreedom.StepElement_YRotation: 4>, 'StepElement_ZRotation': <StepElement_EnumeratedCurveElementFreedom.StepElement_ZRotation: 5>, 'StepElement_Warp': <StepElement_EnumeratedCurveElementFreedom.StepElement_Warp: 6>, 'StepElement_None': <StepElement_EnumeratedCurveElementFreedom.StepElement_None: 7>}
    pass
class StepElement_EnumeratedCurveElementPurpose():
    """
    None

    Members:

      StepElement_Axial

      StepElement_YYBending

      StepElement_ZZBending

      StepElement_Torsion

      StepElement_XYShear

      StepElement_XZShear

      StepElement_Warping
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
    StepElement_Axial: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_Axial: 0>
    StepElement_Torsion: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_Torsion: 3>
    StepElement_Warping: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_Warping: 6>
    StepElement_XYShear: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_XYShear: 4>
    StepElement_XZShear: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_XZShear: 5>
    StepElement_YYBending: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_YYBending: 1>
    StepElement_ZZBending: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_ZZBending: 2>
    __entries: dict # value = {'StepElement_Axial': (<StepElement_EnumeratedCurveElementPurpose.StepElement_Axial: 0>, None), 'StepElement_YYBending': (<StepElement_EnumeratedCurveElementPurpose.StepElement_YYBending: 1>, None), 'StepElement_ZZBending': (<StepElement_EnumeratedCurveElementPurpose.StepElement_ZZBending: 2>, None), 'StepElement_Torsion': (<StepElement_EnumeratedCurveElementPurpose.StepElement_Torsion: 3>, None), 'StepElement_XYShear': (<StepElement_EnumeratedCurveElementPurpose.StepElement_XYShear: 4>, None), 'StepElement_XZShear': (<StepElement_EnumeratedCurveElementPurpose.StepElement_XZShear: 5>, None), 'StepElement_Warping': (<StepElement_EnumeratedCurveElementPurpose.StepElement_Warping: 6>, None)}
    __members__: dict # value = {'StepElement_Axial': <StepElement_EnumeratedCurveElementPurpose.StepElement_Axial: 0>, 'StepElement_YYBending': <StepElement_EnumeratedCurveElementPurpose.StepElement_YYBending: 1>, 'StepElement_ZZBending': <StepElement_EnumeratedCurveElementPurpose.StepElement_ZZBending: 2>, 'StepElement_Torsion': <StepElement_EnumeratedCurveElementPurpose.StepElement_Torsion: 3>, 'StepElement_XYShear': <StepElement_EnumeratedCurveElementPurpose.StepElement_XYShear: 4>, 'StepElement_XZShear': <StepElement_EnumeratedCurveElementPurpose.StepElement_XZShear: 5>, 'StepElement_Warping': <StepElement_EnumeratedCurveElementPurpose.StepElement_Warping: 6>}
    pass
class StepElement_EnumeratedSurfaceElementPurpose():
    """
    None

    Members:

      StepElement_MembraneDirect

      StepElement_MembraneShear

      StepElement_BendingDirect

      StepElement_BendingTorsion

      StepElement_NormalToPlaneShear
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
    StepElement_BendingDirect: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingDirect: 2>
    StepElement_BendingTorsion: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingTorsion: 3>
    StepElement_MembraneDirect: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneDirect: 0>
    StepElement_MembraneShear: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneShear: 1>
    StepElement_NormalToPlaneShear: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_NormalToPlaneShear: 4>
    __entries: dict # value = {'StepElement_MembraneDirect': (<StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneDirect: 0>, None), 'StepElement_MembraneShear': (<StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneShear: 1>, None), 'StepElement_BendingDirect': (<StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingDirect: 2>, None), 'StepElement_BendingTorsion': (<StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingTorsion: 3>, None), 'StepElement_NormalToPlaneShear': (<StepElement_EnumeratedSurfaceElementPurpose.StepElement_NormalToPlaneShear: 4>, None)}
    __members__: dict # value = {'StepElement_MembraneDirect': <StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneDirect: 0>, 'StepElement_MembraneShear': <StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneShear: 1>, 'StepElement_BendingDirect': <StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingDirect: 2>, 'StepElement_BendingTorsion': <StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingTorsion: 3>, 'StepElement_NormalToPlaneShear': <StepElement_EnumeratedSurfaceElementPurpose.StepElement_NormalToPlaneShear: 4>}
    pass
class StepElement_EnumeratedVolumeElementPurpose():
    """
    None

    Members:

      StepElement_StressDisplacement
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
    StepElement_StressDisplacement: OCP.StepElement.StepElement_EnumeratedVolumeElementPurpose # value = <StepElement_EnumeratedVolumeElementPurpose.StepElement_StressDisplacement: 0>
    __entries: dict # value = {'StepElement_StressDisplacement': (<StepElement_EnumeratedVolumeElementPurpose.StepElement_StressDisplacement: 0>, None)}
    __members__: dict # value = {'StepElement_StressDisplacement': <StepElement_EnumeratedVolumeElementPurpose.StepElement_StressDisplacement: 0>}
    pass
class StepElement_HArray1OfCurveElementEndReleasePacket(StepElement_Array1OfCurveElementEndReleasePacket, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepElement_Array1OfCurveElementEndReleasePacket: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array1OfCurveElementEndReleasePacket) -> StepElement_Array1OfCurveElementEndReleasePacket: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepElement_Array1OfCurveElementEndReleasePacket: 
        """
        None
        """
    def ChangeFirst(self) -> StepElement_CurveElementEndReleasePacket: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_CurveElementEndReleasePacket: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_CurveElementEndReleasePacket: 
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
    def First(self) -> StepElement_CurveElementEndReleasePacket: 
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
    def Init(self,theValue : StepElement_CurveElementEndReleasePacket) -> None: 
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
    def Last(self) -> StepElement_CurveElementEndReleasePacket: 
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
    def Move(self,theOther : StepElement_Array1OfCurveElementEndReleasePacket) -> StepElement_Array1OfCurveElementEndReleasePacket: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_CurveElementEndReleasePacket) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_CurveElementEndReleasePacket: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepElement_CurveElementEndReleasePacket) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfCurveElementEndReleasePacket) -> None: ...
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
class StepElement_HArray1OfCurveElementSectionDefinition(StepElement_Array1OfCurveElementSectionDefinition, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepElement_Array1OfCurveElementSectionDefinition: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array1OfCurveElementSectionDefinition) -> StepElement_Array1OfCurveElementSectionDefinition: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepElement_Array1OfCurveElementSectionDefinition: 
        """
        None
        """
    def ChangeFirst(self) -> StepElement_CurveElementSectionDefinition: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_CurveElementSectionDefinition: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_CurveElementSectionDefinition: 
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
    def First(self) -> StepElement_CurveElementSectionDefinition: 
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
    def Init(self,theValue : StepElement_CurveElementSectionDefinition) -> None: 
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
    def Last(self) -> StepElement_CurveElementSectionDefinition: 
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
    def Move(self,theOther : StepElement_Array1OfCurveElementSectionDefinition) -> StepElement_Array1OfCurveElementSectionDefinition: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_CurveElementSectionDefinition) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_CurveElementSectionDefinition: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfCurveElementSectionDefinition) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepElement_CurveElementSectionDefinition) -> None: ...
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
class StepElement_HArray1OfHSequenceOfCurveElementPurposeMember(StepElement_Array1OfHSequenceOfCurveElementPurposeMember, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepElement_Array1OfHSequenceOfCurveElementPurposeMember: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array1OfHSequenceOfCurveElementPurposeMember) -> StepElement_Array1OfHSequenceOfCurveElementPurposeMember: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepElement_Array1OfHSequenceOfCurveElementPurposeMember: 
        """
        None
        """
    def ChangeFirst(self) -> StepElement_HSequenceOfCurveElementPurposeMember: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_HSequenceOfCurveElementPurposeMember: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_HSequenceOfCurveElementPurposeMember: 
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
    def First(self) -> StepElement_HSequenceOfCurveElementPurposeMember: 
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
    def Init(self,theValue : StepElement_HSequenceOfCurveElementPurposeMember) -> None: 
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
    def Last(self) -> StepElement_HSequenceOfCurveElementPurposeMember: 
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
    def Move(self,theOther : StepElement_Array1OfHSequenceOfCurveElementPurposeMember) -> StepElement_Array1OfHSequenceOfCurveElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_HSequenceOfCurveElementPurposeMember) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_HSequenceOfCurveElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfHSequenceOfCurveElementPurposeMember) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepElement_HSequenceOfCurveElementPurposeMember) -> None: ...
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
class StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember(StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember) -> StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember: 
        """
        None
        """
    def ChangeFirst(self) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
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
    def First(self) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
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
    def Init(self,theValue : StepElement_HSequenceOfSurfaceElementPurposeMember) -> None: 
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
    def Last(self) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
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
    def Move(self,theOther : StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember) -> StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_HSequenceOfSurfaceElementPurposeMember) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_HSequenceOfSurfaceElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepElement_HSequenceOfSurfaceElementPurposeMember) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember) -> None: ...
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
class StepElement_HArray1OfMeasureOrUnspecifiedValue(StepElement_Array1OfMeasureOrUnspecifiedValue, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepElement_Array1OfMeasureOrUnspecifiedValue: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array1OfMeasureOrUnspecifiedValue) -> StepElement_Array1OfMeasureOrUnspecifiedValue: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepElement_Array1OfMeasureOrUnspecifiedValue: 
        """
        None
        """
    def ChangeFirst(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_MeasureOrUnspecifiedValue: 
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
    def First(self) -> StepElement_MeasureOrUnspecifiedValue: 
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
    def Init(self,theValue : StepElement_MeasureOrUnspecifiedValue) -> None: 
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
    def Last(self) -> StepElement_MeasureOrUnspecifiedValue: 
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
    def Move(self,theOther : StepElement_Array1OfMeasureOrUnspecifiedValue) -> StepElement_Array1OfMeasureOrUnspecifiedValue: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_MeasureOrUnspecifiedValue) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfMeasureOrUnspecifiedValue) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepElement_MeasureOrUnspecifiedValue) -> None: ...
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
class StepElement_HArray1OfSurfaceSection(StepElement_Array1OfSurfaceSection, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepElement_Array1OfSurfaceSection: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array1OfSurfaceSection) -> StepElement_Array1OfSurfaceSection: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepElement_Array1OfSurfaceSection: 
        """
        None
        """
    def ChangeFirst(self) -> StepElement_SurfaceSection: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_SurfaceSection: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_SurfaceSection: 
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
    def First(self) -> StepElement_SurfaceSection: 
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
    def Init(self,theValue : StepElement_SurfaceSection) -> None: 
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
    def Last(self) -> StepElement_SurfaceSection: 
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
    def Move(self,theOther : StepElement_Array1OfSurfaceSection) -> StepElement_Array1OfSurfaceSection: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_SurfaceSection) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_SurfaceSection: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepElement_SurfaceSection) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfSurfaceSection) -> None: ...
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
class StepElement_HArray1OfVolumeElementPurpose(StepElement_Array1OfVolumeElementPurpose, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepElement_Array1OfVolumeElementPurpose: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array1OfVolumeElementPurpose) -> StepElement_Array1OfVolumeElementPurpose: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepElement_Array1OfVolumeElementPurpose: 
        """
        None
        """
    def ChangeFirst(self) -> StepElement_VolumeElementPurpose: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_VolumeElementPurpose: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_VolumeElementPurpose: 
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
    def First(self) -> StepElement_VolumeElementPurpose: 
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
    def Init(self,theValue : StepElement_VolumeElementPurpose) -> None: 
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
    def Last(self) -> StepElement_VolumeElementPurpose: 
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
    def Move(self,theOther : StepElement_Array1OfVolumeElementPurpose) -> StepElement_Array1OfVolumeElementPurpose: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_VolumeElementPurpose) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_VolumeElementPurpose: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepElement_Array1OfVolumeElementPurpose) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepElement_VolumeElementPurpose) -> None: ...
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
class StepElement_HArray1OfVolumeElementPurposeMember(StepElement_Array1OfVolumeElementPurposeMember, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepElement_Array1OfVolumeElementPurposeMember: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array1OfVolumeElementPurposeMember) -> StepElement_Array1OfVolumeElementPurposeMember: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepElement_Array1OfVolumeElementPurposeMember: 
        """
        None
        """
    def ChangeFirst(self) -> StepElement_VolumeElementPurposeMember: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepElement_VolumeElementPurposeMember: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepElement_VolumeElementPurposeMember: 
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
    def First(self) -> StepElement_VolumeElementPurposeMember: 
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
    def Init(self,theValue : StepElement_VolumeElementPurposeMember) -> None: 
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
    def Last(self) -> StepElement_VolumeElementPurposeMember: 
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
    def Move(self,theOther : StepElement_Array1OfVolumeElementPurposeMember) -> StepElement_Array1OfVolumeElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepElement_VolumeElementPurposeMember) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_VolumeElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array1OfVolumeElementPurposeMember) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepElement_VolumeElementPurposeMember) -> None: ...
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
class StepElement_HArray2OfCurveElementPurposeMember(StepElement_Array2OfCurveElementPurposeMember, OCP.Standard.Standard_Transient):
    def Array2(self) -> StepElement_Array2OfCurveElementPurposeMember: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array2OfCurveElementPurposeMember) -> StepElement_Array2OfCurveElementPurposeMember: 
        """
        Assignment
        """
    def ChangeArray2(self) -> StepElement_Array2OfCurveElementPurposeMember: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepElement_CurveElementPurposeMember: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
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
    def Init(self,theValue : StepElement_CurveElementPurposeMember) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
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
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : StepElement_Array2OfCurveElementPurposeMember) -> StepElement_Array2OfCurveElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> StepElement_CurveElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepElement_Array2OfCurveElementPurposeMember) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : StepElement_CurveElementPurposeMember) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepElement_HArray2OfSurfaceElementPurpose(StepElement_Array2OfSurfaceElementPurpose, OCP.Standard.Standard_Transient):
    def Array2(self) -> StepElement_Array2OfSurfaceElementPurpose: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array2OfSurfaceElementPurpose) -> StepElement_Array2OfSurfaceElementPurpose: 
        """
        Assignment
        """
    def ChangeArray2(self) -> StepElement_Array2OfSurfaceElementPurpose: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepElement_SurfaceElementPurpose: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
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
    def Init(self,theValue : StepElement_SurfaceElementPurpose) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
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
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : StepElement_Array2OfSurfaceElementPurpose) -> StepElement_Array2OfSurfaceElementPurpose: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : StepElement_SurfaceElementPurpose) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> StepElement_SurfaceElementPurpose: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : StepElement_SurfaceElementPurpose) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array2OfSurfaceElementPurpose) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepElement_HArray2OfSurfaceElementPurposeMember(StepElement_Array2OfSurfaceElementPurposeMember, OCP.Standard.Standard_Transient):
    def Array2(self) -> StepElement_Array2OfSurfaceElementPurposeMember: 
        """
        None
        """
    def Assign(self,theOther : StepElement_Array2OfSurfaceElementPurposeMember) -> StepElement_Array2OfSurfaceElementPurposeMember: 
        """
        Assignment
        """
    def ChangeArray2(self) -> StepElement_Array2OfSurfaceElementPurposeMember: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepElement_SurfaceElementPurposeMember: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
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
    def Init(self,theValue : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
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
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : StepElement_Array2OfSurfaceElementPurposeMember) -> StepElement_Array2OfSurfaceElementPurposeMember: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> StepElement_SurfaceElementPurposeMember: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : StepElement_SurfaceElementPurposeMember) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_Array2OfSurfaceElementPurposeMember) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepElement_SequenceOfCurveElementPurposeMember(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : StepElement_SequenceOfCurveElementPurposeMember) -> None: ...
    def Assign(self,theOther : StepElement_SequenceOfCurveElementPurposeMember) -> StepElement_SequenceOfCurveElementPurposeMember: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepElement_CurveElementPurposeMember: 
        """
        First item access
        """
    def ChangeLast(self) -> StepElement_CurveElementPurposeMember: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepElement_CurveElementPurposeMember: 
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
    def First(self) -> StepElement_CurveElementPurposeMember: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementPurposeMember) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementPurposeMember) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepElement_CurveElementPurposeMember: 
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
    def Prepend(self,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepElement_SequenceOfCurveElementPurposeMember) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementPurposeMember) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepElement_CurveElementPurposeMember: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StepElement_SequenceOfCurveElementPurposeMember) -> None: ...
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
class StepElement_SequenceOfCurveElementSectionDefinition(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : StepElement_SequenceOfCurveElementSectionDefinition) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : StepElement_CurveElementSectionDefinition) -> None: ...
    def Assign(self,theOther : StepElement_SequenceOfCurveElementSectionDefinition) -> StepElement_SequenceOfCurveElementSectionDefinition: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepElement_CurveElementSectionDefinition: 
        """
        First item access
        """
    def ChangeLast(self) -> StepElement_CurveElementSectionDefinition: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepElement_CurveElementSectionDefinition: 
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
    def First(self) -> StepElement_CurveElementSectionDefinition: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepElement_CurveElementSectionDefinition) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementSectionDefinition) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepElement_CurveElementSectionDefinition) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementSectionDefinition) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepElement_CurveElementSectionDefinition: 
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
    def Prepend(self,theItem : StepElement_CurveElementSectionDefinition) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepElement_SequenceOfCurveElementSectionDefinition) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : StepElement_CurveElementSectionDefinition) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementSectionDefinition) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepElement_CurveElementSectionDefinition: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_SequenceOfCurveElementSectionDefinition) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StepElement_SequenceOfElementMaterial(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepElement_ElementMaterial) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : StepElement_SequenceOfElementMaterial) -> None: ...
    def Assign(self,theOther : StepElement_SequenceOfElementMaterial) -> StepElement_SequenceOfElementMaterial: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepElement_ElementMaterial: 
        """
        First item access
        """
    def ChangeLast(self) -> StepElement_ElementMaterial: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepElement_ElementMaterial: 
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
    def First(self) -> StepElement_ElementMaterial: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepElement_ElementMaterial) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepElement_SequenceOfElementMaterial) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepElement_SequenceOfElementMaterial) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepElement_ElementMaterial) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepElement_ElementMaterial: 
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
    def Prepend(self,theSeq : StepElement_SequenceOfElementMaterial) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : StepElement_ElementMaterial) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StepElement_ElementMaterial) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepElement_SequenceOfElementMaterial) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepElement_ElementMaterial: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_SequenceOfElementMaterial) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StepElement_SequenceOfSurfaceElementPurposeMember(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: ...
    def Assign(self,theOther : StepElement_SequenceOfSurfaceElementPurposeMember) -> StepElement_SequenceOfSurfaceElementPurposeMember: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepElement_SurfaceElementPurposeMember: 
        """
        First item access
        """
    def ChangeLast(self) -> StepElement_SurfaceElementPurposeMember: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepElement_SurfaceElementPurposeMember: 
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
    def First(self) -> StepElement_SurfaceElementPurposeMember: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepElement_SurfaceElementPurposeMember) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepElement_SurfaceElementPurposeMember: 
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
    def Prepend(self,theItem : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepElement_SurfaceElementPurposeMember: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StepElement_MeasureOrUnspecifiedValue(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type MeasureOrUnspecifiedValue
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a items of select member MeasureOrUnspecifiedValueMember 1 -> ContextDependentMeasure 2 -> UnspecifiedValue 0 else
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of MeasureOrUnspecifiedValue select type return 0
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def ContextDependentMeasure(self) -> float: 
        """
        Returns Value as ContextDependentMeasure (or Null if another type)
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
        Returns a new select member the type MeasureOrUnspecifiedValueMember
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
    def SetContextDependentMeasure(self,aVal : float) -> None: 
        """
        Set Value for ContextDependentMeasure
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
    def SetUnspecifiedValue(self,aVal : StepElement_UnspecifiedValue) -> None: 
        """
        Set Value for UnspecifiedValue
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def UnspecifiedValue(self) -> StepElement_UnspecifiedValue: 
        """
        Returns Value as UnspecifiedValue (or Null if another type)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepElement_MeasureOrUnspecifiedValueMember(OCP.StepData.StepData_SelectNamed, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Representation of member for STEP SELECT type MeasureOrUnspecifiedValueRepresentation of member for STEP SELECT type MeasureOrUnspecifiedValueRepresentation of member for STEP SELECT type MeasureOrUnspecifiedValue
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CField(self) -> OCP.StepData.StepData_Field: 
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
    def Field(self) -> OCP.StepData.StepData_Field: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        Returns True if has name
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one;
        """
    def Name(self) -> str: 
        """
        Returns set name
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        Set name
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
class StepElement_HSequenceOfCurveElementPurposeMember(StepElement_SequenceOfCurveElementPurposeMember, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : StepElement_SequenceOfCurveElementPurposeMember) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : StepElement_CurveElementPurposeMember) -> None: ...
    def Assign(self,theOther : StepElement_SequenceOfCurveElementPurposeMember) -> StepElement_SequenceOfCurveElementPurposeMember: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepElement_CurveElementPurposeMember: 
        """
        First item access
        """
    def ChangeLast(self) -> StepElement_CurveElementPurposeMember: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepElement_SequenceOfCurveElementPurposeMember: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepElement_CurveElementPurposeMember: 
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
    def First(self) -> StepElement_CurveElementPurposeMember: 
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
    def InsertAfter(self,theIndex : int,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementPurposeMember) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementPurposeMember) -> None: ...
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
    def Last(self) -> StepElement_CurveElementPurposeMember: 
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
    def Prepend(self,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepElement_SequenceOfCurveElementPurposeMember) -> None: ...
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
    def Sequence(self) -> StepElement_SequenceOfCurveElementPurposeMember: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepElement_CurveElementPurposeMember) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementPurposeMember) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_CurveElementPurposeMember: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StepElement_SequenceOfCurveElementPurposeMember) -> None: ...
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
class StepElement_HSequenceOfCurveElementSectionDefinition(StepElement_SequenceOfCurveElementSectionDefinition, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepElement_CurveElementSectionDefinition) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : StepElement_SequenceOfCurveElementSectionDefinition) -> None: ...
    def Assign(self,theOther : StepElement_SequenceOfCurveElementSectionDefinition) -> StepElement_SequenceOfCurveElementSectionDefinition: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepElement_CurveElementSectionDefinition: 
        """
        First item access
        """
    def ChangeLast(self) -> StepElement_CurveElementSectionDefinition: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepElement_SequenceOfCurveElementSectionDefinition: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepElement_CurveElementSectionDefinition: 
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
    def First(self) -> StepElement_CurveElementSectionDefinition: 
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
    def InsertAfter(self,theIndex : int,theItem : StepElement_CurveElementSectionDefinition) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementSectionDefinition) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepElement_CurveElementSectionDefinition) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementSectionDefinition) -> None: ...
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
    def Last(self) -> StepElement_CurveElementSectionDefinition: 
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
    def Prepend(self,theItem : StepElement_CurveElementSectionDefinition) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepElement_SequenceOfCurveElementSectionDefinition) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def Sequence(self) -> StepElement_SequenceOfCurveElementSectionDefinition: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepElement_CurveElementSectionDefinition) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepElement_SequenceOfCurveElementSectionDefinition) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_CurveElementSectionDefinition: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_SequenceOfCurveElementSectionDefinition) -> None: ...
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
class StepElement_HSequenceOfElementMaterial(StepElement_SequenceOfElementMaterial, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepElement_ElementMaterial) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : StepElement_SequenceOfElementMaterial) -> None: ...
    def Assign(self,theOther : StepElement_SequenceOfElementMaterial) -> StepElement_SequenceOfElementMaterial: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepElement_ElementMaterial: 
        """
        First item access
        """
    def ChangeLast(self) -> StepElement_ElementMaterial: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepElement_SequenceOfElementMaterial: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepElement_ElementMaterial: 
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
    def First(self) -> StepElement_ElementMaterial: 
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
    def InsertAfter(self,theIndex : int,theItem : StepElement_ElementMaterial) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepElement_SequenceOfElementMaterial) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepElement_SequenceOfElementMaterial) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepElement_ElementMaterial) -> None: ...
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
    def Last(self) -> StepElement_ElementMaterial: 
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
    def Prepend(self,theSeq : StepElement_SequenceOfElementMaterial) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : StepElement_ElementMaterial) -> None: ...
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
    def Sequence(self) -> StepElement_SequenceOfElementMaterial: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepElement_ElementMaterial) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepElement_SequenceOfElementMaterial) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_ElementMaterial: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StepElement_SequenceOfElementMaterial) -> None: ...
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
class StepElement_HSequenceOfSurfaceElementPurposeMember(StepElement_SequenceOfSurfaceElementPurposeMember, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : StepElement_SurfaceElementPurposeMember) -> None: ...
    def Assign(self,theOther : StepElement_SequenceOfSurfaceElementPurposeMember) -> StepElement_SequenceOfSurfaceElementPurposeMember: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepElement_SurfaceElementPurposeMember: 
        """
        First item access
        """
    def ChangeLast(self) -> StepElement_SurfaceElementPurposeMember: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepElement_SequenceOfSurfaceElementPurposeMember: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepElement_SurfaceElementPurposeMember: 
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
    def First(self) -> StepElement_SurfaceElementPurposeMember: 
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
    def InsertAfter(self,theIndex : int,theItem : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepElement_SurfaceElementPurposeMember) -> None: ...
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
    def Last(self) -> StepElement_SurfaceElementPurposeMember: 
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
    def Prepend(self,theItem : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: ...
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
    def Sequence(self) -> StepElement_SequenceOfSurfaceElementPurposeMember: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepElement_SurfaceElementPurposeMember) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: 
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
    def Value(self,theIndex : int) -> StepElement_SurfaceElementPurposeMember: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepElement_SequenceOfSurfaceElementPurposeMember) -> None: ...
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
class StepElement_Surface3dElementDescriptor(StepElement_ElementDescriptor, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity Surface3dElementDescriptorRepresentation of STEP entity Surface3dElementDescriptorRepresentation of STEP entity Surface3dElementDescriptor
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
    def Init(self,aElementDescriptor_TopologyOrder : StepElement_ElementOrder,aElementDescriptor_Description : OCP.TCollection.TCollection_HAsciiString,aPurpose : StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember,aShape : StepElement_Element2dShape) -> None: 
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
    def Purpose(self) -> StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember: 
        """
        Returns field Purpose
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetPurpose(self,Purpose : StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember) -> None: 
        """
        Set field Purpose
        """
    def SetShape(self,Shape : StepElement_Element2dShape) -> None: 
        """
        Set field Shape
        """
    def SetTopologyOrder(self,TopologyOrder : StepElement_ElementOrder) -> None: 
        """
        Set field TopologyOrder
        """
    def Shape(self) -> StepElement_Element2dShape: 
        """
        Returns field Shape
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TopologyOrder(self) -> StepElement_ElementOrder: 
        """
        Returns field TopologyOrder
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
class StepElement_SurfaceElementProperty(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SurfaceElementPropertyRepresentation of STEP entity SurfaceElementPropertyRepresentation of STEP entity SurfaceElementProperty
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
    def Init(self,aPropertyId : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aSection : StepElement_SurfaceSectionField) -> None: 
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
    def PropertyId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field PropertyId
        """
    def Section(self) -> StepElement_SurfaceSectionField: 
        """
        Returns field Section
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetPropertyId(self,PropertyId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field PropertyId
        """
    def SetSection(self,Section : StepElement_SurfaceSectionField) -> None: 
        """
        Set field Section
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
class StepElement_SurfaceElementPurpose(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type SurfaceElementPurpose
    """
    def ApplicationDefinedElementPurpose(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Value as ApplicationDefinedElementPurpose (or Null if another type)
        """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a items of select member SurfaceElementPurposeMember 1 -> EnumeratedSurfaceElementPurpose 2 -> ApplicationDefinedElementPurpose 0 else
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of SurfaceElementPurpose select type return 0
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def EnumeratedSurfaceElementPurpose(self) -> StepElement_EnumeratedSurfaceElementPurpose: 
        """
        Returns Value as EnumeratedSurfaceElementPurpose (or Null if another type)
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
        Returns a new select member the type SurfaceElementPurposeMember
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
    def SetApplicationDefinedElementPurpose(self,aVal : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set Value for ApplicationDefinedElementPurpose
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetEnumeratedSurfaceElementPurpose(self,aVal : StepElement_EnumeratedSurfaceElementPurpose) -> None: 
        """
        Set Value for EnumeratedSurfaceElementPurpose
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
class StepElement_SurfaceElementPurposeMember(OCP.StepData.StepData_SelectNamed, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Representation of member for STEP SELECT type SurfaceElementPurposeRepresentation of member for STEP SELECT type SurfaceElementPurposeRepresentation of member for STEP SELECT type SurfaceElementPurpose
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CField(self) -> OCP.StepData.StepData_Field: 
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
    def Field(self) -> OCP.StepData.StepData_Field: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        Returns True if has name
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one;
        """
    def Name(self) -> str: 
        """
        Returns set name
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        Set name
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
class StepElement_SurfaceSection(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SurfaceSectionRepresentation of STEP entity SurfaceSectionRepresentation of STEP entity SurfaceSection
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
    def Init(self,aOffset : StepElement_MeasureOrUnspecifiedValue,aNonStructuralMass : StepElement_MeasureOrUnspecifiedValue,aNonStructuralMassOffset : StepElement_MeasureOrUnspecifiedValue) -> None: 
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
    def NonStructuralMass(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field NonStructuralMass
        """
    def NonStructuralMassOffset(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field NonStructuralMassOffset
        """
    def Offset(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field Offset
        """
    def SetNonStructuralMass(self,NonStructuralMass : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field NonStructuralMass
        """
    def SetNonStructuralMassOffset(self,NonStructuralMassOffset : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field NonStructuralMassOffset
        """
    def SetOffset(self,Offset : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field Offset
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
class StepElement_SurfaceSectionField(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SurfaceSectionFieldRepresentation of STEP entity SurfaceSectionFieldRepresentation of STEP entity SurfaceSectionField
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
class StepElement_SurfaceSectionFieldConstant(StepElement_SurfaceSectionField, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SurfaceSectionFieldConstantRepresentation of STEP entity SurfaceSectionFieldConstantRepresentation of STEP entity SurfaceSectionFieldConstant
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> StepElement_SurfaceSection: 
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
    def Init(self,aDefinition : StepElement_SurfaceSection) -> None: 
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
    def SetDefinition(self,Definition : StepElement_SurfaceSection) -> None: 
        """
        Set field Definition
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
class StepElement_SurfaceSectionFieldVarying(StepElement_SurfaceSectionField, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SurfaceSectionFieldVaryingRepresentation of STEP entity SurfaceSectionFieldVaryingRepresentation of STEP entity SurfaceSectionFieldVarying
    """
    def AdditionalNodeValues(self) -> bool: 
        """
        Returns field AdditionalNodeValues
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definitions(self) -> StepElement_HArray1OfSurfaceSection: 
        """
        Returns field Definitions
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
    def Init(self,aDefinitions : StepElement_HArray1OfSurfaceSection,aAdditionalNodeValues : bool) -> None: 
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
    def SetAdditionalNodeValues(self,AdditionalNodeValues : bool) -> None: 
        """
        Set field AdditionalNodeValues
        """
    def SetDefinitions(self,Definitions : StepElement_HArray1OfSurfaceSection) -> None: 
        """
        Set field Definitions
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
class StepElement_UniformSurfaceSection(StepElement_SurfaceSection, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity UniformSurfaceSectionRepresentation of STEP entity UniformSurfaceSectionRepresentation of STEP entity UniformSurfaceSection
    """
    def BendingThickness(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field BendingThickness
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
    def Init(self,aSurfaceSection_Offset : StepElement_MeasureOrUnspecifiedValue,aSurfaceSection_NonStructuralMass : StepElement_MeasureOrUnspecifiedValue,aSurfaceSection_NonStructuralMassOffset : StepElement_MeasureOrUnspecifiedValue,aThickness : float,aBendingThickness : StepElement_MeasureOrUnspecifiedValue,aShearThickness : StepElement_MeasureOrUnspecifiedValue) -> None: 
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
    def NonStructuralMass(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field NonStructuralMass
        """
    def NonStructuralMassOffset(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field NonStructuralMassOffset
        """
    def Offset(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field Offset
        """
    def SetBendingThickness(self,BendingThickness : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field BendingThickness
        """
    def SetNonStructuralMass(self,NonStructuralMass : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field NonStructuralMass
        """
    def SetNonStructuralMassOffset(self,NonStructuralMassOffset : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field NonStructuralMassOffset
        """
    def SetOffset(self,Offset : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field Offset
        """
    def SetShearThickness(self,ShearThickness : StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field ShearThickness
        """
    def SetThickness(self,Thickness : float) -> None: 
        """
        Set field Thickness
        """
    def ShearThickness(self) -> StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field ShearThickness
        """
    def Thickness(self) -> float: 
        """
        Returns field Thickness
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
class StepElement_UnspecifiedValue():
    """
    None

    Members:

      StepElement_Unspecified
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
    StepElement_Unspecified: OCP.StepElement.StepElement_UnspecifiedValue # value = <StepElement_UnspecifiedValue.StepElement_Unspecified: 0>
    __entries: dict # value = {'StepElement_Unspecified': (<StepElement_UnspecifiedValue.StepElement_Unspecified: 0>, None)}
    __members__: dict # value = {'StepElement_Unspecified': <StepElement_UnspecifiedValue.StepElement_Unspecified: 0>}
    pass
class StepElement_Volume3dElementDescriptor(StepElement_ElementDescriptor, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity Volume3dElementDescriptorRepresentation of STEP entity Volume3dElementDescriptorRepresentation of STEP entity Volume3dElementDescriptor
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
    def Init(self,aElementDescriptor_TopologyOrder : StepElement_ElementOrder,aElementDescriptor_Description : OCP.TCollection.TCollection_HAsciiString,aPurpose : StepElement_HArray1OfVolumeElementPurposeMember,aShape : StepElement_Volume3dElementShape) -> None: 
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
    def Purpose(self) -> StepElement_HArray1OfVolumeElementPurposeMember: 
        """
        Returns field Purpose
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetPurpose(self,Purpose : StepElement_HArray1OfVolumeElementPurposeMember) -> None: 
        """
        Set field Purpose
        """
    def SetShape(self,Shape : StepElement_Volume3dElementShape) -> None: 
        """
        Set field Shape
        """
    def SetTopologyOrder(self,TopologyOrder : StepElement_ElementOrder) -> None: 
        """
        Set field TopologyOrder
        """
    def Shape(self) -> StepElement_Volume3dElementShape: 
        """
        Returns field Shape
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TopologyOrder(self) -> StepElement_ElementOrder: 
        """
        Returns field TopologyOrder
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
class StepElement_Volume3dElementShape():
    """
    None

    Members:

      StepElement_Hexahedron

      StepElement_Wedge

      StepElement_Tetrahedron

      StepElement_Pyramid
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
    StepElement_Hexahedron: OCP.StepElement.StepElement_Volume3dElementShape # value = <StepElement_Volume3dElementShape.StepElement_Hexahedron: 0>
    StepElement_Pyramid: OCP.StepElement.StepElement_Volume3dElementShape # value = <StepElement_Volume3dElementShape.StepElement_Pyramid: 3>
    StepElement_Tetrahedron: OCP.StepElement.StepElement_Volume3dElementShape # value = <StepElement_Volume3dElementShape.StepElement_Tetrahedron: 2>
    StepElement_Wedge: OCP.StepElement.StepElement_Volume3dElementShape # value = <StepElement_Volume3dElementShape.StepElement_Wedge: 1>
    __entries: dict # value = {'StepElement_Hexahedron': (<StepElement_Volume3dElementShape.StepElement_Hexahedron: 0>, None), 'StepElement_Wedge': (<StepElement_Volume3dElementShape.StepElement_Wedge: 1>, None), 'StepElement_Tetrahedron': (<StepElement_Volume3dElementShape.StepElement_Tetrahedron: 2>, None), 'StepElement_Pyramid': (<StepElement_Volume3dElementShape.StepElement_Pyramid: 3>, None)}
    __members__: dict # value = {'StepElement_Hexahedron': <StepElement_Volume3dElementShape.StepElement_Hexahedron: 0>, 'StepElement_Wedge': <StepElement_Volume3dElementShape.StepElement_Wedge: 1>, 'StepElement_Tetrahedron': <StepElement_Volume3dElementShape.StepElement_Tetrahedron: 2>, 'StepElement_Pyramid': <StepElement_Volume3dElementShape.StepElement_Pyramid: 3>}
    pass
class StepElement_VolumeElementPurpose(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type VolumeElementPurpose
    """
    def ApplicationDefinedElementPurpose(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns Value as ApplicationDefinedElementPurpose (or Null if another type)
        """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a items of select member VolumeElementPurposeMember 1 -> EnumeratedVolumeElementPurpose 2 -> ApplicationDefinedElementPurpose 0 else
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of VolumeElementPurpose select type return 0
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def EnumeratedVolumeElementPurpose(self) -> StepElement_EnumeratedVolumeElementPurpose: 
        """
        Returns Value as EnumeratedVolumeElementPurpose (or Null if another type)
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
        Returns a new select member the type VolumeElementPurposeMember
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
    def SetApplicationDefinedElementPurpose(self,aVal : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set Value for ApplicationDefinedElementPurpose
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetEnumeratedVolumeElementPurpose(self,aVal : StepElement_EnumeratedVolumeElementPurpose) -> None: 
        """
        Set Value for EnumeratedVolumeElementPurpose
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
class StepElement_VolumeElementPurposeMember(OCP.StepData.StepData_SelectNamed, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Representation of member for STEP SELECT type VolumeElementPurposeRepresentation of member for STEP SELECT type VolumeElementPurposeRepresentation of member for STEP SELECT type VolumeElementPurpose
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CField(self) -> OCP.StepData.StepData_Field: 
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
    def Field(self) -> OCP.StepData.StepData_Field: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        Returns True if has name
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
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one;
        """
    def Name(self) -> str: 
        """
        Returns set name
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
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        Set name
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
StepElement_Axial: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_Axial: 0>
StepElement_BendingDirect: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingDirect: 2>
StepElement_BendingTorsion: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingTorsion: 3>
StepElement_Cubic: OCP.StepElement.StepElement_ElementOrder # value = <StepElement_ElementOrder.StepElement_Cubic: 2>
StepElement_ElementEdge: OCP.StepElement.StepElement_CurveEdge # value = <StepElement_CurveEdge.StepElement_ElementEdge: 0>
StepElement_Hexahedron: OCP.StepElement.StepElement_Volume3dElementShape # value = <StepElement_Volume3dElementShape.StepElement_Hexahedron: 0>
StepElement_Linear: OCP.StepElement.StepElement_ElementOrder # value = <StepElement_ElementOrder.StepElement_Linear: 0>
StepElement_MembraneDirect: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneDirect: 0>
StepElement_MembraneShear: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneShear: 1>
StepElement_None: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_None: 7>
StepElement_NormalToPlaneShear: OCP.StepElement.StepElement_EnumeratedSurfaceElementPurpose # value = <StepElement_EnumeratedSurfaceElementPurpose.StepElement_NormalToPlaneShear: 4>
StepElement_Pyramid: OCP.StepElement.StepElement_Volume3dElementShape # value = <StepElement_Volume3dElementShape.StepElement_Pyramid: 3>
StepElement_Quadratic: OCP.StepElement.StepElement_ElementOrder # value = <StepElement_ElementOrder.StepElement_Quadratic: 1>
StepElement_Quadrilateral: OCP.StepElement.StepElement_Element2dShape # value = <StepElement_Element2dShape.StepElement_Quadrilateral: 0>
StepElement_StressDisplacement: OCP.StepElement.StepElement_EnumeratedVolumeElementPurpose # value = <StepElement_EnumeratedVolumeElementPurpose.StepElement_StressDisplacement: 0>
StepElement_Tetrahedron: OCP.StepElement.StepElement_Volume3dElementShape # value = <StepElement_Volume3dElementShape.StepElement_Tetrahedron: 2>
StepElement_Torsion: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_Torsion: 3>
StepElement_Triangle: OCP.StepElement.StepElement_Element2dShape # value = <StepElement_Element2dShape.StepElement_Triangle: 1>
StepElement_Unspecified: OCP.StepElement.StepElement_UnspecifiedValue # value = <StepElement_UnspecifiedValue.StepElement_Unspecified: 0>
StepElement_Volume: OCP.StepElement.StepElement_ElementVolume # value = <StepElement_ElementVolume.StepElement_Volume: 0>
StepElement_Warp: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_Warp: 6>
StepElement_Warping: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_Warping: 6>
StepElement_Wedge: OCP.StepElement.StepElement_Volume3dElementShape # value = <StepElement_Volume3dElementShape.StepElement_Wedge: 1>
StepElement_XRotation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_XRotation: 3>
StepElement_XTranslation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_XTranslation: 0>
StepElement_XYShear: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_XYShear: 4>
StepElement_XZShear: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_XZShear: 5>
StepElement_YRotation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_YRotation: 4>
StepElement_YTranslation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_YTranslation: 1>
StepElement_YYBending: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_YYBending: 1>
StepElement_ZRotation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_ZRotation: 5>
StepElement_ZTranslation: OCP.StepElement.StepElement_EnumeratedCurveElementFreedom # value = <StepElement_EnumeratedCurveElementFreedom.StepElement_ZTranslation: 2>
StepElement_ZZBending: OCP.StepElement.StepElement_EnumeratedCurveElementPurpose # value = <StepElement_EnumeratedCurveElementPurpose.StepElement_ZZBending: 2>
