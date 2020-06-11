import OCP.XCAFDimTolObjects
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TDocStd
import OCP.TCollection
import OCP.TopoDS
import OCP.Standard
import OCP.gp
import OCP.TColStd
__all__  = [
"XCAFDimTolObjects_DatumModifWithValue",
"XCAFDimTolObjects_DatumModifiersSequence",
"XCAFDimTolObjects_DatumObject",
"XCAFDimTolObjects_DatumObjectSequence",
"XCAFDimTolObjects_DatumSingleModif",
"XCAFDimTolObjects_DatumTargetType",
"XCAFDimTolObjects_DimensionFormVariance",
"XCAFDimTolObjects_DimensionGrade",
"XCAFDimTolObjects_DimensionModif",
"XCAFDimTolObjects_DimensionModifiersSequence",
"XCAFDimTolObjects_DimensionObject",
"XCAFDimTolObjects_DimensionObjectSequence",
"XCAFDimTolObjects_DimensionQualifier",
"XCAFDimTolObjects_DimensionType",
"XCAFDimTolObjects_GeomToleranceMatReqModif",
"XCAFDimTolObjects_GeomToleranceModif",
"XCAFDimTolObjects_GeomToleranceModifiersSequence",
"XCAFDimTolObjects_GeomToleranceObject",
"XCAFDimTolObjects_GeomToleranceObjectSequence",
"XCAFDimTolObjects_GeomToleranceType",
"XCAFDimTolObjects_GeomToleranceTypeValue",
"XCAFDimTolObjects_GeomToleranceZoneModif",
"XCAFDimTolObjects_ToleranceZoneAffectedPlane",
"XCAFDimTolObjects_Tool",
"XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical",
"XCAFDimTolObjects_DatumModifWithValue_Distance",
"XCAFDimTolObjects_DatumModifWithValue_None",
"XCAFDimTolObjects_DatumModifWithValue_Projected",
"XCAFDimTolObjects_DatumModifWithValue_Spherical",
"XCAFDimTolObjects_DatumSingleModif_AnyCrossSection",
"XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection",
"XCAFDimTolObjects_DatumSingleModif_Basic",
"XCAFDimTolObjects_DatumSingleModif_ContactingFeature",
"XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU",
"XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV",
"XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW",
"XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX",
"XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY",
"XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ",
"XCAFDimTolObjects_DatumSingleModif_DistanceVariable",
"XCAFDimTolObjects_DatumSingleModif_FreeState",
"XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement",
"XCAFDimTolObjects_DatumSingleModif_Line",
"XCAFDimTolObjects_DatumSingleModif_MajorDiameter",
"XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement",
"XCAFDimTolObjects_DatumSingleModif_MinorDiameter",
"XCAFDimTolObjects_DatumSingleModif_Orientation",
"XCAFDimTolObjects_DatumSingleModif_PitchDiameter",
"XCAFDimTolObjects_DatumSingleModif_Plane",
"XCAFDimTolObjects_DatumSingleModif_Point",
"XCAFDimTolObjects_DatumSingleModif_Translation",
"XCAFDimTolObjects_DatumTargetType_Area",
"XCAFDimTolObjects_DatumTargetType_Circle",
"XCAFDimTolObjects_DatumTargetType_Line",
"XCAFDimTolObjects_DatumTargetType_Point",
"XCAFDimTolObjects_DatumTargetType_Rectangle",
"XCAFDimTolObjects_DimensionFormVariance_A",
"XCAFDimTolObjects_DimensionFormVariance_B",
"XCAFDimTolObjects_DimensionFormVariance_C",
"XCAFDimTolObjects_DimensionFormVariance_CD",
"XCAFDimTolObjects_DimensionFormVariance_D",
"XCAFDimTolObjects_DimensionFormVariance_E",
"XCAFDimTolObjects_DimensionFormVariance_EF",
"XCAFDimTolObjects_DimensionFormVariance_F",
"XCAFDimTolObjects_DimensionFormVariance_FG",
"XCAFDimTolObjects_DimensionFormVariance_G",
"XCAFDimTolObjects_DimensionFormVariance_H",
"XCAFDimTolObjects_DimensionFormVariance_J",
"XCAFDimTolObjects_DimensionFormVariance_JS",
"XCAFDimTolObjects_DimensionFormVariance_K",
"XCAFDimTolObjects_DimensionFormVariance_M",
"XCAFDimTolObjects_DimensionFormVariance_N",
"XCAFDimTolObjects_DimensionFormVariance_None",
"XCAFDimTolObjects_DimensionFormVariance_P",
"XCAFDimTolObjects_DimensionFormVariance_R",
"XCAFDimTolObjects_DimensionFormVariance_S",
"XCAFDimTolObjects_DimensionFormVariance_T",
"XCAFDimTolObjects_DimensionFormVariance_U",
"XCAFDimTolObjects_DimensionFormVariance_V",
"XCAFDimTolObjects_DimensionFormVariance_X",
"XCAFDimTolObjects_DimensionFormVariance_Y",
"XCAFDimTolObjects_DimensionFormVariance_Z",
"XCAFDimTolObjects_DimensionFormVariance_ZA",
"XCAFDimTolObjects_DimensionFormVariance_ZB",
"XCAFDimTolObjects_DimensionFormVariance_ZC",
"XCAFDimTolObjects_DimensionGrade_IT0",
"XCAFDimTolObjects_DimensionGrade_IT01",
"XCAFDimTolObjects_DimensionGrade_IT1",
"XCAFDimTolObjects_DimensionGrade_IT10",
"XCAFDimTolObjects_DimensionGrade_IT11",
"XCAFDimTolObjects_DimensionGrade_IT12",
"XCAFDimTolObjects_DimensionGrade_IT13",
"XCAFDimTolObjects_DimensionGrade_IT14",
"XCAFDimTolObjects_DimensionGrade_IT15",
"XCAFDimTolObjects_DimensionGrade_IT16",
"XCAFDimTolObjects_DimensionGrade_IT17",
"XCAFDimTolObjects_DimensionGrade_IT18",
"XCAFDimTolObjects_DimensionGrade_IT2",
"XCAFDimTolObjects_DimensionGrade_IT3",
"XCAFDimTolObjects_DimensionGrade_IT4",
"XCAFDimTolObjects_DimensionGrade_IT5",
"XCAFDimTolObjects_DimensionGrade_IT6",
"XCAFDimTolObjects_DimensionGrade_IT7",
"XCAFDimTolObjects_DimensionGrade_IT8",
"XCAFDimTolObjects_DimensionGrade_IT9",
"XCAFDimTolObjects_DimensionModif_AnyCrossSection",
"XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature",
"XCAFDimTolObjects_DimensionModif_AreaDiameter",
"XCAFDimTolObjects_DimensionModif_AverageSize",
"XCAFDimTolObjects_DimensionModif_Between",
"XCAFDimTolObjects_DimensionModif_CircumferenceDiameter",
"XCAFDimTolObjects_DimensionModif_CommonTolerance",
"XCAFDimTolObjects_DimensionModif_ContinuousFeature",
"XCAFDimTolObjects_DimensionModif_ControlledRadius",
"XCAFDimTolObjects_DimensionModif_FreeStateCondition",
"XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion",
"XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere",
"XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation",
"XCAFDimTolObjects_DimensionModif_MaximumSize",
"XCAFDimTolObjects_DimensionModif_MedianSize",
"XCAFDimTolObjects_DimensionModif_MidRangeSize",
"XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation",
"XCAFDimTolObjects_DimensionModif_MinimumSize",
"XCAFDimTolObjects_DimensionModif_RangeOfSizes",
"XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection",
"XCAFDimTolObjects_DimensionModif_Square",
"XCAFDimTolObjects_DimensionModif_StatisticalTolerance",
"XCAFDimTolObjects_DimensionModif_TwoPointSize",
"XCAFDimTolObjects_DimensionModif_VolumeDiameter",
"XCAFDimTolObjects_DimensionQualifier_Avg",
"XCAFDimTolObjects_DimensionQualifier_Max",
"XCAFDimTolObjects_DimensionQualifier_Min",
"XCAFDimTolObjects_DimensionQualifier_None",
"XCAFDimTolObjects_DimensionType_CommonLabel",
"XCAFDimTolObjects_DimensionType_DimensionPresentation",
"XCAFDimTolObjects_DimensionType_Location_Angular",
"XCAFDimTolObjects_DimensionType_Location_CurvedDistance",
"XCAFDimTolObjects_DimensionType_Location_LinearDistance",
"XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner",
"XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter",
"XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter",
"XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner",
"XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter",
"XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter",
"XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner",
"XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter",
"XCAFDimTolObjects_DimensionType_Location_None",
"XCAFDimTolObjects_DimensionType_Location_Oriented",
"XCAFDimTolObjects_DimensionType_Location_WithPath",
"XCAFDimTolObjects_DimensionType_Size_Angular",
"XCAFDimTolObjects_DimensionType_Size_CurveLength",
"XCAFDimTolObjects_DimensionType_Size_Diameter",
"XCAFDimTolObjects_DimensionType_Size_Radius",
"XCAFDimTolObjects_DimensionType_Size_SphericalDiameter",
"XCAFDimTolObjects_DimensionType_Size_SphericalRadius",
"XCAFDimTolObjects_DimensionType_Size_Thickness",
"XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter",
"XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius",
"XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter",
"XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius",
"XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter",
"XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius",
"XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter",
"XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius",
"XCAFDimTolObjects_DimensionType_Size_WithPath",
"XCAFDimTolObjects_GeomToleranceMatReqModif_L",
"XCAFDimTolObjects_GeomToleranceMatReqModif_M",
"XCAFDimTolObjects_GeomToleranceMatReqModif_None",
"XCAFDimTolObjects_GeomToleranceModif_All_Around",
"XCAFDimTolObjects_GeomToleranceModif_All_Over",
"XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section",
"XCAFDimTolObjects_GeomToleranceModif_Common_Zone",
"XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element",
"XCAFDimTolObjects_GeomToleranceModif_Free_State",
"XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement",
"XCAFDimTolObjects_GeomToleranceModif_Line_Element",
"XCAFDimTolObjects_GeomToleranceModif_Major_Diameter",
"XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement",
"XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter",
"XCAFDimTolObjects_GeomToleranceModif_Not_Convex",
"XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter",
"XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement",
"XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement",
"XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance",
"XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane",
"XCAFDimTolObjects_GeomToleranceTypeValue_Diameter",
"XCAFDimTolObjects_GeomToleranceTypeValue_None",
"XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter",
"XCAFDimTolObjects_GeomToleranceType_Angularity",
"XCAFDimTolObjects_GeomToleranceType_CircularRunout",
"XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness",
"XCAFDimTolObjects_GeomToleranceType_Coaxiality",
"XCAFDimTolObjects_GeomToleranceType_Concentricity",
"XCAFDimTolObjects_GeomToleranceType_Cylindricity",
"XCAFDimTolObjects_GeomToleranceType_Flatness",
"XCAFDimTolObjects_GeomToleranceType_None",
"XCAFDimTolObjects_GeomToleranceType_Parallelism",
"XCAFDimTolObjects_GeomToleranceType_Perpendicularity",
"XCAFDimTolObjects_GeomToleranceType_Position",
"XCAFDimTolObjects_GeomToleranceType_ProfileOfLine",
"XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface",
"XCAFDimTolObjects_GeomToleranceType_Straightness",
"XCAFDimTolObjects_GeomToleranceType_Symmetry",
"XCAFDimTolObjects_GeomToleranceType_TotalRunout",
"XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform",
"XCAFDimTolObjects_GeomToleranceZoneModif_None",
"XCAFDimTolObjects_GeomToleranceZoneModif_Projected",
"XCAFDimTolObjects_GeomToleranceZoneModif_Runout",
"XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection",
"XCAFDimTolObjects_ToleranceZoneAffectedPlane_None",
"XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation"
]
class XCAFDimTolObjects_DatumModifWithValue():
    """
    Defines modifirs

    Members:

      XCAFDimTolObjects_DatumModifWithValue_None

      XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical

      XCAFDimTolObjects_DatumModifWithValue_Distance

      XCAFDimTolObjects_DatumModifWithValue_Projected

      XCAFDimTolObjects_DatumModifWithValue_Spherical
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical
    XCAFDimTolObjects_DatumModifWithValue_Distance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Distance
    XCAFDimTolObjects_DatumModifWithValue_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_None
    XCAFDimTolObjects_DatumModifWithValue_Projected: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Projected
    XCAFDimTolObjects_DatumModifWithValue_Spherical: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Spherical
    __entries: dict # value = {'XCAFDimTolObjects_DatumModifWithValue_None': (XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_None, None), 'XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical': (XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical, None), 'XCAFDimTolObjects_DatumModifWithValue_Distance': (XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Distance, None), 'XCAFDimTolObjects_DatumModifWithValue_Projected': (XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Projected, None), 'XCAFDimTolObjects_DatumModifWithValue_Spherical': (XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Spherical, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DatumModifWithValue_None': XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_None, 'XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical': XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical, 'XCAFDimTolObjects_DatumModifWithValue_Distance': XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Distance, 'XCAFDimTolObjects_DatumModifWithValue_Projected': XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Projected, 'XCAFDimTolObjects_DatumModifWithValue_Spherical': XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Spherical}
    pass
class XCAFDimTolObjects_DatumModifiersSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : XCAFDimTolObjects_DatumModifiersSequence) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : XCAFDimTolObjects_DatumSingleModif) -> None: ...
    def Assign(self,theOther : XCAFDimTolObjects_DatumModifiersSequence) -> XCAFDimTolObjects_DatumModifiersSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> XCAFDimTolObjects_DatumSingleModif: 
        """
        First item access
        """
    def ChangeLast(self) -> XCAFDimTolObjects_DatumSingleModif: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> XCAFDimTolObjects_DatumSingleModif: 
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
    def First(self) -> XCAFDimTolObjects_DatumSingleModif: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : XCAFDimTolObjects_DatumModifiersSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : XCAFDimTolObjects_DatumSingleModif) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_DatumSingleModif) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_DatumModifiersSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> XCAFDimTolObjects_DatumSingleModif: 
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
    def Prepend(self,theSeq : XCAFDimTolObjects_DatumModifiersSequence) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : XCAFDimTolObjects_DatumSingleModif) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : XCAFDimTolObjects_DatumSingleModif) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : XCAFDimTolObjects_DatumModifiersSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> XCAFDimTolObjects_DatumSingleModif: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_DatumModifiersSequence) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class XCAFDimTolObjects_DatumObject(OCP.Standard.Standard_Transient):
    """
    Access object to store datumAccess object to store datumAccess object to store datum
    """
    def AddModifier(self,theModifier : XCAFDimTolObjects_DatumSingleModif) -> None: 
        """
        Adds a modifier to the datum sequence of modifiers.
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
    def GetDatumTarget(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns datum target shape.
        """
    def GetDatumTargetAxis(self) -> OCP.gp.gp_Ax2: 
        """
        Returns datum target axis. The Z axis of the datum placement denotes the normal of the surface pointing away from the material.
        """
    def GetDatumTargetLength(self) -> float: 
        """
        Returns datum target length for line and rectangle types. The length along the X axis of the datum placement.
        """
    def GetDatumTargetNumber(self) -> int: 
        """
        Returns datum target number.
        """
    def GetDatumTargetType(self) -> XCAFDimTolObjects_DatumTargetType: 
        """
        Returns datum target type
        """
    def GetDatumTargetWidth(self) -> float: 
        """
        Returns datum target width for rectangle type. The width along the derived Y axis, with the placement itself positioned at the centre of the rectangle.
        """
    def GetModifierWithValue(self,theModifier : XCAFDimTolObjects_DatumModifWithValue) -> Tuple[float]: 
        """
        Retrieves datum modifier with value.
        """
    def GetModifiers(self) -> XCAFDimTolObjects_DatumModifiersSequence: 
        """
        Returns a sequence of modifiers of the datum.
        """
    def GetName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns datum name.
        """
    def GetPlane(self) -> OCP.gp.gp_Ax2: 
        """
        Returns annotation plane.
        """
    def GetPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Gets point on the datum shape.
        """
    def GetPointTextAttach(self) -> OCP.gp.gp_Pnt: 
        """
        Gets datum text position.
        """
    def GetPosition(self) -> int: 
        """
        Returns datum position in the related geometric tolerance object.
        """
    def GetPresentation(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns graphical presentation of the object.
        """
    def GetPresentationName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns graphical presentation of the object.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSemanticName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns semantic name
        """
    def HasDatumTargetParams(self) -> bool: 
        """
        Returns True if the datum has valid parameters for datum target (width, length, circle radius etc)
        """
    def HasPlane(self) -> bool: 
        """
        Returns True if the datum has annotation plane.
        """
    def HasPoint(self) -> bool: 
        """
        Returns True if point on the datum target is specified.
        """
    def HasPointText(self) -> bool: 
        """
        Returns True if the datum text position is specified.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IsDatumTarget(self) -> bool: 
        """
        Returns True if the datum target is specified.

        Sets or drops the datum target indicator.
        """
    @overload
    def IsDatumTarget(self,theIsDT : bool) -> None: ...
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
    def SetDatumTarget(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets datum target shape.
        """
    def SetDatumTargetAxis(self,theAxis : OCP.gp.gp_Ax2) -> None: 
        """
        Sets datum target axis.
        """
    def SetDatumTargetLength(self,theLength : float) -> None: 
        """
        Sets datum target length.
        """
    def SetDatumTargetNumber(self,theNumber : int) -> None: 
        """
        Sets datum target number.
        """
    def SetDatumTargetType(self,theType : XCAFDimTolObjects_DatumTargetType) -> None: 
        """
        Sets datum target to point, line, rectangle, circle or area type.
        """
    def SetDatumTargetWidth(self,theWidth : float) -> None: 
        """
        Sets datum target width.
        """
    def SetModifierWithValue(self,theModifier : XCAFDimTolObjects_DatumModifWithValue,theValue : float) -> None: 
        """
        Sets datum modifier with value.
        """
    def SetModifiers(self,theModifiers : XCAFDimTolObjects_DatumModifiersSequence) -> None: 
        """
        Sets new sequence of datum modifiers.
        """
    def SetName(self,theTag : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets datum name.
        """
    def SetPlane(self,thePlane : OCP.gp.gp_Ax2) -> None: 
        """
        Sets annotation plane.
        """
    def SetPoint(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets a point on the datum target shape.
        """
    def SetPointTextAttach(self,thePntText : OCP.gp.gp_Pnt) -> None: 
        """
        Sets a position of the datum text.
        """
    def SetPosition(self,thePosition : int) -> None: 
        """
        Sets datum position in the related geometric tolerance object.
        """
    def SetPresentation(self,thePresentation : OCP.TopoDS.TopoDS_Shape,thePresentationName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set graphical presentation for object.
        """
    def SetSemanticName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets semantic name
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theObj : XCAFDimTolObjects_DatumObject) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class XCAFDimTolObjects_DatumObjectSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : XCAFDimTolObjects_DatumObject) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : XCAFDimTolObjects_DatumObjectSequence) -> None: ...
    def Assign(self,theOther : XCAFDimTolObjects_DatumObjectSequence) -> XCAFDimTolObjects_DatumObjectSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> XCAFDimTolObjects_DatumObject: 
        """
        First item access
        """
    def ChangeLast(self) -> XCAFDimTolObjects_DatumObject: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> XCAFDimTolObjects_DatumObject: 
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
    def First(self) -> XCAFDimTolObjects_DatumObject: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : XCAFDimTolObjects_DatumObjectSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : XCAFDimTolObjects_DatumObject) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_DatumObject) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_DatumObjectSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> XCAFDimTolObjects_DatumObject: 
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
    def Prepend(self,theSeq : XCAFDimTolObjects_DatumObjectSequence) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : XCAFDimTolObjects_DatumObject) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : XCAFDimTolObjects_DatumObject) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : XCAFDimTolObjects_DatumObjectSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> XCAFDimTolObjects_DatumObject: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_DatumObjectSequence) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class XCAFDimTolObjects_DatumSingleModif():
    """
    Defines modifirs

    Members:

      XCAFDimTolObjects_DatumSingleModif_AnyCrossSection

      XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection

      XCAFDimTolObjects_DatumSingleModif_Basic

      XCAFDimTolObjects_DatumSingleModif_ContactingFeature

      XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU

      XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV

      XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW

      XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX

      XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY

      XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ

      XCAFDimTolObjects_DatumSingleModif_DistanceVariable

      XCAFDimTolObjects_DatumSingleModif_FreeState

      XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement

      XCAFDimTolObjects_DatumSingleModif_Line

      XCAFDimTolObjects_DatumSingleModif_MajorDiameter

      XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement

      XCAFDimTolObjects_DatumSingleModif_MinorDiameter

      XCAFDimTolObjects_DatumSingleModif_Orientation

      XCAFDimTolObjects_DatumSingleModif_PitchDiameter

      XCAFDimTolObjects_DatumSingleModif_Plane

      XCAFDimTolObjects_DatumSingleModif_Point

      XCAFDimTolObjects_DatumSingleModif_Translation
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_DatumSingleModif_AnyCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_AnyCrossSection
    XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection
    XCAFDimTolObjects_DatumSingleModif_Basic: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Basic
    XCAFDimTolObjects_DatumSingleModif_ContactingFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_ContactingFeature
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ
    XCAFDimTolObjects_DatumSingleModif_DistanceVariable: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DistanceVariable
    XCAFDimTolObjects_DatumSingleModif_FreeState: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_FreeState
    XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement
    XCAFDimTolObjects_DatumSingleModif_Line: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Line
    XCAFDimTolObjects_DatumSingleModif_MajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MajorDiameter
    XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement
    XCAFDimTolObjects_DatumSingleModif_MinorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MinorDiameter
    XCAFDimTolObjects_DatumSingleModif_Orientation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Orientation
    XCAFDimTolObjects_DatumSingleModif_PitchDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_PitchDiameter
    XCAFDimTolObjects_DatumSingleModif_Plane: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Plane
    XCAFDimTolObjects_DatumSingleModif_Point: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Point
    XCAFDimTolObjects_DatumSingleModif_Translation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Translation
    __entries: dict # value = {'XCAFDimTolObjects_DatumSingleModif_AnyCrossSection': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_AnyCrossSection, None), 'XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection, None), 'XCAFDimTolObjects_DatumSingleModif_Basic': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Basic, None), 'XCAFDimTolObjects_DatumSingleModif_ContactingFeature': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_ContactingFeature, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ, None), 'XCAFDimTolObjects_DatumSingleModif_DistanceVariable': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DistanceVariable, None), 'XCAFDimTolObjects_DatumSingleModif_FreeState': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_FreeState, None), 'XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement, None), 'XCAFDimTolObjects_DatumSingleModif_Line': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Line, None), 'XCAFDimTolObjects_DatumSingleModif_MajorDiameter': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MajorDiameter, None), 'XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement, None), 'XCAFDimTolObjects_DatumSingleModif_MinorDiameter': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MinorDiameter, None), 'XCAFDimTolObjects_DatumSingleModif_Orientation': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Orientation, None), 'XCAFDimTolObjects_DatumSingleModif_PitchDiameter': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_PitchDiameter, None), 'XCAFDimTolObjects_DatumSingleModif_Plane': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Plane, None), 'XCAFDimTolObjects_DatumSingleModif_Point': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Point, None), 'XCAFDimTolObjects_DatumSingleModif_Translation': (XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Translation, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DatumSingleModif_AnyCrossSection': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_AnyCrossSection, 'XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection, 'XCAFDimTolObjects_DatumSingleModif_Basic': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Basic, 'XCAFDimTolObjects_DatumSingleModif_ContactingFeature': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_ContactingFeature, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ, 'XCAFDimTolObjects_DatumSingleModif_DistanceVariable': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DistanceVariable, 'XCAFDimTolObjects_DatumSingleModif_FreeState': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_FreeState, 'XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement, 'XCAFDimTolObjects_DatumSingleModif_Line': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Line, 'XCAFDimTolObjects_DatumSingleModif_MajorDiameter': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MajorDiameter, 'XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement, 'XCAFDimTolObjects_DatumSingleModif_MinorDiameter': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MinorDiameter, 'XCAFDimTolObjects_DatumSingleModif_Orientation': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Orientation, 'XCAFDimTolObjects_DatumSingleModif_PitchDiameter': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_PitchDiameter, 'XCAFDimTolObjects_DatumSingleModif_Plane': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Plane, 'XCAFDimTolObjects_DatumSingleModif_Point': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Point, 'XCAFDimTolObjects_DatumSingleModif_Translation': XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Translation}
    pass
class XCAFDimTolObjects_DatumTargetType():
    """
    Defines types of dimension

    Members:

      XCAFDimTolObjects_DatumTargetType_Point

      XCAFDimTolObjects_DatumTargetType_Line

      XCAFDimTolObjects_DatumTargetType_Rectangle

      XCAFDimTolObjects_DatumTargetType_Circle

      XCAFDimTolObjects_DatumTargetType_Area
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_DatumTargetType_Area: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Area
    XCAFDimTolObjects_DatumTargetType_Circle: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Circle
    XCAFDimTolObjects_DatumTargetType_Line: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Line
    XCAFDimTolObjects_DatumTargetType_Point: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Point
    XCAFDimTolObjects_DatumTargetType_Rectangle: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Rectangle
    __entries: dict # value = {'XCAFDimTolObjects_DatumTargetType_Point': (XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Point, None), 'XCAFDimTolObjects_DatumTargetType_Line': (XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Line, None), 'XCAFDimTolObjects_DatumTargetType_Rectangle': (XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Rectangle, None), 'XCAFDimTolObjects_DatumTargetType_Circle': (XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Circle, None), 'XCAFDimTolObjects_DatumTargetType_Area': (XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Area, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DatumTargetType_Point': XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Point, 'XCAFDimTolObjects_DatumTargetType_Line': XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Line, 'XCAFDimTolObjects_DatumTargetType_Rectangle': XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Rectangle, 'XCAFDimTolObjects_DatumTargetType_Circle': XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Circle, 'XCAFDimTolObjects_DatumTargetType_Area': XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Area}
    pass
