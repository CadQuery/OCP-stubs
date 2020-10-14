import OCP.StdPrs
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.BRep
import OCP.TColgp
import OCP.HLRAlgo
import OCP.Adaptor3d
import OCP.TopoDS
import OCP.BRepAdaptor
import OCP.Adaptor2d
import OCP.gp
import OCP.TColStd
import OCP.Poly
import OCP.Bnd
import OCP.Graphic3d
import OCP.Prs3d
import OCP.Geom
import OCP.TopLoc
__all__  = [
"StdPrs_BndBox",
"StdPrs_Curve",
"StdPrs_DeflectionCurve",
"StdPrs_HLRPolyShape",
"StdPrs_HLRShape",
"StdPrs_HLRToolShape",
"StdPrs_Isolines",
"StdPrs_Plane",
"StdPrs_Point",
"StdPrs_PoleCurve",
"StdPrs_ShadedShape",
"StdPrs_ShadedSurface",
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
class StdPrs_BndBox(OCP.Prs3d.Prs3d_Root):
    """
    Tool for computing bounding box presentation.
    """
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theBndBox : OCP.Bnd.Bnd_OBB,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Computes presentation of a bounding box.

        Computes presentation of a bounding box.
        """
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theBndBox : OCP.Bnd.Bnd_Box,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    @overload
    def FillSegments_s(theSegments : OCP.Graphic3d.Graphic3d_ArrayOfSegments,theBox : OCP.Bnd.Bnd_OBB) -> None: 
        """
        Create primitive array with line segments for displaying a box.

        Create primitive array with line segments for displaying a box.

        Create primitive array with line segments for displaying a box.

        Create primitive array with line segments for displaying a box.
        """
    @staticmethod
    @overload
    def FillSegments_s(theSegments : OCP.Graphic3d.Graphic3d_ArrayOfSegments,theBox : OCP.Bnd.Bnd_Box) -> None: ...
    @staticmethod
    @overload
    def FillSegments_s(theBox : OCP.Bnd.Bnd_OBB) -> OCP.Graphic3d.Graphic3d_ArrayOfSegments: ...
    @staticmethod
    @overload
    def FillSegments_s(theBox : OCP.Bnd.Bnd_Box) -> OCP.Graphic3d.Graphic3d_ArrayOfSegments: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def fillSegments_s(theSegments : OCP.Graphic3d.Graphic3d_ArrayOfSegments,theBox : OCP.gp.gp_Pnt) -> None: 
        """
        Create primitive array with line segments for displaying a box.
        """
    pass
class StdPrs_Curve(OCP.Prs3d.Prs3d_Root):
    """
    A framework to define display of lines, arcs of circles and conic sections. This is done with a fixed number of points, which can be modified.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,Points : OCP.TColgp.TColgp_SequenceOfPnt,aNbPoints : int=30,drawCurve : bool=True) -> None: 
        """
        Adds to the presentation aPresentation the drawing of the curve aCurve. The aspect is defined by LineAspect in aDrawer. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        Adds to the presentation aPresentation the drawing of the curve aCurve. The aspect is defined by LineAspect in aDrawer. The drawing will be limited between the points of parameter U1 and U2. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        adds to the presentation aPresentation the drawing of the curve aCurve. The aspect is the current aspect. aDeflection is used in the circle case. Points give a sequence of curve points. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).

        adds to the presentation aPresentation the drawing of the curve aCurve. The aspect is the current aspect. The drawing will be limited between the points of parameter U1 and U2. aDeflection is used in the circle case. Points give a sequence of curve points. If drawCurve equals Standard_False the curve will not be displayed, it is used if the curve is a part of some shape and PrimitiveArray visualization approach is activated (it is activated by default).
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDrawer : OCP.Prs3d.Prs3d_Drawer,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer,Points : OCP.TColgp.TColgp_SequenceOfPnt,drawCurve : bool=True) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
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
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDeflection : float,aLimit : float,aNbPoints : int) -> bool: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
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
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDeflection : float,Points : OCP.TColgp.TColgp_SequenceOfPnt,anAngle : float=0.2,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDrawer : OCP.Prs3d.Prs3d_Drawer,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer,drawCurve : bool=True) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDeflection : float,aDrawer : OCP.Prs3d.Prs3d_Drawer,Points : OCP.TColgp.TColgp_SequenceOfPnt,drawCurve : bool=True) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,U1 : float,U2 : float,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        returns true if the distance between the point (X,Y,Z) and the drawing of the curve aCurve with respect of the maximal chordial deviation defined by the drawer aDrawer is less then aDistance.

        returns true if the distance between the point (X,Y,Z) and the drawing of the curve aCurve with respect of the maximal chordial deviation defined by the drawer aDrawer is less then aDistance. The drawing is considered between the points of parameter U1 and U2;

        Returns true if the distance between the point (theX, theY, theZ) and the drawing with respect of the maximal chordial deviation theDeflection is less then theDistance.

        Returns true if the distance between the point (theX, theY, theZ) and the drawing with respect of the maximal chordial deviation theDeflection is less then theDistance. The drawing is considered between the points of parameter theU1 and theU2.
        """
    @staticmethod
    @overload
    def Match_s(theX : float,theY : float,theZ : float,theDistance : float,theCurve : OCP.Adaptor3d.Adaptor3d_Curve,theDeflection : float,theLimit : float,theAngle : float) -> bool: ...
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: ...
    @staticmethod
    @overload
    def Match_s(theX : float,theY : float,theZ : float,theDistance : float,theCurve : OCP.Adaptor3d.Adaptor3d_Curve,theU1 : float,theU2 : float,theDeflection : float,theAngle : float) -> bool: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_HLRPolyShape(OCP.Prs3d.Prs3d_Root):
    """
    Instantiates Prs3d_PolyHLRShape to define a display of a shape where hidden and visible lines are identified with respect to a given projection. StdPrs_HLRPolyShape works with a polyhedral simplification of the shape whereas StdPrs_HLRShape takes the shape itself into account. When you use StdPrs_HLRShape, you obtain an exact result, whereas, when you use StdPrs_HLRPolyShape, you reduce computation time but obtain polygonal segments. The polygonal algorithm is used.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aShape : OCP.TopoDS.TopoDS_Shape,aDrawer : OCP.Prs3d.Prs3d_Drawer,aProjector : OCP.Prs3d.Prs3d_Projector) -> None: 
        """
        Defines the hidden line removal display of the topology aShape in the projection defined by aProjector. The shape and the projection are added to the display aPresentation, and the attributes of the elements present in the aPresentation are defined by the attribute manager aDrawer.
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
class StdPrs_HLRShape(OCP.Prs3d.Prs3d_Root):
    """
    None
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
    def AddOnSurface_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theSurface : OCP.BRepAdaptor.BRepAdaptor_HSurface,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float,theUIsoParams : OCP.TColStd.TColStd_SequenceOfReal,theVIsoParams : OCP.TColStd.TColStd_SequenceOfReal) -> None: 
        """
        Computes isolines on surface and adds them to presentation.

        Computes isolines on surface and adds them to presentation.

        Computes isolines on surface and adds them to presentation.
        """
    @staticmethod
    @overload
    def AddOnSurface_s(theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float,theUPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt,theVPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: ...
    @staticmethod
    @overload
    def AddOnSurface_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float) -> None: ...
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
    def AddOnTriangulation_s(theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theUPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt,theVPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: ...
    @staticmethod
    @overload
    def AddOnTriangulation_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theTriangulation : OCP.Poly.Poly_Triangulation,theSurface : OCP.Geom.Geom_Surface,theLocation : OCP.TopLoc.TopLoc_Location,theDrawer : OCP.Prs3d.Prs3d_Drawer,theUIsoParams : OCP.TColStd.TColStd_SequenceOfReal,theVIsoParams : OCP.TColStd.TColStd_SequenceOfReal) -> None: ...
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float) -> None: 
        """
        Computes isolines presentation for a TopoDS face. This method chooses proper version of isoline builder algorithm : on triangulation or surface depending on the flag passed from Prs3d_Drawer attributes. This method is a default way to display isolines for a given TopoDS face.

        Computes isolines presentation for a TopoDS face. This method chooses proper version of isoline builder algorithm : on triangulation or surface depending on the flag passed from Prs3d_Drawer attributes. This method is a default way to display isolines for a given TopoDS face.
        """
    @staticmethod
    @overload
    def Add_s(theFace : OCP.TopoDS.TopoDS_Face,theDrawer : OCP.Prs3d.Prs3d_Drawer,theDeflection : float,theUPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt,theVPolylines : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: ...
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
    @staticmethod
    def UVIsoParameters_s(theFace : OCP.TopoDS.TopoDS_Face,theNbIsoU : int,theNbIsoV : int,theUVLimit : float,theUIsoParams : OCP.TColStd.TColStd_SequenceOfReal,theVIsoParams : OCP.TColStd.TColStd_SequenceOfReal) -> Tuple[float, float, float, float]: 
        """
        Evalute sequence of parameters for drawing uv isolines for a given face.
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
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aPlane : OCP.Adaptor3d.Adaptor3d_Surface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        returns true if the distance between the point (X,Y,Z) and the plane is less than aDistance.
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_Point():
    """
    None
    """
    @staticmethod
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,thePoint : OCP.Geom.Geom_Point,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
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
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aCurve : OCP.Adaptor3d.Adaptor3d_Curve,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        returns true if the distance between the point (X,Y,Z) and the broken line made of the poles is less then aDistance.
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
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
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
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
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
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
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
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
    def __init__(self,aSurface : OCP.BRepAdaptor.BRepAdaptor_HSurface) -> None: ...
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
    def ComputeNormals_s(theFace : OCP.TopoDS.TopoDS_Face,theTris : OCP.Poly.Poly_Triangulation,thePolyConnect : OCP.Poly.Poly_Connect) -> None: 
        """
        Computes nodal normals for Poly_Triangulation structure using UV coordinates and surface. Does nothing if triangulation already defines normals.

        Computes nodal normals for Poly_Triangulation structure using UV coordinates and surface. Does nothing if triangulation already defines normals.
        """
    @staticmethod
    @overload
    def ComputeNormals_s(theFace : OCP.TopoDS.TopoDS_Face,theTris : OCP.Poly.Poly_Triangulation) -> None: ...
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
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,thePoint : OCP.TopoDS.TopoDS_Vertex,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
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
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StdPrs_Volume_Autodetection: OCP.StdPrs.StdPrs_Volume # value = StdPrs_Volume.StdPrs_Volume_Autodetection
    StdPrs_Volume_Closed: OCP.StdPrs.StdPrs_Volume # value = StdPrs_Volume.StdPrs_Volume_Closed
    StdPrs_Volume_Opened: OCP.StdPrs.StdPrs_Volume # value = StdPrs_Volume.StdPrs_Volume_Opened
    __entries: dict # value = {'StdPrs_Volume_Autodetection': (StdPrs_Volume.StdPrs_Volume_Autodetection, None), 'StdPrs_Volume_Closed': (StdPrs_Volume.StdPrs_Volume_Closed, None), 'StdPrs_Volume_Opened': (StdPrs_Volume.StdPrs_Volume_Opened, None)}
    __members__: dict # value = {'StdPrs_Volume_Autodetection': StdPrs_Volume.StdPrs_Volume_Autodetection, 'StdPrs_Volume_Closed': StdPrs_Volume.StdPrs_Volume_Closed, 'StdPrs_Volume_Opened': StdPrs_Volume.StdPrs_Volume_Opened}
    pass
