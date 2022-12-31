import OCP.CSLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.math
import OCP.TColgp
import OCP.TColStd
import OCP.gp
__all__  = [
"CSLib",
"CSLib_Class2d",
"CSLib_DerivativeStatus",
"CSLib_NormalPolyDef",
"CSLib_NormalStatus",
"CSLib_D1IsNull",
"CSLib_D1NIsNull",
"CSLib_D1NuIsNull",
"CSLib_D1NuIsParallelD1Nv",
"CSLib_D1NuNvRatioIsNull",
"CSLib_D1NvIsNull",
"CSLib_D1NvNuRatioIsNull",
"CSLib_D1uD1vRatioIsNull",
"CSLib_D1uIsNull",
"CSLib_D1uIsParallelD1v",
"CSLib_D1vD1uRatioIsNull",
"CSLib_D1vIsNull",
"CSLib_Defined",
"CSLib_Done",
"CSLib_InfinityOfSolutions",
"CSLib_Singular"
]
class CSLib():
    """
    This package implements functions for basis geometric computation on curves and surfaces. The tolerance criterions used in this package are Resolution from package gp and RealEpsilon from class Real of package Standard.
    """
    @staticmethod
    @overload
    def DNNUV_s(Nu : int,Nv : int,DerSurf1 : OCP.TColgp.TColgp_Array2OfVec,DerSurf2 : OCP.TColgp.TColgp_Array2OfVec) -> OCP.gp.gp_Vec: 
        """
        -- Computes the derivative of order Nu in the -- direction U and Nv in the direction V of the not -- normalized normal vector at the point P(U,V) The array DerSurf contain the derivative (i,j) of the surface for i=0,Nu+1 ; j=0,Nv+1

        Computes the derivatives of order Nu in the direction Nu and Nv in the direction Nv of the not normalized vector N(u,v) = dS1/du * dS2/dv (cases where we use an osculating surface) DerSurf1 are the derivatives of S1
        """
    @staticmethod
    @overload
    def DNNUV_s(Nu : int,Nv : int,DerSurf : OCP.TColgp.TColgp_Array2OfVec) -> OCP.gp.gp_Vec: ...
    @staticmethod
    def DNNormal_s(Nu : int,Nv : int,DerNUV : OCP.TColgp.TColgp_Array2OfVec,Iduref : int=0,Idvref : int=0) -> OCP.gp.gp_Vec: 
        """
        -- Computes the derivative of order Nu in the -- direction U and Nv in the direction V of the normalized normal vector at the point P(U,V) array DerNUV contain the derivative (i+Iduref,j+Idvref) of D1U ^ D1V for i=0,Nu ; j=0,Nv Iduref and Idvref correspond to a derivative of D1U ^ D1V which can be used to compute the normalized normal vector. In the regular cases , Iduref=Idvref=0.
        """
    @staticmethod
    @overload
    def Normal_s(D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,MagTol : float,theStatus : CSLib_NormalStatus,Normal : OCP.gp.gp_Dir) -> None: 
        """
        The following functions computes the normal to a surface inherits FunctionWithDerivative from math

        Computes the normal direction of a surface as the cross product between D1U and D1V.

        If there is a singularity on the surface the previous method cannot compute the local normal. This method computes an approached normal direction of a surface. It does a limited development and needs the second derivatives on the surface as input data. It computes the normal as follow : N(u, v) = D1U ^ D1V N(u0+du,v0+dv) = N0 + DN/du(u0,v0) * du + DN/dv(u0,v0) * dv + Eps with Eps->0 so we can have the equivalence N ~ dN/du + dN/dv. DNu = ||DN/du|| and DNv = ||DN/dv||

        find the first order k0 of deriviative of NUV where: foreach order < k0 all the derivatives of NUV are null all the derivatives of NUV corresponding to the order k0 are collinear and have the same sens. In this case, normal at U,V is unique.
        """
    @staticmethod
    @overload
    def Normal_s(MaxOrder : int,DerNUV : OCP.TColgp.TColgp_Array2OfVec,MagTol : float,U : float,V : float,Umin : float,Umax : float,Vmin : float,Vmax : float,theStatus : CSLib_NormalStatus,Normal : OCP.gp.gp_Dir) -> Tuple[int, int]: ...
    @staticmethod
    @overload
    def Normal_s(D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,SinTol : float,theStatus : CSLib_NormalStatus,Normal : OCP.gp.gp_Dir) -> Tuple[bool]: ...
    @staticmethod
    @overload
    def Normal_s(D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,SinTol : float,theStatus : CSLib_DerivativeStatus,Normal : OCP.gp.gp_Dir) -> None: ...
    def __init__(self) -> None: ...
    pass