class XCAFDimTolObjects_DimensionFormVariance():
    """
    Defines value of form variance

    Members:

      XCAFDimTolObjects_DimensionFormVariance_None

      XCAFDimTolObjects_DimensionFormVariance_A

      XCAFDimTolObjects_DimensionFormVariance_B

      XCAFDimTolObjects_DimensionFormVariance_C

      XCAFDimTolObjects_DimensionFormVariance_CD

      XCAFDimTolObjects_DimensionFormVariance_D

      XCAFDimTolObjects_DimensionFormVariance_E

      XCAFDimTolObjects_DimensionFormVariance_EF

      XCAFDimTolObjects_DimensionFormVariance_F

      XCAFDimTolObjects_DimensionFormVariance_FG

      XCAFDimTolObjects_DimensionFormVariance_G

      XCAFDimTolObjects_DimensionFormVariance_H

      XCAFDimTolObjects_DimensionFormVariance_JS

      XCAFDimTolObjects_DimensionFormVariance_J

      XCAFDimTolObjects_DimensionFormVariance_K

      XCAFDimTolObjects_DimensionFormVariance_M

      XCAFDimTolObjects_DimensionFormVariance_N

      XCAFDimTolObjects_DimensionFormVariance_P

      XCAFDimTolObjects_DimensionFormVariance_R

      XCAFDimTolObjects_DimensionFormVariance_S

      XCAFDimTolObjects_DimensionFormVariance_T

      XCAFDimTolObjects_DimensionFormVariance_U

      XCAFDimTolObjects_DimensionFormVariance_V

      XCAFDimTolObjects_DimensionFormVariance_X

      XCAFDimTolObjects_DimensionFormVariance_Y

      XCAFDimTolObjects_DimensionFormVariance_Z

      XCAFDimTolObjects_DimensionFormVariance_ZA

      XCAFDimTolObjects_DimensionFormVariance_ZB

      XCAFDimTolObjects_DimensionFormVariance_ZC
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_DimensionFormVariance_A: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_A
    XCAFDimTolObjects_DimensionFormVariance_B: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_B
    XCAFDimTolObjects_DimensionFormVariance_C: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_C
    XCAFDimTolObjects_DimensionFormVariance_CD: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_CD
    XCAFDimTolObjects_DimensionFormVariance_D: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_D
    XCAFDimTolObjects_DimensionFormVariance_E: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_E
    XCAFDimTolObjects_DimensionFormVariance_EF: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_EF
    XCAFDimTolObjects_DimensionFormVariance_F: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_F
    XCAFDimTolObjects_DimensionFormVariance_FG: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_FG
    XCAFDimTolObjects_DimensionFormVariance_G: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_G
    XCAFDimTolObjects_DimensionFormVariance_H: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_H
    XCAFDimTolObjects_DimensionFormVariance_J: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_J
    XCAFDimTolObjects_DimensionFormVariance_JS: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_JS
    XCAFDimTolObjects_DimensionFormVariance_K: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_K
    XCAFDimTolObjects_DimensionFormVariance_M: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_M
    XCAFDimTolObjects_DimensionFormVariance_N: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_N
    XCAFDimTolObjects_DimensionFormVariance_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_None
    XCAFDimTolObjects_DimensionFormVariance_P: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_P
    XCAFDimTolObjects_DimensionFormVariance_R: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_R
    XCAFDimTolObjects_DimensionFormVariance_S: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_S
    XCAFDimTolObjects_DimensionFormVariance_T: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_T
    XCAFDimTolObjects_DimensionFormVariance_U: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_U
    XCAFDimTolObjects_DimensionFormVariance_V: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_V
    XCAFDimTolObjects_DimensionFormVariance_X: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_X
    XCAFDimTolObjects_DimensionFormVariance_Y: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Y
    XCAFDimTolObjects_DimensionFormVariance_Z: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Z
    XCAFDimTolObjects_DimensionFormVariance_ZA: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZA
    XCAFDimTolObjects_DimensionFormVariance_ZB: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZB
    XCAFDimTolObjects_DimensionFormVariance_ZC: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZC
    __entries: dict # value = {'XCAFDimTolObjects_DimensionFormVariance_None': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_None, None), 'XCAFDimTolObjects_DimensionFormVariance_A': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_A, None), 'XCAFDimTolObjects_DimensionFormVariance_B': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_B, None), 'XCAFDimTolObjects_DimensionFormVariance_C': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_C, None), 'XCAFDimTolObjects_DimensionFormVariance_CD': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_CD, None), 'XCAFDimTolObjects_DimensionFormVariance_D': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_D, None), 'XCAFDimTolObjects_DimensionFormVariance_E': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_E, None), 'XCAFDimTolObjects_DimensionFormVariance_EF': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_EF, None), 'XCAFDimTolObjects_DimensionFormVariance_F': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_F, None), 'XCAFDimTolObjects_DimensionFormVariance_FG': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_FG, None), 'XCAFDimTolObjects_DimensionFormVariance_G': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_G, None), 'XCAFDimTolObjects_DimensionFormVariance_H': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_H, None), 'XCAFDimTolObjects_DimensionFormVariance_JS': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_JS, None), 'XCAFDimTolObjects_DimensionFormVariance_J': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_J, None), 'XCAFDimTolObjects_DimensionFormVariance_K': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_K, None), 'XCAFDimTolObjects_DimensionFormVariance_M': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_M, None), 'XCAFDimTolObjects_DimensionFormVariance_N': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_N, None), 'XCAFDimTolObjects_DimensionFormVariance_P': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_P, None), 'XCAFDimTolObjects_DimensionFormVariance_R': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_R, None), 'XCAFDimTolObjects_DimensionFormVariance_S': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_S, None), 'XCAFDimTolObjects_DimensionFormVariance_T': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_T, None), 'XCAFDimTolObjects_DimensionFormVariance_U': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_U, None), 'XCAFDimTolObjects_DimensionFormVariance_V': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_V, None), 'XCAFDimTolObjects_DimensionFormVariance_X': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_X, None), 'XCAFDimTolObjects_DimensionFormVariance_Y': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Y, None), 'XCAFDimTolObjects_DimensionFormVariance_Z': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Z, None), 'XCAFDimTolObjects_DimensionFormVariance_ZA': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZA, None), 'XCAFDimTolObjects_DimensionFormVariance_ZB': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZB, None), 'XCAFDimTolObjects_DimensionFormVariance_ZC': (XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZC, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionFormVariance_None': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_None, 'XCAFDimTolObjects_DimensionFormVariance_A': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_A, 'XCAFDimTolObjects_DimensionFormVariance_B': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_B, 'XCAFDimTolObjects_DimensionFormVariance_C': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_C, 'XCAFDimTolObjects_DimensionFormVariance_CD': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_CD, 'XCAFDimTolObjects_DimensionFormVariance_D': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_D, 'XCAFDimTolObjects_DimensionFormVariance_E': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_E, 'XCAFDimTolObjects_DimensionFormVariance_EF': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_EF, 'XCAFDimTolObjects_DimensionFormVariance_F': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_F, 'XCAFDimTolObjects_DimensionFormVariance_FG': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_FG, 'XCAFDimTolObjects_DimensionFormVariance_G': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_G, 'XCAFDimTolObjects_DimensionFormVariance_H': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_H, 'XCAFDimTolObjects_DimensionFormVariance_JS': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_JS, 'XCAFDimTolObjects_DimensionFormVariance_J': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_J, 'XCAFDimTolObjects_DimensionFormVariance_K': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_K, 'XCAFDimTolObjects_DimensionFormVariance_M': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_M, 'XCAFDimTolObjects_DimensionFormVariance_N': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_N, 'XCAFDimTolObjects_DimensionFormVariance_P': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_P, 'XCAFDimTolObjects_DimensionFormVariance_R': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_R, 'XCAFDimTolObjects_DimensionFormVariance_S': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_S, 'XCAFDimTolObjects_DimensionFormVariance_T': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_T, 'XCAFDimTolObjects_DimensionFormVariance_U': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_U, 'XCAFDimTolObjects_DimensionFormVariance_V': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_V, 'XCAFDimTolObjects_DimensionFormVariance_X': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_X, 'XCAFDimTolObjects_DimensionFormVariance_Y': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Y, 'XCAFDimTolObjects_DimensionFormVariance_Z': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Z, 'XCAFDimTolObjects_DimensionFormVariance_ZA': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZA, 'XCAFDimTolObjects_DimensionFormVariance_ZB': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZB, 'XCAFDimTolObjects_DimensionFormVariance_ZC': XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZC}
    pass
class XCAFDimTolObjects_DimensionGrade():
    """
    Defines value of grade

    Members:

      XCAFDimTolObjects_DimensionGrade_IT01

      XCAFDimTolObjects_DimensionGrade_IT0

      XCAFDimTolObjects_DimensionGrade_IT1

      XCAFDimTolObjects_DimensionGrade_IT2

      XCAFDimTolObjects_DimensionGrade_IT3

      XCAFDimTolObjects_DimensionGrade_IT4

      XCAFDimTolObjects_DimensionGrade_IT5

      XCAFDimTolObjects_DimensionGrade_IT6

      XCAFDimTolObjects_DimensionGrade_IT7

      XCAFDimTolObjects_DimensionGrade_IT8

      XCAFDimTolObjects_DimensionGrade_IT9

      XCAFDimTolObjects_DimensionGrade_IT10

      XCAFDimTolObjects_DimensionGrade_IT11

      XCAFDimTolObjects_DimensionGrade_IT12

      XCAFDimTolObjects_DimensionGrade_IT13

      XCAFDimTolObjects_DimensionGrade_IT14

      XCAFDimTolObjects_DimensionGrade_IT15

      XCAFDimTolObjects_DimensionGrade_IT16

      XCAFDimTolObjects_DimensionGrade_IT17

      XCAFDimTolObjects_DimensionGrade_IT18
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_DimensionGrade_IT0: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT0
    XCAFDimTolObjects_DimensionGrade_IT01: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT01
    XCAFDimTolObjects_DimensionGrade_IT1: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT1
    XCAFDimTolObjects_DimensionGrade_IT10: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT10
    XCAFDimTolObjects_DimensionGrade_IT11: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT11
    XCAFDimTolObjects_DimensionGrade_IT12: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT12
    XCAFDimTolObjects_DimensionGrade_IT13: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT13
    XCAFDimTolObjects_DimensionGrade_IT14: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT14
    XCAFDimTolObjects_DimensionGrade_IT15: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT15
    XCAFDimTolObjects_DimensionGrade_IT16: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT16
    XCAFDimTolObjects_DimensionGrade_IT17: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT17
    XCAFDimTolObjects_DimensionGrade_IT18: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT18
    XCAFDimTolObjects_DimensionGrade_IT2: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT2
    XCAFDimTolObjects_DimensionGrade_IT3: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT3
    XCAFDimTolObjects_DimensionGrade_IT4: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT4
    XCAFDimTolObjects_DimensionGrade_IT5: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT5
    XCAFDimTolObjects_DimensionGrade_IT6: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT6
    XCAFDimTolObjects_DimensionGrade_IT7: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT7
    XCAFDimTolObjects_DimensionGrade_IT8: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT8
    XCAFDimTolObjects_DimensionGrade_IT9: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT9
    __entries: dict # value = {'XCAFDimTolObjects_DimensionGrade_IT01': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT01, None), 'XCAFDimTolObjects_DimensionGrade_IT0': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT0, None), 'XCAFDimTolObjects_DimensionGrade_IT1': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT1, None), 'XCAFDimTolObjects_DimensionGrade_IT2': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT2, None), 'XCAFDimTolObjects_DimensionGrade_IT3': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT3, None), 'XCAFDimTolObjects_DimensionGrade_IT4': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT4, None), 'XCAFDimTolObjects_DimensionGrade_IT5': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT5, None), 'XCAFDimTolObjects_DimensionGrade_IT6': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT6, None), 'XCAFDimTolObjects_DimensionGrade_IT7': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT7, None), 'XCAFDimTolObjects_DimensionGrade_IT8': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT8, None), 'XCAFDimTolObjects_DimensionGrade_IT9': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT9, None), 'XCAFDimTolObjects_DimensionGrade_IT10': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT10, None), 'XCAFDimTolObjects_DimensionGrade_IT11': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT11, None), 'XCAFDimTolObjects_DimensionGrade_IT12': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT12, None), 'XCAFDimTolObjects_DimensionGrade_IT13': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT13, None), 'XCAFDimTolObjects_DimensionGrade_IT14': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT14, None), 'XCAFDimTolObjects_DimensionGrade_IT15': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT15, None), 'XCAFDimTolObjects_DimensionGrade_IT16': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT16, None), 'XCAFDimTolObjects_DimensionGrade_IT17': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT17, None), 'XCAFDimTolObjects_DimensionGrade_IT18': (XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT18, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionGrade_IT01': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT01, 'XCAFDimTolObjects_DimensionGrade_IT0': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT0, 'XCAFDimTolObjects_DimensionGrade_IT1': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT1, 'XCAFDimTolObjects_DimensionGrade_IT2': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT2, 'XCAFDimTolObjects_DimensionGrade_IT3': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT3, 'XCAFDimTolObjects_DimensionGrade_IT4': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT4, 'XCAFDimTolObjects_DimensionGrade_IT5': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT5, 'XCAFDimTolObjects_DimensionGrade_IT6': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT6, 'XCAFDimTolObjects_DimensionGrade_IT7': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT7, 'XCAFDimTolObjects_DimensionGrade_IT8': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT8, 'XCAFDimTolObjects_DimensionGrade_IT9': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT9, 'XCAFDimTolObjects_DimensionGrade_IT10': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT10, 'XCAFDimTolObjects_DimensionGrade_IT11': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT11, 'XCAFDimTolObjects_DimensionGrade_IT12': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT12, 'XCAFDimTolObjects_DimensionGrade_IT13': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT13, 'XCAFDimTolObjects_DimensionGrade_IT14': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT14, 'XCAFDimTolObjects_DimensionGrade_IT15': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT15, 'XCAFDimTolObjects_DimensionGrade_IT16': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT16, 'XCAFDimTolObjects_DimensionGrade_IT17': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT17, 'XCAFDimTolObjects_DimensionGrade_IT18': XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT18}
    pass
