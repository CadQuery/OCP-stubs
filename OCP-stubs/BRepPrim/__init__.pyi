import OCP.BRepPrim
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.BRep
import OCP.Geom
import OCP.TopoDS
import OCP.Geom2d
__all__  = [
"BRepPrim_Builder",
"BRepPrim_OneAxis",
"BRepPrim_Revolution",
"BRepPrim_Direction",
"BRepPrim_FaceBuilder",
"BRepPrim_GWedge",
"BRepPrim_Cone",
"BRepPrim_Cylinder",
"BRepPrim_Sphere",
"BRepPrim_Torus",
"BRepPrim_Wedge",
"BRepPrim_XMax",
"BRepPrim_XMin",
"BRepPrim_YMax",
"BRepPrim_YMin",
"BRepPrim_ZMax",
"BRepPrim_ZMin"
]
class BRepPrim_Builder():
    """
    implements the abstract Builder with the BRep Builder
    """
    @overload
    def AddEdgeVertex(self,E : OCP.TopoDS.TopoDS_Edge,V : OCP.TopoDS.TopoDS_Vertex,P : float,direct : bool) -> None: 
        """
        Adds the Vertex <V> in the Edge <E>. <P> is the parameter of the vertex on the edge. If direct is False the Vertex is reversed.

        Adds the Vertex <V> in the Edge <E>. <P1,P2> are the parameters of the vertex on the closed edge.
        """
    @overload
    def AddEdgeVertex(self,E : OCP.TopoDS.TopoDS_Edge,V : OCP.TopoDS.TopoDS_Vertex,P1 : float,P2 : float) -> None: ...
    def AddFaceWire(self,F : OCP.TopoDS.TopoDS_Face,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Adds the Wire <W> in the Face <F>.
        """
    def AddShellFace(self,Sh : OCP.TopoDS.TopoDS_Shell,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Adds the Face <F> in the Shell <Sh>.
        """
    def AddWireEdge(self,W : OCP.TopoDS.TopoDS_Wire,E : OCP.TopoDS.TopoDS_Edge,direct : bool) -> None: 
        """
        Adds the Edge <E> in the Wire <W>, if direct is False the Edge is reversed.
        """
    def Builder(self) -> OCP.BRep.BRep_Builder: 
        """
        None

        None
        """
    def CompleteEdge(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        This is called once an edge is completed. It gives the opportunity to perform any post treatment.
        """
    def CompleteFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        This is called once a face is completed. It gives the opportunity to perform any post treatment.
        """
    def CompleteShell(self,S : OCP.TopoDS.TopoDS_Shell) -> None: 
        """
        This is called once a shell is completed. It gives the opportunity to perform any post treatment.
        """
    def CompleteWire(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        This is called once a wire is completed. It gives the opportunity to perform any post treatment.
        """
    def MakeDegeneratedEdge(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Returns in <E> a degenerated edge.
        """
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.gp.gp_Circ) -> None: 
        """
        Returns in <E> an Edge built with the line equation <L>.

        Returns in <E> an Edge built with the circle equation <C>.
        """
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge,L : OCP.gp.gp_Lin) -> None: ...
    def MakeFace(self,F : OCP.TopoDS.TopoDS_Face,P : OCP.gp.gp_Pln) -> None: 
        """
        Returns in <F> a Face built with the plane equation <P>. Used by all primitives.
        """
    def MakeShell(self,S : OCP.TopoDS.TopoDS_Shell) -> None: 
        """
        Make a empty Shell.
        """
    def MakeVertex(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt) -> None: 
        """
        Returns in <V> a Vertex built with the point <P>.
        """
    def MakeWire(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Returns in <W> an empty Wire.
        """
    def ReverseFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Reverses the Face <F>.
        """
    @overload
    def SetPCurve(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,L : OCP.gp.gp_Lin2d) -> None: 
        """
        Sets the line <L> to be the curve representing the edge <E> in the parametric space of the surface of <F>.

        Sets the lines <L1,L2> to be the curves representing the edge <E> in the parametric space of the closed surface of <F>.

        Sets the circle <C> to be the curve representing the edge <E> in the parametric space of the surface of <F>.
        """
    @overload
    def SetPCurve(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,C : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def SetPCurve(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,L1 : OCP.gp.gp_Lin2d,L2 : OCP.gp.gp_Lin2d) -> None: ...
    def SetParameters(self,E : OCP.TopoDS.TopoDS_Edge,V : OCP.TopoDS.TopoDS_Vertex,P1 : float,P2 : float) -> None: 
        """
        <P1,P2> are the parameters of the vertex on the edge. The edge is a closed curve.
        """
    @overload
    def __init__(self,B : OCP.BRep.BRep_Builder) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepPrim_OneAxis():
    """
    Algorithm to build primitives with one axis of revolution.
    """
    @overload
    def Angle(self,A : float) -> None: 
        """
        None

        None
        """
    @overload
    def Angle(self) -> float: ...
    @overload
    def Axes(self,A : OCP.gp.gp_Ax2) -> None: 
        """
        None

        Returns the Ax2 from <me>.
        """
    @overload
    def Axes(self) -> OCP.gp.gp_Ax2: ...
    def AxisBottomVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Bottom altitude on the axis.
        """
    def AxisEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge built along the Axis and oriented on +Z of the Axis.
        """
    def AxisEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face with the AxisEdge.
        """
    def AxisStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face with the AxisEdge.
        """
    def AxisTopVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Top altitude on the axis.
        """
    def BottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMin. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def BottomEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def BottomFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Bottom planar Face. It is Oriented toward the -Z axis (outside).
        """
    def BottomStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMin)
        """
    def BottomWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the bottom face.
        """
    def EndBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and bottom Face.
        """
    def EndEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle Angle. If !HasSides() the StartEdge and the EndEdge are the same edge.
        """
    def EndFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face ending the slice, it is oriented toward the exterior of the primitive.
        """
    def EndTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and top Face.
        """
    def EndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face.
        """
    def HasBottom(self) -> bool: 
        """
        Returns True if there is a bottom face.
        """
    def HasSides(self) -> bool: 
        """
        Returns True if there are Start and End faces.
        """
    def HasTop(self) -> bool: 
        """
        Returns True if there is a top face.
        """
    def LateralEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire with in lateral face with the end edge.
        """
    def LateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral Face. It is oriented toward the outside of the primitive.
        """
    def LateralStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face with the start edge.
        """
    def LateralWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face.
        """
    def MakeEmptyLateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns a face with no edges. The surface is the lateral surface with normals pointing outward. The U parameter is the angle with the origin on the X axis. The V parameter is the parameter of the meridian.
        """
    def MakeEmptyMeridianEdge(self,Ang : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns an edge with a 3D curve made from the meridian in the XZ plane rotated by <Ang> around the Z-axis. Ang may be 0 or myAngle.
        """
    def MeridianClosed(self) -> bool: 
        """
        Returns True if the meridian is closed. Default implementation is MeridianValue(VMin).IsEqual(MeridianValue(VMax), Precision::Confusion())
        """
    def MeridianOnAxis(self,V : float) -> bool: 
        """
        Returns True if the point of parameter <V> on the meridian is on the Axis. Default implementation is Abs(MeridianValue(V).X()) < Precision::Confusion()
        """
    def MeridianValue(self,V : float) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the meridian point at parameter <V> in the plane XZ.
        """
    def SetMeridianOffset(self,MeridianOffset : float=0.0) -> None: 
        """
        The MeridianOffset is added to the parameters on the meridian curve and to the V values of the pcurves. This is used for the sphere for example, to give a range on the meridian edge which is not VMin, VMax.
        """
    def SetMeridianPCurve(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the parametric curve of the edge <E> in the face <F> to be the 2d representation of the meridian.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the Shell containing all the Faces of the primitive.
        """
    def StartBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and bottom Face.
        """
    def StartEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle 0.
        """
    def StartFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face starting the slice, it is oriented toward the exterior of the primitive.
        """
    def StartTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and top Face.
        """
    def StartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face.
        """
    def TopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMax. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def TopEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def TopFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the top planar Face. It is Oriented toward the +Z axis (outside).
        """
    def TopStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMax)
        """
    def TopWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the top face.
        """
    @overload
    def VMax(self) -> float: 
        """
        None

        None
        """
    @overload
    def VMax(self,V : float) -> None: ...
    def VMaxInfinite(self) -> bool: 
        """
        Returns True if VMax is infinite. Default Precision::IsPositiveInfinite(VMax);
        """
    @overload
    def VMin(self,V : float) -> None: 
        """
        None

        None
        """
    @overload
    def VMin(self) -> float: ...
    def VMinInfinite(self) -> bool: 
        """
        Returns True if VMin is infinite. Default Precision::IsNegativeInfinite(VMax);
        """
    pass
class BRepPrim_Revolution(BRepPrim_OneAxis):
    """
    Implement the OneAxis algoritm for a revolution surface.
    """
    @overload
    def Angle(self,A : float) -> None: 
        """
        None

        None
        """
    @overload
    def Angle(self) -> float: ...
    @overload
    def Axes(self,A : OCP.gp.gp_Ax2) -> None: 
        """
        None

        Returns the Ax2 from <me>.
        """
    @overload
    def Axes(self) -> OCP.gp.gp_Ax2: ...
    def AxisBottomVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Bottom altitude on the axis.
        """
    def AxisEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge built along the Axis and oriented on +Z of the Axis.
        """
    def AxisEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face with the AxisEdge.
        """
    def AxisStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face with the AxisEdge.
        """
    def AxisTopVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Top altitude on the axis.
        """
    def BottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMin. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def BottomEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def BottomFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Bottom planar Face. It is Oriented toward the -Z axis (outside).
        """
    def BottomStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMin)
        """
    def BottomWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the bottom face.
        """
    def EndBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and bottom Face.
        """
    def EndEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle Angle. If !HasSides() the StartEdge and the EndEdge are the same edge.
        """
    def EndFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face ending the slice, it is oriented toward the exterior of the primitive.
        """
    def EndTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and top Face.
        """
    def EndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face.
        """
    def HasBottom(self) -> bool: 
        """
        Returns True if there is a bottom face.
        """
    def HasSides(self) -> bool: 
        """
        Returns True if there are Start and End faces.
        """
    def HasTop(self) -> bool: 
        """
        Returns True if there is a top face.
        """
    def LateralEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire with in lateral face with the end edge.
        """
    def LateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral Face. It is oriented toward the outside of the primitive.
        """
    def LateralStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face with the start edge.
        """
    def LateralWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face.
        """
    def MakeEmptyLateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        The surface normal should be directed towards the outside.
        """
    def MakeEmptyMeridianEdge(self,Ang : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns an edge with a 3D curve made from the meridian in the XZ plane rotated by <Ang> around the Z-axis. Ang may be 0 or myAngle.
        """
    def MeridianClosed(self) -> bool: 
        """
        Returns True if the meridian is closed. Default implementation is MeridianValue(VMin).IsEqual(MeridianValue(VMax), Precision::Confusion())
        """
    def MeridianOnAxis(self,V : float) -> bool: 
        """
        Returns True if the point of parameter <V> on the meridian is on the Axis. Default implementation is Abs(MeridianValue(V).X()) < Precision::Confusion()
        """
    def MeridianValue(self,V : float) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the meridian point at parameter <V> in the plane XZ.
        """
    def SetMeridianOffset(self,MeridianOffset : float=0.0) -> None: 
        """
        The MeridianOffset is added to the parameters on the meridian curve and to the V values of the pcurves. This is used for the sphere for example, to give a range on the meridian edge which is not VMin, VMax.
        """
    def SetMeridianPCurve(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the parametric urve of the edge <E> in the face <F> to be the 2d representation of the meridian.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the Shell containing all the Faces of the primitive.
        """
    def StartBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and bottom Face.
        """
    def StartEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle 0.
        """
    def StartFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face starting the slice, it is oriented toward the exterior of the primitive.
        """
    def StartTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and top Face.
        """
    def StartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face.
        """
    def TopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMax. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def TopEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def TopFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the top planar Face. It is Oriented toward the +Z axis (outside).
        """
    def TopStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMax)
        """
    def TopWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the top face.
        """
    @overload
    def VMax(self) -> float: 
        """
        None

        None
        """
    @overload
    def VMax(self,V : float) -> None: ...
    def VMaxInfinite(self) -> bool: 
        """
        Returns True if VMax is infinite. Default Precision::IsPositiveInfinite(VMax);
        """
    @overload
    def VMin(self,V : float) -> None: 
        """
        None

        None
        """
    @overload
    def VMin(self) -> float: ...
    def VMinInfinite(self) -> bool: 
        """
        Returns True if VMin is infinite. Default Precision::IsNegativeInfinite(VMax);
        """
    def __init__(self,A : OCP.gp.gp_Ax2,VMin : float,VMax : float,M : OCP.Geom.Geom_Curve,PM : OCP.Geom2d.Geom2d_Curve) -> None: ...
    pass
class BRepPrim_Direction():
    """
    None

    Members:

      BRepPrim_XMin

      BRepPrim_XMax

      BRepPrim_YMin

      BRepPrim_YMax

      BRepPrim_ZMin

      BRepPrim_ZMax
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
    BRepPrim_XMax: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_XMax: 1>
    BRepPrim_XMin: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_XMin: 0>
    BRepPrim_YMax: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_YMax: 3>
    BRepPrim_YMin: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_YMin: 2>
    BRepPrim_ZMax: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_ZMax: 5>
    BRepPrim_ZMin: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_ZMin: 4>
    __entries: dict # value = {'BRepPrim_XMin': (<BRepPrim_Direction.BRepPrim_XMin: 0>, None), 'BRepPrim_XMax': (<BRepPrim_Direction.BRepPrim_XMax: 1>, None), 'BRepPrim_YMin': (<BRepPrim_Direction.BRepPrim_YMin: 2>, None), 'BRepPrim_YMax': (<BRepPrim_Direction.BRepPrim_YMax: 3>, None), 'BRepPrim_ZMin': (<BRepPrim_Direction.BRepPrim_ZMin: 4>, None), 'BRepPrim_ZMax': (<BRepPrim_Direction.BRepPrim_ZMax: 5>, None)}
    __members__: dict # value = {'BRepPrim_XMin': <BRepPrim_Direction.BRepPrim_XMin: 0>, 'BRepPrim_XMax': <BRepPrim_Direction.BRepPrim_XMax: 1>, 'BRepPrim_YMin': <BRepPrim_Direction.BRepPrim_YMin: 2>, 'BRepPrim_YMax': <BRepPrim_Direction.BRepPrim_YMax: 3>, 'BRepPrim_ZMin': <BRepPrim_Direction.BRepPrim_ZMin: 4>, 'BRepPrim_ZMax': <BRepPrim_Direction.BRepPrim_ZMax: 5>}
    pass
class BRepPrim_FaceBuilder():
    """
    The FaceBuilder is an algorithm to build a BRep Face from a Geom Surface.
    """
    def Edge(self,I : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge of index <I> 1 - Edge VMin 2 - Edge UMax 3 - Edge VMax 4 - Edge UMin
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    @overload
    def Init(self,B : OCP.BRep.BRep_Builder,S : OCP.Geom.Geom_Surface,UMin : float,UMax : float,VMin : float,VMax : float) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,B : OCP.BRep.BRep_Builder,S : OCP.Geom.Geom_Surface) -> None: ...
    def Vertex(self,I : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex of index <I> 1 - Vertex UMin,VMin 2 - Vertex UMax,VMin 3 - Vertex UMax,VMax 4 - Vertex UMin,VMax
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,B : OCP.BRep.BRep_Builder,S : OCP.Geom.Geom_Surface,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,B : OCP.BRep.BRep_Builder,S : OCP.Geom.Geom_Surface) -> None: ...
    pass
class BRepPrim_GWedge():
    """
    A wedge is defined by :
    """
    def Axes(self) -> OCP.gp.gp_Ax2: 
        """
        Returns the coordinates system from <me>.
        """
    def Close(self,d1 : BRepPrim_Direction) -> None: 
        """
        Closes <me> in <d1> direction. A face and its edges or vertices are said existant.
        """
    def Edge(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge of <me> located in <d1><d2> direction.
        """
    def Face(self,d1 : BRepPrim_Direction) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face of <me> located in <d1> direction.
        """
    def GetX2Max(self) -> float: 
        """
        Returns X2Max value from <me>.
        """
    def GetX2Min(self) -> float: 
        """
        Returns X2Min value from <me>.
        """
    def GetXMax(self) -> float: 
        """
        Returns XMax value from <me>.
        """
    def GetXMin(self) -> float: 
        """
        Returns Xmin value from <me>.
        """
    def GetYMax(self) -> float: 
        """
        Returns YMax value from <me>.
        """
    def GetYMin(self) -> float: 
        """
        Returns YMin value from <me>.
        """
    def GetZ2Max(self) -> float: 
        """
        Returns Z2Max value from <me>.
        """
    def GetZ2Min(self) -> float: 
        """
        Returns Z2Min value from <me>.
        """
    def GetZMax(self) -> float: 
        """
        Returns ZMax value from <me>.
        """
    def GetZMin(self) -> float: 
        """
        Returns ZMin value from <me>.
        """
    def HasEdge(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> has an Edge in <d1><d2> direction.
        """
    def HasFace(self,d1 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> has a Face in <d1> direction.
        """
    def HasVertex(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction,d3 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> has a Vertex in <d1><d2><d3> direction.
        """
    def HasWire(self,d1 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> has a Wire in <d1> direction.
        """
    def IsDegeneratedShape(self) -> bool: 
        """
        Checkes a shape on degeneracy
        """
    def IsInfinite(self,d1 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> is open in <d1> direction.
        """
    def Line(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction) -> OCP.gp.gp_Lin: 
        """
        Returns the line of the Edge of <me> located in <d1><d2> direction.
        """
    def Open(self,d1 : BRepPrim_Direction) -> None: 
        """
        Opens <me> in <d1> direction. A face and its edges or vertices are said nonexistant.
        """
    def Plane(self,d1 : BRepPrim_Direction) -> OCP.gp.gp_Pln: 
        """
        Returns the plane of the Face of <me> located in <d1> direction.
        """
    def Point(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction,d3 : BRepPrim_Direction) -> OCP.gp.gp_Pnt: 
        """
        Returns the point of the Vertex of <me> located in <d1><d2><d3> direction.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the Shell containing the Faces of <me>.
        """
    def Vertex(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction,d3 : BRepPrim_Direction) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex of <me> located in <d1><d2><d3> direction.
        """
    def Wire(self,d1 : BRepPrim_Direction) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire of <me> located in <d1> direction.
        """
    @overload
    def __init__(self,B : BRepPrim_Builder,Axes : OCP.gp.gp_Ax2,dx : float,dy : float,dz : float) -> None: ...
    @overload
    def __init__(self,B : BRepPrim_Builder,Axes : OCP.gp.gp_Ax2,dx : float,dy : float,dz : float,ltx : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,B : BRepPrim_Builder,Axes : OCP.gp.gp_Ax2,xmin : float,ymin : float,zmin : float,z2min : float,x2min : float,xmax : float,ymax : float,zmax : float,z2max : float,x2max : float) -> None: ...
    pass
class BRepPrim_Cone(BRepPrim_Revolution, BRepPrim_OneAxis):
    """
    Implement the cone primitive.
    """
    @overload
    def Angle(self,A : float) -> None: 
        """
        None

        None
        """
    @overload
    def Angle(self) -> float: ...
    @overload
    def Axes(self,A : OCP.gp.gp_Ax2) -> None: 
        """
        None

        Returns the Ax2 from <me>.
        """
    @overload
    def Axes(self) -> OCP.gp.gp_Ax2: ...
    def AxisBottomVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Bottom altitude on the axis.
        """
    def AxisEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge built along the Axis and oriented on +Z of the Axis.
        """
    def AxisEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face with the AxisEdge.
        """
    def AxisStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face with the AxisEdge.
        """
    def AxisTopVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Top altitude on the axis.
        """
    def BottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMin. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def BottomEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def BottomFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Bottom planar Face. It is Oriented toward the -Z axis (outside).
        """
    def BottomStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMin)
        """
    def BottomWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the bottom face.
        """
    def EndBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and bottom Face.
        """
    def EndEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle Angle. If !HasSides() the StartEdge and the EndEdge are the same edge.
        """
    def EndFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face ending the slice, it is oriented toward the exterior of the primitive.
        """
    def EndTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and top Face.
        """
    def EndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face.
        """
    def HasBottom(self) -> bool: 
        """
        Returns True if there is a bottom face.
        """
    def HasSides(self) -> bool: 
        """
        Returns True if there are Start and End faces.
        """
    def HasTop(self) -> bool: 
        """
        Returns True if there is a top face.
        """
    def LateralEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire with in lateral face with the end edge.
        """
    def LateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral Face. It is oriented toward the outside of the primitive.
        """
    def LateralStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face with the start edge.
        """
    def LateralWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face.
        """
    def MakeEmptyLateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        The surface normal should be directed towards the outside.
        """
    def MakeEmptyMeridianEdge(self,Ang : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns an edge with a 3D curve made from the meridian in the XZ plane rotated by <Ang> around the Z-axis. Ang may be 0 or myAngle.
        """
    def MeridianClosed(self) -> bool: 
        """
        Returns True if the meridian is closed. Default implementation is MeridianValue(VMin).IsEqual(MeridianValue(VMax), Precision::Confusion())
        """
    def MeridianOnAxis(self,V : float) -> bool: 
        """
        Returns True if the point of parameter <V> on the meridian is on the Axis. Default implementation is Abs(MeridianValue(V).X()) < Precision::Confusion()
        """
    def MeridianValue(self,V : float) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the meridian point at parameter <V> in the plane XZ.
        """
    def SetMeridianOffset(self,MeridianOffset : float=0.0) -> None: 
        """
        The MeridianOffset is added to the parameters on the meridian curve and to the V values of the pcurves. This is used for the sphere for example, to give a range on the meridian edge which is not VMin, VMax.
        """
    def SetMeridianPCurve(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the parametric urve of the edge <E> in the face <F> to be the 2d representation of the meridian.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the Shell containing all the Faces of the primitive.
        """
    def StartBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and bottom Face.
        """
    def StartEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle 0.
        """
    def StartFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face starting the slice, it is oriented toward the exterior of the primitive.
        """
    def StartTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and top Face.
        """
    def StartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face.
        """
    def TopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMax. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def TopEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def TopFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the top planar Face. It is Oriented toward the +Z axis (outside).
        """
    def TopStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMax)
        """
    def TopWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the top face.
        """
    @overload
    def VMax(self) -> float: 
        """
        None

        None
        """
    @overload
    def VMax(self,V : float) -> None: ...
    def VMaxInfinite(self) -> bool: 
        """
        Returns True if VMax is infinite. Default Precision::IsPositiveInfinite(VMax);
        """
    @overload
    def VMin(self,V : float) -> None: 
        """
        None

        None
        """
    @overload
    def VMin(self) -> float: ...
    def VMinInfinite(self) -> bool: 
        """
        Returns True if VMin is infinite. Default Precision::IsNegativeInfinite(VMax);
        """
    @overload
    def __init__(self,R1 : float,R2 : float,H : float) -> None: ...
    @overload
    def __init__(self,Angle : float,Position : OCP.gp.gp_Ax2,Height : float,Radius : float=0.0) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,R1 : float,R2 : float,H : float) -> None: ...
    @overload
    def __init__(self,Angle : float) -> None: ...
    @overload
    def __init__(self,Angle : float,Axes : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,R1 : float,R2 : float,H : float) -> None: ...
    @overload
    def __init__(self,Angle : float,Apex : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepPrim_Cylinder(BRepPrim_Revolution, BRepPrim_OneAxis):
    """
    Cylinder primitive.
    """
    @overload
    def Angle(self,A : float) -> None: 
        """
        None

        None
        """
    @overload
    def Angle(self) -> float: ...
    @overload
    def Axes(self,A : OCP.gp.gp_Ax2) -> None: 
        """
        None

        Returns the Ax2 from <me>.
        """
    @overload
    def Axes(self) -> OCP.gp.gp_Ax2: ...
    def AxisBottomVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Bottom altitude on the axis.
        """
    def AxisEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge built along the Axis and oriented on +Z of the Axis.
        """
    def AxisEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face with the AxisEdge.
        """
    def AxisStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face with the AxisEdge.
        """
    def AxisTopVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Top altitude on the axis.
        """
    def BottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMin. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def BottomEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def BottomFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Bottom planar Face. It is Oriented toward the -Z axis (outside).
        """
    def BottomStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMin)
        """
    def BottomWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the bottom face.
        """
    def EndBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and bottom Face.
        """
    def EndEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle Angle. If !HasSides() the StartEdge and the EndEdge are the same edge.
        """
    def EndFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face ending the slice, it is oriented toward the exterior of the primitive.
        """
    def EndTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and top Face.
        """
    def EndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face.
        """
    def HasBottom(self) -> bool: 
        """
        Returns True if there is a bottom face.
        """
    def HasSides(self) -> bool: 
        """
        Returns True if there are Start and End faces.
        """
    def HasTop(self) -> bool: 
        """
        Returns True if there is a top face.
        """
    def LateralEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire with in lateral face with the end edge.
        """
    def LateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral Face. It is oriented toward the outside of the primitive.
        """
    def LateralStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face with the start edge.
        """
    def LateralWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face.
        """
    def MakeEmptyLateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        The surface normal should be directed towards the outside.
        """
    def MakeEmptyMeridianEdge(self,Ang : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns an edge with a 3D curve made from the meridian in the XZ plane rotated by <Ang> around the Z-axis. Ang may be 0 or myAngle.
        """
    def MeridianClosed(self) -> bool: 
        """
        Returns True if the meridian is closed. Default implementation is MeridianValue(VMin).IsEqual(MeridianValue(VMax), Precision::Confusion())
        """
    def MeridianOnAxis(self,V : float) -> bool: 
        """
        Returns True if the point of parameter <V> on the meridian is on the Axis. Default implementation is Abs(MeridianValue(V).X()) < Precision::Confusion()
        """
    def MeridianValue(self,V : float) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the meridian point at parameter <V> in the plane XZ.
        """
    def SetMeridianOffset(self,MeridianOffset : float=0.0) -> None: 
        """
        The MeridianOffset is added to the parameters on the meridian curve and to the V values of the pcurves. This is used for the sphere for example, to give a range on the meridian edge which is not VMin, VMax.
        """
    def SetMeridianPCurve(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the parametric urve of the edge <E> in the face <F> to be the 2d representation of the meridian.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the Shell containing all the Faces of the primitive.
        """
    def StartBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and bottom Face.
        """
    def StartEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle 0.
        """
    def StartFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face starting the slice, it is oriented toward the exterior of the primitive.
        """
    def StartTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and top Face.
        """
    def StartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face.
        """
    def TopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMax. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def TopEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def TopFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the top planar Face. It is Oriented toward the +Z axis (outside).
        """
    def TopStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMax)
        """
    def TopWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the top face.
        """
    @overload
    def VMax(self) -> float: 
        """
        None

        None
        """
    @overload
    def VMax(self,V : float) -> None: ...
    def VMaxInfinite(self) -> bool: 
        """
        Returns True if VMax is infinite. Default Precision::IsPositiveInfinite(VMax);
        """
    @overload
    def VMin(self,V : float) -> None: 
        """
        None

        None
        """
    @overload
    def VMin(self) -> float: ...
    def VMinInfinite(self) -> bool: 
        """
        Returns True if VMin is infinite. Default Precision::IsNegativeInfinite(VMax);
        """
    @overload
    def __init__(self,R : float,H : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,Radius : float) -> None: ...
    @overload
    def __init__(self,Position : OCP.gp.gp_Ax2,Radius : float,Height : float) -> None: ...
    @overload
    def __init__(self,Radius : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,Radius : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,R : float,H : float) -> None: ...
    pass
class BRepPrim_Sphere(BRepPrim_Revolution, BRepPrim_OneAxis):
    """
    Implements the sphere primitive
    """
    @overload
    def Angle(self,A : float) -> None: 
        """
        None

        None
        """
    @overload
    def Angle(self) -> float: ...
    @overload
    def Axes(self,A : OCP.gp.gp_Ax2) -> None: 
        """
        None

        Returns the Ax2 from <me>.
        """
    @overload
    def Axes(self) -> OCP.gp.gp_Ax2: ...
    def AxisBottomVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Bottom altitude on the axis.
        """
    def AxisEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge built along the Axis and oriented on +Z of the Axis.
        """
    def AxisEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face with the AxisEdge.
        """
    def AxisStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face with the AxisEdge.
        """
    def AxisTopVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Top altitude on the axis.
        """
    def BottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMin. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def BottomEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def BottomFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Bottom planar Face. It is Oriented toward the -Z axis (outside).
        """
    def BottomStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMin)
        """
    def BottomWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the bottom face.
        """
    def EndBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and bottom Face.
        """
    def EndEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle Angle. If !HasSides() the StartEdge and the EndEdge are the same edge.
        """
    def EndFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face ending the slice, it is oriented toward the exterior of the primitive.
        """
    def EndTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and top Face.
        """
    def EndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face.
        """
    def HasBottom(self) -> bool: 
        """
        Returns True if there is a bottom face.
        """
    def HasSides(self) -> bool: 
        """
        Returns True if there are Start and End faces.
        """
    def HasTop(self) -> bool: 
        """
        Returns True if there is a top face.
        """
    def LateralEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire with in lateral face with the end edge.
        """
    def LateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral Face. It is oriented toward the outside of the primitive.
        """
    def LateralStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face with the start edge.
        """
    def LateralWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face.
        """
    def MakeEmptyLateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        The surface normal should be directed towards the outside.
        """
    def MakeEmptyMeridianEdge(self,Ang : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns an edge with a 3D curve made from the meridian in the XZ plane rotated by <Ang> around the Z-axis. Ang may be 0 or myAngle.
        """
    def MeridianClosed(self) -> bool: 
        """
        Returns True if the meridian is closed. Default implementation is MeridianValue(VMin).IsEqual(MeridianValue(VMax), Precision::Confusion())
        """
    def MeridianOnAxis(self,V : float) -> bool: 
        """
        Returns True if the point of parameter <V> on the meridian is on the Axis. Default implementation is Abs(MeridianValue(V).X()) < Precision::Confusion()
        """
    def MeridianValue(self,V : float) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the meridian point at parameter <V> in the plane XZ.
        """
    def SetMeridianOffset(self,MeridianOffset : float=0.0) -> None: 
        """
        The MeridianOffset is added to the parameters on the meridian curve and to the V values of the pcurves. This is used for the sphere for example, to give a range on the meridian edge which is not VMin, VMax.
        """
    def SetMeridianPCurve(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the parametric urve of the edge <E> in the face <F> to be the 2d representation of the meridian.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the Shell containing all the Faces of the primitive.
        """
    def StartBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and bottom Face.
        """
    def StartEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle 0.
        """
    def StartFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face starting the slice, it is oriented toward the exterior of the primitive.
        """
    def StartTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and top Face.
        """
    def StartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face.
        """
    def TopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMax. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def TopEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def TopFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the top planar Face. It is Oriented toward the +Z axis (outside).
        """
    def TopStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMax)
        """
    def TopWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the top face.
        """
    @overload
    def VMax(self) -> float: 
        """
        None

        None
        """
    @overload
    def VMax(self,V : float) -> None: ...
    def VMaxInfinite(self) -> bool: 
        """
        Returns True if VMax is infinite. Default Precision::IsPositiveInfinite(VMax);
        """
    @overload
    def VMin(self,V : float) -> None: 
        """
        None

        None
        """
    @overload
    def VMin(self) -> float: ...
    def VMinInfinite(self) -> bool: 
        """
        Returns True if VMin is infinite. Default Precision::IsNegativeInfinite(VMax);
        """
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,Radius : float) -> None: ...
    @overload
    def __init__(self,Radius : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,Radius : float) -> None: ...
    pass
class BRepPrim_Torus(BRepPrim_Revolution, BRepPrim_OneAxis):
    """
    Implements the torus primitive
    """
    @overload
    def Angle(self,A : float) -> None: 
        """
        None

        None
        """
    @overload
    def Angle(self) -> float: ...
    @overload
    def Axes(self,A : OCP.gp.gp_Ax2) -> None: 
        """
        None

        Returns the Ax2 from <me>.
        """
    @overload
    def Axes(self) -> OCP.gp.gp_Ax2: ...
    def AxisBottomVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Bottom altitude on the axis.
        """
    def AxisEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge built along the Axis and oriented on +Z of the Axis.
        """
    def AxisEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face with the AxisEdge.
        """
    def AxisStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face with the AxisEdge.
        """
    def AxisTopVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex at the Top altitude on the axis.
        """
    def BottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMin. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def BottomEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def BottomFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Bottom planar Face. It is Oriented toward the -Z axis (outside).
        """
    def BottomStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMin)
        """
    def BottomWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the bottom face.
        """
    def EndBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and bottom Face.
        """
    def EndEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle Angle. If !HasSides() the StartEdge and the EndEdge are the same edge.
        """
    def EndFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face ending the slice, it is oriented toward the exterior of the primitive.
        """
    def EndTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between end Face and top Face.
        """
    def EndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire in the end face.
        """
    def HasBottom(self) -> bool: 
        """
        Returns True if there is a bottom face.
        """
    def HasSides(self) -> bool: 
        """
        Returns True if there are Start and End faces.
        """
    def HasTop(self) -> bool: 
        """
        Returns True if there is a top face.
        """
    def LateralEndWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire with in lateral face with the end edge.
        """
    def LateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral Face. It is oriented toward the outside of the primitive.
        """
    def LateralStartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face with the start edge.
        """
    def LateralWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the lateral face.
        """
    def MakeEmptyLateralFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        The surface normal should be directed towards the outside.
        """
    def MakeEmptyMeridianEdge(self,Ang : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns an edge with a 3D curve made from the meridian in the XZ plane rotated by <Ang> around the Z-axis. Ang may be 0 or myAngle.
        """
    def MeridianClosed(self) -> bool: 
        """
        Returns True if the meridian is closed. Default implementation is MeridianValue(VMin).IsEqual(MeridianValue(VMax), Precision::Confusion())
        """
    def MeridianOnAxis(self,V : float) -> bool: 
        """
        Returns True if the point of parameter <V> on the meridian is on the Axis. Default implementation is Abs(MeridianValue(V).X()) < Precision::Confusion()
        """
    def MeridianValue(self,V : float) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the meridian point at parameter <V> in the plane XZ.
        """
    def SetMeridianOffset(self,MeridianOffset : float=0.0) -> None: 
        """
        The MeridianOffset is added to the parameters on the meridian curve and to the V values of the pcurves. This is used for the sphere for example, to give a range on the meridian edge which is not VMin, VMax.
        """
    def SetMeridianPCurve(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the parametric urve of the edge <E> in the face <F> to be the 2d representation of the meridian.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the Shell containing all the Faces of the primitive.
        """
    def StartBottomEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and bottom Face.
        """
    def StartEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge at angle 0.
        """
    def StartFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face starting the slice, it is oriented toward the exterior of the primitive.
        """
    def StartTopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the linear Edge between start Face and top Face.
        """
    def StartWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the start face.
        """
    def TopEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge at VMax. If MeridianClosed() the TopEdge and the BottomEdge are the same edge.
        """
    def TopEndVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (angle,VMax)
        """
    def TopFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the top planar Face. It is Oriented toward the +Z axis (outside).
        """
    def TopStartVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex (0,VMax)
        """
    def TopWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the wire in the top face.
        """
    @overload
    def VMax(self) -> float: 
        """
        None

        None
        """
    @overload
    def VMax(self,V : float) -> None: ...
    def VMaxInfinite(self) -> bool: 
        """
        Returns True if VMax is infinite. Default Precision::IsPositiveInfinite(VMax);
        """
    @overload
    def VMin(self,V : float) -> None: 
        """
        None

        None
        """
    @overload
    def VMin(self) -> float: ...
    def VMinInfinite(self) -> bool: 
        """
        Returns True if VMin is infinite. Default Precision::IsNegativeInfinite(VMax);
        """
    @overload
    def __init__(self,Position : OCP.gp.gp_Ax2,Major : float,Minor : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,Major : float,Minor : float) -> None: ...
    @overload
    def __init__(self,Major : float,Minor : float) -> None: ...
    pass
class BRepPrim_Wedge(BRepPrim_GWedge):
    """
    Provides constructors without Builders.
    """
    def Axes(self) -> OCP.gp.gp_Ax2: 
        """
        Returns the coordinates system from <me>.
        """
    def Close(self,d1 : BRepPrim_Direction) -> None: 
        """
        Closes <me> in <d1> direction. A face and its edges or vertices are said existant.
        """
    def Edge(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge of <me> located in <d1><d2> direction.
        """
    def Face(self,d1 : BRepPrim_Direction) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the Face of <me> located in <d1> direction.
        """
    def GetX2Max(self) -> float: 
        """
        Returns X2Max value from <me>.
        """
    def GetX2Min(self) -> float: 
        """
        Returns X2Min value from <me>.
        """
    def GetXMax(self) -> float: 
        """
        Returns XMax value from <me>.
        """
    def GetXMin(self) -> float: 
        """
        Returns Xmin value from <me>.
        """
    def GetYMax(self) -> float: 
        """
        Returns YMax value from <me>.
        """
    def GetYMin(self) -> float: 
        """
        Returns YMin value from <me>.
        """
    def GetZ2Max(self) -> float: 
        """
        Returns Z2Max value from <me>.
        """
    def GetZ2Min(self) -> float: 
        """
        Returns Z2Min value from <me>.
        """
    def GetZMax(self) -> float: 
        """
        Returns ZMax value from <me>.
        """
    def GetZMin(self) -> float: 
        """
        Returns ZMin value from <me>.
        """
    def HasEdge(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> has an Edge in <d1><d2> direction.
        """
    def HasFace(self,d1 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> has a Face in <d1> direction.
        """
    def HasVertex(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction,d3 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> has a Vertex in <d1><d2><d3> direction.
        """
    def HasWire(self,d1 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> has a Wire in <d1> direction.
        """
    def IsDegeneratedShape(self) -> bool: 
        """
        Checkes a shape on degeneracy
        """
    def IsInfinite(self,d1 : BRepPrim_Direction) -> bool: 
        """
        Returns True if <me> is open in <d1> direction.
        """
    def Line(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction) -> OCP.gp.gp_Lin: 
        """
        Returns the line of the Edge of <me> located in <d1><d2> direction.
        """
    def Open(self,d1 : BRepPrim_Direction) -> None: 
        """
        Opens <me> in <d1> direction. A face and its edges or vertices are said nonexistant.
        """
    def Plane(self,d1 : BRepPrim_Direction) -> OCP.gp.gp_Pln: 
        """
        Returns the plane of the Face of <me> located in <d1> direction.
        """
    def Point(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction,d3 : BRepPrim_Direction) -> OCP.gp.gp_Pnt: 
        """
        Returns the point of the Vertex of <me> located in <d1><d2><d3> direction.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the Shell containing the Faces of <me>.
        """
    def Vertex(self,d1 : BRepPrim_Direction,d2 : BRepPrim_Direction,d3 : BRepPrim_Direction) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the Vertex of <me> located in <d1><d2><d3> direction.
        """
    def Wire(self,d1 : BRepPrim_Direction) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the Wire of <me> located in <d1> direction.
        """
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,dx : float,dy : float,dz : float,ltx : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,dx : float,dy : float,dz : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,xmin : float,ymin : float,zmin : float,z2min : float,x2min : float,xmax : float,ymax : float,zmax : float,z2max : float,x2max : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
BRepPrim_XMax: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_XMax: 1>
BRepPrim_XMin: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_XMin: 0>
BRepPrim_YMax: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_YMax: 3>
BRepPrim_YMin: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_YMin: 2>
BRepPrim_ZMax: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_ZMax: 5>
BRepPrim_ZMin: OCP.BRepPrim.BRepPrim_Direction # value = <BRepPrim_Direction.BRepPrim_ZMin: 4>
