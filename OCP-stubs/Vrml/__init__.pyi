import OCP.Vrml
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.TCollection
import OCP.Quantity
import OCP.TColgp
import OCP.Standard
import OCP.gp
__all__  = [
"Vrml",
"Vrml_AsciiText",
"Vrml_AsciiTextJustification",
"Vrml_Cone",
"Vrml_ConeParts",
"Vrml_Coordinate3",
"Vrml_Cube",
"Vrml_Cylinder",
"Vrml_CylinderParts",
"Vrml_DirectionalLight",
"Vrml_FaceType",
"Vrml_FontStyle",
"Vrml_FontStyleFamily",
"Vrml_FontStyleStyle",
"Vrml_Group",
"Vrml_IndexedFaceSet",
"Vrml_IndexedLineSet",
"Vrml_Info",
"Vrml_Instancing",
"Vrml_LOD",
"Vrml_Material",
"Vrml_MaterialBinding",
"Vrml_MaterialBindingAndNormalBinding",
"Vrml_MatrixTransform",
"Vrml_Normal",
"Vrml_NormalBinding",
"Vrml_OrthographicCamera",
"Vrml_PerspectiveCamera",
"Vrml_PointLight",
"Vrml_PointSet",
"Vrml_Rotation",
"Vrml_SFImage",
"Vrml_SFImageNumber",
"Vrml_SFRotation",
"Vrml_Scale",
"Vrml_Separator",
"Vrml_SeparatorRenderCulling",
"Vrml_ShapeHints",
"Vrml_ShapeType",
"Vrml_Sphere",
"Vrml_SpotLight",
"Vrml_Switch",
"Vrml_Texture2",
"Vrml_Texture2Transform",
"Vrml_Texture2Wrap",
"Vrml_TextureCoordinate2",
"Vrml_Transform",
"Vrml_TransformSeparator",
"Vrml_Translation",
"Vrml_VertexOrdering",
"Vrml_WWWAnchor",
"Vrml_WWWAnchorMap",
"Vrml_WWWInline",
"Vrml_AUTO",
"Vrml_BOLD",
"Vrml_CENTER",
"Vrml_CLAMP",
"Vrml_CLOCKWISE",
"Vrml_CONVEX",
"Vrml_COUNTERCLOCKWISE",
"Vrml_ConeALL",
"Vrml_ConeBOTTOM",
"Vrml_ConeSIDES",
"Vrml_CylinderALL",
"Vrml_CylinderBOTTOM",
"Vrml_CylinderSIDES",
"Vrml_CylinderTOP",
"Vrml_DEFAULT",
"Vrml_FOUR",
"Vrml_ITALIC",
"Vrml_LEFT",
"Vrml_MAP_NONE",
"Vrml_NONE",
"Vrml_NULL",
"Vrml_OFF",
"Vrml_ON",
"Vrml_ONE",
"Vrml_OVERALL",
"Vrml_PER_FACE",
"Vrml_PER_FACE_INDEXED",
"Vrml_PER_PART",
"Vrml_PER_PART_INDEXED",
"Vrml_PER_VERTEX",
"Vrml_PER_VERTEX_INDEXED",
"Vrml_POINT",
"Vrml_REPEAT",
"Vrml_RIGHT",
"Vrml_SANS",
"Vrml_SERIF",
"Vrml_SOLID",
"Vrml_THREE",
"Vrml_TWO",
"Vrml_TYPEWRITER",
"Vrml_UNKNOWN_FACE_TYPE",
"Vrml_UNKNOWN_ORDERING",
"Vrml_UNKNOWN_SHAPE_TYPE"
]
class Vrml():
    """
    Vrml package implements the specification of the VRML ( Virtual Reality Modeling Language ). VRML is a standard language for describing interactive 3-D objects and worlds delivered across Internet. Actual version of Vrml package have made for objects of VRML version 1.0. This package is used by VrmlConverter package. The developer should already be familiar with VRML specification before using this package.
    """
    @staticmethod
    def CommentWriter_s(aComment : str,anOStream : Any) -> Any: 
        """
        None
        """
    @staticmethod
    def VrmlHeaderWriter_s(anOStream : Any) -> Any: 
        """
        Writes a header in anOStream (VRML file). Writes one line of commentary in anOStream (VRML file).
        """
    def __init__(self) -> None: ...
    pass
class Vrml_AsciiText(OCP.Standard.Standard_Transient):
    """
    defines a AsciiText node of VRML specifying geometry shapes. This node represents strings of text characters from ASCII coded character set. All subsequent strings advance y by -( size * spacing). The justification field determines the placement of the strings in the x dimension. LEFT (the default) places the left edge of each string at x=0. CENTER places the center of each string at x=0. RIGHT places the right edge of each string at x=0. Text is rendered from left to right, top to bottom in the font set by FontStyle. The default value for the wigth field indicates the natural width should be used for that string.defines a AsciiText node of VRML specifying geometry shapes. This node represents strings of text characters from ASCII coded character set. All subsequent strings advance y by -( size * spacing). The justification field determines the placement of the strings in the x dimension. LEFT (the default) places the left edge of each string at x=0. CENTER places the center of each string at x=0. RIGHT places the right edge of each string at x=0. Text is rendered from left to right, top to bottom in the font set by FontStyle. The default value for the wigth field indicates the natural width should be used for that string.defines a AsciiText node of VRML specifying geometry shapes. This node represents strings of text characters from ASCII coded character set. All subsequent strings advance y by -( size * spacing). The justification field determines the placement of the strings in the x dimension. LEFT (the default) places the left edge of each string at x=0. CENTER places the center of each string at x=0. RIGHT places the right edge of each string at x=0. Text is rendered from left to right, top to bottom in the font set by FontStyle. The default value for the wigth field indicates the natural width should be used for that string.
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
    def Justification(self) -> Vrml_AsciiTextJustification: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetJustification(self,aJustification : Vrml_AsciiTextJustification) -> None: 
        """
        None
        """
    def SetSpacing(self,aSpacing : float) -> None: 
        """
        None
        """
    def SetString(self,aString : OCP.TColStd.TColStd_HArray1OfAsciiString) -> None: 
        """
        None
        """
    def SetWidth(self,aWidth : float) -> None: 
        """
        None
        """
    def Spacing(self) -> float: 
        """
        None
        """
    def String(self) -> OCP.TColStd.TColStd_HArray1OfAsciiString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Width(self) -> float: 
        """
        None
        """
    @overload
    def __init__(self,aString : OCP.TColStd.TColStd_HArray1OfAsciiString,aSpacing : float,aJustification : Vrml_AsciiTextJustification,aWidth : float) -> None: ...
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
class Vrml_AsciiTextJustification():
    """
    None

    Members:

      Vrml_LEFT

      Vrml_CENTER

      Vrml_RIGHT
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
    Vrml_CENTER: OCP.Vrml.Vrml_AsciiTextJustification # value = Vrml_AsciiTextJustification.Vrml_CENTER
    Vrml_LEFT: OCP.Vrml.Vrml_AsciiTextJustification # value = Vrml_AsciiTextJustification.Vrml_LEFT
    Vrml_RIGHT: OCP.Vrml.Vrml_AsciiTextJustification # value = Vrml_AsciiTextJustification.Vrml_RIGHT
    __entries: dict # value = {'Vrml_LEFT': (Vrml_AsciiTextJustification.Vrml_LEFT, None), 'Vrml_CENTER': (Vrml_AsciiTextJustification.Vrml_CENTER, None), 'Vrml_RIGHT': (Vrml_AsciiTextJustification.Vrml_RIGHT, None)}
    __members__: dict # value = {'Vrml_LEFT': Vrml_AsciiTextJustification.Vrml_LEFT, 'Vrml_CENTER': Vrml_AsciiTextJustification.Vrml_CENTER, 'Vrml_RIGHT': Vrml_AsciiTextJustification.Vrml_RIGHT}
    pass
class Vrml_Cone():
    """
    defines a Cone node of VRML specifying geometry shapes. This node represents a simple cone, whose central axis is aligned with the y-axis. By default , the cone is centred at (0,0,0) and has size of -1 to +1 in the all three directions. the cone has a radius of 1 at the bottom and height of 2, with its apex at 1 and its bottom at -1. The cone has two parts: the sides and the bottom
    """
    def BottomRadius(self) -> float: 
        """
        None
        """
    def Height(self) -> float: 
        """
        None
        """
    def Parts(self) -> Vrml_ConeParts: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetBottomRadius(self,aBottomRadius : float) -> None: 
        """
        None
        """
    def SetHeight(self,aHeight : float) -> None: 
        """
        None
        """
    def SetParts(self,aParts : Vrml_ConeParts) -> None: 
        """
        None
        """
    def __init__(self,aParts : Vrml_ConeParts=Vrml_ConeParts.Vrml_ConeALL,aBottomRadius : float=1.0,aHeight : float=2.0) -> None: ...
    pass