class StdPrs_WFDeflectionRestrictedFace(OCP.Prs3d.Prs3d_Root):
    """
    A framework to provide display of U and V isoparameters of faces, while allowing you to impose a deflection on them. Computes the wireframe presentation of faces with restrictions by displaying a given number of U and/or V isoparametric curves. The isoparametric curves are drawn with respect to a maximal chordial deviation. The presentation includes the restriction curves.
    """
    @staticmethod
    def AddUIso_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Defines a display featuring U isoparameters respectively. Add the surface aFace to the StdPrs_WFRestrictedFace algorithm. This face is found in a shape in the presentation object aPresentation, and its display attributes - in particular, the number of U isoparameters - are set in the attribute manager aDrawer. aFace is BRepAdaptor_HSurface surface created from a face in a topological shape. which is passed to the function as an argument through the BRepAdaptor_HSurface surface created from it. This is what allows the topological face to be treated as a geometric surface.
        """
    @staticmethod
    def AddVIso_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Defines a display featuring V isoparameters respectively. Add the surface aFace to the StdPrs_WFRestrictedFace algorithm. This face is found in a shape in the presentation object aPresentation, and its display attributes - in particular, the number of V isoparameters - are set in the attribute manager aDrawer. aFace is BRepAdaptor_HSurface surface created from a face in a topological shape. which is passed to the function as an argument through the BRepAdaptor_HSurface surface created from it. This is what allows the topological face to be treated as a geometric surface.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,DrawUIso : bool,DrawVIso : bool,Deflection : float,NBUiso : int,NBViso : int,aDrawer : OCP.Prs3d.Prs3d_Drawer,Curves : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: 
        """
        Defines a display featuring U and V isoparameters. Adds the surface aFace to the StdPrs_WFRestrictedFace algorithm. This face is found in a shape in the presentation object aPresentation, and its display attributes - in particular, the number of U and V isoparameters - are set in the attribute manager aDrawer. aFace is BRepAdaptor_HSurface surface created from a face in a topological shape. which is passed as an argument through the BRepAdaptor_HSurface surface created from it. This is what allows the topological face to be treated as a geometric surface.

        Defines a display of a delection-specified face. The display will feature U and V isoparameters. Adds the topology aShape to the StdPrs_WFRestrictedFace algorithm. This shape is found in the presentation object aPresentation, and its display attributes - except the number of U and V isoparameters - are set in the attribute manager aDrawer. The function sets the number of U and V isoparameters, NBUiso and NBViso, in the shape. To do this, the arguments DrawUIso and DrawVIso must be true. aFace is BRepAdaptor_HSurface surface created from a face in a topological shape. which is passed as an argument through the BRepAdaptor_HSurface surface created from it. This is what allows the topological face to be treated as a geometric surface. Curves give a sequence of face curves, it is used if the PrimitiveArray visualization approach is activated (it is activated by default).
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    def MatchUIso_s(X : float,Y : float,Z : float,aDistance : float,aFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None
        """
    @staticmethod
    def MatchVIso_s(X : float,Y : float,Z : float,aDistance : float,aFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,aDrawer : OCP.Prs3d.Prs3d_Drawer,DrawUIso : bool,DrawVIso : bool,aDeflection : float,NBUiso : int,NBViso : int) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Match_s(X : float,Y : float,Z : float,aDistance : float,aFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_WFDeflectionSurface(OCP.Prs3d.Prs3d_Root):
    """
    Draws a surface by drawing the isoparametric curves with respect to a maximal chordial deviation. The number of isoparametric curves to be drawn and their color are controlled by the furnished Drawer.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aSurface : OCP.Adaptor3d.Adaptor3d_HSurface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Adds the surface aSurface to the presentation object aPresentation, and defines its boundaries and isoparameters. The shape's display attributes are set in the attribute manager aDrawer. These include whether deflection is absolute or relative to the size of the shape. The surface aSurface is a surface object from Adaptor, and provides data from a Geom surface. This makes it possible to use the surface in a geometric algorithm. Note that this surface object is manipulated by handles.
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
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_WFRestrictedFace(OCP.Prs3d.Prs3d_Root):
    """
    None
    """
    @staticmethod
    def AddUIso_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        None
        """
    @staticmethod
    def AddVIso_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,theDrawUIso : bool,theDrawVIso : bool,theNbUIso : int,theNbVIso : int,theDrawer : OCP.Prs3d.Prs3d_Drawer,theCurves : OCP.Prs3d.Prs3d_NListOfSequenceOfPnt) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: ...
    @staticmethod
    def CurrentGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    def MatchUIso_s(theX : float,theY : float,theZ : float,theDistance : float,theFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None
        """
    @staticmethod
    def MatchVIso_s(theX : float,theY : float,theZ : float,theDistance : float,theFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def Match_s(theX : float,theY : float,theZ : float,theDistance : float,theFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,theDrawUIso : bool,theDrawVIso : bool,theDeflection : float,theNbUIso : int,theNbVIso : int,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Match_s(theX : float,theY : float,theZ : float,theDistance : float,theFace : OCP.BRepAdaptor.BRepAdaptor_HSurface,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> bool: ...
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
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
        Returns the current (last created) group of primititves inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    @staticmethod
    def NewGroup_s(thePrs3d : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Returns the new group of primitives inside graphic objects in the display. A group also contains the attributes whose ranges are limited to the primitives in it.
        """
    def __init__(self) -> None: ...
    pass
class StdPrs_WFSurface(OCP.Prs3d.Prs3d_Root):
    """
    Computes the wireframe presentation of surfaces by displaying a given number of U and/or V isoparametric curves. The isoparametric curves are drawn with respect to a given number of points.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aSurface : OCP.Adaptor3d.Adaptor3d_HSurface,aDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Draws a surface by drawing the isoparametric curves with respect to a fixed number of points given by the Drawer. The number of isoparametric curves to be drawn and their color are controlled by the furnished Drawer.
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
StdPrs_Volume_Autodetection: OCP.StdPrs.StdPrs_Volume # value = StdPrs_Volume.StdPrs_Volume_Autodetection
StdPrs_Volume_Closed: OCP.StdPrs.StdPrs_Volume # value = StdPrs_Volume.StdPrs_Volume_Closed
StdPrs_Volume_Opened: OCP.StdPrs.StdPrs_Volume # value = StdPrs_Volume.StdPrs_Volume_Opened
