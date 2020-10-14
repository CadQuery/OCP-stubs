import OCP.Prs3d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.TColgp
import OCP.HLRAlgo
import OCP.TopoDS
import OCP.NCollection
import OCP.gp
import OCP.GeomAbs
import OCP.TColStd
import OCP.Poly
import OCP.Bnd
import OCP.Quantity
import OCP.Graphic3d
import OCP.Aspect
import OCP.TopTools
import OCP.Standard
import OCP.Geom
import OCP.TopLoc
__all__  = [
"Prs3d",
"Prs3d_Root",
"Prs3d_BasicAspect",
"Prs3d_ArrowAspect",
"Prs3d_DatumAspect",
"Prs3d_DatumAttribute",
"Prs3d_DatumAxes",
"Prs3d_DatumMode",
"Prs3d_DatumParts",
"Prs3d_DimensionArrowOrientation",
"Prs3d_DimensionAspect",
"Prs3d_DimensionTextHorizontalPosition",
"Prs3d_DimensionTextVerticalPosition",
"Prs3d_DimensionUnits",
"Prs3d_Drawer",
"Prs3d_InvalidAngle",
"Prs3d_LineAspect",
"Prs3d_IsoAspect",
"Prs3d_NListOfSequenceOfPnt",
"Prs3d_PlaneAspect",
"Prs3d_PointAspect",
"Prs3d_PresentationShadow",
"Prs3d_Projector",
"Prs3d_Arrow",
"Prs3d_ShadingAspect",
"Prs3d_ShapeTool",
"Prs3d_Text",
"Prs3d_TextAspect",
"Prs3d_ToolQuadric",
"Prs3d_ToolDisk",
"Prs3d_ToolCylinder",
"Prs3d_ToolSector",
"Prs3d_ToolSphere",
"Prs3d_TypeOfHLR",
"Prs3d_TypeOfHighlight",
"Prs3d_TypeOfLinePicking",
"Prs3d_VertexDrawMode",
"Prs3d_DAO_External",
"Prs3d_DAO_Fit",
"Prs3d_DAO_Internal",
"Prs3d_DA_XAxis",
"Prs3d_DA_XAxisLength",
"Prs3d_DA_XYAxis",
"Prs3d_DA_XYZAxis",
"Prs3d_DA_XZAxis",
"Prs3d_DA_YAxis",
"Prs3d_DA_YAxisLength",
"Prs3d_DA_YZAxis",
"Prs3d_DA_ZAxis",
"Prs3d_DA_ZAxisLength",
"Prs3d_DM_Shaded",
"Prs3d_DM_WireFrame",
"Prs3d_DP_None",
"Prs3d_DP_Origin",
"Prs3d_DP_ShadingConeLengthPercent",
"Prs3d_DP_ShadingConeRadiusPercent",
"Prs3d_DP_ShadingNumberOfFacettes",
"Prs3d_DP_ShadingOriginRadiusPercent",
"Prs3d_DP_ShadingTubeRadiusPercent",
"Prs3d_DP_XArrow",
"Prs3d_DP_XAxis",
"Prs3d_DP_XOYAxis",
"Prs3d_DP_XOZAxis",
"Prs3d_DP_YArrow",
"Prs3d_DP_YAxis",
"Prs3d_DP_YOZAxis",
"Prs3d_DP_ZArrow",
"Prs3d_DP_ZAxis",
"Prs3d_DTHP_Center",
"Prs3d_DTHP_Fit",
"Prs3d_DTHP_Left",
"Prs3d_DTHP_Right",
"Prs3d_DTVP_Above",
"Prs3d_DTVP_Below",
"Prs3d_DTVP_Center",
"Prs3d_TOH_Algo",
"Prs3d_TOH_NotSet",
"Prs3d_TOH_PolyAlgo",
"Prs3d_TOLP_Point",
"Prs3d_TOLP_Segment",
"Prs3d_TypeOfHighlight_Dynamic",
"Prs3d_TypeOfHighlight_LocalDynamic",
"Prs3d_TypeOfHighlight_LocalSelected",
"Prs3d_TypeOfHighlight_NB",
"Prs3d_TypeOfHighlight_None",
"Prs3d_TypeOfHighlight_Selected",
"Prs3d_TypeOfHighlight_SubIntensity",
"Prs3d_VDM_All",
"Prs3d_VDM_Inherited",
"Prs3d_VDM_Isolated"
]
class Prs3d():
    """
    The Prs3d package provides the following services - a presentation object (the context for all modifications to the display, its presentation will be displayed in every view of an active viewer) - an attribute manager governing how objects such as color, width, and type of line are displayed; these are generic objects, whereas those in StdPrs are specific geometries and topologies. - generic algorithms providing default settings for objects such as points, curves, surfaces and shapes - a root object which provides the abstract framework for the DsgPrs definitions at work in display of dimensions, relations and trihedra.
    """
    @staticmethod
    def AddPrimitivesGroup_s(thePrs : OCP.Graphic3d.Graphic3d_Structure,theAspect : Prs3d_LineAspect,thePolylines : Prs3d_NListOfSequenceOfPnt) -> None: 
        """
        Add primitives into new group in presentation and clear the list of polylines.
        """
    @staticmethod
    def GetDeflection_s(theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : Prs3d_Drawer) -> float: 
        """
        Computes the absolute deflection value depending on the type of deflection in theDrawer: Aspect_TOD_RELATIVE: the absolute deflection is computed using the relative deviation coefficient from theDrawer and the shape's bounding box; Aspect_TOD_ABSOLUTE: the maximal chordial deviation from theDrawer is returned. In case of the type of deflection in theDrawer computed relative deflection for shape is stored as absolute deflection. It is necessary to use it later on for sub-shapes. This function should always be used to compute the deflection value for building discrete representations of the shape (triangualtion, wireframe) to avoid incosistencies between different representations of the shape and undesirable visual artifacts.
        """
    @staticmethod
    def MatchSegment_s(X : float,Y : float,Z : float,aDistance : float,p1 : OCP.gp.gp_Pnt,p2 : OCP.gp.gp_Pnt,dist : float) -> bool: 
        """
        draws an arrow at a given location, with respect to a given direction.
        """
    @staticmethod
    def PrimitivesFromPolylines_s(thePoints : Prs3d_NListOfSequenceOfPnt) -> OCP.Graphic3d.Graphic3d_ArrayOfPrimitives: 
        """
        Assembles array of primitives for sequence of polylines.
        """
    def __init__(self) -> None: ...
    pass
class Prs3d_Root():
    """
    A root class for the standard presentation algorithms of the StdPrs package.
    """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
    pass
class Prs3d_BasicAspect(OCP.Standard.Standard_Transient):
    """
    All basic Prs3d_xxxAspect must inherits from this class The aspect classes qualifies how to represent a given kind of object.All basic Prs3d_xxxAspect must inherits from this class The aspect classes qualifies how to represent a given kind of object.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
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
class Prs3d_ArrowAspect(Prs3d_BasicAspect, OCP.Standard.Standard_Transient):
    """
    A framework for displaying arrows in representations of dimensions and relations.A framework for displaying arrows in representations of dimensions and relations.
    """
    def Angle(self) -> float: 
        """
        returns the current value of the angle used when drawing an arrow.
        """
    def Aspect(self) -> OCP.Graphic3d.Graphic3d_AspectLine3d: 
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
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
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
    def Length(self) -> float: 
        """
        Returns the current value of the length used when drawing an arrow.
        """
    def SetAngle(self,anAngle : float) -> None: 
        """
        defines the angle of the arrows.
        """
    def SetAspect(self,theAspect : OCP.Graphic3d.Graphic3d_AspectLine3d) -> None: 
        """
        None
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        None
        """
    def SetLength(self,theLength : float) -> None: 
        """
        Defines the length of the arrows.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theAspect : OCP.Graphic3d.Graphic3d_AspectLine3d) -> None: ...
    @overload
    def __init__(self,anAngle : float,aLength : float) -> None: ...
    @overload
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
class Prs3d_DatumAspect(Prs3d_BasicAspect, OCP.Standard.Standard_Transient):
    """
    A framework to define the display of datums.A framework to define the display of datums.
    """
    def ArrowAspect(self) -> Prs3d_ArrowAspect: 
        """
        Returns the arrow aspect of presentation
        """
    def ArrowPartForAxis(self,thePart : Prs3d_DatumParts) -> Prs3d_DatumParts: 
        """
        Returns type of arrow for a type of axis
        """
    def Attribute(self,theType : Prs3d_DatumAttribute) -> float: 
        """
        Returns the attribute of the datum type
        """
    def AxisLength(self,thePart : Prs3d_DatumParts) -> float: 
        """
        Returns the length of the displayed first axis.
        """
    def DatumAxes(self) -> Prs3d_DatumAxes: 
        """
        Returns axes used in the datum aspect
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DrawDatumPart(self,thePart : Prs3d_DatumParts) -> bool: 
        """
        Returns true if the given part is used in axes of aspect
        """
    def DrawFirstAndSecondAxis(self) -> bool: 
        """
        Returns true if the first and second axes can be drawn.
        """
    def DrawThirdAxis(self) -> bool: 
        """
        Returns true if the third axis can be drawn.
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstAxisAspect(self) -> Prs3d_LineAspect: 
        """
        Returns the attributes for display of the first axis.
        """
    def FirstAxisLength(self) -> float: 
        """
        Returns the length of the displayed first axis.
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
    def LineAspect(self,thePart : Prs3d_DatumParts) -> Prs3d_LineAspect: 
        """
        Returns the right-handed coordinate system set in SetComponent.
        """
    def PointAspect(self) -> Prs3d_PointAspect: 
        """
        Returns the point aspect of origin wireframe presentation
        """
    def SecondAxisAspect(self) -> Prs3d_LineAspect: 
        """
        Returns the attributes for display of the second axis.
        """
    def SecondAxisLength(self) -> float: 
        """
        Returns the length of the displayed second axis.
        """
    def SetArrowAspect(self,theAspect : Prs3d_ArrowAspect) -> None: 
        """
        Sets the arrow aspect of presentation
        """
    def SetAttribute(self,theType : Prs3d_DatumAttribute,theValue : float) -> None: 
        """
        Sets the attribute of the datum type
        """
    def SetAxisLength(self,theL1 : float,theL2 : float,theL3 : float) -> None: 
        """
        Sets the lengths of the three axes.
        """
    def SetDrawArrows(self,theToDraw : bool) -> None: 
        """
        Sets option to draw or not arrows for axes
        """
    def SetDrawDatumAxes(self,theType : Prs3d_DatumAxes) -> None: 
        """
        Sets the axes used in the datum aspect
        """
    def SetDrawFirstAndSecondAxis(self,theToDraw : bool) -> None: 
        """
        Sets the DrawFirstAndSecondAxis attributes to active.
        """
    def SetDrawLabels(self,theToDraw : bool) -> None: 
        """
        Sets option to draw or not to draw text labels for axes
        """
    def SetDrawThirdAxis(self,theToDraw : bool) -> None: 
        """
        Sets the DrawThirdAxis attributes to active.
        """
    def SetPointAspect(self,theAspect : Prs3d_PointAspect) -> None: 
        """
        Returns the point aspect of origin wireframe presentation
        """
    def SetTextAspect(self,theTextAspect : Prs3d_TextAspect) -> None: 
        """
        Sets text attributes for rendering labels.
        """
    def SetToDrawLabels(self,theToDraw : bool) -> None: 
        """
        None
        """
    def ShadingAspect(self,thePart : Prs3d_DatumParts) -> Prs3d_ShadingAspect: 
        """
        Returns the right-handed coordinate system set in SetComponent.
        """
    def TextAspect(self) -> Prs3d_TextAspect: 
        """
        Returns the text attributes for rendering labels.
        """
    def ThirdAxisAspect(self) -> Prs3d_LineAspect: 
        """
        Returns the attributes for display of the third axis.
        """
    def ThirdAxisLength(self) -> float: 
        """
        Returns the length of the displayed third axis.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToDrawArrows(self) -> bool: 
        """
        Returns true if axes arrows are drawn; TRUE by default.
        """
    def ToDrawLabels(self) -> bool: 
        """
        Returns true if axes labels are drawn; TRUE by default.
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
class Prs3d_DatumAttribute():
    """
    Enumeration defining a part of datum aspect, see Prs3d_Datum.

    Members:

      Prs3d_DA_XAxisLength

      Prs3d_DA_YAxisLength

      Prs3d_DA_ZAxisLength

      Prs3d_DP_ShadingTubeRadiusPercent

      Prs3d_DP_ShadingConeRadiusPercent

      Prs3d_DP_ShadingConeLengthPercent

      Prs3d_DP_ShadingOriginRadiusPercent

      Prs3d_DP_ShadingNumberOfFacettes
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_DA_XAxisLength: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DA_XAxisLength
    Prs3d_DA_YAxisLength: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DA_YAxisLength
    Prs3d_DA_ZAxisLength: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DA_ZAxisLength
    Prs3d_DP_ShadingConeLengthPercent: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingConeLengthPercent
    Prs3d_DP_ShadingConeRadiusPercent: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingConeRadiusPercent
    Prs3d_DP_ShadingNumberOfFacettes: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingNumberOfFacettes
    Prs3d_DP_ShadingOriginRadiusPercent: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingOriginRadiusPercent
    Prs3d_DP_ShadingTubeRadiusPercent: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingTubeRadiusPercent
    __entries: dict # value = {'Prs3d_DA_XAxisLength': (Prs3d_DatumAttribute.Prs3d_DA_XAxisLength, None), 'Prs3d_DA_YAxisLength': (Prs3d_DatumAttribute.Prs3d_DA_YAxisLength, None), 'Prs3d_DA_ZAxisLength': (Prs3d_DatumAttribute.Prs3d_DA_ZAxisLength, None), 'Prs3d_DP_ShadingTubeRadiusPercent': (Prs3d_DatumAttribute.Prs3d_DP_ShadingTubeRadiusPercent, None), 'Prs3d_DP_ShadingConeRadiusPercent': (Prs3d_DatumAttribute.Prs3d_DP_ShadingConeRadiusPercent, None), 'Prs3d_DP_ShadingConeLengthPercent': (Prs3d_DatumAttribute.Prs3d_DP_ShadingConeLengthPercent, None), 'Prs3d_DP_ShadingOriginRadiusPercent': (Prs3d_DatumAttribute.Prs3d_DP_ShadingOriginRadiusPercent, None), 'Prs3d_DP_ShadingNumberOfFacettes': (Prs3d_DatumAttribute.Prs3d_DP_ShadingNumberOfFacettes, None)}
    __members__: dict # value = {'Prs3d_DA_XAxisLength': Prs3d_DatumAttribute.Prs3d_DA_XAxisLength, 'Prs3d_DA_YAxisLength': Prs3d_DatumAttribute.Prs3d_DA_YAxisLength, 'Prs3d_DA_ZAxisLength': Prs3d_DatumAttribute.Prs3d_DA_ZAxisLength, 'Prs3d_DP_ShadingTubeRadiusPercent': Prs3d_DatumAttribute.Prs3d_DP_ShadingTubeRadiusPercent, 'Prs3d_DP_ShadingConeRadiusPercent': Prs3d_DatumAttribute.Prs3d_DP_ShadingConeRadiusPercent, 'Prs3d_DP_ShadingConeLengthPercent': Prs3d_DatumAttribute.Prs3d_DP_ShadingConeLengthPercent, 'Prs3d_DP_ShadingOriginRadiusPercent': Prs3d_DatumAttribute.Prs3d_DP_ShadingOriginRadiusPercent, 'Prs3d_DP_ShadingNumberOfFacettes': Prs3d_DatumAttribute.Prs3d_DP_ShadingNumberOfFacettes}
    pass
