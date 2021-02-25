import OCP.DsgPrs
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.Prs3d
import OCP.gp
import OCP.Geom
import OCP.TopoDS
import OCP.Graphic3d
__all__  = [
"DsgPrs",
"DsgPrs_AnglePresentation",
"DsgPrs_ArrowSide",
"DsgPrs_Chamf2dPresentation",
"DsgPrs_ConcentricPresentation",
"DsgPrs_DatumPrs",
"DsgPrs_DiameterPresentation",
"DsgPrs_EllipseRadiusPresentation",
"DsgPrs_EqualDistancePresentation",
"DsgPrs_EqualRadiusPresentation",
"DsgPrs_FilletRadiusPresentation",
"DsgPrs_FixPresentation",
"DsgPrs_IdenticPresentation",
"DsgPrs_LengthPresentation",
"DsgPrs_MidPointPresentation",
"DsgPrs_OffsetPresentation",
"DsgPrs_ParalPresentation",
"DsgPrs_PerpenPresentation",
"DsgPrs_RadiusPresentation",
"DsgPrs_ShadedPlanePresentation",
"DsgPrs_ShapeDirPresentation",
"DsgPrs_SymbPresentation",
"DsgPrs_SymmetricPresentation",
"DsgPrs_TangentPresentation",
"DsgPrs_XYZAxisPresentation",
"DsgPrs_XYZPlanePresentation",
"DsgPrs_AS_BOTHAR",
"DsgPrs_AS_BOTHPT",
"DsgPrs_AS_FIRSTAR",
"DsgPrs_AS_FIRSTAR_LASTPT",
"DsgPrs_AS_FIRSTPT",
"DsgPrs_AS_FIRSTPT_LASTAR",
"DsgPrs_AS_LASTAR",
"DsgPrs_AS_LASTPT",
"DsgPrs_AS_NONE"
]
class DsgPrs():
    """
    Describes Standard Presentations for DsgIHM objects
    """
    @staticmethod
    def ComputeCurvilinearFacesLengthPresentation_s(FirstArrowLength : float,SecondArrowLength : float,SecondSurf : OCP.Geom.Geom_Surface,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,DirAttach : OCP.gp.gp_Dir,EndOfArrow2 : OCP.gp.gp_Pnt,DirOfArrow1 : OCP.gp.gp_Dir,VCurve : OCP.Geom.Geom_Curve,UCurve : OCP.Geom.Geom_Curve) -> Tuple[float, float, float, float]: 
        """
        None
        """
    @staticmethod
    def ComputeFacesAnglePresentation_s(ArrowLength : float,Value : float,CenterPoint : OCP.gp.gp_Pnt,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,dir1 : OCP.gp.gp_Dir,dir2 : OCP.gp.gp_Dir,axisdir : OCP.gp.gp_Dir,isPlane : bool,AxisOfSurf : OCP.gp.gp_Ax1,OffsetPoint : OCP.gp.gp_Pnt,AngleCirc : OCP.gp.gp_Circ,EndOfArrow1 : OCP.gp.gp_Pnt,EndOfArrow2 : OCP.gp.gp_Pnt,DirOfArrow1 : OCP.gp.gp_Dir,DirOfArrow2 : OCP.gp.gp_Dir,ProjAttachPoint2 : OCP.gp.gp_Pnt,AttachCirc : OCP.gp.gp_Circ) -> Tuple[float, float, float, float]: 
        """
        None
        """
    @staticmethod
    def ComputeFilletRadiusPresentation_s(ArrowLength : float,Value : float,Position : OCP.gp.gp_Pnt,NormalDir : OCP.gp.gp_Dir,FirstPoint : OCP.gp.gp_Pnt,SecondPoint : OCP.gp.gp_Pnt,Center : OCP.gp.gp_Pnt,BasePnt : OCP.gp.gp_Pnt,drawRevers : bool,FilletCirc : OCP.gp.gp_Circ,EndOfArrow : OCP.gp.gp_Pnt,DirOfArrow : OCP.gp.gp_Dir,DrawPosition : OCP.gp.gp_Pnt) -> Tuple[bool, float, float]: 
        """
        computes Geometry for fillet radius presentation; special case flag SpecCase equal Standard_True if radius of fillet circle = 0 or if anngle between Vec1(Center, FirstPoint) and Vec2(Center,SecondPoint) equal 0 or PI
        """
    @staticmethod
    def ComputePlanarFacesLengthPresentation_s(FirstArrowLength : float,SecondArrowLength : float,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,DirAttach : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt,PlaneOfFaces : OCP.gp.gp_Pln,EndOfArrow1 : OCP.gp.gp_Pnt,EndOfArrow2 : OCP.gp.gp_Pnt,DirOfArrow1 : OCP.gp.gp_Dir) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeRadiusLine_s(aCenter : OCP.gp.gp_Pnt,anEndOfArrow : OCP.gp.gp_Pnt,aPosition : OCP.gp.gp_Pnt,drawFromCenter : bool,aRadLineOrign : OCP.gp.gp_Pnt,aRadLineEnd : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeSymbol_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,anAspect : OCP.Prs3d.Prs3d_DimensionAspect,pt1 : OCP.gp.gp_Pnt,pt2 : OCP.gp.gp_Pnt,dir1 : OCP.gp.gp_Dir,dir2 : OCP.gp.gp_Dir,ArrowSide : DsgPrs_ArrowSide,drawFromCenter : bool=True) -> None: 
        """
        draws symbols ((one or two) arrows,(one or two)points at thebeginning and at the end of the dimension
        """
    @staticmethod
    def DistanceFromApex_s(elips : OCP.gp.gp_Elips,Apex : OCP.gp.gp_Pnt,par : float) -> float: 
        """
        computes length of ellipse arc in parametric units
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_AnglePresentation():
    """
    A framework for displaying angles.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theval : float,thevalstring : OCP.TCollection.TCollection_ExtendedString,CenterPoint : OCP.gp.gp_Pnt,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,dir1 : OCP.gp.gp_Dir,dir2 : OCP.gp.gp_Dir,axisdir : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt) -> None: 
        """
        Draws the presenation of the full angle of a cone. VminCircle - a circle at V parameter = Vmin VmaxCircle - a circle at V parameter = Vmax aCircle - a circle at V parameter from projection of aPosition to axis of the cone

        Draws the representation of the angle defined by dir1 and dir2, centered on CenterPoint, using the offset point OffsetPoint. Lines are drawn to points AttachmentPoint1 and AttachmentPoint2

        Same as above, but <thevalstring> contains conversion in Session units....

        Same as above, may add one or two Arrows according to <ArrowSide> value

        Same as above, but axisdir contains the axis direction useful for Revol that can be opened with 180 degrees

        Same as above,may add one or two Arrows according to <ArrowSide> value

        simple representation of a poor lonesome angle dimension Draw a line from <theCenter> to <AttachmentPoint1>, then operates a rotation around the perpmay add one or two Arrows according to <ArrowSide> value. The attributes (color,arrowsize,...) are driven by the Drawer.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theval : float,CenterPoint : OCP.gp.gp_Pnt,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,dir1 : OCP.gp.gp_Dir,dir2 : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theval : float,thevalstring : OCP.TCollection.TCollection_ExtendedString,CenterPoint : OCP.gp.gp_Pnt,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,dir1 : OCP.gp.gp_Dir,dir2 : OCP.gp.gp_Dir,axisdir : OCP.gp.gp_Dir,isPlane : bool,AxisOfSurf : OCP.gp.gp_Ax1,OffsetPoint : OCP.gp.gp_Pnt,ArrowSide : DsgPrs_ArrowSide) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theval : float,theCenter : OCP.gp.gp_Pnt,AttachmentPoint1 : OCP.gp.gp_Pnt,theAxe : OCP.gp.gp_Ax1,ArrowSide : DsgPrs_ArrowSide) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theval : float,thevalstring : OCP.TCollection.TCollection_ExtendedString,CenterPoint : OCP.gp.gp_Pnt,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,dir1 : OCP.gp.gp_Dir,dir2 : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt,ArrowSide : DsgPrs_ArrowSide) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theval : float,thevalstring : OCP.TCollection.TCollection_ExtendedString,CenterPoint : OCP.gp.gp_Pnt,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,dir1 : OCP.gp.gp_Dir,dir2 : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aVal : float,aText : OCP.TCollection.TCollection_ExtendedString,aCircle : OCP.gp.gp_Circ,aPosition : OCP.gp.gp_Pnt,Apex : OCP.gp.gp_Pnt,VminCircle : OCP.gp.gp_Circ,VmaxCircle : OCP.gp.gp_Circ,aArrowSize : float) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_ArrowSide():
    """
    Designates how many arrows will be displayed and where they will be displayed in presenting a length.

    Members:

      DsgPrs_AS_NONE

      DsgPrs_AS_FIRSTAR

      DsgPrs_AS_LASTAR

      DsgPrs_AS_BOTHAR

      DsgPrs_AS_FIRSTPT

      DsgPrs_AS_LASTPT

      DsgPrs_AS_BOTHPT

      DsgPrs_AS_FIRSTAR_LASTPT

      DsgPrs_AS_FIRSTPT_LASTAR
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
    DsgPrs_AS_BOTHAR: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_BOTHAR: 3>
    DsgPrs_AS_BOTHPT: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_BOTHPT: 6>
    DsgPrs_AS_FIRSTAR: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR: 1>
    DsgPrs_AS_FIRSTAR_LASTPT: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR_LASTPT: 7>
    DsgPrs_AS_FIRSTPT: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT: 4>
    DsgPrs_AS_FIRSTPT_LASTAR: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT_LASTAR: 8>
    DsgPrs_AS_LASTAR: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_LASTAR: 2>
    DsgPrs_AS_LASTPT: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_LASTPT: 5>
    DsgPrs_AS_NONE: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_NONE: 0>
    __entries: dict # value = {'DsgPrs_AS_NONE': (<DsgPrs_ArrowSide.DsgPrs_AS_NONE: 0>, None), 'DsgPrs_AS_FIRSTAR': (<DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR: 1>, None), 'DsgPrs_AS_LASTAR': (<DsgPrs_ArrowSide.DsgPrs_AS_LASTAR: 2>, None), 'DsgPrs_AS_BOTHAR': (<DsgPrs_ArrowSide.DsgPrs_AS_BOTHAR: 3>, None), 'DsgPrs_AS_FIRSTPT': (<DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT: 4>, None), 'DsgPrs_AS_LASTPT': (<DsgPrs_ArrowSide.DsgPrs_AS_LASTPT: 5>, None), 'DsgPrs_AS_BOTHPT': (<DsgPrs_ArrowSide.DsgPrs_AS_BOTHPT: 6>, None), 'DsgPrs_AS_FIRSTAR_LASTPT': (<DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR_LASTPT: 7>, None), 'DsgPrs_AS_FIRSTPT_LASTAR': (<DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT_LASTAR: 8>, None)}
    __members__: dict # value = {'DsgPrs_AS_NONE': <DsgPrs_ArrowSide.DsgPrs_AS_NONE: 0>, 'DsgPrs_AS_FIRSTAR': <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR: 1>, 'DsgPrs_AS_LASTAR': <DsgPrs_ArrowSide.DsgPrs_AS_LASTAR: 2>, 'DsgPrs_AS_BOTHAR': <DsgPrs_ArrowSide.DsgPrs_AS_BOTHAR: 3>, 'DsgPrs_AS_FIRSTPT': <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT: 4>, 'DsgPrs_AS_LASTPT': <DsgPrs_ArrowSide.DsgPrs_AS_LASTPT: 5>, 'DsgPrs_AS_BOTHPT': <DsgPrs_ArrowSide.DsgPrs_AS_BOTHPT: 6>, 'DsgPrs_AS_FIRSTAR_LASTPT': <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR_LASTPT: 7>, 'DsgPrs_AS_FIRSTPT_LASTAR': <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT_LASTAR: 8>}
    pass
