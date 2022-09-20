import OCP.BRepMAT2d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.MAT
import OCP.Bisector
import OCP.NCollection
import OCP.TColGeom2d
import io
import OCP.Geom2d
import OCP.gp
import OCP.TopoDS
import OCP.TColStd
__all__  = [
"BRepMAT2d_BisectingLocus",
"BRepMAT2d_DataMapOfBasicEltShape",
"BRepMAT2d_DataMapOfShapeSequenceOfBasicElt",
"BRepMAT2d_Explorer",
"BRepMAT2d_LinkTopoBilo"
]
class BRepMAT2d_BisectingLocus():
    """
    BisectingLocus generates and contains the Bisecting_Locus of a set of lines from Geom2d, defined by <ExploSet>.
    """
    def BasicElt(self,IndLine : int,Index : int) -> OCP.MAT.MAT_BasicElt: 
        """
        Returns the BasicElts located at the position <Index> on the contour designed by <IndLine>. Remark: the BasicElts on a contour are sorted.
        """
    def Compute(self,anExplo : BRepMAT2d_Explorer,LineIndex : int=1,aSide : OCP.MAT.MAT_Side=MAT_Side.MAT_Left,aJoinType : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,IsOpenResult : bool=False) -> None: 
        """
        Computation of the Bisector_Locus in a set of Lines defined in <anExplo>. The bisecting locus are computed on the side <aSide> from the line <LineIndex> in <anExplo>.
        """
    def GeomBis(self,anArc : OCP.MAT.MAT_Arc,Reverse : bool) -> OCP.Bisector.Bisector_Bisec: 
        """
        Returns the geometry of type <Bissec> linked to the arc <ARC>. <Reverse> is False when the FirstNode of <anArc> correspond to the first point of geometry.
        """
    @overload
    def GeomElt(self,aNode : OCP.MAT.MAT_Node) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the geometry linked to the <BasicElt>.

        Returns the geometry of type <gp> linked to the <Node>.
        """
    @overload
    def GeomElt(self,aBasicElt : OCP.MAT.MAT_BasicElt) -> OCP.Geom2d.Geom2d_Geometry: ...
    def Graph(self) -> OCP.MAT.MAT_Graph: 
        """
        Returns <theGraph> of <me>.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if Compute has succeeded.
        """
    def NumberOfContours(self) -> int: 
        """
        Returns the number of contours.
        """
    def NumberOfElts(self,IndLine : int) -> int: 
        """
        Returns the number of BasicElts on the line <IndLine>.
        """
    def NumberOfSections(self,IndLine : int,Index : int) -> int: 
        """
        Returns the number of sections of a curve. this curve is the Indexth curve in the IndLineth contour given by anExplo.
        """
    def __init__(self) -> None: ...
    pass
class BRepMAT2d_DataMapOfBasicEltShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepMAT2d_DataMapOfBasicEltShape) -> BRepMAT2d_DataMapOfBasicEltShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.MAT.MAT_BasicElt,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.MAT.MAT_BasicElt,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.MAT.MAT_BasicElt) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.MAT.MAT_BasicElt) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Exchange(self,theOther : BRepMAT2d_DataMapOfBasicEltShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.MAT.MAT_BasicElt,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.MAT.MAT_BasicElt) -> OCP.TopoDS.TopoDS_Shape: ...
    def IsBound(self,theKey : OCP.MAT.MAT_BasicElt) -> bool: 
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
    def Seek(self,theKey : OCP.MAT.MAT_BasicElt) -> OCP.TopoDS.TopoDS_Shape: 
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
    def UnBind(self,theKey : OCP.MAT.MAT_BasicElt) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : BRepMAT2d_DataMapOfBasicEltShape) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepMAT2d_DataMapOfShapeSequenceOfBasicElt(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepMAT2d_DataMapOfShapeSequenceOfBasicElt) -> BRepMAT2d_DataMapOfShapeSequenceOfBasicElt: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.MAT.MAT_SequenceOfBasicElt) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.MAT.MAT_SequenceOfBasicElt) -> OCP.MAT.MAT_SequenceOfBasicElt: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.MAT.MAT_SequenceOfBasicElt: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.MAT.MAT_SequenceOfBasicElt: 
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
    def Exchange(self,theOther : BRepMAT2d_DataMapOfShapeSequenceOfBasicElt) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.MAT.MAT_SequenceOfBasicElt) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.MAT.MAT_SequenceOfBasicElt: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.MAT.MAT_SequenceOfBasicElt: 
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
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BRepMAT2d_DataMapOfShapeSequenceOfBasicElt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepMAT2d_Explorer():
    """
    Construct an explorer from wires, face, set of curves from Geom2d to compute the bisecting Locus.
    """
    def Clear(self) -> None: 
        """
        Clear the contents of <me>.
        """
    def Contour(self,IndexContour : int) -> OCP.TColGeom2d.TColGeom2d_SequenceOfCurve: 
        """
        None
        """
    def GetIsClosed(self) -> OCP.TColStd.TColStd_SequenceOfBoolean: 
        """
        None
        """
    def Init(self,IndexContour : int) -> None: 
        """
        Initialisation of an Iterator on the curves of the Contour number <IndexContour>.
        """
    def IsModified(self,aShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def ModifiedShape(self,aShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        If the shape is not modified, returns the shape itself.
        """
    def More(self) -> bool: 
        """
        Return False if there is no more curves on the Contour initialised by the method Init.
        """
    def Next(self) -> None: 
        """
        Move to the next curve of the current Contour.
        """
    def NumberOfContours(self) -> int: 
        """
        Returns the Number of contours.
        """
    def NumberOfCurves(self,IndexContour : int) -> int: 
        """
        Returns the Number of Curves in the Contour number <IndexContour>.
        """
    def Perform(self,aFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Value(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns the current curve on the current Contour.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aFace : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
class BRepMAT2d_LinkTopoBilo():
    """
    Constructs links between the Wire or the Face of the explorer and the BasicElts contained in the bisecting locus.
    """
    def GeneratingShape(self,aBE : OCP.MAT.MAT_BasicElt) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the Shape linked to <aBE>.
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialise the Iterator on <S> <S> is an edge or a vertex of the initial wire or face. raises if <S> is not an edge or a vertex.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current BasicElt.
        """
    def Next(self) -> None: 
        """
        Proceed to the next BasicElt.
        """
    def Perform(self,Explo : BRepMAT2d_Explorer,BiLo : BRepMAT2d_BisectingLocus) -> None: 
        """
        Constructs the links Between S and BiLo.
        """
    def Value(self) -> OCP.MAT.MAT_BasicElt: 
        """
        Returns the current BasicElt.
        """
    @overload
    def __init__(self,Explo : BRepMAT2d_Explorer,BiLo : BRepMAT2d_BisectingLocus) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