class Vrml_ConeParts():
    """
    None

    Members:

      Vrml_ConeSIDES

      Vrml_ConeBOTTOM

      Vrml_ConeALL
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
    Vrml_ConeALL: OCP.Vrml.Vrml_ConeParts # value = Vrml_ConeParts.Vrml_ConeALL
    Vrml_ConeBOTTOM: OCP.Vrml.Vrml_ConeParts # value = Vrml_ConeParts.Vrml_ConeBOTTOM
    Vrml_ConeSIDES: OCP.Vrml.Vrml_ConeParts # value = Vrml_ConeParts.Vrml_ConeSIDES
    __entries: dict # value = {'Vrml_ConeSIDES': (Vrml_ConeParts.Vrml_ConeSIDES, None), 'Vrml_ConeBOTTOM': (Vrml_ConeParts.Vrml_ConeBOTTOM, None), 'Vrml_ConeALL': (Vrml_ConeParts.Vrml_ConeALL, None)}
    __members__: dict # value = {'Vrml_ConeSIDES': Vrml_ConeParts.Vrml_ConeSIDES, 'Vrml_ConeBOTTOM': Vrml_ConeParts.Vrml_ConeBOTTOM, 'Vrml_ConeALL': Vrml_ConeParts.Vrml_ConeALL}
    pass
class Vrml_Coordinate3(OCP.Standard.Standard_Transient):
    """
    defines a Coordinate3 node of VRML specifying properties of geometry and its appearance. This node defines a set of 3D coordinates to be used by a subsequent IndexedFaceSet, IndexedLineSet, or PointSet node. This node does not produce a visible result during rendering; it simply replaces the current coordinates in the rendering state for subsequent nodes to use.defines a Coordinate3 node of VRML specifying properties of geometry and its appearance. This node defines a set of 3D coordinates to be used by a subsequent IndexedFaceSet, IndexedLineSet, or PointSet node. This node does not produce a visible result during rendering; it simply replaces the current coordinates in the rendering state for subsequent nodes to use.defines a Coordinate3 node of VRML specifying properties of geometry and its appearance. This node defines a set of 3D coordinates to be used by a subsequent IndexedFaceSet, IndexedLineSet, or PointSet node. This node does not produce a visible result during rendering; it simply replaces the current coordinates in the rendering state for subsequent nodes to use.
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
    def Point(self) -> OCP.TColgp.TColgp_HArray1OfVec: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetPoint(self,aPoint : OCP.TColgp.TColgp_HArray1OfVec) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aPoint : OCP.TColgp.TColgp_HArray1OfVec) -> None: ...
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
class Vrml_Cube():
    """
    defines a Cube node of VRML specifying geometry shapes. This node represents a cuboid aligned with the coordinate axes. By default , the cube is centred at (0,0,0) and measures 2 units in each dimension, from -1 to +1. A cube's width is its extent along its object-space X axis, its height is its extent along the object-space Y axis, and its depth is its extent along its object-space Z axis.
    """
    def Depth(self) -> float: 
        """
        None
        """
    def Height(self) -> float: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetDepth(self,aDepth : float) -> None: 
        """
        None
        """
    def SetHeight(self,aHeight : float) -> None: 
        """
        None
        """
    def SetWidth(self,aWidth : float) -> None: 
        """
        None
        """
    def Width(self) -> float: 
        """
        None
        """
    def __init__(self,aWidth : float=2.0,aHeight : float=2.0,aDepth : float=2.0) -> None: ...
    pass
class Vrml_Cylinder():
    """
    defines a Cylinder node of VRML specifying geometry shapes. This node represents a simple capped cylinder centred around the y-axis. By default , the cylinder is centred at (0,0,0) and has size of -1 to +1 in the all three dimensions. The cylinder has three parts: the sides, the top (y=+1) and the bottom (y=-1)
    """
    def Height(self) -> float: 
        """
        None
        """
    def Parts(self) -> Vrml_CylinderParts: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def Radius(self) -> float: 
        """
        None
        """
    def SetHeight(self,aHeight : float) -> None: 
        """
        None
        """
    def SetParts(self,aParts : Vrml_CylinderParts) -> None: 
        """
        None
        """
    def SetRadius(self,aRadius : float) -> None: 
        """
        None
        """
    def __init__(self,aParts : Vrml_CylinderParts=Vrml_CylinderParts.Vrml_CylinderALL,aRadius : float=1.0,aHeight : float=2.0) -> None: ...
    pass
