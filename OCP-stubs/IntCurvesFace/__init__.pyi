import OCP.IntCurvesFace
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IntCurveSurface
import OCP.Adaptor3d
import OCP.TopoDS
import OCP.TopAbs
import OCP.gp
import OCP.Bnd
import OCP.GeomAbs
import OCP.Standard
__all__  = [
"IntCurvesFace_Intersector",
"IntCurvesFace_ShapeIntersector"
]
class IntCurvesFace_Intersector(OCP.Standard.Standard_Transient):
    def Bounding(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def ClassifyUVPoint(self,Puv : OCP.gp.gp_Pnt2d) -> OCP.TopAbs.TopAbs_State: 
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
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the significant face used to determine the intersection.

        Returns the significant face used to determine the intersection.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetUseBoundToler(self) -> bool: 
        """
        Returns the boundary tolerance flag
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        True is returned when the intersection have been computed.

        True is returned when the intersection have been computed.
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
    def IsParallel(self) -> bool: 
        """
        Returns true if curve is parallel or belongs face surface This case is recognized only for some pairs of analytical curves and surfaces (plane - line, ...)

        Returns true if curve is parallel or belongs face surface This case is recognized only for some pairs of analytical curves and surfaces (plane - line, ...)
        """
    def NbPnt(self) -> int: 
        """
        None

        None
        """
    @overload
    def Perform(self,L : OCP.gp.gp_Lin,PInf : float,PSup : float) -> None: 
        """
        Perform the intersection between the segment L and the loaded face.

        same method for a HCurve from Adaptor3d. PInf an PSup can also be - and + INF.
        """
    @overload
    def Perform(self,HCu : OCP.Adaptor3d.Adaptor3d_Curve,PInf : float,PSup : float) -> None: ...
    @overload
    def Pnt(self,I : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the geometric point of the ith intersection between the line and the surface.

        Returns the geometric point of the ith intersection between the line and the surface.
        """
    @overload
    def Pnt(self,i : int) -> OCP.gp.gp_Pnt: ...
    def SetUseBoundToler(self,UseBToler : bool) -> None: 
        """
        Sets the boundary tolerance flag
        """
    @overload
    def State(self,I : int) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the ith state of the point on the face. The values can be either TopAbs_IN ( the point is in the face) or TopAbs_ON ( the point is on a boundary of the face).

        Returns the ith state of the point on the face. The values can be either TopAbs_IN ( the point is in the face) or TopAbs_ON ( the point is on a boundary of the face).
        """
    @overload
    def State(self,i : int) -> OCP.TopAbs.TopAbs_State: ...
    def SurfaceType(self) -> OCP.GeomAbs.GeomAbs_SurfaceType: 
        """
        Return the surface type
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transition(self,I : int) -> OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve: 
        """
        Returns the ith transition of the line on the surface.

        Returns the ith transition of the line on the surface.
        """
    @overload
    def Transition(self,i : int) -> OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve: ...
    @overload
    def UParameter(self,i : int) -> float: 
        """
        Returns the U parameter of the ith intersection point on the surface.

        Returns the U parameter of the ith intersection point on the surface.
        """
    @overload
    def UParameter(self,I : int) -> float: ...
    @overload
    def VParameter(self,i : int) -> float: 
        """
        Returns the V parameter of the ith intersection point on the surface.

        Returns the V parameter of the ith intersection point on the surface.
        """
    @overload
    def VParameter(self,I : int) -> float: ...
    @overload
    def WParameter(self,i : int) -> float: 
        """
        Returns the parameter of the ith intersection point on the line.

        Returns the parameter of the ith intersection point on the line.
        """
    @overload
    def WParameter(self,I : int) -> float: ...
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,aTol : float,aRestr : bool=True,UseBToler : bool=True) -> None: ...
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
class IntCurvesFace_ShapeIntersector():
    """
    None
    """
    def Face(self,I : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the significant face used to determine the intersection.
        """
    def IsDone(self) -> bool: 
        """
        True when the intersection has been computed.
        """
    def Load(self,Sh : OCP.TopoDS.TopoDS_Shape,Tol : float) -> None: 
        """
        None
        """
    def NbPnt(self) -> int: 
        """
        Returns the number of the intersection points
        """
    @overload
    def Perform(self,HCu : OCP.Adaptor3d.Adaptor3d_Curve,PInf : float,PSup : float) -> None: 
        """
        Perform the intersection between the segment L and the loaded shape.

        same method for a HCurve from Adaptor3d. PInf an PSup can also be -INF and +INF.
        """
    @overload
    def Perform(self,L : OCP.gp.gp_Lin,PInf : float,PSup : float) -> None: ...
    def PerformNearest(self,L : OCP.gp.gp_Lin,PInf : float,PSup : float) -> None: 
        """
        Perform the intersection between the segment L and the loaded shape.
        """
    def Pnt(self,I : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the geometric point of the ith intersection between the line and the surface.
        """
    def SortResult(self) -> None: 
        """
        Internal method. Sort the result on the Curve parameter.
        """
    def State(self,I : int) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the ith state of the point on the face. The values can be either TopAbs_IN ( the point is in the face) or TopAbs_ON ( the point is on a boundary of the face).
        """
    def Transition(self,I : int) -> OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve: 
        """
        Returns the ith transition of the line on the surface.
        """
    def UParameter(self,I : int) -> float: 
        """
        Returns the U parameter of the ith intersection point on the surface.
        """
    def VParameter(self,I : int) -> float: 
        """
        Returns the V parameter of the ith intersection point on the surface.
        """
    def WParameter(self,I : int) -> float: 
        """
        Returns the parameter of the ith intersection point on the line.
        """
    def __init__(self) -> None: ...
    pass
