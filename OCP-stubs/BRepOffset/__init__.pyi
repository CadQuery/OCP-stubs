import OCP.BRepOffset
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.TCollection
import OCP.GeomAbs
import OCP.Poly
import OCP.Geom2d
import OCP.BRepAlgo
import OCP.TopTools
import OCP.TopLoc
import OCP.Standard
import OCP.TopoDS
import OCP.Geom
import OCP.NCollection
import OCP.BRepTools
import OCP.gp
__all__  = [
"BRepOffset",
"BRepOffsetSimple_Status",
"BRepOffset_Analyse",
"BRepOffset_DataMapOfShapeListOfInterval",
"BRepOffset_DataMapOfShapeMapOfShape",
"BRepOffset_DataMapOfShapeOffset",
"BRepOffset_Error",
"BRepOffset_Inter2d",
"BRepOffset_Inter3d",
"BRepOffset_Interval",
"BRepOffset_ListOfInterval",
"BRepOffset_MakeLoops",
"BRepOffset_MakeOffset",
"BRepOffset_MakeSimpleOffset",
"BRepOffset_Mode",
"BRepOffset_Offset",
"BRepOffset_SimpleOffset",
"BRepOffset_Status",
"BRepOffset_Tool",
"BRepOffset_Type",
"BRepOffsetSimple_ErrorInvalidNbShells",
"BRepOffsetSimple_ErrorNonClosedShell",
"BRepOffsetSimple_ErrorOffsetComputation",
"BRepOffsetSimple_ErrorWallFaceComputation",
"BRepOffsetSimple_NullInputShape",
"BRepOffsetSimple_OK",
"BRepOffset_BadNormalsOnGeometry",
"BRepOffset_C0Geometry",
"BRepOffset_Concave",
"BRepOffset_Convex",
"BRepOffset_Degenerated",
"BRepOffset_FreeBoundary",
"BRepOffset_Good",
"BRepOffset_NoError",
"BRepOffset_NotConnectedShell",
"BRepOffset_NullOffset",
"BRepOffset_Other",
"BRepOffset_Pipe",
"BRepOffset_RectoVerso",
"BRepOffset_Reversed",
"BRepOffset_Skin",
"BRepOffset_Tangent",
"BRepOffset_Unknown",
"BRepOffset_UnknownError"
]
class BRepOffset():
    """
    Auxiliary tools for offset algorithms
    """
    @staticmethod
    def CollapseSingularities_s(theSurface : OCP.Geom.Geom_Surface,theFace : OCP.TopoDS.TopoDS_Face,thePrecision : float) -> OCP.Geom.Geom_Surface: 
        """
        Preprocess surface to be offset (bspline, bezier, or revolution based on bspline or bezier curve), by collapsing each singular side to single point.
        """
    @staticmethod
    def Surface_s(Surface : OCP.Geom.Geom_Surface,Offset : float,theStatus : BRepOffset_Status,allowC0 : bool=False) -> OCP.Geom.Geom_Surface: 
        """
        returns the Offset surface computed from the surface <Surface> at an OffsetDistance <Offset>.
        """
    def __init__(self) -> None: ...
    pass
