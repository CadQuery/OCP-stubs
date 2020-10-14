import OCP.FilletSurf
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.GeomAbs
import OCP.Geom2d
import OCP.Law
import OCP.TopTools
import OCP.TopOpeBRepBuild
import OCP.ChFi3d
import OCP.Adaptor3d
import OCP.TopoDS
import OCP.ChFiDS
import OCP.Geom
import OCP.gp
__all__  = [
"FilletSurf_Builder",
"FilletSurf_ErrorTypeStatus",
"FilletSurf_InternalBuilder",
"FilletSurf_StatusDone",
"FilletSurf_StatusType",
"FilletSurf_EdgeNotG1",
"FilletSurf_EdgeNotOnShape",
"FilletSurf_EmptyList",
"FilletSurf_FacesNotG1",
"FilletSurf_IsNotOk",
"FilletSurf_IsOk",
"FilletSurf_IsPartial",
"FilletSurf_NoExtremityOnEdge",
"FilletSurf_NotSharpEdge",
"FilletSurf_OneExtremityOnEdge",
"FilletSurf_PbFilletCompute",
"FilletSurf_TwoExtremityOnEdge"
]
class FilletSurf_Builder():
    """
    API giving the following geometric information about fillets list of corresponding NUBS surfaces for each surface: the 2 support faces on each face: the 3d curve and the corresponding 2d curve the 2d curves on the fillet status of start and end section of the fillet first and last parameter on edge of the fillet.
    """
    def CurveOnFace1(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        gives the 3d curve of SurfaceFillet(Index) on SupportFace1(Index)
        """
    def CurveOnFace2(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        gives the 3d curve of SurfaceFillet(Index) on SupportFace2(Index)
        """
    def EndSectionStatus(self) -> FilletSurf_StatusType: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        gives the parameter of the fillet on the first edge.
        """
    def IsDone(self) -> FilletSurf_StatusDone: 
        """
        gives the status about the computation of the fillet returns: IsOK :no problem during the computation IsNotOk: no result is produced IsPartial: the result is partial
        """
    def LastParameter(self) -> float: 
        """
        gives the parameter of the fillet on the last edge
        """
    def NbSection(self,IndexSurf : int) -> int: 
        """
        None
        """
    def NbSurface(self) -> int: 
        """
        gives the number of NUBS surfaces of the Fillet.
        """
    def PCurve1OnFillet(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        gives the PCurve associated to CurveOnFace1(Index) on the Fillet
        """
    def PCurve2OnFillet(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        gives the PCurve associated to CurveOnSup2(Index) on the fillet
        """
    def PCurveOnFace1(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        gives the PCurve associated to CurvOnSup1(Index) on the support face
        """
    def PCurveOnFace2(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        gives the PCurve associated to CurveOnSup2(Index) on the support face
        """
    def Perform(self) -> None: 
        """
        ---Purpose computation of the fillet (list of NUBS)
        """
    def Section(self,IndexSurf : int,IndexSec : int,Circ : OCP.Geom.Geom_TrimmedCurve) -> Any: 
        """
        None
        """
    def Simulate(self) -> None: 
        """
        None
        """
    def StartSectionStatus(self) -> FilletSurf_StatusType: 
        """
        None
        """
    def StatusError(self) -> FilletSurf_ErrorTypeStatus: 
        """
        gives informations about error status if IsDone=IsNotOk returns EdgeNotG1: the edges are not G1 FacesNotG1 : two connected faces on a same support are not G1 EdgeNotOnShape: the edge is not on shape NotSharpEdge: the edge is not sharp PbFilletCompute: problem during the computation of the fillet
        """
    def SupportFace1(self,Index : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        gives the first support face relative to SurfaceFillet(Index);
        """
    def SupportFace2(self,Index : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        gives the second support face relative to SurfaceFillet(Index);
        """
    def SurfaceFillet(self,Index : int) -> OCP.Geom.Geom_Surface: 
        """
        gives the NUBS surface of index Index.
        """
    def TolApp3d(self,Index : int) -> float: 
        """
        gives the 3d tolerance reached during approximation of surface of index Index
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,E : OCP.TopTools.TopTools_ListOfShape,R : float,Ta : float=0.01,Tapp3d : float=0.0001,Tapp2d : float=1e-05) -> None: ...
    pass
class FilletSurf_ErrorTypeStatus():
    """
    None

    Members:

      FilletSurf_EmptyList

      FilletSurf_EdgeNotG1

      FilletSurf_FacesNotG1

      FilletSurf_EdgeNotOnShape

      FilletSurf_NotSharpEdge

      FilletSurf_PbFilletCompute
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
    FilletSurf_EdgeNotG1: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotG1
    FilletSurf_EdgeNotOnShape: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotOnShape
    FilletSurf_EmptyList: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_EmptyList
    FilletSurf_FacesNotG1: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_FacesNotG1
    FilletSurf_NotSharpEdge: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_NotSharpEdge
    FilletSurf_PbFilletCompute: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_PbFilletCompute
    __entries: dict # value = {'FilletSurf_EmptyList': (FilletSurf_ErrorTypeStatus.FilletSurf_EmptyList, None), 'FilletSurf_EdgeNotG1': (FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotG1, None), 'FilletSurf_FacesNotG1': (FilletSurf_ErrorTypeStatus.FilletSurf_FacesNotG1, None), 'FilletSurf_EdgeNotOnShape': (FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotOnShape, None), 'FilletSurf_NotSharpEdge': (FilletSurf_ErrorTypeStatus.FilletSurf_NotSharpEdge, None), 'FilletSurf_PbFilletCompute': (FilletSurf_ErrorTypeStatus.FilletSurf_PbFilletCompute, None)}
    __members__: dict # value = {'FilletSurf_EmptyList': FilletSurf_ErrorTypeStatus.FilletSurf_EmptyList, 'FilletSurf_EdgeNotG1': FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotG1, 'FilletSurf_FacesNotG1': FilletSurf_ErrorTypeStatus.FilletSurf_FacesNotG1, 'FilletSurf_EdgeNotOnShape': FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotOnShape, 'FilletSurf_NotSharpEdge': FilletSurf_ErrorTypeStatus.FilletSurf_NotSharpEdge, 'FilletSurf_PbFilletCompute': FilletSurf_ErrorTypeStatus.FilletSurf_PbFilletCompute}
    pass
class FilletSurf_InternalBuilder(OCP.ChFi3d.ChFi3d_FilBuilder, OCP.ChFi3d.ChFi3d_Builder):
    """
    This class is private. It is used by the class Builder from FilletSurf. It computes geometric information about fillets.
    """
    def Abscissa(self,IC : int,V : OCP.TopoDS.TopoDS_Vertex) -> float: 
        """
        returns the abscissa of the vertex V on the contour of index IC.
        """
    def Add(self,E : OCP.TopTools.TopTools_ListOfShape,R : float) -> int: 
        """
        Initializes the contour with a list of Edges 0 : no problem 1 : empty list 2 : the edges are not G1 3 : two connected faces on a same support are not G1 4 : the edge is not on shape 5 : NotSharpEdge: the edge is not sharp
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
    def CurveOnFace1(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        gives the 3d curve of SurfaceFillet(Index) on SupportFace1(Index)
        """
    def CurveOnFace2(self,Index : int) -> OCP.Geom.Geom_Curve: 
        """
        gives the 3d curve of SurfaceFillet(Index) on SupportFace2(Index)
        """
    def Done(self) -> bool: 
        """
        None
        """
    def EndSectionStatus(self) -> FilletSurf_StatusType: 
        """
        None
        """
    def FaultyContour(self,I : int) -> int: 
        """
        Returns the number of I'th contour on which the calculation has failed.
        """
    def FaultyVertex(self,IV : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns the IV'th vertex on which the calculation has failed.
        """
    def FirstParameter(self) -> float: 
        """
        gives the parameter of the fillet on the first edge.
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
    def GetFilletShape(self) -> OCP.ChFi3d.ChFi3d_FilletShape: 
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
    def LastParameter(self) -> float: 
        """
        gives the parameter of the fillet on the last edge
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
    def NbSection(self,IndexSurf : int) -> int: 
        """
        None
        """
    def NbSurf(self,IC : int) -> int: 
        """
        None
        """
    def NbSurface(self) -> int: 
        """
        gives the number of NUBS surfaces of the Fillet.
        """
    def PCurve1OnFillet(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        gives the PCurve associated to CurveOnFace1(Index) on the Fillet
        """
    def PCurve2OnFillet(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        gives the PCurve associated to CurveOnSup2(Index) on the fillet
        """
    def PCurveOnFace1(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        gives the PCurve associated to CurvOnSup1(Index) on the support face
        """
    def PCurveOnFace2(self,Index : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        gives the PCurve associated to CurveOnSup2(Index) on the support face
        """
    def Perform(self) -> None: 
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
    def Section(self,IndexSurf : int,IndexSec : int,Circ : OCP.Geom.Geom_TrimmedCurve) -> Any: 
        """
        None
        """
    def SetContinuity(self,InternalContinuity : OCP.GeomAbs.GeomAbs_Shape,AngularTolerance : float) -> None: 
        """
        None
        """
    def SetFilletShape(self,FShape : OCP.ChFi3d.ChFi3d_FilletShape) -> None: 
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
    def Simulate(self) -> None: 
        """
        None
        """
    def SplitKPart(self,Data : OCP.ChFiDS.ChFiDS_SurfData,SetData : OCP.ChFiDS.ChFiDS_SequenceOfSurfData,Spine : OCP.ChFiDS.ChFiDS_Spine,Iedge : int,S1 : OCP.Adaptor3d.Adaptor3d_HSurface,I1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_HSurface,I2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Intf : bool,Intl : bool) -> bool: 
        """
        Method, implemented in the inheritants, calculates the elements of construction of the surface (fillet or chamfer).
        """
    def StartSectionStatus(self) -> FilletSurf_StatusType: 
        """
        None
        """
    def StripeStatus(self,IC : int) -> OCP.ChFiDS.ChFiDS_ErrorStatus: 
        """
        for the stripe IC ,indication on the cause of failure WalkingFailure,TwistedSurface,Error, Ok
        """
    def SupportFace1(self,Index : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        gives the first support face relative to SurfaceFillet(Index);
        """
    def SupportFace2(self,Index : int) -> OCP.TopoDS.TopoDS_Face: 
        """
        gives the second support face relative to SurfaceFillet(Index);
        """
    def SurfaceFillet(self,Index : int) -> OCP.Geom.Geom_Surface: 
        """
        gives the NUBS surface of index Index.
        """
    def TolApp3d(self,Index : int) -> float: 
        """
        gives the 3d tolerance reached during approximation of the surface of index Index
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
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,FShape : OCP.ChFi3d.ChFi3d_FilletShape=ChFi3d_FilletShape.ChFi3d_Polynomial,Ta : float=0.01,Tapp3d : float=0.0001,Tapp2d : float=1e-05) -> None: ...
    pass
class FilletSurf_StatusDone():
    """
    None

    Members:

      FilletSurf_IsOk

      FilletSurf_IsNotOk

      FilletSurf_IsPartial
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
    FilletSurf_IsNotOk: OCP.FilletSurf.FilletSurf_StatusDone # value = FilletSurf_StatusDone.FilletSurf_IsNotOk
    FilletSurf_IsOk: OCP.FilletSurf.FilletSurf_StatusDone # value = FilletSurf_StatusDone.FilletSurf_IsOk
    FilletSurf_IsPartial: OCP.FilletSurf.FilletSurf_StatusDone # value = FilletSurf_StatusDone.FilletSurf_IsPartial
    __entries: dict # value = {'FilletSurf_IsOk': (FilletSurf_StatusDone.FilletSurf_IsOk, None), 'FilletSurf_IsNotOk': (FilletSurf_StatusDone.FilletSurf_IsNotOk, None), 'FilletSurf_IsPartial': (FilletSurf_StatusDone.FilletSurf_IsPartial, None)}
    __members__: dict # value = {'FilletSurf_IsOk': FilletSurf_StatusDone.FilletSurf_IsOk, 'FilletSurf_IsNotOk': FilletSurf_StatusDone.FilletSurf_IsNotOk, 'FilletSurf_IsPartial': FilletSurf_StatusDone.FilletSurf_IsPartial}
    pass
class FilletSurf_StatusType():
    """
    None

    Members:

      FilletSurf_TwoExtremityOnEdge

      FilletSurf_OneExtremityOnEdge

      FilletSurf_NoExtremityOnEdge
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
    FilletSurf_NoExtremityOnEdge: OCP.FilletSurf.FilletSurf_StatusType # value = FilletSurf_StatusType.FilletSurf_NoExtremityOnEdge
    FilletSurf_OneExtremityOnEdge: OCP.FilletSurf.FilletSurf_StatusType # value = FilletSurf_StatusType.FilletSurf_OneExtremityOnEdge
    FilletSurf_TwoExtremityOnEdge: OCP.FilletSurf.FilletSurf_StatusType # value = FilletSurf_StatusType.FilletSurf_TwoExtremityOnEdge
    __entries: dict # value = {'FilletSurf_TwoExtremityOnEdge': (FilletSurf_StatusType.FilletSurf_TwoExtremityOnEdge, None), 'FilletSurf_OneExtremityOnEdge': (FilletSurf_StatusType.FilletSurf_OneExtremityOnEdge, None), 'FilletSurf_NoExtremityOnEdge': (FilletSurf_StatusType.FilletSurf_NoExtremityOnEdge, None)}
    __members__: dict # value = {'FilletSurf_TwoExtremityOnEdge': FilletSurf_StatusType.FilletSurf_TwoExtremityOnEdge, 'FilletSurf_OneExtremityOnEdge': FilletSurf_StatusType.FilletSurf_OneExtremityOnEdge, 'FilletSurf_NoExtremityOnEdge': FilletSurf_StatusType.FilletSurf_NoExtremityOnEdge}
    pass
FilletSurf_EdgeNotG1: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotG1
FilletSurf_EdgeNotOnShape: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_EdgeNotOnShape
FilletSurf_EmptyList: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_EmptyList
FilletSurf_FacesNotG1: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_FacesNotG1
FilletSurf_IsNotOk: OCP.FilletSurf.FilletSurf_StatusDone # value = FilletSurf_StatusDone.FilletSurf_IsNotOk
FilletSurf_IsOk: OCP.FilletSurf.FilletSurf_StatusDone # value = FilletSurf_StatusDone.FilletSurf_IsOk
FilletSurf_IsPartial: OCP.FilletSurf.FilletSurf_StatusDone # value = FilletSurf_StatusDone.FilletSurf_IsPartial
FilletSurf_NoExtremityOnEdge: OCP.FilletSurf.FilletSurf_StatusType # value = FilletSurf_StatusType.FilletSurf_NoExtremityOnEdge
FilletSurf_NotSharpEdge: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_NotSharpEdge
FilletSurf_OneExtremityOnEdge: OCP.FilletSurf.FilletSurf_StatusType # value = FilletSurf_StatusType.FilletSurf_OneExtremityOnEdge
FilletSurf_PbFilletCompute: OCP.FilletSurf.FilletSurf_ErrorTypeStatus # value = FilletSurf_ErrorTypeStatus.FilletSurf_PbFilletCompute
FilletSurf_TwoExtremityOnEdge: OCP.FilletSurf.FilletSurf_StatusType # value = FilletSurf_StatusType.FilletSurf_TwoExtremityOnEdge
