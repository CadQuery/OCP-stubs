import OCP.BRepTools
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.BRep
import OCP.Geom
import OCP.TColgp
import OCP.Bnd
import OCP.TopoDS
import OCP.Standard
import OCP.TopAbs
import OCP.Poly
import OCP.TopTools
import OCP.TCollection
import io
import OCP.GeomAbs
import OCP.gp
import OCP.Geom2d
import OCP.TopLoc
__all__  = [
"BRepTools",
"BRepTools_Modification",
"BRepTools_History",
"BRepTools_MapOfVertexPnt2d",
"BRepTools_GTrsfModification",
"BRepTools_Modifier",
"BRepTools_NurbsConvertModification",
"BRepTools_Quilt",
"BRepTools_ReShape",
"BRepTools_ShapeSet",
"BRepTools_Substitution",
"BRepTools_TrsfModification",
"BRepTools_WireExplorer"
]
class BRepTools():
    """
    The BRepTools package provides utilities for BRep data structures.
    """
    @staticmethod
    @overload
    def AddUVBounds_s(F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge,B : OCP.Bnd.Bnd_Box2d) -> None: 
        """
        Adds to the box <B> the bounding values in the parametric space of F.

        Adds to the box <B> the bounding values of the wire in the parametric space of F.

        Adds to the box <B> the bounding values of the edge in the parametric space of F.
        """
    @staticmethod
    @overload
    def AddUVBounds_s(F : OCP.TopoDS.TopoDS_Face,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    @overload
    def AddUVBounds_s(F : OCP.TopoDS.TopoDS_Face,W : OCP.TopoDS.TopoDS_Wire,B : OCP.Bnd.Bnd_Box2d) -> None: ...
    @staticmethod
    def CleanGeometry_s(theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Removes geometry (curves and surfaces) from all edges and faces of the shape
        """
    @staticmethod
    def Clean_s(S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Removes all cashed polygonal representation of the shape, i.e. the triangulations of the faces of <S> and polygons on triangulations and polygons 3d of the edges. In case polygonal representation is the only available representation for the shape (shape does not have geometry) it is not removed.
        """
    @staticmethod
    @overload
    def Compare_s(V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        Returns True if the distance between the two vertices is lower than their tolerance.

        Returns True if the distance between the two edges is lower than their tolerance.
        """
    @staticmethod
    @overload
    def Compare_s(E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge) -> bool: ...
    @staticmethod
    def DetectClosedness_s(theFace : OCP.TopoDS.TopoDS_Face) -> Tuple[bool, bool]: 
        """
        Detect closedness of face in U and V directions
        """
    @staticmethod
    def Dump_s(Sh : OCP.TopoDS.TopoDS_Shape,S : io.BytesIO) -> None: 
        """
        Dumps the topological structure and the geometry of <Sh> on the stream <S>.
        """
    @staticmethod
    def EvalAndUpdateTol_s(theE : OCP.TopoDS.TopoDS_Edge,theC3d : OCP.Geom.Geom_Curve,theC2d : OCP.Geom2d.Geom2d_Curve,theS : OCP.Geom.Geom_Surface,theF : float,theL : float) -> float: 
        """
        Evals real tolerance of edge <theE>. <theC3d>, <theC2d>, <theS>, <theF>, <theL> are correspondently 3d curve of edge, 2d curve on surface <theS> and rang of edge If calculated tolerance is more then current edge tolerance, edge is updated. Method returns actual tolerance of edge
        """
    @staticmethod
    def IsReallyClosed_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Verifies that the edge <E> is found two times on the face <F> before calling BRep_Tool::IsClosed.
        """
    @staticmethod
    def Map3DEdges_s(S : OCP.TopoDS.TopoDS_Shape,M : OCP.TopTools.TopTools_IndexedMapOfShape) -> None: 
        """
        Stores in the map <M> all the 3D topology edges of <S>.
        """
    @staticmethod
    def OriEdgeInFace_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        returns the cumul of the orientation of <Edge> and thc containing wire in <Face>
        """
    @staticmethod
    def OuterWire_s(F : OCP.TopoDS.TopoDS_Face) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the outer most wire of <F>. Returns a Null wire if <F> has no wires.
        """
    @staticmethod
    @overload
    def Read_s(Sh : OCP.TopoDS.TopoDS_Shape,File : str,B : OCP.BRep.BRep_Builder,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Reads a Shape from <S> in returns it in <Sh>. <B> is used to build the shape.

        Reads a Shape from <File>, returns it in <Sh>. <B> is used to build the shape.
        """
    @staticmethod
    @overload
    def Read_s(Sh : OCP.TopoDS.TopoDS_Shape,S : io.BytesIO,B : OCP.BRep.BRep_Builder,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @staticmethod
    def RemoveInternals_s(theS : OCP.TopoDS.TopoDS_Shape,theForce : bool=False) -> None: 
        """
        Removes internal sub-shapes from the shape. The check on internal status is based on orientation of sub-shapes, classification is not performed. Before removal of internal sub-shapes the algorithm checks if such removal is not going to break topological connectivity between sub-shapes. The flag <theForce> if set to true disables the connectivity check and clears the given shape from all sub-shapes with internal orientation.
        """
    @staticmethod
    def RemoveUnusedPCurves_s(S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Removes all the pcurves of the edges of <S> that refer to surfaces not belonging to any face of <S>
        """
    @staticmethod
    def Triangulation_s(theShape : OCP.TopoDS.TopoDS_Shape,theLinDefl : float,theToCheckFreeEdges : bool=False) -> bool: 
        """
        Verifies that each Face from the shape has got a triangulation with a deflection smaller or equal to specified one and the Edges a discretization on this triangulation.
        """
    @staticmethod
    @overload
    def UVBounds_s(F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge) -> Tuple[float, float, float, float]: 
        """
        Returns in UMin, UMax, VMin, VMax the bounding values in the parametric space of F.

        Returns in UMin, UMax, VMin, VMax the bounding values of the wire in the parametric space of F.

        Returns in UMin, UMax, VMin, VMax the bounding values of the edge in the parametric space of F.
        """
    @staticmethod
    @overload
    def UVBounds_s(F : OCP.TopoDS.TopoDS_Face,W : OCP.TopoDS.TopoDS_Wire) -> Tuple[float, float, float, float]: ...
    @staticmethod
    @overload
    def UVBounds_s(F : OCP.TopoDS.TopoDS_Face) -> Tuple[float, float, float, float]: ...
    @staticmethod
    def UpdateFaceUVPoints_s(theF : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        For each edge of the face <F> reset the UV points to the bounding points of the parametric curve of the edge on the face.
        """
    @staticmethod
    @overload
    def Update_s(S : OCP.TopoDS.TopoDS_Solid) -> None: 
        """
        Update a vertex (nothing is done)

        Update an edge, compute 2d bounding boxes.

        Update a wire (nothing is done)

        Update a Face, update UV points.

        Update a shell (nothing is done)

        Update a solid (nothing is done)

        Update a composite solid (nothing is done)

        Update a compound (nothing is done)

        Update a shape, call the corect update.
        """
    @staticmethod
    @overload
    def Update_s(F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @staticmethod
    @overload
    def Update_s(C : OCP.TopoDS.TopoDS_Compound) -> None: ...
    @staticmethod
    @overload
    def Update_s(E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @staticmethod
    @overload
    def Update_s(S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @staticmethod
    @overload
    def Update_s(V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @staticmethod
    @overload
    def Update_s(C : OCP.TopoDS.TopoDS_CompSolid) -> None: ...
    @staticmethod
    @overload
    def Update_s(W : OCP.TopoDS.TopoDS_Wire) -> None: ...
    @staticmethod
    @overload
    def Update_s(S : OCP.TopoDS.TopoDS_Shell) -> None: ...
    @staticmethod
    @overload
    def Write_s(Sh : OCP.TopoDS.TopoDS_Shape,S : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes <Sh> on <S> in an ASCII format.

        Writes <Sh> in <File>.
        """
    @staticmethod
    @overload
    def Write_s(Sh : OCP.TopoDS.TopoDS_Shape,File : str,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    def __init__(self) -> None: ...
    pass
class BRepTools_Modification(OCP.Standard.Standard_Transient):
    """
    Defines geometric modifications to a shape, i.e. changes to faces, edges and vertices.Defines geometric modifications to a shape, i.e. changes to faces, edges and vertices.Defines geometric modifications to a shape, i.e. changes to faces, edges and vertices.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>. <NewE> is the new edge created from <E>. <NewF1> (resp. <NewF2>) is the new face created from <F1> (resp. <F2>).
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
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns true if the edge, E, has been modified. If the edge has been modified: - C is the new geometry associated with the edge, - L is its new location, and - Tol is the new tolerance. If the edge has not been modified, this function returns false, and the values of C, L and Tol are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns true if the edge, E, has a new curve on surface on the face, F. If a new curve exists: - C is the new geometry of the edge, - L is the new location, and - Tol is the new tolerance. NewE is the new edge created from E, and NewF is the new face created from F. If there is no new curve on the face, this function returns false, and the values of C, L and Tol are not significant.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Returns true if the vertex V has a new parameter on the edge E. If a new parameter exists: - P is the parameter, and - Tol is the new tolerance. If there is no new parameter this function returns false, and the values of P and Tol are not significant.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Returns true if the vertex V has been modified. If V has been modified: - P is the new geometry of the vertex, and - Tol is the new tolerance. If the vertex has not been modified this function returns false, and the values of P and Tol are not significant.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns true if the face, F, has been modified. If the face has been modified: - S is the new geometry of the face, - L is its new location, and - Tol is the new tolerance. The flag, RevWires, is set to true when the modification reverses the normal of the surface, (i.e. the wires have to be reversed). The flag, RevFace, is set to true if the orientation of the modified face changes in the shells which contain it. If the face has not been modified this function returns false, and the values of S, L, Tol, RevWires and RevFace are not significant.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
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
class BRepTools_History(OCP.Standard.Standard_Transient):
    """
    The history keeps the following relations between the input shapes (S1, ..., Sm) and output shapes (T1, ..., Tn): 1) an output shape Tj is generated from an input shape Si: Tj <= G(Si); 2) a output shape Tj is modified from an input shape Si: Tj <= M(Si); 3) an input shape (Si) is removed: R(Si) == 1.The history keeps the following relations between the input shapes (S1, ..., Sm) and output shapes (T1, ..., Tn): 1) an output shape Tj is generated from an input shape Si: Tj <= G(Si); 2) a output shape Tj is modified from an input shape Si: Tj <= M(Si); 3) an input shape (Si) is removed: R(Si) == 1.The history keeps the following relations between the input shapes (S1, ..., Sm) and output shapes (T1, ..., Tn): 1) an output shape Tj is generated from an input shape Si: Tj <= G(Si); 2) a output shape Tj is modified from an input shape Si: Tj <= M(Si); 3) an input shape (Si) is removed: R(Si) == 1.
    """
    class TRelationType_e():
        """
        The types of the historical relations.

        Members:

          TRelationType_Removed

          TRelationType_Generated

          TRelationType_Modified
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
        TRelationType_Generated: OCP.BRepTools.TRelationType_e # value = <TRelationType_e.TRelationType_Generated: 1>
        TRelationType_Modified: OCP.BRepTools.TRelationType_e # value = <TRelationType_e.TRelationType_Modified: 2>
        TRelationType_Removed: OCP.BRepTools.TRelationType_e # value = <TRelationType_e.TRelationType_Removed: 0>
        __entries: dict # value = {'TRelationType_Removed': (<TRelationType_e.TRelationType_Removed: 0>, None), 'TRelationType_Generated': (<TRelationType_e.TRelationType_Generated: 1>, None), 'TRelationType_Modified': (<TRelationType_e.TRelationType_Modified: 2>, None)}
        __members__: dict # value = {'TRelationType_Removed': <TRelationType_e.TRelationType_Removed: 0>, 'TRelationType_Generated': <TRelationType_e.TRelationType_Generated: 1>, 'TRelationType_Modified': <TRelationType_e.TRelationType_Modified: 2>}
        pass
    def AddGenerated(self,theInitial : OCP.TopoDS.TopoDS_Shape,theGenerated : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set the second shape as generated one from the first shape.
        """
    def AddModified(self,theInitial : OCP.TopoDS.TopoDS_Shape,theModified : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set the second shape as modified one from the first shape.
        """
    def Clear(self) -> None: 
        """
        Clears the history.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,theS : io.BytesIO) -> None: 
        """
        Prints the brief description of the history into a stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Generated(self,theInitial : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns all shapes generated from the shape.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasGenerated(self) -> bool: 
        """
        Returns 'true' if there any shapes with Generated elements present
        """
    def HasModified(self) -> bool: 
        """
        Returns 'true' if there any Modified shapes present
        """
    def HasRemoved(self) -> bool: 
        """
        Returns 'true' if there any removed shapes present
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
    def IsRemoved(self,theInitial : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns 'true' if the shape is removed.
        """
    @staticmethod
    def IsSupportedType_s(theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns 'true' if the type of the shape is supported by the history.
        """
    def Merge(self,theHistory23 : BRepTools_History) -> None: 
        """
        Merges the next history to this history.

        Merges the next history to this history.
        """
    def Modified(self,theInitial : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns all shapes modified from the shape.
        """
    def Remove(self,theRemoved : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set the shape as removed one.
        """
    def ReplaceGenerated(self,theInitial : OCP.TopoDS.TopoDS_Shape,theGenerated : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set the second shape as the only generated one from the first one.
        """
    def ReplaceModified(self,theInitial : OCP.TopoDS.TopoDS_Shape,theModified : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set the second shape as the only modified one from the first one.
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
    TRelationType_Generated: OCP.BRepTools.TRelationType_e # value = <TRelationType_e.TRelationType_Generated: 1>
    TRelationType_Modified: OCP.BRepTools.TRelationType_e # value = <TRelationType_e.TRelationType_Modified: 2>
    TRelationType_Removed: OCP.BRepTools.TRelationType_e # value = <TRelationType_e.TRelationType_Removed: 0>
    pass
class BRepTools_MapOfVertexPnt2d(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepTools_MapOfVertexPnt2d) -> BRepTools_MapOfVertexPnt2d: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColgp.TColgp_SequenceOfPnt2d) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColgp.TColgp_SequenceOfPnt2d) -> OCP.TColgp.TColgp_SequenceOfPnt2d: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColgp.TColgp_SequenceOfPnt2d: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColgp.TColgp_SequenceOfPnt2d: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : BRepTools_MapOfVertexPnt2d) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TColgp.TColgp_SequenceOfPnt2d) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColgp.TColgp_SequenceOfPnt2d: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        IsBound
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColgp.TColgp_SequenceOfPnt2d: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BRepTools_MapOfVertexPnt2d) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepTools_GTrsfModification(BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    Defines a modification of the geometry by a GTrsf from gp. All methods return True and transform the geometry.Defines a modification of the geometry by a GTrsf from gp. All methods return True and transform the geometry.Defines a modification of the geometry by a GTrsf from gp. All methods return True and transform the geometry.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>.
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
    def GTrsf(self) -> OCP.gp.gp_GTrsf: 
        """
        Gives an access on the GTrsf.
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
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has been modified. In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has a new curve on surface on the face <F>.In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Returns Standard_True if the Vertex <V> has a new parameter on the edge <E>. In this case, <P> is the parameter, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Returns Standard_True if the vertex <V> has been modified. In this case, <P> is the new geometric support of the vertex, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns Standard_True if the face <F> has been modified. In this case, <S> is the new geometric support of the face, <L> the new location,<Tol> the new tolerance.<RevWires> has to be set to Standard_True when the modification reverses the normal of the surface.(the wires have to be reversed). <RevFace> has to be set to Standard_True if the orientation of the modified face changes in the shells which contain it. -- Here, <RevFace> will return Standard_True if the -- gp_Trsf is negative.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,T : OCP.gp.gp_GTrsf) -> None: ...
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
class BRepTools_Modifier():
    """
    Performs geometric modifications on a shape.
    """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes the modifier with the shape <S>.
        """
    def IsDone(self) -> bool: 
        """
        Returns Standard_True if the modification has been computed successfully.

        Returns Standard_True if the modification has been computed successfully.
        """
    def IsMutableInput(self) -> bool: 
        """
        Returns the current mutable input state
        """
    def ModifiedShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the modified shape corresponding to <S>.

        Returns the modified shape corresponding to <S>.
        """
    def Perform(self,M : BRepTools_Modification,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the modifications described by <M>.
        """
    def SetMutableInput(self,theMutableInput : bool) -> None: 
        """
        Sets the mutable input state If true then the input (original) shape can be modified during modification process
        """
    @overload
    def __init__(self,theMutableInput : bool=False) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,M : BRepTools_Modification) -> None: ...
    pass
