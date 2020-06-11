import OCP.ChFi2d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64

_Shape = Tuple[int, ...]
import OCP.TopoDS
import OCP.TopTools
import OCP.gp

__all__ = [
    "ChFi2d",
    "ChFi2d_AnaFilletAlgo",
    "ChFi2d_Builder",
    "ChFi2d_ChamferAPI",
    "ChFi2d_ConstructionError",
    "ChFi2d_FilletAPI",
    "ChFi2d_FilletAlgo",
    "FilletPoint",
    "ChFi2d_BothEdgesDegenerated",
    "ChFi2d_ComputationError",
    "ChFi2d_ConnexionError",
    "ChFi2d_FirstEdgeDegenerated",
    "ChFi2d_InitialisationError",
    "ChFi2d_IsDone",
    "ChFi2d_LastEdgeDegenerated",
    "ChFi2d_NoFace",
    "ChFi2d_NotAuthorized",
    "ChFi2d_NotPlanar",
    "ChFi2d_ParametersError",
    "ChFi2d_Ready",
    "ChFi2d_TangencyError",
]

class ChFi2d:
    """
    This package contains the algorithms used to build fillets or chamfers on planar wire.
    """

    def __init__(self) -> None: ...
    pass

class ChFi2d_AnaFilletAlgo:
    """
    An analytical algorithm for calculation of the fillets. It is implemented for segments and arcs of circle only.
    """

    @overload
    def Init(self, theWire: OCP.TopoDS.TopoDS_Wire, thePlane: OCP.gp.gp_Pln) -> None:
        """
        Initializes the class by a wire consisting of two edges.

        Initializes the class by two edges.
        """
    @overload
    def Init(
        self,
        theEdge1: OCP.TopoDS.TopoDS_Edge,
        theEdge2: OCP.TopoDS.TopoDS_Edge,
        thePlane: OCP.gp.gp_Pln,
    ) -> None: ...
    def Perform(self, radius: float) -> bool:
        """
        Calculates a fillet.
        """
    def Result(
        self, e1: OCP.TopoDS.TopoDS_Edge, e2: OCP.TopoDS.TopoDS_Edge
    ) -> OCP.TopoDS.TopoDS_Edge:
        """
        Retrieves a result (fillet and shrinked neighbours).
        """
    @overload
    def __init__(
        self, theWire: OCP.TopoDS.TopoDS_Wire, thePlane: OCP.gp.gp_Pln
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        theEdge1: OCP.TopoDS.TopoDS_Edge,
        theEdge2: OCP.TopoDS.TopoDS_Edge,
        thePlane: OCP.gp.gp_Pln,
    ) -> None: ...
    pass

