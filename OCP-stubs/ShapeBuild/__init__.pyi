import OCP.ShapeBuild
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.BRepTools
import OCP.Geom
import OCP.TopoDS
import OCP.TopLoc
import OCP.Geom2d
import OCP.ShapeExtend
import OCP.Standard
import OCP.TopAbs
__all__  = [
"ShapeBuild",
"ShapeBuild_Edge",
"ShapeBuild_ReShape",
"ShapeBuild_Vertex"
]
class ShapeBuild():
    """
    This package provides basic building tools for other packages in ShapeHealing. These tools are rather internal for ShapeHealing .
    """
    @staticmethod
    def PlaneXOY_s() -> OCP.Geom.Geom_Plane: 
        """
        Rebuilds a shape with substitution of some components Returns a Geom_Surface which is the Plane XOY (Z positive) This allows to consider an UV space homologous to a 3D space, with this support surface
        """
    def __init__(self) -> None: ...
    pass
class ShapeBuild_Edge():
    """
    This class provides low-level operators for building an edge 3d curve, copying edge with replaced vertices etc.
    """
    def BuildCurve3d(self,edge : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Calls BRepTools::BuildCurve3D
        """
    def Copy(self,edge : OCP.TopoDS.TopoDS_Edge,sharepcurves : bool=True) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Make a copy of <edge> by call to CopyReplaceVertices() (i.e. construct new TEdge with the same pcurves and vertices). If <sharepcurves> is False, pcurves are also replaced by their copies with help of method CopyPCurves
        """
    def CopyPCurves(self,toedge : OCP.TopoDS.TopoDS_Edge,fromedge : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Makes a copy of pcurves from edge <fromedge> into edge <toedge>. Pcurves which are already present in <toedge>, are replaced by copies, other are copied. Ranges are also copied.
        """
    def CopyRanges(self,toedge : OCP.TopoDS.TopoDS_Edge,fromedge : OCP.TopoDS.TopoDS_Edge,alpha : float=0.0,beta : float=1.0) -> None: 
        """
        Copies ranges for curve3d and all common pcurves from edge <fromedge> into edge <toedge>.
        """
    def CopyReplaceVertices(self,edge : OCP.TopoDS.TopoDS_Edge,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Copy edge and replace one or both its vertices to a given one(s). Vertex V1 replaces FORWARD vertex, and V2 - REVERSED, as they are found by TopoDS_Iterator. If V1 or V2 is NULL, the original vertex is taken
        """
    @overload
    def MakeEdge(self,edge : OCP.TopoDS.TopoDS_Edge,curve : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Makes edge with curve and location

        Makes edge with curve, location and range [p1, p2]

        Makes edge with pcurve and face

        Makes edge with pcurve, face and range [p1, p2]

        Makes edge with pcurve, surface and location

        Makes edge with pcurve, surface, location and range [p1, p2]
        """
    @overload
    def MakeEdge(self,edge : OCP.TopoDS.TopoDS_Edge,pcurve : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,p1 : float,p2 : float) -> None: ...
    @overload
    def MakeEdge(self,edge : OCP.TopoDS.TopoDS_Edge,pcurve : OCP.Geom2d.Geom2d_Curve,face : OCP.TopoDS.TopoDS_Face,p1 : float,p2 : float) -> None: ...
    @overload
    def MakeEdge(self,edge : OCP.TopoDS.TopoDS_Edge,curve : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,p1 : float,p2 : float) -> None: ...
    @overload
    def MakeEdge(self,edge : OCP.TopoDS.TopoDS_Edge,pcurve : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> None: ...
    @overload
    def MakeEdge(self,edge : OCP.TopoDS.TopoDS_Edge,pcurve : OCP.Geom2d.Geom2d_Curve,face : OCP.TopoDS.TopoDS_Face) -> None: ...
    def ReassignPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,old : OCP.TopoDS.TopoDS_Face,sub : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Reassign edge pcurve lying on face <old> to another face . If edge has two pcurves on <old> face, only one of them will be reassigned, and other will left alone. Similarly, if edge already had a pcurve on face , it will have two pcurves on it. Returns True if succeeded, False if no pcurve lying on <old> found.
        """
    def RemoveCurve3d(self,edge : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Removes the Curve3D recorded in an Edge
        """
    @overload
    def RemovePCurve(self,edge : OCP.TopoDS.TopoDS_Edge,surf : OCP.Geom.Geom_Surface) -> None: 
        """
        Removes the PCurve(s) which could be recorded in an Edge for the given Face

        Removes the PCurve(s) which could be recorded in an Edge for the given Surface

        Removes the PCurve(s) which could be recorded in an Edge for the given Surface, with given Location
        """
    @overload
    def RemovePCurve(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def RemovePCurve(self,edge : OCP.TopoDS.TopoDS_Edge,surf : OCP.Geom.Geom_Surface,loc : OCP.TopLoc.TopLoc_Location) -> None: ...
    def ReplacePCurve(self,edge : OCP.TopoDS.TopoDS_Edge,pcurve : OCP.Geom2d.Geom2d_Curve,face : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Replace the PCurve in an Edge for the given Face In case if edge is seam, i.e. has 2 pcurves on that face, only pcurve corresponding to the orientation of the edge is replaced
        """
    def SetRange3d(self,edge : OCP.TopoDS.TopoDS_Edge,first : float,last : float) -> None: 
        """
        Sets range on 3d curve only.
        """
    def TransformPCurve(self,pcurve : OCP.Geom2d.Geom2d_Curve,trans : OCP.gp.gp_Trsf2d,uFact : float,aFirst : float,aLast : float) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Transforms the PCurve with given matrix and affinity U factor.
        """
    def __init__(self) -> None: ...
    pass
class ShapeBuild_ReShape(OCP.BRepTools.BRepTools_ReShape, OCP.Standard.Standard_Transient):
    """
    Rebuilds a Shape by making pre-defined substitutions on some of its componentsRebuilds a Shape by making pre-defined substitutions on some of its componentsRebuilds a Shape by making pre-defined substitutions on some of its components
    """
    @overload
    def Apply(self,shape : OCP.TopoDS.TopoDS_Shape,until : OCP.TopAbs.TopAbs_ShapeEnum,buildmode : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Applies the substitutions requests to a shape

        Applies the substitutions requests to a shape.
        """
    @overload
    def Apply(self,shape : OCP.TopoDS.TopoDS_Shape,until : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> OCP.TopoDS.TopoDS_Shape: ...
    def Clear(self) -> None: 
        """
        Clears all substitutions requests
        """
    @overload
    def CopyVertex(self,theV : OCP.TopoDS.TopoDS_Vertex,theTol : float=-1.0) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None

        None
        """
    @overload
    def CopyVertex(self,theV : OCP.TopoDS.TopoDS_Vertex,theNewPos : OCP.gp.gp_Pnt,aTol : float) -> OCP.TopoDS.TopoDS_Vertex: ...
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        Returns the history of the substituted shapes.
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
    def IsNewShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsRecorded(self,shape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Tells if a shape is recorded for Replace/Remove
        """
    def Remove(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets a request to Remove a Shape whatever the orientation
        """
    def Replace(self,shape : OCP.TopoDS.TopoDS_Shape,newshape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets a request to Replace a Shape by a new one.
        """
    @overload
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns a complete substitution status for a shape 0 : not recorded, <newsh> = original <shape> < 0: to be removed, <newsh> is NULL > 0: to be replaced, <newsh> is a new item If <last> is False, returns status and new shape recorded in the map directly for the shape, if True and status > 0 then recursively searches for the last status and new shape.

        Queries the status of last call to Apply(shape,enum) OK : no (sub)shapes replaced or removed DONE1: source (starting) shape replaced DONE2: source (starting) shape removed DONE3: some subshapes replaced DONE4: some subshapes removed FAIL1: some replacements not done because of bad type of subshape
        """
    @overload
    def Status(self,shape : OCP.TopoDS.TopoDS_Shape,newsh : OCP.TopoDS.TopoDS_Shape,last : bool=False) -> int: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,shape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the new value for an individual shape If not recorded, returns the original shape itself If to be Removed, returns a Null Shape Else, returns the replacing item
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
    @property
    def ModeConsiderLocation(self) -> bool:
        """
        :type: bool
        """
    @ModeConsiderLocation.setter
    def ModeConsiderLocation(self, arg1: bool) -> None:
        pass
    pass
class ShapeBuild_Vertex():
    """
    Provides low-level functions used for constructing vertices
    """
    @overload
    def CombineVertex(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,tolFactor : float=1.0001) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Combines new vertex from two others. This new one is the smallest vertex which comprises both of the source vertices. The function takes into account the positions and tolerances of the source vertices. The tolerance of the new vertex will be equal to the minimal tolerance that is required to comprise source vertices multiplied by tolFactor (in order to avoid errors because of discreteness of calculations).

        The same function as above, except that it accepts two points and two tolerances instead of vertices
        """
    @overload
    def CombineVertex(self,pnt1 : OCP.gp.gp_Pnt,pnt2 : OCP.gp.gp_Pnt,tol1 : float,tol2 : float,tolFactor : float=1.0001) -> OCP.TopoDS.TopoDS_Vertex: ...
    def __init__(self) -> None: ...
    pass
