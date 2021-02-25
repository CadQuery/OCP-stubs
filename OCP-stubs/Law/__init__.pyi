import OCP.Law
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.TColStd
import OCP.NCollection
import OCP.GeomAbs
import OCP.TColgp
import OCP.Standard
__all__  = [
"Law",
"Law_Function",
"Law_BSpline",
"Law_BSplineKnotSplitting",
"Law_Composite",
"Law_Constant",
"Law_BSpFunc",
"Law_Interpol",
"Law_Interpolate",
"Law_Laws",
"Law_Linear",
"Law_S"
]
class Law():
    """
    Multiple services concerning 1d functions.
    """
    @staticmethod
    @overload
    def MixBnd_s(Degree : int,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,Lin : Law_Linear) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        This algorithm searches the knot values corresponding to the splitting of a given B-spline law into several arcs with the same continuity. The continuity order is given at the construction time. Builds a 1d bspline that is near from Lin with null derivatives at the extremities.

        Builds the poles of the 1d bspline that is near from Lin with null derivatives at the extremities.
        """
    @staticmethod
    @overload
    def MixBnd_s(Lin : Law_Linear) -> Law_BSpFunc: ...
    @staticmethod
    def MixTgt_s(Degree : int,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,NulOnTheRight : bool,Index : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Builds the poles of the 1d bspline that is null on the rigth side of Knots(Index) (on the left if NulOnTheRight is false) and that is like a t*(1-t)(1-t) curve on the left side of Knots(Index) (on the rigth if NulOnTheRight is false). The result curve is C1 with a derivative equal to 1. at first parameter (-1 at last parameter if NulOnTheRight is false). Warning: Mults(Index) must greater or equal to degree-1.
        """
    @staticmethod
    def Reparametrize_s(Curve : OCP.Adaptor3d.Adaptor3d_Curve,First : float,Last : float,HasDF : bool,HasDL : bool,DFirst : float,DLast : float,Rev : bool,NbPoints : int) -> Law_BSpline: 
        """
        Computes a 1 d curve to reparametrize a curve. Its an interpolation of NbPoints points calculated at quasi constant abscissa.
        """
    @staticmethod
    def ScaleCub_s(First : float,Last : float,HasF : bool,HasL : bool,VFirst : float,VLast : float) -> Law_BSpline: 
        """
        None
        """
    @staticmethod
    def Scale_s(First : float,Last : float,HasF : bool,HasL : bool,VFirst : float,VLast : float) -> Law_BSpline: 
        """
        Computes a 1 d curve to scale a field of tangency. Value is 1. for t = (First+Last)/2 . If HasFirst value for t = First is VFirst (null derivative). If HasLast value for t = Last is VLast (null derivative).
        """
    def __init__(self) -> None: ...
    pass
