import OCP.Approx
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.Adaptor2d
import OCP.GeomAbs
import OCP.NCollection
import OCP.TColgp
import io
import OCP.Geom2d
import OCP.gp
import OCP.Standard
import OCP.Geom
import OCP.TColStd
import OCP.AppCont
import OCP.AppParCurves
__all__  = [
"Approx_Array1OfAdHSurface",
"Approx_Array1OfGTrsf2d",
"Approx_Curve2d",
"Approx_Curve3d",
"Approx_CurveOnSurface",
"Approx_CurvilinearParameter",
"Approx_CurvlinFunc",
"Approx_FitAndDivide",
"Approx_FitAndDivide2d",
"Approx_HArray1OfAdHSurface",
"Approx_HArray1OfGTrsf2d",
"Approx_MCurvesToBSpCurve",
"Approx_ParametrizationType",
"Approx_SameParameter",
"Approx_SequenceOfHArray1OfReal",
"Approx_Status",
"Approx_SweepApproximation",
"Approx_SweepFunction",
"Approx_Centripetal",
"Approx_ChordLength",
"Approx_IsoParametric",
"Approx_NoApproximation",
"Approx_NoPointsAdded",
"Approx_PointsAdded"
]
class Approx_Array1OfAdHSurface():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Approx_Array1OfAdHSurface) -> Approx_Array1OfAdHSurface: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Variable value access
        """
    def First(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.Adaptor3d.Adaptor3d_Surface) -> None: 
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
    def Last(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
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
    def Move(self,theOther : Approx_Array1OfAdHSurface) -> Approx_Array1OfAdHSurface: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Adaptor3d.Adaptor3d_Surface) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Approx_Array1OfAdHSurface) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.Adaptor3d.Adaptor3d_Surface,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Approx_Array1OfGTrsf2d():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Approx_Array1OfGTrsf2d) -> Approx_Array1OfGTrsf2d: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_GTrsf2d: 
        """
        Variable value access
        """
    def First(self) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.gp.gp_GTrsf2d) -> None: 
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
    def Last(self) -> OCP.gp.gp_GTrsf2d: 
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
    def Move(self,theOther : Approx_Array1OfGTrsf2d) -> Approx_Array1OfGTrsf2d: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_GTrsf2d) -> None: 
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
    def Value(self,theIndex : int) -> OCP.gp.gp_GTrsf2d: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.gp.gp_GTrsf2d,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Approx_Array1OfGTrsf2d) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Approx_Curve2d():
    """
    Makes an approximation for HCurve2d from Adaptor3d
    """
    def Curve(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    def HasResult(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def MaxError2dU(self) -> float: 
        """
        None
        """
    def MaxError2dV(self) -> float: 
        """
        None
        """
    def __init__(self,C2D : OCP.Adaptor2d.Adaptor2d_Curve2d,First : float,Last : float,TolU : float,TolV : float,Continuity : OCP.GeomAbs.GeomAbs_Shape,MaxDegree : int,MaxSegments : int) -> None: ...
    pass
class Approx_Curve3d():
    """
    None
    """
    def Curve(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Print on the stream o information about the object
        """
    def HasResult(self) -> bool: 
        """
        returns Standard_True if the approximation did come out with a result that is not NECESSARELY within the required tolerance
        """
    def IsDone(self) -> bool: 
        """
        returns Standard_True if the approximation has been done within required tolerance
        """
    def MaxError(self) -> float: 
        """
        returns the Maximum Error (>0 when an approximation has been done, 0 if no approximation)
        """
    def __init__(self,Curve : OCP.Adaptor3d.Adaptor3d_Curve,Tol3d : float,Order : OCP.GeomAbs.GeomAbs_Shape,MaxSegments : int,MaxDegree : int) -> None: ...
    pass
