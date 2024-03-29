import OCP.BRepLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.Adaptor3d
import OCP.TopLoc
import OCP.TopoDS
import OCP.BRepTools
import OCP.Poly
import OCP.gp
import OCP.Geom2d
import OCP.GeomAbs
import OCP.TopTools
__all__  = [
"BRepLib",
"BRepLib_Command",
"BRepLib_EdgeError",
"BRepLib_FaceError",
"BRepLib_FindSurface",
"BRepLib_FuseEdges",
"BRepLib_MakeShape",
"BRepLib_MakeEdge2d",
"BRepLib_MakeFace",
"BRepLib_MakePolygon",
"BRepLib_MakeEdge",
"BRepLib_MakeShell",
"BRepLib_MakeSolid",
"BRepLib_MakeVertex",
"BRepLib_MakeWire",
"BRepLib_PointCloudShape",
"BRepLib_ShapeModification",
"BRepLib_ShellError",
"BRepLib_ToolTriangulatedShape",
"BRepLib_ValidateEdge",
"BRepLib_WireError",
"BRepLib_BoundaryModified",
"BRepLib_CurveProjectionFailed",
"BRepLib_Deleted",
"BRepLib_DifferentPointsOnClosedCurve",
"BRepLib_DifferentsPointAndParameter",
"BRepLib_DisconnectedShell",
"BRepLib_DisconnectedWire",
"BRepLib_EdgeDone",
"BRepLib_EmptyShell",
"BRepLib_EmptyWire",
"BRepLib_FaceDone",
"BRepLib_LineThroughIdenticPoints",
"BRepLib_Merged",
"BRepLib_NoFace",
"BRepLib_NonManifoldWire",
"BRepLib_NotPlanar",
"BRepLib_ParameterOutOfRange",
"BRepLib_ParametersOutOfRange",
"BRepLib_PointProjectionFailed",
"BRepLib_PointWithInfiniteParameter",
"BRepLib_Preserved",
"BRepLib_ShellDone",
"BRepLib_ShellParametersOutOfRange",
"BRepLib_Trimmed",
"BRepLib_WireDone"
]
class BRepLib():
    """
    The BRepLib package provides general utilities for BRep.
    """
    @staticmethod
    def BoundingVertex_s(theLV : OCP.TopTools.TopTools_ListOfShape,theNewCenter : OCP.gp.gp_Pnt) -> Tuple[float]: 
        """
        Calculates the bounding sphere around the set of vertexes from the theLV list. Returns the center (theNewCenter) and the radius (theNewTol) of this sphere. This can be used to construct the new vertex which covers the given set of other vertices.
        """
    @staticmethod
    def BuildCurve3d_s(E : OCP.TopoDS.TopoDS_Edge,Tolerance : float=1e-05,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1,MaxDegree : int=14,MaxSegment : int=0) -> bool: 
        """
        Computes the 3d curve for the edge <E> if it does not exist. Returns True if the curve was computed or existed. Returns False if there is no planar pcurve or the computation failed. <MaxSegment> >= 30 in approximation
        """
    @staticmethod
    @overload
    def BuildCurves3d_s(S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Computes the 3d curves for all the edges of <S> return False if one of the computation failed. <MaxSegment> >= 30 in approximation

        Computes the 3d curves for all the edges of <S> return False if one of the computation failed.
        """
    @staticmethod
    @overload
    def BuildCurves3d_s(S : OCP.TopoDS.TopoDS_Shape,Tolerance : float,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1,MaxDegree : int=14,MaxSegment : int=0) -> bool: ...
    @staticmethod
    @overload
    def BuildPCurveForEdgeOnPlane_s(theE : OCP.TopoDS.TopoDS_Edge,theF : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Builds pcurve of edge on face if the surface is plane, and updates the edge.

        Builds pcurve of edge on face if the surface is plane, but does not update the edge. The output are the pcurve and the flag telling that pcurve was built.
        """
    @staticmethod
    @overload
    def BuildPCurveForEdgeOnPlane_s(theE : OCP.TopoDS.TopoDS_Edge,theF : OCP.TopoDS.TopoDS_Face,aC2D : OCP.Geom2d.Geom2d_Curve) -> Tuple[bool]: ...
    @staticmethod
    def CheckSameRange_s(E : OCP.TopoDS.TopoDS_Edge,Confusion : float=1e-12) -> bool: 
        """
        checks if the Edge is same range IGNORING the same range flag of the edge Confusion argument is to compare real numbers idenpendently of any model space tolerance
        """
    @staticmethod
    def ContinuityOfFaces_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace1 : OCP.TopoDS.TopoDS_Face,theFace2 : OCP.TopoDS.TopoDS_Face,theAngleTol : float) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the order of continuity between two faces connected by an edge
        """
    @staticmethod
    @overload
    def EncodeRegularity_s(S : OCP.TopoDS.TopoDS_Shape,LE : OCP.TopTools.TopTools_ListOfShape,TolAng : float=1e-10) -> None: 
        """
        Encodes the Regularity of edges on a Shape. Warning: <TolAng> is an angular tolerance, expressed in Rad. Warning: If the edges's regularity are coded before, nothing is done.

        Encodes the Regularity of edges in list <LE> on the shape <S> Warning: <TolAng> is an angular tolerance, expressed in Rad. Warning: If the edges's regularity are coded before, nothing is done.

        Encodes the Regularity between <F1> and <F2> by <E> Warning: <TolAng> is an angular tolerance, expressed in Rad. Warning: If the edge's regularity is coded before, nothing is done.
        """
    @staticmethod
    @overload
    def EncodeRegularity_s(E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,TolAng : float=1e-10) -> None: ...
    @staticmethod
    @overload
    def EncodeRegularity_s(S : OCP.TopoDS.TopoDS_Shape,TolAng : float=1e-10) -> None: ...
    @staticmethod
    def EnsureNormalConsistency_s(S : OCP.TopoDS.TopoDS_Shape,theAngTol : float=0.001,ForceComputeNormals : bool=False) -> bool: 
        """
        Corrects the normals in Poly_Triangulation of faces, in such way that normals at nodes lying along smooth edges have the same value on both adjacent triangulations. Returns TRUE if any correction is done.
        """
    @staticmethod
    def ExtendFace_s(theF : OCP.TopoDS.TopoDS_Face,theExtVal : float,theExtUMin : bool,theExtUMax : bool,theExtVMin : bool,theExtVMax : bool,theFExtended : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Enlarges the face on the given value.
        """
    @staticmethod
    @overload
    def FindValidRange_s(theCurve : OCP.Adaptor3d.Adaptor3d_Curve,theTolE : float,theParV1 : float,thePntV1 : OCP.gp.gp_Pnt,theTolV1 : float,theParV2 : float,thePntV2 : OCP.gp.gp_Pnt,theTolV2 : float,theFirst : float,theLast : float) -> bool: 
        """
        For an edge defined by 3d curve and tolerance and vertices defined by points, parameters on curve and tolerances, finds a range of curve between vertices not covered by vertices tolerances. Returns false if there is no such range. Otherwise, sets theFirst and theLast as its bounds.

        Finds a range of 3d curve of the edge not covered by vertices tolerances. Returns false if there is no such range. Otherwise, sets theFirst and theLast as its bounds.
        """
    @staticmethod
    @overload
    def FindValidRange_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFirst : float,theLast : float) -> bool: ...
    @staticmethod
    def OrientClosedSolid_s(solid : OCP.TopoDS.TopoDS_Solid) -> bool: 
        """
        Orients the solid forward and the shell with the orientation to have matter in the solid. Returns False if the solid is unOrientable (open or incoherent)
        """
    @staticmethod
    @overload
    def Plane_s(P : OCP.Geom.Geom_Plane) -> None: 
        """
        Sets the current plane to P.

        Returns the current plane.
        """
    @staticmethod
    @overload
    def Plane_s() -> OCP.Geom.Geom_Plane: ...
    @staticmethod
    @overload
    def Precision_s(P : float) -> None: 
        """
        Computes the max distance between edge and its 2d representation on the face. Sets the default precision. The current Precision is returned.

        Returns the default precision.
        """
    @staticmethod
    @overload
    def Precision_s() -> float: ...
    @staticmethod
    def ReverseSortFaces_s(S : OCP.TopoDS.TopoDS_Shape,LF : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sorts in LF the Faces of S on the reverse complexity of their surfaces (other,Torus,Sphere,Cone,Cylinder,Plane)
        """
    @staticmethod
    @overload
    def SameParameter_s(S : OCP.TopoDS.TopoDS_Shape,theReshaper : OCP.BRepTools.BRepTools_ReShape,Tolerance : float=1e-05,forced : bool=False) -> None: 
        """
        Computes new 2d curve(s) for the edge <theEdge> to have the same parameter as the 3d curve. The algorithm is not done if the flag SameParameter was True on the Edge.

        Computes new 2d curve(s) for the edge <theEdge> to have the same parameter as the 3d curve. The algorithm is not done if the flag SameParameter was True on the Edge. theNewTol is a new tolerance of vertices of the input edge (not applied inside the algorithm, but pre-computed). If IsUseOldEdge is true then the input edge will be modified, otherwise the new copy of input edge will be created. Returns the new edge as a result, can be ignored if IsUseOldEdge is true.

        Computes new 2d curve(s) for all the edges of <S> to have the same parameter as the 3d curve. The algorithm is not done if the flag SameParameter was True on an Edge.

        Computes new 2d curve(s) for all the edges of <S> to have the same parameter as the 3d curve. The algorithm is not done if the flag SameParameter was True on an Edge. theReshaper is used to record the modifications of input shape <S> to prevent any modifications on the shape itself. Thus the input shape (and its subshapes) will not be modified, instead the reshaper will contain a modified empty-copies of original subshapes as substitutions.
        """
    @staticmethod
    @overload
    def SameParameter_s(theEdge : OCP.TopoDS.TopoDS_Edge,theTolerance : float,theNewTol : float,IsUseOldEdge : bool) -> OCP.TopoDS.TopoDS_Edge: ...
    @staticmethod
    @overload
    def SameParameter_s(theEdge : OCP.TopoDS.TopoDS_Edge,Tolerance : float=1e-05) -> None: ...
    @staticmethod
    @overload
    def SameParameter_s(S : OCP.TopoDS.TopoDS_Shape,Tolerance : float=1e-05,forced : bool=False) -> None: ...
    @staticmethod
    def SameRange_s(E : OCP.TopoDS.TopoDS_Edge,Tolerance : float=1e-05) -> None: 
        """
        will make all the curve representation have the same range domain for the parameters. This will IGNORE the same range flag value to proceed. If there is a 3D curve there it will the range of that curve. If not the first curve representation encountered in the list will give its range to the all the other curves.
        """
    @staticmethod
    def SortFaces_s(S : OCP.TopoDS.TopoDS_Shape,LF : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sorts in LF the Faces of S on the complexity of their surfaces (Plane,Cylinder,Cone,Sphere,Torus,other)
        """
    @staticmethod
    def UpdateDeflection_s(S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Updates value of deflection in Poly_Triangulation of faces by the maximum deviation measured on existing triangulation.
        """
    @staticmethod
    def UpdateEdgeTol_s(E : OCP.TopoDS.TopoDS_Edge,MinToleranceRequest : float,MaxToleranceToCheck : float) -> bool: 
        """
        Checks if the edge has a Tolerance smaller than -- -- -- -- MaxToleranceToCheck if so it will compute the radius of -- the cylindrical pipe surface that MinToleranceRequest is the minimum tolerance before it is useful to start testing. Usually it should be around 10e-5 contains all -- the curve representation of the edge returns True if the Edge tolerance had to be updated
        """
    @staticmethod
    def UpdateEdgeTolerance_s(S : OCP.TopoDS.TopoDS_Shape,MinToleranceRequest : float,MaxToleranceToCheck : float) -> bool: 
        """
        -- Checks all the edges of the shape whose -- -- -- Tolerance is smaller than MaxToleranceToCheck -- Returns True if at least one edge was updated -- MinToleranceRequest is the minimum tolerance before -- it -- is useful to start testing. Usually it should be around -- 10e-5--
        """
    @staticmethod
    def UpdateInnerTolerances_s(S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Checks tolerances of edges (including inner points) and vertices of a shape and updates them to satisfy "SameParameter" condition
        """
    @staticmethod
    @overload
    def UpdateTolerances_s(S : OCP.TopoDS.TopoDS_Shape,theReshaper : OCP.BRepTools.BRepTools_ReShape,verifyFaceTolerance : bool=False) -> None: 
        """
        Replaces tolerance of FACE EDGE VERTEX by the tolerance Max of their connected handling shapes. It is not necessary to use this call after SameParameter. (called in)

        Replaces tolerance of FACE EDGE VERTEX by the tolerance Max of their connected handling shapes. It is not necessary to use this call after SameParameter. (called in) theReshaper is used to record the modifications of input shape <S> to prevent any modifications on the shape itself. Thus the input shape (and its subshapes) will not be modified, instead the reshaper will contain a modified empty-copies of original subshapes as substitutions.
        """
    @staticmethod
    @overload
    def UpdateTolerances_s(S : OCP.TopoDS.TopoDS_Shape,verifyFaceTolerance : bool=False) -> None: ...
    def __init__(self) -> None: ...
    pass
class BRepLib_Command():
    """
    Root class for all commands in BRepLib.
    """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    pass
class BRepLib_EdgeError():
    """
    Errors that can occur at edge construction. no error

    Members:

      BRepLib_EdgeDone

      BRepLib_PointProjectionFailed

      BRepLib_ParameterOutOfRange

      BRepLib_DifferentPointsOnClosedCurve

      BRepLib_PointWithInfiniteParameter

      BRepLib_DifferentsPointAndParameter

      BRepLib_LineThroughIdenticPoints
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
    BRepLib_DifferentPointsOnClosedCurve: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_DifferentPointsOnClosedCurve: 3>
    BRepLib_DifferentsPointAndParameter: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_DifferentsPointAndParameter: 5>
    BRepLib_EdgeDone: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_EdgeDone: 0>
    BRepLib_LineThroughIdenticPoints: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_LineThroughIdenticPoints: 6>
    BRepLib_ParameterOutOfRange: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_ParameterOutOfRange: 2>
    BRepLib_PointProjectionFailed: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_PointProjectionFailed: 1>
    BRepLib_PointWithInfiniteParameter: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_PointWithInfiniteParameter: 4>
    __entries: dict # value = {'BRepLib_EdgeDone': (<BRepLib_EdgeError.BRepLib_EdgeDone: 0>, None), 'BRepLib_PointProjectionFailed': (<BRepLib_EdgeError.BRepLib_PointProjectionFailed: 1>, None), 'BRepLib_ParameterOutOfRange': (<BRepLib_EdgeError.BRepLib_ParameterOutOfRange: 2>, None), 'BRepLib_DifferentPointsOnClosedCurve': (<BRepLib_EdgeError.BRepLib_DifferentPointsOnClosedCurve: 3>, None), 'BRepLib_PointWithInfiniteParameter': (<BRepLib_EdgeError.BRepLib_PointWithInfiniteParameter: 4>, None), 'BRepLib_DifferentsPointAndParameter': (<BRepLib_EdgeError.BRepLib_DifferentsPointAndParameter: 5>, None), 'BRepLib_LineThroughIdenticPoints': (<BRepLib_EdgeError.BRepLib_LineThroughIdenticPoints: 6>, None)}
    __members__: dict # value = {'BRepLib_EdgeDone': <BRepLib_EdgeError.BRepLib_EdgeDone: 0>, 'BRepLib_PointProjectionFailed': <BRepLib_EdgeError.BRepLib_PointProjectionFailed: 1>, 'BRepLib_ParameterOutOfRange': <BRepLib_EdgeError.BRepLib_ParameterOutOfRange: 2>, 'BRepLib_DifferentPointsOnClosedCurve': <BRepLib_EdgeError.BRepLib_DifferentPointsOnClosedCurve: 3>, 'BRepLib_PointWithInfiniteParameter': <BRepLib_EdgeError.BRepLib_PointWithInfiniteParameter: 4>, 'BRepLib_DifferentsPointAndParameter': <BRepLib_EdgeError.BRepLib_DifferentsPointAndParameter: 5>, 'BRepLib_LineThroughIdenticPoints': <BRepLib_EdgeError.BRepLib_LineThroughIdenticPoints: 6>}
    pass
class BRepLib_FaceError():
    """
    Errors that can occur at face construction. no error not initialised

    Members:

      BRepLib_FaceDone

      BRepLib_NoFace

      BRepLib_NotPlanar

      BRepLib_CurveProjectionFailed

      BRepLib_ParametersOutOfRange
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
    BRepLib_CurveProjectionFailed: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_CurveProjectionFailed: 3>
    BRepLib_FaceDone: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_FaceDone: 0>
    BRepLib_NoFace: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_NoFace: 1>
    BRepLib_NotPlanar: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_NotPlanar: 2>
    BRepLib_ParametersOutOfRange: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_ParametersOutOfRange: 4>
    __entries: dict # value = {'BRepLib_FaceDone': (<BRepLib_FaceError.BRepLib_FaceDone: 0>, None), 'BRepLib_NoFace': (<BRepLib_FaceError.BRepLib_NoFace: 1>, None), 'BRepLib_NotPlanar': (<BRepLib_FaceError.BRepLib_NotPlanar: 2>, None), 'BRepLib_CurveProjectionFailed': (<BRepLib_FaceError.BRepLib_CurveProjectionFailed: 3>, None), 'BRepLib_ParametersOutOfRange': (<BRepLib_FaceError.BRepLib_ParametersOutOfRange: 4>, None)}
    __members__: dict # value = {'BRepLib_FaceDone': <BRepLib_FaceError.BRepLib_FaceDone: 0>, 'BRepLib_NoFace': <BRepLib_FaceError.BRepLib_NoFace: 1>, 'BRepLib_NotPlanar': <BRepLib_FaceError.BRepLib_NotPlanar: 2>, 'BRepLib_CurveProjectionFailed': <BRepLib_FaceError.BRepLib_CurveProjectionFailed: 3>, 'BRepLib_ParametersOutOfRange': <BRepLib_FaceError.BRepLib_ParametersOutOfRange: 4>}
    pass
class BRepLib_FindSurface():
    """
    Provides an algorithm to find a Surface through a set of edges.
    """
    def Existed(self) -> bool: 
        """
        None
        """
    def Found(self) -> bool: 
        """
        None
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape,Tol : float=-1.0,OnlyPlane : bool=False,OnlyClosed : bool=False) -> None: 
        """
        Computes the Surface from the edges of <S> with the given tolerance. if <OnlyPlane> is true, the computed surface will be a plane. If it is not possible to find a plane, the flag NotDone will be set. If <OnlyClosed> is true, then S should be a wire and the existing surface, on which wire S is not closed in 2D, will be ignored.
        """
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        None
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Tolerance(self) -> float: 
        """
        None
        """
    def ToleranceReached(self) -> float: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,Tol : float=-1.0,OnlyPlane : bool=False,OnlyClosed : bool=False) -> None: ...
    pass
class BRepLib_FuseEdges():
    """
    This class can detect vertices in a face that can be considered useless and then perform the fuse of the edges and remove the useless vertices. By useles vertices, we mean : * vertices that have exactly two connex edges * the edges connex to the vertex must have exactly the same 2 connex faces . * The edges connex to the vertex must have the same geometric support.
    """
    def AvoidEdges(self,theMapEdg : OCP.TopTools.TopTools_IndexedMapOfShape) -> None: 
        """
        set edges to avoid being fused
        """
    def Edges(self,theMapLstEdg : OCP.TopTools.TopTools_DataMapOfIntegerListOfShape) -> None: 
        """
        returns all the list of edges to be fused each list of the map represent a set of connex edges that can be fused.
        """
    def Faces(self,theMapFac : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        returns the map of modified faces.
        """
    def NbVertices(self) -> int: 
        """
        returns the number of vertices candidate to be removed
        """
    def Perform(self) -> None: 
        """
        Using map of list of connex edges, fuse each list to one edge and then update myShape
        """
    def ResultEdges(self,theMapEdg : OCP.TopTools.TopTools_DataMapOfIntegerShape) -> None: 
        """
        returns all the fused edges. each integer entry in the map corresponds to the integer in the DataMapOfIntegerListOfShape we get in method Edges. That is to say, to the list of edges in theMapLstEdg(i) corresponds the resulting edge theMapEdge(i)
        """
    def SetConcatBSpl(self,theConcatBSpl : bool=True) -> None: 
        """
        set mode to enable concatenation G1 BSpline edges in one End Modified by IFV 19.04.07
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns myShape modified with the list of internal edges removed from it.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape,PerformNow : bool=False) -> None: ...
    pass
class BRepLib_MakeShape(BRepLib_Command):
    """
    This is the root class for all shape constructions. It stores the result.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def FaceStatus(self,F : OCP.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification: 
        """
        returns the status of the Face after the shape creation.
        """
    def FacesFromEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the edge <E>.
        """
    def HasDescendants(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face generates new topology.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface I.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    pass
class BRepLib_MakeEdge2d(BRepLib_MakeShape, BRepLib_Command):
    """
    Provides methods to build edges.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def Error(self) -> BRepLib_EdgeError: 
        """
        Returns the error description when NotDone.
        """
    def FaceStatus(self,F : OCP.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification: 
        """
        returns the status of the Face after the shape creation.
        """
    def FacesFromEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the edge <E>.
        """
    def HasDescendants(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face generates new topology.
        """
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None

        None

        None

        None

        None

        None
        """
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,p1 : float,p2 : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface I.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Vertex1(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the first vertex of the edge. May be Null.
        """
    def Vertex2(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the second vertex of the edge. May be Null.
        """
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab2d,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips2d) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips2d,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ2d,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr2d,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr2d,p1 : float,p2 : float) -> None: ...
    pass
class BRepLib_MakeFace(BRepLib_MakeShape, BRepLib_Command):
    """
    Provides methods to build faces.
    """
    def Add(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Adds the wire <W> in the current face.
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def Error(self) -> BRepLib_FaceError: 
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the new face.
        """
    def FaceStatus(self,F : OCP.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification: 
        """
        returns the status of the Face after the shape creation.
        """
    def FacesFromEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the edge <E>.
        """
    def HasDescendants(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face generates new topology.
        """
    @overload
    def Init(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Load the face.

        Creates the face from the surface. If Bound is True a wire is made from the natural bounds. Accepts tolerance value (TolDegen) for resolution of degenerated edges.

        Creates the face from the surface and the min-max values. Accepts tolerance value (TolDegen) for resolution of degenerated edges.
        """
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface,Bound : bool,TolDegen : float) -> None: ...
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface,UMin : float,UMax : float,VMin : float,VMax : float,TolDegen : float) -> None: ...
    @staticmethod
    def IsDegenerated_s(theCurve : OCP.Geom.Geom_Curve,theMaxTol : float,theActTol : float) -> bool: 
        """
        Checks the specified curve is degenerated according to specified tolerance. Returns <theActTol> less than <theMaxTol>, which shows actual tolerance to decide the curve is degenerated. Warning: For internal use of BRepLib_MakeFace and BRepLib_MakeShell.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface I.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,W : OCP.TopoDS.TopoDS_Wire) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cone,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Torus) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cone) -> None: ...
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface,TolDegen : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface,UMin : float,UMax : float,VMin : float,VMax : float,TolDegen : float) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Torus,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Torus,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cone,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,OnlyPlane : bool=False) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
class BRepLib_MakePolygon(BRepLib_MakeShape, BRepLib_Command):
    """
    Class to build polygonal wires.
    """
    @overload
    def Add(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        None

        None
        """
    @overload
    def Add(self,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    def Added(self) -> bool: 
        """
        Returns True if the last vertex or point was successfully added.
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Close(self) -> None: 
        """
        None
        """
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the last edge added to the polygon.
        """
    def FaceStatus(self,F : OCP.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification: 
        """
        returns the status of the Face after the shape creation.
        """
    def FacesFromEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the edge <E>.
        """
    def FirstVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def HasDescendants(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face generates new topology.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface I.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        None
        """
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,V3 : OCP.TopoDS.TopoDS_Vertex,V4 : OCP.TopoDS.TopoDS_Vertex,Close : bool=False) -> None: ...
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,V3 : OCP.TopoDS.TopoDS_Vertex,Close : bool=False) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt,P4 : OCP.gp.gp_Pnt,Close : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt,Close : bool=False) -> None: ...
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    pass
class BRepLib_MakeEdge(BRepLib_MakeShape, BRepLib_Command):
    """
    Provides methods to build edges.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def Error(self) -> BRepLib_EdgeError: 
        """
        Returns the error description when NotDone.
        """
    def FaceStatus(self,F : OCP.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification: 
        """
        returns the status of the Face after the shape creation.
        """
    def FacesFromEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the edge <E>.
        """
    def HasDescendants(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face generates new topology.
        """
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface I.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Vertex1(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the first vertex of the edge. May be Null.
        """
    def Vertex2(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the second vertex of the edge. May be Null.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepLib_MakeShell(BRepLib_MakeShape, BRepLib_Command):
    """
    Provides methods to build shells.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def Error(self) -> BRepLib_ShellError: 
        """
        None
        """
    def FaceStatus(self,F : OCP.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification: 
        """
        returns the status of the Face after the shape creation.
        """
    def FacesFromEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the edge <E>.
        """
    def HasDescendants(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face generates new topology.
        """
    def Init(self,S : OCP.Geom.Geom_Surface,UMin : float,UMax : float,VMin : float,VMax : float,Segment : bool=False) -> None: 
        """
        Creates the shell from the surface and the min-max values.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface I.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the new Shell.
        """
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface,Segment : bool=False) -> None: ...
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface,UMin : float,UMax : float,VMin : float,VMax : float,Segment : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepLib_MakeSolid(BRepLib_MakeShape, BRepLib_Command):
    """
    Makes a solid from compsolid or shells.
    """
    def Add(self,S : OCP.TopoDS.TopoDS_Shell) -> None: 
        """
        Add the shell to the current solid.
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def FaceStatus(self,F : OCP.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification: 
        """
        returns the status of the Face after the shape creation.
        """
    def FacesFromEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the edge <E>.
        """
    def HasDescendants(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face generates new topology.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface I.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the new Solid.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shell) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_CompSolid) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,So : OCP.TopoDS.TopoDS_Solid) -> None: ...
    @overload
    def __init__(self,So : OCP.TopoDS.TopoDS_Solid,S : OCP.TopoDS.TopoDS_Shell) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shell,S2 : OCP.TopoDS.TopoDS_Shell,S3 : OCP.TopoDS.TopoDS_Shell) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shell,S2 : OCP.TopoDS.TopoDS_Shell) -> None: ...
    pass
class BRepLib_MakeVertex(BRepLib_MakeShape, BRepLib_Command):
    """
    Provides methods to build vertices.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def FaceStatus(self,F : OCP.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification: 
        """
        returns the status of the Face after the shape creation.
        """
    def FacesFromEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the edge <E>.
        """
    def HasDescendants(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face generates new topology.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface I.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def __init__(self,P : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepLib_MakeWire(BRepLib_MakeShape, BRepLib_Command):
    """
    Provides methods to build wires.
    """
    @overload
    def Add(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Add the edge <E> to the current wire.

        Add the edges of <W> to the current wire.

        Add the edges of <L> to the current wire. The edges are not to be consecutive. But they are to be all connected geometrically or topologically.
        """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def Add(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DescendantFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the last edge added to the wire.
        """
    def Error(self) -> BRepLib_WireError: 
        """
        None
        """
    def FaceStatus(self,F : OCP.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification: 
        """
        returns the status of the Face after the shape creation.
        """
    def FacesFromEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the edge <E>.
        """
    def HasDescendants(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face generates new topology.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface I.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the last connecting vertex.
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the new wire.
        """
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,E3 : OCP.TopoDS.TopoDS_Edge,E4 : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,E3 : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire) -> None: ...
    pass
class BRepLib_PointCloudShape():
    """
    This tool is intended to get points from shape with specified distance from shape along normal. Can be used to simulation of points obtained in result of laser scan of shape. There are 2 ways for generation points by shape: 1. Generation points with specified density 2. Generation points using triangulation Nodes Generation of points by density using the GeneratePointsByDensity() function is not thread safe.
    """
    def GeneratePointsByDensity(self,theDensity : float=0.0) -> bool: 
        """
        Computes points with specified density for initial shape. If parameter Density is equal to 0 then density will be computed automatically by criterion: - 10 points per minimal unreduced face area.
        """
    def GeneratePointsByTriangulation(self) -> bool: 
        """
        Get points from triangulation existing in the shape.
        """
    def GetDistance(self) -> float: 
        """
        Returns value of the distance to define deflection of points from shape along normal to shape; 0.0 by default.
        """
    def NbPointsByDensity(self,theDensity : float=0.0) -> int: 
        """
        Returns size of the point cloud for specified density.
        """
    def NbPointsByTriangulation(self) -> int: 
        """
        Returns size of the point cloud for using triangulation.
        """
    def SetDistance(self,theDist : float) -> None: 
        """
        Sets value of the distance to define deflection of points from shape along normal to shape. Negative values of theDist parameter are ignored.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set shape.
        """
    def SetTolerance(self,theTol : float) -> None: 
        """
        Set tolerance.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Return loaded shape.
        """
    def Tolerance(self) -> float: 
        """
        Return tolerance.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape=OCP.TopoDS.TopoDS_Shape,theTol : float=1e-07) -> None: ...
    pass
class BRepLib_ShapeModification():
    """
    Modification type after a topologic operation.

    Members:

      BRepLib_Preserved

      BRepLib_Deleted

      BRepLib_Trimmed

      BRepLib_Merged

      BRepLib_BoundaryModified
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
    BRepLib_BoundaryModified: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_BoundaryModified: 4>
    BRepLib_Deleted: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_Deleted: 1>
    BRepLib_Merged: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_Merged: 3>
    BRepLib_Preserved: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_Preserved: 0>
    BRepLib_Trimmed: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_Trimmed: 2>
    __entries: dict # value = {'BRepLib_Preserved': (<BRepLib_ShapeModification.BRepLib_Preserved: 0>, None), 'BRepLib_Deleted': (<BRepLib_ShapeModification.BRepLib_Deleted: 1>, None), 'BRepLib_Trimmed': (<BRepLib_ShapeModification.BRepLib_Trimmed: 2>, None), 'BRepLib_Merged': (<BRepLib_ShapeModification.BRepLib_Merged: 3>, None), 'BRepLib_BoundaryModified': (<BRepLib_ShapeModification.BRepLib_BoundaryModified: 4>, None)}
    __members__: dict # value = {'BRepLib_Preserved': <BRepLib_ShapeModification.BRepLib_Preserved: 0>, 'BRepLib_Deleted': <BRepLib_ShapeModification.BRepLib_Deleted: 1>, 'BRepLib_Trimmed': <BRepLib_ShapeModification.BRepLib_Trimmed: 2>, 'BRepLib_Merged': <BRepLib_ShapeModification.BRepLib_Merged: 3>, 'BRepLib_BoundaryModified': <BRepLib_ShapeModification.BRepLib_BoundaryModified: 4>}
    pass
class BRepLib_ShellError():
    """
    Errors that can occur at shell construction.

    Members:

      BRepLib_ShellDone

      BRepLib_EmptyShell

      BRepLib_DisconnectedShell

      BRepLib_ShellParametersOutOfRange
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
    BRepLib_DisconnectedShell: OCP.BRepLib.BRepLib_ShellError # value = <BRepLib_ShellError.BRepLib_DisconnectedShell: 2>
    BRepLib_EmptyShell: OCP.BRepLib.BRepLib_ShellError # value = <BRepLib_ShellError.BRepLib_EmptyShell: 1>
    BRepLib_ShellDone: OCP.BRepLib.BRepLib_ShellError # value = <BRepLib_ShellError.BRepLib_ShellDone: 0>
    BRepLib_ShellParametersOutOfRange: OCP.BRepLib.BRepLib_ShellError # value = <BRepLib_ShellError.BRepLib_ShellParametersOutOfRange: 3>
    __entries: dict # value = {'BRepLib_ShellDone': (<BRepLib_ShellError.BRepLib_ShellDone: 0>, None), 'BRepLib_EmptyShell': (<BRepLib_ShellError.BRepLib_EmptyShell: 1>, None), 'BRepLib_DisconnectedShell': (<BRepLib_ShellError.BRepLib_DisconnectedShell: 2>, None), 'BRepLib_ShellParametersOutOfRange': (<BRepLib_ShellError.BRepLib_ShellParametersOutOfRange: 3>, None)}
    __members__: dict # value = {'BRepLib_ShellDone': <BRepLib_ShellError.BRepLib_ShellDone: 0>, 'BRepLib_EmptyShell': <BRepLib_ShellError.BRepLib_EmptyShell: 1>, 'BRepLib_DisconnectedShell': <BRepLib_ShellError.BRepLib_DisconnectedShell: 2>, 'BRepLib_ShellParametersOutOfRange': <BRepLib_ShellError.BRepLib_ShellParametersOutOfRange: 3>}
    pass
class BRepLib_ToolTriangulatedShape():
    """
    Provides methods for calculating normals to Poly_Triangulation of TopoDS_Face.
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
    def __init__(self) -> None: ...
    pass
class BRepLib_ValidateEdge():
    """
    Computes the max distance between 3D-curve and curve on surface. This class uses 2 methods: approximate using finite number of points (default) and exact
    """
    def CheckTolerance(self,theToleranceToCheck : float) -> bool: 
        """
        Returns true if computed distance is less than <theToleranceToCheck>
        """
    def GetMaxDistance(self) -> float: 
        """
        Returns max distance
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the distance has been found for all points
        """
    def IsExactMethod(self) -> bool: 
        """
        Returns true if exact method selected
        """
    def IsParallel(self) -> bool: 
        """
        Returns true if parallel flag is set
        """
    def Process(self) -> None: 
        """
        Computes the max distance for the 3d curve <myReferenceCurve> and curve on surface <myOtherCurve>. If the SetExitIfToleranceExceeded() function was called before <myCalculatedDistance> contains first greater than SetExitIfToleranceExceeded() parameter value. In case using exact method always computes real max distance.
        """
    def SetControlPointsNumber(self,theControlPointsNumber : int) -> None: 
        """
        Set control points number (if you need a value other than 22)
        """
    def SetExactMethod(self,theIsExact : bool) -> None: 
        """
        Sets method to calculate distance: Calculating in finite number of points (if theIsExact is false, faster, but possible not correct result) or exact calculating by using BRepLib_CheckCurveOnSurface class (if theIsExact is true, slowly, but more correctly). Exact method is used only when edge is SameParameter. Default method is calculating in finite number of points
        """
    def SetParallel(self,theIsMultiThread : bool) -> None: 
        """
        Sets parallel flag
        """
    def UpdateTolerance(self) -> Tuple[float]: 
        """
        Increase <theToleranceToUpdate> if max distance is greater than <theToleranceToUpdate>
        """
    def __init__(self,theReferenceCurve : OCP.Adaptor3d.Adaptor3d_Curve,theOtherCurve : OCP.Adaptor3d.Adaptor3d_CurveOnSurface,theSameParameter : bool) -> None: ...
    pass
class BRepLib_WireError():
    """
    Errors that can occur at wire construction. no error

    Members:

      BRepLib_WireDone

      BRepLib_EmptyWire

      BRepLib_DisconnectedWire

      BRepLib_NonManifoldWire
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
    BRepLib_DisconnectedWire: OCP.BRepLib.BRepLib_WireError # value = <BRepLib_WireError.BRepLib_DisconnectedWire: 2>
    BRepLib_EmptyWire: OCP.BRepLib.BRepLib_WireError # value = <BRepLib_WireError.BRepLib_EmptyWire: 1>
    BRepLib_NonManifoldWire: OCP.BRepLib.BRepLib_WireError # value = <BRepLib_WireError.BRepLib_NonManifoldWire: 3>
    BRepLib_WireDone: OCP.BRepLib.BRepLib_WireError # value = <BRepLib_WireError.BRepLib_WireDone: 0>
    __entries: dict # value = {'BRepLib_WireDone': (<BRepLib_WireError.BRepLib_WireDone: 0>, None), 'BRepLib_EmptyWire': (<BRepLib_WireError.BRepLib_EmptyWire: 1>, None), 'BRepLib_DisconnectedWire': (<BRepLib_WireError.BRepLib_DisconnectedWire: 2>, None), 'BRepLib_NonManifoldWire': (<BRepLib_WireError.BRepLib_NonManifoldWire: 3>, None)}
    __members__: dict # value = {'BRepLib_WireDone': <BRepLib_WireError.BRepLib_WireDone: 0>, 'BRepLib_EmptyWire': <BRepLib_WireError.BRepLib_EmptyWire: 1>, 'BRepLib_DisconnectedWire': <BRepLib_WireError.BRepLib_DisconnectedWire: 2>, 'BRepLib_NonManifoldWire': <BRepLib_WireError.BRepLib_NonManifoldWire: 3>}
    pass
BRepLib_BoundaryModified: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_BoundaryModified: 4>
BRepLib_CurveProjectionFailed: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_CurveProjectionFailed: 3>
BRepLib_Deleted: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_Deleted: 1>
BRepLib_DifferentPointsOnClosedCurve: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_DifferentPointsOnClosedCurve: 3>
BRepLib_DifferentsPointAndParameter: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_DifferentsPointAndParameter: 5>
BRepLib_DisconnectedShell: OCP.BRepLib.BRepLib_ShellError # value = <BRepLib_ShellError.BRepLib_DisconnectedShell: 2>
BRepLib_DisconnectedWire: OCP.BRepLib.BRepLib_WireError # value = <BRepLib_WireError.BRepLib_DisconnectedWire: 2>
BRepLib_EdgeDone: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_EdgeDone: 0>
BRepLib_EmptyShell: OCP.BRepLib.BRepLib_ShellError # value = <BRepLib_ShellError.BRepLib_EmptyShell: 1>
BRepLib_EmptyWire: OCP.BRepLib.BRepLib_WireError # value = <BRepLib_WireError.BRepLib_EmptyWire: 1>
BRepLib_FaceDone: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_FaceDone: 0>
BRepLib_LineThroughIdenticPoints: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_LineThroughIdenticPoints: 6>
BRepLib_Merged: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_Merged: 3>
BRepLib_NoFace: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_NoFace: 1>
BRepLib_NonManifoldWire: OCP.BRepLib.BRepLib_WireError # value = <BRepLib_WireError.BRepLib_NonManifoldWire: 3>
BRepLib_NotPlanar: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_NotPlanar: 2>
BRepLib_ParameterOutOfRange: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_ParameterOutOfRange: 2>
BRepLib_ParametersOutOfRange: OCP.BRepLib.BRepLib_FaceError # value = <BRepLib_FaceError.BRepLib_ParametersOutOfRange: 4>
BRepLib_PointProjectionFailed: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_PointProjectionFailed: 1>
BRepLib_PointWithInfiniteParameter: OCP.BRepLib.BRepLib_EdgeError # value = <BRepLib_EdgeError.BRepLib_PointWithInfiniteParameter: 4>
BRepLib_Preserved: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_Preserved: 0>
BRepLib_ShellDone: OCP.BRepLib.BRepLib_ShellError # value = <BRepLib_ShellError.BRepLib_ShellDone: 0>
BRepLib_ShellParametersOutOfRange: OCP.BRepLib.BRepLib_ShellError # value = <BRepLib_ShellError.BRepLib_ShellParametersOutOfRange: 3>
BRepLib_Trimmed: OCP.BRepLib.BRepLib_ShapeModification # value = <BRepLib_ShapeModification.BRepLib_Trimmed: 2>
BRepLib_WireDone: OCP.BRepLib.BRepLib_WireError # value = <BRepLib_WireError.BRepLib_WireDone: 0>
