import OCP.BRepExtrema
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.SelectMgr
import OCP.TopoDS
import BRepExtrema_ProximityDistTool
import OCP.NCollection
import OCP.Standard
import OCP.gp
import OCP.Bnd
import BRepExtrema_ElementFilter
import io
import OCP.TColStd
import OCP.Extrema
__all__  = [
"BRepExtrema_DistShapeShape",
"BRepExtrema_DistanceSS",
"BRepExtrema_ElementFilter",
"BRepExtrema_ExtCC",
"BRepExtrema_ExtCF",
"BRepExtrema_ExtFF",
"BRepExtrema_ExtPC",
"BRepExtrema_ExtPF",
"BRepExtrema_OverlapTool",
"BRepExtrema_Poly",
"BRepExtrema_ProximityDistTool",
"BRepExtrema_ProximityValueTool",
"BRepExtrema_SelfIntersection",
"BRepExtrema_SeqOfSolution",
"BRepExtrema_ShapeList",
"BRepExtrema_ShapeProximity",
"BRepExtrema_SolutionElem",
"BRepExtrema_SupportType",
"BRepExtrema_TriangleSet",
"BRepExtrema_UnCompatibleShape",
"BRepExtrema_IsInFace",
"BRepExtrema_IsOnEdge",
"BRepExtrema_IsVertex"
]
class BRepExtrema_DistShapeShape():
    """
    This class provides tools to compute minimum distance between two Shapes (Compound,CompSolid, Solid, Shell, Face, Wire, Edge, Vertex).
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object.
        """
    def InnerSolution(self) -> bool: 
        """
        True if one of the shapes is a solid and the other shape is completely or partially inside the solid.
        """
    def IsDone(self) -> bool: 
        """
        True if the minimum distance is found.
        """
    def IsMultiThread(self) -> bool: 
        """
        Returns Standard_True then computation will be performed in parallel Default value is Standard_False
        """
    def LoadS1(self,Shape1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        load first shape into extrema
        """
    def LoadS2(self,Shape1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        load second shape into extrema
        """
    def NbSolution(self) -> int: 
        """
        Returns the number of solutions satisfying the minimum distance.
        """
    def ParOnEdgeS1(self,N : int) -> Tuple[float]: 
        """
        gives the corresponding parameter t if the Nth solution is situated on an Edge of the first shape
        """
    def ParOnEdgeS2(self,N : int) -> Tuple[float]: 
        """
        gives the corresponding parameter t if the Nth solution is situated on an Edge of the first shape
        """
    def ParOnFaceS1(self,N : int) -> Tuple[float, float]: 
        """
        gives the corresponding parameters (U,V) if the Nth solution is situated on an face of the first shape
        """
    def ParOnFaceS2(self,N : int) -> Tuple[float, float]: 
        """
        gives the corresponding parameters (U,V) if the Nth solution is situated on an Face of the second shape
        """
    def Perform(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        computation of the minimum distance (value and couple of points). Parameter theDeflection is used to specify a maximum deviation of extreme distances from the minimum one. Returns IsDone status. theRange - the progress indicator of algorithm
        """
    def PointOnShape1(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point corresponding to the <N>th solution on the first Shape
        """
    def PointOnShape2(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point corresponding to the <N>th solution on the second Shape
        """
    def SetAlgo(self,A : OCP.Extrema.Extrema_ExtAlgo) -> None: 
        """
        Sets unused parameter Obsolete
        """
    def SetDeflection(self,theDeflection : float) -> None: 
        """
        Sets deflection to computation of the minimum distance
        """
    def SetFlag(self,F : OCP.Extrema.Extrema_ExtFlag) -> None: 
        """
        Sets unused parameter Obsolete
        """
    def SetMultiThread(self,theIsMultiThread : bool) -> None: 
        """
        If isMultiThread == Standard_True then computation will be performed in parallel.
        """
    def SupportOnShape1(self,N : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        gives the support where the Nth solution on the first shape is situated. This support can be a Vertex, an Edge or a Face.
        """
    def SupportOnShape2(self,N : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        gives the support where the Nth solution on the second shape is situated. This support can be a Vertex, an Edge or a Face.
        """
    def SupportTypeShape1(self,N : int) -> BRepExtrema_SupportType: 
        """
        gives the type of the support where the Nth solution on the first shape is situated: IsVertex => the Nth solution on the first shape is a Vertex IsOnEdge => the Nth soluion on the first shape is on a Edge IsInFace => the Nth solution on the first shape is inside a face the corresponding support is obtained by the method SupportOnShape1
        """
    def SupportTypeShape2(self,N : int) -> BRepExtrema_SupportType: 
        """
        gives the type of the support where the Nth solution on the second shape is situated: IsVertex => the Nth solution on the second shape is a Vertex IsOnEdge => the Nth soluion on the secondt shape is on a Edge IsInFace => the Nth solution on the second shape is inside a face the corresponding support is obtained by the method SupportOnShape2
        """
    def Value(self) -> float: 
        """
        Returns the value of the minimum distance.
        """
    @overload
    def __init__(self,Shape1 : OCP.TopoDS.TopoDS_Shape,Shape2 : OCP.TopoDS.TopoDS_Shape,theDeflection : float,F : OCP.Extrema.Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,A : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Shape1 : OCP.TopoDS.TopoDS_Shape,Shape2 : OCP.TopoDS.TopoDS_Shape,F : OCP.Extrema.Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,A : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    pass
class BRepExtrema_DistanceSS():
    """
    This class allows to compute minimum distance between two brep shapes (face edge vertex) and is used in DistShapeShape class.
    """
    def DistValue(self) -> float: 
        """
        Returns the distance value.
        """
    def IsDone(self) -> bool: 
        """
        Returns true if the distance has been computed, false otherwise.
        """
    def Seq1Value(self) -> BRepExtrema_SeqOfSolution: 
        """
        Returns the list of solutions on the first shape.
        """
    def Seq2Value(self) -> BRepExtrema_SeqOfSolution: 
        """
        Returns the list of solutions on the second shape.
        """
    def __init__(self,theS1 : OCP.TopoDS.TopoDS_Shape,theS2 : OCP.TopoDS.TopoDS_Shape,theBox1 : OCP.Bnd.Bnd_Box,theBox2 : OCP.Bnd.Bnd_Box,theDstRef : float,theDeflection : float=1e-07,theExtFlag : OCP.Extrema.Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,theExtAlgo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    pass
class BRepExtrema_ElementFilter():
    """
    Filtering tool used to detect if two given mesh elements should be tested for overlapping/intersection or not.
    """
    class FilterResult_e():
        """
        Result of filtering function.

        Members:

          NoCheck

          Overlap

          DoCheck
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
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
        DoCheck: OCP.BRepExtrema.FilterResult_e # value = <FilterResult_e.DoCheck: 2>
        NoCheck: OCP.BRepExtrema.FilterResult_e # value = <FilterResult_e.NoCheck: 0>
        Overlap: OCP.BRepExtrema.FilterResult_e # value = <FilterResult_e.Overlap: 1>
        __entries: dict # value = {'NoCheck': (<FilterResult_e.NoCheck: 0>, None), 'Overlap': (<FilterResult_e.Overlap: 1>, None), 'DoCheck': (<FilterResult_e.DoCheck: 2>, None)}
        __members__: dict # value = {'NoCheck': <FilterResult_e.NoCheck: 0>, 'Overlap': <FilterResult_e.Overlap: 1>, 'DoCheck': <FilterResult_e.DoCheck: 2>}
        pass
    def PreCheckElements(self,arg1 : int,arg2 : int) -> BRepExtrema_ElementFilter.FilterResult_e: 
        """
        Checks if two mesh elements should be tested for overlapping/intersection (used for detection correct/incorrect cases of shared edges and vertices).
        """
    def __init__(self) -> None: ...
    DoCheck: OCP.BRepExtrema.FilterResult_e # value = <FilterResult_e.DoCheck: 2>
    NoCheck: OCP.BRepExtrema.FilterResult_e # value = <FilterResult_e.NoCheck: 0>
    Overlap: OCP.BRepExtrema.FilterResult_e # value = <FilterResult_e.Overlap: 1>
    pass
class BRepExtrema_ExtCC():
    """
    None
    """
    def Initialize(self,E2 : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if E1 and E2 are parallel.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def ParameterOnE1(self,N : int) -> float: 
        """
        Returns the parameter on the first edge of the <N>th extremum distance.
        """
    def ParameterOnE2(self,N : int) -> float: 
        """
        Returns the parameter on the second edge of the <N>th extremum distance.
        """
    def Perform(self,E1 : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        An exception is raised if the fields have not been initialized.
        """
    def PointOnE1(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point of the <N>th extremum distance on the edge E1.
        """
    def PointOnE2(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point of the <N>th extremum distance on the edge E2.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the <N>th extremum square distance.
        """
    def TrimmedSquareDistances(self,P11 : OCP.gp.gp_Pnt,P12 : OCP.gp.gp_Pnt,P21 : OCP.gp.gp_Pnt,P22 : OCP.gp.gp_Pnt) -> Tuple[float, float, float, float]: 
        """
        if the edges is a trimmed curve, dist11 is a square distance between the point on E1 of parameter FirstParameter and the point of parameter FirstParameter on E2.
        """
    @overload
    def __init__(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepExtrema_ExtCF():
    """
    None
    """
    def Initialize(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the curve is on a parallel surface.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def ParameterOnEdge(self,N : int) -> float: 
        """
        Returns the parameters on the Edge of the <N>th extremum distance.
        """
    def ParameterOnFace(self,N : int) -> Tuple[float, float]: 
        """
        Returns the parameters on the Face of the <N>th extremum distance.
        """
    def Perform(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        An exception is raised if the fields have not been initialized. Be careful: this method uses the Face only for classify not for the fields.
        """
    def PointOnEdge(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point of the <N>th extremum distance.
        """
    def PointOnFace(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point of the <N>th extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the <N>th extremum square distance.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
class BRepExtrema_ExtFF():
    """
    None
    """
    def Initialize(self,F2 : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsParallel(self) -> bool: 
        """
        Returns True if the surfaces are parallel.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def ParameterOnFace1(self,N : int) -> Tuple[float, float]: 
        """
        Returns the parameters on the Face F1 of the <N>th extremum distance.
        """
    def ParameterOnFace2(self,N : int) -> Tuple[float, float]: 
        """
        Returns the parameters on the Face F2 of the <N>th extremum distance.
        """
    def Perform(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        An exception is raised if the fields have not been initialized. Be careful: this method uses the Face F2 only for classify, not for the fields.
        """
    def PointOnFace1(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point of the <N>th extremum distance.
        """
    def PointOnFace2(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point of the <N>th extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the <N>th extremum square distance.
        """
    @overload
    def __init__(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepExtrema_ExtPC():
    """
    None
    """
    def Initialize(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def IsMin(self,N : int) -> bool: 
        """
        Returns True if the <N>th extremum distance is a minimum.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Parameter(self,N : int) -> float: 
        """
        Returns the parameter on the edge of the <N>th extremum distance.
        """
    def Perform(self,V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        An exception is raised if the fields have not been initialized.
        """
    def Point(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point of the <N>th extremum distance.
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the <N>th extremum square distance.
        """
    def TrimmedSquareDistances(self,pnt1 : OCP.gp.gp_Pnt,pnt2 : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        if the curve is a trimmed curve, dist1 is a square distance between <P> and the point of parameter FirstParameter <pnt1> and dist2 is a square distance between <P> and the point of parameter LastParameter <pnt2>.
        """
    @overload
    def __init__(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepExtrema_ExtPF():
    """
    None
    """
    def Initialize(self,TheFace : OCP.TopoDS.TopoDS_Face,TheFlag : OCP.Extrema.Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,TheAlgo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        True if the distances are found.
        """
    def NbExt(self) -> int: 
        """
        Returns the number of extremum distances.
        """
    def Parameter(self,N : int) -> Tuple[float, float]: 
        """
        Returns the parameters on the Face of the <N>th extremum distance.
        """
    def Perform(self,TheVertex : OCP.TopoDS.TopoDS_Vertex,TheFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        An exception is raised if the fields have not been initialized. Be careful: this method uses the Face only for classify not for the fields.
        """
    def Point(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the Point of the <N>th extremum distance.
        """
    def SetAlgo(self,A : OCP.Extrema.Extrema_ExtAlgo) -> None: 
        """
        None
        """
    def SetFlag(self,F : OCP.Extrema.Extrema_ExtFlag) -> None: 
        """
        None
        """
    def SquareDistance(self,N : int) -> float: 
        """
        Returns the value of the <N>th extremum square distance.
        """
    @overload
    def __init__(self,TheVertex : OCP.TopoDS.TopoDS_Vertex,TheFace : OCP.TopoDS.TopoDS_Face,TheFlag : OCP.Extrema.Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,TheAlgo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepExtrema_OverlapTool():
    """
    Tool class for for detection of overlapping of two BVH primitive sets. This tool is not intended to be used independently, and is integrated in other classes, implementing algorithms based on shape tessellation (BRepExtrema_ShapeProximity and BRepExtrema_SelfIntersection).
    """
    def Accept(self,theLeaf1 : int,theLeaf2 : int) -> bool: 
        """
        Defines the rules for leaf acceptance
        """
    def IsDone(self) -> bool: 
        """
        Is overlap test completed?
        """
    def MarkDirty(self) -> None: 
        """
        Marks test results as outdated.
        """
    def OverlapSubShapes1(self) -> Any: 
        """
        Returns set of overlapped sub-shapes of 1st shape (currently only faces are detected).
        """
    def OverlapSubShapes2(self) -> Any: 
        """
        Returns set of overlapped sub-shapes of 2nd shape (currently only faces are detected).
        """
    def RejectNode(self,theCornerMin1 : OCP.SelectMgr.SelectMgr_Vec3,theCornerMax1 : OCP.SelectMgr.SelectMgr_Vec3,theCornerMin2 : OCP.SelectMgr.SelectMgr_Vec3,theCornerMax2 : OCP.SelectMgr.SelectMgr_Vec3,arg5 : float) -> bool: 
        """
        Defines the rules for node rejection by bounding box
        """
    def SetElementFilter(self,theFilter : BRepExtrema_ElementFilter) -> None: 
        """
        Sets filtering tool for preliminary checking pairs of mesh elements.
        """
    pass
class BRepExtrema_Poly():
    """
    None
    """
    @staticmethod
    def Distance_s(S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,dist : float) -> bool: 
        """
        returns Standard_True if OK.
        """
    def __init__(self) -> None: ...
    pass
class BRepExtrema_ProximityDistTool():
    """
    Tool class for computation the proximity distance from first primitive set to second one that is the maximal from minimum perpendicular distances. If no perpendicular distance is found, the minimum distance will be returned. This tool is not intended to be used independently, and is integrated in other classes, implementing algorithms based on shape tessellation (BRepExtrema_ProximityValueTool).
    """
    class ProxPnt_Status_e():
        """
        None

        Members:

          ProxPnt_Status_BORDER

          ProxPnt_Status_MIDDLE

          ProxPnt_Status_UNKNOWN
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
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
        ProxPnt_Status_BORDER: OCP.BRepExtrema.ProxPnt_Status_e # value = <ProxPnt_Status_e.ProxPnt_Status_BORDER: 0>
        ProxPnt_Status_MIDDLE: OCP.BRepExtrema.ProxPnt_Status_e # value = <ProxPnt_Status_e.ProxPnt_Status_MIDDLE: 1>
        ProxPnt_Status_UNKNOWN: OCP.BRepExtrema.ProxPnt_Status_e # value = <ProxPnt_Status_e.ProxPnt_Status_UNKNOWN: 2>
        __entries: dict # value = {'ProxPnt_Status_BORDER': (<ProxPnt_Status_e.ProxPnt_Status_BORDER: 0>, None), 'ProxPnt_Status_MIDDLE': (<ProxPnt_Status_e.ProxPnt_Status_MIDDLE: 1>, None), 'ProxPnt_Status_UNKNOWN': (<ProxPnt_Status_e.ProxPnt_Status_UNKNOWN: 2>, None)}
        __members__: dict # value = {'ProxPnt_Status_BORDER': <ProxPnt_Status_e.ProxPnt_Status_BORDER: 0>, 'ProxPnt_Status_MIDDLE': <ProxPnt_Status_e.ProxPnt_Status_MIDDLE: 1>, 'ProxPnt_Status_UNKNOWN': <ProxPnt_Status_e.ProxPnt_Status_UNKNOWN: 2>}
        pass
    def Accept(self,theSgmIdx : int,arg2 : float) -> bool: 
        """
        Defines the rules for leaf acceptance.
        """
    def LoadShapeLists(self,theShapeList1 : BRepExtrema_ShapeList,theShapeList2 : BRepExtrema_ShapeList) -> None: 
        """
        Loads the given list of subshapes into the tool.
        """
    def LoadTriangleSets(self,theSet1 : BRepExtrema_TriangleSet,theSet2 : BRepExtrema_TriangleSet) -> None: 
        """
        Loads the given element sets into the tool.
        """
    def Perform(self) -> None: 
        """
        Performs searching of the proximity distance.
        """
    def ProximityDistance(self) -> float: 
        """
        Returns the computed distance
        """
    def ProximityPoints(self,thePoint1 : OCP.SelectMgr.SelectMgr_Vec3,thePoint2 : OCP.SelectMgr.SelectMgr_Vec3) -> None: 
        """
        Returns points on triangles sets, which provide the proximity distance.
        """
    def ProximityPointsStatus(self,thePointStatus1 : BRepExtrema_ProximityDistTool.ProxPnt_Status_e,thePointStatus2 : BRepExtrema_ProximityDistTool.ProxPnt_Status_e) -> None: 
        """
        Returns status of points on triangles sets, which provide the proximity distance.
        """
    def RejectNode(self,theCornerMin : OCP.SelectMgr.SelectMgr_Vec3,theCornerMax : OCP.SelectMgr.SelectMgr_Vec3,theMetric : float) -> bool: 
        """
        Defines the rules for node rejection by bounding box.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theSet1 : BRepExtrema_TriangleSet,theNbSamples1 : int,theSet2 : BRepExtrema_TriangleSet,theShapeList1 : BRepExtrema_ShapeList,theShapeList2 : BRepExtrema_ShapeList) -> None: ...
    ProxPnt_Status_BORDER: OCP.BRepExtrema.ProxPnt_Status_e # value = <ProxPnt_Status_e.ProxPnt_Status_BORDER: 0>
    ProxPnt_Status_MIDDLE: OCP.BRepExtrema.ProxPnt_Status_e # value = <ProxPnt_Status_e.ProxPnt_Status_MIDDLE: 1>
    ProxPnt_Status_UNKNOWN: OCP.BRepExtrema.ProxPnt_Status_e # value = <ProxPnt_Status_e.ProxPnt_Status_UNKNOWN: 2>
    pass
class BRepExtrema_ProximityValueTool():
    """
    Tool class for computation of the proximity value from one BVH primitive set to another, solving max(min) problem. This tool is not intended to be used independently, and is integrated in other classes, implementing algorithms based on shape tessellation (BRepExtrema_ShapeProximity and BRepExtrema_SelfIntersection).
    """
    def Distance(self) -> float: 
        """
        Returns the computed distance.
        """
    def IsDone(self) -> bool: 
        """
        Is proximity test completed?
        """
    def LoadShapeLists(self,theShapeList1 : BRepExtrema_ShapeList,theShapeList2 : BRepExtrema_ShapeList) -> None: 
        """
        Loads the given list of subshapes into the proximity tool.
        """
    def LoadTriangleSets(self,theSet1 : BRepExtrema_TriangleSet,theSet2 : BRepExtrema_TriangleSet) -> None: 
        """
        Loads the given element sets into the proximity tool.
        """
    def MarkDirty(self) -> None: 
        """
        Marks test results as outdated.
        """
    def Perform(self) -> Tuple[float]: 
        """
        Performs the computation of the proximity value.
        """
    def ProximityPoints(self,thePoint1 : OCP.gp.gp_Pnt,thePoint2 : OCP.gp.gp_Pnt) -> None: 
        """
        Returns points on triangles sets, which provide the proximity distance.
        """
    def ProximityPointsStatus(self,thePointStatus1 : BRepExtrema_ProximityDistTool.ProxPnt_Status_e,thePointStatus2 : BRepExtrema_ProximityDistTool.ProxPnt_Status_e) -> None: 
        """
        Returns status of points on triangles sets, which provide the proximity distance.
        """
    def SetNbSamplePoints(self,theSamples1 : int=0,theSamples2 : int=0) -> None: 
        """
        Sets number of sample points used for proximity calculation for each shape. If number is less or equal zero, all triangulation nodes are used.
        """
    @overload
    def __init__(self,theSet1 : BRepExtrema_TriangleSet,theSet2 : BRepExtrema_TriangleSet,theShapeList1 : BRepExtrema_ShapeList,theShapeList2 : BRepExtrema_ShapeList) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepExtrema_SelfIntersection(BRepExtrema_ElementFilter):
    """
    Tool class for detection of self-sections in the given shape. This class is based on BRepExtrema_OverlapTool and thus uses shape tessellation to detect incorrect mesh fragments (pairs of overlapped triangles belonging to different faces). Thus, a result depends critically on the quality of mesh generator (e.g., BREP mesh is not always a good choice, because it can contain gaps between adjacent face triangulations, which may not share vertices on common edge; thus false overlap can be detected). As a result, this tool can be used for relatively fast approximated test which provides sub-set of potentially overlapped faces.
    """
    class FilterResult_e():
        pass
    def ElementSet(self) -> BRepExtrema_TriangleSet: 
        """
        Returns set of all the face triangles of the shape.
        """
    def GetSubShape(self,theID : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns sub-shape from the shape for the given index (started from 0).
        """
    def IsDone(self) -> bool: 
        """
        True if the detection is completed.
        """
    def LoadShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Loads shape for detection of self-intersections.
        """
    def OverlapElements(self) -> Any: 
        """
        Returns set of IDs of overlapped sub-shapes (started from 0).
        """
    def Perform(self) -> None: 
        """
        Performs detection of self-intersections.
        """
    def PreCheckElements(self,arg1 : int,arg2 : int) -> BRepExtrema_ElementFilter.FilterResult_e: 
        """
        Checks if two mesh elements should be tested for overlapping/intersection (used for detection correct/incorrect cases of shared edges and vertices).
        """
    def SetTolerance(self,theTolerance : float) -> None: 
        """
        Sets tolerance value used for self-intersection test.
        """
    def Tolerance(self) -> float: 
        """
        Returns tolerance value used for self-intersection test.
        """
    @overload
    def __init__(self,theTolerance : float=0.0) -> None: ...
    @overload
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape,theTolerance : float=0.0) -> None: ...
    DoCheck: OCP.BRepExtrema.FilterResult_e # value = <FilterResult_e.DoCheck: 2>
    NoCheck: OCP.BRepExtrema.FilterResult_e # value = <FilterResult_e.NoCheck: 0>
    Overlap: OCP.BRepExtrema.FilterResult_e # value = <FilterResult_e.Overlap: 1>
    pass
class BRepExtrema_SeqOfSolution(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : BRepExtrema_SeqOfSolution) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : BRepExtrema_SolutionElem) -> None: ...
    def Assign(self,theOther : BRepExtrema_SeqOfSolution) -> BRepExtrema_SeqOfSolution: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> BRepExtrema_SolutionElem: 
        """
        First item access
        """
    def ChangeLast(self) -> BRepExtrema_SolutionElem: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> BRepExtrema_SolutionElem: 
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
    def First(self) -> BRepExtrema_SolutionElem: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : BRepExtrema_SolutionElem) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : BRepExtrema_SeqOfSolution) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : BRepExtrema_SeqOfSolution) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : BRepExtrema_SolutionElem) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BRepExtrema_SolutionElem: 
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
    def Prepend(self,theItem : BRepExtrema_SolutionElem) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : BRepExtrema_SeqOfSolution) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : BRepExtrema_SolutionElem) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : BRepExtrema_SeqOfSolution) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BRepExtrema_SolutionElem: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : BRepExtrema_SeqOfSolution) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class BRepExtrema_ShapeList(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Append
        """
    def Appended(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BRepExtrema_ShapeList,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def SetValue(self,theIndex : int,theValue : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BRepExtrema_ShapeList) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepExtrema_ShapeProximity():
    """
    Tool class for shape proximity detection.
    """
    def ElementSet1(self) -> BRepExtrema_TriangleSet: 
        """
        Returns set of all the face triangles of the 1st shape.
        """
    def ElementSet2(self) -> BRepExtrema_TriangleSet: 
        """
        Returns set of all the face triangles of the 2nd shape.
        """
    def GetSubShape1(self,theID : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns sub-shape from 1st shape with the given index (started from 0).
        """
    def GetSubShape2(self,theID : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns sub-shape from 1st shape with the given index (started from 0).
        """
    def IsDone(self) -> bool: 
        """
        True if the search is completed.
        """
    def LoadShape1(self,theShape1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Loads 1st shape into proximity tool.
        """
    def LoadShape2(self,theShape2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Loads 2nd shape into proximity tool.
        """
    def OverlapSubShapes1(self) -> Any: 
        """
        Returns set of IDs of overlapped faces of 1st shape (started from 0).
        """
    def OverlapSubShapes2(self) -> Any: 
        """
        Returns set of IDs of overlapped faces of 2nd shape (started from 0).
        """
    def Perform(self) -> None: 
        """
        Performs search of overlapped faces.
        """
    def ProxPntStatus1(self) -> BRepExtrema_ProximityDistTool.ProxPnt_Status_e: 
        """
        Returns the status of point on the 1st shape, which could be used as a reference point for the value of the proximity.
        """
    def ProxPntStatus2(self) -> BRepExtrema_ProximityDistTool.ProxPnt_Status_e: 
        """
        Returns the status of point on the 2nd shape, which could be used as a reference point for the value of the proximity.
        """
    def Proximity(self) -> float: 
        """
        Returns proximity value calculated for the whole input shapes.
        """
    def ProximityPoint1(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the 1st shape, which could be used as a reference point for the value of the proximity.
        """
    def ProximityPoint2(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point on the 2nd shape, which could be used as a reference point for the value of the proximity.
        """
    def SetNbSamples1(self,theNbSamples : int) -> None: 
        """
        Set number of sample points on the 1st shape used to compute the proximity value. In case of 0, all triangulation nodes will be used.
        """
    def SetNbSamples2(self,theNbSamples : int) -> None: 
        """
        Set number of sample points on the 2nd shape used to compute the proximity value. In case of 0, all triangulation nodes will be used.
        """
    def SetTolerance(self,theTolerance : float) -> None: 
        """
        Sets tolerance value for overlap test (distance between shapes).
        """
    def Tolerance(self) -> float: 
        """
        Returns tolerance value for overlap test (distance between shapes).
        """
    @overload
    def __init__(self,theTolerance : float=2e+100) -> None: ...
    @overload
    def __init__(self,theShape1 : OCP.TopoDS.TopoDS_Shape,theShape2 : OCP.TopoDS.TopoDS_Shape,theTolerance : float=2e+100) -> None: ...
    pass
class BRepExtrema_SolutionElem():
    """
    This class is used to store information relative to the minimum distance between two shapes.
    """
    def Dist(self) -> float: 
        """
        Returns the value of the minimum distance.
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the vertex if the solution is an Edge.
        """
    def EdgeParameter(self) -> Tuple[float]: 
        """
        Returns the parameter value if the solution is on Edge.
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the vertex if the solution is an Face.
        """
    def FaceParameter(self) -> Tuple[float, float]: 
        """
        Returns the parameters U and V if the solution is in a Face.
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the solution point.
        """
    def SupportKind(self) -> BRepExtrema_SupportType: 
        """
        Returns the Support type: IsVertex => The solution is a vertex. IsOnEdge => The solution belongs to an Edge. IsInFace => The solution is inside a Face.
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the vertex if the solution is a Vertex.
        """
    @overload
    def __init__(self,theDist : float,thePoint : OCP.gp.gp_Pnt,theSolType : BRepExtrema_SupportType,theEdge : OCP.TopoDS.TopoDS_Edge,theParam : float) -> None: ...
    @overload
    def __init__(self,theDist : float,thePoint : OCP.gp.gp_Pnt,theSolType : BRepExtrema_SupportType,theVertex : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self,theDist : float,thePoint : OCP.gp.gp_Pnt,theSolType : BRepExtrema_SupportType,theFace : OCP.TopoDS.TopoDS_Face,theU : float,theV : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepExtrema_SupportType():
    """
    None

    Members:

      BRepExtrema_IsVertex

      BRepExtrema_IsOnEdge

      BRepExtrema_IsInFace
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
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
    BRepExtrema_IsInFace: OCP.BRepExtrema.BRepExtrema_SupportType # value = <BRepExtrema_SupportType.BRepExtrema_IsInFace: 2>
    BRepExtrema_IsOnEdge: OCP.BRepExtrema.BRepExtrema_SupportType # value = <BRepExtrema_SupportType.BRepExtrema_IsOnEdge: 1>
    BRepExtrema_IsVertex: OCP.BRepExtrema.BRepExtrema_SupportType # value = <BRepExtrema_SupportType.BRepExtrema_IsVertex: 0>
    __entries: dict # value = {'BRepExtrema_IsVertex': (<BRepExtrema_SupportType.BRepExtrema_IsVertex: 0>, None), 'BRepExtrema_IsOnEdge': (<BRepExtrema_SupportType.BRepExtrema_IsOnEdge: 1>, None), 'BRepExtrema_IsInFace': (<BRepExtrema_SupportType.BRepExtrema_IsInFace: 2>, None)}
    __members__: dict # value = {'BRepExtrema_IsVertex': <BRepExtrema_SupportType.BRepExtrema_IsVertex: 0>, 'BRepExtrema_IsOnEdge': <BRepExtrema_SupportType.BRepExtrema_IsOnEdge: 1>, 'BRepExtrema_IsInFace': <BRepExtrema_SupportType.BRepExtrema_IsInFace: 2>}
    pass
class BRepExtrema_TriangleSet():
    """
    Triangle set corresponding to specific face.Triangle set corresponding to specific face.
    """
    def Box(self,theIndex : int) -> Any: 
        """
        Returns AABB of the given triangle.
        """
    def Center(self,theIndex : int,theAxis : int) -> float: 
        """
        Returns centroid position along specified axis.
        """
    def Clear(self) -> None: 
        """
        Clears triangle set data.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetFaceID(self,theIndex : int) -> int: 
        """
        Returns face ID of the given triangle.
        """
    def GetShapeIDOfVtx(self,theIndex : int) -> int: 
        """
        Returns shape ID of the given vertex index.
        """
    def GetTrgIdxInShape(self,theIndex : int) -> int: 
        """
        Returns triangle index (before swapping) in tringulation of the shape, which triangle belongs, with the given trg ID in whole set (after swapping).
        """
    @overload
    def GetVertices(self,theIndex : int,theVertex1 : OCP.SelectMgr.SelectMgr_Vec3,theVertex2 : OCP.SelectMgr.SelectMgr_Vec3,theVertex3 : OCP.SelectMgr.SelectMgr_Vec3) -> None: 
        """
        Returns vertices of the given triangle.

        Returns all vertices.
        """
    @overload
    def GetVertices(self) -> List[OCP.SelectMgr.SelectMgr_Vec3]: ...
    def GetVtxIdxInShape(self,theIndex : int) -> int: 
        """
        Returns vertex index in tringulation of the shape, which vertex belongs, with the given vtx ID in whole set.
        """
    def GetVtxIndices(self,theIndex : int,theVtxIndices : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        Returns vertex indices of the given triangle.
        """
    def Init(self,theShapes : BRepExtrema_ShapeList) -> bool: 
        """
        Initializes triangle set.
        """
    def Size(self) -> int: 
        """
        Returns total number of triangles.
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps indices of two specified triangles.
        """
    @overload
    def __init__(self,theFaces : BRepExtrema_ShapeList) -> None: ...
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
class BRepExtrema_UnCompatibleShape(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.BRepExtrema', '__weakref__': <attribute '__weakref__' of 'BRepExtrema_UnCompatibleShape' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'BRepExtrema_UnCompatibleShape' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
BRepExtrema_IsInFace: OCP.BRepExtrema.BRepExtrema_SupportType # value = <BRepExtrema_SupportType.BRepExtrema_IsInFace: 2>
BRepExtrema_IsOnEdge: OCP.BRepExtrema.BRepExtrema_SupportType # value = <BRepExtrema_SupportType.BRepExtrema_IsOnEdge: 1>
BRepExtrema_IsVertex: OCP.BRepExtrema.BRepExtrema_SupportType # value = <BRepExtrema_SupportType.BRepExtrema_IsVertex: 0>
