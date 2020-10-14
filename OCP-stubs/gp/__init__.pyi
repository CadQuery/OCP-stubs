import OCP.gp
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
__all__  = [
"NCollection_Lerp_gp_Trsf",
"gp",
"gp_Ax1",
"gp_Ax2",
"gp_Ax22d",
"gp_Ax2d",
"gp_Ax3",
"gp_Circ",
"gp_Circ2d",
"gp_Cone",
"gp_Cylinder",
"gp_Dir",
"gp_Dir2d",
"gp_Elips",
"gp_Elips2d",
"gp_EulerSequence",
"gp_GTrsf",
"gp_GTrsf2d",
"gp_Hypr",
"gp_Hypr2d",
"gp_Lin",
"gp_Lin2d",
"gp_Mat",
"gp_Mat2d",
"gp_Parab",
"gp_Parab2d",
"gp_Pln",
"gp_Pnt",
"gp_Pnt2d",
"gp_Quaternion",
"gp_QuaternionNLerp",
"gp_QuaternionSLerp",
"gp_Sphere",
"gp_Torus",
"gp_Trsf",
"gp_Trsf2d",
"gp_TrsfForm",
"gp_Vec",
"gp_Vec2d",
"gp_VectorWithNullMagnitude",
"gp_XY",
"gp_XYZ",
"__mul__",
"__rmul__",
"gp_Ax1Mirror",
"gp_Ax2Mirror",
"gp_CompoundTrsf",
"gp_EulerAngles",
"gp_Extrinsic_XYX",
"gp_Extrinsic_XYZ",
"gp_Extrinsic_XZX",
"gp_Extrinsic_XZY",
"gp_Extrinsic_YXY",
"gp_Extrinsic_YXZ",
"gp_Extrinsic_YZX",
"gp_Extrinsic_YZY",
"gp_Extrinsic_ZXY",
"gp_Extrinsic_ZXZ",
"gp_Extrinsic_ZYX",
"gp_Extrinsic_ZYZ",
"gp_Identity",
"gp_Intrinsic_XYX",
"gp_Intrinsic_XYZ",
"gp_Intrinsic_XZX",
"gp_Intrinsic_XZY",
"gp_Intrinsic_YXY",
"gp_Intrinsic_YXZ",
"gp_Intrinsic_YZX",
"gp_Intrinsic_YZY",
"gp_Intrinsic_ZXY",
"gp_Intrinsic_ZXZ",
"gp_Intrinsic_ZYX",
"gp_Intrinsic_ZYZ",
"gp_Other",
"gp_PntMirror",
"gp_Rotation",
"gp_Scale",
"gp_Translation",
"gp_YawPitchRoll"
]
class NCollection_Lerp_gp_Trsf():
    """
    Linear interpolation tool for transformation defined by gp_Trsf.
    """
    def Init(self,theStart : gp_Trsf,theEnd : gp_Trsf) -> None: 
        """
        Initialize values.
        """
    def Interpolate(self,theT : float,theResult : gp_Trsf) -> None: 
        """
        Compute interpolated value between two values.
        """
    @overload
    def __init__(self,theStart : gp_Trsf,theEnd : gp_Trsf) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp():
    """
    The geometric processor package, called gp, provides an implementation of entities used : . for algebraic calculation such as "XYZ" coordinates, "Mat" matrix . for basis analytic geometry such as Transformations, point, vector, line, plane, axis placement, conics, and elementary surfaces. These entities are defined in 2d and 3d space. All the classes of this package are non-persistent.
    """
    @staticmethod
    def DX2d_s() -> gp_Dir2d: 
        """
        Returns a unit vector with the combinations (1,0)
        """
    @staticmethod
    def DX_s() -> gp_Dir: 
        """
        Returns a unit vector with the combination (1,0,0)
        """
    @staticmethod
    def DY2d_s() -> gp_Dir2d: 
        """
        Returns a unit vector with the combinations (0,1)
        """
    @staticmethod
    def DY_s() -> gp_Dir: 
        """
        Returns a unit vector with the combination (0,1,0)
        """
    @staticmethod
    def DZ_s() -> gp_Dir: 
        """
        Returns a unit vector with the combination (0,0,1)
        """
    @staticmethod
    def OX2d_s() -> gp_Ax2d: 
        """
        Identifies an axis where its origin is Origin2d and its unit vector coordinates are: X = 1.0, Y = 0.0
        """
    @staticmethod
    def OX_s() -> gp_Ax1: 
        """
        Identifies an axis where its origin is Origin and its unit vector coordinates X = 1.0, Y = Z = 0.0
        """
    @staticmethod
    def OY2d_s() -> gp_Ax2d: 
        """
        Identifies an axis where its origin is Origin2d and its unit vector coordinates are Y = 1.0, X = 0.0
        """
    @staticmethod
    def OY_s() -> gp_Ax1: 
        """
        Identifies an axis where its origin is Origin and its unit vector coordinates Y = 1.0, X = Z = 0.0
        """
    @staticmethod
    def OZ_s() -> gp_Ax1: 
        """
        Identifies an axis where its origin is Origin and its unit vector coordinates Z = 1.0, Y = X = 0.0
        """
    @staticmethod
    def Origin2d_s() -> gp_Pnt2d: 
        """
        Identifies a Cartesian point with coordinates X = Y = 0.0
        """
    @staticmethod
    def Origin_s() -> gp_Pnt: 
        """
        Identifies a Cartesian point with coordinates X = Y = Z = 0.0.0
        """
    @staticmethod
    def Resolution_s() -> float: 
        """
        Method of package gp
        """
    @staticmethod
    def XOY_s() -> gp_Ax2: 
        """
        Identifies a coordinate system where its origin is Origin, and its "main Direction" and "X Direction" coordinates Z = 1.0, X = Y =0.0 and X direction coordinates X = 1.0, Y = Z = 0.0
        """
    @staticmethod
    def YOZ_s() -> gp_Ax2: 
        """
        Identifies a coordinate system where its origin is Origin, and its "main Direction" and "X Direction" coordinates X = 1.0, Z = Y =0.0 and X direction coordinates Y = 1.0, X = Z = 0.0 In 2D space
        """
    @staticmethod
    def ZOX_s() -> gp_Ax2: 
        """
        Identifies a coordinate system where its origin is Origin, and its "main Direction" and "X Direction" coordinates Y = 1.0, X = Z =0.0 and X direction coordinates Z = 1.0, X = Y = 0.0
        """
    def __init__(self) -> None: ...
    pass
class gp_Ax1():
    """
    Describes an axis in 3D space. An axis is defined by: - its origin (also referred to as its "Location point"), and - its unit vector (referred to as its "Direction" or "main Direction"). An axis is used: - to describe 3D geometric entities (for example, the axis of a revolution entity). It serves the same purpose as the STEP function "axis placement one axis", or - to define geometric transformations (axis of symmetry, axis of rotation, and so on). For example, this entity can be used to locate a geometric entity or to define a symmetry axis.
    """
    def Angle(self,Other : gp_Ax1) -> float: 
        """
        Computes the angular value, in radians, between <me>.Direction() and <Other>.Direction(). Returns the angle between 0 and 2*PI radians.

        Computes the angular value, in radians, between <me>.Direction() and <Other>.Direction(). Returns the angle between 0 and 2*PI radians.
        """
    def Direction(self) -> gp_Dir: 
        """
        Returns the direction of <me>.

        Returns the direction of <me>.
        """
    def IsCoaxial(self,Other : gp_Ax1,AngularTolerance : float,LinearTolerance : float) -> bool: 
        """
        Returns True if : . the angle between <me> and <Other> is lower or equal to <AngularTolerance> and . the distance between <me>.Location() and <Other> is lower or equal to <LinearTolerance> and . the distance between <Other>.Location() and <me> is lower or equal to LinearTolerance.
        """
    def IsNormal(self,Other : gp_Ax1,AngularTolerance : float) -> bool: 
        """
        Returns True if the direction of the <me> and <Other> are normal to each other. That is, if the angle between the two axes is equal to Pi/2. Note: the tolerance criterion is given by AngularTolerance..

        Returns True if the direction of the <me> and <Other> are normal to each other. That is, if the angle between the two axes is equal to Pi/2. Note: the tolerance criterion is given by AngularTolerance..
        """
    def IsOpposite(self,Other : gp_Ax1,AngularTolerance : float) -> bool: 
        """
        Returns True if the direction of <me> and <Other> are parallel with opposite orientation. That is, if the angle between the two axes is equal to Pi. Note: the tolerance criterion is given by AngularTolerance.

        Returns True if the direction of <me> and <Other> are parallel with opposite orientation. That is, if the angle between the two axes is equal to Pi. Note: the tolerance criterion is given by AngularTolerance.
        """
    def IsParallel(self,Other : gp_Ax1,AngularTolerance : float) -> bool: 
        """
        Returns True if the direction of <me> and <Other> are parallel with same orientation or opposite orientation. That is, if the angle between the two axes is equal to 0 or Pi. Note: the tolerance criterion is given by AngularTolerance.

        Returns True if the direction of <me> and <Other> are parallel with same orientation or opposite orientation. That is, if the angle between the two axes is equal to 0 or Pi. Note: the tolerance criterion is given by AngularTolerance.
        """
    def Location(self) -> gp_Pnt: 
        """
        Returns the location point of <me>.

        Returns the location point of <me>.
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of an axis placement with respect to the point P which is the center of the symmetry and assigns the result to this axis.

        Performs the symmetrical transformation of an axis placement with respect to an axis placement which is the axis of the symmetry and assigns the result to this axis.

        Performs the symmetrical transformation of an axis placement with respect to a plane. The axis placement <A2> locates the plane of the symmetry : (Location, XDirection, YDirection) and assigns the result to this axis.
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: ...
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Ax1: 
        """
        Performs the symmetrical transformation of an axis placement with respect to the point P which is the center of the symmetry and creates a new axis.

        Performs the symmetrical transformation of an axis placement with respect to an axis placement which is the axis of the symmetry and creates a new axis.

        Performs the symmetrical transformation of an axis placement with respect to a plane. The axis placement <A2> locates the plane of the symmetry : (Location, XDirection, YDirection) and creates a new axis.
        """
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Ax1: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Ax1: ...
    def Reverse(self) -> None: 
        """
        Reverses the unit vector of this axis. and assigns the result to this axis.

        Reverses the unit vector of this axis. and assigns the result to this axis.
        """
    def Reversed(self) -> gp_Ax1: 
        """
        Reverses the unit vector of this axis and creates a new one.

        Reverses the unit vector of this axis and creates a new one.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        Rotates this axis at an angle Ang (in radians) about the axis A1 and assigns the result to this axis.

        Rotates this axis at an angle Ang (in radians) about the axis A1 and assigns the result to this axis.
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Ax1: 
        """
        Rotates this axis at an angle Ang (in radians) about the axis A1 and creates a new one.

        Rotates this axis at an angle Ang (in radians) about the axis A1 and creates a new one.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        Applies a scaling transformation to this axis with: - scale factor S, and - center P and assigns the result to this axis.

        Applies a scaling transformation to this axis with: - scale factor S, and - center P and assigns the result to this axis.
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Ax1: 
        """
        Applies a scaling transformation to this axis with: - scale factor S, and - center P and creates a new axis.

        Applies a scaling transformation to this axis with: - scale factor S, and - center P and creates a new axis.
        """
    def SetDirection(self,V : gp_Dir) -> None: 
        """
        Assigns V as the "Direction" of this axis.

        Assigns V as the "Direction" of this axis.
        """
    def SetLocation(self,P : gp_Pnt) -> None: 
        """
        Assigns P as the origin of this axis.

        Assigns P as the origin of this axis.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        Applies the transformation T to this axis. and assigns the result to this axis.

        Applies the transformation T to this axis. and assigns the result to this axis.
        """
    def Transformed(self,T : gp_Trsf) -> gp_Ax1: 
        """
        Applies the transformation T to this axis and creates a new one.

        Applies the transformation T to this axis and creates a new one.
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: 
        """
        Translates this axis by the vector V, and assigns the result to this axis.

        Translates this axis by: the vector (P1, P2) defined from point P1 to point P2. and assigns the result to this axis.

        Translates this axis by the vector V, and assigns the result to this axis.

        Translates this axis by: the vector (P1, P2) defined from point P1 to point P2. and assigns the result to this axis.
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Ax1: 
        """
        Translates this axis by the vector V, and creates a new one.

        Translates this axis by: the vector (P1, P2) defined from point P1 to point P2. and creates a new one.

        Translates this axis by the vector V, and creates a new one.

        Translates this axis by: the vector (P1, P2) defined from point P1 to point P2. and creates a new one.
        """
    @overload
    def Translated(self,V : gp_Vec) -> gp_Ax1: ...
    @overload
    def __init__(self,P : gp_Pnt,V : gp_Dir) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Ax2():
    """
    Describes a right-handed coordinate system in 3D space. A coordinate system is defined by: - its origin (also referred to as its "Location point"), and - three orthogonal unit vectors, termed respectively the "X Direction", the "Y Direction" and the "Direction" (also referred to as the "main Direction"). The "Direction" of the coordinate system is called its "main Direction" because whenever this unit vector is modified, the "X Direction" and the "Y Direction" are recomputed. However, when we modify either the "X Direction" or the "Y Direction", "Direction" is not modified. The "main Direction" is also the "Z Direction". Since an Ax2 coordinate system is right-handed, its "main Direction" is always equal to the cross product of its "X Direction" and "Y Direction". (To define a left-handed coordinate system, use gp_Ax3.) A coordinate system is used: - to describe geometric entities, in particular to position them. The local coordinate system of a geometric entity serves the same purpose as the STEP function "axis placement two axes", or - to define geometric transformations. Note: we refer to the "X Axis", "Y Axis" and "Z Axis", respectively, as to axes having: - the origin of the coordinate system as their origin, and - the unit vectors "X Direction", "Y Direction" and "main Direction", respectively, as their unit vectors. The "Z Axis" is also the "main Axis".
    """
    def Angle(self,Other : gp_Ax2) -> float: 
        """
        Computes the angular value, in radians, between the main direction of <me> and the main direction of <Other>. Returns the angle between 0 and PI in radians.

        Computes the angular value, in radians, between the main direction of <me> and the main direction of <Other>. Returns the angle between 0 and PI in radians.
        """
    def Axis(self) -> gp_Ax1: 
        """
        Returns the main axis of <me>. It is the "Location" point and the main "Direction".

        Returns the main axis of <me>. It is the "Location" point and the main "Direction".
        """
    def Direction(self) -> gp_Dir: 
        """
        Returns the main direction of <me>.

        Returns the main direction of <me>.
        """
    @overload
    def IsCoplanar(self,A : gp_Ax1,LinearTolerance : float,AngularTolerance : float) -> bool: 
        """
        None

        Returns True if . the distance between <me> and the "Location" point of A1 is lower of equal to LinearTolerance and . the main direction of <me> and the direction of A1 are normal. Note: the tolerance criterion for angular equality is given by AngularTolerance.

        None

        Returns True if . the distance between <me> and the "Location" point of A1 is lower of equal to LinearTolerance and . the main direction of <me> and the direction of A1 are normal. Note: the tolerance criterion for angular equality is given by AngularTolerance.
        """
    @overload
    def IsCoplanar(self,Other : gp_Ax2,LinearTolerance : float,AngularTolerance : float) -> bool: ...
    @overload
    def IsCoplanar(self,A1 : gp_Ax1,LinearTolerance : float,AngularTolerance : float) -> bool: ...
    def Location(self) -> gp_Pnt: 
        """
        Returns the "Location" point (origin) of <me>.

        Returns the "Location" point (origin) of <me>.
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: 
        """
        Performs a symmetrical transformation of this coordinate system with respect to: - the point P, and assigns the result to this coordinate system. Warning This transformation is always performed on the origin. In case of a reflection with respect to a point: - the main direction of the coordinate system is not changed, and - the "X Direction" and the "Y Direction" are simply reversed In case of a reflection with respect to an axis or a plane: - the transformation is applied to the "X Direction" and the "Y Direction", then - the "main Direction" is recomputed as the cross product "X Direction" ^ "Y Direction". This maintains the right-handed property of the coordinate system.

        Performs a symmetrical transformation of this coordinate system with respect to: - the axis A1, and assigns the result to this coordinate systeme. Warning This transformation is always performed on the origin. In case of a reflection with respect to a point: - the main direction of the coordinate system is not changed, and - the "X Direction" and the "Y Direction" are simply reversed In case of a reflection with respect to an axis or a plane: - the transformation is applied to the "X Direction" and the "Y Direction", then - the "main Direction" is recomputed as the cross product "X Direction" ^ "Y Direction". This maintains the right-handed property of the coordinate system.

        Performs a symmetrical transformation of this coordinate system with respect to: - the plane defined by the origin, "X Direction" and "Y Direction" of coordinate system A2 and assigns the result to this coordinate systeme. Warning This transformation is always performed on the origin. In case of a reflection with respect to a point: - the main direction of the coordinate system is not changed, and - the "X Direction" and the "Y Direction" are simply reversed In case of a reflection with respect to an axis or a plane: - the transformation is applied to the "X Direction" and the "Y Direction", then - the "main Direction" is recomputed as the cross product "X Direction" ^ "Y Direction". This maintains the right-handed property of the coordinate system.
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: ...
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Ax2: 
        """
        Performs a symmetrical transformation of this coordinate system with respect to: - the point P, and creates a new one. Warning This transformation is always performed on the origin. In case of a reflection with respect to a point: - the main direction of the coordinate system is not changed, and - the "X Direction" and the "Y Direction" are simply reversed In case of a reflection with respect to an axis or a plane: - the transformation is applied to the "X Direction" and the "Y Direction", then - the "main Direction" is recomputed as the cross product "X Direction" ^ "Y Direction". This maintains the right-handed property of the coordinate system.

        Performs a symmetrical transformation of this coordinate system with respect to: - the axis A1, and creates a new one. Warning This transformation is always performed on the origin. In case of a reflection with respect to a point: - the main direction of the coordinate system is not changed, and - the "X Direction" and the "Y Direction" are simply reversed In case of a reflection with respect to an axis or a plane: - the transformation is applied to the "X Direction" and the "Y Direction", then - the "main Direction" is recomputed as the cross product "X Direction" ^ "Y Direction". This maintains the right-handed property of the coordinate system.

        Performs a symmetrical transformation of this coordinate system with respect to: - the plane defined by the origin, "X Direction" and "Y Direction" of coordinate system A2 and creates a new one. Warning This transformation is always performed on the origin. In case of a reflection with respect to a point: - the main direction of the coordinate system is not changed, and - the "X Direction" and the "Y Direction" are simply reversed In case of a reflection with respect to an axis or a plane: - the transformation is applied to the "X Direction" and the "Y Direction", then - the "main Direction" is recomputed as the cross product "X Direction" ^ "Y Direction". This maintains the right-handed property of the coordinate system.
        """
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Ax2: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Ax2: ...
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Ax2: 
        """
        Rotates an axis placement. <A1> is the axis of the rotation . Ang is the angular value of the rotation in radians.

        Rotates an axis placement. <A1> is the axis of the rotation . Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Ax2: 
        """
        Applies a scaling transformation on the axis placement. The "Location" point of the axisplacement is modified. Warnings : If the scale <S> is negative : . the main direction of the axis placement is not changed. . The "XDirection" and the "YDirection" are reversed. So the axis placement stay right handed.

        Applies a scaling transformation on the axis placement. The "Location" point of the axisplacement is modified. Warnings : If the scale <S> is negative : . the main direction of the axis placement is not changed. . The "XDirection" and the "YDirection" are reversed. So the axis placement stay right handed.
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Assigns the origin and "main Direction" of the axis A1 to this coordinate system, then recomputes its "X Direction" and "Y Direction". Note: The new "X Direction" is computed as follows: new "X Direction" = V1 ^(previous "X Direction" ^ V) where V is the "Direction" of A1. Exceptions Standard_ConstructionError if A1 is parallel to the "X Direction" of this coordinate system.

        Assigns the origin and "main Direction" of the axis A1 to this coordinate system, then recomputes its "X Direction" and "Y Direction". Note: The new "X Direction" is computed as follows: new "X Direction" = V1 ^(previous "X Direction" ^ V) where V is the "Direction" of A1. Exceptions Standard_ConstructionError if A1 is parallel to the "X Direction" of this coordinate system.
        """
    def SetDirection(self,V : gp_Dir) -> None: 
        """
        Changes the "main Direction" of this coordinate system, then recomputes its "X Direction" and "Y Direction". Note: the new "X Direction" is computed as follows: new "X Direction" = V ^ (previous "X Direction" ^ V) Exceptions Standard_ConstructionError if V is parallel to the "X Direction" of this coordinate system.

        Changes the "main Direction" of this coordinate system, then recomputes its "X Direction" and "Y Direction". Note: the new "X Direction" is computed as follows: new "X Direction" = V ^ (previous "X Direction" ^ V) Exceptions Standard_ConstructionError if V is parallel to the "X Direction" of this coordinate system.
        """
    def SetLocation(self,P : gp_Pnt) -> None: 
        """
        Changes the "Location" point (origin) of <me>.

        Changes the "Location" point (origin) of <me>.
        """
    def SetXDirection(self,Vx : gp_Dir) -> None: 
        """
        Changes the "Xdirection" of <me>. The main direction "Direction" is not modified, the "Ydirection" is modified. If <Vx> is not normal to the main direction then <XDirection> is computed as follows XDirection = Direction ^ (Vx ^ Direction). Exceptions Standard_ConstructionError if Vx or Vy is parallel to the "main Direction" of this coordinate system.

        Changes the "Xdirection" of <me>. The main direction "Direction" is not modified, the "Ydirection" is modified. If <Vx> is not normal to the main direction then <XDirection> is computed as follows XDirection = Direction ^ (Vx ^ Direction). Exceptions Standard_ConstructionError if Vx or Vy is parallel to the "main Direction" of this coordinate system.
        """
    def SetYDirection(self,Vy : gp_Dir) -> None: 
        """
        Changes the "Ydirection" of <me>. The main direction is not modified but the "Xdirection" is changed. If <Vy> is not normal to the main direction then "YDirection" is computed as follows YDirection = Direction ^ (<Vy> ^ Direction). Exceptions Standard_ConstructionError if Vx or Vy is parallel to the "main Direction" of this coordinate system.

        Changes the "Ydirection" of <me>. The main direction is not modified but the "Xdirection" is changed. If <Vy> is not normal to the main direction then "YDirection" is computed as follows YDirection = Direction ^ (<Vy> ^ Direction). Exceptions Standard_ConstructionError if Vx or Vy is parallel to the "main Direction" of this coordinate system.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Ax2: 
        """
        Transforms an axis placement with a Trsf. The "Location" point, the "XDirection" and the "YDirection" are transformed with T. The resulting main "Direction" of <me> is the cross product between the "XDirection" and the "YDirection" after transformation.

        Transforms an axis placement with a Trsf. The "Location" point, the "XDirection" and the "YDirection" are transformed with T. The resulting main "Direction" of <me> is the cross product between the "XDirection" and the "YDirection" after transformation.
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Ax2: 
        """
        Translates an axis plaxement in the direction of the vector <V>. The magnitude of the translation is the vector's magnitude.

        Translates an axis placement from the point <P1> to the point <P2>.

        Translates an axis plaxement in the direction of the vector <V>. The magnitude of the translation is the vector's magnitude.

        Translates an axis placement from the point <P1> to the point <P2>.
        """
    @overload
    def Translated(self,V : gp_Vec) -> gp_Ax2: ...
    def XDirection(self) -> gp_Dir: 
        """
        Returns the "XDirection" of <me>.

        Returns the "XDirection" of <me>.
        """
    def YDirection(self) -> gp_Dir: 
        """
        Returns the "YDirection" of <me>.

        Returns the "YDirection" of <me>.
        """
    @overload
    def __init__(self,P : gp_Pnt,V : gp_Dir) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : gp_Pnt,N : gp_Dir,Vx : gp_Dir) -> None: ...
    pass
class gp_Ax22d():
    """
    Describes a coordinate system in a plane (2D space). A coordinate system is defined by: - its origin (also referred to as its "Location point"), and - two orthogonal unit vectors, respectively, called the "X Direction" and the "Y Direction". A gp_Ax22d may be right-handed ("direct sense") or left-handed ("inverse" or "indirect sense"). You use a gp_Ax22d to: - describe 2D geometric entities, in particular to position them. The local coordinate system of a geometric entity serves for the same purpose as the STEP function "axis placement two axes", or - define geometric transformations. Note: we refer to the "X Axis" and "Y Axis" as the axes having: - the origin of the coordinate system as their origin, and - the unit vectors "X Direction" and "Y Direction", respectively, as their unit vectors.
    """
    def Location(self) -> gp_Pnt2d: 
        """
        Returns the "Location" point (origin) of <me>.

        Returns the "Location" point (origin) of <me>.
        """
    @overload
    def Mirror(self,P : gp_Pnt2d) -> None: 
        """
        None

        None
        """
    @overload
    def Mirror(self,A : gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,A : gp_Ax2d) -> gp_Ax22d: 
        """
        Performs the symmetrical transformation of an axis placement with respect to the point P which is the center of the symmetry. Warnings : The main direction of the axis placement is not changed. The "XDirection" and the "YDirection" are reversed. So the axis placement stay right handed.

        Performs the symmetrical transformation of an axis placement with respect to an axis placement which is the axis of the symmetry. The transformation is performed on the "Location" point, on the "XDirection" and "YDirection". The resulting main "Direction" is the cross product between the "XDirection" and the "YDirection" after transformation.
        """
    @overload
    def Mirrored(self,P : gp_Pnt2d) -> gp_Ax22d: ...
    def Rotate(self,P : gp_Pnt2d,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,P : gp_Pnt2d,Ang : float) -> gp_Ax22d: 
        """
        Rotates an axis placement. <A1> is the axis of the rotation . Ang is the angular value of the rotation in radians.

        Rotates an axis placement. <A1> is the axis of the rotation . Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt2d,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt2d,S : float) -> gp_Ax22d: 
        """
        Applies a scaling transformation on the axis placement. The "Location" point of the axisplacement is modified. Warnings : If the scale <S> is negative : . the main direction of the axis placement is not changed. . The "XDirection" and the "YDirection" are reversed. So the axis placement stay right handed.

        Applies a scaling transformation on the axis placement. The "Location" point of the axisplacement is modified. Warnings : If the scale <S> is negative : . the main direction of the axis placement is not changed. . The "XDirection" and the "YDirection" are reversed. So the axis placement stay right handed.
        """
    def SetAxis(self,A1 : gp_Ax22d) -> None: 
        """
        Assigns the origin and the two unit vectors of the coordinate system A1 to this coordinate system.

        Assigns the origin and the two unit vectors of the coordinate system A1 to this coordinate system.
        """
    def SetLocation(self,P : gp_Pnt2d) -> None: 
        """
        Changes the "Location" point (origin) of <me>.

        Changes the "Location" point (origin) of <me>.
        """
    def SetXAxis(self,A1 : gp_Ax2d) -> None: 
        """
        Changes the XAxis and YAxis ("Location" point and "Direction") of <me>. The "YDirection" is recomputed in the same sense as before.

        Changes the XAxis and YAxis ("Location" point and "Direction") of <me>. The "YDirection" is recomputed in the same sense as before.
        """
    def SetXDirection(self,Vx : gp_Dir2d) -> None: 
        """
        Assigns Vx to the "X Direction" of this coordinate system. The other unit vector of this coordinate system is recomputed, normal to Vx , without modifying the orientation (right-handed or left-handed) of this coordinate system.

        Assigns Vx to the "X Direction" of this coordinate system. The other unit vector of this coordinate system is recomputed, normal to Vx , without modifying the orientation (right-handed or left-handed) of this coordinate system.
        """
    def SetYAxis(self,A1 : gp_Ax2d) -> None: 
        """
        Changes the XAxis and YAxis ("Location" point and "Direction") of <me>. The "XDirection" is recomputed in the same sense as before.

        Changes the XAxis and YAxis ("Location" point and "Direction") of <me>. The "XDirection" is recomputed in the same sense as before.
        """
    def SetYDirection(self,Vy : gp_Dir2d) -> None: 
        """
        Assignsr Vy to the "Y Direction" of this coordinate system. The other unit vector of this coordinate system is recomputed, normal to Vy, without modifying the orientation (right-handed or left-handed) of this coordinate system.

        Assignsr Vy to the "Y Direction" of this coordinate system. The other unit vector of this coordinate system is recomputed, normal to Vy, without modifying the orientation (right-handed or left-handed) of this coordinate system.
        """
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Ax22d: 
        """
        Transforms an axis placement with a Trsf. The "Location" point, the "XDirection" and the "YDirection" are transformed with T. The resulting main "Direction" of <me> is the cross product between the "XDirection" and the "YDirection" after transformation.

        Transforms an axis placement with a Trsf. The "Location" point, the "XDirection" and the "YDirection" are transformed with T. The resulting main "Direction" of <me> is the cross product between the "XDirection" and the "YDirection" after transformation.
        """
    @overload
    def Translate(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec2d) -> None: ...
    @overload
    def Translated(self,V : gp_Vec2d) -> gp_Ax22d: 
        """
        Translates an axis plaxement in the direction of the vector <V>. The magnitude of the translation is the vector's magnitude.

        Translates an axis placement from the point <P1> to the point <P2>.

        Translates an axis plaxement in the direction of the vector <V>. The magnitude of the translation is the vector's magnitude.

        Translates an axis placement from the point <P1> to the point <P2>.
        """
    @overload
    def Translated(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> gp_Ax22d: ...
    def XAxis(self) -> gp_Ax2d: 
        """
        Returns an axis, for which - the origin is that of this coordinate system, and - the unit vector is either the "X Direction" of this coordinate system. Note: the result is the "X Axis" of this coordinate system.

        Returns an axis, for which - the origin is that of this coordinate system, and - the unit vector is either the "X Direction" of this coordinate system. Note: the result is the "X Axis" of this coordinate system.
        """
    def XDirection(self) -> gp_Dir2d: 
        """
        Returns the "XDirection" of <me>.

        Returns the "XDirection" of <me>.
        """
    def YAxis(self) -> gp_Ax2d: 
        """
        Returns an axis, for which - the origin is that of this coordinate system, and - the unit vector is either the "Y Direction" of this coordinate system. Note: the result is the "Y Axis" of this coordinate system.

        Returns an axis, for which - the origin is that of this coordinate system, and - the unit vector is either the "Y Direction" of this coordinate system. Note: the result is the "Y Axis" of this coordinate system.
        """
    def YDirection(self) -> gp_Dir2d: 
        """
        Returns the "YDirection" of <me>.

        Returns the "YDirection" of <me>.
        """
    @overload
    def __init__(self,P : gp_Pnt2d,Vx : gp_Dir2d,Vy : gp_Dir2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : gp_Pnt2d,V : gp_Dir2d,Sense : bool=True) -> None: ...
    @overload
    def __init__(self,A : gp_Ax2d,Sense : bool=True) -> None: ...
    pass
class gp_Ax2d():
    """
    Describes an axis in the plane (2D space). An axis is defined by: - its origin (also referred to as its "Location point"), and - its unit vector (referred to as its "Direction"). An axis implicitly defines a direct, right-handed coordinate system in 2D space by: - its origin, - its "Direction" (giving the "X Direction" of the coordinate system), and - the unit vector normal to "Direction" (positive angle measured in the trigonometric sense). An axis is used: - to describe 2D geometric entities (for example, the axis which defines angular coordinates on a circle). It serves for the same purpose as the STEP function "axis placement one axis", or - to define geometric transformations (axis of symmetry, axis of rotation, and so on). Note: to define a left-handed 2D coordinate system, use gp_Ax22d.
    """
    def Angle(self,Other : gp_Ax2d) -> float: 
        """
        Computes the angle, in radians, between this axis and the axis Other. The value of the angle is between -Pi and Pi.

        Computes the angle, in radians, between this axis and the axis Other. The value of the angle is between -Pi and Pi.
        """
    def Direction(self) -> gp_Dir2d: 
        """
        Returns the direction of <me>.

        Returns the direction of <me>.
        """
    def IsCoaxial(self,Other : gp_Ax2d,AngularTolerance : float,LinearTolerance : float) -> bool: 
        """
        Returns True if : . the angle between <me> and <Other> is lower or equal to <AngularTolerance> and . the distance between <me>.Location() and <Other> is lower or equal to <LinearTolerance> and . the distance between <Other>.Location() and <me> is lower or equal to LinearTolerance.
        """
    def IsNormal(self,Other : gp_Ax2d,AngularTolerance : float) -> bool: 
        """
        Returns true if this axis and the axis Other are normal to each other. That is, if the angle between the two axes is equal to Pi/2 or -Pi/2. Note: the tolerance criterion is given by AngularTolerance.

        Returns true if this axis and the axis Other are normal to each other. That is, if the angle between the two axes is equal to Pi/2 or -Pi/2. Note: the tolerance criterion is given by AngularTolerance.
        """
    def IsOpposite(self,Other : gp_Ax2d,AngularTolerance : float) -> bool: 
        """
        Returns true if this axis and the axis Other are parallel, and have opposite orientations. That is, if the angle between the two axes is equal to Pi or -Pi. Note: the tolerance criterion is given by AngularTolerance.

        Returns true if this axis and the axis Other are parallel, and have opposite orientations. That is, if the angle between the two axes is equal to Pi or -Pi. Note: the tolerance criterion is given by AngularTolerance.
        """
    def IsParallel(self,Other : gp_Ax2d,AngularTolerance : float) -> bool: 
        """
        Returns true if this axis and the axis Other are parallel, and have either the same or opposite orientations. That is, if the angle between the two axes is equal to 0, Pi or -Pi. Note: the tolerance criterion is given by AngularTolerance.

        Returns true if this axis and the axis Other are parallel, and have either the same or opposite orientations. That is, if the angle between the two axes is equal to 0, Pi or -Pi. Note: the tolerance criterion is given by AngularTolerance.
        """
    def Location(self) -> gp_Pnt2d: 
        """
        Returns the origin of <me>.

        Returns the origin of <me>.
        """
    @overload
    def Mirror(self,A : gp_Ax2d) -> None: 
        """
        None

        None
        """
    @overload
    def Mirror(self,P : gp_Pnt2d) -> None: ...
    @overload
    def Mirrored(self,A : gp_Ax2d) -> gp_Ax2d: 
        """
        Performs the symmetrical transformation of an axis placement with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of an axis placement with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirrored(self,P : gp_Pnt2d) -> gp_Ax2d: ...
    def Reverse(self) -> None: 
        """
        Reverses the direction of <me> and assigns the result to this axis.

        Reverses the direction of <me> and assigns the result to this axis.
        """
    def Reversed(self) -> gp_Ax2d: 
        """
        Computes a new axis placement with a direction opposite to the direction of <me>.

        Computes a new axis placement with a direction opposite to the direction of <me>.
        """
    def Rotate(self,P : gp_Pnt2d,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,P : gp_Pnt2d,Ang : float) -> gp_Ax2d: 
        """
        Rotates an axis placement. <P> is the center of the rotation . Ang is the angular value of the rotation in radians.

        Rotates an axis placement. <P> is the center of the rotation . Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt2d,S : float) -> None: 
        """
        None
        """
    def Scaled(self,P : gp_Pnt2d,S : float) -> gp_Ax2d: 
        """
        Applies a scaling transformation on the axis placement. The "Location" point of the axisplacement is modified. The "Direction" is reversed if the scale is negative.

        Applies a scaling transformation on the axis placement. The "Location" point of the axisplacement is modified. The "Direction" is reversed if the scale is negative.
        """
    def SetDirection(self,V : gp_Dir2d) -> None: 
        """
        Changes the direction of <me>.

        Changes the direction of <me>.
        """
    @overload
    def SetLocation(self,Locat : gp_Pnt2d) -> None: 
        """
        Changes the "Location" point (origin) of <me>.

        Changes the "Location" point (origin) of <me>.
        """
    @overload
    def SetLocation(self,P : gp_Pnt2d) -> None: ...
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Ax2d: 
        """
        Transforms an axis placement with a Trsf.

        Transforms an axis placement with a Trsf.
        """
    @overload
    def Translate(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec2d) -> None: ...
    @overload
    def Translated(self,V : gp_Vec2d) -> gp_Ax2d: 
        """
        Translates an axis placement in the direction of the vector <V>. The magnitude of the translation is the vector's magnitude.

        Translates an axis placement from the point <P1> to the point <P2>.

        Translates an axis placement in the direction of the vector <V>. The magnitude of the translation is the vector's magnitude.

        Translates an axis placement from the point <P1> to the point <P2>.
        """
    @overload
    def Translated(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> gp_Ax2d: ...
    @overload
    def __init__(self,P : gp_Pnt2d,V : gp_Dir2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Ax3():
    """
    Describes a coordinate system in 3D space. Unlike a gp_Ax2 coordinate system, a gp_Ax3 can be right-handed ("direct sense") or left-handed ("indirect sense"). A coordinate system is defined by: - its origin (also referred to as its "Location point"), and - three orthogonal unit vectors, termed the "X Direction", the "Y Direction" and the "Direction" (also referred to as the "main Direction"). The "Direction" of the coordinate system is called its "main Direction" because whenever this unit vector is modified, the "X Direction" and the "Y Direction" are recomputed. However, when we modify either the "X Direction" or the "Y Direction", "Direction" is not modified. "Direction" is also the "Z Direction". The "main Direction" is always parallel to the cross product of its "X Direction" and "Y Direction". If the coordinate system is right-handed, it satisfies the equation: "main Direction" = "X Direction" ^ "Y Direction" and if it is left-handed, it satisfies the equation: "main Direction" = -"X Direction" ^ "Y Direction" A coordinate system is used: - to describe geometric entities, in particular to position them. The local coordinate system of a geometric entity serves the same purpose as the STEP function "axis placement three axes", or - to define geometric transformations. Note: - We refer to the "X Axis", "Y Axis" and "Z Axis", respectively, as the axes having: - the origin of the coordinate system as their origin, and - the unit vectors "X Direction", "Y Direction" and "main Direction", respectively, as their unit vectors. - The "Z Axis" is also the "main Axis". - gp_Ax2 is used to define a coordinate system that must be always right-handed.
    """
    def Angle(self,Other : gp_Ax3) -> float: 
        """
        Computes the angular value between the main direction of <me> and the main direction of <Other>. Returns the angle between 0 and PI in radians.

        Computes the angular value between the main direction of <me> and the main direction of <Other>. Returns the angle between 0 and PI in radians.
        """
    def Ax2(self) -> gp_Ax2: 
        """
        Computes a right-handed coordinate system with the same "X Direction" and "Y Direction" as those of this coordinate system, then recomputes the "main Direction". If this coordinate system is right-handed, the result returned is the same coordinate system. If this coordinate system is left-handed, the result is reversed.

        Computes a right-handed coordinate system with the same "X Direction" and "Y Direction" as those of this coordinate system, then recomputes the "main Direction". If this coordinate system is right-handed, the result returned is the same coordinate system. If this coordinate system is left-handed, the result is reversed.
        """
    def Axis(self) -> gp_Ax1: 
        """
        Returns the main axis of <me>. It is the "Location" point and the main "Direction".

        Returns the main axis of <me>. It is the "Location" point and the main "Direction".
        """
    def Direct(self) -> bool: 
        """
        Returns True if the coordinate system is right-handed. i.e. XDirection().Crossed(YDirection()).Dot(Direction()) > 0

        Returns True if the coordinate system is right-handed. i.e. XDirection().Crossed(YDirection()).Dot(Direction()) > 0
        """
    def Direction(self) -> gp_Dir: 
        """
        Returns the main direction of <me>.

        Returns the main direction of <me>.
        """
    @overload
    def IsCoplanar(self,Other : gp_Ax3,LinearTolerance : float,AngularTolerance : float) -> bool: 
        """
        Returns True if . the distance between the "Location" point of <me> and <Other> is lower or equal to LinearTolerance and . the distance between the "Location" point of <Other> and <me> is lower or equal to LinearTolerance and . the main direction of <me> and the main direction of <Other> are parallel (same or opposite orientation).

        Returns True if . the distance between <me> and the "Location" point of A1 is lower of equal to LinearTolerance and . the distance between A1 and the "Location" point of <me> is lower or equal to LinearTolerance and . the main direction of <me> and the direction of A1 are normal.

        Returns True if . the distance between the "Location" point of <me> and <Other> is lower or equal to LinearTolerance and . the distance between the "Location" point of <Other> and <me> is lower or equal to LinearTolerance and . the main direction of <me> and the main direction of <Other> are parallel (same or opposite orientation).

        Returns True if . the distance between <me> and the "Location" point of A1 is lower of equal to LinearTolerance and . the distance between A1 and the "Location" point of <me> is lower or equal to LinearTolerance and . the main direction of <me> and the direction of A1 are normal.
        """
    @overload
    def IsCoplanar(self,A1 : gp_Ax1,LinearTolerance : float,AngularTolerance : float) -> bool: ...
    def Location(self) -> gp_Pnt: 
        """
        Returns the "Location" point (origin) of <me>.

        Returns the "Location" point (origin) of <me>.
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirror(self,P : gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Ax3: 
        """
        Performs the symmetrical transformation of an axis placement with respect to the point P which is the center of the symmetry. Warnings : The main direction of the axis placement is not changed. The "XDirection" and the "YDirection" are reversed. So the axis placement stay right handed.

        Performs the symmetrical transformation of an axis placement with respect to an axis placement which is the axis of the symmetry. The transformation is performed on the "Location" point, on the "XDirection" and "YDirection". The resulting main "Direction" is the cross product between the "XDirection" and the "YDirection" after transformation.

        Performs the symmetrical transformation of an axis placement with respect to a plane. The axis placement <A2> locates the plane of the symmetry : (Location, XDirection, YDirection). The transformation is performed on the "Location" point, on the "XDirection" and "YDirection". The resulting main "Direction" is the cross product between the "XDirection" and the "YDirection" after transformation.
        """
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Ax3: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Ax3: ...
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Ax3: 
        """
        Rotates an axis placement. <A1> is the axis of the rotation . Ang is the angular value of the rotation in radians.

        Rotates an axis placement. <A1> is the axis of the rotation . Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Ax3: 
        """
        Applies a scaling transformation on the axis placement. The "Location" point of the axisplacement is modified. Warnings : If the scale <S> is negative : . the main direction of the axis placement is not changed. . The "XDirection" and the "YDirection" are reversed. So the axis placement stay right handed.

        Applies a scaling transformation on the axis placement. The "Location" point of the axisplacement is modified. Warnings : If the scale <S> is negative : . the main direction of the axis placement is not changed. . The "XDirection" and the "YDirection" are reversed. So the axis placement stay right handed.
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Assigns the origin and "main Direction" of the axis A1 to this coordinate system, then recomputes its "X Direction" and "Y Direction". Note: - The new "X Direction" is computed as follows: new "X Direction" = V1 ^(previous "X Direction" ^ V) where V is the "Direction" of A1. - The orientation of this coordinate system (right-handed or left-handed) is not modified. Raises ConstructionError if the "Direction" of <A1> and the "XDirection" of <me> are parallel (same or opposite orientation) because it is impossible to calculate the new "XDirection" and the new "YDirection".

        Assigns the origin and "main Direction" of the axis A1 to this coordinate system, then recomputes its "X Direction" and "Y Direction". Note: - The new "X Direction" is computed as follows: new "X Direction" = V1 ^(previous "X Direction" ^ V) where V is the "Direction" of A1. - The orientation of this coordinate system (right-handed or left-handed) is not modified. Raises ConstructionError if the "Direction" of <A1> and the "XDirection" of <me> are parallel (same or opposite orientation) because it is impossible to calculate the new "XDirection" and the new "YDirection".
        """
    def SetDirection(self,V : gp_Dir) -> None: 
        """
        Changes the main direction of this coordinate system, then recomputes its "X Direction" and "Y Direction". Note: - The new "X Direction" is computed as follows: new "X Direction" = V ^ (previous "X Direction" ^ V). - The orientation of this coordinate system (left- or right-handed) is not modified. Raises ConstructionError if <V< and the previous "XDirection" are parallel because it is impossible to calculate the new "XDirection" and the new "YDirection".

        Changes the main direction of this coordinate system, then recomputes its "X Direction" and "Y Direction". Note: - The new "X Direction" is computed as follows: new "X Direction" = V ^ (previous "X Direction" ^ V). - The orientation of this coordinate system (left- or right-handed) is not modified. Raises ConstructionError if <V< and the previous "XDirection" are parallel because it is impossible to calculate the new "XDirection" and the new "YDirection".
        """
    def SetLocation(self,P : gp_Pnt) -> None: 
        """
        Changes the "Location" point (origin) of <me>.

        Changes the "Location" point (origin) of <me>.
        """
    def SetXDirection(self,Vx : gp_Dir) -> None: 
        """
        Changes the "Xdirection" of <me>. The main direction "Direction" is not modified, the "Ydirection" is modified. If <Vx> is not normal to the main direction then <XDirection> is computed as follows XDirection = Direction ^ (Vx ^ Direction). Raises ConstructionError if <Vx> is parallel (same or opposite orientation) to the main direction of <me>

        Changes the "Xdirection" of <me>. The main direction "Direction" is not modified, the "Ydirection" is modified. If <Vx> is not normal to the main direction then <XDirection> is computed as follows XDirection = Direction ^ (Vx ^ Direction). Raises ConstructionError if <Vx> is parallel (same or opposite orientation) to the main direction of <me>
        """
    def SetYDirection(self,Vy : gp_Dir) -> None: 
        """
        Changes the "Ydirection" of <me>. The main direction is not modified but the "Xdirection" is changed. If <Vy> is not normal to the main direction then "YDirection" is computed as follows YDirection = Direction ^ (<Vy> ^ Direction). Raises ConstructionError if <Vy> is parallel to the main direction of <me>

        Changes the "Ydirection" of <me>. The main direction is not modified but the "Xdirection" is changed. If <Vy> is not normal to the main direction then "YDirection" is computed as follows YDirection = Direction ^ (<Vy> ^ Direction). Raises ConstructionError if <Vy> is parallel to the main direction of <me>
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Ax3: 
        """
        Transforms an axis placement with a Trsf. The "Location" point, the "XDirection" and the "YDirection" are transformed with T. The resulting main "Direction" of <me> is the cross product between the "XDirection" and the "YDirection" after transformation.

        Transforms an axis placement with a Trsf. The "Location" point, the "XDirection" and the "YDirection" are transformed with T. The resulting main "Direction" of <me> is the cross product between the "XDirection" and the "YDirection" after transformation.
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Ax3: 
        """
        Translates an axis plaxement in the direction of the vector <V>. The magnitude of the translation is the vector's magnitude.

        Translates an axis placement from the point <P1> to the point <P2>.

        Translates an axis plaxement in the direction of the vector <V>. The magnitude of the translation is the vector's magnitude.

        Translates an axis placement from the point <P1> to the point <P2>.
        """
    @overload
    def Translated(self,V : gp_Vec) -> gp_Ax3: ...
    def XDirection(self) -> gp_Dir: 
        """
        Returns the "XDirection" of <me>.

        Returns the "XDirection" of <me>.
        """
    def XReverse(self) -> None: 
        """
        Reverses the X direction of <me>.

        Reverses the X direction of <me>.
        """
    def YDirection(self) -> gp_Dir: 
        """
        Returns the "YDirection" of <me>.

        Returns the "YDirection" of <me>.
        """
    def YReverse(self) -> None: 
        """
        Reverses the Y direction of <me>.

        Reverses the Y direction of <me>.
        """
    def ZReverse(self) -> None: 
        """
        Reverses the Z direction of <me>.

        Reverses the Z direction of <me>.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : gp_Pnt,N : gp_Dir,Vx : gp_Dir) -> None: ...
    @overload
    def __init__(self,P : gp_Pnt,V : gp_Dir) -> None: ...
    @overload
    def __init__(self,A : gp_Ax2) -> None: ...
    pass
