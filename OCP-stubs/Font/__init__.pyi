import OCP.Font
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TCollection
import OCP.TopoDS
import OCP.Standard
import OCP.Graphic3d
import OCP.TColStd
import OCP.Image
__all__  = [
"Font_BRepTextBuilder",
"Font_FTFont",
"Font_FTFontParams",
"Font_FTLibrary",
"Font_FontAspect",
"Font_FontMgr",
"Font_NListOfSystemFont",
"Font_Rect",
"Font_StrictLevel",
"Font_SystemFont",
"Font_TextFormatter",
"Font_UnicodeSubset",
"IsEqual",
"Font_FA_Bold",
"Font_FA_BoldItalic",
"Font_FA_Italic",
"Font_FA_Regular",
"Font_FA_Undefined",
"Font_FontAspect_Bold",
"Font_FontAspect_BoldItalic",
"Font_FontAspect_Italic",
"Font_FontAspect_NB",
"Font_FontAspect_Regular",
"Font_FontAspect_UNDEFINED",
"Font_StrictLevel_Aliases",
"Font_StrictLevel_Any",
"Font_StrictLevel_Strict",
"Font_UnicodeSubset_Arabic",
"Font_UnicodeSubset_CJK",
"Font_UnicodeSubset_Korean",
"Font_UnicodeSubset_NB",
"Font_UnicodeSubset_Western"
]
class Font_BRepTextBuilder():
    """
    Represents class for applying text formatting.
    """
    @overload
    def Perform(self,Fontpath : str,Fontsize : float,Fontstyle : Font_FontAspect,Text : str) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Render text as BRep shape.

        Render text as BRep shape.

        Render text as BRep shape.
        """
    @overload
    def Perform(self,theFont : Font_BRepFont,theFormatter : Font_TextFormatter,thePenLoc : OCP.gp.gp_Ax3=OCP.gp.gp_Ax3) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def Perform(self,theFont : Font_BRepFont,theString : OCP.NCollection.NCollection_Utf8String,thePenLoc : OCP.gp.gp_Ax3=OCP.gp.gp_Ax3,theHAlign : OCP.Graphic3d.Graphic3d_HorizontalTextAlignment=Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_LEFT,theVAlign : OCP.Graphic3d.Graphic3d_VerticalTextAlignment=Graphic3d_VerticalTextAlignment.Graphic3d_VTA_BOTTOM) -> OCP.TopoDS.TopoDS_Shape: ...
    def __init__(self) -> None: ...
    pass
class Font_FTFont(OCP.Standard.Standard_Transient):
    """
    Wrapper over FreeType font. Notice that this class uses internal buffers for loaded glyphs and it is absolutely UNSAFE to load/read glyph from concurrent threads!Wrapper over FreeType font. Notice that this class uses internal buffers for loaded glyphs and it is absolutely UNSAFE to load/read glyph from concurrent threads!
    """
    @overload
    def AdvanceX(self,theUCharNext : str) -> float: 
        """
        Compute horizontal advance to the next character with kerning applied when applicable. Assuming text rendered horizontally.

        Compute horizontal advance to the next character with kerning applied when applicable. Assuming text rendered horizontally.
        """
    @overload
    def AdvanceX(self,theUChar : str,theUCharNext : str) -> float: ...
    @overload
    def AdvanceY(self,theUChar : str,theUCharNext : str) -> float: 
        """
        Compute vertical advance to the next character with kerning applied when applicable. Assuming text rendered vertically.

        Compute vertical advance to the next character with kerning applied when applicable. Assuming text rendered vertically.
        """
    @overload
    def AdvanceY(self,theUCharNext : str) -> float: ...
    def Ascender(self) -> float: 
        """
        Returns vertical distance from the horizontal baseline to the highest character coordinate.
        """
    def BoundingBox(self,theString : OCP.NCollection.NCollection_Utf8String,theAlignX : OCP.Graphic3d.Graphic3d_HorizontalTextAlignment,theAlignY : OCP.Graphic3d.Graphic3d_VerticalTextAlignment) -> Font_Rect: 
        """
        Computes bounding box of the given text using plain-text formatter (Font_TextFormatter). Note that bounding box takes into account the text alignment options. Its corners are relative to the text alignment anchor point, their coordinates can be negative.
        """
    @staticmethod
    def CharSubset_s(theUChar : str) -> Font_UnicodeSubset: 
        """
        Determine Unicode subset for specified character
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Descender(self) -> float: 
        """
        Returns vertical distance from the horizontal baseline to the lowest character coordinate.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def FindAndCreate_s(theFontName : OCP.TCollection.TCollection_AsciiString,theFontAspect : Font_FontAspect,theParams : Font_FTFontParams,theStrictLevel : Font_StrictLevel=Font_StrictLevel.Font_StrictLevel_Any) -> Font_FTFont: 
        """
        Find the font Initialize the font.
        """
    def FindAndInit(self,theFontName : OCP.TCollection.TCollection_AsciiString,theFontAspect : Font_FontAspect,theParams : Font_FTFontParams,theStrictLevel : Font_StrictLevel=Font_StrictLevel.Font_StrictLevel_Any) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlyphImage(self) -> OCP.Image.Image_PixMap: 
        """
        Returns image plane for currently rendered glyph
        """
    def GlyphMaxSizeX(self,theToIncludeFallback : bool=False) -> int: 
        """
        Returns maximal glyph width in pixels (rendered to bitmap).
        """
    def GlyphMaxSizeY(self,theToIncludeFallback : bool=False) -> int: 
        """
        Returns maximal glyph height in pixels (rendered to bitmap).
        """
    def GlyphRect(self,theRect : Font_Rect) -> None: 
        """
        Retrieve glyph bitmap rectangle
        """
    def GlyphsNumber(self,theToIncludeFallback : bool=False) -> int: 
        """
        Return glyphs number in this font.
        """
    def HasSymbol(self,theUChar : str) -> bool: 
        """
        Return TRUE if font contains specified symbol (excluding fallback list).
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theFontPath : OCP.TCollection.TCollection_AsciiString,theParams : Font_FTFontParams) -> bool: 
        """
        Initialize the font from the given file path.

        Initialize the font from the given file path or memory buffer.

        Initialize the font.

        Initialize the font.
        """
    @overload
    def Init(self,theFontPath : OCP.NCollection.NCollection_Utf8String,thePointSize : int,theResolution : int) -> bool: ...
    @overload
    def Init(self,theData : OCP.NCollection.NCollection_Buffer,theFileName : OCP.TCollection.TCollection_AsciiString,theParams : Font_FTFontParams) -> bool: ...
    @overload
    def Init(self,theFontName : OCP.NCollection.NCollection_Utf8String,theFontAspect : Font_FontAspect,thePointSize : int,theResolution : int) -> bool: ...
    @staticmethod
    def IsCharFromArabic_s(theUChar : str) -> bool: 
        """
        Return TRUE if specified character is within subset of Arabic characters.
        """
    @staticmethod
    def IsCharFromCJK_s(theUChar : str) -> bool: 
        """
        Return TRUE if specified character is within subset of modern CJK characters.
        """
    @staticmethod
    def IsCharFromHiragana_s(theUChar : str) -> bool: 
        """
        Return TRUE if specified character is within subset of Hiragana (Japanese).
        """
    @staticmethod
    def IsCharFromKatakana_s(theUChar : str) -> bool: 
        """
        Return TRUE if specified character is within subset of Katakana (Japanese).
        """
    @staticmethod
    def IsCharFromKorean_s(theUChar : str) -> bool: 
        """
        Return TRUE if specified character is within subset of modern Korean characters (Hangul).
        """
    @staticmethod
    def IsCharRightToLeft_s(theUChar : str) -> bool: 
        """
        Return TRUE if specified character should be displayed in Right-to-Left order.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsSingleStrokeFont(self) -> bool: 
        """
        Return TRUE if this is single-stroke (one-line) font, FALSE by default. Such fonts define single-line glyphs instead of closed contours, so that they are rendered incorrectly by normal software.
        """
    def IsValid(self) -> bool: 
        """
        Returns true if font is loaded
        """
    def LineSpacing(self) -> float: 
        """
        Returns default line spacing (the baseline-to-baseline distance).
        """
    def PointSize(self) -> int: 
        """
        Configured point size
        """
    def Release(self) -> None: 
        """
        Release currently loaded font.
        """
    def RenderGlyph(self,theChar : str) -> bool: 
        """
        Render specified glyph into internal buffer (bitmap).
        """
    def SetSingleStrokeFont(self,theIsSingleLine : bool) -> None: 
        """
        Set if this font should be rendered as single-stroke (one-line).
        """
    def SetUseUnicodeSubsetFallback(self,theToFallback : bool) -> None: 
        """
        Set if fallback fonts should be used in case if used font does not include symbols from specific Unicode subset.
        """
    def SetWidthScaling(self,theScaleFactor : float) -> None: 
        """
        Setup glyph scaling along X-axis. By default glyphs are not scaled (scaling factor = 1.0)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToSynthesizeItalic(self) -> bool: 
        """
        Return TRUE if italic style should be synthesized; FALSE by default.
        """
    def ToUseUnicodeSubsetFallback(self) -> bool: 
        """
        Return flag to use fallback fonts in case if used font does not include symbols from specific Unicode subset; TRUE by default.
        """
    def __init__(self,theFTLib : Font_FTLibrary=None) -> None: ...
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
class Font_FTFontParams():
    """
    Font initialization parameters.
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,thePointSize : int,theResolution : int) -> None: ...
    pass
class Font_FTLibrary(OCP.Standard.Standard_Transient):
    """
    Wrapper over FT_Library. Provides access to FreeType library.Wrapper over FT_Library. Provides access to FreeType library.
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
    def Instance(self) -> FT_LibraryRec_: 
        """
        Access FT_Library instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsValid(self) -> bool: 
        """
        This method should always return true.
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
class Font_FontAspect():
    """
    Specifies aspect of system font.

    Members:

      Font_FontAspect_UNDEFINED

      Font_FontAspect_Regular

      Font_FontAspect_Bold

      Font_FontAspect_Italic

      Font_FontAspect_BoldItalic

      Font_FA_Undefined

      Font_FA_Regular

      Font_FA_Bold

      Font_FA_Italic

      Font_FA_BoldItalic
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Font_FA_Bold: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Bold
    Font_FA_BoldItalic: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_BoldItalic
    Font_FA_Italic: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Italic
    Font_FA_Regular: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Regular
    Font_FA_Undefined: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_UNDEFINED
    Font_FontAspect_Bold: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Bold
    Font_FontAspect_BoldItalic: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_BoldItalic
    Font_FontAspect_Italic: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Italic
    Font_FontAspect_Regular: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Regular
    Font_FontAspect_UNDEFINED: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_UNDEFINED
    __entries: dict # value = {'Font_FontAspect_UNDEFINED': (Font_FontAspect.Font_FontAspect_UNDEFINED, None), 'Font_FontAspect_Regular': (Font_FontAspect.Font_FontAspect_Regular, None), 'Font_FontAspect_Bold': (Font_FontAspect.Font_FontAspect_Bold, None), 'Font_FontAspect_Italic': (Font_FontAspect.Font_FontAspect_Italic, None), 'Font_FontAspect_BoldItalic': (Font_FontAspect.Font_FontAspect_BoldItalic, None), 'Font_FA_Undefined': (Font_FontAspect.Font_FontAspect_UNDEFINED, None), 'Font_FA_Regular': (Font_FontAspect.Font_FontAspect_Regular, None), 'Font_FA_Bold': (Font_FontAspect.Font_FontAspect_Bold, None), 'Font_FA_Italic': (Font_FontAspect.Font_FontAspect_Italic, None), 'Font_FA_BoldItalic': (Font_FontAspect.Font_FontAspect_BoldItalic, None)}
    __members__: dict # value = {'Font_FontAspect_UNDEFINED': Font_FontAspect.Font_FontAspect_UNDEFINED, 'Font_FontAspect_Regular': Font_FontAspect.Font_FontAspect_Regular, 'Font_FontAspect_Bold': Font_FontAspect.Font_FontAspect_Bold, 'Font_FontAspect_Italic': Font_FontAspect.Font_FontAspect_Italic, 'Font_FontAspect_BoldItalic': Font_FontAspect.Font_FontAspect_BoldItalic, 'Font_FA_Undefined': Font_FontAspect.Font_FontAspect_UNDEFINED, 'Font_FA_Regular': Font_FontAspect.Font_FontAspect_Regular, 'Font_FA_Bold': Font_FontAspect.Font_FontAspect_Bold, 'Font_FA_Italic': Font_FontAspect.Font_FontAspect_Italic, 'Font_FA_BoldItalic': Font_FontAspect.Font_FontAspect_BoldItalic}
    pass
class Font_FontMgr(OCP.Standard.Standard_Transient):
    """
    Collects and provides information about available fonts in system.Collects and provides information about available fonts in system.
    """
    def AvailableFonts(self,theList : Font_NListOfSystemFont) -> None: 
        """
        Return the list of available fonts.
        """
    def CheckFont(self,theFontPath : str) -> Font_SystemFont: 
        """
        Read font file and retrieve information from it.
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
    def FindFallbackFont(self,theSubset : Font_UnicodeSubset,theFontAspect : Font_FontAspect) -> Font_SystemFont: 
        """
        Tries to find fallback font for specified Unicode subset. Returns NULL in case when fallback font is not found in the system.
        """
    @overload
    def FindFont(self,theFontName : OCP.TCollection.TCollection_AsciiString,theStrictLevel : Font_StrictLevel,theFontAspect : Font_FontAspect) -> Font_SystemFont: 
        """
        Tries to find font by given parameters. If the specified font is not found tries to use font names mapping. If the requested family name not found -> search for any font family with given aspect and height. If the font is still not found, returns any font available in the system. Returns NULL in case when the fonts are not found in the system.

        Tries to find font by given parameters.
        """
    @overload
    def FindFont(self,theFontName : OCP.TCollection.TCollection_AsciiString,theFontAspect : Font_FontAspect) -> Font_SystemFont: ...
    @staticmethod
    def FontAspectToString_s(theAspect : Font_FontAspect) -> str: 
        """
        Return font aspect as string.
        """
    def GetAvailableFonts(self) -> Font_NListOfSystemFont: 
        """
        Return the list of available fonts.
        """
    def GetAvailableFontsNames(self,theFontsNames : OCP.TColStd.TColStd_SequenceOfHAsciiString) -> None: 
        """
        Returns sequence of available fonts names
        """
    @overload
    def GetFont(self,theFontName : OCP.TCollection.TCollection_AsciiString) -> Font_SystemFont: 
        """
        Returns font that match given parameters. If theFontName is empty string returned font can have any FontName. If theFontAspect is Font_FA_Undefined returned font can have any FontAspect. If theFontSize is "-1" returned font can have any FontSize.

        Returns font that match given name or NULL if such font family is NOT registered. Note that unlike FindFont(), this method ignores font aliases and does not look for fall-back.
        """
    @overload
    def GetFont(self,theFontName : OCP.TCollection.TCollection_HAsciiString,theFontAspect : Font_FontAspect,theFontSize : int) -> Font_SystemFont: ...
    @staticmethod
    def GetInstance_s() -> Font_FontMgr: 
        """
        Return global instance of font manager.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def RegisterFont(self,theFont : Font_SystemFont,theToOverride : bool) -> bool: 
        """
        Register new font. If there is existing entity with the same name and properties but different path then font will be overridden or ignored depending on theToOverride flag.
        """
    def SetTraceAliases(self,theToTrace : bool) -> None: 
        """
        Set flag for tracing font alias usage; useful to trace which fonts are actually used. Can be disabled to avoid redundant messages with Message_Trace level.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToTraceAliases(self) -> bool: 
        """
        Return flag for tracing font aliases usage via Message_Trace messages; TRUE by default.
        """
    @staticmethod
    def ToUseUnicodeSubsetFallback_s() -> bool: 
        """
        Return flag to use fallback fonts in case if used font does not include symbols from specific Unicode subset; TRUE by default.
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
class Font_NListOfSystemFont(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Font_SystemFont,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : Font_SystemFont) -> Font_SystemFont: ...
    @overload
    def Append(self,theOther : Font_NListOfSystemFont) -> None: ...
    def Assign(self,theOther : Font_NListOfSystemFont) -> Font_NListOfSystemFont: 
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
    def First(self) -> Font_SystemFont: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : Font_NListOfSystemFont,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : Font_SystemFont,theIter : Any) -> Font_SystemFont: ...
    @overload
    def InsertBefore(self,theItem : Font_SystemFont,theIter : Any) -> Font_SystemFont: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : Font_NListOfSystemFont,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> Font_SystemFont: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : Font_SystemFont) -> Font_SystemFont: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : Font_NListOfSystemFont) -> None: ...
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
    def __init__(self,theOther : Font_NListOfSystemFont) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Font_Rect():
    """
    Auxiliary POD structure - 2D rectangle definition.
    """
    def BottomLeft(self,theVec : OCP.Graphic3d.Graphic3d_Vec2) -> OCP.Graphic3d.Graphic3d_Vec2: 
        """
        Bottom-left corner as vec2.
        """
    def BottomRight(self,theVec : OCP.Graphic3d.Graphic3d_Vec2) -> OCP.Graphic3d.Graphic3d_Vec2: 
        """
        Bottom-right corner as vec2.
        """
    def Height(self) -> float: 
        """
        Rectangle height.
        """
    @overload
    def TopLeft(self) -> OCP.Graphic3d.Graphic3d_Vec2: 
        """
        Top-left corner as vec2.

        Top-left corner as vec2.
        """
    @overload
    def TopLeft(self,theVec : OCP.Graphic3d.Graphic3d_Vec2) -> OCP.Graphic3d.Graphic3d_Vec2: ...
    def TopRight(self,theVec : OCP.Graphic3d.Graphic3d_Vec2) -> OCP.Graphic3d.Graphic3d_Vec2: 
        """
        Top-right corner as vec2.
        """
    def Width(self) -> float: 
        """
        Rectangle width.
        """
    def __init__(self) -> None: ...
    pass
class Font_StrictLevel():
    """
    Enumeration defining font search restrictions.

    Members:

      Font_StrictLevel_Strict

      Font_StrictLevel_Aliases

      Font_StrictLevel_Any
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Font_StrictLevel_Aliases: OCP.Font.Font_StrictLevel # value = Font_StrictLevel.Font_StrictLevel_Aliases
    Font_StrictLevel_Any: OCP.Font.Font_StrictLevel # value = Font_StrictLevel.Font_StrictLevel_Any
    Font_StrictLevel_Strict: OCP.Font.Font_StrictLevel # value = Font_StrictLevel.Font_StrictLevel_Strict
    __entries: dict # value = {'Font_StrictLevel_Strict': (Font_StrictLevel.Font_StrictLevel_Strict, None), 'Font_StrictLevel_Aliases': (Font_StrictLevel.Font_StrictLevel_Aliases, None), 'Font_StrictLevel_Any': (Font_StrictLevel.Font_StrictLevel_Any, None)}
    __members__: dict # value = {'Font_StrictLevel_Strict': Font_StrictLevel.Font_StrictLevel_Strict, 'Font_StrictLevel_Aliases': Font_StrictLevel.Font_StrictLevel_Aliases, 'Font_StrictLevel_Any': Font_StrictLevel.Font_StrictLevel_Any}
    pass
