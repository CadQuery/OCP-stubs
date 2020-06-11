import OCP.BRepClass3d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64

_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.ShapeAnalysis
import OCP.TopAbs
import OCP.TopoDS
import OCP.Bnd
import OCP.BRepAdaptor
import OCP.TopTools
import OCP.gp
import OCP.IntCurveSurface
import OCP.IntCurvesFace

__all__ = [
    "BRepClass3d",
    "BRepClass3d_Intersector3d",
    "BRepClass3d_MapOfInter",
    "BRepClass3d_SClassifier",
    "BRepClass3d_SolidClassifier",
    "BRepClass3d_SolidExplorer",
    "BRepClass3d_SolidPassiveClassifier",
]

class BRepClass3d:
    """
    None
    """

    @staticmethod
    def OuterShell_s(S: OCP.TopoDS.TopoDS_Solid) -> OCP.TopoDS.TopoDS_Shell:
        """
        Returns the outer most shell of <S>. Returns a Null shell if <S> has no outer shell. If <S> has only one shell, then it will return, without checking orientation.
        """
    def __init__(self) -> None: ...
    pass

class BRepClass3d_Intersector3d:
    """
    None
    """

    def Face(self) -> OCP.TopoDS.TopoDS_Face:
        """
        Returns the significant face used to determine the intersection.

        Returns the significant face used to determine the intersection.
        """
    def HasAPoint(self) -> bool:
        """
        True is returned if a point has been found.

        True is returned if a point has been found.
        """
    def IsDone(self) -> bool:
        """
        True is returned when the intersection have been computed.

        True is returned when the intersection have been computed.
        """
    def Perform(
        self, L: OCP.gp.gp_Lin, Prm: float, Tol: float, F: OCP.TopoDS.TopoDS_Face
    ) -> None:
        """
        Perform the intersection between the segment L(0) ... L(Prm) and the Shape <Sh>.
        """
    def Pnt(self) -> OCP.gp.gp_Pnt:
        """
        Returns the geometric point of the intersection between the line and the surface.

        Returns the geometric point of the intersection between the line and the surface.
        """
    def State(self) -> OCP.TopAbs.TopAbs_State:
        """
        Returns the state of the point on the face. The values can be either TopAbs_IN ( the point is in the face) or TopAbs_ON ( the point is on a boudary of the face).

        Returns the state of the point on the face. The values can be either TopAbs_IN ( the point is in the face) or TopAbs_ON ( the point is on a boudary of the face).
        """
    def Transition(self) -> OCP.IntCurveSurface.IntCurveSurface_TransitionOnCurve:
        """
        Returns the transition of the line on the surface.

        Returns the transition of the line on the surface.
        """
    def UParameter(self) -> float:
        """
        Returns the U parameter of the intersection point on the surface.

        Returns the U parameter of the intersection point on the surface.
        """
    def VParameter(self) -> float:
        """
        Returns the V parameter of the intersection point on the surface.

        Returns the V parameter of the intersection point on the surface.
        """
    def WParameter(self) -> float:
        """
        Returns the parameter of the intersection point on the line.

        Returns the parameter of the intersection point on the line.
        """
    def __init__(self) -> None: ...
    pass

class BRepClass3d_MapOfInter(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """

    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator:
        """
        Returns attached allocator
        """
    def Assign(self, theOther: BRepClass3d_MapOfInter) -> BRepClass3d_MapOfInter:
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self, theKey: OCP.TopoDS.TopoDS_Shape, theItem: capsule) -> bool:
        """
        Bind binds Item to Key in map.
        """
    def Bound(self, theKey: OCP.TopoDS.TopoDS_Shape, theItem: capsule) -> capsule:
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self, theKey: OCP.TopoDS.TopoDS_Shape) -> capsule:
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self, theKey: OCP.TopoDS.TopoDS_Shape) -> capsule:
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self, doReleaseMemory: bool = True) -> None:
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(
        self, theAllocator: OCP.NCollection.NCollection_BaseAllocator
    ) -> None: ...
    def Exchange(self, theOther: BRepClass3d_MapOfInter) -> None:
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int:
        """
        Extent
        """
    @overload
    def Find(self, theKey: OCP.TopoDS.TopoDS_Shape, theValue: capsule) -> bool:
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self, theKey: OCP.TopoDS.TopoDS_Shape) -> capsule: ...
    def IsBound(self, theKey: OCP.TopoDS.TopoDS_Shape) -> bool:
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
    def ReSize(self, N: int) -> None:
        """
        ReSize
        """
    def Seek(self, theKey: OCP.TopoDS.TopoDS_Shape) -> capsule:
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int:
        """
        Size
        """
    def Statistics(self, S: Any) -> None:
        """
        Statistics
        """
    def UnBind(self, theKey: OCP.TopoDS.TopoDS_Shape) -> bool:
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self, theOther: BRepClass3d_MapOfInter) -> None: ...
    @overload
    def __init__(
        self,
        theNbBuckets: int,
        theAllocator: OCP.NCollection.NCollection_BaseAllocator = None,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass

class BRepClass3d_SClassifier:
    """
    Provides an algorithm to classify a point in a solid.
    """

    def Face(self) -> OCP.TopoDS.TopoDS_Face:
        """
        Returns the face used to determine the classification. When the state is ON, this is the face containing the point.
        """
    def IsOnAFace(self) -> bool:
        """
        Returns True when the point is a point of a face.
        """
    def Perform(
        self, S: BRepClass3d_SolidExplorer, P: OCP.gp.gp_Pnt, Tol: float
    ) -> None:
        """
        Classify the point P with the tolerance Tol on the solid S.
        """
    def PerformInfinitePoint(self, S: BRepClass3d_SolidExplorer, Tol: float) -> None:
        """
        Classify an infinite point with the tolerance Tol on the solid S.
        """
    def Rejected(self) -> bool:
        """
        Returns True if the classification has been computed by rejection. The State is then OUT.
        """
    def State(self) -> OCP.TopAbs.TopAbs_State:
        """
        Returns the result of the classification.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, S: BRepClass3d_SolidExplorer, P: OCP.gp.gp_Pnt, Tol: float
    ) -> None: ...
    pass

