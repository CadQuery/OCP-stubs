import OCP.BRepMesh
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.TCollection
import OCP.TColStd
import OCP.GeomAbs
import OCP.Poly
import OCP.Geom2d
import OCP.Bnd
import OCP.Standard
import OCP.TopoDS
import OCP.BRepAdaptor
import OCP.Geom
import OCP.NCollection
import OCP.TopLoc
import OCP.gp
__all__  = [
"BRepMesh_Circle",
"BRepMesh_CircleInspector",
"BRepMesh_CircleTool",
"BRepMesh_Classifier",
"BRepMesh_Context",
"BRepMesh_CurveTessellator",
"BRepMesh_DataStructureOfDelaun",
"BRepMesh_Deflection",
"BRepMesh_DegreeOfFreedom",
"BRepMesh_DiscretFactory",
"BRepMesh_DiscretRoot",
"BRepMesh_OrientedEdge",
"BRepMesh_EdgeDiscret",
"BRepMesh_EdgeTessellationExtractor",
"BRepMesh_FaceChecker",
"BRepMesh_FaceDiscret",
"BRepMesh_FactoryError",
"BRepMesh_FastDiscret",
"BRepMesh_GeomTool",
"BRepMesh_IncrementalMesh",
"BRepMesh_MeshAlgoFactory",
"BRepMesh_MeshTool",
"BRepMesh_ModelBuilder",
"BRepMesh_ModelHealer",
"BRepMesh_ModelPostProcessor",
"BRepMesh_ModelPreProcessor",
"BRepMesh_Edge",
"BRepMesh_PairOfIndex",
"BRepMesh_SelectorOfDataStructureOfDelaun",
"BRepMesh_ShapeTool",
"BRepMesh_ShapeVisitor",
"BRepMesh_Vertex",
"BRepMesh_VertexInspector",
"BRepMesh_VertexTool",
"HashCode",
"BRepMesh_Deleted",
"BRepMesh_FE_CANNOTCREATEALGO",
"BRepMesh_FE_FUNCTIONNOTFOUND",
"BRepMesh_FE_LIBRARYNOTFOUND",
"BRepMesh_FE_NOERROR",
"BRepMesh_Fixed",
"BRepMesh_Free",
"BRepMesh_Frontier",
"BRepMesh_InVolume",
"BRepMesh_OnCurve",
"BRepMesh_OnSurface"
]
class BRepMesh_Circle():
    """
    Describes a 2d circle with a size of only 3 Standard_Real numbers instead of gp who needs 7 Standard_Real numbers.
    """
    def Location(self) -> OCP.gp.gp_XY: 
        """
        Returns location of a circle.
        """
    def Radius(self) -> float: 
        """
        Returns radius of a circle.
        """
    def SetLocation(self,theLocation : OCP.gp.gp_XY) -> None: 
        """
        Sets location of a circle.
        """
    def SetRadius(self,theRadius : float) -> None: 
        """
        Sets radius of a circle.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLocation : OCP.gp.gp_XY,theRadius : float) -> None: ...
    pass
class BRepMesh_CircleInspector(OCP.NCollection.NCollection_CellFilter_InspectorXY):
    """
    Auxilary class to find circles shot by the given point.
    """
    def Bind(self,theIndex : int,theCircle : BRepMesh_Circle) -> None: 
        """
        Adds the circle to vector of circles at the given position.
        """
    def Circle(self,theIndex : int) -> BRepMesh_Circle: 
        """
        Returns circle with the given index.
        """
    def Circles(self) -> Any: 
        """
        Resutns vector of registered circles.
        """
    @staticmethod
    def Coord_s(i : int,thePnt : OCP.gp.gp_XY) -> float: 
        """
        Access to co-ordinate
        """
    def GetShotCircles(self) -> Any: 
        """
        Returns list of circles shot by the reference point.
        """
    def Inspect(self,theTargetIndex : int) -> OCP.NCollection.NCollection_CellFilter_Action: 
        """
        Performs inspection of a circle with the given index.
        """
    @staticmethod
    def IsEqual_s(theIndex : int,theTargetIndex : int) -> bool: 
        """
        Checks indices for equlity.
        """
    def SetPoint(self,thePoint : OCP.gp.gp_XY) -> None: 
        """
        Set reference point to be checked.
        """
    def Shift(self,thePnt : OCP.gp.gp_XY,theTol : float) -> OCP.gp.gp_XY: 
        """
        Auxiliary method to shift point by each coordinate on given value; useful for preparing a points range for Inspect with tolerance
        """
    def __init__(self,theTolerance : float,theReservedSize : int,theAllocator : OCP.NCollection.NCollection_IncAllocator) -> None: ...
    pass
class BRepMesh_CircleTool():
    """
    Create sort and destroy the circles used in triangulation.
    """
    @overload
    def Bind(self,theIndex : int,theCircle : OCP.gp.gp_Circ2d) -> None: 
        """
        Binds the circle to the tool.

        Computes circle on three points and bind it to the tool.
        """
    @overload
    def Bind(self,theIndex : int,thePoint1 : OCP.gp.gp_XY,thePoint2 : OCP.gp.gp_XY,thePoint3 : OCP.gp.gp_XY) -> bool: ...
    def Delete(self,theIndex : int) -> None: 
        """
        Deletes a circle from the tool.
        """
    def Init(self,arg1 : int) -> None: 
        """
        Initializes the tool.
        """
    def IsEmpty(self) -> bool: 
        """
        Retruns true if cell filter contains no circle.
        """
    @staticmethod
    def MakeCircle_s(thePoint1 : OCP.gp.gp_XY,thePoint2 : OCP.gp.gp_XY,thePoint3 : OCP.gp.gp_XY,theLocation : OCP.gp.gp_XY,theRadius : float) -> bool: 
        """
        Computes circle on three points.
        """
    def MocBind(self,theIndex : int) -> None: 
        """
        Binds implicit zero circle.
        """
    def Select(self,thePoint : OCP.gp.gp_XY) -> Any: 
        """
        Select the circles shot by the given point.
        """
    @overload
    def SetCellSize(self,theSizeX : float,theSizeY : float) -> None: 
        """
        Sets new size for cell filter.

        Sets new size for cell filter.
        """
    @overload
    def SetCellSize(self,theSize : float) -> None: ...
    def SetMinMaxSize(self,theMin : OCP.gp.gp_XY,theMax : OCP.gp.gp_XY) -> None: 
        """
        Sets limits of inspection area.
        """
    @overload
    def __init__(self,theReservedSize : int,theAllocator : OCP.NCollection.NCollection_IncAllocator) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_IncAllocator) -> None: ...
    pass
class BRepMesh_Classifier(OCP.Standard.Standard_Transient):
    """
    Auxilary class intended for classification of points regarding internals of discrete face.
    """
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
    def Perform(self,thePoint : OCP.gp.gp_Pnt2d) -> OCP.TopAbs.TopAbs_State: 
        """
        Performs classification of the given point regarding to face internals.
        """
    def RegisterWire(self,theWire : Any,theTolUV : Tuple[floatfloat],theRangeU : Tuple[floatfloat],theRangeV : Tuple[floatfloat]) -> None: 
        """
        Registers wire specified by sequence of points for further classification of points.
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
class BRepMesh_Context():
    """
    Class implemeting default context of BRepMesh algorithm. Initializes context by default algorithms.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
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
class BRepMesh_CurveTessellator():
    """
    Auxiliary class performing tessellation of passed edge according to specified parameters.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def PointsNb(self) -> int: 
        """
        Returns number of tessellation points.
        """
    def Value(self,theIndex : int,thePoint : OCP.gp.gp_Pnt,theParameter : float) -> bool: 
        """
        Returns parameters of solution with the given index.
        """
    @overload
    def __init__(self,theEdge : IMeshData_Edge,theParameters : IMeshTools_Parameters) -> None: ...
    @overload
    def __init__(self,theEdge : IMeshData_Edge,theOrientation : OCP.TopAbs.TopAbs_Orientation,theFace : IMeshData_Face,theParameters : IMeshTools_Parameters) -> None: ...
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
class BRepMesh_DataStructureOfDelaun(OCP.Standard.Standard_Transient):
    """
    Describes the data structure necessary for the mesh algorithms in two dimensions plane or on surface by meshing in UV space.
    """
    def AddElement(self,theElement : BRepMesh_Triangle) -> int: 
        """
        Adds element to the mesh if it is not already in the mesh.
        """
    def AddLink(self,theLink : BRepMesh_Edge) -> int: 
        """
        Adds link to the mesh if it is not already in the mesh.
        """
    def AddNode(self,theNode : BRepMesh_Vertex,isForceAdd : bool=False) -> int: 
        """
        Adds node to the mesh if it is not already in the mesh.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_IncAllocator: 
        """
        Returns memory allocator used by the structure.
        """
    def ClearDeleted(self) -> None: 
        """
        Substitutes deleted items by the last one from corresponding map to have only non-deleted elements, links or nodes in the structure.
        """
    def ClearDomain(self) -> None: 
        """
        Removes all elements.
        """
    def Data(self) -> BRepMesh_VertexTool: 
        """
        Gives the data structure for initialization of cell size and tolerance.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,theFileNameStr : str) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ElementsConnectedTo(self,theLinkIndex : int) -> BRepMesh_PairOfIndex: 
        """
        Returns indices of elements conected to the link with the given index.
        """
    def ElementsOfDomain(self) -> Any: 
        """
        Returns map of indices of elements registered in mesh.
        """
    def GetElement(self,theIndex : int) -> BRepMesh_Triangle: 
        """
        Get element by the index.
        """
    def GetLink(self,theIndex : int) -> BRepMesh_Edge: 
        """
        Get link by the index.
        """
    def GetNode(self,theIndex : int) -> BRepMesh_Vertex: 
        """
        Get node by the index.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IndexOf(self,theLink : BRepMesh_Edge) -> int: 
        """
        Finds the index of the given node.

        Finds the index of the given link.
        """
    @overload
    def IndexOf(self,theNode : BRepMesh_Vertex) -> int: ...
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
    def LinksConnectedTo(self,theIndex : int) -> Any: 
        """
        Get list of links attached to the node with the given index.
        """
    def LinksOfDomain(self) -> Any: 
        """
        Returns map of indices of links registered in mesh.
        """
    def NbElements(self) -> int: 
        """
        Returns number of links.
        """
    def NbLinks(self) -> int: 
        """
        Returns number of links.
        """
    def NbNodes(self) -> int: 
        """
        Returns number of nodes.
        """
    def RemoveElement(self,theIndex : int) -> None: 
        """
        Removes element from the mesh.
        """
    def RemoveLink(self,theIndex : int,isForce : bool=False) -> None: 
        """
        Removes link from the mesh in case if it has no connected elements and its type is Free.
        """
    def RemoveNode(self,theIndex : int,isForce : bool=False) -> None: 
        """
        Removes node from the mesh in case if it has no connected links and its type is Free.
        """
    def Statistics(self,theStream : Any) -> None: 
        """
        Dumps information about this structure.
        """
    def SubstituteElement(self,theIndex : int,theNewElement : BRepMesh_Triangle) -> bool: 
        """
        Substitutes the element with the given index by new one.
        """
    def SubstituteLink(self,theIndex : int,theNewLink : BRepMesh_Edge) -> bool: 
        """
        Substitutes the link with the given index by new one.
        """
    def SubstituteNode(self,theIndex : int,theNewNode : BRepMesh_Vertex) -> bool: 
        """
        Substitutes the node with the given index by new one.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theAllocator : OCP.NCollection.NCollection_IncAllocator,theReservedNodeSize : int=100) -> None: ...
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
class BRepMesh_Deflection(OCP.Standard.Standard_Transient):
    """
    Auxiliary tool encompassing methods to compute deflection of shapes.
    """
    @staticmethod
    def ComputeAbsoluteDeflection_s(theShape : OCP.TopoDS.TopoDS_Shape,theRelativeDeflection : float,theMaxShapeSize : float) -> float: 
        """
        Returns absolute deflection for theShape with respect to the relative deflection and theMaxShapeSize.
        """
    @staticmethod
    @overload
    def ComputeDeflection_s(theDWire : IMeshData_Wire,theParameters : IMeshTools_Parameters) -> None: 
        """
        Computes and updates deflection of the given discrete edge.

        Computes and updates deflection of the given discrete wire.

        Computes and updates deflection of the given discrete face.
        """
    @staticmethod
    @overload
    def ComputeDeflection_s(theDFace : IMeshData_Face,theParameters : IMeshTools_Parameters) -> None: ...
    @staticmethod
    @overload
    def ComputeDeflection_s(theDEdge : IMeshData_Edge,theMaxShapeSize : float,theParameters : IMeshTools_Parameters) -> None: ...
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
class BRepMesh_DegreeOfFreedom():
    """
    None

    Members:

      BRepMesh_Free

      BRepMesh_InVolume

      BRepMesh_OnSurface

      BRepMesh_OnCurve

      BRepMesh_Fixed

      BRepMesh_Frontier

      BRepMesh_Deleted
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
    BRepMesh_Deleted: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_Deleted
    BRepMesh_Fixed: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_Fixed
    BRepMesh_Free: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_Free
    BRepMesh_Frontier: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_Frontier
    BRepMesh_InVolume: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_InVolume
    BRepMesh_OnCurve: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_OnCurve
    BRepMesh_OnSurface: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_OnSurface
    __entries: dict # value = {'BRepMesh_Free': (BRepMesh_DegreeOfFreedom.BRepMesh_Free, None), 'BRepMesh_InVolume': (BRepMesh_DegreeOfFreedom.BRepMesh_InVolume, None), 'BRepMesh_OnSurface': (BRepMesh_DegreeOfFreedom.BRepMesh_OnSurface, None), 'BRepMesh_OnCurve': (BRepMesh_DegreeOfFreedom.BRepMesh_OnCurve, None), 'BRepMesh_Fixed': (BRepMesh_DegreeOfFreedom.BRepMesh_Fixed, None), 'BRepMesh_Frontier': (BRepMesh_DegreeOfFreedom.BRepMesh_Frontier, None), 'BRepMesh_Deleted': (BRepMesh_DegreeOfFreedom.BRepMesh_Deleted, None)}
    __members__: dict # value = {'BRepMesh_Free': BRepMesh_DegreeOfFreedom.BRepMesh_Free, 'BRepMesh_InVolume': BRepMesh_DegreeOfFreedom.BRepMesh_InVolume, 'BRepMesh_OnSurface': BRepMesh_DegreeOfFreedom.BRepMesh_OnSurface, 'BRepMesh_OnCurve': BRepMesh_DegreeOfFreedom.BRepMesh_OnCurve, 'BRepMesh_Fixed': BRepMesh_DegreeOfFreedom.BRepMesh_Fixed, 'BRepMesh_Frontier': BRepMesh_DegreeOfFreedom.BRepMesh_Frontier, 'BRepMesh_Deleted': BRepMesh_DegreeOfFreedom.BRepMesh_Deleted}
    pass
class BRepMesh_DiscretFactory():
    """
    This class intended to setup / retrieve default triangulation algorithm. Use BRepMesh_DiscretFactory::Get() static method to retrieve global Factory instance. Use BRepMesh_DiscretFactory::Discret() method to retrieve meshing tool.
    """
    def DefaultName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns name for current meshing algorithm.
        """
    def Discret(self,theShape : OCP.TopoDS.TopoDS_Shape,theLinDeflection : float,theAngDeflection : float) -> BRepMesh_DiscretRoot: 
        """
        Returns triangulation algorithm instance.
        """
    def ErrorStatus(self) -> BRepMesh_FactoryError: 
        """
        Returns error status for last meshing algorithm switch.
        """
    def FunctionName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns function name that should be exported by plugin.
        """
    @staticmethod
    def Get_s() -> BRepMesh_DiscretFactory: 
        """
        Returns the global factory instance.
        """
    def Names(self) -> OCP.TColStd.TColStd_MapOfAsciiString: 
        """
        Returns the list of registered meshing algorithms.
        """
    def SetDefault(self,theName : OCP.TCollection.TCollection_AsciiString,theFuncName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Setup meshing algorithm that should be created by this Factory. Returns TRUE if requested tool is available. On fail Factory will continue to use previous algo. Call ::ErrorStatus() method to retrieve fault reason.
        """
    def SetDefaultName(self,theName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Setup meshing algorithm by name. Returns TRUE if requested tool is available. On fail Factory will continue to use previous algo.
        """
    def SetFunctionName(self,theFuncName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Advanced function. Changes function name to retrieve from plugin. Returns TRUE if requested tool is available. On fail Factory will continue to use previous algo.
        """
    pass
class BRepMesh_DiscretRoot(OCP.Standard.Standard_Transient):
    """
    This is a common interface for meshing algorithms instantiated by Mesh Factory and implemented by plugins.This is a common interface for meshing algorithms instantiated by Mesh Factory and implemented by plugins.
    """
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Returns true if triangualtion was performed and has success.
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
        Compute triangulation for set shape.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set the shape to triangulate.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class BRepMesh_OrientedEdge():
    """
    Light weighted structure representing simple link.
    """
    def FirstNode(self) -> int: 
        """
        Returns index of first node of the Link.
        """
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Computes a hash code for this oriented edge, in the range [1, theUpperBound]
        """
    def IsEqual(self,theOther : BRepMesh_OrientedEdge) -> bool: 
        """
        Checks this and other edge for equality.
        """
    def LastNode(self) -> int: 
        """
        Returns index of last node of the Link.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theFirstNode : int,theLastNode : int) -> None: ...
    pass
