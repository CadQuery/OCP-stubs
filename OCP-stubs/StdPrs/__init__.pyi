import OCP.StdPrs
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.BRep
import OCP.Poly
import OCP.NCollection
import OCP.HLRAlgo
import OCP.BRepAdaptor
import OCP.Standard
import OCP.TopoDS
import OCP.Prs3d
import OCP.Adaptor3d
import OCP.Adaptor2d
import OCP.Font
import OCP.TColgp
import OCP.Bnd
import OCP.TopLoc
import OCP.Graphic3d
import OCP.gp
import OCP.Geom
import OCP.TopAbs
import OCP.TCollection
import OCP.TColStd
__all__  = [
"StdPrs_BRepFont",
"StdPrs_BRepTextBuilder",
"StdPrs_Curve",
"StdPrs_DeflectionCurve",
"StdPrs_HLRShapeI",
"StdPrs_HLRShape",
"StdPrs_HLRPolyShape",
"StdPrs_HLRToolShape",
"StdPrs_Isolines",
"StdPrs_Plane",
"StdPrs_Point",
"StdPrs_PoleCurve",
"StdPrs_ShadedShape",
"StdPrs_ShadedSurface",
"StdPrs_ShapeTool",
"StdPrs_ToolPoint",
"StdPrs_ToolRFace",
"StdPrs_ToolTriangulatedShape",
"StdPrs_ToolVertex",
"StdPrs_Vertex",
"StdPrs_Volume",
"StdPrs_WFDeflectionRestrictedFace",
"StdPrs_WFDeflectionSurface",
"StdPrs_WFPoleSurface",
"StdPrs_WFRestrictedFace",
"StdPrs_WFShape",
"StdPrs_WFSurface",
"StdPrs_Volume_Autodetection",
"StdPrs_Volume_Closed",
"StdPrs_Volume_Opened"
]
class StdPrs_BRepFont(OCP.Standard.Standard_Transient):
    """
    This tool provides basic services for rendering of vectorized text glyphs as BRep shapes. Single instance initialize single font for sequential glyphs rendering with implicit caching of already rendered glyphs. Thus position of each glyph in the text is specified by shape location.This tool provides basic services for rendering of vectorized text glyphs as BRep shapes. Single instance initialize single font for sequential glyphs rendering with implicit caching of already rendered glyphs. Thus position of each glyph in the text is specified by shape location.
    """
    @overload
    def AdvanceX(self,theUChar : str,theUCharNext : str) -> float: 
        """
        Compute advance to the next character with kerning applied when applicable. Assuming text rendered horizontally.

        Compute advance to the next character with kerning applied when applicable. Assuming text rendered horizontally.
        """
    @overload
    def AdvanceX(self,theUCharNext : str) -> float: ...
    @overload
    def AdvanceY(self,theUChar : str,theUCharNext : str) -> float: 
        """
        Compute advance to the next character with kerning applied when applicable. Assuming text rendered vertically.

        Compute advance to the next character with kerning applied when applicable. Assuming text rendered vertically.
        """
    @overload
    def AdvanceY(self,theUCharNext : str) -> float: ...
    def Ascender(self) -> float: 
        """
        Returns vertical distance from the horizontal baseline to the highest character coordinate.
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
    def FTFont(self) -> OCP.Font.Font_FTFont: 
        """
        Return wrapper over FreeType font.
        """
    @staticmethod
    def FindAndCreate_s(theFontName : OCP.TCollection.TCollection_AsciiString,theFontAspect : OCP.Font.Font_FontAspect,theSize : float,theStrictLevel : OCP.Font.Font_StrictLevel=Font_StrictLevel.Font_StrictLevel_Any) -> StdPrs_BRepFont: 
        """
        Find the font Initialize the font.
        """
    def FindAndInit(self,theFontName : OCP.TCollection.TCollection_AsciiString,theFontAspect : OCP.Font.Font_FontAspect,theSize : float,theStrictLevel : OCP.Font.Font_StrictLevel=Font_StrictLevel.Font_StrictLevel_Any) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theFontName : OCP.NCollection.NCollection_Utf8String,theFontAspect : OCP.Font.Font_FontAspect,theSize : float) -> bool: 
        """
        Initialize the font.
        """
    @overload
    def Init(self,theFontPath : OCP.NCollection.NCollection_Utf8String,theSize : float,theFaceId : int) -> bool: ...
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
    def LineSpacing(self) -> float: 
        """
        Returns default line spacing (the baseline-to-baseline distance).
        """
    def Mutex(self) -> OCP.Standard.Standard_Mutex: 
        """
        Returns mutex.
        """
    def PointSize(self) -> float: 
        """
        Configured point size
        """
    def Release(self) -> None: 
        """
        Release currently loaded font.
        """
    def RenderGlyph(self,theChar : str) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Render single glyph as TopoDS_Shape.
        """
    def Scale(self) -> float: 
        """
        Returns scaling factor for current font size.
        """
    def SetCompositeCurveMode(self,theToConcatenate : bool) -> None: 
        """
        Setup glyph geometry construction mode. By default algorithm creates independent TopoDS_Edge for each original curve in the glyph (line segment or Bezie curve). Algorithm might optionally create composite BSpline curve for each contour which reduces memory footprint but limits curve class to C0. Notice that altering this flag clears currently accumulated cache!
        """
    def SetWidthScaling(self,theScaleFactor : float) -> None: 
        """
        Setup glyph scaling along X-axis. By default glyphs are not scaled (scaling factor = 1.0)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theFontName : OCP.NCollection.NCollection_Utf8String,theFontAspect : OCP.Font.Font_FontAspect,theSize : float,theStrictLevel : OCP.Font.Font_StrictLevel=Font_StrictLevel.Font_StrictLevel_Any) -> None: ...
    @overload
    def __init__(self,theFontPath : OCP.NCollection.NCollection_Utf8String,theSize : float,theFaceId : int=0) -> None: ...
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
class StdPrs_BRepTextBuilder():
    """
    Represents class for applying text formatting.
    """
    @overload
    def Perform(self,theFont : StdPrs_BRepFont,theString : OCP.NCollection.NCollection_Utf8String,thePenLoc : OCP.gp.gp_Ax3=OCP.gp.gp_Ax3,theHAlign : OCP.Graphic3d.Graphic3d_HorizontalTextAlignment=Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_LEFT,theVAlign : OCP.Graphic3d.Graphic3d_VerticalTextAlignment=Graphic3d_VerticalTextAlignment.Graphic3d_VTA_BOTTOM) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Render text as BRep shape.

        Render text as BRep shape.
        """
    @overload
    def Perform(self,theFont : StdPrs_BRepFont,theFormatter : OCP.Font.Font_TextFormatter,thePenLoc : OCP.gp.gp_Ax3=OCP.gp.gp_Ax3) -> OCP.TopoDS.TopoDS_Shape: ...
    def __init__(self) -> None: ...
    pass
