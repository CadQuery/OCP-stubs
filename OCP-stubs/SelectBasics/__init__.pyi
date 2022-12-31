import OCP.SelectBasics
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColgp
import OCP.SelectMgr
import OCP.gp
import io
__all__  = [
"SelectBasics",
"SelectBasics_PickResult",
"SelectBasics_SelectingVolumeManager"
]
class SelectBasics():
    """
    interface class for dynamic selection
    """
    @staticmethod
    def MaxOwnerPriority_s() -> int: 
        """
        Structure to provide all-in-one result of selection of sensitive for "Matches" method of Select3D_SensitiveEntity.
        """
    @staticmethod
    def MinOwnerPriority_s() -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class SelectBasics_PickResult():
    """
    This structure provides unified access to the results of Matches() method in all sensitive entities, so that it defines a Depth (distance to the entity along picking ray) and a closest Point on entity.
    """
    def Depth(self) -> float: 
        """
        Return depth along picking ray.
        """
    def DistToGeomCenter(self) -> float: 
        """
        Return distance to geometry center (auxiliary value for comparing results).
        """
    def HasPickedPoint(self) -> bool: 
        """
        Return TRUE if Picked Point lying on detected entity was set.
        """
    def Invalidate(self) -> None: 
        """
        Reset depth value.
        """
    def IsValid(self) -> bool: 
        """
        Return TRUE if result was been defined.
        """
    @staticmethod
    def Min_s(thePickResult1 : SelectBasics_PickResult,thePickResult2 : SelectBasics_PickResult) -> SelectBasics_PickResult: 
        """
        Return closest result between two Pick Results according to Depth value.
        """
    def PickedPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Return picked point lying on detected entity. WARNING! Point is defined in local coordinate system and should be translated into World System before usage!
        """
    def SetDepth(self,theDepth : float) -> None: 
        """
        Set depth along picking ray.
        """
    def SetDistToGeomCenter(self,theDistToCenter : float) -> None: 
        """
        Set distance to geometry center.
        """
    def SetPickedPoint(self,theObjPickedPnt : OCP.gp.gp_Pnt) -> None: 
        """
        Set picked point.
        """
    @overload
    def SetSurfaceNormal(self,theNormal : OCP.gp.gp_Vec) -> None: 
        """
        Set surface normal at picked point.

        Set surface normal at picked point.
        """
    @overload
    def SetSurfaceNormal(self,theNormal : OCP.gp.gp_Vec3f) -> None: ...
    def SurfaceNormal(self) -> OCP.gp.gp_Vec3f: ...
    @overload
    def __init__(self,theDepth : float,theDistToCenter : float,theObjPickedPnt : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class SelectBasics_SelectingVolumeManager():
    """
    This class provides an interface for selecting volume manager, which is responsible for all overlap detection methods and calculation of minimum depth, distance to center of geometry and detected closest point on entity.
    """
    def DetectedPoint(self,theDepth : float) -> OCP.gp.gp_Pnt: 
        """
        Return 3D point corresponding to specified depth within picking ray.
        """
    def DistToGeometryCenter(self,theCOG : OCP.gp.gp_Pnt) -> float: 
        """
        Calculates distance from 3d projection of user-defined selection point to the given point theCOG
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetActiveSelectionType(self) -> int: 
        """
        Return selection type.
        """
    def GetFarPickedPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Valid only for point and rectangular selection. Returns projection of 2d mouse picked point or projection of center of 2d rectangle (for point and rectangular selection correspondingly) onto far view frustum plane
        """
    def GetMousePosition(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns mouse coordinates for Point selection mode.
        """
    def GetNearPickedPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Valid only for point and rectangular selection. Returns projection of 2d mouse picked point or projection of center of 2d rectangle (for point and rectangular selection correspondingly) onto near view frustum plane
        """
    def GetPlanes(self,thePlaneEquations : Any) -> None: 
        """
        Stores plane equation coefficients (in the following form: Ax + By + Cz + D = 0) to the given vector
        """
    def GetViewRayDirection(self) -> OCP.gp.gp_Dir: 
        """
        Valid only for point and rectangular selection. Returns view ray direction
        """
    def IsOverlapAllowed(self) -> bool: 
        """
        Returns flag indicating if partial overlapping of entities is allowed or should be rejected.
        """
    def IsScalableActiveVolume(self) -> bool: 
        """
        Checks if it is possible to scale current active selecting volume
        """
    @overload
    def Overlaps(self,thePnt : OCP.gp.gp_Pnt,thePickResult : SelectBasics_PickResult) -> bool: 
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
    def Overlaps(self,theArrayOfPts : OCP.TColgp.TColgp_HArray1OfPnt,theSensType : int,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,theSensType : int,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,theBoxMin : OCP.SelectMgr.SelectMgr_Vec3,theBoxMax : OCP.SelectMgr.SelectMgr_Vec3,theInside : bool=None) -> bool: ...
    @overload
    def Overlaps(self,theBoxMin : OCP.SelectMgr.SelectMgr_Vec3,theBoxMax : OCP.SelectMgr.SelectMgr_Vec3,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,theArrayOfPts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : int,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,thePnt : OCP.gp.gp_Pnt) -> bool: ...
    @overload
    def OverlapsBox(self,theBoxMin : OCP.SelectMgr.SelectMgr_Vec3,theBoxMax : OCP.SelectMgr.SelectMgr_Vec3,thePickResult : SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by box theBox

        Returns true if selecting volume is overlapped by axis-aligned bounding box with minimum corner at point theMinPt and maximum at point theMaxPt
        """
    @overload
    def OverlapsBox(self,theBoxMin : OCP.SelectMgr.SelectMgr_Vec3,theBoxMax : OCP.SelectMgr.SelectMgr_Vec3,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsCircle(self,theRadius : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,thePickResult : SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius, the boolean theIsFilled, and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().

        Returns true if selecting volume is overlapped by circle with radius theRadius, the boolean theIsFilled, and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """
    @overload
    def OverlapsCircle(self,theRadius : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,thePickResult : SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight, the boolean theIsHollow and transformation to apply theTrsf.

        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight, the boolean theIsHollow and transformation to apply theTrsf.
        """
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns true if selecting volume is overlapped by point thePnt

        Returns true if selecting volume is overlapped by point thePnt. Does not perform depth calculation, so this method is defined as helper function for inclusion test.
        """
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt,thePickResult : SelectBasics_PickResult) -> bool: ...
    def OverlapsPolygon(self,theArrayOfPts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : int,thePickResult : SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by planar convex polygon, which points are stored in theArrayOfPts, taking into account sensitivity type theSensType
        """
    def OverlapsSegment(self,thePt1 : OCP.gp.gp_Pnt,thePt2 : OCP.gp.gp_Pnt,thePickResult : SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by line segment with start point at thePt1 and end point at thePt2
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius

        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,thePickResult : SelectBasics_PickResult) -> bool: ...
    def OverlapsTriangle(self,thePt1 : OCP.gp.gp_Pnt,thePt2 : OCP.gp.gp_Pnt,thePt3 : OCP.gp.gp_Pnt,theSensType : int,thePickResult : SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by triangle with vertices thePt1, thePt2 and thePt3, taking into account sensitivity type theSensType
        """
    pass
