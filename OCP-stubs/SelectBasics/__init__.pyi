import OCP.SelectBasics
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColgp
import OCP.SelectMgr
import OCP.gp
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theDepth : float,theDistToCenter : float,theObjPickedPnt : OCP.gp.gp_Pnt) -> None: ...
    pass
class SelectBasics_SelectingVolumeManager():
    """
    This class provides an interface for selecting volume manager, which is responsible for all overlap detection methods and calculation of minimum depth, distance to center of geometry and detected closest point on entity.
    """
    def DetectedPoint(self,theDepth : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def DistToGeometryCenter(self,theCOG : OCP.gp.gp_Pnt) -> float: 
        """
        Calculates distance from 3d projection of user-defined selection point to the given point theCOG
        """
    def GetActiveSelectionType(self) -> int: 
        """
        None
        """
    def GetFarPickedPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Valid only for point and rectangular selection. Returns projection of 2d mouse picked point or projection of center of 2d rectangle (for point and rectangular selection correspondingly) onto far view frustum plane
        """
    def GetMousePosition(self) -> OCP.gp.gp_Pnt2d: 
        """
        Return mouse coordinates for Point selection mode.
        """
    def GetNearPickedPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Valid only for point and rectangular selection. Returns projection of 2d mouse picked point or projection of center of 2d rectangle (for point and rectangular selection correspondingly) onto near view frustum plane
        """
    def GetPlanes(self,thePlaneEquations : Any) -> None: 
        """
        Stores plane equation coefficients (in the following form: Ax + By + Cz + D = 0) to the given vector
        """
    def IsOverlapAllowed(self) -> bool: 
        """
        None
        """
    @overload
    def Overlaps(self,thePnt : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns true if selecting volume is overlapped by box theBox

        Returns true if selecting volume is overlapped by axis-aligned bounding box with minimum corner at point theMinPt and maximum at point theMaxPt

        Returns true if selecting volume is overlapped by point thePnt

        Returns true if selecting volume is overlapped by point thePnt. Does not perform depth calculation, so this method is defined as helper function for inclusion test.

        Returns true if selecting volume is overlapped by planar convex polygon, which points are stored in theArrayOfPts, taking into account sensitivity type theSensType

        Returns true if selecting volume is overlapped by planar convex polygon, which points are stored in theArrayOfPts, taking into account sensitivity type theSensType

        Returns true if selecting volume is overlapped by line segment with start point at thePt1 and end point at thePt2

        Returns true if selecting volume is overlapped by triangle with vertices thePt1, thePt2 and thePt3, taking into account sensitivity type theSensType
        """
    @overload
    def Overlaps(self,thePnt : OCP.gp.gp_Pnt,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,theArrayOfPts : OCP.TColgp.TColgp_HArray1OfPnt,theSensType : int,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,theBoxMin : OCP.SelectMgr.SelectMgr_Vec3,theBoxMax : OCP.SelectMgr.SelectMgr_Vec3,theInside : bool=None) -> bool: ...
    @overload
    def Overlaps(self,theBoxMin : OCP.SelectMgr.SelectMgr_Vec3,theBoxMax : OCP.SelectMgr.SelectMgr_Vec3,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,thePt1 : OCP.gp.gp_Pnt,thePt2 : OCP.gp.gp_Pnt,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,theArrayOfPts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : int,thePickResult : SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,thePt1 : OCP.gp.gp_Pnt,thePt2 : OCP.gp.gp_Pnt,thePt3 : OCP.gp.gp_Pnt,theSensType : int,thePickResult : SelectBasics_PickResult) -> bool: ...
    def __init__(self) -> None: ...
    pass
