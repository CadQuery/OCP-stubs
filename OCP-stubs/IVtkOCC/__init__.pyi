import OCP.IVtkOCC
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.AIS
import OCP.PrsMgr
import OCP.NCollection
import OCP.IVtk
import io
import OCP.SelectMgr
import OCP.Standard
import OCP.V3d
import OCP.StdSelect
import OCP.TopoDS
import OCP.Prs3d
import OCP.Select3D
import OCP.Quantity
import OCP.TColgp
import OCP.Bnd
import OCP.TopLoc
import OCP.Graphic3d
import OCP.gp
import OCP.Image
import OCP.Aspect
import OCP.TCollection
import OCP.TColStd
__all__  = [
"IVtkOCC_SelectableObject",
"IVtkOCC_Shape",
"IVtkOCC_ShapeMesher",
"IVtkOCC_ShapePickerAlgo",
"IVtkOCC_ViewerSelector",
"IVtk_PolylineList",
"IVtk_ShapeTypeMap"
]
class IVtkOCC_SelectableObject(OCP.SelectMgr.SelectMgr_SelectableObject, OCP.PrsMgr.PrsMgr_PresentableObject, OCP.Standard.Standard_Transient):
    """
    Class with selection primitives used by OCCT selection algorithm.Class with selection primitives used by OCCT selection algorithm.Class with selection primitives used by OCCT selection algorithm.
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
    def AddSelection(self,aSelection : OCP.SelectMgr.SelectMgr_Selection,aMode : int) -> None: 
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
        Returns bounding box of object
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
    def ComputeSelection(self,theSelection : OCP.SelectMgr.SelectMgr_Selection,theMode : int) -> None: 
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
    def GetAssemblyOwner(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
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
    def GetShape(self) -> IVtkOCC_Shape: 
        """
        None
        """
    def GlobalSelOwner(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
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
    def HilightOwnerWithColor(self,thePM : OCP.PrsMgr.PrsMgr_PresentationManager,theStyle : OCP.Prs3d.Prs3d_Drawer,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner) -> None: 
        """
        Method which hilight an owner belonging to this selectable object ( for fast presentation draw )
        """
    def HilightSelected(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,theSeq : OCP.SelectMgr.SelectMgr_SequenceOfOwner) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
    def RecomputePrimitives(self,theMode : int) -> None: 
        """
        Re-computes the sensitive primitives for all modes. IMPORTANT: Do not use this method to update selection primitives except implementing custom selection manager! This method does not take into account necessary BVH updates, but may invalidate the pointers it refers to. TO UPDATE SELECTION properly from outside classes, use method UpdateSelection.

        Re-computes the sensitive primitives which correspond to the <theMode>th selection mode. IMPORTANT: Do not use this method to update selection primitives except implementing custom selection manager! selection manager! This method does not take into account necessary BVH updates, but may invalidate the pointers it refers to. TO UPDATE SELECTION properly from outside classes, use method UpdateSelection.
        """
    @overload
    def RecomputePrimitives(self) -> None: ...
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
    def Selection(self,theMode : int) -> OCP.SelectMgr.SelectMgr_Selection: 
        """
        Returns the selection having specified selection mode or NULL.
        """
    def Selections(self) -> OCP.SelectMgr.SelectMgr_SequenceOfSelection: 
        """
        Return the sequence of selections.
        """
    def SetAssemblyOwner(self,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theMode : int=-1) -> None: 
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
    def SetLocalTransformation(self,theTrsf : OCP.TopLoc.TopLoc_Datum3D) -> None: 
        """
        Sets local transformation to theTransformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.

        Sets local transformation to theTransformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    @overload
    def SetLocalTransformation(self,theTrsf : OCP.gp.gp_Trsf) -> None: ...
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
    def SetShape(self,theShape : IVtkOCC_Shape) -> None: 
        """
        Sets the selectable shape
        """
    @overload
    def SetToUpdate(self,theMode : int) -> None: 
        """
        Flags presentation to be updated; UpdatePresentations() will recompute these presentations.

        flags all the Presentations to be Updated.
        """
    @overload
    def SetToUpdate(self) -> None: ...
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
    def UpdateTransformations(self,aSelection : OCP.SelectMgr.SelectMgr_Selection) -> None: 
        """
        Updates locations in all sensitive entities from <aSelection> and in corresponding entity owners.
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
class IVtkOCC_Shape(OCP.IVtk.IVtk_IShape, OCP.IVtk.IVtk_Interface, OCP.Standard.Standard_Transient):
    """
    OCC implementation of IShape interface.OCC implementation of IShape interface.OCC implementation of IShape interface.
    """
    def Attributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Return presentation attributes.
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
    def GetId(self) -> int: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectableObject(self) -> OCP.SelectMgr.SelectMgr_SelectableObject: 
        """
        Returns Handle to the selectable object for this shape.
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Get the wrapped original OCCT shape
        """
    def GetSubIds(self,arg1 : int) -> OCP.IVtk.IVtk_ShapeIdList: 
        """
        Get ids of sub-shapes composing a sub-shape with the given id
        """
    def GetSubShape(self,theId : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Get a sub-shape by its local ID.
        """
    def GetSubShapeId(self,theSubShape : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Get local ID of a sub-shape.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def SetAttributes(self,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Set presentation attributes.
        """
    def SetId(self,theId : int) -> None: 
        """
        None
        """
    def SetSelectableObject(self,theSelObj : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: 
        """
        Stores a handle to selectable object used by OCCT selection algorithm in a data field. This object internally caches selection data so it should be stored until the shape is no longer selectable. Note that the selectable object keeps a pointer to OccShape.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape,theDrawerLink : OCP.Prs3d.Prs3d_Drawer=None) -> None: ...
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
class IVtkOCC_ShapeMesher(OCP.IVtk.IVtk_IShapeMesher, OCP.IVtk.IVtk_Interface, OCP.Standard.Standard_Transient):
    """
    OCC implementation of IMesher interface.OCC implementation of IMesher interface.OCC implementation of IMesher interface.
    """
    def Build(self,theShape : OCP.IVtk.IVtk_IShape,theData : OCP.IVtk.IVtk_IShapeData) -> None: 
        """
        Main entry point for building shape representation
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
    def GetDeflection(self) -> float: 
        """
        Returns absolute deflection used by this algorithm. This value is calculated on the basis of the shape's bounding box. Zero might be returned in case if the underlying OCCT shape is empty or invalid. Thus check the returned value before passing it to OCCT meshing algorithms!
        """
    def GetDeviationAngle(self) -> float: 
        """
        Returns deviation angle used by this algorithm. This is the maximum allowed angle between the normals to the curve/surface and the normals to polyline/faceted representation.
        """
    def GetDeviationCoeff(self) -> float: 
        """
        Returns relative deviation coefficient used by this algorithm.
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class IVtkOCC_ShapePickerAlgo():
    """
    OCC implementation of 3D shapes picking algorithm.OCC implementation of 3D shapes picking algorithm.OCC implementation of 3D shapes picking algorithm.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetSelectionModes(self,theShape : OCP.IVtk.IVtk_IShape) -> OCP.IVtk.IVtk_SelectionModeList: 
        """
        Get activated selection modes for a shape.
        """
    def NbPicked(self) -> int: 
        """
        Get number of picked entities.
        """
    def RemoveSelectableObject(self,theShape : OCP.IVtk.IVtk_IShape) -> None: 
        """
        Remove selectable object from the picker (from internal maps).
        """
    @overload
    def SetSelectionMode(self,theShapes : OCP.IVtk.IVtk_ShapePtrList,theMode : OCP.IVtk.IVtk_SelectionMode,theIsTurnOn : bool=True) -> None: 
        """
        Activates/deactivates the given selection mode for the shape. If mode == SM_None, the shape becomes non-selectable and is removed from the internal selection data.

        Activates/deactivates the given selection mode for the shape. If mode == SM_None, the shape becomes non-selectable and is removed from the internal selection data.
        """
    @overload
    def SetSelectionMode(self,theShape : OCP.IVtk.IVtk_IShape,theMode : OCP.IVtk.IVtk_SelectionMode,theIsTurnOn : bool=True) -> None: ...
    def SetView(self,theView : OCP.IVtk.IVtk_IView) -> None: 
        """
        Sets the picker's view interface. The picker uses the view to obtain parameters of the 3D view projection.
        """
    def ShapesPicked(self) -> OCP.IVtk.IVtk_ShapeIdList: 
        """
        Returns the list of picked top-level shape IDs, in the order of increasing depth (the ID of the shape closest to the eye is the first in the list)
        """
    def SubShapesPicked(self,theId : int,theShapeList : OCP.IVtk.IVtk_ShapeIdList) -> None: ...
    def TopPickedPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Return topmost picked 3D point or (Inf, Inf, Inf) if undefined.
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
class IVtkOCC_ViewerSelector(OCP.SelectMgr.SelectMgr_ViewerSelector, OCP.Standard.Standard_Transient):
    """
    Class that implements OCCT selection algorithm.Class that implements OCCT selection algorithm.
    """
    def ActiveOwners(self,theOwners : OCP.AIS.AIS_NListOfEntityOwner) -> None: 
        """
        Returns the list of active entity owners
        """
    def AddSelectableObject(self,theObject : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: 
        """
        Adds new object to the map of selectable objects
        """
    def AddSelectionToObject(self,theObject : OCP.SelectMgr.SelectMgr_SelectableObject,theSelection : OCP.SelectMgr.SelectMgr_Selection) -> None: 
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
    def Contains(self,theObject : OCP.SelectMgr.SelectMgr_SelectableObject) -> bool: 
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
    def DepthToleranceType(self) -> OCP.SelectMgr.SelectMgr_TypeOfDepthTolerance: 
        """
        Return the type of tolerance for considering two entities having a similar depth (distance from eye to entity); SelectMgr_TypeOfDepthTolerance_SensitivityFactor by default.
        """
    @overload
    def DisplaySensitive(self,theView : OCP.V3d.V3d_View) -> None: 
        """
        Displays sensitives in view <theView>.

        None
        """
    @overload
    def DisplaySensitive(self,theSel : OCP.SelectMgr.SelectMgr_Selection,theTrsf : OCP.gp.gp_Trsf,theView : OCP.V3d.V3d_View,theToClearOthers : bool=True) -> None: ...
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
    def GetManager(self) -> OCP.SelectMgr.SelectMgr_SelectingVolumeManager: 
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
    def IsActive(self,theSelectableObject : OCP.SelectMgr.SelectMgr_SelectableObject,theMode : int) -> bool: 
        """
        Returns true if the selectable object aSelectableObject having the selection mode aMode is active in this selector.
        """
    def IsInside(self,theSelectableObject : OCP.SelectMgr.SelectMgr_SelectableObject,theMode : int) -> bool: 
        """
        Returns true if the selectable object aSelectableObject having the selection mode aMode is in this selector.
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def Modes(self,theSelectableObject : OCP.SelectMgr.SelectMgr_SelectableObject,theModeList : OCP.TColStd.TColStd_ListOfInteger,theWantedState : OCP.SelectMgr.SelectMgr_StateOfSelection=SelectMgr_StateOfSelection.SelectMgr_SOS_Any) -> bool: 
        """
        Returns the list of selection modes ModeList found in this selector for the selectable object aSelectableObject. Returns true if aSelectableObject is referenced inside this selector; returns false if the object is not present in this selector.
        """
    def MoveSelectableObject(self,theObject : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: 
        """
        Moves existing object from set of not transform persistence objects to set of transform persistence objects (or vice versa).
        """
    def NbPicked(self) -> int: 
        """
        Returns the number of detected owners.
        """
    def OnePicked(self) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns the picked element with the highest priority, and which is the closest to the last successful mouse position.
        """
    @overload
    def Pick(self,theXPMin : int,theYPMin : int,theXPMax : int,theYPMax : int,theView : OCP.V3d.V3d_View) -> None: 
        """
        Picks the sensitive entity at the pixel coordinates of the mouse <theXPix> and <theYPix>. The selector looks for touched areas and owners.

        Picks the sensitive entity according to the minimum and maximum pixel values <theXPMin>, <theYPMin>, <theXPMax> and <theYPMax> defining a 2D area for selection in the 3D view aView.

        pick action - input pixel values for polyline selection for selection.

        Picks the sensitive entity according to the input axis. This is geometric intersection 3D objects by axis (camera parameters are ignored and objects with transform persistance are skipped).
        """
    @overload
    def Pick(self,theAxis : OCP.gp.gp_Ax1,theView : OCP.V3d.V3d_View) -> None: ...
    @overload
    def Pick(self,theXPix : int,theYPix : int,theView : OCP.V3d.V3d_View) -> None: ...
    @overload
    def Pick(self,thePolyline : OCP.TColgp.TColgp_Array1OfPnt2d,theView : OCP.V3d.V3d_View) -> None: ...
    def Picked(self,theRank : int) -> OCP.SelectMgr.SelectMgr_EntityOwner: 
        """
        Returns the entity Owner for the object picked at specified position.
        """
    def PickedData(self,theRank : int) -> OCP.SelectMgr.SelectMgr_SortCriterion: 
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
    def RebuildSensitivesTree(self,theObject : OCP.SelectMgr.SelectMgr_SelectableObject,theIsForce : bool=False) -> None: 
        """
        Marks BVH of sensitive entities of particular selectable object for rebuild. Parameter theIsForce set as true guarantees that 2nd level BVH for the object given will be rebuilt during this call
        """
    def RemovePicked(self,theObject : OCP.SelectMgr.SelectMgr_SelectableObject) -> bool: 
        """
        Remove picked entities associated with specified object.
        """
    def RemoveSelectableObject(self,theObject : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: 
        """
        Removes selectable object from map of selectable ones
        """
    def RemoveSelectionOfObject(self,theObject : OCP.SelectMgr.SelectMgr_SelectableObject,theSelection : OCP.SelectMgr.SelectMgr_Selection) -> None: 
        """
        Removes selection of the object and marks its BVH tree for rebuild
        """
    def ResetSelectionActivationStatus(self) -> None: 
        """
        Marks all added sensitive entities of all objects as non-selectable
        """
    def SelectableObjects(self) -> OCP.SelectMgr.SelectMgr_SelectableObjectSet: 
        """
        Return map of selectable objects.
        """
    def Sensitivity(self) -> float: 
        """
        Returns the largest sensitivity of picking
        """
    def SetDepthTolerance(self,theType : OCP.SelectMgr.SelectMgr_TypeOfDepthTolerance,theTolerance : float) -> None: 
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
    def Status(self,theSelectableObject : OCP.SelectMgr.SelectMgr_SelectableObject) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the selection status Status of the selection aSelection.

        None
        """
    @overload
    def Status(self,theSelection : OCP.SelectMgr.SelectMgr_Selection) -> OCP.SelectMgr.SelectMgr_StateOfSelection: ...
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
class IVtk_PolylineList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : IVtk_PolylineList) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.TColgp.TColgp_SequenceOfPnt) -> OCP.TColgp.TColgp_SequenceOfPnt: ...
    @overload
    def Append(self,theItem : OCP.TColgp.TColgp_SequenceOfPnt,theIter : Any) -> None: ...
    def Assign(self,theOther : IVtk_PolylineList) -> IVtk_PolylineList: 
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
    def First(self) -> OCP.TColgp.TColgp_SequenceOfPnt: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.TColgp.TColgp_SequenceOfPnt,theIter : Any) -> OCP.TColgp.TColgp_SequenceOfPnt: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : IVtk_PolylineList,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : OCP.TColgp.TColgp_SequenceOfPnt,theIter : Any) -> OCP.TColgp.TColgp_SequenceOfPnt: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : IVtk_PolylineList,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.TColgp.TColgp_SequenceOfPnt: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.TColgp.TColgp_SequenceOfPnt) -> OCP.TColgp.TColgp_SequenceOfPnt: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : IVtk_PolylineList) -> None: ...
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
    def __init__(self,theOther : IVtk_PolylineList) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class IVtk_ShapeTypeMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : IVtk_ShapeTypeMap) -> IVtk_ShapeTypeMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.IVtk.IVtk_MeshType) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.IVtk.IVtk_MeshType) -> OCP.IVtk.IVtk_MeshType: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.IVtk.IVtk_MeshType: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.IVtk.IVtk_MeshType: 
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
    def Exchange(self,theOther : IVtk_ShapeTypeMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.IVtk.IVtk_MeshType) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.IVtk.IVtk_MeshType: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.IVtk.IVtk_MeshType: 
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IVtk_ShapeTypeMap) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
