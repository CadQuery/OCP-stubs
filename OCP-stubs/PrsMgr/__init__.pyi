import OCP.PrsMgr
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.Quantity
import OCP.Aspect
import OCP.Bnd
import OCP.Standard
import OCP.gp
import OCP.Geom
import OCP.Graphic3d
import OCP.V3d
import OCP.TColStd
import OCP.Prs3d
__all__  = [
"PrsMgr_ListOfPresentableObjects",
"PrsMgr_ListOfPresentations",
"PrsMgr_PresentableObject",
"PrsMgr_Presentation",
"PrsMgr_PresentationManager",
"PrsMgr_Presentations",
"PrsMgr_TypeOfPresentation3d",
"PrsMgr_TOP_AllView",
"PrsMgr_TOP_ProjectorDependant"
]
class PrsMgr_ListOfPresentableObjects(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : PrsMgr_PresentableObject) -> PrsMgr_PresentableObject: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : PrsMgr_ListOfPresentableObjects) -> None: ...
    @overload
    def Append(self,theItem : PrsMgr_PresentableObject,theIter : Any) -> None: ...
    def Assign(self,theOther : PrsMgr_ListOfPresentableObjects) -> PrsMgr_ListOfPresentableObjects: 
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
    def First(self) -> PrsMgr_PresentableObject: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : PrsMgr_PresentableObject,theIter : Any) -> PrsMgr_PresentableObject: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : PrsMgr_ListOfPresentableObjects,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : PrsMgr_ListOfPresentableObjects,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : PrsMgr_PresentableObject,theIter : Any) -> PrsMgr_PresentableObject: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> PrsMgr_PresentableObject: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : PrsMgr_ListOfPresentableObjects) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : PrsMgr_PresentableObject) -> PrsMgr_PresentableObject: ...
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
    def __init__(self,theOther : PrsMgr_ListOfPresentableObjects) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class PrsMgr_ListOfPresentations(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : PrsMgr_ListOfPresentations) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Structure: ...
    @overload
    def Append(self,theItem : OCP.Graphic3d.Graphic3d_Structure,theIter : Any) -> None: ...
    def Assign(self,theOther : PrsMgr_ListOfPresentations) -> PrsMgr_ListOfPresentations: 
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
    def First(self) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : PrsMgr_ListOfPresentations,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OCP.Graphic3d.Graphic3d_Structure,theIter : Any) -> OCP.Graphic3d.Graphic3d_Structure: ...
    @overload
    def InsertBefore(self,theItem : OCP.Graphic3d.Graphic3d_Structure,theIter : Any) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : PrsMgr_ListOfPresentations,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : PrsMgr_ListOfPresentations) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Structure: ...
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
    def __init__(self,theOther : PrsMgr_ListOfPresentations) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class PrsMgr_PresentableObject(OCP.Standard.Standard_Transient):
    """
    A framework to supply the Graphic3d structure of the object to be presented. On the first display request, this structure is created by calling the appropriate algorithm and retaining this framework for further display. This abstract framework is inherited in Application Interactive Services (AIS), notably by AIS_InteractiveObject. Consequently, 3D presentation should be handled by the relevant daughter classes and their member functions in AIS. This is particularly true in the creation of new interactive objects.A framework to supply the Graphic3d structure of the object to be presented. On the first display request, this structure is created by calling the appropriate algorithm and retaining this framework for further display. This abstract framework is inherited in Application Interactive Services (AIS), notably by AIS_InteractiveObject. Consequently, 3D presentation should be handled by the relevant daughter classes and their member functions in AIS. This is particularly true in the creation of new interactive objects.
    """
    def AcceptDisplayMode(self,theMode : int) -> bool: 
        """
        Returns true if the class of objects accepts specified display mode index. The interactive context can have a default mode of representation for the set of Interactive Objects. This mode may not be accepted by a given class of objects. Consequently, this virtual method allowing us to get information about the class in question must be implemented. At least one display mode index should be accepted by this method. Although subclass can leave default implementation, it is highly desired defining exact list of supported modes instead, which is usually an enumeration for one object or objects class sharing similar list of display modes.
        """
    def AddChild(self,theObject : PrsMgr_PresentableObject) -> None: 
        """
        Makes theObject child of current object in scene hierarchy.
        """
    def AddChildWithCurrentTransformation(self,theObject : PrsMgr_PresentableObject) -> None: 
        """
        Makes theObject child of current object in scene hierarchy with keeping the current global transformation So the object keeps the same position/orientation in the global CS.
        """
    def AddClipPlane(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> None: 
        """
        Adds clip plane for graphical clipping for all display mode presentations. The composition of clip planes truncates the rendering space to convex volume. Please be aware that number of supported clip plane is limited. The planes which exceed the limit are ignored. Besides of this, some planes can be already set in view where the object is shown: the number of these planes should be subtracted from limit to predict the maximum possible number of object clipping planes.
        """
    def Attributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Returns the attributes settings.
        """
    def BoundingBox(self,theBndBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        Returns bounding box of object correspondingly to its current display mode. This method requires presentation to be already computed, since it relies on bounding box of presentation structures, which are supposed to be same/close amongst different display modes of this object.
        """
    def Children(self) -> PrsMgr_ListOfPresentableObjects: 
        """
        Returns children of the current object.
        """
    def ClipPlanes(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Get clip planes.
        """
    def Color(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns the color setting of the Interactive Object.
        """
    def CombinedParentTransformation(self) -> OCP.Geom.Geom_Transformation: 
        """
        Return combined parent transformation.
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
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicHilightAttributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Returns the hilight attributes settings. When not NULL, overrides both Prs3d_TypeOfHighlight_LocalDynamic and Prs3d_TypeOfHighlight_Dynamic defined within AIS_InteractiveContext.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTransformPersistenceMode(self) -> OCP.Graphic3d.Graphic3d_TransModeFlags: 
        """
        Gets Transform Persistence Mode for this object
        """
    def GetTransformPersistencePoint(self) -> OCP.gp.gp_Pnt: 
        """
        Gets point of transform persistence for this object
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
        Returns the hilight attributes settings. When not NULL, overrides both Prs3d_TypeOfHighlight_LocalSelected and Prs3d_TypeOfHighlight_Selected defined within AIS_InteractiveContext.
        """
    def HilightMode(self) -> int: 
        """
        Returns highlight display mode. This is obsolete method for backward compatibility - use ::HilightAttributes() and ::DynamicHilightAttributes() instead.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InversedTransformation(self) -> OCP.gp.gp_GTrsf: 
        """
        Return inversed transformation.
        """
    def IsInfinite(self) -> bool: 
        """
        Returns true if the interactive object is infinite; FALSE by default. This flag affects various operations operating on bounding box of graphic presentations of this object. For instance, infinite objects are not taken in account for View FitAll. This does not necessarily means that object is actually infinite, auxiliary objects might be also marked with this flag to achieve desired behavior.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def LocalTransformationGeom(self) -> OCP.Geom.Geom_Transformation: 
        """
        Return the local transformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def Material(self) -> OCP.Graphic3d.Graphic3d_NameOfMaterial: 
        """
        Returns the current material setting as enumeration value.
        """
    def Parent(self) -> PrsMgr_PresentableObject: 
        """
        Returns parent of current object in scene hierarchy.
        """
    def PolygonOffsets(self,aFactor : float,aUnits : float) -> Tuple[int]: 
        """
        Retrieves current polygon offsets settings from <myDrawer>.
        """
    def Presentations(self) -> PrsMgr_Presentations: 
        """
        Return presentations.
        """
    def RemoveChild(self,theObject : PrsMgr_PresentableObject) -> None: 
        """
        Removes theObject from children of current object in scene hierarchy.
        """
    def RemoveChildWithRestoreTransformation(self,theObject : PrsMgr_PresentableObject) -> None: 
        """
        Removes theObject from children of current object in scene hierarchy with keeping the current global transformation. So the object keeps the same position/orientation in the global CS.
        """
    def RemoveClipPlane(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> None: 
        """
        Removes previously added clip plane.
        """
    def ResetTransformation(self) -> None: 
        """
        resets local transformation to identity.
        """
    def SetAttributes(self,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Initializes the drawing tool theDrawer.
        """
    def SetClipPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Set clip planes for graphical clipping for all display mode presentations. The composition of clip planes truncates the rendering space to convex volume. Please be aware that number of supported clip plane is limited. The planes which exceed the limit are ignored. Besides of this, some planes can be already set in view where the object is shown: the number of these planes should be subtracted from limit to predict the maximum possible number of object clipping planes.

        None
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
    def SetLocalTransformation(self,theTrsf : OCP.Geom.Geom_Transformation) -> None: ...
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
    @overload
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Sets up Transform Persistence defining a special Local Coordinate system where this object should be located. Note that management of Transform Persistence object is more expensive than of the normal one, because it requires its position being recomputed basing on camera position within each draw call / traverse.

        Sets up Transform Persistence Mode for this object. This function used to lock in object position, rotation and / or zooming relative to camera position. Object will be drawn in the origin setted by thePoint parameter (except Graphic3d_TMF_TriedronPers flag - see description later). theMode should be: - Graphic3d_TMF_None - no persistence attributes (reset); - Graphic3d_TMF_ZoomPers - object doesn't resize; - Graphic3d_TMF_RotatePers - object doesn't rotate; - Graphic3d_TMF_ZoomRotatePers - object doesn't resize and rotate; - Graphic3d_TMF_RotatePers - object doesn't rotate; - Graphic3d_TMF_TriedronPers - object behaves like trihedron. If Graphic3d_TMF_TriedronPers or Graphic3d_TMF_2d persistence mode selected thePoint coordinates X and Y means: - X = 0.0, Y = 0.0 - center of view window; - X > 0.0, Y > 0.0 - right upper corner of view window; - X > 0.0, Y < 0.0 - right lower corner of view window; - X < 0.0, Y > 0.0 - left upper corner of view window; - X < 0.0, Y < 0.0 - left lower corner of view window. And Z coordinate defines the gap from border of view window (except center position).
        """
    @overload
    def SetTransformPersistence(self,theMode : OCP.Graphic3d.Graphic3d_TransModeFlags,thePoint : OCP.gp.gp_Pnt=OCP.gp.gp_Pnt) -> None: ...
    def SetTransparency(self,aValue : float=0.6) -> None: 
        """
        Attributes a setting aValue for transparency. The transparency value should be between 0.0 and 1.0. At 0.0 an object will be totally opaque, and at 1.0, fully transparent. Warning At a value of 1.0, there may be nothing visible.
        """
    def SetTypeOfPresentation(self,theType : PrsMgr_TypeOfPresentation3d) -> None: 
        """
        Set type of presentation.
        """
    def SetWidth(self,theWidth : float) -> None: 
        """
        Allows you to provide the setting aValue for width. Only the Interactive Object knows which Drawer attribute is affected by the width setting.
        """
    def SetZLayer(self,theLayerId : int) -> None: 
        """
        Set Z layer ID and update all presentations of the presentable object. The layers mechanism allows drawing objects in higher layers in overlay of objects in lower layers.
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
    def TransformationGeom(self) -> OCP.Geom.Geom_Transformation: 
        """
        Return the transformation taking into account transformation of parent object(s). Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    def Transparency(self) -> float: 
        """
        Returns the transparency setting. This will be between 0.0 and 1.0. At 0.0 an object will be totally opaque, and at 1.0, fully transparent.
        """
    def TypeOfPresentation3d(self) -> PrsMgr_TypeOfPresentation3d: 
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
    def UpdateTransformation(self) -> None: 
        """
        Updates final transformation (parent + local) of presentable object and its presentations.
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
class PrsMgr_Presentation(OCP.Graphic3d.Graphic3d_Structure, OCP.Standard.Standard_Transient):
    @staticmethod
    def AcceptConnection_s(theStructure1 : OCP.Graphic3d.Graphic3d_Structure,theStructure2 : OCP.Graphic3d.Graphic3d_Structure,theType : OCP.Graphic3d.Graphic3d_TypeOfConnection) -> bool: 
        """
        Returns Standard_True if the connection is possible between <AStructure1> and <AStructure2> without a creation of a cycle.
        """
    def Ancestors(self,SG : Any) -> None: 
        """
        Returns the group of structures to which <me> is connected.
        """
    def CStructure(self) -> OCP.Graphic3d.Graphic3d_CStructure: 
        """
        Returns the low-level structure
        """
    def CalculateBoundBox(self) -> None: 
        """
        Computes axis-aligned bounding box of a structure.
        """
    def Clear(self,theWithDestruction : bool=True) -> None: 
        """
        removes the whole content of the presentation. Does not remove the other connected presentations.
        """
    def ClipPlanes(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Get clip planes slicing the structure on rendering.
        """
    def Compute(self) -> None: 
        """
        Compute structure using presentation manager.
        """
    def ComputeVisual(self) -> OCP.Graphic3d.Graphic3d_TypeOfStructure: 
        """
        None
        """
    @overload
    def Connect(self,theStructure : OCP.Graphic3d.Graphic3d_Structure,theType : OCP.Graphic3d.Graphic3d_TypeOfConnection,theWithCheck : bool=False) -> None: 
        """
        If Atype is TOC_DESCENDANT then add <AStructure> as a child structure of <me>. If Atype is TOC_ANCESTOR then add <AStructure> as a parent structure of <me>. The connection propagates Display, Highlight, Erase, Remove, and stacks the transformations. No connection if the graph of the structures contains a cycle and <WithCheck> is Standard_True;

        None
        """
    @overload
    def Connect(self,thePrs : OCP.Graphic3d.Graphic3d_Structure) -> None: ...
    def ContainsFacet(self) -> bool: 
        """
        Returns Standard_True if the structure <me> contains Polygons, Triangles or Quadrangles.
        """
    def CurrentGroup(self) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the last created group or creates new one if list is empty.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Descendants(self,SG : Any) -> None: 
        """
        Returns the group of structures connected to <me>.
        """
    def Disconnect(self,theStructure : OCP.Graphic3d.Graphic3d_Structure) -> None: 
        """
        Suppress the connection between <AStructure> and <me>.
        """
    def DisconnectAll(self,AType : OCP.Graphic3d.Graphic3d_TypeOfConnection) -> None: 
        """
        If Atype is TOC_DESCENDANT then suppress all the connections with the child structures of <me>. If Atype is TOC_ANCESTOR then suppress all the connections with the parent structures of <me>.
        """
    def Display(self) -> None: 
        """
        Display structure.
        """
    def DisplayPriority(self) -> int: 
        """
        Returns the current display priority for this structure.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Erase(self) -> None: 
        """
        Remove structure.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetZLayer(self) -> int: 
        """
        Get Z layer ID of displayed structure. The method returns -1 if the structure has no ID (deleted from graphic driver).
        """
    def GraphicClear(self,WithDestruction : bool) -> None: 
        """
        Clears the structure <me>.
        """
    def GraphicConnect(self,theDaughter : OCP.Graphic3d.Graphic3d_Structure) -> None: 
        """
        None
        """
    def GraphicDisconnect(self,theDaughter : OCP.Graphic3d.Graphic3d_Structure) -> None: 
        """
        None
        """
    def GraphicTransform(self,theTrsf : OCP.Geom.Geom_Transformation) -> None: 
        """
        Internal method which sets new transformation without calling graphic manager callbacks.
        """
    def Groups(self) -> OCP.Graphic3d.Graphic3d_SequenceOfGroup: 
        """
        Returns the groups sequence included in this structure.
        """
    def HLRValidation(self) -> bool: 
        """
        Hidden parts stored in this structure are valid if: 1) the owner is defined. 2) they are not invalid.
        """
    def Highlight(self,theStyle : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Highlight structure.
        """
    def HighlightStyle(self) -> OCP.Graphic3d.Graphic3d_PresentationAttributes: 
        """
        Returns the highlight attributes.
        """
    def Identification(self) -> int: 
        """
        Returns the identification number of this structure.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDeleted(self) -> bool: 
        """
        Returns TRUE if this structure is deleted (after Remove() call).
        """
    def IsDisplayed(self) -> bool: 
        """
        Return TRUE if structure has been displayed and in no hidden state.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns Standard_True if the structure <me> is empty. Warning: A structure is empty if : it do not have group or all the groups are empties and it do not have descendant or all the descendants are empties.
        """
    def IsHighlighted(self) -> bool: 
        """
        Returns the highlight indicator for this structure.
        """
    def IsInfinite(self) -> bool: 
        """
        Returns Standard_True if the structure <me> is infinite.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
        Returns true if structure has mutable nature (content or location are be changed regularly). Mutable structure will be managed in different way than static onces.
        """
    def IsTransformed(self) -> bool: 
        """
        Returns TRUE if the structure is transformed.
        """
    def IsVisible(self) -> bool: 
        """
        Returns the visibility indicator for this structure.
        """
    def MinMaxValues(self,theToIgnoreInfiniteFlag : bool=False) -> OCP.Bnd.Bnd_Box: 
        """
        Returns the coordinates of the boundary box of the structure <me>. If <theToIgnoreInfiniteFlag> is TRUE, the method returns actual graphical boundaries of the Graphic3d_Group components. Otherwise, the method returns boundaries taking into account infinite state of the structure. This approach generally used for application specific fit operation (e.g. fitting the model into screen, not taking into accout infinite helper elements). Warning: If the structure <me> is empty then the empty box is returned, If the structure <me> is infinite then the whole box is returned.
        """
    def Mode(self) -> int: 
        """
        Return display mode index.
        """
    def MustBeUpdated(self) -> bool: 
        """
        None
        """
    @staticmethod
    def Network_s(theStructure : OCP.Graphic3d.Graphic3d_Structure,theType : OCP.Graphic3d.Graphic3d_TypeOfConnection,theSet : Any) -> None: 
        """
        Returns <ASet> the group of structures : - directly or indirectly connected to <AStructure> if the TypeOfConnection == TOC_DESCENDANT - to which <AStructure> is directly or indirectly connected if the TypeOfConnection == TOC_ANCESTOR
        """
    def NewGroup(self) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Append new group to this structure.
        """
    def NumberOfGroups(self) -> int: 
        """
        Returns the current number of groups in this structure.
        """
    def Owner(self) -> capsule: 
        """
        None
        """
    def Presentation(self) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        None
        """
    def PresentationManager(self) -> PrsMgr_PresentationManager: 
        """
        returns the PresentationManager in which the presentation has been created.
        """
    @staticmethod
    def PrintNetwork_s(AStructure : OCP.Graphic3d.Graphic3d_Structure,AType : OCP.Graphic3d.Graphic3d_TypeOfConnection) -> None: 
        """
        Prints informations about the network associated with the structure <AStructure>.
        """
    @overload
    def ReCompute(self,aProjector : OCP.Graphic3d.Graphic3d_DataStructureManager) -> None: 
        """
        Forces a new construction of the structure <me> if <me> is displayed and TOS_COMPUTED.

        Forces a new construction of the structure <me> if <me> is displayed in <aProjetor> and TOS_COMPUTED.
        """
    @overload
    def ReCompute(self) -> None: ...
    @overload
    def Remove(self) -> None: 
        """
        Suppress the structure <me>. It will be erased at the next screen update. Warning: No more graphic operations in <me> after this call. Category: Methods to modify the class definition

        None

        Suppress the structure in the list of descendants or in the list of ancestors.
        """
    @overload
    def Remove(self,thePtr : OCP.Graphic3d.Graphic3d_Structure,theType : OCP.Graphic3d.Graphic3d_TypeOfConnection) -> None: ...
    @overload
    def Remove(self,thePrs : OCP.Graphic3d.Graphic3d_Structure) -> None: ...
    def RemoveAll(self) -> None: 
        """
        None
        """
    def ResetDisplayPriority(self) -> None: 
        """
        Reset the current priority of the structure to the previous priority. Category: Methods to modify the class definition Warning: If <me> is displayed then the SetDisplayPriority method erase <me> and display <me> with the previous priority.
        """
    def SetClipPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Changes a sequence of clip planes slicing the structure on rendering.
        """
    def SetComputeVisual(self,theVisual : OCP.Graphic3d.Graphic3d_TypeOfStructure) -> None: 
        """
        None
        """
    def SetDisplayPriority(self,Priority : int) -> None: 
        """
        Modifies the order of displaying the structure. Values are between 0 and 10. Structures are drawn according to their display priorities in ascending order. A structure of priority 10 is displayed the last and appears over the others. The default value is 5. Category: Methods to modify the class definition Warning: If <me> is displayed then the SetDisplayPriority method erase <me> and display <me> with the new priority. Raises PriorityDefinitionError if <Priority> is greater than 10 or a negative value.
        """
    def SetHLRValidation(self,theFlag : bool) -> None: 
        """
        None
        """
    def SetInfiniteState(self,theToSet : bool) -> None: 
        """
        Sets infinite flag. When TRUE, the MinMaxValues method returns: theXMin = theYMin = theZMin = RealFirst(). theXMax = theYMax = theZMax = RealLast(). By default, structure is created not infinite but empty.
        """
    def SetIsForHighlight(self,isForHighlight : bool) -> None: 
        """
        Marks the structure <me> representing wired structure needed for highlight only so it won't be added to BVH tree.
        """
    def SetMutable(self,theIsMutable : bool) -> None: 
        """
        Sets if the structure location has mutable nature (content or location will be changed regularly).
        """
    def SetOwner(self,theOwner : capsule) -> None: 
        """
        None
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Modifies the current transform persistence (pan, zoom or rotate)
        """
    def SetTransformation(self,theTrsf : OCP.Geom.Geom_Transformation) -> None: 
        """
        Modifies the current local transformation
        """
    def SetUpdateStatus(self,theUpdateStatus : bool) -> None: 
        """
        None
        """
    def SetVisible(self,AValue : bool) -> None: 
        """
        Modifies the visibility indicator to Standard_True or Standard_False for the structure <me>. The default value at the definition of <me> is Standard_True.
        """
    def SetVisual(self,AVisual : OCP.Graphic3d.Graphic3d_TypeOfStructure) -> None: 
        """
        Modifies the visualisation mode for the structure <me>.
        """
    def SetZLayer(self,theLayerId : int) -> None: 
        """
        Set Z layer ID for the structure. The Z layer mechanism allows to display structures presented in higher layers in overlay of structures in lower layers by switching off z buffer depth test between layers
        """
    def SetZoomLimit(self,LimitInf : float,LimitSup : float) -> None: 
        """
        Modifies the minimum and maximum zoom coefficients for the structure <me>. The default value at the definition of <me> is unlimited. Category: Methods to modify the class definition Warning: Raises StructureDefinitionError if <LimitInf> is greater than <LimitSup> or if <LimitInf> or <LimitSup> is a negative value.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,theTrsf : OCP.Geom.Geom_Transformation) -> None: 
        """
        None
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Returns transform persistence of the presentable object.
        """
    def Transformation(self) -> OCP.Geom.Geom_Transformation: 
        """
        Return local transformation.
        """
    @staticmethod
    def Transforms_s(theTrsf : OCP.gp.gp_Trsf,theX : float,theY : float,theZ : float) -> Tuple[float, float, float]: 
        """
        Transforms theX, theY, theZ with the transformation theTrsf.
        """
    def UnHighlight(self) -> None: 
        """
        Suppresses the highlight for the structure <me> in all the views of the visualiser.
        """
    def Unhighlight(self) -> None: 
        """
        Unhighlight structure.
        """
    def Visual(self) -> OCP.Graphic3d.Graphic3d_TypeOfStructure: 
        """
        Returns the visualisation mode for the structure <me>.
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
class PrsMgr_PresentationManager(OCP.Standard.Standard_Transient):
    """
    A framework to manage 3D displays, graphic entities and their updates. Used in the AIS package (Application Interactive Services), to enable the advanced user to define the default display mode of a new interactive object which extends the list of signatures and types. Definition of new display types is handled by calling the presentation algorithms provided by the StdPrs package.A framework to manage 3D displays, graphic entities and their updates. Used in the AIS package (Application Interactive Services), to enable the advanced user to define the default display mode of a new interactive object which extends the list of signatures and types. Definition of new display types is handled by calling the presentation algorithms provided by the StdPrs package.
    """
    def AddToImmediateList(self,thePrs : OCP.Graphic3d.Graphic3d_Structure) -> None: 
        """
        Stores thePrs in the transient list of presentations to be displayed in immediate mode. Will be taken in account in EndImmediateDraw method.
        """
    def BeginImmediateDraw(self) -> None: 
        """
        Resets the transient list of presentations previously displayed in immediate mode and begins accumulation of new list by following AddToImmediateList()/Color()/Highlight() calls.
        """
    def Clear(self,thePrsObject : PrsMgr_PresentableObject,theMode : int=0) -> None: 
        """
        Clears the presentation of the presentable object thePrsObject in this framework with the display mode theMode.
        """
    def ClearImmediateDraw(self) -> None: 
        """
        Resets the transient list of presentations previously displayed in immediate mode.
        """
    def Color(self,thePrsObject : PrsMgr_PresentableObject,theStyle : OCP.Prs3d.Prs3d_Drawer,theMode : int=0,theSelObj : PrsMgr_PresentableObject=None,theImmediateStructLayerId : int=-3) -> None: 
        """
        Highlights the graphic object thePrsObject in the color theColor. thePrsObject has the display mode theMode; this has the default value of 0, that is, the wireframe display mode.
        """
    def Connect(self,thePrsObject : PrsMgr_PresentableObject,theOtherObject : PrsMgr_PresentableObject,theMode : int=0,theOtherMode : int=0) -> None: 
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
    def Display(self,thePrsObject : PrsMgr_PresentableObject,theMode : int=0) -> None: 
        """
        Displays the presentation of the object in the given Presentation manager with the given mode. The mode should be enumerated by the object which inherits PresentableObject.
        """
    def DisplayPriority(self,thePrsObject : PrsMgr_PresentableObject,theMode : int) -> int: 
        """
        Returns the display priority of the presentable object thePrsObject in this framework with the display mode theMode.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EndImmediateDraw(self,theViewer : OCP.V3d.V3d_Viewer) -> None: 
        """
        Allows rapid drawing of the each view in theViewer by avoiding an update of the whole background.
        """
    def Erase(self,thePrsObject : PrsMgr_PresentableObject,theMode : int=0) -> None: 
        """
        erases the presentation of the object in the given Presentation manager with the given mode. If is -1, then erases all presentations of the object.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetZLayer(self,thePrsObject : PrsMgr_PresentableObject) -> int: 
        """
        Get Z layer ID assigned to all presentations of the object. Method returns -1 value if object has no presentations and is impossible to get layer index.
        """
    def HasPresentation(self,thePrsObject : PrsMgr_PresentableObject,theMode : int=0) -> bool: 
        """
        Returns true if there is a presentation of the presentable object thePrsObject in this framework, thePrsObject having the display mode theMode.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDisplayed(self,thePrsObject : PrsMgr_PresentableObject,theMode : int=0) -> bool: 
        """
        None
        """
    def IsHighlighted(self,thePrsObject : PrsMgr_PresentableObject,theMode : int=0) -> bool: 
        """
        Returns true if the presentation of the presentable object thePrsObject in this framework with the display mode theMode is highlighted.
        """
    def IsImmediateModeOn(self) -> bool: 
        """
        Returns true if Presentation Manager is accumulating transient list of presentations to be displayed in immediate mode.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Presentation(self,thePrsObject : PrsMgr_PresentableObject,theMode : int=0,theToCreate : bool=False,theSelObj : PrsMgr_PresentableObject=None) -> PrsMgr_Presentation: 
        """
        Returns the presentation Presentation of the presentable object thePrsObject in this framework. When theToCreate is true - automatically creates presentation for specified mode when not exist. Optional argument theSelObj specifies parent decomposed object to inherit its view affinity.
        """
    def RedrawImmediate(self,theViewer : OCP.V3d.V3d_Viewer) -> None: 
        """
        Clears and redisplays immediate structures of the viewer taking into account its affinity.
        """
    def SetDisplayPriority(self,thePrsObject : PrsMgr_PresentableObject,theMode : int,theNewPrior : int) -> None: 
        """
        Sets the display priority theNewPrior of the presentable object thePrsObject in this framework with the display mode theMode.
        """
    def SetVisibility(self,thePrsObject : PrsMgr_PresentableObject,theMode : int,theValue : bool) -> None: 
        """
        Sets the visibility of presentable object.
        """
    def SetZLayer(self,thePrsObject : PrsMgr_PresentableObject,theLayerId : int) -> None: 
        """
        Set Z layer ID for all presentations of the object.
        """
    def StructureManager(self) -> OCP.Graphic3d.Graphic3d_StructureManager: 
        """
        Returns the structure manager.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,thePrsObject : PrsMgr_PresentableObject,theTransformation : OCP.Geom.Geom_Transformation,theMode : int=0) -> None: 
        """
        Sets the transformation theTransformation for the presentable object thePrsObject. thePrsObject has the display mode theMode; this has the default value of 0, that is, the wireframe display mode.
        """
    @overload
    def Unhighlight(self,thePrsObject : PrsMgr_PresentableObject) -> None: 
        """
        Removes highlighting from the presentation of the presentable object.

        None
        """
    @overload
    def Unhighlight(self,thePrsObject : PrsMgr_PresentableObject,theMode : int) -> None: ...
    def Update(self,thePrsObject : PrsMgr_PresentableObject,theMode : int=0) -> None: 
        """
        Updates the presentation of the presentable object thePrsObject in this framework with the display mode theMode.
        """
    def UpdateHighlightTrsf(self,theViewer : OCP.V3d.V3d_Viewer,theObj : PrsMgr_PresentableObject,theMode : int=0,theSelObj : PrsMgr_PresentableObject=None) -> None: 
        """
        Allows to apply location transformation to shadow highlight presentation immediately.
        """
    def __init__(self,theStructureManager : OCP.Graphic3d.Graphic3d_StructureManager) -> None: ...
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
class PrsMgr_Presentations(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : PrsMgr_Presentations) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : PrsMgr_Presentation) -> None: ...
    def Assign(self,theOther : PrsMgr_Presentations) -> PrsMgr_Presentations: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> PrsMgr_Presentation: 
        """
        First item access
        """
    def ChangeLast(self) -> PrsMgr_Presentation: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> PrsMgr_Presentation: 
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
    def First(self) -> PrsMgr_Presentation: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : PrsMgr_Presentations) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : PrsMgr_Presentation) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : PrsMgr_Presentations) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : PrsMgr_Presentation) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> PrsMgr_Presentation: 
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
    def Prepend(self,theSeq : PrsMgr_Presentations) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : PrsMgr_Presentation) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : PrsMgr_Presentation) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : PrsMgr_Presentations) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> PrsMgr_Presentation: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : PrsMgr_Presentations) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class PrsMgr_TypeOfPresentation3d():
    """
    To declare the type of presentation as follows - AllView for display involving no recalculation for new projectors (points of view)in hidden line removal mode - ProjectorDependant for display in hidden line removal mode, where every new point of view entails recalculation of the display.

    Members:

      PrsMgr_TOP_AllView

      PrsMgr_TOP_ProjectorDependant
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    PrsMgr_TOP_AllView: OCP.PrsMgr.PrsMgr_TypeOfPresentation3d # value = PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_AllView
    PrsMgr_TOP_ProjectorDependant: OCP.PrsMgr.PrsMgr_TypeOfPresentation3d # value = PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_ProjectorDependant
    __entries: dict # value = {'PrsMgr_TOP_AllView': (PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_AllView, None), 'PrsMgr_TOP_ProjectorDependant': (PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_ProjectorDependant, None)}
    __members__: dict # value = {'PrsMgr_TOP_AllView': PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_AllView, 'PrsMgr_TOP_ProjectorDependant': PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_ProjectorDependant}
    pass
PrsMgr_TOP_AllView: OCP.PrsMgr.PrsMgr_TypeOfPresentation3d # value = PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_AllView
PrsMgr_TOP_ProjectorDependant: OCP.PrsMgr.PrsMgr_TypeOfPresentation3d # value = PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_ProjectorDependant
