import OCP.StepFEA
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.TColStd
import OCP.StepData
import OCP.StepRepr
import OCP.StepBasic
import OCP.StepGeom
import OCP.Standard
import OCP.StepElement
import OCP.NCollection
import OCP.Interface
__all__  = [
"StepFEA_FeaRepresentationItem",
"StepFEA_AlignedSurface3dElementCoordinateSystem",
"StepFEA_ArbitraryVolume3dElementCoordinateSystem",
"StepFEA_Array1OfCurveElementEndOffset",
"StepFEA_Array1OfCurveElementEndRelease",
"StepFEA_Array1OfCurveElementInterval",
"StepFEA_Array1OfDegreeOfFreedom",
"StepFEA_Array1OfElementRepresentation",
"StepFEA_Array1OfNodeRepresentation",
"StepFEA_ConstantSurface3dElementCoordinateSystem",
"StepFEA_CoordinateSystemType",
"StepFEA_Curve3dElementProperty",
"StepFEA_ElementRepresentation",
"StepFEA_CurveEdge",
"StepFEA_CurveElementEndCoordinateSystem",
"StepFEA_CurveElementEndOffset",
"StepFEA_CurveElementEndRelease",
"StepFEA_CurveElementInterval",
"StepFEA_CurveElementIntervalConstant",
"StepFEA_CurveElementIntervalLinearlyVarying",
"StepFEA_CurveElementLocation",
"StepFEA_DegreeOfFreedom",
"StepFEA_DegreeOfFreedomMember",
"StepFEA_NodeRepresentation",
"StepFEA_ElementGeometricRelationship",
"StepFEA_FeaGroup",
"StepFEA_ElementOrElementGroup",
"StepFEA_Curve3dElementRepresentation",
"StepFEA_ElementVolume",
"StepFEA_EnumeratedDegreeOfFreedom",
"StepFEA_FeaMaterialPropertyRepresentationItem",
"StepFEA_FeaAxis2Placement3d",
"StepFEA_FeaCurveSectionGeometricRelationship",
"StepFEA_ElementGroup",
"StepFEA_FeaLinearElasticity",
"StepFEA_FeaMassDensity",
"StepFEA_FeaMaterialPropertyRepresentation",
"StepFEA_FeaAreaDensity",
"StepFEA_FeaModel",
"StepFEA_FeaModel3d",
"StepFEA_FeaModelDefinition",
"StepFEA_FeaMoistureAbsorption",
"StepFEA_FeaParametricPoint",
"StepFEA_AlignedCurve3dElementCoordinateSystem",
"StepFEA_FeaSecantCoefficientOfLinearThermalExpansion",
"StepFEA_FeaShellBendingStiffness",
"StepFEA_FeaShellMembraneBendingCouplingStiffness",
"StepFEA_FeaShellMembraneStiffness",
"StepFEA_FeaShellShearStiffness",
"StepFEA_FeaSurfaceSectionGeometricRelationship",
"StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion",
"StepFEA_FreedomAndCoefficient",
"StepFEA_FreedomsList",
"StepFEA_GeometricNode",
"StepFEA_HArray1OfCurveElementEndOffset",
"StepFEA_HArray1OfCurveElementEndRelease",
"StepFEA_HArray1OfCurveElementInterval",
"StepFEA_HArray1OfDegreeOfFreedom",
"StepFEA_HArray1OfElementRepresentation",
"StepFEA_HArray1OfNodeRepresentation",
"StepFEA_SequenceOfCurve3dElementProperty",
"StepFEA_SequenceOfElementGeometricRelationship",
"StepFEA_SequenceOfElementRepresentation",
"StepFEA_SequenceOfNodeRepresentation",
"StepFEA_Node",
"StepFEA_NodeDefinition",
"StepFEA_NodeGroup",
"StepFEA_DummyNode",
"StepFEA_NodeSet",
"StepFEA_NodeWithSolutionCoordinateSystem",
"StepFEA_NodeWithVector",
"StepFEA_ParametricCurve3dElementCoordinateDirection",
"StepFEA_ParametricCurve3dElementCoordinateSystem",
"StepFEA_ParametricSurface3dElementCoordinateSystem",
"StepFEA_HSequenceOfCurve3dElementProperty",
"StepFEA_HSequenceOfElementGeometricRelationship",
"StepFEA_HSequenceOfElementRepresentation",
"StepFEA_HSequenceOfNodeRepresentation",
"StepFEA_Surface3dElementRepresentation",
"StepFEA_SymmetricTensor22d",
"StepFEA_SymmetricTensor23d",
"StepFEA_SymmetricTensor23dMember",
"StepFEA_SymmetricTensor42d",
"StepFEA_SymmetricTensor43d",
"StepFEA_SymmetricTensor43dMember",
"StepFEA_UnspecifiedValue",
"StepFEA_Volume3dElementRepresentation",
"StepFEA_Cartesian",
"StepFEA_Cylindrical",
"StepFEA_ElementEdge",
"StepFEA_Spherical",
"StepFEA_Unspecified",
"StepFEA_Volume",
"StepFEA_Warp",
"StepFEA_XRotation",
"StepFEA_XTranslation",
"StepFEA_YRotation",
"StepFEA_YTranslation",
"StepFEA_ZRotation",
"StepFEA_ZTranslation"
]
class StepFEA_FeaRepresentationItem(OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaRepresentationItemRepresentation of STEP entity FeaRepresentationItemRepresentation of STEP entity FeaRepresentationItem
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
class StepFEA_AlignedSurface3dElementCoordinateSystem(StepFEA_FeaRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity AlignedSurface3dElementCoordinateSystemRepresentation of STEP entity AlignedSurface3dElementCoordinateSystemRepresentation of STEP entity AlignedSurface3dElementCoordinateSystem
    """
    def CoordinateSystem(self) -> StepFEA_FeaAxis2Placement3d: 
        """
        Returns field CoordinateSystem
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aCoordinateSystem : StepFEA_FeaAxis2Placement3d) -> None: 
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
    def SetCoordinateSystem(self,CoordinateSystem : StepFEA_FeaAxis2Placement3d) -> None: 
        """
        Set field CoordinateSystem
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
class StepFEA_ArbitraryVolume3dElementCoordinateSystem(StepFEA_FeaRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ArbitraryVolume3dElementCoordinateSystemRepresentation of STEP entity ArbitraryVolume3dElementCoordinateSystemRepresentation of STEP entity ArbitraryVolume3dElementCoordinateSystem
    """
    def CoordinateSystem(self) -> StepFEA_FeaAxis2Placement3d: 
        """
        Returns field CoordinateSystem
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aCoordinateSystem : StepFEA_FeaAxis2Placement3d) -> None: 
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
    def SetCoordinateSystem(self,CoordinateSystem : StepFEA_FeaAxis2Placement3d) -> None: 
        """
        Set field CoordinateSystem
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
class StepFEA_Array1OfCurveElementEndOffset():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepFEA_Array1OfCurveElementEndOffset) -> StepFEA_Array1OfCurveElementEndOffset: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepFEA_CurveElementEndOffset: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_CurveElementEndOffset: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_CurveElementEndOffset: 
        """
        Variable value access
        """
    def First(self) -> StepFEA_CurveElementEndOffset: 
        """
        Returns first element
        """
    def Init(self,theValue : StepFEA_CurveElementEndOffset) -> None: 
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
    def Last(self) -> StepFEA_CurveElementEndOffset: 
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
    def Move(self,theOther : StepFEA_Array1OfCurveElementEndOffset) -> StepFEA_Array1OfCurveElementEndOffset: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_CurveElementEndOffset) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_CurveElementEndOffset: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepFEA_CurveElementEndOffset,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfCurveElementEndOffset) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepFEA_Array1OfCurveElementEndRelease():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepFEA_Array1OfCurveElementEndRelease) -> StepFEA_Array1OfCurveElementEndRelease: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepFEA_CurveElementEndRelease: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_CurveElementEndRelease: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_CurveElementEndRelease: 
        """
        Variable value access
        """
    def First(self) -> StepFEA_CurveElementEndRelease: 
        """
        Returns first element
        """
    def Init(self,theValue : StepFEA_CurveElementEndRelease) -> None: 
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
    def Last(self) -> StepFEA_CurveElementEndRelease: 
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
    def Move(self,theOther : StepFEA_Array1OfCurveElementEndRelease) -> StepFEA_Array1OfCurveElementEndRelease: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_CurveElementEndRelease) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_CurveElementEndRelease: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepFEA_CurveElementEndRelease,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfCurveElementEndRelease) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepFEA_Array1OfCurveElementInterval():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepFEA_Array1OfCurveElementInterval) -> StepFEA_Array1OfCurveElementInterval: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepFEA_CurveElementInterval: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_CurveElementInterval: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_CurveElementInterval: 
        """
        Variable value access
        """
    def First(self) -> StepFEA_CurveElementInterval: 
        """
        Returns first element
        """
    def Init(self,theValue : StepFEA_CurveElementInterval) -> None: 
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
    def Last(self) -> StepFEA_CurveElementInterval: 
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
    def Move(self,theOther : StepFEA_Array1OfCurveElementInterval) -> StepFEA_Array1OfCurveElementInterval: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_CurveElementInterval) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_CurveElementInterval: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfCurveElementInterval) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepFEA_CurveElementInterval,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepFEA_Array1OfDegreeOfFreedom():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepFEA_Array1OfDegreeOfFreedom) -> StepFEA_Array1OfDegreeOfFreedom: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepFEA_DegreeOfFreedom: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_DegreeOfFreedom: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_DegreeOfFreedom: 
        """
        Variable value access
        """
    def First(self) -> StepFEA_DegreeOfFreedom: 
        """
        Returns first element
        """
    def Init(self,theValue : StepFEA_DegreeOfFreedom) -> None: 
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
    def Last(self) -> StepFEA_DegreeOfFreedom: 
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
    def Move(self,theOther : StepFEA_Array1OfDegreeOfFreedom) -> StepFEA_Array1OfDegreeOfFreedom: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_DegreeOfFreedom) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_DegreeOfFreedom: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfDegreeOfFreedom) -> None: ...
    @overload
    def __init__(self,theBegin : StepFEA_DegreeOfFreedom,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepFEA_Array1OfElementRepresentation():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepFEA_Array1OfElementRepresentation) -> StepFEA_Array1OfElementRepresentation: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepFEA_ElementRepresentation: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_ElementRepresentation: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_ElementRepresentation: 
        """
        Variable value access
        """
    def First(self) -> StepFEA_ElementRepresentation: 
        """
        Returns first element
        """
    def Init(self,theValue : StepFEA_ElementRepresentation) -> None: 
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
    def Last(self) -> StepFEA_ElementRepresentation: 
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
    def Move(self,theOther : StepFEA_Array1OfElementRepresentation) -> StepFEA_Array1OfElementRepresentation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_ElementRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_ElementRepresentation: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepFEA_ElementRepresentation,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfElementRepresentation) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepFEA_Array1OfNodeRepresentation():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepFEA_Array1OfNodeRepresentation) -> StepFEA_Array1OfNodeRepresentation: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepFEA_NodeRepresentation: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_NodeRepresentation: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_NodeRepresentation: 
        """
        Variable value access
        """
    def First(self) -> StepFEA_NodeRepresentation: 
        """
        Returns first element
        """
    def Init(self,theValue : StepFEA_NodeRepresentation) -> None: 
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
    def Last(self) -> StepFEA_NodeRepresentation: 
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
    def Move(self,theOther : StepFEA_Array1OfNodeRepresentation) -> StepFEA_Array1OfNodeRepresentation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_NodeRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_NodeRepresentation: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepFEA_NodeRepresentation,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfNodeRepresentation) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepFEA_ConstantSurface3dElementCoordinateSystem(StepFEA_FeaRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ConstantSurface3dElementCoordinateSystemRepresentation of STEP entity ConstantSurface3dElementCoordinateSystemRepresentation of STEP entity ConstantSurface3dElementCoordinateSystem
    """
    def Angle(self) -> float: 
        """
        Returns field Angle
        """
    def Axis(self) -> int: 
        """
        Returns field Axis
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aAxis : int,aAngle : float) -> None: 
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
    def SetAngle(self,Angle : float) -> None: 
        """
        Set field Angle
        """
    def SetAxis(self,Axis : int) -> None: 
        """
        Set field Axis
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
class StepFEA_CoordinateSystemType():
    """
    None

    Members:

      StepFEA_Cartesian

      StepFEA_Cylindrical

      StepFEA_Spherical
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
    StepFEA_Cartesian: OCP.StepFEA.StepFEA_CoordinateSystemType # value = StepFEA_CoordinateSystemType.StepFEA_Cartesian
    StepFEA_Cylindrical: OCP.StepFEA.StepFEA_CoordinateSystemType # value = StepFEA_CoordinateSystemType.StepFEA_Cylindrical
    StepFEA_Spherical: OCP.StepFEA.StepFEA_CoordinateSystemType # value = StepFEA_CoordinateSystemType.StepFEA_Spherical
    __entries: dict # value = {'StepFEA_Cartesian': (StepFEA_CoordinateSystemType.StepFEA_Cartesian, None), 'StepFEA_Cylindrical': (StepFEA_CoordinateSystemType.StepFEA_Cylindrical, None), 'StepFEA_Spherical': (StepFEA_CoordinateSystemType.StepFEA_Spherical, None)}
    __members__: dict # value = {'StepFEA_Cartesian': StepFEA_CoordinateSystemType.StepFEA_Cartesian, 'StepFEA_Cylindrical': StepFEA_CoordinateSystemType.StepFEA_Cylindrical, 'StepFEA_Spherical': StepFEA_CoordinateSystemType.StepFEA_Spherical}
    pass
