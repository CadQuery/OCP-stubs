import OCP.BRepFilletAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.ChFi2d
import OCP.GeomAbs
import OCP.Law
import OCP.BRepBuilderAPI
import OCP.TopTools
import OCP.TColgp
import OCP.TopOpeBRepBuild
import OCP.ChFi3d
import OCP.TopoDS
import OCP.ChFiDS
import OCP.Geom
__all__  = [
"BRepFilletAPI_LocalOperation",
"BRepFilletAPI_MakeChamfer",
"BRepFilletAPI_MakeFillet",
"BRepFilletAPI_MakeFillet2d"
]
class BRepFilletAPI_LocalOperation(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Construction of fillets on the edges of a Shell.
    """
    def Abscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        returns the abscissa of the vertex V on the contour of index IC.
        """
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Adds a contour in the builder (builds a contour of tangent edges).
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Closed(self,IC : int) -> bool: 
        """
        returns true if the contour of index IC is closed
        """
    def ClosedAndTangent(self,IC : int) -> bool: 
        """
        returns true if the contour of index IC is closed an tangent.
        """
    def Contour(self,E : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        Returns the index of the contour containing the edge E, returns 0 if E doesn't belong to any contour.
        """
    def Edge(self,I : int,J : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the Edge J in the contour I.
        """
    def FirstVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the first Vertex of the contour of index IC.
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
    def LastVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the last Vertex of the contour of index IC.
        """
    def Length(self,IC : int) -> float: 
        """
        returns the length the contour of index IC.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def NbContours(self) -> int: 
        """
        Number of contours.
        """
    def NbEdges(self,I : int) -> int: 
        """
        Number of Edges in the contour I.
        """
    def NbSurf(self,IC : int) -> int: 
        """
        None
        """
    def RelativeAbscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        returns the relative abscissa([0.,1.]) of the vertex V on the contour of index IC.
        """
    def Remove(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        remove the contour containing the Edge E.
        """
    def Reset(self) -> None: 
        """
        Reset all the fields updated by Build operation and leave the algorithm in the same state than before build call. It allows contours and radius modifications to build the result another time.
        """
    def ResetContour(self,IC : int) -> None: 
        """
        Reset the contour of index IC, there is nomore information in the contour.
        """
    def Sect(self,IC : int,IS : int) -> OCP.ChFiDS.ChFiDS_SecHArray1: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Simulate(self,IC : int) -> None: 
        """
        None
        """
    pass
class BRepFilletAPI_MakeChamfer(BRepFilletAPI_LocalOperation, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build chamfers on edges of a shell or solid. Chamfered Edge of a Shell or Solid A MakeChamfer object provides a framework for: - initializing the construction algorithm with a given shape, - acquiring the data characterizing the chamfers, - building the chamfers and constructing the resulting shape, and - consulting the result.
    """
    def Abscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        Returns the curvilinear abscissa of the vertex V on the contour of index IC in the internal data structure of this algorithm. Warning Returns -1. if: - IC is outside the bounds of the table of contours, or - V is not on the contour of index IC.
        """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Adds edge E to the table of edges used by this algorithm to build chamfers, where the parameters of the chamfer must be set after the

        Adds edge E to the table of edges used by this algorithm to build chamfers, where the parameters of the chamfer are given by the distance Dis (symmetric chamfer). The Add function results in a contour being built by propagation from the edge E (i.e. the contour contains at least this edge). This contour is composed of edges of the shape which are tangential to one another and which delimit two series of tangential faces, with one series of faces being located on either side of the contour. Warning Nothing is done if edge E or the face F does not belong to the initial shape.

        Adds edge E to the table of edges used by this algorithm to build chamfers, where the parameters of the chamfer are given by the two distances Dis1 and Dis2; the face F identifies the side where Dis1 is measured. The Add function results in a contour being built by propagation from the edge E (i.e. the contour contains at least this edge). This contour is composed of edges of the shape which are tangential to one another and which delimit two series of tangential faces, with one series of faces being located on either side of the contour. Warning Nothing is done if edge E or the face F does not belong to the initial shape.
        """
    @overload
    def Add(self,Dis : float,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def Add(self,Dis1 : float,Dis2 : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    def AddDA(self,Dis : float,Angle : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Adds a fillet contour in the builder (builds a contour of tangent edges to <E> and sets the distance <Dis1> and angle <Angle> ( parameters of the chamfer ) ).
        """
    def Build(self) -> None: 
        """
        Builds the chamfers on all the contours in the internal data structure of this algorithm and constructs the resulting shape. Use the function IsDone to verify that the chamfered shape is built. Use the function Shape to retrieve the chamfered shape. Warning The construction of chamfers implements highly complex construction algorithms. Consequently, there may be instances where the algorithm fails, for example if the data defining the parameters of the chamfer is not compatible with the geometry of the initial shape. There is no initial analysis of errors and these only become evident at the construction stage. Additionally, in the current software release, the following cases are not handled: - the end point of the contour is the point of intersection of 4 or more edges of the shape, or - the intersection of the chamfer with a face which limits the contour is not fully contained in this face.
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
        """
        Returns the internal filleting algorithm.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Closed(self,IC : int) -> bool: 
        """
        Returns true if the contour of index IC in the internal data structure of this algorithm is closed. Warning Returns false if IC is outside the bounds of the table of contours.
        """
    def ClosedAndTangent(self,IC : int) -> bool: 
        """
        eturns true if the contour of index IC in the internal data structure of this algorithm is closed and tangential at the point of closure. Warning Returns false if IC is outside the bounds of the table of contours.
        """
    def Contour(self,E : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        Returns the index of the contour in the internal data structure of this algorithm, which contains the edge E of the shape. This function returns 0 if the edge E does not belong to any contour. Warning This index can change if a contour is removed from the internal data structure of this algorithm using the function Remove.
        """
    def Dists(self,IC : int) -> Tuple[float, float]: 
        """
        Returns the distances Dis1 and Dis2 which give the parameters of the chamfer along the contour of index IC in the internal data structure of this algorithm. Warning -1. is returned if IC is outside the bounds of the table of contours.
        """
    def Edge(self,I : int,J : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge of index J in the contour of index I in the internal data structure of this algorithm. Warning Returns a null shape if: - I is outside the bounds of the table of contours, or - J is outside the bounds of the table of edges of the contour of index I.
        """
    def FirstVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the first vertex of the contour of index IC in the internal data structure of this algorithm. Warning Returns a null shape if IC is outside the bounds of the table of contours.
        """
    def Generated(self,EorV : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <EorV>.
        """
    def GetDist(self,IC : int) -> Tuple[float]: 
        """
        None
        """
    def GetDistAngle(self,IC : int) -> Tuple[float, float]: 
        """
        gives the distances <Dis> and <Angle> of the fillet contour of index <IC> in the DS
        """
    def IsDeleted(self,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsDistanceAngle(self,IC : int) -> bool: 
        """
        return True if chamfer is made with distance and angle false else.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsSymetric(self,IC : int) -> bool: 
        """
        return True if chamfer symetric false else.
        """
    def IsTwoDistances(self,IC : int) -> bool: 
        """
        return True if chamfer is made with two distances false else.
        """
    def LastVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the last vertex of the contour of index IC in the internal data structure of this algorithm. Warning Returns a null shape if IC is outside the bounds of the table of contours.
        """
    def Length(self,IC : int) -> float: 
        """
        Returns the length of the contour of index IC in the internal data structure of this algorithm. Warning Returns -1. if IC is outside the bounds of the table of contours.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <F>.
        """
    def NbContours(self) -> int: 
        """
        Returns the number of contours generated using the Add function in the internal data structure of this algorithm.
        """
    def NbEdges(self,I : int) -> int: 
        """
        Returns the number of edges in the contour of index I in the internal data structure of this algorithm. Warning Returns 0 if I is outside the bounds of the table of contours.
        """
    def NbSurf(self,IC : int) -> int: 
        """
        None
        """
    def RelativeAbscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        Returns the relative curvilinear abscissa (i.e. between 0 and 1) of the vertex V on the contour of index IC in the internal data structure of this algorithm. Warning Returns -1. if: - IC is outside the bounds of the table of contours, or - V is not on the contour of index IC.
        """
    def Remove(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Removes the contour in the internal data structure of this algorithm which contains the edge E of the shape. Warning Nothing is done if the edge E does not belong to the contour in the internal data structure of this algorithm.
        """
    def Reset(self) -> None: 
        """
        Reinitializes this algorithm, thus canceling the effects of the Build function. This function allows modifications to be made to the contours and chamfer parameters in order to rebuild the shape.
        """
    def ResetContour(self,IC : int) -> None: 
        """
        Erases the chamfer parameters on the contour of index IC in the internal data structure of this algorithm. Use the SetDists function to reset this data. Warning Nothing is done if IC is outside the bounds of the table of contours.
        """
    def Sect(self,IC : int,IS : int) -> OCP.ChFiDS.ChFiDS_SecHArray1: 
        """
        None
        """
    def SetDist(self,Dis : float,IC : int,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the distances Dis1 and Dis2 which give the parameters of the chamfer along the contour of index IC generated using the Add function in the internal data structure of this algorithm. The face F identifies the side where Dis1 is measured. Warning Nothing is done if either the edge E or the face F does not belong to the initial shape.
        """
    def SetDistAngle(self,Dis : float,Angle : float,IC : int,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        set the distance <Dis> and <Angle> of the fillet contour of index <IC> in the DS with <Dis> on <F>. if the face <F> is not one of common faces of an edge of the contour <IC>
        """
    def SetDists(self,Dis1 : float,Dis2 : float,IC : int,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the distances Dis1 and Dis2 which give the parameters of the chamfer along the contour of index IC generated using the Add function in the internal data structure of this algorithm. The face F identifies the side where Dis1 is measured. Warning Nothing is done if either the edge E or the face F does not belong to the initial shape.
        """
    def SetMode(self,theMode : OCP.ChFiDS.ChFiDS_ChamfMode) -> None: 
        """
        Sets the mode of chamfer
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Simulate(self,IC : int) -> None: 
        """
        None
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class BRepFilletAPI_MakeFillet(BRepFilletAPI_LocalOperation, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build fillets on the broken edges of a shell or solid. A MakeFillet object provides a framework for: - initializing the construction algorithm with a given shape, - acquiring the data characterizing the fillets, - building the fillets and constructing the resulting shape, and - consulting the result.
    """
    def Abscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        Returns the curvilinear abscissa of the vertex V on the contour of index IC in the internal data structure of this algorithm. Warning Returns -1. if: - IC is outside the bounds of the table of contours, or - V is not on the contour of index IC.
        """
    @overload
    def Add(self,Radius : float,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Adds a fillet contour in the builder (builds a contour of tangent edges). The Radius must be set after.

        Adds a fillet description in the builder - builds a contour of tangent edges, - sets the radius.

        Adds a fillet description in the builder - builds a contour of tangent edges, - sets a linear radius evolution law between the first and last vertex of the spine.

        Adds a fillet description in the builder - builds a contour of tangent edges, - sest the radius evolution law.

        Adds a fillet description in the builder - builds a contour of tangent edges, - sets the radius evolution law interpolating the values given in the array UandR :
        """
    @overload
    def Add(self,UandR : OCP.TColgp.TColgp_Array1OfPnt2d,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def Add(self,R1 : float,R2 : float,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def Add(self,L : OCP.Law.Law_Function,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    def BadShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        if (HasResult()) returns the partial result
        """
    def Build(self) -> None: 
        """
        Builds the fillets on all the contours in the internal data structure of this algorithm and constructs the resulting shape. Use the function IsDone to verify that the filleted shape is built. Use the function Shape to retrieve the filleted shape. Warning The construction of fillets implements highly complex construction algorithms. Consequently, there may be instances where the algorithm fails, for example if the data defining the radius of the fillet is not compatible with the geometry of the initial shape. There is no initial analysis of errors and they only become evident at the construction stage. Additionally, in the current software release, the following cases are not handled: - the end point of the contour is the point of intersection of 4 or more edges of the shape, or - the intersection of the fillet with a face which limits the contour is not fully contained in this face.
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
        """
        Returns the internal topology building algorithm.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Closed(self,IC : int) -> bool: 
        """
        Returns true if the contour of index IC in the internal data structure of this algorithm is closed. Warning Returns false if IC is outside the bounds of the table of contours.
        """
    def ClosedAndTangent(self,IC : int) -> bool: 
        """
        Returns true if the contour of index IC in the internal data structure of this algorithm is closed and tangential at the point of closure. Warning Returns false if IC is outside the bounds of the table of contours.
        """
    def ComputedSurface(self,IC : int,IS : int) -> OCP.Geom.Geom_Surface: 
        """
        returns the surface number IS concerning the contour IC
        """
    def Contour(self,E : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        Returns the index of the contour in the internal data structure of this algorithm which contains the edge E of the shape. This function returns 0 if the edge E does not belong to any contour. Warning This index can change if a contour is removed from the internal data structure of this algorithm using the function Remove.
        """
    def Edge(self,I : int,J : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge of index J in the contour of index I in the internal data structure of this algorithm. Warning Returns a null shape if: - I is outside the bounds of the table of contours, or - J is outside the bounds of the table of edges of the index I contour.
        """
    def FaultyContour(self,I : int) -> int: 
        """
        for each I in [1.. NbFaultyContours] returns the index IC of the contour where the computation of the fillet failed. the method NbEdges(IC) gives the number of edges in the contour IC the method Edge(IC,ie) gives the edge number ie of the contour IC
        """
    def FaultyVertex(self,IV : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        returns the vertex where the computation failed
        """
    def FirstVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the first vertex of the contour of index IC in the internal data structure of this algorithm. Warning Returns a null shape if IC is outside the bounds of the table of contours.
        """
    def Generated(self,EorV : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <EorV>.
        """
    def GetBounds(self,IC : int,E : OCP.TopoDS.TopoDS_Edge,F : float,L : float) -> bool: 
        """
        None
        """
    def GetFilletShape(self) -> OCP.ChFi3d.ChFi3d_FilletShape: 
        """
        Returns the type of fillet shape built by this algorithm.
        """
    def GetLaw(self,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> OCP.Law.Law_Function: 
        """
        None
        """
    def HasResult(self) -> bool: 
        """
        returns true if a part of the result has been computed if the filling in a corner failed a shape with a hole is returned
        """
    @overload
    def IsConstant(self,IC : int) -> bool: 
        """
        Returns true if the radius of the fillet along the contour of index IC in the internal data structure of this algorithm is constant, Warning False is returned if IC is outside the bounds of the table of contours or if E does not belong to the contour of index IC.

        Returns true if the radius of the fillet along the edge E of the contour of index IC in the internal data structure of this algorithm is constant. Warning False is returned if IC is outside the bounds of the table of contours or if E does not belong to the contour of index IC.
        """
    @overload
    def IsConstant(self,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> bool: ...
    def IsDeleted(self,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the last vertex of the contour of index IC in the internal data structure of this algorithm. Warning Returns a null shape if IC is outside the bounds of the table of contours.
        """
    def Length(self,IC : int) -> float: 
        """
        Returns the length of the contour of index IC in the internal data structure of this algorithm. Warning Returns -1. if IC is outside the bounds of the table of contours.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <F>.
        """
    def NbComputedSurfaces(self,IC : int) -> int: 
        """
        returns the number of surfaces which have been computed on the contour IC
        """
    def NbContours(self) -> int: 
        """
        Returns the number of contours generated using the Add function in the internal data structure of this algorithm.
        """
    def NbEdges(self,I : int) -> int: 
        """
        Returns the number of edges in the contour of index I in the internal data structure of this algorithm. Warning Returns 0 if I is outside the bounds of the table of contours.
        """
    def NbFaultyContours(self) -> int: 
        """
        Returns the number of contours where the computation of the fillet failed
        """
    def NbFaultyVertices(self) -> int: 
        """
        returns the number of vertices where the computation failed
        """
    def NbSurf(self,IC : int) -> int: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        returns the number of surfaces after the shape creation.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the faces created for surface <I>.
        """
    @overload
    def Radius(self,IC : int) -> float: 
        """
        Returns the radius of the fillet along the contour of index IC in the internal data structure of this algorithm Warning - Use this function only if the radius is constant. - -1. is returned if IC is outside the bounds of the table of contours or if E does not belong to the contour of index IC.

        Returns the radius of the fillet along the edge E of the contour of index IC in the internal data structure of this algorithm. Warning - Use this function only if the radius is constant. - -1 is returned if IC is outside the bounds of the table of contours or if E does not belong to the contour of index IC.
        """
    @overload
    def Radius(self,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> float: ...
    def RelativeAbscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        Returns the relative curvilinear abscissa (i.e. between 0 and 1) of the vertex V on the contour of index IC in the internal data structure of this algorithm. Warning Returns -1. if: - IC is outside the bounds of the table of contours, or - V is not on the contour of index IC.
        """
    def Remove(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Removes the contour in the internal data structure of this algorithm which contains the edge E of the shape. Warning Nothing is done if the edge E does not belong to the contour in the internal data structure of this algorithm.
        """
    def Reset(self) -> None: 
        """
        Reinitializes this algorithm, thus canceling the effects of the Build function. This function allows modifications to be made to the contours and fillet parameters in order to rebuild the shape.
        """
    def ResetContour(self,IC : int) -> None: 
        """
        Erases the radius information on the contour of index IC in the internal data structure of this algorithm. Use the SetRadius function to reset this data. Warning Nothing is done if IC is outside the bounds of the table of contours.
        """
    def Sect(self,IC : int,IS : int) -> OCP.ChFiDS.ChFiDS_SecHArray1: 
        """
        None
        """
    def SetContinuity(self,InternalContinuity : OCP.GeomAbs.GeomAbs_Shape,AngularTolerance : float) -> None: 
        """
        Changes the parameters of continiuity InternalContinuity to produce fillet'surfaces with an continuity Ci (i=0,1 or 2). By defaultInternalContinuity = GeomAbs_C1. AngularTolerance is the G1 tolerance between fillet and support'faces.
        """
    def SetFilletShape(self,FShape : OCP.ChFi3d.ChFi3d_FilletShape) -> None: 
        """
        Assigns FShape as the type of fillet shape built by this algorithm.
        """
    def SetLaw(self,IC : int,E : OCP.TopoDS.TopoDS_Edge,L : OCP.Law.Law_Function) -> None: 
        """
        None
        """
    def SetParams(self,Tang : float,Tesp : float,T2d : float,TApp3d : float,TolApp2d : float,Fleche : float) -> None: 
        """
        None
        """
    @overload
    def SetRadius(self,Radius : float,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Sets the parameters of the fillet along the contour of index IC generated using the Add function in the internal data structure of this algorithm, where Radius is the radius of the fillet.

        Sets the parameters of the fillet along the contour of index IC generated using the Add function in the internal data structure of this algorithm, where the radius of the fillet evolves according to a linear evolution law defined from R1 to R2, between the first and last vertices of the contour of index IC.

        Sets the parameters of the fillet along the contour of index IC generated using the Add function in the internal data structure of this algorithm, where the radius of the fillet evolves according to the evolution law L, between the first and last vertices of the contour of index IC.

        Sets the parameters of the fillet along the contour of index IC generated using the Add function in the internal data structure of this algorithm, where the radius of the fillet evolves according to the evolution law which interpolates the set of parameter and radius pairs given in the array UandR as follows: - the X coordinate of a point in UandR defines a relative parameter on the contour (i.e. a parameter between 0 and 1), - the Y coordinate of a point in UandR gives the corresponding value of the radius, and the radius evolves between the first and last vertices of the contour of index IC.

        Assigns Radius as the radius of the fillet on the edge E

        None
        """
    @overload
    def SetRadius(self,R1 : float,R2 : float,IC : int,IinC : int) -> None: ...
    @overload
    def SetRadius(self,UandR : OCP.TColgp.TColgp_Array1OfPnt2d,IC : int,IinC : int) -> None: ...
    @overload
    def SetRadius(self,Radius : float,IC : int,IinC : int) -> None: ...
    @overload
    def SetRadius(self,L : OCP.Law.Law_Function,IC : int,IinC : int) -> None: ...
    @overload
    def SetRadius(self,Radius : float,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Simulate(self,IC : int) -> None: 
        """
        None
        """
    def StripeStatus(self,IC : int) -> OCP.ChFiDS.ChFiDS_ErrorStatus: 
        """
        returns the status concerning the contour IC in case of error ChFiDS_Ok : the computation is Ok ChFiDS_StartsolFailure : the computation can't start, perhaps the the radius is too big ChFiDS_TwistedSurface : the computation failed because of a twisted surface ChFiDS_WalkingFailure : there is a problem in the walking ChFiDS_Error: other error different from above
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,FShape : OCP.ChFi3d.ChFi3d_FilletShape=ChFi3d_FilletShape.ChFi3d_Rational) -> None: ...
    pass
class BRepFilletAPI_MakeFillet2d(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build fillets and chamfers on the vertices of a planar face. Fillets and Chamfers on the Vertices of a Planar Face A MakeFillet2d object provides a framework for: - initializing the construction algorithm with a given face, - acquiring the data characterizing the fillets and chamfers, - building the fillets and chamfers, and constructing the resulting shape, and - consulting the result. Warning Only segments of straight lines and arcs of circles are treated. BSplines are not processed.
    """
    @overload
    def AddChamfer(self,E : OCP.TopoDS.TopoDS_Edge,V : OCP.TopoDS.TopoDS_Vertex,D : float,Ang : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Adds a chamfer on the face modified by this algorithm between the two adjacent edges E1 and E2, where the extremities of the chamfer are on E1 and E2 at distances D1 and D2 respectively In cases where the edges are not rectilinear, distances are measured using the curvilinear abscissa of the edges and the angle is measured with respect to the tangent at the corresponding point. The angle Ang is given in radians. This function returns the chamfer and builds the resulting face.

        Adds a chamfer on the face modified by this algorithm between the two edges connected by the vertex V, where E is one of the two edges. The chamfer makes an angle Ang with E and one of its extremities is on E at distance D from V. In cases where the edges are not rectilinear, distances are measured using the curvilinear abscissa of the edges and the angle is measured with respect to the tangent at the corresponding point. The angle Ang is given in radians. This function returns the chamfer and builds the resulting face. Warning The status of the construction, as given by the Status function, can be one of the following: - ChFi2d_IsDone if the chamfer is built, - ChFi2d_ParametersError if D1, D2, D or Ang is less than or equal to zero, - ChFi2d_ConnexionError if: - the edge E, E1 or E2 does not belong to the initial face, or - the edges E1 and E2 are not adjacent, or - the vertex V is not one of the limit points of the edge E, - ChFi2d_ComputationError if the parameters of the chamfer are too large to build a chamfer between the two adjacent edges, - ChFi2d_NotAuthorized if: - the edge E1, E2 or one of the two edges connected to V is a fillet or chamfer, or - a curve other than a straight line or an arc of a circle is used as E, E1 or E2. Do not use the returned chamfer if the status of the construction is not ChFi2d_IsDone.
        """
    @overload
    def AddChamfer(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,D1 : float,D2 : float) -> OCP.TopoDS.TopoDS_Edge: ...
    def AddFillet(self,V : OCP.TopoDS.TopoDS_Vertex,Radius : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Adds a fillet of radius Radius between the two edges adjacent to the vertex V on the face modified by this algorithm. The two edges do not need to be rectilinear. This function returns the fillet and builds the resulting face. Warning The status of the construction, as given by the Status function, can be one of the following: - ChFi2d_IsDone if the fillet is built, - ChFi2d_ConnexionError if V does not belong to the initial face, - ChFi2d_ComputationError if Radius is too large to build a fillet between the two adjacent edges, - ChFi2d_NotAuthorized - if one of the two edges connected to V is a fillet or chamfer, or - if a curve other than a straight line or an arc of a circle is used as E, E1 or E2. Do not use the returned fillet if the status of the construction is not ChFi2d_IsDone. Exceptions Standard_NegativeValue if Radius is less than or equal to zero.
        """
    def BasisEdge(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the basis edge on the face modified by this algorithm from which the chamfered or filleted edge E is built. If E has not been modified, this function returns E. Warning E is returned if it does not belong to the initial face.
        """
    def Build(self) -> None: 
        """
        Update the result and set the Done flag
        """
    def ChamferEdges(self) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        Returns the table of chamfers on the face modified by this algorithm.

        Returns the table of chamfers on the face modified by this algorithm.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DescendantEdge(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the chamfered or filleted edge built from the edge E on the face modified by this algorithm. If E has not been modified, this function returns E. Exceptions Standard_NoSuchObject if the edge E does not belong to the initial face.

        Returns the chamfered or filleted edge built from the edge E on the face modified by this algorithm. If E has not been modified, this function returns E. Exceptions Standard_NoSuchObject if the edge E does not belong to the initial face.
        """
    def FilletEdges(self) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        Returns the table of fillets on the face modified by this algorithm.

        Returns the table of fillets on the face modified by this algorithm.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def HasDescendant(self,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None

        None
        """
    @overload
    def Init(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Initializes this algorithm for constructing fillets or chamfers with the face F. Warning The status of the initialization, as given by the Status function, can be one of the following: - ChFi2d_Ready if the initialization is correct, - ChFi2d_NotPlanar if F is not planar, - ChFi2d_NoFace if F is a null face.

        This initialize method allow to init the builder from a face <RefFace> and another face <ModFace> which derive from <RefFace>. This is usefull to modify a fillet or a chamfer already created on <ModFace> .
        """
    @overload
    def Init(self,RefFace : OCP.TopoDS.TopoDS_Face,ModFace : OCP.TopoDS.TopoDS_Face) -> None: ...
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsModified(self,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Returns true if the edge E on the face modified by this algorithm is chamfered or filleted. Warning Returns false if E does not belong to the face modified by this algorithm.

        Returns true if the edge E on the face modified by this algorithm is chamfered or filleted. Warning Returns false if E does not belong to the face modified by this algorithm.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    @overload
    def ModifyChamfer(self,Chamfer : OCP.TopoDS.TopoDS_Edge,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,D1 : float,D2 : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Modifies the chamfer Chamfer on the face modified by this algorithm, where: E1 and E2 are the two adjacent edges on which Chamfer is already built; the extremities of the new chamfer are on E1 and E2 at distances D1 and D2 respectively.

        Modifies the chamfer Chamfer on the face modified by this algorithm, where: E is one of the two adjacent edges on which Chamfer is already built; the new chamfer makes an angle Ang with E and one of its extremities is on E at distance D from the vertex on which the chamfer is built. In cases where the edges are not rectilinear, the distances are measured using the curvilinear abscissa of the edges and the angle is measured with respect to the tangent at the corresponding point. The angle Ang is given in radians. This function returns the new chamfer and modifies the existing face. Warning The status of the construction, as given by the Status function, can be one of the following: - ChFi2d_IsDone if the chamfer is built, - ChFi2d_ParametersError if D1, D2, D or Ang is less than or equal to zero, - ChFi2d_ConnexionError if: - the edge E, E1, E2 or Chamfer does not belong to the existing face, or - the edges E1 and E2 are not adjacent, - ChFi2d_ComputationError if the parameters of the chamfer are too large to build a chamfer between the two adjacent edges, - ChFi2d_NotAuthorized if E1 or E2 is a fillet or chamfer. Do not use the returned chamfer if the status of the construction is not ChFi2d_IsDone.
        """
    @overload
    def ModifyChamfer(self,Chamfer : OCP.TopoDS.TopoDS_Edge,E : OCP.TopoDS.TopoDS_Edge,D : float,Ang : float) -> OCP.TopoDS.TopoDS_Edge: ...
    def ModifyFillet(self,Fillet : OCP.TopoDS.TopoDS_Edge,Radius : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Assigns the radius Radius to the fillet Fillet already built on the face modified by this algorithm. This function returns the new fillet and modifies the existing face. Warning The status of the construction, as given by the Status function, can be one of the following: - ChFi2d_IsDone if the new fillet is built, - ChFi2d_ConnexionError if Fillet does not belong to the existing face, - ChFi2d_ComputationError if Radius is too large to build a fillet between the two adjacent edges. Do not use the returned fillet if the status of the construction is not ChFi2d_IsDone. Exceptions Standard_NegativeValue if Radius is less than or equal to zero.
        """
    def NbChamfer(self) -> int: 
        """
        Returns the number of chamfers on the face modified by this algorithm.

        Returns the number of chamfers on the face modified by this algorithm.
        """
    def NbCurves(self) -> int: 
        """
        returns the number of new curves after the shape creation.
        """
    def NbFillet(self) -> int: 
        """
        Returns the number of fillets on the face modified by this algorithm.

        Returns the number of fillets on the face modified by this algorithm.
        """
    def NewEdges(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Return the Edges created for curve I.
        """
    def RemoveChamfer(self,Chamfer : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Removes the chamfer Chamfer already built on the face modified by this algorithm. This function returns the vertex connecting the two adjacent edges of Chamfer and modifies the existing face. Warning - The returned vertex is only valid if the Status function returns ChFi2d_IsDone. - A null vertex is returned if the edge Chamfer does not belong to the initial face.
        """
    def RemoveFillet(self,Fillet : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Removes the fillet Fillet already built on the face modified by this algorithm. This function returns the vertex connecting the two adjacent edges of Fillet and modifies the existing face. Warning - The returned vertex is only valid if the Status function returns ChFi2d_IsDone. - A null vertex is returned if the edge Fillet does not belong to the initial face.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Status(self) -> OCP.ChFi2d.ChFi2d_ConstructionError: 
        """
        None

        None
        """
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