class XCAFDimTolObjects_DimensionModif():
    """
    Defines modifirs

    Members:

      XCAFDimTolObjects_DimensionModif_ControlledRadius

      XCAFDimTolObjects_DimensionModif_Square

      XCAFDimTolObjects_DimensionModif_StatisticalTolerance

      XCAFDimTolObjects_DimensionModif_ContinuousFeature

      XCAFDimTolObjects_DimensionModif_TwoPointSize

      XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere

      XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion

      XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation

      XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation

      XCAFDimTolObjects_DimensionModif_CircumferenceDiameter

      XCAFDimTolObjects_DimensionModif_AreaDiameter

      XCAFDimTolObjects_DimensionModif_VolumeDiameter

      XCAFDimTolObjects_DimensionModif_MaximumSize

      XCAFDimTolObjects_DimensionModif_MinimumSize

      XCAFDimTolObjects_DimensionModif_AverageSize

      XCAFDimTolObjects_DimensionModif_MedianSize

      XCAFDimTolObjects_DimensionModif_MidRangeSize

      XCAFDimTolObjects_DimensionModif_RangeOfSizes

      XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature

      XCAFDimTolObjects_DimensionModif_AnyCrossSection

      XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection

      XCAFDimTolObjects_DimensionModif_CommonTolerance

      XCAFDimTolObjects_DimensionModif_FreeStateCondition

      XCAFDimTolObjects_DimensionModif_Between
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_DimensionModif_AnyCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyCrossSection
    XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature
    XCAFDimTolObjects_DimensionModif_AreaDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AreaDiameter
    XCAFDimTolObjects_DimensionModif_AverageSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AverageSize
    XCAFDimTolObjects_DimensionModif_Between: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Between
    XCAFDimTolObjects_DimensionModif_CircumferenceDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CircumferenceDiameter
    XCAFDimTolObjects_DimensionModif_CommonTolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CommonTolerance
    XCAFDimTolObjects_DimensionModif_ContinuousFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ContinuousFeature
    XCAFDimTolObjects_DimensionModif_ControlledRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ControlledRadius
    XCAFDimTolObjects_DimensionModif_FreeStateCondition: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_FreeStateCondition
    XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion
    XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere
    XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation
    XCAFDimTolObjects_DimensionModif_MaximumSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumSize
    XCAFDimTolObjects_DimensionModif_MedianSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MedianSize
    XCAFDimTolObjects_DimensionModif_MidRangeSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MidRangeSize
    XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation
    XCAFDimTolObjects_DimensionModif_MinimumSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumSize
    XCAFDimTolObjects_DimensionModif_RangeOfSizes: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_RangeOfSizes
    XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection
    XCAFDimTolObjects_DimensionModif_Square: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Square
    XCAFDimTolObjects_DimensionModif_StatisticalTolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_StatisticalTolerance
    XCAFDimTolObjects_DimensionModif_TwoPointSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_TwoPointSize
    XCAFDimTolObjects_DimensionModif_VolumeDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_VolumeDiameter
    __entries: dict # value = {'XCAFDimTolObjects_DimensionModif_ControlledRadius': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ControlledRadius, None), 'XCAFDimTolObjects_DimensionModif_Square': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Square, None), 'XCAFDimTolObjects_DimensionModif_StatisticalTolerance': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_StatisticalTolerance, None), 'XCAFDimTolObjects_DimensionModif_ContinuousFeature': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ContinuousFeature, None), 'XCAFDimTolObjects_DimensionModif_TwoPointSize': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_TwoPointSize, None), 'XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere, None), 'XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion, None), 'XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation, None), 'XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation, None), 'XCAFDimTolObjects_DimensionModif_CircumferenceDiameter': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CircumferenceDiameter, None), 'XCAFDimTolObjects_DimensionModif_AreaDiameter': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AreaDiameter, None), 'XCAFDimTolObjects_DimensionModif_VolumeDiameter': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_VolumeDiameter, None), 'XCAFDimTolObjects_DimensionModif_MaximumSize': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumSize, None), 'XCAFDimTolObjects_DimensionModif_MinimumSize': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumSize, None), 'XCAFDimTolObjects_DimensionModif_AverageSize': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AverageSize, None), 'XCAFDimTolObjects_DimensionModif_MedianSize': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MedianSize, None), 'XCAFDimTolObjects_DimensionModif_MidRangeSize': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MidRangeSize, None), 'XCAFDimTolObjects_DimensionModif_RangeOfSizes': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_RangeOfSizes, None), 'XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature, None), 'XCAFDimTolObjects_DimensionModif_AnyCrossSection': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyCrossSection, None), 'XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection, None), 'XCAFDimTolObjects_DimensionModif_CommonTolerance': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CommonTolerance, None), 'XCAFDimTolObjects_DimensionModif_FreeStateCondition': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_FreeStateCondition, None), 'XCAFDimTolObjects_DimensionModif_Between': (XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Between, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionModif_ControlledRadius': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ControlledRadius, 'XCAFDimTolObjects_DimensionModif_Square': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Square, 'XCAFDimTolObjects_DimensionModif_StatisticalTolerance': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_StatisticalTolerance, 'XCAFDimTolObjects_DimensionModif_ContinuousFeature': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ContinuousFeature, 'XCAFDimTolObjects_DimensionModif_TwoPointSize': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_TwoPointSize, 'XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere, 'XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion, 'XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation, 'XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation, 'XCAFDimTolObjects_DimensionModif_CircumferenceDiameter': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CircumferenceDiameter, 'XCAFDimTolObjects_DimensionModif_AreaDiameter': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AreaDiameter, 'XCAFDimTolObjects_DimensionModif_VolumeDiameter': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_VolumeDiameter, 'XCAFDimTolObjects_DimensionModif_MaximumSize': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumSize, 'XCAFDimTolObjects_DimensionModif_MinimumSize': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumSize, 'XCAFDimTolObjects_DimensionModif_AverageSize': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AverageSize, 'XCAFDimTolObjects_DimensionModif_MedianSize': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MedianSize, 'XCAFDimTolObjects_DimensionModif_MidRangeSize': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MidRangeSize, 'XCAFDimTolObjects_DimensionModif_RangeOfSizes': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_RangeOfSizes, 'XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature, 'XCAFDimTolObjects_DimensionModif_AnyCrossSection': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyCrossSection, 'XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection, 'XCAFDimTolObjects_DimensionModif_CommonTolerance': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CommonTolerance, 'XCAFDimTolObjects_DimensionModif_FreeStateCondition': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_FreeStateCondition, 'XCAFDimTolObjects_DimensionModif_Between': XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Between}
    pass
class XCAFDimTolObjects_DimensionModifiersSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : XCAFDimTolObjects_DimensionModif) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : XCAFDimTolObjects_DimensionModifiersSequence) -> None: ...
    def Assign(self,theOther : XCAFDimTolObjects_DimensionModifiersSequence) -> XCAFDimTolObjects_DimensionModifiersSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> XCAFDimTolObjects_DimensionModif: 
        """
        First item access
        """
    def ChangeLast(self) -> XCAFDimTolObjects_DimensionModif: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> XCAFDimTolObjects_DimensionModif: 
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
    def First(self) -> XCAFDimTolObjects_DimensionModif: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : XCAFDimTolObjects_DimensionModif) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : XCAFDimTolObjects_DimensionModifiersSequence) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_DimensionModifiersSequence) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_DimensionModif) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> XCAFDimTolObjects_DimensionModif: 
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
    def Prepend(self,theItem : XCAFDimTolObjects_DimensionModif) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : XCAFDimTolObjects_DimensionModifiersSequence) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : XCAFDimTolObjects_DimensionModif) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : XCAFDimTolObjects_DimensionModifiersSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> XCAFDimTolObjects_DimensionModif: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_DimensionModifiersSequence) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class XCAFDimTolObjects_DimensionObject(OCP.Standard.Standard_Transient):
    """
    Access object to store dimension dataAccess object to store dimension dataAccess object to store dimension data
    """
    def AddDescription(self,theDescription : OCP.TCollection.TCollection_HAsciiString,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Add new description.
        """
    def AddModifier(self,theModifier : XCAFDimTolObjects_DimensionModif) -> None: 
        """
        Adds a modifier to the dimension sequence of modifiers.
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
    def GetClassOfTolerance(self,theHole : bool,theFormVariance : XCAFDimTolObjects_DimensionFormVariance,theGrade : XCAFDimTolObjects_DimensionGrade) -> bool: 
        """
        Retrieves tolerance class parameters of the dimension. Returns True if the dimension is toleranced.
        """
    def GetDescription(self,theNumber : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns description with the given number.
        """
    def GetDescriptionName(self,theNumber : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns name of description with the given number.
        """
    def GetDirection(self,theDir : OCP.gp.gp_Dir) -> bool: 
        """
        Returns the orientation of the dimension in annotation plane.
        """
    def GetLowerBound(self) -> float: 
        """
        Returns the lower bound of the range dimension, otherwise - zero.
        """
    def GetLowerTolValue(self) -> float: 
        """
        Returns the upper value of the toleranced dimension, otherwise - zero.
        """
    def GetModifiers(self) -> XCAFDimTolObjects_DimensionModifiersSequence: 
        """
        Returns a sequence of modifiers of the dimension.
        """
    def GetNbOfDecimalPlaces(self) -> Tuple[int, int]: 
        """
        Returns the number of places to the left and right of the decimal point respectively.
        """
    def GetPath(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns a 'curve' along which the dimension is measured.
        """
    def GetPlane(self) -> OCP.gp.gp_Ax2: 
        """
        Returns annotation plane.
        """
    def GetPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Get connection point (for dimesional_size), Get connection point for the first shape (for dimensional_location).
        """
    def GetPoint2(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def GetPointTextAttach(self) -> OCP.gp.gp_Pnt: 
        """
        Returns position of the dimension text.
        """
    def GetPresentation(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns graphical presentation of the object.
        """
    def GetPresentationName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns graphical presentation of the object
        """
    def GetQualifier(self) -> XCAFDimTolObjects_DimensionQualifier: 
        """
        Returns dimension qualifier.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSemanticName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns semantic name
        """
    def GetType(self) -> XCAFDimTolObjects_DimensionType: 
        """
        Returns dimension type.
        """
    def GetUpperBound(self) -> float: 
        """
        Returns the upper bound of the range dimension, otherwise - zero.
        """
    def GetUpperTolValue(self) -> float: 
        """
        Returns the lower value of the toleranced dimension, otherwise - zero.
        """
    def GetValue(self) -> float: 
        """
        Returns the main dimension value. It will be the middle value in case of range dimension.
        """
    def GetValues(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns raw array of dimension values
        """
    def HasDescriptions(self) -> bool: 
        """
        Returns true, if the object has descriptions.
        """
    def HasPlane(self) -> bool: 
        """
        Returns True if the object has annotation plane.
        """
    def HasPoint(self) -> bool: 
        """
        Returns true, if connection point exists (for dimesional_size), if connection point for the first shape exists (for dimensional_location).
        """
    def HasPoint2(self) -> bool: 
        """
        None
        """
    def HasQualifier(self) -> bool: 
        """
        Returns True if the object has dimension qualifier.
        """
    def HasTextPoint(self) -> bool: 
        """
        Returns True if the position of dimension text is specified.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDimWithClassOfTolerance(self) -> bool: 
        """
        Returns True if the form variance was set to not XCAFDimTolObjects_DimensionFormVariance_None value.
        """
    def IsDimWithPlusMinusTolerance(self) -> bool: 
        """
        Returns True if the dimension is of +/- tolerance kind. Dimension is of +/- tolerance kind if its values array contains three elements defining the main value and the lower/upper tolerances.
        """
    def IsDimWithRange(self) -> bool: 
        """
        Returns True if the dimension is of range kind. Dimension is of range kind if its values array contains two elements defining lower and upper bounds.
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
    def NbDescriptions(self) -> int: 
        """
        Returns number of descriptions.
        """
    def RemoveDescription(self,theNumber : int) -> None: 
        """
        Remove description with the given number.
        """
    def SetClassOfTolerance(self,theHole : bool,theFormVariance : XCAFDimTolObjects_DimensionFormVariance,theGrade : XCAFDimTolObjects_DimensionGrade) -> None: 
        """
        Sets tolerance class of the dimension.
        """
    def SetDirection(self,theDir : OCP.gp.gp_Dir) -> bool: 
        """
        Sets an orientation of the dimension in annotation plane.
        """
    def SetLowerBound(self,theLowerBound : float) -> None: 
        """
        Sets the lower bound of the range dimension, otherwise resets it to an empty range with the specified lower bound.
        """
    def SetLowerTolValue(self,theLowerTolValue : float) -> bool: 
        """
        Sets the lower value of the toleranced dimension, otherwise resets a simple dimension to toleranced one with the specified lower/upper tolerances. Returns False in case of range dimension.
        """
    def SetModifiers(self,theModifiers : XCAFDimTolObjects_DimensionModifiersSequence) -> None: 
        """
        Sets new sequence of dimension modifiers.
        """
    def SetNbOfDecimalPlaces(self,theL : int,theR : int) -> None: 
        """
        Sets the number of places to the left and right of the decimal point respectively.
        """
    def SetPath(self,thePath : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Sets a 'curve' along which the dimension is measured.
        """
    def SetPlane(self,thePlane : OCP.gp.gp_Ax2) -> None: 
        """
        Sets annotation plane.
        """
    def SetPoint(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Set connection point (for dimesional_size), Set connection point for the first shape (for dimensional_location).
        """
    def SetPoint2(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def SetPointTextAttach(self,thePntText : OCP.gp.gp_Pnt) -> None: 
        """
        Sets position of the dimension text.
        """
    def SetPresentation(self,thePresentation : OCP.TopoDS.TopoDS_Shape,thePresentationName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set graphical presentation for the object.
        """
    def SetQualifier(self,theQualifier : XCAFDimTolObjects_DimensionQualifier) -> None: 
        """
        Sets dimension qualifier as min., max. or average.
        """
    def SetSemanticName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets semantic name
        """
    def SetType(self,theTyupe : XCAFDimTolObjects_DimensionType) -> None: 
        """
        Sets a specific type of dimension.
        """
    def SetUpperBound(self,theUpperBound : float) -> None: 
        """
        Sets the upper bound of the range dimension, otherwise resets it to an empty range with the specified upper bound.
        """
    def SetUpperTolValue(self,theUperTolValue : float) -> bool: 
        """
        Sets the upper value of the toleranced dimension, otherwise resets a simple dimension to toleranced one with the specified lower/upper tolerances. Returns False in case of range dimension.
        """
    def SetValue(self,theValue : float) -> None: 
        """
        Sets the main dimension value. Overwrites previous values.
        """
    def SetValues(self,theValue : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Replaces current raw array of dimension values with theValues array.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theObj : XCAFDimTolObjects_DimensionObject) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class XCAFDimTolObjects_DimensionObjectSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : XCAFDimTolObjects_DimensionObject) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : XCAFDimTolObjects_DimensionObjectSequence) -> None: ...
    def Assign(self,theOther : XCAFDimTolObjects_DimensionObjectSequence) -> XCAFDimTolObjects_DimensionObjectSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> XCAFDimTolObjects_DimensionObject: 
        """
        First item access
        """
    def ChangeLast(self) -> XCAFDimTolObjects_DimensionObject: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> XCAFDimTolObjects_DimensionObject: 
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
    def First(self) -> XCAFDimTolObjects_DimensionObject: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : XCAFDimTolObjects_DimensionObjectSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : XCAFDimTolObjects_DimensionObject) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_DimensionObject) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_DimensionObjectSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> XCAFDimTolObjects_DimensionObject: 
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
    def Prepend(self,theItem : XCAFDimTolObjects_DimensionObject) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : XCAFDimTolObjects_DimensionObjectSequence) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : XCAFDimTolObjects_DimensionObject) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : XCAFDimTolObjects_DimensionObjectSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> XCAFDimTolObjects_DimensionObject: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_DimensionObjectSequence) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class XCAFDimTolObjects_DimensionQualifier():
    """
    Defines types of qualifier

    Members:

      XCAFDimTolObjects_DimensionQualifier_None

      XCAFDimTolObjects_DimensionQualifier_Min

      XCAFDimTolObjects_DimensionQualifier_Max

      XCAFDimTolObjects_DimensionQualifier_Avg
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_DimensionQualifier_Avg: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Avg
    XCAFDimTolObjects_DimensionQualifier_Max: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Max
    XCAFDimTolObjects_DimensionQualifier_Min: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Min
    XCAFDimTolObjects_DimensionQualifier_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_None
    __entries: dict # value = {'XCAFDimTolObjects_DimensionQualifier_None': (XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_None, None), 'XCAFDimTolObjects_DimensionQualifier_Min': (XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Min, None), 'XCAFDimTolObjects_DimensionQualifier_Max': (XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Max, None), 'XCAFDimTolObjects_DimensionQualifier_Avg': (XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Avg, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionQualifier_None': XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_None, 'XCAFDimTolObjects_DimensionQualifier_Min': XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Min, 'XCAFDimTolObjects_DimensionQualifier_Max': XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Max, 'XCAFDimTolObjects_DimensionQualifier_Avg': XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Avg}
    pass
class XCAFDimTolObjects_DimensionType():
    """
    Defines types of dimension

    Members:

      XCAFDimTolObjects_DimensionType_Location_None

      XCAFDimTolObjects_DimensionType_Location_CurvedDistance

      XCAFDimTolObjects_DimensionType_Location_LinearDistance

      XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter

      XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner

      XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter

      XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter

      XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner

      XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter

      XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter

      XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner

      XCAFDimTolObjects_DimensionType_Location_Angular

      XCAFDimTolObjects_DimensionType_Location_Oriented

      XCAFDimTolObjects_DimensionType_Location_WithPath

      XCAFDimTolObjects_DimensionType_Size_CurveLength

      XCAFDimTolObjects_DimensionType_Size_Diameter

      XCAFDimTolObjects_DimensionType_Size_SphericalDiameter

      XCAFDimTolObjects_DimensionType_Size_Radius

      XCAFDimTolObjects_DimensionType_Size_SphericalRadius

      XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter

      XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter

      XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius

      XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius

      XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter

      XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter

      XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius

      XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius

      XCAFDimTolObjects_DimensionType_Size_Thickness

      XCAFDimTolObjects_DimensionType_Size_Angular

      XCAFDimTolObjects_DimensionType_Size_WithPath

      XCAFDimTolObjects_DimensionType_CommonLabel

      XCAFDimTolObjects_DimensionType_DimensionPresentation
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_DimensionType_CommonLabel: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_CommonLabel
    XCAFDimTolObjects_DimensionType_DimensionPresentation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_DimensionPresentation
    XCAFDimTolObjects_DimensionType_Location_Angular: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Angular
    XCAFDimTolObjects_DimensionType_Location_CurvedDistance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_CurvedDistance
    XCAFDimTolObjects_DimensionType_Location_LinearDistance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter
    XCAFDimTolObjects_DimensionType_Location_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_None
    XCAFDimTolObjects_DimensionType_Location_Oriented: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Oriented
    XCAFDimTolObjects_DimensionType_Location_WithPath: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_WithPath
    XCAFDimTolObjects_DimensionType_Size_Angular: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Angular
    XCAFDimTolObjects_DimensionType_Size_CurveLength: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_CurveLength
    XCAFDimTolObjects_DimensionType_Size_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter
    XCAFDimTolObjects_DimensionType_Size_Radius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Radius
    XCAFDimTolObjects_DimensionType_Size_SphericalDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalDiameter
    XCAFDimTolObjects_DimensionType_Size_SphericalRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalRadius
    XCAFDimTolObjects_DimensionType_Size_Thickness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Thickness
    XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter
    XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius
    XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter
    XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius
    XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter
    XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius
    XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter
    XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius
    XCAFDimTolObjects_DimensionType_Size_WithPath: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_WithPath
    __entries: dict # value = {'XCAFDimTolObjects_DimensionType_Location_None': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_None, None), 'XCAFDimTolObjects_DimensionType_Location_CurvedDistance': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_CurvedDistance, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner, None), 'XCAFDimTolObjects_DimensionType_Location_Angular': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Angular, None), 'XCAFDimTolObjects_DimensionType_Location_Oriented': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Oriented, None), 'XCAFDimTolObjects_DimensionType_Location_WithPath': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_WithPath, None), 'XCAFDimTolObjects_DimensionType_Size_CurveLength': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_CurveLength, None), 'XCAFDimTolObjects_DimensionType_Size_Diameter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter, None), 'XCAFDimTolObjects_DimensionType_Size_SphericalDiameter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalDiameter, None), 'XCAFDimTolObjects_DimensionType_Size_Radius': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Radius, None), 'XCAFDimTolObjects_DimensionType_Size_SphericalRadius': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalRadius, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius, None), 'XCAFDimTolObjects_DimensionType_Size_Thickness': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Thickness, None), 'XCAFDimTolObjects_DimensionType_Size_Angular': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Angular, None), 'XCAFDimTolObjects_DimensionType_Size_WithPath': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_WithPath, None), 'XCAFDimTolObjects_DimensionType_CommonLabel': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_CommonLabel, None), 'XCAFDimTolObjects_DimensionType_DimensionPresentation': (XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_DimensionPresentation, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionType_Location_None': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_None, 'XCAFDimTolObjects_DimensionType_Location_CurvedDistance': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_CurvedDistance, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner, 'XCAFDimTolObjects_DimensionType_Location_Angular': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Angular, 'XCAFDimTolObjects_DimensionType_Location_Oriented': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Oriented, 'XCAFDimTolObjects_DimensionType_Location_WithPath': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_WithPath, 'XCAFDimTolObjects_DimensionType_Size_CurveLength': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_CurveLength, 'XCAFDimTolObjects_DimensionType_Size_Diameter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter, 'XCAFDimTolObjects_DimensionType_Size_SphericalDiameter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalDiameter, 'XCAFDimTolObjects_DimensionType_Size_Radius': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Radius, 'XCAFDimTolObjects_DimensionType_Size_SphericalRadius': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalRadius, 'XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter, 'XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter, 'XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius, 'XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius, 'XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter, 'XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter, 'XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius, 'XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius, 'XCAFDimTolObjects_DimensionType_Size_Thickness': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Thickness, 'XCAFDimTolObjects_DimensionType_Size_Angular': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Angular, 'XCAFDimTolObjects_DimensionType_Size_WithPath': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_WithPath, 'XCAFDimTolObjects_DimensionType_CommonLabel': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_CommonLabel, 'XCAFDimTolObjects_DimensionType_DimensionPresentation': XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_DimensionPresentation}
    pass
