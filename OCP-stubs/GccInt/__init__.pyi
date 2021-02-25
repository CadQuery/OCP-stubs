import OCP.GccInt
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.Standard
__all__  = [
"GccInt_Bisec",
"GccInt_BElips",
"GccInt_BHyper",
"GccInt_BLine",
"GccInt_BParab",
"GccInt_BPoint",
"GccInt_BCirc",
"GccInt_IType",
"GccInt_Cir",
"GccInt_Ell",
"GccInt_Hpr",
"GccInt_Lin",
"GccInt_Par",
"GccInt_Pnt"
]
class GccInt_Bisec(OCP.Standard.Standard_Transient):
    """
    The deferred class GccInt_Bisec is the root class for elementary bisecting loci between two simple geometric objects (i.e. circles, lines or points). Bisecting loci between two geometric objects are such that each of their points is at the same distance from the two geometric objects. It is typically a curve, such as a line, circle or conic. Generally there is more than one elementary object which is the solution to a bisecting loci problem: each solution is described with one elementary bisecting locus. For example, the bisectors of two secant straight lines are two perpendicular straight lines. The GccInt package provides concrete implementations of the following elementary derived bisecting loci: - lines, circles, ellipses, hyperbolas and parabolas, and - points (not used in this context). The GccAna package provides numerous algorithms for computing the bisecting loci between circles, lines or points, whose solutions are these types of elementary bisecting locus.The deferred class GccInt_Bisec is the root class for elementary bisecting loci between two simple geometric objects (i.e. circles, lines or points). Bisecting loci between two geometric objects are such that each of their points is at the same distance from the two geometric objects. It is typically a curve, such as a line, circle or conic. Generally there is more than one elementary object which is the solution to a bisecting loci problem: each solution is described with one elementary bisecting locus. For example, the bisectors of two secant straight lines are two perpendicular straight lines. The GccInt package provides concrete implementations of the following elementary derived bisecting loci: - lines, circles, ellipses, hyperbolas and parabolas, and - points (not used in this context). The GccAna package provides numerous algorithms for computing the bisecting loci between circles, lines or points, whose solutions are these types of elementary bisecting locus.The deferred class GccInt_Bisec is the root class for elementary bisecting loci between two simple geometric objects (i.e. circles, lines or points). Bisecting loci between two geometric objects are such that each of their points is at the same distance from the two geometric objects. It is typically a curve, such as a line, circle or conic. Generally there is more than one elementary object which is the solution to a bisecting loci problem: each solution is described with one elementary bisecting locus. For example, the bisectors of two secant straight lines are two perpendicular straight lines. The GccInt package provides concrete implementations of the following elementary derived bisecting loci: - lines, circles, ellipses, hyperbolas and parabolas, and - points (not used in this context). The GccAna package provides numerous algorithms for computing the bisecting loci between circles, lines or points, whose solutions are these types of elementary bisecting locus.
    """
    def ArcType(self) -> GccInt_IType: 
        """
        Returns the type of bisecting object (line, circle, parabola, hyperbola, ellipse, point).
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns the bisecting line when ArcType returns Cir. An exception DomainError is raised if ArcType is not a Cir.
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
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        Returns the bisecting line when ArcType returns Ell. An exception DomainError is raised if ArcType is not an Ell.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        Returns the bisecting line when ArcType returns Hpr. An exception DomainError is raised if ArcType is not a Hpr.
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
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns the bisecting line when ArcType returns Lin. An exception DomainError is raised if ArcType is not a Lin.
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        Returns the bisecting line when ArcType returns Par. An exception DomainError is raised if ArcType is not a Par.
        """
    def Point(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the bisecting line when ArcType returns Pnt. An exception DomainError is raised if ArcType is not a Pnt.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
class GccInt_BElips(GccInt_Bisec, OCP.Standard.Standard_Transient):
    """
    Describes an ellipse as a bisecting curve between two 2D geometric objects (such as circles or points).Describes an ellipse as a bisecting curve between two 2D geometric objects (such as circles or points).Describes an ellipse as a bisecting curve between two 2D geometric objects (such as circles or points).
    """
    def ArcType(self) -> GccInt_IType: 
        """
        Returns GccInt_Ell, which is the type of any GccInt_BElips bisecting curve.
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns the bisecting line when ArcType returns Cir. An exception DomainError is raised if ArcType is not a Cir.
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
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        Returns a 2D ellipse which is the geometry of this bisecting curve.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        Returns the bisecting line when ArcType returns Hpr. An exception DomainError is raised if ArcType is not a Hpr.
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
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns the bisecting line when ArcType returns Lin. An exception DomainError is raised if ArcType is not a Lin.
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        Returns the bisecting line when ArcType returns Par. An exception DomainError is raised if ArcType is not a Par.
        """
    def Point(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the bisecting line when ArcType returns Pnt. An exception DomainError is raised if ArcType is not a Pnt.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Ellipse : OCP.gp.gp_Elips2d) -> None: ...
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
class GccInt_BHyper(GccInt_Bisec, OCP.Standard.Standard_Transient):
    """
    Describes a hyperbola as a bisecting curve between two 2D geometric objects (such as circles or points).Describes a hyperbola as a bisecting curve between two 2D geometric objects (such as circles or points).Describes a hyperbola as a bisecting curve between two 2D geometric objects (such as circles or points).
    """
    def ArcType(self) -> GccInt_IType: 
        """
        Returns GccInt_Hpr, which is the type of any GccInt_BHyper bisecting curve.
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns the bisecting line when ArcType returns Cir. An exception DomainError is raised if ArcType is not a Cir.
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
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        Returns the bisecting line when ArcType returns Ell. An exception DomainError is raised if ArcType is not an Ell.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        Returns a 2D hyperbola which is the geometry of this bisecting curve.
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
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns the bisecting line when ArcType returns Lin. An exception DomainError is raised if ArcType is not a Lin.
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        Returns the bisecting line when ArcType returns Par. An exception DomainError is raised if ArcType is not a Par.
        """
    def Point(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the bisecting line when ArcType returns Pnt. An exception DomainError is raised if ArcType is not a Pnt.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Hyper : OCP.gp.gp_Hypr2d) -> None: ...
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
class GccInt_BLine(GccInt_Bisec, OCP.Standard.Standard_Transient):
    """
    Describes a line as a bisecting curve between two 2D geometric objects (such as lines, circles or points).Describes a line as a bisecting curve between two 2D geometric objects (such as lines, circles or points).Describes a line as a bisecting curve between two 2D geometric objects (such as lines, circles or points).
    """
    def ArcType(self) -> GccInt_IType: 
        """
        Returns GccInt_Lin, which is the type of any GccInt_BLine bisecting line.
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns the bisecting line when ArcType returns Cir. An exception DomainError is raised if ArcType is not a Cir.
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
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        Returns the bisecting line when ArcType returns Ell. An exception DomainError is raised if ArcType is not an Ell.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        Returns the bisecting line when ArcType returns Hpr. An exception DomainError is raised if ArcType is not a Hpr.
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
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns a 2D line which is the geometry of this bisecting line.
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        Returns the bisecting line when ArcType returns Par. An exception DomainError is raised if ArcType is not a Par.
        """
    def Point(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the bisecting line when ArcType returns Pnt. An exception DomainError is raised if ArcType is not a Pnt.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Line : OCP.gp.gp_Lin2d) -> None: ...
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
class GccInt_BParab(GccInt_Bisec, OCP.Standard.Standard_Transient):
    """
    Describes a parabola as a bisecting curve between two 2D geometric objects (such as lines, circles or points).Describes a parabola as a bisecting curve between two 2D geometric objects (such as lines, circles or points).Describes a parabola as a bisecting curve between two 2D geometric objects (such as lines, circles or points).
    """
    def ArcType(self) -> GccInt_IType: 
        """
        Returns GccInt_Par, which is the type of any GccInt_BParab bisecting curve.
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns the bisecting line when ArcType returns Cir. An exception DomainError is raised if ArcType is not a Cir.
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
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        Returns the bisecting line when ArcType returns Ell. An exception DomainError is raised if ArcType is not an Ell.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        Returns the bisecting line when ArcType returns Hpr. An exception DomainError is raised if ArcType is not a Hpr.
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
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns the bisecting line when ArcType returns Lin. An exception DomainError is raised if ArcType is not a Lin.
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        Returns a 2D parabola which is the geometry of this bisecting curve.
        """
    def Point(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the bisecting line when ArcType returns Pnt. An exception DomainError is raised if ArcType is not a Pnt.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Parab : OCP.gp.gp_Parab2d) -> None: ...
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
class GccInt_BPoint(GccInt_Bisec, OCP.Standard.Standard_Transient):
    """
    Describes a point as a bisecting object between two 2D geometric objects.Describes a point as a bisecting object between two 2D geometric objects.Describes a point as a bisecting object between two 2D geometric objects.
    """
    def ArcType(self) -> GccInt_IType: 
        """
        Returns GccInt_Pnt, which is the type of any GccInt_BPoint bisecting object.
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns the bisecting line when ArcType returns Cir. An exception DomainError is raised if ArcType is not a Cir.
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
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        Returns the bisecting line when ArcType returns Ell. An exception DomainError is raised if ArcType is not an Ell.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        Returns the bisecting line when ArcType returns Hpr. An exception DomainError is raised if ArcType is not a Hpr.
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
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns the bisecting line when ArcType returns Lin. An exception DomainError is raised if ArcType is not a Lin.
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        Returns the bisecting line when ArcType returns Par. An exception DomainError is raised if ArcType is not a Par.
        """
    def Point(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns a 2D point which is the geometry of this bisecting object.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Point : OCP.gp.gp_Pnt2d) -> None: ...
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
class GccInt_BCirc(GccInt_Bisec, OCP.Standard.Standard_Transient):
    """
    Describes a circle as a bisecting curve between two 2D geometric objects (such as circles or points).Describes a circle as a bisecting curve between two 2D geometric objects (such as circles or points).Describes a circle as a bisecting curve between two 2D geometric objects (such as circles or points).
    """
    def ArcType(self) -> GccInt_IType: 
        """
        Returns GccInt_Cir, which is the type of any GccInt_BCirc bisecting curve.
        """
    def Circle(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns a 2D circle which is the geometry of this bisecting curve.
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
    def Ellipse(self) -> OCP.gp.gp_Elips2d: 
        """
        Returns the bisecting line when ArcType returns Ell. An exception DomainError is raised if ArcType is not an Ell.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr2d: 
        """
        Returns the bisecting line when ArcType returns Hpr. An exception DomainError is raised if ArcType is not a Hpr.
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
    def Line(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns the bisecting line when ArcType returns Lin. An exception DomainError is raised if ArcType is not a Lin.
        """
    def Parabola(self) -> OCP.gp.gp_Parab2d: 
        """
        Returns the bisecting line when ArcType returns Par. An exception DomainError is raised if ArcType is not a Par.
        """
    def Point(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the bisecting line when ArcType returns Pnt. An exception DomainError is raised if ArcType is not a Pnt.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Circ : OCP.gp.gp_Circ2d) -> None: ...
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
class GccInt_IType():
    """
    None

    Members:

      GccInt_Lin

      GccInt_Cir

      GccInt_Ell

      GccInt_Par

      GccInt_Hpr

      GccInt_Pnt
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
    GccInt_Cir: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Cir: 1>
    GccInt_Ell: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Ell: 2>
    GccInt_Hpr: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Hpr: 4>
    GccInt_Lin: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Lin: 0>
    GccInt_Par: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Par: 3>
    GccInt_Pnt: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Pnt: 5>
    __entries: dict # value = {'GccInt_Lin': (<GccInt_IType.GccInt_Lin: 0>, None), 'GccInt_Cir': (<GccInt_IType.GccInt_Cir: 1>, None), 'GccInt_Ell': (<GccInt_IType.GccInt_Ell: 2>, None), 'GccInt_Par': (<GccInt_IType.GccInt_Par: 3>, None), 'GccInt_Hpr': (<GccInt_IType.GccInt_Hpr: 4>, None), 'GccInt_Pnt': (<GccInt_IType.GccInt_Pnt: 5>, None)}
    __members__: dict # value = {'GccInt_Lin': <GccInt_IType.GccInt_Lin: 0>, 'GccInt_Cir': <GccInt_IType.GccInt_Cir: 1>, 'GccInt_Ell': <GccInt_IType.GccInt_Ell: 2>, 'GccInt_Par': <GccInt_IType.GccInt_Par: 3>, 'GccInt_Hpr': <GccInt_IType.GccInt_Hpr: 4>, 'GccInt_Pnt': <GccInt_IType.GccInt_Pnt: 5>}
    pass
GccInt_Cir: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Cir: 1>
GccInt_Ell: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Ell: 2>
GccInt_Hpr: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Hpr: 4>
GccInt_Lin: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Lin: 0>
GccInt_Par: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Par: 3>
GccInt_Pnt: OCP.GccInt.GccInt_IType # value = <GccInt_IType.GccInt_Pnt: 5>