class CSLib_Class2d():
    """
    *** Class2d : Low level algorithm for 2d classification this class was moved from package BRepTopAdaptor
    """
    def InternalSiDans(self,X : float,Y : float) -> int: 
        """
        None
        """
    def InternalSiDansOuOn(self,X : float,Y : float) -> int: 
        """
        None
        """
    def SiDans(self,P : OCP.gp.gp_Pnt2d) -> int: 
        """
        None
        """
    def SiDans_OnMode(self,P : OCP.gp.gp_Pnt2d,Tol : float) -> int: 
        """
        None
        """
    @overload
    def __init__(self,thePnts2d : OCP.TColgp.TColgp_SequenceOfPnt2d,theTolU : float,theTolV : float,theUMin : float,theVMin : float,theUMax : float,theVMax : float) -> None: ...
    @overload
    def __init__(self,thePnts2d : OCP.TColgp.TColgp_Array1OfPnt2d,theTolU : float,theTolV : float,theUMin : float,theVMin : float,theUMax : float,theVMax : float) -> None: ...
    pass
class CSLib_DerivativeStatus():
    """
    D1uIsNull : ||D1U|| <= Resolution

    Members:

      CSLib_Done

      CSLib_D1uIsNull

      CSLib_D1vIsNull

      CSLib_D1IsNull

      CSLib_D1uD1vRatioIsNull

      CSLib_D1vD1uRatioIsNull

      CSLib_D1uIsParallelD1v
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
    CSLib_D1IsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1IsNull: 3>
    CSLib_D1uD1vRatioIsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1uD1vRatioIsNull: 4>
    CSLib_D1uIsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1uIsNull: 1>
    CSLib_D1uIsParallelD1v: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1uIsParallelD1v: 6>
    CSLib_D1vD1uRatioIsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1vD1uRatioIsNull: 5>
    CSLib_D1vIsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1vIsNull: 2>
    CSLib_Done: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_Done: 0>
    __entries: dict # value = {'CSLib_Done': (<CSLib_DerivativeStatus.CSLib_Done: 0>, None), 'CSLib_D1uIsNull': (<CSLib_DerivativeStatus.CSLib_D1uIsNull: 1>, None), 'CSLib_D1vIsNull': (<CSLib_DerivativeStatus.CSLib_D1vIsNull: 2>, None), 'CSLib_D1IsNull': (<CSLib_DerivativeStatus.CSLib_D1IsNull: 3>, None), 'CSLib_D1uD1vRatioIsNull': (<CSLib_DerivativeStatus.CSLib_D1uD1vRatioIsNull: 4>, None), 'CSLib_D1vD1uRatioIsNull': (<CSLib_DerivativeStatus.CSLib_D1vD1uRatioIsNull: 5>, None), 'CSLib_D1uIsParallelD1v': (<CSLib_DerivativeStatus.CSLib_D1uIsParallelD1v: 6>, None)}
    __members__: dict # value = {'CSLib_Done': <CSLib_DerivativeStatus.CSLib_Done: 0>, 'CSLib_D1uIsNull': <CSLib_DerivativeStatus.CSLib_D1uIsNull: 1>, 'CSLib_D1vIsNull': <CSLib_DerivativeStatus.CSLib_D1vIsNull: 2>, 'CSLib_D1IsNull': <CSLib_DerivativeStatus.CSLib_D1IsNull: 3>, 'CSLib_D1uD1vRatioIsNull': <CSLib_DerivativeStatus.CSLib_D1uD1vRatioIsNull: 4>, 'CSLib_D1vD1uRatioIsNull': <CSLib_DerivativeStatus.CSLib_D1vD1uRatioIsNull: 5>, 'CSLib_D1uIsParallelD1v': <CSLib_DerivativeStatus.CSLib_D1uIsParallelD1v: 6>}
    pass
class CSLib_NormalPolyDef(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
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
    def __init__(self,k0 : int,li : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    pass
class CSLib_NormalStatus():
    """
    if N is the normal

    Members:

      CSLib_Singular

      CSLib_Defined

      CSLib_InfinityOfSolutions

      CSLib_D1NuIsNull

      CSLib_D1NvIsNull

      CSLib_D1NIsNull

      CSLib_D1NuNvRatioIsNull

      CSLib_D1NvNuRatioIsNull

      CSLib_D1NuIsParallelD1Nv
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
    CSLib_D1NIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NIsNull: 5>
    CSLib_D1NuIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NuIsNull: 3>
    CSLib_D1NuIsParallelD1Nv: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NuIsParallelD1Nv: 8>
    CSLib_D1NuNvRatioIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NuNvRatioIsNull: 6>
    CSLib_D1NvIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NvIsNull: 4>
    CSLib_D1NvNuRatioIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NvNuRatioIsNull: 7>
    CSLib_Defined: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_Defined: 1>
    CSLib_InfinityOfSolutions: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_InfinityOfSolutions: 2>
    CSLib_Singular: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_Singular: 0>
    __entries: dict # value = {'CSLib_Singular': (<CSLib_NormalStatus.CSLib_Singular: 0>, None), 'CSLib_Defined': (<CSLib_NormalStatus.CSLib_Defined: 1>, None), 'CSLib_InfinityOfSolutions': (<CSLib_NormalStatus.CSLib_InfinityOfSolutions: 2>, None), 'CSLib_D1NuIsNull': (<CSLib_NormalStatus.CSLib_D1NuIsNull: 3>, None), 'CSLib_D1NvIsNull': (<CSLib_NormalStatus.CSLib_D1NvIsNull: 4>, None), 'CSLib_D1NIsNull': (<CSLib_NormalStatus.CSLib_D1NIsNull: 5>, None), 'CSLib_D1NuNvRatioIsNull': (<CSLib_NormalStatus.CSLib_D1NuNvRatioIsNull: 6>, None), 'CSLib_D1NvNuRatioIsNull': (<CSLib_NormalStatus.CSLib_D1NvNuRatioIsNull: 7>, None), 'CSLib_D1NuIsParallelD1Nv': (<CSLib_NormalStatus.CSLib_D1NuIsParallelD1Nv: 8>, None)}
    __members__: dict # value = {'CSLib_Singular': <CSLib_NormalStatus.CSLib_Singular: 0>, 'CSLib_Defined': <CSLib_NormalStatus.CSLib_Defined: 1>, 'CSLib_InfinityOfSolutions': <CSLib_NormalStatus.CSLib_InfinityOfSolutions: 2>, 'CSLib_D1NuIsNull': <CSLib_NormalStatus.CSLib_D1NuIsNull: 3>, 'CSLib_D1NvIsNull': <CSLib_NormalStatus.CSLib_D1NvIsNull: 4>, 'CSLib_D1NIsNull': <CSLib_NormalStatus.CSLib_D1NIsNull: 5>, 'CSLib_D1NuNvRatioIsNull': <CSLib_NormalStatus.CSLib_D1NuNvRatioIsNull: 6>, 'CSLib_D1NvNuRatioIsNull': <CSLib_NormalStatus.CSLib_D1NvNuRatioIsNull: 7>, 'CSLib_D1NuIsParallelD1Nv': <CSLib_NormalStatus.CSLib_D1NuIsParallelD1Nv: 8>}
    pass
