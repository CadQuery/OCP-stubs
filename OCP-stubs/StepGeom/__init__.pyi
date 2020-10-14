import OCP.StepGeom
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.TColStd
import OCP.StepRepr
import OCP.StepBasic
import OCP.Standard
import OCP.StepData
import OCP.Interface
__all__  = [
"StepGeom_Array1OfBoundaryCurve",
"StepGeom_Array1OfCartesianPoint",
"StepGeom_Array1OfCompositeCurveSegment",
"StepGeom_Array1OfCurve",
"StepGeom_Array1OfPcurveOrSurface",
"StepGeom_Array1OfSurfaceBoundary",
"StepGeom_Array1OfTrimmingSelect",
"StepGeom_Array2OfCartesianPoint",
"StepGeom_Array2OfSurfacePatch",
"StepGeom_GeometricRepresentationItem",
"StepGeom_Axis2Placement",
"StepGeom_Placement",
"StepGeom_Axis2Placement3d",
"StepGeom_Curve",
"StepGeom_BSplineCurveForm",
"StepGeom_BoundedCurve",
"StepGeom_BSplineCurve",
"StepGeom_Surface",
"StepGeom_BSplineSurfaceForm",
"StepGeom_BoundedSurface",
"StepGeom_BSplineSurface",
"StepGeom_BezierCurve",
"StepGeom_BezierCurveAndRationalBSplineCurve",
"StepGeom_BezierSurface",
"StepGeom_BezierSurfaceAndRationalBSplineSurface",
"StepGeom_CompositeCurve",
"StepGeom_BSplineCurveWithKnots",
"StepGeom_BSplineSurfaceWithKnots",
"StepGeom_Point",
"StepGeom_CartesianTransformationOperator",
"StepGeom_CartesianTransformationOperator2d",
"StepGeom_CartesianTransformationOperator3d",
"StepGeom_Conic",
"StepGeom_CompositeCurveOnSurface",
"StepGeom_BoundaryCurve",
"StepGeom_CompositeCurveSegment",
"StepGeom_Circle",
"StepGeom_ElementarySurface",
"StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve",
"StepGeom_CurveBoundedSurface",
"StepGeom_CurveOnSurface",
"StepGeom_CurveReplica",
"StepGeom_CylindricalSurface",
"StepGeom_DegeneratePcurve",
"StepGeom_ToroidalSurface",
"StepGeom_Direction",
"StepGeom_ConicalSurface",
"StepGeom_Ellipse",
"StepGeom_EvaluatedDegeneratePcurve",
"StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx",
"StepGeom_GeometricRepresentationContext",
"StepGeom_GeometricRepresentationContextAndGlobalUnitAssignedContext",
"StepGeom_GeometricRepresentationContextAndParametricRepresentationContext",
"StepGeom_Axis1Placement",
"StepGeom_HArray1OfBoundaryCurve",
"StepGeom_HArray1OfCartesianPoint",
"StepGeom_HArray1OfCompositeCurveSegment",
"StepGeom_HArray1OfCurve",
"StepGeom_HArray1OfPcurveOrSurface",
"StepGeom_HArray1OfSurfaceBoundary",
"StepGeom_HArray1OfTrimmingSelect",
"StepGeom_HArray2OfCartesianPoint",
"StepGeom_HArray2OfSurfacePatch",
"StepGeom_Hyperbola",
"StepGeom_SurfaceCurve",
"StepGeom_KnotType",
"StepGeom_Line",
"StepGeom_OffsetCurve3d",
"StepGeom_OffsetSurface",
"StepGeom_OrientedSurface",
"StepGeom_OuterBoundaryCurve",
"StepGeom_Parabola",
"StepGeom_Pcurve",
"StepGeom_PcurveOrSurface",
"StepGeom_Axis2Placement2d",
"StepGeom_Plane",
"StepGeom_CartesianPoint",
"StepGeom_PointOnCurve",
"StepGeom_PointOnSurface",
"StepGeom_PointReplica",
"StepGeom_Polyline",
"StepGeom_PreferredSurfaceCurveRepresentation",
"StepGeom_QuasiUniformCurve",
"StepGeom_QuasiUniformCurveAndRationalBSplineCurve",
"StepGeom_QuasiUniformSurface",
"StepGeom_QuasiUniformSurfaceAndRationalBSplineSurface",
"StepGeom_RationalBSplineCurve",
"StepGeom_RationalBSplineSurface",
"StepGeom_RectangularCompositeSurface",
"StepGeom_RectangularTrimmedSurface",
"StepGeom_ReparametrisedCompositeCurveSegment",
"StepGeom_SeamCurve",
"StepGeom_SphericalSurface",
"StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface",
"StepGeom_SurfaceBoundary",
"StepGeom_IntersectionCurve",
"StepGeom_SurfaceCurveAndBoundedCurve",
"StepGeom_SweptSurface",
"StepGeom_SurfaceOfRevolution",
"StepGeom_SurfacePatch",
"StepGeom_SurfaceReplica",
"StepGeom_SurfaceOfLinearExtrusion",
"StepGeom_DegenerateToroidalSurface",
"StepGeom_TransitionCode",
"StepGeom_TrimmedCurve",
"StepGeom_TrimmingMember",
"StepGeom_TrimmingPreference",
"StepGeom_TrimmingSelect",
"StepGeom_UniformCurve",
"StepGeom_UniformCurveAndRationalBSplineCurve",
"StepGeom_UniformSurface",
"StepGeom_UniformSurfaceAndRationalBSplineSurface",
"StepGeom_Vector",
"StepGeom_VectorOrDirection",
"StepGeom_bscfCircularArc",
"StepGeom_bscfEllipticArc",
"StepGeom_bscfHyperbolicArc",
"StepGeom_bscfParabolicArc",
"StepGeom_bscfPolylineForm",
"StepGeom_bscfUnspecified",
"StepGeom_bssfConicalSurf",
"StepGeom_bssfCylindricalSurf",
"StepGeom_bssfGeneralisedCone",
"StepGeom_bssfPlaneSurf",
"StepGeom_bssfQuadricSurf",
"StepGeom_bssfRuledSurf",
"StepGeom_bssfSphericalSurf",
"StepGeom_bssfSurfOfLinearExtrusion",
"StepGeom_bssfSurfOfRevolution",
"StepGeom_bssfToroidalSurf",
"StepGeom_bssfUnspecified",
"StepGeom_ktPiecewiseBezierKnots",
"StepGeom_ktQuasiUniformKnots",
"StepGeom_ktUniformKnots",
"StepGeom_ktUnspecified",
"StepGeom_pscrCurve3d",
"StepGeom_pscrPcurveS1",
"StepGeom_pscrPcurveS2",
"StepGeom_tcContSameGradient",
"StepGeom_tcContSameGradientSameCurvature",
"StepGeom_tcContinuous",
"StepGeom_tcDiscontinuous",
"StepGeom_tpCartesian",
"StepGeom_tpParameter",
"StepGeom_tpUnspecified"
]
class StepGeom_Array1OfBoundaryCurve():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepGeom_Array1OfBoundaryCurve) -> StepGeom_Array1OfBoundaryCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepGeom_BoundaryCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_BoundaryCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_BoundaryCurve: 
        """
        Variable value access
        """
    def First(self) -> StepGeom_BoundaryCurve: 
        """
        Returns first element
        """
    def Init(self,theValue : StepGeom_BoundaryCurve) -> None: 
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
    def Last(self) -> StepGeom_BoundaryCurve: 
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
    def Move(self,theOther : StepGeom_Array1OfBoundaryCurve) -> StepGeom_Array1OfBoundaryCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_BoundaryCurve) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_BoundaryCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array1OfBoundaryCurve) -> None: ...
    @overload
    def __init__(self,theBegin : StepGeom_BoundaryCurve,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepGeom_Array1OfCartesianPoint():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepGeom_Array1OfCartesianPoint) -> StepGeom_Array1OfCartesianPoint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepGeom_CartesianPoint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_CartesianPoint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_CartesianPoint: 
        """
        Variable value access
        """
    def First(self) -> StepGeom_CartesianPoint: 
        """
        Returns first element
        """
    def Init(self,theValue : StepGeom_CartesianPoint) -> None: 
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
    def Last(self) -> StepGeom_CartesianPoint: 
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
    def Move(self,theOther : StepGeom_Array1OfCartesianPoint) -> StepGeom_Array1OfCartesianPoint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_CartesianPoint) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_CartesianPoint: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepGeom_CartesianPoint,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array1OfCartesianPoint) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepGeom_Array1OfCompositeCurveSegment():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepGeom_Array1OfCompositeCurveSegment) -> StepGeom_Array1OfCompositeCurveSegment: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepGeom_CompositeCurveSegment: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_CompositeCurveSegment: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_CompositeCurveSegment: 
        """
        Variable value access
        """
    def First(self) -> StepGeom_CompositeCurveSegment: 
        """
        Returns first element
        """
    def Init(self,theValue : StepGeom_CompositeCurveSegment) -> None: 
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
    def Last(self) -> StepGeom_CompositeCurveSegment: 
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
    def Move(self,theOther : StepGeom_Array1OfCompositeCurveSegment) -> StepGeom_Array1OfCompositeCurveSegment: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_CompositeCurveSegment) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_CompositeCurveSegment: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array1OfCompositeCurveSegment) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepGeom_CompositeCurveSegment,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepGeom_Array1OfCurve():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepGeom_Array1OfCurve) -> StepGeom_Array1OfCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepGeom_Curve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_Curve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_Curve: 
        """
        Variable value access
        """
    def First(self) -> StepGeom_Curve: 
        """
        Returns first element
        """
    def Init(self,theValue : StepGeom_Curve) -> None: 
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
    def Last(self) -> StepGeom_Curve: 
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
    def Move(self,theOther : StepGeom_Array1OfCurve) -> StepGeom_Array1OfCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_Curve) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_Curve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepGeom_Array1OfCurve) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepGeom_Curve,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepGeom_Array1OfPcurveOrSurface():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepGeom_Array1OfPcurveOrSurface) -> StepGeom_Array1OfPcurveOrSurface: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepGeom_PcurveOrSurface: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_PcurveOrSurface: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_PcurveOrSurface: 
        """
        Variable value access
        """
    def First(self) -> StepGeom_PcurveOrSurface: 
        """
        Returns first element
        """
    def Init(self,theValue : StepGeom_PcurveOrSurface) -> None: 
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
    def Last(self) -> StepGeom_PcurveOrSurface: 
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
    def Move(self,theOther : StepGeom_Array1OfPcurveOrSurface) -> StepGeom_Array1OfPcurveOrSurface: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_PcurveOrSurface) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_PcurveOrSurface: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepGeom_PcurveOrSurface,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array1OfPcurveOrSurface) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepGeom_Array1OfSurfaceBoundary():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepGeom_Array1OfSurfaceBoundary) -> StepGeom_Array1OfSurfaceBoundary: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepGeom_SurfaceBoundary: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_SurfaceBoundary: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_SurfaceBoundary: 
        """
        Variable value access
        """
    def First(self) -> StepGeom_SurfaceBoundary: 
        """
        Returns first element
        """
    def Init(self,theValue : StepGeom_SurfaceBoundary) -> None: 
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
    def Last(self) -> StepGeom_SurfaceBoundary: 
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
    def Move(self,theOther : StepGeom_Array1OfSurfaceBoundary) -> StepGeom_Array1OfSurfaceBoundary: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_SurfaceBoundary) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_SurfaceBoundary: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepGeom_SurfaceBoundary,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array1OfSurfaceBoundary) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepGeom_Array1OfTrimmingSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepGeom_Array1OfTrimmingSelect) -> StepGeom_Array1OfTrimmingSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepGeom_TrimmingSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_TrimmingSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_TrimmingSelect: 
        """
        Variable value access
        """
    def First(self) -> StepGeom_TrimmingSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepGeom_TrimmingSelect) -> None: 
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
    def Last(self) -> StepGeom_TrimmingSelect: 
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
    def Move(self,theOther : StepGeom_Array1OfTrimmingSelect) -> StepGeom_Array1OfTrimmingSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_TrimmingSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_TrimmingSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepGeom_Array1OfTrimmingSelect) -> None: ...
    @overload
    def __init__(self,theBegin : StepGeom_TrimmingSelect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepGeom_Array2OfCartesianPoint():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : StepGeom_Array2OfCartesianPoint) -> StepGeom_Array2OfCartesianPoint: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepGeom_CartesianPoint: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : StepGeom_CartesianPoint) -> None: 
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
    def Move(self,theOther : StepGeom_Array2OfCartesianPoint) -> StepGeom_Array2OfCartesianPoint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : StepGeom_CartesianPoint) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> StepGeom_CartesianPoint: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepGeom_CartesianPoint,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array2OfCartesianPoint) -> None: ...
    pass
