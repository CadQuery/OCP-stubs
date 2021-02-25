import OCP.NLPlate
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Plate
import OCP.NCollection
import OCP.gp
import OCP.Geom
import OCP.Standard
__all__  = [
"NLPlate_HGPPConstraint",
"NLPlate_HPG0Constraint",
"NLPlate_HPG0G1Constraint",
"NLPlate_HPG0G2Constraint",
"NLPlate_HPG0G3Constraint",
"NLPlate_HPG1Constraint",
"NLPlate_HPG2Constraint",
"NLPlate_HPG3Constraint",
"NLPlate_NLPlate",
"NLPlate_SequenceOfHGPPConstraint",
"NLPlate_StackOfPlate"
]
class NLPlate_HGPPConstraint(OCP.Standard.Standard_Transient):
    """
    define a PinPoint geometric Constraint used to load a Non Linear Platedefine a PinPoint geometric Constraint used to load a Non Linear Platedefine a PinPoint geometric Constraint used to load a Non Linear Plate
    """
    def ActiveOrder(self) -> int: 
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
    def G0Criterion(self) -> float: 
        """
        None
        """
    def G0Target(self) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def G1Criterion(self) -> float: 
        """
        None
        """
    def G1Target(self) -> OCP.Plate.Plate_D1: 
        """
        None
        """
    def G2Criterion(self) -> float: 
        """
        None
        """
    def G2Target(self) -> OCP.Plate.Plate_D2: 
        """
        None
        """
    def G3Criterion(self) -> float: 
        """
        None
        """
    def G3Target(self) -> OCP.Plate.Plate_D3: 
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
    def IncrementalLoadAllowed(self) -> bool: 
        """
        None
        """
    def IsG0(self) -> bool: 
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
    def Orientation(self) -> int: 
        """
        None
        """
    def SetActiveOrder(self,ActiveOrder : int) -> None: 
        """
        None
        """
    def SetG0Criterion(self,TolDist : float) -> None: 
        """
        None
        """
    def SetG1Criterion(self,TolAng : float) -> None: 
        """
        None
        """
    def SetG2Criterion(self,TolCurv : float) -> None: 
        """
        None
        """
    def SetG3Criterion(self,TolG3 : float) -> None: 
        """
        None
        """
    def SetIncrementalLoadAllowed(self,ILA : bool) -> None: 
        """
        None
        """
    def SetOrientation(self,Orient : int=0) -> None: 
        """
        None
        """
    def SetUV(self,UV : OCP.gp.gp_XY) -> None: 
        """
        None
        """
    def SetUVFreeSliding(self,UVFree : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UV(self) -> OCP.gp.gp_XY: 
        """
        None
        """
    def UVFreeSliding(self) -> bool: 
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
class NLPlate_HPG0Constraint(NLPlate_HGPPConstraint, OCP.Standard.Standard_Transient):
    """
    define a PinPoint G0 Constraint used to load a Non Linear Platedefine a PinPoint G0 Constraint used to load a Non Linear Platedefine a PinPoint G0 Constraint used to load a Non Linear Plate
    """
    def ActiveOrder(self) -> int: 
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
    def G0Criterion(self) -> float: 
        """
        None
        """
    def G0Target(self) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def G1Criterion(self) -> float: 
        """
        None
        """
    def G1Target(self) -> OCP.Plate.Plate_D1: 
        """
        None
        """
    def G2Criterion(self) -> float: 
        """
        None
        """
    def G2Target(self) -> OCP.Plate.Plate_D2: 
        """
        None
        """
    def G3Criterion(self) -> float: 
        """
        None
        """
    def G3Target(self) -> OCP.Plate.Plate_D3: 
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
    def IncrementalLoadAllowed(self) -> bool: 
        """
        None
        """
    def IsG0(self) -> bool: 
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
    def Orientation(self) -> int: 
        """
        None
        """
    def SetActiveOrder(self,ActiveOrder : int) -> None: 
        """
        None
        """
    def SetG0Criterion(self,TolDist : float) -> None: 
        """
        None
        """
    def SetG1Criterion(self,TolAng : float) -> None: 
        """
        None
        """
    def SetG2Criterion(self,TolCurv : float) -> None: 
        """
        None
        """
    def SetG3Criterion(self,TolG3 : float) -> None: 
        """
        None
        """
    def SetIncrementalLoadAllowed(self,ILA : bool) -> None: 
        """
        None
        """
    def SetOrientation(self,Orient : int=0) -> None: 
        """
        None
        """
    def SetUV(self,UV : OCP.gp.gp_XY) -> None: 
        """
        None
        """
    def SetUVFreeSliding(self,UVFree : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UV(self) -> OCP.gp.gp_XY: 
        """
        None
        """
    def UVFreeSliding(self) -> bool: 
        """
        None
        """
    def __init__(self,UV : OCP.gp.gp_XY,Value : OCP.gp.gp_XYZ) -> None: ...
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
class NLPlate_HPG0G1Constraint(NLPlate_HPG0Constraint, NLPlate_HGPPConstraint, OCP.Standard.Standard_Transient):
    """
    define a PinPoint G0+G1 Constraint used to load a Non Linear Platedefine a PinPoint G0+G1 Constraint used to load a Non Linear Platedefine a PinPoint G0+G1 Constraint used to load a Non Linear Plate
    """
    def ActiveOrder(self) -> int: 
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
    def G0Criterion(self) -> float: 
        """
        None
        """
    def G0Target(self) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def G1Criterion(self) -> float: 
        """
        None
        """
    def G1Target(self) -> OCP.Plate.Plate_D1: 
        """
        None
        """
    def G2Criterion(self) -> float: 
        """
        None
        """
    def G2Target(self) -> OCP.Plate.Plate_D2: 
        """
        None
        """
    def G3Criterion(self) -> float: 
        """
        None
        """
    def G3Target(self) -> OCP.Plate.Plate_D3: 
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
    def IncrementalLoadAllowed(self) -> bool: 
        """
        None
        """
    def IsG0(self) -> bool: 
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
    def Orientation(self) -> int: 
        """
        None
        """
    def SetActiveOrder(self,ActiveOrder : int) -> None: 
        """
        None
        """
    def SetG0Criterion(self,TolDist : float) -> None: 
        """
        None
        """
    def SetG1Criterion(self,TolAng : float) -> None: 
        """
        None
        """
    def SetG2Criterion(self,TolCurv : float) -> None: 
        """
        None
        """
    def SetG3Criterion(self,TolG3 : float) -> None: 
        """
        None
        """
    def SetIncrementalLoadAllowed(self,ILA : bool) -> None: 
        """
        None
        """
    def SetOrientation(self,Orient : int=0) -> None: 
        """
        None
        """
    def SetUV(self,UV : OCP.gp.gp_XY) -> None: 
        """
        None
        """
    def SetUVFreeSliding(self,UVFree : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UV(self) -> OCP.gp.gp_XY: 
        """
        None
        """
    def UVFreeSliding(self) -> bool: 
        """
        None
        """
    def __init__(self,UV : OCP.gp.gp_XY,Value : OCP.gp.gp_XYZ,D1T : OCP.Plate.Plate_D1) -> None: ...
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
class NLPlate_HPG0G2Constraint(NLPlate_HPG0G1Constraint, NLPlate_HPG0Constraint, NLPlate_HGPPConstraint, OCP.Standard.Standard_Transient):
    """
    define a PinPoint G0+G2 Constraint used to load a Non Linear Platedefine a PinPoint G0+G2 Constraint used to load a Non Linear Platedefine a PinPoint G0+G2 Constraint used to load a Non Linear Plate
    """
    def ActiveOrder(self) -> int: 
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
    def G0Criterion(self) -> float: 
        """
        None
        """
    def G0Target(self) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def G1Criterion(self) -> float: 
        """
        None
        """
    def G1Target(self) -> OCP.Plate.Plate_D1: 
        """
        None
        """
    def G2Criterion(self) -> float: 
        """
        None
        """
    def G2Target(self) -> OCP.Plate.Plate_D2: 
        """
        None
        """
    def G3Criterion(self) -> float: 
        """
        None
        """
    def G3Target(self) -> OCP.Plate.Plate_D3: 
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
    def IncrementalLoadAllowed(self) -> bool: 
        """
        None
        """
    def IsG0(self) -> bool: 
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
    def Orientation(self) -> int: 
        """
        None
        """
    def SetActiveOrder(self,ActiveOrder : int) -> None: 
        """
        None
        """
    def SetG0Criterion(self,TolDist : float) -> None: 
        """
        None
        """
    def SetG1Criterion(self,TolAng : float) -> None: 
        """
        None
        """
    def SetG2Criterion(self,TolCurv : float) -> None: 
        """
        None
        """
    def SetG3Criterion(self,TolG3 : float) -> None: 
        """
        None
        """
    def SetIncrementalLoadAllowed(self,ILA : bool) -> None: 
        """
        None
        """
    def SetOrientation(self,Orient : int=0) -> None: 
        """
        None
        """
    def SetUV(self,UV : OCP.gp.gp_XY) -> None: 
        """
        None
        """
    def SetUVFreeSliding(self,UVFree : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UV(self) -> OCP.gp.gp_XY: 
        """
        None
        """
    def UVFreeSliding(self) -> bool: 
        """
        None
        """
    def __init__(self,UV : OCP.gp.gp_XY,Value : OCP.gp.gp_XYZ,D1T : OCP.Plate.Plate_D1,D2T : OCP.Plate.Plate_D2) -> None: ...
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
class NLPlate_HPG0G3Constraint(NLPlate_HPG0G2Constraint, NLPlate_HPG0G1Constraint, NLPlate_HPG0Constraint, NLPlate_HGPPConstraint, OCP.Standard.Standard_Transient):
    """
    define a PinPoint G0+G3 Constraint used to load a Non Linear Platedefine a PinPoint G0+G3 Constraint used to load a Non Linear Platedefine a PinPoint G0+G3 Constraint used to load a Non Linear Plate
    """
    def ActiveOrder(self) -> int: 
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
    def G0Criterion(self) -> float: 
        """
        None
        """
    def G0Target(self) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def G1Criterion(self) -> float: 
        """
        None
        """
    def G1Target(self) -> OCP.Plate.Plate_D1: 
        """
        None
        """
    def G2Criterion(self) -> float: 
        """
        None
        """
    def G2Target(self) -> OCP.Plate.Plate_D2: 
        """
        None
        """
    def G3Criterion(self) -> float: 
        """
        None
        """
    def G3Target(self) -> OCP.Plate.Plate_D3: 
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
    def IncrementalLoadAllowed(self) -> bool: 
        """
        None
        """
    def IsG0(self) -> bool: 
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
    def Orientation(self) -> int: 
        """
        None
        """
    def SetActiveOrder(self,ActiveOrder : int) -> None: 
        """
        None
        """
    def SetG0Criterion(self,TolDist : float) -> None: 
        """
        None
        """
    def SetG1Criterion(self,TolAng : float) -> None: 
        """
        None
        """
    def SetG2Criterion(self,TolCurv : float) -> None: 
        """
        None
        """
    def SetG3Criterion(self,TolG3 : float) -> None: 
        """
        None
        """
    def SetIncrementalLoadAllowed(self,ILA : bool) -> None: 
        """
        None
        """
    def SetOrientation(self,Orient : int=0) -> None: 
        """
        None
        """
    def SetUV(self,UV : OCP.gp.gp_XY) -> None: 
        """
        None
        """
    def SetUVFreeSliding(self,UVFree : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UV(self) -> OCP.gp.gp_XY: 
        """
        None
        """
    def UVFreeSliding(self) -> bool: 
        """
        None
        """
    def __init__(self,UV : OCP.gp.gp_XY,Value : OCP.gp.gp_XYZ,D1T : OCP.Plate.Plate_D1,D2T : OCP.Plate.Plate_D2,D3T : OCP.Plate.Plate_D3) -> None: ...
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
class NLPlate_HPG1Constraint(NLPlate_HGPPConstraint, OCP.Standard.Standard_Transient):
    """
    define a PinPoint (no G0) G1 Constraint used to load a Non Linear Platedefine a PinPoint (no G0) G1 Constraint used to load a Non Linear Platedefine a PinPoint (no G0) G1 Constraint used to load a Non Linear Plate
    """
    def ActiveOrder(self) -> int: 
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
    def G0Criterion(self) -> float: 
        """
        None
        """
    def G0Target(self) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def G1Criterion(self) -> float: 
        """
        None
        """
    def G1Target(self) -> OCP.Plate.Plate_D1: 
        """
        None
        """
    def G2Criterion(self) -> float: 
        """
        None
        """
    def G2Target(self) -> OCP.Plate.Plate_D2: 
        """
        None
        """
    def G3Criterion(self) -> float: 
        """
        None
        """
    def G3Target(self) -> OCP.Plate.Plate_D3: 
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
    def IncrementalLoadAllowed(self) -> bool: 
        """
        None
        """
    def IsG0(self) -> bool: 
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
    def Orientation(self) -> int: 
        """
        None
        """
    def SetActiveOrder(self,ActiveOrder : int) -> None: 
        """
        None
        """
    def SetG0Criterion(self,TolDist : float) -> None: 
        """
        None
        """
    def SetG1Criterion(self,TolAng : float) -> None: 
        """
        None
        """
    def SetG2Criterion(self,TolCurv : float) -> None: 
        """
        None
        """
    def SetG3Criterion(self,TolG3 : float) -> None: 
        """
        None
        """
    def SetIncrementalLoadAllowed(self,ILA : bool) -> None: 
        """
        None
        """
    def SetOrientation(self,Orient : int=0) -> None: 
        """
        None
        """
    def SetUV(self,UV : OCP.gp.gp_XY) -> None: 
        """
        None
        """
    def SetUVFreeSliding(self,UVFree : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UV(self) -> OCP.gp.gp_XY: 
        """
        None
        """
    def UVFreeSliding(self) -> bool: 
        """
        None
        """
    def __init__(self,UV : OCP.gp.gp_XY,D1T : OCP.Plate.Plate_D1) -> None: ...
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
class NLPlate_HPG2Constraint(NLPlate_HPG1Constraint, NLPlate_HGPPConstraint, OCP.Standard.Standard_Transient):
    """
    define a PinPoint (no G0) G2 Constraint used to load a Non Linear Platedefine a PinPoint (no G0) G2 Constraint used to load a Non Linear Platedefine a PinPoint (no G0) G2 Constraint used to load a Non Linear Plate
    """
    def ActiveOrder(self) -> int: 
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
    def G0Criterion(self) -> float: 
        """
        None
        """
    def G0Target(self) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def G1Criterion(self) -> float: 
        """
        None
        """
    def G1Target(self) -> OCP.Plate.Plate_D1: 
        """
        None
        """
    def G2Criterion(self) -> float: 
        """
        None
        """
    def G2Target(self) -> OCP.Plate.Plate_D2: 
        """
        None
        """
    def G3Criterion(self) -> float: 
        """
        None
        """
    def G3Target(self) -> OCP.Plate.Plate_D3: 
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
    def IncrementalLoadAllowed(self) -> bool: 
        """
        None
        """
    def IsG0(self) -> bool: 
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
    def Orientation(self) -> int: 
        """
        None
        """
    def SetActiveOrder(self,ActiveOrder : int) -> None: 
        """
        None
        """
    def SetG0Criterion(self,TolDist : float) -> None: 
        """
        None
        """
    def SetG1Criterion(self,TolAng : float) -> None: 
        """
        None
        """
    def SetG2Criterion(self,TolCurv : float) -> None: 
        """
        None
        """
    def SetG3Criterion(self,TolG3 : float) -> None: 
        """
        None
        """
    def SetIncrementalLoadAllowed(self,ILA : bool) -> None: 
        """
        None
        """
    def SetOrientation(self,Orient : int=0) -> None: 
        """
        None
        """
    def SetUV(self,UV : OCP.gp.gp_XY) -> None: 
        """
        None
        """
    def SetUVFreeSliding(self,UVFree : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UV(self) -> OCP.gp.gp_XY: 
        """
        None
        """
    def UVFreeSliding(self) -> bool: 
        """
        None
        """
    def __init__(self,UV : OCP.gp.gp_XY,D1T : OCP.Plate.Plate_D1,D2T : OCP.Plate.Plate_D2) -> None: ...
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
class NLPlate_HPG3Constraint(NLPlate_HPG2Constraint, NLPlate_HPG1Constraint, NLPlate_HGPPConstraint, OCP.Standard.Standard_Transient):
    """
    define a PinPoint (no G0) G3 Constraint used to load a Non Linear Platedefine a PinPoint (no G0) G3 Constraint used to load a Non Linear Platedefine a PinPoint (no G0) G3 Constraint used to load a Non Linear Plate
    """
    def ActiveOrder(self) -> int: 
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
    def G0Criterion(self) -> float: 
        """
        None
        """
    def G0Target(self) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def G1Criterion(self) -> float: 
        """
        None
        """
    def G1Target(self) -> OCP.Plate.Plate_D1: 
        """
        None
        """
    def G2Criterion(self) -> float: 
        """
        None
        """
    def G2Target(self) -> OCP.Plate.Plate_D2: 
        """
        None
        """
    def G3Criterion(self) -> float: 
        """
        None
        """
    def G3Target(self) -> OCP.Plate.Plate_D3: 
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
    def IncrementalLoadAllowed(self) -> bool: 
        """
        None
        """
    def IsG0(self) -> bool: 
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
    def Orientation(self) -> int: 
        """
        None
        """
    def SetActiveOrder(self,ActiveOrder : int) -> None: 
        """
        None
        """
    def SetG0Criterion(self,TolDist : float) -> None: 
        """
        None
        """
    def SetG1Criterion(self,TolAng : float) -> None: 
        """
        None
        """
    def SetG2Criterion(self,TolCurv : float) -> None: 
        """
        None
        """
    def SetG3Criterion(self,TolG3 : float) -> None: 
        """
        None
        """
    def SetIncrementalLoadAllowed(self,ILA : bool) -> None: 
        """
        None
        """
    def SetOrientation(self,Orient : int=0) -> None: 
        """
        None
        """
    def SetUV(self,UV : OCP.gp.gp_XY) -> None: 
        """
        None
        """
    def SetUVFreeSliding(self,UVFree : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UV(self) -> OCP.gp.gp_XY: 
        """
        None
        """
    def UVFreeSliding(self) -> bool: 
        """
        None
        """
    def __init__(self,UV : OCP.gp.gp_XY,D1T : OCP.Plate.Plate_D1,D2T : OCP.Plate.Plate_D2,D3T : OCP.Plate.Plate_D3) -> None: ...
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
class NLPlate_NLPlate():
    """
    None
    """
    def ConstraintsSliding(self,NbIterations : int=3) -> None: 
        """
        None
        """
    def Continuity(self) -> int: 
        """
        None
        """
    def Evaluate(self,point2d : OCP.gp.gp_XY) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def EvaluateDerivative(self,point2d : OCP.gp.gp_XY,iu : int,iv : int) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def IncrementalSolve(self,ord : int=2,InitialConsraintOrder : int=1,NbIncrements : int=4,UVSliding : bool=False) -> None: 
        """
        None
        """
    def Init(self) -> None: 
        """
        reset the Plate in the initial state ( same as after Create((Surface))
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    def Load(self,GConst : NLPlate_HGPPConstraint) -> None: 
        """
        None
        """
    def MaxActiveConstraintOrder(self) -> int: 
        """
        None
        """
    def Solve(self,ord : int=2,InitialConsraintOrder : int=1) -> None: 
        """
        None
        """
    def Solve2(self,ord : int=2,InitialConsraintOrder : int=1) -> None: 
        """
        None
        """
    def __init__(self,InitialSurface : OCP.Geom.Geom_Surface) -> None: ...
    def destroy(self) -> None: 
        """
        None
        """
    pass
class NLPlate_SequenceOfHGPPConstraint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : NLPlate_SequenceOfHGPPConstraint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : NLPlate_HGPPConstraint) -> None: ...
    def Assign(self,theOther : NLPlate_SequenceOfHGPPConstraint) -> NLPlate_SequenceOfHGPPConstraint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> NLPlate_HGPPConstraint: 
        """
        First item access
        """
    def ChangeLast(self) -> NLPlate_HGPPConstraint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> NLPlate_HGPPConstraint: 
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
    def First(self) -> NLPlate_HGPPConstraint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : NLPlate_HGPPConstraint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : NLPlate_SequenceOfHGPPConstraint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : NLPlate_SequenceOfHGPPConstraint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : NLPlate_HGPPConstraint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> NLPlate_HGPPConstraint: 
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
    def Prepend(self,theSeq : NLPlate_SequenceOfHGPPConstraint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : NLPlate_HGPPConstraint) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : NLPlate_HGPPConstraint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : NLPlate_SequenceOfHGPPConstraint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> NLPlate_HGPPConstraint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : NLPlate_SequenceOfHGPPConstraint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class NLPlate_StackOfPlate(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.Plate.Plate_Plate) -> OCP.Plate.Plate_Plate: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.Plate.Plate_Plate,theIter : Any) -> None: ...
    @overload
    def Append(self,theOther : NLPlate_StackOfPlate) -> None: ...
    def Assign(self,theOther : NLPlate_StackOfPlate) -> NLPlate_StackOfPlate: 
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
    def First(self) -> OCP.Plate.Plate_Plate: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.Plate.Plate_Plate,theIter : Any) -> OCP.Plate.Plate_Plate: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : NLPlate_StackOfPlate,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : NLPlate_StackOfPlate,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : OCP.Plate.Plate_Plate,theIter : Any) -> OCP.Plate.Plate_Plate: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.Plate.Plate_Plate: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : NLPlate_StackOfPlate) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OCP.Plate.Plate_Plate) -> OCP.Plate.Plate_Plate: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : NLPlate_StackOfPlate) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
