import OCP.IntCurveSurface
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.IntSurf
import OCP.GeomAbs
import OCP.math
import OCP.NCollection
import OCP.Bnd
import OCP.gp
import OCP.Geom
import OCP.TColStd
import OCP.Intf
__all__  = [
"IntCurveSurface_Intersection",
"IntCurveSurface_HInter",
"IntCurveSurface_IntersectionPoint",
"IntCurveSurface_IntersectionSegment",
"IntCurveSurface_SequenceOfPnt",
"IntCurveSurface_SequenceOfSeg",
"IntCurveSurface_TheCSFunctionOfHInter",
"IntCurveSurface_TheExactHInter",
"IntCurveSurface_TheHCurveTool",
"IntCurveSurface_TheInterferenceOfHInter",
"IntCurveSurface_ThePolygonOfHInter",
"IntCurveSurface_ThePolygonToolOfHInter",
"IntCurveSurface_ThePolyhedronOfHInter",
"IntCurveSurface_ThePolyhedronToolOfHInter",
"IntCurveSurface_TheQuadCurvExactHInter",
"IntCurveSurface_TheQuadCurvFuncOfTheQuadCurvExactHInter",
"IntCurveSurface_TransitionOnCurve",
"IntCurveSurface_In",
"IntCurveSurface_Out",
"IntCurveSurface_Tangent"
]
class IntCurveSurface_Intersection():
    """
    None
    """
    def Dump(self) -> None: 
        """
        Dump all the fields.
        """
    def IsDone(self) -> bool: 
        """
        returns the <done> field.
        """
    def IsParallel(self) -> bool: 
        """
        Returns true if curve is parallel or belongs surface This case is recognized only for some pairs of analytical curves and surfaces (plane - line, ...)
        """
    def NbPoints(self) -> int: 
        """
        returns the number of IntersectionPoint if IsDone returns True. else NotDone is raised.
        """
    def NbSegments(self) -> int: 
        """
        returns the number of IntersectionSegment if IsDone returns True. else NotDone is raised.
        """
    def Point(self,Index : int) -> IntCurveSurface_IntersectionPoint: 
        """
        returns the IntersectionPoint of range <Index> raises NotDone if the computation has failed or if the computation has not been done raises OutOfRange if Index is not in the range <1..NbPoints>
        """
    def Segment(self,Index : int) -> IntCurveSurface_IntersectionSegment: 
        """
        returns the IntersectionSegment of range <Index> raises NotDone if the computation has failed or if the computation has not been done raises OutOfRange if Index is not in the range <1..NbSegment>
        """
    pass
