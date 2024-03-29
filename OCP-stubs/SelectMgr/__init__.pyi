import OCP.SelectMgr
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Graphic3d
import OCP.AIS
import OCP.Aspect
import OCP.TopLoc
import OCP.SelectBasics
import OCP.TCollection
import OCP.PrsMgr
import SelectMgr_SelectableObjectSet
import OCP.Standard
import OCP.TColStd
import OCP.Prs3d
import OCP.V3d
import OCP.Select3D
import OCP.NCollection
import OCP.TopAbs
import OCP.gp
import OCP.Image
import OCP.TColgp
import OCP.Bnd
import io
import OCP.Quantity
import OCP.StdSelect
__all__  = [
"SelectMgr",
"SelectMgr_Filter",
"SelectMgr_CompositionFilter",
"SelectMgr_BaseIntersector",
"SelectMgr_BVHThreadPool",
"SelectMgr_BaseFrustum",
"SelectMgr_AxisIntersector",
"SelectMgr_AndFilter",
"SelectMgr_EntityOwner",
"SelectMgr_AndOrFilter",
"SelectMgr_FilterType",
"SelectMgr_FrustumBuilder",
"SelectMgr_IndexedDataMapOfOwnerCriterion",
"SelectMgr_ListOfFilter",
"SelectMgr_MapOfOwners",
"SelectMgr_OrFilter",
"SelectMgr_PickingStrategy",
"SelectMgr_RectangularFrustum",
"SelectMgr_SelectableObject",
"SelectMgr_SelectableObjectSet",
"SelectMgr_SelectingVolumeManager",
"SelectMgr_Selection",
"SelectMgr_SelectionImageFiller",
"SelectMgr_SelectionManager",
"SelectMgr_SelectionType",
"SelectMgr_SensitiveEntity",
"SelectMgr_SensitiveEntitySet",
"SelectMgr_SequenceOfOwner",
"SelectMgr_SequenceOfSelection",
"SelectMgr_SortCriterion",
"SelectMgr_StateOfSelection",
"SelectMgr_ToleranceMap",
"SelectMgr_TriangFrustums",
"SelectMgr_TriangularFrustum",
"SelectMgr_TriangularFrustumSet",
"SelectMgr_TypeOfBVHUpdate",
"SelectMgr_TypeOfDepthTolerance",
"SelectMgr_TypeOfUpdate",
"SelectMgr_Vec3",
"SelectMgr_ViewClipRange",
"SelectMgr_ViewerSelector",
"SelectMgr_FilterType_AND",
"SelectMgr_FilterType_OR",
"SelectMgr_PickingStrategy_FirstAcceptable",
"SelectMgr_PickingStrategy_OnlyTopmost",
"SelectMgr_SOS_Activated",
"SelectMgr_SOS_Any",
"SelectMgr_SOS_Deactivated",
"SelectMgr_SOS_Unknown",
"SelectMgr_SelectionType_Box",
"SelectMgr_SelectionType_Point",
"SelectMgr_SelectionType_Polyline",
"SelectMgr_SelectionType_Unknown",
"SelectMgr_TBU_Add",
"SelectMgr_TBU_Invalidate",
"SelectMgr_TBU_None",
"SelectMgr_TBU_Remove",
"SelectMgr_TBU_Renew",
"SelectMgr_TOU_Full",
"SelectMgr_TOU_None",
"SelectMgr_TOU_Partial",
"SelectMgr_TypeOfDepthTolerance_SensitivityFactor",
"SelectMgr_TypeOfDepthTolerance_Uniform",
"SelectMgr_TypeOfDepthTolerance_UniformPixels"
]
class SelectMgr():
    """
    Auxiliary tools for SelectMgr package.
    """
    @staticmethod
    def ComputeSensitivePrs_s(theStructure : OCP.Graphic3d.Graphic3d_Structure,theSel : SelectMgr_Selection,theLoc : OCP.gp.gp_Trsf,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Compute debug presentation for sensitive objects.
        """
    def __init__(self) -> None: ...
    pass
class SelectMgr_Filter(OCP.Standard.Standard_Transient):
    """
    The root class to define filter objects for selection. Advance handling of objects requires the services of filters. These only allow dynamic detection and selection of objects which correspond to the criteria defined in each. Eight standard filters inheriting SelectMgr_Filter are defined in Open CASCADE. You can create your own filters by defining new filter classes inheriting this framework. You use these filters by loading them into an AIS interactive context.The root class to define filter objects for selection. Advance handling of objects requires the services of filters. These only allow dynamic detection and selection of objects which correspond to the criteria defined in each. Eight standard filters inheriting SelectMgr_Filter are defined in Open CASCADE. You can create your own filters by defining new filter classes inheriting this framework. You use these filters by loading them into an AIS interactive context.The root class to define filter objects for selection. Advance handling of objects requires the services of filters. These only allow dynamic detection and selection of objects which correspond to the criteria defined in each. Eight standard filters inheriting SelectMgr_Filter are defined in Open CASCADE. You can create your own filters by defining new filter classes inheriting this framework. You use these filters by loading them into an AIS interactive context.
    """
    def ActsOn(self,aStandardMode : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
        """
        Returns true in an AIS local context, if this filter operates on a type of subshape defined in a filter class inheriting this framework. This function completes IsOk in an AIS local context.
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
    def IsOk(self,anObj : SelectMgr_EntityOwner) -> bool: 
        """
        Indicates that the selected Interactive Object passes the filter. The owner, anObj, can be either direct or user. A direct owner is the corresponding construction element, whereas a user is the compound shape of which the entity forms a part. When an object is detected by the mouse - in AIS, this is done through a context selector - its owner is passed to the filter as an argument. If the object returns Standard_True, it is kept; if not, it is rejected. If you are creating a filter class inheriting this framework, and the daughter class is to be used in an AIS local context, you will need to implement the virtual function ActsOn.
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
class SelectMgr_CompositionFilter(SelectMgr_Filter, OCP.Standard.Standard_Transient):
    """
    A framework to define a compound filter composed of two or more simple filters.A framework to define a compound filter composed of two or more simple filters.
    """
    def ActsOn(self,aStandardMode : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
        """
        None
        """
    def Add(self,afilter : SelectMgr_Filter) -> None: 
        """
        Adds the filter afilter to a filter object created by a filter class inheriting this framework.
        """
    def Clear(self) -> None: 
        """
        Clears the filters used in this framework.
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
    def IsEmpty(self) -> bool: 
        """
        Returns true if this framework is empty.
        """
    def IsIn(self,aFilter : SelectMgr_Filter) -> bool: 
        """
        Returns true if the filter aFilter is in this framework.
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
    def IsOk(self,anObj : SelectMgr_EntityOwner) -> bool: 
        """
        Indicates that the selected Interactive Object passes the filter. The owner, anObj, can be either direct or user. A direct owner is the corresponding construction element, whereas a user is the compound shape of which the entity forms a part. When an object is detected by the mouse - in AIS, this is done through a context selector - its owner is passed to the filter as an argument. If the object returns Standard_True, it is kept; if not, it is rejected. If you are creating a filter class inheriting this framework, and the daughter class is to be used in an AIS local context, you will need to implement the virtual function ActsOn.
        """
    def Remove(self,aFilter : SelectMgr_Filter) -> None: 
        """
        Removes the filter aFilter from this framework.
        """
    def StoredFilters(self) -> SelectMgr_ListOfFilter: 
        """
        Returns the list of stored filters from this framework.
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
class SelectMgr_BaseIntersector(OCP.Standard.Standard_Transient):
    """
    This class is an interface for different types of selecting intersector, defining different selection types, like point, box or polyline selection. It contains signatures of functions for detection of overlap by sensitive entity and initializes some data for building the selecting intersector
    """
    def Build(self) -> None: 
        """
        Builds intersector according to internal parameters
        """
    def Camera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Return camera definition.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DetectedPoint(self,theDepth : float) -> OCP.gp.gp_Pnt: 
        """
        Calculates the point on a view ray that was detected during the run of selection algo by given depth. It makes sense only for intersectors built on a single point. This method returns infinite point for the base class.
        """
    def DistToGeometryCenter(self,theCOG : OCP.gp.gp_Pnt) -> float: 
        """
        Measures distance between 3d projection of user-picked screen point and given point theCOG. It makes sense only for intersectors built on a single point. This method returns infinite value for the base class.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetFarPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns far point of intersector. This method returns zero point for the base class.
        """
    def GetMousePosition(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns current mouse coordinates. This method returns infinite point for the base class.
        """
    def GetNearPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns near point of intersector. This method returns zero point for the base class.
        """
    def GetPlanes(self,thePlaneEquations : Any) -> None: 
        """
        Stores plane equation coefficients (in the following form: Ax + By + Cz + D = 0) to the given vector. This method only clears input vector for the base class.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectionType(self) -> SelectMgr_SelectionType: 
        """
        Returns selection type of this intersector
        """
    def GetViewRayDirection(self) -> OCP.gp.gp_Dir: 
        """
        Returns direction ray of intersector. This method returns zero direction for the base class.
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
    def IsScalable(self) -> bool: 
        """
        Checks if it is possible to scale this intersector.
        """
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given axis-aligned box

        Returns true if selecting volume is overlapped by axis-aligned bounding box with minimum corner at point theMinPt and maximum at point theMaxPt
        """
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().

        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.

        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined volume and given point

        Intersection test between defined volume and given point Does not perform depth calculation, so this method is defined as helper function for inclusion test. Therefore, its implementation makes sense only for rectangular frustum with box selection mode activated.
        """
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt) -> bool: ...
    def OverlapsPolygon(self,theArrayOfPnts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given ordered set of points, representing line segments. The test may be considered of interior part or boundary line defined by segments depending on given sensitivity type
        """
    def OverlapsSegment(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks if line segment overlaps selecting frustum
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius

        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    def OverlapsTriangle(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given triangle. The test may be considered of interior part or boundary line defined by triangle vertices depending on given sensitivity type
        """
    def RayCircleIntersection(self,theRadius : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theIsFilled : bool,theTime : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the circle
        """
    def RayCylinderIntersection(self,theBottomRadius : float,theTopRadius : float,theHeight : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theIsHollow : bool,theTimeEnter : float,theTimeLeave : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the hollow cylinder (or cone)
        """
    def RaySphereIntersection(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theTimeEnter : float,theTimeLeave : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the sphere with center at theCenter and radius TheRadius
        """
    def ScaleAndTransform(self,theScaleFactor : int,theTrsf : OCP.gp.gp_GTrsf,theBuilder : SelectMgr_FrustumBuilder) -> SelectMgr_BaseIntersector: 
        """
        Note that this method does not perform any checks on type of the frustum.
        """
    def SetCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Saves camera definition.
        """
    def SetPixelTolerance(self,theTol : int) -> None: 
        """
        Sets pixel tolerance. It makes sense only for scalable intersectors (built on a single point). This method does nothing for the base class.
        """
    def SetViewport(self,theX : float,theY : float,theWidth : float,theHeight : float) -> None: 
        """
        Sets viewport parameters. This method does nothing for the base class.
        """
    def SetWindowSize(self,theWidth : int,theHeight : int) -> None: 
        """
        Sets current window size. This method does nothing for the base class.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WindowSize(self) -> Tuple[int, int]: 
        """
        Returns current window size. This method doesn't set any output values for the base class.
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
class SelectMgr_BVHThreadPool(OCP.Standard.Standard_Transient):
    """
    Class defining a thread pool for building BVH for the list of Select3D_SensitiveEntity within background thread(s).
    """
    def AddEntity(self,theEntity : OCP.Select3D.Select3D_SensitiveEntity) -> None: 
        """
        Queue a sensitive entity to build its BVH
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
    def StopThreads(self) -> None: 
        """
        Stops threads
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Threads(self) -> Any: 
        """
        Returns array of threads
        """
    def WaitThreads(self) -> None: 
        """
        Waits for all threads finish their jobs
        """
    def __init__(self,theNbThreads : int) -> None: ...
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
class SelectMgr_BaseFrustum(SelectMgr_BaseIntersector, OCP.Standard.Standard_Transient):
    """
    This class is an interface for different types of selecting frustums, defining different selection types, like point, box or polyline selection. It contains signatures of functions for detection of overlap by sensitive entity and initializes some data for building the selecting frustum
    """
    def Build(self) -> None: 
        """
        Builds intersector according to internal parameters
        """
    def Camera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Return camera definition.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DetectedPoint(self,theDepth : float) -> OCP.gp.gp_Pnt: 
        """
        Calculates the point on a view ray that was detected during the run of selection algo by given depth. It makes sense only for intersectors built on a single point. This method returns infinite point for the base class.
        """
    def DistToGeometryCenter(self,theCOG : OCP.gp.gp_Pnt) -> float: 
        """
        Measures distance between 3d projection of user-picked screen point and given point theCOG. It makes sense only for intersectors built on a single point. This method returns infinite value for the base class.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetFarPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns far point of intersector. This method returns zero point for the base class.
        """
    def GetMousePosition(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns current mouse coordinates. This method returns infinite point for the base class.
        """
    def GetNearPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns near point of intersector. This method returns zero point for the base class.
        """
    def GetPlanes(self,thePlaneEquations : Any) -> None: 
        """
        Stores plane equation coefficients (in the following form: Ax + By + Cz + D = 0) to the given vector. This method only clears input vector for the base class.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectionType(self) -> SelectMgr_SelectionType: 
        """
        Returns selection type of this intersector
        """
    def GetViewRayDirection(self) -> OCP.gp.gp_Dir: 
        """
        Returns direction ray of intersector. This method returns zero direction for the base class.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsBoundaryIntersectSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,thePlaneNormal : OCP.gp.gp_Dir,theBoundaries : OCP.TColgp.TColgp_Array1OfPnt,theBoundaryInside : bool) -> bool: 
        """
        Checks whether the boundary of the current volume selection intersects with a sphere or are there it's boundaries lying inside the sphere
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
    def IsScalable(self) -> bool: 
        """
        Checks if it is possible to scale this intersector.
        """
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given axis-aligned box

        Returns true if selecting volume is overlapped by axis-aligned bounding box with minimum corner at point theMinPt and maximum at point theMaxPt
        """
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().

        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.

        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined volume and given point

        Intersection test between defined volume and given point Does not perform depth calculation, so this method is defined as helper function for inclusion test. Therefore, its implementation makes sense only for rectangular frustum with box selection mode activated.
        """
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt) -> bool: ...
    def OverlapsPolygon(self,theArrayOfPnts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given ordered set of points, representing line segments. The test may be considered of interior part or boundary line defined by segments depending on given sensitivity type
        """
    def OverlapsSegment(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks if line segment overlaps selecting frustum
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius

        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    def OverlapsTriangle(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given triangle. The test may be considered of interior part or boundary line defined by triangle vertices depending on given sensitivity type
        """
    def RayCircleIntersection(self,theRadius : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theIsFilled : bool,theTime : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the circle
        """
    def RayCylinderIntersection(self,theBottomRadius : float,theTopRadius : float,theHeight : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theIsHollow : bool,theTimeEnter : float,theTimeLeave : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the hollow cylinder (or cone)
        """
    def RaySphereIntersection(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theTimeEnter : float,theTimeLeave : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the sphere with center at theCenter and radius TheRadius
        """
    def ScaleAndTransform(self,theScaleFactor : int,theTrsf : OCP.gp.gp_GTrsf,theBuilder : SelectMgr_FrustumBuilder) -> SelectMgr_BaseIntersector: 
        """
        Note that this method does not perform any checks on type of the frustum.
        """
    def SetBuilder(self,theBuilder : SelectMgr_FrustumBuilder) -> None: 
        """
        Nullifies the builder created in the constructor and copies the pointer given
        """
    def SetCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Saves camera definition and passes it to builder
        """
    def SetPixelTolerance(self,theTol : int) -> None: 
        """
        None
        """
    def SetViewport(self,theX : float,theY : float,theWidth : float,theHeight : float) -> None: 
        """
        Passes viewport parameters to builder
        """
    def SetWindowSize(self,theWidth : int,theHeight : int) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WindowSize(self) -> Tuple[int, int]: 
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
class SelectMgr_AxisIntersector(SelectMgr_BaseIntersector, OCP.Standard.Standard_Transient):
    """
    This class contains representation of selecting axis, created in case of point selection and algorithms for overlap detection between this axis and sensitive entities.
    """
    def Build(self) -> None: 
        """
        Builds axis according to internal parameters. NOTE: it should be called after Init() method
        """
    def Camera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Return camera definition.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DetectedPoint(self,theDepth : float) -> OCP.gp.gp_Pnt: 
        """
        Calculates the point on a axis ray that was detected during the run of selection algo by given depth
        """
    def DistToGeometryCenter(self,theCOG : OCP.gp.gp_Pnt) -> float: 
        """
        Measures distance between start axis point and given point theCOG.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetFarPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns far point along axis (infinite).
        """
    def GetMousePosition(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns current mouse coordinates. This method returns infinite point for the base class.
        """
    def GetNearPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns near point along axis.
        """
    def GetPlanes(self,thePlaneEquations : Any) -> None: 
        """
        Stores plane equation coefficients (in the following form: Ax + By + Cz + D = 0) to the given vector. This method only clears input vector for the base class.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectionType(self) -> SelectMgr_SelectionType: 
        """
        Returns selection type of this intersector
        """
    def GetViewRayDirection(self) -> OCP.gp.gp_Dir: 
        """
        Returns axis direction.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theAxis : OCP.gp.gp_Ax1) -> None: 
        """
        Initializes selecting axis according to the input one
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
    def IsScalable(self) -> bool: 
        """
        Returns FALSE (not applicable to this volume).
        """
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined axis and given axis-aligned box

        Returns true if selecting axis intersects axis-aligned bounding box with minimum corner at point theMinPt and maximum at point theMaxPt
        """
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theInside : bool) -> bool: ...
    @overload
    def OverlapsCircle(self,theRadius : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().

        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """
    @overload
    def OverlapsCircle(self,theRadius : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.

        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined axis and given point

        Intersection test between defined axis and given point
        """
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt) -> bool: ...
    def OverlapsPolygon(self,theArrayOfPnts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined axis and given ordered set of points, representing line segments. The test may be considered of interior part or boundary line defined by segments depending on given sensitivity type
        """
    def OverlapsSegment(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks if selecting axis intersects line segment
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined axis and given sphere with center theCenter and radius theRadius

        Intersection test between defined axis and given sphere with center theCenter and radius theRadius
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theInside : bool=None) -> bool: ...
    def OverlapsTriangle(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined axis and given triangle. The test may be considered of interior part or boundary line defined by triangle vertices depending on given sensitivity type
        """
    def RayCircleIntersection(self,theRadius : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theIsFilled : bool,theTime : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the circle
        """
    def RayCylinderIntersection(self,theBottomRadius : float,theTopRadius : float,theHeight : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theIsHollow : bool,theTimeEnter : float,theTimeLeave : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the hollow cylinder (or cone)
        """
    def RaySphereIntersection(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theTimeEnter : float,theTimeLeave : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the sphere with center at theCenter and radius TheRadius
        """
    def ScaleAndTransform(self,theScaleFactor : int,theTrsf : OCP.gp.gp_GTrsf,theBuilder : SelectMgr_FrustumBuilder) -> SelectMgr_BaseIntersector: 
        """
        IMPORTANT: Scaling doesn't make sense for this intersector. Returns a copy of the intersector transformed using the matrix given. Builder is an optional argument that represents corresponding settings for re-constructing transformed frustum from scratch. Can be null if reconstruction is not expected furthermore.
        """
    def SetCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Saves camera definition. Do nothing for axis intersector (not applicable to this volume).
        """
    def SetPixelTolerance(self,theTol : int) -> None: 
        """
        Sets pixel tolerance. It makes sense only for scalable intersectors (built on a single point). This method does nothing for the base class.
        """
    def SetViewport(self,theX : float,theY : float,theWidth : float,theHeight : float) -> None: 
        """
        Sets viewport parameters. This method does nothing for the base class.
        """
    def SetWindowSize(self,theWidth : int,theHeight : int) -> None: 
        """
        Sets current window size. This method does nothing for the base class.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WindowSize(self) -> Tuple[int, int]: 
        """
        Returns current window size. This method doesn't set any output values for the base class.
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
class SelectMgr_AndFilter(SelectMgr_CompositionFilter, SelectMgr_Filter, OCP.Standard.Standard_Transient):
    """
    A framework to define a selection filter for two or more types of entity.A framework to define a selection filter for two or more types of entity.A framework to define a selection filter for two or more types of entity.
    """
    def ActsOn(self,aStandardMode : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
        """
        None
        """
    def Add(self,afilter : SelectMgr_Filter) -> None: 
        """
        Adds the filter afilter to a filter object created by a filter class inheriting this framework.
        """
    def Clear(self) -> None: 
        """
        Clears the filters used in this framework.
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
    def IsEmpty(self) -> bool: 
        """
        Returns true if this framework is empty.
        """
    def IsIn(self,aFilter : SelectMgr_Filter) -> bool: 
        """
        Returns true if the filter aFilter is in this framework.
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
    def IsOk(self,anobj : SelectMgr_EntityOwner) -> bool: 
        """
        None
        """
    def Remove(self,aFilter : SelectMgr_Filter) -> None: 
        """
        Removes the filter aFilter from this framework.
        """
    def StoredFilters(self) -> SelectMgr_ListOfFilter: 
        """
        Returns the list of stored filters from this framework.
        """
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
class SelectMgr_EntityOwner(OCP.Standard.Standard_Transient):
    """
    A framework to define classes of owners of sensitive primitives. The owner is the link between application and selection data structures. For the application to make its own objects selectable, it must define owner classes inheriting this framework.A framework to define classes of owners of sensitive primitives. The owner is the link between application and selection data structures. For the application to make its own objects selectable, it must define owner classes inheriting this framework.
    """
    def Clear(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,theMode : int=0) -> None: 
        """
        Clears the owners matching the value of the selection mode aMode from the presentation manager object aPM.
        """
    def ComesFromDecomposition(self) -> bool: 
        """
        Returns TRUE if this owner points to a part of object and FALSE for entire object.
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
    def HandleMouseClick(self,thePoint : OCP.Graphic3d.Graphic3d_Vec2i,theButton : int,theModifiers : int,theIsDoubleClick : bool) -> bool: 
        """
        Handle mouse button click event. Does nothing by default and returns FALSE.
        """
    def HasLocation(self) -> bool: 
        """
        Returns TRUE if selectable has transformation.
        """
    def HasSelectable(self) -> bool: 
        """
        Returns true if there is a selectable object to serve as an owner.
        """
    def HilightWithColor(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,theStyle : OCP.Prs3d.Prs3d_Drawer,theMode : int=0) -> None: 
        """
        Highlights selectable object's presentation with display mode in presentation manager with given highlight style. Also a check for auto-highlight is performed - if selectable object manages highlighting on its own, execution will be passed to SelectMgr_SelectableObject::HilightOwnerWithColor method.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAutoHilight(self) -> bool: 
        """
        if owner is not auto hilighted, for group contains many such owners will be called one method HilightSelected of SelectableObject
        """
    def IsForcedHilight(self) -> bool: 
        """
        if this method returns TRUE the owner will always call method Hilight for SelectableObject when the owner is detected. By default it always return FALSE.
        """
    def IsHilighted(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,theMode : int=0) -> bool: 
        """
        Returns true if the presentation manager highlights selections corresponding to the selection mode.
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
    def IsSameSelectable(self,theOther : SelectMgr_SelectableObject) -> bool: 
        """
        Returns true if pointer to selectable object of this owner is equal to the given one
        """
    def IsSelected(self) -> bool: 
        """
        Returns Standard_True if the owner is selected.
        """
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Returns transformation of selectable.
        """
    def Priority(self) -> int: 
        """
        Return selection priority (within range [0-9]) for results with the same depth; 0 by default. Example - selection of shapes: the owners are selectable objects (presentations) a user can give vertex priority [3], edges [2] faces [1] shape [0], so that if during selection one vertex one edge and one face are simultaneously detected, the vertex will only be hilighted.
        """
    def Selectable(self) -> SelectMgr_SelectableObject: 
        """
        Returns a selectable object detected in the working context.
        """
    @overload
    def Set(self,theSelObj : SelectMgr_SelectableObject) -> None: 
        """
        Sets the selectable object.

        sets the selectable priority of the owner
        """
    @overload
    def Set(self,thePriority : int) -> None: ...
    def SetComesFromDecomposition(self,theIsFromDecomposition : bool) -> None: 
        """
        Sets flag indicating this owner points to a part of object (TRUE) or to entire object (FALSE).
        """
    def SetLocation(self,theLocation : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Change owner location (callback for handling change of location of selectable object).
        """
    def SetPriority(self,thePriority : int) -> None: 
        """
        Sets the selectable priority of the owner within range [0-9].
        """
    def SetSelectable(self,theSelObj : SelectMgr_SelectableObject) -> None: 
        """
        Sets the selectable object.
        """
    def SetSelected(self,theIsSelected : bool) -> None: 
        """
        Set the state of the owner.
        """
    def SetZLayer(self,theLayerId : int) -> None: 
        """
        Set Z layer ID and update all presentations.
        """
    @overload
    def State(self) -> int: 
        """
        Returns selection state.

        Set the state of the owner. The method is deprecated. Use SetSelected() instead.
        """
    @overload
    def State(self,theStatus : int) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unhilight(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,theMode : int=0) -> None: 
        """
        Removes highlighting from the owner of a detected selectable object in the presentation manager. This object could be the owner of a sensitive primitive.
        """
    def UpdateHighlightTrsf(self,theViewer : OCP.V3d.V3d_Viewer,theManager : OCP.PrsMgr.PrsMgr_PresentationManager,theDispMode : int) -> None: 
        """
        Implements immediate application of location transformation of parent object to dynamic highlight structure
        """
    @overload
    def __init__(self,aPriority : int=0) -> None: ...
    @overload
    def __init__(self,aSO : SelectMgr_SelectableObject,aPriority : int=0) -> None: ...
    @overload
    def __init__(self,theOwner : SelectMgr_EntityOwner,aPriority : int=0) -> None: ...
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
class SelectMgr_AndOrFilter(SelectMgr_CompositionFilter, SelectMgr_Filter, OCP.Standard.Standard_Transient):
    """
    A framework to define an OR or AND selection filter. To use an AND selection filter call SetUseOrFilter with False parameter. By default the OR selection filter is used.A framework to define an OR or AND selection filter. To use an AND selection filter call SetUseOrFilter with False parameter. By default the OR selection filter is used.
    """
    def ActsOn(self,aStandardMode : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
        """
        None
        """
    def Add(self,afilter : SelectMgr_Filter) -> None: 
        """
        Adds the filter afilter to a filter object created by a filter class inheriting this framework.
        """
    def Clear(self) -> None: 
        """
        Clears the filters used in this framework.
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
    def FilterType(self) -> SelectMgr_FilterType: 
        """
        Returns a selection filter type ( SelectMgr_FilterType).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if this framework is empty.
        """
    def IsIn(self,aFilter : SelectMgr_Filter) -> bool: 
        """
        Returns true if the filter aFilter is in this framework.
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
    def IsOk(self,theObj : SelectMgr_EntityOwner) -> bool: 
        """
        Indicates that the selected Interactive Object passes the filter.
        """
    def Remove(self,aFilter : SelectMgr_Filter) -> None: 
        """
        Removes the filter aFilter from this framework.
        """
    def SetDisabledObjects(self,theObjects : Any) -> None: 
        """
        Disable selection of specified objects.
        """
    def SetFilterType(self,theFilterType : SelectMgr_FilterType) -> None: 
        """
        Sets a selection filter type. SelectMgr_FilterType_OR selection filter is used be default.
        """
    def StoredFilters(self) -> SelectMgr_ListOfFilter: 
        """
        Returns the list of stored filters from this framework.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theFilterType : SelectMgr_FilterType) -> None: ...
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
class SelectMgr_FilterType():
    """
    Enumeration defines the filter type.

    Members:

      SelectMgr_FilterType_AND

      SelectMgr_FilterType_OR
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
    SelectMgr_FilterType_AND: OCP.SelectMgr.SelectMgr_FilterType # value = <SelectMgr_FilterType.SelectMgr_FilterType_AND: 0>
    SelectMgr_FilterType_OR: OCP.SelectMgr.SelectMgr_FilterType # value = <SelectMgr_FilterType.SelectMgr_FilterType_OR: 1>
    __entries: dict # value = {'SelectMgr_FilterType_AND': (<SelectMgr_FilterType.SelectMgr_FilterType_AND: 0>, None), 'SelectMgr_FilterType_OR': (<SelectMgr_FilterType.SelectMgr_FilterType_OR: 1>, None)}
    __members__: dict # value = {'SelectMgr_FilterType_AND': <SelectMgr_FilterType.SelectMgr_FilterType_AND: 0>, 'SelectMgr_FilterType_OR': <SelectMgr_FilterType.SelectMgr_FilterType_OR: 1>}
    pass
class SelectMgr_FrustumBuilder(OCP.Standard.Standard_Transient):
    """
    The purpose of this class is to provide unified interface for building selecting frustum depending on current camera projection and orientation matrices, window size and viewport parameters.The purpose of this class is to provide unified interface for building selecting frustum depending on current camera projection and orientation matrices, window size and viewport parameters.
    """
    def Camera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Returns current camera
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
    def InvalidateViewport(self) -> None: 
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
    def ProjectPntOnViewPlane(self,theX : float,theY : float,theZ : float) -> OCP.gp.gp_Pnt: 
        """
        Projects 2d screen point onto view frustum plane: theZ = 0 - near plane, theZ = 1 - far plane
        """
    def SetCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Stores current camera
        """
    def SetViewport(self,theX : float,theY : float,theWidth : float,theHeight : float) -> None: 
        """
        Stores current viewport coordinates
        """
    def SetWindowSize(self,theWidth : int,theHeight : int) -> None: 
        """
        Stores current window width and height
        """
    def SignedPlanePntDist(self,theEq : SelectMgr_Vec3,thePnt : SelectMgr_Vec3) -> float: 
        """
        Calculates signed distance between plane with equation theEq and point thePnt
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WindowSize(self) -> Tuple[int, int]: 
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
class SelectMgr_IndexedDataMapOfOwnerCriterion(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : SelectMgr_EntityOwner,theItem : SelectMgr_SortCriterion) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : SelectMgr_IndexedDataMapOfOwnerCriterion) -> SelectMgr_IndexedDataMapOfOwnerCriterion: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> SelectMgr_SortCriterion: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : SelectMgr_EntityOwner) -> SelectMgr_SortCriterion: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : SelectMgr_EntityOwner) -> SelectMgr_SortCriterion: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : SelectMgr_EntityOwner) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : SelectMgr_IndexedDataMapOfOwnerCriterion) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> SelectMgr_SortCriterion: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : SelectMgr_EntityOwner,theValue : SelectMgr_SortCriterion) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : SelectMgr_EntityOwner) -> SelectMgr_SortCriterion: ...
    def FindIndex(self,theKey1 : SelectMgr_EntityOwner) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> SelectMgr_EntityOwner: 
        """
        FindKey
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
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : SelectMgr_EntityOwner) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : SelectMgr_EntityOwner) -> SelectMgr_SortCriterion: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : SelectMgr_EntityOwner,theItem : SelectMgr_SortCriterion) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : SelectMgr_IndexedDataMapOfOwnerCriterion) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class SelectMgr_ListOfFilter(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : SelectMgr_ListOfFilter) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : SelectMgr_Filter) -> SelectMgr_Filter: ...
    @overload
    def Append(self,theItem : SelectMgr_Filter,theIter : Any) -> None: ...
    def Assign(self,theOther : SelectMgr_ListOfFilter) -> SelectMgr_ListOfFilter: 
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
    def First(self) -> SelectMgr_Filter: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : SelectMgr_Filter,theIter : Any) -> SelectMgr_Filter: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : SelectMgr_ListOfFilter,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : SelectMgr_ListOfFilter,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : SelectMgr_Filter,theIter : Any) -> SelectMgr_Filter: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> SelectMgr_Filter: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : SelectMgr_Filter) -> SelectMgr_Filter: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : SelectMgr_ListOfFilter) -> None: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : SelectMgr_ListOfFilter) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class SelectMgr_MapOfOwners(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : SelectMgr_MapOfOwners) -> SelectMgr_MapOfOwners: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : SelectMgr_EntityOwner,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : SelectMgr_EntityOwner,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : SelectMgr_EntityOwner) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : SelectMgr_EntityOwner) -> int: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : SelectMgr_MapOfOwners) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : SelectMgr_EntityOwner) -> int: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : SelectMgr_EntityOwner,theValue : int) -> bool: ...
    def IsBound(self,theKey : SelectMgr_EntityOwner) -> bool: 
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
    def Seek(self,theKey : SelectMgr_EntityOwner) -> int: 
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
    def UnBind(self,theKey : SelectMgr_EntityOwner) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : SelectMgr_MapOfOwners) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class SelectMgr_OrFilter(SelectMgr_CompositionFilter, SelectMgr_Filter, OCP.Standard.Standard_Transient):
    """
    A framework to define an or selection filter. This selects one or another type of sensitive entity.A framework to define an or selection filter. This selects one or another type of sensitive entity.A framework to define an or selection filter. This selects one or another type of sensitive entity.
    """
    def ActsOn(self,aStandardMode : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
        """
        None
        """
    def Add(self,afilter : SelectMgr_Filter) -> None: 
        """
        Adds the filter afilter to a filter object created by a filter class inheriting this framework.
        """
    def Clear(self) -> None: 
        """
        Clears the filters used in this framework.
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
    def IsEmpty(self) -> bool: 
        """
        Returns true if this framework is empty.
        """
    def IsIn(self,aFilter : SelectMgr_Filter) -> bool: 
        """
        Returns true if the filter aFilter is in this framework.
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
    def IsOk(self,anobj : SelectMgr_EntityOwner) -> bool: 
        """
        None
        """
    def Remove(self,aFilter : SelectMgr_Filter) -> None: 
        """
        Removes the filter aFilter from this framework.
        """
    def StoredFilters(self) -> SelectMgr_ListOfFilter: 
        """
        Returns the list of stored filters from this framework.
        """
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
class SelectMgr_PickingStrategy():
    """
    Enumeration defines picking strategy - which entities detected by picking line will be accepted, considering selection filters.

    Members:

      SelectMgr_PickingStrategy_FirstAcceptable

      SelectMgr_PickingStrategy_OnlyTopmost
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
    SelectMgr_PickingStrategy_FirstAcceptable: OCP.SelectMgr.SelectMgr_PickingStrategy # value = <SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_FirstAcceptable: 0>
    SelectMgr_PickingStrategy_OnlyTopmost: OCP.SelectMgr.SelectMgr_PickingStrategy # value = <SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_OnlyTopmost: 1>
    __entries: dict # value = {'SelectMgr_PickingStrategy_FirstAcceptable': (<SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_FirstAcceptable: 0>, None), 'SelectMgr_PickingStrategy_OnlyTopmost': (<SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_OnlyTopmost: 1>, None)}
    __members__: dict # value = {'SelectMgr_PickingStrategy_FirstAcceptable': <SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_FirstAcceptable: 0>, 'SelectMgr_PickingStrategy_OnlyTopmost': <SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_OnlyTopmost: 1>}
    pass
class SelectMgr_RectangularFrustum():
    """
    This class contains representation of rectangular selecting frustum, created in case of point and box selection, and algorithms for overlap detection between selecting frustum and sensitive entities. The principle of frustum calculation: - for point selection: on a near view frustum plane rectangular neighborhood of user-picked point is created according to the pixel tolerance given and then this rectangle is projected onto far view frustum plane. This rectangles define the parallel bases of selecting frustum; - for box selection: box points are projected onto near and far view frustum planes. These 2 projected rectangles define parallel bases of selecting frustum. Overlap detection tests are implemented according to the terms of separating axis theorem (SAT).
    """
    def Build(self) -> None: 
        """
        Builds volume according to internal parameters. NOTE: it should be called after Init() method
        """
    def DetectedPoint(self,theDepth : float) -> OCP.gp.gp_Pnt: 
        """
        Calculates the point on a view ray that was detected during the run of selection algo by given depth
        """
    def DistToGeometryCenter(self,theCOG : OCP.gp.gp_Pnt) -> float: 
        """
        Measures distance between 3d projection of user-picked screen point and given point theCOG. It makes sense only for frustums built on a single point.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetFarPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns projection of 2d mouse picked point or projection of center of 2d rectangle (for point and rectangular selection correspondingly) onto far view frustum plane
        """
    def GetMousePosition(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns current mouse coordinates.
        """
    def GetNearPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns projection of 2d mouse picked point or projection of center of 2d rectangle (for point and rectangular selection correspondingly) onto near view frustum plane
        """
    def GetPlanes(self,thePlaneEquations : Any) -> None: 
        """
        Stores plane equation coefficients (in the following form: Ax + By + Cz + D = 0) to the given vector
        """
    def GetVertices(self) -> OCP.gp.gp_Pnt: 
        """
        A set of helper functions that return rectangular selecting frustum data
        """
    def GetViewRayDirection(self) -> OCP.gp.gp_Dir: 
        """
        Returns view ray direction.
        """
    @overload
    def Init(self,thePoint : OCP.gp.gp_Pnt2d) -> None: 
        """
        Initializes volume according to the point and given pixel tolerance

        Initializes volume according to the selected rectangle
        """
    @overload
    def Init(self,theMinPnt : OCP.gp.gp_Pnt2d,theMaxPnt : OCP.gp.gp_Pnt2d) -> None: ...
    def IsScalable(self) -> bool: 
        """
        Checks if it is possible to scale this frustum. It is true for frustum built on a single point.
        """
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theInside : bool) -> bool: 
        """
        SAT intersection test between defined volume and given axis-aligned box

        Returns true if selecting volume is overlapped by axis-aligned bounding box with minimum corner at point theMinPt and maximum at point theMaxPt
        """
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().

        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.

        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined volume and given point

        Intersection test between defined volume and given point
        """
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt) -> bool: ...
    def OverlapsPolygon(self,theArrayOfPnts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given ordered set of points, representing line segments. The test may be considered of interior part or boundary line defined by segments depending on given sensitivity type
        """
    def OverlapsSegment(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks if line segment overlaps selecting frustum
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theInside : bool) -> bool: 
        """
        Intersection test between defined volume and given sphere

        Intersection test between defined volume and given sphere
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    def OverlapsTriangle(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given triangle. The test may be considered of interior part or boundary line defined by triangle vertices depending on given sensitivity type
        """
    def ScaleAndTransform(self,theScaleFactor : int,theTrsf : OCP.gp.gp_GTrsf,theBuilder : SelectMgr_FrustumBuilder) -> SelectMgr_BaseIntersector: 
        """
        IMPORTANT: Scaling makes sense only for frustum built on a single point! Note that this method does not perform any checks on type of the frustum. Returns a copy of the frustum resized according to the scale factor given and transforms it using the matrix given. There are no default parameters, but in case if: - transformation only is needed: must be initialized as any negative value; - scale only is needed: must be set to gp_Identity. Builder is an optional argument that represents corresponding settings for re-constructing transformed frustum from scratch. Can be null if reconstruction is not expected furthermore.
        """
    def __init__(self) -> None: ...
    def isIntersectCircle(self,theRadius : float,theCenter : OCP.gp.gp_Pnt,theTrsf : OCP.gp.gp_Trsf,theVertices : OCP.TColgp.TColgp_Array1OfPnt) -> bool: 
        """
        Returns True if Frustum (theVertices) intersects the circle.
        """
    def isSegmentsIntersect(self,thePnt1Seg1 : OCP.gp.gp_Pnt,thePnt2Seg1 : OCP.gp.gp_Pnt,thePnt1Seg2 : OCP.gp.gp_Pnt,thePnt2Seg2 : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns True if Seg1 (thePnt1Seg1, thePnt2Seg1) and Seg2 (thePnt1Seg2, thePnt2Seg2) intersect.
        """
    pass
class SelectMgr_SelectableObject(OCP.PrsMgr.PrsMgr_PresentableObject, OCP.Standard.Standard_Transient):
    """
    A framework to supply the structure of the object to be selected. At the first pick, this structure is created by calling the appropriate algorithm and retaining this framework for further picking. This abstract framework is inherited in Application Interactive Services (AIS), notably in AIS_InteractiveObject. Consequently, 3D selection should be handled by the relevant daughter classes and their member functions in AIS. This is particularly true in the creation of new interactive objects.A framework to supply the structure of the object to be selected. At the first pick, this structure is created by calling the appropriate algorithm and retaining this framework for further picking. This abstract framework is inherited in Application Interactive Services (AIS), notably in AIS_InteractiveObject. Consequently, 3D selection should be handled by the relevant daughter classes and their member functions in AIS. This is particularly true in the creation of new interactive objects.
    """
    def AcceptDisplayMode(self,theMode : int) -> bool: 
        """
        Returns true if the class of objects accepts specified display mode index. The interactive context can have a default mode of representation for the set of Interactive Objects. This mode may not be accepted by a given class of objects. Consequently, this virtual method allowing us to get information about the class in question must be implemented. At least one display mode index should be accepted by this method. Although subclass can leave default implementation, it is highly desired defining exact list of supported modes instead, which is usually an enumeration for one object or objects class sharing similar list of display modes.
        """
    def AcceptShapeDecomposition(self) -> bool: 
        """
        Informs the graphic context that the interactive Object may be decomposed into sub-shapes for dynamic selection. The most used Interactive Object is AIS_Shape.
        """
    def AddChild(self,theObject : OCP.PrsMgr.PrsMgr_PresentableObject) -> None: 
        """
        Makes theObject child of current object in scene hierarchy.
        """
    def AddChildWithCurrentTransformation(self,theObject : OCP.PrsMgr.PrsMgr_PresentableObject) -> None: 
        """
        Makes theObject child of current object in scene hierarchy with keeping the current global transformation So the object keeps the same position/orientation in the global CS.
        """
    def AddClipPlane(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> None: 
        """
        Adds clip plane for graphical clipping for all display mode presentations. The composition of clip planes truncates the rendering space to convex volume. Please be aware that number of supported clip plane is limited. The planes which exceed the limit are ignored. Besides of this, some planes can be already set in view where the object is shown: the number of these planes should be subtracted from limit to predict the maximum possible number of object clipping planes.
        """
    def AddSelection(self,aSelection : SelectMgr_Selection,aMode : int) -> None: 
        """
        Adds the selection aSelection with the selection mode index aMode to this framework.
        """
    def Attributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Returns the attributes settings.
        """
    def BndBoxOfSelected(self,theOwners : Any) -> OCP.Bnd.Bnd_Box: 
        """
        Returns a bounding box of sensitive entities with the owners given if they are a part of activated selection
        """
    def BoundingBox(self,theBndBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        Returns bounding box of object correspondingly to its current display mode. This method requires presentation to be already computed, since it relies on bounding box of presentation structures, which are supposed to be same/close amongst different display modes of this object.
        """
    def Children(self) -> OCP.PrsMgr.PrsMgr_ListOfPresentableObjects: 
        """
        Returns children of the current object.
        """
    def ClearDynamicHighlight(self,theMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> None: 
        """
        Method that needs to be implemented when the object manages selection and dynamic highlighting on its own. Clears or invalidates dynamic highlight presentation. By default it clears immediate draw of given presentation manager.
        """
    def ClearSelected(self) -> None: 
        """
        Method which clear all selected owners belonging to this selectable object ( for fast presentation draw )
        """
    def ClearSelections(self,update : bool=False) -> None: 
        """
        Empties all the selections in the SelectableObject <update> parameter defines whether all object's selections should be flagged for further update or not. This improved method can be used to recompute an object's selection (without redisplaying the object completely) when some selection mode is activated not for the first time.
        """
    def ClipPlanes(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Get clip planes.
        """
    def Color(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns the color setting of the Interactive Object.
        """
    def CombinedParentTransformation(self) -> OCP.TopLoc.TopLoc_Datum3D: 
        """
        Return combined parent transformation.
        """
    def ComputeSelection(self,theSelection : SelectMgr_Selection,theMode : int) -> None: 
        """
        Computes sensitive primitives for the given selection mode - key interface method of Selectable Object.
        """
    def CurrentFacingModel(self) -> OCP.Aspect.Aspect_TypeOfFacingModel: 
        """
        Returns the current facing model which is in effect.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultDisplayMode(self) -> int: 
        """
        Returns the default display mode.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisplayMode(self) -> int: 
        """
        Returns the display mode setting of the Interactive Object. The range of supported display mode indexes should be specified within object definition and filtered by AccepDisplayMode().
        """
    def DisplayStatus(self) -> OCP.PrsMgr.PrsMgr_DisplayStatus: 
        """
        Return presentation display status; PrsMgr_DisplayStatus_None by default.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicHilightAttributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Returns the hilight attributes settings. When not NULL, overrides both Prs3d_TypeOfHighlight_LocalDynamic and Prs3d_TypeOfHighlight_Dynamic defined within AIS_InteractiveContext::HighlightStyle().
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ErasePresentations(self,theToRemove : bool) -> None: 
        """
        Removes presentations returned by GetHilightPresentation() and GetSelectPresentation().
        """
    def GetAssemblyOwner(self) -> SelectMgr_EntityOwner: 
        """
        Returns common entity owner if the object is an assembly
        """
    def GetHilightPresentation(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Creates or returns existing presentation for highlighting detected object.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectPresentation(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Creates or returns existing presentation for highlighting selected object.
        """
    def GlobalSelOwner(self) -> SelectMgr_EntityOwner: 
        """
        Returns the owner of mode for selection of object as a whole
        """
    def GlobalSelectionMode(self) -> int: 
        """
        Returns the mode for selection of object as a whole; 0 by default.
        """
    def HasColor(self) -> bool: 
        """
        Returns true if the Interactive Object has color.
        """
    def HasDisplayMode(self) -> bool: 
        """
        Returns true if the Interactive Object has display mode setting overriding global setting (within Interactive Context).
        """
    def HasHilightMode(self) -> bool: 
        """
        Returns true if the Interactive Object is in highlight mode.
        """
    def HasMaterial(self) -> bool: 
        """
        Returns true if the Interactive Object has a setting for material.
        """
    def HasOwnPresentations(self) -> bool: 
        """
        Returns true if object should have own presentations.
        """
    def HasPolygonOffsets(self) -> bool: 
        """
        Returns Standard_True if <myDrawer> has non-null shading aspect
        """
    def HasSelection(self,theMode : int) -> bool: 
        """
        Returns true if a selection corresponding to the selection mode theMode was computed for this object.
        """
    def HasTransformation(self) -> bool: 
        """
        Returns true if object has a transformation that is different from the identity.
        """
    def HasWidth(self) -> bool: 
        """
        Returns true if the Interactive Object has width.
        """
    def HilightAttributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Returns the hilight attributes settings. When not NULL, overrides both Prs3d_TypeOfHighlight_LocalSelected and Prs3d_TypeOfHighlight_Selected defined within AIS_InteractiveContext::HighlightStyle().
        """
    def HilightMode(self) -> int: 
        """
        Returns highlight display mode. This is obsolete method for backward compatibility - use ::HilightAttributes() and ::DynamicHilightAttributes() instead.
        """
    def HilightOwnerWithColor(self,thePM : OCP.PrsMgr.PrsMgr_PresentationManager,theStyle : OCP.Prs3d.Prs3d_Drawer,theOwner : SelectMgr_EntityOwner) -> None: 
        """
        Method which hilight an owner belonging to this selectable object ( for fast presentation draw )
        """
    def HilightSelected(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,theSeq : SelectMgr_SequenceOfOwner) -> None: 
        """
        Method which draws selected owners ( for fast presentation draw )
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InversedTransformation(self) -> OCP.gp.gp_GTrsf: 
        """
        Return inversed transformation.
        """
    def IsAutoHilight(self) -> bool: 
        """
        If returns True, the old mechanism for highlighting selected objects is used (HilightSelected Method may be empty). If returns False, the HilightSelected method will be fully responsible for highlighting selected entity owners belonging to this selectable object.
        """
    def IsInfinite(self) -> bool: 
        """
        Returns true if the interactive object is infinite; FALSE by default. This flag affects various operations operating on bounding box of graphic presentations of this object. For instance, infinite objects are not taken in account for View FitAll. This does not necessarily means that object is actually infinite, auxiliary objects might be also marked with this flag to achieve desired behavior.
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
    def IsMutable(self) -> bool: 
        """
        Returns true if object has mutable nature (content or location are be changed regularly). Mutable object will be managed in different way than static onces (another optimizations).
        """
    def IsTransparent(self) -> bool: 
        """
        Returns true if there is a transparency setting.
        """
    def LocalTransformation(self) -> OCP.gp.gp_Trsf: 
        """
        Return the local transformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def LocalTransformationGeom(self) -> OCP.TopLoc.TopLoc_Datum3D: 
        """
        Return the local transformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def Material(self) -> OCP.Graphic3d.Graphic3d_NameOfMaterial: 
        """
        Returns the current material setting as enumeration value.
        """
    def Parent(self) -> OCP.PrsMgr.PrsMgr_PresentableObject: 
        """
        Returns parent of current object in scene hierarchy.
        """
    def PolygonOffsets(self,aFactor : float,aUnits : float) -> Tuple[int]: 
        """
        Retrieves current polygon offsets settings from <myDrawer>.
        """
    def Presentations(self) -> OCP.PrsMgr.PrsMgr_Presentations: 
        """
        Return presentations.
        """
    @overload
    def RecomputePrimitives(self) -> None: 
        """
        Re-computes the sensitive primitives for all modes. IMPORTANT: Do not use this method to update selection primitives except implementing custom selection manager! This method does not take into account necessary BVH updates, but may invalidate the pointers it refers to. TO UPDATE SELECTION properly from outside classes, use method UpdateSelection.

        Re-computes the sensitive primitives which correspond to the <theMode>th selection mode. IMPORTANT: Do not use this method to update selection primitives except implementing custom selection manager! selection manager! This method does not take into account necessary BVH updates, but may invalidate the pointers it refers to. TO UPDATE SELECTION properly from outside classes, use method UpdateSelection.
        """
    @overload
    def RecomputePrimitives(self,theMode : int) -> None: ...
    def RemoveChild(self,theObject : OCP.PrsMgr.PrsMgr_PresentableObject) -> None: 
        """
        Removes theObject from children of current object in scene hierarchy.
        """
    def RemoveChildWithRestoreTransformation(self,theObject : OCP.PrsMgr.PrsMgr_PresentableObject) -> None: 
        """
        Removes theObject from children of current object in scene hierarchy with keeping the current global transformation. So the object keeps the same position/orientation in the global CS.
        """
    def RemoveClipPlane(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> None: 
        """
        Removes previously added clip plane.
        """
    def ResetTransformation(self) -> None: 
        """
        None
        """
    def Selection(self,theMode : int) -> SelectMgr_Selection: 
        """
        Returns the selection having specified selection mode or NULL.
        """
    def Selections(self) -> SelectMgr_SequenceOfSelection: 
        """
        Return the sequence of selections.
        """
    def SetAssemblyOwner(self,theOwner : SelectMgr_EntityOwner,theMode : int=-1) -> None: 
        """
        Sets common entity owner for assembly sensitive object entities
        """
    def SetAttributes(self,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Initializes the drawing tool theDrawer.
        """
    def SetAutoHilight(self,theAutoHilight : bool) -> None: 
        """
        Set AutoHilight property to true or false.
        """
    def SetClipPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Set clip planes for graphical clipping for all display mode presentations. The composition of clip planes truncates the rendering space to convex volume. Please be aware that number of supported clip plane is limited. The planes which exceed the limit are ignored. Besides of this, some planes can be already set in view where the object is shown: the number of these planes should be subtracted from limit to predict the maximum possible number of object clipping planes.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Only the interactive object knowns which Drawer attribute is affected by the color, if any (ex: for a wire,it's the wireaspect field of the drawer, but for a vertex, only the point aspect field is affected by the color). WARNING : Do not forget to set the corresponding fields here (hasOwnColor and myDrawer->SetColor())
        """
    def SetCurrentFacingModel(self,theModel : OCP.Aspect.Aspect_TypeOfFacingModel=Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None: 
        """
        change the current facing model apply on polygons for SetColor(), SetTransparency(), SetMaterial() methods default facing model is Aspect_TOFM_TWO_SIDE. This mean that attributes is applying both on the front and back face.
        """
    def SetDisplayMode(self,theMode : int) -> None: 
        """
        Sets the display mode for the interactive object. An object can have its own temporary display mode, which is different from that proposed by the interactive context.
        """
    def SetDynamicHilightAttributes(self,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Initializes the dynamic hilight drawing tool.
        """
    def SetHilightAttributes(self,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Initializes the hilight drawing tool theDrawer.
        """
    def SetHilightMode(self,theMode : int) -> None: 
        """
        Sets highlight display mode. This is obsolete method for backward compatibility - use ::HilightAttributes() and ::DynamicHilightAttributes() instead.
        """
    def SetInfiniteState(self,theFlag : bool=True) -> None: 
        """
        Sets if object should be considered as infinite.
        """
    def SetIsoOnTriangulation(self,theIsEnabled : bool) -> None: 
        """
        Enables or disables on-triangulation build of isolines according to the flag given.
        """
    @overload
    def SetLocalTransformation(self,theTrsf : OCP.gp.gp_Trsf) -> None: 
        """
        Sets local transformation to theTransformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.

        Sets local transformation to theTransformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    @overload
    def SetLocalTransformation(self,theTrsf : OCP.TopLoc.TopLoc_Datum3D) -> None: ...
    def SetMaterial(self,aName : OCP.Graphic3d.Graphic3d_MaterialAspect) -> None: 
        """
        Sets the material aMat defining this display attribute for the interactive object. Material aspect determines shading aspect, color and transparency of visible entities.
        """
    def SetMutable(self,theIsMutable : bool) -> None: 
        """
        Sets if the object has mutable nature (content or location will be changed regularly). This method should be called before object displaying to take effect.
        """
    def SetPolygonOffsets(self,aMode : int,aFactor : float=1.0,aUnits : float=0.0) -> None: 
        """
        Sets up polygon offsets for this object.
        """
    def SetPropagateVisualState(self,theFlag : bool) -> None: 
        """
        Change the value of the flag "propagate visual state"
        """
    @overload
    def SetToUpdate(self) -> None: 
        """
        Flags presentation to be updated; UpdatePresentations() will recompute these presentations.

        flags all the Presentations to be Updated.
        """
    @overload
    def SetToUpdate(self,theMode : int) -> None: ...
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Sets up Transform Persistence defining a special Local Coordinate system where this object should be located. Note that management of Transform Persistence object is more expensive than of the normal one, because it requires its position being recomputed basing on camera position within each draw call / traverse.
        """
    def SetTransparency(self,aValue : float=0.6) -> None: 
        """
        Attributes a setting aValue for transparency. The transparency value should be between 0.0 and 1.0. At 0.0 an object will be totally opaque, and at 1.0, fully transparent. Warning At a value of 1.0, there may be nothing visible.
        """
    def SetTypeOfPresentation(self,theType : OCP.PrsMgr.PrsMgr_TypeOfPresentation3d) -> None: 
        """
        Set type of presentation.
        """
    def SetWidth(self,theWidth : float) -> None: 
        """
        Allows you to provide the setting aValue for width. Only the Interactive Object knows which Drawer attribute is affected by the width setting.
        """
    def SetZLayer(self,theLayerId : int) -> None: 
        """
        Set Z layer ID and update all presentations of the selectable object. The layers mechanism allows drawing objects in higher layers in overlay of objects in lower layers.
        """
    def SynchronizeAspects(self) -> None: 
        """
        Synchronize presentation aspects after their modification.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def ToBeUpdated(self,ListOfMode : OCP.TColStd.TColStd_ListOfInteger) -> None: 
        """
        Returns TRUE if any active presentation has invalidation flag.

        gives the list of modes which are flagged "to be updated".
        """
    @overload
    def ToBeUpdated(self,theToIncludeHidden : bool=False) -> bool: ...
    def ToPropagateVisualState(self) -> bool: 
        """
        Get value of the flag "propagate visual state" It means that the display/erase/color visual state is propagated automatically to all children; by default, the flag is true
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Returns Transformation Persistence defining a special Local Coordinate system where this presentable object is located or NULL handle if not defined. Position of the object having Transformation Persistence is mutable and depends on camera position. The same applies to a bounding box of the object.
        """
    def Transformation(self) -> OCP.gp.gp_Trsf: 
        """
        Return the transformation taking into account transformation of parent object(s). Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def TransformationGeom(self) -> OCP.TopLoc.TopLoc_Datum3D: 
        """
        Return the transformation taking into account transformation of parent object(s). Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def Transparency(self) -> float: 
        """
        Returns the transparency setting. This will be between 0.0 and 1.0. At 0.0 an object will be totally opaque, and at 1.0, fully transparent.
        """
    def TypeOfPresentation3d(self) -> OCP.PrsMgr.PrsMgr_TypeOfPresentation3d: 
        """
        Returns information on whether the object accepts display in HLR mode or not.
        """
    def UnsetAttributes(self) -> None: 
        """
        Clears settings provided by the drawing tool aDrawer.
        """
    def UnsetColor(self) -> None: 
        """
        Removes color settings. Only the Interactive Object knows which Drawer attribute is affected by the color setting. For a wire, for example, wire aspect is the attribute affected. For a vertex, however, only point aspect is affected by the color setting.
        """
    def UnsetDisplayMode(self) -> None: 
        """
        Removes display mode settings from the interactive object.
        """
    def UnsetHilightAttributes(self) -> None: 
        """
        Clears settings provided by the hilight drawing tool theDrawer.
        """
    def UnsetHilightMode(self) -> None: 
        """
        Unsets highlight display mode.
        """
    def UnsetMaterial(self) -> None: 
        """
        Removes the setting for material.
        """
    def UnsetTransparency(self) -> None: 
        """
        Removes the transparency setting. The object is opaque by default.
        """
    def UnsetWidth(self) -> None: 
        """
        Reset width to default value.
        """
    def UpdateSelection(self,theMode : int=-1) -> None: 
        """
        Sets update status FULL to selections of the object. Must be used as the only method of UpdateSelection from outer classes to prevent BVH structures from being outdated.
        """
    def UpdateTransformation(self) -> None: 
        """
        Recomputes the location of the selection aSelection.
        """
    def UpdateTransformations(self,aSelection : SelectMgr_Selection) -> None: 
        """
        Updates locations in all sensitive entities from <aSelection> and in corresponding entity owners.
        """
    def ViewAffinity(self) -> OCP.Graphic3d.Graphic3d_ViewAffinity: 
        """
        Return view affinity mask.
        """
    def Width(self) -> float: 
        """
        Returns the width setting of the Interactive Object.
        """
    def ZLayer(self) -> int: 
        """
        Get ID of Z layer for main presentation.
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
class SelectMgr_SelectableObjectSet():
    """
    The purpose of this class is to organize all selectable objects into data structure, allowing to build set of BVH trees for each transformation persistence subclass of selectable objects. This allow to minify number of updates for BVH trees - for example 2D persistent object subclass depends only on camera's projection and the corresponding BVH tree needs to be updated when camera's projection parameters change, while another tree for non-persistent objects can be left unchanged in this case.
    """
    class BVHSubset_e():
        """
        This enumeration declares names for subsets of selectable objects. Each subset has independent BVH tree. The class maintains subsets of selectable objects by their persistence flag. This allows to restric rebuilding of the trees for particular subset when the camera change does not implicitly require it: - BVHSubset_3d refers to the subset of normal world-space 3D objects. Associated BVH tree does not depend on the camera's state at all. This subset uses binned BVH builder with 32 bins and 1 element per leaf. - BVHSubset_3dPersistent refers to the subset of 3D persistent selectable objects (rotate, pan, zoom persistence). Associated BVH tree needs to be updated when either the camera's projection and position change. This subset uses linear BVH builder with 32 levels of depth and 1 element per leaf. - BVHSubset_2dPersistent refers to the subset of 2D persistent selectable objects. Associated BVH tree needs to be updated only when camera's projection changes. Bounding volumes for this object subclass is represented directly in eye space coordinates. This subset uses linear BVH builder with 32 levels of depth and 1 element per leaf.

        Members:

          BVHSubset_3d

          BVHSubset_3dPersistent

          BVHSubset_2dPersistent

          BVHSubsetNb
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
        BVHSubsetNb: OCP.SelectMgr.BVHSubset_e # value = <BVHSubset_e.BVHSubsetNb: 3>
        BVHSubset_2dPersistent: OCP.SelectMgr.BVHSubset_e # value = <BVHSubset_e.BVHSubset_2dPersistent: 2>
        BVHSubset_3d: OCP.SelectMgr.BVHSubset_e # value = <BVHSubset_e.BVHSubset_3d: 0>
        BVHSubset_3dPersistent: OCP.SelectMgr.BVHSubset_e # value = <BVHSubset_e.BVHSubset_3dPersistent: 1>
        __entries: dict # value = {'BVHSubset_3d': (<BVHSubset_e.BVHSubset_3d: 0>, None), 'BVHSubset_3dPersistent': (<BVHSubset_e.BVHSubset_3dPersistent: 1>, None), 'BVHSubset_2dPersistent': (<BVHSubset_e.BVHSubset_2dPersistent: 2>, None), 'BVHSubsetNb': (<BVHSubset_e.BVHSubsetNb: 3>, None)}
        __members__: dict # value = {'BVHSubset_3d': <BVHSubset_e.BVHSubset_3d: 0>, 'BVHSubset_3dPersistent': <BVHSubset_e.BVHSubset_3dPersistent: 1>, 'BVHSubset_2dPersistent': <BVHSubset_e.BVHSubset_2dPersistent: 2>, 'BVHSubsetNb': <BVHSubset_e.BVHSubsetNb: 3>}
        pass
    def Append(self,theObject : SelectMgr_SelectableObject) -> bool: 
        """
        Adds the new selectable object to the set. The selectable object is placed into one of the predefined subsets depending on its persistence type. After adding an object, this method marks the corresponding BVH tree for rebuild.
        """
    def BVH(self,theSubset : SelectMgr_SelectableObjectSet.BVHSubset_e) -> Any: 
        """
        Returns computed BVH for the theSubset given.
        """
    def ChangeSubset(self,theObject : SelectMgr_SelectableObject) -> None: 
        """
        Performs necessary updates when object's persistence types changes. This method should be called right after changing transformation persistence flags of the objects and before updating BVH tree - to provide up-to-date state of the object set.
        """
    def Contains(self,theObject : SelectMgr_SelectableObject) -> bool: 
        """
        Returns true if this objects set contains theObject given.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetObjectById(self,theSubset : SelectMgr_SelectableObjectSet.BVHSubset_e,theIndex : int) -> SelectMgr_SelectableObject: 
        """
        Returns object from subset theSubset by theIndex given. The method allows to get selectable object referred by the index of an element of the subset's BVH tree.
        """
    @overload
    def IsEmpty(self,theSubset : SelectMgr_SelectableObjectSet.BVHSubset_e) -> bool: 
        """
        Returns true if the object set does not contain any selectable objects.

        Returns true if the specified object subset is empty.
        """
    @overload
    def IsEmpty(self) -> bool: ...
    def MarkDirty(self) -> None: 
        """
        Marks every BVH subset for update.
        """
    def Remove(self,theObject : SelectMgr_SelectableObject) -> bool: 
        """
        Removes the selectable object from the set. The selectable object is removed from the subset it has been placed into. After removing an object, this method marks the corresponding BVH tree for rebuild.
        """
    def UpdateBVH(self,theCam : OCP.Graphic3d.Graphic3d_Camera,theWinSize : OCP.Graphic3d.Graphic3d_Vec2i) -> None: 
        """
        Updates outdated BVH trees and remembers the last state of the camera view-projection matrices and viewport (window) dimensions.
        """
    def __init__(self) -> None: ...
    BVHSubsetNb: OCP.SelectMgr.BVHSubset_e # value = <BVHSubset_e.BVHSubsetNb: 3>
    BVHSubset_2dPersistent: OCP.SelectMgr.BVHSubset_e # value = <BVHSubset_e.BVHSubset_2dPersistent: 2>
    BVHSubset_3d: OCP.SelectMgr.BVHSubset_e # value = <BVHSubset_e.BVHSubset_3d: 0>
    BVHSubset_3dPersistent: OCP.SelectMgr.BVHSubset_e # value = <BVHSubset_e.BVHSubset_3dPersistent: 1>
    pass
class SelectMgr_SelectingVolumeManager(OCP.SelectBasics.SelectBasics_SelectingVolumeManager):
    """
    This class is used to switch between active selecting volumes depending on selection type chosen by the user. The sample of correct selection volume initialization procedure:
    """
    def ActiveVolume(self) -> SelectMgr_BaseIntersector: 
        """
        Returns active selecting volume that was built during last run of OCCT selection mechanism
        """
    def AllowOverlapDetection(self,theIsToAllow : bool) -> None: 
        """
        If theIsToAllow is false, only fully included sensitives will be detected, otherwise the algorithm will mark both included and overlapped entities as matched
        """
    @overload
    def BuildSelectingVolume(self) -> None: 
        """
        Builds previously initialized selecting volume.

        None

        None

        None
        """
    @overload
    def BuildSelectingVolume(self,theMinPt : OCP.gp.gp_Pnt2d,theMaxPt : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def BuildSelectingVolume(self,thePoint : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def BuildSelectingVolume(self,thePoints : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
    def Camera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Returns current camera definition.
        """
    def DetectedPoint(self,theDepth : float) -> OCP.gp.gp_Pnt: 
        """
        Calculates the point on a view ray that was detected during the run of selection algo by given depth. Throws exception if active selection type is not Point.
        """
    def DistToGeometryCenter(self,theCOG : OCP.gp.gp_Pnt) -> float: 
        """
        Measures distance between 3d projection of user-picked screen point and given point theCOG
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def GetVertices(self) -> OCP.gp.gp_Pnt: 
        """
        A set of helper functions that return rectangular selecting frustum data
        """
    def GetViewRayDirection(self) -> OCP.gp.gp_Dir: 
        """
        Valid only for point and rectangular selection. Returns view ray direction
        """
    def InitAxisSelectingVolume(self,theAxis : OCP.gp.gp_Ax1) -> None: 
        """
        Creates and activates axis selector for point selection
        """
    def InitBoxSelectingVolume(self,theMinPt : OCP.gp.gp_Pnt2d,theMaxPt : OCP.gp.gp_Pnt2d) -> None: 
        """
        Creates, initializes and activates rectangular selecting frustum for box selection
        """
    def InitPointSelectingVolume(self,thePoint : OCP.gp.gp_Pnt2d) -> None: 
        """
        Creates, initializes and activates rectangular selecting frustum for point selection
        """
    def InitPolylineSelectingVolume(self,thePoints : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        Creates, initializes and activates set of triangular selecting frustums for polyline selection
        """
    def InitSelectingVolume(self,theVolume : SelectMgr_BaseIntersector) -> None: 
        """
        Sets as active the custom selecting volume
        """
    def IsOverlapAllowed(self) -> bool: 
        """
        None
        """
    def IsScalableActiveVolume(self) -> bool: 
        """
        Checks if it is possible to scale current active selecting volume
        """
    def ObjectClipping(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Return object clipping planes.
        """
    @overload
    def Overlaps(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
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
    def Overlaps(self,theArrayOfPts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : int,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,thePnt : OCP.gp.gp_Pnt,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,theSensType : int,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,theArrayOfPts : OCP.TColgp.TColgp_HArray1OfPnt,theSensType : int,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def Overlaps(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theInside : bool=None) -> bool: ...
    @overload
    def Overlaps(self,thePnt : OCP.gp.gp_Pnt) -> bool: ...
    @overload
    def Overlaps(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,theInside : bool=None) -> bool: 
        """
        SAT intersection test between defined volume and given axis-aligned box

        Returns true if selecting volume is overlapped by axis-aligned bounding box with minimum corner at point theMinPt and maximum at point theMaxPt
        """
    @overload
    def OverlapsBox(self,theBoxMin : SelectMgr_Vec3,theBoxMax : SelectMgr_Vec3,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().

        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.

        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined volume and given point

        Intersection test between defined volume and given point
        """
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt) -> bool: ...
    def OverlapsPolygon(self,theArrayOfPts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : int,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given ordered set of points, representing line segments. The test may be considered of interior part or boundary line defined by segments depending on given sensitivity type
        """
    def OverlapsSegment(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks if line segment overlaps selecting frustum
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Intersection test between defined volume and given sphere

        Intersection test between defined volume and given sphere
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theInside : bool=None) -> bool: ...
    def OverlapsTriangle(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,theSensType : int,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given triangle. The test may be considered of interior part or boundary line defined by triangle vertices depending on given sensitivity type
        """
    def ScaleAndTransform(self,theScaleFactor : int,theTrsf : OCP.gp.gp_GTrsf,theBuilder : SelectMgr_FrustumBuilder) -> SelectMgr_SelectingVolumeManager: 
        """
        IMPORTANT: Scaling makes sense only for frustum built on a single point! Note that this method does not perform any checks on type of the frustum.
        """
    def SetCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Updates camera projection and orientation matrices in all selecting volumes Note: this method should be called after selection volume building else exception will be thrown
        """
    def SetPixelTolerance(self,theTolerance : int) -> None: 
        """
        Updates pixel tolerance in all selecting volumes Note: this method should be called after selection volume building else exception will be thrown
        """
    def SetViewClipRanges(self,theRange : SelectMgr_ViewClipRange) -> None: 
        """
        Set clipping range.
        """
    @overload
    def SetViewClipping(self,theViewPlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane,theObjPlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane,theWorldSelMgr : SelectMgr_SelectingVolumeManager) -> None: 
        """
        Valid for point selection only! Computes depth range for clipping planes.

        Copy clipping planes from another volume manager.
        """
    @overload
    def SetViewClipping(self,theOther : SelectMgr_SelectingVolumeManager) -> None: ...
    def SetViewport(self,theX : float,theY : float,theWidth : float,theHeight : float) -> None: 
        """
        Updates viewport in all selecting volumes Note: this method should be called after selection volume building else exception will be thrown
        """
    def SetWindowSize(self,theWidth : int,theHeight : int) -> None: 
        """
        Updates window size in all selecting volumes Note: this method should be called after selection volume building else exception will be thrown
        """
    def ViewClipRanges(self) -> SelectMgr_ViewClipRange: 
        """
        Return clipping range.
        """
    def ViewClipping(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Return view clipping planes.
        """
    def WindowSize(self) -> Tuple[int, int]: 
        """
        Returns window size
        """
    def __init__(self) -> None: ...
    pass
class SelectMgr_Selection(OCP.Standard.Standard_Transient):
    """
    Represents the state of a given selection mode for a Selectable Object. Contains all the sensitive entities available for this mode. An interactive object can have an indefinite number of modes of selection, each representing a "decomposition" into sensitive primitives; each primitive has an Owner (SelectMgr_EntityOwner) which allows us to identify the exact entity which has been detected. Each Selection mode is identified by an index. The set of sensitive primitives which correspond to a given mode is stocked in a SelectMgr_Selection object. By Convention, the default selection mode which allows us to grasp the Interactive object in its entirety will be mode 0. AIS_Trihedron : 4 selection modes - mode 0 : selection of a trihedron - mode 1 : selection of the origin of the trihedron - mode 2 : selection of the axes - mode 3 : selection of the planes XOY, YOZ, XOZ when you activate one of modes 1 2 3 4 , you pick AIS objects of type: - AIS_Point - AIS_Axis (and information on the type of axis) - AIS_Plane (and information on the type of plane). AIS_PlaneTrihedron offers 3 selection modes: - mode 0 : selection of the whole trihedron - mode 1 : selection of the origin of the trihedron - mode 2 : selection of the axes - same remarks as for the Trihedron. AIS_Shape : 7 maximum selection modes, depending on the complexity of the shape : - mode 0 : selection of the AIS_Shape - mode 1 : selection of the vertices - mode 2 : selection of the edges - mode 3 : selection of the wires - mode 4 : selection of the faces - mode 5 : selection of the shells - mode 6 : selection of the constituent solids.Represents the state of a given selection mode for a Selectable Object. Contains all the sensitive entities available for this mode. An interactive object can have an indefinite number of modes of selection, each representing a "decomposition" into sensitive primitives; each primitive has an Owner (SelectMgr_EntityOwner) which allows us to identify the exact entity which has been detected. Each Selection mode is identified by an index. The set of sensitive primitives which correspond to a given mode is stocked in a SelectMgr_Selection object. By Convention, the default selection mode which allows us to grasp the Interactive object in its entirety will be mode 0. AIS_Trihedron : 4 selection modes - mode 0 : selection of a trihedron - mode 1 : selection of the origin of the trihedron - mode 2 : selection of the axes - mode 3 : selection of the planes XOY, YOZ, XOZ when you activate one of modes 1 2 3 4 , you pick AIS objects of type: - AIS_Point - AIS_Axis (and information on the type of axis) - AIS_Plane (and information on the type of plane). AIS_PlaneTrihedron offers 3 selection modes: - mode 0 : selection of the whole trihedron - mode 1 : selection of the origin of the trihedron - mode 2 : selection of the axes - same remarks as for the Trihedron. AIS_Shape : 7 maximum selection modes, depending on the complexity of the shape : - mode 0 : selection of the AIS_Shape - mode 1 : selection of the vertices - mode 2 : selection of the edges - mode 3 : selection of the wires - mode 4 : selection of the faces - mode 5 : selection of the shells - mode 6 : selection of the constituent solids.
    """
    def Add(self,theSensitive : OCP.Select3D.Select3D_SensitiveEntity) -> None: 
        """
        Adds the sensitive primitive to the list of stored entities in this object. Raises NullObject if the primitive is a null handle.
        """
    def BVHUpdateStatus(self) -> SelectMgr_TypeOfBVHUpdate: 
        """
        None
        """
    def ChangeEntities(self) -> Any: 
        """
        Return entities.
        """
    def Clear(self) -> None: 
        """
        empties the selection from all the stored entities
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Entities(self) -> Any: 
        """
        Return entities.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectionState(self) -> SelectMgr_StateOfSelection: 
        """
        Returns status of selection
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEmpty(self) -> bool: 
        """
        returns true if no sensitive entity is stored.
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
    def Mode(self) -> int: 
        """
        returns the selection mode represented by this selection
        """
    def Sensitivity(self) -> int: 
        """
        Returns sensitivity of the selection
        """
    def SetSelectionState(self,theState : SelectMgr_StateOfSelection) -> None: 
        """
        Sets status of selection
        """
    def SetSensitivity(self,theNewSens : int) -> None: 
        """
        Changes sensitivity of the selection and all its entities to the given value. IMPORTANT: This method does not update any outer selection structures, so for proper updates use SelectMgr_SelectionManager::SetSelectionSensitivity method.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateBVHStatus(self,theStatus : SelectMgr_TypeOfBVHUpdate) -> None: 
        """
        None
        """
    @overload
    def UpdateStatus(self,theStatus : SelectMgr_TypeOfUpdate) -> None: 
        """
        Returns the flag UpdateFlag. This flage gives the update status of this framework in a ViewerSelector object: - full - partial, or - none.

        None
        """
    @overload
    def UpdateStatus(self) -> SelectMgr_TypeOfUpdate: ...
    def __init__(self,theModeIdx : int=0) -> None: ...
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
class SelectMgr_SelectionImageFiller(OCP.Standard.Standard_Transient):
    """
    Abstract class for filling pixel with color. This is internal tool for SelectMgr_ViewerSelector::ToPixMap().
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
        Returns a type descriptor about this object.
        """
    def Fill(self,theCol : int,theRow : int,thePicked : int) -> None: 
        """
        Fill pixel at specified position.
        """
    def Flush(self) -> None: 
        """
        Flush results into final image.
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
    def __init__(self,thePixMap : OCP.Image.Image_PixMap,theSelector : SelectMgr_ViewerSelector) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        Returns type descriptor of Standard_Transient class
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class SelectMgr_SelectionManager(OCP.Standard.Standard_Transient):
    """
    A framework to manage selection from the point of view of viewer selectors. These can be added and removed, and selection modes can be activated and deactivated. In addition, objects may be known to all selectors or only to some.A framework to manage selection from the point of view of viewer selectors. These can be added and removed, and selection modes can be activated and deactivated. In addition, objects may be known to all selectors or only to some.
    """
    def Activate(self,theObject : SelectMgr_SelectableObject,theMode : int=0) -> None: 
        """
        Activates the selection mode theMode in the selector theSelector for the selectable object anObject. By default, theMode is equal to 0. If theSelector is set to default (NULL), the selection with the mode theMode will be activated in all the viewers available.
        """
    def ClearSelectionStructures(self,theObj : SelectMgr_SelectableObject,theMode : int=-1) -> None: 
        """
        Removes sensitive entities from all viewer selectors after method Clear() was called to the selection they belonged to or it was recomputed somehow.
        """
    def Contains(self,theObject : SelectMgr_SelectableObject) -> bool: 
        """
        Returns true if the manager contains the selectable object theObject.
        """
    def Deactivate(self,theObject : SelectMgr_SelectableObject,theMode : int=-1) -> None: 
        """
        Deactivates mode theMode of theObject in theSelector. If theMode value is set to default (-1), all active selection modes will be deactivated. Likewise, if theSelector value is set to default (NULL), theMode will be deactivated in all viewer selectors.
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
    def IsActivated(self,theObject : SelectMgr_SelectableObject,theMode : int=-1) -> bool: 
        """
        Returns true if the selection with theMode is active for the selectable object theObject and selector theSelector. If all parameters are set to default values, it returns it there is any active selection in any known viewer selector for object theObject.
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
    def Load(self,theObject : SelectMgr_SelectableObject,theMode : int=-1) -> None: 
        """
        Loads and computes selection mode theMode (if it is not equal to -1) in global context and adds selectable object to BVH tree. If the object theObject has an already calculated selection with mode theMode and it was removed, the selection will be recalculated.
        """
    def RecomputeSelection(self,theObject : SelectMgr_SelectableObject,theIsForce : bool=False,theMode : int=-1) -> None: 
        """
        Recomputes activated selections of theObject for all known viewer selectors according to theMode specified. If theMode is set to default (-1), then all activated selections will be recomputed. If theIsForce is set to true, then selection mode theMode for object theObject will be recomputed regardless of its activation status.
        """
    def Remove(self,theObject : SelectMgr_SelectableObject) -> None: 
        """
        Removes selectable object theObject from all viewer selectors it was added to previously, removes it from all contexts and clears all computed selections of theObject.
        """
    def RestoreSelectionStructures(self,theObj : SelectMgr_SelectableObject,theMode : int=-1) -> None: 
        """
        Re-adds newly calculated sensitive entities of recomputed selection defined by mode theMode to all viewer selectors contained that selection.
        """
    def Selector(self) -> SelectMgr_ViewerSelector: 
        """
        Return the Selector.
        """
    def SetSelectionSensitivity(self,theObject : SelectMgr_SelectableObject,theMode : int,theNewSens : int) -> None: 
        """
        Allows to manage sensitivity of a particular selection of interactive object theObject and changes previous sensitivity value of all sensitive entities in selection with theMode to the given theNewSensitivity.
        """
    @overload
    def SetUpdateMode(self,theObject : SelectMgr_SelectableObject,theMode : int,theType : SelectMgr_TypeOfUpdate) -> None: 
        """
        Sets type of update of all selections of theObject to the given theType.

        Sets type of update of selection with theMode of theObject to the given theType.
        """
    @overload
    def SetUpdateMode(self,theObject : SelectMgr_SelectableObject,theType : SelectMgr_TypeOfUpdate) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self,theObject : SelectMgr_SelectableObject,theIsForce : bool=True) -> None: 
        """
        Updates all selections of theObject in all viewer selectors according to its current update status. If theIsForce is set to true, the call is equal to recomputation.
        """
    def UpdateSelection(self,theObj : SelectMgr_SelectableObject) -> None: 
        """
        Re-adds selectable object in BVHs in all viewer selectors.
        """
    def __init__(self,theSelector : SelectMgr_ViewerSelector) -> None: ...
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
class SelectMgr_SelectionType():
    """
    Possible selection types

    Members:

      SelectMgr_SelectionType_Unknown

      SelectMgr_SelectionType_Point

      SelectMgr_SelectionType_Box

      SelectMgr_SelectionType_Polyline
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
    SelectMgr_SelectionType_Box: OCP.SelectMgr.SelectMgr_SelectionType # value = <SelectMgr_SelectionType.SelectMgr_SelectionType_Box: 1>
    SelectMgr_SelectionType_Point: OCP.SelectMgr.SelectMgr_SelectionType # value = <SelectMgr_SelectionType.SelectMgr_SelectionType_Point: 0>
    SelectMgr_SelectionType_Polyline: OCP.SelectMgr.SelectMgr_SelectionType # value = <SelectMgr_SelectionType.SelectMgr_SelectionType_Polyline: 2>
    SelectMgr_SelectionType_Unknown: OCP.SelectMgr.SelectMgr_SelectionType # value = <SelectMgr_SelectionType.SelectMgr_SelectionType_Unknown: -1>
    __entries: dict # value = {'SelectMgr_SelectionType_Unknown': (<SelectMgr_SelectionType.SelectMgr_SelectionType_Unknown: -1>, None), 'SelectMgr_SelectionType_Point': (<SelectMgr_SelectionType.SelectMgr_SelectionType_Point: 0>, None), 'SelectMgr_SelectionType_Box': (<SelectMgr_SelectionType.SelectMgr_SelectionType_Box: 1>, None), 'SelectMgr_SelectionType_Polyline': (<SelectMgr_SelectionType.SelectMgr_SelectionType_Polyline: 2>, None)}
    __members__: dict # value = {'SelectMgr_SelectionType_Unknown': <SelectMgr_SelectionType.SelectMgr_SelectionType_Unknown: -1>, 'SelectMgr_SelectionType_Point': <SelectMgr_SelectionType.SelectMgr_SelectionType_Point: 0>, 'SelectMgr_SelectionType_Box': <SelectMgr_SelectionType.SelectMgr_SelectionType_Box: 1>, 'SelectMgr_SelectionType_Polyline': <SelectMgr_SelectionType.SelectMgr_SelectionType_Polyline: 2>}
    pass
class SelectMgr_SensitiveEntity(OCP.Standard.Standard_Transient):
    """
    The purpose of this class is to mark sensitive entities selectable or not depending on current active selection of parent object for proper BVH traverseThe purpose of this class is to mark sensitive entities selectable or not depending on current active selection of parent object for proper BVH traverse
    """
    def BaseSensitive(self) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        Returns related instance of SelectBasics class
        """
    def Clear(self) -> None: 
        """
        Clears up all resources and memory
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
    def IsActiveForSelection(self) -> bool: 
        """
        Returns true if this entity belongs to the active selection mode of parent object
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
    def ResetSelectionActiveStatus(self) -> None: 
        """
        Marks entity as inactive for selection
        """
    def SetActiveForSelection(self) -> None: 
        """
        Marks entity as active for selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theEntity : OCP.Select3D.Select3D_SensitiveEntity) -> None: ...
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
class SelectMgr_SensitiveEntitySet():
    """
    This class is used to store all calculated sensitive entities of one selectable object. It provides an interface for building BVH tree which is used to speed-up the performance of searching for overlap among sensitives of one selectable object
    """
    @overload
    def Append(self,theSelection : SelectMgr_Selection) -> None: 
        """
        Adds new entity to the set and marks BVH tree for rebuild

        Adds every entity of selection theSelection to the set and marks BVH tree for rebuild
        """
    @overload
    def Append(self,theEntity : SelectMgr_SensitiveEntity) -> None: ...
    def Box(self,theIndex : int) -> Any: 
        """
        Returns bounding box of entity with index theIdx
        """
    def Center(self,theIndex : int,theAxis : int) -> float: 
        """
        Returns geometry center of sensitive entity index theIdx along the given axis theAxis
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetSensitiveById(self,theIndex : int) -> SelectMgr_SensitiveEntity: 
        """
        Returns the entity with index theIndex in the set
        """
    def HasEntityWithPersistence(self) -> bool: 
        """
        Returns map of entities.
        """
    def Owners(self) -> SelectMgr_MapOfOwners: 
        """
        Returns map of owners.
        """
    def Remove(self,theSelection : SelectMgr_Selection) -> None: 
        """
        Removes every entity of selection theSelection from the set and marks BVH tree for rebuild
        """
    def Sensitives(self) -> Any: 
        """
        Returns map of entities.
        """
    def Size(self) -> int: 
        """
        Returns the amount of entities
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps items with indexes theIdx1 and theIdx2
        """
    def __init__(self,theBuilder : OCP.Select3D.Select3D_BVHBuilder3d) -> None: ...
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
class SelectMgr_SequenceOfOwner(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : SelectMgr_SequenceOfOwner) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : SelectMgr_EntityOwner) -> None: ...
    def Assign(self,theOther : SelectMgr_SequenceOfOwner) -> SelectMgr_SequenceOfOwner: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> SelectMgr_EntityOwner: 
        """
        First item access
        """
    def ChangeLast(self) -> SelectMgr_EntityOwner: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> SelectMgr_EntityOwner: 
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
    def First(self) -> SelectMgr_EntityOwner: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : SelectMgr_SequenceOfOwner) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : SelectMgr_EntityOwner) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : SelectMgr_EntityOwner) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : SelectMgr_SequenceOfOwner) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> SelectMgr_EntityOwner: 
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
    def Prepend(self,theItem : SelectMgr_EntityOwner) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : SelectMgr_SequenceOfOwner) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : SelectMgr_EntityOwner) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : SelectMgr_SequenceOfOwner) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> SelectMgr_EntityOwner: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : SelectMgr_SequenceOfOwner) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class SelectMgr_SequenceOfSelection(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : SelectMgr_Selection) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : SelectMgr_SequenceOfSelection) -> None: ...
    def Assign(self,theOther : SelectMgr_SequenceOfSelection) -> SelectMgr_SequenceOfSelection: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> SelectMgr_Selection: 
        """
        First item access
        """
    def ChangeLast(self) -> SelectMgr_Selection: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> SelectMgr_Selection: 
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
    def First(self) -> SelectMgr_Selection: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : SelectMgr_SequenceOfSelection) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : SelectMgr_Selection) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : SelectMgr_SequenceOfSelection) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : SelectMgr_Selection) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> SelectMgr_Selection: 
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
    def Prepend(self,theSeq : SelectMgr_SequenceOfSelection) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : SelectMgr_Selection) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : SelectMgr_Selection) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : SelectMgr_SequenceOfSelection) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> SelectMgr_Selection: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : SelectMgr_SequenceOfSelection) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class SelectMgr_SortCriterion():
    """
    This class provides data and criterion for sorting candidate entities in the process of interactive selection by mouse click
    """
    def IsCloserDepth(self,theOther : SelectMgr_SortCriterion) -> bool: 
        """
        Compare with another item by depth, priority and minDist.
        """
    def IsHigherPriority(self,theOther : SelectMgr_SortCriterion) -> bool: 
        """
        Compare with another item using old logic (OCCT version <= 6.3.1) with priority considered preceding depth.
        """
    def __init__(self) -> None: ...
    @property
    def Depth(self) -> float:
        """
        :type: float
        """
    @Depth.setter
    def Depth(self, arg0: float) -> None:
        pass
    @property
    def MinDist(self) -> float:
        """
        :type: float
        """
    @MinDist.setter
    def MinDist(self, arg0: float) -> None:
        pass
    @property
    def NbOwnerMatches(self) -> int:
        """
        :type: int
        """
    @NbOwnerMatches.setter
    def NbOwnerMatches(self, arg0: int) -> None:
        pass
    @property
    def Normal(self) -> OCP.gp.gp_Vec3f:
        """
        :type: OCP.gp.gp_Vec3f
        """
    @Normal.setter
    def Normal(self, arg0: OCP.gp.gp_Vec3f) -> None:
        pass
    @property
    def Point(self) -> OCP.gp.gp_Pnt:
        """
        :type: OCP.gp.gp_Pnt
        """
    @Point.setter
    def Point(self, arg0: OCP.gp.gp_Pnt) -> None:
        pass
    @property
    def Priority(self) -> int:
        """
        :type: int
        """
    @Priority.setter
    def Priority(self, arg0: int) -> None:
        pass
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg0: float) -> None:
        pass
    @property
    def ZLayerPosition(self) -> int:
        """
        :type: int
        """
    @ZLayerPosition.setter
    def ZLayerPosition(self, arg0: int) -> None:
        pass
    pass
class SelectMgr_StateOfSelection():
    """
    different state of a Selection in a ViewerSelector...

    Members:

      SelectMgr_SOS_Any

      SelectMgr_SOS_Unknown

      SelectMgr_SOS_Deactivated

      SelectMgr_SOS_Activated
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
    SelectMgr_SOS_Activated: OCP.SelectMgr.SelectMgr_StateOfSelection # value = <SelectMgr_StateOfSelection.SelectMgr_SOS_Activated: 1>
    SelectMgr_SOS_Any: OCP.SelectMgr.SelectMgr_StateOfSelection # value = <SelectMgr_StateOfSelection.SelectMgr_SOS_Any: -2>
    SelectMgr_SOS_Deactivated: OCP.SelectMgr.SelectMgr_StateOfSelection # value = <SelectMgr_StateOfSelection.SelectMgr_SOS_Deactivated: 0>
    SelectMgr_SOS_Unknown: OCP.SelectMgr.SelectMgr_StateOfSelection # value = <SelectMgr_StateOfSelection.SelectMgr_SOS_Unknown: -1>
    __entries: dict # value = {'SelectMgr_SOS_Any': (<SelectMgr_StateOfSelection.SelectMgr_SOS_Any: -2>, None), 'SelectMgr_SOS_Unknown': (<SelectMgr_StateOfSelection.SelectMgr_SOS_Unknown: -1>, None), 'SelectMgr_SOS_Deactivated': (<SelectMgr_StateOfSelection.SelectMgr_SOS_Deactivated: 0>, None), 'SelectMgr_SOS_Activated': (<SelectMgr_StateOfSelection.SelectMgr_SOS_Activated: 1>, None)}
    __members__: dict # value = {'SelectMgr_SOS_Any': <SelectMgr_StateOfSelection.SelectMgr_SOS_Any: -2>, 'SelectMgr_SOS_Unknown': <SelectMgr_StateOfSelection.SelectMgr_SOS_Unknown: -1>, 'SelectMgr_SOS_Deactivated': <SelectMgr_StateOfSelection.SelectMgr_SOS_Deactivated: 0>, 'SelectMgr_SOS_Activated': <SelectMgr_StateOfSelection.SelectMgr_SOS_Activated: 1>}
    pass
class SelectMgr_ToleranceMap():
    """
    An internal class for calculation of current largest tolerance value which will be applied for creation of selecting frustum by default. Each time the selection set is deactivated, maximum tolerance value will be recalculated. If a user enables custom precision using StdSelect_ViewerSelector3d::SetPixelTolerance, it will be applied to all sensitive entities without any checks.
    """
    def Add(self,theTolerance : int) -> None: 
        """
        Adds the value given to map, checks if the current tolerance value should be replaced by theTolerance
        """
    def CustomTolerance(self) -> int: 
        """
        Returns the value of custom tolerance regardless of it validity
        """
    def Decrement(self,theTolerance : int) -> None: 
        """
        Decrements a counter of the tolerance given, checks if the current tolerance value should be recalculated
        """
    def IsCustomTolSet(self) -> bool: 
        """
        Returns true if custom tolerance value is greater than zero
        """
    def ResetDefaults(self) -> None: 
        """
        Unsets a custom tolerance and enables adaptive checks
        """
    def SetCustomTolerance(self,theTolerance : int) -> None: 
        """
        Sets tolerance to the given one and disables adaptive checks
        """
    def Tolerance(self) -> int: 
        """
        Returns a current tolerance that must be applied
        """
    def __init__(self) -> None: ...
    pass
class SelectMgr_TriangFrustums(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : SelectMgr_TriangularFrustum) -> SelectMgr_TriangularFrustum: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : SelectMgr_TriangularFrustum,theIter : Any) -> None: ...
    @overload
    def Append(self,theOther : SelectMgr_TriangFrustums) -> None: ...
    def Assign(self,theOther : SelectMgr_TriangFrustums) -> SelectMgr_TriangFrustums: 
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
    def First(self) -> SelectMgr_TriangularFrustum: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : SelectMgr_TriangFrustums,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : SelectMgr_TriangularFrustum,theIter : Any) -> SelectMgr_TriangularFrustum: ...
    @overload
    def InsertBefore(self,theItem : SelectMgr_TriangularFrustum,theIter : Any) -> SelectMgr_TriangularFrustum: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : SelectMgr_TriangFrustums,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> SelectMgr_TriangularFrustum: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : SelectMgr_TriangFrustums) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : SelectMgr_TriangularFrustum) -> SelectMgr_TriangularFrustum: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : SelectMgr_TriangFrustums) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class SelectMgr_TriangularFrustum():
    """
    This class contains representation of triangular selecting frustum, created in case of polyline selection, and algorithms for overlap detection between selecting frustum and sensitive entities. Overlap detection tests are implemented according to the terms of separating axis theorem (SAT). NOTE: the object of this class can be created only as part of SelectMgr_TriangularFrustumSet.
    """
    def Build(self) -> None: 
        """
        Creates new triangular frustum with bases of triangles with vertices theP1, theP2 and theP3 projections onto near and far view frustum planes (only for triangular frustums) NOTE: it should be called after Init() method
        """
    def Clear(self) -> None: 
        """
        Nullifies the handle to corresponding builder instance to prevent memory leaks
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetPlanes(self,thePlaneEquations : Any) -> None: 
        """
        Stores plane equation coefficients (in the following form: Ax + By + Cz + D = 0) to the given vector
        """
    def Init(self,theP1 : OCP.gp.gp_Pnt2d,theP2 : OCP.gp.gp_Pnt2d,theP3 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Initializes selection triangle by input points
        """
    def IsScalable(self) -> bool: 
        """
        Returns FALSE (not applicable to this volume).
        """
    @overload
    def OverlapsBox(self,theMinPt : SelectMgr_Vec3,theMaxPt : SelectMgr_Vec3,theInside : bool) -> bool: 
        """
        SAT intersection test between defined volume and given axis-aligned box

        Returns true if selecting volume is overlapped by axis-aligned bounding box with minimum corner at point theMinPt and maximum at point theMaxPt
        """
    @overload
    def OverlapsBox(self,theMinPnt : SelectMgr_Vec3,theMaxPnt : SelectMgr_Vec3,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCircle(self,theRadius : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().

        Returns true if selecting volume is overlapped by circle with radius theRadius, boolean theIsFilled and transformation to apply theTrsf. The position and orientation of the circle are specified via theTrsf transformation for gp::XOY() with center in gp::Origin().
        """
    @overload
    def OverlapsCircle(self,theRadius : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.

        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsPoint(self,arg1 : OCP.gp.gp_Pnt) -> bool: 
        """
        Intersection test between defined volume and given point

        Always returns FALSE (not applicable to this selector).
        """
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    def OverlapsPolygon(self,theArrayOfPnts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given ordered set of points, representing line segments. The test may be considered of interior part or boundary line defined by segments depending on given sensitivity type
        """
    def OverlapsSegment(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Checks if line segment overlaps selecting frustum
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius

        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    def OverlapsTriangle(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        SAT intersection test between defined volume and given triangle. The test may be considered of interior part or boundary line defined by triangle vertices depending on given sensitivity type
        """
    def ScaleAndTransform(self,theScale : int,theTrsf : OCP.gp.gp_GTrsf,theBuilder : SelectMgr_FrustumBuilder) -> SelectMgr_BaseIntersector: 
        """
        Returns a copy of the frustum transformed according to the matrix given
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
class SelectMgr_TriangularFrustumSet(SelectMgr_BaseFrustum, SelectMgr_BaseIntersector, OCP.Standard.Standard_Transient):
    """
    This class is used to handle polyline selection. The main principle of polyline selection algorithm is to split the polygon defined by polyline onto triangles. Than each of them is considered as a base for triangular frustum building. In other words, each triangle vertex will be projected from 2d screen space to 3d world space onto near and far view frustum planes. Thus, the projected triangles make up the bases of selecting frustum. When the set of such frustums is created, the function determining selection iterates through triangular frustum set and searches for overlap with any frustum.
    """
    def Build(self) -> None: 
        """
        Meshes polygon bounded by polyline. Than organizes a set of triangular frustums, where each triangle's projection onto near and far view frustum planes is considered as a frustum base NOTE: it should be called after Init() method
        """
    def Camera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Return camera definition.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DetectedPoint(self,theDepth : float) -> OCP.gp.gp_Pnt: 
        """
        Calculates the point on a view ray that was detected during the run of selection algo by given depth
        """
    def DistToGeometryCenter(self,theCOG : OCP.gp.gp_Pnt) -> float: 
        """
        Measures distance between 3d projection of user-picked screen point and given point theCOG. It makes sense only for intersectors built on a single point. This method returns infinite value for the base class.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetFarPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns far point of intersector. This method returns zero point for the base class.
        """
    def GetMousePosition(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns current mouse coordinates. This method returns infinite point for the base class.
        """
    def GetNearPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns near point of intersector. This method returns zero point for the base class.
        """
    def GetPlanes(self,thePlaneEquations : Any) -> None: 
        """
        Stores plane equation coefficients (in the following form: Ax + By + Cz + D = 0) to the given vector
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectionType(self) -> SelectMgr_SelectionType: 
        """
        Returns selection type of this intersector
        """
    def GetViewRayDirection(self) -> OCP.gp.gp_Dir: 
        """
        Returns direction ray of intersector. This method returns zero direction for the base class.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,thePoints : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: 
        """
        Initializes set of triangular frustums by polyline
        """
    def IsBoundaryIntersectSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,thePlaneNormal : OCP.gp.gp_Dir,theBoundaries : OCP.TColgp.TColgp_Array1OfPnt,theBoundaryInside : bool) -> bool: 
        """
        Checks whether the boundary of the current volume selection intersects with a sphere or are there it's boundaries lying inside the sphere
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
    def IsScalable(self) -> bool: 
        """
        Returns FALSE (not applicable to this volume).
        """
    @overload
    def OverlapsBox(self,theMinPnt : SelectMgr_Vec3,theMaxPnt : SelectMgr_Vec3,theInside : bool) -> bool: 
        """
        None

        None
        """
    @overload
    def OverlapsBox(self,theMinPnt : SelectMgr_Vec3,theMaxPnt : SelectMgr_Vec3,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.

        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """
    @overload
    def OverlapsCircle(self,theBottomRad : float,theTrsf : OCP.gp.gp_Trsf,theIsFilled : bool,theInside : bool=None) -> bool: ...
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theInside : bool=None) -> bool: 
        """
        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.

        Returns true if selecting volume is overlapped by cylinder (or cone) with radiuses theBottomRad and theTopRad, height theHeight and transformation to apply theTrsf.
        """
    @overload
    def OverlapsCylinder(self,theBottomRad : float,theTopRad : float,theHeight : float,theTrsf : OCP.gp.gp_Trsf,theIsHollow : bool,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsPoint(self,arg1 : OCP.gp.gp_Pnt) -> bool: 
        """
        None

        Always returns FALSE (not applicable to this selector).
        """
    @overload
    def OverlapsPoint(self,thePnt : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: ...
    def OverlapsPolygon(self,theArrayOfPnts : OCP.TColgp.TColgp_Array1OfPnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        None
        """
    def OverlapsSegment(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        None
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius

        Returns true if selecting volume is overlapped by sphere with center theCenter and radius theRadius
        """
    @overload
    def OverlapsSphere(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theInside : bool=None) -> bool: ...
    def OverlapsTriangle(self,thePnt1 : OCP.gp.gp_Pnt,thePnt2 : OCP.gp.gp_Pnt,thePnt3 : OCP.gp.gp_Pnt,theSensType : OCP.Select3D.Select3D_TypeOfSensitivity,theClipRange : SelectMgr_ViewClipRange,thePickResult : OCP.SelectBasics.SelectBasics_PickResult) -> bool: 
        """
        None
        """
    def RayCircleIntersection(self,theRadius : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theIsFilled : bool,theTime : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the circle
        """
    def RayCylinderIntersection(self,theBottomRadius : float,theTopRadius : float,theHeight : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theIsHollow : bool,theTimeEnter : float,theTimeLeave : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the hollow cylinder (or cone)
        """
    def RaySphereIntersection(self,theCenter : OCP.gp.gp_Pnt,theRadius : float,theLoc : OCP.gp.gp_Pnt,theRayDir : OCP.gp.gp_Dir,theTimeEnter : float,theTimeLeave : float) -> bool: 
        """
        Checks whether the ray that starts at the point theLoc and directs with the direction theRayDir intersects with the sphere with center at theCenter and radius TheRadius
        """
    def ScaleAndTransform(self,theScale : int,theTrsf : OCP.gp.gp_GTrsf,theBuilder : SelectMgr_FrustumBuilder) -> SelectMgr_BaseIntersector: 
        """
        Returns a copy of the frustum with all sub-volumes transformed according to the matrix given
        """
    def SetAllowOverlapDetection(self,theIsToAllow : bool) -> None: 
        """
        If theIsToAllow is false, only fully included sensitives will be detected, otherwise the algorithm will mark both included and overlapped entities as matched
        """
    def SetBuilder(self,theBuilder : SelectMgr_FrustumBuilder) -> None: 
        """
        Nullifies the builder created in the constructor and copies the pointer given
        """
    def SetCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Saves camera definition and passes it to builder
        """
    def SetPixelTolerance(self,theTol : int) -> None: 
        """
        None
        """
    def SetViewport(self,theX : float,theY : float,theWidth : float,theHeight : float) -> None: 
        """
        Passes viewport parameters to builder
        """
    def SetWindowSize(self,theWidth : int,theHeight : int) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WindowSize(self) -> Tuple[int, int]: 
        """
        None
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
class SelectMgr_TypeOfBVHUpdate():
    """
    Keeps track for BVH update state for each SelectMgr_Selection entity in a following way: - Add : 2nd level BVH does not contain any of the selection's sensitive entities and they must be added; - Remove : all sensitive entities of the selection must be removed from 2nd level BVH; - Renew : 2nd level BVH already contains sensitives of the selection, but the its complete update and removal is required. Therefore, sensitives of the selection with this type of update must be removed from 2nd level BVH and added after recomputation. - Invalidate : the 2nd level BVH needs to be rebuilt; - None : entities of the selection are up to date.

    Members:

      SelectMgr_TBU_Add

      SelectMgr_TBU_Remove

      SelectMgr_TBU_Renew

      SelectMgr_TBU_Invalidate

      SelectMgr_TBU_None
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
    SelectMgr_TBU_Add: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Add: 0>
    SelectMgr_TBU_Invalidate: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Invalidate: 3>
    SelectMgr_TBU_None: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_None: 4>
    SelectMgr_TBU_Remove: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Remove: 1>
    SelectMgr_TBU_Renew: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Renew: 2>
    __entries: dict # value = {'SelectMgr_TBU_Add': (<SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Add: 0>, None), 'SelectMgr_TBU_Remove': (<SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Remove: 1>, None), 'SelectMgr_TBU_Renew': (<SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Renew: 2>, None), 'SelectMgr_TBU_Invalidate': (<SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Invalidate: 3>, None), 'SelectMgr_TBU_None': (<SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_None: 4>, None)}
    __members__: dict # value = {'SelectMgr_TBU_Add': <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Add: 0>, 'SelectMgr_TBU_Remove': <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Remove: 1>, 'SelectMgr_TBU_Renew': <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Renew: 2>, 'SelectMgr_TBU_Invalidate': <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Invalidate: 3>, 'SelectMgr_TBU_None': <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_None: 4>}
    pass
class SelectMgr_TypeOfDepthTolerance():
    """
    Define the type of depth tolerance for considering picked entities to lie on the same depth (distance from eye to entity).

    Members:

      SelectMgr_TypeOfDepthTolerance_Uniform

      SelectMgr_TypeOfDepthTolerance_UniformPixels

      SelectMgr_TypeOfDepthTolerance_SensitivityFactor
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
    SelectMgr_TypeOfDepthTolerance_SensitivityFactor: OCP.SelectMgr.SelectMgr_TypeOfDepthTolerance # value = <SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_SensitivityFactor: 2>
    SelectMgr_TypeOfDepthTolerance_Uniform: OCP.SelectMgr.SelectMgr_TypeOfDepthTolerance # value = <SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_Uniform: 0>
    SelectMgr_TypeOfDepthTolerance_UniformPixels: OCP.SelectMgr.SelectMgr_TypeOfDepthTolerance # value = <SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_UniformPixels: 1>
    __entries: dict # value = {'SelectMgr_TypeOfDepthTolerance_Uniform': (<SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_Uniform: 0>, None), 'SelectMgr_TypeOfDepthTolerance_UniformPixels': (<SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_UniformPixels: 1>, None), 'SelectMgr_TypeOfDepthTolerance_SensitivityFactor': (<SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_SensitivityFactor: 2>, None)}
    __members__: dict # value = {'SelectMgr_TypeOfDepthTolerance_Uniform': <SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_Uniform: 0>, 'SelectMgr_TypeOfDepthTolerance_UniformPixels': <SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_UniformPixels: 1>, 'SelectMgr_TypeOfDepthTolerance_SensitivityFactor': <SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_SensitivityFactor: 2>}
    pass
class SelectMgr_TypeOfUpdate():
    """
    Provides values for types of update, including - full - partial - none.

    Members:

      SelectMgr_TOU_Full

      SelectMgr_TOU_Partial

      SelectMgr_TOU_None
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
    SelectMgr_TOU_Full: OCP.SelectMgr.SelectMgr_TypeOfUpdate # value = <SelectMgr_TypeOfUpdate.SelectMgr_TOU_Full: 0>
    SelectMgr_TOU_None: OCP.SelectMgr.SelectMgr_TypeOfUpdate # value = <SelectMgr_TypeOfUpdate.SelectMgr_TOU_None: 2>
    SelectMgr_TOU_Partial: OCP.SelectMgr.SelectMgr_TypeOfUpdate # value = <SelectMgr_TypeOfUpdate.SelectMgr_TOU_Partial: 1>
    __entries: dict # value = {'SelectMgr_TOU_Full': (<SelectMgr_TypeOfUpdate.SelectMgr_TOU_Full: 0>, None), 'SelectMgr_TOU_Partial': (<SelectMgr_TypeOfUpdate.SelectMgr_TOU_Partial: 1>, None), 'SelectMgr_TOU_None': (<SelectMgr_TypeOfUpdate.SelectMgr_TOU_None: 2>, None)}
    __members__: dict # value = {'SelectMgr_TOU_Full': <SelectMgr_TypeOfUpdate.SelectMgr_TOU_Full: 0>, 'SelectMgr_TOU_Partial': <SelectMgr_TypeOfUpdate.SelectMgr_TOU_Partial: 1>, 'SelectMgr_TOU_None': <SelectMgr_TypeOfUpdate.SelectMgr_TOU_None: 2>}
    pass
class SelectMgr_Vec3():
    """
    Generic 3-components vector. To be used as RGB color pixel or XYZ 3D-point. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> float: 
        """
        None
        """
    @staticmethod
    def Cross_s(theVec1 : SelectMgr_Vec3,theVec2 : SelectMgr_Vec3) -> SelectMgr_Vec3: 
        """
        Computes the cross product.
        """
    @staticmethod
    def DX_s() -> SelectMgr_Vec3: 
        """
        Construct DX unit vector.
        """
    @staticmethod
    def DY_s() -> SelectMgr_Vec3: 
        """
        Construct DY unit vector.
        """
    @staticmethod
    def DZ_s() -> SelectMgr_Vec3: 
        """
        Construct DZ unit vector.
        """
    def Dot(self,theOther : SelectMgr_Vec3) -> float: 
        """
        Computes the dot product.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetData(self) -> float: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    @staticmethod
    def GetLERP_s(theFrom : SelectMgr_Vec3,theTo : SelectMgr_Vec3,theT : float) -> SelectMgr_Vec3: 
        """
        Compute linear interpolation between to vectors.
        """
    def IsEqual(self,theOther : SelectMgr_Vec3) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> float: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : float) -> SelectMgr_Vec3: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : float) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Normalize(self) -> None: 
        """
        Normalize the vector.
        """
    def Normalized(self) -> SelectMgr_Vec3: 
        """
        Normalize the vector.
        """
    @overload
    def SetValues(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Assign new values to the vector.

        Assign new values to the vector.
        """
    @overload
    def SetValues(self,theVec2 : OCP.Graphic3d.Graphic3d_Vec2d,theZ : float) -> None: ...
    def SquareModulus(self) -> float: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : SelectMgr_Vec3) -> SelectMgr_Vec3: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theFactor : float) -> SelectMgr_Vec3: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theRight : SelectMgr_Vec3) -> SelectMgr_Vec3: ...
    @overload
    def __init__(self,theX : float,theY : float,theZ : float) -> None: ...
    @overload
    def __init__(self,theVec2 : OCP.Graphic3d.Graphic3d_Vec2d,theZ : float=0.0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theValue : float) -> None: ...
    def __isub__(self,theDec : SelectMgr_Vec3) -> SelectMgr_Vec3: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theInvFactor : float) -> SelectMgr_Vec3: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theRight : SelectMgr_Vec3) -> SelectMgr_Vec3: ...
    def __mul__(self,theFactor : float) -> SelectMgr_Vec3: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : float) -> SelectMgr_Vec3: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> SelectMgr_Vec3: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : float) -> SelectMgr_Vec3: 
        """
        Compute per-component division by scale factor.
        """
    def b(self) -> float: 
        """
        Alias to 3rd component as BLUE channel in RGB.

        Alias to 3rd component as BLUE channel in RGB.
        """
    def cwiseAbs(self) -> SelectMgr_Vec3: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : SelectMgr_Vec3) -> SelectMgr_Vec3: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : SelectMgr_Vec3) -> SelectMgr_Vec3: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> float: 
        """
        Alias to 2nd component as GREEN channel in RGB.

        Alias to 2nd component as GREEN channel in RGB.
        """
    def maxComp(self) -> float: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> float: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> float: 
        """
        Alias to 1st component as RED channel in RGB.

        Alias to 1st component as RED channel in RGB.
        """
    def x(self) -> float: 
        """
        Alias to 1st component as X coordinate in XYZ.

        Alias to 1st component as X coordinate in XYZ.
        """
    def xy(self) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        None
        """
    def xyz(self) -> SelectMgr_Vec3: 
        """
        None
        """
    def xz(self) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        None
        """
    def xzy(self) -> SelectMgr_Vec3: 
        """
        None
        """
    def y(self) -> float: 
        """
        Alias to 2nd component as Y coordinate in XYZ.

        Alias to 2nd component as Y coordinate in XYZ.
        """
    def yx(self) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        None
        """
    def yxz(self) -> SelectMgr_Vec3: 
        """
        None
        """
    def yz(self) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        None
        """
    def yzx(self) -> SelectMgr_Vec3: 
        """
        None
        """
    def z(self) -> float: 
        """
        Alias to 3rd component as Z coordinate in XYZ.

        Alias to 3rd component as Z coordinate in XYZ.
        """
    def zx(self) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        None
        """
    def zxy(self) -> SelectMgr_Vec3: 
        """
        None
        """
    def zy(self) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        None
        """
    def zyx(self) -> SelectMgr_Vec3: 
        """
        None
        """
    pass
class SelectMgr_ViewClipRange():
    """
    Class for handling depth clipping range. It is used to perform checks in case if global (for the whole view) clipping planes are defined inside of SelectMgr_RectangularFrustum class methods.
    """
    def AddClipSubRange(self,theRange : OCP.Bnd.Bnd_Range) -> None: 
        """
        Adds a clipping sub-range (for clipping chains).
        """
    def AddClippingPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane,thePickRay : OCP.gp.gp_Ax1) -> None: 
        """
        Add clipping planes. Planes and picking ray should be defined in the same coordinate system.
        """
    def ChangeUnclipRange(self) -> OCP.Bnd.Bnd_Range: 
        """
        Returns the main unclipped range; [-inf, inf] by default.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetNearestDepth(self,theRange : OCP.Bnd.Bnd_Range,theDepth : float) -> bool: 
        """
        Calculates the min not clipped value from the range. Returns FALSE if the whole range is clipped.
        """
    def IsClipped(self,theDepth : float) -> bool: 
        """
        Check if the given depth is not within clipping range(s), e.g. TRUE means depth is clipped.
        """
    def SetVoid(self) -> None: 
        """
        Clears clipping range.
        """
    def __init__(self) -> None: ...
    pass
class SelectMgr_ViewerSelector(OCP.Standard.Standard_Transient):
    """
    A framework to define finding, sorting the sensitive primitives in a view. Services are also provided to define the return of the owners of those primitives selected. The primitives are sorted by criteria such as priority of the primitive or its depth in the view relative to that of other primitives. Note that in 3D, the inheriting framework StdSelect_ViewerSelector3d is only to be used if you do not want to use the services provided by AIS. Two tools are available to find and select objects found at a given position in the view. If you want to select the owners of all the objects detected at point x,y,z you use the Init - More - Next - Picked loop. If, on the other hand, you want to select only one object detected at that point, you use the Init - More - OnePicked loop. In this iteration, More is used to see if an object was picked and OnePicked, to get the object closest to the pick position. Viewer selectors are driven by SelectMgr_SelectionManager, and manipulate the SelectMgr_Selection objects given to them by the selection manager.A framework to define finding, sorting the sensitive primitives in a view. Services are also provided to define the return of the owners of those primitives selected. The primitives are sorted by criteria such as priority of the primitive or its depth in the view relative to that of other primitives. Note that in 3D, the inheriting framework StdSelect_ViewerSelector3d is only to be used if you do not want to use the services provided by AIS. Two tools are available to find and select objects found at a given position in the view. If you want to select the owners of all the objects detected at point x,y,z you use the Init - More - Next - Picked loop. If, on the other hand, you want to select only one object detected at that point, you use the Init - More - OnePicked loop. In this iteration, More is used to see if an object was picked and OnePicked, to get the object closest to the pick position. Viewer selectors are driven by SelectMgr_SelectionManager, and manipulate the SelectMgr_Selection objects given to them by the selection manager.
    """
    def ActiveOwners(self,theOwners : OCP.AIS.AIS_NListOfEntityOwner) -> None: 
        """
        Returns the list of active entity owners
        """
    def AddSelectableObject(self,theObject : SelectMgr_SelectableObject) -> None: 
        """
        Adds new object to the map of selectable objects
        """
    def AddSelectionToObject(self,theObject : SelectMgr_SelectableObject,theSelection : SelectMgr_Selection) -> None: 
        """
        Adds new selection to the object and builds its BVH tree
        """
    def AllowOverlapDetection(self,theIsToAllow : bool) -> None: 
        """
        Is used for rectangular selection only If theIsToAllow is false, only fully included sensitives will be detected, otherwise the algorithm will mark both included and overlapped entities as matched
        """
    def Clear(self) -> None: 
        """
        Empties all the tables, removes all selections...
        """
    def ClearPicked(self) -> None: 
        """
        Clears picking results.
        """
    def ClearSensitive(self,theView : OCP.V3d.V3d_View) -> None: 
        """
        None
        """
    def Contains(self,theObject : SelectMgr_SelectableObject) -> bool: 
        """
        None
        """
    def CustomPixelTolerance(self) -> int: 
        """
        Returns custom pixel tolerance value.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DepthTolerance(self) -> float: 
        """
        Return the tolerance for considering two entities having a similar depth (distance from eye to entity).
        """
    def DepthToleranceType(self) -> SelectMgr_TypeOfDepthTolerance: 
        """
        Return the type of tolerance for considering two entities having a similar depth (distance from eye to entity); SelectMgr_TypeOfDepthTolerance_SensitivityFactor by default.
        """
    @overload
    def DisplaySensitive(self,theSel : SelectMgr_Selection,theTrsf : OCP.gp.gp_Trsf,theView : OCP.V3d.V3d_View,theToClearOthers : bool=True) -> None: 
        """
        Displays sensitives in view <theView>.

        None
        """
    @overload
    def DisplaySensitive(self,theView : OCP.V3d.V3d_View) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EntitySetBuilder(self) -> OCP.Select3D.Select3D_BVHBuilder3d: 
        """
        Returns the default builder used to construct BVH of entity set.
        """
    def GetManager(self) -> SelectMgr_SelectingVolumeManager: 
        """
        Returns instance of selecting volume manager of the viewer selector
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsActive(self,theSelectableObject : SelectMgr_SelectableObject,theMode : int) -> bool: 
        """
        Returns true if the selectable object aSelectableObject having the selection mode aMode is active in this selector.
        """
    def IsInside(self,theSelectableObject : SelectMgr_SelectableObject,theMode : int) -> bool: 
        """
        Returns true if the selectable object aSelectableObject having the selection mode aMode is in this selector.
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
    def Modes(self,theSelectableObject : SelectMgr_SelectableObject,theModeList : OCP.TColStd.TColStd_ListOfInteger,theWantedState : SelectMgr_StateOfSelection=SelectMgr_StateOfSelection.SelectMgr_SOS_Any) -> bool: 
        """
        Returns the list of selection modes ModeList found in this selector for the selectable object aSelectableObject. Returns true if aSelectableObject is referenced inside this selector; returns false if the object is not present in this selector.
        """
    def MoveSelectableObject(self,theObject : SelectMgr_SelectableObject) -> None: 
        """
        Moves existing object from set of not transform persistence objects to set of transform persistence objects (or vice versa).
        """
    def NbPicked(self) -> int: 
        """
        Returns the number of detected owners.
        """
    def OnePicked(self) -> SelectMgr_EntityOwner: 
        """
        Returns the picked element with the highest priority, and which is the closest to the last successful mouse position.
        """
    @overload
    def Pick(self,thePolyline : OCP.TColgp.TColgp_Array1OfPnt2d,theView : OCP.V3d.V3d_View) -> None: 
        """
        Picks the sensitive entity at the pixel coordinates of the mouse <theXPix> and <theYPix>. The selector looks for touched areas and owners.

        Picks the sensitive entity according to the minimum and maximum pixel values <theXPMin>, <theYPMin>, <theXPMax> and <theYPMax> defining a 2D area for selection in the 3D view aView.

        pick action - input pixel values for polyline selection for selection.

        Picks the sensitive entity according to the input axis. This is geometric intersection 3D objects by axis (camera parameters are ignored and objects with transform persistance are skipped).
        """
    @overload
    def Pick(self,theXPMin : int,theYPMin : int,theXPMax : int,theYPMax : int,theView : OCP.V3d.V3d_View) -> None: ...
    @overload
    def Pick(self,theXPix : int,theYPix : int,theView : OCP.V3d.V3d_View) -> None: ...
    @overload
    def Pick(self,theAxis : OCP.gp.gp_Ax1,theView : OCP.V3d.V3d_View) -> None: ...
    def Picked(self,theRank : int) -> SelectMgr_EntityOwner: 
        """
        Returns the entity Owner for the object picked at specified position.
        """
    def PickedData(self,theRank : int) -> SelectMgr_SortCriterion: 
        """
        Returns the Entity for the object picked at specified position.
        """
    def PickedEntity(self,theRank : int) -> OCP.Select3D.Select3D_SensitiveEntity: 
        """
        Returns the Entity for the object picked at specified position.
        """
    def PickedPoint(self,theRank : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the 3D point (intersection of picking axis with the object nearest to eye) for the object picked at specified position.
        """
    def PixelTolerance(self) -> int: 
        """
        Returns the largest pixel tolerance.
        """
    def QueueBVHBuild(self,theEntity : OCP.Select3D.Select3D_SensitiveEntity) -> None: 
        """
        Queues a sensitive entity to build its BVH
        """
    def RebuildObjectsTree(self,theIsForce : bool=False) -> None: 
        """
        Marks BVH of selectable objects for rebuild. Parameter theIsForce set as true guarantees that 1st level BVH for the viewer selector will be rebuilt during this call
        """
    def RebuildSensitivesTree(self,theObject : SelectMgr_SelectableObject,theIsForce : bool=False) -> None: 
        """
        Marks BVH of sensitive entities of particular selectable object for rebuild. Parameter theIsForce set as true guarantees that 2nd level BVH for the object given will be rebuilt during this call
        """
    def RemovePicked(self,theObject : SelectMgr_SelectableObject) -> bool: 
        """
        Remove picked entities associated with specified object.
        """
    def RemoveSelectableObject(self,theObject : SelectMgr_SelectableObject) -> None: 
        """
        Removes selectable object from map of selectable ones
        """
    def RemoveSelectionOfObject(self,theObject : SelectMgr_SelectableObject,theSelection : SelectMgr_Selection) -> None: 
        """
        Removes selection of the object and marks its BVH tree for rebuild
        """
    def ResetSelectionActivationStatus(self) -> None: 
        """
        Marks all added sensitive entities of all objects as non-selectable
        """
    def SelectableObjects(self) -> SelectMgr_SelectableObjectSet: 
        """
        Return map of selectable objects.
        """
    def Sensitivity(self) -> float: 
        """
        Returns the largest sensitivity of picking
        """
    def SetDepthTolerance(self,theType : SelectMgr_TypeOfDepthTolerance,theTolerance : float) -> None: 
        """
        Set the tolerance for considering two entities having a similar depth (distance from eye to entity).
        """
    def SetEntitySetBuilder(self,theBuilder : OCP.Select3D.Select3D_BVHBuilder3d) -> None: 
        """
        Sets the default builder used to construct BVH of entity set. The new builder will be also assigned for already defined objects, but computed BVH trees will not be invalidated.
        """
    def SetPickClosest(self,theToPreferClosest : bool) -> None: 
        """
        Set flag determining precedence of picked depth over entity priority in sorted results.
        """
    def SetPixelTolerance(self,theTolerance : int) -> None: 
        """
        Sets the pixel tolerance <theTolerance>.
        """
    def SetToPrebuildBVH(self,theToPrebuild : bool,theThreadsNum : int=-1) -> None: 
        """
        Enables/disables building BVH for sensitives in separate threads
        """
    def SortResult(self) -> None: 
        """
        Sorts the detected entities by priority and distance.
        """
    @overload
    def Status(self,theSelection : SelectMgr_Selection) -> SelectMgr_StateOfSelection: 
        """
        Returns the selection status Status of the selection aSelection.

        None
        """
    @overload
    def Status(self,theSelectableObject : SelectMgr_SelectableObject) -> OCP.TCollection.TCollection_AsciiString: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToPickClosest(self) -> bool: 
        """
        Return the flag determining precedence of picked depth (distance from eye to entity) over entity priority in sorted results; TRUE by default. When flag is TRUE, priority will be considered only if entities have the same depth within the tolerance. When flag is FALSE, entities with higher priority will be in front regardless of their depth (like x-ray).
        """
    def ToPixMap(self,theImage : OCP.Image.Image_PixMap,theView : OCP.V3d.V3d_View,theType : OCP.StdSelect.StdSelect_TypeOfSelectionImage,thePickedIndex : int=1) -> bool: 
        """
        Dump of detection results into image. This method performs axis picking for each pixel in the image and generates a color depending on picking results and selection image type.
        """
    def ToPrebuildBVH(self) -> bool: 
        """
        Returns TRUE if building BVH for sensitives in separate threads is enabled
        """
    def WaitForBVHBuild(self) -> None: 
        """
        Waits BVH threads finished building
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
SelectMgr_FilterType_AND: OCP.SelectMgr.SelectMgr_FilterType # value = <SelectMgr_FilterType.SelectMgr_FilterType_AND: 0>
SelectMgr_FilterType_OR: OCP.SelectMgr.SelectMgr_FilterType # value = <SelectMgr_FilterType.SelectMgr_FilterType_OR: 1>
SelectMgr_PickingStrategy_FirstAcceptable: OCP.SelectMgr.SelectMgr_PickingStrategy # value = <SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_FirstAcceptable: 0>
SelectMgr_PickingStrategy_OnlyTopmost: OCP.SelectMgr.SelectMgr_PickingStrategy # value = <SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_OnlyTopmost: 1>
SelectMgr_SOS_Activated: OCP.SelectMgr.SelectMgr_StateOfSelection # value = <SelectMgr_StateOfSelection.SelectMgr_SOS_Activated: 1>
SelectMgr_SOS_Any: OCP.SelectMgr.SelectMgr_StateOfSelection # value = <SelectMgr_StateOfSelection.SelectMgr_SOS_Any: -2>
SelectMgr_SOS_Deactivated: OCP.SelectMgr.SelectMgr_StateOfSelection # value = <SelectMgr_StateOfSelection.SelectMgr_SOS_Deactivated: 0>
SelectMgr_SOS_Unknown: OCP.SelectMgr.SelectMgr_StateOfSelection # value = <SelectMgr_StateOfSelection.SelectMgr_SOS_Unknown: -1>
SelectMgr_SelectionType_Box: OCP.SelectMgr.SelectMgr_SelectionType # value = <SelectMgr_SelectionType.SelectMgr_SelectionType_Box: 1>
SelectMgr_SelectionType_Point: OCP.SelectMgr.SelectMgr_SelectionType # value = <SelectMgr_SelectionType.SelectMgr_SelectionType_Point: 0>
SelectMgr_SelectionType_Polyline: OCP.SelectMgr.SelectMgr_SelectionType # value = <SelectMgr_SelectionType.SelectMgr_SelectionType_Polyline: 2>
SelectMgr_SelectionType_Unknown: OCP.SelectMgr.SelectMgr_SelectionType # value = <SelectMgr_SelectionType.SelectMgr_SelectionType_Unknown: -1>
SelectMgr_TBU_Add: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Add: 0>
SelectMgr_TBU_Invalidate: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Invalidate: 3>
SelectMgr_TBU_None: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_None: 4>
SelectMgr_TBU_Remove: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Remove: 1>
SelectMgr_TBU_Renew: OCP.SelectMgr.SelectMgr_TypeOfBVHUpdate # value = <SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Renew: 2>
SelectMgr_TOU_Full: OCP.SelectMgr.SelectMgr_TypeOfUpdate # value = <SelectMgr_TypeOfUpdate.SelectMgr_TOU_Full: 0>
SelectMgr_TOU_None: OCP.SelectMgr.SelectMgr_TypeOfUpdate # value = <SelectMgr_TypeOfUpdate.SelectMgr_TOU_None: 2>
SelectMgr_TOU_Partial: OCP.SelectMgr.SelectMgr_TypeOfUpdate # value = <SelectMgr_TypeOfUpdate.SelectMgr_TOU_Partial: 1>
SelectMgr_TypeOfDepthTolerance_SensitivityFactor: OCP.SelectMgr.SelectMgr_TypeOfDepthTolerance # value = <SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_SensitivityFactor: 2>
SelectMgr_TypeOfDepthTolerance_Uniform: OCP.SelectMgr.SelectMgr_TypeOfDepthTolerance # value = <SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_Uniform: 0>
SelectMgr_TypeOfDepthTolerance_UniformPixels: OCP.SelectMgr.SelectMgr_TypeOfDepthTolerance # value = <SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_UniformPixels: 1>