class Font_SystemFont(OCP.Standard.Standard_Transient):
    """
    This class stores information about the font, which is merely a file path and cached metadata about the font.This class stores information about the font, which is merely a file path and cached metadata about the font.
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
    def FontKey(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns font family name (lower-cased).
        """
    def FontName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns font family name.
        """
    def FontPath(self,theAspect : Font_FontAspect) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns font file path.
        """
    def FontPathAny(self,theAspect : Font_FontAspect,theToSynthesizeItalic : bool) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns any defined font file path.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFontAspect(self,theAspect : Font_FontAspect) -> bool: 
        """
        Returns TRUE if dedicated file for specified font aspect has been defined.
        """
    @staticmethod
    def HashCode_s(theSystemFont : Font_SystemFont,theUpperBound : int) -> int: 
        """
        Computes a hash code for the system font, in the range [1, theUpperBound]. Based on Font Family, so that the whole family with different aspects can be found within the same bucket of some map
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEqual(self,theOtherFont : Font_SystemFont) -> bool: 
        """
        Return true if the FontName, FontAspect and FontSize are the same.
        """
    @staticmethod
    def IsEqual_s(theFont1 : Font_SystemFont,theFont2 : Font_SystemFont) -> bool: 
        """
        Matching two instances, for Map interface.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsSingleStrokeFont(self) -> bool: 
        """
        Return TRUE if this is single-stroke (one-line) font, FALSE by default. Such fonts define single-line glyphs instead of closed contours, so that they are rendered incorrectly by normal software.
        """
    def SetFontPath(self,theAspect : Font_FontAspect,thePath : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets font file path for specific aspect.
        """
    def SetSingleStrokeFont(self,theIsSingleLine : bool) -> None: 
        """
        Set if this font should be rendered as single-stroke (one-line).
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToString(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Format font description.
        """
    def __init__(self,theFontName : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Font_TextFormatter():
    """
    This class intended to prepare formatted text.
    """
    def Append(self,theString : OCP.NCollection.NCollection_Utf8String,theFont : Font_FTFont) -> None: 
        """
        Render specified text to inner buffer.
        """
    def BndBox(self,theBndBox : Font_Rect) -> None: ...
    def Format(self) -> None: 
        """
        Perform formatting on the buffered text. Should not be called more than once after initialization!
        """
    def Reset(self) -> None: 
        """
        Reset current progress.
        """
    def ResultHeight(self) -> float: 
        """
        Returns height of formatted text.
        """
    def ResultWidth(self) -> float: 
        """
        Returns width of formatted text.
        """
    def SetupAlignment(self,theAlignX : OCP.Graphic3d.Graphic3d_HorizontalTextAlignment,theAlignY : OCP.Graphic3d.Graphic3d_VerticalTextAlignment) -> None: 
        """
        Setup alignment style.
        """
    def String(self) -> OCP.NCollection.NCollection_Utf8String: 
        """
        Returns current rendering string.
        """
    def TabSize(self) -> int: 
        """
        Returns tab size.
        """
    def TopLeft(self,theIndex : int) -> OCP.Graphic3d.Graphic3d_Vec2: 
        """
        Returns specific glyph rectangle.
        """
    def __init__(self) -> None: ...
    pass
class Font_UnicodeSubset():
    """
    Enumeration defining Unicode subsets.

    Members:

      Font_UnicodeSubset_Western

      Font_UnicodeSubset_Korean

      Font_UnicodeSubset_CJK

      Font_UnicodeSubset_Arabic
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Font_UnicodeSubset_Arabic: OCP.Font.Font_UnicodeSubset # value = Font_UnicodeSubset.Font_UnicodeSubset_Arabic
    Font_UnicodeSubset_CJK: OCP.Font.Font_UnicodeSubset # value = Font_UnicodeSubset.Font_UnicodeSubset_CJK
    Font_UnicodeSubset_Korean: OCP.Font.Font_UnicodeSubset # value = Font_UnicodeSubset.Font_UnicodeSubset_Korean
    Font_UnicodeSubset_Western: OCP.Font.Font_UnicodeSubset # value = Font_UnicodeSubset.Font_UnicodeSubset_Western
    __entries: dict # value = {'Font_UnicodeSubset_Western': (Font_UnicodeSubset.Font_UnicodeSubset_Western, None), 'Font_UnicodeSubset_Korean': (Font_UnicodeSubset.Font_UnicodeSubset_Korean, None), 'Font_UnicodeSubset_CJK': (Font_UnicodeSubset.Font_UnicodeSubset_CJK, None), 'Font_UnicodeSubset_Arabic': (Font_UnicodeSubset.Font_UnicodeSubset_Arabic, None)}
    __members__: dict # value = {'Font_UnicodeSubset_Western': Font_UnicodeSubset.Font_UnicodeSubset_Western, 'Font_UnicodeSubset_Korean': Font_UnicodeSubset.Font_UnicodeSubset_Korean, 'Font_UnicodeSubset_CJK': Font_UnicodeSubset.Font_UnicodeSubset_CJK, 'Font_UnicodeSubset_Arabic': Font_UnicodeSubset.Font_UnicodeSubset_Arabic}
    pass
def IsEqual(theFirstFont : Font_SystemFont,theSecondFont : Font_SystemFont) -> bool:
    """
    None
    """
Font_FA_Bold: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Bold
Font_FA_BoldItalic: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_BoldItalic
Font_FA_Italic: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Italic
Font_FA_Regular: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Regular
Font_FA_Undefined: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_UNDEFINED
Font_FontAspect_Bold: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Bold
Font_FontAspect_BoldItalic: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_BoldItalic
Font_FontAspect_Italic: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Italic
Font_FontAspect_NB = 4
Font_FontAspect_Regular: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_Regular
Font_FontAspect_UNDEFINED: OCP.Font.Font_FontAspect # value = Font_FontAspect.Font_FontAspect_UNDEFINED
Font_StrictLevel_Aliases: OCP.Font.Font_StrictLevel # value = Font_StrictLevel.Font_StrictLevel_Aliases
Font_StrictLevel_Any: OCP.Font.Font_StrictLevel # value = Font_StrictLevel.Font_StrictLevel_Any
Font_StrictLevel_Strict: OCP.Font.Font_StrictLevel # value = Font_StrictLevel.Font_StrictLevel_Strict
Font_UnicodeSubset_Arabic: OCP.Font.Font_UnicodeSubset # value = Font_UnicodeSubset.Font_UnicodeSubset_Arabic
Font_UnicodeSubset_CJK: OCP.Font.Font_UnicodeSubset # value = Font_UnicodeSubset.Font_UnicodeSubset_CJK
Font_UnicodeSubset_Korean: OCP.Font.Font_UnicodeSubset # value = Font_UnicodeSubset.Font_UnicodeSubset_Korean
Font_UnicodeSubset_NB = 3
Font_UnicodeSubset_Western: OCP.Font.Font_UnicodeSubset # value = Font_UnicodeSubset.Font_UnicodeSubset_Western
