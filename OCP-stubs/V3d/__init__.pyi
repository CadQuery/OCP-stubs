import OCP.V3d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Quantity
import OCP.TCollection
import OCP.TColStd
import io
import OCP.NCollection
import OCP.gp
import OCP.Image
import OCP.Bnd
import OCP.Graphic3d
import OCP.Standard
import OCP.Aspect
__all__  = [
"V3d",
"V3d_AmbientLight",
"V3d_BadValue",
"V3d_CircularGrid",
"V3d_PositionLight",
"V3d_ImageDumpOptions",
"V3d_ListOfLight",
"V3d_ListOfView",
"V3d_Plane",
"V3d_DirectionalLight",
"V3d_PositionalLight",
"V3d_RectangularGrid",
"V3d_SpotLight",
"V3d_StereoDumpOptions",
"V3d_Trihedron",
"V3d_TypeOfAxe",
"V3d_TypeOfBackfacingModel",
"V3d_TypeOfOrientation",
"V3d_TypeOfPickCamera",
"V3d_TypeOfPickLight",
"V3d_TypeOfRepresentation",
"V3d_TypeOfView",
"V3d_TypeOfVisualization",
"V3d_UnMapped",
"V3d_View",
"V3d_Viewer",
"V3d_COMPLETE",
"V3d_ExtRADIUSCAMERA",
"V3d_ExtRADIUSLIGHT",
"V3d_IntRADIUSCAMERA",
"V3d_IntRADIUSLIGHT",
"V3d_NOTHING",
"V3d_NOTHINGCAMERA",
"V3d_ORTHOGRAPHIC",
"V3d_PARTIAL",
"V3d_PERSPECTIVE",
"V3d_POSITIONCAMERA",
"V3d_POSITIONLIGHT",
"V3d_RADIUSTEXTCAMERA",
"V3d_RADIUSTEXTLIGHT",
"V3d_SAMELAST",
"V3d_SDO_BLENDED",
"V3d_SDO_LEFT_EYE",
"V3d_SDO_MONO",
"V3d_SDO_RIGHT_EYE",
"V3d_SIMPLE",
"V3d_SPACECAMERA",
"V3d_SPACELIGHT",
"V3d_TOBM_ALWAYS_DISPLAYED",
"V3d_TOBM_AUTOMATIC",
"V3d_TOBM_NEVER_DISPLAYED",
"V3d_TypeOfOrientation_Yup_AxoLeft",
"V3d_TypeOfOrientation_Yup_AxoRight",
"V3d_TypeOfOrientation_Yup_Back",
"V3d_TypeOfOrientation_Yup_Bottom",
"V3d_TypeOfOrientation_Yup_Front",
"V3d_TypeOfOrientation_Yup_Left",
"V3d_TypeOfOrientation_Yup_Right",
"V3d_TypeOfOrientation_Yup_Top",
"V3d_TypeOfOrientation_Zup_AxoLeft",
"V3d_TypeOfOrientation_Zup_AxoRight",
"V3d_TypeOfOrientation_Zup_Back",
"V3d_TypeOfOrientation_Zup_Bottom",
"V3d_TypeOfOrientation_Zup_Front",
"V3d_TypeOfOrientation_Zup_Left",
"V3d_TypeOfOrientation_Zup_Right",
"V3d_TypeOfOrientation_Zup_Top",
"V3d_WIREFRAME",
"V3d_X",
"V3d_Xneg",
"V3d_XnegYneg",
"V3d_XnegYnegZneg",
"V3d_XnegYnegZpos",
"V3d_XnegYpos",
"V3d_XnegYposZneg",
"V3d_XnegYposZpos",
"V3d_XnegZneg",
"V3d_XnegZpos",
"V3d_Xpos",
"V3d_XposYneg",
"V3d_XposYnegZneg",
"V3d_XposYnegZpos",
"V3d_XposYpos",
"V3d_XposYposZneg",
"V3d_XposYposZpos",
"V3d_XposZneg",
"V3d_XposZpos",
"V3d_Y",
"V3d_Yneg",
"V3d_YnegZneg",
"V3d_YnegZpos",
"V3d_Ypos",
"V3d_YposZneg",
"V3d_YposZpos",
"V3d_Z",
"V3d_ZBUFFER",
"V3d_Zneg",
"V3d_Zpos"
]
class V3d():
    """
    This package contains the set of commands and services of the 3D Viewer. It provides a set of high level commands to control the views and viewing modes.
    """
    @staticmethod
    def ArrowOfRadius_s(garrow : OCP.Graphic3d.Graphic3d_Group,X0 : float,Y0 : float,Z0 : float,DX : float,DY : float,DZ : float,Alpha : float,Lng : float) -> None: 
        """
        Compute the graphic structure of arrow. X0,Y0,Z0 : coordinate of the arrow. DX,DY,DZ : Direction of the arrow. Alpha : Angle of arrow. Lng : Length of arrow.
        """
    @staticmethod
    def CircleInPlane_s(gcircle : OCP.Graphic3d.Graphic3d_Group,X0 : float,Y0 : float,Z0 : float,VX : float,VY : float,VZ : float,Radius : float) -> None: 
        """
        Compute the graphic structure of circle. X0,Y0,Z0 : Center of circle. VX,VY,VZ : Axis of circle. Radius : Radius of circle.
        """
    @staticmethod
    def GetProjAxis_s(theOrientation : V3d_TypeOfOrientation) -> OCP.gp.gp_Dir: 
        """
        Determines the orientation vector corresponding to the predefined orientation type.
        """
    @staticmethod
    def SwitchViewsinWindow_s(aPreviousView : V3d_View,aNextView : V3d_View) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def TypeOfOrientationFromString_s(theTypeString : str) -> V3d_TypeOfOrientation: 
        """
        Returns the orientation type from the given string identifier (using case-insensitive comparison).

        Determines the shape type from the given string identifier (using case-insensitive comparison).
        """
    @staticmethod
    @overload
    def TypeOfOrientationFromString_s(theTypeString : str,theType : V3d_TypeOfOrientation) -> bool: ...
    @staticmethod
    def TypeOfOrientationToString_s(theType : V3d_TypeOfOrientation) -> str: 
        """
        Returns the string name for a given orientation type.
        """
    def __init__(self) -> None: ...
    pass
