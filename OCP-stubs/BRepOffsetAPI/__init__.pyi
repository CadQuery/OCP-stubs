import OCP.BRepOffsetAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Approx
import OCP.NCollection
import OCP.BRepBuilderAPI
import OCP.Law
import OCP.Geom
import OCP.TopoDS
import OCP.GeomFill
import OCP.Draft
import OCP.TopTools
import OCP.TColStd
import OCP.BRepFill
import OCP.BRepPrimAPI
import OCP.gp
import OCP.GeomAbs
import OCP.BRepOffset
__all__  = [
"BRepOffsetAPI_DraftAngle",
"BRepOffsetAPI_FindContigousEdges",
"BRepOffsetAPI_MakeDraft",
"BRepOffsetAPI_MakeEvolved",
"BRepOffsetAPI_MakeFilling",
"BRepOffsetAPI_MakeOffset",
"BRepOffsetAPI_MakeOffsetShape",
"BRepOffsetAPI_MakePipe",
"BRepOffsetAPI_MakePipeShell",
"BRepOffsetAPI_MakeThickSolid",
"BRepOffsetAPI_MiddlePath",
"BRepOffsetAPI_NormalProjection",
"BRepOffsetAPI_SequenceOfSequenceOfReal",
"BRepOffsetAPI_SequenceOfSequenceOfShape",
"BRepOffsetAPI_ThruSections"
]
class BRepOffsetAPI_DraftAngle(OCP.BRepBuilderAPI.BRepBuilderAPI_ModifyShape, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Taper-adding transformations on a shape. The resulting shape is constructed by defining one face to be tapered after another one, as well as the geometric properties of their tapered transformation. Each tapered transformation is propagated along the series of faces which are tangential to one another and which contains the face to be tapered. This algorithm is useful in the construction of molds or dies. It facilitates the removal of the article being produced. A DraftAngle object provides a framework for: - initializing the construction algorithm with a given shape, - acquiring the data characterizing the faces to be tapered, - implementing the construction algorithm, and - consulting the results. Warning - This algorithm treats planar, cylindrical and conical faces. - Do not use shapes, which with a draft angle added to a face would modify the topology. This would, for example, involve creation of new vertices, edges or faces, or suppression of existing vertices, edges or faces. - Any face, which is continuous in tangency with the face to be tapered, will also be tapered. These connected faces must also respect the above criteria.
    """
    def Add(self,F : OCP.TopoDS.TopoDS_Face,Direction : OCP.gp.gp_Dir,Angle : float,NeutralPlane : OCP.gp.gp_Pln,Flag : bool=True) -> None: 
        """
        Adds the face F, the direction Direction, the angle Angle, the plane NeutralPlane, and the flag Flag to the framework created at construction time, and with this data, defines the taper-adding transformation. F is a face, which belongs to the initial shape of this algorithm or to the shape loaded by the function Init. Only planar, cylindrical or conical faces can be tapered: - If the face F is planar, it is tapered by inclining it through the angle Angle about the line of intersection between the plane NeutralPlane and F. Direction indicates the side of NeutralPlane from which matter is removed if Angle is positive or added if Angle is negative. - If F is cylindrical or conical, it is transformed in the same way on a single face, resulting in a conical face if F is cylindrical, and a conical or cylindrical face if it is already conical. The taper-adding transformation is propagated from the face F along the series of planar, cylindrical or conical faces containing F, which are tangential to one another. Use the function AddDone to check if this taper-adding transformation is successful. Warning Nothing is done if: - the face F does not belong to the initial shape of this algorithm, or - the face F is not planar, cylindrical or conical. Exceptions - Standard_NullObject if the initial shape is not defined, i.e. if this algorithm has not been initialized with the non-empty constructor or the Init function. - Standard_ConstructionError if the previous call to Add has failed. The function AddDone ought to have been used to check for this, and the function Remove to cancel the results of the unsuccessful taper-adding transformation and to retrieve the previous shape.
        """
    def AddDone(self) -> bool: 
        """
        Returns true if the previous taper-adding transformation performed by this algorithm in the last call to Add, was successful. If AddDone returns false: - the function ProblematicShape returns the face on which the error occurred, - the function Remove has to be used to cancel the results of the unsuccessful taper-adding transformation and to retrieve the previous shape. Exceptions Standard_NullObject if the initial shape has not been defined, i.e. if this algorithm has not been initialized with the non-empty constructor or the .Init function.
        """
    def Build(self) -> None: 
        """
        Builds the resulting shape (redefined from MakeShape).
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Clear(self) -> None: 
        """
        Cancels the results of all taper-adding transformations performed by this algorithm on the initial shape. These results will have been defined by successive calls to the function Add.
        """
    def ConnectedFaces(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns all the faces which have been added together with the face <F>.
        """
    def CorrectWires(self) -> None: 
        """
        None
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes, or reinitializes this taper-adding algorithm with the shape S. S will be referred to as the initial shape of this algorithm.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def ModifiedFaces(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns all the faces on which a modification has been given.
        """
    def ModifiedShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the modified shape corresponding to <S>. S can correspond to the entire initial shape or to its subshape. Raises exceptions Standard_NoSuchObject if S is not the initial shape or a subshape of the initial shape to which the transformation has been applied.
        """
    def ProblematicShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape on which an error occurred after an unsuccessful call to Add or when IsDone returns false. Exceptions Standard_NullObject if the initial shape has not been defined, i.e. if this algorithm has not been initialized with the non-empty constructor or the Init function.
        """
    def Remove(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Cancels the taper-adding transformation previously performed by this algorithm on the face F and the series of tangential faces which contain F, and retrieves the shape before the last taper-adding transformation. Warning You will have to use this function if the previous call to Add fails. Use the function AddDone to check it. Exceptions - Standard_NullObject if the initial shape has not been defined, i.e. if this algorithm has not been initialized with the non-empty constructor or the Init function. - Standard_NoSuchObject if F has not been added or has already been removed.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Status(self) -> OCP.Draft.Draft_ErrorStatus: 
        """
        Returns an error status when an error has occured (Face, Edge or Vertex recomputaion problem). Otherwise returns Draft_NoError. The method may be called if AddDone returns Standard_False, or when IsDone returns Standard_False.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class BRepOffsetAPI_FindContigousEdges():
    """
    Provides methods to identify contigous boundaries for continuity control (C0, C1, ...)
    """
    def Add(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the shape shape to the list of shapes to be checked by this algorithm. Once all the shapes to be checked have been added, use the function Perform to find the contiguous edges and the function ContigousEdge to return these edges.
        """
    def ContigousEdge(self,index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the contiguous edge of index index found by the function Perform on the shapes added to this algorithm. Exceptions Standard_OutOfRange if: - index is less than 1, or - index is greater than the number of contiguous edges found by the function Perform on the shapes added to this algorithm.
        """
    def ContigousEdgeCouple(self,index : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of edges coincident with the contiguous edge of index index found by the function Perform. There are as many edges in the list as there are faces adjacent to this contiguous edge. Exceptions Standard_OutOfRange if: - index is less than 1, or - index is greater than the number of contiguous edges found by the function Perform on the shapes added to this algorithm.
        """
    def DegeneratedShape(self,index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives a degenerated shape
        """
    def Dump(self) -> None: 
        """
        Dump properties of resulting shape.
        """
    def Init(self,tolerance : float,option : bool) -> None: 
        """
        Initializes this algorithm for identifying contiguous edges on shapes using the tolerance of contiguity tolerance. This tolerance value is used to determine whether two edges or sections of edges are coincident. Use the function Add to define the shapes to be checked. Sets <option> to false.
        """
    def IsDegenerated(self,shape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Indicates if a input shape is degenerated
        """
    def IsModified(self,shape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the copy of the initial shape shape was modified by the function Perform (i.e. if one or more of its edges was broken down into contiguous and non-contiguous sections). Warning Returns false if shape is not one of the initial shapes added to this algorithm.
        """
    def Modified(self,shape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives a modifieded shape Raises NoSuchObject if shape has not been modified
        """
    def NbContigousEdges(self) -> int: 
        """
        Returns the number of contiguous edges found by the function Perform on the shapes added to this algorithm.
        """
    def NbDegeneratedShapes(self) -> int: 
        """
        Gives the number of degenerated shapes
        """
    def Perform(self) -> None: 
        """
        Finds coincident parts of edges of two or more shapes added to this algorithm and breaks down these edges into contiguous and non-contiguous sections on copies of the initial shapes. The function ContigousEdge returns contiguous edges. The function Modified can be used to return modified copies of the initial shapes where one or more edges were broken down into contiguous and non-contiguous sections. Warning This function must be used once all the shapes to be checked have been added. It is not possible to add further shapes subsequently and then to repeat the call to Perform.
        """
    def SectionToBoundary(self,section : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge on the initial shape, of which the modified copy contains the edge section. section is coincident with a contiguous edge found by the function Perform. Use the function ContigousEdgeCouple to obtain a valid section. This information is useful for verification purposes, since it provides a means of determining the surface to which the contiguous edge belongs. Exceptions Standard_NoSuchObject if section is not coincident with a contiguous edge. Use the function ContigousEdgeCouple to obtain a valid section.
        """
    def __init__(self,tolerance : float=1e-06,option : bool=True) -> None: ...
    pass
class BRepOffsetAPI_MakeDraft(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Build a draft surface along a wire
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    @overload
    def Perform(self,Surface : OCP.Geom.Geom_Surface,KeepInsideSurface : bool=True) -> None: 
        """
        Performs the draft using the length LengthMax as the maximum length for the corner edge between two draft faces.

        Performs the draft up to the surface Surface. If KeepInsideSurface is true, the part of Surface inside the draft is kept in the result.

        Performs the draft up to the shape StopShape. If KeepOutSide is true, the part of StopShape which is outside the Draft is kept in the result.
        """
    @overload
    def Perform(self,StopShape : OCP.TopoDS.TopoDS_Shape,KeepOutSide : bool=True) -> None: ...
    @overload
    def Perform(self,LengthMax : float) -> None: ...
    def SetDraft(self,IsInternal : bool=False) -> None: 
        """
        Sets the direction of the draft for this object. If IsInternal is true, the draft is internal to the argument Shape used in the constructor.
        """
    def SetOptions(self,Style : OCP.BRepBuilderAPI.BRepBuilderAPI_TransitionMode=BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RightCorner,AngleMin : float=0.01,AngleMax : float=3.0) -> None: 
        """
        Sets the options of this draft tool. If a transition has to be performed, it can be defined by the mode Style as RightCorner or RoundCorner, RightCorner being a corner defined by a sharp angle, and RoundCorner being a rounded corner. AngleMin is an angular tolerance used to detect whether a transition has to be performed or not. AngleMax sets the maximum value within which a RightCorner transition can be performed. AngleMin and AngleMax are expressed in radians.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the shell resulting from performance of the draft along the wire.
        """
    def __init__(self,Shape : OCP.TopoDS.TopoDS_Shape,Dir : OCP.gp.gp_Dir,Angle : float) -> None: ...
    pass
class BRepOffsetAPI_MakeEvolved(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build evolved shapes. An evolved shape is built from a planar spine (face or wire) and a profile (wire). The evolved shape is the unlooped sweep (pipe) of the profile along the spine. Self-intersections are removed. A MakeEvolved object provides a framework for: - defining the construction of an evolved shape, - implementing the construction algorithm, and - consulting the result. Computes an Evolved by 1 - sweeping a profile along a spine. 2 - removing the self-intersections.
    """
    def Bottom(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Return the face Bottom if <Solid> is True in the constructor.
        """
    def Build(self) -> None: 
        """
        Builds the resulting shape (redefined from MakeShape).
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Evolved(self) -> OCP.BRepFill.BRepFill_Evolved: 
        """
        None
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def GeneratedShapes(self,SpineShape : OCP.TopoDS.TopoDS_Shape,ProfShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes created from a subshape <SpineShape> of the spine and a subshape <ProfShape> on the profile.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Top(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Return the face Top if <Solid> is True in the constructor.
        """
    @overload
    def __init__(self,theSpine : OCP.TopoDS.TopoDS_Shape,theProfile : OCP.TopoDS.TopoDS_Wire,theJoinType : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,theIsAxeProf : bool=True,theIsSolid : bool=False,theIsProfOnSpine : bool=False,theTol : float=1e-07,theIsVolume : bool=False,theRunInParallel : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepOffsetAPI_MakeFilling(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    N-Side Filling This algorithm avoids to build a face from: * a set of edges defining the bounds of the face and some constraints the surface of the face has to satisfy * a set of edges and points defining some constraints the support surface has to satisfy * an initial surface to deform for satisfying the constraints * a set of parameters to control the constraints.
    """
    @overload
    def Add(self,Support : OCP.TopoDS.TopoDS_Face,Order : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Adds a new constraint which also defines an edge of the wire of the face Order: Order of the constraint: GeomAbs_C0 : the surface has to pass by 3D representation of the edge GeomAbs_G1 : the surface has to pass by 3D representation of the edge and to respect tangency with the first face of the edge GeomAbs_G2 : the surface has to pass by 3D representation of the edge and to respect tangency and curvature with the first face of the edge. Raises ConstructionError if the edge has no representation on a face and Order is GeomAbs_G1 or GeomAbs_G2.

        Adds a new constraint which also defines an edge of the wire of the face Order: Order of the constraint: GeomAbs_C0 : the surface has to pass by 3D representation of the edge GeomAbs_G1 : the surface has to pass by 3D representation of the edge and to respect tangency with the given face GeomAbs_G2 : the surface has to pass by 3D representation of the edge and to respect tangency and curvature with the given face. Raises ConstructionError if the edge has no 2d representation on the given face

        Adds a free constraint on a face. The corresponding edge has to be automatically recomputed. It is always a bound.

        Adds a punctual constraint.

        Adds a punctual constraint.
        """
    @overload
    def Add(self,Constr : OCP.TopoDS.TopoDS_Edge,Order : OCP.GeomAbs.GeomAbs_Shape,IsBound : bool=True) -> int: ...
    @overload
    def Add(self,Constr : OCP.TopoDS.TopoDS_Edge,Support : OCP.TopoDS.TopoDS_Face,Order : OCP.GeomAbs.GeomAbs_Shape,IsBound : bool=True) -> int: ...
    @overload
    def Add(self,Point : OCP.gp.gp_Pnt) -> int: ...
    @overload
    def Add(self,U : float,V : float,Support : OCP.TopoDS.TopoDS_Face,Order : OCP.GeomAbs.GeomAbs_Shape) -> int: ...
    def Build(self) -> None: 
        """
        Builds the resulting faces
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    @overload
    def G0Error(self,Index : int) -> float: 
        """
        Returns the maximum distance between the result and the constraints. This is set at construction time.

        Returns the maximum distance attained between the result and the constraint Index. This is set at construction time.
        """
    @overload
    def G0Error(self) -> float: ...
    @overload
    def G1Error(self) -> float: 
        """
        Returns the maximum angle between the result and the constraints. This is set at construction time.

        Returns the maximum angle between the result and the constraints. This is set at construction time.
        """
    @overload
    def G1Error(self,Index : int) -> float: ...
    @overload
    def G2Error(self) -> float: 
        """
        Returns the maximum angle between the result and the constraints. This is set at construction time.

        Returns the greatest difference in curvature found between the result and the constraint Index.
        """
    @overload
    def G2Error(self,Index : int) -> float: ...
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        Tests whether computation of the filling plate has been completed.
        """
    def LoadInitSurface(self,Surf : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Loads the initial surface Surf to begin the construction of the surface. This optional function is useful if the surface resulting from construction for the algorithm is likely to be complex. The support surface of the face under construction is computed by a deformation of Surf which satisfies the given constraints. The set of bounding edges defines the wire of the face. If no initial surface is given, the algorithm computes it automatically. If the set of edges is not connected (Free constraint), missing edges are automatically computed. Important: the initial surface must have orthogonal local coordinates, i.e. partial derivatives dS/du and dS/dv must be orthogonal at each point of surface. If this condition breaks, distortions of resulting surface are possible.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def SetApproxParam(self,MaxDeg : int=8,MaxSegments : int=9) -> None: 
        """
        Sets the parameters used to approximate the filling surface. These include: - MaxDeg - the highest degree which the polynomial defining the filling surface can have - MaxSegments - the greatest number of segments which the filling surface can have.
        """
    def SetConstrParam(self,Tol2d : float=1e-05,Tol3d : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1) -> None: 
        """
        Sets the values of Tolerances used to control the constraint. Tol2d: Tol3d: it is the maximum distance allowed between the support surface and the constraints TolAng: it is the maximum angle allowed between the normal of the surface and the constraints TolCurv: it is the maximum difference of curvature allowed between the surface and the constraint
        """
    def SetResolParam(self,Degree : int=3,NbPtsOnCur : int=15,NbIter : int=2,Anisotropie : bool=False) -> None: 
        """
        Sets the parameters used for resolution. The default values of these parameters have been chosen for a good ratio quality/performance. Degree: it is the order of energy criterion to minimize for computing the deformation of the surface. The default value is 3 The recommanded value is i+2 where i is the maximum order of the constraints. NbPtsOnCur: it is the average number of points for discretisation of the edges. NbIter: it is the maximum number of iterations of the process. For each iteration the number of discretisation points is increased. Anisotropie:
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def __init__(self,Degree : int=3,NbPtsOnCur : int=15,NbIter : int=2,Anisotropie : bool=False,Tol2d : float=1e-05,Tol3d : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1,MaxDeg : int=8,MaxSegments : int=9) -> None: ...
    pass
class BRepOffsetAPI_MakeOffset(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes algorithms for offsetting wires from a set of wires contained in a planar face. A MakeOffset object provides a framework for: - defining the construction of an offset, - implementing the construction algorithm, and - consulting the result.
    """
    def AddWire(self,Spine : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Initializes the algorithm to construct parallels to the wire Spine.
        """
    def Build(self) -> None: 
        """
        Builds the resulting shape (redefined from MakeShape).
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created shapes from the shape <S>.
        """
    @overload
    def Init(self,Spine : OCP.TopoDS.TopoDS_Face,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,IsOpenResult : bool=False) -> None: 
        """
        Initializes the algorithm to construct parallels to the spine Spine. Join defines the type of parallel generated by the salient vertices of the spine. The default type is GeomAbs_Arc where the vertices generate sections of a circle. If join type is GeomAbs_Intersection, the edges that intersect in a salient vertex generate the edges prolonged until intersection.

        Initialize the evaluation of Offseting.
        """
    @overload
    def Init(self,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,IsOpenResult : bool=False) -> None: ...
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Perform(self,Offset : float,Alt : float=0.0) -> None: 
        """
        Computes a parallel to the spine at distance Offset and at an altitude Alt from the plane of the spine in relation to the normal to the spine. Exceptions: StdFail_NotDone if the offset is not built.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Face,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,IsOpenResult : bool=False) -> None: ...
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Wire,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,IsOpenResult : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepOffsetAPI_MakeOffsetShape(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build a shell out of a shape. The result is an unlooped shape parallel to the source shape. A MakeOffsetShape object provides a framework for: - defining the construction of a shell - implementing the construction algorithm - consulting the result.
    """
    def Build(self) -> None: 
        """
        Does nothing.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def GetJoinType(self) -> OCP.GeomAbs.GeomAbs_JoinType: 
        """
        Returns offset join type.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape has been removed from the result.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def MakeOffset(self) -> OCP.BRepOffset.BRepOffset_MakeOffset: 
        """
        Returns instance of the unrelying intersection / arc algorithm.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape <S>.
        """
    def PerformByJoin(self,S : OCP.TopoDS.TopoDS_Shape,Offset : float,Tol : float,Mode : OCP.BRepOffset.BRepOffset_Mode=BRepOffset_Mode.BRepOffset_Skin,Intersection : bool=False,SelfInter : bool=False,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,RemoveIntEdges : bool=False) -> None: 
        """
        Constructs a shape parallel to the shape S, where - S may be a face, a shell, a solid or a compound of these shape kinds; - Offset is the offset value. The offset shape is constructed: - outside S, if Offset is positive, - inside S, if Offset is negative; - Tol defines the coincidence tolerance criterion for generated shapes; - Mode defines the construction type of parallels applied to the free edges of shape S; currently, only one construction type is implemented, namely the one where the free edges do not generate parallels; this corresponds to the default value BRepOffset_Skin; - Intersection specifies how the algorithm must work in order to limit the parallels to two adjacent shapes: - if Intersection is false (default value), the intersection is calculated with the parallels to the two adjacent shapes, - if Intersection is true, the intersection is calculated by taking all generated parallels into account; this computation method is more general as it avoids some self-intersections generated in the offset shape from features of small dimensions on shape S, however this method has not been completely implemented and therefore is not recommended for use; - SelfInter tells the algorithm whether a computation to eliminate self-intersections must be applied to the resulting shape; however, as this functionality is not yet implemented, it is recommended to use the default value (false); - Join defines how to fill the holes that may appear between parallels to the two adjacent faces. It may take values GeomAbs_Arc or GeomAbs_Intersection: - if Join is equal to GeomAbs_Arc, then pipes are generated between two free edges of two adjacent parallels, and spheres are generated on "images" of vertices; it is the default value, - if Join is equal to GeomAbs_Intersection, then the parallels to the two adjacent faces are enlarged and intersected, so that there are no free edges on parallels to faces. RemoveIntEdges flag defines whether to remove the INTERNAL edges from the result or not. Warnings 1. All the faces of the shape S should be based on the surfaces with continuity at least C1. 2. The offset value should be sufficiently small to avoid self-intersections in resulting shape. Otherwise these self-intersections may appear inside an offset face if its initial surface is not plane or sphere or cylinder, also some non-adjacent offset faces may intersect each other. Also, some offset surfaces may "turn inside out". 3. The algorithm may fail if the shape S contains vertices where more than 3 edges converge. 4. Since 3d-offset algorithm involves intersection of surfaces, it is under limitations of surface intersection algorithm. 5. A result cannot be generated if the underlying geometry of S is BSpline with continuity C0. Exceptions Geom_UndefinedDerivative if the underlying geometry of S is BSpline with continuity C0.
        """
    def PerformBySimple(self,theS : OCP.TopoDS.TopoDS_Shape,theOffsetValue : float) -> None: 
        """
        Constructs offset shape for the given one using simple algorithm without intersections computation.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,Offset : float,Tol : float,Mode : OCP.BRepOffset.BRepOffset_Mode=BRepOffset_Mode.BRepOffset_Skin,Intersection : bool=False,SelfInter : bool=False,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,RemoveIntEdges : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepOffsetAPI_MakePipe(OCP.BRepPrimAPI.BRepPrimAPI_MakeSweep, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build pipes. A pipe is built a basis shape (called the profile) along a wire (called the spine) by sweeping. The profile must not contain solids. A MakePipe object provides a framework for: - defining the construction of a pipe, - implementing the construction algorithm, and - consulting the result. Warning The MakePipe class implements pipe constructions with G1 continuous spines only.
    """
    def Build(self) -> None: 
        """
        Builds the resulting shape (redefined from MakeShape).
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def ErrorOnSurface(self) -> float: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the bottom of the prism.
        """
    @overload
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    @overload
    def Generated(self,SSpine : OCP.TopoDS.TopoDS_Shape,SProfile : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the top of the prism.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Pipe(self) -> OCP.BRepFill.BRepFill_Pipe: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Wire,Profile : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Wire,Profile : OCP.TopoDS.TopoDS_Shape,aMode : OCP.GeomFill.GeomFill_Trihedron,ForceApproxC1 : bool=False) -> None: ...
    pass
class BRepOffsetAPI_MakePipeShell(OCP.BRepPrimAPI.BRepPrimAPI_MakeSweep, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    This class provides for a framework to construct a shell or a solid along a spine consisting in a wire. To produce a solid, the initial wire must be closed. Two approaches are used: - definition by section - by a section and a scaling law - by addition of successive intermediary sections - definition by sweep mode. - pseudo-Frenet - constant - binormal constant - normal defined by a surface support - normal defined by a guiding contour. The two global approaches can also be combined. You can also close the surface later in order to form a solid. Warning: some limitations exist -- Mode with auxilary spine is incompatible with hometetic laws -- Mode with auxilary spine and keep contact produce only CO surface.
    """
    @overload
    def Add(self,Profile : OCP.TopoDS.TopoDS_Shape,WithContact : bool=False,WithCorrection : bool=False) -> None: 
        """
        Adds the section Profile to this framework. First and last sections may be punctual, so the shape Profile may be both wire and vertex. Correspondent point on spine is computed automatically. If WithContact is true, the section is translated to be in contact with the spine. If WithCorrection is true, the section is rotated to be orthogonal to the spine?s tangent in the correspondent point. This option has no sense if the section is punctual (Profile is of type TopoDS_Vertex).

        Adds the section Profile to this framework. Correspondent point on the spine is given by Location. Warning: To be effective, it is not recommended to combine methods Add and SetLaw.
        """
    @overload
    def Add(self,Profile : OCP.TopoDS.TopoDS_Shape,Location : OCP.TopoDS.TopoDS_Vertex,WithContact : bool=False,WithCorrection : bool=False) -> None: ...
    def Build(self) -> None: 
        """
        Builds the resulting shape (redefined from MakeShape).
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Delete(self,Profile : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Removes the section Profile from this framework.
        """
    def ErrorOnSurface(self) -> float: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the bottom of the sweep.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of new shapes generated from the shape S by the shell-generating algorithm. This function is redefined from BRepOffsetAPI_MakeShape::Generated. S can be an edge or a vertex of a given Profile (see methods Add).
        """
    def GetStatus(self) -> OCP.BRepBuilderAPI.BRepBuilderAPI_PipeError: 
        """
        Get a status, when Simulate or Build failed. It can be BRepBuilderAPI_PipeDone, BRepBuilderAPI_PipeNotDone, BRepBuilderAPI_PlaneNotIntersectGuide, BRepBuilderAPI_ImpossibleContact.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsReady(self) -> bool: 
        """
        Returns true if this tool object is ready to build the shape, i.e. has a definition for the wire section Profile.
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the top of the sweep.
        """
    def MakeSolid(self) -> bool: 
        """
        Transforms the sweeping Shell in Solid. If a propfile is not closed returns False
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Profiles(self,theProfiles : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Returns the list of original profiles
        """
    def SetDiscreteMode(self) -> None: 
        """
        Sets a Discrete trihedron to perform the sweeping
        """
    def SetForceApproxC1(self,ForceApproxC1 : bool) -> None: 
        """
        Set the flag that indicates attempt to approximate a C1-continuous surface if a swept surface proved to be C0.
        """
    @overload
    def SetLaw(self,Profile : OCP.TopoDS.TopoDS_Shape,L : OCP.Law.Law_Function,Location : OCP.TopoDS.TopoDS_Vertex,WithContact : bool=False,WithCorrection : bool=False) -> None: 
        """
        Sets the evolution law defined by the wire Profile with its position (Location, WithContact, WithCorrection are the same options as in methods Add) and a homotetic law defined by the function L. Warning: To be effective, it is not recommended to combine methods Add and SetLaw.

        Sets the evolution law defined by the wire Profile with its position (Location, WithContact, WithCorrection are the same options as in methods Add) and a homotetic law defined by the function L. Warning: To be effective, it is not recommended to combine methods Add and SetLaw.
        """
    @overload
    def SetLaw(self,Profile : OCP.TopoDS.TopoDS_Shape,L : OCP.Law.Law_Function,WithContact : bool=False,WithCorrection : bool=False) -> None: ...
    def SetMaxDegree(self,NewMaxDegree : int) -> None: 
        """
        Define the maximum V degree of resulting surface
        """
    def SetMaxSegments(self,NewMaxSegments : int) -> None: 
        """
        Define the maximum number of spans in V-direction on resulting surface
        """
    @overload
    def SetMode(self,AuxiliarySpine : OCP.TopoDS.TopoDS_Wire,CurvilinearEquivalence : bool,KeepContact : OCP.BRepFill.BRepFill_TypeOfContact=BRepFill_TypeOfContact.BRepFill_NoContact) -> None: 
        """
        Sets a Frenet or a CorrectedFrenet trihedron to perform the sweeping If IsFrenet is false, a corrected Frenet trihedron is used.

        Sets a fixed trihedron to perform the sweeping all sections will be parallel.

        Sets a fixed BiNormal direction to perform the -- sweeping. Angular relations beetween the section(s) and <BiNormal> will be constant

        Sets support to the spine to define the BiNormal of the trihedron, like the normal to the surfaces. Warning: To be effective, Each edge of the <spine> must have an representaion on one face of<SpineSupport>

        Sets an auxiliary spine to define the Normal For each Point of the Spine P, an Point Q is evalued on <AuxiliarySpine> If <CurvilinearEquivalence> Q split <AuxiliarySpine> with the same length ratio than P split <Spline>. Else the plan define by P and the tangent to the <Spine> intersect <AuxiliarySpine> in Q. If <KeepContact> equals BRepFill_NoContact: The Normal is defined by the vector PQ. If <KeepContact> equals BRepFill_Contact: The Normal is defined to achieve that the sweeped section is in contact to the auxiliarySpine. The width of section is constant all along the path. In other words, the auxiliary spine lies on the swept surface, but not necessarily is a boundary of this surface. However, the auxiliary spine has to be close enough to the main spine to provide intersection with any section all along the path. If <KeepContact> equals BRepFill_ContactOnBorder: The auxiliary spine becomes a boundary of the swept surface and the width of section varies along the path. Give section to sweep. Possibilities are : - Give one or sevral section - Give one profile and an homotetic law. - Automatic compute of correspondance beetween spine, and section on the sweeped shape - correspondance beetween spine, and section on the sweeped shape defined by a vertex of the spine
        """
    @overload
    def SetMode(self,BiNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetMode(self,Axe : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def SetMode(self,IsFrenet : bool=False) -> None: ...
    @overload
    def SetMode(self,SpineSupport : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def SetTolerance(self,Tol3d : float=0.0001,BoundTol : float=0.0001,TolAngular : float=0.01) -> None: 
        """
        Sets the following tolerance values - 3D tolerance Tol3d - boundary tolerance BoundTol - angular tolerance TolAngular.
        """
    def SetTransitionMode(self,Mode : OCP.BRepBuilderAPI.BRepBuilderAPI_TransitionMode=BRepBuilderAPI_TransitionMode.BRepBuilderAPI_Transformed) -> None: 
        """
        Sets the transition mode to manage discontinuities on the swept shape caused by fractures on the spine. The transition mode can be BRepBuilderAPI_Transformed (default value), BRepBuilderAPI_RightCorner, BRepBuilderAPI_RoundCorner: - RepBuilderAPI_Transformed: discontinuities are treated by modification of the sweeping mode. The pipe is "transformed" at the fractures of the spine. This mode assumes building a self-intersected shell. - BRepBuilderAPI_RightCorner: discontinuities are treated like right corner. Two pieces of the pipe corresponding to two adjacent segments of the spine are extended and intersected at a fracture of the spine. - BRepBuilderAPI_RoundCorner: discontinuities are treated like round corner. The corner is treated as rotation of the profile around an axis which passes through the point of the spine's fracture. This axis is based on cross product of directions tangent to the adjacent segments of the spine at their common point. Warnings The mode BRepBuilderAPI_RightCorner provides a valid result if intersection of two pieces of the pipe (corresponding to two adjacent segments of the spine) in the neighborhood of the spine?s fracture is connected and planar. This condition can be violated if the spine is non-linear in some neighborhood of the fracture or if the profile was set with a scaling law. The last mode, BRepBuilderAPI_RoundCorner, will assuredly provide a good result only if a profile was set with option WithCorrection = True, i.e. it is strictly orthogonal to the spine.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Simulate(self,NumberOfSection : int,Result : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Simulates the resulting shape by calculating its cross-sections. The spine is devided by this cross-sections into (NumberOfSection - 1) equal parts, the number of cross-sections is NumberOfSection. The cross-sections are wires and they are returned in the list Result. This gives a rapid preview of the resulting shape, which will be obtained using the settings you have provided. Raises NotDone if <me> it is not Ready
        """
    def Spine(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the spine
        """
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Wire) -> None: ...
    pass
class BRepOffsetAPI_MakeThickSolid(BRepOffsetAPI_MakeOffsetShape, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build hollowed solids. A hollowed solid is built from an initial solid and a set of faces on this solid, which are to be removed. The remaining faces of the solid become the walls of the hollowed solid, their thickness defined at the time of construction. the solid is built from an initial solid <S> and a set of faces {Fi} from <S>, builds a solid composed by two shells closed by the {Fi}. First shell <SS> is composed by all the faces of <S> expected {Fi}. Second shell is the offset shell of <SS>. A MakeThickSolid object provides a framework for: - defining the cross-section of a hollowed solid, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        None
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def GetJoinType(self) -> OCP.GeomAbs.GeomAbs_JoinType: 
        """
        Returns offset join type.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape has been removed from the result.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def MakeOffset(self) -> OCP.BRepOffset.BRepOffset_MakeOffset: 
        """
        Returns instance of the unrelying intersection / arc algorithm.
        """
    def MakeThickSolidByJoin(self,S : OCP.TopoDS.TopoDS_Shape,ClosingFaces : OCP.TopTools.TopTools_ListOfShape,Offset : float,Tol : float,Mode : OCP.BRepOffset.BRepOffset_Mode=BRepOffset_Mode.BRepOffset_Skin,Intersection : bool=False,SelfInter : bool=False,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,RemoveIntEdges : bool=False) -> None: 
        """
        Constructs a hollowed solid from the solid S by removing the set of faces ClosingFaces from S, where: Offset defines the thickness of the walls. Its sign indicates which side of the surface of the solid the hollowed shape is built on; - Tol defines the tolerance criterion for coincidence in generated shapes; - Mode defines the construction type of parallels applied to free edges of shape S. Currently, only one construction type is implemented, namely the one where the free edges do not generate parallels; this corresponds to the default value BRepOffset_Skin; Intersection specifies how the algorithm must work in order to limit the parallels to two adjacent shapes: - if Intersection is false (default value), the intersection is calculated with the parallels to the two adjacent shapes, - if Intersection is true, the intersection is calculated by taking account of all parallels generated; this computation method is more general as it avoids self-intersections generated in the offset shape from features of small dimensions on shape S, however this method has not been completely implemented and therefore is not recommended for use; - SelfInter tells the algorithm whether a computation to eliminate self-intersections needs to be applied to the resulting shape. However, as this functionality is not yet implemented, you should use the default value (false); - Join defines how to fill the holes that may appear between parallels to the two adjacent faces. It may take values GeomAbs_Arc or GeomAbs_Intersection: - if Join is equal to GeomAbs_Arc, then pipes are generated between two free edges of two adjacent parallels, and spheres are generated on "images" of vertices; it is the default value, - if Join is equal to GeomAbs_Intersection, then the parallels to the two adjacent faces are enlarged and intersected, so that there are no free edges on parallels to faces. RemoveIntEdges flag defines whether to remove the INTERNAL edges from the result or not. Warnings Since the algorithm of MakeThickSolid is based on MakeOffsetShape algorithm, the warnings are the same as for MakeOffsetShape.
        """
    def MakeThickSolidBySimple(self,theS : OCP.TopoDS.TopoDS_Shape,theOffsetValue : float) -> None: 
        """
        Constructs solid using simple algorithm. According to its nature it is not possible to set list of the closing faces. This algorithm does not support faces removing. It is caused by fact that intersections are not computed during offset creation. Non-closed shell or face is expected as input.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def PerformByJoin(self,S : OCP.TopoDS.TopoDS_Shape,Offset : float,Tol : float,Mode : OCP.BRepOffset.BRepOffset_Mode=BRepOffset_Mode.BRepOffset_Skin,Intersection : bool=False,SelfInter : bool=False,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,RemoveIntEdges : bool=False) -> None: 
        """
        Constructs a shape parallel to the shape S, where - S may be a face, a shell, a solid or a compound of these shape kinds; - Offset is the offset value. The offset shape is constructed: - outside S, if Offset is positive, - inside S, if Offset is negative; - Tol defines the coincidence tolerance criterion for generated shapes; - Mode defines the construction type of parallels applied to the free edges of shape S; currently, only one construction type is implemented, namely the one where the free edges do not generate parallels; this corresponds to the default value BRepOffset_Skin; - Intersection specifies how the algorithm must work in order to limit the parallels to two adjacent shapes: - if Intersection is false (default value), the intersection is calculated with the parallels to the two adjacent shapes, - if Intersection is true, the intersection is calculated by taking all generated parallels into account; this computation method is more general as it avoids some self-intersections generated in the offset shape from features of small dimensions on shape S, however this method has not been completely implemented and therefore is not recommended for use; - SelfInter tells the algorithm whether a computation to eliminate self-intersections must be applied to the resulting shape; however, as this functionality is not yet implemented, it is recommended to use the default value (false); - Join defines how to fill the holes that may appear between parallels to the two adjacent faces. It may take values GeomAbs_Arc or GeomAbs_Intersection: - if Join is equal to GeomAbs_Arc, then pipes are generated between two free edges of two adjacent parallels, and spheres are generated on "images" of vertices; it is the default value, - if Join is equal to GeomAbs_Intersection, then the parallels to the two adjacent faces are enlarged and intersected, so that there are no free edges on parallels to faces. RemoveIntEdges flag defines whether to remove the INTERNAL edges from the result or not. Warnings 1. All the faces of the shape S should be based on the surfaces with continuity at least C1. 2. The offset value should be sufficiently small to avoid self-intersections in resulting shape. Otherwise these self-intersections may appear inside an offset face if its initial surface is not plane or sphere or cylinder, also some non-adjacent offset faces may intersect each other. Also, some offset surfaces may "turn inside out". 3. The algorithm may fail if the shape S contains vertices where more than 3 edges converge. 4. Since 3d-offset algorithm involves intersection of surfaces, it is under limitations of surface intersection algorithm. 5. A result cannot be generated if the underlying geometry of S is BSpline with continuity C0. Exceptions Geom_UndefinedDerivative if the underlying geometry of S is BSpline with continuity C0.
        """
    def PerformBySimple(self,theS : OCP.TopoDS.TopoDS_Shape,theOffsetValue : float) -> None: 
        """
        Constructs offset shape for the given one using simple algorithm without intersections computation.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,ClosingFaces : OCP.TopTools.TopTools_ListOfShape,Offset : float,Tol : float,Mode : OCP.BRepOffset.BRepOffset_Mode=BRepOffset_Mode.BRepOffset_Skin,Intersection : bool=False,SelfInter : bool=False,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,RemoveIntEdges : bool=False) -> None: ...
    pass
class BRepOffsetAPI_MiddlePath(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build a middle path of a pipe-like shape
    """
    def Build(self) -> None: 
        """
        None
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape,StartShape : OCP.TopoDS.TopoDS_Shape,EndShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class BRepOffsetAPI_NormalProjection(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    A framework to define projection onto a shape according to the normal from each point to be projected. The target shape is a face, and the source shape is an edge or a wire.
    """
    def Add(self,ToProj : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the shape ToProj to the framework for calculation of the projection by Compute3d. ToProj is an edge or a wire and will be projected onto the basis shape. Exceptions Standard_ConstructionError if ToProj is not added.
        """
    def Ancestor(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the initial edge corresponding to the edge E resulting from the computation of the projection. Exceptions StdFail_NotDone if no edge was found. Standard_NoSuchObject if an edge corresponding to E has already been found.
        """
    def Build(self) -> None: 
        """
        Builds the result of the projection as a compound of wires. Tries to build oriented wires.
        """
    def BuildWire(self,Liste : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        build the result as a list of wire if possible in -- a first returns a wire only if there is only a wire.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Compute3d(self,With3d : bool=True) -> None: 
        """
        Returns true if a 3D curve is computed. If not, false is returned and an initial 3D curve is kept to build the resulting edges.
        """
    def Couple(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the initial face corresponding to the projected edge E. Exceptions StdFail_NotDone if no face was found. Standard_NoSuchObject if if a face corresponding to E has already been found.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes the empty constructor framework with the shape S.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the object was correctly built by the shape construction algorithm. If at the construction time of the shape, the algorithm cannot be completed, or the original data is corrupted, IsDone returns false and therefore protects the use of functions to access the result of the construction (typically the Shape function).
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Projection(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Performs the projection. The construction of the result is performed by Build. Exceptions StdFail_NotDone if the projection was not performed.
        """
    def SetLimit(self,FaceBoundaries : bool=True) -> None: 
        """
        Manage limitation of projected edges.
        """
    def SetMaxDistance(self,MaxDist : float) -> None: 
        """
        Sets the maximum distance between target shape and shape to project. If this condition is not satisfied then corresponding part of solution is discarded. if MaxDist < 0 then this method does not affect the algorithm
        """
    def SetParams(self,Tol3D : float,Tol2D : float,InternalContinuity : OCP.GeomAbs.GeomAbs_Shape,MaxDegree : int,MaxSeg : int) -> None: 
        """
        Sets the parameters used for computation Tol3 is the requiered tolerance between the 3d projected curve and its 2d representation InternalContinuity is the order of constraints used for approximation MaxDeg and MaxSeg are the maximum degree and the maximum number of segment for BSpline resulting of an approximation.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepOffsetAPI_SequenceOfSequenceOfReal(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : BRepOffsetAPI_SequenceOfSequenceOfReal) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OCP.TColStd.TColStd_SequenceOfReal) -> None: ...
    def Assign(self,theOther : BRepOffsetAPI_SequenceOfSequenceOfReal) -> BRepOffsetAPI_SequenceOfSequenceOfReal: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TColStd.TColStd_SequenceOfReal) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : BRepOffsetAPI_SequenceOfSequenceOfReal) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : BRepOffsetAPI_SequenceOfSequenceOfReal) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TColStd.TColStd_SequenceOfReal) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : OCP.TColStd.TColStd_SequenceOfReal) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : BRepOffsetAPI_SequenceOfSequenceOfReal) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : OCP.TColStd.TColStd_SequenceOfReal) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : BRepOffsetAPI_SequenceOfSequenceOfReal) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : BRepOffsetAPI_SequenceOfSequenceOfReal) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class BRepOffsetAPI_SequenceOfSequenceOfShape(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : BRepOffsetAPI_SequenceOfSequenceOfShape) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OCP.TopTools.TopTools_SequenceOfShape) -> None: ...
    def Assign(self,theOther : BRepOffsetAPI_SequenceOfSequenceOfShape) -> BRepOffsetAPI_SequenceOfSequenceOfShape: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TopTools.TopTools_SequenceOfShape) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : BRepOffsetAPI_SequenceOfSequenceOfShape) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : BRepOffsetAPI_SequenceOfSequenceOfShape) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TopTools.TopTools_SequenceOfShape) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : OCP.TopTools.TopTools_SequenceOfShape) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : BRepOffsetAPI_SequenceOfSequenceOfShape) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : OCP.TopTools.TopTools_SequenceOfShape) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : BRepOffsetAPI_SequenceOfSequenceOfShape) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : BRepOffsetAPI_SequenceOfSequenceOfShape) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class BRepOffsetAPI_ThruSections(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build a loft. This is a shell or a solid passing through a set of sections in a given sequence. Usually sections are wires, but the first and the last sections may be vertices (punctual sections).
    """
    def AddVertex(self,aVertex : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Adds the vertex Vertex (punctual section) to the set of sections through which the shell or solid is built. A vertex may be added to the set of sections only as first or last section. At least one wire must be added to the set of sections by the method AddWire. Use the Build function to construct the shape.
        """
    def AddWire(self,wire : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Adds the wire wire to the set of sections through which the shell or solid is built. Use the Build function to construct the shape.
        """
    def Build(self) -> None: 
        """
        None
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CheckCompatibility(self,check : bool=True) -> None: 
        """
        Sets/unsets the option to compute origin and orientation on wires to avoid twisted results and update wires to have same number of edges.
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        returns the Continuity used in the approximation
        """
    def CriteriumWeight(self) -> Tuple[float, float, float]: 
        """
        returns the Weights associed to the criterium used in the optimization.
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the bottom of the loft if solid
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of new shapes generated from the shape S by the shell-generating algorithm. This function is redefined from BRepBuilderAPI_MakeShape::Generated. S can be an edge or a vertex of a given Profile (see methods AddWire and AddVertex).
        """
    def GeneratedFace(self,Edge : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        if Ruled Returns the Face generated by each edge except the last wire if smoothed Returns the Face generated by each edge of the first wire
        """
    def Init(self,isSolid : bool=False,ruled : bool=False,pres3d : float=1e-06) -> None: 
        """
        Initializes this algorithm for building a shell or a solid passing through a set of sections, where: - isSolid is set to true if this construction algorithm is required to build a solid or to false if it is required to build a shell. false is the default value; - ruled is set to true if the faces generated between the edges of two consecutive wires are ruled surfaces or to false (the default value) if they are smoothed out by approximation, - pres3d defines the precision criterion used by the approximation algorithm; the default value is 1.0e-6. Use AddWire and AddVertex to define the successive sections of the shell or solid to be built.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the top of the loft if solid
        """
    def MaxDegree(self) -> int: 
        """
        returns the maximal U degree of result surface
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def ParType(self) -> OCP.Approx.Approx_ParametrizationType: 
        """
        returns the type of parametrization used in the approximation
        """
    def SetContinuity(self,C : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Define the Continuity used in the approximation
        """
    def SetCriteriumWeight(self,W1 : float,W2 : float,W3 : float) -> None: 
        """
        define the Weights associed to the criterium used in the optimization.
        """
    def SetMaxDegree(self,MaxDeg : int) -> None: 
        """
        Define the maximal U degree of result surface
        """
    def SetParType(self,ParType : OCP.Approx.Approx_ParametrizationType) -> None: 
        """
        Define the type of parametrization used in the approximation
        """
    def SetSmoothing(self,UseSmoothing : bool) -> None: 
        """
        Define the approximation algorithm
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def UseSmoothing(self) -> bool: 
        """
        Define the approximation algorithm
        """
    def Wires(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of original wires
        """
    def __init__(self,isSolid : bool=False,ruled : bool=False,pres3d : float=1e-06) -> None: ...
    pass
