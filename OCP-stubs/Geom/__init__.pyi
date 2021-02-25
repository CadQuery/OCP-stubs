import OCP.Geom
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import io
import OCP.NCollection
import OCP.gp
import OCP.GeomAbs
import OCP.TColgp
import OCP.Standard
__all__  = [
"Geom_Geometry",
"Geom_AxisPlacement",
"Geom_Axis1Placement",
"Geom_Curve",
"Geom_Surface",
"Geom_BoundedCurve",
"Geom_BoundedSurface",
"Geom_BSplineCurve",
"Geom_BSplineSurface",
"Geom_Point",
"Geom_Conic",
"Geom_Circle",
"Geom_ElementarySurface",
"Geom_BezierCurve",
"Geom_CylindricalSurface",
"Geom_Vector",
"Geom_ConicalSurface",
"Geom_Ellipse",
"Geom_Axis2Placement",
"Geom_SequenceOfBSplineSurface",
"Geom_Hyperbola",
"Geom_Line",
"Geom_OffsetCurve",
"Geom_OffsetSurface",
"Geom_OsculatingSurface",
"Geom_Parabola",
"Geom_Plane",
"Geom_CartesianPoint",
"Geom_RectangularTrimmedSurface",
"Geom_HSequenceOfBSplineSurface",
"Geom_SphericalSurface",
"Geom_BezierSurface",
"Geom_SweptSurface",
"Geom_SurfaceOfRevolution",
"Geom_SurfaceOfLinearExtrusion",
"Geom_ToroidalSurface",
"Geom_Transformation",
"Geom_TrimmedCurve",
"Geom_UndefinedDerivative",
"Geom_UndefinedValue",
"Geom_Direction",
"Geom_VectorWithMagnitude"
]
class Geom_Geometry(OCP.Standard.Standard_Transient):
    """
    The abstract class Geometry for 3D space is the root class of all geometric objects from the Geom package. It describes the common behavior of these objects when: - applying geometric transformations to objects, and - constructing objects by geometric transformation (including copying). Warning Only transformations which do not modify the nature of the geometry can be applied to Geom objects: this is the case with translations, rotations, symmetries and scales; this is also the case with gp_Trsf composite transformations which are used to define the geometric transformations applied using the Transform or Transformed functions. Note: Geometry defines the "prototype" of the abstract method Transform which is defined for each concrete type of derived object. All other transformations are implemented using the Transform method.The abstract class Geometry for 3D space is the root class of all geometric objects from the Geom package. It describes the common behavior of these objects when: - applying geometric transformations to objects, and - constructing objects by geometric transformation (including copying). Warning Only transformations which do not modify the nature of the geometry can be applied to Geom objects: this is the case with translations, rotations, symmetries and scales; this is also the case with gp_Trsf composite transformations which are used to define the geometric transformations applied using the Transform or Transformed functions. Note: Geometry defines the "prototype" of the abstract method Transform which is defined for each concrete type of derived object. All other transformations are implemented using the Transform method.The abstract class Geometry for 3D space is the root class of all geometric objects from the Geom package. It describes the common behavior of these objects when: - applying geometric transformations to objects, and - constructing objects by geometric transformation (including copying). Warning Only transformations which do not modify the nature of the geometry can be applied to Geom objects: this is the case with translations, rotations, symmetries and scales; this is also the case with gp_Trsf composite transformations which are used to define the geometric transformations applied using the Transform or Transformed functions. Note: Geometry defines the "prototype" of the abstract method Transform which is defined for each concrete type of derived object. All other transformations are implemented using the Transform method.
    """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
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
class Geom_AxisPlacement(Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    The abstract class AxisPlacement describes the common behavior of positioning systems in 3D space, such as axis or coordinate systems. The Geom package provides two implementations of 3D positioning systems: - the axis (Geom_Axis1Placement class), which is defined by: - its origin, also termed the "Location point" of the axis, - its unit vector, termed the "Direction" or "main Direction" of the axis; - the right-handed coordinate system (Geom_Axis2Placement class), which is defined by: - its origin, also termed the "Location point" of the coordinate system, - three orthogonal unit vectors, termed respectively the "X Direction", the "Y Direction" and the "Direction" of the coordinate system. As the coordinate system is right-handed, these unit vectors have the following relation: "Direction" = "X Direction" ^ "Y Direction". The "Direction" is also called the "main Direction" because, when the unit vector is modified, the "X Direction" and "Y Direction" are recomputed, whereas when the "X Direction" or "Y Direction" is modified, the "main Direction" does not change. The axis whose origin is the origin of the positioning system and whose unit vector is its "main Direction" is also called the "Axis" or "main Axis" of the positioning system.The abstract class AxisPlacement describes the common behavior of positioning systems in 3D space, such as axis or coordinate systems. The Geom package provides two implementations of 3D positioning systems: - the axis (Geom_Axis1Placement class), which is defined by: - its origin, also termed the "Location point" of the axis, - its unit vector, termed the "Direction" or "main Direction" of the axis; - the right-handed coordinate system (Geom_Axis2Placement class), which is defined by: - its origin, also termed the "Location point" of the coordinate system, - three orthogonal unit vectors, termed respectively the "X Direction", the "Y Direction" and the "Direction" of the coordinate system. As the coordinate system is right-handed, these unit vectors have the following relation: "Direction" = "X Direction" ^ "Y Direction". The "Direction" is also called the "main Direction" because, when the unit vector is modified, the "X Direction" and "Y Direction" are recomputed, whereas when the "X Direction" or "Y Direction" is modified, the "main Direction" does not change. The axis whose origin is the origin of the positioning system and whose unit vector is its "main Direction" is also called the "Axis" or "main Axis" of the positioning system.The abstract class AxisPlacement describes the common behavior of positioning systems in 3D space, such as axis or coordinate systems. The Geom package provides two implementations of 3D positioning systems: - the axis (Geom_Axis1Placement class), which is defined by: - its origin, also termed the "Location point" of the axis, - its unit vector, termed the "Direction" or "main Direction" of the axis; - the right-handed coordinate system (Geom_Axis2Placement class), which is defined by: - its origin, also termed the "Location point" of the coordinate system, - three orthogonal unit vectors, termed respectively the "X Direction", the "Y Direction" and the "Direction" of the coordinate system. As the coordinate system is right-handed, these unit vectors have the following relation: "Direction" = "X Direction" ^ "Y Direction". The "Direction" is also called the "main Direction" because, when the unit vector is modified, the "X Direction" and "Y Direction" are recomputed, whereas when the "X Direction" or "Y Direction" is modified, the "main Direction" does not change. The axis whose origin is the origin of the positioning system and whose unit vector is its "main Direction" is also called the "Axis" or "main Axis" of the positioning system.
    """
    def Angle(self,Other : Geom_AxisPlacement) -> float: 
        """
        Computes the angular value, in radians, between the "main Direction" of this positioning system and that of positioning system Other. The result is a value between 0 and Pi.
        """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the main axis of the axis placement. For an "Axis2placement" it is the main axis (Location, Direction ). For an "Axis1Placement" this method returns a copy of <me>.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns the main "Direction" of an axis placement.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the Location point (origin) of the axis placement.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Assigns A1 as the "main Axis" of this positioning system. This modifies - its origin, and - its "main Direction". If this positioning system is a Geom_Axis2Placement, then its "X Direction" and "Y Direction" are recomputed. Exceptions For a Geom_Axis2Placement: Standard_ConstructionError if A1 and the previous "X Direction" of the coordinate system are parallel.
        """
    def SetDirection(self,V : OCP.gp.gp_Dir) -> None: 
        """
        Changes the direction of the axis placement. If <me> is an axis placement two axis the main "Direction" is modified and the "XDirection" and "YDirection" are recomputed. Raises ConstructionError only for an axis placement two axis if V and the previous "XDirection" are parallel because it is not possible to calculate the new "XDirection" and the new "YDirection".
        """
    def SetLocation(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Assigns the point P as the origin of this positioning system.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
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
class Geom_Axis1Placement(Geom_AxisPlacement, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes an axis in 3D space. An axis is defined by: - its origin, also termed the "Location point" of the axis, - its unit vector, termed the "Direction" of the axis. Note: Geom_Axis1Placement axes provide the same kind of "geometric" services as gp_Ax1 axes but have more complex data structures. The geometric objects provided by the Geom package use gp_Ax1 objects to include axes in their data structures, or to define an axis of symmetry or axis of rotation. Geom_Axis1Placement axes are used in a context where they can be shared by several objects contained inside a common data structure.Describes an axis in 3D space. An axis is defined by: - its origin, also termed the "Location point" of the axis, - its unit vector, termed the "Direction" of the axis. Note: Geom_Axis1Placement axes provide the same kind of "geometric" services as gp_Ax1 axes but have more complex data structures. The geometric objects provided by the Geom package use gp_Ax1 objects to include axes in their data structures, or to define an axis of symmetry or axis of rotation. Geom_Axis1Placement axes are used in a context where they can be shared by several objects contained inside a common data structure.Describes an axis in 3D space. An axis is defined by: - its origin, also termed the "Location point" of the axis, - its unit vector, termed the "Direction" of the axis. Note: Geom_Axis1Placement axes provide the same kind of "geometric" services as gp_Ax1 axes but have more complex data structures. The geometric objects provided by the Geom package use gp_Ax1 objects to include axes in their data structures, or to define an axis of symmetry or axis of rotation. Geom_Axis1Placement axes are used in a context where they can be shared by several objects contained inside a common data structure.
    """
    def Angle(self,Other : Geom_AxisPlacement) -> float: 
        """
        Computes the angular value, in radians, between the "main Direction" of this positioning system and that of positioning system Other. The result is a value between 0 and Pi.
        """
    def Ax1(self) -> OCP.gp.gp_Ax1: 
        """
        Returns a non transient copy of <me>.
        """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the main axis of the axis placement. For an "Axis2placement" it is the main axis (Location, Direction ). For an "Axis1Placement" this method returns a copy of <me>.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object, which is a copy of this axis.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns the main "Direction" of an axis placement.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the Location point (origin) of the axis placement.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Reverse(self) -> None: 
        """
        Reverses the direction of the axis placement.
        """
    def Reversed(self) -> Geom_Axis1Placement: 
        """
        Returns a copy of <me> reversed.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Assigns A1 as the "main Axis" of this positioning system. This modifies - its origin, and - its "main Direction". If this positioning system is a Geom_Axis2Placement, then its "X Direction" and "Y Direction" are recomputed. Exceptions For a Geom_Axis2Placement: Standard_ConstructionError if A1 and the previous "X Direction" of the coordinate system are parallel.
        """
    def SetDirection(self,V : OCP.gp.gp_Dir) -> None: 
        """
        Assigns V to the unit vector of this axis.
        """
    def SetLocation(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Assigns the point P as the origin of this positioning system.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this axis.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Dir) -> None: ...
    @overload
    def __init__(self,A1 : OCP.gp.gp_Ax1) -> None: ...
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
class Geom_Curve(Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    The abstract class Curve describes the common behavior of curves in 3D space. The Geom package provides numerous concrete classes of derived curves, including lines, circles, conics, Bezier or BSpline curves, etc. The main characteristic of these curves is that they are parameterized. The Geom_Curve class shows: - how to work with the parametric equation of a curve in order to calculate the point of parameter u, together with the vector tangent and the derivative vectors of order 2, 3,..., N at this point; - how to obtain general information about the curve (for example, level of continuity, closed characteristics, periodicity, bounds of the parameter field); - how the parameter changes when a geometric transformation is applied to the curve or when the orientation of the curve is inverted. All curves must have a geometric continuity: a curve is at least "C0". Generally, this property is checked at the time of construction or when the curve is edited. Where this is not the case, the documentation states so explicitly. Warning The Geom package does not prevent the construction of curves with null length or curves which self-intersect.The abstract class Curve describes the common behavior of curves in 3D space. The Geom package provides numerous concrete classes of derived curves, including lines, circles, conics, Bezier or BSpline curves, etc. The main characteristic of these curves is that they are parameterized. The Geom_Curve class shows: - how to work with the parametric equation of a curve in order to calculate the point of parameter u, together with the vector tangent and the derivative vectors of order 2, 3,..., N at this point; - how to obtain general information about the curve (for example, level of continuity, closed characteristics, periodicity, bounds of the parameter field); - how the parameter changes when a geometric transformation is applied to the curve or when the orientation of the curve is inverted. All curves must have a geometric continuity: a curve is at least "C0". Generally, this property is checked at the time of construction or when the curve is edited. Where this is not the case, the documentation states so explicitly. Warning The Geom package does not prevent the construction of curves with null length or curves which self-intersect.The abstract class Curve describes the common behavior of curves in 3D space. The Geom package provides numerous concrete classes of derived curves, including lines, circles, conics, Bezier or BSpline curves, etc. The main characteristic of these curves is that they are parameterized. The Geom_Curve class shows: - how to work with the parametric equation of a curve in order to calculate the point of parameter u, together with the vector tangent and the derivative vectors of order 2, 3,..., N at this point; - how to obtain general information about the curve (for example, level of continuity, closed characteristics, periodicity, bounds of the parameter field); - how the parameter changes when a geometric transformation is applied to the curve or when the orientation of the curve is inverted. All curves must have a geometric continuity: a curve is at least "C0". Generally, this property is checked at the time of construction or when the curve is edited. Where this is not the case, the documentation states so explicitly. Warning The Geom package does not prevent the construction of curves with null length or curves which self-intersect.
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        It is the global continuity of the curve C0 : only geometric continuity, C1 : continuity of the first derivative all along the Curve, C2 : continuity of the second derivative all along the Curve, C3 : continuity of the third derivative all along the Curve, G1 : tangency continuity all along the Curve, G2 : curvature continuity all along the Curve, CN : the order of continuity is infinite.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U and the first derivative V1. Raised if the continuity of the curve is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the curve is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the curve is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the curve is not CN.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter. Warnings : It can be RealFirst from package Standard if the curve is infinite
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns true if the degree of continuity of this curve is at least N. Exceptions - Standard_RangeError if N is less than 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns true if the curve is closed. Some curves such as circle are always closed, others such as line are never closed (by definition). Some Curves such as OffsetCurve can be closed or not. These curves are considered as closed if the distance between the first point and the last point of the curve is lower or equal to the Resolution from package gp wich is a fixed criterion independant of the application.
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
    def IsPeriodic(self) -> bool: 
        """
        Is the parametrization of the curve periodic ? It is possible only if the curve is closed and if the following relation is satisfied : for each parametric value U the distance between the point P(u) and the point P (u + T) is lower or equal to Resolution from package gp, T is the period and must be a constant. There are three possibilities : . the curve is never periodic by definition (SegmentLine) . the curve is always periodic by definition (Circle) . the curve can be defined as periodic (BSpline). In this case a function SetPeriodic allows you to give the shape of the curve. The general rule for this case is : if a curve can be periodic or not the default periodicity set is non periodic and you have to turn (explicitly) the curve into a periodic curve if you want the curve to be periodic.
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the last parameter. Warnings : It can be RealLast from package Standard if the curve is infinite
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def Reverse(self) -> None: 
        """
        Changes the direction of parametrization of <me>. The "FirstParameter" and the "LastParameter" are not changed but the orientation of the curve is modified. If the curve is bounded the StartPoint of the initial curve becomes the EndPoint of the reversed curve and the EndPoint of the initial curve becomes the StartPoint of the reversed curve.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the reversed curve for the point of parameter U on <me>.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
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
class Geom_Surface(Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes the common behavior of surfaces in 3D space. The Geom package provides many implementations of concrete derived surfaces, such as planes, cylinders, cones, spheres and tori, surfaces of linear extrusion, surfaces of revolution, Bezier and BSpline surfaces, and so on. The key characteristic of these surfaces is that they are parameterized. Geom_Surface demonstrates: - how to work with the parametric equation of a surface to compute the point of parameters (u, v), and, at this point, the 1st, 2nd ... Nth derivative, - how to find global information about a surface in each parametric direction (for example, level of continuity, whether the surface is closed, its periodicity, the bounds of the parameters and so on), and - how the parameters change when geometric transformations are applied to the surface, or the orientation is modified. Note that all surfaces must have a geometric continuity, and any surface is at least "C0". Generally, continuity is checked at construction time or when the curve is edited. Where this is not the case, the documentation makes this explicit. Warning The Geom package does not prevent the construction of surfaces with null areas, or surfaces which self-intersect.Describes the common behavior of surfaces in 3D space. The Geom package provides many implementations of concrete derived surfaces, such as planes, cylinders, cones, spheres and tori, surfaces of linear extrusion, surfaces of revolution, Bezier and BSpline surfaces, and so on. The key characteristic of these surfaces is that they are parameterized. Geom_Surface demonstrates: - how to work with the parametric equation of a surface to compute the point of parameters (u, v), and, at this point, the 1st, 2nd ... Nth derivative, - how to find global information about a surface in each parametric direction (for example, level of continuity, whether the surface is closed, its periodicity, the bounds of the parameters and so on), and - how the parameters change when geometric transformations are applied to the surface, or the orientation is modified. Note that all surfaces must have a geometric continuity, and any surface is at least "C0". Generally, continuity is checked at construction time or when the curve is edited. Where this is not the case, the documentation makes this explicit. Warning The Geom package does not prevent the construction of surfaces with null areas, or surfaces which self-intersect.Describes the common behavior of surfaces in 3D space. The Geom package provides many implementations of concrete derived surfaces, such as planes, cylinders, cones, spheres and tori, surfaces of linear extrusion, surfaces of revolution, Bezier and BSpline surfaces, and so on. The key characteristic of these surfaces is that they are parameterized. Geom_Surface demonstrates: - how to work with the parametric equation of a surface to compute the point of parameters (u, v), and, at this point, the 1st, 2nd ... Nth derivative, - how to find global information about a surface in each parametric direction (for example, level of continuity, whether the surface is closed, its periodicity, the bounds of the parameters and so on), and - how the parameters change when geometric transformations are applied to the surface, or the orientation is modified. Note that all surfaces must have a geometric continuity, and any surface is at least "C0". Generally, continuity is checked at construction time or when the curve is edited. Where this is not the case, the documentation makes this explicit. Warning The Geom package does not prevent the construction of surfaces with null areas, or surfaces which self-intersect.
    """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this surface. If the surface is infinite, this function can return a value equal to Precision::Infinite: instead of Standard_Real::LastReal.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the Global Continuity of the surface in direction U and V : C0 : only geometric continuity, C1 : continuity of the first derivative all along the surface, C2 : continuity of the second derivative all along the surface, C3 : continuity of the third derivative all along the surface, G1 : tangency continuity all along the surface, G2 : curvature continuity all along the surface, CN : the order of continuity is infinite. Example : If the surface is C1 in the V parametric direction and C2 in the U parametric direction Shape = C1.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U,V on the surface.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P and the first derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first and the second derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first,the second and the third derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        ---Purpose ; Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns the order of continuity of the surface in the U parametric direction. Raised if N < 0.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns the order of continuity of the surface in the V parametric direction. Raised if N < 0.
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
    def IsUClosed(self) -> bool: 
        """
        Checks whether this surface is closed in the u parametric direction. Returns true if, in the u parametric direction: taking uFirst and uLast as the parametric bounds in the u parametric direction, for each parameter v, the distance between the points P(uFirst, v) and P(uLast, v) is less than or equal to gp::Resolution().
        """
    def IsUPeriodic(self) -> bool: 
        """
        Checks if this surface is periodic in the u parametric direction. Returns true if: - this surface is closed in the u parametric direction, and - there is a constant T such that the distance between the points P (u, v) and P (u + T, v) (or the points P (u, v) and P (u, v + T)) is less than or equal to gp::Resolution(). Note: T is the parametric period in the u parametric direction.
        """
    def IsVClosed(self) -> bool: 
        """
        Checks whether this surface is closed in the u parametric direction. Returns true if, in the v parametric direction: taking vFirst and vLast as the parametric bounds in the v parametric direction, for each parameter u, the distance between the points P(u, vFirst) and P(u, vLast) is less than or equal to gp::Resolution().
        """
    def IsVPeriodic(self) -> bool: 
        """
        Checks if this surface is periodic in the v parametric direction. Returns true if: - this surface is closed in the v parametric direction, and - there is a constant T such that the distance between the points P (u, v) and P (u + T, v) (or the points P (u, v) and P (u, v + T)) is less than or equal to gp::Resolution(). Note: T is the parametric period in the v parametric direction.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the Ureversed surface for the point of parameter U on <me>.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Returns the parameter on the Vreversed surface for the point of parameter V on <me>.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
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
class Geom_BoundedCurve(Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    The abstract class BoundedCurve describes the common behavior of bounded curves in 3D space. A bounded curve is limited by two finite values of the parameter, termed respectively "first parameter" and "last parameter". The "first parameter" gives the "start point" of the bounded curve, and the "last parameter" gives the "end point" of the bounded curve. The length of a bounded curve is finite. The Geom package provides three concrete classes of bounded curves: - two frequently used mathematical formulations of complex curves: - Geom_BezierCurve, - Geom_BSplineCurve, and - Geom_TrimmedCurve to trim a curve, i.e. to only take part of the curve limited by two values of the parameter of the basis curve.The abstract class BoundedCurve describes the common behavior of bounded curves in 3D space. A bounded curve is limited by two finite values of the parameter, termed respectively "first parameter" and "last parameter". The "first parameter" gives the "start point" of the bounded curve, and the "last parameter" gives the "end point" of the bounded curve. The length of a bounded curve is finite. The Geom package provides three concrete classes of bounded curves: - two frequently used mathematical formulations of complex curves: - Geom_BezierCurve, - Geom_BSplineCurve, and - Geom_TrimmedCurve to trim a curve, i.e. to only take part of the curve limited by two values of the parameter of the basis curve.The abstract class BoundedCurve describes the common behavior of bounded curves in 3D space. A bounded curve is limited by two finite values of the parameter, termed respectively "first parameter" and "last parameter". The "first parameter" gives the "start point" of the bounded curve, and the "last parameter" gives the "end point" of the bounded curve. The length of a bounded curve is finite. The Geom package provides three concrete classes of bounded curves: - two frequently used mathematical formulations of complex curves: - Geom_BezierCurve, - Geom_BSplineCurve, and - Geom_TrimmedCurve to trim a curve, i.e. to only take part of the curve limited by two values of the parameter of the basis curve.
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        It is the global continuity of the curve C0 : only geometric continuity, C1 : continuity of the first derivative all along the Curve, C2 : continuity of the second derivative all along the Curve, C3 : continuity of the third derivative all along the Curve, G1 : tangency continuity all along the Curve, G2 : curvature continuity all along the Curve, CN : the order of continuity is infinite.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U and the first derivative V1. Raised if the continuity of the curve is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the curve is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the curve is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the curve is not CN.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the end point of the curve.
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter. Warnings : It can be RealFirst from package Standard if the curve is infinite
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns true if the degree of continuity of this curve is at least N. Exceptions - Standard_RangeError if N is less than 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns true if the curve is closed. Some curves such as circle are always closed, others such as line are never closed (by definition). Some Curves such as OffsetCurve can be closed or not. These curves are considered as closed if the distance between the first point and the last point of the curve is lower or equal to the Resolution from package gp wich is a fixed criterion independant of the application.
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
    def IsPeriodic(self) -> bool: 
        """
        Is the parametrization of the curve periodic ? It is possible only if the curve is closed and if the following relation is satisfied : for each parametric value U the distance between the point P(u) and the point P (u + T) is lower or equal to Resolution from package gp, T is the period and must be a constant. There are three possibilities : . the curve is never periodic by definition (SegmentLine) . the curve is always periodic by definition (Circle) . the curve can be defined as periodic (BSpline). In this case a function SetPeriodic allows you to give the shape of the curve. The general rule for this case is : if a curve can be periodic or not the default periodicity set is non periodic and you have to turn (explicitly) the curve into a periodic curve if you want the curve to be periodic.
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the last parameter. Warnings : It can be RealLast from package Standard if the curve is infinite
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def Reverse(self) -> None: 
        """
        Changes the direction of parametrization of <me>. The "FirstParameter" and the "LastParameter" are not changed but the orientation of the curve is modified. If the curve is bounded the StartPoint of the initial curve becomes the EndPoint of the reversed curve and the EndPoint of the initial curve becomes the StartPoint of the reversed curve.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the reversed curve for the point of parameter U on <me>.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def StartPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the start point of the curve.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
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
class Geom_BoundedSurface(Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    The root class for bounded surfaces in 3D space. A bounded surface is defined by a rectangle in its 2D parametric space, i.e. - its u parameter, which ranges between two finite values u0 and u1, referred to as "First u parameter" and "Last u parameter" respectively, and - its v parameter, which ranges between two finite values v0 and v1, referred to as "First v parameter" and the "Last v parameter" respectively. The surface is limited by four curves which are the boundaries of the surface: - its u0 and u1 isoparametric curves in the u parametric direction, and - its v0 and v1 isoparametric curves in the v parametric direction. A bounded surface is finite. The common behavior of all bounded surfaces is described by the Geom_Surface class. The Geom package provides three concrete implementations of bounded surfaces: - Geom_BezierSurface, - Geom_BSplineSurface, and - Geom_RectangularTrimmedSurface. The first two of these implement well known mathematical definitions of complex surfaces, the third trims a surface using four isoparametric curves, i.e. it limits the variation of its parameters to a rectangle in 2D parametric space.The root class for bounded surfaces in 3D space. A bounded surface is defined by a rectangle in its 2D parametric space, i.e. - its u parameter, which ranges between two finite values u0 and u1, referred to as "First u parameter" and "Last u parameter" respectively, and - its v parameter, which ranges between two finite values v0 and v1, referred to as "First v parameter" and the "Last v parameter" respectively. The surface is limited by four curves which are the boundaries of the surface: - its u0 and u1 isoparametric curves in the u parametric direction, and - its v0 and v1 isoparametric curves in the v parametric direction. A bounded surface is finite. The common behavior of all bounded surfaces is described by the Geom_Surface class. The Geom package provides three concrete implementations of bounded surfaces: - Geom_BezierSurface, - Geom_BSplineSurface, and - Geom_RectangularTrimmedSurface. The first two of these implement well known mathematical definitions of complex surfaces, the third trims a surface using four isoparametric curves, i.e. it limits the variation of its parameters to a rectangle in 2D parametric space.The root class for bounded surfaces in 3D space. A bounded surface is defined by a rectangle in its 2D parametric space, i.e. - its u parameter, which ranges between two finite values u0 and u1, referred to as "First u parameter" and "Last u parameter" respectively, and - its v parameter, which ranges between two finite values v0 and v1, referred to as "First v parameter" and the "Last v parameter" respectively. The surface is limited by four curves which are the boundaries of the surface: - its u0 and u1 isoparametric curves in the u parametric direction, and - its v0 and v1 isoparametric curves in the v parametric direction. A bounded surface is finite. The common behavior of all bounded surfaces is described by the Geom_Surface class. The Geom package provides three concrete implementations of bounded surfaces: - Geom_BezierSurface, - Geom_BSplineSurface, and - Geom_RectangularTrimmedSurface. The first two of these implement well known mathematical definitions of complex surfaces, the third trims a surface using four isoparametric curves, i.e. it limits the variation of its parameters to a rectangle in 2D parametric space.
    """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this surface. If the surface is infinite, this function can return a value equal to Precision::Infinite: instead of Standard_Real::LastReal.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the Global Continuity of the surface in direction U and V : C0 : only geometric continuity, C1 : continuity of the first derivative all along the surface, C2 : continuity of the second derivative all along the surface, C3 : continuity of the third derivative all along the surface, G1 : tangency continuity all along the surface, G2 : curvature continuity all along the surface, CN : the order of continuity is infinite. Example : If the surface is C1 in the V parametric direction and C2 in the U parametric direction Shape = C1.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U,V on the surface.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P and the first derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first and the second derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first,the second and the third derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        ---Purpose ; Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns the order of continuity of the surface in the U parametric direction. Raised if N < 0.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns the order of continuity of the surface in the V parametric direction. Raised if N < 0.
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
    def IsUClosed(self) -> bool: 
        """
        Checks whether this surface is closed in the u parametric direction. Returns true if, in the u parametric direction: taking uFirst and uLast as the parametric bounds in the u parametric direction, for each parameter v, the distance between the points P(uFirst, v) and P(uLast, v) is less than or equal to gp::Resolution().
        """
    def IsUPeriodic(self) -> bool: 
        """
        Checks if this surface is periodic in the u parametric direction. Returns true if: - this surface is closed in the u parametric direction, and - there is a constant T such that the distance between the points P (u, v) and P (u + T, v) (or the points P (u, v) and P (u, v + T)) is less than or equal to gp::Resolution(). Note: T is the parametric period in the u parametric direction.
        """
    def IsVClosed(self) -> bool: 
        """
        Checks whether this surface is closed in the u parametric direction. Returns true if, in the v parametric direction: taking vFirst and vLast as the parametric bounds in the v parametric direction, for each parameter u, the distance between the points P(u, vFirst) and P(u, vLast) is less than or equal to gp::Resolution().
        """
    def IsVPeriodic(self) -> bool: 
        """
        Checks if this surface is periodic in the v parametric direction. Returns true if: - this surface is closed in the v parametric direction, and - there is a constant T such that the distance between the points P (u, v) and P (u + T, v) (or the points P (u, v) and P (u, v + T)) is less than or equal to gp::Resolution(). Note: T is the parametric period in the v parametric direction.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the Ureversed surface for the point of parameter U on <me>.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Returns the parameter on the Vreversed surface for the point of parameter V on <me>.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
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
class Geom_BSplineCurve(Geom_BoundedCurve, Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Definition of the B_spline curve. A B-spline curve can be Uniform or non-uniform Rational or non-rational Periodic or non-periodicDefinition of the B_spline curve. A B-spline curve can be Uniform or non-uniform Rational or non-rational Periodic or non-periodicDefinition of the B_spline curve. A B-spline curve can be Uniform or non-uniform Rational or non-rational Periodic or non-periodic
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the global continuity of the curve : C0 : only geometric continuity, C1 : continuity of the first derivative all along the Curve, C2 : continuity of the second derivative all along the Curve, C3 : continuity of the third derivative all along the Curve, CN : the order of continuity is infinite. For a B-spline curve of degree d if a knot Ui has a multiplicity p the B-spline curve is only Cd-p continuous at Ui. So the global continuity of the curve can't be greater than Cd-p where p is the maximum multiplicity of the interior Knots. In the interior of a knot span the curve is infinitely continuously differentiable.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this BSpline curve.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the curve is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the curve is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the curve is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        For the point of parameter U of this BSpline curve, computes the vector corresponding to the Nth derivative. Warning On a point where the continuity of the curve is not the one requested, this function impacts the part defined by the parameter with a value greater than U, i.e. the part of the curve to the "right" of the singularity. Exceptions Standard_RangeError if N is less than 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
        """
        Returns the degree of this BSpline curve. The degree of a Geom_BSplineCurve curve cannot be greater than Geom_BSplineCurve::MaxDegree(). Computation of value and derivatives
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the last point of the curve. Warnings : The last point of the curve is different from the last pole of the curve if the multiplicity of the last knot is lower than Degree.
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter of this BSpline curve. This is a knot value. The first parameter is the one of the start point of the BSpline curve.
        """
    def FirstUKnotIndex(self) -> int: 
        """
        Returns the index in the knot array of the knot corresponding to the first or last parameter of this BSpline curve. For a BSpline curve, the first (or last) parameter (which gives the start (or end) point of the curve) is a knot value. However, if the multiplicity of the first (or last) knot is less than Degree + 1, where Degree is the degree of the curve, it is not the first (or last) knot of the curve.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncreaseDegree(self,Degree : int) -> None: 
        """
        Increases the degree of this BSpline curve to Degree. As a result, the poles, weights and multiplicities tables are modified; the knots table is not changed. Nothing is done if Degree is less than or equal to the current degree. Exceptions Standard_ConstructionError if Degree is greater than Geom_BSplineCurve::MaxDegree().
        """
    @overload
    def IncreaseMultiplicity(self,I1 : int,I2 : int,M : int) -> None: 
        """
        Increases the multiplicity of the knot <Index> to <M>.

        Increases the multiplicities of the knots in [I1,I2] to <M>.
        """
    @overload
    def IncreaseMultiplicity(self,Index : int,M : int) -> None: ...
    def IncrementMultiplicity(self,I1 : int,I2 : int,M : int) -> None: 
        """
        Increment the multiplicities of the knots in [I1,I2] by <M>.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InsertKnot(self,U : float,M : int=1,ParametricTolerance : float=0.0,Add : bool=True) -> None: 
        """
        Inserts a knot value in the sequence of knots. If <U> is an existing knot the multiplicity is increased by <M>.
        """
    def InsertKnots(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,ParametricTolerance : float=0.0,Add : bool=False) -> None: 
        """
        Inserts a set of knots values in the sequence of knots.
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns the continuity of the curve, the curve is at least C0. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns true if the distance between the first point and the last point of the curve is lower or equal to Resolution from package gp. Warnings : The first and the last point can be different from the first pole and the last pole of the curve.
        """
    def IsEqual(self,theOther : Geom_BSplineCurve,thePreci : float) -> bool: 
        """
        Comapare two Bspline curve on identity;
        """
    def IsG1(self,theTf : float,theTl : float,theAngTol : float) -> bool: 
        """
        Check if curve has at least G1 continuity in interval [theTf, theTl] Returns true if IsCN(1) or angle betweem "left" and "right" first derivatives at knots with C0 continuity is less then theAngTol only knots in interval [theTf, theTl] is checked
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
    def IsPeriodic(self) -> bool: 
        """
        Returns True if the curve is periodic.
        """
    def IsRational(self) -> bool: 
        """
        Returns True if the weights are not identical. The tolerance criterion is Epsilon of the class Real.
        """
    def Knot(self,Index : int) -> float: 
        """
        Returns the knot of range Index. When there is a knot with a multiplicity greater than 1 the knot is not repeated. The method Multiplicity can be used to get the multiplicity of the Knot. Raised if Index < 1 or Index > NbKnots
        """
    def KnotDistribution(self) -> OCP.GeomAbs.GeomAbs_BSplKnotDistribution: 
        """
        Returns NonUniform or Uniform or QuasiUniform or PiecewiseBezier. If all the knots differ by a positive constant from the preceding knot the BSpline Curve can be : - Uniform if all the knots are of multiplicity 1, - QuasiUniform if all the knots are of multiplicity 1 except for the first and last knot which are of multiplicity Degree + 1, - PiecewiseBezier if the first and last knots have multiplicity Degree + 1 and if interior knots have multiplicity Degree A piecewise Bezier with only two knots is a BezierCurve. else the curve is non uniform. The tolerance criterion is Epsilon from class Real.
        """
    @overload
    def KnotSequence(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Returns K, the knots sequence of this BSpline curve. In this sequence, knots with a multiplicity greater than 1 are repeated. In the case of a non-periodic curve the length of the sequence must be equal to the sum of the NbKnots multiplicities of the knots of the curve (where NbKnots is the number of knots of this BSpline curve). This sum is also equal to : NbPoles + Degree + 1 where NbPoles is the number of poles and Degree the degree of this BSpline curve. In the case of a periodic curve, if there are k periodic knots, the period is Knot(k+1) - Knot(1). The initial sequence is built by writing knots 1 to k+1, which are repeated according to their corresponding multiplicities. If Degree is the degree of the curve, the degree of continuity of the curve at the knot of index 1 (or k+1) is equal to c = Degree + 1 - Mult(1). c knots are then inserted at the beginning and end of the initial sequence: - the c values of knots preceding the first item Knot(k+1) in the initial sequence are inserted at the beginning; the period is subtracted from these c values; - the c values of knots following the last item Knot(1) in the initial sequence are inserted at the end; the period is added to these c values. The length of the sequence must therefore be equal to: NbPoles + 2*Degree - Mult(1) + 2. Example For a non-periodic BSpline curve of degree 2 where: - the array of knots is: { k1 k2 k3 k4 }, - with associated multiplicities: { 3 1 2 3 }, the knot sequence is: K = { k1 k1 k1 k2 k3 k3 k4 k4 k4 } For a periodic BSpline curve of degree 4 , which is "C1" continuous at the first knot, and where : - the periodic knots are: { k1 k2 k3 (k4) } (3 periodic knots: the points of parameter k1 and k4 are identical, the period is p = k4 - k1), - with associated multiplicities: { 3 1 2 (3) }, the degree of continuity at knots k1 and k4 is: Degree + 1 - Mult(i) = 2. 2 supplementary knots are added at the beginning and end of the sequence: - at the beginning: the 2 knots preceding k4 minus the period; in this example, this is k3 - p both times; - at the end: the 2 knots following k1 plus the period; in this example, this is k2 + p and k3 + p. The knot sequence is therefore: K = { k3-p k3-p k1 k1 k1 k2 k3 k3 k4 k4 k4 k2+p k3+p } Exceptions Raised if K.Lower() is less than number of first knot in knot sequence with repetitions or K.Upper() is more than number of last knot in knot sequence with repetitions.

        returns the knots of the B-spline curve. Knots with multiplicit greater than 1 are repeated
        """
    @overload
    def KnotSequence(self,K : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def Knots(self,K : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        returns the knot values of the B-spline curve; Warning A knot with a multiplicity greater than 1 is not repeated in the knot table. The Multiplicity function can be used to obtain the multiplicity of each knot.

        returns the knot values of the B-spline curve; Warning A knot with a multiplicity greater than 1 is not repeated in the knot table. The Multiplicity function can be used to obtain the multiplicity of each knot.
        """
    @overload
    def Knots(self) -> OCP.TColStd.TColStd_Array1OfReal: ...
    def LastParameter(self) -> float: 
        """
        Computes the parametric value of the end point of the curve. It is a knot value.
        """
    def LastUKnotIndex(self) -> int: 
        """
        For a BSpline curve the last parameter (which gives the end point of the curve) is a knot value but if the multiplicity of the last knot index is lower than Degree + 1 it is not the last knot of the curve. This method computes the index of the knot corresponding to the last parameter.
        """
    def LocalD0(self,U : float,FromK1 : int,ToK2 : int,P : OCP.gp.gp_Pnt) -> None: 
        """
        Raised if FromK1 = ToK2.
        """
    def LocalD1(self,U : float,FromK1 : int,ToK2 : int,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the local continuity of the curve is not C1 between the knot K1 and the knot K2. Raised if FromK1 = ToK2.
        """
    def LocalD2(self,U : float,FromK1 : int,ToK2 : int,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the local continuity of the curve is not C2 between the knot K1 and the knot K2. Raised if FromK1 = ToK2.
        """
    def LocalD3(self,U : float,FromK1 : int,ToK2 : int,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the local continuity of the curve is not C3 between the knot K1 and the knot K2. Raised if FromK1 = ToK2.
        """
    def LocalDN(self,U : float,FromK1 : int,ToK2 : int,N : int) -> OCP.gp.gp_Vec: 
        """
        Raised if the local continuity of the curve is not CN between the knot K1 and the knot K2. Raised if FromK1 = ToK2. Raised if N < 1.
        """
    def LocalValue(self,U : float,FromK1 : int,ToK2 : int) -> OCP.gp.gp_Pnt: 
        """
        Raised if FromK1 = ToK2.
        """
    def LocateU(self,U : float,ParametricTolerance : float,WithKnotRepetition : bool=False) -> Tuple[int, int]: 
        """
        Locates the parametric value U in the sequence of knots. If "WithKnotRepetition" is True we consider the knot's representation with repetition of multiple knot value, otherwise we consider the knot's representation with no repetition of multiple knot values. Knots (I1) <= U <= Knots (I2) . if I1 = I2 U is a knot value (the tolerance criterion ParametricTolerance is used). . if I1 < 1 => U < Knots (1) - Abs(ParametricTolerance) . if I2 > NbKnots => U > Knots (NbKnots) + Abs(ParametricTolerance)
        """
    @staticmethod
    def MaxDegree_s() -> int: 
        """
        Returns the value of the maximum degree of the normalized B-spline basis functions in this package.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def MovePoint(self,U : float,P : OCP.gp.gp_Pnt,Index1 : int,Index2 : int) -> Tuple[int, int]: 
        """
        Moves the point of parameter U of this BSpline curve to P. Index1 and Index2 are the indexes in the table of poles of this BSpline curve of the first and last poles designated to be moved. FirstModifiedPole and LastModifiedPole are the indexes of the first and last poles which are effectively modified. In the event of incompatibility between Index1, Index2 and the value U: - no change is made to this BSpline curve, and - the FirstModifiedPole and LastModifiedPole are returned null. Exceptions Standard_OutOfRange if: - Index1 is greater than or equal to Index2, or - Index1 or Index2 is less than 1 or greater than the number of poles of this BSpline curve.
        """
    def MovePointAndTangent(self,U : float,P : OCP.gp.gp_Pnt,Tangent : OCP.gp.gp_Vec,Tolerance : float,StartingCondition : int,EndingCondition : int) -> Tuple[int]: 
        """
        Move a point with parameter U to P. and makes it tangent at U be Tangent. StartingCondition = -1 means first can move EndingCondition = -1 means last point can move StartingCondition = 0 means the first point cannot move EndingCondition = 0 means the last point cannot move StartingCondition = 1 means the first point and tangent cannot move EndingCondition = 1 means the last point and tangent cannot move and so forth ErrorStatus != 0 means that there are not enought degree of freedom with the constrain to deform the curve accordingly
        """
    @overload
    def Multiplicities(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        Returns the multiplicity of the knots of the curve.

        returns the multiplicity of the knots of the curve.
        """
    @overload
    def Multiplicities(self,M : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
    def Multiplicity(self,Index : int) -> int: 
        """
        Returns the multiplicity of the knots of range Index. Raised if Index < 1 or Index > NbKnots
        """
    def NbKnots(self) -> int: 
        """
        Returns the number of knots. This method returns the number of knot without repetition of multiple knots.
        """
    def NbPoles(self) -> int: 
        """
        Returns the number of poles
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def PeriodicNormalization(self) -> Tuple[float]: 
        """
        returns the parameter normalized within the period if the curve is periodic : otherwise does not do anything
        """
    def Pole(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the pole of range Index. Raised if Index < 1 or Index > NbPoles.
        """
    @overload
    def Poles(self) -> OCP.TColgp.TColgp_Array1OfPnt: 
        """
        Returns the poles of the B-spline curve;

        Returns the poles of the B-spline curve;
        """
    @overload
    def Poles(self,P : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    def RemoveKnot(self,Index : int,M : int,Tolerance : float) -> bool: 
        """
        Reduces the multiplicity of the knot of index Index to M. If M is equal to 0, the knot is removed. With a modification of this type, the array of poles is also modified. Two different algorithms are systematically used to compute the new poles of the curve. If, for each pole, the distance between the pole calculated using the first algorithm and the same pole calculated using the second algorithm, is less than Tolerance, this ensures that the curve is not modified by more than Tolerance. Under these conditions, true is returned; otherwise, false is returned. A low tolerance is used to prevent modification of the curve. A high tolerance is used to "smooth" the curve. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table. pole insertion and pole removing this operation is limited to the Uniform or QuasiUniform BSplineCurve. The knot values are modified . If the BSpline is NonUniform or Piecewise Bezier an exception Construction error is raised.
        """
    def Resolution(self,Tolerance3D : float) -> Tuple[float]: 
        """
        Computes for this BSpline curve the parametric tolerance UTolerance for a given 3D tolerance Tolerance3D. If f(t) is the equation of this BSpline curve, UTolerance ensures that: | t1 - t0| < Utolerance ===> |f(t1) - f(t0)| < Tolerance3D
        """
    def Reverse(self) -> None: 
        """
        Changes the direction of parametrization of <me>. The Knot sequence is modified, the FirstParameter and the LastParameter are not modified. The StartPoint of the initial curve becomes the EndPoint of the reversed curve and the EndPoint of the initial curve becomes the StartPoint of the reversed curve.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the reversed curve for the point of parameter U on <me>.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def Segment(self,U1 : float,U2 : float,theTolerance : float=9.999999999999999e-10) -> None: 
        """
        Modifies this BSpline curve by segmenting it between U1 and U2. Either of these values can be outside the bounds of the curve, but U2 must be greater than U1. All data structure tables of this BSpline curve are modified, but the knots located between U1 and U2 are retained. The degree of the curve is not modified.
        """
    @overload
    def SetKnot(self,Index : int,K : float) -> None: 
        """
        Modifies this BSpline curve by assigning the value K to the knot of index Index in the knots table. This is a relatively local modification because K must be such that: Knots(Index - 1) < K < Knots(Index + 1) The second syntax allows you also to increase the multiplicity of the knot to M (but it is not possible to decrease the multiplicity of the knot with this function). Standard_ConstructionError if: - K is not such that: Knots(Index - 1) < K < Knots(Index + 1) - M is greater than the degree of this BSpline curve or lower than the previous multiplicity of knot of index Index in the knots table. Standard_OutOfRange if Index is outside the bounds of the knots table.

        Changes the knot of range Index with its multiplicity. You can increase the multiplicity of a knot but it is not allowed to decrease the multiplicity of an existing knot.
        """
    @overload
    def SetKnot(self,Index : int,K : float,M : int) -> None: ...
    def SetKnots(self,K : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Modifies this BSpline curve by assigning the array K to its knots table. The multiplicity of the knots is not modified. Exceptions Standard_ConstructionError if the values in the array K are not in ascending order. Standard_OutOfRange if the bounds of the array K are not respectively 1 and the number of knots of this BSpline curve.
        """
    def SetNotPeriodic(self) -> None: 
        """
        Changes this BSpline curve into a non-periodic curve. If this curve is already non-periodic, it is not modified. Note: the poles and knots tables are modified. Warning If this curve is periodic, as the multiplicity of the first and last knots is not modified, and is not equal to Degree + 1, where Degree is the degree of this BSpline curve, the start and end points of the curve are not its first and last poles.
        """
    @overload
    def SetOrigin(self,U : float,Tol : float) -> None: 
        """
        Assigns the knot of index Index in the knots table as the origin of this periodic BSpline curve. As a consequence, the knots and poles tables are modified. Exceptions Standard_NoSuchObject if this curve is not periodic. Standard_DomainError if Index is outside the bounds of the knots table.

        Set the origin of a periodic curve at Knot U. If U is not a knot of the BSpline a new knot is inseted. KnotVector and poles are modified. Raised if the curve is not periodic
        """
    @overload
    def SetOrigin(self,Index : int) -> None: ...
    def SetPeriodic(self) -> None: 
        """
        Changes this BSpline curve into a periodic curve. To become periodic, the curve must first be closed. Next, the knot sequence must be periodic. For this, FirstUKnotIndex and LastUKnotIndex are used to compute I1 and I2, the indexes in the knots array of the knots corresponding to the first and last parameters of this BSpline curve. The period is therefore: Knots(I2) - Knots(I1). Consequently, the knots and poles tables are modified. Exceptions Standard_ConstructionError if this BSpline curve is not closed.
        """
    @overload
    def SetPole(self,Index : int,P : OCP.gp.gp_Pnt,Weight : float) -> None: 
        """
        Modifies this BSpline curve by assigning P to the pole of index Index in the poles table. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table. Standard_ConstructionError if Weight is negative or null.

        Modifies this BSpline curve by assigning P to the pole of index Index in the poles table. This syntax also allows you to modify the weight of the modified pole, which becomes Weight. In this case, if this BSpline curve is non-rational, it can become rational and vice versa. Exceptions Standard_OutOfRange if Index is outside the bounds of the poles table. Standard_ConstructionError if Weight is negative or null.
        """
    @overload
    def SetPole(self,Index : int,P : OCP.gp.gp_Pnt) -> None: ...
    def SetWeight(self,Index : int,Weight : float) -> None: 
        """
        Changes the weight for the pole of range Index. If the curve was non rational it can become rational. If the curve was rational it can become non rational.
        """
    def StartPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the start point of the curve. Warnings : This point is different from the first pole of the curve if the multiplicity of the first knot is lower than Degree.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this BSpline curve.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    def Weight(self,Index : int) -> float: 
        """
        Returns the weight of the pole of range Index . Raised if Index < 1 or Index > NbPoles.
        """
    @overload
    def Weights(self,W : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the weights of the B-spline curve;

        Returns the weights of the B-spline curve;
        """
    @overload
    def Weights(self) -> OCP.TColStd.TColStd_Array1OfReal: ...
    @overload
    def __init__(self,Poles : OCP.TColgp.TColgp_Array1OfPnt,Knots : OCP.TColStd.TColStd_Array1OfReal,Multiplicities : OCP.TColStd.TColStd_Array1OfInteger,Degree : int,Periodic : bool=False) -> None: ...
    @overload
    def __init__(self,Poles : OCP.TColgp.TColgp_Array1OfPnt,Weights : OCP.TColStd.TColStd_Array1OfReal,Knots : OCP.TColStd.TColStd_Array1OfReal,Multiplicities : OCP.TColStd.TColStd_Array1OfInteger,Degree : int,Periodic : bool=False,CheckRational : bool=True) -> None: ...
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
class Geom_BSplineSurface(Geom_BoundedSurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a BSpline surface. In each parametric direction, a BSpline surface can be: - uniform or non-uniform, - rational or non-rational, - periodic or non-periodic. A BSpline surface is defined by: - its degrees, in the u and v parametric directions, - its periodic characteristic, in the u and v parametric directions, - a table of poles, also called control points (together with the associated weights if the surface is rational), and - a table of knots, together with the associated multiplicities. The degree of a Geom_BSplineSurface is limited to a value (25) which is defined and controlled by the system. This value is returned by the function MaxDegree. Poles and Weights Poles and Weights are manipulated using two associative double arrays: - the poles table, which is a double array of gp_Pnt points, and - the weights table, which is a double array of reals. The bounds of the poles and weights arrays are: - 1 and NbUPoles for the row bounds (provided that the BSpline surface is not periodic in the u parametric direction), where NbUPoles is the number of poles of the surface in the u parametric direction, and - 1 and NbVPoles for the column bounds (provided that the BSpline surface is not periodic in the v parametric direction), where NbVPoles is the number of poles of the surface in the v parametric direction. The poles of the surface are the points used to shape and reshape the surface. They comprise a rectangular network. If the surface is not periodic: - The points (1, 1), (NbUPoles, 1), (1, NbVPoles), and (NbUPoles, NbVPoles) are the four parametric "corners" of the surface. - The first column of poles and the last column of poles define two BSpline curves which delimit the surface in the v parametric direction. These are the v isoparametric curves corresponding to the two bounds of the v parameter. - The first row of poles and the last row of poles define two BSpline curves which delimit the surface in the u parametric direction. These are the u isoparametric curves corresponding to the two bounds of the u parameter. If the surface is periodic, these geometric properties are not verified. It is more difficult to define a geometrical significance for the weights. However they are useful for representing a quadric surface precisely. Moreover, if the weights of all the poles are equal, the surface has a polynomial equation, and hence is a "non-rational surface". The non-rational surface is a special, but frequently used, case, where all poles have identical weights. The weights are defined and used only in the case of a rational surface. The rational characteristic is defined in each parametric direction. A surface can be rational in the u parametric direction, and non-rational in the v parametric direction. Knots and Multiplicities For a Geom_BSplineSurface the table of knots is made up of two increasing sequences of reals, without repetition, one for each parametric direction. The multiplicities define the repetition of the knots. A BSpline surface comprises multiple contiguous patches, which are themselves polynomial or rational surfaces. The knots are the parameters of the isoparametric curves which limit these contiguous patches. The multiplicity of a knot on a BSpline surface (in a given parametric direction) is related to the degree of continuity of the surface at that knot in that parametric direction: Degree of continuity at knot(i) = Degree - Multi(i) where: - Degree is the degree of the BSpline surface in the given parametric direction, and - Multi(i) is the multiplicity of knot number i in the given parametric direction. There are some special cases, where the knots are regularly spaced in one parametric direction (i.e. the difference between two consecutive knots is a constant). - "Uniform": all the multiplicities are equal to 1. - "Quasi-uniform": all the multiplicities are equal to 1, except for the first and last knots in this parametric direction, and these are equal to Degree + 1. - "Piecewise Bezier": all the multiplicities are equal to Degree except for the first and last knots, which are equal to Degree + 1. This surface is a concatenation of Bezier patches in the given parametric direction. If the BSpline surface is not periodic in a given parametric direction, the bounds of the knots and multiplicities tables are 1 and NbKnots, where NbKnots is the number of knots of the BSpline surface in that parametric direction. If the BSpline surface is periodic in a given parametric direction, and there are k periodic knots and p periodic poles in that parametric direction: - the period is such that: period = Knot(k+1) - Knot(1), and - the poles and knots tables in that parametric direction can be considered as infinite tables, such that: Knot(i+k) = Knot(i) + period, and Pole(i+p) = Pole(i) Note: The data structure tables for a periodic BSpline surface are more complex than those of a non-periodic one. References : . A survey of curve and surface methods in CADG Wolfgang BOHM CAGD 1 (1984) . On de Boor-like algorithms and blossoming Wolfgang BOEHM cagd 5 (1988) . Blossoming and knot insertion algorithms for B-spline curves Ronald N. GOLDMAN . Modelisation des surfaces en CAO, Henri GIAUME Peugeot SA . Curves and Surfaces for Computer Aided Geometric Design, a practical guide Gerald FarinDescribes a BSpline surface. In each parametric direction, a BSpline surface can be: - uniform or non-uniform, - rational or non-rational, - periodic or non-periodic. A BSpline surface is defined by: - its degrees, in the u and v parametric directions, - its periodic characteristic, in the u and v parametric directions, - a table of poles, also called control points (together with the associated weights if the surface is rational), and - a table of knots, together with the associated multiplicities. The degree of a Geom_BSplineSurface is limited to a value (25) which is defined and controlled by the system. This value is returned by the function MaxDegree. Poles and Weights Poles and Weights are manipulated using two associative double arrays: - the poles table, which is a double array of gp_Pnt points, and - the weights table, which is a double array of reals. The bounds of the poles and weights arrays are: - 1 and NbUPoles for the row bounds (provided that the BSpline surface is not periodic in the u parametric direction), where NbUPoles is the number of poles of the surface in the u parametric direction, and - 1 and NbVPoles for the column bounds (provided that the BSpline surface is not periodic in the v parametric direction), where NbVPoles is the number of poles of the surface in the v parametric direction. The poles of the surface are the points used to shape and reshape the surface. They comprise a rectangular network. If the surface is not periodic: - The points (1, 1), (NbUPoles, 1), (1, NbVPoles), and (NbUPoles, NbVPoles) are the four parametric "corners" of the surface. - The first column of poles and the last column of poles define two BSpline curves which delimit the surface in the v parametric direction. These are the v isoparametric curves corresponding to the two bounds of the v parameter. - The first row of poles and the last row of poles define two BSpline curves which delimit the surface in the u parametric direction. These are the u isoparametric curves corresponding to the two bounds of the u parameter. If the surface is periodic, these geometric properties are not verified. It is more difficult to define a geometrical significance for the weights. However they are useful for representing a quadric surface precisely. Moreover, if the weights of all the poles are equal, the surface has a polynomial equation, and hence is a "non-rational surface". The non-rational surface is a special, but frequently used, case, where all poles have identical weights. The weights are defined and used only in the case of a rational surface. The rational characteristic is defined in each parametric direction. A surface can be rational in the u parametric direction, and non-rational in the v parametric direction. Knots and Multiplicities For a Geom_BSplineSurface the table of knots is made up of two increasing sequences of reals, without repetition, one for each parametric direction. The multiplicities define the repetition of the knots. A BSpline surface comprises multiple contiguous patches, which are themselves polynomial or rational surfaces. The knots are the parameters of the isoparametric curves which limit these contiguous patches. The multiplicity of a knot on a BSpline surface (in a given parametric direction) is related to the degree of continuity of the surface at that knot in that parametric direction: Degree of continuity at knot(i) = Degree - Multi(i) where: - Degree is the degree of the BSpline surface in the given parametric direction, and - Multi(i) is the multiplicity of knot number i in the given parametric direction. There are some special cases, where the knots are regularly spaced in one parametric direction (i.e. the difference between two consecutive knots is a constant). - "Uniform": all the multiplicities are equal to 1. - "Quasi-uniform": all the multiplicities are equal to 1, except for the first and last knots in this parametric direction, and these are equal to Degree + 1. - "Piecewise Bezier": all the multiplicities are equal to Degree except for the first and last knots, which are equal to Degree + 1. This surface is a concatenation of Bezier patches in the given parametric direction. If the BSpline surface is not periodic in a given parametric direction, the bounds of the knots and multiplicities tables are 1 and NbKnots, where NbKnots is the number of knots of the BSpline surface in that parametric direction. If the BSpline surface is periodic in a given parametric direction, and there are k periodic knots and p periodic poles in that parametric direction: - the period is such that: period = Knot(k+1) - Knot(1), and - the poles and knots tables in that parametric direction can be considered as infinite tables, such that: Knot(i+k) = Knot(i) + period, and Pole(i+p) = Pole(i) Note: The data structure tables for a periodic BSpline surface are more complex than those of a non-periodic one. References : . A survey of curve and surface methods in CADG Wolfgang BOHM CAGD 1 (1984) . On de Boor-like algorithms and blossoming Wolfgang BOEHM cagd 5 (1988) . Blossoming and knot insertion algorithms for B-spline curves Ronald N. GOLDMAN . Modelisation des surfaces en CAO, Henri GIAUME Peugeot SA . Curves and Surfaces for Computer Aided Geometric Design, a practical guide Gerald FarinDescribes a BSpline surface. In each parametric direction, a BSpline surface can be: - uniform or non-uniform, - rational or non-rational, - periodic or non-periodic. A BSpline surface is defined by: - its degrees, in the u and v parametric directions, - its periodic characteristic, in the u and v parametric directions, - a table of poles, also called control points (together with the associated weights if the surface is rational), and - a table of knots, together with the associated multiplicities. The degree of a Geom_BSplineSurface is limited to a value (25) which is defined and controlled by the system. This value is returned by the function MaxDegree. Poles and Weights Poles and Weights are manipulated using two associative double arrays: - the poles table, which is a double array of gp_Pnt points, and - the weights table, which is a double array of reals. The bounds of the poles and weights arrays are: - 1 and NbUPoles for the row bounds (provided that the BSpline surface is not periodic in the u parametric direction), where NbUPoles is the number of poles of the surface in the u parametric direction, and - 1 and NbVPoles for the column bounds (provided that the BSpline surface is not periodic in the v parametric direction), where NbVPoles is the number of poles of the surface in the v parametric direction. The poles of the surface are the points used to shape and reshape the surface. They comprise a rectangular network. If the surface is not periodic: - The points (1, 1), (NbUPoles, 1), (1, NbVPoles), and (NbUPoles, NbVPoles) are the four parametric "corners" of the surface. - The first column of poles and the last column of poles define two BSpline curves which delimit the surface in the v parametric direction. These are the v isoparametric curves corresponding to the two bounds of the v parameter. - The first row of poles and the last row of poles define two BSpline curves which delimit the surface in the u parametric direction. These are the u isoparametric curves corresponding to the two bounds of the u parameter. If the surface is periodic, these geometric properties are not verified. It is more difficult to define a geometrical significance for the weights. However they are useful for representing a quadric surface precisely. Moreover, if the weights of all the poles are equal, the surface has a polynomial equation, and hence is a "non-rational surface". The non-rational surface is a special, but frequently used, case, where all poles have identical weights. The weights are defined and used only in the case of a rational surface. The rational characteristic is defined in each parametric direction. A surface can be rational in the u parametric direction, and non-rational in the v parametric direction. Knots and Multiplicities For a Geom_BSplineSurface the table of knots is made up of two increasing sequences of reals, without repetition, one for each parametric direction. The multiplicities define the repetition of the knots. A BSpline surface comprises multiple contiguous patches, which are themselves polynomial or rational surfaces. The knots are the parameters of the isoparametric curves which limit these contiguous patches. The multiplicity of a knot on a BSpline surface (in a given parametric direction) is related to the degree of continuity of the surface at that knot in that parametric direction: Degree of continuity at knot(i) = Degree - Multi(i) where: - Degree is the degree of the BSpline surface in the given parametric direction, and - Multi(i) is the multiplicity of knot number i in the given parametric direction. There are some special cases, where the knots are regularly spaced in one parametric direction (i.e. the difference between two consecutive knots is a constant). - "Uniform": all the multiplicities are equal to 1. - "Quasi-uniform": all the multiplicities are equal to 1, except for the first and last knots in this parametric direction, and these are equal to Degree + 1. - "Piecewise Bezier": all the multiplicities are equal to Degree except for the first and last knots, which are equal to Degree + 1. This surface is a concatenation of Bezier patches in the given parametric direction. If the BSpline surface is not periodic in a given parametric direction, the bounds of the knots and multiplicities tables are 1 and NbKnots, where NbKnots is the number of knots of the BSpline surface in that parametric direction. If the BSpline surface is periodic in a given parametric direction, and there are k periodic knots and p periodic poles in that parametric direction: - the period is such that: period = Knot(k+1) - Knot(1), and - the poles and knots tables in that parametric direction can be considered as infinite tables, such that: Knot(i+k) = Knot(i) + period, and Pole(i+p) = Pole(i) Note: The data structure tables for a periodic BSpline surface are more complex than those of a non-periodic one. References : . A survey of curve and surface methods in CADG Wolfgang BOHM CAGD 1 (1984) . On de Boor-like algorithms and blossoming Wolfgang BOEHM cagd 5 (1988) . Blossoming and knot insertion algorithms for B-spline curves Ronald N. GOLDMAN . Modelisation des surfaces en CAO, Henri GIAUME Peugeot SA . Curves and Surfaces for Computer Aided Geometric Design, a practical guide Gerald Farin
    """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds of the surface. Warnings : These parametric values are the bounds of the array of knots UKnots and VKnots only if the first knots and the last knots have a multiplicity equal to UDegree + 1 or VDegree + 1
        """
    def CheckAndSegment(self,U1 : float,U2 : float,V1 : float,V2 : float,theUTolerance : float=9.999999999999999e-10,theVTolerance : float=9.999999999999999e-10) -> None: 
        """
        Segments the surface between U1 and U2 in the U-Direction. between V1 and V2 in the V-Direction.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of the surface : C0 : only geometric continuity, C1 : continuity of the first derivative all along the Surface, C2 : continuity of the second derivative all along the Surface, C3 : continuity of the third derivative all along the Surface, CN : the order of continuity is infinite. A B-spline surface is infinitely continuously differentiable for the couple of parameters U, V such thats U != UKnots(i) and V != VKnots(i). The continuity of the surface at a knot value depends on the multiplicity of this knot. Example : If the surface is C1 in the V direction and C2 in the U direction this function returns Shape = C1.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this BSpline surface.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the surface is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the surface is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the surface is not C3.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Nu is the order of derivation in the U parametric direction and Nv is the order of derivation in the V parametric direction.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExchangeUV(self) -> None: 
        """
        Exchanges the u and v parametric directions on this BSpline surface. As a consequence: - the poles and weights tables are transposed, - the knots and multiplicities tables are exchanged, - degrees of continuity, and rational, periodic and uniform characteristics are exchanged, and - the orientation of the surface is inverted.
        """
    def FirstUKnotIndex(self) -> int: 
        """
        Computes the Index of the UKnots which gives the first parametric value of the surface in the U direction. The UIso curve corresponding to this value is a boundary curve of the surface.
        """
    def FirstVKnotIndex(self) -> int: 
        """
        Computes the Index of the VKnots which gives the first parametric value of the surface in the V direction. The VIso curve corresponding to this knot is a boundary curve of the surface.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncreaseDegree(self,UDegree : int,VDegree : int) -> None: 
        """
        Increases the degrees of this BSpline surface to UDegree and VDegree in the u and v parametric directions respectively. As a result, the tables of poles, weights and multiplicities are modified. The tables of knots is not changed. Note: Nothing is done if the given degree is less than or equal to the current degree in the corresponding parametric direction. Exceptions Standard_ConstructionError if UDegree or VDegree is greater than Geom_BSplineSurface::MaxDegree().
        """
    @overload
    def IncreaseUMultiplicity(self,FromI1 : int,ToI2 : int,M : int) -> None: 
        """
        Increases the multiplicity of the knot of range UIndex in the UKnots sequence. M is the new multiplicity. M must be greater than the previous multiplicity and lower or equal to the degree of the surface in the U parametric direction. Raised if M is not in the range [1, UDegree]

        Increases until order M the multiplicity of the set of knots FromI1,...., ToI2 in the U direction. This method can be used to make a B_spline surface into a PiecewiseBezier B_spline surface. If <me> was uniform, it can become non uniform.
        """
    @overload
    def IncreaseUMultiplicity(self,UIndex : int,M : int) -> None: ...
    @overload
    def IncreaseVMultiplicity(self,VIndex : int,M : int) -> None: 
        """
        Increases the multiplicity of a knot in the V direction. M is the new multiplicity.

        Increases until order M the multiplicity of the set of knots FromI1,...., ToI2 in the V direction. This method can be used to make a BSplineSurface into a PiecewiseBezier B_spline surface. If <me> was uniform, it can become non-uniform.
        """
    @overload
    def IncreaseVMultiplicity(self,FromI1 : int,ToI2 : int,M : int) -> None: ...
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IncrementUMultiplicity(self,FromI1 : int,ToI2 : int,Step : int) -> None: 
        """
        Increments the multiplicity of the consecutives uknots FromI1..ToI2 by step. The multiplicity of each knot FromI1,.....,ToI2 must be lower or equal to the UDegree of the B_spline.
        """
    def IncrementVMultiplicity(self,FromI1 : int,ToI2 : int,Step : int) -> None: 
        """
        Increments the multiplicity of the consecutives vknots FromI1..ToI2 by step. The multiplicity of each knot FromI1,.....,ToI2 must be lower or equal to the VDegree of the B_spline.
        """
    def InsertUKnot(self,U : float,M : int,ParametricTolerance : float,Add : bool=True) -> None: 
        """
        Inserts a knot value in the sequence of UKnots. If U is a knot value this method increases the multiplicity of the knot if the previous multiplicity was lower than M else it does nothing. The tolerance criterion is ParametricTolerance. ParametricTolerance should be greater or equal than Resolution from package gp.
        """
    def InsertUKnots(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,ParametricTolerance : float=0.0,Add : bool=True) -> None: 
        """
        Inserts into the knots table for the U parametric direction of this BSpline surface: - the values of the array Knots, with their respective multiplicities, Mults. If the knot value to insert already exists in the table, its multiplicity is: - increased by M, if Add is true (the default), or - increased to M, if Add is false. The tolerance criterion used to check the equality of the knots is the larger of the values ParametricTolerance and Standard_Real::Epsilon(val), where val is the knot value to be inserted. Warning - If a given multiplicity coefficient is null, or negative, nothing is done. - The new multiplicity of a knot is limited to the degree of this BSpline surface in the corresponding parametric direction. Exceptions Standard_ConstructionError if a knot value to insert is outside the bounds of this BSpline surface in the specified parametric direction. The comparison uses the precision criterion ParametricTolerance.
        """
    def InsertVKnot(self,V : float,M : int,ParametricTolerance : float,Add : bool=True) -> None: 
        """
        Inserts a knot value in the sequence of VKnots. If V is a knot value this method increases the multiplicity of the knot if the previous multiplicity was lower than M otherwise it does nothing. The tolerance criterion is ParametricTolerance. ParametricTolerance should be greater or equal than Resolution from package gp.
        """
    def InsertVKnots(self,Knots : OCP.TColStd.TColStd_Array1OfReal,Mults : OCP.TColStd.TColStd_Array1OfInteger,ParametricTolerance : float=0.0,Add : bool=True) -> None: 
        """
        Inserts into the knots table for the V parametric direction of this BSpline surface: - the values of the array Knots, with their respective multiplicities, Mults. If the knot value to insert already exists in the table, its multiplicity is: - increased by M, if Add is true (the default), or - increased to M, if Add is false. The tolerance criterion used to check the equality of the knots is the larger of the values ParametricTolerance and Standard_Real::Epsilon(val), where val is the knot value to be inserted. Warning - If a given multiplicity coefficient is null, or negative, nothing is done. - The new multiplicity of a knot is limited to the degree of this BSpline surface in the corresponding parametric direction. Exceptions Standard_ConstructionError if a knot value to insert is outside the bounds of this BSpline surface in the specified parametric direction. The comparison uses the precision criterion ParametricTolerance.
        """
    def IsCNu(self,N : int) -> bool: 
        """
        Returns True if the order of continuity of the surface in the U direction is N. Raised if N < 0.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns True if the order of continuity of the surface in the V direction is N. Raised if N < 0.
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
    def IsUClosed(self) -> bool: 
        """
        Returns true if the first control points row and the last control points row are identical. The tolerance criterion is Resolution from package gp.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns True if the surface is closed in the U direction and if the B-spline has been turned into a periodic surface using the function SetUPeriodic.
        """
    def IsURational(self) -> bool: 
        """
        Returns False if for each row of weights all the weights are identical. The tolerance criterion is resolution from package gp. Example : |1.0, 1.0, 1.0| if Weights = |0.5, 0.5, 0.5| returns False |2.0, 2.0, 2.0|
        """
    def IsVClosed(self) -> bool: 
        """
        Returns true if the first control points column and the last last control points column are identical. The tolerance criterion is Resolution from package gp.
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns True if the surface is closed in the V direction and if the B-spline has been turned into a periodic surface using the function SetVPeriodic.
        """
    def IsVRational(self) -> bool: 
        """
        Returns False if for each column of weights all the weights are identical. The tolerance criterion is resolution from package gp. Examples : |1.0, 2.0, 0.5| if Weights = |1.0, 2.0, 0.5| returns False |1.0, 2.0, 0.5|
        """
    def LastUKnotIndex(self) -> int: 
        """
        Computes the Index of the UKnots which gives the last parametric value of the surface in the U direction. The UIso curve corresponding to this knot is a boundary curve of the surface.
        """
    def LastVKnotIndex(self) -> int: 
        """
        Computes the Index of the VKnots which gives the last parametric value of the surface in the V direction. The VIso curve corresponding to this knot is a boundary curve of the surface.
        """
    def LocalD0(self,U : float,V : float,FromUK1 : int,ToUK2 : int,FromVK1 : int,ToVK2 : int,P : OCP.gp.gp_Pnt) -> None: 
        """
        Raised if FromUK1 = ToUK2 or FromVK1 = ToVK2.
        """
    def LocalD1(self,U : float,V : float,FromUK1 : int,ToUK2 : int,FromVK1 : int,ToVK2 : int,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the local continuity of the surface is not C1 between the knots FromUK1, ToUK2 and FromVK1, ToVK2. Raised if FromUK1 = ToUK2 or FromVK1 = ToVK2.
        """
    def LocalD2(self,U : float,V : float,FromUK1 : int,ToUK2 : int,FromVK1 : int,ToVK2 : int,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the local continuity of the surface is not C2 between the knots FromUK1, ToUK2 and FromVK1, ToVK2. Raised if FromUK1 = ToUK2 or FromVK1 = ToVK2.
        """
    def LocalD3(self,U : float,V : float,FromUK1 : int,ToUK2 : int,FromVK1 : int,ToVK2 : int,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the local continuity of the surface is not C3 between the knots FromUK1, ToUK2 and FromVK1, ToVK2. Raised if FromUK1 = ToUK2 or FromVK1 = ToVK2.
        """
    def LocalDN(self,U : float,V : float,FromUK1 : int,ToUK2 : int,FromVK1 : int,ToVK2 : int,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Raised if the local continuity of the surface is not CNu between the knots FromUK1, ToUK2 and CNv between the knots FromVK1, ToVK2. Raised if FromUK1 = ToUK2 or FromVK1 = ToVK2.
        """
    def LocalValue(self,U : float,V : float,FromUK1 : int,ToUK2 : int,FromVK1 : int,ToVK2 : int) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U, V on the BSpline surface patch defines between the knots UK1 UK2, VK1, VK2. U can be out of the bounds [Knot UK1, Knot UK2] and V can be outof the bounds [Knot VK1, Knot VK2] but for the computation we only use the definition of the surface between these knot values. Raises if FromUK1 = ToUK2 or FromVK1 = ToVK2.
        """
    def LocateU(self,U : float,ParametricTolerance : float,WithKnotRepetition : bool=False) -> Tuple[int, int]: 
        """
        Locates the parametric value U in the sequence of UKnots. If "WithKnotRepetition" is True we consider the knot's representation with repetition of multiple knot value, otherwise we consider the knot's representation with no repetition of multiple knot values. UKnots (I1) <= U <= UKnots (I2) . if I1 = I2 U is a knot value (the tolerance criterion ParametricTolerance is used). . if I1 < 1 => U < UKnots(1) - Abs(ParametricTolerance) . if I2 > NbUKnots => U > UKnots(NbUKnots)+Abs(ParametricTolerance)
        """
    def LocateV(self,V : float,ParametricTolerance : float,WithKnotRepetition : bool=False) -> Tuple[int, int]: 
        """
        Locates the parametric value V in the sequence of knots. If "WithKnotRepetition" is True we consider the knot's representation with repetition of multiple knot value, otherwise we consider the knot's representation with no repetition of multiple knot values. VKnots (I1) <= V <= VKnots (I2) . if I1 = I2 V is a knot value (the tolerance criterion ParametricTolerance is used). . if I1 < 1 => V < VKnots(1) - Abs(ParametricTolerance) . if I2 > NbVKnots => V > VKnots(NbVKnots)+Abs(ParametricTolerance) poles insertion and removing The following methods are available only if the surface is Uniform or QuasiUniform in the considered direction The knot repartition is modified.
        """
    @staticmethod
    def MaxDegree_s() -> int: 
        """
        Returns the value of the maximum degree of the normalized B-spline basis functions in the u and v directions.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def MovePoint(self,U : float,V : float,P : OCP.gp.gp_Pnt,UIndex1 : int,UIndex2 : int,VIndex1 : int,VIndex2 : int) -> Tuple[int, int, int, int]: 
        """
        Move a point with parameter U and V to P. given u,v as parameters) to reach a new position UIndex1, UIndex2, VIndex1, VIndex2: indicates the poles which can be moved if Problem in BSplineBasis calculation, no change for the curve and UFirstIndex, VLastIndex = 0 VFirstIndex, VLastIndex = 0
        """
    def NbUKnots(self) -> int: 
        """
        Returns the number of knots in the U direction.
        """
    def NbUPoles(self) -> int: 
        """
        Returns number of poles in the U direction.
        """
    def NbVKnots(self) -> int: 
        """
        Returns the number of knots in the V direction.
        """
    def NbVPoles(self) -> int: 
        """
        Returns the number of poles in the V direction.
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def PeriodicNormalization(self) -> Tuple[float, float]: 
        """
        returns the parameter normalized within the period if the surface is periodic : otherwise does not do anything
        """
    def Pole(self,UIndex : int,VIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the pole of range (UIndex, VIndex).
        """
    @overload
    def Poles(self,P : OCP.TColgp.TColgp_Array2OfPnt) -> None: 
        """
        Returns the poles of the B-spline surface.

        Returns the poles of the B-spline surface.
        """
    @overload
    def Poles(self) -> OCP.TColgp.TColgp_Array2OfPnt: ...
    def RemoveUKnot(self,Index : int,M : int,Tolerance : float) -> bool: 
        """
        Reduces to M the multiplicity of the knot of index Index in the U parametric direction. If M is 0, the knot is removed. With a modification of this type, the table of poles is also modified. Two different algorithms are used systematically to compute the new poles of the surface. For each pole, the distance between the pole calculated using the first algorithm and the same pole calculated using the second algorithm, is checked. If this distance is less than Tolerance it ensures that the surface is not modified by more than Tolerance. Under these conditions, the function returns true; otherwise, it returns false. A low tolerance prevents modification of the surface. A high tolerance "smoothes" the surface. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of this BSpline surface.
        """
    def RemoveVKnot(self,Index : int,M : int,Tolerance : float) -> bool: 
        """
        Reduces to M the multiplicity of the knot of index Index in the V parametric direction. If M is 0, the knot is removed. With a modification of this type, the table of poles is also modified. Two different algorithms are used systematically to compute the new poles of the surface. For each pole, the distance between the pole calculated using the first algorithm and the same pole calculated using the second algorithm, is checked. If this distance is less than Tolerance it ensures that the surface is not modified by more than Tolerance. Under these conditions, the function returns true; otherwise, it returns false. A low tolerance prevents modification of the surface. A high tolerance "smoothes" the surface. Exceptions Standard_OutOfRange if Index is outside the bounds of the knots table of this BSpline surface.
        """
    def Resolution(self,Tolerance3D : float) -> Tuple[float, float]: 
        """
        Computes two tolerance values for this BSpline surface, based on the given tolerance in 3D space Tolerance3D. The tolerances computed are: - UTolerance in the u parametric direction, and - VTolerance in the v parametric direction. If f(u,v) is the equation of this BSpline surface, UTolerance and VTolerance guarantee that : | u1 - u0 | < UTolerance and | v1 - v0 | < VTolerance ====> |f (u1,v1) - f (u0,v0)| < Tolerance3D
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def Segment(self,U1 : float,U2 : float,V1 : float,V2 : float,theUTolerance : float=9.999999999999999e-10,theVTolerance : float=9.999999999999999e-10) -> None: 
        """
        Segments the surface between U1 and U2 in the U-Direction. between V1 and V2 in the V-Direction. The control points are modified, the first and the last point are not the same.
        """
    @overload
    def SetPole(self,UIndex : int,VIndex : int,P : OCP.gp.gp_Pnt) -> None: 
        """
        Substitutes the pole of range (UIndex, VIndex) with P. If the surface is rational the weight of range (UIndex, VIndex) is not modified.

        Substitutes the pole and the weight of range (UIndex, VIndex) with P and W.
        """
    @overload
    def SetPole(self,UIndex : int,VIndex : int,P : OCP.gp.gp_Pnt,Weight : float) -> None: ...
    @overload
    def SetPoleCol(self,VIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        Changes a column of poles or a part of this column. Raised if Vindex < 1 or VIndex > NbVPoles.

        Changes a column of poles or a part of this column with the corresponding weights. If the surface was rational it can become non rational. If the surface was non rational it can become rational. Raised if Vindex < 1 or VIndex > NbVPoles.
        """
    @overload
    def SetPoleCol(self,VIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def SetPoleRow(self,UIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Changes a row of poles or a part of this row with the corresponding weights. If the surface was rational it can become non rational. If the surface was non rational it can become rational. Raised if Uindex < 1 or UIndex > NbUPoles.

        Changes a row of poles or a part of this row. Raised if Uindex < 1 or UIndex > NbUPoles.
        """
    @overload
    def SetPoleRow(self,UIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def SetUKnot(self,UIndex : int,K : float,M : int) -> None: 
        """
        Substitutes the UKnots of range UIndex with K.

        Changes the value of the UKnots of range UIndex and increases its multiplicity.
        """
    @overload
    def SetUKnot(self,UIndex : int,K : float) -> None: ...
    def SetUKnots(self,UK : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Changes all the U-knots of the surface. The multiplicity of the knots are not modified.
        """
    def SetUNotPeriodic(self) -> None: 
        """
        Sets the surface U not periodic. Changes this BSpline surface into a non-periodic surface along U direction. If this surface is already non-periodic, it is not modified. Note: the poles and knots tables are modified.
        """
    def SetUOrigin(self,Index : int) -> None: 
        """
        Assigns the knot of index Index in the knots table in the corresponding parametric direction to be the origin of this periodic BSpline surface. As a consequence, the knots and poles tables are modified. Exceptions Standard_NoSuchObject if this BSpline surface is not periodic in the given parametric direction. Standard_DomainError if Index is outside the bounds of the knots table in the given parametric direction.
        """
    def SetUPeriodic(self) -> None: 
        """
        Sets the surface U periodic. Modifies this surface to be periodic in the U parametric direction. To become periodic in a given parametric direction a surface must be closed in that parametric direction, and the knot sequence relative to that direction must be periodic. To generate this periodic sequence of knots, the functions FirstUKnotIndex and LastUKnotIndex are used to compute I1 and I2. These are the indexes, in the knot array associated with the given parametric direction, of the knots that correspond to the first and last parameters of this BSpline surface in the given parametric direction. Hence the period is: Knots(I1) - Knots(I2) As a result, the knots and poles tables are modified. Exceptions Standard_ConstructionError if the surface is not closed in the given parametric direction.
        """
    @overload
    def SetVKnot(self,VIndex : int,K : float,M : int) -> None: 
        """
        Substitutes the VKnots of range VIndex with K.

        Changes the value of the VKnots of range VIndex and increases its multiplicity.
        """
    @overload
    def SetVKnot(self,VIndex : int,K : float) -> None: ...
    def SetVKnots(self,VK : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Changes all the V-knots of the surface. The multiplicity of the knots are not modified.
        """
    def SetVNotPeriodic(self) -> None: 
        """
        Sets the surface V not periodic. Changes this BSpline surface into a non-periodic surface along V direction. If this surface is already non-periodic, it is not modified. Note: the poles and knots tables are modified.
        """
    def SetVOrigin(self,Index : int) -> None: 
        """
        Assigns the knot of index Index in the knots table in the corresponding parametric direction to be the origin of this periodic BSpline surface. As a consequence, the knots and poles tables are modified. Exceptions Standard_NoSuchObject if this BSpline surface is not periodic in the given parametric direction. Standard_DomainError if Index is outside the bounds of the knots table in the given parametric direction.
        """
    def SetVPeriodic(self) -> None: 
        """
        Sets the surface V periodic. Modifies this surface to be periodic in the V parametric direction. To become periodic in a given parametric direction a surface must be closed in that parametric direction, and the knot sequence relative to that direction must be periodic. To generate this periodic sequence of knots, the functions FirstVKnotIndex and LastVKnotIndex are used to compute I1 and I2. These are the indexes, in the knot array associated with the given parametric direction, of the knots that correspond to the first and last parameters of this BSpline surface in the given parametric direction. Hence the period is: Knots(I1) - Knots(I2) As a result, the knots and poles tables are modified. Exceptions Standard_ConstructionError if the surface is not closed in the given parametric direction.
        """
    def SetWeight(self,UIndex : int,VIndex : int,Weight : float) -> None: 
        """
        Changes the weight of the pole of range UIndex, VIndex. If the surface was non rational it can become rational. If the surface was rational it can become non rational.
        """
    def SetWeightCol(self,VIndex : int,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Changes a column of weights of a part of this column.
        """
    def SetWeightRow(self,UIndex : int,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Changes a row of weights or a part of this row.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this BSpline surface.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UDegree(self) -> int: 
        """
        Returns the degree of the normalized B-splines Ni,n in the U direction.
        """
    @overload
    def UIso(self,U : float,CheckRational : bool) -> Geom_Curve: 
        """
        Computes the U isoparametric curve. A B-spline curve is returned.

        Computes the U isoparametric curve. If CheckRational=False, no try to make it non-rational. A B-spline curve is returned.
        """
    @overload
    def UIso(self,U : float) -> Geom_Curve: ...
    def UKnot(self,UIndex : int) -> float: 
        """
        Returns the Knot value of range UIndex. Raised if UIndex < 1 or UIndex > NbUKnots
        """
    def UKnotDistribution(self) -> OCP.GeomAbs.GeomAbs_BSplKnotDistribution: 
        """
        Returns NonUniform or Uniform or QuasiUniform or PiecewiseBezier. If all the knots differ by a positive constant from the preceding knot in the U direction the B-spline surface can be : - Uniform if all the knots are of multiplicity 1, - QuasiUniform if all the knots are of multiplicity 1 except for the first and last knot which are of multiplicity Degree + 1, - PiecewiseBezier if the first and last knots have multiplicity Degree + 1 and if interior knots have multiplicity Degree otherwise the surface is non uniform in the U direction The tolerance criterion is Resolution from package gp.
        """
    @overload
    def UKnotSequence(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Returns the uknots sequence. In this sequence the knots with a multiplicity greater than 1 are repeated. Example : Ku = {k1, k1, k1, k2, k3, k3, k4, k4, k4}

        Returns the uknots sequence. In this sequence the knots with a multiplicity greater than 1 are repeated. Example : Ku = {k1, k1, k1, k2, k3, k3, k4, k4, k4}
        """
    @overload
    def UKnotSequence(self,Ku : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def UKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Returns the knots in the U direction.

        Returns the knots in the U direction.
        """
    @overload
    def UKnots(self,Ku : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def UMultiplicities(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        Returns the multiplicities of the knots in the U direction.

        Returns the multiplicities of the knots in the U direction.
        """
    @overload
    def UMultiplicities(self,Mu : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
    def UMultiplicity(self,UIndex : int) -> int: 
        """
        Returns the multiplicity value of knot of range UIndex in the u direction. Raised if UIndex < 1 or UIndex > NbUKnots.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Changes the orientation of this BSpline surface in the U parametric direction. The bounds of the surface are not changed but the given parametric direction is reversed. Hence the orientation of the surface is reversed. The knots and poles tables are modified.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Computes the u parameter on the modified surface, produced by reversing its U parametric direction, for the point of u parameter U, on this BSpline surface. For a BSpline surface, these functions return respectively: - UFirst + ULast - U, where UFirst, ULast are the values of the first and last parameters of this BSpline surface, in the u parametric directions.
        """
    def VDegree(self) -> int: 
        """
        Returns the degree of the normalized B-splines Ni,d in the V direction.
        """
    @overload
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve. A B-spline curve is returned.

        Computes the V isoparametric curve. If CheckRational=False, no try to make it non-rational. A B-spline curve is returned. transformations
        """
    @overload
    def VIso(self,V : float,CheckRational : bool) -> Geom_Curve: ...
    def VKnot(self,VIndex : int) -> float: 
        """
        Returns the Knot value of range VIndex. Raised if VIndex < 1 or VIndex > NbVKnots
        """
    def VKnotDistribution(self) -> OCP.GeomAbs.GeomAbs_BSplKnotDistribution: 
        """
        Returns NonUniform or Uniform or QuasiUniform or PiecewiseBezier. If all the knots differ by a positive constant from the preceding knot in the V direction the B-spline surface can be : - Uniform if all the knots are of multiplicity 1, - QuasiUniform if all the knots are of multiplicity 1 except for the first and last knot which are of multiplicity Degree + 1, - PiecewiseBezier if the first and last knots have multiplicity Degree + 1 and if interior knots have multiplicity Degree otherwise the surface is non uniform in the V direction. The tolerance criterion is Resolution from package gp.
        """
    @overload
    def VKnotSequence(self,Kv : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the vknots sequence. In this sequence the knots with a multiplicity greater than 1 are repeated. Example : Kv = {k1, k1, k1, k2, k3, k3, k4, k4, k4}

        Returns the vknots sequence. In this sequence the knots with a multiplicity greater than 1 are repeated. Example : Ku = {k1, k1, k1, k2, k3, k3, k4, k4, k4}
        """
    @overload
    def VKnotSequence(self) -> OCP.TColStd.TColStd_Array1OfReal: ...
    @overload
    def VKnots(self,Kv : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the knots in the V direction.

        Returns the knots in the V direction.
        """
    @overload
    def VKnots(self) -> OCP.TColStd.TColStd_Array1OfReal: ...
    @overload
    def VMultiplicities(self,Mv : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Returns the multiplicities of the knots in the V direction.

        Returns the multiplicities of the knots in the V direction.
        """
    @overload
    def VMultiplicities(self) -> OCP.TColStd.TColStd_Array1OfInteger: ...
    def VMultiplicity(self,VIndex : int) -> int: 
        """
        Returns the multiplicity value of knot of range VIndex in the v direction. Raised if VIndex < 1 or VIndex > NbVKnots
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Changes the orientation of this BSpline surface in the V parametric direction. The bounds of the surface are not changed but the given parametric direction is reversed. Hence the orientation of the surface is reversed. The knots and poles tables are modified.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Computes the v parameter on the modified surface, produced by reversing its V parametric direction, for the point of v parameter V on this BSpline surface. For a BSpline surface, these functions return respectively: - VFirst + VLast - V, VFirst and VLast are the values of the first and last parameters of this BSpline surface, in the v pametric directions.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    def Weight(self,UIndex : int,VIndex : int) -> float: 
        """
        Returns the weight value of range UIndex, VIndex.
        """
    @overload
    def Weights(self) -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        Returns the weights of the B-spline surface.

        Returns the weights of the B-spline surface. value and derivatives computation
        """
    @overload
    def Weights(self,W : OCP.TColStd.TColStd_Array2OfReal) -> None: ...
    @overload
    def __init__(self,Poles : OCP.TColgp.TColgp_Array2OfPnt,Weights : OCP.TColStd.TColStd_Array2OfReal,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,UDegree : int,VDegree : int,UPeriodic : bool=False,VPeriodic : bool=False) -> None: ...
    @overload
    def __init__(self,Poles : OCP.TColgp.TColgp_Array2OfPnt,UKnots : OCP.TColStd.TColStd_Array1OfReal,VKnots : OCP.TColStd.TColStd_Array1OfReal,UMults : OCP.TColStd.TColStd_Array1OfInteger,VMults : OCP.TColStd.TColStd_Array1OfInteger,UDegree : int,VDegree : int,UPeriodic : bool=False,VPeriodic : bool=False) -> None: ...
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
class Geom_Point(Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    The abstract class Point describes the common behavior of geometric points in 3D space. The Geom package also provides the concrete class Geom_CartesianPoint.The abstract class Point describes the common behavior of geometric points in 3D space. The Geom package also provides the concrete class Geom_CartesianPoint.The abstract class Point describes the common behavior of geometric points in 3D space. The Geom package also provides the concrete class Geom_CartesianPoint.
    """
    def Coord(self) -> Tuple[float, float, float]: 
        """
        returns the Coordinates of <me>.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Distance(self,Other : Geom_Point) -> float: 
        """
        Computes the distance between <me> and <Other>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Pnt(self) -> OCP.gp.gp_Pnt: 
        """
        returns a non transient copy of <me>
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SquareDistance(self,Other : Geom_Point) -> float: 
        """
        Computes the square distance between <me> and <Other>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def X(self) -> float: 
        """
        returns the X coordinate of <me>.
        """
    def Y(self) -> float: 
        """
        returns the Y coordinate of <me>.
        """
    def Z(self) -> float: 
        """
        returns the Z coordinate of <me>.
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
class Geom_Conic(Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    The abstract class Conic describes the common behavior of conic curves in 3D space and, in particular, their general characteristics. The Geom package provides four concrete classes of conics: Geom_Circle, Geom_Ellipse, Geom_Hyperbola and Geom_Parabola. A conic is positioned in space with a right-handed coordinate system (gp_Ax2 object), where: - the origin is the center of the conic (or the apex in the case of a parabola), - the origin, "X Direction" and "Y Direction" define the plane of the conic. This coordinate system is the local coordinate system of the conic. The "main Direction" of this coordinate system is the vector normal to the plane of the conic. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the conic. The "main Direction" of the local coordinate system gives an explicit orientation to the conic, determining the direction in which the parameter increases along the conic. The "X Axis" of the local coordinate system also defines the origin of the parameter of the conic.The abstract class Conic describes the common behavior of conic curves in 3D space and, in particular, their general characteristics. The Geom package provides four concrete classes of conics: Geom_Circle, Geom_Ellipse, Geom_Hyperbola and Geom_Parabola. A conic is positioned in space with a right-handed coordinate system (gp_Ax2 object), where: - the origin is the center of the conic (or the apex in the case of a parabola), - the origin, "X Direction" and "Y Direction" define the plane of the conic. This coordinate system is the local coordinate system of the conic. The "main Direction" of this coordinate system is the vector normal to the plane of the conic. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the conic. The "main Direction" of the local coordinate system gives an explicit orientation to the conic, determining the direction in which the parameter increases along the conic. The "X Axis" of the local coordinate system also defines the origin of the parameter of the conic.The abstract class Conic describes the common behavior of conic curves in 3D space and, in particular, their general characteristics. The Geom package provides four concrete classes of conics: Geom_Circle, Geom_Ellipse, Geom_Hyperbola and Geom_Parabola. A conic is positioned in space with a right-handed coordinate system (gp_Ax2 object), where: - the origin is the center of the conic (or the apex in the case of a parabola), - the origin, "X Direction" and "Y Direction" define the plane of the conic. This coordinate system is the local coordinate system of the conic. The "main Direction" of this coordinate system is the vector normal to the plane of the conic. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the conic. The "main Direction" of the local coordinate system gives an explicit orientation to the conic, determining the direction in which the parameter increases along the conic. The "X Axis" of the local coordinate system also defines the origin of the parameter of the conic.
    """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the "main Axis" of this conic. This axis is normal to the plane of the conic.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        The continuity of the conic is Cn.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U and the first derivative V1. Raised if the continuity of the curve is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the curve is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the curve is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the curve is not CN.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Eccentricity(self) -> float: 
        """
        Returns the eccentricity value of the conic e. e = 0 for a circle 0 < e < 1 for an ellipse (e = 0 if MajorRadius = MinorRadius) e > 1 for a hyperbola e = 1 for a parabola Exceptions Standard_DomainError in the case of a hyperbola if its major radius is null.
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter. Warnings : It can be RealFirst from package Standard if the curve is infinite
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns True. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns true if the curve is closed. Some curves such as circle are always closed, others such as line are never closed (by definition). Some Curves such as OffsetCurve can be closed or not. These curves are considered as closed if the distance between the first point and the last point of the curve is lower or equal to the Resolution from package gp wich is a fixed criterion independant of the application.
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
    def IsPeriodic(self) -> bool: 
        """
        Is the parametrization of the curve periodic ? It is possible only if the curve is closed and if the following relation is satisfied : for each parametric value U the distance between the point P(u) and the point P (u + T) is lower or equal to Resolution from package gp, T is the period and must be a constant. There are three possibilities : . the curve is never periodic by definition (SegmentLine) . the curve is always periodic by definition (Circle) . the curve can be defined as periodic (BSpline). In this case a function SetPeriodic allows you to give the shape of the curve. The general rule for this case is : if a curve can be periodic or not the default periodicity set is non periodic and you have to turn (explicitly) the curve into a periodic curve if you want the curve to be periodic.
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the last parameter. Warnings : It can be RealLast from package Standard if the curve is infinite
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the conic. For the circle, the ellipse and the hyperbola it is the center of the conic. For the parabola it is the Apex of the parabola.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def Position(self) -> OCP.gp.gp_Ax2: 
        """
        Returns the local coordinates system of the conic. The main direction of the Axis2Placement is normal to the plane of the conic. The X direction of the Axis2placement is in the plane of the conic and corresponds to the origin for the conic's parametric value u.
        """
    def Reverse(self) -> None: 
        """
        Reverses the direction of parameterization of <me>. The local coordinate system of the conic is modified.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the reversed curve for the point of parameter U on <me>.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the orientation of the conic's plane. The normal axis to the plane is A1. The XAxis and the YAxis are recomputed.
        """
    def SetLocation(self,theP : OCP.gp.gp_Pnt) -> None: 
        """
        changes the location point of the conic.
        """
    def SetPosition(self,theA2 : OCP.gp.gp_Ax2) -> None: 
        """
        changes the local coordinate system of the conic.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    def XAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the XAxis of the conic. This axis defines the origin of parametrization of the conic. This axis is perpendicular to the Axis of the conic. This axis and the Yaxis define the plane of the conic.
        """
    def YAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the YAxis of the conic. The YAxis is perpendicular to the Xaxis. This axis and the Xaxis define the plane of the conic.
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
class Geom_Circle(Geom_Conic, Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a circle in 3D space. A circle is defined by its radius and, as with any conic curve, is positioned in space with a right-handed coordinate system (gp_Ax2 object) where: - the origin is the center of the circle, and - the origin, "X Direction" and "Y Direction" define the plane of the circle. This coordinate system is the local coordinate system of the circle. The "main Direction" of this coordinate system is the vector normal to the plane of the circle. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the circle. The "main Direction" of the local coordinate system gives an explicit orientation to the circle (definition of the trigonometric sense), determining the direction in which the parameter increases along the circle. The Geom_Circle circle is parameterized by an angle: P(U) = O + R*Cos(U)*XDir + R*Sin(U)*YDir, where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - R is the radius of the circle. The "X Axis" of the local coordinate system therefore defines the origin of the parameter of the circle. The parameter is the angle with this "X Direction". A circle is a closed and periodic curve. The period is 2.*Pi and the parameter range is [ 0, 2.*Pi [.Describes a circle in 3D space. A circle is defined by its radius and, as with any conic curve, is positioned in space with a right-handed coordinate system (gp_Ax2 object) where: - the origin is the center of the circle, and - the origin, "X Direction" and "Y Direction" define the plane of the circle. This coordinate system is the local coordinate system of the circle. The "main Direction" of this coordinate system is the vector normal to the plane of the circle. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the circle. The "main Direction" of the local coordinate system gives an explicit orientation to the circle (definition of the trigonometric sense), determining the direction in which the parameter increases along the circle. The Geom_Circle circle is parameterized by an angle: P(U) = O + R*Cos(U)*XDir + R*Sin(U)*YDir, where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - R is the radius of the circle. The "X Axis" of the local coordinate system therefore defines the origin of the parameter of the circle. The parameter is the angle with this "X Direction". A circle is a closed and periodic curve. The period is 2.*Pi and the parameter range is [ 0, 2.*Pi [.Describes a circle in 3D space. A circle is defined by its radius and, as with any conic curve, is positioned in space with a right-handed coordinate system (gp_Ax2 object) where: - the origin is the center of the circle, and - the origin, "X Direction" and "Y Direction" define the plane of the circle. This coordinate system is the local coordinate system of the circle. The "main Direction" of this coordinate system is the vector normal to the plane of the circle. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the circle. The "main Direction" of the local coordinate system gives an explicit orientation to the circle (definition of the trigonometric sense), determining the direction in which the parameter increases along the circle. The Geom_Circle circle is parameterized by an angle: P(U) = O + R*Cos(U)*XDir + R*Sin(U)*YDir, where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - R is the radius of the circle. The "X Axis" of the local coordinate system therefore defines the origin of the parameter of the circle. The parameter is the angle with this "X Direction". A circle is a closed and periodic curve. The period is 2.*Pi and the parameter range is [ 0, 2.*Pi [.
    """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the "main Axis" of this conic. This axis is normal to the plane of the conic.
        """
    def Circ(self) -> OCP.gp.gp_Circ: 
        """
        returns the non transient circle from gp with the same geometric properties as <me>.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        The continuity of the conic is Cn.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this circle.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U. P = C + R * Cos (U) * XDir + R * Sin (U) * YDir where C is the center of the circle , XDir the XDirection and YDir the YDirection of the circle's local coordinate system.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U and the first derivative V1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter u, the first second and third derivatives V1 V2 and V3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if N < 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Eccentricity(self) -> float: 
        """
        Returns the eccentricity e = 0 for a circle.
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter of this circle. This is 0.0, which gives the start point of this circle, or The start point and end point of a circle are coincident.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns True. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        returns True.
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
    def IsPeriodic(self) -> bool: 
        """
        returns True.
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the last parameter of this circle. This is 2.*Pi, which gives the end point of this circle. The start point and end point of a circle are coincident.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the conic. For the circle, the ellipse and the hyperbola it is the center of the conic. For the parabola it is the Apex of the parabola.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def Position(self) -> OCP.gp.gp_Ax2: 
        """
        Returns the local coordinates system of the conic. The main direction of the Axis2Placement is normal to the plane of the conic. The X direction of the Axis2placement is in the plane of the conic and corresponds to the origin for the conic's parametric value u.
        """
    def Radius(self) -> float: 
        """
        Returns the radius of this circle.
        """
    def Reverse(self) -> None: 
        """
        Reverses the direction of parameterization of <me>. The local coordinate system of the conic is modified.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Computes the parameter on the reversed circle for the point of parameter U on this circle. For a circle, the returned value is: 2.*Pi - U.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the orientation of the conic's plane. The normal axis to the plane is A1. The XAxis and the YAxis are recomputed.
        """
    def SetCirc(self,C : OCP.gp.gp_Circ) -> None: 
        """
        Set <me> so that <me> has the same geometric properties as C.
        """
    def SetLocation(self,theP : OCP.gp.gp_Pnt) -> None: 
        """
        changes the location point of the conic.
        """
    def SetPosition(self,theA2 : OCP.gp.gp_Ax2) -> None: 
        """
        changes the local coordinate system of the conic.
        """
    def SetRadius(self,R : float) -> None: 
        """
        Assigns the value R to the radius of this circle. Note: it is possible to have a circle with a radius equal to 0.0. Exceptions - Standard_ConstructionError if R is negative.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this circle.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    def XAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the XAxis of the conic. This axis defines the origin of parametrization of the conic. This axis is perpendicular to the Axis of the conic. This axis and the Yaxis define the plane of the conic.
        """
    def YAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the YAxis of the conic. The YAxis is perpendicular to the Xaxis. This axis and the Xaxis define the plane of the conic.
        """
    @overload
    def __init__(self,C : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,Radius : float) -> None: ...
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
class Geom_ElementarySurface(Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes the common behavior of surfaces which have a simple parametric equation in a local coordinate system. The Geom package provides several implementations of concrete elementary surfaces: - the plane, and - four simple surfaces of revolution: the cylinder, the cone, the sphere and the torus. An elementary surface inherits the common behavior of Geom_Surface surfaces. Furthermore, it is located in 3D space by a coordinate system (a gp_Ax3 object) which is also its local coordinate system. Any elementary surface is oriented, i.e. the normal vector is always defined, and gives the same orientation to the surface, at any point on the surface. In topology this property is referred to as the "outside region of the surface". This orientation is related to the two parametric directions of the surface. Rotation of a surface around the "main Axis" of its coordinate system, in the trigonometric sense given by the "X Direction" and the "Y Direction" of the coordinate system, defines the u parametric direction of that elementary surface of revolution. This is the default construction mode. It is also possible, however, to change the orientation of a surface by reversing one of the two parametric directions: use the UReverse or VReverse functions to change the orientation of the normal at any point on the surface. Warning The local coordinate system of an elementary surface is not necessarily direct: - if it is direct, the trigonometric sense defined by its "main Direction" is the same as the trigonometric sense defined by its two vectors "X Direction" and "Y Direction": "main Direction" = "X Direction" ^ "Y Direction" - if it is indirect, the two definitions of trigonometric sense are opposite: "main Direction" = - "X Direction" ^ "Y Direction"Describes the common behavior of surfaces which have a simple parametric equation in a local coordinate system. The Geom package provides several implementations of concrete elementary surfaces: - the plane, and - four simple surfaces of revolution: the cylinder, the cone, the sphere and the torus. An elementary surface inherits the common behavior of Geom_Surface surfaces. Furthermore, it is located in 3D space by a coordinate system (a gp_Ax3 object) which is also its local coordinate system. Any elementary surface is oriented, i.e. the normal vector is always defined, and gives the same orientation to the surface, at any point on the surface. In topology this property is referred to as the "outside region of the surface". This orientation is related to the two parametric directions of the surface. Rotation of a surface around the "main Axis" of its coordinate system, in the trigonometric sense given by the "X Direction" and the "Y Direction" of the coordinate system, defines the u parametric direction of that elementary surface of revolution. This is the default construction mode. It is also possible, however, to change the orientation of a surface by reversing one of the two parametric directions: use the UReverse or VReverse functions to change the orientation of the normal at any point on the surface. Warning The local coordinate system of an elementary surface is not necessarily direct: - if it is direct, the trigonometric sense defined by its "main Direction" is the same as the trigonometric sense defined by its two vectors "X Direction" and "Y Direction": "main Direction" = "X Direction" ^ "Y Direction" - if it is indirect, the two definitions of trigonometric sense are opposite: "main Direction" = - "X Direction" ^ "Y Direction"Describes the common behavior of surfaces which have a simple parametric equation in a local coordinate system. The Geom package provides several implementations of concrete elementary surfaces: - the plane, and - four simple surfaces of revolution: the cylinder, the cone, the sphere and the torus. An elementary surface inherits the common behavior of Geom_Surface surfaces. Furthermore, it is located in 3D space by a coordinate system (a gp_Ax3 object) which is also its local coordinate system. Any elementary surface is oriented, i.e. the normal vector is always defined, and gives the same orientation to the surface, at any point on the surface. In topology this property is referred to as the "outside region of the surface". This orientation is related to the two parametric directions of the surface. Rotation of a surface around the "main Axis" of its coordinate system, in the trigonometric sense given by the "X Direction" and the "Y Direction" of the coordinate system, defines the u parametric direction of that elementary surface of revolution. This is the default construction mode. It is also possible, however, to change the orientation of a surface by reversing one of the two parametric directions: use the UReverse or VReverse functions to change the orientation of the normal at any point on the surface. Warning The local coordinate system of an elementary surface is not necessarily direct: - if it is direct, the trigonometric sense defined by its "main Direction" is the same as the trigonometric sense defined by its two vectors "X Direction" and "Y Direction": "main Direction" = "X Direction" ^ "Y Direction" - if it is indirect, the two definitions of trigonometric sense are opposite: "main Direction" = - "X Direction" ^ "Y Direction"
    """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the main axis of the surface (ZAxis).
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this surface. If the surface is infinite, this function can return a value equal to Precision::Infinite: instead of Standard_Real::LastReal.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_CN, the global continuity of any elementary surface.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U,V on the surface.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P and the first derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first and the second derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first,the second and the third derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        ---Purpose ; Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns True.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns True.
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
    def IsUClosed(self) -> bool: 
        """
        Checks whether this surface is closed in the u parametric direction. Returns true if, in the u parametric direction: taking uFirst and uLast as the parametric bounds in the u parametric direction, for each parameter v, the distance between the points P(uFirst, v) and P(uLast, v) is less than or equal to gp::Resolution().
        """
    def IsUPeriodic(self) -> bool: 
        """
        Checks if this surface is periodic in the u parametric direction. Returns true if: - this surface is closed in the u parametric direction, and - there is a constant T such that the distance between the points P (u, v) and P (u + T, v) (or the points P (u, v) and P (u, v + T)) is less than or equal to gp::Resolution(). Note: T is the parametric period in the u parametric direction.
        """
    def IsVClosed(self) -> bool: 
        """
        Checks whether this surface is closed in the u parametric direction. Returns true if, in the v parametric direction: taking vFirst and vLast as the parametric bounds in the v parametric direction, for each parameter u, the distance between the points P(u, vFirst) and P(u, vLast) is less than or equal to gp::Resolution().
        """
    def IsVPeriodic(self) -> bool: 
        """
        Checks if this surface is periodic in the v parametric direction. Returns true if: - this surface is closed in the v parametric direction, and - there is a constant T such that the distance between the points P (u, v) and P (u + T, v) (or the points P (u, v) and P (u, v + T)) is less than or equal to gp::Resolution(). Note: T is the parametric period in the v parametric direction.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the local coordinate system of the surface.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Position(self) -> OCP.gp.gp_Ax3: 
        """
        Returns the local coordinates system of the surface.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the main axis (ZAxis) of the elementary surface.
        """
    def SetLocation(self,theLoc : OCP.gp.gp_Pnt) -> None: 
        """
        Changes the location of the local coordinates system of the surface.
        """
    def SetPosition(self,theAx3 : OCP.gp.gp_Ax3) -> None: 
        """
        Changes the local coordinates system of the surface.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Reverses the U parametric direction of the surface.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Return the parameter on the Ureversed surface for the point of parameter U on <me>.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V parametric direction of the surface.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Return the parameter on the Vreversed surface for the point of parameter V on <me>.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
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
class Geom_BezierCurve(Geom_BoundedCurve, Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a rational or non-rational Bezier curve - a non-rational Bezier curve is defined by a table of poles (also called control points), - a rational Bezier curve is defined by a table of poles with varying weights. These data are manipulated by two parallel arrays: - the poles table, which is an array of gp_Pnt points, and - the weights table, which is an array of reals. The bounds of these arrays are 1 and "the number of "poles" of the curve. The poles of the curve are "control points" used to deform the curve. The first pole is the start point of the curve, and the last pole is the end point of the curve. The segment that joins the first pole to the second pole is the tangent to the curve at its start point, and the segment that joins the last pole to the second-from-last pole is the tangent to the curve at its end point. It is more difficult to give a geometric signification to the weights but they are useful for providing the exact representations of arcs of a circle or ellipse. Moreover, if the weights of all poles are equal, the curve is polynomial; it is therefore a non-rational curve. The non-rational curve is a special and frequently used case. The weights are defined and used only in the case of a rational curve. The degree of a Bezier curve is equal to the number of poles, minus 1. It must be greater than or equal to 1. However, the degree of a Geom_BezierCurve curve is limited to a value (25) which is defined and controlled by the system. This value is returned by the function MaxDegree. The parameter range for a Bezier curve is [ 0, 1 ]. If the first and last control points of the Bezier curve are the same point then the curve is closed. For example, to create a closed Bezier curve with four control points, you have to give the set of control points P1, P2, P3 and P1. The continuity of a Bezier curve is infinite. It is not possible to build a Bezier curve with negative weights. We consider that a weight value is zero if it is less than or equal to gp::Resolution(). We also consider that two weight values W1 and W2 are equal if: |W2 - W1| <= gp::Resolution(). Warning - When considering the continuity of a closed Bezier curve at the junction point, remember that a curve of this type is never periodic. This means that the derivatives for the parameter u = 0 have no reason to be the same as the derivatives for the parameter u = 1 even if the curve is closed. - The length of a Bezier curve can be null.Describes a rational or non-rational Bezier curve - a non-rational Bezier curve is defined by a table of poles (also called control points), - a rational Bezier curve is defined by a table of poles with varying weights. These data are manipulated by two parallel arrays: - the poles table, which is an array of gp_Pnt points, and - the weights table, which is an array of reals. The bounds of these arrays are 1 and "the number of "poles" of the curve. The poles of the curve are "control points" used to deform the curve. The first pole is the start point of the curve, and the last pole is the end point of the curve. The segment that joins the first pole to the second pole is the tangent to the curve at its start point, and the segment that joins the last pole to the second-from-last pole is the tangent to the curve at its end point. It is more difficult to give a geometric signification to the weights but they are useful for providing the exact representations of arcs of a circle or ellipse. Moreover, if the weights of all poles are equal, the curve is polynomial; it is therefore a non-rational curve. The non-rational curve is a special and frequently used case. The weights are defined and used only in the case of a rational curve. The degree of a Bezier curve is equal to the number of poles, minus 1. It must be greater than or equal to 1. However, the degree of a Geom_BezierCurve curve is limited to a value (25) which is defined and controlled by the system. This value is returned by the function MaxDegree. The parameter range for a Bezier curve is [ 0, 1 ]. If the first and last control points of the Bezier curve are the same point then the curve is closed. For example, to create a closed Bezier curve with four control points, you have to give the set of control points P1, P2, P3 and P1. The continuity of a Bezier curve is infinite. It is not possible to build a Bezier curve with negative weights. We consider that a weight value is zero if it is less than or equal to gp::Resolution(). We also consider that two weight values W1 and W2 are equal if: |W2 - W1| <= gp::Resolution(). Warning - When considering the continuity of a closed Bezier curve at the junction point, remember that a curve of this type is never periodic. This means that the derivatives for the parameter u = 0 have no reason to be the same as the derivatives for the parameter u = 1 even if the curve is closed. - The length of a Bezier curve can be null.Describes a rational or non-rational Bezier curve - a non-rational Bezier curve is defined by a table of poles (also called control points), - a rational Bezier curve is defined by a table of poles with varying weights. These data are manipulated by two parallel arrays: - the poles table, which is an array of gp_Pnt points, and - the weights table, which is an array of reals. The bounds of these arrays are 1 and "the number of "poles" of the curve. The poles of the curve are "control points" used to deform the curve. The first pole is the start point of the curve, and the last pole is the end point of the curve. The segment that joins the first pole to the second pole is the tangent to the curve at its start point, and the segment that joins the last pole to the second-from-last pole is the tangent to the curve at its end point. It is more difficult to give a geometric signification to the weights but they are useful for providing the exact representations of arcs of a circle or ellipse. Moreover, if the weights of all poles are equal, the curve is polynomial; it is therefore a non-rational curve. The non-rational curve is a special and frequently used case. The weights are defined and used only in the case of a rational curve. The degree of a Bezier curve is equal to the number of poles, minus 1. It must be greater than or equal to 1. However, the degree of a Geom_BezierCurve curve is limited to a value (25) which is defined and controlled by the system. This value is returned by the function MaxDegree. The parameter range for a Bezier curve is [ 0, 1 ]. If the first and last control points of the Bezier curve are the same point then the curve is closed. For example, to create a closed Bezier curve with four control points, you have to give the set of control points P1, P2, P3 and P1. The continuity of a Bezier curve is infinite. It is not possible to build a Bezier curve with negative weights. We consider that a weight value is zero if it is less than or equal to gp::Resolution(). We also consider that two weight values W1 and W2 are equal if: |W2 - W1| <= gp::Resolution(). Warning - When considering the continuity of a closed Bezier curve at the junction point, remember that a curve of this type is never periodic. This means that the derivatives for the parameter u = 0 have no reason to be the same as the derivatives for the parameter u = 1 even if the curve is closed. - The length of a Bezier curve can be null.
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        a Bezier curve is CN
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this Bezier curve.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        For this Bezier curve, computes - the point P of parameter U, or - the point P and one or more of the following values: - V1, the first derivative vector, - V2, the second derivative vector, - V3, the third derivative vector. Note: the parameter U can be outside the bounds of the curve.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        For the point of parameter U of this Bezier curve, computes the vector corresponding to the Nth derivative. Note: the parameter U can be outside the bounds of the curve. Exceptions Standard_RangeError if N is less than 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
        """
        Returns the polynomial degree of the curve. it is the number of poles - 1 point P and derivatives (V1, V2, V3) computation The Bezier Curve has a Polynomial representation so the parameter U can be out of the bounds of the curve.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns Value (U=1.), it is the last control point of the Bezier curve.
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter of this Bezier curve. This is 0.0, which gives the start point of this Bezier curve
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Increase(self,Degree : int) -> None: 
        """
        Increases the degree of a bezier curve. Degree is the new degree of <me>. Raises ConstructionError if Degree is greater than MaxDegree or lower than 2 or lower than the initial degree of <me>.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def InsertPoleAfter(self,Index : int,P : OCP.gp.gp_Pnt) -> None: 
        """
        Inserts a pole P after the pole of range Index. If the curve <me> is rational the weight value for the new pole of range Index is 1.0. raised if Index is not in the range [1, NbPoles]

        Inserts a pole with its weight in the set of poles after the pole of range Index. If the curve was non rational it can become rational if all the weights are not identical. Raised if Index is not in the range [1, NbPoles]
        """
    @overload
    def InsertPoleAfter(self,Index : int,P : OCP.gp.gp_Pnt,Weight : float) -> None: ...
    @overload
    def InsertPoleBefore(self,Index : int,P : OCP.gp.gp_Pnt,Weight : float) -> None: 
        """
        Inserts a pole P before the pole of range Index. If the curve <me> is rational the weight value for the new pole of range Index is 1.0. Raised if Index is not in the range [1, NbPoles]

        Inserts a pole with its weight in the set of poles after the pole of range Index. If the curve was non rational it can become rational if all the weights are not identical. Raised if Index is not in the range [1, NbPoles]
        """
    @overload
    def InsertPoleBefore(self,Index : int,P : OCP.gp.gp_Pnt) -> None: ...
    def IsCN(self,N : int) -> bool: 
        """
        Continuity of the curve, returns True.
        """
    def IsClosed(self) -> bool: 
        """
        Returns True if the distance between the first point and the last point of the curve is lower or equal to the Resolution from package gp.
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
    def IsPeriodic(self) -> bool: 
        """
        Returns True if the parametrization of a curve is periodic. (P(u) = P(u + T) T = constante)
        """
    def IsRational(self) -> bool: 
        """
        Returns false if all the weights are identical. The tolerance criterion is Resolution from package gp.
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the last parameter of this Bezier curve. This is 1.0, which gives the end point of this Bezier curve.
        """
    @staticmethod
    def MaxDegree_s() -> int: 
        """
        Returns the value of the maximum polynomial degree of any Geom_BezierCurve curve. This value is 25.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def NbPoles(self) -> int: 
        """
        Returns the number of poles of this Bezier curve.
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def Pole(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the pole of range Index. Raised if Index is not in the range [1, NbPoles]
        """
    @overload
    def Poles(self,P : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        Returns all the poles of the curve.

        Returns all the poles of the curve.
        """
    @overload
    def Poles(self) -> OCP.TColgp.TColgp_Array1OfPnt: ...
    def RemovePole(self,Index : int) -> None: 
        """
        Removes the pole of range Index. If the curve was rational it can become non rational. Raised if Index is not in the range [1, NbPoles] Raised if Degree is lower than 2.
        """
    def Resolution(self,Tolerance3D : float) -> Tuple[float]: 
        """
        Computes for this Bezier curve the parametric tolerance UTolerance for a given 3D tolerance Tolerance3D. If f(t) is the equation of this Bezier curve, UTolerance ensures that: |t1-t0| < UTolerance ===> |f(t1)-f(t0)| < Tolerance3D
        """
    def Reverse(self) -> None: 
        """
        Reverses the direction of parametrization of <me> Value (NewU) = Value (1 - OldU)
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the reversed curve for the point of parameter U on <me>.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def Segment(self,U1 : float,U2 : float) -> None: 
        """
        Segments the curve between U1 and U2 which can be out of the bounds of the curve. The curve is oriented from U1 to U2. The control points are modified, the first and the last point are not the same but the parametrization range is [0, 1] else it could not be a Bezier curve. Warnings : Even if <me> is not closed it can become closed after the segmentation for example if U1 or U2 are out of the bounds of the curve <me> or if the curve makes loop. After the segmentation the length of a curve can be null.
        """
    @overload
    def SetPole(self,Index : int,P : OCP.gp.gp_Pnt) -> None: 
        """
        Substitutes the pole of range index with P. If the curve <me> is rational the weight of range Index is not modified. raiseD if Index is not in the range [1, NbPoles]

        Substitutes the pole and the weights of range Index. If the curve <me> is not rational it can become rational if all the weights are not identical. If the curve was rational it can become non rational if all the weights are identical. Raised if Index is not in the range [1, NbPoles] Raised if Weight <= Resolution from package gp
        """
    @overload
    def SetPole(self,Index : int,P : OCP.gp.gp_Pnt,Weight : float) -> None: ...
    def SetWeight(self,Index : int,Weight : float) -> None: 
        """
        Changes the weight of the pole of range Index. If the curve <me> is not rational it can become rational if all the weights are not identical. If the curve was rational it can become non rational if all the weights are identical. Raised if Index is not in the range [1, NbPoles] Raised if Weight <= Resolution from package gp
        """
    def StartPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns Value (U=0.), it is the first control point of the curve.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this Bezier curve.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    def Weight(self,Index : int) -> float: 
        """
        Returns the weight of range Index. Raised if Index is not in the range [1, NbPoles]
        """
    @overload
    def Weights(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Returns all the weights of the curve.

        Returns all the weights of the curve.
        """
    @overload
    def Weights(self,W : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,CurvePoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self,CurvePoles : OCP.TColgp.TColgp_Array1OfPnt,PoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
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
class Geom_CylindricalSurface(Geom_ElementarySurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    This class defines the infinite cylindrical surface.This class defines the infinite cylindrical surface.This class defines the infinite cylindrical surface.
    """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the main axis of the surface (ZAxis).
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        The CylindricalSurface is infinite in the V direction so V1 = Realfirst, V2 = RealLast from package Standard. U1 = 0 and U2 = 2*PI.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float, float, float, float, float]: 
        """
        Returns the coefficients of the implicit equation of the quadric in the absolute cartesian coordinate system : These coefficients are normalized. A1.X**2 + A2.Y**2 + A3.Z**2 + 2.(B1.X.Y + B2.X.Z + B3.Y.Z) + 2.(C1.X + C2.Y + C3.Z) + D = 0.0
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_CN, the global continuity of any elementary surface.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this cylinder.
        """
    def Cylinder(self) -> OCP.gp.gp_Cylinder: 
        """
        returns a non transient cylinder with the same geometric properties as <me>.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point P (U, V) on the surface. P (U, V) = Loc + Radius * (cos (U) * XDir + sin (U) * YDir) + V * ZDir where Loc is the origin of the placement plane (XAxis, YAxis) XDir is the direction of the XAxis and YDir the direction of the YAxis.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point and the first derivatives in the directions U and V.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first and the second derivatives in the directions U and V.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first, the second and the third derivatives in the directions U and V.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction u and Nv in the direction v. Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns True.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns True.
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
    def IsUClosed(self) -> bool: 
        """
        Returns True.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns True.
        """
    def IsVClosed(self) -> bool: 
        """
        Returns False.
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns False.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the local coordinate system of the surface.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface. me->Transformed(T)->Value(U',V') is the same point as me->Value(U,V).Transformed(T) Where U',V' are obtained by transforming U,V with th 2d transformation returned by me->ParametricTransformation(T) This methods returns a scale centered on the U axis with T.ScaleFactor
        """
    def Position(self) -> OCP.gp.gp_Ax3: 
        """
        Returns the local coordinates system of the surface.
        """
    def Radius(self) -> float: 
        """
        Returns the radius of this cylinder.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the main axis (ZAxis) of the elementary surface.
        """
    def SetCylinder(self,C : OCP.gp.gp_Cylinder) -> None: 
        """
        Set <me> so that <me> has the same geometric properties as C.
        """
    def SetLocation(self,theLoc : OCP.gp.gp_Pnt) -> None: 
        """
        Changes the location of the local coordinates system of the surface.
        """
    def SetPosition(self,theAx3 : OCP.gp.gp_Ax3) -> None: 
        """
        Changes the local coordinates system of the surface.
        """
    def SetRadius(self,R : float) -> None: 
        """
        Changes the radius of the cylinder. Raised if R < 0.0
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this cylinder.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>. me->Transformed(T)->Value(U',V') is the same point as me->Value(U,V).Transformed(T) Where U',V' are the new values of U,V after calling me->TranformParameters(U,V,T) This methods multiplies V by T.ScaleFactor()
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        The UIso curve is a Line. The location point of this line is on the placement plane (XAxis, YAxis) of the surface. This line is parallel to the axis of symmetry of the surface.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Reverses the U parametric direction of the surface.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Return the parameter on the Ureversed surface for the point of parameter U on <me>. Return 2.PI - U.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        The VIso curve is a circle. The start point of this circle (U = 0) is defined with the "XAxis" of the surface. The center of the circle is on the symmetry axis.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V parametric direction of the surface.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Return the parameter on the Vreversed surface for the point of parameter V on <me>. Return -V
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def __init__(self,A3 : OCP.gp.gp_Ax3,Radius : float) -> None: ...
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
class Geom_Vector(Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    The abstract class Vector describes the common behavior of vectors in 3D space. The Geom package provides two concrete classes of vectors: Geom_Direction (unit vector) and Geom_VectorWithMagnitude.The abstract class Vector describes the common behavior of vectors in 3D space. The Geom package provides two concrete classes of vectors: Geom_Direction (unit vector) and Geom_VectorWithMagnitude.The abstract class Vector describes the common behavior of vectors in 3D space. The Geom package provides two concrete classes of vectors: Geom_Direction (unit vector) and Geom_VectorWithMagnitude.
    """
    def Angle(self,Other : Geom_Vector) -> float: 
        """
        Computes the angular value, in radians, between this vector and vector Other. The result is a value between 0 and Pi. Exceptions gp_VectorWithNullMagnitude if: - the magnitude of this vector is less than or equal to gp::Resolution(), or - the magnitude of vector Other is less than or equal to gp::Resolution().
        """
    def AngleWithRef(self,Other : Geom_Vector,VRef : Geom_Vector) -> float: 
        """
        Computes the angular value, in radians, between this vector and vector Other. The result is a value between -Pi and Pi. The vector VRef defines the positive sense of rotation: the angular value is positive if the cross product this ^ Other has the same orientation as VRef (in relation to the plane defined by this vector and vector Other). Otherwise, it is negative. Exceptions Standard_DomainError if this vector, vector Other and vector VRef are coplanar, except if this vector and vector Other are parallel. gp_VectorWithNullMagnitude if the magnitude of this vector, vector Other or vector VRef is less than or equal to gp::Resolution().
        """
    def Coord(self) -> Tuple[float, float, float]: 
        """
        Returns the coordinates X, Y and Z of this vector.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def Cross(self,Other : Geom_Vector) -> None: 
        """
        Computes the cross product between <me> and <Other>.
        """
    def CrossCross(self,V1 : Geom_Vector,V2 : Geom_Vector) -> None: 
        """
        Computes the triple vector product <me> ^(V1 ^ V2).
        """
    def CrossCrossed(self,V1 : Geom_Vector,V2 : Geom_Vector) -> Geom_Vector: 
        """
        Computes the triple vector product <me> ^(V1 ^ V2).
        """
    def Crossed(self,Other : Geom_Vector) -> Geom_Vector: 
        """
        Computes the cross product between <me> and <Other>. A new direction is returned.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dot(self,Other : Geom_Vector) -> float: 
        """
        Computes the scalar product of this vector and vector Other.
        """
    def DotCross(self,V1 : Geom_Vector,V2 : Geom_Vector) -> float: 
        """
        Computes the triple scalar product. Returns me . (V1 ^ V2)
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def Magnitude(self) -> float: 
        """
        Returns the Magnitude of <me>.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Reverse(self) -> None: 
        """
        Reverses the vector <me>.
        """
    def Reversed(self) -> Geom_Vector: 
        """
        Returns a copy of <me> reversed.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SquareMagnitude(self) -> float: 
        """
        Returns the square magnitude of <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Vec(self) -> OCP.gp.gp_Vec: 
        """
        Converts this vector into a gp_Vec vector.
        """
    def X(self) -> float: 
        """
        Returns the X coordinate of <me>.
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate of <me>.
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate of <me>.
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
class Geom_ConicalSurface(Geom_ElementarySurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a cone. A cone is defined by the half-angle (can be negative) at its apex, and is positioned in space by a coordinate system (a gp_Ax3 object) and a reference radius as follows: - The "main Axis" of the coordinate system is the axis of revolution of the cone. - The plane defined by the origin, the "X Direction" and the "Y Direction" of the coordinate system is the reference plane of the cone. The intersection of the cone with this reference plane is a circle of radius equal to the reference radius. - The apex of the cone is on the negative side of the "main Axis" of the coordinate system if the half-angle is positive, and on the positive side if the half-angle is negative. This coordinate system is the "local coordinate system" of the cone. The following apply: - Rotation around its "main Axis", in the trigonometric sense given by the "X Direction" and the "Y Direction", defines the u parametric direction. - Its "X Axis" gives the origin for the u parameter. - Its "main Direction" is the v parametric direction of the cone. - Its origin is the origin of the v parameter. The parametric range of the two parameters is: - [ 0, 2.*Pi ] for u, and - ] -infinity, +infinity [ for v The parametric equation of the cone is: P(u, v) = O + (R + v*sin(Ang)) * (cos(u)*XDir + sin(u)*YDir) + v*cos(Ang)*ZDir where: - O, XDir, YDir and ZDir are respectively the origin, the "X Direction", the "Y Direction" and the "Z Direction" of the cone's local coordinate system, - Ang is the half-angle at the apex of the cone, and - R is the reference radius.Describes a cone. A cone is defined by the half-angle (can be negative) at its apex, and is positioned in space by a coordinate system (a gp_Ax3 object) and a reference radius as follows: - The "main Axis" of the coordinate system is the axis of revolution of the cone. - The plane defined by the origin, the "X Direction" and the "Y Direction" of the coordinate system is the reference plane of the cone. The intersection of the cone with this reference plane is a circle of radius equal to the reference radius. - The apex of the cone is on the negative side of the "main Axis" of the coordinate system if the half-angle is positive, and on the positive side if the half-angle is negative. This coordinate system is the "local coordinate system" of the cone. The following apply: - Rotation around its "main Axis", in the trigonometric sense given by the "X Direction" and the "Y Direction", defines the u parametric direction. - Its "X Axis" gives the origin for the u parameter. - Its "main Direction" is the v parametric direction of the cone. - Its origin is the origin of the v parameter. The parametric range of the two parameters is: - [ 0, 2.*Pi ] for u, and - ] -infinity, +infinity [ for v The parametric equation of the cone is: P(u, v) = O + (R + v*sin(Ang)) * (cos(u)*XDir + sin(u)*YDir) + v*cos(Ang)*ZDir where: - O, XDir, YDir and ZDir are respectively the origin, the "X Direction", the "Y Direction" and the "Z Direction" of the cone's local coordinate system, - Ang is the half-angle at the apex of the cone, and - R is the reference radius.Describes a cone. A cone is defined by the half-angle (can be negative) at its apex, and is positioned in space by a coordinate system (a gp_Ax3 object) and a reference radius as follows: - The "main Axis" of the coordinate system is the axis of revolution of the cone. - The plane defined by the origin, the "X Direction" and the "Y Direction" of the coordinate system is the reference plane of the cone. The intersection of the cone with this reference plane is a circle of radius equal to the reference radius. - The apex of the cone is on the negative side of the "main Axis" of the coordinate system if the half-angle is positive, and on the positive side if the half-angle is negative. This coordinate system is the "local coordinate system" of the cone. The following apply: - Rotation around its "main Axis", in the trigonometric sense given by the "X Direction" and the "Y Direction", defines the u parametric direction. - Its "X Axis" gives the origin for the u parameter. - Its "main Direction" is the v parametric direction of the cone. - Its origin is the origin of the v parameter. The parametric range of the two parameters is: - [ 0, 2.*Pi ] for u, and - ] -infinity, +infinity [ for v The parametric equation of the cone is: P(u, v) = O + (R + v*sin(Ang)) * (cos(u)*XDir + sin(u)*YDir) + v*cos(Ang)*ZDir where: - O, XDir, YDir and ZDir are respectively the origin, the "X Direction", the "Y Direction" and the "Z Direction" of the cone's local coordinate system, - Ang is the half-angle at the apex of the cone, and - R is the reference radius.
    """
    def Apex(self) -> OCP.gp.gp_Pnt: 
        """
        Computes the apex of this cone. It is on the negative side of the axis of revolution of this cone if the half-angle at the apex is positive, and on the positive side of the "main Axis" if the half-angle is negative.
        """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the main axis of the surface (ZAxis).
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        The conical surface is infinite in the V direction so V1 = Realfirst from Standard and V2 = RealLast. U1 = 0 and U2 = 2*PI.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float, float, float, float, float]: 
        """
        Returns the coefficients of the implicit equation of the quadric in the absolute cartesian coordinate system : These coefficients are normalized. A1.X**2 + A2.Y**2 + A3.Z**2 + 2.(B1.X.Y + B2.X.Z + B3.Y.Z) + 2.(C1.X + C2.Y + C3.Z) + D = 0.0
        """
    def Cone(self) -> OCP.gp.gp_Cone: 
        """
        returns a non transient cone with the same geometric properties as <me>.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_CN, the global continuity of any elementary surface.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this cone.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point P (U, V) on the surface. P (U, V) = Loc + (RefRadius + V * sin (Semi-Angle)) * (cos (U) * XDir + sin (U) * YDir) + V * cos (Semi-Angle) * ZDir where Loc is the origin of the placement plane (XAxis, YAxis) XDir is the direction of the XAxis and YDir the direction of the YAxis.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point and the first derivatives in the directions U and V.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first and the second derivatives in the directions U and V.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first,the second and the third derivatives in the directions U and V.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the u parametric direction, and Nv in the v parametric direction at the point of parameters (U, V) of this cone. Exceptions Standard_RangeError if: - Nu + Nv is less than 1, - Nu or Nv is negative.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns True.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns True.
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
    def IsUClosed(self) -> bool: 
        """
        returns True.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns True.
        """
    def IsVClosed(self) -> bool: 
        """
        returns False.
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns False.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the local coordinate system of the surface.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Position(self) -> OCP.gp.gp_Ax3: 
        """
        Returns the local coordinates system of the surface.
        """
    def RefRadius(self) -> float: 
        """
        Returns the reference radius of this cone. The reference radius is the radius of the circle formed by the intersection of this cone and its reference plane (i.e. the plane defined by the origin, "X Direction" and "Y Direction" of the local coordinate system of this cone). If the apex of this cone is on the origin of the local coordinate system of this cone, the returned value is 0.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SemiAngle(self) -> float: 
        """
        Returns the semi-angle at the apex of this cone. Attention! Semi-angle can be negative.
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the main axis (ZAxis) of the elementary surface.
        """
    def SetCone(self,C : OCP.gp.gp_Cone) -> None: 
        """
        Set <me> so that <me> has the same geometric properties as C.
        """
    def SetLocation(self,theLoc : OCP.gp.gp_Pnt) -> None: 
        """
        Changes the location of the local coordinates system of the surface.
        """
    def SetPosition(self,theAx3 : OCP.gp.gp_Ax3) -> None: 
        """
        Changes the local coordinates system of the surface.
        """
    def SetRadius(self,R : float) -> None: 
        """
        Changes the radius of the conical surface in the placement plane (Z = 0, V = 0). The local coordinate system is not modified. Raised if R < 0.0
        """
    def SetSemiAngle(self,Ang : float) -> None: 
        """
        Changes the semi angle of the conical surface. Semi-angle can be negative. Its absolute value Abs(Ang) is in range ]0,PI/2[. Raises ConstructionError if Abs(Ang) < Resolution from gp or Abs(Ang) >= PI/2 - Resolution
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this cone.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Builds the U isoparametric line of this cone. The origin of this line is on the reference plane of this cone (i.e. the plane defined by the origin, "X Direction" and "Y Direction" of the local coordinate system of this cone).
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Reverses the U parametric direction of the surface.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        return 2.PI - U.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Builds the V isoparametric circle of this cone. It is the circle on this cone, located in the plane of Z coordinate V*cos(Semi-Angle) in the local coordinate system of this cone. The "Axis" of this circle is the axis of revolution of this cone. Its starting point is defined by the "X Direction" of this cone. Warning If the V isoparametric circle is close to the apex of this cone, the radius of the circle becomes very small. It is possible to have a circle with radius equal to 0.0.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Changes the orientation of this cone in the v parametric direction. The bounds of the surface are not changed but the v parametric direction is reversed. As a consequence, for a cone: - the "main Direction" of the local coordinate system is reversed, and - the half-angle at the apex is inverted.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Computes the u (or v) parameter on the modified surface, when reversing its u (or v) parametric direction, for any point of u parameter U (or of v parameter V) on this cone. In the case of a cone, these functions return respectively: - 2.*Pi - U, -V.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    @overload
    def __init__(self,C : OCP.gp.gp_Cone) -> None: ...
    @overload
    def __init__(self,A3 : OCP.gp.gp_Ax3,Ang : float,Radius : float) -> None: ...
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
class Geom_Ellipse(Geom_Conic, Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes an ellipse in 3D space. An ellipse is defined by its major and minor radii and, as with any conic curve, is positioned in space with a right-handed coordinate system (gp_Ax2 object) where: - the origin is the center of the ellipse, - the "X Direction" defines the major axis, and - the "Y Direction" defines the minor axis. The origin, "X Direction" and "Y Direction" of this coordinate system define the plane of the ellipse. The coordinate system is the local coordinate system of the ellipse. The "main Direction" of this coordinate system is the vector normal to the plane of the ellipse. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the ellipse. The "main Direction" of the local coordinate system gives an explicit orientation to the ellipse (definition of the trigonometric sense), determining the direction in which the parameter increases along the ellipse. The Geom_Ellipse ellipse is parameterized by an angle: P(U) = O + MajorRad*Cos(U)*XDir + MinorRad*Sin(U)*YDir where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - MajorRad and MinorRad are the major and minor radii of the ellipse. The "X Axis" of the local coordinate system therefore defines the origin of the parameter of the ellipse. An ellipse is a closed and periodic curve. The period is 2.*Pi and the parameter range is [ 0, 2.*Pi [.Describes an ellipse in 3D space. An ellipse is defined by its major and minor radii and, as with any conic curve, is positioned in space with a right-handed coordinate system (gp_Ax2 object) where: - the origin is the center of the ellipse, - the "X Direction" defines the major axis, and - the "Y Direction" defines the minor axis. The origin, "X Direction" and "Y Direction" of this coordinate system define the plane of the ellipse. The coordinate system is the local coordinate system of the ellipse. The "main Direction" of this coordinate system is the vector normal to the plane of the ellipse. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the ellipse. The "main Direction" of the local coordinate system gives an explicit orientation to the ellipse (definition of the trigonometric sense), determining the direction in which the parameter increases along the ellipse. The Geom_Ellipse ellipse is parameterized by an angle: P(U) = O + MajorRad*Cos(U)*XDir + MinorRad*Sin(U)*YDir where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - MajorRad and MinorRad are the major and minor radii of the ellipse. The "X Axis" of the local coordinate system therefore defines the origin of the parameter of the ellipse. An ellipse is a closed and periodic curve. The period is 2.*Pi and the parameter range is [ 0, 2.*Pi [.Describes an ellipse in 3D space. An ellipse is defined by its major and minor radii and, as with any conic curve, is positioned in space with a right-handed coordinate system (gp_Ax2 object) where: - the origin is the center of the ellipse, - the "X Direction" defines the major axis, and - the "Y Direction" defines the minor axis. The origin, "X Direction" and "Y Direction" of this coordinate system define the plane of the ellipse. The coordinate system is the local coordinate system of the ellipse. The "main Direction" of this coordinate system is the vector normal to the plane of the ellipse. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the ellipse. The "main Direction" of the local coordinate system gives an explicit orientation to the ellipse (definition of the trigonometric sense), determining the direction in which the parameter increases along the ellipse. The Geom_Ellipse ellipse is parameterized by an angle: P(U) = O + MajorRad*Cos(U)*XDir + MinorRad*Sin(U)*YDir where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - MajorRad and MinorRad are the major and minor radii of the ellipse. The "X Axis" of the local coordinate system therefore defines the origin of the parameter of the ellipse. An ellipse is a closed and periodic curve. The period is 2.*Pi and the parameter range is [ 0, 2.*Pi [.
    """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the "main Axis" of this conic. This axis is normal to the plane of the conic.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        The continuity of the conic is Cn.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this ellipse.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U. P = C + MajorRadius * Cos (U) * XDir + MinorRadius * Sin (U) * YDir where C is the center of the ellipse , XDir the direction of the "XAxis" and "YDir" the "YAxis" of the ellipse.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U. The vectors V1 and V2 are the first and second derivatives at this point.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first second and third derivatives V1 V2 and V3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        For the point of parameter U of this ellipse, computes the vector corresponding to the Nth derivative. Exceptions Standard_RangeError if N is less than 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Directrix1(self) -> OCP.gp.gp_Ax1: 
        """
        This directrix is the line normal to the XAxis of the ellipse in the local plane (Z = 0) at a distance d = MajorRadius / e from the center of the ellipse, where e is the eccentricity of the ellipse. This line is parallel to the "YAxis". The intersection point between directrix1 and the "XAxis" is the "Location" point of the directrix1. This point is on the positive side of the "XAxis". Raised if Eccentricity = 0.0. (The ellipse degenerates into a circle)
        """
    def Directrix2(self) -> OCP.gp.gp_Ax1: 
        """
        This line is obtained by the symmetrical transformation of "Directrix1" with respect to the "YAxis" of the ellipse.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Eccentricity(self) -> float: 
        """
        Returns the eccentricity of the ellipse between 0.0 and 1.0 If f is the distance between the center of the ellipse and the Focus1 then the eccentricity e = f / MajorRadius. Returns 0 if MajorRadius = 0
        """
    def Elips(self) -> OCP.gp.gp_Elips: 
        """
        returns the non transient ellipse from gp with the same
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter of this ellipse. This is respectively: - 0.0, which gives the start point of this ellipse, or The start point and end point of an ellipse are coincident.
        """
    def Focal(self) -> float: 
        """
        Computes the focal distance. It is the distance between the the two focus of the ellipse.
        """
    def Focus1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the first focus of the ellipse. This focus is on the positive side of the "XAxis" of the ellipse.
        """
    def Focus2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the second focus of the ellipse. This focus is on the negative side of the "XAxis" of the ellipse.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns True. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        return True.
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
    def IsPeriodic(self) -> bool: 
        """
        return True.
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the last parameter of this ellipse. This is respectively: - 2.*Pi, which gives the end point of this ellipse. The start point and end point of an ellipse are coincident.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the conic. For the circle, the ellipse and the hyperbola it is the center of the conic. For the parabola it is the Apex of the parabola.
        """
    def MajorRadius(self) -> float: 
        """
        Returns the major radius of this ellipse.
        """
    def MinorRadius(self) -> float: 
        """
        Returns the minor radius of this ellipse.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Parameter(self) -> float: 
        """
        Returns p = (1 - e * e) * MajorRadius where e is the eccentricity of the ellipse. Returns 0 if MajorRadius = 0
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def Position(self) -> OCP.gp.gp_Ax2: 
        """
        Returns the local coordinates system of the conic. The main direction of the Axis2Placement is normal to the plane of the conic. The X direction of the Axis2placement is in the plane of the conic and corresponds to the origin for the conic's parametric value u.
        """
    def Reverse(self) -> None: 
        """
        Reverses the direction of parameterization of <me>. The local coordinate system of the conic is modified.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Computes the parameter on the reversed ellipse for the point of parameter U on this ellipse. For an ellipse, the returned value is: 2.*Pi - U.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the orientation of the conic's plane. The normal axis to the plane is A1. The XAxis and the YAxis are recomputed.
        """
    def SetElips(self,E : OCP.gp.gp_Elips) -> None: 
        """
        Converts the gp_Elips ellipse E into this ellipse.
        """
    def SetLocation(self,theP : OCP.gp.gp_Pnt) -> None: 
        """
        changes the location point of the conic.
        """
    def SetMajorRadius(self,MajorRadius : float) -> None: 
        """
        Assigns a value to the major radius of this ellipse. ConstructionError raised if MajorRadius < MinorRadius.
        """
    def SetMinorRadius(self,MinorRadius : float) -> None: 
        """
        Assigns a value to the minor radius of this ellipse. ConstructionError raised if MajorRadius < MinorRadius or if MinorRadius < 0.
        """
    def SetPosition(self,theA2 : OCP.gp.gp_Ax2) -> None: 
        """
        changes the local coordinate system of the conic.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this ellipse.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    def XAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the XAxis of the conic. This axis defines the origin of parametrization of the conic. This axis is perpendicular to the Axis of the conic. This axis and the Yaxis define the plane of the conic.
        """
    def YAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the YAxis of the conic. The YAxis is perpendicular to the Xaxis. This axis and the Xaxis define the plane of the conic.
        """
    @overload
    def __init__(self,E : OCP.gp.gp_Elips) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float) -> None: ...
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
class Geom_Axis2Placement(Geom_AxisPlacement, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a right-handed coordinate system in 3D space. A coordinate system is defined by: - its origin, also termed the "Location point" of the coordinate system, - three orthogonal unit vectors, termed respectively the "X Direction", "Y Direction" and "Direction" (or "main Direction") of the coordinate system. As a Geom_Axis2Placement coordinate system is right-handed, its "Direction" is always equal to the cross product of its "X Direction" and "Y Direction". The "Direction" of a coordinate system is called the "main Direction" because when this unit vector is modified, the "X Direction" and "Y Direction" are recomputed, whereas when the "X Direction" or "Y Direction" is changed, the "main Direction" is retained. The "main Direction" is also the "Z Direction". Note: Geom_Axis2Placement coordinate systems provide the same kind of "geometric" services as gp_Ax2 coordinate systems but have more complex data structures. The geometric objects provided by the Geom package use gp_Ax2 objects to include coordinate systems in their data structures, or to define the geometric transformations, which are applied to them. Geom_Axis2Placement coordinate systems are used in a context where they can be shared by several objects contained inside a common data structure.Describes a right-handed coordinate system in 3D space. A coordinate system is defined by: - its origin, also termed the "Location point" of the coordinate system, - three orthogonal unit vectors, termed respectively the "X Direction", "Y Direction" and "Direction" (or "main Direction") of the coordinate system. As a Geom_Axis2Placement coordinate system is right-handed, its "Direction" is always equal to the cross product of its "X Direction" and "Y Direction". The "Direction" of a coordinate system is called the "main Direction" because when this unit vector is modified, the "X Direction" and "Y Direction" are recomputed, whereas when the "X Direction" or "Y Direction" is changed, the "main Direction" is retained. The "main Direction" is also the "Z Direction". Note: Geom_Axis2Placement coordinate systems provide the same kind of "geometric" services as gp_Ax2 coordinate systems but have more complex data structures. The geometric objects provided by the Geom package use gp_Ax2 objects to include coordinate systems in their data structures, or to define the geometric transformations, which are applied to them. Geom_Axis2Placement coordinate systems are used in a context where they can be shared by several objects contained inside a common data structure.Describes a right-handed coordinate system in 3D space. A coordinate system is defined by: - its origin, also termed the "Location point" of the coordinate system, - three orthogonal unit vectors, termed respectively the "X Direction", "Y Direction" and "Direction" (or "main Direction") of the coordinate system. As a Geom_Axis2Placement coordinate system is right-handed, its "Direction" is always equal to the cross product of its "X Direction" and "Y Direction". The "Direction" of a coordinate system is called the "main Direction" because when this unit vector is modified, the "X Direction" and "Y Direction" are recomputed, whereas when the "X Direction" or "Y Direction" is changed, the "main Direction" is retained. The "main Direction" is also the "Z Direction". Note: Geom_Axis2Placement coordinate systems provide the same kind of "geometric" services as gp_Ax2 coordinate systems but have more complex data structures. The geometric objects provided by the Geom package use gp_Ax2 objects to include coordinate systems in their data structures, or to define the geometric transformations, which are applied to them. Geom_Axis2Placement coordinate systems are used in a context where they can be shared by several objects contained inside a common data structure.
    """
    def Angle(self,Other : Geom_AxisPlacement) -> float: 
        """
        Computes the angular value, in radians, between the "main Direction" of this positioning system and that of positioning system Other. The result is a value between 0 and Pi.
        """
    def Ax2(self) -> OCP.gp.gp_Ax2: 
        """
        Returns a non transient copy of <me>.
        """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the main axis of the axis placement. For an "Axis2placement" it is the main axis (Location, Direction ). For an "Axis1Placement" this method returns a copy of <me>.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this coordinate system.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns the main "Direction" of an axis placement.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the Location point (origin) of the axis placement.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAx2(self,A2 : OCP.gp.gp_Ax2) -> None: 
        """
        Assigns the origin and the three unit vectors of A2 to this coordinate system.
        """
    def SetAxis(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Assigns A1 as the "main Axis" of this positioning system. This modifies - its origin, and - its "main Direction". If this positioning system is a Geom_Axis2Placement, then its "X Direction" and "Y Direction" are recomputed. Exceptions For a Geom_Axis2Placement: Standard_ConstructionError if A1 and the previous "X Direction" of the coordinate system are parallel.
        """
    def SetDirection(self,V : OCP.gp.gp_Dir) -> None: 
        """
        Changes the main direction of the axis placement. The "Xdirection" is modified : New XDirection = V ^ (Previous_Xdirection ^ V).
        """
    def SetLocation(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Assigns the point P as the origin of this positioning system.
        """
    def SetXDirection(self,Vx : OCP.gp.gp_Dir) -> None: 
        """
        Changes the "XDirection" of the axis placement, Vx is the new "XDirection". If Vx is not normal to the main direction then "XDirection" is computed as follow : XDirection = Direction ^ ( Vx ^ Direction). The main direction is not modified. Raised if Vx and "Direction" are parallel.
        """
    def SetYDirection(self,Vy : OCP.gp.gp_Dir) -> None: 
        """
        Changes the "YDirection" of the axis placement, Vy is the new "YDirection". If Vy is not normal to the main direction then "YDirection" is computed as follow : YDirection = Direction ^ ( Vy ^ Direction). The main direction is not modified. The "XDirection" is modified. Raised if Vy and the main direction are parallel.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transforms an axis placement with a Trsf. The "Location" point, the "XDirection" and the "YDirection" are transformed with T. The resulting main "Direction" of <me> is the cross product between the "XDirection" and the "YDirection" after transformation.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def XDirection(self) -> OCP.gp.gp_Dir: 
        """
        Returns the "XDirection". This is a unit vector.
        """
    def YDirection(self) -> OCP.gp.gp_Dir: 
        """
        Returns the "YDirection". This is a unit vector.
        """
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,N : OCP.gp.gp_Dir,Vx : OCP.gp.gp_Dir) -> None: ...
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
class Geom_SequenceOfBSplineSurface(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Geom_SequenceOfBSplineSurface) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Geom_BSplineSurface) -> None: ...
    def Assign(self,theOther : Geom_SequenceOfBSplineSurface) -> Geom_SequenceOfBSplineSurface: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Geom_BSplineSurface: 
        """
        First item access
        """
    def ChangeLast(self) -> Geom_BSplineSurface: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Geom_BSplineSurface: 
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
    def First(self) -> Geom_BSplineSurface: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Geom_BSplineSurface) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Geom_SequenceOfBSplineSurface) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Geom_SequenceOfBSplineSurface) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Geom_BSplineSurface) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Geom_BSplineSurface: 
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
    def Prepend(self,theItem : Geom_BSplineSurface) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Geom_SequenceOfBSplineSurface) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Geom_BSplineSurface) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Geom_SequenceOfBSplineSurface) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Geom_BSplineSurface: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Geom_SequenceOfBSplineSurface) -> None: ...
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
class Geom_Hyperbola(Geom_Conic, Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a branch of a hyperbola in 3D space. A hyperbola is defined by its major and minor radii and, as with any conic curve, is positioned in space with a right-handed coordinate system (gp_Ax2 object) where: - the origin is the center of the hyperbola, - the "X Direction" defines the major axis, and - the "Y Direction" defines the minor axis. The origin, "X Direction" and "Y Direction" of this coordinate system define the plane of the hyperbola. The coordinate system is the local coordinate system of the hyperbola. The branch of the hyperbola described is the one located on the positive side of the major axis. The "main Direction" of the local coordinate system is a vector normal to the plane of the hyperbola. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the hyperbola. The "main Direction" of the local coordinate system gives an explicit orientation to the hyperbola, determining the direction in which the parameter increases along the hyperbola. The Geom_Hyperbola hyperbola is parameterized as follows: P(U) = O + MajRad*Cosh(U)*XDir + MinRad*Sinh(U)*YDir, where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - MajRad and MinRad are the major and minor radii of the hyperbola. The "X Axis" of the local coordinate system therefore defines the origin of the parameter of the hyperbola. The parameter range is ] -infinite, +infinite [. The following diagram illustrates the respective positions, in the plane of the hyperbola, of the three branches of hyperbolas constructed using the functions OtherBranch, ConjugateBranch1 and ConjugateBranch2: Defines the main branch of an hyperbola. ^YAxis | FirstConjugateBranch | Other | Main --------------------- C ------------------------------>XAxis Branch | Branch | SecondConjugateBranch | Warning The value of the major radius (on the major axis) can be less than the value of the minor radius (on the minor axis).Describes a branch of a hyperbola in 3D space. A hyperbola is defined by its major and minor radii and, as with any conic curve, is positioned in space with a right-handed coordinate system (gp_Ax2 object) where: - the origin is the center of the hyperbola, - the "X Direction" defines the major axis, and - the "Y Direction" defines the minor axis. The origin, "X Direction" and "Y Direction" of this coordinate system define the plane of the hyperbola. The coordinate system is the local coordinate system of the hyperbola. The branch of the hyperbola described is the one located on the positive side of the major axis. The "main Direction" of the local coordinate system is a vector normal to the plane of the hyperbola. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the hyperbola. The "main Direction" of the local coordinate system gives an explicit orientation to the hyperbola, determining the direction in which the parameter increases along the hyperbola. The Geom_Hyperbola hyperbola is parameterized as follows: P(U) = O + MajRad*Cosh(U)*XDir + MinRad*Sinh(U)*YDir, where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - MajRad and MinRad are the major and minor radii of the hyperbola. The "X Axis" of the local coordinate system therefore defines the origin of the parameter of the hyperbola. The parameter range is ] -infinite, +infinite [. The following diagram illustrates the respective positions, in the plane of the hyperbola, of the three branches of hyperbolas constructed using the functions OtherBranch, ConjugateBranch1 and ConjugateBranch2: Defines the main branch of an hyperbola. ^YAxis | FirstConjugateBranch | Other | Main --------------------- C ------------------------------>XAxis Branch | Branch | SecondConjugateBranch | Warning The value of the major radius (on the major axis) can be less than the value of the minor radius (on the minor axis).Describes a branch of a hyperbola in 3D space. A hyperbola is defined by its major and minor radii and, as with any conic curve, is positioned in space with a right-handed coordinate system (gp_Ax2 object) where: - the origin is the center of the hyperbola, - the "X Direction" defines the major axis, and - the "Y Direction" defines the minor axis. The origin, "X Direction" and "Y Direction" of this coordinate system define the plane of the hyperbola. The coordinate system is the local coordinate system of the hyperbola. The branch of the hyperbola described is the one located on the positive side of the major axis. The "main Direction" of the local coordinate system is a vector normal to the plane of the hyperbola. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the hyperbola. The "main Direction" of the local coordinate system gives an explicit orientation to the hyperbola, determining the direction in which the parameter increases along the hyperbola. The Geom_Hyperbola hyperbola is parameterized as follows: P(U) = O + MajRad*Cosh(U)*XDir + MinRad*Sinh(U)*YDir, where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - MajRad and MinRad are the major and minor radii of the hyperbola. The "X Axis" of the local coordinate system therefore defines the origin of the parameter of the hyperbola. The parameter range is ] -infinite, +infinite [. The following diagram illustrates the respective positions, in the plane of the hyperbola, of the three branches of hyperbolas constructed using the functions OtherBranch, ConjugateBranch1 and ConjugateBranch2: Defines the main branch of an hyperbola. ^YAxis | FirstConjugateBranch | Other | Main --------------------- C ------------------------------>XAxis Branch | Branch | SecondConjugateBranch | Warning The value of the major radius (on the major axis) can be less than the value of the minor radius (on the minor axis).
    """
    def Asymptote1(self) -> OCP.gp.gp_Ax1: 
        """
        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = (B/A)*X. Raises ConstructionError if MajorRadius = 0.0
        """
    def Asymptote2(self) -> OCP.gp.gp_Ax1: 
        """
        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = -(B/A)*X. Raises ConstructionError if MajorRadius = 0.0
        """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the "main Axis" of this conic. This axis is normal to the plane of the conic.
        """
    def ConjugateBranch1(self) -> OCP.gp.gp_Hypr: 
        """
        This branch of hyperbola is on the positive side of the YAxis of <me>.
        """
    def ConjugateBranch2(self) -> OCP.gp.gp_Hypr: 
        """
        This branch of hyperbola is on the negative side of the YAxis of <me>. Note: The diagram given under the class purpose indicates where these two branches of hyperbola are positioned in relation to this branch of hyperbola.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        The continuity of the conic is Cn.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this hyperbola.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U. P = C + MajorRadius * Cosh (U) * XDir + MinorRadius * Sinh (U) * YDir where C is the center of the hyperbola , XDir the XDirection and YDir the YDirection of the hyperbola's local coordinate system.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U and the first derivative V1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first second and third derivatives V1 V2 and V3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if N < 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Directrix1(self) -> OCP.gp.gp_Ax1: 
        """
        This directrix is the line normal to the XAxis of the hyperbola in the local plane (Z = 0) at a distance d = MajorRadius / e from the center of the hyperbola, where e is the eccentricity of the hyperbola. This line is parallel to the YAxis. The intersection point between directrix1 and the XAxis is the location point of the directrix1. This point is on the positive side of the XAxis.
        """
    def Directrix2(self) -> OCP.gp.gp_Ax1: 
        """
        This line is obtained by the symmetrical transformation of "directrix1" with respect to the YAxis of the hyperbola.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Eccentricity(self) -> float: 
        """
        Returns the excentricity of the hyperbola (e > 1). If f is the distance between the location of the hyperbola and the Focus1 then the eccentricity e = f / MajorRadius. raised if MajorRadius = 0.0
        """
    def FirstParameter(self) -> float: 
        """
        Returns RealFirst from Standard.
        """
    def Focal(self) -> float: 
        """
        Computes the focal distance. It is the distance between the two focus of the hyperbola.
        """
    def Focus1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the first focus of the hyperbola. This focus is on the positive side of the XAxis of the hyperbola.
        """
    def Focus2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the second focus of the hyperbola. This focus is on the negative side of the XAxis of the hyperbola.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hypr(self) -> OCP.gp.gp_Hypr: 
        """
        returns the non transient parabola from gp with the same geometric properties as <me>.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns True. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns False.
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
    def IsPeriodic(self) -> bool: 
        """
        return False for an hyperbola.
        """
    def LastParameter(self) -> float: 
        """
        returns RealLast from Standard.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the conic. For the circle, the ellipse and the hyperbola it is the center of the conic. For the parabola it is the Apex of the parabola.
        """
    def MajorRadius(self) -> float: 
        """
        Returns the major or minor radius of this hyperbola. The major radius is also the distance between the center of the hyperbola and the apex of the main branch (located on the "X Axis" of the hyperbola).
        """
    def MinorRadius(self) -> float: 
        """
        Returns the major or minor radius of this hyperbola. The minor radius is also the distance between the center of the hyperbola and the apex of a conjugate branch (located on the "Y Axis" of the hyperbola).
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def OtherBranch(self) -> OCP.gp.gp_Hypr: 
        """
        Computes the "other" branch of this hyperbola. This is the symmetrical branch with respect to the center of this hyperbola. Note: The diagram given under the class purpose indicates where the "other" branch is positioned in relation to this branch of the hyperbola.
        """
    def Parameter(self) -> float: 
        """
        Returns p = (e * e - 1) * MajorRadius where e is the eccentricity of the hyperbola. raised if MajorRadius = 0.0
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def Position(self) -> OCP.gp.gp_Ax2: 
        """
        Returns the local coordinates system of the conic. The main direction of the Axis2Placement is normal to the plane of the conic. The X direction of the Axis2placement is in the plane of the conic and corresponds to the origin for the conic's parametric value u.
        """
    def Reverse(self) -> None: 
        """
        Reverses the direction of parameterization of <me>. The local coordinate system of the conic is modified.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Computes the parameter on the reversed hyperbola, for the point of parameter U on this hyperbola. For a hyperbola, the returned value is: -U.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the orientation of the conic's plane. The normal axis to the plane is A1. The XAxis and the YAxis are recomputed.
        """
    def SetHypr(self,H : OCP.gp.gp_Hypr) -> None: 
        """
        Converts the gp_Hypr hyperbola H into this hyperbola.
        """
    def SetLocation(self,theP : OCP.gp.gp_Pnt) -> None: 
        """
        changes the location point of the conic.
        """
    def SetMajorRadius(self,MajorRadius : float) -> None: 
        """
        Assigns a value to the major radius of this hyperbola. Exceptions Standard_ConstructionError if: - MajorRadius is less than 0.0, or - MinorRadius is less than 0.0.Raised if MajorRadius < 0.0
        """
    def SetMinorRadius(self,MinorRadius : float) -> None: 
        """
        Assigns a value to the minor radius of this hyperbola. Exceptions Standard_ConstructionError if: - MajorRadius is less than 0.0, or - MinorRadius is less than 0.0.Raised if MajorRadius < 0.0
        """
    def SetPosition(self,theA2 : OCP.gp.gp_Ax2) -> None: 
        """
        changes the local coordinate system of the conic.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this hyperbola.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    def XAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the XAxis of the conic. This axis defines the origin of parametrization of the conic. This axis is perpendicular to the Axis of the conic. This axis and the Yaxis define the plane of the conic.
        """
    def YAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the YAxis of the conic. The YAxis is perpendicular to the Xaxis. This axis and the Xaxis define the plane of the conic.
        """
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,MajorRadius : float,MinorRadius : float) -> None: ...
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
class Geom_Line(Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes an infinite line. A line is defined and positioned in space with an axis (gp_Ax1 object) which gives it an origin and a unit vector. The Geom_Line line is parameterized: P (U) = O + U*Dir, where: - P is the point of parameter U, - O is the origin and Dir the unit vector of its positioning axis. The parameter range is ] -infinite, +infinite [. The orientation of the line is given by the unit vector of its positioning axis.Describes an infinite line. A line is defined and positioned in space with an axis (gp_Ax1 object) which gives it an origin and a unit vector. The Geom_Line line is parameterized: P (U) = O + U*Dir, where: - P is the point of parameter U, - O is the origin and Dir the unit vector of its positioning axis. The parameter range is ] -infinite, +infinite [. The orientation of the line is given by the unit vector of its positioning axis.Describes an infinite line. A line is defined and positioned in space with an axis (gp_Ax1 object) which gives it an origin and a unit vector. The Geom_Line line is parameterized: P (U) = O + U*Dir, where: - P is the point of parameter U, - O is the origin and Dir the unit vector of its positioning axis. The parameter range is ] -infinite, +infinite [. The orientation of the line is given by the unit vector of its positioning axis.
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_CN, which is the global continuity of any line.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this line.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U. P (U) = O + U * Dir where O is the "Location" point of the line and Dir the direction of the line.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter u and the first derivative V1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. V2 is a vector with null magnitude for a line.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        V2 and V3 are vectors with null magnitude for a line.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if N < 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter of this line. This is Standard_Real::RealFirst().
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        returns True. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        returns False
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
    def IsPeriodic(self) -> bool: 
        """
        returns False
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the last parameter of this line. This is Standard_Real::RealLast().
        """
    def Lin(self) -> OCP.gp.gp_Lin: 
        """
        Returns non transient line from gp with the same geometric properties as <me>
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def Position(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the positioning axis of this line; this is also its local coordinate system.
        """
    def Reverse(self) -> None: 
        """
        Changes the orientation of this line. As a result, the unit vector of the positioning axis of this line is reversed.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Computes the parameter on the reversed line for the point of parameter U on this line. For a line, the returned value is -U.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetDirection(self,V : OCP.gp.gp_Dir) -> None: 
        """
        changes the direction of the line.
        """
    def SetLin(self,L : OCP.gp.gp_Lin) -> None: 
        """
        Set <me> so that <me> has the same geometric properties as L.
        """
    def SetLocation(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        changes the "Location" point (origin) of the line.
        """
    def SetPosition(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        changes the "Location" and a the "Direction" of <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this line.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    @overload
    def __init__(self,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def __init__(self,A1 : OCP.gp.gp_Ax1) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Dir) -> None: ...
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
class Geom_OffsetCurve(Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    This class implements the basis services for an offset curve in 3D space. The Offset curve in this package can be a self intersecting curve even if the basis curve does not self-intersect. The self intersecting portions are not deleted at the construction time. An offset curve is a curve at constant distance (Offset) from a basis curve in a reference direction V. The offset curve takes its parametrization from the basis curve. The Offset curve is in the direction of the normal N defined with the cross product T^V, where the vector T is given by the first derivative on the basis curve with non zero length. The distance offset may be positive or negative to indicate the preferred side of the curve : . distance offset >0 => the curve is in the direction of N . distance offset <0 => the curve is in the direction of - NThis class implements the basis services for an offset curve in 3D space. The Offset curve in this package can be a self intersecting curve even if the basis curve does not self-intersect. The self intersecting portions are not deleted at the construction time. An offset curve is a curve at constant distance (Offset) from a basis curve in a reference direction V. The offset curve takes its parametrization from the basis curve. The Offset curve is in the direction of the normal N defined with the cross product T^V, where the vector T is given by the first derivative on the basis curve with non zero length. The distance offset may be positive or negative to indicate the preferred side of the curve : . distance offset >0 => the curve is in the direction of N . distance offset <0 => the curve is in the direction of - NThis class implements the basis services for an offset curve in 3D space. The Offset curve in this package can be a self intersecting curve even if the basis curve does not self-intersect. The self intersecting portions are not deleted at the construction time. An offset curve is a curve at constant distance (Offset) from a basis curve in a reference direction V. The offset curve takes its parametrization from the basis curve. The Offset curve is in the direction of the normal N defined with the cross product T^V, where the vector T is given by the first derivative on the basis curve with non zero length. The distance offset may be positive or negative to indicate the preferred side of the curve : . distance offset >0 => the curve is in the direction of N . distance offset <0 => the curve is in the direction of - N
    """
    def BasisCurve(self) -> Geom_Curve: 
        """
        Returns the basis curve of this offset curve. Note: The basis curve can be an offset curve.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the global continuity of this offset curve as a value of the GeomAbs_Shape enumeration. The degree of continuity of this offset curve is equal to the degree of continuity of the basis curve minus 1. Continuity of the Offset curve : C0 : only geometric continuity, C1 : continuity of the first derivative all along the Curve, C2 : continuity of the second derivative all along the Curve, C3 : continuity of the third derivative all along the Curve, G1 : tangency continuity all along the Curve, G2 : curvature continuity all along the Curve, CN : the order of continuity is infinite. Warnings : Returns the continuity of the basis curve - 1. The offset curve must have a unique offset direction defined at any point.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this offset curve.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Warning! this should not be called if the basis curve is not at least C1. Nevertheless if used on portion where the curve is C1, it is OK
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Warning! this should not be called if the continuity of the basis curve is not C2. Nevertheless, it's OK to use it on portion where the curve is C2
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Warning! this should not be called if the continuity of the basis curve is not C3. Nevertheless, it's OK to use it on portion where the curve is C3
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        The returned vector gives the value of the derivative for the order of derivation N.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns the reference vector of this offset curve. Value and derivatives Warnings : The exception UndefinedValue or UndefinedDerivative is raised if it is not possible to compute a unique offset direction. If T is the first derivative with not null length and V the offset direction the relation ||T(U) ^ V|| != 0 must be satisfied to evaluate the offset curve. No check is done at the creation time and we suppose in this package that the offset curve is well defined.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter of this offset curve. The first parameter corresponds to the start point of the curve. Note: the first and last parameters of this offset curve are also the ones of its basis curve.
        """
    def GetBasisCurveContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns continuity of the basis curve.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns true if the degree of continuity of the basis curve of this offset curve is at least N + 1. This method answer True if the continuity of the basis curve is N + 1. We suppose in this class that a normal direction to the basis curve (used to compute the offset curve) is defined at any point on the basis curve. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns True if the distance between the start point and the end point of the curve is lower or equal to Resolution from package gp.
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
    def IsPeriodic(self) -> bool: 
        """
        Returns true if this offset curve is periodic, i.e. if the basis curve of this offset curve is periodic.
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the last parameter of this offset curve. The last parameter corresponds to the end point. Note: the first and last parameters of this offset curve are also the ones of its basis curve.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Offset(self) -> float: 
        """
        Returns the offset value of this offset curve.
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this offset curve, i.e. the period of the basis curve of this offset curve. Exceptions Standard_NoSuchObject if the basis curve is not periodic.
        """
    def Reverse(self) -> None: 
        """
        Changes the orientation of this offset curve. As a result: - the basis curve is reversed, - the start point of the initial curve becomes the end point of the reversed curve, - the end point of the initial curve becomes the start point of the reversed curve, and - the first and last parameters are recomputed.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Computes the parameter on the reversed curve for the point of parameter U on this offset curve.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetBasisCurve(self,C : Geom_Curve,isNotCheckC0 : bool=False) -> None: 
        """
        Changes this offset curve by assigning C as the basis curve from which it is built. If isNotCheckC0 = TRUE checking if basis curve has C0-continuity is not made. Exceptions Standard_ConstructionError if the curve C is not at least "C1" continuous.
        """
    def SetDirection(self,V : OCP.gp.gp_Dir) -> None: 
        """
        Changes this offset curve by assigning V as the reference vector used to compute the offset direction.
        """
    def SetOffsetValue(self,D : float) -> None: 
        """
        Changes this offset curve by assigning D as the offset value.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this offset curve. Note: the basis curve is also modified.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>. me->Transformed(T)->Value(me->TransformedParameter(U,T)) is the same point as me->Value(U).Transformed(T) This methods calls the basis curve method.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    def __init__(self,C : Geom_Curve,Offset : float,V : OCP.gp.gp_Dir,isNotCheckC0 : bool=False) -> None: ...
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
class Geom_OffsetSurface(Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes an offset surface in 3D space. An offset surface is defined by: - the basis surface to which it is parallel, and - the distance between the offset surface and its basis surface. A point on the offset surface is built by measuring the offset value along the normal vector at a point on the basis surface. This normal vector is given by the cross product D1u^D1v, where D1u and D1v are the vectors tangential to the basis surface in the u and v parametric directions at this point. The side of the basis surface on which the offset is measured depends on the sign of the offset value. A Geom_OffsetSurface surface can be self-intersecting, even if the basis surface does not self-intersect. The self-intersecting portions are not deleted at the time of construction. Warning There must be only one normal vector defined at any point on the basis surface. This must be verified by the user as no check is made at the time of construction to detect points with multiple possible normal directions (for example, the top of a conical surface).Describes an offset surface in 3D space. An offset surface is defined by: - the basis surface to which it is parallel, and - the distance between the offset surface and its basis surface. A point on the offset surface is built by measuring the offset value along the normal vector at a point on the basis surface. This normal vector is given by the cross product D1u^D1v, where D1u and D1v are the vectors tangential to the basis surface in the u and v parametric directions at this point. The side of the basis surface on which the offset is measured depends on the sign of the offset value. A Geom_OffsetSurface surface can be self-intersecting, even if the basis surface does not self-intersect. The self-intersecting portions are not deleted at the time of construction. Warning There must be only one normal vector defined at any point on the basis surface. This must be verified by the user as no check is made at the time of construction to detect points with multiple possible normal directions (for example, the top of a conical surface).Describes an offset surface in 3D space. An offset surface is defined by: - the basis surface to which it is parallel, and - the distance between the offset surface and its basis surface. A point on the offset surface is built by measuring the offset value along the normal vector at a point on the basis surface. This normal vector is given by the cross product D1u^D1v, where D1u and D1v are the vectors tangential to the basis surface in the u and v parametric directions at this point. The side of the basis surface on which the offset is measured depends on the sign of the offset value. A Geom_OffsetSurface surface can be self-intersecting, even if the basis surface does not self-intersect. The self-intersecting portions are not deleted at the time of construction. Warning There must be only one normal vector defined at any point on the basis surface. This must be verified by the user as no check is made at the time of construction to detect points with multiple possible normal directions (for example, the top of a conical surface).
    """
    def BasisSurface(self) -> Geom_Surface: 
        """
        Returns the basis surface of this offset surface. Note: The basis surface can be an offset surface.
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this offset surface. If the surface is infinite, this function can return: - Standard_Real::RealFirst(), or - Standard_Real::RealLast().
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        This method returns the continuity of the basis surface - 1. Continuity of the Offset surface : C0 : only geometric continuity, C1 : continuity of the first derivative all along the Surface, C2 : continuity of the second derivative all along the Surface, C3 : continuity of the third derivative all along the Surface, CN : the order of continuity is infinite. Example : If the basis surface is C2 in the V direction and C3 in the U direction Shape = C1. Warnings : If the basis surface has a unique normal direction defined at any point this method gives the continuity of the offset surface otherwise the effective continuity can be lower than the continuity of the basis surface - 1.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this offset surface.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: ...
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the basis surface is not C2.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        ---Purpose ; Raised if the continuity of the basis surface is not C3.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the basis surface is not C4.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction u and Nv in the direction v. ---Purpose ; Raised if the continuity of the basis surface is not CNu + 1 in the U direction and CNv + 1 in the V direction. Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetBasisSurfContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns continuity of the basis surface.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCNu(self,N : int) -> bool: 
        """
        This method answer True if the continuity of the basis surface is N + 1 in the U parametric direction. We suppose in this class that a unique normal is defined at any point on the basis surface. Raised if N <0.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        This method answer True if the continuity of the basis surface is N + 1 in the V parametric direction. We suppose in this class that a unique normal is defined at any point on the basis surface. Raised if N <0.
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
    def IsUClosed(self) -> bool: 
        """
        Checks whether this offset surface is closed in the u parametric direction. Returns true if, taking uFirst and uLast as the parametric bounds in the u parametric direction, the distance between the points P(uFirst,v) and P(uLast,v) is less than or equal to gp::Resolution() for each value of the parameter v.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns true if this offset surface is periodic in the u parametric direction, i.e. if the basis surface of this offset surface is periodic in this direction.
        """
    def IsVClosed(self) -> bool: 
        """
        Checks whether this offset surface is closed in the u or v parametric direction. Returns true if taking vFirst and vLast as the parametric bounds in the v parametric direction, the distance between the points P(u,vFirst) and P(u,vLast) is less than or equal to gp::Resolution() for each value of the parameter u.
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns true if this offset surface is periodic in the v parametric direction, i.e. if the basis surface of this offset surface is periodic in this direction.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Offset(self) -> float: 
        """
        Returns the offset value of this offset surface.
        """
    def OsculatingSurface(self) -> Geom_OsculatingSurface: 
        """
        Returns osculating surface if base surface is B-spline or Bezier
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetBasisSurface(self,S : Geom_Surface,isNotCheckC0 : bool=False) -> None: 
        """
        Raised if S is not at least C1. Warnings : No check is done to verify that a unique normal direction is defined at any point of the basis surface S. If isNotCheckC0 = TRUE checking if basis surface has C0-continuity is not made. Exceptions Standard_ConstructionError if the surface S is not at least "C1" continuous.
        """
    def SetOffsetValue(self,D : float) -> None: 
        """
        Changes this offset surface by assigning D as the offset value.
        """
    def Surface(self) -> Geom_Surface: 
        """
        returns an equivalent surface of the offset surface when the basis surface is a canonic surface or a rectangular limited surface on canonic surface or if the offset is null.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this offset surface. Note: the basis surface is also modified.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve.
        """
    def UOsculatingSurface(self,U : float,V : float,IsOpposite : bool,UOsculSurf : Geom_BSplineSurface) -> bool: 
        """
        if Standard_True, L is the local osculating surface along U at the point U,V. It means that DL/DU is collinear to DS/DU . If IsOpposite == Standard_True these vectors have opposite direction.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this offset surface in the u parametric direction respectively, i.e. the period of the basis surface of this offset surface in this parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Changes the orientation of this offset surface in the u parametric direction. The bounds of the surface are not changed but the given parametric direction is reversed.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Computes the u parameter on the modified surface, produced by reversing the u parametric direction of this offset surface, for any point of u parameter U on this offset surface.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve.
        """
    def VOsculatingSurface(self,U : float,V : float,IsOpposite : bool,VOsculSurf : Geom_BSplineSurface) -> bool: 
        """
        if Standard_True, L is the local osculating surface along V at the point U,V. It means that DL/DV is collinear to DS/DV . If IsOpposite == Standard_True these vectors have opposite direction.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this offset surface in the v parametric direction respectively, i.e. the period of the basis surface of this offset surface in this parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Changes the orientation of this offset surface in the v parametric direction. The bounds of the surface are not changed but the given parametric direction is reversed.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Computes the v parameter on the modified surface, produced by reversing the or v parametric direction of this offset surface, for any point of v parameter V on this offset surface.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    def __init__(self,S : Geom_Surface,Offset : float,isNotCheckC0 : bool=False) -> None: ...
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
class Geom_OsculatingSurface(OCP.Standard.Standard_Transient):
    def BasisSurface(self) -> Geom_Surface: 
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def Init(self,BS : Geom_Surface,Tol : float) -> None: 
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Tolerance(self) -> float: 
        """
        None
        """
    def UOscSurf(self,U : float,V : float,t : bool,L : Geom_BSplineSurface) -> bool: 
        """
        if Standard_True, L is the local osculating surface along U at the point U,V.
        """
    def VOscSurf(self,U : float,V : float,t : bool,L : Geom_BSplineSurface) -> bool: 
        """
        if Standard_True, L is the local osculating surface along V at the point U,V.
        """
    @overload
    def __init__(self,BS : Geom_Surface,Tol : float) -> None: ...
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
class Geom_Parabola(Geom_Conic, Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a parabola in 3D space. A parabola is defined by its focal length (i.e. the distance between its focus and its apex) and is positioned in space with a coordinate system (gp_Ax2 object) where: - the origin is the apex of the parabola, - the "X Axis" defines the axis of symmetry; the parabola is on the positive side of this axis, - the origin, "X Direction" and "Y Direction" define the plane of the parabola. This coordinate system is the local coordinate system of the parabola. The "main Direction" of this coordinate system is a vector normal to the plane of the parabola. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the parabola. The "main Direction" of the local coordinate system gives an explicit orientation to the parabola, determining the direction in which the parameter increases along the parabola. The Geom_Parabola parabola is parameterized as follows: P(U) = O + U*U/(4.*F)*XDir + U*YDir where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - F is the focal length of the parabola. The parameter of the parabola is therefore its Y coordinate in the local coordinate system, with the "X Axis" of the local coordinate system defining the origin of the parameter. The parameter range is ] -infinite, +infinite [.Describes a parabola in 3D space. A parabola is defined by its focal length (i.e. the distance between its focus and its apex) and is positioned in space with a coordinate system (gp_Ax2 object) where: - the origin is the apex of the parabola, - the "X Axis" defines the axis of symmetry; the parabola is on the positive side of this axis, - the origin, "X Direction" and "Y Direction" define the plane of the parabola. This coordinate system is the local coordinate system of the parabola. The "main Direction" of this coordinate system is a vector normal to the plane of the parabola. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the parabola. The "main Direction" of the local coordinate system gives an explicit orientation to the parabola, determining the direction in which the parameter increases along the parabola. The Geom_Parabola parabola is parameterized as follows: P(U) = O + U*U/(4.*F)*XDir + U*YDir where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - F is the focal length of the parabola. The parameter of the parabola is therefore its Y coordinate in the local coordinate system, with the "X Axis" of the local coordinate system defining the origin of the parameter. The parameter range is ] -infinite, +infinite [.Describes a parabola in 3D space. A parabola is defined by its focal length (i.e. the distance between its focus and its apex) and is positioned in space with a coordinate system (gp_Ax2 object) where: - the origin is the apex of the parabola, - the "X Axis" defines the axis of symmetry; the parabola is on the positive side of this axis, - the origin, "X Direction" and "Y Direction" define the plane of the parabola. This coordinate system is the local coordinate system of the parabola. The "main Direction" of this coordinate system is a vector normal to the plane of the parabola. The axis, of which the origin and unit vector are respectively the origin and "main Direction" of the local coordinate system, is termed the "Axis" or "main Axis" of the parabola. The "main Direction" of the local coordinate system gives an explicit orientation to the parabola, determining the direction in which the parameter increases along the parabola. The Geom_Parabola parabola is parameterized as follows: P(U) = O + U*U/(4.*F)*XDir + U*YDir where: - P is the point of parameter U, - O, XDir and YDir are respectively the origin, "X Direction" and "Y Direction" of its local coordinate system, - F is the focal length of the parabola. The parameter of the parabola is therefore its Y coordinate in the local coordinate system, with the "X Axis" of the local coordinate system defining the origin of the parameter. The parameter range is ] -infinite, +infinite [.
    """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the "main Axis" of this conic. This axis is normal to the plane of the conic.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        The continuity of the conic is Cn.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this parabola.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U. If U = 0 the returned point is the origin of the XAxis and the YAxis of the parabola and it is the vertex of the parabola. P = S + F * (U * U * XDir + * U * YDir) where S is the vertex of the parabola, XDir the XDirection and YDir the YDirection of the parabola's local coordinate system.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U and the first derivative V1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point P of parameter U, the first second and third derivatives V1 V2 and V3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        For the point of parameter U of this parabola, computes the vector corresponding to the Nth derivative. Exceptions Standard_RangeError if N is less than 1.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Directrix(self) -> OCP.gp.gp_Ax1: 
        """
        Computes the directrix of this parabola. This is a line normal to the axis of symmetry, in the plane of this parabola, located on the negative side of its axis of symmetry, at a distance from the apex equal to the focal length. The directrix is returned as an axis (gp_Ax1 object), where the origin is located on the "X Axis" of this parabola.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Eccentricity(self) -> float: 
        """
        Returns 1. (which is the eccentricity of any parabola).
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first or last parameter of this parabola. This is, respectively: - Standard_Real::RealFirst(), or - Standard_Real::RealLast().
        """
    def Focal(self) -> float: 
        """
        Computes the focal distance of this parabola The focal distance is the distance between the apex and the focus of the parabola.
        """
    def Focus(self) -> OCP.gp.gp_Pnt: 
        """
        Computes the focus of this parabola. The focus is on the positive side of the "X Axis" of the local coordinate system of the parabola.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns True. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns False
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
    def IsPeriodic(self) -> bool: 
        """
        Returns False
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the first or last parameter of this parabola. This is, respectively: - Standard_Real::RealFirst(), or - Standard_Real::RealLast().
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the conic. For the circle, the ellipse and the hyperbola it is the center of the conic. For the parabola it is the Apex of the parabola.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Parab(self) -> OCP.gp.gp_Parab: 
        """
        Returns the non transient parabola from gp with the same geometric properties as <me>.
        """
    def Parameter(self) -> float: 
        """
        Computes the parameter of this parabola which is the distance between its focus and its directrix. This distance is twice the focal length. If P is the parameter of the parabola, the equation of the parabola in its local coordinate system is: Y**2 = 2.*P*X.
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of this curve. Exceptions Standard_NoSuchObject if this curve is not periodic.
        """
    def Position(self) -> OCP.gp.gp_Ax2: 
        """
        Returns the local coordinates system of the conic. The main direction of the Axis2Placement is normal to the plane of the conic. The X direction of the Axis2placement is in the plane of the conic and corresponds to the origin for the conic's parametric value u.
        """
    def Reverse(self) -> None: 
        """
        Reverses the direction of parameterization of <me>. The local coordinate system of the conic is modified.
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Computes the parameter on the reversed parabola, for the point of parameter U on this parabola. For a parabola, the returned value is: -U.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the orientation of the conic's plane. The normal axis to the plane is A1. The XAxis and the YAxis are recomputed.
        """
    def SetFocal(self,Focal : float) -> None: 
        """
        Assigns the value Focal to the focal distance of this parabola. Exceptions Standard_ConstructionError if Focal is negative.
        """
    def SetLocation(self,theP : OCP.gp.gp_Pnt) -> None: 
        """
        changes the location point of the conic.
        """
    def SetParab(self,Prb : OCP.gp.gp_Parab) -> None: 
        """
        Converts the gp_Parab parabola Prb into this parabola.
        """
    def SetPosition(self,theA2 : OCP.gp.gp_Ax2) -> None: 
        """
        changes the local coordinate system of the conic.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this parabola.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    def XAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the XAxis of the conic. This axis defines the origin of parametrization of the conic. This axis is perpendicular to the Axis of the conic. This axis and the Yaxis define the plane of the conic.
        """
    def YAxis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the YAxis of the conic. The YAxis is perpendicular to the Xaxis. This axis and the Xaxis define the plane of the conic.
        """
    @overload
    def __init__(self,D : OCP.gp.gp_Ax1,F : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Prb : OCP.gp.gp_Parab) -> None: ...
    @overload
    def __init__(self,A2 : OCP.gp.gp_Ax2,Focal : float) -> None: ...
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
class Geom_Plane(Geom_ElementarySurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a plane in 3D space. A plane is positioned in space by a coordinate system (a gp_Ax3 object) such that the plane is defined by the origin, "X Direction" and "Y Direction" of this coordinate system. This coordinate system is the "local coordinate system" of the plane. The following apply: - Its "X Direction" and "Y Direction" are respectively the u and v parametric directions of the plane. - Its origin is the origin of the u and v parameters (also called the "origin" of the plane). - Its "main Direction" is a vector normal to the plane. This normal vector gives the orientation of the plane only if the local coordinate system is "direct". (The orientation of the plane is always defined by the "X Direction" and the "Y Direction" of its local coordinate system.) The parametric equation of the plane is: P(u, v) = O + u*XDir + v*YDir where O, XDir and YDir are respectively the origin, the "X Direction" and the "Y Direction" of the local coordinate system of the plane. The parametric range of the two parameters u and v is ] -infinity, +infinity [.Describes a plane in 3D space. A plane is positioned in space by a coordinate system (a gp_Ax3 object) such that the plane is defined by the origin, "X Direction" and "Y Direction" of this coordinate system. This coordinate system is the "local coordinate system" of the plane. The following apply: - Its "X Direction" and "Y Direction" are respectively the u and v parametric directions of the plane. - Its origin is the origin of the u and v parameters (also called the "origin" of the plane). - Its "main Direction" is a vector normal to the plane. This normal vector gives the orientation of the plane only if the local coordinate system is "direct". (The orientation of the plane is always defined by the "X Direction" and the "Y Direction" of its local coordinate system.) The parametric equation of the plane is: P(u, v) = O + u*XDir + v*YDir where O, XDir and YDir are respectively the origin, the "X Direction" and the "Y Direction" of the local coordinate system of the plane. The parametric range of the two parameters u and v is ] -infinity, +infinity [.Describes a plane in 3D space. A plane is positioned in space by a coordinate system (a gp_Ax3 object) such that the plane is defined by the origin, "X Direction" and "Y Direction" of this coordinate system. This coordinate system is the "local coordinate system" of the plane. The following apply: - Its "X Direction" and "Y Direction" are respectively the u and v parametric directions of the plane. - Its origin is the origin of the u and v parameters (also called the "origin" of the plane). - Its "main Direction" is a vector normal to the plane. This normal vector gives the orientation of the plane only if the local coordinate system is "direct". (The orientation of the plane is always defined by the "X Direction" and the "Y Direction" of its local coordinate system.) The parametric equation of the plane is: P(u, v) = O + u*XDir + v*YDir where O, XDir and YDir are respectively the origin, the "X Direction" and the "Y Direction" of the local coordinate system of the plane. The parametric range of the two parameters u and v is ] -infinity, +infinity [.
    """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the main axis of the surface (ZAxis).
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this plane. Because a plane is an infinite surface, the following is always true: - U1 = V1 = Standard_Real::RealFirst() - U2 = V2 = Standard_Real::RealLast().
        """
    def Coefficients(self) -> Tuple[float, float, float, float]: 
        """
        Computes the normalized coefficients of the plane's cartesian equation : Ax + By + Cz + D = 0.0
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_CN, the global continuity of any elementary surface.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this plane.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point P (U, V) on <me>. P = O + U * XDir + V * YDir. where O is the "Location" point of the plane, XDir the "XDirection" and YDir the "YDirection" of the plane's local coordinate system.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point and the first derivatives in the directions U and V.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first and the second derivatives in the directions U and V.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first,the second and the third derivatives in the directions U and V.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction u and Nv in the direction v. Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns True.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns True.
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
    def IsUClosed(self) -> bool: 
        """
        return False
        """
    def IsUPeriodic(self) -> bool: 
        """
        return False.
        """
    def IsVClosed(self) -> bool: 
        """
        return False
        """
    def IsVPeriodic(self) -> bool: 
        """
        return False.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the local coordinate system of the surface.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface. me->Transformed(T)->Value(U',V') is the same point as me->Value(U,V).Transformed(T) Where U',V' are obtained by transforming U,V with th 2d transformation returned by me->ParametricTransformation(T) This methods returns a scale centered on the origin with T.ScaleFactor
        """
    def Pln(self) -> OCP.gp.gp_Pln: 
        """
        Converts this plane into a gp_Pln plane.
        """
    def Position(self) -> OCP.gp.gp_Ax3: 
        """
        Returns the local coordinates system of the surface.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the main axis (ZAxis) of the elementary surface.
        """
    def SetLocation(self,theLoc : OCP.gp.gp_Pnt) -> None: 
        """
        Changes the location of the local coordinates system of the surface.
        """
    def SetPln(self,Pl : OCP.gp.gp_Pln) -> None: 
        """
        Set <me> so that <me> has the same geometric properties as Pl.
        """
    def SetPosition(self,theAx3 : OCP.gp.gp_Ax3) -> None: 
        """
        Changes the local coordinates system of the surface.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this plane.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>. me->Transformed(T)->Value(U',V') is the same point as me->Value(U,V).Transformed(T) Where U',V' are the new values of U,V after calling me->TranformParameters(U,V,T) This methods multiplies U and V by T.ScaleFactor()
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve. This is a Line parallel to the YAxis of the plane.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Changes the orientation of this plane in the u (or v) parametric direction. The bounds of the plane are not changed but the given parametric direction is reversed. Hence the orientation of the surface is reversed.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Computes the u parameter on the modified plane, produced when reversing the u parametric of this plane, for any point of u parameter U on this plane. In the case of a plane, these methods return - -U.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve. This is a Line parallel to the XAxis of the plane.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Changes the orientation of this plane in the u (or v) parametric direction. The bounds of the plane are not changed but the given parametric direction is reversed. Hence the orientation of the surface is reversed.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Computes the v parameter on the modified plane, produced when reversing the v parametric of this plane, for any point of v parameter V on this plane. In the case of a plane, these methods return -V.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    @overload
    def __init__(self,A : float,B : float,C : float,D : float) -> None: ...
    @overload
    def __init__(self,Pl : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,A3 : OCP.gp.gp_Ax3) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Dir) -> None: ...
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
class Geom_CartesianPoint(Geom_Point, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a point in 3D space. A Geom_CartesianPoint is defined by a gp_Pnt point, with its three Cartesian coordinates X, Y and Z.Describes a point in 3D space. A Geom_CartesianPoint is defined by a gp_Pnt point, with its three Cartesian coordinates X, Y and Z.Describes a point in 3D space. A Geom_CartesianPoint is defined by a gp_Pnt point, with its three Cartesian coordinates X, Y and Z.
    """
    def Coord(self) -> Tuple[float, float, float]: 
        """
        Returns the coordinates of <me>.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this point.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Distance(self,Other : Geom_Point) -> float: 
        """
        Computes the distance between <me> and <Other>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Pnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns a non transient cartesian point with the same coordinates as <me>.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetCoord(self,X : float,Y : float,Z : float) -> None: 
        """
        Assigns the coordinates X, Y and Z to this point.
        """
    def SetPnt(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Set <me> to P.X(), P.Y(), P.Z() coordinates.
        """
    def SetX(self,X : float) -> None: 
        """
        Changes the X coordinate of me.
        """
    def SetY(self,Y : float) -> None: 
        """
        Changes the Y coordinate of me.
        """
    def SetZ(self,Z : float) -> None: 
        """
        Changes the Z coordinate of me.
        """
    def SquareDistance(self,Other : Geom_Point) -> float: 
        """
        Computes the square distance between <me> and <Other>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this point.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def X(self) -> float: 
        """
        Returns the X coordinate of <me>.
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate of <me>.
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate of <me>.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,X : float,Y : float,Z : float) -> None: ...
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
class Geom_RectangularTrimmedSurface(Geom_BoundedSurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a portion of a surface (a patch) limited by two values of the u parameter in the u parametric direction, and two values of the v parameter in the v parametric direction. The domain of the trimmed surface must be within the domain of the surface being trimmed. The trimmed surface is defined by: - the basis surface, and - the values (umin, umax) and (vmin, vmax) which limit it in the u and v parametric directions. The trimmed surface is built from a copy of the basis surface. Therefore, when the basis surface is modified the trimmed surface is not changed. Consequently, the trimmed surface does not necessarily have the same orientation as the basis surface. Warning: The case of surface being trimmed is periodic and parametrics values are outside the domain is possible. But, domain of the trimmed surface can be translated by (n X) the period.Describes a portion of a surface (a patch) limited by two values of the u parameter in the u parametric direction, and two values of the v parameter in the v parametric direction. The domain of the trimmed surface must be within the domain of the surface being trimmed. The trimmed surface is defined by: - the basis surface, and - the values (umin, umax) and (vmin, vmax) which limit it in the u and v parametric directions. The trimmed surface is built from a copy of the basis surface. Therefore, when the basis surface is modified the trimmed surface is not changed. Consequently, the trimmed surface does not necessarily have the same orientation as the basis surface. Warning: The case of surface being trimmed is periodic and parametrics values are outside the domain is possible. But, domain of the trimmed surface can be translated by (n X) the period.Describes a portion of a surface (a patch) limited by two values of the u parameter in the u parametric direction, and two values of the v parameter in the v parametric direction. The domain of the trimmed surface must be within the domain of the surface being trimmed. The trimmed surface is defined by: - the basis surface, and - the values (umin, umax) and (vmin, vmax) which limit it in the u and v parametric directions. The trimmed surface is built from a copy of the basis surface. Therefore, when the basis surface is modified the trimmed surface is not changed. Consequently, the trimmed surface does not necessarily have the same orientation as the basis surface. Warning: The case of surface being trimmed is periodic and parametrics values are outside the domain is possible. But, domain of the trimmed surface can be translated by (n X) the period.
    """
    def BasisSurface(self) -> Geom_Surface: 
        """
        Returns the Basis surface of <me>.
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this patch.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of the surface : C0 : only geometric continuity, C1 : continuity of the first derivative all along the Surface, C2 : continuity of the second derivative all along the Surface, C3 : continuity of the third derivative all along the Surface, CN : the order of continuity is infinite.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this patch.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Can be raised if the basis surface is an OffsetSurface.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        The returned derivatives have the same orientation as the derivatives of the basis surface even if the trimmed surface has not the same parametric orientation. Warning! UndefinedDerivative raised if the continuity of the surface is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        The returned derivatives have the same orientation as the derivatives of the basis surface even if the trimmed surface has not the same parametric orientation. Warning! UndefinedDerivative raised if the continuity of the surface is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        The returned derivatives have the same orientation as the derivatives of the basis surface even if the trimmed surface has not the same parametric orientation. Warning UndefinedDerivative raised if the continuity of the surface is not C3.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        The returned derivative has the same orientation as the derivative of the basis surface even if the trimmed surface has not the same parametric orientation. Warning! UndefinedDerivative raised if the continuity of the surface is not CNu in the U parametric direction and CNv in the V parametric direction. RangeError Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns true if the order of derivation in the U parametric direction is N. Raised if N < 0.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns true if the order of derivation in the V parametric direction is N. Raised if N < 0.
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
    def IsUClosed(self) -> bool: 
        """
        Returns true if this patch is closed in the given parametric direction.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns true if this patch is periodic and not trimmed in the given parametric direction.
        """
    def IsVClosed(self) -> bool: 
        """
        Returns true if this patch is closed in the given parametric direction.
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns true if this patch is periodic and not trimmed in the given parametric direction.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def SetTrim(self,Param1 : float,Param2 : float,UTrim : bool,Sense : bool=True) -> None: 
        """
        Modifies this patch by changing the trim values applied to the original surface The u parametric direction of this patch is oriented from U1 to U2. The v parametric direction of this patch is oriented from V1 to V2. USense and VSense are used for the construction only if the surface is periodic in the corresponding parametric direction, and define the available part of the surface; by default in this case, this patch has the same orientation as the basis surface. Raised if The BasisSurface is not periodic in the UDirection and U1 or U2 are out of the bounds of the BasisSurface. The BasisSurface is not periodic in the VDirection and V1 or V2 are out of the bounds of the BasisSurface. U1 = U2 or V1 = V2

        Modifies this patch by changing the trim values applied to the original surface The basis surface is trimmed only in one parametric direction: if UTrim is true, the surface is trimmed in the u parametric direction; if it is false, it is trimmed in the v parametric direction. In the "trimmed" direction, this patch is oriented from Param1 to Param2. If the basis surface is periodic in the "trimmed" direction, Sense defines its available part. By default in this case, this patch has the same orientation as the basis surface in this parametric direction. If the basis surface is closed or periodic in the other parametric direction (i.e. not the "trimmed" direction), this patch has the same characteristics as the basis surface in that parametric direction. Raised if The BasisSurface is not periodic in the considered direction and Param1 or Param2 are out of the bounds of the BasisSurface. Param1 = Param2
        """
    @overload
    def SetTrim(self,U1 : float,U2 : float,V1 : float,V2 : float,USense : bool=True,VSense : bool=True) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this patch. Warning As a consequence, the basis surface included in the data structure of this patch is also modified.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        computes the U isoparametric curve.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this patch in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Changes the orientation of this patch in the u parametric direction. The bounds of the surface are not changed, but the given parametric direction is reversed. Hence the orientation of the surface is reversed.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Computes the u parameter on the modified surface, produced by when reversing its u parametric direction, for any point of u parameter U on this patch.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this patch in the v parametric direction. raises if the surface is not vperiodic. value and derivatives
        """
    def VReverse(self) -> None: 
        """
        Changes the orientation of this patch in the v parametric direction. The bounds of the surface are not changed, but the given parametric direction is reversed. Hence the orientation of the surface is reversed.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Computes the v parameter on the modified surface, produced by when reversing its v parametric direction, for any point of v parameter V on this patch.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    @overload
    def __init__(self,S : Geom_Surface,U1 : float,U2 : float,V1 : float,V2 : float,USense : bool=True,VSense : bool=True) -> None: ...
    @overload
    def __init__(self,S : Geom_Surface,Param1 : float,Param2 : float,UTrim : bool,Sense : bool=True) -> None: ...
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
class Geom_HSequenceOfBSplineSurface(Geom_SequenceOfBSplineSurface, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Geom_BSplineSurface) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : Geom_SequenceOfBSplineSurface) -> None: ...
    def Assign(self,theOther : Geom_SequenceOfBSplineSurface) -> Geom_SequenceOfBSplineSurface: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Geom_BSplineSurface: 
        """
        First item access
        """
    def ChangeLast(self) -> Geom_BSplineSurface: 
        """
        Last item access
        """
    def ChangeSequence(self) -> Geom_SequenceOfBSplineSurface: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> Geom_BSplineSurface: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
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
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> Geom_BSplineSurface: 
        """
        First item access
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
    def InsertAfter(self,theIndex : int,theItem : Geom_BSplineSurface) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Geom_SequenceOfBSplineSurface) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Geom_SequenceOfBSplineSurface) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Geom_BSplineSurface) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> Geom_BSplineSurface: 
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
    def Prepend(self,theItem : Geom_BSplineSurface) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Geom_SequenceOfBSplineSurface) -> None: ...
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
    def Sequence(self) -> Geom_SequenceOfBSplineSurface: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : Geom_BSplineSurface) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Geom_SequenceOfBSplineSurface) -> None: 
        """
        Split in two sequences
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Geom_BSplineSurface: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Geom_SequenceOfBSplineSurface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
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
class Geom_SphericalSurface(Geom_ElementarySurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a sphere. A sphere is defined by its radius, and is positioned in space by a coordinate system (a gp_Ax3 object), the origin of which is the center of the sphere. This coordinate system is the "local coordinate system" of the sphere. The following apply: - Rotation around its "main Axis", in the trigonometric sense given by the "X Direction" and the "Y Direction", defines the u parametric direction. - Its "X Axis" gives the origin for the u parameter. - The "reference meridian" of the sphere is a half-circle, of radius equal to the radius of the sphere. It is located in the plane defined by the origin, "X Direction" and "main Direction", centered on the origin, and positioned on the positive side of the "X Axis". - Rotation around the "Y Axis" gives the v parameter on the reference meridian. - The "X Axis" gives the origin of the v parameter on the reference meridian. - The v parametric direction is oriented by the "main Direction", i.e. when v increases, the Z coordinate increases. (This implies that the "Y Direction" orients the reference meridian only when the local coordinate system is indirect.) - The u isoparametric curve is a half-circle obtained by rotating the reference meridian of the sphere through an angle u around the "main Axis", in the trigonometric sense defined by the "X Direction" and the "Y Direction". The parametric equation of the sphere is: P(u,v) = O + R*cos(v)*(cos(u)*XDir + sin(u)*YDir)+R*sin(v)*ZDir where: - O, XDir, YDir and ZDir are respectively the origin, the "X Direction", the "Y Direction" and the "Z Direction" of its local coordinate system, and - R is the radius of the sphere. The parametric range of the two parameters is: - [ 0, 2.*Pi ] for u, and - [ - Pi/2., + Pi/2. ] for v.Describes a sphere. A sphere is defined by its radius, and is positioned in space by a coordinate system (a gp_Ax3 object), the origin of which is the center of the sphere. This coordinate system is the "local coordinate system" of the sphere. The following apply: - Rotation around its "main Axis", in the trigonometric sense given by the "X Direction" and the "Y Direction", defines the u parametric direction. - Its "X Axis" gives the origin for the u parameter. - The "reference meridian" of the sphere is a half-circle, of radius equal to the radius of the sphere. It is located in the plane defined by the origin, "X Direction" and "main Direction", centered on the origin, and positioned on the positive side of the "X Axis". - Rotation around the "Y Axis" gives the v parameter on the reference meridian. - The "X Axis" gives the origin of the v parameter on the reference meridian. - The v parametric direction is oriented by the "main Direction", i.e. when v increases, the Z coordinate increases. (This implies that the "Y Direction" orients the reference meridian only when the local coordinate system is indirect.) - The u isoparametric curve is a half-circle obtained by rotating the reference meridian of the sphere through an angle u around the "main Axis", in the trigonometric sense defined by the "X Direction" and the "Y Direction". The parametric equation of the sphere is: P(u,v) = O + R*cos(v)*(cos(u)*XDir + sin(u)*YDir)+R*sin(v)*ZDir where: - O, XDir, YDir and ZDir are respectively the origin, the "X Direction", the "Y Direction" and the "Z Direction" of its local coordinate system, and - R is the radius of the sphere. The parametric range of the two parameters is: - [ 0, 2.*Pi ] for u, and - [ - Pi/2., + Pi/2. ] for v.Describes a sphere. A sphere is defined by its radius, and is positioned in space by a coordinate system (a gp_Ax3 object), the origin of which is the center of the sphere. This coordinate system is the "local coordinate system" of the sphere. The following apply: - Rotation around its "main Axis", in the trigonometric sense given by the "X Direction" and the "Y Direction", defines the u parametric direction. - Its "X Axis" gives the origin for the u parameter. - The "reference meridian" of the sphere is a half-circle, of radius equal to the radius of the sphere. It is located in the plane defined by the origin, "X Direction" and "main Direction", centered on the origin, and positioned on the positive side of the "X Axis". - Rotation around the "Y Axis" gives the v parameter on the reference meridian. - The "X Axis" gives the origin of the v parameter on the reference meridian. - The v parametric direction is oriented by the "main Direction", i.e. when v increases, the Z coordinate increases. (This implies that the "Y Direction" orients the reference meridian only when the local coordinate system is indirect.) - The u isoparametric curve is a half-circle obtained by rotating the reference meridian of the sphere through an angle u around the "main Axis", in the trigonometric sense defined by the "X Direction" and the "Y Direction". The parametric equation of the sphere is: P(u,v) = O + R*cos(v)*(cos(u)*XDir + sin(u)*YDir)+R*sin(v)*ZDir where: - O, XDir, YDir and ZDir are respectively the origin, the "X Direction", the "Y Direction" and the "Z Direction" of its local coordinate system, and - R is the radius of the sphere. The parametric range of the two parameters is: - [ 0, 2.*Pi ] for u, and - [ - Pi/2., + Pi/2. ] for v.
    """
    def Area(self) -> float: 
        """
        Computes the aera of the spherical surface.
        """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the main axis of the surface (ZAxis).
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this sphere. For a sphere: U1 = 0, U2 = 2*PI, V1 = -PI/2, V2 = PI/2.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float, float, float, float, float]: 
        """
        Returns the coefficients of the implicit equation of the quadric in the absolute cartesian coordinates system : These coefficients are normalized. A1.X**2 + A2.Y**2 + A3.Z**2 + 2.(B1.X.Y + B2.X.Z + B3.Y.Z) + 2.(C1.X + C2.Y + C3.Z) + D = 0.0
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_CN, the global continuity of any elementary surface.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this sphere.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point P (U, V) on the surface. P (U, V) = Loc + Radius * Sin (V) * Zdir + Radius * Cos (V) * (cos (U) * XDir + sin (U) * YDir) where Loc is the origin of the placement plane (XAxis, YAxis) XDir is the direction of the XAxis and YDir the direction of the YAxis and ZDir the direction of the ZAxis.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point and the first derivatives in the directions U and V.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first and the second derivatives in the directions U and V.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first,the second and the third derivatives in the directions U and V.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction u and Nv in the direction v. Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns True.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns True.
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
    def IsUClosed(self) -> bool: 
        """
        Returns True.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns True.
        """
    def IsVClosed(self) -> bool: 
        """
        Returns False.
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns False.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the local coordinate system of the surface.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Position(self) -> OCP.gp.gp_Ax3: 
        """
        Returns the local coordinates system of the surface.
        """
    def Radius(self) -> float: 
        """
        Computes the coefficients of the implicit equation of this quadric in the absolute Cartesian coordinate system: A1.X**2 + A2.Y**2 + A3.Z**2 + 2.(B1.X.Y + B2.X.Z + B3.Y.Z) + 2.(C1.X + C2.Y + C3.Z) + D = 0.0 An implicit normalization is applied (i.e. A1 = A2 = 1. in the local coordinate system of this sphere).
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the main axis (ZAxis) of the elementary surface.
        """
    def SetLocation(self,theLoc : OCP.gp.gp_Pnt) -> None: 
        """
        Changes the location of the local coordinates system of the surface.
        """
    def SetPosition(self,theAx3 : OCP.gp.gp_Ax3) -> None: 
        """
        Changes the local coordinates system of the surface.
        """
    def SetRadius(self,R : float) -> None: 
        """
        Assigns the value R to the radius of this sphere. Exceptions Standard_ConstructionError if R is less than 0.0.
        """
    def SetSphere(self,S : OCP.gp.gp_Sphere) -> None: 
        """
        Converts the gp_Sphere S into this sphere.
        """
    def Sphere(self) -> OCP.gp.gp_Sphere: 
        """
        Returns a non persistent sphere with the same geometric properties as <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this sphere.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve. The U isoparametric curves of the surface are defined by the section of the spherical surface with plane obtained by rotation of the plane (Location, XAxis, ZAxis) around ZAxis. This plane defines the origin of parametrization u. For a SphericalSurface the UIso curve is a Circle. Warnings : The radius of this circle can be zero.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Reverses the U parametric direction of the surface.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Computes the u parameter on the modified surface, when reversing its u parametric direction, for any point of u parameter U on this sphere. In the case of a sphere, these functions returns 2.PI - U.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve. The V isoparametric curves of the surface are defined by the section of the spherical surface with plane parallel to the plane (Location, XAxis, YAxis). This plane defines the origin of parametrization V. Be careful if V is close to PI/2 or 3*PI/2 the radius of the circle becomes tiny. It is not forbidden in this toolkit to create circle with radius = 0.0 For a SphericalSurface the VIso curve is a Circle. Warnings : The radius of this circle can be zero.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V parametric direction of the surface.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Computes the v parameter on the modified surface, when reversing its v parametric direction, for any point of v parameter V on this sphere. In the case of a sphere, these functions returns -U.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    def Volume(self) -> float: 
        """
        Computes the volume of the spherical surface.
        """
    @overload
    def __init__(self,A3 : OCP.gp.gp_Ax3,Radius : float) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere) -> None: ...
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
class Geom_BezierSurface(Geom_BoundedSurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a rational or non-rational Bezier surface. - A non-rational Bezier surface is defined by a table of poles (also known as control points). - A rational Bezier surface is defined by a table of poles with varying associated weights. This data is manipulated using two associative 2D arrays: - the poles table, which is a 2D array of gp_Pnt, and - the weights table, which is a 2D array of reals. The bounds of these arrays are: - 1 and NbUPoles for the row bounds, where NbUPoles is the number of poles of the surface in the u parametric direction, and - 1 and NbVPoles for the column bounds, where NbVPoles is the number of poles of the surface in the v parametric direction. The poles of the surface, the "control points", are the points used to shape and reshape the surface. They comprise a rectangular network of points: - The points (1, 1), (NbUPoles, 1), (1, NbVPoles) and (NbUPoles, NbVPoles) are the four parametric "corners" of the surface. - The first column of poles and the last column of poles define two Bezier curves which delimit the surface in the v parametric direction. These are the v isoparametric curves corresponding to values 0 and 1 of the v parameter. - The first row of poles and the last row of poles define two Bezier curves which delimit the surface in the u parametric direction. These are the u isoparametric curves corresponding to values 0 and 1 of the u parameter. It is more difficult to define a geometrical significance for the weights. However they are useful for representing a quadric surface precisely. Moreover, if the weights of all the poles are equal, the surface has a polynomial equation, and hence is a "non-rational surface". The non-rational surface is a special, but frequently used, case, where all poles have identical weights. The weights are defined and used only in the case of a rational surface. This rational characteristic is defined in each parametric direction. Hence, a surface can be rational in the u parametric direction, and non-rational in the v parametric direction. Likewise, the degree of a surface is defined in each parametric direction. The degree of a Bezier surface in a given parametric direction is equal to the number of poles of the surface in that parametric direction, minus 1. This must be greater than or equal to 1. However, the degree for a Geom_BezierSurface is limited to a value of (25) which is defined and controlled by the system. This value is returned by the function MaxDegree. The parameter range for a Bezier surface is [ 0, 1 ] in the two parametric directions. A Bezier surface can also be closed, or open, in each parametric direction. If the first row of poles is identical to the last row of poles, the surface is closed in the u parametric direction. If the first column of poles is identical to the last column of poles, the surface is closed in the v parametric direction. The continuity of a Bezier surface is infinite in the u parametric direction and the in v parametric direction. Note: It is not possible to build a Bezier surface with negative weights. Any weight value that is less than, or equal to, gp::Resolution() is considered to be zero. Two weight values, W1 and W2, are considered equal if: |W2-W1| <= gp::Resolution()Describes a rational or non-rational Bezier surface. - A non-rational Bezier surface is defined by a table of poles (also known as control points). - A rational Bezier surface is defined by a table of poles with varying associated weights. This data is manipulated using two associative 2D arrays: - the poles table, which is a 2D array of gp_Pnt, and - the weights table, which is a 2D array of reals. The bounds of these arrays are: - 1 and NbUPoles for the row bounds, where NbUPoles is the number of poles of the surface in the u parametric direction, and - 1 and NbVPoles for the column bounds, where NbVPoles is the number of poles of the surface in the v parametric direction. The poles of the surface, the "control points", are the points used to shape and reshape the surface. They comprise a rectangular network of points: - The points (1, 1), (NbUPoles, 1), (1, NbVPoles) and (NbUPoles, NbVPoles) are the four parametric "corners" of the surface. - The first column of poles and the last column of poles define two Bezier curves which delimit the surface in the v parametric direction. These are the v isoparametric curves corresponding to values 0 and 1 of the v parameter. - The first row of poles and the last row of poles define two Bezier curves which delimit the surface in the u parametric direction. These are the u isoparametric curves corresponding to values 0 and 1 of the u parameter. It is more difficult to define a geometrical significance for the weights. However they are useful for representing a quadric surface precisely. Moreover, if the weights of all the poles are equal, the surface has a polynomial equation, and hence is a "non-rational surface". The non-rational surface is a special, but frequently used, case, where all poles have identical weights. The weights are defined and used only in the case of a rational surface. This rational characteristic is defined in each parametric direction. Hence, a surface can be rational in the u parametric direction, and non-rational in the v parametric direction. Likewise, the degree of a surface is defined in each parametric direction. The degree of a Bezier surface in a given parametric direction is equal to the number of poles of the surface in that parametric direction, minus 1. This must be greater than or equal to 1. However, the degree for a Geom_BezierSurface is limited to a value of (25) which is defined and controlled by the system. This value is returned by the function MaxDegree. The parameter range for a Bezier surface is [ 0, 1 ] in the two parametric directions. A Bezier surface can also be closed, or open, in each parametric direction. If the first row of poles is identical to the last row of poles, the surface is closed in the u parametric direction. If the first column of poles is identical to the last column of poles, the surface is closed in the v parametric direction. The continuity of a Bezier surface is infinite in the u parametric direction and the in v parametric direction. Note: It is not possible to build a Bezier surface with negative weights. Any weight value that is less than, or equal to, gp::Resolution() is considered to be zero. Two weight values, W1 and W2, are considered equal if: |W2-W1| <= gp::Resolution()Describes a rational or non-rational Bezier surface. - A non-rational Bezier surface is defined by a table of poles (also known as control points). - A rational Bezier surface is defined by a table of poles with varying associated weights. This data is manipulated using two associative 2D arrays: - the poles table, which is a 2D array of gp_Pnt, and - the weights table, which is a 2D array of reals. The bounds of these arrays are: - 1 and NbUPoles for the row bounds, where NbUPoles is the number of poles of the surface in the u parametric direction, and - 1 and NbVPoles for the column bounds, where NbVPoles is the number of poles of the surface in the v parametric direction. The poles of the surface, the "control points", are the points used to shape and reshape the surface. They comprise a rectangular network of points: - The points (1, 1), (NbUPoles, 1), (1, NbVPoles) and (NbUPoles, NbVPoles) are the four parametric "corners" of the surface. - The first column of poles and the last column of poles define two Bezier curves which delimit the surface in the v parametric direction. These are the v isoparametric curves corresponding to values 0 and 1 of the v parameter. - The first row of poles and the last row of poles define two Bezier curves which delimit the surface in the u parametric direction. These are the u isoparametric curves corresponding to values 0 and 1 of the u parameter. It is more difficult to define a geometrical significance for the weights. However they are useful for representing a quadric surface precisely. Moreover, if the weights of all the poles are equal, the surface has a polynomial equation, and hence is a "non-rational surface". The non-rational surface is a special, but frequently used, case, where all poles have identical weights. The weights are defined and used only in the case of a rational surface. This rational characteristic is defined in each parametric direction. Hence, a surface can be rational in the u parametric direction, and non-rational in the v parametric direction. Likewise, the degree of a surface is defined in each parametric direction. The degree of a Bezier surface in a given parametric direction is equal to the number of poles of the surface in that parametric direction, minus 1. This must be greater than or equal to 1. However, the degree for a Geom_BezierSurface is limited to a value of (25) which is defined and controlled by the system. This value is returned by the function MaxDegree. The parameter range for a Bezier surface is [ 0, 1 ] in the two parametric directions. A Bezier surface can also be closed, or open, in each parametric direction. If the first row of poles is identical to the last row of poles, the surface is closed in the u parametric direction. If the first column of poles is identical to the last column of poles, the surface is closed in the v parametric direction. The continuity of a Bezier surface is infinite in the u parametric direction and the in v parametric direction. Note: It is not possible to build a Bezier surface with negative weights. Any weight value that is less than, or equal to, gp::Resolution() is considered to be zero. Two weight values, W1 and W2, are considered equal if: |W2-W1| <= gp::Resolution()
    """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this Bezier surface. In the case of a Bezier surface, this function returns U1 = 0, V1 = 0, U2 = 1, V2 = 1.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of the surface CN : the order of continuity is infinite.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this Bezier surface.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes P, the point of parameters (U, V) of this Bezier surface, and - one or more of the following sets of vectors: - D1U and D1V, the first derivative vectors at this point, - D2U, D2V and D2UV, the second derivative vectors at this point, - D3U, D3V, D3UUV and D3UVV, the third derivative vectors at this point. Note: The parameters U and V can be outside the bounds of the surface.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the u parametric direction, and Nv in the v parametric direction, at the point of parameters (U, V) of this Bezier surface. Note: The parameters U and V can be outside the bounds of the surface. Exceptions Standard_RangeError if: - Nu + Nv is less than 1, or Nu or Nv is negative.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExchangeUV(self) -> None: 
        """
        Exchanges the direction U and V on a Bezier surface As a consequence: - the poles and weights tables are transposed, - degrees, rational characteristics and so on are exchanged between the two parametric directions, and - the orientation of the surface is reversed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Increase(self,UDeg : int,VDeg : int) -> None: 
        """
        Increases the degree of this Bezier surface in the two parametric directions.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def InsertPoleColAfter(self,VIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Inserts a column of poles. If the surface is rational the weights values associated with CPoles are equal defaulted to 1.

        Inserts a column of poles and weights. If the surface was non-rational it can become rational.
        """
    @overload
    def InsertPoleColAfter(self,VIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def InsertPoleColBefore(self,VIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        Inserts a column of poles. If the surface is rational the weights values associated with CPoles are equal defaulted to 1.

        Inserts a column of poles and weights. If the surface was non-rational it can become rational.
        """
    @overload
    def InsertPoleColBefore(self,VIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def InsertPoleRowAfter(self,UIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        Inserts a row of poles. If the surface is rational the weights values associated with CPoles are equal defaulted to 1.

        Inserts a row of poles and weights. If the surface was non-rational it can become rational.
        """
    @overload
    def InsertPoleRowAfter(self,UIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def InsertPoleRowBefore(self,UIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Inserts a row of poles. If the surface is rational the weights values associated with CPoles are equal defaulted to 1.

        Inserts a row of poles and weights. If the surface was non-rational it can become rational.
        """
    @overload
    def InsertPoleRowBefore(self,UIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    def IsCNu(self,N : int) -> bool: 
        """
        Returns True, a Bezier surface is always CN
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns True, a BezierSurface is always CN
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
    def IsUClosed(self) -> bool: 
        """
        Returns True if the first control points row and the last control points row are identical. The tolerance criterion is Resolution from package gp.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns False.
        """
    def IsURational(self) -> bool: 
        """
        Returns False if the weights are identical in the U direction, The tolerance criterion is Resolution from package gp. Example : |1.0, 1.0, 1.0| if Weights = |0.5, 0.5, 0.5| returns False |2.0, 2.0, 2.0|
        """
    def IsVClosed(self) -> bool: 
        """
        Returns True if the first control points column and the last control points column are identical. The tolerance criterion is Resolution from package gp.
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns False.
        """
    def IsVRational(self) -> bool: 
        """
        Returns False if the weights are identical in the V direction, The tolerance criterion is Resolution from package gp. Example : |1.0, 2.0, 0.5| if Weights = |1.0, 2.0, 0.5| returns False |1.0, 2.0, 0.5|
        """
    @staticmethod
    def MaxDegree_s() -> int: 
        """
        Returns the value of the maximum polynomial degree of a Bezier surface. This value is 25.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def NbUPoles(self) -> int: 
        """
        Returns the number of poles in the U direction.
        """
    def NbVPoles(self) -> int: 
        """
        Returns the number of poles in the V direction.
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Pole(self,UIndex : int,VIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the pole of range UIndex, VIndex Raised if UIndex < 1 or UIndex > NbUPoles, or VIndex < 1 or VIndex > NbVPoles.
        """
    @overload
    def Poles(self,P : OCP.TColgp.TColgp_Array2OfPnt) -> None: 
        """
        Returns the poles of the Bezier surface.

        Returns the poles of the Bezier surface.
        """
    @overload
    def Poles(self) -> OCP.TColgp.TColgp_Array2OfPnt: ...
    def RemovePoleCol(self,VIndex : int) -> None: 
        """
        Removes a column of poles. If the surface was rational it can become non-rational.
        """
    def RemovePoleRow(self,UIndex : int) -> None: 
        """
        Removes a row of poles. If the surface was rational it can become non-rational.
        """
    def Resolution(self,Tolerance3D : float) -> Tuple[float, float]: 
        """
        Computes two tolerance values for this Bezier surface, based on the given tolerance in 3D space Tolerance3D. The tolerances computed are: - UTolerance in the u parametric direction, and - VTolerance in the v parametric direction. If f(u,v) is the equation of this Bezier surface, UTolerance and VTolerance guarantee that: | u1 - u0 | < UTolerance and | v1 - v0 | < VTolerance ====> |f (u1,v1) - f (u0,v0)| < Tolerance3D
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def Segment(self,U1 : float,U2 : float,V1 : float,V2 : float) -> None: 
        """
        Modifies this Bezier surface by segmenting it between U1 and U2 in the u parametric direction, and between V1 and V2 in the v parametric direction. U1, U2, V1, and V2 can be outside the bounds of this surface. - U1 and U2 isoparametric Bezier curves, segmented between V1 and V2, become the two bounds of the surface in the v parametric direction (0. and 1. u isoparametric curves). - V1 and V2 isoparametric Bezier curves, segmented between U1 and U2, become the two bounds of the surface in the u parametric direction (0. and 1. v isoparametric curves). The poles and weights tables are modified, but the degree of this surface in the u and v parametric directions does not change. U1 can be greater than U2, and V1 can be greater than V2. In these cases, the corresponding parametric direction is inverted. The orientation of the surface is inverted if one (and only one) parametric direction is inverted.
        """
    @overload
    def SetPole(self,UIndex : int,VIndex : int,P : OCP.gp.gp_Pnt,Weight : float) -> None: 
        """
        Modifies a pole value. If the surface is rational the weight of range (UIndex, VIndex) is not modified.

        Substitutes the pole and the weight of range UIndex, VIndex. If the surface <me> is not rational it can become rational. if the surface was rational it can become non-rational.
        """
    @overload
    def SetPole(self,UIndex : int,VIndex : int,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def SetPoleCol(self,VIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Modifies a column of poles. The length of CPoles can be lower but not greater than NbUPoles so you can modify just a part of the column. Raised if VIndex < 1 or VIndex > NbVPoles

        Modifies a column of poles. If the surface was rational it can become non-rational If the surface was non-rational it can become rational. The length of CPoles can be lower but not greater than NbUPoles so you can modify just a part of the column. Raised if VIndex < 1 or VIndex > NbVPoles
        """
    @overload
    def SetPoleCol(self,VIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def SetPoleRow(self,UIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Modifies a row of poles. The length of CPoles can be lower but not greater than NbVPoles so you can modify just a part of the row. Raised if UIndex < 1 or UIndex > NbUPoles

        Modifies a row of poles and weights. If the surface was rational it can become non-rational. If the surface was non-rational it can become rational. The length of CPoles can be lower but not greater than NbVPoles so you can modify just a part of the row. Raised if UIndex < 1 or UIndex > NbUPoles
        """
    @overload
    def SetPoleRow(self,UIndex : int,CPoles : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    def SetWeight(self,UIndex : int,VIndex : int,Weight : float) -> None: 
        """
        Modifies the weight of the pole of range UIndex, VIndex. If the surface was non-rational it can become rational. If the surface was rational it can become non-rational.
        """
    def SetWeightCol(self,VIndex : int,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Modifies a column of weights. If the surface was rational it can become non-rational. If the surface was non-rational it can become rational. The length of CPoleWeights can be lower but not greater than NbUPoles. Raised if VIndex < 1 or VIndex > NbVPoles
        """
    def SetWeightRow(self,UIndex : int,CPoleWeights : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Modifies a row of weights. If the surface was rational it can become non-rational. If the surface was non-rational it can become rational. The length of CPoleWeights can be lower but not greater than NbVPoles. Raised if UIndex < 1 or UIndex > NbUPoles
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this Bezier surface.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UDegree(self) -> int: 
        """
        Returns the degree of the surface in the U direction it is NbUPoles - 1
        """
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve. For a Bezier surface the UIso curve is a Bezier curve.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Changes the orientation of this Bezier surface in the u parametric direction. The bounds of the surface are not changed, but the given parametric direction is reversed. Hence, the orientation of the surface is reversed.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Computes the u (or v) parameter on the modified surface, produced by reversing its u (or v) parametric direction, for any point of u parameter U (or of v parameter V) on this Bezier surface. In the case of a Bezier surface, these functions return respectively: - 1.-U, or 1.-V.
        """
    def VDegree(self) -> int: 
        """
        Returns the degree of the surface in the V direction it is NbVPoles - 1
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve. For a Bezier surface the VIso curve is a Bezier curve.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Changes the orientation of this Bezier surface in the v parametric direction. The bounds of the surface are not changed, but the given parametric direction is reversed. Hence, the orientation of the surface is reversed.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Computes the u (or v) parameter on the modified surface, produced by reversing its u (or v) parametric direction, for any point of u parameter U (or of v parameter V) on this Bezier surface. In the case of a Bezier surface, these functions return respectively: - 1.-U, or 1.-V.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    def Weight(self,UIndex : int,VIndex : int) -> float: 
        """
        Returns the weight of range UIndex, VIndex
        """
    @overload
    def Weights(self) -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        Returns the weights of the Bezier surface.

        Returns the weights of the Bezier surface.
        """
    @overload
    def Weights(self,W : OCP.TColStd.TColStd_Array2OfReal) -> None: ...
    @overload
    def __init__(self,SurfacePoles : OCP.TColgp.TColgp_Array2OfPnt) -> None: ...
    @overload
    def __init__(self,SurfacePoles : OCP.TColgp.TColgp_Array2OfPnt,PoleWeights : OCP.TColStd.TColStd_Array2OfReal) -> None: ...
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
class Geom_SweptSurface(Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes the common behavior for surfaces constructed by sweeping a curve with another curve. The Geom package provides two concrete derived surfaces: surface of revolution (a revolved surface), and surface of linear extrusion (an extruded surface).Describes the common behavior for surfaces constructed by sweeping a curve with another curve. The Geom package provides two concrete derived surfaces: surface of revolution (a revolved surface), and surface of linear extrusion (an extruded surface).Describes the common behavior for surfaces constructed by sweeping a curve with another curve. The Geom package provides two concrete derived surfaces: surface of revolution (a revolved surface), and surface of linear extrusion (an extruded surface).
    """
    def BasisCurve(self) -> Geom_Curve: 
        """
        Returns the referenced curve of the surface. For a surface of revolution it is the revolution curve, for a surface of linear extrusion it is the extruded curve.
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this surface. If the surface is infinite, this function can return a value equal to Precision::Infinite: instead of Standard_Real::LastReal.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        returns the continuity of the surface : C0 : only geometric continuity, C1 : continuity of the first derivative all along the surface, C2 : continuity of the second derivative all along the surface, C3 : continuity of the third derivative all along the surface, G1 : tangency continuity all along the surface, G2 : curvature continuity all along the surface, CN : the order of continuity is infinite.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U,V on the surface.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P and the first derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first and the second derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first,the second and the third derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        ---Purpose ; Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns the reference direction of the swept surface. For a surface of revolution it is the direction of the revolution axis, for a surface of linear extrusion it is the direction of extrusion.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns the order of continuity of the surface in the U parametric direction. Raised if N < 0.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns the order of continuity of the surface in the V parametric direction. Raised if N < 0.
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
    def IsUClosed(self) -> bool: 
        """
        Checks whether this surface is closed in the u parametric direction. Returns true if, in the u parametric direction: taking uFirst and uLast as the parametric bounds in the u parametric direction, for each parameter v, the distance between the points P(uFirst, v) and P(uLast, v) is less than or equal to gp::Resolution().
        """
    def IsUPeriodic(self) -> bool: 
        """
        Checks if this surface is periodic in the u parametric direction. Returns true if: - this surface is closed in the u parametric direction, and - there is a constant T such that the distance between the points P (u, v) and P (u + T, v) (or the points P (u, v) and P (u, v + T)) is less than or equal to gp::Resolution(). Note: T is the parametric period in the u parametric direction.
        """
    def IsVClosed(self) -> bool: 
        """
        Checks whether this surface is closed in the u parametric direction. Returns true if, in the v parametric direction: taking vFirst and vLast as the parametric bounds in the v parametric direction, for each parameter u, the distance between the points P(u, vFirst) and P(u, vLast) is less than or equal to gp::Resolution().
        """
    def IsVPeriodic(self) -> bool: 
        """
        Checks if this surface is periodic in the v parametric direction. Returns true if: - this surface is closed in the v parametric direction, and - there is a constant T such that the distance between the points P (u, v) and P (u + T, v) (or the points P (u, v) and P (u, v + T)) is less than or equal to gp::Resolution(). Note: T is the parametric period in the v parametric direction.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Returns the parameter on the Ureversed surface for the point of parameter U on <me>.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Returns the parameter on the Vreversed surface for the point of parameter V on <me>.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
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
class Geom_SurfaceOfRevolution(Geom_SweptSurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a surface of revolution (revolved surface). Such a surface is obtained by rotating a curve (called the "meridian") through a complete revolution about an axis (referred to as the "axis of revolution"). The curve and the axis must be in the same plane (the "reference plane" of the surface). Rotation around the axis of revolution in the trigonometric sense defines the u parametric direction. So the u parameter is an angle, and its origin is given by the position of the meridian on the surface. The parametric range for the u parameter is: [ 0, 2.*Pi ] The v parameter is that of the meridian. Note: A surface of revolution is built from a copy of the original meridian. As a result the original meridian is not modified when the surface is modified. The form of a surface of revolution is typically a general revolution surface (GeomAbs_RevolutionForm). It can be: - a conical surface, if the meridian is a line or a trimmed line (GeomAbs_ConicalForm), - a cylindrical surface, if the meridian is a line or a trimmed line parallel to the axis of revolution (GeomAbs_CylindricalForm), - a planar surface if the meridian is a line or a trimmed line perpendicular to the axis of revolution of the surface (GeomAbs_PlanarForm), - a toroidal surface, if the meridian is a circle or a trimmed circle (GeomAbs_ToroidalForm), or - a spherical surface, if the meridian is a circle, the center of which is located on the axis of the revolved surface (GeomAbs_SphericalForm). Warning Be careful not to construct a surface of revolution where the curve and the axis or revolution are not defined in the same plane. If you do not have a correct configuration, you can correct your initial curve, using a cylindrical projection in the reference plane.Describes a surface of revolution (revolved surface). Such a surface is obtained by rotating a curve (called the "meridian") through a complete revolution about an axis (referred to as the "axis of revolution"). The curve and the axis must be in the same plane (the "reference plane" of the surface). Rotation around the axis of revolution in the trigonometric sense defines the u parametric direction. So the u parameter is an angle, and its origin is given by the position of the meridian on the surface. The parametric range for the u parameter is: [ 0, 2.*Pi ] The v parameter is that of the meridian. Note: A surface of revolution is built from a copy of the original meridian. As a result the original meridian is not modified when the surface is modified. The form of a surface of revolution is typically a general revolution surface (GeomAbs_RevolutionForm). It can be: - a conical surface, if the meridian is a line or a trimmed line (GeomAbs_ConicalForm), - a cylindrical surface, if the meridian is a line or a trimmed line parallel to the axis of revolution (GeomAbs_CylindricalForm), - a planar surface if the meridian is a line or a trimmed line perpendicular to the axis of revolution of the surface (GeomAbs_PlanarForm), - a toroidal surface, if the meridian is a circle or a trimmed circle (GeomAbs_ToroidalForm), or - a spherical surface, if the meridian is a circle, the center of which is located on the axis of the revolved surface (GeomAbs_SphericalForm). Warning Be careful not to construct a surface of revolution where the curve and the axis or revolution are not defined in the same plane. If you do not have a correct configuration, you can correct your initial curve, using a cylindrical projection in the reference plane.Describes a surface of revolution (revolved surface). Such a surface is obtained by rotating a curve (called the "meridian") through a complete revolution about an axis (referred to as the "axis of revolution"). The curve and the axis must be in the same plane (the "reference plane" of the surface). Rotation around the axis of revolution in the trigonometric sense defines the u parametric direction. So the u parameter is an angle, and its origin is given by the position of the meridian on the surface. The parametric range for the u parameter is: [ 0, 2.*Pi ] The v parameter is that of the meridian. Note: A surface of revolution is built from a copy of the original meridian. As a result the original meridian is not modified when the surface is modified. The form of a surface of revolution is typically a general revolution surface (GeomAbs_RevolutionForm). It can be: - a conical surface, if the meridian is a line or a trimmed line (GeomAbs_ConicalForm), - a cylindrical surface, if the meridian is a line or a trimmed line parallel to the axis of revolution (GeomAbs_CylindricalForm), - a planar surface if the meridian is a line or a trimmed line perpendicular to the axis of revolution of the surface (GeomAbs_PlanarForm), - a toroidal surface, if the meridian is a circle or a trimmed circle (GeomAbs_ToroidalForm), or - a spherical surface, if the meridian is a circle, the center of which is located on the axis of the revolved surface (GeomAbs_SphericalForm). Warning Be careful not to construct a surface of revolution where the curve and the axis or revolution are not defined in the same plane. If you do not have a correct configuration, you can correct your initial curve, using a cylindrical projection in the reference plane.
    """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the revolution axis of the surface.
        """
    def BasisCurve(self) -> Geom_Curve: 
        """
        Returns the referenced curve of the surface. For a surface of revolution it is the revolution curve, for a surface of linear extrusion it is the extruded curve.
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2 , V1 and V2 of this surface. A surface of revolution is always complete, so U1 = 0, U2 = 2*PI.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        returns the continuity of the surface : C0 : only geometric continuity, C1 : continuity of the first derivative all along the surface, C2 : continuity of the second derivative all along the surface, C3 : continuity of the third derivative all along the surface, G1 : tangency continuity all along the surface, G2 : curvature continuity all along the surface, CN : the order of continuity is infinite.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this surface of revolution.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point P (U, V) on the surface. U is the angle of the rotation around the revolution axis. The direction of this axis gives the sense of rotation. V is the parameter of the revolved curve.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point and the first derivatives in the directions U and V. Raised if the continuity of the surface is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first and the second derivatives in the directions U and V. Raised if the continuity of the surface is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first,the second and the third derivatives in the directions U and V. Raised if the continuity of the surface is not C3.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction u and Nv in the direction v.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns the reference direction of the swept surface. For a surface of revolution it is the direction of the revolution axis, for a surface of linear extrusion it is the direction of extrusion.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        IsCNu always returns true.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        IsCNv returns true if the degree of continuity of the meridian of this surface of revolution is at least N. Raised if N < 0.
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
    def IsUClosed(self) -> bool: 
        """
        IsUClosed always returns true.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns True.
        """
    def IsVClosed(self) -> bool: 
        """
        IsVClosed returns true if the meridian of this surface of revolution is closed.
        """
    def IsVPeriodic(self) -> bool: 
        """
        IsVPeriodic returns true if the meridian of this surface of revolution is periodic.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the axis of revolution.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def ReferencePlane(self) -> OCP.gp.gp_Ax2: 
        """
        Computes the position of the reference plane of the surface defined by the basis curve and the symmetry axis. The location point is the location point of the revolution's axis, the XDirection of the plane is given by the revolution's axis and the orientation of the normal to the plane is given by the sense of revolution.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the axis of revolution. Warnings : It is not checked that the axis is in the plane of the revolved curve.
        """
    def SetBasisCurve(self,C : Geom_Curve) -> None: 
        """
        Changes the revolved curve of the surface. Warnings : It is not checked that the curve C is planar and that the surface axis is in the plane of the curve. It is not checked that the revolved curve C doesn't self-intersects.
        """
    def SetDirection(self,V : OCP.gp.gp_Dir) -> None: 
        """
        Changes the direction of the revolution axis. Warnings : It is not checked that the axis is in the plane of the revolved curve.
        """
    def SetLocation(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Changes the location point of the revolution axis. Warnings : It is not checked that the axis is in the plane of the revolved curve.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this surface of revolution.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve of this surface of revolution. It is the curve obtained by rotating the meridian through an angle U about the axis of revolution.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Changes the orientation of this surface of revolution in the u parametric direction. The bounds of the surface are not changed but the given parametric direction is reversed. Hence the orientation of the surface is reversed. As a consequence: - UReverse reverses the direction of the axis of revolution of this surface,
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Computes the u parameter on the modified surface, when reversing its u parametric direction, for any point of u parameter U on this surface of revolution. In the case of a revolved surface: - UReversedParameter returns 2.*Pi - U
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve of this surface of revolution. It is the curve obtained by rotating the meridian through an angle U about the axis of revolution.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Changes the orientation of this surface of revolution in the v parametric direction. The bounds of the surface are not changed but the given parametric direction is reversed. Hence the orientation of the surface is reversed. As a consequence: - VReverse reverses the meridian of this surface of revolution.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Computes the v parameter on the modified surface, when reversing its v parametric direction, for any point of v parameter V on this surface of revolution. In the case of a revolved surface: - VReversedParameter returns the reversed parameter given by the function ReversedParameter called with V on the meridian.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    def __init__(self,C : Geom_Curve,A1 : OCP.gp.gp_Ax1) -> None: ...
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
class Geom_SurfaceOfLinearExtrusion(Geom_SweptSurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a surface of linear extrusion ("extruded surface"), e.g. a generalized cylinder. Such a surface is obtained by sweeping a curve (called the "extruded curve" or "basis") in a given direction (referred to as the "direction of extrusion" and defined by a unit vector). The u parameter is along the extruded curve. The v parameter is along the direction of extrusion. The parameter range for the u parameter is defined by the reference curve. The parameter range for the v parameter is ] - infinity, + infinity [. The position of the curve gives the origin of the v parameter. The surface is "CN" in the v parametric direction. The form of a surface of linear extrusion is generally a ruled surface (GeomAbs_RuledForm). It can be: - a cylindrical surface, if the extruded curve is a circle, or a trimmed circle, with an axis parallel to the direction of extrusion (GeomAbs_CylindricalForm), or - a planar surface, if the extruded curve is a line (GeomAbs_PlanarForm). Note: The surface of extrusion is built from a copy of the original basis curve, so the original curve is not modified when the surface is modified. Warning Degenerate surfaces are not detected. A degenerate surface is obtained, for example, when the extruded curve is a line and the direction of extrusion is parallel to that line.Describes a surface of linear extrusion ("extruded surface"), e.g. a generalized cylinder. Such a surface is obtained by sweeping a curve (called the "extruded curve" or "basis") in a given direction (referred to as the "direction of extrusion" and defined by a unit vector). The u parameter is along the extruded curve. The v parameter is along the direction of extrusion. The parameter range for the u parameter is defined by the reference curve. The parameter range for the v parameter is ] - infinity, + infinity [. The position of the curve gives the origin of the v parameter. The surface is "CN" in the v parametric direction. The form of a surface of linear extrusion is generally a ruled surface (GeomAbs_RuledForm). It can be: - a cylindrical surface, if the extruded curve is a circle, or a trimmed circle, with an axis parallel to the direction of extrusion (GeomAbs_CylindricalForm), or - a planar surface, if the extruded curve is a line (GeomAbs_PlanarForm). Note: The surface of extrusion is built from a copy of the original basis curve, so the original curve is not modified when the surface is modified. Warning Degenerate surfaces are not detected. A degenerate surface is obtained, for example, when the extruded curve is a line and the direction of extrusion is parallel to that line.Describes a surface of linear extrusion ("extruded surface"), e.g. a generalized cylinder. Such a surface is obtained by sweeping a curve (called the "extruded curve" or "basis") in a given direction (referred to as the "direction of extrusion" and defined by a unit vector). The u parameter is along the extruded curve. The v parameter is along the direction of extrusion. The parameter range for the u parameter is defined by the reference curve. The parameter range for the v parameter is ] - infinity, + infinity [. The position of the curve gives the origin of the v parameter. The surface is "CN" in the v parametric direction. The form of a surface of linear extrusion is generally a ruled surface (GeomAbs_RuledForm). It can be: - a cylindrical surface, if the extruded curve is a circle, or a trimmed circle, with an axis parallel to the direction of extrusion (GeomAbs_CylindricalForm), or - a planar surface, if the extruded curve is a line (GeomAbs_PlanarForm). Note: The surface of extrusion is built from a copy of the original basis curve, so the original curve is not modified when the surface is modified. Warning Degenerate surfaces are not detected. A degenerate surface is obtained, for example, when the extruded curve is a line and the direction of extrusion is parallel to that line.
    """
    def BasisCurve(self) -> Geom_Curve: 
        """
        Returns the referenced curve of the surface. For a surface of revolution it is the revolution curve, for a surface of linear extrusion it is the extruded curve.
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this surface of linear extrusion. A surface of linear extrusion is infinite in the v parametric direction, so: - V1 = Standard_Real::RealFirst() - V2 = Standard_Real::RealLast().
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        returns the continuity of the surface : C0 : only geometric continuity, C1 : continuity of the first derivative all along the surface, C2 : continuity of the second derivative all along the surface, C3 : continuity of the third derivative all along the surface, G1 : tangency continuity all along the surface, G2 : curvature continuity all along the surface, CN : the order of continuity is infinite.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this surface of linear extrusion.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point P (U, V) on the surface. The parameter U is the parameter on the extruded curve. The parametrization V is a linear parametrization, and the direction of parametrization is the direction of extrusion. If the point is on the extruded curve, V = 0.0
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point and the first derivatives in the directions U and V. Raises UndefinedDerivative if the continuity of the surface is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        --- Purpose ; Computes the current point, the first and the second derivatives in the directions U and V. Raises UndefinedDerivative if the continuity of the surface is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first,the second and the third derivatives in the directions U and V. Raises UndefinedDerivative if the continuity of the surface is not C3.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction u and Nv in the direction v. Raises UndefinedDerivative if the continuity of the surface is not CNu in the u direction and CNv in the v direction. Raises RangeError if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns the reference direction of the swept surface. For a surface of revolution it is the direction of the revolution axis, for a surface of linear extrusion it is the direction of extrusion.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        IsCNu returns true if the degree of continuity for the "basis curve" of this surface of linear extrusion is at least N. Raises RangeError if N < 0.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        IsCNv always returns true.
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
    def IsUClosed(self) -> bool: 
        """
        IsUClosed returns true if the "basis curve" of this surface of linear extrusion is closed.
        """
    def IsUPeriodic(self) -> bool: 
        """
        IsUPeriodic returns true if the "basis curve" of this surface of linear extrusion is periodic.
        """
    def IsVClosed(self) -> bool: 
        """
        IsVClosed always returns false.
        """
    def IsVPeriodic(self) -> bool: 
        """
        IsVPeriodic always returns false.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetBasisCurve(self,C : Geom_Curve) -> None: 
        """
        Modifies this surface of linear extrusion by redefining its "basis curve" (the "extruded curve").
        """
    def SetDirection(self,V : OCP.gp.gp_Dir) -> None: 
        """
        Assigns V as the "direction of extrusion" for this surface of linear extrusion.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this surface of linear extrusion.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve of this surface of linear extrusion. This is the line parallel to the direction of extrusion, passing through the point of parameter U of the basis curve.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Changes the orientation of this surface of linear extrusion in the u parametric direction. The bounds of the surface are not changed, but the given parametric direction is reversed. Hence the orientation of the surface is reversed. In the case of a surface of linear extrusion: - UReverse reverses the basis curve, and - VReverse reverses the direction of linear extrusion.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Computes the u parameter on the modified surface, produced by reversing its u parametric direction, for any point of u parameter U on this surface of linear extrusion. In the case of an extruded surface: - UReverseParameter returns the reversed parameter given by the function ReversedParameter called with U on the basis curve,
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve of this surface of linear extrusion. This curve is obtained by translating the extruded curve in the direction of extrusion, with the magnitude V.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Changes the orientation of this surface of linear extrusion in the v parametric direction. The bounds of the surface are not changed, but the given parametric direction is reversed. Hence the orientation of the surface is reversed. In the case of a surface of linear extrusion: - UReverse reverses the basis curve, and - VReverse reverses the direction of linear extrusion.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Computes the v parameter on the modified surface, produced by reversing its u v parametric direction, for any point of v parameter V on this surface of linear extrusion. In the case of an extruded surface VReverse returns -V.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    def __init__(self,C : Geom_Curve,V : OCP.gp.gp_Dir) -> None: ...
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
class Geom_ToroidalSurface(Geom_ElementarySurface, Geom_Surface, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a torus. A torus is defined by its major and minor radii, and positioned in space with a coordinate system (a gp_Ax3 object) as follows: - The origin is the center of the torus. - The surface is obtained by rotating a circle around the "main Direction". This circle has a radius equal to the minor radius, and is located in the plane defined by the origin, "X Direction" and "main Direction". It is centered on the "X Axis", on its positive side, and positioned at a distance from the origin equal to the major radius. This circle is the "reference circle" of the torus. - The plane defined by the origin, the "X Direction" and the "Y Direction" is called the "reference plane" of the torus. This coordinate system is the "local coordinate system" of the torus. The following apply: - Rotation around its "main Axis", in the trigonometric sense given by "X Direction" and "Y Direction", defines the u parametric direction. - The "X Axis" gives the origin for the u parameter. - Rotation around an axis parallel to the "Y Axis" and passing through the center of the "reference circle" gives the v parameter on the "reference circle". - The "X Axis" gives the origin of the v parameter on the "reference circle". - The v parametric direction is oriented by the inverse of the "main Direction", i.e. near 0, as v increases, the Z coordinate decreases. (This implies that the "Y Direction" orients the reference circle only when the local coordinate system is direct.) - The u isoparametric curve is a circle obtained by rotating the "reference circle" of the torus through an angle u about the "main Axis". The parametric equation of the torus is : P(u, v) = O + (R + r*cos(v)) * (cos(u)*XDir + sin(u)*YDir ) + r*sin(v)*ZDir, where: - O, XDir, YDir and ZDir are respectively the origin, the "X Direction", the "Y Direction" and the "Z Direction" of the local coordinate system, - r and R are, respectively, the minor and major radius. The parametric range of the two parameters is: - [ 0, 2.*Pi ] for u - [ 0, 2.*Pi ] for vDescribes a torus. A torus is defined by its major and minor radii, and positioned in space with a coordinate system (a gp_Ax3 object) as follows: - The origin is the center of the torus. - The surface is obtained by rotating a circle around the "main Direction". This circle has a radius equal to the minor radius, and is located in the plane defined by the origin, "X Direction" and "main Direction". It is centered on the "X Axis", on its positive side, and positioned at a distance from the origin equal to the major radius. This circle is the "reference circle" of the torus. - The plane defined by the origin, the "X Direction" and the "Y Direction" is called the "reference plane" of the torus. This coordinate system is the "local coordinate system" of the torus. The following apply: - Rotation around its "main Axis", in the trigonometric sense given by "X Direction" and "Y Direction", defines the u parametric direction. - The "X Axis" gives the origin for the u parameter. - Rotation around an axis parallel to the "Y Axis" and passing through the center of the "reference circle" gives the v parameter on the "reference circle". - The "X Axis" gives the origin of the v parameter on the "reference circle". - The v parametric direction is oriented by the inverse of the "main Direction", i.e. near 0, as v increases, the Z coordinate decreases. (This implies that the "Y Direction" orients the reference circle only when the local coordinate system is direct.) - The u isoparametric curve is a circle obtained by rotating the "reference circle" of the torus through an angle u about the "main Axis". The parametric equation of the torus is : P(u, v) = O + (R + r*cos(v)) * (cos(u)*XDir + sin(u)*YDir ) + r*sin(v)*ZDir, where: - O, XDir, YDir and ZDir are respectively the origin, the "X Direction", the "Y Direction" and the "Z Direction" of the local coordinate system, - r and R are, respectively, the minor and major radius. The parametric range of the two parameters is: - [ 0, 2.*Pi ] for u - [ 0, 2.*Pi ] for vDescribes a torus. A torus is defined by its major and minor radii, and positioned in space with a coordinate system (a gp_Ax3 object) as follows: - The origin is the center of the torus. - The surface is obtained by rotating a circle around the "main Direction". This circle has a radius equal to the minor radius, and is located in the plane defined by the origin, "X Direction" and "main Direction". It is centered on the "X Axis", on its positive side, and positioned at a distance from the origin equal to the major radius. This circle is the "reference circle" of the torus. - The plane defined by the origin, the "X Direction" and the "Y Direction" is called the "reference plane" of the torus. This coordinate system is the "local coordinate system" of the torus. The following apply: - Rotation around its "main Axis", in the trigonometric sense given by "X Direction" and "Y Direction", defines the u parametric direction. - The "X Axis" gives the origin for the u parameter. - Rotation around an axis parallel to the "Y Axis" and passing through the center of the "reference circle" gives the v parameter on the "reference circle". - The "X Axis" gives the origin of the v parameter on the "reference circle". - The v parametric direction is oriented by the inverse of the "main Direction", i.e. near 0, as v increases, the Z coordinate decreases. (This implies that the "Y Direction" orients the reference circle only when the local coordinate system is direct.) - The u isoparametric curve is a circle obtained by rotating the "reference circle" of the torus through an angle u about the "main Axis". The parametric equation of the torus is : P(u, v) = O + (R + r*cos(v)) * (cos(u)*XDir + sin(u)*YDir ) + r*sin(v)*ZDir, where: - O, XDir, YDir and ZDir are respectively the origin, the "X Direction", the "Y Direction" and the "Z Direction" of the local coordinate system, - r and R are, respectively, the minor and major radius. The parametric range of the two parameters is: - [ 0, 2.*Pi ] for u - [ 0, 2.*Pi ] for v
    """
    def Area(self) -> float: 
        """
        Computes the aera of the surface.
        """
    def Axis(self) -> OCP.gp.gp_Ax1: 
        """
        Returns the main axis of the surface (ZAxis).
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds U1, U2, V1 and V2 of this torus. For a torus: U1 = V1 = 0 and U2 = V2 = 2*PI .
        """
    def Coefficients(self,Coef : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Returns the coefficients of the implicit equation of the surface in the absolute cartesian coordinate system : Coef(1) * X**4 + Coef(2) * Y**4 + Coef(3) * Z**4 + Coef(4) * X**3 * Y + Coef(5) * X**3 * Z + Coef(6) * Y**3 * X + Coef(7) * Y**3 * Z + Coef(8) * Z**3 * X + Coef(9) * Z**3 * Y + Coef(10) * X**2 * Y**2 + Coef(11) * X**2 * Z**2 + Coef(12) * Y**2 * Z**2 + Coef(13) * X**3 + Coef(14) * Y**3 + Coef(15) * Z**3 + Coef(16) * X**2 * Y + Coef(17) * X**2 * Z + Coef(18) * Y**2 * X + Coef(19) * Y**2 * Z + Coef(20) * Z**2 * X + Coef(21) * Z**2 * Y + Coef(22) * X**2 + Coef(23) * Y**2 + Coef(24) * Z**2 + Coef(25) * X * Y + Coef(26) * X * Z + Coef(27) * Y * Z + Coef(28) * X + Coef(29) * Y + Coef(30) * Z + Coef(31) = 0.0 Raised if the length of Coef is lower than 31.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_CN, the global continuity of any elementary surface.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this torus.
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point P (U, V) on the surface. P (U, V) = Loc + MinorRadius * Sin (V) * Zdir + (MajorRadius + MinorRadius * Cos(V)) * (cos (U) * XDir + sin (U) * YDir) where Loc is the origin of the placement plane (XAxis, YAxis) XDir is the direction of the XAxis and YDir the direction of the YAxis and ZDir the direction of the ZAxis.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point and the first derivatives in the directions U and V.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first and the second derivatives in the directions U and V.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the current point, the first,the second and the third derivatives in the directions U and V.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction u and Nv in the direction v. Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns True.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns True.
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
    def IsUClosed(self) -> bool: 
        """
        Returns True.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns True.
        """
    def IsVClosed(self) -> bool: 
        """
        Returns True.
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns True.
        """
    def Location(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location point of the local coordinate system of the surface.
        """
    def MajorRadius(self) -> float: 
        """
        Returns the major radius, or the minor radius, of this torus.
        """
    def MinorRadius(self) -> float: 
        """
        Returns the major radius, or the minor radius, of this torus.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def Position(self) -> OCP.gp.gp_Ax3: 
        """
        Returns the local coordinates system of the surface.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetAxis(self,theA1 : OCP.gp.gp_Ax1) -> None: 
        """
        Changes the main axis (ZAxis) of the elementary surface.
        """
    def SetLocation(self,theLoc : OCP.gp.gp_Pnt) -> None: 
        """
        Changes the location of the local coordinates system of the surface.
        """
    def SetMajorRadius(self,MajorRadius : float) -> None: 
        """
        Modifies this torus by changing its major radius. Exceptions Standard_ConstructionError if: - MajorRadius is negative, or - MajorRadius - r is less than or equal to gp::Resolution(), where r is the minor radius of this torus.
        """
    def SetMinorRadius(self,MinorRadius : float) -> None: 
        """
        Modifies this torus by changing its minor radius. Exceptions Standard_ConstructionError if: - MinorRadius is negative, or - R - MinorRadius is less than or equal to gp::Resolution(), where R is the major radius of this torus.
        """
    def SetPosition(self,theAx3 : OCP.gp.gp_Ax3) -> None: 
        """
        Changes the local coordinates system of the surface.
        """
    def SetTorus(self,T : OCP.gp.gp_Torus) -> None: 
        """
        Converts the gp_Torus torus T into this torus.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Torus(self) -> OCP.gp.gp_Torus: 
        """
        Returns the non transient torus with the same geometric properties as <me>.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this torus.
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def UIso(self,U : float) -> Geom_Curve: 
        """
        Computes the U isoparametric curve.
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Reverses the U parametric direction of the surface.
        """
    def UReversed(self) -> Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Return the parameter on the Ureversed surface for the point of parameter U on <me>. Return 2.PI - U.
        """
    def VIso(self,V : float) -> Geom_Curve: 
        """
        Computes the V isoparametric curve.
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V parametric direction of the surface.
        """
    def VReversed(self) -> Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,U : float) -> float: 
        """
        Return the parameter on the Ureversed surface for the point of parameter U on <me>. Return 2.PI - U.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    def Volume(self) -> float: 
        """
        Computes the volume.
        """
    @overload
    def __init__(self,T : OCP.gp.gp_Torus) -> None: ...
    @overload
    def __init__(self,A3 : OCP.gp.gp_Ax3,MajorRadius : float,MinorRadius : float) -> None: ...
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
class Geom_Transformation(OCP.Standard.Standard_Transient):
    """
    Describes how to construct the following elementary transformations - translations, - rotations, - symmetries, - scales. The Transformation class can also be used to construct complex transformations by combining these elementary transformations. However, these transformations can never change the type of an object. For example, the projection transformation can change a circle into an ellipse, and therefore change the real type of the object. Such a transformation is forbidden in this environment and cannot be a Geom_Transformation. The transformation can be represented as follow :Describes how to construct the following elementary transformations - translations, - rotations, - symmetries, - scales. The Transformation class can also be used to construct complex transformations by combining these elementary transformations. However, these transformations can never change the type of an object. For example, the projection transformation can change a circle into an ellipse, and therefore change the real type of the object. Such a transformation is forbidden in this environment and cannot be a Geom_Transformation. The transformation can be represented as follow :
    """
    def Copy(self) -> Geom_Transformation: 
        """
        Creates a new object which is a copy of this transformation.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Form(self) -> OCP.gp.gp_TrsfForm: 
        """
        Returns the nature of this transformation as a value of the gp_TrsfForm enumeration.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Invert(self) -> None: 
        """
        Raised if the the transformation is singular. This means that the ScaleFactor is lower or equal to Resolution from package gp.
        """
    def Inverted(self) -> Geom_Transformation: 
        """
        Raised if the the transformation is singular. This means that the ScaleFactor is lower or equal to Resolution from package gp.
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
    def IsNegative(self) -> bool: 
        """
        Checks whether this transformation is an indirect transformation: returns true if the determinant of the matrix of the vectorial part of the transformation is less than 0.
        """
    def Multiplied(self,Other : Geom_Transformation) -> Geom_Transformation: 
        """
        Computes the transformation composed with Other and <me>. <me> * Other. Returns a new transformation
        """
    def Multiply(self,theOther : Geom_Transformation) -> None: 
        """
        Computes the transformation composed with Other and <me> . <me> = <me> * Other.
        """
    def Power(self,N : int) -> None: 
        """
        Computes the following composition of transformations if N > 0 <me> * <me> * .......* <me>. if N = 0 Identity if N < 0 <me>.Invert() * .........* <me>.Invert()
        """
    def Powered(self,N : int) -> Geom_Transformation: 
        """
        Raised if N < 0 and if the transformation is not inversible
        """
    def PreMultiply(self,Other : Geom_Transformation) -> None: 
        """
        Computes the matrix of the transformation composed with <me> and Other. <me> = Other * <me>
        """
    def ScaleFactor(self) -> float: 
        """
        Returns the scale value of the transformation.
        """
    @overload
    def SetMirror(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Makes the transformation into a symmetrical transformation with respect to a point P. P is the center of the symmetry.

        Makes the transformation into a symmetrical transformation with respect to an axis A1. A1 is the center of the axial symmetry.

        Makes the transformation into a symmetrical transformation with respect to a plane. The plane of the symmetry is defined with the axis placement A2. It is the plane (Location, XDirection, YDirection).
        """
    @overload
    def SetMirror(self,theA2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def SetMirror(self,theA1 : OCP.gp.gp_Ax1) -> None: ...
    def SetRotation(self,theA1 : OCP.gp.gp_Ax1,theAng : float) -> None: 
        """
        Makes the transformation into a rotation. A1 is the axis rotation and Ang is the angular value of the rotation in radians.
        """
    def SetScale(self,thePnt : OCP.gp.gp_Pnt,theScale : float) -> None: 
        """
        Makes the transformation into a scale. P is the center of the scale and S is the scaling value.
        """
    @overload
    def SetTransformation(self,theToSystem : OCP.gp.gp_Ax3) -> None: 
        """
        Makes a transformation allowing passage from the coordinate system "FromSystem1" to the coordinate system "ToSystem2". Example : In a C++ implementation : Real x1, y1, z1; // are the coordinates of a point in the // local system FromSystem1 Real x2, y2, z2; // are the coordinates of a point in the // local system ToSystem2 gp_Pnt P1 (x1, y1, z1) Geom_Transformation T; T.SetTransformation (FromSystem1, ToSystem2); gp_Pnt P2 = P1.Transformed (T); P2.Coord (x2, y2, z2);

        Makes the transformation allowing passage from the basic coordinate system {P(0.,0.,0.), VX (1.,0.,0.), VY (0.,1.,0.), VZ (0., 0. ,1.) } to the local coordinate system defined with the Ax2 ToSystem. Same utilisation as the previous method. FromSystem1 is defaulted to the absolute coordinate system.
        """
    @overload
    def SetTransformation(self,theFromSystem1 : OCP.gp.gp_Ax3,theToSystem2 : OCP.gp.gp_Ax3) -> None: ...
    @overload
    def SetTranslation(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Makes the transformation into a translation. V is the vector of the translation.

        Makes the transformation into a translation from the point P1 to the point P2.
        """
    @overload
    def SetTranslation(self,theVec : OCP.gp.gp_Vec) -> None: ...
    def SetTrsf(self,theTrsf : OCP.gp.gp_Trsf) -> None: 
        """
        Converts the gp_Trsf transformation T into this transformation.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transforms(self) -> Tuple[float, float, float]: 
        """
        Applies the transformation <me> to the triplet {X, Y, Z}.
        """
    def Trsf(self) -> OCP.gp.gp_Trsf: 
        """
        Returns a non transient copy of <me>.
        """
    def Value(self,theRow : int,theCol : int) -> float: 
        """
        Returns the coefficients of the global matrix of transformation. It is a 3 rows X 4 columns matrix.
        """
    @overload
    def __init__(self,T : OCP.gp.gp_Trsf) -> None: ...
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
class Geom_TrimmedCurve(Geom_BoundedCurve, Geom_Curve, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes a portion of a curve (termed the "basis curve") limited by two parameter values inside the parametric domain of the basis curve. The trimmed curve is defined by: - the basis curve, and - the two parameter values which limit it. The trimmed curve can either have the same orientation as the basis curve or the opposite orientation.Describes a portion of a curve (termed the "basis curve") limited by two parameter values inside the parametric domain of the basis curve. The trimmed curve is defined by: - the basis curve, and - the two parameter values which limit it. The trimmed curve can either have the same orientation as the basis curve or the opposite orientation.Describes a portion of a curve (termed the "basis curve") limited by two parameter values inside the parametric domain of the basis curve. The trimmed curve is defined by: - the basis curve, and - the two parameter values which limit it. The trimmed curve can either have the same orientation as the basis curve or the opposite orientation.
    """
    def BasisCurve(self) -> Geom_Curve: 
        """
        Returns the basis curve. Warning This function does not return a constant reference. Consequently, any modification of the returned value directly modifies the trimmed curve.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of the curve : C0 : only geometric continuity, C1 : continuity of the first derivative all along the Curve, C2 : continuity of the second derivative all along the Curve, C3 : continuity of the third derivative all along the Curve, CN : the order of continuity is infinite.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this trimmed curve.
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in P the point of parameter U.
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the curve is not C1.
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the curve is not C2.
        """
    def D3(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Raised if the continuity of the curve is not C3.
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
        """
        N is the order of derivation. Raised if the continuity of the curve is not CN. Raised if N < 1. geometric transformations
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the end point of <me>. This point is the evaluation of the curve for the "LastParameter".
        """
    def FirstParameter(self) -> float: 
        """
        Returns the value of the first parameter of <me>. The first parameter is the parameter of the "StartPoint" of the trimmed curve.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns true if the degree of continuity of the basis curve of this trimmed curve is at least N. A trimmed curve is at least "C0" continuous. Warnings : The continuity of the trimmed curve can be greater than the continuity of the basis curve because you consider only a part of the basis curve. Raised if N < 0.
        """
    def IsClosed(self) -> bool: 
        """
        Returns True if the distance between the StartPoint and the EndPoint is lower or equal to Resolution from package gp.
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
    def IsPeriodic(self) -> bool: 
        """
        Always returns FALSE (independently of the type of basis curve).
        """
    def LastParameter(self) -> float: 
        """
        Returns the value of the last parameter of <me>. The last parameter is the parameter of the "EndPoint" of the trimmed curve.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns a coefficient to compute the parameter on the transformed curve for the transform of the point on <me>.
        """
    def Period(self) -> float: 
        """
        Returns the period of the basis curve of this trimmed curve. Exceptions Standard_NoSuchObject if the basis curve is not periodic.
        """
    def Reverse(self) -> None: 
        """
        Changes the orientation of this trimmed curve. As a result: - the basis curve is reversed, - the start point of the initial curve becomes the end point of the reversed curve, - the end point of the initial curve becomes the start point of the reversed curve, - the first and last parameters are recomputed. If the trimmed curve was defined by: - a basis curve whose parameter range is [ 0., 1. ], - the two trim values U1 (first parameter) and U2 (last parameter), the reversed trimmed curve is defined by: - the reversed basis curve, whose parameter range is still [ 0., 1. ], - the two trim values 1. - U2 (first parameter) and 1. - U1 (last parameter).
        """
    def Reversed(self) -> Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Computes the parameter on the reversed curve for the point of parameter U on this trimmed curve.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetTrim(self,U1 : float,U2 : float,Sense : bool=True,theAdjustPeriodic : bool=True) -> None: 
        """
        Changes this trimmed curve, by redefining the parameter values U1 and U2 which limit its basis curve. Note: If the basis curve is periodic, the trimmed curve has the same orientation as the basis curve if Sense is true (default value) or the opposite orientation if Sense is false. Warning If the basis curve is periodic and theAdjustPeriodic is True, the bounds of the trimmed curve may be different from U1 and U2 if the parametric origin of the basis curve is within the arc of the trimmed curve. In this case, the modified parameter will be equal to U1 or U2 plus or minus the period. When theAdjustPeriodic is False, parameters U1 and U2 will be the same, without adjustment into the first period. Exceptions Standard_ConstructionError if: - the basis curve is not periodic, and either U1 or U2 are outside the bounds of the basis curve, or - U1 is equal to U2.
        """
    def StartPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the start point of <me>. This point is the evaluation of the curve from the "FirstParameter". value and derivatives Warnings : The returned derivatives have the same orientation as the derivatives of the basis curve even if the trimmed curve has not the same orientation as the basis curve.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this trimmed curve. Warning The basis curve is also modified.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on <me>. If the curve is periodic then the returned point is P(U) with U = Ustart + (U - Uend) where Ustart and Uend are the parametric bounds of the curve. it is implemented with D0.
        """
    def __init__(self,C : Geom_Curve,U1 : float,U2 : float,Sense : bool=True,theAdjustPeriodic : bool=True) -> None: ...
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
class Geom_UndefinedDerivative(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Geom', '__weakref__': <attribute '__weakref__' of 'Geom_UndefinedDerivative' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Geom_UndefinedDerivative' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Geom_UndefinedValue(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Geom', '__weakref__': <attribute '__weakref__' of 'Geom_UndefinedValue' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Geom_UndefinedValue' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Geom_Direction(Geom_Vector, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    The class Direction specifies a vector that is never null. It is a unit vector.The class Direction specifies a vector that is never null. It is a unit vector.The class Direction specifies a vector that is never null. It is a unit vector.
    """
    def Angle(self,Other : Geom_Vector) -> float: 
        """
        Computes the angular value, in radians, between this vector and vector Other. The result is a value between 0 and Pi. Exceptions gp_VectorWithNullMagnitude if: - the magnitude of this vector is less than or equal to gp::Resolution(), or - the magnitude of vector Other is less than or equal to gp::Resolution().
        """
    def AngleWithRef(self,Other : Geom_Vector,VRef : Geom_Vector) -> float: 
        """
        Computes the angular value, in radians, between this vector and vector Other. The result is a value between -Pi and Pi. The vector VRef defines the positive sense of rotation: the angular value is positive if the cross product this ^ Other has the same orientation as VRef (in relation to the plane defined by this vector and vector Other). Otherwise, it is negative. Exceptions Standard_DomainError if this vector, vector Other and vector VRef are coplanar, except if this vector and vector Other are parallel. gp_VectorWithNullMagnitude if the magnitude of this vector, vector Other or vector VRef is less than or equal to gp::Resolution().
        """
    def Coord(self) -> Tuple[float, float, float]: 
        """
        Returns the coordinates X, Y and Z of this vector.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this unit vector.
        """
    def Cross(self,Other : Geom_Vector) -> None: 
        """
        Computes the cross product between <me> and <Other>.
        """
    def CrossCross(self,V1 : Geom_Vector,V2 : Geom_Vector) -> None: 
        """
        Computes the triple vector product <me> ^(V1 ^ V2).
        """
    def CrossCrossed(self,V1 : Geom_Vector,V2 : Geom_Vector) -> Geom_Vector: 
        """
        Computes the triple vector product <me> ^(V1 ^ V2).
        """
    def Crossed(self,Other : Geom_Vector) -> Geom_Vector: 
        """
        Computes the cross product between <me> and <Other>. A new direction is returned.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dir(self) -> OCP.gp.gp_Dir: 
        """
        Returns the non transient direction with the same coordinates as <me>.
        """
    def Dot(self,Other : Geom_Vector) -> float: 
        """
        Computes the scalar product of this vector and vector Other.
        """
    def DotCross(self,V1 : Geom_Vector,V2 : Geom_Vector) -> float: 
        """
        Computes the triple scalar product. Returns me . (V1 ^ V2)
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def Magnitude(self) -> float: 
        """
        returns 1.0 which is the magnitude of any unit vector.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Reverse(self) -> None: 
        """
        Reverses the vector <me>.
        """
    def Reversed(self) -> Geom_Vector: 
        """
        Returns a copy of <me> reversed.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetCoord(self,X : float,Y : float,Z : float) -> None: 
        """
        Sets <me> to X,Y,Z coordinates.
        """
    def SetDir(self,V : OCP.gp.gp_Dir) -> None: 
        """
        Converts the gp_Dir unit vector V into this unit vector.
        """
    def SetX(self,X : float) -> None: 
        """
        Changes the X coordinate of <me>.
        """
    def SetY(self,Y : float) -> None: 
        """
        Changes the Y coordinate of <me>.
        """
    def SetZ(self,Z : float) -> None: 
        """
        Changes the Z coordinate of <me>.
        """
    def SquareMagnitude(self) -> float: 
        """
        returns 1.0 which is the square magnitude of any unit vector.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this unit vector, then normalizes it.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Vec(self) -> OCP.gp.gp_Vec: 
        """
        Converts this vector into a gp_Vec vector.
        """
    def X(self) -> float: 
        """
        Returns the X coordinate of <me>.
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate of <me>.
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate of <me>.
        """
    @overload
    def __init__(self,X : float,Y : float,Z : float) -> None: ...
    @overload
    def __init__(self,V : OCP.gp.gp_Dir) -> None: ...
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
class Geom_VectorWithMagnitude(Geom_Vector, Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Defines a vector with magnitude. A vector with magnitude can have a zero length.Defines a vector with magnitude. A vector with magnitude can have a zero length.Defines a vector with magnitude. A vector with magnitude can have a zero length.
    """
    def Add(self,Other : Geom_Vector) -> None: 
        """
        Adds the Vector Other to <me>.
        """
    def Added(self,Other : Geom_Vector) -> Geom_VectorWithMagnitude: 
        """
        Adds the vector Other to <me>.
        """
    def Angle(self,Other : Geom_Vector) -> float: 
        """
        Computes the angular value, in radians, between this vector and vector Other. The result is a value between 0 and Pi. Exceptions gp_VectorWithNullMagnitude if: - the magnitude of this vector is less than or equal to gp::Resolution(), or - the magnitude of vector Other is less than or equal to gp::Resolution().
        """
    def AngleWithRef(self,Other : Geom_Vector,VRef : Geom_Vector) -> float: 
        """
        Computes the angular value, in radians, between this vector and vector Other. The result is a value between -Pi and Pi. The vector VRef defines the positive sense of rotation: the angular value is positive if the cross product this ^ Other has the same orientation as VRef (in relation to the plane defined by this vector and vector Other). Otherwise, it is negative. Exceptions Standard_DomainError if this vector, vector Other and vector VRef are coplanar, except if this vector and vector Other are parallel. gp_VectorWithNullMagnitude if the magnitude of this vector, vector Other or vector VRef is less than or equal to gp::Resolution().
        """
    def Coord(self) -> Tuple[float, float, float]: 
        """
        Returns the coordinates X, Y and Z of this vector.
        """
    def Copy(self) -> Geom_Geometry: 
        """
        Creates a new object which is a copy of this vector.
        """
    def Cross(self,Other : Geom_Vector) -> None: 
        """
        Computes the cross product between <me> and Other <me> ^ Other.
        """
    def CrossCross(self,V1 : Geom_Vector,V2 : Geom_Vector) -> None: 
        """
        Computes the triple vector product <me> ^ (V1 ^ V2).
        """
    def CrossCrossed(self,V1 : Geom_Vector,V2 : Geom_Vector) -> Geom_Vector: 
        """
        Computes the triple vector product <me> ^ (V1 ^ V2). A new vector is returned.
        """
    def Crossed(self,Other : Geom_Vector) -> Geom_Vector: 
        """
        Computes the cross product between <me> and Other <me> ^ Other. A new vector is returned.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Divide(self,Scalar : float) -> None: 
        """
        Divides <me> by a scalar.
        """
    def Divided(self,Scalar : float) -> Geom_VectorWithMagnitude: 
        """
        Divides <me> by a scalar. A new vector is returned.
        """
    def Dot(self,Other : Geom_Vector) -> float: 
        """
        Computes the scalar product of this vector and vector Other.
        """
    def DotCross(self,V1 : Geom_Vector,V2 : Geom_Vector) -> float: 
        """
        Computes the triple scalar product. Returns me . (V1 ^ V2)
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def Magnitude(self) -> float: 
        """
        Returns the magnitude of <me>.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> Geom_Geometry: ...
    def Multiplied(self,Scalar : float) -> Geom_VectorWithMagnitude: 
        """
        Computes the product of the vector <me> by a scalar. A new vector is returned.
        """
    def Multiply(self,Scalar : float) -> None: 
        """
        Computes the product of the vector <me> by a scalar.
        """
    def Normalize(self) -> None: 
        """
        Normalizes <me>.
        """
    def Normalized(self) -> Geom_VectorWithMagnitude: 
        """
        Returns a copy of <me> Normalized.
        """
    def Reverse(self) -> None: 
        """
        Reverses the vector <me>.
        """
    def Reversed(self) -> Geom_Vector: 
        """
        Returns a copy of <me> reversed.
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> Geom_Geometry: 
        """
        None
        """
    def SetCoord(self,X : float,Y : float,Z : float) -> None: 
        """
        Assigns the values X, Y and Z to the coordinates of this vector.
        """
    def SetVec(self,V : OCP.gp.gp_Vec) -> None: 
        """
        Converts the gp_Vec vector V into this vector.
        """
    def SetX(self,X : float) -> None: 
        """
        Changes the X coordinate of <me>.
        """
    def SetY(self,Y : float) -> None: 
        """
        Changes the Y coordinate of <me>
        """
    def SetZ(self,Z : float) -> None: 
        """
        Changes the Z coordinate of <me>.
        """
    def SquareMagnitude(self) -> float: 
        """
        Returns the square magnitude of <me>.
        """
    def Subtract(self,Other : Geom_Vector) -> None: 
        """
        Subtracts the Vector Other to <me>.
        """
    def Subtracted(self,Other : Geom_Vector) -> Geom_VectorWithMagnitude: 
        """
        Subtracts the vector Other to <me>. A new vector is returned.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies the transformation T to this vector.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> Geom_Geometry: ...
    def Vec(self) -> OCP.gp.gp_Vec: 
        """
        Converts this vector into a gp_Vec vector.
        """
    def X(self) -> float: 
        """
        Returns the X coordinate of <me>.
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate of <me>.
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate of <me>.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def __init__(self,X : float,Y : float,Z : float) -> None: ...
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
