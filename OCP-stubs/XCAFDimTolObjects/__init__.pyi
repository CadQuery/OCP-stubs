import OCP.XCAFDimTolObjects
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TDocStd
import io
import OCP.gp
import OCP.Standard
import OCP.TopoDS
import OCP.TCollection
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
    XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical: 1>
    XCAFDimTolObjects_DatumModifWithValue_Distance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Distance: 2>
    XCAFDimTolObjects_DatumModifWithValue_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_None: 0>
    XCAFDimTolObjects_DatumModifWithValue_Projected: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Projected: 3>
    XCAFDimTolObjects_DatumModifWithValue_Spherical: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Spherical: 4>
    __entries: dict # value = {'XCAFDimTolObjects_DatumModifWithValue_None': (<XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_None: 0>, None), 'XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical': (<XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical: 1>, None), 'XCAFDimTolObjects_DatumModifWithValue_Distance': (<XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Distance: 2>, None), 'XCAFDimTolObjects_DatumModifWithValue_Projected': (<XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Projected: 3>, None), 'XCAFDimTolObjects_DatumModifWithValue_Spherical': (<XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Spherical: 4>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DatumModifWithValue_None': <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_None: 0>, 'XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical': <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical: 1>, 'XCAFDimTolObjects_DatumModifWithValue_Distance': <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Distance: 2>, 'XCAFDimTolObjects_DatumModifWithValue_Projected': <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Projected: 3>, 'XCAFDimTolObjects_DatumModifWithValue_Spherical': <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Spherical: 4>}
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
    def Append(self,theItem : XCAFDimTolObjects_DatumSingleModif) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : XCAFDimTolObjects_DatumModifiersSequence) -> None: ...
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
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_DatumModifiersSequence) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_DatumSingleModif) -> None: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_DatumModifiersSequence) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theObj : XCAFDimTolObjects_DatumObject) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
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
    def Prepend(self,theItem : XCAFDimTolObjects_DatumObject) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : XCAFDimTolObjects_DatumObjectSequence) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_DatumObjectSequence) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
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
    XCAFDimTolObjects_DatumSingleModif_AnyCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_AnyCrossSection: 0>
    XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection: 1>
    XCAFDimTolObjects_DatumSingleModif_Basic: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Basic: 2>
    XCAFDimTolObjects_DatumSingleModif_ContactingFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_ContactingFeature: 3>
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU: 4>
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV: 5>
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW: 6>
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX: 7>
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY: 8>
    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ: 9>
    XCAFDimTolObjects_DatumSingleModif_DistanceVariable: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DistanceVariable: 10>
    XCAFDimTolObjects_DatumSingleModif_FreeState: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_FreeState: 11>
    XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement: 12>
    XCAFDimTolObjects_DatumSingleModif_Line: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Line: 13>
    XCAFDimTolObjects_DatumSingleModif_MajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MajorDiameter: 14>
    XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement: 15>
    XCAFDimTolObjects_DatumSingleModif_MinorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MinorDiameter: 16>
    XCAFDimTolObjects_DatumSingleModif_Orientation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Orientation: 17>
    XCAFDimTolObjects_DatumSingleModif_PitchDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_PitchDiameter: 18>
    XCAFDimTolObjects_DatumSingleModif_Plane: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Plane: 19>
    XCAFDimTolObjects_DatumSingleModif_Point: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Point: 20>
    XCAFDimTolObjects_DatumSingleModif_Translation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Translation: 21>
    __entries: dict # value = {'XCAFDimTolObjects_DatumSingleModif_AnyCrossSection': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_AnyCrossSection: 0>, None), 'XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection: 1>, None), 'XCAFDimTolObjects_DatumSingleModif_Basic': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Basic: 2>, None), 'XCAFDimTolObjects_DatumSingleModif_ContactingFeature': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_ContactingFeature: 3>, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU: 4>, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV: 5>, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW: 6>, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX: 7>, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY: 8>, None), 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ: 9>, None), 'XCAFDimTolObjects_DatumSingleModif_DistanceVariable': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DistanceVariable: 10>, None), 'XCAFDimTolObjects_DatumSingleModif_FreeState': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_FreeState: 11>, None), 'XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement: 12>, None), 'XCAFDimTolObjects_DatumSingleModif_Line': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Line: 13>, None), 'XCAFDimTolObjects_DatumSingleModif_MajorDiameter': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MajorDiameter: 14>, None), 'XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement: 15>, None), 'XCAFDimTolObjects_DatumSingleModif_MinorDiameter': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MinorDiameter: 16>, None), 'XCAFDimTolObjects_DatumSingleModif_Orientation': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Orientation: 17>, None), 'XCAFDimTolObjects_DatumSingleModif_PitchDiameter': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_PitchDiameter: 18>, None), 'XCAFDimTolObjects_DatumSingleModif_Plane': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Plane: 19>, None), 'XCAFDimTolObjects_DatumSingleModif_Point': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Point: 20>, None), 'XCAFDimTolObjects_DatumSingleModif_Translation': (<XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Translation: 21>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DatumSingleModif_AnyCrossSection': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_AnyCrossSection: 0>, 'XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection: 1>, 'XCAFDimTolObjects_DatumSingleModif_Basic': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Basic: 2>, 'XCAFDimTolObjects_DatumSingleModif_ContactingFeature': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_ContactingFeature: 3>, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU: 4>, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV: 5>, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW: 6>, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX: 7>, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY: 8>, 'XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ: 9>, 'XCAFDimTolObjects_DatumSingleModif_DistanceVariable': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DistanceVariable: 10>, 'XCAFDimTolObjects_DatumSingleModif_FreeState': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_FreeState: 11>, 'XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement: 12>, 'XCAFDimTolObjects_DatumSingleModif_Line': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Line: 13>, 'XCAFDimTolObjects_DatumSingleModif_MajorDiameter': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MajorDiameter: 14>, 'XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement: 15>, 'XCAFDimTolObjects_DatumSingleModif_MinorDiameter': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MinorDiameter: 16>, 'XCAFDimTolObjects_DatumSingleModif_Orientation': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Orientation: 17>, 'XCAFDimTolObjects_DatumSingleModif_PitchDiameter': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_PitchDiameter: 18>, 'XCAFDimTolObjects_DatumSingleModif_Plane': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Plane: 19>, 'XCAFDimTolObjects_DatumSingleModif_Point': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Point: 20>, 'XCAFDimTolObjects_DatumSingleModif_Translation': <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Translation: 21>}
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
    XCAFDimTolObjects_DatumTargetType_Area: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Area: 4>
    XCAFDimTolObjects_DatumTargetType_Circle: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Circle: 3>
    XCAFDimTolObjects_DatumTargetType_Line: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Line: 1>
    XCAFDimTolObjects_DatumTargetType_Point: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Point: 0>
    XCAFDimTolObjects_DatumTargetType_Rectangle: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Rectangle: 2>
    __entries: dict # value = {'XCAFDimTolObjects_DatumTargetType_Point': (<XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Point: 0>, None), 'XCAFDimTolObjects_DatumTargetType_Line': (<XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Line: 1>, None), 'XCAFDimTolObjects_DatumTargetType_Rectangle': (<XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Rectangle: 2>, None), 'XCAFDimTolObjects_DatumTargetType_Circle': (<XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Circle: 3>, None), 'XCAFDimTolObjects_DatumTargetType_Area': (<XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Area: 4>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DatumTargetType_Point': <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Point: 0>, 'XCAFDimTolObjects_DatumTargetType_Line': <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Line: 1>, 'XCAFDimTolObjects_DatumTargetType_Rectangle': <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Rectangle: 2>, 'XCAFDimTolObjects_DatumTargetType_Circle': <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Circle: 3>, 'XCAFDimTolObjects_DatumTargetType_Area': <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Area: 4>}
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
    XCAFDimTolObjects_DimensionFormVariance_A: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_A: 1>
    XCAFDimTolObjects_DimensionFormVariance_B: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_B: 2>
    XCAFDimTolObjects_DimensionFormVariance_C: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_C: 3>
    XCAFDimTolObjects_DimensionFormVariance_CD: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_CD: 4>
    XCAFDimTolObjects_DimensionFormVariance_D: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_D: 5>
    XCAFDimTolObjects_DimensionFormVariance_E: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_E: 6>
    XCAFDimTolObjects_DimensionFormVariance_EF: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_EF: 7>
    XCAFDimTolObjects_DimensionFormVariance_F: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_F: 8>
    XCAFDimTolObjects_DimensionFormVariance_FG: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_FG: 9>
    XCAFDimTolObjects_DimensionFormVariance_G: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_G: 10>
    XCAFDimTolObjects_DimensionFormVariance_H: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_H: 11>
    XCAFDimTolObjects_DimensionFormVariance_J: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_J: 13>
    XCAFDimTolObjects_DimensionFormVariance_JS: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_JS: 12>
    XCAFDimTolObjects_DimensionFormVariance_K: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_K: 14>
    XCAFDimTolObjects_DimensionFormVariance_M: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_M: 15>
    XCAFDimTolObjects_DimensionFormVariance_N: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_N: 16>
    XCAFDimTolObjects_DimensionFormVariance_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_None: 0>
    XCAFDimTolObjects_DimensionFormVariance_P: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_P: 17>
    XCAFDimTolObjects_DimensionFormVariance_R: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_R: 18>
    XCAFDimTolObjects_DimensionFormVariance_S: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_S: 19>
    XCAFDimTolObjects_DimensionFormVariance_T: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_T: 20>
    XCAFDimTolObjects_DimensionFormVariance_U: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_U: 21>
    XCAFDimTolObjects_DimensionFormVariance_V: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_V: 22>
    XCAFDimTolObjects_DimensionFormVariance_X: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_X: 23>
    XCAFDimTolObjects_DimensionFormVariance_Y: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Y: 24>
    XCAFDimTolObjects_DimensionFormVariance_Z: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Z: 25>
    XCAFDimTolObjects_DimensionFormVariance_ZA: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZA: 26>
    XCAFDimTolObjects_DimensionFormVariance_ZB: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZB: 27>
    XCAFDimTolObjects_DimensionFormVariance_ZC: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZC: 28>
    __entries: dict # value = {'XCAFDimTolObjects_DimensionFormVariance_None': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_None: 0>, None), 'XCAFDimTolObjects_DimensionFormVariance_A': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_A: 1>, None), 'XCAFDimTolObjects_DimensionFormVariance_B': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_B: 2>, None), 'XCAFDimTolObjects_DimensionFormVariance_C': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_C: 3>, None), 'XCAFDimTolObjects_DimensionFormVariance_CD': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_CD: 4>, None), 'XCAFDimTolObjects_DimensionFormVariance_D': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_D: 5>, None), 'XCAFDimTolObjects_DimensionFormVariance_E': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_E: 6>, None), 'XCAFDimTolObjects_DimensionFormVariance_EF': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_EF: 7>, None), 'XCAFDimTolObjects_DimensionFormVariance_F': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_F: 8>, None), 'XCAFDimTolObjects_DimensionFormVariance_FG': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_FG: 9>, None), 'XCAFDimTolObjects_DimensionFormVariance_G': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_G: 10>, None), 'XCAFDimTolObjects_DimensionFormVariance_H': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_H: 11>, None), 'XCAFDimTolObjects_DimensionFormVariance_JS': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_JS: 12>, None), 'XCAFDimTolObjects_DimensionFormVariance_J': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_J: 13>, None), 'XCAFDimTolObjects_DimensionFormVariance_K': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_K: 14>, None), 'XCAFDimTolObjects_DimensionFormVariance_M': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_M: 15>, None), 'XCAFDimTolObjects_DimensionFormVariance_N': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_N: 16>, None), 'XCAFDimTolObjects_DimensionFormVariance_P': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_P: 17>, None), 'XCAFDimTolObjects_DimensionFormVariance_R': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_R: 18>, None), 'XCAFDimTolObjects_DimensionFormVariance_S': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_S: 19>, None), 'XCAFDimTolObjects_DimensionFormVariance_T': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_T: 20>, None), 'XCAFDimTolObjects_DimensionFormVariance_U': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_U: 21>, None), 'XCAFDimTolObjects_DimensionFormVariance_V': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_V: 22>, None), 'XCAFDimTolObjects_DimensionFormVariance_X': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_X: 23>, None), 'XCAFDimTolObjects_DimensionFormVariance_Y': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Y: 24>, None), 'XCAFDimTolObjects_DimensionFormVariance_Z': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Z: 25>, None), 'XCAFDimTolObjects_DimensionFormVariance_ZA': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZA: 26>, None), 'XCAFDimTolObjects_DimensionFormVariance_ZB': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZB: 27>, None), 'XCAFDimTolObjects_DimensionFormVariance_ZC': (<XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZC: 28>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionFormVariance_None': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_None: 0>, 'XCAFDimTolObjects_DimensionFormVariance_A': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_A: 1>, 'XCAFDimTolObjects_DimensionFormVariance_B': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_B: 2>, 'XCAFDimTolObjects_DimensionFormVariance_C': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_C: 3>, 'XCAFDimTolObjects_DimensionFormVariance_CD': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_CD: 4>, 'XCAFDimTolObjects_DimensionFormVariance_D': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_D: 5>, 'XCAFDimTolObjects_DimensionFormVariance_E': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_E: 6>, 'XCAFDimTolObjects_DimensionFormVariance_EF': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_EF: 7>, 'XCAFDimTolObjects_DimensionFormVariance_F': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_F: 8>, 'XCAFDimTolObjects_DimensionFormVariance_FG': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_FG: 9>, 'XCAFDimTolObjects_DimensionFormVariance_G': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_G: 10>, 'XCAFDimTolObjects_DimensionFormVariance_H': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_H: 11>, 'XCAFDimTolObjects_DimensionFormVariance_JS': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_JS: 12>, 'XCAFDimTolObjects_DimensionFormVariance_J': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_J: 13>, 'XCAFDimTolObjects_DimensionFormVariance_K': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_K: 14>, 'XCAFDimTolObjects_DimensionFormVariance_M': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_M: 15>, 'XCAFDimTolObjects_DimensionFormVariance_N': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_N: 16>, 'XCAFDimTolObjects_DimensionFormVariance_P': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_P: 17>, 'XCAFDimTolObjects_DimensionFormVariance_R': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_R: 18>, 'XCAFDimTolObjects_DimensionFormVariance_S': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_S: 19>, 'XCAFDimTolObjects_DimensionFormVariance_T': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_T: 20>, 'XCAFDimTolObjects_DimensionFormVariance_U': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_U: 21>, 'XCAFDimTolObjects_DimensionFormVariance_V': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_V: 22>, 'XCAFDimTolObjects_DimensionFormVariance_X': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_X: 23>, 'XCAFDimTolObjects_DimensionFormVariance_Y': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Y: 24>, 'XCAFDimTolObjects_DimensionFormVariance_Z': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Z: 25>, 'XCAFDimTolObjects_DimensionFormVariance_ZA': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZA: 26>, 'XCAFDimTolObjects_DimensionFormVariance_ZB': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZB: 27>, 'XCAFDimTolObjects_DimensionFormVariance_ZC': <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZC: 28>}
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
    XCAFDimTolObjects_DimensionGrade_IT0: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT0: 1>
    XCAFDimTolObjects_DimensionGrade_IT01: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT01: 0>
    XCAFDimTolObjects_DimensionGrade_IT1: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT1: 2>
    XCAFDimTolObjects_DimensionGrade_IT10: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT10: 11>
    XCAFDimTolObjects_DimensionGrade_IT11: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT11: 12>
    XCAFDimTolObjects_DimensionGrade_IT12: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT12: 13>
    XCAFDimTolObjects_DimensionGrade_IT13: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT13: 14>
    XCAFDimTolObjects_DimensionGrade_IT14: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT14: 15>
    XCAFDimTolObjects_DimensionGrade_IT15: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT15: 16>
    XCAFDimTolObjects_DimensionGrade_IT16: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT16: 17>
    XCAFDimTolObjects_DimensionGrade_IT17: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT17: 18>
    XCAFDimTolObjects_DimensionGrade_IT18: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT18: 19>
    XCAFDimTolObjects_DimensionGrade_IT2: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT2: 3>
    XCAFDimTolObjects_DimensionGrade_IT3: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT3: 4>
    XCAFDimTolObjects_DimensionGrade_IT4: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT4: 5>
    XCAFDimTolObjects_DimensionGrade_IT5: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT5: 6>
    XCAFDimTolObjects_DimensionGrade_IT6: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT6: 7>
    XCAFDimTolObjects_DimensionGrade_IT7: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT7: 8>
    XCAFDimTolObjects_DimensionGrade_IT8: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT8: 9>
    XCAFDimTolObjects_DimensionGrade_IT9: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT9: 10>
    __entries: dict # value = {'XCAFDimTolObjects_DimensionGrade_IT01': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT01: 0>, None), 'XCAFDimTolObjects_DimensionGrade_IT0': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT0: 1>, None), 'XCAFDimTolObjects_DimensionGrade_IT1': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT1: 2>, None), 'XCAFDimTolObjects_DimensionGrade_IT2': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT2: 3>, None), 'XCAFDimTolObjects_DimensionGrade_IT3': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT3: 4>, None), 'XCAFDimTolObjects_DimensionGrade_IT4': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT4: 5>, None), 'XCAFDimTolObjects_DimensionGrade_IT5': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT5: 6>, None), 'XCAFDimTolObjects_DimensionGrade_IT6': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT6: 7>, None), 'XCAFDimTolObjects_DimensionGrade_IT7': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT7: 8>, None), 'XCAFDimTolObjects_DimensionGrade_IT8': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT8: 9>, None), 'XCAFDimTolObjects_DimensionGrade_IT9': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT9: 10>, None), 'XCAFDimTolObjects_DimensionGrade_IT10': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT10: 11>, None), 'XCAFDimTolObjects_DimensionGrade_IT11': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT11: 12>, None), 'XCAFDimTolObjects_DimensionGrade_IT12': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT12: 13>, None), 'XCAFDimTolObjects_DimensionGrade_IT13': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT13: 14>, None), 'XCAFDimTolObjects_DimensionGrade_IT14': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT14: 15>, None), 'XCAFDimTolObjects_DimensionGrade_IT15': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT15: 16>, None), 'XCAFDimTolObjects_DimensionGrade_IT16': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT16: 17>, None), 'XCAFDimTolObjects_DimensionGrade_IT17': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT17: 18>, None), 'XCAFDimTolObjects_DimensionGrade_IT18': (<XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT18: 19>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionGrade_IT01': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT01: 0>, 'XCAFDimTolObjects_DimensionGrade_IT0': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT0: 1>, 'XCAFDimTolObjects_DimensionGrade_IT1': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT1: 2>, 'XCAFDimTolObjects_DimensionGrade_IT2': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT2: 3>, 'XCAFDimTolObjects_DimensionGrade_IT3': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT3: 4>, 'XCAFDimTolObjects_DimensionGrade_IT4': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT4: 5>, 'XCAFDimTolObjects_DimensionGrade_IT5': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT5: 6>, 'XCAFDimTolObjects_DimensionGrade_IT6': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT6: 7>, 'XCAFDimTolObjects_DimensionGrade_IT7': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT7: 8>, 'XCAFDimTolObjects_DimensionGrade_IT8': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT8: 9>, 'XCAFDimTolObjects_DimensionGrade_IT9': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT9: 10>, 'XCAFDimTolObjects_DimensionGrade_IT10': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT10: 11>, 'XCAFDimTolObjects_DimensionGrade_IT11': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT11: 12>, 'XCAFDimTolObjects_DimensionGrade_IT12': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT12: 13>, 'XCAFDimTolObjects_DimensionGrade_IT13': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT13: 14>, 'XCAFDimTolObjects_DimensionGrade_IT14': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT14: 15>, 'XCAFDimTolObjects_DimensionGrade_IT15': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT15: 16>, 'XCAFDimTolObjects_DimensionGrade_IT16': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT16: 17>, 'XCAFDimTolObjects_DimensionGrade_IT17': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT17: 18>, 'XCAFDimTolObjects_DimensionGrade_IT18': <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT18: 19>}
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
    XCAFDimTolObjects_DimensionModif_AnyCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyCrossSection: 19>
    XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature: 18>
    XCAFDimTolObjects_DimensionModif_AreaDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AreaDiameter: 10>
    XCAFDimTolObjects_DimensionModif_AverageSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AverageSize: 14>
    XCAFDimTolObjects_DimensionModif_Between: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Between: 23>
    XCAFDimTolObjects_DimensionModif_CircumferenceDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CircumferenceDiameter: 9>
    XCAFDimTolObjects_DimensionModif_CommonTolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CommonTolerance: 21>
    XCAFDimTolObjects_DimensionModif_ContinuousFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ContinuousFeature: 3>
    XCAFDimTolObjects_DimensionModif_ControlledRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ControlledRadius: 0>
    XCAFDimTolObjects_DimensionModif_FreeStateCondition: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_FreeStateCondition: 22>
    XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion: 6>
    XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere: 5>
    XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation: 7>
    XCAFDimTolObjects_DimensionModif_MaximumSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumSize: 12>
    XCAFDimTolObjects_DimensionModif_MedianSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MedianSize: 15>
    XCAFDimTolObjects_DimensionModif_MidRangeSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MidRangeSize: 16>
    XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation: 8>
    XCAFDimTolObjects_DimensionModif_MinimumSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumSize: 13>
    XCAFDimTolObjects_DimensionModif_RangeOfSizes: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_RangeOfSizes: 17>
    XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection: 20>
    XCAFDimTolObjects_DimensionModif_Square: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Square: 1>
    XCAFDimTolObjects_DimensionModif_StatisticalTolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_StatisticalTolerance: 2>
    XCAFDimTolObjects_DimensionModif_TwoPointSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_TwoPointSize: 4>
    XCAFDimTolObjects_DimensionModif_VolumeDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_VolumeDiameter: 11>
    __entries: dict # value = {'XCAFDimTolObjects_DimensionModif_ControlledRadius': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ControlledRadius: 0>, None), 'XCAFDimTolObjects_DimensionModif_Square': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Square: 1>, None), 'XCAFDimTolObjects_DimensionModif_StatisticalTolerance': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_StatisticalTolerance: 2>, None), 'XCAFDimTolObjects_DimensionModif_ContinuousFeature': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ContinuousFeature: 3>, None), 'XCAFDimTolObjects_DimensionModif_TwoPointSize': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_TwoPointSize: 4>, None), 'XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere: 5>, None), 'XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion: 6>, None), 'XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation: 7>, None), 'XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation: 8>, None), 'XCAFDimTolObjects_DimensionModif_CircumferenceDiameter': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CircumferenceDiameter: 9>, None), 'XCAFDimTolObjects_DimensionModif_AreaDiameter': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AreaDiameter: 10>, None), 'XCAFDimTolObjects_DimensionModif_VolumeDiameter': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_VolumeDiameter: 11>, None), 'XCAFDimTolObjects_DimensionModif_MaximumSize': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumSize: 12>, None), 'XCAFDimTolObjects_DimensionModif_MinimumSize': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumSize: 13>, None), 'XCAFDimTolObjects_DimensionModif_AverageSize': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AverageSize: 14>, None), 'XCAFDimTolObjects_DimensionModif_MedianSize': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MedianSize: 15>, None), 'XCAFDimTolObjects_DimensionModif_MidRangeSize': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MidRangeSize: 16>, None), 'XCAFDimTolObjects_DimensionModif_RangeOfSizes': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_RangeOfSizes: 17>, None), 'XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature: 18>, None), 'XCAFDimTolObjects_DimensionModif_AnyCrossSection': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyCrossSection: 19>, None), 'XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection: 20>, None), 'XCAFDimTolObjects_DimensionModif_CommonTolerance': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CommonTolerance: 21>, None), 'XCAFDimTolObjects_DimensionModif_FreeStateCondition': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_FreeStateCondition: 22>, None), 'XCAFDimTolObjects_DimensionModif_Between': (<XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Between: 23>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionModif_ControlledRadius': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ControlledRadius: 0>, 'XCAFDimTolObjects_DimensionModif_Square': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Square: 1>, 'XCAFDimTolObjects_DimensionModif_StatisticalTolerance': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_StatisticalTolerance: 2>, 'XCAFDimTolObjects_DimensionModif_ContinuousFeature': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ContinuousFeature: 3>, 'XCAFDimTolObjects_DimensionModif_TwoPointSize': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_TwoPointSize: 4>, 'XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere: 5>, 'XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion: 6>, 'XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation: 7>, 'XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation: 8>, 'XCAFDimTolObjects_DimensionModif_CircumferenceDiameter': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CircumferenceDiameter: 9>, 'XCAFDimTolObjects_DimensionModif_AreaDiameter': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AreaDiameter: 10>, 'XCAFDimTolObjects_DimensionModif_VolumeDiameter': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_VolumeDiameter: 11>, 'XCAFDimTolObjects_DimensionModif_MaximumSize': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumSize: 12>, 'XCAFDimTolObjects_DimensionModif_MinimumSize': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumSize: 13>, 'XCAFDimTolObjects_DimensionModif_AverageSize': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AverageSize: 14>, 'XCAFDimTolObjects_DimensionModif_MedianSize': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MedianSize: 15>, 'XCAFDimTolObjects_DimensionModif_MidRangeSize': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MidRangeSize: 16>, 'XCAFDimTolObjects_DimensionModif_RangeOfSizes': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_RangeOfSizes: 17>, 'XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature: 18>, 'XCAFDimTolObjects_DimensionModif_AnyCrossSection': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyCrossSection: 19>, 'XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection: 20>, 'XCAFDimTolObjects_DimensionModif_CommonTolerance': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CommonTolerance: 21>, 'XCAFDimTolObjects_DimensionModif_FreeStateCondition': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_FreeStateCondition: 22>, 'XCAFDimTolObjects_DimensionModif_Between': <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Between: 23>}
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
    def Append(self,theSeq : XCAFDimTolObjects_DimensionModifiersSequence) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : XCAFDimTolObjects_DimensionModif) -> None: ...
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
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_DimensionModif) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_DimensionModifiersSequence) -> None: ...
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
    def Prepend(self,theSeq : XCAFDimTolObjects_DimensionModifiersSequence) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : XCAFDimTolObjects_DimensionModif) -> None: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_DimensionModifiersSequence) -> None: ...
    def __iter__(self) -> Iterator: ...
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_DimensionObjectSequence) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_DimensionObject) -> None: ...
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
    def __iter__(self) -> Iterator: ...
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
    XCAFDimTolObjects_DimensionQualifier_Avg: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Avg: 3>
    XCAFDimTolObjects_DimensionQualifier_Max: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Max: 2>
    XCAFDimTolObjects_DimensionQualifier_Min: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Min: 1>
    XCAFDimTolObjects_DimensionQualifier_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_None: 0>
    __entries: dict # value = {'XCAFDimTolObjects_DimensionQualifier_None': (<XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_None: 0>, None), 'XCAFDimTolObjects_DimensionQualifier_Min': (<XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Min: 1>, None), 'XCAFDimTolObjects_DimensionQualifier_Max': (<XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Max: 2>, None), 'XCAFDimTolObjects_DimensionQualifier_Avg': (<XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Avg: 3>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionQualifier_None': <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_None: 0>, 'XCAFDimTolObjects_DimensionQualifier_Min': <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Min: 1>, 'XCAFDimTolObjects_DimensionQualifier_Max': <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Max: 2>, 'XCAFDimTolObjects_DimensionQualifier_Avg': <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Avg: 3>}
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
    XCAFDimTolObjects_DimensionType_CommonLabel: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_CommonLabel: 30>
    XCAFDimTolObjects_DimensionType_DimensionPresentation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_DimensionPresentation: 31>
    XCAFDimTolObjects_DimensionType_Location_Angular: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Angular: 11>
    XCAFDimTolObjects_DimensionType_Location_CurvedDistance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_CurvedDistance: 1>
    XCAFDimTolObjects_DimensionType_Location_LinearDistance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance: 2>
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner: 4>
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter: 3>
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter: 8>
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner: 10>
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter: 9>
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter: 5>
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner: 7>
    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter: 6>
    XCAFDimTolObjects_DimensionType_Location_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_None: 0>
    XCAFDimTolObjects_DimensionType_Location_Oriented: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Oriented: 12>
    XCAFDimTolObjects_DimensionType_Location_WithPath: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_WithPath: 13>
    XCAFDimTolObjects_DimensionType_Size_Angular: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Angular: 28>
    XCAFDimTolObjects_DimensionType_Size_CurveLength: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_CurveLength: 14>
    XCAFDimTolObjects_DimensionType_Size_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter: 15>
    XCAFDimTolObjects_DimensionType_Size_Radius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Radius: 17>
    XCAFDimTolObjects_DimensionType_Size_SphericalDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalDiameter: 16>
    XCAFDimTolObjects_DimensionType_Size_SphericalRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalRadius: 18>
    XCAFDimTolObjects_DimensionType_Size_Thickness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Thickness: 27>
    XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter: 23>
    XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius: 25>
    XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter: 24>
    XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius: 26>
    XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter: 20>
    XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius: 22>
    XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter: 19>
    XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius: 21>
    XCAFDimTolObjects_DimensionType_Size_WithPath: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_WithPath: 29>
    __entries: dict # value = {'XCAFDimTolObjects_DimensionType_Location_None': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_None: 0>, None), 'XCAFDimTolObjects_DimensionType_Location_CurvedDistance': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_CurvedDistance: 1>, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance: 2>, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter: 3>, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner: 4>, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter: 5>, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter: 6>, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner: 7>, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter: 8>, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter: 9>, None), 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner: 10>, None), 'XCAFDimTolObjects_DimensionType_Location_Angular': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Angular: 11>, None), 'XCAFDimTolObjects_DimensionType_Location_Oriented': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Oriented: 12>, None), 'XCAFDimTolObjects_DimensionType_Location_WithPath': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_WithPath: 13>, None), 'XCAFDimTolObjects_DimensionType_Size_CurveLength': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_CurveLength: 14>, None), 'XCAFDimTolObjects_DimensionType_Size_Diameter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter: 15>, None), 'XCAFDimTolObjects_DimensionType_Size_SphericalDiameter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalDiameter: 16>, None), 'XCAFDimTolObjects_DimensionType_Size_Radius': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Radius: 17>, None), 'XCAFDimTolObjects_DimensionType_Size_SphericalRadius': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalRadius: 18>, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter: 19>, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter: 20>, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius: 21>, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius: 22>, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter: 23>, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter: 24>, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius: 25>, None), 'XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius: 26>, None), 'XCAFDimTolObjects_DimensionType_Size_Thickness': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Thickness: 27>, None), 'XCAFDimTolObjects_DimensionType_Size_Angular': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Angular: 28>, None), 'XCAFDimTolObjects_DimensionType_Size_WithPath': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_WithPath: 29>, None), 'XCAFDimTolObjects_DimensionType_CommonLabel': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_CommonLabel: 30>, None), 'XCAFDimTolObjects_DimensionType_DimensionPresentation': (<XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_DimensionPresentation: 31>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_DimensionType_Location_None': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_None: 0>, 'XCAFDimTolObjects_DimensionType_Location_CurvedDistance': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_CurvedDistance: 1>, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance: 2>, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter: 3>, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner: 4>, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter: 5>, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter: 6>, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner: 7>, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter: 8>, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter: 9>, 'XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner: 10>, 'XCAFDimTolObjects_DimensionType_Location_Angular': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Angular: 11>, 'XCAFDimTolObjects_DimensionType_Location_Oriented': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Oriented: 12>, 'XCAFDimTolObjects_DimensionType_Location_WithPath': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_WithPath: 13>, 'XCAFDimTolObjects_DimensionType_Size_CurveLength': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_CurveLength: 14>, 'XCAFDimTolObjects_DimensionType_Size_Diameter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter: 15>, 'XCAFDimTolObjects_DimensionType_Size_SphericalDiameter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalDiameter: 16>, 'XCAFDimTolObjects_DimensionType_Size_Radius': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Radius: 17>, 'XCAFDimTolObjects_DimensionType_Size_SphericalRadius': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalRadius: 18>, 'XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter: 19>, 'XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter: 20>, 'XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius: 21>, 'XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius: 22>, 'XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter: 23>, 'XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter: 24>, 'XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius: 25>, 'XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius: 26>, 'XCAFDimTolObjects_DimensionType_Size_Thickness': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Thickness: 27>, 'XCAFDimTolObjects_DimensionType_Size_Angular': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Angular: 28>, 'XCAFDimTolObjects_DimensionType_Size_WithPath': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_WithPath: 29>, 'XCAFDimTolObjects_DimensionType_CommonLabel': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_CommonLabel: 30>, 'XCAFDimTolObjects_DimensionType_DimensionPresentation': <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_DimensionPresentation: 31>}
    pass