class XCAFDimTolObjects_GeomToleranceMatReqModif():
    """
    Defines types of material requirement

    Members:

      XCAFDimTolObjects_GeomToleranceMatReqModif_None

      XCAFDimTolObjects_GeomToleranceMatReqModif_M

      XCAFDimTolObjects_GeomToleranceMatReqModif_L
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_GeomToleranceMatReqModif_L: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_L
    XCAFDimTolObjects_GeomToleranceMatReqModif_M: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_M
    XCAFDimTolObjects_GeomToleranceMatReqModif_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_None
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceMatReqModif_None': (XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_None, None), 'XCAFDimTolObjects_GeomToleranceMatReqModif_M': (XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_M, None), 'XCAFDimTolObjects_GeomToleranceMatReqModif_L': (XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_L, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceMatReqModif_None': XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_None, 'XCAFDimTolObjects_GeomToleranceMatReqModif_M': XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_M, 'XCAFDimTolObjects_GeomToleranceMatReqModif_L': XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_L}
    pass
class XCAFDimTolObjects_GeomToleranceModif():
    """
    Defines modifirs

    Members:

      XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section

      XCAFDimTolObjects_GeomToleranceModif_Common_Zone

      XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element

      XCAFDimTolObjects_GeomToleranceModif_Free_State

      XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement

      XCAFDimTolObjects_GeomToleranceModif_Line_Element

      XCAFDimTolObjects_GeomToleranceModif_Major_Diameter

      XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement

      XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter

      XCAFDimTolObjects_GeomToleranceModif_Not_Convex

      XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter

      XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement

      XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement

      XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance

      XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane

      XCAFDimTolObjects_GeomToleranceModif_All_Around

      XCAFDimTolObjects_GeomToleranceModif_All_Over
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_GeomToleranceModif_All_Around: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Around
    XCAFDimTolObjects_GeomToleranceModif_All_Over: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Over
    XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section
    XCAFDimTolObjects_GeomToleranceModif_Common_Zone: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Common_Zone
    XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element
    XCAFDimTolObjects_GeomToleranceModif_Free_State: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Free_State
    XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement
    XCAFDimTolObjects_GeomToleranceModif_Line_Element: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Line_Element
    XCAFDimTolObjects_GeomToleranceModif_Major_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Major_Diameter
    XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement
    XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter
    XCAFDimTolObjects_GeomToleranceModif_Not_Convex: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Not_Convex
    XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter
    XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement
    XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement
    XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance
    XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section, None), 'XCAFDimTolObjects_GeomToleranceModif_Common_Zone': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Common_Zone, None), 'XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element, None), 'XCAFDimTolObjects_GeomToleranceModif_Free_State': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Free_State, None), 'XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement, None), 'XCAFDimTolObjects_GeomToleranceModif_Line_Element': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Line_Element, None), 'XCAFDimTolObjects_GeomToleranceModif_Major_Diameter': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Major_Diameter, None), 'XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement, None), 'XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter, None), 'XCAFDimTolObjects_GeomToleranceModif_Not_Convex': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Not_Convex, None), 'XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter, None), 'XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement, None), 'XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement, None), 'XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance, None), 'XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane, None), 'XCAFDimTolObjects_GeomToleranceModif_All_Around': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Around, None), 'XCAFDimTolObjects_GeomToleranceModif_All_Over': (XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Over, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section, 'XCAFDimTolObjects_GeomToleranceModif_Common_Zone': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Common_Zone, 'XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element, 'XCAFDimTolObjects_GeomToleranceModif_Free_State': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Free_State, 'XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement, 'XCAFDimTolObjects_GeomToleranceModif_Line_Element': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Line_Element, 'XCAFDimTolObjects_GeomToleranceModif_Major_Diameter': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Major_Diameter, 'XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement, 'XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter, 'XCAFDimTolObjects_GeomToleranceModif_Not_Convex': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Not_Convex, 'XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter, 'XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement, 'XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement, 'XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance, 'XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane, 'XCAFDimTolObjects_GeomToleranceModif_All_Around': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Around, 'XCAFDimTolObjects_GeomToleranceModif_All_Over': XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Over}
    pass
