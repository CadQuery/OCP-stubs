import OCP.StdSelect
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.PrsMgr
import io
import OCP.SelectMgr
import OCP.Standard
import OCP.V3d
import OCP.TopoDS
import OCP.Prs3d
import OCP.Select3D
import OCP.Quantity
import OCP.Bnd
import OCP.TopLoc
import OCP.Graphic3d
import OCP.gp
import OCP.TopAbs
import OCP.Aspect
import OCP.TColStd
__all__  = [
"StdSelect",
"StdSelect_BRepOwner",
"StdSelect_BRepSelectionTool",
"StdSelect_EdgeFilter",
"StdSelect_FaceFilter",
"StdSelect_Shape",
"StdSelect_ShapeTypeFilter",
"StdSelect_TypeOfEdge",
"StdSelect_TypeOfFace",
"StdSelect_TypeOfSelectionImage",
"StdSelect_AnyEdge",
"StdSelect_AnyFace",
"StdSelect_Circle",
"StdSelect_Cone",
"StdSelect_Cylinder",
"StdSelect_Line",
"StdSelect_Plane",
"StdSelect_Revol",
"StdSelect_Sphere",
"StdSelect_Torus",
"StdSelect_TypeOfSelectionImage_ColoredDetectedObject",
"StdSelect_TypeOfSelectionImage_ColoredEntity",
"StdSelect_TypeOfSelectionImage_ColoredEntityType",
"StdSelect_TypeOfSelectionImage_ColoredOwner",
"StdSelect_TypeOfSelectionImage_ColoredSelectionMode",
"StdSelect_TypeOfSelectionImage_NormalizedDepth",
"StdSelect_TypeOfSelectionImage_NormalizedDepthInverted",
"StdSelect_TypeOfSelectionImage_SurfaceNormal",
"StdSelect_TypeOfSelectionImage_UnnormalizedDepth"
]
class StdSelect():
    """
    The StdSelect package provides the following services - the definition of selection modes for topological shapes - the definition of several concrete filtertandard Selection2d.ap classes - 2D and 3D viewer selectors. Note that each new Interactive Object must have all its selection modes defined. Standard Classes is useful to build 3D Selectable Objects, and to process 3D Selections:
    """
    @staticmethod
    def SetDrawerForBRepOwner_s(aSelection : OCP.SelectMgr.SelectMgr_Selection,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        puts The same drawer in every BRepOwner Of SensitivePrimitive Used Only for hilight Of BRepOwner...
        """
    def __init__(self) -> None: ...
    pass
class StdSelect_BRepOwner(OCP.SelectMgr.SelectMgr_EntityOwner, OCP.Standard.Standard_Transient):
    """
    Defines Specific Owners for Sensitive Primitives (Sensitive Segments,Circles...). Used in Dynamic Selection Mechanism. A BRepOwner has an Owner (the shape it represents) and Users (One or More Transient entities). The highlight-unhighlight methods are empty and must be redefined by each User.Defines Specific Owners for Sensitive Primitives (Sensitive Segments,Circles...). Used in Dynamic Selection Mechanism. A BRepOwner has an Owner (the shape it represents) and Users (One or More Transient entities). The highlight-unhighlight methods are empty and must be redefined by each User.
    """
    def Clear(self,aPM : OCP.PrsMgr.PrsMgr_PresentationManager,aMode : int=0) -> None: 
        """
        Clears the presentation manager object aPM of all shapes with the selection mode aMode.
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
    def HasHilightMode(self) -> bool: 
        """
        Returns true if this framework has a highlight mode defined for it.
        """
    def HasLocation(self) -> bool: 
        """
        Returns TRUE if selectable has transformation.
        """
    def HasSelectable(self) -> bool: 
        """
        Returns true if there is a selectable object to serve as an owner.
        """
    def HasShape(self) -> bool: 
        """
        returns False if no shape was set
        """
    def HilightMode(self) -> int: 
        """
        Returns the highlight mode for this framework. This defines the type of display used to highlight the owner of the shape when it is detected by the selector. The default type of display is wireframe, defined by the index 0.
        """
    def HilightWithColor(self,thePM : OCP.PrsMgr.PrsMgr_PresentationManager,theStyle : OCP.Prs3d.Prs3d_Drawer,theMode : int) -> None: 
        """
        None
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
    def IsHilighted(self,aPM : OCP.PrsMgr.PrsMgr_PresentationManager,aMode : int=0) -> bool: 
        """
        Returns true if an object with the selection mode aMode is highlighted in the presentation manager aPM.
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
    def IsSameSelectable(self,theOther : OCP.SelectMgr.SelectMgr_SelectableObject) -> bool: 
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
    def ResetHilightMode(self) -> None: 
        """
        Resets the higlight mode for this framework. This defines the type of display used to highlight the owner of the shape when it is detected by the selector. The default type of display is wireframe, defined by the index 0.
        """
    def Selectable(self) -> OCP.SelectMgr.SelectMgr_SelectableObject: 
        """
        Returns a selectable object detected in the working context.
        """
    @overload
    def Set(self,thePriority : int) -> None: 
        """
        Sets the selectable object.

        sets the selectable priority of the owner
        """
    @overload
    def Set(self,theSelObj : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: ...
    def SetComesFromDecomposition(self,theIsFromDecomposition : bool) -> None: 
        """
        Sets flag indicating this owner points to a part of object (TRUE) or to entire object (FALSE).
        """
    def SetHilightMode(self,theMode : int) -> None: 
        """
        Sets the highlight mode for this framework. This defines the type of display used to highlight the owner of the shape when it is detected by the selector. The default type of display is wireframe, defined by the index 0.
        """
    def SetLocation(self,aLoc : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None
        """
    def SetPriority(self,thePriority : int) -> None: 
        """
        Sets the selectable priority of the owner within range [0-9].
        """
    def SetSelectable(self,theSelObj : OCP.SelectMgr.SelectMgr_SelectableObject) -> None: 
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
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape.
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
    def Unhilight(self,aPM : OCP.PrsMgr.PrsMgr_PresentationManager,aMode : int=0) -> None: 
        """
        Removes highlighting from the type of shape identified the selection mode aMode in the presentation manager aPM.
        """
    def UpdateHighlightTrsf(self,theViewer : OCP.V3d.V3d_Viewer,theManager : OCP.PrsMgr.PrsMgr_PresentationManager,theDispMode : int) -> None: 
        """
        Implements immediate application of location transformation of parent object to dynamic highlight structure
        """
    @overload
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape,aPriority : int=0,ComesFromDecomposition : bool=False) -> None: ...
    @overload
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape,theOrigin : OCP.SelectMgr.SelectMgr_SelectableObject,aPriority : int=0,FromDecomposition : bool=False) -> None: ...
    @overload
    def __init__(self,aPriority : int) -> None: ...
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
class StdSelect_BRepSelectionTool():
    """
    Tool to create specific selections (sets of primitives) for Shapes from Topology. These Selections may be used in dynamic selection Mechanism Given a Shape and a mode of selection (selection of vertices, edges,faces ...) , This Tool Computes corresponding sensitive primitives, puts them in an entity called Selection (see package SelectMgr) and returns it.
    """
    @staticmethod
    def ComputeSensitive_s(theShape : OCP.TopoDS.TopoDS_Shape,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theSelection : OCP.SelectMgr.SelectMgr_Selection,theDeflection : float,theDeflAngle : float,theNbPOnEdge : int,theMaxiParam : float,theAutoTriang : bool=True) -> None: 
        """
        Computes the sensitive primitives, stores them in the SelectMgr_Selection object, and returns this object.
        """
    @staticmethod
    def GetEdgeSensitive_s(theShape : OCP.TopoDS.TopoDS_Shape,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theSelection : OCP.SelectMgr.SelectMgr_Selection,theDeflection : float,theDeviationAngle : float,theNbPOnEdge : int,theMaxiParam : float,theSensitive : OCP.Select3D.Select3D_SensitiveEntity) -> None: 
        """
        Create a sensitive edge or sensitive wire.
        """
    @staticmethod
    def GetSensitiveForFace_s(theFace : OCP.TopoDS.TopoDS_Face,theOwner : OCP.SelectMgr.SelectMgr_EntityOwner,theOutList : OCP.Select3D.Select3D_EntitySequence,theAutoTriang : bool=True,theNbPOnEdge : int=9,theMaxiParam : float=500.0,theInteriorFlag : bool=True) -> bool: 
        """
        Creates the 3D sensitive entities for Face selection.
        """
    @staticmethod
    def GetStandardPriority_s(theShape : OCP.TopoDS.TopoDS_Shape,theType : OCP.TopAbs.TopAbs_ShapeEnum) -> int: 
        """
        Returns the standard priority of the shape aShap having the type aType. This priority is passed to a StdSelect_BRepOwner object. You can use the function Load to modify the selection priority of an owner to make one entity more selectable than another one.
        """
    @staticmethod
    @overload
    def Load_s(aSelection : OCP.SelectMgr.SelectMgr_Selection,Origin : OCP.SelectMgr.SelectMgr_SelectableObject,aShape : OCP.TopoDS.TopoDS_Shape,aType : OCP.TopAbs.TopAbs_ShapeEnum,theDeflection : float,theDeviationAngle : float,AutoTriangulation : bool=True,aPriority : int=-1,NbPOnEdge : int=9,MaximalParameter : float=500.0) -> None: 
        """
        Decomposition of <aShape> into sensitive entities following a mode of decomposition <aType>. These entities are stored in <aSelection>. BrepOwners are created to store the identity of the picked shapes during the selection process. In those BRepOwners is also stored the original shape. But One can't get the selectable object which was decomposed to give the sensitive entities. maximal parameter is used for infinite objects, to limit the sensitive Domain.... If AutoTriangulation = True, a Triangulation will be computed for faces which have no existing one. if AutoTriangulation = False the old algorithm will be called to compute sensitive entities on faces.

        Same functionalities ; the only difference is that the selectable object from which the selection comes is stored in each Sensitive EntityOwner; decomposition of <aShape> into sensitive entities following a mode of decomposition <aType>. These entities are stored in <aSelection> The Major difference is that the known users are first inserted in the BRepOwners. the original shape is the last user... (see EntityOwner from SelectBasics and BrepOwner)...
        """
    @staticmethod
    @overload
    def Load_s(aSelection : OCP.SelectMgr.SelectMgr_Selection,aShape : OCP.TopoDS.TopoDS_Shape,aType : OCP.TopAbs.TopAbs_ShapeEnum,theDeflection : float,theDeviationAngle : float,AutoTriangulation : bool=True,aPriority : int=-1,NbPOnEdge : int=9,MaximalParameter : float=500.0) -> None: ...
    @staticmethod
    def PreBuildBVH_s(theSelection : OCP.SelectMgr.SelectMgr_Selection) -> None: 
        """
        Traverses the selection given and pre-builds BVH trees for heavyweight sensitive entities containing more than BVH_PRIMITIVE_LIMIT (defined in .cxx file) sub-elements.
        """
    def __init__(self) -> None: ...
    pass
class StdSelect_EdgeFilter(OCP.SelectMgr.SelectMgr_Filter, OCP.Standard.Standard_Transient):
    """
    A framework to define a filter to select a specific type of edge. The types available include: - any edge - a linear edge - a circular edge.A framework to define a filter to select a specific type of edge. The types available include: - any edge - a linear edge - a circular edge.A framework to define a filter to select a specific type of edge. The types available include: - any edge - a linear edge - a circular edge.
    """
    def ActsOn(self,aStandardMode : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
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
    def IsOk(self,anobj : OCP.SelectMgr.SelectMgr_EntityOwner) -> bool: 
        """
        None
        """
    def SetType(self,aNewType : StdSelect_TypeOfEdge) -> None: 
        """
        Sets the type of edge aNewType. aNewType is to be highlighted in selection.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> StdSelect_TypeOfEdge: 
        """
        Returns the type of edge to be highlighted in selection.
        """
    def __init__(self,Edge : StdSelect_TypeOfEdge) -> None: ...
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
class StdSelect_FaceFilter(OCP.SelectMgr.SelectMgr_Filter, OCP.Standard.Standard_Transient):
    """
    A framework to define a filter to select a specific type of face. The types available include: - any face - a planar face - a cylindrical face - a spherical face - a toroidal face - a revol face.A framework to define a filter to select a specific type of face. The types available include: - any face - a planar face - a cylindrical face - a spherical face - a toroidal face - a revol face.A framework to define a filter to select a specific type of face. The types available include: - any face - a planar face - a cylindrical face - a spherical face - a toroidal face - a revol face.
    """
    def ActsOn(self,aStandardMode : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
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
    def IsOk(self,anobj : OCP.SelectMgr.SelectMgr_EntityOwner) -> bool: 
        """
        None
        """
    def SetType(self,aNewType : StdSelect_TypeOfFace) -> None: 
        """
        Sets the type of face aNewType. aNewType is to be highlighted in selection.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> StdSelect_TypeOfFace: 
        """
        Returns the type of face to be highlighted in selection.
        """
    def __init__(self,aTypeOfFace : StdSelect_TypeOfFace) -> None: ...
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
class StdSelect_Shape(OCP.PrsMgr.PrsMgr_PresentableObject, OCP.Standard.Standard_Transient):
    """
    Presentable shape only for purpose of display for BRepOwner...Presentable shape only for purpose of display for BRepOwner...
    """
    def AcceptDisplayMode(self,theMode : int) -> bool: 
        """
        Returns true if the class of objects accepts specified display mode index. The interactive context can have a default mode of representation for the set of Interactive Objects. This mode may not be accepted by a given class of objects. Consequently, this virtual method allowing us to get information about the class in question must be implemented. At least one display mode index should be accepted by this method. Although subclass can leave default implementation, it is highly desired defining exact list of supported modes instead, which is usually an enumeration for one object or objects class sharing similar list of display modes.
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
    def Attributes(self) -> OCP.Prs3d.Prs3d_Drawer: 
        """
        Returns the attributes settings.
        """
    def BoundingBox(self,theBndBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        Returns bounding box of object correspondingly to its current display mode. This method requires presentation to be already computed, since it relies on bounding box of presentation structures, which are supposed to be same/close amongst different display modes of this object.
        """
    def Children(self) -> OCP.PrsMgr.PrsMgr_ListOfPresentableObjects: 
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
    def CombinedParentTransformation(self) -> OCP.TopLoc.TopLoc_Datum3D: 
        """
        Return combined parent transformation.
        """
    def Compute(self,thePrsMgr : OCP.PrsMgr.PrsMgr_PresentationManager,thePrs : OCP.Graphic3d.Graphic3d_Structure,theMode : int) -> None: 
        """
        None
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
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
        Returns the hilight attributes settings. When not NULL, overrides both Prs3d_TypeOfHighlight_LocalSelected and Prs3d_TypeOfHighlight_Selected defined within AIS_InteractiveContext::HighlightStyle().
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
        resets local transformation to identity.
        """
    def SetAttributes(self,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Initializes the drawing tool theDrawer.
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
        Set Z layer ID and update all presentations of the presentable object. The layers mechanism allows drawing objects in higher layers in overlay of objects in lower layers.
        """
    @overload
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    @overload
    def Shape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer=None) -> None: ...
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
class StdSelect_ShapeTypeFilter(OCP.SelectMgr.SelectMgr_Filter, OCP.Standard.Standard_Transient):
    """
    A filter framework which allows you to define a filter for a specific shape type.A filter framework which allows you to define a filter for a specific shape type.
    """
    def ActsOn(self,aStandardMode : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
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
    def IsOk(self,anobj : OCP.SelectMgr.SelectMgr_EntityOwner) -> bool: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the type of shape selected by the filter.
        """
    def __init__(self,aType : OCP.TopAbs.TopAbs_ShapeEnum) -> None: ...
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
class StdSelect_TypeOfEdge():
    """
    Provides values for different types of edges. These values are used to filter edges in frameworks inheriting StdSelect_EdgeFilter.

    Members:

      StdSelect_AnyEdge

      StdSelect_Line

      StdSelect_Circle
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
    StdSelect_AnyEdge: OCP.StdSelect.StdSelect_TypeOfEdge # value = <StdSelect_TypeOfEdge.StdSelect_AnyEdge: 0>
    StdSelect_Circle: OCP.StdSelect.StdSelect_TypeOfEdge # value = <StdSelect_TypeOfEdge.StdSelect_Circle: 2>
    StdSelect_Line: OCP.StdSelect.StdSelect_TypeOfEdge # value = <StdSelect_TypeOfEdge.StdSelect_Line: 1>
    __entries: dict # value = {'StdSelect_AnyEdge': (<StdSelect_TypeOfEdge.StdSelect_AnyEdge: 0>, None), 'StdSelect_Line': (<StdSelect_TypeOfEdge.StdSelect_Line: 1>, None), 'StdSelect_Circle': (<StdSelect_TypeOfEdge.StdSelect_Circle: 2>, None)}
    __members__: dict # value = {'StdSelect_AnyEdge': <StdSelect_TypeOfEdge.StdSelect_AnyEdge: 0>, 'StdSelect_Line': <StdSelect_TypeOfEdge.StdSelect_Line: 1>, 'StdSelect_Circle': <StdSelect_TypeOfEdge.StdSelect_Circle: 2>}
    pass
class StdSelect_TypeOfFace():
    """
    Provides values for different types of faces. These values are used to filter faces in frameworks inheriting StdSelect_FaceFilter.

    Members:

      StdSelect_AnyFace

      StdSelect_Plane

      StdSelect_Cylinder

      StdSelect_Sphere

      StdSelect_Torus

      StdSelect_Revol

      StdSelect_Cone
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
    StdSelect_AnyFace: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_AnyFace: 0>
    StdSelect_Cone: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Cone: 6>
    StdSelect_Cylinder: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Cylinder: 2>
    StdSelect_Plane: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Plane: 1>
    StdSelect_Revol: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Revol: 5>
    StdSelect_Sphere: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Sphere: 3>
    StdSelect_Torus: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Torus: 4>
    __entries: dict # value = {'StdSelect_AnyFace': (<StdSelect_TypeOfFace.StdSelect_AnyFace: 0>, None), 'StdSelect_Plane': (<StdSelect_TypeOfFace.StdSelect_Plane: 1>, None), 'StdSelect_Cylinder': (<StdSelect_TypeOfFace.StdSelect_Cylinder: 2>, None), 'StdSelect_Sphere': (<StdSelect_TypeOfFace.StdSelect_Sphere: 3>, None), 'StdSelect_Torus': (<StdSelect_TypeOfFace.StdSelect_Torus: 4>, None), 'StdSelect_Revol': (<StdSelect_TypeOfFace.StdSelect_Revol: 5>, None), 'StdSelect_Cone': (<StdSelect_TypeOfFace.StdSelect_Cone: 6>, None)}
    __members__: dict # value = {'StdSelect_AnyFace': <StdSelect_TypeOfFace.StdSelect_AnyFace: 0>, 'StdSelect_Plane': <StdSelect_TypeOfFace.StdSelect_Plane: 1>, 'StdSelect_Cylinder': <StdSelect_TypeOfFace.StdSelect_Cylinder: 2>, 'StdSelect_Sphere': <StdSelect_TypeOfFace.StdSelect_Sphere: 3>, 'StdSelect_Torus': <StdSelect_TypeOfFace.StdSelect_Torus: 4>, 'StdSelect_Revol': <StdSelect_TypeOfFace.StdSelect_Revol: 5>, 'StdSelect_Cone': <StdSelect_TypeOfFace.StdSelect_Cone: 6>}
    pass
class StdSelect_TypeOfSelectionImage():
    """
    Type of output selection image.

    Members:

      StdSelect_TypeOfSelectionImage_NormalizedDepth

      StdSelect_TypeOfSelectionImage_NormalizedDepthInverted

      StdSelect_TypeOfSelectionImage_UnnormalizedDepth

      StdSelect_TypeOfSelectionImage_ColoredDetectedObject

      StdSelect_TypeOfSelectionImage_ColoredEntity

      StdSelect_TypeOfSelectionImage_ColoredEntityType

      StdSelect_TypeOfSelectionImage_ColoredOwner

      StdSelect_TypeOfSelectionImage_ColoredSelectionMode

      StdSelect_TypeOfSelectionImage_SurfaceNormal
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
    StdSelect_TypeOfSelectionImage_ColoredDetectedObject: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredDetectedObject: 3>
    StdSelect_TypeOfSelectionImage_ColoredEntity: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntity: 4>
    StdSelect_TypeOfSelectionImage_ColoredEntityType: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntityType: 5>
    StdSelect_TypeOfSelectionImage_ColoredOwner: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredOwner: 6>
    StdSelect_TypeOfSelectionImage_ColoredSelectionMode: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredSelectionMode: 7>
    StdSelect_TypeOfSelectionImage_NormalizedDepth: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepth: 0>
    StdSelect_TypeOfSelectionImage_NormalizedDepthInverted: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepthInverted: 1>
    StdSelect_TypeOfSelectionImage_SurfaceNormal: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_SurfaceNormal: 8>
    StdSelect_TypeOfSelectionImage_UnnormalizedDepth: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_UnnormalizedDepth: 2>
    __entries: dict # value = {'StdSelect_TypeOfSelectionImage_NormalizedDepth': (<StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepth: 0>, None), 'StdSelect_TypeOfSelectionImage_NormalizedDepthInverted': (<StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepthInverted: 1>, None), 'StdSelect_TypeOfSelectionImage_UnnormalizedDepth': (<StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_UnnormalizedDepth: 2>, None), 'StdSelect_TypeOfSelectionImage_ColoredDetectedObject': (<StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredDetectedObject: 3>, None), 'StdSelect_TypeOfSelectionImage_ColoredEntity': (<StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntity: 4>, None), 'StdSelect_TypeOfSelectionImage_ColoredEntityType': (<StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntityType: 5>, None), 'StdSelect_TypeOfSelectionImage_ColoredOwner': (<StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredOwner: 6>, None), 'StdSelect_TypeOfSelectionImage_ColoredSelectionMode': (<StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredSelectionMode: 7>, None), 'StdSelect_TypeOfSelectionImage_SurfaceNormal': (<StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_SurfaceNormal: 8>, None)}
    __members__: dict # value = {'StdSelect_TypeOfSelectionImage_NormalizedDepth': <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepth: 0>, 'StdSelect_TypeOfSelectionImage_NormalizedDepthInverted': <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepthInverted: 1>, 'StdSelect_TypeOfSelectionImage_UnnormalizedDepth': <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_UnnormalizedDepth: 2>, 'StdSelect_TypeOfSelectionImage_ColoredDetectedObject': <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredDetectedObject: 3>, 'StdSelect_TypeOfSelectionImage_ColoredEntity': <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntity: 4>, 'StdSelect_TypeOfSelectionImage_ColoredEntityType': <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntityType: 5>, 'StdSelect_TypeOfSelectionImage_ColoredOwner': <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredOwner: 6>, 'StdSelect_TypeOfSelectionImage_ColoredSelectionMode': <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredSelectionMode: 7>, 'StdSelect_TypeOfSelectionImage_SurfaceNormal': <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_SurfaceNormal: 8>}
    pass
StdSelect_AnyEdge: OCP.StdSelect.StdSelect_TypeOfEdge # value = <StdSelect_TypeOfEdge.StdSelect_AnyEdge: 0>
StdSelect_AnyFace: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_AnyFace: 0>
StdSelect_Circle: OCP.StdSelect.StdSelect_TypeOfEdge # value = <StdSelect_TypeOfEdge.StdSelect_Circle: 2>
StdSelect_Cone: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Cone: 6>
StdSelect_Cylinder: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Cylinder: 2>
StdSelect_Line: OCP.StdSelect.StdSelect_TypeOfEdge # value = <StdSelect_TypeOfEdge.StdSelect_Line: 1>
StdSelect_Plane: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Plane: 1>
StdSelect_Revol: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Revol: 5>
StdSelect_Sphere: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Sphere: 3>
StdSelect_Torus: OCP.StdSelect.StdSelect_TypeOfFace # value = <StdSelect_TypeOfFace.StdSelect_Torus: 4>
StdSelect_TypeOfSelectionImage_ColoredDetectedObject: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredDetectedObject: 3>
StdSelect_TypeOfSelectionImage_ColoredEntity: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntity: 4>
StdSelect_TypeOfSelectionImage_ColoredEntityType: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredEntityType: 5>
StdSelect_TypeOfSelectionImage_ColoredOwner: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredOwner: 6>
StdSelect_TypeOfSelectionImage_ColoredSelectionMode: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_ColoredSelectionMode: 7>
StdSelect_TypeOfSelectionImage_NormalizedDepth: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepth: 0>
StdSelect_TypeOfSelectionImage_NormalizedDepthInverted: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_NormalizedDepthInverted: 1>
StdSelect_TypeOfSelectionImage_SurfaceNormal: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_SurfaceNormal: 8>
StdSelect_TypeOfSelectionImage_UnnormalizedDepth: OCP.StdSelect.StdSelect_TypeOfSelectionImage # value = <StdSelect_TypeOfSelectionImage.StdSelect_TypeOfSelectionImage_UnnormalizedDepth: 2>