class BRepOffsetSimple_Status():
    """
    None

    Members:

      BRepOffsetSimple_OK

      BRepOffsetSimple_NullInputShape

      BRepOffsetSimple_ErrorOffsetComputation

      BRepOffsetSimple_ErrorWallFaceComputation

      BRepOffsetSimple_ErrorInvalidNbShells

      BRepOffsetSimple_ErrorNonClosedShell
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
    BRepOffsetSimple_ErrorInvalidNbShells: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_ErrorInvalidNbShells
    BRepOffsetSimple_ErrorNonClosedShell: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_ErrorNonClosedShell
    BRepOffsetSimple_ErrorOffsetComputation: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_ErrorOffsetComputation
    BRepOffsetSimple_ErrorWallFaceComputation: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_ErrorWallFaceComputation
    BRepOffsetSimple_NullInputShape: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_NullInputShape
    BRepOffsetSimple_OK: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_OK
    __entries: dict # value = {'BRepOffsetSimple_OK': (BRepOffsetSimple_Status.BRepOffsetSimple_OK, None), 'BRepOffsetSimple_NullInputShape': (BRepOffsetSimple_Status.BRepOffsetSimple_NullInputShape, None), 'BRepOffsetSimple_ErrorOffsetComputation': (BRepOffsetSimple_Status.BRepOffsetSimple_ErrorOffsetComputation, None), 'BRepOffsetSimple_ErrorWallFaceComputation': (BRepOffsetSimple_Status.BRepOffsetSimple_ErrorWallFaceComputation, None), 'BRepOffsetSimple_ErrorInvalidNbShells': (BRepOffsetSimple_Status.BRepOffsetSimple_ErrorInvalidNbShells, None), 'BRepOffsetSimple_ErrorNonClosedShell': (BRepOffsetSimple_Status.BRepOffsetSimple_ErrorNonClosedShell, None)}
    __members__: dict # value = {'BRepOffsetSimple_OK': BRepOffsetSimple_Status.BRepOffsetSimple_OK, 'BRepOffsetSimple_NullInputShape': BRepOffsetSimple_Status.BRepOffsetSimple_NullInputShape, 'BRepOffsetSimple_ErrorOffsetComputation': BRepOffsetSimple_Status.BRepOffsetSimple_ErrorOffsetComputation, 'BRepOffsetSimple_ErrorWallFaceComputation': BRepOffsetSimple_Status.BRepOffsetSimple_ErrorWallFaceComputation, 'BRepOffsetSimple_ErrorInvalidNbShells': BRepOffsetSimple_Status.BRepOffsetSimple_ErrorInvalidNbShells, 'BRepOffsetSimple_ErrorNonClosedShell': BRepOffsetSimple_Status.BRepOffsetSimple_ErrorNonClosedShell}
    pass
class BRepOffset_Analyse():
    """
    Analyse of a shape consit to Find the part of edges convex concave tangent.
    """
    @overload
    def AddFaces(self,Face : OCP.TopoDS.TopoDS_Face,Co : OCP.TopoDS.TopoDS_Compound,Map : OCP.TopTools.TopTools_MapOfShape,Type : BRepOffset_Type) -> None: 
        """
        Add in <CO> the faces of the shell containing <Face> where all the connex edges are of type <Side>.

        Add in <CO> the faces of the shell containing <Face> where all the connex edges are of type <Side1> or <Side2>.
        """
    @overload
    def AddFaces(self,Face : OCP.TopoDS.TopoDS_Face,Co : OCP.TopoDS.TopoDS_Compound,Map : OCP.TopTools.TopTools_MapOfShape,Type1 : BRepOffset_Type,Type2 : BRepOffset_Type) -> None: ...
    def Ancestors(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    @overload
    def Edges(self,V : OCP.TopoDS.TopoDS_Vertex,T : BRepOffset_Type,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Stores in <L> all the edges of Type <T> on the vertex <V>.

        Stores in <L> all the edges of Type <T> on the face <F>.
        """
    @overload
    def Edges(self,F : OCP.TopoDS.TopoDS_Face,T : BRepOffset_Type,L : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    @overload
    def Explode(self,L : OCP.TopTools.TopTools_ListOfShape,Type1 : BRepOffset_Type,Type2 : BRepOffset_Type) -> None: 
        """
        Explode in compounds of faces where all the connex edges are of type <Side>

        Explode in compounds of faces where all the connex edges are of type <Side1> or <Side2>
        """
    @overload
    def Explode(self,L : OCP.TopTools.TopTools_ListOfShape,Type : BRepOffset_Type) -> None: ...
    def HasAncestor(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Perform(self,S : OCP.TopoDS.TopoDS_Shape,Angle : float) -> None: 
        """
        None
        """
    def TangentEdges(self,Edge : OCP.TopoDS.TopoDS_Edge,Vertex : OCP.TopoDS.TopoDS_Vertex,Edges : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        set in <Edges> all the Edges of <Shape> which are tangent to <Edge> at the vertex <Vertex>.
        """
    def Type(self,E : OCP.TopoDS.TopoDS_Edge) -> BRepOffset_ListOfInterval: 
        """
        None
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,Angle : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepOffset_DataMapOfShapeListOfInterval(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepOffset_DataMapOfShapeListOfInterval) -> BRepOffset_DataMapOfShapeListOfInterval: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BRepOffset_ListOfInterval) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BRepOffset_ListOfInterval) -> BRepOffset_ListOfInterval: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepOffset_ListOfInterval: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepOffset_ListOfInterval: 
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
    def Exchange(self,theOther : BRepOffset_DataMapOfShapeListOfInterval) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : BRepOffset_ListOfInterval) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepOffset_ListOfInterval: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepOffset_ListOfInterval: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BRepOffset_DataMapOfShapeListOfInterval) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BRepOffset_DataMapOfShapeMapOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepOffset_DataMapOfShapeMapOfShape) -> BRepOffset_DataMapOfShapeMapOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopTools.TopTools_MapOfShape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopTools.TopTools_MapOfShape) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_MapOfShape: 
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
    def Exchange(self,theOther : BRepOffset_DataMapOfShapeMapOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TopTools.TopTools_MapOfShape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_MapOfShape: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_MapOfShape: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
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
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BRepOffset_DataMapOfShapeMapOfShape) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BRepOffset_DataMapOfShapeOffset(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepOffset_DataMapOfShapeOffset) -> BRepOffset_DataMapOfShapeOffset: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BRepOffset_Offset) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BRepOffset_Offset) -> BRepOffset_Offset: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepOffset_Offset: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepOffset_Offset: 
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
    def Exchange(self,theOther : BRepOffset_DataMapOfShapeOffset) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : BRepOffset_Offset) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepOffset_Offset: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepOffset_Offset: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
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
    def __init__(self,theOther : BRepOffset_DataMapOfShapeOffset) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BRepOffset_Error():
    """
    None

    Members:

      BRepOffset_NoError

      BRepOffset_UnknownError

      BRepOffset_BadNormalsOnGeometry

      BRepOffset_C0Geometry

      BRepOffset_NullOffset

      BRepOffset_NotConnectedShell
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
    BRepOffset_BadNormalsOnGeometry: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_BadNormalsOnGeometry
    BRepOffset_C0Geometry: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_C0Geometry
    BRepOffset_NoError: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_NoError
    BRepOffset_NotConnectedShell: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_NotConnectedShell
    BRepOffset_NullOffset: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_NullOffset
    BRepOffset_UnknownError: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_UnknownError
    __entries: dict # value = {'BRepOffset_NoError': (BRepOffset_Error.BRepOffset_NoError, None), 'BRepOffset_UnknownError': (BRepOffset_Error.BRepOffset_UnknownError, None), 'BRepOffset_BadNormalsOnGeometry': (BRepOffset_Error.BRepOffset_BadNormalsOnGeometry, None), 'BRepOffset_C0Geometry': (BRepOffset_Error.BRepOffset_C0Geometry, None), 'BRepOffset_NullOffset': (BRepOffset_Error.BRepOffset_NullOffset, None), 'BRepOffset_NotConnectedShell': (BRepOffset_Error.BRepOffset_NotConnectedShell, None)}
    __members__: dict # value = {'BRepOffset_NoError': BRepOffset_Error.BRepOffset_NoError, 'BRepOffset_UnknownError': BRepOffset_Error.BRepOffset_UnknownError, 'BRepOffset_BadNormalsOnGeometry': BRepOffset_Error.BRepOffset_BadNormalsOnGeometry, 'BRepOffset_C0Geometry': BRepOffset_Error.BRepOffset_C0Geometry, 'BRepOffset_NullOffset': BRepOffset_Error.BRepOffset_NullOffset, 'BRepOffset_NotConnectedShell': BRepOffset_Error.BRepOffset_NotConnectedShell}
    pass
class BRepOffset_Inter2d():
    """
    Computes the intersections betwwen edges on a face stores result is SD as AsDes from BRepOffset.
    """
    @staticmethod
    def Compute_s(AsDes : OCP.BRepAlgo.BRepAlgo_AsDes,F : OCP.TopoDS.TopoDS_Face,NewEdges : OCP.TopTools.TopTools_IndexedMapOfShape,Tol : float,theDMVV : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape) -> None: 
        """
        Computes the intersections between the edges stored is AsDes as descendants of <F> . Intersections is computed between two edges if one of them is bound in NewEdges. When all faces of the shape are treated the intersection vertices have to be fused using the FuseVertices method. theDMVV contains the vertices that should be fused
        """
    @staticmethod
    def ConnexIntByIntInVert_s(FI : OCP.TopoDS.TopoDS_Face,OFI : BRepOffset_Offset,MES : OCP.TopTools.TopTools_DataMapOfShapeShape,Build : OCP.TopTools.TopTools_DataMapOfShapeShape,AsDes : OCP.BRepAlgo.BRepAlgo_AsDes,AsDes2d : OCP.BRepAlgo.BRepAlgo_AsDes,Tol : float,theDMVV : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape) -> None: 
        """
        Computes the intersection between the offset edges generated from vertices and stored into AsDes as descendants of the <FI>. All intersection vertices will be stored in AsDes2d. When all faces of the shape are treated the intersection vertices have to be fused using the FuseVertices method. theDMVV contains the vertices that should be fused.
        """
    @staticmethod
    def ConnexIntByInt_s(FI : OCP.TopoDS.TopoDS_Face,OFI : BRepOffset_Offset,MES : OCP.TopTools.TopTools_DataMapOfShapeShape,Build : OCP.TopTools.TopTools_DataMapOfShapeShape,AsDes2d : OCP.BRepAlgo.BRepAlgo_AsDes,Offset : float,Tol : float,FacesWithVerts : OCP.TopTools.TopTools_IndexedMapOfShape,theDMVV : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape) -> None: 
        """
        Computes the intersection between the offset edges of the <FI>. All intersection vertices will be stored in AsDes2d. When all faces of the shape are treated the intersection vertices have to be fused using the FuseVertices method. theDMVV contains the vertices that should be fused.
        """
    @staticmethod
    def FuseVertices_s(theDMVV : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape,theAsDes : OCP.BRepAlgo.BRepAlgo_AsDes) -> None: 
        """
        Fuses the chains of vertices in the theDMVV and updates AsDes by replacing the old vertices with the new ones.
        """
    def __init__(self) -> None: ...
    pass
class BRepOffset_Inter3d():
    """
    Computes the intersection face face in a set of faces Store the result in a SD as AsDes.
    """
    def AddCommonEdges(self,SetOfFaces : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def AsDes(self) -> OCP.BRepAlgo.BRepAlgo_AsDes: 
        """
        None
        """
    def CompletInt(self,SetOfFaces : OCP.TopTools.TopTools_ListOfShape,InitOffsetFace : OCP.BRepAlgo.BRepAlgo_Image) -> None: 
        """
        None
        """
    def ConnexIntByArc(self,SetOfFaces : OCP.TopTools.TopTools_ListOfShape,ShapeInit : OCP.TopoDS.TopoDS_Shape,Analyse : BRepOffset_Analyse,InitOffsetFace : OCP.BRepAlgo.BRepAlgo_Image) -> None: 
        """
        None
        """
    def ConnexIntByInt(self,SI : OCP.TopoDS.TopoDS_Shape,MapSF : BRepOffset_DataMapOfShapeOffset,A : BRepOffset_Analyse,MES : OCP.TopTools.TopTools_DataMapOfShapeShape,Build : OCP.TopTools.TopTools_DataMapOfShapeShape,Failed : OCP.TopTools.TopTools_ListOfShape,bIsPlanar : bool=False) -> None: 
        """
        None
        """
    def ContextIntByArc(self,ContextFaces : OCP.TopTools.TopTools_IndexedMapOfShape,ExtentContext : bool,Analyse : BRepOffset_Analyse,InitOffsetFace : OCP.BRepAlgo.BRepAlgo_Image,InitOffsetEdge : OCP.BRepAlgo.BRepAlgo_Image) -> None: 
        """
        None
        """
    def ContextIntByInt(self,ContextFaces : OCP.TopTools.TopTools_IndexedMapOfShape,ExtentContext : bool,MapSF : BRepOffset_DataMapOfShapeOffset,A : BRepOffset_Analyse,MES : OCP.TopTools.TopTools_DataMapOfShapeShape,Build : OCP.TopTools.TopTools_DataMapOfShapeShape,Failed : OCP.TopTools.TopTools_ListOfShape,bIsPlanar : bool=False) -> None: 
        """
        None
        """
    def FaceInter(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,InitOffsetFace : OCP.BRepAlgo.BRepAlgo_Image) -> None: 
        """
        None
        """
    def IsDone(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def NewEdges(self) -> OCP.TopTools.TopTools_IndexedMapOfShape: 
        """
        None
        """
    def SetDone(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def TouchedFaces(self) -> OCP.TopTools.TopTools_IndexedMapOfShape: 
        """
        None
        """
    def __init__(self,AsDes : OCP.BRepAlgo.BRepAlgo_AsDes,Side : OCP.TopAbs.TopAbs_State,Tol : float) -> None: ...
    pass
class BRepOffset_Interval():
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
    def First(self,U : float) -> None: ...
    @overload
    def Last(self,U : float) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Last(self) -> float: ...
    @overload
    def Type(self) -> BRepOffset_Type: 
        """
        None

        None

        None

        None
        """
    @overload
    def Type(self,T : BRepOffset_Type) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,U1 : float,U2 : float,Type : BRepOffset_Type) -> None: ...
    pass
class BRepOffset_ListOfInterval(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BRepOffset_Interval) -> BRepOffset_Interval: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : BRepOffset_ListOfInterval) -> None: ...
    @overload
    def Append(self,theItem : BRepOffset_Interval,theIter : Any) -> None: ...
    def Assign(self,theOther : BRepOffset_ListOfInterval) -> BRepOffset_ListOfInterval: 
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
    def First(self) -> BRepOffset_Interval: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : BRepOffset_ListOfInterval,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : BRepOffset_Interval,theIter : Any) -> BRepOffset_Interval: ...
    @overload
    def InsertBefore(self,theItem : BRepOffset_Interval,theIter : Any) -> BRepOffset_Interval: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : BRepOffset_ListOfInterval,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BRepOffset_Interval: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : BRepOffset_Interval) -> BRepOffset_Interval: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : BRepOffset_ListOfInterval) -> None: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BRepOffset_ListOfInterval) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BRepOffset_MakeLoops():
    """
    None
    """
    def Build(self,LF : OCP.TopTools.TopTools_ListOfShape,AsDes : OCP.BRepAlgo.BRepAlgo_AsDes,Image : OCP.BRepAlgo.BRepAlgo_Image) -> None: 
        """
        None
        """
    def BuildFaces(self,LF : OCP.TopTools.TopTools_ListOfShape,AsDes : OCP.BRepAlgo.BRepAlgo_AsDes,Image : OCP.BRepAlgo.BRepAlgo_Image) -> None: 
        """
        None
        """
    def BuildOnContext(self,LContext : OCP.TopTools.TopTools_ListOfShape,Analyse : BRepOffset_Analyse,AsDes : OCP.BRepAlgo.BRepAlgo_AsDes,Image : OCP.BRepAlgo.BRepAlgo_Image,InSide : bool) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BRepOffset_MakeOffset():
    """
    None
    """
    def AddFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Add Closing Faces, <F> has to be in the initial shape S.
        """
    def CheckInputData(self) -> bool: 
        """
        Makes pre analysis of possibility offset perform. Use method Error() to get more information. Finds first error. List of checks: 1) Check for existence object with non-null offset. 2) Check for connectivity in offset shell. 3) Check continuity of input surfaces. 4) Check for normals existence on grid.
        """
    def Clear(self) -> None: 
        """
        None
        """
    def ClosingFaces(self) -> OCP.TopTools.TopTools_IndexedMapOfShape: 
        """
        Returns the list of closing faces stores by AddFace
        """
    def Error(self) -> BRepOffset_Error: 
        """
        returns information about offset state.
        """
    def GetBadShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Return bad shape, which obtained in CheckInputData.
        """
    def GetJoinType(self) -> OCP.GeomAbs.GeomAbs_JoinType: 
        """
        Returns myJoin.
        """
    def Initialize(self,S : OCP.TopoDS.TopoDS_Shape,Offset : float,Tol : float,Mode : BRepOffset_Mode=BRepOffset_Mode.BRepOffset_Skin,Intersection : bool=False,SelfInter : bool=False,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,Thickening : bool=False,RemoveIntEdges : bool=False) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def MakeOffsetShape(self) -> None: 
        """
        None
        """
    def MakeThickSolid(self) -> None: 
        """
        None
        """
    def OffsetEdgesFromShapes(self) -> OCP.BRepAlgo.BRepAlgo_Image: 
        """
        Returns <Image> containing links between initials shapes and offset edges.
        """
    def OffsetFacesFromShapes(self) -> OCP.BRepAlgo.BRepAlgo_Image: 
        """
        Returns <Image> containing links between initials shapes and offset faces.
        """
    def SetOffsetOnFace(self,F : OCP.TopoDS.TopoDS_Face,Off : float) -> None: 
        """
        set the offset <Off> on the Face <F>
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,Offset : float,Tol : float,Mode : BRepOffset_Mode=BRepOffset_Mode.BRepOffset_Skin,Intersection : bool=False,SelfInter : bool=False,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,Thickening : bool=False,RemoveIntEdges : bool=False) -> None: ...
    pass