class XCAFDimTolObjects_GeomToleranceModifiersSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : XCAFDimTolObjects_GeomToleranceModif) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: ...
    def Assign(self,theOther : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> XCAFDimTolObjects_GeomToleranceModifiersSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> XCAFDimTolObjects_GeomToleranceModif: 
        """
        First item access
        """
    def ChangeLast(self) -> XCAFDimTolObjects_GeomToleranceModif: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> XCAFDimTolObjects_GeomToleranceModif: 
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
    def First(self) -> XCAFDimTolObjects_GeomToleranceModif: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : XCAFDimTolObjects_GeomToleranceModif) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_GeomToleranceModif) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> XCAFDimTolObjects_GeomToleranceModif: 
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
    def Prepend(self,theItem : XCAFDimTolObjects_GeomToleranceModif) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : XCAFDimTolObjects_GeomToleranceModif) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> XCAFDimTolObjects_GeomToleranceModif: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class XCAFDimTolObjects_GeomToleranceObject(OCP.Standard.Standard_Transient):
    """
    Access object to store dimension and toleranceAccess object to store dimension and toleranceAccess object to store dimension and tolerance
    """
    def AddModifier(self,theModifier : XCAFDimTolObjects_GeomToleranceModif) -> None: 
        """
        Adds a tolerance modifier to the sequence of modifiers.
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
    def GetAffectedPlane(self) -> OCP.gp.gp_Pln: 
        """
        Returns affected plane.
        """
    def GetAffectedPlaneType(self) -> XCAFDimTolObjects_ToleranceZoneAffectedPlane: 
        """
        None
        """
    def GetAxis(self) -> OCP.gp.gp_Ax2: 
        """
        None
        """
    def GetMaterialRequirementModifier(self) -> XCAFDimTolObjects_GeomToleranceMatReqModif: 
        """
        Returns material requirement of the tolerance.
        """
    def GetMaxValueModifier(self) -> float: 
        """
        Returns the maximal upper tolerance.
        """
    def GetModifiers(self) -> XCAFDimTolObjects_GeomToleranceModifiersSequence: 
        """
        Returns a sequence of modifiers of the tolerance.
        """
    def GetPlane(self) -> OCP.gp.gp_Ax2: 
        """
        Returns annotation plane.
        """
    def GetPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns reference point.
        """
    def GetPointTextAttach(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the text position.
        """
    def GetPresentation(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns graphical presentation of the object.
        """
    def GetPresentationName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns graphical presentation of the object.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSemanticName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns semantic name
        """
    def GetType(self) -> XCAFDimTolObjects_GeomToleranceType: 
        """
        Returns type of the object.
        """
    def GetTypeOfValue(self) -> XCAFDimTolObjects_GeomToleranceTypeValue: 
        """
        Returns type of tolerance value.
        """
    def GetValue(self) -> float: 
        """
        Returns tolerance value.
        """
    def GetValueOfZoneModifier(self) -> float: 
        """
        Returns value associated with tolerance zone.
        """
    def GetZoneModifier(self) -> XCAFDimTolObjects_GeomToleranceZoneModif: 
        """
        Returns tolerance zone.
        """
    def HasAffectedPlane(self) -> bool: 
        """
        None
        """
    def HasAxis(self) -> bool: 
        """
        None
        """
    def HasPlane(self) -> bool: 
        """
        Returns True if the object has annotation plane.
        """
    def HasPoint(self) -> bool: 
        """
        Returns True if reference point is specified.
        """
    def HasPointText(self) -> bool: 
        """
        Returns True if text position is specified.
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
    @overload
    def SetAffectedPlane(self,thePlane : OCP.gp.gp_Pln) -> None: 
        """
        Sets affected plane.

        Sets affected plane.
        """
    @overload
    def SetAffectedPlane(self,thePlane : OCP.gp.gp_Pln,theType : XCAFDimTolObjects_ToleranceZoneAffectedPlane) -> None: ...
    def SetAffectedPlaneType(self,theType : XCAFDimTolObjects_ToleranceZoneAffectedPlane) -> None: 
        """
        None
        """
    def SetAxis(self,theAxis : OCP.gp.gp_Ax2) -> None: 
        """
        None
        """
    def SetMaterialRequirementModifier(self,theMatReqModif : XCAFDimTolObjects_GeomToleranceMatReqModif) -> None: 
        """
        Sets material requirement of the tolerance.
        """
    def SetMaxValueModifier(self,theModifier : float) -> None: 
        """
        Sets the maximal upper tolerance value for tolerance with modifiers.
        """
    def SetModifiers(self,theModifiers : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: 
        """
        Sets new sequence of tolerance modifiers.
        """
    def SetPlane(self,thePlane : OCP.gp.gp_Ax2) -> None: 
        """
        Sets annotation plane.
        """
    def SetPoint(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets reference point.
        """
    def SetPointTextAttach(self,thePntText : OCP.gp.gp_Pnt) -> None: 
        """
        Sets text position.
        """
    def SetPresentation(self,thePresentation : OCP.TopoDS.TopoDS_Shape,thePresentationName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set graphical presentation for object.
        """
    def SetSemanticName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Sets semantic name
        """
    def SetType(self,theType : XCAFDimTolObjects_GeomToleranceType) -> None: 
        """
        Sets type of the object.
        """
    def SetTypeOfValue(self,theTypeOfValue : XCAFDimTolObjects_GeomToleranceTypeValue) -> None: 
        """
        Sets type of tolerance value.
        """
    def SetValue(self,theValue : float) -> None: 
        """
        Sets tolerance value.
        """
    def SetValueOfZoneModifier(self,theValue : float) -> None: 
        """
        Sets value associated with tolerance zone.
        """
    def SetZoneModifier(self,theZoneModif : XCAFDimTolObjects_GeomToleranceZoneModif) -> None: 
        """
        Sets tolerance zone.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theObj : XCAFDimTolObjects_GeomToleranceObject) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class XCAFDimTolObjects_GeomToleranceObjectSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : XCAFDimTolObjects_GeomToleranceObject) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: ...
    def Assign(self,theOther : XCAFDimTolObjects_GeomToleranceObjectSequence) -> XCAFDimTolObjects_GeomToleranceObjectSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> XCAFDimTolObjects_GeomToleranceObject: 
        """
        First item access
        """
    def ChangeLast(self) -> XCAFDimTolObjects_GeomToleranceObject: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> XCAFDimTolObjects_GeomToleranceObject: 
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
    def First(self) -> XCAFDimTolObjects_GeomToleranceObject: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : XCAFDimTolObjects_GeomToleranceObject) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_GeomToleranceObject) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> XCAFDimTolObjects_GeomToleranceObject: 
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
    def Prepend(self,theItem : XCAFDimTolObjects_GeomToleranceObject) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : XCAFDimTolObjects_GeomToleranceObject) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> XCAFDimTolObjects_GeomToleranceObject: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class XCAFDimTolObjects_GeomToleranceType():
    """
    Defines types of geom tolerance

    Members:

      XCAFDimTolObjects_GeomToleranceType_None

      XCAFDimTolObjects_GeomToleranceType_Angularity

      XCAFDimTolObjects_GeomToleranceType_CircularRunout

      XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness

      XCAFDimTolObjects_GeomToleranceType_Coaxiality

      XCAFDimTolObjects_GeomToleranceType_Concentricity

      XCAFDimTolObjects_GeomToleranceType_Cylindricity

      XCAFDimTolObjects_GeomToleranceType_Flatness

      XCAFDimTolObjects_GeomToleranceType_Parallelism

      XCAFDimTolObjects_GeomToleranceType_Perpendicularity

      XCAFDimTolObjects_GeomToleranceType_Position

      XCAFDimTolObjects_GeomToleranceType_ProfileOfLine

      XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface

      XCAFDimTolObjects_GeomToleranceType_Straightness

      XCAFDimTolObjects_GeomToleranceType_Symmetry

      XCAFDimTolObjects_GeomToleranceType_TotalRunout
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_GeomToleranceType_Angularity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Angularity
    XCAFDimTolObjects_GeomToleranceType_CircularRunout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularRunout
    XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness
    XCAFDimTolObjects_GeomToleranceType_Coaxiality: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Coaxiality
    XCAFDimTolObjects_GeomToleranceType_Concentricity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Concentricity
    XCAFDimTolObjects_GeomToleranceType_Cylindricity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity
    XCAFDimTolObjects_GeomToleranceType_Flatness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Flatness
    XCAFDimTolObjects_GeomToleranceType_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_None
    XCAFDimTolObjects_GeomToleranceType_Parallelism: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Parallelism
    XCAFDimTolObjects_GeomToleranceType_Perpendicularity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Perpendicularity
    XCAFDimTolObjects_GeomToleranceType_Position: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Position
    XCAFDimTolObjects_GeomToleranceType_ProfileOfLine: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfLine
    XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface
    XCAFDimTolObjects_GeomToleranceType_Straightness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Straightness
    XCAFDimTolObjects_GeomToleranceType_Symmetry: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Symmetry
    XCAFDimTolObjects_GeomToleranceType_TotalRunout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_TotalRunout
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceType_None': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_None, None), 'XCAFDimTolObjects_GeomToleranceType_Angularity': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Angularity, None), 'XCAFDimTolObjects_GeomToleranceType_CircularRunout': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularRunout, None), 'XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness, None), 'XCAFDimTolObjects_GeomToleranceType_Coaxiality': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Coaxiality, None), 'XCAFDimTolObjects_GeomToleranceType_Concentricity': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Concentricity, None), 'XCAFDimTolObjects_GeomToleranceType_Cylindricity': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity, None), 'XCAFDimTolObjects_GeomToleranceType_Flatness': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Flatness, None), 'XCAFDimTolObjects_GeomToleranceType_Parallelism': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Parallelism, None), 'XCAFDimTolObjects_GeomToleranceType_Perpendicularity': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Perpendicularity, None), 'XCAFDimTolObjects_GeomToleranceType_Position': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Position, None), 'XCAFDimTolObjects_GeomToleranceType_ProfileOfLine': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfLine, None), 'XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface, None), 'XCAFDimTolObjects_GeomToleranceType_Straightness': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Straightness, None), 'XCAFDimTolObjects_GeomToleranceType_Symmetry': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Symmetry, None), 'XCAFDimTolObjects_GeomToleranceType_TotalRunout': (XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_TotalRunout, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceType_None': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_None, 'XCAFDimTolObjects_GeomToleranceType_Angularity': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Angularity, 'XCAFDimTolObjects_GeomToleranceType_CircularRunout': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularRunout, 'XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness, 'XCAFDimTolObjects_GeomToleranceType_Coaxiality': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Coaxiality, 'XCAFDimTolObjects_GeomToleranceType_Concentricity': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Concentricity, 'XCAFDimTolObjects_GeomToleranceType_Cylindricity': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity, 'XCAFDimTolObjects_GeomToleranceType_Flatness': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Flatness, 'XCAFDimTolObjects_GeomToleranceType_Parallelism': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Parallelism, 'XCAFDimTolObjects_GeomToleranceType_Perpendicularity': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Perpendicularity, 'XCAFDimTolObjects_GeomToleranceType_Position': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Position, 'XCAFDimTolObjects_GeomToleranceType_ProfileOfLine': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfLine, 'XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface, 'XCAFDimTolObjects_GeomToleranceType_Straightness': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Straightness, 'XCAFDimTolObjects_GeomToleranceType_Symmetry': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Symmetry, 'XCAFDimTolObjects_GeomToleranceType_TotalRunout': XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_TotalRunout}
    pass
class XCAFDimTolObjects_GeomToleranceTypeValue():
    """
    Defines types of value of tolerane

    Members:

      XCAFDimTolObjects_GeomToleranceTypeValue_None

      XCAFDimTolObjects_GeomToleranceTypeValue_Diameter

      XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_GeomToleranceTypeValue_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_Diameter
    XCAFDimTolObjects_GeomToleranceTypeValue_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_None
    XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceTypeValue_None': (XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_None, None), 'XCAFDimTolObjects_GeomToleranceTypeValue_Diameter': (XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_Diameter, None), 'XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter': (XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceTypeValue_None': XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_None, 'XCAFDimTolObjects_GeomToleranceTypeValue_Diameter': XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_Diameter, 'XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter': XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter}
    pass
