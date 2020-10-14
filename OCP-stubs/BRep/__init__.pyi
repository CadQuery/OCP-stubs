import OCP.BRep
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.GeomAbs
import OCP.Poly
import OCP.Geom2d
import OCP.Standard
import OCP.TopoDS
import OCP.Geom
import OCP.NCollection
import OCP.TopLoc
import OCP.gp
__all__  = [
"BRep_Builder",
"BRep_CurveRepresentation",
"BRep_CurveOn2Surfaces",
"BRep_GCurve",
"BRep_CurveOnSurface",
"BRep_Curve3D",
"BRep_CurveOnClosedSurface",
"BRep_ListOfCurveRepresentation",
"BRep_ListOfPointRepresentation",
"BRep_PointRepresentation",
"BRep_PointsOnSurface",
"BRep_PointOnSurface",
"BRep_PointOnCurve",
"BRep_PointOnCurveOnSurface",
"BRep_Polygon3D",
"BRep_PolygonOnSurface",
"BRep_PolygonOnTriangulation",
"BRep_PolygonOnClosedSurface",
"BRep_PolygonOnClosedTriangulation",
"BRep_TEdge",
"BRep_TFace",
"BRep_TVertex",
"BRep_Tool"
]
class BRep_Builder(OCP.TopoDS.TopoDS_Builder):
    """
    A framework providing advanced tolerance control. It is used to build Shapes. If tolerance control is required, you are advised to: 1. build a default precision for topology, using the classes provided in the BRepAPI package 2. update the tolerance of the resulting shape. Note that only vertices, edges and faces have meaningful tolerance control. The tolerance value must always comply with the condition that face tolerances are more restrictive than edge tolerances which are more restrictive than vertex tolerances. In other words: Tol(Vertex) >= Tol(Edge) >= Tol(Face). Other rules in setting tolerance include: - you can open up tolerance but should never restrict it - an edge cannot be included within the fusion of the tolerance spheres of two vertices
    """
    def Add(self,S : OCP.TopoDS.TopoDS_Shape,C : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Add the Shape C in the Shape S. Exceptions - TopoDS_FrozenShape if S is not free and cannot be modified. - TopoDS__UnCompatibleShapes if S and C are not compatible.
        """
    @overload
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,C : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Sets the geometric continuity on the edge.

        Sets the geometric continuity on the edge.
        """
    @overload
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Degenerated(self,E : OCP.TopoDS.TopoDS_Edge,D : bool) -> None: 
        """
        Sets the degenerated flag for the edge <E>.
        """
    def MakeCompSolid(self,C : OCP.TopoDS.TopoDS_CompSolid) -> None: 
        """
        Make an empty Composite Solid.

        Make an empty Composite Solid.
        """
    def MakeCompound(self,C : OCP.TopoDS.TopoDS_Compound) -> None: 
        """
        Make an empty Compound.

        Make an empty Compound.
        """
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge,N : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Makes an undefined Edge (no geometry).

        Makes an Edge with a curve.

        Makes an Edge with a curve and a location.

        Makes an Edge with a polygon 3d.

        makes an Edge polygon on Triangulation.

        makes an Edge polygon on Triangulation.

        Makes an Edge with a curve.

        Makes an Edge with a polygon 3d.

        makes an Edge polygon on Triangulation.

        makes an Edge polygon on Triangulation.

        Makes an Edge with a curve and a location.
        """
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge,N : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation) -> None: ...
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> None: ...
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> None: ...
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,Tol : float) -> None: ...
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation) -> None: ...
    @overload
    def MakeFace(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> None: 
        """
        Makes an undefined Face.

        Makes a Face with a surface.

        Makes a Face with a surface and a location.

        Makes a Face with a triangulation. The triangulation is in the same reference system than the TFace.

        Makes an undefined Face.
        """
    @overload
    def MakeFace(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,Tol : float) -> None: ...
    @overload
    def MakeFace(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> None: ...
    @overload
    def MakeFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    def MakeShell(self,S : OCP.TopoDS.TopoDS_Shell) -> None: 
        """
        Make an empty Shell.

        Make an empty Shell.
        """
    def MakeSolid(self,S : OCP.TopoDS.TopoDS_Solid) -> None: 
        """
        Make a Solid covering the whole 3D space.

        Make a Solid covering the whole 3D space.
        """
    @overload
    def MakeVertex(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> None: 
        """
        Makes an udefined vertex without geometry.

        Makes a vertex from a 3D point.

        Makes an udefined vertex without geometry.

        Makes a vertex from a 3D point.
        """
    @overload
    def MakeVertex(self,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    def MakeWire(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Make an empty Wire.

        Make an empty Wire.
        """
    def NaturalRestriction(self,F : OCP.TopoDS.TopoDS_Face,N : bool) -> None: 
        """
        Sets the NaturalRestriction flag of the face.
        """
    @overload
    def Range(self,E : OCP.TopoDS.TopoDS_Edge,First : float,Last : float,Only3d : bool=False) -> None: 
        """
        Sets the range of the 3d curve if Only3d=TRUE, otherwise sets the range to all the representations

        Sets the range of the edge on the pcurve on the surface.

        Sets the range of the edge on the pcurve on the face.

        Sets the range of the edge on the pcurve on the face.
        """
    @overload
    def Range(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,First : float,Last : float) -> None: ...
    @overload
    def Range(self,E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,First : float,Last : float) -> None: ...
    def Remove(self,S : OCP.TopoDS.TopoDS_Shape,C : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the Shape C from the Shape S. Exceptions TopoDS_FrozenShape if S is frozen and cannot be modified.
        """
    def SameParameter(self,E : OCP.TopoDS.TopoDS_Edge,S : bool) -> None: 
        """
        Sets the same parameter flag for the edge <E>.
        """
    def SameRange(self,E : OCP.TopoDS.TopoDS_Edge,S : bool) -> None: 
        """
        Sets the same range flag for the edge <E>.
        """
    @overload
    def Transfert(self,Ein : OCP.TopoDS.TopoDS_Edge,Eout : OCP.TopoDS.TopoDS_Edge,Vin : OCP.TopoDS.TopoDS_Vertex,Vout : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Add to <Eout> the geometric representations of <Ein>.

        Transfert the parameters of Vin on Ein as the parameter of Vout on Eout.
        """
    @overload
    def Transfert(self,Ein : OCP.TopoDS.TopoDS_Edge,Eout : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon2D,S : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets a 3D curve for the edge. If <C> is a null handle, remove any existing 3d curve.

        Sets a 3D curve for the edge. If <C> is a null handle, remove any existing 3d curve.

        Sets a pcurve for the edge on the face. If <C> is a null handle, remove any existing pcurve.

        Sets pcurves for the edge on the closed face. If <C1> or <C2> is a null handle, remove any existing pcurve.

        Sets a pcurve for the edge on the face. If <C> is a null handle, remove any existing pcurve.

        Sets a pcurve for the edge on the face. If <C> is a null handle, remove any existing pcurve. Sets UV bounds for curve repsentation

        Sets pcurves for the edge on the closed surface. <C1> or <C2> is a null handle, remove any existing pcurve.

        Sets pcurves for the edge on the closed surface. <C1> or <C2> is a null handle, remove any existing pcurve. Sets UV bounds for curve repsentation

        Changes an Edge 3D polygon. A null Polygon removes the 3d Polygon.

        Changes an Edge 3D polygon. A null Polygon removes the 3d Polygon.

        Changes an Edge polygon on Triangulation.

        Changes an Edge polygon on Triangulation.

        Changes an Edge polygon on Triangulation.

        Changes an Edge polygon on Triangulation.

        Changes Edge polygon on a face.

        Changes Edge polygon on a face.

        Changes Edge polygons on a face.

        Changes Edge polygons on a face.

        Updates the edge tolerance.

        Sets a 3D curve for the edge. If <C> is a null handle, remove any existing 3d curve.

        Sets a pcurve for the edge on the face. If <C> is a null handle, remove any existing pcurve.

        Sets pcurves for the edge on the closed face. If <C1> or <C2> is a null handle, remove any existing pcurve.

        Changes an Edge 3D polygon. A null Polygon removes the 3d Polygon.

        Changes an Edge polygon on Triangulation.

        Changes an Edge polygon on Triangulation.
        """
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,Tol : float) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon2D,S : OCP.Geom.Geom_Surface,T : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,Pf : OCP.gp.gp_Pnt2d,Pl : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,P1 : OCP.Poly.Poly_Polygon2D,P2 : OCP.Poly.Poly_Polygon2D,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,Tol : float) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,C1 : OCP.Geom2d.Geom2d_Curve,C2 : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,Pf : OCP.gp.gp_Pnt2d,Pl : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,C1 : OCP.Geom2d.Geom2d_Curve,C2 : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,N1 : OCP.Poly.Poly_PolygonOnTriangulation,N2 : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,P1 : OCP.Poly.Poly_Polygon2D,P2 : OCP.Poly.Poly_Polygon2D,S : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,P1 : OCP.Poly.Poly_PolygonOnTriangulation,P2 : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,N : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,N : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom2d.Geom2d_Curve,F : OCP.TopoDS.TopoDS_Face,Tol : float) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,C1 : OCP.Geom2d.Geom2d_Curve,C2 : OCP.Geom2d.Geom2d_Curve,F : OCP.TopoDS.TopoDS_Face,Tol : float) -> None: ...
    @overload
    def UpdateEdge(self,E : OCP.TopoDS.TopoDS_Edge,N1 : OCP.Poly.Poly_PolygonOnTriangulation,N2 : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def UpdateFace(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> None: 
        """
        Updates the face F using the tolerance value Tol, surface S and location Location.

        Changes a face triangulation.

        Updates the face Tolerance.
        """
    @overload
    def UpdateFace(self,F : OCP.TopoDS.TopoDS_Face,Tol : float) -> None: ...
    @overload
    def UpdateFace(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> None: ...
    @overload
    def UpdateVertex(self,V : OCP.TopoDS.TopoDS_Vertex,P : float,E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> None: 
        """
        Sets a 3D point on the vertex.

        Sets the parameter for the vertex on the edge curves.

        Sets the parameter for the vertex on the edge pcurve on the face.

        Sets the parameter for the vertex on the edge pcurve on the surface.

        Sets the parameters for the vertex on the face.

        Updates the vertex tolerance.

        Sets the parameter for the vertex on the edge pcurve on the face.
        """
    @overload
    def UpdateVertex(self,V : OCP.TopoDS.TopoDS_Vertex,Tol : float) -> None: ...
    @overload
    def UpdateVertex(self,Ve : OCP.TopoDS.TopoDS_Vertex,U : float,V : float,F : OCP.TopoDS.TopoDS_Face,Tol : float) -> None: ...
    @overload
    def UpdateVertex(self,V : OCP.TopoDS.TopoDS_Vertex,P : float,E : OCP.TopoDS.TopoDS_Edge,Tol : float) -> None: ...
    @overload
    def UpdateVertex(self,V : OCP.TopoDS.TopoDS_Vertex,P : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,Tol : float) -> None: ...
    @overload
    def UpdateVertex(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> None: ...
    @overload
    def UpdateVertex(self,V : OCP.TopoDS.TopoDS_Vertex,Par : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,Tol : float) -> None: ...
    def __init__(self) -> None: ...
    pass
class BRep_CurveRepresentation(OCP.Standard.Standard_Transient):
    """
    Root class for the curve representations. Contains a location.Root class for the curve representations. Contains a location.Root class for the curve representations. Contains a location.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        A curve in the parametric space of a surface.

        Is it a curve in the parametric space of <S> with location <L>.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A polygon in the parametric space of a surface.

        Is it a polygon in the parametric space of <S> with location <L>.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A representation by an array of nodes on a triangulation.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self) -> bool: 
        """
        A continuity between two surfaces.

        Is it a regularity between <S1> and <S2> with location <L1> and <L2>.
        """
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
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
class BRep_CurveOn2Surfaces(BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    Defines a continuity between two surfaces.Defines a continuity between two surfaces.Defines a continuity between two surfaces.
    """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Raises an error.
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
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        A curve in the parametric space of a surface.

        Is it a curve in the parametric space of <S> with location <L>.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A polygon in the parametric space of a surface.

        Is it a polygon in the parametric space of <S> with location <L>.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A representation by an array of nodes on a triangulation.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        Returns True.

        A curve on two surfaces (continuity).
        """
    @overload
    def IsRegularity(self) -> bool: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def __init__(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
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
class BRep_GCurve(BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    Root class for the geometric curves representation. Contains a range. Contains a first and a last parameter.Root class for the geometric curves representation. Contains a range. Contains a first and a last parameter.Root class for the geometric curves representation. Contains a range. Contains a first and a last parameter.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point at parameter U.
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
    @overload
    def First(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def First(self,F : float) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        A curve in the parametric space of a surface.

        Is it a curve in the parametric space of <S> with location <L>.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A polygon in the parametric space of a surface.

        Is it a polygon in the parametric space of <S> with location <L>.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A representation by an array of nodes on a triangulation.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self) -> bool: 
        """
        A continuity between two surfaces.

        Is it a regularity between <S1> and <S2> with location <L1> and <L2>.
        """
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Last(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Last(self,L : float) -> None: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Range(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def SetRange(self,First : float,Last : float) -> None: 
        """
        None

        None
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def Update(self) -> None: 
        """
        Recomputes any derived data after a modification. This is called when the range is modified.
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
class BRep_CurveOnSurface(BRep_GCurve, BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation of a curve by a curve in the parametric space of a surface.Representation of a curve by a curve in the parametric space of a surface.Representation of a curve by a curve in the parametric space of a surface.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point at parameter U.
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
    @overload
    def First(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def First(self,F : float) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        Returns True.

        A curve in the parametric space of a surface.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A polygon in the parametric space of a surface.

        Is it a polygon in the parametric space of <S> with location <L>.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A representation by an array of nodes on a triangulation.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self) -> bool: 
        """
        A continuity between two surfaces.

        Is it a regularity between <S1> and <S2> with location <L1> and <L2>.
        """
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Last(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Last(self,L : float) -> None: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Range(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def SetRange(self,First : float,Last : float) -> None: 
        """
        None

        None
        """
    def SetUVPoints(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def UVPoints(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None
        """
    def Update(self) -> None: 
        """
        Recomputes any derived data after a modification. This is called when the range is modified.
        """
    def __init__(self,PC : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_Curve3D(BRep_GCurve, BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation of a curve by a 3D curve.Representation of a curve by a 3D curve.Representation of a curve by a 3D curve.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: ...
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point at parameter U.
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
    @overload
    def First(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def First(self,F : float) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCurve3D(self) -> bool: 
        """
        Returns True.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        A curve in the parametric space of a surface.

        Is it a curve in the parametric space of <S> with location <L>.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A polygon in the parametric space of a surface.

        Is it a polygon in the parametric space of <S> with location <L>.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A representation by an array of nodes on a triangulation.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self) -> bool: 
        """
        A continuity between two surfaces.

        Is it a regularity between <S1> and <S2> with location <L1> and <L2>.
        """
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Last(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Last(self,L : float) -> None: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Range(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def SetRange(self,First : float,Last : float) -> None: 
        """
        None

        None
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def Update(self) -> None: 
        """
        Recomputes any derived data after a modification. This is called when the range is modified.
        """
    def __init__(self,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_CurveOnClosedSurface(BRep_CurveOnSurface, BRep_GCurve, BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation of a curve by two pcurves on a closed surface.Representation of a curve by two pcurves on a closed surface.Representation of a curve by two pcurves on a closed surface.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point at parameter U.
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
    @overload
    def First(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def First(self,F : float) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        Returns True.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        Returns True.

        A curve in the parametric space of a surface.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A polygon in the parametric space of a surface.

        Is it a polygon in the parametric space of <S> with location <L>.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A representation by an array of nodes on a triangulation.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        Returns True

        A curve on two surfaces (continuity).
        """
    @overload
    def IsRegularity(self) -> bool: ...
    @overload
    def Last(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Last(self,L : float) -> None: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Returns Location()
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Range(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    def SetRange(self,First : float,Last : float) -> None: 
        """
        None

        None
        """
    def SetUVPoints(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None
        """
    def SetUVPoints2(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        Returns Surface()
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def UVPoints(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None
        """
    def UVPoints2(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        None

        None
        """
    def Update(self) -> None: 
        """
        Recomputes any derived data after a modification. This is called when the range is modified.
        """
    def __init__(self,PC1 : OCP.Geom2d.Geom2d_Curve,PC2 : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
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
class BRep_ListOfCurveRepresentation(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BRep_CurveRepresentation,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : BRep_ListOfCurveRepresentation) -> None: ...
    @overload
    def Append(self,theItem : BRep_CurveRepresentation) -> BRep_CurveRepresentation: ...
    def Assign(self,theOther : BRep_ListOfCurveRepresentation) -> BRep_ListOfCurveRepresentation: 
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
    def First(self) -> BRep_CurveRepresentation: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : BRep_ListOfCurveRepresentation,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : BRep_CurveRepresentation,theIter : Any) -> BRep_CurveRepresentation: ...
    @overload
    def InsertBefore(self,theOther : BRep_ListOfCurveRepresentation,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : BRep_CurveRepresentation,theIter : Any) -> BRep_CurveRepresentation: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BRep_CurveRepresentation: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : BRep_ListOfCurveRepresentation) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : BRep_CurveRepresentation) -> BRep_CurveRepresentation: ...
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
    def __init__(self,theOther : BRep_ListOfCurveRepresentation) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BRep_ListOfPointRepresentation(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : BRep_ListOfPointRepresentation) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : BRep_PointRepresentation,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : BRep_PointRepresentation) -> BRep_PointRepresentation: ...
    def Assign(self,theOther : BRep_ListOfPointRepresentation) -> BRep_ListOfPointRepresentation: 
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
    def First(self) -> BRep_PointRepresentation: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : BRep_ListOfPointRepresentation,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : BRep_PointRepresentation,theIter : Any) -> BRep_PointRepresentation: ...
    @overload
    def InsertBefore(self,theItem : BRep_PointRepresentation,theIter : Any) -> BRep_PointRepresentation: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : BRep_ListOfPointRepresentation,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BRep_PointRepresentation: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : BRep_ListOfPointRepresentation) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : BRep_PointRepresentation) -> BRep_PointRepresentation: ...
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
    def __init__(self,theOther : BRep_ListOfPointRepresentation) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BRep_PointRepresentation(OCP.Standard.Standard_Transient):
    """
    Root class for the points representations. Contains a location and a parameter.Root class for the points representations. Contains a location and a parameter.Root class for the points representations. Contains a location and a parameter.
    """
    @overload
    def Curve(self,C : OCP.Geom.Geom_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def Curve(self) -> OCP.Geom.Geom_Curve: ...
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
    def IsPointOnCurve(self) -> bool: 
        """
        A point on a 3d curve.

        A point on the curve <C>.
        """
    @overload
    def IsPointOnCurve(self,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def IsPointOnCurveOnSurface(self,PC : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A point on a 2d curve on a surface.

        A point on the 2d curve <PC> on the surface <S>.
        """
    @overload
    def IsPointOnCurveOnSurface(self) -> bool: ...
    @overload
    def IsPointOnSurface(self) -> bool: 
        """
        A point on a surface.

        A point on the surface <S>.
        """
    @overload
    def IsPointOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Parameter(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Parameter(self,P : float) -> None: ...
    @overload
    def Parameter2(self,P : float) -> None: 
        """
        None

        None
        """
    @overload
    def Parameter2(self) -> float: ...
    @overload
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None

        None
        """
    @overload
    def Surface(self,S : OCP.Geom.Geom_Surface) -> None: ...
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
class BRep_PointsOnSurface(BRep_PointRepresentation, OCP.Standard.Standard_Transient):
    """
    Root for points on surface.Root for points on surface.Root for points on surface.
    """
    @overload
    def Curve(self,C : OCP.Geom.Geom_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def Curve(self) -> OCP.Geom.Geom_Curve: ...
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
    def IsPointOnCurve(self) -> bool: 
        """
        A point on a 3d curve.

        A point on the curve <C>.
        """
    @overload
    def IsPointOnCurve(self,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def IsPointOnCurveOnSurface(self,PC : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A point on a 2d curve on a surface.

        A point on the 2d curve <PC> on the surface <S>.
        """
    @overload
    def IsPointOnCurveOnSurface(self) -> bool: ...
    @overload
    def IsPointOnSurface(self) -> bool: 
        """
        A point on a surface.

        A point on the surface <S>.
        """
    @overload
    def IsPointOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Parameter(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Parameter(self,P : float) -> None: ...
    @overload
    def Parameter2(self,P : float) -> None: 
        """
        None

        None
        """
    @overload
    def Parameter2(self) -> float: ...
    @overload
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None

        None
        """
    @overload
    def Surface(self,S : OCP.Geom.Geom_Surface) -> None: ...
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
class BRep_PointOnSurface(BRep_PointsOnSurface, BRep_PointRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation by two parameters on a surface.Representation by two parameters on a surface.Representation by two parameters on a surface.
    """
    @overload
    def Curve(self,C : OCP.Geom.Geom_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def Curve(self) -> OCP.Geom.Geom_Curve: ...
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
    def IsPointOnCurve(self) -> bool: 
        """
        A point on a 3d curve.

        A point on the curve <C>.
        """
    @overload
    def IsPointOnCurve(self,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def IsPointOnCurveOnSurface(self,PC : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A point on a 2d curve on a surface.

        A point on the 2d curve <PC> on the surface <S>.
        """
    @overload
    def IsPointOnCurveOnSurface(self) -> bool: ...
    @overload
    def IsPointOnSurface(self) -> bool: 
        """
        None

        None
        """
    @overload
    def IsPointOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Parameter(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Parameter(self,P : float) -> None: ...
    @overload
    def Parameter2(self,P : float) -> None: 
        """
        None

        None
        """
    @overload
    def Parameter2(self) -> float: ...
    @overload
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None

        None
        """
    @overload
    def Surface(self,S : OCP.Geom.Geom_Surface) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,P1 : float,P2 : float,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_PointOnCurve(BRep_PointRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation by a parameter on a 3D curve.Representation by a parameter on a 3D curve.Representation by a parameter on a 3D curve.
    """
    @overload
    def Curve(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def IsPointOnCurve(self,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        Returns True

        None
        """
    @overload
    def IsPointOnCurve(self) -> bool: ...
    @overload
    def IsPointOnCurveOnSurface(self,PC : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A point on a 2d curve on a surface.

        A point on the 2d curve <PC> on the surface <S>.
        """
    @overload
    def IsPointOnCurveOnSurface(self) -> bool: ...
    @overload
    def IsPointOnSurface(self) -> bool: 
        """
        A point on a surface.

        A point on the surface <S>.
        """
    @overload
    def IsPointOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Parameter(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Parameter(self,P : float) -> None: ...
    @overload
    def Parameter2(self,P : float) -> None: 
        """
        None

        None
        """
    @overload
    def Parameter2(self) -> float: ...
    @overload
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None

        None
        """
    @overload
    def Surface(self,S : OCP.Geom.Geom_Surface) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,P : float,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_PointOnCurveOnSurface(BRep_PointsOnSurface, BRep_PointRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation by a parameter on a curve on a surface.Representation by a parameter on a curve on a surface.Representation by a parameter on a curve on a surface.
    """
    @overload
    def Curve(self,C : OCP.Geom.Geom_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def Curve(self) -> OCP.Geom.Geom_Curve: ...
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
    def IsPointOnCurve(self) -> bool: 
        """
        A point on a 3d curve.

        A point on the curve <C>.
        """
    @overload
    def IsPointOnCurve(self,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def IsPointOnCurveOnSurface(self,PC : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        Returns True

        None
        """
    @overload
    def IsPointOnCurveOnSurface(self) -> bool: ...
    @overload
    def IsPointOnSurface(self) -> bool: 
        """
        A point on a surface.

        A point on the surface <S>.
        """
    @overload
    def IsPointOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def Parameter(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Parameter(self,P : float) -> None: ...
    @overload
    def Parameter2(self,P : float) -> None: 
        """
        None

        None
        """
    @overload
    def Parameter2(self) -> float: ...
    @overload
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None

        None
        """
    @overload
    def Surface(self,S : OCP.Geom.Geom_Surface) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,P : float,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_Polygon3D(BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation by a 3D polygon.Representation by a 3D polygon.Representation by a 3D polygon.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        A curve in the parametric space of a surface.

        Is it a curve in the parametric space of <S> with location <L>.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        Returns True.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A polygon in the parametric space of a surface.

        Is it a polygon in the parametric space of <S> with location <L>.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A representation by an array of nodes on a triangulation.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self) -> bool: 
        """
        A continuity between two surfaces.

        Is it a regularity between <S1> and <S2> with location <L1> and <L2>.
        """
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: ...
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def __init__(self,P : OCP.Poly.Poly_Polygon3D,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_PolygonOnSurface(BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation of a 2D polygon in the parametric space of a surface.Representation of a 2D polygon in the parametric space of a surface.Representation of a 2D polygon in the parametric space of a surface.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        A curve in the parametric space of a surface.

        Is it a curve in the parametric space of <S> with location <L>.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A 2D polygon representation in the parametric space of a surface.

        A 2D polygon representation in the parametric space of a surface.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A representation by an array of nodes on a triangulation.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self) -> bool: 
        """
        A continuity between two surfaces.

        Is it a regularity between <S1> and <S2> with location <L1> and <L2>.
        """
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def __init__(self,P : OCP.Poly.Poly_Polygon2D,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_PolygonOnTriangulation(BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    A representation by an array of nodes on a triangulation.A representation by an array of nodes on a triangulation.A representation by an array of nodes on a triangulation.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        A curve in the parametric space of a surface.

        Is it a curve in the parametric space of <S> with location <L>.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A polygon in the parametric space of a surface.

        Is it a polygon in the parametric space of <S> with location <L>.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        returns True.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self) -> bool: 
        """
        A continuity between two surfaces.

        Is it a regularity between <S1> and <S2> with location <L1> and <L2>.
        """
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        returns True.

        None
        """
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def __init__(self,P : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_PolygonOnClosedSurface(BRep_PolygonOnSurface, BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation by two 2d polygons in the parametric space of a surface.Representation by two 2d polygons in the parametric space of a surface.Representation by two 2d polygons in the parametric space of a surface.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        A curve in the parametric space of a surface.

        Is it a curve in the parametric space of <S> with location <L>.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        returns True.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        A representation by two arrays of nodes on a triangulation.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A 2D polygon representation in the parametric space of a surface.

        A 2D polygon representation in the parametric space of a surface.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A representation by an array of nodes on a triangulation.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self) -> bool: 
        """
        A continuity between two surfaces.

        Is it a regularity between <S1> and <S2> with location <L1> and <L2>.
        """
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def __init__(self,P1 : OCP.Poly.Poly_Polygon2D,P2 : OCP.Poly.Poly_Polygon2D,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_PolygonOnClosedTriangulation(BRep_PolygonOnTriangulation, BRep_CurveRepresentation, OCP.Standard.Standard_Transient):
    """
    A representation by two arrays of nodes on a triangulation.A representation by two arrays of nodes on a triangulation.A representation by two arrays of nodes on a triangulation.
    """
    @overload
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None

        None
        """
    @overload
    def Continuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    def Copy(self) -> BRep_CurveRepresentation: 
        """
        Return a copy of this representation.
        """
    @overload
    def Curve3D(self) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @overload
    def Curve3D(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def IsCurve3D(self) -> bool: 
        """
        A 3D curve representation.
        """
    def IsCurveOnClosedSurface(self) -> bool: 
        """
        A curve with two parametric curves on the same surface.
        """
    @overload
    def IsCurveOnSurface(self) -> bool: 
        """
        A curve in the parametric space of a surface.

        Is it a curve in the parametric space of <S> with location <L>.
        """
    @overload
    def IsCurveOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
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
    def IsPolygon3D(self) -> bool: 
        """
        A 3D polygon representation.
        """
    def IsPolygonOnClosedSurface(self) -> bool: 
        """
        Two 2D polygon representations in the parametric space of a surface.
        """
    def IsPolygonOnClosedTriangulation(self) -> bool: 
        """
        Returns True.
        """
    @overload
    def IsPolygonOnSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        A polygon in the parametric space of a surface.

        Is it a polygon in the parametric space of <S> with location <L>.
        """
    @overload
    def IsPolygonOnSurface(self) -> bool: ...
    @overload
    def IsPolygonOnTriangulation(self,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        returns True.

        Is it a polygon in the definition of <T> with location <L>.
        """
    @overload
    def IsPolygonOnTriangulation(self) -> bool: ...
    @overload
    def IsRegularity(self) -> bool: 
        """
        A continuity between two surfaces.

        Is it a regularity between <S1> and <S2> with location <L1> and <L2>.
        """
    @overload
    def IsRegularity(self,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: ...
    def Location2(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    @overload
    def PCurve(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: ...
    @overload
    def PCurve2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve2(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Polygon(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon2(self) -> OCP.Poly.Poly_Polygon2D: 
        """
        None

        None
        """
    @overload
    def Polygon2(self,P : OCP.Poly.Poly_Polygon2D) -> None: ...
    @overload
    def Polygon3D(self,P : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        None

        None
        """
    @overload
    def Polygon3D(self) -> OCP.Poly.Poly_Polygon3D: ...
    @overload
    def PolygonOnTriangulation(self,P : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        returns True.

        None
        """
    @overload
    def PolygonOnTriangulation(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    @overload
    def PolygonOnTriangulation2(self,P2 : OCP.Poly.Poly_PolygonOnTriangulation) -> None: 
        """
        None

        None
        """
    @overload
    def PolygonOnTriangulation2(self) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Surface2(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None
        """
    def __init__(self,P1 : OCP.Poly.Poly_PolygonOnTriangulation,P2 : OCP.Poly.Poly_PolygonOnTriangulation,Tr : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> None: ...
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
class BRep_TEdge(OCP.TopoDS.TopoDS_TEdge, OCP.TopoDS.TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    The TEdge from BRep is inherited from the TEdge from TopoDS. It contains the geometric data.The TEdge from BRep is inherited from the TEdge from TopoDS. It contains the geometric data.The TEdge from BRep is inherited from the TEdge from TopoDS. It contains the geometric data.
    """
    def ChangeCurves(self) -> BRep_ListOfCurveRepresentation: 
        """
        None

        None
        """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def Curves(self) -> BRep_ListOfCurveRepresentation: 
        """
        None

        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @overload
    def Degenerated(self,S : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Degenerated(self) -> bool: ...
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EmptyCopy(self) -> OCP.TopoDS.TopoDS_TShape: 
        """
        Returns a copy of the TShape with no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self) -> bool: ...
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
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def SameParameter(self) -> bool: 
        """
        None

        None
        """
    @overload
    def SameParameter(self,S : bool) -> None: ...
    @overload
    def SameRange(self) -> bool: 
        """
        None

        None
        """
    @overload
    def SameRange(self,S : bool) -> None: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns EDGE.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tolerance(self,T : float) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Tolerance(self) -> float: ...
    def UpdateTolerance(self,T : float) -> None: 
        """
        Sets the tolerance to the max of <T> and the current tolerance.

        Sets the tolerance to the max of <T> and the current tolerance.
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
class BRep_TFace(OCP.TopoDS.TopoDS_TFace, OCP.TopoDS.TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    The Tface from BRep is based on the TFace from TopoDS. The TFace contains :The Tface from BRep is based on the TFace from TopoDS. The TFace contains :The Tface from BRep is based on the TFace from TopoDS. The TFace contains :
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EmptyCopy(self) -> OCP.TopoDS.TopoDS_TShape: 
        """
        Returns a copy of the TShape with no sub-shapes. The new Face has no triangulation.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self) -> bool: ...
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
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None

        None

        None

        None
        """
    @overload
    def Location(self,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    @overload
    def NaturalRestriction(self,N : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def NaturalRestriction(self) -> bool: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        returns FACE.
        """
    @overload
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None

        None

        None

        None
        """
    @overload
    def Surface(self,S : OCP.Geom.Geom_Surface) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tolerance(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Tolerance(self,T : float) -> None: ...
    @overload
    def Triangulation(self) -> OCP.Poly.Poly_Triangulation: 
        """
        None

        None

        None

        None
        """
    @overload
    def Triangulation(self,T : OCP.Poly.Poly_Triangulation) -> None: ...
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
class BRep_TVertex(OCP.TopoDS.TopoDS_TVertex, OCP.TopoDS.TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    The TVertex from BRep inherits from the TVertex from TopoDS. It contains the geometric data.The TVertex from BRep inherits from the TVertex from TopoDS. It contains the geometric data.The TVertex from BRep inherits from the TVertex from TopoDS. It contains the geometric data.
    """
    def ChangePoints(self) -> BRep_ListOfPointRepresentation: 
        """
        None

        None
        """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EmptyCopy(self) -> OCP.TopoDS.TopoDS_TShape: 
        """
        Returns a copy of the TShape with no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self) -> bool: ...
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
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Pnt(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Pnt(self) -> OCP.gp.gp_Pnt: ...
    def Points(self) -> BRep_ListOfPointRepresentation: 
        """
        None

        None
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns VERTEX.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tolerance(self,T : float) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Tolerance(self) -> float: ...
    def UpdateTolerance(self,T : float) -> None: 
        """
        Sets the tolerance to the max of <T> and the current tolerance.

        Sets the tolerance to the max of <T> and the current tolerance.
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
class BRep_Tool():
    """
    Provides class methods to access to the geometry of BRep shapes.
    """
    @staticmethod
    @overload
    def Continuity_s(E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity.

        Returns the continuity.
        """
    @staticmethod
    @overload
    def Continuity_s(E : OCP.TopoDS.TopoDS_Edge,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> OCP.GeomAbs.GeomAbs_Shape: ...
    @staticmethod
    def CurveOnPlane_s(E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,First : float,Last : float) -> OCP.Geom2d.Geom2d_Curve: 
        """
        For the planar surface builds the 2d curve for the edge by projection of the edge on plane. Returns a NULL handle if the surface is not planar or the projection failed.
        """
    @staticmethod
    @overload
    def CurveOnSurface_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,First : float,Last : float,theIsStored : bool=None) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns the curve associated to the edge in the parametric space of the face. Returns a NULL handle if this curve does not exist. Returns in <First> and <Last> the parameter range. If the surface is a plane the curve can be not stored but created a new each time. The flag pointed by <theIsStored> serves to indicate storage status. It is valued if the pointer is non-null.

        Returns the curve associated to the edge in the parametric space of the surface. Returns a NULL handle if this curve does not exist. Returns in <First> and <Last> the parameter range. If the surface is a plane the curve can be not stored but created a new each time. The flag pointed by <theIsStored> serves to indicate storage status. It is valued if the pointer is non-null.

        Returns in <C>, <S>, <L> a 2d curve, a surface and a location for the edge <E>. <C> and <S> are null if the edge has no curve on surface. Returns in <First> and <Last> the parameter range.

        Returns in <C>, <S>, <L> the 2d curve, the surface and the location for the edge <E> of rank <Index>. <C> and <S> are null if the index is out of range. Returns in <First> and <Last> the parameter range.
        """
    @staticmethod
    @overload
    def CurveOnSurface_s(E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,First : float,Last : float,theIsStored : bool=None) -> OCP.Geom2d.Geom2d_Curve: ...
    @staticmethod
    @overload
    def CurveOnSurface_s(E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> Tuple[float, float]: ...
    @staticmethod
    @overload
    def CurveOnSurface_s(E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Index : int) -> Tuple[float, float]: ...
    @staticmethod
    @overload
    def Curve_s(E : OCP.TopoDS.TopoDS_Edge,First : float,Last : float) -> OCP.Geom.Geom_Curve: 
        """
        Returns the 3D curve of the edge. May be a Null handle. Returns in <L> the location for the curve. In <First> and <Last> the parameter range.

        Returns the 3D curve of the edge. May be a Null handle. In <First> and <Last> the parameter range. It can be a copy if there is a Location.
        """
    @staticmethod
    @overload
    def Curve_s(E : OCP.TopoDS.TopoDS_Edge,L : OCP.TopLoc.TopLoc_Location,First : float,Last : float) -> OCP.Geom.Geom_Curve: ...
    @staticmethod
    def Degenerated_s(E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Returns True if the edge is degenerated.
        """
    @staticmethod
    @overload
    def HasContinuity_s(E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the edge is on the surfaces of the two faces.

        Returns True if the edge is on the surfaces.

        Returns True if the edge has regularity on some two surfaces
        """
    @staticmethod
    @overload
    def HasContinuity_s(E : OCP.TopoDS.TopoDS_Edge,S1 : OCP.Geom.Geom_Surface,S2 : OCP.Geom.Geom_Surface,L1 : OCP.TopLoc.TopLoc_Location,L2 : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @staticmethod
    @overload
    def HasContinuity_s(E : OCP.TopoDS.TopoDS_Edge) -> bool: ...
    @staticmethod
    @overload
    def IsClosed_s(E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        If S is Shell, returns True if it has no free boundaries (edges). If S is Wire, returns True if it has no free ends (vertices). (Internal and External sub-shepes are ignored in these checks) If S is Edge, returns True if its vertices are the same. For other shape types returns S.Closed().

        Returns True if <E> has two PCurves in the parametric space of <F>. i.e. <F> is on a closed surface and <E> is on the closing curve.

        Returns True if <E> has two PCurves in the parametric space of <S>. i.e. <S> is a closed surface and <E> is on the closing curve.

        Returns True if <E> has two arrays of indices in the triangulation <T>.
        """
    @staticmethod
    @overload
    def IsClosed_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> bool: ...
    @staticmethod
    @overload
    def IsClosed_s(S : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    @staticmethod
    @overload
    def IsClosed_s(E : OCP.TopoDS.TopoDS_Edge,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> bool: ...
    @staticmethod
    def IsGeometric_s(E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Returns True if <E> is a 3d curve or a curve on surface.
        """
    @staticmethod
    def MaxContinuity_s(theEdge : OCP.TopoDS.TopoDS_Edge) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the max continuity of edge between some surfaces or GeomAbs_C0 if there no such surfaces.
        """
    @staticmethod
    def MaxTolerance_s(theShape : OCP.TopoDS.TopoDS_Shape,theSubShape : OCP.TopAbs.TopAbs_ShapeEnum) -> float: 
        """
        None
        """
    @staticmethod
    def NaturalRestriction_s(F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns the NaturalRestriction flag of the face.
        """
    @staticmethod
    @overload
    def Parameter_s(V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge) -> float: 
        """
        Returns the parameter of <V> on <E>.

        Returns the parameters of the vertex on the pcurve of the edge on the face.

        Returns the parameters of the vertex on the pcurve of the edge on the surface.
        """
    @staticmethod
    @overload
    def Parameter_s(V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> float: ...
    @staticmethod
    @overload
    def Parameter_s(V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> float: ...
    @staticmethod
    def Parameters_s(V : OCP.TopoDS.TopoDS_Vertex,F : OCP.TopoDS.TopoDS_Face) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the parameters of the vertex on the face.
        """
    @staticmethod
    def Pnt_s(V : OCP.TopoDS.TopoDS_Vertex) -> OCP.gp.gp_Pnt: 
        """
        Returns the 3d point.
        """
    @staticmethod
    def Polygon3D_s(E : OCP.TopoDS.TopoDS_Edge,L : OCP.TopLoc.TopLoc_Location) -> OCP.Poly.Poly_Polygon3D: 
        """
        Returns the 3D polygon of the edge. May be a Null handle. Returns in <L> the location for the polygon.
        """
    @staticmethod
    @overload
    def PolygonOnSurface_s(E : OCP.TopoDS.TopoDS_Edge,C : OCP.Poly.Poly_Polygon2D,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Returns the polygon associated to the edge in the parametric space of the face. Returns a NULL handle if this polygon does not exist.

        Returns the polygon associated to the edge in the parametric space of the surface. Returns a NULL handle if this polygon does not exist.

        Returns in <C>, <S>, <L> a 2d curve, a surface and a location for the edge <E>. <C> and <S> are null if the edge has no polygon on surface.

        Returns in <C>, <S>, <L> the 2d curve, the surface and the location for the edge <E> of rank <Index>. <C> and <S> are null if the index is out of range.
        """
    @staticmethod
    @overload
    def PolygonOnSurface_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> OCP.Poly.Poly_Polygon2D: ...
    @staticmethod
    @overload
    def PolygonOnSurface_s(E : OCP.TopoDS.TopoDS_Edge,C : OCP.Poly.Poly_Polygon2D,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Index : int) -> None: ...
    @staticmethod
    @overload
    def PolygonOnSurface_s(E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> OCP.Poly.Poly_Polygon2D: ...
    @staticmethod
    @overload
    def PolygonOnTriangulation_s(E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Returns the polygon associated to the edge in the parametric space of the face. Returns a NULL handle if this polygon does not exist.

        Returns in <P>, <T>, <L> a polygon on triangulation, a triangulation and a location for the edge <E>. <P> and <T> are null if the edge has no polygon on triangulation.

        Returns in <P>, <T>, <L> a polygon on triangulation, a triangulation and a location for the edge <E> for the range index. <C> and <S> are null if the edge has no polygon on triangulation.
        """
    @staticmethod
    @overload
    def PolygonOnTriangulation_s(E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_PolygonOnTriangulation,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location,Index : int) -> None: ...
    @staticmethod
    @overload
    def PolygonOnTriangulation_s(E : OCP.TopoDS.TopoDS_Edge,T : OCP.Poly.Poly_Triangulation,L : OCP.TopLoc.TopLoc_Location) -> OCP.Poly.Poly_PolygonOnTriangulation: ...
    @staticmethod
    @overload
    def Range_s(E : OCP.TopoDS.TopoDS_Edge) -> Tuple[float, float]: 
        """
        Gets the range of the 3d curve.

        Gets the range of the edge on the pcurve on the surface.

        Gets the range of the edge on the pcurve on the face.
        """
    @staticmethod
    @overload
    def Range_s(E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> Tuple[float, float]: ...
    @staticmethod
    @overload
    def Range_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> Tuple[float, float]: ...
    @staticmethod
    def SameParameter_s(E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Returns the SameParameter flag for the edge.
        """
    @staticmethod
    def SameRange_s(E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Returns the SameRange flag for the edge.
        """
    @staticmethod
    @overload
    def SetUVPoints_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,PFirst : OCP.gp.gp_Pnt2d,PLast : OCP.gp.gp_Pnt2d) -> None: 
        """
        Sets the UV locations of the extremities of the edge.

        Sets the UV locations of the extremities of the edge.
        """
    @staticmethod
    @overload
    def SetUVPoints_s(E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,PFirst : OCP.gp.gp_Pnt2d,PLast : OCP.gp.gp_Pnt2d) -> None: ...
    @staticmethod
    @overload
    def Surface_s(F : OCP.TopoDS.TopoDS_Face,L : OCP.TopLoc.TopLoc_Location) -> OCP.Geom.Geom_Surface: 
        """
        Returns the geometric surface of the face. Returns in <L> the location for the surface.

        Returns the geometric surface of the face. It can be a copy if there is a Location.
        """
    @staticmethod
    @overload
    def Surface_s(F : OCP.TopoDS.TopoDS_Face) -> OCP.Geom.Geom_Surface: ...
    @staticmethod
    @overload
    def Tolerance_s(V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        Returns the tolerance of the face.

        Returns the tolerance for <E>.

        Returns the tolerance.
        """
    @staticmethod
    @overload
    def Tolerance_s(F : OCP.TopoDS.TopoDS_Face) -> float: ...
    @staticmethod
    @overload
    def Tolerance_s(E : OCP.TopoDS.TopoDS_Edge) -> float: ...
    @staticmethod
    def Triangulation_s(F : OCP.TopoDS.TopoDS_Face,L : OCP.TopLoc.TopLoc_Location) -> OCP.Poly.Poly_Triangulation: 
        """
        Returns the Triangulation of the face. It is a null handle if there is no triangulation.
        """
    @staticmethod
    @overload
    def UVPoints_s(E : OCP.TopoDS.TopoDS_Edge,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,PFirst : OCP.gp.gp_Pnt2d,PLast : OCP.gp.gp_Pnt2d) -> None: 
        """
        Gets the UV locations of the extremities of the edge.

        Gets the UV locations of the extremities of the edge.
        """
    @staticmethod
    @overload
    def UVPoints_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,PFirst : OCP.gp.gp_Pnt2d,PLast : OCP.gp.gp_Pnt2d) -> None: ...
    def __init__(self) -> None: ...
    pass