class Approx_CurveOnSurface():
    """
    Approximation of curve on surface
    """
    def Curve2d(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    def Curve3d(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def HasResult(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def MaxError2dU(self) -> float: 
        """
        None
        """
    def MaxError2dV(self) -> float: 
        """
        returns the maximum errors relatively to the U component or the V component of the 2d Curve
        """
    def MaxError3d(self) -> float: 
        """
        None
        """
    def Perform(self,theMaxSegments : int,theMaxDegree : int,theContinuity : OCP.GeomAbs.GeomAbs_Shape,theOnly3d : bool=False,theOnly2d : bool=False) -> None: 
        """
        Constructs the 3d curve. Input parameters are ignored when the input curve is U-isoline or V-isoline.
        """
    @overload
    def __init__(self,theC2D : OCP.Adaptor2d.Adaptor2d_Curve2d,theSurf : OCP.Adaptor3d.Adaptor3d_Surface,theFirst : float,theLast : float,theTol : float) -> None: ...
    @overload
    def __init__(self,C2D : OCP.Adaptor2d.Adaptor2d_Curve2d,Surf : OCP.Adaptor3d.Adaptor3d_Surface,First : float,Last : float,Tol : float,Continuity : OCP.GeomAbs.GeomAbs_Shape,MaxDegree : int,MaxSegments : int,Only3d : bool=False,Only2d : bool=False) -> None: ...
    pass
class Approx_CurvilinearParameter():
    """
    Approximation of a Curve to make its parameter be its curvilinear abscissa. If the curve is a curve on a surface S, C2D is the corresponding Pcurve, we consider the curve is given by its representation If the curve is a curve on 2 surfaces S1 and S2 and C2D1 C2D2 are the two corresponding Pcurve, we consider the curve is given by its representation
    """
    def Curve2d1(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        returns the BsplineCurve representing the reparametrized 2D curve on the first surface (case of a curve on one or two surfaces)
        """
    def Curve2d2(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        returns the BsplineCurve representing the reparametrized 2D curve on the second surface (case of a curve on two surfaces)
        """
    def Curve3d(self) -> OCP.Geom.Geom_BSplineCurve: 
        """
        returns the Bspline curve corresponding to the reparametrized 3D curve
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        print the maximum errors(s)
        """
    def HasResult(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def MaxError2d1(self) -> float: 
        """
        returns the maximum error on the first reparametrized 2D curve
        """
    def MaxError2d2(self) -> float: 
        """
        returns the maximum error on the second reparametrized 2D curve
        """
    def MaxError3d(self) -> float: 
        """
        returns the maximum error on the reparametrized 3D curve
        """
    @overload
    def __init__(self,C2D1 : OCP.Adaptor2d.Adaptor2d_Curve2d,Surf1 : OCP.Adaptor3d.Adaptor3d_Surface,C2D2 : OCP.Adaptor2d.Adaptor2d_Curve2d,Surf2 : OCP.Adaptor3d.Adaptor3d_Surface,Tol : float,Order : OCP.GeomAbs.GeomAbs_Shape,MaxDegree : int,MaxSegments : int) -> None: ...
    @overload
    def __init__(self,C3D : OCP.Adaptor3d.Adaptor3d_Curve,Tol : float,Order : OCP.GeomAbs.GeomAbs_Shape,MaxDegree : int,MaxSegments : int) -> None: ...
    @overload
    def __init__(self,C2D : OCP.Adaptor2d.Adaptor2d_Curve2d,Surf : OCP.Adaptor3d.Adaptor3d_Surface,Tol : float,Order : OCP.GeomAbs.GeomAbs_Shape,MaxDegree : int,MaxSegments : int) -> None: ...
    pass
class Approx_CurvlinFunc(OCP.Standard.Standard_Transient):
    """
    defines an abstract curve with curvilinear parametrizationdefines an abstract curve with curvilinear parametrization
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
    def EvalCase1(self,S : float,Order : int,Result : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        if myCase != 1
        """
    def EvalCase2(self,S : float,Order : int,Result : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        if myCase != 2
        """
    def EvalCase3(self,S : float,Order : int,Result : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        if myCase != 3
        """
    def FirstParameter(self) -> float: 
        """
        None
        """
    def GetLength(self) -> float: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSParameter(self,U : float) -> float: 
        """
        returns original parameter corresponding S.
        """
    def GetUParameter(self,C : OCP.Adaptor3d.Adaptor3d_Curve,S : float,NumberOfCurve : int) -> float: 
        """
        returns original parameter corresponding S. if Case == 1 computation is performed on myC2D1 and mySurf1, otherwise it is done on myC2D2 and mySurf2.
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
    def LastParameter(self) -> float: 
        """
        None
        """
    @overload
    def Length(self,C : OCP.Adaptor3d.Adaptor3d_Curve,FirstU : float,LasrU : float) -> float: 
        """
        Computes length of the curve.

        Computes length of the curve segment.
        """
    @overload
    def Length(self) -> None: ...
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetTol(self,Tol : float) -> None: 
        """
        ---Purpose Update the tolerance to used
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,First : float,Last : float,Tol : float) -> None: 
        """
        if First < 0 or Last > 1
        """
    @overload
    def __init__(self,C2D : OCP.Adaptor2d.Adaptor2d_Curve2d,S : OCP.Adaptor3d.Adaptor3d_Surface,Tol : float) -> None: ...
    @overload
    def __init__(self,C2D1 : OCP.Adaptor2d.Adaptor2d_Curve2d,C2D2 : OCP.Adaptor2d.Adaptor2d_Curve2d,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,Tol : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,Tol : float) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class Approx_FitAndDivide():
    """
    None
    """
    def Error(self,Index : int) -> Tuple[float, float]: 
        """
        returns the tolerances 2d and 3d of the <Index> MultiCurve.
        """
    def IsAllApproximated(self) -> bool: 
        """
        returns False if at a moment of the approximation, the status NoApproximation has been sent by the user when more points were needed.
        """
    def IsToleranceReached(self) -> bool: 
        """
        returns False if the status NoPointsAdded has been sent.
        """
    def NbMultiCurves(self) -> int: 
        """
        Returns the number of MultiCurve doing the approximation of the MultiLine.
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        None
        """
    def Perform(self,Line : OCP.AppCont.AppCont_Function) -> None: 
        """
        runs the algorithm after having initialized the fields.
        """
    def SetConstraints(self,FirstC : OCP.AppParCurves.AppParCurves_Constraint,LastC : OCP.AppParCurves.AppParCurves_Constraint) -> None: 
        """
        Changes the constraints of the approximation.
        """
    def SetDegrees(self,degreemin : int,degreemax : int) -> None: 
        """
        changes the degrees of the approximation.
        """
    def SetHangChecking(self,theHangChecking : bool) -> None: 
        """
        Set value of hang checking flag if this flag = true, possible hang of algorithm is checked and algorithm is forced to stop. By default hang checking is used.
        """
    def SetInvOrder(self,theInvOrder : bool) -> None: 
        """
        Set inverse order of degree selection: if theInvOrdr = true, current degree is chosen by inverse order - from maxdegree to mindegree. By default inverse order is used.
        """
    def SetMaxSegments(self,theMaxSegments : int) -> None: 
        """
        Changes the max number of segments, which is allowed for cutting.
        """
    def SetTolerances(self,Tolerance3d : float,Tolerance2d : float) -> None: 
        """
        Changes the tolerances of the approximation.
        """
    def Value(self,Index : int=1) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the approximation MultiCurve of range <Index>.
        """
    @overload
    def __init__(self,degreemin : int=3,degreemax : int=8,Tolerance3d : float=1e-05,Tolerance2d : float=1e-05,cutting : bool=False,FirstC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint,LastC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint) -> None: ...
    @overload
    def __init__(self,Line : OCP.AppCont.AppCont_Function,degreemin : int=3,degreemax : int=8,Tolerance3d : float=1e-05,Tolerance2d : float=1e-05,cutting : bool=False,FirstC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint,LastC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint) -> None: ...
    pass
class Approx_FitAndDivide2d():
    """
    None
    """
    def Error(self,Index : int) -> Tuple[float, float]: 
        """
        returns the tolerances 2d and 3d of the <Index> MultiCurve.
        """
    def IsAllApproximated(self) -> bool: 
        """
        returns False if at a moment of the approximation, the status NoApproximation has been sent by the user when more points were needed.
        """
    def IsToleranceReached(self) -> bool: 
        """
        returns False if the status NoPointsAdded has been sent.
        """
    def NbMultiCurves(self) -> int: 
        """
        Returns the number of MultiCurve doing the approximation of the MultiLine.
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        None
        """
    def Perform(self,Line : OCP.AppCont.AppCont_Function) -> None: 
        """
        runs the algorithm after having initialized the fields.
        """
    def SetConstraints(self,FirstC : OCP.AppParCurves.AppParCurves_Constraint,LastC : OCP.AppParCurves.AppParCurves_Constraint) -> None: 
        """
        Changes the constraints of the approximation.
        """
    def SetDegrees(self,degreemin : int,degreemax : int) -> None: 
        """
        changes the degrees of the approximation.
        """
    def SetHangChecking(self,theHangChecking : bool) -> None: 
        """
        Set value of hang checking flag if this flag = true, possible hang of algorithm is checked and algorithm is forced to stop. By default hang checking is used.
        """
    def SetInvOrder(self,theInvOrder : bool) -> None: 
        """
        Set inverse order of degree selection: if theInvOrdr = true, current degree is chosen by inverse order - from maxdegree to mindegree. By default inverse order is used.
        """
    def SetMaxSegments(self,theMaxSegments : int) -> None: 
        """
        Changes the max number of segments, which is allowed for cutting.
        """
    def SetTolerances(self,Tolerance3d : float,Tolerance2d : float) -> None: 
        """
        Changes the tolerances of the approximation.
        """
    def Value(self,Index : int=1) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the approximation MultiCurve of range <Index>.
        """
    @overload
    def __init__(self,degreemin : int=3,degreemax : int=8,Tolerance3d : float=1e-05,Tolerance2d : float=1e-05,cutting : bool=False,FirstC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint,LastC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint) -> None: ...
    @overload
    def __init__(self,Line : OCP.AppCont.AppCont_Function,degreemin : int=3,degreemax : int=8,Tolerance3d : float=1e-05,Tolerance2d : float=1e-05,cutting : bool=False,FirstC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint,LastC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint) -> None: ...
    pass
class Approx_HArray1OfAdHSurface(Approx_Array1OfAdHSurface, OCP.Standard.Standard_Transient):
    def Array1(self) -> Approx_Array1OfAdHSurface: 
        """
        None
        """
    def Assign(self,theOther : Approx_Array1OfAdHSurface) -> Approx_Array1OfAdHSurface: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Approx_Array1OfAdHSurface: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Adaptor3d.Adaptor3d_Surface: 
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
    def First(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
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
    def Init(self,theValue : OCP.Adaptor3d.Adaptor3d_Surface) -> None: 
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
    def Last(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
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
    def Move(self,theOther : Approx_Array1OfAdHSurface) -> Approx_Array1OfAdHSurface: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Adaptor3d.Adaptor3d_Surface) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Approx_Array1OfAdHSurface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
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
class Approx_HArray1OfGTrsf2d(Approx_Array1OfGTrsf2d, OCP.Standard.Standard_Transient):
    def Array1(self) -> Approx_Array1OfGTrsf2d: 
        """
        None
        """
    def Assign(self,theOther : Approx_Array1OfGTrsf2d) -> Approx_Array1OfGTrsf2d: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Approx_Array1OfGTrsf2d: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_GTrsf2d: 
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
    def First(self) -> OCP.gp.gp_GTrsf2d: 
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
    def Init(self,theValue : OCP.gp.gp_GTrsf2d) -> None: 
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
    def Last(self) -> OCP.gp.gp_GTrsf2d: 
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
    def Move(self,theOther : Approx_Array1OfGTrsf2d) -> Approx_Array1OfGTrsf2d: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_GTrsf2d) -> None: 
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
    def Value(self,theIndex : int) -> OCP.gp.gp_GTrsf2d: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Approx_Array1OfGTrsf2d) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.gp.gp_GTrsf2d) -> None: ...
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
class Approx_MCurvesToBSpCurve():
    """
    None
    """
    def Append(self,MC : OCP.AppParCurves.AppParCurves_MultiCurve) -> None: 
        """
        None
        """
    def ChangeValue(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        return the composite MultiCurves as a MultiBSpCurve.
        """
    @overload
    def Perform(self) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,TheSeq : OCP.AppParCurves.AppParCurves_SequenceOfMultiCurve) -> None: ...
    def Reset(self) -> None: 
        """
        None
        """
    def Value(self) -> OCP.AppParCurves.AppParCurves_MultiBSpCurve: 
        """
        return the composite MultiCurves as a MultiBSpCurve.
        """
    def __init__(self) -> None: ...
    pass
class Approx_ParametrizationType():
    """
    None

    Members:

      Approx_ChordLength

      Approx_Centripetal

      Approx_IsoParametric
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
    Approx_Centripetal: OCP.Approx.Approx_ParametrizationType # value = <Approx_ParametrizationType.Approx_Centripetal: 1>
    Approx_ChordLength: OCP.Approx.Approx_ParametrizationType # value = <Approx_ParametrizationType.Approx_ChordLength: 0>
    Approx_IsoParametric: OCP.Approx.Approx_ParametrizationType # value = <Approx_ParametrizationType.Approx_IsoParametric: 2>
    __entries: dict # value = {'Approx_ChordLength': (<Approx_ParametrizationType.Approx_ChordLength: 0>, None), 'Approx_Centripetal': (<Approx_ParametrizationType.Approx_Centripetal: 1>, None), 'Approx_IsoParametric': (<Approx_ParametrizationType.Approx_IsoParametric: 2>, None)}
    __members__: dict # value = {'Approx_ChordLength': <Approx_ParametrizationType.Approx_ChordLength: 0>, 'Approx_Centripetal': <Approx_ParametrizationType.Approx_Centripetal: 1>, 'Approx_IsoParametric': <Approx_ParametrizationType.Approx_IsoParametric: 2>}
    pass
class Approx_SameParameter():
    """
    Approximation of a PCurve on a surface to make its parameter be the same that the parameter of a given 3d reference curve.
    """
    def Curve2d(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns the 2D curve that has the same parameter as the 3D curve once evaluated on the surface up to the specified tolerance.
        """
    def IsDone(self) -> bool: 
        """
        Returns .false. if calculations failed, .true. if calculations succeed
        """
    def IsSameParameter(self) -> bool: 
        """
        Tells whether the original data had already the same parameter up to the tolerance : in that case nothing is done.
        """
    def TolReached(self) -> float: 
        """
        Returns tolerance (maximal distance) between 3d curve and curve on surface, generated by 2d curve and surface.
        """
    @overload
    def __init__(self,C3D : OCP.Adaptor3d.Adaptor3d_Curve,C2D : OCP.Geom2d.Geom2d_Curve,S : OCP.Adaptor3d.Adaptor3d_Surface,Tol : float) -> None: ...
    @overload
    def __init__(self,C3D : OCP.Geom.Geom_Curve,C2D : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,Tol : float) -> None: ...
    @overload
    def __init__(self,C3D : OCP.Adaptor3d.Adaptor3d_Curve,C2D : OCP.Adaptor2d.Adaptor2d_Curve2d,S : OCP.Adaptor3d.Adaptor3d_Surface,Tol : float) -> None: ...
    pass
class Approx_SequenceOfHArray1OfReal(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Approx_SequenceOfHArray1OfReal) -> None: ...
    def Assign(self,theOther : Approx_SequenceOfHArray1OfReal) -> Approx_SequenceOfHArray1OfReal: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
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
    def First(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Approx_SequenceOfHArray1OfReal) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TColStd.TColStd_HArray1OfReal) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Approx_SequenceOfHArray1OfReal) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TColStd.TColStd_HArray1OfReal) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
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
    def Prepend(self,theItem : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Approx_SequenceOfHArray1OfReal) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Approx_SequenceOfHArray1OfReal) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Approx_SequenceOfHArray1OfReal) -> None: ...
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
class Approx_Status():
    """
    It is an auxiliary flag being used in inner computations

    Members:

      Approx_PointsAdded

      Approx_NoPointsAdded

      Approx_NoApproximation
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
    Approx_NoApproximation: OCP.Approx.Approx_Status # value = <Approx_Status.Approx_NoApproximation: 2>
    Approx_NoPointsAdded: OCP.Approx.Approx_Status # value = <Approx_Status.Approx_NoPointsAdded: 1>
    Approx_PointsAdded: OCP.Approx.Approx_Status # value = <Approx_Status.Approx_PointsAdded: 0>
    __entries: dict # value = {'Approx_PointsAdded': (<Approx_Status.Approx_PointsAdded: 0>, None), 'Approx_NoPointsAdded': (<Approx_Status.Approx_NoPointsAdded: 1>, None), 'Approx_NoApproximation': (<Approx_Status.Approx_NoApproximation: 2>, None)}
    __members__: dict # value = {'Approx_PointsAdded': <Approx_Status.Approx_PointsAdded: 0>, 'Approx_NoPointsAdded': <Approx_Status.Approx_NoPointsAdded: 1>, 'Approx_NoApproximation': <Approx_Status.Approx_NoApproximation: 2>}
    pass
class Approx_SweepApproximation():
    """
    Approximation of an Surface S(u,v) (and eventually associate 2d Curves) defined by section's law.
    """
    def Average2dError(self,Index : int) -> float: 
        """
        returns the average error of the <Index> 2d curve approximation.
        """
    def AverageErrorOnSurf(self) -> float: 
        """
        returns the average error in the surface approximation.
        """
    def Curve2d(self,Index : int,TPoles : OCP.TColgp.TColgp_Array1OfPnt2d,TKnots : OCP.TColStd.TColStd_Array1OfReal,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def Curve2dPoles(self,Index : int) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        None

        None
        """
    def Curves2dDegree(self) -> int: 
        """
        None

        None
        """
    def Curves2dKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None

        None
        """
    def Curves2dMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None

        None
        """
    def Curves2dShape(self) -> Tuple[int, int, int]: 
        """
        None
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        display information on approximation.
        """
    def Eval(self,Parameter : float,DerivativeRequest : int,First : float,Last : float,Result : float) -> int: 
        """
        The EvaluatorFunction from AdvApprox;
        """
    def IsDone(self) -> bool: 
        """
        returns if we have an result

        returns if we have an result
        """
    def Max2dError(self,Index : int) -> float: 
        """
        returns the maximum error of the <Index> 2d curve approximation.
        """
    def MaxErrorOnSurf(self) -> float: 
        """
        returns the maximum error in the surface approximation.
        """
    def NbCurves2d(self) -> int: 
        """
        None

        None
        """
    def Perform(self,First : float,Last : float,Tol3d : float,BoundTol : float,Tol2d : float,TolAngular : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C0,Degmax : int=11,Segmax : int=50) -> None: 
        """
        Perform the Approximation [First, Last] : Approx_SweepApproximation.cdl Tol3d : Tolerance to surface approximation Tol2d : Tolerance used to perform curve approximation Normally the 2d curve are approximated with a tolerance given by the resolution on support surfaces, but if this tolerance is too large Tol2d is used. TolAngular : Tolerance (in radian) to control the angle between tangents on the section law and tangent of iso-v on approximated surface Continuity : The continuity in v waiting on the surface Degmax : The maximum degree in v required on the surface Segmax : The maximum number of span in v required on the surface Warning : The continuity ci can be obtained only if Ft is Ci
        """
    def SurfPoles(self) -> OCP.TColgp.TColgp_Array2OfPnt: 
        """
        None

        None
        """
    def SurfShape(self) -> Tuple[int, int, int, int, int, int]: 
        """
        None
        """
    def SurfUKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None

        None
        """
    def SurfUMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None

        None
        """
    def SurfVKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None

        None
        """
    def SurfVMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None

        None
        """
    def SurfWeights(self) -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        None

        None
        """
    def Surface(self,TPoles : OCP.TColgp.TColgp_Array2OfPnt,TWeights : OCP.TColStd.TColStd_Array2OfReal,TUKnots : OCP.TColStd.TColStd_Array1OfReal,TVKnots : OCP.TColStd.TColStd_Array1OfReal,TUMults : OCP.TColStd.TColStd_Array1OfInteger,TVMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def TolCurveOnSurf(self,Index : int) -> float: 
        """
        returns the maximum 3d error of the <Index> 2d curve approximation on the Surface.
        """
    def UDegree(self) -> int: 
        """
        None

        None
        """
    def VDegree(self) -> int: 
        """
        None

        None
        """
    def __init__(self,Func : Approx_SweepFunction) -> None: ...
    pass
class Approx_SweepFunction(OCP.Standard.Standard_Transient):
    """
    defined the function used by SweepApproximation to perform sweeping application.defined the function used by SweepApproximation to perform sweeping application.defined the function used by SweepApproximation to perform sweeping application.
    """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficient. This information is useful to perform well conditioned rational approximation. Warning: Used only if <me> IsRational
        """
    def D0(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param Warning : It used only for C1 or C2 approximation
        """
    def D2(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param Warning : It used only for C2 approximation
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
        Compute the minimal value of weight for each poles in all sections. This information is useful to control error in rational approximation. Warning: Used only if <me> IsRational
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerance to reach in approximation to satisfy. BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
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
    def IsRational(self) -> bool: 
        """
        Returns if the sections are rationnal or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the greater section. Thisinformation is useful to G1's control. Warning: With an little value, approximation can be slower.
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
        Is useful, if (me) have to run numerical algorithm to perform D0, D1 or D2
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
Approx_Centripetal: OCP.Approx.Approx_ParametrizationType # value = <Approx_ParametrizationType.Approx_Centripetal: 1>
Approx_ChordLength: OCP.Approx.Approx_ParametrizationType # value = <Approx_ParametrizationType.Approx_ChordLength: 0>
Approx_IsoParametric: OCP.Approx.Approx_ParametrizationType # value = <Approx_ParametrizationType.Approx_IsoParametric: 2>
Approx_NoApproximation: OCP.Approx.Approx_Status # value = <Approx_Status.Approx_NoApproximation: 2>
Approx_NoPointsAdded: OCP.Approx.Approx_Status # value = <Approx_Status.Approx_NoPointsAdded: 1>
Approx_PointsAdded: OCP.Approx.Approx_Status # value = <Approx_Status.Approx_PointsAdded: 0>
