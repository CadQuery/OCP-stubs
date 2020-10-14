import OCP.Image
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.Standard
import OCP.TCollection
import OCP.Quantity
__all__  = [
"Image_PixMap",
"Image_ColorBGR",
"Image_ColorBGR32",
"Image_ColorBGRA",
"Image_ColorBGRAF",
"Image_ColorBGRF",
"Image_ColorRGB",
"Image_ColorRGB32",
"Image_ColorRGBA",
"Image_ColorRGBAF",
"Image_ColorRGBF",
"Image_Diff",
"Image_Format",
"Image_AlienPixMap",
"Image_PixMapData",
"Image_Texture",
"Image_VideoParams",
"Image_VideoRecorder",
"Image_Format_Alpha",
"Image_Format_AlphaF",
"Image_Format_BGR",
"Image_Format_BGR32",
"Image_Format_BGRA",
"Image_Format_BGRAF",
"Image_Format_BGRF",
"Image_Format_Gray",
"Image_Format_GrayF",
"Image_Format_RGB",
"Image_Format_RGB32",
"Image_Format_RGBA",
"Image_Format_RGBAF",
"Image_Format_RGBF",
"Image_Format_UNKNOWN"
]
class Image_PixMap(OCP.Standard.Standard_Transient):
    """
    Class represents packed image plane.Class represents packed image plane.
    """
    def ChangeData(self) -> int: 
        """
        Returns data pointer for low-level operations (copying entire buffer, parsing with extra tools etc.).
        """
    def ChangeRawValue(self,theRow : int,theCol : int) -> int: 
        """
        Access image pixel as raw data pointer. This method does not perform any type checks - use on own risk (check Format() before)!
        """
    def ChangeRow(self,theRow : int) -> int: 
        """
        Returns data pointer to requested row (first column).
        """
    def Clear(self) -> None: 
        """
        Method correctly deallocate internal buffer.
        """
    def Data(self) -> int: 
        """
        Returns data pointer for low-level operations (copying entire buffer, parsing with extra tools etc.).
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
    def Format(self) -> Image_Format: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Height(self) -> int: 
        """
        Returns image height in pixels
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitCopy(self,theCopy : Image_PixMap) -> bool: 
        """
        Initialize by copying data. If you want to copy alien data you should create wrapper using InitWrapper() before.
        """
    def InitTrash(self,thePixelFormat : Image_Format,theSizeX : int,theSizeY : int,theSizeRowBytes : int=0) -> bool: 
        """
        Initialize image plane with required dimensions. Memory will be left uninitialized (performance trick).
        """
    def InitWrapper(self,thePixelFormat : Image_Format,theDataPtr : int,theSizeX : int,theSizeY : int,theSizeRowBytes : int=0) -> bool: 
        """
        Initialize image plane as wrapper over alien data. Data will not be copied! Notice that caller should ensure that data pointer will not be released during this wrapper lifetime. You may call InitCopy() to perform data copying.
        """
    def InitZero(self,thePixelFormat : Image_Format,theSizeX : int,theSizeY : int,theSizeRowBytes : int=0,theValue : int=0) -> bool: 
        """
        Initialize image plane with required dimensions. Buffer will be zeroed (black color for most formats).
        """
    @staticmethod
    def IsBigEndianHost_s() -> bool: 
        """
        Determine Big-Endian at runtime
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if data is NULL.
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
    def IsTopDown(self) -> bool: 
        """
        Returns TRUE if image data is stored from Top to the Down. By default Bottom Up order is used instead (topmost scanlines starts from the bottom in memory). which is most image frameworks naturally support.
        """
    def MaxRowAligmentBytes(self) -> int: 
        """
        Compute the maximal row alignment for current row size.
        """
    def PixelColor(self,theX : int,theY : int) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns the pixel color. This function is relatively slow. Beware that this method takes coordinates in opposite order in contrast to ::Value() and ::ChangeValue().
        """
    def Ratio(self) -> float: 
        """
        Returns width / height.
        """
    def RawValue(self,theRow : int,theCol : int) -> int: 
        """
        Access image pixel as raw data pointer. This method does not perform any type checks - use on own risk (check Format() before)!
        """
    def Row(self,theRow : int) -> int: 
        """
        Returns data pointer to requested row (first column).
        """
    def RowExtraBytes(self) -> int: 
        """
        Returns the extra bytes in the row.
        """
    def SetFormat(self,thePixelFormat : Image_Format) -> None: 
        """
        Override pixel format specified by InitXXX() methods. Will throw exception if pixel size of new format is not equal to currently initialized format. Intended to switch formats indicating different interpretation of the same data (e.g. ImgGray and ImgAlpha).
        """
    @overload
    def SetPixelColor(self,theX : int,theY : int,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Sets the pixel color. This function is relatively slow. Beware that this method takes coordinates in opposite order in contrast to ::Value() and ::ChangeValue().

        Sets the pixel color. This function is relatively slow. Beware that this method takes coordinates in opposite order in contrast to ::Value() and ::ChangeValue().
        """
    @overload
    def SetPixelColor(self,theX : int,theY : int,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetTopDown(self,theIsTopDown : bool) -> None: 
        """
        Setup scanlines order in memory - top-down or bottom-up. Drawers should explicitly specify this value if current state IsTopDown() was ignored!
        """
    def SizeBytes(self) -> int: 
        """
        Returns buffer size
        """
    def SizePixelBytes(self) -> int: 
        """
        Returns bytes reserved for one pixel (may include extra bytes for alignment).
        """
    @staticmethod
    def SizePixelBytes_s(thePixelFormat : Image_Format) -> int: 
        """
        Returns bytes reserved for one pixel (may include extra bytes for alignment).
        """
    def SizeRowBytes(self) -> int: 
        """
        Returns bytes reserved per row. Could be larger than needed to store packed row (extra bytes for alignment etc.).
        """
    def SizeX(self) -> int: 
        """
        Returns image width in pixels
        """
    def SizeY(self) -> int: 
        """
        Returns image height in pixels
        """
    @staticmethod
    def SwapRgbaBgra_s(theImage : Image_PixMap) -> bool: 
        """
        Auxiliary method for swapping bytes between RGB and BGR formats. This method modifies the image data but does not change pixel format! Method will fail if pixel format is not one of the following: - Image_Format_RGB32 / Image_Format_BGR32 - Image_Format_RGBA / Image_Format_BGRA - Image_Format_RGB / Image_Format_BGR - Image_Format_RGBF / Image_Format_BGRF - Image_Format_RGBAF / Image_Format_BGRAF
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @staticmethod
    def ToBlackWhite_s(theImage : Image_PixMap) -> None: 
        """
        Convert image to Black/White.
        """
    def TopDownInc(self) -> int: 
        """
        Returns +1 if scanlines ordered in Top->Down order in memory and -1 otherwise.
        """
    def Width(self) -> int: 
        """
        Returns image width in pixels
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
class Image_ColorBGR():
    """
    POD structure for packed BGR color value (3 bytes)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def b(self) -> int: 
        """
        Alias to 1st component (blue intensity).

        Alias to 1st component (blue intensity).
        """
    def g(self) -> int: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> int: 
        """
        Alias to 3rd component (red intensity).

        Alias to 3rd component (red intensity).
        """
    pass
class Image_ColorBGR32():
    """
    POD structure for packed BGR color value (4 bytes with extra byte for alignment)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def a_(self) -> int: 
        """
        Alias to 4th component (dummy).

        Alias to 4th component (dummy).
        """
    def b(self) -> int: 
        """
        Alias to 1st component (blue intensity).

        Alias to 1st component (blue intensity).
        """
    def g(self) -> int: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> int: 
        """
        Alias to 3rd component (red intensity).

        Alias to 3rd component (red intensity).
        """
    pass
class Image_ColorBGRA():
    """
    POD structure for packed BGRA color value (4 bytes)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def a(self) -> int: 
        """
        Alias to 4th component (alpha value).

        Alias to 4th component (alpha value).
        """
    def b(self) -> int: 
        """
        Alias to 1st component (blue intensity).

        Alias to 1st component (blue intensity).
        """
    def g(self) -> int: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> int: 
        """
        Alias to 3rd component (red intensity).

        Alias to 3rd component (red intensity).
        """
    pass
class Image_ColorBGRAF():
    """
    POD structure for packed float BGRA color value (4 floats)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def a(self) -> float: 
        """
        Alias to 4th component (alpha value).

        Alias to 4th component (alpha value).
        """
    def b(self) -> float: 
        """
        Alias to 1st component (blue intensity).

        Alias to 1st component (blue intensity).
        """
    def g(self) -> float: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> float: 
        """
        Alias to 3rd component (red intensity).

        Alias to 3rd component (red intensity).
        """
    pass
class Image_ColorBGRF():
    """
    POD structure for packed BGR float color value (3 floats)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def b(self) -> float: 
        """
        Alias to 1st component (blue intensity).

        Alias to 1st component (blue intensity).
        """
    def g(self) -> float: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> float: 
        """
        Alias to 3rd component (red intensity).

        Alias to 3rd component (red intensity).
        """
    pass
class Image_ColorRGB():
    """
    POD structure for packed RGB color value (3 bytes)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def b(self) -> int: 
        """
        Alias to 3rd component (blue intensity).

        Alias to 3rd component (blue intensity).
        """
    def g(self) -> int: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> int: 
        """
        Alias to 1st component (red intensity).

        Alias to 1st component (red intensity).
        """
    pass
class Image_ColorRGB32():
    """
    POD structure for packed RGB color value (4 bytes with extra byte for alignment)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def a_(self) -> int: 
        """
        Alias to 4th component (dummy).

        Alias to 4th component (dummy).
        """
    def b(self) -> int: 
        """
        Alias to 3rd component (blue intensity).

        Alias to 3rd component (blue intensity).
        """
    def g(self) -> int: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> int: 
        """
        Alias to 1st component (red intensity).

        Alias to 1st component (red intensity).
        """
    pass
class Image_ColorRGBA():
    """
    POD structure for packed RGBA color value (4 bytes)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def a(self) -> int: 
        """
        Alias to 4th component (alpha value).

        Alias to 4th component (alpha value).
        """
    def b(self) -> int: 
        """
        Alias to 3rd component (blue intensity).

        Alias to 3rd component (blue intensity).
        """
    def g(self) -> int: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> int: 
        """
        Alias to 1st component (red intensity).

        Alias to 1st component (red intensity).
        """
    pass
class Image_ColorRGBAF():
    """
    POD structure for packed RGBA color value (4 floats)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def a(self) -> float: 
        """
        Alias to 4th component (alpha value).

        Alias to 4th component (alpha value).
        """
    def b(self) -> float: 
        """
        Alias to 3rd component (blue intensity).

        Alias to 3rd component (blue intensity).
        """
    def g(self) -> float: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> float: 
        """
        Alias to 1st component (red intensity).

        Alias to 1st component (red intensity).
        """
    pass
class Image_ColorRGBF():
    """
    POD structure for packed float RGB color value (3 floats)
    """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def __init__(self) -> None: ...
    def b(self) -> float: 
        """
        Alias to 3rd component (blue intensity).

        Alias to 3rd component (blue intensity).
        """
    def g(self) -> float: 
        """
        Alias to 2nd component (green intensity).

        Alias to 2nd component (green intensity).
        """
    def r(self) -> float: 
        """
        Alias to 1st component (red intensity).

        Alias to 1st component (red intensity).
        """
    pass
class Image_Diff(OCP.Standard.Standard_Transient):
    """
    This class compares two images pixel-by-pixel. It uses the following methods to ignore the difference between images: - Black/White comparison. It makes the images 2-colored before the comparison. - Equality with tolerance. Colors of two pixels are considered the same if the differnce of their color is less than a tolerance. - Border filter. The algorithm ignores alone independent pixels, which are different on both images, ignores the "border effect" - the difference caused by triangles located at angle about 0 or 90 degrees to the user.This class compares two images pixel-by-pixel. It uses the following methods to ignore the difference between images: - Black/White comparison. It makes the images 2-colored before the comparison. - Equality with tolerance. Colors of two pixels are considered the same if the differnce of their color is less than a tolerance. - Border filter. The algorithm ignores alone independent pixels, which are different on both images, ignores the "border effect" - the difference caused by triangles located at angle about 0 or 90 degrees to the user.
    """
    def ColorTolerance(self) -> float: 
        """
        Color tolerance for equality check.
        """
    def Compare(self) -> int: 
        """
        Compares two images. It returns a number of different pixels (or groups of pixels). It returns -1 if algorithm not initialized before.
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
    def Init(self,theImageRef : Image_PixMap,theImageNew : Image_PixMap,theToBlackWhite : bool=False) -> bool: 
        """
        Initialize algorithm by two images.

        Initialize algorithm by two images (will be loaded from files).
        """
    @overload
    def Init(self,theImgPathRef : OCP.TCollection.TCollection_AsciiString,theImgPathNew : OCP.TCollection.TCollection_AsciiString,theToBlackWhite : bool=False) -> bool: ...
    def IsBorderFilterOn(self) -> bool: 
        """
        Returns a flag of taking into account (ignoring) a border effect in comparison of images.
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
    @overload
    def SaveDiffImage(self,theDiffPath : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Saves a difference between two images as white pixels on black backgroud.

        Saves a difference between two images as white pixels on black backgroud.
        """
    @overload
    def SaveDiffImage(self,theDiffImage : Image_PixMap) -> bool: ...
    def SetBorderFilterOn(self,theToIgnore : bool) -> None: 
        """
        Sets taking into account (ignoring) a "border effect" on comparison of images. The border effect is caused by a border of shaded shapes in the viewer 3d. Triangles of this area are located at about 0 or 90 degrees to the user. Therefore, they deflect light differently according to implementation of a video card driver. This flag allows to detect such a "border" area and skip it from comparison of images. Filter turned OFF by default.
        """
    def SetColorTolerance(self,theTolerance : float) -> None: 
        """
        Color tolerance for equality check. Should be within range 0..1: Corresponds to a difference between white and black colors (maximum difference). By default, the tolerance is equal to 0 thus equality check will return false for any different colors.
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
class Image_Format():
    """
    This enumeration defines packed image plane formats

    Members:

      Image_Format_UNKNOWN

      Image_Format_Gray

      Image_Format_Alpha

      Image_Format_RGB

      Image_Format_BGR

      Image_Format_RGB32

      Image_Format_BGR32

      Image_Format_RGBA

      Image_Format_BGRA

      Image_Format_GrayF

      Image_Format_AlphaF

      Image_Format_RGBF

      Image_Format_BGRF

      Image_Format_RGBAF

      Image_Format_BGRAF
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
    Image_Format_Alpha: OCP.Image.Image_Format # value = Image_Format.Image_Format_Alpha
    Image_Format_AlphaF: OCP.Image.Image_Format # value = Image_Format.Image_Format_AlphaF
    Image_Format_BGR: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGR
    Image_Format_BGR32: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGR32
    Image_Format_BGRA: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGRA
    Image_Format_BGRAF: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGRAF
    Image_Format_BGRF: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGRF
    Image_Format_Gray: OCP.Image.Image_Format # value = Image_Format.Image_Format_Gray
    Image_Format_GrayF: OCP.Image.Image_Format # value = Image_Format.Image_Format_GrayF
    Image_Format_RGB: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGB
    Image_Format_RGB32: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGB32
    Image_Format_RGBA: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGBA
    Image_Format_RGBAF: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGBAF
    Image_Format_RGBF: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGBF
    Image_Format_UNKNOWN: OCP.Image.Image_Format # value = Image_Format.Image_Format_UNKNOWN
    __entries: dict # value = {'Image_Format_UNKNOWN': (Image_Format.Image_Format_UNKNOWN, None), 'Image_Format_Gray': (Image_Format.Image_Format_Gray, None), 'Image_Format_Alpha': (Image_Format.Image_Format_Alpha, None), 'Image_Format_RGB': (Image_Format.Image_Format_RGB, None), 'Image_Format_BGR': (Image_Format.Image_Format_BGR, None), 'Image_Format_RGB32': (Image_Format.Image_Format_RGB32, None), 'Image_Format_BGR32': (Image_Format.Image_Format_BGR32, None), 'Image_Format_RGBA': (Image_Format.Image_Format_RGBA, None), 'Image_Format_BGRA': (Image_Format.Image_Format_BGRA, None), 'Image_Format_GrayF': (Image_Format.Image_Format_GrayF, None), 'Image_Format_AlphaF': (Image_Format.Image_Format_AlphaF, None), 'Image_Format_RGBF': (Image_Format.Image_Format_RGBF, None), 'Image_Format_BGRF': (Image_Format.Image_Format_BGRF, None), 'Image_Format_RGBAF': (Image_Format.Image_Format_RGBAF, None), 'Image_Format_BGRAF': (Image_Format.Image_Format_BGRAF, None)}
    __members__: dict # value = {'Image_Format_UNKNOWN': Image_Format.Image_Format_UNKNOWN, 'Image_Format_Gray': Image_Format.Image_Format_Gray, 'Image_Format_Alpha': Image_Format.Image_Format_Alpha, 'Image_Format_RGB': Image_Format.Image_Format_RGB, 'Image_Format_BGR': Image_Format.Image_Format_BGR, 'Image_Format_RGB32': Image_Format.Image_Format_RGB32, 'Image_Format_BGR32': Image_Format.Image_Format_BGR32, 'Image_Format_RGBA': Image_Format.Image_Format_RGBA, 'Image_Format_BGRA': Image_Format.Image_Format_BGRA, 'Image_Format_GrayF': Image_Format.Image_Format_GrayF, 'Image_Format_AlphaF': Image_Format.Image_Format_AlphaF, 'Image_Format_RGBF': Image_Format.Image_Format_RGBF, 'Image_Format_BGRF': Image_Format.Image_Format_BGRF, 'Image_Format_RGBAF': Image_Format.Image_Format_RGBAF, 'Image_Format_BGRAF': Image_Format.Image_Format_BGRAF}
    pass
class Image_AlienPixMap(Image_PixMap, OCP.Standard.Standard_Transient):
    """
    Image class that support file reading/writing operations using auxiliary image library. Supported image formats: - *.bmp - bitmap image, lossless format without compression. - *.ppm - PPM (Portable Pixmap Format), lossless format without compression. - *.png - PNG (Portable Network Graphics) lossless format with compression. - *.jpg, *.jpe, *.jpeg - JPEG/JIFF (Joint Photographic Experts Group) lossy format (compressed with quality losses). YUV color space used (automatically converted from/to RGB). - *.tif, *.tiff - TIFF (Tagged Image File Format). - *.tga - TGA (Truevision Targa Graphic), lossless format. - *.gif - GIF (Graphical Interchange Format), lossy format. Color stored using palette (up to 256 distinct colors). - *.exr - OpenEXR high dynamic-range format (supports float pixel formats).Image class that support file reading/writing operations using auxiliary image library. Supported image formats: - *.bmp - bitmap image, lossless format without compression. - *.ppm - PPM (Portable Pixmap Format), lossless format without compression. - *.png - PNG (Portable Network Graphics) lossless format with compression. - *.jpg, *.jpe, *.jpeg - JPEG/JIFF (Joint Photographic Experts Group) lossy format (compressed with quality losses). YUV color space used (automatically converted from/to RGB). - *.tif, *.tiff - TIFF (Tagged Image File Format). - *.tga - TGA (Truevision Targa Graphic), lossless format. - *.gif - GIF (Graphical Interchange Format), lossy format. Color stored using palette (up to 256 distinct colors). - *.exr - OpenEXR high dynamic-range format (supports float pixel formats).
    """
    def AdjustGamma(self,theGammaCorr : float) -> bool: 
        """
        Performs gamma correction on image. theGamma - gamma value to use; a value of 1.0 leaves the image alone
        """
    def ChangeData(self) -> int: 
        """
        Returns data pointer for low-level operations (copying entire buffer, parsing with extra tools etc.).
        """
    def ChangeRawValue(self,theRow : int,theCol : int) -> int: 
        """
        Access image pixel as raw data pointer. This method does not perform any type checks - use on own risk (check Format() before)!
        """
    def ChangeRow(self,theRow : int) -> int: 
        """
        Returns data pointer to requested row (first column).
        """
    def Clear(self) -> None: 
        """
        Method correctly deallocate internal buffer.
        """
    def Data(self) -> int: 
        """
        Returns data pointer for low-level operations (copying entire buffer, parsing with extra tools etc.).
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
    def Format(self) -> Image_Format: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Height(self) -> int: 
        """
        Returns image height in pixels
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitCopy(self,theCopy : Image_PixMap) -> bool: 
        """
        Initialize by copying data.
        """
    def InitTrash(self,thePixelFormat : Image_Format,theSizeX : int,theSizeY : int,theSizeRowBytes : int=0) -> bool: 
        """
        Initialize image plane with required dimensions. thePixelFormat - if specified pixel format doesn't supported by image library than nearest supported will be used instead! theSizeRowBytes - may be ignored by this class and required alignemnt will be used instead!
        """
    def InitWrapper(self,thePixelFormat : Image_Format,theDataPtr : int,theSizeX : int,theSizeY : int,theSizeRowBytes : int=0) -> bool: 
        """
        Initialize image plane as wrapper over alien data. Data will not be copied! Notice that caller should ensure that data pointer will not be released during this wrapper lifetime. You may call InitCopy() to perform data copying.
        """
    def InitZero(self,thePixelFormat : Image_Format,theSizeX : int,theSizeY : int,theSizeRowBytes : int=0,theValue : int=0) -> bool: 
        """
        Initialize image plane with required dimensions. Buffer will be zeroed (black color for most formats).
        """
    @staticmethod
    def IsBigEndianHost_s() -> bool: 
        """
        Determine Big-Endian at runtime
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if data is NULL.
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
    def IsTopDown(self) -> bool: 
        """
        Returns TRUE if image data is stored from Top to the Down. By default Bottom Up order is used instead (topmost scanlines starts from the bottom in memory). which is most image frameworks naturally support.
        """
    @staticmethod
    def IsTopDownDefault_s() -> bool: 
        """
        Return default rows order used by underlying image library.
        """
    def MaxRowAligmentBytes(self) -> int: 
        """
        Compute the maximal row alignment for current row size.
        """
    def PixelColor(self,theX : int,theY : int) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns the pixel color. This function is relatively slow. Beware that this method takes coordinates in opposite order in contrast to ::Value() and ::ChangeValue().
        """
    def Ratio(self) -> float: 
        """
        Returns width / height.
        """
    def RawValue(self,theRow : int,theCol : int) -> int: 
        """
        Access image pixel as raw data pointer. This method does not perform any type checks - use on own risk (check Format() before)!
        """
    def Row(self,theRow : int) -> int: 
        """
        Returns data pointer to requested row (first column).
        """
    def RowExtraBytes(self) -> int: 
        """
        Returns the extra bytes in the row.
        """
    def Save(self,theFileName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Write image data to file using file extension to determine compression format.
        """
    def SetFormat(self,thePixelFormat : Image_Format) -> None: 
        """
        Override pixel format specified by InitXXX() methods. Will throw exception if pixel size of new format is not equal to currently initialized format. Intended to switch formats indicating different interpretation of the same data (e.g. ImgGray and ImgAlpha).
        """
    @overload
    def SetPixelColor(self,theX : int,theY : int,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Sets the pixel color. This function is relatively slow. Beware that this method takes coordinates in opposite order in contrast to ::Value() and ::ChangeValue().

        Sets the pixel color. This function is relatively slow. Beware that this method takes coordinates in opposite order in contrast to ::Value() and ::ChangeValue().
        """
    @overload
    def SetPixelColor(self,theX : int,theY : int,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetTopDown(self,theIsTopDown : bool) -> None: 
        """
        Setup scanlines order in memory - top-down or bottom-up. Drawers should explicitly specify this value if current state IsTopDown() was ignored!
        """
    def SizeBytes(self) -> int: 
        """
        Returns buffer size
        """
    def SizePixelBytes(self) -> int: 
        """
        Returns bytes reserved for one pixel (may include extra bytes for alignment).
        """
    @staticmethod
    def SizePixelBytes_s(thePixelFormat : Image_Format) -> int: 
        """
        Returns bytes reserved for one pixel (may include extra bytes for alignment).
        """
    def SizeRowBytes(self) -> int: 
        """
        Returns bytes reserved per row. Could be larger than needed to store packed row (extra bytes for alignment etc.).
        """
    def SizeX(self) -> int: 
        """
        Returns image width in pixels
        """
    def SizeY(self) -> int: 
        """
        Returns image height in pixels
        """
    @staticmethod
    def SwapRgbaBgra_s(theImage : Image_PixMap) -> bool: 
        """
        Auxiliary method for swapping bytes between RGB and BGR formats. This method modifies the image data but does not change pixel format! Method will fail if pixel format is not one of the following: - Image_Format_RGB32 / Image_Format_BGR32 - Image_Format_RGBA / Image_Format_BGRA - Image_Format_RGB / Image_Format_BGR - Image_Format_RGBF / Image_Format_BGRF - Image_Format_RGBAF / Image_Format_BGRAF
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @staticmethod
    def ToBlackWhite_s(theImage : Image_PixMap) -> None: 
        """
        Convert image to Black/White.
        """
    def TopDownInc(self) -> int: 
        """
        Returns +1 if scanlines ordered in Top->Down order in memory and -1 otherwise.
        """
    def Width(self) -> int: 
        """
        Returns image width in pixels
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
class Image_PixMapData(OCP.NCollection.NCollection_Buffer, OCP.Standard.Standard_Transient):
    """
    Structure to manage image buffer.Structure to manage image buffer.
    """
    def Allocate(self,theSize : int) -> bool: 
        """
        Allocate the buffer.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns buffer allocator
        """
    def ChangeData(self) -> int: 
        """
        Returns buffer data
        """
    def ChangeRow(self,theRow : int) -> int: 
        """
        Returns data pointer to requested row (first column).
        """
    def ChangeValue(self,theRow : int,theCol : int) -> int: 
        """
        Returns data pointer to requested position.
        """
    def Data(self) -> int: 
        """
        Returns buffer data
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
    def Free(self) -> None: 
        """
        De-allocate buffer.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator,theSizeBPP : int,theSizeX : int,theSizeY : int,theSizeRowBytes : int,theDataPtr : int) -> bool: 
        """
        Initializer.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if buffer is not allocated
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
    def MaxRowAligmentBytes(self) -> int: 
        """
        Compute the maximal row alignment for current row size.
        """
    def Row(self,theRow : int) -> int: 
        """
        Returns data pointer to requested row (first column).
        """
    def SetAllocator(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Assign new buffer allocator with de-allocation of buffer.
        """
    def SetTopDown(self,theIsTopDown : bool) -> None: 
        """
        Setup scanlines order in memory - top-down or bottom-up. Drawers should explicitly specify this value if current state IsTopDown() was ignored!
        """
    def Size(self) -> int: 
        """
        Return buffer length in bytes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,theRow : int,theCol : int) -> int: 
        """
        Returns data pointer to requested position.
        """
    def ZeroData(self) -> None: 
        """
        Reset all values to zeros.
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
    @property
    def SizeBPP(self) -> int:
        """
        :type: int
        """
    @SizeBPP.setter
    def SizeBPP(self, arg0: int) -> None:
        pass
    @property
    def SizeRowBytes(self) -> int:
        """
        :type: int
        """
    @SizeRowBytes.setter
    def SizeRowBytes(self, arg0: int) -> None:
        pass
    @property
    def SizeX(self) -> int:
        """
        :type: int
        """
    @SizeX.setter
    def SizeX(self, arg0: int) -> None:
        pass
    @property
    def SizeY(self) -> int:
        """
        :type: int
        """
    @SizeY.setter
    def SizeY(self, arg0: int) -> None:
        pass
    @property
    def TopToDown(self) -> int:
        """
        :type: int
        """
    @TopToDown.setter
    def TopToDown(self, arg0: int) -> None:
        pass
    pass
class Image_Texture(OCP.Standard.Standard_Transient):
    """
    Texture image definition. The image can be stored as path to image file, as file path with the given offset and as a data buffer of encoded image.
    """
    def DataBuffer(self) -> OCP.NCollection.NCollection_Buffer: 
        """
        Return buffer holding encoded image content.
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
    def FileLength(self) -> int: 
        """
        Return length of image data within the file after offset.
        """
    def FileOffset(self) -> int: 
        """
        Return offset within file.
        """
    def FilePath(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return image file path.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def HashCode_s(theTexture : Image_Texture,theUpper : int) -> int: 
        """
        Hash value, for Map interface.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @staticmethod
    def IsEqual_s(theTex1 : Image_Texture,theTex2 : Image_Texture) -> bool: 
        """
        Matching two instances, for Map interface.
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
    def ProbeImageFileFormat(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return image file format.
        """
    def ReadImage(self) -> Image_PixMap: 
        """
        Image reader.
        """
    def TextureId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return generated texture id.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WriteImage(self,theFile : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Write image to specified file without decoding data.
        """
    @overload
    def __init__(self,theFileName : OCP.TCollection.TCollection_AsciiString,theOffset : int,theLength : int) -> None: ...
    @overload
    def __init__(self,theFileName : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,theBuffer : OCP.NCollection.NCollection_Buffer,theId : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Image_VideoParams():
    """
    Auxiliary structure defining video parameters. Please refer to FFmpeg documentation for defining text values.
    """
    @overload
    def SetFramerate(self,theNumerator : int,theDenominator : int) -> None: 
        """
        Setup playback FPS.

        Setup playback FPS. For fixed-fps content, timebase should be 1/framerate and timestamp increments should be identical to 1.
        """
    @overload
    def SetFramerate(self,theValue : int) -> None: ...
    def __init__(self) -> None: ...
    @property
    def Format(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @Format.setter
    def Format(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    @property
    def FpsDen(self) -> int:
        """
        :type: int
        """
    @FpsDen.setter
    def FpsDen(self, arg0: int) -> None:
        pass
    @property
    def FpsNum(self) -> int:
        """
        :type: int
        """
    @FpsNum.setter
    def FpsNum(self, arg0: int) -> None:
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
    def PixelFormat(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @PixelFormat.setter
    def PixelFormat(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    @property
    def VideoCodec(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @VideoCodec.setter
    def VideoCodec(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    @property
    def VideoCodecParams(self) -> OCP.Resource.Resource_DataMapOfAsciiStringAsciiString:
        """
        :type: OCP.Resource.Resource_DataMapOfAsciiStringAsciiString
        """
    @VideoCodecParams.setter
    def VideoCodecParams(self, arg0: OCP.Resource.Resource_DataMapOfAsciiStringAsciiString) -> None:
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
class Image_VideoRecorder(OCP.Standard.Standard_Transient):
    """
    Video recording tool based on FFmpeg framework.Video recording tool based on FFmpeg framework.
    """
    def ChangeFrame(self) -> Image_PixMap: 
        """
        Access RGBA frame, should NOT be re-initialized outside. Note that image is expected to have upper-left origin.
        """
    def Close(self) -> None: 
        """
        Close the stream - stop recorder.
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
    def FrameCount(self) -> int: 
        """
        Return current frame index.
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
    def Open(self,theFileName : str,theParams : Image_VideoParams) -> bool: 
        """
        Open output stream - initialize recorder.
        """
    def PushFrame(self) -> bool: 
        """
        Push new frame, should be called after Open().
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
Image_Format_Alpha: OCP.Image.Image_Format # value = Image_Format.Image_Format_Alpha
Image_Format_AlphaF: OCP.Image.Image_Format # value = Image_Format.Image_Format_AlphaF
Image_Format_BGR: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGR
Image_Format_BGR32: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGR32
Image_Format_BGRA: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGRA
Image_Format_BGRAF: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGRAF
Image_Format_BGRF: OCP.Image.Image_Format # value = Image_Format.Image_Format_BGRF
Image_Format_Gray: OCP.Image.Image_Format # value = Image_Format.Image_Format_Gray
Image_Format_GrayF: OCP.Image.Image_Format # value = Image_Format.Image_Format_GrayF
Image_Format_RGB: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGB
Image_Format_RGB32: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGB32
Image_Format_RGBA: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGBA
Image_Format_RGBAF: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGBAF
Image_Format_RGBF: OCP.Image.Image_Format # value = Image_Format.Image_Format_RGBF
Image_Format_UNKNOWN: OCP.Image.Image_Format # value = Image_Format.Image_Format_UNKNOWN
