import OCP.Aspect
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.WNT
import OCP.Quantity
import OCP.NCollection
import io
import Aspect_XRSession
import OCP.Graphic3d
import OCP.gp
import OCP.Standard
import OCP.Image
import OCP.TCollection
__all__  = [
"Aspect_AspectFillAreaDefinitionError",
"Aspect_AspectLineDefinitionError",
"Aspect_AspectMarkerDefinitionError",
"Aspect_Background",
"Aspect_Grid",
"Aspect_ColorSpace",
"Aspect_DisplayConnection",
"Aspect_DisplayConnectionDefinitionError",
"Aspect_Eye",
"Aspect_FillMethod",
"Aspect_GenId",
"Aspect_GradientBackground",
"Aspect_GradientFillMethod",
"Aspect_GraphicDeviceDefinitionError",
"Aspect_GraphicsLibrary",
"Aspect_CircularGrid",
"Aspect_GridDrawMode",
"Aspect_GridType",
"Aspect_HatchStyle",
"Aspect_IdentDefinitionError",
"Aspect_InteriorStyle",
"Aspect_Window",
"Aspect_XRSession",
"Aspect_PolygonOffsetMode",
"Aspect_RectangularGrid",
"Aspect_ScrollDelta",
"Aspect_SequenceOfColor",
"Aspect_Touch",
"Aspect_TouchMap",
"Aspect_TrackedDevicePose",
"Aspect_TrackedDevicePoseArray",
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
"Aspect_WindowInputListener",
"Aspect_XAtom",
"Aspect_XRAction",
"Aspect_XRActionSet",
"Aspect_XRActionType",
"Aspect_XRAnalogActionData",
"Aspect_XRDigitalActionData",
"Aspect_XRGenericAction",
"Aspect_XRHapticActionData",
"Aspect_XRPoseActionData",
"Aspect_OpenVRSession",
"Aspect_XRTrackedDeviceRole",
"Aspect_VKey2Modifier",
"Aspect_ColorSpace_Linear",
"Aspect_ColorSpace_sRGB",
"Aspect_Eye_Left",
"Aspect_Eye_Right",
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
"Aspect_GradientFillMethod_Corner1",
"Aspect_GradientFillMethod_Corner2",
"Aspect_GradientFillMethod_Corner3",
"Aspect_GradientFillMethod_Corner4",
"Aspect_GradientFillMethod_Diagonal1",
"Aspect_GradientFillMethod_Diagonal2",
"Aspect_GradientFillMethod_Elliptical",
"Aspect_GradientFillMethod_Horizontal",
"Aspect_GradientFillMethod_None",
"Aspect_GradientFillMethod_Vertical",
"Aspect_GraphicsLibrary_OpenGL",
"Aspect_GraphicsLibrary_OpenGLES",
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
"Aspect_VKey_ViewAxoLeftProj",
"Aspect_VKey_ViewAxoRightProj",
"Aspect_VKey_ViewBack",
"Aspect_VKey_ViewBottom",
"Aspect_VKey_ViewFitAll",
"Aspect_VKey_ViewFront",
"Aspect_VKey_ViewLeft",
"Aspect_VKey_ViewRight",
"Aspect_VKey_ViewRoll90CCW",
"Aspect_VKey_ViewRoll90CW",
"Aspect_VKey_ViewSwitchRotate",
"Aspect_VKey_ViewTop",
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
"Aspect_XA_DELETE_WINDOW",
"Aspect_XRActionType_InputAnalog",
"Aspect_XRActionType_InputDigital",
"Aspect_XRActionType_InputPose",
"Aspect_XRActionType_InputSkeletal",
"Aspect_XRActionType_OutputHaptic",
"Aspect_XRGenericAction_InputAppMenu",
"Aspect_XRGenericAction_InputGripClick",
"Aspect_XRGenericAction_InputPoseBase",
"Aspect_XRGenericAction_InputPoseFingerTip",
"Aspect_XRGenericAction_InputPoseFront",
"Aspect_XRGenericAction_InputPoseHandGrip",
"Aspect_XRGenericAction_InputSysMenu",
"Aspect_XRGenericAction_InputThumbstickClick",
"Aspect_XRGenericAction_InputThumbstickPosition",
"Aspect_XRGenericAction_InputThumbstickTouch",
"Aspect_XRGenericAction_InputTrackPadClick",
"Aspect_XRGenericAction_InputTrackPadPosition",
"Aspect_XRGenericAction_InputTrackPadTouch",
"Aspect_XRGenericAction_InputTriggerClick",
"Aspect_XRGenericAction_InputTriggerPull",
"Aspect_XRGenericAction_IsHeadsetOn",
"Aspect_XRGenericAction_NB",
"Aspect_XRGenericAction_OutputHaptic",
"Aspect_XRTrackedDeviceRole_Head",
"Aspect_XRTrackedDeviceRole_LeftHand",
"Aspect_XRTrackedDeviceRole_NB",
"Aspect_XRTrackedDeviceRole_Other",
"Aspect_XRTrackedDeviceRole_RightHand"
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
        __dict__: mappingproxy # value = mappingproxy({'__repr__': <slot wrapper '__repr__' of 'type' objects>, '__call__': <slot wrapper '__call__' of 'type' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'type' objects>, '__setattr__': <slot wrapper '__setattr__' of 'type' objects>, '__delattr__': <slot wrapper '__delattr__' of 'type' objects>, '__init__': <slot wrapper '__init__' of 'type' objects>, '__new__': <built-in method __new__ of type object at 0x00007FFF4287BC90>, 'mro': <method 'mro' of 'type' objects>, '__subclasses__': <method '__subclasses__' of 'type' objects>, '__prepare__': <method '__prepare__' of 'type' objects>, '__instancecheck__': <method '__instancecheck__' of 'type' objects>, '__subclasscheck__': <method '__subclasscheck__' of 'type' objects>, '__dir__': <method '__dir__' of 'type' objects>, '__sizeof__': <method '__sizeof__' of 'type' objects>, '__basicsize__': <member '__basicsize__' of 'type' objects>, '__itemsize__': <member '__itemsize__' of 'type' objects>, '__flags__': <member '__flags__' of 'type' objects>, '__weakrefoffset__': <member '__weakrefoffset__' of 'type' objects>, '__base__': <member '__base__' of 'type' objects>, '__dictoffset__': <member '__dictoffset__' of 'type' objects>, '__mro__': <member '__mro__' of 'type' objects>, '__name__': <attribute '__name__' of 'type' objects>, '__qualname__': <attribute '__qualname__' of 'type' objects>, '__bases__': <attribute '__bases__' of 'type' objects>, '__module__': <attribute '__module__' of 'type' objects>, '__abstractmethods__': <attribute '__abstractmethods__' of 'type' objects>, '__dict__': <attribute '__dict__' of 'type' objects>, '__doc__': <attribute '__doc__' of 'type' objects>, '__text_signature__': <attribute '__text_signature__' of 'type' objects>})
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
class Aspect_ColorSpace():
    """
    Texture color spaces accepted by XR composer.

    Members:

      Aspect_ColorSpace_sRGB

      Aspect_ColorSpace_Linear
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
    Aspect_ColorSpace_Linear: OCP.Aspect.Aspect_ColorSpace # value = <Aspect_ColorSpace.Aspect_ColorSpace_Linear: 1>
    Aspect_ColorSpace_sRGB: OCP.Aspect.Aspect_ColorSpace # value = <Aspect_ColorSpace.Aspect_ColorSpace_sRGB: 0>
    __entries: dict # value = {'Aspect_ColorSpace_sRGB': (<Aspect_ColorSpace.Aspect_ColorSpace_sRGB: 0>, None), 'Aspect_ColorSpace_Linear': (<Aspect_ColorSpace.Aspect_ColorSpace_Linear: 1>, None)}
    __members__: dict # value = {'Aspect_ColorSpace_sRGB': <Aspect_ColorSpace.Aspect_ColorSpace_sRGB: 0>, 'Aspect_ColorSpace_Linear': <Aspect_ColorSpace.Aspect_ColorSpace_Linear: 1>}
    pass
class Aspect_DisplayConnection(OCP.Standard.Standard_Transient):
    """
    This class creates and provides connection with X server. Raises exception if can not connect to X server. On Windows and Mac OS X (in case when Cocoa used) platforms this class does nothing. WARRNING: Do not close display connection manually!This class creates and provides connection with X server. Raises exception if can not connect to X server. On Windows and Mac OS X (in case when Cocoa used) platforms this class does nothing. WARRNING: Do not close display connection manually!
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
    def GetDefaultFBConfig(self) -> __GLXFBConfigRec: 
        """
        Returns native Window FB config (GLXFBConfig on Xlib)
        """
    def GetDefaultVisualInfo(self) -> Aspect_XVisualInfo: 
        """
        Return default window visual or NULL when undefined.
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
    def IsOwnDisplay(self) -> bool: 
        """
        Returns TRUE if X Display has been allocated by this class
        """
    def SetDefaultVisualInfo(self,theVisual : Aspect_XVisualInfo,theFBConfig : __GLXFBConfigRec) -> None: 
        """
        Set default window visual; the visual will be deallocated using XFree().
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
class Aspect_Eye():
    """
    Camera eye index within stereoscopic pair.

    Members:

      Aspect_Eye_Left

      Aspect_Eye_Right
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
    Aspect_Eye_Left: OCP.Aspect.Aspect_Eye # value = <Aspect_Eye.Aspect_Eye_Left: 0>
    Aspect_Eye_Right: OCP.Aspect.Aspect_Eye # value = <Aspect_Eye.Aspect_Eye_Right: 1>
    __entries: dict # value = {'Aspect_Eye_Left': (<Aspect_Eye.Aspect_Eye_Left: 0>, None), 'Aspect_Eye_Right': (<Aspect_Eye.Aspect_Eye_Right: 1>, None)}
    __members__: dict # value = {'Aspect_Eye_Left': <Aspect_Eye.Aspect_Eye_Left: 0>, 'Aspect_Eye_Right': <Aspect_Eye.Aspect_Eye_Right: 1>}
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
    Aspect_FM_CENTERED: OCP.Aspect.Aspect_FillMethod # value = <Aspect_FillMethod.Aspect_FM_CENTERED: 1>
    Aspect_FM_NONE: OCP.Aspect.Aspect_FillMethod # value = <Aspect_FillMethod.Aspect_FM_NONE: 0>
    Aspect_FM_STRETCH: OCP.Aspect.Aspect_FillMethod # value = <Aspect_FillMethod.Aspect_FM_STRETCH: 3>
    Aspect_FM_TILED: OCP.Aspect.Aspect_FillMethod # value = <Aspect_FillMethod.Aspect_FM_TILED: 2>
    __entries: dict # value = {'Aspect_FM_NONE': (<Aspect_FillMethod.Aspect_FM_NONE: 0>, None), 'Aspect_FM_CENTERED': (<Aspect_FillMethod.Aspect_FM_CENTERED: 1>, None), 'Aspect_FM_TILED': (<Aspect_FillMethod.Aspect_FM_TILED: 2>, None), 'Aspect_FM_STRETCH': (<Aspect_FillMethod.Aspect_FM_STRETCH: 3>, None)}
    __members__: dict # value = {'Aspect_FM_NONE': <Aspect_FillMethod.Aspect_FM_NONE: 0>, 'Aspect_FM_CENTERED': <Aspect_FillMethod.Aspect_FM_CENTERED: 1>, 'Aspect_FM_TILED': <Aspect_FillMethod.Aspect_FM_TILED: 2>, 'Aspect_FM_STRETCH': <Aspect_FillMethod.Aspect_FM_STRETCH: 3>}
    pass
class Aspect_GenId():
    """
    This class permits the creation and control of integer identifiers.
    """
    def Available(self) -> int: 
        """
        Returns the number of available identifiers.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def Colors(self,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns colours of the window gradient background.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def SetColor(self,AColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the colour of the window background <me>.
        """
    def SetColors(self,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color,theMethod : Aspect_GradientFillMethod=Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal) -> None: 
        """
        Modifies the colours of the window gradient background.
        """
    @overload
    def __init__(self,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color,theMethod : Aspect_GradientFillMethod=Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Aspect_GradientFillMethod():
    """
    Defines the fill methods to write gradient background in a window.

    Members:

      Aspect_GradientFillMethod_None

      Aspect_GradientFillMethod_Horizontal

      Aspect_GradientFillMethod_Vertical

      Aspect_GradientFillMethod_Diagonal1

      Aspect_GradientFillMethod_Diagonal2

      Aspect_GradientFillMethod_Corner1

      Aspect_GradientFillMethod_Corner2

      Aspect_GradientFillMethod_Corner3

      Aspect_GradientFillMethod_Corner4

      Aspect_GradientFillMethod_Elliptical

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
    Aspect_GFM_CORNER1: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner1: 5>
    Aspect_GFM_CORNER2: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner2: 6>
    Aspect_GFM_CORNER3: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner3: 7>
    Aspect_GFM_CORNER4: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner4: 8>
    Aspect_GFM_DIAG1: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal1: 3>
    Aspect_GFM_DIAG2: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal2: 4>
    Aspect_GFM_HOR: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal: 1>
    Aspect_GFM_NONE: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_None: 0>
    Aspect_GFM_VER: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Vertical: 2>
    Aspect_GradientFillMethod_Corner1: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner1: 5>
    Aspect_GradientFillMethod_Corner2: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner2: 6>
    Aspect_GradientFillMethod_Corner3: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner3: 7>
    Aspect_GradientFillMethod_Corner4: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner4: 8>
    Aspect_GradientFillMethod_Diagonal1: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal1: 3>
    Aspect_GradientFillMethod_Diagonal2: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal2: 4>
    Aspect_GradientFillMethod_Elliptical: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Elliptical: 9>
    Aspect_GradientFillMethod_Horizontal: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal: 1>
    Aspect_GradientFillMethod_None: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_None: 0>
    Aspect_GradientFillMethod_Vertical: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Vertical: 2>
    __entries: dict # value = {'Aspect_GradientFillMethod_None': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_None: 0>, None), 'Aspect_GradientFillMethod_Horizontal': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal: 1>, None), 'Aspect_GradientFillMethod_Vertical': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Vertical: 2>, None), 'Aspect_GradientFillMethod_Diagonal1': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal1: 3>, None), 'Aspect_GradientFillMethod_Diagonal2': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal2: 4>, None), 'Aspect_GradientFillMethod_Corner1': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner1: 5>, None), 'Aspect_GradientFillMethod_Corner2': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner2: 6>, None), 'Aspect_GradientFillMethod_Corner3': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner3: 7>, None), 'Aspect_GradientFillMethod_Corner4': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner4: 8>, None), 'Aspect_GradientFillMethod_Elliptical': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Elliptical: 9>, None), 'Aspect_GFM_NONE': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_None: 0>, None), 'Aspect_GFM_HOR': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal: 1>, None), 'Aspect_GFM_VER': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Vertical: 2>, None), 'Aspect_GFM_DIAG1': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal1: 3>, None), 'Aspect_GFM_DIAG2': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal2: 4>, None), 'Aspect_GFM_CORNER1': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner1: 5>, None), 'Aspect_GFM_CORNER2': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner2: 6>, None), 'Aspect_GFM_CORNER3': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner3: 7>, None), 'Aspect_GFM_CORNER4': (<Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner4: 8>, None)}
    __members__: dict # value = {'Aspect_GradientFillMethod_None': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_None: 0>, 'Aspect_GradientFillMethod_Horizontal': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal: 1>, 'Aspect_GradientFillMethod_Vertical': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Vertical: 2>, 'Aspect_GradientFillMethod_Diagonal1': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal1: 3>, 'Aspect_GradientFillMethod_Diagonal2': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal2: 4>, 'Aspect_GradientFillMethod_Corner1': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner1: 5>, 'Aspect_GradientFillMethod_Corner2': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner2: 6>, 'Aspect_GradientFillMethod_Corner3': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner3: 7>, 'Aspect_GradientFillMethod_Corner4': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner4: 8>, 'Aspect_GradientFillMethod_Elliptical': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Elliptical: 9>, 'Aspect_GFM_NONE': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_None: 0>, 'Aspect_GFM_HOR': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal: 1>, 'Aspect_GFM_VER': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Vertical: 2>, 'Aspect_GFM_DIAG1': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal1: 3>, 'Aspect_GFM_DIAG2': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal2: 4>, 'Aspect_GFM_CORNER1': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner1: 5>, 'Aspect_GFM_CORNER2': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner2: 6>, 'Aspect_GFM_CORNER3': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner3: 7>, 'Aspect_GFM_CORNER4': <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner4: 8>}
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
class Aspect_GraphicsLibrary():
    """
    Graphics API enumeration.

    Members:

      Aspect_GraphicsLibrary_OpenGL

      Aspect_GraphicsLibrary_OpenGLES
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
    Aspect_GraphicsLibrary_OpenGL: OCP.Aspect.Aspect_GraphicsLibrary # value = <Aspect_GraphicsLibrary.Aspect_GraphicsLibrary_OpenGL: 0>
    Aspect_GraphicsLibrary_OpenGLES: OCP.Aspect.Aspect_GraphicsLibrary # value = <Aspect_GraphicsLibrary.Aspect_GraphicsLibrary_OpenGLES: 1>
    __entries: dict # value = {'Aspect_GraphicsLibrary_OpenGL': (<Aspect_GraphicsLibrary.Aspect_GraphicsLibrary_OpenGL: 0>, None), 'Aspect_GraphicsLibrary_OpenGLES': (<Aspect_GraphicsLibrary.Aspect_GraphicsLibrary_OpenGLES: 1>, None)}
    __members__: dict # value = {'Aspect_GraphicsLibrary_OpenGL': <Aspect_GraphicsLibrary.Aspect_GraphicsLibrary_OpenGL: 0>, 'Aspect_GraphicsLibrary_OpenGLES': <Aspect_GraphicsLibrary.Aspect_GraphicsLibrary_OpenGLES: 1>}
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    Aspect_GDM_Lines: OCP.Aspect.Aspect_GridDrawMode # value = <Aspect_GridDrawMode.Aspect_GDM_Lines: 0>
    Aspect_GDM_None: OCP.Aspect.Aspect_GridDrawMode # value = <Aspect_GridDrawMode.Aspect_GDM_None: 2>
    Aspect_GDM_Points: OCP.Aspect.Aspect_GridDrawMode # value = <Aspect_GridDrawMode.Aspect_GDM_Points: 1>
    __entries: dict # value = {'Aspect_GDM_Lines': (<Aspect_GridDrawMode.Aspect_GDM_Lines: 0>, None), 'Aspect_GDM_Points': (<Aspect_GridDrawMode.Aspect_GDM_Points: 1>, None), 'Aspect_GDM_None': (<Aspect_GridDrawMode.Aspect_GDM_None: 2>, None)}
    __members__: dict # value = {'Aspect_GDM_Lines': <Aspect_GridDrawMode.Aspect_GDM_Lines: 0>, 'Aspect_GDM_Points': <Aspect_GridDrawMode.Aspect_GDM_Points: 1>, 'Aspect_GDM_None': <Aspect_GridDrawMode.Aspect_GDM_None: 2>}
    pass
class Aspect_GridType():
    """
    Defines the grid type : Rectangular or Circular.

    Members:

      Aspect_GT_Rectangular

      Aspect_GT_Circular
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
    Aspect_GT_Circular: OCP.Aspect.Aspect_GridType # value = <Aspect_GridType.Aspect_GT_Circular: 1>
    Aspect_GT_Rectangular: OCP.Aspect.Aspect_GridType # value = <Aspect_GridType.Aspect_GT_Rectangular: 0>
    __entries: dict # value = {'Aspect_GT_Rectangular': (<Aspect_GridType.Aspect_GT_Rectangular: 0>, None), 'Aspect_GT_Circular': (<Aspect_GridType.Aspect_GT_Circular: 1>, None)}
    __members__: dict # value = {'Aspect_GT_Rectangular': <Aspect_GridType.Aspect_GT_Rectangular: 0>, 'Aspect_GT_Circular': <Aspect_GridType.Aspect_GT_Circular: 1>}
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
    Aspect_HS_DIAGONAL_135: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_DIAGONAL_135: 6>
    Aspect_HS_DIAGONAL_135_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_DIAGONAL_135_WIDE: 10>
    Aspect_HS_DIAGONAL_45: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_DIAGONAL_45: 5>
    Aspect_HS_DIAGONAL_45_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_DIAGONAL_45_WIDE: 9>
    Aspect_HS_GRID: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_GRID: 3>
    Aspect_HS_GRID_DIAGONAL: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL: 1>
    Aspect_HS_GRID_DIAGONAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL_WIDE: 2>
    Aspect_HS_GRID_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_GRID_WIDE: 4>
    Aspect_HS_HORIZONTAL: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_HORIZONTAL: 7>
    Aspect_HS_HORIZONTAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_HORIZONTAL_WIDE: 11>
    Aspect_HS_NB: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_NB: 13>
    Aspect_HS_SOLID: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_SOLID: 0>
    Aspect_HS_VERTICAL: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_VERTICAL: 8>
    Aspect_HS_VERTICAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_VERTICAL_WIDE: 12>
    __entries: dict # value = {'Aspect_HS_SOLID': (<Aspect_HatchStyle.Aspect_HS_SOLID: 0>, None), 'Aspect_HS_HORIZONTAL': (<Aspect_HatchStyle.Aspect_HS_HORIZONTAL: 7>, None), 'Aspect_HS_HORIZONTAL_WIDE': (<Aspect_HatchStyle.Aspect_HS_HORIZONTAL_WIDE: 11>, None), 'Aspect_HS_VERTICAL': (<Aspect_HatchStyle.Aspect_HS_VERTICAL: 8>, None), 'Aspect_HS_VERTICAL_WIDE': (<Aspect_HatchStyle.Aspect_HS_VERTICAL_WIDE: 12>, None), 'Aspect_HS_DIAGONAL_45': (<Aspect_HatchStyle.Aspect_HS_DIAGONAL_45: 5>, None), 'Aspect_HS_DIAGONAL_45_WIDE': (<Aspect_HatchStyle.Aspect_HS_DIAGONAL_45_WIDE: 9>, None), 'Aspect_HS_DIAGONAL_135': (<Aspect_HatchStyle.Aspect_HS_DIAGONAL_135: 6>, None), 'Aspect_HS_DIAGONAL_135_WIDE': (<Aspect_HatchStyle.Aspect_HS_DIAGONAL_135_WIDE: 10>, None), 'Aspect_HS_GRID': (<Aspect_HatchStyle.Aspect_HS_GRID: 3>, None), 'Aspect_HS_GRID_WIDE': (<Aspect_HatchStyle.Aspect_HS_GRID_WIDE: 4>, None), 'Aspect_HS_GRID_DIAGONAL': (<Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL: 1>, None), 'Aspect_HS_GRID_DIAGONAL_WIDE': (<Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL_WIDE: 2>, None), 'Aspect_HS_NB': (<Aspect_HatchStyle.Aspect_HS_NB: 13>, None)}
    __members__: dict # value = {'Aspect_HS_SOLID': <Aspect_HatchStyle.Aspect_HS_SOLID: 0>, 'Aspect_HS_HORIZONTAL': <Aspect_HatchStyle.Aspect_HS_HORIZONTAL: 7>, 'Aspect_HS_HORIZONTAL_WIDE': <Aspect_HatchStyle.Aspect_HS_HORIZONTAL_WIDE: 11>, 'Aspect_HS_VERTICAL': <Aspect_HatchStyle.Aspect_HS_VERTICAL: 8>, 'Aspect_HS_VERTICAL_WIDE': <Aspect_HatchStyle.Aspect_HS_VERTICAL_WIDE: 12>, 'Aspect_HS_DIAGONAL_45': <Aspect_HatchStyle.Aspect_HS_DIAGONAL_45: 5>, 'Aspect_HS_DIAGONAL_45_WIDE': <Aspect_HatchStyle.Aspect_HS_DIAGONAL_45_WIDE: 9>, 'Aspect_HS_DIAGONAL_135': <Aspect_HatchStyle.Aspect_HS_DIAGONAL_135: 6>, 'Aspect_HS_DIAGONAL_135_WIDE': <Aspect_HatchStyle.Aspect_HS_DIAGONAL_135_WIDE: 10>, 'Aspect_HS_GRID': <Aspect_HatchStyle.Aspect_HS_GRID: 3>, 'Aspect_HS_GRID_WIDE': <Aspect_HatchStyle.Aspect_HS_GRID_WIDE: 4>, 'Aspect_HS_GRID_DIAGONAL': <Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL: 1>, 'Aspect_HS_GRID_DIAGONAL_WIDE': <Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL_WIDE: 2>, 'Aspect_HS_NB': <Aspect_HatchStyle.Aspect_HS_NB: 13>}
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
    Aspect_IS_EMPTY: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_EMPTY: -1>
    Aspect_IS_HATCH: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_HATCH: 1>
    Aspect_IS_HIDDENLINE: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_HIDDENLINE: 2>
    Aspect_IS_HOLLOW: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_EMPTY: -1>
    Aspect_IS_POINT: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_POINT: 3>
    Aspect_IS_SOLID: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_SOLID: 0>
    __entries: dict # value = {'Aspect_IS_EMPTY': (<Aspect_InteriorStyle.Aspect_IS_EMPTY: -1>, None), 'Aspect_IS_SOLID': (<Aspect_InteriorStyle.Aspect_IS_SOLID: 0>, None), 'Aspect_IS_HATCH': (<Aspect_InteriorStyle.Aspect_IS_HATCH: 1>, None), 'Aspect_IS_HIDDENLINE': (<Aspect_InteriorStyle.Aspect_IS_HIDDENLINE: 2>, None), 'Aspect_IS_POINT': (<Aspect_InteriorStyle.Aspect_IS_POINT: 3>, None), 'Aspect_IS_HOLLOW': (<Aspect_InteriorStyle.Aspect_IS_EMPTY: -1>, None)}
    __members__: dict # value = {'Aspect_IS_EMPTY': <Aspect_InteriorStyle.Aspect_IS_EMPTY: -1>, 'Aspect_IS_SOLID': <Aspect_InteriorStyle.Aspect_IS_SOLID: 0>, 'Aspect_IS_HATCH': <Aspect_InteriorStyle.Aspect_IS_HATCH: 1>, 'Aspect_IS_HIDDENLINE': <Aspect_InteriorStyle.Aspect_IS_HIDDENLINE: 2>, 'Aspect_IS_POINT': <Aspect_InteriorStyle.Aspect_IS_POINT: 3>, 'Aspect_IS_HOLLOW': <Aspect_InteriorStyle.Aspect_IS_EMPTY: -1>}
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
    def ConvertPointFromBacking(self,thePnt : OCP.Graphic3d.Graphic3d_Vec2d) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        Convert point from backing store units to logical units.
        """
    def ConvertPointToBacking(self,thePnt : OCP.Graphic3d.Graphic3d_Vec2d) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        Convert point from logical units into backing store units.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DevicePixelRatio(self) -> float: 
        """
        Return device pixel ratio (logical to backing store scale factor).
        """
    def DisplayConnection(self) -> Aspect_DisplayConnection: 
        """
        Returns connection to Display or NULL.
        """
    def DoMapping(self) -> bool: 
        """
        Apply the mapping change to the window <me>. and returns TRUE if the window is mapped at screen.
        """
    def DoResize(self) -> Aspect_TypeOfResize: 
        """
        Apply the resizing to the window <me>.
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
    def NativeHandle(self) -> capsule: 
        """
        Returns native Window handle (HWND on Windows, Window with Xlib, and so on)
        """
    def NativeParentHandle(self) -> capsule: 
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
    def SetBackground(self,ABackground : Aspect_GradientBackground) -> None: ...
    @overload
    def SetBackground(self,ABack : Aspect_Background) -> None: ...
    @overload
    def SetBackground(self,theFirstColor : OCP.Quantity.Quantity_Color,theSecondColor : OCP.Quantity.Quantity_Color,theFillMethod : Aspect_GradientFillMethod) -> None: ...
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
class Aspect_XRSession(OCP.Standard.Standard_Transient):
    """
    Extended Reality (XR) Session interface.
    """
    class InfoString_e():
        pass
    class TrackingUniverseOrigin_e():
        pass
    def AbortHapticVibrationAction(self,theAction : Aspect_XRAction) -> None: 
        """
        Abort vibration.
        """
    def Aspect(self) -> float: 
        """
        Return aspect ratio.
        """
    def Close(self) -> None: 
        """
        Release session.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisplayFrequency(self) -> float: 
        """
        Return display frequency or 0 if unknown.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EyeToHeadTransform(self,theEye : Aspect_Eye) -> OCP.Graphic3d.Graphic3d_Mat4d: 
        """
        Return transformation from eye to head.
        """
    def FieldOfView(self) -> float: 
        """
        Return field of view.
        """
    def GenericAction(self,theDevice : Aspect_XRTrackedDeviceRole,theAction : Aspect_XRGenericAction) -> Aspect_XRAction: 
        """
        Return generic action for specific hand or NULL if undefined.
        """
    def GetAnalogActionData(self,theAction : Aspect_XRAction) -> Aspect_XRAnalogActionData: 
        """
        Fetch data for digital input action (like axis).
        """
    def GetDigitalActionData(self,theAction : Aspect_XRAction) -> Aspect_XRDigitalActionData: 
        """
        Fetch data for digital input action (like button).
        """
    def GetPoseActionDataForNextFrame(self,theAction : Aspect_XRAction) -> Aspect_XRPoseActionData: 
        """
        Fetch data for pose input action (like fingertip position). The returned values will match the values returned by the last call to WaitPoses().
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetString(self,theInfo : Aspect_XRSession.InfoString_e) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Query information.
        """
    def HasProjectionFrustums(self) -> bool: 
        """
        Return FALSE if projection frustums are unsupported and general 4x4 projection matrix should be fetched instead
        """
    def HasTrackedPose(self,theDevice : int) -> bool: 
        """
        Return TRUE if device orientation is defined.
        """
    def HeadPose(self) -> OCP.gp.gp_Trsf: 
        """
        Return head orientation in right-handed system: +y is up +x is to the right -z is forward Distance unit is meters by default (
        """
    def HeadToEyeTransform(self,theEye : Aspect_Eye) -> OCP.Graphic3d.Graphic3d_Mat4d: 
        """
        Return transformation from head to eye.
        """
    def IOD(self) -> float: 
        """
        Return Intra-ocular Distance (IOD); also known as Interpupillary Distance (IPD). Defined in meters by default (
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
    def IsOpen(self) -> bool: 
        """
        Return TRUE if session is opened.
        """
    def LeftHandPose(self) -> OCP.gp.gp_Trsf: 
        """
        Return left hand orientation.
        """
    @overload
    def LoadRenderModel(self,theDevice : int,theTexture : OCP.Image.Image_Texture) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: 
        """
        Load model for displaying device.

        Load model for displaying device.
        """
    @overload
    def LoadRenderModel(self,theDevice : int,theToApplyUnitFactor : bool,theTexture : OCP.Image.Image_Texture) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: ...
    def NamedTrackedDevice(self,theDevice : Aspect_XRTrackedDeviceRole) -> int: 
        """
        Return index of tracked device of known role, or -1 if undefined.
        """
    def Open(self) -> bool: 
        """
        Initialize session.
        """
    def ProcessEvents(self) -> None: 
        """
        Receive XR events.
        """
    def ProjectionFrustum(self,theEye : Aspect_Eye) -> Any: 
        """
        Return projection frustum.
        """
    def ProjectionMatrix(self,theEye : Aspect_Eye,theZNear : float,theZFar : float) -> OCP.Graphic3d.Graphic3d_Mat4d: 
        """
        Return projection matrix.
        """
    def RecommendedViewport(self) -> OCP.Graphic3d.Graphic3d_Vec2i: 
        """
        Return recommended viewport Width x Height for rendering into VR.
        """
    def RightHandPose(self) -> OCP.gp.gp_Trsf: 
        """
        Return right hand orientation.
        """
    def SetTrackingOrigin(self,theOrigin : Aspect_XRSession.TrackingUniverseOrigin_e) -> None: 
        """
        Set tracking origin.
        """
    def SetUnitFactor(self,theFactor : float) -> None: 
        """
        Set unit scale factor.
        """
    def SubmitEye(self,theTexture : capsule,theGraphicsLib : Aspect_GraphicsLibrary,theColorSpace : Aspect_ColorSpace,theEye : Aspect_Eye) -> bool: 
        """
        Submit texture eye to XR Composer.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TrackedPoses(self) -> Aspect_TrackedDevicePoseArray: 
        """
        Return number of tracked poses array.
        """
    def TrackingOrigin(self) -> Aspect_XRSession.TrackingUniverseOrigin_e: 
        """
        Return tracking origin.
        """
    def TriggerHapticVibrationAction(self,theAction : Aspect_XRAction,theParams : Aspect_XRHapticActionData) -> None: 
        """
        Trigger vibration.
        """
    def UnitFactor(self) -> float: 
        """
        Return unit scale factor defined as scale factor for m (meters); 1.0 by default.
        """
    def WaitPoses(self) -> bool: 
        """
        Fetch actual poses of tracked devices.
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
    InfoString_Device: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_Device: 1>
    InfoString_SerialNumber: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_SerialNumber: 3>
    InfoString_Tracker: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_Tracker: 2>
    InfoString_Vendor: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_Vendor: 0>
    TrackingUniverseOrigin_Seated: OCP.Aspect.TrackingUniverseOrigin_e # value = <TrackingUniverseOrigin_e.TrackingUniverseOrigin_Seated: 0>
    TrackingUniverseOrigin_Standing: OCP.Aspect.TrackingUniverseOrigin_e # value = <TrackingUniverseOrigin_e.TrackingUniverseOrigin_Standing: 1>
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
    Aspect_POM_All: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_All: 7>
    Aspect_POM_Fill: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Fill: 1>
    Aspect_POM_Line: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Line: 2>
    Aspect_POM_Mask: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Mask: 15>
    Aspect_POM_None: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_None: 8>
    Aspect_POM_Off: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Off: 0>
    Aspect_POM_Point: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Point: 4>
    __entries: dict # value = {'Aspect_POM_Off': (<Aspect_PolygonOffsetMode.Aspect_POM_Off: 0>, None), 'Aspect_POM_Fill': (<Aspect_PolygonOffsetMode.Aspect_POM_Fill: 1>, None), 'Aspect_POM_Line': (<Aspect_PolygonOffsetMode.Aspect_POM_Line: 2>, None), 'Aspect_POM_Point': (<Aspect_PolygonOffsetMode.Aspect_POM_Point: 4>, None), 'Aspect_POM_All': (<Aspect_PolygonOffsetMode.Aspect_POM_All: 7>, None), 'Aspect_POM_None': (<Aspect_PolygonOffsetMode.Aspect_POM_None: 8>, None), 'Aspect_POM_Mask': (<Aspect_PolygonOffsetMode.Aspect_POM_Mask: 15>, None)}
    __members__: dict # value = {'Aspect_POM_Off': <Aspect_PolygonOffsetMode.Aspect_POM_Off: 0>, 'Aspect_POM_Fill': <Aspect_PolygonOffsetMode.Aspect_POM_Fill: 1>, 'Aspect_POM_Line': <Aspect_PolygonOffsetMode.Aspect_POM_Line: 2>, 'Aspect_POM_Point': <Aspect_PolygonOffsetMode.Aspect_POM_Point: 4>, 'Aspect_POM_All': <Aspect_PolygonOffsetMode.Aspect_POM_All: 7>, 'Aspect_POM_None': <Aspect_PolygonOffsetMode.Aspect_POM_None: 8>, 'Aspect_POM_Mask': <Aspect_PolygonOffsetMode.Aspect_POM_Mask: 15>}
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
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
    def __init__(self,thePnt : OCP.Graphic3d.Graphic3d_Vec2i,theValue : float,theFlags : int=0) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
    def InsertAfter(self,theIndex : int,theSeq : Aspect_SequenceOfColor) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Quantity.Quantity_Color) -> None: ...
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
    def Prepend(self,theItem : OCP.Quantity.Quantity_Color) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Aspect_SequenceOfColor) -> None: ...
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
    def __init__(self,theOther : Aspect_SequenceOfColor) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
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
    def __init__(self,thePnt : OCP.Graphic3d.Graphic3d_Vec2d,theIsPreciseDevice : bool) -> None: ...
    @overload
    def __init__(self,theX : float,theY : float,theIsPreciseDevice : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
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
    def FindFromKey(self,theKey1 : int) -> Aspect_Touch: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : int,theValue : Aspect_Touch) -> bool: ...
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
    def Statistics(self,S : io.BytesIO) -> None: 
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : Aspect_TouchMap) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Aspect_TrackedDevicePose():
    """
    Describes a single pose for a tracked object (for XR).
    """
    def __init__(self) -> None: ...
    @property
    def AngularVelocity(self) -> OCP.gp.gp_Vec:
        """
        :type: OCP.gp.gp_Vec
        """
    @AngularVelocity.setter
    def AngularVelocity(self, arg0: OCP.gp.gp_Vec) -> None:
        pass
    @property
    def Orientation(self) -> OCP.gp.gp_Trsf:
        """
        :type: OCP.gp.gp_Trsf
        """
    @Orientation.setter
    def Orientation(self, arg0: OCP.gp.gp_Trsf) -> None:
        pass
    @property
    def Velocity(self) -> OCP.gp.gp_Vec:
        """
        :type: OCP.gp.gp_Vec
        """
    @Velocity.setter
    def Velocity(self, arg0: OCP.gp.gp_Vec) -> None:
        pass
    pass
class Aspect_TrackedDevicePoseArray():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Aspect_TrackedDevicePoseArray) -> Aspect_TrackedDevicePoseArray: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Aspect_TrackedDevicePose: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Aspect_TrackedDevicePose: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Aspect_TrackedDevicePose: 
        """
        Variable value access
        """
    def First(self) -> Aspect_TrackedDevicePose: 
        """
        Returns first element
        """
    def Init(self,theValue : Aspect_TrackedDevicePose) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> Aspect_TrackedDevicePose: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : Aspect_TrackedDevicePoseArray) -> Aspect_TrackedDevicePoseArray: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Aspect_TrackedDevicePose) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> Aspect_TrackedDevicePose: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : Aspect_TrackedDevicePose,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Aspect_TrackedDevicePoseArray) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Aspect_TypeOfColorScaleData():
    """
    Defines the using type of colors and labels

    Members:

      Aspect_TOCSD_AUTO

      Aspect_TOCSD_USER
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
    Aspect_TOCSD_AUTO: OCP.Aspect.Aspect_TypeOfColorScaleData # value = <Aspect_TypeOfColorScaleData.Aspect_TOCSD_AUTO: 0>
    Aspect_TOCSD_USER: OCP.Aspect.Aspect_TypeOfColorScaleData # value = <Aspect_TypeOfColorScaleData.Aspect_TOCSD_USER: 1>
    __entries: dict # value = {'Aspect_TOCSD_AUTO': (<Aspect_TypeOfColorScaleData.Aspect_TOCSD_AUTO: 0>, None), 'Aspect_TOCSD_USER': (<Aspect_TypeOfColorScaleData.Aspect_TOCSD_USER: 1>, None)}
    __members__: dict # value = {'Aspect_TOCSD_AUTO': <Aspect_TypeOfColorScaleData.Aspect_TOCSD_AUTO: 0>, 'Aspect_TOCSD_USER': <Aspect_TypeOfColorScaleData.Aspect_TOCSD_USER: 1>}
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
    Aspect_TOCSO_CENTER: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_CENTER: 3>
    Aspect_TOCSO_LEFT: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_LEFT: 1>
    Aspect_TOCSO_NONE: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_NONE: 0>
    Aspect_TOCSO_RIGHT: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_RIGHT: 2>
    __entries: dict # value = {'Aspect_TOCSO_NONE': (<Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_NONE: 0>, None), 'Aspect_TOCSO_LEFT': (<Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_LEFT: 1>, None), 'Aspect_TOCSO_RIGHT': (<Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_RIGHT: 2>, None), 'Aspect_TOCSO_CENTER': (<Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_CENTER: 3>, None)}
    __members__: dict # value = {'Aspect_TOCSO_NONE': <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_NONE: 0>, 'Aspect_TOCSO_LEFT': <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_LEFT: 1>, 'Aspect_TOCSO_RIGHT': <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_RIGHT: 2>, 'Aspect_TOCSO_CENTER': <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_CENTER: 3>}
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
    Aspect_TOCSP_CENTER: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_CENTER: 3>
    Aspect_TOCSP_LEFT: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_LEFT: 1>
    Aspect_TOCSP_NONE: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_NONE: 0>
    Aspect_TOCSP_RIGHT: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_RIGHT: 2>
    __entries: dict # value = {'Aspect_TOCSP_NONE': (<Aspect_TypeOfColorScalePosition.Aspect_TOCSP_NONE: 0>, None), 'Aspect_TOCSP_LEFT': (<Aspect_TypeOfColorScalePosition.Aspect_TOCSP_LEFT: 1>, None), 'Aspect_TOCSP_RIGHT': (<Aspect_TypeOfColorScalePosition.Aspect_TOCSP_RIGHT: 2>, None), 'Aspect_TOCSP_CENTER': (<Aspect_TypeOfColorScalePosition.Aspect_TOCSP_CENTER: 3>, None)}
    __members__: dict # value = {'Aspect_TOCSP_NONE': <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_NONE: 0>, 'Aspect_TOCSP_LEFT': <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_LEFT: 1>, 'Aspect_TOCSP_RIGHT': <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_RIGHT: 2>, 'Aspect_TOCSP_CENTER': <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_CENTER: 3>}
    pass
class Aspect_TypeOfDeflection():
    """
    Defines if the maximal chordial deflection used when drawing an object is absolute or relative to the size of the object.

    Members:

      Aspect_TOD_RELATIVE

      Aspect_TOD_ABSOLUTE
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
    Aspect_TOD_ABSOLUTE: OCP.Aspect.Aspect_TypeOfDeflection # value = <Aspect_TypeOfDeflection.Aspect_TOD_ABSOLUTE: 1>
    Aspect_TOD_RELATIVE: OCP.Aspect.Aspect_TypeOfDeflection # value = <Aspect_TypeOfDeflection.Aspect_TOD_RELATIVE: 0>
    __entries: dict # value = {'Aspect_TOD_RELATIVE': (<Aspect_TypeOfDeflection.Aspect_TOD_RELATIVE: 0>, None), 'Aspect_TOD_ABSOLUTE': (<Aspect_TypeOfDeflection.Aspect_TOD_ABSOLUTE: 1>, None)}
    __members__: dict # value = {'Aspect_TOD_RELATIVE': <Aspect_TypeOfDeflection.Aspect_TOD_RELATIVE: 0>, 'Aspect_TOD_ABSOLUTE': <Aspect_TypeOfDeflection.Aspect_TOD_ABSOLUTE: 1>}
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
    Aspect_TODT_BLEND: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_BLEND: 3>
    Aspect_TODT_DEKALE: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_DEKALE: 2>
    Aspect_TODT_DIMENSION: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_DIMENSION: 4>
    Aspect_TODT_NORMAL: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL: 0>
    Aspect_TODT_SHADOW: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_SHADOW: 5>
    Aspect_TODT_SUBTITLE: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_SUBTITLE: 1>
    __entries: dict # value = {'Aspect_TODT_NORMAL': (<Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL: 0>, None), 'Aspect_TODT_SUBTITLE': (<Aspect_TypeOfDisplayText.Aspect_TODT_SUBTITLE: 1>, None), 'Aspect_TODT_DEKALE': (<Aspect_TypeOfDisplayText.Aspect_TODT_DEKALE: 2>, None), 'Aspect_TODT_BLEND': (<Aspect_TypeOfDisplayText.Aspect_TODT_BLEND: 3>, None), 'Aspect_TODT_DIMENSION': (<Aspect_TypeOfDisplayText.Aspect_TODT_DIMENSION: 4>, None), 'Aspect_TODT_SHADOW': (<Aspect_TypeOfDisplayText.Aspect_TODT_SHADOW: 5>, None)}
    __members__: dict # value = {'Aspect_TODT_NORMAL': <Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL: 0>, 'Aspect_TODT_SUBTITLE': <Aspect_TypeOfDisplayText.Aspect_TODT_SUBTITLE: 1>, 'Aspect_TODT_DEKALE': <Aspect_TypeOfDisplayText.Aspect_TODT_DEKALE: 2>, 'Aspect_TODT_BLEND': <Aspect_TypeOfDisplayText.Aspect_TODT_BLEND: 3>, 'Aspect_TODT_DIMENSION': <Aspect_TypeOfDisplayText.Aspect_TODT_DIMENSION: 4>, 'Aspect_TODT_SHADOW': <Aspect_TypeOfDisplayText.Aspect_TODT_SHADOW: 5>}
    pass
class Aspect_TypeOfFacingModel():
    """
    None

    Members:

      Aspect_TOFM_BOTH_SIDE

      Aspect_TOFM_BACK_SIDE

      Aspect_TOFM_FRONT_SIDE
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
    Aspect_TOFM_BACK_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = <Aspect_TypeOfFacingModel.Aspect_TOFM_BACK_SIDE: 1>
    Aspect_TOFM_BOTH_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = <Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE: 0>
    Aspect_TOFM_FRONT_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = <Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE: 2>
    __entries: dict # value = {'Aspect_TOFM_BOTH_SIDE': (<Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE: 0>, None), 'Aspect_TOFM_BACK_SIDE': (<Aspect_TypeOfFacingModel.Aspect_TOFM_BACK_SIDE: 1>, None), 'Aspect_TOFM_FRONT_SIDE': (<Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE: 2>, None)}
    __members__: dict # value = {'Aspect_TOFM_BOTH_SIDE': <Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE: 0>, 'Aspect_TOFM_BACK_SIDE': <Aspect_TypeOfFacingModel.Aspect_TOFM_BACK_SIDE: 1>, 'Aspect_TOFM_FRONT_SIDE': <Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE: 2>}
    pass
class Aspect_TypeOfHighlightMethod():
    """
    Definition of a highlight method

    Members:

      Aspect_TOHM_COLOR

      Aspect_TOHM_BOUNDBOX
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
    Aspect_TOHM_BOUNDBOX: OCP.Aspect.Aspect_TypeOfHighlightMethod # value = <Aspect_TypeOfHighlightMethod.Aspect_TOHM_BOUNDBOX: 1>
    Aspect_TOHM_COLOR: OCP.Aspect.Aspect_TypeOfHighlightMethod # value = <Aspect_TypeOfHighlightMethod.Aspect_TOHM_COLOR: 0>
    __entries: dict # value = {'Aspect_TOHM_COLOR': (<Aspect_TypeOfHighlightMethod.Aspect_TOHM_COLOR: 0>, None), 'Aspect_TOHM_BOUNDBOX': (<Aspect_TypeOfHighlightMethod.Aspect_TOHM_BOUNDBOX: 1>, None)}
    __members__: dict # value = {'Aspect_TOHM_COLOR': <Aspect_TypeOfHighlightMethod.Aspect_TOHM_COLOR: 0>, 'Aspect_TOHM_BOUNDBOX': <Aspect_TypeOfHighlightMethod.Aspect_TOHM_BOUNDBOX: 1>}
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
    Aspect_TOL_DASH: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_DASH: 1>
    Aspect_TOL_DOT: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_DOT: 2>
    Aspect_TOL_DOTDASH: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_DOTDASH: 3>
    Aspect_TOL_EMPTY: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_EMPTY: -1>
    Aspect_TOL_SOLID: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_SOLID: 0>
    Aspect_TOL_USERDEFINED: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_USERDEFINED: 4>
    __entries: dict # value = {'Aspect_TOL_EMPTY': (<Aspect_TypeOfLine.Aspect_TOL_EMPTY: -1>, None), 'Aspect_TOL_SOLID': (<Aspect_TypeOfLine.Aspect_TOL_SOLID: 0>, None), 'Aspect_TOL_DASH': (<Aspect_TypeOfLine.Aspect_TOL_DASH: 1>, None), 'Aspect_TOL_DOT': (<Aspect_TypeOfLine.Aspect_TOL_DOT: 2>, None), 'Aspect_TOL_DOTDASH': (<Aspect_TypeOfLine.Aspect_TOL_DOTDASH: 3>, None), 'Aspect_TOL_USERDEFINED': (<Aspect_TypeOfLine.Aspect_TOL_USERDEFINED: 4>, None)}
    __members__: dict # value = {'Aspect_TOL_EMPTY': <Aspect_TypeOfLine.Aspect_TOL_EMPTY: -1>, 'Aspect_TOL_SOLID': <Aspect_TypeOfLine.Aspect_TOL_SOLID: 0>, 'Aspect_TOL_DASH': <Aspect_TypeOfLine.Aspect_TOL_DASH: 1>, 'Aspect_TOL_DOT': <Aspect_TypeOfLine.Aspect_TOL_DOT: 2>, 'Aspect_TOL_DOTDASH': <Aspect_TypeOfLine.Aspect_TOL_DOTDASH: 3>, 'Aspect_TOL_USERDEFINED': <Aspect_TypeOfLine.Aspect_TOL_USERDEFINED: 4>}
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
    Aspect_TOM_BALL: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_BALL: 12>
    Aspect_TOM_EMPTY: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_EMPTY: -1>
    Aspect_TOM_O: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O: 4>
    Aspect_TOM_O_PLUS: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O_PLUS: 6>
    Aspect_TOM_O_POINT: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O_POINT: 5>
    Aspect_TOM_O_STAR: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O_STAR: 7>
    Aspect_TOM_O_X: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O_X: 8>
    Aspect_TOM_PLUS: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_PLUS: 1>
    Aspect_TOM_POINT: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_POINT: 0>
    Aspect_TOM_RING1: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_RING1: 9>
    Aspect_TOM_RING2: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_RING2: 10>
    Aspect_TOM_RING3: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_RING3: 11>
    Aspect_TOM_STAR: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_STAR: 2>
    Aspect_TOM_USERDEFINED: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_USERDEFINED: 13>
    Aspect_TOM_X: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_X: 3>
    __entries: dict # value = {'Aspect_TOM_EMPTY': (<Aspect_TypeOfMarker.Aspect_TOM_EMPTY: -1>, None), 'Aspect_TOM_POINT': (<Aspect_TypeOfMarker.Aspect_TOM_POINT: 0>, None), 'Aspect_TOM_PLUS': (<Aspect_TypeOfMarker.Aspect_TOM_PLUS: 1>, None), 'Aspect_TOM_STAR': (<Aspect_TypeOfMarker.Aspect_TOM_STAR: 2>, None), 'Aspect_TOM_X': (<Aspect_TypeOfMarker.Aspect_TOM_X: 3>, None), 'Aspect_TOM_O': (<Aspect_TypeOfMarker.Aspect_TOM_O: 4>, None), 'Aspect_TOM_O_POINT': (<Aspect_TypeOfMarker.Aspect_TOM_O_POINT: 5>, None), 'Aspect_TOM_O_PLUS': (<Aspect_TypeOfMarker.Aspect_TOM_O_PLUS: 6>, None), 'Aspect_TOM_O_STAR': (<Aspect_TypeOfMarker.Aspect_TOM_O_STAR: 7>, None), 'Aspect_TOM_O_X': (<Aspect_TypeOfMarker.Aspect_TOM_O_X: 8>, None), 'Aspect_TOM_RING1': (<Aspect_TypeOfMarker.Aspect_TOM_RING1: 9>, None), 'Aspect_TOM_RING2': (<Aspect_TypeOfMarker.Aspect_TOM_RING2: 10>, None), 'Aspect_TOM_RING3': (<Aspect_TypeOfMarker.Aspect_TOM_RING3: 11>, None), 'Aspect_TOM_BALL': (<Aspect_TypeOfMarker.Aspect_TOM_BALL: 12>, None), 'Aspect_TOM_USERDEFINED': (<Aspect_TypeOfMarker.Aspect_TOM_USERDEFINED: 13>, None)}
    __members__: dict # value = {'Aspect_TOM_EMPTY': <Aspect_TypeOfMarker.Aspect_TOM_EMPTY: -1>, 'Aspect_TOM_POINT': <Aspect_TypeOfMarker.Aspect_TOM_POINT: 0>, 'Aspect_TOM_PLUS': <Aspect_TypeOfMarker.Aspect_TOM_PLUS: 1>, 'Aspect_TOM_STAR': <Aspect_TypeOfMarker.Aspect_TOM_STAR: 2>, 'Aspect_TOM_X': <Aspect_TypeOfMarker.Aspect_TOM_X: 3>, 'Aspect_TOM_O': <Aspect_TypeOfMarker.Aspect_TOM_O: 4>, 'Aspect_TOM_O_POINT': <Aspect_TypeOfMarker.Aspect_TOM_O_POINT: 5>, 'Aspect_TOM_O_PLUS': <Aspect_TypeOfMarker.Aspect_TOM_O_PLUS: 6>, 'Aspect_TOM_O_STAR': <Aspect_TypeOfMarker.Aspect_TOM_O_STAR: 7>, 'Aspect_TOM_O_X': <Aspect_TypeOfMarker.Aspect_TOM_O_X: 8>, 'Aspect_TOM_RING1': <Aspect_TypeOfMarker.Aspect_TOM_RING1: 9>, 'Aspect_TOM_RING2': <Aspect_TypeOfMarker.Aspect_TOM_RING2: 10>, 'Aspect_TOM_RING3': <Aspect_TypeOfMarker.Aspect_TOM_RING3: 11>, 'Aspect_TOM_BALL': <Aspect_TypeOfMarker.Aspect_TOM_BALL: 12>, 'Aspect_TOM_USERDEFINED': <Aspect_TypeOfMarker.Aspect_TOM_USERDEFINED: 13>}
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
    Aspect_TOR_BOTTOM_AND_LEFT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_BOTTOM_AND_LEFT_BORDER: 8>
    Aspect_TOR_BOTTOM_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_BOTTOM_BORDER: 4>
    Aspect_TOR_LEFT_AND_TOP_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_LEFT_AND_TOP_BORDER: 9>
    Aspect_TOR_LEFT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_LEFT_BORDER: 5>
    Aspect_TOR_NO_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_NO_BORDER: 1>
    Aspect_TOR_RIGHT_AND_BOTTOM_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_RIGHT_AND_BOTTOM_BORDER: 7>
    Aspect_TOR_RIGHT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_RIGHT_BORDER: 3>
    Aspect_TOR_TOP_AND_RIGHT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_TOP_AND_RIGHT_BORDER: 6>
    Aspect_TOR_TOP_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_TOP_BORDER: 2>
    Aspect_TOR_UNKNOWN: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_UNKNOWN: 0>
    __entries: dict # value = {'Aspect_TOR_UNKNOWN': (<Aspect_TypeOfResize.Aspect_TOR_UNKNOWN: 0>, None), 'Aspect_TOR_NO_BORDER': (<Aspect_TypeOfResize.Aspect_TOR_NO_BORDER: 1>, None), 'Aspect_TOR_TOP_BORDER': (<Aspect_TypeOfResize.Aspect_TOR_TOP_BORDER: 2>, None), 'Aspect_TOR_RIGHT_BORDER': (<Aspect_TypeOfResize.Aspect_TOR_RIGHT_BORDER: 3>, None), 'Aspect_TOR_BOTTOM_BORDER': (<Aspect_TypeOfResize.Aspect_TOR_BOTTOM_BORDER: 4>, None), 'Aspect_TOR_LEFT_BORDER': (<Aspect_TypeOfResize.Aspect_TOR_LEFT_BORDER: 5>, None), 'Aspect_TOR_TOP_AND_RIGHT_BORDER': (<Aspect_TypeOfResize.Aspect_TOR_TOP_AND_RIGHT_BORDER: 6>, None), 'Aspect_TOR_RIGHT_AND_BOTTOM_BORDER': (<Aspect_TypeOfResize.Aspect_TOR_RIGHT_AND_BOTTOM_BORDER: 7>, None), 'Aspect_TOR_BOTTOM_AND_LEFT_BORDER': (<Aspect_TypeOfResize.Aspect_TOR_BOTTOM_AND_LEFT_BORDER: 8>, None), 'Aspect_TOR_LEFT_AND_TOP_BORDER': (<Aspect_TypeOfResize.Aspect_TOR_LEFT_AND_TOP_BORDER: 9>, None)}
    __members__: dict # value = {'Aspect_TOR_UNKNOWN': <Aspect_TypeOfResize.Aspect_TOR_UNKNOWN: 0>, 'Aspect_TOR_NO_BORDER': <Aspect_TypeOfResize.Aspect_TOR_NO_BORDER: 1>, 'Aspect_TOR_TOP_BORDER': <Aspect_TypeOfResize.Aspect_TOR_TOP_BORDER: 2>, 'Aspect_TOR_RIGHT_BORDER': <Aspect_TypeOfResize.Aspect_TOR_RIGHT_BORDER: 3>, 'Aspect_TOR_BOTTOM_BORDER': <Aspect_TypeOfResize.Aspect_TOR_BOTTOM_BORDER: 4>, 'Aspect_TOR_LEFT_BORDER': <Aspect_TypeOfResize.Aspect_TOR_LEFT_BORDER: 5>, 'Aspect_TOR_TOP_AND_RIGHT_BORDER': <Aspect_TypeOfResize.Aspect_TOR_TOP_AND_RIGHT_BORDER: 6>, 'Aspect_TOR_RIGHT_AND_BOTTOM_BORDER': <Aspect_TypeOfResize.Aspect_TOR_RIGHT_AND_BOTTOM_BORDER: 7>, 'Aspect_TOR_BOTTOM_AND_LEFT_BORDER': <Aspect_TypeOfResize.Aspect_TOR_BOTTOM_AND_LEFT_BORDER: 8>, 'Aspect_TOR_LEFT_AND_TOP_BORDER': <Aspect_TypeOfResize.Aspect_TOR_LEFT_AND_TOP_BORDER: 9>}
    pass
class Aspect_TypeOfStyleText():
    """
    Define the style of the text.

    Members:

      Aspect_TOST_NORMAL

      Aspect_TOST_ANNOTATION
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
    Aspect_TOST_ANNOTATION: OCP.Aspect.Aspect_TypeOfStyleText # value = <Aspect_TypeOfStyleText.Aspect_TOST_ANNOTATION: 1>
    Aspect_TOST_NORMAL: OCP.Aspect.Aspect_TypeOfStyleText # value = <Aspect_TypeOfStyleText.Aspect_TOST_NORMAL: 0>
    __entries: dict # value = {'Aspect_TOST_NORMAL': (<Aspect_TypeOfStyleText.Aspect_TOST_NORMAL: 0>, None), 'Aspect_TOST_ANNOTATION': (<Aspect_TypeOfStyleText.Aspect_TOST_ANNOTATION: 1>, None)}
    __members__: dict # value = {'Aspect_TOST_NORMAL': <Aspect_TypeOfStyleText.Aspect_TOST_NORMAL: 0>, 'Aspect_TOST_ANNOTATION': <Aspect_TypeOfStyleText.Aspect_TOST_ANNOTATION: 1>}
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
    Aspect_TOTP_BOTTOM: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_BOTTOM: 2>
    Aspect_TOTP_CENTER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER: 0>
    Aspect_TOTP_LEFT: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT: 4>
    Aspect_TOTP_LEFT_LOWER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_LOWER: 6>
    Aspect_TOTP_LEFT_UPPER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_UPPER: 5>
    Aspect_TOTP_RIGHT: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT: 8>
    Aspect_TOTP_RIGHT_LOWER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_LOWER: 10>
    Aspect_TOTP_RIGHT_UPPER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_UPPER: 9>
    Aspect_TOTP_TOP: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_TOP: 1>
    __entries: dict # value = {'Aspect_TOTP_CENTER': (<Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER: 0>, None), 'Aspect_TOTP_TOP': (<Aspect_TypeOfTriedronPosition.Aspect_TOTP_TOP: 1>, None), 'Aspect_TOTP_BOTTOM': (<Aspect_TypeOfTriedronPosition.Aspect_TOTP_BOTTOM: 2>, None), 'Aspect_TOTP_LEFT': (<Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT: 4>, None), 'Aspect_TOTP_RIGHT': (<Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT: 8>, None), 'Aspect_TOTP_LEFT_LOWER': (<Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_LOWER: 6>, None), 'Aspect_TOTP_LEFT_UPPER': (<Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_UPPER: 5>, None), 'Aspect_TOTP_RIGHT_LOWER': (<Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_LOWER: 10>, None), 'Aspect_TOTP_RIGHT_UPPER': (<Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_UPPER: 9>, None)}
    __members__: dict # value = {'Aspect_TOTP_CENTER': <Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER: 0>, 'Aspect_TOTP_TOP': <Aspect_TypeOfTriedronPosition.Aspect_TOTP_TOP: 1>, 'Aspect_TOTP_BOTTOM': <Aspect_TypeOfTriedronPosition.Aspect_TOTP_BOTTOM: 2>, 'Aspect_TOTP_LEFT': <Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT: 4>, 'Aspect_TOTP_RIGHT': <Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT: 8>, 'Aspect_TOTP_LEFT_LOWER': <Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_LOWER: 6>, 'Aspect_TOTP_LEFT_UPPER': <Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_UPPER: 5>, 'Aspect_TOTP_RIGHT_LOWER': <Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_LOWER: 10>, 'Aspect_TOTP_RIGHT_UPPER': <Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_UPPER: 9>}
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

      Aspect_VKey_ViewTop

      Aspect_VKey_ViewBottom

      Aspect_VKey_ViewLeft

      Aspect_VKey_ViewRight

      Aspect_VKey_ViewFront

      Aspect_VKey_ViewBack

      Aspect_VKey_ViewAxoLeftProj

      Aspect_VKey_ViewAxoRightProj

      Aspect_VKey_ViewFitAll

      Aspect_VKey_ViewRoll90CW

      Aspect_VKey_ViewRoll90CCW

      Aspect_VKey_ViewSwitchRotate

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
    Aspect_VKey_0: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_0: 27>
    Aspect_VKey_1: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_1: 28>
    Aspect_VKey_2: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_2: 29>
    Aspect_VKey_3: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_3: 30>
    Aspect_VKey_4: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_4: 31>
    Aspect_VKey_5: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_5: 32>
    Aspect_VKey_6: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_6: 33>
    Aspect_VKey_7: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_7: 34>
    Aspect_VKey_8: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_8: 35>
    Aspect_VKey_9: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_9: 36>
    Aspect_VKey_A: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_A: 1>
    Aspect_VKey_Alt: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Alt: 120>
    Aspect_VKey_Apostrophe: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Apostrophe: 75>
    Aspect_VKey_B: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_B: 2>
    Aspect_VKey_Back: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Back: 61>
    Aspect_VKey_Backslash: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Backslash: 73>
    Aspect_VKey_Backspace: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Backspace: 63>
    Aspect_VKey_BracketLeft: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BracketLeft: 72>
    Aspect_VKey_BracketRight: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BracketRight: 74>
    Aspect_VKey_BrowserBack: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserBack: 99>
    Aspect_VKey_BrowserFavorites: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserFavorites: 104>
    Aspect_VKey_BrowserForward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserForward: 100>
    Aspect_VKey_BrowserHome: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserHome: 105>
    Aspect_VKey_BrowserRefresh: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserRefresh: 101>
    Aspect_VKey_BrowserSearch: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserSearch: 103>
    Aspect_VKey_BrowserStop: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserStop: 102>
    Aspect_VKey_C: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_C: 3>
    Aspect_VKey_Comma: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Comma: 68>
    Aspect_VKey_Control: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Control: 119>
    Aspect_VKey_D: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_D: 4>
    Aspect_VKey_Delete: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Delete: 65>
    Aspect_VKey_Down: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Down: 50>
    Aspect_VKey_E: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_E: 5>
    Aspect_VKey_End: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_End: 59>
    Aspect_VKey_Enter: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Enter: 62>
    Aspect_VKey_Equal: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Equal: 55>
    Aspect_VKey_Escape: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Escape: 60>
    Aspect_VKey_F: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F: 6>
    Aspect_VKey_F1: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F1: 37>
    Aspect_VKey_F10: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F10: 46>
    Aspect_VKey_F11: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F11: 47>
    Aspect_VKey_F12: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F12: 48>
    Aspect_VKey_F2: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F2: 38>
    Aspect_VKey_F3: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F3: 39>
    Aspect_VKey_F4: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F4: 40>
    Aspect_VKey_F5: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F5: 41>
    Aspect_VKey_F6: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F6: 42>
    Aspect_VKey_F7: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F7: 43>
    Aspect_VKey_F8: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F8: 44>
    Aspect_VKey_F9: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F9: 45>
    Aspect_VKey_G: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_G: 7>
    Aspect_VKey_H: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_H: 8>
    Aspect_VKey_Home: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Home: 58>
    Aspect_VKey_I: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_I: 9>
    Aspect_VKey_J: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_J: 10>
    Aspect_VKey_K: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_K: 11>
    Aspect_VKey_L: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_L: 12>
    Aspect_VKey_Left: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Left: 51>
    Aspect_VKey_M: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_M: 13>
    Aspect_VKey_MediaNextTrack: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_MediaNextTrack: 92>
    Aspect_VKey_MediaPlayPause: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_MediaPlayPause: 95>
    Aspect_VKey_MediaPreviousTrack: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_MediaPreviousTrack: 93>
    Aspect_VKey_MediaStop: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_MediaStop: 94>
    Aspect_VKey_Menu: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Menu: 121>
    Aspect_VKey_Meta: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Meta: 122>
    Aspect_VKey_Minus: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Minus: 54>
    Aspect_VKey_N: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_N: 14>
    Aspect_VKey_NavBackward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavBackward: 125>
    Aspect_VKey_NavCrouch: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavCrouch: 136>
    Aspect_VKey_NavForward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavForward: 124>
    Aspect_VKey_NavInteract: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavInteract: 123>
    Aspect_VKey_NavJump: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavJump: 137>
    Aspect_VKey_NavLookDown: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavLookDown: 135>
    Aspect_VKey_NavLookLeft: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavLookLeft: 132>
    Aspect_VKey_NavLookRight: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavLookRight: 133>
    Aspect_VKey_NavLookUp: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavLookUp: 134>
    Aspect_VKey_NavRollCCW: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavRollCCW: 130>
    Aspect_VKey_NavRollCW: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavRollCW: 131>
    Aspect_VKey_NavSlideDown: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSlideDown: 129>
    Aspect_VKey_NavSlideLeft: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSlideLeft: 126>
    Aspect_VKey_NavSlideRight: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSlideRight: 127>
    Aspect_VKey_NavSlideUp: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSlideUp: 128>
    Aspect_VKey_NavSpeedDecrease: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSpeedDecrease: 142>
    Aspect_VKey_NavSpeedIncrease: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSpeedIncrease: 141>
    Aspect_VKey_NavThrustBackward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavThrustBackward: 139>
    Aspect_VKey_NavThrustForward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavThrustForward: 138>
    Aspect_VKey_NavThrustStop: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavThrustStop: 140>
    Aspect_VKey_Numlock: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numlock: 76>
    Aspect_VKey_Numpad0: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad0: 78>
    Aspect_VKey_Numpad1: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad1: 79>
    Aspect_VKey_Numpad2: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad2: 80>
    Aspect_VKey_Numpad3: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad3: 81>
    Aspect_VKey_Numpad4: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad4: 82>
    Aspect_VKey_Numpad5: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad5: 83>
    Aspect_VKey_Numpad6: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad6: 84>
    Aspect_VKey_Numpad7: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad7: 85>
    Aspect_VKey_Numpad8: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad8: 86>
    Aspect_VKey_Numpad9: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad9: 87>
    Aspect_VKey_NumpadAdd: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NumpadAdd: 89>
    Aspect_VKey_NumpadDivide: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NumpadDivide: 91>
    Aspect_VKey_NumpadMultiply: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NumpadMultiply: 88>
    Aspect_VKey_NumpadSubtract: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NumpadSubtract: 90>
    Aspect_VKey_O: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_O: 15>
    Aspect_VKey_P: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_P: 16>
    Aspect_VKey_PageDown: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_PageDown: 57>
    Aspect_VKey_PageUp: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_PageUp: 56>
    Aspect_VKey_Period: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Period: 69>
    Aspect_VKey_Plus: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Plus: 53>
    Aspect_VKey_Q: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Q: 17>
    Aspect_VKey_R: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_R: 18>
    Aspect_VKey_Right: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Right: 52>
    Aspect_VKey_S: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_S: 19>
    Aspect_VKey_Scroll: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Scroll: 77>
    Aspect_VKey_Semicolon: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Semicolon: 70>
    Aspect_VKey_Shift: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Shift: 118>
    Aspect_VKey_Slash: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Slash: 71>
    Aspect_VKey_Space: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Space: 64>
    Aspect_VKey_T: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_T: 20>
    Aspect_VKey_Tab: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Tab: 67>
    Aspect_VKey_Tilde: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Tilde: 66>
    Aspect_VKey_U: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_U: 21>
    Aspect_VKey_UNKNOWN: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_UNKNOWN: 0>
    Aspect_VKey_Up: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Up: 49>
    Aspect_VKey_V: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_V: 22>
    Aspect_VKey_ViewAxoLeftProj: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewAxoLeftProj: 112>
    Aspect_VKey_ViewAxoRightProj: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewAxoRightProj: 113>
    Aspect_VKey_ViewBack: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewBack: 111>
    Aspect_VKey_ViewBottom: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewBottom: 107>
    Aspect_VKey_ViewFitAll: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewFitAll: 114>
    Aspect_VKey_ViewFront: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewFront: 110>
    Aspect_VKey_ViewLeft: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewLeft: 108>
    Aspect_VKey_ViewRight: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewRight: 109>
    Aspect_VKey_ViewRoll90CCW: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CCW: 116>
    Aspect_VKey_ViewRoll90CW: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CW: 115>
    Aspect_VKey_ViewSwitchRotate: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewSwitchRotate: 117>
    Aspect_VKey_ViewTop: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewTop: 106>
    Aspect_VKey_VolumeDown: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_VolumeDown: 97>
    Aspect_VKey_VolumeMute: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_VolumeMute: 96>
    Aspect_VKey_VolumeUp: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_VolumeUp: 98>
    Aspect_VKey_W: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_W: 23>
    Aspect_VKey_X: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_X: 24>
    Aspect_VKey_Y: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Y: 25>
    Aspect_VKey_Z: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Z: 26>
    __entries: dict # value = {'Aspect_VKey_UNKNOWN': (<Aspect_VKeyBasic.Aspect_VKey_UNKNOWN: 0>, None), 'Aspect_VKey_A': (<Aspect_VKeyBasic.Aspect_VKey_A: 1>, None), 'Aspect_VKey_B': (<Aspect_VKeyBasic.Aspect_VKey_B: 2>, None), 'Aspect_VKey_C': (<Aspect_VKeyBasic.Aspect_VKey_C: 3>, None), 'Aspect_VKey_D': (<Aspect_VKeyBasic.Aspect_VKey_D: 4>, None), 'Aspect_VKey_E': (<Aspect_VKeyBasic.Aspect_VKey_E: 5>, None), 'Aspect_VKey_F': (<Aspect_VKeyBasic.Aspect_VKey_F: 6>, None), 'Aspect_VKey_G': (<Aspect_VKeyBasic.Aspect_VKey_G: 7>, None), 'Aspect_VKey_H': (<Aspect_VKeyBasic.Aspect_VKey_H: 8>, None), 'Aspect_VKey_I': (<Aspect_VKeyBasic.Aspect_VKey_I: 9>, None), 'Aspect_VKey_J': (<Aspect_VKeyBasic.Aspect_VKey_J: 10>, None), 'Aspect_VKey_K': (<Aspect_VKeyBasic.Aspect_VKey_K: 11>, None), 'Aspect_VKey_L': (<Aspect_VKeyBasic.Aspect_VKey_L: 12>, None), 'Aspect_VKey_M': (<Aspect_VKeyBasic.Aspect_VKey_M: 13>, None), 'Aspect_VKey_N': (<Aspect_VKeyBasic.Aspect_VKey_N: 14>, None), 'Aspect_VKey_O': (<Aspect_VKeyBasic.Aspect_VKey_O: 15>, None), 'Aspect_VKey_P': (<Aspect_VKeyBasic.Aspect_VKey_P: 16>, None), 'Aspect_VKey_Q': (<Aspect_VKeyBasic.Aspect_VKey_Q: 17>, None), 'Aspect_VKey_R': (<Aspect_VKeyBasic.Aspect_VKey_R: 18>, None), 'Aspect_VKey_S': (<Aspect_VKeyBasic.Aspect_VKey_S: 19>, None), 'Aspect_VKey_T': (<Aspect_VKeyBasic.Aspect_VKey_T: 20>, None), 'Aspect_VKey_U': (<Aspect_VKeyBasic.Aspect_VKey_U: 21>, None), 'Aspect_VKey_V': (<Aspect_VKeyBasic.Aspect_VKey_V: 22>, None), 'Aspect_VKey_W': (<Aspect_VKeyBasic.Aspect_VKey_W: 23>, None), 'Aspect_VKey_X': (<Aspect_VKeyBasic.Aspect_VKey_X: 24>, None), 'Aspect_VKey_Y': (<Aspect_VKeyBasic.Aspect_VKey_Y: 25>, None), 'Aspect_VKey_Z': (<Aspect_VKeyBasic.Aspect_VKey_Z: 26>, None), 'Aspect_VKey_0': (<Aspect_VKeyBasic.Aspect_VKey_0: 27>, None), 'Aspect_VKey_1': (<Aspect_VKeyBasic.Aspect_VKey_1: 28>, None), 'Aspect_VKey_2': (<Aspect_VKeyBasic.Aspect_VKey_2: 29>, None), 'Aspect_VKey_3': (<Aspect_VKeyBasic.Aspect_VKey_3: 30>, None), 'Aspect_VKey_4': (<Aspect_VKeyBasic.Aspect_VKey_4: 31>, None), 'Aspect_VKey_5': (<Aspect_VKeyBasic.Aspect_VKey_5: 32>, None), 'Aspect_VKey_6': (<Aspect_VKeyBasic.Aspect_VKey_6: 33>, None), 'Aspect_VKey_7': (<Aspect_VKeyBasic.Aspect_VKey_7: 34>, None), 'Aspect_VKey_8': (<Aspect_VKeyBasic.Aspect_VKey_8: 35>, None), 'Aspect_VKey_9': (<Aspect_VKeyBasic.Aspect_VKey_9: 36>, None), 'Aspect_VKey_F1': (<Aspect_VKeyBasic.Aspect_VKey_F1: 37>, None), 'Aspect_VKey_F2': (<Aspect_VKeyBasic.Aspect_VKey_F2: 38>, None), 'Aspect_VKey_F3': (<Aspect_VKeyBasic.Aspect_VKey_F3: 39>, None), 'Aspect_VKey_F4': (<Aspect_VKeyBasic.Aspect_VKey_F4: 40>, None), 'Aspect_VKey_F5': (<Aspect_VKeyBasic.Aspect_VKey_F5: 41>, None), 'Aspect_VKey_F6': (<Aspect_VKeyBasic.Aspect_VKey_F6: 42>, None), 'Aspect_VKey_F7': (<Aspect_VKeyBasic.Aspect_VKey_F7: 43>, None), 'Aspect_VKey_F8': (<Aspect_VKeyBasic.Aspect_VKey_F8: 44>, None), 'Aspect_VKey_F9': (<Aspect_VKeyBasic.Aspect_VKey_F9: 45>, None), 'Aspect_VKey_F10': (<Aspect_VKeyBasic.Aspect_VKey_F10: 46>, None), 'Aspect_VKey_F11': (<Aspect_VKeyBasic.Aspect_VKey_F11: 47>, None), 'Aspect_VKey_F12': (<Aspect_VKeyBasic.Aspect_VKey_F12: 48>, None), 'Aspect_VKey_Up': (<Aspect_VKeyBasic.Aspect_VKey_Up: 49>, None), 'Aspect_VKey_Down': (<Aspect_VKeyBasic.Aspect_VKey_Down: 50>, None), 'Aspect_VKey_Left': (<Aspect_VKeyBasic.Aspect_VKey_Left: 51>, None), 'Aspect_VKey_Right': (<Aspect_VKeyBasic.Aspect_VKey_Right: 52>, None), 'Aspect_VKey_Plus': (<Aspect_VKeyBasic.Aspect_VKey_Plus: 53>, None), 'Aspect_VKey_Minus': (<Aspect_VKeyBasic.Aspect_VKey_Minus: 54>, None), 'Aspect_VKey_Equal': (<Aspect_VKeyBasic.Aspect_VKey_Equal: 55>, None), 'Aspect_VKey_PageUp': (<Aspect_VKeyBasic.Aspect_VKey_PageUp: 56>, None), 'Aspect_VKey_PageDown': (<Aspect_VKeyBasic.Aspect_VKey_PageDown: 57>, None), 'Aspect_VKey_Home': (<Aspect_VKeyBasic.Aspect_VKey_Home: 58>, None), 'Aspect_VKey_End': (<Aspect_VKeyBasic.Aspect_VKey_End: 59>, None), 'Aspect_VKey_Escape': (<Aspect_VKeyBasic.Aspect_VKey_Escape: 60>, None), 'Aspect_VKey_Back': (<Aspect_VKeyBasic.Aspect_VKey_Back: 61>, None), 'Aspect_VKey_Enter': (<Aspect_VKeyBasic.Aspect_VKey_Enter: 62>, None), 'Aspect_VKey_Backspace': (<Aspect_VKeyBasic.Aspect_VKey_Backspace: 63>, None), 'Aspect_VKey_Space': (<Aspect_VKeyBasic.Aspect_VKey_Space: 64>, None), 'Aspect_VKey_Delete': (<Aspect_VKeyBasic.Aspect_VKey_Delete: 65>, None), 'Aspect_VKey_Tilde': (<Aspect_VKeyBasic.Aspect_VKey_Tilde: 66>, None), 'Aspect_VKey_Tab': (<Aspect_VKeyBasic.Aspect_VKey_Tab: 67>, None), 'Aspect_VKey_Comma': (<Aspect_VKeyBasic.Aspect_VKey_Comma: 68>, None), 'Aspect_VKey_Period': (<Aspect_VKeyBasic.Aspect_VKey_Period: 69>, None), 'Aspect_VKey_Semicolon': (<Aspect_VKeyBasic.Aspect_VKey_Semicolon: 70>, None), 'Aspect_VKey_Slash': (<Aspect_VKeyBasic.Aspect_VKey_Slash: 71>, None), 'Aspect_VKey_BracketLeft': (<Aspect_VKeyBasic.Aspect_VKey_BracketLeft: 72>, None), 'Aspect_VKey_Backslash': (<Aspect_VKeyBasic.Aspect_VKey_Backslash: 73>, None), 'Aspect_VKey_BracketRight': (<Aspect_VKeyBasic.Aspect_VKey_BracketRight: 74>, None), 'Aspect_VKey_Apostrophe': (<Aspect_VKeyBasic.Aspect_VKey_Apostrophe: 75>, None), 'Aspect_VKey_Numlock': (<Aspect_VKeyBasic.Aspect_VKey_Numlock: 76>, None), 'Aspect_VKey_Scroll': (<Aspect_VKeyBasic.Aspect_VKey_Scroll: 77>, None), 'Aspect_VKey_Numpad0': (<Aspect_VKeyBasic.Aspect_VKey_Numpad0: 78>, None), 'Aspect_VKey_Numpad1': (<Aspect_VKeyBasic.Aspect_VKey_Numpad1: 79>, None), 'Aspect_VKey_Numpad2': (<Aspect_VKeyBasic.Aspect_VKey_Numpad2: 80>, None), 'Aspect_VKey_Numpad3': (<Aspect_VKeyBasic.Aspect_VKey_Numpad3: 81>, None), 'Aspect_VKey_Numpad4': (<Aspect_VKeyBasic.Aspect_VKey_Numpad4: 82>, None), 'Aspect_VKey_Numpad5': (<Aspect_VKeyBasic.Aspect_VKey_Numpad5: 83>, None), 'Aspect_VKey_Numpad6': (<Aspect_VKeyBasic.Aspect_VKey_Numpad6: 84>, None), 'Aspect_VKey_Numpad7': (<Aspect_VKeyBasic.Aspect_VKey_Numpad7: 85>, None), 'Aspect_VKey_Numpad8': (<Aspect_VKeyBasic.Aspect_VKey_Numpad8: 86>, None), 'Aspect_VKey_Numpad9': (<Aspect_VKeyBasic.Aspect_VKey_Numpad9: 87>, None), 'Aspect_VKey_NumpadMultiply': (<Aspect_VKeyBasic.Aspect_VKey_NumpadMultiply: 88>, None), 'Aspect_VKey_NumpadAdd': (<Aspect_VKeyBasic.Aspect_VKey_NumpadAdd: 89>, None), 'Aspect_VKey_NumpadSubtract': (<Aspect_VKeyBasic.Aspect_VKey_NumpadSubtract: 90>, None), 'Aspect_VKey_NumpadDivide': (<Aspect_VKeyBasic.Aspect_VKey_NumpadDivide: 91>, None), 'Aspect_VKey_MediaNextTrack': (<Aspect_VKeyBasic.Aspect_VKey_MediaNextTrack: 92>, None), 'Aspect_VKey_MediaPreviousTrack': (<Aspect_VKeyBasic.Aspect_VKey_MediaPreviousTrack: 93>, None), 'Aspect_VKey_MediaStop': (<Aspect_VKeyBasic.Aspect_VKey_MediaStop: 94>, None), 'Aspect_VKey_MediaPlayPause': (<Aspect_VKeyBasic.Aspect_VKey_MediaPlayPause: 95>, None), 'Aspect_VKey_VolumeMute': (<Aspect_VKeyBasic.Aspect_VKey_VolumeMute: 96>, None), 'Aspect_VKey_VolumeDown': (<Aspect_VKeyBasic.Aspect_VKey_VolumeDown: 97>, None), 'Aspect_VKey_VolumeUp': (<Aspect_VKeyBasic.Aspect_VKey_VolumeUp: 98>, None), 'Aspect_VKey_BrowserBack': (<Aspect_VKeyBasic.Aspect_VKey_BrowserBack: 99>, None), 'Aspect_VKey_BrowserForward': (<Aspect_VKeyBasic.Aspect_VKey_BrowserForward: 100>, None), 'Aspect_VKey_BrowserRefresh': (<Aspect_VKeyBasic.Aspect_VKey_BrowserRefresh: 101>, None), 'Aspect_VKey_BrowserStop': (<Aspect_VKeyBasic.Aspect_VKey_BrowserStop: 102>, None), 'Aspect_VKey_BrowserSearch': (<Aspect_VKeyBasic.Aspect_VKey_BrowserSearch: 103>, None), 'Aspect_VKey_BrowserFavorites': (<Aspect_VKeyBasic.Aspect_VKey_BrowserFavorites: 104>, None), 'Aspect_VKey_BrowserHome': (<Aspect_VKeyBasic.Aspect_VKey_BrowserHome: 105>, None), 'Aspect_VKey_ViewTop': (<Aspect_VKeyBasic.Aspect_VKey_ViewTop: 106>, None), 'Aspect_VKey_ViewBottom': (<Aspect_VKeyBasic.Aspect_VKey_ViewBottom: 107>, None), 'Aspect_VKey_ViewLeft': (<Aspect_VKeyBasic.Aspect_VKey_ViewLeft: 108>, None), 'Aspect_VKey_ViewRight': (<Aspect_VKeyBasic.Aspect_VKey_ViewRight: 109>, None), 'Aspect_VKey_ViewFront': (<Aspect_VKeyBasic.Aspect_VKey_ViewFront: 110>, None), 'Aspect_VKey_ViewBack': (<Aspect_VKeyBasic.Aspect_VKey_ViewBack: 111>, None), 'Aspect_VKey_ViewAxoLeftProj': (<Aspect_VKeyBasic.Aspect_VKey_ViewAxoLeftProj: 112>, None), 'Aspect_VKey_ViewAxoRightProj': (<Aspect_VKeyBasic.Aspect_VKey_ViewAxoRightProj: 113>, None), 'Aspect_VKey_ViewFitAll': (<Aspect_VKeyBasic.Aspect_VKey_ViewFitAll: 114>, None), 'Aspect_VKey_ViewRoll90CW': (<Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CW: 115>, None), 'Aspect_VKey_ViewRoll90CCW': (<Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CCW: 116>, None), 'Aspect_VKey_ViewSwitchRotate': (<Aspect_VKeyBasic.Aspect_VKey_ViewSwitchRotate: 117>, None), 'Aspect_VKey_Shift': (<Aspect_VKeyBasic.Aspect_VKey_Shift: 118>, None), 'Aspect_VKey_Control': (<Aspect_VKeyBasic.Aspect_VKey_Control: 119>, None), 'Aspect_VKey_Alt': (<Aspect_VKeyBasic.Aspect_VKey_Alt: 120>, None), 'Aspect_VKey_Menu': (<Aspect_VKeyBasic.Aspect_VKey_Menu: 121>, None), 'Aspect_VKey_Meta': (<Aspect_VKeyBasic.Aspect_VKey_Meta: 122>, None), 'Aspect_VKey_NavInteract': (<Aspect_VKeyBasic.Aspect_VKey_NavInteract: 123>, None), 'Aspect_VKey_NavForward': (<Aspect_VKeyBasic.Aspect_VKey_NavForward: 124>, None), 'Aspect_VKey_NavBackward': (<Aspect_VKeyBasic.Aspect_VKey_NavBackward: 125>, None), 'Aspect_VKey_NavSlideLeft': (<Aspect_VKeyBasic.Aspect_VKey_NavSlideLeft: 126>, None), 'Aspect_VKey_NavSlideRight': (<Aspect_VKeyBasic.Aspect_VKey_NavSlideRight: 127>, None), 'Aspect_VKey_NavSlideUp': (<Aspect_VKeyBasic.Aspect_VKey_NavSlideUp: 128>, None), 'Aspect_VKey_NavSlideDown': (<Aspect_VKeyBasic.Aspect_VKey_NavSlideDown: 129>, None), 'Aspect_VKey_NavRollCCW': (<Aspect_VKeyBasic.Aspect_VKey_NavRollCCW: 130>, None), 'Aspect_VKey_NavRollCW': (<Aspect_VKeyBasic.Aspect_VKey_NavRollCW: 131>, None), 'Aspect_VKey_NavLookLeft': (<Aspect_VKeyBasic.Aspect_VKey_NavLookLeft: 132>, None), 'Aspect_VKey_NavLookRight': (<Aspect_VKeyBasic.Aspect_VKey_NavLookRight: 133>, None), 'Aspect_VKey_NavLookUp': (<Aspect_VKeyBasic.Aspect_VKey_NavLookUp: 134>, None), 'Aspect_VKey_NavLookDown': (<Aspect_VKeyBasic.Aspect_VKey_NavLookDown: 135>, None), 'Aspect_VKey_NavCrouch': (<Aspect_VKeyBasic.Aspect_VKey_NavCrouch: 136>, None), 'Aspect_VKey_NavJump': (<Aspect_VKeyBasic.Aspect_VKey_NavJump: 137>, None), 'Aspect_VKey_NavThrustForward': (<Aspect_VKeyBasic.Aspect_VKey_NavThrustForward: 138>, None), 'Aspect_VKey_NavThrustBackward': (<Aspect_VKeyBasic.Aspect_VKey_NavThrustBackward: 139>, None), 'Aspect_VKey_NavThrustStop': (<Aspect_VKeyBasic.Aspect_VKey_NavThrustStop: 140>, None), 'Aspect_VKey_NavSpeedIncrease': (<Aspect_VKeyBasic.Aspect_VKey_NavSpeedIncrease: 141>, None), 'Aspect_VKey_NavSpeedDecrease': (<Aspect_VKeyBasic.Aspect_VKey_NavSpeedDecrease: 142>, None)}
    __members__: dict # value = {'Aspect_VKey_UNKNOWN': <Aspect_VKeyBasic.Aspect_VKey_UNKNOWN: 0>, 'Aspect_VKey_A': <Aspect_VKeyBasic.Aspect_VKey_A: 1>, 'Aspect_VKey_B': <Aspect_VKeyBasic.Aspect_VKey_B: 2>, 'Aspect_VKey_C': <Aspect_VKeyBasic.Aspect_VKey_C: 3>, 'Aspect_VKey_D': <Aspect_VKeyBasic.Aspect_VKey_D: 4>, 'Aspect_VKey_E': <Aspect_VKeyBasic.Aspect_VKey_E: 5>, 'Aspect_VKey_F': <Aspect_VKeyBasic.Aspect_VKey_F: 6>, 'Aspect_VKey_G': <Aspect_VKeyBasic.Aspect_VKey_G: 7>, 'Aspect_VKey_H': <Aspect_VKeyBasic.Aspect_VKey_H: 8>, 'Aspect_VKey_I': <Aspect_VKeyBasic.Aspect_VKey_I: 9>, 'Aspect_VKey_J': <Aspect_VKeyBasic.Aspect_VKey_J: 10>, 'Aspect_VKey_K': <Aspect_VKeyBasic.Aspect_VKey_K: 11>, 'Aspect_VKey_L': <Aspect_VKeyBasic.Aspect_VKey_L: 12>, 'Aspect_VKey_M': <Aspect_VKeyBasic.Aspect_VKey_M: 13>, 'Aspect_VKey_N': <Aspect_VKeyBasic.Aspect_VKey_N: 14>, 'Aspect_VKey_O': <Aspect_VKeyBasic.Aspect_VKey_O: 15>, 'Aspect_VKey_P': <Aspect_VKeyBasic.Aspect_VKey_P: 16>, 'Aspect_VKey_Q': <Aspect_VKeyBasic.Aspect_VKey_Q: 17>, 'Aspect_VKey_R': <Aspect_VKeyBasic.Aspect_VKey_R: 18>, 'Aspect_VKey_S': <Aspect_VKeyBasic.Aspect_VKey_S: 19>, 'Aspect_VKey_T': <Aspect_VKeyBasic.Aspect_VKey_T: 20>, 'Aspect_VKey_U': <Aspect_VKeyBasic.Aspect_VKey_U: 21>, 'Aspect_VKey_V': <Aspect_VKeyBasic.Aspect_VKey_V: 22>, 'Aspect_VKey_W': <Aspect_VKeyBasic.Aspect_VKey_W: 23>, 'Aspect_VKey_X': <Aspect_VKeyBasic.Aspect_VKey_X: 24>, 'Aspect_VKey_Y': <Aspect_VKeyBasic.Aspect_VKey_Y: 25>, 'Aspect_VKey_Z': <Aspect_VKeyBasic.Aspect_VKey_Z: 26>, 'Aspect_VKey_0': <Aspect_VKeyBasic.Aspect_VKey_0: 27>, 'Aspect_VKey_1': <Aspect_VKeyBasic.Aspect_VKey_1: 28>, 'Aspect_VKey_2': <Aspect_VKeyBasic.Aspect_VKey_2: 29>, 'Aspect_VKey_3': <Aspect_VKeyBasic.Aspect_VKey_3: 30>, 'Aspect_VKey_4': <Aspect_VKeyBasic.Aspect_VKey_4: 31>, 'Aspect_VKey_5': <Aspect_VKeyBasic.Aspect_VKey_5: 32>, 'Aspect_VKey_6': <Aspect_VKeyBasic.Aspect_VKey_6: 33>, 'Aspect_VKey_7': <Aspect_VKeyBasic.Aspect_VKey_7: 34>, 'Aspect_VKey_8': <Aspect_VKeyBasic.Aspect_VKey_8: 35>, 'Aspect_VKey_9': <Aspect_VKeyBasic.Aspect_VKey_9: 36>, 'Aspect_VKey_F1': <Aspect_VKeyBasic.Aspect_VKey_F1: 37>, 'Aspect_VKey_F2': <Aspect_VKeyBasic.Aspect_VKey_F2: 38>, 'Aspect_VKey_F3': <Aspect_VKeyBasic.Aspect_VKey_F3: 39>, 'Aspect_VKey_F4': <Aspect_VKeyBasic.Aspect_VKey_F4: 40>, 'Aspect_VKey_F5': <Aspect_VKeyBasic.Aspect_VKey_F5: 41>, 'Aspect_VKey_F6': <Aspect_VKeyBasic.Aspect_VKey_F6: 42>, 'Aspect_VKey_F7': <Aspect_VKeyBasic.Aspect_VKey_F7: 43>, 'Aspect_VKey_F8': <Aspect_VKeyBasic.Aspect_VKey_F8: 44>, 'Aspect_VKey_F9': <Aspect_VKeyBasic.Aspect_VKey_F9: 45>, 'Aspect_VKey_F10': <Aspect_VKeyBasic.Aspect_VKey_F10: 46>, 'Aspect_VKey_F11': <Aspect_VKeyBasic.Aspect_VKey_F11: 47>, 'Aspect_VKey_F12': <Aspect_VKeyBasic.Aspect_VKey_F12: 48>, 'Aspect_VKey_Up': <Aspect_VKeyBasic.Aspect_VKey_Up: 49>, 'Aspect_VKey_Down': <Aspect_VKeyBasic.Aspect_VKey_Down: 50>, 'Aspect_VKey_Left': <Aspect_VKeyBasic.Aspect_VKey_Left: 51>, 'Aspect_VKey_Right': <Aspect_VKeyBasic.Aspect_VKey_Right: 52>, 'Aspect_VKey_Plus': <Aspect_VKeyBasic.Aspect_VKey_Plus: 53>, 'Aspect_VKey_Minus': <Aspect_VKeyBasic.Aspect_VKey_Minus: 54>, 'Aspect_VKey_Equal': <Aspect_VKeyBasic.Aspect_VKey_Equal: 55>, 'Aspect_VKey_PageUp': <Aspect_VKeyBasic.Aspect_VKey_PageUp: 56>, 'Aspect_VKey_PageDown': <Aspect_VKeyBasic.Aspect_VKey_PageDown: 57>, 'Aspect_VKey_Home': <Aspect_VKeyBasic.Aspect_VKey_Home: 58>, 'Aspect_VKey_End': <Aspect_VKeyBasic.Aspect_VKey_End: 59>, 'Aspect_VKey_Escape': <Aspect_VKeyBasic.Aspect_VKey_Escape: 60>, 'Aspect_VKey_Back': <Aspect_VKeyBasic.Aspect_VKey_Back: 61>, 'Aspect_VKey_Enter': <Aspect_VKeyBasic.Aspect_VKey_Enter: 62>, 'Aspect_VKey_Backspace': <Aspect_VKeyBasic.Aspect_VKey_Backspace: 63>, 'Aspect_VKey_Space': <Aspect_VKeyBasic.Aspect_VKey_Space: 64>, 'Aspect_VKey_Delete': <Aspect_VKeyBasic.Aspect_VKey_Delete: 65>, 'Aspect_VKey_Tilde': <Aspect_VKeyBasic.Aspect_VKey_Tilde: 66>, 'Aspect_VKey_Tab': <Aspect_VKeyBasic.Aspect_VKey_Tab: 67>, 'Aspect_VKey_Comma': <Aspect_VKeyBasic.Aspect_VKey_Comma: 68>, 'Aspect_VKey_Period': <Aspect_VKeyBasic.Aspect_VKey_Period: 69>, 'Aspect_VKey_Semicolon': <Aspect_VKeyBasic.Aspect_VKey_Semicolon: 70>, 'Aspect_VKey_Slash': <Aspect_VKeyBasic.Aspect_VKey_Slash: 71>, 'Aspect_VKey_BracketLeft': <Aspect_VKeyBasic.Aspect_VKey_BracketLeft: 72>, 'Aspect_VKey_Backslash': <Aspect_VKeyBasic.Aspect_VKey_Backslash: 73>, 'Aspect_VKey_BracketRight': <Aspect_VKeyBasic.Aspect_VKey_BracketRight: 74>, 'Aspect_VKey_Apostrophe': <Aspect_VKeyBasic.Aspect_VKey_Apostrophe: 75>, 'Aspect_VKey_Numlock': <Aspect_VKeyBasic.Aspect_VKey_Numlock: 76>, 'Aspect_VKey_Scroll': <Aspect_VKeyBasic.Aspect_VKey_Scroll: 77>, 'Aspect_VKey_Numpad0': <Aspect_VKeyBasic.Aspect_VKey_Numpad0: 78>, 'Aspect_VKey_Numpad1': <Aspect_VKeyBasic.Aspect_VKey_Numpad1: 79>, 'Aspect_VKey_Numpad2': <Aspect_VKeyBasic.Aspect_VKey_Numpad2: 80>, 'Aspect_VKey_Numpad3': <Aspect_VKeyBasic.Aspect_VKey_Numpad3: 81>, 'Aspect_VKey_Numpad4': <Aspect_VKeyBasic.Aspect_VKey_Numpad4: 82>, 'Aspect_VKey_Numpad5': <Aspect_VKeyBasic.Aspect_VKey_Numpad5: 83>, 'Aspect_VKey_Numpad6': <Aspect_VKeyBasic.Aspect_VKey_Numpad6: 84>, 'Aspect_VKey_Numpad7': <Aspect_VKeyBasic.Aspect_VKey_Numpad7: 85>, 'Aspect_VKey_Numpad8': <Aspect_VKeyBasic.Aspect_VKey_Numpad8: 86>, 'Aspect_VKey_Numpad9': <Aspect_VKeyBasic.Aspect_VKey_Numpad9: 87>, 'Aspect_VKey_NumpadMultiply': <Aspect_VKeyBasic.Aspect_VKey_NumpadMultiply: 88>, 'Aspect_VKey_NumpadAdd': <Aspect_VKeyBasic.Aspect_VKey_NumpadAdd: 89>, 'Aspect_VKey_NumpadSubtract': <Aspect_VKeyBasic.Aspect_VKey_NumpadSubtract: 90>, 'Aspect_VKey_NumpadDivide': <Aspect_VKeyBasic.Aspect_VKey_NumpadDivide: 91>, 'Aspect_VKey_MediaNextTrack': <Aspect_VKeyBasic.Aspect_VKey_MediaNextTrack: 92>, 'Aspect_VKey_MediaPreviousTrack': <Aspect_VKeyBasic.Aspect_VKey_MediaPreviousTrack: 93>, 'Aspect_VKey_MediaStop': <Aspect_VKeyBasic.Aspect_VKey_MediaStop: 94>, 'Aspect_VKey_MediaPlayPause': <Aspect_VKeyBasic.Aspect_VKey_MediaPlayPause: 95>, 'Aspect_VKey_VolumeMute': <Aspect_VKeyBasic.Aspect_VKey_VolumeMute: 96>, 'Aspect_VKey_VolumeDown': <Aspect_VKeyBasic.Aspect_VKey_VolumeDown: 97>, 'Aspect_VKey_VolumeUp': <Aspect_VKeyBasic.Aspect_VKey_VolumeUp: 98>, 'Aspect_VKey_BrowserBack': <Aspect_VKeyBasic.Aspect_VKey_BrowserBack: 99>, 'Aspect_VKey_BrowserForward': <Aspect_VKeyBasic.Aspect_VKey_BrowserForward: 100>, 'Aspect_VKey_BrowserRefresh': <Aspect_VKeyBasic.Aspect_VKey_BrowserRefresh: 101>, 'Aspect_VKey_BrowserStop': <Aspect_VKeyBasic.Aspect_VKey_BrowserStop: 102>, 'Aspect_VKey_BrowserSearch': <Aspect_VKeyBasic.Aspect_VKey_BrowserSearch: 103>, 'Aspect_VKey_BrowserFavorites': <Aspect_VKeyBasic.Aspect_VKey_BrowserFavorites: 104>, 'Aspect_VKey_BrowserHome': <Aspect_VKeyBasic.Aspect_VKey_BrowserHome: 105>, 'Aspect_VKey_ViewTop': <Aspect_VKeyBasic.Aspect_VKey_ViewTop: 106>, 'Aspect_VKey_ViewBottom': <Aspect_VKeyBasic.Aspect_VKey_ViewBottom: 107>, 'Aspect_VKey_ViewLeft': <Aspect_VKeyBasic.Aspect_VKey_ViewLeft: 108>, 'Aspect_VKey_ViewRight': <Aspect_VKeyBasic.Aspect_VKey_ViewRight: 109>, 'Aspect_VKey_ViewFront': <Aspect_VKeyBasic.Aspect_VKey_ViewFront: 110>, 'Aspect_VKey_ViewBack': <Aspect_VKeyBasic.Aspect_VKey_ViewBack: 111>, 'Aspect_VKey_ViewAxoLeftProj': <Aspect_VKeyBasic.Aspect_VKey_ViewAxoLeftProj: 112>, 'Aspect_VKey_ViewAxoRightProj': <Aspect_VKeyBasic.Aspect_VKey_ViewAxoRightProj: 113>, 'Aspect_VKey_ViewFitAll': <Aspect_VKeyBasic.Aspect_VKey_ViewFitAll: 114>, 'Aspect_VKey_ViewRoll90CW': <Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CW: 115>, 'Aspect_VKey_ViewRoll90CCW': <Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CCW: 116>, 'Aspect_VKey_ViewSwitchRotate': <Aspect_VKeyBasic.Aspect_VKey_ViewSwitchRotate: 117>, 'Aspect_VKey_Shift': <Aspect_VKeyBasic.Aspect_VKey_Shift: 118>, 'Aspect_VKey_Control': <Aspect_VKeyBasic.Aspect_VKey_Control: 119>, 'Aspect_VKey_Alt': <Aspect_VKeyBasic.Aspect_VKey_Alt: 120>, 'Aspect_VKey_Menu': <Aspect_VKeyBasic.Aspect_VKey_Menu: 121>, 'Aspect_VKey_Meta': <Aspect_VKeyBasic.Aspect_VKey_Meta: 122>, 'Aspect_VKey_NavInteract': <Aspect_VKeyBasic.Aspect_VKey_NavInteract: 123>, 'Aspect_VKey_NavForward': <Aspect_VKeyBasic.Aspect_VKey_NavForward: 124>, 'Aspect_VKey_NavBackward': <Aspect_VKeyBasic.Aspect_VKey_NavBackward: 125>, 'Aspect_VKey_NavSlideLeft': <Aspect_VKeyBasic.Aspect_VKey_NavSlideLeft: 126>, 'Aspect_VKey_NavSlideRight': <Aspect_VKeyBasic.Aspect_VKey_NavSlideRight: 127>, 'Aspect_VKey_NavSlideUp': <Aspect_VKeyBasic.Aspect_VKey_NavSlideUp: 128>, 'Aspect_VKey_NavSlideDown': <Aspect_VKeyBasic.Aspect_VKey_NavSlideDown: 129>, 'Aspect_VKey_NavRollCCW': <Aspect_VKeyBasic.Aspect_VKey_NavRollCCW: 130>, 'Aspect_VKey_NavRollCW': <Aspect_VKeyBasic.Aspect_VKey_NavRollCW: 131>, 'Aspect_VKey_NavLookLeft': <Aspect_VKeyBasic.Aspect_VKey_NavLookLeft: 132>, 'Aspect_VKey_NavLookRight': <Aspect_VKeyBasic.Aspect_VKey_NavLookRight: 133>, 'Aspect_VKey_NavLookUp': <Aspect_VKeyBasic.Aspect_VKey_NavLookUp: 134>, 'Aspect_VKey_NavLookDown': <Aspect_VKeyBasic.Aspect_VKey_NavLookDown: 135>, 'Aspect_VKey_NavCrouch': <Aspect_VKeyBasic.Aspect_VKey_NavCrouch: 136>, 'Aspect_VKey_NavJump': <Aspect_VKeyBasic.Aspect_VKey_NavJump: 137>, 'Aspect_VKey_NavThrustForward': <Aspect_VKeyBasic.Aspect_VKey_NavThrustForward: 138>, 'Aspect_VKey_NavThrustBackward': <Aspect_VKeyBasic.Aspect_VKey_NavThrustBackward: 139>, 'Aspect_VKey_NavThrustStop': <Aspect_VKeyBasic.Aspect_VKey_NavThrustStop: 140>, 'Aspect_VKey_NavSpeedIncrease': <Aspect_VKeyBasic.Aspect_VKey_NavSpeedIncrease: 141>, 'Aspect_VKey_NavSpeedDecrease': <Aspect_VKeyBasic.Aspect_VKey_NavSpeedDecrease: 142>}
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
    Aspect_WOL_MEDIUM: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_MEDIUM: 1>
    Aspect_WOL_THICK: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_THICK: 2>
    Aspect_WOL_THIN: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_THIN: 0>
    Aspect_WOL_USERDEFINED: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_USERDEFINED: 4>
    Aspect_WOL_VERYTHICK: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_VERYTHICK: 3>
    __entries: dict # value = {'Aspect_WOL_THIN': (<Aspect_WidthOfLine.Aspect_WOL_THIN: 0>, None), 'Aspect_WOL_MEDIUM': (<Aspect_WidthOfLine.Aspect_WOL_MEDIUM: 1>, None), 'Aspect_WOL_THICK': (<Aspect_WidthOfLine.Aspect_WOL_THICK: 2>, None), 'Aspect_WOL_VERYTHICK': (<Aspect_WidthOfLine.Aspect_WOL_VERYTHICK: 3>, None), 'Aspect_WOL_USERDEFINED': (<Aspect_WidthOfLine.Aspect_WOL_USERDEFINED: 4>, None)}
    __members__: dict # value = {'Aspect_WOL_THIN': <Aspect_WidthOfLine.Aspect_WOL_THIN: 0>, 'Aspect_WOL_MEDIUM': <Aspect_WidthOfLine.Aspect_WOL_MEDIUM: 1>, 'Aspect_WOL_THICK': <Aspect_WidthOfLine.Aspect_WOL_THICK: 2>, 'Aspect_WOL_VERYTHICK': <Aspect_WidthOfLine.Aspect_WOL_VERYTHICK: 3>, 'Aspect_WOL_USERDEFINED': <Aspect_WidthOfLine.Aspect_WOL_USERDEFINED: 4>}
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
    def ConvertPointFromBacking(self,thePnt : OCP.Graphic3d.Graphic3d_Vec2d) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        Convert point from backing store units to logical units.
        """
    def ConvertPointToBacking(self,thePnt : OCP.Graphic3d.Graphic3d_Vec2d) -> OCP.Graphic3d.Graphic3d_Vec2d: 
        """
        Convert point from logical units into backing store units.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DevicePixelRatio(self) -> float: 
        """
        Return device pixel ratio (logical to backing store scale factor).
        """
    def DisplayConnection(self) -> Aspect_DisplayConnection: 
        """
        Returns connection to Display or NULL.
        """
    def DoMapping(self) -> bool: 
        """
        Map window - do nothing.
        """
    def DoResize(self) -> Aspect_TypeOfResize: 
        """
        Resize window - do nothing.
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
    def NativeHandle(self) -> capsule: 
        """
        Return native handle of this drawable.
        """
    def NativeParentHandle(self) -> capsule: 
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
    def SetBackground(self,ABackground : Aspect_GradientBackground) -> None: ...
    @overload
    def SetBackground(self,ABack : Aspect_Background) -> None: ...
    @overload
    def SetBackground(self,theFirstColor : OCP.Quantity.Quantity_Color,theSecondColor : OCP.Quantity.Quantity_Color,theFillMethod : Aspect_GradientFillMethod) -> None: ...
    def SetNativeHandle(self,theWindow : capsule) -> bool: 
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
class Aspect_WindowInputListener():
    """
    Defines a listener for window input events.
    """
    def AddTouchPoint(self,theId : int,thePnt : OCP.Graphic3d.Graphic3d_Vec2d,theClearBefore : bool=False) -> None: 
        """
        Add touch point with the given ID. This method is expected to be called from UI thread.
        """
    def Change3dMouseIsNoRotate(self) -> Any: 
        """
        Return 3d mouse rotation axes (tilt/roll/spin) ignore flag; (FALSE, FALSE, FALSE) by default.
        """
    def Change3dMouseToReverse(self) -> Any: 
        """
        Return 3d mouse rotation axes (tilt/roll/spin) reverse flag; (TRUE, FALSE, FALSE) by default.
        """
    def ChangeKeys(self) -> Aspect_VKeySet: 
        """
        Return keyboard state.
        """
    def EventTime(self) -> float: 
        """
        Return event time (e.g. current time).
        """
    def Get3dMouseIsNoRotate(self) -> Any: 
        """
        Return 3d mouse rotation axes (tilt/roll/spin) ignore flag; (FALSE, FALSE, FALSE) by default.
        """
    def Get3dMouseRotationScale(self) -> float: 
        """
        Return acceleration ratio for rotation event; 4.0 by default.
        """
    def Get3dMouseToReverse(self) -> Any: 
        """
        Return 3d mouse rotation axes (tilt/roll/spin) reverse flag; (TRUE, FALSE, FALSE) by default.
        """
    def Get3dMouseTranslationScale(self) -> float: 
        """
        Return acceleration ratio for translation event; 2.0 by default.
        """
    def HasTouchPoints(self) -> bool: 
        """
        Return TRUE if touches map is not empty.
        """
    def KeyDown(self,theKey : int,theTime : float,thePressure : float=1.0) -> None: 
        """
        Press key. Default implementation updates internal cache.
        """
    def KeyFromAxis(self,theNegative : int,thePositive : int,theTime : float,thePressure : float) -> None: 
        """
        Simulate key up/down events from axis value. Default implementation updates internal cache.
        """
    def KeyUp(self,theKey : int,theTime : float) -> None: 
        """
        Release key. Default implementation updates internal cache.
        """
    def Keys(self) -> Aspect_VKeySet: 
        """
        Return keyboard state.
        """
    def LastMouseFlags(self) -> int: 
        """
        Return active key modifiers passed with last mouse event.
        """
    def LastMousePosition(self) -> OCP.Graphic3d.Graphic3d_Vec2i: 
        """
        Return last mouse position.
        """
    def PressMouseButton(self,thePoint : OCP.Graphic3d.Graphic3d_Vec2i,theButton : int,theModifiers : int,theIsEmulated : bool) -> bool: 
        """
        Handle mouse button press event. This method is expected to be called from UI thread. Default implementation redirects to UpdateMousePosition().
        """
    def PressedMouseButtons(self) -> int: 
        """
        Return currently pressed mouse buttons.
        """
    def ProcessClose(self) -> None: 
        """
        Handle window close event.
        """
    def ProcessConfigure(self,theIsResized : bool) -> None: 
        """
        Handle window resize event.
        """
    def ProcessExpose(self) -> None: 
        """
        Handle expose event (window content has been invalidation and should be redrawn).
        """
    def ProcessFocus(self,theIsActivated : bool) -> None: 
        """
        Handle focus event.
        """
    def ProcessInput(self) -> None: 
        """
        Handle window input event immediately (flush input buffer or ignore).
        """
    def ReleaseMouseButton(self,thePoint : OCP.Graphic3d.Graphic3d_Vec2i,theButton : int,theModifiers : int,theIsEmulated : bool) -> bool: 
        """
        Handle mouse button release event. This method is expected to be called from UI thread. Default implementation redirects to UpdateMousePosition().
        """
    def RemoveTouchPoint(self,theId : int,theClearSelectPnts : bool=False) -> bool: 
        """
        Remove touch point with the given ID. This method is expected to be called from UI thread.
        """
    def Set3dMousePreciseInput(self,theIsQuadric : bool) -> None: 
        """
        Set quadric acceleration flag.
        """
    def Set3dMouseRotationScale(self,theScale : float) -> None: 
        """
        Set acceleration ratio for rotation event.
        """
    def Set3dMouseTranslationScale(self,theScale : float) -> None: 
        """
        Set acceleration ratio for translation event.
        """
    def To3dMousePreciseInput(self) -> bool: 
        """
        Return quadric acceleration flag; TRUE by default.
        """
    def TouchPoints(self) -> Aspect_TouchMap: 
        """
        Return map of active touches.
        """
    def Update3dMouse(self,theEvent : OCP.WNT.WNT_HIDSpaceMouse) -> bool: 
        """
        Process 3d mouse input event (redirects to translation, rotation and keys).
        """
    def UpdateMouseButtons(self,thePoint : OCP.Graphic3d.Graphic3d_Vec2i,theButtons : int,theModifiers : int,theIsEmulated : bool) -> bool: 
        """
        Handle mouse button press/release event. This method is expected to be called from UI thread.
        """
    def UpdateMousePosition(self,thePoint : OCP.Graphic3d.Graphic3d_Vec2i,theButtons : int,theModifiers : int,theIsEmulated : bool) -> bool: 
        """
        Handle mouse cursor movement event. This method is expected to be called from UI thread. Default implementation does nothing.
        """
    def UpdateMouseScroll(self,theDelta : Aspect_ScrollDelta) -> bool: 
        """
        Update mouse scroll event. This method is expected to be called from UI thread.
        """
    def UpdateTouchPoint(self,theId : int,thePnt : OCP.Graphic3d.Graphic3d_Vec2d) -> None: 
        """
        Update touch point with the given ID. If point with specified ID was not registered before, it will be added. This method is expected to be called from UI thread.
        """
    def update3dMouseKeys(self,theEvent : OCP.WNT.WNT_HIDSpaceMouse) -> bool: 
        """
        Process 3d mouse input keys event.
        """
    def update3dMouseRotation(self,theEvent : OCP.WNT.WNT_HIDSpaceMouse) -> bool: 
        """
        Process 3d mouse input rotation event.
        """
    def update3dMouseTranslation(self,theEvent : OCP.WNT.WNT_HIDSpaceMouse) -> bool: 
        """
        Process 3d mouse input translation event.
        """
    pass
class Aspect_XAtom():
    """
    Defines custom identifiers(atoms) for X window custom named properties

    Members:

      Aspect_XA_DELETE_WINDOW
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
    Aspect_XA_DELETE_WINDOW: OCP.Aspect.Aspect_XAtom # value = <Aspect_XAtom.Aspect_XA_DELETE_WINDOW: 0>
    __entries: dict # value = {'Aspect_XA_DELETE_WINDOW': (<Aspect_XAtom.Aspect_XA_DELETE_WINDOW: 0>, None)}
    __members__: dict # value = {'Aspect_XA_DELETE_WINDOW': <Aspect_XAtom.Aspect_XA_DELETE_WINDOW: 0>}
    pass
class Aspect_XRAction(OCP.Standard.Standard_Transient):
    """
    XR action definition.
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
    def Id(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return action id.
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
    def IsValid(self) -> bool: 
        """
        Return TRUE if action is defined.
        """
    def RawHandle(self) -> int: 
        """
        Return action handle.
        """
    def SetRawHandle(self,theHande : int) -> None: 
        """
        Set action handle.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Aspect_XRActionType: 
        """
        Return action type.
        """
    def __init__(self,theId : OCP.TCollection.TCollection_AsciiString,theType : Aspect_XRActionType) -> None: ...
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
class Aspect_XRActionSet(OCP.Standard.Standard_Transient):
    """
    XR action set.
    """
    def Actions(self) -> Any: 
        """
        Return map of actions.
        """
    def AddAction(self,theAction : Aspect_XRAction) -> None: 
        """
        Add action.
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
    def Id(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return action id.
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
    def RawHandle(self) -> int: 
        """
        Return action handle.
        """
    def SetRawHandle(self,theHande : int) -> None: 
        """
        Set action handle.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theId : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Aspect_XRActionType():
    """
    XR action type.

    Members:

      Aspect_XRActionType_InputDigital

      Aspect_XRActionType_InputAnalog

      Aspect_XRActionType_InputPose

      Aspect_XRActionType_InputSkeletal

      Aspect_XRActionType_OutputHaptic
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
    Aspect_XRActionType_InputAnalog: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_InputAnalog: 1>
    Aspect_XRActionType_InputDigital: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_InputDigital: 0>
    Aspect_XRActionType_InputPose: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_InputPose: 2>
    Aspect_XRActionType_InputSkeletal: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_InputSkeletal: 3>
    Aspect_XRActionType_OutputHaptic: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_OutputHaptic: 4>
    __entries: dict # value = {'Aspect_XRActionType_InputDigital': (<Aspect_XRActionType.Aspect_XRActionType_InputDigital: 0>, None), 'Aspect_XRActionType_InputAnalog': (<Aspect_XRActionType.Aspect_XRActionType_InputAnalog: 1>, None), 'Aspect_XRActionType_InputPose': (<Aspect_XRActionType.Aspect_XRActionType_InputPose: 2>, None), 'Aspect_XRActionType_InputSkeletal': (<Aspect_XRActionType.Aspect_XRActionType_InputSkeletal: 3>, None), 'Aspect_XRActionType_OutputHaptic': (<Aspect_XRActionType.Aspect_XRActionType_OutputHaptic: 4>, None)}
    __members__: dict # value = {'Aspect_XRActionType_InputDigital': <Aspect_XRActionType.Aspect_XRActionType_InputDigital: 0>, 'Aspect_XRActionType_InputAnalog': <Aspect_XRActionType.Aspect_XRActionType_InputAnalog: 1>, 'Aspect_XRActionType_InputPose': <Aspect_XRActionType.Aspect_XRActionType_InputPose: 2>, 'Aspect_XRActionType_InputSkeletal': <Aspect_XRActionType.Aspect_XRActionType_InputSkeletal: 3>, 'Aspect_XRActionType_OutputHaptic': <Aspect_XRActionType.Aspect_XRActionType_OutputHaptic: 4>}
    pass
class Aspect_XRAnalogActionData():
    """
    Analog input XR action data.
    """
    def IsChanged(self) -> bool: 
        """
        Return TRUE if delta is non-zero.
        """
    def __init__(self) -> None: ...
    pass
class Aspect_XRDigitalActionData():
    """
    Digital input XR action data.
    """
    def __init__(self) -> None: ...
    pass
class Aspect_XRGenericAction():
    """
    Generic XR action.

    Members:

      Aspect_XRGenericAction_IsHeadsetOn

      Aspect_XRGenericAction_InputAppMenu

      Aspect_XRGenericAction_InputSysMenu

      Aspect_XRGenericAction_InputTriggerPull

      Aspect_XRGenericAction_InputTriggerClick

      Aspect_XRGenericAction_InputGripClick

      Aspect_XRGenericAction_InputTrackPadPosition

      Aspect_XRGenericAction_InputTrackPadTouch

      Aspect_XRGenericAction_InputTrackPadClick

      Aspect_XRGenericAction_InputThumbstickPosition

      Aspect_XRGenericAction_InputThumbstickTouch

      Aspect_XRGenericAction_InputThumbstickClick

      Aspect_XRGenericAction_InputPoseBase

      Aspect_XRGenericAction_InputPoseFront

      Aspect_XRGenericAction_InputPoseHandGrip

      Aspect_XRGenericAction_InputPoseFingerTip

      Aspect_XRGenericAction_OutputHaptic
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
    Aspect_XRGenericAction_InputAppMenu: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputAppMenu: 1>
    Aspect_XRGenericAction_InputGripClick: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputGripClick: 5>
    Aspect_XRGenericAction_InputPoseBase: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseBase: 12>
    Aspect_XRGenericAction_InputPoseFingerTip: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseFingerTip: 15>
    Aspect_XRGenericAction_InputPoseFront: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseFront: 13>
    Aspect_XRGenericAction_InputPoseHandGrip: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseHandGrip: 14>
    Aspect_XRGenericAction_InputSysMenu: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputSysMenu: 2>
    Aspect_XRGenericAction_InputThumbstickClick: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickClick: 11>
    Aspect_XRGenericAction_InputThumbstickPosition: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickPosition: 9>
    Aspect_XRGenericAction_InputThumbstickTouch: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickTouch: 10>
    Aspect_XRGenericAction_InputTrackPadClick: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadClick: 8>
    Aspect_XRGenericAction_InputTrackPadPosition: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadPosition: 6>
    Aspect_XRGenericAction_InputTrackPadTouch: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadTouch: 7>
    Aspect_XRGenericAction_InputTriggerClick: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTriggerClick: 4>
    Aspect_XRGenericAction_InputTriggerPull: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTriggerPull: 3>
    Aspect_XRGenericAction_IsHeadsetOn: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_IsHeadsetOn: 0>
    Aspect_XRGenericAction_OutputHaptic: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_OutputHaptic: 16>
    __entries: dict # value = {'Aspect_XRGenericAction_IsHeadsetOn': (<Aspect_XRGenericAction.Aspect_XRGenericAction_IsHeadsetOn: 0>, None), 'Aspect_XRGenericAction_InputAppMenu': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputAppMenu: 1>, None), 'Aspect_XRGenericAction_InputSysMenu': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputSysMenu: 2>, None), 'Aspect_XRGenericAction_InputTriggerPull': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputTriggerPull: 3>, None), 'Aspect_XRGenericAction_InputTriggerClick': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputTriggerClick: 4>, None), 'Aspect_XRGenericAction_InputGripClick': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputGripClick: 5>, None), 'Aspect_XRGenericAction_InputTrackPadPosition': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadPosition: 6>, None), 'Aspect_XRGenericAction_InputTrackPadTouch': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadTouch: 7>, None), 'Aspect_XRGenericAction_InputTrackPadClick': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadClick: 8>, None), 'Aspect_XRGenericAction_InputThumbstickPosition': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickPosition: 9>, None), 'Aspect_XRGenericAction_InputThumbstickTouch': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickTouch: 10>, None), 'Aspect_XRGenericAction_InputThumbstickClick': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickClick: 11>, None), 'Aspect_XRGenericAction_InputPoseBase': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseBase: 12>, None), 'Aspect_XRGenericAction_InputPoseFront': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseFront: 13>, None), 'Aspect_XRGenericAction_InputPoseHandGrip': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseHandGrip: 14>, None), 'Aspect_XRGenericAction_InputPoseFingerTip': (<Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseFingerTip: 15>, None), 'Aspect_XRGenericAction_OutputHaptic': (<Aspect_XRGenericAction.Aspect_XRGenericAction_OutputHaptic: 16>, None)}
    __members__: dict # value = {'Aspect_XRGenericAction_IsHeadsetOn': <Aspect_XRGenericAction.Aspect_XRGenericAction_IsHeadsetOn: 0>, 'Aspect_XRGenericAction_InputAppMenu': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputAppMenu: 1>, 'Aspect_XRGenericAction_InputSysMenu': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputSysMenu: 2>, 'Aspect_XRGenericAction_InputTriggerPull': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTriggerPull: 3>, 'Aspect_XRGenericAction_InputTriggerClick': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTriggerClick: 4>, 'Aspect_XRGenericAction_InputGripClick': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputGripClick: 5>, 'Aspect_XRGenericAction_InputTrackPadPosition': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadPosition: 6>, 'Aspect_XRGenericAction_InputTrackPadTouch': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadTouch: 7>, 'Aspect_XRGenericAction_InputTrackPadClick': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadClick: 8>, 'Aspect_XRGenericAction_InputThumbstickPosition': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickPosition: 9>, 'Aspect_XRGenericAction_InputThumbstickTouch': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickTouch: 10>, 'Aspect_XRGenericAction_InputThumbstickClick': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickClick: 11>, 'Aspect_XRGenericAction_InputPoseBase': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseBase: 12>, 'Aspect_XRGenericAction_InputPoseFront': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseFront: 13>, 'Aspect_XRGenericAction_InputPoseHandGrip': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseHandGrip: 14>, 'Aspect_XRGenericAction_InputPoseFingerTip': <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseFingerTip: 15>, 'Aspect_XRGenericAction_OutputHaptic': <Aspect_XRGenericAction.Aspect_XRGenericAction_OutputHaptic: 16>}
    pass
class Aspect_XRHapticActionData():
    """
    Haptic output XR action data.
    """
    def IsValid(self) -> bool: 
        """
        Return TRUE if data is not empty.
        """
    def __init__(self) -> None: ...
    pass
class Aspect_XRPoseActionData():
    """
    Pose input XR action data.
    """
    def __init__(self) -> None: ...
    @property
    def Pose(self) -> Aspect_TrackedDevicePose:
        """
        :type: Aspect_TrackedDevicePose
        """
    @Pose.setter
    def Pose(self, arg0: Aspect_TrackedDevicePose) -> None:
        pass
    pass
class Aspect_OpenVRSession(Aspect_XRSession, OCP.Standard.Standard_Transient):
    """
    OpenVR wrapper implementing Aspect_XRSession interface.
    """
    class InfoString_e():
        """
        Info string enumeration.

        Members:

          InfoString_Vendor

          InfoString_Device

          InfoString_Tracker

          InfoString_SerialNumber
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
        InfoString_Device: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_Device: 1>
        InfoString_SerialNumber: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_SerialNumber: 3>
        InfoString_Tracker: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_Tracker: 2>
        InfoString_Vendor: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_Vendor: 0>
        __entries: dict # value = {'InfoString_Vendor': (<InfoString_e.InfoString_Vendor: 0>, None), 'InfoString_Device': (<InfoString_e.InfoString_Device: 1>, None), 'InfoString_Tracker': (<InfoString_e.InfoString_Tracker: 2>, None), 'InfoString_SerialNumber': (<InfoString_e.InfoString_SerialNumber: 3>, None)}
        __members__: dict # value = {'InfoString_Vendor': <InfoString_e.InfoString_Vendor: 0>, 'InfoString_Device': <InfoString_e.InfoString_Device: 1>, 'InfoString_Tracker': <InfoString_e.InfoString_Tracker: 2>, 'InfoString_SerialNumber': <InfoString_e.InfoString_SerialNumber: 3>}
        pass
    class TrackingUniverseOrigin_e():
        """
        Identifies which style of tracking origin the application wants to use for the poses it is requesting.

        Members:

          TrackingUniverseOrigin_Seated

          TrackingUniverseOrigin_Standing
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
        TrackingUniverseOrigin_Seated: OCP.Aspect.TrackingUniverseOrigin_e # value = <TrackingUniverseOrigin_e.TrackingUniverseOrigin_Seated: 0>
        TrackingUniverseOrigin_Standing: OCP.Aspect.TrackingUniverseOrigin_e # value = <TrackingUniverseOrigin_e.TrackingUniverseOrigin_Standing: 1>
        __entries: dict # value = {'TrackingUniverseOrigin_Seated': (<TrackingUniverseOrigin_e.TrackingUniverseOrigin_Seated: 0>, None), 'TrackingUniverseOrigin_Standing': (<TrackingUniverseOrigin_e.TrackingUniverseOrigin_Standing: 1>, None)}
        __members__: dict # value = {'TrackingUniverseOrigin_Seated': <TrackingUniverseOrigin_e.TrackingUniverseOrigin_Seated: 0>, 'TrackingUniverseOrigin_Standing': <TrackingUniverseOrigin_e.TrackingUniverseOrigin_Standing: 1>}
        pass
    def AbortHapticVibrationAction(self,theAction : Aspect_XRAction) -> None: 
        """
        Abort vibration.
        """
    def Aspect(self) -> float: 
        """
        Return aspect ratio.
        """
    def Close(self) -> None: 
        """
        Release session.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisplayFrequency(self) -> float: 
        """
        Return display frequency or 0 if unknown.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EyeToHeadTransform(self,theEye : Aspect_Eye) -> OCP.Graphic3d.Graphic3d_Mat4d: 
        """
        Return transformation from eye to head. vr::GetEyeToHeadTransform() wrapper.
        """
    def FieldOfView(self) -> float: 
        """
        Return field of view.
        """
    def GenericAction(self,theDevice : Aspect_XRTrackedDeviceRole,theAction : Aspect_XRGenericAction) -> Aspect_XRAction: 
        """
        Return generic action for specific hand or NULL if undefined.
        """
    def GetAnalogActionData(self,theAction : Aspect_XRAction) -> Aspect_XRAnalogActionData: 
        """
        Fetch data for analog input action (like axis).
        """
    def GetDigitalActionData(self,theAction : Aspect_XRAction) -> Aspect_XRDigitalActionData: 
        """
        Fetch data for digital input action (like button).
        """
    def GetPoseActionDataForNextFrame(self,theAction : Aspect_XRAction) -> Aspect_XRPoseActionData: 
        """
        Fetch data for pose input action (like fingertip position).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetString(self,theInfo : Aspect_XRSession.InfoString_e) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Query information.
        """
    def HasProjectionFrustums(self) -> bool: 
        """
        Return TRUE.
        """
    def HasTrackedPose(self,theDevice : int) -> bool: 
        """
        Return TRUE if device orientation is defined.
        """
    def HeadPose(self) -> OCP.gp.gp_Trsf: 
        """
        Return head orientation in right-handed system: +y is up +x is to the right -z is forward Distance unit is meters by default (
        """
    def HeadToEyeTransform(self,theEye : Aspect_Eye) -> OCP.Graphic3d.Graphic3d_Mat4d: 
        """
        Return transformation from head to eye.
        """
    def IOD(self) -> float: 
        """
        Return Intra-ocular Distance (IOD); also known as Interpupillary Distance (IPD). Defined in meters by default (
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @staticmethod
    def IsHmdPresent_s() -> bool: 
        """
        Return TRUE if an HMD may be presented on the system (e.g. to show VR checkbox in application GUI). This is fast check, and even if it returns TRUE, opening session may fail.
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
    def IsOpen(self) -> bool: 
        """
        Return TRUE if session is opened.
        """
    def LeftHandPose(self) -> OCP.gp.gp_Trsf: 
        """
        Return left hand orientation.
        """
    @overload
    def LoadRenderModel(self,theDevice : int,theTexture : OCP.Image.Image_Texture) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: 
        """
        Load model for displaying device.

        Load model for displaying device.
        """
    @overload
    def LoadRenderModel(self,theDevice : int,theToApplyUnitFactor : bool,theTexture : OCP.Image.Image_Texture) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: ...
    def NamedTrackedDevice(self,theDevice : Aspect_XRTrackedDeviceRole) -> int: 
        """
        Return index of tracked device of known role.
        """
    def Open(self) -> bool: 
        """
        Initialize session.
        """
    def ProcessEvents(self) -> None: 
        """
        Receive XR events.
        """
    def ProjectionFrustum(self,theEye : Aspect_Eye) -> Any: 
        """
        Return projection frustum.
        """
    def ProjectionMatrix(self,theEye : Aspect_Eye,theZNear : float,theZFar : float) -> OCP.Graphic3d.Graphic3d_Mat4d: 
        """
        Return projection matrix.
        """
    def RecommendedViewport(self) -> OCP.Graphic3d.Graphic3d_Vec2i: 
        """
        Return recommended viewport Width x Height for rendering into VR.
        """
    def RightHandPose(self) -> OCP.gp.gp_Trsf: 
        """
        Return right hand orientation.
        """
    def SetTrackingOrigin(self,theOrigin : Aspect_XRSession.TrackingUniverseOrigin_e) -> None: 
        """
        Set tracking origin.
        """
    def SetUnitFactor(self,theFactor : float) -> None: 
        """
        Set unit scale factor.
        """
    def SubmitEye(self,theTexture : capsule,theGraphicsLib : Aspect_GraphicsLibrary,theColorSpace : Aspect_ColorSpace,theEye : Aspect_Eye) -> bool: 
        """
        Submit texture eye to XR Composer.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TrackedPoses(self) -> Aspect_TrackedDevicePoseArray: 
        """
        Return number of tracked poses array.
        """
    def TrackingOrigin(self) -> Aspect_XRSession.TrackingUniverseOrigin_e: 
        """
        Return tracking origin.
        """
    def TriggerHapticVibrationAction(self,theAction : Aspect_XRAction,theParams : Aspect_XRHapticActionData) -> None: 
        """
        Trigger vibration.
        """
    def UnitFactor(self) -> float: 
        """
        Return unit scale factor defined as scale factor for m (meters); 1.0 by default.
        """
    def WaitPoses(self) -> bool: 
        """
        Fetch actual poses of tracked devices.
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
    InfoString_Device: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_Device: 1>
    InfoString_SerialNumber: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_SerialNumber: 3>
    InfoString_Tracker: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_Tracker: 2>
    InfoString_Vendor: OCP.Aspect.InfoString_e # value = <InfoString_e.InfoString_Vendor: 0>
    TrackingUniverseOrigin_Seated: OCP.Aspect.TrackingUniverseOrigin_e # value = <TrackingUniverseOrigin_e.TrackingUniverseOrigin_Seated: 0>
    TrackingUniverseOrigin_Standing: OCP.Aspect.TrackingUniverseOrigin_e # value = <TrackingUniverseOrigin_e.TrackingUniverseOrigin_Standing: 1>
    pass
class Aspect_XRTrackedDeviceRole():
    """
    Predefined tracked devices.

    Members:

      Aspect_XRTrackedDeviceRole_Head

      Aspect_XRTrackedDeviceRole_LeftHand

      Aspect_XRTrackedDeviceRole_RightHand

      Aspect_XRTrackedDeviceRole_Other
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
    Aspect_XRTrackedDeviceRole_Head: OCP.Aspect.Aspect_XRTrackedDeviceRole # value = <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_Head: 0>
    Aspect_XRTrackedDeviceRole_LeftHand: OCP.Aspect.Aspect_XRTrackedDeviceRole # value = <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_LeftHand: 1>
    Aspect_XRTrackedDeviceRole_Other: OCP.Aspect.Aspect_XRTrackedDeviceRole # value = <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_Other: 3>
    Aspect_XRTrackedDeviceRole_RightHand: OCP.Aspect.Aspect_XRTrackedDeviceRole # value = <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_RightHand: 2>
    __entries: dict # value = {'Aspect_XRTrackedDeviceRole_Head': (<Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_Head: 0>, None), 'Aspect_XRTrackedDeviceRole_LeftHand': (<Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_LeftHand: 1>, None), 'Aspect_XRTrackedDeviceRole_RightHand': (<Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_RightHand: 2>, None), 'Aspect_XRTrackedDeviceRole_Other': (<Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_Other: 3>, None)}
    __members__: dict # value = {'Aspect_XRTrackedDeviceRole_Head': <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_Head: 0>, 'Aspect_XRTrackedDeviceRole_LeftHand': <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_LeftHand: 1>, 'Aspect_XRTrackedDeviceRole_RightHand': <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_RightHand: 2>, 'Aspect_XRTrackedDeviceRole_Other': <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_Other: 3>}
    pass
def Aspect_VKey2Modifier(theKey : int) -> int:
    """
    Return modifier flags for specified modifier key.
    """
Aspect_ColorSpace_Linear: OCP.Aspect.Aspect_ColorSpace # value = <Aspect_ColorSpace.Aspect_ColorSpace_Linear: 1>
Aspect_ColorSpace_sRGB: OCP.Aspect.Aspect_ColorSpace # value = <Aspect_ColorSpace.Aspect_ColorSpace_sRGB: 0>
Aspect_Eye_Left: OCP.Aspect.Aspect_Eye # value = <Aspect_Eye.Aspect_Eye_Left: 0>
Aspect_Eye_Right: OCP.Aspect.Aspect_Eye # value = <Aspect_Eye.Aspect_Eye_Right: 1>
Aspect_FM_CENTERED: OCP.Aspect.Aspect_FillMethod # value = <Aspect_FillMethod.Aspect_FM_CENTERED: 1>
Aspect_FM_NONE: OCP.Aspect.Aspect_FillMethod # value = <Aspect_FillMethod.Aspect_FM_NONE: 0>
Aspect_FM_STRETCH: OCP.Aspect.Aspect_FillMethod # value = <Aspect_FillMethod.Aspect_FM_STRETCH: 3>
Aspect_FM_TILED: OCP.Aspect.Aspect_FillMethod # value = <Aspect_FillMethod.Aspect_FM_TILED: 2>
Aspect_GDM_Lines: OCP.Aspect.Aspect_GridDrawMode # value = <Aspect_GridDrawMode.Aspect_GDM_Lines: 0>
Aspect_GDM_None: OCP.Aspect.Aspect_GridDrawMode # value = <Aspect_GridDrawMode.Aspect_GDM_None: 2>
Aspect_GDM_Points: OCP.Aspect.Aspect_GridDrawMode # value = <Aspect_GridDrawMode.Aspect_GDM_Points: 1>
Aspect_GFM_CORNER1: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner1: 5>
Aspect_GFM_CORNER2: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner2: 6>
Aspect_GFM_CORNER3: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner3: 7>
Aspect_GFM_CORNER4: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner4: 8>
Aspect_GFM_DIAG1: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal1: 3>
Aspect_GFM_DIAG2: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal2: 4>
Aspect_GFM_HOR: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal: 1>
Aspect_GFM_NONE: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_None: 0>
Aspect_GFM_VER: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Vertical: 2>
Aspect_GT_Circular: OCP.Aspect.Aspect_GridType # value = <Aspect_GridType.Aspect_GT_Circular: 1>
Aspect_GT_Rectangular: OCP.Aspect.Aspect_GridType # value = <Aspect_GridType.Aspect_GT_Rectangular: 0>
Aspect_GradientFillMethod_Corner1: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner1: 5>
Aspect_GradientFillMethod_Corner2: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner2: 6>
Aspect_GradientFillMethod_Corner3: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner3: 7>
Aspect_GradientFillMethod_Corner4: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Corner4: 8>
Aspect_GradientFillMethod_Diagonal1: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal1: 3>
Aspect_GradientFillMethod_Diagonal2: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Diagonal2: 4>
Aspect_GradientFillMethod_Elliptical: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Elliptical: 9>
Aspect_GradientFillMethod_Horizontal: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Horizontal: 1>
Aspect_GradientFillMethod_None: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_None: 0>
Aspect_GradientFillMethod_Vertical: OCP.Aspect.Aspect_GradientFillMethod # value = <Aspect_GradientFillMethod.Aspect_GradientFillMethod_Vertical: 2>
Aspect_GraphicsLibrary_OpenGL: OCP.Aspect.Aspect_GraphicsLibrary # value = <Aspect_GraphicsLibrary.Aspect_GraphicsLibrary_OpenGL: 0>
Aspect_GraphicsLibrary_OpenGLES: OCP.Aspect.Aspect_GraphicsLibrary # value = <Aspect_GraphicsLibrary.Aspect_GraphicsLibrary_OpenGLES: 1>
Aspect_HS_DIAGONAL_135: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_DIAGONAL_135: 6>
Aspect_HS_DIAGONAL_135_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_DIAGONAL_135_WIDE: 10>
Aspect_HS_DIAGONAL_45: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_DIAGONAL_45: 5>
Aspect_HS_DIAGONAL_45_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_DIAGONAL_45_WIDE: 9>
Aspect_HS_GRID: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_GRID: 3>
Aspect_HS_GRID_DIAGONAL: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL: 1>
Aspect_HS_GRID_DIAGONAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL_WIDE: 2>
Aspect_HS_GRID_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_GRID_WIDE: 4>
Aspect_HS_HORIZONTAL: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_HORIZONTAL: 7>
Aspect_HS_HORIZONTAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_HORIZONTAL_WIDE: 11>
Aspect_HS_NB: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_NB: 13>
Aspect_HS_SOLID: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_SOLID: 0>
Aspect_HS_VERTICAL: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_VERTICAL: 8>
Aspect_HS_VERTICAL_WIDE: OCP.Aspect.Aspect_HatchStyle # value = <Aspect_HatchStyle.Aspect_HS_VERTICAL_WIDE: 12>
Aspect_IS_EMPTY: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_EMPTY: -1>
Aspect_IS_HATCH: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_HATCH: 1>
Aspect_IS_HIDDENLINE: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_HIDDENLINE: 2>
Aspect_IS_HOLLOW: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_EMPTY: -1>
Aspect_IS_POINT: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_POINT: 3>
Aspect_IS_SOLID: OCP.Aspect.Aspect_InteriorStyle # value = <Aspect_InteriorStyle.Aspect_IS_SOLID: 0>
Aspect_POM_All: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_All: 7>
Aspect_POM_Fill: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Fill: 1>
Aspect_POM_Line: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Line: 2>
Aspect_POM_Mask: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Mask: 15>
Aspect_POM_None: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_None: 8>
Aspect_POM_Off: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Off: 0>
Aspect_POM_Point: OCP.Aspect.Aspect_PolygonOffsetMode # value = <Aspect_PolygonOffsetMode.Aspect_POM_Point: 4>
Aspect_TOCSD_AUTO: OCP.Aspect.Aspect_TypeOfColorScaleData # value = <Aspect_TypeOfColorScaleData.Aspect_TOCSD_AUTO: 0>
Aspect_TOCSD_USER: OCP.Aspect.Aspect_TypeOfColorScaleData # value = <Aspect_TypeOfColorScaleData.Aspect_TOCSD_USER: 1>
Aspect_TOCSO_CENTER: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_CENTER: 3>
Aspect_TOCSO_LEFT: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_LEFT: 1>
Aspect_TOCSO_NONE: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_NONE: 0>
Aspect_TOCSO_RIGHT: OCP.Aspect.Aspect_TypeOfColorScaleOrientation # value = <Aspect_TypeOfColorScaleOrientation.Aspect_TOCSO_RIGHT: 2>
Aspect_TOCSP_CENTER: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_CENTER: 3>
Aspect_TOCSP_LEFT: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_LEFT: 1>
Aspect_TOCSP_NONE: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_NONE: 0>
Aspect_TOCSP_RIGHT: OCP.Aspect.Aspect_TypeOfColorScalePosition # value = <Aspect_TypeOfColorScalePosition.Aspect_TOCSP_RIGHT: 2>
Aspect_TODT_BLEND: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_BLEND: 3>
Aspect_TODT_DEKALE: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_DEKALE: 2>
Aspect_TODT_DIMENSION: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_DIMENSION: 4>
Aspect_TODT_NORMAL: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL: 0>
Aspect_TODT_SHADOW: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_SHADOW: 5>
Aspect_TODT_SUBTITLE: OCP.Aspect.Aspect_TypeOfDisplayText # value = <Aspect_TypeOfDisplayText.Aspect_TODT_SUBTITLE: 1>
Aspect_TOD_ABSOLUTE: OCP.Aspect.Aspect_TypeOfDeflection # value = <Aspect_TypeOfDeflection.Aspect_TOD_ABSOLUTE: 1>
Aspect_TOD_RELATIVE: OCP.Aspect.Aspect_TypeOfDeflection # value = <Aspect_TypeOfDeflection.Aspect_TOD_RELATIVE: 0>
Aspect_TOFM_BACK_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = <Aspect_TypeOfFacingModel.Aspect_TOFM_BACK_SIDE: 1>
Aspect_TOFM_BOTH_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = <Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE: 0>
Aspect_TOFM_FRONT_SIDE: OCP.Aspect.Aspect_TypeOfFacingModel # value = <Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE: 2>
Aspect_TOHM_BOUNDBOX: OCP.Aspect.Aspect_TypeOfHighlightMethod # value = <Aspect_TypeOfHighlightMethod.Aspect_TOHM_BOUNDBOX: 1>
Aspect_TOHM_COLOR: OCP.Aspect.Aspect_TypeOfHighlightMethod # value = <Aspect_TypeOfHighlightMethod.Aspect_TOHM_COLOR: 0>
Aspect_TOL_DASH: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_DASH: 1>
Aspect_TOL_DOT: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_DOT: 2>
Aspect_TOL_DOTDASH: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_DOTDASH: 3>
Aspect_TOL_EMPTY: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_EMPTY: -1>
Aspect_TOL_SOLID: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_SOLID: 0>
Aspect_TOL_USERDEFINED: OCP.Aspect.Aspect_TypeOfLine # value = <Aspect_TypeOfLine.Aspect_TOL_USERDEFINED: 4>
Aspect_TOM_BALL: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_BALL: 12>
Aspect_TOM_EMPTY: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_EMPTY: -1>
Aspect_TOM_O: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O: 4>
Aspect_TOM_O_PLUS: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O_PLUS: 6>
Aspect_TOM_O_POINT: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O_POINT: 5>
Aspect_TOM_O_STAR: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O_STAR: 7>
Aspect_TOM_O_X: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_O_X: 8>
Aspect_TOM_PLUS: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_PLUS: 1>
Aspect_TOM_POINT: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_POINT: 0>
Aspect_TOM_RING1: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_RING1: 9>
Aspect_TOM_RING2: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_RING2: 10>
Aspect_TOM_RING3: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_RING3: 11>
Aspect_TOM_STAR: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_STAR: 2>
Aspect_TOM_USERDEFINED: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_USERDEFINED: 13>
Aspect_TOM_X: OCP.Aspect.Aspect_TypeOfMarker # value = <Aspect_TypeOfMarker.Aspect_TOM_X: 3>
Aspect_TOR_BOTTOM_AND_LEFT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_BOTTOM_AND_LEFT_BORDER: 8>
Aspect_TOR_BOTTOM_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_BOTTOM_BORDER: 4>
Aspect_TOR_LEFT_AND_TOP_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_LEFT_AND_TOP_BORDER: 9>
Aspect_TOR_LEFT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_LEFT_BORDER: 5>
Aspect_TOR_NO_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_NO_BORDER: 1>
Aspect_TOR_RIGHT_AND_BOTTOM_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_RIGHT_AND_BOTTOM_BORDER: 7>
Aspect_TOR_RIGHT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_RIGHT_BORDER: 3>
Aspect_TOR_TOP_AND_RIGHT_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_TOP_AND_RIGHT_BORDER: 6>
Aspect_TOR_TOP_BORDER: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_TOP_BORDER: 2>
Aspect_TOR_UNKNOWN: OCP.Aspect.Aspect_TypeOfResize # value = <Aspect_TypeOfResize.Aspect_TOR_UNKNOWN: 0>
Aspect_TOST_ANNOTATION: OCP.Aspect.Aspect_TypeOfStyleText # value = <Aspect_TypeOfStyleText.Aspect_TOST_ANNOTATION: 1>
Aspect_TOST_NORMAL: OCP.Aspect.Aspect_TypeOfStyleText # value = <Aspect_TypeOfStyleText.Aspect_TOST_NORMAL: 0>
Aspect_TOTP_BOTTOM: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_BOTTOM: 2>
Aspect_TOTP_CENTER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER: 0>
Aspect_TOTP_LEFT: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT: 4>
Aspect_TOTP_LEFT_LOWER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_LOWER: 6>
Aspect_TOTP_LEFT_UPPER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT_UPPER: 5>
Aspect_TOTP_RIGHT: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT: 8>
Aspect_TOTP_RIGHT_LOWER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_LOWER: 10>
Aspect_TOTP_RIGHT_UPPER: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT_UPPER: 9>
Aspect_TOTP_TOP: OCP.Aspect.Aspect_TypeOfTriedronPosition # value = <Aspect_TypeOfTriedronPosition.Aspect_TOTP_TOP: 1>
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
Aspect_VKey_0: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_0: 27>
Aspect_VKey_1: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_1: 28>
Aspect_VKey_2: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_2: 29>
Aspect_VKey_3: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_3: 30>
Aspect_VKey_4: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_4: 31>
Aspect_VKey_5: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_5: 32>
Aspect_VKey_6: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_6: 33>
Aspect_VKey_7: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_7: 34>
Aspect_VKey_8: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_8: 35>
Aspect_VKey_9: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_9: 36>
Aspect_VKey_A: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_A: 1>
Aspect_VKey_Alt: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Alt: 120>
Aspect_VKey_Apostrophe: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Apostrophe: 75>
Aspect_VKey_B: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_B: 2>
Aspect_VKey_Back: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Back: 61>
Aspect_VKey_Backslash: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Backslash: 73>
Aspect_VKey_Backspace: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Backspace: 63>
Aspect_VKey_BracketLeft: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BracketLeft: 72>
Aspect_VKey_BracketRight: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BracketRight: 74>
Aspect_VKey_BrowserBack: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserBack: 99>
Aspect_VKey_BrowserFavorites: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserFavorites: 104>
Aspect_VKey_BrowserForward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserForward: 100>
Aspect_VKey_BrowserHome: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserHome: 105>
Aspect_VKey_BrowserRefresh: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserRefresh: 101>
Aspect_VKey_BrowserSearch: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserSearch: 103>
Aspect_VKey_BrowserStop: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_BrowserStop: 102>
Aspect_VKey_C: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_C: 3>
Aspect_VKey_Comma: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Comma: 68>
Aspect_VKey_Control: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Control: 119>
Aspect_VKey_D: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_D: 4>
Aspect_VKey_Delete: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Delete: 65>
Aspect_VKey_Down: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Down: 50>
Aspect_VKey_E: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_E: 5>
Aspect_VKey_End: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_End: 59>
Aspect_VKey_Enter: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Enter: 62>
Aspect_VKey_Equal: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Equal: 55>
Aspect_VKey_Escape: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Escape: 60>
Aspect_VKey_F: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F: 6>
Aspect_VKey_F1: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F1: 37>
Aspect_VKey_F10: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F10: 46>
Aspect_VKey_F11: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F11: 47>
Aspect_VKey_F12: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F12: 48>
Aspect_VKey_F2: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F2: 38>
Aspect_VKey_F3: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F3: 39>
Aspect_VKey_F4: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F4: 40>
Aspect_VKey_F5: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F5: 41>
Aspect_VKey_F6: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F6: 42>
Aspect_VKey_F7: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F7: 43>
Aspect_VKey_F8: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F8: 44>
Aspect_VKey_F9: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_F9: 45>
Aspect_VKey_G: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_G: 7>
Aspect_VKey_H: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_H: 8>
Aspect_VKey_Home: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Home: 58>
Aspect_VKey_I: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_I: 9>
Aspect_VKey_J: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_J: 10>
Aspect_VKey_K: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_K: 11>
Aspect_VKey_L: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_L: 12>
Aspect_VKey_Left: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Left: 51>
Aspect_VKey_Lower = 0
Aspect_VKey_M: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_M: 13>
Aspect_VKey_MAX = 255
Aspect_VKey_MediaNextTrack: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_MediaNextTrack: 92>
Aspect_VKey_MediaPlayPause: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_MediaPlayPause: 95>
Aspect_VKey_MediaPreviousTrack: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_MediaPreviousTrack: 93>
Aspect_VKey_MediaStop: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_MediaStop: 94>
Aspect_VKey_Menu: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Menu: 121>
Aspect_VKey_Meta: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Meta: 122>
Aspect_VKey_Minus: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Minus: 54>
Aspect_VKey_ModifiersLower = 118
Aspect_VKey_ModifiersUpper = 122
Aspect_VKey_N: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_N: 14>
Aspect_VKey_NB = 143
Aspect_VKey_NavBackward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavBackward: 125>
Aspect_VKey_NavCrouch: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavCrouch: 136>
Aspect_VKey_NavForward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavForward: 124>
Aspect_VKey_NavInteract: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavInteract: 123>
Aspect_VKey_NavJump: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavJump: 137>
Aspect_VKey_NavLookDown: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavLookDown: 135>
Aspect_VKey_NavLookLeft: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavLookLeft: 132>
Aspect_VKey_NavLookRight: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavLookRight: 133>
Aspect_VKey_NavLookUp: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavLookUp: 134>
Aspect_VKey_NavRollCCW: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavRollCCW: 130>
Aspect_VKey_NavRollCW: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavRollCW: 131>
Aspect_VKey_NavSlideDown: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSlideDown: 129>
Aspect_VKey_NavSlideLeft: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSlideLeft: 126>
Aspect_VKey_NavSlideRight: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSlideRight: 127>
Aspect_VKey_NavSlideUp: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSlideUp: 128>
Aspect_VKey_NavSpeedDecrease: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSpeedDecrease: 142>
Aspect_VKey_NavSpeedIncrease: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavSpeedIncrease: 141>
Aspect_VKey_NavThrustBackward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavThrustBackward: 139>
Aspect_VKey_NavThrustForward: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavThrustForward: 138>
Aspect_VKey_NavThrustStop: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NavThrustStop: 140>
Aspect_VKey_NavigationKeysLower = 123
Aspect_VKey_NavigationKeysUpper = 142
Aspect_VKey_Numlock: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numlock: 76>
Aspect_VKey_Numpad0: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad0: 78>
Aspect_VKey_Numpad1: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad1: 79>
Aspect_VKey_Numpad2: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad2: 80>
Aspect_VKey_Numpad3: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad3: 81>
Aspect_VKey_Numpad4: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad4: 82>
Aspect_VKey_Numpad5: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad5: 83>
Aspect_VKey_Numpad6: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad6: 84>
Aspect_VKey_Numpad7: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad7: 85>
Aspect_VKey_Numpad8: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad8: 86>
Aspect_VKey_Numpad9: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Numpad9: 87>
Aspect_VKey_NumpadAdd: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NumpadAdd: 89>
Aspect_VKey_NumpadDivide: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NumpadDivide: 91>
Aspect_VKey_NumpadMultiply: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NumpadMultiply: 88>
Aspect_VKey_NumpadSubtract: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_NumpadSubtract: 90>
Aspect_VKey_O: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_O: 15>
Aspect_VKey_P: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_P: 16>
Aspect_VKey_PageDown: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_PageDown: 57>
Aspect_VKey_PageUp: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_PageUp: 56>
Aspect_VKey_Period: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Period: 69>
Aspect_VKey_Plus: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Plus: 53>
Aspect_VKey_Q: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Q: 17>
Aspect_VKey_R: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_R: 18>
Aspect_VKey_Right: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Right: 52>
Aspect_VKey_S: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_S: 19>
Aspect_VKey_Scroll: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Scroll: 77>
Aspect_VKey_Semicolon: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Semicolon: 70>
Aspect_VKey_Shift: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Shift: 118>
Aspect_VKey_Slash: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Slash: 71>
Aspect_VKey_Space: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Space: 64>
Aspect_VKey_T: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_T: 20>
Aspect_VKey_Tab: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Tab: 67>
Aspect_VKey_Tilde: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Tilde: 66>
Aspect_VKey_U: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_U: 21>
Aspect_VKey_UNKNOWN: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_UNKNOWN: 0>
Aspect_VKey_Up: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Up: 49>
Aspect_VKey_Upper = 142
Aspect_VKey_V: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_V: 22>
Aspect_VKey_ViewAxoLeftProj: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewAxoLeftProj: 112>
Aspect_VKey_ViewAxoRightProj: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewAxoRightProj: 113>
Aspect_VKey_ViewBack: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewBack: 111>
Aspect_VKey_ViewBottom: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewBottom: 107>
Aspect_VKey_ViewFitAll: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewFitAll: 114>
Aspect_VKey_ViewFront: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewFront: 110>
Aspect_VKey_ViewLeft: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewLeft: 108>
Aspect_VKey_ViewRight: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewRight: 109>
Aspect_VKey_ViewRoll90CCW: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CCW: 116>
Aspect_VKey_ViewRoll90CW: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CW: 115>
Aspect_VKey_ViewSwitchRotate: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewSwitchRotate: 117>
Aspect_VKey_ViewTop: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_ViewTop: 106>
Aspect_VKey_VolumeDown: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_VolumeDown: 97>
Aspect_VKey_VolumeMute: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_VolumeMute: 96>
Aspect_VKey_VolumeUp: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_VolumeUp: 98>
Aspect_VKey_W: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_W: 23>
Aspect_VKey_X: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_X: 24>
Aspect_VKey_Y: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Y: 25>
Aspect_VKey_Z: OCP.Aspect.Aspect_VKeyBasic # value = <Aspect_VKeyBasic.Aspect_VKey_Z: 26>
Aspect_WOL_MEDIUM: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_MEDIUM: 1>
Aspect_WOL_THICK: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_THICK: 2>
Aspect_WOL_THIN: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_THIN: 0>
Aspect_WOL_USERDEFINED: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_USERDEFINED: 4>
Aspect_WOL_VERYTHICK: OCP.Aspect.Aspect_WidthOfLine # value = <Aspect_WidthOfLine.Aspect_WOL_VERYTHICK: 3>
Aspect_XA_DELETE_WINDOW: OCP.Aspect.Aspect_XAtom # value = <Aspect_XAtom.Aspect_XA_DELETE_WINDOW: 0>
Aspect_XRActionType_InputAnalog: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_InputAnalog: 1>
Aspect_XRActionType_InputDigital: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_InputDigital: 0>
Aspect_XRActionType_InputPose: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_InputPose: 2>
Aspect_XRActionType_InputSkeletal: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_InputSkeletal: 3>
Aspect_XRActionType_OutputHaptic: OCP.Aspect.Aspect_XRActionType # value = <Aspect_XRActionType.Aspect_XRActionType_OutputHaptic: 4>
Aspect_XRGenericAction_InputAppMenu: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputAppMenu: 1>
Aspect_XRGenericAction_InputGripClick: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputGripClick: 5>
Aspect_XRGenericAction_InputPoseBase: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseBase: 12>
Aspect_XRGenericAction_InputPoseFingerTip: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseFingerTip: 15>
Aspect_XRGenericAction_InputPoseFront: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseFront: 13>
Aspect_XRGenericAction_InputPoseHandGrip: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputPoseHandGrip: 14>
Aspect_XRGenericAction_InputSysMenu: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputSysMenu: 2>
Aspect_XRGenericAction_InputThumbstickClick: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickClick: 11>
Aspect_XRGenericAction_InputThumbstickPosition: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickPosition: 9>
Aspect_XRGenericAction_InputThumbstickTouch: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputThumbstickTouch: 10>
Aspect_XRGenericAction_InputTrackPadClick: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadClick: 8>
Aspect_XRGenericAction_InputTrackPadPosition: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadPosition: 6>
Aspect_XRGenericAction_InputTrackPadTouch: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTrackPadTouch: 7>
Aspect_XRGenericAction_InputTriggerClick: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTriggerClick: 4>
Aspect_XRGenericAction_InputTriggerPull: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_InputTriggerPull: 3>
Aspect_XRGenericAction_IsHeadsetOn: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_IsHeadsetOn: 0>
Aspect_XRGenericAction_NB = 17
Aspect_XRGenericAction_OutputHaptic: OCP.Aspect.Aspect_XRGenericAction # value = <Aspect_XRGenericAction.Aspect_XRGenericAction_OutputHaptic: 16>
Aspect_XRTrackedDeviceRole_Head: OCP.Aspect.Aspect_XRTrackedDeviceRole # value = <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_Head: 0>
Aspect_XRTrackedDeviceRole_LeftHand: OCP.Aspect.Aspect_XRTrackedDeviceRole # value = <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_LeftHand: 1>
Aspect_XRTrackedDeviceRole_NB = 4
Aspect_XRTrackedDeviceRole_Other: OCP.Aspect.Aspect_XRTrackedDeviceRole # value = <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_Other: 3>
Aspect_XRTrackedDeviceRole_RightHand: OCP.Aspect.Aspect_XRTrackedDeviceRole # value = <Aspect_XRTrackedDeviceRole.Aspect_XRTrackedDeviceRole_RightHand: 2>
