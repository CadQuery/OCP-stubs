import OCP.StepDimTol
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.StepBasic
import OCP.Interface
import OCP.Standard
import OCP.StepShape
import OCP.StepRepr
import OCP.StepData
__all__  = [
"StepDimTol_GeometricTolerance",
"StepDimTol_AreaUnitType",
"StepDimTol_Array1OfDatumReference",
"StepDimTol_Array1OfDatumReferenceCompartment",
"StepDimTol_Array1OfDatumReferenceElement",
"StepDimTol_Array1OfDatumReferenceModifier",
"StepDimTol_Array1OfDatumSystemOrReference",
"StepDimTol_Array1OfGeometricToleranceModifier",
"StepDimTol_Array1OfToleranceZoneTarget",
"StepDimTol_GeometricToleranceWithDatumReference",
"StepDimTol_CoaxialityTolerance",
"StepDimTol_CommonDatum",
"StepDimTol_ConcentricityTolerance",
"StepDimTol_CylindricityTolerance",
"StepDimTol_Datum",
"StepDimTol_DatumFeature",
"StepDimTol_DatumOrCommonDatum",
"StepDimTol_DatumReference",
"StepDimTol_GeneralDatumReference",
"StepDimTol_DatumReferenceElement",
"StepDimTol_DatumReferenceModifier",
"StepDimTol_DatumReferenceModifierType",
"StepDimTol_DatumReferenceModifierWithValue",
"StepDimTol_DatumSystem",
"StepDimTol_DatumSystemOrReference",
"StepDimTol_DatumTarget",
"StepDimTol_FlatnessTolerance",
"StepDimTol_DatumReferenceCompartment",
"StepDimTol_GeoTolAndGeoTolWthDatRef",
"StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod",
"StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol",
"StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol",
"StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol",
"StepDimTol_GeoTolAndGeoTolWthMod",
"StepDimTol_GeoTolAndGeoTolWthMaxTol",
"StepDimTol_AngularityTolerance",
"StepDimTol_GeometricToleranceModifier",
"StepDimTol_GeometricToleranceRelationship",
"StepDimTol_GeometricToleranceTarget",
"StepDimTol_GeometricToleranceType",
"StepDimTol_CircularRunoutTolerance",
"StepDimTol_GeometricToleranceWithDefinedUnit",
"StepDimTol_GeometricToleranceWithDefinedAreaUnit",
"StepDimTol_GeometricToleranceWithModifiers",
"StepDimTol_GeometricToleranceWithMaximumTolerance",
"StepDimTol_HArray1OfDatumReference",
"StepDimTol_HArray1OfDatumReferenceCompartment",
"StepDimTol_HArray1OfDatumReferenceElement",
"StepDimTol_HArray1OfDatumReferenceModifier",
"StepDimTol_HArray1OfDatumSystemOrReference",
"StepDimTol_HArray1OfGeometricToleranceModifier",
"StepDimTol_HArray1OfToleranceZoneTarget",
"StepDimTol_LimitCondition",
"StepDimTol_LineProfileTolerance",
"StepDimTol_ModifiedGeometricTolerance",
"StepDimTol_ToleranceZoneDefinition",
"StepDimTol_ParallelismTolerance",
"StepDimTol_PerpendicularityTolerance",
"StepDimTol_PlacedDatumTargetFeature",
"StepDimTol_PositionTolerance",
"StepDimTol_ProjectedZoneDefinition",
"StepDimTol_RoundnessTolerance",
"StepDimTol_RunoutZoneDefinition",
"StepDimTol_RunoutZoneOrientation",
"StepDimTol_ShapeToleranceSelect",
"StepDimTol_SimpleDatumReferenceModifier",
"StepDimTol_SimpleDatumReferenceModifierMember",
"StepDimTol_StraightnessTolerance",
"StepDimTol_SurfaceProfileTolerance",
"StepDimTol_SymmetryTolerance",
"StepDimTol_ToleranceZone",
"StepDimTol_NonUniformZoneDefinition",
"StepDimTol_ToleranceZoneForm",
"StepDimTol_ToleranceZoneTarget",
"StepDimTol_TotalRunoutTolerance",
"StepDimTol_UnequallyDisposedGeometricTolerance",
"StepDimTol_Circular",
"StepDimTol_CircularOrCylindrical",
"StepDimTol_Distance",
"StepDimTol_GTMAnyCrossSection",
"StepDimTol_GTMCommonZone",
"StepDimTol_GTMEachRadialElement",
"StepDimTol_GTMFreeState",
"StepDimTol_GTMLeastMaterialRequirement",
"StepDimTol_GTMLineElement",
"StepDimTol_GTMMajorDiameter",
"StepDimTol_GTMMaximumMaterialRequirement",
"StepDimTol_GTMMinorDiameter",
"StepDimTol_GTMNotConvex",
"StepDimTol_GTMPitchDiameter",
"StepDimTol_GTMReciprocityRequirement",
"StepDimTol_GTMSeparateRequirement",
"StepDimTol_GTMStatisticalTolerance",
"StepDimTol_GTMTangentPlane",
"StepDimTol_GTTAngularityTolerance",
"StepDimTol_GTTCircularRunoutTolerance",
"StepDimTol_GTTCoaxialityTolerance",
"StepDimTol_GTTConcentricityTolerance",
"StepDimTol_GTTCylindricityTolerance",
"StepDimTol_GTTFlatnessTolerance",
"StepDimTol_GTTLineProfileTolerance",
"StepDimTol_GTTParallelismTolerance",
"StepDimTol_GTTPerpendicularityTolerance",
"StepDimTol_GTTPositionTolerance",
"StepDimTol_GTTRoundnessTolerance",
"StepDimTol_GTTStraightnessTolerance",
"StepDimTol_GTTSurfaceProfileTolerance",
"StepDimTol_GTTSymmetryTolerance",
"StepDimTol_GTTTotalRunoutTolerance",
"StepDimTol_LeastMaterialCondition",
"StepDimTol_MaximumMaterialCondition",
"StepDimTol_Projected",
"StepDimTol_Rectangular",
"StepDimTol_RegardlessOfFeatureSize",
"StepDimTol_SDRMAnyCrossSection",
"StepDimTol_SDRMAnyLongitudinalSection",
"StepDimTol_SDRMBasic",
"StepDimTol_SDRMContactingFeature",
"StepDimTol_SDRMDegreeOfFreedomConstraintU",
"StepDimTol_SDRMDegreeOfFreedomConstraintV",
"StepDimTol_SDRMDegreeOfFreedomConstraintW",
"StepDimTol_SDRMDegreeOfFreedomConstraintX",
"StepDimTol_SDRMDegreeOfFreedomConstraintY",
"StepDimTol_SDRMDegreeOfFreedomConstraintZ",
"StepDimTol_SDRMDistanceVariable",
"StepDimTol_SDRMFreeState",
"StepDimTol_SDRMLeastMaterialRequirement",
"StepDimTol_SDRMLine",
"StepDimTol_SDRMMajorDiameter",
"StepDimTol_SDRMMaximumMaterialRequirement",
"StepDimTol_SDRMMinorDiameter",
"StepDimTol_SDRMOrientation",
"StepDimTol_SDRMPitchDiameter",
"StepDimTol_SDRMPlane",
"StepDimTol_SDRMPoint",
"StepDimTol_SDRMTranslation",
"StepDimTol_Spherical",
"StepDimTol_Square"
]
class StepDimTol_GeometricTolerance(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeometricToleranceRepresentation of STEP entity GeometricToleranceRepresentation of STEP entity GeometricTolerance
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
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_AreaUnitType():
    """
    None

    Members:

      StepDimTol_Circular

      StepDimTol_Rectangular

      StepDimTol_Square
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
    StepDimTol_Circular: OCP.StepDimTol.StepDimTol_AreaUnitType # value = <StepDimTol_AreaUnitType.StepDimTol_Circular: 0>
    StepDimTol_Rectangular: OCP.StepDimTol.StepDimTol_AreaUnitType # value = <StepDimTol_AreaUnitType.StepDimTol_Rectangular: 1>
    StepDimTol_Square: OCP.StepDimTol.StepDimTol_AreaUnitType # value = <StepDimTol_AreaUnitType.StepDimTol_Square: 2>
    __entries: dict # value = {'StepDimTol_Circular': (<StepDimTol_AreaUnitType.StepDimTol_Circular: 0>, None), 'StepDimTol_Rectangular': (<StepDimTol_AreaUnitType.StepDimTol_Rectangular: 1>, None), 'StepDimTol_Square': (<StepDimTol_AreaUnitType.StepDimTol_Square: 2>, None)}
    __members__: dict # value = {'StepDimTol_Circular': <StepDimTol_AreaUnitType.StepDimTol_Circular: 0>, 'StepDimTol_Rectangular': <StepDimTol_AreaUnitType.StepDimTol_Rectangular: 1>, 'StepDimTol_Square': <StepDimTol_AreaUnitType.StepDimTol_Square: 2>}
    pass
class StepDimTol_Array1OfDatumReference():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepDimTol_Array1OfDatumReference) -> StepDimTol_Array1OfDatumReference: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepDimTol_DatumReference: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumReference: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumReference: 
        """
        Variable value access
        """
    def First(self) -> StepDimTol_DatumReference: 
        """
        Returns first element
        """
    def Init(self,theValue : StepDimTol_DatumReference) -> None: 
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
    def Last(self) -> StepDimTol_DatumReference: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumReference) -> StepDimTol_Array1OfDatumReference: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumReference) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumReference: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepDimTol_DatumReference,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumReference) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepDimTol_Array1OfDatumReferenceCompartment():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepDimTol_Array1OfDatumReferenceCompartment) -> StepDimTol_Array1OfDatumReferenceCompartment: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepDimTol_DatumReferenceCompartment: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumReferenceCompartment: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumReferenceCompartment: 
        """
        Variable value access
        """
    def First(self) -> StepDimTol_DatumReferenceCompartment: 
        """
        Returns first element
        """
    def Init(self,theValue : StepDimTol_DatumReferenceCompartment) -> None: 
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
    def Last(self) -> StepDimTol_DatumReferenceCompartment: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumReferenceCompartment) -> StepDimTol_Array1OfDatumReferenceCompartment: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumReferenceCompartment) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumReferenceCompartment: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumReferenceCompartment) -> None: ...
    @overload
    def __init__(self,theBegin : StepDimTol_DatumReferenceCompartment,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepDimTol_Array1OfDatumReferenceElement():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepDimTol_Array1OfDatumReferenceElement) -> StepDimTol_Array1OfDatumReferenceElement: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepDimTol_DatumReferenceElement: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumReferenceElement: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumReferenceElement: 
        """
        Variable value access
        """
    def First(self) -> StepDimTol_DatumReferenceElement: 
        """
        Returns first element
        """
    def Init(self,theValue : StepDimTol_DatumReferenceElement) -> None: 
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
    def Last(self) -> StepDimTol_DatumReferenceElement: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumReferenceElement) -> StepDimTol_Array1OfDatumReferenceElement: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumReferenceElement) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumReferenceElement: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepDimTol_DatumReferenceElement,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumReferenceElement) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepDimTol_Array1OfDatumReferenceModifier():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepDimTol_Array1OfDatumReferenceModifier) -> StepDimTol_Array1OfDatumReferenceModifier: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepDimTol_DatumReferenceModifier: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumReferenceModifier: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumReferenceModifier: 
        """
        Variable value access
        """
    def First(self) -> StepDimTol_DatumReferenceModifier: 
        """
        Returns first element
        """
    def Init(self,theValue : StepDimTol_DatumReferenceModifier) -> None: 
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
    def Last(self) -> StepDimTol_DatumReferenceModifier: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumReferenceModifier) -> StepDimTol_Array1OfDatumReferenceModifier: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumReferenceModifier) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumReferenceModifier: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumReferenceModifier) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepDimTol_DatumReferenceModifier,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepDimTol_Array1OfDatumSystemOrReference():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepDimTol_Array1OfDatumSystemOrReference) -> StepDimTol_Array1OfDatumSystemOrReference: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepDimTol_DatumSystemOrReference: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumSystemOrReference: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumSystemOrReference: 
        """
        Variable value access
        """
    def First(self) -> StepDimTol_DatumSystemOrReference: 
        """
        Returns first element
        """
    def Init(self,theValue : StepDimTol_DatumSystemOrReference) -> None: 
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
    def Last(self) -> StepDimTol_DatumSystemOrReference: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumSystemOrReference) -> StepDimTol_Array1OfDatumSystemOrReference: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumSystemOrReference) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumSystemOrReference: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumSystemOrReference) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepDimTol_DatumSystemOrReference,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepDimTol_Array1OfGeometricToleranceModifier():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepDimTol_Array1OfGeometricToleranceModifier) -> StepDimTol_Array1OfGeometricToleranceModifier: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepDimTol_GeometricToleranceModifier: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_GeometricToleranceModifier: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_GeometricToleranceModifier: 
        """
        Variable value access
        """
    def First(self) -> StepDimTol_GeometricToleranceModifier: 
        """
        Returns first element
        """
    def Init(self,theValue : StepDimTol_GeometricToleranceModifier) -> None: 
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
    def Last(self) -> StepDimTol_GeometricToleranceModifier: 
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
    def Move(self,theOther : StepDimTol_Array1OfGeometricToleranceModifier) -> StepDimTol_Array1OfGeometricToleranceModifier: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_GeometricToleranceModifier) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_GeometricToleranceModifier: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepDimTol_GeometricToleranceModifier,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfGeometricToleranceModifier) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepDimTol_Array1OfToleranceZoneTarget():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepDimTol_Array1OfToleranceZoneTarget) -> StepDimTol_Array1OfToleranceZoneTarget: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepDimTol_ToleranceZoneTarget: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_ToleranceZoneTarget: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_ToleranceZoneTarget: 
        """
        Variable value access
        """
    def First(self) -> StepDimTol_ToleranceZoneTarget: 
        """
        Returns first element
        """
    def Init(self,theValue : StepDimTol_ToleranceZoneTarget) -> None: 
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
    def Last(self) -> StepDimTol_ToleranceZoneTarget: 
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
    def Move(self,theOther : StepDimTol_Array1OfToleranceZoneTarget) -> StepDimTol_Array1OfToleranceZoneTarget: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_ToleranceZoneTarget) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_ToleranceZoneTarget: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepDimTol_ToleranceZoneTarget,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfToleranceZoneTarget) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepDimTol_GeometricToleranceWithDatumReference(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeometricToleranceWithDatumReferenceRepresentation of STEP entity GeometricToleranceWithDatumReferenceRepresentation of STEP entity GeometricToleranceWithDatumReference
    """
    def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: 
        """
        Returns field DatumSystem AP214
        """
    def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: 
        """
        Returns field DatumSystem AP242
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Set field DatumSystem AP214

        Set field DatumSystem AP242
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_CoaxialityTolerance(StepDimTol_GeometricToleranceWithDatumReference, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CoaxialityToleranceRepresentation of STEP entity CoaxialityToleranceRepresentation of STEP entity CoaxialityTolerance
    """
    def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: 
        """
        Returns field DatumSystem AP214
        """
    def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: 
        """
        Returns field DatumSystem AP242
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Set field DatumSystem AP214

        Set field DatumSystem AP242
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_CommonDatum(OCP.StepRepr.StepRepr_CompositeShapeAspect, OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CommonDatumRepresentation of STEP entity CommonDatumRepresentation of STEP entity CommonDatum
    """
    def Datum(self) -> StepDimTol_Datum: 
        """
        Returns data for supertype Datum
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
    def Init(self,theShapeAspect_Name : OCP.TCollection.TCollection_HAsciiString,theShapeAspect_Description : OCP.TCollection.TCollection_HAsciiString,theShapeAspect_OfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theShapeAspect_ProductDefinitional : OCP.StepData.StepData_Logical,theDatum_Name : OCP.TCollection.TCollection_HAsciiString,theDatum_Description : OCP.TCollection.TCollection_HAsciiString,theDatum_OfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theDatum_ProductDefinitional : OCP.StepData.StepData_Logical,theDatum_Identification : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def OfShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDatum(self,theDatum : StepDimTol_Datum) -> None: 
        """
        Set data for supertype Datum
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
class StepDimTol_ConcentricityTolerance(StepDimTol_GeometricToleranceWithDatumReference, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ConcentricityToleranceRepresentation of STEP entity ConcentricityToleranceRepresentation of STEP entity ConcentricityTolerance
    """
    def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: 
        """
        Returns field DatumSystem AP214
        """
    def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: 
        """
        Returns field DatumSystem AP242
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Set field DatumSystem AP214

        Set field DatumSystem AP242
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_CylindricityTolerance(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CylindricityToleranceRepresentation of STEP entity CylindricityToleranceRepresentation of STEP entity CylindricityTolerance
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
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_Datum(OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DatumRepresentation of STEP entity DatumRepresentation of STEP entity Datum
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
    def Identification(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Identification
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theShapeAspect_Name : OCP.TCollection.TCollection_HAsciiString,theShapeAspect_Description : OCP.TCollection.TCollection_HAsciiString,theShapeAspect_OfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theShapeAspect_ProductDefinitional : OCP.StepData.StepData_Logical,theIdentification : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def SetIdentification(self,theIdentification : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Identification
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
class StepDimTol_DatumFeature(OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DatumFeatureRepresentation of STEP entity DatumFeatureRepresentation of STEP entity DatumFeature
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
class StepDimTol_DatumOrCommonDatum(OCP.StepData.StepData_SelectType):
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
        Recognizes a DatumOrCommonDatum Kind Entity that is : 1 -> Datum 2 -> CommonDatumList 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CommonDatumList(self) -> StepDimTol_HArray1OfDatumReferenceElement: 
        """
        returns Value as a CommonDatumList (Null if another type)
        """
    def Datum(self) -> StepDimTol_Datum: 
        """
        returns Value as a Datum (Null if another type)
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
class StepDimTol_DatumReference(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DatumReferenceRepresentation of STEP entity DatumReferenceRepresentation of STEP entity DatumReference
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
    def Init(self,thePrecedence : int,theReferencedDatum : StepDimTol_Datum) -> None: 
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
    def Precedence(self) -> int: 
        """
        Returns field Precedence
        """
    def ReferencedDatum(self) -> StepDimTol_Datum: 
        """
        Returns field ReferencedDatum
        """
    def SetPrecedence(self,thePrecedence : int) -> None: 
        """
        Set field Precedence
        """
    def SetReferencedDatum(self,theReferencedDatum : StepDimTol_Datum) -> None: 
        """
        Set field ReferencedDatum
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
class StepDimTol_GeneralDatumReference(OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeneralDatumReferenceRepresentation of STEP entity GeneralDatumReferenceRepresentation of STEP entity GeneralDatumReference
    """
    def Base(self) -> StepDimTol_DatumOrCommonDatum: 
        """
        Returns field Base
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
    def HasModifiers(self) -> bool: 
        """
        Indicates is field Modifiers exist
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theOfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theProductDefinitional : OCP.StepData.StepData_Logical,theBase : StepDimTol_DatumOrCommonDatum,theHasModifiers : bool,theModifiers : StepDimTol_HArray1OfDatumReferenceModifier) -> None: 
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
    def Modifiers(self) -> StepDimTol_HArray1OfDatumReferenceModifier: 
        """
        Returns field Modifiers
        """
    @overload
    def ModifiersValue(self,theNum : int) -> StepDimTol_DatumReferenceModifier: 
        """
        Returns Modifiers with the given number

        Sets Modifiers with given number
        """
    @overload
    def ModifiersValue(self,theNum : int,theItem : StepDimTol_DatumReferenceModifier) -> None: ...
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbModifiers(self) -> int: 
        """
        Returns number of Modifiers
        """
    def OfShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetBase(self,theBase : StepDimTol_DatumOrCommonDatum) -> None: 
        """
        Set field Base
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetModifiers(self,theModifiers : StepDimTol_HArray1OfDatumReferenceModifier) -> None: 
        """
        Set field Modifiers
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
class StepDimTol_DatumReferenceElement(StepDimTol_GeneralDatumReference, OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DatumReferenceElementRepresentation of STEP entity DatumReferenceElementRepresentation of STEP entity DatumReferenceElement
    """
    def Base(self) -> StepDimTol_DatumOrCommonDatum: 
        """
        Returns field Base
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
    def HasModifiers(self) -> bool: 
        """
        Indicates is field Modifiers exist
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theOfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theProductDefinitional : OCP.StepData.StepData_Logical,theBase : StepDimTol_DatumOrCommonDatum,theHasModifiers : bool,theModifiers : StepDimTol_HArray1OfDatumReferenceModifier) -> None: 
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
    def Modifiers(self) -> StepDimTol_HArray1OfDatumReferenceModifier: 
        """
        Returns field Modifiers
        """
    @overload
    def ModifiersValue(self,theNum : int) -> StepDimTol_DatumReferenceModifier: 
        """
        Returns Modifiers with the given number

        Sets Modifiers with given number
        """
    @overload
    def ModifiersValue(self,theNum : int,theItem : StepDimTol_DatumReferenceModifier) -> None: ...
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbModifiers(self) -> int: 
        """
        Returns number of Modifiers
        """
    def OfShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetBase(self,theBase : StepDimTol_DatumOrCommonDatum) -> None: 
        """
        Set field Base
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetModifiers(self,theModifiers : StepDimTol_HArray1OfDatumReferenceModifier) -> None: 
        """
        Set field Modifiers
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
class StepDimTol_DatumReferenceModifier(OCP.StepData.StepData_SelectType):
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
        Recognizes a DatumReferenceModifier Kind Entity that is : 1 -> DatumReferenceModifierWithValue 2 -> SimpleDatumReferenceModifierMember 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def DatumReferenceModifierWithValue(self) -> StepDimTol_DatumReferenceModifierWithValue: 
        """
        returns Value as a DatumReferenceModifierWithValue (Null if another type)
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
    def SimpleDatumReferenceModifierMember(self) -> StepDimTol_SimpleDatumReferenceModifierMember: 
        """
        returns Value as a SimpleDatumReferenceModifierMember (Null if another type)
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
class StepDimTol_DatumReferenceModifierType():
    """
    None

    Members:

      StepDimTol_CircularOrCylindrical

      StepDimTol_Distance

      StepDimTol_Projected

      StepDimTol_Spherical
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
    StepDimTol_CircularOrCylindrical: OCP.StepDimTol.StepDimTol_DatumReferenceModifierType # value = <StepDimTol_DatumReferenceModifierType.StepDimTol_CircularOrCylindrical: 0>
    StepDimTol_Distance: OCP.StepDimTol.StepDimTol_DatumReferenceModifierType # value = <StepDimTol_DatumReferenceModifierType.StepDimTol_Distance: 1>
    StepDimTol_Projected: OCP.StepDimTol.StepDimTol_DatumReferenceModifierType # value = <StepDimTol_DatumReferenceModifierType.StepDimTol_Projected: 2>
    StepDimTol_Spherical: OCP.StepDimTol.StepDimTol_DatumReferenceModifierType # value = <StepDimTol_DatumReferenceModifierType.StepDimTol_Spherical: 3>
    __entries: dict # value = {'StepDimTol_CircularOrCylindrical': (<StepDimTol_DatumReferenceModifierType.StepDimTol_CircularOrCylindrical: 0>, None), 'StepDimTol_Distance': (<StepDimTol_DatumReferenceModifierType.StepDimTol_Distance: 1>, None), 'StepDimTol_Projected': (<StepDimTol_DatumReferenceModifierType.StepDimTol_Projected: 2>, None), 'StepDimTol_Spherical': (<StepDimTol_DatumReferenceModifierType.StepDimTol_Spherical: 3>, None)}
    __members__: dict # value = {'StepDimTol_CircularOrCylindrical': <StepDimTol_DatumReferenceModifierType.StepDimTol_CircularOrCylindrical: 0>, 'StepDimTol_Distance': <StepDimTol_DatumReferenceModifierType.StepDimTol_Distance: 1>, 'StepDimTol_Projected': <StepDimTol_DatumReferenceModifierType.StepDimTol_Projected: 2>, 'StepDimTol_Spherical': <StepDimTol_DatumReferenceModifierType.StepDimTol_Spherical: 3>}
    pass
class StepDimTol_DatumReferenceModifierWithValue(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DatumReferenceModifierWithValueRepresentation of STEP entity DatumReferenceModifierWithValueRepresentation of STEP entity DatumReferenceModifierWithValue
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
    def Init(self,theModifierType : StepDimTol_DatumReferenceModifierType,theModifierValue : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
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
    def ModifierType(self) -> StepDimTol_DatumReferenceModifierType: 
        """
        Returns field ModifierType
        """
    def ModifierValue(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        Returns field ModifierValue
        """
    def SetModifierType(self,theModifierType : StepDimTol_DatumReferenceModifierType) -> None: 
        """
        Set field ModifierType
        """
    def SetModifierValue(self,theModifierValue : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        Set field ModifierValue
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
class StepDimTol_DatumSystem(OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DatumSystemRepresentation of STEP entity DatumSystemRepresentation of STEP entity DatumSystem
    """
    def Constituents(self) -> StepDimTol_HArray1OfDatumReferenceCompartment: 
        """
        Returns field Constituents
        """
    @overload
    def ConstituentsValue(self,num : int) -> StepDimTol_DatumReferenceCompartment: 
        """
        Returns Constituents with the given number

        Sets Constituents with given number
        """
    @overload
    def ConstituentsValue(self,num : int,theItem : StepDimTol_DatumReferenceCompartment) -> None: ...
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theOfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theProductDefinitional : OCP.StepData.StepData_Logical,theConstituents : StepDimTol_HArray1OfDatumReferenceCompartment) -> None: 
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
    def NbConstituents(self) -> int: 
        """
        Returns number of Constituents
        """
    def OfShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetConstituents(self,theConstituents : StepDimTol_HArray1OfDatumReferenceCompartment) -> None: 
        """
        Set field Constituents
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
class StepDimTol_DatumSystemOrReference(OCP.StepData.StepData_SelectType):
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
        Recognizes a DatumSystemOrReference Kind Entity that is : 1 -> DatumSystem 2 -> DatumReference 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def DatumReference(self) -> StepDimTol_DatumReference: 
        """
        returns Value as a DatumReference (Null if another type)
        """
    def DatumSystem(self) -> StepDimTol_DatumSystem: 
        """
        returns Value as a DatumSystem (Null if another type)
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
class StepDimTol_DatumTarget(OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DatumTargetRepresentation of STEP entity DatumTargetRepresentation of STEP entity DatumTarget
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
    def Init(self,theShapeAspect_Name : OCP.TCollection.TCollection_HAsciiString,theShapeAspect_Description : OCP.TCollection.TCollection_HAsciiString,theShapeAspect_OfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theShapeAspect_ProductDefinitional : OCP.StepData.StepData_Logical,theTargetId : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def SetTargetId(self,theTargetId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field TargetId
        """
    def TargetId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field TargetId
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
class StepDimTol_FlatnessTolerance(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FlatnessToleranceRepresentation of STEP entity FlatnessToleranceRepresentation of STEP entity FlatnessTolerance
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
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_DatumReferenceCompartment(StepDimTol_GeneralDatumReference, OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DatumReferenceCompartmentRepresentation of STEP entity DatumReferenceCompartmentRepresentation of STEP entity DatumReferenceCompartment
    """
    def Base(self) -> StepDimTol_DatumOrCommonDatum: 
        """
        Returns field Base
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
    def HasModifiers(self) -> bool: 
        """
        Indicates is field Modifiers exist
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theOfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theProductDefinitional : OCP.StepData.StepData_Logical,theBase : StepDimTol_DatumOrCommonDatum,theHasModifiers : bool,theModifiers : StepDimTol_HArray1OfDatumReferenceModifier) -> None: 
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
    def Modifiers(self) -> StepDimTol_HArray1OfDatumReferenceModifier: 
        """
        Returns field Modifiers
        """
    @overload
    def ModifiersValue(self,theNum : int) -> StepDimTol_DatumReferenceModifier: 
        """
        Returns Modifiers with the given number

        Sets Modifiers with given number
        """
    @overload
    def ModifiersValue(self,theNum : int,theItem : StepDimTol_DatumReferenceModifier) -> None: ...
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbModifiers(self) -> int: 
        """
        Returns number of Modifiers
        """
    def OfShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetBase(self,theBase : StepDimTol_DatumOrCommonDatum) -> None: 
        """
        Set field Base
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetModifiers(self,theModifiers : StepDimTol_HArray1OfDatumReferenceModifier) -> None: 
        """
        Set field Modifiers
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
class StepDimTol_GeoTolAndGeoTolWthDatRef(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
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
    def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theGTWDR : StepDimTol_GeometricToleranceWithDatumReference,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,aTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,aGTWDR : StepDimTol_GeometricToleranceWithDatumReference,theType : StepDimTol_GeometricToleranceType) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetGeometricToleranceType(self,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None
        """
    def SetGeometricToleranceWithDatumReference(self,theGTWDR : StepDimTol_GeometricToleranceWithDatumReference) -> None: 
        """
        None
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
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
    def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: 
        """
        None
        """
    def GetGeometricToleranceWithModifiers(self) -> StepDimTol_GeometricToleranceWithModifiers: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,aTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,aGTWDR : StepDimTol_GeometricToleranceWithDatumReference,aGTWM : StepDimTol_GeometricToleranceWithModifiers,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theGTWDR : StepDimTol_GeometricToleranceWithDatumReference,theGTWM : StepDimTol_GeometricToleranceWithModifiers,theType : StepDimTol_GeometricToleranceType) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetGeometricToleranceType(self,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None
        """
    def SetGeometricToleranceWithDatumReference(self,theGTWDR : StepDimTol_GeometricToleranceWithDatumReference) -> None: 
        """
        None
        """
    def SetGeometricToleranceWithModifiers(self,theGTWM : StepDimTol_GeometricToleranceWithModifiers) -> None: 
        """
        None
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol(StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
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
    def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: 
        """
        None
        """
    def GetGeometricToleranceWithModifiers(self) -> StepDimTol_GeometricToleranceWithModifiers: 
        """
        None
        """
    def GetMaxTolerance(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theGTWDR : StepDimTol_GeometricToleranceWithDatumReference,theGTWM : StepDimTol_GeometricToleranceWithModifiers,theMaxTol : OCP.StepBasic.StepBasic_LengthMeasureWithUnit,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,aTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,aGTWDR : StepDimTol_GeometricToleranceWithDatumReference,aGTWM : StepDimTol_GeometricToleranceWithModifiers,theMaxTol : OCP.StepBasic.StepBasic_LengthMeasureWithUnit,theType : StepDimTol_GeometricToleranceType) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetGeometricToleranceType(self,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None
        """
    def SetGeometricToleranceWithDatumReference(self,theGTWDR : StepDimTol_GeometricToleranceWithDatumReference) -> None: 
        """
        None
        """
    def SetGeometricToleranceWithModifiers(self,theGTWM : StepDimTol_GeometricToleranceWithModifiers) -> None: 
        """
        None
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetMaxTolerance(self,theMaxTol : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> Any: 
        """
        None
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
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
    def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: 
        """
        None
        """
    def GetModifiedGeometricTolerance(self) -> StepDimTol_ModifiedGeometricTolerance: 
        """
        None
        """
    def GetPositionTolerance(self) -> StepDimTol_PositionTolerance: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,aTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,aGTWDR : StepDimTol_GeometricToleranceWithDatumReference,aMGT : StepDimTol_ModifiedGeometricTolerance) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,aTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,aGTWDR : StepDimTol_GeometricToleranceWithDatumReference,aMGT : StepDimTol_ModifiedGeometricTolerance) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetGeometricToleranceWithDatumReference(self,aGTWDR : StepDimTol_GeometricToleranceWithDatumReference) -> None: 
        """
        None
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetModifiedGeometricTolerance(self,aMGT : StepDimTol_ModifiedGeometricTolerance) -> None: 
        """
        None
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetPositionTolerance(self,aPT : StepDimTol_PositionTolerance) -> None: 
        """
        None
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol(StepDimTol_GeoTolAndGeoTolWthDatRef, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
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
    def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: 
        """
        None
        """
    def GetUnequallyDisposedGeometricTolerance(self) -> StepDimTol_UnequallyDisposedGeometricTolerance: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theGTWDR : StepDimTol_GeometricToleranceWithDatumReference,theType : StepDimTol_GeometricToleranceType,theUDGT : StepDimTol_UnequallyDisposedGeometricTolerance) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,aTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,aGTWDR : StepDimTol_GeometricToleranceWithDatumReference,theType : StepDimTol_GeometricToleranceType,theUDGT : StepDimTol_UnequallyDisposedGeometricTolerance) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetGeometricToleranceType(self,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None
        """
    def SetGeometricToleranceWithDatumReference(self,theGTWDR : StepDimTol_GeometricToleranceWithDatumReference) -> None: 
        """
        None
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def SetUnequallyDisposedGeometricTolerance(self,theUDGT : StepDimTol_UnequallyDisposedGeometricTolerance) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeoTolAndGeoTolWthMod(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
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
    def GetGeometricToleranceWithModifiers(self) -> StepDimTol_GeometricToleranceWithModifiers: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,aTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,aGTWM : StepDimTol_GeometricToleranceWithModifiers,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theGTWM : StepDimTol_GeometricToleranceWithModifiers,theType : StepDimTol_GeometricToleranceType) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetGeometricToleranceType(self,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None
        """
    def SetGeometricToleranceWithModifiers(self,theGTWM : StepDimTol_GeometricToleranceWithModifiers) -> None: 
        """
        None
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeoTolAndGeoTolWthMaxTol(StepDimTol_GeoTolAndGeoTolWthMod, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
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
    def GetGeometricToleranceWithModifiers(self) -> StepDimTol_GeometricToleranceWithModifiers: 
        """
        None
        """
    def GetMaxTolerance(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,aTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,aGTWM : StepDimTol_GeometricToleranceWithModifiers,theMaxTol : OCP.StepBasic.StepBasic_LengthMeasureWithUnit,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theGTWM : StepDimTol_GeometricToleranceWithModifiers,theMaxTol : OCP.StepBasic.StepBasic_LengthMeasureWithUnit,theType : StepDimTol_GeometricToleranceType) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetGeometricToleranceType(self,theType : StepDimTol_GeometricToleranceType) -> None: 
        """
        None
        """
    def SetGeometricToleranceWithModifiers(self,theGTWM : StepDimTol_GeometricToleranceWithModifiers) -> None: 
        """
        None
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetMaxTolerance(self,theMaxTol : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> Any: 
        """
        None
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_AngularityTolerance(StepDimTol_GeometricToleranceWithDatumReference, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity AngularityToleranceRepresentation of STEP entity AngularityToleranceRepresentation of STEP entity AngularityTolerance
    """
    def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: 
        """
        Returns field DatumSystem AP214
        """
    def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: 
        """
        Returns field DatumSystem AP242
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Set field DatumSystem AP214

        Set field DatumSystem AP242
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeometricToleranceModifier():
    """
    None

    Members:

      StepDimTol_GTMAnyCrossSection

      StepDimTol_GTMCommonZone

      StepDimTol_GTMEachRadialElement

      StepDimTol_GTMFreeState

      StepDimTol_GTMLeastMaterialRequirement

      StepDimTol_GTMLineElement

      StepDimTol_GTMMajorDiameter

      StepDimTol_GTMMaximumMaterialRequirement

      StepDimTol_GTMMinorDiameter

      StepDimTol_GTMNotConvex

      StepDimTol_GTMPitchDiameter

      StepDimTol_GTMReciprocityRequirement

      StepDimTol_GTMSeparateRequirement

      StepDimTol_GTMStatisticalTolerance

      StepDimTol_GTMTangentPlane
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
    StepDimTol_GTMAnyCrossSection: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMAnyCrossSection: 0>
    StepDimTol_GTMCommonZone: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMCommonZone: 1>
    StepDimTol_GTMEachRadialElement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMEachRadialElement: 2>
    StepDimTol_GTMFreeState: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMFreeState: 3>
    StepDimTol_GTMLeastMaterialRequirement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLeastMaterialRequirement: 4>
    StepDimTol_GTMLineElement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLineElement: 5>
    StepDimTol_GTMMajorDiameter: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMajorDiameter: 6>
    StepDimTol_GTMMaximumMaterialRequirement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMaximumMaterialRequirement: 7>
    StepDimTol_GTMMinorDiameter: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMinorDiameter: 8>
    StepDimTol_GTMNotConvex: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMNotConvex: 9>
    StepDimTol_GTMPitchDiameter: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMPitchDiameter: 10>
    StepDimTol_GTMReciprocityRequirement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMReciprocityRequirement: 11>
    StepDimTol_GTMSeparateRequirement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMSeparateRequirement: 12>
    StepDimTol_GTMStatisticalTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMStatisticalTolerance: 13>
    StepDimTol_GTMTangentPlane: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMTangentPlane: 14>
    __entries: dict # value = {'StepDimTol_GTMAnyCrossSection': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMAnyCrossSection: 0>, None), 'StepDimTol_GTMCommonZone': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMCommonZone: 1>, None), 'StepDimTol_GTMEachRadialElement': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMEachRadialElement: 2>, None), 'StepDimTol_GTMFreeState': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMFreeState: 3>, None), 'StepDimTol_GTMLeastMaterialRequirement': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLeastMaterialRequirement: 4>, None), 'StepDimTol_GTMLineElement': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLineElement: 5>, None), 'StepDimTol_GTMMajorDiameter': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMajorDiameter: 6>, None), 'StepDimTol_GTMMaximumMaterialRequirement': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMaximumMaterialRequirement: 7>, None), 'StepDimTol_GTMMinorDiameter': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMinorDiameter: 8>, None), 'StepDimTol_GTMNotConvex': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMNotConvex: 9>, None), 'StepDimTol_GTMPitchDiameter': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMPitchDiameter: 10>, None), 'StepDimTol_GTMReciprocityRequirement': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMReciprocityRequirement: 11>, None), 'StepDimTol_GTMSeparateRequirement': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMSeparateRequirement: 12>, None), 'StepDimTol_GTMStatisticalTolerance': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMStatisticalTolerance: 13>, None), 'StepDimTol_GTMTangentPlane': (<StepDimTol_GeometricToleranceModifier.StepDimTol_GTMTangentPlane: 14>, None)}
    __members__: dict # value = {'StepDimTol_GTMAnyCrossSection': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMAnyCrossSection: 0>, 'StepDimTol_GTMCommonZone': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMCommonZone: 1>, 'StepDimTol_GTMEachRadialElement': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMEachRadialElement: 2>, 'StepDimTol_GTMFreeState': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMFreeState: 3>, 'StepDimTol_GTMLeastMaterialRequirement': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLeastMaterialRequirement: 4>, 'StepDimTol_GTMLineElement': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLineElement: 5>, 'StepDimTol_GTMMajorDiameter': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMajorDiameter: 6>, 'StepDimTol_GTMMaximumMaterialRequirement': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMaximumMaterialRequirement: 7>, 'StepDimTol_GTMMinorDiameter': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMinorDiameter: 8>, 'StepDimTol_GTMNotConvex': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMNotConvex: 9>, 'StepDimTol_GTMPitchDiameter': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMPitchDiameter: 10>, 'StepDimTol_GTMReciprocityRequirement': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMReciprocityRequirement: 11>, 'StepDimTol_GTMSeparateRequirement': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMSeparateRequirement: 12>, 'StepDimTol_GTMStatisticalTolerance': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMStatisticalTolerance: 13>, 'StepDimTol_GTMTangentPlane': <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMTangentPlane: 14>}
    pass
class StepDimTol_GeometricToleranceRelationship(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeometricToleranceRelationshipRepresentation of STEP entity GeometricToleranceRelationshipRepresentation of STEP entity GeometricToleranceRelationship
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theRelatingGeometricTolerance : StepDimTol_GeometricTolerance,theRelatedGeometricTolerance : StepDimTol_GeometricTolerance) -> None: 
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
    def RelatedGeometricTolerance(self) -> StepDimTol_GeometricTolerance: 
        """
        Returns field RelatedGeometricTolerance
        """
    def RelatingGeometricTolerance(self) -> StepDimTol_GeometricTolerance: 
        """
        Returns field RelatingGeometricTolerance
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedGeometricTolerance(self,theRelatedGeometricTolerance : StepDimTol_GeometricTolerance) -> None: 
        """
        Set field RelatedGeometricTolerance
        """
    def SetRelatingGeometricTolerance(self,theRelatingGeometricTolerance : StepDimTol_GeometricTolerance) -> None: 
        """
        Set field RelatingGeometricTolerance
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
class StepDimTol_GeometricToleranceTarget(OCP.StepData.StepData_SelectType):
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
        Recognizes a GeometricToleranceTarget Kind Entity that is : 1 -> DimensionalLocation 2 -> DimensionalSize 3 -> ProductDefinitionShape 4 -> ShapeAspect 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DimensionalLocation(self) -> OCP.StepShape.StepShape_DimensionalLocation: 
        """
        returns Value as a DimensionalLocation (Null if another type)
        """
    def DimensionalSize(self) -> OCP.StepShape.StepShape_DimensionalSize: 
        """
        returns Value as a DimensionalSize (Null if another type)
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
    def ProductDefinitionShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
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
    def ShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        returns Value as a ShapeAspect (Null if another type)
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
class StepDimTol_GeometricToleranceType():
    """
    None

    Members:

      StepDimTol_GTTAngularityTolerance

      StepDimTol_GTTCircularRunoutTolerance

      StepDimTol_GTTCoaxialityTolerance

      StepDimTol_GTTConcentricityTolerance

      StepDimTol_GTTCylindricityTolerance

      StepDimTol_GTTFlatnessTolerance

      StepDimTol_GTTLineProfileTolerance

      StepDimTol_GTTParallelismTolerance

      StepDimTol_GTTPerpendicularityTolerance

      StepDimTol_GTTPositionTolerance

      StepDimTol_GTTRoundnessTolerance

      StepDimTol_GTTStraightnessTolerance

      StepDimTol_GTTSurfaceProfileTolerance

      StepDimTol_GTTSymmetryTolerance

      StepDimTol_GTTTotalRunoutTolerance
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
    StepDimTol_GTTAngularityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTAngularityTolerance: 0>
    StepDimTol_GTTCircularRunoutTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTCircularRunoutTolerance: 1>
    StepDimTol_GTTCoaxialityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTCoaxialityTolerance: 2>
    StepDimTol_GTTConcentricityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTConcentricityTolerance: 3>
    StepDimTol_GTTCylindricityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTCylindricityTolerance: 4>
    StepDimTol_GTTFlatnessTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTFlatnessTolerance: 5>
    StepDimTol_GTTLineProfileTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTLineProfileTolerance: 6>
    StepDimTol_GTTParallelismTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTParallelismTolerance: 7>
    StepDimTol_GTTPerpendicularityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTPerpendicularityTolerance: 8>
    StepDimTol_GTTPositionTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTPositionTolerance: 9>
    StepDimTol_GTTRoundnessTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTRoundnessTolerance: 10>
    StepDimTol_GTTStraightnessTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTStraightnessTolerance: 11>
    StepDimTol_GTTSurfaceProfileTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTSurfaceProfileTolerance: 12>
    StepDimTol_GTTSymmetryTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTSymmetryTolerance: 13>
    StepDimTol_GTTTotalRunoutTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTTotalRunoutTolerance: 14>
    __entries: dict # value = {'StepDimTol_GTTAngularityTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTAngularityTolerance: 0>, None), 'StepDimTol_GTTCircularRunoutTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTCircularRunoutTolerance: 1>, None), 'StepDimTol_GTTCoaxialityTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTCoaxialityTolerance: 2>, None), 'StepDimTol_GTTConcentricityTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTConcentricityTolerance: 3>, None), 'StepDimTol_GTTCylindricityTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTCylindricityTolerance: 4>, None), 'StepDimTol_GTTFlatnessTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTFlatnessTolerance: 5>, None), 'StepDimTol_GTTLineProfileTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTLineProfileTolerance: 6>, None), 'StepDimTol_GTTParallelismTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTParallelismTolerance: 7>, None), 'StepDimTol_GTTPerpendicularityTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTPerpendicularityTolerance: 8>, None), 'StepDimTol_GTTPositionTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTPositionTolerance: 9>, None), 'StepDimTol_GTTRoundnessTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTRoundnessTolerance: 10>, None), 'StepDimTol_GTTStraightnessTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTStraightnessTolerance: 11>, None), 'StepDimTol_GTTSurfaceProfileTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTSurfaceProfileTolerance: 12>, None), 'StepDimTol_GTTSymmetryTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTSymmetryTolerance: 13>, None), 'StepDimTol_GTTTotalRunoutTolerance': (<StepDimTol_GeometricToleranceType.StepDimTol_GTTTotalRunoutTolerance: 14>, None)}
    __members__: dict # value = {'StepDimTol_GTTAngularityTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTAngularityTolerance: 0>, 'StepDimTol_GTTCircularRunoutTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTCircularRunoutTolerance: 1>, 'StepDimTol_GTTCoaxialityTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTCoaxialityTolerance: 2>, 'StepDimTol_GTTConcentricityTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTConcentricityTolerance: 3>, 'StepDimTol_GTTCylindricityTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTCylindricityTolerance: 4>, 'StepDimTol_GTTFlatnessTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTFlatnessTolerance: 5>, 'StepDimTol_GTTLineProfileTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTLineProfileTolerance: 6>, 'StepDimTol_GTTParallelismTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTParallelismTolerance: 7>, 'StepDimTol_GTTPerpendicularityTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTPerpendicularityTolerance: 8>, 'StepDimTol_GTTPositionTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTPositionTolerance: 9>, 'StepDimTol_GTTRoundnessTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTRoundnessTolerance: 10>, 'StepDimTol_GTTStraightnessTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTStraightnessTolerance: 11>, 'StepDimTol_GTTSurfaceProfileTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTSurfaceProfileTolerance: 12>, 'StepDimTol_GTTSymmetryTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTSymmetryTolerance: 13>, 'StepDimTol_GTTTotalRunoutTolerance': <StepDimTol_GeometricToleranceType.StepDimTol_GTTTotalRunoutTolerance: 14>}
    pass
class StepDimTol_CircularRunoutTolerance(StepDimTol_GeometricToleranceWithDatumReference, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CircularRunoutToleranceRepresentation of STEP entity CircularRunoutToleranceRepresentation of STEP entity CircularRunoutTolerance
    """
    def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: 
        """
        Returns field DatumSystem AP214
        """
    def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: 
        """
        Returns field DatumSystem AP242
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Set field DatumSystem AP214

        Set field DatumSystem AP242
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeometricToleranceWithDefinedUnit(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeometricToleranceWithDefinedUnitRepresentation of STEP entity GeometricToleranceWithDefinedUnitRepresentation of STEP entity GeometricToleranceWithDefinedUnit
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
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theUnitSize : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theUnitSize : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def SetUnitSize(self,theUnitSize : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        Set field UnitSize
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def UnitSize(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        Returns field UnitSize
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeometricToleranceWithDefinedAreaUnit(StepDimTol_GeometricToleranceWithDefinedUnit, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeometricToleranceWithDefinedAreaUnitRepresentation of STEP entity GeometricToleranceWithDefinedAreaUnitRepresentation of STEP entity GeometricToleranceWithDefinedAreaUnit
    """
    def AreaType(self) -> StepDimTol_AreaUnitType: 
        """
        Returns field AreaType
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
    def HasSecondUnitSize(self) -> bool: 
        """
        Indicates if SecondUnitSize field exist
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theUnitSize : OCP.StepBasic.StepBasic_LengthMeasureWithUnit,theAreaType : StepDimTol_AreaUnitType,theHasSecondUnitSize : bool,theSecondUnitSize : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SecondUnitSize(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        Returns field SecondUnitSize
        """
    def SetAreaType(self,theAreaType : StepDimTol_AreaUnitType) -> None: 
        """
        Set field AreaType
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetSecondUnitSize(self,theSecondUnitSize : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        Set field SecondUnitSize
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def SetUnitSize(self,theUnitSize : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        Set field UnitSize
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def UnitSize(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        Returns field UnitSize
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeometricToleranceWithModifiers(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeometricToleranceWithModifiersRepresentation of STEP entity GeometricToleranceWithModifiersRepresentation of STEP entity GeometricToleranceWithModifiers
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theModifiers : StepDimTol_HArray1OfGeometricToleranceModifier) -> None: 
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def ModifierValue(self,theNum : int) -> StepDimTol_GeometricToleranceModifier: 
        """
        Returns modifier with the given number
        """
    def Modifiers(self) -> StepDimTol_HArray1OfGeometricToleranceModifier: 
        """
        Returns field Modifiers
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def NbModifiers(self) -> int: 
        """
        Returns number of modifiers
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetModifierValue(self,theNum : int,theItem : StepDimTol_GeometricToleranceModifier) -> None: 
        """
        Sets modifier with given number
        """
    def SetModifiers(self,theModifiers : StepDimTol_HArray1OfGeometricToleranceModifier) -> None: 
        """
        Set field Modifiers
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_GeometricToleranceWithMaximumTolerance(StepDimTol_GeometricToleranceWithModifiers, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity GeometricToleranceWithMaximumToleranceRepresentation of STEP entity GeometricToleranceWithMaximumToleranceRepresentation of STEP entity GeometricToleranceWithMaximumTolerance
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theModifiers : StepDimTol_HArray1OfGeometricToleranceModifier,theUnitSize : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def MaximumUpperTolerance(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        Returns field MaximumUpperTolerance
        """
    def ModifierValue(self,theNum : int) -> StepDimTol_GeometricToleranceModifier: 
        """
        Returns modifier with the given number
        """
    def Modifiers(self) -> StepDimTol_HArray1OfGeometricToleranceModifier: 
        """
        Returns field Modifiers
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def NbModifiers(self) -> int: 
        """
        Returns number of modifiers
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetMaximumUpperTolerance(self,theMaximumUpperTolerance : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        Set field MaximumUpperTolerance
        """
    def SetModifierValue(self,theNum : int,theItem : StepDimTol_GeometricToleranceModifier) -> None: 
        """
        Sets modifier with given number
        """
    def SetModifiers(self,theModifiers : StepDimTol_HArray1OfGeometricToleranceModifier) -> None: 
        """
        Set field Modifiers
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_HArray1OfDatumReference(StepDimTol_Array1OfDatumReference, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepDimTol_Array1OfDatumReference: 
        """
        None
        """
    def Assign(self,theOther : StepDimTol_Array1OfDatumReference) -> StepDimTol_Array1OfDatumReference: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepDimTol_Array1OfDatumReference: 
        """
        None
        """
    def ChangeFirst(self) -> StepDimTol_DatumReference: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumReference: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumReference: 
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
    def First(self) -> StepDimTol_DatumReference: 
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
    def Init(self,theValue : StepDimTol_DatumReference) -> None: 
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
    def Last(self) -> StepDimTol_DatumReference: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumReference) -> StepDimTol_Array1OfDatumReference: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumReference) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumReference: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumReference) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepDimTol_DatumReference) -> None: ...
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
class StepDimTol_HArray1OfDatumReferenceCompartment(StepDimTol_Array1OfDatumReferenceCompartment, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepDimTol_Array1OfDatumReferenceCompartment: 
        """
        None
        """
    def Assign(self,theOther : StepDimTol_Array1OfDatumReferenceCompartment) -> StepDimTol_Array1OfDatumReferenceCompartment: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepDimTol_Array1OfDatumReferenceCompartment: 
        """
        None
        """
    def ChangeFirst(self) -> StepDimTol_DatumReferenceCompartment: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumReferenceCompartment: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumReferenceCompartment: 
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
    def First(self) -> StepDimTol_DatumReferenceCompartment: 
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
    def Init(self,theValue : StepDimTol_DatumReferenceCompartment) -> None: 
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
    def Last(self) -> StepDimTol_DatumReferenceCompartment: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumReferenceCompartment) -> StepDimTol_Array1OfDatumReferenceCompartment: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumReferenceCompartment) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumReferenceCompartment: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepDimTol_DatumReferenceCompartment) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumReferenceCompartment) -> None: ...
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
class StepDimTol_HArray1OfDatumReferenceElement(StepDimTol_Array1OfDatumReferenceElement, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepDimTol_Array1OfDatumReferenceElement: 
        """
        None
        """
    def Assign(self,theOther : StepDimTol_Array1OfDatumReferenceElement) -> StepDimTol_Array1OfDatumReferenceElement: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepDimTol_Array1OfDatumReferenceElement: 
        """
        None
        """
    def ChangeFirst(self) -> StepDimTol_DatumReferenceElement: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumReferenceElement: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumReferenceElement: 
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
    def First(self) -> StepDimTol_DatumReferenceElement: 
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
    def Init(self,theValue : StepDimTol_DatumReferenceElement) -> None: 
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
    def Last(self) -> StepDimTol_DatumReferenceElement: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumReferenceElement) -> StepDimTol_Array1OfDatumReferenceElement: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumReferenceElement) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumReferenceElement: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumReferenceElement) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepDimTol_DatumReferenceElement) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
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
class StepDimTol_HArray1OfDatumReferenceModifier(StepDimTol_Array1OfDatumReferenceModifier, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepDimTol_Array1OfDatumReferenceModifier: 
        """
        None
        """
    def Assign(self,theOther : StepDimTol_Array1OfDatumReferenceModifier) -> StepDimTol_Array1OfDatumReferenceModifier: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepDimTol_Array1OfDatumReferenceModifier: 
        """
        None
        """
    def ChangeFirst(self) -> StepDimTol_DatumReferenceModifier: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumReferenceModifier: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumReferenceModifier: 
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
    def First(self) -> StepDimTol_DatumReferenceModifier: 
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
    def Init(self,theValue : StepDimTol_DatumReferenceModifier) -> None: 
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
    def Last(self) -> StepDimTol_DatumReferenceModifier: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumReferenceModifier) -> StepDimTol_Array1OfDatumReferenceModifier: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumReferenceModifier) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumReferenceModifier: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepDimTol_DatumReferenceModifier) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumReferenceModifier) -> None: ...
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
class StepDimTol_HArray1OfDatumSystemOrReference(StepDimTol_Array1OfDatumSystemOrReference, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepDimTol_Array1OfDatumSystemOrReference: 
        """
        None
        """
    def Assign(self,theOther : StepDimTol_Array1OfDatumSystemOrReference) -> StepDimTol_Array1OfDatumSystemOrReference: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepDimTol_Array1OfDatumSystemOrReference: 
        """
        None
        """
    def ChangeFirst(self) -> StepDimTol_DatumSystemOrReference: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_DatumSystemOrReference: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_DatumSystemOrReference: 
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
    def First(self) -> StepDimTol_DatumSystemOrReference: 
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
    def Init(self,theValue : StepDimTol_DatumSystemOrReference) -> None: 
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
    def Last(self) -> StepDimTol_DatumSystemOrReference: 
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
    def Move(self,theOther : StepDimTol_Array1OfDatumSystemOrReference) -> StepDimTol_Array1OfDatumSystemOrReference: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_DatumSystemOrReference) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_DatumSystemOrReference: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepDimTol_DatumSystemOrReference) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfDatumSystemOrReference) -> None: ...
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
class StepDimTol_HArray1OfGeometricToleranceModifier(StepDimTol_Array1OfGeometricToleranceModifier, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepDimTol_Array1OfGeometricToleranceModifier: 
        """
        None
        """
    def Assign(self,theOther : StepDimTol_Array1OfGeometricToleranceModifier) -> StepDimTol_Array1OfGeometricToleranceModifier: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepDimTol_Array1OfGeometricToleranceModifier: 
        """
        None
        """
    def ChangeFirst(self) -> StepDimTol_GeometricToleranceModifier: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_GeometricToleranceModifier: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_GeometricToleranceModifier: 
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
    def First(self) -> StepDimTol_GeometricToleranceModifier: 
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
    def Init(self,theValue : StepDimTol_GeometricToleranceModifier) -> None: 
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
    def Last(self) -> StepDimTol_GeometricToleranceModifier: 
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
    def Move(self,theOther : StepDimTol_Array1OfGeometricToleranceModifier) -> StepDimTol_Array1OfGeometricToleranceModifier: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_GeometricToleranceModifier) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_GeometricToleranceModifier: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfGeometricToleranceModifier) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepDimTol_GeometricToleranceModifier) -> None: ...
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
class StepDimTol_HArray1OfToleranceZoneTarget(StepDimTol_Array1OfToleranceZoneTarget, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepDimTol_Array1OfToleranceZoneTarget: 
        """
        None
        """
    def Assign(self,theOther : StepDimTol_Array1OfToleranceZoneTarget) -> StepDimTol_Array1OfToleranceZoneTarget: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepDimTol_Array1OfToleranceZoneTarget: 
        """
        None
        """
    def ChangeFirst(self) -> StepDimTol_ToleranceZoneTarget: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepDimTol_ToleranceZoneTarget: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepDimTol_ToleranceZoneTarget: 
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
    def First(self) -> StepDimTol_ToleranceZoneTarget: 
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
    def Init(self,theValue : StepDimTol_ToleranceZoneTarget) -> None: 
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
    def Last(self) -> StepDimTol_ToleranceZoneTarget: 
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
    def Move(self,theOther : StepDimTol_Array1OfToleranceZoneTarget) -> StepDimTol_Array1OfToleranceZoneTarget: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepDimTol_ToleranceZoneTarget) -> None: 
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
    def Value(self,theIndex : int) -> StepDimTol_ToleranceZoneTarget: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepDimTol_Array1OfToleranceZoneTarget) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepDimTol_ToleranceZoneTarget) -> None: ...
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
class StepDimTol_LimitCondition():
    """
    None

    Members:

      StepDimTol_MaximumMaterialCondition

      StepDimTol_LeastMaterialCondition

      StepDimTol_RegardlessOfFeatureSize
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
    StepDimTol_LeastMaterialCondition: OCP.StepDimTol.StepDimTol_LimitCondition # value = <StepDimTol_LimitCondition.StepDimTol_LeastMaterialCondition: 1>
    StepDimTol_MaximumMaterialCondition: OCP.StepDimTol.StepDimTol_LimitCondition # value = <StepDimTol_LimitCondition.StepDimTol_MaximumMaterialCondition: 0>
    StepDimTol_RegardlessOfFeatureSize: OCP.StepDimTol.StepDimTol_LimitCondition # value = <StepDimTol_LimitCondition.StepDimTol_RegardlessOfFeatureSize: 2>
    __entries: dict # value = {'StepDimTol_MaximumMaterialCondition': (<StepDimTol_LimitCondition.StepDimTol_MaximumMaterialCondition: 0>, None), 'StepDimTol_LeastMaterialCondition': (<StepDimTol_LimitCondition.StepDimTol_LeastMaterialCondition: 1>, None), 'StepDimTol_RegardlessOfFeatureSize': (<StepDimTol_LimitCondition.StepDimTol_RegardlessOfFeatureSize: 2>, None)}
    __members__: dict # value = {'StepDimTol_MaximumMaterialCondition': <StepDimTol_LimitCondition.StepDimTol_MaximumMaterialCondition: 0>, 'StepDimTol_LeastMaterialCondition': <StepDimTol_LimitCondition.StepDimTol_LeastMaterialCondition: 1>, 'StepDimTol_RegardlessOfFeatureSize': <StepDimTol_LimitCondition.StepDimTol_RegardlessOfFeatureSize: 2>}
    pass
class StepDimTol_LineProfileTolerance(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity LineProfileToleranceRepresentation of STEP entity LineProfileToleranceRepresentation of STEP entity LineProfileTolerance
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
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_ModifiedGeometricTolerance(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ModifiedGeometricToleranceRepresentation of STEP entity ModifiedGeometricToleranceRepresentation of STEP entity ModifiedGeometricTolerance
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theModifier : StepDimTol_LimitCondition) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theModifier : StepDimTol_LimitCondition) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Modifier(self) -> StepDimTol_LimitCondition: 
        """
        Returns field Modifier
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetModifier(self,theModifier : StepDimTol_LimitCondition) -> None: 
        """
        Set field Modifier
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_ToleranceZoneDefinition(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ToleranceZoneDefinitionRepresentation of STEP entity ToleranceZoneDefinitionRepresentation of STEP entity ToleranceZoneDefinition
    """
    def Boundaries(self) -> OCP.StepRepr.StepRepr_HArray1OfShapeAspect: 
        """
        Returns field Boundaries
        """
    def BoundariesValue(self,theNum : int) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns Boundaries with the given number
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
    def Init(self,theZone : StepDimTol_ToleranceZone,theBoundaries : OCP.StepRepr.StepRepr_HArray1OfShapeAspect) -> None: 
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
    def NbBoundaries(self) -> int: 
        """
        Returns number of Boundaries
        """
    def SetBoundaries(self,theBoundaries : OCP.StepRepr.StepRepr_HArray1OfShapeAspect) -> None: 
        """
        Set field Boundaries
        """
    def SetBoundariesValue(self,theNum : int,theItem : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Sets Boundaries with given number
        """
    def SetZone(self,theZone : StepDimTol_ToleranceZone) -> None: 
        """
        Set field Zone
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Zone(self) -> StepDimTol_ToleranceZone: 
        """
        Returns field Zone
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_ParallelismTolerance(StepDimTol_GeometricToleranceWithDatumReference, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ParallelismToleranceRepresentation of STEP entity ParallelismToleranceRepresentation of STEP entity ParallelismTolerance
    """
    def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: 
        """
        Returns field DatumSystem AP214
        """
    def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: 
        """
        Returns field DatumSystem AP242
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Set field DatumSystem AP214

        Set field DatumSystem AP242
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_PerpendicularityTolerance(StepDimTol_GeometricToleranceWithDatumReference, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity PerpendicularityToleranceRepresentation of STEP entity PerpendicularityToleranceRepresentation of STEP entity PerpendicularityTolerance
    """
    def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: 
        """
        Returns field DatumSystem AP214
        """
    def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: 
        """
        Returns field DatumSystem AP242
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Set field DatumSystem AP214

        Set field DatumSystem AP242
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_PlacedDatumTargetFeature(StepDimTol_DatumTarget, OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity PlacedDatumTargetFeatureRepresentation of STEP entity PlacedDatumTargetFeatureRepresentation of STEP entity PlacedDatumTargetFeature
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
    def Init(self,theShapeAspect_Name : OCP.TCollection.TCollection_HAsciiString,theShapeAspect_Description : OCP.TCollection.TCollection_HAsciiString,theShapeAspect_OfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theShapeAspect_ProductDefinitional : OCP.StepData.StepData_Logical,theTargetId : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def SetTargetId(self,theTargetId : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field TargetId
        """
    def TargetId(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field TargetId
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
class StepDimTol_PositionTolerance(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity PositionToleranceRepresentation of STEP entity PositionToleranceRepresentation of STEP entity PositionTolerance
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
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_ProjectedZoneDefinition(StepDimTol_ToleranceZoneDefinition, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ProjectedZoneDefinitionRepresentation of STEP entity ProjectedZoneDefinitionRepresentation of STEP entity ProjectedZoneDefinition
    """
    def Boundaries(self) -> OCP.StepRepr.StepRepr_HArray1OfShapeAspect: 
        """
        Returns field Boundaries
        """
    def BoundariesValue(self,theNum : int) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns Boundaries with the given number
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
    def Init(self,theZone : StepDimTol_ToleranceZone,theBoundaries : OCP.StepRepr.StepRepr_HArray1OfShapeAspect,theProjectionEnd : OCP.StepRepr.StepRepr_ShapeAspect,theProjectionLength : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
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
    def NbBoundaries(self) -> int: 
        """
        Returns number of Boundaries
        """
    def ProjectionEnd(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field ProjectionEnd
        """
    def ProjectionLength(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        Returns field ProjectionLength
        """
    def SetBoundaries(self,theBoundaries : OCP.StepRepr.StepRepr_HArray1OfShapeAspect) -> None: 
        """
        Set field Boundaries
        """
    def SetBoundariesValue(self,theNum : int,theItem : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Sets Boundaries with given number
        """
    def SetProjectionEnd(self,theProjectionEnd : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field ProjectionEnd
        """
    def SetProjectionLength(self,theProjectionLength : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        Set field ProjectionLength
        """
    def SetZone(self,theZone : StepDimTol_ToleranceZone) -> None: 
        """
        Set field Zone
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Zone(self) -> StepDimTol_ToleranceZone: 
        """
        Returns field Zone
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_RoundnessTolerance(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity RoundnessToleranceRepresentation of STEP entity RoundnessToleranceRepresentation of STEP entity RoundnessTolerance
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
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_RunoutZoneDefinition(StepDimTol_ToleranceZoneDefinition, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ToleranceZoneDefinitionRepresentation of STEP entity ToleranceZoneDefinitionRepresentation of STEP entity ToleranceZoneDefinition
    """
    def Boundaries(self) -> OCP.StepRepr.StepRepr_HArray1OfShapeAspect: 
        """
        Returns field Boundaries
        """
    def BoundariesValue(self,theNum : int) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns Boundaries with the given number
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
    def Init(self,theZone : StepDimTol_ToleranceZone,theBoundaries : OCP.StepRepr.StepRepr_HArray1OfShapeAspect,theOrientation : StepDimTol_RunoutZoneOrientation) -> None: 
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
    def NbBoundaries(self) -> int: 
        """
        Returns number of Boundaries
        """
    def Orientation(self) -> StepDimTol_RunoutZoneOrientation: 
        """
        Returns field Orientation
        """
    def SetBoundaries(self,theBoundaries : OCP.StepRepr.StepRepr_HArray1OfShapeAspect) -> None: 
        """
        Set field Boundaries
        """
    def SetBoundariesValue(self,theNum : int,theItem : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Sets Boundaries with given number
        """
    def SetOrientation(self,theOrientation : StepDimTol_RunoutZoneOrientation) -> None: 
        """
        Set field Orientation
        """
    def SetZone(self,theZone : StepDimTol_ToleranceZone) -> None: 
        """
        Set field Zone
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Zone(self) -> StepDimTol_ToleranceZone: 
        """
        Returns field Zone
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_RunoutZoneOrientation(OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def Angle(self) -> OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit: 
        """
        Returns field Angle
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
    def Init(self,theAngle : OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit) -> None: 
        """
        Init all field own and inherited
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
    def SetAngle(self,theAngle : OCP.StepBasic.StepBasic_PlaneAngleMeasureWithUnit) -> None: 
        """
        Set field Angle
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
class StepDimTol_ShapeToleranceSelect(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type ShapeToleranceSelect
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
        Recognizes a kind of ShapeToleranceSelect select type 1 -> GeometricTolerance from StepDimTol 2 -> PlusMinusTolerance from StepShape 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def GeometricTolerance(self) -> StepDimTol_GeometricTolerance: 
        """
        Returns Value as GeometricTolerance (or Null if another type)
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
    def PlusMinusTolerance(self) -> OCP.StepShape.StepShape_PlusMinusTolerance: 
        """
        Returns Value as PlusMinusTolerance (or Null if another type)
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
class StepDimTol_SimpleDatumReferenceModifier():
    """
    None

    Members:

      StepDimTol_SDRMAnyCrossSection

      StepDimTol_SDRMAnyLongitudinalSection

      StepDimTol_SDRMBasic

      StepDimTol_SDRMContactingFeature

      StepDimTol_SDRMDegreeOfFreedomConstraintU

      StepDimTol_SDRMDegreeOfFreedomConstraintV

      StepDimTol_SDRMDegreeOfFreedomConstraintW

      StepDimTol_SDRMDegreeOfFreedomConstraintX

      StepDimTol_SDRMDegreeOfFreedomConstraintY

      StepDimTol_SDRMDegreeOfFreedomConstraintZ

      StepDimTol_SDRMDistanceVariable

      StepDimTol_SDRMFreeState

      StepDimTol_SDRMLeastMaterialRequirement

      StepDimTol_SDRMLine

      StepDimTol_SDRMMajorDiameter

      StepDimTol_SDRMMaximumMaterialRequirement

      StepDimTol_SDRMMinorDiameter

      StepDimTol_SDRMOrientation

      StepDimTol_SDRMPitchDiameter

      StepDimTol_SDRMPlane

      StepDimTol_SDRMPoint

      StepDimTol_SDRMTranslation
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
    StepDimTol_SDRMAnyCrossSection: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyCrossSection: 0>
    StepDimTol_SDRMAnyLongitudinalSection: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyLongitudinalSection: 1>
    StepDimTol_SDRMBasic: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMBasic: 2>
    StepDimTol_SDRMContactingFeature: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMContactingFeature: 3>
    StepDimTol_SDRMDegreeOfFreedomConstraintU: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintU: 4>
    StepDimTol_SDRMDegreeOfFreedomConstraintV: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintV: 5>
    StepDimTol_SDRMDegreeOfFreedomConstraintW: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintW: 6>
    StepDimTol_SDRMDegreeOfFreedomConstraintX: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintX: 7>
    StepDimTol_SDRMDegreeOfFreedomConstraintY: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintY: 8>
    StepDimTol_SDRMDegreeOfFreedomConstraintZ: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintZ: 9>
    StepDimTol_SDRMDistanceVariable: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDistanceVariable: 10>
    StepDimTol_SDRMFreeState: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMFreeState: 11>
    StepDimTol_SDRMLeastMaterialRequirement: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLeastMaterialRequirement: 12>
    StepDimTol_SDRMLine: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLine: 13>
    StepDimTol_SDRMMajorDiameter: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMajorDiameter: 14>
    StepDimTol_SDRMMaximumMaterialRequirement: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMaximumMaterialRequirement: 15>
    StepDimTol_SDRMMinorDiameter: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMinorDiameter: 16>
    StepDimTol_SDRMOrientation: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMOrientation: 17>
    StepDimTol_SDRMPitchDiameter: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPitchDiameter: 18>
    StepDimTol_SDRMPlane: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPlane: 19>
    StepDimTol_SDRMPoint: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPoint: 20>
    StepDimTol_SDRMTranslation: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMTranslation: 21>
    __entries: dict # value = {'StepDimTol_SDRMAnyCrossSection': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyCrossSection: 0>, None), 'StepDimTol_SDRMAnyLongitudinalSection': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyLongitudinalSection: 1>, None), 'StepDimTol_SDRMBasic': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMBasic: 2>, None), 'StepDimTol_SDRMContactingFeature': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMContactingFeature: 3>, None), 'StepDimTol_SDRMDegreeOfFreedomConstraintU': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintU: 4>, None), 'StepDimTol_SDRMDegreeOfFreedomConstraintV': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintV: 5>, None), 'StepDimTol_SDRMDegreeOfFreedomConstraintW': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintW: 6>, None), 'StepDimTol_SDRMDegreeOfFreedomConstraintX': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintX: 7>, None), 'StepDimTol_SDRMDegreeOfFreedomConstraintY': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintY: 8>, None), 'StepDimTol_SDRMDegreeOfFreedomConstraintZ': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintZ: 9>, None), 'StepDimTol_SDRMDistanceVariable': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDistanceVariable: 10>, None), 'StepDimTol_SDRMFreeState': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMFreeState: 11>, None), 'StepDimTol_SDRMLeastMaterialRequirement': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLeastMaterialRequirement: 12>, None), 'StepDimTol_SDRMLine': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLine: 13>, None), 'StepDimTol_SDRMMajorDiameter': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMajorDiameter: 14>, None), 'StepDimTol_SDRMMaximumMaterialRequirement': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMaximumMaterialRequirement: 15>, None), 'StepDimTol_SDRMMinorDiameter': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMinorDiameter: 16>, None), 'StepDimTol_SDRMOrientation': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMOrientation: 17>, None), 'StepDimTol_SDRMPitchDiameter': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPitchDiameter: 18>, None), 'StepDimTol_SDRMPlane': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPlane: 19>, None), 'StepDimTol_SDRMPoint': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPoint: 20>, None), 'StepDimTol_SDRMTranslation': (<StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMTranslation: 21>, None)}
    __members__: dict # value = {'StepDimTol_SDRMAnyCrossSection': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyCrossSection: 0>, 'StepDimTol_SDRMAnyLongitudinalSection': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyLongitudinalSection: 1>, 'StepDimTol_SDRMBasic': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMBasic: 2>, 'StepDimTol_SDRMContactingFeature': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMContactingFeature: 3>, 'StepDimTol_SDRMDegreeOfFreedomConstraintU': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintU: 4>, 'StepDimTol_SDRMDegreeOfFreedomConstraintV': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintV: 5>, 'StepDimTol_SDRMDegreeOfFreedomConstraintW': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintW: 6>, 'StepDimTol_SDRMDegreeOfFreedomConstraintX': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintX: 7>, 'StepDimTol_SDRMDegreeOfFreedomConstraintY': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintY: 8>, 'StepDimTol_SDRMDegreeOfFreedomConstraintZ': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintZ: 9>, 'StepDimTol_SDRMDistanceVariable': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDistanceVariable: 10>, 'StepDimTol_SDRMFreeState': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMFreeState: 11>, 'StepDimTol_SDRMLeastMaterialRequirement': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLeastMaterialRequirement: 12>, 'StepDimTol_SDRMLine': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLine: 13>, 'StepDimTol_SDRMMajorDiameter': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMajorDiameter: 14>, 'StepDimTol_SDRMMaximumMaterialRequirement': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMaximumMaterialRequirement: 15>, 'StepDimTol_SDRMMinorDiameter': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMinorDiameter: 16>, 'StepDimTol_SDRMOrientation': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMOrientation: 17>, 'StepDimTol_SDRMPitchDiameter': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPitchDiameter: 18>, 'StepDimTol_SDRMPlane': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPlane: 19>, 'StepDimTol_SDRMPoint': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPoint: 20>, 'StepDimTol_SDRMTranslation': <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMTranslation: 21>}
    pass
class StepDimTol_SimpleDatumReferenceModifierMember(OCP.StepData.StepData_SelectInt, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Defines SimpleDatumReferenceModifier as unique member of DatumReferenceModifier Works with an EnumToolDefines SimpleDatumReferenceModifier as unique member of DatumReferenceModifier Works with an EnumToolDefines SimpleDatumReferenceModifier as unique member of DatumReferenceModifier Works with an EnumTool
    """
    def Boolean(self) -> bool: 
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        None
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
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        None
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
    def SetEnumText(self,theValue : int,theText : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        None
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
    def SetName(self,arg1 : str) -> bool: 
        """
        None
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def SetValue(self,theValue : StepDimTol_SimpleDatumReferenceModifier) -> None: 
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
    def Value(self) -> StepDimTol_SimpleDatumReferenceModifier: 
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
class StepDimTol_StraightnessTolerance(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity StraightnessToleranceRepresentation of STEP entity StraightnessToleranceRepresentation of STEP entity StraightnessTolerance
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
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_SurfaceProfileTolerance(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SurfaceProfileToleranceRepresentation of STEP entity SurfaceProfileToleranceRepresentation of STEP entity SurfaceProfileTolerance
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
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_SymmetryTolerance(StepDimTol_GeometricToleranceWithDatumReference, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SymmetryToleranceRepresentation of STEP entity SymmetryToleranceRepresentation of STEP entity SymmetryTolerance
    """
    def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: 
        """
        Returns field DatumSystem AP214
        """
    def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: 
        """
        Returns field DatumSystem AP242
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Set field DatumSystem AP214

        Set field DatumSystem AP242
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_ToleranceZone(OCP.StepRepr.StepRepr_ShapeAspect, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ToleranceZoneRepresentation of STEP entity ToleranceZoneRepresentation of STEP entity ToleranceZone
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefiningTolerance(self) -> StepDimTol_HArray1OfToleranceZoneTarget: 
        """
        Returns field DefiningTolerance
        """
    def DefiningToleranceValue(self,theNum : int) -> StepDimTol_ToleranceZoneTarget: 
        """
        Returns Defining Tolerance with the given number
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
    def Form(self) -> StepDimTol_ToleranceZoneForm: 
        """
        Returns field Form
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theOfShape : OCP.StepRepr.StepRepr_ProductDefinitionShape,theProductDefinitional : OCP.StepData.StepData_Logical,theDefiningTolerance : StepDimTol_HArray1OfToleranceZoneTarget,theForm : StepDimTol_ToleranceZoneForm) -> None: 
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
    def NbDefiningTolerances(self) -> int: 
        """
        Returns number of Defining Tolerances
        """
    def OfShape(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def ProductDefinitional(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetDefiningTolerance(self,theDefiningTolerance : StepDimTol_HArray1OfToleranceZoneTarget) -> None: 
        """
        Set field DefiningTolerance
        """
    def SetDefiningToleranceValue(self,theNum : int,theItem : StepDimTol_ToleranceZoneTarget) -> None: 
        """
        Sets Defining Tolerance with given number
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetForm(self,theForm : StepDimTol_ToleranceZoneForm) -> None: 
        """
        Set field Form
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
class StepDimTol_NonUniformZoneDefinition(StepDimTol_ToleranceZoneDefinition, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NonUniformZoneDefinitionRepresentation of STEP entity NonUniformZoneDefinitionRepresentation of STEP entity NonUniformZoneDefinition
    """
    def Boundaries(self) -> OCP.StepRepr.StepRepr_HArray1OfShapeAspect: 
        """
        Returns field Boundaries
        """
    def BoundariesValue(self,theNum : int) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns Boundaries with the given number
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
    def Init(self,theZone : StepDimTol_ToleranceZone,theBoundaries : OCP.StepRepr.StepRepr_HArray1OfShapeAspect) -> None: 
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
    def NbBoundaries(self) -> int: 
        """
        Returns number of Boundaries
        """
    def SetBoundaries(self,theBoundaries : OCP.StepRepr.StepRepr_HArray1OfShapeAspect) -> None: 
        """
        Set field Boundaries
        """
    def SetBoundariesValue(self,theNum : int,theItem : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Sets Boundaries with given number
        """
    def SetZone(self,theZone : StepDimTol_ToleranceZone) -> None: 
        """
        Set field Zone
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Zone(self) -> StepDimTol_ToleranceZone: 
        """
        Returns field Zone
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_ToleranceZoneForm(OCP.Standard.Standard_Transient):
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Init all field own and inherited
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
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepDimTol_ToleranceZoneTarget(OCP.StepData.StepData_SelectType):
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
        Recognizes a ToleranceZoneTarget Kind Entity that is : 1 -> DimensionalLocation 2 -> DimensionalSize 3 -> GeometricTolerance 4 -> GeneralDatumReference 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DimensionalLocation(self) -> OCP.StepShape.StepShape_DimensionalLocation: 
        """
        returns Value as a DimensionalLocation (Null if another type)
        """
    def DimensionalSize(self) -> OCP.StepShape.StepShape_DimensionalSize: 
        """
        returns Value as a DimensionalSize (Null if another type)
        """
    def GeneralDatumReference(self) -> StepDimTol_GeneralDatumReference: 
        """
        returns Value as a GeneralDatumReference (Null if another type)
        """
    def GeometricTolerance(self) -> StepDimTol_GeometricTolerance: 
        """
        returns Value as a GeometricTolerance (Null if another type)
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
class StepDimTol_TotalRunoutTolerance(StepDimTol_GeometricToleranceWithDatumReference, StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity TotalRunoutToleranceRepresentation of STEP entity TotalRunoutToleranceRepresentation of STEP entity TotalRunoutTolerance
    """
    def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: 
        """
        Returns field DatumSystem AP214
        """
    def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: 
        """
        Returns field DatumSystem AP242
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
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Initialize all fields (own and inherited) AP214

        Initialize all fields (own and inherited) AP242
        """
    @overload
    def Init(self,theGeometricTolerance_Name : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Description : OCP.TCollection.TCollection_HAsciiString,theGeometricTolerance_Magnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theGeometricTolerance_TolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumReference) -> None: 
        """
        Set field DatumSystem AP214

        Set field DatumSystem AP242
        """
    @overload
    def SetDatumSystem(self,theDatumSystem : StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepDimTol_UnequallyDisposedGeometricTolerance(StepDimTol_GeometricTolerance, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity UnequallyDisposedGeometricToleranceRepresentation of STEP entity UnequallyDisposedGeometricToleranceRepresentation of STEP entity UnequallyDisposedGeometricTolerance
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
    def Displacement(self) -> OCP.StepBasic.StepBasic_LengthMeasureWithUnit: 
        """
        Returns field Displacement
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theDescription : OCP.TCollection.TCollection_HAsciiString,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget,theDisplacement : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
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
    def Magnitude(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        Returns field Magnitude
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Name
        """
    def SetDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetDisplacement(self,theDisplacement : OCP.StepBasic.StepBasic_LengthMeasureWithUnit) -> None: 
        """
        Set field Displacement
        """
    def SetMagnitude(self,theMagnitude : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        Set field Magnitude
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field TolerancedShapeAspect AP214

        Set field TolerancedShapeAspect AP242
        """
    @overload
    def SetTolerancedShapeAspect(self,theTolerancedShapeAspect : StepDimTol_GeometricToleranceTarget) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: 
        """
        Returns field TolerancedShapeAspect Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
StepDimTol_Circular: OCP.StepDimTol.StepDimTol_AreaUnitType # value = <StepDimTol_AreaUnitType.StepDimTol_Circular: 0>
StepDimTol_CircularOrCylindrical: OCP.StepDimTol.StepDimTol_DatumReferenceModifierType # value = <StepDimTol_DatumReferenceModifierType.StepDimTol_CircularOrCylindrical: 0>
StepDimTol_Distance: OCP.StepDimTol.StepDimTol_DatumReferenceModifierType # value = <StepDimTol_DatumReferenceModifierType.StepDimTol_Distance: 1>
StepDimTol_GTMAnyCrossSection: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMAnyCrossSection: 0>
StepDimTol_GTMCommonZone: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMCommonZone: 1>
StepDimTol_GTMEachRadialElement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMEachRadialElement: 2>
StepDimTol_GTMFreeState: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMFreeState: 3>
StepDimTol_GTMLeastMaterialRequirement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLeastMaterialRequirement: 4>
StepDimTol_GTMLineElement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLineElement: 5>
StepDimTol_GTMMajorDiameter: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMajorDiameter: 6>
StepDimTol_GTMMaximumMaterialRequirement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMaximumMaterialRequirement: 7>
StepDimTol_GTMMinorDiameter: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMinorDiameter: 8>
StepDimTol_GTMNotConvex: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMNotConvex: 9>
StepDimTol_GTMPitchDiameter: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMPitchDiameter: 10>
StepDimTol_GTMReciprocityRequirement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMReciprocityRequirement: 11>
StepDimTol_GTMSeparateRequirement: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMSeparateRequirement: 12>
StepDimTol_GTMStatisticalTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMStatisticalTolerance: 13>
StepDimTol_GTMTangentPlane: OCP.StepDimTol.StepDimTol_GeometricToleranceModifier # value = <StepDimTol_GeometricToleranceModifier.StepDimTol_GTMTangentPlane: 14>
StepDimTol_GTTAngularityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTAngularityTolerance: 0>
StepDimTol_GTTCircularRunoutTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTCircularRunoutTolerance: 1>
StepDimTol_GTTCoaxialityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTCoaxialityTolerance: 2>
StepDimTol_GTTConcentricityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTConcentricityTolerance: 3>
StepDimTol_GTTCylindricityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTCylindricityTolerance: 4>
StepDimTol_GTTFlatnessTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTFlatnessTolerance: 5>
StepDimTol_GTTLineProfileTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTLineProfileTolerance: 6>
StepDimTol_GTTParallelismTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTParallelismTolerance: 7>
StepDimTol_GTTPerpendicularityTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTPerpendicularityTolerance: 8>
StepDimTol_GTTPositionTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTPositionTolerance: 9>
StepDimTol_GTTRoundnessTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTRoundnessTolerance: 10>
StepDimTol_GTTStraightnessTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTStraightnessTolerance: 11>
StepDimTol_GTTSurfaceProfileTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTSurfaceProfileTolerance: 12>
StepDimTol_GTTSymmetryTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTSymmetryTolerance: 13>
StepDimTol_GTTTotalRunoutTolerance: OCP.StepDimTol.StepDimTol_GeometricToleranceType # value = <StepDimTol_GeometricToleranceType.StepDimTol_GTTTotalRunoutTolerance: 14>
StepDimTol_LeastMaterialCondition: OCP.StepDimTol.StepDimTol_LimitCondition # value = <StepDimTol_LimitCondition.StepDimTol_LeastMaterialCondition: 1>
StepDimTol_MaximumMaterialCondition: OCP.StepDimTol.StepDimTol_LimitCondition # value = <StepDimTol_LimitCondition.StepDimTol_MaximumMaterialCondition: 0>
StepDimTol_Projected: OCP.StepDimTol.StepDimTol_DatumReferenceModifierType # value = <StepDimTol_DatumReferenceModifierType.StepDimTol_Projected: 2>
StepDimTol_Rectangular: OCP.StepDimTol.StepDimTol_AreaUnitType # value = <StepDimTol_AreaUnitType.StepDimTol_Rectangular: 1>
StepDimTol_RegardlessOfFeatureSize: OCP.StepDimTol.StepDimTol_LimitCondition # value = <StepDimTol_LimitCondition.StepDimTol_RegardlessOfFeatureSize: 2>
StepDimTol_SDRMAnyCrossSection: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyCrossSection: 0>
StepDimTol_SDRMAnyLongitudinalSection: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyLongitudinalSection: 1>
StepDimTol_SDRMBasic: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMBasic: 2>
StepDimTol_SDRMContactingFeature: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMContactingFeature: 3>
StepDimTol_SDRMDegreeOfFreedomConstraintU: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintU: 4>
StepDimTol_SDRMDegreeOfFreedomConstraintV: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintV: 5>
StepDimTol_SDRMDegreeOfFreedomConstraintW: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintW: 6>
StepDimTol_SDRMDegreeOfFreedomConstraintX: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintX: 7>
StepDimTol_SDRMDegreeOfFreedomConstraintY: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintY: 8>
StepDimTol_SDRMDegreeOfFreedomConstraintZ: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintZ: 9>
StepDimTol_SDRMDistanceVariable: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDistanceVariable: 10>
StepDimTol_SDRMFreeState: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMFreeState: 11>
StepDimTol_SDRMLeastMaterialRequirement: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLeastMaterialRequirement: 12>
StepDimTol_SDRMLine: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLine: 13>
StepDimTol_SDRMMajorDiameter: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMajorDiameter: 14>
StepDimTol_SDRMMaximumMaterialRequirement: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMaximumMaterialRequirement: 15>
StepDimTol_SDRMMinorDiameter: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMinorDiameter: 16>
StepDimTol_SDRMOrientation: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMOrientation: 17>
StepDimTol_SDRMPitchDiameter: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPitchDiameter: 18>
StepDimTol_SDRMPlane: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPlane: 19>
StepDimTol_SDRMPoint: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPoint: 20>
StepDimTol_SDRMTranslation: OCP.StepDimTol.StepDimTol_SimpleDatumReferenceModifier # value = <StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMTranslation: 21>
StepDimTol_Spherical: OCP.StepDimTol.StepDimTol_DatumReferenceModifierType # value = <StepDimTol_DatumReferenceModifierType.StepDimTol_Spherical: 3>
StepDimTol_Square: OCP.StepDimTol.StepDimTol_AreaUnitType # value = <StepDimTol_AreaUnitType.StepDimTol_Square: 2>