class Vrml_CylinderParts():
    """
    None

    Members:

      Vrml_CylinderSIDES

      Vrml_CylinderTOP

      Vrml_CylinderBOTTOM

      Vrml_CylinderALL
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
    Vrml_CylinderALL: OCP.Vrml.Vrml_CylinderParts # value = Vrml_CylinderParts.Vrml_CylinderALL
    Vrml_CylinderBOTTOM: OCP.Vrml.Vrml_CylinderParts # value = Vrml_CylinderParts.Vrml_CylinderBOTTOM
    Vrml_CylinderSIDES: OCP.Vrml.Vrml_CylinderParts # value = Vrml_CylinderParts.Vrml_CylinderSIDES
    Vrml_CylinderTOP: OCP.Vrml.Vrml_CylinderParts # value = Vrml_CylinderParts.Vrml_CylinderTOP
    __entries: dict # value = {'Vrml_CylinderSIDES': (Vrml_CylinderParts.Vrml_CylinderSIDES, None), 'Vrml_CylinderTOP': (Vrml_CylinderParts.Vrml_CylinderTOP, None), 'Vrml_CylinderBOTTOM': (Vrml_CylinderParts.Vrml_CylinderBOTTOM, None), 'Vrml_CylinderALL': (Vrml_CylinderParts.Vrml_CylinderALL, None)}
    __members__: dict # value = {'Vrml_CylinderSIDES': Vrml_CylinderParts.Vrml_CylinderSIDES, 'Vrml_CylinderTOP': Vrml_CylinderParts.Vrml_CylinderTOP, 'Vrml_CylinderBOTTOM': Vrml_CylinderParts.Vrml_CylinderBOTTOM, 'Vrml_CylinderALL': Vrml_CylinderParts.Vrml_CylinderALL}
    pass
class Vrml_DirectionalLight():
    """
    defines a directional light node of VRML specifying properties of lights. This node defines a directional light source that illuminates along rays parallel to a given 3-dimentional vector Color is written as an RGB triple. Light intensity must be in the range 0.0 to 1.0, inclusive.
    """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        None
        """
    def Direction(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Intensity(self) -> float: 
        """
        None
        """
    def OnOff(self) -> bool: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetColor(self,aColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        None
        """
    def SetDirection(self,aDirection : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetIntensity(self,aIntensity : float) -> None: 
        """
        None
        """
    def SetOnOff(self,aOnOff : bool) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aOnOff : bool,aIntensity : float,aColor : OCP.Quantity.Quantity_Color,aDirection : OCP.gp.gp_Vec) -> None: ...
    pass
class Vrml_FaceType():
    """
    None

    Members:

      Vrml_UNKNOWN_FACE_TYPE

      Vrml_CONVEX
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
    Vrml_CONVEX: OCP.Vrml.Vrml_FaceType # value = Vrml_FaceType.Vrml_CONVEX
    Vrml_UNKNOWN_FACE_TYPE: OCP.Vrml.Vrml_FaceType # value = Vrml_FaceType.Vrml_UNKNOWN_FACE_TYPE
    __entries: dict # value = {'Vrml_UNKNOWN_FACE_TYPE': (Vrml_FaceType.Vrml_UNKNOWN_FACE_TYPE, None), 'Vrml_CONVEX': (Vrml_FaceType.Vrml_CONVEX, None)}
    __members__: dict # value = {'Vrml_UNKNOWN_FACE_TYPE': Vrml_FaceType.Vrml_UNKNOWN_FACE_TYPE, 'Vrml_CONVEX': Vrml_FaceType.Vrml_CONVEX}
    pass
class Vrml_FontStyle():
    """
    defines a FontStyle node of VRML of properties of geometry and its appearance. The size field specifies the height (in object space units) of glyphs rendered and determines the vertical spacing of adjacent lines of text.
    """
    def Family(self) -> Vrml_FontStyleFamily: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetFamily(self,aFamily : Vrml_FontStyleFamily) -> None: 
        """
        None
        """
    def SetSize(self,aSize : float) -> None: 
        """
        None
        """
    def SetStyle(self,aStyle : Vrml_FontStyleStyle) -> None: 
        """
        None
        """
    def Size(self) -> float: 
        """
        None
        """
    def Style(self) -> Vrml_FontStyleStyle: 
        """
        None
        """
    def __init__(self,aSize : float=10.0,aFamily : Vrml_FontStyleFamily=Vrml_FontStyleFamily.Vrml_SERIF,aStyle : Vrml_FontStyleStyle=Vrml_FontStyleStyle.Vrml_NONE) -> None: ...
    pass
class Vrml_FontStyleFamily():
    """
    None

    Members:

      Vrml_SERIF

      Vrml_SANS

      Vrml_TYPEWRITER
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
    Vrml_SANS: OCP.Vrml.Vrml_FontStyleFamily # value = Vrml_FontStyleFamily.Vrml_SANS
    Vrml_SERIF: OCP.Vrml.Vrml_FontStyleFamily # value = Vrml_FontStyleFamily.Vrml_SERIF
    Vrml_TYPEWRITER: OCP.Vrml.Vrml_FontStyleFamily # value = Vrml_FontStyleFamily.Vrml_TYPEWRITER
    __entries: dict # value = {'Vrml_SERIF': (Vrml_FontStyleFamily.Vrml_SERIF, None), 'Vrml_SANS': (Vrml_FontStyleFamily.Vrml_SANS, None), 'Vrml_TYPEWRITER': (Vrml_FontStyleFamily.Vrml_TYPEWRITER, None)}
    __members__: dict # value = {'Vrml_SERIF': Vrml_FontStyleFamily.Vrml_SERIF, 'Vrml_SANS': Vrml_FontStyleFamily.Vrml_SANS, 'Vrml_TYPEWRITER': Vrml_FontStyleFamily.Vrml_TYPEWRITER}
    pass
class Vrml_FontStyleStyle():
    """
    None

    Members:

      Vrml_NONE

      Vrml_BOLD

      Vrml_ITALIC
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
    Vrml_BOLD: OCP.Vrml.Vrml_FontStyleStyle # value = Vrml_FontStyleStyle.Vrml_BOLD
    Vrml_ITALIC: OCP.Vrml.Vrml_FontStyleStyle # value = Vrml_FontStyleStyle.Vrml_ITALIC
    Vrml_NONE: OCP.Vrml.Vrml_FontStyleStyle # value = Vrml_FontStyleStyle.Vrml_NONE
    __entries: dict # value = {'Vrml_NONE': (Vrml_FontStyleStyle.Vrml_NONE, None), 'Vrml_BOLD': (Vrml_FontStyleStyle.Vrml_BOLD, None), 'Vrml_ITALIC': (Vrml_FontStyleStyle.Vrml_ITALIC, None)}
    __members__: dict # value = {'Vrml_NONE': Vrml_FontStyleStyle.Vrml_NONE, 'Vrml_BOLD': Vrml_FontStyleStyle.Vrml_BOLD, 'Vrml_ITALIC': Vrml_FontStyleStyle.Vrml_ITALIC}
    pass
class Vrml_Group():
    """
    defines a Group node of VRML specifying group properties. This node defines the base class for all group nodes. Group is a node that contains an ordered list of child nodes. This node is simply a container for the child nodes and does not alter the traversal state in any way. During traversal, state accumulated for a child is passed on to each successive child and then to the parents of the group (Group does not push or pop traversal state as separator does).
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Vrml_IndexedFaceSet(OCP.Standard.Standard_Transient):
    """
    defines a IndexedFaceSet node of VRML specifying geometry shapes. This node represents a 3D shape formed by constructing faces (polygons) from vertices located at the current coordinates. IndexedFaceSet uses the indices in its coordIndex to define polygonal faces. An index of -1 separates faces (so a -1 at the end of the list is optional).defines a IndexedFaceSet node of VRML specifying geometry shapes. This node represents a 3D shape formed by constructing faces (polygons) from vertices located at the current coordinates. IndexedFaceSet uses the indices in its coordIndex to define polygonal faces. An index of -1 separates faces (so a -1 at the end of the list is optional).defines a IndexedFaceSet node of VRML specifying geometry shapes. This node represents a 3D shape formed by constructing faces (polygons) from vertices located at the current coordinates. IndexedFaceSet uses the indices in its coordIndex to define polygonal faces. An index of -1 separates faces (so a -1 at the end of the list is optional).
    """
    def CoordIndex(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
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
    def MaterialIndex(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def NormalIndex(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetCoordIndex(self,aCoordIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetMaterialIndex(self,aMaterialIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetNormalIndex(self,aNormalIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetTextureCoordIndex(self,aTextureCoordIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def TextureCoordIndex(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aCoordIndex : OCP.TColStd.TColStd_HArray1OfInteger,aMaterialIndex : OCP.TColStd.TColStd_HArray1OfInteger,aNormalIndex : OCP.TColStd.TColStd_HArray1OfInteger,aTextureCoordIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: ...
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
class Vrml_IndexedLineSet(OCP.Standard.Standard_Transient):
    """
    defines a IndexedLineSet node of VRML specifying geometry shapes. This node represents a 3D shape formed by constructing polylines from vertices located at the current coordinates. IndexedLineSet uses the indices in its coordIndex field to specify the polylines. An index of -1 separates one polyline from the next (thus, a final -1 is optional). the current polyline has ended and the next one begins. Treatment of the current material and normal binding is as follows: The PER_PART binding specifies a material or normal for each segment of the line. The PER_FACE binding specifies a material or normal for each polyline. PER_VERTEX specifies a material or normal for each vertex. The corresponding _INDEXED bindings are the same, but use the materialIndex or normalIndex indices. The DEFAULT material binding is equal to OVERALL. The DEFAULT normal binding is equal to PER_VERTEX_INDEXED; if insufficient normals exist in the state, the lines will be drawn unlit. The same rules for texture coordinate generation as IndexedFaceSet are used.defines a IndexedLineSet node of VRML specifying geometry shapes. This node represents a 3D shape formed by constructing polylines from vertices located at the current coordinates. IndexedLineSet uses the indices in its coordIndex field to specify the polylines. An index of -1 separates one polyline from the next (thus, a final -1 is optional). the current polyline has ended and the next one begins. Treatment of the current material and normal binding is as follows: The PER_PART binding specifies a material or normal for each segment of the line. The PER_FACE binding specifies a material or normal for each polyline. PER_VERTEX specifies a material or normal for each vertex. The corresponding _INDEXED bindings are the same, but use the materialIndex or normalIndex indices. The DEFAULT material binding is equal to OVERALL. The DEFAULT normal binding is equal to PER_VERTEX_INDEXED; if insufficient normals exist in the state, the lines will be drawn unlit. The same rules for texture coordinate generation as IndexedFaceSet are used.defines a IndexedLineSet node of VRML specifying geometry shapes. This node represents a 3D shape formed by constructing polylines from vertices located at the current coordinates. IndexedLineSet uses the indices in its coordIndex field to specify the polylines. An index of -1 separates one polyline from the next (thus, a final -1 is optional). the current polyline has ended and the next one begins. Treatment of the current material and normal binding is as follows: The PER_PART binding specifies a material or normal for each segment of the line. The PER_FACE binding specifies a material or normal for each polyline. PER_VERTEX specifies a material or normal for each vertex. The corresponding _INDEXED bindings are the same, but use the materialIndex or normalIndex indices. The DEFAULT material binding is equal to OVERALL. The DEFAULT normal binding is equal to PER_VERTEX_INDEXED; if insufficient normals exist in the state, the lines will be drawn unlit. The same rules for texture coordinate generation as IndexedFaceSet are used.
    """
    def CoordIndex(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
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
    def MaterialIndex(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def NormalIndex(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetCoordIndex(self,aCoordIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetMaterialIndex(self,aMaterialIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetNormalIndex(self,aNormalIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetTextureCoordIndex(self,aTextureCoordIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def TextureCoordIndex(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,aCoordIndex : OCP.TColStd.TColStd_HArray1OfInteger,aMaterialIndex : OCP.TColStd.TColStd_HArray1OfInteger,aNormalIndex : OCP.TColStd.TColStd_HArray1OfInteger,aTextureCoordIndex : OCP.TColStd.TColStd_HArray1OfInteger) -> None: ...
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
class Vrml_Info():
    """
    defines a Info node of VRML specifying properties of geometry and its appearance. It is used to store information in the scene graph, Typically for application-specific purposes, copyright messages, or other strings.
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetString(self,aString : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def __init__(self,aString : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    pass
class Vrml_Instancing():
    """
    defines "instancing" - using the same instance of a node multiple times. It is accomplished by using the "DEF" and "USE" keywords. The DEF keyword both defines a named node, and creates a single instance of it. The USE keyword indicates that the most recently defined instance should be used again. If several nades were given the same name, then the last DEF encountered during parsing "wins". DEF/USE is limited to a single file.
    """
    def DEF(self,anOStream : Any) -> Any: 
        """
        Adds "USE <myName>" in anOStream (VRML file).
        """
    def USE(self,anOStream : Any) -> Any: 
        """
        None
        """
    def __init__(self,aString : OCP.TCollection.TCollection_AsciiString) -> None: ...
    pass
class Vrml_LOD(OCP.Standard.Standard_Transient):
    """
    defines a LOD (level of detailization) node of VRML specifying properties of geometry and its appearance. This group node is used to allow applications to switch between various representations of objects automatically. The children of this node typically represent the same object or objects at the varying of Levels Of Detail (LOD), from highest detail to lowest.defines a LOD (level of detailization) node of VRML specifying properties of geometry and its appearance. This group node is used to allow applications to switch between various representations of objects automatically. The children of this node typically represent the same object or objects at the varying of Levels Of Detail (LOD), from highest detail to lowest.defines a LOD (level of detailization) node of VRML specifying properties of geometry and its appearance. This group node is used to allow applications to switch between various representations of objects automatically. The children of this node typically represent the same object or objects at the varying of Levels Of Detail (LOD), from highest detail to lowest.
    """
    def Center(self) -> OCP.gp.gp_Vec: 
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
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def Range(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def SetCenter(self,aCenter : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetRange(self,aRange : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aRange : OCP.TColStd.TColStd_HArray1OfReal,aCenter : OCP.gp.gp_Vec) -> None: ...
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
class Vrml_Material(OCP.Standard.Standard_Transient):
    """
    defines a Material node of VRML specifying properties of geometry and its appearance. This node defines the current surface material properties for all subsequent shapes. Material sets several components of the current material during traversal. Different shapes interpret materials with multiple values differently. To bind materials to shapes, use a MaterialBinding node.defines a Material node of VRML specifying properties of geometry and its appearance. This node defines the current surface material properties for all subsequent shapes. Material sets several components of the current material during traversal. Different shapes interpret materials with multiple values differently. To bind materials to shapes, use a MaterialBinding node.defines a Material node of VRML specifying properties of geometry and its appearance. This node defines the current surface material properties for all subsequent shapes. Material sets several components of the current material during traversal. Different shapes interpret materials with multiple values differently. To bind materials to shapes, use a MaterialBinding node.
    """
    def AmbientColor(self) -> OCP.Quantity.Quantity_HArray1OfColor: 
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
    def DiffuseColor(self) -> OCP.Quantity.Quantity_HArray1OfColor: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EmissiveColor(self) -> OCP.Quantity.Quantity_HArray1OfColor: 
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
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetAmbientColor(self,aAmbientColor : OCP.Quantity.Quantity_HArray1OfColor) -> None: 
        """
        None
        """
    def SetDiffuseColor(self,aDiffuseColor : OCP.Quantity.Quantity_HArray1OfColor) -> None: 
        """
        None
        """
    def SetEmissiveColor(self,aEmissiveColor : OCP.Quantity.Quantity_HArray1OfColor) -> None: 
        """
        None
        """
    def SetShininess(self,aShininess : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def SetSpecularColor(self,aSpecularColor : OCP.Quantity.Quantity_HArray1OfColor) -> None: 
        """
        None
        """
    def SetTransparency(self,aTransparency : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        None
        """
    def Shininess(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def SpecularColor(self) -> OCP.Quantity.Quantity_HArray1OfColor: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transparency(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    @overload
    def __init__(self,aAmbientColor : OCP.Quantity.Quantity_HArray1OfColor,aDiffuseColor : OCP.Quantity.Quantity_HArray1OfColor,aSpecularColor : OCP.Quantity.Quantity_HArray1OfColor,aEmissiveColor : OCP.Quantity.Quantity_HArray1OfColor,aShininess : OCP.TColStd.TColStd_HArray1OfReal,aTransparency : OCP.TColStd.TColStd_HArray1OfReal) -> None: ...
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
class Vrml_MaterialBinding():
    """
    defines a MaterialBinding node of VRML specifying properties of geometry and its appearance. Material nodes may contain more than one material. This node specifies how the current materials are bound to shapes that follow in the scene graph. Each shape node may interpret bindings differently. For example, a Sphere node is always drawn using the first material in the material node, no matter what the current MaterialBinding, while a Cube node may use six different materials to draw each of its six faces, depending on the MaterialBinding.
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetValue(self,aValue : Vrml_MaterialBindingAndNormalBinding) -> None: 
        """
        None
        """
    def Value(self) -> Vrml_MaterialBindingAndNormalBinding: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aValue : Vrml_MaterialBindingAndNormalBinding) -> None: ...
    pass
class Vrml_MaterialBindingAndNormalBinding():
    """
    None

    Members:

      Vrml_DEFAULT

      Vrml_OVERALL

      Vrml_PER_PART

      Vrml_PER_PART_INDEXED

      Vrml_PER_FACE

      Vrml_PER_FACE_INDEXED

      Vrml_PER_VERTEX

      Vrml_PER_VERTEX_INDEXED
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
    Vrml_DEFAULT: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_DEFAULT
    Vrml_OVERALL: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_OVERALL
    Vrml_PER_FACE: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE
    Vrml_PER_FACE_INDEXED: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE_INDEXED
    Vrml_PER_PART: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART
    Vrml_PER_PART_INDEXED: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART_INDEXED
    Vrml_PER_VERTEX: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX
    Vrml_PER_VERTEX_INDEXED: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX_INDEXED
    __entries: dict # value = {'Vrml_DEFAULT': (Vrml_MaterialBindingAndNormalBinding.Vrml_DEFAULT, None), 'Vrml_OVERALL': (Vrml_MaterialBindingAndNormalBinding.Vrml_OVERALL, None), 'Vrml_PER_PART': (Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART, None), 'Vrml_PER_PART_INDEXED': (Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART_INDEXED, None), 'Vrml_PER_FACE': (Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE, None), 'Vrml_PER_FACE_INDEXED': (Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE_INDEXED, None), 'Vrml_PER_VERTEX': (Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX, None), 'Vrml_PER_VERTEX_INDEXED': (Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX_INDEXED, None)}
    __members__: dict # value = {'Vrml_DEFAULT': Vrml_MaterialBindingAndNormalBinding.Vrml_DEFAULT, 'Vrml_OVERALL': Vrml_MaterialBindingAndNormalBinding.Vrml_OVERALL, 'Vrml_PER_PART': Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART, 'Vrml_PER_PART_INDEXED': Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART_INDEXED, 'Vrml_PER_FACE': Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE, 'Vrml_PER_FACE_INDEXED': Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE_INDEXED, 'Vrml_PER_VERTEX': Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX, 'Vrml_PER_VERTEX_INDEXED': Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX_INDEXED}
    pass
class Vrml_MatrixTransform():
    """
    defines a MatrixTransform node of VRML specifying matrix and transform properties. This node defines 3D transformation with a 4 by 4 matrix. By default : a11=1 a12=0 a13=0 a14=0 a21=0 a22=1 a23=0 a24=0 a31=0 a32=0 a33=1 a34=0 a41=0 a42=0 a43=0 a44=1 It is written to the file in row-major order as 16 Real numbers separated by whitespace. For example , matrix expressing a translation of 7.3 units along the X axis is written as: 1 0 0 0 0 1 0 0 0 0 1 0 7.3 0 0 1
    """
    def Matrix(self) -> OCP.gp.gp_Trsf: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetMatrix(self,aMatrix : OCP.gp.gp_Trsf) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aMatrix : OCP.gp.gp_Trsf) -> None: ...
    pass
class Vrml_Normal(OCP.Standard.Standard_Transient):
    """
    defines a Normal node of VRML specifying properties of geometry and its appearance. This node defines a set of 3D surface normal vectors to be used by vertex-based shape nodes (IndexedFaceSet, IndexedLineSet, PointSet) that follow it in the scene graph. This node does not produce a visible result during rendering; it simply replaces the current normals in the rendering state for subsequent nodes to use. This node contains one multiple-valued field that contains the normal vectors.defines a Normal node of VRML specifying properties of geometry and its appearance. This node defines a set of 3D surface normal vectors to be used by vertex-based shape nodes (IndexedFaceSet, IndexedLineSet, PointSet) that follow it in the scene graph. This node does not produce a visible result during rendering; it simply replaces the current normals in the rendering state for subsequent nodes to use. This node contains one multiple-valued field that contains the normal vectors.defines a Normal node of VRML specifying properties of geometry and its appearance. This node defines a set of 3D surface normal vectors to be used by vertex-based shape nodes (IndexedFaceSet, IndexedLineSet, PointSet) that follow it in the scene graph. This node does not produce a visible result during rendering; it simply replaces the current normals in the rendering state for subsequent nodes to use. This node contains one multiple-valued field that contains the normal vectors.
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
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetVector(self,aVector : OCP.TColgp.TColgp_HArray1OfVec) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vector(self) -> OCP.TColgp.TColgp_HArray1OfVec: 
        """
        None
        """
    @overload
    def __init__(self,aVector : OCP.TColgp.TColgp_HArray1OfVec) -> None: ...
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
class Vrml_NormalBinding():
    """
    defines a NormalBinding node of VRML specifying properties of geometry and its appearance. This node specifies how the current normals are bound to shapes that follow in the scene graph. Each shape node may interpret bindings differently. The bindings for faces and vertices are meaningful only for shapes that are made from faces and vertices. Similarly, the indexed bindings are only used by the shapes that allow indexing. For bindings that require multiple normals, be sure to have at least as many normals defined as are necessary; otherwise, errors will occur.
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetValue(self,aValue : Vrml_MaterialBindingAndNormalBinding) -> None: 
        """
        None
        """
    def Value(self) -> Vrml_MaterialBindingAndNormalBinding: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aValue : Vrml_MaterialBindingAndNormalBinding) -> None: ...
    pass
class Vrml_OrthographicCamera():
    """
    specifies a OrthographicCamera node of VRML specifying properties of cameras. An orthographic camera defines a parallel projection from a viewpoint. This camera does not diminish objects with distance, as a PerspectiveCamera does. The viewing volume for an orthographic camera is a rectangular parallelepiped (a box).
    """
    def FocalDistance(self) -> float: 
        """
        None
        """
    def Height(self) -> float: 
        """
        None
        """
    def Orientation(self) -> Vrml_SFRotation: 
        """
        None
        """
    def Position(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetFocalDistance(self,aFocalDistance : float) -> None: 
        """
        None
        """
    def SetHeight(self,aHeight : float) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : Vrml_SFRotation) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aPosition : OCP.gp.gp_Vec,aOrientation : Vrml_SFRotation,aFocalDistance : float,aHeight : float) -> None: ...
    pass
class Vrml_PerspectiveCamera():
    """
    specifies a PerspectiveCamera node of VRML specifying properties of cameras. A perspective camera defines a perspective projection from a viewpoint. The viewing volume for a perspective camera is a truncated right pyramid.
    """
    def Angle(self) -> float: 
        """
        None
        """
    def FocalDistance(self) -> float: 
        """
        None
        """
    def Orientation(self) -> Vrml_SFRotation: 
        """
        None
        """
    def Position(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetAngle(self,aHeightAngle : float) -> None: 
        """
        None
        """
    def SetFocalDistance(self,aFocalDistance : float) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : Vrml_SFRotation) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @overload
    def __init__(self,aPosition : OCP.gp.gp_Vec,aOrientation : Vrml_SFRotation,aFocalDistance : float,aHeightAngle : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Vrml_PointLight():
    """
    defines a point light node of VRML specifying properties of lights. This node defines a point light source at a fixed 3D location A point source illuminates equally in all directions; that is omni-directional. Color is written as an RGB triple. Light intensity must be in the range 0.0 to 1.0, inclusive.
    """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        None
        """
    def Intensity(self) -> float: 
        """
        None
        """
    def Location(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def OnOff(self) -> bool: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetColor(self,aColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        None
        """
    def SetIntensity(self,aIntensity : float) -> None: 
        """
        None
        """
    def SetLocation(self,aLocation : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetOnOff(self,aOnOff : bool) -> None: 
        """
        None
        """
    @overload
    def __init__(self,aOnOff : bool,aIntensity : float,aColor : OCP.Quantity.Quantity_Color,aLocation : OCP.gp.gp_Vec) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Vrml_PointSet():
    """
    defines a PointSet node of VRML specifying geometry shapes.
    """
    def NumPoints(self) -> int: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetNumPoints(self,aNumPoints : int) -> None: 
        """
        None
        """
    def SetStartIndex(self,aStartIndex : int) -> None: 
        """
        None
        """
    def StartIndex(self) -> int: 
        """
        None
        """
    def __init__(self,aStartIndex : int=0,aNumPoints : int=-1) -> None: ...
    pass
class Vrml_Rotation():
    """
    defines a Rotation node of VRML specifying matrix and transform properties. This node defines a 3D rotation about an arbitrary axis through the origin. By default : myRotation = (0 0 1 0)
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def Rotation(self) -> Vrml_SFRotation: 
        """
        None
        """
    def SetRotation(self,aRotation : Vrml_SFRotation) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aRotation : Vrml_SFRotation) -> None: ...
    pass
class Vrml_SFImage(OCP.Standard.Standard_Transient):
    """
    defines SFImage type of VRML field types.defines SFImage type of VRML field types.defines SFImage type of VRML field types.
    """
    def Array(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        None
        """
    def ArrayFlag(self) -> bool: 
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
    def Height(self) -> int: 
        """
        None
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
    def Number(self) -> Vrml_SFImageNumber: 
        """
        None
        """
    def SetArray(self,anArray : OCP.TColStd.TColStd_HArray1OfInteger) -> None: 
        """
        None
        """
    def SetHeight(self,aHeight : int) -> None: 
        """
        None
        """
    def SetNumber(self,aNumber : Vrml_SFImageNumber) -> None: 
        """
        None
        """
    def SetWidth(self,aWidth : int) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Width(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self,aWidth : int,aHeight : int,aNumber : Vrml_SFImageNumber,anArray : OCP.TColStd.TColStd_HArray1OfInteger) -> None: ...
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
class Vrml_SFImageNumber():
    """
    qualifies VRML geometry shapes.

    Members:

      Vrml_NULL

      Vrml_ONE

      Vrml_TWO

      Vrml_THREE

      Vrml_FOUR
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
    Vrml_FOUR: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_FOUR
    Vrml_NULL: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_NULL
    Vrml_ONE: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_ONE
    Vrml_THREE: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_THREE
    Vrml_TWO: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_TWO
    __entries: dict # value = {'Vrml_NULL': (Vrml_SFImageNumber.Vrml_NULL, None), 'Vrml_ONE': (Vrml_SFImageNumber.Vrml_ONE, None), 'Vrml_TWO': (Vrml_SFImageNumber.Vrml_TWO, None), 'Vrml_THREE': (Vrml_SFImageNumber.Vrml_THREE, None), 'Vrml_FOUR': (Vrml_SFImageNumber.Vrml_FOUR, None)}
    __members__: dict # value = {'Vrml_NULL': Vrml_SFImageNumber.Vrml_NULL, 'Vrml_ONE': Vrml_SFImageNumber.Vrml_ONE, 'Vrml_TWO': Vrml_SFImageNumber.Vrml_TWO, 'Vrml_THREE': Vrml_SFImageNumber.Vrml_THREE, 'Vrml_FOUR': Vrml_SFImageNumber.Vrml_FOUR}
    pass
class Vrml_SFRotation():
    """
    defines SFRotation type of VRML field types. The 4 values represent an axis of rotation followed by amount of right-handed rotation about the that axis, in radians.
    """
    def Angle(self) -> float: 
        """
        None
        """
    def RotationX(self) -> float: 
        """
        None
        """
    def RotationY(self) -> float: 
        """
        None
        """
    def RotationZ(self) -> float: 
        """
        None
        """
    def SetAngle(self,anAngle : float) -> None: 
        """
        None
        """
    def SetRotationX(self,aRotationX : float) -> None: 
        """
        None
        """
    def SetRotationY(self,aRotationY : float) -> None: 
        """
        None
        """
    def SetRotationZ(self,aRotationZ : float) -> None: 
        """
        None
        """
    @overload
    def __init__(self,aRotationX : float,aRotationY : float,aRotationZ : float,anAngle : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Vrml_Scale():
    """
    defines a Scale node of VRML specifying transform properties. This node defines a 3D scaling about the origin. By default : myRotation = (1 1 1)
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def ScaleFactor(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def SetScaleFactor(self,aScaleFactor : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @overload
    def __init__(self,aScaleFactor : OCP.gp.gp_Vec) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Vrml_Separator():
    """
    defines a Separator node of VRML specifying group properties. This group node performs a push (save) of the traversal state before traversing its children and a pop (restore) after traversing them. This isolates the separator's children from the rest of the scene graph. A separator can include lights, cameras, coordinates, normals, bindings, and all other properties. Separators can also perform render culling. Render culling skips over traversal of the separator's children if they are not going to be rendered, based on the comparison of the separator's bounding box with the current view volume. Culling is controlled by the renderCulling field. These are set to AUTO by default, allowing the implementation to decide whether or not to cull.
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def RenderCulling(self) -> Vrml_SeparatorRenderCulling: 
        """
        None
        """
    def SetRenderCulling(self,aRenderCulling : Vrml_SeparatorRenderCulling) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aRenderCulling : Vrml_SeparatorRenderCulling) -> None: ...
    pass
class Vrml_SeparatorRenderCulling():
    """
    None

    Members:

      Vrml_OFF

      Vrml_ON

      Vrml_AUTO
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
    Vrml_AUTO: OCP.Vrml.Vrml_SeparatorRenderCulling # value = Vrml_SeparatorRenderCulling.Vrml_AUTO
    Vrml_OFF: OCP.Vrml.Vrml_SeparatorRenderCulling # value = Vrml_SeparatorRenderCulling.Vrml_OFF
    Vrml_ON: OCP.Vrml.Vrml_SeparatorRenderCulling # value = Vrml_SeparatorRenderCulling.Vrml_ON
    __entries: dict # value = {'Vrml_OFF': (Vrml_SeparatorRenderCulling.Vrml_OFF, None), 'Vrml_ON': (Vrml_SeparatorRenderCulling.Vrml_ON, None), 'Vrml_AUTO': (Vrml_SeparatorRenderCulling.Vrml_AUTO, None)}
    __members__: dict # value = {'Vrml_OFF': Vrml_SeparatorRenderCulling.Vrml_OFF, 'Vrml_ON': Vrml_SeparatorRenderCulling.Vrml_ON, 'Vrml_AUTO': Vrml_SeparatorRenderCulling.Vrml_AUTO}
    pass
class Vrml_ShapeHints():
    """
    defines a ShapeHints node of VRML specifying properties of geometry and its appearance. The ShapeHints node indicates that IndexedFaceSets are solid, contain ordered vertices, or contain convex faces. These hints allow VRML implementations to optimize certain rendering features. Optimizations that may be performed include enabling back-face culling and disabling two-sided lighting. For example, if an object is solid and has ordered vertices, an implementation may turn on backface culling and turn off two-sided lighting. To ensure that an IndexedFaceSet can be viewed from either direction, set shapeType to be UNKNOWN_SHAPE_TYPE. If you know that your shapes are closed and will alwsys be viewed from the outside, set vertexOrdering to be either CLOCKWISE or COUNTERCLOCKWISE (depending on how you built your object), and set shapeType to be SOLID. Placing this near the top of your VRML file will allow the scene to be rendered much faster. The ShapeHints node also affects how default normals are generated. When an IndexedFaceSet has to generate default normals, it uses the creaseAngle field to determine which edges should be smoothly shaded and which ones should have a sharp crease. The crease angle is the angle between surface normals on adjacent polygons. For example, a crease angle of .5 radians (the default value) means that an edge between two adjacent polygonal faces will be smooth shaded if the normals to the two faces form an angle that is less than .5 radians (about 30 degrees). Otherwise, it will be faceted.
    """
    def Angle(self) -> float: 
        """
        None
        """
    def FaceType(self) -> Vrml_FaceType: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetAngle(self,aAngle : float) -> None: 
        """
        None
        """
    def SetFaceType(self,aFaceType : Vrml_FaceType) -> None: 
        """
        None
        """
    def SetShapeType(self,aShapeType : Vrml_ShapeType) -> None: 
        """
        None
        """
    def SetVertexOrdering(self,aVertexOrdering : Vrml_VertexOrdering) -> None: 
        """
        None
        """
    def ShapeType(self) -> Vrml_ShapeType: 
        """
        None
        """
    def VertexOrdering(self) -> Vrml_VertexOrdering: 
        """
        None
        """
    def __init__(self,aVertexOrdering : Vrml_VertexOrdering=Vrml_VertexOrdering.Vrml_UNKNOWN_ORDERING,aShapeType : Vrml_ShapeType=Vrml_ShapeType.Vrml_UNKNOWN_SHAPE_TYPE,aFaceType : Vrml_FaceType=Vrml_FaceType.Vrml_CONVEX,aAngle : float=0.5) -> None: ...
    pass
class Vrml_ShapeType():
    """
    None

    Members:

      Vrml_UNKNOWN_SHAPE_TYPE

      Vrml_SOLID
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
    Vrml_SOLID: OCP.Vrml.Vrml_ShapeType # value = Vrml_ShapeType.Vrml_SOLID
    Vrml_UNKNOWN_SHAPE_TYPE: OCP.Vrml.Vrml_ShapeType # value = Vrml_ShapeType.Vrml_UNKNOWN_SHAPE_TYPE
    __entries: dict # value = {'Vrml_UNKNOWN_SHAPE_TYPE': (Vrml_ShapeType.Vrml_UNKNOWN_SHAPE_TYPE, None), 'Vrml_SOLID': (Vrml_ShapeType.Vrml_SOLID, None)}
    __members__: dict # value = {'Vrml_UNKNOWN_SHAPE_TYPE': Vrml_ShapeType.Vrml_UNKNOWN_SHAPE_TYPE, 'Vrml_SOLID': Vrml_ShapeType.Vrml_SOLID}
    pass
class Vrml_Sphere():
    """
    defines a Sphere node of VRML specifying geometry shapes. This node represents a sphere. By default , the sphere is centred at (0,0,0) and has a radius of 1.
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def Radius(self) -> float: 
        """
        None
        """
    def SetRadius(self,aRadius : float) -> None: 
        """
        None
        """
    def __init__(self,aRadius : float=1.0) -> None: ...
    pass
class Vrml_SpotLight():
    """
    specifies a spot light node of VRML nodes specifying properties of lights. This node defines a spotlight light source. A spotlight is placed at a fixed location in 3D-space and illuminates in a cone along a particular direction. The intensity of the illumination drops off exponentially as a ray of light diverges from this direction toward the edges of cone. The rate of drop-off and agle of the cone are controlled by the dropOfRate and cutOffAngle Color is written as an RGB triple. Light intensity must be in the range 0.0 to 1.0, inclusive.
    """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        None
        """
    def CutOffAngle(self) -> float: 
        """
        None
        """
    def Direction(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def DropOffRate(self) -> float: 
        """
        None
        """
    def Intensity(self) -> float: 
        """
        None
        """
    def Location(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def OnOff(self) -> bool: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetColor(self,aColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        None
        """
    def SetCutOffAngle(self,aCutOffAngle : float) -> None: 
        """
        None
        """
    def SetDirection(self,aDirection : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetDropOffRate(self,aDropOffRate : float) -> None: 
        """
        None
        """
    def SetIntensity(self,aIntensity : float) -> None: 
        """
        None
        """
    def SetLocation(self,aLocation : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetOnOff(self,anOnOff : bool) -> None: 
        """
        None
        """
    @overload
    def __init__(self,aOnOff : bool,aIntensity : float,aColor : OCP.Quantity.Quantity_Color,aLocation : OCP.gp.gp_Vec,aDirection : OCP.gp.gp_Vec,aDropOffRate : float,aCutOffAngle : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Vrml_Switch():
    """
    defines a Switch node of VRML specifying group properties. This group node traverses one, none, or all of its children. One can use this node to switch on and off the effects of some properties or to switch between different properties. The whichChild field specifies the index of the child to traverse, where the first child has index 0. A value of -1 (the default) means do not traverse any children. A value of -3 traverses all children, making the switch behave exactly like a regular Group.
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetWhichChild(self,aWhichChild : int) -> None: 
        """
        None
        """
    def WhichChild(self) -> int: 
        """
        None
        """
    def __init__(self,aWhichChild : int=-1) -> None: ...
    pass
class Vrml_Texture2():
    """
    defines a Texture2 node of VRML specifying properties of geometry and its appearance. This property node defines a texture map and parameters for that map The texture can be read from the URL specified by the filename field. To turn off texturing, set the filename field to an empty string (""). Textures can alsobe specified inline by setting the image field to contain the texture data. By default : myFilename ("") myImage (0 0 0) myWrapS (Vrml_REPEAT) myWrapT (Vrml_REPEAT)
    """
    def Filename(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def Image(self) -> Vrml_SFImage: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetFilename(self,aFilename : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetImage(self,aImage : Vrml_SFImage) -> None: 
        """
        None
        """
    def SetWrapS(self,aWrapS : Vrml_Texture2Wrap) -> None: 
        """
        None
        """
    def SetWrapT(self,aWrapT : Vrml_Texture2Wrap) -> None: 
        """
        None
        """
    def WrapS(self) -> Vrml_Texture2Wrap: 
        """
        None
        """
    def WrapT(self) -> Vrml_Texture2Wrap: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aFilename : OCP.TCollection.TCollection_AsciiString,aImage : Vrml_SFImage,aWrapS : Vrml_Texture2Wrap,aWrapT : Vrml_Texture2Wrap) -> None: ...
    pass
class Vrml_Texture2Transform():
    """
    defines a Texture2Transform node of VRML specifying properties of geometry and its appearance. This node defines a 2D transformation applied to texture coordinates. This affect the way textures are applied to the surfaces of subsequent shapes. Transformation consisits of(in order) a non-uniform scale about an arbitrary center point, a rotation about that same point, and a translation. This allows a user to change the size and position of the textures on the shape. By default : myTranslation (0 0) myRotation (0) myScaleFactor (1 1) myCenter (0 0)
    """
    def Center(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def Rotation(self) -> float: 
        """
        None
        """
    def ScaleFactor(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    def SetCenter(self,aCenter : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def SetRotation(self,aRotation : float) -> None: 
        """
        None
        """
    def SetScaleFactor(self,aScaleFactor : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def SetTranslation(self,aTranslation : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def Translation(self) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    @overload
    def __init__(self,aTranslation : OCP.gp.gp_Vec2d,aRotation : float,aScaleFactor : OCP.gp.gp_Vec2d,aCenter : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Vrml_Texture2Wrap():
    """
    None

    Members:

      Vrml_REPEAT

      Vrml_CLAMP
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
    Vrml_CLAMP: OCP.Vrml.Vrml_Texture2Wrap # value = Vrml_Texture2Wrap.Vrml_CLAMP
    Vrml_REPEAT: OCP.Vrml.Vrml_Texture2Wrap # value = Vrml_Texture2Wrap.Vrml_REPEAT
    __entries: dict # value = {'Vrml_REPEAT': (Vrml_Texture2Wrap.Vrml_REPEAT, None), 'Vrml_CLAMP': (Vrml_Texture2Wrap.Vrml_CLAMP, None)}
    __members__: dict # value = {'Vrml_REPEAT': Vrml_Texture2Wrap.Vrml_REPEAT, 'Vrml_CLAMP': Vrml_Texture2Wrap.Vrml_CLAMP}
    pass
class Vrml_TextureCoordinate2(OCP.Standard.Standard_Transient):
    """
    defines a TextureCoordinate2 node of VRML specifying properties of geometry and its appearance. This node defines a set of 2D coordinates to be used to map textures to the vertices of subsequent PointSet, IndexedLineSet, or IndexedFaceSet objects. It replaces the current texture coordinates in the rendering state for the shapes to use. Texture coordinates range from 0 to 1 across the texture. The horizontal coordinate, called S, is specified first, followed by vertical coordinate, T. By default : myPoint (0 0)defines a TextureCoordinate2 node of VRML specifying properties of geometry and its appearance. This node defines a set of 2D coordinates to be used to map textures to the vertices of subsequent PointSet, IndexedLineSet, or IndexedFaceSet objects. It replaces the current texture coordinates in the rendering state for the shapes to use. Texture coordinates range from 0 to 1 across the texture. The horizontal coordinate, called S, is specified first, followed by vertical coordinate, T. By default : myPoint (0 0)defines a TextureCoordinate2 node of VRML specifying properties of geometry and its appearance. This node defines a set of 2D coordinates to be used to map textures to the vertices of subsequent PointSet, IndexedLineSet, or IndexedFaceSet objects. It replaces the current texture coordinates in the rendering state for the shapes to use. Texture coordinates range from 0 to 1 across the texture. The horizontal coordinate, called S, is specified first, followed by vertical coordinate, T. By default : myPoint (0 0)
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
    def Point(self) -> OCP.TColgp.TColgp_HArray1OfVec2d: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetPoint(self,aPoint : OCP.TColgp.TColgp_HArray1OfVec2d) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aPoint : OCP.TColgp.TColgp_HArray1OfVec2d) -> None: ...
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
class Vrml_Transform():
    """
    defines a Transform of VRML specifying transform properties. This node defines a geometric 3D transformation consisting of (in order) a (possibly) non-uniform scale about an arbitrary point, a rotation about an arbitrary point and axis and translation. By default : myTranslation (0,0,0) myRotation (0,0,1,0) myScaleFactor (1,1,1) myScaleOrientation (0,0,1,0) myCenter (0,0,0)
    """
    def Center(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def Rotation(self) -> Vrml_SFRotation: 
        """
        None
        """
    def ScaleFactor(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def ScaleOrientation(self) -> Vrml_SFRotation: 
        """
        None
        """
    def SetCenter(self,aCenter : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetRotation(self,aRotation : Vrml_SFRotation) -> None: 
        """
        None
        """
    def SetScaleFactor(self,aScaleFactor : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetScaleOrientation(self,aScaleOrientation : Vrml_SFRotation) -> None: 
        """
        None
        """
    def SetTranslation(self,aTranslation : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def Translation(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aTranslation : OCP.gp.gp_Vec,aRotation : Vrml_SFRotation,aScaleFactor : OCP.gp.gp_Vec,aScaleOrientation : Vrml_SFRotation,aCenter : OCP.gp.gp_Vec) -> None: ...
    pass
class Vrml_TransformSeparator():
    """
    defines a TransformSeparator node of VRML specifying group properties. This group node is similar to separator node in that it saves state before traversing its children and restores it afterwards. This node can be used to isolate transformations to light sources or objects.
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Vrml_Translation():
    """
    defines a Translation of VRML specifying transform properties. This node defines a translation by 3D vector. By default : myTranslation (0,0,0)
    """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetTranslation(self,aTranslation : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def Translation(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aTranslation : OCP.gp.gp_Vec) -> None: ...
    pass
class Vrml_VertexOrdering():
    """
    None

    Members:

      Vrml_UNKNOWN_ORDERING

      Vrml_CLOCKWISE

      Vrml_COUNTERCLOCKWISE
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
    Vrml_CLOCKWISE: OCP.Vrml.Vrml_VertexOrdering # value = Vrml_VertexOrdering.Vrml_CLOCKWISE
    Vrml_COUNTERCLOCKWISE: OCP.Vrml.Vrml_VertexOrdering # value = Vrml_VertexOrdering.Vrml_COUNTERCLOCKWISE
    Vrml_UNKNOWN_ORDERING: OCP.Vrml.Vrml_VertexOrdering # value = Vrml_VertexOrdering.Vrml_UNKNOWN_ORDERING
    __entries: dict # value = {'Vrml_UNKNOWN_ORDERING': (Vrml_VertexOrdering.Vrml_UNKNOWN_ORDERING, None), 'Vrml_CLOCKWISE': (Vrml_VertexOrdering.Vrml_CLOCKWISE, None), 'Vrml_COUNTERCLOCKWISE': (Vrml_VertexOrdering.Vrml_COUNTERCLOCKWISE, None)}
    __members__: dict # value = {'Vrml_UNKNOWN_ORDERING': Vrml_VertexOrdering.Vrml_UNKNOWN_ORDERING, 'Vrml_CLOCKWISE': Vrml_VertexOrdering.Vrml_CLOCKWISE, 'Vrml_COUNTERCLOCKWISE': Vrml_VertexOrdering.Vrml_COUNTERCLOCKWISE}
    pass
class Vrml_WWWAnchor():
    """
    defines a WWWAnchor node of VRML specifying group properties. The WWWAnchor group node loads a new scene into a VRML browser when one of its children is closen. Exactly how a user "chooses" a child of the WWWAnchor is up to the VRML browser. WWWAnchor with an empty ("") name does nothing when its children are chosen. WWWAnchor behaves like a Separator, pushing the traversal state before traversing its children and popping it afterwards.
    """
    def Description(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def Map(self) -> Vrml_WWWAnchorMap: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetMap(self,aMap : Vrml_WWWAnchorMap) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def __init__(self,aName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,aDescription : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,aMap : Vrml_WWWAnchorMap=Vrml_WWWAnchorMap.Vrml_MAP_NONE) -> None: ...
    pass
class Vrml_WWWAnchorMap():
    """
    None

    Members:

      Vrml_MAP_NONE

      Vrml_POINT
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
    Vrml_MAP_NONE: OCP.Vrml.Vrml_WWWAnchorMap # value = Vrml_WWWAnchorMap.Vrml_MAP_NONE
    Vrml_POINT: OCP.Vrml.Vrml_WWWAnchorMap # value = Vrml_WWWAnchorMap.Vrml_POINT
    __entries: dict # value = {'Vrml_MAP_NONE': (Vrml_WWWAnchorMap.Vrml_MAP_NONE, None), 'Vrml_POINT': (Vrml_WWWAnchorMap.Vrml_POINT, None)}
    __members__: dict # value = {'Vrml_MAP_NONE': Vrml_WWWAnchorMap.Vrml_MAP_NONE, 'Vrml_POINT': Vrml_WWWAnchorMap.Vrml_POINT}
    pass
class Vrml_WWWInline():
    """
    defines a WWWInline node of VRML specifying group properties. The WWWInline group node reads its children from anywhere in the World Wide Web. Exactly when its children are read is not defined; reading the children may be delayed until the WWWInline is actually displayed. WWWInline with an empty ("") name does nothing. WWWInline behaves like a Separator, pushing the traversal state before traversing its children and popping it afterwards. By defaults: myName ("") myBboxSize (0,0,0) myBboxCenter (0,0,0)
    """
    def BboxCenter(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def BboxSize(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def Print(self,anOStream : Any) -> Any: 
        """
        None
        """
    def SetBboxCenter(self,aBboxCenter : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetBboxSize(self,aBboxSize : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    @overload
    def __init__(self,aName : OCP.TCollection.TCollection_AsciiString,aBboxSize : OCP.gp.gp_Vec,aBboxCenter : OCP.gp.gp_Vec) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
Vrml_AUTO: OCP.Vrml.Vrml_SeparatorRenderCulling # value = Vrml_SeparatorRenderCulling.Vrml_AUTO
Vrml_BOLD: OCP.Vrml.Vrml_FontStyleStyle # value = Vrml_FontStyleStyle.Vrml_BOLD
Vrml_CENTER: OCP.Vrml.Vrml_AsciiTextJustification # value = Vrml_AsciiTextJustification.Vrml_CENTER
Vrml_CLAMP: OCP.Vrml.Vrml_Texture2Wrap # value = Vrml_Texture2Wrap.Vrml_CLAMP
Vrml_CLOCKWISE: OCP.Vrml.Vrml_VertexOrdering # value = Vrml_VertexOrdering.Vrml_CLOCKWISE
Vrml_CONVEX: OCP.Vrml.Vrml_FaceType # value = Vrml_FaceType.Vrml_CONVEX
Vrml_COUNTERCLOCKWISE: OCP.Vrml.Vrml_VertexOrdering # value = Vrml_VertexOrdering.Vrml_COUNTERCLOCKWISE
Vrml_ConeALL: OCP.Vrml.Vrml_ConeParts # value = Vrml_ConeParts.Vrml_ConeALL
Vrml_ConeBOTTOM: OCP.Vrml.Vrml_ConeParts # value = Vrml_ConeParts.Vrml_ConeBOTTOM
Vrml_ConeSIDES: OCP.Vrml.Vrml_ConeParts # value = Vrml_ConeParts.Vrml_ConeSIDES
Vrml_CylinderALL: OCP.Vrml.Vrml_CylinderParts # value = Vrml_CylinderParts.Vrml_CylinderALL
Vrml_CylinderBOTTOM: OCP.Vrml.Vrml_CylinderParts # value = Vrml_CylinderParts.Vrml_CylinderBOTTOM
Vrml_CylinderSIDES: OCP.Vrml.Vrml_CylinderParts # value = Vrml_CylinderParts.Vrml_CylinderSIDES
Vrml_CylinderTOP: OCP.Vrml.Vrml_CylinderParts # value = Vrml_CylinderParts.Vrml_CylinderTOP
Vrml_DEFAULT: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_DEFAULT
Vrml_FOUR: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_FOUR
Vrml_ITALIC: OCP.Vrml.Vrml_FontStyleStyle # value = Vrml_FontStyleStyle.Vrml_ITALIC
Vrml_LEFT: OCP.Vrml.Vrml_AsciiTextJustification # value = Vrml_AsciiTextJustification.Vrml_LEFT
Vrml_MAP_NONE: OCP.Vrml.Vrml_WWWAnchorMap # value = Vrml_WWWAnchorMap.Vrml_MAP_NONE
Vrml_NONE: OCP.Vrml.Vrml_FontStyleStyle # value = Vrml_FontStyleStyle.Vrml_NONE
Vrml_NULL: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_NULL
Vrml_OFF: OCP.Vrml.Vrml_SeparatorRenderCulling # value = Vrml_SeparatorRenderCulling.Vrml_OFF
Vrml_ON: OCP.Vrml.Vrml_SeparatorRenderCulling # value = Vrml_SeparatorRenderCulling.Vrml_ON
Vrml_ONE: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_ONE
Vrml_OVERALL: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_OVERALL
Vrml_PER_FACE: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE
Vrml_PER_FACE_INDEXED: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE_INDEXED
Vrml_PER_PART: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART
Vrml_PER_PART_INDEXED: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART_INDEXED
Vrml_PER_VERTEX: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX
Vrml_PER_VERTEX_INDEXED: OCP.Vrml.Vrml_MaterialBindingAndNormalBinding # value = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX_INDEXED
Vrml_POINT: OCP.Vrml.Vrml_WWWAnchorMap # value = Vrml_WWWAnchorMap.Vrml_POINT
Vrml_REPEAT: OCP.Vrml.Vrml_Texture2Wrap # value = Vrml_Texture2Wrap.Vrml_REPEAT
Vrml_RIGHT: OCP.Vrml.Vrml_AsciiTextJustification # value = Vrml_AsciiTextJustification.Vrml_RIGHT
Vrml_SANS: OCP.Vrml.Vrml_FontStyleFamily # value = Vrml_FontStyleFamily.Vrml_SANS
Vrml_SERIF: OCP.Vrml.Vrml_FontStyleFamily # value = Vrml_FontStyleFamily.Vrml_SERIF
Vrml_SOLID: OCP.Vrml.Vrml_ShapeType # value = Vrml_ShapeType.Vrml_SOLID
Vrml_THREE: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_THREE
Vrml_TWO: OCP.Vrml.Vrml_SFImageNumber # value = Vrml_SFImageNumber.Vrml_TWO
Vrml_TYPEWRITER: OCP.Vrml.Vrml_FontStyleFamily # value = Vrml_FontStyleFamily.Vrml_TYPEWRITER
Vrml_UNKNOWN_FACE_TYPE: OCP.Vrml.Vrml_FaceType # value = Vrml_FaceType.Vrml_UNKNOWN_FACE_TYPE
Vrml_UNKNOWN_ORDERING: OCP.Vrml.Vrml_VertexOrdering # value = Vrml_VertexOrdering.Vrml_UNKNOWN_ORDERING
Vrml_UNKNOWN_SHAPE_TYPE: OCP.Vrml.Vrml_ShapeType # value = Vrml_ShapeType.Vrml_UNKNOWN_SHAPE_TYPE
