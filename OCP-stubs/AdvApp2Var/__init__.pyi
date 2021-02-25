import OCP.AdvApp2Var
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import io
import OCP.NCollection
import OCP.AdvApprox
import OCP.GeomAbs
import OCP.gp
import OCP.Geom
import OCP.TColgp
import OCP.Standard
__all__  = [
"AdvApp2Var_ApproxAFunc2Var",
"AdvApp2Var_ApproxF2var",
"AdvApp2Var_Context",
"AdvApp2Var_Criterion",
"AdvApp2Var_CriterionRepartition",
"AdvApp2Var_CriterionType",
"AdvApp2Var_Data",
"AdvApp2Var_EvaluatorFunc2Var",
"AdvApp2Var_Framework",
"AdvApp2Var_Iso",
"AdvApp2Var_MathBase",
"AdvApp2Var_Network",
"AdvApp2Var_Node",
"AdvApp2Var_Patch",
"AdvApp2Var_SequenceOfNode",
"AdvApp2Var_SequenceOfPatch",
"AdvApp2Var_SequenceOfStrip",
"AdvApp2Var_Strip",
"AdvApp2Var_SysBase",
"Namelist",
"Vardesc",
"alist",
"cilist",
"cllist",
"complex",
"doublecomplex",
"icilist",
"inlist",
"maovpar_1_",
"maovpch_1_",
"mdnombr_1_",
"minombr_1_",
"mlgdrtl_1_",
"mmapgs0_1_",
"mmapgs1_1_",
"mmapgs2_1_",
"mmapgss_1_",
"mmcmcnp_1_",
"mmjcobi_1_",
"olist",
"AdvApp2Var_Absolute",
"AdvApp2Var_Incremental",
"AdvApp2Var_Regular",
"AdvApp2Var_Relative"
]
class AdvApp2Var_ApproxAFunc2Var():
    """
    Perform the approximation of <Func> F(U,V) Arguments are : Num1DSS, Num2DSS, Num3DSS :The numbers of 1,2,3 dimensional subspaces OneDTol, TwoDTol, ThreeDTol: The tolerance of approximation in each subspaces OneDTolFr, TwoDTolFr, ThreeDTolFr: The tolerance of approximation on the boundarys in each subspaces [FirstInU, LastInU]: The Bounds in U of the Approximation [FirstInV, LastInV]: The Bounds in V of the Approximation FavorIso : Give preference to extract u-iso or v-iso on F(U,V) This can be usefull to optimize the <Func> methode ContInU, ContInV : Continuity waiting in u and v PrecisCode : Precision on approximation's error mesurement 1 : Fast computation and average precision 2 : Average computation and good precision 3 : Slow computation and very good precision MaxDegInU : Maximum u-degree waiting in U MaxDegInV : Maximum u-degree waiting in V Warning: MaxDegInU (resp. MaxDegInV) must be >= 2*iu (resp. iv) + 1, where iu (resp. iv) = 0 if ContInU (resp. ContInV) = GeomAbs_C0, = 1 if = GeomAbs_C1, = 2 if = GeomAbs_C2. MaxPatch : Maximun number of Patch waiting number of Patch is number of u span * number of v span Func : The external method to evaluate F(U,V) Crit : To (re)defined condition of convergence UChoice, VChoice : To define the way in U (or V) Knot insertion Warning: for the moment, the result is a 3D Surface so Num1DSS and Num2DSS must be equals to 0 and Num3DSS must be equal to 1. Warning: the Function of type EvaluatorFunc2Var from Approx must be a subclass of AdvApp2Var_EvaluatorFunc2Var
    """
    @overload
    def AverageError(self,Dimension : int,Index : int) -> float: 
        """
        returns the average errors

        returns the average error of the BSplineSurface of range Index
        """
    @overload
    def AverageError(self,Dimension : int) -> OCP.TColStd.TColStd_HArray1OfReal: ...
    def CritError(self,Dimension : int,Index : int) -> float: 
        """
        None
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o informations on the current state of the object.
        """
    def HasResult(self) -> bool: 
        """
        True if the approximation did come out with a result that is not NECESSARELY within the required tolerance or a result that is not recognized with the wished continuities

        True if the approximation did come out with a result that is not NECESSARELY within the required tolerance or a result that is not recognized with the wished continuities
        """
    def IsDone(self) -> bool: 
        """
        True if the approximation succeeded within the imposed tolerances and the wished continuities

        True if the approximation succeeded within the imposed tolerances and the wished continuities
        """
    @overload
    def MaxError(self,Dimension : int,Index : int) -> float: 
        """
        returns the errors max

        returns the error max of the BSplineSurface of range Index
        """
    @overload
    def MaxError(self,Dimension : int) -> OCP.TColStd.TColStd_HArray1OfReal: ...
    def NumSubSpaces(self,Dimension : int) -> int: 
        """
        None

        None
        """
    @overload
    def Surface(self,Index : int) -> OCP.Geom.Geom_BSplineSurface: 
        """
        returns the BSplineSurface of range Index

        returns the BSplineSurface of range Index
        """
    @overload
    def Surface(self,SSPIndex : int) -> OCP.Geom.Geom_BSplineSurface: ...
    def UDegree(self) -> int: 
        """
        None

        None
        """
    @overload
    def UFrontError(self,Dimension : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        returns the errors max on UFrontiers Warning: Dimension must be equal to 3.

        returns the error max of the BSplineSurface of range Index on a UFrontier
        """
    @overload
    def UFrontError(self,Dimension : int,Index : int) -> float: ...
    def VDegree(self) -> int: 
        """
        None

        None
        """
    @overload
    def VFrontError(self,Dimension : int,Index : int) -> float: 
        """
        returns the errors max on VFrontiers Warning: Dimension must be equal to 3.

        returns the error max of the BSplineSurface of range Index on a VFrontier
        """
    @overload
    def VFrontError(self,Dimension : int) -> OCP.TColStd.TColStd_HArray1OfReal: ...
    @overload
    def __init__(self,Num1DSS : int,Num2DSS : int,Num3DSS : int,OneDTol : OCP.TColStd.TColStd_HArray1OfReal,TwoDTol : OCP.TColStd.TColStd_HArray1OfReal,ThreeDTol : OCP.TColStd.TColStd_HArray1OfReal,OneDTolFr : OCP.TColStd.TColStd_HArray2OfReal,TwoDTolFr : OCP.TColStd.TColStd_HArray2OfReal,ThreeDTolFr : OCP.TColStd.TColStd_HArray2OfReal,FirstInU : float,LastInU : float,FirstInV : float,LastInV : float,FavorIso : OCP.GeomAbs.GeomAbs_IsoType,ContInU : OCP.GeomAbs.GeomAbs_Shape,ContInV : OCP.GeomAbs.GeomAbs_Shape,PrecisCode : int,MaxDegInU : int,MaxDegInV : int,MaxPatch : int,Func : AdvApp2Var_EvaluatorFunc2Var,Crit : AdvApp2Var_Criterion,UChoice : OCP.AdvApprox.AdvApprox_Cutting,VChoice : OCP.AdvApprox.AdvApprox_Cutting) -> None: ...
    @overload
    def __init__(self,Num1DSS : int,Num2DSS : int,Num3DSS : int,OneDTol : OCP.TColStd.TColStd_HArray1OfReal,TwoDTol : OCP.TColStd.TColStd_HArray1OfReal,ThreeDTol : OCP.TColStd.TColStd_HArray1OfReal,OneDTolFr : OCP.TColStd.TColStd_HArray2OfReal,TwoDTolFr : OCP.TColStd.TColStd_HArray2OfReal,ThreeDTolFr : OCP.TColStd.TColStd_HArray2OfReal,FirstInU : float,LastInU : float,FirstInV : float,LastInV : float,FavorIso : OCP.GeomAbs.GeomAbs_IsoType,ContInU : OCP.GeomAbs.GeomAbs_Shape,ContInV : OCP.GeomAbs.GeomAbs_Shape,PrecisCode : int,MaxDegInU : int,MaxDegInV : int,MaxPatch : int,Func : AdvApp2Var_EvaluatorFunc2Var,UChoice : OCP.AdvApprox.AdvApprox_Cutting,VChoice : OCP.AdvApprox.AdvApprox_Cutting) -> None: ...
    pass
class AdvApp2Var_ApproxF2var():
    """
    None
    """
    def __init__(self) -> None: ...
    @staticmethod
    def mma1her__s(arg0 : int,arg1 : float,arg2 : int) -> int: 
        """
        None
        """
    @staticmethod
    def mma2ac1__s(arg0 : int,arg1 : int,arg2 : int,arg3 : int,arg4 : int,arg5 : float,arg6 : float,arg7 : float,arg8 : float,arg9 : float,arg10 : float,arg11 : float) -> int: 
        """
        None
        """
    @staticmethod
    def mma2ac2__s(arg0 : int,arg1 : int,arg2 : int,arg3 : int,arg4 : int,arg5 : int,arg6 : float,arg7 : int,arg8 : float,arg9 : float,arg10 : float) -> int: 
        """
        None
        """
    @staticmethod
    def mma2ac3__s(arg0 : int,arg1 : int,arg2 : int,arg3 : int,arg4 : int,arg5 : int,arg6 : float,arg7 : int,arg8 : float,arg9 : float,arg10 : float) -> int: 
        """
        None
        """
    @staticmethod
    def mma2can__s(arg0 : int,arg1 : int,arg2 : int,arg3 : int,arg4 : int,arg5 : int,arg6 : int,arg7 : float,arg8 : float,arg9 : float,arg10 : int) -> int: 
        """
        None
        """
    @staticmethod
    def mma2cdi__s(ndimen : int,nbpntu : int,urootl : float,nbpntv : int,vrootl : float,iordru : int,iordrv : int,contr1 : float,contr2 : float,contr3 : float,contr4 : float,sotbu1 : float,sotbu2 : float,ditbu1 : float,ditbu2 : float,sotbv1 : float,sotbv2 : float,ditbv1 : float,ditbv2 : float,sosotb : float,soditb : float,disotb : float,diditb : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mma2ce1__s(numdec : int,ndimen : int,nbsesp : int,ndimse : int,ndminu : int,ndminv : int,ndguli : int,ndgvli : int,ndjacu : int,ndjacv : int,iordru : int,iordrv : int,nbpntu : int,nbpntv : int,epsapr : float,sosotb : float,disotb : float,soditb : float,diditb : float,patjac : float,errmax : float,errmoy : float,ndegpu : int,ndegpv : int,itydec : int,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mma2ds1__s(ndimen : int,uintfn : float,vintfn : float,foncnp : AdvApp2Var_EvaluatorFunc2Var,nbpntu : int,nbpntv : int,urootb : float,vrootb : float,isofav : int,sosotb : float,disotb : float,soditb : float,diditb : float,fpntab : float,ttable : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mma2fnc__s(ndimen : int,nbsesp : int,ndimse : int,uvfonc : float,foncnp : AdvApp2Var_EvaluatorFunc2Var,tconst : float,isofav : int,nbroot : int,rootlg : float,iordre : int,ideriv : int,ndgjac : int,nbcrmx : int,ncflim : int,epsapr : float,ncoeff : int,courbe : float,nbcrbe : int,somtab : float,diftab : float,contr1 : float,contr2 : float,tabdec : float,errmax : float,errmoy : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mma2fx6__s(ncfmxu : int,ncfmxv : int,ndimen : int,nbsesp : int,ndimse : int,nbupat : int,nbvpat : int,iordru : int,iordrv : int,epsapr : float,epsfro : float,patcan : float,errmax : float,ncoefu : int,ncoefv : int) -> int: 
        """
        None
        """
    @staticmethod
    def mma2jmx__s(ndgjac : int,iordre : int,xjacmx : float) -> int: 
        """
        None
        """
    @staticmethod
    def mma2roo__s(nbpntu : int,nbpntv : int,urootl : float,vrootl : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmapptt__s(arg0 : int,arg1 : int,arg2 : int,arg3 : float,arg4 : int) -> int: 
        """
        None
        """
    pass
class AdvApp2Var_Context():
    """
    contains all the parameters for approximation ( tolerancy, computing option, ...)
    """
    def CToler(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def FToler(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def FavorIso(self) -> int: 
        """
        None
        """
    def IToler(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def TotalDimension(self) -> int: 
        """
        None
        """
    def TotalNumberSSP(self) -> int: 
        """
        None
        """
    def UGauss(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def UJacDeg(self) -> int: 
        """
        None
        """
    def UJacMax(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def ULimit(self) -> int: 
        """
        None
        """
    def UOrder(self) -> int: 
        """
        None
        """
    def URoots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def VGauss(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def VJacDeg(self) -> int: 
        """
        None
        """
    def VJacMax(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def VLimit(self) -> int: 
        """
        None
        """
    def VOrder(self) -> int: 
        """
        None
        """
    def VRoots(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,ifav : int,iu : int,iv : int,nlimu : int,nlimv : int,iprecis : int,nb1Dss : int,nb2Dss : int,nb3Dss : int,tol1D : OCP.TColStd.TColStd_HArray1OfReal,tol2D : OCP.TColStd.TColStd_HArray1OfReal,tol3D : OCP.TColStd.TColStd_HArray1OfReal,tof1D : OCP.TColStd.TColStd_HArray2OfReal,tof2D : OCP.TColStd.TColStd_HArray2OfReal,tof3D : OCP.TColStd.TColStd_HArray2OfReal) -> None: ...
    pass
class AdvApp2Var_Criterion():
    """
    this class contains a given criterion to be satisfied
    """
    def IsSatisfied(self,P : AdvApp2Var_Patch) -> bool: 
        """
        None
        """
    def MaxValue(self) -> float: 
        """
        None
        """
    def Repartition(self) -> AdvApp2Var_CriterionRepartition: 
        """
        None
        """
    def Type(self) -> AdvApp2Var_CriterionType: 
        """
        None
        """
    def Value(self,P : AdvApp2Var_Patch,C : AdvApp2Var_Context) -> None: 
        """
        None
        """
    pass
class AdvApp2Var_CriterionRepartition():
    """
    way of cutting process//! all new cutting points at each step of cutting process : (a+i(b-a)/N)i at step N, (a+i(b-a)/(N+1))i at step N+1,... where (a,b) is the global interval//! add one new cutting point at each step of cutting process

    Members:

      AdvApp2Var_Regular

      AdvApp2Var_Incremental
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    AdvApp2Var_Incremental: OCP.AdvApp2Var.AdvApp2Var_CriterionRepartition # value = <AdvApp2Var_CriterionRepartition.AdvApp2Var_Incremental: 1>
    AdvApp2Var_Regular: OCP.AdvApp2Var.AdvApp2Var_CriterionRepartition # value = <AdvApp2Var_CriterionRepartition.AdvApp2Var_Regular: 0>
    __entries: dict # value = {'AdvApp2Var_Regular': (<AdvApp2Var_CriterionRepartition.AdvApp2Var_Regular: 0>, None), 'AdvApp2Var_Incremental': (<AdvApp2Var_CriterionRepartition.AdvApp2Var_Incremental: 1>, None)}
    __members__: dict # value = {'AdvApp2Var_Regular': <AdvApp2Var_CriterionRepartition.AdvApp2Var_Regular: 0>, 'AdvApp2Var_Incremental': <AdvApp2Var_CriterionRepartition.AdvApp2Var_Incremental: 1>}
    pass
class AdvApp2Var_CriterionType():
    """
    influency of the criterion on cutting process//! cutting when criterion is not satisfied desactivation of the compute of the error max//! cutting when error max is not good or if error max is good and criterion is not satisfied

    Members:

      AdvApp2Var_Absolute

      AdvApp2Var_Relative
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    AdvApp2Var_Absolute: OCP.AdvApp2Var.AdvApp2Var_CriterionType # value = <AdvApp2Var_CriterionType.AdvApp2Var_Absolute: 0>
    AdvApp2Var_Relative: OCP.AdvApp2Var.AdvApp2Var_CriterionType # value = <AdvApp2Var_CriterionType.AdvApp2Var_Relative: 1>
    __entries: dict # value = {'AdvApp2Var_Absolute': (<AdvApp2Var_CriterionType.AdvApp2Var_Absolute: 0>, None), 'AdvApp2Var_Relative': (<AdvApp2Var_CriterionType.AdvApp2Var_Relative: 1>, None)}
    __members__: dict # value = {'AdvApp2Var_Absolute': <AdvApp2Var_CriterionType.AdvApp2Var_Absolute: 0>, 'AdvApp2Var_Relative': <AdvApp2Var_CriterionType.AdvApp2Var_Relative: 1>}
    pass
class AdvApp2Var_Data():
    """
    /
    """
    @staticmethod
    def Getmaovpar_s() -> maovpar_1_: 
        """
        None
        """
    @staticmethod
    def Getmaovpch_s() -> maovpch_1_: 
        """
        None
        """
    @staticmethod
    def Getmdnombr_s() -> mdnombr_1_: 
        """
        None
        """
    @staticmethod
    def Getminombr_s() -> minombr_1_: 
        """
        None
        """
    @staticmethod
    def Getmlgdrtl_s() -> mlgdrtl_1_: 
        """
        None
        """
    @staticmethod
    def Getmmapgs0_s() -> mmapgs0_1_: 
        """
        None
        """
    @staticmethod
    def Getmmapgs1_s() -> mmapgs1_1_: 
        """
        None
        """
    @staticmethod
    def Getmmapgs2_s() -> mmapgs2_1_: 
        """
        None
        """
    @staticmethod
    def Getmmapgss_s() -> mmapgss_1_: 
        """
        None
        """
    @staticmethod
    def Getmmcmcnp_s() -> mmcmcnp_1_: 
        """
        None
        """
    @staticmethod
    def Getmmjcobi_s() -> mmjcobi_1_: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class AdvApp2Var_EvaluatorFunc2Var():
    """
    None
    """
    def Evaluate(self,theDimension : int,theUStartEnd : float,theVStartEnd : float,theFavorIso : int,theConstParam : float,theNbParams : int,theParameters : float,theUOrder : int,theVOrder : int,theResult : float,theErrorCode : int) -> None: 
        """
        Function evaluation method to be defined by descendant
        """
    def __init__(self) -> None: ...
    pass
class AdvApp2Var_Framework():
    """
    None
    """
    def ChangeIso(self,IndexIso : int,IndexStrip : int,anIso : AdvApp2Var_Iso) -> None: 
        """
        None
        """
    def FirstNode(self,Type : OCP.GeomAbs.GeomAbs_IsoType,IndexIso : int,IndexStrip : int) -> int: 
        """
        None
        """
    def FirstNotApprox(self,IndexIso : int,IndexStrip : int) -> AdvApp2Var_Iso: 
        """
        search the Index of the first Iso not approximated, if all Isos are approximated NULL is returned.
        """
    def IsoU(self,U : float,V0 : float,V1 : float) -> AdvApp2Var_Iso: 
        """
        None
        """
    def IsoV(self,U0 : float,U1 : float,V : float) -> AdvApp2Var_Iso: 
        """
        None
        """
    def LastNode(self,Type : OCP.GeomAbs.GeomAbs_IsoType,IndexIso : int,IndexStrip : int) -> int: 
        """
        None
        """
    @overload
    def Node(self,U : float,V : float) -> AdvApp2Var_Node: 
        """
        None

        None
        """
    @overload
    def Node(self,IndexNode : int) -> AdvApp2Var_Node: ...
    def UEquation(self,IndexIso : int,IndexStrip : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def UpdateInU(self,CuttingValue : float) -> None: 
        """
        None
        """
    def UpdateInV(self,CuttingValue : float) -> None: 
        """
        None
        """
    def VEquation(self,IndexIso : int,IndexStrip : int) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Frame : AdvApp2Var_SequenceOfNode,UFrontier : AdvApp2Var_SequenceOfStrip,VFrontier : AdvApp2Var_SequenceOfStrip) -> None: ...
    pass
class AdvApp2Var_Iso(OCP.Standard.Standard_Transient):
    """
    used to store constraints on a line U = Ui or V = Vj
    """
    @overload
    def ChangeDomain(self,a : float,b : float,c : float,d : float) -> None: 
        """
        None

        None
        """
    @overload
    def ChangeDomain(self,a : float,b : float) -> None: ...
    def Constante(self) -> float: 
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
    def DifTab(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
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
    def HasResult(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsApproximated(self) -> bool: 
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
    def MakeApprox(self,Conditions : AdvApp2Var_Context,a : float,b : float,c : float,d : float,func : AdvApp2Var_EvaluatorFunc2Var,NodeBegin : AdvApp2Var_Node,NodeEnd : AdvApp2Var_Node) -> None: 
        """
        None
        """
    def MaxErrors(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def MoyErrors(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def NbCoeff(self) -> int: 
        """
        None
        """
    def OverwriteApprox(self) -> None: 
        """
        None
        """
    def Polynom(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def Position(self) -> int: 
        """
        None
        """
    def ResetApprox(self) -> None: 
        """
        None
        """
    def SetConstante(self,newcte : float) -> None: 
        """
        None
        """
    def SetPosition(self,newpos : int) -> None: 
        """
        None
        """
    def SomTab(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def T0(self) -> float: 
        """
        None
        """
    def T1(self) -> float: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.GeomAbs.GeomAbs_IsoType: 
        """
        None
        """
    def U0(self) -> float: 
        """
        None
        """
    def U1(self) -> float: 
        """
        None
        """
    def UOrder(self) -> int: 
        """
        None
        """
    def V0(self) -> float: 
        """
        None
        """
    def V1(self) -> float: 
        """
        None
        """
    def VOrder(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self,type : OCP.GeomAbs.GeomAbs_IsoType,cte : float,Ufirst : float,Ulast : float,Vfirst : float,Vlast : float,pos : int,iu : int,iv : int) -> None: ...
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
class AdvApp2Var_MathBase():
    """
    None
    """
    def __init__(self) -> None: ...
    @staticmethod
    def mdsptpt__s(ndimen : int,point1 : float,point2 : float,distan : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmapcmp__s(arg0 : int,arg1 : int,arg2 : int,arg3 : float,arg4 : float) -> int: ...
    @staticmethod
    def mmaperx__s(ncofmx : int,ndimen : int,ncoeff : int,iordre : int,crvjac : float,ncfnew : int,ycvmax : float,errmax : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmarcin__s(ndimax : int,ndim : int,ncoeff : int,crvold : float,u0 : float,u1 : float,crvnew : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmbulld__s(nbcoln : int,nblign : int,dtabtr : float,numcle : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmcdriv__s(ndimen : int,ncoeff : int,courbe : float,ideriv : int,ncofdv : int,crvdrv : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmcglc1__s(ndimax : int,ndimen : int,ncoeff : int,courbe : float,tdebut : float,tfinal : float,epsiln : float,xlongc : float,erreur : float,iercod : int) -> int: ...
    @staticmethod
    def mmcvctx__s(ndimen : int,ncofmx : int,nderiv : int,ctrtes : float,crvres : float,tabaux : float,xmatri : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmcvinv__s(ndimax : int,ncoef : int,ndim : int,curveo : float,curve : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmdrc11__s(arg0 : int,arg1 : int,arg2 : int,arg3 : float,arg4 : float,arg5 : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmdrvck__s(ncoeff : int,ndimen : int,courbe : float,ideriv : int,tparam : float,pntcrb : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmeps1__s(epsilo : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmfmca8__s(ndimen : int,ncoefu : int,ncoefv : int,ndimax : int,ncfumx : int,ncfvmx : int,tabini : float,tabres : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmfmca9__s(arg0 : int,arg1 : int,arg2 : int,arg3 : int,arg4 : int,arg5 : int,arg6 : float,arg7 : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmfmcar__s(ndimen : int,ncofmx : int,ncoefu : int,ncoefv : int,patold : float,upara1 : float,upara2 : float,vpara1 : float,vpara2 : float,patnew : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmfmcb5__s(arg0 : int,arg1 : int,arg2 : int,arg3 : float,arg4 : int,arg5 : int,arg6 : int,arg7 : float,arg8 : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmfmtb1__s(maxsz1 : int,table1 : float,isize1 : int,jsize1 : int,maxsz2 : int,table2 : float,isize2 : int,jsize2 : int,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmgaus1__s(ndimf : int,bfunx : Any,k : int,xd : float,xf : float,saux1 : float,saux2 : float,somme : float,niter : int,iercod : int) -> int: 
        """
        mmgaus1__s(ndimf: int, bfunx: int (int*, double*, double*, int*), k: int, xd: float, xf: float, saux1: float, saux2: float, somme: float, niter: int, iercod: int) -> int

        None
        """
    @staticmethod
    def mmhjcan__s(ndimen : int,ncourb : int,ncftab : int,orcont : int,ncflim : int,tcbold : float,tdecop : float,tcbnew : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mminltt__s(ncolmx : int,nlgnmx : int,tabtri : float,nbrcol : int,nbrlgn : int,ajoute : float,epseg : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmjacan__s(ideriv : int,ndeg : int,poljac : float,polcan : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmjaccv__s(ncoef : int,ndim : int,ider : int,crvlgd : float,polaux : float,crvcan : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmmpocur__s(ncofmx : int,ndim : int,ndeg : int,courbe : float,tparam : float,tabval : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmmrslwd__s(normax : int,nordre : int,ndim : int,amat : float,bmat : float,epspiv : float,aaux : float,xmat : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmpobas__s(tparam : float,iordre : int,ncoeff : int,nderiv : int,valbas : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmpocrb__s(ndimax : int,ncoeff : int,courbe : float,ndim : int,tparam : float,pntcrb : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmposui__s(dimmat : int,nistoc : int,aposit : int,posuiv : int,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmresol__s(hdimen : int,gdimen : int,hnstoc : int,gnstoc : int,mnstoc : int,matsyh : float,matsyg : float,vecsyh : float,vecsyg : float,hposit : int,hposui : int,gposit : int,mmposui : int,mposit : int,vecsol : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmrtptt__s(ndglgd : int,rtlegd : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmsrre2__s(tparam : float,nbrval : int,tablev : float,epsil : float,numint : int,itypen : int,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmtrpjj__s(ncofmx : int,ndimen : int,ncoeff : int,epsi3d : float,iordre : int,crvlgd : float,ycvmax : float,errmax : float,ncfnew : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmunivt__s(ndimen : int,vector : float,vecnrm : float,epsiln : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmveps3__s(eps03 : float) -> int: 
        """
        None
        """
    @staticmethod
    def mmvncol__s(ndimen : int,vecin : float,vecout : float,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mmwprcs__s(arg0 : float,arg1 : float,arg2 : float,arg3 : float,arg4 : int,arg5 : int) -> None: 
        """
        None
        """
    @staticmethod
    def msc__s(ndimen : int,vecte1 : float,vecte2 : float) -> float: 
        """
        None
        """
    @staticmethod
    def mvsheld__s(n : int,is_ : int,dtab : float,icle : int) -> int: 
        """
        None
        """
    @staticmethod
    def mzsnorm__s(ndimen : int,vecteu : float) -> float: 
        """
        None
        """
    @staticmethod
    def pow__di_s(x : float,n : int) -> float: 
        """
        None
        """
    pass
class AdvApp2Var_Network():
    """
    None
    """
    def ChangePatch(self,Index : int) -> AdvApp2Var_Patch: 
        """
        None
        """
    def FirstNotApprox(self,Index : int) -> bool: 
        """
        search the Index of the first Patch not approximated, if all Patches are approximated Standard_False is returned
        """
    def NbPatch(self) -> int: 
        """
        None
        """
    def NbPatchInU(self) -> int: 
        """
        None
        """
    def NbPatchInV(self) -> int: 
        """
        None
        """
    def Patch(self,UIndex : int,VIndex : int) -> AdvApp2Var_Patch: 
        """
        None
        """
    def SameDegree(self,iu : int,iv : int) -> Tuple[int, int]: 
        """
        None
        """
    def UParameter(self,Index : int) -> float: 
        """
        None
        """
    def UpdateInU(self,CuttingValue : float) -> None: 
        """
        None
        """
    def UpdateInV(self,CuttingValue : float) -> None: 
        """
        None
        """
    def VParameter(self,Index : int) -> float: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Net : AdvApp2Var_SequenceOfPatch,TheU : OCP.TColStd.TColStd_SequenceOfReal,TheV : OCP.TColStd.TColStd_SequenceOfReal) -> None: ...
    pass
class AdvApp2Var_Node(OCP.Standard.Standard_Transient):
    """
    used to store constraints on a (Ui,Vj) point
    """
    def Coord(self) -> OCP.gp.gp_XY: 
        """
        Returns the coordinates (U,V) of the node
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
    def Error(self,iu : int,iv : int) -> float: 
        """
        returns the error between F(U,V) and its approximation
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
    def Point(self,iu : int,iv : int) -> OCP.gp.gp_Pnt: 
        """
        returns the value F(U,V) or its derivates on the node (U,V)
        """
    def SetCoord(self,x1 : float,x2 : float) -> None: 
        """
        changes the coordinates (U,V) to (x1,x2)
        """
    def SetError(self,iu : int,iv : int,error : float) -> None: 
        """
        affects the error between F(U,V) and its approximation
        """
    def SetPoint(self,iu : int,iv : int,Pt : OCP.gp.gp_Pnt) -> None: 
        """
        affects the value F(U,V) or its derivates on the node (U,V)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UOrder(self) -> int: 
        """
        returns the continuity order in U of the node
        """
    def VOrder(self) -> int: 
        """
        returns the continuity order in V of the node
        """
    @overload
    def __init__(self,UV : OCP.gp.gp_XY,iu : int,iv : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,iu : int,iv : int) -> None: ...
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
class AdvApp2Var_Patch(OCP.Standard.Standard_Transient):
    """
    used to store results on a domain [Ui,Ui+1]x[Vj,Vj+1]
    """
    def AddConstraints(self,Conditions : AdvApp2Var_Context,Constraints : AdvApp2Var_Framework) -> None: 
        """
        None
        """
    def AddErrors(self,Constraints : AdvApp2Var_Framework) -> None: 
        """
        None
        """
    def AverageErrors(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def ChangeDomain(self,a : float,b : float,c : float,d : float) -> None: 
        """
        None
        """
    def ChangeNbCoeff(self,NbCoeffU : int,NbCoeffV : int) -> None: 
        """
        None
        """
    def Coefficients(self,SSPIndex : int,Conditions : AdvApp2Var_Context) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def CritValue(self) -> float: 
        """
        None
        """
    @overload
    def CutSense(self) -> int: 
        """
        None

        None
        """
    @overload
    def CutSense(self,Crit : AdvApp2Var_Criterion,NumDec : int) -> int: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Discretise(self,Conditions : AdvApp2Var_Context,Constraints : AdvApp2Var_Framework,func : AdvApp2Var_EvaluatorFunc2Var) -> None: 
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
    def HasResult(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsApproximated(self) -> bool: 
        """
        None
        """
    def IsDiscretised(self) -> bool: 
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
    def IsoErrors(self) -> OCP.TColStd.TColStd_HArray2OfReal: 
        """
        None
        """
    def MakeApprox(self,Conditions : AdvApp2Var_Context,Constraints : AdvApp2Var_Framework,NumDec : int) -> None: 
        """
        None
        """
    def MaxErrors(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def NbCoeffInU(self) -> int: 
        """
        None
        """
    def NbCoeffInV(self) -> int: 
        """
        None
        """
    def OverwriteApprox(self) -> None: 
        """
        None
        """
    def Poles(self,SSPIndex : int,Conditions : AdvApp2Var_Context) -> OCP.TColgp.TColgp_HArray2OfPnt: 
        """
        None
        """
    def ResetApprox(self) -> None: 
        """
        None
        """
    def SetCritValue(self,dist : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def U0(self) -> float: 
        """
        None
        """
    def U1(self) -> float: 
        """
        None
        """
    def UOrder(self) -> int: 
        """
        None
        """
    def V0(self) -> float: 
        """
        None
        """
    def V1(self) -> float: 
        """
        None
        """
    def VOrder(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,U0 : float,U1 : float,V0 : float,V1 : float,iu : int,iv : int) -> None: ...
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
class AdvApp2Var_SequenceOfNode(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : AdvApp2Var_Node) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : AdvApp2Var_SequenceOfNode) -> None: ...
    def Assign(self,theOther : AdvApp2Var_SequenceOfNode) -> AdvApp2Var_SequenceOfNode: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> AdvApp2Var_Node: 
        """
        First item access
        """
    def ChangeLast(self) -> AdvApp2Var_Node: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> AdvApp2Var_Node: 
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
    def First(self) -> AdvApp2Var_Node: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : AdvApp2Var_Node) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : AdvApp2Var_SequenceOfNode) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : AdvApp2Var_SequenceOfNode) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : AdvApp2Var_Node) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> AdvApp2Var_Node: 
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
    def Prepend(self,theSeq : AdvApp2Var_SequenceOfNode) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : AdvApp2Var_Node) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : AdvApp2Var_Node) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : AdvApp2Var_SequenceOfNode) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> AdvApp2Var_Node: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : AdvApp2Var_SequenceOfNode) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class AdvApp2Var_SequenceOfPatch(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : AdvApp2Var_SequenceOfPatch) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : AdvApp2Var_Patch) -> None: ...
    def Assign(self,theOther : AdvApp2Var_SequenceOfPatch) -> AdvApp2Var_SequenceOfPatch: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> AdvApp2Var_Patch: 
        """
        First item access
        """
    def ChangeLast(self) -> AdvApp2Var_Patch: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> AdvApp2Var_Patch: 
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
    def First(self) -> AdvApp2Var_Patch: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : AdvApp2Var_SequenceOfPatch) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : AdvApp2Var_Patch) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : AdvApp2Var_Patch) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : AdvApp2Var_SequenceOfPatch) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> AdvApp2Var_Patch: 
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
    def Prepend(self,theItem : AdvApp2Var_Patch) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : AdvApp2Var_SequenceOfPatch) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : AdvApp2Var_Patch) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : AdvApp2Var_SequenceOfPatch) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> AdvApp2Var_Patch: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : AdvApp2Var_SequenceOfPatch) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class AdvApp2Var_SequenceOfStrip(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : AdvApp2Var_SequenceOfStrip) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : AdvApp2Var_Strip) -> None: ...
    def Assign(self,theOther : AdvApp2Var_SequenceOfStrip) -> AdvApp2Var_SequenceOfStrip: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> AdvApp2Var_Strip: 
        """
        First item access
        """
    def ChangeLast(self) -> AdvApp2Var_Strip: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> AdvApp2Var_Strip: 
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
    def First(self) -> AdvApp2Var_Strip: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : AdvApp2Var_Strip) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : AdvApp2Var_SequenceOfStrip) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : AdvApp2Var_SequenceOfStrip) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : AdvApp2Var_Strip) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> AdvApp2Var_Strip: 
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
    def Prepend(self,theItem : AdvApp2Var_Strip) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : AdvApp2Var_SequenceOfStrip) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : AdvApp2Var_Strip) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : AdvApp2Var_SequenceOfStrip) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> AdvApp2Var_Strip: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : AdvApp2Var_SequenceOfStrip) -> None: ...
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
class AdvApp2Var_Strip(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : AdvApp2Var_Strip) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : AdvApp2Var_Iso) -> None: ...
    def Assign(self,theOther : AdvApp2Var_Strip) -> AdvApp2Var_Strip: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> AdvApp2Var_Iso: 
        """
        First item access
        """
    def ChangeLast(self) -> AdvApp2Var_Iso: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> AdvApp2Var_Iso: 
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
    def First(self) -> AdvApp2Var_Iso: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : AdvApp2Var_Iso) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : AdvApp2Var_Strip) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : AdvApp2Var_Iso) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : AdvApp2Var_Strip) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> AdvApp2Var_Iso: 
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
    def Prepend(self,theSeq : AdvApp2Var_Strip) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : AdvApp2Var_Iso) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : AdvApp2Var_Iso) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : AdvApp2Var_Strip) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> AdvApp2Var_Iso: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : AdvApp2Var_Strip) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class AdvApp2Var_SysBase():
    """
    None
    """
    def __init__(self) -> None: ...
    @staticmethod
    def do__fio_s() -> int: 
        """
        None
        """
    @staticmethod
    def do__lio_s() -> int: 
        """
        None
        """
    @staticmethod
    def macinit__s(arg0 : int,arg1 : int) -> int: 
        """
        None
        """
    def macrai4_(self,nbelem : int,maxelm : int,itablo : int,iofset : int,iercod : int) -> int: 
        """
        None
        """
    def macrar8_(self,nbelem : int,maxelm : int,xtablo : float,iofset : int,iercod : int) -> int: 
        """
        None
        """
    def macrdi4_(self,nbelem : int,maxelm : int,itablo : int,iofset : int,iercod : int) -> int: 
        """
        None
        """
    def macrdr8_(self,nbelem : int,maxelm : int,xtablo : float,iofset : int,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def maermsg__s(cnompg : str,icoder : int,cnompg_len : int) -> int: 
        """
        None
        """
    def mainial_(self) -> int: 
        """
        None
        """
    @staticmethod
    def maitbr8__s(itaill : int,xtab : float,xval : float) -> int: 
        """
        None
        """
    @staticmethod
    def maovsr8__s(ivalcs : int) -> int: 
        """
        None
        """
    def mcrdelt_(self,iunit : int,isize : int,t : capsule,iofset : int,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mcrfill__s(size : int,tin : capsule,tout : capsule) -> int: 
        """
        None
        """
    def mcrrqst_(self,iunit : int,isize : int,t : capsule,iofset : int,iercod : int) -> int: 
        """
        None
        """
    @staticmethod
    def mgenmsg__s(nomprg : str,nomprg_len : int) -> int: 
        """
        None
        """
    @staticmethod
    def mgsomsg__s(nomprg : str,nomprg_len : int) -> int: 
        """
        None
        """
    @staticmethod
    def miraz__s(taille : int,adt : capsule) -> None: 
        """
        None
        """
    @staticmethod
    def mnfndeb__s() -> int: 
        """
        None
        """
    @staticmethod
    def msifill__s(nbintg : int,ivecin : int,ivecou : int) -> int: 
        """
        None
        """
    @staticmethod
    def msrfill__s(nbreel : int,vecent : float,vecsor : float) -> int: 
        """
        None
        """
    @staticmethod
    def mswrdbg__s(ctexte : str,ctexte_len : int) -> int: 
        """
        None
        """
    @staticmethod
    def mvriraz__s(taille : int,adt : capsule) -> None: 
        """
        None
        """
    pass
class Namelist():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Vardesc():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class alist():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def aerr(self) -> int:
        """
        :type: int
        """
    @aerr.setter
    def aerr(self, arg0: int) -> None:
        pass
    @property
    def aunit(self) -> int:
        """
        :type: int
        """
    @aunit.setter
    def aunit(self, arg0: int) -> None:
        pass
    pass
class cilist():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def ciend(self) -> int:
        """
        :type: int
        """
    @ciend.setter
    def ciend(self, arg0: int) -> None:
        pass
    @property
    def cierr(self) -> int:
        """
        :type: int
        """
    @cierr.setter
    def cierr(self, arg0: int) -> None:
        pass
    @property
    def cirec(self) -> int:
        """
        :type: int
        """
    @cirec.setter
    def cirec(self, arg0: int) -> None:
        pass
    @property
    def ciunit(self) -> int:
        """
        :type: int
        """
    @ciunit.setter
    def ciunit(self, arg0: int) -> None:
        pass
    pass
class cllist():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def cerr(self) -> int:
        """
        :type: int
        """
    @cerr.setter
    def cerr(self, arg0: int) -> None:
        pass
    @property
    def cunit(self) -> int:
        """
        :type: int
        """
    @cunit.setter
    def cunit(self, arg0: int) -> None:
        pass
    pass
class complex():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def i(self) -> float:
        """
        :type: float
        """
    @i.setter
    def i(self, arg0: float) -> None:
        pass
    @property
    def r(self) -> float:
        """
        :type: float
        """
    @r.setter
    def r(self, arg0: float) -> None:
        pass
    pass
class doublecomplex():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def i(self) -> float:
        """
        :type: float
        """
    @i.setter
    def i(self, arg0: float) -> None:
        pass
    @property
    def r(self) -> float:
        """
        :type: float
        """
    @r.setter
    def r(self, arg0: float) -> None:
        pass
    pass
class icilist():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def iciend(self) -> int:
        """
        :type: int
        """
    @iciend.setter
    def iciend(self, arg0: int) -> None:
        pass
    @property
    def icierr(self) -> int:
        """
        :type: int
        """
    @icierr.setter
    def icierr(self, arg0: int) -> None:
        pass
    @property
    def icirlen(self) -> int:
        """
        :type: int
        """
    @icirlen.setter
    def icirlen(self, arg0: int) -> None:
        pass
    @property
    def icirnum(self) -> int:
        """
        :type: int
        """
    @icirnum.setter
    def icirnum(self, arg0: int) -> None:
        pass
    pass
class inlist():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def inacclen(self) -> int:
        """
        :type: int
        """
    @inacclen.setter
    def inacclen(self, arg0: int) -> None:
        pass
    @property
    def inblanklen(self) -> int:
        """
        :type: int
        """
    @inblanklen.setter
    def inblanklen(self, arg0: int) -> None:
        pass
    @property
    def indirlen(self) -> int:
        """
        :type: int
        """
    @indirlen.setter
    def indirlen(self, arg0: int) -> None:
        pass
    @property
    def inerr(self) -> int:
        """
        :type: int
        """
    @inerr.setter
    def inerr(self, arg0: int) -> None:
        pass
    @property
    def infilen(self) -> int:
        """
        :type: int
        """
    @infilen.setter
    def infilen(self, arg0: int) -> None:
        pass
    @property
    def infmtlen(self) -> int:
        """
        :type: int
        """
    @infmtlen.setter
    def infmtlen(self, arg0: int) -> None:
        pass
    @property
    def informlen(self) -> int:
        """
        :type: int
        """
    @informlen.setter
    def informlen(self, arg0: int) -> None:
        pass
    @property
    def innamlen(self) -> int:
        """
        :type: int
        """
    @innamlen.setter
    def innamlen(self, arg0: int) -> None:
        pass
    @property
    def inseqlen(self) -> int:
        """
        :type: int
        """
    @inseqlen.setter
    def inseqlen(self, arg0: int) -> None:
        pass
    @property
    def inunflen(self) -> int:
        """
        :type: int
        """
    @inunflen.setter
    def inunflen(self, arg0: int) -> None:
        pass
    @property
    def inunit(self) -> int:
        """
        :type: int
        """
    @inunit.setter
    def inunit(self, arg0: int) -> None:
        pass
    pass
class maovpar_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def i2ovn(self) -> int:
        """
        :type: int
        """
    @i2ovn.setter
    def i2ovn(self, arg0: int) -> None:
        pass
    @property
    def i2ovr(self) -> int:
        """
        :type: int
        """
    @i2ovr.setter
    def i2ovr(self, arg0: int) -> None:
        pass
    @property
    def i4ovn(self) -> int:
        """
        :type: int
        """
    @i4ovn.setter
    def i4ovn(self, arg0: int) -> None:
        pass
    @property
    def i4ovr(self) -> int:
        """
        :type: int
        """
    @i4ovr.setter
    def i4ovr(self, arg0: int) -> None:
        pass
    @property
    def r4exn(self) -> int:
        """
        :type: int
        """
    @r4exn.setter
    def r4exn(self, arg0: int) -> None:
        pass
    @property
    def r4exp(self) -> int:
        """
        :type: int
        """
    @r4exp.setter
    def r4exp(self, arg0: int) -> None:
        pass
    @property
    def r4nbe(self) -> int:
        """
        :type: int
        """
    @r4nbe.setter
    def r4nbe(self, arg0: int) -> None:
        pass
    @property
    def r4nbm(self) -> int:
        """
        :type: int
        """
    @r4nbm.setter
    def r4nbm(self, arg0: int) -> None:
        pass
    @property
    def r4ncs(self) -> int:
        """
        :type: int
        """
    @r4ncs.setter
    def r4ncs(self, arg0: int) -> None:
        pass
    @property
    def r4ovr(self) -> float:
        """
        :type: float
        """
    @r4ovr.setter
    def r4ovr(self, arg0: float) -> None:
        pass
    @property
    def r4und(self) -> float:
        """
        :type: float
        """
    @r4und.setter
    def r4und(self, arg0: float) -> None:
        pass
    @property
    def r8exn(self) -> int:
        """
        :type: int
        """
    @r8exn.setter
    def r8exn(self, arg0: int) -> None:
        pass
    @property
    def r8exp(self) -> int:
        """
        :type: int
        """
    @r8exp.setter
    def r8exp(self, arg0: int) -> None:
        pass
    @property
    def r8nbe(self) -> int:
        """
        :type: int
        """
    @r8nbe.setter
    def r8nbe(self, arg0: int) -> None:
        pass
    @property
    def r8nbm(self) -> int:
        """
        :type: int
        """
    @r8nbm.setter
    def r8nbm(self, arg0: int) -> None:
        pass
    @property
    def r8ncs(self) -> int:
        """
        :type: int
        """
    @r8ncs.setter
    def r8ncs(self, arg0: int) -> None:
        pass
    @property
    def r8ovr(self) -> float:
        """
        :type: float
        """
    @r8ovr.setter
    def r8ovr(self, arg0: float) -> None:
        pass
    @property
    def r8und(self) -> float:
        """
        :type: float
        """
    @r8und.setter
    def r8und(self, arg0: float) -> None:
        pass
    @property
    def x4ovr(self) -> float:
        """
        :type: float
        """
    @x4ovr.setter
    def x4ovr(self, arg0: float) -> None:
        pass
    @property
    def x4und(self) -> float:
        """
        :type: float
        """
    @x4und.setter
    def x4und(self, arg0: float) -> None:
        pass
    pass
class maovpch_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class mdnombr_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def a180(self) -> float:
        """
        :type: float
        """
    @a180.setter
    def a180(self, arg0: float) -> None:
        pass
    @property
    def a360(self) -> float:
        """
        :type: float
        """
    @a360.setter
    def a360(self, arg0: float) -> None:
        pass
    @property
    def a90(self) -> float:
        """
        :type: float
        """
    @a90.setter
    def a90(self, arg0: float) -> None:
        pass
    @property
    def c180pi(self) -> float:
        """
        :type: float
        """
    @c180pi.setter
    def c180pi(self, arg0: float) -> None:
        pass
    @property
    def deuxpi(self) -> float:
        """
        :type: float
        """
    @deuxpi.setter
    def deuxpi(self, arg0: float) -> None:
        pass
    @property
    def one(self) -> float:
        """
        :type: float
        """
    @one.setter
    def one(self, arg0: float) -> None:
        pass
    @property
    def pi(self) -> float:
        """
        :type: float
        """
    @pi.setter
    def pi(self, arg0: float) -> None:
        pass
    @property
    def pis180(self) -> float:
        """
        :type: float
        """
    @pis180.setter
    def pis180(self, arg0: float) -> None:
        pass
    @property
    def pisur2(self) -> float:
        """
        :type: float
        """
    @pisur2.setter
    def pisur2(self, arg0: float) -> None:
        pass
    @property
    def zero(self) -> float:
        """
        :type: float
        """
    @zero.setter
    def zero(self, arg0: float) -> None:
        pass
    pass
class minombr_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class mlgdrtl_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class mmapgs0_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class mmapgs1_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class mmapgs2_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class mmapgss_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class mmcmcnp_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class mmjcobi_1_():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class olist():
    """
    None
    """
    def __init__(self) -> None: ...
    @property
    def oerr(self) -> int:
        """
        :type: int
        """
    @oerr.setter
    def oerr(self, arg0: int) -> None:
        pass
    @property
    def ofnmlen(self) -> int:
        """
        :type: int
        """
    @ofnmlen.setter
    def ofnmlen(self, arg0: int) -> None:
        pass
    @property
    def orl(self) -> int:
        """
        :type: int
        """
    @orl.setter
    def orl(self, arg0: int) -> None:
        pass
    @property
    def ounit(self) -> int:
        """
        :type: int
        """
    @ounit.setter
    def ounit(self, arg0: int) -> None:
        pass
    pass
AdvApp2Var_Absolute: OCP.AdvApp2Var.AdvApp2Var_CriterionType # value = <AdvApp2Var_CriterionType.AdvApp2Var_Absolute: 0>
AdvApp2Var_Incremental: OCP.AdvApp2Var.AdvApp2Var_CriterionRepartition # value = <AdvApp2Var_CriterionRepartition.AdvApp2Var_Incremental: 1>
AdvApp2Var_Regular: OCP.AdvApp2Var.AdvApp2Var_CriterionRepartition # value = <AdvApp2Var_CriterionRepartition.AdvApp2Var_Regular: 0>
AdvApp2Var_Relative: OCP.AdvApp2Var.AdvApp2Var_CriterionType # value = <AdvApp2Var_CriterionType.AdvApp2Var_Relative: 1>
