import OCP.BRepBlend
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.Geom2d
import OCP.Law
import OCP.TColgp
import OCP.BlendFunc
import OCP.Adaptor3d
import OCP.Blend
import OCP.NCollection
import OCP.Adaptor2d
import OCP.gp
import OCP.TColStd
import OCP.GeomAbs
import OCP.Approx
import OCP.IntSurf
import OCP.Standard
import OCP.ChFiDS
import OCP.Geom
import OCP.math
import OCP.AppBlend
__all__  = [
"BRepBlend_AppFuncRoot",
"BRepBlend_AppFunc",
"BRepBlend_AppFuncRst",
"BRepBlend_AppFuncRstRst",
"BRepBlend_AppSurf",
"BRepBlend_BlendTool",
"BRepBlend_CSWalking",
"BRepBlend_CurvPointRadInv",
"BRepBlend_Extremity",
"BRepBlend_HCurve2dTool",
"BRepBlend_HCurveTool",
"BRepBlend_Line",
"BRepBlend_PointOnRst",
"BRepBlend_RstRstConstRad",
"BRepBlend_RstRstEvolRad",
"BRepBlend_RstRstLineBuilder",
"BRepBlend_SequenceOfLine",
"BRepBlend_SequenceOfPointOnRst",
"BRepBlend_SurfCurvConstRadInv",
"BRepBlend_SurfCurvEvolRadInv",
"BRepBlend_SurfPointConstRadInv",
"BRepBlend_SurfPointEvolRadInv",
"BRepBlend_SurfRstConstRad",
"BRepBlend_SurfRstEvolRad",
"BRepBlend_SurfRstLineBuilder",
"BRepBlend_Walking"
]
class BRepBlend_AppFuncRoot(OCP.Approx.Approx_SweepFunction, OCP.Standard.Standard_Transient):
    """
    Function to approximate by AppSurfaceFunction to approximate by AppSurfaceFunction to approximate by AppSurface
    """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditionned rational approximation.
        """
    def D0(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param
        """
    def D2(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param
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
        Compute the minimal value of weight for each poles of all sections. This information is usefull to perform well conditionned rational approximation.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
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
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the maximum section. This information is usefull to perform well conditionned rational approximation.
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
    def Point(self,Func : OCP.Blend.Blend_AppFunction,Param : float,Sol : OCP.math.math_Vector,Pnt : OCP.Blend.Blend_Point) -> None: 
        """
        None
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> -- This information is usfull to find an good tolerance in 2d approximation
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
        Is usfull, if (me) have to be run numerical algorithme to perform D0, D1 or D2
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vec(self,Sol : OCP.math.math_Vector,Pnt : OCP.Blend.Blend_Point) -> None: 
        """
        None
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
class BRepBlend_AppFunc(BRepBlend_AppFuncRoot, OCP.Approx.Approx_SweepFunction, OCP.Standard.Standard_Transient):
    """
    Function to approximate by AppSurface for Surface/Surface contact.Function to approximate by AppSurface for Surface/Surface contact.Function to approximate by AppSurface for Surface/Surface contact.
    """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditionned rational approximation.
        """
    def D0(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param
        """
    def D2(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param
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
        Compute the minimal value of weight for each poles of all sections. This information is usefull to perform well conditionned rational approximation.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
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
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the maximum section. This information is usefull to perform well conditionned rational approximation.
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
    def Point(self,Func : OCP.Blend.Blend_AppFunction,Param : float,Sol : OCP.math.math_Vector,Pnt : OCP.Blend.Blend_Point) -> None: 
        """
        None
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> -- This information is usfull to find an good tolerance in 2d approximation
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
        Is usfull, if (me) have to be run numerical algorithme to perform D0, D1 or D2
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vec(self,Sol : OCP.math.math_Vector,Pnt : OCP.Blend.Blend_Point) -> None: 
        """
        None
        """
    def __init__(self,Line : BRepBlend_Line,Func : OCP.Blend.Blend_Function,Tol3d : float,Tol2d : float) -> None: ...
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
class BRepBlend_AppFuncRst(BRepBlend_AppFuncRoot, OCP.Approx.Approx_SweepFunction, OCP.Standard.Standard_Transient):
    """
    Function to approximate by AppSurface for Curve/Surface contact.Function to approximate by AppSurface for Curve/Surface contact.Function to approximate by AppSurface for Curve/Surface contact.
    """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditionned rational approximation.
        """
    def D0(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param
        """
    def D2(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param
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
        Compute the minimal value of weight for each poles of all sections. This information is usefull to perform well conditionned rational approximation.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
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
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the maximum section. This information is usefull to perform well conditionned rational approximation.
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
    def Point(self,Func : OCP.Blend.Blend_AppFunction,Param : float,Sol : OCP.math.math_Vector,Pnt : OCP.Blend.Blend_Point) -> None: 
        """
        None
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> -- This information is usfull to find an good tolerance in 2d approximation
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
        Is usfull, if (me) have to be run numerical algorithme to perform D0, D1 or D2
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vec(self,Sol : OCP.math.math_Vector,Pnt : OCP.Blend.Blend_Point) -> None: 
        """
        None
        """
    def __init__(self,Line : BRepBlend_Line,Func : OCP.Blend.Blend_SurfRstFunction,Tol3d : float,Tol2d : float) -> None: ...
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
class BRepBlend_AppFuncRstRst(BRepBlend_AppFuncRoot, OCP.Approx.Approx_SweepFunction, OCP.Standard.Standard_Transient):
    """
    Function to approximate by AppSurface for Edge/Face (Curve/Curve contact).Function to approximate by AppSurface for Edge/Face (Curve/Curve contact).Function to approximate by AppSurface for Edge/Face (Curve/Curve contact).
    """
    def BarycentreOfSurf(self) -> OCP.gp.gp_Pnt: 
        """
        Get the barycentre of Surface. An very poor estimation is sufficent. This information is usefull to perform well conditionned rational approximation.
        """
    def D0(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the section for v = param
        """
    def D1(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the first derivative in v direction of the section for v = param
        """
    def D2(self,Param : float,First : float,Last : float,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        compute the second derivative in v direction of the section for v = param
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
        Compute the minimal value of weight for each poles of all sections. This information is usefull to perform well conditionned rational approximation.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self,BoundTol : float,SurfTol : float,AngleTol : float,Tol3d : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the tolerance to reach in approximation to respecte BoundTol error at the Boundary AngleTol tangent error at the Boundary (in radian) SurfTol error inside the surface.
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
    def IsRational(self) -> bool: 
        """
        Returns if the section is rationnal or not
        """
    def Knots(self,TKnots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        get the Knots of the section
        """
    def MaximalSection(self) -> float: 
        """
        Returns the length of the maximum section. This information is usefull to perform well conditionned rational approximation.
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
    def Point(self,Func : OCP.Blend.Blend_AppFunction,Param : float,Sol : OCP.math.math_Vector,Pnt : OCP.Blend.Blend_Point) -> None: 
        """
        None
        """
    def Resolution(self,Index : int,Tol : float) -> Tuple[float, float]: 
        """
        Returns the resolutions in the sub-space 2d <Index> -- This information is usfull to find an good tolerance in 2d approximation
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
        Is usfull, if (me) have to be run numerical algorithme to perform D0, D1 or D2
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vec(self,Sol : OCP.math.math_Vector,Pnt : OCP.Blend.Blend_Point) -> None: 
        """
        None
        """
    def __init__(self,Line : BRepBlend_Line,Func : OCP.Blend.Blend_RstRstFunction,Tol3d : float,Tol2d : float) -> None: ...
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
class BRepBlend_AppSurf(OCP.AppBlend.AppBlend_Approx):
    """
    None
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        returns the Continuity used in the approximation
        """
    def CriteriumWeight(self) -> Tuple[float, float, float]: 
        """
        returns the Weights (as percent) associed to the criterium used in the optimization.
        """
    def Curve2d(self,Index : int,TPoles : OCP.TColgp.TColgp_Array1OfPnt2d,TKnots : OCP.TColStd.TColStd_Array1OfReal,TMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def Curve2dPoles(self,Index : int) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        None
        """
    def Curves2dDegree(self) -> int: 
        """
        None
        """
    def Curves2dKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def Curves2dMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def Curves2dShape(self) -> Tuple[int, int, int]: 
        """
        None
        """
    def Init(self,Degmin : int,Degmax : int,Tol3d : float,Tol2d : float,NbIt : int,KnownParameters : bool=False) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbCurves2d(self) -> int: 
        """
        None
        """
    def ParType(self) -> OCP.Approx.Approx_ParametrizationType: 
        """
        returns the type of parametrization used in the approximation
        """
    @overload
    def Perform(self,Lin : BRepBlend_Line,SecGen : OCP.Blend.Blend_AppFunction,NbMaxP : int) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,Lin : BRepBlend_Line,SecGen : OCP.Blend.Blend_AppFunction,SpApprox : bool=False) -> None: ...
    def PerformSmoothing(self,Lin : BRepBlend_Line,SecGen : OCP.Blend.Blend_AppFunction) -> None: 
        """
        None
        """
    def SetContinuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Define the Continuity used in the approximation
        """
    def SetCriteriumWeight(self,W1 : float,W2 : float,W3 : float) -> None: 
        """
        define the Weights associed to the criterium used in the optimization.
        """
    def SetParType(self,ParType : OCP.Approx.Approx_ParametrizationType) -> None: 
        """
        Define the type of parametrization used in the approximation
        """
    def SurfPoles(self) -> OCP.TColgp.TColgp_Array2OfPnt: 
        """
        None
        """
    def SurfShape(self) -> Tuple[int, int, int, int, int, int]: 
        """
        None
        """
    def SurfUKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def SurfUMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def SurfVKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
        """
    def SurfVMults(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def SurfWeights(self) -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        None
        """
    def Surface(self,TPoles : OCP.TColgp.TColgp_Array2OfPnt,TWeights : OCP.TColStd.TColStd_Array2OfReal,TUKnots : OCP.TColStd.TColStd_Array1OfReal,TVKnots : OCP.TColStd.TColStd_Array1OfReal,TUMults : OCP.TColStd.TColStd_Array1OfInteger,TVMults : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def TolCurveOnSurf(self,Index : int) -> float: 
        """
        None
        """
    def TolReached(self) -> Tuple[float, float]: 
        """
        None
        """
    def UDegree(self) -> int: 
        """
        None
        """
    def VDegree(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Degmin : int,Degmax : int,Tol3d : float,Tol2d : float,NbIt : int,KnownParameters : bool=False) -> None: ...
    pass
class BRepBlend_BlendTool():
    """
    None
    """
    @staticmethod
    def Bounds_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> Tuple[float, float]: 
        """
        Returns the parametric limits on the arc C. These limits must be finite : they are either the real limits of the arc, for a finite arc, or a bounding box for an infinite arc.
        """
    @staticmethod
    def CurveOnSurf_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,S : OCP.Adaptor3d.Adaptor3d_HSurface) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        None
        """
    @staticmethod
    def Inters_s(P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor2d.Adaptor2d_HCurve2d,Param : float,Dist : float) -> bool: 
        """
        None
        """
    @staticmethod
    def NbSamplesU_s(S : OCP.Adaptor3d.Adaptor3d_HSurface,u1 : float,u2 : float) -> int: 
        """
        None
        """
    @staticmethod
    def NbSamplesV_s(S : OCP.Adaptor3d.Adaptor3d_HSurface,v1 : float,v2 : float) -> int: 
        """
        None
        """
    @staticmethod
    def Parameter_s(V : OCP.Adaptor3d.Adaptor3d_HVertex,A : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        Returns the parameter of the vertex V on the edge A.
        """
    @staticmethod
    def Project_s(P : OCP.gp.gp_Pnt2d,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor2d.Adaptor2d_HCurve2d,Paramproj : float,Dist : float) -> bool: 
        """
        Projects the point P on the arc C. If the methods returns Standard_True, the projection is successful, and Paramproj is the parameter on the arc of the projected point, Dist is the distance between P and the curve.. If the method returns Standard_False, Param proj and Dist are not significant.
        """
    @staticmethod
    def SingularOnUMax_s(S : OCP.Adaptor3d.Adaptor3d_HSurface) -> bool: 
        """
        None
        """
    @staticmethod
    def SingularOnUMin_s(S : OCP.Adaptor3d.Adaptor3d_HSurface) -> bool: 
        """
        None
        """
    @staticmethod
    def SingularOnVMax_s(S : OCP.Adaptor3d.Adaptor3d_HSurface) -> bool: 
        """
        None
        """
    @staticmethod
    def SingularOnVMin_s(S : OCP.Adaptor3d.Adaptor3d_HSurface) -> bool: 
        """
        None
        """
    @staticmethod
    def Tolerance_s(V : OCP.Adaptor3d.Adaptor3d_HVertex,A : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        Returns the parametric tolerance on the arc A used to consider that the vertex and another point meet, i-e if Abs(Parameter(Vertex)-Parameter(OtherPnt))<= Tolerance, the points are "merged".
        """
    def __init__(self) -> None: ...
    pass
class BRepBlend_CSWalking():
    """
    None
    """
    def Complete(self,F : OCP.Blend.Blend_CSFunction,Pmin : float) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Line(self) -> BRepBlend_Line: 
        """
        None
        """
    def Perform(self,F : OCP.Blend.Blend_CSFunction,Pdep : float,Pmax : float,MaxStep : float,TolGuide : float,Soldep : OCP.math.math_Vector,Tolesp : float,Fleche : float,Appro : bool=False) -> None: 
        """
        None
        """
    def __init__(self,Curv : OCP.Adaptor3d.Adaptor3d_HCurve,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool) -> None: ...
    pass
class BRepBlend_CurvPointRadInv(OCP.Blend.Blend_CurvPointFuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Function of reframing between a point and a curve. valid in cases of constant and progressive radius. This function is used to find a solution on a done point of the curve 1 when using RstRstConsRad or CSConstRad... The vector <X> used in Value, Values and Derivatives methods has to be the vector of the parametric coordinates w, U where w is the parameter on the guide line, U are the parametric coordinates of a point on the partner curve 2.
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
        returns 2.
        """
    def NbVariables(self) -> int: 
        """
        Returns 3.
        """
    @overload
    def Set(self,Choix : int) -> None: 
        """
        None

        Set the Point on which a solution has to be found.
        """
    @overload
    def Set(self,P : OCP.gp.gp_Pnt) -> None: ...
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,C1 : OCP.Adaptor3d.Adaptor3d_HCurve,C2 : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    pass
class BRepBlend_Extremity():
    """
    None
    """
    def AddArc(self,A : OCP.Adaptor2d.Adaptor2d_HCurve2d,Param : float,TLine : OCP.IntSurf.IntSurf_Transition,TArc : OCP.IntSurf.IntSurf_Transition) -> None: 
        """
        Sets the values of a point which is on the arc A, at parameter Param.
        """
    def HasTangent(self) -> bool: 
        """
        Returns TRUE if the Tangent is stored.

        Returns TRUE if the Tangent is stored.
        """
    def IsVertex(self) -> bool: 
        """
        Returns Standard_True when the point coincide with an existing vertex.

        Returns Standard_True when the point coincide with an existing vertex.
        """
    def NbPointOnRst(self) -> int: 
        """
        Returns the number of arc containing the extremity. If the method returns 0, the point is inside the surface. Otherwise, the extremity lies on at least 1 arc, and all the information (arc, parameter, transitions) are given by the point on restriction (PointOnRst) returned by the next method.

        Returns the number of arc containing the extremity. If the method returns 0, the point is inside the surface. Otherwise, the extremity lies on at least 1 arc, and all the information (arc, parameter, transitions) are given by the point on restriction (PointOnRst) returned by the next method.
        """
    def Parameter(self) -> float: 
        """
        None

        None
        """
    def ParameterOnGuide(self) -> float: 
        """
        None

        None
        """
    def Parameters(self) -> Tuple[float, float]: 
        """
        This method returns the parameters of the point on the concerned surface.

        This method returns the parameters of the point on the concerned surface.
        """
    def PointOnRst(self,Index : int) -> BRepBlend_PointOnRst: 
        """
        None

        None
        """
    def SetTangent(self,Tangent : OCP.gp.gp_Vec) -> None: 
        """
        Set the tangent vector for an extremity on a surface.

        Set the tangent vector for an extremity on a surface.
        """
    @overload
    def SetValue(self,P : OCP.gp.gp_Pnt,W : float,Param : float,Tol : float) -> None: 
        """
        Set the values for an extremity on a surface.

        Set the values for an extremity on a surface.This extremity matches the vertex <Vtx>.

        Set the values for an extremity on curve.
        """
    @overload
    def SetValue(self,P : OCP.gp.gp_Pnt,U : float,V : float,Param : float,Tol : float,Vtx : OCP.Adaptor3d.Adaptor3d_HVertex) -> None: ...
    @overload
    def SetValue(self,P : OCP.gp.gp_Pnt,U : float,V : float,Param : float,Tol : float) -> None: ...
    def SetVertex(self,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> None: 
        """
        Set the values for an extremity on a curve.
        """
    def Tangent(self) -> OCP.gp.gp_Vec: 
        """
        This method returns the value of tangent in 3d space.

        This method returns the value of tangent in 3d space.
        """
    def Tolerance(self) -> float: 
        """
        This method returns the fuzziness on the point in 3d space.

        This method returns the fuzziness on the point in 3d space.
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        This method returns the value of the point in 3d space.

        This method returns the value of the point in 3d space.
        """
    def Vertex(self) -> OCP.Adaptor3d.Adaptor3d_HVertex: 
        """
        Returns the vertex when IsVertex returns Standard_True.

        Returns the vertex when IsVertex returns Standard_True.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,U : float,V : float,Param : float,Tol : float,Vtx : OCP.Adaptor3d.Adaptor3d_HVertex) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,U : float,V : float,Param : float,Tol : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,W : float,Param : float,Tol : float) -> None: ...
    pass
class BRepBlend_HCurve2dTool():
    """
    None
    """
    @staticmethod
    def BSpline_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Circ2d: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Computes the point of parameter U on the curve.
        """
    @staticmethod
    def D1_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    @staticmethod
    def D2_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    @staticmethod
    def D3_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    @staticmethod
    def DN_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    @staticmethod
    def Ellipse_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Elips2d: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Hyperbola_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Hypr2d: 
        """
        None
        """
    @staticmethod
    def Intervals_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def IsClosed_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPeriodic_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> bool: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(myclass) >= <S>
        """
    @staticmethod
    def NbSamples_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U0 : float,U1 : float) -> int: 
        """
        None
        """
    @staticmethod
    def Parabola_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @staticmethod
    def Period_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> float: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor2d.Adaptor2d_HCurve2d,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self) -> None: ...
    pass
class BRepBlend_HCurveTool():
    """
    None
    """
    @staticmethod
    def BSpline_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> OCP.Geom.Geom_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> OCP.gp.gp_Circ: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U on the curve.
        """
    @staticmethod
    def D1_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,U : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    @staticmethod
    def D2_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    @staticmethod
    def D3_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    @staticmethod
    def DN_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    @staticmethod
    def Ellipse_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> OCP.gp.gp_Elips: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Hyperbola_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> OCP.gp.gp_Hypr: 
        """
        None
        """
    @staticmethod
    def Intervals_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def IsClosed_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPeriodic_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> bool: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> OCP.gp.gp_Lin: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(myclass) >= <S>
        """
    @staticmethod
    def NbSamples_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,U0 : float,U1 : float) -> int: 
        """
        None
        """
    @staticmethod
    def Parabola_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> OCP.gp.gp_Parab: 
        """
        None
        """
    @staticmethod
    def Period_s(C : OCP.Adaptor3d.Adaptor3d_HCurve) -> float: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor3d.Adaptor3d_HCurve,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self) -> None: ...
    pass
class BRepBlend_Line(OCP.Standard.Standard_Transient):
    def Append(self,P : OCP.Blend.Blend_Point) -> None: 
        """
        Adds a point in the line.

        Adds a point in the line.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the line.
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
    def EndPointOnFirst(self) -> BRepBlend_Extremity: 
        """
        Returns the end point on S1.

        Returns the end point on S1.
        """
    def EndPointOnSecond(self) -> BRepBlend_Extremity: 
        """
        Returns the point on S2.

        Returns the point on S2.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InsertBefore(self,Index : int,P : OCP.Blend.Blend_Point) -> None: 
        """
        Adds a point in the line at the first place.

        Adds a point in the line at the first place.
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
    def NbPoints(self) -> int: 
        """
        Returns the number of points in the line.

        Returns the number of points in the line.
        """
    def Point(self,Index : int) -> OCP.Blend.Blend_Point: 
        """
        Returns the point of range Index.

        Returns the point of range Index.
        """
    def Prepend(self,P : OCP.Blend.Blend_Point) -> None: 
        """
        Adds a point in the line at the first place.

        Adds a point in the line at the first place.
        """
    def Remove(self,FromIndex : int,ToIndex : int) -> None: 
        """
        Removes from <me> all the items of positions between <FromIndex> and <ToIndex>. Raises an exception if the indices are out of bounds.

        Removes from <me> all the items of positions between <FromIndex> and <ToIndex>. Raises an exception if the indices are out of bounds.
        """
    @overload
    def Set(self,Trans : OCP.IntSurf.IntSurf_TypeTrans) -> None: 
        """
        Sets the value of the transition of the line on S1 and the line on S2.

        Sets the value of the transition of the line on a surface
        """
    @overload
    def Set(self,TranS1 : OCP.IntSurf.IntSurf_TypeTrans,TranS2 : OCP.IntSurf.IntSurf_TypeTrans) -> None: ...
    @overload
    def SetEndPoints(self,EndPtOnS1 : BRepBlend_Extremity,EndPtOnS2 : BRepBlend_Extremity) -> None: 
        """
        Sets tne values of the end points for the line.

        Sets tne values of the end points for the line.
        """
    @overload
    def SetEndPoints(self,EndPt1 : BRepBlend_Extremity,EndPt2 : BRepBlend_Extremity) -> None: ...
    @overload
    def SetStartPoints(self,StartPt1 : BRepBlend_Extremity,StartPt2 : BRepBlend_Extremity) -> None: 
        """
        Sets the values of the start points for the line.

        Sets the values of the start points for the line.
        """
    @overload
    def SetStartPoints(self,StartPtOnS1 : BRepBlend_Extremity,StartPtOnS2 : BRepBlend_Extremity) -> None: ...
    def StartPointOnFirst(self) -> BRepBlend_Extremity: 
        """
        Returns the start point on S1.

        Returns the start point on S1.
        """
    def StartPointOnSecond(self) -> BRepBlend_Extremity: 
        """
        Returns the start point on S2

        Returns the start point on S2
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransitionOnS(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line defined on the surface.

        Returns the type of the transition of the line defined on the surface.
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line defined on the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vectors (N,DRac,T) is right-handed, where N is the normal to the first surface at a point P, DRac is a vector tangent to the blending patch, oriented towards the valid part of this patch, T is the tangent to the line on S1 at P. The transitioon is OUT when the system of vectors is left-handed.

        Returns the type of the transition of the line defined on the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vectors (N,DRac,T) is right-handed, where N is the normal to the first surface at a point P, DRac is a vector tangent to the blending patch, oriented towards the valid part of this patch, T is the tangent to the line on S1 at P. The transitioon is OUT when the system of vectors is left-handed.
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line defined on the second surface. The transition is "constant" along the line.

        Returns the type of the transition of the line defined on the second surface. The transition is "constant" along the line.
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
class BRepBlend_PointOnRst():
    """
    Definition of an intersection point between a line and a restriction on a surface. Such a point is contains geometrical informations (see the Value method) and logical informations.
    """
    def Arc(self) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        Returns the arc of restriction containing the vertex.

        Returns the arc of restriction containing the vertex.
        """
    def ParameterOnArc(self) -> float: 
        """
        Returns the parameter of the point on the arc returned by the method Arc().

        Returns the parameter of the point on the arc returned by the method Arc().
        """
    def SetArc(self,A : OCP.Adaptor2d.Adaptor2d_HCurve2d,Param : float,TLine : OCP.IntSurf.IntSurf_Transition,TArc : OCP.IntSurf.IntSurf_Transition) -> None: 
        """
        Sets the values of a point which is on the arc A, at parameter Param.
        """
    def TransitionOnArc(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        Returns the transition of the point on the arc returned by Arc().

        Returns the transition of the point on the arc returned by Arc().
        """
    def TransitionOnLine(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        Returns the transition of the point on the line on surface.

        Returns the transition of the point on the line on surface.
        """
    @overload
    def __init__(self,A : OCP.Adaptor2d.Adaptor2d_HCurve2d,Param : float,TLine : OCP.IntSurf.IntSurf_Transition,TArc : OCP.IntSurf.IntSurf_Transition) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepBlend_RstRstConstRad(OCP.Blend.Blend_RstRstFunction, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Copy of CSConstRad with a pcurve on surface as support.
    """
    def CenterCircleRst1Rst2(self,PtRst1 : OCP.gp.gp_Pnt,PtRst2 : OCP.gp.gp_Pnt,np : OCP.gp.gp_Vec,Center : OCP.gp.gp_Pnt,VdMed : OCP.gp.gp_Vec) -> bool: 
        """
        Give the center of circle define by PtRst1, PtRst2 and radius ray.
        """
    def Decroch(self,Sol : OCP.math.math_Vector,NRst1 : OCP.gp.gp_Vec,TgRst1 : OCP.gp.gp_Vec,NRst2 : OCP.gp.gp_Vec,TgRst2 : OCP.gp.gp_Vec) -> OCP.Blend.Blend_DecrochStatus: 
        """
        Permet d ' implementer un critere de decrochage specifique a la fonction.
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
        Returns the minimal Distance beetween two extremitys of calculed sections.
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
        Stores in <T> the parameters bounding the intervals of continuity <S>. The array must provide enough room to accomodate for the parameters. i.e. T.Length() > NbIntervals()
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
        Returns 2.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 2.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
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
        None
        """
    def PointOnRst2(self) -> OCP.gp.gp_Pnt: 
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

        None

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Section(self,Param : float,U : float,V : float,C : OCP.gp.gp_Circ) -> Tuple[float, float]: ...
    @overload
    def Set(self,Param : float) -> None: 
        """
        None

        None

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.

        None

        Sets the type of section generation for the approximations.
        """
    @overload
    def Set(self,SurfRef1 : OCP.Adaptor3d.Adaptor3d_HSurface,RstRef1 : OCP.Adaptor2d.Adaptor2d_HCurve2d,SurfRef2 : OCP.Adaptor3d.Adaptor3d_HSurface,RstRef2 : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> None: ...
    @overload
    def Set(self,Radius : float,Choix : int) -> None: ...
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    @overload
    def Set(self,TypeSection : OCP.BlendFunc.BlendFunc_SectionShape) -> None: ...
    def Tangent2dOnRst1(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnRst2(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnRst1(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnRst2(self) -> OCP.gp.gp_Vec: 
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
    def __init__(self,Surf1 : OCP.Adaptor3d.Adaptor3d_HSurface,Rst1 : OCP.Adaptor2d.Adaptor2d_HCurve2d,Surf2 : OCP.Adaptor3d.Adaptor3d_HSurface,Rst2 : OCP.Adaptor2d.Adaptor2d_HCurve2d,CGuide : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    pass
class BRepBlend_RstRstEvolRad(OCP.Blend.Blend_RstRstFunction, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Function to approximate by AppSurface for Edge/Edge and evolutif radius
    """
    def CenterCircleRst1Rst2(self,PtRst1 : OCP.gp.gp_Pnt,PtRst2 : OCP.gp.gp_Pnt,np : OCP.gp.gp_Vec,Center : OCP.gp.gp_Pnt,VdMed : OCP.gp.gp_Vec) -> bool: 
        """
        Gives the center of circle defined by PtRst1, PtRst2 and radius ray.
        """
    def Decroch(self,Sol : OCP.math.math_Vector,NRst1 : OCP.gp.gp_Vec,TgRst1 : OCP.gp.gp_Vec,NRst2 : OCP.gp.gp_Vec,TgRst2 : OCP.gp.gp_Vec) -> OCP.Blend.Blend_DecrochStatus: 
        """
        Enables implementation of a criterion of decrochage specific to the function.
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
        Returns the minimal Distance beetween two extremitys of calculed sections.
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
        Stores in <T> the parameters bounding the intervals of continuity <S>. The array must provide enough room to accomodate for the parameters. i.e. T.Length() > NbIntervals()
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
        Returns 2.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 2.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
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
        None
        """
    def PointOnRst2(self) -> OCP.gp.gp_Pnt: 
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

        None

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,Param : float,U : float,V : float,C : OCP.gp.gp_Circ) -> Tuple[float, float]: ...
    @overload
    def Set(self,Param : float) -> None: 
        """
        None

        None

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.

        None

        Sets the type of section generation for the approximations.
        """
    @overload
    def Set(self,TypeSection : OCP.BlendFunc.BlendFunc_SectionShape) -> None: ...
    @overload
    def Set(self,SurfRef1 : OCP.Adaptor3d.Adaptor3d_HSurface,RstRef1 : OCP.Adaptor2d.Adaptor2d_HCurve2d,SurfRef2 : OCP.Adaptor3d.Adaptor3d_HSurface,RstRef2 : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> None: ...
    @overload
    def Set(self,Choix : int) -> None: ...
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    def Tangent2dOnRst1(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnRst2(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnRst1(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def TangentOnRst2(self) -> OCP.gp.gp_Vec: 
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
    def __init__(self,Surf1 : OCP.Adaptor3d.Adaptor3d_HSurface,Rst1 : OCP.Adaptor2d.Adaptor2d_HCurve2d,Surf2 : OCP.Adaptor3d.Adaptor3d_HSurface,Rst2 : OCP.Adaptor2d.Adaptor2d_HCurve2d,CGuide : OCP.Adaptor3d.Adaptor3d_HCurve,Evol : OCP.Law.Law_Function) -> None: ...
    pass
class BRepBlend_RstRstLineBuilder():
    """
    This class processes the data resulting from Blend_CSWalking but it takes in consideration the Surface supporting the curve to detect the breakpoint.
    """
    def Complete(self,Func : OCP.Blend.Blend_RstRstFunction,Finv1 : OCP.Blend.Blend_SurfCurvFuncInv,FinvP1 : OCP.Blend.Blend_CurvPointFuncInv,Finv2 : OCP.Blend.Blend_SurfCurvFuncInv,FinvP2 : OCP.Blend.Blend_CurvPointFuncInv,Pmin : float) -> bool: 
        """
        None
        """
    def Decroch1End(self) -> bool: 
        """
        None

        None
        """
    def Decroch1Start(self) -> bool: 
        """
        None

        None
        """
    def Decroch2End(self) -> bool: 
        """
        None

        None
        """
    def Decroch2Start(self) -> bool: 
        """
        None

        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def Line(self) -> BRepBlend_Line: 
        """
        None

        None
        """
    def Perform(self,Func : OCP.Blend.Blend_RstRstFunction,Finv1 : OCP.Blend.Blend_SurfCurvFuncInv,FinvP1 : OCP.Blend.Blend_CurvPointFuncInv,Finv2 : OCP.Blend.Blend_SurfCurvFuncInv,FinvP2 : OCP.Blend.Blend_CurvPointFuncInv,Pdep : float,Pmax : float,MaxStep : float,TolGuide : float,Soldep : OCP.math.math_Vector,Tolesp : float,Fleche : float,Appro : bool=False) -> None: 
        """
        None
        """
    def PerformFirstSection(self,Func : OCP.Blend.Blend_RstRstFunction,Finv1 : OCP.Blend.Blend_SurfCurvFuncInv,FinvP1 : OCP.Blend.Blend_CurvPointFuncInv,Finv2 : OCP.Blend.Blend_SurfCurvFuncInv,FinvP2 : OCP.Blend.Blend_CurvPointFuncInv,Pdep : float,Pmax : float,Soldep : OCP.math.math_Vector,Tolesp : float,TolGuide : float,RecRst1 : bool,RecP1 : bool,RecRst2 : bool,RecP2 : bool,Psol : float,ParSol : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def __init__(self,Surf1 : OCP.Adaptor3d.Adaptor3d_HSurface,Rst1 : OCP.Adaptor2d.Adaptor2d_HCurve2d,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Surf2 : OCP.Adaptor3d.Adaptor3d_HSurface,Rst2 : OCP.Adaptor2d.Adaptor2d_HCurve2d,Domain2 : OCP.Adaptor3d.Adaptor3d_TopolTool) -> None: ...
    pass
class BRepBlend_SequenceOfLine(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BRepBlend_Line) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : BRepBlend_SequenceOfLine) -> None: ...
    def Assign(self,theOther : BRepBlend_SequenceOfLine) -> BRepBlend_SequenceOfLine: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> BRepBlend_Line: 
        """
        First item access
        """
    def ChangeLast(self) -> BRepBlend_Line: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> BRepBlend_Line: 
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
    def First(self) -> BRepBlend_Line: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : BRepBlend_Line) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : BRepBlend_SequenceOfLine) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : BRepBlend_Line) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : BRepBlend_SequenceOfLine) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BRepBlend_Line: 
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
    def Prepend(self,theItem : BRepBlend_Line) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : BRepBlend_SequenceOfLine) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : BRepBlend_Line) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : BRepBlend_SequenceOfLine) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BRepBlend_Line: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : BRepBlend_SequenceOfLine) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class BRepBlend_SequenceOfPointOnRst(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BRepBlend_PointOnRst) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : BRepBlend_SequenceOfPointOnRst) -> None: ...
    def Assign(self,theOther : BRepBlend_SequenceOfPointOnRst) -> BRepBlend_SequenceOfPointOnRst: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> BRepBlend_PointOnRst: 
        """
        First item access
        """
    def ChangeLast(self) -> BRepBlend_PointOnRst: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> BRepBlend_PointOnRst: 
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
    def First(self) -> BRepBlend_PointOnRst: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : BRepBlend_SequenceOfPointOnRst) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : BRepBlend_PointOnRst) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : BRepBlend_SequenceOfPointOnRst) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : BRepBlend_PointOnRst) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BRepBlend_PointOnRst: 
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
    def Prepend(self,theItem : BRepBlend_PointOnRst) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : BRepBlend_SequenceOfPointOnRst) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : BRepBlend_PointOnRst) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : BRepBlend_SequenceOfPointOnRst) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BRepBlend_PointOnRst: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : BRepBlend_SequenceOfPointOnRst) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class BRepBlend_SurfCurvConstRadInv(OCP.Blend.Blend_SurfCurvFuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Function of reframing between a restriction surface of the surface and a curve. Class used to compute a solution of the surfRstConstRad problem on a done restriction of the surface. The vector <X> used in Value, Values and Derivatives methods has to be the vector of the parametric coordinates wguide, wcurv, wrst where wguide is the parameter on the guide line, wcurv is the parameter on the curve, wrst is the parameter on the restriction on the surface.
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
        returns 3.
        """
    def NbVariables(self) -> int: 
        """
        Returns 3.
        """
    @overload
    def Set(self,R : float,Choix : int) -> None: 
        """
        None

        Set the restriction on which a solution has to be found.
        """
    @overload
    def Set(self,Rst : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> None: ...
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve,Cg : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    pass
class BRepBlend_SurfCurvEvolRadInv(OCP.Blend.Blend_SurfCurvFuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Function of reframing between a surface restriction of the surface and a curve. Class used to compute a solution of the surfRstConstRad problem on a done restriction of the surface. The vector <X> used in Value, Values and Derivatives methods has to be the vector of the parametric coordinates wguide, wcurv, wrst where wguide is the parameter on the guide line, wcurv is the parameter on the curve, wrst is the parameter on the restriction on the surface.
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
        returns 3.
        """
    def NbVariables(self) -> int: 
        """
        Returns 3.
        """
    @overload
    def Set(self,Rst : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> None: 
        """
        None

        Set the restriction on which a solution has to be found.
        """
    @overload
    def Set(self,Choix : int) -> None: ...
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve,Cg : OCP.Adaptor3d.Adaptor3d_HCurve,Evol : OCP.Law.Law_Function) -> None: ...
    pass
class BRepBlend_SurfPointConstRadInv(OCP.Blend.Blend_SurfPointFuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Function of reframing between a point and a surface. This function is used to find a solution on a done point of the curve when using SurfRstConsRad or CSConstRad... The vector <X> used in Value, Values and Derivatives methods has to be the vector of the parametric coordinates w, U, V where w is the parameter on the guide line, U,V are the parametric coordinates of a point on the partner surface.
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
        returns 3.
        """
    def NbVariables(self) -> int: 
        """
        Returns 3.
        """
    @overload
    def Set(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        None

        Set the Point on which a solution has to be found.
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
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    pass
class BRepBlend_SurfPointEvolRadInv(OCP.Blend.Blend_SurfPointFuncInv, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Function of reframing between a point and a surface. This function is used to find a solution on a done point of the curve when using SurfRstConsRad or CSConstRad... The vector <X> used in Value, Values and Derivatives methods has to be the vector of the parametric coordinates w, U, V where w is the parameter on the guide line, U,V are the parametric coordinates of a point on the partner surface.
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
        returns 3.
        """
    def NbVariables(self) -> int: 
        """
        Returns 3.
        """
    @overload
    def Set(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        None

        Set the Point on which a solution has to be found.
        """
    @overload
    def Set(self,Choix : int) -> None: ...
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the Functions for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        returns the values <F> of the functions and the derivatives <D> for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve,Evol : OCP.Law.Law_Function) -> None: ...
    pass
class BRepBlend_SurfRstConstRad(OCP.Blend.Blend_SurfRstFunction, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Copy of CSConstRad with pcurve on surface as support.
    """
    def Decroch(self,Sol : OCP.math.math_Vector,NS : OCP.gp.gp_Vec,TgS : OCP.gp.gp_Vec) -> bool: 
        """
        Enables implementation of a criterion of decrochage specific to the function. Warning: Can be called without previous call of issolution but the values calculated can be senseless.
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
        Returns the minimal Distance beetween two extremitys of calculed sections.
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
        Stores in <T> the parameters bounding the intervals of continuity <S>. The array must provide enough room to accomodate for the parameters. i.e. T.Length() > NbIntervals()
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
        Returns 3.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 3.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
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
        Used for the first and last section

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

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
    def Set(self,Radius : float,Choix : int) -> None: 
        """
        None

        None

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.

        None

        Sets the type of section generation for the approximations.
        """
    @overload
    def Set(self,Param : float) -> None: ...
    @overload
    def Set(self,TypeSection : OCP.BlendFunc.BlendFunc_SectionShape) -> None: ...
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    @overload
    def Set(self,SurfRef : OCP.Adaptor3d.Adaptor3d_HSurface,RstRef : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> None: ...
    def Tangent2dOnRst(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnS(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnRst(self) -> OCP.gp.gp_Vec: 
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
    def __init__(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,SurfRst : OCP.Adaptor3d.Adaptor3d_HSurface,Rst : OCP.Adaptor2d.Adaptor2d_HCurve2d,CGuide : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    pass
class BRepBlend_SurfRstEvolRad(OCP.Blend.Blend_SurfRstFunction, OCP.Blend.Blend_AppFunction, OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    Function to approximate by AppSurface for Edge/Face and evolutif radius
    """
    def Decroch(self,Sol : OCP.math.math_Vector,NS : OCP.gp.gp_Vec,TgS : OCP.gp.gp_Vec) -> bool: 
        """
        Permet d ' implementer un critere de decrochage specifique a la fonction.
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
        Returns the minimal Distance beetween two extremitys of calculed sections.
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
        Stores in <T> the parameters bounding the intervals of continuity <S>. The array must provide enough room to accomodate for the parameters. i.e. T.Length() > NbIntervals()
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
        Returns 3.
        """
    def NbIntervals(self,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    def NbVariables(self) -> int: 
        """
        Returns 3.
        """
    def Parameter(self,P : OCP.Blend.Blend_Point) -> float: 
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
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Used for the first and last section

        Used for the first and last section The method returns Standard_True if the derivatives are computed, otherwise it returns Standard_False.

        None

        None
        """
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,DPoles : OCP.TColgp.TColgp_Array1OfVec,D2Poles : OCP.TColgp.TColgp_Array1OfVec,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,DPoles2d : OCP.TColgp.TColgp_Array1OfVec2d,D2Poles2d : OCP.TColgp.TColgp_Array1OfVec2d,Weigths : OCP.TColStd.TColStd_Array1OfReal,DWeigths : OCP.TColStd.TColStd_Array1OfReal,D2Weigths : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    @overload
    def Section(self,Param : float,U : float,V : float,W : float,C : OCP.gp.gp_Circ) -> Tuple[float, float]: ...
    @overload
    def Section(self,P : OCP.Blend.Blend_Point,Poles : OCP.TColgp.TColgp_Array1OfPnt,Poles2d : OCP.TColgp.TColgp_Array1OfPnt2d,Weigths : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Set(self,Choix : int) -> None: 
        """
        None

        None

        Sets the bounds of the parametric interval on the guide line. This determines the derivatives in these values if the function is not Cn.

        None

        Sets the type of section generation for the approximations.
        """
    @overload
    def Set(self,First : float,Last : float) -> None: ...
    @overload
    def Set(self,Param : float) -> None: ...
    @overload
    def Set(self,TypeSection : OCP.BlendFunc.BlendFunc_SectionShape) -> None: ...
    @overload
    def Set(self,SurfRef : OCP.Adaptor3d.Adaptor3d_HSurface,RstRef : OCP.Adaptor2d.Adaptor2d_HCurve2d) -> None: ...
    def Tangent2dOnRst(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Tangent2dOnS(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def TangentOnRst(self) -> OCP.gp.gp_Vec: 
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
    def __init__(self,Surf : OCP.Adaptor3d.Adaptor3d_HSurface,SurfRst : OCP.Adaptor3d.Adaptor3d_HSurface,Rst : OCP.Adaptor2d.Adaptor2d_HCurve2d,CGuide : OCP.Adaptor3d.Adaptor3d_HCurve,Evol : OCP.Law.Law_Function) -> None: ...
    pass
class BRepBlend_SurfRstLineBuilder():
    """
    This class processes data resulting from Blend_CSWalking taking in consideration the Surface supporting the curve to detect the breakpoint.
    """
    def ArcToRecadre(self,Sol : OCP.math.math_Vector,PrevIndex : int,pt2d : OCP.gp.gp_Pnt2d,lastpt2d : OCP.gp.gp_Pnt2d,ponarc : float) -> int: 
        """
        None
        """
    def Complete(self,Func : OCP.Blend.Blend_SurfRstFunction,Finv : OCP.Blend.Blend_FuncInv,FinvP : OCP.Blend.Blend_SurfPointFuncInv,FinvC : OCP.Blend.Blend_SurfCurvFuncInv,Pmin : float) -> bool: 
        """
        None
        """
    def DecrochEnd(self) -> bool: 
        """
        None

        None
        """
    def DecrochStart(self) -> bool: 
        """
        None

        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def Line(self) -> BRepBlend_Line: 
        """
        None

        None
        """
    def Perform(self,Func : OCP.Blend.Blend_SurfRstFunction,Finv : OCP.Blend.Blend_FuncInv,FinvP : OCP.Blend.Blend_SurfPointFuncInv,FinvC : OCP.Blend.Blend_SurfCurvFuncInv,Pdep : float,Pmax : float,MaxStep : float,TolGuide : float,Soldep : OCP.math.math_Vector,Tolesp : float,Fleche : float,Appro : bool=False) -> None: 
        """
        None
        """
    def PerformFirstSection(self,Func : OCP.Blend.Blend_SurfRstFunction,Finv : OCP.Blend.Blend_FuncInv,FinvP : OCP.Blend.Blend_SurfPointFuncInv,FinvC : OCP.Blend.Blend_SurfCurvFuncInv,Pdep : float,Pmax : float,Soldep : OCP.math.math_Vector,Tolesp : float,TolGuide : float,RecRst : bool,RecP : bool,RecS : bool,Psol : float,ParSol : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def __init__(self,Surf1 : OCP.Adaptor3d.Adaptor3d_HSurface,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Surf2 : OCP.Adaptor3d.Adaptor3d_HSurface,Rst : OCP.Adaptor2d.Adaptor2d_HCurve2d,Domain2 : OCP.Adaptor3d.Adaptor3d_TopolTool) -> None: ...
    pass
class BRepBlend_Walking():
    """
    None
    """
    def AddSingularPoint(self,P : OCP.Blend.Blend_Point) -> None: 
        """
        To define singular points computed before walking.
        """
    def Check(self,C : bool) -> None: 
        """
        None
        """
    def Check2d(self,C : bool) -> None: 
        """
        None
        """
    def ClassificationOnS1(self,C : bool) -> None: 
        """
        None
        """
    def ClassificationOnS2(self,C : bool) -> None: 
        """
        None
        """
    def Complete(self,F : OCP.Blend.Blend_Function,FInv : OCP.Blend.Blend_FuncInv,Pmin : float) -> bool: 
        """
        None
        """
    @overload
    def Continu(self,F : OCP.Blend.Blend_Function,FInv : OCP.Blend.Blend_FuncInv,P : float) -> bool: 
        """
        None

        None
        """
    @overload
    def Continu(self,F : OCP.Blend.Blend_Function,FInv : OCP.Blend.Blend_FuncInv,P : float,OnS1 : bool) -> bool: ...
    def IsDone(self) -> bool: 
        """
        None
        """
    def Line(self) -> BRepBlend_Line: 
        """
        None
        """
    def Perform(self,F : OCP.Blend.Blend_Function,FInv : OCP.Blend.Blend_FuncInv,Pdep : float,Pmax : float,MaxStep : float,TolGuide : float,Soldep : OCP.math.math_Vector,Tolesp : float,Fleche : float,Appro : bool=False) -> None: 
        """
        None
        """
    @overload
    def PerformFirstSection(self,F : OCP.Blend.Blend_Function,FInv : OCP.Blend.Blend_FuncInv,Pdep : float,Pmax : float,ParDep : OCP.math.math_Vector,Tolesp : float,TolGuide : float,RecOnS1 : bool,RecOnS2 : bool,Psol : float,ParSol : OCP.math.math_Vector) -> bool: 
        """
        None

        None
        """
    @overload
    def PerformFirstSection(self,F : OCP.Blend.Blend_Function,Pdep : float,ParDep : OCP.math.math_Vector,Tolesp : float,TolGuide : float,Pos1 : OCP.TopAbs.TopAbs_State,Pos2 : OCP.TopAbs.TopAbs_State) -> bool: ...
    def SetDomainsToRecadre(self,RecDomain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,RecDomain2 : OCP.Adaptor3d.Adaptor3d_TopolTool) -> None: 
        """
        To define different domains for control and clipping.
        """
    def TwistOnS1(self) -> bool: 
        """
        None
        """
    def TwistOnS2(self) -> bool: 
        """
        None
        """
    def __init__(self,Surf1 : OCP.Adaptor3d.Adaptor3d_HSurface,Surf2 : OCP.Adaptor3d.Adaptor3d_HSurface,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Domain2 : OCP.Adaptor3d.Adaptor3d_TopolTool,HGuide : OCP.ChFiDS.ChFiDS_HElSpine) -> None: ...
    pass