class DsgPrs_Chamf2dPresentation():
    """
    Framework for display of 2D chamfers.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aPntAttach : OCP.gp.gp_Pnt,aPntEnd : OCP.gp.gp_Pnt,aText : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Defines the display of elements showing 2D chamfers on shapes. These include the text aText, the point of attachment, aPntAttach and the end point aPntEnd. These arguments are added to the presentation object aPresentation. Their display attributes are defined by the attribute manager aDrawer.

        Defines the display of texts, symbols and icons used to present 2D chamfers. These include the text aText, the point of attachment, aPntAttach and the end point aPntEnd. These arguments are added to the presentation object aPresentation. Their display attributes are defined by the attribute manager aDrawer. The arrow at the point of attachment has a display defined by a value of the enumeration DsgPrs_Arrowside.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aPntAttach : OCP.gp.gp_Pnt,aPntEnd : OCP.gp.gp_Pnt,aText : OCP.TCollection.TCollection_ExtendedString,ArrowSide : DsgPrs_ArrowSide) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_ConcentricPresentation():
    """
    A framework to define display of relations of concentricity.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aCenter : OCP.gp.gp_Pnt,aRadius : float,aNorm : OCP.gp.gp_Dir,aPoint : OCP.gp.gp_Pnt) -> None: 
        """
        Defines the display of elements showing relations of concentricity between shapes. These include the center aCenter, the radius aRadius, the direction aNorm and the point aPoint. These arguments are added to the presentation object aPresentation. Their display attributes are defined by the attribute manager aDrawer.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_DatumPrs(OCP.Prs3d.Prs3d_Root):
    """
    A framework for displaying an XYZ trihedron.
    """
    @staticmethod
    def Add_s(thePresentation : OCP.Graphic3d.Graphic3d_Structure,theDatum : OCP.gp.gp_Ax2,theDrawer : OCP.Prs3d.Prs3d_Drawer) -> None: 
        """
        Draw XYZ axes at specified location with attributes defined by the attribute manager theDrawer: - Prs3d_DatumAspect defines arrow, line and lenght trihedron axis parameters, - Prs3d_TextAspect defines displayed text. The thihedron origin and axis directions are defined by theDatum coordinate system. DsgPrs_XYZAxisPresentation framework is used to create graphical primitives for each axis. Axes are marked with "X", "Y", "Z" text.
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
class DsgPrs_DiameterPresentation():
    """
    A framework for displaying diameters in shapes.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint : OCP.gp.gp_Pnt,aCircle : OCP.gp.gp_Circ,uFirst : float,uLast : float,ArrowSide : DsgPrs_ArrowSide,IsDiamSymbol : bool) -> None: 
        """
        Draws the diameter of the circle aCircle displayed in the presentation aPresentation and with attributes defined by the attribute manager aDrawer. The point AttachmentPoint defines the point of contact between the circle and the diameter presentation. The value of the enumeration ArrowSide controls whether arrows will be displayed at either or both ends of the length. The text aText labels the diameter.

        Draws the diameter of the arc anArc displayed in the presentation aPresentation and with attributes defined by the attribute manager aDrawer. The point AttachmentPoint defines the point of contact between the arc and the diameter presentation. The value of the enumeration ArrowSide controls whether arrows will be displayed at either or both ends of the length. The parameters uFirst and uLast define the first and last points of the arc. The text aText labels the diameter.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint : OCP.gp.gp_Pnt,aCircle : OCP.gp.gp_Circ,ArrowSide : DsgPrs_ArrowSide,IsDiamSymbol : bool) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_EllipseRadiusPresentation():
    """
    None
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theval : float,aText : OCP.TCollection.TCollection_ExtendedString,anEllipse : OCP.gp.gp_Elips,AttachmentPoint : OCP.gp.gp_Pnt,anEndOfArrow : OCP.gp.gp_Pnt,aCenter : OCP.gp.gp_Pnt,uFirst : float,IsInDomain : bool,IsMaxRadius : bool,ArrowSide : DsgPrs_ArrowSide) -> None: 
        """
        draws a Radius (Major or Minor) representation for whole ellipse case

        draws a Radius (Major or Minor) representation for arc of an ellipse case

        draws a Radius (Major or Minor) representation for arc of an offset curve from ellipse
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theval : float,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint : OCP.gp.gp_Pnt,anEndOfArrow : OCP.gp.gp_Pnt,aCenter : OCP.gp.gp_Pnt,IsMaxRadius : bool,ArrowSide : DsgPrs_ArrowSide) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theval : float,aText : OCP.TCollection.TCollection_ExtendedString,aCurve : OCP.Geom.Geom_OffsetCurve,AttachmentPoint : OCP.gp.gp_Pnt,anEndOfArrow : OCP.gp.gp_Pnt,aCenter : OCP.gp.gp_Pnt,uFirst : float,IsInDomain : bool,IsMaxRadius : bool,ArrowSide : DsgPrs_ArrowSide) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_EqualDistancePresentation():
    """
    A framework to display equal distances between shapes and a given plane. The distance is the length of a projection from the shape to the plane. These distances are used to compare two shapes by this vector alone.
    """
    @staticmethod
    def AddIntervalBetweenTwoArcs_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aCircle1 : OCP.gp.gp_Circ,aCircle2 : OCP.gp.gp_Circ,aPoint1 : OCP.gp.gp_Pnt,aPoint2 : OCP.gp.gp_Pnt,aPoint3 : OCP.gp.gp_Pnt,aPoint4 : OCP.gp.gp_Pnt,anArrowSide : DsgPrs_ArrowSide) -> None: 
        """
        is used for presentation of interval between two arcs. One of arcs can have a zero radius.
        """
    @staticmethod
    def AddInterval_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aPoint1 : OCP.gp.gp_Pnt,aPoint2 : OCP.gp.gp_Pnt,aDir : OCP.gp.gp_Dir,aPosition : OCP.gp.gp_Pnt,anArrowSide : DsgPrs_ArrowSide,anExtremePnt1 : OCP.gp.gp_Pnt,anExtremePnt2 : OCP.gp.gp_Pnt) -> None: 
        """
        is used for presentation of interval between two lines or two points or between a line and a point.
        """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,Point1 : OCP.gp.gp_Pnt,Point2 : OCP.gp.gp_Pnt,Point3 : OCP.gp.gp_Pnt,Point4 : OCP.gp.gp_Pnt,Plane : OCP.Geom.Geom_Plane) -> None: 
        """
        Adds the points Point1, Point2, Point3 Point4, and the plane Plane to the presentation object aPresentation. The display attributes of these elements is defined by the attribute manager aDrawer. The distance is the length of a projection from the shape to the plane. These distances are used to compare two shapes by this vector alone.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_EqualRadiusPresentation():
    """
    A framework to define display of equality in radii.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,FirstCenter : OCP.gp.gp_Pnt,SecondCenter : OCP.gp.gp_Pnt,FirstPoint : OCP.gp.gp_Pnt,SecondPoint : OCP.gp.gp_Pnt,Plane : OCP.Geom.Geom_Plane) -> None: 
        """
        Adds the points FirstCenter, SecondCenter, FirstPoint, SecondPoint, and the plane Plane to the presentation object aPresentation. The display attributes of these elements is defined by the attribute manager aDrawer. FirstCenter and SecondCenter are the centers of the first and second shapes respectively, and FirstPoint and SecondPoint are the attachment points of the radii to arcs.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_FilletRadiusPresentation():
    """
    A framework for displaying radii of fillets.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,thevalue : float,aText : OCP.TCollection.TCollection_ExtendedString,aPosition : OCP.gp.gp_Pnt,aNormalDir : OCP.gp.gp_Dir,aBasePnt : OCP.gp.gp_Pnt,aFirstPoint : OCP.gp.gp_Pnt,aSecondPoint : OCP.gp.gp_Pnt,aCenter : OCP.gp.gp_Pnt,ArrowPrs : DsgPrs_ArrowSide,drawRevers : bool,DrawPosition : OCP.gp.gp_Pnt,EndOfArrow : OCP.gp.gp_Pnt,TrimCurve : OCP.Geom.Geom_TrimmedCurve) -> Tuple[bool]: 
        """
        Adds a display of the radius of a fillet to the presentation aPresentation. The display ttributes defined by the attribute manager aDrawer. the value specifies the length of the radius.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_FixPresentation():
    """
    class which draws the presentation of Fixed objects
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aPntAttach : OCP.gp.gp_Pnt,aPntEnd : OCP.gp.gp_Pnt,aNormPln : OCP.gp.gp_Dir,aSymbSize : float) -> None: 
        """
        draws the presentation of fixed objects by drawing the 'fix' symbol at position <aPntEnd>. A binding segment is drawn between <aPntAttach> ( which belongs the the fix object) and <aPntEnd>. aSymbSize is the size of the 'fix'symbol
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_IdenticPresentation():
    """
    None
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,aPntAttach : OCP.gp.gp_Pnt,aPntOffset : OCP.gp.gp_Pnt) -> None: 
        """
        draws a line between <aPntAttach> and <aPntOffset>.

        draws the 'identic' presentation by drawing a line between <aFAttach> and <aSAttach> , and a linkimg segment between <aPntOffset> and its projection on the precedent line.

        draws the 'identic' presentation in the case of circles : draws an arc of circle between <aFAttach> and <aSAttach> of center <aCenter> and of radius dist(aCenter, aFAttach), and draws a segment between <aPntOffset> and its projection on the arc.

        draws the 'identic' presentation in the case of circles : draws an arc of circle between <aFAttach> and <aSAttach> of center <aCenter> and of radius dist(aCenter, aFAttach), and draws a segment between <aPntOffset> and <aPntOnCirc>

        draws the 'identic' presentation in the case of ellipses: draws an arc of the anEllipse between <aFAttach> and <aSAttach> and draws a segment between <aPntOffset> and <aPntOnElli>
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,anEllipse : OCP.gp.gp_Elips,aFAttach : OCP.gp.gp_Pnt,aSAttach : OCP.gp.gp_Pnt,aPntOffset : OCP.gp.gp_Pnt,aPntOnElli : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,aAx2 : OCP.gp.gp_Ax2,aCenter : OCP.gp.gp_Pnt,aFAttach : OCP.gp.gp_Pnt,aSAttach : OCP.gp.gp_Pnt,aPntOffset : OCP.gp.gp_Pnt,aPntOnCirc : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,aFAttach : OCP.gp.gp_Pnt,aSAttach : OCP.gp.gp_Pnt,aPntOffset : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,aAx2 : OCP.gp.gp_Ax2,aCenter : OCP.gp.gp_Pnt,aFAttach : OCP.gp.gp_Pnt,aSAttach : OCP.gp.gp_Pnt,aPntOffset : OCP.gp.gp_Pnt) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_LengthPresentation():
    """
    Framework for displaying lengths. The length displayed is indicated by line segments and text alone or by a combination of line segment, text and arrows at either or both of its ends.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,Pt1 : OCP.gp.gp_Pnt,Pt2 : OCP.gp.gp_Pnt,ArrowSide : DsgPrs_ArrowSide) -> None: 
        """
        Draws a line segment representing a length in the display aPresentation. This segment joins the points AttachmentPoint1 and AttachmentPoint2, along the direction aDirection. The text aText will be displayed at the offset point OffsetPoint. The line and text attributes are specified by the attribute manager aDrawer.

        Draws a line segment representing a length in the display aPresentation. This segment joins the points AttachmentPoint1 and AttachmentPoint2, along the direction aDirection. The text aText will be displayed at the offset point OffsetPoint. The value of the enumeration ArrowSide controls whether arrows will be displayed at either or both ends of the length. The line, text and arrow attributes are specified by the attribute manager aDrawer.

        Draws a line segment representing a length in the display aPresentation. This segment joins the points AttachmentPoint1 and AttachmentPoint2, along the direction aDirection. The text aText will be displayed at the offset point OffsetPoint. The value of the enumeration ArrowSide controls whether arrows will be displayed at either or both ends of the length. The plane PlaneOfFaces is used if length is null. The line, text and arrow attributes are specified by the attribute manager aDrawer.

        Draws a line segment representing a length in the display aPresentation. This segment joins the points AttachmentPoint1 and AttachmentPoint2, along the direction aDirection. AttachmentPoint2 lies on the curvilinear faces SecondSurf. The text aText will be displayed at the offset point OffsetPoint. The value of the enumeration ArrowSide controls whether arrows will be displayed at either or both ends of the length. The line, text and arrow attributes are specified by the attribute manager aDrawer.

        Draws a line segment representing a length in the display aPresentation. This segment joins the points AttachmentPoint1 and AttachmentPoint2, along the direction aDirection. The value of the enumeration ArrowSide controls whether arrows will be displayed at either or both ends of the length. The line and arrow attributes are specified by the attribute manager aDrawer.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,PlaneOfFaces : OCP.gp.gp_Pln,aDirection : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt,ArrowSide : DsgPrs_ArrowSide) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aDirection : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,SecondSurf : OCP.Geom.Geom_Surface,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aDirection : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt,ArrowSide : DsgPrs_ArrowSide) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aDirection : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt,ArrowSide : DsgPrs_ArrowSide) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_MidPointPresentation():
    """
    None
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,anElips : OCP.gp.gp_Elips,MidPoint : OCP.gp.gp_Pnt,Position : OCP.gp.gp_Pnt,AttachPoint : OCP.gp.gp_Pnt,Point1 : OCP.gp.gp_Pnt,Point2 : OCP.gp.gp_Pnt,first : bool) -> None: 
        """
        draws the representation of a MidPoint between two vertices.

        draws the representation of a MidPoint between two lines or linear segments.

        draws the representation of a MidPoint between two entire circles or two circular arcs.

        draws the representation of a MidPoint between two entire ellipses or two elliptic arcs.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theAxe : OCP.gp.gp_Ax2,MidPoint : OCP.gp.gp_Pnt,Position : OCP.gp.gp_Pnt,AttachPoint : OCP.gp.gp_Pnt,Point1 : OCP.gp.gp_Pnt,Point2 : OCP.gp.gp_Pnt,first : bool) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aCircle : OCP.gp.gp_Circ,MidPoint : OCP.gp.gp_Pnt,Position : OCP.gp.gp_Pnt,AttachPoint : OCP.gp.gp_Pnt,Point1 : OCP.gp.gp_Pnt,Point2 : OCP.gp.gp_Pnt,first : bool) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,theAxe : OCP.gp.gp_Ax2,MidPoint : OCP.gp.gp_Pnt,Position : OCP.gp.gp_Pnt,AttachPoint : OCP.gp.gp_Pnt,first : bool) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_OffsetPresentation():
    """
    A framework to define display of offsets.
    """
    @staticmethod
    def AddAxes_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aDirection : OCP.gp.gp_Dir,aDirection2 : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt) -> None: 
        """
        draws the representation of axes alignement Constraint between the point AttachmentPoint1 and the point AttachmentPoint2, along direction aDirection, using the offset point OffsetPoint.
        """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aDirection : OCP.gp.gp_Dir,aDirection2 : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt) -> None: 
        """
        Defines the display of elements showing offset shapes. These include the two points of attachment AttachmentPoint1 and AttachmentPoint1, the two directions aDirection and aDirection2, and the offset point OffsetPoint. These arguments are added to the presentation object aPresentation. Their display attributes are defined by the attribute manager aDrawer.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_ParalPresentation():
    """
    A framework to define display of relations of parallelism between shapes.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aDirection : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt,ArrowSide : DsgPrs_ArrowSide) -> None: 
        """
        Defines the display of elements showing relations of parallelism between shapes. These include the two points of attachment AttachmentPoint1 and AttachmentPoint1, the direction aDirection, and the offset point OffsetPoint. These arguments are added to the presentation object aPresentation. Their display attributes are defined by the attribute manager aDrawer.

        Defines the display of elements showing relations of parallelism between shapes. These include the two points of attachment AttachmentPoint1 and AttachmentPoint1, the direction aDirection, the offset point OffsetPoint and the text aText. These arguments are added to the presentation object aPresentation. Their display attributes are defined by the attribute manager aDrawer.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aDirection : OCP.gp.gp_Dir,OffsetPoint : OCP.gp.gp_Pnt) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_PerpenPresentation():
    """
    A framework to define display of perpendicular constraints between shapes.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,pAx1 : OCP.gp.gp_Pnt,pAx2 : OCP.gp.gp_Pnt,pnt1 : OCP.gp.gp_Pnt,pnt2 : OCP.gp.gp_Pnt,OffsetPoint : OCP.gp.gp_Pnt,intOut1 : bool,intOut2 : bool) -> None: 
        """
        Defines the display of elements showing perpendicular constraints between shapes. These include the two axis points pAx1 and pAx2, the two points pnt1 and pnt2, the offset point OffsetPoint and the two Booleans intOut1} and intOut2{. These arguments are added to the presentation object aPresentation. Their display attributes are defined by the attribute manager aDrawer.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_RadiusPresentation():
    """
    A framework to define display of radii.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint : OCP.gp.gp_Pnt,Center : OCP.gp.gp_Pnt,EndOfArrow : OCP.gp.gp_Pnt,ArrowSide : DsgPrs_ArrowSide,drawFromCenter : bool=True,reverseArrow : bool=False) -> None: 
        """
        Adds the point AttachmentPoint, the circle aCircle, the text aText, and the parameters firstparam and lastparam to the presentation object aPresentation. The display attributes of these elements is defined by the attribute manager aDrawer. If the Boolean drawFromCenter is false, the arrowhead will point towards the center of aCircle. If the Boolean reverseArrow is true, the arrowhead will point away from the attachment point.

        Adds the circle aCircle, the text aText, the points AttachmentPoint, Center and EndOfArrow to the presentation object aPresentation. The display attributes of these elements is defined by the attribute manager aDrawer. The value of the enumeration Arrowside determines the type of arrow displayed: whether there will be arrowheads at both ends or only one, for example. If the Boolean drawFromCenter is false, the arrowhead will point towards the center of aCircle. If the Boolean reverseArrow is true, the arrowhead will point away from the attachment point.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,AttachmentPoint : OCP.gp.gp_Pnt,aCircle : OCP.gp.gp_Circ,firstparam : float,lastparam : float,drawFromCenter : bool=True,reverseArrow : bool=False) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_ShadedPlanePresentation():
    """
    A framework to define display of shaded planes.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aPt1 : OCP.gp.gp_Pnt,aPt2 : OCP.gp.gp_Pnt,aPt3 : OCP.gp.gp_Pnt) -> None: 
        """
        Adds the points aPt1, aPt2 and aPt3 to the presentation object, aPresentation. The display attributes of the shaded plane are defined by the attribute manager aDrawer.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_ShapeDirPresentation():
    """
    A framework to define display of the normal to the surface of a shape.
    """
    @staticmethod
    def Add_s(prs : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,shape : OCP.TopoDS.TopoDS_Shape,mode : int) -> None: 
        """
        Adds the shape shape and the mode mode to the presentation object prs. The display attributes of the normal are defined by the attribute manager aDrawer. mode determines whether the first or the last point of the normal is given to the presentation object. If the first point: 0; if the last point, 1.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_SymbPresentation():
    """
    A framework to define display of symbols.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aText : OCP.TCollection.TCollection_ExtendedString,OffsetPoint : OCP.gp.gp_Pnt) -> None: 
        """
        Adds the text aText and the point OffsetPoint to the presentation object aPresentation. The display attributes of the shaded plane are defined by the attribute manager aDrawer.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_SymmetricPresentation():
    """
    A framework to define display of symmetry between shapes.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aDirection1 : OCP.gp.gp_Dir,aAxis : OCP.gp.gp_Lin,OffsetPoint : OCP.gp.gp_Pnt) -> None: 
        """
        Adds the points OffsetPoint, AttachmentPoint1, AttachmentPoint2, the direction aDirection1 and the axis anAxis to the presentation object aPresentation. The display attributes of the symmetry are defined by the attribute manager aDrawer. This syntax is used for display of symmetries between two segments.

        Adds the points OffsetPoint, AttachmentPoint1, AttachmentPoint2, the direction aDirection1 the circle aCircle1 and the axis anAxis to the presentation object aPresentation. The display attributes of the symmetry are defined by the attribute manager aDrawer. This syntax is used for display of symmetries between two arcs.

        Adds the points OffsetPoint, AttachmentPoint1, AttachmentPoint2 and the axis anAxis to the presentation object aPresentation. The display attributes of the symmetry are defined by the attribute manager aDrawer. This syntax is used for display of symmetries between two vertices.
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aCircle1 : OCP.gp.gp_Circ,aAxis : OCP.gp.gp_Lin,OffsetPoint : OCP.gp.gp_Pnt) -> None: ...
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,AttachmentPoint1 : OCP.gp.gp_Pnt,AttachmentPoint2 : OCP.gp.gp_Pnt,aAxis : OCP.gp.gp_Lin,OffsetPoint : OCP.gp.gp_Pnt) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_TangentPresentation():
    """
    A framework to define display of tangents.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,OffsetPoint : OCP.gp.gp_Pnt,aDirection : OCP.gp.gp_Dir,aLength : float) -> None: 
        """
        Adds the point OffsetPoint, the direction aDirection and the length aLength to the presentation object aPresentation. The display attributes of the tangent are defined by the attribute manager aDrawer.
        """
    def __init__(self) -> None: ...
    pass