class BRepMesh_EdgeDiscret():
    """
    Class implements functionality of edge discret tool. Performs check of the edges for existing Poly_PolygonOnTriangulation. In case if it fits specified deflection, restores data structure using it, else clears edges from outdated data.
    """
    @staticmethod
    def CreateEdgeTessellationExtractor_s(theDEdge : IMeshData_Edge,theDFace : IMeshData_Face) -> IMeshTools_CurveTessellator: 
        """
        Creates instance of tessellation extractor.
        """
    @staticmethod
    @overload
    def CreateEdgeTessellator_s(theDEdge : IMeshData_Edge,theParameters : IMeshTools_Parameters) -> IMeshTools_CurveTessellator: 
        """
        Creates instance of free edge tessellator.

        Creates instance of edge tessellator.
        """
    @staticmethod
    @overload
    def CreateEdgeTessellator_s(theDEdge : IMeshData_Edge,theOrientation : OCP.TopAbs.TopAbs_Orientation,theDFace : IMeshData_Face,theParameters : IMeshTools_Parameters) -> IMeshTools_CurveTessellator: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @staticmethod
    def Tessellate2d_s(theDEdge : IMeshData_Edge,theUpdateEnds : bool) -> None: 
        """
        Updates 2d discrete edge model using tessellation of 3D curve.
        """
    @staticmethod
    def Tessellate3d_s(theDEdge : IMeshData_Edge,theTessellator : IMeshTools_CurveTessellator,theUpdateEnds : bool) -> None: 
        """
        Updates 3d discrete edge model using the given tessellation tool.
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
class BRepMesh_EdgeTessellationExtractor():
    """
    Auxiliary class implements functionality retrieving tessellated representation of an edge stored in polygon.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def PointsNb(self) -> int: 
        """
        Returns number of tessellation points.
        """
    def Value(self,theIndex : int,thePoint : OCP.gp.gp_Pnt,theParameter : float) -> bool: 
        """
        Returns parameters of solution with the given index.
        """
    def __init__(self,theEdge : IMeshData_Edge,theFace : IMeshData_Face) -> None: ...
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
class BRepMesh_FaceChecker(OCP.Standard.Standard_Transient):
    """
    Auxiliary class checking wires of target face for self-intersections. Explodes wires of discrete face on sets of segments using tessellation data stored in model. Each segment is then checked for intersection with other ones. All collisions are registerd and returned as result of check.
    """
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
    def GetIntersectingEdges(self) -> Any: 
        """
        Returns intersecting edges.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
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
    def Perform(self) -> bool: 
        """
        Performs check wires of the face for intersections.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theFace : IMeshData_Face,theParameters : IMeshTools_Parameters) -> None: ...
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
class BRepMesh_FaceDiscret():
    """
    Class implements functionality starting triangulation of model's faces. Each face is processed separately and can be executed in parallel mode. Uses mesh algo factory passed as initializer to create instance of triangulation algorithm according to type of surface of target face.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def __init__(self,theAlgoFactory : IMeshTools_MeshAlgoFactory) -> None: ...
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
class BRepMesh_FactoryError():
    """
    None

    Members:

      BRepMesh_FE_NOERROR

      BRepMesh_FE_LIBRARYNOTFOUND

      BRepMesh_FE_FUNCTIONNOTFOUND

      BRepMesh_FE_CANNOTCREATEALGO
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
    BRepMesh_FE_CANNOTCREATEALGO: OCP.BRepMesh.BRepMesh_FactoryError # value = BRepMesh_FactoryError.BRepMesh_FE_CANNOTCREATEALGO
    BRepMesh_FE_FUNCTIONNOTFOUND: OCP.BRepMesh.BRepMesh_FactoryError # value = BRepMesh_FactoryError.BRepMesh_FE_FUNCTIONNOTFOUND
    BRepMesh_FE_LIBRARYNOTFOUND: OCP.BRepMesh.BRepMesh_FactoryError # value = BRepMesh_FactoryError.BRepMesh_FE_LIBRARYNOTFOUND
    BRepMesh_FE_NOERROR: OCP.BRepMesh.BRepMesh_FactoryError # value = BRepMesh_FactoryError.BRepMesh_FE_NOERROR
    __entries: dict # value = {'BRepMesh_FE_NOERROR': (BRepMesh_FactoryError.BRepMesh_FE_NOERROR, None), 'BRepMesh_FE_LIBRARYNOTFOUND': (BRepMesh_FactoryError.BRepMesh_FE_LIBRARYNOTFOUND, None), 'BRepMesh_FE_FUNCTIONNOTFOUND': (BRepMesh_FactoryError.BRepMesh_FE_FUNCTIONNOTFOUND, None), 'BRepMesh_FE_CANNOTCREATEALGO': (BRepMesh_FactoryError.BRepMesh_FE_CANNOTCREATEALGO, None)}
    __members__: dict # value = {'BRepMesh_FE_NOERROR': BRepMesh_FactoryError.BRepMesh_FE_NOERROR, 'BRepMesh_FE_LIBRARYNOTFOUND': BRepMesh_FactoryError.BRepMesh_FE_LIBRARYNOTFOUND, 'BRepMesh_FE_FUNCTIONNOTFOUND': BRepMesh_FactoryError.BRepMesh_FE_FUNCTIONNOTFOUND, 'BRepMesh_FE_CANNOTCREATEALGO': BRepMesh_FactoryError.BRepMesh_FE_CANNOTCREATEALGO}
    pass