CSLib_D1IsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1IsNull: 3>
CSLib_D1NIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NIsNull: 5>
CSLib_D1NuIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NuIsNull: 3>
CSLib_D1NuIsParallelD1Nv: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NuIsParallelD1Nv: 8>
CSLib_D1NuNvRatioIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NuNvRatioIsNull: 6>
CSLib_D1NvIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NvIsNull: 4>
CSLib_D1NvNuRatioIsNull: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_D1NvNuRatioIsNull: 7>
CSLib_D1uD1vRatioIsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1uD1vRatioIsNull: 4>
CSLib_D1uIsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1uIsNull: 1>
CSLib_D1uIsParallelD1v: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1uIsParallelD1v: 6>
CSLib_D1vD1uRatioIsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1vD1uRatioIsNull: 5>
CSLib_D1vIsNull: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_D1vIsNull: 2>
CSLib_Defined: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_Defined: 1>
CSLib_Done: OCP.CSLib.CSLib_DerivativeStatus # value = <CSLib_DerivativeStatus.CSLib_Done: 0>
CSLib_InfinityOfSolutions: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_InfinityOfSolutions: 2>
CSLib_Singular: OCP.CSLib.CSLib_NormalStatus # value = <CSLib_NormalStatus.CSLib_Singular: 0>