class XCAFDimTolObjects_GeomToleranceZoneModif():
    """
    Defines types of zone

    Members:

      XCAFDimTolObjects_GeomToleranceZoneModif_None

      XCAFDimTolObjects_GeomToleranceZoneModif_Projected

      XCAFDimTolObjects_GeomToleranceZoneModif_Runout

      XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform
    XCAFDimTolObjects_GeomToleranceZoneModif_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_None
    XCAFDimTolObjects_GeomToleranceZoneModif_Projected: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Projected
    XCAFDimTolObjects_GeomToleranceZoneModif_Runout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Runout
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceZoneModif_None': (XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_None, None), 'XCAFDimTolObjects_GeomToleranceZoneModif_Projected': (XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Projected, None), 'XCAFDimTolObjects_GeomToleranceZoneModif_Runout': (XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Runout, None), 'XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform': (XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceZoneModif_None': XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_None, 'XCAFDimTolObjects_GeomToleranceZoneModif_Projected': XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Projected, 'XCAFDimTolObjects_GeomToleranceZoneModif_Runout': XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Runout, 'XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform': XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform}
    pass
class XCAFDimTolObjects_ToleranceZoneAffectedPlane():
    """
    Defines types of tolerance zone affected plane

    Members:

      XCAFDimTolObjects_ToleranceZoneAffectedPlane_None

      XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection

      XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection
    XCAFDimTolObjects_ToleranceZoneAffectedPlane_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_None
    XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation
    __entries: dict # value = {'XCAFDimTolObjects_ToleranceZoneAffectedPlane_None': (XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_None, None), 'XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection': (XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection, None), 'XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation': (XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation, None)}
    __members__: dict # value = {'XCAFDimTolObjects_ToleranceZoneAffectedPlane_None': XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_None, 'XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection': XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection, 'XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation': XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation}
    pass
