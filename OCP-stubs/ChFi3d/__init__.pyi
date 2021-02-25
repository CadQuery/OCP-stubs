import OCP.ChFi3d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopOpeBRepBuild
import OCP.GeomAdaptor
import OCP.math
import OCP.Law
import OCP.BRepBlend
import OCP.Geom
import OCP.IntSurf
import OCP.TopoDS
import OCP.Bnd
import OCP.GeomFill
import OCP.BRepAdaptor
import OCP.TopAbs
import OCP.Adaptor3d
import OCP.TopTools
import OCP.TColStd
import OCP.GeomAbs
import OCP.gp
import OCP.TopOpeBRepDS
import OCP.Geom2d
import OCP.ChFiDS
__all__  = [
"ChFi3d",
"ChFi3d_Builder",
"ChFi3d_ChBuilder",
"ChFi3d_FilBuilder",
"ChFi3d_FilletShape",
"ChFi3d_SearchSing",
"ChFi3d_AngleEdge",
"ChFi3d_BoundFac",
"ChFi3d_BoundSrf",
"ChFi3d_BoundSurf",
"ChFi3d_BuildPCurve",
"ChFi3d_CheckSameParameter",
"ChFi3d_ChercheBordsLibres",
"ChFi3d_CircularSpine",
"ChFi3d_Coefficient",
"ChFi3d_ComputeArete",
"ChFi3d_ComputeCurves",
"ChFi3d_ComputePCurv",
"ChFi3d_ComputesIntPC",
"ChFi3d_ConvTol2dToTol3d",
"ChFi3d_Couture",
"ChFi3d_CoutureOnVertex",
"ChFi3d_EdgeFromV1",
"ChFi3d_EdgeState",
"ChFi3d_EnlargeBox",
"ChFi3d_EvalTolReached",
"ChFi3d_ExtrSpineCarac",
"ChFi3d_FilCommonPoint",
"ChFi3d_FilCurveInDS",
"ChFi3d_FilDS",
"ChFi3d_FilPointInDS",
"ChFi3d_FilVertexInDS",
"ChFi3d_IndexOfSurfData",
"ChFi3d_IndexPointInDS",
"ChFi3d_IntCS",
"ChFi3d_IntTraces",
"ChFi3d_InterPlaneEdge",
"ChFi3d_IsInFront",
"ChFi3d_IsPseudoSeam",
"ChFi3d_IsSmooth",
"ChFi3d_KParticular",
"ChFi3d_NbNotDegeneratedEdges",
"ChFi3d_NumberOfEdges",
"ChFi3d_NumberOfSharpEdges",
"ChFi3d_Parameters",
"ChFi3d_PerformElSpine",
"ChFi3d_ProjectPCurv",
"ChFi3d_ReparamPcurv",
"ChFi3d_SameParameter",
"ChFi3d_SearchFD",
"ChFi3d_SolidIndex",
"ChFi3d_Spine",
"ChFi3d_StripeEdgeInter",
"ChFi3d_TrimCurve",
"ChFi3d_TrsfTrans",
"ChFi3d_cherche_edge",
"ChFi3d_cherche_element",
"ChFi3d_cherche_face1",
"ChFi3d_cherche_vertex",
"ChFi3d_conexfaces",
"ChFi3d_edge_common_faces",
"ChFi3d_evalconti",
"ChFi3d_mkbound",
"ChFi3d_nbface",
"ChFi3d_Polynomial",
"ChFi3d_QuasiAngular",
"ChFi3d_Rational"
]
class ChFi3d():
    """
    creation of spatial fillets on a solid.
    """
    @staticmethod
    def ConcaveSide_s(S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface,E : OCP.TopoDS.TopoDS_Edge,Or1 : OCP.TopAbs.TopAbs_Orientation,Or2 : OCP.TopAbs.TopAbs_Orientation) -> int: 
        """
        Returns Reversed in Or1 and(or) Or2 if the concave edge defined by the interior of faces F1 and F2, in the neighbourhood of their boundary E is of the edge opposite to the normal of their surface support. The orientation of faces is not taken into consideration in the calculation. The function returns 0 if the calculation fails (tangence), if not, it returns the number of choice of the fillet or chamfer corresponding to the orientations calculated and to the tangent to the guide line read in E.
        """
    @staticmethod
    def DefineConnectType_s(E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,SinTol : float,CorrectPoint : bool) -> OCP.ChFiDS.ChFiDS_TypeOfConcavity: 
        """
        Defines the type of concavity in the edge of connection of two faces
        """
    @staticmethod
    def IsTangentFaces_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace1 : OCP.TopoDS.TopoDS_Face,theFace2 : OCP.TopoDS.TopoDS_Face,Order : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_G1) -> bool: 
        """
        Returns true if theEdge between theFace1 and theFace2 is tangent
        """
    @staticmethod
    @overload
    def NextSide_s(Or : OCP.TopAbs.TopAbs_Orientation,OrSave : OCP.TopAbs.TopAbs_Orientation,OrFace : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Same as ConcaveSide, but the orientations are logically deduced from the result of the call of ConcaveSide on the first pair of faces of the fillet or chamnfer.

        Same as the other NextSide, but the calculation is done on an edge only.
        """
    @staticmethod
    @overload
    def NextSide_s(Or1 : OCP.TopAbs.TopAbs_Orientation,Or2 : OCP.TopAbs.TopAbs_Orientation,OrSave1 : OCP.TopAbs.TopAbs_Orientation,OrSave2 : OCP.TopAbs.TopAbs_Orientation,ChoixSauv : int) -> int: ...
    @staticmethod
    def SameSide_s(Or : OCP.TopAbs.TopAbs_Orientation,OrSave1 : OCP.TopAbs.TopAbs_Orientation,OrSave2 : OCP.TopAbs.TopAbs_Orientation,OrFace1 : OCP.TopAbs.TopAbs_Orientation,OrFace2 : OCP.TopAbs.TopAbs_Orientation) -> bool: 
        """
        Enables to determine while processing an angle, if two fillets or chamfers constituting a face have identic or opposed concave edges.
        """
    def __init__(self) -> None: ...
    pass
class ChFi3d_Builder():
    """
    Root class for calculation of surfaces (fillets, chamfers) destined to smooth edges of a gap on a Shape and the reconstruction of the Shape.
    """
    def Abscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        returns the abscissa of the vertex V on the contour of index IC.
        """
    def BadShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        if (HasResult()) returns partial result if (!HasResult())
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
        """
        Returns the Builder of topologic operations.
        """
    def Closed(self,IC : int) -> bool: 
        """
        returns true if the contour of index IC is closed
        """
    def ClosedAndTangent(self,IC : int) -> bool: 
        """
        returns true if the contour of index IC is closed an tangent.
        """
    def Compute(self) -> None: 
        """
        general calculation of geometry on all edges, topologic reconstruction.
        """
    def ComputedSurface(self,IC : int,IS : int) -> OCP.Geom.Geom_Surface: 
        """
        Returns the IS'th surface calculated on the contour IC.
        """
    @overload
    def Contains(self,E : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        gives the number of the contour containing E or 0 if E does not belong to any contour.

        gives the number of the contour containing E or 0 if E does not belong to any contour. Sets in IndexInSpine the index of E in the contour if it's found
        """
    @overload
    def Contains(self,E : OCP.TopoDS.TopoDS_Edge,IndexInSpine : int) -> int: ...
    def FaultyContour(self,I : int) -> int: 
        """
        Returns the number of I'th contour on which the calculation has failed.
        """
    def FaultyVertex(self,IV : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the IV'th vertex on which the calculation has failed.
        """
    def FirstVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        returns the First vertex V of the contour of index IC.
        """
    def Generated(self,EouV : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Advanced function for the history
        """
    def HasResult(self) -> bool: 
        """
        returns True if a partial result has been calculated
        """
    def IsDone(self) -> bool: 
        """
        returns True if the computation is success
        """
    def LastVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        returns the Last vertex V of the contour of index IC.
        """
    def Length(self,IC : int) -> float: 
        """
        returns the length of the contour of index IC.
        """
    def NbComputedSurfaces(self,IC : int) -> int: 
        """
        Returns the number of surfaces calculated on the contour IC.
        """
    def NbElements(self) -> int: 
        """
        gives the number of disjoint contours on which the fillets are calculated
        """
    def NbFaultyContours(self) -> int: 
        """
        Returns the number of contours on which the calculation has failed.
        """
    def NbFaultyVertices(self) -> int: 
        """
        Returns the number of vertices on which the calculation has failed.
        """
    def PerformTwoCornerbyInter(self,Index : int) -> bool: 
        """
        None
        """
    def RelativeAbscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        returns the relative abscissa([0.,1.]) of the vertex V on the contour of index IC.
        """
    def Remove(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        extracts from the list the contour containing edge E.
        """
    def Reset(self) -> None: 
        """
        Reset all results of compute and returns the algorythm in the state of the last acquisition to enable modification of contours or areas.
        """
    def SetContinuity(self,InternalContinuity : OCP.GeomAbs.GeomAbs_Shape,AngularTolerance : float) -> None: 
        """
        None
        """
    def SetParams(self,Tang : float,Tesp : float,T2d : float,TApp3d : float,TolApp2d : float,Fleche : float) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        if (Isdone()) makes the result. if (!Isdone())
        """
    def SplitKPart(self,Data : OCP.ChFiDS.ChFiDS_SurfData,SetData : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Spine : OCP.ChFiDS.ChFiDS_Spine,Iedge : int,S1 : OCP.Adaptor3d.Adaptor3d_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Intf : bool,Intl : bool) -> bool: 
        """
        Method, implemented in the inheritants, calculates the elements of construction of the surface (fillet or chamfer).
        """
    def StripeStatus(self,IC : int) -> OCP.ChFiDS.ChFiDS_ErrorStatus: 
        """
        for the stripe IC ,indication on the cause of failure WalkingFailure,TwistedSurface,Error, Ok
        """
    def Value(self,I : int) -> OCP.ChFiDS.ChFiDS_Spine: 
        """
        gives the n'th set of edges (contour) if I >NbElements()
        """
    pass
class ChFi3d_ChBuilder(ChFi3d_Builder):
    """
    construction tool for 3D chamfers on edges (on a solid).
    """
    def Abscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        returns the abscissa of the vertex V on the contour of index IC.
        """
    @overload
    def Add(self,Dis1 : float,Dis2 : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        initializes a contour with the edge <E> as first (the next are found by propagation ). The two distances (parameters of the chamfer) must be set after. if the edge <E> has more than 2 adjacent faces

        initializes a new contour with the edge <E> as first (the next are found by propagation ), and the distance <Dis> if the edge <E> has more than 2 adjacent faces

        initializes a new contour with the edge <E> as first (the next are found by propagation ), and the distance <Dis1> and <Dis2> if the edge <E> has more than 2 adjacent faces
        """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def Add(self,Dis : float,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    def AddDA(self,Dis : float,Angle : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        initializes a new contour with the edge <E> as first (the next are found by propagation ), and the distance <Dis1> and <Angle> if the edge <E> has more than 2 adjacent faces
        """
    def BadShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        if (HasResult()) returns partial result if (!HasResult())
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
        """
        Returns the Builder of topologic operations.
        """
    def Closed(self,IC : int) -> bool: 
        """
        returns true if the contour of index IC is closed
        """
    def ClosedAndTangent(self,IC : int) -> bool: 
        """
        returns true if the contour of index IC is closed an tangent.
        """
    def Compute(self) -> None: 
        """
        general calculation of geometry on all edges, topologic reconstruction.
        """
    def ComputedSurface(self,IC : int,IS : int) -> OCP.Geom.Geom_Surface: 
        """
        Returns the IS'th surface calculated on the contour IC.
        """
    @overload
    def Contains(self,E : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        gives the number of the contour containing E or 0 if E does not belong to any contour.

        gives the number of the contour containing E or 0 if E does not belong to any contour. Sets in IndexInSpine the index of E in the contour if it's found
        """
    @overload
    def Contains(self,E : OCP.TopoDS.TopoDS_Edge,IndexInSpine : int) -> int: ...
    def Dists(self,IC : int) -> Tuple[float, float]: 
        """
        gives the distances <Dis1> and <Dis2> of the fillet contour of index <IC> in the DS
        """
    def FaultyContour(self,I : int) -> int: 
        """
        Returns the number of I'th contour on which the calculation has failed.
        """
    def FaultyVertex(self,IV : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the IV'th vertex on which the calculation has failed.
        """
    def FirstVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        returns the First vertex V of the contour of index IC.
        """
    def Generated(self,EouV : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Advanced function for the history
        """
    def GetDist(self,IC : int) -> Tuple[float]: 
        """
        gives the distances <Dis> of the fillet contour of index <IC> in the DS
        """
    def GetDistAngle(self,IC : int) -> Tuple[float, float]: 
        """
        gives the distances <Dis> and <Angle> of the fillet contour of index <IC> in the DS
        """
    def HasResult(self) -> bool: 
        """
        returns True if a partial result has been calculated
        """
    def IsChamfer(self,IC : int) -> OCP.ChFiDS.ChFiDS_ChamfMethod: 
        """
        renvoi la methode des chanfreins utilisee
        """
    def IsDone(self) -> bool: 
        """
        returns True if the computation is success
        """
    def LastVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        returns the Last vertex V of the contour of index IC.
        """
    def Length(self,IC : int) -> float: 
        """
        returns the length of the contour of index IC.
        """
    def Mode(self) -> OCP.ChFiDS.ChFiDS_ChamfMode: 
        """
        returns the mode of chamfer used
        """
    def NbComputedSurfaces(self,IC : int) -> int: 
        """
        Returns the number of surfaces calculated on the contour IC.
        """
    def NbElements(self) -> int: 
        """
        gives the number of disjoint contours on which the fillets are calculated
        """
    def NbFaultyContours(self) -> int: 
        """
        Returns the number of contours on which the calculation has failed.
        """
    def NbFaultyVertices(self) -> int: 
        """
        Returns the number of vertices on which the calculation has failed.
        """
    def NbSurf(self,IC : int) -> int: 
        """
        None
        """
    @overload
    def PerformSurf(self,Data : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Guide : OCP.ChFiDS.ChFiDS_HElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC1 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Sref1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,PCref1 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Or1 : OCP.TopAbs.TopAbs_Orientation,S2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC2 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Sref2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,PCref2 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Or2 : OCP.TopAbs.TopAbs_Orientation,MaxStep : float,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP1 : bool,RecRst1 : bool,RecP2 : bool,RecRst2 : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, bool, float, float]: 
        """
        Methode, implemented in inheritants, calculates the elements of construction of the surface (fillet or chamfer).

        Method, implemented in the inheritants, calculates the elements of construction of the surface (fillet or chamfer) contact edge/face.

        Method, implemented in inheritants, calculates the elements of construction of the surface (fillet or chamfer) contact edge/face.

        Method, implemented in inheritants, calculates the elements of construction of the surface (fillet or chamfer) contact edge/edge.
        """
    @overload
    def PerformSurf(self,Data : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Guide : OCP.ChFiDS.ChFiDS_HElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC1 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Sref1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,PCref1 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,S2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Or2 : OCP.TopAbs.TopAbs_Orientation,MaxStep : float,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP : bool,RecS : bool,RecRst : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, float, float]: ...
    @overload
    def PerformSurf(self,Data : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Guide : OCP.ChFiDS.ChFiDS_HElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,MaxStep : float,Fleche : float,TolGuide : float,First : float,Last : float,Inside : bool,Appro : bool,Forward : bool,RecOnS1 : bool,RecOnS2 : bool,Soldep : OCP.math.math_Vector,Intf : int,Intl : int) -> bool: ...
    @overload
    def PerformSurf(self,Data : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Guide : OCP.ChFiDS.ChFiDS_HElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Or1 : OCP.TopAbs.TopAbs_Orientation,S2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC2 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Sref2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,PCref2 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,MaxStep : float,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP : bool,RecS : bool,RecRst : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, float, float]: ...
    def PerformTwoCornerbyInter(self,Index : int) -> bool: 
        """
        None
        """
    def RelativeAbscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        returns the relative abscissa([0.,1.]) of the vertex V on the contour of index IC.
        """
    def Remove(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        extracts from the list the contour containing edge E.
        """
    def Reset(self) -> None: 
        """
        Reset all results of compute and returns the algorythm in the state of the last acquisition to enable modification of contours or areas.
        """
    def ResetContour(self,IC : int) -> None: 
        """
        Reset tous rayons du contour IC.
        """
    def Sect(self,IC : int,IS : int) -> OCP.ChFiDS.ChFiDS_SecHArray1: 
        """
        None
        """
    def SetContinuity(self,InternalContinuity : OCP.GeomAbs.GeomAbs_Shape,AngularTolerance : float) -> None: 
        """
        None
        """
    def SetDist(self,Dis : float,IC : int,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        set the distance <Dis> of the fillet contour of index <IC> in the DS with <Dis> on <F>. if the face <F> is not one of common faces of an edge of the contour <IC>
        """
    def SetDistAngle(self,Dis : float,Angle : float,IC : int,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        set the distance <Dis> and <Angle> of the fillet contour of index <IC> in the DS with <Dis> on <F>. if the face <F> is not one of common faces of an edge of the contour <IC>
        """
    def SetDists(self,Dis1 : float,Dis2 : float,IC : int,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        set the distances <Dis1> and <Dis2> of the fillet contour of index <IC> in the DS with <Dis1> on <F>. if the face <F> is not one of common faces of an edge of the contour <IC>
        """
    def SetMode(self,theMode : OCP.ChFiDS.ChFiDS_ChamfMode) -> None: 
        """
        set the mode of shamfer
        """
    def SetParams(self,Tang : float,Tesp : float,T2d : float,TApp3d : float,TolApp2d : float,Fleche : float) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        if (Isdone()) makes the result. if (!Isdone())
        """
    @overload
    def SimulSurf(self,Data : OCP.ChFiDS.ChFiDS_SurfData,Guide : OCP.ChFiDS.ChFiDS_HElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC1 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Sref1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,PCref1 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,S2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Or2 : OCP.TopAbs.TopAbs_Orientation,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP : bool,RecS : bool,RecRst : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, float, float]: 
        """
        None

        None

        None
        """
    @overload
    def SimulSurf(self,Data : OCP.ChFiDS.ChFiDS_SurfData,Guide : OCP.ChFiDS.ChFiDS_HElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC1 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Sref1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,PCref1 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Or1 : OCP.TopAbs.TopAbs_Orientation,S2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC2 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Sref2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,PCref2 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Or2 : OCP.TopAbs.TopAbs_Orientation,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP1 : bool,RecRst1 : bool,RecP2 : bool,RecRst2 : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, bool, float, float]: ...
    @overload
    def SimulSurf(self,Data : OCP.ChFiDS.ChFiDS_SurfData,Guide : OCP.ChFiDS.ChFiDS_HElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Or1 : OCP.TopAbs.TopAbs_Orientation,S2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC2 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Sref2 : OCP.BRepAdaptor.BRepAdaptor_HSurface,PCref2 : OCP.BRepAdaptor.BRepAdaptor_HCurve2d,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP : bool,RecS : bool,RecRst : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, float, float]: ...
    def Simulate(self,IC : int) -> None: 
        """
        None
        """
    def SplitKPart(self,Data : OCP.ChFiDS.ChFiDS_SurfData,SetData : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Spine : OCP.ChFiDS.ChFiDS_Spine,Iedge : int,S1 : OCP.Adaptor3d.Adaptor3d_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Intf : bool,Intl : bool) -> bool: 
        """
        Method, implemented in the inheritants, calculates the elements of construction of the surface (fillet or chamfer).
        """
    def StripeStatus(self,IC : int) -> OCP.ChFiDS.ChFiDS_ErrorStatus: 
        """
        for the stripe IC ,indication on the cause of failure WalkingFailure,TwistedSurface,Error, Ok
        """
    def Value(self,I : int) -> OCP.ChFiDS.ChFiDS_Spine: 
        """
        gives the n'th set of edges (contour) if I >NbElements()
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,Ta : float=0.01) -> None: ...
    pass
class ChFi3d_FilBuilder(ChFi3d_Builder):
    """
    Tool of construction of fillets 3d on edges (on a solid).
    """
    def Abscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        returns the abscissa of the vertex V on the contour of index IC.
        """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        initialisation of a contour with the first edge (the following are found by propagation). Attention, you need to start with SetRadius.

        initialisation of the constant vector the corresponding 1st edge.
        """
    @overload
    def Add(self,Radius : float,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    def BadShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        if (HasResult()) returns partial result if (!HasResult())
        """
    def Builder(self) -> OCP.TopOpeBRepBuild.TopOpeBRepBuild_HBuilder: 
        """
        Returns the Builder of topologic operations.
        """
    def Closed(self,IC : int) -> bool: 
        """
        returns true if the contour of index IC is closed
        """
    def ClosedAndTangent(self,IC : int) -> bool: 
        """
        returns true if the contour of index IC is closed an tangent.
        """
    def Compute(self) -> None: 
        """
        general calculation of geometry on all edges, topologic reconstruction.
        """
    def ComputedSurface(self,IC : int,IS : int) -> OCP.Geom.Geom_Surface: 
        """
        Returns the IS'th surface calculated on the contour IC.
        """
    @overload
    def Contains(self,E : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        gives the number of the contour containing E or 0 if E does not belong to any contour.

        gives the number of the contour containing E or 0 if E does not belong to any contour. Sets in IndexInSpine the index of E in the contour if it's found
        """
    @overload
    def Contains(self,E : OCP.TopoDS.TopoDS_Edge,IndexInSpine : int) -> int: ...
    def FaultyContour(self,I : int) -> int: 
        """
        Returns the number of I'th contour on which the calculation has failed.
        """
    def FaultyVertex(self,IV : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the IV'th vertex on which the calculation has failed.
        """
    def FirstVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        returns the First vertex V of the contour of index IC.
        """
    def Generated(self,EouV : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Advanced function for the history
        """
    def GetBounds(self,IC : int,E : OCP.TopoDS.TopoDS_Edge,First : float,Last : float) -> bool: 
        """
        Returns in First and Last les extremities of the part of variable vector framing E, returns False if E is flagged as edge constant.
        """
    def GetFilletShape(self) -> ChFi3d_FilletShape: 
        """
        Returns the type of fillet surface.
        """
    def GetLaw(self,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> OCP.Law.Law_Function: 
        """
        Returns the rule of elementary evolution of the part to variable vector framing E, returns a rule zero if E is flagged as edge constant.
        """
    def HasResult(self) -> bool: 
        """
        returns True if a partial result has been calculated
        """
    @overload
    def IsConstant(self,IC : int) -> bool: 
        """
        Returns true the contour is flaged as edge constant.

        Returns true E is flagged as edge constant.
        """
    @overload
    def IsConstant(self,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> bool: ...
    def IsDone(self) -> bool: 
        """
        returns True if the computation is success
        """
    def LastVertex(self,IC : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        returns the Last vertex V of the contour of index IC.
        """
    def Length(self,IC : int) -> float: 
        """
        returns the length of the contour of index IC.
        """
    def NbComputedSurfaces(self,IC : int) -> int: 
        """
        Returns the number of surfaces calculated on the contour IC.
        """
    def NbElements(self) -> int: 
        """
        gives the number of disjoint contours on which the fillets are calculated
        """
    def NbFaultyContours(self) -> int: 
        """
        Returns the number of contours on which the calculation has failed.
        """
    def NbFaultyVertices(self) -> int: 
        """
        Returns the number of vertices on which the calculation has failed.
        """
    def NbSurf(self,IC : int) -> int: 
        """
        None
        """
    def PerformTwoCornerbyInter(self,Index : int) -> bool: 
        """
        None
        """
    @overload
    def Radius(self,IC : int) -> float: 
        """
        Returns the vector if the contour is flagged as edge constant.

        Returns the vector if E is flagged as edge constant.
        """
    @overload
    def Radius(self,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> float: ...
    def RelativeAbscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        returns the relative abscissa([0.,1.]) of the vertex V on the contour of index IC.
        """
    def Remove(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        extracts from the list the contour containing edge E.
        """
    def Reset(self) -> None: 
        """
        Reset all results of compute and returns the algorythm in the state of the last acquisition to enable modification of contours or areas.
        """
    def ResetContour(self,IC : int) -> None: 
        """
        Reset all vectors of contour IC.
        """
    def Sect(self,IC : int,IS : int) -> OCP.ChFiDS.ChFiDS_SecHArray1: 
        """
        None
        """
    def SetContinuity(self,InternalContinuity : OCP.GeomAbs.GeomAbs_Shape,AngularTolerance : float) -> None: 
        """
        None
        """
    def SetFilletShape(self,FShape : ChFi3d_FilletShape) -> None: 
        """
        Sets the type of fillet surface.
        """
    def SetLaw(self,IC : int,E : OCP.TopoDS.TopoDS_Edge,L : OCP.Law.Law_Function) -> None: 
        """
        Sets the rule of elementary evolution of the part to variable vector framing E.
        """
    def SetParams(self,Tang : float,Tesp : float,T2d : float,TApp3d : float,TolApp2d : float,Fleche : float) -> None: 
        """
        None
        """
    @overload
    def SetRadius(self,C : OCP.Law.Law_Function,IC : int,IinC : int) -> None: 
        """
        Set the radius of the contour of index IC.

        Set a constant on edge E of the contour of index IC. Since then E is flagged as constant.

        Set a vector on vertex V of the contour of index IC.

        Set a vertex on the point of parametre U in the edge IinC of the contour of index IC
        """
    @overload
    def SetRadius(self,Radius : float,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def SetRadius(self,Radius : float,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def SetRadius(self,UandR : OCP.gp.gp_XY,IC : int,IinC : int) -> None: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        if (Isdone()) makes the result. if (!Isdone())
        """
    def Simulate(self,IC : int) -> None: 
        """
        None
        """
    def SplitKPart(self,Data : OCP.ChFiDS.ChFiDS_SurfData,SetData : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Spine : OCP.ChFiDS.ChFiDS_Spine,Iedge : int,S1 : OCP.Adaptor3d.Adaptor3d_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Intf : bool,Intl : bool) -> bool: 
        """
        Method, implemented in the inheritants, calculates the elements of construction of the surface (fillet or chamfer).
        """
    def StripeStatus(self,IC : int) -> OCP.ChFiDS.ChFiDS_ErrorStatus: 
        """
        for the stripe IC ,indication on the cause of failure WalkingFailure,TwistedSurface,Error, Ok
        """
    @overload
    def UnSet(self,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Extracts the flag constant and the vector of edge E.

        Extracts the vector of the vertex V.
        """
    @overload
    def UnSet(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    def Value(self,I : int) -> OCP.ChFiDS.ChFiDS_Spine: 
        """
        gives the n'th set of edges (contour) if I >NbElements()
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,FShape : ChFi3d_FilletShape=ChFi3d_FilletShape.ChFi3d_Rational,Ta : float=0.01) -> None: ...
    pass
class ChFi3d_FilletShape():
    """
    Lists the types of fillet shapes. These include the following: - ChFi3d_Rational (default value), which is the standard NURBS representation of circles, - ChFi3d_QuasiAngular, which is a NURBS representation of circles where the parameters match those of the circle, - ChFi3d_Polynomial, which corresponds to a polynomial approximation of circles. This type facilitates the implementation of the construction algorithm.

    Members:

      ChFi3d_Rational

      ChFi3d_QuasiAngular

      ChFi3d_Polynomial
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
    ChFi3d_Polynomial: OCP.ChFi3d.ChFi3d_FilletShape # value = <ChFi3d_FilletShape.ChFi3d_Polynomial: 2>
    ChFi3d_QuasiAngular: OCP.ChFi3d.ChFi3d_FilletShape # value = <ChFi3d_FilletShape.ChFi3d_QuasiAngular: 1>
    ChFi3d_Rational: OCP.ChFi3d.ChFi3d_FilletShape # value = <ChFi3d_FilletShape.ChFi3d_Rational: 0>
    __entries: dict # value = {'ChFi3d_Rational': (<ChFi3d_FilletShape.ChFi3d_Rational: 0>, None), 'ChFi3d_QuasiAngular': (<ChFi3d_FilletShape.ChFi3d_QuasiAngular: 1>, None), 'ChFi3d_Polynomial': (<ChFi3d_FilletShape.ChFi3d_Polynomial: 2>, None)}
    __members__: dict # value = {'ChFi3d_Rational': <ChFi3d_FilletShape.ChFi3d_Rational: 0>, 'ChFi3d_QuasiAngular': <ChFi3d_FilletShape.ChFi3d_QuasiAngular: 1>, 'ChFi3d_Polynomial': <ChFi3d_FilletShape.ChFi3d_Polynomial: 2>}
    pass
class ChFi3d_SearchSing(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    Searches singularities on fillet. F(t) = (C1(t) - C2(t)).(C1'(t) - C2'(t));
    """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        computes the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        computes the value of the function <F> for the variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        computes the value <F> and the derivative <D> of the function for the variable <X>. Returns True if the calculation were successfully done, False otherwise.
        """
    def __init__(self,C1 : OCP.Geom.Geom_Curve,C2 : OCP.Geom.Geom_Curve) -> None: ...
    pass
def ChFi3d_AngleEdge(Vtx : OCP.TopoDS.TopoDS_Vertex,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge) -> float:
    """
    None
    """
def ChFi3d_BoundFac(S : OCP.BRepAdaptor.BRepAdaptor_Surface,umin : float,umax : float,vmin : float,vmax : float,checknaturalbounds : bool=True) -> None:
    """
    None
    """
def ChFi3d_BoundSrf(S : OCP.GeomAdaptor.GeomAdaptor_Surface,umin : float,umax : float,vmin : float,vmax : float,checknaturalbounds : bool=True) -> None:
    """
    None
    """
def ChFi3d_BoundSurf(DStr : OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure,Fd1 : OCP.ChFiDS.ChFiDS_SurfData,IFaCo1 : int,IFaArc1 : int) -> OCP.GeomAdaptor.GeomAdaptor_HSurface:
    """
    None
    """
@overload
def ChFi3d_BuildPCurve(Surf : OCP.Adaptor3d.Adaptor3d_HSurface,p1 : OCP.gp.gp_Pnt2d,v1 : OCP.gp.gp_Vec,p2 : OCP.gp.gp_Pnt2d,v2 : OCP.gp.gp_Vec,redresse : bool=False) -> OCP.Geom2d.Geom2d_Curve:
    """
    None

    None

    None
    """
@overload
def ChFi3d_BuildPCurve(Surf : OCP.Adaptor3d.Adaptor3d_HSurface,p1 : OCP.gp.gp_Pnt2d,v1 : OCP.gp.gp_Vec2d,p2 : OCP.gp.gp_Pnt2d,v2 : OCP.gp.gp_Vec2d,redresse : bool=False) -> OCP.Geom2d.Geom2d_Curve:
    pass
@overload
def ChFi3d_BuildPCurve(p1 : OCP.gp.gp_Pnt2d,d1 : OCP.gp.gp_Dir2d,p2 : OCP.gp.gp_Pnt2d,d2 : OCP.gp.gp_Dir2d,redresse : bool=True) -> OCP.Geom2d.Geom2d_Curve:
    pass
def ChFi3d_CheckSameParameter(C3d : OCP.Adaptor3d.Adaptor3d_HCurve,Pcurv : OCP.Geom2d.Geom2d_Curve,S : OCP.Adaptor3d.Adaptor3d_HSurface,tol3d : float,tolreached : float) -> bool:
    """
    None
    """
def ChFi3d_ChercheBordsLibres(myVEMap : OCP.ChFiDS.ChFiDS_Map,V1 : OCP.TopoDS.TopoDS_Vertex,bordlibre : bool,edgelibre1 : OCP.TopoDS.TopoDS_Edge,edgelibre2 : OCP.TopoDS.TopoDS_Edge) -> None:
    """
    None
    """
def ChFi3d_CircularSpine(WFirst : float,WLast : float,Pdeb : OCP.gp.gp_Pnt,Vdeb : OCP.gp.gp_Vec,Pfin : OCP.gp.gp_Pnt,Vfin : OCP.gp.gp_Vec,rad : float) -> OCP.Geom.Geom_Circle:
    """
    None
    """
def ChFi3d_Coefficient(V3d : OCP.gp.gp_Vec,D1u : OCP.gp.gp_Vec,D1v : OCP.gp.gp_Vec,DU : float,DV : float) -> None:
    """
    None
    """
def ChFi3d_ComputeArete(P1 : OCP.ChFiDS.ChFiDS_CommonPoint,UV1 : OCP.gp.gp_Pnt2d,P2 : OCP.ChFiDS.ChFiDS_CommonPoint,UV2 : OCP.gp.gp_Pnt2d,Surf : OCP.Geom.Geom_Surface,C3d : OCP.Geom.Geom_Curve,Pcurv : OCP.Geom2d.Geom2d_Curve,Pardeb : float,Parfin : float,tol3d : float,tol2d : float,tolreached : float,IFlag : int) -> None:
    """
    None
    """
def ChFi3d_ComputeCurves(S1 : OCP.Adaptor3d.Adaptor3d_HSurface,S2 : OCP.Adaptor3d.Adaptor3d_HSurface,Pardeb : OCP.TColStd.TColStd_Array1OfReal,Parfin : OCP.TColStd.TColStd_Array1OfReal,C3d : OCP.Geom.Geom_Curve,Pc1 : OCP.Geom2d.Geom2d_Curve,Pc2 : OCP.Geom2d.Geom2d_Curve,tol3d : float,tol2d : float,tolreached : float,wholeCurv : bool=True) -> bool:
    """
    None
    """
@overload
def ChFi3d_ComputePCurv(UV1 : OCP.gp.gp_Pnt2d,UV2 : OCP.gp.gp_Pnt2d,Pcurv : OCP.Geom2d.Geom2d_Curve,Pardeb : float,Parfin : float,reverse : bool=False) -> None:
    """
    None

    None

    None
    """
@overload
def ChFi3d_ComputePCurv(C3d : OCP.Adaptor3d.Adaptor3d_HCurve,UV1 : OCP.gp.gp_Pnt2d,UV2 : OCP.gp.gp_Pnt2d,Pcurv : OCP.Geom2d.Geom2d_Curve,S : OCP.Adaptor3d.Adaptor3d_HSurface,Pardeb : float,Parfin : float,tol3d : float,tolreached : float,reverse : bool=False) -> None:
    pass
@overload
def ChFi3d_ComputePCurv(C3d : OCP.Geom.Geom_Curve,UV1 : OCP.gp.gp_Pnt2d,UV2 : OCP.gp.gp_Pnt2d,Pcurv : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,Pardeb : float,Parfin : float,tol3d : float,tolreached : float,reverse : bool=False) -> None:
    pass
@overload
def ChFi3d_ComputesIntPC(Fi1 : OCP.ChFiDS.ChFiDS_FaceInterference,Fi2 : OCP.ChFiDS.ChFiDS_FaceInterference,HS1 : OCP.GeomAdaptor.GeomAdaptor_HSurface,HS2 : OCP.GeomAdaptor.GeomAdaptor_HSurface,UInt1 : float,UInt2 : float,P : OCP.gp.gp_Pnt) -> None:
    """
    None

    None
    """
@overload
def ChFi3d_ComputesIntPC(Fi1 : OCP.ChFiDS.ChFiDS_FaceInterference,Fi2 : OCP.ChFiDS.ChFiDS_FaceInterference,HS1 : OCP.GeomAdaptor.GeomAdaptor_HSurface,HS2 : OCP.GeomAdaptor.GeomAdaptor_HSurface,UInt1 : float,UInt2 : float) -> None:
    pass
def ChFi3d_ConvTol2dToTol3d(S : OCP.Adaptor3d.Adaptor3d_HSurface,tol2d : float) -> float:
    """
    None
    """
def ChFi3d_Couture(F : OCP.TopoDS.TopoDS_Face,couture : bool,edgecouture : OCP.TopoDS.TopoDS_Edge) -> None:
    """
    None
    """
def ChFi3d_CoutureOnVertex(F : OCP.TopoDS.TopoDS_Face,V : OCP.TopoDS.TopoDS_Vertex,couture : bool,edgecouture : OCP.TopoDS.TopoDS_Edge) -> None:
    """
    None
    """
def ChFi3d_EdgeFromV1(V1 : OCP.TopoDS.TopoDS_Vertex,CD : OCP.ChFiDS.ChFiDS_Stripe,sens : int) -> OCP.TopoDS.TopoDS_Edge:
    """
    None
    """
def ChFi3d_EdgeState(E : OCP.TopoDS.TopoDS_Edge,EFMap : OCP.ChFiDS.ChFiDS_Map) -> OCP.ChFiDS.ChFiDS_State:
    """
    None
    """
@overload
def ChFi3d_EnlargeBox(E : OCP.TopoDS.TopoDS_Edge,LF : OCP.TopTools.TopTools_ListOfShape,w : float,box : OCP.Bnd.Bnd_Box) -> None:
    """
    None

    None

    None

    None
    """
@overload
def ChFi3d_EnlargeBox(C : OCP.Geom.Geom_Curve,wd : float,wf : float,box1 : OCP.Bnd.Bnd_Box,box2 : OCP.Bnd.Bnd_Box) -> None:
    pass
@overload
def ChFi3d_EnlargeBox(DStr : OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure,st : OCP.ChFiDS.ChFiDS_Stripe,sd : OCP.ChFiDS.ChFiDS_SurfData,b1 : OCP.Bnd.Bnd_Box,b2 : OCP.Bnd.Bnd_Box,isfirst : bool) -> None:
    pass
@overload
def ChFi3d_EnlargeBox(S : OCP.Adaptor3d.Adaptor3d_HSurface,PC : OCP.Geom2d.Geom2d_Curve,wd : float,wf : float,box1 : OCP.Bnd.Bnd_Box,box2 : OCP.Bnd.Bnd_Box) -> None:
    pass
def ChFi3d_EvalTolReached(S1 : OCP.Adaptor3d.Adaptor3d_HSurface,pc1 : OCP.Geom2d.Geom2d_Curve,S2 : OCP.Adaptor3d.Adaptor3d_HSurface,pc2 : OCP.Geom2d.Geom2d_Curve,C : OCP.Geom.Geom_Curve) -> float:
    """
    None
    """
def ChFi3d_ExtrSpineCarac(DStr : OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure,cd : OCP.ChFiDS.ChFiDS_Stripe,i : int,p : float,jf : int,sens : int,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec,R : float) -> None:
    """
    None
    """
def ChFi3d_FilCommonPoint(SP : OCP.BRepBlend.BRepBlend_Extremity,TransLine : OCP.IntSurf.IntSurf_TypeTrans,Start : bool,CP : OCP.ChFiDS.ChFiDS_CommonPoint,Tol : float) -> None:
    """
    None
    """
def ChFi3d_FilCurveInDS(Icurv : int,Isurf : int,Pcurv : OCP.Geom2d.Geom2d_Curve,Et : OCP.TopAbs.TopAbs_Orientation) -> OCP.TopOpeBRepDS.TopOpeBRepDS_SurfaceCurveInterference:
    """
    None
    """
def ChFi3d_FilDS(SolidIndex : int,CorDat : OCP.ChFiDS.ChFiDS_Stripe,DStr : OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure,reglist : OCP.ChFiDS.ChFiDS_Regularities,tol3d : float,tol2d : float) -> None:
    """
    None
    """
def ChFi3d_FilPointInDS(Et : OCP.TopAbs.TopAbs_Orientation,Ic : int,Ip : int,Par : float,IsVertex : bool=False) -> OCP.TopOpeBRepDS.TopOpeBRepDS_CurvePointInterference:
    """
    None
    """
def ChFi3d_FilVertexInDS(Et : OCP.TopAbs.TopAbs_Orientation,Ic : int,Ip : int,Par : float) -> OCP.TopOpeBRepDS.TopOpeBRepDS_CurvePointInterference:
    """
    None
    """
def ChFi3d_IndexOfSurfData(V1 : OCP.TopoDS.TopoDS_Vertex,CD : OCP.ChFiDS.ChFiDS_Stripe,sens : int) -> int:
    """
    None
    """
def ChFi3d_IndexPointInDS(P1 : OCP.ChFiDS.ChFiDS_CommonPoint,DStr : OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure) -> int:
    """
    None
    """
def ChFi3d_IntCS(S : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve,p2dS : OCP.gp.gp_Pnt2d,wc : float) -> bool:
    """
    None
    """
def ChFi3d_IntTraces(fd1 : OCP.ChFiDS.ChFiDS_SurfData,pref1 : float,p1 : float,jf1 : int,sens1 : int,fd2 : OCP.ChFiDS.ChFiDS_SurfData,pref2 : float,p2 : float,jf2 : int,sens2 : int,RefP2d : OCP.gp.gp_Pnt2d,Check2dDistance : bool=False,enlarge : bool=False) -> bool:
    """
    None
    """
def ChFi3d_InterPlaneEdge(Plan : OCP.Adaptor3d.Adaptor3d_HSurface,C : OCP.Adaptor3d.Adaptor3d_HCurve,W : float,Sens : bool,tolc : float) -> bool:
    """
    None
    """
def ChFi3d_IsInFront(DStr : OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure,cd1 : OCP.ChFiDS.ChFiDS_Stripe,cd2 : OCP.ChFiDS.ChFiDS_Stripe,i1 : int,i2 : int,sens1 : int,sens2 : int,p1 : float,p2 : float,face : OCP.TopoDS.TopoDS_Face,sameside : bool,jf1 : int,jf2 : int,visavis : bool,Vtx : OCP.TopoDS.TopoDS_Vertex,Check2dDistance : bool=False,enlarge : bool=False) -> bool:
    """
    None
    """
def ChFi3d_IsPseudoSeam(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> bool:
    """
    None
    """
def ChFi3d_IsSmooth(C : OCP.Geom.Geom_Curve) -> bool:
    """
    None
    """
def ChFi3d_KParticular(Spine : OCP.ChFiDS.ChFiDS_Spine,IE : int,S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface) -> bool:
    """
    None
    """
def ChFi3d_NbNotDegeneratedEdges(Vtx : OCP.TopoDS.TopoDS_Vertex,VEMap : OCP.ChFiDS.ChFiDS_Map) -> int:
    """
    None
    """
def ChFi3d_NumberOfEdges(Vtx : OCP.TopoDS.TopoDS_Vertex,VEMap : OCP.ChFiDS.ChFiDS_Map) -> int:
    """
    None
    """
def ChFi3d_NumberOfSharpEdges(Vtx : OCP.TopoDS.TopoDS_Vertex,VEMap : OCP.ChFiDS.ChFiDS_Map,EFmap : OCP.ChFiDS.ChFiDS_Map) -> int:
    """
    None
    """
def ChFi3d_Parameters(S : OCP.Geom.Geom_Surface,p3d : OCP.gp.gp_Pnt,u : float,v : float) -> None:
    """
    None
    """
def ChFi3d_PerformElSpine(HES : OCP.ChFiDS.ChFiDS_HElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,continuity : OCP.GeomAbs.GeomAbs_Shape,tol : float,IsOffset : bool=False) -> None:
    """
    None
    """
def ChFi3d_ProjectPCurv(HCg : OCP.Adaptor3d.Adaptor3d_HCurve,HSg : OCP.Adaptor3d.Adaptor3d_HSurface,Pcurv : OCP.Geom2d.Geom2d_Curve,tol3d : float,tolreached : float) -> None:
    """
    None
    """
def ChFi3d_ReparamPcurv(Uf : float,Ul : float,Pcurv : OCP.Geom2d.Geom2d_Curve) -> None:
    """
    None
    """
@overload
def ChFi3d_SameParameter(C3d : OCP.Adaptor3d.Adaptor3d_HCurve,Pcurv : OCP.Geom2d.Geom2d_Curve,S : OCP.Adaptor3d.Adaptor3d_HSurface,tol3d : float,tolreached : float) -> bool:
    """
    None

    None
    """
@overload
def ChFi3d_SameParameter(C3d : OCP.Geom.Geom_Curve,Pcurv : OCP.Geom2d.Geom2d_Curve,S : OCP.Geom.Geom_Surface,Pardeb : float,Parfin : float,tol3d : float,tolreached : float) -> bool:
    pass
def ChFi3d_SearchFD(DStr : OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure,cd1 : OCP.ChFiDS.ChFiDS_Stripe,cd2 : OCP.ChFiDS.ChFiDS_Stripe,sens1 : int,sens2 : int,i1 : int,i2 : int,p1 : float,p2 : float,ind1 : int,ind2 : int,face : OCP.TopoDS.TopoDS_Face,sameside : bool,jf1 : int,jf2 : int) -> bool:
    """
    None
    """
def ChFi3d_SolidIndex(sp : OCP.ChFiDS.ChFiDS_Spine,DStr : OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure,MapESo : OCP.ChFiDS.ChFiDS_Map,MapESh : OCP.ChFiDS.ChFiDS_Map) -> int:
    """
    None
    """
def ChFi3d_Spine(pd : OCP.gp.gp_Pnt,vd : OCP.gp.gp_Vec,pf : OCP.gp.gp_Pnt,vf : OCP.gp.gp_Vec,R : float) -> OCP.Geom.Geom_BezierCurve:
    """
    None
    """
def ChFi3d_StripeEdgeInter(theStripe1 : OCP.ChFiDS.ChFiDS_Stripe,theStripe2 : OCP.ChFiDS.ChFiDS_Stripe,DStr : OCP.TopOpeBRepDS.TopOpeBRepDS_DataStructure,tol2d : float) -> None:
    """
    None
    """
def ChFi3d_TrimCurve(gc : OCP.Geom.Geom_Curve,FirstP : OCP.gp.gp_Pnt,LastP : OCP.gp.gp_Pnt,gtc : OCP.Geom.Geom_TrimmedCurve) -> None:
    """
    None
    """
def ChFi3d_TrsfTrans(T1 : OCP.IntSurf.IntSurf_TypeTrans) -> OCP.TopAbs.TopAbs_Orientation:
    """
    None
    """
def ChFi3d_cherche_edge(V : OCP.TopoDS.TopoDS_Vertex,E1 : OCP.TopTools.TopTools_Array1OfShape,F1 : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge,Vtx : OCP.TopoDS.TopoDS_Vertex) -> None:
    """
    None
    """
def ChFi3d_cherche_element(V : OCP.TopoDS.TopoDS_Vertex,E1 : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge,Vtx : OCP.TopoDS.TopoDS_Vertex) -> None:
    """
    None
    """
def ChFi3d_cherche_face1(map : OCP.TopTools.TopTools_ListOfShape,F1 : OCP.TopoDS.TopoDS_Face,F : OCP.TopoDS.TopoDS_Face) -> None:
    """
    None
    """
def ChFi3d_cherche_vertex(E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,vertex : OCP.TopoDS.TopoDS_Vertex,trouve : bool) -> None:
    """
    None
    """
def ChFi3d_conexfaces(E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,EFMap : OCP.ChFiDS.ChFiDS_Map) -> None:
    """
    None
    """
def ChFi3d_edge_common_faces(mapEF : OCP.TopTools.TopTools_ListOfShape,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> None:
    """
    None
    """
def ChFi3d_evalconti(E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape:
    """
    None
    """
@overload
def ChFi3d_mkbound(s : OCP.Geom.Geom_Surface,p1 : OCP.gp.gp_Pnt2d,p2 : OCP.gp.gp_Pnt2d,t3d : float,ta : float,isfreeboundary : bool=False) -> OCP.GeomFill.GeomFill_Boundary:
    """
    None

    None

    None

    None

    None

    None
    """
@overload
def ChFi3d_mkbound(Surf : OCP.Adaptor3d.Adaptor3d_HSurface,curv : OCP.Geom2d.Geom2d_Curve,sens1 : int,p1 : OCP.gp.gp_Pnt2d,v1 : OCP.gp.gp_Vec,sens2 : int,p2 : OCP.gp.gp_Pnt2d,v2 : OCP.gp.gp_Vec,t3d : float,ta : float) -> OCP.GeomFill.GeomFill_Boundary:
    pass
@overload
def ChFi3d_mkbound(HS : OCP.Adaptor3d.Adaptor3d_HSurface,curv : OCP.Geom2d.Geom2d_Curve,t3d : float,ta : float,isfreeboundary : bool=False) -> OCP.GeomFill.GeomFill_Boundary:
    pass
@overload
def ChFi3d_mkbound(Fac : OCP.Adaptor3d.Adaptor3d_HSurface,curv : OCP.Geom2d.Geom2d_Curve,p1 : OCP.gp.gp_Pnt2d,p2 : OCP.gp.gp_Pnt2d,t3d : float,ta : float,isfreeboundary : bool=False) -> OCP.GeomFill.GeomFill_Boundary:
    pass
@overload
def ChFi3d_mkbound(HS : OCP.Adaptor3d.Adaptor3d_HSurface,p1 : OCP.gp.gp_Pnt2d,p2 : OCP.gp.gp_Pnt2d,t3d : float,ta : float,isfreeboundary : bool=False) -> OCP.GeomFill.GeomFill_Boundary:
    pass
@overload
def ChFi3d_mkbound(Fac : OCP.Adaptor3d.Adaptor3d_HSurface,curv : OCP.Geom2d.Geom2d_Curve,sens1 : int,pfac1 : OCP.gp.gp_Pnt2d,vfac1 : OCP.gp.gp_Vec2d,sens2 : int,pfac2 : OCP.gp.gp_Pnt2d,vfac2 : OCP.gp.gp_Vec2d,t3d : float,ta : float) -> OCP.GeomFill.GeomFill_Boundary:
    pass
def ChFi3d_nbface(mapVF : OCP.TopTools.TopTools_ListOfShape) -> int:
    """
    None
    """
ChFi3d_Polynomial: OCP.ChFi3d.ChFi3d_FilletShape # value = <ChFi3d_FilletShape.ChFi3d_Polynomial: 2>
ChFi3d_QuasiAngular: OCP.ChFi3d.ChFi3d_FilletShape # value = <ChFi3d_FilletShape.ChFi3d_QuasiAngular: 1>
ChFi3d_Rational: OCP.ChFi3d.ChFi3d_FilletShape # value = <ChFi3d_FilletShape.ChFi3d_Rational: 0>