class Prs3d_DatumAxes():
    """
    Enumeration defining an axes used in datum aspect, see Prs3d_Datum.

    Members:

      Prs3d_DA_XAxis

      Prs3d_DA_YAxis

      Prs3d_DA_ZAxis

      Prs3d_DA_XYAxis

      Prs3d_DA_YZAxis

      Prs3d_DA_XZAxis

      Prs3d_DA_XYZAxis
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_DA_XAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_XAxis
    Prs3d_DA_XYAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_XYAxis
    Prs3d_DA_XYZAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_XYZAxis
    Prs3d_DA_XZAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_XZAxis
    Prs3d_DA_YAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_YAxis
    Prs3d_DA_YZAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_YZAxis
    Prs3d_DA_ZAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_ZAxis
    __entries: dict # value = {'Prs3d_DA_XAxis': (Prs3d_DatumAxes.Prs3d_DA_XAxis, None), 'Prs3d_DA_YAxis': (Prs3d_DatumAxes.Prs3d_DA_YAxis, None), 'Prs3d_DA_ZAxis': (Prs3d_DatumAxes.Prs3d_DA_ZAxis, None), 'Prs3d_DA_XYAxis': (Prs3d_DatumAxes.Prs3d_DA_XYAxis, None), 'Prs3d_DA_YZAxis': (Prs3d_DatumAxes.Prs3d_DA_YZAxis, None), 'Prs3d_DA_XZAxis': (Prs3d_DatumAxes.Prs3d_DA_XZAxis, None), 'Prs3d_DA_XYZAxis': (Prs3d_DatumAxes.Prs3d_DA_XYZAxis, None)}
    __members__: dict # value = {'Prs3d_DA_XAxis': Prs3d_DatumAxes.Prs3d_DA_XAxis, 'Prs3d_DA_YAxis': Prs3d_DatumAxes.Prs3d_DA_YAxis, 'Prs3d_DA_ZAxis': Prs3d_DatumAxes.Prs3d_DA_ZAxis, 'Prs3d_DA_XYAxis': Prs3d_DatumAxes.Prs3d_DA_XYAxis, 'Prs3d_DA_YZAxis': Prs3d_DatumAxes.Prs3d_DA_YZAxis, 'Prs3d_DA_XZAxis': Prs3d_DatumAxes.Prs3d_DA_XZAxis, 'Prs3d_DA_XYZAxis': Prs3d_DatumAxes.Prs3d_DA_XYZAxis}
    pass
class Prs3d_DatumMode():
    """
    Enumeration defining a mode of datum graphic presentation, see Prs3d_Datum.

    Members:

      Prs3d_DM_WireFrame

      Prs3d_DM_Shaded
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_DM_Shaded: OCP.Prs3d.Prs3d_DatumMode # value = Prs3d_DatumMode.Prs3d_DM_Shaded
    Prs3d_DM_WireFrame: OCP.Prs3d.Prs3d_DatumMode # value = Prs3d_DatumMode.Prs3d_DM_WireFrame
    __entries: dict # value = {'Prs3d_DM_WireFrame': (Prs3d_DatumMode.Prs3d_DM_WireFrame, None), 'Prs3d_DM_Shaded': (Prs3d_DatumMode.Prs3d_DM_Shaded, None)}
    __members__: dict # value = {'Prs3d_DM_WireFrame': Prs3d_DatumMode.Prs3d_DM_WireFrame, 'Prs3d_DM_Shaded': Prs3d_DatumMode.Prs3d_DM_Shaded}
    pass
class Prs3d_DatumParts():
    """
    Enumeration defining a part of datum aspect, see Prs3d_Datum.

    Members:

      Prs3d_DP_Origin

      Prs3d_DP_XAxis

      Prs3d_DP_YAxis

      Prs3d_DP_ZAxis

      Prs3d_DP_XArrow

      Prs3d_DP_YArrow

      Prs3d_DP_ZArrow

      Prs3d_DP_XOYAxis

      Prs3d_DP_YOZAxis

      Prs3d_DP_XOZAxis

      Prs3d_DP_None
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_DP_None: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_None
    Prs3d_DP_Origin: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_Origin
    Prs3d_DP_XArrow: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_XArrow
    Prs3d_DP_XAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_XAxis
    Prs3d_DP_XOYAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_XOYAxis
    Prs3d_DP_XOZAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_XOZAxis
    Prs3d_DP_YArrow: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_YArrow
    Prs3d_DP_YAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_YAxis
    Prs3d_DP_YOZAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_YOZAxis
    Prs3d_DP_ZArrow: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_ZArrow
    Prs3d_DP_ZAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_ZAxis
    __entries: dict # value = {'Prs3d_DP_Origin': (Prs3d_DatumParts.Prs3d_DP_Origin, None), 'Prs3d_DP_XAxis': (Prs3d_DatumParts.Prs3d_DP_XAxis, None), 'Prs3d_DP_YAxis': (Prs3d_DatumParts.Prs3d_DP_YAxis, None), 'Prs3d_DP_ZAxis': (Prs3d_DatumParts.Prs3d_DP_ZAxis, None), 'Prs3d_DP_XArrow': (Prs3d_DatumParts.Prs3d_DP_XArrow, None), 'Prs3d_DP_YArrow': (Prs3d_DatumParts.Prs3d_DP_YArrow, None), 'Prs3d_DP_ZArrow': (Prs3d_DatumParts.Prs3d_DP_ZArrow, None), 'Prs3d_DP_XOYAxis': (Prs3d_DatumParts.Prs3d_DP_XOYAxis, None), 'Prs3d_DP_YOZAxis': (Prs3d_DatumParts.Prs3d_DP_YOZAxis, None), 'Prs3d_DP_XOZAxis': (Prs3d_DatumParts.Prs3d_DP_XOZAxis, None), 'Prs3d_DP_None': (Prs3d_DatumParts.Prs3d_DP_None, None)}
    __members__: dict # value = {'Prs3d_DP_Origin': Prs3d_DatumParts.Prs3d_DP_Origin, 'Prs3d_DP_XAxis': Prs3d_DatumParts.Prs3d_DP_XAxis, 'Prs3d_DP_YAxis': Prs3d_DatumParts.Prs3d_DP_YAxis, 'Prs3d_DP_ZAxis': Prs3d_DatumParts.Prs3d_DP_ZAxis, 'Prs3d_DP_XArrow': Prs3d_DatumParts.Prs3d_DP_XArrow, 'Prs3d_DP_YArrow': Prs3d_DatumParts.Prs3d_DP_YArrow, 'Prs3d_DP_ZArrow': Prs3d_DatumParts.Prs3d_DP_ZArrow, 'Prs3d_DP_XOYAxis': Prs3d_DatumParts.Prs3d_DP_XOYAxis, 'Prs3d_DP_YOZAxis': Prs3d_DatumParts.Prs3d_DP_YOZAxis, 'Prs3d_DP_XOZAxis': Prs3d_DatumParts.Prs3d_DP_XOZAxis, 'Prs3d_DP_None': Prs3d_DatumParts.Prs3d_DP_None}
    pass
class Prs3d_DimensionArrowOrientation():
    """
    Specifies dimension arrow location and orientation. DAO_Internal - arrows "inside", pointing outwards. DAO_External - arrows "outside", pointing inwards. DAO_Fit - arrows oriented inside if value label with arrowtips fit the dimension line, otherwise - externally

    Members:

      Prs3d_DAO_Internal

      Prs3d_DAO_External

      Prs3d_DAO_Fit
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_DAO_External: OCP.Prs3d.Prs3d_DimensionArrowOrientation # value = Prs3d_DimensionArrowOrientation.Prs3d_DAO_External
    Prs3d_DAO_Fit: OCP.Prs3d.Prs3d_DimensionArrowOrientation # value = Prs3d_DimensionArrowOrientation.Prs3d_DAO_Fit
    Prs3d_DAO_Internal: OCP.Prs3d.Prs3d_DimensionArrowOrientation # value = Prs3d_DimensionArrowOrientation.Prs3d_DAO_Internal
    __entries: dict # value = {'Prs3d_DAO_Internal': (Prs3d_DimensionArrowOrientation.Prs3d_DAO_Internal, None), 'Prs3d_DAO_External': (Prs3d_DimensionArrowOrientation.Prs3d_DAO_External, None), 'Prs3d_DAO_Fit': (Prs3d_DimensionArrowOrientation.Prs3d_DAO_Fit, None)}
    __members__: dict # value = {'Prs3d_DAO_Internal': Prs3d_DimensionArrowOrientation.Prs3d_DAO_Internal, 'Prs3d_DAO_External': Prs3d_DimensionArrowOrientation.Prs3d_DAO_External, 'Prs3d_DAO_Fit': Prs3d_DimensionArrowOrientation.Prs3d_DAO_Fit}
    pass
