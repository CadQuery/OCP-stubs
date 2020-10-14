import OCP.IntCurvesFace
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.GeomAbs
import OCP.Bnd
import OCP.Adaptor3d
import OCP.TopoDS
import OCP.IntCurveSurface
import OCP.gp
__all__  = [
"IntCurvesFace_Intersector",
"IntCurvesFace_ShapeIntersector"
]
class IntCurvesFace_Intersector():
    """
    None
    """
    def Bounding(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def ClassifyUVPoint(self,Puv : OCP.gp.gp_Pnt2d) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the significant face used to determine the intersection.

        Returns the significant face used to determine the intersection.
        """
    def GetUseBoundToler(self) -> bool: 
        """
        Returns the boundary tolerance flag
        """
    def IsDone(self) -> bool: 
        """
        True is returned when the intersection have been computed.

        True is returned when the intersection have been computed.
        """
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
    def Perform(self,HCu : OCP.Adaptor3d.Adaptor3d_HCurve,PInf : float,PSup : float) -> None: 
        """
        Perform the intersection between the segment L and the loaded face.

        same method for a HCurve from Adaptor3d. PInf an PSup can also be - and + INF.
        """
    @overload
    def Perform(self,L : OCP.gp.gp_Lin,PInf : float,PSup : float) -> None: ...
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
        Returns the ith state of the point on the face. The values can be either TopAbs_IN ( the point is in the face) or TopAbs_ON ( the point is on a boudary of the face).

        Returns the ith state of the point on the face. The values can be either TopAbs_IN ( the point is in the face) or TopAbs_ON ( the point is on a boudary of the face).
        """
    @overload
    def State(self,i : int) -> OCP.TopAbs.TopAbs_State: ...
    def SurfaceType(self) -> OCP.GeomAbs.GeomAbs_SurfaceType: 
        """
        Return the surface type
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
    def VParameter(self,I : int) -> float: 
        """
        Returns the V parameter of the ith intersection point on the surface.

        Returns the V parameter of the ith intersection point on the surface.
        """
    @overload
    def VParameter(self,i : int) -> float: ...
    @overload
    def WParameter(self,I : int) -> float: 
        """
        Returns the parameter of the ith intersection point on the line.

        Returns the parameter of the ith intersection point on the line.
        """
    @overload
    def WParameter(self,i : int) -> float: ...
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,aTol : float,aRestr : bool=True,UseBToler : bool=True) -> None: ...
    pass
class IntCurvesFace_ShapeIntersector():
    """
    None
    """
    def Destroy(self) -> None: 
        """
        None
        """
    @overload
    def Face(self,I : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the significant face used to determine the intersection.

        Returns the significant face used to determine the intersection.
        """
    @overload
    def Face(self,i : int) -> OCP.TopoDS.TopoDS_Face: ...
    def IsDone(self) -> bool: 
        """
        True is returned when the intersection have been computed.

        True is returned when the intersection have been computed.
        """
    def Load(self,Sh : OCP.TopoDS.TopoDS_Shape,Tol : float) -> None: 
        """
        None
        """
    def NbPnt(self) -> int: 
        """
        None

        None
        """
    @overload
    def Perform(self,HCu : OCP.Adaptor3d.Adaptor3d_HCurve,PInf : float,PSup : float) -> None: 
        """
        Perform the intersection between the segment L and the loaded shape.

        same method for a HCurve from Adaptor3d. PInf an PSup can also be - and + INF.
        """
    @overload
    def Perform(self,L : OCP.gp.gp_Lin,PInf : float,PSup : float) -> None: ...
    def PerformNearest(self,L : OCP.gp.gp_Lin,PInf : float,PSup : float) -> None: 
        """
        Perform the intersection between the segment L and the loaded shape.
        """
    @overload
    def Pnt(self,I : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the geometric point of the ith intersection between the line and the surface.

        Returns the geometric point of the ith intersection between the line and the surface.
        """
    @overload
    def Pnt(self,i : int) -> OCP.gp.gp_Pnt: ...
    def SortResult(self) -> None: 
        """
        Internal method. Sort the result on the Curve parameter.
        """
    @overload
    def State(self,I : int) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the ith state of the point on the face. The values can be either TopAbs_IN ( the point is in the face) or TopAbs_ON ( the point is on a boudary of the face).

        Returns the ith state of the point on the face. The values can be either TopAbs_IN ( the point is in the face) or TopAbs_ON ( the point is on a boudary of the face).
        """
    @overload
    def State(self,i : int) -> OCP.TopAbs.TopAbs_State: ...
    @overload
    def Transition(self,i : int) -> OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve: 
        """
        Returns the ith transition of the line on the surface.

        Returns the ith transition of the line on the surface.
        """
    @overload
    def Transition(self,I : int) -> OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve: ...
    @overload
    def UParameter(self,i : int) -> float: 
        """
        Returns the U parameter of the ith intersection point on the surface.

        Returns the U parameter of the ith intersection point on the surface.
        """
    @overload
    def UParameter(self,I : int) -> float: ...
    @overload
    def VParameter(self,I : int) -> float: 
        """
        Returns the V parameter of the ith intersection point on the surface.

        Returns the V parameter of the ith intersection point on the surface.
        """
    @overload
    def VParameter(self,i : int) -> float: ...
    @overload
    def WParameter(self,I : int) -> float: 
        """
        Returns the parameter of the ith intersection point on the line.

        Returns the parameter of the ith intersection point on the line.
        """
    @overload
    def WParameter(self,i : int) -> float: ...
    def __init__(self) -> None: ...
    pass
