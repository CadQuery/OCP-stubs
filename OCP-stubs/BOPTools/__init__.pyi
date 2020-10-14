import OCP.BOPTools
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.TColStd
import OCP.Geom2d
import OCP.SelectMgr
import OCP.TopTools
import OCP.Graphic3d
import OCP.TopoDS
import OCP.IntTools
import OCP.BRepAdaptor
import OCP.Geom
import OCP.NCollection
import OCP.gp
__all__  = [
"BOPTools_AlgoTools",
"BOPTools_AlgoTools2D",
"BOPTools_AlgoTools3D",
"BOPTools_Box2dTreeSelector",
"BOPTools_BoxTree",
"BOPTools_BoxTreeSelector",
"BOPTools_ConnexityBlock",
"BOPTools_CoupleOfShape",
"BOPTools_IndexedDataMapOfSetShape",
"BOPTools_ListOfConnexityBlock",
"BOPTools_ListOfCoupleOfShape",
"BOPTools_MapOfSet",
"BOPTools_Parallel",
"BOPTools_Set",
"BOPTools_SetMapHasher"
]
class BOPTools_AlgoTools():
    """
    Provides tools used in Boolean Operations algorithm: - Vertices intersection; - Vertex construction; - Edge construction; - Classification algorithms; - Making connexity blocks; - Shape validation.
    """
    @staticmethod
    def AreFacesSameDomain_s(theF1 : OCP.TopoDS.TopoDS_Face,theF2 : OCP.TopoDS.TopoDS_Face,theContext : OCP.IntTools.IntTools_Context,theFuzz : float=1e-07) -> bool: 
        """
        Checks if the given faces are same-domain, i.e. coincide.
        """
    @staticmethod
    def ComputeStateByOnePoint_s(theShape : OCP.TopoDS.TopoDS_Shape,theSolid : OCP.TopoDS.TopoDS_Solid,theTol : float,theContext : OCP.IntTools.IntTools_Context) -> OCP.TopAbs.TopAbs_State: 
        """
        Computes the 3-D state of the shape theShape toward solid theSolid. theTol - value of precision of computation theContext- cahed geometrical tools Returns 3-D state.
        """
    @staticmethod
    @overload
    def ComputeState_s(thePoint : OCP.gp.gp_Pnt,theSolid : OCP.TopoDS.TopoDS_Solid,theTol : float,theContext : OCP.IntTools.IntTools_Context) -> OCP.TopAbs.TopAbs_State: 
        """
        Computes the 3-D state of the point thePoint toward solid theSolid. theTol - value of precision of computation theContext- cahed geometrical tools Returns 3-D state.

        Computes the 3-D state of the vertex theVertex toward solid theSolid. theTol - value of precision of computation theContext- cahed geometrical tools Returns 3-D state.

        Computes the 3-D state of the edge theEdge toward solid theSolid. theTol - value of precision of computation theContext- cahed geometrical tools Returns 3-D state.

        Computes the 3-D state of the face theFace toward solid theSolid. theTol - value of precision of computation theBounds - set of edges of <theSolid> to avoid theContext- cahed geometrical tools Returns 3-D state.
        """
    @staticmethod
    @overload
    def ComputeState_s(theFace : OCP.TopoDS.TopoDS_Face,theSolid : OCP.TopoDS.TopoDS_Solid,theTol : float,theBounds : OCP.TopTools.TopTools_IndexedMapOfShape,theContext : OCP.IntTools.IntTools_Context) -> OCP.TopAbs.TopAbs_State: ...
    @staticmethod
    @overload
    def ComputeState_s(theEdge : OCP.TopoDS.TopoDS_Edge,theSolid : OCP.TopoDS.TopoDS_Solid,theTol : float,theContext : OCP.IntTools.IntTools_Context) -> OCP.TopAbs.TopAbs_State: ...
    @staticmethod
    @overload
    def ComputeState_s(theVertex : OCP.TopoDS.TopoDS_Vertex,theSolid : OCP.TopoDS.TopoDS_Solid,theTol : float,theContext : OCP.IntTools.IntTools_Context) -> OCP.TopAbs.TopAbs_State: ...
    @staticmethod
    def ComputeTolerance_s(theFace : OCP.TopoDS.TopoDS_Face,theEdge : OCP.TopoDS.TopoDS_Edge,theMaxDist : float,theMaxPar : float) -> bool: 
        """
        Computes the necessary value of the tolerance for the edge
        """
    @staticmethod
    @overload
    def ComputeVV_s(theV1 : OCP.TopoDS.TopoDS_Vertex,theV2 : OCP.TopoDS.TopoDS_Vertex,theFuzz : float=1e-07) -> int: 
        """
        Intersects the vertex <theV1> with the point <theP> with tolerance <theTolP>. Returns the error status: - 0 - no error, meaning that the vertex intersects the point; - 1 - the distance between vertex and point is grater than the sum of tolerances.

        Intersects the given vertices with given fuzzy value. Returns the error status: - 0 - no error, meaning that the vertices interferes with given tolerance; - 1 - the distance between vertices is grater than the sum of their tolerances.
        """
    @staticmethod
    @overload
    def ComputeVV_s(theV : OCP.TopoDS.TopoDS_Vertex,theP : OCP.gp.gp_Pnt,theTolP : float) -> int: ...
    @staticmethod
    def CopyEdge_s(theEdge : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Makes a copy of <theEdge> with vertices.
        """
    @staticmethod
    def CorrectCurveOnSurface_s(theS : OCP.TopoDS.TopoDS_Shape,theMapToAvoid : OCP.TopTools.TopTools_IndexedMapOfShape,theTolMax : float=0.0001,theRunParallel : bool=False) -> None: 
        """
        Provides valid values of tolerances for the shape <theS> in terms of BRepCheck_InvalidCurveOnSurface.
        """
    @staticmethod
    def CorrectPointOnCurve_s(theS : OCP.TopoDS.TopoDS_Shape,theMapToAvoid : OCP.TopTools.TopTools_IndexedMapOfShape,theTolMax : float=0.0001,theRunParallel : bool=False) -> None: 
        """
        Provides valid values of tolerances for the shape <theS> in terms of BRepCheck_InvalidPointOnCurve.
        """
    @staticmethod
    @overload
    def CorrectRange_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aSR : OCP.IntTools.IntTools_Range,aNewSR : OCP.IntTools.IntTools_Range) -> None: 
        """
        Correct shrunk range <aSR> taking into account 3D-curve resolution and corresponding tolerance values of <aE1>, <aE2>

        Correct shrunk range <aSR> taking into account 3D-curve resolution and corresponding tolerance values of <aE>, <aF>
        """
    @staticmethod
    @overload
    def CorrectRange_s(aE1 : OCP.TopoDS.TopoDS_Edge,aE2 : OCP.TopoDS.TopoDS_Edge,aSR : OCP.IntTools.IntTools_Range,aNewSR : OCP.IntTools.IntTools_Range) -> None: ...
    @staticmethod
    def CorrectShapeTolerances_s(theS : OCP.TopoDS.TopoDS_Shape,theMapToAvoid : OCP.TopTools.TopTools_IndexedMapOfShape,theRunParallel : bool=False) -> None: 
        """
        Corrects tolerance values of the sub-shapes of the shape <theS> if needed.
        """
    @staticmethod
    def CorrectTolerances_s(theS : OCP.TopoDS.TopoDS_Shape,theMapToAvoid : OCP.TopTools.TopTools_IndexedMapOfShape,theTolMax : float=0.0001,theRunParallel : bool=False) -> None: 
        """
        Provides valid values of tolerances for the shape <theS> <theTolMax> is max value of the tolerance that can be accepted for correction. If real value of the tolerance will be greater than <aTolMax>, the correction does not perform.
        """
    @staticmethod
    def Dimension_s(theS : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Retutns dimension of the shape <theS>.
        """
    @staticmethod
    def GetEdgeOff_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face,theEdgeOff : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Returns True if the face theFace contains the edge theEdge but with opposite orientation. If the method returns True theEdgeOff is the edge founded
        """
    @staticmethod
    def GetEdgeOnFace_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face,theEdgeOnF : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        For the face theFace gets the edge theEdgeOnF that is the same as theEdge Returns True if such edge exists Returns False if there is no such edge
        """
    @staticmethod
    def GetFaceOff_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face,theLCEF : BOPTools_ListOfCoupleOfShape,theFaceOff : OCP.TopoDS.TopoDS_Face,theContext : OCP.IntTools.IntTools_Context) -> bool: 
        """
        For the face theFace and its edge theEdge finds the face suitable to produce shell. theLCEF - set of faces to search. All faces from theLCEF must share edge theEdge
        """
    @staticmethod
    def IsBlockInOnFace_s(aShR : OCP.IntTools.IntTools_Range,aF : OCP.TopoDS.TopoDS_Face,aE : OCP.TopoDS.TopoDS_Edge,aContext : OCP.IntTools.IntTools_Context) -> bool: 
        """
        Returns TRUE if PaveBlock <aPB> lays on the face <aF>, i.e the <PB> is IN or ON in 2D of <aF>
        """
    @staticmethod
    def IsHole_s(theW : OCP.TopoDS.TopoDS_Shape,theF : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the wire is a hole for the face.
        """
    @staticmethod
    @overload
    def IsInternalFace_s(theFace : OCP.TopoDS.TopoDS_Face,theEdge : OCP.TopoDS.TopoDS_Edge,theFace1 : OCP.TopoDS.TopoDS_Face,theFace2 : OCP.TopoDS.TopoDS_Face,theContext : OCP.IntTools.IntTools_Context) -> int: 
        """
        Returns True if the face theFace is inside of the couple of faces theFace1, theFace2. The faces theFace, theFace1, theFace2 must share the edge theEdge Return values: * 0 state is not IN * 1 state is IN * 2 state can not be found by the method of angles

        Returns True if the face theFace is inside of the appropriate couple of faces (from the set theLF) . The faces of the set theLF and theFace must share the edge theEdge * 0 state is not IN * 1 state is IN * 2 state can not be found by the method of angles

        Returns True if the face theFace is inside the solid theSolid. theMEF - Map Edge/Faces for theSolid theTol - value of precision of computation theContext- cahed geometrical tools
        """
    @staticmethod
    @overload
    def IsInternalFace_s(theFace : OCP.TopoDS.TopoDS_Face,theEdge : OCP.TopoDS.TopoDS_Edge,theLF : OCP.TopTools.TopTools_ListOfShape,theContext : OCP.IntTools.IntTools_Context) -> int: ...
    @staticmethod
    @overload
    def IsInternalFace_s(theFace : OCP.TopoDS.TopoDS_Face,theSolid : OCP.TopoDS.TopoDS_Solid,theMEF : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape,theTol : float,theContext : OCP.IntTools.IntTools_Context) -> bool: ...
    @staticmethod
    def IsInvertedSolid_s(theSolid : OCP.TopoDS.TopoDS_Solid) -> bool: 
        """
        Returns true if the solid <theSolid> is inverted
        """
    @staticmethod
    def IsMicroEdge_s(theEdge : OCP.TopoDS.TopoDS_Edge,theContext : OCP.IntTools.IntTools_Context,theCheckSplittable : bool=True) -> bool: 
        """
        Checks if it is possible to compute shrunk range for the edge <aE> Flag <theCheckSplittable> defines whether to take into account the possibility to split the edge or not.
        """
    @staticmethod
    def IsOpenShell_s(theShell : OCP.TopoDS.TopoDS_Shell) -> bool: 
        """
        Returns true if the shell <theShell> is open
        """
    @staticmethod
    def IsSplitToReverseWithWarn_s(theSplit : OCP.TopoDS.TopoDS_Shape,theShape : OCP.TopoDS.TopoDS_Shape,theContext : OCP.IntTools.IntTools_Context,theReport : OCP.Message.Message_Report=None) -> bool: 
        """
        Add-on for the *IsSplitToReverse()* to check for its errors and in case of any add the *BOPAlgo_AlertUnableToOrientTheShape* warning to the report.
        """
    @staticmethod
    @overload
    def IsSplitToReverse_s(theSplit : OCP.TopoDS.TopoDS_Edge,theShape : OCP.TopoDS.TopoDS_Edge,theContext : OCP.IntTools.IntTools_Context,theError : int=None) -> bool: 
        """
        Checks if the direction of the split shape is opposite to the direction of the original shape. The method is an overload for (Edge,Edge) and (Face,Face) corresponding methods and checks only these types of shapes. For faces the method checks if normal directions are opposite. For edges the method checks if tangent vectors are opposite.

        Checks if the normal direction of the split face is opposite to the normal direction of the original face. The normal directions for both faces are taken in the same point - point inside the split face is projected onto the original face. Returns TRUE if the normals do not coincide, meaning the necessity to revert the orientation of the split face to match the direction of the original face.

        Checks if the tangent vector of the split edge is opposite to the tangent vector of the original edge. The tangent vectors for both edges are computed in the same point - point inside the split edge is projected onto the original edge. Returns TRUE if the tangent vectors do not coincide, meaning the necessity to revert the orientation of the split edge to match the direction of the original edge.
        """
    @staticmethod
    @overload
    def IsSplitToReverse_s(theSplit : OCP.TopoDS.TopoDS_Face,theShape : OCP.TopoDS.TopoDS_Face,theContext : OCP.IntTools.IntTools_Context,theError : int=None) -> bool: ...
    @staticmethod
    @overload
    def IsSplitToReverse_s(theSplit : OCP.TopoDS.TopoDS_Shape,theShape : OCP.TopoDS.TopoDS_Shape,theContext : OCP.IntTools.IntTools_Context,theError : int=None) -> bool: ...
    @staticmethod
    def MakeConnexityBlock_s(theLS : OCP.TopTools.TopTools_ListOfShape,theMapAvoid : OCP.TopTools.TopTools_IndexedMapOfShape,theLSCB : OCP.TopTools.TopTools_ListOfShape,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        For the list of faces theLS build block theLSCB in terms of connexity by edges theMapAvoid - set of edges to avoid for the treatment
        """
    @staticmethod
    @overload
    def MakeConnexityBlocks_s(theS : OCP.TopoDS.TopoDS_Shape,theConnectionType : OCP.TopAbs.TopAbs_ShapeEnum,theElementType : OCP.TopAbs.TopAbs_ShapeEnum,theLCB : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        For the compound <theS> builds the blocks (compounds) of elements of type <theElementType> connected through the shapes of the type <theConnectionType>. The blocks are stored into the list <theLCB>.

        For the compound <theS> builds the blocks (compounds) of elements of type <theElementType> connected through the shapes of the type <theConnectionType>. The blocks are stored into the list of lists <theLCB>. Returns also the connection map <theConnectionMap>, filled during operation.

        Makes connexity blocks of elements of the given type with the given type of the connecting elements. The blocks are checked on regularity (multi-connectivity) and stored to the list of blocks <theLCB>.
        """
    @staticmethod
    @overload
    def MakeConnexityBlocks_s(theS : OCP.TopoDS.TopoDS_Shape,theConnectionType : OCP.TopAbs.TopAbs_ShapeEnum,theElementType : OCP.TopAbs.TopAbs_ShapeEnum,theLCB : OCP.TopTools.TopTools_ListOfListOfShape,theConnectionMap : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...
    @staticmethod
    @overload
    def MakeConnexityBlocks_s(theLS : OCP.TopTools.TopTools_ListOfShape,theConnectionType : OCP.TopAbs.TopAbs_ShapeEnum,theElementType : OCP.TopAbs.TopAbs_ShapeEnum,theLCB : BOPTools_ListOfConnexityBlock) -> None: ...
    @staticmethod
    def MakeContainer_s(theType : OCP.TopAbs.TopAbs_ShapeEnum,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Makes empty container of requested type
        """
    @staticmethod
    def MakeEdge_s(theCurve : OCP.IntTools.IntTools_Curve,theV1 : OCP.TopoDS.TopoDS_Vertex,theT1 : float,theV2 : OCP.TopoDS.TopoDS_Vertex,theT2 : float,theTolR3D : float,theE : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Makes the edge based on the given curve with given bounding vertices.
        """
    @staticmethod
    @overload
    def MakeNewVertex_s(aV1 : OCP.TopoDS.TopoDS_Vertex,aV2 : OCP.TopoDS.TopoDS_Vertex,aNewVertex : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Make a vertex using 3D-point <aP1> and 3D-tolerance value <aTol>

        Make a vertex using couple of vertices <aV1, aV2>

        Make a vertex in place of intersection between two edges <aE1, aE2> with parameters <aP1, aP2>

        Make a vertex in place of intersection between the edge <aE1> with parameter <aP1> and the face <aF2>
        """
    @staticmethod
    @overload
    def MakeNewVertex_s(aE1 : OCP.TopoDS.TopoDS_Edge,aP1 : float,aF2 : OCP.TopoDS.TopoDS_Face,aNewVertex : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @staticmethod
    @overload
    def MakeNewVertex_s(aE1 : OCP.TopoDS.TopoDS_Edge,aP1 : float,aE2 : OCP.TopoDS.TopoDS_Edge,aP2 : float,aNewVertex : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @staticmethod
    @overload
    def MakeNewVertex_s(aP1 : OCP.gp.gp_Pnt,aTol : float,aNewVertex : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @staticmethod
    def MakePCurve_s(theE : OCP.TopoDS.TopoDS_Edge,theF1 : OCP.TopoDS.TopoDS_Face,theF2 : OCP.TopoDS.TopoDS_Face,theCurve : OCP.IntTools.IntTools_Curve,thePC1 : bool,thePC2 : bool,theContext : OCP.IntTools.IntTools_Context=None) -> None: 
        """
        Makes 2d curve of the edge <theE> on the faces <theF1> and <theF2>. <theContext> - storage for caching the geometrical tools
        """
    @staticmethod
    def MakeSectEdge_s(aIC : OCP.IntTools.IntTools_Curve,aV1 : OCP.TopoDS.TopoDS_Vertex,aP1 : float,aV2 : OCP.TopoDS.TopoDS_Vertex,aP2 : float,aNewEdge : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Make the edge from 3D-Curve <aIC> and two vertices <aV1,aV2> at parameters <aP1,aP2>
        """
    @staticmethod
    def MakeSplitEdge_s(aE1 : OCP.TopoDS.TopoDS_Edge,aV1 : OCP.TopoDS.TopoDS_Vertex,aP1 : float,aV2 : OCP.TopoDS.TopoDS_Vertex,aP2 : float,aNewEdge : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Make the edge from base edge <aE1> and two vertices <aV1,aV2> at parameters <aP1,aP2>
        """
    @staticmethod
    def MakeVertex_s(theLV : OCP.TopTools.TopTools_ListOfShape,theV : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Makes the vertex in the middle of given vertices with the tolerance covering all tolerance spheres of vertices.
        """
    @staticmethod
    def OrientEdgesOnWire_s(theWire : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Correctly orients edges on the wire
        """
    @staticmethod
    def OrientFacesOnShell_s(theShell : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Correctly orients faces on the shell
        """
    @staticmethod
    def PointOnEdge_s(aEdge : OCP.TopoDS.TopoDS_Edge,aPrm : float,aP : OCP.gp.gp_Pnt) -> None: 
        """
        Compute a 3D-point on the edge <aEdge> at parameter <aPrm>
        """
    @staticmethod
    def Sense_s(theF1 : OCP.TopoDS.TopoDS_Face,theF2 : OCP.TopoDS.TopoDS_Face,theContext : OCP.IntTools.IntTools_Context) -> int: 
        """
        Checks if the normals direction of the given faces computed near the shared edge coincide. Returns the status of operation: * 0 - in case of error (shared edge not found or directions are not collinear) * 1 - normal directions coincide; * -1 - normal directions are opposite.
        """
    @staticmethod
    @overload
    def UpdateVertex_s(aE : OCP.TopoDS.TopoDS_Edge,aT : float,aV : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Update the tolerance value for vertex <aV> taking into account the fact that <aV> lays on the curve <aIC>

        Update the tolerance value for vertex <aV> taking into account the fact that <aV> lays on the edge <aE>

        Update the tolerance value for vertex <aVN> taking into account the fact that <aVN> should cover tolerance zone of <aVF>
        """
    @staticmethod
    @overload
    def UpdateVertex_s(aVF : OCP.TopoDS.TopoDS_Vertex,aVN : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @staticmethod
    @overload
    def UpdateVertex_s(aIC : OCP.IntTools.IntTools_Curve,aT : float,aV : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    def __init__(self) -> None: ...
    pass
class BOPTools_AlgoTools2D():
    """
    The class contains handy static functions dealing with the topology This is the copy of the BOPTools_AlgoTools2D.cdl
    """
    @staticmethod
    @overload
    def AdjustPCurveOnFace_s(theF : OCP.TopoDS.TopoDS_Face,theC3D : OCP.Geom.Geom_Curve,theC2D : OCP.Geom2d.Geom2d_Curve,theC2DA : OCP.Geom2d.Geom2d_Curve,theContext : OCP.IntTools.IntTools_Context=None) -> None: 
        """
        Adjust P-Curve <theC2D> (3D-curve <theC3D>) on surface of the face <theF>. <theContext> - storage for caching the geometrical tools

        Adjust P-Curve <aC2D> (3D-curve <C3D>) on surface <aF> . [aT1, aT2] - range to adjust <theContext> - storage for caching the geometrical tools
        """
    @staticmethod
    @overload
    def AdjustPCurveOnFace_s(theF : OCP.TopoDS.TopoDS_Face,theFirst : float,theLast : float,theC2D : OCP.Geom2d.Geom2d_Curve,theC2DA : OCP.Geom2d.Geom2d_Curve,theContext : OCP.IntTools.IntTools_Context=None) -> None: ...
    @staticmethod
    def AdjustPCurveOnSurf_s(aF : OCP.BRepAdaptor.BRepAdaptor_Surface,aT1 : float,aT2 : float,aC2D : OCP.Geom2d.Geom2d_Curve,aC2DA : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Adjust P-Curve <aC2D> (3D-curve <C3D>) on surface <aF> . [aT1, aT2] - range to adjust
        """
    @staticmethod
    def AttachExistingPCurve_s(aEold : OCP.TopoDS.TopoDS_Edge,aEnew : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aCtx : OCP.IntTools.IntTools_Context) -> int: 
        """
        Attach P-Curve from the edge <aEold> on surface <aF> to the edge <aEnew> Returns 0 in case of success
        """
    @staticmethod
    def BuildPCurveForEdgeOnFace_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,theContext : OCP.IntTools.IntTools_Context=None) -> None: 
        """
        Compute P-Curve for the edge <aE> on the face <aF>. Raises exception Standard_ConstructionError if projection algorithm fails. <theContext> - storage for caching the geometrical tools
        """
    @staticmethod
    @overload
    def CurveOnSurface_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aC : OCP.Geom2d.Geom2d_Curve,theContext : OCP.IntTools.IntTools_Context=None) -> Tuple[float]: 
        """
        Get P-Curve <aC> for the edge <aE> on surface <aF> . If the P-Curve does not exist, build it using Make2D(). [aToler] - reached tolerance Raises exception Standard_ConstructionError if algorithm Make2D() fails. <theContext> - storage for caching the geometrical tools

        Get P-Curve <aC> for the edge <aE> on surface <aF> . If the P-Curve does not exist, build it using Make2D(). [aFirst, aLast] - range of the P-Curve [aToler] - reached tolerance Raises exception Standard_ConstructionError if algorithm Make2D() fails. <theContext> - storage for caching the geometrical tools
        """
    @staticmethod
    @overload
    def CurveOnSurface_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aC : OCP.Geom2d.Geom2d_Curve,theContext : OCP.IntTools.IntTools_Context=None) -> Tuple[float, float, float]: ...
    @staticmethod
    def EdgeTangent_s(anE : OCP.TopoDS.TopoDS_Edge,aT : float,Tau : OCP.gp.gp_Vec) -> bool: 
        """
        Compute tangent for the edge <aE> [in 3D] at parameter <aT>
        """
    @staticmethod
    @overload
    def HasCurveOnSurface_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aC : OCP.Geom2d.Geom2d_Curve,aFirst : float,aLast : float,aToler : float) -> bool: 
        """
        Returns TRUE if the edge <aE> has P-Curve <aC> on surface <aF> . [aFirst, aLast] - range of the P-Curve [aToler] - reached tolerance If the P-Curve does not exist, aC.IsNull()=TRUE.

        Returns TRUE if the edge <aE> has P-Curve <aC> on surface <aF> . If the P-Curve does not exist, aC.IsNull()=TRUE.
        """
    @staticmethod
    @overload
    def HasCurveOnSurface_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face) -> bool: ...
    @staticmethod
    @overload
    def IntermediatePoint_s(anE : OCP.TopoDS.TopoDS_Edge) -> float: 
        """
        Compute intermediate value in between [aFirst, aLast] .

        Compute intermediate value of parameter for the edge <anE>.
        """
    @staticmethod
    @overload
    def IntermediatePoint_s(aFirst : float,aLast : float) -> float: ...
    @staticmethod
    def IsEdgeIsoline_s(theE : OCP.TopoDS.TopoDS_Edge,theF : OCP.TopoDS.TopoDS_Face) -> Tuple[bool, bool]: 
        """
        Checks if CurveOnSurface of theE on theF matches with isoline of theF surface. Sets corresponding values for isTheUIso and isTheVIso variables. ATTENTION!!! This method is based on comparation between direction of surface (which theF is based on) iso-lines and the direction of the edge p-curve (on theF) in middle-point of the p-curve. This method should be used carefully (e.g. BRep_Tool::IsClosed(...) together) in order to avoid false classification some p-curves as isoline (e.g. circle on a plane).
        """
    @staticmethod
    def Make2D_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aC : OCP.Geom2d.Geom2d_Curve,theContext : OCP.IntTools.IntTools_Context=None) -> Tuple[float, float, float]: 
        """
        Make P-Curve <aC> for the edge <aE> on surface <aF> . [aFirst, aLast] - range of the P-Curve [aToler] - reached tolerance Raises exception Standard_ConstructionError if algorithm fails. <theContext> - storage for caching the geometrical tools
        """
    @staticmethod
    @overload
    def MakePCurveOnFace_s(aF : OCP.TopoDS.TopoDS_Face,C3D : OCP.Geom.Geom_Curve,aC : OCP.Geom2d.Geom2d_Curve,theContext : OCP.IntTools.IntTools_Context=None) -> Tuple[float]: 
        """
        Make P-Curve <aC> for the 3D-curve <C3D> on surface <aF> . [aToler] - reached tolerance Raises exception Standard_ConstructionError if projection algorithm fails. <theContext> - storage for caching the geometrical tools

        Make P-Curve <aC> for the 3D-curve <C3D> on surface <aF> . [aT1, aT2] - range to build [aToler] - reached tolerance Raises exception Standard_ConstructionError if projection algorithm fails. <theContext> - storage for caching the geometrical tools
        """
    @staticmethod
    @overload
    def MakePCurveOnFace_s(aF : OCP.TopoDS.TopoDS_Face,C3D : OCP.Geom.Geom_Curve,aT1 : float,aT2 : float,aC : OCP.Geom2d.Geom2d_Curve,theContext : OCP.IntTools.IntTools_Context=None) -> Tuple[float]: ...
    @staticmethod
    def PointOnSurface_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aT : float,theContext : OCP.IntTools.IntTools_Context=None) -> Tuple[float, float]: 
        """
        Compute surface parameters <U,V> of the face <aF> for the point from the edge <aE> at parameter <aT>. If <aE> has't pcurve on surface, algorithm tries to get it by projection and can raise exception Standard_ConstructionError if projection algorithm fails. <theContext> - storage for caching the geometrical tools
        """
    def __init__(self) -> None: ...
    pass
class BOPTools_AlgoTools3D():
    """
    The class contains handy static functions dealing with the topology This is the copy of BOPTools_AlgoTools3D.cdl file
    """
    @staticmethod
    def DoSplitSEAMOnFace_s(aSp : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Make the edge <aSp> seam edge for the face <aF>
        """
    @staticmethod
    @overload
    def GetApproxNormalToFaceOnEdge_s(theE : OCP.TopoDS.TopoDS_Edge,theF : OCP.TopoDS.TopoDS_Face,aT : float,aP : OCP.gp.gp_Pnt,aDNF : OCP.gp.gp_Dir,aDt2D : float) -> bool: 
        """
        Computes normal to the face <aF> for the 3D-point that belongs to the edge <aE> at parameter <aT>. Output: aPx - the 3D-point where the normal computed aD - the normal; Warning: The normal is computed not exactly in the point on the edge, but in point that is near to the edge towards to the face material (so, we'll have approx. normal); The point is computed using PointNearEdge function, with the shifting value BOPTools_AlgoTools3D::MinStepIn2d(), from the edge, but if this value is too big, the point will be computed using Hatcher (PointInFace function). Returns TRUE in case of success.

        Computes normal to the face <aF> for the 3D-point that belongs to the edge <aE> at parameter <aT>. Output: aPx - the 3D-point where the normal computed aD - the normal; Warning: The normal is computed not exactly in the point on the edge, but in point that is near to the edge towards to the face material (so, we'll have approx. normal); The point is computed using PointNearEdge function with the shifting value <aDt2D> from the edge; No checks on this value will be done. Returns TRUE in case of success.

        Computes normal to the face <aF> for the 3D-point that belongs to the edge <aE> at parameter <aT>. Output: aPx - the 3D-point where the normal computed aD - the normal; Warning: The normal is computed not exactly in the point on the edge, but in point that is near to the edge towards to the face material (so, we'll have approx. normal); The point is computed using PointNearEdge function with the shifting value <aDt2D> from the edge, but if this value is too big the point will be computed using Hatcher (PointInFace function). Returns TRUE in case of success.
        """
    @staticmethod
    @overload
    def GetApproxNormalToFaceOnEdge_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aT : float,aPx : OCP.gp.gp_Pnt,aD : OCP.gp.gp_Dir,theContext : OCP.IntTools.IntTools_Context) -> bool: ...
    @staticmethod
    @overload
    def GetApproxNormalToFaceOnEdge_s(theE : OCP.TopoDS.TopoDS_Edge,theF : OCP.TopoDS.TopoDS_Face,aT : float,aDt2D : float,aP : OCP.gp.gp_Pnt,aDNF : OCP.gp.gp_Dir,theContext : OCP.IntTools.IntTools_Context) -> bool: ...
    @staticmethod
    @overload
    def GetNormalToFaceOnEdge_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aD : OCP.gp.gp_Dir,theContext : OCP.IntTools.IntTools_Context=None) -> None: 
        """
        Computes normal to the face <aF> for the point on the edge <aE> at parameter <aT>. <theContext> - storage for caching the geometrical tools

        Computes normal to the face <aF> for the point on the edge <aE> at arbitrary intermediate parameter. <theContext> - storage for caching the geometrical tools
        """
    @staticmethod
    @overload
    def GetNormalToFaceOnEdge_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aT : float,aD : OCP.gp.gp_Dir,theContext : OCP.IntTools.IntTools_Context=None) -> None: ...
    @staticmethod
    def GetNormalToSurface_s(aS : OCP.Geom.Geom_Surface,U : float,V : float,aD : OCP.gp.gp_Dir) -> bool: 
        """
        Compute normal <aD> to surface <aS> in point (U,V) Returns TRUE if directions aD1U, aD1V coincide
        """
    @staticmethod
    def IsEmptyShape_s(aS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns TRUE if the shape <aS> does not contain geometry information (e.g. empty compound)
        """
    @staticmethod
    def MinStepIn2d_s() -> float: 
        """
        Returns simple step value that is used in 2D-computations = 1.e-5
        """
    @staticmethod
    def OrientEdgeOnFace_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aER : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Get the edge <aER> from the face <aF> that is the same as the edge <aE>
        """
    @staticmethod
    @overload
    def PointInFace_s(theF : OCP.TopoDS.TopoDS_Face,theL : OCP.Geom2d.Geom2d_Curve,theP : OCP.gp.gp_Pnt,theP2D : OCP.gp.gp_Pnt2d,theContext : OCP.IntTools.IntTools_Context,theDt2D : float=0.0) -> int: 
        """
        Computes arbitrary point <theP> inside the face <theF>. <theP2D> - 2D representation of <theP> on the surface of <theF> Returns 0 in case of success.

        Computes a point <theP> inside the face <theF> using starting point taken by the parameter <theT> from the 2d curve of the edge <theE> on the face <theF> in the direction perpendicular to the tangent vector of the 2d curve of the edge. The point will be distanced on <theDt2D> from the 2d curve. <theP2D> - 2D representation of <theP> on the surface of <theF> Returns 0 in case of success.

        Computes a point <theP> inside the face <theF> using the line <theL> so that 2D point <theP2D>, 2D representation of <theP> on the surface of <theF>, lies on that line. Returns 0 in case of success.
        """
    @staticmethod
    @overload
    def PointInFace_s(theF : OCP.TopoDS.TopoDS_Face,theP : OCP.gp.gp_Pnt,theP2D : OCP.gp.gp_Pnt2d,theContext : OCP.IntTools.IntTools_Context) -> int: ...
    @staticmethod
    @overload
    def PointInFace_s(theF : OCP.TopoDS.TopoDS_Face,theE : OCP.TopoDS.TopoDS_Edge,theT : float,theDt2D : float,theP : OCP.gp.gp_Pnt,theP2D : OCP.gp.gp_Pnt2d,theContext : OCP.IntTools.IntTools_Context) -> int: ...
    @staticmethod
    @overload
    def PointNearEdge_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aT : float,aP2D : OCP.gp.gp_Pnt2d,aPx : OCP.gp.gp_Pnt,theContext : OCP.IntTools.IntTools_Context) -> int: 
        """
        Compute the point <aPx>, (<aP2D>) that is near to the edge <aE> at parameter <aT> towards to the material of the face <aF>. The value of shifting in 2D is <aDt2D> If the value of shifting is too big the point will be computed using Hatcher (PointInFace function). Returns error status: 0 - in case of success; 1 - <aE> does not have 2d curve on the face <aF>; 2 - the computed point is out of the face.

        Compute the point <aPx>, (<aP2D>) that is near to the edge <aE> at parameter <aT> towards to the material of the face <aF>. The value of shifting in 2D is <aDt2D>. No checks on this value will be done. Returns error status: 0 - in case of success; 1 - <aE> does not have 2d curve on the face <aF>.

        Computes the point <aPx>, (<aP2D>) that is near to the edge <aE> at parameter <aT> towards to the material of the face <aF>. The value of shifting in 2D is dt2D=BOPTools_AlgoTools3D::MinStepIn2d() If the value of shifting is too big the point will be computed using Hatcher (PointInFace function). Returns error status: 0 - in case of success; 1 - <aE> does not have 2d curve on the face <aF>; 2 - the computed point is out of the face.

        Compute the point <aPx>, (<aP2D>) that is near to the edge <aE> at arbitrary parameter towards to the material of the face <aF>. The value of shifting in 2D is dt2D=BOPTools_AlgoTools3D::MinStepIn2d(). If the value of shifting is too big the point will be computed using Hatcher (PointInFace function). Returns error status: 0 - in case of success; 1 - <aE> does not have 2d curve on the face <aF>; 2 - the computed point is out of the face.
        """
    @staticmethod
    @overload
    def PointNearEdge_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aT : float,aDt2D : float,aP2D : OCP.gp.gp_Pnt2d,aPx : OCP.gp.gp_Pnt) -> int: ...
    @staticmethod
    @overload
    def PointNearEdge_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aP2D : OCP.gp.gp_Pnt2d,aPx : OCP.gp.gp_Pnt,theContext : OCP.IntTools.IntTools_Context) -> int: ...
    @staticmethod
    @overload
    def PointNearEdge_s(aE : OCP.TopoDS.TopoDS_Edge,aF : OCP.TopoDS.TopoDS_Face,aT : float,aDt2D : float,aP2D : OCP.gp.gp_Pnt2d,aPx : OCP.gp.gp_Pnt,theContext : OCP.IntTools.IntTools_Context) -> int: ...
    @staticmethod
    def SenseFlag_s(aNF1 : OCP.gp.gp_Dir,aNF2 : OCP.gp.gp_Dir) -> int: 
        """
        Returns 1 if scalar product aNF1* aNF2>0. Returns 0 if directions aNF1 aNF2 coincide Returns -1 if scalar product aNF1* aNF2<0.
        """
    def __init__(self) -> None: ...
    pass
class BOPTools_Box2dTreeSelector():
    """
    Template Selector for elements selection from BVH tree.
    """
    def Accept(self,theIndex : int,theIsInside : bool) -> bool: 
        """
        Accepts the element with the index <theIndex> in BVH tree
        """
    def AcceptMetric(self,theIsInside : bool) -> bool: 
        """
        Checks if the metric of the node may be accepted
        """
    def Clear(self) -> None: 
        """
        Clears the indices
        """
    def Indices(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Returns the list of accepted indices
        """
    def RejectElement(self,theIndex : int) -> bool: 
        """
        Checks if the element should be rejected
        """
    def RejectNode(self,theCMin : OCP.Graphic3d.Graphic3d_Vec2d,theCMax : OCP.Graphic3d.Graphic3d_Vec2d,theIsInside : bool) -> bool: 
        """
        Checks if the box should be rejected
        """
    def SetBox(self,theBox : Any) -> None: 
        """
        Sets the box
        """
    def __init__(self) -> None: ...
    pass
class BOPTools_BoxTree():
    """
    Redefines BoxSet to use the Linear builder by default
    """
    def __init__(self,theBuilder : OCP.Select3D.Select3D_BVHBuilder3d=None) -> None: ...
    pass
class BOPTools_BoxTreeSelector():
    """
    Template Selector for elements selection from BVH tree.
    """
    def Accept(self,theIndex : int,theIsInside : bool) -> bool: 
        """
        Accepts the element with the index <theIndex> in BVH tree
        """
    def AcceptMetric(self,theIsInside : bool) -> bool: 
        """
        Checks if the metric of the node may be accepted
        """
    def Clear(self) -> None: 
        """
        Clears the indices
        """
    def Indices(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Returns the list of accepted indices
        """
    def RejectElement(self,theIndex : int) -> bool: 
        """
        Checks if the element should be rejected
        """
    def RejectNode(self,theCMin : OCP.SelectMgr.SelectMgr_Vec3,theCMax : OCP.SelectMgr.SelectMgr_Vec3,theIsInside : bool) -> bool: 
        """
        Checks if the box should be rejected
        """
    def SetBox(self,theBox : OCP.Graphic3d.Graphic3d_BndBox3d) -> None: 
        """
        Sets the box
        """
    def __init__(self) -> None: ...
    pass
class BOPTools_ConnexityBlock():
    """
    None
    """
    def ChangeLoops(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def ChangeShapes(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def IsRegular(self) -> bool: 
        """
        None
        """
    def Loops(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def SetRegular(self,theFlag : bool) -> None: 
        """
        None
        """
    def Shapes(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPTools_CoupleOfShape():
    """
    None
    """
    def SetShape1(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def SetShape2(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BOPTools_IndexedDataMapOfSetShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : BOPTools_Set,theItem : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPTools_IndexedDataMapOfSetShape) -> BOPTools_IndexedDataMapOfSetShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : BOPTools_Set) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : BOPTools_Set) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Contains(self,theKey1 : BOPTools_Set) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : BOPTools_IndexedDataMapOfSetShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : BOPTools_Set) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : BOPTools_Set,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def FindIndex(self,theKey1 : BOPTools_Set) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> BOPTools_Set: 
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
    def RemoveKey(self,theKey1 : BOPTools_Set) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : BOPTools_Set) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : BOPTools_Set,theItem : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theOther : BOPTools_IndexedDataMapOfSetShape) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BOPTools_ListOfConnexityBlock(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : BOPTools_ListOfConnexityBlock) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : BOPTools_ConnexityBlock) -> BOPTools_ConnexityBlock: ...
    @overload
    def Append(self,theItem : BOPTools_ConnexityBlock,theIter : Any) -> None: ...
    def Assign(self,theOther : BOPTools_ListOfConnexityBlock) -> BOPTools_ListOfConnexityBlock: 
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
    def First(self) -> BOPTools_ConnexityBlock: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : BOPTools_ConnexityBlock,theIter : Any) -> BOPTools_ConnexityBlock: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : BOPTools_ListOfConnexityBlock,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : BOPTools_ConnexityBlock,theIter : Any) -> BOPTools_ConnexityBlock: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : BOPTools_ListOfConnexityBlock,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BOPTools_ConnexityBlock: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : BOPTools_ListOfConnexityBlock) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : BOPTools_ConnexityBlock) -> BOPTools_ConnexityBlock: ...
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
    def __init__(self,theOther : BOPTools_ListOfConnexityBlock) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BOPTools_ListOfCoupleOfShape(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BOPTools_CoupleOfShape) -> BOPTools_CoupleOfShape: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : BOPTools_CoupleOfShape,theIter : Any) -> None: ...
    @overload
    def Append(self,theOther : BOPTools_ListOfCoupleOfShape) -> None: ...
    def Assign(self,theOther : BOPTools_ListOfCoupleOfShape) -> BOPTools_ListOfCoupleOfShape: 
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
    def First(self) -> BOPTools_CoupleOfShape: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : BOPTools_CoupleOfShape,theIter : Any) -> BOPTools_CoupleOfShape: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : BOPTools_ListOfCoupleOfShape,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : BOPTools_ListOfCoupleOfShape,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : BOPTools_CoupleOfShape,theIter : Any) -> BOPTools_CoupleOfShape: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BOPTools_CoupleOfShape: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : BOPTools_CoupleOfShape) -> BOPTools_CoupleOfShape: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : BOPTools_ListOfCoupleOfShape) -> None: ...
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
    def __init__(self,theOther : BOPTools_ListOfCoupleOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BOPTools_MapOfSet(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : BOPTools_Set) -> bool: 
        """
        Add
        """
    def Added(self,K : BOPTools_Set) -> BOPTools_Set: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPTools_MapOfSet) -> BOPTools_MapOfSet: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,K : BOPTools_Set) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : BOPTools_MapOfSet) -> bool: ...
    def Differ(self,theOther : BOPTools_MapOfSet) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : BOPTools_MapOfSet,theRight : BOPTools_MapOfSet) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : BOPTools_MapOfSet) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : BOPTools_MapOfSet) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : BOPTools_MapOfSet) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : BOPTools_MapOfSet,theRight : BOPTools_MapOfSet) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : BOPTools_MapOfSet) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : BOPTools_Set) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : BOPTools_MapOfSet) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : BOPTools_MapOfSet,theRight : BOPTools_MapOfSet) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : BOPTools_MapOfSet,theRight : BOPTools_MapOfSet) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : BOPTools_MapOfSet) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BOPTools_MapOfSet) -> None: ...
    pass
class BOPTools_Parallel():
    """
    Implementation of Functors/Starters
    """
    def __init__(self) -> None: ...
    pass
class BOPTools_Set():
    """
    None
    """
    def Add(self,theS : OCP.TopoDS.TopoDS_Shape,theType : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        None
        """
    def Assign(self,Other : BOPTools_Set) -> BOPTools_Set: 
        """
        None
        """
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Computes a hash code for this set, in the range [1, theUpperBound]
        """
    def IsEqual(self,aOther : BOPTools_Set) -> bool: 
        """
        None
        """
    def NbShapes(self) -> int: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPTools_SetMapHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(theSet : BOPTools_Set,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given set, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(aSet1 : BOPTools_Set,aSet2 : BOPTools_Set) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
