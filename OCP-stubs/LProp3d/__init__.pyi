import OCP.LProp3d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.gp
__all__  = [
"LProp3d_CLProps",
"LProp3d_CurveTool",
"LProp3d_SLProps",
"LProp3d_SurfaceTool"
]
class LProp3d_CLProps():
    """
    None
    """
    def CentreOfCurvature(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns the centre of curvature <P>.
        """
    def Curvature(self) -> float: 
        """
        Returns the curvature.
        """
    def D1(self) -> OCP.gp.gp_Vec: 
        """
        Returns the first derivative. The derivative is computed if it has not been yet.
        """
    def D2(self) -> OCP.gp.gp_Vec: 
        """
        Returns the second derivative. The derivative is computed if it has not been yet.
        """
    def D3(self) -> OCP.gp.gp_Vec: 
        """
        Returns the third derivative. The derivative is computed if it has not been yet.
        """
    def IsTangentDefined(self) -> bool: 
        """
        Returns True if the tangent is defined. For example, the tangent is not defined if the three first derivatives are all null.
        """
    def Normal(self,N : OCP.gp.gp_Dir) -> None: 
        """
        Returns the normal direction <N>.
        """
    def SetCurve(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> None: 
        """
        Initializes the local properties of the curve for the new curve.
        """
    def SetParameter(self,U : float) -> None: 
        """
        Initializes the local properties of the curve for the parameter value <U>.
        """
    def Tangent(self,D : OCP.gp.gp_Dir) -> None: 
        """
        output the tangent direction <D>
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point.
        """
    @overload
    def __init__(self,N : int,Resolution : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,N : int,Resolution : float) -> None: ...
    @overload
    def __init__(self,C : OCP.Adaptor3d.Adaptor3d_Curve,N : int,Resolution : float) -> None: ...
    pass
class LProp3d_CurveTool():
    """
    None
    """
    @staticmethod
    def Continuity_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> int: 
        """
        returns the order of continuity of the HCurve <C>. returns 1 : first derivative only is computable returns 2 : first and second derivative only are computable. returns 3 : first, second and third are computable.
        """
    @staticmethod
    def D1_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P> and first derivative <V1> of parameter <U> on the HCurve <C>.
        """
    @staticmethod
    def D2_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P>, the first derivative <V1> and second derivative <V2> of parameter <U> on the HCurve <C>.
        """
    @staticmethod
    def D3_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P>, the first derivative <V1>, the second derivative <V2> and third derivative <V3> of parameter <U> on the HCurve <C>.
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> float: 
        """
        returns the first parameter bound of the HCurve.
        """
    @staticmethod
    def LastParameter_s(C : OCP.Adaptor3d.Adaptor3d_Curve) -> float: 
        """
        returns the last parameter bound of the HCurve. FirstParameter must be less than LastParamenter.
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor3d.Adaptor3d_Curve,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point <P> of parameter <U> on the HCurve <C>.
        """
    def __init__(self) -> None: ...
    pass
class LProp3d_SLProps():
    """
    None
    """
    def CurvatureDirections(self,MaxD : OCP.gp.gp_Dir,MinD : OCP.gp.gp_Dir) -> None: 
        """
        Returns the direction of the maximum and minimum curvature <MaxD> and <MinD>
        """
    def D1U(self) -> OCP.gp.gp_Vec: 
        """
        Returns the first U derivative. The derivative is computed if it has not been yet.
        """
    def D1V(self) -> OCP.gp.gp_Vec: 
        """
        Returns the first V derivative. The derivative is computed if it has not been yet.
        """
    def D2U(self) -> OCP.gp.gp_Vec: 
        """
        Returns the second U derivatives The derivative is computed if it has not been yet.
        """
    def D2V(self) -> OCP.gp.gp_Vec: 
        """
        Returns the second V derivative. The derivative is computed if it has not been yet.
        """
    def DUV(self) -> OCP.gp.gp_Vec: 
        """
        Returns the second UV cross-derivative. The derivative is computed if it has not been yet.
        """
    def GaussianCurvature(self) -> float: 
        """
        Returns the Gaussian curvature
        """
    def IsCurvatureDefined(self) -> bool: 
        """
        returns True if the curvature is defined.
        """
    def IsNormalDefined(self) -> bool: 
        """
        Tells if the normal is defined.
        """
    def IsTangentUDefined(self) -> bool: 
        """
        returns True if the U tangent is defined. For example, the tangent is not defined if the two first U derivatives are null.
        """
    def IsTangentVDefined(self) -> bool: 
        """
        returns if the V tangent is defined. For example, the tangent is not defined if the two first V derivatives are null.
        """
    def IsUmbilic(self) -> bool: 
        """
        returns True if the point is umbilic (i.e. if the curvature is constant).
        """
    def MaxCurvature(self) -> float: 
        """
        Returns the maximum curvature
        """
    def MeanCurvature(self) -> float: 
        """
        Returns the mean curvature.
        """
    def MinCurvature(self) -> float: 
        """
        Returns the minimum curvature
        """
    def Normal(self) -> OCP.gp.gp_Dir: 
        """
        Returns the normal direction.
        """
    def SetParameters(self,U : float,V : float) -> None: 
        """
        Initializes the local properties of the surface S for the new parameter values (<U>, <V>).
        """
    def SetSurface(self,S : OCP.Adaptor3d.Adaptor3d_Surface) -> None: 
        """
        Initializes the local properties of the surface S for the new surface.
        """
    def TangentU(self,D : OCP.gp.gp_Dir) -> None: 
        """
        Returns the tangent direction <D> on the iso-V.
        """
    def TangentV(self,D : OCP.gp.gp_Dir) -> None: 
        """
        Returns the tangent direction <D> on the iso-V.
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point.
        """
    @overload
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_Surface,N : int,Resolution : float) -> None: ...
    @overload
    def __init__(self,N : int,Resolution : float) -> None: ...
    @overload
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_Surface,U : float,V : float,N : int,Resolution : float) -> None: ...
    pass
class LProp3d_SurfaceTool():
    """
    None
    """
    @staticmethod
    def Bounds_s(S : OCP.Adaptor3d.Adaptor3d_Surface) -> Tuple[float, float, float, float]: 
        """
        returns the bounds of the HSurface.
        """
    @staticmethod
    def Continuity_s(S : OCP.Adaptor3d.Adaptor3d_Surface) -> int: 
        """
        returns the order of continuity of the HSurface <S>. returns 1 : first derivative only is computable returns 2 : first and second derivative only are computable.
        """
    @staticmethod
    def D1_s(S : OCP.Adaptor3d.Adaptor3d_Surface,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P> and first derivative <D1*> of parameter <U> and <V> on the HSurface <S>.
        """
    @staticmethod
    def D2_s(S : OCP.Adaptor3d.Adaptor3d_Surface,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,DUV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point <P>, the first derivative <D1*> and second derivative <D2*> of parameter <U> and <V> on the HSurface <S>.
        """
    @staticmethod
    def DN_s(S : OCP.Adaptor3d.Adaptor3d_Surface,U : float,V : float,IU : int,IV : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @staticmethod
    def Value_s(S : OCP.Adaptor3d.Adaptor3d_Surface,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point <P> of parameter <U> and <V> on the HSurface <S>.
        """
    def __init__(self) -> None: ...
    pass
