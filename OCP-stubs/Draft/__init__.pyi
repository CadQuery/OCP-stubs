import OCP.Draft
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.GeomAbs
import OCP.NCollection
import OCP.Poly
import OCP.BRepTools
import io
import OCP.gp
import OCP.Geom2d
import OCP.TopLoc
import OCP.Geom
import OCP.Standard
import OCP.TopoDS
__all__  = [
"Draft",
"Draft_EdgeInfo",
"Draft_ErrorStatus",
"Draft_FaceInfo",
"Draft_IndexedDataMapOfEdgeEdgeInfo",
"Draft_IndexedDataMapOfFaceFaceInfo",
"Draft_IndexedDataMapOfVertexVertexInfo",
"Draft_Modification",
"Draft_VertexInfo",
"Draft_EdgeRecomputation",
"Draft_FaceRecomputation",
"Draft_NoError",
"Draft_VertexRecomputation"
]
class Draft():
    """
    None
    """
    @staticmethod
    def Angle_s(F : OCP.TopoDS.TopoDS_Face,Direction : OCP.gp.gp_Dir) -> float: 
        """
        Returns the draft angle of the face <F> using the direction <Direction>. The method is valid for : - Plane faces, - Cylindrical or conical faces, when the direction of the axis of the surface is colinear with the direction. Otherwise, the exception DomainError is raised.
        """
    def __init__(self) -> None: ...
    pass