class StepGeom_Array2OfSurfacePatch():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : StepGeom_Array2OfSurfacePatch) -> StepGeom_Array2OfSurfacePatch: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepGeom_SurfacePatch: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : StepGeom_SurfacePatch) -> None: 
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
    def Move(self,theOther : StepGeom_Array2OfSurfacePatch) -> StepGeom_Array2OfSurfacePatch: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : StepGeom_SurfacePatch) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> StepGeom_SurfacePatch: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepGeom_SurfacePatch,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array2OfSurfacePatch) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class StepGeom_GeometricRepresentationItem(OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
class StepGeom_Axis2Placement(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Axis2Placement2d(self) -> StepGeom_Axis2Placement2d: 
        """
        returns Value as a Axis2Placement2d (Null if another type)
        """
    def Axis2Placement3d(self) -> StepGeom_Axis2Placement3d: 
        """
        returns Value as a Axis2Placement3d (Null if another type)
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
        Recognizes a Axis2Placement Kind Entity that is : 1 -> Axis2Placement2d 2 -> Axis2Placement3d 0 else
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
class StepGeom_Placement(StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aLocation : StepGeom_CartesianPoint) -> None: 
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
    def Location(self) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetLocation(self,aLocation : StepGeom_CartesianPoint) -> None: 
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
class StepGeom_Axis2Placement3d(StepGeom_Placement, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Axis(self) -> StepGeom_Direction: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aLocation : StepGeom_CartesianPoint,hasAaxis : bool,aAxis : StepGeom_Direction,hasArefDirection : bool,aRefDirection : StepGeom_Direction) -> None: 
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
    def Location(self) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def RefDirection(self) -> StepGeom_Direction: 
        """
        None
        """
    def SetAxis(self,aAxis : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetLocation(self,aLocation : StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRefDirection(self,aRefDirection : StepGeom_Direction) -> None: 
        """
        None
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
class StepGeom_Curve(StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
class StepGeom_BSplineCurveForm():
    """
    None

    Members:

      StepGeom_bscfPolylineForm

      StepGeom_bscfCircularArc

      StepGeom_bscfEllipticArc

      StepGeom_bscfParabolicArc

      StepGeom_bscfHyperbolicArc

      StepGeom_bscfUnspecified
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
    StepGeom_bscfCircularArc: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfCircularArc
    StepGeom_bscfEllipticArc: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfEllipticArc
    StepGeom_bscfHyperbolicArc: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfHyperbolicArc
    StepGeom_bscfParabolicArc: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfParabolicArc
    StepGeom_bscfPolylineForm: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfPolylineForm
    StepGeom_bscfUnspecified: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfUnspecified
    __entries: dict # value = {'StepGeom_bscfPolylineForm': (StepGeom_BSplineCurveForm.StepGeom_bscfPolylineForm, None), 'StepGeom_bscfCircularArc': (StepGeom_BSplineCurveForm.StepGeom_bscfCircularArc, None), 'StepGeom_bscfEllipticArc': (StepGeom_BSplineCurveForm.StepGeom_bscfEllipticArc, None), 'StepGeom_bscfParabolicArc': (StepGeom_BSplineCurveForm.StepGeom_bscfParabolicArc, None), 'StepGeom_bscfHyperbolicArc': (StepGeom_BSplineCurveForm.StepGeom_bscfHyperbolicArc, None), 'StepGeom_bscfUnspecified': (StepGeom_BSplineCurveForm.StepGeom_bscfUnspecified, None)}
    __members__: dict # value = {'StepGeom_bscfPolylineForm': StepGeom_BSplineCurveForm.StepGeom_bscfPolylineForm, 'StepGeom_bscfCircularArc': StepGeom_BSplineCurveForm.StepGeom_bscfCircularArc, 'StepGeom_bscfEllipticArc': StepGeom_BSplineCurveForm.StepGeom_bscfEllipticArc, 'StepGeom_bscfParabolicArc': StepGeom_BSplineCurveForm.StepGeom_bscfParabolicArc, 'StepGeom_bscfHyperbolicArc': StepGeom_BSplineCurveForm.StepGeom_bscfHyperbolicArc, 'StepGeom_bscfUnspecified': StepGeom_BSplineCurveForm.StepGeom_bscfUnspecified}
    pass
class StepGeom_BoundedCurve(StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
class StepGeom_BSplineCurve(StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_Surface(StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
class StepGeom_BSplineSurfaceForm():
    """
    None

    Members:

      StepGeom_bssfPlaneSurf

      StepGeom_bssfCylindricalSurf

      StepGeom_bssfConicalSurf

      StepGeom_bssfSphericalSurf

      StepGeom_bssfToroidalSurf

      StepGeom_bssfSurfOfRevolution

      StepGeom_bssfRuledSurf

      StepGeom_bssfGeneralisedCone

      StepGeom_bssfQuadricSurf

      StepGeom_bssfSurfOfLinearExtrusion

      StepGeom_bssfUnspecified
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
    StepGeom_bssfConicalSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfConicalSurf
    StepGeom_bssfCylindricalSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfCylindricalSurf
    StepGeom_bssfGeneralisedCone: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfGeneralisedCone
    StepGeom_bssfPlaneSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfPlaneSurf
    StepGeom_bssfQuadricSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfQuadricSurf
    StepGeom_bssfRuledSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfRuledSurf
    StepGeom_bssfSphericalSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfSphericalSurf
    StepGeom_bssfSurfOfLinearExtrusion: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfSurfOfLinearExtrusion
    StepGeom_bssfSurfOfRevolution: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfSurfOfRevolution
    StepGeom_bssfToroidalSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfToroidalSurf
    StepGeom_bssfUnspecified: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfUnspecified
    __entries: dict # value = {'StepGeom_bssfPlaneSurf': (StepGeom_BSplineSurfaceForm.StepGeom_bssfPlaneSurf, None), 'StepGeom_bssfCylindricalSurf': (StepGeom_BSplineSurfaceForm.StepGeom_bssfCylindricalSurf, None), 'StepGeom_bssfConicalSurf': (StepGeom_BSplineSurfaceForm.StepGeom_bssfConicalSurf, None), 'StepGeom_bssfSphericalSurf': (StepGeom_BSplineSurfaceForm.StepGeom_bssfSphericalSurf, None), 'StepGeom_bssfToroidalSurf': (StepGeom_BSplineSurfaceForm.StepGeom_bssfToroidalSurf, None), 'StepGeom_bssfSurfOfRevolution': (StepGeom_BSplineSurfaceForm.StepGeom_bssfSurfOfRevolution, None), 'StepGeom_bssfRuledSurf': (StepGeom_BSplineSurfaceForm.StepGeom_bssfRuledSurf, None), 'StepGeom_bssfGeneralisedCone': (StepGeom_BSplineSurfaceForm.StepGeom_bssfGeneralisedCone, None), 'StepGeom_bssfQuadricSurf': (StepGeom_BSplineSurfaceForm.StepGeom_bssfQuadricSurf, None), 'StepGeom_bssfSurfOfLinearExtrusion': (StepGeom_BSplineSurfaceForm.StepGeom_bssfSurfOfLinearExtrusion, None), 'StepGeom_bssfUnspecified': (StepGeom_BSplineSurfaceForm.StepGeom_bssfUnspecified, None)}
    __members__: dict # value = {'StepGeom_bssfPlaneSurf': StepGeom_BSplineSurfaceForm.StepGeom_bssfPlaneSurf, 'StepGeom_bssfCylindricalSurf': StepGeom_BSplineSurfaceForm.StepGeom_bssfCylindricalSurf, 'StepGeom_bssfConicalSurf': StepGeom_BSplineSurfaceForm.StepGeom_bssfConicalSurf, 'StepGeom_bssfSphericalSurf': StepGeom_BSplineSurfaceForm.StepGeom_bssfSphericalSurf, 'StepGeom_bssfToroidalSurf': StepGeom_BSplineSurfaceForm.StepGeom_bssfToroidalSurf, 'StepGeom_bssfSurfOfRevolution': StepGeom_BSplineSurfaceForm.StepGeom_bssfSurfOfRevolution, 'StepGeom_bssfRuledSurf': StepGeom_BSplineSurfaceForm.StepGeom_bssfRuledSurf, 'StepGeom_bssfGeneralisedCone': StepGeom_BSplineSurfaceForm.StepGeom_bssfGeneralisedCone, 'StepGeom_bssfQuadricSurf': StepGeom_BSplineSurfaceForm.StepGeom_bssfQuadricSurf, 'StepGeom_bssfSurfOfLinearExtrusion': StepGeom_BSplineSurfaceForm.StepGeom_bssfSurfOfLinearExtrusion, 'StepGeom_bssfUnspecified': StepGeom_BSplineSurfaceForm.StepGeom_bssfUnspecified}
    pass
class StepGeom_BoundedSurface(StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
class StepGeom_BSplineSurface(StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
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
class StepGeom_BezierCurve(StepGeom_BSplineCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_BezierCurveAndRationalBSplineCurve(StepGeom_BSplineCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BezierCurve(self) -> StepGeom_BezierCurve: 
        """
        None
        """
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aBezierCurve : StepGeom_BezierCurve,aRationalBSplineCurve : StepGeom_RationalBSplineCurve) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
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
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def NbWeightsData(self) -> int: 
        """
        None
        """
    def RationalBSplineCurve(self) -> StepGeom_RationalBSplineCurve: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetBezierCurve(self,aBezierCurve : StepGeom_BezierCurve) -> None: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRationalBSplineCurve(self,aRationalBSplineCurve : StepGeom_RationalBSplineCurve) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num : int) -> float: 
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
class StepGeom_BezierSurface(StepGeom_BSplineSurface, StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
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
class StepGeom_BezierSurfaceAndRationalBSplineSurface(StepGeom_BSplineSurface, StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BezierSurface(self) -> StepGeom_BezierSurface: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aBezierSurface : StepGeom_BezierSurface,aRationalBSplineSurface : StepGeom_RationalBSplineSurface) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
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
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def NbWeightsDataI(self) -> int: 
        """
        None
        """
    def NbWeightsDataJ(self) -> int: 
        """
        None
        """
    def RationalBSplineSurface(self) -> StepGeom_RationalBSplineSurface: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetBezierSurface(self,aBezierSurface : StepGeom_BezierSurface) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRationalBSplineSurface(self,aRationalBSplineSurface : StepGeom_RationalBSplineSurface) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num1 : int,num2 : int) -> float: 
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
class StepGeom_CompositeCurve(StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSegments : StepGeom_HArray1OfCompositeCurveSegment,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbSegments(self) -> int: 
        """
        None
        """
    def Segments(self) -> StepGeom_HArray1OfCompositeCurveSegment: 
        """
        None
        """
    def SegmentsValue(self,num : int) -> StepGeom_CompositeCurveSegment: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSegments(self,aSegments : StepGeom_HArray1OfCompositeCurveSegment) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_BSplineCurveWithKnots(StepGeom_BSplineCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aKnotMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger,aKnots : OCP.TColStd.TColStd_HArray1OfReal,aKnotSpec : StepGeom_KnotType) -> None: 
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
    def KnotMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def KnotMultiplicitiesValue(self,num : int) -> int: 
        """
        None
        """
    def KnotSpec(self) -> StepGeom_KnotType: 
        """
        None
        """
    def Knots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def KnotsValue(self,num : int) -> float: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def NbKnotMultiplicities(self) -> int: 
        """
        None
        """
    def NbKnots(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetKnotMultiplicities(self,aKnotMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetKnotSpec(self,aKnotSpec : StepGeom_KnotType) -> None: 
        """
        None
        """
    def SetKnots(self,aKnots : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_BSplineSurfaceWithKnots(StepGeom_BSplineSurface, StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aUMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger,aVMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger,aUKnots : OCP.TColStd.TColStd_HArray1OfReal,aVKnots : OCP.TColStd.TColStd_HArray1OfReal,aKnotSpec : StepGeom_KnotType) -> None: 
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
    def KnotSpec(self) -> StepGeom_KnotType: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUMultiplicities(self) -> int: 
        """
        None
        """
    def NbVKnots(self) -> int: 
        """
        None
        """
    def NbVMultiplicities(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetKnotSpec(self,aKnotSpec : StepGeom_KnotType) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetUKnots(self,aUKnots : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def SetUMultiplicities(self,aUMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SetVKnots(self,aVKnots : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def SetVMultiplicities(self,aVMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UKnots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def UKnotsValue(self,num : int) -> float: 
        """
        None
        """
    def UMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def UMultiplicitiesValue(self,num : int) -> int: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    def VKnots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def VKnotsValue(self,num : int) -> float: 
        """
        None
        """
    def VMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def VMultiplicitiesValue(self,num : int) -> int: 
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
class StepGeom_Point(StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
class StepGeom_CartesianTransformationOperator(StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Axis1(self) -> StepGeom_Direction: 
        """
        None
        """
    def Axis2(self) -> StepGeom_Direction: 
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
    def HasAxis1(self) -> bool: 
        """
        None
        """
    def HasAxis2(self) -> bool: 
        """
        None
        """
    def HasScale(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasAaxis1 : bool,aAxis1 : StepGeom_Direction,hasAaxis2 : bool,aAxis2 : StepGeom_Direction,aLocalOrigin : StepGeom_CartesianPoint,hasAscale : bool,aScale : float) -> None: 
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
    def LocalOrigin(self) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Scale(self) -> float: 
        """
        None
        """
    def SetAxis1(self,aAxis1 : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetAxis2(self,aAxis2 : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetLocalOrigin(self,aLocalOrigin : StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetScale(self,aScale : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetAxis1(self) -> None: 
        """
        None
        """
    def UnSetAxis2(self) -> None: 
        """
        None
        """
    def UnSetScale(self) -> None: 
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
class StepGeom_CartesianTransformationOperator2d(StepGeom_CartesianTransformationOperator, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Added from StepGeom Rev2 to Rev4Added from StepGeom Rev2 to Rev4Added from StepGeom Rev2 to Rev4
    """
    def Axis1(self) -> StepGeom_Direction: 
        """
        None
        """
    def Axis2(self) -> StepGeom_Direction: 
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
    def HasAxis1(self) -> bool: 
        """
        None
        """
    def HasAxis2(self) -> bool: 
        """
        None
        """
    def HasScale(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasAaxis1 : bool,aAxis1 : StepGeom_Direction,hasAaxis2 : bool,aAxis2 : StepGeom_Direction,aLocalOrigin : StepGeom_CartesianPoint,hasAscale : bool,aScale : float) -> None: 
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
    def LocalOrigin(self) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Scale(self) -> float: 
        """
        None
        """
    def SetAxis1(self,aAxis1 : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetAxis2(self,aAxis2 : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetLocalOrigin(self,aLocalOrigin : StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetScale(self,aScale : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetAxis1(self) -> None: 
        """
        None
        """
    def UnSetAxis2(self) -> None: 
        """
        None
        """
    def UnSetScale(self) -> None: 
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
class StepGeom_CartesianTransformationOperator3d(StepGeom_CartesianTransformationOperator, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Axis1(self) -> StepGeom_Direction: 
        """
        None
        """
    def Axis2(self) -> StepGeom_Direction: 
        """
        None
        """
    def Axis3(self) -> StepGeom_Direction: 
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
    def HasAxis1(self) -> bool: 
        """
        None
        """
    def HasAxis2(self) -> bool: 
        """
        None
        """
    def HasAxis3(self) -> bool: 
        """
        None
        """
    def HasScale(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasAaxis1 : bool,aAxis1 : StepGeom_Direction,hasAaxis2 : bool,aAxis2 : StepGeom_Direction,aLocalOrigin : StepGeom_CartesianPoint,hasAscale : bool,aScale : float,hasAaxis3 : bool,aAxis3 : StepGeom_Direction) -> None: 
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
    def LocalOrigin(self) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Scale(self) -> float: 
        """
        None
        """
    def SetAxis1(self,aAxis1 : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetAxis2(self,aAxis2 : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetAxis3(self,aAxis3 : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetLocalOrigin(self,aLocalOrigin : StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetScale(self,aScale : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnSetAxis1(self) -> None: 
        """
        None
        """
    def UnSetAxis2(self) -> None: 
        """
        None
        """
    def UnSetAxis3(self) -> None: 
        """
        None
        """
    def UnSetScale(self) -> None: 
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
class StepGeom_Conic(StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement) -> None: 
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
class StepGeom_CompositeCurveOnSurface(StepGeom_CompositeCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSegments : StepGeom_HArray1OfCompositeCurveSegment,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbSegments(self) -> int: 
        """
        None
        """
    def Segments(self) -> StepGeom_HArray1OfCompositeCurveSegment: 
        """
        None
        """
    def SegmentsValue(self,num : int) -> StepGeom_CompositeCurveSegment: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSegments(self,aSegments : StepGeom_HArray1OfCompositeCurveSegment) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_BoundaryCurve(StepGeom_CompositeCurveOnSurface, StepGeom_CompositeCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSegments : StepGeom_HArray1OfCompositeCurveSegment,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbSegments(self) -> int: 
        """
        None
        """
    def Segments(self) -> StepGeom_HArray1OfCompositeCurveSegment: 
        """
        None
        """
    def SegmentsValue(self,num : int) -> StepGeom_CompositeCurveSegment: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSegments(self,aSegments : StepGeom_HArray1OfCompositeCurveSegment) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_CompositeCurveSegment(OCP.Standard.Standard_Transient):
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
    def Init(self,aTransition : StepGeom_TransitionCode,aSameSense : bool,aParentCurve : StepGeom_Curve) -> None: 
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
    def ParentCurve(self) -> StepGeom_Curve: 
        """
        None
        """
    def SameSense(self) -> bool: 
        """
        None
        """
    def SetParentCurve(self,aParentCurve : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetSameSense(self,aSameSense : bool) -> None: 
        """
        None
        """
    def SetTransition(self,aTransition : StepGeom_TransitionCode) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transition(self) -> StepGeom_TransitionCode: 
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
class StepGeom_Circle(StepGeom_Conic, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement,aRadius : float) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement: 
        """
        None
        """
    def Radius(self) -> float: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement) -> None: 
        """
        None
        """
    def SetRadius(self,aRadius : float) -> None: 
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
class StepGeom_ElementarySurface(StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement3d) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement3d: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement3d) -> None: 
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
class StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve(StepGeom_BSplineCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BSplineCurveWithKnots(self) -> StepGeom_BSplineCurveWithKnots: 
        """
        None
        """
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aBSplineCurveWithKnots : StepGeom_BSplineCurveWithKnots,aRationalBSplineCurve : StepGeom_RationalBSplineCurve) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aKnotMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger,aKnots : OCP.TColStd.TColStd_HArray1OfReal,aKnotSpec : StepGeom_KnotType,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def KnotMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def KnotMultiplicitiesValue(self,num : int) -> int: 
        """
        None
        """
    def KnotSpec(self) -> StepGeom_KnotType: 
        """
        None
        """
    def Knots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def KnotsValue(self,num : int) -> float: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def NbKnotMultiplicities(self) -> int: 
        """
        None
        """
    def NbKnots(self) -> int: 
        """
        None
        """
    def NbWeightsData(self) -> int: 
        """
        None
        """
    def RationalBSplineCurve(self) -> StepGeom_RationalBSplineCurve: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetBSplineCurveWithKnots(self,aBSplineCurveWithKnots : StepGeom_BSplineCurveWithKnots) -> None: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetKnotMultiplicities(self,aKnotMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetKnotSpec(self,aKnotSpec : StepGeom_KnotType) -> None: 
        """
        None
        """
    def SetKnots(self,aKnots : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRationalBSplineCurve(self,aRationalBSplineCurve : StepGeom_RationalBSplineCurve) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num : int) -> float: 
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
class StepGeom_CurveBoundedSurface(StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CurveBoundedSurfaceRepresentation of STEP entity CurveBoundedSurfaceRepresentation of STEP entity CurveBoundedSurface
    """
    def BasisSurface(self) -> StepGeom_Surface: 
        """
        Returns field BasisSurface
        """
    def Boundaries(self) -> StepGeom_HArray1OfSurfaceBoundary: 
        """
        Returns field Boundaries
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
    def ImplicitOuter(self) -> bool: 
        """
        Returns field ImplicitOuter
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aBasisSurface : StepGeom_Surface,aBoundaries : StepGeom_HArray1OfSurfaceBoundary,aImplicitOuter : bool) -> None: 
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
    def SetBasisSurface(self,BasisSurface : StepGeom_Surface) -> None: 
        """
        Set field BasisSurface
        """
    def SetBoundaries(self,Boundaries : StepGeom_HArray1OfSurfaceBoundary) -> None: 
        """
        Set field Boundaries
        """
    def SetImplicitOuter(self,ImplicitOuter : bool) -> None: 
        """
        Set field ImplicitOuter
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
class StepGeom_CurveOnSurface(OCP.StepData.StepData_SelectType):
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
        Recognizes a CurveOnSurface Kind Entity that is : 1 -> Pcurve 2 -> SurfaceCurve 3 -> CompositeCurveOnSurface 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CompositeCurveOnSurface(self) -> StepGeom_CompositeCurveOnSurface: 
        """
        returns Value as a CompositeCurveOnSurface (Null if another type)
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
    def Pcurve(self) -> StepGeom_Pcurve: 
        """
        returns Value as a Pcurve (Null if another type)
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
    def SurfaceCurve(self) -> StepGeom_SurfaceCurve: 
        """
        returns Value as a SurfaceCurve (Null if another type)
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
class StepGeom_CurveReplica(StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aParentCurve : StepGeom_Curve,aTransformation : StepGeom_CartesianTransformationOperator) -> None: 
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
    def ParentCurve(self) -> StepGeom_Curve: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetParentCurve(self,aParentCurve : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetTransformation(self,aTransformation : StepGeom_CartesianTransformationOperator) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transformation(self) -> StepGeom_CartesianTransformationOperator: 
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
class StepGeom_CylindricalSurface(StepGeom_ElementarySurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement3d,aRadius : float) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement3d: 
        """
        None
        """
    def Radius(self) -> float: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement3d) -> None: 
        """
        None
        """
    def SetRadius(self,aRadius : float) -> None: 
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
class StepGeom_DegeneratePcurve(StepGeom_Point, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BasisSurface(self) -> StepGeom_Surface: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBasisSurface : StepGeom_Surface,aReferenceToCurve : OCP.StepRepr.StepRepr_DefinitionalRepresentation) -> None: 
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
    def ReferenceToCurve(self) -> OCP.StepRepr.StepRepr_DefinitionalRepresentation: 
        """
        None
        """
    def SetBasisSurface(self,aBasisSurface : StepGeom_Surface) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetReferenceToCurve(self,aReferenceToCurve : OCP.StepRepr.StepRepr_DefinitionalRepresentation) -> None: 
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
class StepGeom_ToroidalSurface(StepGeom_ElementarySurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement3d,aMajorRadius : float,aMinorRadius : float) -> None: 
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
    def MajorRadius(self) -> float: 
        """
        None
        """
    def MinorRadius(self) -> float: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Position(self) -> StepGeom_Axis2Placement3d: 
        """
        None
        """
    def SetMajorRadius(self,aMajorRadius : float) -> None: 
        """
        None
        """
    def SetMinorRadius(self,aMinorRadius : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement3d) -> None: 
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
class StepGeom_Direction(StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirectionRatios(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def DirectionRatiosValue(self,num : int) -> float: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDirectionRatios : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
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
    def NbDirectionRatios(self) -> int: 
        """
        None
        """
    def SetDirectionRatios(self,aDirectionRatios : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
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
class StepGeom_ConicalSurface(StepGeom_ElementarySurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement3d,aRadius : float,aSemiAngle : float) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement3d: 
        """
        None
        """
    def Radius(self) -> float: 
        """
        None
        """
    def SemiAngle(self) -> float: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement3d) -> None: 
        """
        None
        """
    def SetRadius(self,aRadius : float) -> None: 
        """
        None
        """
    def SetSemiAngle(self,aSemiAngle : float) -> None: 
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
class StepGeom_Ellipse(StepGeom_Conic, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement,aSemiAxis1 : float,aSemiAxis2 : float) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement: 
        """
        None
        """
    def SemiAxis1(self) -> float: 
        """
        None
        """
    def SemiAxis2(self) -> float: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement) -> None: 
        """
        None
        """
    def SetSemiAxis1(self,aSemiAxis1 : float) -> None: 
        """
        None
        """
    def SetSemiAxis2(self,aSemiAxis2 : float) -> None: 
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
class StepGeom_EvaluatedDegeneratePcurve(StepGeom_DegeneratePcurve, StepGeom_Point, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BasisSurface(self) -> StepGeom_Surface: 
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
    def EquivalentPoint(self) -> StepGeom_CartesianPoint: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBasisSurface : StepGeom_Surface,aReferenceToCurve : OCP.StepRepr.StepRepr_DefinitionalRepresentation,aEquivalentPoint : StepGeom_CartesianPoint) -> None: 
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
    def ReferenceToCurve(self) -> OCP.StepRepr.StepRepr_DefinitionalRepresentation: 
        """
        None
        """
    def SetBasisSurface(self,aBasisSurface : StepGeom_Surface) -> None: 
        """
        None
        """
    def SetEquivalentPoint(self,aEquivalentPoint : StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetReferenceToCurve(self,aReferenceToCurve : OCP.StepRepr.StepRepr_DefinitionalRepresentation) -> None: 
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
class StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx(OCP.StepRepr.StepRepr_RepresentationContext, OCP.Standard.Standard_Transient):
    def ContextIdentifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ContextType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def CoordinateSpaceDimension(self) -> int: 
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
    def GeometricRepresentationContext(self) -> StepGeom_GeometricRepresentationContext: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlobalUncertaintyAssignedContext(self) -> OCP.StepRepr.StepRepr_GlobalUncertaintyAssignedContext: 
        """
        None
        """
    def GlobalUnitAssignedContext(self) -> OCP.StepRepr.StepRepr_GlobalUnitAssignedContext: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString,aCoordinateSpaceDimension : int,aUnits : OCP.StepBasic.StepBasic_HArray1OfNamedUnit,anUncertainty : OCP.StepBasic.StepBasic_HArray1OfUncertaintyMeasureWithUnit) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString,aGeometricRepresentationCtx : StepGeom_GeometricRepresentationContext,aGlobalUnitAssignedCtx : OCP.StepRepr.StepRepr_GlobalUnitAssignedContext,aGlobalUncertaintyAssignedCtx : OCP.StepRepr.StepRepr_GlobalUncertaintyAssignedContext) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
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
    def SetCoordinateSpaceDimension(self,aCoordinateSpaceDimension : int) -> None: 
        """
        None
        """
    def SetGeometricRepresentationContext(self,aGeometricRepresentationContext : StepGeom_GeometricRepresentationContext) -> None: 
        """
        None
        """
    def SetGlobalUncertaintyAssignedContext(self,aGlobalUncertaintyAssignedCtx : OCP.StepRepr.StepRepr_GlobalUncertaintyAssignedContext) -> None: 
        """
        None
        """
    def SetGlobalUnitAssignedContext(self,aGlobalUnitAssignedContext : OCP.StepRepr.StepRepr_GlobalUnitAssignedContext) -> None: 
        """
        None
        """
    def SetUncertainty(self,aUncertainty : OCP.StepBasic.StepBasic_HArray1OfUncertaintyMeasureWithUnit) -> None: 
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
    def Uncertainty(self) -> OCP.StepBasic.StepBasic_HArray1OfUncertaintyMeasureWithUnit: 
        """
        None
        """
    def UncertaintyValue(self,num : int) -> OCP.StepBasic.StepBasic_UncertaintyMeasureWithUnit: 
        """
        None
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
class StepGeom_GeometricRepresentationContext(OCP.StepRepr.StepRepr_RepresentationContext, OCP.Standard.Standard_Transient):
    def ContextIdentifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ContextType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def CoordinateSpaceDimension(self) -> int: 
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
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString,aCoordinateSpaceDimension : int) -> None: 
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
    def SetCoordinateSpaceDimension(self,aCoordinateSpaceDimension : int) -> None: 
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
class StepGeom_GeometricRepresentationContextAndGlobalUnitAssignedContext(OCP.StepRepr.StepRepr_RepresentationContext, OCP.Standard.Standard_Transient):
    def ContextIdentifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ContextType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def CoordinateSpaceDimension(self) -> int: 
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
    def GeometricRepresentationContext(self) -> StepGeom_GeometricRepresentationContext: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlobalUnitAssignedContext(self) -> OCP.StepRepr.StepRepr_GlobalUnitAssignedContext: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString,aCoordinateSpaceDimension : int,aUnits : OCP.StepBasic.StepBasic_HArray1OfNamedUnit) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString,aGeometricRepresentationContext : StepGeom_GeometricRepresentationContext,aGlobalUnitAssignedContext : OCP.StepRepr.StepRepr_GlobalUnitAssignedContext) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
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
    def SetCoordinateSpaceDimension(self,aCoordinateSpaceDimension : int) -> None: 
        """
        None
        """
    def SetGeometricRepresentationContext(self,aGeometricRepresentationContext : StepGeom_GeometricRepresentationContext) -> None: 
        """
        None
        """
    def SetGlobalUnitAssignedContext(self,aGlobalUnitAssignedContext : OCP.StepRepr.StepRepr_GlobalUnitAssignedContext) -> None: 
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
class StepGeom_GeometricRepresentationContextAndParametricRepresentationContext(OCP.StepRepr.StepRepr_RepresentationContext, OCP.Standard.Standard_Transient):
    def ContextIdentifier(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ContextType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def CoordinateSpaceDimension(self) -> int: 
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
    def GeometricRepresentationContext(self) -> StepGeom_GeometricRepresentationContext: 
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
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString,aCoordinateSpaceDimension : int) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aContextIdentifier : OCP.TCollection.TCollection_HAsciiString,aContextType : OCP.TCollection.TCollection_HAsciiString,aGeometricRepresentationContext : StepGeom_GeometricRepresentationContext,aParametricRepresentationContext : OCP.StepRepr.StepRepr_ParametricRepresentationContext) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def ParametricRepresentationContext(self) -> OCP.StepRepr.StepRepr_ParametricRepresentationContext: 
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
    def SetCoordinateSpaceDimension(self,aCoordinateSpaceDimension : int) -> None: 
        """
        None
        """
    def SetGeometricRepresentationContext(self,aGeometricRepresentationContext : StepGeom_GeometricRepresentationContext) -> None: 
        """
        None
        """
    def SetParametricRepresentationContext(self,aParametricRepresentationContext : OCP.StepRepr.StepRepr_ParametricRepresentationContext) -> None: 
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
class StepGeom_Axis1Placement(StepGeom_Placement, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Axis(self) -> StepGeom_Direction: 
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
    def HasAxis(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aLocation : StepGeom_CartesianPoint,hasAaxis : bool,aAxis : StepGeom_Direction) -> None: 
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
    def Location(self) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetAxis(self,aAxis : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetLocation(self,aLocation : StepGeom_CartesianPoint) -> None: 
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
    def UnSetAxis(self) -> None: 
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
class StepGeom_HArray1OfBoundaryCurve(StepGeom_Array1OfBoundaryCurve, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepGeom_Array1OfBoundaryCurve: 
        """
        None
        """
    def Assign(self,theOther : StepGeom_Array1OfBoundaryCurve) -> StepGeom_Array1OfBoundaryCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepGeom_Array1OfBoundaryCurve: 
        """
        None
        """
    def ChangeFirst(self) -> StepGeom_BoundaryCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_BoundaryCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_BoundaryCurve: 
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
    def First(self) -> StepGeom_BoundaryCurve: 
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
    def Init(self,theValue : StepGeom_BoundaryCurve) -> None: 
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
    def Last(self) -> StepGeom_BoundaryCurve: 
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
    def Move(self,theOther : StepGeom_Array1OfBoundaryCurve) -> StepGeom_Array1OfBoundaryCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_BoundaryCurve) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_BoundaryCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepGeom_BoundaryCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array1OfBoundaryCurve) -> None: ...
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
class StepGeom_HArray1OfCartesianPoint(StepGeom_Array1OfCartesianPoint, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepGeom_Array1OfCartesianPoint: 
        """
        None
        """
    def Assign(self,theOther : StepGeom_Array1OfCartesianPoint) -> StepGeom_Array1OfCartesianPoint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepGeom_Array1OfCartesianPoint: 
        """
        None
        """
    def ChangeFirst(self) -> StepGeom_CartesianPoint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_CartesianPoint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_CartesianPoint: 
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
    def First(self) -> StepGeom_CartesianPoint: 
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
    def Init(self,theValue : StepGeom_CartesianPoint) -> None: 
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
    def Last(self) -> StepGeom_CartesianPoint: 
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
    def Move(self,theOther : StepGeom_Array1OfCartesianPoint) -> StepGeom_Array1OfCartesianPoint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_CartesianPoint) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_CartesianPoint: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array1OfCartesianPoint) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepGeom_CartesianPoint) -> None: ...
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
class StepGeom_HArray1OfCompositeCurveSegment(StepGeom_Array1OfCompositeCurveSegment, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepGeom_Array1OfCompositeCurveSegment: 
        """
        None
        """
    def Assign(self,theOther : StepGeom_Array1OfCompositeCurveSegment) -> StepGeom_Array1OfCompositeCurveSegment: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepGeom_Array1OfCompositeCurveSegment: 
        """
        None
        """
    def ChangeFirst(self) -> StepGeom_CompositeCurveSegment: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_CompositeCurveSegment: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_CompositeCurveSegment: 
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
    def First(self) -> StepGeom_CompositeCurveSegment: 
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
    def Init(self,theValue : StepGeom_CompositeCurveSegment) -> None: 
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
    def Last(self) -> StepGeom_CompositeCurveSegment: 
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
    def Move(self,theOther : StepGeom_Array1OfCompositeCurveSegment) -> StepGeom_Array1OfCompositeCurveSegment: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_CompositeCurveSegment) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_CompositeCurveSegment: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepGeom_Array1OfCompositeCurveSegment) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepGeom_CompositeCurveSegment) -> None: ...
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
class StepGeom_HArray1OfCurve(StepGeom_Array1OfCurve, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepGeom_Array1OfCurve: 
        """
        None
        """
    def Assign(self,theOther : StepGeom_Array1OfCurve) -> StepGeom_Array1OfCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepGeom_Array1OfCurve: 
        """
        None
        """
    def ChangeFirst(self) -> StepGeom_Curve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_Curve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_Curve: 
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
    def First(self) -> StepGeom_Curve: 
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
    def Init(self,theValue : StepGeom_Curve) -> None: 
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
    def Last(self) -> StepGeom_Curve: 
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
    def Move(self,theOther : StepGeom_Array1OfCurve) -> StepGeom_Array1OfCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_Curve) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_Curve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepGeom_Array1OfCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepGeom_Curve) -> None: ...
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
class StepGeom_HArray1OfPcurveOrSurface(StepGeom_Array1OfPcurveOrSurface, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepGeom_Array1OfPcurveOrSurface: 
        """
        None
        """
    def Assign(self,theOther : StepGeom_Array1OfPcurveOrSurface) -> StepGeom_Array1OfPcurveOrSurface: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepGeom_Array1OfPcurveOrSurface: 
        """
        None
        """
    def ChangeFirst(self) -> StepGeom_PcurveOrSurface: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_PcurveOrSurface: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_PcurveOrSurface: 
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
    def First(self) -> StepGeom_PcurveOrSurface: 
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
    def Init(self,theValue : StepGeom_PcurveOrSurface) -> None: 
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
    def Last(self) -> StepGeom_PcurveOrSurface: 
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
    def Move(self,theOther : StepGeom_Array1OfPcurveOrSurface) -> StepGeom_Array1OfPcurveOrSurface: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_PcurveOrSurface) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_PcurveOrSurface: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array1OfPcurveOrSurface) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepGeom_PcurveOrSurface) -> None: ...
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
class StepGeom_HArray1OfSurfaceBoundary(StepGeom_Array1OfSurfaceBoundary, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepGeom_Array1OfSurfaceBoundary: 
        """
        None
        """
    def Assign(self,theOther : StepGeom_Array1OfSurfaceBoundary) -> StepGeom_Array1OfSurfaceBoundary: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepGeom_Array1OfSurfaceBoundary: 
        """
        None
        """
    def ChangeFirst(self) -> StepGeom_SurfaceBoundary: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_SurfaceBoundary: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_SurfaceBoundary: 
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
    def First(self) -> StepGeom_SurfaceBoundary: 
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
    def Init(self,theValue : StepGeom_SurfaceBoundary) -> None: 
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
    def Last(self) -> StepGeom_SurfaceBoundary: 
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
    def Move(self,theOther : StepGeom_Array1OfSurfaceBoundary) -> StepGeom_Array1OfSurfaceBoundary: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_SurfaceBoundary) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_SurfaceBoundary: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepGeom_Array1OfSurfaceBoundary) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepGeom_SurfaceBoundary) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
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
class StepGeom_HArray1OfTrimmingSelect(StepGeom_Array1OfTrimmingSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepGeom_Array1OfTrimmingSelect: 
        """
        None
        """
    def Assign(self,theOther : StepGeom_Array1OfTrimmingSelect) -> StepGeom_Array1OfTrimmingSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepGeom_Array1OfTrimmingSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepGeom_TrimmingSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepGeom_TrimmingSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepGeom_TrimmingSelect: 
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
    def First(self) -> StepGeom_TrimmingSelect: 
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
    def Init(self,theValue : StepGeom_TrimmingSelect) -> None: 
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
    def Last(self) -> StepGeom_TrimmingSelect: 
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
    def Move(self,theOther : StepGeom_Array1OfTrimmingSelect) -> StepGeom_Array1OfTrimmingSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepGeom_TrimmingSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepGeom_TrimmingSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepGeom_Array1OfTrimmingSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepGeom_TrimmingSelect) -> None: ...
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
class StepGeom_HArray2OfCartesianPoint(StepGeom_Array2OfCartesianPoint, OCP.Standard.Standard_Transient):
    def Array2(self) -> StepGeom_Array2OfCartesianPoint: 
        """
        None
        """
    def Assign(self,theOther : StepGeom_Array2OfCartesianPoint) -> StepGeom_Array2OfCartesianPoint: 
        """
        Assignment
        """
    def ChangeArray2(self) -> StepGeom_Array2OfCartesianPoint: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepGeom_CartesianPoint: 
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
    def Init(self,theValue : StepGeom_CartesianPoint) -> None: 
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
    def Move(self,theOther : StepGeom_Array2OfCartesianPoint) -> StepGeom_Array2OfCartesianPoint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : StepGeom_CartesianPoint) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> StepGeom_CartesianPoint: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepGeom_Array2OfCartesianPoint) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : StepGeom_CartesianPoint) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepGeom_HArray2OfSurfacePatch(StepGeom_Array2OfSurfacePatch, OCP.Standard.Standard_Transient):
    def Array2(self) -> StepGeom_Array2OfSurfacePatch: 
        """
        None
        """
    def Assign(self,theOther : StepGeom_Array2OfSurfacePatch) -> StepGeom_Array2OfSurfacePatch: 
        """
        Assignment
        """
    def ChangeArray2(self) -> StepGeom_Array2OfSurfacePatch: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> StepGeom_SurfacePatch: 
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
    def Init(self,theValue : StepGeom_SurfacePatch) -> None: 
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
    def Move(self,theOther : StepGeom_Array2OfSurfacePatch) -> StepGeom_Array2OfSurfacePatch: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def SetValue(self,theRow : int,theCol : int,theItem : StepGeom_SurfacePatch) -> None: 
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
    def Value(self,theRow : int,theCol : int) -> StepGeom_SurfacePatch: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int) -> None: ...
    @overload
    def __init__(self,theRowLow : int,theRowUpp : int,theColLow : int,theColUpp : int,theValue : StepGeom_SurfacePatch) -> None: ...
    @overload
    def __init__(self,theOther : StepGeom_Array2OfSurfacePatch) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class StepGeom_Hyperbola(StepGeom_Conic, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement,aSemiAxis : float,aSemiImagAxis : float) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement: 
        """
        None
        """
    def SemiAxis(self) -> float: 
        """
        None
        """
    def SemiImagAxis(self) -> float: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement) -> None: 
        """
        None
        """
    def SetSemiAxis(self,aSemiAxis : float) -> None: 
        """
        None
        """
    def SetSemiImagAxis(self,aSemiImagAxis : float) -> None: 
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
class StepGeom_SurfaceCurve(StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def AssociatedGeometry(self) -> StepGeom_HArray1OfPcurveOrSurface: 
        """
        None
        """
    def AssociatedGeometryValue(self,num : int) -> StepGeom_PcurveOrSurface: 
        """
        None
        """
    def Curve3d(self) -> StepGeom_Curve: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCurve3d : StepGeom_Curve,aAssociatedGeometry : StepGeom_HArray1OfPcurveOrSurface,aMasterRepresentation : StepGeom_PreferredSurfaceCurveRepresentation) -> None: 
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
    def MasterRepresentation(self) -> StepGeom_PreferredSurfaceCurveRepresentation: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbAssociatedGeometry(self) -> int: 
        """
        None
        """
    def SetAssociatedGeometry(self,aAssociatedGeometry : StepGeom_HArray1OfPcurveOrSurface) -> None: 
        """
        None
        """
    def SetCurve3d(self,aCurve3d : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetMasterRepresentation(self,aMasterRepresentation : StepGeom_PreferredSurfaceCurveRepresentation) -> None: 
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
class StepGeom_KnotType():
    """
    None

    Members:

      StepGeom_ktUniformKnots

      StepGeom_ktUnspecified

      StepGeom_ktQuasiUniformKnots

      StepGeom_ktPiecewiseBezierKnots
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
    StepGeom_ktPiecewiseBezierKnots: OCP.StepGeom.StepGeom_KnotType # value = StepGeom_KnotType.StepGeom_ktPiecewiseBezierKnots
    StepGeom_ktQuasiUniformKnots: OCP.StepGeom.StepGeom_KnotType # value = StepGeom_KnotType.StepGeom_ktQuasiUniformKnots
    StepGeom_ktUniformKnots: OCP.StepGeom.StepGeom_KnotType # value = StepGeom_KnotType.StepGeom_ktUniformKnots
    StepGeom_ktUnspecified: OCP.StepGeom.StepGeom_KnotType # value = StepGeom_KnotType.StepGeom_ktUnspecified
    __entries: dict # value = {'StepGeom_ktUniformKnots': (StepGeom_KnotType.StepGeom_ktUniformKnots, None), 'StepGeom_ktUnspecified': (StepGeom_KnotType.StepGeom_ktUnspecified, None), 'StepGeom_ktQuasiUniformKnots': (StepGeom_KnotType.StepGeom_ktQuasiUniformKnots, None), 'StepGeom_ktPiecewiseBezierKnots': (StepGeom_KnotType.StepGeom_ktPiecewiseBezierKnots, None)}
    __members__: dict # value = {'StepGeom_ktUniformKnots': StepGeom_KnotType.StepGeom_ktUniformKnots, 'StepGeom_ktUnspecified': StepGeom_KnotType.StepGeom_ktUnspecified, 'StepGeom_ktQuasiUniformKnots': StepGeom_KnotType.StepGeom_ktQuasiUniformKnots, 'StepGeom_ktPiecewiseBezierKnots': StepGeom_KnotType.StepGeom_ktPiecewiseBezierKnots}
    pass
class StepGeom_Line(StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dir(self) -> StepGeom_Vector: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPnt : StepGeom_CartesianPoint,aDir : StepGeom_Vector) -> None: 
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
    def Pnt(self) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def SetDir(self,aDir : StepGeom_Vector) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPnt(self,aPnt : StepGeom_CartesianPoint) -> None: 
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
class StepGeom_OffsetCurve3d(StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BasisCurve(self) -> StepGeom_Curve: 
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
    def Distance(self) -> float: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBasisCurve : StepGeom_Curve,aDistance : float,aSelfIntersect : OCP.StepData.StepData_Logical,aRefDirection : StepGeom_Direction) -> None: 
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
    def RefDirection(self) -> StepGeom_Direction: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetBasisCurve(self,aBasisCurve : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetDistance(self,aDistance : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRefDirection(self,aRefDirection : StepGeom_Direction) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_OffsetSurface(StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BasisSurface(self) -> StepGeom_Surface: 
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
    def Distance(self) -> float: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBasisSurface : StepGeom_Surface,aDistance : float,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetBasisSurface(self,aBasisSurface : StepGeom_Surface) -> None: 
        """
        None
        """
    def SetDistance(self,aDistance : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_OrientedSurface(StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity OrientedSurfaceRepresentation of STEP entity OrientedSurfaceRepresentation of STEP entity OrientedSurface
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aOrientation : bool) -> None: 
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
    def Orientation(self) -> bool: 
        """
        Returns field Orientation
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,Orientation : bool) -> None: 
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
class StepGeom_OuterBoundaryCurve(StepGeom_BoundaryCurve, StepGeom_CompositeCurveOnSurface, StepGeom_CompositeCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSegments : StepGeom_HArray1OfCompositeCurveSegment,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbSegments(self) -> int: 
        """
        None
        """
    def Segments(self) -> StepGeom_HArray1OfCompositeCurveSegment: 
        """
        None
        """
    def SegmentsValue(self,num : int) -> StepGeom_CompositeCurveSegment: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSegments(self,aSegments : StepGeom_HArray1OfCompositeCurveSegment) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_Parabola(StepGeom_Conic, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def FocalDist(self) -> float: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement,aFocalDist : float) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement: 
        """
        None
        """
    def SetFocalDist(self,aFocalDist : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement) -> None: 
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
class StepGeom_Pcurve(StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BasisSurface(self) -> StepGeom_Surface: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBasisSurface : StepGeom_Surface,aReferenceToCurve : OCP.StepRepr.StepRepr_DefinitionalRepresentation) -> None: 
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
    def ReferenceToCurve(self) -> OCP.StepRepr.StepRepr_DefinitionalRepresentation: 
        """
        None
        """
    def SetBasisSurface(self,aBasisSurface : StepGeom_Surface) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetReferenceToCurve(self,aReferenceToCurve : OCP.StepRepr.StepRepr_DefinitionalRepresentation) -> None: 
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
class StepGeom_PcurveOrSurface(OCP.StepData.StepData_SelectType):
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
        Recognizes a PcurveOrSurface Kind Entity that is : 1 -> Pcurve 2 -> Surface 0 else
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
    def Pcurve(self) -> StepGeom_Pcurve: 
        """
        returns Value as a Pcurve (Null if another type)
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
    def Surface(self) -> StepGeom_Surface: 
        """
        returns Value as a Surface (Null if another type)
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
class StepGeom_Axis2Placement2d(StepGeom_Placement, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def HasRefDirection(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aLocation : StepGeom_CartesianPoint,hasArefDirection : bool,aRefDirection : StepGeom_Direction) -> None: 
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
    def Location(self) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def RefDirection(self) -> StepGeom_Direction: 
        """
        None
        """
    def SetLocation(self,aLocation : StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRefDirection(self,aRefDirection : StepGeom_Direction) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class StepGeom_Plane(StepGeom_ElementarySurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement3d) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement3d: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement3d) -> None: 
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
class StepGeom_CartesianPoint(StepGeom_Point, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Coordinates(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def CoordinatesValue(self,num : int) -> float: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCoordinates : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def Init2D(self,aName : OCP.TCollection.TCollection_HAsciiString,X : float,Y : float) -> None: 
        """
        None
        """
    def Init3D(self,aName : OCP.TCollection.TCollection_HAsciiString,X : float,Y : float,Z : float) -> None: 
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
    def NbCoordinates(self) -> int: 
        """
        None
        """
    def SetCoordinates(self,aCoordinates : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
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
class StepGeom_PointOnCurve(StepGeom_Point, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BasisCurve(self) -> StepGeom_Curve: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBasisCurve : StepGeom_Curve,aPointParameter : float) -> None: 
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
    def PointParameter(self) -> float: 
        """
        None
        """
    def SetBasisCurve(self,aBasisCurve : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPointParameter(self,aPointParameter : float) -> None: 
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
class StepGeom_PointOnSurface(StepGeom_Point, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BasisSurface(self) -> StepGeom_Surface: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBasisSurface : StepGeom_Surface,aPointParameterU : float,aPointParameterV : float) -> None: 
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
    def PointParameterU(self) -> float: 
        """
        None
        """
    def PointParameterV(self) -> float: 
        """
        None
        """
    def SetBasisSurface(self,aBasisSurface : StepGeom_Surface) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPointParameterU(self,aPointParameterU : float) -> None: 
        """
        None
        """
    def SetPointParameterV(self,aPointParameterV : float) -> None: 
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
class StepGeom_PointReplica(StepGeom_Point, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aParentPt : StepGeom_Point,aTransformation : StepGeom_CartesianTransformationOperator) -> None: 
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
    def ParentPt(self) -> StepGeom_Point: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetParentPt(self,aParentPt : StepGeom_Point) -> None: 
        """
        None
        """
    def SetTransformation(self,aTransformation : StepGeom_CartesianTransformationOperator) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transformation(self) -> StepGeom_CartesianTransformationOperator: 
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
class StepGeom_Polyline(StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPoints : StepGeom_HArray1OfCartesianPoint) -> None: 
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
    def NbPoints(self) -> int: 
        """
        None
        """
    def Points(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def PointsValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPoints(self,aPoints : StepGeom_HArray1OfCartesianPoint) -> None: 
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
class StepGeom_PreferredSurfaceCurveRepresentation():
    """
    None

    Members:

      StepGeom_pscrCurve3d

      StepGeom_pscrPcurveS1

      StepGeom_pscrPcurveS2
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
    StepGeom_pscrCurve3d: OCP.StepGeom.StepGeom_PreferredSurfaceCurveRepresentation # value = StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrCurve3d
    StepGeom_pscrPcurveS1: OCP.StepGeom.StepGeom_PreferredSurfaceCurveRepresentation # value = StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrPcurveS1
    StepGeom_pscrPcurveS2: OCP.StepGeom.StepGeom_PreferredSurfaceCurveRepresentation # value = StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrPcurveS2
    __entries: dict # value = {'StepGeom_pscrCurve3d': (StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrCurve3d, None), 'StepGeom_pscrPcurveS1': (StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrPcurveS1, None), 'StepGeom_pscrPcurveS2': (StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrPcurveS2, None)}
    __members__: dict # value = {'StepGeom_pscrCurve3d': StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrCurve3d, 'StepGeom_pscrPcurveS1': StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrPcurveS1, 'StepGeom_pscrPcurveS2': StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrPcurveS2}
    pass
class StepGeom_QuasiUniformCurve(StepGeom_BSplineCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_QuasiUniformCurveAndRationalBSplineCurve(StepGeom_BSplineCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aQuasiUniformCurve : StepGeom_QuasiUniformCurve,aRationalBSplineCurve : StepGeom_RationalBSplineCurve) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
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
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def NbWeightsData(self) -> int: 
        """
        None
        """
    def QuasiUniformCurve(self) -> StepGeom_QuasiUniformCurve: 
        """
        None
        """
    def RationalBSplineCurve(self) -> StepGeom_RationalBSplineCurve: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetQuasiUniformCurve(self,aQuasiUniformCurve : StepGeom_QuasiUniformCurve) -> None: 
        """
        None
        """
    def SetRationalBSplineCurve(self,aRationalBSplineCurve : StepGeom_RationalBSplineCurve) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num : int) -> float: 
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
class StepGeom_QuasiUniformSurface(StepGeom_BSplineSurface, StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
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
class StepGeom_QuasiUniformSurfaceAndRationalBSplineSurface(StepGeom_BSplineSurface, StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aQuasiUniformSurface : StepGeom_QuasiUniformSurface,aRationalBSplineSurface : StepGeom_RationalBSplineSurface) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
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
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def NbWeightsDataI(self) -> int: 
        """
        None
        """
    def NbWeightsDataJ(self) -> int: 
        """
        None
        """
    def QuasiUniformSurface(self) -> StepGeom_QuasiUniformSurface: 
        """
        None
        """
    def RationalBSplineSurface(self) -> StepGeom_RationalBSplineSurface: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetQuasiUniformSurface(self,aQuasiUniformSurface : StepGeom_QuasiUniformSurface) -> None: 
        """
        None
        """
    def SetRationalBSplineSurface(self,aRationalBSplineSurface : StepGeom_RationalBSplineSurface) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num1 : int,num2 : int) -> float: 
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
class StepGeom_RationalBSplineCurve(StepGeom_BSplineCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
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
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def NbWeightsData(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num : int) -> float: 
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
class StepGeom_RationalBSplineSurface(StepGeom_BSplineSurface, StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
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
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def NbWeightsDataI(self) -> int: 
        """
        None
        """
    def NbWeightsDataJ(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num1 : int,num2 : int) -> float: 
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
class StepGeom_RectangularCompositeSurface(StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSegments : StepGeom_HArray2OfSurfacePatch) -> None: 
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
    def NbSegmentsI(self) -> int: 
        """
        None
        """
    def NbSegmentsJ(self) -> int: 
        """
        None
        """
    def Segments(self) -> StepGeom_HArray2OfSurfacePatch: 
        """
        None
        """
    def SegmentsValue(self,num1 : int,num2 : int) -> StepGeom_SurfacePatch: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSegments(self,aSegments : StepGeom_HArray2OfSurfacePatch) -> None: 
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
class StepGeom_RectangularTrimmedSurface(StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BasisSurface(self) -> StepGeom_Surface: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBasisSurface : StepGeom_Surface,aU1 : float,aU2 : float,aV1 : float,aV2 : float,aUsense : bool,aVsense : bool) -> None: 
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
    def SetBasisSurface(self,aBasisSurface : StepGeom_Surface) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetU1(self,aU1 : float) -> None: 
        """
        None
        """
    def SetU2(self,aU2 : float) -> None: 
        """
        None
        """
    def SetUsense(self,aUsense : bool) -> None: 
        """
        None
        """
    def SetV1(self,aV1 : float) -> None: 
        """
        None
        """
    def SetV2(self,aV2 : float) -> None: 
        """
        None
        """
    def SetVsense(self,aVsense : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def U1(self) -> float: 
        """
        None
        """
    def U2(self) -> float: 
        """
        None
        """
    def Usense(self) -> bool: 
        """
        None
        """
    def V1(self) -> float: 
        """
        None
        """
    def V2(self) -> float: 
        """
        None
        """
    def Vsense(self) -> bool: 
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
class StepGeom_ReparametrisedCompositeCurveSegment(StepGeom_CompositeCurveSegment, OCP.Standard.Standard_Transient):
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
    def Init(self,aTransition : StepGeom_TransitionCode,aSameSense : bool,aParentCurve : StepGeom_Curve,aParamLength : float) -> None: 
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
    def ParamLength(self) -> float: 
        """
        None
        """
    def ParentCurve(self) -> StepGeom_Curve: 
        """
        None
        """
    def SameSense(self) -> bool: 
        """
        None
        """
    def SetParamLength(self,aParamLength : float) -> None: 
        """
        None
        """
    def SetParentCurve(self,aParentCurve : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetSameSense(self,aSameSense : bool) -> None: 
        """
        None
        """
    def SetTransition(self,aTransition : StepGeom_TransitionCode) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transition(self) -> StepGeom_TransitionCode: 
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
class StepGeom_SeamCurve(StepGeom_SurfaceCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def AssociatedGeometry(self) -> StepGeom_HArray1OfPcurveOrSurface: 
        """
        None
        """
    def AssociatedGeometryValue(self,num : int) -> StepGeom_PcurveOrSurface: 
        """
        None
        """
    def Curve3d(self) -> StepGeom_Curve: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCurve3d : StepGeom_Curve,aAssociatedGeometry : StepGeom_HArray1OfPcurveOrSurface,aMasterRepresentation : StepGeom_PreferredSurfaceCurveRepresentation) -> None: 
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
    def MasterRepresentation(self) -> StepGeom_PreferredSurfaceCurveRepresentation: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbAssociatedGeometry(self) -> int: 
        """
        None
        """
    def SetAssociatedGeometry(self,aAssociatedGeometry : StepGeom_HArray1OfPcurveOrSurface) -> None: 
        """
        None
        """
    def SetCurve3d(self,aCurve3d : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetMasterRepresentation(self,aMasterRepresentation : StepGeom_PreferredSurfaceCurveRepresentation) -> None: 
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
class StepGeom_SphericalSurface(StepGeom_ElementarySurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement3d,aRadius : float) -> None: 
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
    def Position(self) -> StepGeom_Axis2Placement3d: 
        """
        None
        """
    def Radius(self) -> float: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement3d) -> None: 
        """
        None
        """
    def SetRadius(self,aRadius : float) -> None: 
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
class StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface(StepGeom_BSplineSurface, StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BSplineSurfaceWithKnots(self) -> StepGeom_BSplineSurfaceWithKnots: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aBSplineSurfaceWithKnots : StepGeom_BSplineSurfaceWithKnots,aRationalBSplineSurface : StepGeom_RationalBSplineSurface) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aUMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger,aVMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger,aUKnots : OCP.TColStd.TColStd_HArray1OfReal,aVKnots : OCP.TColStd.TColStd_HArray1OfReal,aKnotSpec : StepGeom_KnotType,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def KnotSpec(self) -> StepGeom_KnotType: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def NbUKnots(self) -> int: 
        """
        None
        """
    def NbUMultiplicities(self) -> int: 
        """
        None
        """
    def NbVKnots(self) -> int: 
        """
        None
        """
    def NbVMultiplicities(self) -> int: 
        """
        None
        """
    def NbWeightsDataI(self) -> int: 
        """
        None
        """
    def NbWeightsDataJ(self) -> int: 
        """
        None
        """
    def RationalBSplineSurface(self) -> StepGeom_RationalBSplineSurface: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetBSplineSurfaceWithKnots(self,aBSplineSurfaceWithKnots : StepGeom_BSplineSurfaceWithKnots) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetKnotSpec(self,aKnotSpec : StepGeom_KnotType) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRationalBSplineSurface(self,aRationalBSplineSurface : StepGeom_RationalBSplineSurface) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetUKnots(self,aUKnots : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def SetUMultiplicities(self,aUMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SetVKnots(self,aVKnots : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def SetVMultiplicities(self,aVMultiplicities : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UKnots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def UKnotsValue(self,num : int) -> float: 
        """
        None
        """
    def UMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def UMultiplicitiesValue(self,num : int) -> int: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    def VKnots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def VKnotsValue(self,num : int) -> float: 
        """
        None
        """
    def VMultiplicities(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def VMultiplicitiesValue(self,num : int) -> int: 
        """
        None
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num1 : int,num2 : int) -> float: 
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
class StepGeom_SurfaceBoundary(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type SurfaceBoundary
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def BoundaryCurve(self) -> StepGeom_BoundaryCurve: 
        """
        Returns Value as BoundaryCurve (or Null if another type)
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
        Recognizes a kind of SurfaceBoundary select type 1 -> BoundaryCurve from StepGeom 2 -> DegeneratePcurve from StepGeom 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def DegeneratePcurve(self) -> StepGeom_DegeneratePcurve: 
        """
        Returns Value as DegeneratePcurve (or Null if another type)
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
class StepGeom_IntersectionCurve(StepGeom_SurfaceCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def AssociatedGeometry(self) -> StepGeom_HArray1OfPcurveOrSurface: 
        """
        None
        """
    def AssociatedGeometryValue(self,num : int) -> StepGeom_PcurveOrSurface: 
        """
        None
        """
    def Curve3d(self) -> StepGeom_Curve: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCurve3d : StepGeom_Curve,aAssociatedGeometry : StepGeom_HArray1OfPcurveOrSurface,aMasterRepresentation : StepGeom_PreferredSurfaceCurveRepresentation) -> None: 
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
    def MasterRepresentation(self) -> StepGeom_PreferredSurfaceCurveRepresentation: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbAssociatedGeometry(self) -> int: 
        """
        None
        """
    def SetAssociatedGeometry(self,aAssociatedGeometry : StepGeom_HArray1OfPcurveOrSurface) -> None: 
        """
        None
        """
    def SetCurve3d(self,aCurve3d : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetMasterRepresentation(self,aMasterRepresentation : StepGeom_PreferredSurfaceCurveRepresentation) -> None: 
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
class StepGeom_SurfaceCurveAndBoundedCurve(StepGeom_SurfaceCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    complex type: bounded_curve + surface_curve needed for curve_bounded_surfaces (S4132)complex type: bounded_curve + surface_curve needed for curve_bounded_surfaces (S4132)complex type: bounded_curve + surface_curve needed for curve_bounded_surfaces (S4132)
    """
    def AssociatedGeometry(self) -> StepGeom_HArray1OfPcurveOrSurface: 
        """
        None
        """
    def AssociatedGeometryValue(self,num : int) -> StepGeom_PcurveOrSurface: 
        """
        None
        """
    def BoundedCurve(self) -> StepGeom_BoundedCurve: 
        """
        returns field BoundedCurve
        """
    def Curve3d(self) -> StepGeom_Curve: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCurve3d : StepGeom_Curve,aAssociatedGeometry : StepGeom_HArray1OfPcurveOrSurface,aMasterRepresentation : StepGeom_PreferredSurfaceCurveRepresentation) -> None: 
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
    def MasterRepresentation(self) -> StepGeom_PreferredSurfaceCurveRepresentation: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbAssociatedGeometry(self) -> int: 
        """
        None
        """
    def SetAssociatedGeometry(self,aAssociatedGeometry : StepGeom_HArray1OfPcurveOrSurface) -> None: 
        """
        None
        """
    def SetCurve3d(self,aCurve3d : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetMasterRepresentation(self,aMasterRepresentation : StepGeom_PreferredSurfaceCurveRepresentation) -> None: 
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
class StepGeom_SweptSurface(StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptCurve : StepGeom_Curve) -> None: 
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
    def SetSweptCurve(self,aSweptCurve : StepGeom_Curve) -> None: 
        """
        None
        """
    def SweptCurve(self) -> StepGeom_Curve: 
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
class StepGeom_SurfaceOfRevolution(StepGeom_SweptSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def AxisPosition(self) -> StepGeom_Axis1Placement: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptCurve : StepGeom_Curve,aAxisPosition : StepGeom_Axis1Placement) -> None: 
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
    def SetAxisPosition(self,aAxisPosition : StepGeom_Axis1Placement) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSweptCurve(self,aSweptCurve : StepGeom_Curve) -> None: 
        """
        None
        """
    def SweptCurve(self) -> StepGeom_Curve: 
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
class StepGeom_SurfacePatch(OCP.Standard.Standard_Transient):
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
    def Init(self,aParentSurface : StepGeom_BoundedSurface,aUTransition : StepGeom_TransitionCode,aVTransition : StepGeom_TransitionCode,aUSense : bool,aVSense : bool) -> None: 
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
    def ParentSurface(self) -> StepGeom_BoundedSurface: 
        """
        None
        """
    def SetParentSurface(self,aParentSurface : StepGeom_BoundedSurface) -> None: 
        """
        None
        """
    def SetUSense(self,aUSense : bool) -> None: 
        """
        None
        """
    def SetUTransition(self,aUTransition : StepGeom_TransitionCode) -> None: 
        """
        None
        """
    def SetVSense(self,aVSense : bool) -> None: 
        """
        None
        """
    def SetVTransition(self,aVTransition : StepGeom_TransitionCode) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def USense(self) -> bool: 
        """
        None
        """
    def UTransition(self) -> StepGeom_TransitionCode: 
        """
        None
        """
    def VSense(self) -> bool: 
        """
        None
        """
    def VTransition(self) -> StepGeom_TransitionCode: 
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
class StepGeom_SurfaceReplica(StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aParentSurface : StepGeom_Surface,aTransformation : StepGeom_CartesianTransformationOperator3d) -> None: 
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
    def ParentSurface(self) -> StepGeom_Surface: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetParentSurface(self,aParentSurface : StepGeom_Surface) -> None: 
        """
        None
        """
    def SetTransformation(self,aTransformation : StepGeom_CartesianTransformationOperator3d) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transformation(self) -> StepGeom_CartesianTransformationOperator3d: 
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
class StepGeom_SurfaceOfLinearExtrusion(StepGeom_SweptSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def ExtrusionAxis(self) -> StepGeom_Vector: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptCurve : StepGeom_Curve,aExtrusionAxis : StepGeom_Vector) -> None: 
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
    def SetExtrusionAxis(self,aExtrusionAxis : StepGeom_Vector) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSweptCurve(self,aSweptCurve : StepGeom_Curve) -> None: 
        """
        None
        """
    def SweptCurve(self) -> StepGeom_Curve: 
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
class StepGeom_DegenerateToroidalSurface(StepGeom_ToroidalSurface, StepGeom_ElementarySurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : StepGeom_Axis2Placement3d,aMajorRadius : float,aMinorRadius : float,aSelectOuter : bool) -> None: 
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
    def MajorRadius(self) -> float: 
        """
        None
        """
    def MinorRadius(self) -> float: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Position(self) -> StepGeom_Axis2Placement3d: 
        """
        None
        """
    def SelectOuter(self) -> bool: 
        """
        None
        """
    def SetMajorRadius(self,aMajorRadius : float) -> None: 
        """
        None
        """
    def SetMinorRadius(self,aMinorRadius : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : StepGeom_Axis2Placement3d) -> None: 
        """
        None
        """
    def SetSelectOuter(self,aSelectOuter : bool) -> None: 
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
class StepGeom_TransitionCode():
    """
    None

    Members:

      StepGeom_tcDiscontinuous

      StepGeom_tcContinuous

      StepGeom_tcContSameGradient

      StepGeom_tcContSameGradientSameCurvature
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
    StepGeom_tcContSameGradient: OCP.StepGeom.StepGeom_TransitionCode # value = StepGeom_TransitionCode.StepGeom_tcContSameGradient
    StepGeom_tcContSameGradientSameCurvature: OCP.StepGeom.StepGeom_TransitionCode # value = StepGeom_TransitionCode.StepGeom_tcContSameGradientSameCurvature
    StepGeom_tcContinuous: OCP.StepGeom.StepGeom_TransitionCode # value = StepGeom_TransitionCode.StepGeom_tcContinuous
    StepGeom_tcDiscontinuous: OCP.StepGeom.StepGeom_TransitionCode # value = StepGeom_TransitionCode.StepGeom_tcDiscontinuous
    __entries: dict # value = {'StepGeom_tcDiscontinuous': (StepGeom_TransitionCode.StepGeom_tcDiscontinuous, None), 'StepGeom_tcContinuous': (StepGeom_TransitionCode.StepGeom_tcContinuous, None), 'StepGeom_tcContSameGradient': (StepGeom_TransitionCode.StepGeom_tcContSameGradient, None), 'StepGeom_tcContSameGradientSameCurvature': (StepGeom_TransitionCode.StepGeom_tcContSameGradientSameCurvature, None)}
    __members__: dict # value = {'StepGeom_tcDiscontinuous': StepGeom_TransitionCode.StepGeom_tcDiscontinuous, 'StepGeom_tcContinuous': StepGeom_TransitionCode.StepGeom_tcContinuous, 'StepGeom_tcContSameGradient': StepGeom_TransitionCode.StepGeom_tcContSameGradient, 'StepGeom_tcContSameGradientSameCurvature': StepGeom_TransitionCode.StepGeom_tcContSameGradientSameCurvature}
    pass
class StepGeom_TrimmedCurve(StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BasisCurve(self) -> StepGeom_Curve: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBasisCurve : StepGeom_Curve,aTrim1 : StepGeom_HArray1OfTrimmingSelect,aTrim2 : StepGeom_HArray1OfTrimmingSelect,aSenseAgreement : bool,aMasterRepresentation : StepGeom_TrimmingPreference) -> None: 
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
    def MasterRepresentation(self) -> StepGeom_TrimmingPreference: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbTrim1(self) -> int: 
        """
        None
        """
    def NbTrim2(self) -> int: 
        """
        None
        """
    def SenseAgreement(self) -> bool: 
        """
        None
        """
    def SetBasisCurve(self,aBasisCurve : StepGeom_Curve) -> None: 
        """
        None
        """
    def SetMasterRepresentation(self,aMasterRepresentation : StepGeom_TrimmingPreference) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSenseAgreement(self,aSenseAgreement : bool) -> None: 
        """
        None
        """
    def SetTrim1(self,aTrim1 : StepGeom_HArray1OfTrimmingSelect) -> None: 
        """
        None
        """
    def SetTrim2(self,aTrim2 : StepGeom_HArray1OfTrimmingSelect) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim1(self) -> StepGeom_HArray1OfTrimmingSelect: 
        """
        None
        """
    def Trim1Value(self,num : int) -> StepGeom_TrimmingSelect: 
        """
        None
        """
    def Trim2(self) -> StepGeom_HArray1OfTrimmingSelect: 
        """
        None
        """
    def Trim2Value(self,num : int) -> StepGeom_TrimmingSelect: 
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
class StepGeom_TrimmingMember(OCP.StepData.StepData_SelectReal, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    For immediate members of TrimmingSelect, i.e. : ParameterValue (a Real)For immediate members of TrimmingSelect, i.e. : ParameterValue (a Real)For immediate members of TrimmingSelect, i.e. : ParameterValue (a Real)
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
class StepGeom_TrimmingPreference():
    """
    None

    Members:

      StepGeom_tpCartesian

      StepGeom_tpParameter

      StepGeom_tpUnspecified
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
    StepGeom_tpCartesian: OCP.StepGeom.StepGeom_TrimmingPreference # value = StepGeom_TrimmingPreference.StepGeom_tpCartesian
    StepGeom_tpParameter: OCP.StepGeom.StepGeom_TrimmingPreference # value = StepGeom_TrimmingPreference.StepGeom_tpParameter
    StepGeom_tpUnspecified: OCP.StepGeom.StepGeom_TrimmingPreference # value = StepGeom_TrimmingPreference.StepGeom_tpUnspecified
    __entries: dict # value = {'StepGeom_tpCartesian': (StepGeom_TrimmingPreference.StepGeom_tpCartesian, None), 'StepGeom_tpParameter': (StepGeom_TrimmingPreference.StepGeom_tpParameter, None), 'StepGeom_tpUnspecified': (StepGeom_TrimmingPreference.StepGeom_tpUnspecified, None)}
    __members__: dict # value = {'StepGeom_tpCartesian': StepGeom_TrimmingPreference.StepGeom_tpCartesian, 'StepGeom_tpParameter': StepGeom_TrimmingPreference.StepGeom_tpParameter, 'StepGeom_tpUnspecified': StepGeom_TrimmingPreference.StepGeom_tpUnspecified}
    pass
class StepGeom_TrimmingSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CartesianPoint(self) -> StepGeom_CartesianPoint: 
        """
        returns Value as a CartesianPoint (Null if another type)
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognizes a SelectMember as Real, named as PARAMETER_VALUE 1 -> ParameterValue i.e. Real 0 else (i.e. Entity)
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a TrimmingSelect Kind Entity that is : 1 -> CartesianPoint 0 else (i.e. Real)
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
        Returns a TrimmingMember (for PARAMETER_VALUE) as preferred
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def ParameterValue(self) -> float: 
        """
        returns Value as a Real (0.0 if not a Real)
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
    def SetParameterValue(self,aParameterValue : float) -> None: 
        """
        sets the ParameterValue as Real
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
class StepGeom_UniformCurve(StepGeom_BSplineCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
class StepGeom_UniformCurveAndRationalBSplineCurve(StepGeom_BSplineCurve, StepGeom_BoundedCurve, StepGeom_Curve, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ClosedCurve(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def ControlPointsList(self) -> StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num : int) -> StepGeom_CartesianPoint: 
        """
        None
        """
    def CurveForm(self) -> StepGeom_BSplineCurveForm: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
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
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aUniformCurve : StepGeom_UniformCurve,aRationalBSplineCurve : StepGeom_RationalBSplineCurve) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDegree : int,aControlPointsList : StepGeom_HArray1OfCartesianPoint,aCurveForm : StepGeom_BSplineCurveForm,aClosedCurve : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
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
    def NbControlPointsList(self) -> int: 
        """
        None
        """
    def NbWeightsData(self) -> int: 
        """
        None
        """
    def RationalBSplineCurve(self) -> StepGeom_RationalBSplineCurve: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetClosedCurve(self,aClosedCurve : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
        """
    def SetCurveForm(self,aCurveForm : StepGeom_BSplineCurveForm) -> None: 
        """
        None
        """
    def SetDegree(self,aDegree : int) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRationalBSplineCurve(self,aRationalBSplineCurve : StepGeom_RationalBSplineCurve) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUniformCurve(self,aUniformCurve : StepGeom_UniformCurve) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniformCurve(self) -> StepGeom_UniformCurve: 
        """
        None
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num : int) -> float: 
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
class StepGeom_UniformSurface(StepGeom_BSplineSurface, StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
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
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
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
class StepGeom_UniformSurfaceAndRationalBSplineSurface(StepGeom_BSplineSurface, StepGeom_BoundedSurface, StepGeom_Surface, StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def ControlPointsList(self) -> StepGeom_HArray2OfCartesianPoint: 
        """
        None
        """
    def ControlPointsListValue(self,num1 : int,num2 : int) -> StepGeom_CartesianPoint: 
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
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aUniformSurface : StepGeom_UniformSurface,aRationalBSplineSurface : StepGeom_RationalBSplineSurface) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aUDegree : int,aVDegree : int,aControlPointsList : StepGeom_HArray2OfCartesianPoint,aSurfaceForm : StepGeom_BSplineSurfaceForm,aUClosed : OCP.StepData.StepData_Logical,aVClosed : OCP.StepData.StepData_Logical,aSelfIntersect : OCP.StepData.StepData_Logical,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: ...
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
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
    def NbControlPointsListI(self) -> int: 
        """
        None
        """
    def NbControlPointsListJ(self) -> int: 
        """
        None
        """
    def NbWeightsDataI(self) -> int: 
        """
        None
        """
    def NbWeightsDataJ(self) -> int: 
        """
        None
        """
    def RationalBSplineSurface(self) -> StepGeom_RationalBSplineSurface: 
        """
        None
        """
    def SelfIntersect(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def SetControlPointsList(self,aControlPointsList : StepGeom_HArray2OfCartesianPoint) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRationalBSplineSurface(self,aRationalBSplineSurface : StepGeom_RationalBSplineSurface) -> None: 
        """
        None
        """
    def SetSelfIntersect(self,aSelfIntersect : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetSurfaceForm(self,aSurfaceForm : StepGeom_BSplineSurfaceForm) -> None: 
        """
        None
        """
    def SetUClosed(self,aUClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetUDegree(self,aUDegree : int) -> None: 
        """
        None
        """
    def SetUniformSurface(self,aUniformSurface : StepGeom_UniformSurface) -> None: 
        """
        None
        """
    def SetVClosed(self,aVClosed : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetVDegree(self,aVDegree : int) -> None: 
        """
        None
        """
    def SetWeightsData(self,aWeightsData : OCP.TColStd.TColStd_HArray2OfReal) -> None: 
        """
        None
        """
    def SurfaceForm(self) -> StepGeom_BSplineSurfaceForm: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def UniformSurface(self) -> StepGeom_UniformSurface: 
        """
        None
        """
    def VClosed(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    def WeightsData(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def WeightsDataValue(self,num1 : int,num2 : int) -> float: 
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
class StepGeom_Vector(StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOrientation : StepGeom_Direction,aMagnitude : float) -> None: 
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
    def Magnitude(self) -> float: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Orientation(self) -> StepGeom_Direction: 
        """
        None
        """
    def SetMagnitude(self,aMagnitude : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : StepGeom_Direction) -> None: 
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
class StepGeom_VectorOrDirection(OCP.StepData.StepData_SelectType):
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
        Recognizes a VectorOrDirection Kind Entity that is : 1 -> Vector 2 -> Direction 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Direction(self) -> StepGeom_Direction: 
        """
        returns Value as a Direction (Null if another type)
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
    def Vector(self) -> StepGeom_Vector: 
        """
        returns Value as a Vector (Null if another type)
        """
    def __init__(self) -> None: ...
    pass
StepGeom_bscfCircularArc: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfCircularArc
StepGeom_bscfEllipticArc: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfEllipticArc
StepGeom_bscfHyperbolicArc: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfHyperbolicArc
StepGeom_bscfParabolicArc: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfParabolicArc
StepGeom_bscfPolylineForm: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfPolylineForm
StepGeom_bscfUnspecified: OCP.StepGeom.StepGeom_BSplineCurveForm # value = StepGeom_BSplineCurveForm.StepGeom_bscfUnspecified
StepGeom_bssfConicalSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfConicalSurf
StepGeom_bssfCylindricalSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfCylindricalSurf
StepGeom_bssfGeneralisedCone: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfGeneralisedCone
StepGeom_bssfPlaneSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfPlaneSurf
StepGeom_bssfQuadricSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfQuadricSurf
StepGeom_bssfRuledSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfRuledSurf
StepGeom_bssfSphericalSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfSphericalSurf
StepGeom_bssfSurfOfLinearExtrusion: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfSurfOfLinearExtrusion
StepGeom_bssfSurfOfRevolution: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfSurfOfRevolution
StepGeom_bssfToroidalSurf: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfToroidalSurf
StepGeom_bssfUnspecified: OCP.StepGeom.StepGeom_BSplineSurfaceForm # value = StepGeom_BSplineSurfaceForm.StepGeom_bssfUnspecified
StepGeom_ktPiecewiseBezierKnots: OCP.StepGeom.StepGeom_KnotType # value = StepGeom_KnotType.StepGeom_ktPiecewiseBezierKnots
StepGeom_ktQuasiUniformKnots: OCP.StepGeom.StepGeom_KnotType # value = StepGeom_KnotType.StepGeom_ktQuasiUniformKnots
StepGeom_ktUniformKnots: OCP.StepGeom.StepGeom_KnotType # value = StepGeom_KnotType.StepGeom_ktUniformKnots
StepGeom_ktUnspecified: OCP.StepGeom.StepGeom_KnotType # value = StepGeom_KnotType.StepGeom_ktUnspecified
StepGeom_pscrCurve3d: OCP.StepGeom.StepGeom_PreferredSurfaceCurveRepresentation # value = StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrCurve3d
StepGeom_pscrPcurveS1: OCP.StepGeom.StepGeom_PreferredSurfaceCurveRepresentation # value = StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrPcurveS1
StepGeom_pscrPcurveS2: OCP.StepGeom.StepGeom_PreferredSurfaceCurveRepresentation # value = StepGeom_PreferredSurfaceCurveRepresentation.StepGeom_pscrPcurveS2
StepGeom_tcContSameGradient: OCP.StepGeom.StepGeom_TransitionCode # value = StepGeom_TransitionCode.StepGeom_tcContSameGradient
StepGeom_tcContSameGradientSameCurvature: OCP.StepGeom.StepGeom_TransitionCode # value = StepGeom_TransitionCode.StepGeom_tcContSameGradientSameCurvature
StepGeom_tcContinuous: OCP.StepGeom.StepGeom_TransitionCode # value = StepGeom_TransitionCode.StepGeom_tcContinuous
StepGeom_tcDiscontinuous: OCP.StepGeom.StepGeom_TransitionCode # value = StepGeom_TransitionCode.StepGeom_tcDiscontinuous
StepGeom_tpCartesian: OCP.StepGeom.StepGeom_TrimmingPreference # value = StepGeom_TrimmingPreference.StepGeom_tpCartesian
StepGeom_tpParameter: OCP.StepGeom.StepGeom_TrimmingPreference # value = StepGeom_TrimmingPreference.StepGeom_tpParameter
StepGeom_tpUnspecified: OCP.StepGeom.StepGeom_TrimmingPreference # value = StepGeom_TrimmingPreference.StepGeom_tpUnspecified
