import OCP.GeomFill
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom2d
import OCP.Law
import OCP.TColgp
import OCP.Adaptor3d
import OCP.Convert
import OCP.NCollection
import OCP.gp
import OCP.TColStd
import OCP.GeomAbs
import OCP.TColGeom
import OCP.Approx
import OCP.Standard
import OCP.Geom
import OCP.math
import OCP.AppBlend
__all__  = [
"GeomFill",
"GeomFill_AppSurf",
"GeomFill_AppSweep",
"GeomFill_ApproxStyle",
"GeomFill_Array1OfLocationLaw",
"GeomFill_Array1OfSectionLaw",
"GeomFill_BSplineCurves",
"GeomFill_BezierCurves",
"GeomFill_Boundary",
"GeomFill_BoundWithSurf",
"GeomFill_CircularBlendFunc",
"GeomFill_TrihedronLaw",
"GeomFill_ConstrainedFilling",
"GeomFill_Filling",
"GeomFill_CoonsAlgPatch",
"GeomFill_CornerState",
"GeomFill_CorrectedFrenet",
"GeomFill_LocationLaw",
"GeomFill_Curved",
"GeomFill_Darboux",
"GeomFill_DegeneratedBound",
"GeomFill_DiscreteTrihedron",
"GeomFill_DraftTrihedron",
"GeomFill_SectionLaw",
"GeomFill_Coons",
"GeomFill_FillingStyle",
"GeomFill_Fixed",
"GeomFill_Frenet",
"GeomFill_FunctionDraft",
"GeomFill_FunctionGuide",
"GeomFill_Profiler",
"GeomFill_TrihedronWithGuide",
"GeomFill_GuideTrihedronPlan",
"GeomFill_HArray1OfLocationLaw",
"GeomFill_HArray1OfSectionLaw",
"GeomFill_SequenceOfAx2",
"GeomFill_Line",
"GeomFill_LocFunction",
"GeomFill_LocationDraft",
"GeomFill_LocationGuide",
"GeomFill_CurveAndTrihedron",
"GeomFill_NSections",
"GeomFill_Pipe",
"GeomFill_PipeError",
"GeomFill_PlanFunc",
"GeomFill_PolynomialConvertor",
"GeomFill_Generator",
"GeomFill_QuasiAngularConvertor",
"GeomFill_SectionGenerator",
"GeomFill_EvolvedSection",
"GeomFill_SectionPlacement",
"GeomFill_HSequenceOfAx2",
"GeomFill_SequenceOfTrsf",
"GeomFill_SimpleBound",
"GeomFill_SnglrFunc",
"GeomFill_Stretch",
"GeomFill_Sweep",
"GeomFill_SweepFunction",
"GeomFill_SweepSectionGenerator",
"GeomFill_Tensor",
"GeomFill_TgtField",
"GeomFill_TgtOnCoons",
"GeomFill_Trihedron",
"GeomFill_ConstantBiNormal",
"GeomFill_GuideTrihedronAC",
"GeomFill_UniformSection",
"GeomFill_CoonsStyle",
"GeomFill_CurvedStyle",
"GeomFill_ImpossibleContact",
"GeomFill_IsConstantNormal",
"GeomFill_IsCorrectedFrenet",
"GeomFill_IsDarboux",
"GeomFill_IsDiscreteTrihedron",
"GeomFill_IsFixed",
"GeomFill_IsFrenet",
"GeomFill_IsGuideAC",
"GeomFill_IsGuideACWithContact",
"GeomFill_IsGuidePlan",
"GeomFill_IsGuidePlanWithContact",
"GeomFill_Location",
"GeomFill_PipeNotOk",
"GeomFill_PipeOk",
"GeomFill_PlaneNotIntersectGuide",
"GeomFill_Section",
"GeomFill_StretchStyle"
]
class GeomFill():
    """
    Tools and Data to filling Surface and Sweep Surfaces
    """
    @staticmethod
    @overload
    def GetCircle_s(TConv : OCP.Convert.Convert_ParameterisationType,ns1 : OCP.gp.gp_Vec,ns2 : OCP.gp.gp_Vec,nplan : OCP.gp.gp_Vec,pt1 : OCP.gp.gp_Pnt,pt2 : OCP.gp.gp_Pnt,Rayon : float,Center : OCP.gp.gp_Pnt,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None

        None
        """
    @staticmethod
    @overload
    def GetCircle_s(TConv : OCP.Convert.Convert_ParameterisationType,ns1 : OCP.gp.gp_Vec,ns2 : OCP.gp.gp_Vec,dn1w : OCP.gp.gp_Vec,dn2w : OCP.gp.gp_Vec,d2n1w : OCP.gp.gp_Vec,d2n2w : OCP.gp.gp_Vec,nplan : OCP.gp.gp_Vec,dnplan : OCP.gp.gp_Vec,d2nplan : OCP.gp.gp_Vec,pts1 : OCP.gp.gp_Pnt,pts2 : OCP.gp.gp_Pnt,tang1 : OCP.gp.gp_Vec,tang2 : OCP.gp.gp_Vec,Dtang1 : OCP.gp.gp_Vec,Dtang2 : OCP.gp.gp_Vec,Rayon : float,DRayon : float,D2Rayon : float,Center : OCP.gp.gp_Pnt,DCenter : OCP.gp.gp_Vec,D2Center : OCP.gp.gp_Vec,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @staticmethod
    @overload
    def GetCircle_s(TConv : OCP.Convert.Convert_ParameterisationType,ns1 : OCP.gp.gp_Vec,ns2 : OCP.gp.gp_Vec,dn1w : OCP.gp.gp_Vec,dn2w : OCP.gp.gp_Vec,nplan : OCP.gp.gp_Vec,dnplan : OCP.gp.gp_Vec,pts1 : OCP.gp.gp_Pnt,pts2 : OCP.gp.gp_Pnt,tang1 : OCP.gp.gp_Vec,tang2 : OCP.gp.gp_Vec,Rayon : float,DRayon : float,Center : OCP.gp.gp_Pnt,DCenter : OCP.gp.gp_Vec,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @staticmethod
    def GetMinimalWeights_s(TConv : OCP.Convert.Convert_ParameterisationType,AngleMin : float,AngleMax : float,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    @staticmethod
    def GetShape_s(MaxAng : float,TypeConv : OCP.Convert.Convert_ParameterisationType) -> Tuple[int, int, int]: 
        """
        None
        """
    @staticmethod
    def GetTolerance_s(TConv : OCP.Convert.Convert_ParameterisationType,AngleMin : float,Radius : float,AngularTol : float,SpatialTol : float) -> float: 
        """
        Used by the generical classes to determine Tolerance for approximation
        """
    @staticmethod
    def Knots_s(TypeConv : OCP.Convert.Convert_ParameterisationType,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    @staticmethod
    def Mults_s(TypeConv : OCP.Convert.Convert_ParameterisationType,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    @staticmethod
    def Surface_s(Curve1 : OCP.Geom.Geom_Curve,Curve2 : OCP.Geom.Geom_Curve) -> OCP.Geom.Geom_Surface: 
        """
        Builds a ruled surface between the two curves, Curve1 and Curve2.
        """
    def __init__(self) -> None: ...
    pass
class GeomFill_AppSurf(OCP.AppBlend.AppBlend_Approx):
    """
    Approximate a BSplineSurface passing by all the curves described in the SectionGenerator
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        returns the Continuity used in the approximation
        """
    def CriteriumWeight(self) -> Tuple[float, float, float]: 
        """
        returns the Weights (as percent) associed to the criterium used in the optimization.
        """
    def Curve2d(self,Index : int,TPoles : OCP.TColgp.TColgp_Array1OfPnt2d,TKnots : OCP.TColStd.TColStd_Array1OfReal,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def Curve2dPoles(self,Index : int) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        None
        """
    def Curves2dDegree(self) -> int: 
        """
        None
        """
    def Curves2dKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def Curves2dMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def Curves2dShape(self) -> Tuple[int, int, int]: 
        """
        None
        """
    def Init(self,Degmin : int,Degmax : int,Tol3d : float,Tol2d : float,NbIt : int,KnownParameters : bool=False) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbCurves2d(self) -> int: 
        """
        None
        """
    def ParType(self) -> OCP.Approx.Approx_ParametrizationType: 
        """
        returns the type of parametrization used in the approximation
        """
    @overload
    def Perform(self,Lin : GeomFill_Line,SecGen : GeomFill_SectionGenerator,SpApprox : bool=False) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,Lin : GeomFill_Line,SecGen : GeomFill_SectionGenerator,NbMaxP : int) -> None: ...
    def PerformSmoothing(self,Lin : GeomFill_Line,SecGen : GeomFill_SectionGenerator) -> None: 
        """
        None
        """
    def SetContinuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Define the Continuity used in the approximation
        """
    def SetCriteriumWeight(self,W1 : float,W2 : float,W3 : float) -> None: 
        """
        define the Weights associed to the criterium used in the optimization.
        """
    def SetParType(self,ParType : OCP.Approx.Approx_ParametrizationType) -> None: 
        """
        Define the type of parametrization used in the approximation
        """
    def SurfPoles(self) -> OCP.TColgp.TColgp_Array2OfPnt: 
        """
        None
        """
    def SurfShape(self) -> Tuple[int, int, int, int, int, int]: 
        """
        None
        """
    def SurfUKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def SurfUMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def SurfVKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def SurfVMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def SurfWeights(self) -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        None
        """
    def Surface(self,TPoles : OCP.TColgp.TColgp_Array2OfPnt,TWeights : OCP.TColStd.TColStd_Array2OfReal,TUKnots : OCP.TColStd.TColStd_Array1OfReal,TVKnots : OCP.TColStd.TColStd_Array1OfReal,TUMults : OCP.TColStd.TColStd_Array1OfInteger,TVMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def TolCurveOnSurf(self,Index : int) -> float: 
        """
        None
        """
    def TolReached(self) -> Tuple[float, float]: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self,Degmin : int,Degmax : int,Tol3d : float,Tol2d : float,NbIt : int,KnownParameters : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomFill_AppSweep(OCP.AppBlend.AppBlend_Approx):
    """
    Approximate a sweep surface passing by all the curves described in the SweepSectionGenerator.
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        returns the Continuity used in the approximation
        """
    def CriteriumWeight(self) -> Tuple[float, float, float]: 
        """
        returns the Weights (as percent) associed to the criterium used in the optimization.
        """
    def Curve2d(self,Index : int,TPoles : OCP.TColgp.TColgp_Array1OfPnt2d,TKnots : OCP.TColStd.TColStd_Array1OfReal,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def Curve2dPoles(self,Index : int) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        None
        """
    def Curves2dDegree(self) -> int: 
        """
        None
        """
    def Curves2dKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def Curves2dMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def Curves2dShape(self) -> Tuple[int, int, int]: 
        """
        None
        """
    def Init(self,Degmin : int,Degmax : int,Tol3d : float,Tol2d : float,NbIt : int,KnownParameters : bool=False) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbCurves2d(self) -> int: 
        """
        None
        """
    def ParType(self) -> OCP.Approx.Approx_ParametrizationType: 
        """
        returns the type of parametrization used in the approximation
        """
    @overload
    def Perform(self,Lin : GeomFill_Line,SecGen : GeomFill_SweepSectionGenerator,SpApprox : bool=False) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,Lin : GeomFill_Line,SecGen : GeomFill_SweepSectionGenerator,NbMaxP : int) -> None: ...
    def PerformSmoothing(self,Lin : GeomFill_Line,SecGen : GeomFill_SweepSectionGenerator) -> None: 
        """
        None
        """
    def SetContinuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Define the Continuity used in the approximation
        """
    def SetCriteriumWeight(self,W1 : float,W2 : float,W3 : float) -> None: 
        """
        define the Weights associed to the criterium used in the optimization.
        """
    def SetParType(self,ParType : OCP.Approx.Approx_ParametrizationType) -> None: 
        """
        Define the type of parametrization used in the approximation
        """
    def SurfPoles(self) -> OCP.TColgp.TColgp_Array2OfPnt: 
        """
        None
        """
    def SurfShape(self) -> Tuple[int, int, int, int, int, int]: 
        """
        None
        """
    def SurfUKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def SurfUMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def SurfVKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def SurfVMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def SurfWeights(self) -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        None
        """
    def Surface(self,TPoles : OCP.TColgp.TColgp_Array2OfPnt,TWeights : OCP.TColStd.TColStd_Array2OfReal,TUKnots : OCP.TColStd.TColStd_Array1OfReal,TVKnots : OCP.TColStd.TColStd_Array1OfReal,TUMults : OCP.TColStd.TColStd_Array1OfInteger,TVMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def TolCurveOnSurf(self,Index : int) -> float: 
        """
        None
        """
    def TolReached(self) -> Tuple[float, float]: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Degmin : int,Degmax : int,Tol3d : float,Tol2d : float,NbIt : int,KnownParameters : bool=False) -> None: ...
    pass
class GeomFill_ApproxStyle():
    """
    None

    Members:

      GeomFill_Section

      GeomFill_Location
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
    GeomFill_Location: OCP.GeomFill.GeomFill_ApproxStyle # value = GeomFill_ApproxStyle.GeomFill_Location
    GeomFill_Section: OCP.GeomFill.GeomFill_ApproxStyle # value = GeomFill_ApproxStyle.GeomFill_Section
    __entries: dict # value = {'GeomFill_Section': (GeomFill_ApproxStyle.GeomFill_Section, None), 'GeomFill_Location': (GeomFill_ApproxStyle.GeomFill_Location, None)}
    __members__: dict # value = {'GeomFill_Section': GeomFill_ApproxStyle.GeomFill_Section, 'GeomFill_Location': GeomFill_ApproxStyle.GeomFill_Location}
    pass
class GeomFill_Array1OfLocationLaw():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : GeomFill_Array1OfLocationLaw) -> GeomFill_Array1OfLocationLaw: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> GeomFill_LocationLaw: 
        """
        Returns first element
        """
    def ChangeLast(self) -> GeomFill_LocationLaw: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> GeomFill_LocationLaw: 
        """
        Variable value access
        """
    def First(self) -> GeomFill_LocationLaw: 
        """
        Returns first element
        """
    def Init(self,theValue : GeomFill_LocationLaw) -> None: 
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
    def Last(self) -> GeomFill_LocationLaw: 
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
    def Move(self,theOther : GeomFill_Array1OfLocationLaw) -> GeomFill_Array1OfLocationLaw: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : GeomFill_LocationLaw) -> None: 
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
    def Value(self,theIndex : int) -> GeomFill_LocationLaw: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : GeomFill_Array1OfLocationLaw) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : GeomFill_LocationLaw,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class GeomFill_Array1OfSectionLaw():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : GeomFill_Array1OfSectionLaw) -> GeomFill_Array1OfSectionLaw: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> GeomFill_SectionLaw: 
        """
        Returns first element
        """
    def ChangeLast(self) -> GeomFill_SectionLaw: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> GeomFill_SectionLaw: 
        """
        Variable value access
        """
    def First(self) -> GeomFill_SectionLaw: 
        """
        Returns first element
        """
    def Init(self,theValue : GeomFill_SectionLaw) -> None: 
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
    def Last(self) -> GeomFill_SectionLaw: 
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
    def Move(self,theOther : GeomFill_Array1OfSectionLaw) -> GeomFill_Array1OfSectionLaw: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : GeomFill_SectionLaw) -> None: 
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
    def Value(self,theIndex : int) -> GeomFill_SectionLaw: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : GeomFill_Array1OfSectionLaw) -> None: ...
    @overload
    def __init__(self,theBegin : GeomFill_SectionLaw,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class GeomFill_BSplineCurves():
    """
    An algorithm for constructing a BSpline surface filled from contiguous BSpline curves which form its boundaries. The algorithm accepts two, three or four BSpline curves as the boundaries of the target surface. A range of filling styles - more or less rounded, more or less flat - is available. A BSplineCurves object provides a framework for: - defining the boundaries, and the filling style of the surface - implementing the construction algorithm - consulting the result. Warning Some problems may show up with rational curves.
    """
    @overload
    def Init(self,C1 : OCP.Geom.Geom_BSplineCurve,C2 : OCP.Geom.Geom_BSplineCurve,C3 : OCP.Geom.Geom_BSplineCurve,C4 : OCP.Geom.Geom_BSplineCurve,Type : GeomFill_FillingStyle) -> None: 
        """
        if the curves cannot be joined

        if the curves cannot be joined

        Initializes or reinitializes this algorithm with two, three, or four curves - C1, C2, C3, and C4 - and Type, one of the following filling styles: - GeomFill_Stretch - the style with the flattest patch - GeomFill_Coons - a rounded style of patch with less depth than that of Curved - GeomFill_Curved - the style with the most rounded patch. Exceptions Standard_ConstructionError if the curves are not contiguous.
        """
    @overload
    def Init(self,C1 : OCP.Geom.Geom_BSplineCurve,C2 : OCP.Geom.Geom_BSplineCurve,C3 : OCP.Geom.Geom_BSplineCurve,Type : GeomFill_FillingStyle) -> None: ...
    @overload
    def Init(self,C1 : OCP.Geom.Geom_BSplineCurve,C2 : OCP.Geom.Geom_BSplineCurve,Type : GeomFill_FillingStyle) -> None: ...
    def Surface(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Returns the BSpline surface Surface resulting from the computation performed by this algorithm.

        Returns the BSpline surface Surface resulting from the computation performed by this algorithm.
        """
    @overload
    def __init__(self,C1 : OCP.Geom.Geom_BSplineCurve,C2 : OCP.Geom.Geom_BSplineCurve,C3 : OCP.Geom.Geom_BSplineCurve,Type : GeomFill_FillingStyle) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom.Geom_BSplineCurve,C2 : OCP.Geom.Geom_BSplineCurve,Type : GeomFill_FillingStyle) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom.Geom_BSplineCurve,C2 : OCP.Geom.Geom_BSplineCurve,C3 : OCP.Geom.Geom_BSplineCurve,C4 : OCP.Geom.Geom_BSplineCurve,Type : GeomFill_FillingStyle) -> None: ...
    pass
class GeomFill_BezierCurves():
    """
    This class provides an algorithm for constructing a Bezier surface filled from contiguous Bezier curves which form its boundaries. The algorithm accepts two, three or four Bezier curves as the boundaries of the target surface. A range of filling styles - more or less rounded, more or less flat - is available. A BezierCurves object provides a framework for: - defining the boundaries, and the filling style of the surface - implementing the construction algorithm - consulting the result. Warning Some problems may show up with rational curves.
    """
    @overload
    def Init(self,C1 : OCP.Geom.Geom_BezierCurve,C2 : OCP.Geom.Geom_BezierCurve,C3 : OCP.Geom.Geom_BezierCurve,C4 : OCP.Geom.Geom_BezierCurve,Type : GeomFill_FillingStyle) -> None: 
        """
        if the curves cannot be joined

        if the curves cannot be joined

        Initializes or reinitializes this algorithm with two, three, or four curves - C1, C2, C3, and C4 - and Type, one of the following filling styles: - GeomFill_Stretch - the style with the flattest patch - GeomFill_Coons - a rounded style of patch with less depth than that of Curved - GeomFill_Curved - the style with the most rounded patch. Exceptions Standard_ConstructionError if the curves are not contiguous.
        """
    @overload
    def Init(self,C1 : OCP.Geom.Geom_BezierCurve,C2 : OCP.Geom.Geom_BezierCurve,C3 : OCP.Geom.Geom_BezierCurve,Type : GeomFill_FillingStyle) -> None: ...
    @overload
    def Init(self,C1 : OCP.Geom.Geom_BezierCurve,C2 : OCP.Geom.Geom_BezierCurve,Type : GeomFill_FillingStyle) -> None: ...
    def Surface(self) -> OCP.Geom.Geom_BezierSurface: 
        """
        Returns the Bezier surface resulting from the computation performed by this algorithm.

        Returns the Bezier surface resulting from the computation performed by this algorithm.
        """
    @overload
    def __init__(self,C1 : OCP.Geom.Geom_BezierCurve,C2 : OCP.Geom.Geom_BezierCurve,C3 : OCP.Geom.Geom_BezierCurve,C4 : OCP.Geom.Geom_BezierCurve,Type : GeomFill_FillingStyle) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom.Geom_BezierCurve,C2 : OCP.Geom.Geom_BezierCurve,C3 : OCP.Geom.Geom_BezierCurve,Type : GeomFill_FillingStyle) -> None: ...
    @overload
    def __init__(self,C1 : OCP.Geom.Geom_BezierCurve,C2 : OCP.Geom.Geom_BezierCurve,Type : GeomFill_FillingStyle) -> None: ...
    pass
class GeomFill_Boundary(OCP.Standard.Standard_Transient):
    """
    Root class to define a boundary which will form part of a contour around a gap requiring filling. Any new type of constrained boundary must inherit this class. The GeomFill package provides two classes to define constrained boundaries: - GeomFill_SimpleBound to define an unattached boundary - GeomFill_BoundWithSurf to define a boundary attached to a surface. These objects are used to define the boundaries for a GeomFill_ConstrainedFilling framework.Root class to define a boundary which will form part of a contour around a gap requiring filling. Any new type of constrained boundary must inherit this class. The GeomFill package provides two classes to define constrained boundaries: - GeomFill_SimpleBound to define an unattached boundary - GeomFill_BoundWithSurf to define a boundary attached to a surface. These objects are used to define the boundaries for a GeomFill_ConstrainedFilling framework.Root class to define a boundary which will form part of a contour around a gap requiring filling. Any new type of constrained boundary must inherit this class. The GeomFill package provides two classes to define constrained boundaries: - GeomFill_SimpleBound to define an unattached boundary - GeomFill_BoundWithSurf to define a boundary attached to a surface. These objects are used to define the boundaries for a GeomFill_ConstrainedFilling framework.
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D1Norm(self,U : float,N : OCP.gp.gp_Vec,DN : OCP.gp.gp_Vec) -> None: 
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
    def HasNormals(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDegenerated(self) -> bool: 
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
    def Norm(self,U : float) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Points(self,PFirst : OCP.gp.gp_Pnt,PLast : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def Reparametrize(self,First : float,Last : float,HasDF : bool,HasDL : bool,DF : float,DL : float,Rev : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tol3d(self) -> float: 
        """
        None

        None
        """
    @overload
    def Tol3d(self,Tol : float) -> None: ...
    @overload
    def Tolang(self) -> float: 
        """
        None

        None
        """
    @overload
    def Tolang(self,Tol : float) -> None: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        None
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
class GeomFill_BoundWithSurf(GeomFill_Boundary, OCP.Standard.Standard_Transient):
    """
    Defines a 3d curve as a boundary for a GeomFill_ConstrainedFilling algorithm. This curve is attached to an existing surface. Defines a constrained boundary for filling the computations are done with a CurveOnSurf and a normals field defined by the normalized normal to the surface along the PCurve. Contains fields to allow a reparametrization of curve and normals field.Defines a 3d curve as a boundary for a GeomFill_ConstrainedFilling algorithm. This curve is attached to an existing surface. Defines a constrained boundary for filling the computations are done with a CurveOnSurf and a normals field defined by the normalized normal to the surface along the PCurve. Contains fields to allow a reparametrization of curve and normals field.Defines a 3d curve as a boundary for a GeomFill_ConstrainedFilling algorithm. This curve is attached to an existing surface. Defines a constrained boundary for filling the computations are done with a CurveOnSurf and a normals field defined by the normalized normal to the surface along the PCurve. Contains fields to allow a reparametrization of curve and normals field.
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D1Norm(self,U : float,N : OCP.gp.gp_Vec,DN : OCP.gp.gp_Vec) -> None: 
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
    def HasNormals(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDegenerated(self) -> bool: 
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
    def Norm(self,U : float) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Points(self,PFirst : OCP.gp.gp_Pnt,PLast : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def Reparametrize(self,First : float,Last : float,HasDF : bool,HasDL : bool,DF : float,DL : float,Rev : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tol3d(self) -> float: 
        """
        None

        None
        """
    @overload
    def Tol3d(self,Tol : float) -> None: ...
    @overload
    def Tolang(self) -> float: 
        """
        None

        None
        """
    @overload
    def Tolang(self,Tol : float) -> None: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def __init__(self,CurveOnSurf : OCP.Adaptor3d.Adaptor3d_CurveOnSurface,Tol3d : float,Tolang : float) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_CircularBlendFunc(OCP.Approx.Approx_SweepFunction, OCP.Standard.Standard_Transient):
    """
    Circular Blend Function to approximate by SweepApproximation from ApproxCircular Blend Function to approximate by SweepApproximation from ApproxCircular Blend Function to approximate by SweepApproximation from Approx
    """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditionned rational approximation.
        """
    def D0(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param
        """
    def D2(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param
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
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections. This information is usefull to perform well conditionned rational approximation.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
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
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the maximum section. This information is usefull to perform well conditionned rational approximation.
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        get the Multplicities of the section
        """
    def Nb2dCurves(self) -> int: 
        """
        get the number of 2d curves to approximate.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> This information is usfull to find an good tolerance in 2d approximation.
        """
    def SectionShape(self) -> Tuple[int, int, int]: 
        """
        get the format of an section
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the fonction This determines the derivatives in these values if the function is not Cn.
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usfull, if (me) have to be run numerical algorithme to perform D0, D1 or D2
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Path : OCP.Adaptor3d.Adaptor3d_HCurve,Curve1 : OCP.Adaptor3d.Adaptor3d_HCurve,Curve2 : OCP.Adaptor3d.Adaptor3d_HCurve,Radius : float,Polynomial : bool=False) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_TrihedronLaw(OCP.Standard.Standard_Transient):
    """
    To define Trihedron along one CurveTo define Trihedron along one CurveTo define Trihedron along one Curve
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon on curve at parameter <Param>
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon and derivative Trihedron on curve at parameter <Param> Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of M(t) and V(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Say if the law is Constant
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Say if the law is defined, only by the 3d Geometry of the setted Curve Return False by Default.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class GeomFill_ConstrainedFilling():
    """
    An algorithm for constructing a BSpline surface filled from a series of boundaries which serve as path constraints and optionally, as tangency constraints. The algorithm accepts three or four curves as the boundaries of the target surface. The only FillingStyle used is Coons. A ConstrainedFilling object provides a framework for: - defining the boundaries of the surface - implementing the construction algorithm - consulting the result. Warning This surface filling algorithm is specifically designed to be used in connection with fillets. Satisfactory results cannot be guaranteed for other uses.
    """
    def Boundary(self,I : int) -> GeomFill_Boundary: 
        """
        Returns the bound of index i after sort.
        """
    def CheckApprox(self,I : int) -> None: 
        """
        Computes values and normals along the bound I and compare them to the approx result curves (bound and tgte field) , draw the normals and tangents.
        """
    def CheckCoonsAlgPatch(self,I : int) -> None: 
        """
        Computes the fields of tangents on 30 points along the bound I, these are not the constraint tangents but gives an idea of the coonsAlgPatch regularity.
        """
    def CheckResult(self,I : int) -> None: 
        """
        Computes values and normals along the bound I on both constraint surface and result surface, draw the normals, and computes the max distance between values and the max angle between normals.
        """
    def CheckTgteField(self,I : int) -> None: 
        """
        Computes the fields of tangents and normals on 30 points along the bound I, draw them, and computes the max dot product that must be near than 0.
        """
    def Eval(self,W : float,Ord : int,Result : float) -> int: 
        """
        Internal use for Advmath approximation call.
        """
    @overload
    def Init(self,B1 : GeomFill_Boundary,B2 : GeomFill_Boundary,B3 : GeomFill_Boundary,NoCheck : bool=False) -> None: 
        """
        None

        Constructs a BSpline surface filled from the series of boundaries B1, B2, B3 and, if need be, B4, which serve: - as path constraints - and optionally, as tangency constraints if they are GeomFill_BoundWithSurf curves. The boundaries may be given in any order: they are classified and if necessary, reversed and reparameterized. The surface will also respect the following constraints: - its degree will not be greater than the maximum degree defined at the time of construction of this framework, and - the maximum number of segments MaxSeg which BSpline surfaces can have
        """
    @overload
    def Init(self,B1 : GeomFill_Boundary,B2 : GeomFill_Boundary,B3 : GeomFill_Boundary,B4 : GeomFill_Boundary,NoCheck : bool=False) -> None: ...
    def ReBuild(self) -> None: 
        """
        Computes the new poles of the surface using the new blending functions set by several calls to SetDomain.
        """
    def SetDomain(self,l : float,B : GeomFill_BoundWithSurf) -> None: 
        """
        Allows to modify domain on witch the blending function associated to the constrained boundary B will propag the influence of the field of tangency. Can be usefull to reduce influence of boundaries on whitch the Coons compatibility conditions are not respected. l is a relative value of the parametric range of B. Default value for l is 1 (used in Init). Warning: Must be called after Init with a constrained boundary used in the call to Init.
        """
    def Surface(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Returns the BSpline surface after computation of the fill by this framework.
        """
    def __init__(self,MaxDeg : int,MaxSeg : int) -> None: ...
    pass
class GeomFill_Filling():
    """
    Root class for Filling;
    """
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVPoles(self) -> int: 
        """
        None
        """
    def Poles(self,Poles : OCP.TColgp.TColgp_Array2OfPnt) -> None: 
        """
        None
        """
    def Weights(self,Weights : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    def isRational(self) -> bool: 
        """
        None
        """
    pass
class GeomFill_CoonsAlgPatch(OCP.Standard.Standard_Transient):
    """
    Provides evaluation methods on an algorithmic patch (based on 4 Curves) defined by its boundaries and blending functions.Provides evaluation methods on an algorithmic patch (based on 4 Curves) defined by its boundaries and blending functions.Provides evaluation methods on an algorithmic patch (based on 4 Curves) defined by its boundaries and blending functions.
    """
    def Bound(self,I : int) -> GeomFill_Boundary: 
        """
        None
        """
    def Corner(self,I : int) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def D1U(self,U : float,V : float) -> OCP.gp.gp_Vec: 
        """
        Computes the d/dU partial derivative on the algorithmic patch at parameters U and V.
        """
    def D1V(self,U : float,V : float) -> OCP.gp.gp_Vec: 
        """
        Computes the d/dV partial derivative on the algorithmic patch at parameters U and V.
        """
    def DUV(self,U : float,V : float) -> OCP.gp.gp_Vec: 
        """
        Computes the d2/dUdV partial derivative on the algorithmic patch made with linear blending functions at parameter U and V.
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
    @overload
    def Func(self,I : int) -> OCP.Law.Law_Function: 
        """
        None

        Give the blending functions.
        """
    @overload
    def Func(self,f1 : OCP.Law.Law_Function,f2 : OCP.Law.Law_Function) -> Any: ...
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
    def SetFunc(self,f1 : OCP.Law.Law_Function,f2 : OCP.Law.Law_Function) -> None: 
        """
        Set the blending functions.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the value on the algorithmic patch at parameters U and V.
        """
    def __init__(self,B1 : GeomFill_Boundary,B2 : GeomFill_Boundary,B3 : GeomFill_Boundary,B4 : GeomFill_Boundary) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_CornerState():
    """
    Class (should be a structure) storing the informations about continuity, normals parallelism, coons conditions and bounds tangents angle on the corner of contour to be filled.
    """
    def Constraint(self) -> None: 
        """
        None
        """
    def DoKill(self,Scal : float) -> None: 
        """
        None
        """
    @overload
    def Gap(self) -> float: 
        """
        None

        None
        """
    @overload
    def Gap(self,G : float) -> None: ...
    def HasConstraint(self) -> bool: 
        """
        None
        """
    def IsToKill(self,Scal : float) -> bool: 
        """
        None
        """
    @overload
    def NorAng(self) -> float: 
        """
        None

        None
        """
    @overload
    def NorAng(self,Ang : float) -> None: ...
    @overload
    def TgtAng(self,Ang : float) -> None: 
        """
        None

        None
        """
    @overload
    def TgtAng(self) -> float: ...
    def __init__(self) -> None: ...
    pass
class GeomFill_CorrectedFrenet(GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    """
    Defined an Corrected Frenet Trihedron Law It is like Frenet with an Torsion's minimizationDefined an Corrected Frenet Trihedron Law It is like Frenet with an Torsion's minimizationDefined an Corrected Frenet Trihedron Law It is like Frenet with an Torsion's minimization
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon on curve at parameter <Param>
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon and derivative Trihedron on curve at parameter <Param> Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def EvaluateBestMode(self) -> GeomFill_Trihedron: 
        """
        Tries to define the best trihedron mode for the curve. It can be: - Frenet - CorrectedFrenet - DiscreteTrihedron Warning: the CorrectedFrenet must be constructed with option ForEvaluation = True, the curve must be set by method SetCurve.
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of Tangent(t) and Normal(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Say if the law is Constant.
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Return True.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,ForEvaluation : bool) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_LocationLaw(OCP.Standard.Standard_Transient):
    """
    To define location law in Sweeping location is -- defined by an Matrix M and an Vector V, and transform an point P in MP+V.To define location law in Sweeping location is -- defined by an Matrix M and an Vector V, and transform an point P in MP+V.To define location law in Sweeping location is -- defined by an Matrix M and an Vector V, and transform an point P in MP+V.
    """
    def Copy(self) -> GeomFill_LocationLaw: 
        """
        None
        """
    @overload
    def D0(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec) -> bool: 
        """
        compute Location

        compute Location and 2d points
        """
    @overload
    def D0(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> bool: ...
    def D1(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,DM : OCP.gp.gp_Mat,DV : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        compute location 2d points and associated first derivatives. Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,DM : OCP.gp.gp_Mat,DV : OCP.gp.gp_Vec,D2M : OCP.gp.gp_Mat,D2V : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        compute location 2d points and associated first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,AM : OCP.gp.gp_Mat,AV : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of M(t) and V(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetCurve(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def GetDomain(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the function parametric domain. Warning: This domain it is not modified by the SetValue method
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetMaximalNorm(self) -> float: 
        """
        Get the maximum Norm of the matrix-location part. It is usful to find an good Tolerance to approx M(t).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstRestriction(self) -> bool: 
        """
        Say if the first restriction is defined in this class. If it is true the first element of poles array in D0,D1,D2... Correspond to this restriction. Returns Standard_False (default implementation)
        """
    def HasLastRestriction(self) -> bool: 
        """
        Say if the last restriction is defined in this class. If it is true the last element of poles array in D0,D1,D2... Correspond to this restriction. Returns Standard_False (default implementation)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
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
    def IsRotation(self,Error : float) -> bool: 
        """
        Say if the Location Law, is a rotation of Location The default implementation is " returns False ".
        """
    def IsTranslation(self,Error : float) -> bool: 
        """
        Say if the Location Law, is an translation of Location The default implementation is " returns False ".
        """
    def Nb2dCurves(self) -> int: 
        """
        get the number of 2d curves (Restrictions + Traces) to approximate.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> This information is usfull to find an good tolerance in 2d approximation.
        """
    def Rotation(self,Center : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usefull, if (me) have to run numerical algorithm to perform D0, D1 or D2 The default implementation make nothing.
        """
    def SetTrsf(self,Transfo : OCP.gp.gp_Mat) -> None: 
        """
        Set a transformation Matrix like the law M(t) become Mat * M(t)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceNumber(self) -> int: 
        """
        Give the number of trace (Curves 2d wich are not restriction) Returns 0 (default implementation)
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
class GeomFill_Curved(GeomFill_Filling):
    """
    None
    """
    @overload
    def Init(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Init(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def Init(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt,W1 : OCP.TColStd.TColStd_Array1OfReal,W2 : OCP.TColStd.TColStd_Array1OfReal,W3 : OCP.TColStd.TColStd_Array1OfReal,W4 : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Init(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,W1 : OCP.TColStd.TColStd_Array1OfReal,W2 : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVPoles(self) -> int: 
        """
        None
        """
    def Poles(self,Poles : OCP.TColgp.TColgp_Array2OfPnt) -> None: 
        """
        None
        """
    def Weights(self,Weights : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt,W1 : OCP.TColStd.TColStd_Array1OfReal,W2 : OCP.TColStd.TColStd_Array1OfReal,W3 : OCP.TColStd.TColStd_Array1OfReal,W4 : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,W1 : OCP.TColStd.TColStd_Array1OfReal,W2 : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    def isRational(self) -> bool: 
        """
        None
        """
    pass
class GeomFill_Darboux(GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    """
    Defines Darboux case of Frenet Trihedron LawDefines Darboux case of Frenet Trihedron LawDefines Darboux case of Frenet Trihedron Law
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon on curve at parameter <Param>
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon and derivative Trihedron on curve at parameter <Param> Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of Tangent(t) and Normal(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Say if the law is Constant.
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Return False.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
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
class GeomFill_DegeneratedBound(GeomFill_Boundary, OCP.Standard.Standard_Transient):
    """
    Description of a degenerated boundary (a point). Class defining a degenerated boundary for a constrained filling with a point and no other constraint. Only used to simulate an ordinary bound, may not be usefull and desapear soon.Description of a degenerated boundary (a point). Class defining a degenerated boundary for a constrained filling with a point and no other constraint. Only used to simulate an ordinary bound, may not be usefull and desapear soon.Description of a degenerated boundary (a point). Class defining a degenerated boundary for a constrained filling with a point and no other constraint. Only used to simulate an ordinary bound, may not be usefull and desapear soon.
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D1Norm(self,U : float,N : OCP.gp.gp_Vec,DN : OCP.gp.gp_Vec) -> None: 
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
    def HasNormals(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDegenerated(self) -> bool: 
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
    def Norm(self,U : float) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Points(self,PFirst : OCP.gp.gp_Pnt,PLast : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def Reparametrize(self,First : float,Last : float,HasDF : bool,HasDL : bool,DF : float,DL : float,Rev : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tol3d(self) -> float: 
        """
        None

        None
        """
    @overload
    def Tol3d(self,Tol : float) -> None: ...
    @overload
    def Tolang(self) -> float: 
        """
        None

        None
        """
    @overload
    def Tolang(self,Tol : float) -> None: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def __init__(self,Point : OCP.gp.gp_Pnt,First : float,Last : float,Tol3d : float,Tolang : float) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_DiscreteTrihedron(GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    """
    Defined Discrete Trihedron Law. The requirement for path curve is only G1. The result is C0-continuous surface that can be later approximated to C1.Defined Discrete Trihedron Law. The requirement for path curve is only G1. The result is C0-continuous surface that can be later approximated to C1.Defined Discrete Trihedron Law. The requirement for path curve is only G1. The result is C0-continuous surface that can be later approximated to C1.
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve at parameter <Param>
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron and derivative Trihedron on curve at parameter <Param> Warning : It used only for C1 or C2 aproximation For the moment it returns null values for DTangent, DNormal and DBiNormal.
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve first and seconde derivatives. Warning : It used only for C2 aproximation For the moment it returns null values for DTangent, DNormal DBiNormal, D2Tangent, D2Normal, D2BiNormal.
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of Tangent(t) and Normal(t) it is usful to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        None
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Say if the law is Constant.
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Return True.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
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
class GeomFill_DraftTrihedron(GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon and derivative Trihedron on curve at parameter <Param> Warning : It used only for C1 or C2 aproximation
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve first and seconde derivatives. Warning : It used only for C2 aproximation
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of Tangent(t) and Normal(t) it is usefull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Say if the law is Constant.
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Return True.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetAngle(self,Angle : float) -> None: 
        """
        None
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,BiNormal : OCP.gp.gp_Vec,Angle : float) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_SectionLaw(OCP.Standard.Standard_Transient):
    """
    To define section law in sweepingTo define section law in sweepingTo define section law in sweeping
    """
    def BSplineSurface(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        give if possible an bspline Surface, like iso-v are the section. If it is not possible this methode have to get an Null Surface. It is the default implementation.
        """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditioned rational approximation. Warning: Used only if <me> IsRational
        """
    def CirclSection(self,Param : float) -> OCP.Geom.Geom_Curve: 
        """
        Return the circle section at parameter <Param>, if <me> a IsConicalLaw
        """
    def ConstantSection(self) -> OCP.Geom.Geom_Curve: 
        """
        Return a copy of the constant Section, if me IsConstant
        """
    def D0(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param Warning : It used only for C2 aproximation
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
    def GetDomain(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the function parametric domain. Warning: This domain it is not modified by the SetValue method
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles in all sections. This information is usefull to control error in rational approximation. Warning: Used only if <me> IsRational
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerances associated at each poles to reach in approximation, to satisfy: BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConicalLaw(self,Error : float) -> bool: 
        """
        Returns True if all section are circle, with same plane,same center and linear radius evolution Return False by Default.
        """
    def IsConstant(self,Error : float) -> bool: 
        """
        Say if all sections are equals
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
    def IsRational(self) -> bool: 
        """
        Returns if the sections are rationnal or not
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns if the sections are periodic or not
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns if law is periodic or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the greater section. This information is usefull to G1's control. Warning: With an little value, approximation can be slower.
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        get the Multplicities of the section
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SectionShape(self) -> Tuple[int, int, int]: 
        """
        get the format of an section
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usefull, if (me) have to run numerical algorithm to perform D0, D1 or D2 The default implementation make nothing.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class GeomFill_Coons(GeomFill_Filling):
    """
    None
    """
    @overload
    def Init(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt,W1 : OCP.TColStd.TColStd_Array1OfReal,W2 : OCP.TColStd.TColStd_Array1OfReal,W3 : OCP.TColStd.TColStd_Array1OfReal,W4 : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVPoles(self) -> int: 
        """
        None
        """
    def Poles(self,Poles : OCP.TColgp.TColgp_Array2OfPnt) -> None: 
        """
        None
        """
    def Weights(self,Weights : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        None
        """
    @overload
    def __init__(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt,W1 : OCP.TColStd.TColStd_Array1OfReal,W2 : OCP.TColStd.TColStd_Array1OfReal,W3 : OCP.TColStd.TColStd_Array1OfReal,W4 : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    def isRational(self) -> bool: 
        """
        None
        """
    pass
class GeomFill_FillingStyle():
    """
    Defines the three filling styles used in this package - GeomFill_Stretch - the style with the flattest patches - GeomFill_Coons - a rounded style of patch with less depth than those of Curved - GeomFill_Curved - the style with the most rounded patches.

    Members:

      GeomFill_StretchStyle

      GeomFill_CoonsStyle

      GeomFill_CurvedStyle
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
    GeomFill_CoonsStyle: OCP.GeomFill.GeomFill_FillingStyle # value = GeomFill_FillingStyle.GeomFill_CoonsStyle
    GeomFill_CurvedStyle: OCP.GeomFill.GeomFill_FillingStyle # value = GeomFill_FillingStyle.GeomFill_CurvedStyle
    GeomFill_StretchStyle: OCP.GeomFill.GeomFill_FillingStyle # value = GeomFill_FillingStyle.GeomFill_StretchStyle
    __entries: dict # value = {'GeomFill_StretchStyle': (GeomFill_FillingStyle.GeomFill_StretchStyle, None), 'GeomFill_CoonsStyle': (GeomFill_FillingStyle.GeomFill_CoonsStyle, None), 'GeomFill_CurvedStyle': (GeomFill_FillingStyle.GeomFill_CurvedStyle, None)}
    __members__: dict # value = {'GeomFill_StretchStyle': GeomFill_FillingStyle.GeomFill_StretchStyle, 'GeomFill_CoonsStyle': GeomFill_FillingStyle.GeomFill_CoonsStyle, 'GeomFill_CurvedStyle': GeomFill_FillingStyle.GeomFill_CurvedStyle}
    pass
class GeomFill_Fixed(GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    """
    Defined an constant TrihedronLawDefined an constant TrihedronLawDefined an constant TrihedronLaw
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon on curve at parameter <Param>
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon and derivative Trihedron on curve at parameter <Param> Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of Tangent(t) and Normal(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Return True.
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Say if the law is defined, only by the 3d Geometry of the setted Curve Return False by Default.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_Frenet(GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    """
    Defined Frenet Trihedron LawDefined Frenet Trihedron LawDefined Frenet Trihedron Law
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon on curve at parameter <Param>
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon and derivative Trihedron on curve at parameter <Param> Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of Tangent(t) and Normal(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        None
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Say if the law is Constant.
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Return True.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
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
class GeomFill_FunctionDraft(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Deriv2T(self,C : OCP.Adaptor3d.Adaptor3d_HCurve,Param : float,W : float,d2N : OCP.gp.gp_Vec,teta : float,F : OCP.math.math_Vector) -> bool: 
        """
        returns the values <F> of the T2 derivatives for the parameter Param .
        """
    def Deriv2X(self,X : OCP.math.math_Vector,T : GeomFill_Tensor) -> bool: 
        """
        returns the values <T> of the X2 derivatives for the parameter Param .
        """
    def DerivT(self,C : OCP.Adaptor3d.Adaptor3d_HCurve,Param : float,W : float,dN : OCP.gp.gp_Vec,teta : float,F : OCP.math.math_Vector) -> bool: 
        """
        returns the values <F> of the T derivatives for the parameter Param .
        """
    def DerivTX(self,dN : OCP.gp.gp_Vec,teta : float,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the TX derivatives for the parameter Param .
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    pass
class GeomFill_FunctionGuide(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def DerivT(self,X : OCP.math.math_Vector,DCentre : OCP.gp.gp_XYZ,DDir : OCP.gp.gp_XYZ,DFDT : OCP.math.math_Vector) -> bool: 
        """
        returns the values <F> of the T derivatives for the parameter Param .
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function.
        """
    def SetParam(self,Param : float,Centre : OCP.gp.gp_Pnt,Dir : OCP.gp.gp_XYZ,XDir : OCP.gp.gp_XYZ) -> None: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S : GeomFill_SectionLaw,Guide : OCP.Adaptor3d.Adaptor3d_HCurve,ParamOnLaw : float=0.0) -> None: ...
    pass
class GeomFill_Profiler():
    """
    Evaluation of the common BSplineProfile of a group of curves from Geom. All the curves will have the same degree, the same knot-vector, so the same number of poles.
    """
    def AddCurve(self,Curve : OCP.Geom.Geom_Curve) -> None: 
        """
        None
        """
    def Curve(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    def Degree(self) -> int: 
        """
        Raises if not yet perform
        """
    def IsPeriodic(self) -> bool: 
        """
        None

        None
        """
    def KnotsAndMults(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Raises if not yet perform Raises if the lengthes of <Knots> and <Mults> are not equal to NbKnots().
        """
    def NbKnots(self) -> int: 
        """
        Raises if not yet perform
        """
    def NbPoles(self) -> int: 
        """
        Raises if not yet perform
        """
    def Perform(self,PTol : float) -> None: 
        """
        Converts all curves to BSplineCurves. Set them to the common profile. <PTol> is used to compare 2 knots.
        """
    def Poles(self,Index : int,Poles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        returns in <Poles> the poles of the BSplineCurve from index <Index> adjusting to the current profile. Raises if not yet perform Raises if <Index> not in the range [1,NbCurves] if the length of <Poles> is not equal to NbPoles().
        """
    def Weights(self,Index : int,Weights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        returns in <Weights> the weights of the BSplineCurve from index <Index> adjusting to the current profile. Raises if not yet perform Raises if <Index> not in the range [1,NbCurves] or if the length of <Weights> is not equal to NbPoles().
        """
    def __init__(self) -> None: ...
    pass
class GeomFill_TrihedronWithGuide(GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    """
    To define Trihedron along one Curve with a guideTo define Trihedron along one Curve with a guideTo define Trihedron along one Curve with a guide
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def CurrentPointOnGuide(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the current point on guide found by D0, D1 or D2.
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon on curve at parameter <Param>
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Triedrhon and derivative Trihedron on curve at parameter <Param> Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of M(t) and V(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Guide(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Say if the law is Constant
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Say if the law is defined, only by the 3d Geometry of the setted Curve Return False by Default.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def Origine(self,Param1 : float,Param2 : float) -> None: 
        """
        None
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class GeomFill_GuideTrihedronPlan(GeomFill_TrihedronWithGuide, GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    """
    Trihedron in the case of sweeping along a guide curve defined by the orthogonal plan on the trajectoryTrihedron in the case of sweeping along a guide curve defined by the orthogonal plan on the trajectoryTrihedron in the case of sweeping along a guide curve defined by the orthogonal plan on the trajectory
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def CurrentPointOnGuide(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the current point on guide found by D0, D1 or D2.
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of M(t) and V(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Guide(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Say if the law is Constant
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Say if the law is defined, only by the 3d Geometry of the setted Curve Return False by Default.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def Origine(self,OrACR1 : float,OrACR2 : float) -> None: 
        """
        None
        """
    def SetCurve(self,thePath : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theGuide : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_HArray1OfLocationLaw(GeomFill_Array1OfLocationLaw, OCP.Standard.Standard_Transient):
    def Array1(self) -> GeomFill_Array1OfLocationLaw: 
        """
        None
        """
    def Assign(self,theOther : GeomFill_Array1OfLocationLaw) -> GeomFill_Array1OfLocationLaw: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> GeomFill_Array1OfLocationLaw: 
        """
        None
        """
    def ChangeFirst(self) -> GeomFill_LocationLaw: 
        """
        Returns first element
        """
    def ChangeLast(self) -> GeomFill_LocationLaw: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> GeomFill_LocationLaw: 
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
    def First(self) -> GeomFill_LocationLaw: 
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
    def Init(self,theValue : GeomFill_LocationLaw) -> None: 
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
    def Last(self) -> GeomFill_LocationLaw: 
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
    def Move(self,theOther : GeomFill_Array1OfLocationLaw) -> GeomFill_Array1OfLocationLaw: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : GeomFill_LocationLaw) -> None: 
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
    def Value(self,theIndex : int) -> GeomFill_LocationLaw: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : GeomFill_LocationLaw) -> None: ...
    @overload
    def __init__(self,theOther : GeomFill_Array1OfLocationLaw) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
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
class GeomFill_HArray1OfSectionLaw(GeomFill_Array1OfSectionLaw, OCP.Standard.Standard_Transient):
    def Array1(self) -> GeomFill_Array1OfSectionLaw: 
        """
        None
        """
    def Assign(self,theOther : GeomFill_Array1OfSectionLaw) -> GeomFill_Array1OfSectionLaw: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> GeomFill_Array1OfSectionLaw: 
        """
        None
        """
    def ChangeFirst(self) -> GeomFill_SectionLaw: 
        """
        Returns first element
        """
    def ChangeLast(self) -> GeomFill_SectionLaw: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> GeomFill_SectionLaw: 
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
    def First(self) -> GeomFill_SectionLaw: 
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
    def Init(self,theValue : GeomFill_SectionLaw) -> None: 
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
    def Last(self) -> GeomFill_SectionLaw: 
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
    def Move(self,theOther : GeomFill_Array1OfSectionLaw) -> GeomFill_Array1OfSectionLaw: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : GeomFill_SectionLaw) -> None: 
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
    def Value(self,theIndex : int) -> GeomFill_SectionLaw: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : GeomFill_SectionLaw) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : GeomFill_Array1OfSectionLaw) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
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
class GeomFill_SequenceOfAx2(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.gp.gp_Ax2) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : GeomFill_SequenceOfAx2) -> None: ...
    def Assign(self,theOther : GeomFill_SequenceOfAx2) -> GeomFill_SequenceOfAx2: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.gp.gp_Ax2: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.gp.gp_Ax2: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_Ax2: 
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
    def First(self) -> OCP.gp.gp_Ax2: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.gp.gp_Ax2) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : GeomFill_SequenceOfAx2) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : GeomFill_SequenceOfAx2) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.gp.gp_Ax2) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.gp.gp_Ax2: 
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
    def Prepend(self,theItem : OCP.gp.gp_Ax2) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : GeomFill_SequenceOfAx2) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_Ax2) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : GeomFill_SequenceOfAx2) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.gp.gp_Ax2: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : GeomFill_SequenceOfAx2) -> None: ...
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
class GeomFill_Line(OCP.Standard.Standard_Transient):
    """
    class for instantiation of AppBlendclass for instantiation of AppBlendclass for instantiation of AppBlend
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
    def NbPoints(self) -> int: 
        """
        None

        None
        """
    def Point(self,Index : int) -> int: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,NbPoints : int) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_LocFunction():
    """
    None
    """
    def D0(self,Param : float,First : float,Last : float) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,First : float,Last : float) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param
        """
    def D2(self,Param : float,First : float,Last : float) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param
        """
    def DN(self,Param : float,First : float,Last : float,Order : int) -> Tuple[float, int]: 
        """
        None
        """
    def __init__(self,Law : GeomFill_LocationLaw) -> None: ...
    pass
class GeomFill_LocationDraft(GeomFill_LocationLaw, OCP.Standard.Standard_Transient):
    def Copy(self) -> GeomFill_LocationLaw: 
        """
        None
        """
    @overload
    def D0(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec) -> bool: 
        """
        compute Location

        compute Location and 2d points
        """
    @overload
    def D0(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> bool: ...
    def D1(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,DM : OCP.gp.gp_Mat,DV : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        compute location 2d points and associated first derivatives. Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,DM : OCP.gp.gp_Mat,DV : OCP.gp.gp_Vec,D2M : OCP.gp.gp_Mat,D2V : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        compute location 2d points and associated first and seconde derivatives. Warning : It used only for C2 aproximation
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,AM : OCP.gp.gp_Mat,AV : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of M(t) and V(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetCurve(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def GetDomain(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the function parametric domain. Warning: This domain it is not modified by the SetValue method
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetMaximalNorm(self) -> float: 
        """
        Get the maximum Norm of the matrix-location part. It is usful to find an good Tolerance to approx M(t).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstRestriction(self) -> bool: 
        """
        Say if the first restriction is defined in this class. If it is true the first element of poles array in D0,D1,D2... Correspond to this restriction. Returns Standard_False (default implementation)
        """
    def HasLastRestriction(self) -> bool: 
        """
        Say if the last restriction is defined in this class. If it is true the last element of poles array in D0,D1,D2... Correspond to this restriction. Returns Standard_False (default implementation)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsIntersec(self) -> bool: 
        """
        Say if the generatrice interset the surface
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsRotation(self,Error : float) -> bool: 
        """
        Say if the Location Law, is a rotation of Location The default implementation is " returns False ".
        """
    def IsTranslation(self,Error : float) -> bool: 
        """
        Say if the Location Law, is an translation of Location The default implementation is " returns False ".
        """
    def Nb2dCurves(self) -> int: 
        """
        get the number of 2d curves (Restrictions + Traces) to approximate.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> This information is usfull to find an good tolerance in 2d approximation. Warning: Used only if Nb2dCurve > 0
        """
    def Rotation(self,Center : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def SetAngle(self,Angle : float) -> None: 
        """
        None
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def SetStopSurf(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: 
        """
        None
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usefull, if (me) have to run numerical algorithm to perform D0, D1 or D2 The default implementation make nothing.
        """
    def SetTrsf(self,Transfo : OCP.gp.gp_Mat) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceNumber(self) -> int: 
        """
        Give the number of trace (Curves 2d wich are not restriction) Returns 1 (default implementation)
        """
    def __init__(self,Direction : OCP.gp.gp_Dir,Angle : float) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_LocationGuide(GeomFill_LocationLaw, OCP.Standard.Standard_Transient):
    def ComputeAutomaticLaw(self,ParAndRad : OCP.TColgp.TColgp_HArray1OfPnt2d) -> GeomFill_PipeError: 
        """
        None
        """
    def Copy(self) -> GeomFill_LocationLaw: 
        """
        None
        """
    @overload
    def D0(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec) -> bool: 
        """
        compute Location

        compute Location and 2d points
        """
    @overload
    def D0(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> bool: ...
    def D1(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,DM : OCP.gp.gp_Mat,DV : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        compute location 2d points and associated first derivatives. Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,DM : OCP.gp.gp_Mat,DV : OCP.gp.gp_Vec,D2M : OCP.gp.gp_Mat,D2V : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        compute location 2d points and associated first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def EraseRotation(self) -> None: 
        """
        None
        """
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,AM : OCP.gp.gp_Mat,AV : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of M(t) and V(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetCurve(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def GetDomain(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the function parametric domain. Warning: This domain it is not modified by the SetValue method
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetMaximalNorm(self) -> float: 
        """
        Get the maximum Norm of the matrix-location part. It is usful to find an good Tolerance to approx M(t).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Guide(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def HasFirstRestriction(self) -> bool: 
        """
        Say if the first restriction is defined in this class. If it is true the first element of poles array in D0,D1,D2... Correspond to this restriction. Returns Standard_False (default implementation)
        """
    def HasLastRestriction(self) -> bool: 
        """
        Say if the last restriction is defined in this class. If it is true the last element of poles array in D0,D1,D2... Correspond to this restriction. Returns Standard_False (default implementation)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
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
    def IsRotation(self,Error : float) -> bool: 
        """
        Say if the Location Law, is a rotation of Location The default implementation is " returns False ".
        """
    def IsTranslation(self,Error : float) -> bool: 
        """
        Say if the Location Law, is an translation of Location The default implementation is " returns False ".
        """
    def Nb2dCurves(self) -> int: 
        """
        get the number of 2d curves (Restrictions + Traces) to approximate.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> This information is usfull to find an good tolerance in 2d approximation. Warning: Used only if Nb2dCurve > 0
        """
    def Rotation(self,Center : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def Section(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def Set(self,Section : GeomFill_SectionLaw,rotat : bool,SFirst : float,SLast : float,PrecAngle : float) -> Tuple[float]: 
        """
        None
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def SetOrigine(self,Param1 : float,Param2 : float) -> None: 
        """
        None
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usefull, if (me) have to run numerical algorithm to perform D0, D1 or D2 The default implementation make nothing.
        """
    def SetTrsf(self,Transfo : OCP.gp.gp_Mat) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceNumber(self) -> int: 
        """
        Give the number of trace (Curves 2d wich are not restriction) Returns 1 (default implementation)
        """
    def __init__(self,Triedre : GeomFill_TrihedronWithGuide) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_CurveAndTrihedron(GeomFill_LocationLaw, OCP.Standard.Standard_Transient):
    """
    Define location law with an TrihedronLaw and an curve Definition Location is : transformed section coordinates in (Curve(v)), (Normal(v), BiNormal(v), Tangente(v))) systeme are the same like section shape coordinates in (O,(OX, OY, OZ)) systeme.Define location law with an TrihedronLaw and an curve Definition Location is : transformed section coordinates in (Curve(v)), (Normal(v), BiNormal(v), Tangente(v))) systeme are the same like section shape coordinates in (O,(OX, OY, OZ)) systeme.Define location law with an TrihedronLaw and an curve Definition Location is : transformed section coordinates in (Curve(v)), (Normal(v), BiNormal(v), Tangente(v))) systeme are the same like section shape coordinates in (O,(OX, OY, OZ)) systeme.
    """
    def Copy(self) -> GeomFill_LocationLaw: 
        """
        None
        """
    @overload
    def D0(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec) -> bool: 
        """
        compute Location and 2d points

        compute Location and 2d points
        """
    @overload
    def D0(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d) -> bool: ...
    def D1(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,DM : OCP.gp.gp_Mat,DV : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        compute location 2d points and associated first derivatives. Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,M : OCP.gp.gp_Mat,V : OCP.gp.gp_Vec,DM : OCP.gp.gp_Mat,DV : OCP.gp.gp_Vec,D2M : OCP.gp.gp_Mat,D2V : OCP.gp.gp_Vec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d) -> bool: 
        """
        compute location 2d points and associated first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,AM : OCP.gp.gp_Mat,AV : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of M(t) and V(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetCurve(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def GetDomain(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the function parametric domain. Warning: This domain it is not modified by the SetValue method
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetMaximalNorm(self) -> float: 
        """
        Get the maximum Norm of the matrix-location part. It is usful to find an good Tolerance to approx M(t).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstRestriction(self) -> bool: 
        """
        Say if the first restriction is defined in this class. If it is true the first element of poles array in D0,D1,D2... Correspond to this restriction. Returns Standard_False (default implementation)
        """
    def HasLastRestriction(self) -> bool: 
        """
        Say if the last restriction is defined in this class. If it is true the last element of poles array in D0,D1,D2... Correspond to this restriction. Returns Standard_False (default implementation)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
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
    def IsRotation(self,Error : float) -> bool: 
        """
        Say if the Location Law, is a rotation of Location The default implementation is " returns False ".
        """
    def IsTranslation(self,Error : float) -> bool: 
        """
        Say if the Location Law, is an translation of Location The default implementation is " returns False ".
        """
    def Nb2dCurves(self) -> int: 
        """
        get the number of 2d curves (Restrictions + Traces) to approximate.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> This information is usfull to find an good tolerance in 2d approximation.
        """
    def Rotation(self,Center : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usefull, if (me) have to run numerical algorithm to perform D0, D1 or D2 The default implementation make nothing.
        """
    def SetTrsf(self,Transfo : OCP.gp.gp_Mat) -> None: 
        """
        Set a transformation Matrix like the law M(t) become Mat * M(t)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TraceNumber(self) -> int: 
        """
        Give the number of trace (Curves 2d wich are not restriction) Returns 0 (default implementation)
        """
    def __init__(self,Trihedron : GeomFill_TrihedronLaw) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_NSections(GeomFill_SectionLaw, OCP.Standard.Standard_Transient):
    """
    Define a Section Law by N SectionsDefine a Section Law by N SectionsDefine a Section Law by N Sections
    """
    def BSplineSurface(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        give if possible an bspline Surface, like iso-v are the section. If it is not possible this methode have to get an Null Surface. Is it the default implementation.
        """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditioned rational approximation. Warning: Used only if <me> IsRational
        """
    def CirclSection(self,Param : float) -> OCP.Geom.Geom_Curve: 
        """
        Return the circle section at parameter <Param>, if <me> a IsConicalLaw
        """
    def ComputeSurface(self) -> None: 
        """
        Computes the surface
        """
    def ConstantSection(self) -> OCP.Geom.Geom_Curve: 
        """
        Return the constant Section if <me> IsConstant.
        """
    def D0(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param Warning : It used only for C2 aproximation
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
    def GetDomain(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the function parametric domain. Warning: This domain it is not modified by the SetValue method
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles in all sections. This information is usefull to control error in rational approximation. Warning: Used only if <me> IsRational
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerances associated at each poles to reach in approximation, to satisfy: BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConicalLaw(self,Error : float) -> bool: 
        """
        Returns True if all section are circle, with same plane,same center and linear radius evolution Return False by Default.
        """
    def IsConstant(self,Error : float) -> bool: 
        """
        return True If the Law isConstant
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
    def IsRational(self) -> bool: 
        """
        Returns if the sections are rationnal or not
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns if the sections are periodic or not
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns if the law isperiodic or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the greater section. This information is usefull to G1's control. Warning: With an little value, approximation can be slower.
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        get the Multplicities of the section
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SectionShape(self) -> Tuple[int, int, int]: 
        """
        get the format of an section
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def SetSurface(self,RefSurf : OCP.Geom.Geom_BSplineSurface) -> None: 
        """
        Sets the reference surface
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usefull, if (me) have to run numerical algorithm to perform D0, D1 or D2 The default implementation make nothing.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,NC : OCP.TColGeom.TColGeom_SequenceOfCurve,NP : OCP.TColStd.TColStd_SequenceOfReal,UF : float,UL : float,VF : float,VL : float) -> None: ...
    @overload
    def __init__(self,NC : OCP.TColGeom.TColGeom_SequenceOfCurve,Trsfs : GeomFill_SequenceOfTrsf,NP : OCP.TColStd.TColStd_SequenceOfReal,UF : float,UL : float,VF : float,VL : float,Surf : OCP.Geom.Geom_BSplineSurface) -> None: ...
    @overload
    def __init__(self,NC : OCP.TColGeom.TColGeom_SequenceOfCurve,NP : OCP.TColStd.TColStd_SequenceOfReal) -> None: ...
    @overload
    def __init__(self,NC : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_Pipe():
    """
    Describes functions to construct pipes. A pipe is built by sweeping a curve (the section) along another curve (the path). The Pipe class provides the following types of construction: - pipes with a circular section of constant radius, - pipes with a constant section, - pipes with a section evolving between two given curves. All standard specific cases are detected in order to build, where required, a plane, cylinder, cone, sphere, torus, surface of linear extrusion or surface of revolution. Generally speaking, the result is a BSpline surface (NURBS). A Pipe object provides a framework for: - defining the pipe to be built, - implementing the construction algorithm, and - consulting the resulting surface. There are several methods to instantiate a Pipe: 1) give a path and a radius : the section is a circle. This location is the first point of the path, and this direction is the first derivate (calculate at the first point ) of the path.
    """
    def ErrorOnSurf(self) -> float: 
        """
        Returns the approximation's error. if the Surface is plane, cylinder ... this error can be 0.

        Returns the approximation's error. if the Surface is plane, cylinder ... this error can be 0.
        """
    def ExchangeUV(self) -> bool: 
        """
        The u parametric direction of the surface constructed by this algorithm usually corresponds to the evolution along the path and the v parametric direction corresponds to the evolution along the section(s). However, this rule is not respected when constructing certain specific Geom surfaces (typically cylindrical surfaces, surfaces of revolution, etc.) for which the parameterization is inversed. The ExchangeUV function checks for this, and returns true in all these specific cases. Warning Do not use this function before the surface is built.

        The u parametric direction of the surface constructed by this algorithm usually corresponds to the evolution along the path and the v parametric direction corresponds to the evolution along the section(s). However, this rule is not respected when constructing certain specific Geom surfaces (typically cylindrical surfaces, surfaces of revolution, etc.) for which the parameterization is inversed. The ExchangeUV function checks for this, and returns true in all these specific cases. Warning Do not use this function before the surface is built.
        """
    @overload
    def GenerateParticularCase(self,B : bool) -> None: 
        """
        Sets a flag to try to create as many planes, cylinder,... as possible. Default value is <Standard_False>.

        Returns the flag.

        Sets a flag to try to create as many planes, cylinder,... as possible. Default value is <Standard_False>.

        Returns the flag.
        """
    @overload
    def GenerateParticularCase(self) -> bool: ...
    @overload
    def Init(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve,LastSect : OCP.Geom.Geom_Curve) -> None: 
        """
        None

        None

        None

        None

        None

        None

        Create a pipe with a constant radius with 2 guide-line.

        Initializes this pipe algorithm to build the following surface: - a pipe with a constant circular section of radius Radius along the path Path, or - a pipe with constant section FirstSect along the path Path, or - a pipe where the section evolves from FirstSect to LastSect along the path Path. Use the function Perform to build the surface. Note: a description of the resulting surface is given under Constructors.
        """
    @overload
    def Init(self,Path : OCP.Adaptor3d.Adaptor3d_HCurve,Curve1 : OCP.Adaptor3d.Adaptor3d_HCurve,Curve2 : OCP.Adaptor3d.Adaptor3d_HCurve,Radius : float) -> None: ...
    @overload
    def Init(self,Path : OCP.Geom2d.Geom2d_Curve,Support : OCP.Geom.Geom_Surface,FirstSect : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def Init(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve,Dir : OCP.gp.gp_Dir) -> None: ...
    @overload
    def Init(self,Path : OCP.Geom.Geom_Curve,Radius : float) -> None: ...
    @overload
    def Init(self,Path : OCP.Geom.Geom_Curve,NSections : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: ...
    @overload
    def Init(self,Path : OCP.Geom.Geom_Curve,Guide : OCP.Adaptor3d.Adaptor3d_HCurve,FirstSect : OCP.Geom.Geom_Curve,ByACR : bool,rotat : bool) -> None: ...
    @overload
    def Init(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve,Option : GeomFill_Trihedron=GeomFill_Trihedron.GeomFill_IsCorrectedFrenet) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns whether approximation was done.

        Returns whether approximation was done.
        """
    @overload
    def Perform(self,WithParameters : bool=False,myPolynomial : bool=False) -> None: 
        """
        Builds the pipe defined at the time of initialization of this algorithm. A description of the resulting surface is given under Constructors. If WithParameters (defaulted to false) is set to true, the approximation algorithm (used only in the general case of construction of a BSpline surface) builds the surface with a u parameter corresponding to the one of the path. Exceptions Standard_ConstructionError if a surface cannot be constructed from the data. Warning: It is the old Perform method, the next methode is recommended.

        detects the particular cases. And compute the surface. if none particular case is detected we make an approximation with respect of the Tolerance <Tol>, the continuty <Conti>, the maximum degree <MaxDegree>, the maximum number of span <NbMaxSegment> and the spine parametrization. If we can't create a surface with the data
        """
    @overload
    def Perform(self,Tol : float,Polynomial : bool,Conti : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1,MaxDegree : int=11,NbMaxSegment : int=30) -> None: ...
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        Returns the surface built by this algorithm. Warning Do not use this function before the surface is built (in this case the function will return a null handle).

        Returns the surface built by this algorithm. Warning Do not use this function before the surface is built (in this case the function will return a null handle).
        """
    @overload
    def __init__(self,Path : OCP.Adaptor3d.Adaptor3d_HCurve,Curve1 : OCP.Adaptor3d.Adaptor3d_HCurve,Curve2 : OCP.Adaptor3d.Adaptor3d_HCurve,Radius : float) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve,LastSect : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve,Dir : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom2d.Geom2d_Curve,Support : OCP.Geom.Geom_Surface,FirstSect : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,NSections : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,Curve1 : OCP.Geom.Geom_Curve,Curve2 : OCP.Geom.Geom_Curve,Radius : float) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,Radius : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,Guide : OCP.Adaptor3d.Adaptor3d_HCurve,FirstSect : OCP.Geom.Geom_Curve,ByACR : bool,rotat : bool) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve,Option : GeomFill_Trihedron=GeomFill_Trihedron.GeomFill_IsCorrectedFrenet) -> None: ...
    pass
class GeomFill_PipeError():
    """
    None

    Members:

      GeomFill_PipeOk

      GeomFill_PipeNotOk

      GeomFill_PlaneNotIntersectGuide

      GeomFill_ImpossibleContact
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
    GeomFill_ImpossibleContact: OCP.GeomFill.GeomFill_PipeError # value = GeomFill_PipeError.GeomFill_ImpossibleContact
    GeomFill_PipeNotOk: OCP.GeomFill.GeomFill_PipeError # value = GeomFill_PipeError.GeomFill_PipeNotOk
    GeomFill_PipeOk: OCP.GeomFill.GeomFill_PipeError # value = GeomFill_PipeError.GeomFill_PipeOk
    GeomFill_PlaneNotIntersectGuide: OCP.GeomFill.GeomFill_PipeError # value = GeomFill_PipeError.GeomFill_PlaneNotIntersectGuide
    __entries: dict # value = {'GeomFill_PipeOk': (GeomFill_PipeError.GeomFill_PipeOk, None), 'GeomFill_PipeNotOk': (GeomFill_PipeError.GeomFill_PipeNotOk, None), 'GeomFill_PlaneNotIntersectGuide': (GeomFill_PipeError.GeomFill_PlaneNotIntersectGuide, None), 'GeomFill_ImpossibleContact': (GeomFill_PipeError.GeomFill_ImpossibleContact, None)}
    __members__: dict # value = {'GeomFill_PipeOk': GeomFill_PipeError.GeomFill_PipeOk, 'GeomFill_PipeNotOk': GeomFill_PipeError.GeomFill_PipeNotOk, 'GeomFill_PlaneNotIntersectGuide': GeomFill_PipeError.GeomFill_PlaneNotIntersectGuide, 'GeomFill_ImpossibleContact': GeomFill_PipeError.GeomFill_ImpossibleContact}
    pass
class GeomFill_PlanFunc(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def D2(self,X : float) -> Tuple[float, float, float]: 
        """
        None
        """
    def D2E(self,X : float,DP : OCP.gp.gp_Vec,D2P : OCP.gp.gp_Vec,DV : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec) -> Tuple[float, float, float]: 
        """
        None
        """
    def DEDT(self,X : float,DP : OCP.gp.gp_Vec,DV : OCP.gp.gp_Vec) -> Tuple[float]: 
        """
        None
        """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        computes the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        computes the value <F>of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        computes the value <F> and the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def __init__(self,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    pass
class GeomFill_PolynomialConvertor():
    """
    To convert circular section in polynome
    """
    def Init(self) -> None: 
        """
        None
        """
    def Initialized(self) -> bool: 
        """
        say if <me> is Initialized
        """
    @overload
    def Section(self,FirstPnt : OCP.gp.gp_Pnt,Center : OCP.gp.gp_Pnt,Dir : OCP.gp.gp_Vec,Angle : float,Poles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Section(self,FirstPnt : OCP.gp.gp_Pnt,DFirstPnt : OCP.gp.gp_Vec,Center : OCP.gp.gp_Pnt,DCenter : OCP.gp.gp_Vec,Dir : OCP.gp.gp_Vec,DDir : OCP.gp.gp_Vec,Angle : float,DAngle : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec) -> None: ...
    @overload
    def Section(self,FirstPnt : OCP.gp.gp_Pnt,DFirstPnt : OCP.gp.gp_Vec,D2FirstPnt : OCP.gp.gp_Vec,Center : OCP.gp.gp_Pnt,DCenter : OCP.gp.gp_Vec,D2Center : OCP.gp.gp_Vec,Dir : OCP.gp.gp_Vec,DDir : OCP.gp.gp_Vec,D2Dir : OCP.gp.gp_Vec,Angle : float,DAngle : float,D2Angle : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec) -> None: ...
    def __init__(self) -> None: ...
    pass
class GeomFill_Generator(GeomFill_Profiler):
    """
    Create a surface using generating lines. Inherits profiler. The surface will be a BSplineSurface passing by all the curves described in the generator. The VDegree of the resulting surface is 1.
    """
    def AddCurve(self,Curve : OCP.Geom.Geom_Curve) -> None: 
        """
        None
        """
    def Curve(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    def Degree(self) -> int: 
        """
        Raises if not yet perform
        """
    def IsPeriodic(self) -> bool: 
        """
        None

        None
        """
    def KnotsAndMults(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Raises if not yet perform Raises if the lengthes of <Knots> and <Mults> are not equal to NbKnots().
        """
    def NbKnots(self) -> int: 
        """
        Raises if not yet perform
        """
    def NbPoles(self) -> int: 
        """
        Raises if not yet perform
        """
    def Perform(self,PTol : float) -> None: 
        """
        Converts all curves to BSplineCurves. Set them to the common profile. Compute the surface (degv = 1). <PTol> is used to compare 2 knots.
        """
    def Poles(self,Index : int,Poles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        returns in <Poles> the poles of the BSplineCurve from index <Index> adjusting to the current profile. Raises if not yet perform Raises if <Index> not in the range [1,NbCurves] if the length of <Poles> is not equal to NbPoles().
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None

        None
        """
    def Weights(self,Index : int,Weights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        returns in <Weights> the weights of the BSplineCurve from index <Index> adjusting to the current profile. Raises if not yet perform Raises if <Index> not in the range [1,NbCurves] or if the length of <Weights> is not equal to NbPoles().
        """
    def __init__(self) -> None: ...
    pass
class GeomFill_QuasiAngularConvertor():
    """
    To convert circular section in QuasiAngular Bezier form
    """
    def Init(self) -> None: 
        """
        None
        """
    def Initialized(self) -> bool: 
        """
        say if <me> is Initialized
        """
    @overload
    def Section(self,FirstPnt : OCP.gp.gp_Pnt,Center : OCP.gp.gp_Pnt,Dir : OCP.gp.gp_Vec,Angle : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Section(self,FirstPnt : OCP.gp.gp_Pnt,DFirstPnt : OCP.gp.gp_Vec,Center : OCP.gp.gp_Pnt,DCenter : OCP.gp.gp_Vec,Dir : OCP.gp.gp_Vec,DDir : OCP.gp.gp_Vec,Angle : float,DAngle : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Weights : OCP.TColStd.TColStd_Array1OfReal,DWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,FirstPnt : OCP.gp.gp_Pnt,DFirstPnt : OCP.gp.gp_Vec,D2FirstPnt : OCP.gp.gp_Vec,Center : OCP.gp.gp_Pnt,DCenter : OCP.gp.gp_Vec,D2Center : OCP.gp.gp_Vec,Dir : OCP.gp.gp_Vec,DDir : OCP.gp.gp_Vec,D2Dir : OCP.gp.gp_Vec,Angle : float,DAngle : float,D2Angle : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Weights : OCP.TColStd.TColStd_Array1OfReal,DWeights : OCP.TColStd.TColStd_Array1OfReal,D2Weights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    def __init__(self) -> None: ...
    pass
class GeomFill_SectionGenerator(GeomFill_Profiler):
    """
    gives the functions needed for instantiation from AppSurf in AppBlend. Allow to evaluate a surface passing by all the curves if the Profiler.
    """
    def AddCurve(self,Curve : OCP.Geom.Geom_Curve) -> None: 
        """
        None
        """
    def Curve(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    def Degree(self) -> int: 
        """
        Raises if not yet perform
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None

        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def KnotsAndMults(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Raises if not yet perform Raises if the lengthes of <Knots> and <Mults> are not equal to NbKnots().
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbKnots(self) -> int: 
        """
        Raises if not yet perform
        """
    def NbPoles(self) -> int: 
        """
        Raises if not yet perform
        """
    def Parameter(self,P : int) -> float: 
        """
        Returns the parameter of Section<P>, to impose it for the approximation.
        """
    def Perform(self,PTol : float) -> None: 
        """
        Converts all curves to BSplineCurves. Set them to the common profile. <PTol> is used to compare 2 knots.
        """
    def Poles(self,Index : int,Poles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        returns in <Poles> the poles of the BSplineCurve from index <Index> adjusting to the current profile. Raises if not yet perform Raises if <Index> not in the range [1,NbCurves] if the length of <Poles> is not equal to NbPoles().
        """
    @overload
    def Section(self,P : int,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        None
        """
    @overload
    def Section(self,P : int,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    def SetParam(self,Params : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def Weights(self,Index : int,Weights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        returns in <Weights> the weights of the BSplineCurve from index <Index> adjusting to the current profile. Raises if not yet perform Raises if <Index> not in the range [1,NbCurves] or if the length of <Weights> is not equal to NbPoles().
        """
    def __init__(self) -> None: ...
    pass
class GeomFill_EvolvedSection(GeomFill_SectionLaw, OCP.Standard.Standard_Transient):
    """
    Define an Constant Section LawDefine an Constant Section LawDefine an Constant Section Law
    """
    def BSplineSurface(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        give if possible an bspline Surface, like iso-v are the section. If it is not possible this methode have to get an Null Surface. Is it the default implementation.
        """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditioned rational approximation. Warning: Used only if <me> IsRational
        """
    def CirclSection(self,Param : float) -> OCP.Geom.Geom_Curve: 
        """
        Return the circle section at parameter <Param>, if <me> a IsConicalLaw
        """
    def ConstantSection(self) -> OCP.Geom.Geom_Curve: 
        """
        Return the constant Section if <me> IsConstant.
        """
    def D0(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param Warning : It used only for C2 aproximation
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
    def GetDomain(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the function parametric domain. Warning: This domain it is not modified by the SetValue method
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles in all sections. This information is usefull to control error in rational approximation. Warning: Used only if <me> IsRational
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerances associated at each poles to reach in approximation, to satisfy: BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConicalLaw(self,Error : float) -> bool: 
        """
        Returns True if all section are circle, with same plane,same center and linear radius evolution Return False by Default.
        """
    def IsConstant(self,Error : float) -> bool: 
        """
        return True If the Law isConstant
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
    def IsRational(self) -> bool: 
        """
        Returns if the sections are rationnal or not
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns if the sections are periodic or not
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns if the law isperiodic or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the greater section. This information is usefull to G1's control. Warning: With an little value, approximation can be slower.
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        get the Multplicities of the section
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SectionShape(self) -> Tuple[int, int, int]: 
        """
        get the format of an section
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usefull, if (me) have to run numerical algorithm to perform D0, D1 or D2 The default implementation make nothing.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,C : OCP.Geom.Geom_Curve,L : OCP.Law.Law_Function) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_SectionPlacement():
    """
    To place section in sweep Function
    """
    def Angle(self) -> float: 
        """
        None
        """
    def Distance(self) -> float: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def ModifiedSection(self,WithTranslation : bool) -> OCP.Geom.Geom_Curve: 
        """
        Compute the Section, in the coordinate syteme given by the Location Law. To have the Normal to section equal to the Location Law Normal. If <WithTranslation> contact beetween <Section> and <Path> is forced.
        """
    def ParameterOnPath(self) -> float: 
        """
        None
        """
    def ParameterOnSection(self) -> float: 
        """
        None
        """
    @overload
    def Perform(self,Path : OCP.Adaptor3d.Adaptor3d_HCurve,Tol : float) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Perform(self,Tol : float) -> None: ...
    @overload
    def Perform(self,ParamOnPath : float,Tol : float) -> None: ...
    def Section(self,WithTranslation : bool) -> OCP.Geom.Geom_Curve: 
        """
        Compute the Section, in the coordinate syteme given by the Location Law. If <WithTranslation> contact beetween <Section> and <Path> is forced.
        """
    def SetLocation(self,L : GeomFill_LocationLaw) -> None: 
        """
        To change the section Law
        """
    def Transformation(self,WithTranslation : bool,WithCorrection : bool=False) -> OCP.gp.gp_Trsf: 
        """
        None
        """
    def __init__(self,L : GeomFill_LocationLaw,Section : OCP.Geom.Geom_Geometry) -> None: ...
    pass
class GeomFill_HSequenceOfAx2(GeomFill_SequenceOfAx2, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.gp.gp_Ax2) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : GeomFill_SequenceOfAx2) -> None: ...
    def Assign(self,theOther : GeomFill_SequenceOfAx2) -> GeomFill_SequenceOfAx2: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.gp.gp_Ax2: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.gp.gp_Ax2: 
        """
        Last item access
        """
    def ChangeSequence(self) -> GeomFill_SequenceOfAx2: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_Ax2: 
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
    def First(self) -> OCP.gp.gp_Ax2: 
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
    def InsertAfter(self,theIndex : int,theItem : OCP.gp.gp_Ax2) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : GeomFill_SequenceOfAx2) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : GeomFill_SequenceOfAx2) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.gp.gp_Ax2) -> None: ...
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
    def Last(self) -> OCP.gp.gp_Ax2: 
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
    def Prepend(self,theItem : OCP.gp.gp_Ax2) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : GeomFill_SequenceOfAx2) -> None: ...
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
    def Sequence(self) -> GeomFill_SequenceOfAx2: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_Ax2) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : GeomFill_SequenceOfAx2) -> None: 
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
    def Value(self,theIndex : int) -> OCP.gp.gp_Ax2: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : GeomFill_SequenceOfAx2) -> None: ...
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
class GeomFill_SequenceOfTrsf(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.gp.gp_Trsf) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : GeomFill_SequenceOfTrsf) -> None: ...
    def Assign(self,theOther : GeomFill_SequenceOfTrsf) -> GeomFill_SequenceOfTrsf: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.gp.gp_Trsf: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.gp.gp_Trsf: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_Trsf: 
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
    def First(self) -> OCP.gp.gp_Trsf: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : GeomFill_SequenceOfTrsf) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.gp.gp_Trsf) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : GeomFill_SequenceOfTrsf) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.gp.gp_Trsf) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.gp.gp_Trsf: 
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
    def Prepend(self,theSeq : GeomFill_SequenceOfTrsf) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.gp.gp_Trsf) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_Trsf) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : GeomFill_SequenceOfTrsf) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.gp.gp_Trsf: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : GeomFill_SequenceOfTrsf) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class GeomFill_SimpleBound(GeomFill_Boundary, OCP.Standard.Standard_Transient):
    """
    Defines a 3d curve as a boundary for a GeomFill_ConstrainedFilling algorithm. This curve is unattached to an existing surface.D Contains fields to allow a reparametrization of curve.Defines a 3d curve as a boundary for a GeomFill_ConstrainedFilling algorithm. This curve is unattached to an existing surface.D Contains fields to allow a reparametrization of curve.Defines a 3d curve as a boundary for a GeomFill_ConstrainedFilling algorithm. This curve is unattached to an existing surface.D Contains fields to allow a reparametrization of curve.
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D1Norm(self,U : float,N : OCP.gp.gp_Vec,DN : OCP.gp.gp_Vec) -> None: 
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
    def HasNormals(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDegenerated(self) -> bool: 
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
    def Norm(self,U : float) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Points(self,PFirst : OCP.gp.gp_Pnt,PLast : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def Reparametrize(self,First : float,Last : float,HasDF : bool,HasDL : bool,DF : float,DL : float,Rev : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tol3d(self) -> float: 
        """
        None

        None
        """
    @overload
    def Tol3d(self,Tol : float) -> None: ...
    @overload
    def Tolang(self) -> float: 
        """
        None

        None
        """
    @overload
    def Tolang(self,Tol : float) -> None: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def __init__(self,Curve : OCP.Adaptor3d.Adaptor3d_HCurve,Tol3d : float,Tolang : float) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_SnglrFunc(OCP.Adaptor3d.Adaptor3d_Curve):
    """
    to represent function C'(t)^C''(t)
    """
    def BSpline(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def Bezier(self) -> OCP.Geom.Geom_BezierCurve: 
        """
        None
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U on the curve.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C1.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if N < 1.
        """
    def Degree(self) -> int: 
        """
        None
        """
    def Ellipse(self) -> OCP.gp.gp_Elips: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        None
        """
    def GetType(self) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def IsRational(self) -> bool: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        None
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        None
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbKnots(self) -> int: 
        """
        None
        """
    def NbPoles(self) -> int: 
        """
        None
        """
    def OffsetCurve(self) -> OCP.Geom.Geom_OffsetCurve: 
        """
        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab: 
        """
        None
        """
    def Period(self) -> float: 
        """
        None
        """
    def Resolution(self,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    def SetRatio(self,Ratio : float) -> None: 
        """
        None
        """
    def Trim(self,First : float,Last : float,Tol : float) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Returns a curve equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. If <First> >= <Last>
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self,HC : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    pass
class GeomFill_Stretch(GeomFill_Filling):
    """
    None
    """
    @overload
    def Init(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt,W1 : OCP.TColStd.TColStd_Array1OfReal,W2 : OCP.TColStd.TColStd_Array1OfReal,W3 : OCP.TColStd.TColStd_Array1OfReal,W4 : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    def NbUPoles(self) -> int: 
        """
        None
        """
    def NbVPoles(self) -> int: 
        """
        None
        """
    def Poles(self,Poles : OCP.TColgp.TColgp_Array2OfPnt) -> None: 
        """
        None
        """
    def Weights(self,Weights : OCP.TColStd.TColStd_Array2OfReal) -> None: 
        """
        None
        """
    @overload
    def __init__(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self,P1 : OCP.TColgp.TColgp_Array1OfPnt,P2 : OCP.TColgp.TColgp_Array1OfPnt,P3 : OCP.TColgp.TColgp_Array1OfPnt,P4 : OCP.TColgp.TColgp_Array1OfPnt,W1 : OCP.TColStd.TColStd_Array1OfReal,W2 : OCP.TColStd.TColStd_Array1OfReal,W3 : OCP.TColStd.TColStd_Array1OfReal,W4 : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def isRational(self) -> bool: 
        """
        None
        """
    pass
class GeomFill_Sweep():
    """
    Geometrical Sweep Algorithm
    """
    def Build(self,Section : GeomFill_SectionLaw,Methode : GeomFill_ApproxStyle=GeomFill_ApproxStyle.GeomFill_Location,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Degmax : int=10,Segmax : int=30) -> None: 
        """
        Build the Sweeep Surface ApproxStyle defines Approximation Strategy - GeomFill_Section : The composed Function : Location X Section is directly approximed. - GeomFill_Location : The location law is approximed, and the SweepSurface is build algebric composition of approximed location law and section law This option is Ok, if Section.Surface() methode is effective. Continuity : The continuity in v waiting on the surface Degmax : The maximum degree in v requiered on the surface Segmax : The maximum number of span in v requiered on the surface
        """
    def ErrorOnRestriction(self,IsFirst : bool) -> Tuple[float, float]: 
        """
        Gets the Approximation error.
        """
    def ErrorOnSurface(self) -> float: 
        """
        Gets the Approximation error.
        """
    def ErrorOnTrace(self,IndexOfTrace : int) -> Tuple[float, float]: 
        """
        Gets the Approximation error.
        """
    def ExchangeUV(self) -> bool: 
        """
        returns true if sections are U-Iso This can be produce in some cases when <WithKpart> is True.
        """
    def IsDone(self) -> bool: 
        """
        Tells if the Surface is Buildt.
        """
    def NumberOfTrace(self) -> int: 
        """
        None
        """
    def Restriction(self,IsFirst : bool) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def SetDomain(self,First : float,Last : float,SectionFirst : float,SectionLast : float) -> None: 
        """
        Set parametric information [<First>, <Last>] Sets the parametric bound of the sweeping surface to build. <SectionFirst>, <SectionLast> gives coresponding bounds parameter on the section law of <First> and <Last>
        """
    def SetForceApproxC1(self,ForceApproxC1 : bool) -> None: 
        """
        Set the flag that indicates attempt to approximate a C1-continuous surface if a swept surface proved to be C0.
        """
    def SetTolerance(self,Tol3d : float,BoundTol : float=1.0,Tol2d : float=1e-05,TolAngular : float=1.0) -> None: 
        """
        Set Approximation Tolerance Tol3d : Tolerance to surface approximation Tol2d : Tolerance used to perform curve approximation Normaly the 2d curve are approximated with a tolerance given by the resolution method define in <LocationLaw> but if this tolerance is too large Tol2d is used. TolAngular : Tolerance (in radian) to control the angle beetween tangents on the section law and tangent of iso-v on approximed surface
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Trace(self,IndexOfTrace : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def UReversed(self) -> bool: 
        """
        returns true if Parametrisation sens in U is inverse of parametrisation sens of section (or of path if ExchangeUV)
        """
    def VReversed(self) -> bool: 
        """
        returns true if Parametrisation sens in V is inverse of parametrisation sens of path (or of section if ExchangeUV)
        """
    def __init__(self,Location : GeomFill_LocationLaw,WithKpart : bool=True) -> None: ...
    pass
class GeomFill_SweepFunction(OCP.Approx.Approx_SweepFunction, OCP.Standard.Standard_Transient):
    """
    Function to approximate by SweepApproximation from Approx. To bulid general sweep Surface.Function to approximate by SweepApproximation from Approx. To bulid general sweep Surface.Function to approximate by SweepApproximation from Approx. To bulid general sweep Surface.
    """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditionned rational approximation. Warning: Used only if <me> IsRational
        """
    def D0(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param
        """
    def D2(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param
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
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections. This information is usefull to perform well conditionned rational approximation. Warning: Used only if <me> IsRational
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
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
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the maximum section. This information is usefull to perform well conditionned rational approximation.
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        get the Multplicities of the section
        """
    def Nb2dCurves(self) -> int: 
        """
        get the number of 2d curves to approximate.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> This information is usfull to find an good tolerance in 2d approximation. Warning: Used only if Nb2dCurve > 0
        """
    def SectionShape(self) -> Tuple[int, int, int]: 
        """
        get the format of an section
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usfull, if (me) have to be run numerical algorithme to perform D0, D1 or D2
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Section : GeomFill_SectionLaw,Location : GeomFill_LocationLaw,FirstParameter : float,FirstParameterOnS : float,RatioParameterOnS : float) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_SweepSectionGenerator():
    """
    class for instantiation of AppBlend. evaluate the sections of a sweep surface.
    """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    @overload
    def Init(self,Path : OCP.Adaptor3d.Adaptor3d_HCurve,Curve1 : OCP.Adaptor3d.Adaptor3d_HCurve,Curve2 : OCP.Adaptor3d.Adaptor3d_HCurve,Radius : float) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Init(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def Init(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve,LastSect : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def Init(self,Path : OCP.Geom.Geom_Curve,Radius : float) -> None: ...
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbSections(self) -> int: 
        """
        None

        None
        """
    def Parameter(self,P : int) -> float: 
        """
        Returns the parameter of <P>, to impose it for the approximation.
        """
    def Perform(self,Polynomial : bool=False) -> None: 
        """
        None
        """
    @overload
    def Section(self,P : int,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        None
        """
    @overload
    def Section(self,P : int,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    def Transformation(self,Index : int) -> OCP.gp.gp_Trsf: 
        """
        raised if <Index> not in the range [1,NbSections()]
        """
    @overload
    def __init__(self,Path : OCP.Adaptor3d.Adaptor3d_HCurve,Curve1 : OCP.Adaptor3d.Adaptor3d_HCurve,Curve2 : OCP.Adaptor3d.Adaptor3d_HCurve,Radius : float) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve,LastSect : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,Radius : float) -> None: ...
    @overload
    def __init__(self,Path : OCP.Geom.Geom_Curve,FirstSect : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomFill_Tensor():
    """
    used to store the "gradient of gradient"
    """
    def ChangeValue(self,Row : int,Col : int,Mat : int) -> float: ...
    def Init(self,InitialValue : float) -> None: 
        """
        Initialize all the elements of a Tensor to InitialValue.
        """
    def Multiply(self,Right : OCP.math.math_Vector,Product : OCP.math.math_Matrix) -> None: 
        """
        None
        """
    def Value(self,Row : int,Col : int,Mat : int) -> float: ...
    def __init__(self,NbRow : int,NbCol : int,NbMat : int) -> None: ...
    pass
class GeomFill_TgtField(OCP.Standard.Standard_Transient):
    """
    Root class defining the methods we need to make an algorithmic tangents field.Root class defining the methods we need to make an algorithmic tangents field.Root class defining the methods we need to make an algorithmic tangents field.
    """
    @overload
    def D1(self,W : float,V : OCP.gp.gp_Vec,DV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the derivative of the field of tangency at parameter W.

        Computes the value and the derivative of the field of tangency at parameter W.
        """
    @overload
    def D1(self,W : float) -> OCP.gp.gp_Vec: ...
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
    def IsScalable(self) -> bool: 
        """
        None
        """
    def Scale(self,Func : OCP.Law.Law_BSpline) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,W : float) -> OCP.gp.gp_Vec: 
        """
        Computes the value of the field of tangency at parameter W.
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
class GeomFill_TgtOnCoons(GeomFill_TgtField, OCP.Standard.Standard_Transient):
    """
    Defines an algorithmic tangents field on a boundary of a CoonsAlgPatch.Defines an algorithmic tangents field on a boundary of a CoonsAlgPatch.Defines an algorithmic tangents field on a boundary of a CoonsAlgPatch.
    """
    @overload
    def D1(self,W : float,T : OCP.gp.gp_Vec,DT : OCP.gp.gp_Vec) -> None: 
        """
        Computes the derivative of the field of tangency at parameter W.

        Computes the value and the derivative of the field of tangency at parameter W.
        """
    @overload
    def D1(self,W : float) -> OCP.gp.gp_Vec: ...
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
    def IsScalable(self) -> bool: 
        """
        None
        """
    def Scale(self,Func : OCP.Law.Law_BSpline) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,W : float) -> OCP.gp.gp_Vec: 
        """
        Computes the value of the field of tangency at parameter W.
        """
    def __init__(self,K : GeomFill_CoonsAlgPatch,I : int) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_Trihedron():
    """
    None

    Members:

      GeomFill_IsCorrectedFrenet

      GeomFill_IsFixed

      GeomFill_IsFrenet

      GeomFill_IsConstantNormal

      GeomFill_IsDarboux

      GeomFill_IsGuideAC

      GeomFill_IsGuidePlan

      GeomFill_IsGuideACWithContact

      GeomFill_IsGuidePlanWithContact

      GeomFill_IsDiscreteTrihedron
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
    GeomFill_IsConstantNormal: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsConstantNormal
    GeomFill_IsCorrectedFrenet: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsCorrectedFrenet
    GeomFill_IsDarboux: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsDarboux
    GeomFill_IsDiscreteTrihedron: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsDiscreteTrihedron
    GeomFill_IsFixed: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsFixed
    GeomFill_IsFrenet: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsFrenet
    GeomFill_IsGuideAC: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsGuideAC
    GeomFill_IsGuideACWithContact: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsGuideACWithContact
    GeomFill_IsGuidePlan: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsGuidePlan
    GeomFill_IsGuidePlanWithContact: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsGuidePlanWithContact
    __entries: dict # value = {'GeomFill_IsCorrectedFrenet': (GeomFill_Trihedron.GeomFill_IsCorrectedFrenet, None), 'GeomFill_IsFixed': (GeomFill_Trihedron.GeomFill_IsFixed, None), 'GeomFill_IsFrenet': (GeomFill_Trihedron.GeomFill_IsFrenet, None), 'GeomFill_IsConstantNormal': (GeomFill_Trihedron.GeomFill_IsConstantNormal, None), 'GeomFill_IsDarboux': (GeomFill_Trihedron.GeomFill_IsDarboux, None), 'GeomFill_IsGuideAC': (GeomFill_Trihedron.GeomFill_IsGuideAC, None), 'GeomFill_IsGuidePlan': (GeomFill_Trihedron.GeomFill_IsGuidePlan, None), 'GeomFill_IsGuideACWithContact': (GeomFill_Trihedron.GeomFill_IsGuideACWithContact, None), 'GeomFill_IsGuidePlanWithContact': (GeomFill_Trihedron.GeomFill_IsGuidePlanWithContact, None), 'GeomFill_IsDiscreteTrihedron': (GeomFill_Trihedron.GeomFill_IsDiscreteTrihedron, None)}
    __members__: dict # value = {'GeomFill_IsCorrectedFrenet': GeomFill_Trihedron.GeomFill_IsCorrectedFrenet, 'GeomFill_IsFixed': GeomFill_Trihedron.GeomFill_IsFixed, 'GeomFill_IsFrenet': GeomFill_Trihedron.GeomFill_IsFrenet, 'GeomFill_IsConstantNormal': GeomFill_Trihedron.GeomFill_IsConstantNormal, 'GeomFill_IsDarboux': GeomFill_Trihedron.GeomFill_IsDarboux, 'GeomFill_IsGuideAC': GeomFill_Trihedron.GeomFill_IsGuideAC, 'GeomFill_IsGuidePlan': GeomFill_Trihedron.GeomFill_IsGuidePlan, 'GeomFill_IsGuideACWithContact': GeomFill_Trihedron.GeomFill_IsGuideACWithContact, 'GeomFill_IsGuidePlanWithContact': GeomFill_Trihedron.GeomFill_IsGuidePlanWithContact, 'GeomFill_IsDiscreteTrihedron': GeomFill_Trihedron.GeomFill_IsDiscreteTrihedron}
    pass
class GeomFill_ConstantBiNormal(GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    """
    Defined an Trihedron Law where the BiNormal, is fixedDefined an Trihedron Law where the BiNormal, is fixedDefined an Trihedron Law where the BiNormal, is fixed
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        Computes Triedrhon on curve at parameter <Param>
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        Computes Triedrhon and derivative Trihedron on curve at parameter <Param> Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        compute Trihedron on curve first and seconde derivatives. Warning : It used only for C2 aproximation
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Gets average value of Tangent(t) and Normal(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Says if the law is Constant.
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Return True.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,BiNormal : OCP.gp.gp_Dir) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_GuideTrihedronAC(GeomFill_TrihedronWithGuide, GeomFill_TrihedronLaw, OCP.Standard.Standard_Transient):
    """
    Trihedron in the case of a sweeping along a guide curve. defined by curviline abscissTrihedron in the case of a sweeping along a guide curve. defined by curviline abscissTrihedron in the case of a sweeping along a guide curve. defined by curviline absciss
    """
    def Copy(self) -> GeomFill_TrihedronLaw: 
        """
        None
        """
    def CurrentPointOnGuide(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the current point on guide found by D0, D1 or D2.
        """
    def D0(self,Param : float,Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    def D1(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    def D2(self,Param : float,Tangent : OCP.gp.gp_Vec,DTangent : OCP.gp.gp_Vec,D2Tangent : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Vec,DNormal : OCP.gp.gp_Vec,D2Normal : OCP.gp.gp_Vec,BiNormal : OCP.gp.gp_Vec,DBiNormal : OCP.gp.gp_Vec,D2BiNormal : OCP.gp.gp_Vec) -> bool: 
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
    def ErrorStatus(self) -> GeomFill_PipeError: 
        """
        Give a status to the Law Returns PipeOk (default implementation)
        """
    def GetAverageLaw(self,ATangent : OCP.gp.gp_Vec,ANormal : OCP.gp.gp_Vec,ABiNormal : OCP.gp.gp_Vec) -> None: 
        """
        Get average value of M(t) and V(t) it is usfull to make fast approximation of rational surfaces.
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Guide(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConstant(self) -> bool: 
        """
        Say if the law is Constant
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
    def IsOnlyBy3dCurve(self) -> bool: 
        """
        Say if the law is defined, only by the 3d Geometry of the setted Curve Return False by Default.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def Origine(self,OrACR1 : float,OrACR2 : float) -> None: 
        """
        None
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
        """
        None
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,guide : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class GeomFill_UniformSection(GeomFill_SectionLaw, OCP.Standard.Standard_Transient):
    """
    Define an Constant Section LawDefine an Constant Section LawDefine an Constant Section Law
    """
    def BSplineSurface(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        give if possible an bspline Surface, like iso-v are the section. If it is not possible this methode have to get an Null Surface. Is it the default implementation.
        """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditioned rational approximation. Warning: Used only if <me> IsRational
        """
    def CirclSection(self,Param : float) -> OCP.Geom.Geom_Curve: 
        """
        Return the circle section at parameter <Param>, if <me> a IsConicalLaw
        """
    def ConstantSection(self) -> OCP.Geom.Geom_Curve: 
        """
        Return the constant Section if <me> IsConstant.
        """
    def D0(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param Warning : It used only for C1 or C2 aproximation
        """
    def D2(self,Param : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param Warning : It used only for C2 aproximation
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
    def GetDomain(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the function parametric domain. Warning: This domain it is not modified by the SetValue method
        """
    def GetInterval(self) -> Tuple[float, float]: 
        """
        Gets the bounds of the parametric interval on the function
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles in all sections. This information is usefull to control error in rational approximation. Warning: Used only if <me> IsRational
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerances associated at each poles to reach in approximation, to satisfy: BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsConicalLaw(self,Error : float) -> bool: 
        """
        Returns True if all section are circle, with same plane,same center and linear radius evolution Return False by Default.
        """
    def IsConstant(self,Error : float) -> bool: 
        """
        return True
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
    def IsRational(self) -> bool: 
        """
        Returns if the sections are rationnal or not
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns if the sections are periodic or not
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns if the law isperiodic or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the greater section. This information is usefull to G1's control. Warning: With an little value, approximation can be slower.
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        get the Multplicities of the section
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SectionShape(self) -> Tuple[int, int, int]: 
        """
        get the format of an section
        """
    def SetInterval(self,First : float,Last : float) -> None: 
        """
        Sets the bounds of the parametric interval on the function This determines the derivatives in these values if the function is not Cn.
        """
    def SetTolerance(self,Tol3d : float,Tol2d : float) -> None: 
        """
        Is usefull, if (me) have to run numerical algorithm to perform D0, D1 or D2 The default implementation make nothing.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,C : OCP.Geom.Geom_Curve,FirstParameter : float=0.0,LastParameter : float=1.0) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
GeomFill_CoonsStyle: OCP.GeomFill.GeomFill_FillingStyle # value = GeomFill_FillingStyle.GeomFill_CoonsStyle
GeomFill_CurvedStyle: OCP.GeomFill.GeomFill_FillingStyle # value = GeomFill_FillingStyle.GeomFill_CurvedStyle
GeomFill_ImpossibleContact: OCP.GeomFill.GeomFill_PipeError # value = GeomFill_PipeError.GeomFill_ImpossibleContact
GeomFill_IsConstantNormal: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsConstantNormal
GeomFill_IsCorrectedFrenet: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsCorrectedFrenet
GeomFill_IsDarboux: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsDarboux
GeomFill_IsDiscreteTrihedron: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsDiscreteTrihedron
GeomFill_IsFixed: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsFixed
GeomFill_IsFrenet: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsFrenet
GeomFill_IsGuideAC: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsGuideAC
GeomFill_IsGuideACWithContact: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsGuideACWithContact
GeomFill_IsGuidePlan: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsGuidePlan
GeomFill_IsGuidePlanWithContact: OCP.GeomFill.GeomFill_Trihedron # value = GeomFill_Trihedron.GeomFill_IsGuidePlanWithContact
GeomFill_Location: OCP.GeomFill.GeomFill_ApproxStyle # value = GeomFill_ApproxStyle.GeomFill_Location
GeomFill_PipeNotOk: OCP.GeomFill.GeomFill_PipeError # value = GeomFill_PipeError.GeomFill_PipeNotOk
GeomFill_PipeOk: OCP.GeomFill.GeomFill_PipeError # value = GeomFill_PipeError.GeomFill_PipeOk
GeomFill_PlaneNotIntersectGuide: OCP.GeomFill.GeomFill_PipeError # value = GeomFill_PipeError.GeomFill_PlaneNotIntersectGuide
GeomFill_Section: OCP.GeomFill.GeomFill_ApproxStyle # value = GeomFill_ApproxStyle.GeomFill_Section
GeomFill_StretchStyle: OCP.GeomFill.GeomFill_FillingStyle # value = GeomFill_FillingStyle.GeomFill_StretchStyle