class gp_Circ():
    """
    Describes a circle in 3D space. A circle is defined by its radius and positioned in space with a coordinate system (a gp_Ax2 object) as follows: - the origin of the coordinate system is the center of the circle, and - the origin, "X Direction" and "Y Direction" of the coordinate system define the plane of the circle. This positioning coordinate system is the "local coordinate system" of the circle. Its "main Direction" gives the normal vector to the plane of the circle. The "main Axis" of the coordinate system is referred to as the "Axis" of the circle. Note: when a gp_Circ circle is converted into a Geom_Circle circle, some implicit properties of the circle are used explicitly: - the "main Direction" of the local coordinate system gives an implicit orientation to the circle (and defines its trigonometric sense), - this orientation corresponds to the direction in which parameter values increase, - the starting point for parameterization is that of the "X Axis" of the local coordinate system (i.e. the "X Axis" of the circle). See Also gce_MakeCirc which provides functions for more complex circle constructions Geom_Circle which provides additional functions for constructing circles and works, in particular, with the parametric equations of circles
    """
    def Area(self) -> float: 
        """
        Computes the area of the circle.

        Computes the area of the circle.
        """
    def Axis(self) -> gp_Ax1: 
        """
        Returns the main axis of the circle. It is the axis perpendicular to the plane of the circle, passing through the "Location" point (center) of the circle.

        Returns the main axis of the circle. It is the axis perpendicular to the plane of the circle, passing through the "Location" point (center) of the circle.
        """
    def Contains(self,P : gp_Pnt,LinearTolerance : float) -> bool: 
        """
        Returns True if the point P is on the circumference. The distance between <me> and <P> must be lower or equal to LinearTolerance.

        Returns True if the point P is on the circumference. The distance between <me> and <P> must be lower or equal to LinearTolerance.
        """
    def Distance(self,P : gp_Pnt) -> float: 
        """
        Computes the minimum of distance between the point P and any point on the circumference of the circle.

        Computes the minimum of distance between the point P and any point on the circumference of the circle.
        """
    def Length(self) -> float: 
        """
        Computes the circumference of the circle.

        Computes the circumference of the circle.
        """
    def Location(self) -> gp_Pnt: 
        """
        Returns the center of the circle. It is the "Location" point of the local coordinate system of the circle

        Returns the center of the circle. It is the "Location" point of the local coordinate system of the circle
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Circ: 
        """
        Performs the symmetrical transformation of a circle with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a circle with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a circle with respect to a plane. The axis placement A2 locates the plane of the of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Circ: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Circ: ...
    def Position(self) -> gp_Ax2: 
        """
        Returns the position of the circle. It is the local coordinate system of the circle.

        Returns the position of the circle. It is the local coordinate system of the circle.
        """
    def Radius(self) -> float: 
        """
        Returns the radius of this circle.

        Returns the radius of this circle.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Circ: 
        """
        Rotates a circle. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a circle. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Circ: 
        """
        Scales a circle. S is the scaling value. Warnings : If S is negative the radius stay positive but the "XAxis" and the "YAxis" are reversed as for an ellipse.

        Scales a circle. S is the scaling value. Warnings : If S is negative the radius stay positive but the "XAxis" and the "YAxis" are reversed as for an ellipse.
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Changes the main axis of the circle. It is the axis perpendicular to the plane of the circle. Raises ConstructionError if the direction of A1 is parallel to the "XAxis" of the circle.

        Changes the main axis of the circle. It is the axis perpendicular to the plane of the circle. Raises ConstructionError if the direction of A1 is parallel to the "XAxis" of the circle.
        """
    def SetLocation(self,P : gp_Pnt) -> None: 
        """
        Changes the "Location" point (center) of the circle.

        Changes the "Location" point (center) of the circle.
        """
    def SetPosition(self,A2 : gp_Ax2) -> None: 
        """
        Changes the position of the circle.

        Changes the position of the circle.
        """
    @overload
    def SetRadius(self,R : float) -> None: 
        """
        Modifies the radius of this circle. Warning. This class does not prevent the creation of a circle where Radius is null. Exceptions Standard_ConstructionError if Radius is negative.

        Modifies the radius of this circle. Warning. This class does not prevent the creation of a circle where Radius is null. Exceptions Standard_ConstructionError if Radius is negative.
        """
    @overload
    def SetRadius(self,Radius : float) -> None: ...
    def SquareDistance(self,P : gp_Pnt) -> float: 
        """
        Computes the square distance between <me> and the point P.

        Computes the square distance between <me> and the point P.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Circ: 
        """
        Transforms a circle with the transformation T from class Trsf.

        Transforms a circle with the transformation T from class Trsf.
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Circ: 
        """
        Translates a circle in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a circle from the point P1 to the point P2.

        Translates a circle in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a circle from the point P1 to the point P2.
        """
    @overload
    def Translated(self,V : gp_Vec) -> gp_Circ: ...
    def XAxis(self) -> gp_Ax1: 
        """
        Returns the "XAxis" of the circle. This axis is perpendicular to the axis of the conic. This axis and the "Yaxis" define the plane of the conic.

        Returns the "XAxis" of the circle. This axis is perpendicular to the axis of the conic. This axis and the "Yaxis" define the plane of the conic.
        """
    def YAxis(self) -> gp_Ax1: 
        """
        Returns the "YAxis" of the circle. This axis and the "Xaxis" define the plane of the conic. The "YAxis" is perpendicular to the "Xaxis".

        Returns the "YAxis" of the circle. This axis and the "Xaxis" define the plane of the conic. The "YAxis" is perpendicular to the "Xaxis".
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,A2 : gp_Ax2,Radius : float) -> None: ...
    pass
class gp_Circ2d():
    """
    Describes a circle in the plane (2D space). A circle is defined by its radius and positioned in the plane with a coordinate system (a gp_Ax22d object) as follows: - the origin of the coordinate system is the center of the circle, and - the orientation (direct or indirect) of the coordinate system gives an implicit orientation to the circle (and defines its trigonometric sense). This positioning coordinate system is the "local coordinate system" of the circle. Note: when a gp_Circ2d circle is converted into a Geom2d_Circle circle, some implicit properties of the circle are used explicitly: - the implicit orientation corresponds to the direction in which parameter values increase, - the starting point for parameterization is that of the "X Axis" of the local coordinate system (i.e. the "X Axis" of the circle). See Also GccAna and Geom2dGcc packages which provide functions for constructing circles defined by geometric constraints gce_MakeCirc2d which provides functions for more complex circle constructions Geom2d_Circle which provides additional functions for constructing circles and works, with the parametric equations of circles in particular gp_Ax22d
    """
    def Area(self) -> float: 
        """
        Computes the area of the circle.

        Computes the area of the circle.
        """
    def Axis(self) -> gp_Ax22d: 
        """
        returns the position of the circle.

        returns the position of the circle.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float]: 
        """
        Returns the normalized coefficients from the implicit equation of the circle : A * (X**2) + B * (Y**2) + 2*C*(X*Y) + 2*D*X + 2*E*Y + F = 0.0

        Returns the normalized coefficients from the implicit equation of the circle : A * (X**2) + B * (Y**2) + 2*C*(X*Y) + 2*D*X + 2*E*Y + F = 0.0
        """
    def Contains(self,P : gp_Pnt2d,LinearTolerance : float) -> bool: 
        """
        Does <me> contain P ? Returns True if the distance between P and any point on the circumference of the circle is lower of equal to <LinearTolerance>.

        Does <me> contain P ? Returns True if the distance between P and any point on the circumference of the circle is lower of equal to <LinearTolerance>.
        """
    def Distance(self,P : gp_Pnt2d) -> float: 
        """
        Computes the minimum of distance between the point P and any point on the circumference of the circle.

        Computes the minimum of distance between the point P and any point on the circumference of the circle.
        """
    def IsDirect(self) -> bool: 
        """
        Returns true if the local coordinate system is direct and false in the other case.

        Returns true if the local coordinate system is direct and false in the other case.
        """
    def Length(self) -> float: 
        """
        computes the circumference of the circle.

        computes the circumference of the circle.
        """
    def Location(self) -> gp_Pnt2d: 
        """
        Returns the location point (center) of the circle.

        Returns the location point (center) of the circle.
        """
    @overload
    def Mirror(self,A : gp_Ax2d) -> None: 
        """
        None

        None
        """
    @overload
    def Mirror(self,P : gp_Pnt2d) -> None: ...
    @overload
    def Mirrored(self,A : gp_Ax2d) -> gp_Circ2d: 
        """
        Performs the symmetrical transformation of a circle with respect to the point P which is the center of the symmetry

        Performs the symmetrical transformation of a circle with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirrored(self,P : gp_Pnt2d) -> gp_Circ2d: ...
    def Position(self) -> gp_Ax22d: 
        """
        returns the position of the circle. Idem Axis(me).

        returns the position of the circle. Idem Axis(me).
        """
    def Radius(self) -> float: 
        """
        Returns the radius value of the circle.

        Returns the radius value of the circle.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation of the local coordinate system of this circle (the "Y Direction" is reversed) and therefore changes the implicit orientation of this circle. Reverse assigns the result to this circle,

        Reverses the orientation of the local coordinate system of this circle (the "Y Direction" is reversed) and therefore changes the implicit orientation of this circle. Reverse assigns the result to this circle,
        """
    def Reversed(self) -> gp_Circ2d: 
        """
        Reverses the orientation of the local coordinate system of this circle (the "Y Direction" is reversed) and therefore changes the implicit orientation of this circle. Reversed creates a new circle.

        Reverses the orientation of the local coordinate system of this circle (the "Y Direction" is reversed) and therefore changes the implicit orientation of this circle. Reversed creates a new circle.
        """
    def Rotate(self,P : gp_Pnt2d,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,P : gp_Pnt2d,Ang : float) -> gp_Circ2d: 
        """
        Rotates a circle. P is the center of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a circle. P is the center of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt2d,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt2d,S : float) -> gp_Circ2d: 
        """
        Scales a circle. S is the scaling value. Warnings : If S is negative the radius stay positive but the "XAxis" and the "YAxis" are reversed as for an ellipse.

        Scales a circle. S is the scaling value. Warnings : If S is negative the radius stay positive but the "XAxis" and the "YAxis" are reversed as for an ellipse.
        """
    def SetAxis(self,A : gp_Ax22d) -> None: 
        """
        Changes the X axis of the circle.

        Changes the X axis of the circle.
        """
    def SetLocation(self,P : gp_Pnt2d) -> None: 
        """
        Changes the location point (center) of the circle.

        Changes the location point (center) of the circle.
        """
    def SetRadius(self,Radius : float) -> None: 
        """
        Modifies the radius of this circle. This class does not prevent the creation of a circle where Radius is null. Exceptions Standard_ConstructionError if Radius is negative.

        Modifies the radius of this circle. This class does not prevent the creation of a circle where Radius is null. Exceptions Standard_ConstructionError if Radius is negative.
        """
    def SetXAxis(self,A : gp_Ax2d) -> None: 
        """
        Changes the X axis of the circle.

        Changes the X axis of the circle.
        """
    def SetYAxis(self,A : gp_Ax2d) -> None: 
        """
        Changes the Y axis of the circle.

        Changes the Y axis of the circle.
        """
    def SquareDistance(self,P : gp_Pnt2d) -> float: 
        """
        Computes the square distance between <me> and the point P.

        Computes the square distance between <me> and the point P.
        """
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Circ2d: 
        """
        Transforms a circle with the transformation T from class Trsf2d.

        Transforms a circle with the transformation T from class Trsf2d.
        """
    @overload
    def Translate(self,V : gp_Vec2d) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> gp_Circ2d: 
        """
        Translates a circle in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a circle from the point P1 to the point P2.

        Translates a circle in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a circle from the point P1 to the point P2.
        """
    @overload
    def Translated(self,V : gp_Vec2d) -> gp_Circ2d: ...
    def XAxis(self) -> gp_Ax2d: 
        """
        returns the X axis of the circle.

        returns the X axis of the circle.
        """
    def YAxis(self) -> gp_Ax2d: 
        """
        Returns the Y axis of the circle. Reverses the direction of the circle.

        Returns the Y axis of the circle. Reverses the direction of the circle.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Axis : gp_Ax22d,Radius : float) -> None: ...
    @overload
    def __init__(self,XAxis : gp_Ax2d,Radius : float,Sense : bool=True) -> None: ...
    pass
class gp_Cone():
    """
    Defines an infinite conical surface. A cone is defined by its half-angle (can be negative) at the apex and positioned in space with a coordinate system (a gp_Ax3 object) and a "reference radius" where: - the "main Axis" of the coordinate system is the axis of revolution of the cone, - the plane defined by the origin, the "X Direction" and the "Y Direction" of the coordinate system is the reference plane of the cone; the intersection of the cone with this reference plane is a circle of radius equal to the reference radius, if the half-angle is positive, the apex of the cone is on the negative side of the "main Axis" of the coordinate system. If the half-angle is negative, the apex is on the positive side. This coordinate system is the "local coordinate system" of the cone. Note: when a gp_Cone cone is converted into a Geom_ConicalSurface cone, some implicit properties of its local coordinate system are used explicitly: - its origin, "X Direction", "Y Direction" and "main Direction" are used directly to define the parametric directions on the cone and the origin of the parameters, - its implicit orientation (right-handed or left-handed) gives the orientation (direct or indirect) of the Geom_ConicalSurface cone. See Also gce_MakeCone which provides functions for more complex cone constructions Geom_ConicalSurface which provides additional functions for constructing cones and works, in particular, with the parametric equations of cones gp_Ax3
    """
    def Apex(self) -> gp_Pnt: 
        """
        Computes the cone's top. The Apex of the cone is on the negative side of the symmetry axis of the cone.

        Computes the cone's top. The Apex of the cone is on the negative side of the symmetry axis of the cone.
        """
    def Axis(self) -> gp_Ax1: 
        """
        returns the symmetry axis of the cone.

        returns the symmetry axis of the cone.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float, float, float, float, float]: 
        """
        Computes the coefficients of the implicit equation of the quadric in the absolute cartesian coordinates system : A1.X**2 + A2.Y**2 + A3.Z**2 + 2.(B1.X.Y + B2.X.Z + B3.Y.Z) + 2.(C1.X + C2.Y + C3.Z) + D = 0.0
        """
    def Direct(self) -> bool: 
        """
        Returns true if the local coordinate system of this cone is right-handed.

        Returns true if the local coordinate system of this cone is right-handed.
        """
    def Location(self) -> gp_Pnt: 
        """
        returns the "Location" point of the cone.

        returns the "Location" point of the cone.
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Cone: 
        """
        Performs the symmetrical transformation of a cone with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a cone with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a cone with respect to a plane. The axis placement A2 locates the plane of the of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Cone: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Cone: ...
    def Position(self) -> gp_Ax3: 
        """
        Returns the local coordinates system of the cone.

        Returns the local coordinates system of the cone.
        """
    def RefRadius(self) -> float: 
        """
        Returns the radius of the cone in the reference plane.

        Returns the radius of the cone in the reference plane.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Cone: 
        """
        Rotates a cone. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a cone. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Cone: 
        """
        Scales a cone. S is the scaling value. The absolute value of S is used to scale the cone

        Scales a cone. S is the scaling value. The absolute value of S is used to scale the cone
        """
    def SemiAngle(self) -> float: 
        """
        Returns the half-angle at the apex of this cone. Attention! Semi-angle can be negative.

        Returns the half-angle at the apex of this cone. Attention! Semi-angle can be negative.
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Changes the symmetry axis of the cone. Raises ConstructionError the direction of A1 is parallel to the "XDirection" of the coordinate system of the cone.

        Changes the symmetry axis of the cone. Raises ConstructionError the direction of A1 is parallel to the "XDirection" of the coordinate system of the cone.
        """
    def SetLocation(self,Loc : gp_Pnt) -> None: 
        """
        Changes the location of the cone.

        Changes the location of the cone.
        """
    def SetPosition(self,A3 : gp_Ax3) -> None: 
        """
        Changes the local coordinate system of the cone. This coordinate system defines the reference plane of the cone.

        Changes the local coordinate system of the cone. This coordinate system defines the reference plane of the cone.
        """
    def SetRadius(self,R : float) -> None: 
        """
        Changes the radius of the cone in the reference plane of the cone. Raised if R < 0.0

        Changes the radius of the cone in the reference plane of the cone. Raised if R < 0.0
        """
    def SetSemiAngle(self,Ang : float) -> None: 
        """
        Changes the semi-angle of the cone. Semi-angle can be negative. Its absolute value Abs(Ang) is in range ]0,PI/2[. Raises ConstructionError if Abs(Ang) < Resolution from gp or Abs(Ang) >= PI/2 - Resolution

        Changes the semi-angle of the cone. Semi-angle can be negative. Its absolute value Abs(Ang) is in range ]0,PI/2[. Raises ConstructionError if Abs(Ang) < Resolution from gp or Abs(Ang) >= PI/2 - Resolution
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Cone: 
        """
        Transforms a cone with the transformation T from class Trsf.

        Transforms a cone with the transformation T from class Trsf.
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Cone: 
        """
        Translates a cone in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a cone from the point P1 to the point P2.

        Translates a cone in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a cone from the point P1 to the point P2.
        """
    @overload
    def Translated(self,V : gp_Vec) -> gp_Cone: ...
    def UReverse(self) -> None: 
        """
        Reverses the U parametrization of the cone reversing the YAxis.

        Reverses the U parametrization of the cone reversing the YAxis.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V parametrization of the cone reversing the ZAxis.

        Reverses the V parametrization of the cone reversing the ZAxis.
        """
    def XAxis(self) -> gp_Ax1: 
        """
        Returns the XAxis of the reference plane.

        Returns the XAxis of the reference plane.
        """
    def YAxis(self) -> gp_Ax1: 
        """
        Returns the YAxis of the reference plane.

        Returns the YAxis of the reference plane.
        """
    @overload
    def __init__(self,A3 : gp_Ax3,Ang : float,Radius : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Cylinder():
    """
    Describes an infinite cylindrical surface. A cylinder is defined by its radius and positioned in space with a coordinate system (a gp_Ax3 object), the "main Axis" of which is the axis of the cylinder. This coordinate system is the "local coordinate system" of the cylinder. Note: when a gp_Cylinder cylinder is converted into a Geom_CylindricalSurface cylinder, some implicit properties of its local coordinate system are used explicitly: - its origin, "X Direction", "Y Direction" and "main Direction" are used directly to define the parametric directions on the cylinder and the origin of the parameters, - its implicit orientation (right-handed or left-handed) gives an orientation (direct or indirect) to the Geom_CylindricalSurface cylinder. See Also gce_MakeCylinder which provides functions for more complex cylinder constructions Geom_CylindricalSurface which provides additional functions for constructing cylinders and works, in particular, with the parametric equations of cylinders gp_Ax3
    """
    def Axis(self) -> gp_Ax1: 
        """
        Returns the symmetry axis of the cylinder.

        Returns the symmetry axis of the cylinder.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float, float, float, float, float]: 
        """
        Computes the coefficients of the implicit equation of the quadric in the absolute cartesian coordinate system : A1.X**2 + A2.Y**2 + A3.Z**2 + 2.(B1.X.Y + B2.X.Z + B3.Y.Z) + 2.(C1.X + C2.Y + C3.Z) + D = 0.0
        """
    def Direct(self) -> bool: 
        """
        Returns true if the local coordinate system of this cylinder is right-handed.

        Returns true if the local coordinate system of this cylinder is right-handed.
        """
    def Location(self) -> gp_Pnt: 
        """
        Returns the "Location" point of the cylinder.

        Returns the "Location" point of the cylinder.
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Cylinder: 
        """
        Performs the symmetrical transformation of a cylinder with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a cylinder with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a cylinder with respect to a plane. The axis placement A2 locates the plane of the of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Cylinder: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Cylinder: ...
    def Position(self) -> gp_Ax3: 
        """
        Returns the local coordinate system of the cylinder.

        Returns the local coordinate system of the cylinder.
        """
    def Radius(self) -> float: 
        """
        Returns the radius of the cylinder.

        Returns the radius of the cylinder.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Cylinder: 
        """
        Rotates a cylinder. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a cylinder. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Cylinder: 
        """
        Scales a cylinder. S is the scaling value. The absolute value of S is used to scale the cylinder

        Scales a cylinder. S is the scaling value. The absolute value of S is used to scale the cylinder
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Changes the symmetry axis of the cylinder. Raises ConstructionError if the direction of A1 is parallel to the "XDirection" of the coordinate system of the cylinder.

        Changes the symmetry axis of the cylinder. Raises ConstructionError if the direction of A1 is parallel to the "XDirection" of the coordinate system of the cylinder.
        """
    def SetLocation(self,Loc : gp_Pnt) -> None: 
        """
        Changes the location of the surface.

        Changes the location of the surface.
        """
    def SetPosition(self,A3 : gp_Ax3) -> None: 
        """
        Change the local coordinate system of the surface.

        Change the local coordinate system of the surface.
        """
    def SetRadius(self,R : float) -> None: 
        """
        Modifies the radius of this cylinder. Exceptions Standard_ConstructionError if R is negative.

        Modifies the radius of this cylinder. Exceptions Standard_ConstructionError if R is negative.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Cylinder: 
        """
        Transforms a cylinder with the transformation T from class Trsf.

        Transforms a cylinder with the transformation T from class Trsf.
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: ...
    @overload
    def Translated(self,V : gp_Vec) -> gp_Cylinder: 
        """
        Translates a cylinder in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a cylinder from the point P1 to the point P2.

        Translates a cylinder in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a cylinder from the point P1 to the point P2.
        """
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Cylinder: ...
    def UReverse(self) -> None: 
        """
        Reverses the U parametrization of the cylinder reversing the YAxis.

        Reverses the U parametrization of the cylinder reversing the YAxis.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V parametrization of the plane reversing the Axis.

        Reverses the V parametrization of the plane reversing the Axis.
        """
    def XAxis(self) -> gp_Ax1: 
        """
        Returns the axis X of the cylinder.

        Returns the axis X of the cylinder.
        """
    def YAxis(self) -> gp_Ax1: 
        """
        Returns the axis Y of the cylinder.

        Returns the axis Y of the cylinder.
        """
    @overload
    def __init__(self,A3 : gp_Ax3,Radius : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Dir():
    """
    Describes a unit vector in 3D space. This unit vector is also called "Direction". See Also gce_MakeDir which provides functions for more complex unit vector constructions Geom_Direction which provides additional functions for constructing unit vectors and works, in particular, with the parametric equations of unit vectors.
    """
    def Angle(self,Other : gp_Dir) -> float: 
        """
        Computes the angular value in radians between <me> and <Other>. This value is always positive in 3D space. Returns the angle in the range [0, PI]
        """
    def AngleWithRef(self,Other : gp_Dir,VRef : gp_Dir) -> float: 
        """
        Computes the angular value between <me> and <Other>. <VRef> is the direction of reference normal to <me> and <Other> and its orientation gives the positive sense of rotation. If the cross product <me> ^ <Other> has the same orientation as <VRef> the angular value is positive else negative. Returns the angular value in the range -PI and PI (in radians). Raises DomainError if <me> and <Other> are not parallel this exception is raised when <VRef> is in the same plane as <me> and <Other> The tolerance criterion is Resolution from package gp.
        """
    @overload
    def Coord(self) -> Tuple[float, float, float]: 
        """
        Returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned Exceptions Standard_OutOfRange if Index is not 1, 2, or 3.

        Returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned Exceptions Standard_OutOfRange if Index is not 1, 2, or 3.

        Returns for the unit vector its three coordinates Xv, Yv, and Zv.

        Returns for the unit vector its three coordinates Xv, Yv, and Zv.
        """
    @overload
    def Coord(self,Index : int) -> float: ...
    def Cross(self,Right : gp_Dir) -> None: 
        """
        Computes the cross product between two directions Raises the exception ConstructionError if the two directions are parallel because the computed vector cannot be normalized to create a direction.

        Computes the cross product between two directions Raises the exception ConstructionError if the two directions are parallel because the computed vector cannot be normalized to create a direction.
        """
    def CrossCross(self,V1 : gp_Dir,V2 : gp_Dir) -> None: 
        """
        None

        None
        """
    def CrossCrossed(self,V1 : gp_Dir,V2 : gp_Dir) -> gp_Dir: 
        """
        Computes the double vector product this ^ (V1 ^ V2). - CrossCrossed creates a new unit vector. Exceptions Standard_ConstructionError if: - V1 and V2 are parallel, or - this unit vector and (V1 ^ V2) are parallel. This is because, in these conditions, the computed vector is null and cannot be normalized.

        Computes the double vector product this ^ (V1 ^ V2). - CrossCrossed creates a new unit vector. Exceptions Standard_ConstructionError if: - V1 and V2 are parallel, or - this unit vector and (V1 ^ V2) are parallel. This is because, in these conditions, the computed vector is null and cannot be normalized.
        """
    def Crossed(self,Right : gp_Dir) -> gp_Dir: 
        """
        Computes the triple vector product. <me> ^ (V1 ^ V2) Raises the exception ConstructionError if V1 and V2 are parallel or <me> and (V1^V2) are parallel because the computed vector can't be normalized to create a direction.

        Computes the triple vector product. <me> ^ (V1 ^ V2) Raises the exception ConstructionError if V1 and V2 are parallel or <me> and (V1^V2) are parallel because the computed vector can't be normalized to create a direction.
        """
    def Dot(self,Other : gp_Dir) -> float: 
        """
        Computes the scalar product

        Computes the scalar product
        """
    def DotCross(self,V1 : gp_Dir,V2 : gp_Dir) -> float: 
        """
        Computes the triple scalar product <me> * (V1 ^ V2). Warnings : The computed vector V1' = V1 ^ V2 is not normalized to create a unitary vector. So this method never raises an exception even if V1 and V2 are parallel.

        Computes the triple scalar product <me> * (V1 ^ V2). Warnings : The computed vector V1' = V1 ^ V2 is not normalized to create a unitary vector. So this method never raises an exception even if V1 and V2 are parallel.
        """
    def IsEqual(self,Other : gp_Dir,AngularTolerance : float) -> bool: 
        """
        Returns True if the angle between the two directions is lower or equal to AngularTolerance.

        Returns True if the angle between the two directions is lower or equal to AngularTolerance.
        """
    def IsNormal(self,Other : gp_Dir,AngularTolerance : float) -> bool: 
        """
        Returns True if the angle between this unit vector and the unit vector Other is equal to Pi/2 (normal).

        Returns True if the angle between this unit vector and the unit vector Other is equal to Pi/2 (normal).
        """
    def IsOpposite(self,Other : gp_Dir,AngularTolerance : float) -> bool: 
        """
        Returns True if the angle between this unit vector and the unit vector Other is equal to Pi (opposite).

        Returns True if the angle between this unit vector and the unit vector Other is equal to Pi (opposite).
        """
    def IsParallel(self,Other : gp_Dir,AngularTolerance : float) -> bool: 
        """
        Returns true if the angle between this unit vector and the unit vector Other is equal to 0 or to Pi. Note: the tolerance criterion is given by AngularTolerance.

        Returns true if the angle between this unit vector and the unit vector Other is equal to 0 or to Pi. Note: the tolerance criterion is given by AngularTolerance.
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirror(self,V : gp_Dir) -> None: ...
    @overload
    def Mirrored(self,V : gp_Dir) -> gp_Dir: 
        """
        Performs the symmetrical transformation of a direction with respect to the direction V which is the center of the symmetry.

        Performs the symmetrical transformation of a direction with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a direction with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Dir: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Dir: ...
    def Reverse(self) -> None: 
        """
        None

        None
        """
    def Reversed(self) -> gp_Dir: 
        """
        Reverses the orientation of a direction geometric transformations Performs the symmetrical transformation of a direction with respect to the direction V which is the center of the symmetry.]

        Reverses the orientation of a direction geometric transformations Performs the symmetrical transformation of a direction with respect to the direction V which is the center of the symmetry.]
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Dir: 
        """
        Rotates a direction. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a direction. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    @overload
    def SetCoord(self,Xv : float,Yv : float,Zv : float) -> None: 
        """
        For this unit vector, assigns the value Xi to: - the X coordinate if Index is 1, or - the Y coordinate if Index is 2, or - the Z coordinate if Index is 3, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_OutOfRange if Index is not 1, 2, or 3. Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - Sqrt(Xv*Xv + Yv*Yv + Zv*Zv), or - the modulus of the number triple formed by the new value Xi and the two other coordinates of this vector that were not directly modified.

        For this unit vector, assigns the values Xv, Yv and Zv to its three coordinates. Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly.

        For this unit vector, assigns the value Xi to: - the X coordinate if Index is 1, or - the Y coordinate if Index is 2, or - the Z coordinate if Index is 3, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_OutOfRange if Index is not 1, 2, or 3. Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - Sqrt(Xv*Xv + Yv*Yv + Zv*Zv), or - the modulus of the number triple formed by the new value Xi and the two other coordinates of this vector that were not directly modified.

        For this unit vector, assigns the values Xv, Yv and Zv to its three coordinates. Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly.
        """
    @overload
    def SetCoord(self,Index : int,Xi : float) -> None: ...
    def SetX(self,X : float) -> None: 
        """
        Assigns the given value to the X coordinate of this unit vector.

        Assigns the given value to the X coordinate of this unit vector.
        """
    @overload
    def SetXYZ(self,XYZ : gp_XYZ) -> None: 
        """
        Assigns the three coordinates of Coord to this unit vector.

        Assigns the three coordinates of Coord to this unit vector.
        """
    @overload
    def SetXYZ(self,Coord : gp_XYZ) -> None: ...
    def SetY(self,Y : float) -> None: 
        """
        Assigns the given value to the Y coordinate of this unit vector.

        Assigns the given value to the Y coordinate of this unit vector.
        """
    def SetZ(self,Z : float) -> None: 
        """
        Assigns the given value to the Z coordinate of this unit vector.

        Assigns the given value to the Z coordinate of this unit vector.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Dir: 
        """
        Transforms a direction with a "Trsf" from gp. Warnings : If the scale factor of the "Trsf" T is negative then the direction <me> is reversed.

        Transforms a direction with a "Trsf" from gp. Warnings : If the scale factor of the "Trsf" T is negative then the direction <me> is reversed.
        """
    def X(self) -> float: 
        """
        Returns the X coordinate for a unit vector.

        Returns the X coordinate for a unit vector.
        """
    def XYZ(self) -> gp_XYZ: 
        """
        for this unit vector, returns its three coordinates as a number triplea.

        for this unit vector, returns its three coordinates as a number triplea.
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate for a unit vector.

        Returns the Y coordinate for a unit vector.
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate for a unit vector.

        Returns the Z coordinate for a unit vector.
        """
    @overload
    def __init__(self,Xv : float,Yv : float,Zv : float) -> None: ...
    @overload
    def __init__(self,Coord : gp_XYZ) -> None: ...
    @overload
    def __init__(self,V : gp_Vec) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __ipow__(self,Right : gp_Dir) -> None: 
        """
        None
        """
    def __mul__(self,Other : gp_Dir) -> float: 
        """
        None
        """
    def __pow__(self,Right : gp_Dir) -> gp_Dir: 
        """
        None
        """
    def __rmul__(self,Other : gp_Dir) -> float: 
        """
        None
        """
    def __sub__(self) -> gp_Dir: 
        """
        None
        """
    pass
