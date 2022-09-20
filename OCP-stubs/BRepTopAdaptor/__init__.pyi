import OCP.BRepTopAdaptor
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.Adaptor2d
import OCP.NCollection
import OCP.BRepAdaptor
import OCP.gp
import io
import OCP.TopAbs
import OCP.Standard
import OCP.TopoDS
import OCP.TColStd
__all__  = [
"BRepTopAdaptor_FClass2d",
"BRepTopAdaptor_HVertex",
"BRepTopAdaptor_MapOfShapeTool",
"BRepTopAdaptor_Tool",
"BRepTopAdaptor_TopolTool"
]
class BRepTopAdaptor_FClass2d():
    """
    None
    """
    def Copy(self,Other : BRepTopAdaptor_FClass2d) -> BRepTopAdaptor_FClass2d: 
        """
        None
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def Perform(self,Puv : OCP.gp.gp_Pnt2d,RecadreOnPeriodic : bool=True) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def PerformInfinitePoint(self) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def TestOnRestriction(self,Puv : OCP.gp.gp_Pnt2d,Tol : float,RecadreOnPeriodic : bool=True) -> OCP.TopAbs.TopAbs_State: 
        """
        Test a point with +- an offset (Tol) and returns On if some points are OUT an some are IN (Caution: Internal use . see the code for more details)
        """
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,Tol : float) -> None: ...
    pass
class BRepTopAdaptor_HVertex(OCP.Adaptor3d.Adaptor3d_HVertex, OCP.Standard.Standard_Transient):
    def ChangeVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None

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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
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
    def IsSame(self,Other : OCP.Adaptor3d.Adaptor3d_HVertex) -> bool: 
        """
        None
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Parameter(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    def Resolution(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        Parametric resolution (2d).
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None

        None
        """
    def __init__(self,Vtx : OCP.TopoDS.TopoDS_Vertex,Curve : OCP.BRepAdaptor.BRepAdaptor_Curve2d) -> None: ...
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
class BRepTopAdaptor_MapOfShapeTool(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepTopAdaptor_MapOfShapeTool) -> BRepTopAdaptor_MapOfShapeTool: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BRepTopAdaptor_Tool) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BRepTopAdaptor_Tool) -> BRepTopAdaptor_Tool: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepTopAdaptor_Tool: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepTopAdaptor_Tool: 
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
    def Exchange(self,theOther : BRepTopAdaptor_MapOfShapeTool) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : BRepTopAdaptor_Tool) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepTopAdaptor_Tool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepTopAdaptor_Tool: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : BRepTopAdaptor_MapOfShapeTool) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepTopAdaptor_Tool():
    """
    None
    """
    def Destroy(self) -> None: 
        """
        None
        """
    def GetSurface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def GetTopolTool(self) -> BRepTopAdaptor_TopolTool: 
        """
        None
        """
    @overload
    def Init(self,Surface : OCP.Adaptor3d.Adaptor3d_Surface,Tol2d : float) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,F : OCP.TopoDS.TopoDS_Face,Tol2d : float) -> None: ...
    def SetTopolTool(self,TT : BRepTopAdaptor_TopolTool) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Surface : OCP.Adaptor3d.Adaptor3d_Surface,Tol2d : float) -> None: ...
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,Tol2d : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepTopAdaptor_TopolTool(OCP.Adaptor3d.Adaptor3d_TopolTool, OCP.Standard.Standard_Transient):
    def BSplSamplePnts(self,theDefl : float,theNUmin : int,theNVmin : int) -> None: 
        """
        Compute the sample-points for the intersections algorithms by adaptive algorithm for BSpline surfaces - is used in SamplePnts
        """
    def Classify(self,P2d : OCP.gp.gp_Pnt2d,Tol : float,RecadreOnPeriodic : bool=True) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def ComputeSamplePoints(self) -> None: 
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
    def Destroy(self) -> None: 
        """
        None
        """
    def DomainIsInfinite(self) -> bool: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self) -> capsule: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Has3d(self) -> bool: 
        """
        answers if arcs and vertices may have 3d representations, so that we could use Tol3d and Pnt methods.
        """
    def Identical(self,V1 : OCP.Adaptor3d.Adaptor3d_HVertex,V2 : OCP.Adaptor3d.Adaptor3d_HVertex) -> bool: 
        """
        Returns True if the vertices V1 and V2 are identical. This method does not take the orientation of the vertices in account.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        None
        """
    def InitVertexIterator(self) -> None: 
        """
        None
        """
    @overload
    def Initialize(self,S : OCP.Adaptor3d.Adaptor3d_Surface) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Initialize(self,Curve : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: ...
    @overload
    def Initialize(self) -> None: ...
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
    def IsThePointOn(self,P2d : OCP.gp.gp_Pnt2d,Tol : float,RecadreOnPeriodic : bool=True) -> bool: 
        """
        see the code for specifications)
        """
    def IsUniformSampling(self) -> bool: 
        """
        Returns true if provide uniform sampling of points.
        """
    def More(self) -> bool: 
        """
        None
        """
    def MoreVertex(self) -> bool: 
        """
        None
        """
    def NbSamples(self) -> int: 
        """
        compute the sample-points for the intersections algorithms
        """
    def NbSamplesU(self) -> int: 
        """
        compute the sample-points for the intersections algorithms
        """
    def NbSamplesV(self) -> int: 
        """
        compute the sample-points for the intersections algorithms
        """
    def Next(self) -> None: 
        """
        None
        """
    def NextVertex(self) -> None: 
        """
        None
        """
    @overload
    def Orientation(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        If the function returns the orientation of the arc. If the orientation is FORWARD or REVERSED, the arc is a "real" limit of the surface. If the orientation is INTERNAL or EXTERNAL, the arc is considered as an arc on the surface.

        If the function returns the orientation of the arc. If the orientation is FORWARD or REVERSED, the arc is a "real" limit of the surface. If the orientation is INTERNAL or EXTERNAL, the arc is considered as an arc on the surface.
        """
    @overload
    def Orientation(self,C : OCP.Adaptor3d.Adaptor3d_HVertex) -> OCP.TopAbs.TopAbs_Orientation: ...
    def Pnt(self,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> OCP.gp.gp_Pnt: 
        """
        returns 3d point of the vertex V
        """
    def SamplePnts(self,theDefl : float,theNUmin : int,theNVmin : int) -> None: 
        """
        Compute the sample-points for the intersections algorithms by adaptive algorithm for BSpline surfaces. For other surfaces algorithm is the same as in method ComputeSamplePoints(), but only fill arrays of U and V sample parameters;
        """
    def SamplePoint(self,Index : int,P2d : OCP.gp.gp_Pnt2d,P3d : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Tol3d(self,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        returns 3d tolerance of the arc C

        returns 3d tolerance of the vertex V
        """
    @overload
    def Tol3d(self,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> float: ...
    def UParameters(self,theArray : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        return the set of U parameters on the surface obtained by the method SamplePnts
        """
    def VParameters(self,theArray : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        return the set of V parameters on the surface obtained by the method SamplePnts
        """
    def Value(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        None
        """
    def Vertex(self) -> OCP.Adaptor3d.Adaptor3d_HVertex: 
        """
        None
        """
    @overload
    def __init__(self,Surface : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
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
