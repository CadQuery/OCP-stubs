import OCP.Bisector
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.math
import OCP.gp
import OCP.Geom2d
import OCP.IntRes2d
import OCP.GeomAbs
import OCP.Standard
import io
__all__  = [
"Bisector",
"Bisector_Bisec",
"Bisector_Curve",
"Bisector_BisecCC",
"Bisector_BisecPC",
"Bisector_BisecAna",
"Bisector_FunctionH",
"Bisector_FunctionInter",
"Bisector_Inter",
"Bisector_PointOnBis",
"Bisector_PolyBis"
]
class Bisector():
    """
    This package provides the bisecting line between two geometric elements.
    """
    @staticmethod
    def IsConvex_s(Cu : OCP.Geom2d.Geom2d_Curve,Sign : float) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Bisector_Bisec():
    """
    Bisec provides the bisecting line between two elements This line is trimmed by a point <P> and it's contained in the domain defined by the two vectors <V1>, <V2> and <Sense>.
    """
    def ChangeValue(self) -> OCP.Geom2d.Geom2d_TrimmedCurve: 
        """
        Returns the Curve of <me>.
        """
    @overload
    def Perform(self,Pnt1 : OCP.Geom2d.Geom2d_Point,Pnt2 : OCP.Geom2d.Geom2d_Point,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,Sense : float,Tolerance : float=0.0,oncurve : bool=True) -> None: 
        """
        Performs the bisecting line between the curves <Cu1> and <Cu2>. <oncurve> is True if the point <P> is common to <Cu1> and <Cu2>.

        Performs the bisecting line between the curve <Cu1> and the point <Pnt>. <oncurve> is True if the point <P> is the point <Pnt>.

        Performs the bisecting line between the curve <Cu> and the point <Pnt>. <oncurve> is True if the point <P> is the point <Pnt>.

        Performs the bisecting line between the two points <Pnt1> and <Pnt2>.
        """
    @overload
    def Perform(self,Pnt : OCP.Geom2d.Geom2d_Point,Cu : OCP.Geom2d.Geom2d_Curve,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,Sense : float,Tolerance : float,oncurve : bool=True) -> None: ...
    @overload
    def Perform(self,Cu1 : OCP.Geom2d.Geom2d_Curve,Cu2 : OCP.Geom2d.Geom2d_Curve,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,Sense : float,ajointype : OCP.GeomAbs.GeomAbs_JoinType,Tolerance : float,oncurve : bool=True) -> None: ...
    @overload
    def Perform(self,Cu : OCP.Geom2d.Geom2d_Curve,Pnt : OCP.Geom2d.Geom2d_Point,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,Sense : float,Tolerance : float,oncurve : bool=True) -> None: ...
    def Value(self) -> OCP.Geom2d.Geom2d_TrimmedCurve: 
        """
        Returns the Curve of <me>.
        """
    def __init__(self) -> None: ...
    pass