class BRepOffset_MakeSimpleOffset():
    """
    Limitations: According to the algorithm nature result depends on the smoothness of input data. Smooth (G1-continuity) input shape will lead to the good result.
    """
    def Generated(self,theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returnes result shape for the given one (if exists).
        """
    def GetBuildSolidFlag(self) -> bool: 
        """
        Gets solid building flag.
        """
    def GetError(self) -> BRepOffsetSimple_Status: 
        """
        Gets error code.
        """
    def GetErrorMessage(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets error message.
        """
    def GetOffsetValue(self) -> float: 
        """
        Gets offset value.
        """
    def GetResultShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns result shape.
        """
    def GetSafeOffset(self,theExpectedToler : float) -> float: 
        """
        Computes max safe offset value for the given tolerance.
        """
    def GetTolerance(self) -> float: 
        """
        Gets tolerance (used for handling singularities).
        """
    def Initialize(self,theInputShape : OCP.TopoDS.TopoDS_Shape,theOffsetValue : float) -> None: 
        """
        Initialies shape for modifications.
        """
    def IsDone(self) -> bool: 
        """
        Gets done state.
        """
    def Modified(self,theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returnes modified shape for the given one (if exists).
        """
    def Perform(self) -> None: 
        """
        Computes offset shape.
        """
    def SetBuildSolidFlag(self,theBuildFlag : bool) -> None: 
        """
        Sets solid building flag.
        """
    def SetOffsetValue(self,theOffsetValue : float) -> None: 
        """
        Sets offset value.
        """
    def SetTolerance(self,theValue : float) -> None: 
        """
        Sets tolerance (used for handling singularities).
        """
    @overload
    def __init__(self,theInputShape : OCP.TopoDS.TopoDS_Shape,theOffsetValue : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepOffset_Mode():
    """
    Lists the offset modes. These are the following: - BRepOffset_Skin which describes the offset along the surface of a solid, used to obtain a manifold topological space, - BRepOffset_Pipe which describes the offset of a curve, used to obtain a pre-surface, - BRepOffset_RectoVerso which describes the offset of a given surface shell along both sides of the surface.

    Members:

      BRepOffset_Skin

      BRepOffset_Pipe

      BRepOffset_RectoVerso
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
    BRepOffset_Pipe: OCP.BRepOffset.BRepOffset_Mode # value = BRepOffset_Mode.BRepOffset_Pipe
    BRepOffset_RectoVerso: OCP.BRepOffset.BRepOffset_Mode # value = BRepOffset_Mode.BRepOffset_RectoVerso
    BRepOffset_Skin: OCP.BRepOffset.BRepOffset_Mode # value = BRepOffset_Mode.BRepOffset_Skin
    __entries: dict # value = {'BRepOffset_Skin': (BRepOffset_Mode.BRepOffset_Skin, None), 'BRepOffset_Pipe': (BRepOffset_Mode.BRepOffset_Pipe, None), 'BRepOffset_RectoVerso': (BRepOffset_Mode.BRepOffset_RectoVerso, None)}
    __members__: dict # value = {'BRepOffset_Skin': BRepOffset_Mode.BRepOffset_Skin, 'BRepOffset_Pipe': BRepOffset_Mode.BRepOffset_Pipe, 'BRepOffset_RectoVerso': BRepOffset_Mode.BRepOffset_RectoVerso}
    pass
class BRepOffset_Offset():
    """
    This class compute elemenary offset surface. Evaluate the offset generated : 1 - from a face. 2 - from an edge. 3 - from a vertex.
    """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def Generated(self,Shape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def Init(self,Vertex : OCP.TopoDS.TopoDS_Vertex,LEdge : OCP.TopTools.TopTools_ListOfShape,Offset : float,Polynomial : bool=False,Tol : float=0.0001,Conti : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: 
        """
        None

        None

        None

        None

        Tol and Conti are only used if Polynomial is True (Used to perfrom the approximation)

        Only used in Rolling Ball. Pipe on Free Boundary
        """
    @overload
    def Init(self,Face : OCP.TopoDS.TopoDS_Face,Offset : float,OffsetOutside : bool=True,JoinType : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc) -> None: ...
    @overload
    def Init(self,Edge : OCP.TopoDS.TopoDS_Edge,Offset : float) -> None: ...
    @overload
    def Init(self,Face : OCP.TopoDS.TopoDS_Face,Offset : float,Created : OCP.TopTools.TopTools_DataMapOfShapeShape,OffsetOutside : bool=True,JoinType : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc) -> None: ...
    @overload
    def Init(self,Path : OCP.TopoDS.TopoDS_Edge,Edge1 : OCP.TopoDS.TopoDS_Edge,Edge2 : OCP.TopoDS.TopoDS_Edge,Offset : float,Polynomial : bool=False,Tol : float=0.0001,Conti : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def Init(self,Path : OCP.TopoDS.TopoDS_Edge,Edge1 : OCP.TopoDS.TopoDS_Edge,Edge2 : OCP.TopoDS.TopoDS_Edge,Offset : float,FirstEdge : OCP.TopoDS.TopoDS_Edge,LastEdge : OCP.TopoDS.TopoDS_Edge,Polynomial : bool=False,Tol : float=0.0001,Conti : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    def InitialShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    def Status(self) -> BRepOffset_Status: 
        """
        None
        """
    @overload
    def __init__(self,Vertex : OCP.TopoDS.TopoDS_Vertex,LEdge : OCP.TopTools.TopTools_ListOfShape,Offset : float,Polynomial : bool=False,Tol : float=0.0001,Conti : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def __init__(self,Face : OCP.TopoDS.TopoDS_Face,Offset : float,OffsetOutside : bool=True,JoinType : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc) -> None: ...
    @overload
    def __init__(self,Face : OCP.TopoDS.TopoDS_Face,Offset : float,Created : OCP.TopTools.TopTools_DataMapOfShapeShape,OffsetOutside : bool=True,JoinType : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Path : OCP.TopoDS.TopoDS_Edge,Edge1 : OCP.TopoDS.TopoDS_Edge,Edge2 : OCP.TopoDS.TopoDS_Edge,Offset : float,Polynomial : bool=False,Tol : float=0.0001,Conti : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    @overload
    def __init__(self,Path : OCP.TopoDS.TopoDS_Edge,Edge1 : OCP.TopoDS.TopoDS_Edge,Edge2 : OCP.TopoDS.TopoDS_Edge,Offset : float,FirstEdge : OCP.TopoDS.TopoDS_Edge,LastEdge : OCP.TopoDS.TopoDS_Edge,Polynomial : bool=False,Tol : float=0.0001,Conti : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: ...
    pass
class BRepOffset_SimpleOffset(OCP.BRepTools.BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    This class represents mechanism of simple offset algorithm i. e. topology-preserve offset construction without intersection.This class represents mechanism of simple offset algorithm i. e. topology-preserve offset construction without intersection.This class represents mechanism of simple offset algorithm i. e. topology-preserve offset construction without intersection.
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
    def __init__(self,theInputShape : OCP.TopoDS.TopoDS_Shape,theOffsetValue : float,theTolerance : float) -> None: ...
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
class BRepOffset_Status():
    """
    status of an offset face Good : Reversed : e.g. Offset > Radius of a cylinder Degenerated : e.g. Offset = Radius of a cylinder Unknown : e.g. for a Beziersurf

    Members:

      BRepOffset_Good

      BRepOffset_Reversed

      BRepOffset_Degenerated

      BRepOffset_Unknown
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
    BRepOffset_Degenerated: OCP.BRepOffset.BRepOffset_Status # value = BRepOffset_Status.BRepOffset_Degenerated
    BRepOffset_Good: OCP.BRepOffset.BRepOffset_Status # value = BRepOffset_Status.BRepOffset_Good
    BRepOffset_Reversed: OCP.BRepOffset.BRepOffset_Status # value = BRepOffset_Status.BRepOffset_Reversed
    BRepOffset_Unknown: OCP.BRepOffset.BRepOffset_Status # value = BRepOffset_Status.BRepOffset_Unknown
    __entries: dict # value = {'BRepOffset_Good': (BRepOffset_Status.BRepOffset_Good, None), 'BRepOffset_Reversed': (BRepOffset_Status.BRepOffset_Reversed, None), 'BRepOffset_Degenerated': (BRepOffset_Status.BRepOffset_Degenerated, None), 'BRepOffset_Unknown': (BRepOffset_Status.BRepOffset_Unknown, None)}
    __members__: dict # value = {'BRepOffset_Good': BRepOffset_Status.BRepOffset_Good, 'BRepOffset_Reversed': BRepOffset_Status.BRepOffset_Reversed, 'BRepOffset_Degenerated': BRepOffset_Status.BRepOffset_Degenerated, 'BRepOffset_Unknown': BRepOffset_Status.BRepOffset_Unknown}
    pass
class BRepOffset_Tool():
    """
    None
    """
    @staticmethod
    def BuildNeighbour_s(W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face,NOnV1 : OCP.TopTools.TopTools_DataMapOfShapeShape,NOnV2 : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        Via the wire explorer store in <NOnV1> for an Edge <E> of <W> his Edge neighbour on the first vertex <V1> of <E>. Store in NOnV2 the Neighbour of <E>on the last vertex <V2> of <E>.
        """
    @staticmethod
    def CheckBounds_s(F : OCP.TopoDS.TopoDS_Face,Analyse : BRepOffset_Analyse) -> Tuple[bool, bool, bool]: 
        """
        None
        """
    @staticmethod
    def CheckPlanesNormals_s(theFace1 : OCP.TopoDS.TopoDS_Face,theFace2 : OCP.TopoDS.TopoDS_Face,theTolAng : float=1e-08) -> bool: 
        """
        Compares the normal directions of the planar faces and returns TRUE if the directions are the same with the given precision.
        """
    @staticmethod
    def CorrectOrientation_s(SI : OCP.TopoDS.TopoDS_Shape,NewEdges : OCP.TopTools.TopTools_IndexedMapOfShape,AsDes : OCP.BRepAlgo.BRepAlgo_AsDes,InitOffset : OCP.BRepAlgo.BRepAlgo_Image,Offset : float) -> None: 
        """
        None
        """
    @staticmethod
    def Deboucle3D_s(S : OCP.TopoDS.TopoDS_Shape,Boundary : OCP.TopTools.TopTools_MapOfShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Remove the non valid part of an offsetshape 1 - Remove all the free boundary and the faces connex to such edges. 2 - Remove all the shapes not valid in the result (according to the side of offseting) in this verion only the first point is implemented.
        """
    @staticmethod
    def EdgeVertices_s(E : OCP.TopoDS.TopoDS_Edge,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        <V1> is the FirstVertex ,<V2> is the Last Vertex of <Edge> taking account the orientation of Edge.
        """
    @staticmethod
    def EnLargeFace_s(F : OCP.TopoDS.TopoDS_Face,NF : OCP.TopoDS.TopoDS_Face,ChangeGeom : bool,UpDatePCurve : bool=False,enlargeU : bool=True,enlargeVfirst : bool=True,enlargeVlast : bool=True,theExtensionMode : int=1,theLenBeforeUfirst : float=-1.0,theLenAfterUlast : float=-1.0,theLenBeforeVfirst : float=-1.0,theLenAfterVlast : float=-1.0) -> bool: 
        """
        Returns True if The Surface of <NF> has changed. if <ChangeGeom> is TRUE , the surface can be changed . if <UpdatePCurve> is TRUE, update the pcurves of the edges of <F> on the new surface if the surface has been changed. <enlargeU>, <enlargeVfirst>, <enlargeVlast> allow or forbid enlargement in U and V directions correspondingly. <theExtensionMode> is a mode of extension of the surface of the face: if <theExtensionMode> equals 1, potentially infinite surfaces are extended by maximum value, and limited surfaces are extended by 25%. if <theExtensionMode> equals 2, potentially infinite surfaces are extended by 10*(correspondent size of face), and limited surfaces are extended by 100%. <theLenBeforeUfirst>, <theLenAfterUlast>, <theLenBeforeVfirst>, <theLenAfterVlast> set the values of enlargement on correspondent directions. If some of them equals -1, the default value of enlargement is used.
        """
    @staticmethod
    def ExtentFace_s(F : OCP.TopoDS.TopoDS_Face,ConstShapes : OCP.TopTools.TopTools_DataMapOfShapeShape,ToBuild : OCP.TopTools.TopTools_DataMapOfShapeShape,Side : OCP.TopAbs.TopAbs_State,TolConf : float,NF : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def FindCommonShapes_s(theF1 : OCP.TopoDS.TopoDS_Face,theF2 : OCP.TopoDS.TopoDS_Face,theLE : OCP.TopTools.TopTools_ListOfShape,theLV : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        Looks for the common Vertices and Edges between faces <theF1> and <theF2>. Returns TRUE if common shapes have been found. <theLE> will contain the found common edges; <theLV> will contain the found common vertices.

        Looks for the common shapes of type <theType> between shapes <theS1> and <theS2>. Returns TRUE if common shapes have been found. <theLSC> will contain the found common shapes.
        """
    @staticmethod
    @overload
    def FindCommonShapes_s(theS1 : OCP.TopoDS.TopoDS_Shape,theS2 : OCP.TopoDS.TopoDS_Shape,theType : OCP.TopAbs.TopAbs_ShapeEnum,theLSC : OCP.TopTools.TopTools_ListOfShape) -> bool: ...
    @staticmethod
    def Gabarit_s(aCurve : OCP.Geom.Geom_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def Inter2d_s(F : OCP.TopoDS.TopoDS_Face,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,LV : OCP.TopTools.TopTools_ListOfShape,Tol : float) -> None: 
        """
        None
        """
    @staticmethod
    def Inter3D_s(F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,LInt1 : OCP.TopTools.TopTools_ListOfShape,LInt2 : OCP.TopTools.TopTools_ListOfShape,Side : OCP.TopAbs.TopAbs_State,RefEdge : OCP.TopoDS.TopoDS_Edge,IsRefEdgeDefined : bool=False) -> None: 
        """
        Computes the Section betwwen <F1> and <F2> the edges solution are stored in <LInt1> with the orientation on <F1>, the sames edges are stored in <Lint2> with the orientation on <F2>.
        """
    @staticmethod
    def InterOrExtent_s(F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,LInt1 : OCP.TopTools.TopTools_ListOfShape,LInt2 : OCP.TopTools.TopTools_ListOfShape,Side : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    @staticmethod
    def MapVertexEdges_s(S : OCP.TopoDS.TopoDS_Shape,MVE : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        Store in MVE for a vertex <V> in <S> the incident edges <E> in <S>. An Edge is Store only one Time for a vertex.
        """
    @staticmethod
    def OriEdgeInFace_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        returns the cumul of the orientation of <Edge> and thc containing wire in <Face>
        """
    @staticmethod
    def OrientSection_s(E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,O1 : OCP.TopAbs.TopAbs_Orientation,O2 : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        <E> is a section between <F1> and <F2>. Computes <O1> the orientation of <E> in <F1> influenced by <F2>. idem for <O2>.
        """
    @staticmethod
    def PipeInter_s(F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,LInt1 : OCP.TopTools.TopTools_ListOfShape,LInt2 : OCP.TopTools.TopTools_ListOfShape,Side : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    @staticmethod
    def TryProject_s(F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,Edges : OCP.TopTools.TopTools_ListOfShape,LInt1 : OCP.TopTools.TopTools_ListOfShape,LInt2 : OCP.TopTools.TopTools_ListOfShape,Side : OCP.TopAbs.TopAbs_State,TolConf : float) -> bool: 
        """
        Find if the edges <Edges> of the face <F2> are on the face <F1>. Set in <LInt1> <LInt2> the updated edges. If all the edges are computed, returns true.
        """
    def __init__(self) -> None: ...
    pass
class BRepOffset_Type():
    """
    None

    Members:

      BRepOffset_Concave

      BRepOffset_Convex

      BRepOffset_Tangent

      BRepOffset_FreeBoundary

      BRepOffset_Other
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
    BRepOffset_Concave: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_Concave
    BRepOffset_Convex: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_Convex
    BRepOffset_FreeBoundary: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_FreeBoundary
    BRepOffset_Other: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_Other
    BRepOffset_Tangent: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_Tangent
    __entries: dict # value = {'BRepOffset_Concave': (BRepOffset_Type.BRepOffset_Concave, None), 'BRepOffset_Convex': (BRepOffset_Type.BRepOffset_Convex, None), 'BRepOffset_Tangent': (BRepOffset_Type.BRepOffset_Tangent, None), 'BRepOffset_FreeBoundary': (BRepOffset_Type.BRepOffset_FreeBoundary, None), 'BRepOffset_Other': (BRepOffset_Type.BRepOffset_Other, None)}
    __members__: dict # value = {'BRepOffset_Concave': BRepOffset_Type.BRepOffset_Concave, 'BRepOffset_Convex': BRepOffset_Type.BRepOffset_Convex, 'BRepOffset_Tangent': BRepOffset_Type.BRepOffset_Tangent, 'BRepOffset_FreeBoundary': BRepOffset_Type.BRepOffset_FreeBoundary, 'BRepOffset_Other': BRepOffset_Type.BRepOffset_Other}
    pass
BRepOffsetSimple_ErrorInvalidNbShells: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_ErrorInvalidNbShells
BRepOffsetSimple_ErrorNonClosedShell: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_ErrorNonClosedShell
BRepOffsetSimple_ErrorOffsetComputation: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_ErrorOffsetComputation
BRepOffsetSimple_ErrorWallFaceComputation: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_ErrorWallFaceComputation
BRepOffsetSimple_NullInputShape: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_NullInputShape
BRepOffsetSimple_OK: OCP.BRepOffset.BRepOffsetSimple_Status # value = BRepOffsetSimple_Status.BRepOffsetSimple_OK
BRepOffset_BadNormalsOnGeometry: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_BadNormalsOnGeometry
BRepOffset_C0Geometry: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_C0Geometry
BRepOffset_Concave: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_Concave
BRepOffset_Convex: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_Convex
BRepOffset_Degenerated: OCP.BRepOffset.BRepOffset_Status # value = BRepOffset_Status.BRepOffset_Degenerated
BRepOffset_FreeBoundary: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_FreeBoundary
BRepOffset_Good: OCP.BRepOffset.BRepOffset_Status # value = BRepOffset_Status.BRepOffset_Good
BRepOffset_NoError: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_NoError
BRepOffset_NotConnectedShell: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_NotConnectedShell
BRepOffset_NullOffset: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_NullOffset
BRepOffset_Other: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_Other
BRepOffset_Pipe: OCP.BRepOffset.BRepOffset_Mode # value = BRepOffset_Mode.BRepOffset_Pipe
BRepOffset_RectoVerso: OCP.BRepOffset.BRepOffset_Mode # value = BRepOffset_Mode.BRepOffset_RectoVerso
BRepOffset_Reversed: OCP.BRepOffset.BRepOffset_Status # value = BRepOffset_Status.BRepOffset_Reversed
BRepOffset_Skin: OCP.BRepOffset.BRepOffset_Mode # value = BRepOffset_Mode.BRepOffset_Skin
BRepOffset_Tangent: OCP.BRepOffset.BRepOffset_Type # value = BRepOffset_Type.BRepOffset_Tangent
BRepOffset_Unknown: OCP.BRepOffset.BRepOffset_Status # value = BRepOffset_Status.BRepOffset_Unknown
BRepOffset_UnknownError: OCP.BRepOffset.BRepOffset_Error # value = BRepOffset_Error.BRepOffset_UnknownError
