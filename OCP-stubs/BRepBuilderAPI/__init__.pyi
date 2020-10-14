import OCP.BRepBuilderAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.Geom2d
import OCP.Bnd
import OCP.TopTools
import OCP.Standard
import OCP.TopoDS
import OCP.Geom
import OCP.NCollection
import OCP.BRepTools
import OCP.gp
__all__  = [
"BRepBuilderAPI",
"BRepBuilderAPI_BndBoxTreeSelector",
"BRepBuilderAPI_Collect",
"BRepBuilderAPI_Command",
"BRepBuilderAPI_MakeShape",
"BRepBuilderAPI_EdgeError",
"BRepBuilderAPI_FaceError",
"BRepBuilderAPI_FastSewing",
"BRepBuilderAPI_FindPlane",
"BRepBuilderAPI_ModifyShape",
"BRepBuilderAPI_MakeEdge",
"BRepBuilderAPI_MakeEdge2d",
"BRepBuilderAPI_MakeFace",
"BRepBuilderAPI_MakePolygon",
"BRepBuilderAPI_Copy",
"BRepBuilderAPI_MakeShell",
"BRepBuilderAPI_MakeSolid",
"BRepBuilderAPI_MakeVertex",
"BRepBuilderAPI_MakeWire",
"BRepBuilderAPI_GTransform",
"BRepBuilderAPI_NurbsConvert",
"BRepBuilderAPI_PipeError",
"BRepBuilderAPI_Sewing",
"BRepBuilderAPI_ShapeModification",
"BRepBuilderAPI_ShellError",
"BRepBuilderAPI_Transform",
"BRepBuilderAPI_TransitionMode",
"BRepBuilderAPI_VertexInspector",
"BRepBuilderAPI_WireError",
"VectorOfPoint",
"BRepBuilderAPI_BoundaryModified",
"BRepBuilderAPI_CurveProjectionFailed",
"BRepBuilderAPI_Deleted",
"BRepBuilderAPI_DifferentPointsOnClosedCurve",
"BRepBuilderAPI_DifferentsPointAndParameter",
"BRepBuilderAPI_DisconnectedShell",
"BRepBuilderAPI_DisconnectedWire",
"BRepBuilderAPI_EdgeDone",
"BRepBuilderAPI_EmptyShell",
"BRepBuilderAPI_EmptyWire",
"BRepBuilderAPI_FaceDone",
"BRepBuilderAPI_ImpossibleContact",
"BRepBuilderAPI_LineThroughIdenticPoints",
"BRepBuilderAPI_Merged",
"BRepBuilderAPI_NoFace",
"BRepBuilderAPI_NonManifoldWire",
"BRepBuilderAPI_NotPlanar",
"BRepBuilderAPI_ParameterOutOfRange",
"BRepBuilderAPI_ParametersOutOfRange",
"BRepBuilderAPI_PipeDone",
"BRepBuilderAPI_PipeNotDone",
"BRepBuilderAPI_PlaneNotIntersectGuide",
"BRepBuilderAPI_PointProjectionFailed",
"BRepBuilderAPI_PointWithInfiniteParameter",
"BRepBuilderAPI_Preserved",
"BRepBuilderAPI_RightCorner",
"BRepBuilderAPI_RoundCorner",
"BRepBuilderAPI_ShellDone",
"BRepBuilderAPI_ShellParametersOutOfRange",
"BRepBuilderAPI_Transformed",
"BRepBuilderAPI_Trimmed",
"BRepBuilderAPI_WireDone"
]
class BRepBuilderAPI():
    """
    The BRepBuilderAPI package provides an Application Programming Interface for the BRep topology data structure.
    """
    @staticmethod
    @overload
    def Plane_s() -> OCP.Geom.Geom_Plane: 
        """
        Sets the current plane.

        Returns the current plane.
        """
    @staticmethod
    @overload
    def Plane_s(P : OCP.Geom.Geom_Plane) -> None: ...
    @staticmethod
    @overload
    def Precision_s() -> float: 
        """
        Sets the default precision. The current Precision is returned.

        Returns the default precision.
        """
    @staticmethod
    @overload
    def Precision_s(P : float) -> None: ...
    def __init__(self) -> None: ...
    pass