class Bisector_Curve(OCP.Geom2d.Geom2d_Curve, OCP.Geom2d.Geom2d_Geometry, OCP.Standard.Standard_Transient):
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        It is the global continuity of the curve : C0 : only geometric continuity, C1 : continuity of the first derivative all along the Curve, C2 : continuity of the second derivative all along the Curve, C3 : continuity of the third derivative all along the Curve, G1 : tangency continuity all along the Curve, G2 : curvature continuity all along the Curve, CN : the order of continuity is infinite.
        """
    def Copy(self) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns in P the point of parameter U. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U and the first derivative V1. Raised if the continuity of the curve is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the curve is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the curve is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        For the point of parameter U of this curve, computes the vector corresponding to the Nth derivative. Exceptions StdFail_UndefinedDerivative if: - the continuity of the curve is not "CN", or - the derivative vector cannot be computed easily; this is the case with specific types of curve (for example, a rational BSpline curve where N is greater than 3). Standard_RangeError if N is less than 1.
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
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter. Warnings : It can be RealFirst or RealLast from package Standard if the curve is infinite
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IntervalFirst(self,Index : int) -> float: 
        """
        Returns the first parameter of the current interval.
        """
    def IntervalLast(self,Index : int) -> float: 
        """
        Returns the last parameter of the current interval.
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns true if the degree of continuity of this curve is at least N. Exceptions Standard_RangeError if N is less than 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns true if the curve is closed. Examples : Some curves such as circle are always closed, others such as line are never closed (by definition). Some Curves such as OffsetCurve can be closed or not. These curves are considered as closed if the distance between the first point and the last point of the curve is lower or equal to the Resolution from package gp which is a fixed criterion independent of the application.
        """
    def IsExtendAtEnd(self) -> bool: 
        """
        None
        """
    def IsExtendAtStart(self) -> bool: 
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
    def IsPeriodic(self) -> bool: 
        """
        Returns true if the parameter of the curve is periodic. It is possible only if the curve is closed and if the following relation is satisfied : for each parametric value U the distance between the point P(u) and the point P (u + T) is lower or equal to Resolution from package gp, T is the period and must be a constant. There are three possibilities : . the curve is never periodic by definition (SegmentLine) . the curve is always periodic by definition (Circle) . the curve can be defined as periodic (BSpline). In this case a function SetPeriodic allows you to give the shape of the curve. The general rule for this case is : if a curve can be periodic or not the default periodicity set is non periodic and you have to turn (explicitly) the curve into a periodic curve if you want the curve to be periodic.
        """
    def LastParameter(self) -> float: 
        """
        Value of the last parameter. Warnings : It can be RealFirst or RealLast from package Standard if the curve is infinite
        """
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry and assigns the result to this geometric object.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirror(self,A : OCP.gp.gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,A : OCP.gp.gp_Ax2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt2d) -> OCP.Geom2d.Geom2d_Geometry: ...
    def NbIntervals(self) -> int: 
        """
        If necessary, breaks the curve in intervals of continuity <C1>. And returns the number of intervals.
        """
    def Parameter(self,P : OCP.gp.gp_Pnt2d) -> float: 
        """
        None
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf2d) -> float: 
        """
        Returns the coefficient required to compute the parametric transformation of this curve when transformation T is applied. This coefficient is the ratio between the parameter of a point on this curve and the parameter of the transformed point on the new curve transformed by T. Note: this function generally returns 1. but it can be redefined (for example, on a line).
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. raises if the curve is not periodic
        """
    def Reverse(self) -> None: 
        """
        Changes the direction of parametrization of <me>. The "FirstParameter" and the "LastParameter" are not changed but the orientation of the curve is modified. If the curve is bounded the StartPoint of the initial curve becomes the EndPoint of the reversed curve and the EndPoint of the initial curve becomes the StartPoint of the reversed curve.
        """
    def Reversed(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Creates a reversed duplicate Changes the orientation of this curve. The first and last parameters are not changed, but the parametric direction of the curve is reversed. If the curve is bounded: - the start point of the initial curve becomes the end point of the reversed curve, and - the end point of the initial curve becomes the start point of the reversed curve. - Reversed creates a new curve.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Computes the parameter on the reversed curve for the point of parameter U on this curve. Note: The point of parameter U on this curve is identical to the point of parameter ReversedParameter(U) on the reversed curve.
        """
    def Rotate(self,P : OCP.gp.gp_Pnt2d,Ang : float) -> None: 
        """
        Rotates a Geometry. P is the center of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,P : OCP.gp.gp_Pnt2d,Ang : float) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt2d,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt2d,S : float) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf2d) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom2d). The following transformations have the same properties as the previous ones but they don't modified the object itself. A copy of the object is returned.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf2d) -> float: 
        """
        Computes the parameter on the curve transformed by T for the point of parameter U on this curve. Note: this function generally returns U but it can be redefined (for example, on a line).
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Translates a Geometry. V is the vector of the translation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,V : OCP.gp.gp_Vec2d) -> OCP.Geom2d.Geom2d_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve.
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
class Bisector_BisecCC(Bisector_Curve, OCP.Geom2d.Geom2d_Curve, OCP.Geom2d.Geom2d_Geometry, OCP.Standard.Standard_Transient):
    """
    Construct the bisector between two curves. The curves can intersect only in their extremities.Construct the bisector between two curves. The curves can intersect only in their extremities.Construct the bisector between two curves. The curves can intersect only in their extremities.
    """
    def ChangeGuide(self) -> Bisector_BisecCC: 
        """
        The parameter on <me> is linked to the parameter on the first curve. This method creates the same bisector where the curves are inversed.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def Copy(self) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def Curve(self,IndCurve : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec2d: 
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
    def Dump(self,Deep : int=0,Offset : int=0) -> None: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstParameter(self) -> float: 
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
    def IntervalContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def IntervalFirst(self,Index : int) -> float: 
        """
        Returns the first parameter of the current interval.
        """
    def IntervalLast(self,Index : int) -> float: 
        """
        Returns the last parameter of the current interval.
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns the order of continuity of the curve. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def IsExtendAtEnd(self) -> bool: 
        """
        None
        """
    def IsExtendAtStart(self) -> bool: 
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
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        None
        """
    def LinkBisCurve(self,U : float) -> float: 
        """
        Returns the parameter on the curve1 of the projection of the point of parameter U on <me>.
        """
    def LinkCurveBis(self,U : float) -> float: 
        """
        Returns the reciproque of LinkBisCurve.
        """
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry and assigns the result to this geometric object.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirror(self,A : OCP.gp.gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,A : OCP.gp.gp_Ax2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt2d) -> OCP.Geom2d.Geom2d_Geometry: ...
    def NbIntervals(self) -> int: 
        """
        If necessary, breaks the curve in intervals of continuity <C1>. And returns the number of intervals.
        """
    def Parameter(self,P : OCP.gp.gp_Pnt2d) -> float: 
        """
        None
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf2d) -> float: 
        """
        Returns the coefficient required to compute the parametric transformation of this curve when transformation T is applied. This coefficient is the ratio between the parameter of a point on this curve and the parameter of the transformed point on the new curve transformed by T. Note: this function generally returns 1. but it can be redefined (for example, on a line).
        """
    def Perform(self,Cu1 : OCP.Geom2d.Geom2d_Curve,Cu2 : OCP.Geom2d.Geom2d_Curve,Side1 : float,Side2 : float,Origin : OCP.gp.gp_Pnt2d,DistMax : float=500.0) -> None: 
        """
        Computes the bisector between the curves <Cu1> and <Cu2>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. raises if the curve is not periodic
        """
    def Polygon(self) -> Bisector_PolyBis: 
        """
        None
        """
    def Reverse(self) -> None: 
        """
        None
        """
    def Reversed(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Creates a reversed duplicate Changes the orientation of this curve. The first and last parameters are not changed, but the parametric direction of the curve is reversed. If the curve is bounded: - the start point of the initial curve becomes the end point of the reversed curve, and - the end point of the initial curve becomes the start point of the reversed curve. - Reversed creates a new curve.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        None
        """
    def Rotate(self,P : OCP.gp.gp_Pnt2d,Ang : float) -> None: 
        """
        Rotates a Geometry. P is the center of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,P : OCP.gp.gp_Pnt2d,Ang : float) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt2d,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt2d,S : float) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf2d) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf2d) -> float: 
        """
        Computes the parameter on the curve transformed by T for the point of parameter U on this curve. Note: this function generally returns U but it can be redefined (for example, on a line).
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Translates a Geometry. V is the vector of the translation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,V : OCP.gp.gp_Vec2d) -> OCP.Geom2d.Geom2d_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve.
        """
    def ValueAndDist(self,U : float,U1 : float,U2 : float,Distance : float) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the point of parameter U. Computes the distance between the current point and the two curves I separate. Computes the parameters on each curve corresponding of the projection of the current point.
        """
    def ValueByInt(self,U : float,U1 : float,U2 : float,Distance : float) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the point of parameter U. Computes the distance between the current point and the two curves I separate. Computes the parameters on each curve corresponding of the projection of the current point.
        """
    @overload
    def __init__(self,Cu1 : OCP.Geom2d.Geom2d_Curve,Cu2 : OCP.Geom2d.Geom2d_Curve,Side1 : float,Side2 : float,Origin : OCP.gp.gp_Pnt2d,DistMax : float=500.0) -> None: ...
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
class Bisector_BisecPC(Bisector_Curve, OCP.Geom2d.Geom2d_Curve, OCP.Geom2d.Geom2d_Geometry, OCP.Standard.Standard_Transient):
    """
    Provides the bisector between a point and a curve. the curvature on the curve has to be monoton. the point can't be on the curve exept at the extremities.Provides the bisector between a point and a curve. the curvature on the curve has to be monoton. the point can't be on the curve exept at the extremities.Provides the bisector between a point and a curve. the curvature on the curve has to be monoton. the point can't be on the curve exept at the extremities.
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def Copy(self) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec2d: 
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
    def Distance(self,U : float) -> float: 
        """
        Returns the distance between the point of parameter U on <me> and my point or my curve.
        """
    def Dump(self,Deep : int=0,Offset : int=0) -> None: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        Value of the first parameter.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IntervalContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def IntervalFirst(self,Index : int) -> float: 
        """
        Returns the first parameter of the current interval.
        """
    def IntervalLast(self,Index : int) -> float: 
        """
        Returns the last parameter of the current interval.
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns the order of continuity of the curve. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        Returns <True> if the bisector is empty.
        """
    def IsExtendAtEnd(self) -> bool: 
        """
        Returns True if the bisector is extended at end.
        """
    def IsExtendAtStart(self) -> bool: 
        """
        Returns True if the bisector is extended at start.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        Value of the last parameter.
        """
    def LinkBisCurve(self,U : float) -> float: 
        """
        Returns the parameter on the curve1 of the projection of the point of parameter U on <me>.
        """
    def LinkCurveBis(self,U : float) -> float: 
        """
        Returns the reciproque of LinkBisCurve.
        """
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry and assigns the result to this geometric object.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirror(self,A : OCP.gp.gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,A : OCP.gp.gp_Ax2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt2d) -> OCP.Geom2d.Geom2d_Geometry: ...
    def NbIntervals(self) -> int: 
        """
        If necessary, breaks the curve in intervals of continuity <C1>. And returns the number of intervals.
        """
    def Parameter(self,P : OCP.gp.gp_Pnt2d) -> float: 
        """
        Returns the parameter on <me> corresponding to <P>.
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf2d) -> float: 
        """
        Returns the coefficient required to compute the parametric transformation of this curve when transformation T is applied. This coefficient is the ratio between the parameter of a point on this curve and the parameter of the transformed point on the new curve transformed by T. Note: this function generally returns 1. but it can be redefined (for example, on a line).
        """
    def Perform(self,Cu : OCP.Geom2d.Geom2d_Curve,P : OCP.gp.gp_Pnt2d,Side : float,DistMax : float=500.0) -> None: 
        """
        Construct the bisector between the point <P> and the curve <Cu>. <Side> = 1. if the bisector curve is on the Left of <Cu> else <Side> = -1. <DistMax> is used to trim the bisector.The distance between the points of the bisector and <Cu> is smaller than <DistMax>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. raises if the curve is not periodic
        """
    def Reverse(self) -> None: 
        """
        Changes the direction of parametrization of <me>. The orientation of the curve is modified. If the curve is bounded the StartPoint of the initial curve becomes the EndPoint of the reversed curve and the EndPoint of the initial curve becomes the StartPoint of the reversed curve.
        """
    def Reversed(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Creates a reversed duplicate Changes the orientation of this curve. The first and last parameters are not changed, but the parametric direction of the curve is reversed. If the curve is bounded: - the start point of the initial curve becomes the end point of the reversed curve, and - the end point of the initial curve becomes the start point of the reversed curve. - Reversed creates a new curve.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the reversed curve for the point of parameter U on <me>.
        """
    def Rotate(self,P : OCP.gp.gp_Pnt2d,Ang : float) -> None: 
        """
        Rotates a Geometry. P is the center of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,P : OCP.gp.gp_Pnt2d,Ang : float) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt2d,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt2d,S : float) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf2d) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf2d) -> float: 
        """
        Computes the parameter on the curve transformed by T for the point of parameter U on this curve. Note: this function generally returns U but it can be redefined (for example, on a line).
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Translates a Geometry. V is the vector of the translation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,V : OCP.gp.gp_Vec2d) -> OCP.Geom2d.Geom2d_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Cu : OCP.Geom2d.Geom2d_Curve,P : OCP.gp.gp_Pnt2d,Side : float,UMin : float,UMax : float) -> None: ...
    @overload
    def __init__(self,Cu : OCP.Geom2d.Geom2d_Curve,P : OCP.gp.gp_Pnt2d,Side : float,DistMax : float=500.0) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class Bisector_BisecAna(Bisector_Curve, OCP.Geom2d.Geom2d_Curve, OCP.Geom2d.Geom2d_Geometry, OCP.Standard.Standard_Transient):
    """
    This class provides the bisecting line between two geometric elements.The elements are Circles,Lines or Points.This class provides the bisecting line between two geometric elements.The elements are Circles,Lines or Points.This class provides the bisecting line between two geometric elements.The elements are Circles,Lines or Points.
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def Copy(self) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec2d: 
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
    def Dump(self,Deep : int=0,Offset : int=0) -> None: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        None
        """
    def Geom2dCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
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
    def Init(self,bisector : OCP.Geom2d.Geom2d_TrimmedCurve) -> None: 
        """
        None
        """
    def IntervalFirst(self,Index : int) -> float: 
        """
        Returns the first parameter of the current interval.
        """
    def IntervalLast(self,Index : int) -> float: 
        """
        Returns the last parameter of the current interval.
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns the order of continuity of the curve. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsExtendAtEnd(self) -> bool: 
        """
        None
        """
    def IsExtendAtStart(self) -> bool: 
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
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        None
        """
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry and assigns the result to this geometric object.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirror(self,A : OCP.gp.gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,A : OCP.gp.gp_Ax2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt2d) -> OCP.Geom2d.Geom2d_Geometry: ...
    def NbIntervals(self) -> int: 
        """
        If necessary, breaks the curve in intervals of continuity <C1>. And returns the number of intervals.
        """
    def Parameter(self,P : OCP.gp.gp_Pnt2d) -> float: 
        """
        None
        """
    def ParameterOfEndPoint(self) -> float: 
        """
        None
        """
    def ParameterOfStartPoint(self) -> float: 
        """
        None
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf2d) -> float: 
        """
        Returns the coefficient required to compute the parametric transformation of this curve when transformation T is applied. This coefficient is the ratio between the parameter of a point on this curve and the parameter of the transformed point on the new curve transformed by T. Note: this function generally returns 1. but it can be redefined (for example, on a line).
        """
    @overload
    def Perform(self,Cu1 : OCP.Geom2d.Geom2d_Curve,Cu2 : OCP.Geom2d.Geom2d_Curve,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,Sense : float,jointype : OCP.GeomAbs.GeomAbs_JoinType,Tolerance : float,oncurve : bool=True) -> None: 
        """
        Performs the bisecting line between the curves <Cu1> and <Cu2>. <oncurve> is True if the point <P> is common to <Cu1> and <Cu2>.

        Performs the bisecting line between the curve <Cu1> and the point <Pnt>. <oncurve> is True if the point <P> is the point <Pnt>.

        Performs the bisecting line between the curve <Cu> and the point <Pnt>. <oncurve> is True if the point <P> is the point <Pnt>.

        Performs the bisecting line between the two points <Pnt1> and <Pnt2>.
        """
    @overload
    def Perform(self,Pnt : OCP.Geom2d.Geom2d_Point,Cu : OCP.Geom2d.Geom2d_Curve,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,Sense : float,Tolerance : float,oncurve : bool=True) -> None: ...
    @overload
    def Perform(self,Cu : OCP.Geom2d.Geom2d_Curve,Pnt : OCP.Geom2d.Geom2d_Point,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,Sense : float,Tolerance : float,oncurve : bool=True) -> None: ...
    @overload
    def Perform(self,Pnt1 : OCP.Geom2d.Geom2d_Point,Pnt2 : OCP.Geom2d.Geom2d_Point,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,Sense : float,Tolerance : float=0.0,oncurve : bool=True) -> None: ...
    def Period(self) -> float: 
        """
        Returns the period of this curve. raises if the curve is not periodic
        """
    def Reverse(self) -> None: 
        """
        None
        """
    def Reversed(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Creates a reversed duplicate Changes the orientation of this curve. The first and last parameters are not changed, but the parametric direction of the curve is reversed. If the curve is bounded: - the start point of the initial curve becomes the end point of the reversed curve, and - the end point of the initial curve becomes the start point of the reversed curve. - Reversed creates a new curve.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        None
        """
    def Rotate(self,P : OCP.gp.gp_Pnt2d,Ang : float) -> None: 
        """
        Rotates a Geometry. P is the center of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,P : OCP.gp.gp_Pnt2d,Ang : float) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt2d,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt2d,S : float) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    @overload
    def SetTrim(self,uf : float,ul : float) -> None: 
        """
        Trim <me> by a domain defined by the curve <Cu>. This domain is the set of the points which are nearest from <Cu> than the extremitis of <Cu>.

        Trim <me> by a domain defined by uf and ul
        """
    @overload
    def SetTrim(self,Cu : OCP.Geom2d.Geom2d_Curve) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf2d) -> None: 
        """
        None
        """
    def Transformed(self,T : OCP.gp.gp_Trsf2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf2d) -> float: 
        """
        Computes the parameter on the curve transformed by T for the point of parameter U on this curve. Note: this function generally returns U but it can be redefined (for example, on a line).
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Translates a Geometry. V is the vector of the translation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,V : OCP.gp.gp_Vec2d) -> OCP.Geom2d.Geom2d_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class Bisector_FunctionH(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    H(v) = (T1 .P2(v) - P1) * ||T(v)|| - 2 2 (T(v).P2(v) - P1) * ||T1||
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Computes the values of the Functions for the variable <X>.
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        Returns the values of the functions and the derivatives for the variable <X>.
        """
    def __init__(self,C2 : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,T1 : OCP.gp.gp_Vec2d) -> None: ...
    pass
class Bisector_FunctionInter(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    2 2 F(u) = (PC(u) - PBis1(u)) + (PC(u) - PBis2(u))
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Perform(self,C : OCP.Geom2d.Geom2d_Curve,Bis1 : Bisector_Curve,Bis2 : Bisector_Curve) -> None: 
        """
        None
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Computes the values of the Functions for the variable <X>.
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        Returns the values of the functions and the derivatives for the variable <X>.
        """
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Curve,Bis1 : Bisector_Curve,Bis2 : Bisector_Curve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Bisector_Inter(OCP.IntRes2d.IntRes2d_Intersection):
    """
    Intersection between two <Bisec> from Bisector.
    """
    def IsDone(self) -> bool: 
        """
        returns TRUE when the computation was successful.

        returns TRUE when the computation was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.

        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbPoints(self) -> int: 
        """
        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbSegments(self) -> int: 
        """
        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def Perform(self,C1 : Bisector_Bisec,D1 : OCP.IntRes2d.IntRes2d_Domain,C2 : Bisector_Bisec,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float,ComunElement : bool) -> None: 
        """
        Intersection between 2 curves. C1 separates the element A and B. C2 separates the elements C et D. If B an C have the same geometry. <ComunElement> Has to be True. It Permits an optimiztion of the computation.
        """
    def Point(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionPoint: 
        """
        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def Segment(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionSegment: 
        """
        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    @overload
    def SetReversedParameters(self,Reverseflag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetReversedParameters(self,flag : bool) -> None: ...
    @overload
    def __init__(self,C1 : Bisector_Bisec,D1 : OCP.IntRes2d.IntRes2d_Domain,C2 : Bisector_Bisec,D2 : OCP.IntRes2d.IntRes2d_Domain,TolConf : float,Tol : float,ComunElement : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Bisector_PointOnBis():
    """
    None
    """
    @overload
    def Distance(self,Distance : float) -> None: 
        """
        None

        None
        """
    @overload
    def Distance(self) -> float: ...
    def Dump(self) -> None: 
        """
        None
        """
    @overload
    def IsInfinite(self) -> bool: 
        """
        None

        None
        """
    @overload
    def IsInfinite(self,Infinite : bool) -> None: ...
    @overload
    def ParamOnBis(self) -> float: 
        """
        None

        None
        """
    @overload
    def ParamOnBis(self,Param : float) -> None: ...
    @overload
    def ParamOnC1(self) -> float: 
        """
        None

        None
        """
    @overload
    def ParamOnC1(self,Param : float) -> None: ...
    @overload
    def ParamOnC2(self) -> float: 
        """
        None

        None
        """
    @overload
    def ParamOnC2(self,Param : float) -> None: ...
    @overload
    def Point(self) -> OCP.gp.gp_Pnt2d: 
        """
        None

        None
        """
    @overload
    def Point(self,P : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Param1 : float,Param2 : float,ParamBis : float,Distance : float,Point : OCP.gp.gp_Pnt2d) -> None: ...
    pass
class Bisector_PolyBis():
    """
    Polygon of PointOnBis
    """
    def Append(self,Point : Bisector_PointOnBis) -> None: 
        """
        None
        """
    def First(self) -> Bisector_PointOnBis: 
        """
        None
        """
    def Interval(self,U : float) -> int: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> Bisector_PointOnBis: 
        """
        None
        """
    def Length(self) -> int: 
        """
        None
        """
    def Transform(self,T : OCP.gp.gp_Trsf2d) -> None: 
        """
        None
        """
    def Value(self,Index : int) -> Bisector_PointOnBis: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
