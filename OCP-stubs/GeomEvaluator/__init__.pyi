import OCP.GeomEvaluator
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.GeomAdaptor
import OCP.gp
import OCP.Geom
import OCP.Standard
__all__  = [
"GeomEvaluator_Curve",
"GeomEvaluator_OffsetCurve",
"GeomEvaluator_Surface",
"GeomEvaluator_OffsetSurface",
"GeomEvaluator_SurfaceOfExtrusion",
"GeomEvaluator_SurfaceOfRevolution"
]
class GeomEvaluator_Curve(OCP.Standard.Standard_Transient):
    """
    Interface for calculation of values and derivatives for different kinds of curves in 3D. Works both with adaptors and curves.Interface for calculation of values and derivatives for different kinds of curves in 3D. Works both with adaptors and curves.
    """
    def D0(self,theU : float,theValue : OCP.gp.gp_Pnt) -> None: 
        """
        Value of 3D curve
        """
    def D1(self,theU : float,theValue : OCP.gp.gp_Pnt,theD1 : OCP.gp.gp_Vec) -> None: 
        """
        Value and first derivatives of curve
        """
    def D2(self,theU : float,theValue : OCP.gp.gp_Pnt,theD1 : OCP.gp.gp_Vec,theD2 : OCP.gp.gp_Vec) -> None: 
        """
        Value, first and second derivatives of curve
        """
    def D3(self,theU : float,theValue : OCP.gp.gp_Pnt,theD1 : OCP.gp.gp_Vec,theD2 : OCP.gp.gp_Vec,theD3 : OCP.gp.gp_Vec) -> None: 
        """
        Value, first, second and third derivatives of curve
        """
    def DN(self,theU : float,theDerU : int) -> OCP.gp.gp_Vec: 
        """
        Calculates N-th derivatives of curve, where N = theDerU. Raises if N < 1
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class GeomEvaluator_OffsetCurve(GeomEvaluator_Curve, OCP.Standard.Standard_Transient):
    """
    Allows to calculate values and derivatives for offset curves in 3DAllows to calculate values and derivatives for offset curves in 3D
    """
    def D0(self,theU : float,theValue : OCP.gp.gp_Pnt) -> None: 
        """
        Value of curve
        """
    def D1(self,theU : float,theValue : OCP.gp.gp_Pnt,theD1 : OCP.gp.gp_Vec) -> None: 
        """
        Value and first derivatives of curve
        """
    def D2(self,theU : float,theValue : OCP.gp.gp_Pnt,theD1 : OCP.gp.gp_Vec,theD2 : OCP.gp.gp_Vec) -> None: 
        """
        Value, first and second derivatives of curve
        """
    def D3(self,theU : float,theValue : OCP.gp.gp_Pnt,theD1 : OCP.gp.gp_Vec,theD2 : OCP.gp.gp_Vec,theD3 : OCP.gp.gp_Vec) -> None: 
        """
        Value, first, second and third derivatives of curve
        """
    def DN(self,theU : float,theDeriv : int) -> OCP.gp.gp_Vec: 
        """
        Calculates N-th derivatives of curve, where N = theDeriv. Raises if N < 1
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
    def SetOffsetDirection(self,theDirection : OCP.gp.gp_Dir) -> None: 
        """
        None
        """
    def SetOffsetValue(self,theOffset : float) -> None: 
        """
        Change the offset value
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theBase : OCP.GeomAdaptor.GeomAdaptor_HCurve,theOffset : float,theDirection : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,theBase : OCP.Geom.Geom_Curve,theOffset : float,theDirection : OCP.gp.gp_Dir) -> None: ...
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
class GeomEvaluator_Surface(OCP.Standard.Standard_Transient):
    """
    Interface for calculation of values and derivatives for different kinds of surfaces. Works both with adaptors and surfaces.Interface for calculation of values and derivatives for different kinds of surfaces. Works both with adaptors and surfaces.
    """
    def D0(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt) -> None: 
        """
        Value of surface
        """
    def D1(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec) -> None: 
        """
        Value and first derivatives of surface
        """
    def D2(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec) -> None: 
        """
        Value, first and second derivatives of surface
        """
    def D3(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec,theD3U : OCP.gp.gp_Vec,theD3V : OCP.gp.gp_Vec,theD3UUV : OCP.gp.gp_Vec,theD3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Value, first, second and third derivatives of surface
        """
    def DN(self,theU : float,theV : float,theDerU : int,theDerV : int) -> OCP.gp.gp_Vec: 
        """
        Calculates N-th derivatives of surface, where N = theDerU + theDerV.
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class GeomEvaluator_OffsetSurface(GeomEvaluator_Surface, OCP.Standard.Standard_Transient):
    """
    Allows to calculate values and derivatives for offset surfacesAllows to calculate values and derivatives for offset surfaces
    """
    def D0(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt) -> None: 
        """
        Value of surface
        """
    def D1(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec) -> None: 
        """
        Value and first derivatives of surface
        """
    def D2(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec) -> None: 
        """
        Value, first and second derivatives of surface
        """
    def D3(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec,theD3U : OCP.gp.gp_Vec,theD3V : OCP.gp.gp_Vec,theD3UUV : OCP.gp.gp_Vec,theD3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Value, first, second and third derivatives of surface
        """
    def DN(self,theU : float,theV : float,theDerU : int,theDerV : int) -> OCP.gp.gp_Vec: 
        """
        Calculates N-th derivatives of surface, where N = theDerU + theDerV.
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
    def SetOffsetValue(self,theOffset : float) -> None: 
        """
        Change the offset value
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theBase : OCP.Geom.Geom_Surface,theOffset : float,theOscSurf : OCP.Geom.Geom_OsculatingSurface=None) -> None: ...
    @overload
    def __init__(self,theBase : OCP.GeomAdaptor.GeomAdaptor_HSurface,theOffset : float,theOscSurf : OCP.Geom.Geom_OsculatingSurface=None) -> None: ...
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
class GeomEvaluator_SurfaceOfExtrusion(GeomEvaluator_Surface, OCP.Standard.Standard_Transient):
    """
    Allows to calculate values and derivatives for surfaces of linear extrusionAllows to calculate values and derivatives for surfaces of linear extrusion
    """
    def D0(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt) -> None: 
        """
        Value of surface
        """
    def D1(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec) -> None: 
        """
        Value and first derivatives of surface
        """
    def D2(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec) -> None: 
        """
        Value, first and second derivatives of surface
        """
    def D3(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec,theD3U : OCP.gp.gp_Vec,theD3V : OCP.gp.gp_Vec,theD3UUV : OCP.gp.gp_Vec,theD3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Value, first, second and third derivatives of surface
        """
    def DN(self,theU : float,theV : float,theDerU : int,theDerV : int) -> OCP.gp.gp_Vec: 
        """
        Calculates N-th derivatives of surface, where N = theDerU + theDerV.
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
    def SetDirection(self,theDirection : OCP.gp.gp_Dir) -> None: 
        """
        ! Changes the direction of extrusion
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theBase : OCP.Geom.Geom_Curve,theExtrusionDir : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,theBase : OCP.Adaptor3d.Adaptor3d_HCurve,theExtrusionDir : OCP.gp.gp_Dir) -> None: ...
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
class GeomEvaluator_SurfaceOfRevolution(GeomEvaluator_Surface, OCP.Standard.Standard_Transient):
    """
    Allows to calculate values and derivatives for surfaces of revolutionAllows to calculate values and derivatives for surfaces of revolution
    """
    def D0(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt) -> None: 
        """
        Value of surface
        """
    def D1(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec) -> None: 
        """
        Value and first derivatives of surface
        """
    def D2(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec) -> None: 
        """
        Value, first and second derivatives of surface
        """
    def D3(self,theU : float,theV : float,theValue : OCP.gp.gp_Pnt,theD1U : OCP.gp.gp_Vec,theD1V : OCP.gp.gp_Vec,theD2U : OCP.gp.gp_Vec,theD2V : OCP.gp.gp_Vec,theD2UV : OCP.gp.gp_Vec,theD3U : OCP.gp.gp_Vec,theD3V : OCP.gp.gp_Vec,theD3UUV : OCP.gp.gp_Vec,theD3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Value, first, second and third derivatives of surface
        """
    def DN(self,theU : float,theV : float,theDerU : int,theDerV : int) -> OCP.gp.gp_Vec: 
        """
        Calculates N-th derivatives of surface, where N = theDerU + theDerV.
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
    def SetAxis(self,theAxis : OCP.gp.gp_Ax1) -> None: 
        """
        Change the axis of revolution
        """
    def SetDirection(self,theDirection : OCP.gp.gp_Dir) -> None: 
        """
        Change direction of the axis of revolution
        """
    def SetLocation(self,theLocation : OCP.gp.gp_Pnt) -> None: 
        """
        Change location of the axis of revolution
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theBase : OCP.Adaptor3d.Adaptor3d_HCurve,theRevolDir : OCP.gp.gp_Dir,theRevolLoc : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,theBase : OCP.Geom.Geom_Curve,theRevolDir : OCP.gp.gp_Dir,theRevolLoc : OCP.gp.gp_Pnt) -> None: ...
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
