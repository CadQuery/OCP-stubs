import OCP.XCAFPrs
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.AIS
import OCP.PrsMgr
import OCP.TPrsStd
import OCP.NCollection
import io
import OCP.SelectMgr
import OCP.OSD
import OCP.Standard
import OCP.V3d
import OCP.TopoDS
import OCP.Prs3d
import OCP.XCAFDoc
import OCP.TDF
import OCP.Quantity
import OCP.Bnd
import OCP.TDocStd
import OCP.TopLoc
import OCP.Graphic3d
import OCP.gp
import OCP.Image
import OCP.TopAbs
import OCP.Aspect
import OCP.TCollection
import OCP.TColStd
__all__  = [
"XCAFPrs",
"XCAFPrs_AISObject",
"XCAFPrs_DataMapOfStyleShape",
"XCAFPrs_DocumentExplorer",
"XCAFPrs_DocumentIdIterator",
"XCAFPrs_DocumentNode",
"XCAFPrs_Driver",
"XCAFPrs_IndexedDataMapOfShapeStyle",
"XCAFPrs_Style",
"XCAFPrs_Texture",
"XCAFPrs_DocumentExplorerFlags_NoStyle",
"XCAFPrs_DocumentExplorerFlags_None",
"XCAFPrs_DocumentExplorerFlags_OnlyLeafNodes"
]
class XCAFPrs():
    """
    Presentation (visualiation, selection etc.) tools for DECAF documents
    """
    @staticmethod
    def CollectStyleSettings_s(L : OCP.TDF.TDF_Label,loc : OCP.TopLoc.TopLoc_Location,settings : XCAFPrs_IndexedDataMapOfShapeStyle,theLayerColor : OCP.Quantity.Quantity_ColorRGBA=OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Collect styles defined for shape on label L and its components and subshapes and fills a map of shape - style correspondence The location <loc> is for internal use, it should be Null location for external call
        """
    @staticmethod
    def GetViewNameMode_s() -> bool: 
        """
        None
        """
    @staticmethod
    def SetViewNameMode_s(viewNameMode : bool) -> None: 
        """
        Set ViewNameMode for indicate display names or not.
        """
    def __init__(self) -> None: ...
    pass
class XCAFPrs_AISObject(OCP.AIS.AIS_ColoredShape, OCP.AIS.AIS_Shape, OCP.AIS.AIS_InteractiveObject, OCP.SelectMgr.SelectMgr_SelectableObject, OCP.PrsMgr.PrsMgr_PresentableObject, OCP.Standard.Standard_Transient):
    """
    Implements AIS_InteractiveObject functionality for shape in DECAF document.Implements AIS_InteractiveObject functionality for shape in DECAF document.
    """
    def AcceptDisplayMode(self,theMode : int) -> bool: 
        """
        Return true if specified display mode is supported.
        """
    def AcceptShapeDecomposition(self) -> bool: 
        """
        Returns true if the Interactive Object accepts shape decomposition.
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
    def BoundingBox(self) -> OCP.Bnd.Bnd_Box: 
        """
        Constructs a bounding box with which to reconstruct compound topological shapes for presentation.
        """
    def ChangeCustomAspectsMap(self) -> Any: 
        """
        Return the map of custom aspects.
        """
    def Children(self) -> OCP.PrsMgr.PrsMgr_ListOfPresentableObjects: 
        """
        Returns children of the current object.
        """
    def ClearCustomAspects(self) -> None: 
        """
        Reset the map of custom sub-shape aspects.
        """
    def ClearDynamicHighlight(self,theMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> None: 
        """
        Method that needs to be implemented when the object manages selection and dynamic highlighting on its own. Clears or invalidates dynamic highlight presentation. By default it clears immediate draw of given presentation manager.
        """
    def ClearOwner(self) -> None: 
        """
        Each Interactive Object has methods which allow us to attribute an Owner to it in the form of a Transient. This method removes the owner from the graphic entity.
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
    def Color(self,aColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns the Color attributes of the shape accordingly to the current facing model;
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
    def CustomAspects(self,theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.AIS.AIS_ColoredDrawer: 
        """
        Customize properties of specified sub-shape. The shape will be stored in the map but ignored, if it is not sub-shape of main Shape! This method can be used to mark sub-shapes with customizable properties.
        """
    def CustomAspectsMap(self) -> Any: 
        """
        Return the map of custom aspects.
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
    def DispatchStyles(self,theToSyncStyles : bool=False) -> None: 
        """
        Fetch the Shape from associated Label and fill the map of sub-shapes styles. By default, this method is called implicitly within first ::Compute(). Application might call this method explicitly to manipulate styles afterwards.
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
    def GetContext(self) -> OCP.AIS.AIS_InteractiveContext: 
        """
        Returns the context pointer to the interactive context.
        """
    def GetHilightPresentation(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Creates or returns existing presentation for highlighting detected object.
        """
    def GetLabel(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label which was visualised by this presentation
        """
    def GetOwner(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the owner of the Interactive Object. The owner can be a shape for a set of sub-shapes or a sub-shape for sub-shapes which it is composed of, and takes the form of a transient. There are two types of owners: - Direct owners, decomposition shapes such as edges, wires, and faces. - Users, presentable objects connecting to sensitive primitives, or a shape which has been decomposed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSelectPresentation(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Creates or returns existing presentation for highlighting selected object.
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
    def HasInteractiveContext(self) -> bool: 
        """
        Indicates whether the Interactive Object has a pointer to an interactive context.
        """
    def HasMaterial(self) -> bool: 
        """
        Returns true if the Interactive Object has a setting for material.
        """
    def HasOwnPresentations(self) -> bool: 
        """
        Returns true if object should have own presentations.
        """
    def HasOwner(self) -> bool: 
        """
        Returns true if the object has an owner attributed to it. The owner can be a shape for a set of sub-shapes or a sub-shape for sub-shapes which it is composed of, and takes the form of a transient.
        """
    def HasPolygonOffsets(self) -> bool: 
        """
        Returns Standard_True if <myDrawer> has non-null shading aspect
        """
    def HasPresentation(self) -> bool: 
        """
        Returns TRUE when this object has a presentation in the current DisplayMode()
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
    def InteractiveContext(self) -> OCP.AIS.AIS_InteractiveContext: 
        """
        Returns the context pointer to the interactive context.
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
        Returns the NameOfMaterial attributes of the shape accordingly to the current facing model;
        """
    def OwnDeviationAngle(self,anAngle : float,aPreviousAngle : float) -> bool: 
        """
        Returns true and the values of the deviation angle anAngle and the previous deviation angle aPreviousAngle. If these values are not already set, false is returned.
        """
    def OwnDeviationCoefficient(self,aCoefficient : float,aPreviousCoefficient : float) -> bool: 
        """
        Returns true and the values of the deviation coefficient aCoefficient and the previous deviation coefficient aPreviousCoefficient. If these values are not already set, false is returned.
        """
    def Parent(self) -> OCP.PrsMgr.PrsMgr_PresentableObject: 
        """
        Returns parent of current object in scene hierarchy.
        """
    def PolygonOffsets(self,aFactor : float,aUnits : float) -> Tuple[int]: 
        """
        Retrieves current polygon offsets settings from <myDrawer>.
        """
    def Presentation(self) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Returns the current presentation of this object according to the current DisplayMode()
        """
    def Presentations(self) -> OCP.PrsMgr.PrsMgr_Presentations: 
        """
        Return presentations.
        """
    def ProcessDragging(self,theCtx : OCP.AIS.AIS_InteractiveContext,theView : OCP.V3d.V3d_View,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theDragFrom : OCP.Graphic3d.Graphic3d_Vec2i,theDragTo : OCP.Graphic3d.Graphic3d_Vec2i,theAction : OCP.AIS.AIS_DragAction) -> bool: 
        """
        Drag object in the viewer.
        """
    @overload
    def RecomputePrimitives(self,theMode : int) -> None: 
        """
        Re-computes the sensitive primitives for all modes. IMPORTANT: Do not use this method to update selection primitives except implementing custom selection manager! This method does not take into account necessary BVH updates, but may invalidate the pointers it refers to. TO UPDATE SELECTION properly from outside classes, use method UpdateSelection.

        Re-computes the sensitive primitives which correspond to the <theMode>th selection mode. IMPORTANT: Do not use this method to update selection primitives except implementing custom selection manager! selection manager! This method does not take into account necessary BVH updates, but may invalidate the pointers it refers to. TO UPDATE SELECTION properly from outside classes, use method UpdateSelection.
        """
    @overload
    def RecomputePrimitives(self) -> None: ...
    def Redisplay(self,AllModes : bool=False) -> None: 
        """
        Updates the active presentation; if <AllModes> = Standard_True all the presentations inside are recomputed. IMPORTANT: It is preferable to call Redisplay method of corresponding AIS_InteractiveContext instance for cases when it is accessible. This method just redirects call to myCTXPtr, so this class field must be up to date for proper result.
        """
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
    @staticmethod
    def SelectionMode_s(theShapeType : OCP.TopAbs.TopAbs_ShapeEnum) -> int: 
        """
        Return selection mode for specified shape type.
        """
    @staticmethod
    def SelectionType_s(theSelMode : int) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Return shape type for specified selection mode.
        """
    def Selections(self) -> OCP.SelectMgr.SelectMgr_SequenceOfSelection: 
        """
        Return the sequence of selections.
        """
    def Set(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Alias for ::SetShape().
        """
    def SetAngleAndDeviation(self,anAngle : float) -> None: 
        """
        this compute a new angle and Deviation from the value anAngle and set the values stored in myDrawer with these that become local to the shape
        """
    def SetAspect(self,anAspect : OCP.Prs3d.Prs3d_BasicAspect) -> None: 
        """
        Sets the graphic basic aspect to the current presentation.
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
        Setup color of entire shape.
        """
    def SetContext(self,aCtx : OCP.AIS.AIS_InteractiveContext) -> None: 
        """
        Sets the interactive context aCtx and provides a link to the default drawing tool or "Drawer" if there is none.
        """
    def SetCurrentFacingModel(self,theModel : OCP.Aspect.Aspect_TypeOfFacingModel=Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None: 
        """
        change the current facing model apply on polygons for SetColor(), SetTransparency(), SetMaterial() methods default facing model is Aspect_TOFM_TWO_SIDE. This mean that attributes is applying both on the front and back face.
        """
    def SetCustomColor(self,theShape : OCP.TopoDS.TopoDS_Shape,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Customize color of specified sub-shape
        """
    def SetCustomTransparency(self,theShape : OCP.TopoDS.TopoDS_Shape,theTransparency : float) -> None: 
        """
        Customize transparency of specified sub-shape
        """
    def SetCustomWidth(self,theShape : OCP.TopoDS.TopoDS_Shape,theLineWidth : float) -> None: 
        """
        Customize line width of specified sub-shape
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
    def SetLabel(self,theLabel : OCP.TDF.TDF_Label) -> None: 
        """
        Assign the label to this presentation (but does not mark it outdated with SetToUpdate()).
        """
    @overload
    def SetLocalTransformation(self,theTrsf : OCP.TopLoc.TopLoc_Datum3D) -> None: 
        """
        Sets local transformation to theTransformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.

        Sets local transformation to theTransformation. Note that the local transformation of the object having Transformation Persistence is applied within Local Coordinate system defined by this Persistence.
        """
    @overload
    def SetLocalTransformation(self,theTrsf : OCP.gp.gp_Trsf) -> None: ...
    def SetMaterial(self,theMaterial : OCP.Graphic3d.Graphic3d_MaterialAspect) -> None: 
        """
        Sets the material aspect. This method assigns the new default material without overriding XDE styles. Re-computation of existing presentation is not required after calling this method.
        """
    def SetMutable(self,theIsMutable : bool) -> None: 
        """
        Sets if the object has mutable nature (content or location will be changed regularly). This method should be called before object displaying to take effect.
        """
    @overload
    def SetOwnDeviationAngle(self) -> bool: 
        """
        Sets a local value for deviation angle for this specific shape.

        sets myOwnDeviationAngle field in Prs3d_Drawer & recomputes presentation
        """
    @overload
    def SetOwnDeviationAngle(self,anAngle : float) -> None: ...
    @overload
    def SetOwnDeviationCoefficient(self) -> bool: 
        """
        Sets a local value for deviation coefficient for this specific shape.

        Sets a local value for deviation coefficient for this specific shape.
        """
    @overload
    def SetOwnDeviationCoefficient(self,aCoefficient : float) -> None: ...
    def SetOwner(self,theApplicativeEntity : OCP.Standard.Standard_Transient) -> None: 
        """
        Allows you to attribute the owner theApplicativeEntity to an Interactive Object. This can be a shape for a set of sub-shapes or a sub-shape for sub-shapes which it is composed of. The owner takes the form of a transient.
        """
    def SetPolygonOffsets(self,aMode : int,aFactor : float=1.0,aUnits : float=0.0) -> None: 
        """
        Sets up polygon offsets for this object.
        """
    def SetPropagateVisualState(self,theFlag : bool) -> None: 
        """
        Change the value of the flag "propagate visual state"
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Constructs an instance of the shape object theShape.
        """
    def SetTextureOriginUV(self,theOriginUV : OCP.gp.gp_Pnt2d) -> None: 
        """
        Use this method to change the origin of the texture. The texel (0,0) will be mapped to the surface (myUVOrigin.X(), myUVOrigin.Y()).
        """
    def SetTextureRepeatUV(self,theRepeatUV : OCP.gp.gp_Pnt2d) -> None: 
        """
        Sets the number of occurrences of the texture on each face. The texture itself is parameterized in (0,1) by (0,1). Each face of the shape to be textured is parameterized in UV space (Umin,Umax) by (Vmin,Vmax).
        """
    def SetTextureScaleUV(self,theScaleUV : OCP.gp.gp_Pnt2d) -> None: 
        """
        Use this method to scale the texture (percent of the face). You can specify a scale factor for both U and V. Example: if you set ScaleU and ScaleV to 0.5 and you enable texture repeat, the texture will appear twice on the face in each direction.
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
    def SetTransparency(self,theValue : float) -> None: 
        """
        Sets transparency value.
        """
    def SetTypeOfHLR(self,theTypeOfHLR : OCP.Prs3d.Prs3d_TypeOfHLR) -> None: 
        """
        Sets the type of HLR algorithm used by the shape
        """
    def SetTypeOfPresentation(self,theType : OCP.PrsMgr.PrsMgr_TypeOfPresentation3d) -> None: 
        """
        Set type of presentation.
        """
    def SetWidth(self,theLineWidth : float) -> None: 
        """
        Setup line width of entire shape.
        """
    def SetZLayer(self,theLayerId : int) -> None: 
        """
        Set Z layer ID and update all presentations of the selectable object. The layers mechanism allows drawing objects in higher layers in overlay of objects in lower layers.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns this shape object.
        """
    def Signature(self) -> int: 
        """
        Returns index 0. This value refers to SHAPE from TopAbs_ShapeEnum
        """
    def SynchronizeAspects(self) -> None: 
        """
        Synchronize presentation aspects after their modification.
        """
    def TextureOriginUV(self) -> OCP.gp.gp_Pnt2d: 
        """
        Return texture origin UV position; (0, 0) by default.
        """
    def TextureRepeatUV(self) -> OCP.gp.gp_Pnt2d: 
        """
        Return texture repeat UV values; (1, 1) by default.
        """
    def TextureScaleUV(self) -> OCP.gp.gp_Pnt2d: 
        """
        Return scale factor for UV coordinates; (1, 1) by default.
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
        Returns the transparency attributes of the shape accordingly to the current facing model;
        """
    def Type(self) -> OCP.AIS.AIS_KindOfInteractive: 
        """
        Returns Object as the type of Interactive Object.
        """
    def TypeOfHLR(self) -> OCP.Prs3d.Prs3d_TypeOfHLR: 
        """
        Gets the type of HLR algorithm
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
        Removes settings for color in the reconstructed compound shape.
        """
    def UnsetCustomAspects(self,theShape : OCP.TopoDS.TopoDS_Shape,theToUnregister : bool=False) -> None: 
        """
        Reset custom properties of specified sub-shape.
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
        Removes settings for material in the reconstructed compound shape.
        """
    def UnsetTransparency(self) -> None: 
        """
        Removes the setting for transparency in the reconstructed compound shape.
        """
    def UnsetWidth(self) -> None: 
        """
        Setup line width of entire shape.
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
    def UserAngle(self) -> float: 
        """
        gives back the angle initial value put by the User.
        """
    def Width(self) -> float: 
        """
        Returns the width setting of the Interactive Object.
        """
    def ZLayer(self) -> int: 
        """
        Get ID of Z layer for main presentation.
        """
    def __init__(self,theLabel : OCP.TDF.TDF_Label) -> None: ...
    @staticmethod
    def computeHlrPresentation_s(theProjector : OCP.Graphic3d.Graphic3d_Camera,thePrs : OCP.Graphic3d.Graphic3d_Structure,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Compute HLR presentation for specified shape.
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
class XCAFPrs_DataMapOfStyleShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : XCAFPrs_DataMapOfStyleShape) -> XCAFPrs_DataMapOfStyleShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : XCAFPrs_Style,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : XCAFPrs_Style,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : XCAFPrs_Style) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : XCAFPrs_Style) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Exchange(self,theOther : XCAFPrs_DataMapOfStyleShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : XCAFPrs_Style) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : XCAFPrs_Style,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def IsBound(self,theKey : XCAFPrs_Style) -> bool: 
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
    def Seek(self,theKey : XCAFPrs_Style) -> OCP.TopoDS.TopoDS_Shape: 
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
    def UnBind(self,theKey : XCAFPrs_Style) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : XCAFPrs_DataMapOfStyleShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class XCAFPrs_DocumentExplorer():
    """
    Document iterator through shape nodes.
    """
    def ChangeCurrent(self) -> XCAFPrs_DocumentNode: 
        """
        Return current position.
        """
    def ColorTool(self) -> OCP.XCAFDoc.XCAFDoc_ColorTool: 
        """
        Return color tool.
        """
    @overload
    def Current(self) -> XCAFPrs_DocumentNode: 
        """
        Return current position within specified assembly depth.

        Return current position.
        """
    @overload
    def Current(self,theDepth : int) -> XCAFPrs_DocumentNode: ...
    def CurrentDepth(self) -> int: 
        """
        Return depth of the current node in hierarchy, starting from 0. Zero means Root label.
        """
    @staticmethod
    def DefineChildId_s(theLabel : OCP.TDF.TDF_Label,theParentId : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Construct a unique string identifier for the given label. The identifier is a concatenation of label entries (TDF_Tool::Entry() with tailing '.') of hierarchy from parent to child joined via '/' and looking like this: This generation scheme also allows finding originating labels using TDF_Tool::Label(). The tailing dot simplifies parent equality check.
        """
    @staticmethod
    @overload
    def FindLabelFromPathId_s(theDocument : OCP.TDocStd.TDocStd_Document,theId : OCP.TCollection.TCollection_AsciiString,theParentLocation : OCP.TopLoc.TopLoc_Location,theLocation : OCP.TopLoc.TopLoc_Location) -> OCP.TDF.TDF_Label: 
        """
        Find a shape entity based on a text identifier constructed from OCAF labels defining full path.

        Find a shape entity based on a text identifier constructed from OCAF labels defining full path.
        """
    @staticmethod
    @overload
    def FindLabelFromPathId_s(theDocument : OCP.TDocStd.TDocStd_Document,theId : OCP.TCollection.TCollection_AsciiString,theLocation : OCP.TopLoc.TopLoc_Location) -> OCP.TDF.TDF_Label: ...
    @staticmethod
    def FindShapeFromPathId_s(theDocument : OCP.TDocStd.TDocStd_Document,theId : OCP.TCollection.TCollection_AsciiString) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Find a shape entity based on a text identifier constructed from OCAF labels defining full path.
        """
    @overload
    def Init(self,theDocument : OCP.TDocStd.TDocStd_Document,theRoots : OCP.TDF.TDF_LabelSequence,theFlags : int,theDefStyle : XCAFPrs_Style=XCAFPrs_Style) -> None: 
        """
        Initialize the iterator from a single root shape in the document.

        Initialize the iterator from the list of root shapes in the document.
        """
    @overload
    def Init(self,theDocument : OCP.TDocStd.TDocStd_Document,theRoot : OCP.TDF.TDF_Label,theFlags : int,theDefStyle : XCAFPrs_Style=XCAFPrs_Style) -> None: ...
    def More(self) -> bool: 
        """
        Return TRUE if iterator points to the valid node.
        """
    def Next(self) -> None: 
        """
        Go to the next node.
        """
    def VisMaterialTool(self) -> OCP.XCAFDoc.XCAFDoc_VisMaterialTool: 
        """
        Return material tool.
        """
    @overload
    def __init__(self,theDocument : OCP.TDocStd.TDocStd_Document,theFlags : int,theDefStyle : XCAFPrs_Style=XCAFPrs_Style) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theDocument : OCP.TDocStd.TDocStd_Document,theRoots : OCP.TDF.TDF_LabelSequence,theFlags : int,theDefStyle : XCAFPrs_Style=XCAFPrs_Style) -> None: ...
    pass
class XCAFPrs_DocumentIdIterator():
    """
    Auxiliary tool for iterating through Path identification string.
    """
    def More(self) -> bool: 
        """
        Return TRUE if iterator points to a value.
        """
    def Next(self) -> None: 
        """
        Find the next value.

        Find the next value.
        """
    def Value(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return current value.
        """
    def __init__(self,thePath : OCP.TCollection.TCollection_AsciiString) -> None: ...
    pass
class XCAFPrs_DocumentNode():
    """
    Structure defining document node.
    """
    @staticmethod
    def HashCode_s(theNode : XCAFPrs_DocumentNode,theN : int) -> int: 
        """
        Return hash code based on node string identifier.
        """
    @staticmethod
    def IsEqual_s(theNode1 : XCAFPrs_DocumentNode,theNode2 : XCAFPrs_DocumentNode) -> bool: 
        """
        Return TRUE if two document nodes has the same string identifier.
        """
    def __init__(self) -> None: ...
    @property
    def ChildIter(self) -> OCP.TDF.TDF_ChildIterator:
        """
        :type: OCP.TDF.TDF_ChildIterator
        """
    @ChildIter.setter
    def ChildIter(self, arg0: OCP.TDF.TDF_ChildIterator) -> None:
        pass
    @property
    def Id(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @Id.setter
    def Id(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    @property
    def IsAssembly(self) -> bool:
        """
        :type: bool
        """
    @IsAssembly.setter
    def IsAssembly(self, arg0: bool) -> None:
        pass
    @property
    def Label(self) -> OCP.TDF.TDF_Label:
        """
        :type: OCP.TDF.TDF_Label
        """
    @Label.setter
    def Label(self, arg0: OCP.TDF.TDF_Label) -> None:
        pass
    @property
    def LocalTrsf(self) -> OCP.TopLoc.TopLoc_Location:
        """
        :type: OCP.TopLoc.TopLoc_Location
        """
    @LocalTrsf.setter
    def LocalTrsf(self, arg0: OCP.TopLoc.TopLoc_Location) -> None:
        pass
    @property
    def Location(self) -> OCP.TopLoc.TopLoc_Location:
        """
        :type: OCP.TopLoc.TopLoc_Location
        """
    @Location.setter
    def Location(self, arg0: OCP.TopLoc.TopLoc_Location) -> None:
        pass
    @property
    def RefLabel(self) -> OCP.TDF.TDF_Label:
        """
        :type: OCP.TDF.TDF_Label
        """
    @RefLabel.setter
    def RefLabel(self, arg0: OCP.TDF.TDF_Label) -> None:
        pass
    @property
    def Style(self) -> XCAFPrs_Style:
        """
        :type: XCAFPrs_Style
        """
    @Style.setter
    def Style(self, arg0: XCAFPrs_Style) -> None:
        pass
    pass
class XCAFPrs_Driver(OCP.TPrsStd.TPrsStd_Driver, OCP.Standard.Standard_Transient):
    """
    Implements a driver for presentation of shapes in DECAF document. Its the only purpose is to initialize and return XCAFPrs_AISObject object on requestImplements a driver for presentation of shapes in DECAF document. Its the only purpose is to initialize and return XCAFPrs_AISObject object on requestImplements a driver for presentation of shapes in DECAF document. Its the only purpose is to initialize and return XCAFPrs_AISObject object on request
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
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        returns GUID of the driver
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
    def Update(self,L : OCP.TDF.TDF_Label,ais : OCP.AIS.AIS_InteractiveObject) -> bool: 
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
class XCAFPrs_IndexedDataMapOfShapeStyle(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : XCAFPrs_Style) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : XCAFPrs_IndexedDataMapOfShapeStyle) -> XCAFPrs_IndexedDataMapOfShapeStyle: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> XCAFPrs_Style: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> XCAFPrs_Style: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> XCAFPrs_Style: 
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
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : XCAFPrs_IndexedDataMapOfShapeStyle) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> XCAFPrs_Style: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> XCAFPrs_Style: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : XCAFPrs_Style) -> bool: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
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
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> XCAFPrs_Style: 
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
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : XCAFPrs_Style) -> None: 
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
    def __init__(self,theOther : XCAFPrs_IndexedDataMapOfShapeStyle) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class XCAFPrs_Style():
    """
    Represents a set of styling settings applicable to a (sub)shape
    """
    def BaseColorTexture(self) -> OCP.Image.Image_Texture: 
        """
        Return base color texture.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetColorCurv(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return curve color.
        """
    def GetColorSurf(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return surface color.
        """
    def GetColorSurfRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return surface color.
        """
    @staticmethod
    def HashCode_s(theStyle : XCAFPrs_Style,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given set of styling settings, in the range [1, theUpperBound]
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if style is empty - does not override any properties.
        """
    def IsEqual(self,theOther : XCAFPrs_Style) -> bool: 
        """
        Returns True if styles are the same Methods for using Style as key in maps
        """
    @staticmethod
    def IsEqual_s(theS1 : XCAFPrs_Style,theS2 : XCAFPrs_Style) -> bool: 
        """
        Returns True when the two keys are the same.
        """
    def IsSetColorCurv(self) -> bool: 
        """
        Return TRUE if curve color has been defined.
        """
    def IsSetColorSurf(self) -> bool: 
        """
        Return TRUE if surface color has been defined.
        """
    def IsVisible(self) -> bool: 
        """
        Manage visibility.
        """
    def Material(self) -> OCP.XCAFDoc.XCAFDoc_VisMaterial: 
        """
        Return material.
        """
    def SetColorCurv(self,col : OCP.Quantity.Quantity_Color) -> None: 
        """
        Set curve color.
        """
    @overload
    def SetColorSurf(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Set surface color.

        Set surface color.
        """
    @overload
    def SetColorSurf(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetMaterial(self,theMaterial : OCP.XCAFDoc.XCAFDoc_VisMaterial) -> None: 
        """
        Set material.
        """
    def SetVisibility(self,theVisibility : bool) -> None: 
        """
        Assign visibility.
        """
    def UnSetColorCurv(self) -> None: 
        """
        Manage curve color setting
        """
    def UnSetColorSurf(self) -> None: 
        """
        Manage surface color setting
        """
    def __init__(self) -> None: ...
    pass
class XCAFPrs_Texture(OCP.Graphic3d.Graphic3d_Texture2Dmanual, OCP.Graphic3d.Graphic3d_Texture2D, OCP.Graphic3d.Graphic3d_TextureMap, OCP.Graphic3d.Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    Texture holder.
    """
    def AnisoFilter(self) -> OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisotropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetCompressedImage(self,theSupported : OCP.Image.Image_SupportedFormats) -> OCP.Image.Image_CompressedPixMap: 
        """
        Image reader.
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self,theSupported : OCP.Image.Image_SupportedFormats) -> OCP.Image.Image_PixMap: 
        """
        Image reader.
        """
    def GetImageSource(self) -> OCP.Image.Image_Texture: 
        """
        Return image source.
        """
    def GetParams(self) -> OCP.Graphic3d.Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasMipMaps(self) -> bool: 
        """
        Return true if mip-maps should be used.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsColorMap(self) -> bool: 
        """
        Return flag indicating color nature of values within the texture; TRUE by default.
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
    def IsModulate(self) -> bool: 
        """
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def IsTopDown(self) -> bool: 
        """
        Returns whether row's memory layout is top-down.
        """
    def Name(self) -> OCP.Graphic3d.Graphic3d_NameOfTexture2D: 
        """
        Returns the name of the predefined textures or NOT_2D_UNKNOWN when the name is given as a filename.
        """
    @staticmethod
    def NumberOfTextures_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetColorMap(self,theIsColor : bool) -> None: 
        """
        Set flag indicating color nature of values within the texture.
        """
    def SetImage(self,thePixMap : OCP.Image.Image_PixMap) -> None: 
        """
        Assign new image to the texture. Note that this method does not invalidate already uploaded resources - consider calling ::UpdateRevision() if needed.
        """
    def SetMipMaps(self,theToUse : bool) -> None: 
        """
        Set if mip-maps should be used (generated if needed). Note that this method should be called before loading / using the texture.
        """
    @staticmethod
    def TextureName_s(theRank : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the predefined texture of rank <aRank>
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.Graphic3d.Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    def __init__(self,theImageSource : OCP.Image.Image_Texture,theUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> None: ...
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
XCAFPrs_DocumentExplorerFlags_NoStyle = 2
XCAFPrs_DocumentExplorerFlags_None = 0
XCAFPrs_DocumentExplorerFlags_OnlyLeafNodes = 1