class gp_Dir2d():
    """
    Describes a unit vector in the plane (2D space). This unit vector is also called "Direction". See Also gce_MakeDir2d which provides functions for more complex unit vector constructions Geom2d_Direction which provides additional functions for constructing unit vectors and works, in particular, with the parametric equations of unit vectors
    """
    def Angle(self,Other : gp_Dir2d) -> float: 
        """
        Computes the angular value in radians between <me> and <Other>. Returns the angle in the range [-PI, PI].
        """
    @overload
    def Coord(self,Index : int) -> float: 
        """
        For this unit vector returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Raises OutOfRange if Index != {1, 2}.

        For this unit vector returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Raises OutOfRange if Index != {1, 2}.

        For this unit vector returns its two coordinates Xv and Yv. Raises OutOfRange if Index != {1, 2}.

        For this unit vector returns its two coordinates Xv and Yv. Raises OutOfRange if Index != {1, 2}.
        """
    @overload
    def Coord(self) -> Tuple[float, float]: ...
    def Crossed(self,Right : gp_Dir2d) -> float: 
        """
        Computes the cross product between two directions.

        Computes the cross product between two directions.
        """
    def Dot(self,Other : gp_Dir2d) -> float: 
        """
        Computes the scalar product

        Computes the scalar product
        """
    def IsEqual(self,Other : gp_Dir2d,AngularTolerance : float) -> bool: 
        """
        Returns True if the two vectors have the same direction i.e. the angle between this unit vector and the unit vector Other is less than or equal to AngularTolerance.

        Returns True if the two vectors have the same direction i.e. the angle between this unit vector and the unit vector Other is less than or equal to AngularTolerance.
        """
    def IsNormal(self,Other : gp_Dir2d,AngularTolerance : float) -> bool: 
        """
        Returns True if the angle between this unit vector and the unit vector Other is equal to Pi/2 or -Pi/2 (normal) i.e. Abs(Abs(<me>.Angle(Other)) - PI/2.) <= AngularTolerance

        Returns True if the angle between this unit vector and the unit vector Other is equal to Pi/2 or -Pi/2 (normal) i.e. Abs(Abs(<me>.Angle(Other)) - PI/2.) <= AngularTolerance
        """
    def IsOpposite(self,Other : gp_Dir2d,AngularTolerance : float) -> bool: 
        """
        Returns True if the angle between this unit vector and the unit vector Other is equal to Pi or -Pi (opposite). i.e. PI - Abs(<me>.Angle(Other)) <= AngularTolerance

        Returns True if the angle between this unit vector and the unit vector Other is equal to Pi or -Pi (opposite). i.e. PI - Abs(<me>.Angle(Other)) <= AngularTolerance
        """
    def IsParallel(self,Other : gp_Dir2d,AngularTolerance : float) -> bool: 
        """
        returns true if if the angle between this unit vector and unit vector Other is equal to 0, Pi or -Pi. i.e. Abs(Angle(<me>, Other)) <= AngularTolerance or PI - Abs(Angle(<me>, Other)) <= AngularTolerance

        returns true if if the angle between this unit vector and unit vector Other is equal to 0, Pi or -Pi. i.e. Abs(Angle(<me>, Other)) <= AngularTolerance or PI - Abs(Angle(<me>, Other)) <= AngularTolerance
        """
    @overload
    def Mirror(self,V : gp_Dir2d) -> None: 
        """
        None

        None
        """
    @overload
    def Mirror(self,A : gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,V : gp_Dir2d) -> gp_Dir2d: 
        """
        Performs the symmetrical transformation of a direction with respect to the direction V which is the center of the symmetry.

        Performs the symmetrical transformation of a direction with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirrored(self,A : gp_Ax2d) -> gp_Dir2d: ...
    def Reverse(self) -> None: 
        """
        None

        None
        """
    def Reversed(self) -> gp_Dir2d: 
        """
        Reverses the orientation of a direction

        Reverses the orientation of a direction
        """
    def Rotate(self,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,Ang : float) -> gp_Dir2d: 
        """
        Rotates a direction. Ang is the angular value of the rotation in radians.

        Rotates a direction. Ang is the angular value of the rotation in radians.
        """
    @overload
    def SetCoord(self,Index : int,Xi : float) -> None: 
        """
        For this unit vector, assigns: the value Xi to: - the X coordinate if Index is 1, or - the Y coordinate if Index is 2, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_OutOfRange if Index is not 1 or 2. Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - Sqrt(Xv*Xv + Yv*Yv), or - the modulus of the number pair formed by the new value Xi and the other coordinate of this vector that was not directly modified. Raises OutOfRange if Index != {1, 2}.

        For this unit vector, assigns: - the values Xv and Yv to its two coordinates, Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_OutOfRange if Index is not 1 or 2. Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - Sqrt(Xv*Xv + Yv*Yv), or - the modulus of the number pair formed by the new value Xi and the other coordinate of this vector that was not directly modified. Raises OutOfRange if Index != {1, 2}.

        For this unit vector, assigns: the value Xi to: - the X coordinate if Index is 1, or - the Y coordinate if Index is 2, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_OutOfRange if Index is not 1 or 2. Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - Sqrt(Xv*Xv + Yv*Yv), or - the modulus of the number pair formed by the new value Xi and the other coordinate of this vector that was not directly modified. Raises OutOfRange if Index != {1, 2}.

        For this unit vector, assigns: - the values Xv and Yv to its two coordinates, Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_OutOfRange if Index is not 1 or 2. Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - Sqrt(Xv*Xv + Yv*Yv), or - the modulus of the number pair formed by the new value Xi and the other coordinate of this vector that was not directly modified. Raises OutOfRange if Index != {1, 2}.
        """
    @overload
    def SetCoord(self,Xv : float,Yv : float) -> None: ...
    def SetX(self,X : float) -> None: 
        """
        Assigns the given value to the X coordinate of this unit vector, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - the modulus of Coord, or - the modulus of the number pair formed from the new X or Y coordinate and the other coordinate of this vector that was not directly modified.

        Assigns the given value to the X coordinate of this unit vector, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - the modulus of Coord, or - the modulus of the number pair formed from the new X or Y coordinate and the other coordinate of this vector that was not directly modified.
        """
    @overload
    def SetXY(self,XY : gp_XY) -> None: 
        """
        Assigns: - the two coordinates of Coord to this unit vector, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - the modulus of Coord, or - the modulus of the number pair formed from the new X or Y coordinate and the other coordinate of this vector that was not directly modified.

        Assigns: - the two coordinates of Coord to this unit vector, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - the modulus of Coord, or - the modulus of the number pair formed from the new X or Y coordinate and the other coordinate of this vector that was not directly modified.
        """
    @overload
    def SetXY(self,Coord : gp_XY) -> None: ...
    def SetY(self,Y : float) -> None: 
        """
        Assigns the given value to the Y coordinate of this unit vector, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - the modulus of Coord, or - the modulus of the number pair formed from the new X or Y coordinate and the other coordinate of this vector that was not directly modified.

        Assigns the given value to the Y coordinate of this unit vector, and then normalizes it. Warning Remember that all the coordinates of a unit vector are implicitly modified when any single one is changed directly. Exceptions Standard_ConstructionError if either of the following is less than or equal to gp::Resolution(): - the modulus of Coord, or - the modulus of the number pair formed from the new X or Y coordinate and the other coordinate of this vector that was not directly modified.
        """
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Dir2d: 
        """
        Transforms a direction with the "Trsf" T. Warnings : If the scale factor of the "Trsf" T is negative then the direction <me> is reversed.

        Transforms a direction with the "Trsf" T. Warnings : If the scale factor of the "Trsf" T is negative then the direction <me> is reversed.
        """
    def X(self) -> float: 
        """
        For this unit vector, returns its X coordinate.

        For this unit vector, returns its X coordinate.
        """
    def XY(self) -> gp_XY: 
        """
        For this unit vector, returns its two coordinates as a number pair. Comparison between Directions The precision value is an input data.

        For this unit vector, returns its two coordinates as a number pair. Comparison between Directions The precision value is an input data.
        """
    def Y(self) -> float: 
        """
        For this unit vector, returns its Y coordinate.

        For this unit vector, returns its Y coordinate.
        """
    @overload
    def __init__(self,V : gp_Vec2d) -> None: ...
    @overload
    def __init__(self,Coord : gp_XY) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Xv : float,Yv : float) -> None: ...
    def __mul__(self,Other : gp_Dir2d) -> float: 
        """
        None
        """
    def __pow__(self,Right : gp_Dir2d) -> float: 
        """
        None
        """
    def __rmul__(self,Other : gp_Dir2d) -> float: 
        """
        None
        """
    def __sub__(self) -> gp_Dir2d: 
        """
        None
        """
    pass
class gp_Elips():
    """
    Describes an ellipse in 3D space. An ellipse is defined by its major and minor radii and positioned in space with a coordinate system (a gp_Ax2 object) as follows: - the origin of the coordinate system is the center of the ellipse, - its "X Direction" defines the major axis of the ellipse, and - its "Y Direction" defines the minor axis of the ellipse. Together, the origin, "X Direction" and "Y Direction" of this coordinate system define the plane of the ellipse. This coordinate system is the "local coordinate system" of the ellipse. In this coordinate system, the equation of the ellipse is: X*X / (MajorRadius**2) + Y*Y / (MinorRadius**2) = 1.0 The "main Direction" of the local coordinate system gives the normal vector to the plane of the ellipse. This vector gives an implicit orientation to the ellipse (definition of the trigonometric sense). We refer to the "main Axis" of the local coordinate system as the "Axis" of the ellipse. See Also gce_MakeElips which provides functions for more complex ellipse constructions Geom_Ellipse which provides additional functions for constructing ellipses and works, in particular, with the parametric equations of ellipses
    """
    def Area(self) -> float: 
        """
        Computes the area of the Ellipse.

        Computes the area of the Ellipse.
        """
    def Axis(self) -> gp_Ax1: 
        """
        Computes the axis normal to the plane of the ellipse.

        Computes the axis normal to the plane of the ellipse.
        """
    def Directrix1(self) -> gp_Ax1: 
        """
        Computes the first or second directrix of this ellipse. These are the lines, in the plane of the ellipse, normal to the major axis, at a distance equal to MajorRadius/e from the center of the ellipse, where e is the eccentricity of the ellipse. The first directrix (Directrix1) is on the positive side of the major axis. The second directrix (Directrix2) is on the negative side. The directrix is returned as an axis (gp_Ax1 object), the origin of which is situated on the "X Axis" of the local coordinate system of this ellipse. Exceptions Standard_ConstructionError if the eccentricity is null (the ellipse has degenerated into a circle).

        Computes the first or second directrix of this ellipse. These are the lines, in the plane of the ellipse, normal to the major axis, at a distance equal to MajorRadius/e from the center of the ellipse, where e is the eccentricity of the ellipse. The first directrix (Directrix1) is on the positive side of the major axis. The second directrix (Directrix2) is on the negative side. The directrix is returned as an axis (gp_Ax1 object), the origin of which is situated on the "X Axis" of the local coordinate system of this ellipse. Exceptions Standard_ConstructionError if the eccentricity is null (the ellipse has degenerated into a circle).
        """
    def Directrix2(self) -> gp_Ax1: 
        """
        This line is obtained by the symmetrical transformation of "Directrix1" with respect to the "YAxis" of the ellipse. Exceptions Standard_ConstructionError if the eccentricity is null (the ellipse has degenerated into a circle).

        This line is obtained by the symmetrical transformation of "Directrix1" with respect to the "YAxis" of the ellipse. Exceptions Standard_ConstructionError if the eccentricity is null (the ellipse has degenerated into a circle).
        """
    def Eccentricity(self) -> float: 
        """
        Returns the eccentricity of the ellipse between 0.0 and 1.0 If f is the distance between the center of the ellipse and the Focus1 then the eccentricity e = f / MajorRadius. Raises ConstructionError if MajorRadius = 0.0

        Returns the eccentricity of the ellipse between 0.0 and 1.0 If f is the distance between the center of the ellipse and the Focus1 then the eccentricity e = f / MajorRadius. Raises ConstructionError if MajorRadius = 0.0
        """
    def Focal(self) -> float: 
        """
        Computes the focal distance. It is the distance between the two focus focus1 and focus2 of the ellipse.

        Computes the focal distance. It is the distance between the two focus focus1 and focus2 of the ellipse.
        """
    def Focus1(self) -> gp_Pnt: 
        """
        Returns the first focus of the ellipse. This focus is on the positive side of the "XAxis" of the ellipse.

        Returns the first focus of the ellipse. This focus is on the positive side of the "XAxis" of the ellipse.
        """
    def Focus2(self) -> gp_Pnt: 
        """
        Returns the second focus of the ellipse. This focus is on the negative side of the "XAxis" of the ellipse.

        Returns the second focus of the ellipse. This focus is on the negative side of the "XAxis" of the ellipse.
        """
    def Location(self) -> gp_Pnt: 
        """
        Returns the center of the ellipse. It is the "Location" point of the coordinate system of the ellipse.

        Returns the center of the ellipse. It is the "Location" point of the coordinate system of the ellipse.
        """
    def MajorRadius(self) -> float: 
        """
        Returns the major radius of the ellipse.

        Returns the major radius of the ellipse.
        """
    def MinorRadius(self) -> float: 
        """
        Returns the minor radius of the ellipse.

        Returns the minor radius of the ellipse.
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Elips: 
        """
        Performs the symmetrical transformation of an ellipse with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of an ellipse with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of an ellipse with respect to a plane. The axis placement A2 locates the plane of the symmetry (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Elips: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Elips: ...
    def Parameter(self) -> float: 
        """
        Returns p = (1 - e * e) * MajorRadius where e is the eccentricity of the ellipse. Returns 0 if MajorRadius = 0

        Returns p = (1 - e * e) * MajorRadius where e is the eccentricity of the ellipse. Returns 0 if MajorRadius = 0
        """
    def Position(self) -> gp_Ax2: 
        """
        Returns the coordinate system of the ellipse.

        Returns the coordinate system of the ellipse.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Elips: 
        """
        Rotates an ellipse. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates an ellipse. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Elips: 
        """
        Scales an ellipse. S is the scaling value.

        Scales an ellipse. S is the scaling value.
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Changes the axis normal to the plane of the ellipse. It modifies the definition of this plane. The "XAxis" and the "YAxis" are recomputed. The local coordinate system is redefined so that: - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed in the same way as for any gp_Ax2), or Raises ConstructionError if the direction of A1 is parallel to the direction of the "XAxis" of the ellipse.

        Changes the axis normal to the plane of the ellipse. It modifies the definition of this plane. The "XAxis" and the "YAxis" are recomputed. The local coordinate system is redefined so that: - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed in the same way as for any gp_Ax2), or Raises ConstructionError if the direction of A1 is parallel to the direction of the "XAxis" of the ellipse.
        """
    def SetLocation(self,P : gp_Pnt) -> None: 
        """
        Modifies this ellipse, by redefining its local coordinate so that its origin becomes P.

        Modifies this ellipse, by redefining its local coordinate so that its origin becomes P.
        """
    @overload
    def SetMajorRadius(self,MajorRadius : float) -> None: 
        """
        The major radius of the ellipse is on the "XAxis" (major axis) of the ellipse. Raises ConstructionError if MajorRadius < MinorRadius.

        The major radius of the ellipse is on the "XAxis" (major axis) of the ellipse. Raises ConstructionError if MajorRadius < MinorRadius.
        """
    @overload
    def SetMajorRadius(self,R : float) -> None: ...
    @overload
    def SetMinorRadius(self,R : float) -> None: 
        """
        The minor radius of the ellipse is on the "YAxis" (minor axis) of the ellipse. Raises ConstructionError if MinorRadius > MajorRadius or MinorRadius < 0.

        The minor radius of the ellipse is on the "YAxis" (minor axis) of the ellipse. Raises ConstructionError if MinorRadius > MajorRadius or MinorRadius < 0.
        """
    @overload
    def SetMinorRadius(self,MinorRadius : float) -> None: ...
    def SetPosition(self,A2 : gp_Ax2) -> None: 
        """
        Modifies this ellipse, by redefining its local coordinate so that it becomes A2e.

        Modifies this ellipse, by redefining its local coordinate so that it becomes A2e.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Elips: 
        """
        Transforms an ellipse with the transformation T from class Trsf.

        Transforms an ellipse with the transformation T from class Trsf.
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: ...
    @overload
    def Translated(self,V : gp_Vec) -> gp_Elips: 
        """
        Translates an ellipse in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates an ellipse from the point P1 to the point P2.

        Translates an ellipse in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates an ellipse from the point P1 to the point P2.
        """
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Elips: ...
    def XAxis(self) -> gp_Ax1: 
        """
        Returns the "XAxis" of the ellipse whose origin is the center of this ellipse. It is the major axis of the ellipse.

        Returns the "XAxis" of the ellipse whose origin is the center of this ellipse. It is the major axis of the ellipse.
        """
    def YAxis(self) -> gp_Ax1: 
        """
        Returns the "YAxis" of the ellipse whose unit vector is the "X Direction" or the "Y Direction" of the local coordinate system of this ellipse. This is the minor axis of the ellipse.

        Returns the "YAxis" of the ellipse whose unit vector is the "X Direction" or the "Y Direction" of the local coordinate system of this ellipse. This is the minor axis of the ellipse.
        """
    @overload
    def __init__(self,A2 : gp_Ax2,MajorRadius : float,MinorRadius : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Elips2d():
    """
    Describes an ellipse in the plane (2D space). An ellipse is defined by its major and minor radii and positioned in the plane with a coordinate system (a gp_Ax22d object) as follows: - the origin of the coordinate system is the center of the ellipse, - its "X Direction" defines the major axis of the ellipse, and - its "Y Direction" defines the minor axis of the ellipse. This coordinate system is the "local coordinate system" of the ellipse. Its orientation (direct or indirect) gives an implicit orientation to the ellipse. In this coordinate system, the equation of the ellipse is: X*X / (MajorRadius**2) + Y*Y / (MinorRadius**2) = 1.0 See Also gce_MakeElips2d which provides functions for more complex ellipse constructions Geom2d_Ellipse which provides additional functions for constructing ellipses and works, in particular, with the parametric equations of ellipses
    """
    def Area(self) -> float: 
        """
        Computes the area of the ellipse.

        Computes the area of the ellipse.
        """
    def Axis(self) -> gp_Ax22d: 
        """
        Returns the major axis of the ellipse.

        Returns the major axis of the ellipse.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float]: 
        """
        Returns the coefficients of the implicit equation of the ellipse. A * (X**2) + B * (Y**2) + 2*C*(X*Y) + 2*D*X + 2*E*Y + F = 0.
        """
    def Directrix1(self) -> gp_Ax2d: 
        """
        This directrix is the line normal to the XAxis of the ellipse in the local plane (Z = 0) at a distance d = MajorRadius / e from the center of the ellipse, where e is the eccentricity of the ellipse. This line is parallel to the "YAxis". The intersection point between directrix1 and the "XAxis" is the location point of the directrix1. This point is on the positive side of the "XAxis".

        This directrix is the line normal to the XAxis of the ellipse in the local plane (Z = 0) at a distance d = MajorRadius / e from the center of the ellipse, where e is the eccentricity of the ellipse. This line is parallel to the "YAxis". The intersection point between directrix1 and the "XAxis" is the location point of the directrix1. This point is on the positive side of the "XAxis".
        """
    def Directrix2(self) -> gp_Ax2d: 
        """
        This line is obtained by the symmetrical transformation of "Directrix1" with respect to the minor axis of the ellipse.

        This line is obtained by the symmetrical transformation of "Directrix1" with respect to the minor axis of the ellipse.
        """
    def Eccentricity(self) -> float: 
        """
        Returns the eccentricity of the ellipse between 0.0 and 1.0 If f is the distance between the center of the ellipse and the Focus1 then the eccentricity e = f / MajorRadius. Returns 0 if MajorRadius = 0.

        Returns the eccentricity of the ellipse between 0.0 and 1.0 If f is the distance between the center of the ellipse and the Focus1 then the eccentricity e = f / MajorRadius. Returns 0 if MajorRadius = 0.
        """
    def Focal(self) -> float: 
        """
        Returns the distance between the center of the ellipse and focus1 or focus2.

        Returns the distance between the center of the ellipse and focus1 or focus2.
        """
    def Focus1(self) -> gp_Pnt2d: 
        """
        Returns the first focus of the ellipse. This focus is on the positive side of the major axis of the ellipse.

        Returns the first focus of the ellipse. This focus is on the positive side of the major axis of the ellipse.
        """
    def Focus2(self) -> gp_Pnt2d: 
        """
        Returns the second focus of the ellipse. This focus is on the negative side of the major axis of the ellipse.

        Returns the second focus of the ellipse. This focus is on the negative side of the major axis of the ellipse.
        """
    def IsDirect(self) -> bool: 
        """
        Returns true if the local coordinate system is direct and false in the other case.

        Returns true if the local coordinate system is direct and false in the other case.
        """
    def Location(self) -> gp_Pnt2d: 
        """
        Returns the center of the ellipse.

        Returns the center of the ellipse.
        """
    def MajorRadius(self) -> float: 
        """
        Returns the major radius of the Ellipse.

        Returns the major radius of the Ellipse.
        """
    def MinorRadius(self) -> float: 
        """
        Returns the minor radius of the Ellipse.

        Returns the minor radius of the Ellipse.
        """
    @overload
    def Mirror(self,P : gp_Pnt2d) -> None: 
        """
        None

        None
        """
    @overload
    def Mirror(self,A : gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,P : gp_Pnt2d) -> gp_Elips2d: 
        """
        Performs the symmetrical transformation of a ellipse with respect to the point P which is the center of the symmetry

        Performs the symmetrical transformation of a ellipse with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirrored(self,A : gp_Ax2d) -> gp_Elips2d: ...
    def Parameter(self) -> float: 
        """
        Returns p = (1 - e * e) * MajorRadius where e is the eccentricity of the ellipse. Returns 0 if MajorRadius = 0

        Returns p = (1 - e * e) * MajorRadius where e is the eccentricity of the ellipse. Returns 0 if MajorRadius = 0
        """
    def Reverse(self) -> None: 
        """
        None

        None
        """
    def Reversed(self) -> gp_Elips2d: 
        """
        None

        None
        """
    def Rotate(self,P : gp_Pnt2d,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,P : gp_Pnt2d,Ang : float) -> gp_Elips2d: 
        """
        None

        None
        """
    def Scale(self,P : gp_Pnt2d,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt2d,S : float) -> gp_Elips2d: 
        """
        Scales a ellipse. S is the scaling value.

        Scales a ellipse. S is the scaling value.
        """
    def SetAxis(self,A : gp_Ax22d) -> None: 
        """
        Modifies this ellipse, by redefining its local coordinate system so that it becomes A.

        Modifies this ellipse, by redefining its local coordinate system so that it becomes A.
        """
    def SetLocation(self,P : gp_Pnt2d) -> None: 
        """
        Modifies this ellipse, by redefining its local coordinate system so that - its origin becomes P.

        Modifies this ellipse, by redefining its local coordinate system so that - its origin becomes P.
        """
    def SetMajorRadius(self,MajorRadius : float) -> None: 
        """
        Changes the value of the major radius. Raises ConstructionError if MajorRadius < MinorRadius.

        Changes the value of the major radius. Raises ConstructionError if MajorRadius < MinorRadius.
        """
    def SetMinorRadius(self,MinorRadius : float) -> None: 
        """
        Changes the value of the minor radius. Raises ConstructionError if MajorRadius < MinorRadius or MinorRadius < 0.0

        Changes the value of the minor radius. Raises ConstructionError if MajorRadius < MinorRadius or MinorRadius < 0.0
        """
    def SetXAxis(self,A : gp_Ax2d) -> None: 
        """
        Modifies this ellipse, by redefining its local coordinate system so that its origin and its "X Direction" become those of the axis A. The "Y Direction" is then recomputed. The orientation of the local coordinate system is not modified.

        Modifies this ellipse, by redefining its local coordinate system so that its origin and its "X Direction" become those of the axis A. The "Y Direction" is then recomputed. The orientation of the local coordinate system is not modified.
        """
    def SetYAxis(self,A : gp_Ax2d) -> None: 
        """
        Modifies this ellipse, by redefining its local coordinate system so that its origin and its "Y Direction" become those of the axis A. The "X Direction" is then recomputed. The orientation of the local coordinate system is not modified.

        Modifies this ellipse, by redefining its local coordinate system so that its origin and its "Y Direction" become those of the axis A. The "X Direction" is then recomputed. The orientation of the local coordinate system is not modified.
        """
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Elips2d: 
        """
        Transforms an ellipse with the transformation T from class Trsf2d.

        Transforms an ellipse with the transformation T from class Trsf2d.
        """
    @overload
    def Translate(self,V : gp_Vec2d) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> gp_Elips2d: 
        """
        Translates a ellipse in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a ellipse from the point P1 to the point P2.

        Translates a ellipse in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a ellipse from the point P1 to the point P2.
        """
    @overload
    def Translated(self,V : gp_Vec2d) -> gp_Elips2d: ...
    def XAxis(self) -> gp_Ax2d: 
        """
        Returns the major axis of the ellipse.

        Returns the major axis of the ellipse.
        """
    def YAxis(self) -> gp_Ax2d: 
        """
        Returns the minor axis of the ellipse. Reverses the direction of the circle.

        Returns the minor axis of the ellipse. Reverses the direction of the circle.
        """
    @overload
    def __init__(self,MajorAxis : gp_Ax2d,MajorRadius : float,MinorRadius : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,A : gp_Ax22d,MajorRadius : float,MinorRadius : float) -> None: ...
    pass
class gp_EulerSequence():
    """
    Enumerates all 24 possible variants of generalized Euler angles, defining general 3d rotation by three rotations around main axes of coordinate system, in different possible orders.

    Members:

      gp_EulerAngles

      gp_YawPitchRoll

      gp_Extrinsic_XYZ

      gp_Extrinsic_XZY

      gp_Extrinsic_YZX

      gp_Extrinsic_YXZ

      gp_Extrinsic_ZXY

      gp_Extrinsic_ZYX

      gp_Intrinsic_XYZ

      gp_Intrinsic_XZY

      gp_Intrinsic_YZX

      gp_Intrinsic_YXZ

      gp_Intrinsic_ZXY

      gp_Intrinsic_ZYX

      gp_Extrinsic_XYX

      gp_Extrinsic_XZX

      gp_Extrinsic_YZY

      gp_Extrinsic_YXY

      gp_Extrinsic_ZYZ

      gp_Extrinsic_ZXZ

      gp_Intrinsic_XYX

      gp_Intrinsic_XZX

      gp_Intrinsic_YZY

      gp_Intrinsic_YXY

      gp_Intrinsic_ZXZ

      gp_Intrinsic_ZYZ
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    __entries: dict # value = {'gp_EulerAngles': (gp_EulerSequence.gp_EulerAngles, None), 'gp_YawPitchRoll': (gp_EulerSequence.gp_YawPitchRoll, None), 'gp_Extrinsic_XYZ': (gp_EulerSequence.gp_Extrinsic_XYZ, None), 'gp_Extrinsic_XZY': (gp_EulerSequence.gp_Extrinsic_XZY, None), 'gp_Extrinsic_YZX': (gp_EulerSequence.gp_Extrinsic_YZX, None), 'gp_Extrinsic_YXZ': (gp_EulerSequence.gp_Extrinsic_YXZ, None), 'gp_Extrinsic_ZXY': (gp_EulerSequence.gp_Extrinsic_ZXY, None), 'gp_Extrinsic_ZYX': (gp_EulerSequence.gp_Extrinsic_ZYX, None), 'gp_Intrinsic_XYZ': (gp_EulerSequence.gp_Intrinsic_XYZ, None), 'gp_Intrinsic_XZY': (gp_EulerSequence.gp_Intrinsic_XZY, None), 'gp_Intrinsic_YZX': (gp_EulerSequence.gp_Intrinsic_YZX, None), 'gp_Intrinsic_YXZ': (gp_EulerSequence.gp_Intrinsic_YXZ, None), 'gp_Intrinsic_ZXY': (gp_EulerSequence.gp_Intrinsic_ZXY, None), 'gp_Intrinsic_ZYX': (gp_EulerSequence.gp_Intrinsic_ZYX, None), 'gp_Extrinsic_XYX': (gp_EulerSequence.gp_Extrinsic_XYX, None), 'gp_Extrinsic_XZX': (gp_EulerSequence.gp_Extrinsic_XZX, None), 'gp_Extrinsic_YZY': (gp_EulerSequence.gp_Extrinsic_YZY, None), 'gp_Extrinsic_YXY': (gp_EulerSequence.gp_Extrinsic_YXY, None), 'gp_Extrinsic_ZYZ': (gp_EulerSequence.gp_Extrinsic_ZYZ, None), 'gp_Extrinsic_ZXZ': (gp_EulerSequence.gp_Extrinsic_ZXZ, None), 'gp_Intrinsic_XYX': (gp_EulerSequence.gp_Intrinsic_XYX, None), 'gp_Intrinsic_XZX': (gp_EulerSequence.gp_Intrinsic_XZX, None), 'gp_Intrinsic_YZY': (gp_EulerSequence.gp_Intrinsic_YZY, None), 'gp_Intrinsic_YXY': (gp_EulerSequence.gp_Intrinsic_YXY, None), 'gp_Intrinsic_ZXZ': (gp_EulerSequence.gp_Intrinsic_ZXZ, None), 'gp_Intrinsic_ZYZ': (gp_EulerSequence.gp_Intrinsic_ZYZ, None)}
    __members__: dict # value = {'gp_EulerAngles': gp_EulerSequence.gp_EulerAngles, 'gp_YawPitchRoll': gp_EulerSequence.gp_YawPitchRoll, 'gp_Extrinsic_XYZ': gp_EulerSequence.gp_Extrinsic_XYZ, 'gp_Extrinsic_XZY': gp_EulerSequence.gp_Extrinsic_XZY, 'gp_Extrinsic_YZX': gp_EulerSequence.gp_Extrinsic_YZX, 'gp_Extrinsic_YXZ': gp_EulerSequence.gp_Extrinsic_YXZ, 'gp_Extrinsic_ZXY': gp_EulerSequence.gp_Extrinsic_ZXY, 'gp_Extrinsic_ZYX': gp_EulerSequence.gp_Extrinsic_ZYX, 'gp_Intrinsic_XYZ': gp_EulerSequence.gp_Intrinsic_XYZ, 'gp_Intrinsic_XZY': gp_EulerSequence.gp_Intrinsic_XZY, 'gp_Intrinsic_YZX': gp_EulerSequence.gp_Intrinsic_YZX, 'gp_Intrinsic_YXZ': gp_EulerSequence.gp_Intrinsic_YXZ, 'gp_Intrinsic_ZXY': gp_EulerSequence.gp_Intrinsic_ZXY, 'gp_Intrinsic_ZYX': gp_EulerSequence.gp_Intrinsic_ZYX, 'gp_Extrinsic_XYX': gp_EulerSequence.gp_Extrinsic_XYX, 'gp_Extrinsic_XZX': gp_EulerSequence.gp_Extrinsic_XZX, 'gp_Extrinsic_YZY': gp_EulerSequence.gp_Extrinsic_YZY, 'gp_Extrinsic_YXY': gp_EulerSequence.gp_Extrinsic_YXY, 'gp_Extrinsic_ZYZ': gp_EulerSequence.gp_Extrinsic_ZYZ, 'gp_Extrinsic_ZXZ': gp_EulerSequence.gp_Extrinsic_ZXZ, 'gp_Intrinsic_XYX': gp_EulerSequence.gp_Intrinsic_XYX, 'gp_Intrinsic_XZX': gp_EulerSequence.gp_Intrinsic_XZX, 'gp_Intrinsic_YZY': gp_EulerSequence.gp_Intrinsic_YZY, 'gp_Intrinsic_YXY': gp_EulerSequence.gp_Intrinsic_YXY, 'gp_Intrinsic_ZXZ': gp_EulerSequence.gp_Intrinsic_ZXZ, 'gp_Intrinsic_ZYZ': gp_EulerSequence.gp_Intrinsic_ZYZ}
    gp_EulerAngles: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_EulerAngles
    gp_Extrinsic_XYX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_XYX
    gp_Extrinsic_XYZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_XYZ
    gp_Extrinsic_XZX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_XZX
    gp_Extrinsic_XZY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_XZY
    gp_Extrinsic_YXY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_YXY
    gp_Extrinsic_YXZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_YXZ
    gp_Extrinsic_YZX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_YZX
    gp_Extrinsic_YZY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_YZY
    gp_Extrinsic_ZXY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_ZXY
    gp_Extrinsic_ZXZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_ZXZ
    gp_Extrinsic_ZYX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_ZYX
    gp_Extrinsic_ZYZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_ZYZ
    gp_Intrinsic_XYX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_XYX
    gp_Intrinsic_XYZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_XYZ
    gp_Intrinsic_XZX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_XZX
    gp_Intrinsic_XZY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_XZY
    gp_Intrinsic_YXY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_YXY
    gp_Intrinsic_YXZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_YXZ
    gp_Intrinsic_YZX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_YZX
    gp_Intrinsic_YZY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_YZY
    gp_Intrinsic_ZXY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_ZXY
    gp_Intrinsic_ZXZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_ZXZ
    gp_Intrinsic_ZYX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_ZYX
    gp_Intrinsic_ZYZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_ZYZ
    gp_YawPitchRoll: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_YawPitchRoll
    pass