class ChFi2d_Builder:
    """
    This class contains the algorithm used to build fillet on planar wire.
    """

    @overload
    def AddChamfer(
        self,
        E1: OCP.TopoDS.TopoDS_Edge,
        E2: OCP.TopoDS.TopoDS_Edge,
        D1: float,
        D2: float,
    ) -> OCP.TopoDS.TopoDS_Edge:
        """
        Add a chamfer on the wire between the two edges connected <E1> and <E2>. <AddChamfer> returns the chamfer edge. This edge has sense only if the status <status> is <IsDone>.

        Add a chamfer on the wire between the two edges connected to the vertex <V>. The chamfer will make an angle <Ang> with the edge <E>, and one of its extremities will be on <E> at distance <D>. The returned edge has sense only if the status <status> is <IsDone>. Warning: The value of <Ang> must be expressed in Radian.
        """
    @overload
    def AddChamfer(
        self,
        E: OCP.TopoDS.TopoDS_Edge,
        V: OCP.TopoDS.TopoDS_Vertex,
        D: float,
        Ang: float,
    ) -> OCP.TopoDS.TopoDS_Edge: ...
    def AddFillet(
        self, V: OCP.TopoDS.TopoDS_Vertex, Radius: float
    ) -> OCP.TopoDS.TopoDS_Edge:
        """
        Add a fillet of radius <Radius> on the wire between the two edges connected to the vertex <V>. <AddFillet> returns the fillet edge. The returned edge has sense only if the status <status> is <IsDone>
        """
    def BasisEdge(self, E: OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Edge:
        """
        Returns the parent edge of <E> Warning: If <E>is a basis edge, the returned edge would be equal to <E>
        """
    def ChamferEdges(self) -> OCP.TopTools.TopTools_SequenceOfShape:
        """
        returns the list of new edges

        returns the list of new edges
        """
    def DescendantEdge(self, E: OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Edge:
        """
        returns the modified edge if <E> has descendant or <E> in the other case.

        returns the modified edge if <E> has descendant or <E> in the other case.
        """
    def FilletEdges(self) -> OCP.TopTools.TopTools_SequenceOfShape:
        """
        returns the list of new edges

        returns the list of new edges
        """
    def HasDescendant(self, E: OCP.TopoDS.TopoDS_Edge) -> bool:
        """
        None

        None
        """
    @overload
    def Init(self, F: OCP.TopoDS.TopoDS_Face) -> None:
        """
        None

        None
        """
    @overload
    def Init(
        self, RefFace: OCP.TopoDS.TopoDS_Face, ModFace: OCP.TopoDS.TopoDS_Face
    ) -> None: ...
    def IsModified(self, E: OCP.TopoDS.TopoDS_Edge) -> bool:
        """
        None

        None
        """
    @overload
    def ModifyChamfer(
        self,
        Chamfer: OCP.TopoDS.TopoDS_Edge,
        E: OCP.TopoDS.TopoDS_Edge,
        D: float,
        Ang: float,
    ) -> OCP.TopoDS.TopoDS_Edge:
        """
        modify the chamfer <Chamfer> and returns the new chamfer edge. This edge as sense only if the status <status> is <IsDone>.

        modify the chamfer <Chamfer> and returns the new chamfer edge. This edge as sense only if the status <status> is <IsDone>. Warning: The value of <Ang> must be expressed in Radian.
        """
    @overload
    def ModifyChamfer(
        self,
        Chamfer: OCP.TopoDS.TopoDS_Edge,
        E1: OCP.TopoDS.TopoDS_Edge,
        E2: OCP.TopoDS.TopoDS_Edge,
        D1: float,
        D2: float,
    ) -> OCP.TopoDS.TopoDS_Edge: ...
    def ModifyFillet(
        self, Fillet: OCP.TopoDS.TopoDS_Edge, Radius: float
    ) -> OCP.TopoDS.TopoDS_Edge:
        """
        modify the fillet radius and return the new fillet edge. this edge has sense only if the status <status> is <IsDone>.
        """
    def NbChamfer(self) -> int:
        """
        None

        None
        """
    def NbFillet(self) -> int:
        """
        None

        None
        """
    def RemoveChamfer(
        self, Chamfer: OCP.TopoDS.TopoDS_Edge
    ) -> OCP.TopoDS.TopoDS_Vertex:
        """
        removes the chamfer <Chamfer> and returns the vertex connecting the two adjacent edges to this chamfer.
        """
    def RemoveFillet(self, Fillet: OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Vertex:
        """
        removes the fillet <Fillet> and returns the vertex connecting the two adjacent edges to this fillet.
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Face:
        """
        returns the modified face

        returns the modified face
        """
    def Status(self) -> ChFi2d_ConstructionError:
        """
        None

        None
        """
    @overload
    def __init__(self, F: OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass

class ChFi2d_ChamferAPI:
    """
    A class making a chamfer between two linear edges.
    """

    @overload
    def Init(
        self, theEdge1: OCP.TopoDS.TopoDS_Edge, theEdge2: OCP.TopoDS.TopoDS_Edge
    ) -> None:
        """
        Initializes the class by a wire consisting of two libear edges.

        Initializes the class by two linear edges.
        """
    @overload
    def Init(self, theWire: OCP.TopoDS.TopoDS_Wire) -> None: ...
    def Perform(self) -> bool:
        """
        Constructs a chamfer edge. Returns true if the edge is constructed.
        """
    def Result(
        self,
        theEdge1: OCP.TopoDS.TopoDS_Edge,
        theEdge2: OCP.TopoDS.TopoDS_Edge,
        theLength1: float,
        theLength2: float,
    ) -> OCP.TopoDS.TopoDS_Edge:
        """
        None
        """
    @overload
    def __init__(self, theWire: OCP.TopoDS.TopoDS_Wire) -> None: ...
    @overload
    def __init__(
        self, theEdge1: OCP.TopoDS.TopoDS_Edge, theEdge2: OCP.TopoDS.TopoDS_Edge
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass

class ChFi2d_ConstructionError:
    """
    error that can occur during the fillet construction on planar wire//! the face is not planar//! the face is null//! the two faces used for the initialisation are uncompatible.//! the parameters as distances or angle for chamfer are less or equal to zero.//! the initialization has been succesfull.//! the algorithm could not find a solution.//! the vertex given to locate the fillet or the chamfer is not connected to 2 edges.//! the two edges connected to the vertex are tangent.//! the first edge is degenerated.//! the last edge is degenerated.//! the two edges are degenerated.//! One or the two edges connected to the vertex is a fillet or a chamfer One or the two edges connected to the vertex is not a line or a circle

    Members:

      ChFi2d_NotPlanar

      ChFi2d_NoFace

      ChFi2d_InitialisationError

      ChFi2d_ParametersError

      ChFi2d_Ready

      ChFi2d_IsDone

      ChFi2d_ComputationError

      ChFi2d_ConnexionError

      ChFi2d_TangencyError

      ChFi2d_FirstEdgeDegenerated

      ChFi2d_LastEdgeDegenerated

      ChFi2d_BothEdgesDegenerated

      ChFi2d_NotAuthorized
    """

    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    ChFi2d_BothEdgesDegenerated: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_BothEdgesDegenerated
    ChFi2d_ComputationError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_ComputationError
    ChFi2d_ConnexionError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_ConnexionError
    ChFi2d_FirstEdgeDegenerated: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_FirstEdgeDegenerated
    ChFi2d_InitialisationError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_InitialisationError
    ChFi2d_IsDone: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_IsDone
    ChFi2d_LastEdgeDegenerated: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_LastEdgeDegenerated
    ChFi2d_NoFace: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_NoFace
    ChFi2d_NotAuthorized: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_NotAuthorized
    ChFi2d_NotPlanar: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_NotPlanar
    ChFi2d_ParametersError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_ParametersError
    ChFi2d_Ready: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_Ready
    ChFi2d_TangencyError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_TangencyError
    __entries: dict  # value = {'ChFi2d_NotPlanar': (ChFi2d_ConstructionError.ChFi2d_NotPlanar, None), 'ChFi2d_NoFace': (ChFi2d_ConstructionError.ChFi2d_NoFace, None), 'ChFi2d_InitialisationError': (ChFi2d_ConstructionError.ChFi2d_InitialisationError, None), 'ChFi2d_ParametersError': (ChFi2d_ConstructionError.ChFi2d_ParametersError, None), 'ChFi2d_Ready': (ChFi2d_ConstructionError.ChFi2d_Ready, None), 'ChFi2d_IsDone': (ChFi2d_ConstructionError.ChFi2d_IsDone, None), 'ChFi2d_ComputationError': (ChFi2d_ConstructionError.ChFi2d_ComputationError, None), 'ChFi2d_ConnexionError': (ChFi2d_ConstructionError.ChFi2d_ConnexionError, None), 'ChFi2d_TangencyError': (ChFi2d_ConstructionError.ChFi2d_TangencyError, None), 'ChFi2d_FirstEdgeDegenerated': (ChFi2d_ConstructionError.ChFi2d_FirstEdgeDegenerated, None), 'ChFi2d_LastEdgeDegenerated': (ChFi2d_ConstructionError.ChFi2d_LastEdgeDegenerated, None), 'ChFi2d_BothEdgesDegenerated': (ChFi2d_ConstructionError.ChFi2d_BothEdgesDegenerated, None), 'ChFi2d_NotAuthorized': (ChFi2d_ConstructionError.ChFi2d_NotAuthorized, None)}
    __members__: dict  # value = {'ChFi2d_NotPlanar': ChFi2d_ConstructionError.ChFi2d_NotPlanar, 'ChFi2d_NoFace': ChFi2d_ConstructionError.ChFi2d_NoFace, 'ChFi2d_InitialisationError': ChFi2d_ConstructionError.ChFi2d_InitialisationError, 'ChFi2d_ParametersError': ChFi2d_ConstructionError.ChFi2d_ParametersError, 'ChFi2d_Ready': ChFi2d_ConstructionError.ChFi2d_Ready, 'ChFi2d_IsDone': ChFi2d_ConstructionError.ChFi2d_IsDone, 'ChFi2d_ComputationError': ChFi2d_ConstructionError.ChFi2d_ComputationError, 'ChFi2d_ConnexionError': ChFi2d_ConstructionError.ChFi2d_ConnexionError, 'ChFi2d_TangencyError': ChFi2d_ConstructionError.ChFi2d_TangencyError, 'ChFi2d_FirstEdgeDegenerated': ChFi2d_ConstructionError.ChFi2d_FirstEdgeDegenerated, 'ChFi2d_LastEdgeDegenerated': ChFi2d_ConstructionError.ChFi2d_LastEdgeDegenerated, 'ChFi2d_BothEdgesDegenerated': ChFi2d_ConstructionError.ChFi2d_BothEdgesDegenerated, 'ChFi2d_NotAuthorized': ChFi2d_ConstructionError.ChFi2d_NotAuthorized}
    pass

class ChFi2d_FilletAPI:
    """
    An interface class for 2D fillets. Open CASCADE provides two algorithms for 2D fillets: ChFi2d_Builder - it constructs a fillet or chamfer for linear and circular edges of a face. ChFi2d_FilletAPI - it encapsulates two algorithms: ChFi2d_AnaFilletAlgo - analytical constructor of the fillet. It works only for linear and circular edges, having a common point. ChFi2d_FilletAlgo - iteration recursive method constructing the fillet edge for any type of edges including ellipses and b-splines. The edges may even have no common point.
    """

    @overload
    def Init(
        self,
        theEdge1: OCP.TopoDS.TopoDS_Edge,
        theEdge2: OCP.TopoDS.TopoDS_Edge,
        thePlane: OCP.gp.gp_Pln,
    ) -> None:
        """
        Initializes a fillet algorithm: accepts a wire consisting of two edges in a plane.

        Initializes a fillet algorithm: accepts two edges in a plane.
        """
    @overload
    def Init(
        self, theWire: OCP.TopoDS.TopoDS_Wire, thePlane: OCP.gp.gp_Pln
    ) -> None: ...
    def NbResults(self, thePoint: OCP.gp.gp_Pnt) -> int:
        """
        Returns number of possible solutions. <thePoint> chooses a particular fillet in case of several fillets may be constructed (for example, a circle intersecting a segment in 2 points). Put the intersecting (or common) point of the edges.
        """
    def Perform(self, theRadius: float) -> bool:
        """
        Constructs a fillet edge. Returns true if at least one result was found.
        """
    def Result(
        self,
        thePoint: OCP.gp.gp_Pnt,
        theEdge1: OCP.TopoDS.TopoDS_Edge,
        theEdge2: OCP.TopoDS.TopoDS_Edge,
        iSolution: int = -1,
    ) -> OCP.TopoDS.TopoDS_Edge:
        """
        Returns result (fillet edge, modified edge1, modified edge2), nearest to the given point <thePoint> if iSolution == -1 <thePoint> chooses a particular fillet in case of several fillets may be constructed (for example, a circle intersecting a segment in 2 points). Put the intersecting (or common) point of the edges.
        """
    @overload
    def __init__(
        self,
        theEdge1: OCP.TopoDS.TopoDS_Edge,
        theEdge2: OCP.TopoDS.TopoDS_Edge,
        thePlane: OCP.gp.gp_Pln,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, theWire: OCP.TopoDS.TopoDS_Wire, thePlane: OCP.gp.gp_Pln
    ) -> None: ...
    pass

class ChFi2d_FilletAlgo:
    """
    Algorithm that creates fillet edge: arc tangent to two edges in the start and in the end vertices. Initial edges must be located on the plane and must be connected by the end or start points (shared vertices are not obligatory). Created fillet arc is created with the given radius, that is useful in sketcher applications.
    """

    @overload
    def Init(self, theWire: OCP.TopoDS.TopoDS_Wire, thePlane: OCP.gp.gp_Pln) -> None:
        """
        Initializes a fillet algorithm: accepts a wire consisting of two edges in a plane.

        Initializes a fillet algorithm: accepts two edges in a plane.
        """
    @overload
    def Init(
        self,
        theEdge1: OCP.TopoDS.TopoDS_Edge,
        theEdge2: OCP.TopoDS.TopoDS_Edge,
        thePlane: OCP.gp.gp_Pln,
    ) -> None: ...
    def NbResults(self, thePoint: OCP.gp.gp_Pnt) -> int:
        """
        Returns number of possible solutions. <thePoint> chooses a particular fillet in case of several fillets may be constructed (for example, a circle intersecting a segment in 2 points). Put the intersecting (or common) point of the edges.
        """
    def Perform(self, theRadius: float) -> bool:
        """
        Constructs a fillet edge. Returns true, if at least one result was found
        """
    def Result(
        self,
        thePoint: OCP.gp.gp_Pnt,
        theEdge1: OCP.TopoDS.TopoDS_Edge,
        theEdge2: OCP.TopoDS.TopoDS_Edge,
        iSolution: int = -1,
    ) -> OCP.TopoDS.TopoDS_Edge:
        """
        Returns result (fillet edge, modified edge1, modified edge2), neares to the given point <thePoint> if iSolution == -1. <thePoint> chooses a particular fillet in case of several fillets may be constructed (for example, a circle intersecting a segment in 2 points). Put the intersecting (or common) point of the edges.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, theWire: OCP.TopoDS.TopoDS_Wire, thePlane: OCP.gp.gp_Pln
    ) -> None: ...
    @overload
    def __init__(
        self,
        theEdge1: OCP.TopoDS.TopoDS_Edge,
        theEdge2: OCP.TopoDS.TopoDS_Edge,
        thePlane: OCP.gp.gp_Pln,
    ) -> None: ...
    pass

class FilletPoint:
    """
    Private class. Corresponds to the point on the first curve, computed fillet function and derivative on it.Private class. Corresponds to the point on the first curve, computed fillet function and derivative on it.
    """

    def Copy(self) -> FilletPoint:
        """
        Returns a pointer to created copy of the point warning: this is not the full copy! Copies only: myParam, myV, myD, myValid
        """
    def FilterPoints(self, arg1: FilletPoint) -> None:
        """
        Filters out the values and leaves the most optimal one.
        """
    def LowerValue(self) -> float:
        """
        For debug only
        """
    def __init__(self, theParam: float) -> None: ...
    def appendValue(self, theValue: float, theValid: bool) -> None:
        """
        Appends value of the function.
        """
    def calculateDiff(self, arg1: FilletPoint) -> bool:
        """
        Computes difference between this point and the given. Stores difference in myD.
        """
    def getCenter(self) -> OCP.gp.gp_Pnt2d:
        """
        Center of the fillet.
        """
    def getDiff(self, theIndex: int) -> float:
        """
        Returns derivatives of function in this point.
        """
    def getNBValues(self) -> int:
        """
        Returns number of found values of function in this point.
        """
    def getNear(self, theIndex: int) -> int:
        """
        Returns the index of the nearest value
        """
    def getParam(self) -> float:
        """
        Returns the point parameter on the first curve.
        """
    def getParam2(self) -> float:
        """
        Returns the parameter of the projected point on the second curve.
        """
    def getValue(self, theIndex: int) -> float:
        """
        Returns value of function in this point.
        """
    def hasSolution(self, theRadius: float) -> int:
        """
        Returns the index of the solution or zero if there is no solution
        """
    def isValid(self, theIndex: int) -> bool:
        """
        Returns true if function is valid (rediuses vectors of fillet do not intersect any curve).
        """
    def remove(self, theIndex: int) -> None:
        """
        Removes the found value by the given index.
        """
    def setCenter(self, thePoint: OCP.gp.gp_Pnt2d) -> None:
        """
        Center of the fillet.
        """
    def setParam(self, theParam: float) -> None:
        """
        Changes the point position by changing point parameter on the first curve.
        """
    def setParam2(self, theParam2: float) -> None:
        """
        Defines the parameter of the projected point on the second curve.
        """
    pass

ChFi2d_BothEdgesDegenerated: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_BothEdgesDegenerated
ChFi2d_ComputationError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_ComputationError
ChFi2d_ConnexionError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_ConnexionError
ChFi2d_FirstEdgeDegenerated: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_FirstEdgeDegenerated
ChFi2d_InitialisationError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_InitialisationError
ChFi2d_IsDone: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_IsDone
ChFi2d_LastEdgeDegenerated: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_LastEdgeDegenerated
ChFi2d_NoFace: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_NoFace
ChFi2d_NotAuthorized: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_NotAuthorized
ChFi2d_NotPlanar: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_NotPlanar
ChFi2d_ParametersError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_ParametersError
ChFi2d_Ready: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_Ready
ChFi2d_TangencyError: OCP.ChFi2d.ChFi2d_ConstructionError  # value = ChFi2d_ConstructionError.ChFi2d_TangencyError