class IntCurveSurface_HInter(IntCurveSurface_Intersection):
    """
    None
    """
    def Dump(self) -> None: 
        """
        Dump all the fields.
        """
    def IsDone(self) -> bool: 
        """
        returns the <done> field.
        """
    def IsParallel(self) -> bool: 
        """
        Returns true if curve is parallel or belongs surface This case is recognized only for some pairs of analytical curves and surfaces (plane - line, ...)
        """
    def NbPoints(self) -> int: 
        """
        returns the number of IntersectionPoint if IsDone returns True. else NotDone is raised.
        """
    def NbSegments(self) -> int: 
        """
        returns the number of IntersectionSegment if IsDone returns True. else NotDone is raised.
        """
    @overload
    def Perform(self,Curve : OCP.Adaptor3d.Adaptor3d_Curve,Surface : OCP.Adaptor3d.Adaptor3d_Surface,Polyhedron : IntCurveSurface_ThePolyhedronOfHInter) -> None: 
        """
        Compute the Intersection between the curve and the surface

        Compute the Intersection between the curve and the surface. The Curve is already sampled and its polygon : <Polygon> is given.

        Compute the Intersection between the curve and the surface. The Curve is already sampled and its polygon : <Polygon> is given. The Surface is also sampled and <Polyhedron> is given.

        Compute the Intersection between the curve and the surface. The Curve is already sampled and its polygon : <Polygon> is given. The Surface is also sampled and <Polyhedron> is given.

        Compute the Intersection between the curve and the surface. The Surface is already sampled and its polyhedron : <Polyhedron> is given.
        """
    @overload
    def Perform(self,Curve : OCP.Adaptor3d.Adaptor3d_Curve,ThePolygon : IntCurveSurface_ThePolygonOfHInter,Surface : OCP.Adaptor3d.Adaptor3d_Surface,Polyhedron : IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
    @overload
    def Perform(self,Curve : OCP.Adaptor3d.Adaptor3d_Curve,ThePolygon : IntCurveSurface_ThePolygonOfHInter,Surface : OCP.Adaptor3d.Adaptor3d_Surface,Polyhedron : IntCurveSurface_ThePolyhedronOfHInter,BndBSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def Perform(self,Curve : OCP.Adaptor3d.Adaptor3d_Curve,Polygon : IntCurveSurface_ThePolygonOfHInter,Surface : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    @overload
    def Perform(self,Curve : OCP.Adaptor3d.Adaptor3d_Curve,Surface : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    def Point(self,Index : int) -> IntCurveSurface_IntersectionPoint: 
        """
        returns the IntersectionPoint of range <Index> raises NotDone if the computation has failed or if the computation has not been done raises OutOfRange if Index is not in the range <1..NbPoints>
        """
    def Segment(self,Index : int) -> IntCurveSurface_IntersectionSegment: 
        """
        returns the IntersectionSegment of range <Index> raises NotDone if the computation has failed or if the computation has not been done raises OutOfRange if Index is not in the range <1..NbSegment>
        """
    def __init__(self) -> None: ...
    pass
class IntCurveSurface_IntersectionPoint():
    """
    Definition of an interserction point between a curve and a surface.
    """
    def Dump(self) -> None: 
        """
        Dump all the fields.
        """
    def Pnt(self) -> OCP.gp.gp_Pnt: 
        """
        returns the geometric point.

        returns the geometric point.
        """
    def SetValues(self,P : OCP.gp.gp_Pnt,USurf : float,VSurf : float,UCurv : float,TrCurv : IntCurveSurface_TransitionOnCurve) -> None: 
        """
        Set the fields of the current IntersectionPoint.
        """
    def Transition(self) -> IntCurveSurface_TransitionOnCurve: 
        """
        returns the Transition of the point.

        returns the Transition of the point.
        """
    def U(self) -> float: 
        """
        returns the U parameter on the surface.

        returns the U parameter on the surface.
        """
    def V(self) -> float: 
        """
        returns the V parameter on the surface.

        returns the V parameter on the surface.
        """
    def Values(self,P : OCP.gp.gp_Pnt,TrCurv : IntCurveSurface_TransitionOnCurve) -> Tuple[float, float, float]: 
        """
        Get the fields of the current IntersectionPoint.
        """
    def W(self) -> float: 
        """
        returns the parameter on the curve.

        returns the parameter on the curve.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,USurf : float,VSurf : float,UCurv : float,TrCurv : IntCurveSurface_TransitionOnCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntCurveSurface_IntersectionSegment():
    """
    A IntersectionSegment describes a segment of curve (w1,w2) where distance(C(w),Surface) is less than a given tolerances.
    """
    def Dump(self) -> None: 
        """
        None
        """
    @overload
    def FirstPoint(self) -> IntCurveSurface_IntersectionPoint: 
        """
        None

        None
        """
    @overload
    def FirstPoint(self,P1 : IntCurveSurface_IntersectionPoint) -> None: ...
    @overload
    def SecondPoint(self) -> IntCurveSurface_IntersectionPoint: 
        """
        None

        None
        """
    @overload
    def SecondPoint(self,P2 : IntCurveSurface_IntersectionPoint) -> None: ...
    def SetValues(self,P1 : IntCurveSurface_IntersectionPoint,P2 : IntCurveSurface_IntersectionPoint) -> None: 
        """
        None
        """
    def Values(self,P1 : IntCurveSurface_IntersectionPoint,P2 : IntCurveSurface_IntersectionPoint) -> None: 
        """
        None
        """
    @overload
    def __init__(self,P1 : IntCurveSurface_IntersectionPoint,P2 : IntCurveSurface_IntersectionPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntCurveSurface_SequenceOfPnt(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntCurveSurface_IntersectionPoint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntCurveSurface_SequenceOfPnt) -> None: ...
    def Assign(self,theOther : IntCurveSurface_SequenceOfPnt) -> IntCurveSurface_SequenceOfPnt: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntCurveSurface_IntersectionPoint: 
        """
        First item access
        """
    def ChangeLast(self) -> IntCurveSurface_IntersectionPoint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntCurveSurface_IntersectionPoint: 
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
    def First(self) -> IntCurveSurface_IntersectionPoint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntCurveSurface_IntersectionPoint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntCurveSurface_SequenceOfPnt) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntCurveSurface_IntersectionPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntCurveSurface_SequenceOfPnt) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntCurveSurface_IntersectionPoint: 
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
    def Prepend(self,theItem : IntCurveSurface_IntersectionPoint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : IntCurveSurface_SequenceOfPnt) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntCurveSurface_IntersectionPoint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntCurveSurface_SequenceOfPnt) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntCurveSurface_IntersectionPoint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntCurveSurface_SequenceOfPnt) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntCurveSurface_SequenceOfSeg(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntCurveSurface_IntersectionSegment) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntCurveSurface_SequenceOfSeg) -> None: ...
    def Assign(self,theOther : IntCurveSurface_SequenceOfSeg) -> IntCurveSurface_SequenceOfSeg: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntCurveSurface_IntersectionSegment: 
        """
        First item access
        """
    def ChangeLast(self) -> IntCurveSurface_IntersectionSegment: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntCurveSurface_IntersectionSegment: 
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
    def First(self) -> IntCurveSurface_IntersectionSegment: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntCurveSurface_IntersectionSegment) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntCurveSurface_SequenceOfSeg) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntCurveSurface_SequenceOfSeg) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntCurveSurface_IntersectionSegment) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntCurveSurface_IntersectionSegment: 
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
    def Prepend(self,theSeq : IntCurveSurface_SequenceOfSeg) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntCurveSurface_IntersectionSegment) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntCurveSurface_IntersectionSegment) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntCurveSurface_SequenceOfSeg) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntCurveSurface_IntersectionSegment: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : IntCurveSurface_SequenceOfSeg) -> None: ...
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
class IntCurveSurface_TheCSFunctionOfHInter(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def AuxillarCurve(self) -> OCP.Adaptor3d.Adaptor3d_Curve: 
        """
        None
        """
    def AuxillarSurface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Root(self) -> float: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class IntCurveSurface_TheExactHInter():
    """
    None
    """
    def Function(self) -> IntCurveSurface_TheCSFunctionOfHInter: 
        """
        return the math function which is used to compute the intersection
        """
    def IsDone(self) -> bool: 
        """
        Returns TRUE if the creation completed without failure.
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def ParameterOnCurve(self) -> float: 
        """
        None
        """
    def ParameterOnSurface(self) -> Tuple[float, float]: 
        """
        None
        """
    def Perform(self,U : float,V : float,W : float,Rsnld : OCP.math.math_FunctionSetRoot,u0 : float,v0 : float,u1 : float,v1 : float,w0 : float,w1 : float) -> None: 
        """
        compute the solution it's possible to write to optimize: IntImp_IntCS inter(S1,C1,Toltangency) math_FunctionSetRoot rsnld(Inter.function()) while ...{ u=... v=... w=... inter.Perform(u,v,w,rsnld) } or IntImp_IntCS inter(Toltangency) inter.SetSurface(S); math_FunctionSetRoot rsnld(Inter.function()) while ...{ C=... inter.SetCurve(C); u=... v=... w=... inter.Perform(u,v,w,rsnld) }
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        returns the intersection point The exception NotDone is raised if IsDone is false. The exception DomainError is raised if IsEmpty is true.
        """
    @overload
    def __init__(self,F : IntCurveSurface_TheCSFunctionOfHInter,TolTangency : float) -> None: ...
    @overload
    def __init__(self,U : float,V : float,W : float,F : IntCurveSurface_TheCSFunctionOfHInter,TolTangency : float,MarginCoef : float=0.0) -> None: ...
    pass
class IntCurveSurface_TheHCurveTool():
    """
    None
    """
    @staticmethod
    def BSpline_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.Geom.Geom_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Circ: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U on the curve.
        """
    @staticmethod
    def D1_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    @staticmethod
    def D2_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    @staticmethod
    def D3_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    @staticmethod
    def DN_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    @staticmethod
    def Ellipse_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Elips: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Hyperbola_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    @staticmethod
    def Intervals_s(C : OCP.Adaptor3d.Adaptor3d_Curve,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def IsClosed_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPeriodic_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> bool: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Lin: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : OCP.Adaptor3d.Adaptor3d_Curve,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(myclass) >= <S>
        """
    @staticmethod
    def NbSamples_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U0 : float,U1 : float) -> int: 
        """
        None
        """
    @staticmethod
    def Parabola_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> OCP.gp.gp_Parab: 
        """
        None
        """
    @staticmethod
    def Period_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : OCP.Adaptor3d.Adaptor3d_Curve,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    @staticmethod
    def SamplePars_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U0 : float,U1 : float,Defl : float,NbMin : int,Pars : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self) -> None: ...
    pass
class IntCurveSurface_TheInterferenceOfHInter(OCP.Intf.Intf_Interference):
    """
    None
    """
    def Contains(self,ThePnt : OCP.Intf.Intf_SectionPoint) -> bool: 
        """
        Tests if the polylines of intersection or the zones of tangence contain the point of intersection <ThePnt>.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def GetTolerance(self) -> float: 
        """
        Gives the tolerance used for the calculation.

        Gives the tolerance used for the calculation.
        """
    @overload
    def Insert(self,pdeb : OCP.Intf.Intf_SectionPoint,pfin : OCP.Intf.Intf_SectionPoint) -> None: 
        """
        Inserts a new zone of tangence in the current list of tangent zones of the interference and returns True when done.

        Insert a new segment of intersection in the current list of polylines of intersection of the interference.
        """
    @overload
    def Insert(self,TheZone : OCP.Intf.Intf_TangentZone) -> bool: ...
    @overload
    def Interference(self,thePolyg : IntCurveSurface_ThePolygonOfHInter,thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> None: 
        """
        Compares the boundings between the segment of <thePolyg> and the facets of <thePolyh>.

        Compares the boundings between the segment of <thePolyg> and the facets of <thePolyh>.
        """
    @overload
    def Interference(self,thePolyg : IntCurveSurface_ThePolygonOfHInter,thePolyh : IntCurveSurface_ThePolyhedronOfHInter,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    def LineValue(self,Index : int) -> OCP.Intf.Intf_SectionLine: 
        """
        Gives the polyline of intersection at address <Index> in the interference.

        Gives the polyline of intersection at address <Index> in the interference.
        """
    def NbSectionLines(self) -> int: 
        """
        Gives the number of polylines of intersection in the interference.

        Gives the number of polylines of intersection in the interference.
        """
    def NbSectionPoints(self) -> int: 
        """
        Gives the number of points of intersection in the interference.

        Gives the number of points of intersection in the interference.
        """
    def NbTangentZones(self) -> int: 
        """
        Gives the number of zones of tangence in the interference.

        Gives the number of zones of tangence in the interference.
        """
    @overload
    def Perform(self,theLins : OCP.Intf.Intf_Array1OfLin,thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> None: 
        """
        Computes an interference between the Polygon and the Polyhedron.

        Computes an interference between the Straight Line and the Polyhedron.

        Computes an interference between the Straight Lines and the Polyhedron.

        Computes an interference between the Polygon and the Polyhedron.

        Computes an interference between the Straight Line and the Polyhedron.

        Computes an interference between the Straight Lines and the Polyhedron.
        """
    @overload
    def Perform(self,thePolyg : IntCurveSurface_ThePolygonOfHInter,thePolyh : IntCurveSurface_ThePolyhedronOfHInter,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def Perform(self,theLin : OCP.gp.gp_Lin,thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
    @overload
    def Perform(self,thePolyg : IntCurveSurface_ThePolygonOfHInter,thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
    @overload
    def Perform(self,theLins : OCP.Intf.Intf_Array1OfLin,thePolyh : IntCurveSurface_ThePolyhedronOfHInter,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def Perform(self,theLin : OCP.gp.gp_Lin,thePolyh : IntCurveSurface_ThePolyhedronOfHInter,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    def PntValue(self,Index : int) -> OCP.Intf.Intf_SectionPoint: 
        """
        Gives the point of intersection of address Index in the interference.

        Gives the point of intersection of address Index in the interference.
        """
    def ZoneValue(self,Index : int) -> OCP.Intf.Intf_TangentZone: 
        """
        Gives the zone of tangence at address Index in the interference.

        Gives the zone of tangence at address Index in the interference.
        """
    @overload
    def __init__(self,theLins : OCP.Intf.Intf_Array1OfLin,thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLin : OCP.gp.gp_Lin,thePolyh : IntCurveSurface_ThePolyhedronOfHInter,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def __init__(self,thePolyg : IntCurveSurface_ThePolygonOfHInter,thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
    @overload
    def __init__(self,theLins : OCP.Intf.Intf_Array1OfLin,thePolyh : IntCurveSurface_ThePolyhedronOfHInter,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def __init__(self,thePolyg : IntCurveSurface_ThePolygonOfHInter,thePolyh : IntCurveSurface_ThePolyhedronOfHInter,theBoundSB : OCP.Bnd.Bnd_BoundSortBox) -> None: ...
    @overload
    def __init__(self,theLin : OCP.gp.gp_Lin,thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
    pass
class IntCurveSurface_ThePolygonOfHInter():
    """
    None
    """
    def ApproxParamOnCurve(self,Index : int,ParamOnLine : float) -> float: 
        """
        Give an approximation of the parameter on the curve according to the discretization of the Curve.
        """
    def BeginOfSeg(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of range Index in the Polygon.
        """
    def Bounding(self) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the polygon.
        """
    @overload
    def Closed(self,flag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Closed(self) -> bool: ...
    def DeflectionOverEstimation(self) -> float: 
        """
        None
        """
    def Dump(self) -> None: 
        """
        None
        """
    def EndOfSeg(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of range Index in the Polygon.
        """
    def InfParameter(self) -> float: 
        """
        Returns the parameter (On the curve) of the first point of the Polygon
        """
    def NbSegments(self) -> int: 
        """
        Give the number of Segments in the polyline.
        """
    def SetDeflectionOverEstimation(self,x : float) -> None: 
        """
        None
        """
    def SupParameter(self) -> float: 
        """
        Returns the parameter (On the curve) of the last point of the Polygon
        """
    @overload
    def __init__(self,Curve : OCP.Adaptor3d.Adaptor3d_Curve,Upars : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,Curve : OCP.Adaptor3d.Adaptor3d_Curve,NbPnt : int) -> None: ...
    @overload
    def __init__(self,Curve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,NbPnt : int) -> None: ...
    pass
class IntCurveSurface_ThePolygonToolOfHInter():
    """
    None
    """
    @staticmethod
    def BeginOfSeg_s(thePolygon : IntCurveSurface_ThePolygonOfHInter,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of range Index in the Polygon.
        """
    @staticmethod
    def Bounding_s(thePolygon : IntCurveSurface_ThePolygonOfHInter) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the polygon.
        """
    @staticmethod
    def Closed_s(thePolygon : IntCurveSurface_ThePolygonOfHInter) -> bool: 
        """
        None
        """
    @staticmethod
    def DeflectionOverEstimation_s(thePolygon : IntCurveSurface_ThePolygonOfHInter) -> float: 
        """
        None
        """
    @staticmethod
    def Dump_s(thePolygon : IntCurveSurface_ThePolygonOfHInter) -> None: 
        """
        None
        """
    @staticmethod
    def EndOfSeg_s(thePolygon : IntCurveSurface_ThePolygonOfHInter,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of range Index in the Polygon.
        """
    @staticmethod
    def NbSegments_s(thePolygon : IntCurveSurface_ThePolygonOfHInter) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IntCurveSurface_ThePolyhedronOfHInter():
    """
    None
    """
    def Bounding(self) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the MaTriangle.
        """
    def ComponentsBounding(self) -> OCP.Bnd.Bnd_HArray1OfBox: 
        """
        Give the array of boxes. The box <n> corresponding to the triangle <n>.
        """
    def Contain(self,Triang : int,ThePnt : OCP.gp.gp_Pnt) -> bool: 
        """
        Give the plane equation of the triangle of address Triang.
        """
    def DeflectionOnTriangle(self,Surface : OCP.Adaptor3d.Adaptor3d_Surface,Index : int) -> float: 
        """
        None
        """
    @overload
    def DeflectionOverEstimation(self) -> float: 
        """
        None

        None
        """
    @overload
    def DeflectionOverEstimation(self,flec : float) -> None: ...
    def Destroy(self) -> None: 
        """
        None
        """
    def Dump(self) -> None: 
        """
        None
        """
    def FillBounding(self) -> None: 
        """
        Compute the array of boxes. The box <n> corresponding to the triangle <n>.
        """
    def GetBorderDeflection(self) -> float: 
        """
        This method returns a border deflection.
        """
    def IsOnBound(self,Index1 : int,Index2 : int) -> bool: 
        """
        This method returns true if the edge based on points with indices Index1 and Index2 represents a boundary edge. It is necessary to take into account the boundary deflection for this edge.
        """
    def NbPoints(self) -> int: 
        """
        Give the number of point in the double array of triangles ((nbdu+1)*(nbdv+1)).
        """
    def NbTriangles(self) -> int: 
        """
        Give the number of triangles in this double array of
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        None
        """
    def PlaneEquation(self,Triang : int,NormalVector : OCP.gp.gp_XYZ) -> Tuple[float]: 
        """
        Give the plane equation of the triangle of address Triang.
        """
    @overload
    def Point(self,thePnt : OCP.gp.gp_Pnt,lig : int,col : int,U : float,V : float) -> None: 
        """
        Set the value of a field of the double array of points.

        Give the point of index i in the MaTriangle.

        Give the point of index i in the MaTriangle.

        Give the point of index i in the MaTriangle.
        """
    @overload
    def Point(self,Index : int,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Point(self,Index : int,U : float,V : float) -> OCP.gp.gp_Pnt: ...
    @overload
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: ...
    def Size(self) -> Tuple[int, int]: 
        """
        get the size of the discretization.
        """
    def TriConnex(self,Triang : int,Pivot : int,Pedge : int,TriCon : int,OtherP : int) -> int: 
        """
        Give the address Tricon of the triangle connexe to the triangle of address Triang by the edge Pivot Pedge and the third point of this connexe triangle. When we are on a free edge TriCon==0 but the function return the value of the triangle in the other side of Pivot on the free edge. Used to turn around a vertex.
        """
    def Triangle(self,Index : int) -> Tuple[int, int, int]: 
        """
        Give the 3 points of the triangle of address Index in the double array of triangles.
        """
    @overload
    def __init__(self,Surface : OCP.Adaptor3d.Adaptor3d_Surface,Upars : OCP.TColStd.TColStd_Array1OfReal,Vpars : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,Surface : OCP.Adaptor3d.Adaptor3d_Surface,nbdU : int,nbdV : int,U1 : float,V1 : float,U2 : float,V2 : float) -> None: ...
    pass
class IntCurveSurface_ThePolyhedronToolOfHInter():
    """
    None
    """
    @staticmethod
    def Bounding_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the PolyhedronTool.
        """
    @staticmethod
    def ComponentsBounding_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> OCP.Bnd.Bnd_HArray1OfBox: 
        """
        Give the array of boxes. The box <n> corresponding to the triangle <n>.
        """
    @staticmethod
    def DeflectionOverEstimation_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> float: 
        """
        Give the tolerance of the polygon.
        """
    @staticmethod
    def Dump_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> None: 
        """
        None
        """
    @staticmethod
    def GetBorderDeflection_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> float: 
        """
        This method returns a border deflection of the polyhedron.
        """
    @staticmethod
    def IsOnBound_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter,Index1 : int,Index2 : int) -> bool: 
        """
        This method returns true if the edge based on points with indices Index1 and Index2 represents a boundary edge. It is necessary to take into account the boundary deflection for this edge.
        """
    @staticmethod
    def NbTriangles_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter) -> int: 
        """
        Give the number of triangles in this polyhedral surface.
        """
    @staticmethod
    def Point_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of index i in the polyhedral surface.
        """
    @staticmethod
    def TriConnex_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter,Triang : int,Pivot : int,Pedge : int,TriCon : int,OtherP : int) -> int: 
        """
        Give the address Tricon of the triangle connexe to the triangle of address Triang by the edge Pivot Pedge and the third point of this connexe triangle. When we are on a free edge TriCon==0 but the function return the value of the triangle in the other side of Pivot on the free edge. Used to turn around a vertex.
        """
    @staticmethod
    def Triangle_s(thePolyh : IntCurveSurface_ThePolyhedronOfHInter,Index : int) -> Tuple[int, int, int]: 
        """
        Give the indices of the 3 points of the triangle of address Index in the PolyhedronTool.
        """
    def __init__(self) -> None: ...
    pass
class IntCurveSurface_TheQuadCurvExactHInter():
    """
    None
    """
    def Intervals(self,Index : int) -> Tuple[float, float]: 
        """
        U1 and U2 are the parameters of a segment on the curve.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbIntervals(self) -> int: 
        """
        None
        """
    def NbRoots(self) -> int: 
        """
        None
        """
    def Root(self,Index : int) -> float: 
        """
        None
        """
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class IntCurveSurface_TheQuadCurvFuncOfTheQuadCurvExactHInter(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Derivative(self,Param : float,D : float) -> bool: 
        """
        Computes the derivative of the previous function at parameter Param. Derivative always returns True.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,Param : float,F : float) -> bool: 
        """
        Computes the value of the signed distance between the implicit surface and the point at parameter Param on the parametrised curve. Value always returns True.
        """
    def Values(self,Param : float,F : float,D : float) -> bool: 
        """
        Computes the value and the derivative of the function. returns True.
        """
    def __init__(self,Q : OCP.IntSurf.IntSurf_Quadric,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class IntCurveSurface_TransitionOnCurve():
    """
    \ Uo ^ \ U1 ^ \ | n \ | n Surf ====\======|=== ====\======|=== \ . \ . \ . \ . U1 \ . Uo \ .

    Members:

      IntCurveSurface_Tangent

      IntCurveSurface_In

      IntCurveSurface_Out
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
    IntCurveSurface_In: OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve # value = <IntCurveSurface_TransitionOnCurve.IntCurveSurface_In: 1>
    IntCurveSurface_Out: OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve # value = <IntCurveSurface_TransitionOnCurve.IntCurveSurface_Out: 2>
    IntCurveSurface_Tangent: OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve # value = <IntCurveSurface_TransitionOnCurve.IntCurveSurface_Tangent: 0>
    __entries: dict # value = {'IntCurveSurface_Tangent': (<IntCurveSurface_TransitionOnCurve.IntCurveSurface_Tangent: 0>, None), 'IntCurveSurface_In': (<IntCurveSurface_TransitionOnCurve.IntCurveSurface_In: 1>, None), 'IntCurveSurface_Out': (<IntCurveSurface_TransitionOnCurve.IntCurveSurface_Out: 2>, None)}
    __members__: dict # value = {'IntCurveSurface_Tangent': <IntCurveSurface_TransitionOnCurve.IntCurveSurface_Tangent: 0>, 'IntCurveSurface_In': <IntCurveSurface_TransitionOnCurve.IntCurveSurface_In: 1>, 'IntCurveSurface_Out': <IntCurveSurface_TransitionOnCurve.IntCurveSurface_Out: 2>}
    pass
IntCurveSurface_In: OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve # value = <IntCurveSurface_TransitionOnCurve.IntCurveSurface_In: 1>
IntCurveSurface_Out: OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve # value = <IntCurveSurface_TransitionOnCurve.IntCurveSurface_Out: 2>
IntCurveSurface_Tangent: OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve # value = <IntCurveSurface_TransitionOnCurve.IntCurveSurface_Tangent: 0>