class XCAFDimTolObjects_GeomToleranceMatReqModif():
    """
    Defines types of material requirement

    Members:

      XCAFDimTolObjects_GeomToleranceMatReqModif_None

      XCAFDimTolObjects_GeomToleranceMatReqModif_M

      XCAFDimTolObjects_GeomToleranceMatReqModif_L
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
    XCAFDimTolObjects_GeomToleranceMatReqModif_L: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = <XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_L: 2>
    XCAFDimTolObjects_GeomToleranceMatReqModif_M: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = <XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_M: 1>
    XCAFDimTolObjects_GeomToleranceMatReqModif_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = <XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_None: 0>
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceMatReqModif_None': (<XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_None: 0>, None), 'XCAFDimTolObjects_GeomToleranceMatReqModif_M': (<XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_M: 1>, None), 'XCAFDimTolObjects_GeomToleranceMatReqModif_L': (<XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_L: 2>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceMatReqModif_None': <XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_None: 0>, 'XCAFDimTolObjects_GeomToleranceMatReqModif_M': <XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_M: 1>, 'XCAFDimTolObjects_GeomToleranceMatReqModif_L': <XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_L: 2>}
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
    XCAFDimTolObjects_GeomToleranceModif_All_Around: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Around: 15>
    XCAFDimTolObjects_GeomToleranceModif_All_Over: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Over: 16>
    XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section: 0>
    XCAFDimTolObjects_GeomToleranceModif_Common_Zone: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Common_Zone: 1>
    XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element: 2>
    XCAFDimTolObjects_GeomToleranceModif_Free_State: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Free_State: 3>
    XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement: 4>
    XCAFDimTolObjects_GeomToleranceModif_Line_Element: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Line_Element: 5>
    XCAFDimTolObjects_GeomToleranceModif_Major_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Major_Diameter: 6>
    XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement: 7>
    XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter: 8>
    XCAFDimTolObjects_GeomToleranceModif_Not_Convex: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Not_Convex: 9>
    XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter: 10>
    XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement: 11>
    XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement: 12>
    XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance: 13>
    XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane: 14>
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section: 0>, None), 'XCAFDimTolObjects_GeomToleranceModif_Common_Zone': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Common_Zone: 1>, None), 'XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element: 2>, None), 'XCAFDimTolObjects_GeomToleranceModif_Free_State': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Free_State: 3>, None), 'XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement: 4>, None), 'XCAFDimTolObjects_GeomToleranceModif_Line_Element': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Line_Element: 5>, None), 'XCAFDimTolObjects_GeomToleranceModif_Major_Diameter': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Major_Diameter: 6>, None), 'XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement: 7>, None), 'XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter: 8>, None), 'XCAFDimTolObjects_GeomToleranceModif_Not_Convex': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Not_Convex: 9>, None), 'XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter: 10>, None), 'XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement: 11>, None), 'XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement: 12>, None), 'XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance: 13>, None), 'XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane: 14>, None), 'XCAFDimTolObjects_GeomToleranceModif_All_Around': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Around: 15>, None), 'XCAFDimTolObjects_GeomToleranceModif_All_Over': (<XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Over: 16>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section: 0>, 'XCAFDimTolObjects_GeomToleranceModif_Common_Zone': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Common_Zone: 1>, 'XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element: 2>, 'XCAFDimTolObjects_GeomToleranceModif_Free_State': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Free_State: 3>, 'XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement: 4>, 'XCAFDimTolObjects_GeomToleranceModif_Line_Element': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Line_Element: 5>, 'XCAFDimTolObjects_GeomToleranceModif_Major_Diameter': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Major_Diameter: 6>, 'XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement: 7>, 'XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter: 8>, 'XCAFDimTolObjects_GeomToleranceModif_Not_Convex': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Not_Convex: 9>, 'XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter: 10>, 'XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement: 11>, 'XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement: 12>, 'XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance: 13>, 'XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane: 14>, 'XCAFDimTolObjects_GeomToleranceModif_All_Around': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Around: 15>, 'XCAFDimTolObjects_GeomToleranceModif_All_Over': <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Over: 16>}
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
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_GeomToleranceModif) -> None: ...
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
    def Prepend(self,theSeq : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : XCAFDimTolObjects_GeomToleranceModif) -> None: ...
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
    def __init__(self,theOther : XCAFDimTolObjects_GeomToleranceModifiersSequence) -> None: ...
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def SetAffectedPlane(self,thePlane : OCP.gp.gp_Pln,theType : XCAFDimTolObjects_ToleranceZoneAffectedPlane) -> None: 
        """
        Sets affected plane.

        Sets affected plane.
        """
    @overload
    def SetAffectedPlane(self,thePlane : OCP.gp.gp_Pln) -> None: ...
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
    def Append(self,theSeq : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : XCAFDimTolObjects_GeomToleranceObject) -> None: ...
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
    def InsertAfter(self,theIndex : int,theSeq : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : XCAFDimTolObjects_GeomToleranceObject) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : XCAFDimTolObjects_GeomToleranceObject) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : XCAFDimTolObjects_GeomToleranceObjectSequence) -> None: ...
    def __iter__(self) -> Iterator: ...
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
    XCAFDimTolObjects_GeomToleranceType_Angularity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Angularity: 1>
    XCAFDimTolObjects_GeomToleranceType_CircularRunout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularRunout: 2>
    XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness: 3>
    XCAFDimTolObjects_GeomToleranceType_Coaxiality: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Coaxiality: 4>
    XCAFDimTolObjects_GeomToleranceType_Concentricity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Concentricity: 5>
    XCAFDimTolObjects_GeomToleranceType_Cylindricity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity: 6>
    XCAFDimTolObjects_GeomToleranceType_Flatness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Flatness: 7>
    XCAFDimTolObjects_GeomToleranceType_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_None: 0>
    XCAFDimTolObjects_GeomToleranceType_Parallelism: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Parallelism: 8>
    XCAFDimTolObjects_GeomToleranceType_Perpendicularity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Perpendicularity: 9>
    XCAFDimTolObjects_GeomToleranceType_Position: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Position: 10>
    XCAFDimTolObjects_GeomToleranceType_ProfileOfLine: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfLine: 11>
    XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface: 12>
    XCAFDimTolObjects_GeomToleranceType_Straightness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Straightness: 13>
    XCAFDimTolObjects_GeomToleranceType_Symmetry: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Symmetry: 14>
    XCAFDimTolObjects_GeomToleranceType_TotalRunout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_TotalRunout: 15>
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceType_None': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_None: 0>, None), 'XCAFDimTolObjects_GeomToleranceType_Angularity': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Angularity: 1>, None), 'XCAFDimTolObjects_GeomToleranceType_CircularRunout': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularRunout: 2>, None), 'XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness: 3>, None), 'XCAFDimTolObjects_GeomToleranceType_Coaxiality': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Coaxiality: 4>, None), 'XCAFDimTolObjects_GeomToleranceType_Concentricity': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Concentricity: 5>, None), 'XCAFDimTolObjects_GeomToleranceType_Cylindricity': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity: 6>, None), 'XCAFDimTolObjects_GeomToleranceType_Flatness': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Flatness: 7>, None), 'XCAFDimTolObjects_GeomToleranceType_Parallelism': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Parallelism: 8>, None), 'XCAFDimTolObjects_GeomToleranceType_Perpendicularity': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Perpendicularity: 9>, None), 'XCAFDimTolObjects_GeomToleranceType_Position': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Position: 10>, None), 'XCAFDimTolObjects_GeomToleranceType_ProfileOfLine': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfLine: 11>, None), 'XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface: 12>, None), 'XCAFDimTolObjects_GeomToleranceType_Straightness': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Straightness: 13>, None), 'XCAFDimTolObjects_GeomToleranceType_Symmetry': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Symmetry: 14>, None), 'XCAFDimTolObjects_GeomToleranceType_TotalRunout': (<XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_TotalRunout: 15>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceType_None': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_None: 0>, 'XCAFDimTolObjects_GeomToleranceType_Angularity': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Angularity: 1>, 'XCAFDimTolObjects_GeomToleranceType_CircularRunout': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularRunout: 2>, 'XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness: 3>, 'XCAFDimTolObjects_GeomToleranceType_Coaxiality': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Coaxiality: 4>, 'XCAFDimTolObjects_GeomToleranceType_Concentricity': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Concentricity: 5>, 'XCAFDimTolObjects_GeomToleranceType_Cylindricity': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity: 6>, 'XCAFDimTolObjects_GeomToleranceType_Flatness': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Flatness: 7>, 'XCAFDimTolObjects_GeomToleranceType_Parallelism': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Parallelism: 8>, 'XCAFDimTolObjects_GeomToleranceType_Perpendicularity': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Perpendicularity: 9>, 'XCAFDimTolObjects_GeomToleranceType_Position': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Position: 10>, 'XCAFDimTolObjects_GeomToleranceType_ProfileOfLine': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfLine: 11>, 'XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface: 12>, 'XCAFDimTolObjects_GeomToleranceType_Straightness': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Straightness: 13>, 'XCAFDimTolObjects_GeomToleranceType_Symmetry': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Symmetry: 14>, 'XCAFDimTolObjects_GeomToleranceType_TotalRunout': <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_TotalRunout: 15>}
    pass
class XCAFDimTolObjects_GeomToleranceTypeValue():
    """
    Defines types of value of tolerane

    Members:

      XCAFDimTolObjects_GeomToleranceTypeValue_None

      XCAFDimTolObjects_GeomToleranceTypeValue_Diameter

      XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter
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
    XCAFDimTolObjects_GeomToleranceTypeValue_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = <XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_Diameter: 1>
    XCAFDimTolObjects_GeomToleranceTypeValue_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = <XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_None: 0>
    XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = <XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter: 2>
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceTypeValue_None': (<XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_None: 0>, None), 'XCAFDimTolObjects_GeomToleranceTypeValue_Diameter': (<XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_Diameter: 1>, None), 'XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter': (<XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter: 2>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceTypeValue_None': <XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_None: 0>, 'XCAFDimTolObjects_GeomToleranceTypeValue_Diameter': <XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_Diameter: 1>, 'XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter': <XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter: 2>}
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
    XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform: 3>
    XCAFDimTolObjects_GeomToleranceZoneModif_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_None: 0>
    XCAFDimTolObjects_GeomToleranceZoneModif_Projected: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Projected: 1>
    XCAFDimTolObjects_GeomToleranceZoneModif_Runout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Runout: 2>
    __entries: dict # value = {'XCAFDimTolObjects_GeomToleranceZoneModif_None': (<XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_None: 0>, None), 'XCAFDimTolObjects_GeomToleranceZoneModif_Projected': (<XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Projected: 1>, None), 'XCAFDimTolObjects_GeomToleranceZoneModif_Runout': (<XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Runout: 2>, None), 'XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform': (<XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform: 3>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_GeomToleranceZoneModif_None': <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_None: 0>, 'XCAFDimTolObjects_GeomToleranceZoneModif_Projected': <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Projected: 1>, 'XCAFDimTolObjects_GeomToleranceZoneModif_Runout': <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Runout: 2>, 'XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform': <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform: 3>}
    pass
