import OCP.BlendFunc
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Blend
import OCP.Adaptor3d
import OCP.Law
import OCP.Adaptor2d
import OCP.Convert
import OCP.GeomAbs
import OCP.TColgp
import OCP.math
import OCP.gp
import OCP.TColStd
__all__  = [
"BlendFunc",
"BlendFunc_CSCircular",
"BlendFunc_CSConstRad",
"BlendFunc_ChAsym",
"BlendFunc_ChAsymInv",
"BlendFunc_GenChamfInv",
"BlendFunc_GenChamfer",
"BlendFunc_ConstRad",
"BlendFunc_ConstRadInv",
"BlendFunc_ConstThroat",
"BlendFunc_ConstThroatInv",
"BlendFunc_ConstThroatWithPenetration",
"BlendFunc_ConstThroatWithPenetrationInv",
"BlendFunc_Corde",
"BlendFunc_EvolRad",
"BlendFunc_EvolRadInv",
"BlendFunc_ChamfInv",
"BlendFunc_Chamfer",
"BlendFunc_Ruled",
"BlendFunc_RuledInv",
"BlendFunc_SectionShape",
"BlendFunc_Tensor",
"BlendFunc_Linear",
"BlendFunc_Polynomial",
"BlendFunc_QuasiAngular",
"BlendFunc_Rational"
]
class BlendFunc():
    """
    This package provides a set of generic functions, that can instantiated to compute blendings between two surfaces (Constant radius, Evolutive radius, Ruled surface).
    """
    @staticmethod
    def ComputeDNormal_s(Surf : OCP.Adaptor3d.Adaptor3d_Surface,p2d : OCP.gp.gp_Pnt2d,Normal : OCP.gp.gp_Vec,DNu : OCP.gp.gp_Vec,DNv : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    @staticmethod
    def ComputeNormal_s(Surf : OCP.Adaptor3d.Adaptor3d_Surface,p2d : OCP.gp.gp_Pnt2d,Normal : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    @staticmethod
    def GetMinimalWeights_s(SectShape : BlendFunc_SectionShape,TConv : OCP.Convert.Convert_ParameterisationType,AngleMin : float,AngleMax : float,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    @staticmethod
    def GetShape_s(SectShape : BlendFunc_SectionShape,MaxAng : float,TypeConv : OCP.Convert.Convert_ParameterisationType) -> Tuple[int, int, int]: 
        """
        None
        """
    @staticmethod
    def NextShape_s(S : OCP.GeomAbs.GeomAbs_Shape) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Used to obtain the next level of continuity.
        """
    def __init__(self) -> None: ...
    pass
class BlendFunc_CSCircular(OCP.Blend.Blend_CSFunction, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSection(self,Param : float,U : float,V : float,W : float,tabP : OCP.TColgp.TColgp_Array1OfPnt,tabV : OCP.TColgp.TColgp_Array1OfVec) -> bool: 
        """
        None
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def IsTangencyPoint(self) -> bool: 
        """
        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function (3).
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def ParameterOnC(self) -> float: 
        """
        Returns parameter of the point on the curve.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def Pnt2d(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns U,V coordinates of the point on the surface.
        """
    def PointOnC(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def PointOnS(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        Used for the first and last section

        None

        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,Param : float,U : float,V : float,W : float,C : OCP.gp.gp_Circ) -> Tuple[float, float]: ...
    @overload
    def Set(self,First : float,Last : float) -> None: 
        """
        None

        None

        None

        Sets the type of section generation for the approximations.
        """
    @overload
    def Set(self,Param : float) -> None: ...
    @overload
    def Set(self,TypeSection : BlendFunc_SectionShape) -> None: ...
    @overload
    def Set(self,Radius : float,Choix : int) -> None: ...
    def Tangent(self,U : float,V : float,TgS : OCP.gp.gp_Vec,NormS : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surface) at these points.
        """
    def Tangent2d(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnC(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnS(self) -> OCP.gp.gp_Vec: 
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
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve,CGuide : OCP.Adaptor3d.Adaptor3d_Curve,L : OCP.Law.Law_Function) -> None: ...
    pass
class BlendFunc_CSConstRad(OCP.Blend.Blend_CSFunction, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSection(self,Param : float,U : float,V : float,W : float,tabP : OCP.TColgp.TColgp_Array1OfPnt,tabV : OCP.TColgp.TColgp_Array1OfVec) -> bool: 
        """
        None
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>. The array must provide enough room to accommodate for the parameters. i.e. T.Length() > NbIntervals() raises OutOfRange from Standard
        """
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def IsTangencyPoint(self) -> bool: 
        """
        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function (3).
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 3 (default value). Can be redefined.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def ParameterOnC(self) -> float: 
        """
        Returns parameter of the point on the curve.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def Pnt2d(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns U,V coordinates of the point on the surface.
        """
    def PointOnC(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def PointOnS(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        Used for the first and last section

        None

        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,Param : float,U : float,V : float,W : float,C : OCP.gp.gp_Circ) -> Tuple[float, float]: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Set(self,TypeSection : BlendFunc_SectionShape) -> None: 
        """
        None

        None

        None

        Sets the type of section generation for the approximations.
        """
    @overload
    def Set(self,Radius : float,Choix : int) -> None: ...
    @overload
    def Set(self,Param : float) -> None: ...
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    def Tangent(self,U : float,V : float,TgS : OCP.gp.gp_Vec,NormS : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surface) at these points.
        """
    def Tangent2d(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnC(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnS(self) -> OCP.gp.gp_Vec: 
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
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve,CGuide : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_ChAsym(OCP.Blend.Blend_Function, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def ComputeValues(self,X : OCP.math.math_Vector,DegF : int,DegL : int) -> bool: 
        """
        computes the values <F> of the derivatives for the variable <X> between DegF and DegL. Returns True if the computation was done successfully, False otherwise.
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def IsTangencyPoint(self) -> bool: 
        """
        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def PointOnS1(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def PointOnS2(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        None

        Used for the first and last section

        Used for the first and last section

        Utile pour une visu rapide et approximative de la surface.
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,C : OCP.gp.gp_Lin) -> Tuple[float, float]: ...
    @overload
    def Set(self,Dist1 : float,Angle : float,Choix : int) -> None: 
        """
        None

        None

        Sets the distances and the angle.
        """
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    @overload
    def Set(self,Param : float) -> None: ...
    def Tangent(self,U1 : float,V1 : float,U2 : float,V2 : float,TgFirst : OCP.gp.gp_Vec,TgLast : OCP.gp.gp_Vec,NormFirst : OCP.gp.gp_Vec,NormLast : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surfaces) at these points.
        """
    def Tangent2dOnS1(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnS2(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnS1(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnS2(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TwistOnS1(self) -> bool: 
        """
        None
        """
    def TwistOnS2(self) -> bool: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_ChAsymInv(OCP.Blend.Blend_FuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def ComputeValues(self,X : OCP.math.math_Vector,DegF : int,DegL : int) -> bool: 
        """
        computes the values <F> of the derivatives for the variable <X> between DegF and DegL. Returns True if the computation was done successfully, False otherwise.
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    @overload
    def Set(self,OnFirst : bool,COnSurf : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        None

        None
        """
    @overload
    def Set(self,Dist1 : float,Angle : float,Choix : int) -> None: ...
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_GenChamfInv(OCP.Blend.Blend_FuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a general chamfer on a surface's boundary
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        Returns Standard_True if Sol is a zero of the function. Tol is the tolerance used in 3d space.
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    @overload
    def Set(self,OnFirst : bool,COnSurf : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        None

        None
        """
    @overload
    def Set(self,Dist1 : float,Dist2 : float,Choix : int) -> None: ...
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_GenChamfer(OCP.Blend.Blend_Function, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a general chamfer
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsRational(self) -> bool: 
        """
        Returns False
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        Returns Standard_True if Sol is a zero of the function. Tol is the tolerance used in 3d space. The computation is made at the current value of the parameter on the guide line.
        """
    def IsTangencyPoint(self) -> bool: 
        """
        Returns True when it is not possible to compute the tangent vectors at PointOnS1 and/or PointOnS2.
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def PointOnS1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first surface, at parameter Sol(1),Sol(2) (Sol is the vector used in the call of IsSolution.
        """
    def PointOnS2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the second surface, at parameter Sol(3),Sol(4) (Sol is the vector used in the call of IsSolution.
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section

        Used for the first and last section

        None

        Obsolete method
        """
    @overload
    def Section(self,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,C : OCP.gp.gp_Lin) -> Tuple[float, float]: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self,Param : float) -> None: 
        """
        Sets the value of the parameter along the guide line. This determines the plane in which the solution has to be found.

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.

        Sets the distances and the "quadrant".
        """
    @overload
    def Set(self,Dist1 : float,Dist2 : float,Choix : int) -> None: ...
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    def Tangent(self,U1 : float,V1 : float,U2 : float,V2 : float,TgFirst : OCP.gp.gp_Vec,TgLast : OCP.gp.gp_Vec,NormFirst : OCP.gp.gp_Vec,NormLast : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surfaces) at these points.
        """
    def Tangent2dOnS1(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the tangent vector at PointOnS1, in the parametric space of the first surface.
        """
    def Tangent2dOnS2(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the tangent vector at PointOnS2, in the parametric space of the second surface.
        """
    def TangentOnS1(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent vector at PointOnS1, in 3d space.
        """
    def TangentOnS2(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent vector at PointOnS2, in 3d space.
        """
    def TwistOnS1(self) -> bool: 
        """
        None
        """
    def TwistOnS2(self) -> bool: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,CG : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_ConstRad(OCP.Blend.Blend_Function, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def AxeRot(self,Prm : float) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def IsTangencyPoint(self) -> bool: 
        """
        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def PointOnS1(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def PointOnS2(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Used for the first and last section

        Used for the first and last section

        None

        Utile pour une visu rapide et approximative de la surface.
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,C : OCP.gp.gp_Circ) -> Tuple[float, float]: ...
    @overload
    def Set(self,First : float,Last : float) -> None: 
        """
        None

        None

        Inits the value of radius, and the "quadrant".

        Sets the type of section generation for the approximations.
        """
    @overload
    def Set(self,TypeSection : BlendFunc_SectionShape) -> None: ...
    @overload
    def Set(self,Radius : float,Choix : int) -> None: ...
    @overload
    def Set(self,Param : float) -> None: ...
    def Tangent(self,U1 : float,V1 : float,U2 : float,V2 : float,TgFirst : OCP.gp.gp_Vec,TgLast : OCP.gp.gp_Vec,NormFirst : OCP.gp.gp_Vec,NormLast : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surfaces) at these points.
        """
    def Tangent2dOnS1(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnS2(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnS1(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnS2(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TwistOnS1(self) -> bool: 
        """
        None
        """
    def TwistOnS2(self) -> bool: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_ConstRadInv(OCP.Blend.Blend_FuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    @overload
    def Set(self,OnFirst : bool,COnSurf : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        None

        None
        """
    @overload
    def Set(self,R : float,Choix : int) -> None: ...
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_ConstThroat(BlendFunc_GenChamfer, OCP.Blend.Blend_Function, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Class for a function used to compute a symmetric chamfer with constant throat that is the height of isosceles triangle in section
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsRational(self) -> bool: 
        """
        Returns False
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def IsTangencyPoint(self) -> bool: 
        """
        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def PointOnS1(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def PointOnS2(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section

        Used for the first and last section

        None

        Obsolete method
        """
    @overload
    def Section(self,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,C : OCP.gp.gp_Lin) -> Tuple[float, float]: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self,aThroat : float,arg2 : float,Choix : int) -> None: 
        """
        None

        Sets the throat and the "quadrant".
        """
    @overload
    def Set(self,Param : float) -> None: ...
    def Tangent(self,U1 : float,V1 : float,U2 : float,V2 : float,TgFirst : OCP.gp.gp_Vec,TgLast : OCP.gp.gp_Vec,NormFirst : OCP.gp.gp_Vec,NormLast : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surfaces) at these points.
        """
    def Tangent2dOnS1(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnS2(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnS1(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnS2(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TwistOnS1(self) -> bool: 
        """
        None
        """
    def TwistOnS2(self) -> bool: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_ConstThroatInv(BlendFunc_GenChamfInv, OCP.Blend.Blend_FuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Class for a function used to compute a ConstThroat chamfer on a surface's boundary
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Set(self,theThroat : float,arg2 : float,Choix : int) -> None: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_ConstThroatWithPenetration(BlendFunc_ConstThroat, BlendFunc_GenChamfer, OCP.Blend.Blend_Function, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Class for a function used to compute a chamfer with constant throat: the section of chamfer is right-angled triangle, the first of two surfaces (where is the top of the chamfer) is virtually moved inside the solid by offset operation, the apex of the section is on the intersection curve between moved surface and second surface, right angle is at the top of the chamfer, the length of the leg from apex to top is constant - it is throat
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsRational(self) -> bool: 
        """
        Returns False
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def IsTangencyPoint(self) -> bool: 
        """
        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def PointOnS1(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def PointOnS2(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section

        Used for the first and last section

        None

        Obsolete method
        """
    @overload
    def Section(self,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,C : OCP.gp.gp_Lin) -> Tuple[float, float]: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self,aThroat : float,arg2 : float,Choix : int) -> None: 
        """
        None

        Sets the throat and the "quadrant".
        """
    @overload
    def Set(self,Param : float) -> None: ...
    def Tangent(self,U1 : float,V1 : float,U2 : float,V2 : float,TgFirst : OCP.gp.gp_Vec,TgLast : OCP.gp.gp_Vec,NormFirst : OCP.gp.gp_Vec,NormLast : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surfaces) at these points.
        """
    def Tangent2dOnS1(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnS2(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnS1(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnS2(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TwistOnS1(self) -> bool: 
        """
        None
        """
    def TwistOnS2(self) -> bool: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_ConstThroatWithPenetrationInv(BlendFunc_ConstThroatInv, BlendFunc_GenChamfInv, OCP.Blend.Blend_FuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Class for a function used to compute a ConstThroatWithPenetration chamfer on a surface's boundary
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Set(self,theThroat : float,arg2 : float,Choix : int) -> None: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_Corde():
    """
    This function calculates point (pts) on the curve of intersection between the normal to a curve (guide) in a chosen parameter and a surface (surf), so that pts was at a given distance from the guide. X(1),X(2) are the parameters U,V of pts on surf.
    """
    def DerFguide(self,Sol : OCP.math.math_Vector,DerF : OCP.gp.gp_Vec2d) -> None: 
        """
        Derived of the function compared to the parameter of the guideline
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        Returns False if Sol is not solution else returns True and updates the fields tgs and tg2d
        """
    def IsTangencyPoint(self) -> bool: 
        """
        Returns True when it is not possible to compute the tangent vectors at PointOnS.
        """
    def NPlan(self) -> OCP.gp.gp_Vec: 
        """
        returns the normal to CGuide at Ptgui.
        """
    def PointOnGuide(self) -> OCP.gp.gp_Pnt: 
        """
        returns the point of parameter <Param> on CGuide
        """
    def PointOnS(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def SetDist(self,Dist : float) -> None: 
        """
        None
        """
    def SetParam(self,Param : float) -> None: 
        """
        None
        """
    def Tangent2dOnS(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the tangent vector at PointOnS, in the parametric space of the first surface.
        """
    def TangentOnS(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent vector at PointOnS, in 3d space.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Function for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_Surface,CGuide : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_EvolRad(OCP.Blend.Blend_Function, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def IsTangencyPoint(self) -> bool: 
        """
        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def PointOnS1(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def PointOnS2(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section

        Used for the first and last section

        None

        Method for graphic traces
        """
    @overload
    def Section(self,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,C : OCP.gp.gp_Circ) -> Tuple[float, float]: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self,First : float,Last : float) -> None: 
        """
        None

        None

        None

        Sets the type of section generation for the approximations.
        """
    @overload
    def Set(self,Param : float) -> None: ...
    @overload
    def Set(self,Choix : int) -> None: ...
    @overload
    def Set(self,TypeSection : BlendFunc_SectionShape) -> None: ...
    def Tangent(self,U1 : float,V1 : float,U2 : float,V2 : float,TgFirst : OCP.gp.gp_Vec,TgLast : OCP.gp.gp_Vec,NormFirst : OCP.gp.gp_Vec,NormLast : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surfaces) at these points.
        """
    def Tangent2dOnS1(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnS2(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnS1(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnS2(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TwistOnS1(self) -> bool: 
        """
        None
        """
    def TwistOnS2(self) -> bool: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve,Law : OCP.Law.Law_Function) -> None: ...
    pass
class BlendFunc_EvolRadInv(OCP.Blend.Blend_FuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    @overload
    def Set(self,Choix : int) -> None: 
        """
        None

        None
        """
    @overload
    def Set(self,OnFirst : bool,COnSurf : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve,Law : OCP.Law.Law_Function) -> None: ...
    pass
class BlendFunc_ChamfInv(BlendFunc_GenChamfInv, OCP.Blend.Blend_FuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Class for a function used to compute a chamfer with two constant distances on a surface's boundary
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Set(self,Dist1 : float,Dist2 : float,Choix : int) -> None: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_Chamfer(BlendFunc_GenChamfer, OCP.Blend.Blend_Function, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Class for a function used to compute a "ordinary" chamfer: when distances from spine to surfaces are constant
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsRational(self) -> bool: 
        """
        Returns False
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def IsTangencyPoint(self) -> bool: 
        """
        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def PointOnS1(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def PointOnS2(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section

        Used for the first and last section

        None

        Obsolete method
        """
    @overload
    def Section(self,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,C : OCP.gp.gp_Lin) -> Tuple[float, float]: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self,Dist1 : float,Dist2 : float,Choix : int) -> None: 
        """
        None

        Sets the distances and the "quadrant".
        """
    @overload
    def Set(self,Param : float) -> None: ...
    def Tangent(self,U1 : float,V1 : float,U2 : float,V2 : float,TgFirst : OCP.gp.gp_Vec,TgLast : OCP.gp.gp_Vec,NormFirst : OCP.gp.gp_Vec,NormLast : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surfaces) at these points.
        """
    def Tangent2dOnS1(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnS2(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnS1(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnS2(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TwistOnS1(self) -> bool: 
        """
        None
        """
    def TwistOnS2(self) -> bool: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,CG : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_Ruled(OCP.Blend.Blend_Function, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def AxeRot(self,Prm : float) -> OCP.gp.gp_Ax1: 
        """
        None
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetMinimalDistance(self) -> float: 
        """
        Returns the minimal Distance between two extremities of calculated sections.
        """
    def GetMinimalWeight(self,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute the minimal value of weight for each poles of all sections.
        """
    def GetSection(self,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,tabP : OCP.TColgp.TColgp_Array1OfPnt,tabV : OCP.TColgp.TColgp_Array1OfVec) -> bool: 
        """
        None
        """
    def GetSectionSize(self) -> float: 
        """
        Returns the length of the maximum section
        """
    def GetShape(self) -> Tuple[int, int, int, int]: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    @overload
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.math.math_Vector,Tol1D : OCP.math.math_Vector) -> None: 
        """
        None

        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary SurfTol error inside the surface.
        """
    @overload
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: ...
    def Intervals(self,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    def IsRational(self) -> bool: 
        """
        Returns False
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def IsTangencyPoint(self) -> bool: 
        """
        None
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Mults(self,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the seconde support.
        """
    def PointOnS1(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def PointOnS2(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Used for the first and last section

        Used for the first and last section

        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self,Param : float) -> None: 
        """
        None

        None
        """
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    def Tangent(self,U1 : float,V1 : float,U2 : float,V2 : float,TgFirst : OCP.gp.gp_Vec,TgLast : OCP.gp.gp_Vec,NormFirst : OCP.gp.gp_Vec,NormLast : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surfaces) at these points.
        """
    def Tangent2dOnS1(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnS2(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnS1(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnS2(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TwistOnS1(self) -> bool: 
        """
        None
        """
    def TwistOnS2(self) -> bool: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_RuledInv(OCP.Blend.Blend_FuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        None
        """
    def IsSolution(self,Sol : OCP.math.math_Vector,Tol : float) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        Returns 4.
        """
    def Set(self,OnFirst : bool,COnSurf : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
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
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,S2 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: ...
    pass
class BlendFunc_SectionShape():
    """
    None

    Members:

      BlendFunc_Rational

      BlendFunc_QuasiAngular

      BlendFunc_Polynomial

      BlendFunc_Linear
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
    BlendFunc_Linear: OCP.BlendFunc.BlendFunc_SectionShape # value = <BlendFunc_SectionShape.BlendFunc_Linear: 3>
    BlendFunc_Polynomial: OCP.BlendFunc.BlendFunc_SectionShape # value = <BlendFunc_SectionShape.BlendFunc_Polynomial: 2>
    BlendFunc_QuasiAngular: OCP.BlendFunc.BlendFunc_SectionShape # value = <BlendFunc_SectionShape.BlendFunc_QuasiAngular: 1>
    BlendFunc_Rational: OCP.BlendFunc.BlendFunc_SectionShape # value = <BlendFunc_SectionShape.BlendFunc_Rational: 0>
    __entries: dict # value = {'BlendFunc_Rational': (<BlendFunc_SectionShape.BlendFunc_Rational: 0>, None), 'BlendFunc_QuasiAngular': (<BlendFunc_SectionShape.BlendFunc_QuasiAngular: 1>, None), 'BlendFunc_Polynomial': (<BlendFunc_SectionShape.BlendFunc_Polynomial: 2>, None), 'BlendFunc_Linear': (<BlendFunc_SectionShape.BlendFunc_Linear: 3>, None)}
    __members__: dict # value = {'BlendFunc_Rational': <BlendFunc_SectionShape.BlendFunc_Rational: 0>, 'BlendFunc_QuasiAngular': <BlendFunc_SectionShape.BlendFunc_QuasiAngular: 1>, 'BlendFunc_Polynomial': <BlendFunc_SectionShape.BlendFunc_Polynomial: 2>, 'BlendFunc_Linear': <BlendFunc_SectionShape.BlendFunc_Linear: 3>}
    pass
class BlendFunc_Tensor():
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
BlendFunc_Linear: OCP.BlendFunc.BlendFunc_SectionShape # value = <BlendFunc_SectionShape.BlendFunc_Linear: 3>
BlendFunc_Polynomial: OCP.BlendFunc.BlendFunc_SectionShape # value = <BlendFunc_SectionShape.BlendFunc_Polynomial: 2>
BlendFunc_QuasiAngular: OCP.BlendFunc.BlendFunc_SectionShape # value = <BlendFunc_SectionShape.BlendFunc_QuasiAngular: 1>
BlendFunc_Rational: OCP.BlendFunc.BlendFunc_SectionShape # value = <BlendFunc_SectionShape.BlendFunc_Rational: 0>
