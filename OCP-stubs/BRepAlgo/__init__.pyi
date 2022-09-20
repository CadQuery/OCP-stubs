import OCP.BRepAlgo
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.TopTools
import OCP.GeomAbs
import OCP.TopAbs
import OCP.Standard
import OCP.TopoDS
__all__  = [
"BRepAlgo",
"BRepAlgo_AsDes",
"BRepAlgo_FaceRestrictor",
"BRepAlgo_Image",
"BRepAlgo_Loop",
"BRepAlgo_NormalProjection"
]
class BRepAlgo():
    """
    The BRepAlgo class provides the following tools for: - Checking validity of the shape; - Concatenation of the edges of the wire.
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
        Checks if the shape is "correct". If not, returns FALSE, else returns TRUE. This method differs from the previous one in the fact that no geometric controls (intersection of wires, pcurve validity) are performed.
        """
    @staticmethod
    @overload
    def IsValid_s(theArgs : OCP.TopTools.TopTools_ListOfShape,theResult : OCP.TopoDS.TopoDS_Shape,closedSolid : bool=False,GeomCtrl : bool=True) -> bool: 
        """
        Checks if the shape is "correct". If not, returns <Standard_False>, else returns <Standard_True>.

        Checks if the Generated and Modified Faces from the shapes <arguments> in the shape <result> are "correct". The args may be empty, then all faces will be checked. If <Closed> is True, only closed shape are valid. If <GeomCtrl> is False the geometry of new vertices and edges are not verified and the auto-intersection of new wires are not searched.
        """
    @staticmethod
    @overload
    def IsValid_s(S : OCP.TopoDS.TopoDS_Shape) -> bool: ...
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
    def Remove(self,theS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove theS from me.
        """
    def Replace(self,theOldS : OCP.TopoDS.TopoDS_Shape,theNewS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Replace theOldS by theNewS. theOldS disappear from this.
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
        the surface of <F> will be the surface of each new faces built. <Proj> is used to update pcurves on edges if necessary. See Add().
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
        Set the parameters used for computation Tol3d is the required tolerance between the 3d projected curve and its 2d representation InternalContinuity is the order of constraints used for approximation. MaxDeg and MaxSeg are the maximum degree and the maximum number of segment for BSpline resulting of an approximation.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