class DsgPrs_XYZAxisPresentation():
    """
    A framework for displaying the axes of an XYZ trihedron.
    """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aLineAspect : OCP.Prs3d.Prs3d_LineAspect,anArrowAspect : OCP.Prs3d.Prs3d_ArrowAspect,aTextAspect : OCP.Prs3d.Prs3d_TextAspect,aDir : OCP.gp.gp_Dir,aVal : float,aText : str,aPfirst : OCP.gp.gp_Pnt,aPlast : OCP.gp.gp_Pnt) -> None: 
        """
        Draws each axis of a trihedron displayed in the presentation aPresentation and with lines shown by the values of aLineAspect. Each axis is defined by: - the first and last points aPfirst and aPlast - the direction aDir and - the value aVal which provides a value for length. The value for length is provided so that the trihedron can vary in length relative to the scale of shape display. Each axis will be identified as X, Y, or Z by the text aText.

        draws the presentation X ,Y ,Z axis
        """
    @staticmethod
    @overload
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,anLineAspect : OCP.Prs3d.Prs3d_LineAspect,aDir : OCP.gp.gp_Dir,aVal : float,aText : str,aPfirst : OCP.gp.gp_Pnt,aPlast : OCP.gp.gp_Pnt) -> None: ...
    def __init__(self) -> None: ...
    pass