class BRepMesh_FastDiscret():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class BRepMesh_GeomTool():
    """
    Tool class accumulating common geometrical functions as well as functionality using shape geometry to produce data necessary for tessellation. General aim is to calculate discretization points for the given curve or iso curve of surface according to the specified parameters.
    """
    def AddPoint(self,thePoint : OCP.gp.gp_Pnt,theParam : float,theIsReplace : bool=True) -> int: 
        """
        Adds point to already calculated points (or replaces existing).
        """
    @staticmethod
    def IntSegSeg_s(theStartPnt1 : OCP.gp.gp_XY,theEndPnt1 : OCP.gp.gp_XY,theStartPnt2 : OCP.gp.gp_XY,theEndPnt2 : OCP.gp.gp_XY,isConsiderEndPointTouch : bool,isConsiderPointOnSegment : bool,theIntPnt : OCP.gp.gp_Pnt2d) -> Any: 
        """
        Checks intersection between the two segments. Checks that intersection point lies within ranges of both segments.
        """
    def NbPoints(self) -> int: 
        """
        Returns number of discretization points.
        """
    @staticmethod
    def Normal_s(theSurface : OCP.BRepAdaptor.BRepAdaptor_HSurface,theParamU : float,theParamV : float,thePoint : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> bool: 
        """
        Computes normal to the given surface at the specified position in parametric space.
        """
    @staticmethod
    def SquareDeflectionOfSegment_s(theFirstPoint : OCP.gp.gp_Pnt,theLastPoint : OCP.gp.gp_Pnt,theMidPoint : OCP.gp.gp_Pnt) -> float: 
        """
        Compute deflection of the given segment.
        """
    @overload
    def Value(self,theIndex : int,theSurface : OCP.BRepAdaptor.BRepAdaptor_HSurface,theParam : float,thePoint : OCP.gp.gp_Pnt,theUV : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Gets parameters of discretization point with the given index.

        Gets parameters of discretization point with the given index.
        """
    @overload
    def Value(self,theIndex : int,theIsoParam : float,theParam : float,thePoint : OCP.gp.gp_Pnt,theUV : OCP.gp.gp_Pnt2d) -> bool: ...
    @overload
    def __init__(self,theSurface : OCP.BRepAdaptor.BRepAdaptor_HSurface,theIsoType : OCP.GeomAbs.GeomAbs_IsoType,theParamIso : float,theFirstParam : float,theLastParam : float,theLinDeflection : float,theAngDeflection : float,theMinPointsNb : int=2,theMinSize : float=1e-07) -> None: ...
    @overload
    def __init__(self,theCurve : OCP.BRepAdaptor.BRepAdaptor_Curve,theFirstParam : float,theLastParam : float,theLinDeflection : float,theAngDeflection : float,theMinPointsNb : int=2,theMinSize : float=1e-07) -> None: ...
    pass
class BRepMesh_IncrementalMesh(BRepMesh_DiscretRoot, OCP.Standard.Standard_Transient):
    """
    Builds the mesh of a shape with respect of their correctly triangulated parts
    """
    def ChangeParameters(self) -> IMeshTools_Parameters: 
        """
        Returns modifiable meshing parameters
        """
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
    def GetStatusFlags(self) -> int: 
        """
        Returns accumulated status flags faced during meshing.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Returns true if triangualtion was performed and has success.
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
    def IsModified(self) -> bool: 
        """
        Returns modified flag.
        """
    @staticmethod
    def IsParallelDefault_s() -> bool: 
        """
        Returns multi-threading usage flag set by default in Discret() static method (thus applied only to Mesh Factories).
        """
    def Parameters(self) -> IMeshTools_Parameters: 
        """
        Returns meshing parameters
        """
    @overload
    def Perform(self,theContext : IMeshTools_Context) -> None: 
        """
        Performs meshing ot the shape.

        Performs meshing using custom context;
        """
    @overload
    def Perform(self) -> None: ...
    @staticmethod
    def SetParallelDefault_s(isInParallel : bool) -> None: 
        """
        Setup multi-threading usage flag set by default in Discret() static method (thus applied only to Mesh Factories).
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set the shape to triangulate.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape,theParameters : IMeshTools_Parameters) -> None: ...
    @overload
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape,theLinDeflection : float,isRelative : bool=False,theAngDeflection : float=0.5,isInParallel : bool=False) -> None: ...
    @overload
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
class BRepMesh_MeshAlgoFactory():
    """
    Default implementation of IMeshTools_MeshAlgoFactory providing algorithms of different compexity depending on type of target surface.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetAlgo(self,theSurfaceType : OCP.GeomAbs.GeomAbs_SurfaceType,theParameters : IMeshTools_Parameters) -> IMeshTools_MeshAlgo: 
        """
        Creates instance of meshing algorithm for the given type of surface.
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
class BRepMesh_MeshTool(OCP.Standard.Standard_Transient):
    """
    Auxiliary tool providing API for manipulation with BRepMesh_DataStructureOfDelaun.
    """
    def AddAndLegalizeTriangle(self,thePoint1 : int,thePoint2 : int,thePoint3 : int) -> None: 
        """
        Adds new triangle with specified nodes to mesh. Legalizes triangle in case if it violates circle criteria.
        """
    def AddLink(self,theFirstNode : int,theLastNode : int) -> Tuple[int, bool]: 
        """
        Adds new link to mesh. Updates link index and link orientaion parameters.
        """
    def CleanFrontierLinks(self) -> None: 
        """
        Cleans frontier links from triangles to the right.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpTriangles(self,theFileName : str,theTriangles : Any) -> None: 
        """
        Dumps triangles to specified file.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def EraseFreeLinks(self) -> None: 
        """
        Erases all links that have no elements connected to them.

        Erases links from the specified map that have no elements connected to them.
        """
    @overload
    def EraseFreeLinks(self,theLinks : Any) -> None: ...
    def EraseItemsConnectedTo(self,theNodeIndex : int) -> None: 
        """
        Erases all elements connected to the specified artificial node. In addition, erases the artificial node itself.
        """
    def EraseTriangle(self,theTriangleIndex : int,theLoopEdges : Any) -> None: 
        """
        Erases triangle with the given index and adds the free edges into the map. When an edge is suppressed more than one time it is destroyed.
        """
    def EraseTriangles(self,theTriangles : Any,theLoopEdges : Any) -> None: 
        """
        Erases the given set of triangles. Fills map of loop edges forming the countour surrounding the erased triangles.
        """
    def GetEdgesByType(self,theEdgeType : BRepMesh_DegreeOfFreedom) -> Any: 
        """
        Gives the list of edges with type defined by input parameter.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStructure(self) -> BRepMesh_DataStructureOfDelaun: 
        """
        Returns data structure manipulated by this tool.
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
    def Legalize(self,theLinkIndex : int) -> None: 
        """
        Performs legalization of triangles connected to the specified link.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theStructure : BRepMesh_DataStructureOfDelaun) -> None: ...
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
class BRepMesh_ModelBuilder():
    """
    Class implements interface representing tool for discrete model building.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
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
class BRepMesh_ModelHealer():
    """
    Class implements functionality of model healer tool. Iterates over model's faces and checks consistency of their wires, i.e.whether wires are closed and do not contain self - intersections. In case if wire contains disconnected parts, ends of adjacent edges forming the gaps are connected in parametric space forcibly. The notion of this operation is to create correct discrete model defined relatively parametric space of target face taking into account connectivity and tolerances of 3D space only. This means that there are no specific computations are made for the sake of determination of U and V tolerance. Registers intersections on edges forming the face's shape and tries to amplify discrete represenation by decreasing of deflection for the target edge. Checks can be performed in parallel mode.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
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
class BRepMesh_ModelPostProcessor():
    """
    Class implements functionality of model post-processing tool. Stores polygons on triangulations to TopoDS_Edge.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
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
class BRepMesh_ModelPreProcessor():
    """
    Class implements functionality of model pre-processing tool. Nullifies existing polygonal data in case if model elements have IMeshData_Outdated status.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
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
class BRepMesh_Edge(BRepMesh_OrientedEdge):
    """
    Light weighted structure representing link of the mesh.
    """
    def FirstNode(self) -> int: 
        """
        Returns index of first node of the Link.
        """
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Computes a hash code for this oriented edge, in the range [1, theUpperBound]
        """
    def IsEqual(self,theOther : BRepMesh_Edge) -> bool: 
        """
        Checks for equality with another edge.
        """
    def IsSameOrientation(self,theOther : BRepMesh_Edge) -> bool: 
        """
        Checks if the given edge and this one have the same orientation.
        """
    def LastNode(self) -> int: 
        """
        Returns index of last node of the Link.
        """
    def Movability(self) -> BRepMesh_DegreeOfFreedom: 
        """
        Returns movability flag of the Link.
        """
    def SetMovability(self,theMovability : BRepMesh_DegreeOfFreedom) -> None: 
        """
        Sets movability flag of the Link.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theFirstNode : int,theLastNode : int,theMovability : BRepMesh_DegreeOfFreedom) -> None: ...
    pass