class Draft_EdgeInfo():
    """
    None
    """
    def Add(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def ChangeFirstPC(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def ChangeGeometry(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def ChangeSecondPC(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def FirstFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def FirstPC(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def Geometry(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def IsTangent(self,P : OCP.gp.gp_Pnt) -> bool: 
        """
        None
        """
    def NewGeometry(self) -> bool: 
        """
        None
        """
    @overload
    def RootFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None

        None
        """
    @overload
    def RootFace(self) -> OCP.TopoDS.TopoDS_Face: ...
    def SecondFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def SecondPC(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def SetNewGeometry(self,NewGeom : bool) -> None: 
        """
        None
        """
    def Tangent(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @overload
    def Tolerance(self) -> float: 
        """
        None

        None
        """
    @overload
    def Tolerance(self,tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,HasNewGeometry : bool) -> None: ...
    pass
class Draft_ErrorStatus():
    """
    None

    Members:

      Draft_NoError

      Draft_FaceRecomputation

      Draft_EdgeRecomputation

      Draft_VertexRecomputation
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
    Draft_EdgeRecomputation: OCP.Draft.Draft_ErrorStatus # value = <Draft_ErrorStatus.Draft_EdgeRecomputation: 2>
    Draft_FaceRecomputation: OCP.Draft.Draft_ErrorStatus # value = <Draft_ErrorStatus.Draft_FaceRecomputation: 1>
    Draft_NoError: OCP.Draft.Draft_ErrorStatus # value = <Draft_ErrorStatus.Draft_NoError: 0>
    Draft_VertexRecomputation: OCP.Draft.Draft_ErrorStatus # value = <Draft_ErrorStatus.Draft_VertexRecomputation: 3>
    __entries: dict # value = {'Draft_NoError': (<Draft_ErrorStatus.Draft_NoError: 0>, None), 'Draft_FaceRecomputation': (<Draft_ErrorStatus.Draft_FaceRecomputation: 1>, None), 'Draft_EdgeRecomputation': (<Draft_ErrorStatus.Draft_EdgeRecomputation: 2>, None), 'Draft_VertexRecomputation': (<Draft_ErrorStatus.Draft_VertexRecomputation: 3>, None)}
    __members__: dict # value = {'Draft_NoError': <Draft_ErrorStatus.Draft_NoError: 0>, 'Draft_FaceRecomputation': <Draft_ErrorStatus.Draft_FaceRecomputation: 1>, 'Draft_EdgeRecomputation': <Draft_ErrorStatus.Draft_EdgeRecomputation: 2>, 'Draft_VertexRecomputation': <Draft_ErrorStatus.Draft_VertexRecomputation: 3>}
    pass
class Draft_FaceInfo():
    """
    None
    """
    def Add(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def ChangeCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def ChangeGeometry(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Curve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def FirstFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def Geometry(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def NewGeometry(self) -> bool: 
        """
        None
        """
    @overload
    def RootFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None

        None
        """
    @overload
    def RootFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    def SecondFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface,HasNewGeometry : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Draft_IndexedDataMapOfEdgeEdgeInfo(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Edge,theItem : Draft_EdgeInfo) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Draft_IndexedDataMapOfEdgeEdgeInfo) -> Draft_IndexedDataMapOfEdgeEdgeInfo: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> Draft_EdgeInfo: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Edge) -> Draft_EdgeInfo: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Edge) -> Draft_EdgeInfo: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : Draft_IndexedDataMapOfEdgeEdgeInfo) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> Draft_EdgeInfo: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Edge) -> Draft_EdgeInfo: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Edge,theValue : Draft_EdgeInfo) -> bool: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        FindKey
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
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Edge) -> Draft_EdgeInfo: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Edge,theItem : Draft_EdgeInfo) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Draft_IndexedDataMapOfEdgeEdgeInfo) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Draft_IndexedDataMapOfFaceFaceInfo(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Face,theItem : Draft_FaceInfo) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Draft_IndexedDataMapOfFaceFaceInfo) -> Draft_IndexedDataMapOfFaceFaceInfo: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> Draft_FaceInfo: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Face) -> Draft_FaceInfo: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Face) -> Draft_FaceInfo: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : Draft_IndexedDataMapOfFaceFaceInfo) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> Draft_FaceInfo: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Face,theValue : Draft_FaceInfo) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Face) -> Draft_FaceInfo: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Face) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        FindKey
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
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Face) -> Draft_FaceInfo: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Face,theItem : Draft_FaceInfo) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : Draft_IndexedDataMapOfFaceFaceInfo) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Draft_IndexedDataMapOfVertexVertexInfo(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Vertex,theItem : Draft_VertexInfo) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Draft_IndexedDataMapOfVertexVertexInfo) -> Draft_IndexedDataMapOfVertexVertexInfo: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> Draft_VertexInfo: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> Draft_VertexInfo: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> Draft_VertexInfo: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : Draft_IndexedDataMapOfVertexVertexInfo) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> Draft_VertexInfo: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> Draft_VertexInfo: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Vertex,theValue : Draft_VertexInfo) -> bool: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        FindKey
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
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Vertex) -> Draft_VertexInfo: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Vertex,theItem : Draft_VertexInfo) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : Draft_IndexedDataMapOfVertexVertexInfo) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Draft_Modification(OCP.BRepTools.BRepTools_Modification, OCP.Standard.Standard_Transient):
    def Add(self,F : OCP.TopoDS.TopoDS_Face,Direction : OCP.gp.gp_Dir,Angle : float,NeutralPlane : OCP.gp.gp_Pln,Flag : bool=True) -> bool: 
        """
        Adds the face F and propagates the draft modification to its neighbour faces if they are tangent. If an error occurs, will return False and ProblematicShape will return the "bad" face.
        """
    def Clear(self) -> None: 
        """
        Resets on the same shape.
        """
    def ConnectedFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns all the faces which have been added together with the face <F>.
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
    def Error(self) -> Draft_ErrorStatus: 
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
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Changes the basis shape and resets.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if Perform has been successfully called. Otherwise more information can be obtained using the methods Error() and ProblematicShape().
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
    def ModifiedFaces(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns all the faces on which a modification has been given.
        """
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has been modified. In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has a new curve on surface on the face <F>.In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance.
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
        Returns Standard_True if the face <F> has been modified. In this case, <S> is the new geometric support of the face, <L> the new location,<Tol> the new tolerance.<RevWires> has to be set to Standard_True when the modification reverses the normal of the surface.(the wires have to be reversed). <RevFace> has to be set to Standard_True if the orientation of the modified face changes in the shells which contain it. Here it will be set to Standard_False.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def Perform(self) -> None: 
        """
        Performs the draft angle modification and sets the value returned by the method IsDone. If an error occurs, IsDone will return Standard_False, and an error status will be given by the method Error, and the shape on which the problem appeared will be given by ProblematicShape
        """
    def ProblematicShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape (Face, Edge or Vertex) on which an error occurred.
        """
    def Remove(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Removes the face F and the neighbour faces if they are tangent. It will be necessary to call this method if the method Add returns Standard_False, to unset ProblematicFace.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class Draft_VertexInfo():
    """
    None
    """
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def ChangeGeometry(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def ChangeParameter(self,E : OCP.TopoDS.TopoDS_Edge) -> float: 
        """
        None
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def Geometry(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def InitEdgeIterator(self) -> None: 
        """
        None
        """
    def MoreEdge(self) -> bool: 
        """
        None
        """
    def NextEdge(self) -> None: 
        """
        None
        """
    def Parameter(self,E : OCP.TopoDS.TopoDS_Edge) -> float: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
Draft_EdgeRecomputation: OCP.Draft.Draft_ErrorStatus # value = <Draft_ErrorStatus.Draft_EdgeRecomputation: 2>
Draft_FaceRecomputation: OCP.Draft.Draft_ErrorStatus # value = <Draft_ErrorStatus.Draft_FaceRecomputation: 1>
Draft_NoError: OCP.Draft.Draft_ErrorStatus # value = <Draft_ErrorStatus.Draft_NoError: 0>
Draft_VertexRecomputation: OCP.Draft.Draft_ErrorStatus # value = <Draft_ErrorStatus.Draft_VertexRecomputation: 3>