class Law_Function(OCP.Standard.Standard_Transient):
    """
    Root class for evolution laws.Root class for evolution laws.Root class for evolution laws.
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        Returns the parametric bounds of the function.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def D1(self,X : float) -> Tuple[float, float]: 
        """
        Returns the value F and the first derivative D of the function at the point of parameter X.
        """
    def D2(self,X : float) -> Tuple[float, float, float]: 
        """
        Returns the value, first and seconde derivatives at parameter X.
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
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,PFirst : float,PLast : float,Tol : float) -> Law_Function: 
        """
        Returns a law equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. It is usfule to determines the derivatives in these values <First> and <Last> if the Law is not Cn.
        """
    def Value(self,X : float) -> float: 
        """
        Returns the value of the function at the point of parameter X.
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
class Law_BSpline(OCP.Standard.Standard_Transient):
    """
    Definition of the 1D B_spline curve.Definition of the 1D B_spline curve.Definition of the 1D B_spline curve.
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the global continuity of the curve : C0 : only geometric continuity, C1 : continuity of the first derivative all along the Curve, C2 : continuity of the second derivative all along the Curve, C3 : continuity of the third derivative all along the Curve, CN : the order of continuity is infinite. For a B-spline curve of degree d if a knot Ui has a multiplicity p the B-spline curve is only Cd-p continuous at Ui. So the global continuity of the curve can't be greater than Cd-p where p is the maximum multiplicity of the interior Knots. In the interior of a knot span the curve is infinitely continuously differentiable.
        """
    def Copy(self) -> Law_BSpline: 
        """
        None
        """
    def D0(self,U : float) -> Tuple[float]: 
        """
        None
        """
    def D1(self,U : float) -> Tuple[float, float]: 
        """
        None
        """
    def D2(self,U : float) -> Tuple[float, float, float]: 
        """
        None
        """
    def D3(self,U : float) -> Tuple[float, float, float, float]: 
        """
        None
        """
    def DN(self,U : float,N : int) -> float: 
        """
        The following functions computes the point of parameter U and the derivatives at this point on the B-spline curve arc defined between the knot FromK1 and the knot ToK2. U can be out of bounds [Knot (FromK1), Knot (ToK2)] but for the computation we only use the definition of the curve between these two knots. This method is useful to compute local derivative, if the order of continuity of the whole curve is not greater enough. Inside the parametric domain Knot (FromK1), Knot (ToK2) the evaluations are the same as if we consider the whole definition of the curve. Of course the evaluations are different outside this parametric domain.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
        """
        Computation of value and derivatives
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndPoint(self) -> float: 
        """
        Returns the last point of the curve. Warnings : The last point of the curve is different from the last pole of the curve if the multiplicity of the last knot is lower than Degree.
        """
    def FirstParameter(self) -> float: 
        """
        Computes the parametric value of the start point of the curve. It is a knot value.
        """
    def FirstUKnotIndex(self) -> int: 
        """
        For a B-spline curve the first parameter (which gives the start point of the curve) is a knot value but if the multiplicity of the first knot index is lower than Degree + 1 it is not the first knot of the curve. This method computes the index of the knot corresponding to the first parameter.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncreaseDegree(self,Degree : int) -> None: 
        """
        Increase the degree to <Degree>. Nothing is done if <Degree> is lower or equal to the current degree.
        """
    @overload
    def IncreaseMultiplicity(self,I1 : int,I2 : int,M : int) -> None: 
        """
        Increases the multiplicity of the knot <Index> to <M>.

        Increases the multiplicities of the knots in [I1,I2] to <M>.
        """
    @overload
    def IncreaseMultiplicity(self,Index : int,M : int) -> None: ...
    def IncrementMultiplicity(self,I1 : int,I2 : int,M : int) -> None: 
        """
        Increment the multiplicities of the knots in [I1,I2] by <M>.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InsertKnot(self,U : float,M : int=1,ParametricTolerance : float=0.0,Add : bool=True) -> None: 
        """
        Inserts a knot value in the sequence of knots. If <U> is an existing knot the multiplicity is increased by <M>.
        """
    def InsertKnots(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,ParametricTolerance : float=0.0,Add : bool=False) -> None: 
        """
        Inserts a set of knots values in the sequence of knots.
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns the continuity of the curve, the curve is at least C0. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns true if the distance between the first point and the last point of the curve is lower or equal to Resolution from package gp. Warnings : The first and the last point can be different from the first pole and the last pole of the curve.
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
        Returns True if the curve is periodic.
        """
    def IsRational(self) -> bool: 
        """
        Returns True if the weights are not identical. The tolerance criterion is Epsilon of the class Real.
        """
    def Knot(self,Index : int) -> float: 
        """
        Returns the knot of range Index. When there is a knot with a multiplicity greater than 1 the knot is not repeated. The method Multiplicity can be used to get the multiplicity of the Knot. Raised if Index < 1 or Index > NbKnots
        """
    def KnotDistribution(self) -> OCP.GeomAbs.GeomAbs_BSplKnotDistribution: 
        """
        Returns NonUniform or Uniform or QuasiUniform or PiecewiseBezier. If all the knots differ by a positive constant from the preceding knot the BSpline Curve can be : - Uniform if all the knots are of multiplicity 1, - QuasiUniform if all the knots are of multiplicity 1 except for the first and last knot which are of multiplicity Degree + 1, - PiecewiseBezier if the first and last knots have multiplicity Degree + 1 and if interior knots have multiplicity Degree A piecewise Bezier with only two knots is a BezierCurve. else the curve is non uniform. The tolerance criterion is Epsilon from class Real.
        """
    def KnotSequence(self,K : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the knots sequence. In this sequence the knots with a multiplicity greater than 1 are repeated. Example : K = {k1, k1, k1, k2, k3, k3, k4, k4, k4}
        """
    def Knots(self,K : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        returns the knot values of the B-spline curve;
        """
    def LastParameter(self) -> float: 
        """
        Computes the parametric value of the end point of the curve. It is a knot value.
        """
    def LastUKnotIndex(self) -> int: 
        """
        For a BSpline curve the last parameter (which gives the end point of the curve) is a knot value but if the multiplicity of the last knot index is lower than Degree + 1 it is not the last knot of the curve. This method computes the index of the knot corresponding to the last parameter.
        """
    def LocalD0(self,U : float,FromK1 : int,ToK2 : int) -> Tuple[float]: 
        """
        None
        """
    def LocalD1(self,U : float,FromK1 : int,ToK2 : int) -> Tuple[float, float]: 
        """
        None
        """
    def LocalD2(self,U : float,FromK1 : int,ToK2 : int) -> Tuple[float, float, float]: 
        """
        None
        """
    def LocalD3(self,U : float,FromK1 : int,ToK2 : int) -> Tuple[float, float, float, float]: 
        """
        None
        """
    def LocalDN(self,U : float,FromK1 : int,ToK2 : int,N : int) -> float: 
        """
        None
        """
    def LocalValue(self,U : float,FromK1 : int,ToK2 : int) -> float: 
        """
        None
        """
    def LocateU(self,U : float,ParametricTolerance : float,WithKnotRepetition : bool=False) -> Tuple[int, int]: 
        """
        Locates the parametric value U in the sequence of knots. If "WithKnotRepetition" is True we consider the knot's representation with repetition of multiple knot value, otherwise we consider the knot's representation with no repetition of multiple knot values. Knots (I1) <= U <= Knots (I2) . if I1 = I2 U is a knot value (the tolerance criterion ParametricTolerance is used). . if I1 < 1 => U < Knots (1) - Abs(ParametricTolerance) . if I2 > NbKnots => U > Knots (NbKnots) + Abs(ParametricTolerance)
        """
    @staticmethod
    def MaxDegree_s() -> int: 
        """
        Returns the value of the maximum degree of the normalized B-spline basis functions in this package.
        """
    def MovePointAndTangent(self,U : float,NewValue : float,Derivative : float,Tolerance : float,StartingCondition : int,EndingCondition : int) -> Tuple[int]: 
        """
        Changes the value of the Law at parameter U to NewValue. and makes its derivative at U be derivative. StartingCondition = -1 means first can move EndingCondition = -1 means last point can move StartingCondition = 0 means the first point cannot move EndingCondition = 0 means the last point cannot move StartingCondition = 1 means the first point and tangent cannot move EndingCondition = 1 means the last point and tangent cannot move and so forth ErrorStatus != 0 means that there are not enought degree of freedom with the constrain to deform the curve accordingly
        """
    def Multiplicities(self,M : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Returns the multiplicity of the knots of the curve.
        """
    def Multiplicity(self,Index : int) -> int: 
        """
        Returns the multiplicity of the knots of range Index. Raised if Index < 1 or Index > NbKnots
        """
    def NbKnots(self) -> int: 
        """
        Returns the number of knots. This method returns the number of knot without repetition of multiple knots.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles
        """
    def PeriodicNormalization(self) -> Tuple[float]: 
        """
        returns the parameter normalized within the period if the curve is periodic : otherwise does not do anything
        """
    def Pole(self,Index : int) -> float: 
        """
        Returns the pole of range Index. Raised if Index < 1 or Index > NbPoles.
        """
    def Poles(self,P : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the poles of the B-spline curve;
        """
    def RemoveKnot(self,Index : int,M : int,Tolerance : float) -> bool: 
        """
        Decrement the knots multiplicity to <M>. If M is 0 the knot is removed. The Poles sequence is modified.
        """
    def Resolution(self,Tolerance3D : float) -> Tuple[float]: 
        """
        given Tolerance3D returns UTolerance such that if f(t) is the curve we have | t1 - t0| < Utolerance ===> |f(t1) - f(t0)| < Tolerance3D
        """
    def Reverse(self) -> None: 
        """
        Changes the direction of parametrization of <me>. The Knot sequence is modified, the FirstParameter and the LastParameter are not modified. The StartPoint of the initial curve becomes the EndPoint of the reversed curve and the EndPoint of the initial curve becomes the StartPoint of the reversed curve.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the reversed curve for the point of parameter U on <me>.
        """
    def Segment(self,U1 : float,U2 : float) -> None: 
        """
        Segments the curve between U1 and U2. The control points are modified, the first and the last point are not the same. Warnings : Even if <me> is not closed it can become closed after the segmentation for example if U1 or U2 are out of the bounds of the curve <me> or if the curve makes loop. After the segmentation the length of a curve can be null. raises if U2 < U1.
        """
    @overload
    def SetKnot(self,Index : int,K : float,M : int) -> None: 
        """
        Changes the knot of range Index. The multiplicity of the knot is not modified. Raised if K >= Knots(Index+1) or K <= Knots(Index-1). Raised if Index < 1 || Index > NbKnots

        Changes the knot of range Index with its multiplicity. You can increase the multiplicity of a knot but it is not allowed to decrease the multiplicity of an existing knot.
        """
    @overload
    def SetKnot(self,Index : int,K : float) -> None: ...
    def SetKnots(self,K : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Changes all the knots of the curve The multiplicity of the knots are not modified.
        """
    def SetNotPeriodic(self) -> None: 
        """
        Makes a non periodic curve. If the curve was non periodic the curve is not modified.
        """
    def SetOrigin(self,Index : int) -> None: 
        """
        Set the origin of a periodic curve at Knot(index) KnotVector and poles are modified. Raised if the curve is not periodic Raised if index not in the range [FirstUKnotIndex , LastUKnotIndex]
        """
    def SetPeriodic(self) -> None: 
        """
        Makes a closed B-spline into a periodic curve. The curve is periodic if the knot sequence is periodic and if the curve is closed (The tolerance criterion is Resolution from gp). The period T is equal to Knot(LastUKnotIndex) - Knot(FirstUKnotIndex). A periodic B-spline can be uniform or not. Raised if the curve is not closed.
        """
    @overload
    def SetPole(self,Index : int,P : float,Weight : float) -> None: 
        """
        Substitutes the Pole of range Index with P.

        Substitutes the pole and the weight of range Index. If the curve <me> is not rational it can become rational If the curve was rational it can become non rational
        """
    @overload
    def SetPole(self,Index : int,P : float) -> None: ...
    def SetWeight(self,Index : int,Weight : float) -> None: 
        """
        Changes the weight for the pole of range Index. If the curve was non rational it can become rational. If the curve was rational it can become non rational.
        """
    def StartPoint(self) -> float: 
        """
        Returns the start point of the curve. Warnings : This point is different from the first pole of the curve if the multiplicity of the first knot is lower than Degree.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,U : float) -> float: 
        """
        None
        """
    def Weight(self,Index : int) -> float: 
        """
        Returns the weight of the pole of range Index . Raised if Index < 1 or Index > NbPoles.
        """
    def Weights(self,W : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the weights of the B-spline curve;
        """
    @overload
    def __init__(self,Poles : OCP.TColStd.TColStd_Array1OfReal,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Multiplicities : OCP.TColStd.TColStd_Array1OfInteger,Degree : int,Periodic : bool=False) -> None: ...
    @overload
    def __init__(self,Poles : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Multiplicities : OCP.TColStd.TColStd_Array1OfInteger,Degree : int,Periodic : bool=False) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class Law_BSplineKnotSplitting():
    """
    For a B-spline curve the discontinuities are localised at the knot values and between two knots values the B-spline is infinitely continuously differentiable. At a knot of range index the continuity is equal to : Degree - Mult (Index) where Degree is the degree of the basis B-spline functions and Mult the multiplicity of the knot of range Index. If for your computation you need to have B-spline curves with a minima of continuity it can be interesting to know between which knot values, a B-spline curve arc, has a continuity of given order. This algorithm computes the indexes of the knots where you should split the curve, to obtain arcs with a constant continuity given at the construction time. The splitting values are in the range [FirstUKnotValue, LastUKnotValue] (See class B-spline curve from package Geom). If you just want to compute the local derivatives on the curve you don't need to create the B-spline curve arcs, you can use the functions LocalD1, LocalD2, LocalD3, LocalDN of the class BSplineCurve.
    """
    def NbSplits(self) -> int: 
        """
        Returns the number of knots corresponding to the splitting.
        """
    def SplitValue(self,Index : int) -> int: 
        """
        Returns the index of the knot corresponding to the splitting of range Index.
        """
    def Splitting(self,SplitValues : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Returns the indexes of the BSpline curve knots corresponding to the splitting.
        """
    def __init__(self,BasisLaw : Law_BSpline,ContinuityRange : int) -> None: ...
    pass
class Law_Composite(Law_Function, OCP.Standard.Standard_Transient):
    """
    Loi composite constituee d une liste de lois de ranges consecutifs. Cette implementation un peu lourde permet de reunir en une seule loi des portions de loi construites de facon independantes (par exemple en interactif) et de lancer le walking d un coup a l echelle d une ElSpine. CET OBJET REPOND DONC A UN PROBLEME D IMPLEMENTATION SPECIFIQUE AUX CONGES!!!Loi composite constituee d une liste de lois de ranges consecutifs. Cette implementation un peu lourde permet de reunir en une seule loi des portions de loi construites de facon independantes (par exemple en interactif) et de lancer le walking d un coup a l echelle d une ElSpine. CET OBJET REPOND DONC A UN PROBLEME D IMPLEMENTATION SPECIFIQUE AUX CONGES!!!Loi composite constituee d une liste de lois de ranges consecutifs. Cette implementation un peu lourde permet de reunir en une seule loi des portions de loi construites de facon independantes (par exemple en interactif) et de lancer le walking d un coup a l echelle d une ElSpine. CET OBJET REPOND DONC A UN PROBLEME D IMPLEMENTATION SPECIFIQUE AUX CONGES!!!
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        Returns the parametric bounds of the function.
        """
    def ChangeElementaryLaw(self,W : float) -> Law_Function: 
        """
        Returns the elementary function of the composite used to compute at parameter W.
        """
    def ChangeLaws(self) -> Law_Laws: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def D1(self,X : float) -> Tuple[float, float]: 
        """
        Returns the value and the first derivative at parameter X.
        """
    def D2(self,X : float) -> Tuple[float, float, float]: 
        """
        Returns the value, first and second derivatives at parameter X.
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
    def IsPeriodic(self) -> bool: 
        """
        None
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetPeriodic(self) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,PFirst : float,PLast : float,Tol : float) -> Law_Function: 
        """
        Returns a law equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. It is usfule to determines the derivatives in these values <First> and <Last> if the Law is not Cn.
        """
    def Value(self,X : float) -> float: 
        """
        Returns the value at parameter X.
        """
    @overload
    def __init__(self,First : float,Last : float,Tol : float) -> None: ...
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
class Law_Constant(Law_Function, OCP.Standard.Standard_Transient):
    """
    Loi constanteLoi constanteLoi constante
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        Returns the parametric bounds of the function.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_CN
        """
    def D1(self,X : float) -> Tuple[float, float]: 
        """
        Returns the value and the first derivative at parameter X.
        """
    def D2(self,X : float) -> Tuple[float, float, float]: 
        """
        Returns the value, first and second derivatives at parameter X.
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
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
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
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns 1
        """
    def Set(self,Radius : float,PFirst : float,PLast : float) -> None: 
        """
        Set the radius and the range of the constant Law.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,PFirst : float,PLast : float,Tol : float) -> Law_Function: 
        """
        None
        """
    def Value(self,X : float) -> float: 
        """
        Returns the value at parameter X.
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
class Law_BSpFunc(Law_Function, OCP.Standard.Standard_Transient):
    """
    Law Function based on a BSpline curve 1d. Package methods and classes are implemented in package Law to construct the basis curve with several constraints.Law Function based on a BSpline curve 1d. Package methods and classes are implemented in package Law to construct the basis curve with several constraints.Law Function based on a BSpline curve 1d. Package methods and classes are implemented in package Law to construct the basis curve with several constraints.
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def Curve(self) -> Law_BSpline: 
        """
        None
        """
    def D1(self,X : float) -> Tuple[float, float]: 
        """
        None
        """
    def D2(self,X : float) -> Tuple[float, float, float]: 
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
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def SetCurve(self,C : Law_BSpline) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,PFirst : float,PLast : float,Tol : float) -> Law_Function: 
        """
        Returns a law equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. It is usfule to determines the derivatives in these values <First> and <Last> if the Law is not Cn.
        """
    def Value(self,X : float) -> float: 
        """
        None
        """
    @overload
    def __init__(self,C : Law_BSpline,First : float,Last : float) -> None: ...
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
class Law_Interpol(Law_BSpFunc, Law_Function, OCP.Standard.Standard_Transient):
    """
    Provides an evolution law that interpolates a set of parameter and value pairs (wi, radi)Provides an evolution law that interpolates a set of parameter and value pairs (wi, radi)Provides an evolution law that interpolates a set of parameter and value pairs (wi, radi)
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def Curve(self) -> Law_BSpline: 
        """
        None
        """
    def D1(self,X : float) -> Tuple[float, float]: 
        """
        None
        """
    def D2(self,X : float) -> Tuple[float, float, float]: 
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
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    @overload
    def Set(self,ParAndRad : OCP.TColgp.TColgp_Array1OfPnt2d,Dd : float,Df : float,Periodic : bool=False) -> None: 
        """
        Defines this evolution law by interpolating the set of 2D points ParAndRad. The Y coordinate of a point of ParAndRad is the value of the function at the parameter point given by its X coordinate. If Periodic is true, this function is assumed to be periodic. Warning - The X coordinates of points in the table ParAndRad must be given in ascendant order. - If Periodic is true, the first and last Y coordinates of points in the table ParAndRad are assumed to be equal. In addition, with the second syntax, Dd and Df are also assumed to be equal. If this is not the case, Set uses the first value(s) as last value(s).

        Defines this evolution law by interpolating the set of 2D points ParAndRad. The Y coordinate of a point of ParAndRad is the value of the function at the parameter point given by its X coordinate. If Periodic is true, this function is assumed to be periodic. In the second syntax, Dd and Df define the values of the first derivative of the function at its first and last points. Warning - The X coordinates of points in the table ParAndRad must be given in ascendant order. - If Periodic is true, the first and last Y coordinates of points in the table ParAndRad are assumed to be equal. In addition, with the second syntax, Dd and Df are also assumed to be equal. If this is not the case, Set uses the first value(s) as last value(s).
        """
    @overload
    def Set(self,ParAndRad : OCP.TColgp.TColgp_Array1OfPnt2d,Periodic : bool=False) -> None: ...
    def SetCurve(self,C : Law_BSpline) -> None: 
        """
        None
        """
    @overload
    def SetInRelative(self,ParAndRad : OCP.TColgp.TColgp_Array1OfPnt2d,Ud : float,Uf : float,Periodic : bool=False) -> None: 
        """
        None

        None
        """
    @overload
    def SetInRelative(self,ParAndRad : OCP.TColgp.TColgp_Array1OfPnt2d,Ud : float,Uf : float,Dd : float,Df : float,Periodic : bool=False) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,PFirst : float,PLast : float,Tol : float) -> Law_Function: 
        """
        Returns a law equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. It is usfule to determines the derivatives in these values <First> and <Last> if the Law is not Cn.
        """
    def Value(self,X : float) -> float: 
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
class Law_Interpolate():
    """
    This class is used to interpolate a BsplineCurve passing through an array of points, with a C2 Continuity if tangency is not requested at the point. If tangency is requested at the point the continuity will be C1. If Perodicity is requested the curve will be closed and the junction will be the first point given. The curve will than be only C1
    """
    def Curve(self) -> Law_BSpline: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    @overload
    def Load(self,InitialTangent : float,FinalTangent : float) -> None: 
        """
        loads initial and final tangents if any.

        loads the tangents. We should have as many tangents as they are points in the array if TangentFlags.Value(i) is Standard_True use the tangent Tangents.Value(i) otherwise the tangent is not constrained.
        """
    @overload
    def Load(self,Tangents : OCP.TColStd.TColStd_Array1OfReal,TangentFlags : OCP.TColStd.TColStd_HArray1OfBoolean) -> None: ...
    def Perform(self) -> None: 
        """
        Makes the interpolation
        """
    @overload
    def __init__(self,Points : OCP.TColStd.TColStd_HArray1OfReal,PeriodicFlag : bool,Tolerance : float) -> None: ...
    @overload
    def __init__(self,Points : OCP.TColStd.TColStd_HArray1OfReal,Parameters : OCP.TColStd.TColStd_HArray1OfReal,PeriodicFlag : bool,Tolerance : float) -> None: ...
    pass
class Law_Laws(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Law_Function) -> Law_Function: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : Law_Function,theIter : Any) -> None: ...
    @overload
    def Append(self,theOther : Law_Laws) -> None: ...
    def Assign(self,theOther : Law_Laws) -> Law_Laws: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> Law_Function: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : Law_Laws,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : Law_Function,theIter : Any) -> Law_Function: ...
    @overload
    def InsertBefore(self,theItem : Law_Function,theIter : Any) -> Law_Function: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : Law_Laws,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> Law_Function: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : Law_Laws) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : Law_Function) -> Law_Function: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Law_Laws) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Law_Linear(Law_Function, OCP.Standard.Standard_Transient):
    """
    Describes an linear evolution law.Describes an linear evolution law.Describes an linear evolution law.
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        Returns the parametric bounds of the function.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_CN
        """
    def D1(self,X : float) -> Tuple[float, float]: 
        """
        Returns the value F and the first derivative D of this function at the point of parameter X.
        """
    def D2(self,X : float) -> Tuple[float, float, float]: 
        """
        Returns the value, first and second derivatives at parameter X.
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
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
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
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns 1
        """
    def Set(self,Pdeb : float,Valdeb : float,Pfin : float,Valfin : float) -> None: 
        """
        Defines this linear evolution law by assigning both: - the bounds Pdeb and Pfin of the parameter, and - the values Valdeb and Valfin of the function at these two parametric bounds.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,PFirst : float,PLast : float,Tol : float) -> Law_Function: 
        """
        Returns a law equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. It is usfule to determines the derivatives in these values <First> and <Last> if the Law is not Cn.
        """
    def Value(self,X : float) -> float: 
        """
        Returns the value of this function at the point of parameter X.
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
class Law_S(Law_BSpFunc, Law_Function, OCP.Standard.Standard_Transient):
    """
    Describes an "S" evolution law.Describes an "S" evolution law.Describes an "S" evolution law.
    """
    def Bounds(self) -> Tuple[float, float]: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def Curve(self) -> Law_BSpline: 
        """
        None
        """
    def D1(self,X : float) -> Tuple[float, float]: 
        """
        None
        """
    def D2(self,X : float) -> Tuple[float, float, float]: 
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
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    @overload
    def Set(self,Pdeb : float,Valdeb : float,Ddeb : float,Pfin : float,Valfin : float,Dfin : float) -> None: 
        """
        Defines this S evolution law by assigning both: - the bounds Pdeb and Pfin of the parameter, and - the values Valdeb and Valfin of the function at these two parametric bounds. The function is assumed to have the first derivatives equal to 0 at the two parameter points Pdeb and Pfin.

        Defines this S evolution law by assigning - the bounds Pdeb and Pfin of the parameter, - the values Valdeb and Valfin of the function at these two parametric bounds, and - the values Ddeb and Dfin of the first derivative of the function at these two parametric bounds.
        """
    @overload
    def Set(self,Pdeb : float,Valdeb : float,Pfin : float,Valfin : float) -> None: ...
    def SetCurve(self,C : Law_BSpline) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trim(self,PFirst : float,PLast : float,Tol : float) -> Law_Function: 
        """
        Returns a law equivalent of <me> between parameters <First> and <Last>. <Tol> is used to test for 3d points confusion. It is usfule to determines the derivatives in these values <First> and <Last> if the Law is not Cn.
        """
    def Value(self,X : float) -> float: 
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