class gp_GTrsf():
    """
    Defines a non-persistent transformation in 3D space. This transformation is a general transformation. It can be a Trsf from gp, an affinity, or you can define your own transformation giving the matrix of transformation.
    """
    def Form(self) -> gp_TrsfForm: 
        """
        Returns the nature of the transformation. It can be an identity transformation, a rotation, a translation, a mirror transformation (relative to a point, an axis or a plane), a scaling transformation, a compound transformation or some other type of transformation.

        Returns the nature of the transformation. It can be an identity transformation, a rotation, a translation, a mirror transformation (relative to a point, an axis or a plane), a scaling transformation, a compound transformation or some other type of transformation.
        """
    def Invert(self) -> None: 
        """
        None
        """
    def Inverted(self) -> gp_GTrsf: 
        """
        Computes the reverse transformation. Raises an exception if the matrix of the transformation is not inversible.

        Computes the reverse transformation. Raises an exception if the matrix of the transformation is not inversible.
        """
    def IsNegative(self) -> bool: 
        """
        Returns true if the determinant of the vectorial part of this transformation is negative.

        Returns true if the determinant of the vectorial part of this transformation is negative.
        """
    def IsSingular(self) -> bool: 
        """
        Returns true if this transformation is singular (and therefore, cannot be inverted). Note: The Gauss LU decomposition is used to invert the transformation matrix. Consequently, the transformation is considered as singular if the largest pivot found is less than or equal to gp::Resolution(). Warning If this transformation is singular, it cannot be inverted.

        Returns true if this transformation is singular (and therefore, cannot be inverted). Note: The Gauss LU decomposition is used to invert the transformation matrix. Consequently, the transformation is considered as singular if the largest pivot found is less than or equal to gp::Resolution(). Warning If this transformation is singular, it cannot be inverted.
        """
    def Multiplied(self,T : gp_GTrsf) -> gp_GTrsf: 
        """
        Computes the transformation composed from T and <me>. In a C++ implementation you can also write Tcomposed = <me> * T. Example : GTrsf T1, T2, Tcomp; ............... //composition : Tcomp = T2.Multiplied(T1); // or (Tcomp = T2 * T1) // transformation of a point XYZ P(10.,3.,4.); XYZ P1(P); Tcomp.Transforms(P1); //using Tcomp XYZ P2(P); T1.Transforms(P2); //using T1 then T2 T2.Transforms(P2); // P1 = P2 !!!

        Computes the transformation composed from T and <me>. In a C++ implementation you can also write Tcomposed = <me> * T. Example : GTrsf T1, T2, Tcomp; ............... //composition : Tcomp = T2.Multiplied(T1); // or (Tcomp = T2 * T1) // transformation of a point XYZ P(10.,3.,4.); XYZ P1(P); Tcomp.Transforms(P1); //using Tcomp XYZ P2(P); T1.Transforms(P2); //using T1 then T2 T2.Transforms(P2); // P1 = P2 !!!
        """
    def Multiply(self,T : gp_GTrsf) -> None: 
        """
        Computes the transformation composed with <me> and T. <me> = <me> * T
        """
    def Power(self,N : int) -> None: 
        """
        None
        """
    def Powered(self,N : int) -> gp_GTrsf: 
        """
        Computes: - the product of this transformation multiplied by itself N times, if N is positive, or - the product of the inverse of this transformation multiplied by itself |N| times, if N is negative. If N equals zero, the result is equal to the Identity transformation. I.e.: <me> * <me> * .......* <me>, N time. if N =0 <me> = Identity if N < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().

        Computes: - the product of this transformation multiplied by itself N times, if N is positive, or - the product of the inverse of this transformation multiplied by itself |N| times, if N is negative. If N equals zero, the result is equal to the Identity transformation. I.e.: <me> * <me> * .......* <me>, N time. if N =0 <me> = Identity if N < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().
        """
    def PreMultiply(self,T : gp_GTrsf) -> None: 
        """
        Computes the product of the transformation T and this transformation and assigns the result to this transformation. this = T * this
        """
    @overload
    def SetAffinity(self,A1 : gp_Ax1,Ratio : float) -> None: 
        """
        Changes this transformation into an affinity of ratio Ratio with respect to the axis A1. Note: an affinity is a point-by-point transformation that transforms any point P into a point P' such that if H is the orthogonal projection of P on the axis A1 or the plane A2, the vectors HP and HP' satisfy: HP' = Ratio * HP.

        Changes this transformation into an affinity of ratio Ratio with respect to the plane defined by the origin, the "X Direction" and the "Y Direction" of coordinate system A2. Note: an affinity is a point-by-point transformation that transforms any point P into a point P' such that if H is the orthogonal projection of P on the axis A1 or the plane A2, the vectors HP and HP' satisfy: HP' = Ratio * HP.

        Changes this transformation into an affinity of ratio Ratio with respect to the axis A1. Note: an affinity is a point-by-point transformation that transforms any point P into a point P' such that if H is the orthogonal projection of P on the axis A1 or the plane A2, the vectors HP and HP' satisfy: HP' = Ratio * HP.

        Changes this transformation into an affinity of ratio Ratio with respect to the plane defined by the origin, the "X Direction" and the "Y Direction" of coordinate system A2. Note: an affinity is a point-by-point transformation that transforms any point P into a point P' such that if H is the orthogonal projection of P on the axis A1 or the plane A2, the vectors HP and HP' satisfy: HP' = Ratio * HP.
        """
    @overload
    def SetAffinity(self,A2 : gp_Ax2,Ratio : float) -> None: ...
    def SetForm(self) -> None: 
        """
        verify and set the shape of the GTrsf Other or CompoundTrsf Ex : myGTrsf.SetValue(row1,col1,val1); myGTrsf.SetValue(row2,col2,val2); ... myGTrsf.SetForm();
        """
    def SetTranslationPart(self,Coord : gp_XYZ) -> None: 
        """
        Replaces the translation part of this transformation by the coordinates of the number triple Coord.
        """
    def SetTrsf(self,T : gp_Trsf) -> None: 
        """
        Assigns the vectorial and translation parts of T to this transformation.

        Assigns the vectorial and translation parts of T to this transformation.
        """
    def SetValue(self,Row : int,Col : int,Value : float) -> None: 
        """
        Replaces the coefficient (Row, Col) of the matrix representing this transformation by Value. Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 4

        Replaces the coefficient (Row, Col) of the matrix representing this transformation by Value. Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 4
        """
    def SetVectorialPart(self,Matrix : gp_Mat) -> None: 
        """
        Replaces the vectorial part of this transformation by Matrix.

        Replaces the vectorial part of this transformation by Matrix.
        """
    @overload
    def Transforms(self,Coord : gp_XYZ) -> None: 
        """
        None

        None

        Transforms a triplet XYZ with a GTrsf.

        Transforms a triplet XYZ with a GTrsf.
        """
    @overload
    def Transforms(self) -> Tuple[float, float, float]: ...
    def TranslationPart(self) -> gp_XYZ: 
        """
        Returns the translation part of the GTrsf.

        Returns the translation part of the GTrsf.
        """
    def Trsf(self) -> gp_Trsf: 
        """
        None

        None
        """
    def Value(self,Row : int,Col : int) -> float: 
        """
        Returns the coefficients of the global matrix of transformation. Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 4

        Returns the coefficients of the global matrix of transformation. Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 4
        """
    def VectorialPart(self) -> gp_Mat: 
        """
        Computes the vectorial part of the GTrsf. The returned Matrix is a 3*3 matrix.

        Computes the vectorial part of the GTrsf. The returned Matrix is a 3*3 matrix.
        """
    def __imul__(self,T : gp_GTrsf) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,M : gp_Mat,V : gp_XYZ) -> None: ...
    @overload
    def __init__(self,T : gp_Trsf) -> None: ...
    def __mul__(self,T : gp_GTrsf) -> gp_GTrsf: 
        """
        None
        """
    def __rmul__(self,T : gp_GTrsf) -> gp_GTrsf: 
        """
        None
        """
    pass
class gp_GTrsf2d():
    """
    Defines a non persistent transformation in 2D space. This transformation is a general transformation. It can be a Trsf2d from package gp, an affinity, or you can define your own transformation giving the corresponding matrix of transformation.
    """
    def Form(self) -> gp_TrsfForm: 
        """
        Returns the nature of the transformation. It can be an identity transformation, a rotation, a translation, a mirror transformation (relative to a point or axis), a scaling transformation, a compound transformation or some other type of transformation.

        Returns the nature of the transformation. It can be an identity transformation, a rotation, a translation, a mirror transformation (relative to a point or axis), a scaling transformation, a compound transformation or some other type of transformation.
        """
    def Invert(self) -> None: 
        """
        None
        """
    def Inverted(self) -> gp_GTrsf2d: 
        """
        Computes the reverse transformation. Raised an exception if the matrix of the transformation is not inversible.

        Computes the reverse transformation. Raised an exception if the matrix of the transformation is not inversible.
        """
    def IsNegative(self) -> bool: 
        """
        Returns true if the determinant of the vectorial part of this transformation is negative.

        Returns true if the determinant of the vectorial part of this transformation is negative.
        """
    def IsSingular(self) -> bool: 
        """
        Returns true if this transformation is singular (and therefore, cannot be inverted). Note: The Gauss LU decomposition is used to invert the transformation matrix. Consequently, the transformation is considered as singular if the largest pivot found is less than or equal to gp::Resolution(). Warning If this transformation is singular, it cannot be inverted.

        Returns true if this transformation is singular (and therefore, cannot be inverted). Note: The Gauss LU decomposition is used to invert the transformation matrix. Consequently, the transformation is considered as singular if the largest pivot found is less than or equal to gp::Resolution(). Warning If this transformation is singular, it cannot be inverted.
        """
    def Multiplied(self,T : gp_GTrsf2d) -> gp_GTrsf2d: 
        """
        Computes the transformation composed with T and <me>. In a C++ implementation you can also write Tcomposed = <me> * T. Example : GTrsf2d T1, T2, Tcomp; ............... //composition : Tcomp = T2.Multiplied(T1); // or (Tcomp = T2 * T1) // transformation of a point XY P(10.,3.); XY P1(P); Tcomp.Transforms(P1); //using Tcomp XY P2(P); T1.Transforms(P2); //using T1 then T2 T2.Transforms(P2); // P1 = P2 !!!

        Computes the transformation composed with T and <me>. In a C++ implementation you can also write Tcomposed = <me> * T. Example : GTrsf2d T1, T2, Tcomp; ............... //composition : Tcomp = T2.Multiplied(T1); // or (Tcomp = T2 * T1) // transformation of a point XY P(10.,3.); XY P1(P); Tcomp.Transforms(P1); //using Tcomp XY P2(P); T1.Transforms(P2); //using T1 then T2 T2.Transforms(P2); // P1 = P2 !!!
        """
    def Multiply(self,T : gp_GTrsf2d) -> None: 
        """
        None
        """
    def Power(self,N : int) -> None: 
        """
        None
        """
    def Powered(self,N : int) -> gp_GTrsf2d: 
        """
        Computes the following composition of transformations <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().

        Computes the following composition of transformations <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().
        """
    def PreMultiply(self,T : gp_GTrsf2d) -> None: 
        """
        Computes the product of the transformation T and this transformation, and assigns the result to this transformation: this = T * this
        """
    def SetAffinity(self,A : gp_Ax2d,Ratio : float) -> None: 
        """
        Changes this transformation into an affinity of ratio Ratio with respect to the axis A. Note: An affinity is a point-by-point transformation that transforms any point P into a point P' such that if H is the orthogonal projection of P on the axis A, the vectors HP and HP' satisfy: HP' = Ratio * HP.
        """
    def SetTranslationPart(self,Coord : gp_XY) -> None: 
        """
        Replacesthe translation part of this transformation by the coordinates of the number pair Coord.
        """
    def SetTrsf2d(self,T : gp_Trsf2d) -> None: 
        """
        Assigns the vectorial and translation parts of T to this transformation.

        Assigns the vectorial and translation parts of T to this transformation.
        """
    def SetValue(self,Row : int,Col : int,Value : float) -> None: 
        """
        Replaces the coefficient (Row, Col) of the matrix representing this transformation by Value, Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 3

        Replaces the coefficient (Row, Col) of the matrix representing this transformation by Value, Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 3
        """
    def SetVectorialPart(self,Matrix : gp_Mat2d) -> None: 
        """
        Replaces the vectorial part of this transformation by Matrix.

        Replaces the vectorial part of this transformation by Matrix.
        """
    def Transformed(self,Coord : gp_XY) -> gp_XY: 
        """
        None

        None
        """
    @overload
    def Transforms(self,Coord : gp_XY) -> None: 
        """
        None

        None

        Applies this transformation to the coordinates: - of the number pair Coord, or - X and Y.

        Applies this transformation to the coordinates: - of the number pair Coord, or - X and Y.
        """
    @overload
    def Transforms(self) -> Tuple[float, float]: ...
    def TranslationPart(self) -> gp_XY: 
        """
        Returns the translation part of the GTrsf2d.

        Returns the translation part of the GTrsf2d.
        """
    def Trsf2d(self) -> gp_Trsf2d: 
        """
        Converts this transformation into a gp_Trsf2d transformation. Exceptions Standard_ConstructionError if this transformation cannot be converted, i.e. if its form is gp_Other.
        """
    def Value(self,Row : int,Col : int) -> float: 
        """
        Returns the coefficients of the global matrix of transformation. Raised OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 3

        Returns the coefficients of the global matrix of transformation. Raised OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 3
        """
    def VectorialPart(self) -> gp_Mat2d: 
        """
        Computes the vectorial part of the GTrsf2d. The returned Matrix is a 2*2 matrix.

        Computes the vectorial part of the GTrsf2d. The returned Matrix is a 2*2 matrix.
        """
    def __imul__(self,T : gp_GTrsf2d) -> None: 
        """
        None
        """
    @overload
    def __init__(self,T : gp_Trsf2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,M : gp_Mat2d,V : gp_XY) -> None: ...
    def __mul__(self,T : gp_GTrsf2d) -> gp_GTrsf2d: 
        """
        None
        """
    def __rmul__(self,T : gp_GTrsf2d) -> gp_GTrsf2d: 
        """
        None
        """
    pass
class gp_Hypr():
    """
    Describes a branch of a hyperbola in 3D space. A hyperbola is defined by its major and minor radii and positioned in space with a coordinate system (a gp_Ax2 object) of which: - the origin is the center of the hyperbola, - the "X Direction" defines the major axis of the hyperbola, and - the "Y Direction" defines the minor axis of the hyperbola. The origin, "X Direction" and "Y Direction" of this coordinate system together define the plane of the hyperbola. This coordinate system is the "local coordinate system" of the hyperbola. In this coordinate system, the equation of the hyperbola is: X*X/(MajorRadius**2)-Y*Y/(MinorRadius**2) = 1.0 The branch of the hyperbola described is the one located on the positive side of the major axis. The "main Direction" of the local coordinate system is a normal vector to the plane of the hyperbola. This vector gives an implicit orientation to the hyperbola. We refer to the "main Axis" of the local coordinate system as the "Axis" of the hyperbola. The following schema shows the plane of the hyperbola, and in it, the respective positions of the three branches of hyperbolas constructed with the functions OtherBranch, ConjugateBranch1, and ConjugateBranch2:
    """
    def Asymptote1(self) -> gp_Ax1: 
        """
        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = (B/A)*X where A is the major radius and B is the minor radius. Raises ConstructionError if MajorRadius = 0.0

        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = (B/A)*X where A is the major radius and B is the minor radius. Raises ConstructionError if MajorRadius = 0.0
        """
    def Asymptote2(self) -> gp_Ax1: 
        """
        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = -(B/A)*X. where A is the major radius and B is the minor radius. Raises ConstructionError if MajorRadius = 0.0

        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = -(B/A)*X. where A is the major radius and B is the minor radius. Raises ConstructionError if MajorRadius = 0.0
        """
    def Axis(self) -> gp_Ax1: 
        """
        Returns the axis passing through the center, and normal to the plane of this hyperbola.

        Returns the axis passing through the center, and normal to the plane of this hyperbola.
        """
    def ConjugateBranch1(self) -> gp_Hypr: 
        """
        Computes the branch of hyperbola which is on the positive side of the "YAxis" of <me>.

        Computes the branch of hyperbola which is on the positive side of the "YAxis" of <me>.
        """
    def ConjugateBranch2(self) -> gp_Hypr: 
        """
        Computes the branch of hyperbola which is on the negative side of the "YAxis" of <me>.

        Computes the branch of hyperbola which is on the negative side of the "YAxis" of <me>.
        """
    def Directrix1(self) -> gp_Ax1: 
        """
        This directrix is the line normal to the XAxis of the hyperbola in the local plane (Z = 0) at a distance d = MajorRadius / e from the center of the hyperbola, where e is the eccentricity of the hyperbola. This line is parallel to the "YAxis". The intersection point between the directrix1 and the "XAxis" is the "Location" point of the directrix1. This point is on the positive side of the "XAxis".

        This directrix is the line normal to the XAxis of the hyperbola in the local plane (Z = 0) at a distance d = MajorRadius / e from the center of the hyperbola, where e is the eccentricity of the hyperbola. This line is parallel to the "YAxis". The intersection point between the directrix1 and the "XAxis" is the "Location" point of the directrix1. This point is on the positive side of the "XAxis".
        """
    def Directrix2(self) -> gp_Ax1: 
        """
        This line is obtained by the symmetrical transformation of "Directrix1" with respect to the "YAxis" of the hyperbola.

        This line is obtained by the symmetrical transformation of "Directrix1" with respect to the "YAxis" of the hyperbola.
        """
    def Eccentricity(self) -> float: 
        """
        Returns the excentricity of the hyperbola (e > 1). If f is the distance between the location of the hyperbola and the Focus1 then the eccentricity e = f / MajorRadius. Raises DomainError if MajorRadius = 0.0

        Returns the excentricity of the hyperbola (e > 1). If f is the distance between the location of the hyperbola and the Focus1 then the eccentricity e = f / MajorRadius. Raises DomainError if MajorRadius = 0.0
        """
    def Focal(self) -> float: 
        """
        Computes the focal distance. It is the distance between the the two focus of the hyperbola.

        Computes the focal distance. It is the distance between the the two focus of the hyperbola.
        """
    def Focus1(self) -> gp_Pnt: 
        """
        Returns the first focus of the hyperbola. This focus is on the positive side of the "XAxis" of the hyperbola.

        Returns the first focus of the hyperbola. This focus is on the positive side of the "XAxis" of the hyperbola.
        """
    def Focus2(self) -> gp_Pnt: 
        """
        Returns the second focus of the hyperbola. This focus is on the negative side of the "XAxis" of the hyperbola.

        Returns the second focus of the hyperbola. This focus is on the negative side of the "XAxis" of the hyperbola.
        """
    def Location(self) -> gp_Pnt: 
        """
        Returns the location point of the hyperbola. It is the intersection point between the "XAxis" and the "YAxis".

        Returns the location point of the hyperbola. It is the intersection point between the "XAxis" and the "YAxis".
        """
    def MajorRadius(self) -> float: 
        """
        Returns the major radius of the hyperbola. It is the radius on the "XAxis" of the hyperbola.

        Returns the major radius of the hyperbola. It is the radius on the "XAxis" of the hyperbola.
        """
    def MinorRadius(self) -> float: 
        """
        Returns the minor radius of the hyperbola. It is the radius on the "YAxis" of the hyperbola.

        Returns the minor radius of the hyperbola. It is the radius on the "YAxis" of the hyperbola.
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Hypr: 
        """
        Performs the symmetrical transformation of an hyperbola with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of an hyperbola with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of an hyperbola with respect to a plane. The axis placement A2 locates the plane of the symmetry (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Hypr: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Hypr: ...
    def OtherBranch(self) -> gp_Hypr: 
        """
        Returns the branch of hyperbola obtained by doing the symmetrical transformation of <me> with respect to the "YAxis" of <me>.

        Returns the branch of hyperbola obtained by doing the symmetrical transformation of <me> with respect to the "YAxis" of <me>.
        """
    def Parameter(self) -> float: 
        """
        Returns p = (e * e - 1) * MajorRadius where e is the eccentricity of the hyperbola. Raises DomainError if MajorRadius = 0.0

        Returns p = (e * e - 1) * MajorRadius where e is the eccentricity of the hyperbola. Raises DomainError if MajorRadius = 0.0
        """
    def Position(self) -> gp_Ax2: 
        """
        Returns the coordinate system of the hyperbola.

        Returns the coordinate system of the hyperbola.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Hypr: 
        """
        Rotates an hyperbola. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates an hyperbola. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Hypr: 
        """
        Scales an hyperbola. S is the scaling value.

        Scales an hyperbola. S is the scaling value.
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Modifies this hyperbola, by redefining its local coordinate system so that: - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed in the same way as for any gp_Ax2). Raises ConstructionError if the direction of A1 is parallel to the direction of the "XAxis" of the hyperbola.

        Modifies this hyperbola, by redefining its local coordinate system so that: - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed in the same way as for any gp_Ax2). Raises ConstructionError if the direction of A1 is parallel to the direction of the "XAxis" of the hyperbola.
        """
    def SetLocation(self,P : gp_Pnt) -> None: 
        """
        Modifies this hyperbola, by redefining its local coordinate system so that its origin becomes P.

        Modifies this hyperbola, by redefining its local coordinate system so that its origin becomes P.
        """
    @overload
    def SetMajorRadius(self,R : float) -> None: 
        """
        Modifies the major radius of this hyperbola. Exceptions Standard_ConstructionError if MajorRadius is negative.

        Modifies the major radius of this hyperbola. Exceptions Standard_ConstructionError if MajorRadius is negative.
        """
    @overload
    def SetMajorRadius(self,MajorRadius : float) -> None: ...
    @overload
    def SetMinorRadius(self,R : float) -> None: 
        """
        Modifies the minor radius of this hyperbola. Exceptions Standard_ConstructionError if MinorRadius is negative.

        Modifies the minor radius of this hyperbola. Exceptions Standard_ConstructionError if MinorRadius is negative.
        """
    @overload
    def SetMinorRadius(self,MinorRadius : float) -> None: ...
    def SetPosition(self,A2 : gp_Ax2) -> None: 
        """
        Modifies this hyperbola, by redefining its local coordinate system so that it becomes A2.

        Modifies this hyperbola, by redefining its local coordinate system so that it becomes A2.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Hypr: 
        """
        Transforms an hyperbola with the transformation T from class Trsf.

        Transforms an hyperbola with the transformation T from class Trsf.
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: ...
    @overload
    def Translated(self,V : gp_Vec) -> gp_Hypr: 
        """
        Translates an hyperbola in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates an hyperbola from the point P1 to the point P2.

        Translates an hyperbola in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates an hyperbola from the point P1 to the point P2.
        """
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Hypr: ...
    def XAxis(self) -> gp_Ax1: 
        """
        Computes an axis, whose - the origin is the center of this hyperbola, and - the unit vector is the "X Direction" of the local coordinate system of this hyperbola. These axes are, the major axis (the "X Axis") and of this hyperboReturns the "XAxis" of the hyperbola.

        Computes an axis, whose - the origin is the center of this hyperbola, and - the unit vector is the "X Direction" of the local coordinate system of this hyperbola. These axes are, the major axis (the "X Axis") and of this hyperboReturns the "XAxis" of the hyperbola.
        """
    def YAxis(self) -> gp_Ax1: 
        """
        Computes an axis, whose - the origin is the center of this hyperbola, and - the unit vector is the "Y Direction" of the local coordinate system of this hyperbola. These axes are the minor axis (the "Y Axis") of this hyperbola

        Computes an axis, whose - the origin is the center of this hyperbola, and - the unit vector is the "Y Direction" of the local coordinate system of this hyperbola. These axes are the minor axis (the "Y Axis") of this hyperbola
        """
    @overload
    def __init__(self,A2 : gp_Ax2,MajorRadius : float,MinorRadius : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Hypr2d():
    """
    Describes a branch of a hyperbola in the plane (2D space). A hyperbola is defined by its major and minor radii, and positioned in the plane with a coordinate system (a gp_Ax22d object) of which: - the origin is the center of the hyperbola, - the "X Direction" defines the major axis of the hyperbola, and - the "Y Direction" defines the minor axis of the hyperbola. This coordinate system is the "local coordinate system" of the hyperbola. The orientation of this coordinate system (direct or indirect) gives an implicit orientation to the hyperbola. In this coordinate system, the equation of the hyperbola is: X*X/(MajorRadius**2)-Y*Y/(MinorRadius**2) = 1.0 The branch of the hyperbola described is the one located on the positive side of the major axis. The following schema shows the plane of the hyperbola, and in it, the respective positions of the three branches of hyperbolas constructed with the functions OtherBranch, ConjugateBranch1, and ConjugateBranch2: ^YAxis | FirstConjugateBranch | Other | Main --------------------- C ------------------------------>XAxis Branch | Branch | | SecondConjugateBranch |
    """
    def Asymptote1(self) -> gp_Ax2d: 
        """
        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = (B/A)*X where A is the major radius of the hyperbola and B the minor radius of the hyperbola. Raises ConstructionError if MajorRadius = 0.0

        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = (B/A)*X where A is the major radius of the hyperbola and B the minor radius of the hyperbola. Raises ConstructionError if MajorRadius = 0.0
        """
    def Asymptote2(self) -> gp_Ax2d: 
        """
        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = -(B/A)*X where A is the major radius of the hyperbola and B the minor radius of the hyperbola. Raises ConstructionError if MajorRadius = 0.0

        In the local coordinate system of the hyperbola the equation of the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the equation of the first asymptote is Y = -(B/A)*X where A is the major radius of the hyperbola and B the minor radius of the hyperbola. Raises ConstructionError if MajorRadius = 0.0
        """
    def Axis(self) -> gp_Ax22d: 
        """
        Returns the axisplacement of the hyperbola.

        Returns the axisplacement of the hyperbola.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float]: 
        """
        Computes the coefficients of the implicit equation of the hyperbola : A * (X**2) + B * (Y**2) + 2*C*(X*Y) + 2*D*X + 2*E*Y + F = 0.
        """
    def ConjugateBranch1(self) -> gp_Hypr2d: 
        """
        Computes the branch of hyperbola which is on the positive side of the "YAxis" of <me>.

        Computes the branch of hyperbola which is on the positive side of the "YAxis" of <me>.
        """
    def ConjugateBranch2(self) -> gp_Hypr2d: 
        """
        Computes the branch of hyperbola which is on the negative side of the "YAxis" of <me>.

        Computes the branch of hyperbola which is on the negative side of the "YAxis" of <me>.
        """
    def Directrix1(self) -> gp_Ax2d: 
        """
        Computes the directrix which is the line normal to the XAxis of the hyperbola in the local plane (Z = 0) at a distance d = MajorRadius / e from the center of the hyperbola, where e is the eccentricity of the hyperbola. This line is parallel to the "YAxis". The intersection point between the "Directrix1" and the "XAxis" is the "Location" point of the "Directrix1". This point is on the positive side of the "XAxis".

        Computes the directrix which is the line normal to the XAxis of the hyperbola in the local plane (Z = 0) at a distance d = MajorRadius / e from the center of the hyperbola, where e is the eccentricity of the hyperbola. This line is parallel to the "YAxis". The intersection point between the "Directrix1" and the "XAxis" is the "Location" point of the "Directrix1". This point is on the positive side of the "XAxis".
        """
    def Directrix2(self) -> gp_Ax2d: 
        """
        This line is obtained by the symmetrical transformation of "Directrix1" with respect to the "YAxis" of the hyperbola.

        This line is obtained by the symmetrical transformation of "Directrix1" with respect to the "YAxis" of the hyperbola.
        """
    def Eccentricity(self) -> float: 
        """
        Returns the excentricity of the hyperbola (e > 1). If f is the distance between the location of the hyperbola and the Focus1 then the eccentricity e = f / MajorRadius. Raises DomainError if MajorRadius = 0.0.

        Returns the excentricity of the hyperbola (e > 1). If f is the distance between the location of the hyperbola and the Focus1 then the eccentricity e = f / MajorRadius. Raises DomainError if MajorRadius = 0.0.
        """
    def Focal(self) -> float: 
        """
        Computes the focal distance. It is the distance between the "Location" of the hyperbola and "Focus1" or "Focus2".

        Computes the focal distance. It is the distance between the "Location" of the hyperbola and "Focus1" or "Focus2".
        """
    def Focus1(self) -> gp_Pnt2d: 
        """
        Returns the first focus of the hyperbola. This focus is on the positive side of the "XAxis" of the hyperbola.

        Returns the first focus of the hyperbola. This focus is on the positive side of the "XAxis" of the hyperbola.
        """
    def Focus2(self) -> gp_Pnt2d: 
        """
        Returns the second focus of the hyperbola. This focus is on the negative side of the "XAxis" of the hyperbola.

        Returns the second focus of the hyperbola. This focus is on the negative side of the "XAxis" of the hyperbola.
        """
    def IsDirect(self) -> bool: 
        """
        Returns true if the local coordinate system is direct and false in the other case.

        Returns true if the local coordinate system is direct and false in the other case.
        """
    def Location(self) -> gp_Pnt2d: 
        """
        Returns the location point of the hyperbola. It is the intersection point between the "XAxis" and the "YAxis".

        Returns the location point of the hyperbola. It is the intersection point between the "XAxis" and the "YAxis".
        """
    def MajorRadius(self) -> float: 
        """
        Returns the major radius of the hyperbola (it is the radius corresponding to the "XAxis" of the hyperbola).

        Returns the major radius of the hyperbola (it is the radius corresponding to the "XAxis" of the hyperbola).
        """
    def MinorRadius(self) -> float: 
        """
        Returns the minor radius of the hyperbola (it is the radius corresponding to the "YAxis" of the hyperbola).

        Returns the minor radius of the hyperbola (it is the radius corresponding to the "YAxis" of the hyperbola).
        """
    @overload
    def Mirror(self,P : gp_Pnt2d) -> None: 
        """
        None

        None
        """
    @overload
    def Mirror(self,A : gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,A : gp_Ax2d) -> gp_Hypr2d: 
        """
        Performs the symmetrical transformation of an hyperbola with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of an hyperbola with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirrored(self,P : gp_Pnt2d) -> gp_Hypr2d: ...
    def OtherBranch(self) -> gp_Hypr2d: 
        """
        Returns the branch of hyperbola obtained by doing the symmetrical transformation of <me> with respect to the "YAxis" of <me>.

        Returns the branch of hyperbola obtained by doing the symmetrical transformation of <me> with respect to the "YAxis" of <me>.
        """
    def Parameter(self) -> float: 
        """
        Returns p = (e * e - 1) * MajorRadius where e is the eccentricity of the hyperbola. Raises DomainError if MajorRadius = 0.0

        Returns p = (e * e - 1) * MajorRadius where e is the eccentricity of the hyperbola. Raises DomainError if MajorRadius = 0.0
        """
    def Reverse(self) -> None: 
        """
        None

        None
        """
    def Reversed(self) -> gp_Hypr2d: 
        """
        Reverses the orientation of the local coordinate system of this hyperbola (the "Y Axis" is reversed). Therefore, the implicit orientation of this hyperbola is reversed. Note: - Reverse assigns the result to this hyperbola, while - Reversed creates a new one.

        Reverses the orientation of the local coordinate system of this hyperbola (the "Y Axis" is reversed). Therefore, the implicit orientation of this hyperbola is reversed. Note: - Reverse assigns the result to this hyperbola, while - Reversed creates a new one.
        """
    def Rotate(self,P : gp_Pnt2d,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,P : gp_Pnt2d,Ang : float) -> gp_Hypr2d: 
        """
        Rotates an hyperbola. P is the center of the rotation. Ang is the angular value of the rotation in radians.

        Rotates an hyperbola. P is the center of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt2d,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt2d,S : float) -> gp_Hypr2d: 
        """
        Scales an hyperbola. <S> is the scaling value. If <S> is positive only the location point is modified. But if <S> is negative the "XAxis" is reversed and the "YAxis" too.

        Scales an hyperbola. <S> is the scaling value. If <S> is positive only the location point is modified. But if <S> is negative the "XAxis" is reversed and the "YAxis" too.
        """
    def SetAxis(self,A : gp_Ax22d) -> None: 
        """
        Modifies this hyperbola, by redefining its local coordinate system so that it becomes A.

        Modifies this hyperbola, by redefining its local coordinate system so that it becomes A.
        """
    def SetLocation(self,P : gp_Pnt2d) -> None: 
        """
        Modifies this hyperbola, by redefining its local coordinate system so that its origin becomes P.

        Modifies this hyperbola, by redefining its local coordinate system so that its origin becomes P.
        """
    def SetMajorRadius(self,MajorRadius : float) -> None: 
        """
        Modifies the major or minor radius of this hyperbola. Exceptions Standard_ConstructionError if MajorRadius or MinorRadius is negative.

        Modifies the major or minor radius of this hyperbola. Exceptions Standard_ConstructionError if MajorRadius or MinorRadius is negative.
        """
    def SetMinorRadius(self,MinorRadius : float) -> None: 
        """
        Modifies the major or minor radius of this hyperbola. Exceptions Standard_ConstructionError if MajorRadius or MinorRadius is negative.

        Modifies the major or minor radius of this hyperbola. Exceptions Standard_ConstructionError if MajorRadius or MinorRadius is negative.
        """
    def SetXAxis(self,A : gp_Ax2d) -> None: 
        """
        Changes the major axis of the hyperbola. The minor axis is recomputed and the location of the hyperbola too.

        Changes the major axis of the hyperbola. The minor axis is recomputed and the location of the hyperbola too.
        """
    def SetYAxis(self,A : gp_Ax2d) -> None: 
        """
        Changes the minor axis of the hyperbola.The minor axis is recomputed and the location of the hyperbola too.

        Changes the minor axis of the hyperbola.The minor axis is recomputed and the location of the hyperbola too.
        """
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Hypr2d: 
        """
        Transforms an hyperbola with the transformation T from class Trsf2d.

        Transforms an hyperbola with the transformation T from class Trsf2d.
        """
    @overload
    def Translate(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec2d) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> gp_Hypr2d: 
        """
        Translates an hyperbola in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates an hyperbola from the point P1 to the point P2.

        Translates an hyperbola in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates an hyperbola from the point P1 to the point P2.
        """
    @overload
    def Translated(self,V : gp_Vec2d) -> gp_Hypr2d: ...
    def XAxis(self) -> gp_Ax2d: 
        """
        Computes an axis whose - the origin is the center of this hyperbola, and - the unit vector is the "X Direction" or "Y Direction" respectively of the local coordinate system of this hyperbola Returns the major axis of the hyperbola.

        Computes an axis whose - the origin is the center of this hyperbola, and - the unit vector is the "X Direction" or "Y Direction" respectively of the local coordinate system of this hyperbola Returns the major axis of the hyperbola.
        """
    def YAxis(self) -> gp_Ax2d: 
        """
        Computes an axis whose - the origin is the center of this hyperbola, and - the unit vector is the "X Direction" or "Y Direction" respectively of the local coordinate system of this hyperbola Returns the minor axis of the hyperbola.

        Computes an axis whose - the origin is the center of this hyperbola, and - the unit vector is the "X Direction" or "Y Direction" respectively of the local coordinate system of this hyperbola Returns the minor axis of the hyperbola.
        """
    @overload
    def __init__(self,A : gp_Ax22d,MajorRadius : float,MinorRadius : float) -> None: ...
    @overload
    def __init__(self,MajorAxis : gp_Ax2d,MajorRadius : float,MinorRadius : float,Sense : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Lin():
    """
    Describes a line in 3D space. A line is positioned in space with an axis (a gp_Ax1 object) which gives it an origin and a unit vector. A line and an axis are similar objects, thus, we can convert one into the other. A line provides direct access to the majority of the edit and query functions available on its positioning axis. In addition, however, a line has specific functions for computing distances and positions. See Also gce_MakeLin which provides functions for more complex line constructions Geom_Line which provides additional functions for constructing lines and works, in particular, with the parametric equations of lines
    """
    def Angle(self,Other : gp_Lin) -> float: 
        """
        Computes the angle between two lines in radians.

        Computes the angle between two lines in radians.
        """
    def Contains(self,P : gp_Pnt,LinearTolerance : float) -> bool: 
        """
        Returns true if this line contains the point P, that is, if the distance between point P and this line is less than or equal to LinearTolerance..

        Returns true if this line contains the point P, that is, if the distance between point P and this line is less than or equal to LinearTolerance..
        """
    def Direction(self) -> gp_Dir: 
        """
        Returns the direction of the line.

        Returns the direction of the line.
        """
    @overload
    def Distance(self,Other : gp_Lin) -> float: 
        """
        Computes the distance between <me> and the point P.

        Computes the distance between two lines.

        Computes the distance between <me> and the point P.
        """
    @overload
    def Distance(self,P : gp_Pnt) -> float: ...
    def Location(self) -> gp_Pnt: 
        """
        Returns the location point (origin) of the line.

        Returns the location point (origin) of the line.
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Lin: 
        """
        Performs the symmetrical transformation of a line with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a line with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a line with respect to a plane. The axis placement <A2> locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Lin: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Lin: ...
    def Normal(self,P : gp_Pnt) -> gp_Lin: 
        """
        Computes the line normal to the direction of <me>, passing through the point P. Raises ConstructionError if the distance between <me> and the point P is lower or equal to Resolution from gp because there is an infinity of solutions in 3D space.

        Computes the line normal to the direction of <me>, passing through the point P. Raises ConstructionError if the distance between <me> and the point P is lower or equal to Resolution from gp because there is an infinity of solutions in 3D space.
        """
    def Position(self) -> gp_Ax1: 
        """
        Returns the axis placement one axis whith the same location and direction as <me>.

        Returns the axis placement one axis whith the same location and direction as <me>.
        """
    def Reverse(self) -> None: 
        """
        None

        None
        """
    def Reversed(self) -> gp_Lin: 
        """
        Reverses the direction of the line. Note: - Reverse assigns the result to this line, while - Reversed creates a new one.

        Reverses the direction of the line. Note: - Reverse assigns the result to this line, while - Reversed creates a new one.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Lin: 
        """
        Rotates a line. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a line. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Lin: 
        """
        Scales a line. S is the scaling value. The "Location" point (origin) of the line is modified. The "Direction" is reversed if the scale is negative.

        Scales a line. S is the scaling value. The "Location" point (origin) of the line is modified. The "Direction" is reversed if the scale is negative.
        """
    def SetDirection(self,V : gp_Dir) -> None: 
        """
        Changes the direction of the line.

        Changes the direction of the line.
        """
    def SetLocation(self,P : gp_Pnt) -> None: 
        """
        Changes the location point (origin) of the line.

        Changes the location point (origin) of the line.
        """
    def SetPosition(self,A1 : gp_Ax1) -> None: 
        """
        Complete redefinition of the line. The "Location" point of <A1> is the origin of the line. The "Direction" of <A1> is the direction of the line.

        Complete redefinition of the line. The "Location" point of <A1> is the origin of the line. The "Direction" of <A1> is the direction of the line.
        """
    @overload
    def SquareDistance(self,Other : gp_Lin) -> float: 
        """
        Computes the square distance between <me> and the point P.

        Computes the square distance between two lines.

        Computes the square distance between <me> and the point P.

        Computes the square distance between two lines.
        """
    @overload
    def SquareDistance(self,P : gp_Pnt) -> float: ...
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Lin: 
        """
        Transforms a line with the transformation T from class Trsf.

        Transforms a line with the transformation T from class Trsf.
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: ...
    @overload
    def Translated(self,V : gp_Vec) -> gp_Lin: 
        """
        Translates a line in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a line from the point P1 to the point P2.

        Translates a line in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a line from the point P1 to the point P2.
        """
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Lin: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : gp_Pnt,V : gp_Dir) -> None: ...
    @overload
    def __init__(self,A1 : gp_Ax1) -> None: ...
    pass
class gp_Lin2d():
    """
    Describes a line in 2D space. A line is positioned in the plane with an axis (a gp_Ax2d object) which gives the line its origin and unit vector. A line and an axis are similar objects, thus, we can convert one into the other. A line provides direct access to the majority of the edit and query functions available on its positioning axis. In addition, however, a line has specific functions for computing distances and positions. See Also GccAna and Geom2dGcc packages which provide functions for constructing lines defined by geometric constraints gce_MakeLin2d which provides functions for more complex line constructions Geom2d_Line which provides additional functions for constructing lines and works, in particular, with the parametric equations of lines
    """
    def Angle(self,Other : gp_Lin2d) -> float: 
        """
        Computes the angle between two lines in radians.

        Computes the angle between two lines in radians.
        """
    def Coefficients(self) -> Tuple[float, float, float]: 
        """
        Returns the normalized coefficients of the line : A * X + B * Y + C = 0.

        Returns the normalized coefficients of the line : A * X + B * Y + C = 0.
        """
    def Contains(self,P : gp_Pnt2d,LinearTolerance : float) -> bool: 
        """
        Returns true if this line contains the point P, that is, if the distance between point P and this line is less than or equal to LinearTolerance.

        Returns true if this line contains the point P, that is, if the distance between point P and this line is less than or equal to LinearTolerance.
        """
    def Direction(self) -> gp_Dir2d: 
        """
        Returns the direction of the line.

        Returns the direction of the line.
        """
    @overload
    def Distance(self,P : gp_Pnt2d) -> float: 
        """
        Computes the distance between <me> and the point <P>.

        Computes the distance between two lines.

        Computes the distance between <me> and the point <P>.

        Computes the distance between two lines.
        """
    @overload
    def Distance(self,Other : gp_Lin2d) -> float: ...
    def Location(self) -> gp_Pnt2d: 
        """
        Returns the location point (origin) of the line.

        Returns the location point (origin) of the line.
        """
    @overload
    def Mirror(self,A : gp_Ax2d) -> None: 
        """
        None

        None
        """
    @overload
    def Mirror(self,P : gp_Pnt2d) -> None: ...
    @overload
    def Mirrored(self,A : gp_Ax2d) -> gp_Lin2d: 
        """
        Performs the symmetrical transformation of a line with respect to the point <P> which is the center of the symmetry

        Performs the symmetrical transformation of a line with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirrored(self,P : gp_Pnt2d) -> gp_Lin2d: ...
    def Normal(self,P : gp_Pnt2d) -> gp_Lin2d: 
        """
        Computes the line normal to the direction of <me>, passing through the point <P>.

        Computes the line normal to the direction of <me>, passing through the point <P>.
        """
    def Position(self) -> gp_Ax2d: 
        """
        Returns the axis placement one axis whith the same location and direction as <me>.

        Returns the axis placement one axis whith the same location and direction as <me>.
        """
    def Reverse(self) -> None: 
        """
        None

        None
        """
    def Reversed(self) -> gp_Lin2d: 
        """
        Reverses the positioning axis of this line. Note: - Reverse assigns the result to this line, while - Reversed creates a new one.

        Reverses the positioning axis of this line. Note: - Reverse assigns the result to this line, while - Reversed creates a new one.
        """
    def Rotate(self,P : gp_Pnt2d,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,P : gp_Pnt2d,Ang : float) -> gp_Lin2d: 
        """
        Rotates a line. P is the center of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a line. P is the center of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt2d,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt2d,S : float) -> gp_Lin2d: 
        """
        Scales a line. S is the scaling value. Only the origin of the line is modified.

        Scales a line. S is the scaling value. Only the origin of the line is modified.
        """
    def SetDirection(self,V : gp_Dir2d) -> None: 
        """
        Changes the direction of the line.

        Changes the direction of the line.
        """
    def SetLocation(self,P : gp_Pnt2d) -> None: 
        """
        Changes the origin of the line.

        Changes the origin of the line.
        """
    def SetPosition(self,A : gp_Ax2d) -> None: 
        """
        Complete redefinition of the line. The "Location" point of <A> is the origin of the line. The "Direction" of <A> is the direction of the line.

        Complete redefinition of the line. The "Location" point of <A> is the origin of the line. The "Direction" of <A> is the direction of the line.
        """
    @overload
    def SquareDistance(self,Other : gp_Lin2d) -> float: 
        """
        Computes the square distance between <me> and the point <P>.

        Computes the square distance between two lines.

        Computes the square distance between <me> and the point <P>.

        Computes the square distance between two lines.
        """
    @overload
    def SquareDistance(self,P : gp_Pnt2d) -> float: ...
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Lin2d: 
        """
        Transforms a line with the transformation T from class Trsf2d.

        Transforms a line with the transformation T from class Trsf2d.
        """
    @overload
    def Translate(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec2d) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> gp_Lin2d: 
        """
        Translates a line in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a line from the point P1 to the point P2.

        Translates a line in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a line from the point P1 to the point P2.
        """
    @overload
    def Translated(self,V : gp_Vec2d) -> gp_Lin2d: ...
    @overload
    def __init__(self,P : gp_Pnt2d,V : gp_Dir2d) -> None: ...
    @overload
    def __init__(self,A : float,B : float,C : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,A : gp_Ax2d) -> None: ...
    pass
