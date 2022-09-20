import OCP.WNT
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Quantity
import io
import OCP.SelectMgr
import OCP.Graphic3d
import OCP.Standard
import OCP.Aspect
import OCP.TCollection
__all__  = [
"WNT_ClassDefinitionError",
"WNT_HIDSpaceMouse",
"WNT_OrientationType",
"WNT_WClass",
"WNT_Window",
"WNT_OT_LANDSCAPE",
"WNT_OT_PORTRAIT"
]
class WNT_ClassDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.WNT', '__weakref__': <attribute '__weakref__' of 'WNT_ClassDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'WNT_ClassDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class WNT_HIDSpaceMouse():
    """
    Wrapper over Space Mouse data chunk within WM_INPUT event (known also as Raw Input in WinAPI). This class predefines specific list of supported devices, which does not depend on 3rdparty library provided by mouse vendor. Supported input chunks: - Rotation (3 directions); - Translation (3 directions); - Pressed buttons.
    """
    def HidToSpaceKey(self,theKeyBit : int) -> int: 
        """
        Convert key state bit into virtual key.
        """
    def IsKeyState(self) -> bool: 
        """
        Return TRUE for key state data chunk.
        """
    @staticmethod
    def IsKnownProduct_s(theProductId : int) -> bool: 
        """
        Return if product id is known by this class.
        """
    def IsRotation(self) -> bool: 
        """
        Return TRUE if data chunk defines new rotation values.
        """
    def IsTranslation(self) -> bool: 
        """
        Return TRUE if data chunk defines new translation values.
        """
    def KeyState(self) -> int: 
        """
        Return new keystate.
        """
    def RawValueRange(self) -> int: 
        """
        Return the raw value range.
        """
    def Rotation(self,theIsIdle : bool,theIsQuadric : bool) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        Return new rotation values.
        """
    def SetRawValueRange(self,theRange : int) -> None: 
        """
        Set the raw value range.
        """
    def Translation(self,theIsIdle : bool,theIsQuadric : bool) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        Return new translation values.
        """
    def __init__(self,theProductId : int,theData : int,theSize : int) -> None: ...
    VENDOR_ID_3DCONNEXION = 9583
    VENDOR_ID_LOGITECH = 1133
    pass
