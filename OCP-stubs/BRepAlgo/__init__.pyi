import OCP.BRepAlgo
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.TopTools
import OCP.TopOpeBRepBuild
import OCP.BRepBuilderAPI
import OCP.GeomAbs
import OCP.gp
import OCP.Geom
import OCP.TopoDS
import OCP.Standard
import OCP.TopAbs
__all__  = [
"BRepAlgo",
"BRepAlgo_AsDes",
"BRepAlgo_BooleanOperation",
"BRepAlgo_CheckStatus",
"BRepAlgo_Common",
"BRepAlgo_Cut",
"BRepAlgo_FaceRestrictor",
"BRepAlgo_Fuse",
"BRepAlgo_Image",
"BRepAlgo_Loop",
"BRepAlgo_NormalProjection",
"BRepAlgo_Section",
"BRepAlgo_Tool",
"BRepAlgo_NOK",
"BRepAlgo_OK"
]
class BRepAlgo():
    """
    The BRepAlgo package provides a full range of services to perform Old Boolean Operations in Open CASCADE. Attention: The New Boolean Operation has replaced the Old Boolean Operations algorithm in the BrepAlgoAPI package in Open CASCADE.
    """
    @staticmethod
    def ConcatenateWireC0_s(Wire : OCP.TopoDS.TopoDS_Wire) -> OCP.TopoDS.TopoDS_Edge: 
        """
        this method makes an edge from a wire. Junction points between edges of wire may be sharp, resulting curve of the resulting edge may be C0.
        """
    @staticmethod
    def ConcatenateWire_s(Wire : OCP.TopoDS.TopoDS_Wire,Option : OCP.GeomAbs.GeomAbs_Shape,AngularTolerance : float=0.0001) -> OCP.TopoDS.TopoDS_Wire: 
        """
        this method makes a wire whose edges are C1 from a Wire whose edges could be G1. It removes a vertex between G1 edges. Option can be G1 or C1.
        """
    @staticmethod
    def IsTopologicallyValid_s(S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the shape is "correct". If not, returns <Standard_False>, else returns <Standard_True>. This method differs from the previous one in the fact that no geometric contols (intersection of wires, pcurve validity) are performed.
        """
    @staticmethod
    @overload
    def IsValid_s(S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the shape is "correct". If not, returns <Standard_False>, else returns <Standard_True>.

        Checks if the Generated and Modified Faces from the shapes <arguments> in the shape <result> are "correct". The args may be empty, then all faces will be checked. If <Closed> is True, only closed shape are valid. If <GeomCtrl> is False the geometry of new vertices and edges are not verified and the auto-intersection of new wires are not searched.
        """
    @staticmethod
    @overload
    def IsValid_s(theArgs : OCP.TopTools.TopTools_ListOfShape,theResult : OCP.TopoDS.TopoDS_Shape,closedSolid : bool=False,GeomCtrl : bool=True) -> bool: ...
    def __init__(self) -> None: ...
    pass
class BRepAlgo_AsDes(OCP.Standard.Standard_Transient):
    """
    SD to store descendants and ascendants of Shapes.SD to store descendants and ascendants of Shapes.SD to store descendants and ascendants of Shapes.
    """
    @overload
    def Add(self,S : OCP.TopoDS.TopoDS_Shape,SS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Stores <SS> as a futur subshape of <S>.

        Stores <SS> as futurs SubShapes of <S>.
        """
    @overload
    def Add(self,S : OCP.TopoDS.TopoDS_Shape,SS : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    def Ascendant(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Shape containing <S>.
        """
    def ChangeDescendant(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns futur subhapes of <S>.
        """
    def Clear(self) -> None: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Descendant(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns futur subhapes of <S>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasAscendant(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def HasCommonDescendant(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,LC : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        Returns True if (S1> and <S2> has common Descendants. Stores in <LC> the Commons Descendants.
        """
    def HasDescendant(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
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
    def Remove(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove <S> from me.
        """
    def Replace(self,OldS : OCP.TopoDS.TopoDS_Shape,NewS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Replace <OldS> by <NewS>. <OldS> disapear from <me>.
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
class BRepAlgo_BooleanOperation(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The abstract class BooleanOperation is the root class of Boolean operations. A BooleanOperation object stores the two shapes in preparation for the Boolean operation specified in one of the classes inheriting from this one. These include: - Common - Cut - Fuse - Section.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
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
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Perform(self,St1 : OCP.TopAbs.TopAbs_State,St2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def PerformDS(self) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first shape involved in this Boolean operation.
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second shape involved in this Boolean operation.
        """
    pass
class BRepAlgo_CheckStatus():
    """
    None

    Members:

      BRepAlgo_OK

      BRepAlgo_NOK
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
    BRepAlgo_NOK: OCP.BRepAlgo.BRepAlgo_CheckStatus # value = <BRepAlgo_CheckStatus.BRepAlgo_NOK: 1>
    BRepAlgo_OK: OCP.BRepAlgo.BRepAlgo_CheckStatus # value = <BRepAlgo_CheckStatus.BRepAlgo_OK: 0>
    __entries: dict # value = {'BRepAlgo_OK': (<BRepAlgo_CheckStatus.BRepAlgo_OK: 0>, None), 'BRepAlgo_NOK': (<BRepAlgo_CheckStatus.BRepAlgo_NOK: 1>, None)}
    __members__: dict # value = {'BRepAlgo_OK': <BRepAlgo_CheckStatus.BRepAlgo_OK: 0>, 'BRepAlgo_NOK': <BRepAlgo_CheckStatus.BRepAlgo_NOK: 1>}
    pass
class BRepAlgo_Common(BRepAlgo_BooleanOperation, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions for performing a topological common operation (Boolean intersection). A Common object provides the framework for: - defining the construction of a common shape, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
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
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Perform(self,St1 : OCP.TopAbs.TopAbs_State,St2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def PerformDS(self) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first shape involved in this Boolean operation.
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second shape involved in this Boolean operation.
        """
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class BRepAlgo_Cut(BRepAlgo_BooleanOperation, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions for performing a topological cut operation (Boolean subtraction). A Cut object provides the framework for: - defining the construction of a cut shape, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
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
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Perform(self,St1 : OCP.TopAbs.TopAbs_State,St2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def PerformDS(self) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first shape involved in this Boolean operation.
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second shape involved in this Boolean operation.
        """
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class BRepAlgo_FaceRestrictor():
    """
    Builds all the faces limited with a set of non jointing and planars wires. if <ControlOrientation> is false The Wires must have correct orientations. Sinon orientation des wires de telle sorte que les faces ne soient pas infinies et qu'elles soient disjointes.
    """
    def Add(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Add the wire <W> to the set of wires.
        """
    def Clear(self) -> None: 
        """
        Removes all the Wires
        """
    def Current(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def Init(self,F : OCP.TopoDS.TopoDS_Face,Proj : bool=False,ControlOrientation : bool=False) -> None: 
        """
        the surface of <F> will be the the surface of each new faces built. <Proj> is used to update pcurves on edges if necessary. See Add().
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def Perform(self) -> None: 
        """
        Evaluate all the faces limited by the set of Wires.
        """
    def __init__(self) -> None: ...
    pass
class BRepAlgo_Fuse(BRepAlgo_BooleanOperation, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions for performing a topological fusion operation (Boolean union). A Fuse object provides the framework for: - defining the construction of a fused shape, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
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
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Perform(self,St1 : OCP.TopAbs.TopAbs_State,St2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def PerformDS(self) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first shape involved in this Boolean operation.
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second shape involved in this Boolean operation.
        """
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class BRepAlgo_Image():
    """
    Stores link between a shape <S> and a shape <NewS> obtained from <S>. <NewS> is an image of <S>.
    """
    @overload
    def Add(self,OldS : OCP.TopoDS.TopoDS_Shape,NewS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Add <NewS> to the image of <OldS>.

        Add <NewS> to the image of <OldS>.
        """
    @overload
    def Add(self,OldS : OCP.TopoDS.TopoDS_Shape,NewS : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    @overload
    def Bind(self,OldS : OCP.TopoDS.TopoDS_Shape,NewS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Links <NewS> as image of <OldS>.

        Links <NewS> as image of <OldS>.
        """
    @overload
    def Bind(self,OldS : OCP.TopoDS.TopoDS_Shape,NewS : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def Clear(self) -> None: 
        """
        None
        """
    def Compact(self) -> None: 
        """
        Keeps only the link between roots and lastimage.
        """
    def Filter(self,S : OCP.TopoDS.TopoDS_Shape,ShapeType : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        Deletes in the images the shape of type <ShapeType> which are not in <S>. Warning: Compact() must be call before.
        """
    def HasImage(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def Image(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Image of <S>. Returns <S> in the list if HasImage(S) is false.
        """
    def ImageFrom(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the generator of <S>
        """
    def IsImage(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def LastImage(self,S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Stores in <L> the images of images of...images of <S>. <L> contains only <S> if HasImage(S) is false.
        """
    def Remove(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove <S> to set of images.
        """
    def RemoveRoot(self,Root : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Removes the root <theRoot> from the list of roots and up and down maps.
        """
    def ReplaceRoot(self,OldRoot : OCP.TopoDS.TopoDS_Shape,NewRoot : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Replaces the <OldRoot> with the <NewRoot>, so all images of the <OldRoot> become the images of the <NewRoot>. The <OldRoot> is removed.
        """
    def Root(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the upper generator of <S>
        """
    def Roots(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def SetRoot(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BRepAlgo_Loop():
    """
    Builds the loops from a set of edges on a face.
    """
    def AddConstEdge(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Add <E> as const edge, E can be in the result.
        """
    def AddConstEdges(self,LE : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Add <LE> as a set of const edges.
        """
    def AddEdge(self,E : OCP.TopoDS.TopoDS_Edge,LV : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Add E with <LV>. <E> will be copied and trim by vertices in <LV>.
        """
    def CutEdge(self,E : OCP.TopoDS.TopoDS_Edge,VonE : OCP.TopTools.TopTools_ListOfShape,NE : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Cut the edge <E> in several edges <NE> on the vertices<VonE>.
        """
    def GetVerticesForSubstitute(self,VerVerMap : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        Returns the datamap of vertices with their substitutes.
        """
    def Init(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Init with <F> the set of edges must have pcurves on <F>.
        """
    def NewEdges(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of new edges built from an edge <E> it can be an empty list.
        """
    def NewFaces(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of faces. Warning: The method <WiresToFaces> as to be called before. can be an empty list.
        """
    def NewWires(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of wires performed. can be an empty list.
        """
    def Perform(self) -> None: 
        """
        Make loops.
        """
    def SetImageVV(self,theImageVV : BRepAlgo_Image) -> None: 
        """
        Sets the Image Vertex - Vertex
        """
    def UpdateVEmap(self,theVEmap : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape) -> None: 
        """
        Update VE map according to Image Vertex - Vertex
        """
    def VerticesForSubstitute(self,VerVerMap : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        None
        """
    def WiresToFaces(self) -> None: 
        """
        Build faces from the wires result.
        """
    def __init__(self) -> None: ...
    pass
class BRepAlgo_NormalProjection():
    """
    This class makes the projection of a wire on a shape.
    """
    def Add(self,ToProj : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Add an edge or a wire to the list of shape to project
        """
    def Ancestor(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Shape: 
        """
        For a resulting edge, returns the corresponding initial edge.
        """
    def Build(self) -> None: 
        """
        Builds the result as a compound.
        """
    def BuildWire(self,Liste : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        build the result as a list of wire if possible in -- a first returns a wire only if there is only a wire.
        """
    def Compute3d(self,With3d : bool=True) -> None: 
        """
        if With3d = Standard_False the 3dcurve is not computed the initial 3dcurve is kept to build the resulting edges.
        """
    def Couple(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Shape: 
        """
        For a projected edge, returns the corresponding initial face.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def IsElementary(self,C : OCP.Adaptor3d.Adaptor3d_Curve) -> bool: 
        """
        None
        """
    def Projection(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns the result
        """
    def SetDefaultParams(self) -> None: 
        """
        Set the parameters used for computation in their default values
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
        Set the parameters used for computation Tol3d is the requiered tolerance between the 3d projected curve and its 2d representation InternalContinuity is the order of constraints used for approximation. MaxDeg and MaxSeg are the maximum degree and the maximum number of segment for BSpline resulting of an approximation.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class BRepAlgo_Section(BRepAlgo_BooleanOperation, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Construction of the section lines between two shapes. For this Boolean operation, each face of the first shape is intersected by each face of the second shape. The resulting intersection edges are brought together into a compound object, but not chained or grouped into wires. Computation of the intersection of two Shapes or Surfaces The two parts involved in this Boolean operation may be defined from geometric surfaces: the most common use is the computation of the planar section of a shape. A Section object provides the framework for: - defining the shapes to be intersected, and the computation options, - implementing the construction algorithm, and - consulting the result. Example : giving two shapes S1,S2 accessing faces, let compute the section edges R on S1,S2, performing approximation on new curves, performing PCurve on part 1 but not on part 2 : Standard_Boolean PerformNow = Standard_False; BRepBoolAPI_Section S(S1,S2,PerformNow); S.ComputePCurveOn1(Standard_True); S.Approximation(Standard_True); S.Build(); TopoDS_Shape R = S.Shape(); On Null Shapes of geometries, NotDone() is called.
    """
    def Approximation(self,B : bool) -> None: 
        """
        Defines an option for computation of further intersections. This computation will be performed by the function Build in this framework. By default, the underlying 3D geometry attached to each elementary edge of the result of a computed intersection is: - analytic where possible, provided the corresponding geometry corresponds to a type of analytic curve defined in the Geom package; for example the intersection of a cylindrical shape with a plane gives an ellipse or a circle; - or elsewhere, given as a succession of points grouped together in a BSpline curve of degree 1. If Approx equals true, when further computations are performed in this framework with the function Build, these edges will have an attached 3D geometry which is a BSpline approximation of the computed set of points. Note that as a result, approximations will be computed on edges built only on new intersection lines.
        """
    def Build(self) -> None: 
        """
        Performs the computation of the section lines between the two parts defined at the time of construction of this framework or reinitialized with the Init1 and Init2 functions. The constructed shape will be returned by the function Shape. This is a compound object composed of edges. These intersection edges may be built: - on new intersection lines, or - on coincident portions of edges in the two intersected shapes. These intersection edges are independent: they are not chained or grouped into wires. If no intersection edge exists, the result is an empty compound object. The shapes involved in the construction of the section lines can be retrieved with the function Shape1 or Shape2. Note that other objects than TopoDS_Shape shapes given as arguments at the construction time of this framework, or to the Init1 or Init2 function, are converted into faces or shells before performing the computation of the intersection. Parametric 2D curves on intersection edges No parametric 2D curve (pcurve) is defined for the elementary edges of the result. To attach parametric curves like this to the constructed edges you have to use: - the function ComputePCurveOn1 to ask for the additional computation of a pcurve in the parametric space of the first shape, - the function ComputePCurveOn2 to ask for the additional computation of a pcurve in the parametric space of the second shape. This must be done before calling this function. Note that as a result, pcurves are added on edges built on new intersection lines only. Approximation of intersection edges The underlying 3D geometry attached to each elementary edge of the result is: - analytic where possible provided the corresponding geometry corresponds to a type of analytic curve defined in the Geom package; for example, the intersection of a cylindrical shape with a plane gives an ellipse or a circle; or - elsewhere, given as a succession of points grouped together in a BSpline curve of degree 1. If, on computed elementary intersection edges whose underlying geometry is not analytic, you prefer to have an attached 3D geometry which is a BSpline approximation of the computed set of points, you have to use the function Approximation to ask for this computation option before calling this function. You may also have combined these computation options: look at the example given above to illustrate the use of the constructors.
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
        """
        None
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def ComputePCurveOn1(self,B : bool) -> None: 
        """
        Indicates if the Pcurve must be (or not) performed on first part.
        """
    def ComputePCurveOn2(self,B : bool) -> None: 
        """
        Define options for the computation of further intersections which will be performed by the function Build in this framework. By default, no parametric 2D curve (pcurve) is defined for the elementary edges of the result. If ComputePCurve1 equals true, further computations performed in this framework with the function Build will attach an additional pcurve in the parametric space of the first shape to the constructed edges. If ComputePCurve2 equals true, the additional pcurve will be attached to the constructed edges in the parametric space of the second shape. These two functions may be used together. Note that as a result, pcurves will only be added onto edges built on new intersection lines.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def HasAncestorFaceOn1(self,E : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Identifies the ancestor faces of the new intersection edge E resulting from the last computation performed in this framework, that is, the faces of the two original shapes on which the edge E lies: - HasAncestorFaceOn1 gives the ancestor face in the first shape, and These functions return: - true if an ancestor face F is found, or - false if not. An ancestor face is identifiable for the edge E if the three following conditions are satisfied: - the first part on which this algorithm performed its last computation is a shape, that is, it was not given as a surface or a plane at the time of construction of this algorithm or at a later time by the Init1 function, - E is one of the elementary edges built by the last computation of this section algorithm, - the edge E is built on an intersection curve. In other words, E is a new edge built on the intersection curve, not on edges belonging to the intersecting shapes. To use these functions properly, you have to test the returned Boolean value before using the ancestor face: F is significant only if the returned Boolean value equals true.
        """
    def HasAncestorFaceOn2(self,E : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Identifies the ancestor faces of the new intersection edge E resulting from the last computation performed in this framework, that is, the faces of the two original shapes on which the edge E lies: - HasAncestorFaceOn2 gives the ancestor face in the second shape. These functions return: - true if an ancestor face F is found, or - false if not. An ancestor face is identifiable for the edge E if the three following conditions are satisfied: - the first part on which this algorithm performed its last computation is a shape, that is, it was not given as a surface or a plane at the time of construction of this algorithm or at a later time by the Init1 function, - E is one of the elementary edges built by the last computation of this section algorithm, - the edge E is built on an intersection curve. In other words, E is a new edge built on the intersection curve, not on edges belonging to the intersecting shapes. To use these functions properly, you have to test the returned Boolean value before using the ancestor face: F is significant only if the returned Boolean value equals true.
        """
    @overload
    def Init1(self,S1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes the first part

        Initializes the first part

        Initializes the first part
        """
    @overload
    def Init1(self,Sf : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def Init1(self,Pl : OCP.gp.gp_Pln) -> None: ...
    @overload
    def Init2(self,Sf : OCP.Geom.Geom_Surface) -> None: 
        """
        initialize second part

        Initializes the second part

        This and the above algorithms reinitialize the first and the second parts on which this algorithm is going to perform the intersection computation. This is done with either: the surface Sf, the plane Pl or the shape Sh. You use the function Build to construct the result.
        """
    @overload
    def Init2(self,S2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def Init2(self,Pl : OCP.gp.gp_Pln) -> None: ...
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Perform(self,St1 : OCP.TopAbs.TopAbs_State,St2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def PerformDS(self) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first shape involved in this Boolean operation.
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second shape involved in this Boolean operation.
        """
    @overload
    def __init__(self,Sf1 : OCP.Geom.Geom_Surface,Sf2 : OCP.Geom.Geom_Surface,PerformNow : bool=True) -> None: ...
    @overload
    def __init__(self,Sf : OCP.Geom.Geom_Surface,Sh : OCP.TopoDS.TopoDS_Shape,PerformNow : bool=True) -> None: ...
    @overload
    def __init__(self,Sh : OCP.TopoDS.TopoDS_Shape,Pl : OCP.gp.gp_Pln,PerformNow : bool=True) -> None: ...
    @overload
    def __init__(self,Sh : OCP.TopoDS.TopoDS_Shape,Sf : OCP.Geom.Geom_Surface,PerformNow : bool=True) -> None: ...
    @overload
    def __init__(self,Sh1 : OCP.TopoDS.TopoDS_Shape,Sh2 : OCP.TopoDS.TopoDS_Shape,PerformNow : bool=True) -> None: ...
    pass
class BRepAlgo_Tool():
    """
    None
    """
    @staticmethod
    def Deboucle3D_s(S : OCP.TopoDS.TopoDS_Shape,Boundary : OCP.TopTools.TopTools_MapOfShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Remove the non valid part of an offsetshape 1 - Remove all the free boundary and the faces connex to such edges. 2 - Remove all the shapes not valid in the result (according to the side of offseting) in this verion only the first point is implemented.
        """
    def __init__(self) -> None: ...
    pass
BRepAlgo_NOK: OCP.BRepAlgo.BRepAlgo_CheckStatus # value = <BRepAlgo_CheckStatus.BRepAlgo_NOK: 1>
BRepAlgo_OK: OCP.BRepAlgo.BRepAlgo_CheckStatus # value = <BRepAlgo_CheckStatus.BRepAlgo_OK: 0>