class BRepClass3d_SolidClassifier(BRepClass3d_SClassifier):
    """
    Provides an algorithm to classify a point in a solid.
    """

    def Destroy(self) -> None:
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face:
        """
        Returns the face used to determine the classification. When the state is ON, this is the face containing the point.
        """
    def IsOnAFace(self) -> bool:
        """
        Returns True when the point is a point of a face.
        """
    def Load(self, S: OCP.TopoDS.TopoDS_Shape) -> None:
        """
        None
        """
    def Perform(self, P: OCP.gp.gp_Pnt, Tol: float) -> None:
        """
        Classify the point P with the tolerance Tol on the solid S.
        """
    def PerformInfinitePoint(self, Tol: float) -> None:
        """
        Classify an infinite point with the tolerance Tol on the solid S. Useful for compute the orientation of a solid.
        """
    def Rejected(self) -> bool:
        """
        Returns True if the classification has been computed by rejection. The State is then OUT.
        """
    def State(self) -> OCP.TopAbs.TopAbs_State:
        """
        Returns the result of the classification.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(
        self, S: OCP.TopoDS.TopoDS_Shape, P: OCP.gp.gp_Pnt, Tol: float
    ) -> None: ...
    pass

class BRepClass3d_SolidExplorer:
    """
    Provide an exploration of a BRep Shape for the classification. Provide access to the special UB tree to obtain fast search.
    """

    def Box(self) -> OCP.Bnd.Bnd_Box:
        """
        None
        """
    def CurrentFace(self) -> OCP.TopoDS.TopoDS_Face:
        """
        Returns the current face.
        """
    def CurrentShell(self) -> OCP.TopoDS.TopoDS_Shell:
        """
        Returns the current shell.
        """
    def Destroy(self) -> None:
        """
        None
        """
    def DumpSegment(
        self, P: OCP.gp.gp_Pnt, L: OCP.gp.gp_Lin, Par: float, S: OCP.TopAbs.TopAbs_State
    ) -> None:
        """
        None
        """
    @staticmethod
    @overload
    def FindAPointInTheFace_s(
        F: OCP.TopoDS.TopoDS_Face, P: OCP.gp.gp_Pnt, u: float, v: float, Param: float
    ) -> bool:
        """
        compute a point P in the face F. Param is a Real in ]0,1[ and is used to initialise the algorithm. For different values , different points are returned.

        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def FindAPointInTheFace_s(
        F: OCP.TopoDS.TopoDS_Face, P: OCP.gp.gp_Pnt, u: float, v: float
    ) -> bool: ...
    @staticmethod
    @overload
    def FindAPointInTheFace_s(
        F: OCP.TopoDS.TopoDS_Face, u: float, v: float
    ) -> bool: ...
    @staticmethod
    @overload
    def FindAPointInTheFace_s(
        F: OCP.TopoDS.TopoDS_Face, P: OCP.gp.gp_Pnt, Param: float
    ) -> bool: ...
    @staticmethod
    @overload
    def FindAPointInTheFace_s(
        F: OCP.TopoDS.TopoDS_Face,
        P: OCP.gp.gp_Pnt,
        u: float,
        v: float,
        Param: float,
        theVecD1U: OCP.gp.gp_Vec,
        theVecD1V: OCP.gp.gp_Vec,
    ) -> bool: ...
    @staticmethod
    @overload
    def FindAPointInTheFace_s(F: OCP.TopoDS.TopoDS_Face, P: OCP.gp.gp_Pnt) -> bool: ...
    def GetFaceSegmentIndex(self) -> int:
        """
        Returns the index of face for which last segment is calculated.
        """
    def GetMapEV(self) -> OCP.TopTools.TopTools_IndexedMapOfShape:
        """
        Return edge/vertices map for current shape.
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape:
        """
        None
        """
    def GetTree(self) -> OCP.ShapeAnalysis.ShapeAnalysis_BoxBndTree:
        """
        Return UB-tree instance which is used for edge / vertex checks.
        """
    def InitFace(self) -> None:
        """
        Starts an exploration of the faces of the current shell.
        """
    def InitShape(self, S: OCP.TopoDS.TopoDS_Shape) -> None:
        """
        None
        """
    def InitShell(self) -> None:
        """
        Starts an exploration of the shells.
        """
    def Intersector(
        self, F: OCP.TopoDS.TopoDS_Face
    ) -> OCP.IntCurvesFace.IntCurvesFace_Intersector:
        """
        None
        """
    def MoreFace(self) -> bool:
        """
        Returns True if current face in current shell.
        """
    def MoreShell(self) -> bool:
        """
        Returns True if there is a current shell.
        """
    def NextFace(self) -> None:
        """
        Sets the explorer to the next Face of the current shell.
        """
    def NextShell(self) -> None:
        """
        Sets the explorer to the next shell.
        """
    def OtherSegment(self, P: OCP.gp.gp_Pnt, L: OCP.gp.gp_Lin, Par: float) -> int:
        """
        Returns in <L>, <Par> a segment having at least one intersection with the shape boundary to compute intersections.
        """
    @overload
    def PointInTheFace(
        self,
        F: OCP.TopoDS.TopoDS_Face,
        P: OCP.gp.gp_Pnt,
        u: float,
        v: float,
        Param: float,
        Index: int,
        surf: OCP.BRepAdaptor.BRepAdaptor_HSurface,
        u1: float,
        v1: float,
        u2: float,
        v2: float,
    ) -> bool:
        """
        None

        None

        <Index> gives point index to search from and returns point index of succeseful search
        """
    @overload
    def PointInTheFace(
        self,
        F: OCP.TopoDS.TopoDS_Face,
        P: OCP.gp.gp_Pnt,
        u: float,
        v: float,
        Param: float,
        Index: int,
        surf: OCP.BRepAdaptor.BRepAdaptor_HSurface,
        u1: float,
        v1: float,
        u2: float,
        v2: float,
        theVecD1U: OCP.gp.gp_Vec,
        theVecD1V: OCP.gp.gp_Vec,
    ) -> bool: ...
    @overload
    def PointInTheFace(
        self,
        F: OCP.TopoDS.TopoDS_Face,
        P: OCP.gp.gp_Pnt,
        u: float,
        v: float,
        Param: float,
        Index: int,
    ) -> bool: ...
    def Reject(self, P: OCP.gp.gp_Pnt) -> bool:
        """
        Should return True if P outside of bounding vol. of the shape
        """
    def RejectFace(self, L: OCP.gp.gp_Lin) -> bool:
        """
        returns True if the face is rejected.
        """
    def RejectShell(self, L: OCP.gp.gp_Lin) -> bool:
        """
        Returns True if the Shell is rejected.
        """
    def Segment(self, P: OCP.gp.gp_Pnt, L: OCP.gp.gp_Lin, Par: float) -> int:
        """
        Returns in <L>, <Par> a segment having at least one intersection with the shape boundary to compute intersections.
        """
    @overload
    def __init__(self, S: OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass

class BRepClass3d_SolidPassiveClassifier:
    """
    None
    """

    def Compare(
        self, F: OCP.TopoDS.TopoDS_Face, Or: OCP.TopAbs.TopAbs_Orientation
    ) -> None:
        """
        Updates the classification process with the face <F> from the boundary.
        """
    def HasIntersection(self) -> bool:
        """
        Returns True if an intersection is computed.
        """
    def Intersector(self) -> BRepClass3d_Intersector3d:
        """
        Returns the intersecting algorithm.
        """
    def Parameter(self) -> float:
        """
        Returns the current value of the parameter.
        """
    def Reset(self, L: OCP.gp.gp_Lin, P: float, Tol: float) -> None:
        """
        Starts a classification process. The point to classify is the origin of the line <L>. <P> is the original length of the segment on <L> used to compute intersections. <Tol> is the tolerance attached to the intersections.
        """
    def State(self) -> OCP.TopAbs.TopAbs_State:
        """
        Returns the current state of the point.
        """
    def __init__(self) -> None: ...
    pass
