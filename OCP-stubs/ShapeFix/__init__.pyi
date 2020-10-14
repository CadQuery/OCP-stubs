import OCP.ShapeFix
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.ShapeExtend
import OCP.Geom2d
import OCP.ShapeAnalysis
import OCP.Message
import OCP.Bnd
import OCP.TopTools
import OCP.TopLoc
import OCP.Standard
import OCP.TopoDS
import OCP.Geom
import OCP.NCollection
import OCP.ShapeBuild
import OCP.ShapeConstruct
__all__  = [
"ShapeFix",
"ShapeFix_Root",
"ShapeFix_DataMapOfShapeBox2d",
"ShapeFix_Edge",
"ShapeFix_EdgeConnect",
"ShapeFix_EdgeProjAux",
"ShapeFix_Face",
"ShapeFix_FaceConnect",
"ShapeFix_FixSmallFace",
"ShapeFix_FixSmallSolid",
"ShapeFix_FreeBounds",
"ShapeFix_IntersectionTool",
"ShapeFix_ComposeShell",
"ShapeFix_SequenceOfWireSegment",
"ShapeFix_Shape",
"ShapeFix_ShapeTolerance",
"ShapeFix_Shell",
"ShapeFix_Solid",
"ShapeFix_SplitCommonVertex",
"ShapeFix_SplitTool",
"ShapeFix_Wire",
"ShapeFix_WireSegment",
"ShapeFix_WireVertex",
"ShapeFix_Wireframe"
]
class ShapeFix():
    """
    This package provides algorithms for fixing problematic (violating Open CASCADE requirements) shapes. Tools from package ShapeAnalysis are used for detecting the problems. The detecting and fixing is done taking in account various criteria implemented in BRepCheck package. Each class of package ShapeFix deals with one certain type of shapes or with some family of problems.
    """
    @staticmethod
    def EncodeRegularity_s(shape : OCP.TopoDS.TopoDS_Shape,tolang : float=1e-10) -> None: 
        """
        Runs EncodeRegularity from BRepLib taking into account shared components of assemblies, so that each component is processed only once
        """
    @staticmethod
    def FixVertexPosition_s(theshape : OCP.TopoDS.TopoDS_Shape,theTolerance : float,thecontext : OCP.ShapeBuild.ShapeBuild_ReShape) -> bool: 
        """
        Fix position of the vertices having tolerance more tnan specified one.;
        """
    @staticmethod
    def LeastEdgeSize_s(theshape : OCP.TopoDS.TopoDS_Shape) -> float: 
        """
        Calculate size of least edge;
        """
    @staticmethod
    def RemoveSmallEdges_s(shape : OCP.TopoDS.TopoDS_Shape,Tolerance : float,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Removes edges which are less than given tolerance from shape with help of ShapeFix_Wire::FixSmall()
        """
    @staticmethod
    def SameParameter_s(shape : OCP.TopoDS.TopoDS_Shape,enforce : bool,preci : float=0.0,theProgress : OCP.Message.Message_ProgressIndicator=None,theMsgReg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator=None) -> bool: 
        """
        Runs SameParameter from BRepLib with these adaptations : <enforce> forces computations, else they are made only on Edges with flag SameParameter false <preci>, if not precised, is taken for each EDge as its own Tolerance Returns True when done, False if an exception has been raised In case of exception anyway, as many edges as possible have been processed. The passed progress indicator allows user to consult the current progress stage and abort algorithm if needed.
        """
    def __init__(self) -> None: ...
    pass
class ShapeFix_Root(OCP.Standard.Standard_Transient):
    """
    Root class for fixing operations Provides context for recording changes (optional), basic precision value and limit (minimal and maximal) values for tolerances, and message registratorRoot class for fixing operations Provides context for recording changes (optional), basic precision value and limit (minimal and maximal) values for tolerances, and message registratorRoot class for fixing operations Provides context for recording changes (optional), basic precision value and limit (minimal and maximal) values for tolerances, and message registrator
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value
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
class ShapeFix_DataMapOfShapeBox2d(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : ShapeFix_DataMapOfShapeBox2d) -> ShapeFix_DataMapOfShapeBox2d: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Bnd.Bnd_Box2d) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Bnd.Bnd_Box2d) -> OCP.Bnd.Bnd_Box2d: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box2d: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box2d: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : ShapeFix_DataMapOfShapeBox2d) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box2d: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.Bnd.Bnd_Box2d) -> bool: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        IsBound
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box2d: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : ShapeFix_DataMapOfShapeBox2d) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ShapeFix_Edge(OCP.Standard.Standard_Transient):
    """
    Fixing invalid edge. Geometrical and/or topological inconsistency: - no 3d curve or pcurve, - mismatching orientation of 3d curve and pcurve, - incorrect SameParameter flag (curve deviation is greater than edge tolerance), - not adjacent curves (3d or pcurve) to the vertices.Fixing invalid edge. Geometrical and/or topological inconsistency: - no 3d curve or pcurve, - mismatching orientation of 3d curve and pcurve, - incorrect SameParameter flag (curve deviation is greater than edge tolerance), - not adjacent curves (3d or pcurve) to the vertices.Fixing invalid edge. Geometrical and/or topological inconsistency: - no 3d curve or pcurve, - mismatching orientation of 3d curve and pcurve, - incorrect SameParameter flag (curve deviation is greater than edge tolerance), - not adjacent curves (3d or pcurve) to the vertices.
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
    def FixAddCurve3d(self,edge : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Tries to build 3d curve of the edge if missing Use : It is to be called after FixRemoveCurve3d (if removed) or in any case when edge can have no 3d curve Returns: True if 3d curve was added, else False Status : OK : 3d curve exists FAIL1: BRepLib::BuildCurve3d() has failed DONE1: 3d curve was added
        """
    @overload
    def FixAddPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face,isSeam : bool,surfana : OCP.ShapeAnalysis.ShapeAnalysis_Surface,prec : float=0.0) -> bool: 
        """
        See method below for information

        See method below for information

        See method below for information

        Adds pcurve(s) of the edge if missing (by projecting 3d curve) Parameter isSeam indicates if the edge is a seam. The parameter <prec> defines the precision for calculations. If it is 0 (default), the tolerance of the edge is taken. Remark : This method is rather for internal use since it accepts parameter <surfana> for optimization of computations Use : It is to be called after FixRemovePCurve (if removed) or in any case when edge can have no pcurve Returns: True if pcurve was added, else False Status : OK : Pcurve exists FAIL1: No 3d curve FAIL2: fail during projecting DONE1: Pcurve was added DONE2: specific case of pcurve going through degenerated point on sphere encountered during projection (see class ShapeConstruct_ProjectCurveOnSurface for more info)
        """
    @overload
    def FixAddPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location,isSeam : bool,surfana : OCP.ShapeAnalysis.ShapeAnalysis_Surface,prec : float=0.0) -> bool: ...
    @overload
    def FixAddPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face,isSeam : bool,prec : float=0.0) -> bool: ...
    @overload
    def FixAddPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location,isSeam : bool,prec : float=0.0) -> bool: ...
    def FixRemoveCurve3d(self,edge : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Removes 3d curve of the edge if it does not match the vertices Returns: True, if does not match, removed (status DONE) False, (status OK) if matches or (status FAIL) if no 3d curve, nothing done
        """
    @overload
    def FixRemovePCurve(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        None

        Removes the pcurve(s) of the edge if it does not match the vertices Check is done Use : It is to be called when pcurve of an edge can be wrong (e.g., after import from IGES) Returns: True, if does not match, removed (status DONE) False, (status OK) if matches or (status FAIL) if no pcurve, nothing done
        """
    @overload
    def FixRemovePCurve(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face) -> bool: ...
    @overload
    def FixReversed2d(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        None

        Fixes edge if pcurve is directed opposite to 3d curve Check is done by call to the function ShapeAnalysis_Edge::CheckCurve3dWithPCurve() Warning: For seam edge this method will check and fix the pcurve in only one direction. Hence, it should be called twice for seam edge: once with edge orientation FORWARD and once with REVERSED. Returns: False if nothing done, True if reversed (status DONE) Status: OK - pcurve OK, nothing done FAIL1 - no pcurve FAIL2 - no 3d curve DONE1 - pcurve was reversed
        """
    @overload
    def FixReversed2d(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face) -> bool: ...
    @overload
    def FixSameParameter(self,edge : OCP.TopoDS.TopoDS_Edge,tolerance : float=0.0) -> bool: 
        """
        Tries to make edge SameParameter and sets corresponding tolerance and SameParameter flag. First, it makes edge same range if SameRange flag is not set.

        Tries to make edge SameParameter and sets corresponding tolerance and SameParameter flag. First, it makes edge same range if SameRange flag is not set.
        """
    @overload
    def FixSameParameter(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face,tolerance : float=0.0) -> bool: ...
    @overload
    def FixVertexTolerance(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None

        Increases the tolerances of the edge vertices to comprise the ends of 3d curve and pcurve on the given face (first method) or all pcurves stored in an edge (second one) Returns: True, if tolerances have been increased, otherwise False Status: OK : the original tolerances have not been changed DONE1: the tolerance of first vertex has been increased DONE2: the tolerance of last vertex has been increased
        """
    @overload
    def FixVertexTolerance(self,edge : OCP.TopoDS.TopoDS_Edge) -> bool: ...
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
    def Projector(self) -> OCP.ShapeConstruct.ShapeConstruct_ProjectCurveOnSurface: 
        """
        Returns the projector used for recomputing missing pcurves Can be used for adjusting parameters of projector
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status (in the form of True/False) of last Fix
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
class ShapeFix_EdgeConnect():
    """
    Rebuilds edges to connect with new vertices, was moved from ShapeBuild. Makes vertices to be shared to connect edges, updates positions and tolerances for shared vertices. Accepts edges bounded by two vertices each.
    """
    @overload
    def Add(self,aFirst : OCP.TopoDS.TopoDS_Edge,aSecond : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Adds information on connectivity between start vertex of second edge and end vertex of first edge, taking edges orientation into account

        Adds connectivity information for the whole shape. Note: edges in wires must be well ordered Note: flag Closed should be set for closed wires
        """
    @overload
    def Add(self,aShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def Build(self) -> None: 
        """
        Builds shared vertices, updates their positions and tolerances
        """
    def Clear(self) -> None: 
        """
        Clears internal data structure
        """
    def __init__(self) -> None: ...
    pass
class ShapeFix_EdgeProjAux(OCP.Standard.Standard_Transient):
    """
    Project 3D point (vertex) on pcurves to find Vertex Parameter on parametric representation of an edgeProject 3D point (vertex) on pcurves to find Vertex Parameter on parametric representation of an edgeProject 3D point (vertex) on pcurves to find Vertex Parameter on parametric representation of an edge
    """
    def Compute(self,preci : float) -> None: 
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
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstParam(self) -> float: 
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
    def Init(self,F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def IsFirstDone(self) -> bool: 
        """
        None
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsIso(self,C : OCP.Geom2d.Geom2d_Curve) -> bool: 
        """
        None
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsLastDone(self) -> bool: 
        """
        None
        """
    def LastParam(self) -> float: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
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
class ShapeFix_Face(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    This operator allows to perform various fixes on face and its wires: fixes provided by ShapeFix_Wire, fixing orientation of wires, addition of natural bounds, fixing of missing seam edge, and detection and removal of null-area wiresThis operator allows to perform various fixes on face and its wires: fixes provided by ShapeFix_Wire, fixing orientation of wires, addition of natural bounds, fixing of missing seam edge, and detection and removal of null-area wiresThis operator allows to perform various fixes on face and its wires: fixes provided by ShapeFix_Wire, fixing orientation of wires, addition of natural bounds, fixing of missing seam edge, and detection and removal of null-area wires
    """
    def Add(self,wire : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Add a wire to current face using BRep_Builder. Wire is added without taking into account orientation of face (as if face were FORWARD).
        """
    def ClearModes(self) -> None: 
        """
        Sets all modes to default
        """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns a face which corresponds to the current state Warning: The finally produced face may be another one ... but with the same support

        Returns a face which corresponds to the current state Warning: The finally produced face may be another one ... but with the same support
        """
    def FixAddNaturalBound(self) -> bool: 
        """
        Adds natural boundary on face if it is missing. Two cases are supported: - face has no wires - face lies on geometrically double-closed surface (sphere or torus) and none of wires is left-oriented Returns True if natural boundary was added
        """
    def FixIntersectingWires(self) -> bool: 
        """
        Detects and fixes the special case when face has more than one wire and this wires have intersection point
        """
    def FixLoopWire(self,aResWires : OCP.TopTools.TopTools_SequenceOfShape) -> bool: 
        """
        Detects if wire has a loop and fixes this situation by splitting on the few parts. if wire has a loops and it was splitted Status was set to value ShapeExtend_DONE6.
        """
    def FixMissingSeam(self) -> bool: 
        """
        Detects and fixes the special case when face on a closed surface is given by two wires closed in 3d but with gap in 2d. In that case it creates a new wire from the two, and adds a missing seam edge Returns True if missing seam was added
        """
    @overload
    def FixOrientation(self) -> bool: 
        """
        Fixes orientation of wires on the face It tries to make all wires lie outside all others (according to orientation) by reversing orientation of some of them. If face lying on sphere or torus has single wire and AddNaturalBoundMode is True, that wire is not reversed in any case (supposing that natural bound will be added). Returns True if wires were reversed

        Fixes orientation of wires on the face It tries to make all wires lie outside all others (according to orientation) by reversing orientation of some of them. If face lying on sphere or torus has single wire and AddNaturalBoundMode is True, that wire is not reversed in any case (supposing that natural bound will be added). Returns True if wires were reversed OutWires return information about out wires + list of internal wires for each (for performing split face).
        """
    @overload
    def FixOrientation(self,MapWires : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> bool: ...
    def FixPeriodicDegenerated(self) -> bool: 
        """
        Fixes topology for a specific case when face is composed by a single wire belting a periodic surface. In that case a degenerated edge is reconstructed in the degenerated pole of the surface. Initial wire gets consistent orientation. Must be used in couple and before FixMissingSeam routine
        """
    def FixSmallAreaWire(self,theIsRemoveSmallFace : bool) -> bool: 
        """
        Detects wires with small area (that is less than 100*Precision::PConfusion(). Removes these wires if they are internal. Returns : True if at least one small wire removed, False if does nothing.
        """
    def FixSplitFace(self,MapWires : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> bool: 
        """
        Split face if there are more than one out wire using inrormation after FixOrientation()
        """
    def FixWireTool(self) -> ShapeFix_Wire: 
        """
        Returns tool for fixing wires.

        Returns tool for fixing wires.
        """
    def FixWiresTwoCoincEdges(self) -> bool: 
        """
        If wire contains two coincidence edges it must be removed Queries on status after Perform()
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
    def Init(self,face : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Loads a whole face already created, with its wires, sense and location

        Starts the creation of the face By default it will be FORWARD, or REVERSED if <fwd> is False

        Starts the creation of the face By default it will be FORWARD, or REVERSED if <fwd> is False
        """
    @overload
    def Init(self,surf : OCP.Geom.Geom_Surface,preci : float,fwd : bool=True) -> None: ...
    @overload
    def Init(self,surf : OCP.ShapeAnalysis.ShapeAnalysis_Surface,preci : float,fwd : bool=True) -> None: ...
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def Perform(self) -> bool: 
        """
        Performs all the fixes, depending on modes Function Status returns the status of last call to Perform() ShapeExtend_OK : face was OK, nothing done ShapeExtend_DONE1: some wires are fixed ShapeExtend_DONE2: orientation of wires fixed ShapeExtend_DONE3: missing seam added ShapeExtend_DONE4: small area wire removed ShapeExtend_DONE5: natural bounds added ShapeExtend_FAIL1: some fails during fixing wires ShapeExtend_FAIL2: cannot fix orientation of wires ShapeExtend_FAIL3: cannot add missing seam ShapeExtend_FAIL4: cannot remove small area wire
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns resulting shape (Face or Shell if splitted) To be used instead of Face() if FixMissingSeam involved

        Returns resulting shape (Face or Shell if splitted) To be used instead of Face() if FixMissingSeam involved
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance (also to FixWireTool)
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance (also to FixWireTool)
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value (also to FixWireTool)
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status of last call to Perform() ShapeExtend_OK : face was OK, nothing done ShapeExtend_DONE1: some wires are fixed ShapeExtend_DONE2: orientation of wires fixed ShapeExtend_DONE3: missing seam added ShapeExtend_DONE4: small area wire removed ShapeExtend_DONE5: natural bounds added ShapeExtend_DONE8: face may be splited ShapeExtend_FAIL1: some fails during fixing wires ShapeExtend_FAIL2: cannot fix orientation of wires ShapeExtend_FAIL3: cannot add missing seam ShapeExtend_FAIL4: cannot remove small area wire

        Returns the status of last call to Perform() ShapeExtend_OK : face was OK, nothing done ShapeExtend_DONE1: some wires are fixed ShapeExtend_DONE2: orientation of wires fixed ShapeExtend_DONE3: missing seam added ShapeExtend_DONE4: small area wire removed ShapeExtend_DONE5: natural bounds added ShapeExtend_DONE8: face may be splited ShapeExtend_FAIL1: some fails during fixing wires ShapeExtend_FAIL2: cannot fix orientation of wires ShapeExtend_FAIL3: cannot add missing seam ShapeExtend_FAIL4: cannot remove small area wire
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,face : OCP.TopoDS.TopoDS_Face) -> None: ...
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
    def AutoCorrectPrecisionMode(self) -> int:
        """
        :type: int
        """
    @AutoCorrectPrecisionMode.setter
    def AutoCorrectPrecisionMode(self, arg1: int) -> None:
        pass
    @property
    def FixAddNaturalBoundMode(self) -> int:
        """
        :type: int
        """
    @FixAddNaturalBoundMode.setter
    def FixAddNaturalBoundMode(self, arg1: int) -> None:
        pass
    @property
    def FixIntersectingWiresMode(self) -> int:
        """
        :type: int
        """
    @FixIntersectingWiresMode.setter
    def FixIntersectingWiresMode(self, arg1: int) -> None:
        pass
    @property
    def FixLoopWiresMode(self) -> int:
        """
        :type: int
        """
    @FixLoopWiresMode.setter
    def FixLoopWiresMode(self, arg1: int) -> None:
        pass
    @property
    def FixMissingSeamMode(self) -> int:
        """
        :type: int
        """
    @FixMissingSeamMode.setter
    def FixMissingSeamMode(self, arg1: int) -> None:
        pass
    @property
    def FixOrientationMode(self) -> int:
        """
        :type: int
        """
    @FixOrientationMode.setter
    def FixOrientationMode(self, arg1: int) -> None:
        pass
    @property
    def FixPeriodicDegeneratedMode(self) -> int:
        """
        :type: int
        """
    @FixPeriodicDegeneratedMode.setter
    def FixPeriodicDegeneratedMode(self, arg1: int) -> None:
        pass
    @property
    def FixSmallAreaWireMode(self) -> int:
        """
        :type: int
        """
    @FixSmallAreaWireMode.setter
    def FixSmallAreaWireMode(self, arg1: int) -> None:
        pass
    @property
    def FixSplitFaceMode(self) -> int:
        """
        :type: int
        """
    @FixSplitFaceMode.setter
    def FixSplitFaceMode(self, arg1: int) -> None:
        pass
    @property
    def FixWireMode(self) -> int:
        """
        :type: int
        """
    @FixWireMode.setter
    def FixWireMode(self, arg1: int) -> None:
        pass
    @property
    def RemoveSmallAreaFaceMode(self) -> int:
        """
        :type: int
        """
    @RemoveSmallAreaFaceMode.setter
    def RemoveSmallAreaFaceMode(self, arg1: int) -> None:
        pass
    pass
class ShapeFix_FaceConnect():
    """
    Rebuilds connectivity between faces in shell
    """
    def Add(self,aFirst : OCP.TopoDS.TopoDS_Face,aSecond : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def Build(self,shell : OCP.TopoDS.TopoDS_Shell,sewtoler : float,fixtoler : float) -> OCP.TopoDS.TopoDS_Shell: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Clears internal data structure
        """
    def __init__(self) -> None: ...
    pass
class ShapeFix_FixSmallFace(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    Fixing face with small sizeFixing face with small sizeFixing face with small size
    """
    def ComputeSharedEdgeForStripFace(self,F : OCP.TopoDS.TopoDS_Face,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,tol : float) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Compute average edge for strip face
        """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def FixFace(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def FixPinFace(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def FixShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def FixSplitFace(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def FixSpotFace(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Fixing case of spot face, if tol = -1 used local tolerance.
        """
    def FixStripFace(self,wasdone : bool=False) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Fixing case of strip face, if tol = -1 used local tolerance
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def Perform(self) -> None: 
        """
        Fixing case of spot face
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def RemoveFacesInCaseOfSpot(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Remove spot face from compound
        """
    def RemoveFacesInCaseOfStrip(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Remove strip face from compound.
        """
    def ReplaceInCaseOfStrip(self,F : OCP.TopoDS.TopoDS_Face,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,tol : float) -> bool: 
        """
        Replace veretces and edges.
        """
    def ReplaceVerticesInCaseOfSpot(self,F : OCP.TopoDS.TopoDS_Face,tol : float) -> bool: 
        """
        Compute average vertex and replacing vertices by new one.
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def SplitOneFace(self,F : OCP.TopoDS.TopoDS_Face,theSplittedFaces : OCP.TopoDS.TopoDS_Compound) -> bool: 
        """
        Compute data for face splitting.
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
class ShapeFix_FixSmallSolid(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    Fixing solids with small sizeFixing solids with small sizeFixing solids with small size
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def Merge(self,theShape : OCP.TopoDS.TopoDS_Shape,theContext : OCP.ShapeBuild.ShapeBuild_ReShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Merge small solids in the given shape to adjacent non-small ones
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Remove(self,theShape : OCP.TopoDS.TopoDS_Shape,theContext : OCP.ShapeBuild.ShapeBuild_ReShape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Remove small solids from the given shape
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetFixMode(self,theMode : int) -> None: 
        """
        Set working mode for operator: - theMode = 0 use both WidthFactorThreshold and VolumeThreshold parameters - theMode = 1 use only WidthFactorThreshold parameter - theMode = 2 use only VolumeThreshold parameter
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value
        """
    def SetVolumeThreshold(self,theThreshold : float=-1.0) -> None: 
        """
        Set or clear volume threshold for small solids
        """
    def SetWidthFactorThreshold(self,theThreshold : float=-1.0) -> None: 
        """
        Set or clear width factor threshold for small solids
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
class ShapeFix_FreeBounds():
    """
    This class is intended to output free bounds of the shape (free bounds are the wires consisting of edges referenced by the only face). For building free bounds it uses ShapeAnalysis_FreeBounds class. This class complements it with the feature to reduce the number of open wires. This reduction is performed with help of connecting several adjacent open wires one to another what can lead to: 1. making an open wire with greater length out of several open wires 2. making closed wire out of several open wires
    """
    def GetClosedWires(self) -> OCP.TopoDS.TopoDS_Compound: 
        """
        Returns compound of closed wires out of free edges.

        Returns compound of closed wires out of free edges.
        """
    def GetOpenWires(self) -> OCP.TopoDS.TopoDS_Compound: 
        """
        Returns compound of open wires out of free edges.

        Returns compound of open wires out of free edges.
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns modified source shape.

        Returns modified source shape.
        """
    @overload
    def __init__(self,shape : OCP.TopoDS.TopoDS_Shape,closetoler : float,splitclosed : bool,splitopen : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,shape : OCP.TopoDS.TopoDS_Shape,sewtoler : float,closetoler : float,splitclosed : bool,splitopen : bool) -> None: ...
    pass
class ShapeFix_IntersectionTool():
    """
    Tool for fixing selfintersecting wire and intersecting wires
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
        """
    def CutEdge(self,edge : OCP.TopoDS.TopoDS_Edge,pend : float,cut : float,face : OCP.TopoDS.TopoDS_Face,iscutline : bool) -> bool: 
        """
        Cut edge by parameters pend and cut
        """
    def FixIntersectingWires(self,face : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def FixSelfIntersectWire(self,sewd : OCP.ShapeExtend.ShapeExtend_WireData,face : OCP.TopoDS.TopoDS_Face,NbSplit : int,NbCut : int,NbRemoved : int) -> bool: 
        """
        None
        """
    def SplitEdge(self,edge : OCP.TopoDS.TopoDS_Edge,param : float,vert : OCP.TopoDS.TopoDS_Vertex,face : OCP.TopoDS.TopoDS_Face,newE1 : OCP.TopoDS.TopoDS_Edge,newE2 : OCP.TopoDS.TopoDS_Edge,preci : float) -> bool: 
        """
        Split edge on two new edges using new vertex "vert" and "param" - parameter for splitting The "face" is necessary for pcurves and using TransferParameterProj
        """
    def __init__(self,context : OCP.ShapeBuild.ShapeBuild_ReShape,preci : float,maxtol : float=1.0) -> None: ...
    pass
class ShapeFix_ComposeShell(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    This class is intended to create a shell from the composite surface (grid of surfaces) and set of wires. It may be either division of the supporting surface of the face, or creating a shape corresponding to face on composite surface which is missing in CAS.CADE but exists in some other systems.This class is intended to create a shell from the composite surface (grid of surfaces) and set of wires. It may be either division of the supporting surface of the face, or creating a shape corresponding to face on composite surface which is missing in CAS.CADE but exists in some other systems.This class is intended to create a shell from the composite surface (grid of surfaces) and set of wires. It may be either division of the supporting surface of the face, or creating a shape corresponding to face on composite surface which is missing in CAS.CADE but exists in some other systems.
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DispatchWires(self,faces : OCP.TopTools.TopTools_SequenceOfShape,wires : ShapeFix_SequenceOfWireSegment) -> None: 
        """
        Creates new faces from the set of (closed) wires. Each wire is put on corresponding patch in the composite surface, and all pcurves on the initial (pseudo)face are reassigned to that surface. If several wires are one inside another, single face is created.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTransferParamTool(self) -> OCP.ShapeAnalysis.ShapeAnalysis_TransferParameters: 
        """
        Gets tool for transfer parameters from 3d to 2d and vice versa.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,Grid : OCP.ShapeExtend.ShapeExtend_CompositeSurface,L : OCP.TopLoc.TopLoc_Location,Face : OCP.TopoDS.TopoDS_Face,Prec : float) -> None: 
        """
        Initializes with composite surface, face and precision. Here face defines both set of wires and way of getting pcurves. Precision is used (together with tolerance of edges) for handling subtle cases, such as tangential intersections.
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def Perform(self) -> bool: 
        """
        Performs the work on already loaded data.
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns resulting shell or face (or Null shape if not done)
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value
        """
    def SetTransferParamTool(self,TransferParam : OCP.ShapeAnalysis.ShapeAnalysis_TransferParameters) -> None: 
        """
        Sets tool for transfer parameters from 3d to 2d and vice versa.
        """
    def SplitEdges(self) -> None: 
        """
        Splits edges in the original shape by grid. This is a part of Perform() which does not produce any resulting shape; the only result is filled context where splittings are recorded.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries status of last call to Perform() OK : nothing done (some kind of error) DONE1: splitting is done, at least one new face created DONE2: splitting is done, several new faces obtained FAIL1: misoriented wire encountered (handled) FAIL2: recoverable parity error FAIL3: edge with no pcurve on supporting face FAIL4: unrecoverable algorithm error (parity check)
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
    @property
    def ClosedMode(self) -> bool:
        """
        :type: bool
        """
    @ClosedMode.setter
    def ClosedMode(self, arg1: bool) -> None:
        pass
    pass
class ShapeFix_SequenceOfWireSegment(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : ShapeFix_SequenceOfWireSegment) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : ShapeFix_WireSegment) -> None: ...
    def Assign(self,theOther : ShapeFix_SequenceOfWireSegment) -> ShapeFix_SequenceOfWireSegment: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> ShapeFix_WireSegment: 
        """
        First item access
        """
    def ChangeLast(self) -> ShapeFix_WireSegment: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> ShapeFix_WireSegment: 
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
    def First(self) -> ShapeFix_WireSegment: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : ShapeFix_SequenceOfWireSegment) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : ShapeFix_WireSegment) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ShapeFix_SequenceOfWireSegment) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : ShapeFix_WireSegment) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> ShapeFix_WireSegment: 
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
    def Prepend(self,theSeq : ShapeFix_SequenceOfWireSegment) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : ShapeFix_WireSegment) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : ShapeFix_WireSegment) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ShapeFix_SequenceOfWireSegment) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> ShapeFix_WireSegment: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : ShapeFix_SequenceOfWireSegment) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class ShapeFix_Shape(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    Fixing shape in generalFixing shape in generalFixing shape in general
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def FixEdgeTool(self) -> ShapeFix_Edge: 
        """
        Returns tool for fixing edges.

        Returns tool for fixing edges.
        """
    def FixFaceTool(self) -> ShapeFix_Face: 
        """
        Returns tool for fixing faces.

        Returns tool for fixing faces.
        """
    def FixShellTool(self) -> ShapeFix_Shell: 
        """
        Returns tool for fixing shells.

        Returns tool for fixing shells.
        """
    def FixSolidTool(self) -> ShapeFix_Solid: 
        """
        Returns tool for fixing solids.

        Returns tool for fixing solids.
        """
    def FixWireTool(self) -> ShapeFix_Wire: 
        """
        Returns tool for fixing wires.

        Returns tool for fixing wires.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initislises by shape.
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def Perform(self,theProgress : OCP.Message.Message_ProgressIndicator=None) -> bool: 
        """
        Iterates on sub- shape and performs fixes
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance (also to FixSolidTool)
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance (also to FixSolidTool)
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value (also to FixSolidTool)
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns resulting shape
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status of the last Fix. This can be a combination of the following flags: ShapeExtend_DONE1: some free edges were fixed ShapeExtend_DONE2: some free wires were fixed ShapeExtend_DONE3: some free faces were fixed ShapeExtend_DONE4: some free shells were fixed ShapeExtend_DONE5: some free solids were fixed ShapeExtend_DONE6: shapes in compound(s) were fixed
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
    @property
    def FixFreeFaceMode(self) -> int:
        """
        :type: int
        """
    @FixFreeFaceMode.setter
    def FixFreeFaceMode(self, arg1: int) -> None:
        pass
    @property
    def FixFreeShellMode(self) -> int:
        """
        :type: int
        """
    @FixFreeShellMode.setter
    def FixFreeShellMode(self, arg1: int) -> None:
        pass
    @property
    def FixFreeWireMode(self) -> int:
        """
        :type: int
        """
    @FixFreeWireMode.setter
    def FixFreeWireMode(self, arg1: int) -> None:
        pass
    @property
    def FixSameParameterMode(self) -> int:
        """
        :type: int
        """
    @FixSameParameterMode.setter
    def FixSameParameterMode(self, arg1: int) -> None:
        pass
    @property
    def FixSolidMode(self) -> int:
        """
        :type: int
        """
    @FixSolidMode.setter
    def FixSolidMode(self, arg1: int) -> None:
        pass
    @property
    def FixVertexPositionMode(self) -> int:
        """
        :type: int
        """
    @FixVertexPositionMode.setter
    def FixVertexPositionMode(self, arg1: int) -> None:
        pass
    @property
    def FixVertexTolMode(self) -> int:
        """
        :type: int
        """
    @FixVertexTolMode.setter
    def FixVertexTolMode(self, arg1: int) -> None:
        pass
    pass
class ShapeFix_ShapeTolerance():
    """
    Modifies tolerances of sub-shapes (vertices, edges, faces)
    """
    def LimitTolerance(self,shape : OCP.TopoDS.TopoDS_Shape,tmin : float,tmax : float=0.0,styp : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> bool: 
        """
        Limits tolerances in a shape as follows : tmin = tmax -> as SetTolerance (forces) tmin = 0 -> maximum tolerance will be <tmax> tmax = 0 or not given (more generally, tmax < tmin) -> <tmax> ignored, minimum will be <tmin> else, maximum will be <max> and minimum will be <min> styp = VERTEX : only vertices are set styp = EDGE : only edges are set styp = FACE : only faces are set styp = WIRE : to have edges and their vertices set styp = other value : all (vertices,edges,faces) are set Returns True if at least one tolerance of the sub-shape has been modified
        """
    def SetTolerance(self,shape : OCP.TopoDS.TopoDS_Shape,preci : float,styp : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...
    def __init__(self) -> None: ...
    pass
class ShapeFix_Shell(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    Fixing orientation of faces in shellFixing orientation of faces in shellFixing orientation of faces in shell
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def ErrorFaces(self) -> OCP.TopoDS.TopoDS_Compound: 
        """
        Returns not oriented subset of faces.
        """
    def FixFaceOrientation(self,shell : OCP.TopoDS.TopoDS_Shell,isAccountMultiConex : bool=True,NonManifold : bool=False) -> bool: 
        """
        Fixes orientation of faces in shell. Changes orientation of face in the shell, if it is oriented opposite to neigbouring faces. If it is not possible to orient all faces in the shell (like in case of mebious band), this method orients only subset of faces. Other faces are stored in Error compound. Modes : isAccountMultiConex - mode for account cases of multiconnexity. If this mode is equal to Standard_True, separate shells will be created in the cases of multiconnexity. If this mode is equal to Standard_False, one shell will be created without account of multiconnexity.By defautt - Standard_True; NonManifold - mode for creation of non-manifold shells. If this mode is equal to Standard_True one non-manifold will be created from shell contains multishared edges. Else if this mode is equal to Standard_False only manifold shells will be created. By default - Standard_False.
        """
    def FixFaceTool(self) -> ShapeFix_Face: 
        """
        Returns tool for fixing faces.

        Returns tool for fixing faces.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,shell : OCP.TopoDS.TopoDS_Shell) -> None: 
        """
        Initializes by shell.
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def NbShells(self) -> int: 
        """
        Returns Number of obtainrd shells;
        """
    def Perform(self,theProgress : OCP.Message.Message_ProgressIndicator=None) -> bool: 
        """
        Iterates on subshapes and performs fixes (for each face calls ShapeFix_Face::Perform and then calls FixFaceOrientation). The passed progress indicator allows user to consult the current progress stage and abort algorithm if needed.
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance (also to FixWireTool)
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance (also to FixWireTool)
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetNonManifoldFlag(self,isNonManifold : bool) -> None: 
        """
        Sets NonManifold flag
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value (also to FixWireTool)
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        In case of multiconnexity returns compound of fixed shells else returns one shell..
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns fixed shell (or subset of oriented faces).
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status of the last Fix.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,shape : OCP.TopoDS.TopoDS_Shell) -> None: ...
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
    @property
    def FixFaceMode(self) -> int:
        """
        :type: int
        """
    @FixFaceMode.setter
    def FixFaceMode(self, arg1: int) -> None:
        pass
    @property
    def FixOrientationMode(self) -> int:
        """
        :type: int
        """
    @FixOrientationMode.setter
    def FixOrientationMode(self, arg1: int) -> None:
        pass
    pass
class ShapeFix_Solid(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    Provides method to build a solid from a shells and orients them in order to have a valid solid with finite volumeProvides method to build a solid from a shells and orients them in order to have a valid solid with finite volumeProvides method to build a solid from a shells and orients them in order to have a valid solid with finite volume
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def FixShellTool(self) -> ShapeFix_Shell: 
        """
        Returns tool for fixing shells.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,solid : OCP.TopoDS.TopoDS_Solid) -> None: 
        """
        Initializes by solid .
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def Perform(self,theProgress : OCP.Message.Message_ProgressIndicator=None) -> bool: 
        """
        Iterates on shells and performs fixes (calls ShapeFix_Shell for each subshell). The passed progress indicator allows user to consult the current progress stage and abort algorithm if needed.
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance (also to FixShellTool)
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance (also to FixShellTool)
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value (also to FixShellTool)
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        In case of multiconnexity returns compound of fixed solids else returns one solid.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns resulting solid.
        """
    def SolidFromShell(self,shell : OCP.TopoDS.TopoDS_Shell) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Calls MakeSolid and orients the solid to be "not infinite"
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status of the last Fix.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,solid : OCP.TopoDS.TopoDS_Solid) -> None: ...
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
    def CreateOpenSolidMode(self) -> bool:
        """
        :type: bool
        """
    @CreateOpenSolidMode.setter
    def CreateOpenSolidMode(self, arg1: bool) -> None:
        pass
    @property
    def FixShellMode(self) -> int:
        """
        :type: int
        """
    @FixShellMode.setter
    def FixShellMode(self, arg1: int) -> None:
        pass
    @property
    def FixShellOrientationMode(self) -> int:
        """
        :type: int
        """
    @FixShellOrientationMode.setter
    def FixShellOrientationMode(self, arg1: int) -> None:
        pass
    pass
class ShapeFix_SplitCommonVertex(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    Two wires have common vertex - this case is valid in BRep model and isn't valid in STEP => before writing into STEP it is necessary to split this vertex (each wire must has one vertex)Two wires have common vertex - this case is valid in BRep model and isn't valid in STEP => before writing into STEP it is necessary to split this vertex (each wire must has one vertex)Two wires have common vertex - this case is valid in BRep model and isn't valid in STEP => before writing into STEP it is necessary to split this vertex (each wire must has one vertex)
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def Perform(self) -> None: 
        """
        None
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
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
class ShapeFix_SplitTool():
    """
    Tool for splitting and cutting edges; includes methods used in OverlappingTool and IntersectionTool
    """
    def CutEdge(self,edge : OCP.TopoDS.TopoDS_Edge,pend : float,cut : float,face : OCP.TopoDS.TopoDS_Face,iscutline : bool) -> bool: 
        """
        Cut edge by parameters pend and cut
        """
    @overload
    def SplitEdge(self,edge : OCP.TopoDS.TopoDS_Edge,param1 : float,param2 : float,vert : OCP.TopoDS.TopoDS_Vertex,face : OCP.TopoDS.TopoDS_Face,newE1 : OCP.TopoDS.TopoDS_Edge,newE2 : OCP.TopoDS.TopoDS_Edge,tol3d : float,tol2d : float) -> bool: 
        """
        Split edge on two new edges using new vertex "vert" and "param" - parameter for splitting The "face" is necessary for pcurves and using TransferParameterProj

        Split edge on two new edges using new vertex "vert" and "param1" and "param2" - parameter for splitting and cutting The "face" is necessary for pcurves and using TransferParameterProj

        Split edge on two new edges using two new vertex V1 and V2 and two parameters for splitting - fp and lp correspondingly The "face" is necessary for pcurves and using TransferParameterProj aNum - number of edge in SeqE which corresponding to [fp,lp]
        """
    @overload
    def SplitEdge(self,edge : OCP.TopoDS.TopoDS_Edge,param : float,vert : OCP.TopoDS.TopoDS_Vertex,face : OCP.TopoDS.TopoDS_Face,newE1 : OCP.TopoDS.TopoDS_Edge,newE2 : OCP.TopoDS.TopoDS_Edge,tol3d : float,tol2d : float) -> bool: ...
    @overload
    def SplitEdge(self,edge : OCP.TopoDS.TopoDS_Edge,fp : float,V1 : OCP.TopoDS.TopoDS_Vertex,lp : float,V2 : OCP.TopoDS.TopoDS_Vertex,face : OCP.TopoDS.TopoDS_Face,SeqE : OCP.TopTools.TopTools_SequenceOfShape,aNum : int,context : OCP.ShapeBuild.ShapeBuild_ReShape,tol3d : float,tol2d : float) -> bool: ...
    def __init__(self) -> None: ...
    pass
class ShapeFix_Wire(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    This class provides a set of tools for repairing a wire.This class provides a set of tools for repairing a wire.This class provides a set of tools for repairing a wire.
    """
    def Analyzer(self) -> OCP.ShapeAnalysis.ShapeAnalysis_Wire: 
        """
        returns field Analyzer (working tool)

        returns field Analyzer (working tool)
        """
    def ClearModes(self) -> None: 
        """
        Sets all modes to default
        """
    def ClearStatuses(self) -> None: 
        """
        Clears all statuses
        """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        returns working face (Analyzer.Face())

        returns working face (Analyzer.Face())
        """
    def FixClosed(self,prec : float=-1.0) -> bool: 
        """
        Fixes a wire to be well closed It performs FixConnected, FixDegenerated and FixLacking between last and first edges (independingly on flag ClosedMode and modes for these fixings) If <prec> is -1 then MaxTolerance() is taken.
        """
    @overload
    def FixConnected(self,prec : float=-1.0) -> bool: 
        """
        Applies FixConnected(num) to all edges in the wire Connection between first and last edges is treated only if flag ClosedMode is True If <prec> is -1 then MaxTolerance() is taken.

        Fixes connected edges (preceeding and current) Forces Vertices (end of preceeding-begin of current) to be the same one Tests with starting preci or, if given greater, <prec> If <prec> is -1 then MaxTolerance() is taken.
        """
    @overload
    def FixConnected(self,num : int,prec : float) -> bool: ...
    @overload
    def FixDegenerated(self) -> bool: 
        """
        Applies FixDegenerated(num) to all edges in the wire Connection between first and last edges is treated only if flag ClosedMode is True

        Fixes Degenerated Edge Checks an <num-th> edge or a point between <num>th-1 and <num>th edges for a singularity on a supporting surface. If singularity is detected, either adds new degenerated edge (before <num>th), or makes <num>th edge to be degenerated.
        """
    @overload
    def FixDegenerated(self,num : int) -> bool: ...
    def FixEdgeCurves(self) -> bool: 
        """
        Groups the fixes dealing with 3d and pcurves of the edges. The order of the fixes and the default behaviour are: ShapeFix_Edge::FixReversed2d ShapeFix_Edge::FixRemovePCurve (only if forced) ShapeFix_Edge::FixAddPCurve ShapeFix_Edge::FixRemoveCurve3d (only if forced) ShapeFix_Edge::FixAddCurve3d FixSeam, FixShifted, ShapeFix_Edge::FixSameParameter
        """
    def FixEdgeTool(self) -> ShapeFix_Edge: 
        """
        Returns tool for fixing wires.

        Returns tool for fixing wires.
        """
    def FixGap2d(self,num : int,convert : bool=False) -> bool: 
        """
        Fixes gap between ends of pcurves on num-1 and num-th edges. myPrecision is used to detect the gap. If convert is True, converts pcurves to bsplines to bend.
        """
    def FixGap3d(self,num : int,convert : bool=False) -> bool: 
        """
        Fixes gap between ends of 3d curves on num-1 and num-th edges. myPrecision is used to detect the gap. If convert is True, converts curves to bsplines to bend.
        """
    def FixGaps2d(self) -> bool: 
        """
        Fixes gaps between ends of pcurves on adjacent edges myPrecision is used to detect the gaps.
        """
    def FixGaps3d(self) -> bool: 
        """
        Fixes gaps between ends of 3d curves on adjacent edges myPrecision is used to detect the gaps.
        """
    @overload
    def FixLacking(self,num : int,force : bool=False) -> bool: 
        """
        Applies FixLacking(num) to all edges in the wire Connection between first and last edges is treated only if flag ClosedMode is True If <force> is False (default), test for connectness is done with precision of vertex between edges, else it is done with minimal value of vertex tolerance and Analyzer.Precision(). Hence, <force> will lead to inserting lacking edges in replacement of vertices which have big tolerances.

        Fixes Lacking Edge Test if two adjucent edges are disconnected in 2d (while connected in 3d), and in that case either increase tolerance of the vertex or add a new edge (straight in 2d space), in order to close wire in 2d. Returns True if edge was added or tolerance was increased.
        """
    @overload
    def FixLacking(self,force : bool=False) -> bool: ...
    def FixNotchedEdges(self) -> bool: 
        """
        None
        """
    @overload
    def FixReorder(self) -> bool: 
        """
        Performs an analysis and reorders edges in the wire using class WireOrder

        Reorder edges in the wire as determined by WireOrder that should be filled and computed before
        """
    @overload
    def FixReorder(self,wi : OCP.ShapeAnalysis.ShapeAnalysis_WireOrder) -> bool: ...
    def FixSeam(self,num : int) -> bool: 
        """
        Fixes a seam edge A Seam edge has two pcurves, one for forward. one for reversed The forward pcurve must be set as first
        """
    def FixSelfIntersection(self) -> bool: 
        """
        Applies FixSelfIntersectingEdge(num) and FixIntersectingEdges(num) to all edges in the wire and FixIntersectingEdges(num1, num2) for all pairs num1 and num2 such that num2 >= num1 + 2 and removes wrong edges if any
        """
    def FixShifted(self) -> bool: 
        """
        Fixes edges which have pcurves shifted by whole parameter range on the closed surface (the case may occur if pcurve of edge was computed by projecting 3d curve, which goes along the seam). It compares each two consequent edges and tries to connect them if distance between ends is near to range of the surface. It also can detect and fix the case if all pcurves are connected, but lie out of parametric bounds of the surface. In addition to FixShifted from ShapeFix_Wire, more sophisticated check of degenerate points is performed, and special cases like sphere given by two meridians are treated.
        """
    @overload
    def FixSmall(self,num : int,lockvtx : bool,precsmall : float) -> bool: 
        """
        Applies FixSmall(num) to all edges in the wire

        Fixes Null Length Edge to be removed If an Edge has Null Length (regarding preci, or <precsmall> - what is smaller), it should be removed It can be with no problem if its two vertices are the same Else, if lockvtx is False, it is removed and its end vertex is put on the preceeding edge But if lockvtx is True, this edge must be kept ...
        """
    @overload
    def FixSmall(self,lockvtx : bool,precsmall : float=0.0) -> int: ...
    def FixTails(self) -> bool: 
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
    def Init(self,saw : OCP.ShapeAnalysis.ShapeAnalysis_Wire) -> None: 
        """
        Load analyzer with all the data for the wire and face and drops all fixing statuses

        Load analyzer with all the data already prepared and drops all fixing statuses If analyzer contains face, there is no need to set it by SetFace or SetSurface
        """
    @overload
    def Init(self,wire : OCP.TopoDS.TopoDS_Wire,face : OCP.TopoDS.TopoDS_Face,prec : float) -> None: ...
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
    def IsLoaded(self) -> bool: 
        """
        Tells if the wire is loaded

        Tells if the wire is loaded
        """
    def IsReady(self) -> bool: 
        """
        Tells if the wire and face are loaded

        Tells if the wire and face are loaded
        """
    def LastFixStatus(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to methods Fix... of advanced level For details see corresponding methods; universal statuses are: OK : problem not detected; nothing done DONE: problem was detected and successfully fixed FAIL: problem cannot be fixed

        Queries the status of last call to methods Fix... of advanced level For details see corresponding methods; universal statuses are: OK : problem not detected; nothing done DONE: problem was detected and successfully fixed FAIL: problem cannot be fixed
        """
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    @overload
    def Load(self,wire : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Load data for the wire, and drops all fixing statuses

        Load data for the wire, and drops all fixing statuses
        """
    @overload
    def Load(self,sbwd : OCP.ShapeExtend.ShapeExtend_WireData) -> None: ...
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def NbEdges(self) -> int: 
        """
        returns number of edges in the working wire
        """
    def Perform(self) -> bool: 
        """
        This method performs all the available fixes. If some fix is turned on or off explicitly by the Fix..Mode() flag, this fix is either called or not depending on that flag. Else (i.e. if flag is default) fix is called depending on the situation: some fixes are not called or are limited if order of edges in the wire is not OK, or depending on modes
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetFace(self,face : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Set working face for the wire

        Set working face for the wire
        """
    def SetMaxTailAngle(self,theMaxTailAngle : float) -> None: 
        """
        Sets the maximal allowed angle of the tails in radians.
        """
    def SetMaxTailWidth(self,theMaxTailWidth : float) -> None: 
        """
        Sets the maximal allowed width of the tails.
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,prec : float) -> None: 
        """
        Set working precision (to root and to analyzer)
        """
    @overload
    def SetSurface(self,surf : OCP.Geom.Geom_Surface,loc : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Set surface for the wire

        Set surface for the wire

        Set surface for the wire

        Set surface for the wire
        """
    @overload
    def SetSurface(self,surf : OCP.Geom.Geom_Surface) -> None: ...
    def StatusClosed(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusConnected(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusDegenerated(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusEdgeCurves(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusFixTails(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusGaps2d(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusGaps3d(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusLacking(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusNotches(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusRemovedSegment(self) -> bool: 
        """
        Querying the status of perfomed API fixing procedures Each Status..() methods gives information about the last call to the corresponding Fix..() method of API level: OK : no problems detected; nothing done DONE: some problem(s) was(were) detected and successfully fixed FAIL: some problem(s) cannot be fixed

        Querying the status of perfomed API fixing procedures Each Status..() methods gives information about the last call to the corresponding Fix..() method of API level: OK : no problems detected; nothing done DONE: some problem(s) was(were) detected and successfully fixed FAIL: some problem(s) cannot be fixed
        """
    def StatusReorder(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusSelfIntersection(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusSmall(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Makes the resulting Wire (by basic Brep_Builder)

        Makes the resulting Wire (by basic Brep_Builder)
        """
    def WireAPIMake(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Makes the resulting Wire (by BRepAPI_MakeWire)

        Makes the resulting Wire (by BRepAPI_MakeWire)
        """
    def WireData(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        returns working wire

        returns working wire
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,wire : OCP.TopoDS.TopoDS_Wire,face : OCP.TopoDS.TopoDS_Face,prec : float) -> None: ...
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
    def ClosedWireMode(self) -> bool:
        """
        :type: bool
        """
    @ClosedWireMode.setter
    def ClosedWireMode(self, arg1: bool) -> None:
        pass
    @property
    def FixAddCurve3dMode(self) -> int:
        """
        None

        :type: int
        """
    @FixAddCurve3dMode.setter
    def FixAddCurve3dMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixAddPCurveMode(self) -> int:
        """
        None

        :type: int
        """
    @FixAddPCurveMode.setter
    def FixAddPCurveMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixConnectedMode(self) -> int:
        """
        None

        :type: int
        """
    @FixConnectedMode.setter
    def FixConnectedMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixDegeneratedMode(self) -> int:
        """
        None

        :type: int
        """
    @FixDegeneratedMode.setter
    def FixDegeneratedMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixEdgeCurvesMode(self) -> int:
        """
        None

        :type: int
        """
    @FixEdgeCurvesMode.setter
    def FixEdgeCurvesMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixGaps2dMode(self) -> int:
        """
        :type: int
        """
    @FixGaps2dMode.setter
    def FixGaps2dMode(self, arg1: int) -> None:
        pass
    @property
    def FixGaps3dMode(self) -> int:
        """
        None

        :type: int
        """
    @FixGaps3dMode.setter
    def FixGaps3dMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixGapsByRangesMode(self) -> bool:
        """
        :type: bool
        """
    @FixGapsByRangesMode.setter
    def FixGapsByRangesMode(self, arg1: bool) -> None:
        pass
    @property
    def FixIntersectingEdgesMode(self) -> int:
        """
        None

        :type: int
        """
    @FixIntersectingEdgesMode.setter
    def FixIntersectingEdgesMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixLackingMode(self) -> int:
        """
        None

        :type: int
        """
    @FixLackingMode.setter
    def FixLackingMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixNonAdjacentIntersectingEdgesMode(self) -> int:
        """
        :type: int
        """
    @FixNonAdjacentIntersectingEdgesMode.setter
    def FixNonAdjacentIntersectingEdgesMode(self, arg1: int) -> None:
        pass
    @property
    def FixNotchedEdgesMode(self) -> int:
        """
        None

        :type: int
        """
    @FixNotchedEdgesMode.setter
    def FixNotchedEdgesMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixRemoveCurve3dMode(self) -> int:
        """
        None

        :type: int
        """
    @FixRemoveCurve3dMode.setter
    def FixRemoveCurve3dMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixRemovePCurveMode(self) -> int:
        """
        None

        :type: int
        """
    @FixRemovePCurveMode.setter
    def FixRemovePCurveMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixReorderMode(self) -> int:
        """
        None

        :type: int
        """
    @FixReorderMode.setter
    def FixReorderMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixReversed2dMode(self) -> int:
        """
        None

        :type: int
        """
    @FixReversed2dMode.setter
    def FixReversed2dMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixSameParameterMode(self) -> int:
        """
        None

        :type: int
        """
    @FixSameParameterMode.setter
    def FixSameParameterMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixSeamMode(self) -> int:
        """
        None

        :type: int
        """
    @FixSeamMode.setter
    def FixSeamMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixSelfIntersectingEdgeMode(self) -> int:
        """
        None

        :type: int
        """
    @FixSelfIntersectingEdgeMode.setter
    def FixSelfIntersectingEdgeMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixSelfIntersectionMode(self) -> int:
        """
        None

        :type: int
        """
    @FixSelfIntersectionMode.setter
    def FixSelfIntersectionMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixShiftedMode(self) -> int:
        """
        None

        :type: int
        """
    @FixShiftedMode.setter
    def FixShiftedMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixSmallMode(self) -> int:
        """
        None

        :type: int
        """
    @FixSmallMode.setter
    def FixSmallMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixTailMode(self) -> int:
        """
        None

        :type: int
        """
    @FixTailMode.setter
    def FixTailMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def FixVertexToleranceMode(self) -> int:
        """
        None

        :type: int
        """
    @FixVertexToleranceMode.setter
    def FixVertexToleranceMode(self, arg1: int) -> None:
        """
        None
        """
    @property
    def ModifyGeometryMode(self) -> bool:
        """
        :type: bool
        """
    @ModifyGeometryMode.setter
    def ModifyGeometryMode(self, arg1: bool) -> None:
        pass
    @property
    def ModifyRemoveLoopMode(self) -> int:
        """
        :type: int
        """
    @ModifyRemoveLoopMode.setter
    def ModifyRemoveLoopMode(self, arg1: int) -> None:
        pass
    @property
    def ModifyTopologyMode(self) -> bool:
        """
        :type: bool
        """
    @ModifyTopologyMode.setter
    def ModifyTopologyMode(self, arg1: bool) -> None:
        pass
    @property
    def PreferencePCurveMode(self) -> bool:
        """
        :type: bool
        """
    @PreferencePCurveMode.setter
    def PreferencePCurveMode(self, arg1: bool) -> None:
        pass
    pass
class ShapeFix_WireSegment():
    """
    This class is auxiliary class (data storage) used in ComposeShell. It is intended for representing segment of the wire (or whole wire). The segment itself is represented by ShapeExtend_WireData. In addition, some associated data necessary for computations are stored:
    """
    @overload
    def AddEdge(self,i : int,edge : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Insert a new edge with index i and implicitly defined patch indices (indefinite patch). If i==0, edge is inserted at end of wire.

        Insert a new edge with index i and explicitly defined patch indices. If i==0, edge is inserted at end of wire.
        """
    @overload
    def AddEdge(self,i : int,edge : OCP.TopoDS.TopoDS_Edge,iumin : int,iumax : int,ivmin : int,ivmax : int) -> None: ...
    def CheckPatchIndex(self,i : int) -> bool: 
        """
        Checks patch indices for edge i to satisfy equations IUMin(i) <= IUMax(i) <= IUMin(i)+1
        """
    def Clear(self) -> None: 
        """
        Clears all fields.
        """
    def DefineIUMax(self,i : int,iumax : int) -> None: 
        """
        None
        """
    def DefineIUMin(self,i : int,iumin : int) -> None: 
        """
        None
        """
    def DefineIVMax(self,i : int,ivmax : int) -> None: 
        """
        Modify minimal or maximal patch index for edge i. The corresponding patch index for that edge is modified so as to satisfy eq. iumin <= myIUMin(i) <= myIUMax(i) <= iumax
        """
    def DefineIVMin(self,i : int,ivmin : int) -> None: 
        """
        None
        """
    def Edge(self,i : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns edge by given index in the wire
        """
    def FirstVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns first vertex of the first edge in the wire (no dependance on Orientation()).
        """
    def GetPatchIndex(self,i : int) -> Tuple[int, int, int, int]: 
        """
        Returns patch indices for edge i.
        """
    def GetVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def IsClosed(self) -> bool: 
        """
        Returns True if FirstVertex() == LastVertex()
        """
    def IsVertex(self) -> bool: 
        """
        None
        """
    def LastVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns last vertex of the last edge in the wire (no dependance on Orientation()).
        """
    def Load(self,wire : OCP.ShapeExtend.ShapeExtend_WireData) -> None: 
        """
        Loads wire.
        """
    def NbEdges(self) -> int: 
        """
        Returns Number of edges in the wire
        """
    @overload
    def Orientation(self,ori : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Sets orientation flag.

        Returns orientation flag.
        """
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: ...
    def SetEdge(self,i : int,edge : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Replaces edge at index i by new one.
        """
    def SetPatchIndex(self,i : int,iumin : int,iumax : int,ivmin : int,ivmax : int) -> None: 
        """
        Set patch indices for edge i.
        """
    def SetVertex(self,theVertex : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None
        """
    def WireData(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        Returns wire.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,wire : OCP.ShapeExtend.ShapeExtend_WireData,ori : OCP.TopAbs.TopAbs_Orientation=TopAbs_Orientation.TopAbs_EXTERNAL) -> None: ...
    pass
class ShapeFix_WireVertex():
    """
    Fixing disconnected edges in the wire Fixes vertices in the wire on the basis of pre-analysis made by ShapeAnalysis_WireVertex (given as argument). The Wire has formerly been loaded in a ShapeExtend_WireData.
    """
    def Analyzer(self) -> OCP.ShapeAnalysis.ShapeAnalysis_WireVertex: 
        """
        returns internal analyzer
        """
    def Fix(self) -> int: 
        """
        Fixes all statuses except "Disjoined", i.e. the cases in which a common value has been set, with or without changing parameters Returns the count of fixed vertices, 0 if none
        """
    def FixSame(self) -> int: 
        """
        Fixes "Same" or "Close" status (same vertex may be set, without changing parameters) Returns the count of fixed vertices, 0 if none
        """
    @overload
    def Init(self,sawv : OCP.ShapeAnalysis.ShapeAnalysis_WireVertex) -> None: 
        """
        Loads the wire, ininializes internal analyzer (ShapeAnalysis_WireVertex) with the given precision, and performs analysis

        Loads the wire, ininializes internal analyzer (ShapeAnalysis_WireVertex) with the given precision, and performs analysis

        Loads all the data on wire, already analysed by ShapeAnalysis_WireVertex
        """
    @overload
    def Init(self,sbwd : OCP.ShapeExtend.ShapeExtend_WireData,preci : float) -> None: ...
    @overload
    def Init(self,wire : OCP.TopoDS.TopoDS_Wire,preci : float) -> None: ...
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        returns resulting wire (fixed)
        """
    def WireData(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        returns data on wire (fixed)
        """
    def __init__(self) -> None: ...
    pass
class ShapeFix_Wireframe(ShapeFix_Root, OCP.Standard.Standard_Transient):
    """
    Provides methods for fixing wireframe of shapeProvides methods for fixing wireframe of shapeProvides methods for fixing wireframe of shape
    """
    def CheckSmallEdges(self,theSmallEdges : OCP.TopTools.TopTools_MapOfShape,theEdgeToFaces : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,theFaceWithSmall : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,theMultyEdges : OCP.TopTools.TopTools_MapOfShape) -> bool: 
        """
        Auxiliary tool for FixSmallEdges which checks for small edges and fills the maps. Returns True if at least one small edge has been found.
        """
    def ClearStatuses(self) -> None: 
        """
        Clears all statuses
        """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def FixSmallEdges(self) -> bool: 
        """
        Fixes small edges in shape by merging adjacent edges If precision is 0.0, uses Precision::Confusion().
        """
    def FixWireGaps(self) -> bool: 
        """
        Fixes gaps between ends of curves of adjacent edges (both 3d and pcurves) in wires If precision is 0.0, uses Precision::Confusion().
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
    def LimitAngle(self) -> float: 
        """
        Get limit angle for merging edges.

        Get limit angle for merging edges.
        """
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def Load(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Loads a shape, resets statuses
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MergeSmallEdges(self,theSmallEdges : OCP.TopTools.TopTools_MapOfShape,theEdgeToFaces : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,theFaceWithSmall : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,theMultyEdges : OCP.TopTools.TopTools_MapOfShape,theModeDrop : bool=False,theLimitAngle : float=-1.0) -> bool: 
        """
        Auxiliary tool for FixSmallEdges which merges small edges. If theModeDrop is equal to Standard_True then small edges, which cannot be connected with adjacent edges are dropped. Otherwise they are kept. theLimitAngle specifies maximum allowed tangency discontinuity between adjacent edges. If theLimitAngle is equal to -1, this angle is not taken into account.
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator

        Returns message registrator
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    @overload
    def SendFail(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.

        Sends a fail to be attached to the shape. Calls SendMsg with gravity set to Message_Fail.

        Calls previous method for myShape.
        """
    @overload
    def SendFail(self,message : OCP.Message.Message_Msg) -> None: ...
    @overload
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.

        Sends a message to be attached to myShape. Calls previous method.

        Sends a message to be attached to myShape. Calls previous method.
        """
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity) -> None: ...
    @overload
    def SendMsg(self,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: ...
    @overload
    def SendWarning(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg) -> None: 
        """
        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.

        Sends a warning to be attached to the shape. Calls SendMsg with gravity set to Message_Warning.

        Calls previous method for myShape.
        """
    @overload
    def SendWarning(self,message : OCP.Message.Message_Msg) -> None: ...
    def Set(self,Root : ShapeFix_Root) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context
        """
    def SetLimitAngle(self,theLimitAngle : float) -> None: 
        """
        Set limit angle for merging edges.

        Set limit angle for merging edges.
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    def StatusSmallEdges(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Decodes the status of the last FixSmallEdges. OK - No small edges were found DONE1 - Some small edges were fixed FAIL1 - Failed to fix some small edges

        Decodes the status of the last FixSmallEdges. OK - No small edges were found DONE1 - Some small edges were fixed FAIL1 - Failed to fix some small edges
        """
    def StatusWireGaps(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Decodes the status of the last FixWireGaps. OK - No gaps were found DONE1 - Some gaps in 3D were fixed DONE2 - Some gaps in 2D were fixed FAIL1 - Failed to fix some gaps in 3D FAIL2 - Failed to fix some gaps in 2D

        Decodes the status of the last FixWireGaps. OK - No gaps were found DONE1 - Some gaps in 3D were fixed DONE2 - Some gaps in 2D were fixed FAIL1 - Failed to fix some gaps in 3D FAIL2 - Failed to fix some gaps in 2D
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
    def ModeDropSmallEdges(self) -> bool:
        """
        Returns mode managing removing small edges.

        :type: bool
        """
    @ModeDropSmallEdges.setter
    def ModeDropSmallEdges(self, arg1: bool) -> None:
        """
        Returns mode managing removing small edges.
        """
    pass