class BRepTools_NurbsConvertModification(BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    Defines a modification of the geometry by a Trsf from gp. All methods return True and transform the geometry.Defines a modification of the geometry by a Trsf from gp. All methods return True and transform the geometry.Defines a modification of the geometry by a Trsf from gp. All methods return True and transform the geometry.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>.
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
    def GetUpdatedEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
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
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has been modified. In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has a new curve on surface on the face <F>.In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Returns Standard_True if the Vertex <V> has a new parameter on the edge <E>. In this case, <P> is the parameter, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Returns Standard_True if the vertex <V> has been modified. In this case, <P> is the new geometric support of the vertex, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns Standard_True if the face <F> has been modified. In this case, <S> is the new geometric support of the face, <L> the new location,<Tol> the new tolerance.<RevWires> has to be set to Standard_True when the modification reverses the normal of the surface.(the wires have to be reversed). <RevFace> has to be set to Standard_True if the orientation of the modified face changes in the shells which contain it. -- Here, <RevFace> will return Standard_True if the -- gp_Trsf is negative.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
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
class BRepTools_Quilt():
    """
    A Tool to glue faces at common edges and reconstruct shells.
    """
    def Add(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Add the faces of <S> to the Quilt, the faces containing bounded edges are copied.
        """
    @overload
    def Bind(self,Eold : OCP.TopoDS.TopoDS_Edge,Enew : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Binds <Enew> to be the new edge instead of <Eold>.

        Binds <VNew> to be a new vertex instead of <Vold>.
        """
    @overload
    def Bind(self,Vold : OCP.TopoDS.TopoDS_Vertex,Vnew : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    def Copy(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape substitued to <S> in the Quilt.
        """
    def IsCopied(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns True if <S> has been copied (<S> is a vertex, an edge or a face)
        """
    def Shells(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a Compound of shells made from the current set of faces. The shells will be flagged as closed or not closed.
        """
    def __init__(self) -> None: ...
    pass
class BRepTools_ReShape(OCP.Standard.Standard_Transient):
    """
    Rebuilds a Shape by making pre-defined substitutions on some of its componentsRebuilds a Shape by making pre-defined substitutions on some of its componentsRebuilds a Shape by making pre-defined substitutions on some of its components
    """
    def Apply(self,shape : OCP.TopoDS.TopoDS_Shape,until : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Applies the substitutions requests to a shape.
        """
    def Clear(self) -> None: 
        """
        Clears all substitutions requests
        """
    @overload
    def CopyVertex(self,theV : OCP.TopoDS.TopoDS_Vertex,theTol : float=-1.0) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None

        None
        """
    @overload
    def CopyVertex(self,theV : OCP.TopoDS.TopoDS_Vertex,theNewPos : OCP.gp.gp_Pnt,aTol : float) -> OCP.TopoDS.TopoDS_Vertex: ...
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
    def History(self) -> BRepTools_History: 
        """
        Returns the history of the substituted shapes.
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
    def IsNewShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsRecorded(self,shape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Tells if a shape is recorded for Replace/Remove
        """
    def Remove(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets a request to Remove a Shape whatever the orientation
        """
    def Replace(self,shape : OCP.TopoDS.TopoDS_Shape,newshape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets a request to Replace a Shape by a new one.
        """
    def Status(self,shape : OCP.TopoDS.TopoDS_Shape,newsh : OCP.TopoDS.TopoDS_Shape,last : bool=False) -> int: 
        """
        Returns a complete substitution status for a shape 0 : not recorded, <newsh> = original <shape> < 0: to be removed, <newsh> is NULL > 0: to be replaced, <newsh> is a new item If <last> is False, returns status and new shape recorded in the map directly for the shape, if True and status > 0 then recursively searches for the last status and new shape.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,shape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the new value for an individual shape If not recorded, returns the original shape itself If to be Removed, returns a Null Shape Else, returns the replacing item
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
    def ModeConsiderLocation(self) -> bool:
        """
        :type: bool
        """
    @ModeConsiderLocation.setter
    def ModeConsiderLocation(self, arg1: bool) -> None:
        pass
    pass
class BRepTools_ShapeSet(OCP.TopTools.TopTools_ShapeSet):
    """
    Contains a Shape and all its subshapes, locations and geometries.
    """
    def Add(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Stores <S> and its sub-shape. Returns the index of <S>. The method AddGeometry is called on each sub-shape.
        """
    def AddGeometry(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Stores the goemetry of <S>.
        """
    def AddShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Inserts the shape <S2> in the shape <S1>. This method must be redefined to use the correct builder.
        """
    def ChangeLocations(self) -> OCP.TopTools.TopTools_LocationSet: 
        """
        None
        """
    def Check(self,T : OCP.TopAbs.TopAbs_ShapeEnum,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    @overload
    def Dump(self,OS : io.BytesIO) -> None: 
        """
        Dumps the content of me on the stream <OS>.

        Dumps on <OS> the shape <S>. Dumps the orientation, the index of the TShape and the index of the Location.
        """
    @overload
    def Dump(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: ...
    @overload
    def DumpExtent(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the number of objects in me on the stream <OS>. (Number of shapes of each type)

        Dumps the number of objects in me in the string S (Number of shapes of each type)
        """
    @overload
    def DumpExtent(self,S : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def DumpGeometry(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: 
        """
        Dumps the geometry of me on the stream <OS>.

        Dumps the geometry of <S> on the stream <OS>.
        """
    @overload
    def DumpGeometry(self,OS : io.BytesIO) -> None: ...
    def DumpPolygon3D(self,OS : io.BytesIO) -> None: 
        """
        Dumps the 3d polygons on the stream <OS>.
        """
    def DumpPolygonOnTriangulation(self,OS : io.BytesIO) -> None: 
        """
        Dumps the polygons on triangulation on the stream <OS>.
        """
    def DumpTriangulation(self,OS : io.BytesIO) -> None: 
        """
        Dumps the triangulation on the stream <OS>.
        """
    def FormatNb(self) -> int: 
        """
        two formats available for the moment: First: does not write CurveOnSurface UV Points into the file on reading calls Check() method. Second: stores CurveOnSurface UV Points. On reading format is recognized from Version string.
        """
    def Index(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Returns the index of <S>.
        """
    def Locations(self) -> OCP.TopTools.TopTools_LocationSet: 
        """
        None
        """
    def NbShapes(self) -> int: 
        """
        Returns number of shapes read from file.
        """
    @overload
    def Read(self,S : OCP.TopoDS.TopoDS_Shape,IS : io.BytesIO) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.

        Reads from <IS> a shape and returns it in S.
        """
    @overload
    def Read(self,IS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def ReadGeometry(self,T : OCP.TopAbs.TopAbs_ShapeEnum,IS : io.BytesIO,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Reads the geometry of me from the stream <IS>.

        Reads the geometry of a shape of type <T> from the stream <IS> and returns it in <S>.
        """
    @overload
    def ReadGeometry(self,IS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def ReadPolygon3D(self,IS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the 3d polygons of me from the stream <IS>.
        """
    def ReadPolygonOnTriangulation(self,IS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the polygons on triangulation of me from the stream <IS>.
        """
    def ReadTriangulation(self,IS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the triangulation of me from the stream <IS>.
        """
    def SetFormatNb(self,theFormatNb : int) -> None: 
        """
        None
        """
    def Shape(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the sub-shape of index <I>.
        """
    @overload
    def Write(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: 
        """
        Writes the content of me on the stream <OS> in a format that can be read back by Read.

        Writes on <OS> the shape <S>. Writes the orientation, the index of the TShape and the index of the Location.
        """
    @overload
    def Write(self,OS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def WriteGeometry(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: 
        """
        Writes the geometry of me on the stream <OS> in a format that can be read back by Read.

        Writes the geometry of <S> on the stream <OS> in a format that can be read back by Read.
        """
    @overload
    def WriteGeometry(self,OS : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def WritePolygon3D(self,OS : io.BytesIO,Compact : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the 3d polygons on the stream <OS> in a format that can be read back by Read.
        """
    def WritePolygonOnTriangulation(self,OS : io.BytesIO,Compact : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the polygons on triangulation on the stream <OS> in a format that can be read back by Read.
        """
    def WriteTriangulation(self,OS : io.BytesIO,Compact : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the triangulation on the stream <OS> in a format that can be read back by Read.
        """
    @overload
    def __init__(self,B : OCP.BRep.BRep_Builder,isWithTriangles : bool=True) -> None: ...
    @overload
    def __init__(self,isWithTriangles : bool=True) -> None: ...
    pass
class BRepTools_Substitution():
    """
    A tool to substitute subshapes by other shapes.
    """
    def Build(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Build NewShape from <S> if its subshapes has modified.
        """
    def Clear(self) -> None: 
        """
        Reset all the fields.
        """
    def Copy(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the set of shapes substitued to <S> .
        """
    def IsCopied(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns True if <S> has been replaced .
        """
    def Substitute(self,OldShape : OCP.TopoDS.TopoDS_Shape,NewShapes : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        <Oldshape> will be replaced by <NewShapes>.
        """
    def __init__(self) -> None: ...
    pass
class BRepTools_TrsfModification(BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    Describes a modification that uses a gp_Trsf to change the geometry of a shape. All functions return true and transform the geometry of the shape.Describes a modification that uses a gp_Trsf to change the geometry of a shape. All functions return true and transform the geometry of the shape.Describes a modification that uses a gp_Trsf to change the geometry of a shape. All functions return true and transform the geometry of the shape.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>.
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
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns true if the edge E has been modified. If the edge has been modified: - C is the new geometric support of the edge, - L is the new location, and - Tol is the new tolerance. If the edge has not been modified, this function returns false, and the values of C, L and Tol are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns true if the edge E has a new curve on surface on the face F. If a new curve exists: - C is the new geometric support of the edge, - L is the new location, and - Tol the new tolerance. If no new curve exists, this function returns false, and the values of C, L and Tol are not significant.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Returns true if the Vertex V has a new parameter on the edge E. If a new parameter exists: - P is the parameter, and - Tol is the new tolerance. If no new parameter exists, this function returns false, and the values of P and Tol are not significant.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Returns true if the vertex V has been modified. If the vertex has been modified: - P is the new geometry of the vertex, and - Tol is the new tolerance. If the vertex has not been modified this function returns false, and the values of P and Tol are not significant.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns true if the face F has been modified. If the face has been modified: - S is the new geometry of the face, - L is its new location, and - Tol is the new tolerance. RevWires is set to true when the modification reverses the normal of the surface (the wires have to be reversed). RevFace is set to true if the orientation of the modified face changes in the shells which contain it. For this class, RevFace returns true if the gp_Trsf associated with this modification is negative.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trsf(self) -> OCP.gp.gp_Trsf: 
        """
        Provides access to the gp_Trsf associated with this modification. The transformation can be changed.
        """
    def __init__(self,T : OCP.gp.gp_Trsf) -> None: ...
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
class BRepTools_WireExplorer():
    """
    The WireExplorer is a tool to explore the edges of a wire in a connection order.
    """
    def Clear(self) -> None: 
        """
        Clears the content of the explorer.
        """
    def Current(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the current edge.
        """
    def CurrentVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex connecting the current edge to the previous one.
        """
    @overload
    def Init(self,W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face,UMin : float,UMax : float,VMin : float,VMax : float) -> None: 
        """
        Initializes an exploration of the wire <W>.

        Initializes an exploration of the wire <W>. F is used to select the edge connected to the previous in the parametric representation of <F>.

        Initializes an exploration of the wire <W>. F is used to select the edge connected to the previous in the parametric representation of <F>. <UMIn>, <UMax>, <VMin>, <VMax> - the UV bounds of the face <F>.
        """
    @overload
    def Init(self,W : OCP.TopoDS.TopoDS_Wire) -> None: ...
    @overload
    def Init(self,W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    def More(self) -> bool: 
        """
        Returns True if there is a current edge.
        """
    def Next(self) -> None: 
        """
        Proceeds to the next edge.
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns an Orientation for the current edge.
        """
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