class XCAFDimTolObjects_ToleranceZoneAffectedPlane():
    """
    Defines types of tolerance zone affected plane

    Members:

      XCAFDimTolObjects_ToleranceZoneAffectedPlane_None

      XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection

      XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation
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
    XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = <XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection: 1>
    XCAFDimTolObjects_ToleranceZoneAffectedPlane_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = <XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_None: 0>
    XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = <XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation: 2>
    __entries: dict # value = {'XCAFDimTolObjects_ToleranceZoneAffectedPlane_None': (<XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_None: 0>, None), 'XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection': (<XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection: 1>, None), 'XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation': (<XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation: 2>, None)}
    __members__: dict # value = {'XCAFDimTolObjects_ToleranceZoneAffectedPlane_None': <XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_None: 0>, 'XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection': <XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection: 1>, 'XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation': <XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation: 2>}
    pass
class XCAFDimTolObjects_Tool():
    """
    None
    """
    def GetDimensions(self,theDimensionObjectSequence : XCAFDimTolObjects_DimensionObjectSequence) -> None: 
        """
        Returns a sequence of Dimensions currently stored in the GD&T table
        """
    def GetRefDatum(self,theShape : OCP.TopoDS.TopoDS_Shape,theDatum : XCAFDimTolObjects_DatumObject) -> bool: 
        """
        Returns DatumObject defined for Shape
        """
    def GetRefDimensions(self,theShape : OCP.TopoDS.TopoDS_Shape,theDimensions : XCAFDimTolObjects_DimensionObjectSequence) -> bool: 
        """
        Returns all Dimensions defined for Shape
        """
    def __init__(self,theDoc : OCP.TDocStd.TDocStd_Document) -> None: ...
    pass
XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical: 1>
XCAFDimTolObjects_DatumModifWithValue_Distance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Distance: 2>
XCAFDimTolObjects_DatumModifWithValue_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_None: 0>
XCAFDimTolObjects_DatumModifWithValue_Projected: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Projected: 3>
XCAFDimTolObjects_DatumModifWithValue_Spherical: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue # value = <XCAFDimTolObjects_DatumModifWithValue.XCAFDimTolObjects_DatumModifWithValue_Spherical: 4>
XCAFDimTolObjects_DatumSingleModif_AnyCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_AnyCrossSection: 0>
XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection: 1>
XCAFDimTolObjects_DatumSingleModif_Basic: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Basic: 2>
XCAFDimTolObjects_DatumSingleModif_ContactingFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_ContactingFeature: 3>
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU: 4>
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV: 5>
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW: 6>
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX: 7>
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY: 8>
XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ: 9>
XCAFDimTolObjects_DatumSingleModif_DistanceVariable: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_DistanceVariable: 10>
XCAFDimTolObjects_DatumSingleModif_FreeState: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_FreeState: 11>
XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement: 12>
XCAFDimTolObjects_DatumSingleModif_Line: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Line: 13>
XCAFDimTolObjects_DatumSingleModif_MajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MajorDiameter: 14>
XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement: 15>
XCAFDimTolObjects_DatumSingleModif_MinorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_MinorDiameter: 16>
XCAFDimTolObjects_DatumSingleModif_Orientation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Orientation: 17>
XCAFDimTolObjects_DatumSingleModif_PitchDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_PitchDiameter: 18>
XCAFDimTolObjects_DatumSingleModif_Plane: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Plane: 19>
XCAFDimTolObjects_DatumSingleModif_Point: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Point: 20>
XCAFDimTolObjects_DatumSingleModif_Translation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif # value = <XCAFDimTolObjects_DatumSingleModif.XCAFDimTolObjects_DatumSingleModif_Translation: 21>
XCAFDimTolObjects_DatumTargetType_Area: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Area: 4>
XCAFDimTolObjects_DatumTargetType_Circle: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Circle: 3>
XCAFDimTolObjects_DatumTargetType_Line: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Line: 1>
XCAFDimTolObjects_DatumTargetType_Point: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Point: 0>
XCAFDimTolObjects_DatumTargetType_Rectangle: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType # value = <XCAFDimTolObjects_DatumTargetType.XCAFDimTolObjects_DatumTargetType_Rectangle: 2>
XCAFDimTolObjects_DimensionFormVariance_A: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_A: 1>
XCAFDimTolObjects_DimensionFormVariance_B: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_B: 2>
XCAFDimTolObjects_DimensionFormVariance_C: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_C: 3>
XCAFDimTolObjects_DimensionFormVariance_CD: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_CD: 4>
XCAFDimTolObjects_DimensionFormVariance_D: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_D: 5>
XCAFDimTolObjects_DimensionFormVariance_E: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_E: 6>
XCAFDimTolObjects_DimensionFormVariance_EF: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_EF: 7>
XCAFDimTolObjects_DimensionFormVariance_F: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_F: 8>
XCAFDimTolObjects_DimensionFormVariance_FG: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_FG: 9>
XCAFDimTolObjects_DimensionFormVariance_G: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_G: 10>
XCAFDimTolObjects_DimensionFormVariance_H: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_H: 11>
XCAFDimTolObjects_DimensionFormVariance_J: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_J: 13>
XCAFDimTolObjects_DimensionFormVariance_JS: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_JS: 12>
XCAFDimTolObjects_DimensionFormVariance_K: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_K: 14>
XCAFDimTolObjects_DimensionFormVariance_M: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_M: 15>
XCAFDimTolObjects_DimensionFormVariance_N: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_N: 16>
XCAFDimTolObjects_DimensionFormVariance_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_None: 0>
XCAFDimTolObjects_DimensionFormVariance_P: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_P: 17>
XCAFDimTolObjects_DimensionFormVariance_R: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_R: 18>
XCAFDimTolObjects_DimensionFormVariance_S: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_S: 19>
XCAFDimTolObjects_DimensionFormVariance_T: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_T: 20>
XCAFDimTolObjects_DimensionFormVariance_U: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_U: 21>
XCAFDimTolObjects_DimensionFormVariance_V: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_V: 22>
XCAFDimTolObjects_DimensionFormVariance_X: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_X: 23>
XCAFDimTolObjects_DimensionFormVariance_Y: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Y: 24>
XCAFDimTolObjects_DimensionFormVariance_Z: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_Z: 25>
XCAFDimTolObjects_DimensionFormVariance_ZA: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZA: 26>
XCAFDimTolObjects_DimensionFormVariance_ZB: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZB: 27>
XCAFDimTolObjects_DimensionFormVariance_ZC: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance # value = <XCAFDimTolObjects_DimensionFormVariance.XCAFDimTolObjects_DimensionFormVariance_ZC: 28>
XCAFDimTolObjects_DimensionGrade_IT0: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT0: 1>
XCAFDimTolObjects_DimensionGrade_IT01: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT01: 0>
XCAFDimTolObjects_DimensionGrade_IT1: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT1: 2>
XCAFDimTolObjects_DimensionGrade_IT10: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT10: 11>
XCAFDimTolObjects_DimensionGrade_IT11: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT11: 12>
XCAFDimTolObjects_DimensionGrade_IT12: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT12: 13>
XCAFDimTolObjects_DimensionGrade_IT13: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT13: 14>
XCAFDimTolObjects_DimensionGrade_IT14: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT14: 15>
XCAFDimTolObjects_DimensionGrade_IT15: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT15: 16>
XCAFDimTolObjects_DimensionGrade_IT16: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT16: 17>
XCAFDimTolObjects_DimensionGrade_IT17: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT17: 18>
XCAFDimTolObjects_DimensionGrade_IT18: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT18: 19>
XCAFDimTolObjects_DimensionGrade_IT2: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT2: 3>
XCAFDimTolObjects_DimensionGrade_IT3: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT3: 4>
XCAFDimTolObjects_DimensionGrade_IT4: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT4: 5>
XCAFDimTolObjects_DimensionGrade_IT5: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT5: 6>
XCAFDimTolObjects_DimensionGrade_IT6: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT6: 7>
XCAFDimTolObjects_DimensionGrade_IT7: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT7: 8>
XCAFDimTolObjects_DimensionGrade_IT8: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT8: 9>
XCAFDimTolObjects_DimensionGrade_IT9: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade # value = <XCAFDimTolObjects_DimensionGrade.XCAFDimTolObjects_DimensionGrade_IT9: 10>
XCAFDimTolObjects_DimensionModif_AnyCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyCrossSection: 19>
XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature: 18>
XCAFDimTolObjects_DimensionModif_AreaDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AreaDiameter: 10>
XCAFDimTolObjects_DimensionModif_AverageSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_AverageSize: 14>
XCAFDimTolObjects_DimensionModif_Between: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Between: 23>
XCAFDimTolObjects_DimensionModif_CircumferenceDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CircumferenceDiameter: 9>
XCAFDimTolObjects_DimensionModif_CommonTolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_CommonTolerance: 21>
XCAFDimTolObjects_DimensionModif_ContinuousFeature: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ContinuousFeature: 3>
XCAFDimTolObjects_DimensionModif_ControlledRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_ControlledRadius: 0>
XCAFDimTolObjects_DimensionModif_FreeStateCondition: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_FreeStateCondition: 22>
XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion: 6>
XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere: 5>
XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation: 7>
XCAFDimTolObjects_DimensionModif_MaximumSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MaximumSize: 12>
XCAFDimTolObjects_DimensionModif_MedianSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MedianSize: 15>
XCAFDimTolObjects_DimensionModif_MidRangeSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MidRangeSize: 16>
XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation: 8>
XCAFDimTolObjects_DimensionModif_MinimumSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_MinimumSize: 13>
XCAFDimTolObjects_DimensionModif_RangeOfSizes: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_RangeOfSizes: 17>
XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection: 20>
XCAFDimTolObjects_DimensionModif_Square: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_Square: 1>
XCAFDimTolObjects_DimensionModif_StatisticalTolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_StatisticalTolerance: 2>
XCAFDimTolObjects_DimensionModif_TwoPointSize: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_TwoPointSize: 4>
XCAFDimTolObjects_DimensionModif_VolumeDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif # value = <XCAFDimTolObjects_DimensionModif.XCAFDimTolObjects_DimensionModif_VolumeDiameter: 11>
XCAFDimTolObjects_DimensionQualifier_Avg: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Avg: 3>
XCAFDimTolObjects_DimensionQualifier_Max: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Max: 2>
XCAFDimTolObjects_DimensionQualifier_Min: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_Min: 1>
XCAFDimTolObjects_DimensionQualifier_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier # value = <XCAFDimTolObjects_DimensionQualifier.XCAFDimTolObjects_DimensionQualifier_None: 0>
XCAFDimTolObjects_DimensionType_CommonLabel: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_CommonLabel: 30>
XCAFDimTolObjects_DimensionType_DimensionPresentation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_DimensionPresentation: 31>
XCAFDimTolObjects_DimensionType_Location_Angular: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Angular: 11>
XCAFDimTolObjects_DimensionType_Location_CurvedDistance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_CurvedDistance: 1>
XCAFDimTolObjects_DimensionType_Location_LinearDistance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance: 2>
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner: 4>
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter: 3>
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter: 8>
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner: 10>
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter: 9>
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter: 5>
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner: 7>
XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter: 6>
XCAFDimTolObjects_DimensionType_Location_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_None: 0>
XCAFDimTolObjects_DimensionType_Location_Oriented: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_Oriented: 12>
XCAFDimTolObjects_DimensionType_Location_WithPath: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Location_WithPath: 13>
XCAFDimTolObjects_DimensionType_Size_Angular: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Angular: 28>
XCAFDimTolObjects_DimensionType_Size_CurveLength: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_CurveLength: 14>
XCAFDimTolObjects_DimensionType_Size_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Diameter: 15>
XCAFDimTolObjects_DimensionType_Size_Radius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Radius: 17>
XCAFDimTolObjects_DimensionType_Size_SphericalDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalDiameter: 16>
XCAFDimTolObjects_DimensionType_Size_SphericalRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_SphericalRadius: 18>
XCAFDimTolObjects_DimensionType_Size_Thickness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_Thickness: 27>
XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter: 23>
XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius: 25>
XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter: 24>
XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius: 26>
XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter: 20>
XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius: 22>
XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter: 19>
XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius: 21>
XCAFDimTolObjects_DimensionType_Size_WithPath: OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType # value = <XCAFDimTolObjects_DimensionType.XCAFDimTolObjects_DimensionType_Size_WithPath: 29>
XCAFDimTolObjects_GeomToleranceMatReqModif_L: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = <XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_L: 2>
XCAFDimTolObjects_GeomToleranceMatReqModif_M: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = <XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_M: 1>
XCAFDimTolObjects_GeomToleranceMatReqModif_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceMatReqModif # value = <XCAFDimTolObjects_GeomToleranceMatReqModif.XCAFDimTolObjects_GeomToleranceMatReqModif_None: 0>
XCAFDimTolObjects_GeomToleranceModif_All_Around: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Around: 15>
XCAFDimTolObjects_GeomToleranceModif_All_Over: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_All_Over: 16>
XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section: 0>
XCAFDimTolObjects_GeomToleranceModif_Common_Zone: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Common_Zone: 1>
XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element: 2>
XCAFDimTolObjects_GeomToleranceModif_Free_State: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Free_State: 3>
XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement: 4>
XCAFDimTolObjects_GeomToleranceModif_Line_Element: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Line_Element: 5>
XCAFDimTolObjects_GeomToleranceModif_Major_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Major_Diameter: 6>
XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement: 7>
XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter: 8>
XCAFDimTolObjects_GeomToleranceModif_Not_Convex: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Not_Convex: 9>
XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter: 10>
XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement: 11>
XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement: 12>
XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance: 13>
XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif # value = <XCAFDimTolObjects_GeomToleranceModif.XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane: 14>
XCAFDimTolObjects_GeomToleranceTypeValue_Diameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = <XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_Diameter: 1>
XCAFDimTolObjects_GeomToleranceTypeValue_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = <XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_None: 0>
XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue # value = <XCAFDimTolObjects_GeomToleranceTypeValue.XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter: 2>
XCAFDimTolObjects_GeomToleranceType_Angularity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Angularity: 1>
XCAFDimTolObjects_GeomToleranceType_CircularRunout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularRunout: 2>
XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness: 3>
XCAFDimTolObjects_GeomToleranceType_Coaxiality: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Coaxiality: 4>
XCAFDimTolObjects_GeomToleranceType_Concentricity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Concentricity: 5>
XCAFDimTolObjects_GeomToleranceType_Cylindricity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Cylindricity: 6>
XCAFDimTolObjects_GeomToleranceType_Flatness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Flatness: 7>
XCAFDimTolObjects_GeomToleranceType_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_None: 0>
XCAFDimTolObjects_GeomToleranceType_Parallelism: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Parallelism: 8>
XCAFDimTolObjects_GeomToleranceType_Perpendicularity: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Perpendicularity: 9>
XCAFDimTolObjects_GeomToleranceType_Position: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Position: 10>
XCAFDimTolObjects_GeomToleranceType_ProfileOfLine: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfLine: 11>
XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface: 12>
XCAFDimTolObjects_GeomToleranceType_Straightness: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Straightness: 13>
XCAFDimTolObjects_GeomToleranceType_Symmetry: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_Symmetry: 14>
XCAFDimTolObjects_GeomToleranceType_TotalRunout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType # value = <XCAFDimTolObjects_GeomToleranceType.XCAFDimTolObjects_GeomToleranceType_TotalRunout: 15>
XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform: 3>
XCAFDimTolObjects_GeomToleranceZoneModif_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_None: 0>
XCAFDimTolObjects_GeomToleranceZoneModif_Projected: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Projected: 1>
XCAFDimTolObjects_GeomToleranceZoneModif_Runout: OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceZoneModif # value = <XCAFDimTolObjects_GeomToleranceZoneModif.XCAFDimTolObjects_GeomToleranceZoneModif_Runout: 2>
XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = <XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection: 1>
XCAFDimTolObjects_ToleranceZoneAffectedPlane_None: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = <XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_None: 0>
XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation: OCP.XCAFDimTolObjects.XCAFDimTolObjects_ToleranceZoneAffectedPlane # value = <XCAFDimTolObjects_ToleranceZoneAffectedPlane.XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation: 2>
