import OCP.ShapeAlgo
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.ShapeFix
import OCP.GeomAbs
import OCP.ShapeExtend
import OCP.TColGeom
import OCP.Geom2d
import OCP.ShapeAnalysis
import OCP.Standard
import OCP.TopoDS
import OCP.TColGeom2d
import OCP.Geom
__all__  = [
"ShapeAlgo",
"ShapeAlgo_AlgoContainer",
"ShapeAlgo_ToolContainer"
]
class ShapeAlgo():
    """
    None
    """
    @staticmethod
    def AlgoContainer_s() -> ShapeAlgo_AlgoContainer: 
        """
        Returns default AlgoContainer
        """
    @staticmethod
    def Init_s() -> None: 
        """
        Provides initerface to the algorithms from Shape Healing. Creates and initializes default AlgoContainer.
        """
    @staticmethod
    def SetAlgoContainer_s(aContainer : ShapeAlgo_AlgoContainer) -> None: 
        """
        Sets default AlgoContainer
        """
    def __init__(self) -> None: ...
    pass
class ShapeAlgo_AlgoContainer(OCP.Standard.Standard_Transient):
    @overload
    def ApproxBSplineCurve(self,bspline : OCP.Geom2d.Geom2d_BSplineCurve,seq : OCP.TColGeom2d.TColGeom2d_SequenceOfCurve) -> None: 
        """
        None

        None
        """
    @overload
    def ApproxBSplineCurve(self,bspline : OCP.Geom.Geom_BSplineCurve,seq : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: ...
    @overload
    def C0BSplineToSequenceOfC1BSplineCurve(self,BS : OCP.Geom2d.Geom2d_BSplineCurve,seqBS : OCP.TColGeom2d.TColGeom2d_HSequenceOfBoundedCurve) -> bool: 
        """
        None

        Converts C0 B-Spline curve into sequence of C1 B-Spline curves. Calls ShapeUpgrade::C0BSplineToSequenceOfC1BSplineCurve.
        """
    @overload
    def C0BSplineToSequenceOfC1BSplineCurve(self,BS : OCP.Geom.Geom_BSplineCurve,seqBS : OCP.TColGeom.TColGeom_HSequenceOfBoundedCurve) -> bool: ...
    def C0ShapeToC1Shape(self,shape : OCP.TopoDS.TopoDS_Shape,tol : float) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Converts a shape on C0 geometry into the shape on C1 geometry.
        """
    def ConnectNextWire(self,saw : OCP.ShapeAnalysis.ShapeAnalysis_Wire,nextsewd : OCP.ShapeExtend.ShapeExtend_WireData,maxtol : float,distmin : float,revsewd : bool,revnextsewd : bool) -> bool: 
        """
        Finds the best way to connect and connects <nextsewd> to already built <sewd> (in <saw>). Returns False if <nextsewd> cannot be connected, otherwise - True. <maxtol> specifies the maximum tolerance with which <nextsewd> can be added. <distmin> is used to receive the minimum distance between <nextsewd> and <sewd>. <revsewd> is True if <sewd> has been reversed before connecting. <revnextwd> is True if <nextsewd> has been reversed before connecting. Uses functionality of ShapeAnalysis_Wire.
        """
    def ConvertCurveToBSpline(self,C3D : OCP.Geom.Geom_Curve,First : float,Last : float,Tol3d : float,Continuity : OCP.GeomAbs.GeomAbs_Shape,MaxSegments : int,MaxDegree : int) -> OCP.Geom.Geom_BSplineCurve: 
        """
        Convert Geom_Curve to Geom_BSplineCurve
        """
    def ConvertSurfaceToBSpline(self,surf : OCP.Geom.Geom_Surface,UF : float,UL : float,VF : float,VL : float) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Converts a surface to B-Spline. Uses ShapeConstruct.
        """
    def ConvertToPeriodic(self,surf : OCP.Geom.Geom_Surface) -> OCP.Geom.Geom_Surface: 
        """
        Converts surface to periodic form. Calls ShapeCustom_Surface.
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
    def GetFaceUVBounds(self,F : OCP.TopoDS.TopoDS_Face) -> Tuple[float, float, float, float]: 
        """
        Computes exact UV bounds of all wires on the face
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HomoWires(self,wireIn1 : OCP.TopoDS.TopoDS_Wire,wireIn2 : OCP.TopoDS.TopoDS_Wire,wireOut1 : OCP.TopoDS.TopoDS_Wire,wireOut2 : OCP.TopoDS.TopoDS_Wire,byParam : bool) -> bool: 
        """
        Return 2 wires with the same number of edges. The both Edges number i of these wires have got the same ratio between theirs parameter lengths and their wire parameter lengths.
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
    def OuterWire(self,face : OCP.TopoDS.TopoDS_Face) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the outer wire on the face <Face>.
        """
    def SetToolContainer(self,TC : ShapeAlgo_ToolContainer) -> None: 
        """
        Sets ToolContainer

        Sets ToolContainer
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToolContainer(self) -> ShapeAlgo_ToolContainer: 
        """
        Returns ToolContainer

        Returns ToolContainer
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
class ShapeAlgo_ToolContainer(OCP.Standard.Standard_Transient):
    """
    Returns tools used by AlgoContainerReturns tools used by AlgoContainerReturns tools used by AlgoContainer
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
    def EdgeProjAux(self) -> OCP.ShapeFix.ShapeFix_EdgeProjAux: 
        """
        Returns ShapeFix_EdgeProjAux
        """
    def FixShape(self) -> OCP.ShapeFix.ShapeFix_Shape: 
        """
        Returns ShapeFix_Shape
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