class gp_Mat():
    """
    Describes a three column, three row matrix. This sort of object is used in various vectorial or matrix computations.
    """
    def Add(self,Other : gp_Mat) -> None: 
        """
        None

        None
        """
    def Added(self,Other : gp_Mat) -> gp_Mat: 
        """
        Computes the sum of this matrix and the matrix Other for each coefficient of the matrix : <me>.Coef(i,j) + <Other>.Coef(i,j)

        Computes the sum of this matrix and the matrix Other for each coefficient of the matrix : <me>.Coef(i,j) + <Other>.Coef(i,j)
        """
    def ChangeValue(self,Row : int,Col : int) -> float: 
        """
        Returns the coefficient of range (Row, Col) Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 3

        Returns the coefficient of range (Row, Col) Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 3
        """
    def Column(self,Col : int) -> gp_XYZ: 
        """
        Returns the column of Col index. Raises OutOfRange if Col < 1 or Col > 3
        """
    def Determinant(self) -> float: 
        """
        Computes the determinant of the matrix.

        Computes the determinant of the matrix.
        """
    def Diagonal(self) -> gp_XYZ: 
        """
        Returns the main diagonal of the matrix.
        """
    def Divide(self,Scalar : float) -> None: 
        """
        None

        None
        """
    def Divided(self,Scalar : float) -> gp_Mat: 
        """
        Divides all the coefficients of the matrix by Scalar

        Divides all the coefficients of the matrix by Scalar
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def Invert(self) -> None: 
        """
        None
        """
    def Inverted(self) -> gp_Mat: 
        """
        Inverses the matrix and raises if the matrix is singular. - Invert assigns the result to this matrix, while - Inverted creates a new one. Warning The Gauss LU decomposition is used to invert the matrix. Consequently, the matrix is considered as singular if the largest pivot found is less than or equal to gp::Resolution(). Exceptions Standard_ConstructionError if this matrix is singular, and therefore cannot be inverted.
        """
    def IsSingular(self) -> bool: 
        """
        The Gauss LU decomposition is used to invert the matrix (see Math package) so the matrix is considered as singular if the largest pivot found is lower or equal to Resolution from gp.

        The Gauss LU decomposition is used to invert the matrix (see Math package) so the matrix is considered as singular if the largest pivot found is lower or equal to Resolution from gp.
        """
    @overload
    def Multiplied(self,Other : gp_Mat) -> gp_Mat: 
        """
        Computes the product of two matrices <me> * <Other>

        None

        Computes the product of two matrices <me> * <Other>

        None
        """
    @overload
    def Multiplied(self,Scalar : float) -> gp_Mat: ...
    @overload
    def Multiply(self,Other : gp_Mat) -> None: 
        """
        Computes the product of two matrices <me> = <Other> * <me>.

        Multiplies all the coefficients of the matrix by Scalar

        Computes the product of two matrices <me> = <Other> * <me>.

        Multiplies all the coefficients of the matrix by Scalar
        """
    @overload
    def Multiply(self,Scalar : float) -> None: ...
    def Power(self,N : int) -> None: 
        """
        None
        """
    def Powered(self,N : int) -> gp_Mat: 
        """
        Computes <me> = <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Invert() *...........* <me>.Invert(). If N < 0 an exception will be raised if the matrix is not inversible

        Computes <me> = <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Invert() *...........* <me>.Invert(). If N < 0 an exception will be raised if the matrix is not inversible
        """
    def PreMultiply(self,Other : gp_Mat) -> None: 
        """
        None

        None
        """
    def Row(self,Row : int) -> gp_XYZ: 
        """
        returns the row of Row index. Raises OutOfRange if Row < 1 or Row > 3
        """
    def SetCol(self,Col : int,Value : gp_XYZ) -> None: 
        """
        Assigns the three coordinates of Value to the column of index Col of this matrix. Raises OutOfRange if Col < 1 or Col > 3.
        """
    def SetCols(self,Col1 : gp_XYZ,Col2 : gp_XYZ,Col3 : gp_XYZ) -> None: 
        """
        Assigns the number triples Col1, Col2, Col3 to the three columns of this matrix.
        """
    def SetCross(self,Ref : gp_XYZ) -> None: 
        """
        Modifies the matrix M so that applying it to any number triple (X, Y, Z) produces the same result as the cross product of Ref and the number triple (X, Y, Z): i.e.: M * {X,Y,Z}t = Ref.Cross({X, Y ,Z}) this matrix is anti symmetric. To apply this matrix to the triplet {XYZ} is the same as to do the cross product between the triplet Ref and the triplet {XYZ}. Note: this matrix is anti-symmetric.
        """
    def SetDiagonal(self,X1 : float,X2 : float,X3 : float) -> None: 
        """
        Modifies the main diagonal of the matrix. <me>.Value (1, 1) = X1 <me>.Value (2, 2) = X2 <me>.Value (3, 3) = X3 The other coefficients of the matrix are not modified.

        Modifies the main diagonal of the matrix. <me>.Value (1, 1) = X1 <me>.Value (2, 2) = X2 <me>.Value (3, 3) = X3 The other coefficients of the matrix are not modified.
        """
    def SetDot(self,Ref : gp_XYZ) -> None: 
        """
        Modifies this matrix so that applying it to any number triple (X, Y, Z) produces the same result as the scalar product of Ref and the number triple (X, Y, Z): this * (X,Y,Z) = Ref.(X,Y,Z) Note: this matrix is symmetric.
        """
    def SetIdentity(self) -> None: 
        """
        Modifies this matrix so that it represents the Identity matrix.

        Modifies this matrix so that it represents the Identity matrix.
        """
    def SetRotation(self,Axis : gp_XYZ,Ang : float) -> None: 
        """
        Modifies this matrix so that it represents a rotation. Ang is the angular value in radians and the XYZ axis gives the direction of the rotation. Raises ConstructionError if XYZ.Modulus() <= Resolution()
        """
    def SetRow(self,Row : int,Value : gp_XYZ) -> None: 
        """
        Assigns the three coordinates of Value to the row of index Row of this matrix. Raises OutOfRange if Row < 1 or Row > 3.
        """
    def SetRows(self,Row1 : gp_XYZ,Row2 : gp_XYZ,Row3 : gp_XYZ) -> None: 
        """
        Assigns the number triples Row1, Row2, Row3 to the three rows of this matrix.
        """
    def SetScale(self,S : float) -> None: 
        """
        Modifies the the matrix so that it represents a scaling transformation, where S is the scale factor. : | S 0.0 0.0 | <me> = | 0.0 S 0.0 | | 0.0 0.0 S |

        Modifies the the matrix so that it represents a scaling transformation, where S is the scale factor. : | S 0.0 0.0 | <me> = | 0.0 S 0.0 | | 0.0 0.0 S |
        """
    def SetValue(self,Row : int,Col : int,Value : float) -> None: 
        """
        Assigns <Value> to the coefficient of row Row, column Col of this matrix. Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 3

        Assigns <Value> to the coefficient of row Row, column Col of this matrix. Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 3
        """
    def Subtract(self,Other : gp_Mat) -> None: 
        """
        None

        None
        """
    def Subtracted(self,Other : gp_Mat) -> gp_Mat: 
        """
        cOmputes for each coefficient of the matrix : <me>.Coef(i,j) - <Other>.Coef(i,j)

        cOmputes for each coefficient of the matrix : <me>.Coef(i,j) - <Other>.Coef(i,j)
        """
    def Transpose(self) -> None: 
        """
        None

        None
        """
    def Transposed(self) -> gp_Mat: 
        """
        Transposes the matrix. A(j, i) -> A (i, j)

        Transposes the matrix. A(j, i) -> A (i, j)
        """
    def Value(self,Row : int,Col : int) -> float: 
        """
        Returns the coefficient of range (Row, Col) Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 3

        Returns the coefficient of range (Row, Col) Raises OutOfRange if Row < 1 or Row > 3 or Col < 1 or Col > 3
        """
    def __add__(self,Other : gp_Mat) -> gp_Mat: 
        """
        None
        """
    def __iadd__(self,Other : gp_Mat) -> None: 
        """
        None
        """
    @overload
    def __imul__(self,Other : gp_Mat) -> None: 
        """
        None

        None
        """
    @overload
    def __imul__(self,Scalar : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Col1 : gp_XYZ,Col2 : gp_XYZ,Col3 : gp_XYZ) -> None: ...
    @overload
    def __init__(self,a11 : float,a12 : float,a13 : float,a21 : float,a22 : float,a23 : float,a31 : float,a32 : float,a33 : float) -> None: ...
    def __isub__(self,Other : gp_Mat) -> None: 
        """
        None
        """
    def __itruediv__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,Scalar : float) -> gp_Mat: 
        """
        None

        None
        """
    @overload
    def __mul__(self,Other : gp_Mat) -> gp_Mat: ...
    @overload
    def __rmul__(self,Scalar : float) -> gp_Mat: 
        """
        None

        None
        """
    @overload
    def __rmul__(self,Other : gp_Mat) -> gp_Mat: ...
    def __sub__(self,Other : gp_Mat) -> gp_Mat: 
        """
        None
        """
    def __truediv__(self,Scalar : float) -> gp_Mat: 
        """
        None
        """
    pass
class gp_Mat2d():
    """
    Describes a two column, two row matrix. This sort of object is used in various vectorial or matrix computations.
    """
    def Add(self,Other : gp_Mat2d) -> None: 
        """
        None

        None
        """
    def Added(self,Other : gp_Mat2d) -> gp_Mat2d: 
        """
        Computes the sum of this matrix and the matrix Other.for each coefficient of the matrix : <me>.Coef(i,j) + <Other>.Coef(i,j) Note: - operator += assigns the result to this matrix, while - operator + creates a new one.

        Computes the sum of this matrix and the matrix Other.for each coefficient of the matrix : <me>.Coef(i,j) + <Other>.Coef(i,j) Note: - operator += assigns the result to this matrix, while - operator + creates a new one.
        """
    def ChangeValue(self,Row : int,Col : int) -> float: 
        """
        Returns the coefficient of range (Row, Col) Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 2

        Returns the coefficient of range (Row, Col) Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 2
        """
    def Column(self,Col : int) -> gp_XY: 
        """
        Returns the column of Col index. Raises OutOfRange if Col < 1 or Col > 2
        """
    def Determinant(self) -> float: 
        """
        Computes the determinant of the matrix.

        Computes the determinant of the matrix.
        """
    def Diagonal(self) -> gp_XY: 
        """
        Returns the main diagonal of the matrix.
        """
    def Divide(self,Scalar : float) -> None: 
        """
        None

        None
        """
    def Divided(self,Scalar : float) -> gp_Mat2d: 
        """
        Divides all the coefficients of the matrix by a scalar.

        Divides all the coefficients of the matrix by a scalar.
        """
    def Invert(self) -> None: 
        """
        None
        """
    def Inverted(self) -> gp_Mat2d: 
        """
        Inverses the matrix and raises exception if the matrix is singular.

        Inverses the matrix and raises exception if the matrix is singular.
        """
    def IsSingular(self) -> bool: 
        """
        Returns true if this matrix is singular (and therefore, cannot be inverted). The Gauss LU decomposition is used to invert the matrix so the matrix is considered as singular if the largest pivot found is lower or equal to Resolution from gp.

        Returns true if this matrix is singular (and therefore, cannot be inverted). The Gauss LU decomposition is used to invert the matrix so the matrix is considered as singular if the largest pivot found is lower or equal to Resolution from gp.
        """
    @overload
    def Multiplied(self,Other : gp_Mat2d) -> gp_Mat2d: 
        """
        None

        None

        None

        None
        """
    @overload
    def Multiplied(self,Scalar : float) -> gp_Mat2d: ...
    @overload
    def Multiply(self,Scalar : float) -> None: 
        """
        Computes the product of two matrices <me> * <Other>

        Multiplies all the coefficients of the matrix by a scalar.

        Computes the product of two matrices <me> * <Other>

        Multiplies all the coefficients of the matrix by a scalar.
        """
    @overload
    def Multiply(self,Other : gp_Mat2d) -> None: ...
    def Power(self,N : int) -> None: 
        """
        None
        """
    def Powered(self,N : int) -> gp_Mat2d: 
        """
        computes <me> = <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Invert() *...........* <me>.Invert(). If N < 0 an exception can be raised if the matrix is not inversible

        computes <me> = <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Invert() *...........* <me>.Invert(). If N < 0 an exception can be raised if the matrix is not inversible
        """
    def PreMultiply(self,Other : gp_Mat2d) -> None: 
        """
        Modifies this matrix by premultiplying it by the matrix Other <me> = Other * <me>.

        Modifies this matrix by premultiplying it by the matrix Other <me> = Other * <me>.
        """
    def Row(self,Row : int) -> gp_XY: 
        """
        Returns the row of index Row. Raised if Row < 1 or Row > 2
        """
    def SetCol(self,Col : int,Value : gp_XY) -> None: 
        """
        Assigns the two coordinates of Value to the column of range Col of this matrix Raises OutOfRange if Col < 1 or Col > 2.
        """
    def SetCols(self,Col1 : gp_XY,Col2 : gp_XY) -> None: 
        """
        Assigns the number pairs Col1, Col2 to the two columns of this matrix
        """
    def SetDiagonal(self,X1 : float,X2 : float) -> None: 
        """
        Modifies the main diagonal of the matrix. <me>.Value (1, 1) = X1 <me>.Value (2, 2) = X2 The other coefficients of the matrix are not modified.

        Modifies the main diagonal of the matrix. <me>.Value (1, 1) = X1 <me>.Value (2, 2) = X2 The other coefficients of the matrix are not modified.
        """
    def SetIdentity(self) -> None: 
        """
        Modifies this matrix, so that it represents the Identity matrix.

        Modifies this matrix, so that it represents the Identity matrix.
        """
    def SetRotation(self,Ang : float) -> None: 
        """
        Modifies this matrix, so that it representso a rotation. Ang is the angular value in radian of the rotation.

        Modifies this matrix, so that it representso a rotation. Ang is the angular value in radian of the rotation.
        """
    def SetRow(self,Row : int,Value : gp_XY) -> None: 
        """
        Assigns the two coordinates of Value to the row of index Row of this matrix. Raises OutOfRange if Row < 1 or Row > 2.
        """
    def SetRows(self,Row1 : gp_XY,Row2 : gp_XY) -> None: 
        """
        Assigns the number pairs Row1, Row2 to the two rows of this matrix.
        """
    def SetScale(self,S : float) -> None: 
        """
        Modifies the matrix such that it represents a scaling transformation, where S is the scale factor : | S 0.0 | <me> = | 0.0 S |

        Modifies the matrix such that it represents a scaling transformation, where S is the scale factor : | S 0.0 | <me> = | 0.0 S |
        """
    def SetValue(self,Row : int,Col : int,Value : float) -> None: 
        """
        Assigns <Value> to the coefficient of row Row, column Col of this matrix. Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 2

        Assigns <Value> to the coefficient of row Row, column Col of this matrix. Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 2
        """
    def Subtract(self,Other : gp_Mat2d) -> None: 
        """
        None

        None
        """
    def Subtracted(self,Other : gp_Mat2d) -> gp_Mat2d: 
        """
        Computes for each coefficient of the matrix : <me>.Coef(i,j) - <Other>.Coef(i,j)

        Computes for each coefficient of the matrix : <me>.Coef(i,j) - <Other>.Coef(i,j)
        """
    def Transpose(self) -> None: 
        """
        None

        None
        """
    def Transposed(self) -> gp_Mat2d: 
        """
        Transposes the matrix. A(j, i) -> A (i, j)

        Transposes the matrix. A(j, i) -> A (i, j)
        """
    def Value(self,Row : int,Col : int) -> float: 
        """
        Returns the coefficient of range (Row, Col) Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 2

        Returns the coefficient of range (Row, Col) Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 2
        """
    def __add__(self,Other : gp_Mat2d) -> gp_Mat2d: 
        """
        None
        """
    def __iadd__(self,Other : gp_Mat2d) -> None: 
        """
        None
        """
    def __imul__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Col1 : gp_XY,Col2 : gp_XY) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __isub__(self,Other : gp_Mat2d) -> None: 
        """
        None
        """
    def __itruediv__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,Scalar : float) -> gp_Mat2d: 
        """
        None

        None
        """
    @overload
    def __mul__(self,Other : gp_Mat2d) -> gp_Mat2d: ...
    @overload
    def __rmul__(self,Scalar : float) -> gp_Mat2d: 
        """
        None

        None
        """
    @overload
    def __rmul__(self,Other : gp_Mat2d) -> gp_Mat2d: ...
    def __sub__(self,Other : gp_Mat2d) -> gp_Mat2d: 
        """
        None
        """
    def __truediv__(self,Scalar : float) -> gp_Mat2d: 
        """
        None
        """
    pass
class gp_Parab():
    """
    Describes a parabola in 3D space. A parabola is defined by its focal length (that is, the distance between its focus and apex) and positioned in space with a coordinate system (a gp_Ax2 object) where: - the origin of the coordinate system is on the apex of the parabola, - the "X Axis" of the coordinate system is the axis of symmetry; the parabola is on the positive side of this axis, and - the origin, "X Direction" and "Y Direction" of the coordinate system define the plane of the parabola. The equation of the parabola in this coordinate system, which is the "local coordinate system" of the parabola, is: Y**2 = (2*P) * X. where P, referred to as the parameter of the parabola, is the distance between the focus and the directrix (P is twice the focal length). The "main Direction" of the local coordinate system gives the normal vector to the plane of the parabola. See Also gce_MakeParab which provides functions for more complex parabola constructions Geom_Parabola which provides additional functions for constructing parabolas and works, in particular, with the parametric equations of parabolas
    """
    def Axis(self) -> gp_Ax1: 
        """
        Returns the main axis of the parabola. It is the axis normal to the plane of the parabola passing through the vertex of the parabola.

        Returns the main axis of the parabola. It is the axis normal to the plane of the parabola passing through the vertex of the parabola.
        """
    def Directrix(self) -> gp_Ax1: 
        """
        Computes the directrix of this parabola. The directrix is: - a line parallel to the "Y Direction" of the local coordinate system of this parabola, and - located on the negative side of the axis of symmetry, at a distance from the apex which is equal to the focal length of this parabola. The directrix is returned as an axis (a gp_Ax1 object), the origin of which is situated on the "X Axis" of this parabola.

        Computes the directrix of this parabola. The directrix is: - a line parallel to the "Y Direction" of the local coordinate system of this parabola, and - located on the negative side of the axis of symmetry, at a distance from the apex which is equal to the focal length of this parabola. The directrix is returned as an axis (a gp_Ax1 object), the origin of which is situated on the "X Axis" of this parabola.
        """
    def Focal(self) -> float: 
        """
        Returns the distance between the vertex and the focus of the parabola.

        Returns the distance between the vertex and the focus of the parabola.
        """
    def Focus(self) -> gp_Pnt: 
        """
        - Computes the focus of the parabola.

        - Computes the focus of the parabola.
        """
    def Location(self) -> gp_Pnt: 
        """
        Returns the vertex of the parabola. It is the "Location" point of the coordinate system of the parabola.

        Returns the vertex of the parabola. It is the "Location" point of the coordinate system of the parabola.
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirror(self,P : gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Parab: 
        """
        Performs the symmetrical transformation of a parabola with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a parabola with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a parabola with respect to a plane. The axis placement A2 locates the plane of the symmetry (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Parab: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Parab: ...
    def Parameter(self) -> float: 
        """
        Computes the parameter of the parabola. It is the distance between the focus and the directrix of the parabola. This distance is twice the focal length.

        Computes the parameter of the parabola. It is the distance between the focus and the directrix of the parabola. This distance is twice the focal length.
        """
    def Position(self) -> gp_Ax2: 
        """
        Returns the local coordinate system of the parabola.

        Returns the local coordinate system of the parabola.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Parab: 
        """
        Rotates a parabola. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a parabola. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Parab: 
        """
        Scales a parabola. S is the scaling value. If S is negative the direction of the symmetry axis XAxis is reversed and the direction of the YAxis too.

        Scales a parabola. S is the scaling value. If S is negative the direction of the symmetry axis XAxis is reversed and the direction of the YAxis too.
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Modifies this parabola by redefining its local coordinate system so that - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed in the same way as for any gp_Ax2) Raises ConstructionError if the direction of A1 is parallel to the previous XAxis of the parabola.

        Modifies this parabola by redefining its local coordinate system so that - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed in the same way as for any gp_Ax2) Raises ConstructionError if the direction of A1 is parallel to the previous XAxis of the parabola.
        """
    def SetFocal(self,Focal : float) -> None: 
        """
        Changes the focal distance of the parabola. Raises ConstructionError if Focal < 0.0

        Changes the focal distance of the parabola. Raises ConstructionError if Focal < 0.0
        """
    def SetLocation(self,P : gp_Pnt) -> None: 
        """
        Changes the location of the parabola. It is the vertex of the parabola.

        Changes the location of the parabola. It is the vertex of the parabola.
        """
    def SetPosition(self,A2 : gp_Ax2) -> None: 
        """
        Changes the local coordinate system of the parabola.

        Changes the local coordinate system of the parabola.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Parab: 
        """
        Transforms a parabola with the transformation T from class Trsf.

        Transforms a parabola with the transformation T from class Trsf.
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Parab: 
        """
        Translates a parabola in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a parabola from the point P1 to the point P2.

        Translates a parabola in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a parabola from the point P1 to the point P2.
        """
    @overload
    def Translated(self,V : gp_Vec) -> gp_Parab: ...
    def XAxis(self) -> gp_Ax1: 
        """
        Returns the symmetry axis of the parabola. The location point of the axis is the vertex of the parabola.

        Returns the symmetry axis of the parabola. The location point of the axis is the vertex of the parabola.
        """
    def YAxis(self) -> gp_Ax1: 
        """
        It is an axis parallel to the directrix of the parabola. The location point of this axis is the vertex of the parabola.

        It is an axis parallel to the directrix of the parabola. The location point of this axis is the vertex of the parabola.
        """
    @overload
    def __init__(self,A2 : gp_Ax2,Focal : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,D : gp_Ax1,F : gp_Pnt) -> None: ...
    pass
class gp_Parab2d():
    """
    Describes a parabola in the plane (2D space). A parabola is defined by its focal length (that is, the distance between its focus and apex) and positioned in the plane with a coordinate system (a gp_Ax22d object) where: - the origin of the coordinate system is on the apex of the parabola, and - the "X Axis" of the coordinate system is the axis of symmetry; the parabola is on the positive side of this axis. This coordinate system is the "local coordinate system" of the parabola. Its orientation (direct or indirect sense) gives an implicit orientation to the parabola. In this coordinate system, the equation for the parabola is: Y**2 = (2*P) * X. where P, referred to as the parameter of the parabola, is the distance between the focus and the directrix (P is twice the focal length). See Also GCE2d_MakeParab2d which provides functions for more complex parabola constructions Geom2d_Parabola which provides additional functions for constructing parabolas and works, in particular, with the parametric equations of parabolas
    """
    def Axis(self) -> gp_Ax22d: 
        """
        Returns the local coordinate system of the parabola. The "Location" point of this axis is the vertex of the parabola.

        Returns the local coordinate system of the parabola. The "Location" point of this axis is the vertex of the parabola.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float]: 
        """
        Computes the coefficients of the implicit equation of the parabola (in WCS - World Coordinate System). A * (X**2) + B * (Y**2) + 2*C*(X*Y) + 2*D*X + 2*E*Y + F = 0.
        """
    def Directrix(self) -> gp_Ax2d: 
        """
        Computes the directrix of the parabola. The directrix is: - a line parallel to the "Y Direction" of the local coordinate system of this parabola, and - located on the negative side of the axis of symmetry, at a distance from the apex which is equal to the focal length of this parabola. The directrix is returned as an axis (a gp_Ax2d object), the origin of which is situated on the "X Axis" of this parabola.

        Computes the directrix of the parabola. The directrix is: - a line parallel to the "Y Direction" of the local coordinate system of this parabola, and - located on the negative side of the axis of symmetry, at a distance from the apex which is equal to the focal length of this parabola. The directrix is returned as an axis (a gp_Ax2d object), the origin of which is situated on the "X Axis" of this parabola.
        """
    def Focal(self) -> float: 
        """
        Returns the distance between the vertex and the focus of the parabola.

        Returns the distance between the vertex and the focus of the parabola.
        """
    def Focus(self) -> gp_Pnt2d: 
        """
        Returns the focus of the parabola.

        Returns the focus of the parabola.
        """
    def IsDirect(self) -> bool: 
        """
        Returns true if the local coordinate system is direct and false in the other case.

        Returns true if the local coordinate system is direct and false in the other case.
        """
    def Location(self) -> gp_Pnt2d: 
        """
        Returns the vertex of the parabola.

        Returns the vertex of the parabola.
        """
    @overload
    def Mirror(self,A : gp_Ax2d) -> None: 
        """
        None

        None
        """
    @overload
    def Mirror(self,P : gp_Pnt2d) -> None: ...
    def MirrorAxis(self) -> gp_Ax2d: 
        """
        Returns the symmetry axis of the parabola. The "Location" point of this axis is the vertex of the parabola.

        Returns the symmetry axis of the parabola. The "Location" point of this axis is the vertex of the parabola.
        """
    @overload
    def Mirrored(self,A : gp_Ax2d) -> gp_Parab2d: 
        """
        Performs the symmetrical transformation of a parabola with respect to the point P which is the center of the symmetry

        Performs the symmetrical transformation of a parabola with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirrored(self,P : gp_Pnt2d) -> gp_Parab2d: ...
    def Parameter(self) -> float: 
        """
        Returns the distance between the focus and the directrix of the parabola.

        Returns the distance between the focus and the directrix of the parabola.
        """
    def Reverse(self) -> None: 
        """
        None

        None
        """
    def Reversed(self) -> gp_Parab2d: 
        """
        Reverses the orientation of the local coordinate system of this parabola (the "Y Direction" is reversed). Therefore, the implicit orientation of this parabola is reversed. Note: - Reverse assigns the result to this parabola, while - Reversed creates a new one.

        Reverses the orientation of the local coordinate system of this parabola (the "Y Direction" is reversed). Therefore, the implicit orientation of this parabola is reversed. Note: - Reverse assigns the result to this parabola, while - Reversed creates a new one.
        """
    def Rotate(self,P : gp_Pnt2d,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,P : gp_Pnt2d,Ang : float) -> gp_Parab2d: 
        """
        Rotates a parabola. P is the center of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a parabola. P is the center of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt2d,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt2d,S : float) -> gp_Parab2d: 
        """
        Scales a parabola. S is the scaling value. If S is negative the direction of the symmetry axis "XAxis" is reversed and the direction of the "YAxis" too.

        Scales a parabola. S is the scaling value. If S is negative the direction of the symmetry axis "XAxis" is reversed and the direction of the "YAxis" too.
        """
    def SetAxis(self,A : gp_Ax22d) -> None: 
        """
        Changes the local coordinate system of the parabola. The "Location" point of A becomes the vertex of the parabola.

        Changes the local coordinate system of the parabola. The "Location" point of A becomes the vertex of the parabola.
        """
    def SetFocal(self,Focal : float) -> None: 
        """
        Changes the focal distance of the parabola Warnings : It is possible to have Focal = 0. Raises ConstructionError if Focal < 0.0

        Changes the focal distance of the parabola Warnings : It is possible to have Focal = 0. Raises ConstructionError if Focal < 0.0
        """
    def SetLocation(self,P : gp_Pnt2d) -> None: 
        """
        Changes the "Location" point of the parabola. It is the vertex of the parabola.

        Changes the "Location" point of the parabola. It is the vertex of the parabola.
        """
    def SetMirrorAxis(self,A : gp_Ax2d) -> None: 
        """
        Modifies this parabola, by redefining its local coordinate system so that its origin and "X Direction" become those of the axis MA. The "Y Direction" of the local coordinate system is then recomputed. The orientation of the local coordinate system is not modified.

        Modifies this parabola, by redefining its local coordinate system so that its origin and "X Direction" become those of the axis MA. The "Y Direction" of the local coordinate system is then recomputed. The orientation of the local coordinate system is not modified.
        """
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Parab2d: 
        """
        Transforms an parabola with the transformation T from class Trsf2d.

        Transforms an parabola with the transformation T from class Trsf2d.
        """
    @overload
    def Translate(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec2d) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> gp_Parab2d: 
        """
        Translates a parabola in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a parabola from the point P1 to the point P2.

        Translates a parabola in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a parabola from the point P1 to the point P2.
        """
    @overload
    def Translated(self,V : gp_Vec2d) -> gp_Parab2d: ...
    @overload
    def __init__(self,theAxes : gp_Ax22d,theFocalLength : float) -> None: ...
    @overload
    def __init__(self,theDirectrix : gp_Ax2d,theFocus : gp_Pnt2d,theSense : bool=True) -> None: ...
    @overload
    def __init__(self,theMirrorAxis : gp_Ax2d,theFocalLength : float,theSense : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Pln():
    """
    Describes a plane. A plane is positioned in space with a coordinate system (a gp_Ax3 object), such that the plane is defined by the origin, "X Direction" and "Y Direction" of this coordinate system, which is the "local coordinate system" of the plane. The "main Direction" of the coordinate system is a vector normal to the plane. It gives the plane an implicit orientation such that the plane is said to be "direct", if the coordinate system is right-handed, or "indirect" in the other case. Note: when a gp_Pln plane is converted into a Geom_Plane plane, some implicit properties of its local coordinate system are used explicitly: - its origin defines the origin of the two parameters of the planar surface, - its implicit orientation is also that of the Geom_Plane. See Also gce_MakePln which provides functions for more complex plane constructions Geom_Plane which provides additional functions for constructing planes and works, in particular, with the parametric equations of planes
    """
    def Axis(self) -> gp_Ax1: 
        """
        Returns the plane's normal Axis.

        Returns the plane's normal Axis.
        """
    def Coefficients(self) -> Tuple[float, float, float, float]: 
        """
        Returns the coefficients of the plane's cartesian equation : A * X + B * Y + C * Z + D = 0.

        Returns the coefficients of the plane's cartesian equation : A * X + B * Y + C * Z + D = 0.
        """
    @overload
    def Contains(self,P : gp_Pnt,LinearTolerance : float) -> bool: 
        """
        Returns true if this plane contains the point P. This means that - the distance between point P and this plane is less than or equal to LinearTolerance, or - line L is normal to the "main Axis" of the local coordinate system of this plane, within the tolerance AngularTolerance, and the distance between the origin of line L and this plane is less than or equal to LinearTolerance.

        Returns true if this plane contains the line L. This means that - the distance between point P and this plane is less than or equal to LinearTolerance, or - line L is normal to the "main Axis" of the local coordinate system of this plane, within the tolerance AngularTolerance, and the distance between the origin of line L and this plane is less than or equal to LinearTolerance.

        Returns true if this plane contains the point P. This means that - the distance between point P and this plane is less than or equal to LinearTolerance, or - line L is normal to the "main Axis" of the local coordinate system of this plane, within the tolerance AngularTolerance, and the distance between the origin of line L and this plane is less than or equal to LinearTolerance.

        Returns true if this plane contains the line L. This means that - the distance between point P and this plane is less than or equal to LinearTolerance, or - line L is normal to the "main Axis" of the local coordinate system of this plane, within the tolerance AngularTolerance, and the distance between the origin of line L and this plane is less than or equal to LinearTolerance.
        """
    @overload
    def Contains(self,L : gp_Lin,LinearTolerance : float,AngularTolerance : float) -> bool: ...
    def Direct(self) -> bool: 
        """
        returns true if the Ax3 is right handed.

        returns true if the Ax3 is right handed.
        """
    @overload
    def Distance(self,L : gp_Lin) -> float: 
        """
        Computes the distance between <me> and the point <P>.

        Computes the distance between <me> and the line <L>.

        Computes the distance between two planes.

        Computes the distance between <me> and the point <P>.

        Computes the distance between <me> and the line <L>.

        Computes the distance between two planes.
        """
    @overload
    def Distance(self,P : gp_Pnt) -> float: ...
    @overload
    def Distance(self,Other : gp_Pln) -> float: ...
    def Location(self) -> gp_Pnt: 
        """
        Returns the plane's location (origin).

        Returns the plane's location (origin).
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirror(self,P : gp_Pnt) -> None: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Pln: 
        """
        Performs the symmetrical transformation of a plane with respect to the point <P> which is the center of the symmetry Warnings : The normal direction to the plane is not changed. The "XAxis" and the "YAxis" are reversed.

        Performs the symmetrical transformation of a plane with respect to an axis placement which is the axis of the symmetry. The transformation is performed on the "Location" point, on the "XAxis" and the "YAxis". The resulting normal direction is the cross product between the "XDirection" and the "YDirection" after transformation if the initial plane was right handed, else it is the opposite.

        Performs the symmetrical transformation of a plane with respect to an axis placement. The axis placement <A2> locates the plane of the symmetry. The transformation is performed on the "Location" point, on the "XAxis" and the "YAxis". The resulting normal direction is the cross product between the "XDirection" and the "YDirection" after transformation if the initial plane was right handed, else it is the opposite.
        """
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Pln: ...
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Pln: ...
    def Position(self) -> gp_Ax3: 
        """
        Returns the local coordinate system of the plane .

        Returns the local coordinate system of the plane .
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Pln: 
        """
        rotates a plane. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        rotates a plane. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Pln: 
        """
        Scales a plane. S is the scaling value.

        Scales a plane. S is the scaling value.
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Modifies this plane, by redefining its local coordinate system so that - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed). Raises ConstructionError if the A1 is parallel to the "XAxis" of the plane.

        Modifies this plane, by redefining its local coordinate system so that - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed). Raises ConstructionError if the A1 is parallel to the "XAxis" of the plane.
        """
    def SetLocation(self,Loc : gp_Pnt) -> None: 
        """
        Changes the origin of the plane.

        Changes the origin of the plane.
        """
    def SetPosition(self,A3 : gp_Ax3) -> None: 
        """
        Changes the local coordinate system of the plane.

        Changes the local coordinate system of the plane.
        """
    @overload
    def SquareDistance(self,Other : gp_Pln) -> float: 
        """
        Computes the square distance between <me> and the point <P>.

        Computes the square distance between <me> and the line <L>.

        Computes the square distance between two planes.

        Computes the square distance between <me> and the point <P>.

        Computes the square distance between <me> and the line <L>.

        Computes the square distance between two planes.
        """
    @overload
    def SquareDistance(self,L : gp_Lin) -> float: ...
    @overload
    def SquareDistance(self,P : gp_Pnt) -> float: ...
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Pln: 
        """
        Transforms a plane with the transformation T from class Trsf. The transformation is performed on the "Location" point, on the "XAxis" and the "YAxis". The resulting normal direction is the cross product between the "XDirection" and the "YDirection" after transformation.

        Transforms a plane with the transformation T from class Trsf. The transformation is performed on the "Location" point, on the "XAxis" and the "YAxis". The resulting normal direction is the cross product between the "XDirection" and the "YDirection" after transformation.
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: ...
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Pln: 
        """
        Translates a plane in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a plane from the point P1 to the point P2.

        Translates a plane in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a plane from the point P1 to the point P2.
        """
    @overload
    def Translated(self,V : gp_Vec) -> gp_Pln: ...
    def UReverse(self) -> None: 
        """
        Reverses the U parametrization of the plane reversing the XAxis.

        Reverses the U parametrization of the plane reversing the XAxis.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V parametrization of the plane reversing the YAxis.

        Reverses the V parametrization of the plane reversing the YAxis.
        """
    def XAxis(self) -> gp_Ax1: 
        """
        Returns the X axis of the plane.

        Returns the X axis of the plane.
        """
    def YAxis(self) -> gp_Ax1: 
        """
        Returns the Y axis of the plane.

        Returns the Y axis of the plane.
        """
    @overload
    def __init__(self,P : gp_Pnt,V : gp_Dir) -> None: ...
    @overload
    def __init__(self,A : float,B : float,C : float,D : float) -> None: ...
    @overload
    def __init__(self,A3 : gp_Ax3) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Pnt():
    """
    Defines a 3D cartesian point.
    """
    @overload
    def BaryCenter(self,A : float,P : gp_Pnt,B : float) -> None: 
        """
        Assigns the result of the following expression to this point (Alpha*this + Beta*P) / (Alpha + Beta)

        Assigns the result of the following expression to this point (Alpha*this + Beta*P) / (Alpha + Beta)
        """
    @overload
    def BaryCenter(self,Alpha : float,P : gp_Pnt,Beta : float) -> None: ...
    def ChangeCoord(self) -> gp_XYZ: 
        """
        Returns the coordinates of this point. Note: This syntax allows direct modification of the returned value.

        Returns the coordinates of this point. Note: This syntax allows direct modification of the returned value.
        """
    @overload
    def Coord(self,Index : int) -> float: 
        """
        Returns the coordinate of corresponding to the value of Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned Raises OutOfRange if Index != {1, 2, 3}. Raised if Index != {1, 2, 3}.

        Returns the coordinate of corresponding to the value of Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned Raises OutOfRange if Index != {1, 2, 3}. Raised if Index != {1, 2, 3}.

        For this point gives its three coordinates Xp, Yp and Zp.

        For this point gives its three coordinates Xp, Yp and Zp.

        For this point, returns its three coordinates as a XYZ object.

        For this point, returns its three coordinates as a XYZ object.
        """
    @overload
    def Coord(self) -> gp_XYZ: ...
    @overload
    def Coord(self) -> Tuple[float, float, float]: ...
    def Distance(self,Other : gp_Pnt) -> float: 
        """
        Computes the distance between two points.

        Computes the distance between two points.
        """
    def IsEqual(self,Other : gp_Pnt,LinearTolerance : float) -> bool: 
        """
        Comparison Returns True if the distance between the two points is lower or equal to LinearTolerance.

        Comparison Returns True if the distance between the two points is lower or equal to LinearTolerance.
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: 
        """
        Performs the symmetrical transformation of a point with respect to the point P which is the center of the symmetry.

        None

        None
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Pnt: 
        """
        Performs the symmetrical transformation of a point with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a point with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).

        Rotates a point. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Pnt: ...
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Pnt: ...
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Pnt: 
        """
        Scales a point. S is the scaling value.

        Scales a point. S is the scaling value.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Pnt: 
        """
        Transforms a point with the transformation T.

        Transforms a point with the transformation T.
        """
    @overload
    def SetCoord(self,Xp : float,Yp : float,Zp : float) -> None: 
        """
        Changes the coordinate of range Index : Index = 1 => X is modified Index = 2 => Y is modified Index = 3 => Z is modified Raised if Index != {1, 2, 3}.

        For this point, assigns the values Xp, Yp and Zp to its three coordinates.

        Changes the coordinate of range Index : Index = 1 => X is modified Index = 2 => Y is modified Index = 3 => Z is modified Raised if Index != {1, 2, 3}.

        For this point, assigns the values Xp, Yp and Zp to its three coordinates.
        """
    @overload
    def SetCoord(self,Index : int,Xi : float) -> None: ...
    def SetX(self,X : float) -> None: 
        """
        Assigns the given value to the X coordinate of this point.

        Assigns the given value to the X coordinate of this point.
        """
    @overload
    def SetXYZ(self,Coord : gp_XYZ) -> None: 
        """
        Assigns the three coordinates of Coord to this point.

        Assigns the three coordinates of Coord to this point.
        """
    @overload
    def SetXYZ(self,Coordinates : gp_XYZ) -> None: ...
    def SetY(self,Y : float) -> None: 
        """
        Assigns the given value to the Y coordinate of this point.

        Assigns the given value to the Y coordinate of this point.
        """
    def SetZ(self,Z : float) -> None: 
        """
        Assigns the given value to the Z coordinate of this point.

        Assigns the given value to the Z coordinate of this point.
        """
    def SquareDistance(self,Other : gp_Pnt) -> float: 
        """
        Computes the square distance between two points.

        Computes the square distance between two points.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Pnt: 
        """
        Translates a point in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a point in the direction of the vector V. The magnitude of the translation is the vector's magnitude.
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: ...
    @overload
    def Translated(self,V : gp_Vec) -> gp_Pnt: 
        """
        Translates a point from the point P1 to the point P2.

        None

        Translates a point from the point P1 to the point P2.

        None
        """
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Pnt: ...
    def X(self) -> float: 
        """
        For this point, returns its X coordinate.

        For this point, returns its X coordinate.
        """
    def XYZ(self) -> gp_XYZ: 
        """
        For this point, returns its three coordinates as a XYZ object.

        For this point, returns its three coordinates as a XYZ object.
        """
    def Y(self) -> float: 
        """
        For this point, returns its Y coordinate.

        For this point, returns its Y coordinate.
        """
    def Z(self) -> float: 
        """
        For this point, returns its Z coordinate.

        For this point, returns its Z coordinate.
        """
    @overload
    def __init__(self,Coord : gp_XYZ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Xp : float,Yp : float,Zp : float) -> None: ...
    pass
class gp_Pnt2d():
    """
    Defines a non-persistent 2D cartesian point.
    """
    def ChangeCoord(self) -> gp_XY: 
        """
        Returns the coordinates of this point. Note: This syntax allows direct modification of the returned value.

        Returns the coordinates of this point. Note: This syntax allows direct modification of the returned value.
        """
    @overload
    def Coord(self,Index : int) -> float: 
        """
        Returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Raises OutOfRange if Index != {1, 2}.

        Returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Raises OutOfRange if Index != {1, 2}.

        For this point returns its two coordinates as a number pair.

        For this point returns its two coordinates as a number pair.

        For this point, returns its two coordinates as a number pair.

        For this point, returns its two coordinates as a number pair.
        """
    @overload
    def Coord(self) -> Tuple[float, float]: ...
    @overload
    def Coord(self) -> gp_XY: ...
    def Distance(self,Other : gp_Pnt2d) -> float: 
        """
        Computes the distance between two points.

        Computes the distance between two points.
        """
    def IsEqual(self,Other : gp_Pnt2d,LinearTolerance : float) -> bool: 
        """
        Comparison Returns True if the distance between the two points is lower or equal to LinearTolerance.

        Comparison Returns True if the distance between the two points is lower or equal to LinearTolerance.
        """
    @overload
    def Mirror(self,P : gp_Pnt2d) -> None: 
        """
        Performs the symmetrical transformation of a point with respect to the point P which is the center of the symmetry.

        None
        """
    @overload
    def Mirror(self,A : gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,A : gp_Ax2d) -> gp_Pnt2d: 
        """
        Performs the symmetrical transformation of a point with respect to an axis placement which is the axis

        Rotates a point. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    @overload
    def Mirrored(self,P : gp_Pnt2d) -> gp_Pnt2d: ...
    def Rotate(self,P : gp_Pnt2d,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,P : gp_Pnt2d,Ang : float) -> gp_Pnt2d: 
        """
        Scales a point. S is the scaling value.

        Scales a point. S is the scaling value.
        """
    def Scale(self,P : gp_Pnt2d,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt2d,S : float) -> gp_Pnt2d: 
        """
        Transforms a point with the transformation T.

        Transforms a point with the transformation T.
        """
    @overload
    def SetCoord(self,Index : int,Xi : float) -> None: 
        """
        Assigns the value Xi to the coordinate that corresponds to Index: Index = 1 => X is modified Index = 2 => Y is modified Raises OutOfRange if Index != {1, 2}.

        For this point, assigns the values Xp and Yp to its two coordinates

        For this point, assigns the values Xp and Yp to its two coordinates

        Assigns the value Xi to the coordinate that corresponds to Index: Index = 1 => X is modified Index = 2 => Y is modified Raises OutOfRange if Index != {1, 2}.
        """
    @overload
    def SetCoord(self,Xp : float,Yp : float) -> None: ...
    def SetX(self,X : float) -> None: 
        """
        Assigns the given value to the X coordinate of this point.

        Assigns the given value to the X coordinate of this point.
        """
    @overload
    def SetXY(self,Coord : gp_XY) -> None: 
        """
        Assigns the two coordinates of Coord to this point.

        Assigns the two coordinates of Coord to this point.
        """
    @overload
    def SetXY(self,Coordinates : gp_XY) -> None: ...
    def SetY(self,Y : float) -> None: 
        """
        Assigns the given value to the Y coordinate of this point.

        Assigns the given value to the Y coordinate of this point.
        """
    def SquareDistance(self,Other : gp_Pnt2d) -> float: 
        """
        Computes the square distance between two points.

        Computes the square distance between two points.
        """
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Pnt2d: 
        """
        Translates a point in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a point in the direction of the vector V. The magnitude of the translation is the vector's magnitude.
        """
    @overload
    def Translate(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec2d) -> None: ...
    @overload
    def Translated(self,V : gp_Vec2d) -> gp_Pnt2d: 
        """
        Translates a point from the point P1 to the point P2.

        None

        Translates a point from the point P1 to the point P2.

        None
        """
    @overload
    def Translated(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> gp_Pnt2d: ...
    def X(self) -> float: 
        """
        For this point, returns its X coordinate.

        For this point, returns its X coordinate.
        """
    def XY(self) -> gp_XY: 
        """
        For this point, returns its two coordinates as a number pair.

        For this point, returns its two coordinates as a number pair.
        """
    def Y(self) -> float: 
        """
        For this point, returns its Y coordinate.

        For this point, returns its Y coordinate.
        """
    @overload
    def __init__(self,Coord : gp_XY) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Xp : float,Yp : float) -> None: ...
    pass
class gp_Quaternion():
    """
    Represents operation of rotation in 3d space as queternion and implements operations with rotations basing on quaternion mathematics.
    """
    @overload
    def Add(self,theQ : gp_Quaternion) -> None: 
        """
        Adds componnets of other quaternion; result is "rotations mix"

        Adds componnets of other quaternion; result is "rotations mix"
        """
    @overload
    def Add(self,theOther : gp_Quaternion) -> None: ...
    @overload
    def Added(self,theOther : gp_Quaternion) -> gp_Quaternion: 
        """
        Makes sum of quaternion components; result is "rotations mix"

        Makes sum of quaternion components; result is "rotations mix"
        """
    @overload
    def Added(self,theQ : gp_Quaternion) -> gp_Quaternion: ...
    @overload
    def Dot(self,theQ : gp_Quaternion) -> float: 
        """
        Computes inner product / scalar product / Dot

        Computes inner product / scalar product / Dot
        """
    @overload
    def Dot(self,theOther : gp_Quaternion) -> float: ...
    def GetEulerAngles(self,theOrder : gp_EulerSequence) -> Tuple[float, float, float]: 
        """
        Returns Euler angles describing current rotation
        """
    def GetMatrix(self) -> gp_Mat: 
        """
        Returns rotation operation as 3*3 matrix
        """
    def GetRotationAngle(self) -> float: 
        """
        Return rotation angle from -PI to PI
        """
    def GetVectorAndAngle(self,theAxis : gp_Vec) -> Tuple[float]: 
        """
        Convert a quaternion to Axis+Angle representation, preserve the axis direction and angle from -PI to +PI
        """
    def Invert(self) -> None: 
        """
        Inverts quaternion (both rotation direction and norm)

        Inverts quaternion (both rotation direction and norm)
        """
    def Inverted(self) -> gp_Quaternion: 
        """
        Return inversed quaternion q^-1

        Return inversed quaternion q^-1
        """
    def IsEqual(self,theOther : gp_Quaternion) -> bool: 
        """
        Simple equal test without precision
        """
    @overload
    def Multiplied(self,theQ : gp_Quaternion) -> gp_Quaternion: 
        """
        Multiply function - work the same as Matrices multiplying. qq' = (cross(v,v') + wv' + w'v, ww' - dot(v,v')) Result is rotation combination: q' than q (here q=this, q'=theQ). Notices than: qq' != q'q; qq^-1 = q;

        Multiply function - work the same as Matrices multiplying. qq' = (cross(v,v') + wv' + w'v, ww' - dot(v,v')) Result is rotation combination: q' than q (here q=this, q'=theQ). Notices than: qq' != q'q; qq^-1 = q;
        """
    @overload
    def Multiplied(self,theOther : gp_Quaternion) -> gp_Quaternion: ...
    @overload
    def Multiply(self,theVec : gp_Vec) -> gp_Vec: 
        """
        Adds rotation by multiplication

        Rotates vector by quaternion as rotation operator

        Adds rotation by multiplication
        """
    @overload
    def Multiply(self,theOther : gp_Quaternion) -> None: ...
    @overload
    def Multiply(self,theQ : gp_Quaternion) -> None: ...
    def Negated(self) -> gp_Quaternion: 
        """
        Returns quaternion with all components negated. Note that this operation does not affect neither rotation operator defined by quaternion nor its norm.

        Returns quaternion with all components negated. Note that this operation does not affect neither rotation operator defined by quaternion nor its norm.
        """
    def Norm(self) -> float: 
        """
        Returns norm of quaternion

        Returns norm of quaternion
        """
    def Normalize(self) -> None: 
        """
        Scale quaternion that its norm goes to 1. The appearing of 0 magnitude or near is a error, so we can be sure that can divide by magnitude
        """
    def Normalized(self) -> gp_Quaternion: 
        """
        Returns quaternion scaled so that its norm goes to 1.

        Returns quaternion scaled so that its norm goes to 1.
        """
    def Reverse(self) -> None: 
        """
        Reverse direction of rotation (conjugate quaternion)

        Reverse direction of rotation (conjugate quaternion)
        """
    def Reversed(self) -> gp_Quaternion: 
        """
        Return rotation with reversed direction (conjugated quaternion)

        Return rotation with reversed direction (conjugated quaternion)
        """
    def Scale(self,theScale : float) -> None: 
        """
        Scale all components by quaternion by theScale; note that rotation is not changed by this operation (except 0-scaling)

        Scale all components by quaternion by theScale; note that rotation is not changed by this operation (except 0-scaling)
        """
    def Scaled(self,theScale : float) -> gp_Quaternion: 
        """
        Returns scaled quaternion

        Returns scaled quaternion
        """
    @overload
    def Set(self,theQuaternion : gp_Quaternion) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Set(self,x : float,y : float,z : float,w : float) -> None: ...
    @overload
    def Set(self,theX : float,theY : float,theZ : float,theW : float) -> None: ...
    def SetEulerAngles(self,theOrder : gp_EulerSequence,theAlpha : float,theBeta : float,theGamma : float) -> None: 
        """
        Create a unit quaternion representing rotation defined by generalized Euler angles
        """
    def SetIdent(self) -> None: 
        """
        Make identity quaternion (zero-rotation)

        Make identity quaternion (zero-rotation)
        """
    def SetMatrix(self,theMat : gp_Mat) -> None: 
        """
        Create a unit quaternion by rotation matrix matrix must contain only rotation (not scale or shear)
        """
    @overload
    def SetRotation(self,theVecFrom : gp_Vec,theVecTo : gp_Vec,theHelpCrossVec : gp_Vec) -> None: 
        """
        Sets quaternion to shortest-arc rotation producing vector theVecTo from vector theVecFrom. If vectors theVecFrom and theVecTo are opposite then rotation axis is computed as theVecFrom ^ (1,0,0) or theVecFrom ^ (0,0,1).

        Sets quaternion to shortest-arc rotation producing vector theVecTo from vector theVecFrom. If vectors theVecFrom and theVecTo are opposite then rotation axis is computed as theVecFrom ^ theHelpCrossVec.
        """
    @overload
    def SetRotation(self,theVecFrom : gp_Vec,theVecTo : gp_Vec) -> None: ...
    def SetVectorAndAngle(self,theAxis : gp_Vec,theAngle : float) -> None: 
        """
        Create a unit quaternion from Axis+Angle representation
        """
    def SquareNorm(self) -> float: 
        """
        Returns square norm of quaternion

        Returns square norm of quaternion
        """
    def StabilizeLength(self) -> None: 
        """
        Stabilize quaternion length within 1 - 1/4. This operation is a lot faster than normalization and preserve length goes to 0 or infinity
        """
    @overload
    def Subtract(self,theQ : gp_Quaternion) -> None: 
        """
        Subtracts componnets of other quaternion; result is "rotations mix"

        Subtracts componnets of other quaternion; result is "rotations mix"
        """
    @overload
    def Subtract(self,theOther : gp_Quaternion) -> None: ...
    @overload
    def Subtracted(self,theQ : gp_Quaternion) -> gp_Quaternion: 
        """
        Makes difference of quaternion components; result is "rotations mix"

        Makes difference of quaternion components; result is "rotations mix"
        """
    @overload
    def Subtracted(self,theOther : gp_Quaternion) -> gp_Quaternion: ...
    def W(self) -> float: 
        """
        None

        None
        """
    def X(self) -> float: 
        """
        None

        None
        """
    def Y(self) -> float: 
        """
        None

        None
        """
    def Z(self) -> float: 
        """
        None

        None
        """
    def __add__(self,theOther : gp_Quaternion) -> gp_Quaternion: 
        """
        None
        """
    def __iadd__(self,theOther : gp_Quaternion) -> None: 
        """
        None
        """
    @overload
    def __imul__(self,theOther : gp_Quaternion) -> None: 
        """
        None

        None
        """
    @overload
    def __imul__(self,theScale : float) -> None: ...
    @overload
    def __init__(self,theVecFrom : gp_Vec,theVecTo : gp_Vec,theHelpCrossVec : gp_Vec) -> None: ...
    @overload
    def __init__(self,theVecFrom : gp_Vec,theVecTo : gp_Vec) -> None: ...
    @overload
    def __init__(self,theAxis : gp_Vec,theAngle : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theMat : gp_Mat) -> None: ...
    @overload
    def __init__(self,theToCopy : gp_Quaternion) -> None: ...
    @overload
    def __init__(self,x : float,y : float,z : float,w : float) -> None: ...
    def __isub__(self,theOther : gp_Quaternion) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,theScale : float) -> gp_Quaternion: 
        """
        None

        None

        None
        """
    @overload
    def __mul__(self,theOther : gp_Quaternion) -> gp_Quaternion: ...
    @overload
    def __mul__(self,theVec : gp_Vec) -> gp_Vec: ...
    @overload
    def __rmul__(self,theVec : gp_Vec) -> gp_Vec: 
        """
        None

        None

        None
        """
    @overload
    def __rmul__(self,theOther : gp_Quaternion) -> gp_Quaternion: ...
    @overload
    def __rmul__(self,theScale : float) -> gp_Quaternion: ...
    @overload
    def __sub__(self,theOther : gp_Quaternion) -> gp_Quaternion: 
        """
        None

        None
        """
    @overload
    def __sub__(self) -> gp_Quaternion: ...
    pass
class gp_QuaternionNLerp():
    """
    Class perform linear interpolation (approximate rotation interpolation), result quaternion nonunit, its length lay between. sqrt(2)/2 and 1.0
    """
    def Init(self,theQStart : gp_Quaternion,theQEnd : gp_Quaternion) -> None: 
        """
        Initialize the tool with Start and End values.
        """
    def InitFromUnit(self,theQStart : gp_Quaternion,theQEnd : gp_Quaternion) -> None: 
        """
        Initialize the tool with Start and End unit quaternions.
        """
    def Interpolate(self,theT : float,theResultQ : gp_Quaternion) -> None: 
        """
        Set interpolated quaternion for theT position (from 0.0 to 1.0)
        """
    @staticmethod
    def Interpolate_s(theQStart : gp_Quaternion,theQEnd : gp_Quaternion,theT : float) -> gp_Quaternion: 
        """
        Compute interpolated quaternion between two quaternions.
        """
    @overload
    def __init__(self,theQStart : gp_Quaternion,theQEnd : gp_Quaternion) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_QuaternionSLerp():
    """
    Perform Spherical Linear Interpolation of the quaternions, return unit length quaternion.
    """
    def Init(self,theQStart : gp_Quaternion,theQEnd : gp_Quaternion) -> None: 
        """
        Initialize the tool with Start and End values.
        """
    def InitFromUnit(self,theQStart : gp_Quaternion,theQEnd : gp_Quaternion) -> None: 
        """
        Initialize the tool with Start and End unit quaternions.
        """
    def Interpolate(self,theT : float,theResultQ : gp_Quaternion) -> None: 
        """
        Set interpolated quaternion for theT position (from 0.0 to 1.0)
        """
    @staticmethod
    def Interpolate_s(theQStart : gp_Quaternion,theQEnd : gp_Quaternion,theT : float) -> gp_Quaternion: 
        """
        Compute interpolated quaternion between two quaternions.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theQStart : gp_Quaternion,theQEnd : gp_Quaternion) -> None: ...
    pass
class gp_Sphere():
    """
    Describes a sphere. A sphere is defined by its radius and positioned in space with a coordinate system (a gp_Ax3 object). The origin of the coordinate system is the center of the sphere. This coordinate system is the "local coordinate system" of the sphere. Note: when a gp_Sphere sphere is converted into a Geom_SphericalSurface sphere, some implicit properties of its local coordinate system are used explicitly: - its origin, "X Direction", "Y Direction" and "main Direction" are used directly to define the parametric directions on the sphere and the origin of the parameters, - its implicit orientation (right-handed or left-handed) gives the orientation (direct, indirect) to the Geom_SphericalSurface sphere. See Also gce_MakeSphere which provides functions for more complex sphere constructions Geom_SphericalSurface which provides additional functions for constructing spheres and works, in particular, with the parametric equations of spheres.
    """
    def Area(self) -> float: 
        """
        Computes the aera of the sphere.

        Computes the aera of the sphere.
        """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float, float, float, float, float]: 
        """
        Computes the coefficients of the implicit equation of the quadric in the absolute cartesian coordinates system : A1.X**2 + A2.Y**2 + A3.Z**2 + 2.(B1.X.Y + B2.X.Z + B3.Y.Z) + 2.(C1.X + C2.Y + C3.Z) + D = 0.0
        """
    def Direct(self) -> bool: 
        """
        Returns true if the local coordinate system of this sphere is right-handed.

        Returns true if the local coordinate system of this sphere is right-handed.
        """
    def Location(self) -> gp_Pnt: 
        """
        --- Purpose ; Returns the center of the sphere.

        --- Purpose ; Returns the center of the sphere.
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: ...
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Sphere: 
        """
        Performs the symmetrical transformation of a sphere with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a sphere with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a sphere with respect to a plane. The axis placement A2 locates the plane of the of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Sphere: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Sphere: ...
    def Position(self) -> gp_Ax3: 
        """
        Returns the local coordinates system of the sphere.

        Returns the local coordinates system of the sphere.
        """
    def Radius(self) -> float: 
        """
        Returns the radius of the sphere.

        Returns the radius of the sphere.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Sphere: 
        """
        Rotates a sphere. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a sphere. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Sphere: 
        """
        Scales a sphere. S is the scaling value. The absolute value of S is used to scale the sphere

        Scales a sphere. S is the scaling value. The absolute value of S is used to scale the sphere
        """
    def SetLocation(self,Loc : gp_Pnt) -> None: 
        """
        Changes the center of the sphere.

        Changes the center of the sphere.
        """
    def SetPosition(self,A3 : gp_Ax3) -> None: 
        """
        Changes the local coordinate system of the sphere.

        Changes the local coordinate system of the sphere.
        """
    def SetRadius(self,R : float) -> None: 
        """
        Assigns R the radius of the Sphere. Warnings : It is not forbidden to create a sphere with null radius. Raises ConstructionError if R < 0.0

        Assigns R the radius of the Sphere. Warnings : It is not forbidden to create a sphere with null radius. Raises ConstructionError if R < 0.0
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Sphere: 
        """
        Transforms a sphere with the transformation T from class Trsf.

        Transforms a sphere with the transformation T from class Trsf.
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: ...
    @overload
    def Translated(self,V : gp_Vec) -> gp_Sphere: 
        """
        Translates a sphere in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a sphere from the point P1 to the point P2.

        Translates a sphere in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a sphere from the point P1 to the point P2.
        """
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Sphere: ...
    def UReverse(self) -> None: 
        """
        Reverses the U parametrization of the sphere reversing the YAxis.

        Reverses the U parametrization of the sphere reversing the YAxis.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V parametrization of the sphere reversing the ZAxis.

        Reverses the V parametrization of the sphere reversing the ZAxis.
        """
    def Volume(self) -> float: 
        """
        Computes the volume of the sphere

        Computes the volume of the sphere
        """
    def XAxis(self) -> gp_Ax1: 
        """
        Returns the axis X of the sphere.

        Returns the axis X of the sphere.
        """
    def YAxis(self) -> gp_Ax1: 
        """
        Returns the axis Y of the sphere.

        Returns the axis Y of the sphere.
        """
    @overload
    def __init__(self,A3 : gp_Ax3,Radius : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class gp_Torus():
    """
    Describes a torus. A torus is defined by its major and minor radii and positioned in space with a coordinate system (a gp_Ax3 object) as follows: - The origin of the coordinate system is the center of the torus; - The surface is obtained by rotating a circle of radius equal to the minor radius of the torus about the "main Direction" of the coordinate system. This circle is located in the plane defined by the origin, the "X Direction" and the "main Direction" of the coordinate system. It is centered on the "X Axis" of this coordinate system, and located at a distance, from the origin of this coordinate system, equal to the major radius of the torus; - The "X Direction" and "Y Direction" define the reference plane of the torus. The coordinate system described above is the "local coordinate system" of the torus. Note: when a gp_Torus torus is converted into a Geom_ToroidalSurface torus, some implicit properties of its local coordinate system are used explicitly: - its origin, "X Direction", "Y Direction" and "main Direction" are used directly to define the parametric directions on the torus and the origin of the parameters, - its implicit orientation (right-handed or left-handed) gives the orientation (direct, indirect) to the Geom_ToroidalSurface torus. See Also gce_MakeTorus which provides functions for more complex torus constructions Geom_ToroidalSurface which provides additional functions for constructing tori and works, in particular, with the parametric equations of tori.
    """
    def Area(self) -> float: 
        """
        Computes the area of the torus.

        Computes the area of the torus.
        """
    def Axis(self) -> gp_Ax1: 
        """
        returns the symmetry axis of the torus.

        returns the symmetry axis of the torus.
        """
    def Coefficients(self,Coef : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Computes the coefficients of the implicit equation of the surface in the absolute Cartesian coordinate system: Coef(1) * X^4 + Coef(2) * Y^4 + Coef(3) * Z^4 + Coef(4) * X^3 * Y + Coef(5) * X^3 * Z + Coef(6) * Y^3 * X + Coef(7) * Y^3 * Z + Coef(8) * Z^3 * X + Coef(9) * Z^3 * Y + Coef(10) * X^2 * Y^2 + Coef(11) * X^2 * Z^2 + Coef(12) * Y^2 * Z^2 + Coef(13) * X^2 * Y * Z + Coef(14) * X * Y^2 * Z + Coef(15) * X * Y * Z^2 + Coef(16) * X^3 + Coef(17) * Y^3 + Coef(18) * Z^3 + Coef(19) * X^2 * Y + Coef(20) * X^2 * Z + Coef(21) * Y^2 * X + Coef(22) * Y^2 * Z + Coef(23) * Z^2 * X + Coef(24) * Z^2 * Y + Coef(25) * X * Y * Z + Coef(26) * X^2 + Coef(27) * Y^2 + Coef(28) * Z^2 + Coef(29) * X * Y + Coef(30) * X * Z + Coef(31) * Y * Z + Coef(32) * X + Coef(33) * Y + Coef(34) * Z + Coef(35) = 0.0 Raises DimensionError if the length of Coef is lower than 35.
        """
    def Direct(self) -> bool: 
        """
        returns true if the Ax3, the local coordinate system of this torus, is right handed.

        returns true if the Ax3, the local coordinate system of this torus, is right handed.
        """
    def Location(self) -> gp_Pnt: 
        """
        Returns the Torus's location.

        Returns the Torus's location.
        """
    def MajorRadius(self) -> float: 
        """
        returns the major radius of the torus.

        returns the major radius of the torus.
        """
    def MinorRadius(self) -> float: 
        """
        returns the minor radius of the torus.

        returns the minor radius of the torus.
        """
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,P : gp_Pnt) -> None: ...
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Torus: 
        """
        Performs the symmetrical transformation of a torus with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a torus with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a torus with respect to a plane. The axis placement A2 locates the plane of the of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,P : gp_Pnt) -> gp_Torus: ...
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Torus: ...
    def Position(self) -> gp_Ax3: 
        """
        Returns the local coordinates system of the torus.

        Returns the local coordinates system of the torus.
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Torus: 
        """
        Rotates a torus. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a torus. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,P : gp_Pnt,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,P : gp_Pnt,S : float) -> gp_Torus: 
        """
        Scales a torus. S is the scaling value. The absolute value of S is used to scale the torus

        Scales a torus. S is the scaling value. The absolute value of S is used to scale the torus
        """
    def SetAxis(self,A1 : gp_Ax1) -> None: 
        """
        Modifies this torus, by redefining its local coordinate system so that: - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed). Raises ConstructionError if the direction of A1 is parallel to the "XDirection" of the coordinate system of the toroidal surface.

        Modifies this torus, by redefining its local coordinate system so that: - its origin and "main Direction" become those of the axis A1 (the "X Direction" and "Y Direction" are then recomputed). Raises ConstructionError if the direction of A1 is parallel to the "XDirection" of the coordinate system of the toroidal surface.
        """
    def SetLocation(self,Loc : gp_Pnt) -> None: 
        """
        Changes the location of the torus.

        Changes the location of the torus.
        """
    def SetMajorRadius(self,MajorRadius : float) -> None: 
        """
        Assigns value to the major radius of this torus. Raises ConstructionError if MajorRadius - MinorRadius <= Resolution()

        Assigns value to the major radius of this torus. Raises ConstructionError if MajorRadius - MinorRadius <= Resolution()
        """
    def SetMinorRadius(self,MinorRadius : float) -> None: 
        """
        Assigns value to the minor radius of this torus. Raises ConstructionError if MinorRadius < 0.0 or if MajorRadius - MinorRadius <= Resolution from gp.

        Assigns value to the minor radius of this torus. Raises ConstructionError if MinorRadius < 0.0 or if MajorRadius - MinorRadius <= Resolution from gp.
        """
    def SetPosition(self,A3 : gp_Ax3) -> None: 
        """
        Changes the local coordinate system of the surface.

        Changes the local coordinate system of the surface.
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        None

        None
        """
    def Transformed(self,T : gp_Trsf) -> gp_Torus: 
        """
        Transforms a torus with the transformation T from class Trsf.

        Transforms a torus with the transformation T from class Trsf.
        """
    @overload
    def Translate(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Translate(self,V : gp_Vec) -> None: ...
    @overload
    def Translated(self,V : gp_Vec) -> gp_Torus: 
        """
        Translates a torus in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a torus from the point P1 to the point P2.

        Translates a torus in the direction of the vector V. The magnitude of the translation is the vector's magnitude.

        Translates a torus from the point P1 to the point P2.
        """
    @overload
    def Translated(self,P1 : gp_Pnt,P2 : gp_Pnt) -> gp_Torus: ...
    def UReverse(self) -> None: 
        """
        Reverses the U parametrization of the torus reversing the YAxis.

        Reverses the U parametrization of the torus reversing the YAxis.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V parametrization of the torus reversing the ZAxis.

        Reverses the V parametrization of the torus reversing the ZAxis.
        """
    def Volume(self) -> float: 
        """
        Computes the volume of the torus.

        Computes the volume of the torus.
        """
    def XAxis(self) -> gp_Ax1: 
        """
        returns the axis X of the torus.

        returns the axis X of the torus.
        """
    def YAxis(self) -> gp_Ax1: 
        """
        returns the axis Y of the torus.

        returns the axis Y of the torus.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,A3 : gp_Ax3,MajorRadius : float,MinorRadius : float) -> None: ...
    pass
class gp_Trsf():
    """
    Defines a non-persistent transformation in 3D space. The following transformations are implemented : . Translation, Rotation, Scale . Symmetry with respect to a point, a line, a plane. Complex transformations can be obtained by combining the previous elementary transformations using the method Multiply. The transformations can be represented as follow :
    """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def Form(self) -> gp_TrsfForm: 
        """
        Returns the nature of the transformation. It can be: an identity transformation, a rotation, a translation, a mirror transformation (relative to a point, an axis or a plane), a scaling transformation, or a compound transformation.

        Returns the nature of the transformation. It can be: an identity transformation, a rotation, a translation, a mirror transformation (relative to a point, an axis or a plane), a scaling transformation, or a compound transformation.
        """
    @overload
    def GetRotation(self) -> gp_Quaternion: 
        """
        Returns the boolean True if there is non-zero rotation. In the presence of rotation, the output parameters store the axis and the angle of rotation. The method always returns positive value "theAngle", i.e., 0. < theAngle <= PI. Note that this rotation is defined only by the vectorial part of the transformation; generally you would need to check also the translational part to obtain the axis (gp_Ax1) of rotation.

        Returns quaternion representing rotational part of the transformation.
        """
    @overload
    def GetRotation(self,theAxis : gp_XYZ,theAngle : float) -> bool: ...
    def HVectorialPart(self) -> gp_Mat: 
        """
        Computes the homogeneous vectorial part of the transformation. It is a 3*3 matrix which doesn't include the scale factor. In other words, the vectorial part of this transformation is equal to its homogeneous vectorial part, multiplied by the scale factor. The coefficients of this matrix must be multiplied by the scale factor to obtain the coefficients of the transformation.

        Computes the homogeneous vectorial part of the transformation. It is a 3*3 matrix which doesn't include the scale factor. In other words, the vectorial part of this transformation is equal to its homogeneous vectorial part, multiplied by the scale factor. The coefficients of this matrix must be multiplied by the scale factor to obtain the coefficients of the transformation.
        """
    def Invert(self) -> None: 
        """
        None
        """
    def Inverted(self) -> gp_Trsf: 
        """
        Computes the reverse transformation Raises an exception if the matrix of the transformation is not inversible, it means that the scale factor is lower or equal to Resolution from package gp. Computes the transformation composed with T and <me>. In a C++ implementation you can also write Tcomposed = <me> * T. Example : Trsf T1, T2, Tcomp; ............... Tcomp = T2.Multiplied(T1); // or (Tcomp = T2 * T1) Pnt P1(10.,3.,4.); Pnt P2 = P1.Transformed(Tcomp); //using Tcomp Pnt P3 = P1.Transformed(T1); //using T1 then T2 P3.Transform(T2); // P3 = P2 !!!

        Computes the reverse transformation Raises an exception if the matrix of the transformation is not inversible, it means that the scale factor is lower or equal to Resolution from package gp. Computes the transformation composed with T and <me>. In a C++ implementation you can also write Tcomposed = <me> * T. Example : Trsf T1, T2, Tcomp; ............... Tcomp = T2.Multiplied(T1); // or (Tcomp = T2 * T1) Pnt P1(10.,3.,4.); Pnt P2 = P1.Transformed(Tcomp); //using Tcomp Pnt P3 = P1.Transformed(T1); //using T1 then T2 P3.Transform(T2); // P3 = P2 !!!
        """
    def IsNegative(self) -> bool: 
        """
        Returns true if the determinant of the vectorial part of this transformation is negative.

        Returns true if the determinant of the vectorial part of this transformation is negative.
        """
    def Multiplied(self,T : gp_Trsf) -> gp_Trsf: 
        """
        None

        None
        """
    def Multiply(self,T : gp_Trsf) -> None: 
        """
        Computes the transformation composed with <me> and T. <me> = <me> * T
        """
    def Power(self,N : int) -> None: 
        """
        None
        """
    def Powered(self,N : int) -> gp_Trsf: 
        """
        Computes the following composition of transformations <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().

        Computes the following composition of transformations <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().
        """
    def PreMultiply(self,T : gp_Trsf) -> None: 
        """
        Computes the transformation composed with <me> and T. <me> = T * <me>
        """
    def ScaleFactor(self) -> float: 
        """
        Returns the scale factor.

        Returns the scale factor.
        """
    def SetDisplacement(self,FromSystem1 : gp_Ax3,ToSystem2 : gp_Ax3) -> None: 
        """
        Modifies this transformation so that it transforms the coordinate system defined by FromSystem1 into the one defined by ToSystem2. After this modification, this transformation transforms: - the origin of FromSystem1 into the origin of ToSystem2, - the "X Direction" of FromSystem1 into the "X Direction" of ToSystem2, - the "Y Direction" of FromSystem1 into the "Y Direction" of ToSystem2, and - the "main Direction" of FromSystem1 into the "main Direction" of ToSystem2. Warning When you know the coordinates of a point in one coordinate system and you want to express these coordinates in another one, do not use the transformation resulting from this function. Use the transformation that results from SetTransformation instead. SetDisplacement and SetTransformation create related transformations: the vectorial part of one is the inverse of the vectorial part of the other.
        """
    def SetForm(self,P : gp_TrsfForm) -> None: 
        """
        None

        None
        """
    @overload
    def SetMirror(self,A2 : gp_Ax2) -> None: 
        """
        Makes the transformation into a symmetrical transformation. P is the center of the symmetry.

        Makes the transformation into a symmetrical transformation. A1 is the center of the axial symmetry.

        Makes the transformation into a symmetrical transformation. A2 is the center of the planar symmetry and defines the plane of symmetry by its origin, "X Direction" and "Y Direction".

        Makes the transformation into a symmetrical transformation. P is the center of the symmetry.
        """
    @overload
    def SetMirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def SetMirror(self,P : gp_Pnt) -> None: ...
    @overload
    def SetRotation(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        Changes the transformation into a rotation. A1 is the rotation axis and Ang is the angular value of the rotation in radians.

        Changes the transformation into a rotation defined by quaternion. Note that rotation is performed around origin, i.e. no translation is involved.
        """
    @overload
    def SetRotation(self,R : gp_Quaternion) -> None: ...
    def SetScale(self,P : gp_Pnt,S : float) -> None: 
        """
        Changes the transformation into a scale. P is the center of the scale and S is the scaling value. Raises ConstructionError If <S> is null.
        """
    def SetScaleFactor(self,S : float) -> None: 
        """
        Modifies the scale factor. Raises ConstructionError If S is null.
        """
    @overload
    def SetTransformation(self,FromSystem1 : gp_Ax3,ToSystem2 : gp_Ax3) -> None: 
        """
        Modifies this transformation so that it transforms the coordinates of any point, (x, y, z), relative to a source coordinate system into the coordinates (x', y', z') which are relative to a target coordinate system, but which represent the same point The transformation is from the coordinate system "FromSystem1" to the coordinate system "ToSystem2". Example : In a C++ implementation : Real x1, y1, z1; // are the coordinates of a point in the // local system FromSystem1 Real x2, y2, z2; // are the coordinates of a point in the // local system ToSystem2 gp_Pnt P1 (x1, y1, z1) Trsf T; T.SetTransformation (FromSystem1, ToSystem2); gp_Pnt P2 = P1.Transformed (T); P2.Coord (x2, y2, z2);

        Modifies this transformation so that it transforms the coordinates of any point, (x, y, z), relative to a source coordinate system into the coordinates (x', y', z') which are relative to a target coordinate system, but which represent the same point The transformation is from the default coordinate system {P(0.,0.,0.), VX (1.,0.,0.), VY (0.,1.,0.), VZ (0., 0. ,1.) } to the local coordinate system defined with the Ax3 ToSystem. Use in the same way as the previous method. FromSystem1 is defaulted to the absolute coordinate system.

        Sets transformation by directly specified rotation and translation.
        """
    @overload
    def SetTransformation(self,ToSystem : gp_Ax3) -> None: ...
    @overload
    def SetTransformation(self,R : gp_Quaternion,T : gp_Vec) -> None: ...
    @overload
    def SetTranslation(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: 
        """
        Changes the transformation into a translation. V is the vector of the translation.

        Makes the transformation into a translation where the translation vector is the vector (P1, P2) defined from point P1 to point P2.

        Changes the transformation into a translation. V is the vector of the translation.

        Makes the transformation into a translation where the translation vector is the vector (P1, P2) defined from point P1 to point P2.
        """
    @overload
    def SetTranslation(self,V : gp_Vec) -> None: ...
    def SetTranslationPart(self,V : gp_Vec) -> None: 
        """
        Replaces the translation vector with the vector V.
        """
    def SetValues(self,a11 : float,a12 : float,a13 : float,a14 : float,a21 : float,a22 : float,a23 : float,a24 : float,a31 : float,a32 : float,a33 : float,a34 : float) -> None: 
        """
        Sets the coefficients of the transformation. The transformation of the point x,y,z is the point x',y',z' with :
        """
    @overload
    def Transforms(self,Coord : gp_XYZ) -> None: 
        """
        Transformation of a triplet XYZ with a Trsf

        Transformation of a triplet XYZ with a Trsf

        None

        None
        """
    @overload
    def Transforms(self) -> Tuple[float, float, float]: ...
    def TranslationPart(self) -> gp_XYZ: 
        """
        Returns the translation part of the transformation's matrix

        Returns the translation part of the transformation's matrix
        """
    def Value(self,Row : int,Col : int) -> float: 
        """
        Returns the coefficients of the transformation's matrix. It is a 3 rows * 4 columns matrix. This coefficient includes the scale factor. Raises OutOfRanged if Row < 1 or Row > 3 or Col < 1 or Col > 4

        Returns the coefficients of the transformation's matrix. It is a 3 rows * 4 columns matrix. This coefficient includes the scale factor. Raises OutOfRanged if Row < 1 or Row > 3 or Col < 1 or Col > 4
        """
    def VectorialPart(self) -> gp_Mat: 
        """
        Returns the vectorial part of the transformation. It is a 3*3 matrix which includes the scale factor.
        """
    def __imul__(self,T : gp_Trsf) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,T : gp_Trsf2d) -> None: ...
    def __mul__(self,T : gp_Trsf) -> gp_Trsf: 
        """
        None
        """
    def __rmul__(self,T : gp_Trsf) -> gp_Trsf: 
        """
        None
        """
    pass
class gp_Trsf2d():
    """
    Defines a non-persistent transformation in 2D space. The following transformations are implemented : . Translation, Rotation, Scale . Symmetry with respect to a point and a line. Complex transformations can be obtained by combining the previous elementary transformations using the method Multiply. The transformations can be represented as follow :
    """
    def Form(self) -> gp_TrsfForm: 
        """
        Returns the nature of the transformation. It can be an identity transformation, a rotation, a translation, a mirror (relative to a point or an axis), a scaling transformation, or a compound transformation.

        Returns the nature of the transformation. It can be an identity transformation, a rotation, a translation, a mirror (relative to a point or an axis), a scaling transformation, or a compound transformation.
        """
    def HVectorialPart(self) -> gp_Mat2d: 
        """
        Returns the homogeneous vectorial part of the transformation. It is a 2*2 matrix which doesn't include the scale factor. The coefficients of this matrix must be multiplied by the scale factor to obtain the coefficients of the transformation.

        Returns the homogeneous vectorial part of the transformation. It is a 2*2 matrix which doesn't include the scale factor. The coefficients of this matrix must be multiplied by the scale factor to obtain the coefficients of the transformation.
        """
    def Invert(self) -> None: 
        """
        None
        """
    def Inverted(self) -> gp_Trsf2d: 
        """
        Computes the reverse transformation. Raises an exception if the matrix of the transformation is not inversible, it means that the scale factor is lower or equal to Resolution from package gp.

        Computes the reverse transformation. Raises an exception if the matrix of the transformation is not inversible, it means that the scale factor is lower or equal to Resolution from package gp.
        """
    def IsNegative(self) -> bool: 
        """
        Returns true if the determinant of the vectorial part of this transformation is negative..

        Returns true if the determinant of the vectorial part of this transformation is negative..
        """
    def Multiplied(self,T : gp_Trsf2d) -> gp_Trsf2d: 
        """
        None

        None
        """
    def Multiply(self,T : gp_Trsf2d) -> None: 
        """
        Computes the transformation composed from <me> and T. <me> = <me> * T
        """
    def Power(self,N : int) -> None: 
        """
        None
        """
    def Powered(self,N : int) -> gp_Trsf2d: 
        """
        Computes the following composition of transformations <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().

        Computes the following composition of transformations <me> * <me> * .......* <me>, N time. if N = 0 <me> = Identity if N < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().
        """
    def PreMultiply(self,T : gp_Trsf2d) -> None: 
        """
        Computes the transformation composed from <me> and T. <me> = T * <me>
        """
    def RotationPart(self) -> float: 
        """
        Returns the angle corresponding to the rotational component of the transformation matrix (operation opposite to SetRotation()).
        """
    def ScaleFactor(self) -> float: 
        """
        Returns the scale factor.

        Returns the scale factor.
        """
    @overload
    def SetMirror(self,A : gp_Ax2d) -> None: 
        """
        Changes the transformation into a symmetrical transformation. P is the center of the symmetry.

        Changes the transformation into a symmetrical transformation. A is the center of the axial symmetry.

        Changes the transformation into a symmetrical transformation. P is the center of the symmetry.
        """
    @overload
    def SetMirror(self,P : gp_Pnt2d) -> None: ...
    def SetRotation(self,P : gp_Pnt2d,Ang : float) -> None: 
        """
        Changes the transformation into a rotation. P is the rotation's center and Ang is the angular value of the rotation in radian.

        Changes the transformation into a rotation. P is the rotation's center and Ang is the angular value of the rotation in radian.
        """
    def SetScale(self,P : gp_Pnt2d,S : float) -> None: 
        """
        Changes the transformation into a scale. P is the center of the scale and S is the scaling value.

        Changes the transformation into a scale. P is the center of the scale and S is the scaling value.
        """
    def SetScaleFactor(self,S : float) -> None: 
        """
        Modifies the scale factor.
        """
    @overload
    def SetTransformation(self,FromSystem1 : gp_Ax2d,ToSystem2 : gp_Ax2d) -> None: 
        """
        Changes a transformation allowing passage from the coordinate system "FromSystem1" to the coordinate system "ToSystem2".

        Changes the transformation allowing passage from the basic coordinate system {P(0.,0.,0.), VX (1.,0.,0.), VY (0.,1.,0.)} to the local coordinate system defined with the Ax2d ToSystem.
        """
    @overload
    def SetTransformation(self,ToSystem : gp_Ax2d) -> None: ...
    @overload
    def SetTranslation(self,V : gp_Vec2d) -> None: 
        """
        Changes the transformation into a translation. V is the vector of the translation.

        Makes the transformation into a translation from the point P1 to the point P2.

        Changes the transformation into a translation. V is the vector of the translation.

        Makes the transformation into a translation from the point P1 to the point P2.
        """
    @overload
    def SetTranslation(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: ...
    def SetTranslationPart(self,V : gp_Vec2d) -> None: 
        """
        Replaces the translation vector with V.
        """
    def SetValues(self,a11 : float,a12 : float,a13 : float,a21 : float,a22 : float,a23 : float) -> None: 
        """
        Sets the coefficients of the transformation. The transformation of the point x,y is the point x',y' with :
        """
    @overload
    def Transforms(self,Coord : gp_XY) -> None: 
        """
        Transforms a doublet XY with a Trsf2d

        Transforms a doublet XY with a Trsf2d

        None

        None
        """
    @overload
    def Transforms(self) -> Tuple[float, float]: ...
    def TranslationPart(self) -> gp_XY: 
        """
        Returns the translation part of the transformation's matrix

        Returns the translation part of the transformation's matrix
        """
    def Value(self,Row : int,Col : int) -> float: 
        """
        Returns the coefficients of the transformation's matrix. It is a 2 rows * 3 columns matrix. Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 3

        Returns the coefficients of the transformation's matrix. It is a 2 rows * 3 columns matrix. Raises OutOfRange if Row < 1 or Row > 2 or Col < 1 or Col > 3
        """
    def VectorialPart(self) -> gp_Mat2d: 
        """
        Returns the vectorial part of the transformation. It is a 2*2 matrix which includes the scale factor.
        """
    def __imul__(self,T : gp_Trsf2d) -> None: 
        """
        None
        """
    @overload
    def __init__(self,T : gp_Trsf) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __mul__(self,T : gp_Trsf2d) -> gp_Trsf2d: 
        """
        None
        """
    def __rmul__(self,T : gp_Trsf2d) -> gp_Trsf2d: 
        """
        None
        """
    pass
class gp_TrsfForm():
    """
    Identifies the type of a geometric transformation.

    Members:

      gp_Identity

      gp_Rotation

      gp_Translation

      gp_PntMirror

      gp_Ax1Mirror

      gp_Ax2Mirror

      gp_Scale

      gp_CompoundTrsf

      gp_Other
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    __entries: dict # value = {'gp_Identity': (gp_TrsfForm.gp_Identity, None), 'gp_Rotation': (gp_TrsfForm.gp_Rotation, None), 'gp_Translation': (gp_TrsfForm.gp_Translation, None), 'gp_PntMirror': (gp_TrsfForm.gp_PntMirror, None), 'gp_Ax1Mirror': (gp_TrsfForm.gp_Ax1Mirror, None), 'gp_Ax2Mirror': (gp_TrsfForm.gp_Ax2Mirror, None), 'gp_Scale': (gp_TrsfForm.gp_Scale, None), 'gp_CompoundTrsf': (gp_TrsfForm.gp_CompoundTrsf, None), 'gp_Other': (gp_TrsfForm.gp_Other, None)}
    __members__: dict # value = {'gp_Identity': gp_TrsfForm.gp_Identity, 'gp_Rotation': gp_TrsfForm.gp_Rotation, 'gp_Translation': gp_TrsfForm.gp_Translation, 'gp_PntMirror': gp_TrsfForm.gp_PntMirror, 'gp_Ax1Mirror': gp_TrsfForm.gp_Ax1Mirror, 'gp_Ax2Mirror': gp_TrsfForm.gp_Ax2Mirror, 'gp_Scale': gp_TrsfForm.gp_Scale, 'gp_CompoundTrsf': gp_TrsfForm.gp_CompoundTrsf, 'gp_Other': gp_TrsfForm.gp_Other}
    gp_Ax1Mirror: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Ax1Mirror
    gp_Ax2Mirror: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Ax2Mirror
    gp_CompoundTrsf: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_CompoundTrsf
    gp_Identity: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Identity
    gp_Other: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Other
    gp_PntMirror: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_PntMirror
    gp_Rotation: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Rotation
    gp_Scale: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Scale
    gp_Translation: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Translation
    pass
class gp_Vec():
    """
    Defines a non-persistent vector in 3D space.
    """
    def Add(self,Other : gp_Vec) -> None: 
        """
        Adds two vectors

        Adds two vectors
        """
    def Added(self,Other : gp_Vec) -> gp_Vec: 
        """
        Adds two vectors

        Adds two vectors
        """
    def Angle(self,Other : gp_Vec) -> float: 
        """
        Computes the angular value between <me> and <Other> Returns the angle value between 0 and PI in radian. Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution from gp or Other.Magnitude() <= Resolution because the angular value is indefinite if one of the vectors has a null magnitude.

        Computes the angular value between <me> and <Other> Returns the angle value between 0 and PI in radian. Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution from gp or Other.Magnitude() <= Resolution because the angular value is indefinite if one of the vectors has a null magnitude.
        """
    @overload
    def AngleWithRef(self,Other : gp_Vec,VRef : gp_Vec) -> float: 
        """
        Computes the angle, in radians, between this vector and vector Other. The result is a value between -Pi and Pi. For this, VRef defines the positive sense of rotation: the angular value is positive, if the cross product this ^ Other has the same orientation as VRef relative to the plane defined by the vectors this and Other. Otherwise, the angular value is negative. Exceptions gp_VectorWithNullMagnitude if the magnitude of this vector, the vector Other, or the vector VRef is less than or equal to gp::Resolution(). Standard_DomainError if this vector, the vector Other, and the vector VRef are coplanar, unless this vector and the vector Other are parallel.

        Computes the angle, in radians, between this vector and vector Other. The result is a value between -Pi and Pi. For this, VRef defines the positive sense of rotation: the angular value is positive, if the cross product this ^ Other has the same orientation as VRef relative to the plane defined by the vectors this and Other. Otherwise, the angular value is negative. Exceptions gp_VectorWithNullMagnitude if the magnitude of this vector, the vector Other, or the vector VRef is less than or equal to gp::Resolution(). Standard_DomainError if this vector, the vector Other, and the vector VRef are coplanar, unless this vector and the vector Other are parallel.
        """
    @overload
    def AngleWithRef(self,Other : gp_Vec,Vref : gp_Vec) -> float: ...
    @overload
    def Coord(self,Index : int) -> float: 
        """
        Returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned Raised if Index != {1, 2, 3}.

        Returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned Raised if Index != {1, 2, 3}.

        For this vector returns its three coordinates Xv, Yv, and Zvinline

        For this vector returns its three coordinates Xv, Yv, and Zvinline
        """
    @overload
    def Coord(self) -> Tuple[float, float, float]: ...
    def Cross(self,Right : gp_Vec) -> None: 
        """
        computes the cross product between two vectors

        computes the cross product between two vectors
        """
    def CrossCross(self,V1 : gp_Vec,V2 : gp_Vec) -> None: 
        """
        Computes the triple vector product. <me> ^= (V1 ^ V2)

        Computes the triple vector product. <me> ^= (V1 ^ V2)
        """
    def CrossCrossed(self,V1 : gp_Vec,V2 : gp_Vec) -> gp_Vec: 
        """
        Computes the triple vector product. <me> ^ (V1 ^ V2)

        Computes the triple vector product. <me> ^ (V1 ^ V2)
        """
    def CrossMagnitude(self,Right : gp_Vec) -> float: 
        """
        Computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||

        Computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||
        """
    def CrossSquareMagnitude(self,Right : gp_Vec) -> float: 
        """
        Computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2

        Computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2
        """
    def Crossed(self,Right : gp_Vec) -> gp_Vec: 
        """
        computes the cross product between two vectors

        computes the cross product between two vectors
        """
    def Divide(self,Scalar : float) -> None: 
        """
        Divides a vector by a scalar

        Divides a vector by a scalar
        """
    def Divided(self,Scalar : float) -> gp_Vec: 
        """
        Divides a vector by a scalar

        Divides a vector by a scalar
        """
    def Dot(self,Other : gp_Vec) -> float: 
        """
        computes the scalar product

        computes the scalar product
        """
    def DotCross(self,V1 : gp_Vec,V2 : gp_Vec) -> float: 
        """
        Computes the triple scalar product <me> * (V1 ^ V2).

        Computes the triple scalar product <me> * (V1 ^ V2).
        """
    def IsEqual(self,Other : gp_Vec,LinearTolerance : float,AngularTolerance : float) -> bool: 
        """
        Returns True if the two vectors have the same magnitude value and the same direction. The precision values are LinearTolerance for the magnitude and AngularTolerance for the direction.
        """
    def IsNormal(self,Other : gp_Vec,AngularTolerance : float) -> bool: 
        """
        Returns True if abs(<me>.Angle(Other) - PI/2.) <= AngularTolerance Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp

        Returns True if abs(<me>.Angle(Other) - PI/2.) <= AngularTolerance Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp
        """
    def IsOpposite(self,Other : gp_Vec,AngularTolerance : float) -> bool: 
        """
        Returns True if PI - <me>.Angle(Other) <= AngularTolerance Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp

        Returns True if PI - <me>.Angle(Other) <= AngularTolerance Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp
        """
    def IsParallel(self,Other : gp_Vec,AngularTolerance : float) -> bool: 
        """
        Returns True if Angle(<me>, Other) <= AngularTolerance or PI - Angle(<me>, Other) <= AngularTolerance This definition means that two parallel vectors cannot define a plane but two vectors with opposite directions are considered as parallel. Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp

        Returns True if Angle(<me>, Other) <= AngularTolerance or PI - Angle(<me>, Other) <= AngularTolerance This definition means that two parallel vectors cannot define a plane but two vectors with opposite directions are considered as parallel. Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp
        """
    def Magnitude(self) -> float: 
        """
        Computes the magnitude of this vector.

        Computes the magnitude of this vector.
        """
    @overload
    def Mirror(self,V : gp_Vec) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Mirror(self,A2 : gp_Ax2) -> None: ...
    @overload
    def Mirror(self,A1 : gp_Ax1) -> None: ...
    @overload
    def Mirrored(self,A1 : gp_Ax1) -> gp_Vec: 
        """
        Performs the symmetrical transformation of a vector with respect to the vector V which is the center of the symmetry.

        Performs the symmetrical transformation of a vector with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a vector with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirrored(self,A2 : gp_Ax2) -> gp_Vec: ...
    @overload
    def Mirrored(self,V : gp_Vec) -> gp_Vec: ...
    def Multiplied(self,Scalar : float) -> gp_Vec: 
        """
        Multiplies a vector by a scalar

        Multiplies a vector by a scalar
        """
    def Multiply(self,Scalar : float) -> None: 
        """
        Multiplies a vector by a scalar

        Multiplies a vector by a scalar
        """
    def Normalize(self) -> None: 
        """
        normalizes a vector Raises an exception if the magnitude of the vector is lower or equal to Resolution from gp.

        normalizes a vector Raises an exception if the magnitude of the vector is lower or equal to Resolution from gp.
        """
    def Normalized(self) -> gp_Vec: 
        """
        normalizes a vector Raises an exception if the magnitude of the vector is lower or equal to Resolution from gp.

        normalizes a vector Raises an exception if the magnitude of the vector is lower or equal to Resolution from gp.
        """
    def Reverse(self) -> None: 
        """
        Reverses the direction of a vector

        Reverses the direction of a vector
        """
    def Reversed(self) -> gp_Vec: 
        """
        Reverses the direction of a vector

        Reverses the direction of a vector
        """
    def Rotate(self,A1 : gp_Ax1,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,A1 : gp_Ax1,Ang : float) -> gp_Vec: 
        """
        Rotates a vector. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.

        Rotates a vector. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,S : float) -> gp_Vec: 
        """
        Scales a vector. S is the scaling value.

        Scales a vector. S is the scaling value.
        """
    @overload
    def SetCoord(self,Index : int,Xi : float) -> None: 
        """
        Changes the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Index = 3 => Z is modified Raised if Index != {1, 2, 3}.

        For this vector, assigns - the values Xv, Yv and Zv to its three coordinates.

        Changes the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Index = 3 => Z is modified Raised if Index != {1, 2, 3}.

        For this vector, assigns - the values Xv, Yv and Zv to its three coordinates.
        """
    @overload
    def SetCoord(self,Xv : float,Yv : float,Zv : float) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,V1 : gp_Vec,A2 : float,V2 : gp_Vec) -> None: 
        """
        <me> is set to the following linear form : A1 * V1 + A2 * V2 + A3 * V3 + V4

        <me> is set to the following linear form : A1 * V1 + A2 * V2 + A3 * V3

        <me> is set to the following linear form : A1 * V1 + A2 * V2 + V3

        <me> is set to the following linear form : A1 * V1 + A2 * V2

        <me> is set to the following linear form : A1 * V1 + V2

        <me> is set to the following linear form : V1 + V2

        <me> is set to the following linear form : A1 * V1 + A2 * V2

        <me> is set to the following linear form : A1 * V1 + V2

        <me> is set to the following linear form : V1 + V2

        <me> is set to the following linear form : A1 * V1 + A2 * V2 + A3 * V3

        <me> is set to the following linear form : A1 * V1 + A2 * V2 + V3

        <me> is set to the following linear form : A1 * V1 + A2 * V2 + A3 * V3 + V4
        """
    @overload
    def SetLinearForm(self,A1 : float,V1 : gp_Vec,A2 : float,V2 : gp_Vec,A3 : float,V3 : gp_Vec,V4 : gp_Vec) -> None: ...
    @overload
    def SetLinearForm(self,V1 : gp_Vec,V2 : gp_Vec) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,V1 : gp_Vec,A2 : float,V2 : gp_Vec,A3 : float,V3 : gp_Vec) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : gp_Vec,Right : gp_Vec) -> None: ...
    @overload
    def SetLinearForm(self,Left : gp_Vec,Right : gp_Vec) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,V1 : gp_Vec,A2 : float,V2 : gp_Vec,V3 : gp_Vec) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,V1 : gp_Vec,V2 : gp_Vec) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : gp_Vec,R : float,Right : gp_Vec) -> None: ...
    def SetX(self,X : float) -> None: 
        """
        Assigns the given value to the X coordinate of this vector.

        Assigns the given value to the X coordinate of this vector.
        """
    def SetXYZ(self,Coord : gp_XYZ) -> None: 
        """
        Assigns the three coordinates of Coord to this vector.

        Assigns the three coordinates of Coord to this vector.
        """
    def SetY(self,Y : float) -> None: 
        """
        Assigns the given value to the X coordinate of this vector.

        Assigns the given value to the X coordinate of this vector.
        """
    def SetZ(self,Z : float) -> None: 
        """
        Assigns the given value to the X coordinate of this vector.

        Assigns the given value to the X coordinate of this vector.
        """
    def SquareMagnitude(self) -> float: 
        """
        Computes the square magnitude of this vector.

        Computes the square magnitude of this vector.
        """
    def Subtract(self,Right : gp_Vec) -> None: 
        """
        Subtracts two vectors

        Subtracts two vectors
        """
    def Subtracted(self,Right : gp_Vec) -> gp_Vec: 
        """
        Subtracts two vectors

        Subtracts two vectors
        """
    def Transform(self,T : gp_Trsf) -> None: 
        """
        Transforms a vector with the transformation T.
        """
    def Transformed(self,T : gp_Trsf) -> gp_Vec: 
        """
        Transforms a vector with the transformation T.

        Transforms a vector with the transformation T.
        """
    def X(self) -> float: 
        """
        For this vector, returns its X coordinate.

        For this vector, returns its X coordinate.
        """
    def XYZ(self) -> gp_XYZ: 
        """
        For this vector, returns - its three coordinates as a number triple

        For this vector, returns - its three coordinates as a number triple
        """
    def Y(self) -> float: 
        """
        For this vector, returns its Y coordinate.

        For this vector, returns its Y coordinate.
        """
    def Z(self) -> float: 
        """
        For this vector, returns its Z coordinate.

        For this vector, returns its Z coordinate.
        """
    def __add__(self,Other : gp_Vec) -> gp_Vec: 
        """
        None
        """
    def __iadd__(self,Other : gp_Vec) -> None: 
        """
        None
        """
    def __imul__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __init__(self,P1 : gp_Pnt,P2 : gp_Pnt) -> None: ...
    @overload
    def __init__(self,V : gp_Dir) -> None: ...
    @overload
    def __init__(self,Xv : float,Yv : float,Zv : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Coord : gp_XYZ) -> None: ...
    def __ipow__(self,Right : gp_Vec) -> None: 
        """
        None
        """
    def __isub__(self,Right : gp_Vec) -> None: 
        """
        None
        """
    def __itruediv__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,Scalar : float) -> gp_Vec: 
        """
        None

        None
        """
    @overload
    def __mul__(self,Other : gp_Vec) -> float: ...
    def __pow__(self,Right : gp_Vec) -> gp_Vec: 
        """
        None
        """
    @overload
    def __rmul__(self,Scalar : float) -> gp_Vec: 
        """
        None

        None
        """
    @overload
    def __rmul__(self,Other : gp_Vec) -> float: ...
    @overload
    def __sub__(self,Right : gp_Vec) -> gp_Vec: 
        """
        None

        None
        """
    @overload
    def __sub__(self) -> gp_Vec: ...
    def __truediv__(self,Scalar : float) -> gp_Vec: 
        """
        None
        """
    pass
class gp_Vec2d():
    """
    Defines a non-persistent vector in 2D space.
    """
    def Add(self,Other : gp_Vec2d) -> None: 
        """
        None

        None
        """
    def Added(self,Other : gp_Vec2d) -> gp_Vec2d: 
        """
        Adds two vectors

        Adds two vectors
        """
    def Angle(self,Other : gp_Vec2d) -> float: 
        """
        Computes the angular value between <me> and <Other> returns the angle value between -PI and PI in radian. The orientation is from <me> to Other. The positive sense is the trigonometric sense. Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution from gp or Other.Magnitude() <= Resolution because the angular value is indefinite if one of the vectors has a null magnitude.
        """
    @overload
    def Coord(self) -> Tuple[float, float]: 
        """
        Returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Raised if Index != {1, 2}.

        Returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Raised if Index != {1, 2}.

        For this vector, returns its two coordinates Xv and Yv

        For this vector, returns its two coordinates Xv and Yv
        """
    @overload
    def Coord(self,Index : int) -> float: ...
    def CrossMagnitude(self,Right : gp_Vec2d) -> float: 
        """
        Computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||

        Computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||
        """
    def CrossSquareMagnitude(self,Right : gp_Vec2d) -> float: 
        """
        Computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2

        Computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2
        """
    def Crossed(self,Right : gp_Vec2d) -> float: 
        """
        Computes the crossing product between two vectors

        Computes the crossing product between two vectors
        """
    def Divide(self,Scalar : float) -> None: 
        """
        None

        None
        """
    def Divided(self,Scalar : float) -> gp_Vec2d: 
        """
        divides a vector by a scalar

        divides a vector by a scalar
        """
    def Dot(self,Other : gp_Vec2d) -> float: 
        """
        Computes the scalar product

        Computes the scalar product
        """
    def GetNormal(self) -> gp_Vec2d: 
        """
        None

        None
        """
    def IsEqual(self,Other : gp_Vec2d,LinearTolerance : float,AngularTolerance : float) -> bool: 
        """
        Returns True if the two vectors have the same magnitude value and the same direction. The precision values are LinearTolerance for the magnitude and AngularTolerance for the direction.
        """
    @overload
    def IsNormal(self,theOther : gp_Vec2d,theAngularTolerance : float) -> bool: 
        """
        Returns True if abs(Abs(<me>.Angle(Other)) - PI/2.) <= AngularTolerance Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp.

        Returns True if abs(Abs(<me>.Angle(Other)) - PI/2.) <= AngularTolerance Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp.
        """
    @overload
    def IsNormal(self,Other : gp_Vec2d,AngularTolerance : float) -> bool: ...
    def IsOpposite(self,Other : gp_Vec2d,AngularTolerance : float) -> bool: 
        """
        Returns True if PI - Abs(<me>.Angle(Other)) <= AngularTolerance Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp.

        Returns True if PI - Abs(<me>.Angle(Other)) <= AngularTolerance Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp.
        """
    def IsParallel(self,Other : gp_Vec2d,AngularTolerance : float) -> bool: 
        """
        Returns true if Abs(Angle(<me>, Other)) <= AngularTolerance or PI - Abs(Angle(<me>, Other)) <= AngularTolerance Two vectors with opposite directions are considered as parallel. Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp

        Returns true if Abs(Angle(<me>, Other)) <= AngularTolerance or PI - Abs(Angle(<me>, Other)) <= AngularTolerance Two vectors with opposite directions are considered as parallel. Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or Other.Magnitude() <= Resolution from gp
        """
    def Magnitude(self) -> float: 
        """
        Computes the magnitude of this vector.

        Computes the magnitude of this vector.
        """
    @overload
    def Mirror(self,V : gp_Vec2d) -> None: 
        """
        Performs the symmetrical transformation of a vector with respect to the vector V which is the center of the symmetry.

        Performs the symmetrical transformation of a vector with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirror(self,A1 : gp_Ax2d) -> None: ...
    @overload
    def Mirrored(self,V : gp_Vec2d) -> gp_Vec2d: 
        """
        Performs the symmetrical transformation of a vector with respect to the vector V which is the center of the symmetry.

        Performs the symmetrical transformation of a vector with respect to an axis placement which is the axis of the symmetry.
        """
    @overload
    def Mirrored(self,A1 : gp_Ax2d) -> gp_Vec2d: ...
    def Multiplied(self,Scalar : float) -> gp_Vec2d: 
        """
        Normalizes a vector Raises an exception if the magnitude of the vector is lower or equal to Resolution from package gp.

        Normalizes a vector Raises an exception if the magnitude of the vector is lower or equal to Resolution from package gp.
        """
    def Multiply(self,Scalar : float) -> None: 
        """
        None

        None
        """
    def Normalize(self) -> None: 
        """
        None

        None
        """
    def Normalized(self) -> gp_Vec2d: 
        """
        Normalizes a vector Raises an exception if the magnitude of the vector is lower or equal to Resolution from package gp. Reverses the direction of a vector

        Normalizes a vector Raises an exception if the magnitude of the vector is lower or equal to Resolution from package gp. Reverses the direction of a vector
        """
    def Reverse(self) -> None: 
        """
        None

        None
        """
    def Reversed(self) -> gp_Vec2d: 
        """
        Reverses the direction of a vector

        Reverses the direction of a vector
        """
    def Rotate(self,Ang : float) -> None: 
        """
        None

        None
        """
    def Rotated(self,Ang : float) -> gp_Vec2d: 
        """
        Rotates a vector. Ang is the angular value of the rotation in radians.

        Rotates a vector. Ang is the angular value of the rotation in radians.
        """
    def Scale(self,S : float) -> None: 
        """
        None

        None
        """
    def Scaled(self,S : float) -> gp_Vec2d: 
        """
        Scales a vector. S is the scaling value.

        Scales a vector. S is the scaling value.
        """
    @overload
    def SetCoord(self,Xv : float,Yv : float) -> None: 
        """
        Changes the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Raises OutOfRange if Index != {1, 2}.

        For this vector, assigns the values Xv and Yv to its two coordinates

        Changes the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Raises OutOfRange if Index != {1, 2}.

        For this vector, assigns the values Xv and Yv to its two coordinates
        """
    @overload
    def SetCoord(self,Index : int,Xi : float) -> None: ...
    @overload
    def SetLinearForm(self,Left : gp_Vec2d,Right : gp_Vec2d) -> None: 
        """
        <me> is set to the following linear form : A1 * V1 + A2 * V2 + V3

        <me> is set to the following linear form : A1 * V1 + A2 * V2

        <me> is set to the following linear form : A1 * V1 + V2

        <me> is set to the following linear form : Left + Right

        <me> is set to the following linear form : A1 * V1 + A2 * V2

        <me> is set to the following linear form : A1 * V1 + V2

        <me> is set to the following linear form : Left + Right

        <me> is set to the following linear form : A1 * V1 + A2 * V2 + V3
        """
    @overload
    def SetLinearForm(self,A1 : float,V1 : gp_Vec2d,A2 : float,V2 : gp_Vec2d) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,V1 : gp_Vec2d,V2 : gp_Vec2d) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,V1 : gp_Vec2d,A2 : float,V2 : gp_Vec2d,V3 : gp_Vec2d) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : gp_Vec2d,R : float,Right : gp_Vec2d) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : gp_Vec2d,Right : gp_Vec2d) -> None: ...
    def SetX(self,X : float) -> None: 
        """
        Assigns the given value to the X coordinate of this vector.

        Assigns the given value to the X coordinate of this vector.
        """
    def SetXY(self,Coord : gp_XY) -> None: 
        """
        Assigns the two coordinates of Coord to this vector.

        Assigns the two coordinates of Coord to this vector.
        """
    def SetY(self,Y : float) -> None: 
        """
        Assigns the given value to the Y coordinate of this vector.

        Assigns the given value to the Y coordinate of this vector.
        """
    def SquareMagnitude(self) -> float: 
        """
        Computes the square magnitude of this vector.

        Computes the square magnitude of this vector.
        """
    def Subtract(self,Right : gp_Vec2d) -> None: 
        """
        Subtracts two vectors

        Subtracts two vectors
        """
    def Subtracted(self,Right : gp_Vec2d) -> gp_Vec2d: 
        """
        Subtracts two vectors

        Subtracts two vectors
        """
    def Transform(self,T : gp_Trsf2d) -> None: 
        """
        None
        """
    def Transformed(self,T : gp_Trsf2d) -> gp_Vec2d: 
        """
        Transforms a vector with a Trsf from gp.

        Transforms a vector with a Trsf from gp.
        """
    def X(self) -> float: 
        """
        For this vector, returns its X coordinate.

        For this vector, returns its X coordinate.
        """
    def XY(self) -> gp_XY: 
        """
        For this vector, returns its two coordinates as a number pair

        For this vector, returns its two coordinates as a number pair
        """
    def Y(self) -> float: 
        """
        For this vector, returns its Y coordinate.

        For this vector, returns its Y coordinate.
        """
    def __add__(self,Other : gp_Vec2d) -> gp_Vec2d: 
        """
        None
        """
    def __iadd__(self,Other : gp_Vec2d) -> None: 
        """
        None
        """
    def __imul__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Xv : float,Yv : float) -> None: ...
    @overload
    def __init__(self,V : gp_Dir2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Coord : gp_XY) -> None: ...
    @overload
    def __init__(self,P1 : gp_Pnt2d,P2 : gp_Pnt2d) -> None: ...
    def __isub__(self,Right : gp_Vec2d) -> None: 
        """
        None
        """
    def __itruediv__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,Other : gp_Vec2d) -> float: 
        """
        None

        None
        """
    @overload
    def __mul__(self,Scalar : float) -> gp_Vec2d: ...
    def __pow__(self,Right : gp_Vec2d) -> float: 
        """
        None
        """
    @overload
    def __rmul__(self,Other : gp_Vec2d) -> float: 
        """
        None

        None
        """
    @overload
    def __rmul__(self,Scalar : float) -> gp_Vec2d: ...
    @overload
    def __sub__(self) -> gp_Vec2d: 
        """
        None

        None
        """
    @overload
    def __sub__(self,Right : gp_Vec2d) -> gp_Vec2d: ...
    def __truediv__(self,Scalar : float) -> gp_Vec2d: 
        """
        None
        """
    pass
