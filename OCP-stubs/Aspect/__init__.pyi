import OCP.Aspect
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.Quantity
import OCP.Graphic3d
import OCP.Standard
import OCP.NCollection
__all__  = [
"Aspect_AspectFillAreaDefinitionError",
"Aspect_AspectLineDefinitionError",
"Aspect_AspectMarkerDefinitionError",
"Aspect_Background",
"Aspect_Grid",
"Aspect_DisplayConnection",
"Aspect_DisplayConnectionDefinitionError",
"Aspect_FillMethod",
"Aspect_GenId",
"Aspect_GradientBackground",
"Aspect_GradientFillMethod",
"Aspect_GraphicDeviceDefinitionError",
"Aspect_CircularGrid",
"Aspect_GridDrawMode",
"Aspect_GridType",
"Aspect_HatchStyle",
"Aspect_IdentDefinitionError",
"Aspect_InteriorStyle",
"Aspect_Window",
"Aspect_PolygonOffsetMode",
"Aspect_RectangularGrid",
"Aspect_ScrollDelta",
"Aspect_SequenceOfColor",
"Aspect_Touch",
"Aspect_TouchMap",
"Aspect_TypeOfColorScaleData",
"Aspect_TypeOfColorScaleOrientation",
"Aspect_TypeOfColorScalePosition",
"Aspect_TypeOfDeflection",
"Aspect_TypeOfDisplayText",
"Aspect_TypeOfFacingModel",
"Aspect_TypeOfHighlightMethod",
"Aspect_TypeOfLine",
"Aspect_TypeOfMarker",
"Aspect_TypeOfResize",
"Aspect_TypeOfStyleText",
"Aspect_TypeOfTriedronPosition",
"Aspect_VKeyBasic",
"Aspect_WidthOfLine",
"Aspect_NeutralWindow",
"Aspect_WindowDefinitionError",
"Aspect_WindowError",
"Aspect_XAtom",
"Aspect_VKey2Modifier",
"Aspect_FM_CENTERED",
"Aspect_FM_NONE",
"Aspect_FM_STRETCH",
"Aspect_FM_TILED",
"Aspect_GDM_Lines",
"Aspect_GDM_None",
"Aspect_GDM_Points",
"Aspect_GFM_CORNER1",
"Aspect_GFM_CORNER2",
"Aspect_GFM_CORNER3",
"Aspect_GFM_CORNER4",
"Aspect_GFM_DIAG1",
"Aspect_GFM_DIAG2",
"Aspect_GFM_HOR",
"Aspect_GFM_NONE",
"Aspect_GFM_VER",
"Aspect_GT_Circular",
"Aspect_GT_Rectangular",
"Aspect_HS_DIAGONAL_135",
"Aspect_HS_DIAGONAL_135_WIDE",
"Aspect_HS_DIAGONAL_45",
"Aspect_HS_DIAGONAL_45_WIDE",
"Aspect_HS_GRID",
"Aspect_HS_GRID_DIAGONAL",
"Aspect_HS_GRID_DIAGONAL_WIDE",
"Aspect_HS_GRID_WIDE",
"Aspect_HS_HORIZONTAL",
"Aspect_HS_HORIZONTAL_WIDE",
"Aspect_HS_NB",
"Aspect_HS_SOLID",
"Aspect_HS_VERTICAL",
"Aspect_HS_VERTICAL_WIDE",
"Aspect_IS_EMPTY",
"Aspect_IS_HATCH",
"Aspect_IS_HIDDENLINE",
"Aspect_IS_HOLLOW",
"Aspect_IS_POINT",
"Aspect_IS_SOLID",
"Aspect_POM_All",
"Aspect_POM_Fill",
"Aspect_POM_Line",
"Aspect_POM_Mask",
"Aspect_POM_None",
"Aspect_POM_Off",
"Aspect_POM_Point",
"Aspect_TOCSD_AUTO",
"Aspect_TOCSD_USER",
"Aspect_TOCSO_CENTER",
"Aspect_TOCSO_LEFT",
"Aspect_TOCSO_NONE",
"Aspect_TOCSO_RIGHT",
"Aspect_TOCSP_CENTER",
"Aspect_TOCSP_LEFT",
"Aspect_TOCSP_NONE",
"Aspect_TOCSP_RIGHT",
"Aspect_TODT_BLEND",
"Aspect_TODT_DEKALE",
"Aspect_TODT_DIMENSION",
"Aspect_TODT_NORMAL",
"Aspect_TODT_SHADOW",
"Aspect_TODT_SUBTITLE",
"Aspect_TOD_ABSOLUTE",
"Aspect_TOD_RELATIVE",
"Aspect_TOFM_BACK_SIDE",
"Aspect_TOFM_BOTH_SIDE",
"Aspect_TOFM_FRONT_SIDE",
"Aspect_TOHM_BOUNDBOX",
"Aspect_TOHM_COLOR",
"Aspect_TOL_DASH",
"Aspect_TOL_DOT",
"Aspect_TOL_DOTDASH",
"Aspect_TOL_EMPTY",
"Aspect_TOL_SOLID",
"Aspect_TOL_USERDEFINED",
"Aspect_TOM_BALL",
"Aspect_TOM_EMPTY",
"Aspect_TOM_O",
"Aspect_TOM_O_PLUS",
"Aspect_TOM_O_POINT",
"Aspect_TOM_O_STAR",
"Aspect_TOM_O_X",
"Aspect_TOM_PLUS",
"Aspect_TOM_POINT",
"Aspect_TOM_RING1",
"Aspect_TOM_RING2",
"Aspect_TOM_RING3",
"Aspect_TOM_STAR",
"Aspect_TOM_USERDEFINED",
"Aspect_TOM_X",
"Aspect_TOR_BOTTOM_AND_LEFT_BORDER",
"Aspect_TOR_BOTTOM_BORDER",
"Aspect_TOR_LEFT_AND_TOP_BORDER",
"Aspect_TOR_LEFT_BORDER",
"Aspect_TOR_NO_BORDER",
"Aspect_TOR_RIGHT_AND_BOTTOM_BORDER",
"Aspect_TOR_RIGHT_BORDER",
"Aspect_TOR_TOP_AND_RIGHT_BORDER",
"Aspect_TOR_TOP_BORDER",
"Aspect_TOR_UNKNOWN",
"Aspect_TOST_ANNOTATION",
"Aspect_TOST_NORMAL",
"Aspect_TOTP_BOTTOM",
"Aspect_TOTP_CENTER",
"Aspect_TOTP_LEFT",
"Aspect_TOTP_LEFT_LOWER",
"Aspect_TOTP_LEFT_UPPER",
"Aspect_TOTP_RIGHT",
"Aspect_TOTP_RIGHT_LOWER",
"Aspect_TOTP_RIGHT_UPPER",
"Aspect_TOTP_TOP",
"Aspect_VKeyFlags_ALL",
"Aspect_VKeyFlags_ALT",
"Aspect_VKeyFlags_CTRL",
"Aspect_VKeyFlags_MENU",
"Aspect_VKeyFlags_META",
"Aspect_VKeyFlags_NONE",
"Aspect_VKeyFlags_SHIFT",
"Aspect_VKeyMouse_LeftButton",
"Aspect_VKeyMouse_MainButtons",
"Aspect_VKeyMouse_MiddleButton",
"Aspect_VKeyMouse_NONE",
"Aspect_VKeyMouse_RightButton",
"Aspect_VKey_0",
"Aspect_VKey_1",
"Aspect_VKey_2",
"Aspect_VKey_3",
"Aspect_VKey_4",
"Aspect_VKey_5",
"Aspect_VKey_6",
"Aspect_VKey_7",
"Aspect_VKey_8",
"Aspect_VKey_9",
"Aspect_VKey_A",
"Aspect_VKey_Alt",
"Aspect_VKey_Apostrophe",
"Aspect_VKey_B",
"Aspect_VKey_Back",
"Aspect_VKey_Backslash",
"Aspect_VKey_Backspace",
"Aspect_VKey_BracketLeft",
"Aspect_VKey_BracketRight",
"Aspect_VKey_BrowserBack",
"Aspect_VKey_BrowserFavorites",
"Aspect_VKey_BrowserForward",
"Aspect_VKey_BrowserHome",
"Aspect_VKey_BrowserRefresh",
"Aspect_VKey_BrowserSearch",
"Aspect_VKey_BrowserStop",
"Aspect_VKey_C",
"Aspect_VKey_Comma",
"Aspect_VKey_Control",
"Aspect_VKey_D",
"Aspect_VKey_Delete",
"Aspect_VKey_Down",
"Aspect_VKey_E",
"Aspect_VKey_End",
"Aspect_VKey_Enter",
"Aspect_VKey_Equal",
"Aspect_VKey_Escape",
"Aspect_VKey_F",
"Aspect_VKey_F1",
"Aspect_VKey_F10",
"Aspect_VKey_F11",
"Aspect_VKey_F12",
"Aspect_VKey_F2",
"Aspect_VKey_F3",
"Aspect_VKey_F4",
"Aspect_VKey_F5",
"Aspect_VKey_F6",
"Aspect_VKey_F7",
"Aspect_VKey_F8",
"Aspect_VKey_F9",
"Aspect_VKey_G",
"Aspect_VKey_H",
"Aspect_VKey_Home",
"Aspect_VKey_I",
"Aspect_VKey_J",
"Aspect_VKey_K",
"Aspect_VKey_L",
"Aspect_VKey_Left",
"Aspect_VKey_Lower",
"Aspect_VKey_M",
"Aspect_VKey_MAX",
"Aspect_VKey_MediaNextTrack",
"Aspect_VKey_MediaPlayPause",
"Aspect_VKey_MediaPreviousTrack",
"Aspect_VKey_MediaStop",
"Aspect_VKey_Menu",
"Aspect_VKey_Meta",
"Aspect_VKey_Minus",
"Aspect_VKey_ModifiersLower",
"Aspect_VKey_ModifiersUpper",
"Aspect_VKey_N",
"Aspect_VKey_NB",
"Aspect_VKey_NavBackward",
"Aspect_VKey_NavCrouch",
"Aspect_VKey_NavForward",
"Aspect_VKey_NavInteract",
"Aspect_VKey_NavJump",
"Aspect_VKey_NavLookDown",
"Aspect_VKey_NavLookLeft",
"Aspect_VKey_NavLookRight",
"Aspect_VKey_NavLookUp",
"Aspect_VKey_NavRollCCW",
"Aspect_VKey_NavRollCW",
"Aspect_VKey_NavSlideDown",
"Aspect_VKey_NavSlideLeft",
"Aspect_VKey_NavSlideRight",
"Aspect_VKey_NavSlideUp",
"Aspect_VKey_NavSpeedDecrease",
"Aspect_VKey_NavSpeedIncrease",
"Aspect_VKey_NavThrustBackward",
"Aspect_VKey_NavThrustForward",
"Aspect_VKey_NavThrustStop",
"Aspect_VKey_NavigationKeysLower",
"Aspect_VKey_NavigationKeysUpper",
"Aspect_VKey_Numlock",
"Aspect_VKey_Numpad0",
"Aspect_VKey_Numpad1",
"Aspect_VKey_Numpad2",
"Aspect_VKey_Numpad3",
"Aspect_VKey_Numpad4",
"Aspect_VKey_Numpad5",
"Aspect_VKey_Numpad6",
"Aspect_VKey_Numpad7",
"Aspect_VKey_Numpad8",
"Aspect_VKey_Numpad9",
"Aspect_VKey_NumpadAdd",
"Aspect_VKey_NumpadDivide",
"Aspect_VKey_NumpadMultiply",
"Aspect_VKey_NumpadSubtract",
"Aspect_VKey_O",
"Aspect_VKey_P",
"Aspect_VKey_PageDown",
"Aspect_VKey_PageUp",
"Aspect_VKey_Period",
"Aspect_VKey_Plus",
"Aspect_VKey_Q",
"Aspect_VKey_R",
"Aspect_VKey_Right",
"Aspect_VKey_S",
"Aspect_VKey_Scroll",
"Aspect_VKey_Semicolon",
"Aspect_VKey_Shift",
"Aspect_VKey_Slash",
"Aspect_VKey_Space",
"Aspect_VKey_T",
"Aspect_VKey_Tab",
"Aspect_VKey_Tilde",
"Aspect_VKey_U",
"Aspect_VKey_UNKNOWN",
"Aspect_VKey_Up",
"Aspect_VKey_Upper",
"Aspect_VKey_V",
"Aspect_VKey_VolumeDown",
"Aspect_VKey_VolumeMute",
"Aspect_VKey_VolumeUp",
"Aspect_VKey_W",
"Aspect_VKey_X",
"Aspect_VKey_Y",
"Aspect_VKey_Z",
"Aspect_WOL_MEDIUM",
"Aspect_WOL_THICK",
"Aspect_WOL_THIN",
"Aspect_WOL_USERDEFINED",
"Aspect_WOL_VERYTHICK",
"Aspect_XA_DELETE_WINDOW"
]
class Aspect_AspectFillAreaDefinitionError(Exception, BaseException):
    class type():
        """
        type(object_or_name, bases, dict)
        type(object) -> the object's type
        type(name, bases, dict) -> a new type
        """
        class object():
            """
            The base class of the class hierarchy.

            When called, it accepts no arguments and returns a new featureless
            instance that has no instance attributes and cannot be given any.
            """
            class type():
                pass
            pass
        class type():
            pass
        @staticmethod
        def __prepare__() -> dict: ...
        __abstractmethods__: getset_descriptor # value = <attribute '__abstractmethods__' of 'type' objects>
        __bases__: tuple # value = (<class 'object'>,)
        __basicsize__ = 880
        __dict__: mappingproxy # value = mappingproxy({'__repr__': <slot wrapper '__repr__' of 'type' objects>, '__call__': <slot wrapper '__call__' of 'type' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'type' objects>, '__setattr__': <slot wrapper '__setattr__' of 'type' objects>, '__delattr__': <slot wrapper '__delattr__' of 'type' objects>, '__init__': <slot wrapper '__init__' of 'type' objects>, '__new__': <built-in method __new__ of type object at 0x55f8b277bac0>, 'mro': <method 'mro' of 'type' objects>, '__subclasses__': <method '__subclasses__' of 'type' objects>, '__prepare__': <method '__prepare__' of 'type' objects>, '__instancecheck__': <method '__instancecheck__' of 'type' objects>, '__subclasscheck__': <method '__subclasscheck__' of 'type' objects>, '__dir__': <method '__dir__' of 'type' objects>, '__sizeof__': <method '__sizeof__' of 'type' objects>, '__basicsize__': <member '__basicsize__' of 'type' objects>, '__itemsize__': <member '__itemsize__' of 'type' objects>, '__flags__': <member '__flags__' of 'type' objects>, '__weakrefoffset__': <member '__weakrefoffset__' of 'type' objects>, '__base__': <member '__base__' of 'type' objects>, '__dictoffset__': <member '__dictoffset__' of 'type' objects>, '__mro__': <member '__mro__' of 'type' objects>, '__name__': <attribute '__name__' of 'type' objects>, '__qualname__': <attribute '__qualname__' of 'type' objects>, '__bases__': <attribute '__bases__' of 'type' objects>, '__module__': <attribute '__module__' of 'type' objects>, '__abstractmethods__': <attribute '__abstractmethods__' of 'type' objects>, '__dict__': <attribute '__dict__' of 'type' objects>, '__doc__': <attribute '__doc__' of 'type' objects>, '__text_signature__': <attribute '__text_signature__' of 'type' objects>})
        __dictoffset__ = 264
        __flags__ = 2148291584
        __itemsize__ = 40
        __mro__: tuple # value = (<class 'type'>, <class 'object'>)
        __name__ = 'type'
        __text_signature__: NoneType # value = None
        __weakrefoffset__ = 368
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Aspect', '__weakref__': <attribute '__weakref__' of 'Aspect_AspectFillAreaDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Aspect_AspectFillAreaDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Aspect_AspectLineDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Aspect', '__weakref__': <attribute '__weakref__' of 'Aspect_AspectLineDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Aspect_AspectLineDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Aspect_AspectMarkerDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Aspect', '__weakref__': <attribute '__weakref__' of 'Aspect_AspectMarkerDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Aspect_AspectMarkerDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Aspect_Background():
    """
    This class allows the definition of a window background.
    """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the colour of the window background <me>.
        """
    def SetColor(self,AColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the colour of the window background <me>.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,AColor : OCP.Quantity.Quantity_Color) -> None: ...
    pass
class Aspect_Grid(OCP.Standard.Standard_Transient):
    def Activate(self) -> None: 
        """
        activates the grid. The Hit method will return gridx and gridx computed according to the steps of the grid.
        """
    def Colors(self,aColor : OCP.Quantity.Quantity_Color,aTenthColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns the colors of the grid.
        """
    def Compute(self,X : float,Y : float) -> Tuple[float, float]: 
        """
        returns the point of the grid the closest to the point X,Y
        """
    def Deactivate(self) -> None: 
        """
        deactivates the grid. The hit method will return gridx and gridx as the enter value X & Y.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Display(self) -> None: 
        """
        Display the grid at screen.
        """
    def DrawMode(self) -> Aspect_GridDrawMode: 
        """
        Returns the grid aspect.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Erase(self) -> None: 
        """
        Erase the grid from screen.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hit(self,X : float,Y : float) -> Tuple[float, float]: 
        """
        returns the point of the grid the closest to the point X,Y if the grid is active. If the grid is not active returns X,Y.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        None
        """
    def IsActive(self) -> bool: 
        """
        Returns TRUE when the grid is active.
        """
    def IsDisplayed(self) -> bool: 
        """
        Returns TRUE when the grid is displayed at screen.
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
    def Rotate(self,anAngle : float) -> None: 
        """
        Rotate the grid from a relative angle.
        """
    def RotationAngle(self) -> float: 
        """
        returns the x Angle of the grid.
        """
    def SetColors(self,aColor : OCP.Quantity.Quantity_Color,aTenthColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the colors of the grid
        """
    def SetDrawMode(self,aDrawMode : Aspect_GridDrawMode) -> None: 
        """
        Change the grid aspect.
        """
    def SetRotationAngle(self,anAngle : float) -> None: 
        """
        defines the orientation of the grid.
        """
    def SetXOrigin(self,anOrigin : float) -> None: 
        """
        defines the x Origin of the grid.
        """
    def SetYOrigin(self,anOrigin : float) -> None: 
        """
        defines the y Origin of the grid.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Translate(self,aDx : float,aDy : float) -> None: 
        """
        Translate the grid from a relative distance.
        """
    def XOrigin(self) -> float: 
        """
        returns the x Origin of the grid.
        """
    def YOrigin(self) -> float: 
        """
        returns the x Origin of the grid.
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
class Aspect_DisplayConnection(OCP.Standard.Standard_Transient):
    """
    This class creates and provides connection with X server. Raises exception if can not connect to X server. On Windows and Mac OS X (in case when Cocoa used) platforms this class do nothing. WARRNING: Do not close display connection manualy!This class creates and provides connection with X server. Raises exception if can not connect to X server. On Windows and Mac OS X (in case when Cocoa used) platforms this class do nothing. WARRNING: Do not close display connection manualy!
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
    def GetAtom(self,theAtom : Aspect_XAtom) -> int: 
        """
        Returns identifier(atom) for custom named property associated with windows that use current connection to X server.
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
    def IsOwnDisplay(self) -> bool: 
        """
        Returns TRUE if X Display has been allocated by this class
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theDisplayName : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Aspect_DisplayConnectionDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Aspect', '__weakref__': <attribute '__weakref__' of 'Aspect_DisplayConnectionDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Aspect_DisplayConnectionDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Aspect_FillMethod():
    """
    Defines the fill methods to write bitmaps in a window.

    Members:

      Aspect_FM_NONE

      Aspect_FM_CENTERED

      Aspect_FM_TILED

      Aspect_FM_STRETCH
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
    Aspect_FM_CENTERED: OCP.Aspect.Aspect_FillMethod # value = Aspect_FillMethod.Aspect_FM_CENTERED
    Aspect_FM_NONE: OCP.Aspect.Aspect_FillMethod # value = Aspect_FillMethod.Aspect_FM_NONE
    Aspect_FM_STRETCH: OCP.Aspect.Aspect_FillMethod # value = Aspect_FillMethod.Aspect_FM_STRETCH
    Aspect_FM_TILED: OCP.Aspect.Aspect_FillMethod # value = Aspect_FillMethod.Aspect_FM_TILED
    __entries: dict # value = {'Aspect_FM_NONE': (Aspect_FillMethod.Aspect_FM_NONE, None), 'Aspect_FM_CENTERED': (Aspect_FillMethod.Aspect_FM_CENTERED, None), 'Aspect_FM_TILED': (Aspect_FillMethod.Aspect_FM_TILED, None), 'Aspect_FM_STRETCH': (Aspect_FillMethod.Aspect_FM_STRETCH, None)}
    __members__: dict # value = {'Aspect_FM_NONE': Aspect_FillMethod.Aspect_FM_NONE, 'Aspect_FM_CENTERED': Aspect_FillMethod.Aspect_FM_CENTERED, 'Aspect_FM_TILED': Aspect_FillMethod.Aspect_FM_TILED, 'Aspect_FM_STRETCH': Aspect_FillMethod.Aspect_FM_STRETCH}
    pass
class Aspect_GenId():
    """
    This class permits the creation and control of integer identifiers.
    """
    def Available(self) -> int: 
        """
        Returns the number of available identifiers.
        """
    @overload
    def Free(self,theId : int) -> None: 
        """
        Free all identifiers - make the whole range available again.

        Free specified identifier. Warning - method has no protection against double-freeing!
        """
    @overload
    def Free(self) -> None: ...
    def HasFree(self) -> bool: 
        """
        Returns true if there are available identifiers in range.
        """
    def Lower(self) -> int: 
        """
        Returns the lower identifier in range.
        """
    @overload
    def Next(self) -> int: 
        """
        Returns the next available identifier. Warning: Raises IdentDefinitionError if all identifiers are busy.

        Generates the next available identifier.
        """
    @overload
    def Next(self,theId : int) -> bool: ...
    def Upper(self) -> int: 
        """
        Returns the upper identifier in range.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLow : int,theUpper : int) -> None: ...
    pass