class XCAFDimTolObjects_Tool():
    """
    None
    """
    def GetDimensions(self,theDimensionObjectSequence : XCAFDimTolObjects_DimensionObjectSequence) -> None: 
        """
        Returns a sequence of Dimensions currently stored in the GD&T table
        """
    def GetGeomTolerances(self,theGeomToleranceObjectSequence : XCAFDimTolObjects_GeomToleranceObjectSequence,theDatumObjectSequence : XCAFDimTolObjects_DatumObjectSequence,theMap : Any) -> None: 
        """
        Returns a sequence of Tolerances currently stored in the GD&T table
        """
    def GetRefDatum(self,theShape : OCP.TopoDS.TopoDS_Shape,theDatum : XCAFDimTolObjects_DatumObject) -> bool: 
        """
        Returns DatumObject defined for Shape
        """
    def GetRefDimensions(self,theShape : OCP.TopoDS.TopoDS_Shape,theDimensions : XCAFDimTolObjects_DimensionObjectSequence) -> bool: 
        """
        Returns all Dimensions defined for Shape
        """
    def GetRefGeomTolerances(self,theShape : OCP.TopoDS.TopoDS_Shape,theGeomToleranceObjectSequence : XCAFDimTolObjects_GeomToleranceObjectSequence,theDatumObjectSequence : XCAFDimTolObjects_DatumObjectSequence,theMap : Any) -> bool: 
        """
        Returns all GeomTolerances defined for Shape
        """
    def __init__(self,theDoc : OCP.TDocStd.TDocStd_Document) -> None: ...
    pass
XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical
XCAFDimTolObjects_DatumModifWithValue_Distance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Distance
XCAFDimTolObjects_DatumModifWithValue_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_None
XCAFDimTolObjects_DatumModifWithValue_Projected: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Projected
XCAFDimTolObjects_DatumModifWithValue_Spherical: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Spherical
XCAFDimTolObjects_DatumSingleModif_AnyCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_AnyCrossSection
XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection
XCAFDimTolObjects_DatumSingleModif_Basic: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Basic
XCAFDimTolObjects_DatumSingleModif_ContactingFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_ContactingFeature
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ
XCAFDimTolObjects_DatumSingleModif_DistanceVariable: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DistanceVariable
XCAFDimTolObjects_DatumSingleModif_FreeState: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_FreeState
XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement
XCAFDimTolObjects_DatumSingleModif_Line: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Line
XCAFDimTolObjects_DatumSingleModif_MajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MajorDiameter
XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement
XCAFDimTolObjects_DatumSingleModif_MinorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MinorDiameter
XCAFDimTolObjects_DatumSingleModif_Orientation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Orientation
XCAFDimTolObjects_DatumSingleModif_PitchDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_PitchDiameter
XCAFDimTolObjects_DatumSingleModif_Plane: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Plane
XCAFDimTolObjects_DatumSingleModif_Point: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Point
XCAFDimTolObjects_DatumSingleModif_Translation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Translation
XCAFDimTolObjects_DatumTargetType_Area: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Area
XCAFDimTolObjects_DatumTargetType_Circle: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Circle
XCAFDimTolObjects_DatumTargetType_Line: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Line
XCAFDimTolObjects_DatumTargetType_Point: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Point
XCAFDimTolObjects_DatumTargetType_Rectangle: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Rectangle
XCAFDimTolObjects_DimensionFormVariance_A: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_A
XCAFDimTolObjects_DimensionFormVariance_B: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_B
XCAFDimTolObjects_DimensionFormVariance_C: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_C
XCAFDimTolObjects_DimensionFormVariance_CD: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_CD
XCAFDimTolObjects_DimensionFormVariance_D: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_D
XCAFDimTolObjects_DimensionFormVariance_E: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_E
XCAFDimTolObjects_DimensionFormVariance_EF: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_EF
XCAFDimTolObjects_DimensionFormVariance_F: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_F
XCAFDimTolObjects_DimensionFormVariance_FG: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_FG
XCAFDimTolObjects_DimensionFormVariance_G: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_G
XCAFDimTolObjects_DimensionFormVariance_H: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_H
XCAFDimTolObjects_DimensionFormVariance_J: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_J
XCAFDimTolObjects_DimensionFormVariance_JS: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_JS
XCAFDimTolObjects_DimensionFormVariance_K: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_K
XCAFDimTolObjects_DimensionFormVariance_M: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_M
XCAFDimTolObjects_DimensionFormVariance_N: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_N
XCAFDimTolObjects_DimensionFormVariance_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_None
XCAFDimTolObjects_DimensionFormVariance_P: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_P
XCAFDimTolObjects_DimensionFormVariance_R: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_R
XCAFDimTolObjects_DimensionFormVariance_S: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_S
XCAFDimTolObjects_DimensionFormVariance_T: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_T
XCAFDimTolObjects_DimensionFormVariance_U: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_U
XCAFDimTolObjects_DimensionFormVariance_V: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_V
XCAFDimTolObjects_DimensionFormVariance_X: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_X
XCAFDimTolObjects_DimensionFormVariance_Y: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Y
XCAFDimTolObjects_DimensionFormVariance_Z: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Z
XCAFDimTolObjects_DimensionFormVariance_ZA: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZA
XCAFDimTolObjects_DimensionFormVariance_ZB: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZB
XCAFDimTolObjects_DimensionFormVariance_ZC: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZC
XCAFDimTolObjects_DimensionGrade_IT0: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT0
XCAFDimTolObjects_DimensionGrade_IT01: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT01
XCAFDimTolObjects_DimensionGrade_IT1: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT1
XCAFDimTolObjects_DimensionGrade_IT10: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT10
XCAFDimTolObjects_DimensionGrade_IT11: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT11
XCAFDimTolObjects_DimensionGrade_IT12: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT12
XCAFDimTolObjects_DimensionGrade_IT13: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT13
XCAFDimTolObjects_DimensionGrade_IT14: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT14
XCAFDimTolObjects_DimensionGrade_IT15: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT15
XCAFDimTolObjects_DimensionGrade_IT16: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT16
XCAFDimTolObjects_DimensionGrade_IT17: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT17
XCAFDimTolObjects_DimensionGrade_IT18: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT18
XCAFDimTolObjects_DimensionGrade_IT2: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT2
XCAFDimTolObjects_DimensionGrade_IT3: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT3
XCAFDimTolObjects_DimensionGrade_IT4: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT4
XCAFDimTolObjects_DimensionGrade_IT5: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT5
XCAFDimTolObjects_DimensionGrade_IT6: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT6
XCAFDimTolObjects_DimensionGrade_IT7: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT7
XCAFDimTolObjects_DimensionGrade_IT8: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT8
XCAFDimTolObjects_DimensionGrade_IT9: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT9
XCAFDimTolObjects_DimensionModif_AnyCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyCrossSection
XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature
XCAFDimTolObjects_DimensionModif_AreaDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AreaDiameter
XCAFDimTolObjects_DimensionModif_AverageSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AverageSize
XCAFDimTolObjects_DimensionModif_Between: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Between
XCAFDimTolObjects_DimensionModif_CircumferenceDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CircumferenceDiameter
XCAFDimTolObjects_DimensionModif_CommonTolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CommonTolerance
XCAFDimTolObjects_DimensionModif_ContinuousFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ContinuousFeature
XCAFDimTolObjects_DimensionModif_ControlledRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ControlledRadius
XCAFDimTolObjects_DimensionModif_FreeStateCondition: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_FreeStateCondition
XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion
XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere
XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation
XCAFDimTolObjects_DimensionModif_MaximumSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumSize
XCAFDimTolObjects_DimensionModif_MedianSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MedianSize
XCAFDimTolObjects_DimensionModif_MidRangeSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MidRangeSize
XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation
XCAFDimTolObjects_DimensionModif_MinimumSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumSize
XCAFDimTolObjects_DimensionModif_RangeOfSizes: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_RangeOfSizes
XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection
XCAFDimTolObjects_DimensionModif_Square: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Square
XCAFDimTolObjects_DimensionModif_StatisticalTolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_StatisticalTolerance
XCAFDimTolObjects_DimensionModif_TwoPointSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_TwoPointSize
XCAFDimTolObjects_DimensionModif_VolumeDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_VolumeDiameter
XCAFDimTolObjects_DimensionQualifier_Avg: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Avg
XCAFDimTolObjects_DimensionQualifier_Max: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Max
XCAFDimTolObjects_DimensionQualifier_Min: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Min
XCAFDimTolObjects_DimensionQualifier_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_None
XCAFDimTolObjects_DimensionType_CommonLabel: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_CommonLabel
XCAFDimTolObjects_DimensionType_DimensionPresentation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_DimensionPresentation
XCAFDimTolObjects_DimensionType_Location_Angular: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Angular
XCAFDimTolObjects_DimensionType_Location_CurvedDistance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_CurvedDistance
XCAFDimTolObjects_DimensionType_Location_LinearDistance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter
XCAFDimTolObjects_DimensionType_Location_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_None
XCAFDimTolObjects_DimensionType_Location_Oriented: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Oriented
XCAFDimTolObjects_DimensionType_Location_WithPath: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_WithPath
XCAFDimTolObjects_DimensionType_Size_Angular: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Angular
XCAFDimTolObjects_DimensionType_Size_CurveLength: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_CurveLength
XCAFDimTolObjects_DimensionType_Size_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter
XCAFDimTolObjects_DimensionType_Size_Radius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Radius
XCAFDimTolObjects_DimensionType_Size_SphericalDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalDiameter
XCAFDimTolObjects_DimensionType_Size_SphericalRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalRadius
XCAFDimTolObjects_DimensionType_Size_Thickness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Thickness
XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter
XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius
XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter
XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius
XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter
XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius
XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter
XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius
XCAFDimTolObjects_DimensionType_Size_WithPath: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_WithPath
XCAFDimTolObjects_GeomToleranceMatReqModif_L: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_L
XCAFDimTolObjects_GeomToleranceMatReqModif_M: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_M
XCAFDimTolObjects_GeomToleranceMatReqModif_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_None
XCAFDimTolObjects_GeomToleranceModif_All_Around: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Around
XCAFDimTolObjects_GeomToleranceModif_All_Over: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Over
XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section
XCAFDimTolObjects_GeomToleranceModif_Common_Zone: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Common_Zone
XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element
XCAFDimTolObjects_GeomToleranceModif_Free_State: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Free_State
XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement
XCAFDimTolObjects_GeomToleranceModif_Line_Element: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Line_Element
XCAFDimTolObjects_GeomToleranceModif_Major_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Major_Diameter
XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement
XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter
XCAFDimTolObjects_GeomToleranceModif_Not_Convex: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Not_Convex
XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter
XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement
XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement
XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance
XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane
XCAFDimTolObjects_GeomToleranceTypeValue_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_Diameter
XCAFDimTolObjects_GeomToleranceTypeValue_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_None
XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter
XCAFDimTolObjects_GeomToleranceType_Angularity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Angularity
XCAFDimTolObjects_GeomToleranceType_CircularRunout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularRunout
XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness
XCAFDimTolObjects_GeomToleranceType_Coaxiality: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Coaxiality
XCAFDimTolObjects_GeomToleranceType_Concentricity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Concentricity
XCAFDimTolObjects_GeomToleranceType_Cylindricity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity
XCAFDimTolObjects_GeomToleranceType_Flatness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Flatness
XCAFDimTolObjects_GeomToleranceType_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_None
XCAFDimTolObjects_GeomToleranceType_Parallelism: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Parallelism
XCAFDimTolObjects_GeomToleranceType_Perpendicularity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Perpendicularity
XCAFDimTolObjects_GeomToleranceType_Position: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Position
XCAFDimTolObjects_GeomToleranceType_ProfileOfLine: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfLine
XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface
XCAFDimTolObjects_GeomToleranceType_Straightness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Straightness
XCAFDimTolObjects_GeomToleranceType_Symmetry: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Symmetry
XCAFDimTolObjects_GeomToleranceType_TotalRunout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_TotalRunout
XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform
XCAFDimTolObjects_GeomToleranceZoneModif_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_None
XCAFDimTolObjects_GeomToleranceZoneModif_Projected: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Projected
XCAFDimTolObjects_GeomToleranceZoneModif_Runout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Runout
XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection
XCAFDimTolObjects_ToleranceZoneAffectedPlane_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_None
XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation
