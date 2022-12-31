import OCP.ShapeExtend
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.TColGeom
import OCP.TopoDS
import OCP.NCollection
import OCP.Message
import OCP.gp
import OCP.TopAbs
import OCP.GeomAbs
import OCP.TopTools
import OCP.Standard
import OCP.TColStd
import io
__all__  = [
"ShapeExtend",
"ShapeExtend_BasicMsgRegistrator",
"ShapeExtend_ComplexCurve",
"ShapeExtend_CompositeSurface",
"ShapeExtend_DataMapOfShapeListOfMsg",
"ShapeExtend_DataMapOfTransientListOfMsg",
"ShapeExtend_Explorer",
"ShapeExtend_MsgRegistrator",
"ShapeExtend_Parametrisation",
"ShapeExtend_Status",
"ShapeExtend_WireData",
"ShapeExtend_DONE",
"ShapeExtend_DONE1",
"ShapeExtend_DONE2",
"ShapeExtend_DONE3",
"ShapeExtend_DONE4",
"ShapeExtend_DONE5",
"ShapeExtend_DONE6",
"ShapeExtend_DONE7",
"ShapeExtend_DONE8",
"ShapeExtend_FAIL",
"ShapeExtend_FAIL1",
"ShapeExtend_FAIL2",
"ShapeExtend_FAIL3",
"ShapeExtend_FAIL4",
"ShapeExtend_FAIL5",
"ShapeExtend_FAIL6",
"ShapeExtend_FAIL7",
"ShapeExtend_FAIL8",
"ShapeExtend_Natural",
"ShapeExtend_OK",
"ShapeExtend_Uniform",
"ShapeExtend_Unitary"
]
class ShapeExtend():
    """
    This package provides general tools and data structures common for other packages in SHAPEWORKS and extending CAS.CADE structures. The following items are provided by this package: - enumeration Status used for coding status flags in methods inside the SHAPEWORKS - enumeration Parametrisation used for setting global parametrisation on the composite surface - class CompositeSurface representing a composite surface made of a grid of surface patches - class WireData representing a wire in the form of ordered list of edges - class MsgRegistrator for attaching messages to the objects - tools for exploring the shapes - tools for creating new shapes.
    """
    @staticmethod
    def DecodeStatus_s(flag : int,status : ShapeExtend_Status) -> bool: 
        """
        Tells if a bit flag contains bit corresponding to enumerated status
        """
    @staticmethod
    def EncodeStatus_s(status : ShapeExtend_Status) -> int: 
        """
        Encodes status (enumeration) to a bit flag
        """
    @staticmethod
    def Init_s() -> None: 
        """
        Inits using of ShapeExtend. Currently, loads messages output by ShapeHealing algorithms.
        """
    def __init__(self) -> None: ...
    pass
class ShapeExtend_BasicMsgRegistrator(OCP.Standard.Standard_Transient):
    """
    Abstract class that can be used for attaching messages to the objects (e.g. shapes). It is used by ShapeHealing algorithms to attach a message describing encountered case (e.g. removing small edge from a wire).Abstract class that can be used for attaching messages to the objects (e.g. shapes). It is used by ShapeHealing algorithms to attach a message describing encountered case (e.g. removing small edge from a wire).Abstract class that can be used for attaching messages to the objects (e.g. shapes). It is used by ShapeHealing algorithms to attach a message describing encountered case (e.g. removing small edge from a wire).
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
    @overload
    def Send(self,object : OCP.Standard.Standard_Transient,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: 
        """
        Sends a message to be attached to the object. Object can be of any type interpreted by redefined MsgRegistrator.

        Sends a message to be attached to the shape.

        Calls Send method with Null Transient.
        """
    @overload
    def Send(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def Send(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
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
class ShapeExtend_ComplexCurve(OCP.Geom.Geom_Curve, OCP.Geom.Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Defines a curve which consists of several segments. Implements basic interface to it.Defines a curve which consists of several segments. Implements basic interface to it.Defines a curve which consists of several segments. Implements basic interface to it.
    """
    def CheckConnectivity(self,Preci : float) -> bool: 
        """
        Checks geometrical connectivity of the curves, including closure (sets fields myClosed)
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns GeomAbs_C0

        Returns GeomAbs_C0
        """
    def Copy(self) -> OCP.Geom.Geom_Geometry: 
        """
        Creates a new object which is a copy of this geometric object.
        """
    def Curve(self,index : int) -> OCP.Geom.Geom_Curve: 
        """
        Returns curve given by its index
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns point at parameter U. Finds appropriate curve and local parameter on it.
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
        None
        """
    def DN(self,U : float,N : int) -> OCP.gp.gp_Vec: 
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
    def FirstParameter(self) -> float: 
        """
        Returns 0

        Returns 0
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetScaleFactor(self,ind : int) -> float: 
        """
        Returns scale factor for recomputing of deviatives.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCN(self,N : int) -> bool: 
        """
        Returns False if N > 0

        Returns False if N > 0
        """
    def IsClosed(self) -> bool: 
        """
        Returns True if the curve is closed

        Returns True if the curve is closed
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

        Returns False
        """
    def LastParameter(self) -> float: 
        """
        Returns 1

        Returns 1
        """
    def LocalToGlobal(self,index : int,Ulocal : float) -> float: 
        """
        Returns global parameter for the whole curve according to the segment and local parameter on it
        """
    def LocateParameter(self,U : float,UOut : float) -> int: 
        """
        Returns number of the curve for the given parameter U and local paramete r UOut for the found curve
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
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> OCP.Geom.Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> OCP.Geom.Geom_Geometry: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> OCP.Geom.Geom_Geometry: ...
    def NbCurves(self) -> int: 
        """
        Returns number of curves
        """
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
    def Reversed(self) -> OCP.Geom.Geom_Curve: 
        """
        Returns a copy of <me> reversed.
        """
    def ReversedParameter(self,U : float) -> float: 
        """
        Returns 1 - U

        Returns 1 - U
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies transformation to each curve
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    def TransformedParameter(self,U : float,T : OCP.gp.gp_Trsf) -> float: 
        """
        Returns the parameter on the transformed curve for the transform of the point of parameter U on <me>.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: 
        """
        Translates a Geometry. V is the vector of the translation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> OCP.Geom.Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> OCP.Geom.Geom_Geometry: ...
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
class ShapeExtend_CompositeSurface(OCP.Geom.Geom_Surface, OCP.Geom.Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Composite surface is represented by a grid of surfaces (patches) connected geometrically. Patches may have different parametrisation ranges, but they should be parametrised in the same manner so that parameter of each patch (u,v) can be converted to global parameter on the whole surface (U,V) with help of linear transformation:Composite surface is represented by a grid of surfaces (patches) connected geometrically. Patches may have different parametrisation ranges, but they should be parametrised in the same manner so that parameter of each patch (u,v) can be converted to global parameter on the whole surface (U,V) with help of linear transformation:Composite surface is represented by a grid of surfaces (patches) connected geometrically. Patches may have different parametrisation ranges, but they should be parametrised in the same manner so that parameter of each patch (u,v) can be converted to global parameter on the whole surface (U,V) with help of linear transformation:
    """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds of grid
        """
    def CheckConnectivity(self,prec : float) -> bool: 
        """
        Checks geometrical connectivity of the patches, including closedness (sets fields muUClosed and myVClosed)
        """
    def ComputeJointValues(self,param : ShapeExtend_Parametrisation=ShapeExtend_Parametrisation.ShapeExtend_Natural) -> None: 
        """
        Computes Joint values according to parameter
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        returns C0
        """
    def Copy(self) -> OCP.Geom.Geom_Geometry: 
        """
        Returns a copy of the surface
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U,V on the grid.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P and the first derivatives in the directions U and V at this point.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first and the second derivatives in the directions U and V at this point.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first,the second and the third derivatives in the directions U and V at this point.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V).
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
    def GlobalToLocal(self,i : int,j : int,UV : OCP.gp.gp_Pnt2d) -> OCP.gp.gp_Pnt2d: 
        """
        Converts global parameters UV to local parameters uv on patch i,j
        """
    def GlobalToLocalTransformation(self,i : int,j : int,uFact : float,Trsf : OCP.gp.gp_Trsf2d) -> bool: 
        """
        Computes transformation operator and uFactor descrinbing affine transformation required to convert global parameters on composite surface to local parameters on patch (i,j): uv = ( uFactor, 1. ) X Trsf * UV; NOTE: Thus Trsf contains shift and scale by V, scale by U is stored in uFact. Returns True if transformation is not an identity
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,GridSurf : OCP.TColGeom.TColGeom_HArray2OfSurface,UJoints : OCP.TColStd.TColStd_Array1OfReal,VJoints : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Initializes by a grid of surfaces. All the Surfaces of the grid must have geometrical connectivity as stated above. If geometrical connectivity is not satisfied, method returns False. However, class is initialized even in that case.

        Initializes by a grid of surfaces with given global parametrisation defined by UJoints and VJoints arrays, each having langth equal to number of patches in corresponding direction + 1. Global joint values should be sorted in increasing order. All the Surfaces of the grid must have geometrical connectivity as stated above. If geometrical connectivity is not satisfied, method returns False. However, class is initialized even in that case.
        """
    @overload
    def Init(self,GridSurf : OCP.TColGeom.TColGeom_HArray2OfSurface,param : ShapeExtend_Parametrisation=ShapeExtend_Parametrisation.ShapeExtend_Natural) -> bool: ...
    def IsCNu(self,N : int) -> bool: 
        """
        returns True if N <=0
        """
    def IsCNv(self,N : int) -> bool: 
        """
        returns True if N <=0
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
        Returns True if grid is closed in U direction (i.e. connected with Precision::Confusion)
        """
    def IsUPeriodic(self) -> bool: 
        """
        Returns False
        """
    def IsVClosed(self) -> bool: 
        """
        Returns True if grid is closed in V direction (i.e. connected with Precision::Confusion)
        """
    def IsVPeriodic(self) -> bool: 
        """
        Returns False
        """
    def LocalToGlobal(self,i : int,j : int,uv : OCP.gp.gp_Pnt2d) -> OCP.gp.gp_Pnt2d: 
        """
        Converts local parameters uv on patch i,j to global parameters UV
        """
    def LocateUParameter(self,U : float) -> int: 
        """
        Returns number of col that contains given (global) parameter
        """
    def LocateUVPoint(self,pnt : OCP.gp.gp_Pnt2d) -> Tuple[int, int]: 
        """
        Returns number of row and col of surface that contains given point
        """
    def LocateVParameter(self,V : float) -> int: 
        """
        Returns number of row that contains given (global) parameter
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
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> OCP.Geom.Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> OCP.Geom.Geom_Geometry: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> OCP.Geom.Geom_Geometry: ...
    def NbUPatches(self) -> int: 
        """
        Returns number of patches in U direction.
        """
    def NbVPatches(self) -> int: 
        """
        Returns number of patches in V direction.
        """
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface. is the same point as Where U',V' are obtained by transforming U,V with the 2d transformation returned by This method returns an identity transformation
        """
    @overload
    def Patch(self,pnt : OCP.gp.gp_Pnt2d) -> OCP.Geom.Geom_Surface: 
        """
        Returns one surface patch

        Returns one surface patch that contains given (global) parameters

        Returns one surface patch that contains given point
        """
    @overload
    def Patch(self,U : float,V : float) -> OCP.Geom.Geom_Surface: ...
    @overload
    def Patch(self,i : int,j : int) -> OCP.Geom.Geom_Surface: ...
    def Patches(self) -> OCP.TColGeom.TColGeom_HArray2OfSurface: 
        """
        Returns grid of surfaces
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    def SetUFirstValue(self,UFirst : float) -> None: 
        """
        Changes starting value for global U parametrisation (all other joint values are shifted accordingly)
        """
    def SetUJointValues(self,UJoints : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Sets the array of U values corresponding to joint points, which define global parametrisation of the surface. Number of values in array should be equal to NbUPatches()+1. All the values should be sorted in increasing order. If this is not satisfied, does nothing and returns False.
        """
    def SetVFirstValue(self,VFirst : float) -> None: 
        """
        Changes starting value for global V parametrisation (all other joint values are shifted accordingly)
        """
    def SetVJointValues(self,VJoints : OCP.TColStd.TColStd_Array1OfReal) -> bool: 
        """
        Sets the array of V values corresponding to joint points, which define global parametrisation of the surface Number of values in array should be equal to NbVPatches()+1. All the values should be sorted in increasing order. If this is not satisfied, does nothing and returns False.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Applies transformation to all the patches
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>. is the same point as Where U',V' are the new values of U,V after calling This method does not change <U> and <V>
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: 
        """
        Translates a Geometry. V is the vector of the translation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> OCP.Geom.Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> OCP.Geom.Geom_Geometry: ...
    def UGlobalToLocal(self,i : int,j : int,U : float) -> float: 
        """
        Converts global parameter U to local parameter u on patch i,j
        """
    def UIso(self,U : float) -> OCP.Geom.Geom_Curve: 
        """
        NOT IMPLEMENTED (returns Null curve)
        """
    def UJointValue(self,i : int) -> float: 
        """
        Returns i-th joint value in U direction (1-st is global Umin, (NbUPatches()+1)-th is global Umax on the composite surface)
        """
    def UJointValues(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the array of U values corresponding to joint points between patches as well as to start and end points, which define global parametrisation of the surface
        """
    def ULocalToGlobal(self,i : int,j : int,u : float) -> float: 
        """
        Converts local parameter u on patch i,j to global parameter U
        """
    def UPeriod(self) -> float: 
        """
        Returns the period of this surface in the u parametric direction. Raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        NOT IMPLEMENTED (does nothing)
        """
    def UReversed(self) -> OCP.Geom.Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Returns U
        """
    def VGlobalToLocal(self,i : int,j : int,V : float) -> float: 
        """
        Converts global parameter V to local parameter v on patch i,j
        """
    def VIso(self,V : float) -> OCP.Geom.Geom_Curve: 
        """
        NOT IMPLEMENTED (returns Null curve)
        """
    def VJointValue(self,j : int) -> float: 
        """
        Returns j-th joint value in V direction (1-st is global Vmin, (NbVPatches()+1)-th is global Vmax on the composite surface)
        """
    def VJointValues(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the array of V values corresponding to joint points between patches as well as to start and end points, which define global parametrisation of the surface
        """
    def VLocalToGlobal(self,i : int,j : int,v : float) -> float: 
        """
        Converts local parameter v on patch i,j to global parameter V
        """
    def VPeriod(self) -> float: 
        """
        Returns the period of this surface in the v parametric direction. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        NOT IMPLEMENTED (does nothing)
        """
    def VReversed(self) -> OCP.Geom.Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Returns V
        """
    def Value(self,pnt : OCP.gp.gp_Pnt2d) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter pnt on the grid.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,GridSurf : OCP.TColGeom.TColGeom_HArray2OfSurface,param : ShapeExtend_Parametrisation=ShapeExtend_Parametrisation.ShapeExtend_Natural) -> None: ...
    @overload
    def __init__(self,GridSurf : OCP.TColGeom.TColGeom_HArray2OfSurface,UJoints : OCP.TColStd.TColStd_Array1OfReal,VJoints : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
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
class ShapeExtend_DataMapOfShapeListOfMsg(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : ShapeExtend_DataMapOfShapeListOfMsg) -> ShapeExtend_DataMapOfShapeListOfMsg: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Message.Message_ListOfMsg) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Message.Message_ListOfMsg) -> OCP.Message.Message_ListOfMsg: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Message.Message_ListOfMsg: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Message.Message_ListOfMsg: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : ShapeExtend_DataMapOfShapeListOfMsg) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.Message.Message_ListOfMsg) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Message.Message_ListOfMsg: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Message.Message_ListOfMsg: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : ShapeExtend_DataMapOfShapeListOfMsg) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class ShapeExtend_DataMapOfTransientListOfMsg(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : ShapeExtend_DataMapOfTransientListOfMsg) -> ShapeExtend_DataMapOfTransientListOfMsg: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.Standard.Standard_Transient,theItem : OCP.Message.Message_ListOfMsg) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.Standard.Standard_Transient,theItem : OCP.Message.Message_ListOfMsg) -> OCP.Message.Message_ListOfMsg: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.Standard.Standard_Transient) -> OCP.Message.Message_ListOfMsg: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.Standard.Standard_Transient) -> OCP.Message.Message_ListOfMsg: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : ShapeExtend_DataMapOfTransientListOfMsg) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.Standard.Standard_Transient,theValue : OCP.Message.Message_ListOfMsg) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.Standard.Standard_Transient) -> OCP.Message.Message_ListOfMsg: ...
    def IsBound(self,theKey : OCP.Standard.Standard_Transient) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.Standard.Standard_Transient) -> OCP.Message.Message_ListOfMsg: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.Standard.Standard_Transient) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : ShapeExtend_DataMapOfTransientListOfMsg) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class ShapeExtend_Explorer():
    """
    This class is intended to explore shapes and convert different representations (list, sequence, compound) of complex shapes. It provides tools for: - obtaining type of the shapes in context of TopoDS_Compound, - exploring shapes in context of TopoDS_Compound, - converting different representations of shapes (list, sequence, compound).
    """
    def CompoundFromSeq(self,seqval : OCP.TopTools.TopTools_HSequenceOfShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Converts a sequence of Shapes to a Compound
        """
    def DispatchList(self,list : OCP.TopTools.TopTools_HSequenceOfShape,vertices : OCP.TopTools.TopTools_HSequenceOfShape,edges : OCP.TopTools.TopTools_HSequenceOfShape,wires : OCP.TopTools.TopTools_HSequenceOfShape,faces : OCP.TopTools.TopTools_HSequenceOfShape,shells : OCP.TopTools.TopTools_HSequenceOfShape,solids : OCP.TopTools.TopTools_HSequenceOfShape,compsols : OCP.TopTools.TopTools_HSequenceOfShape,compounds : OCP.TopTools.TopTools_HSequenceOfShape) -> Any: 
        """
        Dispatches starting list of shapes according to their type, to the appropriate resulting lists For each of these lists, if it is null, it is firstly created else, new items are appended to the already existing ones
        """
    def ListFromSeq(self,seqval : OCP.TopTools.TopTools_HSequenceOfShape,lisval : OCP.TopTools.TopTools_ListOfShape,clear : bool=True) -> None: 
        """
        Converts a Sequence of Shapes to a List of Shapes <clear> if True (D), commands the list to start from scratch else, the list is cumulated
        """
    def SeqFromCompound(self,comp : OCP.TopoDS.TopoDS_Shape,expcomp : bool) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        Converts a Compound to a list of Shapes if <comp> is not a compound, the list contains only <comp> if <comp> is Null, the list is empty if <comp> is a Compound, its sub-shapes are put into the list then if <expcomp> is True, if a sub-shape is a Compound, it is not put to the list but its sub-shapes are (recursive)
        """
    def SeqFromList(self,lisval : OCP.TopTools.TopTools_ListOfShape) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        Converts a List of Shapes to a Sequence of Shapes
        """
    def ShapeType(self,shape : OCP.TopoDS.TopoDS_Shape,compound : bool) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the type of a Shape: true type if <compound> is False If <compound> is True and <shape> is a Compound, iterates on its items. If all are of the same type, returns this type. Else, returns COMPOUND. If it is empty, returns SHAPE For a Null Shape, returns SHAPE
        """
    def SortedCompound(self,shape : OCP.TopoDS.TopoDS_Shape,type : OCP.TopAbs.TopAbs_ShapeEnum,explore : bool,compound : bool) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Builds a COMPOUND from the given shape. It explores the shape level by level, according to the <explore> argument. If <explore> is False, only COMPOUND items are explored, else all items are. The following shapes are added to resulting compound: - shapes which comply to <type> - if <type> is WIRE, considers also free edges (and makes wires) - if <type> is SHELL, considers also free faces (and makes shells) If <compound> is True, gathers items in compounds which correspond to starting COMPOUND,SOLID or SHELL containers, or items directly contained in a Compound
        """
    def __init__(self) -> None: ...
    pass
class ShapeExtend_MsgRegistrator(ShapeExtend_BasicMsgRegistrator, OCP.Standard.Standard_Transient):
    """
    Attaches messages to the objects (generic Transient or shape). The objects of this class are transmitted to the Shape Healing algorithms so that they could collect messages occurred during processing.Attaches messages to the objects (generic Transient or shape). The objects of this class are transmitted to the Shape Healing algorithms so that they could collect messages occurred during processing.Attaches messages to the objects (generic Transient or shape). The objects of this class are transmitted to the Shape Healing algorithms so that they could collect messages occurred during processing.
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
    def MapShape(self) -> ShapeExtend_DataMapOfShapeListOfMsg: 
        """
        Returns a Map of shapes and message list

        Returns a Map of shapes and message list
        """
    def MapTransient(self) -> ShapeExtend_DataMapOfTransientListOfMsg: 
        """
        Returns a Map of objects and message list

        Returns a Map of objects and message list
        """
    @overload
    def Send(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: 
        """
        Sends a message to be attached to the object. If the object is in the map then the message is added to the list, otherwise the object is firstly added to the map.

        Sends a message to be attached to the shape. If the shape is in the map then the message is added to the list, otherwise the shape is firstly added to the map.
        """
    @overload
    def Send(self,object : OCP.Standard.Standard_Transient,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
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
class ShapeExtend_Parametrisation():
    """
    Defines kind of global parametrisation on the composite surface each patch of the 1st row and column adds its range, Ui+1 = Ui + URange(i,1), etc. each patch gives range 1.: Ui = i-1, Vj = j-1 uniform parametrisation with global range [0,1]

    Members:

      ShapeExtend_Natural

      ShapeExtend_Uniform

      ShapeExtend_Unitary
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
    ShapeExtend_Natural: OCP.ShapeExtend.ShapeExtend_Parametrisation # value = <ShapeExtend_Parametrisation.ShapeExtend_Natural: 0>
    ShapeExtend_Uniform: OCP.ShapeExtend.ShapeExtend_Parametrisation # value = <ShapeExtend_Parametrisation.ShapeExtend_Uniform: 1>
    ShapeExtend_Unitary: OCP.ShapeExtend.ShapeExtend_Parametrisation # value = <ShapeExtend_Parametrisation.ShapeExtend_Unitary: 2>
    __entries: dict # value = {'ShapeExtend_Natural': (<ShapeExtend_Parametrisation.ShapeExtend_Natural: 0>, None), 'ShapeExtend_Uniform': (<ShapeExtend_Parametrisation.ShapeExtend_Uniform: 1>, None), 'ShapeExtend_Unitary': (<ShapeExtend_Parametrisation.ShapeExtend_Unitary: 2>, None)}
    __members__: dict # value = {'ShapeExtend_Natural': <ShapeExtend_Parametrisation.ShapeExtend_Natural: 0>, 'ShapeExtend_Uniform': <ShapeExtend_Parametrisation.ShapeExtend_Uniform: 1>, 'ShapeExtend_Unitary': <ShapeExtend_Parametrisation.ShapeExtend_Unitary: 2>}
    pass
class ShapeExtend_Status():
    """
    This enumeration is used in ShapeHealing toolkit for representing flags in the return statuses of class methods. The status is a field of the class which is set by one or several methods of that class. It is used for reporting about errors and other situations encountered during execution of the method. There are defined 8 values for DONE and 8 for FAIL flags: ShapeExtend_DONE1 ... ShapeExtend_DONE8, ShapeExtend_FAIL1 ... ShapeExtend_FAIL8 and also enumerations for representing combinations of flags: ShapeExtend_OK - no flags at all, ShapeExtend_DONE - any of flags DONEi, ShapeExtend_FAIL - any of flags FAILi. The class that uses statuses provides a method(s) which answers whether the flag corresponding to a given enumerative value is (are) set: Standard_Boolean Status(const ShapeExtend_Status test); Note that status can have several flags set simultaneously. Status(ShapeExtend_OK) gives True when no flags are set. Nothing done, everything OK Something was done, case 1 Something was done, case 2 Something was done, case 3 Something was done, case 4 Something was done, case 5 Something was done, case 6 Something was done, case 7 Something was done, case 8 Something was done (any of DONE#) The method failed, case 1 The method failed, case 2 The method failed, case 3 The method failed, case 4 The method failed, case 5 The method failed, case 6 The method failed, case 7 The method failed, case 8 The method failed (any of FAIL# occurred)

    Members:

      ShapeExtend_OK

      ShapeExtend_DONE1

      ShapeExtend_DONE2

      ShapeExtend_DONE3

      ShapeExtend_DONE4

      ShapeExtend_DONE5

      ShapeExtend_DONE6

      ShapeExtend_DONE7

      ShapeExtend_DONE8

      ShapeExtend_DONE

      ShapeExtend_FAIL1

      ShapeExtend_FAIL2

      ShapeExtend_FAIL3

      ShapeExtend_FAIL4

      ShapeExtend_FAIL5

      ShapeExtend_FAIL6

      ShapeExtend_FAIL7

      ShapeExtend_FAIL8

      ShapeExtend_FAIL
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
    ShapeExtend_DONE: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE: 9>
    ShapeExtend_DONE1: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE1: 1>
    ShapeExtend_DONE2: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE2: 2>
    ShapeExtend_DONE3: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE3: 3>
    ShapeExtend_DONE4: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE4: 4>
    ShapeExtend_DONE5: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE5: 5>
    ShapeExtend_DONE6: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE6: 6>
    ShapeExtend_DONE7: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE7: 7>
    ShapeExtend_DONE8: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE8: 8>
    ShapeExtend_FAIL: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL: 18>
    ShapeExtend_FAIL1: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL1: 10>
    ShapeExtend_FAIL2: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL2: 11>
    ShapeExtend_FAIL3: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL3: 12>
    ShapeExtend_FAIL4: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL4: 13>
    ShapeExtend_FAIL5: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL5: 14>
    ShapeExtend_FAIL6: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL6: 15>
    ShapeExtend_FAIL7: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL7: 16>
    ShapeExtend_FAIL8: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL8: 17>
    ShapeExtend_OK: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_OK: 0>
    __entries: dict # value = {'ShapeExtend_OK': (<ShapeExtend_Status.ShapeExtend_OK: 0>, None), 'ShapeExtend_DONE1': (<ShapeExtend_Status.ShapeExtend_DONE1: 1>, None), 'ShapeExtend_DONE2': (<ShapeExtend_Status.ShapeExtend_DONE2: 2>, None), 'ShapeExtend_DONE3': (<ShapeExtend_Status.ShapeExtend_DONE3: 3>, None), 'ShapeExtend_DONE4': (<ShapeExtend_Status.ShapeExtend_DONE4: 4>, None), 'ShapeExtend_DONE5': (<ShapeExtend_Status.ShapeExtend_DONE5: 5>, None), 'ShapeExtend_DONE6': (<ShapeExtend_Status.ShapeExtend_DONE6: 6>, None), 'ShapeExtend_DONE7': (<ShapeExtend_Status.ShapeExtend_DONE7: 7>, None), 'ShapeExtend_DONE8': (<ShapeExtend_Status.ShapeExtend_DONE8: 8>, None), 'ShapeExtend_DONE': (<ShapeExtend_Status.ShapeExtend_DONE: 9>, None), 'ShapeExtend_FAIL1': (<ShapeExtend_Status.ShapeExtend_FAIL1: 10>, None), 'ShapeExtend_FAIL2': (<ShapeExtend_Status.ShapeExtend_FAIL2: 11>, None), 'ShapeExtend_FAIL3': (<ShapeExtend_Status.ShapeExtend_FAIL3: 12>, None), 'ShapeExtend_FAIL4': (<ShapeExtend_Status.ShapeExtend_FAIL4: 13>, None), 'ShapeExtend_FAIL5': (<ShapeExtend_Status.ShapeExtend_FAIL5: 14>, None), 'ShapeExtend_FAIL6': (<ShapeExtend_Status.ShapeExtend_FAIL6: 15>, None), 'ShapeExtend_FAIL7': (<ShapeExtend_Status.ShapeExtend_FAIL7: 16>, None), 'ShapeExtend_FAIL8': (<ShapeExtend_Status.ShapeExtend_FAIL8: 17>, None), 'ShapeExtend_FAIL': (<ShapeExtend_Status.ShapeExtend_FAIL: 18>, None)}
    __members__: dict # value = {'ShapeExtend_OK': <ShapeExtend_Status.ShapeExtend_OK: 0>, 'ShapeExtend_DONE1': <ShapeExtend_Status.ShapeExtend_DONE1: 1>, 'ShapeExtend_DONE2': <ShapeExtend_Status.ShapeExtend_DONE2: 2>, 'ShapeExtend_DONE3': <ShapeExtend_Status.ShapeExtend_DONE3: 3>, 'ShapeExtend_DONE4': <ShapeExtend_Status.ShapeExtend_DONE4: 4>, 'ShapeExtend_DONE5': <ShapeExtend_Status.ShapeExtend_DONE5: 5>, 'ShapeExtend_DONE6': <ShapeExtend_Status.ShapeExtend_DONE6: 6>, 'ShapeExtend_DONE7': <ShapeExtend_Status.ShapeExtend_DONE7: 7>, 'ShapeExtend_DONE8': <ShapeExtend_Status.ShapeExtend_DONE8: 8>, 'ShapeExtend_DONE': <ShapeExtend_Status.ShapeExtend_DONE: 9>, 'ShapeExtend_FAIL1': <ShapeExtend_Status.ShapeExtend_FAIL1: 10>, 'ShapeExtend_FAIL2': <ShapeExtend_Status.ShapeExtend_FAIL2: 11>, 'ShapeExtend_FAIL3': <ShapeExtend_Status.ShapeExtend_FAIL3: 12>, 'ShapeExtend_FAIL4': <ShapeExtend_Status.ShapeExtend_FAIL4: 13>, 'ShapeExtend_FAIL5': <ShapeExtend_Status.ShapeExtend_FAIL5: 14>, 'ShapeExtend_FAIL6': <ShapeExtend_Status.ShapeExtend_FAIL6: 15>, 'ShapeExtend_FAIL7': <ShapeExtend_Status.ShapeExtend_FAIL7: 16>, 'ShapeExtend_FAIL8': <ShapeExtend_Status.ShapeExtend_FAIL8: 17>, 'ShapeExtend_FAIL': <ShapeExtend_Status.ShapeExtend_FAIL: 18>}
    pass
class ShapeExtend_WireData(OCP.Standard.Standard_Transient):
    """
    This class provides a data structure necessary for work with the wire as with ordered list of edges, what is required for many algorithms. The advantage of this class is that it allows to work with wires which are not correct. The object of the class ShapeExtend_WireData can be initialized by TopoDS_Wire, and converted back to TopoDS_Wire. An edge in the wire is defined by its rank number. Operations of accessing, adding and removing edge at the given rank number are provided. On the whole wire, operations of circular permutation and reversing (both orientations of all edges and order of edges) are provided as well. This class also provides a method to check if the edge in the wire is a seam (if the wire lies on a face). This class is handled by reference. Such an approach gives the following advantages: 1. Sharing the object of this class strongly optimizes the processes of analysis and fixing performed in parallel on the wire stored in the form of this class. Fixing tool (e.g. ShapeFix_Wire) fixes problems one by one using analyzing tool (e.g. ShapeAnalysis_Wire). Sharing allows not to reinitialize each time the analyzing tool with modified ShapeExtend_WireData what consumes certain time. 2. No copying of contents. The object of ShapeExtend_WireData class has quite big size, returning it as a result of the function would cause additional copying of contents if this class were one handled by value. Moreover, this class is stored as a field in other classes which are they returned as results of functions, storing only a handle to ShapeExtend_WireData saves time and memory.This class provides a data structure necessary for work with the wire as with ordered list of edges, what is required for many algorithms. The advantage of this class is that it allows to work with wires which are not correct. The object of the class ShapeExtend_WireData can be initialized by TopoDS_Wire, and converted back to TopoDS_Wire. An edge in the wire is defined by its rank number. Operations of accessing, adding and removing edge at the given rank number are provided. On the whole wire, operations of circular permutation and reversing (both orientations of all edges and order of edges) are provided as well. This class also provides a method to check if the edge in the wire is a seam (if the wire lies on a face). This class is handled by reference. Such an approach gives the following advantages: 1. Sharing the object of this class strongly optimizes the processes of analysis and fixing performed in parallel on the wire stored in the form of this class. Fixing tool (e.g. ShapeFix_Wire) fixes problems one by one using analyzing tool (e.g. ShapeAnalysis_Wire). Sharing allows not to reinitialize each time the analyzing tool with modified ShapeExtend_WireData what consumes certain time. 2. No copying of contents. The object of ShapeExtend_WireData class has quite big size, returning it as a result of the function would cause additional copying of contents if this class were one handled by value. Moreover, this class is stored as a field in other classes which are they returned as results of functions, storing only a handle to ShapeExtend_WireData saves time and memory.This class provides a data structure necessary for work with the wire as with ordered list of edges, what is required for many algorithms. The advantage of this class is that it allows to work with wires which are not correct. The object of the class ShapeExtend_WireData can be initialized by TopoDS_Wire, and converted back to TopoDS_Wire. An edge in the wire is defined by its rank number. Operations of accessing, adding and removing edge at the given rank number are provided. On the whole wire, operations of circular permutation and reversing (both orientations of all edges and order of edges) are provided as well. This class also provides a method to check if the edge in the wire is a seam (if the wire lies on a face). This class is handled by reference. Such an approach gives the following advantages: 1. Sharing the object of this class strongly optimizes the processes of analysis and fixing performed in parallel on the wire stored in the form of this class. Fixing tool (e.g. ShapeFix_Wire) fixes problems one by one using analyzing tool (e.g. ShapeAnalysis_Wire). Sharing allows not to reinitialize each time the analyzing tool with modified ShapeExtend_WireData what consumes certain time. 2. No copying of contents. The object of ShapeExtend_WireData class has quite big size, returning it as a result of the function would cause additional copying of contents if this class were one handled by value. Moreover, this class is stored as a field in other classes which are they returned as results of functions, storing only a handle to ShapeExtend_WireData saves time and memory.
    """
    @overload
    def Add(self,wire : OCP.TopoDS.TopoDS_Wire,atnum : int=0) -> None: 
        """
        Adds an edge to a wire, being defined (not yet ended) This is the plain, basic, function to add an edge <num> = 0 (D): Appends at end <num> = 1: Preprends at start else, Insert before <num> Remark : Null Edge is simply ignored

        Adds an entire wire, considered as a list of edges Remark : The wire is assumed to be ordered (TopoDS_Iterator is used)

        Adds a wire in the form of WireData

        Adds an edge or a wire invoking corresponding method Add
        """
    @overload
    def Add(self,wire : ShapeExtend_WireData,atnum : int=0) -> None: ...
    @overload
    def Add(self,shape : OCP.TopoDS.TopoDS_Shape,atnum : int=0) -> None: ...
    @overload
    def Add(self,edge : OCP.TopoDS.TopoDS_Edge,atnum : int=0) -> None: ...
    @overload
    def AddOriented(self,wire : OCP.TopoDS.TopoDS_Wire,mode : int) -> None: 
        """
        Adds an edge to start or end of <me>, according to <mode> 0: at end, as direct 1: at end, as reversed 2: at start, as direct 3: at start, as reversed < 0: no adding

        Adds a wire to start or end of <me>, according to <mode> 0: at end, as direct 1: at end, as reversed 2: at start, as direct 3: at start, as reversed < 0: no adding

        Adds an edge or a wire invoking corresponding method AddOriented
        """
    @overload
    def AddOriented(self,edge : OCP.TopoDS.TopoDS_Edge,mode : int) -> None: ...
    @overload
    def AddOriented(self,shape : OCP.TopoDS.TopoDS_Shape,mode : int) -> None: ...
    def Clear(self) -> None: 
        """
        Clears data about Wire.
        """
    def ComputeSeams(self,enforce : bool=True) -> None: 
        """
        Computes the list of seam edges By default (direct call), computing is enforced For indirect call (from IsSeam) it is redone only if not yet already done or if the list of edges has changed Remark : A Seam Edge is an Edge present twice in the list, once as FORWARD and once as REVERSED Each sense has its own PCurve, the one for FORWARD must be set in first
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
    def Edge(self,num : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns <num>th Edge
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self,edge : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        Returns the index of the edge If the edge is a seam the orientation is also checked Returns 0 if the edge is not found in the list
        """
    @overload
    def Init(self,other : ShapeExtend_WireData) -> None: 
        """
        Copies data from another WireData

        Loads an already existing wire If <chained> is True (default), edges are added in the sequence as they are explored by TopoDS_Iterator Else, if <chained> is False, wire is explored by BRepTools_WireExplorer and it is guaranteed that edges will be sequentially connected. Remark : In the latter case it can happen that not all edges will be found (because of limitations of BRepTools_WireExplorer for disconnected wires and wires with seam edges).
        """
    @overload
    def Init(self,wire : OCP.TopoDS.TopoDS_Wire,chained : bool=True,theManifoldMode : bool=True) -> bool: ...
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
    def IsSeam(self,num : int) -> bool: 
        """
        Tells if an Edge is seam (see ComputeSeams) An edge is considered as seam if it presents twice in the edge list, once as FORWARD and once as REVERSED.
        """
    def NbEdges(self) -> int: 
        """
        Returns the count of currently recorded edges
        """
    def NbNonManifoldEdges(self) -> int: 
        """
        Returns the count of currently recorded non-manifold edges
        """
    def NonmanifoldEdge(self,num : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns <num>th nonmanifold Edge
        """
    def NonmanifoldEdges(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        Returns sequence of non-manifold edges This sequence can be not empty if wire data set in manifold mode but initial wire has INTERNAL orientation or contains INTERNAL edges
        """
    def Remove(self,num : int=0) -> None: 
        """
        Removes an Edge, given its rank. By default removes the last edge.
        """
    @overload
    def Reverse(self,face : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Reverses the sense of the list and the orientation of each Edge This method should be called when either wire has no seam edges or face is not available

        Reverses the sense of the list and the orientation of each Edge The face is necessary for swapping pcurves for seam edges (first pcurve corresponds to orientation FORWARD, and second to REVERSED; when edge is reversed, pcurves must be swapped) If face is NULL, no swapping is performed
        """
    @overload
    def Reverse(self) -> None: ...
    def Set(self,edge : OCP.TopoDS.TopoDS_Edge,num : int=0) -> None: 
        """
        Replaces an edge at the given rank number <num> with new one. Default is last edge (<num> = 0).
        """
    def SetDegeneratedLast(self) -> None: 
        """
        When the wire contains at least one degenerated edge, sets it as last one Note : It is useful to process pcurves, for instance, while the pcurve of a DGNR may not be computed from its 3D part (there is none) it is computed after the other edges have been computed and chained.
        """
    def SetLast(self,num : int) -> None: 
        """
        Does a circular permutation in order to set <num>th edge last
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Makes TopoDS_Wire using BRep_Builder (just creates the TopoDS_Wire object and adds all edges into it). This method should be called when the wire is correct (for example, after successful fixes by ShapeFix_Wire) and adjacent edges share common vertices. In case if adjacent edges do not share the same vertices the resulting TopoDS_Wire will be invalid.
        """
    def WireAPIMake(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Makes TopoDS_Wire using BRepAPI_MakeWire. Class BRepAPI_MakeWire merges geometrically coincided vertices and can disturb correct order of edges in the wire. If this class fails, null shape is returned.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,wire : OCP.TopoDS.TopoDS_Wire,chained : bool=True,theManifoldMode : bool=True) -> None: ...
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
    @property
    def ManifoldMode(self) -> bool:
        """
        Returns mode defining manifold wire data or not. If manifold that nonmanifold edges will not be not consider during operations(previous behaviour) and they will be added only in result wire else non-manifold edges will consider during operations

        :type: bool
        """
    @ManifoldMode.setter
    def ManifoldMode(self, arg1: bool) -> None:
        """
        Returns mode defining manifold wire data or not. If manifold that nonmanifold edges will not be not consider during operations(previous behaviour) and they will be added only in result wire else non-manifold edges will consider during operations
        """
    pass
ShapeExtend_DONE: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE: 9>
ShapeExtend_DONE1: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE1: 1>
ShapeExtend_DONE2: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE2: 2>
ShapeExtend_DONE3: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE3: 3>
ShapeExtend_DONE4: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE4: 4>
ShapeExtend_DONE5: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE5: 5>
ShapeExtend_DONE6: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE6: 6>
ShapeExtend_DONE7: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE7: 7>
ShapeExtend_DONE8: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_DONE8: 8>
ShapeExtend_FAIL: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL: 18>
ShapeExtend_FAIL1: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL1: 10>
ShapeExtend_FAIL2: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL2: 11>
ShapeExtend_FAIL3: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL3: 12>
ShapeExtend_FAIL4: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL4: 13>
ShapeExtend_FAIL5: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL5: 14>
ShapeExtend_FAIL6: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL6: 15>
ShapeExtend_FAIL7: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL7: 16>
ShapeExtend_FAIL8: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_FAIL8: 17>
ShapeExtend_Natural: OCP.ShapeExtend.ShapeExtend_Parametrisation # value = <ShapeExtend_Parametrisation.ShapeExtend_Natural: 0>
ShapeExtend_OK: OCP.ShapeExtend.ShapeExtend_Status # value = <ShapeExtend_Status.ShapeExtend_OK: 0>
ShapeExtend_Uniform: OCP.ShapeExtend.ShapeExtend_Parametrisation # value = <ShapeExtend_Parametrisation.ShapeExtend_Uniform: 1>
ShapeExtend_Unitary: OCP.ShapeExtend.ShapeExtend_Parametrisation # value = <ShapeExtend_Parametrisation.ShapeExtend_Unitary: 2>