class BRepBuilderAPI_BndBoxTreeSelector():
    """
    Class BRepBuilderAPI_BndBoxTreeSelector derived from UBTree::Selector This class is used to select overlapping boxes, stored in NCollection::UBTree; contains methods to maintain the selection condition and to retrieve selected objects after search.
    """
    def Accept(self,theObj : int) -> bool: 
        """
        Implementation of acceptance method This method is called when the bounding box intersect with the current. It stores the object - the index of box in the list of accepted objects.
        """
    def ClearResList(self) -> None: 
        """
        Clear the list of intersecting boxes
        """
    def Reject(self,theBox : OCP.Bnd.Bnd_Box) -> bool: 
        """
        Implementation of rejection method
        """
    def ResInd(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Get list of indexes of boxes intersecting with the current box
        """
    def SetCurrent(self,theBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        Set current box to search for overlapping with him
        """
    def __init__(self) -> None: ...
    pass
class BRepBuilderAPI_Collect():
    """
    None
    """
    def Add(self,SI : OCP.TopoDS.TopoDS_Shape,MKS : BRepBuilderAPI_MakeShape) -> None: 
        """
        None
        """
    def AddGenerated(self,S : OCP.TopoDS.TopoDS_Shape,Gen : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddModif(self,S : OCP.TopoDS.TopoDS_Shape,Mod : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Filter(self,SF : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Generated(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        None
        """
    def Modification(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BRepBuilderAPI_Command():
    """
    Root class for all commands in BRepBuilderAPI.
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
class BRepBuilderAPI_MakeShape(BRepBuilderAPI_Command):
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
    pass
class BRepBuilderAPI_EdgeError():
    """
    Indicates the outcome of the construction of an edge, i.e. whether it has been successful or not, as explained below: - BRepBuilderAPI_EdgeDone No error occurred; The edge is correctly built. - BRepBuilderAPI_PointProjectionFailed No parameters were given but the projection of the 3D points on the curve failed. This happens when the point distance to the curve is greater than the precision value. - BRepBuilderAPI_ParameterOutOfRange The given parameters are not in the parametric range C->FirstParameter(), C->LastParameter() - BRepBuilderAPI_DifferentPointsOnClosedCurve The two vertices or points are the extremities of a closed curve but have different locations. - BRepBuilderAPI_PointWithInfiniteParameter A finite coordinate point was associated with an infinite parameter (see the Precision package for a definition of infinite values). - BRepBuilderAPI_DifferentsPointAndParameter The distance between the 3D point and the point evaluated on the curve with the parameter is greater than the precision. - BRepBuilderAPI_LineThroughIdenticPoints Two identical points were given to define a line (construction of an edge without curve); gp::Resolution is used for the confusion test.

    Members:

      BRepBuilderAPI_EdgeDone

      BRepBuilderAPI_PointProjectionFailed

      BRepBuilderAPI_ParameterOutOfRange

      BRepBuilderAPI_DifferentPointsOnClosedCurve

      BRepBuilderAPI_PointWithInfiniteParameter

      BRepBuilderAPI_DifferentsPointAndParameter

      BRepBuilderAPI_LineThroughIdenticPoints
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BRepBuilderAPI_DifferentPointsOnClosedCurve: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentPointsOnClosedCurve
    BRepBuilderAPI_DifferentsPointAndParameter: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentsPointAndParameter
    BRepBuilderAPI_EdgeDone: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_EdgeDone
    BRepBuilderAPI_LineThroughIdenticPoints: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_LineThroughIdenticPoints
    BRepBuilderAPI_ParameterOutOfRange: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_ParameterOutOfRange
    BRepBuilderAPI_PointProjectionFailed: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointProjectionFailed
    BRepBuilderAPI_PointWithInfiniteParameter: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointWithInfiniteParameter
    __entries: dict # value = {'BRepBuilderAPI_EdgeDone': (BRepBuilderAPI_EdgeError.BRepBuilderAPI_EdgeDone, None), 'BRepBuilderAPI_PointProjectionFailed': (BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointProjectionFailed, None), 'BRepBuilderAPI_ParameterOutOfRange': (BRepBuilderAPI_EdgeError.BRepBuilderAPI_ParameterOutOfRange, None), 'BRepBuilderAPI_DifferentPointsOnClosedCurve': (BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentPointsOnClosedCurve, None), 'BRepBuilderAPI_PointWithInfiniteParameter': (BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointWithInfiniteParameter, None), 'BRepBuilderAPI_DifferentsPointAndParameter': (BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentsPointAndParameter, None), 'BRepBuilderAPI_LineThroughIdenticPoints': (BRepBuilderAPI_EdgeError.BRepBuilderAPI_LineThroughIdenticPoints, None)}
    __members__: dict # value = {'BRepBuilderAPI_EdgeDone': BRepBuilderAPI_EdgeError.BRepBuilderAPI_EdgeDone, 'BRepBuilderAPI_PointProjectionFailed': BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointProjectionFailed, 'BRepBuilderAPI_ParameterOutOfRange': BRepBuilderAPI_EdgeError.BRepBuilderAPI_ParameterOutOfRange, 'BRepBuilderAPI_DifferentPointsOnClosedCurve': BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentPointsOnClosedCurve, 'BRepBuilderAPI_PointWithInfiniteParameter': BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointWithInfiniteParameter, 'BRepBuilderAPI_DifferentsPointAndParameter': BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentsPointAndParameter, 'BRepBuilderAPI_LineThroughIdenticPoints': BRepBuilderAPI_EdgeError.BRepBuilderAPI_LineThroughIdenticPoints}
    pass
class BRepBuilderAPI_FaceError():
    """
    Indicates the outcome of the construction of a face, i.e. whether it has been successful or not, as explained below: - BRepBuilderAPI_FaceDone No error occurred. The face is correctly built. - BRepBuilderAPI_NoFace No initialization of the algorithm; only an empty constructor was used. - BRepBuilderAPI_NotPlanar No surface was given and the wire was not planar. - BRepBuilderAPI_CurveProjectionFailed Not used so far. - BRepBuilderAPI_ParametersOutOfRange The parameters given to limit the surface are out of its bounds.

    Members:

      BRepBuilderAPI_FaceDone

      BRepBuilderAPI_NoFace

      BRepBuilderAPI_NotPlanar

      BRepBuilderAPI_CurveProjectionFailed

      BRepBuilderAPI_ParametersOutOfRange
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BRepBuilderAPI_CurveProjectionFailed: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_CurveProjectionFailed
    BRepBuilderAPI_FaceDone: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_FaceDone
    BRepBuilderAPI_NoFace: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_NoFace
    BRepBuilderAPI_NotPlanar: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_NotPlanar
    BRepBuilderAPI_ParametersOutOfRange: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_ParametersOutOfRange
    __entries: dict # value = {'BRepBuilderAPI_FaceDone': (BRepBuilderAPI_FaceError.BRepBuilderAPI_FaceDone, None), 'BRepBuilderAPI_NoFace': (BRepBuilderAPI_FaceError.BRepBuilderAPI_NoFace, None), 'BRepBuilderAPI_NotPlanar': (BRepBuilderAPI_FaceError.BRepBuilderAPI_NotPlanar, None), 'BRepBuilderAPI_CurveProjectionFailed': (BRepBuilderAPI_FaceError.BRepBuilderAPI_CurveProjectionFailed, None), 'BRepBuilderAPI_ParametersOutOfRange': (BRepBuilderAPI_FaceError.BRepBuilderAPI_ParametersOutOfRange, None)}
    __members__: dict # value = {'BRepBuilderAPI_FaceDone': BRepBuilderAPI_FaceError.BRepBuilderAPI_FaceDone, 'BRepBuilderAPI_NoFace': BRepBuilderAPI_FaceError.BRepBuilderAPI_NoFace, 'BRepBuilderAPI_NotPlanar': BRepBuilderAPI_FaceError.BRepBuilderAPI_NotPlanar, 'BRepBuilderAPI_CurveProjectionFailed': BRepBuilderAPI_FaceError.BRepBuilderAPI_CurveProjectionFailed, 'BRepBuilderAPI_ParametersOutOfRange': BRepBuilderAPI_FaceError.BRepBuilderAPI_ParametersOutOfRange}
    pass
class BRepBuilderAPI_FastSewing(OCP.Standard.Standard_Transient):
    """
    This class performs fast sewing of surfaces (faces). It supposes that all surfaces are finite and are naturally restricted by their bounds. Moreover, it supposes that stitched together surfaces have the same parameterization along common boundaries, therefore it does not perform time-consuming check for SameParameter property of edges.This class performs fast sewing of surfaces (faces). It supposes that all surfaces are finite and are naturally restricted by their bounds. Moreover, it supposes that stitched together surfaces have the same parameterization along common boundaries, therefore it does not perform time-consuming check for SameParameter property of edges.
    """
    @overload
    def Add(self,theSurface : OCP.Geom.Geom_Surface) -> bool: 
        """
        Adds faces of a shape

        Adds a surface
        """
    @overload
    def Add(self,theShape : OCP.TopoDS.TopoDS_Shape) -> bool: ...
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
    def GetResult(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns resulted shape
        """
    def GetTolerance(self) -> float: 
        """
        Returns tolerance
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
    def Perform(self) -> None: 
        """
        Compute resulted shape
        """
    def SetTolerance(self,theToler : float) -> None: 
        """
        Sets tolerance
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theTolerance : float=1e-06) -> None: ...
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
class BRepBuilderAPI_FindPlane():
    """
    Describes functions to find the plane in which the edges of a given shape are located. A FindPlane object provides a framework for: - extracting the edges of a given shape, - implementing the construction algorithm, and - consulting the result.
    """
    def Found(self) -> bool: 
        """
        Returns true if a plane containing the edges of the shape is found and built. Use the function Plane to consult the result.
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape,Tol : float=-1.0) -> None: 
        """
        Constructs the plane containing the edges of the shape S. A plane is built only if all the edges are within a distance of less than or equal to tolerance from a planar surface. This tolerance value is equal to the larger of the following two values: - Tol, where the default value is negative, or - the largest of the tolerance values assigned to the individual edges of S. Use the function Found to verify that a plane is built. The resulting plane is then retrieved using the function Plane.
        """
    def Plane(self) -> OCP.Geom.Geom_Plane: 
        """
        Returns the plane containing the edges of the shape. Warning Use the function Found to verify that the plane is built. If a plane is not found, Plane returns a null handle.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,Tol : float=-1.0) -> None: ...
    pass
class BRepBuilderAPI_ModifyShape(BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Implements the methods of MakeShape for the constant topology modifications. The methods are implemented when the modification uses a Modifier from BRepTools. Some of them have to be redefined if the modification is implemented with another tool (see Transform from BRepBuilderAPI for example). The BRepBuilderAPI package provides the following frameworks to perform modifications of this sort: - BRepBuilderAPI_Copy to produce the copy of a shape, - BRepBuilderAPI_Transform and BRepBuilderAPI_GTransform to apply a geometric transformation to a shape, - BRepBuilderAPI_NurbsConvert to convert the whole geometry of a shape into NURBS geometry, - BRepOffsetAPI_DraftAngle to build a tapered shape.
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
    def ModifiedShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the modified shape corresponding to <S>. S can correspond to the entire initial shape or to its subshape. Exceptions Standard_NoSuchObject if S is not the initial shape or a subshape of the initial shape to which the transformation has been applied. Raises NoSuchObject from Standard if S is not the initial shape or a sub-shape of the initial shape.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    pass
class BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
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
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the constructed edge. Exceptions StdFail_NotDone if the edge is not built.
        """
    def Error(self) -> BRepBuilderAPI_EdgeError: 
        """
        Returns the construction status - BRepBuilderAPI_EdgeDone if the edge is built, or - another value of the BRepBuilderAPI_EdgeError enumeration indicating the reason of construction failure.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
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

        Defines or redefines the arguments for the construction of an edge. This function is currently used after the empty constructor BRepAPI_MakeEdge().
        """
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,p1 : float,p2 : float) -> None: ...
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the edge is built.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
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
    def __init__(self,L : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface) -> None: ...
    pass
class BRepBuilderAPI_MakeEdge2d(BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
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
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def Error(self) -> BRepBuilderAPI_EdgeError: 
        """
        Returns the error description when NotDone.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,p1 : float,p2 : float) -> None: 
        """
        None

        None

        None

        None

        None

        None
        """
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,p1 : float,p2 : float) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
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
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ2d,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Circ2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab2d,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips2d,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr2d,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab2d) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Elips2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Parab2d,p1 : float,p2 : float) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Hypr2d) -> None: ...
    @overload
    def __init__(self,L : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,p1 : float,p2 : float) -> None: ...
    pass
class BRepBuilderAPI_MakeFace(BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Provides methods to build faces.
    """
    def Add(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Adds the wire W to the constructed face as a hole. Warning W must not cross the other bounds of the face, and all the bounds must define only one area on the surface. (Be careful, however, as this is not checked.) Example // a cylinder gp_Cylinder C = ..; // a wire TopoDS_Wire W = ...; BRepBuilderAPI_MakeFace MF(C); MF.Add(W); TopoDS_Face F = MF;
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Error(self) -> BRepBuilderAPI_FaceError: 
        """
        Returns the construction status BRepBuilderAPI_FaceDone if the face is built, or - another value of the BRepBuilderAPI_FaceError enumeration indicating why the construction failed, in particular when the given parameters are outside the bounds of the surface.
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the constructed face. Exceptions StdFail_NotDone if no face is built.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    @overload
    def Init(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface,UMin : float,UMax : float,VMin : float,VMax : float,TolDegen : float) -> None: ...
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface,Bound : bool,TolDegen : float) -> None: ...
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if this algorithm has a valid face.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cone) -> None: ...
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface,TolDegen : float) -> None: ...
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface,UMin : float,UMax : float,VMin : float,VMax : float,TolDegen : float) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cone,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,W : OCP.TopoDS.TopoDS_Wire) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Torus,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,OnlyPlane : bool=False) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cone,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln,W : OCP.TopoDS.TopoDS_Wire,Inside : bool=True) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Torus) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Torus,UMin : float,UMax : float,VMin : float,VMax : float) -> None: ...
    pass
class BRepBuilderAPI_MakePolygon(BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Describes functions to build polygonal wires. A polygonal wire can be built from any number of points or vertices, and consists of a sequence of connected rectilinear edges. When a point or vertex is added to the polygon if it is identic to the previous point no edge is built. The method added can be used to test it. Construction of a Polygonal Wire You can construct: - a complete polygonal wire by defining all its points or vertices (limited to four), or - an empty polygonal wire and add its points or vertices in sequence (unlimited number). A MakePolygon object provides a framework for: - initializing the construction of a polygonal wire, - adding points or vertices to the polygonal wire under construction, and - consulting the result.
    """
    @overload
    def Add(self,V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None

        Adds the point P or the vertex V at the end of the polygonal wire under construction. A vertex is automatically created on the point P. Warning - When P or V is coincident to the previous vertex, no edge is built. The method Added can be used to test for this. Neither P nor V is checked to verify that it is coincident with another vertex than the last one, of the polygonal wire under construction. It is also possible to add vertices on a closed polygon (built for example by using a constructor which declares the polygon closed, or after the use of the Close function). Consequently, be careful using this function: you might create: - a polygonal wire with two consecutive coincident edges, or - a non manifold polygonal wire. - P or V is not checked to verify if it is coincident with another vertex but the last one, of the polygonal wire under construction. It is also possible to add vertices on a closed polygon (built for example by using a constructor which declares the polygon closed, or after the use of the Close function). Consequently, be careful when using this function: you might create: - a polygonal wire with two consecutive coincident edges, or - a non-manifold polygonal wire.
        """
    @overload
    def Add(self,P : OCP.gp.gp_Pnt) -> None: ...
    def Added(self) -> bool: 
        """
        Returns true if the last vertex added to the constructed polygonal wire is not coincident with the previous one.
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
        Closes the polygonal wire under construction. Note - this is equivalent to adding the first vertex to the polygonal wire under construction.
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge built between the last two points or vertices added to the constructed polygonal wire under construction. Warning If there is only one vertex in the polygonal wire, the result is a null edge.
        """
    def FirstVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
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
        Returns true if this algorithm contains a valid polygonal wire (i.e. if there is at least one edge). IsDone returns false if fewer than two vertices have been chained together by this construction algorithm.
        """
    def LastVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the first or the last vertex of the polygonal wire under construction. If the constructed polygonal wire is closed, the first and the last vertices are identical.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the constructed polygonal wire, or the already built part of the polygonal wire under construction. Exceptions StdFail_NotDone if the wire is not built, i.e. if fewer than two vertices have been chained together by this construction algorithm.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt,P4 : OCP.gp.gp_Pnt,Close : bool=False) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt,Close : bool=False) -> None: ...
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,V3 : OCP.TopoDS.TopoDS_Vertex,V4 : OCP.TopoDS.TopoDS_Vertex,Close : bool=False) -> None: ...
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,V3 : OCP.TopoDS.TopoDS_Vertex,Close : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepBuilderAPI_Copy(BRepBuilderAPI_ModifyShape, BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Duplication of a shape. A Copy object provides a framework for: - defining the construction of a duplicate shape, - implementing the construction algorithm, and - consulting the result.
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
    def ModifiedShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the modified shape corresponding to <S>. S can correspond to the entire initial shape or to its subshape. Exceptions Standard_NoSuchObject if S is not the initial shape or a subshape of the initial shape to which the transformation has been applied. Raises NoSuchObject from Standard if S is not the initial shape or a sub-shape of the initial shape.
        """
    def Perform(self,S : OCP.TopoDS.TopoDS_Shape,copyGeom : bool=True,copyMesh : bool=False) -> None: 
        """
        Copies the shape S. Use the function Shape to access the result. If copyMesh is True, triangulation contained in original shape will be copied along with geometry (by default, triangulation gets lost). If copyGeom is False, only topological objects will be copied, while geometry and triangulation will be shared with original shape.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,copyGeom : bool=True,copyMesh : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepBuilderAPI_MakeShell(BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Describes functions to build a shape corresponding to the skin of a surface. Note that the term shell in the class name has the same definition as that of a shell in STEP, in other words the skin of a shape, and not a solid model defined by surface and thickness. If you want to build the second sort of shell, you must use BRepOffsetAPI_MakeOffsetShape. A shell is made of a series of faces connected by their common edges. If the underlying surface of a face is not C2 continuous and the flag Segment is True, MakeShell breaks the surface down into several faces which are all C2 continuous and which are connected along the non-regular curves on the surface. The resulting shell contains all these faces. Construction of a Shell from a non-C2 continuous Surface A MakeShell object provides a framework for: - defining the construction of a shell, - implementing the construction algorithm, and - consulting the result. Warning The connected C2 faces in the shell resulting from a decomposition of the surface are not sewn. For a sewn result, you need to use BRepOffsetAPI_Sewing. For a shell with thickness, you need to use BRepOffsetAPI_MakeOffsetShape.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Error(self) -> BRepBuilderAPI_ShellError: 
        """
        Returns the construction status: - BRepBuilderAPI_ShellDone if the shell is built, or - another value of the BRepBuilderAPI_ShellError enumeration indicating why the construction failed. This is frequently BRepBuilderAPI_ShellParametersOutOfRange indicating that the given parameters are outside the bounds of the surface.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def Init(self,S : OCP.Geom.Geom_Surface,UMin : float,UMax : float,VMin : float,VMax : float,Segment : bool=False) -> None: 
        """
        Defines or redefines the arguments for the construction of a shell. The construction is initialized with the surface S, limited in the u parametric direction by the two parameter values UMin and UMax, and in the v parametric direction by the two parameter values VMin and VMax. Warning The function Error returns: - BRepBuilderAPI_ShellParametersOutOfRange when the given parameters are outside the bounds of the surface or the basis surface if S is trimmed
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the shell is built.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
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
class BRepBuilderAPI_MakeSolid(BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Describes functions to build a solid from shells. A solid is made of one shell, or a series of shells, which do not intersect each other. One of these shells constitutes the outside skin of the solid. It may be closed (a finite solid) or open (an infinite solid). Other shells form hollows (cavities) in these previous ones. Each must bound a closed volume. A MakeSolid object provides a framework for: - defining and implementing the construction of a solid, and - consulting the result.
    """
    def Add(self,S : OCP.TopoDS.TopoDS_Shell) -> None: 
        """
        Adds the shell to the current solid. Warning No check is done to verify the conditions of coherence of the resulting solid. In particular, S must not intersect other shells of the solid under construction. Besides, after all shells have been added, one of these shells should constitute the outside skin of the solid. It may be closed (a finite solid) or open (an infinite solid). Other shells form hollows (cavities) in these previous ones. Each must bound a closed volume.
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
        None
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the solid is built. For this class, a solid under construction is always valid. If no shell has been added, it could be a whole-space solid. However, no check was done to verify the conditions of coherence of the resulting solid.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the new Solid.
        """
    @overload
    def __init__(self,So : OCP.TopoDS.TopoDS_Solid,S : OCP.TopoDS.TopoDS_Shell) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_CompSolid) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shell) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shell,S2 : OCP.TopoDS.TopoDS_Shell) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shell,S2 : OCP.TopoDS.TopoDS_Shell,S3 : OCP.TopoDS.TopoDS_Shell) -> None: ...
    @overload
    def __init__(self,So : OCP.TopoDS.TopoDS_Solid) -> None: ...
    pass
class BRepBuilderAPI_MakeVertex(BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Describes functions to build BRepBuilder vertices directly from 3D geometric points. A vertex built using a MakeVertex object is only composed of a 3D point and a default precision value (Precision::Confusion()). Later on, 2D representations can be added, for example, when inserting a vertex in an edge. A MakeVertex object provides a framework for: - defining and implementing the construction of a vertex, and - consulting the result.
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
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the constructed vertex.
        """
    def __init__(self,P : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepBuilderAPI_MakeWire(BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Describes functions to build wires from edges. A wire can be built from any number of edges. To build a wire you first initialize the construction, then add edges in sequence. An unlimited number of edges can be added. The initialization of construction is done with: - no edge (an empty wire), or - edges of an existing wire, or - up to four connectable edges. In order to be added to a wire under construction, an edge (unless it is the first one) must satisfy the following condition: one of its vertices must be geometrically coincident with one of the vertices of the wire (provided that the highest tolerance factor is assigned to the two vertices). It could also be the same vertex. - The given edge is shared by the wire if it contains: - two vertices, identical to two vertices of the wire under construction (a general case of the wire closure), or - one vertex, identical to a vertex of the wire under construction; the other vertex not being geometrically coincident with another vertex of the wire. - In other cases, when one of the vertices of the edge is simply geometrically coincident with a vertex of the wire under construction (provided that the highest tolerance factor is assigned to the two vertices), the given edge is first copied and the coincident vertex is replaced in this new edge, by the coincident vertex of the wire. Note: it is possible to build non manifold wires using this construction tool. A MakeWire object provides a framework for: - initializing the construction of a wire, - adding edges to the wire under construction, and - consulting the result.
    """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Adds the edge E to the wire under construction. E must be connectable to the wire under construction, and, unless it is the first edge of the wire, must satisfy the following condition: one of its vertices must be geometrically coincident with one of the vertices of the wire (provided that the highest tolerance factor is assigned to the two vertices). It could also be the same vertex. Warning If E is not connectable to the wire under construction it is not added. The function Error will return BRepBuilderAPI_DisconnectedWire, the function IsDone will return false and the function Wire will raise an error, until a new connectable edge is added.

        Add the edges of <W> to the current wire.

        Adds the edges of <L> to the current wire. The edges are not to be consecutive. But they are to be all connected geometrically or topologically. If some of them are not connected the Status give DisconnectedWire but the "Maker" is Done() and you can get the partial result. (ie connected to the first edgeof the list <L>)
        """
    @overload
    def Add(self,W : OCP.TopoDS.TopoDS_Wire) -> None: ...
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
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the last edge added to the wire under construction. Warning - This edge can be different from the original one (the argument of the function Add, for instance,) - A null edge is returned if there are no edges in the wire under construction, or if the last edge which you tried to add was not connectable..
        """
    def Error(self) -> BRepBuilderAPI_WireError: 
        """
        Returns the construction status - BRepBuilderAPI_WireDone if the wire is built, or - another value of the BRepBuilderAPI_WireError enumeration indicating why the construction failed.
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
        Returns true if this algorithm contains a valid wire. IsDone returns false if: - there are no edges in the wire, or - the last edge which you tried to add was not connectable.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the last vertex of the last edge added to the wire under construction. Warning A null vertex is returned if there are no edges in the wire under construction, or if the last edge which you tried to add was not connectableR
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the constructed wire; or the part of the wire under construction already built. Exceptions StdFail_NotDone if a wire is not built.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,E3 : OCP.TopoDS.TopoDS_Edge,E4 : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire) -> None: ...
    @overload
    def __init__(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,E3 : OCP.TopoDS.TopoDS_Edge) -> None: ...
    pass
class BRepBuilderAPI_GTransform(BRepBuilderAPI_ModifyShape, BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Geometric transformation on a shape. The transformation to be applied is defined as a gp_GTrsf transformation. It may be: - a transformation equivalent to a gp_Trsf transformation, the most common case: you should , however, use a BRepAPI_Transform object to perform this kind of transformation; or - an affinity, or - more generally, any type of point transformation which may be defined by a three row, four column matrix of transformation. In the last two cases, the underlying geometry of the following shapes may change: - a curve which supports an edge of the shape, or - a surface which supports a face of the shape; For example, a circle may be transformed into an ellipse when applying an affinity transformation. The transformation is applied to: - all the curves which support edges of the shape, and - all the surfaces which support faces of the shape. A GTransform object provides a framework for: - defining the geometric transformation to be applied, - implementing the transformation algorithm, and - consulting the result.
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
    def ModifiedShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the modified shape corresponding to <S>.
        """
    def Perform(self,S : OCP.TopoDS.TopoDS_Shape,Copy : bool=False) -> None: 
        """
        Applies the geometric transformation defined at the time of construction of this framework to the shape S. - If the transformation T is direct and isometric (i.e. if the determinant of the vectorial part of T is equal to 1.), and if Copy equals false (default value), the resulting shape is the same as the original but with a new location assigned to it. - In all other cases, the transformation is applied to a duplicate of S. Use the function Shape to access the result. Note: this framework can be reused to apply the same geometric transformation to other shapes: just specify them by calling the function Perform again.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.gp.gp_GTrsf,Copy : bool=False) -> None: ...
    @overload
    def __init__(self,T : OCP.gp.gp_GTrsf) -> None: ...
    pass
class BRepBuilderAPI_NurbsConvert(BRepBuilderAPI_ModifyShape, BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Conversion of the complete geometry of a shape (all 3D analytical representation of surfaces and curves) into NURBS geometry (execpt for Planes). For example, all curves supporting edges of the basis shape are converted into BSpline curves, and all surfaces supporting its faces are converted into BSpline surfaces.
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
    def ModifiedShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the modified shape corresponding to <S>. S can correspond to the entire initial shape or to its subshape. Exceptions Standard_NoSuchObject if S is not the initial shape or a subshape of the initial shape to which the transformation has been applied.
        """
    def Perform(self,S : OCP.TopoDS.TopoDS_Shape,Copy : bool=False) -> None: 
        """
        Builds a new shape by converting the geometry of the shape S into NURBS geometry. Specifically, all curves supporting edges of S are converted into BSpline curves, and all surfaces supporting its faces are converted into BSpline surfaces. Use the function Shape to access the new shape. Note: this framework can be reused to convert other shapes: you specify them by calling the function Perform again.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,Copy : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepBuilderAPI_PipeError():
    """
    Errors that can occur at (shell)pipe construction.

    Members:

      BRepBuilderAPI_PipeDone

      BRepBuilderAPI_PipeNotDone

      BRepBuilderAPI_PlaneNotIntersectGuide

      BRepBuilderAPI_ImpossibleContact
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BRepBuilderAPI_ImpossibleContact: OCP.BRepBuilderAPI.BRepBuilderAPI_PipeError # value = BRepBuilderAPI_PipeError.BRepBuilderAPI_ImpossibleContact
    BRepBuilderAPI_PipeDone: OCP.BRepBuilderAPI.BRepBuilderAPI_PipeError # value = BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeDone
    BRepBuilderAPI_PipeNotDone: OCP.BRepBuilderAPI.BRepBuilderAPI_PipeError # value = BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeNotDone
    BRepBuilderAPI_PlaneNotIntersectGuide: OCP.BRepBuilderAPI.BRepBuilderAPI_PipeError # value = BRepBuilderAPI_PipeError.BRepBuilderAPI_PlaneNotIntersectGuide
    __entries: dict # value = {'BRepBuilderAPI_PipeDone': (BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeDone, None), 'BRepBuilderAPI_PipeNotDone': (BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeNotDone, None), 'BRepBuilderAPI_PlaneNotIntersectGuide': (BRepBuilderAPI_PipeError.BRepBuilderAPI_PlaneNotIntersectGuide, None), 'BRepBuilderAPI_ImpossibleContact': (BRepBuilderAPI_PipeError.BRepBuilderAPI_ImpossibleContact, None)}
    __members__: dict # value = {'BRepBuilderAPI_PipeDone': BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeDone, 'BRepBuilderAPI_PipeNotDone': BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeNotDone, 'BRepBuilderAPI_PlaneNotIntersectGuide': BRepBuilderAPI_PipeError.BRepBuilderAPI_PlaneNotIntersectGuide, 'BRepBuilderAPI_ImpossibleContact': BRepBuilderAPI_PipeError.BRepBuilderAPI_ImpossibleContact}
    pass
class BRepBuilderAPI_Sewing(OCP.Standard.Standard_Transient):
    """
    Provides methods toProvides methods toProvides methods to
    """
    def Add(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Defines the shapes to be sewed or controlled
        """
    def ContigousEdge(self,index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Gives each contigous edge
        """
    def ContigousEdgeCouple(self,index : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Gives the sections (edge) belonging to a contigous edge
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DegeneratedShape(self,index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives each degenerated shape
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeletedFace(self,index : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        Gives each deleted face
        """
    def Dump(self) -> None: 
        """
        print the informations
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FaceMode(self) -> bool: 
        """
        Returns mode for sewing faces By default - true.

        Returns mode for sewing faces By default - true.
        """
    def FloatingEdgesMode(self) -> bool: 
        """
        Returns mode for sewing floating edges By default - false.

        Returns mode for sewing floating edges By default - false.
        """
    def FreeEdge(self,index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Gives each free edge
        """
    def GetContext(self) -> OCP.BRepTools.BRepTools_ReShape: 
        """
        return context
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,tolerance : float=1e-06,option1 : bool=True,option2 : bool=True,option3 : bool=True,option4 : bool=False) -> None: 
        """
        initialize the parameters if necessary
        """
    def IsDegenerated(self,shape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Indicates if a input shape is degenerated
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
    def IsModified(self,shape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Indicates if a input shape has been modified
        """
    def IsModifiedSubShape(self,shape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Indicates if a input subshape has been modified
        """
    def IsSectionBound(self,section : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Indicates if a section is bound (before use SectionToBoundary)
        """
    def Load(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Loades the context shape.
        """
    def LocalTolerancesMode(self) -> bool: 
        """
        Returns mode for accounting of local tolerances of edges and vertices during of merging.

        Returns mode for accounting of local tolerances of edges and vertices during of merging.
        """
    def MaxTolerance(self) -> float: 
        """
        Gives set max tolerance

        Gives set max tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Gives set min tolerance.

        Gives set min tolerance.
        """
    def Modified(self,shape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives a modifieded shape
        """
    def ModifiedSubShape(self,shape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives a modifieded subshape
        """
    def MultipleEdge(self,index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Gives each multiple edge
        """
    def NbContigousEdges(self) -> int: 
        """
        Gives the number of contigous edges (edge shared by two faces)
        """
    def NbDegeneratedShapes(self) -> int: 
        """
        Gives the number of degenerated shapes
        """
    def NbDeletedFaces(self) -> int: 
        """
        Gives the number of deleted faces (faces smallest than tolerance)
        """
    def NbFreeEdges(self) -> int: 
        """
        Gives the number of free edges (edge shared by one face)
        """
    def NbMultipleEdges(self) -> int: 
        """
        Gives the number of multiple edges (edge shared by more than two faces)
        """
    def NonManifoldMode(self) -> bool: 
        """
        Gets mode for non-manifold sewing.

        Gets mode for non-manifold sewing.
        """
    def Perform(self,thePI : OCP.Message.Message_ProgressIndicator=None) -> None: 
        """
        Computing thePI - progress indicator of algorithm
        """
    def SameParameterMode(self) -> bool: 
        """
        Gets same parameter mode.

        Gets same parameter mode.
        """
    def SectionToBoundary(self,section : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Gives the original edge (free boundary) which becomes the the section. Remember that sections constitute common edges. This imformation is important for control because with original edge we can find the surface to which the section is attached.
        """
    def SetContext(self,theContext : OCP.BRepTools.BRepTools_ReShape) -> None: 
        """
        set context
        """
    def SetFaceMode(self,theFaceMode : bool) -> None: 
        """
        Sets mode for sewing faces By default - true.

        Sets mode for sewing faces By default - true.
        """
    def SetFloatingEdgesMode(self,theFloatingEdgesMode : bool) -> None: 
        """
        Sets mode for sewing floating edges By default - false. Returns mode for cutting floating edges By default - false. Sets mode for cutting floating edges By default - false.

        Sets mode for sewing floating edges By default - false. Returns mode for cutting floating edges By default - false. Sets mode for cutting floating edges By default - false.
        """
    def SetLocalTolerancesMode(self,theLocalTolerancesMode : bool) -> None: 
        """
        Sets mode for accounting of local tolerances of edges and vertices during of merging in this case WorkTolerance = myTolerance + tolEdge1+ tolEdg2;

        Sets mode for accounting of local tolerances of edges and vertices during of merging in this case WorkTolerance = myTolerance + tolEdge1+ tolEdg2;
        """
    def SetMaxTolerance(self,theMaxToler : float) -> None: 
        """
        Sets max tolerance.

        Sets max tolerance.
        """
    def SetMinTolerance(self,theMinToler : float) -> None: 
        """
        Sets min tolerance

        Sets min tolerance
        """
    def SetNonManifoldMode(self,theNonManifoldMode : bool) -> None: 
        """
        Sets mode for non-manifold sewing.

        Sets mode for non-manifold sewing.
        """
    def SetSameParameterMode(self,SameParameterMode : bool) -> None: 
        """
        Sets same parameter mode.

        Sets same parameter mode.
        """
    def SetTolerance(self,theToler : float) -> None: 
        """
        Sets tolerance

        Sets tolerance
        """
    def SewedShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the sewed shape a null shape if nothing constructed may be a face, a shell, a solid or a compound
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Tolerance(self) -> float: 
        """
        Gives set tolerance.

        Gives set tolerance.
        """
    def WhichFace(self,theEdg : OCP.TopoDS.TopoDS_Edge,index : int=1) -> OCP.TopoDS.TopoDS_Face: 
        """
        Gives a modified shape
        """
    def __init__(self,tolerance : float=1e-06,option1 : bool=True,option2 : bool=True,option3 : bool=True,option4 : bool=False) -> None: ...
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
class BRepBuilderAPI_ShapeModification():
    """
    Lists the possible types of modification to a shape following a topological operation: Preserved, Deleted, Trimmed, Merged or BoundaryModified. This enumeration enables you to assign a "state" to the different shapes that are on the list of operands for each API function. The MakeShape class then uses this to determine what has happened to the shapes which constitute the list of operands.

    Members:

      BRepBuilderAPI_Preserved

      BRepBuilderAPI_Deleted

      BRepBuilderAPI_Trimmed

      BRepBuilderAPI_Merged

      BRepBuilderAPI_BoundaryModified
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BRepBuilderAPI_BoundaryModified: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_BoundaryModified
    BRepBuilderAPI_Deleted: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Deleted
    BRepBuilderAPI_Merged: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Merged
    BRepBuilderAPI_Preserved: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Preserved
    BRepBuilderAPI_Trimmed: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Trimmed
    __entries: dict # value = {'BRepBuilderAPI_Preserved': (BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Preserved, None), 'BRepBuilderAPI_Deleted': (BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Deleted, None), 'BRepBuilderAPI_Trimmed': (BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Trimmed, None), 'BRepBuilderAPI_Merged': (BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Merged, None), 'BRepBuilderAPI_BoundaryModified': (BRepBuilderAPI_ShapeModification.BRepBuilderAPI_BoundaryModified, None)}
    __members__: dict # value = {'BRepBuilderAPI_Preserved': BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Preserved, 'BRepBuilderAPI_Deleted': BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Deleted, 'BRepBuilderAPI_Trimmed': BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Trimmed, 'BRepBuilderAPI_Merged': BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Merged, 'BRepBuilderAPI_BoundaryModified': BRepBuilderAPI_ShapeModification.BRepBuilderAPI_BoundaryModified}
    pass
class BRepBuilderAPI_ShellError():
    """
    Indicates the outcome of the construction of a face, i.e. whether it is successful or not, as explained below: - BRepBuilderAPI_ShellDone No error occurred. The shell is correctly built. - BRepBuilderAPI_EmptyShell No initialization of the algorithm: only an empty constructor was used. - BRepBuilderAPI_DisconnectedShell not yet used - BRepBuilderAPI_ShellParametersOutOfRange The parameters given to limit the surface are out of its bounds.

    Members:

      BRepBuilderAPI_ShellDone

      BRepBuilderAPI_EmptyShell

      BRepBuilderAPI_DisconnectedShell

      BRepBuilderAPI_ShellParametersOutOfRange
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BRepBuilderAPI_DisconnectedShell: OCP.BRepBuilderAPI.BRepBuilderAPI_ShellError # value = BRepBuilderAPI_ShellError.BRepBuilderAPI_DisconnectedShell
    BRepBuilderAPI_EmptyShell: OCP.BRepBuilderAPI.BRepBuilderAPI_ShellError # value = BRepBuilderAPI_ShellError.BRepBuilderAPI_EmptyShell
    BRepBuilderAPI_ShellDone: OCP.BRepBuilderAPI.BRepBuilderAPI_ShellError # value = BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellDone
    BRepBuilderAPI_ShellParametersOutOfRange: OCP.BRepBuilderAPI.BRepBuilderAPI_ShellError # value = BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellParametersOutOfRange
    __entries: dict # value = {'BRepBuilderAPI_ShellDone': (BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellDone, None), 'BRepBuilderAPI_EmptyShell': (BRepBuilderAPI_ShellError.BRepBuilderAPI_EmptyShell, None), 'BRepBuilderAPI_DisconnectedShell': (BRepBuilderAPI_ShellError.BRepBuilderAPI_DisconnectedShell, None), 'BRepBuilderAPI_ShellParametersOutOfRange': (BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellParametersOutOfRange, None)}
    __members__: dict # value = {'BRepBuilderAPI_ShellDone': BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellDone, 'BRepBuilderAPI_EmptyShell': BRepBuilderAPI_ShellError.BRepBuilderAPI_EmptyShell, 'BRepBuilderAPI_DisconnectedShell': BRepBuilderAPI_ShellError.BRepBuilderAPI_DisconnectedShell, 'BRepBuilderAPI_ShellParametersOutOfRange': BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellParametersOutOfRange}
    pass
class BRepBuilderAPI_Transform(BRepBuilderAPI_ModifyShape, BRepBuilderAPI_MakeShape, BRepBuilderAPI_Command):
    """
    Geometric transformation on a shape. The transformation to be applied is defined as a gp_Trsf transformation, i.e. a transformation which does not modify the underlying geometry of shapes. The transformation is applied to: - all curves which support edges of a shape, and - all surfaces which support its faces. A Transform object provides a framework for: - defining the geometric transformation to be applied, - implementing the transformation algorithm, and - consulting the results.
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
    def ModifiedShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the modified shape corresponding to <S>.
        """
    def Perform(self,S : OCP.TopoDS.TopoDS_Shape,Copy : bool=False) -> None: 
        """
        pplies the geometric transformation defined at the time of construction of this framework to the shape S. - If the transformation T is direct and isometric, in other words, if the determinant of the vectorial part of T is equal to 1., and if Copy equals false (the default value), the resulting shape is the same as the original but with a new location assigned to it. - In all other cases, the transformation is applied to a duplicate of S. Use the function Shape to access the result. Note: this framework can be reused to apply the same geometric transformation to other shapes. You only need to specify them by calling the function Perform again.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,T : OCP.gp.gp_Trsf) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.gp.gp_Trsf,Copy : bool=False) -> None: ...
    pass
class BRepBuilderAPI_TransitionMode():
    """
    Option to manage discontinuities in Sweep

    Members:

      BRepBuilderAPI_Transformed

      BRepBuilderAPI_RightCorner

      BRepBuilderAPI_RoundCorner
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BRepBuilderAPI_RightCorner: OCP.BRepBuilderAPI.BRepBuilderAPI_TransitionMode # value = BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RightCorner
    BRepBuilderAPI_RoundCorner: OCP.BRepBuilderAPI.BRepBuilderAPI_TransitionMode # value = BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RoundCorner
    BRepBuilderAPI_Transformed: OCP.BRepBuilderAPI.BRepBuilderAPI_TransitionMode # value = BRepBuilderAPI_TransitionMode.BRepBuilderAPI_Transformed
    __entries: dict # value = {'BRepBuilderAPI_Transformed': (BRepBuilderAPI_TransitionMode.BRepBuilderAPI_Transformed, None), 'BRepBuilderAPI_RightCorner': (BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RightCorner, None), 'BRepBuilderAPI_RoundCorner': (BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RoundCorner, None)}
    __members__: dict # value = {'BRepBuilderAPI_Transformed': BRepBuilderAPI_TransitionMode.BRepBuilderAPI_Transformed, 'BRepBuilderAPI_RightCorner': BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RightCorner, 'BRepBuilderAPI_RoundCorner': BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RoundCorner}
    pass
class BRepBuilderAPI_VertexInspector(OCP.NCollection.NCollection_CellFilter_InspectorXYZ):
    """
    Class BRepBuilderAPI_VertexInspector derived from NCollection_CellFilter_InspectorXYZ This class define the Inspector interface for CellFilter algorithm, working with gp_XYZ points in 3d space. Used in search of coincidence points with a certain tolerance.
    """
    def Add(self,thePnt : OCP.gp.gp_XYZ) -> None: 
        """
        Keep the points used for comparison
        """
    def ClearResList(self) -> None: 
        """
        Clear the list of adjacent points
        """
    @staticmethod
    def Coord_s(i : int,thePnt : OCP.gp.gp_XYZ) -> float: 
        """
        Access to co-ordinate
        """
    def Inspect(self,theTarget : int) -> OCP.NCollection.NCollection_CellFilter_Action: 
        """
        Implementation of inspection method
        """
    def ResInd(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Get list of indexes of points adjacent with the current
        """
    def SetCurrent(self,theCurPnt : OCP.gp.gp_XYZ) -> None: 
        """
        Set current point to search for coincidence
        """
    def Shift(self,thePnt : OCP.gp.gp_XYZ,theTol : float) -> OCP.gp.gp_XYZ: 
        """
        Auxiliary method to shift point by each coordinate on given value; useful for preparing a points range for Inspect with tolerance
        """
    def __init__(self,theTol : float) -> None: ...
    pass
class BRepBuilderAPI_WireError():
    """
    Indicates the outcome of wire construction, i.e. whether it is successful or not, as explained below: - BRepBuilderAPI_WireDone No error occurred. The wire is correctly built. - BRepBuilderAPI_EmptyWire No initialization of the algorithm. Only an empty constructor was used. - BRepBuilderAPI_DisconnectedWire The last edge which you attempted to add was not connected to the wire. - BRepBuilderAPI_NonManifoldWire The wire with some singularity.

    Members:

      BRepBuilderAPI_WireDone

      BRepBuilderAPI_EmptyWire

      BRepBuilderAPI_DisconnectedWire

      BRepBuilderAPI_NonManifoldWire
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BRepBuilderAPI_DisconnectedWire: OCP.BRepBuilderAPI.BRepBuilderAPI_WireError # value = BRepBuilderAPI_WireError.BRepBuilderAPI_DisconnectedWire
    BRepBuilderAPI_EmptyWire: OCP.BRepBuilderAPI.BRepBuilderAPI_WireError # value = BRepBuilderAPI_WireError.BRepBuilderAPI_EmptyWire
    BRepBuilderAPI_NonManifoldWire: OCP.BRepBuilderAPI.BRepBuilderAPI_WireError # value = BRepBuilderAPI_WireError.BRepBuilderAPI_NonManifoldWire
    BRepBuilderAPI_WireDone: OCP.BRepBuilderAPI.BRepBuilderAPI_WireError # value = BRepBuilderAPI_WireError.BRepBuilderAPI_WireDone
    __entries: dict # value = {'BRepBuilderAPI_WireDone': (BRepBuilderAPI_WireError.BRepBuilderAPI_WireDone, None), 'BRepBuilderAPI_EmptyWire': (BRepBuilderAPI_WireError.BRepBuilderAPI_EmptyWire, None), 'BRepBuilderAPI_DisconnectedWire': (BRepBuilderAPI_WireError.BRepBuilderAPI_DisconnectedWire, None), 'BRepBuilderAPI_NonManifoldWire': (BRepBuilderAPI_WireError.BRepBuilderAPI_NonManifoldWire, None)}
    __members__: dict # value = {'BRepBuilderAPI_WireDone': BRepBuilderAPI_WireError.BRepBuilderAPI_WireDone, 'BRepBuilderAPI_EmptyWire': BRepBuilderAPI_WireError.BRepBuilderAPI_EmptyWire, 'BRepBuilderAPI_DisconnectedWire': BRepBuilderAPI_WireError.BRepBuilderAPI_DisconnectedWire, 'BRepBuilderAPI_NonManifoldWire': BRepBuilderAPI_WireError.BRepBuilderAPI_NonManifoldWire}
    pass
class VectorOfPoint(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        Append
        """
    def Appended(self) -> OCP.gp.gp_XYZ: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : VectorOfPoint,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> OCP.gp.gp_XYZ: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.gp.gp_XYZ: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> OCP.gp.gp_XYZ: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.gp.gp_XYZ: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    @overload
    def __init__(self,theOther : VectorOfPoint) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
BRepBuilderAPI_BoundaryModified: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_BoundaryModified
BRepBuilderAPI_CurveProjectionFailed: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_CurveProjectionFailed
BRepBuilderAPI_Deleted: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Deleted
BRepBuilderAPI_DifferentPointsOnClosedCurve: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentPointsOnClosedCurve
BRepBuilderAPI_DifferentsPointAndParameter: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentsPointAndParameter
BRepBuilderAPI_DisconnectedShell: OCP.BRepBuilderAPI.BRepBuilderAPI_ShellError # value = BRepBuilderAPI_ShellError.BRepBuilderAPI_DisconnectedShell
BRepBuilderAPI_DisconnectedWire: OCP.BRepBuilderAPI.BRepBuilderAPI_WireError # value = BRepBuilderAPI_WireError.BRepBuilderAPI_DisconnectedWire
BRepBuilderAPI_EdgeDone: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_EdgeDone
BRepBuilderAPI_EmptyShell: OCP.BRepBuilderAPI.BRepBuilderAPI_ShellError # value = BRepBuilderAPI_ShellError.BRepBuilderAPI_EmptyShell
BRepBuilderAPI_EmptyWire: OCP.BRepBuilderAPI.BRepBuilderAPI_WireError # value = BRepBuilderAPI_WireError.BRepBuilderAPI_EmptyWire
BRepBuilderAPI_FaceDone: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_FaceDone
BRepBuilderAPI_ImpossibleContact: OCP.BRepBuilderAPI.BRepBuilderAPI_PipeError # value = BRepBuilderAPI_PipeError.BRepBuilderAPI_ImpossibleContact
BRepBuilderAPI_LineThroughIdenticPoints: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_LineThroughIdenticPoints
BRepBuilderAPI_Merged: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Merged
BRepBuilderAPI_NoFace: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_NoFace
BRepBuilderAPI_NonManifoldWire: OCP.BRepBuilderAPI.BRepBuilderAPI_WireError # value = BRepBuilderAPI_WireError.BRepBuilderAPI_NonManifoldWire
BRepBuilderAPI_NotPlanar: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_NotPlanar
BRepBuilderAPI_ParameterOutOfRange: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_ParameterOutOfRange
BRepBuilderAPI_ParametersOutOfRange: OCP.BRepBuilderAPI.BRepBuilderAPI_FaceError # value = BRepBuilderAPI_FaceError.BRepBuilderAPI_ParametersOutOfRange
BRepBuilderAPI_PipeDone: OCP.BRepBuilderAPI.BRepBuilderAPI_PipeError # value = BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeDone
BRepBuilderAPI_PipeNotDone: OCP.BRepBuilderAPI.BRepBuilderAPI_PipeError # value = BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeNotDone
BRepBuilderAPI_PlaneNotIntersectGuide: OCP.BRepBuilderAPI.BRepBuilderAPI_PipeError # value = BRepBuilderAPI_PipeError.BRepBuilderAPI_PlaneNotIntersectGuide
BRepBuilderAPI_PointProjectionFailed: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointProjectionFailed
BRepBuilderAPI_PointWithInfiniteParameter: OCP.BRepBuilderAPI.BRepBuilderAPI_EdgeError # value = BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointWithInfiniteParameter
BRepBuilderAPI_Preserved: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Preserved
BRepBuilderAPI_RightCorner: OCP.BRepBuilderAPI.BRepBuilderAPI_TransitionMode # value = BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RightCorner
BRepBuilderAPI_RoundCorner: OCP.BRepBuilderAPI.BRepBuilderAPI_TransitionMode # value = BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RoundCorner
BRepBuilderAPI_ShellDone: OCP.BRepBuilderAPI.BRepBuilderAPI_ShellError # value = BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellDone
BRepBuilderAPI_ShellParametersOutOfRange: OCP.BRepBuilderAPI.BRepBuilderAPI_ShellError # value = BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellParametersOutOfRange
BRepBuilderAPI_Transformed: OCP.BRepBuilderAPI.BRepBuilderAPI_TransitionMode # value = BRepBuilderAPI_TransitionMode.BRepBuilderAPI_Transformed
BRepBuilderAPI_Trimmed: OCP.BRepBuilderAPI.BRepBuilderAPI_ShapeModification # value = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Trimmed
BRepBuilderAPI_WireDone: OCP.BRepBuilderAPI.BRepBuilderAPI_WireError # value = BRepBuilderAPI_WireError.BRepBuilderAPI_WireDone