class gp_VectorWithNullMagnitude(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.gp', '__weakref__': <attribute '__weakref__' of 'gp_VectorWithNullMagnitude' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'gp_VectorWithNullMagnitude' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class gp_XY():
    """
    This class describes a cartesian coordinate entity in 2D space {X,Y}. This class is non persistent. This entity used for algebraic calculation. An XY can be transformed with a Trsf2d or a GTrsf2d from package gp. It is used in vectorial computations or for holding this type of information in data structures.
    """
    def Add(self,Other : gp_XY) -> None: 
        """
        Computes the sum of this number pair and number pair Other <me>.X() = <me>.X() + Other.X() <me>.Y() = <me>.Y() + Other.Y()

        Computes the sum of this number pair and number pair Other <me>.X() = <me>.X() + Other.X() <me>.Y() = <me>.Y() + Other.Y()
        """
    def Added(self,Other : gp_XY) -> gp_XY: 
        """
        Computes the sum of this number pair and number pair Other new.X() = <me>.X() + Other.X() new.Y() = <me>.Y() + Other.Y()

        Computes the sum of this number pair and number pair Other new.X() = <me>.X() + Other.X() new.Y() = <me>.Y() + Other.Y()
        """
    def ChangeCoord(self,theIndex : int) -> float: 
        """
        None

        None
        """
    @overload
    def Coord(self,Index : int) -> float: 
        """
        returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Raises OutOfRange if Index != {1, 2}.

        returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Raises OutOfRange if Index != {1, 2}.

        For this number pair, returns its coordinates X and Y.

        For this number pair, returns its coordinates X and Y.
        """
    @overload
    def Coord(self) -> Tuple[float, float]: ...
    @overload
    def Coord(self,i : int) -> float: ...
    def CrossMagnitude(self,Right : gp_XY) -> float: 
        """
        computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||

        computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||
        """
    def CrossSquareMagnitude(self,Right : gp_XY) -> float: 
        """
        computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2

        computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2
        """
    def Crossed(self,Right : gp_XY) -> float: 
        """
        Real D = <me>.X() * Other.Y() - <me>.Y() * Other.X()

        Real D = <me>.X() * Other.Y() - <me>.Y() * Other.X()
        """
    def Divide(self,Scalar : float) -> None: 
        """
        divides <me> by a real.

        divides <me> by a real.
        """
    def Divided(self,Scalar : float) -> gp_XY: 
        """
        Divides <me> by a real.

        Divides <me> by a real.
        """
    def Dot(self,Other : gp_XY) -> float: 
        """
        Computes the scalar product between <me> and Other

        Computes the scalar product between <me> and Other
        """
    def IsEqual(self,Other : gp_XY,Tolerance : float) -> bool: 
        """
        Returns true if the coordinates of this number pair are equal to the respective coordinates of the number pair Other, within the specified tolerance Tolerance. I.e.: abs(<me>.X() - Other.X()) <= Tolerance and abs(<me>.Y() - Other.Y()) <= Tolerance and computations
        """
    def Modulus(self) -> float: 
        """
        Computes Sqrt (X*X + Y*Y) where X and Y are the two coordinates of this number pair.

        Computes Sqrt (X*X + Y*Y) where X and Y are the two coordinates of this number pair.
        """
    @overload
    def Multiplied(self,Matrix : gp_Mat2d) -> gp_XY: 
        """
        New.X() = <me>.X() * Scalar; New.Y() = <me>.Y() * Scalar;

        new.X() = <me>.X() * Other.X(); new.Y() = <me>.Y() * Other.Y();

        New = Matrix * <me>

        New.X() = <me>.X() * Scalar; New.Y() = <me>.Y() * Scalar;

        new.X() = <me>.X() * Other.X(); new.Y() = <me>.Y() * Other.Y();

        New = Matrix * <me>
        """
    @overload
    def Multiplied(self,Other : gp_XY) -> gp_XY: ...
    @overload
    def Multiplied(self,Scalar : float) -> gp_XY: ...
    @overload
    def Multiply(self,Matrix : gp_Mat2d) -> None: 
        """
        <me>.X() = <me>.X() * Scalar; <me>.Y() = <me>.Y() * Scalar;

        <me>.X() = <me>.X() * Other.X(); <me>.Y() = <me>.Y() * Other.Y();

        <me> = Matrix * <me>

        <me>.X() = <me>.X() * Scalar; <me>.Y() = <me>.Y() * Scalar;

        <me>.X() = <me>.X() * Other.X(); <me>.Y() = <me>.Y() * Other.Y();

        <me> = Matrix * <me>
        """
    @overload
    def Multiply(self,Other : gp_XY) -> None: ...
    @overload
    def Multiply(self,Scalar : float) -> None: ...
    def Normalize(self) -> None: 
        """
        <me>.X() = <me>.X()/ <me>.Modulus() <me>.Y() = <me>.Y()/ <me>.Modulus() Raises ConstructionError if <me>.Modulus() <= Resolution from gp

        <me>.X() = <me>.X()/ <me>.Modulus() <me>.Y() = <me>.Y()/ <me>.Modulus() Raises ConstructionError if <me>.Modulus() <= Resolution from gp
        """
    def Normalized(self) -> gp_XY: 
        """
        New.X() = <me>.X()/ <me>.Modulus() New.Y() = <me>.Y()/ <me>.Modulus() Raises ConstructionError if <me>.Modulus() <= Resolution from gp

        New.X() = <me>.X()/ <me>.Modulus() New.Y() = <me>.Y()/ <me>.Modulus() Raises ConstructionError if <me>.Modulus() <= Resolution from gp
        """
    def Reverse(self) -> None: 
        """
        <me>.X() = -<me>.X() <me>.Y() = -<me>.Y()

        <me>.X() = -<me>.X() <me>.Y() = -<me>.Y()
        """
    def Reversed(self) -> gp_XY: 
        """
        New.X() = -<me>.X() New.Y() = -<me>.Y()

        New.X() = -<me>.X() New.Y() = -<me>.Y()
        """
    @overload
    def SetCoord(self,X : float,Y : float) -> None: 
        """
        modifies the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Raises OutOfRange if Index != {1, 2}.

        For this number pair, assigns the values X and Y to its coordinates

        modifies the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Raises OutOfRange if Index != {1, 2}.

        For this number pair, assigns the values X and Y to its coordinates
        """
    @overload
    def SetCoord(self,Index : int,Xi : float) -> None: ...
    @overload
    def SetCoord(self,i : int,X : float) -> None: ...
    @overload
    def SetLinearForm(self,Left : gp_XY,Right : gp_XY) -> None: 
        """
        Computes the following linear combination and assigns the result to this number pair: A1 * XY1 + A2 * XY2

        -- Computes the following linear combination and assigns the result to this number pair: A1 * XY1 + A2 * XY2 + XY3

        Computes the following linear combination and assigns the result to this number pair: A1 * XY1 + XY2

        Computes the following linear combination and assigns the result to this number pair: XY1 + XY2

        Computes the following linear combination and assigns the result to this number pair: A1 * XY1 + A2 * XY2

        Computes the following linear combination and assigns the result to this number pair: A1 * XY1 + XY2

        Computes the following linear combination and assigns the result to this number pair: XY1 + XY2

        -- Computes the following linear combination and assigns the result to this number pair: A1 * XY1 + A2 * XY2 + XY3
        """
    @overload
    def SetLinearForm(self,A1 : float,XY1 : gp_XY,A2 : float,XY2 : gp_XY) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : gp_XY,R : float,Right : gp_XY) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XY1 : gp_XY,A2 : float,XY2 : gp_XY,XY3 : gp_XY) -> None: ...
    @overload
    def SetLinearForm(self,XY1 : gp_XY,XY2 : gp_XY) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XY1 : gp_XY,XY2 : gp_XY) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : gp_XY,Right : gp_XY) -> None: ...
    def SetX(self,X : float) -> None: 
        """
        Assigns the given value to the X coordinate of this number pair.

        Assigns the given value to the X coordinate of this number pair.
        """
    def SetY(self,Y : float) -> None: 
        """
        Assigns the given value to the Y coordinate of this number pair.

        Assigns the given value to the Y coordinate of this number pair.
        """
    def SquareModulus(self) -> float: 
        """
        Computes X*X + Y*Y where X and Y are the two coordinates of this number pair.

        Computes X*X + Y*Y where X and Y are the two coordinates of this number pair.
        """
    def Subtract(self,Right : gp_XY) -> None: 
        """
        <me>.X() = <me>.X() - Other.X() <me>.Y() = <me>.Y() - Other.Y()

        <me>.X() = <me>.X() - Other.X() <me>.Y() = <me>.Y() - Other.Y()
        """
    def Subtracted(self,Right : gp_XY) -> gp_XY: 
        """
        new.X() = <me>.X() - Other.X() new.Y() = <me>.Y() - Other.Y()

        new.X() = <me>.X() - Other.X() new.Y() = <me>.Y() - Other.Y()
        """
    def X(self) -> float: 
        """
        Returns the X coordinate of this number pair.

        Returns the X coordinate of this number pair.
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate of this number pair.

        Returns the Y coordinate of this number pair.
        """
    def __add__(self,Other : gp_XY) -> gp_XY: 
        """
        None
        """
    def __iadd__(self,Other : gp_XY) -> None: 
        """
        None
        """
    @overload
    def __imul__(self,Other : gp_XY) -> None: 
        """
        None

        None

        None
        """
    @overload
    def __imul__(self,Scalar : float) -> None: ...
    @overload
    def __imul__(self,Matrix : gp_Mat2d) -> None: ...
    @overload
    def __init__(self,X : float,Y : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __isub__(self,Right : gp_XY) -> None: 
        """
        None
        """
    def __itruediv__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,Scalar : float) -> gp_XY: 
        """
        None

        None

        None
        """
    @overload
    def __mul__(self,Matrix : gp_Mat2d) -> gp_XY: ...
    @overload
    def __mul__(self,Other : gp_XY) -> float: ...
    def __pow__(self,Right : gp_XY) -> float: 
        """
        None
        """
    @overload
    def __rmul__(self,Matrix : gp_Mat2d) -> gp_XY: 
        """
        None

        None

        None
        """
    @overload
    def __rmul__(self,Scalar : float) -> gp_XY: ...
    @overload
    def __rmul__(self,Other : gp_XY) -> float: ...
    @overload
    def __sub__(self) -> gp_XY: 
        """
        None

        None
        """
    @overload
    def __sub__(self,Right : gp_XY) -> gp_XY: ...
    def __truediv__(self,Scalar : float) -> gp_XY: 
        """
        None
        """
    pass
class gp_XYZ():
    """
    This class describes a cartesian coordinate entity in 3D space {X,Y,Z}. This entity is used for algebraic calculation. This entity can be transformed with a "Trsf" or a "GTrsf" from package "gp". It is used in vectorial computations or for holding this type of information in data structures.
    """
    def Add(self,Other : gp_XYZ) -> None: 
        """
        <me>.X() = <me>.X() + Other.X() <me>.Y() = <me>.Y() + Other.Y() <me>.Z() = <me>.Z() + Other.Z()

        <me>.X() = <me>.X() + Other.X() <me>.Y() = <me>.Y() + Other.Y() <me>.Z() = <me>.Z() + Other.Z()
        """
    def Added(self,Other : gp_XYZ) -> gp_XYZ: 
        """
        new.X() = <me>.X() + Other.X() new.Y() = <me>.Y() + Other.Y() new.Z() = <me>.Z() + Other.Z()

        new.X() = <me>.X() + Other.X() new.Y() = <me>.Y() + Other.Y() new.Z() = <me>.Z() + Other.Z()
        """
    def ChangeCoord(self,theIndex : int) -> float: 
        """
        None

        None
        """
    def ChangeData(self) -> float: 
        """
        Returns a ptr to coordinates location. Is useful for algorithms, but DOES NOT PERFORM ANY CHECKS!
        """
    @overload
    def Coord(self,i : int) -> float: 
        """
        returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned

        returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned

        None

        None
        """
    @overload
    def Coord(self,Index : int) -> float: ...
    @overload
    def Coord(self) -> Tuple[float, float, float]: ...
    def Cross(self,Right : gp_XYZ) -> None: 
        """
        <me>.X() = <me>.Y() * Other.Z() - <me>.Z() * Other.Y() <me>.Y() = <me>.Z() * Other.X() - <me>.X() * Other.Z() <me>.Z() = <me>.X() * Other.Y() - <me>.Y() * Other.X()

        <me>.X() = <me>.Y() * Other.Z() - <me>.Z() * Other.Y() <me>.Y() = <me>.Z() * Other.X() - <me>.X() * Other.Z() <me>.Z() = <me>.X() * Other.Y() - <me>.Y() * Other.X()
        """
    def CrossCross(self,Coord1 : gp_XYZ,Coord2 : gp_XYZ) -> None: 
        """
        Triple vector product Computes <me> = <me>.Cross(Coord1.Cross(Coord2))

        Triple vector product Computes <me> = <me>.Cross(Coord1.Cross(Coord2))
        """
    def CrossCrossed(self,Coord1 : gp_XYZ,Coord2 : gp_XYZ) -> gp_XYZ: 
        """
        Triple vector product computes New = <me>.Cross(Coord1.Cross(Coord2))

        Triple vector product computes New = <me>.Cross(Coord1.Cross(Coord2))
        """
    def CrossMagnitude(self,Right : gp_XYZ) -> float: 
        """
        Computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||

        Computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||
        """
    def CrossSquareMagnitude(self,Right : gp_XYZ) -> float: 
        """
        Computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2

        Computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2
        """
    def Crossed(self,Right : gp_XYZ) -> gp_XYZ: 
        """
        new.X() = <me>.Y() * Other.Z() - <me>.Z() * Other.Y() new.Y() = <me>.Z() * Other.X() - <me>.X() * Other.Z() new.Z() = <me>.X() * Other.Y() - <me>.Y() * Other.X()

        new.X() = <me>.Y() * Other.Z() - <me>.Z() * Other.Y() new.Y() = <me>.Z() * Other.X() - <me>.X() * Other.Z() new.Z() = <me>.X() * Other.Y() - <me>.Y() * Other.X()
        """
    def Divide(self,Scalar : float) -> None: 
        """
        divides <me> by a real.

        divides <me> by a real.
        """
    def Divided(self,Scalar : float) -> gp_XYZ: 
        """
        divides <me> by a real.

        divides <me> by a real.
        """
    def Dot(self,Other : gp_XYZ) -> float: 
        """
        computes the scalar product between <me> and Other

        computes the scalar product between <me> and Other
        """
    def DotCross(self,Coord1 : gp_XYZ,Coord2 : gp_XYZ) -> float: 
        """
        computes the triple scalar product

        computes the triple scalar product
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetData(self) -> float: 
        """
        Returns a const ptr to coordinates location. Is useful for algorithms, but DOES NOT PERFORM ANY CHECKS!
        """
    def IsEqual(self,Other : gp_XYZ,Tolerance : float) -> bool: 
        """
        Returns True if he coordinates of this XYZ object are equal to the respective coordinates Other, within the specified tolerance Tolerance. I.e.: abs(<me>.X() - Other.X()) <= Tolerance and abs(<me>.Y() - Other.Y()) <= Tolerance and abs(<me>.Z() - Other.Z()) <= Tolerance.
        """
    def Modulus(self) -> float: 
        """
        computes Sqrt (X*X + Y*Y + Z*Z) where X, Y and Z are the three coordinates of this XYZ object.

        computes Sqrt (X*X + Y*Y + Z*Z) where X, Y and Z are the three coordinates of this XYZ object.
        """
    @overload
    def Multiplied(self,Scalar : float) -> gp_XYZ: 
        """
        New.X() = <me>.X() * Scalar; New.Y() = <me>.Y() * Scalar; New.Z() = <me>.Z() * Scalar;

        new.X() = <me>.X() * Other.X(); new.Y() = <me>.Y() * Other.Y(); new.Z() = <me>.Z() * Other.Z();

        New = Matrix * <me>

        New.X() = <me>.X() * Scalar; New.Y() = <me>.Y() * Scalar; New.Z() = <me>.Z() * Scalar;

        new.X() = <me>.X() * Other.X(); new.Y() = <me>.Y() * Other.Y(); new.Z() = <me>.Z() * Other.Z();

        New = Matrix * <me>
        """
    @overload
    def Multiplied(self,Matrix : gp_Mat) -> gp_XYZ: ...
    @overload
    def Multiplied(self,Other : gp_XYZ) -> gp_XYZ: ...
    @overload
    def Multiply(self,Scalar : float) -> None: 
        """
        <me>.X() = <me>.X() * Scalar; <me>.Y() = <me>.Y() * Scalar; <me>.Z() = <me>.Z() * Scalar;

        <me>.X() = <me>.X() * Other.X(); <me>.Y() = <me>.Y() * Other.Y(); <me>.Z() = <me>.Z() * Other.Z();

        <me> = Matrix * <me>

        <me>.X() = <me>.X() * Scalar; <me>.Y() = <me>.Y() * Scalar; <me>.Z() = <me>.Z() * Scalar;

        <me>.X() = <me>.X() * Other.X(); <me>.Y() = <me>.Y() * Other.Y(); <me>.Z() = <me>.Z() * Other.Z();

        <me> = Matrix * <me>
        """
    @overload
    def Multiply(self,Matrix : gp_Mat) -> None: ...
    @overload
    def Multiply(self,Other : gp_XYZ) -> None: ...
    def Normalize(self) -> None: 
        """
        <me>.X() = <me>.X()/ <me>.Modulus() <me>.Y() = <me>.Y()/ <me>.Modulus() <me>.Z() = <me>.Z()/ <me>.Modulus() Raised if <me>.Modulus() <= Resolution from gp

        <me>.X() = <me>.X()/ <me>.Modulus() <me>.Y() = <me>.Y()/ <me>.Modulus() <me>.Z() = <me>.Z()/ <me>.Modulus() Raised if <me>.Modulus() <= Resolution from gp
        """
    def Normalized(self) -> gp_XYZ: 
        """
        New.X() = <me>.X()/ <me>.Modulus() New.Y() = <me>.Y()/ <me>.Modulus() New.Z() = <me>.Z()/ <me>.Modulus() Raised if <me>.Modulus() <= Resolution from gp

        New.X() = <me>.X()/ <me>.Modulus() New.Y() = <me>.Y()/ <me>.Modulus() New.Z() = <me>.Z()/ <me>.Modulus() Raised if <me>.Modulus() <= Resolution from gp
        """
    def Reverse(self) -> None: 
        """
        <me>.X() = -<me>.X() <me>.Y() = -<me>.Y() <me>.Z() = -<me>.Z()

        <me>.X() = -<me>.X() <me>.Y() = -<me>.Y() <me>.Z() = -<me>.Z()
        """
    def Reversed(self) -> gp_XYZ: 
        """
        New.X() = -<me>.X() New.Y() = -<me>.Y() New.Z() = -<me>.Z()

        New.X() = -<me>.X() New.Y() = -<me>.Y() New.Z() = -<me>.Z()
        """
    @overload
    def SetCoord(self,i : int,X : float) -> None: 
        """
        For this XYZ object, assigns the values X, Y and Z to its three coordinates

        modifies the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Index = 3 => Z is modified Raises OutOfRange if Index != {1, 2, 3}.

        For this XYZ object, assigns the values X, Y and Z to its three coordinates

        modifies the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Index = 3 => Z is modified Raises OutOfRange if Index != {1, 2, 3}.
        """
    @overload
    def SetCoord(self,Index : int,Xi : float) -> None: ...
    @overload
    def SetCoord(self,X : float,Y : float,Z : float) -> None: ...
    @overload
    def SetLinearForm(self,XYZ1 : gp_XYZ,XYZ2 : gp_XYZ) -> None: 
        """
        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + A3 * XYZ3 + XYZ4

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + A3 * XYZ3

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + XYZ3

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2

        <me> is set to the following linear form : A1 * XYZ1 + XYZ2

        <me> is set to the following linear form : XYZ1 + XYZ2

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2

        <me> is set to the following linear form : A1 * XYZ1 + XYZ2

        <me> is set to the following linear form : XYZ1 + XYZ2

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + A3 * XYZ3

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + XYZ3

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + A3 * XYZ3 + XYZ4
        """
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : gp_XYZ,A2 : float,XYZ2 : gp_XYZ,A3 : float,XYZ3 : gp_XYZ,XYZ4 : gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : gp_XYZ,Right : gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : gp_XYZ,R : float,Right : gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : gp_XYZ,A2 : float,XYZ2 : gp_XYZ,XYZ3 : gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : gp_XYZ,A2 : float,XYZ2 : gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : gp_XYZ,XYZ2 : gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,Left : gp_XYZ,Right : gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : gp_XYZ,A2 : float,XYZ2 : gp_XYZ,A3 : float,XYZ3 : gp_XYZ) -> None: ...
    def SetX(self,X : float) -> None: 
        """
        Assigns the given value to the X coordinate

        Assigns the given value to the X coordinate
        """
    def SetY(self,Y : float) -> None: 
        """
        Assigns the given value to the Y coordinate

        Assigns the given value to the Y coordinate
        """
    def SetZ(self,Z : float) -> None: 
        """
        Assigns the given value to the Z coordinate

        Assigns the given value to the Z coordinate
        """
    def SquareModulus(self) -> float: 
        """
        Computes X*X + Y*Y + Z*Z where X, Y and Z are the three coordinates of this XYZ object.

        Computes X*X + Y*Y + Z*Z where X, Y and Z are the three coordinates of this XYZ object.
        """
    def Subtract(self,Right : gp_XYZ) -> None: 
        """
        <me>.X() = <me>.X() - Other.X() <me>.Y() = <me>.Y() - Other.Y() <me>.Z() = <me>.Z() - Other.Z()

        <me>.X() = <me>.X() - Other.X() <me>.Y() = <me>.Y() - Other.Y() <me>.Z() = <me>.Z() - Other.Z()
        """
    def Subtracted(self,Right : gp_XYZ) -> gp_XYZ: 
        """
        new.X() = <me>.X() - Other.X() new.Y() = <me>.Y() - Other.Y() new.Z() = <me>.Z() - Other.Z()

        new.X() = <me>.X() - Other.X() new.Y() = <me>.Y() - Other.Y() new.Z() = <me>.Z() - Other.Z()
        """
    def X(self) -> float: 
        """
        Returns the X coordinate

        Returns the X coordinate
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate

        Returns the Y coordinate
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate

        Returns the Z coordinate
        """
    def __add__(self,Other : gp_XYZ) -> gp_XYZ: 
        """
        None
        """
    def __iadd__(self,Other : gp_XYZ) -> None: 
        """
        None
        """
    @overload
    def __imul__(self,Other : gp_XYZ) -> None: 
        """
        None

        None

        None
        """
    @overload
    def __imul__(self,Matrix : gp_Mat) -> None: ...
    @overload
    def __imul__(self,Scalar : float) -> None: ...
    @overload
    def __init__(self,X : float,Y : float,Z : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __ipow__(self,Right : gp_XYZ) -> None: 
        """
        None
        """
    def __isub__(self,Right : gp_XYZ) -> None: 
        """
        None
        """
    def __itruediv__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,Scalar : float) -> gp_XYZ: 
        """
        None

        None

        None
        """
    @overload
    def __mul__(self,Other : gp_XYZ) -> float: ...
    @overload
    def __mul__(self,Matrix : gp_Mat) -> gp_XYZ: ...
    def __pow__(self,Right : gp_XYZ) -> gp_XYZ: 
        """
        None
        """
    @overload
    def __rmul__(self,Matrix : gp_Mat) -> gp_XYZ: 
        """
        None

        None

        None
        """
    @overload
    def __rmul__(self,Other : gp_XYZ) -> float: ...
    @overload
    def __rmul__(self,Scalar : float) -> gp_XYZ: ...
    def __sub__(self,Right : gp_XYZ) -> gp_XYZ: 
        """
        None
        """
    def __truediv__(self,Scalar : float) -> gp_XYZ: 
        """
        None
        """
    pass
@overload
def __mul__(Scalar : float,Coord1 : gp_XY) -> gp_XY:
    """
    None

    None

    None

    None

    None

    None

    None

    None
    """
@overload
def __mul__(Scalar : float,Coord1 : gp_XYZ) -> gp_XYZ:
    pass
@overload
def __mul__(Scalar : float,V : gp_Vec) -> gp_Vec:
    pass
@overload
def __mul__(Scalar : float,Mat3D : gp_Mat) -> gp_Mat:
    pass
@overload
def __mul__(Scalar : float,Mat2D : gp_Mat2d) -> gp_Mat2d:
    pass
@overload
def __mul__(Matrix : gp_Mat,Coord1 : gp_XYZ) -> gp_XYZ:
    pass
@overload
def __mul__(Matrix : gp_Mat2d,Coord1 : gp_XY) -> gp_XY:
    pass
@overload
def __mul__(Scalar : float,V : gp_Vec2d) -> gp_Vec2d:
    pass
@overload
def __rmul__(Scalar : float,Mat3D : gp_Mat) -> gp_Mat:
    """
    None

    None

    None

    None

    None

    None

    None

    None
    """
@overload
def __rmul__(Matrix : gp_Mat,Coord1 : gp_XYZ) -> gp_XYZ:
    pass
@overload
def __rmul__(Scalar : float,V : gp_Vec2d) -> gp_Vec2d:
    pass
@overload
def __rmul__(Scalar : float,Coord1 : gp_XYZ) -> gp_XYZ:
    pass
@overload
def __rmul__(Scalar : float,Coord1 : gp_XY) -> gp_XY:
    pass
@overload
def __rmul__(Scalar : float,Mat2D : gp_Mat2d) -> gp_Mat2d:
    pass
@overload
def __rmul__(Matrix : gp_Mat2d,Coord1 : gp_XY) -> gp_XY:
    pass
@overload
def __rmul__(Scalar : float,V : gp_Vec) -> gp_Vec:
    pass
gp_Ax1Mirror: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Ax1Mirror
gp_Ax2Mirror: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Ax2Mirror
gp_CompoundTrsf: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_CompoundTrsf
gp_EulerAngles: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_EulerAngles
gp_Extrinsic_XYX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_XYX
gp_Extrinsic_XYZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_XYZ
gp_Extrinsic_XZX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_XZX
gp_Extrinsic_XZY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_XZY
gp_Extrinsic_YXY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_YXY
gp_Extrinsic_YXZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_YXZ
gp_Extrinsic_YZX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_YZX
gp_Extrinsic_YZY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_YZY
gp_Extrinsic_ZXY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_ZXY
gp_Extrinsic_ZXZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_ZXZ
gp_Extrinsic_ZYX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_ZYX
gp_Extrinsic_ZYZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Extrinsic_ZYZ
gp_Identity: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Identity
gp_Intrinsic_XYX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_XYX
gp_Intrinsic_XYZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_XYZ
gp_Intrinsic_XZX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_XZX
gp_Intrinsic_XZY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_XZY
gp_Intrinsic_YXY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_YXY
gp_Intrinsic_YXZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_YXZ
gp_Intrinsic_YZX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_YZX
gp_Intrinsic_YZY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_YZY
gp_Intrinsic_ZXY: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_ZXY
gp_Intrinsic_ZXZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_ZXZ
gp_Intrinsic_ZYX: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_ZYX
gp_Intrinsic_ZYZ: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_Intrinsic_ZYZ
gp_Other: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Other
gp_PntMirror: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_PntMirror
gp_Rotation: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Rotation
gp_Scale: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Scale
gp_Translation: OCP.gp.gp_TrsfForm # value = gp_TrsfForm.gp_Translation
gp_YawPitchRoll: OCP.gp.gp_EulerSequence # value = gp_EulerSequence.gp_YawPitchRoll
