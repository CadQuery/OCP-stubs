import OCP.Geom2dEvaluator
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
import OCP.Geom2dAdaptor
import OCP.Geom2d
import OCP.gp
__all__  = [
"Geom2dEvaluator_Curve",
"Geom2dEvaluator_OffsetCurve"
]
class Geom2dEvaluator_Curve(OCP.Standard.Standard_Transient):
    """
    Interface for calculation of values and derivatives for different kinds of curves in 2D. Works both with adaptors and curves.Interface for calculation of values and derivatives for different kinds of curves in 2D. Works both with adaptors and curves.
    """
    def D0(self,theU : float,theValue : OCP.gp.gp_Pnt2d) -> None: 
        """
        Value of 2D curve
        """
    def D1(self,theU : float,theValue : OCP.gp.gp_Pnt2d,theD1 : OCP.gp.gp_Vec2d) -> None: 
        """
        Value and first derivatives of curve
        """
    def D2(self,theU : float,theValue : OCP.gp.gp_Pnt2d,theD1 : OCP.gp.gp_Vec2d,theD2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Value, first and second derivatives of curve
        """
    def D3(self,theU : float,theValue : OCP.gp.gp_Pnt2d,theD1 : OCP.gp.gp_Vec2d,theD2 : OCP.gp.gp_Vec2d,theD3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Value, first, second and third derivatives of curve
        """
    def DN(self,theU : float,theDerU : int) -> OCP.gp.gp_Vec2d: 
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
class Geom2dEvaluator_OffsetCurve(Geom2dEvaluator_Curve, OCP.Standard.Standard_Transient):
    """
    Allows to calculate values and derivatives for offset curves in 2DAllows to calculate values and derivatives for offset curves in 2D
    """
    def D0(self,theU : float,theValue : OCP.gp.gp_Pnt2d) -> None: 
        """
        Value of curve
        """
    def D1(self,theU : float,theValue : OCP.gp.gp_Pnt2d,theD1 : OCP.gp.gp_Vec2d) -> None: 
        """
        Value and first derivatives of curve
        """
    def D2(self,theU : float,theValue : OCP.gp.gp_Pnt2d,theD1 : OCP.gp.gp_Vec2d,theD2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Value, first and second derivatives of curve
        """
    def D3(self,theU : float,theValue : OCP.gp.gp_Pnt2d,theD1 : OCP.gp.gp_Vec2d,theD2 : OCP.gp.gp_Vec2d,theD3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Value, first, second and third derivatives of curve
        """
    def DN(self,theU : float,theDeriv : int) -> OCP.gp.gp_Vec2d: 
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
    def SetOffsetValue(self,theOffset : float) -> None: 
        """
        Change the offset value
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theBase : OCP.Geom2d.Geom2d_Curve,theOffset : float) -> None: ...
    @overload
    def __init__(self,theBase : OCP.Geom2dAdaptor.Geom2dAdaptor_HCurve,theOffset : float) -> None: ...
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
