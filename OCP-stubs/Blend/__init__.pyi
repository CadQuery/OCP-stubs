import OCP.Blend
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor2d
import OCP.GeomAbs
import OCP.math
import OCP.TColgp
import OCP.NCollection
import OCP.gp
import OCP.TColStd
__all__  = [
"Blend_AppFunction",
"Blend_CSFunction",
"Blend_CurvPointFuncInv",
"Blend_DecrochStatus",
"Blend_FuncInv",
"Blend_Function",
"Blend_Point",
"Blend_RstRstFunction",
"Blend_SequenceOfPoint",
"Blend_Status",
"Blend_SurfCurvFuncInv",
"Blend_SurfPointFuncInv",
"Blend_SurfRstFunction",
"Blend_Backward",
"Blend_DecrochBoth",
"Blend_DecrochRst1",
"Blend_DecrochRst2",
"Blend_NoDecroch",
"Blend_OK",
"Blend_OnRst1",
"Blend_OnRst12",
"Blend_OnRst2",
"Blend_SamePoints",
"Blend_StepTooLarge",
"Blend_StepTooSmall"
]
class Blend_AppFunction(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a blending surface between two surfaces, using a guide line. The vector <X> used in Value, Values and Derivatives methods has to be the vector of the parametric coordinates U1,V1, U2,V2, of the extremities of a section on the first and second surface.
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        Returns in the vector InfBound the lowest values allowed for each of the 4 variables. Returns in the vector SupBound the greatest values allowed for each of the 4 variables.
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
        Returns in the vector Tolerance the parametric tolerance for each of the 4 variables; Tol is the tolerance used in 3d space.

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
        Returns Standard_True if Sol is a zero of the function. Tol is the tolerance used in 3d space. The computation is made at the current value of the parameter on the guide line.
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
        returns the number of variables of the function.
        """
    def Parameter(self,P : Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def Pnt1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Pnt2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the first support.
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        None

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.
        """
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self,Param : float) -> None: 
        """
        Sets the value of the parameter along the guide line. This determines the plane in which the solution has to be found.

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.
        """
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class Blend_CSFunction(Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a blending surface between a surface and a curve, using a guide line. The vector <X> used in Value, Values and Derivatives methods may be the vector of the parametric coordinates U,V, W of the extremities of a section on the surface and the curve.
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        Returns in the vector InfBound the lowest values allowed for each of the 3 variables. Returns in the vector SupBound the greatest values allowed for each of the 3 variables.
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
        Returns in the vector Tolerance the parametric tolerance for each of the 3 variables; Tol is the tolerance used in 3d space.

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
        Returns Standard_True if Sol is a zero of the function. Tol is the tolerance used in 3d space. The computation is made at the current value of the parameter on the guide line.
        """
    def IsTangencyPoint(self) -> bool: 
        """
        Returns True when it is not possible to compute the tangent vectors at PointOnS and/or PointOnC.
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
        Returns 3 (default value). Can be redefined.
        """
    def Parameter(self,P : Blend_Point) -> float: 
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
        Returns the point on the curve.
        """
    def PointOnS(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the surface.
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        None

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.
        """
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Set(self,Param : float) -> None: 
        """
        Sets the value of the parameter along the guide line. This determines the plane in which the solution has to be found.

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.
        """
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    def Tangent(self,U : float,V : float,TgS : OCP.gp.gp_Vec,NormS : OCP.gp.gp_Vec) -> None: 
        """
        Returns the tangent vector at the section, at the beginning and the end of the section, and returns the normal (of the surfaces) at these points.
        """
    def Tangent2d(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the tangent vector at PointOnS, in the parametric space of the first surface.
        """
    def TangentOnC(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent vector at PointOnC, in 3d space.
        """
    def TangentOnS(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent vector at PointOnS, in 3d space.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class Blend_CurvPointFuncInv(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a blending surface between a surface and a curve, using a guide line. This function is used to find a solution on a done point of the curve. The vector <X> used in Value, Values and Derivatives methods has to be the vector of the parametric coordinates w, U, V where w is the parameter on the guide line, U,V are the parametric coordinates of a point on the partner surface.
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        Returns in the vector InfBound the lowest values allowed for each of the 3 variables. Returns in the vector SupBound the greatest values allowed for each of the 3 variables.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        Returns in the vector Tolerance the parametric tolerance for each of the 3 variables; Tol is the tolerance used in 3d space.
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
        Returns 3.
        """
    def Set(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Set the Point on which a solution has to be found.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class Blend_DecrochStatus():
    """
    None

    Members:

      Blend_NoDecroch

      Blend_DecrochRst1

      Blend_DecrochRst2

      Blend_DecrochBoth
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
    Blend_DecrochBoth: OCP.Blend.Blend_DecrochStatus # value = <Blend_DecrochStatus.Blend_DecrochBoth: 3>
    Blend_DecrochRst1: OCP.Blend.Blend_DecrochStatus # value = <Blend_DecrochStatus.Blend_DecrochRst1: 1>
    Blend_DecrochRst2: OCP.Blend.Blend_DecrochStatus # value = <Blend_DecrochStatus.Blend_DecrochRst2: 2>
    Blend_NoDecroch: OCP.Blend.Blend_DecrochStatus # value = <Blend_DecrochStatus.Blend_NoDecroch: 0>
    __entries: dict # value = {'Blend_NoDecroch': (<Blend_DecrochStatus.Blend_NoDecroch: 0>, None), 'Blend_DecrochRst1': (<Blend_DecrochStatus.Blend_DecrochRst1: 1>, None), 'Blend_DecrochRst2': (<Blend_DecrochStatus.Blend_DecrochRst2: 2>, None), 'Blend_DecrochBoth': (<Blend_DecrochStatus.Blend_DecrochBoth: 3>, None)}
    __members__: dict # value = {'Blend_NoDecroch': <Blend_DecrochStatus.Blend_NoDecroch: 0>, 'Blend_DecrochRst1': <Blend_DecrochStatus.Blend_DecrochRst1: 1>, 'Blend_DecrochRst2': <Blend_DecrochStatus.Blend_DecrochRst2: 2>, 'Blend_DecrochBoth': <Blend_DecrochStatus.Blend_DecrochBoth: 3>}
    pass
class Blend_FuncInv(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a blending surface between two surfaces, using a guide line. This function is used to find a solution on a restriction of one of the surface. The vector <X> used in Value, Values and Derivatives methods has to be the vector of the parametric coordinates t,w,U,V where t is the parameter on the curve on surface, w is the parameter on the guide line, U,V are the parametric coordinates of a point on the partner surface.
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        Returns in the vector InfBound the lowest values allowed for each of the 4 variables. Returns in the vector SupBound the greatest values allowed for each of the 4 variables.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        Returns in the vector Tolerance the parametric tolerance for each of the 4 variables; Tol is the tolerance used in 3d space.
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
    def Set(self,OnFirst : bool,COnSurf : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        Sets the CurveOnSurface on which a solution has to be found. If <OnFirst> is set to Standard_True, the curve will be on the first surface, otherwise the curve is on the second one.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class Blend_Function(Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a blending surface between two surfaces, using a guide line. The vector <X> used in Value, Values and Derivatives methods has to be the vector of the parametric coordinates U1,V1, U2,V2, of the extremities of a section on the first and second surface.
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        Returns in the vector InfBound the lowest values allowed for each of the 4 variables. Returns in the vector SupBound the greatest values allowed for each of the 4 variables.
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
        Returns in the vector Tolerance the parametric tolerance for each of the 4 variables; Tol is the tolerance used in 3d space.

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
    def Parameter(self,P : Blend_Point) -> float: 
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
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        None

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False
        """
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Set(self,Param : float) -> None: 
        """
        Sets the value of the parameter along the guide line. This determines the plane in which the solution has to be found.

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.
        """
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
    pass
class Blend_Point():
    """
    None
    """
    def IsTangencyPoint(self) -> bool: 
        """
        Returns Standard_True if it was not possible to compute the tangent vectors at PointOnS1 and/or PointOnS2.

        Returns Standard_True if it was not possible to compute the tangent vectors at PointOnS1 and/or PointOnS2.
        """
    def Parameter(self) -> float: 
        """
        None

        None
        """
    def ParameterOnC(self) -> float: 
        """
        None

        None
        """
    def ParameterOnC1(self) -> float: 
        """
        None

        None
        """
    def ParameterOnC2(self) -> float: 
        """
        None

        None
        """
    def ParametersOnS(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def ParametersOnS1(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def ParametersOnS2(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def PointOnC(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def PointOnC1(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def PointOnC2(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def PointOnS(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def PointOnS1(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def PointOnS2(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def SetParameter(self,Param : float) -> None: 
        """
        Changes parameter on existing point

        Changes parameter on existing point
        """
    @overload
    def SetValue(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,Tg1 : OCP.gp.gp_Vec,Tg2 : OCP.gp.gp_Vec,Tg12d : OCP.gp.gp_Vec2d,Tg22d : OCP.gp.gp_Vec2d) -> None: 
        """
        Set the values for a point on 2 surfaces, with tangents.

        Set the values for a point on 2 surfaces, without tangents.

        Set the values for a point on a surface and a curve, with tangents.

        Set the values for a point on a surface and a curve, without tangents.

        Creates a point on a surface and a curve on surface, with tangents.

        Creates a point on a surface and a curve on surface, without tangents.

        Creates a point on two curves on surfaces, with tangents.

        Creates a point on two curves on surfaces, without tangents.

        Creates a point on two curves.
        """
    @overload
    def SetValue(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,PC1 : float,PC2 : float,Tg1 : OCP.gp.gp_Vec,Tg2 : OCP.gp.gp_Vec,Tg12d : OCP.gp.gp_Vec2d,Tg22d : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def SetValue(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,PC1 : float,PC2 : float) -> None: ...
    @overload
    def SetValue(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float) -> None: ...
    @overload
    def SetValue(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,PC : float,Tg1 : OCP.gp.gp_Vec,Tg2 : OCP.gp.gp_Vec,Tg12d : OCP.gp.gp_Vec2d,Tg22d : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def SetValue(self,Pts : OCP.gp.gp_Pnt,Ptc : OCP.gp.gp_Pnt,Param : float,U : float,V : float,W : float,Tgs : OCP.gp.gp_Vec,Tgc : OCP.gp.gp_Vec,Tg2d : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def SetValue(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,PC1 : float,PC2 : float) -> None: ...
    @overload
    def SetValue(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,PC : float) -> None: ...
    @overload
    def SetValue(self,Pts : OCP.gp.gp_Pnt,Ptc : OCP.gp.gp_Pnt,Param : float,U : float,V : float,W : float) -> None: ...
    def Tangent2d(self) -> OCP.gp.gp_Vec2d: 
        """
        None

        None
        """
    def Tangent2dOnS1(self) -> OCP.gp.gp_Vec2d: 
        """
        None

        None
        """
    def Tangent2dOnS2(self) -> OCP.gp.gp_Vec2d: 
        """
        None

        None
        """
    def TangentOnC(self) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    def TangentOnC1(self) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    def TangentOnC2(self) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    def TangentOnS(self) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    def TangentOnS1(self) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    def TangentOnS2(self) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    @overload
    def __init__(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,PC : float,Tg1 : OCP.gp.gp_Vec,Tg2 : OCP.gp.gp_Vec,Tg12d : OCP.gp.gp_Vec2d,Tg22d : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def __init__(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,Tg1 : OCP.gp.gp_Vec,Tg2 : OCP.gp.gp_Vec,Tg12d : OCP.gp.gp_Vec2d,Tg22d : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def __init__(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,PC1 : float,PC2 : float,Tg1 : OCP.gp.gp_Vec,Tg2 : OCP.gp.gp_Vec,Tg12d : OCP.gp.gp_Vec2d,Tg22d : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def __init__(self,Pts : OCP.gp.gp_Pnt,Ptc : OCP.gp.gp_Pnt,Param : float,U : float,V : float,W : float,Tgs : OCP.gp.gp_Vec,Tgc : OCP.gp.gp_Vec,Tg2d : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def __init__(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,PC : float) -> None: ...
    @overload
    def __init__(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float,PC1 : float,PC2 : float) -> None: ...
    @overload
    def __init__(self,Pts : OCP.gp.gp_Pnt,Ptc : OCP.gp.gp_Pnt,Param : float,U : float,V : float,W : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,Param : float,U1 : float,V1 : float,U2 : float,V2 : float) -> None: ...
    pass
class Blend_RstRstFunction(Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a blending surface between a surface and a pcurve on an other Surface, using a guide line. The vector <X> used in Value, Values and Derivatives methods may be the vector of the parametric coordinates U,V, W of the extremities of a section on the surface and the curve.
    """
    def Decroch(self,Sol : OCP.math.math_Vector,NRst1 : OCP.gp.gp_Vec,TgRst1 : OCP.gp.gp_Vec,NRst2 : OCP.gp.gp_Vec,TgRst2 : OCP.gp.gp_Vec) -> Blend_DecrochStatus: 
        """
        Enables to implement a criterion of decrochage specific to the function. Warning: Can be called without previous call of issolution but the values calculated can be senseless.
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        Returns in the vector InfBound the lowest values allowed for each variables. Returns in the vector SupBound the greatest values allowed for each of the 3 variables.
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
        Returns in the vector Tolerance the parametric tolerance for each variable; Tol is the tolerance used in 3d space.

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
        Returns Standard_True if Sol is a zero of the function. Tol is the tolerance used in 3d space. The computation is made at the current value of the parameter on the guide line.
        """
    def IsTangencyPoint(self) -> bool: 
        """
        Returns True when it is not possible to compute the tangent vectors at PointOnS and/or PointOnRst.
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
        Returns 2 (default value). Can be redefined.
        """
    def Parameter(self,P : Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def ParameterOnRst1(self) -> float: 
        """
        Returns parameter of the point on the curve.
        """
    def ParameterOnRst2(self) -> float: 
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
    def Pnt2dOnRst1(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns U,V coordinates of the point on the surface.
        """
    def Pnt2dOnRst2(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns U,V coordinates of the point on the curve on surface.
        """
    def PointOnRst1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the surface.
        """
    def PointOnRst2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the curve.
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        None

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.
        """
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Set(self,Param : float) -> None: 
        """
        Sets the value of the parameter along the guide line. This determines the plane in which the solution has to be found.

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.
        """
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    def Tangent2dOnRst1(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the tangent vector at PointOnS, in the parametric space of the first surface.
        """
    def Tangent2dOnRst2(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the tangent vector at PointOnRst, in the parametric space of the second surface.
        """
    def TangentOnRst1(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent vector at PointOnS, in 3d space.
        """
    def TangentOnRst2(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent vector at PointOnC, in 3d space.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class Blend_SequenceOfPoint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Blend_SequenceOfPoint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Blend_Point) -> None: ...
    def Assign(self,theOther : Blend_SequenceOfPoint) -> Blend_SequenceOfPoint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Blend_Point: 
        """
        First item access
        """
    def ChangeLast(self) -> Blend_Point: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Blend_Point: 
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
    def First(self) -> Blend_Point: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Blend_SequenceOfPoint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Blend_Point) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Blend_Point) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Blend_SequenceOfPoint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Blend_Point: 
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
    def Prepend(self,theSeq : Blend_SequenceOfPoint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Blend_Point) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Blend_Point) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Blend_SequenceOfPoint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Blend_Point: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Blend_SequenceOfPoint) -> None: ...
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
class Blend_Status():
    """
    None

    Members:

      Blend_StepTooLarge

      Blend_StepTooSmall

      Blend_Backward

      Blend_SamePoints

      Blend_OnRst1

      Blend_OnRst2

      Blend_OnRst12

      Blend_OK
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
    Blend_Backward: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_Backward: 2>
    Blend_OK: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_OK: 7>
    Blend_OnRst1: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_OnRst1: 4>
    Blend_OnRst12: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_OnRst12: 6>
    Blend_OnRst2: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_OnRst2: 5>
    Blend_SamePoints: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_SamePoints: 3>
    Blend_StepTooLarge: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_StepTooLarge: 0>
    Blend_StepTooSmall: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_StepTooSmall: 1>
    __entries: dict # value = {'Blend_StepTooLarge': (<Blend_Status.Blend_StepTooLarge: 0>, None), 'Blend_StepTooSmall': (<Blend_Status.Blend_StepTooSmall: 1>, None), 'Blend_Backward': (<Blend_Status.Blend_Backward: 2>, None), 'Blend_SamePoints': (<Blend_Status.Blend_SamePoints: 3>, None), 'Blend_OnRst1': (<Blend_Status.Blend_OnRst1: 4>, None), 'Blend_OnRst2': (<Blend_Status.Blend_OnRst2: 5>, None), 'Blend_OnRst12': (<Blend_Status.Blend_OnRst12: 6>, None), 'Blend_OK': (<Blend_Status.Blend_OK: 7>, None)}
    __members__: dict # value = {'Blend_StepTooLarge': <Blend_Status.Blend_StepTooLarge: 0>, 'Blend_StepTooSmall': <Blend_Status.Blend_StepTooSmall: 1>, 'Blend_Backward': <Blend_Status.Blend_Backward: 2>, 'Blend_SamePoints': <Blend_Status.Blend_SamePoints: 3>, 'Blend_OnRst1': <Blend_Status.Blend_OnRst1: 4>, 'Blend_OnRst2': <Blend_Status.Blend_OnRst2: 5>, 'Blend_OnRst12': <Blend_Status.Blend_OnRst12: 6>, 'Blend_OK': <Blend_Status.Blend_OK: 7>}
    pass
class Blend_SurfCurvFuncInv(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a blending surface between a surface and a curve, using a guide line. This function is used to find a solution on a done restriction of the surface.
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        Returns in the vector InfBound the lowest values allowed for each of the 3 variables. Returns in the vector SupBound the greatest values allowed for each of the 3 variables.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        Returns in the vector Tolerance the parametric tolerance for each of the 3 variables; Tol is the tolerance used in 3d space.
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
        Returns 3.
        """
    def Set(self,Rst : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        Set the Point on which a solution has to be found.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class Blend_SurfPointFuncInv(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a blending surface between a surface and a curve, using a guide line. This function is used to find a solution on a done point of the curve.
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        Returns in the vector InfBound the lowest values allowed for each of the 3 variables. Returns in the vector SupBound the greatest values allowed for each of the 3 variables.
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def GetTolerance(self,Tolerance : OCP.math.math_Vector,Tol : float) -> None: 
        """
        Returns in the vector Tolerance the parametric tolerance for each of the 3 variables; Tol is the tolerance used in 3d space.
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
        Returns 3.
        """
    def Set(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Set the Point on which a solution has to be found.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
class Blend_SurfRstFunction(Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Deferred class for a function used to compute a blending surface between a surface and a pcurve on an other Surface, using a guide line. The vector <X> used in Value, Values and Derivatives methods may be the vector of the parametric coordinates U,V, W of the extremities of a section on the surface and the curve.
    """
    def Decroch(self,Sol : OCP.math.math_Vector,NS : OCP.gp.gp_Vec,TgS : OCP.gp.gp_Vec) -> bool: 
        """
        Enables implementation of a criterion of decrochage specific to the function.
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <D> of the derivatives for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def GetBounds(self,InfBound : OCP.math.math_Vector,SupBound : OCP.math.math_Vector) -> None: 
        """
        Returns in the vector InfBound the lowest values allowed for each variables. Returns in the vector SupBound the greatest values allowed for each of the 3 variables.
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
        Returns in the vector Tolerance the parametric tolerance for each variable; Tol is the tolerance used in 3d space.

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
        Returns Standard_True if Sol is a zero of the function. Tol is the tolerance used in 3d space. The computation is made at the current value of the parameter on the guide line.
        """
    def IsTangencyPoint(self) -> bool: 
        """
        Returns True when it is not possible to compute the tangent vectors at PointOnS and/or PointOnRst.
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
        Returns 3 (default value). Can be redefined.
        """
    def Parameter(self,P : Blend_Point) -> float: 
        """
        Returns the parameter of the point P. Used to impose the parameters in the approximation.
        """
    def ParameterOnRst(self) -> float: 
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
    def Pnt2dOnRst(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns U,V coordinates of the point on the curve on surface.
        """
    def Pnt2dOnS(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns U,V coordinates of the point on the surface.
        """
    def PointOnRst(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the curve.
        """
    def PointOnS(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the surface.
        """
    def Resolution(self,IC2d : int,Tol : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        None
        """
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,P : Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Set(self,Param : float) -> None: 
        """
        Sets the value of the parameter along the guide line. This determines the plane in which the solution has to be found.

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.
        """
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    def Tangent2dOnRst(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the tangent vector at PointOnRst, in the parametric space of the second surface.
        """
    def Tangent2dOnS(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the tangent vector at PointOnS, in the parametric space of the first surface.
        """
    def TangentOnRst(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent vector at PointOnC, in 3d space.
        """
    def TangentOnS(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent vector at PointOnS, in 3d space.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    pass
Blend_Backward: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_Backward: 2>
Blend_DecrochBoth: OCP.Blend.Blend_DecrochStatus # value = <Blend_DecrochStatus.Blend_DecrochBoth: 3>
Blend_DecrochRst1: OCP.Blend.Blend_DecrochStatus # value = <Blend_DecrochStatus.Blend_DecrochRst1: 1>
Blend_DecrochRst2: OCP.Blend.Blend_DecrochStatus # value = <Blend_DecrochStatus.Blend_DecrochRst2: 2>
Blend_NoDecroch: OCP.Blend.Blend_DecrochStatus # value = <Blend_DecrochStatus.Blend_NoDecroch: 0>
Blend_OK: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_OK: 7>
Blend_OnRst1: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_OnRst1: 4>
Blend_OnRst12: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_OnRst12: 6>
Blend_OnRst2: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_OnRst2: 5>
Blend_SamePoints: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_SamePoints: 3>
Blend_StepTooLarge: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_StepTooLarge: 0>
Blend_StepTooSmall: OCP.Blend.Blend_Status # value = <Blend_Status.Blend_StepTooSmall: 1>