class Prs3d_DimensionAspect(Prs3d_BasicAspect, OCP.Standard.Standard_Transient):
    """
    defines the attributes when drawing a Length Presentation.defines the attributes when drawing a Length Presentation.
    """
    def ArrowAspect(self) -> Prs3d_ArrowAspect: 
        """
        Returns the settings for displaying arrows.
        """
    def ArrowOrientation(self) -> Prs3d_DimensionArrowOrientation: 
        """
        Gets orientation of arrows (external or internal).
        """
    def ArrowTailSize(self) -> float: 
        """
        Returns arrow tail size.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtensionSize(self) -> float: 
        """
        Returns extension size.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsArrows3d(self) -> bool: 
        """
        Gets type of arrows.
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
    def IsText3d(self) -> bool: 
        """
        Check if text for dimension label is 3d.
        """
    def IsTextShaded(self) -> bool: 
        """
        Check if 3d text for dimension label is shaded.
        """
    def IsUnitsDisplayed(self) -> bool: 
        """
        Shows if Units are to be displayed along with dimension value.
        """
    def LineAspect(self) -> Prs3d_LineAspect: 
        """
        Returns the settings for the display of lines used in presentation of dimensions.
        """
    def MakeArrows3d(self,theIsArrows3d : bool) -> None: 
        """
        Sets type of arrows.
        """
    def MakeText3d(self,isText3d : bool) -> None: 
        """
        Sets type of text.
        """
    def MakeTextShaded(self,theIsTextShaded : bool) -> None: 
        """
        Turns on/off text shading for 3d text.
        """
    def MakeUnitsDisplayed(self,theIsDisplayed : bool) -> None: 
        """
        Specifies whether the units string should be displayed along with value label or not.
        """
    def SetArrowAspect(self,theAspect : Prs3d_ArrowAspect) -> None: 
        """
        Sets the display attributes of arrows used in presentation of dimensions.
        """
    def SetArrowOrientation(self,theArrowOrient : Prs3d_DimensionArrowOrientation) -> None: 
        """
        Sets orientation of arrows (external or internal). By default orientation is chosen automatically according to situation and text label size.
        """
    def SetArrowTailSize(self,theSize : float) -> None: 
        """
        Set size for arrow tail (extension without text).
        """
    def SetCommonColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Sets the same color for all parts of dimension: lines, arrows and text.
        """
    def SetExtensionSize(self,theSize : float) -> None: 
        """
        Sets extension size.
        """
    def SetLineAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets the display attributes of lines used in presentation of dimensions.
        """
    def SetTextAspect(self,theAspect : Prs3d_TextAspect) -> None: 
        """
        Sets the display attributes of text used in presentation of dimensions.
        """
    def SetTextHorizontalPosition(self,thePosition : Prs3d_DimensionTextHorizontalPosition) -> None: 
        """
        Sets horizontal text alignment for text label.
        """
    def SetTextVerticalPosition(self,thePosition : Prs3d_DimensionTextVerticalPosition) -> None: 
        """
        Sets vertical text alignment for text label.
        """
    def SetValueStringFormat(self,theFormat : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets "sprintf"-syntax format for formatting dimension value labels.
        """
    def TextAspect(self) -> Prs3d_TextAspect: 
        """
        Returns the settings for the display of text used in presentation of dimensions.
        """
    def TextHorizontalPosition(self) -> Prs3d_DimensionTextHorizontalPosition: 
        """
        Gets horizontal text alignment for text label.
        """
    def TextVerticalPosition(self) -> Prs3d_DimensionTextVerticalPosition: 
        """
        Gets vertical text alignment for text label.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ValueStringFormat(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns format.
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
class Prs3d_DimensionTextHorizontalPosition():
    """
    Specifies options for positioning dimension value label in horizontal direction. DTHP_Left - value label located at left side on dimension extension. DTHP_Right - value label located at right side on dimension extension. DTHP_Center - value label located at center of dimension line. DTHP_Fit - value label located automatically at left side if does not fits the dimension space, otherwise the value label is placed at center.

    Members:

      Prs3d_DTHP_Left

      Prs3d_DTHP_Right

      Prs3d_DTHP_Center

      Prs3d_DTHP_Fit
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_DTHP_Center: OCP.Prs3d.Prs3d_DimensionTextHorizontalPosition # value = Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Center
    Prs3d_DTHP_Fit: OCP.Prs3d.Prs3d_DimensionTextHorizontalPosition # value = Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Fit
    Prs3d_DTHP_Left: OCP.Prs3d.Prs3d_DimensionTextHorizontalPosition # value = Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Left
    Prs3d_DTHP_Right: OCP.Prs3d.Prs3d_DimensionTextHorizontalPosition # value = Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Right
    __entries: dict # value = {'Prs3d_DTHP_Left': (Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Left, None), 'Prs3d_DTHP_Right': (Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Right, None), 'Prs3d_DTHP_Center': (Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Center, None), 'Prs3d_DTHP_Fit': (Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Fit, None)}
    __members__: dict # value = {'Prs3d_DTHP_Left': Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Left, 'Prs3d_DTHP_Right': Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Right, 'Prs3d_DTHP_Center': Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Center, 'Prs3d_DTHP_Fit': Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Fit}
    pass