class BRepMesh_PairOfIndex():
    """
    This class represents a pair of integer indices to store element indices connected to link. It is restricted to store more than two indices in it.
    """
    def Append(self,theIndex : int) -> None: 
        """
        Appends index to the pair.
        """
    def Clear(self) -> None: 
        """
        Clears indices.
        """
    def Extent(self) -> int: 
        """
        Returns number of initialized indeces.
        """
    def FirstIndex(self) -> int: 
        """
        Returns first index of pair.
        """
    def Index(self,thePairPos : int) -> int: 
        """
        Returns index corresponding to the given position in the pair.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns is pair is empty.
        """
    def LastIndex(self) -> int: 
        """
        Returns last index of pair
        """
    def Prepend(self,theIndex : int) -> None: 
        """
        Prepends index to the pair.
        """
    def RemoveIndex(self,thePairPos : int) -> None: 
        """
        Remove index from the given position.
        """
    def SetIndex(self,thePairPos : int,theIndex : int) -> None: 
        """
        Sets index corresponding to the given position in the pair.
        """
    def __init__(self) -> None: ...
    pass
class BRepMesh_SelectorOfDataStructureOfDelaun(OCP.Standard.Standard_Transient):
    """
    Describes a selector and an iterator on a selector of components of a mesh.
    """
    def AddNeighbours(self) -> None: 
        """
        Adds a level of neighbours by edge the selector.
        """
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
    def Elements(self) -> Any: 
        """
        Returns selected elements.
        """
    def FrontierLinks(self) -> Any: 
        """
        Gives the list of incices of frontier links.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Initialize(self,theMesh : BRepMesh_DataStructureOfDelaun) -> None: 
        """
        Initializes selector by the mesh.
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
    def Links(self) -> Any: 
        """
        Returns selected links.
        """
    def NeighboursByEdgeOf(self,theElement : BRepMesh_Triangle) -> None: 
        """
        Selects all neighboring elements by links of the given element.
        """
    @overload
    def NeighboursOf(self,theNode : BRepMesh_Vertex) -> None: 
        """
        Selects all neighboring elements of the given node.

        Selects all neighboring elements of the given link.

        Selects all neighboring elements of the given element.

        Adds a level of neighbours by edge to the selector.
        """
    @overload
    def NeighboursOf(self,arg1 : BRepMesh_SelectorOfDataStructureOfDelaun) -> None: ...
    @overload
    def NeighboursOf(self,theLink : BRepMesh_Edge) -> None: ...
    @overload
    def NeighboursOf(self,theElement : BRepMesh_Triangle) -> None: ...
    def NeighboursOfElement(self,theElementIndex : int) -> None: 
        """
        Selects all neighboring elements by nodes of the given element.
        """
    def NeighboursOfLink(self,theLinkIndex : int) -> None: 
        """
        Selects all neighboring elements of link with the given index.
        """
    def NeighboursOfNode(self,theNodeIndex : int) -> None: 
        """
        Selects all neighboring elements of node with the given index.
        """
    def Nodes(self) -> Any: 
        """
        Returns selected nodes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theMesh : BRepMesh_DataStructureOfDelaun) -> None: ...
    @overload
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
class BRepMesh_ShapeTool(OCP.Standard.Standard_Transient):
    """
    Auxiliary class providing functionality to compute, retrieve and store data to TopoDS and model shape.
    """
    @staticmethod
    def AddInFace_s(theFace : OCP.TopoDS.TopoDS_Face,theTriangulation : OCP.Poly.Poly_Triangulation) -> None: 
        """
        Stores the given triangulation into the given face.
        """
    @staticmethod
    def BoxMaxDimension_s(theBox : OCP.Bnd.Bnd_Box) -> Tuple[float]: 
        """
        Gets the maximum dimension of the given bounding box. If the given bounding box is void leaves the resulting value unchanged.
        """
    @staticmethod
    def CheckAndUpdateFlags_s(theEdge : IMeshData_Edge,thePCurve : IMeshData_PCurve) -> None: 
        """
        Checks same parameter, same range and degenerativity attributes using geometrical data of the given edge and updates edge model by computed parameters in case of worst case - it can drop flags same parameter and same range to False but never to True if it is already set to False. In contrary, it can also drop degenerated flag to True, but never to False if it is already set to True.
        """
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
    @staticmethod
    def MaxFaceTolerance_s(theFace : OCP.TopoDS.TopoDS_Face) -> float: 
        """
        Returns maximum tolerance of the given face. Considers tolerances of edges and vertices contained in the given face.
        """
    @staticmethod
    @overload
    def NullifyEdge_s(theEdge : OCP.TopoDS.TopoDS_Edge,theTriangulation : OCP.Poly.Poly_Triangulation,theLocation : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Nullifies polygon on triangulation stored in the edge.

        Nullifies 3d polygon stored in the edge.
        """
    @staticmethod
    @overload
    def NullifyEdge_s(theEdge : OCP.TopoDS.TopoDS_Edge,theLocation : OCP.TopLoc.TopLoc_Location) -> None: ...
    @staticmethod
    def NullifyFace_s(theFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Nullifies triangulation stored in the face.
        """
    @staticmethod
    @overload
    def Range_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face,thePCurve : OCP.Geom2d.Geom2d_Curve,theFirstParam : float,theLastParam : float,isConsiderOrientation : bool=False) -> bool: 
        """
        Gets the parametric range of the given edge on the given face.

        Gets the 3d range of the given edge.
        """
    @staticmethod
    @overload
    def Range_s(theEdge : OCP.TopoDS.TopoDS_Edge,theCurve : OCP.Geom.Geom_Curve,theFirstParam : float,theLastParam : float,isConsiderOrientation : bool=False) -> bool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @staticmethod
    def UVPoints_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face,theFirstPoint2d : OCP.gp.gp_Pnt2d,theLastPoint2d : OCP.gp.gp_Pnt2d,isConsiderOrientation : bool=False) -> bool: 
        """
        Gets the strict UV locations of the extremities of the edge using pcurve.
        """
    @staticmethod
    @overload
    def UpdateEdge_s(theEdge : OCP.TopoDS.TopoDS_Edge,thePolygon : OCP.Poly.Poly_Polygon3D) -> None: 
        """
        Updates the given edge by the given tessellated representation.

        Updates the given edge by the given tessellated representation.

        Updates the given seam edge by the given tessellated representations.
        """
    @staticmethod
    @overload
    def UpdateEdge_s(theEdge : OCP.TopoDS.TopoDS_Edge,thePolygon1 : OCP.Poly.Poly_PolygonOnTriangulation,thePolygon2 : OCP.Poly.Poly_PolygonOnTriangulation,theTriangulation : OCP.Poly.Poly_Triangulation,theLocation : OCP.TopLoc.TopLoc_Location) -> None: ...
    @staticmethod
    @overload
    def UpdateEdge_s(theEdge : OCP.TopoDS.TopoDS_Edge,thePolygon : OCP.Poly.Poly_PolygonOnTriangulation,theTriangulation : OCP.Poly.Poly_Triangulation,theLocation : OCP.TopLoc.TopLoc_Location) -> None: ...
    @staticmethod
    def UseLocation_s(thePnt : OCP.gp.gp_Pnt,theLoc : OCP.TopLoc.TopLoc_Location) -> OCP.gp.gp_Pnt: 
        """
        Applies location to the given point and return result.
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
class BRepMesh_ShapeVisitor():
    """
    Builds discrete model of a shape by adding faces and free edges. Computes deflection for corresponded shape and checks whether it fits existing polygonal representation. If not, cleans shape from outdated info.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def Visit(self,theFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Handles TopoDS_Face object.

        Handles TopoDS_Edge object.
        """
    @overload
    def Visit(self,theEdge : OCP.TopoDS.TopoDS_Edge) -> None: ...
    def __init__(self,theModel : IMeshData_Model) -> None: ...
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
class BRepMesh_Vertex():
    """
    Light weighted structure representing vertex of the mesh in parametric space. Vertex could be associated with 3d point stored in external map.
    """
    def ChangeCoord(self) -> OCP.gp.gp_XY: 
        """
        Returns position of the vertex in parametric space for modification.
        """
    def Coord(self) -> OCP.gp.gp_XY: 
        """
        Returns position of the vertex in parametric space.
        """
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Computes a hash code for this vertex, in the range [1, theUpperBound]
        """
    def Initialize(self,theUV : OCP.gp.gp_XY,theLocation3d : int,theMovability : BRepMesh_DegreeOfFreedom) -> None: 
        """
        Initializes vertex associated with point in 3d space.
        """
    def IsEqual(self,theOther : BRepMesh_Vertex) -> bool: 
        """
        Checks for equality with another vertex.
        """
    def Location3d(self) -> int: 
        """
        Returns index of 3d point associated with the vertex.
        """
    def Movability(self) -> BRepMesh_DegreeOfFreedom: 
        """
        Returns movability of the vertex.
        """
    def SetMovability(self,theMovability : BRepMesh_DegreeOfFreedom) -> None: 
        """
        Sets movability of the vertex.
        """
    @overload
    def __init__(self,theUV : OCP.gp.gp_XY,theLocation3d : int,theMovability : BRepMesh_DegreeOfFreedom) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theU : float,theV : float,theMovability : BRepMesh_DegreeOfFreedom) -> None: ...
    pass
class BRepMesh_VertexInspector(OCP.NCollection.NCollection_CellFilter_InspectorXY):
    """
    Class intended for fast searching of the coincidence points.
    """
    def Add(self,theVertex : BRepMesh_Vertex) -> int: 
        """
        Registers the given vertex.
        """
    def ChangeVertices(self) -> Any: 
        """
        Returns set of mesh vertices for modification.
        """
    def Clear(self) -> None: 
        """
        Clear inspector's internal data structures.
        """
    @staticmethod
    def Coord_s(i : int,thePnt : OCP.gp.gp_XY) -> float: 
        """
        Access to co-ordinate
        """
    def Delete(self,theIndex : int) -> None: 
        """
        Deletes vertex with the given index.
        """
    def GetCoincidentPoint(self) -> int: 
        """
        Returns index of point coinciding with regerence one.
        """
    def GetListOfDelPoints(self) -> Any: 
        """
        Returns list with indexes of vertices that have movability attribute equal to BRepMesh_Deleted and can be replaced with another node.
        """
    def GetVertex(self,theIndex : int) -> BRepMesh_Vertex: 
        """
        Returns vertex with the given index.
        """
    def Inspect(self,theTargetIndex : int) -> OCP.NCollection.NCollection_CellFilter_Action: 
        """
        Performs inspection of a point with the given index.
        """
    @staticmethod
    def IsEqual_s(theIndex : int,theTargetIndex : int) -> bool: 
        """
        Checks indices for equlity.
        """
    def NbVertices(self) -> int: 
        """
        Returns number of registered vertices.
        """
    def SetPoint(self,thePoint : OCP.gp.gp_XY) -> None: 
        """
        Set reference point to be checked.
        """
    @overload
    def SetTolerance(self,theToleranceX : float,theToleranceY : float) -> None: 
        """
        Sets the tolerance to be used for identification of coincident vertices equal for both dimensions.

        Sets the tolerance to be used for identification of coincident vertices.
        """
    @overload
    def SetTolerance(self,theTolerance : float) -> None: ...
    def Shift(self,thePnt : OCP.gp.gp_XY,theTol : float) -> OCP.gp.gp_XY: 
        """
        Auxiliary method to shift point by each coordinate on given value; useful for preparing a points range for Inspect with tolerance
        """
    def Vertices(self) -> Any: 
        """
        Returns set of mesh vertices.
        """
    def __init__(self,theAllocator : OCP.NCollection.NCollection_IncAllocator) -> None: ...
    pass
class BRepMesh_VertexTool(OCP.Standard.Standard_Transient):
    """
    Describes data structure intended to keep mesh nodes defined in UV space and implements functionality providing their uniqueness regarding their position.
    """
    def Add(self,theVertex : BRepMesh_Vertex,isForceAdd : bool) -> int: 
        """
        Adds vertex with empty data to the tool.
        """
    def ChangeVertices(self) -> Any: 
        """
        Returns set of mesh vertices.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeleteVertex(self,theIndex : int) -> None: 
        """
        Deletes vertex with the given index from the tool.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Extent(self) -> int: 
        """
        Returns a number of vertices.
        """
    def FindIndex(self,theVertex : BRepMesh_Vertex) -> int: 
        """
        Returns index of the given vertex.
        """
    def FindKey(self,theIndex : int) -> BRepMesh_Vertex: 
        """
        Returns vertex by the given index.
        """
    def GetListOfDelNodes(self) -> Any: 
        """
        Returns the list with indexes of vertices that have movability attribute equal to BRepMesh_Deleted and can be replaced with another node.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTolerance(self) -> Tuple[float, float]: 
        """
        Gets the tolerance to be used for identification of coincident vertices.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEmpty(self) -> bool: 
        """
        Returns True when the map contains no keys.
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
    def RemoveLast(self) -> None: 
        """
        Remove last node from the structure.
        """
    @overload
    def SetCellSize(self,theSize : float) -> None: 
        """
        Sets new size of cell for cellfilter equal in both directions.

        Sets new size of cell for cellfilter.
        """
    @overload
    def SetCellSize(self,theSizeX : float,theSizeY : float) -> None: ...
    @overload
    def SetTolerance(self,theToleranceX : float,theToleranceY : float) -> None: 
        """
        Sets the tolerance to be used for identification of coincident vertices equal for both dimensions.

        Sets the tolerance to be used for identification of coincident vertices.
        """
    @overload
    def SetTolerance(self,theTolerance : float) -> None: ...
    def Statistics(self,theStream : Any) -> None: 
        """
        Prints statistics.
        """
    def Substitute(self,theIndex : int,theVertex : BRepMesh_Vertex) -> None: 
        """
        Substitutes vertex with the given by the given vertex with attributes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vertices(self) -> Any: 
        """
        Returns set of mesh vertices.
        """
    def __init__(self,theAllocator : OCP.NCollection.NCollection_IncAllocator) -> None: ...
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
@overload
def HashCode(theTriangle : BRepMesh_Triangle,theUpperBound : int) -> int:
    """
    Computes a hash code for the given oriented edge, in the range [1, theUpperBound]

    Computes a hash code for the given triangle, in the range [1, theUpperBound]

    Computes a hash code for the given vertex, in the range [1, theUpperBound]

    Computes a hash code for the given edge, in the range [1, theUpperBound]
    """
@overload
def HashCode(theEdge : BRepMesh_Edge,theUpperBound : int) -> int:
    pass
@overload
def HashCode(theOrientedEdge : BRepMesh_OrientedEdge,theUpperBound : int) -> int:
    pass
@overload
def HashCode(theVertex : BRepMesh_Vertex,theUpperBound : int) -> int:
    pass
BRepMesh_Deleted: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_Deleted
BRepMesh_FE_CANNOTCREATEALGO: OCP.BRepMesh.BRepMesh_FactoryError # value = BRepMesh_FactoryError.BRepMesh_FE_CANNOTCREATEALGO
BRepMesh_FE_FUNCTIONNOTFOUND: OCP.BRepMesh.BRepMesh_FactoryError # value = BRepMesh_FactoryError.BRepMesh_FE_FUNCTIONNOTFOUND
BRepMesh_FE_LIBRARYNOTFOUND: OCP.BRepMesh.BRepMesh_FactoryError # value = BRepMesh_FactoryError.BRepMesh_FE_LIBRARYNOTFOUND
BRepMesh_FE_NOERROR: OCP.BRepMesh.BRepMesh_FactoryError # value = BRepMesh_FactoryError.BRepMesh_FE_NOERROR
BRepMesh_Fixed: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_Fixed
BRepMesh_Free: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_Free
BRepMesh_Frontier: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_Frontier
BRepMesh_InVolume: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_InVolume
BRepMesh_OnCurve: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_OnCurve
BRepMesh_OnSurface: OCP.BRepMesh.BRepMesh_DegreeOfFreedom # value = BRepMesh_DegreeOfFreedom.BRepMesh_OnSurface