class StdPrs_Curve(OCP.Prs3d.Prs3d_Root):
    """
    A framework to define display of lines, arcs of circles and conic sections. This is done with a fixed number of points, which can be modified.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer,Points : OCP.TColgp.TColgp_SequenceOfPnt,drawCurve : bool=True) -> None: 
        """
        Adds to the presentation aPresentation the drawing of the curve aCurve. The aspect is defined by LineAspect in aDrawer. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        Adds to the presentation aPresentation the drawing of the curve aCurve. The aspect is defined by LineAspect in aDrawer. The drawing will be limited between the points of parameter U1 and U2. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        adds to the presentation aPresentation the drawing of the curve aCurve. The aspect is the current aspect. aDeflection is used in the circle case. Points give a sequence of curve points. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        adds to the presentation aPresentation the drawing of the curve aCurve. The aspect is the current aspect. The drawing will be limited between the points of parameter U1 and U2. aDeflection is used in the circle case. Points give a sequence of curve points. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,Points : OCP.TColgp.TColgp_SequenceOfPnt,aNbPoints : int=30,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDrawer : OCP.Prs3d.Prs3d_Drawer,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer,drawCurve : bool=True) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDeflection : float,aLimit : float,aNbPoints : int) -> bool: 
        """
        returns true if the distance between the point (X,Y,Z) and the drawing of the curve is less than aDistance.

        returns true if the distance between the point (X,Y,Z) and the drawing of the curve is less than aDistance.

        returns true if the distance between the point (X,Y,Z) and the drawing of the curve aCurve is less than aDistance. The drawing is considered between the points of parameter U1 and U2;

        returns true if the distance between the point (X,Y,Z) and the drawing of the curve aCurve is less than aDistance. The drawing is considered between the points of parameter U1 and U2;
        """
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: ...
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDeflection : float,aNbPoints : int) -> bool: ...
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_DeflectionCurve(OCP.Prs3d.Prs3d_Root):
    """
    A framework to provide display of any curve with respect to the maximal chordal deviation defined in the Prs3d_Drawer attributes manager.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDeflection : float,aLimit : float,anAngle : float=0.2,drawCurve : bool=True) -> None: 
        """
        adds to the presentation aPresentation the drawing of the curve aCurve with respect to the maximal chordial deviation defined by the drawer aDrawer. The aspect is defined by LineAspect in aDrawer. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        adds to the presentation aPresentation the drawing of the curve aCurve with respect to the maximal chordial deviation defined by the drawer aDrawer. The aspect is defined by LineAspect in aDrawer. The drawing will be limited between the points of parameter U1 and U2. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        adds to the presentation aPresentation the drawing of the curve aCurve with respect to the maximal chordial deviation aDeflection. The aspect is the current aspect If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        adds to the presentation aPresentation the drawing of the curve aCurve with respect to the maximal chordial deviation aDeflection. The aspect is the current aspect Points give a sequence of curve points. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        adds to the presentation aPresentation the drawing of the curve aCurve with respect to the maximal chordial deviation aDeflection. The aspect is the current aspect The drawing will be limited between the points of parameter U1 and U2. Points give a sequence of curve points. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDrawer : OCP.Prs3d.Prs3d_Drawer,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDeflection : float,aDrawer : OCP.Prs3d.Prs3d_Drawer,Points : OCP.TColgp.TColgp_SequenceOfPnt,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDeflection : float,Points : OCP.TColgp.TColgp_SequenceOfPnt,anAngle : float=0.2,drawCurve : bool=True) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    @overload
    def Match_s(theX : float,theY : float,theZ : float,theDistance : float,theCurve : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theLimit : float,theAngle : float) -> bool: 
        """
        returns true if the distance between the point (X,Y,Z) and the drawing of the curve aCurve with respect of the maximal chordial deviation defined by the drawer aDrawer is less then aDistance.

        returns true if the distance between the point (X,Y,Z) and the drawing of the curve aCurve with respect of the maximal chordial deviation defined by the drawer aDrawer is less then aDistance. The drawing is considered between the points of parameter U1 and U2;

        Returns true if the distance between the point (theX, theY, theZ) and the drawing with respect of the maximal chordial deviation theDeflection is less then theDistance.

        Returns true if the distance between the point (theX, theY, theZ) and the drawing with respect of the maximal chordial deviation theDeflection is less then theDistance. The drawing is considered between the points of parameter theU1 and theU2.
        """
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: ...
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: ...
    @staticmethod
    @overload
    def Match_s(theX : float,theY : float,theZ : float,theDistance : float,theCurve : OCP.Adaptor3d.Adaptor3d_Curve,theU1 : float,theU2 : float,theDeflection : float,theAngle : float) -> bool: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_HLRShapeI(OCP.Standard.Standard_Transient):
    """
    Computes the presentation of objects with removal of their hidden lines for a specific projector.
    """
    def ComputeHLR(self,thePrs : OCP.Graphic3d.Graphic3d_Structure,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer,theProjector : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Compute presentation for specified shape.
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
class StdPrs_HLRShape(StdPrs_HLRShapeI, OCP.Standard.Standard_Transient):
    """
    Computes the presentation of objects with removal of their hidden lines for a specific projector. The exact algorithm is used.
    """
    def ComputeHLR(self,thePrs : OCP.Graphic3d.Graphic3d_Structure,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer,theProjector : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Compute presentation for specified shape.
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
class StdPrs_HLRPolyShape(StdPrs_HLRShapeI, OCP.Standard.Standard_Transient):
    """
    Instantiates Prs3d_PolyHLRShape to define a display of a shape where hidden and visible lines are identified with respect to a given projection. StdPrs_HLRPolyShape works with a polyhedral simplification of the shape whereas StdPrs_HLRShape takes the shape itself into account. When you use StdPrs_HLRShape, you obtain an exact result, whereas, when you use StdPrs_HLRPolyShape, you reduce computation time but obtain polygonal segments. The polygonal algorithm is used.
    """
    def ComputeHLR(self,thePrs : OCP.Graphic3d.Graphic3d_Structure,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer,theProjector : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Compute presentation for specified shape.
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
class StdPrs_HLRToolShape():
    """
    None
    """
    def Hidden(self,TheEdge : OCP.BRepAdaptor.BRepAdaptor_Curve) -> Tuple[float, float]: 
        """
        None
        """
    def InitHidden(self,EdgeNumber : int) -> None: 
        """
        None
        """
    def InitVisible(self,EdgeNumber : int) -> None: 
        """
        None
        """
    def MoreHidden(self) -> bool: 
        """
        None
        """
    def MoreVisible(self) -> bool: 
        """
        None
        """
    def NbEdges(self) -> int: 
        """
        None
        """
    def NextHidden(self) -> None: 
        """
        None
        """
    def NextVisible(self) -> None: 
        """
        None
        """
    def Visible(self,TheEdge : OCP.BRepAdaptor.BRepAdaptor_Curve) -> Tuple[float, float]: 
        """
        None
        """
    def __init__(self,TheShape : OCP.TopoDS.TopoDS_Shape,TheProjector : OCP.HLRAlgo.HLRAlgo_Projector) -> None: ...
    pass
class StdPrs_Isolines(OCP.Prs3d.Prs3d_Root):
    """
    Tool for computing isoline representation for a face or surface. Depending on a flags set to the given Prs3d_Drawer instance, on-surface (is used by default) or on-triangulation isoline builder algorithm will be used. If the given shape is not triangulated, on-surface isoline builder will be applied regardless of Prs3d_Drawer flags.
    """
    @staticmethod
    @overload
    def AddOnSurface_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theSurface : OCP.BRepAdaptor.BRepAdaptor_Surface,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float,theUIsoParams : OCP.TColStd.TColStd_SequenceOfReal,theVIsoParams : OCP.TColStd.TColStd_SequenceOfReal) -> None: 
        """
        Computes isolines on surface and adds them to presentation.

        Computes isolines on surface and adds them to presentation.

        Computes isolines on surface and adds them to presentation.
        """
    @staticmethod
    @overload
    def AddOnSurface_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float) -> None: ...
    @staticmethod
    @overload
    def AddOnSurface_s(theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float,theUPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt,theVPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: ...
    @staticmethod
    @overload
    def AddOnTriangulation_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Computes isolines on triangulation and adds them to a presentation.

        Computes isolines on triangulation.

        Computes isolines on triangulation and adds them to a presentation.
        """
    @staticmethod
    @overload
    def AddOnTriangulation_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theTriangulation : OCP.Poly.Poly_Triangulation,theSurface : OCP.Geom.Geom_Surface,theLocation : OCP.TopLoc.TopLoc_Location,theDrawer : OCP.Prs3d.Prs3d_Drawer,theUIsoParams : OCP.TColStd.TColStd_SequenceOfReal,theVIsoParams : OCP.TColStd.TColStd_SequenceOfReal) -> None: ...
    @staticmethod
    @overload
    def AddOnTriangulation_s(theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theUPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt,theVPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: ...
    @staticmethod
    @overload
    def Add_s(theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float,theUPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt,theVPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: 
        """
        Computes isolines presentation for a TopoDS face. This method chooses proper version of isoline builder algorithm : on triangulation or surface depending on the flag passed from Prs3d_Drawer attributes. This method is a default way to display isolines for a given TopoDS face.

        Computes isolines presentation for a TopoDS face. This method chooses proper version of isoline builder algorithm : on triangulation or surface depending on the flag passed from Prs3d_Drawer attributes. This method is a default way to display isolines for a given TopoDS face.
        """
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def UVIsoParameters_s(theFace : OCP.TopoDS.TopoDS_Face,theNbIsoU : int,theNbIsoV : int,theUVLimit : float,theUIsoParams : OCP.TColStd.TColStd_SequenceOfReal,theVIsoParams : OCP.TColStd.TColStd_SequenceOfReal) -> Tuple[float, float, float, float]: 
        """
        Evaluate sequence of parameters for drawing uv isolines for a given face.
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_Plane(OCP.Prs3d.Prs3d_Root):
    """
    A framework to display infinite planes.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aPlane : OCP.Adaptor3d.Adaptor3d_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Defines display of infinite planes. The infinite plane aPlane is added to the display aPresentation, and the attributes of the display are defined by the attribute manager aDrawer.
        """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aPlane : OCP.Adaptor3d.Adaptor3d_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        returns true if the distance between the point (X,Y,Z) and the plane is less than aDistance.
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_Point():
    """
    None
    """
    @staticmethod
    def Add_s(thePrs : OCP.Graphic3d.Graphic3d_Structure,thePoint : OCP.Geom.Geom_Point,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        None
        """
    @staticmethod
    def Match_s(thePoint : OCP.Geom.Geom_Point,theX : float,theY : float,theZ : float,theDistance : float) -> bool: 
        """
        None
        """
    pass
class StdPrs_PoleCurve(OCP.Prs3d.Prs3d_Root):
    """
    A framework to provide display of Bezier or BSpline curves (by drawing a broken line linking the poles of the curve).
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Defines display of BSpline and Bezier curves. Adds the 3D curve aCurve to the StdPrs_PoleCurve algorithm. This shape is found in the presentation object aPresentation, and its display attributes are set in the attribute manager aDrawer. The curve object from Adaptor3d provides data from a Geom curve. This makes it possible to use the surface in a geometric algorithm.
        """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        returns true if the distance between the point (X,Y,Z) and the broken line made of the poles is less then aDistance.
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def Pick_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> int: 
        """
        returns the pole the most near of the point (X,Y,Z) and returns its range. The distance between the pole and (X,Y,Z) must be less then aDistance. If no pole corresponds, 0 is returned.
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_ShadedShape(OCP.Prs3d.Prs3d_Root):
    """
    Auxiliary procedures to prepare Shaded presentation of specified shape.
    """
    @staticmethod
    def AddWireframeForFacesWithoutTriangles_s(thePrs : OCP.Graphic3d.Graphic3d_Structure,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Computes special wireframe presentation for faces without triangulation.
        """
    @staticmethod
    def AddWireframeForFreeElements_s(thePrs : OCP.Graphic3d.Graphic3d_Structure,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Computes wireframe presentation for free wires and vertices
        """
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer,theVolume : StdPrs_Volume=StdPrs_Volume.StdPrs_Volume_Autodetection) -> None: 
        """
        Shades <theShape>.

        Shades <theShape> with texture coordinates.
        """
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer,theHasTexels : bool,theUVOrigin : OCP.gp.gp_Pnt2d,theUVRepeat : OCP.gp.gp_Pnt2d,theUVScale : OCP.gp.gp_Pnt2d,theVolume : StdPrs_Volume=StdPrs_Volume.StdPrs_Volume_Autodetection) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def ExploreSolids_s(theShape : OCP.TopoDS.TopoDS_Shape,theBuilder : OCP.BRep.BRep_Builder,theClosed : OCP.TopoDS.TopoDS_Compound,theOpened : OCP.TopoDS.TopoDS_Compound,theIgnore1DSubShape : bool) -> None: 
        """
        Searches closed and unclosed subshapes in shape structure and puts them into two compounds for separate processing of closed and unclosed sub-shapes
        """
    @staticmethod
    def FillFaceBoundaries_s(theShape : OCP.TopoDS.TopoDS_Shape,theUpperContinuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_CN) -> OCP.Graphic3d.Graphic3d_ArrayOfSegments: 
        """
        Define primitive array of boundary segments for specified shape.
        """
    @staticmethod
    @overload
    def FillTriangles_s(theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: 
        """
        Create primitive array with triangles for specified shape.

        Create primitive array of triangles for specified shape.
        """
    @staticmethod
    @overload
    def FillTriangles_s(theShape : OCP.TopoDS.TopoDS_Shape,theHasTexels : bool,theUVOrigin : OCP.gp.gp_Pnt2d,theUVRepeat : OCP.gp.gp_Pnt2d,theUVScale : OCP.gp.gp_Pnt2d) -> OCP.Graphic3d.Graphic3d_ArrayOfTriangles: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_ShadedSurface(OCP.Prs3d.Prs3d_Root):
    """
    Computes the shading presentation of surfaces. Draws a surface by drawing the isoparametric curves with respect to a maximal chordial deviation. The number of isoparametric curves to be drawn and their color are controlled by the furnished Drawer.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aSurface : OCP.Adaptor3d.Adaptor3d_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Adds the surface aSurface to the presentation object aPresentation. The surface's display attributes are set in the attribute manager aDrawer. The surface object from Adaptor3d provides data from a Geom surface in order to use the surface in an algorithm.
        """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_ShapeTool():
    """
    Describes the behaviour requested for a wireframe shape presentation.
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
class StdPrs_ToolPoint():
    """
    None
    """
    @staticmethod
    def Coord_s(aPoint : OCP.Geom.Geom_Point) -> Tuple[float, float, float]: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_ToolRFace():
    """
    Iterator over 2D curves restricting a face (skipping internal/external edges). In addition, the algorithm skips NULL curves - IsInvalidGeometry() can be checked if this should be handled within algorithm.
    """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Return current edge.
        """
    def Init(self) -> None: 
        """
        Move iterator to the first element.
        """
    def IsInvalidGeometry(self) -> bool: 
        """
        Return TRUE if NULL curves have been skipped.
        """
    def IsOriented(self) -> bool: 
        """
        Return TRUE indicating that iterator looks only for oriented edges.
        """
    def More(self) -> bool: 
        """
        Return TRUE if iterator points to the curve.
        """
    def Next(self) -> None: 
        """
        Go to the next curve in the face.
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Return current edge orientation.
        """
    def Value(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Return current curve.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aSurface : OCP.BRepAdaptor.BRepAdaptor_Surface) -> None: ...
    pass
class StdPrs_ToolTriangulatedShape():
    """
    None
    """
    @staticmethod
    def ClearOnOwnDeflectionChange_s(theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer,theToResetCoeff : bool) -> None: 
        """
        If presentation has own deviation coefficient and IsAutoTriangulation() is true, function will compare actual coefficients with previous values and will clear triangulation on their change (regardless actual tessellation quality). Function is placed here for compatibility reasons - new code should avoid using IsAutoTriangulation().
        """
    @staticmethod
    @overload
    def ComputeNormals_s(theFace : OCP.TopoDS.TopoDS_Face,theTris : OCP.Poly.Poly_Triangulation) -> None: 
        """
        Computes nodal normals for Poly_Triangulation structure using UV coordinates and surface. Does nothing if triangulation already defines normals.

        Computes nodal normals for Poly_Triangulation structure using UV coordinates and surface. Does nothing if triangulation already defines normals.
        """
    @staticmethod
    @overload
    def ComputeNormals_s(theFace : OCP.TopoDS.TopoDS_Face,theTris : OCP.Poly.Poly_Triangulation,thePolyConnect : OCP.Poly.Poly_Connect) -> None: ...
    @staticmethod
    def GetDeflection_s(theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> float: 
        """
        Computes the absolute deflection value depending on the type of deflection in theDrawer: Aspect_TOD_RELATIVE: the absolute deflection is computed using the relative deviation coefficient from theDrawer and the shape's bounding box; Aspect_TOD_ABSOLUTE: the maximal chordial deviation from theDrawer is returned. In case of the type of deflection in theDrawer computed relative deflection for shape is stored as absolute deflection. It is necessary to use it later on for sub-shapes. This function should always be used to compute the deflection value for building discrete representations of the shape (triangualtion, wireframe) to avoid incosistencies between different representations of the shape and undesirable visual artifacts.
        """
    @staticmethod
    def IsClosed_s(theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks back faces visibility for specified shape (to activate back-face culling).
        """
    @staticmethod
    def IsTessellated_s(theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        Checks whether the shape is properly triangulated for a given display settings.
        """
    @staticmethod
    def IsTriangulated_s(theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Similar to BRepTools::Triangulation() but without extra checks.
        """
    @staticmethod
    def Normal_s(theFace : OCP.TopoDS.TopoDS_Face,thePolyConnect : OCP.Poly.Poly_Connect,theNormals : OCP.TColgp.TColgp_Array1OfDir) -> None: 
        """
        Evaluate normals for a triangle of a face.
        """
    @staticmethod
    def Tessellate_s(theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        Validates triangulation within the shape and performs tessellation if necessary.
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_ToolVertex():
    """
    None
    """
    @staticmethod
    def Coord_s(aPoint : OCP.TopoDS.TopoDS_Vertex) -> Tuple[float, float, float]: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_Vertex():
    """
    None
    """
    @staticmethod
    def Add_s(thePrs : OCP.Graphic3d.Graphic3d_Structure,thePoint : OCP.TopoDS.TopoDS_Vertex,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        None
        """
    @staticmethod
    def Match_s(thePoint : OCP.TopoDS.TopoDS_Vertex,theX : float,theY : float,theZ : float,theDistance : float) -> bool: 
        """
        None
        """
    pass
class StdPrs_Volume():
    """
    defines the way how to interpret input shapes Volume_Autodetection to perform Autodetection (would split input shape into two groups) Volume_Closed as Closed volumes (to activate back-face culling and capping plane algorithms) Volume_Opened as Open volumes (shells or solids with holes)

    Members:

      StdPrs_Volume_Autodetection

      StdPrs_Volume_Closed

      StdPrs_Volume_Opened
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
    StdPrs_Volume_Autodetection: OCP.StdPrs.StdPrs_Volume # value = <StdPrs_Volume.StdPrs_Volume_Autodetection: 0>
    StdPrs_Volume_Closed: OCP.StdPrs.StdPrs_Volume # value = <StdPrs_Volume.StdPrs_Volume_Closed: 1>
    StdPrs_Volume_Opened: OCP.StdPrs.StdPrs_Volume # value = <StdPrs_Volume.StdPrs_Volume_Opened: 2>
    __entries: dict # value = {'StdPrs_Volume_Autodetection': (<StdPrs_Volume.StdPrs_Volume_Autodetection: 0>, None), 'StdPrs_Volume_Closed': (<StdPrs_Volume.StdPrs_Volume_Closed: 1>, None), 'StdPrs_Volume_Opened': (<StdPrs_Volume.StdPrs_Volume_Opened: 2>, None)}
    __members__: dict # value = {'StdPrs_Volume_Autodetection': <StdPrs_Volume.StdPrs_Volume_Autodetection: 0>, 'StdPrs_Volume_Closed': <StdPrs_Volume.StdPrs_Volume_Closed: 1>, 'StdPrs_Volume_Opened': <StdPrs_Volume.StdPrs_Volume_Opened: 2>}
    pass
class StdPrs_WFDeflectionRestrictedFace(OCP.Prs3d.Prs3d_Root):
    """
    A framework to provide display of U and V isoparameters of faces, while allowing you to impose a deflection on them. Computes the wireframe presentation of faces with restrictions by displaying a given number of U and/or V isoparametric curves. The isoparametric curves are drawn with respect to a maximal chordial deviation. The presentation includes the restriction curves.
    """
    @staticmethod
    def AddUIso_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aFace : OCP.BRepAdaptor.BRepAdaptor_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Defines a display featuring U isoparameters respectively. Add the surface aFace to the StdPrs_WFRestrictedFace algorithm. This face is found in a shape in the presentation object aPresentation, and its display attributes - in particular, the number of U isoparameters - are set in the attribute manager aDrawer. aFace is BRepAdaptor_Surface surface created from a face in a topological shape. which is passed to the function as an argument through the BRepAdaptor_Surface surface created from it. This is what allows the topological face to be treated as a geometric surface.
        """
    @staticmethod
    def AddVIso_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aFace : OCP.BRepAdaptor.BRepAdaptor_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Defines a display featuring V isoparameters respectively. Add the surface aFace to the StdPrs_WFRestrictedFace algorithm. This face is found in a shape in the presentation object aPresentation, and its display attributes - in particular, the number of V isoparameters - are set in the attribute manager aDrawer. aFace is BRepAdaptor_Surface surface created from a face in a topological shape. which is passed to the function as an argument through the BRepAdaptor_Surface surface created from it. This is what allows the topological face to be treated as a geometric surface.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aFace : OCP.BRepAdaptor.BRepAdaptor_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Defines a display featuring U and V isoparameters. Adds the surface aFace to the StdPrs_WFRestrictedFace algorithm. This face is found in a shape in the presentation object aPresentation, and its display attributes - in particular, the number of U and V isoparameters - are set in the attribute manager aDrawer. aFace is BRepAdaptor_Surface surface created from a face in a topological shape. which is passed as an argument through the BRepAdaptor_Surface surface created from it. This is what allows the topological face to be treated as a geometric surface.

        Defines a display of a delection-specified face. The display will feature U and V isoparameters. Adds the topology aShape to the StdPrs_WFRestrictedFace algorithm. This shape is found in the presentation object aPresentation, and its display attributes - except the number of U and V isoparameters - are set in the attribute manager aDrawer. The function sets the number of U and V isoparameters, NBUiso and NBViso, in the shape. To do this, the arguments DrawUIso and DrawVIso must be true. aFace is BRepAdaptor_Surface surface created from a face in a topological shape. which is passed as an argument through the BRepAdaptor_Surface surface created from it. This is what allows the topological face to be treated as a geometric surface. Curves give a sequence of face curves, it is used if the PrimitiveArray visualization approach is activated (it is activated by default).
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aFace : OCP.BRepAdaptor.BRepAdaptor_Surface,DrawUIso : bool,DrawVIso : bool,Deflection : float,NBUiso : int,NBViso : int,aDrawer : OCP.Prs3d.Prs3d_Drawer,Curves : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def MatchUIso_s(X : float,Y : float,Z : float,aDistance : float,aFace : OCP.BRepAdaptor.BRepAdaptor_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None
        """
    @staticmethod
    def MatchVIso_s(X : float,Y : float,Z : float,aDistance : float,aFace : OCP.BRepAdaptor.BRepAdaptor_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aFace : OCP.BRepAdaptor.BRepAdaptor_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aFace : OCP.BRepAdaptor.BRepAdaptor_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer,DrawUIso : bool,DrawVIso : bool,aDeflection : float,NBUiso : int,NBViso : int) -> bool: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_WFDeflectionSurface(OCP.Prs3d.Prs3d_Root):
    """
    Draws a surface by drawing the isoparametric curves with respect to a maximal chordial deviation. The number of isoparametric curves to be drawn and their color are controlled by the furnished Drawer.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aSurface : OCP.Adaptor3d.Adaptor3d_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Adds the surface aSurface to the presentation object aPresentation, and defines its boundaries and isoparameters. The shape's display attributes are set in the attribute manager aDrawer. These include whether deflection is absolute or relative to the size of the shape. The surface aSurface is a surface object from Adaptor, and provides data from a Geom surface. This makes it possible to use the surface in a geometric algorithm. Note that this surface object is manipulated by handles.
        """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_WFPoleSurface(OCP.Prs3d.Prs3d_Root):
    """
    Computes the presentation of surfaces by drawing a double network of lines linking the poles of the surface in the two parametric direction. The number of lines to be drawn is controlled by the NetworkNumber of the given Drawer.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aSurface : OCP.Adaptor3d.Adaptor3d_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Adds the surface aSurface to the presentation object aPresentation. The shape's display attributes are set in the attribute manager aDrawer. The surface aSurface is a surface object from Adaptor3d, and provides data from a Geom surface. This makes it possible to use the surface in a geometric algorithm.
        """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_WFRestrictedFace(OCP.Prs3d.Prs3d_Root):
    """
    None
    """
    @staticmethod
    def AddUIso_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.BRepAdaptor.BRepAdaptor_Surface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        None
        """
    @staticmethod
    def AddVIso_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.BRepAdaptor.BRepAdaptor_Surface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.BRepAdaptor.BRepAdaptor_Surface,theDrawUIso : bool,theDrawVIso : bool,theNbUIso : int,theNbVIso : int,theDrawer : OCP.Prs3d.Prs3d_Drawer,theCurves : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.BRepAdaptor.BRepAdaptor_Surface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def MatchUIso_s(theX : float,theY : float,theZ : float,theDistance : float,theFace : OCP.BRepAdaptor.BRepAdaptor_Surface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None
        """
    @staticmethod
    def MatchVIso_s(theX : float,theY : float,theZ : float,theDistance : float,theFace : OCP.BRepAdaptor.BRepAdaptor_Surface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def Match_s(theX : float,theY : float,theZ : float,theDistance : float,theFace : OCP.BRepAdaptor.BRepAdaptor_Surface,theDrawUIso : bool,theDrawVIso : bool,theDeflection : float,theNbUIso : int,theNbVIso : int,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Match_s(theX : float,theY : float,theZ : float,theDistance : float,theFace : OCP.BRepAdaptor.BRepAdaptor_Surface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_WFShape(OCP.Prs3d.Prs3d_Root):
    """
    Tool for computing wireframe presentation of a TopoDS_Shape.
    """
    @staticmethod
    def AddAllEdges_s(theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> OCP.Graphic3d.Graphic3d_ArrayOfPrimitives: 
        """
        Compute all edges (wire, free, unfree) and put them into single primitive array.
        """
    @staticmethod
    @overload
    def AddEdgesOnTriangulation_s(theShape : OCP.TopoDS.TopoDS_Shape,theToExcludeGeometric : bool=True) -> OCP.Graphic3d.Graphic3d_ArrayOfPrimitives: 
        """
        Compute free and boundary edges on a triangulation of each face in the given shape.

        Compute free and boundary edges on a triangulation of each face in the given shape.
        """
    @staticmethod
    @overload
    def AddEdgesOnTriangulation_s(theSegments : OCP.TColgp.TColgp_SequenceOfPnt,theShape : OCP.TopoDS.TopoDS_Shape,theToExcludeGeometric : bool=True) -> None: ...
    @staticmethod
    def AddVertexes_s(theShape : OCP.TopoDS.TopoDS_Shape,theVertexMode : OCP.Prs3d.Prs3d_VertexDrawMode) -> OCP.Graphic3d.Graphic3d_ArrayOfPoints: 
        """
        Compute vertex presentation for a shape.
        """
    @staticmethod
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theShape : OCP.TopoDS.TopoDS_Shape,theDrawer : OCP.Prs3d.Prs3d_Drawer,theIsParallel : bool=False) -> None: 
        """
        Computes wireframe presentation of a shape.
        """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_WFSurface(OCP.Prs3d.Prs3d_Root):
    """
    Computes the wireframe presentation of surfaces by displaying a given number of U and/or V isoparametric curves. The isoparametric curves are drawn with respect to a given number of points.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aSurface : OCP.Adaptor3d.Adaptor3d_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Draws a surface by drawing the isoparametric curves with respect to a fixed number of points given by the Drawer. The number of isoparametric curves to be drawn and their color are controlled by the furnished Drawer.
        """
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
StdPrs_Volume_Autodetection: OCP.StdPrs.StdPrs_Volume # value = <StdPrs_Volume.StdPrs_Volume_Autodetection: 0>
StdPrs_Volume_Closed: OCP.StdPrs.StdPrs_Volume # value = <StdPrs_Volume.StdPrs_Volume_Closed: 1>
StdPrs_Volume_Opened: OCP.StdPrs.StdPrs_Volume # value = <StdPrs_Volume.StdPrs_Volume_Opened: 2>