class Prs3d_DimensionTextVerticalPosition():
    """
    Specifies options for positioning dimension value label in vertical direction with respect to dimension (extension) line. DTVP_Above - text label is located above the dimension or extension line. DTVP_Below - text label is located below the dimension or extension line. DTVP_Center - the text label middle-point is in line with dimension or extension line.

    Members:

      Prs3d_DTVP_Above

      Prs3d_DTVP_Below

      Prs3d_DTVP_Center
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_DTVP_Above: OCP.Prs3d.Prs3d_DimensionTextVerticalPosition # value = Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Above
    Prs3d_DTVP_Below: OCP.Prs3d.Prs3d_DimensionTextVerticalPosition # value = Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Below
    Prs3d_DTVP_Center: OCP.Prs3d.Prs3d_DimensionTextVerticalPosition # value = Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Center
    __entries: dict # value = {'Prs3d_DTVP_Above': (Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Above, None), 'Prs3d_DTVP_Below': (Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Below, None), 'Prs3d_DTVP_Center': (Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Center, None)}
    __members__: dict # value = {'Prs3d_DTVP_Above': Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Above, 'Prs3d_DTVP_Below': Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Below, 'Prs3d_DTVP_Center': Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Center}
    pass
class Prs3d_DimensionUnits():
    """
    This class provides units for two dimension groups: - lengthes (length, radius, diameter) - angles
    """
    def GetAngleUnits(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns angle units
        """
    def GetLengthUnits(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns length units
        """
    def SetAngleUnits(self,theUnits : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets angle units
        """
    def SetLengthUnits(self,theUnits : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets length units
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theUnits : Prs3d_DimensionUnits) -> None: ...
    pass
class Prs3d_Drawer(OCP.Graphic3d.Graphic3d_PresentationAttributes, OCP.Standard.Standard_Transient):
    """
    A graphic attribute manager which governs how objects such as color, width, line thickness and deflection are displayed. A drawer includes an instance of the Aspect classes with particular default values.A graphic attribute manager which governs how objects such as color, width, line thickness and deflection are displayed. A drawer includes an instance of the Aspect classes with particular default values.
    """
    def ArrowAspect(self) -> Prs3d_ArrowAspect: 
        """
        Returns the attributes for display of arrows.
        """
    def BasicFillAreaAspect(self) -> OCP.Graphic3d.Graphic3d_AspectFillArea3d: 
        """
        Return basic presentation fill area aspect, NULL by default. When set, might be used instead of Color() property.
        """
    def ClearLocalAttributes(self) -> None: 
        """
        Removes local attributes.
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns basic presentation color, Quantity_NOC_WHITE by default.
        """
    def ColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns basic presentation color (including alpha channel).
        """
    def DatumAspect(self) -> Prs3d_DatumAspect: 
        """
        Returns settings for the appearance of datums. These settings can be edited. The default values for the three axes are: Color: Quantity_NOC_PEACHPUFF Type of line: Aspect_TOL_SOLID Width: 1.0
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeviationAngle(self) -> float: 
        """
        Returns the value for deviation angle.
        """
    def DeviationCoefficient(self) -> float: 
        """
        Returns the deviation coefficient. Drawings of curves or patches are made with respect to a maximal chordal deviation. A Deviation coefficient is used in the shading display mode. The shape is seen decomposed into triangles. These are used to calculate reflection of light from the surface of the object. The triangles are formed from chords of the curves in the shape. The deviation coefficient gives the highest value of the angle with which a chord can deviate from a tangent to a curve. If this limit is reached, a new triangle is begun. This deviation is absolute and is set through the method: SetMaximalChordialDeviation. The default value is 0.001. In drawing shapes, however, you are allowed to ask for a relative deviation. This deviation will be: SizeOfObject * DeviationCoefficient.
        """
    def DimAngleDisplayUnits(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns angle units in which dimension presentation is displayed.
        """
    def DimAngleModelUnits(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns angle model units for the dimension presentation.
        """
    def DimLengthDisplayUnits(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns length units in which dimension presentation is displayed.
        """
    def DimLengthModelUnits(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns length model units for the dimension presentation.
        """
    def DimensionAspect(self) -> Prs3d_DimensionAspect: 
        """
        Returns settings for the appearance of dimensions.
        """
    def DisableDrawHiddenLine(self) -> None: 
        """
        Disables the DrawHiddenLine function.
        """
    def Discretisation(self) -> int: 
        """
        Returns the discretisation setting.
        """
    def DisplayMode(self) -> int: 
        """
        Returns display mode, 0 by default. -1 means undefined (main display mode of presentation to be used).
        """
    def DrawHiddenLine(self) -> bool: 
        """
        Returns Standard_True if the hidden lines are to be drawn. By default the hidden lines are not drawn.
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableDrawHiddenLine(self) -> None: 
        """
        Enables the DrawHiddenLine function.
        """
    def FaceBoundaryAspect(self) -> Prs3d_LineAspect: 
        """
        Returns line aspect of face boundaries.
        """
    def FaceBoundaryDraw(self) -> bool: 
        """
        Checks whether the face boundary drawing is enabled or not.
        """
    def FaceBoundaryUpperContinuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Get the most edge continuity class; GeomAbs_CN by default (all edges).
        """
    def FreeBoundaryAspect(self) -> Prs3d_LineAspect: 
        """
        Returns the values for presentation of free boundaries, in other words, boundaries which are not shared. The LineAspect for the free boundaries can be edited. The default values are: Color: Quantity_NOC_GREEN Type of line: Aspect_TOL_SOLID Width: 1.0 These attributes are used by the algorithm Prs3d_WFShape
        """
    def FreeBoundaryDraw(self) -> bool: 
        """
        Returns True if the drawing of the free boundaries is enabled True is the default setting.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HLRAngle(self) -> float: 
        """
        Returns the real number value of the deviation angle in hidden line removal views. The default value is 20 * M_PI / 180.
        """
    def HLRDeviationCoefficient(self) -> float: 
        """
        Returns the real number value of the hidden line removal deviation coefficient in this framework, if the flag hasOwnHLRDeviationCoefficient is true or there is no Link. Else the shape's HLR deviation coefficient is used. A Deviation coefficient is used in the shading display mode. The shape is seen decomposed into triangles. These are used to calculate reflection of light from the surface of the object. The triangles are formed from chords of the curves in the shape. The deviation coefficient give the highest value of the angle with which a chord can deviate from a tangent to a curve. If this limit is reached, a new triangle is begun. To find the hidden lines, hidden line display mode entails recalculation of the view at each different projector perspective. Since hidden lines entail calculations of more than usual complexity to decompose them into these triangles, a deviation coefficient allowing greater tolerance is used. This increases efficiency in calculation. The Default value is 0.02.
        """
    def HasLink(self) -> bool: 
        """
        Returns true if the current object has a link on the other drawer.
        """
    def HasOwnArrowAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for arrow aspect that overrides the one in the link.
        """
    def HasOwnDatumAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for datum aspect that overrides the one in the link.
        """
    def HasOwnDeviationAngle(self) -> bool: 
        """
        Returns true if the there is a local setting for deviation angle in this framework for a specific interactive object.
        """
    def HasOwnDeviationCoefficient(self) -> bool: 
        """
        Returns true if there is a local setting for deviation coefficient in this framework for a specific interactive object.
        """
    def HasOwnDimAngleDisplayUnits(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for angle units in which dimension presentation is displayed that overrides the one in the link.
        """
    def HasOwnDimAngleModelUnits(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for dimension angle model units that overrides the one in the link.
        """
    def HasOwnDimLengthDisplayUnits(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for length units in which dimension presentation is displayed that overrides the one in the link.
        """
    def HasOwnDimLengthModelUnits(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for dimension length model units that overrides the one in the link.
        """
    def HasOwnDimensionAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for the appearance of dimensions that overrides the one in the link.
        """
    def HasOwnDiscretisation(self) -> bool: 
        """
        Returns true if the drawer has discretisation setting active.
        """
    def HasOwnDrawHiddenLine(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for "draw hidden lines" flag that overrides the one in the link.
        """
    def HasOwnFaceBoundaryAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for face boundaries aspect that overrides the one in the link.
        """
    def HasOwnFaceBoundaryDraw(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for "draw face boundaries" flag that overrides the one in the link.
        """
    def HasOwnFaceBoundaryUpperContinuity(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for face boundaries upper edge continuity class that overrides the one in the link.
        """
    def HasOwnFreeBoundaryAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for free boundaries aspect that overrides the one in the link.
        """
    def HasOwnFreeBoundaryDraw(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for "draw free boundaries" flag that overrides the one in the link.
        """
    def HasOwnHLRDeviationAngle(self) -> bool: 
        """
        Returns true if the there is a setting for HLR deviation angle in this framework for a specific interactive object.
        """
    def HasOwnHLRDeviationCoefficient(self) -> bool: 
        """
        Returns true if the there is a setting for HLR deviation coefficient in this framework for a specific interactive object.
        """
    def HasOwnHiddenLineAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for hidden lines aspect that overrides the one in the link.
        """
    def HasOwnIsAutoTriangulation(self) -> bool: 
        """
        Returns true if the drawer has IsoOnPlane setting active.
        """
    def HasOwnIsoOnPlane(self) -> bool: 
        """
        Returns true if the drawer has IsoOnPlane setting active.
        """
    def HasOwnIsoOnTriangulation(self) -> bool: 
        """
        Returns true if the drawer has IsoOnTriangulation setting active.
        """
    def HasOwnLineArrowDraw(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for "draw arrow" flag that overrides the one in the link.
        """
    def HasOwnLineAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for line aspect that overrides the one in the link.
        """
    def HasOwnMaximalChordialDeviation(self) -> bool: 
        """
        Returns true if the drawer has a maximal chordial deviation setting active.
        """
    def HasOwnMaximalParameterValue(self) -> bool: 
        """
        Returns true if the drawer has a maximum value allowed for the first and last parameters of an infinite curve setting active.
        """
    def HasOwnPlaneAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for plane aspect that overrides the one in the link.
        """
    def HasOwnPointAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for point aspect that overrides the one in the link.
        """
    def HasOwnSectionAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for section aspect that overrides the one in the link.
        """
    def HasOwnSeenLineAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for seen line aspect that overrides the one in the link.
        """
    def HasOwnShadingAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for shading aspect that overrides the one in the link.
        """
    def HasOwnTextAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for text aspect that overrides the one in the link.
        """
    def HasOwnTypeOfDeflection(self) -> bool: 
        """
        Returns true if the drawer has a type of deflection setting active.
        """
    def HasOwnTypeOfHLR(self) -> bool: 
        """
        Returns true if the type of HLR is not equal to Prs3d_TOH_NotSet.
        """
    def HasOwnUIsoAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for UIso aspect that overrides the one in the link.
        """
    def HasOwnUnFreeBoundaryAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for unfree boundaries aspect that overrides the one in the link.
        """
    def HasOwnUnFreeBoundaryDraw(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for "draw shared boundaries" flag that overrides the one in the link.
        """
    def HasOwnVIsoAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for VIso aspect that overrides the one in the link.
        """
    def HasOwnVectorAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for vector aspect that overrides the one in the link.
        """
    def HasOwnVertexDrawMode(self) -> bool: 
        """
        Returns true if the vertex draw mode is not equal to Prs3d_VDM_Inherited. This means that individual vertex draw mode value (i.e. not inherited from the global drawer) is used for a specific interactive object.
        """
    def HasOwnWireAspect(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for wire aspect that overrides the one in the link.
        """
    def HasOwnWireDraw(self) -> bool: 
        """
        Returns true if the drawer has its own attribute for "draw wires" flag that overrides the one in the link.
        """
    def HiddenLineAspect(self) -> Prs3d_LineAspect: 
        """
        Returns settings for hidden line aspects. These settings can be edited. The default values are: Color: Quantity_NOC_YELLOW Type of line: Aspect_TOL_DASH Width: 1.0
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAutoTriangulation(self) -> bool: 
        """
        Returns True if automatic triangulation is enabled.
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
    def IsoOnPlane(self) -> bool: 
        """
        Returns True if the drawing of isos on planes is enabled.
        """
    def IsoOnTriangulation(self) -> bool: 
        """
        Returns True if the drawing of isos on triangulation is enabled.
        """
    def LineArrowDraw(self) -> bool: 
        """
        Returns True if drawing an arrow at the end of each edge is enabled and False otherwise (the default).
        """
    def LineAspect(self) -> Prs3d_LineAspect: 
        """
        Returns settings for line aspects. These settings can be edited. The default values are: Color: Quantity_NOC_YELLOW Type of line: Aspect_TOL_SOLID Width: 1.0 These attributes are used by the following algorithms: Prs3d_Curve Prs3d_Line Prs3d_HLRShape
        """
    @overload
    def Link(self) -> Prs3d_Drawer: 
        """
        Sets theDrawer as a link to which the current object references.

        Returns the drawer to which the current object references.
        """
    @overload
    def Link(self,theDrawer : Prs3d_Drawer) -> None: ...
    def MaximalChordialDeviation(self) -> float: 
        """
        Returns the maximal chordal deviation. The default value is 0.1. Drawings of curves or patches are made with respect to an absolute maximal chordal deviation.
        """
    def MaximalParameterValue(self) -> float: 
        """
        Sets the maximum value allowed for the first and last parameters of an infinite curve. By default, this value is 500000.
        """
    def Method(self) -> OCP.Aspect.Aspect_TypeOfHighlightMethod: 
        """
        Returns highlight method, Aspect_TOHM_COLOR by default.
        """
    def PlaneAspect(self) -> Prs3d_PlaneAspect: 
        """
        Returns settings for the appearance of planes.
        """
    def PointAspect(self) -> Prs3d_PointAspect: 
        """
        Returns the point aspect setting. The default values are Color: Quantity_NOC_YELLOW Type of marker: Aspect_TOM_PLUS Scale: 1.0 These attributes are used by the algorithms Prs3d_Point.
        """
    def PreviousDeviationAngle(self) -> float: 
        """
        Returns the previous deviation angle
        """
    def PreviousDeviationCoefficient(self) -> float: 
        """
        Saves the previous value used for the chordal deviation coefficient.
        """
    def PreviousHLRDeviationAngle(self) -> float: 
        """
        Returns the previous value of the HLR deviation angle.
        """
    def PreviousHLRDeviationCoefficient(self) -> float: 
        """
        Returns the previous value of the hidden line removal deviation coefficient.
        """
    def SectionAspect(self) -> Prs3d_LineAspect: 
        """
        The LineAspect for the wire can be edited. The default values are: Color: Quantity_NOC_ORANGE Type of line: Aspect_TOL_SOLID Width: 1.0 These attributes are used by the algorithm Prs3d_WFShape.
        """
    def SeenLineAspect(self) -> Prs3d_LineAspect: 
        """
        Returns settings for seen line aspects. These settings can be edited. The default values are: Color: Quantity_NOC_YELLOW Type of line: Aspect_TOL_SOLID Width: 1.0
        """
    def SetArrowAspect(self,theAspect : Prs3d_ArrowAspect) -> None: 
        """
        Sets the parameter theAspect for display attributes of arrows.
        """
    def SetAutoTriangulation(self,theIsEnabled : bool) -> None: 
        """
        Sets IsAutoTriangulated on or off by setting the parameter theIsEnabled to true or false. If this flag is True automatic re-triangulation with deflection-check logic will be applied. Else this feature will be disable and triangulation is expected to be computed by application itself and no shading presentation at all if unavailable.
        """
    def SetBasicFillAreaAspect(self,theAspect : OCP.Graphic3d.Graphic3d_AspectFillArea3d) -> None: 
        """
        Sets basic presentation fill area aspect.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Sets basic presentation color (RGB components, does not modifies transparency).
        """
    def SetDatumAspect(self,theAspect : Prs3d_DatumAspect) -> None: 
        """
        Sets the modality theAspect for the display of datums.
        """
    @overload
    def SetDeviationAngle(self,theAngle : float) -> None: 
        """
        Sets the deviation angle theAngle. Also sets the hasOwnDeviationAngle flag to Standard_True, and myPreviousDeviationAngle.

        Sets the hasOwnDeviationAngle flag to Standard_False
        """
    @overload
    def SetDeviationAngle(self) -> None: ...
    @overload
    def SetDeviationCoefficient(self,theCoefficient : float) -> None: 
        """
        Sets the deviation coefficient theCoefficient. Also sets the hasOwnDeviationCoefficient flag to Standard_True and myPreviousDeviationCoefficient

        Sets the hasOwnDeviationCoefficient flag to Standard_False
        """
    @overload
    def SetDeviationCoefficient(self) -> None: ...
    def SetDimAngleDisplayUnits(self,theUnits : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets angle units in which value for dimension presentation is displayed. The method sets value owned by the drawer that will be used during visualization instead of the one set in link.
        """
    def SetDimAngleModelUnits(self,theUnits : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets dimension angle model units for computing of dimension presentation. The method sets value owned by the drawer that will be used during visualization instead of the one set in link.
        """
    def SetDimLengthDisplayUnits(self,theUnits : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets length units in which value for dimension presentation is displayed. The method sets value owned by the drawer that will be used during visualization instead of the one set in link.
        """
    def SetDimLengthModelUnits(self,theUnits : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets dimension length model units for computing of dimension presentation. The method sets value owned by the drawer that will be used during visualization instead of the one set in link.
        """
    def SetDimensionAspect(self,theAspect : Prs3d_DimensionAspect) -> None: 
        """
        Sets the settings for the appearance of dimensions. The method sets aspect owned by the drawer that will be used during visualization instead of the one set in link.
        """
    def SetDiscretisation(self,theValue : int) -> None: 
        """
        Sets the discretisation parameter theValue.
        """
    def SetDisplayMode(self,theMode : int) -> None: 
        """
        Sets display mode.
        """
    def SetFaceBoundaryAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets line aspect for face boundaries. The method sets line aspect owned by the drawer that will be used during visualization instead of the one set in link. theAspect is the line aspect that determines the look of the face boundaries.
        """
    def SetFaceBoundaryDraw(self,theIsEnabled : bool) -> None: 
        """
        Enables or disables face boundary drawing for shading presentations. The method sets drawing flag owned by the drawer that will be used during visualization instead of the one set in link. theIsEnabled is a boolean flag indicating whether the face boundaries should be drawn or not.
        """
    def SetFaceBoundaryUpperContinuity(self,theMostAllowedEdgeClass : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Set the most edge continuity class for face boundaries.
        """
    def SetFreeBoundaryAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets the parameter theAspect for the display of free boundaries. The method sets aspect owned by the drawer that will be used during visualization instead of the one set in link.
        """
    def SetFreeBoundaryDraw(self,theIsEnabled : bool) -> None: 
        """
        Enables or disables drawing of free boundaries for shading presentations. The method sets drawing flag owned by the drawer that will be used during visualization instead of the one set in link. theIsEnabled is a boolean flag indicating whether the free boundaries should be drawn or not.
        """
    @overload
    def SetHLRAngle(self,theAngle : float) -> None: 
        """
        Sets anAngle, the angle of maximum chordal deviation for removal of hidden lines created by different viewpoints in different presentations. The default value is 20 * M_PI / 180. Also sets the hasOwnHLRDeviationAngle flag to Standard_True and myPreviousHLRDeviationAngle.

        Sets the hasOwnHLRDeviationAngle flag to Standard_False
        """
    @overload
    def SetHLRAngle(self) -> None: ...
    @overload
    def SetHLRDeviationCoefficient(self) -> None: 
        """
        Sets the deviation coefficient aCoefficient for removal of hidden lines created by different viewpoints in different presentations. The Default value is 0.02. Also sets the hasOwnHLRDeviationCoefficient flag to Standard_True and myPreviousHLRDeviationCoefficient

        Sets the hasOwnHLRDeviationCoefficient flag to Standard_False
        """
    @overload
    def SetHLRDeviationCoefficient(self,theCoefficient : float) -> None: ...
    def SetHiddenLineAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets the parameter theAspect for the display of hidden lines in hidden line removal mode.
        """
    def SetIsoOnPlane(self,theIsEnabled : bool) -> None: 
        """
        Sets IsoOnPlane on or off by setting the parameter theIsEnabled to true or false.
        """
    def SetIsoOnTriangulation(self,theToEnable : bool) -> None: 
        """
        Enables or disables isolines on triangulation by setting the parameter theIsEnabled to true or false.
        """
    def SetLineArrowDraw(self,theIsEnabled : bool) -> None: 
        """
        Enables the drawing of an arrow at the end of each line. By default the arrows are not drawn.
        """
    def SetLineAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets the parameter theAspect for display attributes of lines.
        """
    def SetLink(self,theDrawer : Prs3d_Drawer) -> None: 
        """
        Sets theDrawer as a link to which the current object references.
        """
    def SetMaximalChordialDeviation(self,theChordialDeviation : float) -> None: 
        """
        Defines the maximal chordial deviation when drawing any curve. Even if the type of deviation is set to TOD_Relative, this value is used by: Prs3d_DeflectionCurve Prs3d_WFDeflectionSurface Prs3d_WFDeflectionRestrictedFace
        """
    def SetMaximalParameterValue(self,theValue : float) -> None: 
        """
        Defines the maximum value allowed for the first and last parameters of an infinite curve.
        """
    def SetMethod(self,theMethod : OCP.Aspect.Aspect_TypeOfHighlightMethod) -> None: 
        """
        Changes highlight method to the given one.
        """
    def SetOwnDatumAspects(self,theDefaults : Prs3d_Drawer=None) -> bool: 
        """
        Sets own line aspects for datums. Returns FALSE if own line for datums are already set.
        """
    def SetOwnLineAspects(self,theDefaults : Prs3d_Drawer=None) -> bool: 
        """
        Sets own line aspects. Returns FALSE if own line aspect are already set.
        """
    def SetPlaneAspect(self,theAspect : Prs3d_PlaneAspect) -> None: 
        """
        Sets the parameter theAspect for the display of planes.
        """
    def SetPointAspect(self,theAspect : Prs3d_PointAspect) -> None: 
        """
        Sets the parameter theAspect for display attributes of points
        """
    def SetSectionAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets the parameter theAspect for display attributes of sections.
        """
    def SetSeenLineAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets the parameter theAspect for the display of seen lines in hidden line removal mode.
        """
    def SetShaderProgram(self,theProgram : OCP.Graphic3d.Graphic3d_ShaderProgram,theAspect : OCP.Graphic3d.Graphic3d_GroupAspect,theToOverrideDefaults : bool=False) -> bool: 
        """
        Assign shader program for specified type of primitives.
        """
    def SetShadingAspect(self,theAspect : Prs3d_ShadingAspect) -> None: 
        """
        Sets the parameter theAspect for display attributes of shading.
        """
    def SetShadingModel(self,theModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theToOverrideDefaults : bool=False) -> bool: 
        """
        Sets Shading Model type for the shading aspect.
        """
    def SetTextAspect(self,theAspect : Prs3d_TextAspect) -> None: 
        """
        Sets the parameter theAspect for display attributes of text.
        """
    def SetTransparency(self,theTranspCoef : float) -> None: 
        """
        Sets basic presentation transparency (0 - opaque, 1 - fully transparent).
        """
    def SetTypeOfDeflection(self,theTypeOfDeflection : OCP.Aspect.Aspect_TypeOfDeflection) -> None: 
        """
        Sets the type of chordal deflection. This indicates whether the deflection value is absolute or relative to the size of the object.
        """
    def SetTypeOfHLR(self,theTypeOfHLR : Prs3d_TypeOfHLR) -> None: 
        """
        Sets the type of HLR algorithm used by drawer's interactive objects
        """
    def SetUIsoAspect(self,theAspect : Prs3d_IsoAspect) -> None: 
        """
        None
        """
    def SetUnFreeBoundaryAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets the parameter theAspect for the display of shared boundaries. The method sets aspect owned by the drawer that will be used during visualization instead of the one set in link.
        """
    def SetUnFreeBoundaryDraw(self,theIsEnabled : bool) -> None: 
        """
        Enables or disables drawing of shared boundaries for shading presentations. The method sets drawing flag owned by the drawer that will be used during visualization instead of the one set in link. theIsEnabled is a boolean flag indicating whether the shared boundaries should be drawn or not.
        """
    def SetVIsoAspect(self,theAspect : Prs3d_IsoAspect) -> None: 
        """
        Sets the appearance of V isoparameters - theAspect.
        """
    def SetVectorAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets the modality theAspect for the display of vectors.
        """
    def SetVertexDrawMode(self,theMode : Prs3d_VertexDrawMode) -> None: 
        """
        Sets the mode of visualization of vertices of a TopoDS_Shape instance. By default, only stand-alone vertices (not belonging topologically to an edge) are drawn, that corresponds to Prs3d_VDM_Standalone mode. Switching to Prs3d_VDM_Standalone mode makes all shape's vertices visible. To inherit this parameter from the global drawer instance ("the link") when it is present, Prs3d_VDM_Inherited value should be used.
        """
    def SetWireAspect(self,theAspect : Prs3d_LineAspect) -> None: 
        """
        Sets the parameter theAspect for display of wires.
        """
    def SetWireDraw(self,theIsEnabled : bool) -> None: 
        """
        Sets WireDraw on or off by setting the parameter theIsEnabled to true or false.
        """
    def SetZLayer(self,theLayer : int) -> None: 
        """
        Sets presentation Zlayer.
        """
    def SetupOwnFaceBoundaryAspect(self,theDefaults : Prs3d_Drawer=None) -> bool: 
        """
        Sets own face boundary aspect. Returns FALSE if the drawer already has its own attribute for face boundary aspect.
        """
    def SetupOwnPointAspect(self,theDefaults : Prs3d_Drawer=None) -> bool: 
        """
        Sets own point aspect. Returns FALSE if the drawer already has its own attribute for point aspect.
        """
    def SetupOwnShadingAspect(self,theDefaults : Prs3d_Drawer=None) -> bool: 
        """
        Sets own shading aspect. Returns FALSE if the drawer already has its own attribute for shading aspect.
        """
    def ShadingAspect(self) -> Prs3d_ShadingAspect: 
        """
        Returns settings for shading aspects. These settings can be edited. The default values are: - Color: Quantity_NOC_YELLOW - Material: Graphic3d_NOM_BRASS Shading aspect is obtained through decomposition of 3d faces into triangles, each side of each triangle being a chord of the corresponding curved edge in the face. Reflection of light in each projector perspective is then calculated for each of the resultant triangular planes.
        """
    def TextAspect(self) -> Prs3d_TextAspect: 
        """
        Returns settings for text aspect. These settings can be edited. The default value is: - Color: Quantity_NOC_YELLOW
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transparency(self) -> float: 
        """
        Returns basic presentation transparency (0 - opaque, 1 - fully transparent), 0 by default (opaque).
        """
    def TypeOfDeflection(self) -> OCP.Aspect.Aspect_TypeOfDeflection: 
        """
        Returns the type of chordal deflection. This indicates whether the deflection value is absolute or relative to the size of the object.
        """
    def TypeOfHLR(self) -> Prs3d_TypeOfHLR: 
        """
        Returns the type of HLR algorithm currently in use.
        """
    def UIsoAspect(self) -> Prs3d_IsoAspect: 
        """
        Defines the attributes which are used when drawing an U isoparametric curve of a face. Defines the number of U isoparametric curves to be drawn for a single face. The LineAspect for U isoparametric lines can be edited (methods SetColor, SetTypeOfLine, SetWidth, SetNumber) The default values are: COLOR : Quantity_NOC_GRAY75 TYPE OF LINE: Aspect_TOL_SOLID WIDTH : 0.5
        """
    def UnFreeBoundaryAspect(self) -> Prs3d_LineAspect: 
        """
        Returns settings for shared boundary line aspects. The LineAspect for the unfree boundaries can be edited. The default values are: Color: Quantity_NOC_YELLOW Type of line: Aspect_TOL_SOLID Width: 1. These attributes are used by the algorithm Prs3d_WFShape
        """
    def UnFreeBoundaryDraw(self) -> bool: 
        """
        Returns True if the drawing of the shared boundaries is enabled. True is the default setting.
        """
    def UnsetFaceBoundaryUpperContinuity(self) -> None: 
        """
        Unset the most edge continuity class for face boundaries.
        """
    def UpdatePreviousDeviationAngle(self) -> None: 
        """
        Updates the previous deviation angle to the current value
        """
    def UpdatePreviousDeviationCoefficient(self) -> None: 
        """
        Updates the previous value used for the chordal deviation coefficient to the current state.
        """
    def VIsoAspect(self) -> Prs3d_IsoAspect: 
        """
        Defines the attributes which are used when drawing an V isoparametric curve of a face. Defines the number of V isoparametric curves to be drawn for a single face. The LineAspect for V isoparametric lines can be edited (methods SetColor, SetTypeOfLine, SetWidth, SetNumber) The default values are: COLOR : Quantity_NOC_GRAY82 TYPE OF LINE: Aspect_TOL_SOLID WIDTH : 0.5
        """
    def VectorAspect(self) -> Prs3d_LineAspect: 
        """
        Returns settings for the appearance of vectors. These settings can be edited. The default values are: Color: Quantity_NOC_SKYBLUE Type of line: Aspect_TOL_SOLID Width: 1.0
        """
    def VertexDrawMode(self) -> Prs3d_VertexDrawMode: 
        """
        Returns the current mode of visualization of vertices of a TopoDS_Shape instance.
        """
    def WireAspect(self) -> Prs3d_LineAspect: 
        """
        Returns wire aspect settings. The LineAspect for the free boundaries can be edited. The default values are: Color: Quantity_NOC_GREEN Type of line: Aspect_TOL_SOLID Width: 1.0 These attributes are used by the algorithm Prs3d_WFShape.
        """
    def WireDraw(self) -> bool: 
        """
        Returns True if the drawing of the wire is enabled.
        """
    def ZLayer(self) -> int: 
        """
        Returns presentation Zlayer, Graphic3d_ZLayerId_Default by default. Graphic3d_ZLayerId_UNKNOWN means undefined (a layer of main presentation to be used).
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
class Prs3d_InvalidAngle(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Prs3d', '__weakref__': <attribute '__weakref__' of 'Prs3d_InvalidAngle' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Prs3d_InvalidAngle' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Prs3d_LineAspect(Prs3d_BasicAspect, OCP.Standard.Standard_Transient):
    """
    A framework for defining how a line will be displayed in a presentation. Aspects of line display include width, color and type of line. The definition set by this class is then passed to the attribute manager Prs3d_Drawer. Any object which requires a value for line aspect as an argument may then be given the attribute manager as a substitute argument in the form of a field such as myDrawer for example.A framework for defining how a line will be displayed in a presentation. Aspects of line display include width, color and type of line. The definition set by this class is then passed to the attribute manager Prs3d_Drawer. Any object which requires a value for line aspect as an argument may then be given the attribute manager as a substitute argument in the form of a field such as myDrawer for example.
    """
    def Aspect(self) -> OCP.Graphic3d.Graphic3d_AspectLine3d: 
        """
        Returns the line aspect. This is defined as the set of color, type and thickness attributes.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
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
    def SetAspect(self,theAspect : OCP.Graphic3d.Graphic3d_AspectLine3d) -> None: 
        """
        None
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Sets the line color defined at the time of construction. Default value: Quantity_NOC_YELLOW
        """
    def SetTypeOfLine(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Sets the type of line defined at the time of construction. This could, for example, be solid, dotted or made up of dashes. Default value: Aspect_TOL_SOLID
        """
    def SetWidth(self,theWidth : float) -> None: 
        """
        Sets the line width defined at the time of construction. Default value: 1.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theAspect : OCP.Graphic3d.Graphic3d_AspectLine3d) -> None: ...
    @overload
    def __init__(self,theColor : OCP.Quantity.Quantity_Color,theType : OCP.Aspect.Aspect_TypeOfLine,theWidth : float) -> None: ...
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
class Prs3d_IsoAspect(Prs3d_LineAspect, Prs3d_BasicAspect, OCP.Standard.Standard_Transient):
    """
    A framework to define the display attributes of isoparameters. This framework can be used to modify the default setting for isoparameters in Prs3d_Drawer.A framework to define the display attributes of isoparameters. This framework can be used to modify the default setting for isoparameters in Prs3d_Drawer.
    """
    def Aspect(self) -> OCP.Graphic3d.Graphic3d_AspectLine3d: 
        """
        Returns the line aspect. This is defined as the set of color, type and thickness attributes.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
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
    def Number(self) -> int: 
        """
        returns the number of U or V isoparametric curves drawn for a single face.
        """
    def SetAspect(self,theAspect : OCP.Graphic3d.Graphic3d_AspectLine3d) -> None: 
        """
        None
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Sets the line color defined at the time of construction. Default value: Quantity_NOC_YELLOW
        """
    def SetNumber(self,theNumber : int) -> None: 
        """
        defines the number of U or V isoparametric curves to be drawn for a single face. Default value: 10
        """
    def SetTypeOfLine(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Sets the type of line defined at the time of construction. This could, for example, be solid, dotted or made up of dashes. Default value: Aspect_TOL_SOLID
        """
    def SetWidth(self,theWidth : float) -> None: 
        """
        Sets the line width defined at the time of construction. Default value: 1.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theColor : OCP.Quantity.Quantity_Color,theType : OCP.Aspect.Aspect_TypeOfLine,theWidth : float,theNumber : int) -> None: ...
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
class Prs3d_NListOfSequenceOfPnt(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : Prs3d_NListOfSequenceOfPnt) -> None: ...
    @overload
    def Append(self,theItem : OCP.TColgp.TColgp_HSequenceOfPnt,theIter : Any) -> None: ...
    def Assign(self,theOther : Prs3d_NListOfSequenceOfPnt) -> Prs3d_NListOfSequenceOfPnt: 
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
    def First(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : Prs3d_NListOfSequenceOfPnt,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OCP.TColgp.TColgp_HSequenceOfPnt,theIter : Any) -> OCP.TColgp.TColgp_HSequenceOfPnt: ...
    @overload
    def InsertBefore(self,theItem : OCP.TColgp.TColgp_HSequenceOfPnt,theIter : Any) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : Prs3d_NListOfSequenceOfPnt,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.TColgp.TColgp_HSequenceOfPnt) -> OCP.TColgp.TColgp_HSequenceOfPnt: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : Prs3d_NListOfSequenceOfPnt) -> None: ...
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
    def __init__(self,theOther : Prs3d_NListOfSequenceOfPnt) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Prs3d_PlaneAspect(Prs3d_BasicAspect, OCP.Standard.Standard_Transient):
    """
    A framework to define the display of planes.A framework to define the display of planes.
    """
    def ArrowAspect(self) -> Prs3d_LineAspect: 
        """
        Returns the settings for displaying an arrow.
        """
    def ArrowsAngle(self) -> float: 
        """
        Returns the angle of the arrowhead used in the display of arrows involved in the presentation of planes.
        """
    def ArrowsLength(self) -> float: 
        """
        Returns the length of the arrow shaft used in the display of arrows.
        """
    def ArrowsSize(self) -> float: 
        """
        Returns the size of arrows used in the display of planes.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisplayCenterArrow(self) -> bool: 
        """
        Returns true if the display of center arrows is allowed.
        """
    def DisplayEdges(self) -> bool: 
        """
        None
        """
    def DisplayEdgesArrows(self) -> bool: 
        """
        Returns true if the display of edge arrows is allowed.
        """
    def DisplayIso(self) -> bool: 
        """
        Returns true if the display of isoparameters is allowed.
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EdgesAspect(self) -> Prs3d_LineAspect: 
        """
        Returns the attributes of displayed edges involved in the presentation of planes.
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
    def IsoAspect(self) -> Prs3d_LineAspect: 
        """
        Returns the attributes of displayed isoparameters involved in the presentation of planes.
        """
    def IsoDistance(self) -> float: 
        """
        Returns the distance between isoparameters used in the display of planes.
        """
    def PlaneXLength(self) -> float: 
        """
        Returns the length of the x axis used in the display of planes.
        """
    def PlaneYLength(self) -> float: 
        """
        Returns the length of the y axis used in the display of planes.
        """
    def SetArrowsAngle(self,theAngle : float) -> None: 
        """
        Sets the angle of the arrowhead used in the display of arrows involved in the presentation of planes.
        """
    def SetArrowsLength(self,theLength : float) -> None: 
        """
        None
        """
    def SetArrowsSize(self,theSize : float) -> None: 
        """
        Sets the angle of the arrowhead used in the display of planes.
        """
    def SetDisplayCenterArrow(self,theToDraw : bool) -> None: 
        """
        Sets the display attributes defined in DisplayCenterArrow to active.
        """
    def SetDisplayEdges(self,theToDraw : bool) -> None: 
        """
        None
        """
    def SetDisplayEdgesArrows(self,theToDraw : bool) -> None: 
        """
        Sets the display attributes defined in DisplayEdgesArrows to active.
        """
    def SetDisplayIso(self,theToDraw : bool) -> None: 
        """
        Sets the display attributes defined in DisplayIso to active.
        """
    def SetIsoDistance(self,theL : float) -> None: 
        """
        Sets the distance L between isoparameters used in the display of planes.
        """
    def SetPlaneLength(self,theLX : float,theLY : float) -> None: 
        """
        None
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
class Prs3d_PointAspect(Prs3d_BasicAspect, OCP.Standard.Standard_Transient):
    """
    This class defines attributes for the points The points are drawn using markers, whose size does not depend on the zoom value of the views.This class defines attributes for the points The points are drawn using markers, whose size does not depend on the zoom value of the views.
    """
    def Aspect(self) -> OCP.Graphic3d.Graphic3d_AspectMarker3d: 
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
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
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
    def GetTexture(self) -> OCP.Graphic3d.Graphic3d_MarkerImage: 
        """
        Returns marker's texture.
        """
    def GetTextureSize(self) -> Tuple[int, int]: 
        """
        Returns marker's texture size.
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
    def SetAspect(self,theAspect : OCP.Graphic3d.Graphic3d_AspectMarker3d) -> None: 
        """
        None
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        defines the color to be used when drawing a point. Default value: Quantity_NOC_YELLOW
        """
    def SetScale(self,theScale : float) -> None: 
        """
        defines the size of the marker used when drawing a point. Default value: 1.
        """
    def SetTypeOfMarker(self,theType : OCP.Aspect.Aspect_TypeOfMarker) -> None: 
        """
        defines the type of representation to be used when drawing a point. Default value: Aspect_TOM_PLUS
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theType : OCP.Aspect.Aspect_TypeOfMarker,theColor : OCP.Quantity.Quantity_Color,theScale : float) -> None: ...
    @overload
    def __init__(self,theColor : OCP.Quantity.Quantity_Color,theWidth : int,theHeight : int,theTexture : OCP.TColStd.TColStd_HArray1OfByte) -> None: ...
    @overload
    def __init__(self,theAspect : OCP.Graphic3d.Graphic3d_AspectMarker3d) -> None: ...
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
class Prs3d_PresentationShadow(OCP.Graphic3d.Graphic3d_Structure, OCP.Standard.Standard_Transient):
    """
    Defines a "shadow" of existing presentation object with custom aspects.Defines a "shadow" of existing presentation object with custom aspects.
    """
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
        Do nothing - axis-aligned bounding box should be initialized from parent structure.
        """
    def Clear(self,WithDestruction : bool=True) -> None: 
        """
        if WithDestruction == Standard_True then suppress all the groups of primitives in the structure. and it is mandatory to create a new group in <me>. if WithDestruction == Standard_False then clears all the groups of primitives in the structure. and all the groups are conserved and empty. They will be erased at the next screen update. The structure itself is conserved. The transformation and the attributes of <me> are conserved. The childs of <me> are conserved.
        """
    def ClipPlanes(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Get clip planes slicing the structure on rendering.
        """
    @overload
    def Compute(self,theProjector : OCP.Graphic3d.Graphic3d_DataStructureManager) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        None

        Returns the new Structure defined for the new visualization

        Returns the new Structure defined for the new visualization

        Returns the new Structure defined for the new visualization

        Returns the new Structure defined for the new visualization
        """
    @overload
    def Compute(self,theProjector : OCP.Graphic3d.Graphic3d_DataStructureManager,theTrsf : OCP.Geom.Geom_Transformation) -> OCP.Graphic3d.Graphic3d_Structure: ...
    @overload
    def Compute(self) -> None: ...
    @overload
    def Compute(self,theProjector : OCP.Graphic3d.Graphic3d_DataStructureManager,theStructure : OCP.Graphic3d.Graphic3d_Structure) -> Any: ...
    @overload
    def Compute(self,theProjector : OCP.Graphic3d.Graphic3d_DataStructureManager,theTrsf : OCP.Geom.Geom_Transformation,theStructure : OCP.Graphic3d.Graphic3d_Structure) -> Any: ...
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
        Displays the structure <me> in all the views of the visualiser.
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
        Erases the structure <me> in all the views of the visualiser.
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
    def Highlight(self,theStyle : OCP.Graphic3d.Graphic3d_PresentationAttributes,theToUpdateMgr : bool=True) -> None: 
        """
        Highlights the structure in all the views with the given style
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
        Returns the display indicator for this structure.
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
    def ParentAffinity(self) -> OCP.Graphic3d.Graphic3d_ViewAffinity: 
        """
        Returns view affinity of the parent presentation
        """
    def ParentId(self) -> int: 
        """
        Returns the id of the parent presentation
        """
    @staticmethod
    def PrintNetwork_s(AStructure : OCP.Graphic3d.Graphic3d_Structure,AType : OCP.Graphic3d.Graphic3d_TypeOfConnection) -> None: 
        """
        Prints informations about the network associated with the structure <AStructure>.
        """
    @overload
    def ReCompute(self) -> None: 
        """
        Forces a new construction of the structure <me> if <me> is displayed and TOS_COMPUTED.

        Forces a new construction of the structure <me> if <me> is displayed in <aProjetor> and TOS_COMPUTED.
        """
    @overload
    def ReCompute(self,aProjector : OCP.Graphic3d.Graphic3d_DataStructureManager) -> None: ...
    @overload
    def Remove(self,thePrs : OCP.Graphic3d.Graphic3d_Structure) -> None: 
        """
        Suppress the structure <me>. It will be erased at the next screen update. Warning: No more graphic operations in <me> after this call. Category: Methods to modify the class definition

        None

        Suppress the structure in the list of descendants or in the list of ancestors.
        """
    @overload
    def Remove(self) -> None: ...
    @overload
    def Remove(self,thePtr : OCP.Graphic3d.Graphic3d_Structure,theType : OCP.Graphic3d.Graphic3d_TypeOfConnection) -> None: ...
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
    def Visual(self) -> OCP.Graphic3d.Graphic3d_TypeOfStructure: 
        """
        Returns the visualisation mode for the structure <me>.
        """
    def __init__(self,theViewer : OCP.Graphic3d.Graphic3d_StructureManager,thePrs : OCP.Graphic3d.Graphic3d_Structure) -> None: ...
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
class Prs3d_Projector(OCP.Standard.Standard_Transient):
    """
    A projector object. This object defines the parameters of a view for a visualization algorithm. It is, for example, used by the hidden line removal algorithms.A projector object. This object defines the parameters of a view for a visualization algorithm. It is, for example, used by the hidden line removal algorithms.A projector object. This object defines the parameters of a view for a visualization algorithm. It is, for example, used by the hidden line removal algorithms.
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
    def Projector(self) -> OCP.HLRAlgo.HLRAlgo_Projector: 
        """
        Returns a projector object for use in a hidden line removal algorithm.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,Pr : OCP.HLRAlgo.HLRAlgo_Projector) -> None: ...
    @overload
    def __init__(self,Pers : bool,Focus : float,DX : float,DY : float,DZ : float,XAt : float,YAt : float,ZAt : float,XUp : float,YUp : float,ZUp : float) -> None: ...
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
class Prs3d_Arrow(Prs3d_Root):
    """
    Provides class methods to draw an arrow at a given location, along a given direction and using a given angle.
    """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    def DrawSegments_s(theLocation : OCP.gp.gp_Pnt,theDir : OCP.gp.gp_Dir,theAngle : float,theLength : float,theNbSegments : int) -> OCP.Graphic3d.Graphic3d_ArrayOfSegments: 
        """
        Defines the representation of the arrow as a container of segments.
        """
    @staticmethod
    def DrawShaded_s(theAxis : OCP.gp.gp_Ax1,theTubeRadius : float,theAxisLength : float,theConeRadius : float,theConeLength : float,theNbFacettes : int) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: 
        """
        Defines the representation of the arrow as shaded triangulation.
        """
    @staticmethod
    @overload
    def Draw_s(theGroup : OCP.Graphic3d.Graphic3d_Group,theLocation : OCP.gp.gp_Pnt,theDirection : OCP.gp.gp_Dir,theAngle : float,theLength : float) -> None: 
        """
        Defines the representation of the arrow. Note that this method does NOT assign any presentation aspects to the primitives group!

        Alias to another method Draw() for backward compatibility.
        """
    @staticmethod
    @overload
    def Draw_s(thePrs : OCP.Graphic3d.Graphic3d_Structure,theLocation : OCP.gp.gp_Pnt,theDirection : OCP.gp.gp_Dir,theAngle : float,theLength : float) -> None: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
    pass
class Prs3d_ShadingAspect(Prs3d_BasicAspect, OCP.Standard.Standard_Transient):
    """
    A framework to define the display of shading. The attributes which make up this definition include: - fill aspect - color, and - materialA framework to define the display of shading. The attributes which make up this definition include: - fill aspect - color, and - material
    """
    def Aspect(self) -> OCP.Graphic3d.Graphic3d_AspectFillArea3d: 
        """
        Returns the polygons aspect properties.
        """
    def Color(self,aModel : OCP.Aspect.Aspect_TypeOfFacingModel=Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the polygons color.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
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
    def Material(self,aModel : OCP.Aspect.Aspect_TypeOfFacingModel=Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE) -> OCP.Graphic3d.Graphic3d_MaterialAspect: 
        """
        Returns the polygons material aspect.
        """
    def SetAspect(self,theAspect : OCP.Graphic3d.Graphic3d_AspectFillArea3d) -> None: 
        """
        None
        """
    def SetColor(self,aColor : OCP.Quantity.Quantity_Color,aModel : OCP.Aspect.Aspect_TypeOfFacingModel=Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None: 
        """
        Change the polygons interior color and material ambient color.
        """
    def SetMaterial(self,aMaterial : OCP.Graphic3d.Graphic3d_MaterialAspect,aModel : OCP.Aspect.Aspect_TypeOfFacingModel=Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None: 
        """
        Change the polygons material aspect.
        """
    def SetTransparency(self,aValue : float,aModel : OCP.Aspect.Aspect_TypeOfFacingModel=Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None: 
        """
        Change the polygons transparency value. Warning : aValue must be in the range 0,1. 0 is the default (NO transparent)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transparency(self,aModel : OCP.Aspect.Aspect_TypeOfFacingModel=Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE) -> float: 
        """
        Returns the polygons transparency value.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAspect : OCP.Graphic3d.Graphic3d_AspectFillArea3d) -> None: ...
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
class Prs3d_ShapeTool():
    """
    describes the behaviour requested for a wireframe shape presentation.
    """
    def CurrentTriangulation(self,l : OCP.TopLoc.TopLoc_Location) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def CurveBound(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def FaceBound(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def FacesOfEdge(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        None
        """
    def GetCurve(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def GetFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def GetVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def HasCurve(self) -> bool: 
        """
        None
        """
    def HasSurface(self) -> bool: 
        """
        None
        """
    def InitCurve(self) -> None: 
        """
        None
        """
    def InitFace(self) -> None: 
        """
        None
        """
    def InitVertex(self) -> None: 
        """
        None
        """
    def IsPlanarFace(self) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPlanarFace_s(theFace : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def MoreCurve(self) -> bool: 
        """
        None
        """
    def MoreFace(self) -> bool: 
        """
        None
        """
    def MoreVertex(self) -> bool: 
        """
        None
        """
    def Neighbours(self) -> int: 
        """
        None
        """
    def NextCurve(self) -> None: 
        """
        None
        """
    def NextFace(self) -> None: 
        """
        None
        """
    def NextVertex(self) -> None: 
        """
        None
        """
    def Polygon3D(self,l : OCP.TopLoc.TopLoc_Location) -> OCP.Poly.Poly_Polygon3D: 
        """
        None
        """
    def PolygonOnTriangulation(self,Indices : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation,l : OCP.TopLoc.TopLoc_Location) -> Any: 
        """
        None
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape,theAllVertices : bool=False) -> None: ...
    pass
class Prs3d_Text(Prs3d_Root):
    """
    A framework to define the display of texts.
    """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    @overload
    def Draw_s(theGroup : OCP.Graphic3d.Graphic3d_Group,theAspect : Prs3d_TextAspect,theText : OCP.TCollection.TCollection_ExtendedString,theOrientation : OCP.gp.gp_Ax2,theHasOwnAnchor : bool=True) -> None: 
        """
        Defines the display of the text.

        Draws the text label.

        Alias to another method Draw() for backward compatibility.

        Alias to another method Draw() for backward compatibility.

        Alias to another method Draw() for backward compatibility.
        """
    @staticmethod
    @overload
    def Draw_s(thePrs : OCP.Graphic3d.Graphic3d_Structure,theDrawer : Prs3d_Drawer,theText : OCP.TCollection.TCollection_ExtendedString,theAttachmentPoint : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def Draw_s(thePrs : OCP.Graphic3d.Graphic3d_Structure,theAspect : Prs3d_TextAspect,theText : OCP.TCollection.TCollection_ExtendedString,theOrientation : OCP.gp.gp_Ax2,theHasOwnAnchor : bool=True) -> None: ...
    @staticmethod
    @overload
    def Draw_s(thePrs : OCP.Graphic3d.Graphic3d_Structure,theAspect : Prs3d_TextAspect,theText : OCP.TCollection.TCollection_ExtendedString,theAttachmentPoint : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def Draw_s(theGroup : OCP.Graphic3d.Graphic3d_Group,theAspect : Prs3d_TextAspect,theText : OCP.TCollection.TCollection_ExtendedString,theAttachmentPoint : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
    pass
class Prs3d_TextAspect(Prs3d_BasicAspect, OCP.Standard.Standard_Transient):
    """
    Defines the attributes when displaying a text.Defines the attributes when displaying a text.
    """
    def Angle(self) -> float: 
        """
        Returns the angle
        """
    def Aspect(self) -> OCP.Graphic3d.Graphic3d_AspectText3d: 
        """
        Returns the purely textual attributes used in the display of text. These include: - color - font - height/width ratio, that is, the expansion factor, and - space between characters.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
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
    def Height(self) -> float: 
        """
        Returns the height of the text box.
        """
    def HorizontalJustification(self) -> OCP.Graphic3d.Graphic3d_HorizontalTextAlignment: 
        """
        Returns the horizontal alignment of the text. The range of values includes: - left - center - right, and - normal (justified).
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
    def Orientation(self) -> OCP.Graphic3d.Graphic3d_TextPath: 
        """
        Returns the orientation of the text. Text can be displayed in the following directions: - up - down - left, or - right
        """
    def SetAngle(self,theAngle : float) -> None: 
        """
        Sets the angle
        """
    def SetAspect(self,theAspect : OCP.Graphic3d.Graphic3d_AspectText3d) -> None: 
        """
        None
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Sets the color of the type used in text display.
        """
    def SetFont(self,theFont : str) -> None: 
        """
        Sets the font used in text display.
        """
    def SetHeight(self,theHeight : float) -> None: 
        """
        Sets the height of the text.
        """
    def SetHorizontalJustification(self,theJustification : OCP.Graphic3d.Graphic3d_HorizontalTextAlignment) -> None: 
        """
        Sets horizontal alignment of text.
        """
    def SetOrientation(self,theOrientation : OCP.Graphic3d.Graphic3d_TextPath) -> None: 
        """
        Sets the orientation of text.
        """
    def SetVerticalJustification(self,theJustification : OCP.Graphic3d.Graphic3d_VerticalTextAlignment) -> None: 
        """
        Sets the vertical alignment of text.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def VerticalJustification(self) -> OCP.Graphic3d.Graphic3d_VerticalTextAlignment: 
        """
        Returns the vertical alignment of the text. The range of values includes: - normal - top - cap - half - base - bottom
        """
    @overload
    def __init__(self,theAspect : OCP.Graphic3d.Graphic3d_AspectText3d) -> None: ...
    @overload
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
class Prs3d_ToolQuadric():
    """
    Base class to build 3D surfaces presentation of quadric surfaces.
    """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTriangulation : OCP.Poly.Poly_Triangulation,theTrsf : OCP.gp.gp_Trsf) -> Any: 
        """
        Generate primitives for 3D quadric surface and fill the given array. Optional transformation is applied.

        Generate primitives for 3D quadric surface presentation and fill the given array and poly triangulation structure. Optional transformation is applied.
        """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTrsf : OCP.gp.gp_Trsf) -> Any: ...
    @staticmethod
    def TrianglesNb_s(theSlicesNb : int,theStacksNb : int) -> int: 
        """
        Number of triangles for presentation with the given params.
        """
    pass
class Prs3d_ToolDisk(Prs3d_ToolQuadric):
    """
    Standard presentation algorithm that outputs graphical primitives for disk surface.
    """
    @staticmethod
    def Create_s(theInnerRadius : float,theOuterRadius : float,theNbSlices : int,theNbStacks : int,theTrsf : OCP.gp.gp_Trsf) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: 
        """
        Generate primitives for 3D quadric surface and return a filled array.
        """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTriangulation : OCP.Poly.Poly_Triangulation,theTrsf : OCP.gp.gp_Trsf) -> Any: 
        """
        Generate primitives for 3D quadric surface and fill the given array. Optional transformation is applied.

        Generate primitives for 3D quadric surface presentation and fill the given array and poly triangulation structure. Optional transformation is applied.
        """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTrsf : OCP.gp.gp_Trsf) -> Any: ...
    def SetAngleRange(self,theStartAngle : float,theEndAngle : float) -> None: 
        """
        Set angle range in radians [0, 2*PI] by default.
        """
    @staticmethod
    def TrianglesNb_s(theSlicesNb : int,theStacksNb : int) -> int: 
        """
        Number of triangles for presentation with the given params.
        """
    def __init__(self,theInnerRadius : float,theOuterRadius : float,theNbSlices : int,theNbStacks : int) -> None: ...
    pass
class Prs3d_ToolCylinder(Prs3d_ToolQuadric):
    """
    Standard presentation algorithm that outputs graphical primitives for cylindrical surface.
    """
    @staticmethod
    def Create_s(theBottomRad : float,theTopRad : float,theHeight : float,theNbSlices : int,theNbStacks : int,theTrsf : OCP.gp.gp_Trsf) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: 
        """
        Generate primitives for 3D quadric surface and return a filled array.
        """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTriangulation : OCP.Poly.Poly_Triangulation,theTrsf : OCP.gp.gp_Trsf) -> Any: 
        """
        Generate primitives for 3D quadric surface and fill the given array. Optional transformation is applied.

        Generate primitives for 3D quadric surface presentation and fill the given array and poly triangulation structure. Optional transformation is applied.
        """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTrsf : OCP.gp.gp_Trsf) -> Any: ...
    @staticmethod
    def TrianglesNb_s(theSlicesNb : int,theStacksNb : int) -> int: 
        """
        Number of triangles for presentation with the given params.
        """
    def __init__(self,theBottomRad : float,theTopRad : float,theHeight : float,theNbSlices : int,theNbStacks : int) -> None: ...
    pass
class Prs3d_ToolSector(Prs3d_ToolQuadric):
    """
    Standard presentation algorithm that outputs graphical primitives for disk surface.
    """
    @staticmethod
    def Create_s(theRadius : float,theNbSlices : int,theNbStacks : int,theTrsf : OCP.gp.gp_Trsf) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: 
        """
        Generate primitives for 3D quadric surface and return a filled array.
        """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTriangulation : OCP.Poly.Poly_Triangulation,theTrsf : OCP.gp.gp_Trsf) -> Any: 
        """
        Generate primitives for 3D quadric surface and fill the given array. Optional transformation is applied.

        Generate primitives for 3D quadric surface presentation and fill the given array and poly triangulation structure. Optional transformation is applied.
        """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTrsf : OCP.gp.gp_Trsf) -> Any: ...
    @staticmethod
    def TrianglesNb_s(theSlicesNb : int,theStacksNb : int) -> int: 
        """
        Number of triangles for presentation with the given params.
        """
    def __init__(self,theRadius : float,theNbSlices : int,theNbStacks : int) -> None: ...
    pass
class Prs3d_ToolSphere(Prs3d_ToolQuadric):
    """
    Standard presentation algorithm that outputs graphical primitives for spherical surface.
    """
    @staticmethod
    def Create_s(theRadius : float,theNbSlices : int,theNbStacks : int,theTrsf : OCP.gp.gp_Trsf) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: 
        """
        Generate primitives for 3D quadric surface and return a filled array.
        """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTriangulation : OCP.Poly.Poly_Triangulation,theTrsf : OCP.gp.gp_Trsf) -> Any: 
        """
        Generate primitives for 3D quadric surface and fill the given array. Optional transformation is applied.

        Generate primitives for 3D quadric surface presentation and fill the given array and poly triangulation structure. Optional transformation is applied.
        """
    @overload
    def FillArray(self,theArray : OCP.Graphic3d.Graphic3d_ArrayOfTriangles,theTrsf : OCP.gp.gp_Trsf) -> Any: ...
    @staticmethod
    def TrianglesNb_s(theSlicesNb : int,theStacksNb : int) -> int: 
        """
        Number of triangles for presentation with the given params.
        """
    def __init__(self,theRadius : float,theNbSlices : int,theNbStacks : int) -> None: ...
    pass
class Prs3d_TypeOfHLR():
    """
    Declares types of hidden line removal algorithm. TOH_Algo enables using of exact HLR algorithm. TOH_PolyAlgo enables using of polygonal HLR algorithm. TOH_NotSet is used by Prs3d_Drawer class, it means that the drawer should return the global value. For more details see Prs3d_Drawer class, AIS_Shape::Compute() method and HLRAlgo package from TKHLR toolkit.

    Members:

      Prs3d_TOH_NotSet

      Prs3d_TOH_PolyAlgo

      Prs3d_TOH_Algo
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_TOH_Algo: OCP.Prs3d.Prs3d_TypeOfHLR # value = Prs3d_TypeOfHLR.Prs3d_TOH_Algo
    Prs3d_TOH_NotSet: OCP.Prs3d.Prs3d_TypeOfHLR # value = Prs3d_TypeOfHLR.Prs3d_TOH_NotSet
    Prs3d_TOH_PolyAlgo: OCP.Prs3d.Prs3d_TypeOfHLR # value = Prs3d_TypeOfHLR.Prs3d_TOH_PolyAlgo
    __entries: dict # value = {'Prs3d_TOH_NotSet': (Prs3d_TypeOfHLR.Prs3d_TOH_NotSet, None), 'Prs3d_TOH_PolyAlgo': (Prs3d_TypeOfHLR.Prs3d_TOH_PolyAlgo, None), 'Prs3d_TOH_Algo': (Prs3d_TypeOfHLR.Prs3d_TOH_Algo, None)}
    __members__: dict # value = {'Prs3d_TOH_NotSet': Prs3d_TypeOfHLR.Prs3d_TOH_NotSet, 'Prs3d_TOH_PolyAlgo': Prs3d_TypeOfHLR.Prs3d_TOH_PolyAlgo, 'Prs3d_TOH_Algo': Prs3d_TypeOfHLR.Prs3d_TOH_Algo}
    pass
class Prs3d_TypeOfHighlight():
    """
    Type of highlighting to apply specific style.

    Members:

      Prs3d_TypeOfHighlight_None

      Prs3d_TypeOfHighlight_Selected

      Prs3d_TypeOfHighlight_Dynamic

      Prs3d_TypeOfHighlight_LocalSelected

      Prs3d_TypeOfHighlight_LocalDynamic

      Prs3d_TypeOfHighlight_SubIntensity

      Prs3d_TypeOfHighlight_NB
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_TypeOfHighlight_Dynamic: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_Dynamic
    Prs3d_TypeOfHighlight_LocalDynamic: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_LocalDynamic
    Prs3d_TypeOfHighlight_LocalSelected: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_LocalSelected
    Prs3d_TypeOfHighlight_NB: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_NB
    Prs3d_TypeOfHighlight_None: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_None
    Prs3d_TypeOfHighlight_Selected: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_Selected
    Prs3d_TypeOfHighlight_SubIntensity: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_SubIntensity
    __entries: dict # value = {'Prs3d_TypeOfHighlight_None': (Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_None, None), 'Prs3d_TypeOfHighlight_Selected': (Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_Selected, None), 'Prs3d_TypeOfHighlight_Dynamic': (Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_Dynamic, None), 'Prs3d_TypeOfHighlight_LocalSelected': (Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_LocalSelected, None), 'Prs3d_TypeOfHighlight_LocalDynamic': (Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_LocalDynamic, None), 'Prs3d_TypeOfHighlight_SubIntensity': (Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_SubIntensity, None), 'Prs3d_TypeOfHighlight_NB': (Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_NB, None)}
    __members__: dict # value = {'Prs3d_TypeOfHighlight_None': Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_None, 'Prs3d_TypeOfHighlight_Selected': Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_Selected, 'Prs3d_TypeOfHighlight_Dynamic': Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_Dynamic, 'Prs3d_TypeOfHighlight_LocalSelected': Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_LocalSelected, 'Prs3d_TypeOfHighlight_LocalDynamic': Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_LocalDynamic, 'Prs3d_TypeOfHighlight_SubIntensity': Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_SubIntensity, 'Prs3d_TypeOfHighlight_NB': Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_NB}
    pass
class Prs3d_TypeOfLinePicking():
    """
    None

    Members:

      Prs3d_TOLP_Point

      Prs3d_TOLP_Segment
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_TOLP_Point: OCP.Prs3d.Prs3d_TypeOfLinePicking # value = Prs3d_TypeOfLinePicking.Prs3d_TOLP_Point
    Prs3d_TOLP_Segment: OCP.Prs3d.Prs3d_TypeOfLinePicking # value = Prs3d_TypeOfLinePicking.Prs3d_TOLP_Segment
    __entries: dict # value = {'Prs3d_TOLP_Point': (Prs3d_TypeOfLinePicking.Prs3d_TOLP_Point, None), 'Prs3d_TOLP_Segment': (Prs3d_TypeOfLinePicking.Prs3d_TOLP_Segment, None)}
    __members__: dict # value = {'Prs3d_TOLP_Point': Prs3d_TypeOfLinePicking.Prs3d_TOLP_Point, 'Prs3d_TOLP_Segment': Prs3d_TypeOfLinePicking.Prs3d_TOLP_Segment}
    pass
class Prs3d_VertexDrawMode():
    """
    Describes supported modes of visualization of the shape's vertices: VDM_Isolated - only isolated vertices (not belonging to a face) are displayed. VDM_All - all vertices of the shape are displayed. VDM_Inherited - the global settings are inherited and applied to the shape's presentation.

    Members:

      Prs3d_VDM_Isolated

      Prs3d_VDM_All

      Prs3d_VDM_Inherited
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Prs3d_VDM_All: OCP.Prs3d.Prs3d_VertexDrawMode # value = Prs3d_VertexDrawMode.Prs3d_VDM_All
    Prs3d_VDM_Inherited: OCP.Prs3d.Prs3d_VertexDrawMode # value = Prs3d_VertexDrawMode.Prs3d_VDM_Inherited
    Prs3d_VDM_Isolated: OCP.Prs3d.Prs3d_VertexDrawMode # value = Prs3d_VertexDrawMode.Prs3d_VDM_Isolated
    __entries: dict # value = {'Prs3d_VDM_Isolated': (Prs3d_VertexDrawMode.Prs3d_VDM_Isolated, None), 'Prs3d_VDM_All': (Prs3d_VertexDrawMode.Prs3d_VDM_All, None), 'Prs3d_VDM_Inherited': (Prs3d_VertexDrawMode.Prs3d_VDM_Inherited, None)}
    __members__: dict # value = {'Prs3d_VDM_Isolated': Prs3d_VertexDrawMode.Prs3d_VDM_Isolated, 'Prs3d_VDM_All': Prs3d_VertexDrawMode.Prs3d_VDM_All, 'Prs3d_VDM_Inherited': Prs3d_VertexDrawMode.Prs3d_VDM_Inherited}
    pass
Prs3d_DAO_External: OCP.Prs3d.Prs3d_DimensionArrowOrientation # value = Prs3d_DimensionArrowOrientation.Prs3d_DAO_External
Prs3d_DAO_Fit: OCP.Prs3d.Prs3d_DimensionArrowOrientation # value = Prs3d_DimensionArrowOrientation.Prs3d_DAO_Fit
Prs3d_DAO_Internal: OCP.Prs3d.Prs3d_DimensionArrowOrientation # value = Prs3d_DimensionArrowOrientation.Prs3d_DAO_Internal
Prs3d_DA_XAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_XAxis
Prs3d_DA_XAxisLength: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DA_XAxisLength
Prs3d_DA_XYAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_XYAxis
Prs3d_DA_XYZAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_XYZAxis
Prs3d_DA_XZAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_XZAxis
Prs3d_DA_YAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_YAxis
Prs3d_DA_YAxisLength: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DA_YAxisLength
Prs3d_DA_YZAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_YZAxis
Prs3d_DA_ZAxis: OCP.Prs3d.Prs3d_DatumAxes # value = Prs3d_DatumAxes.Prs3d_DA_ZAxis
Prs3d_DA_ZAxisLength: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DA_ZAxisLength
Prs3d_DM_Shaded: OCP.Prs3d.Prs3d_DatumMode # value = Prs3d_DatumMode.Prs3d_DM_Shaded
Prs3d_DM_WireFrame: OCP.Prs3d.Prs3d_DatumMode # value = Prs3d_DatumMode.Prs3d_DM_WireFrame
Prs3d_DP_None: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_None
Prs3d_DP_Origin: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_Origin
Prs3d_DP_ShadingConeLengthPercent: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingConeLengthPercent
Prs3d_DP_ShadingConeRadiusPercent: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingConeRadiusPercent
Prs3d_DP_ShadingNumberOfFacettes: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingNumberOfFacettes
Prs3d_DP_ShadingOriginRadiusPercent: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingOriginRadiusPercent
Prs3d_DP_ShadingTubeRadiusPercent: OCP.Prs3d.Prs3d_DatumAttribute # value = Prs3d_DatumAttribute.Prs3d_DP_ShadingTubeRadiusPercent
Prs3d_DP_XArrow: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_XArrow
Prs3d_DP_XAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_XAxis
Prs3d_DP_XOYAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_XOYAxis
Prs3d_DP_XOZAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_XOZAxis
Prs3d_DP_YArrow: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_YArrow
Prs3d_DP_YAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_YAxis
Prs3d_DP_YOZAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_YOZAxis
Prs3d_DP_ZArrow: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_ZArrow
Prs3d_DP_ZAxis: OCP.Prs3d.Prs3d_DatumParts # value = Prs3d_DatumParts.Prs3d_DP_ZAxis
Prs3d_DTHP_Center: OCP.Prs3d.Prs3d_DimensionTextHorizontalPosition # value = Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Center
Prs3d_DTHP_Fit: OCP.Prs3d.Prs3d_DimensionTextHorizontalPosition # value = Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Fit
Prs3d_DTHP_Left: OCP.Prs3d.Prs3d_DimensionTextHorizontalPosition # value = Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Left
Prs3d_DTHP_Right: OCP.Prs3d.Prs3d_DimensionTextHorizontalPosition # value = Prs3d_DimensionTextHorizontalPosition.Prs3d_DTHP_Right
Prs3d_DTVP_Above: OCP.Prs3d.Prs3d_DimensionTextVerticalPosition # value = Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Above
Prs3d_DTVP_Below: OCP.Prs3d.Prs3d_DimensionTextVerticalPosition # value = Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Below
Prs3d_DTVP_Center: OCP.Prs3d.Prs3d_DimensionTextVerticalPosition # value = Prs3d_DimensionTextVerticalPosition.Prs3d_DTVP_Center
Prs3d_TOH_Algo: OCP.Prs3d.Prs3d_TypeOfHLR # value = Prs3d_TypeOfHLR.Prs3d_TOH_Algo
Prs3d_TOH_NotSet: OCP.Prs3d.Prs3d_TypeOfHLR # value = Prs3d_TypeOfHLR.Prs3d_TOH_NotSet
Prs3d_TOH_PolyAlgo: OCP.Prs3d.Prs3d_TypeOfHLR # value = Prs3d_TypeOfHLR.Prs3d_TOH_PolyAlgo
Prs3d_TOLP_Point: OCP.Prs3d.Prs3d_TypeOfLinePicking # value = Prs3d_TypeOfLinePicking.Prs3d_TOLP_Point
Prs3d_TOLP_Segment: OCP.Prs3d.Prs3d_TypeOfLinePicking # value = Prs3d_TypeOfLinePicking.Prs3d_TOLP_Segment
Prs3d_TypeOfHighlight_Dynamic: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_Dynamic
Prs3d_TypeOfHighlight_LocalDynamic: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_LocalDynamic
Prs3d_TypeOfHighlight_LocalSelected: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_LocalSelected
Prs3d_TypeOfHighlight_NB: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_NB
Prs3d_TypeOfHighlight_None: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_None
Prs3d_TypeOfHighlight_Selected: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_Selected
Prs3d_TypeOfHighlight_SubIntensity: OCP.Prs3d.Prs3d_TypeOfHighlight # value = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_SubIntensity
Prs3d_VDM_All: OCP.Prs3d.Prs3d_VertexDrawMode # value = Prs3d_VertexDrawMode.Prs3d_VDM_All
Prs3d_VDM_Inherited: OCP.Prs3d.Prs3d_VertexDrawMode # value = Prs3d_VertexDrawMode.Prs3d_VDM_Inherited
Prs3d_VDM_Isolated: OCP.Prs3d.Prs3d_VertexDrawMode # value = Prs3d_VertexDrawMode.Prs3d_VDM_Isolated