class StepFEA_Curve3dElementProperty(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity Curve3dElementPropertyRepresentation of STEP entity Curve3dElementPropertyRepresentation of STEP entity Curve3dElementProperty
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
    def EndOffsets(self) -> StepFEA_HArray1OfCurveElementEndOffset: 
        """
        Returns field EndOffsets
        """
    def EndReleases(self) -> StepFEA_HArray1OfCurveElementEndRelease: 
        """
        Returns field EndReleases
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aPropertyId : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aIntervalDefinitions : StepFEA_HArray1OfCurveElementInterval,aEndOffsets : StepFEA_HArray1OfCurveElementEndOffset,aEndReleases : StepFEA_HArray1OfCurveElementEndRelease) -> None: 
        """
        Initialize all fields (own and inherited)
        """
    def IntervalDefinitions(self) -> StepFEA_HArray1OfCurveElementInterval: 
        """
        Returns field IntervalDefinitions
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
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetEndOffsets(self,EndOffsets : StepFEA_HArray1OfCurveElementEndOffset) -> None: 
        """
        Set field EndOffsets
        """
    def SetEndReleases(self,EndReleases : StepFEA_HArray1OfCurveElementEndRelease) -> None: 
        """
        Set field EndReleases
        """
    def SetIntervalDefinitions(self,IntervalDefinitions : StepFEA_HArray1OfCurveElementInterval) -> None: 
        """
        Set field IntervalDefinitions
        """
    def SetPropertyId(self,PropertyId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field PropertyId
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
class StepFEA_ElementRepresentation(OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ElementRepresentationRepresentation of STEP entity ElementRepresentationRepresentation of STEP entity ElementRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aNodeList : StepFEA_HArray1OfNodeRepresentation) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
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
    def NodeList(self) -> StepFEA_HArray1OfNodeRepresentation: 
        """
        Returns field NodeList
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetNodeList(self,NodeList : StepFEA_HArray1OfNodeRepresentation) -> None: 
        """
        Set field NodeList
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
class StepFEA_CurveEdge():
    """
    None

    Members:

      StepFEA_ElementEdge
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
    StepFEA_ElementEdge: OCP.StepFEA.StepFEA_CurveEdge # value = StepFEA_CurveEdge.StepFEA_ElementEdge
    __entries: dict # value = {'StepFEA_ElementEdge': (StepFEA_CurveEdge.StepFEA_ElementEdge, None)}
    __members__: dict # value = {'StepFEA_ElementEdge': StepFEA_CurveEdge.StepFEA_ElementEdge}
    pass
class StepFEA_CurveElementEndCoordinateSystem(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type CurveElementEndCoordinateSystem
    """
    def AlignedCurve3dElementCoordinateSystem(self) -> StepFEA_AlignedCurve3dElementCoordinateSystem: 
        """
        Returns Value as AlignedCurve3dElementCoordinateSystem (or Null if another type)
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
        Recognizes a kind of CurveElementEndCoordinateSystem select type 1 -> FeaAxis2Placement3d from StepFEA 2 -> AlignedCurve3dElementCoordinateSystem from StepFEA 3 -> ParametricCurve3dElementCoordinateSystem from StepFEA 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def FeaAxis2Placement3d(self) -> StepFEA_FeaAxis2Placement3d: 
        """
        Returns Value as FeaAxis2Placement3d (or Null if another type)
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
    def ParametricCurve3dElementCoordinateSystem(self) -> StepFEA_ParametricCurve3dElementCoordinateSystem: 
        """
        Returns Value as ParametricCurve3dElementCoordinateSystem (or Null if another type)
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
class StepFEA_CurveElementEndOffset(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveElementEndOffsetRepresentation of STEP entity CurveElementEndOffsetRepresentation of STEP entity CurveElementEndOffset
    """
    def CoordinateSystem(self) -> StepFEA_CurveElementEndCoordinateSystem: 
        """
        Returns field CoordinateSystem
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
    def Init(self,aCoordinateSystem : StepFEA_CurveElementEndCoordinateSystem,aOffsetVector : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
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
    def OffsetVector(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns field OffsetVector
        """
    def SetCoordinateSystem(self,CoordinateSystem : StepFEA_CurveElementEndCoordinateSystem) -> None: 
        """
        Set field CoordinateSystem
        """
    def SetOffsetVector(self,OffsetVector : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Set field OffsetVector
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
class StepFEA_CurveElementEndRelease(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveElementEndReleaseRepresentation of STEP entity CurveElementEndReleaseRepresentation of STEP entity CurveElementEndRelease
    """
    def CoordinateSystem(self) -> StepFEA_CurveElementEndCoordinateSystem: 
        """
        Returns field CoordinateSystem
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
    def Init(self,aCoordinateSystem : StepFEA_CurveElementEndCoordinateSystem,aReleases : OCP.StepElement.StepElement_HArray1OfCurveElementEndReleasePacket) -> None: 
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
    def Releases(self) -> OCP.StepElement.StepElement_HArray1OfCurveElementEndReleasePacket: 
        """
        Returns field Releases
        """
    def SetCoordinateSystem(self,CoordinateSystem : StepFEA_CurveElementEndCoordinateSystem) -> None: 
        """
        Set field CoordinateSystem
        """
    def SetReleases(self,Releases : OCP.StepElement.StepElement_HArray1OfCurveElementEndReleasePacket) -> None: 
        """
        Set field Releases
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
class StepFEA_CurveElementInterval(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveElementIntervalRepresentation of STEP entity CurveElementIntervalRepresentation of STEP entity CurveElementInterval
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
    def EuAngles(self) -> OCP.StepBasic.StepBasic_EulerAngles: 
        """
        Returns field EuAngles
        """
    def FinishPosition(self) -> StepFEA_CurveElementLocation: 
        """
        Returns field FinishPosition
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aFinishPosition : StepFEA_CurveElementLocation,aEuAngles : OCP.StepBasic.StepBasic_EulerAngles) -> None: 
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
    def SetEuAngles(self,EuAngles : OCP.StepBasic.StepBasic_EulerAngles) -> None: 
        """
        Set field EuAngles
        """
    def SetFinishPosition(self,FinishPosition : StepFEA_CurveElementLocation) -> None: 
        """
        Set field FinishPosition
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
class StepFEA_CurveElementIntervalConstant(StepFEA_CurveElementInterval, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveElementIntervalConstantRepresentation of STEP entity CurveElementIntervalConstantRepresentation of STEP entity CurveElementIntervalConstant
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
    def EuAngles(self) -> OCP.StepBasic.StepBasic_EulerAngles: 
        """
        Returns field EuAngles
        """
    def FinishPosition(self) -> StepFEA_CurveElementLocation: 
        """
        Returns field FinishPosition
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aCurveElementInterval_FinishPosition : StepFEA_CurveElementLocation,aCurveElementInterval_EuAngles : OCP.StepBasic.StepBasic_EulerAngles,aSection : OCP.StepElement.StepElement_CurveElementSectionDefinition) -> None: 
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
    def Section(self) -> OCP.StepElement.StepElement_CurveElementSectionDefinition: 
        """
        Returns field Section
        """
    def SetEuAngles(self,EuAngles : OCP.StepBasic.StepBasic_EulerAngles) -> None: 
        """
        Set field EuAngles
        """
    def SetFinishPosition(self,FinishPosition : StepFEA_CurveElementLocation) -> None: 
        """
        Set field FinishPosition
        """
    def SetSection(self,Section : OCP.StepElement.StepElement_CurveElementSectionDefinition) -> None: 
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
class StepFEA_CurveElementIntervalLinearlyVarying(StepFEA_CurveElementInterval, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveElementIntervalLinearlyVaryingRepresentation of STEP entity CurveElementIntervalLinearlyVaryingRepresentation of STEP entity CurveElementIntervalLinearlyVarying
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
    def EuAngles(self) -> OCP.StepBasic.StepBasic_EulerAngles: 
        """
        Returns field EuAngles
        """
    def FinishPosition(self) -> StepFEA_CurveElementLocation: 
        """
        Returns field FinishPosition
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aCurveElementInterval_FinishPosition : StepFEA_CurveElementLocation,aCurveElementInterval_EuAngles : OCP.StepBasic.StepBasic_EulerAngles,aSections : OCP.StepElement.StepElement_HArray1OfCurveElementSectionDefinition) -> None: 
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
    def Sections(self) -> OCP.StepElement.StepElement_HArray1OfCurveElementSectionDefinition: 
        """
        Returns field Sections
        """
    def SetEuAngles(self,EuAngles : OCP.StepBasic.StepBasic_EulerAngles) -> None: 
        """
        Set field EuAngles
        """
    def SetFinishPosition(self,FinishPosition : StepFEA_CurveElementLocation) -> None: 
        """
        Set field FinishPosition
        """
    def SetSections(self,Sections : OCP.StepElement.StepElement_HArray1OfCurveElementSectionDefinition) -> None: 
        """
        Set field Sections
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
class StepFEA_CurveElementLocation(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveElementLocationRepresentation of STEP entity CurveElementLocationRepresentation of STEP entity CurveElementLocation
    """
    def Coordinate(self) -> StepFEA_FeaParametricPoint: 
        """
        Returns field Coordinate
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
    def Init(self,aCoordinate : StepFEA_FeaParametricPoint) -> None: 
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
    def SetCoordinate(self,Coordinate : StepFEA_FeaParametricPoint) -> None: 
        """
        Set field Coordinate
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
class StepFEA_DegreeOfFreedom(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type DegreeOfFreedom
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
    def EnumeratedDegreeOfFreedom(self) -> StepFEA_EnumeratedDegreeOfFreedom: 
        """
        Returns Value as EnumeratedDegreeOfFreedom (or Null if another type)
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
    def SetEnumeratedDegreeOfFreedom(self,aVal : StepFEA_EnumeratedDegreeOfFreedom) -> None: 
        """
        Returns Value as EnumeratedDegreeOfFreedom (or Null if another type)
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
class StepFEA_DegreeOfFreedomMember(OCP.StepData.StepData_SelectNamed, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
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
class StepFEA_NodeRepresentation(OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NodeRepresentationRepresentation of STEP entity NodeRepresentationRepresentation of STEP entity NodeRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aModelRef : StepFEA_FeaModel) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ModelRef(self) -> StepFEA_FeaModel: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel) -> None: 
        """
        Set field ModelRef
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
class StepFEA_ElementGeometricRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ElementGeometricRelationshipRepresentation of STEP entity ElementGeometricRelationshipRepresentation of STEP entity ElementGeometricRelationship
    """
    def Aspect(self) -> OCP.StepElement.StepElement_ElementAspect: 
        """
        Returns field Aspect
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
    def ElementRef(self) -> StepFEA_ElementOrElementGroup: 
        """
        Returns field ElementRef
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aElementRef : StepFEA_ElementOrElementGroup,aItem : OCP.StepElement.StepElement_AnalysisItemWithinRepresentation,aAspect : OCP.StepElement.StepElement_ElementAspect) -> None: 
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
    def Item(self) -> OCP.StepElement.StepElement_AnalysisItemWithinRepresentation: 
        """
        Returns field Item
        """
    def SetAspect(self,Aspect : OCP.StepElement.StepElement_ElementAspect) -> None: 
        """
        Set field Aspect
        """
    def SetElementRef(self,ElementRef : StepFEA_ElementOrElementGroup) -> None: 
        """
        Set field ElementRef
        """
    def SetItem(self,Item : OCP.StepElement.StepElement_AnalysisItemWithinRepresentation) -> None: 
        """
        Set field Item
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
class StepFEA_FeaGroup(OCP.StepBasic.StepBasic_Group, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaGroupRepresentation of STEP entity FeaGroupRepresentation of STEP entity FeaGroup
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
    def Init(self,aGroup_Name : OCP.TCollection.TCollection_HAsciiString,aGroup_Description : OCP.TCollection.TCollection_HAsciiString,aModelRef : StepFEA_FeaModel) -> None: 
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
    def ModelRef(self) -> StepFEA_FeaModel: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel) -> None: 
        """
        Set field ModelRef
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
class StepFEA_ElementOrElementGroup(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type ElementOrElementGroup
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
        Recognizes a kind of ElementOrElementGroup select type 1 -> ElementRepresentation from StepFEA 2 -> ElementGroup from StepFEA 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def ElementGroup(self) -> StepFEA_ElementGroup: 
        """
        Returns Value as ElementGroup (or Null if another type)
        """
    def ElementRepresentation(self) -> StepFEA_ElementRepresentation: 
        """
        Returns Value as ElementRepresentation (or Null if another type)
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
class StepFEA_Curve3dElementRepresentation(StepFEA_ElementRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity Curve3dElementRepresentationRepresentation of STEP entity Curve3dElementRepresentationRepresentation of STEP entity Curve3dElementRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def ElementDescriptor(self) -> OCP.StepElement.StepElement_Curve3dElementDescriptor: 
        """
        Returns field ElementDescriptor
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aElementRepresentation_NodeList : StepFEA_HArray1OfNodeRepresentation,aModelRef : StepFEA_FeaModel3d,aElementDescriptor : OCP.StepElement.StepElement_Curve3dElementDescriptor,aProperty : StepFEA_Curve3dElementProperty,aMaterial : OCP.StepElement.StepElement_ElementMaterial) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Material(self) -> OCP.StepElement.StepElement_ElementMaterial: 
        """
        Returns field Material
        """
    def ModelRef(self) -> StepFEA_FeaModel3d: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def NodeList(self) -> StepFEA_HArray1OfNodeRepresentation: 
        """
        Returns field NodeList
        """
    def Property(self) -> StepFEA_Curve3dElementProperty: 
        """
        Returns field Property
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetElementDescriptor(self,ElementDescriptor : OCP.StepElement.StepElement_Curve3dElementDescriptor) -> None: 
        """
        Set field ElementDescriptor
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetMaterial(self,Material : OCP.StepElement.StepElement_ElementMaterial) -> None: 
        """
        Set field Material
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel3d) -> None: 
        """
        Set field ModelRef
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetNodeList(self,NodeList : StepFEA_HArray1OfNodeRepresentation) -> None: 
        """
        Set field NodeList
        """
    def SetProperty(self,Property : StepFEA_Curve3dElementProperty) -> None: 
        """
        Set field Property
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
class StepFEA_ElementVolume():
    """
    None

    Members:

      StepFEA_Volume
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
    StepFEA_Volume: OCP.StepFEA.StepFEA_ElementVolume # value = StepFEA_ElementVolume.StepFEA_Volume
    __entries: dict # value = {'StepFEA_Volume': (StepFEA_ElementVolume.StepFEA_Volume, None)}
    __members__: dict # value = {'StepFEA_Volume': StepFEA_ElementVolume.StepFEA_Volume}
    pass
class StepFEA_EnumeratedDegreeOfFreedom():
    """
    None

    Members:

      StepFEA_XTranslation

      StepFEA_YTranslation

      StepFEA_ZTranslation

      StepFEA_XRotation

      StepFEA_YRotation

      StepFEA_ZRotation

      StepFEA_Warp
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
    StepFEA_Warp: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_Warp
    StepFEA_XRotation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_XRotation
    StepFEA_XTranslation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_XTranslation
    StepFEA_YRotation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_YRotation
    StepFEA_YTranslation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_YTranslation
    StepFEA_ZRotation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_ZRotation
    StepFEA_ZTranslation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_ZTranslation
    __entries: dict # value = {'StepFEA_XTranslation': (StepFEA_EnumeratedDegreeOfFreedom.StepFEA_XTranslation, None), 'StepFEA_YTranslation': (StepFEA_EnumeratedDegreeOfFreedom.StepFEA_YTranslation, None), 'StepFEA_ZTranslation': (StepFEA_EnumeratedDegreeOfFreedom.StepFEA_ZTranslation, None), 'StepFEA_XRotation': (StepFEA_EnumeratedDegreeOfFreedom.StepFEA_XRotation, None), 'StepFEA_YRotation': (StepFEA_EnumeratedDegreeOfFreedom.StepFEA_YRotation, None), 'StepFEA_ZRotation': (StepFEA_EnumeratedDegreeOfFreedom.StepFEA_ZRotation, None), 'StepFEA_Warp': (StepFEA_EnumeratedDegreeOfFreedom.StepFEA_Warp, None)}
    __members__: dict # value = {'StepFEA_XTranslation': StepFEA_EnumeratedDegreeOfFreedom.StepFEA_XTranslation, 'StepFEA_YTranslation': StepFEA_EnumeratedDegreeOfFreedom.StepFEA_YTranslation, 'StepFEA_ZTranslation': StepFEA_EnumeratedDegreeOfFreedom.StepFEA_ZTranslation, 'StepFEA_XRotation': StepFEA_EnumeratedDegreeOfFreedom.StepFEA_XRotation, 'StepFEA_YRotation': StepFEA_EnumeratedDegreeOfFreedom.StepFEA_YRotation, 'StepFEA_ZRotation': StepFEA_EnumeratedDegreeOfFreedom.StepFEA_ZRotation, 'StepFEA_Warp': StepFEA_EnumeratedDegreeOfFreedom.StepFEA_Warp}
    pass
class StepFEA_FeaMaterialPropertyRepresentationItem(OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaMaterialPropertyRepresentationItemRepresentation of STEP entity FeaMaterialPropertyRepresentationItemRepresentation of STEP entity FeaMaterialPropertyRepresentationItem
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
class StepFEA_FeaAxis2Placement3d(OCP.StepGeom.StepGeom_Axis2Placement3d, OCP.StepGeom.StepGeom_Placement, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaAxis2Placement3dRepresentation of STEP entity FeaAxis2Placement3dRepresentation of STEP entity FeaAxis2Placement3d
    """
    def Axis(self) -> OCP.StepGeom.StepGeom_Direction: 
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
    def HasAxis(self) -> bool: 
        """
        None
        """
    def HasRefDirection(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aPlacement_Location : OCP.StepGeom.StepGeom_CartesianPoint,hasAxis2Placement3d_Axis : bool,aAxis2Placement3d_Axis : OCP.StepGeom.StepGeom_Direction,hasAxis2Placement3d_RefDirection : bool,aAxis2Placement3d_RefDirection : OCP.StepGeom.StepGeom_Direction,aSystemType : StepFEA_CoordinateSystemType,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Location(self) -> OCP.StepGeom.StepGeom_CartesianPoint: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def RefDirection(self) -> OCP.StepGeom.StepGeom_Direction: 
        """
        None
        """
    def SetAxis(self,aAxis : OCP.StepGeom.StepGeom_Direction) -> None: 
        """
        None
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetLocation(self,aLocation : OCP.StepGeom.StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRefDirection(self,aRefDirection : OCP.StepGeom.StepGeom_Direction) -> None: 
        """
        None
        """
    def SetSystemType(self,SystemType : StepFEA_CoordinateSystemType) -> None: 
        """
        Set field SystemType
        """
    def SystemType(self) -> StepFEA_CoordinateSystemType: 
        """
        Returns field SystemType
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetAxis(self) -> None: 
        """
        None
        """
    def UnSetRefDirection(self) -> None: 
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
class StepFEA_FeaCurveSectionGeometricRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaCurveSectionGeometricRelationshipRepresentation of STEP entity FeaCurveSectionGeometricRelationshipRepresentation of STEP entity FeaCurveSectionGeometricRelationship
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
    def Init(self,aSectionRef : OCP.StepElement.StepElement_CurveElementSectionDefinition,aItem : OCP.StepElement.StepElement_AnalysisItemWithinRepresentation) -> None: 
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
    def Item(self) -> OCP.StepElement.StepElement_AnalysisItemWithinRepresentation: 
        """
        Returns field Item
        """
    def SectionRef(self) -> OCP.StepElement.StepElement_CurveElementSectionDefinition: 
        """
        Returns field SectionRef
        """
    def SetItem(self,Item : OCP.StepElement.StepElement_AnalysisItemWithinRepresentation) -> None: 
        """
        Set field Item
        """
    def SetSectionRef(self,SectionRef : OCP.StepElement.StepElement_CurveElementSectionDefinition) -> None: 
        """
        Set field SectionRef
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
class StepFEA_ElementGroup(StepFEA_FeaGroup, OCP.StepBasic.StepBasic_Group, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ElementGroupRepresentation of STEP entity ElementGroupRepresentation of STEP entity ElementGroup
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
    def Elements(self) -> StepFEA_HArray1OfElementRepresentation: 
        """
        Returns field Elements
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
    def Init(self,aGroup_Name : OCP.TCollection.TCollection_HAsciiString,aGroup_Description : OCP.TCollection.TCollection_HAsciiString,aFeaGroup_ModelRef : StepFEA_FeaModel,aElements : StepFEA_HArray1OfElementRepresentation) -> None: 
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
    def ModelRef(self) -> StepFEA_FeaModel: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetElements(self,Elements : StepFEA_HArray1OfElementRepresentation) -> None: 
        """
        Set field Elements
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel) -> None: 
        """
        Set field ModelRef
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
class StepFEA_FeaLinearElasticity(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaLinearElasticityRepresentation of STEP entity FeaLinearElasticityRepresentation of STEP entity FeaLinearElasticity
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
    def FeaConstants(self) -> StepFEA_SymmetricTensor43d: 
        """
        Returns field FeaConstants
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstants : StepFEA_SymmetricTensor43d) -> None: 
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
    def SetFeaConstants(self,FeaConstants : StepFEA_SymmetricTensor43d) -> None: 
        """
        Set field FeaConstants
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
class StepFEA_FeaMassDensity(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaMassDensityRepresentation of STEP entity FeaMassDensityRepresentation of STEP entity FeaMassDensity
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
    def FeaConstant(self) -> float: 
        """
        Returns field FeaConstant
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstant : float) -> None: 
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
    def SetFeaConstant(self,FeaConstant : float) -> None: 
        """
        Set field FeaConstant
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
class StepFEA_FeaMaterialPropertyRepresentation(OCP.StepRepr.StepRepr_MaterialPropertyRepresentation, OCP.StepRepr.StepRepr_PropertyDefinitionRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaMaterialPropertyRepresentationRepresentation of STEP entity FeaMaterialPropertyRepresentationRepresentation of STEP entity FeaMaterialPropertyRepresentation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> OCP.StepRepr.StepRepr_RepresentedDefinition: 
        """
        Returns field Definition
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DependentEnvironment(self) -> OCP.StepRepr.StepRepr_DataEnvironment: 
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
    def Init(self,aPropertyDefinitionRepresentation_Definition : OCP.StepRepr.StepRepr_RepresentedDefinition,aPropertyDefinitionRepresentation_UsedRepresentation : OCP.StepRepr.StepRepr_Representation,aDependentEnvironment : OCP.StepRepr.StepRepr_DataEnvironment) -> None: 
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
    def SetDefinition(self,Definition : OCP.StepRepr.StepRepr_RepresentedDefinition) -> None: 
        """
        Set field Definition
        """
    def SetDependentEnvironment(self,DependentEnvironment : OCP.StepRepr.StepRepr_DataEnvironment) -> None: 
        """
        Set field DependentEnvironment
        """
    def SetUsedRepresentation(self,UsedRepresentation : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        Set field UsedRepresentation
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UsedRepresentation(self) -> OCP.StepRepr.StepRepr_Representation: 
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
class StepFEA_FeaAreaDensity(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaAreaDensityRepresentation of STEP entity FeaAreaDensityRepresentation of STEP entity FeaAreaDensity
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
    def FeaConstant(self) -> float: 
        """
        Returns field FeaConstant
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstant : float) -> None: 
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
    def SetFeaConstant(self,FeaConstant : float) -> None: 
        """
        Set field FeaConstant
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
class StepFEA_FeaModel(OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaModelRepresentation of STEP entity FeaModelRepresentation of STEP entity FeaModel
    """
    def AnalysisType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field AnalysisType
        """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
        """
        None
        """
    def CreatingSoftware(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field CreatingSoftware
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
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aCreatingSoftware : OCP.TCollection.TCollection_HAsciiString,aIntendedAnalysisCode : OCP.TColStd.TColStd_HArray1OfAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aAnalysisType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
        """
    def IntendedAnalysisCode(self) -> OCP.TColStd.TColStd_HArray1OfAsciiString: 
        """
        Returns field IntendedAnalysisCode
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
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
    def SetAnalysisType(self,AnalysisType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field AnalysisType
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetCreatingSoftware(self,CreatingSoftware : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field CreatingSoftware
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetIntendedAnalysisCode(self,IntendedAnalysisCode : OCP.TColStd.TColStd_HArray1OfAsciiString) -> None: 
        """
        Set field IntendedAnalysisCode
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
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
class StepFEA_FeaModel3d(StepFEA_FeaModel, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaModel3dRepresentation of STEP entity FeaModel3dRepresentation of STEP entity FeaModel3d
    """
    def AnalysisType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field AnalysisType
        """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
        """
        None
        """
    def CreatingSoftware(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field CreatingSoftware
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
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aCreatingSoftware : OCP.TCollection.TCollection_HAsciiString,aIntendedAnalysisCode : OCP.TColStd.TColStd_HArray1OfAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aAnalysisType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
        """
    def IntendedAnalysisCode(self) -> OCP.TColStd.TColStd_HArray1OfAsciiString: 
        """
        Returns field IntendedAnalysisCode
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
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
    def SetAnalysisType(self,AnalysisType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field AnalysisType
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetCreatingSoftware(self,CreatingSoftware : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field CreatingSoftware
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetIntendedAnalysisCode(self,IntendedAnalysisCode : OCP.TColStd.TColStd_HArray1OfAsciiString) -> None: 
        """
        Set field IntendedAnalysisCode
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
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
class StepFEA_FeaModelDefinition(OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaModelDefinitionRepresentation of STEP entity FeaModelDefinitionRepresentation of STEP entity FeaModelDefinition
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def OfShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
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
    def SetOfShape(self,aOfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape) -> None: 
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
class StepFEA_FeaMoistureAbsorption(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaMoistureAbsorptionRepresentation of STEP entity FeaMoistureAbsorptionRepresentation of STEP entity FeaMoistureAbsorption
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
    def FeaConstants(self) -> StepFEA_SymmetricTensor23d: 
        """
        Returns field FeaConstants
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstants : StepFEA_SymmetricTensor23d) -> None: 
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
    def SetFeaConstants(self,FeaConstants : StepFEA_SymmetricTensor23d) -> None: 
        """
        Set field FeaConstants
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
class StepFEA_FeaParametricPoint(OCP.StepGeom.StepGeom_Point, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaParametricPointRepresentation of STEP entity FeaParametricPointRepresentation of STEP entity FeaParametricPoint
    """
    def Coordinates(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns field Coordinates
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aCoordinates : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
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
    def SetCoordinates(self,Coordinates : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Set field Coordinates
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
class StepFEA_AlignedCurve3dElementCoordinateSystem(StepFEA_FeaRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity AlignedCurve3dElementCoordinateSystemRepresentation of STEP entity AlignedCurve3dElementCoordinateSystemRepresentation of STEP entity AlignedCurve3dElementCoordinateSystem
    """
    def CoordinateSystem(self) -> StepFEA_FeaAxis2Placement3d: 
        """
        Returns field CoordinateSystem
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aCoordinateSystem : StepFEA_FeaAxis2Placement3d) -> None: 
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
    def SetCoordinateSystem(self,CoordinateSystem : StepFEA_FeaAxis2Placement3d) -> None: 
        """
        Set field CoordinateSystem
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
class StepFEA_FeaSecantCoefficientOfLinearThermalExpansion(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaSecantCoefficientOfLinearThermalExpansionRepresentation of STEP entity FeaSecantCoefficientOfLinearThermalExpansionRepresentation of STEP entity FeaSecantCoefficientOfLinearThermalExpansion
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
    def FeaConstants(self) -> StepFEA_SymmetricTensor23d: 
        """
        Returns field FeaConstants
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstants : StepFEA_SymmetricTensor23d,aReferenceTemperature : float) -> None: 
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
    def ReferenceTemperature(self) -> float: 
        """
        Returns field ReferenceTemperature
        """
    def SetFeaConstants(self,FeaConstants : StepFEA_SymmetricTensor23d) -> None: 
        """
        Set field FeaConstants
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetReferenceTemperature(self,ReferenceTemperature : float) -> None: 
        """
        Set field ReferenceTemperature
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
class StepFEA_FeaShellBendingStiffness(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaShellBendingStiffnessRepresentation of STEP entity FeaShellBendingStiffnessRepresentation of STEP entity FeaShellBendingStiffness
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
    def FeaConstants(self) -> StepFEA_SymmetricTensor42d: 
        """
        Returns field FeaConstants
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstants : StepFEA_SymmetricTensor42d) -> None: 
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
    def SetFeaConstants(self,FeaConstants : StepFEA_SymmetricTensor42d) -> None: 
        """
        Set field FeaConstants
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
class StepFEA_FeaShellMembraneBendingCouplingStiffness(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaShellMembraneBendingCouplingStiffnessRepresentation of STEP entity FeaShellMembraneBendingCouplingStiffnessRepresentation of STEP entity FeaShellMembraneBendingCouplingStiffness
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
    def FeaConstants(self) -> StepFEA_SymmetricTensor42d: 
        """
        Returns field FeaConstants
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstants : StepFEA_SymmetricTensor42d) -> None: 
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
    def SetFeaConstants(self,FeaConstants : StepFEA_SymmetricTensor42d) -> None: 
        """
        Set field FeaConstants
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
class StepFEA_FeaShellMembraneStiffness(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaShellMembraneStiffnessRepresentation of STEP entity FeaShellMembraneStiffnessRepresentation of STEP entity FeaShellMembraneStiffness
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
    def FeaConstants(self) -> StepFEA_SymmetricTensor42d: 
        """
        Returns field FeaConstants
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstants : StepFEA_SymmetricTensor42d) -> None: 
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
    def SetFeaConstants(self,FeaConstants : StepFEA_SymmetricTensor42d) -> None: 
        """
        Set field FeaConstants
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
class StepFEA_FeaShellShearStiffness(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaShellShearStiffnessRepresentation of STEP entity FeaShellShearStiffnessRepresentation of STEP entity FeaShellShearStiffness
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
    def FeaConstants(self) -> StepFEA_SymmetricTensor22d: 
        """
        Returns field FeaConstants
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstants : StepFEA_SymmetricTensor22d) -> None: 
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
    def SetFeaConstants(self,FeaConstants : StepFEA_SymmetricTensor22d) -> None: 
        """
        Set field FeaConstants
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
class StepFEA_FeaSurfaceSectionGeometricRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaSurfaceSectionGeometricRelationshipRepresentation of STEP entity FeaSurfaceSectionGeometricRelationshipRepresentation of STEP entity FeaSurfaceSectionGeometricRelationship
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
    def Init(self,aSectionRef : OCP.StepElement.StepElement_SurfaceSection,aItem : OCP.StepElement.StepElement_AnalysisItemWithinRepresentation) -> None: 
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
    def Item(self) -> OCP.StepElement.StepElement_AnalysisItemWithinRepresentation: 
        """
        Returns field Item
        """
    def SectionRef(self) -> OCP.StepElement.StepElement_SurfaceSection: 
        """
        Returns field SectionRef
        """
    def SetItem(self,Item : OCP.StepElement.StepElement_AnalysisItemWithinRepresentation) -> None: 
        """
        Set field Item
        """
    def SetSectionRef(self,SectionRef : OCP.StepElement.StepElement_SurfaceSection) -> None: 
        """
        Set field SectionRef
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
class StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion(StepFEA_FeaMaterialPropertyRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FeaTangentialCoefficientOfLinearThermalExpansionRepresentation of STEP entity FeaTangentialCoefficientOfLinearThermalExpansionRepresentation of STEP entity FeaTangentialCoefficientOfLinearThermalExpansion
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
    def FeaConstants(self) -> StepFEA_SymmetricTensor23d: 
        """
        Returns field FeaConstants
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFeaConstants : StepFEA_SymmetricTensor23d) -> None: 
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
    def SetFeaConstants(self,FeaConstants : StepFEA_SymmetricTensor23d) -> None: 
        """
        Set field FeaConstants
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
class StepFEA_FreedomAndCoefficient(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FreedomAndCoefficientRepresentation of STEP entity FreedomAndCoefficientRepresentation of STEP entity FreedomAndCoefficient
    """
    def A(self) -> OCP.StepElement.StepElement_MeasureOrUnspecifiedValue: 
        """
        Returns field A
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
    def Freedom(self) -> StepFEA_DegreeOfFreedom: 
        """
        Returns field Freedom
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aFreedom : StepFEA_DegreeOfFreedom,aA : OCP.StepElement.StepElement_MeasureOrUnspecifiedValue) -> None: 
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
    def SetA(self,A : OCP.StepElement.StepElement_MeasureOrUnspecifiedValue) -> None: 
        """
        Set field A
        """
    def SetFreedom(self,Freedom : StepFEA_DegreeOfFreedom) -> None: 
        """
        Set field Freedom
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
class StepFEA_FreedomsList(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FreedomsListRepresentation of STEP entity FreedomsListRepresentation of STEP entity FreedomsList
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
    def Freedoms(self) -> StepFEA_HArray1OfDegreeOfFreedom: 
        """
        Returns field Freedoms
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aFreedoms : StepFEA_HArray1OfDegreeOfFreedom) -> None: 
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
    def SetFreedoms(self,Freedoms : StepFEA_HArray1OfDegreeOfFreedom) -> None: 
        """
        Set field Freedoms
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
class StepFEA_GeometricNode(StepFEA_NodeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeometricNodeRepresentation of STEP entity GeometricNodeRepresentation of STEP entity GeometricNode
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aModelRef : StepFEA_FeaModel) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ModelRef(self) -> StepFEA_FeaModel: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel) -> None: 
        """
        Set field ModelRef
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
class StepFEA_HArray1OfCurveElementEndOffset(StepFEA_Array1OfCurveElementEndOffset, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepFEA_Array1OfCurveElementEndOffset: 
        """
        None
        """
    def Assign(self,theOther : StepFEA_Array1OfCurveElementEndOffset) -> StepFEA_Array1OfCurveElementEndOffset: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepFEA_Array1OfCurveElementEndOffset: 
        """
        None
        """
    def ChangeFirst(self) -> StepFEA_CurveElementEndOffset: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_CurveElementEndOffset: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_CurveElementEndOffset: 
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
    def First(self) -> StepFEA_CurveElementEndOffset: 
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
    def Init(self,theValue : StepFEA_CurveElementEndOffset) -> None: 
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
    def Last(self) -> StepFEA_CurveElementEndOffset: 
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
    def Move(self,theOther : StepFEA_Array1OfCurveElementEndOffset) -> StepFEA_Array1OfCurveElementEndOffset: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_CurveElementEndOffset) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_CurveElementEndOffset: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepFEA_CurveElementEndOffset) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfCurveElementEndOffset) -> None: ...
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
class StepFEA_HArray1OfCurveElementEndRelease(StepFEA_Array1OfCurveElementEndRelease, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepFEA_Array1OfCurveElementEndRelease: 
        """
        None
        """
    def Assign(self,theOther : StepFEA_Array1OfCurveElementEndRelease) -> StepFEA_Array1OfCurveElementEndRelease: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepFEA_Array1OfCurveElementEndRelease: 
        """
        None
        """
    def ChangeFirst(self) -> StepFEA_CurveElementEndRelease: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_CurveElementEndRelease: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_CurveElementEndRelease: 
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
    def First(self) -> StepFEA_CurveElementEndRelease: 
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
    def Init(self,theValue : StepFEA_CurveElementEndRelease) -> None: 
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
    def Last(self) -> StepFEA_CurveElementEndRelease: 
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
    def Move(self,theOther : StepFEA_Array1OfCurveElementEndRelease) -> StepFEA_Array1OfCurveElementEndRelease: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_CurveElementEndRelease) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_CurveElementEndRelease: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepFEA_Array1OfCurveElementEndRelease) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepFEA_CurveElementEndRelease) -> None: ...
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
class StepFEA_HArray1OfCurveElementInterval(StepFEA_Array1OfCurveElementInterval, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepFEA_Array1OfCurveElementInterval: 
        """
        None
        """
    def Assign(self,theOther : StepFEA_Array1OfCurveElementInterval) -> StepFEA_Array1OfCurveElementInterval: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepFEA_Array1OfCurveElementInterval: 
        """
        None
        """
    def ChangeFirst(self) -> StepFEA_CurveElementInterval: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_CurveElementInterval: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_CurveElementInterval: 
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
    def First(self) -> StepFEA_CurveElementInterval: 
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
    def Init(self,theValue : StepFEA_CurveElementInterval) -> None: 
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
    def Last(self) -> StepFEA_CurveElementInterval: 
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
    def Move(self,theOther : StepFEA_Array1OfCurveElementInterval) -> StepFEA_Array1OfCurveElementInterval: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_CurveElementInterval) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_CurveElementInterval: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfCurveElementInterval) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepFEA_CurveElementInterval) -> None: ...
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
class StepFEA_HArray1OfDegreeOfFreedom(StepFEA_Array1OfDegreeOfFreedom, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepFEA_Array1OfDegreeOfFreedom: 
        """
        None
        """
    def Assign(self,theOther : StepFEA_Array1OfDegreeOfFreedom) -> StepFEA_Array1OfDegreeOfFreedom: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepFEA_Array1OfDegreeOfFreedom: 
        """
        None
        """
    def ChangeFirst(self) -> StepFEA_DegreeOfFreedom: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_DegreeOfFreedom: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_DegreeOfFreedom: 
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
    def First(self) -> StepFEA_DegreeOfFreedom: 
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
    def Init(self,theValue : StepFEA_DegreeOfFreedom) -> None: 
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
    def Last(self) -> StepFEA_DegreeOfFreedom: 
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
    def Move(self,theOther : StepFEA_Array1OfDegreeOfFreedom) -> StepFEA_Array1OfDegreeOfFreedom: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_DegreeOfFreedom) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_DegreeOfFreedom: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepFEA_DegreeOfFreedom) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfDegreeOfFreedom) -> None: ...
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
class StepFEA_HArray1OfElementRepresentation(StepFEA_Array1OfElementRepresentation, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepFEA_Array1OfElementRepresentation: 
        """
        None
        """
    def Assign(self,theOther : StepFEA_Array1OfElementRepresentation) -> StepFEA_Array1OfElementRepresentation: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepFEA_Array1OfElementRepresentation: 
        """
        None
        """
    def ChangeFirst(self) -> StepFEA_ElementRepresentation: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_ElementRepresentation: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_ElementRepresentation: 
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
    def First(self) -> StepFEA_ElementRepresentation: 
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
    def Init(self,theValue : StepFEA_ElementRepresentation) -> None: 
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
    def Last(self) -> StepFEA_ElementRepresentation: 
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
    def Move(self,theOther : StepFEA_Array1OfElementRepresentation) -> StepFEA_Array1OfElementRepresentation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_ElementRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_ElementRepresentation: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_Array1OfElementRepresentation) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepFEA_ElementRepresentation) -> None: ...
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
class StepFEA_HArray1OfNodeRepresentation(StepFEA_Array1OfNodeRepresentation, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepFEA_Array1OfNodeRepresentation: 
        """
        None
        """
    def Assign(self,theOther : StepFEA_Array1OfNodeRepresentation) -> StepFEA_Array1OfNodeRepresentation: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepFEA_Array1OfNodeRepresentation: 
        """
        None
        """
    def ChangeFirst(self) -> StepFEA_NodeRepresentation: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepFEA_NodeRepresentation: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_NodeRepresentation: 
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
    def First(self) -> StepFEA_NodeRepresentation: 
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
    def Init(self,theValue : StepFEA_NodeRepresentation) -> None: 
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
    def Last(self) -> StepFEA_NodeRepresentation: 
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
    def Move(self,theOther : StepFEA_Array1OfNodeRepresentation) -> StepFEA_Array1OfNodeRepresentation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_NodeRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_NodeRepresentation: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepFEA_Array1OfNodeRepresentation) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepFEA_NodeRepresentation) -> None: ...
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
class StepFEA_SequenceOfCurve3dElementProperty(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : StepFEA_SequenceOfCurve3dElementProperty) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : StepFEA_Curve3dElementProperty) -> None: ...
    def Assign(self,theOther : StepFEA_SequenceOfCurve3dElementProperty) -> StepFEA_SequenceOfCurve3dElementProperty: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepFEA_Curve3dElementProperty: 
        """
        First item access
        """
    def ChangeLast(self) -> StepFEA_Curve3dElementProperty: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_Curve3dElementProperty: 
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
    def First(self) -> StepFEA_Curve3dElementProperty: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepFEA_SequenceOfCurve3dElementProperty) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepFEA_Curve3dElementProperty) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepFEA_SequenceOfCurve3dElementProperty) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepFEA_Curve3dElementProperty) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepFEA_Curve3dElementProperty: 
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
    def Prepend(self,theSeq : StepFEA_SequenceOfCurve3dElementProperty) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : StepFEA_Curve3dElementProperty) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StepFEA_Curve3dElementProperty) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepFEA_SequenceOfCurve3dElementProperty) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepFEA_Curve3dElementProperty: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StepFEA_SequenceOfCurve3dElementProperty) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StepFEA_SequenceOfElementGeometricRelationship(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepFEA_ElementGeometricRelationship) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : StepFEA_SequenceOfElementGeometricRelationship) -> None: ...
    def Assign(self,theOther : StepFEA_SequenceOfElementGeometricRelationship) -> StepFEA_SequenceOfElementGeometricRelationship: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepFEA_ElementGeometricRelationship: 
        """
        First item access
        """
    def ChangeLast(self) -> StepFEA_ElementGeometricRelationship: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_ElementGeometricRelationship: 
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
    def First(self) -> StepFEA_ElementGeometricRelationship: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepFEA_ElementGeometricRelationship) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepFEA_SequenceOfElementGeometricRelationship) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepFEA_SequenceOfElementGeometricRelationship) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepFEA_ElementGeometricRelationship) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepFEA_ElementGeometricRelationship: 
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
    def Prepend(self,theItem : StepFEA_ElementGeometricRelationship) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepFEA_SequenceOfElementGeometricRelationship) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StepFEA_ElementGeometricRelationship) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepFEA_SequenceOfElementGeometricRelationship) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepFEA_ElementGeometricRelationship: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_SequenceOfElementGeometricRelationship) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StepFEA_SequenceOfElementRepresentation(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : StepFEA_SequenceOfElementRepresentation) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : StepFEA_ElementRepresentation) -> None: ...
    def Assign(self,theOther : StepFEA_SequenceOfElementRepresentation) -> StepFEA_SequenceOfElementRepresentation: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepFEA_ElementRepresentation: 
        """
        First item access
        """
    def ChangeLast(self) -> StepFEA_ElementRepresentation: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_ElementRepresentation: 
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
    def First(self) -> StepFEA_ElementRepresentation: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepFEA_ElementRepresentation) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepFEA_SequenceOfElementRepresentation) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepFEA_SequenceOfElementRepresentation) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepFEA_ElementRepresentation) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepFEA_ElementRepresentation: 
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
    def Prepend(self,theSeq : StepFEA_SequenceOfElementRepresentation) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : StepFEA_ElementRepresentation) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StepFEA_ElementRepresentation) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepFEA_SequenceOfElementRepresentation) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepFEA_ElementRepresentation: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_SequenceOfElementRepresentation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StepFEA_SequenceOfNodeRepresentation(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepFEA_NodeRepresentation) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : StepFEA_SequenceOfNodeRepresentation) -> None: ...
    def Assign(self,theOther : StepFEA_SequenceOfNodeRepresentation) -> StepFEA_SequenceOfNodeRepresentation: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepFEA_NodeRepresentation: 
        """
        First item access
        """
    def ChangeLast(self) -> StepFEA_NodeRepresentation: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_NodeRepresentation: 
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
    def First(self) -> StepFEA_NodeRepresentation: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepFEA_NodeRepresentation) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepFEA_SequenceOfNodeRepresentation) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepFEA_SequenceOfNodeRepresentation) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepFEA_NodeRepresentation) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> StepFEA_NodeRepresentation: 
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
    def Prepend(self,theItem : StepFEA_NodeRepresentation) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepFEA_SequenceOfNodeRepresentation) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : StepFEA_NodeRepresentation) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepFEA_SequenceOfNodeRepresentation) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> StepFEA_NodeRepresentation: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StepFEA_SequenceOfNodeRepresentation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class StepFEA_Node(StepFEA_NodeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NodeRepresentation of STEP entity NodeRepresentation of STEP entity Node
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aModelRef : StepFEA_FeaModel) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ModelRef(self) -> StepFEA_FeaModel: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel) -> None: 
        """
        Set field ModelRef
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
class StepFEA_NodeDefinition(OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NodeDefinitionRepresentation of STEP entity NodeDefinitionRepresentation of STEP entity NodeDefinition
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aOfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,aProductDefinitional : OCP.StepData.StepData_Logical) -> None: 
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
    def OfShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
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
    def SetOfShape(self,aOfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape) -> None: 
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
class StepFEA_NodeGroup(StepFEA_FeaGroup, OCP.StepBasic.StepBasic_Group, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NodeGroupRepresentation of STEP entity NodeGroupRepresentation of STEP entity NodeGroup
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
    def Init(self,aGroup_Name : OCP.TCollection.TCollection_HAsciiString,aGroup_Description : OCP.TCollection.TCollection_HAsciiString,aFeaGroup_ModelRef : StepFEA_FeaModel,aNodes : StepFEA_HArray1OfNodeRepresentation) -> None: 
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
    def ModelRef(self) -> StepFEA_FeaModel: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def Nodes(self) -> StepFEA_HArray1OfNodeRepresentation: 
        """
        Returns field Nodes
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel) -> None: 
        """
        Set field ModelRef
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetNodes(self,Nodes : StepFEA_HArray1OfNodeRepresentation) -> None: 
        """
        Set field Nodes
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
class StepFEA_DummyNode(StepFEA_NodeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DummyNodeRepresentation of STEP entity DummyNodeRepresentation of STEP entity DummyNode
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aModelRef : StepFEA_FeaModel) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ModelRef(self) -> StepFEA_FeaModel: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel) -> None: 
        """
        Set field ModelRef
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
class StepFEA_NodeSet(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NodeSetRepresentation of STEP entity NodeSetRepresentation of STEP entity NodeSet
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aNodes : StepFEA_HArray1OfNodeRepresentation) -> None: 
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
    def Nodes(self) -> StepFEA_HArray1OfNodeRepresentation: 
        """
        Returns field Nodes
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetNodes(self,Nodes : StepFEA_HArray1OfNodeRepresentation) -> None: 
        """
        Set field Nodes
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
class StepFEA_NodeWithSolutionCoordinateSystem(StepFEA_Node, StepFEA_NodeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NodeWithSolutionCoordinateSystemRepresentation of STEP entity NodeWithSolutionCoordinateSystemRepresentation of STEP entity NodeWithSolutionCoordinateSystem
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aModelRef : StepFEA_FeaModel) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ModelRef(self) -> StepFEA_FeaModel: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel) -> None: 
        """
        Set field ModelRef
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
class StepFEA_NodeWithVector(StepFEA_Node, StepFEA_NodeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NodeWithVectorRepresentation of STEP entity NodeWithVectorRepresentation of STEP entity NodeWithVector
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aModelRef : StepFEA_FeaModel) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ModelRef(self) -> StepFEA_FeaModel: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel) -> None: 
        """
        Set field ModelRef
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
class StepFEA_ParametricCurve3dElementCoordinateDirection(StepFEA_FeaRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ParametricCurve3dElementCoordinateDirectionRepresentation of STEP entity ParametricCurve3dElementCoordinateDirectionRepresentation of STEP entity ParametricCurve3dElementCoordinateDirection
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aOrientation : OCP.StepGeom.StepGeom_Direction) -> None: 
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
    def Orientation(self) -> OCP.StepGeom.StepGeom_Direction: 
        """
        Returns field Orientation
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,Orientation : OCP.StepGeom.StepGeom_Direction) -> None: 
        """
        Set field Orientation
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
class StepFEA_ParametricCurve3dElementCoordinateSystem(StepFEA_FeaRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ParametricCurve3dElementCoordinateSystemRepresentation of STEP entity ParametricCurve3dElementCoordinateSystemRepresentation of STEP entity ParametricCurve3dElementCoordinateSystem
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> StepFEA_ParametricCurve3dElementCoordinateDirection: 
        """
        Returns field Direction
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aDirection : StepFEA_ParametricCurve3dElementCoordinateDirection) -> None: 
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
    def SetDirection(self,Direction : StepFEA_ParametricCurve3dElementCoordinateDirection) -> None: 
        """
        Set field Direction
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
class StepFEA_ParametricSurface3dElementCoordinateSystem(StepFEA_FeaRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ParametricSurface3dElementCoordinateSystemRepresentation of STEP entity ParametricSurface3dElementCoordinateSystemRepresentation of STEP entity ParametricSurface3dElementCoordinateSystem
    """
    def Angle(self) -> float: 
        """
        Returns field Angle
        """
    def Axis(self) -> int: 
        """
        Returns field Axis
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aAxis : int,aAngle : float) -> None: 
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
    def SetAngle(self,Angle : float) -> None: 
        """
        Set field Angle
        """
    def SetAxis(self,Axis : int) -> None: 
        """
        Set field Axis
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
class StepFEA_HSequenceOfCurve3dElementProperty(StepFEA_SequenceOfCurve3dElementProperty, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepFEA_Curve3dElementProperty) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : StepFEA_SequenceOfCurve3dElementProperty) -> None: ...
    def Assign(self,theOther : StepFEA_SequenceOfCurve3dElementProperty) -> StepFEA_SequenceOfCurve3dElementProperty: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepFEA_Curve3dElementProperty: 
        """
        First item access
        """
    def ChangeLast(self) -> StepFEA_Curve3dElementProperty: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepFEA_SequenceOfCurve3dElementProperty: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_Curve3dElementProperty: 
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
    def First(self) -> StepFEA_Curve3dElementProperty: 
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
    def InsertAfter(self,theIndex : int,theSeq : StepFEA_SequenceOfCurve3dElementProperty) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : StepFEA_Curve3dElementProperty) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepFEA_SequenceOfCurve3dElementProperty) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepFEA_Curve3dElementProperty) -> None: ...
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
    def Last(self) -> StepFEA_Curve3dElementProperty: 
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
    def Prepend(self,theSeq : StepFEA_SequenceOfCurve3dElementProperty) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : StepFEA_Curve3dElementProperty) -> None: ...
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
    def Sequence(self) -> StepFEA_SequenceOfCurve3dElementProperty: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_Curve3dElementProperty) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepFEA_SequenceOfCurve3dElementProperty) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_Curve3dElementProperty: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StepFEA_SequenceOfCurve3dElementProperty) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepFEA_HSequenceOfElementGeometricRelationship(StepFEA_SequenceOfElementGeometricRelationship, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepFEA_ElementGeometricRelationship) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : StepFEA_SequenceOfElementGeometricRelationship) -> None: ...
    def Assign(self,theOther : StepFEA_SequenceOfElementGeometricRelationship) -> StepFEA_SequenceOfElementGeometricRelationship: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepFEA_ElementGeometricRelationship: 
        """
        First item access
        """
    def ChangeLast(self) -> StepFEA_ElementGeometricRelationship: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepFEA_SequenceOfElementGeometricRelationship: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_ElementGeometricRelationship: 
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
    def First(self) -> StepFEA_ElementGeometricRelationship: 
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
    def InsertAfter(self,theIndex : int,theItem : StepFEA_ElementGeometricRelationship) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepFEA_SequenceOfElementGeometricRelationship) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepFEA_SequenceOfElementGeometricRelationship) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepFEA_ElementGeometricRelationship) -> None: ...
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
    def Last(self) -> StepFEA_ElementGeometricRelationship: 
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
    def Prepend(self,theItem : StepFEA_ElementGeometricRelationship) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepFEA_SequenceOfElementGeometricRelationship) -> None: ...
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
    def Sequence(self) -> StepFEA_SequenceOfElementGeometricRelationship: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_ElementGeometricRelationship) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepFEA_SequenceOfElementGeometricRelationship) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_ElementGeometricRelationship: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_SequenceOfElementGeometricRelationship) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepFEA_HSequenceOfElementRepresentation(StepFEA_SequenceOfElementRepresentation, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : StepFEA_SequenceOfElementRepresentation) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : StepFEA_ElementRepresentation) -> None: ...
    def Assign(self,theOther : StepFEA_SequenceOfElementRepresentation) -> StepFEA_SequenceOfElementRepresentation: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepFEA_ElementRepresentation: 
        """
        First item access
        """
    def ChangeLast(self) -> StepFEA_ElementRepresentation: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepFEA_SequenceOfElementRepresentation: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_ElementRepresentation: 
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
    def First(self) -> StepFEA_ElementRepresentation: 
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
    def InsertAfter(self,theIndex : int,theItem : StepFEA_ElementRepresentation) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepFEA_SequenceOfElementRepresentation) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepFEA_SequenceOfElementRepresentation) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepFEA_ElementRepresentation) -> None: ...
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
    def Last(self) -> StepFEA_ElementRepresentation: 
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
    def Prepend(self,theSeq : StepFEA_SequenceOfElementRepresentation) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : StepFEA_ElementRepresentation) -> None: ...
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
    def Sequence(self) -> StepFEA_SequenceOfElementRepresentation: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_ElementRepresentation) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepFEA_SequenceOfElementRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_ElementRepresentation: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : StepFEA_SequenceOfElementRepresentation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepFEA_HSequenceOfNodeRepresentation(StepFEA_SequenceOfNodeRepresentation, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : StepFEA_NodeRepresentation) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : StepFEA_SequenceOfNodeRepresentation) -> None: ...
    def Assign(self,theOther : StepFEA_SequenceOfNodeRepresentation) -> StepFEA_SequenceOfNodeRepresentation: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> StepFEA_NodeRepresentation: 
        """
        First item access
        """
    def ChangeLast(self) -> StepFEA_NodeRepresentation: 
        """
        Last item access
        """
    def ChangeSequence(self) -> StepFEA_SequenceOfNodeRepresentation: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> StepFEA_NodeRepresentation: 
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
    def First(self) -> StepFEA_NodeRepresentation: 
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
    def InsertAfter(self,theIndex : int,theItem : StepFEA_NodeRepresentation) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : StepFEA_SequenceOfNodeRepresentation) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : StepFEA_SequenceOfNodeRepresentation) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : StepFEA_NodeRepresentation) -> None: ...
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
    def Last(self) -> StepFEA_NodeRepresentation: 
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
    def Prepend(self,theItem : StepFEA_NodeRepresentation) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : StepFEA_SequenceOfNodeRepresentation) -> None: ...
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
    def Sequence(self) -> StepFEA_SequenceOfNodeRepresentation: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : StepFEA_NodeRepresentation) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : StepFEA_SequenceOfNodeRepresentation) -> None: 
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
    def Value(self,theIndex : int) -> StepFEA_NodeRepresentation: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepFEA_SequenceOfNodeRepresentation) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepFEA_Surface3dElementRepresentation(StepFEA_ElementRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity Surface3dElementRepresentationRepresentation of STEP entity Surface3dElementRepresentationRepresentation of STEP entity Surface3dElementRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def ElementDescriptor(self) -> OCP.StepElement.StepElement_Surface3dElementDescriptor: 
        """
        Returns field ElementDescriptor
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aElementRepresentation_NodeList : StepFEA_HArray1OfNodeRepresentation,aModelRef : StepFEA_FeaModel3d,aElementDescriptor : OCP.StepElement.StepElement_Surface3dElementDescriptor,aProperty : OCP.StepElement.StepElement_SurfaceElementProperty,aMaterial : OCP.StepElement.StepElement_ElementMaterial) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Material(self) -> OCP.StepElement.StepElement_ElementMaterial: 
        """
        Returns field Material
        """
    def ModelRef(self) -> StepFEA_FeaModel3d: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def NodeList(self) -> StepFEA_HArray1OfNodeRepresentation: 
        """
        Returns field NodeList
        """
    def Property(self) -> OCP.StepElement.StepElement_SurfaceElementProperty: 
        """
        Returns field Property
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetElementDescriptor(self,ElementDescriptor : OCP.StepElement.StepElement_Surface3dElementDescriptor) -> None: 
        """
        Set field ElementDescriptor
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetMaterial(self,Material : OCP.StepElement.StepElement_ElementMaterial) -> None: 
        """
        Set field Material
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel3d) -> None: 
        """
        Set field ModelRef
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetNodeList(self,NodeList : StepFEA_HArray1OfNodeRepresentation) -> None: 
        """
        Set field NodeList
        """
    def SetProperty(self,Property : OCP.StepElement.StepElement_SurfaceElementProperty) -> None: 
        """
        Set field Property
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
class StepFEA_SymmetricTensor22d(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type SymmetricTensor22d
    """
    def AnisotropicSymmetricTensor22d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as AnisotropicSymmetricTensor22d (or Null if another type)
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
        Recognizes a kind of SymmetricTensor22d select type 1 -> HArray1OfReal from TColStd 0 else
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
class StepFEA_SymmetricTensor23d(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type SymmetricTensor23d
    """
    def AnisotropicSymmetricTensor23d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as AnisotropicSymmetricTensor23d (or Null if another type)
        """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a items of select member SymmetricTensor23dMember 1 -> IsotropicSymmetricTensor23d 2 -> OrthotropicSymmetricTensor23d 3 -> AnisotropicSymmetricTensor23d 0 else
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of SymmetricTensor23d select type return 0
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
    def IsotropicSymmetricTensor23d(self) -> float: 
        """
        Returns Value as IsotropicSymmetricTensor23d (or Null if another type)
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
        Returns a new select member the type SymmetricTensor23dMember
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def OrthotropicSymmetricTensor23d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as OrthotropicSymmetricTensor23d (or Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetAnisotropicSymmetricTensor23d(self,aVal : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Set Value for AnisotropicSymmetricTensor23d
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
    def SetIsotropicSymmetricTensor23d(self,aVal : float) -> None: 
        """
        Set Value for IsotropicSymmetricTensor23d
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetOrthotropicSymmetricTensor23d(self,aVal : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Set Value for OrthotropicSymmetricTensor23d
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
class StepFEA_SymmetricTensor23dMember(OCP.StepData.StepData_SelectArrReal, OCP.StepData.StepData_SelectNamed, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Representation of member for STEP SELECT type SymmetricTensor23dRepresentation of member for STEP SELECT type SymmetricTensor23dRepresentation of member for STEP SELECT type SymmetricTensor23d
    """
    def ArrReal(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
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
class StepFEA_SymmetricTensor42d(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type SymmetricTensor42d
    """
    def AnisotropicSymmetricTensor42d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as AnisotropicSymmetricTensor42d (or Null if another type)
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
        Recognizes a kind of SymmetricTensor42d select type 1 -> HArray1OfReal from TColStd 0 else
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
class StepFEA_SymmetricTensor43d(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type SymmetricTensor43d
    """
    def AnisotropicSymmetricTensor43d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as AnisotropicSymmetricTensor43d (or Null if another type)
        """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a items of select member CurveElementFreedomMember 1 -> AnisotropicSymmetricTensor43d 2 -> FeaIsotropicSymmetricTensor43d 3 -> FeaIsoOrthotropicSymmetricTensor43d 4 -> FeaTransverseIsotropicSymmetricTensor43d 5 -> FeaColumnNormalisedOrthotropicSymmetricTensor43d 6 -> FeaColumnNormalisedMonoclinicSymmetricTensor43d 0 else
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        return 0
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def FeaColumnNormalisedMonoclinicSymmetricTensor43d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as FeaColumnNormalisedMonoclinicSymmetricTensor43d (or Null if another type)
        """
    def FeaColumnNormalisedOrthotropicSymmetricTensor43d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as FeaColumnNormalisedOrthotropicSymmetricTensor43d (or Null if another type)
        """
    def FeaIsoOrthotropicSymmetricTensor43d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as FeaIsoOrthotropicSymmetricTensor43d (or Null if another type)
        """
    def FeaIsotropicSymmetricTensor43d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as FeaIsotropicSymmetricTensor43d (or Null if another type)
        """
    def FeaTransverseIsotropicSymmetricTensor43d(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns Value as FeaTransverseIsotropicSymmetricTensor43d (or Null if another type)
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
        None
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
class StepFEA_SymmetricTensor43dMember(OCP.StepData.StepData_SelectArrReal, OCP.StepData.StepData_SelectNamed, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Representation of member for STEP SELECT type SymmetricTensor43dRepresentation of member for STEP SELECT type SymmetricTensor43dRepresentation of member for STEP SELECT type SymmetricTensor43d
    """
    def ArrReal(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
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
class StepFEA_UnspecifiedValue():
    """
    None

    Members:

      StepFEA_Unspecified
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
    StepFEA_Unspecified: OCP.StepFEA.StepFEA_UnspecifiedValue # value = StepFEA_UnspecifiedValue.StepFEA_Unspecified
    __entries: dict # value = {'StepFEA_Unspecified': (StepFEA_UnspecifiedValue.StepFEA_Unspecified, None)}
    __members__: dict # value = {'StepFEA_Unspecified': StepFEA_UnspecifiedValue.StepFEA_Unspecified}
    pass
class StepFEA_Volume3dElementRepresentation(StepFEA_ElementRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity Volume3dElementRepresentationRepresentation of STEP entity Volume3dElementRepresentationRepresentation of STEP entity Volume3dElementRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def ElementDescriptor(self) -> OCP.StepElement.StepElement_Volume3dElementDescriptor: 
        """
        Returns field ElementDescriptor
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentation_Name : OCP.TCollection.TCollection_HAsciiString,aRepresentation_Items : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aRepresentation_ContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext,aElementRepresentation_NodeList : StepFEA_HArray1OfNodeRepresentation,aModelRef : StepFEA_FeaModel3d,aElementDescriptor : OCP.StepElement.StepElement_Volume3dElementDescriptor,aMaterial : OCP.StepElement.StepElement_ElementMaterial) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Material(self) -> OCP.StepElement.StepElement_ElementMaterial: 
        """
        Returns field Material
        """
    def ModelRef(self) -> StepFEA_FeaModel3d: 
        """
        Returns field ModelRef
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def NodeList(self) -> StepFEA_HArray1OfNodeRepresentation: 
        """
        Returns field NodeList
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetElementDescriptor(self,ElementDescriptor : OCP.StepElement.StepElement_Volume3dElementDescriptor) -> None: 
        """
        Set field ElementDescriptor
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetMaterial(self,Material : OCP.StepElement.StepElement_ElementMaterial) -> None: 
        """
        Set field Material
        """
    def SetModelRef(self,ModelRef : StepFEA_FeaModel3d) -> None: 
        """
        Set field ModelRef
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetNodeList(self,NodeList : StepFEA_HArray1OfNodeRepresentation) -> None: 
        """
        Set field NodeList
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
StepFEA_Cartesian: OCP.StepFEA.StepFEA_CoordinateSystemType # value = StepFEA_CoordinateSystemType.StepFEA_Cartesian
StepFEA_Cylindrical: OCP.StepFEA.StepFEA_CoordinateSystemType # value = StepFEA_CoordinateSystemType.StepFEA_Cylindrical
StepFEA_ElementEdge: OCP.StepFEA.StepFEA_CurveEdge # value = StepFEA_CurveEdge.StepFEA_ElementEdge
StepFEA_Spherical: OCP.StepFEA.StepFEA_CoordinateSystemType # value = StepFEA_CoordinateSystemType.StepFEA_Spherical
StepFEA_Unspecified: OCP.StepFEA.StepFEA_UnspecifiedValue # value = StepFEA_UnspecifiedValue.StepFEA_Unspecified
StepFEA_Volume: OCP.StepFEA.StepFEA_ElementVolume # value = StepFEA_ElementVolume.StepFEA_Volume
StepFEA_Warp: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_Warp
StepFEA_XRotation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_XRotation
StepFEA_XTranslation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_XTranslation
StepFEA_YRotation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_YRotation
StepFEA_YTranslation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_YTranslation
StepFEA_ZRotation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_ZRotation
StepFEA_ZTranslation: OCP.StepFEA.StepFEA_EnumeratedDegreeOfFreedom # value = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_ZTranslation