class WNT_OrientationType():
    """
    Portrait/landscape orientation.

    Members:

      WNT_OT_PORTRAIT

      WNT_OT_LANDSCAPE
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
    WNT_OT_LANDSCAPE: OCP.WNT.WNT_OrientationType # value = <WNT_OrientationType.WNT_OT_LANDSCAPE: 1>
    WNT_OT_PORTRAIT: OCP.WNT.WNT_OrientationType # value = <WNT_OrientationType.WNT_OT_PORTRAIT: 0>
    __entries: dict # value = {'WNT_OT_PORTRAIT': (<WNT_OrientationType.WNT_OT_PORTRAIT: 0>, None), 'WNT_OT_LANDSCAPE': (<WNT_OrientationType.WNT_OT_LANDSCAPE: 1>, None)}
    __members__: dict # value = {'WNT_OT_PORTRAIT': <WNT_OrientationType.WNT_OT_PORTRAIT: 0>, 'WNT_OT_LANDSCAPE': <WNT_OrientationType.WNT_OT_LANDSCAPE: 1>}
    pass
class WNT_WClass(OCP.Standard.Standard_Transient):
    """
    This class defines a Windows NT window class. A window in Windows NT is always created based on a window class. The window class identifies the window procedure that processes messages to the window. Each window class has unique name ( character string ). More than one window can be created based on a single window class. For example, all button windows in Windows NT are created based on the same window class. The window class defines the window procedure and some other characteristics ( background, mouse cursor shape etc. ) of the windows that are created based on that class. When we create a window, we define additional characteristics of the window that are unique to that window. So, we have to create and register window class before creation of any window. Of course, it's possible to create a new window class for each window inside the Window class and do not use the WClass at all. We implemented this class for sake of flexibility of event processing.This class defines a Windows NT window class. A window in Windows NT is always created based on a window class. The window class identifies the window procedure that processes messages to the window. Each window class has unique name ( character string ). More than one window can be created based on a single window class. For example, all button windows in Windows NT are created based on the same window class. The window class defines the window procedure and some other characteristics ( background, mouse cursor shape etc. ) of the windows that are created based on that class. When we create a window, we define additional characteristics of the window that are unique to that window. So, we have to create and register window class before creation of any window. Of course, it's possible to create a new window class for each window inside the Window class and do not use the WClass at all. We implemented this class for sake of flexibility of event processing.
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
    def Instance(self) -> capsule: 
        """
        Returns a program instance handle.
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
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a class name.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WndProc(self) -> capsule: 
        """
        Returns address of window procedure.
        """
    def __init__(self,theClassName : OCP.TCollection.TCollection_AsciiString,theWndProc : capsule,theStyle : int,theClassExtra : int=0,theWindowExtra : int=0,theCursor : capsule=None,theIcon : capsule=None,theMenuName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class WNT_Window(OCP.Aspect.Aspect_Window, OCP.Standard.Standard_Transient):
    """
    This class defines Windows NT windowThis class defines Windows NT window
    """
    class RawInputMask_e():
        """
        Raw input flags.

        Members:

          RawInputMask_Mouse

          RawInputMask_SpaceMouse
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
        RawInputMask_Mouse: OCP.WNT.RawInputMask_e # value = <RawInputMask_e.RawInputMask_Mouse: 1>
        RawInputMask_SpaceMouse: OCP.WNT.RawInputMask_e # value = <RawInputMask_e.RawInputMask_SpaceMouse: 2>
        __entries: dict # value = {'RawInputMask_Mouse': (<RawInputMask_e.RawInputMask_Mouse: 1>, None), 'RawInputMask_SpaceMouse': (<RawInputMask_e.RawInputMask_SpaceMouse: 2>, None)}
        __members__: dict # value = {'RawInputMask_Mouse': <RawInputMask_e.RawInputMask_Mouse: 1>, 'RawInputMask_SpaceMouse': <RawInputMask_e.RawInputMask_SpaceMouse: 2>}
        pass
    def Background(self) -> OCP.Aspect.Aspect_Background: 
        """
        Returns the window background.
        """
    def BackgroundFillMethod(self) -> OCP.Aspect.Aspect_FillMethod: 
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
    def DisplayConnection(self) -> OCP.Aspect.Aspect_DisplayConnection: 
        """
        Returns connection to Display or NULL.
        """
    def DoMapping(self) -> bool: 
        """
        Does nothing on Windows.
        """
    def DoResize(self) -> OCP.Aspect.Aspect_TypeOfResize: 
        """
        Applies the resizing to the window <me>.
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
    def GradientBackground(self) -> OCP.Aspect.Aspect_GradientBackground: 
        """
        Returns the window gradient background.
        """
    def HParentWindow(self) -> capsule: 
        """
        Returns the Windows NT handle parent of the created window <me>.
        """
    def HWindow(self) -> capsule: 
        """
        Returns the Windows NT handle of the created window <me>.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvalidateContent(self,theDisp : OCP.Aspect.Aspect_DisplayConnection=None) -> None: 
        """
        Invalidate entire window content by calling InvalidateRect() WinAPI function, resulting in WM_PAINT event put into window message loop. Method can be called from non-window thread, and system will also automatically aggregate multiple events into single one.
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
    @overload
    def Map(self) -> None: 
        """
        Opens the window <me>.

        Opens a window according to the map mode. This method is specific to Windows NT.
        """
    @overload
    def Map(self,theMapMode : int) -> None: ...
    @staticmethod
    def MouseButtonsAsync_s() -> int: 
        """
        Use GetAsyncKeyState() to fetch actual mouse buttons state regardless of event loop.
        """
    @staticmethod
    def MouseButtonsFromEvent_s(theKeys : int) -> int: 
        """
        Convert WPARAM from mouse event to mouse buttons bitmask.
        """
    @staticmethod
    def MouseKeyFlagsAsync_s() -> int: 
        """
        Use GetAsyncKeyState() to fetch actual mouse key flags regardless of event loop.
        """
    @staticmethod
    def MouseKeyFlagsFromEvent_s(theKeys : int) -> int: 
        """
        Convert WPARAM from mouse event to key flags.
        """
    def NativeFBConfig(self) -> __GLXFBConfigRec: 
        """
        Returns nothing on Windows
        """
    def NativeHandle(self) -> capsule: 
        """
        Returns native Window handle (HWND)
        """
    def NativeParentHandle(self) -> capsule: 
        """
        Returns parent of native Window handle (HWND on Windows).
        """
    def Position(self) -> Tuple[int, int, int, int]: 
        """
        Returns The Window POSITION in PIXEL
        """
    def Ratio(self) -> float: 
        """
        Returns The Window RATIO equal to the physical WIDTH/HEIGHT dimensions.
        """
    def RegisterRawInputDevices(self,theRawDeviceMask : int) -> int: ...
    @overload
    def SetBackground(self,ABackground : OCP.Aspect.Aspect_GradientBackground) -> None: 
        """
        Modifies the window background.

        Modifies the window background.

        Modifies the window gradient background.

        Modifies the window gradient background.
        """
    @overload
    def SetBackground(self,ABack : OCP.Aspect.Aspect_Background) -> None: ...
    @overload
    def SetBackground(self,theFirstColor : OCP.Quantity.Quantity_Color,theSecondColor : OCP.Quantity.Quantity_Color,theFillMethod : OCP.Aspect.Aspect_GradientFillMethod) -> None: ...
    @overload
    def SetBackground(self,color : OCP.Quantity.Quantity_Color) -> None: ...
    def SetCursor(self,theCursor : capsule) -> None: 
        """
        Sets cursor for ENTIRE WINDOW CLASS to which the Window belongs.
        """
    def SetPos(self,X : int,Y : int,X1 : int,Y1 : int) -> None: 
        """
        Changes variables due to window position.
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
    def VirtualKeyFromNative_s(theKey : int) -> int: 
        """
        Convert WInAPI virtual key (VK_ enumeration) into Aspect_VKey.
        """
    @overload
    def __init__(self,theTitle : str,theClass : WNT_WClass,theStyle : int,thePxLeft : int,thePxTop : int,thePxWidth : int,thePxHeight : int,theBackColor : OCP.Quantity.Quantity_NameOfColor=Quantity_NameOfColor.Quantity_NOC_MATRAGRAY,theParent : capsule=None,theMenu : capsule=None,theClientStruct : capsule=None) -> None: ...
    @overload
    def __init__(self,theHandle : capsule,theBackColor : OCP.Quantity.Quantity_NameOfColor=Quantity_NameOfColor.Quantity_NOC_MATRAGRAY) -> None: ...
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
    RawInputMask_Mouse: OCP.WNT.RawInputMask_e # value = <RawInputMask_e.RawInputMask_Mouse: 1>
    RawInputMask_SpaceMouse: OCP.WNT.RawInputMask_e # value = <RawInputMask_e.RawInputMask_SpaceMouse: 2>
    pass
WNT_OT_LANDSCAPE: OCP.WNT.WNT_OrientationType # value = <WNT_OrientationType.WNT_OT_LANDSCAPE: 1>
WNT_OT_PORTRAIT: OCP.WNT.WNT_OrientationType # value = <WNT_OrientationType.WNT_OT_PORTRAIT: 0>
