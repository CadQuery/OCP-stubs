import OCP.ChFi3d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.math
import OCP.BRepAdaptor
import OCP.Geom
import OCP.Law
import OCP.Adaptor3d
import OCP.ChFiDS
import OCP.TopoDS
import OCP.BRepBlend
import OCP.TopAbs
import OCP.gp
import OCP.GeomAbs
import OCP.TopTools
import OCP.TopOpeBRepBuild
import OCP.IntSurf
__all__  = [
"ChFi3d",
"ChFi3d_Builder",
"ChFi3d_ChBuilder",
"ChFi3d_FilBuilder",
"ChFi3d_FilletShape",
"ChFi3d_SearchSing",
"ChFi3d_FilCommonPoint",
"ChFi3d_PerformElSpine",
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
    @overload
    def IsTangentFaces_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace1 : OCP.TopoDS.TopoDS_Face,theFace2 : OCP.TopoDS.TopoDS_Face,Order : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_G1) -> bool: 
        """
        Returns true if theEdge between theFace1 and theFace2 is tangent

        None
        """
    @staticmethod
    @overload
    def IsTangentFaces_s(theEdge : OCP.TopoDS.TopoDS_Edge,theFace1 : OCP.TopoDS.TopoDS_Face,theFace2 : OCP.TopoDS.TopoDS_Face,G1Tol : float,Order : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_G1) -> bool: ...
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
        Reset all results of compute and returns the algorithm in the state of the last acquisition to enable modification of contours or areas.
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
    def SplitKPart(self,Data : OCP.ChFiDS.ChFiDS_SurfData,SetData : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Spine : OCP.ChFiDS.ChFiDS_Spine,Iedge : int,S1 : OCP.Adaptor3d.Adaptor3d_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Intf : bool,Intl : bool) -> bool: 
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
    def Add(self,Dis : float,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        initializes a contour with the edge <E> as first (the next are found by propagation ). The two distances (parameters of the chamfer) must be set after. if the edge <E> has more than 2 adjacent faces

        initializes a new contour with the edge <E> as first (the next are found by propagation ), and the distance <Dis> if the edge <E> has more than 2 adjacent faces

        initializes a new contour with the edge <E> as first (the next are found by propagation ), and the distance <Dis1> and <Dis2> if the edge <E> has more than 2 adjacent faces
        """
    @overload
    def Add(self,Dis1 : float,Dis2 : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
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
    def PerformSurf(self,Data : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Guide : OCP.ChFiDS.ChFiDS_ElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC1 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Sref1 : OCP.BRepAdaptor.BRepAdaptor_Surface,PCref1 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Or2 : OCP.TopAbs.TopAbs_Orientation,MaxStep : float,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP : bool,RecS : bool,RecRst : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, float, float]: 
        """
        Methode, implemented in inheritants, calculates the elements of construction of the surface (fillet or chamfer).

        Method, implemented in the inheritants, calculates the elements of construction of the surface (fillet or chamfer) contact edge/face.

        Method, implemented in inheritants, calculates the elements of construction of the surface (fillet or chamfer) contact edge/face.

        Method, implemented in inheritants, calculates the elements of construction of the surface (fillet or chamfer) contact edge/edge.
        """
    @overload
    def PerformSurf(self,Data : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Guide : OCP.ChFiDS.ChFiDS_ElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Or1 : OCP.TopAbs.TopAbs_Orientation,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC2 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Sref2 : OCP.BRepAdaptor.BRepAdaptor_Surface,PCref2 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,MaxStep : float,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP : bool,RecS : bool,RecRst : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, float, float]: ...
    @overload
    def PerformSurf(self,Data : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Guide : OCP.ChFiDS.ChFiDS_ElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC1 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Sref1 : OCP.BRepAdaptor.BRepAdaptor_Surface,PCref1 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Or1 : OCP.TopAbs.TopAbs_Orientation,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC2 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Sref2 : OCP.BRepAdaptor.BRepAdaptor_Surface,PCref2 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Or2 : OCP.TopAbs.TopAbs_Orientation,MaxStep : float,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP1 : bool,RecRst1 : bool,RecP2 : bool,RecRst2 : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, bool, float, float]: ...
    @overload
    def PerformSurf(self,Data : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Guide : OCP.ChFiDS.ChFiDS_ElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,MaxStep : float,Fleche : float,TolGuide : float,First : float,Last : float,Inside : bool,Appro : bool,Forward : bool,RecOnS1 : bool,RecOnS2 : bool,Soldep : OCP.math.math_Vector,Intf : int,Intl : int) -> bool: ...
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
        Reset all results of compute and returns the algorithm in the state of the last acquisition to enable modification of contours or areas.
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
    def SimulSurf(self,Data : OCP.ChFiDS.ChFiDS_SurfData,Guide : OCP.ChFiDS.ChFiDS_ElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Or1 : OCP.TopAbs.TopAbs_Orientation,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC2 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Sref2 : OCP.BRepAdaptor.BRepAdaptor_Surface,PCref2 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP : bool,RecS : bool,RecRst : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, float, float]: 
        """
        None

        None

        None
        """
    @overload
    def SimulSurf(self,Data : OCP.ChFiDS.ChFiDS_SurfData,Guide : OCP.ChFiDS.ChFiDS_ElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC1 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Sref1 : OCP.BRepAdaptor.BRepAdaptor_Surface,PCref1 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Or1 : OCP.TopAbs.TopAbs_Orientation,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC2 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Sref2 : OCP.BRepAdaptor.BRepAdaptor_Surface,PCref2 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Or2 : OCP.TopAbs.TopAbs_Orientation,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP1 : bool,RecRst1 : bool,RecP2 : bool,RecRst2 : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, bool, float, float]: ...
    @overload
    def SimulSurf(self,Data : OCP.ChFiDS.ChFiDS_SurfData,Guide : OCP.ChFiDS.ChFiDS_ElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,Choix : int,S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,PC1 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,Sref1 : OCP.BRepAdaptor.BRepAdaptor_Surface,PCref1 : OCP.BRepAdaptor.BRepAdaptor_Curve2d,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Or2 : OCP.TopAbs.TopAbs_Orientation,Fleche : float,TolGuide : float,Inside : bool,Appro : bool,Forward : bool,RecP : bool,RecS : bool,RecRst : bool,Soldep : OCP.math.math_Vector) -> Tuple[bool, float, float]: ...
    def Simulate(self,IC : int) -> None: 
        """
        None
        """
    def SplitKPart(self,Data : OCP.ChFiDS.ChFiDS_SurfData,SetData : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Spine : OCP.ChFiDS.ChFiDS_Spine,Iedge : int,S1 : OCP.Adaptor3d.Adaptor3d_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Intf : bool,Intl : bool) -> bool: 
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
    def Add(self,Radius : float,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        initialisation of a contour with the first edge (the following are found by propagation). Attention, you need to start with SetRadius.

        initialisation of the constant vector the corresponding 1st edge.
        """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
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
        Returns true the contour is flagged as edge constant.

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
    def Radius(self,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> float: 
        """
        Returns the vector if the contour is flagged as edge constant.

        Returns the vector if E is flagged as edge constant.
        """
    @overload
    def Radius(self,IC : int) -> float: ...
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
        Reset all results of compute and returns the algorithm in the state of the last acquisition to enable modification of contours or areas.
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
    def SetRadius(self,Radius : float,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Set the radius of the contour of index IC.

        Set a constant on edge E of the contour of index IC. Since then E is flagged as constant.

        Set a vector on vertex V of the contour of index IC.

        Set a vertex on the point of parametre U in the edge IinC of the contour of index IC
        """
    @overload
    def SetRadius(self,Radius : float,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
    @overload
    def SetRadius(self,UandR : OCP.gp.gp_XY,IC : int,IinC : int) -> None: ...
    @overload
    def SetRadius(self,C : OCP.Law.Law_Function,IC : int,IinC : int) -> None: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        if (Isdone()) makes the result. if (!Isdone())
        """
    def Simulate(self,IC : int) -> None: 
        """
        None
        """
    def SplitKPart(self,Data : OCP.ChFiDS.ChFiDS_SurfData,SetData : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Spine : OCP.ChFiDS.ChFiDS_Spine,Iedge : int,S1 : OCP.Adaptor3d.Adaptor3d_Surface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Intf : bool,Intl : bool) -> bool: 
        """
        Method, implemented in the inheritants, calculates the elements of construction of the surface (fillet or chamfer).
        """
    def StripeStatus(self,IC : int) -> OCP.ChFiDS.ChFiDS_ErrorStatus: 
        """
        for the stripe IC ,indication on the cause of failure WalkingFailure,TwistedSurface,Error, Ok
        """
    @overload
    def UnSet(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Extracts the flag constant and the vector of edge E.

        Extracts the vector of the vertex V.
        """
    @overload
    def UnSet(self,IC : int,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
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
def ChFi3d_FilCommonPoint(SP : OCP.BRepBlend.BRepBlend_Extremity,TransLine : OCP.IntSurf.IntSurf_TypeTrans,Start : bool,CP : OCP.ChFiDS.ChFiDS_CommonPoint,Tol : float) -> None:
    """
    None
    """
def ChFi3d_PerformElSpine(HES : OCP.ChFiDS.ChFiDS_ElSpine,Spine : OCP.ChFiDS.ChFiDS_Spine,continuity : OCP.GeomAbs.GeomAbs_Shape,tol : float,IsOffset : bool=False) -> None:
    """
    None
    """
ChFi3d_Polynomial: OCP.ChFi3d.ChFi3d_FilletShape # value = <ChFi3d_FilletShape.ChFi3d_Polynomial: 2>
ChFi3d_QuasiAngular: OCP.ChFi3d.ChFi3d_FilletShape # value = <ChFi3d_FilletShape.ChFi3d_QuasiAngular: 1>
ChFi3d_Rational: OCP.ChFi3d.ChFi3d_FilletShape # value = <ChFi3d_FilletShape.ChFi3d_Rational: 0>