class DsgPrs_XYZPlanePresentation():
    """
    A framework for displaying the planes of an XYZ trihedron.
    """
    @staticmethod
    def Add_s(aPresentation : OCP.Graphic3d.Graphic3d_Structure,aDrawer : OCP.Prs3d.Prs3d_Drawer,aPt1 : OCP.gp.gp_Pnt,aPt2 : OCP.gp.gp_Pnt,aPt3 : OCP.gp.gp_Pnt) -> None: 
        """
        Draws each plane of a trihedron displayed in the presentation aPresentation and with attributes defined by the attribute manager aDrawer. Each triangular plane is defined by the points aPt1 aPt2 and aPt3.
        """
    def __init__(self) -> None: ...
    pass
DsgPrs_AS_BOTHAR: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_BOTHAR: 3>
DsgPrs_AS_BOTHPT: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_BOTHPT: 6>
DsgPrs_AS_FIRSTAR: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR: 1>
DsgPrs_AS_FIRSTAR_LASTPT: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTAR_LASTPT: 7>
DsgPrs_AS_FIRSTPT: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT: 4>
DsgPrs_AS_FIRSTPT_LASTAR: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_FIRSTPT_LASTAR: 8>
DsgPrs_AS_LASTAR: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_LASTAR: 2>
DsgPrs_AS_LASTPT: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_LASTPT: 5>
DsgPrs_AS_NONE: OCP.DsgPrs.DsgPrs_ArrowSide # value = <DsgPrs_ArrowSide.DsgPrs_AS_NONE: 0>