class V3d_AmbientLight(OCP.Graphic3d.Graphic3d_CLight, OCP.Standard.Standard_Transient):
    """
    Creation of an ambient light source in a viewer.Creation of an ambient light source in a viewer.
    """
    def Angle(self) -> float: 
        """
        Returns an angle in radians of the cone created by the spot; 30 degrees by default.
        """
    def Attenuation(self) -> Tuple[float, float]: 
        """
        Returns the attenuation factors.
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the color of the light source; WHITE by default.
        """
    def Concentration(self) -> float: 
        """
        Returns intensity distribution of the spot light, within [0.0, 1.0] range; 1.0 by default. This coefficient should be converted into spotlight exponent within [0.0, 128.0] range: The concentration factor determines the dispersion of the light on the surface, the default value (1.0) corresponds to a minimum of dispersion.
        """
    def ConstAttenuation(self) -> float: 
        """
        Returns constant attenuation factor of positional/spot light source; 1.0f by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns direction of directional/spot light.

        Returns the theVx, theVy, theVz direction of the light source.
        """
    @overload
    def Direction(self) -> Tuple[float, float, float]: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light resource identifier string
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Headlight(self) -> bool: 
        """
        Alias for IsHeadlight().
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intensity(self) -> float: 
        """
        Returns the intensity of light source; 1.0 by default.
        """
    def IsEnabled(self) -> bool: 
        """
        Check that the light source is turned on; TRUE by default. This flag affects all occurrences of light sources, where it was registered and activated; so that it is possible defining an active light in View which is actually in disabled state.
        """
    def IsHeadlight(self) -> bool: 
        """
        Returns true if the light is a headlight; FALSE by default. Headlight flag means that light position/direction are defined not in a World coordinate system, but relative to the camera orientation.
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
    def LinearAttenuation(self) -> float: 
        """
        Returns linear attenuation factor of positional/spot light source; 0.0 by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light source name; empty string by default.
        """
    def PackedColor(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns the color of the light source with dummy Alpha component, which should be ignored.
        """
    def PackedDirectionRange(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns direction of directional/spot light and range for positional/spot light in alpha channel.
        """
    def PackedParams(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Packed light parameters.
        """
    @overload
    def Position(self) -> OCP.gp.gp_Pnt: 
        """
        Returns location of positional/spot light.

        Returns location of positional/spot light; (0, 0, 0) by default.
        """
    @overload
    def Position(self) -> Tuple[float, float, float]: ...
    def Range(self) -> float: 
        """
        Returns maximum distance on which point light source affects to objects and is considered during illumination calculations. 0.0 means disabling range considering at all without any distance limits. Has sense only for point light sources (positional and spot).
        """
    def Revision(self) -> int: 
        """
        Returns modification counter
        """
    def SetAngle(self,theAngle : float) -> None: 
        """
        Angle in radians of the cone created by the spot, should be within range (0.0, M_PI).
        """
    def SetAttenuation(self,theConstAttenuation : float,theLinearAttenuation : float) -> None: 
        """
        Defines the coefficients of attenuation; values should be >= 0.0 and their summ should not be equal to 0.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Defines the color of a light source by giving the basic color.
        """
    def SetConcentration(self,theConcentration : float) -> None: 
        """
        Defines the coefficient of concentration; value should be within range [0.0, 1.0].
        """
    @overload
    def SetDirection(self,theDir : OCP.gp.gp_Dir) -> None: 
        """
        Sets direction of directional/spot light.

        Sets direction of directional/spot light.
        """
    @overload
    def SetDirection(self,theVx : float,theVy : float,theVz : float) -> None: ...
    def SetEnabled(self,theIsOn : bool) -> None: 
        """
        Change enabled state of the light state. This call does not remove or deactivate light source in Views/Viewers; instead it turns it OFF so that it just have no effect.
        """
    def SetHeadlight(self,theValue : bool) -> None: 
        """
        Setup headlight flag.
        """
    def SetIntensity(self,theValue : float) -> None: 
        """
        Modifies the intensity of light source, which should be > 0.0.
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets light source name.
        """
    @overload
    def SetPosition(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Setup location of positional/spot light.

        Setup location of positional/spot light.
        """
    @overload
    def SetPosition(self,thePosition : OCP.gp.gp_Pnt) -> None: ...
    def SetRange(self,theValue : float) -> None: 
        """
        Modifies maximum distance on which point light source affects to objects and is considered during illumination calculations. Positional and spot lights are only point light sources. 0.0 means disabling range considering at all without any distance limits.
        """
    def SetSmoothAngle(self,theValue : float) -> None: 
        """
        Modifies the smoothing angle (in radians) of directional light source; should be within range [0.0, M_PI/2].
        """
    def SetSmoothRadius(self,theValue : float) -> None: 
        """
        Modifies the smoothing radius of positional/spot light; should be >= 0.0.
        """
    def Smoothness(self) -> float: 
        """
        Returns the smoothness of light source (either smoothing angle for directional light or smoothing radius in case of positional light); 0.0 by default.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.Graphic3d.Graphic3d_TypeOfLightSource: 
        """
        Returns the Type of the Light, cannot be changed after object construction.
        """
    def __init__(self,theColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color) -> None: ...
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
class V3d_BadValue(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.V3d', '__weakref__': <attribute '__weakref__' of 'V3d_BadValue' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'V3d_BadValue' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class V3d_CircularGrid(OCP.Aspect.Aspect_CircularGrid, OCP.Aspect.Aspect_Grid, OCP.Standard.Standard_Transient):
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
        None
        """
    def DivisionNumber(self) -> int: 
        """
        returns the x step of the grid.
        """
    def DrawMode(self) -> OCP.Aspect.Aspect_GridDrawMode: 
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
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GraphicValues(self) -> Tuple[float, float]: 
        """
        None
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
        None
        """
    def SetDivisionNumber(self,aNumber : int) -> None: 
        """
        defines the step of the grid.
        """
    def SetDrawMode(self,aDrawMode : OCP.Aspect.Aspect_GridDrawMode) -> None: 
        """
        Change the grid aspect.
        """
    def SetGraphicValues(self,Radius : float,OffSet : float) -> None: 
        """
        None
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
class V3d_PositionLight(OCP.Graphic3d.Graphic3d_CLight, OCP.Standard.Standard_Transient):
    """
    Base class for Positional, Spot and Directional Light classes.Base class for Positional, Spot and Directional Light classes.
    """
    def Angle(self) -> float: 
        """
        Returns an angle in radians of the cone created by the spot; 30 degrees by default.
        """
    def Attenuation(self) -> Tuple[float, float]: 
        """
        Returns the attenuation factors.
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the color of the light source; WHITE by default.
        """
    def Concentration(self) -> float: 
        """
        Returns intensity distribution of the spot light, within [0.0, 1.0] range; 1.0 by default. This coefficient should be converted into spotlight exponent within [0.0, 128.0] range: The concentration factor determines the dispersion of the light on the surface, the default value (1.0) corresponds to a minimum of dispersion.
        """
    def ConstAttenuation(self) -> float: 
        """
        Returns constant attenuation factor of positional/spot light source; 1.0f by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns direction of directional/spot light.

        Returns the theVx, theVy, theVz direction of the light source.
        """
    @overload
    def Direction(self) -> Tuple[float, float, float]: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light resource identifier string
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Headlight(self) -> bool: 
        """
        Alias for IsHeadlight().
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intensity(self) -> float: 
        """
        Returns the intensity of light source; 1.0 by default.
        """
    def IsEnabled(self) -> bool: 
        """
        Check that the light source is turned on; TRUE by default. This flag affects all occurrences of light sources, where it was registered and activated; so that it is possible defining an active light in View which is actually in disabled state.
        """
    def IsHeadlight(self) -> bool: 
        """
        Returns true if the light is a headlight; FALSE by default. Headlight flag means that light position/direction are defined not in a World coordinate system, but relative to the camera orientation.
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
    def LinearAttenuation(self) -> float: 
        """
        Returns linear attenuation factor of positional/spot light source; 0.0 by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light source name; empty string by default.
        """
    def PackedColor(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns the color of the light source with dummy Alpha component, which should be ignored.
        """
    def PackedDirectionRange(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns direction of directional/spot light and range for positional/spot light in alpha channel.
        """
    def PackedParams(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Packed light parameters.
        """
    @overload
    def Position(self) -> OCP.gp.gp_Pnt: 
        """
        Returns location of positional/spot light.

        Returns location of positional/spot light; (0, 0, 0) by default.
        """
    @overload
    def Position(self) -> Tuple[float, float, float]: ...
    def Range(self) -> float: 
        """
        Returns maximum distance on which point light source affects to objects and is considered during illumination calculations. 0.0 means disabling range considering at all without any distance limits. Has sense only for point light sources (positional and spot).
        """
    def Revision(self) -> int: 
        """
        Returns modification counter
        """
    def SetAngle(self,theAngle : float) -> None: 
        """
        Angle in radians of the cone created by the spot, should be within range (0.0, M_PI).
        """
    def SetAttenuation(self,theConstAttenuation : float,theLinearAttenuation : float) -> None: 
        """
        Defines the coefficients of attenuation; values should be >= 0.0 and their summ should not be equal to 0.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Defines the color of a light source by giving the basic color.
        """
    def SetConcentration(self,theConcentration : float) -> None: 
        """
        Defines the coefficient of concentration; value should be within range [0.0, 1.0].
        """
    @overload
    def SetDirection(self,theDir : OCP.gp.gp_Dir) -> None: 
        """
        Sets direction of directional/spot light.

        Sets direction of directional/spot light.
        """
    @overload
    def SetDirection(self,theVx : float,theVy : float,theVz : float) -> None: ...
    def SetEnabled(self,theIsOn : bool) -> None: 
        """
        Change enabled state of the light state. This call does not remove or deactivate light source in Views/Viewers; instead it turns it OFF so that it just have no effect.
        """
    def SetHeadlight(self,theValue : bool) -> None: 
        """
        Setup headlight flag.
        """
    def SetIntensity(self,theValue : float) -> None: 
        """
        Modifies the intensity of light source, which should be > 0.0.
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets light source name.
        """
    @overload
    def SetPosition(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Setup location of positional/spot light.

        Setup location of positional/spot light.
        """
    @overload
    def SetPosition(self,thePosition : OCP.gp.gp_Pnt) -> None: ...
    def SetRange(self,theValue : float) -> None: 
        """
        Modifies maximum distance on which point light source affects to objects and is considered during illumination calculations. Positional and spot lights are only point light sources. 0.0 means disabling range considering at all without any distance limits.
        """
    def SetSmoothAngle(self,theValue : float) -> None: 
        """
        Modifies the smoothing angle (in radians) of directional light source; should be within range [0.0, M_PI/2].
        """
    def SetSmoothRadius(self,theValue : float) -> None: 
        """
        Modifies the smoothing radius of positional/spot light; should be >= 0.0.
        """
    def Smoothness(self) -> float: 
        """
        Returns the smoothness of light source (either smoothing angle for directional light or smoothing radius in case of positional light); 0.0 by default.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.Graphic3d.Graphic3d_TypeOfLightSource: 
        """
        Returns the Type of the Light, cannot be changed after object construction.
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
class V3d_ImageDumpOptions():
    """
    The structure defines options for image dump functionality.
    """
    def __init__(self) -> None: ...
    @property
    def BufferType(self) -> OCP.Graphic3d.Graphic3d_BufferType:
        """
        :type: OCP.Graphic3d.Graphic3d_BufferType
        """
    @BufferType.setter
    def BufferType(self, arg0: OCP.Graphic3d.Graphic3d_BufferType) -> None:
        pass
    @property
    def Height(self) -> int:
        """
        :type: int
        """
    @Height.setter
    def Height(self, arg0: int) -> None:
        pass
    @property
    def StereoOptions(self) -> V3d_StereoDumpOptions:
        """
        :type: V3d_StereoDumpOptions
        """
    @StereoOptions.setter
    def StereoOptions(self, arg0: V3d_StereoDumpOptions) -> None:
        pass
    @property
    def TileSize(self) -> int:
        """
        :type: int
        """
    @TileSize.setter
    def TileSize(self, arg0: int) -> None:
        pass
    @property
    def ToAdjustAspect(self) -> bool:
        """
        :type: bool
        """
    @ToAdjustAspect.setter
    def ToAdjustAspect(self, arg0: bool) -> None:
        pass
    @property
    def Width(self) -> int:
        """
        :type: int
        """
    @Width.setter
    def Width(self, arg0: int) -> None:
        pass
    pass
class V3d_ListOfLight(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : V3d_ListOfLight) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.Graphic3d.Graphic3d_CLight,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : OCP.Graphic3d.Graphic3d_CLight) -> OCP.Graphic3d.Graphic3d_CLight: ...
    def Assign(self,theOther : V3d_ListOfLight) -> V3d_ListOfLight: 
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
    def First(self) -> OCP.Graphic3d.Graphic3d_CLight: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.Graphic3d.Graphic3d_CLight,theIter : Any) -> OCP.Graphic3d.Graphic3d_CLight: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : V3d_ListOfLight,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : V3d_ListOfLight,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : OCP.Graphic3d.Graphic3d_CLight,theIter : Any) -> OCP.Graphic3d.Graphic3d_CLight: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.Graphic3d.Graphic3d_CLight: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.Graphic3d.Graphic3d_CLight) -> OCP.Graphic3d.Graphic3d_CLight: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : V3d_ListOfLight) -> None: ...
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
    def __init__(self,theOther : V3d_ListOfLight) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class V3d_ListOfView(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : V3d_View,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : V3d_View) -> V3d_View: ...
    @overload
    def Append(self,theOther : V3d_ListOfView) -> None: ...
    def Assign(self,theOther : V3d_ListOfView) -> V3d_ListOfView: 
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
    def First(self) -> V3d_View: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : V3d_View,theIter : Any) -> V3d_View: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : V3d_ListOfView,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : V3d_ListOfView,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : V3d_View,theIter : Any) -> V3d_View: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> V3d_View: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : V3d_ListOfView) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : V3d_View) -> V3d_View: ...
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
    def __init__(self,theOther : V3d_ListOfView) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class V3d_Plane(OCP.Standard.Standard_Transient):
    """
    Obsolete clip plane presentation class. Ported on new core of Graphic3d_ClipPlane approach. Please access Graphic3d_ClipPlane via ClipPlane() method to use it for standard clipping workflow. Example of use:Obsolete clip plane presentation class. Ported on new core of Graphic3d_ClipPlane approach. Please access Graphic3d_ClipPlane via ClipPlane() method to use it for standard clipping workflow. Example of use:Obsolete clip plane presentation class. Ported on new core of Graphic3d_ClipPlane approach. Please access Graphic3d_ClipPlane via ClipPlane() method to use it for standard clipping workflow. Example of use:
    """
    def ClipPlane(self) -> OCP.Graphic3d.Graphic3d_ClipPlane: 
        """
        Use this method to pass clipping plane implementation for standard clipping workflow.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Display(self,theView : V3d_View,theColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color) -> None: 
        """
        Display the plane representation in the choosen view.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Erase(self) -> None: 
        """
        Erase the plane representation.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDisplayed(self) -> bool: 
        """
        Returns TRUE when the plane representation is displayed.
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
    def Plane(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parameters of the plane.
        """
    def SetPlane(self,theA : float,theB : float,theC : float,theD : float) -> None: 
        """
        Change plane equation.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theA : float=0.0,theB : float=0.0,theC : float=1.0,theD : float=0.0) -> None: ...
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
class V3d_DirectionalLight(V3d_PositionLight, OCP.Graphic3d.Graphic3d_CLight, OCP.Standard.Standard_Transient):
    """
    Directional light source for a viewer.Directional light source for a viewer.
    """
    def Angle(self) -> float: 
        """
        Returns an angle in radians of the cone created by the spot; 30 degrees by default.
        """
    def Attenuation(self) -> Tuple[float, float]: 
        """
        Returns the attenuation factors.
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the color of the light source; WHITE by default.
        """
    def Concentration(self) -> float: 
        """
        Returns intensity distribution of the spot light, within [0.0, 1.0] range; 1.0 by default. This coefficient should be converted into spotlight exponent within [0.0, 128.0] range: The concentration factor determines the dispersion of the light on the surface, the default value (1.0) corresponds to a minimum of dispersion.
        """
    def ConstAttenuation(self) -> float: 
        """
        Returns constant attenuation factor of positional/spot light source; 1.0f by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns direction of directional/spot light.

        Returns the theVx, theVy, theVz direction of the light source.
        """
    @overload
    def Direction(self) -> Tuple[float, float, float]: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light resource identifier string
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Headlight(self) -> bool: 
        """
        Alias for IsHeadlight().
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intensity(self) -> float: 
        """
        Returns the intensity of light source; 1.0 by default.
        """
    def IsEnabled(self) -> bool: 
        """
        Check that the light source is turned on; TRUE by default. This flag affects all occurrences of light sources, where it was registered and activated; so that it is possible defining an active light in View which is actually in disabled state.
        """
    def IsHeadlight(self) -> bool: 
        """
        Returns true if the light is a headlight; FALSE by default. Headlight flag means that light position/direction are defined not in a World coordinate system, but relative to the camera orientation.
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
    def LinearAttenuation(self) -> float: 
        """
        Returns linear attenuation factor of positional/spot light source; 0.0 by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light source name; empty string by default.
        """
    def PackedColor(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns the color of the light source with dummy Alpha component, which should be ignored.
        """
    def PackedDirectionRange(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns direction of directional/spot light and range for positional/spot light in alpha channel.
        """
    def PackedParams(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Packed light parameters.
        """
    @overload
    def Position(self) -> OCP.gp.gp_Pnt: 
        """
        Returns location of positional/spot light.

        Returns location of positional/spot light; (0, 0, 0) by default.
        """
    @overload
    def Position(self) -> Tuple[float, float, float]: ...
    def Range(self) -> float: 
        """
        Returns maximum distance on which point light source affects to objects and is considered during illumination calculations. 0.0 means disabling range considering at all without any distance limits. Has sense only for point light sources (positional and spot).
        """
    def Revision(self) -> int: 
        """
        Returns modification counter
        """
    def SetAngle(self,theAngle : float) -> None: 
        """
        Angle in radians of the cone created by the spot, should be within range (0.0, M_PI).
        """
    def SetAttenuation(self,theConstAttenuation : float,theLinearAttenuation : float) -> None: 
        """
        Defines the coefficients of attenuation; values should be >= 0.0 and their summ should not be equal to 0.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Defines the color of a light source by giving the basic color.
        """
    def SetConcentration(self,theConcentration : float) -> None: 
        """
        Defines the coefficient of concentration; value should be within range [0.0, 1.0].
        """
    def SetDirection(self,theDirection : V3d_TypeOfOrientation) -> None: 
        """
        Defines the direction of the light source by a predefined orientation.
        """
    def SetEnabled(self,theIsOn : bool) -> None: 
        """
        Change enabled state of the light state. This call does not remove or deactivate light source in Views/Viewers; instead it turns it OFF so that it just have no effect.
        """
    def SetHeadlight(self,theValue : bool) -> None: 
        """
        Setup headlight flag.
        """
    def SetIntensity(self,theValue : float) -> None: 
        """
        Modifies the intensity of light source, which should be > 0.0.
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets light source name.
        """
    @overload
    def SetPosition(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Setup location of positional/spot light.

        Setup location of positional/spot light.
        """
    @overload
    def SetPosition(self,thePosition : OCP.gp.gp_Pnt) -> None: ...
    def SetRange(self,theValue : float) -> None: 
        """
        Modifies maximum distance on which point light source affects to objects and is considered during illumination calculations. Positional and spot lights are only point light sources. 0.0 means disabling range considering at all without any distance limits.
        """
    def SetSmoothAngle(self,theValue : float) -> None: 
        """
        Modifies the smoothing angle (in radians) of directional light source; should be within range [0.0, M_PI/2].
        """
    def SetSmoothRadius(self,theValue : float) -> None: 
        """
        Modifies the smoothing radius of positional/spot light; should be >= 0.0.
        """
    def Smoothness(self) -> float: 
        """
        Returns the smoothness of light source (either smoothing angle for directional light or smoothing radius in case of positional light); 0.0 by default.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.Graphic3d.Graphic3d_TypeOfLightSource: 
        """
        Returns the Type of the Light, cannot be changed after object construction.
        """
    @overload
    def __init__(self,theDirection : V3d_TypeOfOrientation=V3d_TypeOfOrientation.V3d_XposYposZpos,theColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theIsHeadlight : bool=False) -> None: ...
    @overload
    def __init__(self,theDirection : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theIsHeadlight : bool=False) -> None: ...
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
class V3d_PositionalLight(V3d_PositionLight, OCP.Graphic3d.Graphic3d_CLight, OCP.Standard.Standard_Transient):
    """
    Creation and modification of an isolated (positional) light source. It is also defined by the color and two attenuation factors ConstAttentuation() and LinearAttentuation(). The resulting attenuation factor determining the illumination of a surface depends on the following formula: Where Distance is the distance of the isolated source from the surface.Creation and modification of an isolated (positional) light source. It is also defined by the color and two attenuation factors ConstAttentuation() and LinearAttentuation(). The resulting attenuation factor determining the illumination of a surface depends on the following formula: Where Distance is the distance of the isolated source from the surface.
    """
    def Angle(self) -> float: 
        """
        Returns an angle in radians of the cone created by the spot; 30 degrees by default.
        """
    def Attenuation(self) -> Tuple[float, float]: 
        """
        Returns the attenuation factors.
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the color of the light source; WHITE by default.
        """
    def Concentration(self) -> float: 
        """
        Returns intensity distribution of the spot light, within [0.0, 1.0] range; 1.0 by default. This coefficient should be converted into spotlight exponent within [0.0, 128.0] range: The concentration factor determines the dispersion of the light on the surface, the default value (1.0) corresponds to a minimum of dispersion.
        """
    def ConstAttenuation(self) -> float: 
        """
        Returns constant attenuation factor of positional/spot light source; 1.0f by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns direction of directional/spot light.

        Returns the theVx, theVy, theVz direction of the light source.
        """
    @overload
    def Direction(self) -> Tuple[float, float, float]: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light resource identifier string
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Headlight(self) -> bool: 
        """
        Alias for IsHeadlight().
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intensity(self) -> float: 
        """
        Returns the intensity of light source; 1.0 by default.
        """
    def IsEnabled(self) -> bool: 
        """
        Check that the light source is turned on; TRUE by default. This flag affects all occurrences of light sources, where it was registered and activated; so that it is possible defining an active light in View which is actually in disabled state.
        """
    def IsHeadlight(self) -> bool: 
        """
        Returns true if the light is a headlight; FALSE by default. Headlight flag means that light position/direction are defined not in a World coordinate system, but relative to the camera orientation.
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
    def LinearAttenuation(self) -> float: 
        """
        Returns linear attenuation factor of positional/spot light source; 0.0 by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light source name; empty string by default.
        """
    def PackedColor(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns the color of the light source with dummy Alpha component, which should be ignored.
        """
    def PackedDirectionRange(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns direction of directional/spot light and range for positional/spot light in alpha channel.
        """
    def PackedParams(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Packed light parameters.
        """
    @overload
    def Position(self) -> OCP.gp.gp_Pnt: 
        """
        Returns location of positional/spot light.

        Returns location of positional/spot light; (0, 0, 0) by default.
        """
    @overload
    def Position(self) -> Tuple[float, float, float]: ...
    def Range(self) -> float: 
        """
        Returns maximum distance on which point light source affects to objects and is considered during illumination calculations. 0.0 means disabling range considering at all without any distance limits. Has sense only for point light sources (positional and spot).
        """
    def Revision(self) -> int: 
        """
        Returns modification counter
        """
    def SetAngle(self,theAngle : float) -> None: 
        """
        Angle in radians of the cone created by the spot, should be within range (0.0, M_PI).
        """
    def SetAttenuation(self,theConstAttenuation : float,theLinearAttenuation : float) -> None: 
        """
        Defines the coefficients of attenuation; values should be >= 0.0 and their summ should not be equal to 0.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Defines the color of a light source by giving the basic color.
        """
    def SetConcentration(self,theConcentration : float) -> None: 
        """
        Defines the coefficient of concentration; value should be within range [0.0, 1.0].
        """
    @overload
    def SetDirection(self,theDir : OCP.gp.gp_Dir) -> None: 
        """
        Sets direction of directional/spot light.

        Sets direction of directional/spot light.
        """
    @overload
    def SetDirection(self,theVx : float,theVy : float,theVz : float) -> None: ...
    def SetEnabled(self,theIsOn : bool) -> None: 
        """
        Change enabled state of the light state. This call does not remove or deactivate light source in Views/Viewers; instead it turns it OFF so that it just have no effect.
        """
    def SetHeadlight(self,theValue : bool) -> None: 
        """
        Setup headlight flag.
        """
    def SetIntensity(self,theValue : float) -> None: 
        """
        Modifies the intensity of light source, which should be > 0.0.
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets light source name.
        """
    @overload
    def SetPosition(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Setup location of positional/spot light.

        Setup location of positional/spot light.
        """
    @overload
    def SetPosition(self,thePosition : OCP.gp.gp_Pnt) -> None: ...
    def SetRange(self,theValue : float) -> None: 
        """
        Modifies maximum distance on which point light source affects to objects and is considered during illumination calculations. Positional and spot lights are only point light sources. 0.0 means disabling range considering at all without any distance limits.
        """
    def SetSmoothAngle(self,theValue : float) -> None: 
        """
        Modifies the smoothing angle (in radians) of directional light source; should be within range [0.0, M_PI/2].
        """
    def SetSmoothRadius(self,theValue : float) -> None: 
        """
        Modifies the smoothing radius of positional/spot light; should be >= 0.0.
        """
    def Smoothness(self) -> float: 
        """
        Returns the smoothness of light source (either smoothing angle for directional light or smoothing radius in case of positional light); 0.0 by default.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.Graphic3d.Graphic3d_TypeOfLightSource: 
        """
        Returns the Type of the Light, cannot be changed after object construction.
        """
    def __init__(self,thePos : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color) -> None: ...
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
class V3d_RectangularGrid(OCP.Aspect.Aspect_RectangularGrid, OCP.Aspect.Aspect_Grid, OCP.Standard.Standard_Transient):
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
        None
        """
    def DrawMode(self) -> OCP.Aspect.Aspect_GridDrawMode: 
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
        None
        """
    def FirstAngle(self) -> float: 
        """
        returns the x Angle of the grid, relatively to the horizontal.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GraphicValues(self) -> Tuple[float, float, float]: 
        """
        None
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
        None
        """
    def SetDrawMode(self,aDrawMode : OCP.Aspect.Aspect_GridDrawMode) -> None: 
        """
        Change the grid aspect.
        """
    def SetGraphicValues(self,XSize : float,YSize : float,OffSet : float) -> None: 
        """
        None
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
class V3d_SpotLight(V3d_PositionLight, OCP.Graphic3d.Graphic3d_CLight, OCP.Standard.Standard_Transient):
    """
    Creation and modification of a spot. The attenuation factor F determines the illumination of a surface: Where Distance is the distance from the source to the surface. The default values (1.0, 0.0) correspond to a minimum of attenuation. The concentration factor determines the dispersion of the light on the surface, the default value (1.0) corresponds to a minimum of dispersion.Creation and modification of a spot. The attenuation factor F determines the illumination of a surface: Where Distance is the distance from the source to the surface. The default values (1.0, 0.0) correspond to a minimum of attenuation. The concentration factor determines the dispersion of the light on the surface, the default value (1.0) corresponds to a minimum of dispersion.
    """
    def Angle(self) -> float: 
        """
        Returns an angle in radians of the cone created by the spot; 30 degrees by default.
        """
    def Attenuation(self) -> Tuple[float, float]: 
        """
        Returns the attenuation factors.
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the color of the light source; WHITE by default.
        """
    def Concentration(self) -> float: 
        """
        Returns intensity distribution of the spot light, within [0.0, 1.0] range; 1.0 by default. This coefficient should be converted into spotlight exponent within [0.0, 128.0] range: The concentration factor determines the dispersion of the light on the surface, the default value (1.0) corresponds to a minimum of dispersion.
        """
    def ConstAttenuation(self) -> float: 
        """
        Returns constant attenuation factor of positional/spot light source; 1.0f by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Returns direction of directional/spot light.

        Returns the theVx, theVy, theVz direction of the light source.
        """
    @overload
    def Direction(self) -> Tuple[float, float, float]: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light resource identifier string
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Headlight(self) -> bool: 
        """
        Alias for IsHeadlight().
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intensity(self) -> float: 
        """
        Returns the intensity of light source; 1.0 by default.
        """
    def IsEnabled(self) -> bool: 
        """
        Check that the light source is turned on; TRUE by default. This flag affects all occurrences of light sources, where it was registered and activated; so that it is possible defining an active light in View which is actually in disabled state.
        """
    def IsHeadlight(self) -> bool: 
        """
        Returns true if the light is a headlight; FALSE by default. Headlight flag means that light position/direction are defined not in a World coordinate system, but relative to the camera orientation.
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
    def LinearAttenuation(self) -> float: 
        """
        Returns linear attenuation factor of positional/spot light source; 0.0 by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light source name; empty string by default.
        """
    def PackedColor(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns the color of the light source with dummy Alpha component, which should be ignored.
        """
    def PackedDirectionRange(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns direction of directional/spot light and range for positional/spot light in alpha channel.
        """
    def PackedParams(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Packed light parameters.
        """
    @overload
    def Position(self) -> OCP.gp.gp_Pnt: 
        """
        Returns location of positional/spot light.

        Returns location of positional/spot light; (0, 0, 0) by default.
        """
    @overload
    def Position(self) -> Tuple[float, float, float]: ...
    def Range(self) -> float: 
        """
        Returns maximum distance on which point light source affects to objects and is considered during illumination calculations. 0.0 means disabling range considering at all without any distance limits. Has sense only for point light sources (positional and spot).
        """
    def Revision(self) -> int: 
        """
        Returns modification counter
        """
    def SetAngle(self,theAngle : float) -> None: 
        """
        Angle in radians of the cone created by the spot, should be within range (0.0, M_PI).
        """
    def SetAttenuation(self,theConstAttenuation : float,theLinearAttenuation : float) -> None: 
        """
        Defines the coefficients of attenuation; values should be >= 0.0 and their summ should not be equal to 0.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Defines the color of a light source by giving the basic color.
        """
    def SetConcentration(self,theConcentration : float) -> None: 
        """
        Defines the coefficient of concentration; value should be within range [0.0, 1.0].
        """
    def SetDirection(self,theOrientation : V3d_TypeOfOrientation) -> None: 
        """
        Defines the direction of the light source according to a predefined directional vector.
        """
    def SetEnabled(self,theIsOn : bool) -> None: 
        """
        Change enabled state of the light state. This call does not remove or deactivate light source in Views/Viewers; instead it turns it OFF so that it just have no effect.
        """
    def SetHeadlight(self,theValue : bool) -> None: 
        """
        Setup headlight flag.
        """
    def SetIntensity(self,theValue : float) -> None: 
        """
        Modifies the intensity of light source, which should be > 0.0.
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets light source name.
        """
    @overload
    def SetPosition(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Setup location of positional/spot light.

        Setup location of positional/spot light.
        """
    @overload
    def SetPosition(self,thePosition : OCP.gp.gp_Pnt) -> None: ...
    def SetRange(self,theValue : float) -> None: 
        """
        Modifies maximum distance on which point light source affects to objects and is considered during illumination calculations. Positional and spot lights are only point light sources. 0.0 means disabling range considering at all without any distance limits.
        """
    def SetSmoothAngle(self,theValue : float) -> None: 
        """
        Modifies the smoothing angle (in radians) of directional light source; should be within range [0.0, M_PI/2].
        """
    def SetSmoothRadius(self,theValue : float) -> None: 
        """
        Modifies the smoothing radius of positional/spot light; should be >= 0.0.
        """
    def Smoothness(self) -> float: 
        """
        Returns the smoothness of light source (either smoothing angle for directional light or smoothing radius in case of positional light); 0.0 by default.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> OCP.Graphic3d.Graphic3d_TypeOfLightSource: 
        """
        Returns the Type of the Light, cannot be changed after object construction.
        """
    @overload
    def __init__(self,thePos : OCP.gp.gp_Pnt,theDirection : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color) -> None: ...
    @overload
    def __init__(self,thePos : OCP.gp.gp_Pnt,theDirection : V3d_TypeOfOrientation=V3d_TypeOfOrientation.V3d_XnegYnegZpos,theColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color) -> None: ...
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
class V3d_StereoDumpOptions():
    """
    Options to be used with image dumping. Notice that the value will have no effect with disabled stereo output.

    Members:

      V3d_SDO_MONO

      V3d_SDO_LEFT_EYE

      V3d_SDO_RIGHT_EYE

      V3d_SDO_BLENDED
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    V3d_SDO_BLENDED: OCP.V3d.V3d_StereoDumpOptions # value = <V3d_StereoDumpOptions.V3d_SDO_BLENDED: 3>
    V3d_SDO_LEFT_EYE: OCP.V3d.V3d_StereoDumpOptions # value = <V3d_StereoDumpOptions.V3d_SDO_LEFT_EYE: 1>
    V3d_SDO_MONO: OCP.V3d.V3d_StereoDumpOptions # value = <V3d_StereoDumpOptions.V3d_SDO_MONO: 0>
    V3d_SDO_RIGHT_EYE: OCP.V3d.V3d_StereoDumpOptions # value = <V3d_StereoDumpOptions.V3d_SDO_RIGHT_EYE: 2>
    __entries: dict # value = {'V3d_SDO_MONO': (<V3d_StereoDumpOptions.V3d_SDO_MONO: 0>, None), 'V3d_SDO_LEFT_EYE': (<V3d_StereoDumpOptions.V3d_SDO_LEFT_EYE: 1>, None), 'V3d_SDO_RIGHT_EYE': (<V3d_StereoDumpOptions.V3d_SDO_RIGHT_EYE: 2>, None), 'V3d_SDO_BLENDED': (<V3d_StereoDumpOptions.V3d_SDO_BLENDED: 3>, None)}
    __members__: dict # value = {'V3d_SDO_MONO': <V3d_StereoDumpOptions.V3d_SDO_MONO: 0>, 'V3d_SDO_LEFT_EYE': <V3d_StereoDumpOptions.V3d_SDO_LEFT_EYE: 1>, 'V3d_SDO_RIGHT_EYE': <V3d_StereoDumpOptions.V3d_SDO_RIGHT_EYE: 2>, 'V3d_SDO_BLENDED': <V3d_StereoDumpOptions.V3d_SDO_BLENDED: 3>}
    pass
class V3d_Trihedron(OCP.Standard.Standard_Transient):
    """
    Class for presentation of zbuffer trihedron object.Class for presentation of zbuffer trihedron object.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Display(self,theView : V3d_View) -> None: 
        """
        Display trihedron.
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
        Erase trihedron.
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
    def SetArrowDiameter(self,theDiam : float) -> None: 
        """
        Setup the arrow diameter.
        """
    def SetArrowsColor(self,theXColor : OCP.Quantity.Quantity_Color,theYColor : OCP.Quantity.Quantity_Color,theZColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Setup colors of arrows.
        """
    def SetLabelsColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Setup color of text labels.
        """
    def SetNbFacets(self,theNbFacets : int) -> None: 
        """
        Setup the number of facets for tessellation.
        """
    def SetPosition(self,thePosition : OCP.Aspect.Aspect_TypeOfTriedronPosition) -> None: 
        """
        Setup the corner to draw the trihedron.
        """
    def SetScale(self,theScale : float) -> None: 
        """
        Setup the scale factor.
        """
    def SetSizeRatio(self,theRatio : float) -> None: 
        """
        Setup the size ratio factor.
        """
    def SetWireframe(self,theAsWireframe : bool) -> None: 
        """
        Switch wireframe / shaded trihedron.
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
class V3d_TypeOfAxe():
    """
    Determines the axis type through the coordinates X, Y, Z.

    Members:

      V3d_X

      V3d_Y

      V3d_Z
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    V3d_X: OCP.V3d.V3d_TypeOfAxe # value = <V3d_TypeOfAxe.V3d_X: 0>
    V3d_Y: OCP.V3d.V3d_TypeOfAxe # value = <V3d_TypeOfAxe.V3d_Y: 1>
    V3d_Z: OCP.V3d.V3d_TypeOfAxe # value = <V3d_TypeOfAxe.V3d_Z: 2>
    __entries: dict # value = {'V3d_X': (<V3d_TypeOfAxe.V3d_X: 0>, None), 'V3d_Y': (<V3d_TypeOfAxe.V3d_Y: 1>, None), 'V3d_Z': (<V3d_TypeOfAxe.V3d_Z: 2>, None)}
    __members__: dict # value = {'V3d_X': <V3d_TypeOfAxe.V3d_X: 0>, 'V3d_Y': <V3d_TypeOfAxe.V3d_Y: 1>, 'V3d_Z': <V3d_TypeOfAxe.V3d_Z: 2>}
    pass
class V3d_TypeOfBackfacingModel():
    """
    Modes of display of back faces in the view

    Members:

      V3d_TOBM_AUTOMATIC

      V3d_TOBM_ALWAYS_DISPLAYED

      V3d_TOBM_NEVER_DISPLAYED
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    V3d_TOBM_ALWAYS_DISPLAYED: OCP.V3d.V3d_TypeOfBackfacingModel # value = <V3d_TypeOfBackfacingModel.V3d_TOBM_ALWAYS_DISPLAYED: 1>
    V3d_TOBM_AUTOMATIC: OCP.V3d.V3d_TypeOfBackfacingModel # value = <V3d_TypeOfBackfacingModel.V3d_TOBM_AUTOMATIC: 0>
    V3d_TOBM_NEVER_DISPLAYED: OCP.V3d.V3d_TypeOfBackfacingModel # value = <V3d_TypeOfBackfacingModel.V3d_TOBM_NEVER_DISPLAYED: 2>
    __entries: dict # value = {'V3d_TOBM_AUTOMATIC': (<V3d_TypeOfBackfacingModel.V3d_TOBM_AUTOMATIC: 0>, None), 'V3d_TOBM_ALWAYS_DISPLAYED': (<V3d_TypeOfBackfacingModel.V3d_TOBM_ALWAYS_DISPLAYED: 1>, None), 'V3d_TOBM_NEVER_DISPLAYED': (<V3d_TypeOfBackfacingModel.V3d_TOBM_NEVER_DISPLAYED: 2>, None)}
    __members__: dict # value = {'V3d_TOBM_AUTOMATIC': <V3d_TypeOfBackfacingModel.V3d_TOBM_AUTOMATIC: 0>, 'V3d_TOBM_ALWAYS_DISPLAYED': <V3d_TypeOfBackfacingModel.V3d_TOBM_ALWAYS_DISPLAYED: 1>, 'V3d_TOBM_NEVER_DISPLAYED': <V3d_TypeOfBackfacingModel.V3d_TOBM_NEVER_DISPLAYED: 2>}
    pass
class V3d_TypeOfOrientation():
    """
    Determines the type of orientation as a combination of standard DX/DY/DZ directions. This enumeration defines a model orientation looking towards the user's eye, which is an opposition to Camera main direction. For example, V3d_Xneg defines +X Camera main direction.

    Members:

      V3d_Xpos

      V3d_Ypos

      V3d_Zpos

      V3d_Xneg

      V3d_Yneg

      V3d_Zneg

      V3d_XposYpos

      V3d_XposZpos

      V3d_YposZpos

      V3d_XnegYneg

      V3d_XnegYpos

      V3d_XnegZneg

      V3d_XnegZpos

      V3d_YnegZneg

      V3d_YnegZpos

      V3d_XposYneg

      V3d_XposZneg

      V3d_YposZneg

      V3d_XposYposZpos

      V3d_XposYnegZpos

      V3d_XposYposZneg

      V3d_XnegYposZpos

      V3d_XposYnegZneg

      V3d_XnegYposZneg

      V3d_XnegYnegZpos

      V3d_XnegYnegZneg

      V3d_TypeOfOrientation_Zup_AxoLeft

      V3d_TypeOfOrientation_Zup_AxoRight

      V3d_TypeOfOrientation_Zup_Front

      V3d_TypeOfOrientation_Zup_Back

      V3d_TypeOfOrientation_Zup_Top

      V3d_TypeOfOrientation_Zup_Bottom

      V3d_TypeOfOrientation_Zup_Left

      V3d_TypeOfOrientation_Zup_Right

      V3d_TypeOfOrientation_Yup_AxoLeft

      V3d_TypeOfOrientation_Yup_AxoRight

      V3d_TypeOfOrientation_Yup_Front

      V3d_TypeOfOrientation_Yup_Back

      V3d_TypeOfOrientation_Yup_Top

      V3d_TypeOfOrientation_Yup_Bottom

      V3d_TypeOfOrientation_Yup_Left

      V3d_TypeOfOrientation_Yup_Right
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    V3d_TypeOfOrientation_Yup_AxoLeft: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYposZpos: 21>
    V3d_TypeOfOrientation_Yup_AxoRight: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYposZpos: 18>
    V3d_TypeOfOrientation_Yup_Back: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zneg: 5>
    V3d_TypeOfOrientation_Yup_Bottom: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Yneg: 4>
    V3d_TypeOfOrientation_Yup_Front: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zpos: 2>
    V3d_TypeOfOrientation_Yup_Left: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xpos: 0>
    V3d_TypeOfOrientation_Yup_Right: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xneg: 3>
    V3d_TypeOfOrientation_Yup_Top: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Ypos: 1>
    V3d_TypeOfOrientation_Zup_AxoLeft: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYnegZpos: 24>
    V3d_TypeOfOrientation_Zup_AxoRight: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYnegZpos: 19>
    V3d_TypeOfOrientation_Zup_Back: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Ypos: 1>
    V3d_TypeOfOrientation_Zup_Bottom: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zneg: 5>
    V3d_TypeOfOrientation_Zup_Front: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Yneg: 4>
    V3d_TypeOfOrientation_Zup_Left: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xneg: 3>
    V3d_TypeOfOrientation_Zup_Right: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xpos: 0>
    V3d_TypeOfOrientation_Zup_Top: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zpos: 2>
    V3d_Xneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xneg: 3>
    V3d_XnegYneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYneg: 9>
    V3d_XnegYnegZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYnegZneg: 25>
    V3d_XnegYnegZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYnegZpos: 24>
    V3d_XnegYpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYpos: 10>
    V3d_XnegYposZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYposZneg: 23>
    V3d_XnegYposZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYposZpos: 21>
    V3d_XnegZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegZneg: 11>
    V3d_XnegZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegZpos: 12>
    V3d_Xpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xpos: 0>
    V3d_XposYneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYneg: 15>
    V3d_XposYnegZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYnegZneg: 22>
    V3d_XposYnegZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYnegZpos: 19>
    V3d_XposYpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYpos: 6>
    V3d_XposYposZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYposZneg: 20>
    V3d_XposYposZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYposZpos: 18>
    V3d_XposZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposZneg: 16>
    V3d_XposZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposZpos: 7>
    V3d_Yneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Yneg: 4>
    V3d_YnegZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_YnegZneg: 13>
    V3d_YnegZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_YnegZpos: 14>
    V3d_Ypos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Ypos: 1>
    V3d_YposZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_YposZneg: 17>
    V3d_YposZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_YposZpos: 8>
    V3d_Zneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zneg: 5>
    V3d_Zpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zpos: 2>
    __entries: dict # value = {'V3d_Xpos': (<V3d_TypeOfOrientation.V3d_Xpos: 0>, None), 'V3d_Ypos': (<V3d_TypeOfOrientation.V3d_Ypos: 1>, None), 'V3d_Zpos': (<V3d_TypeOfOrientation.V3d_Zpos: 2>, None), 'V3d_Xneg': (<V3d_TypeOfOrientation.V3d_Xneg: 3>, None), 'V3d_Yneg': (<V3d_TypeOfOrientation.V3d_Yneg: 4>, None), 'V3d_Zneg': (<V3d_TypeOfOrientation.V3d_Zneg: 5>, None), 'V3d_XposYpos': (<V3d_TypeOfOrientation.V3d_XposYpos: 6>, None), 'V3d_XposZpos': (<V3d_TypeOfOrientation.V3d_XposZpos: 7>, None), 'V3d_YposZpos': (<V3d_TypeOfOrientation.V3d_YposZpos: 8>, None), 'V3d_XnegYneg': (<V3d_TypeOfOrientation.V3d_XnegYneg: 9>, None), 'V3d_XnegYpos': (<V3d_TypeOfOrientation.V3d_XnegYpos: 10>, None), 'V3d_XnegZneg': (<V3d_TypeOfOrientation.V3d_XnegZneg: 11>, None), 'V3d_XnegZpos': (<V3d_TypeOfOrientation.V3d_XnegZpos: 12>, None), 'V3d_YnegZneg': (<V3d_TypeOfOrientation.V3d_YnegZneg: 13>, None), 'V3d_YnegZpos': (<V3d_TypeOfOrientation.V3d_YnegZpos: 14>, None), 'V3d_XposYneg': (<V3d_TypeOfOrientation.V3d_XposYneg: 15>, None), 'V3d_XposZneg': (<V3d_TypeOfOrientation.V3d_XposZneg: 16>, None), 'V3d_YposZneg': (<V3d_TypeOfOrientation.V3d_YposZneg: 17>, None), 'V3d_XposYposZpos': (<V3d_TypeOfOrientation.V3d_XposYposZpos: 18>, None), 'V3d_XposYnegZpos': (<V3d_TypeOfOrientation.V3d_XposYnegZpos: 19>, None), 'V3d_XposYposZneg': (<V3d_TypeOfOrientation.V3d_XposYposZneg: 20>, None), 'V3d_XnegYposZpos': (<V3d_TypeOfOrientation.V3d_XnegYposZpos: 21>, None), 'V3d_XposYnegZneg': (<V3d_TypeOfOrientation.V3d_XposYnegZneg: 22>, None), 'V3d_XnegYposZneg': (<V3d_TypeOfOrientation.V3d_XnegYposZneg: 23>, None), 'V3d_XnegYnegZpos': (<V3d_TypeOfOrientation.V3d_XnegYnegZpos: 24>, None), 'V3d_XnegYnegZneg': (<V3d_TypeOfOrientation.V3d_XnegYnegZneg: 25>, None), 'V3d_TypeOfOrientation_Zup_AxoLeft': (<V3d_TypeOfOrientation.V3d_XnegYnegZpos: 24>, None), 'V3d_TypeOfOrientation_Zup_AxoRight': (<V3d_TypeOfOrientation.V3d_XposYnegZpos: 19>, None), 'V3d_TypeOfOrientation_Zup_Front': (<V3d_TypeOfOrientation.V3d_Yneg: 4>, None), 'V3d_TypeOfOrientation_Zup_Back': (<V3d_TypeOfOrientation.V3d_Ypos: 1>, None), 'V3d_TypeOfOrientation_Zup_Top': (<V3d_TypeOfOrientation.V3d_Zpos: 2>, None), 'V3d_TypeOfOrientation_Zup_Bottom': (<V3d_TypeOfOrientation.V3d_Zneg: 5>, None), 'V3d_TypeOfOrientation_Zup_Left': (<V3d_TypeOfOrientation.V3d_Xneg: 3>, None), 'V3d_TypeOfOrientation_Zup_Right': (<V3d_TypeOfOrientation.V3d_Xpos: 0>, None), 'V3d_TypeOfOrientation_Yup_AxoLeft': (<V3d_TypeOfOrientation.V3d_XnegYposZpos: 21>, None), 'V3d_TypeOfOrientation_Yup_AxoRight': (<V3d_TypeOfOrientation.V3d_XposYposZpos: 18>, None), 'V3d_TypeOfOrientation_Yup_Front': (<V3d_TypeOfOrientation.V3d_Zpos: 2>, None), 'V3d_TypeOfOrientation_Yup_Back': (<V3d_TypeOfOrientation.V3d_Zneg: 5>, None), 'V3d_TypeOfOrientation_Yup_Top': (<V3d_TypeOfOrientation.V3d_Ypos: 1>, None), 'V3d_TypeOfOrientation_Yup_Bottom': (<V3d_TypeOfOrientation.V3d_Yneg: 4>, None), 'V3d_TypeOfOrientation_Yup_Left': (<V3d_TypeOfOrientation.V3d_Xpos: 0>, None), 'V3d_TypeOfOrientation_Yup_Right': (<V3d_TypeOfOrientation.V3d_Xneg: 3>, None)}
    __members__: dict # value = {'V3d_Xpos': <V3d_TypeOfOrientation.V3d_Xpos: 0>, 'V3d_Ypos': <V3d_TypeOfOrientation.V3d_Ypos: 1>, 'V3d_Zpos': <V3d_TypeOfOrientation.V3d_Zpos: 2>, 'V3d_Xneg': <V3d_TypeOfOrientation.V3d_Xneg: 3>, 'V3d_Yneg': <V3d_TypeOfOrientation.V3d_Yneg: 4>, 'V3d_Zneg': <V3d_TypeOfOrientation.V3d_Zneg: 5>, 'V3d_XposYpos': <V3d_TypeOfOrientation.V3d_XposYpos: 6>, 'V3d_XposZpos': <V3d_TypeOfOrientation.V3d_XposZpos: 7>, 'V3d_YposZpos': <V3d_TypeOfOrientation.V3d_YposZpos: 8>, 'V3d_XnegYneg': <V3d_TypeOfOrientation.V3d_XnegYneg: 9>, 'V3d_XnegYpos': <V3d_TypeOfOrientation.V3d_XnegYpos: 10>, 'V3d_XnegZneg': <V3d_TypeOfOrientation.V3d_XnegZneg: 11>, 'V3d_XnegZpos': <V3d_TypeOfOrientation.V3d_XnegZpos: 12>, 'V3d_YnegZneg': <V3d_TypeOfOrientation.V3d_YnegZneg: 13>, 'V3d_YnegZpos': <V3d_TypeOfOrientation.V3d_YnegZpos: 14>, 'V3d_XposYneg': <V3d_TypeOfOrientation.V3d_XposYneg: 15>, 'V3d_XposZneg': <V3d_TypeOfOrientation.V3d_XposZneg: 16>, 'V3d_YposZneg': <V3d_TypeOfOrientation.V3d_YposZneg: 17>, 'V3d_XposYposZpos': <V3d_TypeOfOrientation.V3d_XposYposZpos: 18>, 'V3d_XposYnegZpos': <V3d_TypeOfOrientation.V3d_XposYnegZpos: 19>, 'V3d_XposYposZneg': <V3d_TypeOfOrientation.V3d_XposYposZneg: 20>, 'V3d_XnegYposZpos': <V3d_TypeOfOrientation.V3d_XnegYposZpos: 21>, 'V3d_XposYnegZneg': <V3d_TypeOfOrientation.V3d_XposYnegZneg: 22>, 'V3d_XnegYposZneg': <V3d_TypeOfOrientation.V3d_XnegYposZneg: 23>, 'V3d_XnegYnegZpos': <V3d_TypeOfOrientation.V3d_XnegYnegZpos: 24>, 'V3d_XnegYnegZneg': <V3d_TypeOfOrientation.V3d_XnegYnegZneg: 25>, 'V3d_TypeOfOrientation_Zup_AxoLeft': <V3d_TypeOfOrientation.V3d_XnegYnegZpos: 24>, 'V3d_TypeOfOrientation_Zup_AxoRight': <V3d_TypeOfOrientation.V3d_XposYnegZpos: 19>, 'V3d_TypeOfOrientation_Zup_Front': <V3d_TypeOfOrientation.V3d_Yneg: 4>, 'V3d_TypeOfOrientation_Zup_Back': <V3d_TypeOfOrientation.V3d_Ypos: 1>, 'V3d_TypeOfOrientation_Zup_Top': <V3d_TypeOfOrientation.V3d_Zpos: 2>, 'V3d_TypeOfOrientation_Zup_Bottom': <V3d_TypeOfOrientation.V3d_Zneg: 5>, 'V3d_TypeOfOrientation_Zup_Left': <V3d_TypeOfOrientation.V3d_Xneg: 3>, 'V3d_TypeOfOrientation_Zup_Right': <V3d_TypeOfOrientation.V3d_Xpos: 0>, 'V3d_TypeOfOrientation_Yup_AxoLeft': <V3d_TypeOfOrientation.V3d_XnegYposZpos: 21>, 'V3d_TypeOfOrientation_Yup_AxoRight': <V3d_TypeOfOrientation.V3d_XposYposZpos: 18>, 'V3d_TypeOfOrientation_Yup_Front': <V3d_TypeOfOrientation.V3d_Zpos: 2>, 'V3d_TypeOfOrientation_Yup_Back': <V3d_TypeOfOrientation.V3d_Zneg: 5>, 'V3d_TypeOfOrientation_Yup_Top': <V3d_TypeOfOrientation.V3d_Ypos: 1>, 'V3d_TypeOfOrientation_Yup_Bottom': <V3d_TypeOfOrientation.V3d_Yneg: 4>, 'V3d_TypeOfOrientation_Yup_Left': <V3d_TypeOfOrientation.V3d_Xpos: 0>, 'V3d_TypeOfOrientation_Yup_Right': <V3d_TypeOfOrientation.V3d_Xneg: 3>}
    pass
class V3d_TypeOfPickCamera():
    """
    None

    Members:

      V3d_POSITIONCAMERA

      V3d_SPACECAMERA

      V3d_RADIUSTEXTCAMERA

      V3d_ExtRADIUSCAMERA

      V3d_IntRADIUSCAMERA

      V3d_NOTHINGCAMERA
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    V3d_ExtRADIUSCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_ExtRADIUSCAMERA: 3>
    V3d_IntRADIUSCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_IntRADIUSCAMERA: 4>
    V3d_NOTHINGCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_NOTHINGCAMERA: 5>
    V3d_POSITIONCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_POSITIONCAMERA: 0>
    V3d_RADIUSTEXTCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_RADIUSTEXTCAMERA: 2>
    V3d_SPACECAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_SPACECAMERA: 1>
    __entries: dict # value = {'V3d_POSITIONCAMERA': (<V3d_TypeOfPickCamera.V3d_POSITIONCAMERA: 0>, None), 'V3d_SPACECAMERA': (<V3d_TypeOfPickCamera.V3d_SPACECAMERA: 1>, None), 'V3d_RADIUSTEXTCAMERA': (<V3d_TypeOfPickCamera.V3d_RADIUSTEXTCAMERA: 2>, None), 'V3d_ExtRADIUSCAMERA': (<V3d_TypeOfPickCamera.V3d_ExtRADIUSCAMERA: 3>, None), 'V3d_IntRADIUSCAMERA': (<V3d_TypeOfPickCamera.V3d_IntRADIUSCAMERA: 4>, None), 'V3d_NOTHINGCAMERA': (<V3d_TypeOfPickCamera.V3d_NOTHINGCAMERA: 5>, None)}
    __members__: dict # value = {'V3d_POSITIONCAMERA': <V3d_TypeOfPickCamera.V3d_POSITIONCAMERA: 0>, 'V3d_SPACECAMERA': <V3d_TypeOfPickCamera.V3d_SPACECAMERA: 1>, 'V3d_RADIUSTEXTCAMERA': <V3d_TypeOfPickCamera.V3d_RADIUSTEXTCAMERA: 2>, 'V3d_ExtRADIUSCAMERA': <V3d_TypeOfPickCamera.V3d_ExtRADIUSCAMERA: 3>, 'V3d_IntRADIUSCAMERA': <V3d_TypeOfPickCamera.V3d_IntRADIUSCAMERA: 4>, 'V3d_NOTHINGCAMERA': <V3d_TypeOfPickCamera.V3d_NOTHINGCAMERA: 5>}
    pass
class V3d_TypeOfPickLight():
    """
    None

    Members:

      V3d_POSITIONLIGHT

      V3d_SPACELIGHT

      V3d_RADIUSTEXTLIGHT

      V3d_ExtRADIUSLIGHT

      V3d_IntRADIUSLIGHT

      V3d_NOTHING
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    V3d_ExtRADIUSLIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_ExtRADIUSLIGHT: 3>
    V3d_IntRADIUSLIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_IntRADIUSLIGHT: 4>
    V3d_NOTHING: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_NOTHING: 5>
    V3d_POSITIONLIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_POSITIONLIGHT: 0>
    V3d_RADIUSTEXTLIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_RADIUSTEXTLIGHT: 2>
    V3d_SPACELIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_SPACELIGHT: 1>
    __entries: dict # value = {'V3d_POSITIONLIGHT': (<V3d_TypeOfPickLight.V3d_POSITIONLIGHT: 0>, None), 'V3d_SPACELIGHT': (<V3d_TypeOfPickLight.V3d_SPACELIGHT: 1>, None), 'V3d_RADIUSTEXTLIGHT': (<V3d_TypeOfPickLight.V3d_RADIUSTEXTLIGHT: 2>, None), 'V3d_ExtRADIUSLIGHT': (<V3d_TypeOfPickLight.V3d_ExtRADIUSLIGHT: 3>, None), 'V3d_IntRADIUSLIGHT': (<V3d_TypeOfPickLight.V3d_IntRADIUSLIGHT: 4>, None), 'V3d_NOTHING': (<V3d_TypeOfPickLight.V3d_NOTHING: 5>, None)}
    __members__: dict # value = {'V3d_POSITIONLIGHT': <V3d_TypeOfPickLight.V3d_POSITIONLIGHT: 0>, 'V3d_SPACELIGHT': <V3d_TypeOfPickLight.V3d_SPACELIGHT: 1>, 'V3d_RADIUSTEXTLIGHT': <V3d_TypeOfPickLight.V3d_RADIUSTEXTLIGHT: 2>, 'V3d_ExtRADIUSLIGHT': <V3d_TypeOfPickLight.V3d_ExtRADIUSLIGHT: 3>, 'V3d_IntRADIUSLIGHT': <V3d_TypeOfPickLight.V3d_IntRADIUSLIGHT: 4>, 'V3d_NOTHING': <V3d_TypeOfPickLight.V3d_NOTHING: 5>}
    pass
class V3d_TypeOfRepresentation():
    """
    None

    Members:

      V3d_SIMPLE

      V3d_COMPLETE

      V3d_PARTIAL

      V3d_SAMELAST
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    V3d_COMPLETE: OCP.V3d.V3d_TypeOfRepresentation # value = <V3d_TypeOfRepresentation.V3d_COMPLETE: 1>
    V3d_PARTIAL: OCP.V3d.V3d_TypeOfRepresentation # value = <V3d_TypeOfRepresentation.V3d_PARTIAL: 2>
    V3d_SAMELAST: OCP.V3d.V3d_TypeOfRepresentation # value = <V3d_TypeOfRepresentation.V3d_SAMELAST: 3>
    V3d_SIMPLE: OCP.V3d.V3d_TypeOfRepresentation # value = <V3d_TypeOfRepresentation.V3d_SIMPLE: 0>
    __entries: dict # value = {'V3d_SIMPLE': (<V3d_TypeOfRepresentation.V3d_SIMPLE: 0>, None), 'V3d_COMPLETE': (<V3d_TypeOfRepresentation.V3d_COMPLETE: 1>, None), 'V3d_PARTIAL': (<V3d_TypeOfRepresentation.V3d_PARTIAL: 2>, None), 'V3d_SAMELAST': (<V3d_TypeOfRepresentation.V3d_SAMELAST: 3>, None)}
    __members__: dict # value = {'V3d_SIMPLE': <V3d_TypeOfRepresentation.V3d_SIMPLE: 0>, 'V3d_COMPLETE': <V3d_TypeOfRepresentation.V3d_COMPLETE: 1>, 'V3d_PARTIAL': <V3d_TypeOfRepresentation.V3d_PARTIAL: 2>, 'V3d_SAMELAST': <V3d_TypeOfRepresentation.V3d_SAMELAST: 3>}
    pass
class V3d_TypeOfView():
    """
    Defines the type of projection of the view.

    Members:

      V3d_ORTHOGRAPHIC

      V3d_PERSPECTIVE
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    V3d_ORTHOGRAPHIC: OCP.V3d.V3d_TypeOfView # value = <V3d_TypeOfView.V3d_ORTHOGRAPHIC: 0>
    V3d_PERSPECTIVE: OCP.V3d.V3d_TypeOfView # value = <V3d_TypeOfView.V3d_PERSPECTIVE: 1>
    __entries: dict # value = {'V3d_ORTHOGRAPHIC': (<V3d_TypeOfView.V3d_ORTHOGRAPHIC: 0>, None), 'V3d_PERSPECTIVE': (<V3d_TypeOfView.V3d_PERSPECTIVE: 1>, None)}
    __members__: dict # value = {'V3d_ORTHOGRAPHIC': <V3d_TypeOfView.V3d_ORTHOGRAPHIC: 0>, 'V3d_PERSPECTIVE': <V3d_TypeOfView.V3d_PERSPECTIVE: 1>}
    pass
class V3d_TypeOfVisualization():
    """
    Determines the type of visualization in the view, either WIREFRAME or ZBUFFER (shading).

    Members:

      V3d_WIREFRAME

      V3d_ZBUFFER
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    V3d_WIREFRAME: OCP.V3d.V3d_TypeOfVisualization # value = <V3d_TypeOfVisualization.V3d_WIREFRAME: 0>
    V3d_ZBUFFER: OCP.V3d.V3d_TypeOfVisualization # value = <V3d_TypeOfVisualization.V3d_ZBUFFER: 1>
    __entries: dict # value = {'V3d_WIREFRAME': (<V3d_TypeOfVisualization.V3d_WIREFRAME: 0>, None), 'V3d_ZBUFFER': (<V3d_TypeOfVisualization.V3d_ZBUFFER: 1>, None)}
    __members__: dict # value = {'V3d_WIREFRAME': <V3d_TypeOfVisualization.V3d_WIREFRAME: 0>, 'V3d_ZBUFFER': <V3d_TypeOfVisualization.V3d_ZBUFFER: 1>}
    pass
class V3d_UnMapped(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.V3d', '__weakref__': <attribute '__weakref__' of 'V3d_UnMapped' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'V3d_UnMapped' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class V3d_View(OCP.Standard.Standard_Transient):
    """
    Defines the application object VIEW for the VIEWER application. The methods of this class allow the editing and inquiring the parameters linked to the view. Provides a set of services common to all types of view. Warning: The default parameters are defined by the class Viewer (Example : SetDefaultViewSize()). Certain methods are mouse oriented, and it is necessary to know the difference between the start and the continuation of this gesture in putting the method into operation. Example : Shifting the eye-view along the screen axes.Defines the application object VIEW for the VIEWER application. The methods of this class allow the editing and inquiring the parameters linked to the view. Provides a set of services common to all types of view. Warning: The default parameters are defined by the class Viewer (Example : SetDefaultViewSize()). Certain methods are mouse oriented, and it is necessary to know the difference between the start and the continuation of this gesture in putting the method into operation. Example : Shifting the eye-view along the screen axes.Defines the application object VIEW for the VIEWER application. The methods of this class allow the editing and inquiring the parameters linked to the view. Provides a set of services common to all types of view. Warning: The default parameters are defined by the class Viewer (Example : SetDefaultViewSize()). Certain methods are mouse oriented, and it is necessary to know the difference between the start and the continuation of this gesture in putting the method into operation. Example : Shifting the eye-view along the screen axes.
    """
    def ActiveLight(self) -> OCP.Graphic3d.Graphic3d_CLight: 
        """
        None
        """
    def ActiveLightIterator(self) -> Any: 
        """
        Return iterator for defined lights.
        """
    def ActiveLights(self) -> V3d_ListOfLight: 
        """
        Returns a list of active lights.
        """
    def AddClipPlane(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> None: 
        """
        Adds clip plane to the view. The composition of clip planes truncates the rendering space to convex volume. Number of supported clip planes can be consulted by PlaneLimit method of associated Graphic3d_GraphicDriver. Please be aware that the planes which exceed the limit are ignored during rendering.
        """
    def At(self) -> Tuple[float, float, float]: 
        """
        Returns the position of the view point.
        """
    def AutoZFit(self) -> None: 
        """
        If automatic z-range fitting is turned on, adjusts Z-min and Z-max projection volume planes with call to ZFitAll.
        """
    def AutoZFitMode(self) -> bool: 
        """
        returns TRUE if automatic z-fit mode is turned on.
        """
    def AutoZFitScaleFactor(self) -> float: 
        """
        returns scale factor parameter of automatic z-fit mode.
        """
    @overload
    def AxialScale(self) -> Tuple[float, float, float]: 
        """
        Performs anisotropic scaling of <me> view along the given <Axis>. The scale factor is calculated on a basis of the mouse pointer displacement <Dx,Dy>. The calculated scale factor is then passed to SetAxialScale(Sx, Sy, Sz) method.

        Returns the current values of the anisotropic (axial) scale factors.
        """
    @overload
    def AxialScale(self,Dx : int,Dy : int,Axis : V3d_TypeOfAxe) -> None: ...
    def BackFacingModel(self) -> V3d_TypeOfBackfacingModel: 
        """
        Returns current state of the back faces display
        """
    @overload
    def BackgroundColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the Background color object of the view.

        Returns the Background color values of the view depending of the color Type.
        """
    @overload
    def BackgroundColor(self,Type : OCP.Quantity.Quantity_TypeOfColor) -> Tuple[float, float, float]: ...
    def Camera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Returns camera object of the view.
        """
    def ChangeRenderingParams(self) -> OCP.Graphic3d.Graphic3d_RenderingParams: 
        """
        Returns reference to current rendering parameters and effect settings.
        """
    def ClearPBREnvironment(self,theToUpdate : bool=False) -> None: 
        """
        Fills PBR specular probe and irradiance map with white color. So that environment indirect illumination will be constant and will be fully controlled by ambient light sources. If PBR is unavailable it does nothing.
        """
    def ClipPlanes(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Get clip planes.
        """
    def ComputedMode(self) -> bool: 
        """
        Returns the computed HLR mode state.
        """
    @overload
    def Convert(self,Vv : float) -> int: 
        """
        Converts the PIXEL value to a value in the projection plane.

        Converts tha value of the projection plane into a PIXEL value.

        Converts the point PIXEL into a point projected in the reference frame of the projection plane.

        Converts the point defined in the reference frame of the projection plane into a point PIXEL.

        Converts the projected point into a point in the reference frame of the view corresponding to the intersection with the projection plane of the eye/view point vector.

        Projects the point defined in the reference frame of the view into the projected point in the associated window.
        """
    @overload
    def Convert(self,Xp : int,Yp : int) -> Tuple[float, float, float]: ...
    @overload
    def Convert(self,Xv : float,Yv : float) -> Tuple[int, int]: ...
    @overload
    def Convert(self,X : float,Y : float,Z : float) -> Tuple[int, int]: ...
    @overload
    def Convert(self,Vp : int) -> float: ...
    @overload
    def Convert(self,Xp : int,Yp : int) -> Tuple[float, float]: ...
    @overload
    def ConvertToGrid(self,Xp : int,Yp : int) -> Tuple[float, float, float]: 
        """
        Converts the projected point into the nearest grid point in the reference frame of the view corresponding to the intersection with the projection plane of the eye/view point vector and display the grid marker. Warning: When the grid is not active the result is identical to the above Convert() method. How to use: 1) Enable the grid echo display myViewer->SetGridEcho(Standard_True); 2) When application receive a move event: 2.1) Check if any object is detected if( myInteractiveContext->MoveTo(x,y) == AIS_SOD_Nothing ) { 2.2) Check if the grid is active if( myViewer->Grid()->IsActive() ) { 2.3) Display the grid echo and gets the grid point myView->ConvertToGrid(x,y,X,Y,Z); myView->Viewer()->ShowGridEcho (myView, Graphic3d_Vertex (X,Y,Z)); myView->RedrawImmediate(); 2.4) Else this is the standard case } else myView->Convert(x,y,X,Y,Z);

        Converts the point into the nearest grid point and display the grid marker.
        """
    @overload
    def ConvertToGrid(self,X : float,Y : float,Z : float) -> Tuple[float, float, float]: ...
    def ConvertWithProj(self,Xp : int,Yp : int) -> Tuple[float, float, float, float, float, float]: 
        """
        Converts the projected point into a point in the reference frame of the view corresponding to the intersection with the projection plane of the eye/view point vector and returns the projection ray for further computations.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultCamera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Return default camera.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Depth(self) -> float: 
        """
        Returns the Distance between the Eye and View Point.
        """
    def DepthFitAll(self,Aspect : float=0.01,Margin : float=0.01) -> None: 
        """
        Adjusts the viewing volume so as not to clip the displayed objects by front and back and back clipping planes. Also sets depth value automatically depending on the calculated Z size and Aspect parameter. NOTE than the original XY size of the view is NOT modified .
        """
    def DiagnosticInformation(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString,theFlags : OCP.Graphic3d.Graphic3d_DiagnosticInfo) -> None: 
        """
        Fill in the dictionary with diagnostic info. Should be called within rendering thread.
        """
    def DoMapping(self) -> None: 
        """
        Must be called when the window supporting the view is mapped or unmapped.
        """
    def Dump(self,theFile : str,theBufferType : OCP.Graphic3d.Graphic3d_BufferType=Graphic3d_BufferType.Graphic3d_BT_RGB) -> bool: 
        """
        Dumps the full contents of the View into the image file. This is an alias for ToPixMap() with Image_AlienPixMap.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Eye(self) -> Tuple[float, float, float]: 
        """
        Returns the position of the eye.
        """
    @overload
    def FitAll(self,theMinXv : float,theMinYv : float,theMaxXv : float,theMaxYv : float) -> None: 
        """
        Adjust view parameters to fit the displayed scene, respecting height / width ratio. The Z clipping range (depth range) is fitted if AutoZFit flag is TRUE. Throws program error exception if margin coefficient is < 0 or >= 1. Updates the view.

        Adjust view parameters to fit the displayed scene, respecting height / width ratio according to the custom bounding box given. Throws program error exception if margin coefficient is < 0 or >= 1. Updates the view.

        Centers the defined projection window so that it occupies the maximum space while respecting the initial height/width ratio. NOTE than the original Z size of the view is NOT modified .
        """
    @overload
    def FitAll(self,theMargin : float=0.01,theToUpdate : bool=True) -> None: ...
    @overload
    def FitAll(self,theBox : OCP.Bnd.Bnd_Box,theMargin : float=0.01,theToUpdate : bool=True) -> None: ...
    def FitMinMax(self,theCamera : OCP.Graphic3d.Graphic3d_Camera,theBox : OCP.Bnd.Bnd_Box,theMargin : float,theResolution : float=0.0,theToEnlargeIfLine : bool=True) -> bool: 
        """
        Transform camera eye, center and scale to fit in the passed bounding box specified in WCS.
        """
    def FocalReferencePoint(self) -> Tuple[float, float, float]: 
        """
        Returns the position of point which emanating the projections.
        """
    def Focale(self) -> float: 
        """
        Returns the View Plane Distance for Perspective Views
        """
    def GeneratePBREnvironment(self,theToUpdate : bool=False) -> None: 
        """
        Generates PBR specular probe and irradiance map in order to provide environment indirect illumination in PBR shading model (Image Based Lighting). The source of environment data is background cubemap. If PBR is unavailable it does nothing. If PBR is available but there is no cubemap being set to background it clears all IBL maps (see 'ClearPBREnvironment').
        """
    def GetGraduatedTrihedron(self) -> OCP.Graphic3d.Graphic3d_GraduatedTrihedron: 
        """
        Returns data of a graduated trihedron.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GradientBackground(self) -> OCP.Aspect.Aspect_GradientBackground: 
        """
        Returns the gradient background of the view.
        """
    def GradientBackgroundColors(self,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns the gradient background colors of the view.
        """
    def GraduatedTrihedronDisplay(self,theTrihedronData : OCP.Graphic3d.Graphic3d_GraduatedTrihedron) -> None: 
        """
        Displays a graduated trihedron.
        """
    def GraduatedTrihedronErase(self) -> None: 
        """
        Erases a graduated trihedron from the view.
        """
    def GravityPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the Objects number and the gravity center of ALL viewable points in the view
        """
    def IfMoreLights(self) -> bool: 
        """
        Returns True if One light more can be activated in this View.
        """
    def IfWindow(self) -> bool: 
        """
        Returns True if MyView is associated with a window .
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitActiveLights(self) -> None: 
        """
        initializes an iteration on the active Lights.
        """
    def Invalidate(self) -> None: 
        """
        Invalidates view content but does not redraw it.
        """
    def InvalidateImmediate(self) -> None: 
        """
        Invalidates view content within immediate layer but does not redraw it.
        """
    def IsActiveLight(self,theLight : OCP.Graphic3d.Graphic3d_CLight) -> bool: 
        """
        Returns TRUE when the light is active in this view.
        """
    def IsCullingEnabled(self) -> bool: 
        """
        Returns flag value of objects culling mechanism
        """
    def IsEmpty(self) -> bool: 
        """
        Returns the status of the view regarding the displayed structures inside Returns True is The View is empty
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInvalidated(self) -> bool: 
        """
        Returns true if cached view content has been invalidated.
        """
    def IsInvalidatedImmediate(self) -> bool: 
        """
        Returns true if immediate layer content has been invalidated.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def LightLimit(self) -> int: 
        """
        Returns the MAX number of light associated to the view.
        """
    def MoreActiveLights(self) -> bool: 
        """
        returns true if there are more active Light(s) to return.
        """
    @overload
    def Move(self,Length : float,Start : bool=True) -> None: 
        """
        Movement of the eye parallel to the coordinate system of reference of the screen a distance relative to the initial position expressed by Start = Standard_True.

        Movement of the eye parallel to one of the axes of the coordinate system of reference of the view a distance relative to the initial position expressed by Start = Standard_True.

        Movement of the eye parllel to the current axis a distance relative to the initial position expressed by Start = Standard_True
        """
    @overload
    def Move(self,Axe : V3d_TypeOfAxe,Length : float,Start : bool=True) -> None: ...
    @overload
    def Move(self,Dx : float,Dy : float,Dz : float,Start : bool=True) -> None: ...
    def MustBeResized(self) -> None: 
        """
        Must be called when the window supporting the view changes size. if the view is not mapped on a window. Warning: The view is centered and resized to preserve the height/width ratio of the window.
        """
    def NextActiveLights(self) -> None: 
        """
        Go to the next active Light (if there is not, ActiveLight will raise an exception)
        """
    def Pan(self,theDXp : int,theDYp : int,theZoomFactor : float=1.0,theToStart : bool=True) -> None: 
        """
        Translates the center of the view along "x" and "y" axes of view projection. Can be used to perform interactive panning operation. In that case the DXp, DXp parameters specify panning relative to the point where the operation is started.
        """
    def Panning(self,theDXv : float,theDYv : float,theZoomFactor : float=1.0,theToStart : bool=True) -> None: 
        """
        Translates the center of the view along "x" and "y" axes of view projection. Can be used to perform interactive panning operation. In that case the DXv, DXy parameters specify panning relative to the point where the operation is started.
        """
    def Place(self,theXp : int,theYp : int,theZoomFactor : float=1.0) -> None: 
        """
        places the point of the view corresponding at the pixel position x,y at the center of the window and updates the view.
        """
    def PlaneLimit(self) -> int: 
        """
        Returns the MAX number of clipping planes associated to the view.
        """
    def Proj(self) -> Tuple[float, float, float]: 
        """
        Returns the projection vector.
        """
    def ProjReferenceAxe(self,Xpix : int,Ypix : int) -> Tuple[float, float, float, float, float, float]: 
        """
        Returns the coordinate of the point (Xpix,Ypix) in the view (XP,YP,ZP), and the projection vector of the view passing by the point (for PerspectiveView).
        """
    @overload
    def Project(self,theX : float,theY : float,theZ : float) -> Tuple[float, float]: 
        """
        Converts the point defined in the user space of the view to the projection plane at the depth relative to theZ.

        Converts the point defined in the user space of the view to the projection plane at the depth relative to theZ.
        """
    @overload
    def Project(self,theX : float,theY : float,theZ : float) -> Tuple[float, float, float]: ...
    def Redraw(self) -> None: 
        """
        Redisplays the view even if there has not been any modification. Must be called if the view is shown. (Ex: DeIconification ) .
        """
    def RedrawImmediate(self) -> None: 
        """
        Updates layer of immediate presentations.
        """
    def Remove(self) -> None: 
        """
        Destroys the view.
        """
    def RemoveClipPlane(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> None: 
        """
        Removes clip plane from the view.
        """
    def RenderingParams(self) -> OCP.Graphic3d.Graphic3d_RenderingParams: 
        """
        Returns current rendering parameters and effect settings. By default it returns default parameters of current viewer. To define view-specific settings use method V3d_View::ChangeRenderingParams().
        """
    def Reset(self,theToUpdate : bool=True) -> None: 
        """
        Resets the centering and the orientation of the view.
        """
    def ResetViewMapping(self) -> None: 
        """
        Resets the centering of the view. Updates the view
        """
    def ResetViewOrientation(self) -> None: 
        """
        Resets the orientation of the view. Updates the view
        """
    @overload
    def Rotate(self,Axe : V3d_TypeOfAxe,Angle : float,X : float,Y : float,Z : float,Start : bool=True) -> None: 
        """
        Rotates the eye about the coordinate system of reference of the screen for which the origin is the view point of the projection, with a relative angular value in RADIANS with respect to the initial position expressed by Start = Standard_True Warning! raises BadValue from V3d If the eye, the view point, or the high point are aligned or confused.

        Rotates the eye about the coordinate system of reference of the screen for which the origin is Gravity point {X,Y,Z}, with a relative angular value in RADIANS with respect to the initial position expressed by Start = Standard_True If the eye, the view point, or the high point are aligned or confused.

        Rotates the eye about one of the coordinate axes of of the view for which the origin is the Gravity point{X,Y,Z} with an relative angular value in RADIANS with respect to the initial position expressed by Start = Standard_True

        Rotates the eye about one of the coordinate axes of of the view for which the origin is the view point of the projection with an relative angular value in RADIANS with respect to the initial position expressed by Start = Standard_True

        Rotates the eye around the current axis a relative angular value in RADIANS with respect to the initial position expressed by Start = Standard_True
        """
    @overload
    def Rotate(self,Ax : float,Ay : float,Az : float,Start : bool=True) -> None: ...
    @overload
    def Rotate(self,Ax : float,Ay : float,Az : float,X : float,Y : float,Z : float,Start : bool=True) -> None: ...
    @overload
    def Rotate(self,Angle : float,Start : bool=True) -> None: ...
    @overload
    def Rotate(self,Axe : V3d_TypeOfAxe,Angle : float,Start : bool=True) -> None: ...
    def Rotation(self,X : int,Y : int) -> None: 
        """
        Continues the rotation of the view with an angle computed from the last and new mouse position <X,Y>.
        """
    def Scale(self) -> float: 
        """
        Returns the current value of the zoom expressed with respect to SetViewMappingDefault().
        """
    def SetAt(self,X : float,Y : float,Z : float) -> None: 
        """
        Defines the position of the view point.
        """
    def SetAutoZFitMode(self,theIsOn : bool,theScaleFactor : float=1.0) -> None: 
        """
        Sets the automatic z-fit mode and its parameters. The auto z-fit has extra parameters which can controlled from application level to ensure that the size of viewing volume will be sufficiently large to cover the depth of unmanaged objects, for example, transformation persistent ones.
        """
    def SetAxialScale(self,Sx : float,Sy : float,Sz : float) -> None: 
        """
        Sets anisotropic (axial) scale factors <Sx>, <Sy>, <Sz> for view <me>. Anisotropic scaling operation is performed through multiplying the current view orientation matrix by a scaling matrix: || Sx 0 0 0 || || 0 Sy 0 0 || || 0 0 Sz 0 || || 0 0 0 1 || Updates the view.
        """
    def SetAxis(self,X : float,Y : float,Z : float,Vx : float,Vy : float,Vz : float) -> None: 
        """
        Definition of an axis from its origin and its orientation . This will be the current axis for rotations and movements. Warning! raises BadValue from V3d if the vector normal is NULL. .
        """
    def SetBackFacingModel(self,theModel : V3d_TypeOfBackfacingModel=V3d_TypeOfBackfacingModel.V3d_TOBM_AUTOMATIC) -> None: 
        """
        Manages display of the back faces When <aModel> is TOBM_AUTOMATIC the object backfaces are displayed only for surface objects and never displayed for solid objects. this was the previous mode. <aModel> is TOBM_ALWAYS_DISPLAYED the object backfaces are always displayed both for surfaces or solids. <aModel> is TOBM_NEVER_DISPLAYED the object backfaces are never displayed.
        """
    @overload
    def SetBackgroundColor(self,theType : OCP.Quantity.Quantity_TypeOfColor,theV1 : float,theV2 : float,theV3 : float) -> None: 
        """
        Defines the background color of the view by the color definition type and the three corresponding values.

        Defines the background color of the view.
        """
    @overload
    def SetBackgroundColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetBackgroundCubeMap(self,theCubeMap : OCP.Graphic3d.Graphic3d_CubeMap,theToUpdatePBREnv : bool=True,theToUpdate : bool=False) -> None: 
        """
        Sets environment cubemap as background.
        """
    @overload
    def SetBackgroundImage(self,theFileName : str,theFillStyle : OCP.Aspect.Aspect_FillMethod=Aspect_FillMethod.Aspect_FM_CENTERED,theToUpdate : bool=False) -> None: 
        """
        Defines the background texture of the view by supplying the texture image file name and fill method (centered by default).

        Defines the background texture of the view by supplying the texture and fill method (centered by default)
        """
    @overload
    def SetBackgroundImage(self,theTexture : OCP.Graphic3d.Graphic3d_Texture2D,theFillStyle : OCP.Aspect.Aspect_FillMethod=Aspect_FillMethod.Aspect_FM_CENTERED,theToUpdate : bool=False) -> None: ...
    def SetBgGradientColors(self,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color,theFillStyle : OCP.Aspect.Aspect_GradientFillMethod=Aspect_GradientFillMethod.Aspect_GFM_HOR,theToUpdate : bool=False) -> None: 
        """
        Defines the gradient background colors of the view by supplying the colors and the fill method (horizontal by default).
        """
    def SetBgGradientStyle(self,theMethod : OCP.Aspect.Aspect_GradientFillMethod=Aspect_GradientFillMethod.Aspect_GFM_HOR,theToUpdate : bool=False) -> None: 
        """
        Defines the gradient background fill method of the view.
        """
    def SetBgImageStyle(self,theFillStyle : OCP.Aspect.Aspect_FillMethod,theToUpdate : bool=False) -> None: 
        """
        Defines the textured background fill method of the view.
        """
    def SetCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Change camera used by view.
        """
    def SetCenter(self,theXp : int,theYp : int) -> None: 
        """
        Relocates center of screen to the point, determined by {Xp, Yp} pixel coordinates relative to the bottom-left corner of screen. To calculate pixel coordinates for any point from world coordinate space, it can be projected using "Project".
        """
    def SetClipPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Sets sequence of clip planes to the view. The planes that have been set before are removed from the view. The composition of clip planes truncates the rendering space to convex volume. Number of supported clip planes can be consulted by InquirePlaneLimit method of Graphic3d_GraphicDriver. Please be aware that the planes that exceed the limit are ignored during rendering.

        None
        """
    def SetComputedMode(self,theMode : bool) -> None: 
        """
        Switches computed HLR mode in the view.
        """
    def SetDepth(self,Depth : float) -> None: 
        """
        Defines the Depth of the eye from the view point without update the projection .
        """
    def SetEye(self,X : float,Y : float,Z : float) -> None: 
        """
        Defines the position of the eye..
        """
    def SetFocale(self,Focale : float) -> None: 
        """
        Change View Plane Distance for Perspective Views Warning! raises TypeMismatch from Standard if the view is not a perspective view.
        """
    def SetFront(self) -> None: 
        """
        modify the Projection of the view perpendicularly to the privileged plane of the viewer.
        """
    def SetFrustumCulling(self,theMode : bool) -> None: 
        """
        Turn on/off automatic culling of objects outside frustum (ON by default)
        """
    def SetGrid(self,aPlane : OCP.gp.gp_Ax3,aGrid : OCP.Aspect.Aspect_Grid) -> None: 
        """
        Defines or Updates the definition of the grid in <me>
        """
    def SetGridActivity(self,aFlag : bool) -> None: 
        """
        Defines or Updates the activity of the grid in <me>
        """
    def SetImmediateUpdate(self,theImmediateUpdate : bool) -> bool: 
        """
        sets the immediate update mode and returns the previous one.
        """
    @overload
    def SetLightOff(self,theLight : OCP.Graphic3d.Graphic3d_CLight) -> None: 
        """
        Deactivate theLight in this view.

        Deactivate all the Lights defined in this view.
        """
    @overload
    def SetLightOff(self) -> None: ...
    @overload
    def SetLightOn(self) -> None: 
        """
        Activates theLight in the view.

        Activates all the lights defined in this view.
        """
    @overload
    def SetLightOn(self,theLight : OCP.Graphic3d.Graphic3d_CLight) -> None: ...
    def SetMagnify(self,theWindow : OCP.Aspect.Aspect_Window,thePreviousView : V3d_View,theX1 : int,theY1 : int,theX2 : int,theY2 : int) -> None: 
        """
        None
        """
    @overload
    def SetProj(self,theOrientation : V3d_TypeOfOrientation,theIsYup : bool=False) -> None: 
        """
        Defines the orientation of the projection.

        Defines the orientation of the projection .
        """
    @overload
    def SetProj(self,Vx : float,Vy : float,Vz : float) -> None: ...
    def SetScale(self,Coef : float) -> None: 
        """
        Zooms the view by a factor relative to the value initialised by SetViewMappingDefault(). Updates the view.
        """
    def SetShadingModel(self,theShadingModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel) -> None: 
        """
        Defines the shading model for the visualization. Various models are available.
        """
    def SetSize(self,theSize : float) -> None: 
        """
        Defines the view projection size in its maximum dimension, keeping the inital height/width ratio unchanged.
        """
    def SetTextureEnv(self,theTexture : OCP.Graphic3d.Graphic3d_TextureEnv) -> None: 
        """
        Sets the environment texture to use. No environment texture by default.
        """
    def SetTwist(self,Angle : float) -> None: 
        """
        Defines the angular position of the high point of the reference frame of the view with respect to the Y screen axis with an absolute angular value in RADIANS.
        """
    @overload
    def SetUp(self,Orientation : V3d_TypeOfOrientation) -> None: 
        """
        Defines the orientation of the high point.

        Defines the orientation(SO) of the high point.
        """
    @overload
    def SetUp(self,Vx : float,Vy : float,Vz : float) -> None: ...
    def SetViewMappingDefault(self) -> None: 
        """
        Saves the current view mapping. This will be the state returned from ResetViewmapping.
        """
    def SetViewOrientationDefault(self) -> None: 
        """
        Saves the current state of the orientation of the view which will be the return state at ResetViewOrientation.
        """
    def SetVisualization(self,theType : V3d_TypeOfVisualization) -> None: 
        """
        Defines the visualization type in the view.
        """
    def SetWindow(self,theWindow : OCP.Aspect.Aspect_Window,theContext : capsule=None) -> None: 
        """
        Activates the view in the specified Window If <aContext> is not NULL the graphic context is used to draw something in this view. Otherwise an internal graphic context is created. Warning: The view is centered and resized to preserve the height/width ratio of the window.
        """
    def SetZSize(self,SetZSize : float) -> None: 
        """
        Defines the Depth size of the view Front Plane will be set to Size/2. Back Plane will be set to -Size/2. Any Object located Above the Front Plane or behind the Back Plane will be Clipped . NOTE than the XY Size of the View is NOT modified .
        """
    def SetZoom(self,Coef : float,Start : bool=True) -> None: 
        """
        Zooms the view by a factor relative to the initial value expressed by Start = Standard_True Updates the view.
        """
    def ShadingModel(self) -> OCP.Graphic3d.Graphic3d_TypeOfShadingModel: 
        """
        Returns the current shading model.
        """
    def Size(self) -> Tuple[float, float]: 
        """
        Returns the height and width of the view.
        """
    def StartRotation(self,X : int,Y : int,zRotationThreshold : float=0.0) -> None: 
        """
        Begin the rotation of the view around the screen axis according to the mouse position <X,Y>. Warning: Enable rotation around the Z screen axis when <zRotationThreshold> factor is > 0 soon the distance from the start point and the center of the view is > (medium viewSize * <zRotationThreshold> ). Generally a value of 0.4 is usable to rotate around XY screen axis inside the circular threshold area and to rotate around Z screen axis outside this area.
        """
    def StartZoomAtPoint(self,theXp : int,theYp : int) -> None: 
        """
        Defines starting point for ZoomAtPoint view operation.
        """
    @overload
    def StatisticInformation(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns string with statistic performance info.

        Fills in the dictionary with statistic performance info.
        """
    @overload
    def StatisticInformation(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString) -> None: ...
    def TextureEnv(self) -> OCP.Graphic3d.Graphic3d_TextureEnv: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def ToPixMap(self,theImage : OCP.Image.Image_PixMap,theParams : V3d_ImageDumpOptions) -> bool: 
        """
        Dumps the full contents of the view to a pixmap with specified parameters. Internally this method calls Redraw() with an offscreen render buffer of requested target size (theWidth x theHeight), so that there is no need resizing a window control for making a dump of different size.

        Dumps the full contents of the view to a pixmap. Internally this method calls Redraw() with an offscreen render buffer of requested target size (theWidth x theHeight), so that there is no need resizing a window control for making a dump of different size.
        """
    @overload
    def ToPixMap(self,theImage : OCP.Image.Image_PixMap,theWidth : int,theHeight : int,theBufferType : OCP.Graphic3d.Graphic3d_BufferType=Graphic3d_BufferType.Graphic3d_BT_RGB,theToAdjustAspect : bool=True,theStereoOptions : V3d_StereoDumpOptions=V3d_StereoDumpOptions.V3d_SDO_MONO) -> bool: ...
    @overload
    def Translate(self,Length : float,Start : bool=True) -> None: 
        """
        Movement of the ye and the view point parallel to the frame of reference of the screen a distance relative to the initial position expressed by Start = Standard_True

        Movement of the eye and the view point parallel to one of the axes of the fame of reference of the view a distance relative to the initial position expressed by Start = Standard_True

        Movement of the eye and view point parallel to the current axis a distance relative to the initial position expressed by Start = Standard_True
        """
    @overload
    def Translate(self,Axe : V3d_TypeOfAxe,Length : float,Start : bool=True) -> None: ...
    @overload
    def Translate(self,Dx : float,Dy : float,Dz : float,Start : bool=True) -> None: ...
    def TriedronDisplay(self,thePosition : OCP.Aspect.Aspect_TypeOfTriedronPosition=Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER,theColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theScale : float=0.02,theMode : V3d_TypeOfVisualization=V3d_TypeOfVisualization.V3d_WIREFRAME) -> None: 
        """
        Display of the Triedron. Initialize position, color and length of Triedron axes. The scale is a percent of the window width.
        """
    def TriedronErase(self) -> None: 
        """
        Erases the Triedron.
        """
    @overload
    def Turn(self,Axe : V3d_TypeOfAxe,Angle : float,Start : bool=True) -> None: 
        """
        Rotation of the view point around the frame of reference of the screen for which the origin is the eye of the projection with a relative angular value in RADIANS with respect to the initial position expressed by Start = Standard_True

        Rotation of the view point around one of the axes of the frame of reference of the view for which the origin is the eye of the projection with an angular value in RADIANS relative to the initial position expressed by Start = Standard_True

        Rotation of the view point around the current axis an angular value in RADIANS relative to the initial position expressed by Start = Standard_True
        """
    @overload
    def Turn(self,Angle : float,Start : bool=True) -> None: ...
    @overload
    def Turn(self,Ax : float,Ay : float,Az : float,Start : bool=True) -> None: ...
    def Twist(self) -> float: 
        """
        Returns in RADIANS the orientation of the view around the visual axis measured from the Y axis of the screen.
        """
    def Type(self) -> V3d_TypeOfView: 
        """
        Returns the Type of the View
        """
    def Up(self) -> Tuple[float, float, float]: 
        """
        Returns the vector giving the position of the high point.
        """
    def Update(self) -> None: 
        """
        Deprecated, Redraw() should be used instead.
        """
    def UpdateLights(self) -> None: 
        """
        Updates the lights of the view.
        """
    def View(self) -> OCP.Graphic3d.Graphic3d_CView: 
        """
        Returns the associated Graphic3d view.
        """
    def Viewer(self) -> V3d_Viewer: 
        """
        Returns the viewer in which the view has been created.
        """
    def Visualization(self) -> V3d_TypeOfVisualization: 
        """
        Returns the current visualisation mode.
        """
    def Window(self) -> OCP.Aspect.Aspect_Window: 
        """
        Returns the Aspect Window associated with the view.
        """
    def WindowFit(self,theMinXp : int,theMinYp : int,theMaxXp : int,theMaxYp : int) -> None: 
        """
        Centers the defined PIXEL window so that it occupies the maximum space while respecting the initial height/width ratio. NOTE than the original Z size of the view is NOT modified.
        """
    def WindowFitAll(self,Xmin : int,Ymin : int,Xmax : int,Ymax : int) -> None: 
        """
        idem than WindowFit
        """
    def ZBufferTriedronSetup(self,theXColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theYColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theZColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theSizeRatio : float=0.8,theAxisDiametr : float=0.05,theNbFacettes : int=12) -> None: 
        """
        Customization of the ZBUFFER Triedron. XColor,YColor,ZColor - colors of axis SizeRatio - ratio of decreasing of the trihedron size when its physical position comes out of the view AxisDiametr - diameter relatively to axis length NbFacettes - number of facets of cylinders and cones
        """
    def ZFitAll(self,theScaleFactor : float=1.0) -> None: 
        """
        Change Z-min and Z-max planes of projection volume to match the displayed objects.
        """
    def ZSize(self) -> float: 
        """
        Returns the Depth of the view .
        """
    def Zoom(self,theXp1 : int,theYp1 : int,theXp2 : int,theYp2 : int) -> None: 
        """
        Zoom the view according to a zoom factor computed from the distance between the 2 mouse position.
        """
    def ZoomAtPoint(self,theMouseStartX : int,theMouseStartY : int,theMouseEndX : int,theMouseEndY : int) -> None: 
        """
        Zooms the model at a pixel defined by the method StartZoomAtPoint().
        """
    @overload
    def __init__(self,theViewer : V3d_Viewer,theView : V3d_View) -> None: ...
    @overload
    def __init__(self,theViewer : V3d_Viewer,theType : V3d_TypeOfView=V3d_TypeOfView.V3d_ORTHOGRAPHIC) -> None: ...
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
class V3d_Viewer(OCP.Standard.Standard_Transient):
    """
    Defines services on Viewer type objects. The methods of this class allow editing and interrogation of the parameters linked to the viewer its friend classes (View,light,plane).Defines services on Viewer type objects. The methods of this class allow editing and interrogation of the parameters linked to the viewer its friend classes (View,light,plane).
    """
    def ActivateGrid(self,aGridType : OCP.Aspect.Aspect_GridType,aGridDrawMode : OCP.Aspect.Aspect_GridDrawMode) -> None: 
        """
        Activates the grid in all views of <me>.
        """
    def ActiveLight(self) -> OCP.Graphic3d.Graphic3d_CLight: 
        """
        None
        """
    def ActiveLightIterator(self) -> Any: 
        """
        Return an iterator for defined lights.
        """
    def ActiveLights(self) -> V3d_ListOfLight: 
        """
        Return a list of active lights.
        """
    def ActiveView(self) -> V3d_View: 
        """
        None
        """
    def ActiveViewIterator(self) -> Any: 
        """
        Return an iterator for active views.
        """
    def ActiveViews(self) -> V3d_ListOfView: 
        """
        Return a list of active views.
        """
    def AddLight(self,theLight : OCP.Graphic3d.Graphic3d_CLight) -> None: 
        """
        Adds Light in Sequence Of Lights.
        """
    def AddZLayer(self,theLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings=OCP.Graphic3d.Graphic3d_ZLayerSettings) -> bool: 
        """
        Add a new top-level Z layer to all managed views and get its ID as <theLayerId> value. The Z layers are controlled entirely by viewer, it is not possible to add a layer to a particular view. Custom layers will be inserted before Graphic3d_ZLayerId_Top (e.g. between Graphic3d_ZLayerId_Default and before Graphic3d_ZLayerId_Top).
        """
    def CircularGridGraphicValues(self) -> Tuple[float, float]: 
        """
        Returns the location and the size of the grid.
        """
    def CircularGridValues(self) -> Tuple[float, float, float, int, float]: 
        """
        Returns the definition of the circular grid.
        """
    def ComputedMode(self) -> bool: 
        """
        returns true if the computed mode can be used.
        """
    def CreateView(self) -> V3d_View: 
        """
        Creates a view in the viewer according to its default parameters.
        """
    def DeactivateGrid(self) -> None: 
        """
        Deactivates the grid in all views of <me>.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @overload
    def DefaultBackgroundColor(self,theType : OCP.Quantity.Quantity_TypeOfColor) -> Tuple[float, float, float]: 
        """
        Returns the default background colour object.

        None
        """
    @overload
    def DefaultBackgroundColor(self) -> OCP.Quantity.Quantity_Color: ...
    def DefaultBgGradientColors(self,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color) -> None: 
        """
        Returns the gradient background colour objects of the view.
        """
    def DefaultComputedMode(self) -> bool: 
        """
        returns true if by default the computed mode must be used.
        """
    def DefaultRenderingParams(self) -> OCP.Graphic3d.Graphic3d_RenderingParams: 
        """
        Return default Rendering Parameters. By default these parameters are set in a new V3d_View.
        """
    def DefaultShadingModel(self) -> OCP.Graphic3d.Graphic3d_TypeOfShadingModel: 
        """
        Returns the default type of Shading
        """
    def DefaultTypeOfView(self) -> V3d_TypeOfView: 
        """
        Returns the default type of View (orthographic or perspective projection) to be returned by CreateView() method.
        """
    def DefaultViewProj(self) -> V3d_TypeOfOrientation: 
        """
        Returns the default Projection.
        """
    def DefaultViewSize(self) -> float: 
        """
        Returns the default size of the view.
        """
    def DefaultVisualization(self) -> V3d_TypeOfVisualization: 
        """
        Returns the default type of Visualization.
        """
    def DefinedLight(self) -> OCP.Graphic3d.Graphic3d_CLight: 
        """
        None
        """
    def DefinedLightIterator(self) -> Any: 
        """
        Return an iterator for defined lights.
        """
    def DefinedLights(self) -> V3d_ListOfLight: 
        """
        Return a list of defined lights.
        """
    def DefinedView(self) -> V3d_View: 
        """
        None
        """
    def DefinedViewIterator(self) -> Any: 
        """
        Return an iterator for defined views.
        """
    def DefinedViews(self) -> V3d_ListOfView: 
        """
        Return a list of defined views.
        """
    def DelLight(self,theLight : OCP.Graphic3d.Graphic3d_CLight) -> None: 
        """
        Delete Light in Sequence Of Lights.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisplayPrivilegedPlane(self,theOnOff : bool,theSize : float=1.0) -> None: 
        """
        None
        """
    def Driver(self) -> OCP.Graphic3d.Graphic3d_GraphicDriver: 
        """
        Return Graphic Driver instance.
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
        Erase all Objects in All the views.
        """
    def GetAllZLayers(self,theLayerSeq : OCP.TColStd.TColStd_SequenceOfInteger) -> None: 
        """
        Return all Z layer ids in sequence ordered by overlay level from lowest layer to highest ( foreground ). The first layer ID in sequence is the default layer that can't be removed.
        """
    def GetGradientBackground(self) -> OCP.Aspect.Aspect_GradientBackground: 
        """
        Returns the gradient background of the view.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Grid(self) -> OCP.Aspect.Aspect_Grid: 
        """
        Returns the defined grid in <me>.
        """
    def GridDrawMode(self) -> OCP.Aspect.Aspect_GridDrawMode: 
        """
        Returns the current grid draw mode defined in <me>.
        """
    def GridEcho(self) -> bool: 
        """
        Returns TRUE when grid echo must be displayed at hit point.
        """
    def GridType(self) -> OCP.Aspect.Aspect_GridType: 
        """
        Returns the current grid type defined in <me>.
        """
    def HideGridEcho(self,theView : V3d_View) -> None: 
        """
        Temporarly hide grid echo.
        """
    def IfMoreViews(self) -> bool: 
        """
        Returns True if One View more can be defined in this Viewer.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitActiveLights(self) -> None: 
        """
        Initializes an internal iteratator on the active Lights.
        """
    def InitActiveViews(self) -> None: 
        """
        Initializes an internal iterator on the active views.
        """
    def InitDefinedLights(self) -> None: 
        """
        Initializes an internal iterattor on the Defined Lights.
        """
    def InitDefinedViews(self) -> None: 
        """
        Initializes an internal iterator on the Defined views.
        """
    def InsertLayerAfter(self,theNewLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings,theLayerBefore : int) -> bool: 
        """
        Add a new top-level Z layer to all managed views and get its ID as <theLayerId> value. The Z layers are controlled entirely by viewer, it is not possible to add a layer to a particular view. Layer rendering order is defined by its position in list (altered by theLayerAfter) and IsImmediate() flag (all layers with IsImmediate() flag are drawn afterwards);
        """
    def InsertLayerBefore(self,theNewLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings,theLayerAfter : int) -> bool: 
        """
        Add a new top-level Z layer to all managed views and get its ID as <theLayerId> value. The Z layers are controlled entirely by viewer, it is not possible to add a layer to a particular view. Layer rendering order is defined by its position in list (altered by theLayerAfter) and IsImmediate() flag (all layers with IsImmediate() flag are drawn afterwards);
        """
    def Invalidate(self) -> None: 
        """
        Invalidates viewer content but does not redraw it.
        """
    def IsActive(self) -> bool: 
        """
        Returns Standard_True if a grid is activated in <me>.
        """
    def IsGlobalLight(self,TheLight : OCP.Graphic3d.Graphic3d_CLight) -> bool: 
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
    def LastActiveView(self) -> bool: 
        """
        returns true if there is only one active view.
        """
    def MoreActiveLights(self) -> bool: 
        """
        returns true if there are more active Light(s) to return.
        """
    def MoreActiveViews(self) -> bool: 
        """
        Returns true if there are more active view(s) to return.
        """
    def MoreDefinedLights(self) -> bool: 
        """
        Returns true if there are more Defined Light(s) to return.
        """
    def MoreDefinedViews(self) -> bool: 
        """
        returns true if there are more Defined view(s) to return.
        """
    def NextActiveLights(self) -> None: 
        """
        Go to the next active Light (if there is not, ActiveLight() will raise an exception)
        """
    def NextActiveViews(self) -> None: 
        """
        Go to the next active view (if there is not, ActiveView will raise an exception)
        """
    def NextDefinedLights(self) -> None: 
        """
        Go to the next Defined Light (if there is not, DefinedLight() will raise an exception)
        """
    def NextDefinedViews(self) -> None: 
        """
        Go to the next Defined view (if there is not, DefinedView will raise an exception)
        """
    def PrivilegedPlane(self) -> OCP.gp.gp_Ax3: ...
    def RectangularGridGraphicValues(self) -> Tuple[float, float, float]: 
        """
        Returns the location and the size of the grid.
        """
    def RectangularGridValues(self) -> Tuple[float, float, float, float, float]: 
        """
        Returns the definition of the rectangular grid.
        """
    def Redraw(self) -> None: 
        """
        Redraws all the views of the Viewer even if no modification has taken place. Must be called if all the views of the Viewer are exposed, as for example in a global DeIconification.
        """
    def RedrawImmediate(self) -> None: 
        """
        Updates layer of immediate presentations.
        """
    def Remove(self) -> None: 
        """
        Suppresses the Viewer.
        """
    def RemoveZLayer(self,theLayerId : int) -> bool: 
        """
        Remove Z layer with ID <theLayerId>. Method returns Standard_False if the layer can not be removed or doesn't exists. By default, there are always default bottom-level layer that can't be removed.
        """
    def SetCircularGridGraphicValues(self,Radius : float,OffSet : float) -> None: 
        """
        Sets the location and the size of the grid. <XSize> defines the width of the grid. <YSize> defines the height of the grid. <OffSet> defines the displacement along the plane normal.
        """
    def SetCircularGridValues(self,XOrigin : float,YOrigin : float,RadiusStep : float,DivisionNumber : int,RotationAngle : float) -> None: 
        """
        Sets the definition of the circular grid. <XOrigin>, <YOrigin> defines the origin of the grid. <RadiusStep> defines the interval between 2 circles. <DivisionNumber> defines the section number of one half circle. <RotationAngle> defines the rotation angle of the grid.
        """
    def SetComputedMode(self,theMode : bool) -> None: 
        """
        Set if the computed mode can be used.
        """
    @overload
    def SetDefaultBackgroundColor(self,theType : OCP.Quantity.Quantity_TypeOfColor,theV1 : float,theV2 : float,theV3 : float) -> None: 
        """
        Defines the default background colour of views attached to the viewer by supplying the color object

        Defines the default base colour of views attached to the Viewer by supplying the type of colour definition and the three component values.
        """
    @overload
    def SetDefaultBackgroundColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetDefaultBgGradientColors(self,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color,theFillStyle : OCP.Aspect.Aspect_GradientFillMethod=Aspect_GradientFillMethod.Aspect_GFM_HOR) -> None: 
        """
        Defines the default gradient background colours of views attached to the viewer by supplying the colour objects
        """
    def SetDefaultComputedMode(self,theMode : bool) -> None: 
        """
        Set if by default the computed mode must be used.
        """
    def SetDefaultLights(self) -> None: 
        """
        Defines default lights: positional-light 0.3 0. 0. directional-light V3d_XnegYposZpos directional-light V3d_XnegYneg ambient-light
        """
    def SetDefaultRenderingParams(self,theParams : OCP.Graphic3d.Graphic3d_RenderingParams) -> None: 
        """
        Set default Rendering Parameters.
        """
    def SetDefaultShadingModel(self,theType : OCP.Graphic3d.Graphic3d_TypeOfShadingModel) -> None: 
        """
        Gives the default type of SHADING.
        """
    def SetDefaultTypeOfView(self,theType : V3d_TypeOfView) -> None: 
        """
        Set the default type of View (orthographic or perspective projection) to be returned by CreateView() method.
        """
    def SetDefaultViewProj(self,theOrientation : V3d_TypeOfOrientation) -> None: 
        """
        Sets the default projection for creating views in the viewer.
        """
    def SetDefaultViewSize(self,theSize : float) -> None: 
        """
        Gives a default size for the creation of views of the viewer.
        """
    def SetDefaultVisualization(self,theType : V3d_TypeOfVisualization) -> None: 
        """
        Gives the default visualization mode.
        """
    @overload
    def SetGridEcho(self,aMarker : OCP.Graphic3d.Graphic3d_AspectMarker3d) -> None: 
        """
        Show/Don't show grid echo to the hit point. If TRUE,the grid echo will be shown at ConvertToGrid() time.

        Show grid echo <aMarker> to the hit point. Warning: When the grid echo marker is not set, a default marker is build with the attributes: marker type : Aspect_TOM_STAR marker color : Quantity_NOC_GRAY90 marker size : 3.0
        """
    @overload
    def SetGridEcho(self,showGrid : bool=True) -> None: ...
    @overload
    def SetLightOff(self) -> None: 
        """
        Deactivates MyLight in this viewer.

        Deactivate all the Lights defined in this viewer.
        """
    @overload
    def SetLightOff(self,theLight : OCP.Graphic3d.Graphic3d_CLight) -> None: ...
    @overload
    def SetLightOn(self) -> None: 
        """
        Activates MyLight in the viewer.

        Activates all the lights defined in this viewer.
        """
    @overload
    def SetLightOn(self,theLight : OCP.Graphic3d.Graphic3d_CLight) -> None: ...
    def SetPrivilegedPlane(self,thePlane : OCP.gp.gp_Ax3) -> None: 
        """
        None
        """
    def SetRectangularGridGraphicValues(self,XSize : float,YSize : float,OffSet : float) -> None: 
        """
        Sets the location and the size of the grid. <XSize> defines the width of the grid. <YSize> defines the height of the grid. <OffSet> defines the displacement along the plane normal.
        """
    def SetRectangularGridValues(self,XOrigin : float,YOrigin : float,XStep : float,YStep : float,RotationAngle : float) -> None: 
        """
        Sets the definition of the rectangular grid. <XOrigin>, <YOrigin> defines the origin of the grid. <XStep> defines the interval between 2 vertical lines. <YStep> defines the interval between 2 horizontal lines. <RotationAngle> defines the rotation angle of the grid.
        """
    @overload
    def SetViewOff(self,theView : V3d_View) -> None: 
        """
        Deactivates all the views of a Viewer attached to a window.

        Deactivates a particular view in the Viewer. Must be call if the Window attached to the view has been Iconified .
        """
    @overload
    def SetViewOff(self) -> None: ...
    @overload
    def SetViewOn(self) -> None: 
        """
        Activates all of the views of a viewer attached to a window.

        Activates a particular view in the Viewer. Must be call if the Window attached to the view has been Deiconified.
        """
    @overload
    def SetViewOn(self,theView : V3d_View) -> None: ...
    def SetZLayerSettings(self,theLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings) -> None: 
        """
        Sets the settings for a single Z layer.
        """
    def ShowGridEcho(self,theView : V3d_View,thePoint : OCP.Graphic3d.Graphic3d_Vertex) -> None: 
        """
        Display grid echo at requested point in the view.
        """
    def StructureManager(self) -> OCP.Graphic3d.Graphic3d_StructureManager: 
        """
        Returns the structure manager associated to this viewer.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnHighlight(self) -> None: 
        """
        UnHighlight all Objects in All the views.
        """
    def Update(self) -> None: 
        """
        Deprecated, Redraw() should be used instead.
        """
    def UpdateLights(self) -> None: 
        """
        Updates the lights of all the views of a viewer.
        """
    def ZLayerSettings(self,theLayerId : int) -> OCP.Graphic3d.Graphic3d_ZLayerSettings: 
        """
        Returns the settings of a single Z layer.
        """
    @overload
    def __init__(self,theDriver : OCP.Graphic3d.Graphic3d_GraphicDriver,theName : str,theDomain : str='',theViewSize : float=1000.0,theViewProj : V3d_TypeOfOrientation=V3d_TypeOfOrientation.V3d_XposYnegZpos,theViewBackground : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theVisualization : V3d_TypeOfVisualization=V3d_TypeOfVisualization.V3d_ZBUFFER,theShadingModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel=Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_VERTEX,theComputedMode : bool=True,theDefaultComputedMode : bool=True) -> None: ...
    @overload
    def __init__(self,theDriver : OCP.Graphic3d.Graphic3d_GraphicDriver) -> None: ...
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
V3d_COMPLETE: OCP.V3d.V3d_TypeOfRepresentation # value = <V3d_TypeOfRepresentation.V3d_COMPLETE: 1>
V3d_ExtRADIUSCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_ExtRADIUSCAMERA: 3>
V3d_ExtRADIUSLIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_ExtRADIUSLIGHT: 3>
V3d_IntRADIUSCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_IntRADIUSCAMERA: 4>
V3d_IntRADIUSLIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_IntRADIUSLIGHT: 4>
V3d_NOTHING: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_NOTHING: 5>
V3d_NOTHINGCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_NOTHINGCAMERA: 5>
V3d_ORTHOGRAPHIC: OCP.V3d.V3d_TypeOfView # value = <V3d_TypeOfView.V3d_ORTHOGRAPHIC: 0>
V3d_PARTIAL: OCP.V3d.V3d_TypeOfRepresentation # value = <V3d_TypeOfRepresentation.V3d_PARTIAL: 2>
V3d_PERSPECTIVE: OCP.V3d.V3d_TypeOfView # value = <V3d_TypeOfView.V3d_PERSPECTIVE: 1>
V3d_POSITIONCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_POSITIONCAMERA: 0>
V3d_POSITIONLIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_POSITIONLIGHT: 0>
V3d_RADIUSTEXTCAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_RADIUSTEXTCAMERA: 2>
V3d_RADIUSTEXTLIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_RADIUSTEXTLIGHT: 2>
V3d_SAMELAST: OCP.V3d.V3d_TypeOfRepresentation # value = <V3d_TypeOfRepresentation.V3d_SAMELAST: 3>
V3d_SDO_BLENDED: OCP.V3d.V3d_StereoDumpOptions # value = <V3d_StereoDumpOptions.V3d_SDO_BLENDED: 3>
V3d_SDO_LEFT_EYE: OCP.V3d.V3d_StereoDumpOptions # value = <V3d_StereoDumpOptions.V3d_SDO_LEFT_EYE: 1>
V3d_SDO_MONO: OCP.V3d.V3d_StereoDumpOptions # value = <V3d_StereoDumpOptions.V3d_SDO_MONO: 0>
V3d_SDO_RIGHT_EYE: OCP.V3d.V3d_StereoDumpOptions # value = <V3d_StereoDumpOptions.V3d_SDO_RIGHT_EYE: 2>
V3d_SIMPLE: OCP.V3d.V3d_TypeOfRepresentation # value = <V3d_TypeOfRepresentation.V3d_SIMPLE: 0>
V3d_SPACECAMERA: OCP.V3d.V3d_TypeOfPickCamera # value = <V3d_TypeOfPickCamera.V3d_SPACECAMERA: 1>
V3d_SPACELIGHT: OCP.V3d.V3d_TypeOfPickLight # value = <V3d_TypeOfPickLight.V3d_SPACELIGHT: 1>
V3d_TOBM_ALWAYS_DISPLAYED: OCP.V3d.V3d_TypeOfBackfacingModel # value = <V3d_TypeOfBackfacingModel.V3d_TOBM_ALWAYS_DISPLAYED: 1>
V3d_TOBM_AUTOMATIC: OCP.V3d.V3d_TypeOfBackfacingModel # value = <V3d_TypeOfBackfacingModel.V3d_TOBM_AUTOMATIC: 0>
V3d_TOBM_NEVER_DISPLAYED: OCP.V3d.V3d_TypeOfBackfacingModel # value = <V3d_TypeOfBackfacingModel.V3d_TOBM_NEVER_DISPLAYED: 2>
V3d_TypeOfOrientation_Yup_AxoLeft: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYposZpos: 21>
V3d_TypeOfOrientation_Yup_AxoRight: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYposZpos: 18>
V3d_TypeOfOrientation_Yup_Back: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zneg: 5>
V3d_TypeOfOrientation_Yup_Bottom: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Yneg: 4>
V3d_TypeOfOrientation_Yup_Front: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zpos: 2>
V3d_TypeOfOrientation_Yup_Left: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xpos: 0>
V3d_TypeOfOrientation_Yup_Right: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xneg: 3>
V3d_TypeOfOrientation_Yup_Top: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Ypos: 1>
V3d_TypeOfOrientation_Zup_AxoLeft: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYnegZpos: 24>
V3d_TypeOfOrientation_Zup_AxoRight: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYnegZpos: 19>
V3d_TypeOfOrientation_Zup_Back: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Ypos: 1>
V3d_TypeOfOrientation_Zup_Bottom: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zneg: 5>
V3d_TypeOfOrientation_Zup_Front: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Yneg: 4>
V3d_TypeOfOrientation_Zup_Left: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xneg: 3>
V3d_TypeOfOrientation_Zup_Right: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xpos: 0>
V3d_TypeOfOrientation_Zup_Top: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zpos: 2>
V3d_WIREFRAME: OCP.V3d.V3d_TypeOfVisualization # value = <V3d_TypeOfVisualization.V3d_WIREFRAME: 0>
V3d_X: OCP.V3d.V3d_TypeOfAxe # value = <V3d_TypeOfAxe.V3d_X: 0>
V3d_Xneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xneg: 3>
V3d_XnegYneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYneg: 9>
V3d_XnegYnegZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYnegZneg: 25>
V3d_XnegYnegZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYnegZpos: 24>
V3d_XnegYpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYpos: 10>
V3d_XnegYposZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYposZneg: 23>
V3d_XnegYposZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegYposZpos: 21>
V3d_XnegZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegZneg: 11>
V3d_XnegZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XnegZpos: 12>
V3d_Xpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Xpos: 0>
V3d_XposYneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYneg: 15>
V3d_XposYnegZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYnegZneg: 22>
V3d_XposYnegZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYnegZpos: 19>
V3d_XposYpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYpos: 6>
V3d_XposYposZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYposZneg: 20>
V3d_XposYposZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposYposZpos: 18>
V3d_XposZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposZneg: 16>
V3d_XposZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_XposZpos: 7>
V3d_Y: OCP.V3d.V3d_TypeOfAxe # value = <V3d_TypeOfAxe.V3d_Y: 1>
V3d_Yneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Yneg: 4>
V3d_YnegZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_YnegZneg: 13>
V3d_YnegZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_YnegZpos: 14>
V3d_Ypos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Ypos: 1>
V3d_YposZneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_YposZneg: 17>
V3d_YposZpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_YposZpos: 8>
V3d_Z: OCP.V3d.V3d_TypeOfAxe # value = <V3d_TypeOfAxe.V3d_Z: 2>
V3d_ZBUFFER: OCP.V3d.V3d_TypeOfVisualization # value = <V3d_TypeOfVisualization.V3d_ZBUFFER: 1>
V3d_Zneg: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zneg: 5>
V3d_Zpos: OCP.V3d.V3d_TypeOfOrientation # value = <V3d_TypeOfOrientation.V3d_Zpos: 2>
