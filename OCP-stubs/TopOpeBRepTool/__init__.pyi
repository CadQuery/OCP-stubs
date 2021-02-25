import OCP.TopOpeBRepTool
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.GeomAdaptor
import OCP.NCollection
import OCP.Geom
import OCP.TColgp
import OCP.TopoDS
import OCP.Bnd
import OCP.TopExp
import OCP.BRepAdaptor
import OCP.Standard
import OCP.TopAbs
import OCP.TopTools
import OCP.Extrema
import io
import OCP.gp
import OCP.GeomAbs
import OCP.Geom2d
__all__  = [
"TopOpeBRepTool",
"TopOpeBRepTool_AncestorsTool",
"TopOpeBRepTool_BoxSort",
"TopOpeBRepTool_C2DF",
"TopOpeBRepTool_CLASSI",
"TopOpeBRepTool_CORRISO",
"TopOpeBRepTool_CurveTool",
"TopOpeBRepTool_DataMapOfOrientedShapeC2DF",
"TopOpeBRepTool_DataMapOfShapeListOfC2DF",
"TopOpeBRepTool_DataMapOfShapeface",
"TopOpeBRepTool_FuseEdges",
"TopOpeBRepTool_GeomTool",
"TopOpeBRepTool_HBoxTool",
"TopOpeBRepTool_IndexedDataMapOfShapeBox",
"TopOpeBRepTool_IndexedDataMapOfShapeBox2d",
"TopOpeBRepTool_IndexedDataMapOfShapeconnexity",
"TopOpeBRepTool_ListOfC2DF",
"TopOpeBRepTool_OutCurveType",
"TopOpeBRepTool_PurgeInternalEdges",
"TopOpeBRepTool_REGUS",
"TopOpeBRepTool_REGUW",
"TopOpeBRepTool_ShapeClassifier",
"TopOpeBRepTool_ShapeExplorer",
"TopOpeBRepTool_ShapeTool",
"TopOpeBRepTool_SolidClassifier",
"TopOpeBRepTool_TOOL",
"TopOpeBRepTool_connexity",
"TopOpeBRepTool_face",
"TopOpeBRepTool_makeTransition",
"TopOpeBRepTool_mkTondgE",
"BASISCURVE2D",
"FBOX_Box",
"FBOX_GetHBoxTool",
"FBOX_Prepare",
"FC2D_AddNewCurveOnSurface",
"FC2D_CurveOnSurface",
"FC2D_EditableCurveOnSurface",
"FC2D_HasC3D",
"FC2D_HasCurveOnSurface",
"FC2D_HasNewCurveOnSurface",
"FC2D_HasOldCurveOnSurface",
"FC2D_MakeCurveOnSurface",
"FC2D_Prepare",
"FSC_GetPSC",
"FSC_StateEonFace",
"FSC_StatePonFace",
"FTOL_FaceTolerances",
"FTOL_FaceTolerances2d",
"FTOL_FaceTolerances3d",
"FUN_ds_CopyEdge",
"FUN_ds_Parameter",
"FUN_nearestISO",
"FUN_quadCT",
"FUN_tool_ClosingE",
"FUN_tool_EboundF",
"FUN_tool_EitangenttoFe",
"FUN_tool_Eshared",
"FUN_tool_EtgF",
"FUN_tool_EtgOOE",
"FUN_tool_IsClosingE",
"FUN_tool_MakeWire",
"FUN_tool_PinC",
"FUN_tool_SameOri",
"FUN_tool_UpdateBnd2d",
"FUN_tool_bounds",
"FUN_tool_closed",
"FUN_tool_closedS",
"FUN_tool_comparebndkole",
"FUN_tool_curvesSO",
"FUN_tool_cylinder",
"FUN_tool_dirC",
"FUN_tool_direct",
"FUN_tool_findAncestor",
"FUN_tool_findPinBAC",
"FUN_tool_findPinE",
"FUN_tool_findparinBAC",
"FUN_tool_findparinE",
"FUN_tool_geombounds",
"FUN_tool_getdxx",
"FUN_tool_getgeomxx",
"FUN_tool_getindex",
"FUN_tool_getxx",
"FUN_tool_haspc",
"FUN_tool_inS",
"FUN_tool_isobounds",
"FUN_tool_line",
"FUN_tool_maxtol",
"FUN_tool_mkBnd2d",
"FUN_tool_nC2dINSIDES",
"FUN_tool_nCinsideS",
"FUN_tool_nbshapes",
"FUN_tool_ngS",
"FUN_tool_nggeomF",
"FUN_tool_onapex",
"FUN_tool_orientEinF",
"FUN_tool_orientEinFFORWARD",
"FUN_tool_orientVinE",
"FUN_tool_outbounds",
"FUN_tool_parE",
"FUN_tool_parF",
"FUN_tool_parVonE",
"FUN_tool_paronEF",
"FUN_tool_pcurveonF",
"FUN_tool_plane",
"FUN_tool_projPonC",
"FUN_tool_projPonC2D",
"FUN_tool_projPonE",
"FUN_tool_projPonF",
"FUN_tool_projPonS",
"FUN_tool_projPonboundedF",
"FUN_tool_quad",
"FUN_tool_shapes",
"FUN_tool_staPinE",
"FUN_tool_tggeomE",
"FUN_tool_tolUV",
"FUN_tool_typ",
"FUN_tool_value",
"TopOpeBRepTool_APPROX",
"TopOpeBRepTool_BSPLINE1",
"TopOpeBRepTool_INTERPOL"
]
class TopOpeBRepTool():
    """
    This package provides services used by the TopOpeBRep package performing topological operations on the BRep data structure.
    """
    @staticmethod
    def CorrectONUVISO_s(F : OCP.TopoDS.TopoDS_Face,Fsp : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    @staticmethod
    def MakeFaces_s(F : OCP.TopoDS.TopoDS_Face,LOF : OCP.TopTools.TopTools_ListOfShape,MshNOK : OCP.TopTools.TopTools_IndexedMapOfOrientedShape,LOFF : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        Builds up the correct list of faces <LOFF> from <LOF>, using faulty shapes from map <MshNOK>. <LOF> is the list of <F>'s descendant faces. returns false if building fails
        """
    @staticmethod
    def Print_s(OCT : TopOpeBRepTool_OutCurveType,S : io.BytesIO) -> io.BytesIO: 
        """
        Prints <OCT> as string on stream <S>; returns <S>.
        """
    @staticmethod
    @overload
    def PurgeClosingEdges_s(F : OCP.TopoDS.TopoDS_Face,LOF : OCP.TopTools.TopTools_ListOfShape,MWisOld : OCP.TopTools.TopTools_DataMapOfShapeInteger,MshNOK : OCP.TopTools.TopTools_IndexedMapOfOrientedShape) -> bool: 
        """
        Fuse edges (in a wire) of a shape where we have useless vertex. In case face <FF> is built on UV-non-connexed wires (with the two closing edges FORWARD and REVERSED, in spite of one only), we find out the faulty edge, add the faulty shapes (edge,wire,face) to <MshNOK>. <FF> is a face descendant of <F>. <MWisOld>(wire) = 1 if wire is wire of <F> 0 wire results from <F>'s wire splitted. returns false if purge fails

        None
        """
    @staticmethod
    @overload
    def PurgeClosingEdges_s(F : OCP.TopoDS.TopoDS_Face,FF : OCP.TopoDS.TopoDS_Face,MWisOld : OCP.TopTools.TopTools_DataMapOfShapeInteger,MshNOK : OCP.TopTools.TopTools_IndexedMapOfOrientedShape) -> bool: ...
    @staticmethod
    def RegularizeFace_s(aFace : OCP.TopoDS.TopoDS_Face,OldWiresnewWires : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,aListOfFaces : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        Classify wire's splits of map <OldWiresnewWires> in order to compute <aListOfFaces>, the splits of <aFace>.
        """
    @staticmethod
    def RegularizeShells_s(aSolid : OCP.TopoDS.TopoDS_Solid,OldSheNewShe : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,FSplits : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> bool: 
        """
        Returns <False> if the shell is valid (the solid is a set of faces connexed by edges with connexity 2). Else, splits faces of the shell; <OldFacesnewFaces> describes (face, splits of face).
        """
    @staticmethod
    def RegularizeWires_s(aFace : OCP.TopoDS.TopoDS_Face,OldWiresNewWires : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,ESplits : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> bool: 
        """
        Returns <False> if the face is valid (the UV representation of the face is a set of pcurves connexed by points with connexity 2). Else, splits wires of the face, these are boundaries of the new faces to build up; <OldWiresNewWires> describes (wire, splits of wire); <ESplits> describes (edge, edge's splits)
        """
    @staticmethod
    def Regularize_s(aFace : OCP.TopoDS.TopoDS_Face,aListOfFaces : OCP.TopTools.TopTools_ListOfShape,ESplits : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> bool: 
        """
        Returns <False> if the face is valid (the UV representation of the face is a set of pcurves connexed by points with connexity 2). Else, splits <aFace> in order to return a list of valid faces.
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_AncestorsTool():
    """
    Describes the ancestors tool needed by the class DSFiller from TopOpeInter.
    """
    @staticmethod
    def MakeAncestors_s(S : OCP.TopoDS.TopoDS_Shape,TS : OCP.TopAbs.TopAbs_ShapeEnum,TA : OCP.TopAbs.TopAbs_ShapeEnum,M : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape) -> None: 
        """
        same as package method TopExp::MapShapeListOfShapes()
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_BoxSort():
    """
    None
    """
    def AddBoxes(self,S : OCP.TopoDS.TopoDS_Shape,TS : OCP.TopAbs.TopAbs_ShapeEnum,TA : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: 
        """
        None
        """
    def AddBoxesMakeCOB(self,S : OCP.TopoDS.TopoDS_Shape,TS : OCP.TopAbs.TopAbs_ShapeEnum,TA : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: 
        """
        None
        """
    def Box(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def Compare(self,S : OCP.TopoDS.TopoDS_Shape) -> Any: 
        """
        None
        """
    def HAB(self) -> OCP.Bnd.Bnd_HArray1OfBox: 
        """
        None
        """
    def HABShape(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def HBoxTool(self) -> TopOpeBRepTool_HBoxTool: 
        """
        None
        """
    def MakeCOB(self,S : OCP.TopoDS.TopoDS_Shape,TS : OCP.TopAbs.TopAbs_ShapeEnum,TA : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: 
        """
        None
        """
    def MakeHAB(self,S : OCP.TopoDS.TopoDS_Shape,TS : OCP.TopAbs.TopAbs_ShapeEnum,TA : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: 
        """
        None
        """
    @staticmethod
    def MakeHABCOB_s(HAB : OCP.Bnd.Bnd_HArray1OfBox,COB : OCP.Bnd.Bnd_Box) -> None: 
        """
        None
        """
    def SetHBoxTool(self,T : TopOpeBRepTool_HBoxTool) -> None: 
        """
        None
        """
    def TouchedShape(self,I : Any) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,T : TopOpeBRepTool_HBoxTool) -> None: ...
    pass
class TopOpeBRepTool_C2DF():
    """
    None
    """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def IsFace(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def IsPC(self,PC : OCP.Geom2d.Geom2d_Curve) -> bool: 
        """
        None
        """
    def PC(self,f2d : float,l2d : float,tol : float) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def SetFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def SetPC(self,PC : OCP.Geom2d.Geom2d_Curve,f2d : float,l2d : float,tol : float) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,PC : OCP.Geom2d.Geom2d_Curve,f2d : float,l2d : float,tol : float,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
class TopOpeBRepTool_CLASSI():
    """
    None
    """
    def Add2d(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def ClassiBnd2d(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,tol : float,checklarge : bool) -> int: 
        """
        None
        """
    def Classilist(self,lS : OCP.TopTools.TopTools_ListOfShape,mapgreasma : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> bool: 
        """
        None
        """
    def Classip2d(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,stabnd2d12 : int) -> int: 
        """
        None
        """
    def GetBox2d(self,S : OCP.TopoDS.TopoDS_Shape,Box2d : OCP.Bnd.Bnd_Box2d) -> bool: 
        """
        None
        """
    def Getface(self,S : OCP.TopoDS.TopoDS_Shape,fa : TopOpeBRepTool_face) -> bool: 
        """
        None
        """
    def HasInit2d(self) -> bool: 
        """
        None
        """
    def Init2d(self,Fref : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_CORRISO():
    """
    Fref is built on x-periodic surface (x=u,v). S built on Fref's geometry, should be UVClosed.
    """
    def AddNewConnexity(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def Connexity(self,V : OCP.TopoDS.TopoDS_Vertex,Eds : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def EdgeOUTofBoundsUV(self,E : OCP.TopoDS.TopoDS_Edge,onU : bool,tolx : float,parspE : float) -> int: 
        """
        None
        """
    @overload
    def EdgeWithFaultyUV(self,EdsToCheck : OCP.TopTools.TopTools_ListOfShape,nfybounds : int,fyE : OCP.TopoDS.TopoDS_Shape,Ifaulty : int) -> bool: 
        """
        None

        None
        """
    @overload
    def EdgeWithFaultyUV(self,E : OCP.TopoDS.TopoDS_Edge,Ivfaulty : int) -> bool: ...
    def EdgesOUTofBoundsUV(self,EdsToCheck : OCP.TopTools.TopTools_ListOfShape,onU : bool,tolx : float,FyEds : OCP.TopTools.TopTools_DataMapOfOrientedShapeInteger) -> bool: 
        """
        None
        """
    def EdgesWithFaultyUV(self,EdsToCheck : OCP.TopTools.TopTools_ListOfShape,nfybounds : int,FyEds : OCP.TopTools.TopTools_DataMapOfOrientedShapeInteger,stopatfirst : bool=False) -> bool: 
        """
        None
        """
    def Eds(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Fref(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def GASref(self) -> OCP.GeomAdaptor.GeomAdaptor_Surface: 
        """
        None
        """
    def GetnewS(self,newS : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def PurgeFyClosingE(self,ClEds : OCP.TopTools.TopTools_ListOfShape,fyClEds : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def Refclosed(self,x : int,xperiod : float) -> bool: 
        """
        None
        """
    def RemoveOldConnexity(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def S(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def SetConnexity(self,V : OCP.TopoDS.TopoDS_Vertex,Eds : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def SetUVRep(self,E : OCP.TopoDS.TopoDS_Edge,C2DF : TopOpeBRepTool_C2DF) -> bool: 
        """
        None
        """
    def Tol(self,I : int,tol3d : float) -> float: 
        """
        None
        """
    def TrslUV(self,onU : bool,FyEds : OCP.TopTools.TopTools_DataMapOfOrientedShapeInteger) -> bool: 
        """
        None
        """
    def UVClosed(self) -> bool: 
        """
        None
        """
    def UVRep(self,E : OCP.TopoDS.TopoDS_Edge,C2DF : TopOpeBRepTool_C2DF) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,FRef : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_CurveTool():
    """
    None
    """
    def ChangeGeomTool(self) -> TopOpeBRepTool_GeomTool: 
        """
        None
        """
    def GetGeomTool(self) -> TopOpeBRepTool_GeomTool: 
        """
        None
        """
    @staticmethod
    def IsProjectable_s(S : OCP.TopoDS.TopoDS_Shape,C : OCP.Geom.Geom_Curve) -> bool: 
        """
        None
        """
    @staticmethod
    def MakeBSpline1fromPnt2d_s(P : OCP.TColgp.TColgp_Array1OfPnt2d) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    @staticmethod
    def MakeBSpline1fromPnt_s(P : OCP.TColgp.TColgp_Array1OfPnt) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def MakeCurves(self,min : float,max : float,C3D : OCP.Geom.Geom_Curve,PC1 : OCP.Geom2d.Geom2d_Curve,PC2 : OCP.Geom2d.Geom2d_Curve,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,C3DN : OCP.Geom.Geom_Curve,PC1N : OCP.Geom2d.Geom2d_Curve,PC2N : OCP.Geom2d.Geom2d_Curve,Tol3d : float,Tol2d : float) -> bool: 
        """
        Approximates curves. Returns False in the case of failure
        """
    @staticmethod
    def MakePCurveOnFace_s(S : OCP.TopoDS.TopoDS_Shape,C : OCP.Geom.Geom_Curve,TolReached2d : float,first : float=0.0,last : float=0.0) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def SetGeomTool(self,GT : TopOpeBRepTool_GeomTool) -> None: 
        """
        None
        """
    @overload
    def __init__(self,OCT : TopOpeBRepTool_OutCurveType) -> None: ...
    @overload
    def __init__(self,GT : TopOpeBRepTool_GeomTool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_DataMapOfOrientedShapeC2DF(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepTool_DataMapOfOrientedShapeC2DF) -> TopOpeBRepTool_DataMapOfOrientedShapeC2DF: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepTool_C2DF) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepTool_C2DF) -> TopOpeBRepTool_C2DF: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_C2DF: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_C2DF: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : TopOpeBRepTool_DataMapOfOrientedShapeC2DF) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_C2DF: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepTool_C2DF) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_C2DF: 
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
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepTool_DataMapOfOrientedShapeC2DF) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepTool_DataMapOfShapeListOfC2DF(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepTool_DataMapOfShapeListOfC2DF) -> TopOpeBRepTool_DataMapOfShapeListOfC2DF: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepTool_ListOfC2DF) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepTool_ListOfC2DF) -> TopOpeBRepTool_ListOfC2DF: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_ListOfC2DF: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_ListOfC2DF: 
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
    def Exchange(self,theOther : TopOpeBRepTool_DataMapOfShapeListOfC2DF) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_ListOfC2DF: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepTool_ListOfC2DF) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_ListOfC2DF: 
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepTool_DataMapOfShapeListOfC2DF) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepTool_DataMapOfShapeface(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepTool_DataMapOfShapeface) -> TopOpeBRepTool_DataMapOfShapeface: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepTool_face) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepTool_face) -> TopOpeBRepTool_face: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_face: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_face: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : TopOpeBRepTool_DataMapOfShapeface) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepTool_face) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_face: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_face: 
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
    def __init__(self,theOther : TopOpeBRepTool_DataMapOfShapeface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepTool_FuseEdges():
    """
    This class can detect vertices in a face that can be considered useless and then perform the fuse of the edges and remove the useless vertices. By useles vertices, we mean : * vertices that have exactly two connex edges * the edges connex to the vertex must have exactly the same 2 connex faces . * The edges connex to the vertex must have the same geometric support.
    """
    def AvoidEdges(self,theMapEdg : OCP.TopTools.TopTools_IndexedMapOfShape) -> None: 
        """
        set edges to avoid being fused
        """
    def Edges(self,theMapLstEdg : OCP.TopTools.TopTools_DataMapOfIntegerListOfShape) -> None: 
        """
        returns all the list of edges to be fused each list of the map represent a set of connex edges that can be fused.
        """
    def Faces(self,theMapFac : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        returns the map of modified faces.
        """
    def NbVertices(self) -> int: 
        """
        returns the number of vertices candidate to be removed
        """
    def Perform(self) -> None: 
        """
        Using map of list of connex edges, fuse each list to one edge and then update myShape
        """
    def ResultEdges(self,theMapEdg : OCP.TopTools.TopTools_DataMapOfIntegerShape) -> None: 
        """
        returns all the fused edges. each integer entry in the map corresponds to the integer in the DataMapOfIntegerListOfShape we get in method Edges. That is to say, to the list of edges in theMapLstEdg(i) corresponds the resulting edge theMapEdge(i)
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns myShape modified with the list of internal edges removed from it.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape,PerformNow : bool=False) -> None: ...
    pass
class TopOpeBRepTool_GeomTool():
    """
    None
    """
    def CompC3D(self) -> bool: 
        """
        None
        """
    def CompPC1(self) -> bool: 
        """
        None
        """
    def CompPC2(self) -> bool: 
        """
        None
        """
    @overload
    def Define(self,GT : TopOpeBRepTool_GeomTool) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Define(self,TypeC3D : TopOpeBRepTool_OutCurveType) -> None: ...
    @overload
    def Define(self,TypeC3D : TopOpeBRepTool_OutCurveType,CompC3D : bool,CompPC1 : bool,CompPC2 : bool) -> None: ...
    def DefineCurves(self,CompC3D : bool) -> None: 
        """
        None
        """
    def DefinePCurves1(self,CompPC1 : bool) -> None: 
        """
        None
        """
    def DefinePCurves2(self,CompPC2 : bool) -> None: 
        """
        None
        """
    def GetTolerances(self) -> Tuple[float, float]: 
        """
        None
        """
    def NbPntMax(self) -> int: 
        """
        None
        """
    def SetNbPntMax(self,NbPntMax : int) -> None: 
        """
        None
        """
    def SetTolerances(self,tol3d : float,tol2d : float) -> None: 
        """
        None
        """
    def TypeC3D(self) -> TopOpeBRepTool_OutCurveType: 
        """
        None
        """
    def __init__(self,TypeC3D : TopOpeBRepTool_OutCurveType=TopOpeBRepTool_OutCurveType.TopOpeBRepTool_BSPLINE1,CompC3D : bool=True,CompPC1 : bool=True,CompPC2 : bool=True) -> None: ...
    pass
class TopOpeBRepTool_HBoxTool(OCP.Standard.Standard_Transient):
    def AddBox(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddBoxes(self,S : OCP.TopoDS.TopoDS_Shape,TS : OCP.TopAbs.TopAbs_ShapeEnum,TA : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: 
        """
        None
        """
    @overload
    def Box(self,I : int) -> OCP.Bnd.Bnd_Box: 
        """
        None

        None
        """
    @overload
    def Box(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: ...
    def ChangeIMS(self) -> TopOpeBRepTool_IndexedDataMapOfShapeBox: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeBoxOnVertices_s(S : OCP.TopoDS.TopoDS_Shape,B : OCP.Bnd.Bnd_Box) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeBox_s(S : OCP.TopoDS.TopoDS_Shape,B : OCP.Bnd.Bnd_Box) -> None: 
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
    @staticmethod
    def DumpB_s(B : OCP.Bnd.Bnd_Box) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Extent(self) -> int: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBox(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IMS(self) -> TopOpeBRepTool_IndexedDataMapOfShapeBox: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
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
    def Shape(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
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
class TopOpeBRepTool_IndexedDataMapOfShapeBox(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Bnd.Bnd_Box) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepTool_IndexedDataMapOfShapeBox) -> TopOpeBRepTool_IndexedDataMapOfShapeBox: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> OCP.Bnd.Bnd_Box: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopOpeBRepTool_IndexedDataMapOfShapeBox) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> OCP.Bnd.Bnd_Box: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : OCP.Bnd.Bnd_Box) -> bool: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindKey
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
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Bnd.Bnd_Box) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepTool_IndexedDataMapOfShapeBox) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepTool_IndexedDataMapOfShapeBox2d(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Bnd.Bnd_Box2d) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepTool_IndexedDataMapOfShapeBox2d) -> TopOpeBRepTool_IndexedDataMapOfShapeBox2d: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> OCP.Bnd.Bnd_Box2d: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box2d: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box2d: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopOpeBRepTool_IndexedDataMapOfShapeBox2d) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> OCP.Bnd.Bnd_Box2d: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : OCP.Bnd.Bnd_Box2d) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box2d: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindKey
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
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box2d: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : OCP.Bnd.Bnd_Box2d) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepTool_IndexedDataMapOfShapeBox2d) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepTool_IndexedDataMapOfShapeconnexity(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepTool_connexity) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepTool_IndexedDataMapOfShapeconnexity) -> TopOpeBRepTool_IndexedDataMapOfShapeconnexity: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> TopOpeBRepTool_connexity: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_connexity: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_connexity: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopOpeBRepTool_IndexedDataMapOfShapeconnexity) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> TopOpeBRepTool_connexity: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepTool_connexity) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_connexity: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindKey
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
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_connexity: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepTool_connexity) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepTool_IndexedDataMapOfShapeconnexity) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepTool_ListOfC2DF(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TopOpeBRepTool_C2DF) -> TopOpeBRepTool_C2DF: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : TopOpeBRepTool_C2DF,theIter : Any) -> None: ...
    @overload
    def Append(self,theOther : TopOpeBRepTool_ListOfC2DF) -> None: ...
    def Assign(self,theOther : TopOpeBRepTool_ListOfC2DF) -> TopOpeBRepTool_ListOfC2DF: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> TopOpeBRepTool_C2DF: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TopOpeBRepTool_ListOfC2DF,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : TopOpeBRepTool_C2DF,theIter : Any) -> TopOpeBRepTool_C2DF: ...
    @overload
    def InsertBefore(self,theItem : TopOpeBRepTool_C2DF,theIter : Any) -> TopOpeBRepTool_C2DF: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TopOpeBRepTool_ListOfC2DF,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TopOpeBRepTool_C2DF: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TopOpeBRepTool_ListOfC2DF) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : TopOpeBRepTool_C2DF) -> TopOpeBRepTool_C2DF: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepTool_ListOfC2DF) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepTool_OutCurveType():
    """
    None

    Members:

      TopOpeBRepTool_BSPLINE1

      TopOpeBRepTool_APPROX

      TopOpeBRepTool_INTERPOL
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
    TopOpeBRepTool_APPROX: OCP.TopOpeBRepTool.TopOpeBRepTool_OutCurveType # value = <TopOpeBRepTool_OutCurveType.TopOpeBRepTool_APPROX: 1>
    TopOpeBRepTool_BSPLINE1: OCP.TopOpeBRepTool.TopOpeBRepTool_OutCurveType # value = <TopOpeBRepTool_OutCurveType.TopOpeBRepTool_BSPLINE1: 0>
    TopOpeBRepTool_INTERPOL: OCP.TopOpeBRepTool.TopOpeBRepTool_OutCurveType # value = <TopOpeBRepTool_OutCurveType.TopOpeBRepTool_INTERPOL: 2>
    __entries: dict # value = {'TopOpeBRepTool_BSPLINE1': (<TopOpeBRepTool_OutCurveType.TopOpeBRepTool_BSPLINE1: 0>, None), 'TopOpeBRepTool_APPROX': (<TopOpeBRepTool_OutCurveType.TopOpeBRepTool_APPROX: 1>, None), 'TopOpeBRepTool_INTERPOL': (<TopOpeBRepTool_OutCurveType.TopOpeBRepTool_INTERPOL: 2>, None)}
    __members__: dict # value = {'TopOpeBRepTool_BSPLINE1': <TopOpeBRepTool_OutCurveType.TopOpeBRepTool_BSPLINE1: 0>, 'TopOpeBRepTool_APPROX': <TopOpeBRepTool_OutCurveType.TopOpeBRepTool_APPROX: 1>, 'TopOpeBRepTool_INTERPOL': <TopOpeBRepTool_OutCurveType.TopOpeBRepTool_INTERPOL: 2>}
    pass
class TopOpeBRepTool_PurgeInternalEdges():
    """
    remove from a shape, the internal edges that are not connected to any face in the shape. We can get the list of the edges as a DataMapOfShapeListOfShape with a Face of the Shape as the key and a list of internal edges as the value. The list of internal edges means edges that are not connected to any face in the shape.
    """
    def Faces(self,theMapFacLstEdg : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        returns the list internal edges associated with the faces of the myShape. If PerformNow was False when created, then call the private Perform method that do the main job.
        """
    def IsDone(self) -> bool: 
        """
        returns False if the list of internal edges has not been extracted
        """
    def NbEdges(self) -> int: 
        """
        returns the number of edges candidate to be removed
        """
    def Perform(self) -> None: 
        """
        Using the list of internal edge from each face, rebuild myShape by removing thoses edges.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns myShape modified with the list of internal edges removed from it.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape,PerformNow : bool=True) -> None: ...
    pass
class TopOpeBRepTool_REGUS():
    """
    None
    """
    def GetFsplits(self,Fsplits : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        None
        """
    def GetOshNsh(self,OshNsh : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        None
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitBlock(self) -> bool: 
        """
        None
        """
    def MapS(self) -> bool: 
        """
        None
        """
    def NearestF(self,e : OCP.TopoDS.TopoDS_Edge,lof : OCP.TopTools.TopTools_ListOfShape,ffound : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def NextinBlock(self) -> bool: 
        """
        None
        """
    def REGU(self) -> bool: 
        """
        None
        """
    def S(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def SetFsplits(self,Fsplits : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        None
        """
    def SetOshNsh(self,OshNsh : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def SplitF_s(Fanc : OCP.TopoDS.TopoDS_Face,FSplits : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def SplitFaces(self) -> bool: 
        """
        None
        """
    @staticmethod
    def WireToFace_s(Fanc : OCP.TopoDS.TopoDS_Face,nWs : OCP.TopTools.TopTools_ListOfShape,nFs : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_REGUW():
    """
    None
    """
    def AddNewConnexity(self,v : OCP.TopoDS.TopoDS_Vertex,OriKey : int,e : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def Connexity(self,v : OCP.TopoDS.TopoDS_Vertex,co : TopOpeBRepTool_connexity) -> bool: 
        """
        None
        """
    def Fref(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def GetEsplits(self,Esplits : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        None
        """
    def GetOwNw(self,OwNw : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        None
        """
    def GetSplits(self,Splits : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def HasInit(self) -> bool: 
        """
        None
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitBlock(self) -> bool: 
        """
        None
        """
    def MapS(self) -> bool: 
        """
        None
        """
    def NearestE(self,loe : OCP.TopTools.TopTools_ListOfShape,efound : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def NextinBlock(self) -> bool: 
        """
        None
        """
    @overload
    def REGU(self,istep : int,Scur : OCP.TopoDS.TopoDS_Shape,Splits : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None

        None
        """
    @overload
    def REGU(self) -> bool: ...
    def RemoveOldConnexity(self,v : OCP.TopoDS.TopoDS_Vertex,OriKey : int,e : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def S(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def SetEsplits(self,Esplits : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        None
        """
    def SetOwNw(self,OwNw : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        None
        """
    def SplitEds(self) -> bool: 
        """
        None
        """
    def UpdateMultiple(self,v : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        None
        """
    def __init__(self,FRef : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
class TopOpeBRepTool_ShapeClassifier():
    """
    None
    """
    def ChangeSolidClassifier(self) -> TopOpeBRepTool_SolidClassifier: 
        """
        None
        """
    def ClearAll(self) -> None: 
        """
        reset all internal data (SolidClassifier included)
        """
    def ClearCurrent(self) -> None: 
        """
        reset all internal data (except SolidClassified)
        """
    def P2D(self) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def P3D(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @overload
    def SameDomain(self,samedomain : int) -> None: 
        """
        None

        set mode for next StateShapeShape call samedomain = true --> S,Sref are same domain --> point on restriction (ON S) is used to classify S. samedomain = false --> S,Sref are not domain --> point not on restriction of S (IN S) is used to classify S. samedomain value is used only in next StateShapeShape call
        """
    @overload
    def SameDomain(self) -> int: ...
    def SetReference(self,SRef : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Set SRef as reference shape the next StateShapeReference(S,AvoidS) calls will classify S with SRef.
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        return field myState
        """
    def StateP2DReference(self,P2D : OCP.gp.gp_Pnt2d) -> None: 
        """
        classify point P2D with myRef
        """
    def StateP3DReference(self,P3D : OCP.gp.gp_Pnt) -> None: 
        """
        classify point P3D with myRef
        """
    @overload
    def StateShapeReference(self,S : OCP.TopoDS.TopoDS_Shape,LAvoidS : OCP.TopTools.TopTools_ListOfShape) -> OCP.TopAbs.TopAbs_State: 
        """
        classify shape S compared with reference shape. AvoidS is not used in classification; AvoidS may be IsNull(). (usefull to avoid ON or UNKNOWN state in special cases)

        classify shape S compared with reference shape. LAvoidS is list of S subshapes to avoid in classification (usefull to avoid ON or UNKNOWN state in special cases)
        """
    @overload
    def StateShapeReference(self,S : OCP.TopoDS.TopoDS_Shape,AvoidS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: ...
    @overload
    def StateShapeShape(self,S : OCP.TopoDS.TopoDS_Shape,AvoidS : OCP.TopoDS.TopoDS_Shape,SRef : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        classify shape S compared with shape SRef. samedomain = 0 : S1,S2 are not same domain samedomain = 1 : S1,S2 are same domain

        classify shape S compared with shape SRef. AvoidS is not used in classification; AvoidS may be IsNull(). (usefull to avoid ON or UNKNOWN state in special cases)

        classify shape S compared with shape SRef. LAvoidS is list of S subshapes to avoid in classification AvoidS is not used in classification; AvoidS may be IsNull(). (usefull to avoid ON or UNKNOWN state in special cases)
        """
    @overload
    def StateShapeShape(self,S : OCP.TopoDS.TopoDS_Shape,LAvoidS : OCP.TopTools.TopTools_ListOfShape,SRef : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: ...
    @overload
    def StateShapeShape(self,S : OCP.TopoDS.TopoDS_Shape,SRef : OCP.TopoDS.TopoDS_Shape,samedomain : int=0) -> OCP.TopAbs.TopAbs_State: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,SRef : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class TopOpeBRepTool_ShapeExplorer(OCP.TopExp.TopExp_Explorer):
    """
    Extends TopExp_Explorer by counting index of current item (for tracing and debug)
    """
    def Clear(self) -> None: 
        """
        Clears the content of the explorer. It will return False on More().

        Clears the content of the explorer. It will return False on More().
        """
    def Current(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the current shape in the exploration. Exceptions Standard_NoSuchObject if this explorer has no more shapes to explore.
        """
    def Depth(self) -> int: 
        """
        Returns the current depth of the exploration. 0 is the shape to explore itself.

        Returns the current depth of the exploration. 0 is the shape to explore itself.
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def DumpCurrent(self,OS : io.BytesIO) -> io.BytesIO: 
        """
        Dump info on current shape to stream
        """
    def Index(self) -> int: 
        """
        Index of current sub-shape
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape,ToFind : OCP.TopAbs.TopAbs_ShapeEnum,ToAvoid : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: 
        """
        None
        """
    def More(self) -> bool: 
        """
        Returns True if there are more shapes in the exploration.

        Returns True if there are more shapes in the exploration.
        """
    def Next(self) -> None: 
        """
        Moves to the next Shape in the exploration.
        """
    def ReInit(self) -> None: 
        """
        Reinitialize the exploration with the original arguments.
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the current shape in the exploration. Exceptions Standard_NoSuchObject if this explorer has no more shapes to explore.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,ToFind : OCP.TopAbs.TopAbs_ShapeEnum,ToAvoid : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_ShapeTool():
    """
    None
    """
    @staticmethod
    def AdjustOnPeriodic_s(S : OCP.TopoDS.TopoDS_Shape) -> Tuple[float, float]: 
        """
        ajust u,v values in UVBounds of the domain of the geometric shape <S>, according to Uperiodicity and VPeriodicity of the domain. <S> is assumed to be a face. u and/or v is/are not modified when the domain is not periodic in U and/or V .
        """
    @staticmethod
    @overload
    def BASISCURVE_s(C : OCP.Geom.Geom_Curve) -> OCP.Geom.Geom_Curve: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def BASISCURVE_s(E : OCP.TopoDS.TopoDS_Edge) -> OCP.Geom.Geom_Curve: ...
    @staticmethod
    @overload
    def BASISSURFACE_s(F : OCP.TopoDS.TopoDS_Face) -> OCP.Geom.Geom_Surface: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def BASISSURFACE_s(S : OCP.Geom.Geom_Surface) -> OCP.Geom.Geom_Surface: ...
    @staticmethod
    def Closed_s(S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        indicates wheter shape S1 is a closing shape on S2 or not.
        """
    @staticmethod
    def CurvesSameOriented_s(C1 : OCP.BRepAdaptor.BRepAdaptor_Curve,C2 : OCP.BRepAdaptor.BRepAdaptor_Curve) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def EdgeData_s(E : OCP.TopoDS.TopoDS_Shape,P : float,T : OCP.gp.gp_Dir,N : OCP.gp.gp_Dir,C : float) -> float: 
        """
        Compute tangent T, normal N, curvature C at point of parameter P on curve BRAC. Returns the tolerance indicating if T,N are null.

        Same as previous on edge E.
        """
    @staticmethod
    @overload
    def EdgeData_s(BRAC : OCP.BRepAdaptor.BRepAdaptor_Curve,P : float,T : OCP.gp.gp_Dir,N : OCP.gp.gp_Dir,C : float) -> float: ...
    @staticmethod
    def EdgesSameOriented_s(E1 : OCP.TopoDS.TopoDS_Shape,E2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    @staticmethod
    def FacesSameOriented_s(F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    @staticmethod
    def PeriodizeParameter_s(par : float,EE : OCP.TopoDS.TopoDS_Shape,FF : OCP.TopoDS.TopoDS_Shape) -> float: 
        """
        None
        """
    @staticmethod
    def Pnt_s(S : OCP.TopoDS.TopoDS_Shape) -> OCP.gp.gp_Pnt: 
        """
        Returns 3D point of vertex <S>.
        """
    @staticmethod
    def Resolution3dU_s(SU : OCP.Geom.Geom_Surface,Tol2d : float) -> float: 
        """
        None
        """
    @staticmethod
    def Resolution3dV_s(SU : OCP.Geom.Geom_Surface,Tol2d : float) -> float: 
        """
        None
        """
    @staticmethod
    @overload
    def Resolution3d_s(F : OCP.TopoDS.TopoDS_Face,Tol2d : float) -> float: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Resolution3d_s(SU : OCP.Geom.Geom_Surface,Tol2d : float) -> float: ...
    @staticmethod
    def ShapesSameOriented_s(S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    @staticmethod
    def SurfacesSameOriented_s(S1 : OCP.BRepAdaptor.BRepAdaptor_Surface,S2 : OCP.BRepAdaptor.BRepAdaptor_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def Tolerance_s(S : OCP.TopoDS.TopoDS_Shape) -> float: 
        """
        Returns the tolerance of the shape <S>. If the shape <S> is Null, returns 0.
        """
    @staticmethod
    @overload
    def UVBOUNDS_s(F : OCP.TopoDS.TopoDS_Face) -> Tuple[bool, bool, float, float, float, float]: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def UVBOUNDS_s(S : OCP.Geom.Geom_Surface) -> Tuple[bool, bool, float, float, float, float]: ...
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_SolidClassifier():
    """
    None
    """
    @overload
    def Classify(self,S : OCP.TopoDS.TopoDS_Shell,P : OCP.gp.gp_Pnt,Tol : float) -> OCP.TopAbs.TopAbs_State: 
        """
        compute the position of point <P> regarding with the geometric domain of the solid <S>.

        compute the position of point <P> regarding with the geometric domain of the shell <S>.
        """
    @overload
    def Classify(self,S : OCP.TopoDS.TopoDS_Solid,P : OCP.gp.gp_Pnt,Tol : float) -> OCP.TopAbs.TopAbs_State: ...
    def Clear(self) -> None: 
        """
        None
        """
    def LoadShell(self,S : OCP.TopoDS.TopoDS_Shell) -> None: 
        """
        None
        """
    def LoadSolid(self,S : OCP.TopoDS.TopoDS_Solid) -> None: 
        """
        None
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_TOOL():
    """
    None
    """
    @staticmethod
    def ClosedE_s(E : OCP.TopoDS.TopoDS_Edge,vclo : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        None
        """
    @staticmethod
    def ClosedS_s(F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    @staticmethod
    def CurvE_s(E : OCP.TopoDS.TopoDS_Edge,par : float,tg0 : OCP.gp.gp_Dir,Curv : float) -> bool: 
        """
        None
        """
    @staticmethod
    def CurvF_s(F : OCP.TopoDS.TopoDS_Face,uv : OCP.gp.gp_Pnt2d,tg0 : OCP.gp.gp_Dir,Curv : float,direct : bool) -> bool: 
        """
        None
        """
    @staticmethod
    def EdgeONFace_s(par : float,ed : OCP.TopoDS.TopoDS_Edge,uv : OCP.gp.gp_Pnt2d,fa : OCP.TopoDS.TopoDS_Face,isonfa : bool) -> bool: 
        """
        None
        """
    @staticmethod
    def Getduv_s(f : OCP.TopoDS.TopoDS_Face,uv : OCP.gp.gp_Pnt2d,dir : OCP.gp.gp_Vec,factor : float,duv : OCP.gp.gp_Dir2d) -> bool: 
        """
        None
        """
    @staticmethod
    def Getstp3dF_s(p : OCP.gp.gp_Pnt,f : OCP.TopoDS.TopoDS_Face,uv : OCP.gp.gp_Pnt2d,st : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def IsClosingE_s(E : OCP.TopoDS.TopoDS_Edge,W : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def IsClosingE_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> bool: ...
    @staticmethod
    @overload
    def IsQuad_s(F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def IsQuad_s(E : OCP.TopoDS.TopoDS_Edge) -> bool: ...
    @staticmethod
    @overload
    def IsonCLO_s(PC : OCP.Geom2d.Geom2d_Curve,onU : bool,xfirst : float,xperiod : float,xtol : float) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def IsonCLO_s(C2DF : TopOpeBRepTool_C2DF,onU : bool,xfirst : float,xperiod : float,xtol : float) -> bool: ...
    @staticmethod
    def MatterKPtg_s(f1 : OCP.TopoDS.TopoDS_Face,f2 : OCP.TopoDS.TopoDS_Face,e : OCP.TopoDS.TopoDS_Edge,Ang : float) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def Matter_s(f1 : OCP.TopoDS.TopoDS_Face,f2 : OCP.TopoDS.TopoDS_Face,e : OCP.TopoDS.TopoDS_Edge,pare : float,tola : float,Ang : float) -> bool: 
        """
        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def Matter_s(d1 : OCP.gp.gp_Vec2d,d2 : OCP.gp.gp_Vec2d) -> float: ...
    @staticmethod
    @overload
    def Matter_s(xx1 : OCP.gp.gp_Dir,nt1 : OCP.gp.gp_Dir,xx2 : OCP.gp.gp_Dir,nt2 : OCP.gp.gp_Dir,tola : float,Ang : float) -> bool: ...
    @staticmethod
    @overload
    def Matter_s(d1 : OCP.gp.gp_Vec,d2 : OCP.gp.gp_Vec,ref : OCP.gp.gp_Vec) -> float: ...
    @staticmethod
    def MkShell_s(lF : OCP.TopTools.TopTools_ListOfShape,She : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def NgApp_s(par : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,tola : float,ngApp : OCP.gp.gp_Dir) -> bool: 
        """
        None
        """
    @staticmethod
    def NggeomF_s(uv : OCP.gp.gp_Pnt2d,F : OCP.TopoDS.TopoDS_Face,ng : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    @staticmethod
    def Nt_s(uv : OCP.gp.gp_Pnt2d,f : OCP.TopoDS.TopoDS_Face,normt : OCP.gp.gp_Dir) -> bool: 
        """
        None
        """
    @staticmethod
    def OnBoundary_s(par : float,E : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        None
        """
    @staticmethod
    def OriinSor_s(sub : OCP.TopoDS.TopoDS_Shape,S : OCP.TopoDS.TopoDS_Shape,checkclo : bool=False) -> int: 
        """
        None
        """
    @staticmethod
    def OriinSorclosed_s(sub : OCP.TopoDS.TopoDS_Shape,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    @staticmethod
    def ParE2d_s(p2d : OCP.gp.gp_Pnt2d,e : OCP.TopoDS.TopoDS_Edge,f : OCP.TopoDS.TopoDS_Face,par : float,dist : float) -> bool: 
        """
        None
        """
    @staticmethod
    def ParE_s(Iv : int,E : OCP.TopoDS.TopoDS_Edge) -> float: 
        """
        None
        """
    @staticmethod
    def ParISO_s(p2d : OCP.gp.gp_Pnt2d,e : OCP.TopoDS.TopoDS_Edge,f : OCP.TopoDS.TopoDS_Face,pare : float) -> bool: 
        """
        None
        """
    @staticmethod
    def Remove_s(loS : OCP.TopTools.TopTools_ListOfShape,toremove : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    @staticmethod
    def SplitE_s(Eanc : OCP.TopoDS.TopoDS_Edge,Splits : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    @staticmethod
    def Tg2dApp_s(iv : int,E : OCP.TopoDS.TopoDS_Edge,C2DF : TopOpeBRepTool_C2DF,factor : float) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    @staticmethod
    def Tg2d_s(iv : int,E : OCP.TopoDS.TopoDS_Edge,C2DF : TopOpeBRepTool_C2DF) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    @staticmethod
    def TgINSIDE_s(v : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,Tg : OCP.gp.gp_Vec,OvinE : int) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def TggeomE_s(par : float,E : OCP.TopoDS.TopoDS_Edge,Tg : OCP.gp.gp_Vec) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def TggeomE_s(par : float,BC : OCP.BRepAdaptor.BRepAdaptor_Curve,Tg : OCP.gp.gp_Vec) -> bool: ...
    @staticmethod
    def TolP_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> float: 
        """
        None
        """
    @staticmethod
    def TolUV_s(F : OCP.TopoDS.TopoDS_Face,tol3d : float) -> float: 
        """
        None
        """
    @staticmethod
    def TrslUVModifE_s(t2d : OCP.gp.gp_Vec2d,F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    @staticmethod
    def TrslUV_s(t2d : OCP.gp.gp_Vec2d,C2DF : TopOpeBRepTool_C2DF) -> None: 
        """
        None
        """
    @staticmethod
    def UVF_s(par : float,C2DF : TopOpeBRepTool_C2DF) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    @staticmethod
    @overload
    def UVISO_s(C2DF : TopOpeBRepTool_C2DF,isou : bool,isov : bool,d2d : OCP.gp.gp_Dir2d,o2d : OCP.gp.gp_Pnt2d) -> bool: 
        """
        None

        None

        None
        """
    @staticmethod
    @overload
    def UVISO_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,isou : bool,isov : bool,d2d : OCP.gp.gp_Dir2d,o2d : OCP.gp.gp_Pnt2d) -> bool: ...
    @staticmethod
    @overload
    def UVISO_s(PC : OCP.Geom2d.Geom2d_Curve,isou : bool,isov : bool,d2d : OCP.gp.gp_Dir2d,o2d : OCP.gp.gp_Pnt2d) -> bool: ...
    @staticmethod
    def Vertex_s(Iv : int,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    @staticmethod
    def Vertices_s(E : OCP.TopoDS.TopoDS_Edge,Vces : OCP.TopTools.TopTools_Array1OfShape) -> None: 
        """
        None
        """
    @staticmethod
    def WireToFace_s(Fref : OCP.TopoDS.TopoDS_Face,mapWlow : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,lFs : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    @staticmethod
    def XX_s(uv : OCP.gp.gp_Pnt2d,f : OCP.TopoDS.TopoDS_Face,par : float,e : OCP.TopoDS.TopoDS_Edge,xx : OCP.gp.gp_Dir) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    @staticmethod
    def minDUV_s(F : OCP.TopoDS.TopoDS_Face) -> float: 
        """
        None
        """
    @staticmethod
    def outUVbounds_s(uv : OCP.gp.gp_Pnt2d,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    @staticmethod
    def stuvF_s(uv : OCP.gp.gp_Pnt2d,F : OCP.TopoDS.TopoDS_Face) -> Tuple[int, int]: 
        """
        None
        """
    @staticmethod
    def tryNgApp_s(par : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,tola : float,ng : OCP.gp.gp_Dir) -> bool: 
        """
        None
        """
    @staticmethod
    def tryOriEinF_s(par : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> int: 
        """
        None
        """
    @staticmethod
    def tryTg2dApp_s(iv : int,E : OCP.TopoDS.TopoDS_Edge,C2DF : TopOpeBRepTool_C2DF,factor : float) -> OCP.gp.gp_Vec2d: 
        """
        None
        """
    @staticmethod
    def uvApp_s(f : OCP.TopoDS.TopoDS_Face,e : OCP.TopoDS.TopoDS_Edge,par : float,eps : float,uvapp : OCP.gp.gp_Pnt2d) -> bool: 
        """
        None
        """
    pass
class TopOpeBRepTool_connexity():
    """
    None
    """
    @overload
    def AddItem(self,OriKey : int,Item : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None

        None
        """
    @overload
    def AddItem(self,OriKey : int,Item : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def AllItems(self,Item : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None
        """
    def ChangeItem(self,OriKey : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def IsFaulty(self) -> bool: 
        """
        None
        """
    def IsInternal(self,Item : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None
        """
    def IsMultiple(self) -> bool: 
        """
        None
        """
    def Item(self,OriKey : int,Item : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None
        """
    def Key(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def RemoveItem(self,OriKey : int,Item : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None

        None
        """
    @overload
    def RemoveItem(self,Item : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def SetKey(self,Key : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Key : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class TopOpeBRepTool_face():
    """
    None
    """
    def Ffinite(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def Finite(self) -> bool: 
        """
        None
        """
    def Init(self,W : OCP.TopoDS.TopoDS_Wire,Fref : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def RealF(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def W(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_makeTransition():
    """
    None
    """
    def Getfactor(self) -> float: 
        """
        None
        """
    def HasRest(self) -> bool: 
        """
        None
        """
    def Initialize(self,E : OCP.TopoDS.TopoDS_Edge,pbef : float,paft : float,parE : float,FS : OCP.TopoDS.TopoDS_Face,uv : OCP.gp.gp_Pnt2d,factor : float) -> bool: 
        """
        None
        """
    def IsT2d(self) -> bool: 
        """
        None
        """
    def MkT2donE(self,stb : OCP.TopAbs.TopAbs_State,sta : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def MkT3dproj(self,stb : OCP.TopAbs.TopAbs_State,sta : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def MkT3onE(self,stb : OCP.TopAbs.TopAbs_State,sta : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def MkTonE(self,stb : OCP.TopAbs.TopAbs_State,sta : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def SetRest(self,ES : OCP.TopoDS.TopoDS_Edge,parES : float) -> bool: 
        """
        None
        """
    def Setfactor(self,factor : float) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepTool_mkTondgE():
    """
    None
    """
    def GetAllRest(self,lEi : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None
        """
    def Initialize(self,dgE : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,uvi : OCP.gp.gp_Pnt2d,Fi : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def IsT2d(self) -> bool: 
        """
        None
        """
    @overload
    def MkTonE(self,Ei : OCP.TopoDS.TopoDS_Edge,mkT : int,par1 : float,par2 : float) -> bool: 
        """
        None

        None
        """
    @overload
    def MkTonE(self,mkT : int,par1 : float,par2 : float) -> bool: ...
    def SetRest(self,pari : float,Ei : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def SetclE(self,clE : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
def BASISCURVE2D(C : OCP.Geom2d.Geom2d_Curve) -> OCP.Geom2d.Geom2d_Curve:
    """
    None
    """
def FBOX_Box(S : OCP.TopoDS.TopoDS_Shape) -> OCP.Bnd.Bnd_Box:
    """
    None
    """
def FBOX_GetHBoxTool() -> TopOpeBRepTool_HBoxTool:
    """
    None
    """
def FBOX_Prepare() -> None:
    """
    None
    """
def FC2D_AddNewCurveOnSurface(PC : OCP.Geom2d.Geom2d_Curve,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,f : float,l : float,tol : float) -> int:
    """
    None
    """
@overload
def FC2D_CurveOnSurface(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,EF : OCP.TopoDS.TopoDS_Edge,f : float,l : float,tol : float,trim3d : bool=False) -> OCP.Geom2d.Geom2d_Curve:
    """
    None

    None
    """
@overload
def FC2D_CurveOnSurface(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,f : float,l : float,tol : float,trim3d : bool=False) -> OCP.Geom2d.Geom2d_Curve:
    pass
def FC2D_EditableCurveOnSurface(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,f : float,l : float,tol : float,trim3d : bool=False) -> OCP.Geom2d.Geom2d_Curve:
    """
    None
    """
def FC2D_HasC3D(E : OCP.TopoDS.TopoDS_Edge) -> bool:
    """
    None
    """
def FC2D_HasCurveOnSurface(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> bool:
    """
    None
    """
@overload
def FC2D_HasNewCurveOnSurface(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,C2D : OCP.Geom2d.Geom2d_Curve) -> bool:
    """
    None

    None
    """
@overload
def FC2D_HasNewCurveOnSurface(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,C2D : OCP.Geom2d.Geom2d_Curve,f : float,l : float,tol : float) -> bool:
    pass
@overload
def FC2D_HasOldCurveOnSurface(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,C2D : OCP.Geom2d.Geom2d_Curve,f : float,l : float,tol : float) -> bool:
    """
    None

    None
    """
@overload
def FC2D_HasOldCurveOnSurface(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,C2D : OCP.Geom2d.Geom2d_Curve) -> bool:
    pass
def FC2D_MakeCurveOnSurface(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,f : float,l : float,tol : float,trim3d : bool=False) -> OCP.Geom2d.Geom2d_Curve:
    """
    None
    """
def FC2D_Prepare(S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> int:
    """
    None
    """
@overload
def FSC_GetPSC(S : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepTool_ShapeClassifier:
    """
    None

    None
    """
@overload
def FSC_GetPSC() -> TopOpeBRepTool_ShapeClassifier:
    pass
def FSC_StateEonFace(E : OCP.TopoDS.TopoDS_Shape,t : float,F : OCP.TopoDS.TopoDS_Shape,PSC : TopOpeBRepTool_ShapeClassifier) -> OCP.TopAbs.TopAbs_State:
    """
    None
    """
def FSC_StatePonFace(P : OCP.gp.gp_Pnt,F : OCP.TopoDS.TopoDS_Shape,PSC : TopOpeBRepTool_ShapeClassifier) -> OCP.TopAbs.TopAbs_State:
    """
    None
    """
def FTOL_FaceTolerances(B1 : OCP.Bnd.Bnd_Box,B2 : OCP.Bnd.Bnd_Box,myFace1 : OCP.TopoDS.TopoDS_Face,myFace2 : OCP.TopoDS.TopoDS_Face,mySurface1 : OCP.BRepAdaptor.BRepAdaptor_Surface,mySurface2 : OCP.BRepAdaptor.BRepAdaptor_Surface,myTol1 : float,myTol2 : float,Deflection : float,MaxUV : float) -> None:
    """
    None
    """
def FTOL_FaceTolerances2d(B1 : OCP.Bnd.Bnd_Box,B2 : OCP.Bnd.Bnd_Box,myFace1 : OCP.TopoDS.TopoDS_Face,myFace2 : OCP.TopoDS.TopoDS_Face,mySurface1 : OCP.BRepAdaptor.BRepAdaptor_Surface,mySurface2 : OCP.BRepAdaptor.BRepAdaptor_Surface,myTol1 : float,myTol2 : float) -> None:
    """
    None
    """
@overload
def FTOL_FaceTolerances3d(B1 : OCP.Bnd.Bnd_Box,B2 : OCP.Bnd.Bnd_Box,myFace1 : OCP.TopoDS.TopoDS_Face,myFace2 : OCP.TopoDS.TopoDS_Face,mySurface1 : OCP.BRepAdaptor.BRepAdaptor_Surface,mySurface2 : OCP.BRepAdaptor.BRepAdaptor_Surface,myTol1 : float,myTol2 : float,Deflection : float,MaxUV : float) -> None:
    """
    None

    None
    """
@overload
def FTOL_FaceTolerances3d(myFace1 : OCP.TopoDS.TopoDS_Face,myFace2 : OCP.TopoDS.TopoDS_Face,Tol : float) -> None:
    pass
def FUN_ds_CopyEdge(Ein : OCP.TopoDS.TopoDS_Shape,Eou : OCP.TopoDS.TopoDS_Shape) -> None:
    """
    None
    """
def FUN_ds_Parameter(E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape,P : float) -> None:
    """
    None
    """
def FUN_nearestISO(F : OCP.TopoDS.TopoDS_Face,xpar : float,isoU : bool,xinf : float,xsup : float) -> bool:
    """
    None
    """
def FUN_quadCT(CT : OCP.GeomAbs.GeomAbs_CurveType) -> bool:
    """
    None
    """
def FUN_tool_ClosingE(E : OCP.TopoDS.TopoDS_Edge,W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face) -> bool:
    """
    None
    """
def FUN_tool_EboundF(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> bool:
    """
    None
    """
def FUN_tool_EitangenttoFe(ngFe : OCP.gp.gp_Dir,Ei : OCP.TopoDS.TopoDS_Edge,parOnEi : float) -> bool:
    """
    None
    """
def FUN_tool_Eshared(v : OCP.TopoDS.TopoDS_Shape,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape,Eshared : OCP.TopoDS.TopoDS_Shape) -> bool:
    """
    None
    """
def FUN_tool_EtgF(paronE : float,E : OCP.TopoDS.TopoDS_Edge,p2d : OCP.gp.gp_Pnt2d,F : OCP.TopoDS.TopoDS_Face,tola : float) -> bool:
    """
    None
    """
def FUN_tool_EtgOOE(paronE : float,E : OCP.TopoDS.TopoDS_Edge,paronOOE : float,OOE : OCP.TopoDS.TopoDS_Edge,tola : float) -> bool:
    """
    None
    """
def FUN_tool_IsClosingE(E : OCP.TopoDS.TopoDS_Edge,S : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Face) -> bool:
    """
    None
    """
def FUN_tool_MakeWire(loE : OCP.TopTools.TopTools_ListOfShape,newW : OCP.TopoDS.TopoDS_Wire) -> bool:
    """
    None
    """
@overload
def FUN_tool_PinC(P : OCP.gp.gp_Pnt,BAC : OCP.BRepAdaptor.BRepAdaptor_Curve,tol : float) -> bool:
    """
    None

    None
    """
@overload
def FUN_tool_PinC(P : OCP.gp.gp_Pnt,BAC : OCP.BRepAdaptor.BRepAdaptor_Curve,pmin : float,pmax : float,tol : float) -> bool:
    pass
def FUN_tool_SameOri(E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge) -> bool:
    """
    None
    """
def FUN_tool_UpdateBnd2d(B2d : OCP.Bnd.Bnd_Box2d,newB2d : OCP.Bnd.Bnd_Box2d) -> None:
    """
    None
    """
@overload
def FUN_tool_bounds(F : OCP.TopoDS.TopoDS_Shape,u1 : float,u2 : float,v1 : float,v2 : float) -> bool:
    """
    None

    None
    """
@overload
def FUN_tool_bounds(E : OCP.TopoDS.TopoDS_Edge,f : float,l : float) -> None:
    pass
def FUN_tool_closed(S : OCP.Geom.Geom_Surface,uclosed : bool,uperiod : float,vclosed : bool,vperiod : float) -> bool:
    """
    None
    """
@overload
def FUN_tool_closedS(F : OCP.TopoDS.TopoDS_Shape,inU : bool,xmin : float,xper : float) -> bool:
    """
    None

    None

    None
    """
@overload
def FUN_tool_closedS(F : OCP.TopoDS.TopoDS_Shape,uclosed : bool,uperiod : float,vclosed : bool,vperiod : float) -> bool:
    pass
@overload
def FUN_tool_closedS(F : OCP.TopoDS.TopoDS_Shape) -> bool:
    pass
def FUN_tool_comparebndkole(sh1 : OCP.TopoDS.TopoDS_Shape,sh2 : OCP.TopoDS.TopoDS_Shape) -> int:
    """
    None
    """
@overload
def FUN_tool_curvesSO(E1 : OCP.TopoDS.TopoDS_Edge,p1 : float,E2 : OCP.TopoDS.TopoDS_Edge,so : bool) -> bool:
    """
    None

    None

    None
    """
@overload
def FUN_tool_curvesSO(E1 : OCP.TopoDS.TopoDS_Edge,p1 : float,E2 : OCP.TopoDS.TopoDS_Edge,p2 : float,so : bool) -> bool:
    pass
@overload
def FUN_tool_curvesSO(E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,so : bool) -> bool:
    pass
def FUN_tool_cylinder(F : OCP.TopoDS.TopoDS_Shape) -> bool:
    """
    None
    """
@overload
def FUN_tool_dirC(par : float,C : OCP.Geom.Geom_Curve) -> OCP.gp.gp_Dir:
    """
    None

    None
    """
@overload
def FUN_tool_dirC(par : float,BAC : OCP.BRepAdaptor.BRepAdaptor_Curve) -> OCP.gp.gp_Dir:
    pass
def FUN_tool_direct(F : OCP.TopoDS.TopoDS_Face,direct : bool) -> bool:
    """
    None
    """
def FUN_tool_findAncestor(lF : OCP.TopTools.TopTools_ListOfShape,E : OCP.TopoDS.TopoDS_Edge,Fanc : OCP.TopoDS.TopoDS_Face) -> bool:
    """
    None
    """
def FUN_tool_findPinBAC(BAC : OCP.BRepAdaptor.BRepAdaptor_Curve,P : OCP.gp.gp_Pnt,par : float) -> bool:
    """
    None
    """
def FUN_tool_findPinE(E : OCP.TopoDS.TopoDS_Shape,P : OCP.gp.gp_Pnt,par : float) -> bool:
    """
    None
    """
def FUN_tool_findparinBAC(BAC : OCP.BRepAdaptor.BRepAdaptor_Curve,par : float) -> bool:
    """
    None
    """
def FUN_tool_findparinE(E : OCP.TopoDS.TopoDS_Shape,par : float) -> bool:
    """
    None
    """
def FUN_tool_geombounds(F : OCP.TopoDS.TopoDS_Face,u1 : float,u2 : float,v1 : float,v2 : float) -> bool:
    """
    None
    """
def FUN_tool_getdxx(F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge,parE : float,XX : OCP.gp.gp_Vec2d) -> bool:
    """
    None
    """
@overload
def FUN_tool_getgeomxx(Fi : OCP.TopoDS.TopoDS_Face,Ei : OCP.TopoDS.TopoDS_Edge,parOnEi : float) -> OCP.gp.gp_Vec:
    """
    None

    None
    """
@overload
def FUN_tool_getgeomxx(Fi : OCP.TopoDS.TopoDS_Face,Ei : OCP.TopoDS.TopoDS_Edge,parOnEi : float,ngFi : OCP.gp.gp_Dir) -> OCP.gp.gp_Vec:
    pass
@overload
def FUN_tool_getindex(ponc : OCP.Extrema.Extrema_ExtPC) -> int:
    """
    None

    None
    """
@overload
def FUN_tool_getindex(ponc : OCP.Extrema.Extrema_ExtPC2d) -> int:
    pass
@overload
def FUN_tool_getxx(Fi : OCP.TopoDS.TopoDS_Face,Ei : OCP.TopoDS.TopoDS_Edge,parOnEi : float,XX : OCP.gp.gp_Dir) -> bool:
    """
    None

    None
    """
@overload
def FUN_tool_getxx(Fi : OCP.TopoDS.TopoDS_Face,Ei : OCP.TopoDS.TopoDS_Edge,parOnEi : float,ngFi : OCP.gp.gp_Dir,XX : OCP.gp.gp_Dir) -> bool:
    pass
def FUN_tool_haspc(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> bool:
    """
    None
    """
def FUN_tool_inS(subshape : OCP.TopoDS.TopoDS_Shape,shape : OCP.TopoDS.TopoDS_Shape) -> bool:
    """
    None
    """
def FUN_tool_isobounds(F : OCP.TopoDS.TopoDS_Shape,u1 : float,u2 : float,v1 : float,v2 : float) -> bool:
    """
    None
    """
@overload
def FUN_tool_line(E : OCP.TopoDS.TopoDS_Edge) -> bool:
    """
    None

    None

    None

    None
    """
@overload
def FUN_tool_line(C3d : OCP.Geom.Geom_Curve) -> bool:
    pass
@overload
def FUN_tool_line(C2d : OCP.Geom2d.Geom2d_Curve) -> bool:
    pass
@overload
def FUN_tool_line(BAC : OCP.BRepAdaptor.BRepAdaptor_Curve) -> bool:
    pass
@overload
def FUN_tool_maxtol(S : OCP.TopoDS.TopoDS_Shape) -> float:
    """
    None

    None
    """
@overload
def FUN_tool_maxtol(S : OCP.TopoDS.TopoDS_Shape,typ : OCP.TopAbs.TopAbs_ShapeEnum,tol : float) -> bool:
    pass
def FUN_tool_mkBnd2d(W : OCP.TopoDS.TopoDS_Shape,FF : OCP.TopoDS.TopoDS_Shape,B2d : OCP.Bnd.Bnd_Box2d) -> None:
    """
    None
    """
def FUN_tool_nC2dINSIDES(tgC2d : OCP.gp.gp_Dir2d) -> OCP.gp.gp_Dir2d:
    """
    None
    """
def FUN_tool_nCinsideS(tgC : OCP.gp.gp_Dir,ngS : OCP.gp.gp_Dir) -> OCP.gp.gp_Dir:
    """
    None
    """
def FUN_tool_nbshapes(S : OCP.TopoDS.TopoDS_Shape,typ : OCP.TopAbs.TopAbs_ShapeEnum) -> int:
    """
    None
    """
def FUN_tool_ngS(p2d : OCP.gp.gp_Pnt2d,S : OCP.Geom.Geom_Surface) -> OCP.gp.gp_Dir:
    """
    None
    """
@overload
def FUN_tool_nggeomF(p2d : OCP.gp.gp_Pnt2d,F : OCP.TopoDS.TopoDS_Face) -> OCP.gp.gp_Vec:
    """
    None

    None

    None
    """
@overload
def FUN_tool_nggeomF(paronE : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,nggeomF : OCP.gp.gp_Vec) -> bool:
    pass
@overload
def FUN_tool_nggeomF(paronE : float,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,nggeomF : OCP.gp.gp_Vec,tol : float) -> bool:
    pass
def FUN_tool_onapex(p2d : OCP.gp.gp_Pnt2d,S : OCP.Geom.Geom_Surface) -> bool:
    """
    None
    """
def FUN_tool_orientEinF(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,oriEinF : OCP.TopAbs.TopAbs_Orientation) -> bool:
    """
    None
    """
def FUN_tool_orientEinFFORWARD(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,oriEinF : OCP.TopAbs.TopAbs_Orientation) -> bool:
    """
    None
    """
def FUN_tool_orientVinE(v : OCP.TopoDS.TopoDS_Vertex,e : OCP.TopoDS.TopoDS_Edge) -> int:
    """
    None
    """
def FUN_tool_outbounds(Sh : OCP.TopoDS.TopoDS_Shape,u1 : float,u2 : float,v1 : float,v2 : float,outbounds : bool) -> bool:
    """
    None
    """
@overload
def FUN_tool_parE(E0 : OCP.TopoDS.TopoDS_Edge,par0 : float,E : OCP.TopoDS.TopoDS_Edge,par : float) -> bool:
    """
    None

    None
    """
@overload
def FUN_tool_parE(E0 : OCP.TopoDS.TopoDS_Edge,par0 : float,E : OCP.TopoDS.TopoDS_Edge,par : float,tol : float) -> bool:
    pass
@overload
def FUN_tool_parF(E : OCP.TopoDS.TopoDS_Edge,par : float,F : OCP.TopoDS.TopoDS_Face,UV : OCP.gp.gp_Pnt2d,tol : float) -> bool:
    """
    None

    None
    """
@overload
def FUN_tool_parF(E : OCP.TopoDS.TopoDS_Edge,par : float,F : OCP.TopoDS.TopoDS_Face,UV : OCP.gp.gp_Pnt2d) -> bool:
    pass
def FUN_tool_parVonE(v : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,par : float) -> bool:
    """
    None
    """
@overload
def FUN_tool_paronEF(E : OCP.TopoDS.TopoDS_Edge,par : float,F : OCP.TopoDS.TopoDS_Face,UV : OCP.gp.gp_Pnt2d) -> bool:
    """
    None

    None
    """
@overload
def FUN_tool_paronEF(E : OCP.TopoDS.TopoDS_Edge,par : float,F : OCP.TopoDS.TopoDS_Face,UV : OCP.gp.gp_Pnt2d,tol : float) -> bool:
    pass
@overload
def FUN_tool_pcurveonF(F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge) -> bool:
    """
    None

    None
    """
@overload
def FUN_tool_pcurveonF(fF : OCP.TopoDS.TopoDS_Face,faultyE : OCP.TopoDS.TopoDS_Edge,C2d : OCP.Geom2d.Geom2d_Curve,newf : OCP.TopoDS.TopoDS_Face) -> bool:
    pass
def FUN_tool_plane(F : OCP.TopoDS.TopoDS_Shape) -> bool:
    """
    None
    """
@overload
def FUN_tool_projPonC(P : OCP.gp.gp_Pnt,tole : float,BAC : OCP.BRepAdaptor.BRepAdaptor_Curve,pmin : float,pmax : float,param : float,dist : float) -> bool:
    """
    None

    None

    None
    """
@overload
def FUN_tool_projPonC(P : OCP.gp.gp_Pnt,BAC : OCP.BRepAdaptor.BRepAdaptor_Curve,param : float,dist : float) -> bool:
    pass
@overload
def FUN_tool_projPonC(P : OCP.gp.gp_Pnt,BAC : OCP.BRepAdaptor.BRepAdaptor_Curve,pmin : float,pmax : float,param : float,dist : float) -> bool:
    pass
@overload
def FUN_tool_projPonC2D(P : OCP.gp.gp_Pnt,tole : float,BAC2D : OCP.BRepAdaptor.BRepAdaptor_Curve2d,pmin : float,pmax : float,param : float,dist : float) -> bool:
    """
    None

    None

    None
    """
@overload
def FUN_tool_projPonC2D(P : OCP.gp.gp_Pnt,BAC2D : OCP.BRepAdaptor.BRepAdaptor_Curve2d,param : float,dist : float) -> bool:
    pass
@overload
def FUN_tool_projPonC2D(P : OCP.gp.gp_Pnt,BAC2D : OCP.BRepAdaptor.BRepAdaptor_Curve2d,pmin : float,pmax : float,param : float,dist : float) -> bool:
    pass
@overload
def FUN_tool_projPonE(P : OCP.gp.gp_Pnt,E : OCP.TopoDS.TopoDS_Edge,param : float,dist : float) -> bool:
    """
    None

    None
    """
@overload
def FUN_tool_projPonE(P : OCP.gp.gp_Pnt,tole : float,E : OCP.TopoDS.TopoDS_Edge,param : float,dist : float) -> bool:
    pass
def FUN_tool_projPonF(P : OCP.gp.gp_Pnt,F : OCP.TopoDS.TopoDS_Face,UV : OCP.gp.gp_Pnt2d,dist : float,anExtFlag : OCP.Extrema.Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,anExtAlgo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> bool:
    """
    None
    """
def FUN_tool_projPonS(P : OCP.gp.gp_Pnt,S : OCP.Geom.Geom_Surface,UV : OCP.gp.gp_Pnt2d,dist : float,anExtFlag : OCP.Extrema.Extrema_ExtFlag=Extrema_ExtFlag.Extrema_ExtFlag_MINMAX,anExtAlgo : OCP.Extrema.Extrema_ExtAlgo=Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> bool:
    """
    None
    """
def FUN_tool_projPonboundedF(P : OCP.gp.gp_Pnt,F : OCP.TopoDS.TopoDS_Face,UV : OCP.gp.gp_Pnt2d,dist : float) -> bool:
    """
    None
    """
@overload
def FUN_tool_quad(E : OCP.TopoDS.TopoDS_Edge) -> bool:
    """
    None

    None

    None

    None

    None

    None
    """
@overload
def FUN_tool_quad(F : OCP.TopoDS.TopoDS_Face) -> bool:
    pass
@overload
def FUN_tool_quad(BAC : OCP.BRepAdaptor.BRepAdaptor_Curve) -> bool:
    pass
@overload
def FUN_tool_quad(pc : OCP.Geom2d.Geom2d_Curve) -> bool:
    pass
@overload
def FUN_tool_quad(C3d : OCP.Geom.Geom_Curve) -> bool:
    pass
@overload
def FUN_tool_quad(S : OCP.Geom.Geom_Surface) -> bool:
    pass
def FUN_tool_shapes(S : OCP.TopoDS.TopoDS_Shape,typ : OCP.TopAbs.TopAbs_ShapeEnum,ltyp : OCP.TopTools.TopTools_ListOfShape) -> None:
    """
    None
    """
@overload
def FUN_tool_staPinE(P : OCP.gp.gp_Pnt,E : OCP.TopoDS.TopoDS_Edge,tol : float) -> OCP.TopAbs.TopAbs_State:
    """
    None

    None
    """
@overload
def FUN_tool_staPinE(P : OCP.gp.gp_Pnt,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopAbs.TopAbs_State:
    pass
def FUN_tool_tggeomE(paronE : float,E : OCP.TopoDS.TopoDS_Edge) -> OCP.gp.gp_Vec:
    """
    None
    """
def FUN_tool_tolUV(F : OCP.TopoDS.TopoDS_Face,tolu : float,tolv : float) -> None:
    """
    None
    """
def FUN_tool_typ(E : OCP.TopoDS.TopoDS_Edge) -> OCP.GeomAbs.GeomAbs_CurveType:
    """
    None
    """
@overload
def FUN_tool_value(UV : OCP.gp.gp_Pnt2d,F : OCP.TopoDS.TopoDS_Face,P : OCP.gp.gp_Pnt) -> bool:
    """
    None

    None
    """
@overload
def FUN_tool_value(par : float,E : OCP.TopoDS.TopoDS_Edge,P : OCP.gp.gp_Pnt) -> bool:
    pass
TopOpeBRepTool_APPROX: OCP.TopOpeBRepTool.TopOpeBRepTool_OutCurveType # value = <TopOpeBRepTool_OutCurveType.TopOpeBRepTool_APPROX: 1>
TopOpeBRepTool_BSPLINE1: OCP.TopOpeBRepTool.TopOpeBRepTool_OutCurveType # value = <TopOpeBRepTool_OutCurveType.TopOpeBRepTool_BSPLINE1: 0>
TopOpeBRepTool_INTERPOL: OCP.TopOpeBRepTool.TopOpeBRepTool_OutCurveType # value = <TopOpeBRepTool_OutCurveType.TopOpeBRepTool_INTERPOL: 2>