class Aspect_GradientBackground(Aspect_Background):
    """
    This class allows the definition of a window gradient background.
    """
    def BgGradientFillMethod(self) -> Aspect_GradientFillMethod: 
        """
        Returns the current gradient background fill mode.
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the colour of the window background <me>.
        """
    def Colors(self,AColor1 : OCP.Quantity.Quantity_Color,AColor2 : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns colours of the window gradient background <me>.
        """
    def SetColor(self,AColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the colour of the window background <me>.
        """
    def SetColors(self,AColor1 : OCP.Quantity.Quantity_Color,AColor2 : OCP.Quantity.Quantity_Color,AMethod : Aspect_GradientFillMethod=Aspect_GradientFillMethod.Aspect_GFM_HOR) -> None: 
        """
        Modifies the colours of the window gradient background <me>.
        """
    @overload
    def __init__(self,AColor1 : OCP.Quantity.Quantity_Color,AColor2 : OCP.Quantity.Quantity_Color,AMethod : Aspect_GradientFillMethod=Aspect_GradientFillMethod.Aspect_GFM_HOR) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Aspect_GradientFillMethod():
    """
    Defines the fill methods to write gradient background in a window.

    Members:

      Aspect_GFM_NONE

      Aspect_GFM_HOR

      Aspect_GFM_VER

      Aspect_GFM_DIAG1

      Aspect_GFM_DIAG2

      Aspect_GFM_CORNER1

      Aspect_GFM_CORNER2

      Aspect_GFM_CORNER3

      Aspect_GFM_CORNER4
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
    Aspect_GFM_CORNER1: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_CORNER1
    Aspect_GFM_CORNER2: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_CORNER2
    Aspect_GFM_CORNER3: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_CORNER3
    Aspect_GFM_CORNER4: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_CORNER4
    Aspect_GFM_DIAG1: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_DIAG1
    Aspect_GFM_DIAG2: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_DIAG2
    Aspect_GFM_HOR: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_HOR
    Aspect_GFM_NONE: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_NONE
    Aspect_GFM_VER: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_VER
    __entries: dict # value = {'Aspect_GFM_NONE': (Aspect_GradientFillMethod.Aspect_GFM_NONE, None), 'Aspect_GFM_HOR': (Aspect_GradientFillMethod.Aspect_GFM_HOR, None), 'Aspect_GFM_VER': (Aspect_GradientFillMethod.Aspect_GFM_VER, None), 'Aspect_GFM_DIAG1': (Aspect_GradientFillMethod.Aspect_GFM_DIAG1, None), 'Aspect_GFM_DIAG2': (Aspect_GradientFillMethod.Aspect_GFM_DIAG2, None), 'Aspect_GFM_CORNER1': (Aspect_GradientFillMethod.Aspect_GFM_CORNER1, None), 'Aspect_GFM_CORNER2': (Aspect_GradientFillMethod.Aspect_GFM_CORNER2, None), 'Aspect_GFM_CORNER3': (Aspect_GradientFillMethod.Aspect_GFM_CORNER3, None), 'Aspect_GFM_CORNER4': (Aspect_GradientFillMethod.Aspect_GFM_CORNER4, None)}
    __members__: dict # value = {'Aspect_GFM_NONE': Aspect_GradientFillMethod.Aspect_GFM_NONE, 'Aspect_GFM_HOR': Aspect_GradientFillMethod.Aspect_GFM_HOR, 'Aspect_GFM_VER': Aspect_GradientFillMethod.Aspect_GFM_VER, 'Aspect_GFM_DIAG1': Aspect_GradientFillMethod.Aspect_GFM_DIAG1, 'Aspect_GFM_DIAG2': Aspect_GradientFillMethod.Aspect_GFM_DIAG2, 'Aspect_GFM_CORNER1': Aspect_GradientFillMethod.Aspect_GFM_CORNER1, 'Aspect_GFM_CORNER2': Aspect_GradientFillMethod.Aspect_GFM_CORNER2, 'Aspect_GFM_CORNER3': Aspect_GradientFillMethod.Aspect_GFM_CORNER3, 'Aspect_GFM_CORNER4': Aspect_GradientFillMethod.Aspect_GFM_CORNER4}
    pass
class Aspect_GraphicDeviceDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Aspect', '__weakref__': <attribute '__weakref__' of 'Aspect_GraphicDeviceDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Aspect_GraphicDeviceDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Aspect_CircularGrid(Aspect_Grid, OCP.Standard.Standard_Transient):
    def Activate(self) -> None: 
        """
        activates the grid. The Hit method will return gridx and gridx computed according to the steps of the grid.
        """
    def Colors(self,aColor : OCP.Quantity.Quantity_Color,aTenthColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns the colors of the grid.
        """
    def Compute(self,X : float,Y : float) -> Tuple[float, float]: 
        """
        returns the point of the grid the closest to the point X,Y
        """
    def Deactivate(self) -> None: 
        """
        deactivates the grid. The hit method will return gridx and gridx as the enter value X & Y.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Display(self) -> None: 
        """
        Display the grid at screen.
        """
    def DivisionNumber(self) -> int: 
        """
        returns the x step of the grid.
        """
    def DrawMode(self) -> Aspect_GridDrawMode: 
        """
        Returns the grid aspect.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Erase(self) -> None: 
        """
        Erase the grid from screen.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hit(self,X : float,Y : float) -> Tuple[float, float]: 
        """
        returns the point of the grid the closest to the point X,Y if the grid is active. If the grid is not active returns X,Y.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        None
        """
    def IsActive(self) -> bool: 
        """
        Returns TRUE when the grid is active.
        """
    def IsDisplayed(self) -> bool: 
        """
        Returns TRUE when the grid is displayed at screen.
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
    def RadiusStep(self) -> float: 
        """
        returns the x step of the grid.
        """
    def Rotate(self,anAngle : float) -> None: 
        """
        Rotate the grid from a relative angle.
        """
    def RotationAngle(self) -> float: 
        """
        returns the x Angle of the grid.
        """
    def SetColors(self,aColor : OCP.Quantity.Quantity_Color,aTenthColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the colors of the grid
        """
    def SetDivisionNumber(self,aNumber : int) -> None: 
        """
        defines the step of the grid.
        """
    def SetDrawMode(self,aDrawMode : Aspect_GridDrawMode) -> None: 
        """
        Change the grid aspect.
        """
    def SetGridValues(self,XOrigin : float,YOrigin : float,RadiusStep : float,DivisionNumber : int,RotationAngle : float) -> None: 
        """
        None
        """
    def SetRadiusStep(self,aStep : float) -> None: 
        """
        defines the x step of the grid.
        """
    def SetRotationAngle(self,anAngle : float) -> None: 
        """
        defines the orientation of the grid.
        """
    def SetXOrigin(self,anOrigin : float) -> None: 
        """
        defines the x Origin of the grid.
        """
    def SetYOrigin(self,anOrigin : float) -> None: 
        """
        defines the y Origin of the grid.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Translate(self,aDx : float,aDy : float) -> None: 
        """
        Translate the grid from a relative distance.
        """
    def XOrigin(self) -> float: 
        """
        returns the x Origin of the grid.
        """
    def YOrigin(self) -> float: 
        """
        returns the x Origin of the grid.
        """
    def __init__(self,aRadiusStep : float,aDivisionNumber : int,XOrigin : float=0.0,anYOrigin : float=0.0,aRotationAngle : float=0.0) -> None: ...
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
class Aspect_GridDrawMode():
    """
    Defines the grid draw mode. The grid may be drawn by using lines or points.

    Members:

      Aspect_GDM_Lines

      Aspect_GDM_Points

      Aspect_GDM_None
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
    Aspect_GDM_Lines: OCP.Aspect.Aspect_GridDrawMode # value = Aspect_GridDrawMode.Aspect_GDM_Lines
    Aspect_GDM_None: OCP.Aspect.Aspect_GridDrawMode # value = Aspect_GridDrawMode.Aspect_GDM_None
    Aspect_GDM_Points: OCP.Aspect.Aspect_GridDrawMode # value = Aspect_GridDrawMode.Aspect_GDM_Points
    __entries: dict # value = {'Aspect_GDM_Lines': (Aspect_GridDrawMode.Aspect_GDM_Lines, None), 'Aspect_GDM_Points': (Aspect_GridDrawMode.Aspect_GDM_Points, None), 'Aspect_GDM_None': (Aspect_GridDrawMode.Aspect_GDM_None, None)}
    __members__: dict # value = {'Aspect_GDM_Lines': Aspect_GridDrawMode.Aspect_GDM_Lines, 'Aspect_GDM_Points': Aspect_GridDrawMode.Aspect_GDM_Points, 'Aspect_GDM_None': Aspect_GridDrawMode.Aspect_GDM_None}
    pass
class Aspect_GridType():
    """
    Defines the grid type : Rectangular or Circular.

    Members:

      Aspect_GT_Rectangular

      Aspect_GT_Circular
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
    Aspect_GT_Circular: OCP.Aspect.Aspect_GridType # value = Aspect_GridType.Aspect_GT_Circular
    Aspect_GT_Rectangular: OCP.Aspect.Aspect_GridType # value = Aspect_GridType.Aspect_GT_Rectangular
    __entries: dict # value = {'Aspect_GT_Rectangular': (Aspect_GridType.Aspect_GT_Rectangular, None), 'Aspect_GT_Circular': (Aspect_GridType.Aspect_GT_Circular, None)}
    __members__: dict # value = {'Aspect_GT_Rectangular': Aspect_GridType.Aspect_GT_Rectangular, 'Aspect_GT_Circular': Aspect_GridType.Aspect_GT_Circular}
    pass
class Aspect_HatchStyle():
    """
    Definition of all available hatch styles.

    Members:

      Aspect_HS_SOLID

      Aspect_HS_HORIZONTAL

      Aspect_HS_HORIZONTAL_WIDE

      Aspect_HS_VERTICAL

      Aspect_HS_VERTICAL_WIDE

      Aspect_HS_DIAGONAL_45

      Aspect_HS_DIAGONAL_45_WIDE

      Aspect_HS_DIAGONAL_135

      Aspect_HS_DIAGONAL_135_WIDE

      Aspect_HS_GRID

      Aspect_HS_GRID_WIDE

      Aspect_HS_GRID_DIAGONAL

      Aspect_HS_GRID_DIAGONAL_WIDE

      Aspect_HS_NB
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
    Aspect_HS_DIAGONAL_135: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_DIAGONAL_135
    Aspect_HS_DIAGONAL_135_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_DIAGONAL_135_WIDE
    Aspect_HS_DIAGONAL_45: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_DIAGONAL_45
    Aspect_HS_DIAGONAL_45_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_DIAGONAL_45_WIDE
    Aspect_HS_GRID: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_GRID
    Aspect_HS_GRID_DIAGONAL: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL
    Aspect_HS_GRID_DIAGONAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL_WIDE
    Aspect_HS_GRID_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_GRID_WIDE
    Aspect_HS_HORIZONTAL: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_HORIZONTAL
    Aspect_HS_HORIZONTAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_HORIZONTAL_WIDE
    Aspect_HS_NB: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_NB
    Aspect_HS_SOLID: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_SOLID
    Aspect_HS_VERTICAL: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_VERTICAL
    Aspect_HS_VERTICAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_VERTICAL_WIDE
    __entries: dict # value = {'Aspect_HS_SOLID': (Aspect_HatchStyle.Aspect_HS_SOLID, None), 'Aspect_HS_HORIZONTAL': (Aspect_HatchStyle.Aspect_HS_HORIZONTAL, None), 'Aspect_HS_HORIZONTAL_WIDE': (Aspect_HatchStyle.Aspect_HS_HORIZONTAL_WIDE, None), 'Aspect_HS_VERTICAL': (Aspect_HatchStyle.Aspect_HS_VERTICAL, None), 'Aspect_HS_VERTICAL_WIDE': (Aspect_HatchStyle.Aspect_HS_VERTICAL_WIDE, None), 'Aspect_HS_DIAGONAL_45': (Aspect_HatchStyle.Aspect_HS_DIAGONAL_45, None), 'Aspect_HS_DIAGONAL_45_WIDE': (Aspect_HatchStyle.Aspect_HS_DIAGONAL_45_WIDE, None), 'Aspect_HS_DIAGONAL_135': (Aspect_HatchStyle.Aspect_HS_DIAGONAL_135, None), 'Aspect_HS_DIAGONAL_135_WIDE': (Aspect_HatchStyle.Aspect_HS_DIAGONAL_135_WIDE, None), 'Aspect_HS_GRID': (Aspect_HatchStyle.Aspect_HS_GRID, None), 'Aspect_HS_GRID_WIDE': (Aspect_HatchStyle.Aspect_HS_GRID_WIDE, None), 'Aspect_HS_GRID_DIAGONAL': (Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL, None), 'Aspect_HS_GRID_DIAGONAL_WIDE': (Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL_WIDE, None), 'Aspect_HS_NB': (Aspect_HatchStyle.Aspect_HS_NB, None)}
    __members__: dict # value = {'Aspect_HS_SOLID': Aspect_HatchStyle.Aspect_HS_SOLID, 'Aspect_HS_HORIZONTAL': Aspect_HatchStyle.Aspect_HS_HORIZONTAL, 'Aspect_HS_HORIZONTAL_WIDE': Aspect_HatchStyle.Aspect_HS_HORIZONTAL_WIDE, 'Aspect_HS_VERTICAL': Aspect_HatchStyle.Aspect_HS_VERTICAL, 'Aspect_HS_VERTICAL_WIDE': Aspect_HatchStyle.Aspect_HS_VERTICAL_WIDE, 'Aspect_HS_DIAGONAL_45': Aspect_HatchStyle.Aspect_HS_DIAGONAL_45, 'Aspect_HS_DIAGONAL_45_WIDE': Aspect_HatchStyle.Aspect_HS_DIAGONAL_45_WIDE, 'Aspect_HS_DIAGONAL_135': Aspect_HatchStyle.Aspect_HS_DIAGONAL_135, 'Aspect_HS_DIAGONAL_135_WIDE': Aspect_HatchStyle.Aspect_HS_DIAGONAL_135_WIDE, 'Aspect_HS_GRID': Aspect_HatchStyle.Aspect_HS_GRID, 'Aspect_HS_GRID_WIDE': Aspect_HatchStyle.Aspect_HS_GRID_WIDE, 'Aspect_HS_GRID_DIAGONAL': Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL, 'Aspect_HS_GRID_DIAGONAL_WIDE': Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL_WIDE, 'Aspect_HS_NB': Aspect_HatchStyle.Aspect_HS_NB}
    pass
class Aspect_IdentDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Aspect', '__weakref__': <attribute '__weakref__' of 'Aspect_IdentDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Aspect_IdentDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Aspect_InteriorStyle():
    """
    Interior types for primitive faces.

    Members:

      Aspect_IS_EMPTY

      Aspect_IS_SOLID

      Aspect_IS_HATCH

      Aspect_IS_HIDDENLINE

      Aspect_IS_POINT

      Aspect_IS_HOLLOW
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
    Aspect_IS_EMPTY: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_EMPTY
    Aspect_IS_HATCH: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_HATCH
    Aspect_IS_HIDDENLINE: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_HIDDENLINE
    Aspect_IS_HOLLOW: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_EMPTY
    Aspect_IS_POINT: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_POINT
    Aspect_IS_SOLID: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_SOLID
    __entries: dict # value = {'Aspect_IS_EMPTY': (Aspect_InteriorStyle.Aspect_IS_EMPTY, None), 'Aspect_IS_SOLID': (Aspect_InteriorStyle.Aspect_IS_SOLID, None), 'Aspect_IS_HATCH': (Aspect_InteriorStyle.Aspect_IS_HATCH, None), 'Aspect_IS_HIDDENLINE': (Aspect_InteriorStyle.Aspect_IS_HIDDENLINE, None), 'Aspect_IS_POINT': (Aspect_InteriorStyle.Aspect_IS_POINT, None), 'Aspect_IS_HOLLOW': (Aspect_InteriorStyle.Aspect_IS_EMPTY, None)}
    __members__: dict # value = {'Aspect_IS_EMPTY': Aspect_InteriorStyle.Aspect_IS_EMPTY, 'Aspect_IS_SOLID': Aspect_InteriorStyle.Aspect_IS_SOLID, 'Aspect_IS_HATCH': Aspect_InteriorStyle.Aspect_IS_HATCH, 'Aspect_IS_HIDDENLINE': Aspect_InteriorStyle.Aspect_IS_HIDDENLINE, 'Aspect_IS_POINT': Aspect_InteriorStyle.Aspect_IS_POINT, 'Aspect_IS_HOLLOW': Aspect_InteriorStyle.Aspect_IS_EMPTY}
    pass
class Aspect_Window(OCP.Standard.Standard_Transient):
    """
    Defines a window.Defines a window.
    """
    def Background(self) -> Aspect_Background: 
        """
        Returns the window background.
        """
    def BackgroundFillMethod(self) -> Aspect_FillMethod: 
        """
        Returns the current image background fill mode.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DoMapping(self) -> bool: 
        """
        Apply the mapping change to the window <me>. and returns TRUE if the window is mapped at screen.
        """
    def DoResize(self) -> Aspect_TypeOfResize: 
        """
        Apply the resizing to the window <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GradientBackground(self) -> Aspect_GradientBackground: 
        """
        Returns the window gradient background.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvalidateContent(self,theDisp : Aspect_DisplayConnection) -> None: 
        """
        Invalidate entire window content.
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
    def IsMapped(self) -> bool: 
        """
        Returns True if the window <me> is opened and False if the window is closed.
        """
    def IsVirtual(self) -> bool: 
        """
        Returns True if the window <me> is virtual
        """
    def Map(self) -> None: 
        """
        Opens the window <me>.
        """
    def NativeHandle(self) -> int: 
        """
        Returns native Window handle (HWND on Windows, Window with Xlib, and so on)
        """
    def NativeParentHandle(self) -> int: 
        """
        Returns parent of native Window handle (HWND on Windows, Window with Xlib, and so on)
        """
    def Position(self) -> Tuple[int, int, int, int]: 
        """
        Returns The Window POSITION in PIXEL
        """
    def Ratio(self) -> float: 
        """
        Returns The Window RATIO equal to the physical WIDTH/HEIGHT dimensions
        """
    @overload
    def SetBackground(self,color : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the window background.

        Modifies the window background.

        Modifies the window gradient background.

        Modifies the window gradient background.
        """
    @overload
    def SetBackground(self,theFirstColor : OCP.Quantity.Quantity_Color,theSecondColor : OCP.Quantity.Quantity_Color,theFillMethod : Aspect_GradientFillMethod) -> None: ...
    @overload
    def SetBackground(self,ABack : Aspect_Background) -> None: ...
    @overload
    def SetBackground(self,ABackground : Aspect_GradientBackground) -> None: ...
    def SetTitle(self,theTitle : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets window title.
        """
    def SetVirtual(self,theVirtual : bool) -> None: 
        """
        Setup the virtual state
        """
    def Size(self) -> Tuple[int, int]: 
        """
        Returns The Window SIZE in PIXEL
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unmap(self) -> None: 
        """
        Closes the window <me>.
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
class Aspect_PolygonOffsetMode():
    """
    None

    Members:

      Aspect_POM_Off

      Aspect_POM_Fill

      Aspect_POM_Line

      Aspect_POM_Point

      Aspect_POM_All

      Aspect_POM_None

      Aspect_POM_Mask
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
    Aspect_POM_All: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_All
    Aspect_POM_Fill: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Fill
    Aspect_POM_Line: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Line
    Aspect_POM_Mask: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Mask
    Aspect_POM_None: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_None
    Aspect_POM_Off: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Off
    Aspect_POM_Point: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Point
    __entries: dict # value = {'Aspect_POM_Off': (Aspect_PolygonOffsetMode.Aspect_POM_Off, None), 'Aspect_POM_Fill': (Aspect_PolygonOffsetMode.Aspect_POM_Fill, None), 'Aspect_POM_Line': (Aspect_PolygonOffsetMode.Aspect_POM_Line, None), 'Aspect_POM_Point': (Aspect_PolygonOffsetMode.Aspect_POM_Point, None), 'Aspect_POM_All': (Aspect_PolygonOffsetMode.Aspect_POM_All, None), 'Aspect_POM_None': (Aspect_PolygonOffsetMode.Aspect_POM_None, None), 'Aspect_POM_Mask': (Aspect_PolygonOffsetMode.Aspect_POM_Mask, None)}
    __members__: dict # value = {'Aspect_POM_Off': Aspect_PolygonOffsetMode.Aspect_POM_Off, 'Aspect_POM_Fill': Aspect_PolygonOffsetMode.Aspect_POM_Fill, 'Aspect_POM_Line': Aspect_PolygonOffsetMode.Aspect_POM_Line, 'Aspect_POM_Point': Aspect_PolygonOffsetMode.Aspect_POM_Point, 'Aspect_POM_All': Aspect_PolygonOffsetMode.Aspect_POM_All, 'Aspect_POM_None': Aspect_PolygonOffsetMode.Aspect_POM_None, 'Aspect_POM_Mask': Aspect_PolygonOffsetMode.Aspect_POM_Mask}
    pass
class Aspect_RectangularGrid(Aspect_Grid, OCP.Standard.Standard_Transient):
    def Activate(self) -> None: 
        """
        activates the grid. The Hit method will return gridx and gridx computed according to the steps of the grid.
        """
    def Colors(self,aColor : OCP.Quantity.Quantity_Color,aTenthColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns the colors of the grid.
        """
    def Compute(self,X : float,Y : float) -> Tuple[float, float]: 
        """
        returns the point of the grid the closest to the point X,Y
        """
    def Deactivate(self) -> None: 
        """
        deactivates the grid. The hit method will return gridx and gridx as the enter value X & Y.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Display(self) -> None: 
        """
        Display the grid at screen.
        """
    def DrawMode(self) -> Aspect_GridDrawMode: 
        """
        Returns the grid aspect.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Erase(self) -> None: 
        """
        Erase the grid from screen.
        """
    def FirstAngle(self) -> float: 
        """
        returns the x Angle of the grid, relatively to the horizontal.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hit(self,X : float,Y : float) -> Tuple[float, float]: 
        """
        returns the point of the grid the closest to the point X,Y if the grid is active. If the grid is not active returns X,Y.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        None
        """
    def IsActive(self) -> bool: 
        """
        Returns TRUE when the grid is active.
        """
    def IsDisplayed(self) -> bool: 
        """
        Returns TRUE when the grid is displayed at screen.
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
    def Rotate(self,anAngle : float) -> None: 
        """
        Rotate the grid from a relative angle.
        """
    def RotationAngle(self) -> float: 
        """
        returns the x Angle of the grid.
        """
    def SecondAngle(self) -> float: 
        """
        returns the y Angle of the grid, relatively to the vertical.
        """
    def SetAngle(self,anAngle1 : float,anAngle2 : float) -> None: 
        """
        defines the angle of the second network the fist angle is given relatively to the horizontal. the second angle is given relatively to the vertical.
        """
    def SetColors(self,aColor : OCP.Quantity.Quantity_Color,aTenthColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the colors of the grid
        """
    def SetDrawMode(self,aDrawMode : Aspect_GridDrawMode) -> None: 
        """
        Change the grid aspect.
        """
    def SetGridValues(self,XOrigin : float,YOrigin : float,XStep : float,YStep : float,RotationAngle : float) -> None: 
        """
        None
        """
    def SetRotationAngle(self,anAngle : float) -> None: 
        """
        defines the orientation of the grid.
        """
    def SetXOrigin(self,anOrigin : float) -> None: 
        """
        defines the x Origin of the grid.
        """
    def SetXStep(self,aStep : float) -> None: 
        """
        defines the x step of the grid.
        """
    def SetYOrigin(self,anOrigin : float) -> None: 
        """
        defines the y Origin of the grid.
        """
    def SetYStep(self,aStep : float) -> None: 
        """
        defines the y step of the grid.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Translate(self,aDx : float,aDy : float) -> None: 
        """
        Translate the grid from a relative distance.
        """
    def XOrigin(self) -> float: 
        """
        returns the x Origin of the grid.
        """
    def XStep(self) -> float: 
        """
        returns the x step of the grid.
        """
    def YOrigin(self) -> float: 
        """
        returns the x Origin of the grid.
        """
    def YStep(self) -> float: 
        """
        returns the x step of the grid.
        """
    def __init__(self,aXStep : float,aYStep : float,anXOrigin : float=0.0,anYOrigin : float=0.0,aFirstAngle : float=0.0,aSecondAngle : float=0.0,aRotationAngle : float=0.0) -> None: ...
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
class Aspect_ScrollDelta():
    """
    Parameters for mouse scroll action.
    """
    def HasPoint(self) -> bool: 
        """
        Return true if action has point defined.
        """
    def ResetPoint(self) -> None: 
        """
        Reset at point.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,thePnt : OCP.Graphic3d.Graphic3d_Vec2i,theValue : float,theFlags : int=0) -> None: ...
    @overload
    def __init__(self,theValue : float,theFlags : int=0) -> None: ...
    @property
    def Delta(self) -> float:
        """
        :type: float
        """
    @Delta.setter
    def Delta(self, arg0: float) -> None:
        pass
    @property
    def Flags(self) -> int:
        """
        :type: int
        """
    @Flags.setter
    def Flags(self, arg0: int) -> None:
        pass
    pass
class Aspect_SequenceOfColor(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.Quantity.Quantity_Color) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Aspect_SequenceOfColor) -> None: ...
    def Assign(self,theOther : Aspect_SequenceOfColor) -> Aspect_SequenceOfColor: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Quantity.Quantity_Color: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Quantity.Quantity_Color: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.Quantity.Quantity_Color: 
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
    def First(self) -> OCP.Quantity.Quantity_Color: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Quantity.Quantity_Color) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Aspect_SequenceOfColor) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Quantity.Quantity_Color) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Aspect_SequenceOfColor) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.Quantity.Quantity_Color: 
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
    def Prepend(self,theSeq : Aspect_SequenceOfColor) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.Quantity.Quantity_Color) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.Quantity.Quantity_Color) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Aspect_SequenceOfColor) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Quantity.Quantity_Color: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Aspect_SequenceOfColor) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Aspect_Touch():
    """
    Structure holding touch position - original and current location.
    """
    def Delta(self) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        Return values delta.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,thePnt : OCP.Graphic3d.Graphic3d_Vec2d,theIsPreciseDevice : bool) -> None: ...
    @overload
    def __init__(self,theX : float,theY : float,theIsPreciseDevice : bool) -> None: ...
    @property
    def IsPreciseDevice(self) -> bool:
        """
        :type: bool
        """
    @IsPreciseDevice.setter
    def IsPreciseDevice(self, arg0: bool) -> None:
        pass
    pass
class Aspect_TouchMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : int,theItem : Aspect_Touch) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Aspect_TouchMap) -> Aspect_TouchMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> Aspect_Touch: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : int) -> Aspect_Touch: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : int) -> Aspect_Touch: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : int) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : Aspect_TouchMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> Aspect_Touch: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : int,theValue : Aspect_Touch) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : int) -> Aspect_Touch: ...
    def FindIndex(self,theKey1 : int) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> int: 
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
    def RemoveKey(self,theKey1 : int) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : int) -> Aspect_Touch: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : int,theItem : Aspect_Touch) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theOther : Aspect_TouchMap) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Aspect_TypeOfColorScaleData():
    """
    Defines the using type of colors and labels

    Members:

      Aspect_TOCSD_AUTO

      Aspect_TOCSD_USER
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
    Aspect_TOCSD_AUTO: OCP.Aspect.Aspect_TypeOfColorScaleData # value = Aspect_TypeOfColorScaleData.Aspect_TOCSD_AUTO
    Aspect_TOCSD_USER: OCP.Aspect.Aspect_TypeOfColorScaleData # value = Aspect_TypeOfColorScaleData.Aspect_TOCSD_USER
    __entries: dict # value = {'Aspect_TOCSD_AUTO': (Aspect_TypeOfColorScaleData.Aspect_TOCSD_AUTO, None), 'Aspect_TOCSD_USER': (Aspect_TypeOfColorScaleData.Aspect_TOCSD_USER, None)}
    __members__: dict # value = {'Aspect_TOCSD_AUTO': Aspect_TypeOfColorScaleData.Aspect_TOCSD_AUTO, 'Aspect_TOCSD_USER': Aspect_TypeOfColorScaleData.Aspect_TOCSD_USER}
    pass
class Aspect_TypeOfColorScaleOrientation():
    """
    Defines the type of color scale orientation

    Members:

      Aspect_TOCSO_NONE

      Aspect_TOCSO_LEFT

      Aspect_TOCSO_RIGHT

      Aspect_TOCSO_CENTER
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
    Aspect_TOCSO_CENTER: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_CENTER
    Aspect_TOCSO_LEFT: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_LEFT
    Aspect_TOCSO_NONE: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_NONE
    Aspect_TOCSO_RIGHT: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_RIGHT
    __entries: dict # value = {'Aspect_TOCSO_NONE': (Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_NONE, None), 'Aspect_TOCSO_LEFT': (Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_LEFT, None), 'Aspect_TOCSO_RIGHT': (Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_RIGHT, None), 'Aspect_TOCSO_CENTER': (Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_CENTER, None)}
    __members__: dict # value = {'Aspect_TOCSO_NONE': Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_NONE, 'Aspect_TOCSO_LEFT': Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_LEFT, 'Aspect_TOCSO_RIGHT': Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_RIGHT, 'Aspect_TOCSO_CENTER': Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_CENTER}
    pass
class Aspect_TypeOfColorScalePosition():
    """
    Defines the type of position for color scale labels

    Members:

      Aspect_TOCSP_NONE

      Aspect_TOCSP_LEFT

      Aspect_TOCSP_RIGHT

      Aspect_TOCSP_CENTER
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
    Aspect_TOCSP_CENTER: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_CENTER
    Aspect_TOCSP_LEFT: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_LEFT
    Aspect_TOCSP_NONE: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_NONE
    Aspect_TOCSP_RIGHT: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_RIGHT
    __entries: dict # value = {'Aspect_TOCSP_NONE': (Aspect_TypeOfColorScalePosition.Aspect_TOCSP_NONE, None), 'Aspect_TOCSP_LEFT': (Aspect_TypeOfColorScalePosition.Aspect_TOCSP_LEFT, None), 'Aspect_TOCSP_RIGHT': (Aspect_TypeOfColorScalePosition.Aspect_TOCSP_RIGHT, None), 'Aspect_TOCSP_CENTER': (Aspect_TypeOfColorScalePosition.Aspect_TOCSP_CENTER, None)}
    __members__: dict # value = {'Aspect_TOCSP_NONE': Aspect_TypeOfColorScalePosition.Aspect_TOCSP_NONE, 'Aspect_TOCSP_LEFT': Aspect_TypeOfColorScalePosition.Aspect_TOCSP_LEFT, 'Aspect_TOCSP_RIGHT': Aspect_TypeOfColorScalePosition.Aspect_TOCSP_RIGHT, 'Aspect_TOCSP_CENTER': Aspect_TypeOfColorScalePosition.Aspect_TOCSP_CENTER}
    pass
class Aspect_TypeOfDeflection():
    """
    Defines if the maximal chordial deflection used when drawing an object is absolute or relative to the size of the object.

    Members:

      Aspect_TOD_RELATIVE

      Aspect_TOD_ABSOLUTE
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
    Aspect_TOD_ABSOLUTE: OCP.Aspect.Aspect_TypeOfDeflection # value = Aspect_TypeOfDeflection.Aspect_TOD_ABSOLUTE
    Aspect_TOD_RELATIVE: OCP.Aspect.Aspect_TypeOfDeflection # value = Aspect_TypeOfDeflection.Aspect_TOD_RELATIVE
    __entries: dict # value = {'Aspect_TOD_RELATIVE': (Aspect_TypeOfDeflection.Aspect_TOD_RELATIVE, None), 'Aspect_TOD_ABSOLUTE': (Aspect_TypeOfDeflection.Aspect_TOD_ABSOLUTE, None)}
    __members__: dict # value = {'Aspect_TOD_RELATIVE': Aspect_TypeOfDeflection.Aspect_TOD_RELATIVE, 'Aspect_TOD_ABSOLUTE': Aspect_TypeOfDeflection.Aspect_TOD_ABSOLUTE}
    pass
class Aspect_TypeOfDisplayText():
    """
    Define the display type of the text.

    Members:

      Aspect_TODT_NORMAL

      Aspect_TODT_SUBTITLE

      Aspect_TODT_DEKALE

      Aspect_TODT_BLEND

      Aspect_TODT_DIMENSION

      Aspect_TODT_SHADOW
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
    Aspect_TODT_BLEND: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_BLEND
    Aspect_TODT_DEKALE: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_DEKALE
    Aspect_TODT_DIMENSION: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_DIMENSION
    Aspect_TODT_NORMAL: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL
    Aspect_TODT_SHADOW: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_SHADOW
    Aspect_TODT_SUBTITLE: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_SUBTITLE
    __entries: dict # value = {'Aspect_TODT_NORMAL': (Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL, None), 'Aspect_TODT_SUBTITLE': (Aspect_TypeOfDisplayText.Aspect_TODT_SUBTITLE, None), 'Aspect_TODT_DEKALE': (Aspect_TypeOfDisplayText.Aspect_TODT_DEKALE, None), 'Aspect_TODT_BLEND': (Aspect_TypeOfDisplayText.Aspect_TODT_BLEND, None), 'Aspect_TODT_DIMENSION': (Aspect_TypeOfDisplayText.Aspect_TODT_DIMENSION, None), 'Aspect_TODT_SHADOW': (Aspect_TypeOfDisplayText.Aspect_TODT_SHADOW, None)}
    __members__: dict # value = {'Aspect_TODT_NORMAL': Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL, 'Aspect_TODT_SUBTITLE': Aspect_TypeOfDisplayText.Aspect_TODT_SUBTITLE, 'Aspect_TODT_DEKALE': Aspect_TypeOfDisplayText.Aspect_TODT_DEKALE, 'Aspect_TODT_BLEND': Aspect_TypeOfDisplayText.Aspect_TODT_BLEND, 'Aspect_TODT_DIMENSION': Aspect_TypeOfDisplayText.Aspect_TODT_DIMENSION, 'Aspect_TODT_SHADOW': Aspect_TypeOfDisplayText.Aspect_TODT_SHADOW}
    pass
class Aspect_TypeOfFacingModel():
    """
    None

    Members:

      Aspect_TOFM_BOTH_SIDE

      Aspect_TOFM_BACK_SIDE

      Aspect_TOFM_FRONT_SIDE
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
    Aspect_TOFM_BACK_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = Aspect_TypeOfFacingModel.Aspect_TOFM_BACK_SIDE
    Aspect_TOFM_BOTH_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE
    Aspect_TOFM_FRONT_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE
    __entries: dict # value = {'Aspect_TOFM_BOTH_SIDE': (Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE, None), 'Aspect_TOFM_BACK_SIDE': (Aspect_TypeOfFacingModel.Aspect_TOFM_BACK_SIDE, None), 'Aspect_TOFM_FRONT_SIDE': (Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE, None)}
    __members__: dict # value = {'Aspect_TOFM_BOTH_SIDE': Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE, 'Aspect_TOFM_BACK_SIDE': Aspect_TypeOfFacingModel.Aspect_TOFM_BACK_SIDE, 'Aspect_TOFM_FRONT_SIDE': Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE}
    pass
class Aspect_TypeOfHighlightMethod():
    """
    Definition of a highlight method

    Members:

      Aspect_TOHM_COLOR

      Aspect_TOHM_BOUNDBOX
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
    Aspect_TOHM_BOUNDBOX: OCP.Aspect.Aspect_TypeOfHighlightMethod # value = Aspect_TypeOfHighlightMethod.Aspect_TOHM_BOUNDBOX
    Aspect_TOHM_COLOR: OCP.Aspect.Aspect_TypeOfHighlightMethod # value = Aspect_TypeOfHighlightMethod.Aspect_TOHM_COLOR
    __entries: dict # value = {'Aspect_TOHM_COLOR': (Aspect_TypeOfHighlightMethod.Aspect_TOHM_COLOR, None), 'Aspect_TOHM_BOUNDBOX': (Aspect_TypeOfHighlightMethod.Aspect_TOHM_BOUNDBOX, None)}
    __members__: dict # value = {'Aspect_TOHM_COLOR': Aspect_TypeOfHighlightMethod.Aspect_TOHM_COLOR, 'Aspect_TOHM_BOUNDBOX': Aspect_TypeOfHighlightMethod.Aspect_TOHM_BOUNDBOX}
    pass
class Aspect_TypeOfLine():
    """
    Definition of line types

    Members:

      Aspect_TOL_EMPTY

      Aspect_TOL_SOLID

      Aspect_TOL_DASH

      Aspect_TOL_DOT

      Aspect_TOL_DOTDASH

      Aspect_TOL_USERDEFINED
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
    Aspect_TOL_DASH: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_DASH
    Aspect_TOL_DOT: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_DOT
    Aspect_TOL_DOTDASH: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_DOTDASH
    Aspect_TOL_EMPTY: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_EMPTY
    Aspect_TOL_SOLID: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_SOLID
    Aspect_TOL_USERDEFINED: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_USERDEFINED
    __entries: dict # value = {'Aspect_TOL_EMPTY': (Aspect_TypeOfLine.Aspect_TOL_EMPTY, None), 'Aspect_TOL_SOLID': (Aspect_TypeOfLine.Aspect_TOL_SOLID, None), 'Aspect_TOL_DASH': (Aspect_TypeOfLine.Aspect_TOL_DASH, None), 'Aspect_TOL_DOT': (Aspect_TypeOfLine.Aspect_TOL_DOT, None), 'Aspect_TOL_DOTDASH': (Aspect_TypeOfLine.Aspect_TOL_DOTDASH, None), 'Aspect_TOL_USERDEFINED': (Aspect_TypeOfLine.Aspect_TOL_USERDEFINED, None)}
    __members__: dict # value = {'Aspect_TOL_EMPTY': Aspect_TypeOfLine.Aspect_TOL_EMPTY, 'Aspect_TOL_SOLID': Aspect_TypeOfLine.Aspect_TOL_SOLID, 'Aspect_TOL_DASH': Aspect_TypeOfLine.Aspect_TOL_DASH, 'Aspect_TOL_DOT': Aspect_TypeOfLine.Aspect_TOL_DOT, 'Aspect_TOL_DOTDASH': Aspect_TypeOfLine.Aspect_TOL_DOTDASH, 'Aspect_TOL_USERDEFINED': Aspect_TypeOfLine.Aspect_TOL_USERDEFINED}
    pass
class Aspect_TypeOfMarker():
    """
    Definition of types of markers

    Members:

      Aspect_TOM_EMPTY

      Aspect_TOM_POINT

      Aspect_TOM_PLUS

      Aspect_TOM_STAR

      Aspect_TOM_X

      Aspect_TOM_O

      Aspect_TOM_O_POINT

      Aspect_TOM_O_PLUS

      Aspect_TOM_O_STAR

      Aspect_TOM_O_X

      Aspect_TOM_RING1

      Aspect_TOM_RING2

      Aspect_TOM_RING3

      Aspect_TOM_BALL

      Aspect_TOM_USERDEFINED
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
    Aspect_TOM_BALL: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_BALL
    Aspect_TOM_EMPTY: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_EMPTY
    Aspect_TOM_O: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O
    Aspect_TOM_O_PLUS: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O_PLUS
    Aspect_TOM_O_POINT: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O_POINT
    Aspect_TOM_O_STAR: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O_STAR
    Aspect_TOM_O_X: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O_X
    Aspect_TOM_PLUS: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_PLUS
    Aspect_TOM_POINT: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_POINT
    Aspect_TOM_RING1: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_RING1
    Aspect_TOM_RING2: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_RING2
    Aspect_TOM_RING3: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_RING3
    Aspect_TOM_STAR: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_STAR
    Aspect_TOM_USERDEFINED: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_USERDEFINED
    Aspect_TOM_X: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_X
    __entries: dict # value = {'Aspect_TOM_EMPTY': (Aspect_TypeOfMarker.Aspect_TOM_EMPTY, None), 'Aspect_TOM_POINT': (Aspect_TypeOfMarker.Aspect_TOM_POINT, None), 'Aspect_TOM_PLUS': (Aspect_TypeOfMarker.Aspect_TOM_PLUS, None), 'Aspect_TOM_STAR': (Aspect_TypeOfMarker.Aspect_TOM_STAR, None), 'Aspect_TOM_X': (Aspect_TypeOfMarker.Aspect_TOM_X, None), 'Aspect_TOM_O': (Aspect_TypeOfMarker.Aspect_TOM_O, None), 'Aspect_TOM_O_POINT': (Aspect_TypeOfMarker.Aspect_TOM_O_POINT, None), 'Aspect_TOM_O_PLUS': (Aspect_TypeOfMarker.Aspect_TOM_O_PLUS, None), 'Aspect_TOM_O_STAR': (Aspect_TypeOfMarker.Aspect_TOM_O_STAR, None), 'Aspect_TOM_O_X': (Aspect_TypeOfMarker.Aspect_TOM_O_X, None), 'Aspect_TOM_RING1': (Aspect_TypeOfMarker.Aspect_TOM_RING1, None), 'Aspect_TOM_RING2': (Aspect_TypeOfMarker.Aspect_TOM_RING2, None), 'Aspect_TOM_RING3': (Aspect_TypeOfMarker.Aspect_TOM_RING3, None), 'Aspect_TOM_BALL': (Aspect_TypeOfMarker.Aspect_TOM_BALL, None), 'Aspect_TOM_USERDEFINED': (Aspect_TypeOfMarker.Aspect_TOM_USERDEFINED, None)}
    __members__: dict # value = {'Aspect_TOM_EMPTY': Aspect_TypeOfMarker.Aspect_TOM_EMPTY, 'Aspect_TOM_POINT': Aspect_TypeOfMarker.Aspect_TOM_POINT, 'Aspect_TOM_PLUS': Aspect_TypeOfMarker.Aspect_TOM_PLUS, 'Aspect_TOM_STAR': Aspect_TypeOfMarker.Aspect_TOM_STAR, 'Aspect_TOM_X': Aspect_TypeOfMarker.Aspect_TOM_X, 'Aspect_TOM_O': Aspect_TypeOfMarker.Aspect_TOM_O, 'Aspect_TOM_O_POINT': Aspect_TypeOfMarker.Aspect_TOM_O_POINT, 'Aspect_TOM_O_PLUS': Aspect_TypeOfMarker.Aspect_TOM_O_PLUS, 'Aspect_TOM_O_STAR': Aspect_TypeOfMarker.Aspect_TOM_O_STAR, 'Aspect_TOM_O_X': Aspect_TypeOfMarker.Aspect_TOM_O_X, 'Aspect_TOM_RING1': Aspect_TypeOfMarker.Aspect_TOM_RING1, 'Aspect_TOM_RING2': Aspect_TypeOfMarker.Aspect_TOM_RING2, 'Aspect_TOM_RING3': Aspect_TypeOfMarker.Aspect_TOM_RING3, 'Aspect_TOM_BALL': Aspect_TypeOfMarker.Aspect_TOM_BALL, 'Aspect_TOM_USERDEFINED': Aspect_TypeOfMarker.Aspect_TOM_USERDEFINED}
    pass
class Aspect_TypeOfResize():
    """
    Defines the type of Resize Window method applied by the user.

    Members:

      Aspect_TOR_UNKNOWN

      Aspect_TOR_NO_BORDER

      Aspect_TOR_TOP_BORDER

      Aspect_TOR_RIGHT_BORDER

      Aspect_TOR_BOTTOM_BORDER

      Aspect_TOR_LEFT_BORDER

      Aspect_TOR_TOP_AND_RIGHT_BORDER

      Aspect_TOR_RIGHT_AND_BOTTOM_BORDER

      Aspect_TOR_BOTTOM_AND_LEFT_BORDER

      Aspect_TOR_LEFT_AND_TOP_BORDER
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
    Aspect_TOR_BOTTOM_AND_LEFT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_BOTTOM_AND_LEFT_BORDER
    Aspect_TOR_BOTTOM_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_BOTTOM_BORDER
    Aspect_TOR_LEFT_AND_TOP_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_LEFT_AND_TOP_BORDER
    Aspect_TOR_LEFT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_LEFT_BORDER
    Aspect_TOR_NO_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_NO_BORDER
    Aspect_TOR_RIGHT_AND_BOTTOM_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_RIGHT_AND_BOTTOM_BORDER
    Aspect_TOR_RIGHT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_RIGHT_BORDER
    Aspect_TOR_TOP_AND_RIGHT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_TOP_AND_RIGHT_BORDER
    Aspect_TOR_TOP_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_TOP_BORDER
    Aspect_TOR_UNKNOWN: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_UNKNOWN
    __entries: dict # value = {'Aspect_TOR_UNKNOWN': (Aspect_TypeOfResize.Aspect_TOR_UNKNOWN, None), 'Aspect_TOR_NO_BORDER': (Aspect_TypeOfResize.Aspect_TOR_NO_BORDER, None), 'Aspect_TOR_TOP_BORDER': (Aspect_TypeOfResize.Aspect_TOR_TOP_BORDER, None), 'Aspect_TOR_RIGHT_BORDER': (Aspect_TypeOfResize.Aspect_TOR_RIGHT_BORDER, None), 'Aspect_TOR_BOTTOM_BORDER': (Aspect_TypeOfResize.Aspect_TOR_BOTTOM_BORDER, None), 'Aspect_TOR_LEFT_BORDER': (Aspect_TypeOfResize.Aspect_TOR_LEFT_BORDER, None), 'Aspect_TOR_TOP_AND_RIGHT_BORDER': (Aspect_TypeOfResize.Aspect_TOR_TOP_AND_RIGHT_BORDER, None), 'Aspect_TOR_RIGHT_AND_BOTTOM_BORDER': (Aspect_TypeOfResize.Aspect_TOR_RIGHT_AND_BOTTOM_BORDER, None), 'Aspect_TOR_BOTTOM_AND_LEFT_BORDER': (Aspect_TypeOfResize.Aspect_TOR_BOTTOM_AND_LEFT_BORDER, None), 'Aspect_TOR_LEFT_AND_TOP_BORDER': (Aspect_TypeOfResize.Aspect_TOR_LEFT_AND_TOP_BORDER, None)}
    __members__: dict # value = {'Aspect_TOR_UNKNOWN': Aspect_TypeOfResize.Aspect_TOR_UNKNOWN, 'Aspect_TOR_NO_BORDER': Aspect_TypeOfResize.Aspect_TOR_NO_BORDER, 'Aspect_TOR_TOP_BORDER': Aspect_TypeOfResize.Aspect_TOR_TOP_BORDER, 'Aspect_TOR_RIGHT_BORDER': Aspect_TypeOfResize.Aspect_TOR_RIGHT_BORDER, 'Aspect_TOR_BOTTOM_BORDER': Aspect_TypeOfResize.Aspect_TOR_BOTTOM_BORDER, 'Aspect_TOR_LEFT_BORDER': Aspect_TypeOfResize.Aspect_TOR_LEFT_BORDER, 'Aspect_TOR_TOP_AND_RIGHT_BORDER': Aspect_TypeOfResize.Aspect_TOR_TOP_AND_RIGHT_BORDER, 'Aspect_TOR_RIGHT_AND_BOTTOM_BORDER': Aspect_TypeOfResize.Aspect_TOR_RIGHT_AND_BOTTOM_BORDER, 'Aspect_TOR_BOTTOM_AND_LEFT_BORDER': Aspect_TypeOfResize.Aspect_TOR_BOTTOM_AND_LEFT_BORDER, 'Aspect_TOR_LEFT_AND_TOP_BORDER': Aspect_TypeOfResize.Aspect_TOR_LEFT_AND_TOP_BORDER}
    pass
class Aspect_TypeOfStyleText():
    """
    Define the style of the text.

    Members:

      Aspect_TOST_NORMAL

      Aspect_TOST_ANNOTATION
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
    Aspect_TOST_ANNOTATION: OCP.Aspect.Aspect_TypeOfStyleText # value = Aspect_TypeOfStyleText.Aspect_TOST_ANNOTATION
    Aspect_TOST_NORMAL: OCP.Aspect.Aspect_TypeOfStyleText # value = Aspect_TypeOfStyleText.Aspect_TOST_NORMAL
    __entries: dict # value = {'Aspect_TOST_NORMAL': (Aspect_TypeOfStyleText.Aspect_TOST_NORMAL, None), 'Aspect_TOST_ANNOTATION': (Aspect_TypeOfStyleText.Aspect_TOST_ANNOTATION, None)}
    __members__: dict # value = {'Aspect_TOST_NORMAL': Aspect_TypeOfStyleText.Aspect_TOST_NORMAL, 'Aspect_TOST_ANNOTATION': Aspect_TypeOfStyleText.Aspect_TOST_ANNOTATION}
    pass
class Aspect_TypeOfTriedronPosition():
    """
    Definition of the Trihedron position in the views. It is defined as a bitmask to simplify handling vertical and horizontal alignment independently.

    Members:

      Aspect_TOTP_CENTER

      Aspect_TOTP_TOP

      Aspect_TOTP_BOTTOM

      Aspect_TOTP_LEFT

      Aspect_TOTP_RIGHT

      Aspect_TOTP_LEFT_LOWER

      Aspect_TOTP_LEFT_UPPER

      Aspect_TOTP_RIGHT_LOWER

      Aspect_TOTP_RIGHT_UPPER
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
    Aspect_TOTP_BOTTOM: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_BOTTOM
    Aspect_TOTP_CENTER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER
    Aspect_TOTP_LEFT: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT
    Aspect_TOTP_LEFT_LOWER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_LOWER
    Aspect_TOTP_LEFT_UPPER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_UPPER
    Aspect_TOTP_RIGHT: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT
    Aspect_TOTP_RIGHT_LOWER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_LOWER
    Aspect_TOTP_RIGHT_UPPER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_UPPER
    Aspect_TOTP_TOP: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_TOP
    __entries: dict # value = {'Aspect_TOTP_CENTER': (Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER, None), 'Aspect_TOTP_TOP': (Aspect_TypeOfTriedronPosition.Aspect_TOTP_TOP, None), 'Aspect_TOTP_BOTTOM': (Aspect_TypeOfTriedronPosition.Aspect_TOTP_BOTTOM, None), 'Aspect_TOTP_LEFT': (Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT, None), 'Aspect_TOTP_RIGHT': (Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT, None), 'Aspect_TOTP_LEFT_LOWER': (Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_LOWER, None), 'Aspect_TOTP_LEFT_UPPER': (Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_UPPER, None), 'Aspect_TOTP_RIGHT_LOWER': (Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_LOWER, None), 'Aspect_TOTP_RIGHT_UPPER': (Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_UPPER, None)}
    __members__: dict # value = {'Aspect_TOTP_CENTER': Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER, 'Aspect_TOTP_TOP': Aspect_TypeOfTriedronPosition.Aspect_TOTP_TOP, 'Aspect_TOTP_BOTTOM': Aspect_TypeOfTriedronPosition.Aspect_TOTP_BOTTOM, 'Aspect_TOTP_LEFT': Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT, 'Aspect_TOTP_RIGHT': Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT, 'Aspect_TOTP_LEFT_LOWER': Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_LOWER, 'Aspect_TOTP_LEFT_UPPER': Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_UPPER, 'Aspect_TOTP_RIGHT_LOWER': Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_LOWER, 'Aspect_TOTP_RIGHT_UPPER': Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_UPPER}
    pass
class Aspect_VKeyBasic():
    """
    Enumeration defining virtual keys irrelevant to current keyboard layout for simplified hot-keys management logic.

    Members:

      Aspect_VKey_UNKNOWN

      Aspect_VKey_A

      Aspect_VKey_B

      Aspect_VKey_C

      Aspect_VKey_D

      Aspect_VKey_E

      Aspect_VKey_F

      Aspect_VKey_G

      Aspect_VKey_H

      Aspect_VKey_I

      Aspect_VKey_J

      Aspect_VKey_K

      Aspect_VKey_L

      Aspect_VKey_M

      Aspect_VKey_N

      Aspect_VKey_O

      Aspect_VKey_P

      Aspect_VKey_Q

      Aspect_VKey_R

      Aspect_VKey_S

      Aspect_VKey_T

      Aspect_VKey_U

      Aspect_VKey_V

      Aspect_VKey_W

      Aspect_VKey_X

      Aspect_VKey_Y

      Aspect_VKey_Z

      Aspect_VKey_0

      Aspect_VKey_1

      Aspect_VKey_2

      Aspect_VKey_3

      Aspect_VKey_4

      Aspect_VKey_5

      Aspect_VKey_6

      Aspect_VKey_7

      Aspect_VKey_8

      Aspect_VKey_9

      Aspect_VKey_F1

      Aspect_VKey_F2

      Aspect_VKey_F3

      Aspect_VKey_F4

      Aspect_VKey_F5

      Aspect_VKey_F6

      Aspect_VKey_F7

      Aspect_VKey_F8

      Aspect_VKey_F9

      Aspect_VKey_F10

      Aspect_VKey_F11

      Aspect_VKey_F12

      Aspect_VKey_Up

      Aspect_VKey_Down

      Aspect_VKey_Left

      Aspect_VKey_Right

      Aspect_VKey_Plus

      Aspect_VKey_Minus

      Aspect_VKey_Equal

      Aspect_VKey_PageUp

      Aspect_VKey_PageDown

      Aspect_VKey_Home

      Aspect_VKey_End

      Aspect_VKey_Escape

      Aspect_VKey_Back

      Aspect_VKey_Enter

      Aspect_VKey_Backspace

      Aspect_VKey_Space

      Aspect_VKey_Delete

      Aspect_VKey_Tilde

      Aspect_VKey_Tab

      Aspect_VKey_Comma

      Aspect_VKey_Period

      Aspect_VKey_Semicolon

      Aspect_VKey_Slash

      Aspect_VKey_BracketLeft

      Aspect_VKey_Backslash

      Aspect_VKey_BracketRight

      Aspect_VKey_Apostrophe

      Aspect_VKey_Numlock

      Aspect_VKey_Scroll

      Aspect_VKey_Numpad0

      Aspect_VKey_Numpad1

      Aspect_VKey_Numpad2

      Aspect_VKey_Numpad3

      Aspect_VKey_Numpad4

      Aspect_VKey_Numpad5

      Aspect_VKey_Numpad6

      Aspect_VKey_Numpad7

      Aspect_VKey_Numpad8

      Aspect_VKey_Numpad9

      Aspect_VKey_NumpadMultiply

      Aspect_VKey_NumpadAdd

      Aspect_VKey_NumpadSubtract

      Aspect_VKey_NumpadDivide

      Aspect_VKey_MediaNextTrack

      Aspect_VKey_MediaPreviousTrack

      Aspect_VKey_MediaStop

      Aspect_VKey_MediaPlayPause

      Aspect_VKey_VolumeMute

      Aspect_VKey_VolumeDown

      Aspect_VKey_VolumeUp

      Aspect_VKey_BrowserBack

      Aspect_VKey_BrowserForward

      Aspect_VKey_BrowserRefresh

      Aspect_VKey_BrowserStop

      Aspect_VKey_BrowserSearch

      Aspect_VKey_BrowserFavorites

      Aspect_VKey_BrowserHome

      Aspect_VKey_Shift

      Aspect_VKey_Control

      Aspect_VKey_Alt

      Aspect_VKey_Menu

      Aspect_VKey_Meta

      Aspect_VKey_NavInteract

      Aspect_VKey_NavForward

      Aspect_VKey_NavBackward

      Aspect_VKey_NavSlideLeft

      Aspect_VKey_NavSlideRight

      Aspect_VKey_NavSlideUp

      Aspect_VKey_NavSlideDown

      Aspect_VKey_NavRollCCW

      Aspect_VKey_NavRollCW

      Aspect_VKey_NavLookLeft

      Aspect_VKey_NavLookRight

      Aspect_VKey_NavLookUp

      Aspect_VKey_NavLookDown

      Aspect_VKey_NavCrouch

      Aspect_VKey_NavJump

      Aspect_VKey_NavThrustForward

      Aspect_VKey_NavThrustBackward

      Aspect_VKey_NavThrustStop

      Aspect_VKey_NavSpeedIncrease

      Aspect_VKey_NavSpeedDecrease
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
    Aspect_VKey_0: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_0
    Aspect_VKey_1: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_1
    Aspect_VKey_2: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_2
    Aspect_VKey_3: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_3
    Aspect_VKey_4: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_4
    Aspect_VKey_5: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_5
    Aspect_VKey_6: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_6
    Aspect_VKey_7: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_7
    Aspect_VKey_8: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_8
    Aspect_VKey_9: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_9
    Aspect_VKey_A: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_A
    Aspect_VKey_Alt: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Alt
    Aspect_VKey_Apostrophe: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Apostrophe
    Aspect_VKey_B: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_B
    Aspect_VKey_Back: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Back
    Aspect_VKey_Backslash: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Backslash
    Aspect_VKey_Backspace: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Backspace
    Aspect_VKey_BracketLeft: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BracketLeft
    Aspect_VKey_BracketRight: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BracketRight
    Aspect_VKey_BrowserBack: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserBack
    Aspect_VKey_BrowserFavorites: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserFavorites
    Aspect_VKey_BrowserForward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserForward
    Aspect_VKey_BrowserHome: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserHome
    Aspect_VKey_BrowserRefresh: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserRefresh
    Aspect_VKey_BrowserSearch: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserSearch
    Aspect_VKey_BrowserStop: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserStop
    Aspect_VKey_C: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_C
    Aspect_VKey_Comma: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Comma
    Aspect_VKey_Control: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Control
    Aspect_VKey_D: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_D
    Aspect_VKey_Delete: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Delete
    Aspect_VKey_Down: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Down
    Aspect_VKey_E: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_E
    Aspect_VKey_End: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_End
    Aspect_VKey_Enter: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Enter
    Aspect_VKey_Equal: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Equal
    Aspect_VKey_Escape: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Escape
    Aspect_VKey_F: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F
    Aspect_VKey_F1: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F1
    Aspect_VKey_F10: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F10
    Aspect_VKey_F11: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F11
    Aspect_VKey_F12: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F12
    Aspect_VKey_F2: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F2
    Aspect_VKey_F3: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F3
    Aspect_VKey_F4: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F4
    Aspect_VKey_F5: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F5
    Aspect_VKey_F6: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F6
    Aspect_VKey_F7: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F7
    Aspect_VKey_F8: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F8
    Aspect_VKey_F9: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F9
    Aspect_VKey_G: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_G
    Aspect_VKey_H: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_H
    Aspect_VKey_Home: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Home
    Aspect_VKey_I: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_I
    Aspect_VKey_J: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_J
    Aspect_VKey_K: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_K
    Aspect_VKey_L: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_L
    Aspect_VKey_Left: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Left
    Aspect_VKey_M: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_M
    Aspect_VKey_MediaNextTrack: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_MediaNextTrack
    Aspect_VKey_MediaPlayPause: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_MediaPlayPause
    Aspect_VKey_MediaPreviousTrack: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_MediaPreviousTrack
    Aspect_VKey_MediaStop: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_MediaStop
    Aspect_VKey_Menu: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Menu
    Aspect_VKey_Meta: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Meta
    Aspect_VKey_Minus: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Minus
    Aspect_VKey_N: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_N
    Aspect_VKey_NavBackward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavBackward
    Aspect_VKey_NavCrouch: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavCrouch
    Aspect_VKey_NavForward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavForward
    Aspect_VKey_NavInteract: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavInteract
    Aspect_VKey_NavJump: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavJump
    Aspect_VKey_NavLookDown: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavLookDown
    Aspect_VKey_NavLookLeft: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavLookLeft
    Aspect_VKey_NavLookRight: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavLookRight
    Aspect_VKey_NavLookUp: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavLookUp
    Aspect_VKey_NavRollCCW: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavRollCCW
    Aspect_VKey_NavRollCW: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavRollCW
    Aspect_VKey_NavSlideDown: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSlideDown
    Aspect_VKey_NavSlideLeft: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSlideLeft
    Aspect_VKey_NavSlideRight: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSlideRight
    Aspect_VKey_NavSlideUp: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSlideUp
    Aspect_VKey_NavSpeedDecrease: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSpeedDecrease
    Aspect_VKey_NavSpeedIncrease: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSpeedIncrease
    Aspect_VKey_NavThrustBackward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavThrustBackward
    Aspect_VKey_NavThrustForward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavThrustForward
    Aspect_VKey_NavThrustStop: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavThrustStop
    Aspect_VKey_Numlock: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numlock
    Aspect_VKey_Numpad0: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad0
    Aspect_VKey_Numpad1: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad1
    Aspect_VKey_Numpad2: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad2
    Aspect_VKey_Numpad3: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad3
    Aspect_VKey_Numpad4: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad4
    Aspect_VKey_Numpad5: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad5
    Aspect_VKey_Numpad6: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad6
    Aspect_VKey_Numpad7: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad7
    Aspect_VKey_Numpad8: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad8
    Aspect_VKey_Numpad9: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad9
    Aspect_VKey_NumpadAdd: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NumpadAdd
    Aspect_VKey_NumpadDivide: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NumpadDivide
    Aspect_VKey_NumpadMultiply: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NumpadMultiply
    Aspect_VKey_NumpadSubtract: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NumpadSubtract
    Aspect_VKey_O: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_O
    Aspect_VKey_P: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_P
    Aspect_VKey_PageDown: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_PageDown
    Aspect_VKey_PageUp: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_PageUp
    Aspect_VKey_Period: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Period
    Aspect_VKey_Plus: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Plus
    Aspect_VKey_Q: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Q
    Aspect_VKey_R: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_R
    Aspect_VKey_Right: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Right
    Aspect_VKey_S: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_S
    Aspect_VKey_Scroll: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Scroll
    Aspect_VKey_Semicolon: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Semicolon
    Aspect_VKey_Shift: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Shift
    Aspect_VKey_Slash: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Slash
    Aspect_VKey_Space: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Space
    Aspect_VKey_T: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_T
    Aspect_VKey_Tab: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Tab
    Aspect_VKey_Tilde: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Tilde
    Aspect_VKey_U: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_U
    Aspect_VKey_UNKNOWN: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_UNKNOWN
    Aspect_VKey_Up: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Up
    Aspect_VKey_V: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_V
    Aspect_VKey_VolumeDown: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_VolumeDown
    Aspect_VKey_VolumeMute: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_VolumeMute
    Aspect_VKey_VolumeUp: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_VolumeUp
    Aspect_VKey_W: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_W
    Aspect_VKey_X: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_X
    Aspect_VKey_Y: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Y
    Aspect_VKey_Z: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Z
    __entries: dict # value = {'Aspect_VKey_UNKNOWN': (Aspect_VKeyBasic.Aspect_VKey_UNKNOWN, None), 'Aspect_VKey_A': (Aspect_VKeyBasic.Aspect_VKey_A, None), 'Aspect_VKey_B': (Aspect_VKeyBasic.Aspect_VKey_B, None), 'Aspect_VKey_C': (Aspect_VKeyBasic.Aspect_VKey_C, None), 'Aspect_VKey_D': (Aspect_VKeyBasic.Aspect_VKey_D, None), 'Aspect_VKey_E': (Aspect_VKeyBasic.Aspect_VKey_E, None), 'Aspect_VKey_F': (Aspect_VKeyBasic.Aspect_VKey_F, None), 'Aspect_VKey_G': (Aspect_VKeyBasic.Aspect_VKey_G, None), 'Aspect_VKey_H': (Aspect_VKeyBasic.Aspect_VKey_H, None), 'Aspect_VKey_I': (Aspect_VKeyBasic.Aspect_VKey_I, None), 'Aspect_VKey_J': (Aspect_VKeyBasic.Aspect_VKey_J, None), 'Aspect_VKey_K': (Aspect_VKeyBasic.Aspect_VKey_K, None), 'Aspect_VKey_L': (Aspect_VKeyBasic.Aspect_VKey_L, None), 'Aspect_VKey_M': (Aspect_VKeyBasic.Aspect_VKey_M, None), 'Aspect_VKey_N': (Aspect_VKeyBasic.Aspect_VKey_N, None), 'Aspect_VKey_O': (Aspect_VKeyBasic.Aspect_VKey_O, None), 'Aspect_VKey_P': (Aspect_VKeyBasic.Aspect_VKey_P, None), 'Aspect_VKey_Q': (Aspect_VKeyBasic.Aspect_VKey_Q, None), 'Aspect_VKey_R': (Aspect_VKeyBasic.Aspect_VKey_R, None), 'Aspect_VKey_S': (Aspect_VKeyBasic.Aspect_VKey_S, None), 'Aspect_VKey_T': (Aspect_VKeyBasic.Aspect_VKey_T, None), 'Aspect_VKey_U': (Aspect_VKeyBasic.Aspect_VKey_U, None), 'Aspect_VKey_V': (Aspect_VKeyBasic.Aspect_VKey_V, None), 'Aspect_VKey_W': (Aspect_VKeyBasic.Aspect_VKey_W, None), 'Aspect_VKey_X': (Aspect_VKeyBasic.Aspect_VKey_X, None), 'Aspect_VKey_Y': (Aspect_VKeyBasic.Aspect_VKey_Y, None), 'Aspect_VKey_Z': (Aspect_VKeyBasic.Aspect_VKey_Z, None), 'Aspect_VKey_0': (Aspect_VKeyBasic.Aspect_VKey_0, None), 'Aspect_VKey_1': (Aspect_VKeyBasic.Aspect_VKey_1, None), 'Aspect_VKey_2': (Aspect_VKeyBasic.Aspect_VKey_2, None), 'Aspect_VKey_3': (Aspect_VKeyBasic.Aspect_VKey_3, None), 'Aspect_VKey_4': (Aspect_VKeyBasic.Aspect_VKey_4, None), 'Aspect_VKey_5': (Aspect_VKeyBasic.Aspect_VKey_5, None), 'Aspect_VKey_6': (Aspect_VKeyBasic.Aspect_VKey_6, None), 'Aspect_VKey_7': (Aspect_VKeyBasic.Aspect_VKey_7, None), 'Aspect_VKey_8': (Aspect_VKeyBasic.Aspect_VKey_8, None), 'Aspect_VKey_9': (Aspect_VKeyBasic.Aspect_VKey_9, None), 'Aspect_VKey_F1': (Aspect_VKeyBasic.Aspect_VKey_F1, None), 'Aspect_VKey_F2': (Aspect_VKeyBasic.Aspect_VKey_F2, None), 'Aspect_VKey_F3': (Aspect_VKeyBasic.Aspect_VKey_F3, None), 'Aspect_VKey_F4': (Aspect_VKeyBasic.Aspect_VKey_F4, None), 'Aspect_VKey_F5': (Aspect_VKeyBasic.Aspect_VKey_F5, None), 'Aspect_VKey_F6': (Aspect_VKeyBasic.Aspect_VKey_F6, None), 'Aspect_VKey_F7': (Aspect_VKeyBasic.Aspect_VKey_F7, None), 'Aspect_VKey_F8': (Aspect_VKeyBasic.Aspect_VKey_F8, None), 'Aspect_VKey_F9': (Aspect_VKeyBasic.Aspect_VKey_F9, None), 'Aspect_VKey_F10': (Aspect_VKeyBasic.Aspect_VKey_F10, None), 'Aspect_VKey_F11': (Aspect_VKeyBasic.Aspect_VKey_F11, None), 'Aspect_VKey_F12': (Aspect_VKeyBasic.Aspect_VKey_F12, None), 'Aspect_VKey_Up': (Aspect_VKeyBasic.Aspect_VKey_Up, None), 'Aspect_VKey_Down': (Aspect_VKeyBasic.Aspect_VKey_Down, None), 'Aspect_VKey_Left': (Aspect_VKeyBasic.Aspect_VKey_Left, None), 'Aspect_VKey_Right': (Aspect_VKeyBasic.Aspect_VKey_Right, None), 'Aspect_VKey_Plus': (Aspect_VKeyBasic.Aspect_VKey_Plus, None), 'Aspect_VKey_Minus': (Aspect_VKeyBasic.Aspect_VKey_Minus, None), 'Aspect_VKey_Equal': (Aspect_VKeyBasic.Aspect_VKey_Equal, None), 'Aspect_VKey_PageUp': (Aspect_VKeyBasic.Aspect_VKey_PageUp, None), 'Aspect_VKey_PageDown': (Aspect_VKeyBasic.Aspect_VKey_PageDown, None), 'Aspect_VKey_Home': (Aspect_VKeyBasic.Aspect_VKey_Home, None), 'Aspect_VKey_End': (Aspect_VKeyBasic.Aspect_VKey_End, None), 'Aspect_VKey_Escape': (Aspect_VKeyBasic.Aspect_VKey_Escape, None), 'Aspect_VKey_Back': (Aspect_VKeyBasic.Aspect_VKey_Back, None), 'Aspect_VKey_Enter': (Aspect_VKeyBasic.Aspect_VKey_Enter, None), 'Aspect_VKey_Backspace': (Aspect_VKeyBasic.Aspect_VKey_Backspace, None), 'Aspect_VKey_Space': (Aspect_VKeyBasic.Aspect_VKey_Space, None), 'Aspect_VKey_Delete': (Aspect_VKeyBasic.Aspect_VKey_Delete, None), 'Aspect_VKey_Tilde': (Aspect_VKeyBasic.Aspect_VKey_Tilde, None), 'Aspect_VKey_Tab': (Aspect_VKeyBasic.Aspect_VKey_Tab, None), 'Aspect_VKey_Comma': (Aspect_VKeyBasic.Aspect_VKey_Comma, None), 'Aspect_VKey_Period': (Aspect_VKeyBasic.Aspect_VKey_Period, None), 'Aspect_VKey_Semicolon': (Aspect_VKeyBasic.Aspect_VKey_Semicolon, None), 'Aspect_VKey_Slash': (Aspect_VKeyBasic.Aspect_VKey_Slash, None), 'Aspect_VKey_BracketLeft': (Aspect_VKeyBasic.Aspect_VKey_BracketLeft, None), 'Aspect_VKey_Backslash': (Aspect_VKeyBasic.Aspect_VKey_Backslash, None), 'Aspect_VKey_BracketRight': (Aspect_VKeyBasic.Aspect_VKey_BracketRight, None), 'Aspect_VKey_Apostrophe': (Aspect_VKeyBasic.Aspect_VKey_Apostrophe, None), 'Aspect_VKey_Numlock': (Aspect_VKeyBasic.Aspect_VKey_Numlock, None), 'Aspect_VKey_Scroll': (Aspect_VKeyBasic.Aspect_VKey_Scroll, None), 'Aspect_VKey_Numpad0': (Aspect_VKeyBasic.Aspect_VKey_Numpad0, None), 'Aspect_VKey_Numpad1': (Aspect_VKeyBasic.Aspect_VKey_Numpad1, None), 'Aspect_VKey_Numpad2': (Aspect_VKeyBasic.Aspect_VKey_Numpad2, None), 'Aspect_VKey_Numpad3': (Aspect_VKeyBasic.Aspect_VKey_Numpad3, None), 'Aspect_VKey_Numpad4': (Aspect_VKeyBasic.Aspect_VKey_Numpad4, None), 'Aspect_VKey_Numpad5': (Aspect_VKeyBasic.Aspect_VKey_Numpad5, None), 'Aspect_VKey_Numpad6': (Aspect_VKeyBasic.Aspect_VKey_Numpad6, None), 'Aspect_VKey_Numpad7': (Aspect_VKeyBasic.Aspect_VKey_Numpad7, None), 'Aspect_VKey_Numpad8': (Aspect_VKeyBasic.Aspect_VKey_Numpad8, None), 'Aspect_VKey_Numpad9': (Aspect_VKeyBasic.Aspect_VKey_Numpad9, None), 'Aspect_VKey_NumpadMultiply': (Aspect_VKeyBasic.Aspect_VKey_NumpadMultiply, None), 'Aspect_VKey_NumpadAdd': (Aspect_VKeyBasic.Aspect_VKey_NumpadAdd, None), 'Aspect_VKey_NumpadSubtract': (Aspect_VKeyBasic.Aspect_VKey_NumpadSubtract, None), 'Aspect_VKey_NumpadDivide': (Aspect_VKeyBasic.Aspect_VKey_NumpadDivide, None), 'Aspect_VKey_MediaNextTrack': (Aspect_VKeyBasic.Aspect_VKey_MediaNextTrack, None), 'Aspect_VKey_MediaPreviousTrack': (Aspect_VKeyBasic.Aspect_VKey_MediaPreviousTrack, None), 'Aspect_VKey_MediaStop': (Aspect_VKeyBasic.Aspect_VKey_MediaStop, None), 'Aspect_VKey_MediaPlayPause': (Aspect_VKeyBasic.Aspect_VKey_MediaPlayPause, None), 'Aspect_VKey_VolumeMute': (Aspect_VKeyBasic.Aspect_VKey_VolumeMute, None), 'Aspect_VKey_VolumeDown': (Aspect_VKeyBasic.Aspect_VKey_VolumeDown, None), 'Aspect_VKey_VolumeUp': (Aspect_VKeyBasic.Aspect_VKey_VolumeUp, None), 'Aspect_VKey_BrowserBack': (Aspect_VKeyBasic.Aspect_VKey_BrowserBack, None), 'Aspect_VKey_BrowserForward': (Aspect_VKeyBasic.Aspect_VKey_BrowserForward, None), 'Aspect_VKey_BrowserRefresh': (Aspect_VKeyBasic.Aspect_VKey_BrowserRefresh, None), 'Aspect_VKey_BrowserStop': (Aspect_VKeyBasic.Aspect_VKey_BrowserStop, None), 'Aspect_VKey_BrowserSearch': (Aspect_VKeyBasic.Aspect_VKey_BrowserSearch, None), 'Aspect_VKey_BrowserFavorites': (Aspect_VKeyBasic.Aspect_VKey_BrowserFavorites, None), 'Aspect_VKey_BrowserHome': (Aspect_VKeyBasic.Aspect_VKey_BrowserHome, None), 'Aspect_VKey_Shift': (Aspect_VKeyBasic.Aspect_VKey_Shift, None), 'Aspect_VKey_Control': (Aspect_VKeyBasic.Aspect_VKey_Control, None), 'Aspect_VKey_Alt': (Aspect_VKeyBasic.Aspect_VKey_Alt, None), 'Aspect_VKey_Menu': (Aspect_VKeyBasic.Aspect_VKey_Menu, None), 'Aspect_VKey_Meta': (Aspect_VKeyBasic.Aspect_VKey_Meta, None), 'Aspect_VKey_NavInteract': (Aspect_VKeyBasic.Aspect_VKey_NavInteract, None), 'Aspect_VKey_NavForward': (Aspect_VKeyBasic.Aspect_VKey_NavForward, None), 'Aspect_VKey_NavBackward': (Aspect_VKeyBasic.Aspect_VKey_NavBackward, None), 'Aspect_VKey_NavSlideLeft': (Aspect_VKeyBasic.Aspect_VKey_NavSlideLeft, None), 'Aspect_VKey_NavSlideRight': (Aspect_VKeyBasic.Aspect_VKey_NavSlideRight, None), 'Aspect_VKey_NavSlideUp': (Aspect_VKeyBasic.Aspect_VKey_NavSlideUp, None), 'Aspect_VKey_NavSlideDown': (Aspect_VKeyBasic.Aspect_VKey_NavSlideDown, None), 'Aspect_VKey_NavRollCCW': (Aspect_VKeyBasic.Aspect_VKey_NavRollCCW, None), 'Aspect_VKey_NavRollCW': (Aspect_VKeyBasic.Aspect_VKey_NavRollCW, None), 'Aspect_VKey_NavLookLeft': (Aspect_VKeyBasic.Aspect_VKey_NavLookLeft, None), 'Aspect_VKey_NavLookRight': (Aspect_VKeyBasic.Aspect_VKey_NavLookRight, None), 'Aspect_VKey_NavLookUp': (Aspect_VKeyBasic.Aspect_VKey_NavLookUp, None), 'Aspect_VKey_NavLookDown': (Aspect_VKeyBasic.Aspect_VKey_NavLookDown, None), 'Aspect_VKey_NavCrouch': (Aspect_VKeyBasic.Aspect_VKey_NavCrouch, None), 'Aspect_VKey_NavJump': (Aspect_VKeyBasic.Aspect_VKey_NavJump, None), 'Aspect_VKey_NavThrustForward': (Aspect_VKeyBasic.Aspect_VKey_NavThrustForward, None), 'Aspect_VKey_NavThrustBackward': (Aspect_VKeyBasic.Aspect_VKey_NavThrustBackward, None), 'Aspect_VKey_NavThrustStop': (Aspect_VKeyBasic.Aspect_VKey_NavThrustStop, None), 'Aspect_VKey_NavSpeedIncrease': (Aspect_VKeyBasic.Aspect_VKey_NavSpeedIncrease, None), 'Aspect_VKey_NavSpeedDecrease': (Aspect_VKeyBasic.Aspect_VKey_NavSpeedDecrease, None)}
    __members__: dict # value = {'Aspect_VKey_UNKNOWN': Aspect_VKeyBasic.Aspect_VKey_UNKNOWN, 'Aspect_VKey_A': Aspect_VKeyBasic.Aspect_VKey_A, 'Aspect_VKey_B': Aspect_VKeyBasic.Aspect_VKey_B, 'Aspect_VKey_C': Aspect_VKeyBasic.Aspect_VKey_C, 'Aspect_VKey_D': Aspect_VKeyBasic.Aspect_VKey_D, 'Aspect_VKey_E': Aspect_VKeyBasic.Aspect_VKey_E, 'Aspect_VKey_F': Aspect_VKeyBasic.Aspect_VKey_F, 'Aspect_VKey_G': Aspect_VKeyBasic.Aspect_VKey_G, 'Aspect_VKey_H': Aspect_VKeyBasic.Aspect_VKey_H, 'Aspect_VKey_I': Aspect_VKeyBasic.Aspect_VKey_I, 'Aspect_VKey_J': Aspect_VKeyBasic.Aspect_VKey_J, 'Aspect_VKey_K': Aspect_VKeyBasic.Aspect_VKey_K, 'Aspect_VKey_L': Aspect_VKeyBasic.Aspect_VKey_L, 'Aspect_VKey_M': Aspect_VKeyBasic.Aspect_VKey_M, 'Aspect_VKey_N': Aspect_VKeyBasic.Aspect_VKey_N, 'Aspect_VKey_O': Aspect_VKeyBasic.Aspect_VKey_O, 'Aspect_VKey_P': Aspect_VKeyBasic.Aspect_VKey_P, 'Aspect_VKey_Q': Aspect_VKeyBasic.Aspect_VKey_Q, 'Aspect_VKey_R': Aspect_VKeyBasic.Aspect_VKey_R, 'Aspect_VKey_S': Aspect_VKeyBasic.Aspect_VKey_S, 'Aspect_VKey_T': Aspect_VKeyBasic.Aspect_VKey_T, 'Aspect_VKey_U': Aspect_VKeyBasic.Aspect_VKey_U, 'Aspect_VKey_V': Aspect_VKeyBasic.Aspect_VKey_V, 'Aspect_VKey_W': Aspect_VKeyBasic.Aspect_VKey_W, 'Aspect_VKey_X': Aspect_VKeyBasic.Aspect_VKey_X, 'Aspect_VKey_Y': Aspect_VKeyBasic.Aspect_VKey_Y, 'Aspect_VKey_Z': Aspect_VKeyBasic.Aspect_VKey_Z, 'Aspect_VKey_0': Aspect_VKeyBasic.Aspect_VKey_0, 'Aspect_VKey_1': Aspect_VKeyBasic.Aspect_VKey_1, 'Aspect_VKey_2': Aspect_VKeyBasic.Aspect_VKey_2, 'Aspect_VKey_3': Aspect_VKeyBasic.Aspect_VKey_3, 'Aspect_VKey_4': Aspect_VKeyBasic.Aspect_VKey_4, 'Aspect_VKey_5': Aspect_VKeyBasic.Aspect_VKey_5, 'Aspect_VKey_6': Aspect_VKeyBasic.Aspect_VKey_6, 'Aspect_VKey_7': Aspect_VKeyBasic.Aspect_VKey_7, 'Aspect_VKey_8': Aspect_VKeyBasic.Aspect_VKey_8, 'Aspect_VKey_9': Aspect_VKeyBasic.Aspect_VKey_9, 'Aspect_VKey_F1': Aspect_VKeyBasic.Aspect_VKey_F1, 'Aspect_VKey_F2': Aspect_VKeyBasic.Aspect_VKey_F2, 'Aspect_VKey_F3': Aspect_VKeyBasic.Aspect_VKey_F3, 'Aspect_VKey_F4': Aspect_VKeyBasic.Aspect_VKey_F4, 'Aspect_VKey_F5': Aspect_VKeyBasic.Aspect_VKey_F5, 'Aspect_VKey_F6': Aspect_VKeyBasic.Aspect_VKey_F6, 'Aspect_VKey_F7': Aspect_VKeyBasic.Aspect_VKey_F7, 'Aspect_VKey_F8': Aspect_VKeyBasic.Aspect_VKey_F8, 'Aspect_VKey_F9': Aspect_VKeyBasic.Aspect_VKey_F9, 'Aspect_VKey_F10': Aspect_VKeyBasic.Aspect_VKey_F10, 'Aspect_VKey_F11': Aspect_VKeyBasic.Aspect_VKey_F11, 'Aspect_VKey_F12': Aspect_VKeyBasic.Aspect_VKey_F12, 'Aspect_VKey_Up': Aspect_VKeyBasic.Aspect_VKey_Up, 'Aspect_VKey_Down': Aspect_VKeyBasic.Aspect_VKey_Down, 'Aspect_VKey_Left': Aspect_VKeyBasic.Aspect_VKey_Left, 'Aspect_VKey_Right': Aspect_VKeyBasic.Aspect_VKey_Right, 'Aspect_VKey_Plus': Aspect_VKeyBasic.Aspect_VKey_Plus, 'Aspect_VKey_Minus': Aspect_VKeyBasic.Aspect_VKey_Minus, 'Aspect_VKey_Equal': Aspect_VKeyBasic.Aspect_VKey_Equal, 'Aspect_VKey_PageUp': Aspect_VKeyBasic.Aspect_VKey_PageUp, 'Aspect_VKey_PageDown': Aspect_VKeyBasic.Aspect_VKey_PageDown, 'Aspect_VKey_Home': Aspect_VKeyBasic.Aspect_VKey_Home, 'Aspect_VKey_End': Aspect_VKeyBasic.Aspect_VKey_End, 'Aspect_VKey_Escape': Aspect_VKeyBasic.Aspect_VKey_Escape, 'Aspect_VKey_Back': Aspect_VKeyBasic.Aspect_VKey_Back, 'Aspect_VKey_Enter': Aspect_VKeyBasic.Aspect_VKey_Enter, 'Aspect_VKey_Backspace': Aspect_VKeyBasic.Aspect_VKey_Backspace, 'Aspect_VKey_Space': Aspect_VKeyBasic.Aspect_VKey_Space, 'Aspect_VKey_Delete': Aspect_VKeyBasic.Aspect_VKey_Delete, 'Aspect_VKey_Tilde': Aspect_VKeyBasic.Aspect_VKey_Tilde, 'Aspect_VKey_Tab': Aspect_VKeyBasic.Aspect_VKey_Tab, 'Aspect_VKey_Comma': Aspect_VKeyBasic.Aspect_VKey_Comma, 'Aspect_VKey_Period': Aspect_VKeyBasic.Aspect_VKey_Period, 'Aspect_VKey_Semicolon': Aspect_VKeyBasic.Aspect_VKey_Semicolon, 'Aspect_VKey_Slash': Aspect_VKeyBasic.Aspect_VKey_Slash, 'Aspect_VKey_BracketLeft': Aspect_VKeyBasic.Aspect_VKey_BracketLeft, 'Aspect_VKey_Backslash': Aspect_VKeyBasic.Aspect_VKey_Backslash, 'Aspect_VKey_BracketRight': Aspect_VKeyBasic.Aspect_VKey_BracketRight, 'Aspect_VKey_Apostrophe': Aspect_VKeyBasic.Aspect_VKey_Apostrophe, 'Aspect_VKey_Numlock': Aspect_VKeyBasic.Aspect_VKey_Numlock, 'Aspect_VKey_Scroll': Aspect_VKeyBasic.Aspect_VKey_Scroll, 'Aspect_VKey_Numpad0': Aspect_VKeyBasic.Aspect_VKey_Numpad0, 'Aspect_VKey_Numpad1': Aspect_VKeyBasic.Aspect_VKey_Numpad1, 'Aspect_VKey_Numpad2': Aspect_VKeyBasic.Aspect_VKey_Numpad2, 'Aspect_VKey_Numpad3': Aspect_VKeyBasic.Aspect_VKey_Numpad3, 'Aspect_VKey_Numpad4': Aspect_VKeyBasic.Aspect_VKey_Numpad4, 'Aspect_VKey_Numpad5': Aspect_VKeyBasic.Aspect_VKey_Numpad5, 'Aspect_VKey_Numpad6': Aspect_VKeyBasic.Aspect_VKey_Numpad6, 'Aspect_VKey_Numpad7': Aspect_VKeyBasic.Aspect_VKey_Numpad7, 'Aspect_VKey_Numpad8': Aspect_VKeyBasic.Aspect_VKey_Numpad8, 'Aspect_VKey_Numpad9': Aspect_VKeyBasic.Aspect_VKey_Numpad9, 'Aspect_VKey_NumpadMultiply': Aspect_VKeyBasic.Aspect_VKey_NumpadMultiply, 'Aspect_VKey_NumpadAdd': Aspect_VKeyBasic.Aspect_VKey_NumpadAdd, 'Aspect_VKey_NumpadSubtract': Aspect_VKeyBasic.Aspect_VKey_NumpadSubtract, 'Aspect_VKey_NumpadDivide': Aspect_VKeyBasic.Aspect_VKey_NumpadDivide, 'Aspect_VKey_MediaNextTrack': Aspect_VKeyBasic.Aspect_VKey_MediaNextTrack, 'Aspect_VKey_MediaPreviousTrack': Aspect_VKeyBasic.Aspect_VKey_MediaPreviousTrack, 'Aspect_VKey_MediaStop': Aspect_VKeyBasic.Aspect_VKey_MediaStop, 'Aspect_VKey_MediaPlayPause': Aspect_VKeyBasic.Aspect_VKey_MediaPlayPause, 'Aspect_VKey_VolumeMute': Aspect_VKeyBasic.Aspect_VKey_VolumeMute, 'Aspect_VKey_VolumeDown': Aspect_VKeyBasic.Aspect_VKey_VolumeDown, 'Aspect_VKey_VolumeUp': Aspect_VKeyBasic.Aspect_VKey_VolumeUp, 'Aspect_VKey_BrowserBack': Aspect_VKeyBasic.Aspect_VKey_BrowserBack, 'Aspect_VKey_BrowserForward': Aspect_VKeyBasic.Aspect_VKey_BrowserForward, 'Aspect_VKey_BrowserRefresh': Aspect_VKeyBasic.Aspect_VKey_BrowserRefresh, 'Aspect_VKey_BrowserStop': Aspect_VKeyBasic.Aspect_VKey_BrowserStop, 'Aspect_VKey_BrowserSearch': Aspect_VKeyBasic.Aspect_VKey_BrowserSearch, 'Aspect_VKey_BrowserFavorites': Aspect_VKeyBasic.Aspect_VKey_BrowserFavorites, 'Aspect_VKey_BrowserHome': Aspect_VKeyBasic.Aspect_VKey_BrowserHome, 'Aspect_VKey_Shift': Aspect_VKeyBasic.Aspect_VKey_Shift, 'Aspect_VKey_Control': Aspect_VKeyBasic.Aspect_VKey_Control, 'Aspect_VKey_Alt': Aspect_VKeyBasic.Aspect_VKey_Alt, 'Aspect_VKey_Menu': Aspect_VKeyBasic.Aspect_VKey_Menu, 'Aspect_VKey_Meta': Aspect_VKeyBasic.Aspect_VKey_Meta, 'Aspect_VKey_NavInteract': Aspect_VKeyBasic.Aspect_VKey_NavInteract, 'Aspect_VKey_NavForward': Aspect_VKeyBasic.Aspect_VKey_NavForward, 'Aspect_VKey_NavBackward': Aspect_VKeyBasic.Aspect_VKey_NavBackward, 'Aspect_VKey_NavSlideLeft': Aspect_VKeyBasic.Aspect_VKey_NavSlideLeft, 'Aspect_VKey_NavSlideRight': Aspect_VKeyBasic.Aspect_VKey_NavSlideRight, 'Aspect_VKey_NavSlideUp': Aspect_VKeyBasic.Aspect_VKey_NavSlideUp, 'Aspect_VKey_NavSlideDown': Aspect_VKeyBasic.Aspect_VKey_NavSlideDown, 'Aspect_VKey_NavRollCCW': Aspect_VKeyBasic.Aspect_VKey_NavRollCCW, 'Aspect_VKey_NavRollCW': Aspect_VKeyBasic.Aspect_VKey_NavRollCW, 'Aspect_VKey_NavLookLeft': Aspect_VKeyBasic.Aspect_VKey_NavLookLeft, 'Aspect_VKey_NavLookRight': Aspect_VKeyBasic.Aspect_VKey_NavLookRight, 'Aspect_VKey_NavLookUp': Aspect_VKeyBasic.Aspect_VKey_NavLookUp, 'Aspect_VKey_NavLookDown': Aspect_VKeyBasic.Aspect_VKey_NavLookDown, 'Aspect_VKey_NavCrouch': Aspect_VKeyBasic.Aspect_VKey_NavCrouch, 'Aspect_VKey_NavJump': Aspect_VKeyBasic.Aspect_VKey_NavJump, 'Aspect_VKey_NavThrustForward': Aspect_VKeyBasic.Aspect_VKey_NavThrustForward, 'Aspect_VKey_NavThrustBackward': Aspect_VKeyBasic.Aspect_VKey_NavThrustBackward, 'Aspect_VKey_NavThrustStop': Aspect_VKeyBasic.Aspect_VKey_NavThrustStop, 'Aspect_VKey_NavSpeedIncrease': Aspect_VKeyBasic.Aspect_VKey_NavSpeedIncrease, 'Aspect_VKey_NavSpeedDecrease': Aspect_VKeyBasic.Aspect_VKey_NavSpeedDecrease}
    pass
class Aspect_WidthOfLine():
    """
    Definition of line types

    Members:

      Aspect_WOL_THIN

      Aspect_WOL_MEDIUM

      Aspect_WOL_THICK

      Aspect_WOL_VERYTHICK

      Aspect_WOL_USERDEFINED
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
    Aspect_WOL_MEDIUM: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_MEDIUM
    Aspect_WOL_THICK: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_THICK
    Aspect_WOL_THIN: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_THIN
    Aspect_WOL_USERDEFINED: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_USERDEFINED
    Aspect_WOL_VERYTHICK: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_VERYTHICK
    __entries: dict # value = {'Aspect_WOL_THIN': (Aspect_WidthOfLine.Aspect_WOL_THIN, None), 'Aspect_WOL_MEDIUM': (Aspect_WidthOfLine.Aspect_WOL_MEDIUM, None), 'Aspect_WOL_THICK': (Aspect_WidthOfLine.Aspect_WOL_THICK, None), 'Aspect_WOL_VERYTHICK': (Aspect_WidthOfLine.Aspect_WOL_VERYTHICK, None), 'Aspect_WOL_USERDEFINED': (Aspect_WidthOfLine.Aspect_WOL_USERDEFINED, None)}
    __members__: dict # value = {'Aspect_WOL_THIN': Aspect_WidthOfLine.Aspect_WOL_THIN, 'Aspect_WOL_MEDIUM': Aspect_WidthOfLine.Aspect_WOL_MEDIUM, 'Aspect_WOL_THICK': Aspect_WidthOfLine.Aspect_WOL_THICK, 'Aspect_WOL_VERYTHICK': Aspect_WidthOfLine.Aspect_WOL_VERYTHICK, 'Aspect_WOL_USERDEFINED': Aspect_WidthOfLine.Aspect_WOL_USERDEFINED}
    pass
class Aspect_NeutralWindow(Aspect_Window, OCP.Standard.Standard_Transient):
    """
    Defines a platform-neutral window. This class is intended to be used in context when window management (including OpenGL context creation) is performed on application side (e.g. using external framework).Defines a platform-neutral window. This class is intended to be used in context when window management (including OpenGL context creation) is performed on application side (e.g. using external framework).
    """
    def Background(self) -> Aspect_Background: 
        """
        Returns the window background.
        """
    def BackgroundFillMethod(self) -> Aspect_FillMethod: 
        """
        Returns the current image background fill mode.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DoMapping(self) -> bool: 
        """
        Map window - do nothing.
        """
    def DoResize(self) -> Aspect_TypeOfResize: 
        """
        Resize window - do nothing.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GradientBackground(self) -> Aspect_GradientBackground: 
        """
        Returns the window gradient background.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvalidateContent(self,theDisp : Aspect_DisplayConnection) -> None: 
        """
        Invalidate entire window content.
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
    def IsMapped(self) -> bool: 
        """
        Return true if window is not hidden.
        """
    def IsVirtual(self) -> bool: 
        """
        Returns True if the window <me> is virtual
        """
    def Map(self) -> None: 
        """
        Change window mapped flag to TRUE.
        """
    def NativeHandle(self) -> int: 
        """
        Return native handle of this drawable.
        """
    def NativeParentHandle(self) -> int: 
        """
        Return native handle of the parent drawable.
        """
    def Position(self) -> Tuple[int, int, int, int]: 
        """
        Return the window position.
        """
    def Ratio(self) -> float: 
        """
        Returns window ratio equal to the physical width/height dimensions.
        """
    @overload
    def SetBackground(self,color : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the window background.

        Modifies the window background.

        Modifies the window gradient background.

        Modifies the window gradient background.
        """
    @overload
    def SetBackground(self,theFirstColor : OCP.Quantity.Quantity_Color,theSecondColor : OCP.Quantity.Quantity_Color,theFillMethod : Aspect_GradientFillMethod) -> None: ...
    @overload
    def SetBackground(self,ABack : Aspect_Background) -> None: ...
    @overload
    def SetBackground(self,ABackground : Aspect_GradientBackground) -> None: ...
    def SetNativeHandle(self,theWindow : int) -> bool: 
        """
        Set native handle.
        """
    @overload
    def SetPosition(self,theX1 : int,theY1 : int) -> bool: 
        """
        Set the window position.

        Set the window position.
        """
    @overload
    def SetPosition(self,theX1 : int,theY1 : int,theX2 : int,theY2 : int) -> bool: ...
    def SetSize(self,theWidth : int,theHeight : int) -> bool: 
        """
        Set the window size.
        """
    def SetTitle(self,theTitle : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets window title.
        """
    def SetVirtual(self,theVirtual : bool) -> None: 
        """
        Setup the virtual state
        """
    def Size(self) -> Tuple[int, int]: 
        """
        Return the window size.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unmap(self) -> None: 
        """
        Change window mapped flag to FALSE.
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
class Aspect_WindowDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Aspect', '__weakref__': <attribute '__weakref__' of 'Aspect_WindowDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Aspect_WindowDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Aspect_WindowError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Aspect', '__weakref__': <attribute '__weakref__' of 'Aspect_WindowError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Aspect_WindowError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Aspect_XAtom():
    """
    Defines custom identifiers(atoms) for X window custom named properties

    Members:

      Aspect_XA_DELETE_WINDOW
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
    Aspect_XA_DELETE_WINDOW: OCP.Aspect.Aspect_XAtom # value = Aspect_XAtom.Aspect_XA_DELETE_WINDOW
    __entries: dict # value = {'Aspect_XA_DELETE_WINDOW': (Aspect_XAtom.Aspect_XA_DELETE_WINDOW, None)}
    __members__: dict # value = {'Aspect_XA_DELETE_WINDOW': Aspect_XAtom.Aspect_XA_DELETE_WINDOW}
    pass
def Aspect_VKey2Modifier(theKey : int) -> int:
    """
    Return modifier flags for specified modifier key.
    """
Aspect_FM_CENTERED: OCP.Aspect.Aspect_FillMethod # value = Aspect_FillMethod.Aspect_FM_CENTERED
Aspect_FM_NONE: OCP.Aspect.Aspect_FillMethod # value = Aspect_FillMethod.Aspect_FM_NONE
Aspect_FM_STRETCH: OCP.Aspect.Aspect_FillMethod # value = Aspect_FillMethod.Aspect_FM_STRETCH
Aspect_FM_TILED: OCP.Aspect.Aspect_FillMethod # value = Aspect_FillMethod.Aspect_FM_TILED
Aspect_GDM_Lines: OCP.Aspect.Aspect_GridDrawMode # value = Aspect_GridDrawMode.Aspect_GDM_Lines
Aspect_GDM_None: OCP.Aspect.Aspect_GridDrawMode # value = Aspect_GridDrawMode.Aspect_GDM_None
Aspect_GDM_Points: OCP.Aspect.Aspect_GridDrawMode # value = Aspect_GridDrawMode.Aspect_GDM_Points
Aspect_GFM_CORNER1: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_CORNER1
Aspect_GFM_CORNER2: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_CORNER2
Aspect_GFM_CORNER3: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_CORNER3
Aspect_GFM_CORNER4: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_CORNER4
Aspect_GFM_DIAG1: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_DIAG1
Aspect_GFM_DIAG2: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_DIAG2
Aspect_GFM_HOR: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_HOR
Aspect_GFM_NONE: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_NONE
Aspect_GFM_VER: OCP.Aspect.Aspect_GradientFillMethod # value = Aspect_GradientFillMethod.Aspect_GFM_VER
Aspect_GT_Circular: OCP.Aspect.Aspect_GridType # value = Aspect_GridType.Aspect_GT_Circular
Aspect_GT_Rectangular: OCP.Aspect.Aspect_GridType # value = Aspect_GridType.Aspect_GT_Rectangular
Aspect_HS_DIAGONAL_135: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_DIAGONAL_135
Aspect_HS_DIAGONAL_135_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_DIAGONAL_135_WIDE
Aspect_HS_DIAGONAL_45: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_DIAGONAL_45
Aspect_HS_DIAGONAL_45_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_DIAGONAL_45_WIDE
Aspect_HS_GRID: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_GRID
Aspect_HS_GRID_DIAGONAL: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL
Aspect_HS_GRID_DIAGONAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL_WIDE
Aspect_HS_GRID_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_GRID_WIDE
Aspect_HS_HORIZONTAL: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_HORIZONTAL
Aspect_HS_HORIZONTAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_HORIZONTAL_WIDE
Aspect_HS_NB: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_NB
Aspect_HS_SOLID: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_SOLID
Aspect_HS_VERTICAL: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_VERTICAL
Aspect_HS_VERTICAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = Aspect_HatchStyle.Aspect_HS_VERTICAL_WIDE
Aspect_IS_EMPTY: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_EMPTY
Aspect_IS_HATCH: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_HATCH
Aspect_IS_HIDDENLINE: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_HIDDENLINE
Aspect_IS_HOLLOW: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_EMPTY
Aspect_IS_POINT: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_POINT
Aspect_IS_SOLID: OCP.Aspect.Aspect_InteriorStyle # value = Aspect_InteriorStyle.Aspect_IS_SOLID
Aspect_POM_All: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_All
Aspect_POM_Fill: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Fill
Aspect_POM_Line: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Line
Aspect_POM_Mask: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Mask
Aspect_POM_None: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_None
Aspect_POM_Off: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Off
Aspect_POM_Point: OCP.Aspect.Aspect_PolygonOffsetMode # value = Aspect_PolygonOffsetMode.Aspect_POM_Point
Aspect_TOCSD_AUTO: OCP.Aspect.Aspect_TypeOfColorScaleData # value = Aspect_TypeOfColorScaleData.Aspect_TOCSD_AUTO
Aspect_TOCSD_USER: OCP.Aspect.Aspect_TypeOfColorScaleData # value = Aspect_TypeOfColorScaleData.Aspect_TOCSD_USER
Aspect_TOCSO_CENTER: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_CENTER
Aspect_TOCSO_LEFT: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_LEFT
Aspect_TOCSO_NONE: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_NONE
Aspect_TOCSO_RIGHT: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_RIGHT
Aspect_TOCSP_CENTER: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_CENTER
Aspect_TOCSP_LEFT: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_LEFT
Aspect_TOCSP_NONE: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_NONE
Aspect_TOCSP_RIGHT: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_RIGHT
Aspect_TODT_BLEND: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_BLEND
Aspect_TODT_DEKALE: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_DEKALE
Aspect_TODT_DIMENSION: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_DIMENSION
Aspect_TODT_NORMAL: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL
Aspect_TODT_SHADOW: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_SHADOW
Aspect_TODT_SUBTITLE: OCP.Aspect.Aspect_TypeOfDisplayText # value = Aspect_TypeOfDisplayText.Aspect_TODT_SUBTITLE
Aspect_TOD_ABSOLUTE: OCP.Aspect.Aspect_TypeOfDeflection # value = Aspect_TypeOfDeflection.Aspect_TOD_ABSOLUTE
Aspect_TOD_RELATIVE: OCP.Aspect.Aspect_TypeOfDeflection # value = Aspect_TypeOfDeflection.Aspect_TOD_RELATIVE
Aspect_TOFM_BACK_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = Aspect_TypeOfFacingModel.Aspect_TOFM_BACK_SIDE
Aspect_TOFM_BOTH_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE
Aspect_TOFM_FRONT_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE
Aspect_TOHM_BOUNDBOX: OCP.Aspect.Aspect_TypeOfHighlightMethod # value = Aspect_TypeOfHighlightMethod.Aspect_TOHM_BOUNDBOX
Aspect_TOHM_COLOR: OCP.Aspect.Aspect_TypeOfHighlightMethod # value = Aspect_TypeOfHighlightMethod.Aspect_TOHM_COLOR
Aspect_TOL_DASH: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_DASH
Aspect_TOL_DOT: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_DOT
Aspect_TOL_DOTDASH: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_DOTDASH
Aspect_TOL_EMPTY: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_EMPTY
Aspect_TOL_SOLID: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_SOLID
Aspect_TOL_USERDEFINED: OCP.Aspect.Aspect_TypeOfLine # value = Aspect_TypeOfLine.Aspect_TOL_USERDEFINED
Aspect_TOM_BALL: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_BALL
Aspect_TOM_EMPTY: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_EMPTY
Aspect_TOM_O: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O
Aspect_TOM_O_PLUS: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O_PLUS
Aspect_TOM_O_POINT: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O_POINT
Aspect_TOM_O_STAR: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O_STAR
Aspect_TOM_O_X: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_O_X
Aspect_TOM_PLUS: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_PLUS
Aspect_TOM_POINT: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_POINT
Aspect_TOM_RING1: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_RING1
Aspect_TOM_RING2: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_RING2
Aspect_TOM_RING3: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_RING3
Aspect_TOM_STAR: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_STAR
Aspect_TOM_USERDEFINED: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_USERDEFINED
Aspect_TOM_X: OCP.Aspect.Aspect_TypeOfMarker # value = Aspect_TypeOfMarker.Aspect_TOM_X
Aspect_TOR_BOTTOM_AND_LEFT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_BOTTOM_AND_LEFT_BORDER
Aspect_TOR_BOTTOM_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_BOTTOM_BORDER
Aspect_TOR_LEFT_AND_TOP_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_LEFT_AND_TOP_BORDER
Aspect_TOR_LEFT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_LEFT_BORDER
Aspect_TOR_NO_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_NO_BORDER
Aspect_TOR_RIGHT_AND_BOTTOM_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_RIGHT_AND_BOTTOM_BORDER
Aspect_TOR_RIGHT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_RIGHT_BORDER
Aspect_TOR_TOP_AND_RIGHT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_TOP_AND_RIGHT_BORDER
Aspect_TOR_TOP_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_TOP_BORDER
Aspect_TOR_UNKNOWN: OCP.Aspect.Aspect_TypeOfResize # value = Aspect_TypeOfResize.Aspect_TOR_UNKNOWN
Aspect_TOST_ANNOTATION: OCP.Aspect.Aspect_TypeOfStyleText # value = Aspect_TypeOfStyleText.Aspect_TOST_ANNOTATION
Aspect_TOST_NORMAL: OCP.Aspect.Aspect_TypeOfStyleText # value = Aspect_TypeOfStyleText.Aspect_TOST_NORMAL
Aspect_TOTP_BOTTOM: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_BOTTOM
Aspect_TOTP_CENTER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER
Aspect_TOTP_LEFT: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT
Aspect_TOTP_LEFT_LOWER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_LOWER
Aspect_TOTP_LEFT_UPPER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_UPPER
Aspect_TOTP_RIGHT: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT
Aspect_TOTP_RIGHT_LOWER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_LOWER
Aspect_TOTP_RIGHT_UPPER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_UPPER
Aspect_TOTP_TOP: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = Aspect_TypeOfTriedronPosition.Aspect_TOTP_TOP
Aspect_VKeyFlags_ALL = 7936
Aspect_VKeyFlags_ALT = 1024
Aspect_VKeyFlags_CTRL = 512
Aspect_VKeyFlags_MENU = 2048
Aspect_VKeyFlags_META = 4096
Aspect_VKeyFlags_NONE = 0
Aspect_VKeyFlags_SHIFT = 256
Aspect_VKeyMouse_LeftButton = 8192
Aspect_VKeyMouse_MainButtons = 57344
Aspect_VKeyMouse_MiddleButton = 16384
Aspect_VKeyMouse_NONE = 0
Aspect_VKeyMouse_RightButton = 32768
Aspect_VKey_0: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_0
Aspect_VKey_1: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_1
Aspect_VKey_2: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_2
Aspect_VKey_3: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_3
Aspect_VKey_4: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_4
Aspect_VKey_5: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_5
Aspect_VKey_6: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_6
Aspect_VKey_7: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_7
Aspect_VKey_8: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_8
Aspect_VKey_9: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_9
Aspect_VKey_A: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_A
Aspect_VKey_Alt: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Alt
Aspect_VKey_Apostrophe: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Apostrophe
Aspect_VKey_B: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_B
Aspect_VKey_Back: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Back
Aspect_VKey_Backslash: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Backslash
Aspect_VKey_Backspace: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Backspace
Aspect_VKey_BracketLeft: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BracketLeft
Aspect_VKey_BracketRight: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BracketRight
Aspect_VKey_BrowserBack: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserBack
Aspect_VKey_BrowserFavorites: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserFavorites
Aspect_VKey_BrowserForward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserForward
Aspect_VKey_BrowserHome: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserHome
Aspect_VKey_BrowserRefresh: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserRefresh
Aspect_VKey_BrowserSearch: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserSearch
Aspect_VKey_BrowserStop: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_BrowserStop
Aspect_VKey_C: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_C
Aspect_VKey_Comma: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Comma
Aspect_VKey_Control: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Control
Aspect_VKey_D: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_D
Aspect_VKey_Delete: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Delete
Aspect_VKey_Down: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Down
Aspect_VKey_E: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_E
Aspect_VKey_End: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_End
Aspect_VKey_Enter: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Enter
Aspect_VKey_Equal: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Equal
Aspect_VKey_Escape: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Escape
Aspect_VKey_F: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F
Aspect_VKey_F1: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F1
Aspect_VKey_F10: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F10
Aspect_VKey_F11: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F11
Aspect_VKey_F12: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F12
Aspect_VKey_F2: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F2
Aspect_VKey_F3: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F3
Aspect_VKey_F4: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F4
Aspect_VKey_F5: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F5
Aspect_VKey_F6: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F6
Aspect_VKey_F7: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F7
Aspect_VKey_F8: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F8
Aspect_VKey_F9: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_F9
Aspect_VKey_G: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_G
Aspect_VKey_H: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_H
Aspect_VKey_Home: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Home
Aspect_VKey_I: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_I
Aspect_VKey_J: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_J
Aspect_VKey_K: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_K
Aspect_VKey_L: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_L
Aspect_VKey_Left: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Left
Aspect_VKey_Lower = 0
Aspect_VKey_M: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_M
Aspect_VKey_MAX = 255
Aspect_VKey_MediaNextTrack: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_MediaNextTrack
Aspect_VKey_MediaPlayPause: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_MediaPlayPause
Aspect_VKey_MediaPreviousTrack: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_MediaPreviousTrack
Aspect_VKey_MediaStop: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_MediaStop
Aspect_VKey_Menu: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Menu
Aspect_VKey_Meta: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Meta
Aspect_VKey_Minus: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Minus
Aspect_VKey_ModifiersLower = 106
Aspect_VKey_ModifiersUpper = 110
Aspect_VKey_N: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_N
Aspect_VKey_NB = 131
Aspect_VKey_NavBackward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavBackward
Aspect_VKey_NavCrouch: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavCrouch
Aspect_VKey_NavForward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavForward
Aspect_VKey_NavInteract: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavInteract
Aspect_VKey_NavJump: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavJump
Aspect_VKey_NavLookDown: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavLookDown
Aspect_VKey_NavLookLeft: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavLookLeft
Aspect_VKey_NavLookRight: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavLookRight
Aspect_VKey_NavLookUp: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavLookUp
Aspect_VKey_NavRollCCW: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavRollCCW
Aspect_VKey_NavRollCW: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavRollCW
Aspect_VKey_NavSlideDown: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSlideDown
Aspect_VKey_NavSlideLeft: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSlideLeft
Aspect_VKey_NavSlideRight: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSlideRight
Aspect_VKey_NavSlideUp: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSlideUp
Aspect_VKey_NavSpeedDecrease: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSpeedDecrease
Aspect_VKey_NavSpeedIncrease: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavSpeedIncrease
Aspect_VKey_NavThrustBackward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavThrustBackward
Aspect_VKey_NavThrustForward: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavThrustForward
Aspect_VKey_NavThrustStop: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NavThrustStop
Aspect_VKey_NavigationKeysLower = 111
Aspect_VKey_NavigationKeysUpper = 130
Aspect_VKey_Numlock: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numlock
Aspect_VKey_Numpad0: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad0
Aspect_VKey_Numpad1: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad1
Aspect_VKey_Numpad2: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad2
Aspect_VKey_Numpad3: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad3
Aspect_VKey_Numpad4: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad4
Aspect_VKey_Numpad5: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad5
Aspect_VKey_Numpad6: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad6
Aspect_VKey_Numpad7: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad7
Aspect_VKey_Numpad8: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad8
Aspect_VKey_Numpad9: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Numpad9
Aspect_VKey_NumpadAdd: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NumpadAdd
Aspect_VKey_NumpadDivide: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NumpadDivide
Aspect_VKey_NumpadMultiply: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NumpadMultiply
Aspect_VKey_NumpadSubtract: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_NumpadSubtract
Aspect_VKey_O: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_O
Aspect_VKey_P: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_P
Aspect_VKey_PageDown: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_PageDown
Aspect_VKey_PageUp: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_PageUp
Aspect_VKey_Period: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Period
Aspect_VKey_Plus: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Plus
Aspect_VKey_Q: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Q
Aspect_VKey_R: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_R
Aspect_VKey_Right: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Right
Aspect_VKey_S: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_S
Aspect_VKey_Scroll: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Scroll
Aspect_VKey_Semicolon: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Semicolon
Aspect_VKey_Shift: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Shift
Aspect_VKey_Slash: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Slash
Aspect_VKey_Space: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Space
Aspect_VKey_T: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_T
Aspect_VKey_Tab: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Tab
Aspect_VKey_Tilde: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Tilde
Aspect_VKey_U: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_U
Aspect_VKey_UNKNOWN: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_UNKNOWN
Aspect_VKey_Up: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Up
Aspect_VKey_Upper = 130
Aspect_VKey_V: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_V
Aspect_VKey_VolumeDown: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_VolumeDown
Aspect_VKey_VolumeMute: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_VolumeMute
Aspect_VKey_VolumeUp: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_VolumeUp
Aspect_VKey_W: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_W
Aspect_VKey_X: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_X
Aspect_VKey_Y: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Y
Aspect_VKey_Z: OCP.Aspect.Aspect_VKeyBasic # value = Aspect_VKeyBasic.Aspect_VKey_Z
Aspect_WOL_MEDIUM: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_MEDIUM
Aspect_WOL_THICK: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_THICK
Aspect_WOL_THIN: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_THIN
Aspect_WOL_USERDEFINED: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_USERDEFINED
Aspect_WOL_VERYTHICK: OCP.Aspect.Aspect_WidthOfLine # value = Aspect_WidthOfLine.Aspect_WOL_VERYTHICK
Aspect_XA_DELETE_WINDOW: OCP.Aspect.Aspect_XAtom # value = Aspect_XAtom.Aspect_XA_DELETE_WINDOW
