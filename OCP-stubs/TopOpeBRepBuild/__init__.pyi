import OCP.TopOpeBRepBuild
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.NCollection
import io
import OCP.TopOpeBRepTool
import OCP.gp
import OCP.TopAbs
import OCP.TopOpeBRepDS
import OCP.Standard
import OCP.TopoDS
import OCP.TCollection
import OCP.TColStd
__all__  = [
"TopOpeBRepBuild_AreaBuilder",
"TopOpeBRepBuild_Area2dBuilder",
"TopOpeBRepBuild_Area3dBuilder",
"TopOpeBRepBuild_Area1dBuilder",
"TopOpeBRepBuild_BlockBuilder",
"TopOpeBRepBuild_BlockIterator",
"TopOpeBRepBuild_Builder",
"TopOpeBRepBuild_Builder1",
"TopOpeBRepBuild_BuilderON",
"TopOpeBRepBuild_LoopClassifier",
"TopOpeBRepBuild_CorrectFace2d",
"TopOpeBRepBuild_DataMapOfShapeListOfShapeListOfShape",
"TopOpeBRepBuild_EdgeBuilder",
"TopOpeBRepBuild_FaceAreaBuilder",
"TopOpeBRepBuild_FaceBuilder",
"TopOpeBRepBuild_FuseFace",
"TopOpeBRepBuild_GIter",
"TopOpeBRepBuild_GTool",
"TopOpeBRepBuild_GTopo",
"TopOpeBRepBuild_HBuilder",
"TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo",
"TopOpeBRepBuild_ListOfListOfLoop",
"TopOpeBRepBuild_ListOfLoop",
"TopOpeBRepBuild_ListOfPave",
"TopOpeBRepBuild_ListOfShapeListOfShape",
"TopOpeBRepBuild_Loop",
"TopOpeBRepBuild_CompositeClassifier",
"TopOpeBRepBuild_LoopEnum",
"TopOpeBRepBuild_LoopSet",
"TopOpeBRepBuild_Pave",
"TopOpeBRepBuild_PaveClassifier",
"TopOpeBRepBuild_PaveSet",
"TopOpeBRepBuild_ShapeListOfShape",
"TopOpeBRepBuild_ShapeSet",
"TopOpeBRepBuild_ShellFaceClassifier",
"TopOpeBRepBuild_ShellFaceSet",
"TopOpeBRepBuild_ShellToSolid",
"TopOpeBRepBuild_SolidAreaBuilder",
"TopOpeBRepBuild_SolidBuilder",
"TopOpeBRepBuild_Tools",
"TopOpeBRepBuild_Tools2d",
"TopOpeBRepBuild_VertexInfo",
"TopOpeBRepBuild_WireEdgeClassifier",
"TopOpeBRepBuild_WireEdgeSet",
"TopOpeBRepBuild_WireToFace",
"TopOpeBRepBuild_ANYLOOP",
"TopOpeBRepBuild_BLOCK",
"TopOpeBRepBuild_BOUNDARY"
]
class TopOpeBRepBuild_AreaBuilder():
    """
    The AreaBuilder algorithm is used to reconstruct complex topological objects as Faces or Solids. * Loop is the composite topological object of the boundary. Wire for a Face. Shell for a Solid. * LoopSet is a tool describing the object to build. It gives an iteration on Loops. For each Loop it tells if it is on the boundary or if it is an interference. * LoopClassifier is an algorithm used to test if a Loop is inside another Loop. The result of the reconstruction is an iteration on the reconstructed areas. An area is described by a set of Loops. A AreaBuilder is built with : - a LoopSet describing the object to reconstruct. - a LoopClassifier providing the classification algorithm.
    """
    def ADD_LISTOFLoop_TO_LISTOFLoop(self,LOL1 : TopOpeBRepBuild_ListOfLoop,LOL2 : TopOpeBRepBuild_ListOfLoop,s : capsule=None,s1 : capsule=None,s2 : capsule=None) -> None: 
        """
        None
        """
    def ADD_Loop_TO_LISTOFLoop(self,L : TopOpeBRepBuild_Loop,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    def InitArea(self) -> int: 
        """
        Initialize iteration on areas.
        """
    def InitAreaBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        Sets a AreaBuilder to find the areas on the shapes described by <LS> using the classifier <LC>.
        """
    def InitLoop(self) -> int: 
        """
        Initialize iteration on loops of current Area.
        """
    def Loop(self) -> TopOpeBRepBuild_Loop: 
        """
        Returns the current Loop in the current area.
        """
    def MoreArea(self) -> bool: 
        """
        None
        """
    def MoreLoop(self) -> bool: 
        """
        None
        """
    def NextArea(self) -> None: 
        """
        None
        """
    def NextLoop(self) -> None: 
        """
        None
        """
    def REM_Loop_FROM_LISTOFLoop(self,ITLOL : Any,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    @overload
    def __init__(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_Area2dBuilder(TopOpeBRepBuild_AreaBuilder):
    """
    The Area2dBuilder algorithm is used to construct Faces from a LoopSet, where the Loop is the composite topological object of the boundary, here wire or block of edges. The LoopSet gives an iteration on Loops. For each Loop it indicates if it is on the boundary (wire) or if it results from an interference (block of edges). The result of the Area2dBuilder is an iteration on areas. An area is described by a set of Loops.
    """
    def ADD_LISTOFLoop_TO_LISTOFLoop(self,LOL1 : TopOpeBRepBuild_ListOfLoop,LOL2 : TopOpeBRepBuild_ListOfLoop,s : capsule=None,s1 : capsule=None,s2 : capsule=None) -> None: 
        """
        None
        """
    def ADD_Loop_TO_LISTOFLoop(self,L : TopOpeBRepBuild_Loop,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    def InitArea(self) -> int: 
        """
        Initialize iteration on areas.
        """
    def InitAreaBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        Sets a Area1dBuilder to find the areas of the shapes described by <LS> using the classifier <LC>.
        """
    def InitLoop(self) -> int: 
        """
        Initialize iteration on loops of current Area.
        """
    def Loop(self) -> TopOpeBRepBuild_Loop: 
        """
        Returns the current Loop in the current area.
        """
    def MoreArea(self) -> bool: 
        """
        None
        """
    def MoreLoop(self) -> bool: 
        """
        None
        """
    def NextArea(self) -> None: 
        """
        None
        """
    def NextLoop(self) -> None: 
        """
        None
        """
    def REM_Loop_FROM_LISTOFLoop(self,ITLOL : Any,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    @overload
    def __init__(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_Area3dBuilder(TopOpeBRepBuild_AreaBuilder):
    """
    The Area3dBuilder algorithm is used to construct Solids from a LoopSet, where the Loop is the composite topological object of the boundary, here wire or block of edges. The LoopSet gives an iteration on Loops. For each Loop it indicates if it is on the boundary (wire) or if it results from an interference (block of edges). The result of the Area3dBuilder is an iteration on areas. An area is described by a set of Loops.
    """
    def ADD_LISTOFLoop_TO_LISTOFLoop(self,LOL1 : TopOpeBRepBuild_ListOfLoop,LOL2 : TopOpeBRepBuild_ListOfLoop,s : capsule=None,s1 : capsule=None,s2 : capsule=None) -> None: 
        """
        None
        """
    def ADD_Loop_TO_LISTOFLoop(self,L : TopOpeBRepBuild_Loop,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    def InitArea(self) -> int: 
        """
        Initialize iteration on areas.
        """
    def InitAreaBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        Sets a Area1dBuilder to find the areas of the shapes described by <LS> using the classifier <LC>.
        """
    def InitLoop(self) -> int: 
        """
        Initialize iteration on loops of current Area.
        """
    def Loop(self) -> TopOpeBRepBuild_Loop: 
        """
        Returns the current Loop in the current area.
        """
    def MoreArea(self) -> bool: 
        """
        None
        """
    def MoreLoop(self) -> bool: 
        """
        None
        """
    def NextArea(self) -> None: 
        """
        None
        """
    def NextLoop(self) -> None: 
        """
        None
        """
    def REM_Loop_FROM_LISTOFLoop(self,ITLOL : Any,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: ...
    pass
class TopOpeBRepBuild_Area1dBuilder(TopOpeBRepBuild_AreaBuilder):
    """
    None
    """
    def ADD_LISTOFLoop_TO_LISTOFLoop(self,LOL1 : TopOpeBRepBuild_ListOfLoop,LOL2 : TopOpeBRepBuild_ListOfLoop,s : capsule=None,s1 : capsule=None,s2 : capsule=None) -> None: 
        """
        None
        """
    def ADD_Loop_TO_LISTOFLoop(self,L : TopOpeBRepBuild_Loop,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    @staticmethod
    def DumpList_s(L : TopOpeBRepBuild_ListOfLoop) -> None: 
        """
        None
        """
    def InitArea(self) -> int: 
        """
        Initialize iteration on areas.
        """
    def InitAreaBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        Sets a Area1dBuilder to find the areas of the shapes described by <LS> using the classifier <LC>.
        """
    def InitLoop(self) -> int: 
        """
        Initialize iteration on loops of current Area.
        """
    def Loop(self) -> TopOpeBRepBuild_Loop: 
        """
        Returns the current Loop in the current area.
        """
    def MoreArea(self) -> bool: 
        """
        None
        """
    def MoreLoop(self) -> bool: 
        """
        None
        """
    def NextArea(self) -> None: 
        """
        None
        """
    def NextLoop(self) -> None: 
        """
        None
        """
    def REM_Loop_FROM_LISTOFLoop(self,ITLOL : Any,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    @overload
    def __init__(self,LS : TopOpeBRepBuild_PaveSet,LC : TopOpeBRepBuild_PaveClassifier,ForceClass : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_BlockBuilder():
    """
    None
    """
    def AddElement(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def BlockIterator(self) -> TopOpeBRepBuild_BlockIterator: 
        """
        None
        """
    def CurrentBlockIsRegular(self) -> bool: 
        """
        None
        """
    @overload
    def Element(self,BI : TopOpeBRepBuild_BlockIterator) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the current element of <BI>.

        None

        None
        """
    @overload
    def Element(self,S : OCP.TopoDS.TopoDS_Shape) -> int: ...
    @overload
    def Element(self,I : int) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def ElementIsValid(self,I : int) -> bool: 
        """
        None

        None
        """
    @overload
    def ElementIsValid(self,BI : TopOpeBRepBuild_BlockIterator) -> bool: ...
    def InitBlock(self) -> None: 
        """
        None
        """
    def MakeBlock(self,SS : TopOpeBRepBuild_ShapeSet) -> None: 
        """
        None
        """
    def MoreBlock(self) -> bool: 
        """
        None
        """
    def NextBlock(self) -> None: 
        """
        None
        """
    @overload
    def SetValid(self,BI : TopOpeBRepBuild_BlockIterator,isvalid : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetValid(self,I : int,isvalid : bool) -> None: ...
    @overload
    def __init__(self,SS : TopOpeBRepBuild_ShapeSet) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_BlockIterator():
    """
    Iterator on the elements of a block.
    """
    def Extent(self) -> int: 
        """
        None

        None
        """
    def Initialize(self) -> None: 
        """
        None

        None
        """
    def More(self) -> bool: 
        """
        None

        None
        """
    def Next(self) -> None: 
        """
        None

        None
        """
    def Value(self) -> int: 
        """
        None

        None
        """
    @overload
    def __init__(self,Lower : int,Upper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_Builder():
    """
    The Builder algorithm constructs topological objects from an existing topology and new geometries attached to the topology. It is used to construct the result of a topological operation; the existing topologies are the parts involved in the topological operation and the new geometries are the intersection lines and points.
    """
    def AddONPatchesSFS(self,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def BuildEdges(self,DS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        update the DS by creating new geometries. create shapes from the new geometries.
        """
    def BuildTool(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_BuildTool: 
        """
        None
        """
    def BuildVertices(self,DS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        update the DS by creating new geometries. create vertices on DS points.
        """
    def ChangeBuildTool(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_BuildTool: 
        """
        None
        """
    def ChangeClassify(self,B : bool) -> None: 
        """
        None
        """
    def ChangeMSplit(self,s : OCP.TopAbs.TopAbs_State) -> OCP.TopOpeBRepDS.TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State: 
        """
        None
        """
    def ChangeSplit(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a ref.on the list of shapes connected to <S> as <TB> split parts of <S>. Mark <S> as split in <TB> parts.
        """
    def Classify(self) -> bool: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Removes all splits and merges already performed. Does NOT clear the handled DS.
        """
    def ClearMaps(self) -> None: 
        """
        None
        """
    @staticmethod
    def Contains_s(S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def DataStructure(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure: 
        """
        returns the DS handled by this builder
        """
    def End(self) -> None: 
        """
        None
        """
    def FillOnPatches(self,anEdgesON : OCP.TopTools.TopTools_ListOfShape,aBaseFace : OCP.TopoDS.TopoDS_Shape,avoidMap : OCP.TopTools.TopTools_IndexedMapOfOrientedShape) -> None: 
        """
        None
        """
    def FillSecEdgeAncestorMap(self,aShapeRank : int,aMapON : OCP.TopTools.TopTools_MapOfShape,anAncMap : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        Fills anAncMap with pairs (edge,ancestor edge) for each split from the map aMapON for the shape object identified by ShapeRank
        """
    def FindFacesTouchingEdge(self,aFace : OCP.TopoDS.TopoDS_Shape,anEdge : OCP.TopoDS.TopoDS_Shape,aShRank : int,aFaces : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def FindIsKPart(self) -> int: 
        """
        None
        """
    def FindSameDomain(self,L1 : OCP.TopTools.TopTools_ListOfShape,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def FindSameDomainSameOrientation(self,LSO : OCP.TopTools.TopTools_ListOfShape,LDO : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def FindSameRank(self,L1 : OCP.TopTools.TopTools_ListOfShape,R : int,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GClearMaps(self) -> None: 
        """
        None
        """
    @staticmethod
    def GContains_s(S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def GCopyList_s(Lin : OCP.TopTools.TopTools_ListOfShape,i1 : int,i2 : int,Lou : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def GCopyList_s(Lin : OCP.TopTools.TopTools_ListOfShape,Lou : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    def GEDBUMakeEdges(self,EF : OCP.TopoDS.TopoDS_Shape,EDBU : TopOpeBRepBuild_EdgeBuilder,LOE : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GFABUMakeFaces(self,FF : OCP.TopoDS.TopoDS_Shape,FABU : TopOpeBRepBuild_FaceBuilder,LOF : OCP.TopTools.TopTools_ListOfShape,MWisOld : OCP.TopTools.TopTools_DataMapOfShapeInteger) -> None: 
        """
        None
        """
    @overload
    def GFillCurveTopologyWES(self,F : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None

        None
        """
    @overload
    def GFillCurveTopologyWES(self,IT : OCP.TopOpeBRepDS.TopOpeBRepDS_CurveIterator,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: ...
    def GFillEdgePVS(self,E : OCP.TopoDS.TopoDS_Shape,LE2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,PVS : TopOpeBRepBuild_PaveSet) -> None: 
        """
        None
        """
    def GFillEdgeWES(self,E : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillEdgesPVS(self,LE1 : OCP.TopTools.TopTools_ListOfShape,LE2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,PVS : TopOpeBRepBuild_PaveSet) -> None: 
        """
        None
        """
    def GFillFaceSFS(self,F1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GFillFaceWES(self,F : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillFacesWES(self,LF1 : OCP.TopTools.TopTools_ListOfShape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillFacesWESK(self,LF1 : OCP.TopTools.TopTools_ListOfShape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet,K : int) -> None: 
        """
        None
        """
    def GFillFacesWESMakeFaces(self,LF1 : OCP.TopTools.TopTools_ListOfShape,LF2 : OCP.TopTools.TopTools_ListOfShape,LSO : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo) -> None: 
        """
        None
        """
    def GFillONPartsWES(self,F : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,LSclass : OCP.TopTools.TopTools_ListOfShape,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    @overload
    def GFillPointTopologyPVS(self,E : OCP.TopoDS.TopoDS_Shape,IT : OCP.TopOpeBRepDS.TopOpeBRepDS_PointIterator,G : TopOpeBRepBuild_GTopo,PVS : TopOpeBRepBuild_PaveSet) -> None: 
        """
        None

        None
        """
    @overload
    def GFillPointTopologyPVS(self,E : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,PVS : TopOpeBRepBuild_PaveSet) -> None: ...
    def GFillShellSFS(self,SH1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GFillSolidSFS(self,SO1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GFillSolidsSFS(self,LSO1 : OCP.TopTools.TopTools_ListOfShape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    @overload
    def GFillSurfaceTopologySFS(self,SO1 : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None

        None
        """
    @overload
    def GFillSurfaceTopologySFS(self,IT : OCP.TopOpeBRepDS.TopOpeBRepDS_SurfaceIterator,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: ...
    def GFillWireWES(self,W : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    @overload
    def GFindSamDom(self,L1 : OCP.TopTools.TopTools_ListOfShape,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None

        None
        """
    @overload
    def GFindSamDom(self,S : OCP.TopoDS.TopoDS_Shape,L1 : OCP.TopTools.TopTools_ListOfShape,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    @overload
    def GFindSamDomSODO(self,S : OCP.TopoDS.TopoDS_Shape,LSO : OCP.TopTools.TopTools_ListOfShape,LDO : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None

        None
        """
    @overload
    def GFindSamDomSODO(self,LSO : OCP.TopTools.TopTools_ListOfShape,LDO : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    def GFindSameRank(self,L1 : OCP.TopTools.TopTools_ListOfShape,R : int,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GIsShapeOf(self,S : OCP.TopoDS.TopoDS_Shape,I12 : int) -> bool: 
        """
        None
        """
    def GKeepShape(self,S : OCP.TopoDS.TopoDS_Shape,Lref : OCP.TopTools.TopTools_ListOfShape,T : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def GKeepShape1(self,S : OCP.TopoDS.TopoDS_Shape,Lref : OCP.TopTools.TopTools_ListOfShape,T : OCP.TopAbs.TopAbs_State,pos : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        return True if S is classified <T> / Lref shapes
        """
    def GKeepShapes(self,S : OCP.TopoDS.TopoDS_Shape,Lref : OCP.TopTools.TopTools_ListOfShape,T : OCP.TopAbs.TopAbs_State,Lin : OCP.TopTools.TopTools_ListOfShape,Lou : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        add to Lou the shapes of Lin classified <T> / Lref shapes. Lou is not cleared. (S is a dummy trace argument)
        """
    def GMapShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def GMergeEdgeWES(self,E : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GMergeEdges(self,LE1 : OCP.TopTools.TopTools_ListOfShape,LE2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo) -> None: 
        """
        None
        """
    def GMergeFaceSFS(self,F : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GMergeFaces(self,LF1 : OCP.TopTools.TopTools_ListOfShape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo) -> None: 
        """
        None
        """
    def GMergeSolids(self,LSO1 : OCP.TopTools.TopTools_ListOfShape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo) -> None: 
        """
        None
        """
    def GPVSMakeEdges(self,EF : OCP.TopoDS.TopoDS_Shape,PVS : TopOpeBRepBuild_PaveSet,LOE : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GParamOnReference(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float) -> bool: 
        """
        None
        """
    def GSFSMakeSolids(self,SOF : OCP.TopoDS.TopoDS_Shape,SFS : TopOpeBRepBuild_ShellFaceSet,LOSO : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GSOBUMakeSolids(self,SOF : OCP.TopoDS.TopoDS_Shape,SOBU : TopOpeBRepBuild_SolidBuilder,LOSO : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GShapeRank(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def GSplitEdge(self,E : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,LSclass : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GSplitEdgeWES(self,E : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GSplitFace(self,F : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,LSclass : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GSplitFaceSFS(self,F1 : OCP.TopoDS.TopoDS_Shape,LSclass : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    @staticmethod
    def GTakeCommonOfDiff_s(G : TopOpeBRepBuild_GTopo) -> bool: 
        """
        None
        """
    @staticmethod
    def GTakeCommonOfSame_s(G : TopOpeBRepBuild_GTopo) -> bool: 
        """
        None
        """
    def GToMerge(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def GToSplit(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def GWESMakeFaces(self,FF : OCP.TopoDS.TopoDS_Shape,WES : TopOpeBRepBuild_WireEdgeSet,LOF : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def GcheckNBOUNDS_s(E : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def GdumpEDBU(self,EB : TopOpeBRepBuild_EdgeBuilder) -> None: 
        """
        None
        """
    def GdumpEDG(self,S : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpEDGVER(self,E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpEXP(self,E : OCP.TopOpeBRepTool.TopOpeBRepTool_ShapeExplorer) -> None: 
        """
        None
        """
    def GdumpFABU(self,FB : TopOpeBRepBuild_FaceBuilder) -> None: 
        """
        None
        """
    def GdumpLS(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def GdumpORIPARPNT_s(o : OCP.TopAbs.TopAbs_Orientation,p : float,Pnt : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def GdumpPNT_s(P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def GdumpSAMDOM(self,L : OCP.TopTools.TopTools_ListOfShape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpSHA(self,S : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpSHAORI(self,S : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpSHAORIGEO(self,S : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpSHASETindex(self) -> int: 
        """
        None
        """
    def GdumpSHASETreset(self) -> None: 
        """
        None
        """
    @overload
    def GdumpSHASTA(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_State,a : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,b : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None

        None

        None
        """
    @overload
    def GdumpSHASTA(self,iS : int,T : OCP.TopAbs.TopAbs_State,SS : TopOpeBRepBuild_ShapeSet,a : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,b : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,c : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def GdumpSHASTA(self,iS : int,T : OCP.TopAbs.TopAbs_State,a : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,b : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    def GdumpSOBU(self,SB : TopOpeBRepBuild_SolidBuilder) -> None: 
        """
        None
        """
    @overload
    def GtraceSPS(self,S : OCP.TopoDS.TopoDS_Shape,IS : int) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def GtraceSPS(self,iS : int) -> bool: ...
    @overload
    def GtraceSPS(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    @overload
    def GtraceSPS(self,iS : int,jS : int) -> bool: ...
    def InitSection(self) -> None: 
        """
        None
        """
    def IsKPart(self) -> int: 
        """
        None
        """
    def IsMerged(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        Returns True if the shape <S> has been merged.
        """
    def IsShapeOf(self,S : OCP.TopoDS.TopoDS_Shape,I12 : int) -> bool: 
        """
        None
        """
    def IsSplit(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        Returns True if the shape <S> has been split.
        """
    def KPClearMaps(self) -> None: 
        """
        None
        """
    @staticmethod
    def KPContains_s(S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def KPSameDomain(self,L1 : OCP.TopTools.TopTools_ListOfShape,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    @overload
    def KPclasSS(self,S1 : OCP.TopoDS.TopoDS_Shape,exceptLS1 : OCP.TopTools.TopTools_ListOfShape,S2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        None

        None

        None
        """
    @overload
    def KPclasSS(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: ...
    @overload
    def KPclasSS(self,S1 : OCP.TopoDS.TopoDS_Shape,exceptS1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: ...
    def KPclassF(self,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def KPclassFF(self,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape,T1 : OCP.TopAbs.TopAbs_State,T2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def KPisdisj(self) -> int: 
        """
        None
        """
    def KPisdisjanalyse(self,ST1 : OCP.TopAbs.TopAbs_State,ST2 : OCP.TopAbs.TopAbs_State) -> Tuple[int, int, int]: 
        """
        None
        """
    def KPisdisjsh(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def KPisfafa(self) -> int: 
        """
        None
        """
    def KPisfafash(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def KPiskole(self) -> int: 
        """
        None
        """
    def KPiskoleFF(self,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape,T1 : OCP.TopAbs.TopAbs_State,T2 : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def KPiskoleanalyse(self,FT1 : OCP.TopAbs.TopAbs_State,FT2 : OCP.TopAbs.TopAbs_State,ST1 : OCP.TopAbs.TopAbs_State,ST2 : OCP.TopAbs.TopAbs_State) -> Tuple[int, int, int]: 
        """
        None
        """
    def KPiskolesh(self,S : OCP.TopoDS.TopoDS_Shape,LS : OCP.TopTools.TopTools_ListOfShape,LF : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def KPiskoletge(self) -> int: 
        """
        None
        """
    def KPiskoletgeanalyse(self,Conf : OCP.TopOpeBRepDS.TopOpeBRepDS_Config,ST1 : OCP.TopAbs.TopAbs_State,ST2 : OCP.TopAbs.TopAbs_State) -> Tuple[int]: 
        """
        None
        """
    def KPiskoletgesh(self,S : OCP.TopoDS.TopoDS_Shape,LS : OCP.TopTools.TopTools_ListOfShape,LF : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def KPissoso(self) -> int: 
        """
        None
        """
    def KPissososh(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    @overload
    def KPlhg(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum,L : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None

        None
        """
    @overload
    def KPlhg(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum) -> int: ...
    @overload
    def KPlhsd(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum) -> int: 
        """
        None

        None
        """
    @overload
    def KPlhsd(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum,L : OCP.TopTools.TopTools_ListOfShape) -> int: ...
    @staticmethod
    @overload
    def KPls_s(S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def KPls_s(S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum,L : OCP.TopTools.TopTools_ListOfShape) -> int: ...
    def KPmakeface(self,F1 : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,T1 : OCP.TopAbs.TopAbs_State,T2 : OCP.TopAbs.TopAbs_State,R1 : bool,R2 : bool) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @staticmethod
    def KPreturn_s(KP : int) -> int: 
        """
        None
        """
    def KeepShape(self,S : OCP.TopoDS.TopoDS_Shape,LS : OCP.TopTools.TopTools_ListOfShape,T : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def MSplit(self,s : OCP.TopAbs.TopAbs_State) -> OCP.TopOpeBRepDS.TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State: 
        """
        None
        """
    def MakeEdges(self,E : OCP.TopoDS.TopoDS_Shape,B : TopOpeBRepBuild_EdgeBuilder,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def MakeFaces(self,F : OCP.TopoDS.TopoDS_Shape,B : TopOpeBRepBuild_FaceBuilder,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def MakeShells(self,B : TopOpeBRepBuild_SolidBuilder,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def MakeSolids(self,B : TopOpeBRepBuild_SolidBuilder,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def MapShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MergeEdges(self,L1 : OCP.TopTools.TopTools_ListOfShape,TB1 : OCP.TopAbs.TopAbs_State,L2 : OCP.TopTools.TopTools_ListOfShape,TB2 : OCP.TopAbs.TopAbs_State,onA : bool=False,onB : bool=False,onAB : bool=False) -> None: 
        """
        Merges the two edges <S1> and <S2> keeping the parts in each edge of states <TB1> and <TB2>. Booleans onA, onB, onAB indicate whether parts of edges found as state ON respectively on first, second, and both shapes must be (or not) built.
        """
    def MergeFaces(self,S1 : OCP.TopTools.TopTools_ListOfShape,TB1 : OCP.TopAbs.TopAbs_State,S2 : OCP.TopTools.TopTools_ListOfShape,TB2 : OCP.TopAbs.TopAbs_State,onA : bool=False,onB : bool=False,onAB : bool=False) -> None: 
        """
        Merges the two faces <S1> and <S2> keeping the parts in each face of states <TB1> and <TB2>.
        """
    @overload
    def MergeKPart(self) -> None: 
        """
        None

        None
        """
    @overload
    def MergeKPart(self,TB1 : OCP.TopAbs.TopAbs_State,TB2 : OCP.TopAbs.TopAbs_State) -> None: ...
    def MergeKPartisdisj(self) -> None: 
        """
        None
        """
    def MergeKPartisfafa(self) -> None: 
        """
        None
        """
    def MergeKPartiskole(self) -> None: 
        """
        None
        """
    def MergeKPartiskoletge(self) -> None: 
        """
        None
        """
    def MergeKPartissoso(self) -> None: 
        """
        None
        """
    def MergeShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,TB1 : OCP.TopAbs.TopAbs_State,S2 : OCP.TopoDS.TopoDS_Shape,TB2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Merges the two shapes <S1> and <S2> keeping the parts of states <TB1>,<TB2> in <S1>,<S2>.
        """
    def MergeSolid(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Merges the solid <S> keeping the parts of state <TB>.
        """
    def MergeSolids(self,S1 : OCP.TopoDS.TopoDS_Shape,TB1 : OCP.TopAbs.TopAbs_State,S2 : OCP.TopoDS.TopoDS_Shape,TB2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Merges the two solids <S1> and <S2> keeping the parts in each solid of states <TB1> and <TB2>.
        """
    def Merged(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the merged parts <TB> of shape <S>.
        """
    def NewEdges(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the edges created on curve <I>.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the faces created on surface <I>.
        """
    def NewVertex(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the vertex created on point <I>.
        """
    def Opec12(self) -> bool: 
        """
        None
        """
    def Opec21(self) -> bool: 
        """
        None
        """
    def Opecom(self) -> bool: 
        """
        None
        """
    def Opefus(self) -> bool: 
        """
        None
        """
    @staticmethod
    def Orient_s(O : OCP.TopAbs.TopAbs_Orientation,R : bool) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    @overload
    def Perform(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Stores the data structure <HDS>, Create shapes from the new geometries.

        Stores the data structure <HDS>, Create shapes from the new geometries, Evaluates if an operation performed on shapes S1,S2 is a particular case.
        """
    @overload
    def Perform(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: ...
    @staticmethod
    def PrintCur_s(E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    @staticmethod
    def PrintGeo_s(S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def PrintOri_s(S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def PrintPnt_s(V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None
        """
    @staticmethod
    def PrintSur_s(F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def RegularizeFace(self,FF : OCP.TopoDS.TopoDS_Shape,newFace : OCP.TopoDS.TopoDS_Shape,LOF : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def RegularizeFaces(self,FF : OCP.TopoDS.TopoDS_Shape,lnewFace : OCP.TopTools.TopTools_ListOfShape,LOF : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def RegularizeSolid(self,SS : OCP.TopoDS.TopoDS_Shape,newSolid : OCP.TopoDS.TopoDS_Shape,LOS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def RegularizeSolids(self,SS : OCP.TopoDS.TopoDS_Shape,lnewSolid : OCP.TopTools.TopTools_ListOfShape,LOS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def Reverse_s(T1 : OCP.TopAbs.TopAbs_State,T2 : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    @overload
    def Section(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        return all section edges.

        None
        """
    @overload
    def Section(self) -> OCP.TopTools.TopTools_ListOfShape: ...
    def SectionCurves(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        return the section edges built on new curves.
        """
    def SectionEdges(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        return the parts of edges found ON the boundary of the two arguments S1,S2 of Perform()
        """
    def ShapePosition(self,S : OCP.TopoDS.TopoDS_Shape,LS : OCP.TopTools.TopTools_ListOfShape) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def ShapeRank(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def SplitEvisoONperiodicF(self) -> None: 
        """
        None
        """
    def SplitSectionEdge(self,E : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        create parts ON solid of section edges
        """
    def SplitSectionEdges(self) -> None: 
        """
        create parts ON solid of section edges
        """
    def Splits(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the split parts <TB> of shape <S>.
        """
    @staticmethod
    def StringState_s(S : OCP.TopAbs.TopAbs_State) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    @staticmethod
    def TopType_s(S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        None
        """
    def __init__(self,BT : OCP.TopOpeBRepDS.TopOpeBRepDS_BuildTool) -> None: ...
    pass
class TopOpeBRepBuild_Builder1(TopOpeBRepBuild_Builder):
    """
    extension of the class TopOpeBRepBuild_Builder dedicated to avoid bugs in "Rebuilding Result" algorithm for the case of SOLID/SOLID Boolean Operations
    """
    def AddONPatchesSFS(self,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def BuildEdges(self,DS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        update the DS by creating new geometries. create shapes from the new geometries.
        """
    def BuildTool(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_BuildTool: 
        """
        None
        """
    def BuildVertices(self,DS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        update the DS by creating new geometries. create vertices on DS points.
        """
    def ChangeBuildTool(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_BuildTool: 
        """
        None
        """
    def ChangeClassify(self,B : bool) -> None: 
        """
        None
        """
    def ChangeMSplit(self,s : OCP.TopAbs.TopAbs_State) -> OCP.TopOpeBRepDS.TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State: 
        """
        None
        """
    def ChangeSplit(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a ref.on the list of shapes connected to <S> as <TB> split parts of <S>. Mark <S> as split in <TB> parts.
        """
    def Classify(self) -> bool: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Removes all splits and merges already performed. Does NOT clear the handled DS (except ShapeWithStatesMaps).
        """
    def ClearMaps(self) -> None: 
        """
        None
        """
    @staticmethod
    def Contains_s(S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def CorrectResult2d(self,aResult : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def DataStructure(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure: 
        """
        returns the DS handled by this builder
        """
    def End(self) -> None: 
        """
        None
        """
    def FillOnPatches(self,anEdgesON : OCP.TopTools.TopTools_ListOfShape,aBaseFace : OCP.TopoDS.TopoDS_Shape,avoidMap : OCP.TopTools.TopTools_IndexedMapOfOrientedShape) -> None: 
        """
        None
        """
    def FillSecEdgeAncestorMap(self,aShapeRank : int,aMapON : OCP.TopTools.TopTools_MapOfShape,anAncMap : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        Fills anAncMap with pairs (edge,ancestor edge) for each split from the map aMapON for the shape object identified by ShapeRank
        """
    def FindFacesTouchingEdge(self,aFace : OCP.TopoDS.TopoDS_Shape,anEdge : OCP.TopoDS.TopoDS_Shape,aShRank : int,aFaces : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def FindIsKPart(self) -> int: 
        """
        None
        """
    def FindSameDomain(self,L1 : OCP.TopTools.TopTools_ListOfShape,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def FindSameDomainSameOrientation(self,LSO : OCP.TopTools.TopTools_ListOfShape,LDO : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def FindSameRank(self,L1 : OCP.TopTools.TopTools_ListOfShape,R : int,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GClearMaps(self) -> None: 
        """
        None
        """
    @staticmethod
    def GContains_s(S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    @staticmethod
    @overload
    def GCopyList_s(Lin : OCP.TopTools.TopTools_ListOfShape,i1 : int,i2 : int,Lou : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def GCopyList_s(Lin : OCP.TopTools.TopTools_ListOfShape,Lou : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    def GEDBUMakeEdges(self,EF : OCP.TopoDS.TopoDS_Shape,EDBU : TopOpeBRepBuild_EdgeBuilder,LOE : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GFABUMakeFaces(self,FF : OCP.TopoDS.TopoDS_Shape,FABU : TopOpeBRepBuild_FaceBuilder,LOF : OCP.TopTools.TopTools_ListOfShape,MWisOld : OCP.TopTools.TopTools_DataMapOfShapeInteger) -> None: 
        """
        None
        """
    @overload
    def GFillCurveTopologyWES(self,F : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None

        None
        """
    @overload
    def GFillCurveTopologyWES(self,IT : OCP.TopOpeBRepDS.TopOpeBRepDS_CurveIterator,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: ...
    def GFillEdgeNotSameDomWES(self,E1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillEdgePVS(self,E : OCP.TopoDS.TopoDS_Shape,LE2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,PVS : TopOpeBRepBuild_PaveSet) -> None: 
        """
        None
        """
    def GFillEdgeSameDomWES(self,E1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillEdgeWES(self,E : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillEdgesPVS(self,LE1 : OCP.TopTools.TopTools_ListOfShape,LE2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,PVS : TopOpeBRepBuild_PaveSet) -> None: 
        """
        None
        """
    def GFillFaceNotSameDomSFS(self,F1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GFillFaceNotSameDomWES(self,F1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillFaceSFS(self,F1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GFillFaceSameDomSFS(self,F1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GFillFaceSameDomWES(self,F1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillFaceWES(self,F : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillFacesWES(self,LF1 : OCP.TopTools.TopTools_ListOfShape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillFacesWESK(self,LF1 : OCP.TopTools.TopTools_ListOfShape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet,K : int) -> None: 
        """
        None
        """
    def GFillFacesWESMakeFaces(self,LF1 : OCP.TopTools.TopTools_ListOfShape,LF2 : OCP.TopTools.TopTools_ListOfShape,LSO : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo) -> None: 
        """
        None
        """
    def GFillONPartsWES(self,F : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,LSclass : OCP.TopTools.TopTools_ListOfShape,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    @overload
    def GFillPointTopologyPVS(self,E : OCP.TopoDS.TopoDS_Shape,IT : OCP.TopOpeBRepDS.TopOpeBRepDS_PointIterator,G : TopOpeBRepBuild_GTopo,PVS : TopOpeBRepBuild_PaveSet) -> None: 
        """
        None

        None
        """
    @overload
    def GFillPointTopologyPVS(self,E : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,PVS : TopOpeBRepBuild_PaveSet) -> None: ...
    def GFillShellSFS(self,SH1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GFillSolidSFS(self,SO1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GFillSolidsSFS(self,LSO1 : OCP.TopTools.TopTools_ListOfShape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    @overload
    def GFillSurfaceTopologySFS(self,SO1 : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None

        None
        """
    @overload
    def GFillSurfaceTopologySFS(self,IT : OCP.TopOpeBRepDS.TopOpeBRepDS_SurfaceIterator,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: ...
    def GFillWireNotSameDomWES(self,W1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillWireSameDomWES(self,W1 : OCP.TopoDS.TopoDS_Shape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GFillWireWES(self,W : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    @overload
    def GFindSamDom(self,L1 : OCP.TopTools.TopTools_ListOfShape,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None

        None
        """
    @overload
    def GFindSamDom(self,S : OCP.TopoDS.TopoDS_Shape,L1 : OCP.TopTools.TopTools_ListOfShape,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    @overload
    def GFindSamDomSODO(self,S : OCP.TopoDS.TopoDS_Shape,LSO : OCP.TopTools.TopTools_ListOfShape,LDO : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None

        None
        """
    @overload
    def GFindSamDomSODO(self,LSO : OCP.TopTools.TopTools_ListOfShape,LDO : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    def GFindSameRank(self,L1 : OCP.TopTools.TopTools_ListOfShape,R : int,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GIsShapeOf(self,S : OCP.TopoDS.TopoDS_Shape,I12 : int) -> bool: 
        """
        None
        """
    def GKeepShape(self,S : OCP.TopoDS.TopoDS_Shape,Lref : OCP.TopTools.TopTools_ListOfShape,T : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def GKeepShape1(self,S : OCP.TopoDS.TopoDS_Shape,Lref : OCP.TopTools.TopTools_ListOfShape,T : OCP.TopAbs.TopAbs_State,pos : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        return True if S is classified <T> / Lref shapes
        """
    def GKeepShapes(self,S : OCP.TopoDS.TopoDS_Shape,Lref : OCP.TopTools.TopTools_ListOfShape,T : OCP.TopAbs.TopAbs_State,Lin : OCP.TopTools.TopTools_ListOfShape,Lou : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        add to Lou the shapes of Lin classified <T> / Lref shapes. Lou is not cleared. (S is a dummy trace argument)
        """
    def GMapShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def GMergeEdgeWES(self,E : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GMergeEdges(self,LE1 : OCP.TopTools.TopTools_ListOfShape,LE2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo) -> None: 
        """
        None
        """
    def GMergeFaceSFS(self,F : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    def GMergeFaces(self,LF1 : OCP.TopTools.TopTools_ListOfShape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo) -> None: 
        """
        None
        """
    def GMergeSolids(self,LSO1 : OCP.TopTools.TopTools_ListOfShape,LSO2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo) -> None: 
        """
        None
        """
    def GPVSMakeEdges(self,EF : OCP.TopoDS.TopoDS_Shape,PVS : TopOpeBRepBuild_PaveSet,LOE : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GParamOnReference(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float) -> bool: 
        """
        None
        """
    def GSFSMakeSolids(self,SOF : OCP.TopoDS.TopoDS_Shape,SFS : TopOpeBRepBuild_ShellFaceSet,LOSO : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GSOBUMakeSolids(self,SOF : OCP.TopoDS.TopoDS_Shape,SOBU : TopOpeBRepBuild_SolidBuilder,LOSO : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GShapeRank(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def GSplitEdge(self,E : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,LSclass : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GSplitEdgeWES(self,E : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def GSplitFace(self,F : OCP.TopoDS.TopoDS_Shape,G : TopOpeBRepBuild_GTopo,LSclass : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def GSplitFaceSFS(self,F1 : OCP.TopoDS.TopoDS_Shape,LSclass : OCP.TopTools.TopTools_ListOfShape,G : TopOpeBRepBuild_GTopo,SFS : TopOpeBRepBuild_ShellFaceSet) -> None: 
        """
        None
        """
    @staticmethod
    def GTakeCommonOfDiff_s(G : TopOpeBRepBuild_GTopo) -> bool: 
        """
        None
        """
    @staticmethod
    def GTakeCommonOfSame_s(G : TopOpeBRepBuild_GTopo) -> bool: 
        """
        None
        """
    def GToMerge(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def GToSplit(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def GWESMakeFaces(self,FF : OCP.TopoDS.TopoDS_Shape,WES : TopOpeBRepBuild_WireEdgeSet,LOF : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def GcheckNBOUNDS_s(E : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def GdumpEDBU(self,EB : TopOpeBRepBuild_EdgeBuilder) -> None: 
        """
        None
        """
    def GdumpEDG(self,S : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpEDGVER(self,E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpEXP(self,E : OCP.TopOpeBRepTool.TopOpeBRepTool_ShapeExplorer) -> None: 
        """
        None
        """
    def GdumpFABU(self,FB : TopOpeBRepBuild_FaceBuilder) -> None: 
        """
        None
        """
    def GdumpLS(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def GdumpORIPARPNT_s(o : OCP.TopAbs.TopAbs_Orientation,p : float,Pnt : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def GdumpPNT_s(P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def GdumpSAMDOM(self,L : OCP.TopTools.TopTools_ListOfShape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpSHA(self,S : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpSHAORI(self,S : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpSHAORIGEO(self,S : OCP.TopoDS.TopoDS_Shape,str : capsule=None) -> None: 
        """
        None
        """
    def GdumpSHASETindex(self) -> int: 
        """
        None
        """
    def GdumpSHASETreset(self) -> None: 
        """
        None
        """
    @overload
    def GdumpSHASTA(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_State,a : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,b : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None

        None

        None
        """
    @overload
    def GdumpSHASTA(self,iS : int,T : OCP.TopAbs.TopAbs_State,SS : TopOpeBRepBuild_ShapeSet,a : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,b : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,c : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def GdumpSHASTA(self,iS : int,T : OCP.TopAbs.TopAbs_State,a : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,b : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    def GdumpSOBU(self,SB : TopOpeBRepBuild_SolidBuilder) -> None: 
        """
        None
        """
    @overload
    def GtraceSPS(self,S : OCP.TopoDS.TopoDS_Shape,IS : int) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def GtraceSPS(self,iS : int) -> bool: ...
    @overload
    def GtraceSPS(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    @overload
    def GtraceSPS(self,iS : int,jS : int) -> bool: ...
    def InitSection(self) -> None: 
        """
        None
        """
    def IsKPart(self) -> int: 
        """
        None
        """
    def IsMerged(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        Returns True if the shape <S> has been merged.
        """
    def IsShapeOf(self,S : OCP.TopoDS.TopoDS_Shape,I12 : int) -> bool: 
        """
        None
        """
    def IsSplit(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        Returns True if the shape <S> has been split.
        """
    def KPClearMaps(self) -> None: 
        """
        None
        """
    @staticmethod
    def KPContains_s(S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def KPSameDomain(self,L1 : OCP.TopTools.TopTools_ListOfShape,L2 : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    @overload
    def KPclasSS(self,S1 : OCP.TopoDS.TopoDS_Shape,exceptLS1 : OCP.TopTools.TopTools_ListOfShape,S2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        None

        None

        None
        """
    @overload
    def KPclasSS(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: ...
    @overload
    def KPclasSS(self,S1 : OCP.TopoDS.TopoDS_Shape,exceptS1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: ...
    def KPclassF(self,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def KPclassFF(self,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape,T1 : OCP.TopAbs.TopAbs_State,T2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def KPisdisj(self) -> int: 
        """
        None
        """
    def KPisdisjanalyse(self,ST1 : OCP.TopAbs.TopAbs_State,ST2 : OCP.TopAbs.TopAbs_State) -> Tuple[int, int, int]: 
        """
        None
        """
    def KPisdisjsh(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def KPisfafa(self) -> int: 
        """
        None
        """
    def KPisfafash(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def KPiskole(self) -> int: 
        """
        None
        """
    def KPiskoleFF(self,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape,T1 : OCP.TopAbs.TopAbs_State,T2 : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def KPiskoleanalyse(self,FT1 : OCP.TopAbs.TopAbs_State,FT2 : OCP.TopAbs.TopAbs_State,ST1 : OCP.TopAbs.TopAbs_State,ST2 : OCP.TopAbs.TopAbs_State) -> Tuple[int, int, int]: 
        """
        None
        """
    def KPiskolesh(self,S : OCP.TopoDS.TopoDS_Shape,LS : OCP.TopTools.TopTools_ListOfShape,LF : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def KPiskoletge(self) -> int: 
        """
        None
        """
    def KPiskoletgeanalyse(self,Conf : OCP.TopOpeBRepDS.TopOpeBRepDS_Config,ST1 : OCP.TopAbs.TopAbs_State,ST2 : OCP.TopAbs.TopAbs_State) -> Tuple[int]: 
        """
        None
        """
    def KPiskoletgesh(self,S : OCP.TopoDS.TopoDS_Shape,LS : OCP.TopTools.TopTools_ListOfShape,LF : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        None
        """
    def KPissoso(self) -> int: 
        """
        None
        """
    def KPissososh(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    @overload
    def KPlhg(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum,L : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None

        None
        """
    @overload
    def KPlhg(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum) -> int: ...
    @overload
    def KPlhsd(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum) -> int: 
        """
        None

        None
        """
    @overload
    def KPlhsd(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum,L : OCP.TopTools.TopTools_ListOfShape) -> int: ...
    @staticmethod
    @overload
    def KPls_s(S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def KPls_s(S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum,L : OCP.TopTools.TopTools_ListOfShape) -> int: ...
    def KPmakeface(self,F1 : OCP.TopoDS.TopoDS_Shape,LF2 : OCP.TopTools.TopTools_ListOfShape,T1 : OCP.TopAbs.TopAbs_State,T2 : OCP.TopAbs.TopAbs_State,R1 : bool,R2 : bool) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @staticmethod
    def KPreturn_s(KP : int) -> int: 
        """
        None
        """
    def KeepShape(self,S : OCP.TopoDS.TopoDS_Shape,LS : OCP.TopTools.TopTools_ListOfShape,T : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    def MSplit(self,s : OCP.TopAbs.TopAbs_State) -> OCP.TopOpeBRepDS.TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State: 
        """
        None
        """
    def MakeEdges(self,E : OCP.TopoDS.TopoDS_Shape,B : TopOpeBRepBuild_EdgeBuilder,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def MakeFaces(self,F : OCP.TopoDS.TopoDS_Shape,B : TopOpeBRepBuild_FaceBuilder,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def MakeShells(self,B : TopOpeBRepBuild_SolidBuilder,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def MakeSolids(self,B : TopOpeBRepBuild_SolidBuilder,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def MapShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MergeEdges(self,L1 : OCP.TopTools.TopTools_ListOfShape,TB1 : OCP.TopAbs.TopAbs_State,L2 : OCP.TopTools.TopTools_ListOfShape,TB2 : OCP.TopAbs.TopAbs_State,onA : bool=False,onB : bool=False,onAB : bool=False) -> None: 
        """
        Merges the two edges <S1> and <S2> keeping the parts in each edge of states <TB1> and <TB2>. Booleans onA, onB, onAB indicate whether parts of edges found as state ON respectively on first, second, and both shapes must be (or not) built.
        """
    def MergeFaces(self,S1 : OCP.TopTools.TopTools_ListOfShape,TB1 : OCP.TopAbs.TopAbs_State,S2 : OCP.TopTools.TopTools_ListOfShape,TB2 : OCP.TopAbs.TopAbs_State,onA : bool=False,onB : bool=False,onAB : bool=False) -> None: 
        """
        Merges the two faces <S1> and <S2> keeping the parts in each face of states <TB1> and <TB2>.
        """
    @overload
    def MergeKPart(self) -> None: 
        """
        None

        None
        """
    @overload
    def MergeKPart(self,TB1 : OCP.TopAbs.TopAbs_State,TB2 : OCP.TopAbs.TopAbs_State) -> None: ...
    def MergeKPartisdisj(self) -> None: 
        """
        None
        """
    def MergeKPartisfafa(self) -> None: 
        """
        None
        """
    def MergeKPartiskole(self) -> None: 
        """
        None
        """
    def MergeKPartiskoletge(self) -> None: 
        """
        None
        """
    def MergeKPartissoso(self) -> None: 
        """
        None
        """
    def MergeShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,TB1 : OCP.TopAbs.TopAbs_State,S2 : OCP.TopoDS.TopoDS_Shape,TB2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Merges the two shapes <S1> and <S2> keeping the parts of states <TB1>,<TB2> in <S1>,<S2>.
        """
    def MergeSolid(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Merges the solid <S> keeping the parts of state <TB>.
        """
    def MergeSolids(self,S1 : OCP.TopoDS.TopoDS_Shape,TB1 : OCP.TopAbs.TopAbs_State,S2 : OCP.TopoDS.TopoDS_Shape,TB2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Merges the two solids <S1> and <S2> keeping the parts in each solid of states <TB1> and <TB2>.
        """
    def Merged(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the merged parts <TB> of shape <S>.
        """
    def NewEdges(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the edges created on curve <I>.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the faces created on surface <I>.
        """
    def NewVertex(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the vertex created on point <I>.
        """
    def Opec12(self) -> bool: 
        """
        None
        """
    def Opec21(self) -> bool: 
        """
        None
        """
    def Opecom(self) -> bool: 
        """
        None
        """
    def Opefus(self) -> bool: 
        """
        None
        """
    @staticmethod
    def Orient_s(O : OCP.TopAbs.TopAbs_Orientation,R : bool) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    @overload
    def Perform(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def PerformONParts(self,F : OCP.TopoDS.TopoDS_Shape,SDfaces : OCP.TopTools.TopTools_IndexedMapOfShape,G : TopOpeBRepBuild_GTopo,WES : TopOpeBRepBuild_WireEdgeSet) -> None: 
        """
        None
        """
    def PerformPieceIn2D(self,aPieceToPerform : OCP.TopoDS.TopoDS_Edge,aOriginalEdge : OCP.TopoDS.TopoDS_Edge,edgeFace : OCP.TopoDS.TopoDS_Face,toFace : OCP.TopoDS.TopoDS_Face,G : TopOpeBRepBuild_GTopo) -> Tuple[bool]: 
        """
        None
        """
    def PerformPieceOn2D(self,aPieceObj : OCP.TopoDS.TopoDS_Shape,aFaceObj : OCP.TopoDS.TopoDS_Shape,aEdgeObj : OCP.TopoDS.TopoDS_Shape,aListOfPieces : OCP.TopTools.TopTools_ListOfShape,aListOfFaces : OCP.TopTools.TopTools_ListOfShape,aListOfPiecesOut2d : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None
        """
    @staticmethod
    def PrintCur_s(E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    @staticmethod
    def PrintGeo_s(S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def PrintOri_s(S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @staticmethod
    def PrintPnt_s(V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None
        """
    @staticmethod
    def PrintSur_s(F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def RegularizeFace(self,FF : OCP.TopoDS.TopoDS_Shape,newFace : OCP.TopoDS.TopoDS_Shape,LOF : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def RegularizeFaces(self,FF : OCP.TopoDS.TopoDS_Shape,lnewFace : OCP.TopTools.TopTools_ListOfShape,LOF : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def RegularizeSolid(self,SS : OCP.TopoDS.TopoDS_Shape,newSolid : OCP.TopoDS.TopoDS_Shape,LOS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def RegularizeSolids(self,SS : OCP.TopoDS.TopoDS_Shape,lnewSolid : OCP.TopTools.TopTools_ListOfShape,LOS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    @staticmethod
    def Reverse_s(T1 : OCP.TopAbs.TopAbs_State,T2 : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None
        """
    @overload
    def Section(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        return all section edges.

        None
        """
    @overload
    def Section(self) -> OCP.TopTools.TopTools_ListOfShape: ...
    def SectionCurves(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        return the section edges built on new curves.
        """
    def SectionEdges(self,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        return the parts of edges found ON the boundary of the two arguments S1,S2 of Perform()
        """
    def ShapePosition(self,S : OCP.TopoDS.TopoDS_Shape,LS : OCP.TopTools.TopTools_ListOfShape) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def ShapeRank(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def SplitEvisoONperiodicF(self) -> None: 
        """
        None
        """
    def SplitSectionEdge(self,E : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        create parts ON solid of section edges
        """
    def SplitSectionEdges(self) -> None: 
        """
        create parts ON solid of section edges
        """
    def Splits(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the split parts <TB> of shape <S>.
        """
    @staticmethod
    def StringState_s(S : OCP.TopAbs.TopAbs_State) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    @staticmethod
    def TopType_s(S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        None
        """
    def TwoPiecesON(self,aSeq : OCP.TopTools.TopTools_SequenceOfShape,aListOfPieces : OCP.TopTools.TopTools_ListOfShape,aListOfFaces : OCP.TopTools.TopTools_ListOfShape,aListOfPiecesOut2d : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None
        """
    def __init__(self,BT : OCP.TopOpeBRepDS.TopOpeBRepDS_BuildTool) -> None: ...
    pass
class TopOpeBRepBuild_BuilderON():
    """
    None
    """
    def GFillONCheckI(self,I : OCP.TopOpeBRepDS.TopOpeBRepDS_Interference) -> bool: 
        """
        None
        """
    def GFillONParts2dWES2(self,I : OCP.TopOpeBRepDS.TopOpeBRepDS_Interference,EspON : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def GFillONPartsWES1(self,I : OCP.TopOpeBRepDS.TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def GFillONPartsWES2(self,I : OCP.TopOpeBRepDS.TopOpeBRepDS_Interference,EspON : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_LoopClassifier():
    """
    classify loops in order to build Areas
    """
    def Compare(self,L1 : TopOpeBRepBuild_Loop,L2 : TopOpeBRepBuild_Loop) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the state of loop <L1> compared with loop <L2>.
        """
    pass
class TopOpeBRepBuild_CorrectFace2d():
    """
    None
    """
    @staticmethod
    def CheckList_s(aFace : OCP.TopoDS.TopoDS_Face,aHeadList : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def CorrectedFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def ErrorStatus(self) -> int: 
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    @staticmethod
    def GetP2dFL_s(aFace : OCP.TopoDS.TopoDS_Face,anEdge : OCP.TopoDS.TopoDS_Edge,P2dF : OCP.gp.gp_Pnt2d,P2dL : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def MapOfTrans2dInfo(self) -> OCP.TopTools.TopTools_IndexedDataMapOfShapeShape: 
        """
        None
        """
    def Perform(self) -> None: 
        """
        None
        """
    def SetMapOfTrans2dInfo(self,aMap : OCP.TopTools.TopTools_IndexedDataMapOfShapeShape) -> None: 
        """
        None
        """
    @overload
    def __init__(self,aFace : OCP.TopoDS.TopoDS_Face,anAvoidMap : OCP.TopTools.TopTools_IndexedMapOfOrientedShape,aMap : OCP.TopTools.TopTools_IndexedDataMapOfShapeShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_DataMapOfShapeListOfShapeListOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepBuild_DataMapOfShapeListOfShapeListOfShape) -> TopOpeBRepBuild_DataMapOfShapeListOfShapeListOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepBuild_ListOfShapeListOfShape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepBuild_ListOfShapeListOfShape) -> TopOpeBRepBuild_ListOfShapeListOfShape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepBuild_ListOfShapeListOfShape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepBuild_ListOfShapeListOfShape: 
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
    def Exchange(self,theOther : TopOpeBRepBuild_DataMapOfShapeListOfShapeListOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepBuild_ListOfShapeListOfShape: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepBuild_ListOfShapeListOfShape) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepBuild_ListOfShapeListOfShape: 
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepBuild_DataMapOfShapeListOfShapeListOfShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepBuild_EdgeBuilder(TopOpeBRepBuild_Area1dBuilder, TopOpeBRepBuild_AreaBuilder):
    """
    None
    """
    def ADD_LISTOFLoop_TO_LISTOFLoop(self,LOL1 : TopOpeBRepBuild_ListOfLoop,LOL2 : TopOpeBRepBuild_ListOfLoop,s : capsule=None,s1 : capsule=None,s2 : capsule=None) -> None: 
        """
        None
        """
    def ADD_Loop_TO_LISTOFLoop(self,L : TopOpeBRepBuild_Loop,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    @staticmethod
    def DumpList_s(L : TopOpeBRepBuild_ListOfLoop) -> None: 
        """
        None
        """
    def InitArea(self) -> int: 
        """
        Initialize iteration on areas.
        """
    def InitAreaBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        Sets a Area1dBuilder to find the areas of the shapes described by <LS> using the classifier <LC>.
        """
    def InitEdge(self) -> None: 
        """
        None
        """
    def InitEdgeBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        None
        """
    def InitLoop(self) -> int: 
        """
        Initialize iteration on loops of current Area.
        """
    def InitVertex(self) -> None: 
        """
        None
        """
    def Loop(self) -> TopOpeBRepBuild_Loop: 
        """
        Returns the current Loop in the current area.
        """
    def MoreArea(self) -> bool: 
        """
        None
        """
    def MoreEdge(self) -> bool: 
        """
        None
        """
    def MoreLoop(self) -> bool: 
        """
        None
        """
    def MoreVertex(self) -> bool: 
        """
        None
        """
    def NextArea(self) -> None: 
        """
        None
        """
    def NextEdge(self) -> None: 
        """
        None
        """
    def NextLoop(self) -> None: 
        """
        None
        """
    def NextVertex(self) -> None: 
        """
        None
        """
    def Parameter(self) -> float: 
        """
        None
        """
    def REM_Loop_FROM_LISTOFLoop(self,ITLOL : Any,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,LS : TopOpeBRepBuild_PaveSet,LC : TopOpeBRepBuild_PaveClassifier,ForceClass : bool=False) -> None: ...
    pass
class TopOpeBRepBuild_FaceAreaBuilder(TopOpeBRepBuild_Area2dBuilder, TopOpeBRepBuild_AreaBuilder):
    """
    The FaceAreaBuilder algorithm is used to construct Faces from a LoopSet, where the Loop is the composite topological object of the boundary, here wire or block of edges. The LoopSet gives an iteration on Loops. For each Loop it indicates if it is on the boundary (wire) or if it results from an interference (block of edges). The result of the FaceAreaBuilder is an iteration on areas. An area is described by a set of Loops.
    """
    def ADD_LISTOFLoop_TO_LISTOFLoop(self,LOL1 : TopOpeBRepBuild_ListOfLoop,LOL2 : TopOpeBRepBuild_ListOfLoop,s : capsule=None,s1 : capsule=None,s2 : capsule=None) -> None: 
        """
        None
        """
    def ADD_Loop_TO_LISTOFLoop(self,L : TopOpeBRepBuild_Loop,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    def InitArea(self) -> int: 
        """
        Initialize iteration on areas.
        """
    def InitAreaBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        Sets a Area1dBuilder to find the areas of the shapes described by <LS> using the classifier <LC>.
        """
    def InitFaceAreaBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        None
        """
    def InitLoop(self) -> int: 
        """
        Initialize iteration on loops of current Area.
        """
    def Loop(self) -> TopOpeBRepBuild_Loop: 
        """
        Returns the current Loop in the current area.
        """
    def MoreArea(self) -> bool: 
        """
        None
        """
    def MoreLoop(self) -> bool: 
        """
        None
        """
    def NextArea(self) -> None: 
        """
        None
        """
    def NextLoop(self) -> None: 
        """
        None
        """
    def REM_Loop_FROM_LISTOFLoop(self,ITLOL : Any,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: ...
    pass
class TopOpeBRepBuild_FaceBuilder():
    """
    None
    """
    def AddEdgeWire(self,E : OCP.TopoDS.TopoDS_Shape,W : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def CorrectGclosedWire(self,mapVVref : OCP.TopTools.TopTools_IndexedDataMapOfShapeShape,mapVon1Edge : OCP.TopTools.TopTools_IndexedDataMapOfShapeShape) -> None: 
        """
        Using the given maps, change the topology of the 3d-closed wires, in order to get closed wires.
        """
    def DetectPseudoInternalEdge(self,mapE : OCP.TopTools.TopTools_IndexedMapOfShape) -> None: 
        """
        Removes edges appearing twice (FORWARD,REVERSED) with a bounding vertex not connected to any other edge. mapE contains edges found. modifies myBlockBuilder.
        """
    def DetectUnclosedWire(self,mapVVsameG : OCP.TopTools.TopTools_IndexedDataMapOfShapeShape,mapVon1Edge : OCP.TopTools.TopTools_IndexedDataMapOfShapeShape) -> None: 
        """
        Removes are non 3d-closed wires. Fills up maps <mapVVsameG> and <mapVon1Edge>, in order to correct 3d-closed but unclosed (topologic connexity) wires. modifies myBlockBuilder
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns current new edge of current new wire.
        """
    def EdgeConnexity(self,E : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        return myFace
        """
    def FindNextValidElement(self) -> None: 
        """
        Iterates on myBlockIterator until finding a valid element
        """
    def InitEdge(self) -> int: 
        """
        None
        """
    def InitFace(self) -> int: 
        """
        None
        """
    def InitFaceBuilder(self,ES : TopOpeBRepBuild_WireEdgeSet,F : OCP.TopoDS.TopoDS_Shape,ForceClass : bool) -> None: 
        """
        None
        """
    def InitWire(self) -> int: 
        """
        None
        """
    def IsOldWire(self) -> bool: 
        """
        None
        """
    def MoreEdge(self) -> bool: 
        """
        None
        """
    def MoreFace(self) -> bool: 
        """
        None
        """
    def MoreWire(self) -> bool: 
        """
        None
        """
    def NextEdge(self) -> None: 
        """
        None
        """
    def NextFace(self) -> None: 
        """
        None
        """
    def NextWire(self) -> None: 
        """
        None
        """
    def OldWire(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns current wire This wire may be : * an old wire OldWire(), which has not been reconstructed; * a new wire made of edges described by ...NewEdge() methods.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,ES : TopOpeBRepBuild_WireEdgeSet,F : OCP.TopoDS.TopoDS_Shape,ForceClass : bool=False) -> None: ...
    pass
class TopOpeBRepBuild_FuseFace():
    """
    None
    """
    def ClearEdge(self) -> None: 
        """
        None
        """
    def ClearVertex(self) -> None: 
        """
        None
        """
    def Init(self,LIF : OCP.TopTools.TopTools_ListOfShape,LRF : OCP.TopTools.TopTools_ListOfShape,CXM : int) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def IsModified(self) -> bool: 
        """
        None

        None
        """
    def LExternEdge(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def LExternVertex(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def LFuseFace(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def LInternEdge(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def LInternVertex(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def LModifEdge(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def LModifVertex(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def PerformEdge(self) -> None: 
        """
        None
        """
    def PerformFace(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,LIF : OCP.TopTools.TopTools_ListOfShape,LRF : OCP.TopTools.TopTools_ListOfShape,CXM : int) -> None: ...
    pass
class TopOpeBRepBuild_GIter():
    """
    None
    """
    def Current(self,s1 : OCP.TopAbs.TopAbs_State,s2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def Dump(self,OS : io.BytesIO) -> None: 
        """
        None
        """
    @overload
    def Init(self) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,G : TopOpeBRepBuild_GTopo) -> None: ...
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self,G : TopOpeBRepBuild_GTopo) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_GTool():
    """
    None
    """
    @staticmethod
    def Dump_s(OS : io.BytesIO) -> None: 
        """
        None
        """
    @staticmethod
    def GComDiff_s(s1 : OCP.TopAbs.TopAbs_ShapeEnum,s2 : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    @staticmethod
    def GComSame_s(s1 : OCP.TopAbs.TopAbs_ShapeEnum,s2 : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    @staticmethod
    def GComUnsh_s(s1 : OCP.TopAbs.TopAbs_ShapeEnum,s2 : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    @staticmethod
    def GCutDiff_s(s1 : OCP.TopAbs.TopAbs_ShapeEnum,s2 : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    @staticmethod
    def GCutSame_s(s1 : OCP.TopAbs.TopAbs_ShapeEnum,s2 : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    @staticmethod
    def GCutUnsh_s(s1 : OCP.TopAbs.TopAbs_ShapeEnum,s2 : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    @staticmethod
    def GFusDiff_s(s1 : OCP.TopAbs.TopAbs_ShapeEnum,s2 : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    @staticmethod
    def GFusSame_s(s1 : OCP.TopAbs.TopAbs_ShapeEnum,s2 : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    @staticmethod
    def GFusUnsh_s(s1 : OCP.TopAbs.TopAbs_ShapeEnum,s2 : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_GTopo():
    """
    None
    """
    def ChangeConfig(self,C1 : OCP.TopOpeBRepDS.TopOpeBRepDS_Config,C2 : OCP.TopOpeBRepDS.TopOpeBRepDS_Config) -> None: 
        """
        None
        """
    def ChangeType(self,t1 : OCP.TopAbs.TopAbs_ShapeEnum,t2 : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        None
        """
    @overload
    def ChangeValue(self,s1 : OCP.TopAbs.TopAbs_State,s2 : OCP.TopAbs.TopAbs_State,b : bool) -> None: 
        """
        None

        None
        """
    @overload
    def ChangeValue(self,i1 : int,i2 : int,b : bool) -> None: ...
    def Config1(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Config: 
        """
        None
        """
    def Config2(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Config: 
        """
        None
        """
    def CopyPermuted(self) -> TopOpeBRepBuild_GTopo: 
        """
        None
        """
    def Dump(self,OS : io.BytesIO,s : capsule=None) -> None: 
        """
        None
        """
    @staticmethod
    def DumpSSB_s(OS : io.BytesIO,s1 : OCP.TopAbs.TopAbs_State,s2 : OCP.TopAbs.TopAbs_State,b : bool) -> None: 
        """
        None
        """
    def DumpType(self,OS : io.BytesIO) -> None: 
        """
        None
        """
    def DumpVal(self,OS : io.BytesIO,s1 : OCP.TopAbs.TopAbs_State,s2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def GIndex(self,S : OCP.TopAbs.TopAbs_State) -> int: 
        """
        None
        """
    def GState(self,I : int) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def Index(self,II : int) -> Tuple[int, int]: 
        """
        None
        """
    def IsToReverse1(self) -> bool: 
        """
        None
        """
    def IsToReverse2(self) -> bool: 
        """
        None
        """
    def Reset(self) -> None: 
        """
        None
        """
    def Reverse(self) -> bool: 
        """
        None
        """
    def Set(self,II : bool,IN : bool,IO : bool,NI : bool,NN : bool,NO : bool,OI : bool,ON : bool,OO : bool) -> None: 
        """
        None
        """
    def SetReverse(self,rev : bool) -> None: 
        """
        None
        """
    def StatesON(self,s1 : OCP.TopAbs.TopAbs_State,s2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def Type(self,t1 : OCP.TopAbs.TopAbs_ShapeEnum,t2 : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        None
        """
    @overload
    def Value(self,s1 : OCP.TopAbs.TopAbs_State,s2 : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        None

        None

        None
        """
    @overload
    def Value(self,I1 : int,I2 : int) -> bool: ...
    @overload
    def Value(self,II : int) -> bool: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,II : bool,IN : bool,IO : bool,NI : bool,NN : bool,NO : bool,OI : bool,ON : bool,OO : bool,t1 : OCP.TopAbs.TopAbs_ShapeEnum,t2 : OCP.TopAbs.TopAbs_ShapeEnum,C1 : OCP.TopOpeBRepDS.TopOpeBRepDS_Config,C2 : OCP.TopOpeBRepDS.TopOpeBRepDS_Config) -> None: ...
    pass
class TopOpeBRepBuild_HBuilder(OCP.Standard.Standard_Transient):
    """
    The HBuilder algorithm constructs topological objects from an existing topology and new geometries attached to the topology. It is used to construct the result of a topological operation; the existing topologies are the parts involved in the topological operation and the new geometries are the intersection lines and points.The HBuilder algorithm constructs topological objects from an existing topology and new geometries attached to the topology. It is used to construct the result of a topological operation; the existing topologies are the parts involved in the topological operation and the new geometries are the intersection lines and points.The HBuilder algorithm constructs topological objects from an existing topology and new geometries attached to the topology. It is used to construct the result of a topological operation; the existing topologies are the parts involved in the topological operation and the new geometries are the intersection lines and points.
    """
    def BuildTool(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_BuildTool: 
        """
        None
        """
    def ChangeBuildTool(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_BuildTool: 
        """
        None
        """
    def ChangeBuilder(self) -> TopOpeBRepBuild_Builder: 
        """
        None
        """
    def ChangeNewEdges(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the edges created on curve <I>.
        """
    def Clear(self) -> None: 
        """
        Removes all split and merge already performed. Does NOT clear the handled DS.
        """
    def CurrentSection(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def DataStructure(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure: 
        """
        returns the DS handled by this builder
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
    def EdgeCurveAncestors(self,E : OCP.TopoDS.TopoDS_Shape,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape,IC : int) -> bool: 
        """
        search for the couple of face F1,F2 (from arguments of supra Perform(S1,S2,HDS)) method which intersection gives section edge E built on an intersection curve. returns True if F1,F2 have been valued. returns False if E is not a section edge built on intersection curve IC.
        """
    def EdgeSectionAncestors(self,E : OCP.TopoDS.TopoDS_Shape,LF1 : OCP.TopTools.TopTools_ListOfShape,LF2 : OCP.TopTools.TopTools_ListOfShape,LE1 : OCP.TopTools.TopTools_ListOfShape,LE2 : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        search for the couple of face F1,F2 (from arguments of supra Perform(S1,S2,HDS)) method which intersection gives section edge E built on at least one edge . returns True if F1,F2 have been valued. returns False if E is not a section edge built on at least one edge of S1 and/or S2. LE1,LE2 are edges of S1,S2 which common part is edge E. LE1 or LE2 may be empty() but not both.
        """
    def GetDSCurveFromSectEdge(self,SectEdge : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def GetDSEdgeFromSectEdge(self,E : OCP.TopoDS.TopoDS_Shape,rank : int) -> int: 
        """
        None
        """
    def GetDSFaceFromDSCurve(self,indexCur : int,rank : int) -> int: 
        """
        None
        """
    def GetDSFaceFromDSEdge(self,indexEdg : int,rank : int) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        None
        """
    def GetDSPointFromNewVertex(self,NewVert : OCP.TopoDS.TopoDS_Shape) -> int: 
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
    def InitExtendedSectionDS(self,k : int=3) -> None: 
        """
        None
        """
    def InitSection(self,k : int=3) -> None: 
        """
        None
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsKPart(self) -> int: 
        """
        Returns 0 is standard operation, != 0 if particular case
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsMerged(self,S : OCP.TopoDS.TopoDS_Shape,ToBuild : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        Returns True if the shape <S> has been merged.
        """
    def IsSplit(self,S : OCP.TopoDS.TopoDS_Shape,ToBuild : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        Returns True if the shape <S> has been split.
        """
    def MergeKPart(self,TB1 : OCP.TopAbs.TopAbs_State,TB2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def MergeShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,TB1 : OCP.TopAbs.TopAbs_State,S2 : OCP.TopoDS.TopoDS_Shape,TB2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Merges the two shapes <S1> and <S2> keeping the parts of states <TB1>,<TB2> in <S1>,<S2>.
        """
    def MergeSolid(self,S : OCP.TopoDS.TopoDS_Shape,TB : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Merges the solid <S> keeping the parts of state <TB>.
        """
    def MergeSolids(self,S1 : OCP.TopoDS.TopoDS_Shape,TB1 : OCP.TopAbs.TopAbs_State,S2 : OCP.TopoDS.TopoDS_Shape,TB2 : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Merges the two solids <S1> and <S2> keeping the parts in each solid of states <TB1> and <TB2>.
        """
    def Merged(self,S : OCP.TopoDS.TopoDS_Shape,ToBuild : OCP.TopAbs.TopAbs_State) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the merged parts <ToBuild> of shape <S>.
        """
    def MoreSection(self) -> bool: 
        """
        None
        """
    def NewEdges(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the edges created on curve <I>.
        """
    def NewFaces(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the faces created on surface <I>.
        """
    def NewVertex(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the vertex created on point <I>.
        """
    def NextSection(self) -> None: 
        """
        None
        """
    @overload
    def Perform(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure) -> None: 
        """
        Stores the data structure <HDS>, Create shapes from the new geometries described in <HDS>.

        Same as previous + evaluates if an operation performed on shapes S1,S2 is a particular case.
        """
    @overload
    def Perform(self,HDS : OCP.TopOpeBRepDS.TopOpeBRepDS_HDataStructure,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def Section(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Splits(self,S : OCP.TopoDS.TopoDS_Shape,ToBuild : OCP.TopAbs.TopAbs_State) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the split parts <ToBuild> of shape <S>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,BT : OCP.TopOpeBRepDS.TopOpeBRepDS_BuildTool) -> None: ...
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
class TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepBuild_VertexInfo) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo) -> TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> TopOpeBRepBuild_VertexInfo: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepBuild_VertexInfo: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepBuild_VertexInfo: 
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
    def Exchange(self,theOther : TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> TopOpeBRepBuild_VertexInfo: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepBuild_VertexInfo) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepBuild_VertexInfo: ...
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
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepBuild_VertexInfo: 
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
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepBuild_VertexInfo) -> None: 
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
    def __init__(self,theOther : TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepBuild_ListOfListOfLoop(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TopOpeBRepBuild_ListOfLoop) -> TopOpeBRepBuild_ListOfLoop: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TopOpeBRepBuild_ListOfListOfLoop) -> None: ...
    @overload
    def Append(self,theItem : TopOpeBRepBuild_ListOfLoop,theIter : Any) -> None: ...
    def Assign(self,theOther : TopOpeBRepBuild_ListOfListOfLoop) -> TopOpeBRepBuild_ListOfListOfLoop: 
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
    def First(self) -> TopOpeBRepBuild_ListOfLoop: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TopOpeBRepBuild_ListOfListOfLoop,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : TopOpeBRepBuild_ListOfLoop,theIter : Any) -> TopOpeBRepBuild_ListOfLoop: ...
    @overload
    def InsertBefore(self,theItem : TopOpeBRepBuild_ListOfLoop,theIter : Any) -> TopOpeBRepBuild_ListOfLoop: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TopOpeBRepBuild_ListOfListOfLoop,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TopOpeBRepBuild_ListOfLoop: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : TopOpeBRepBuild_ListOfLoop) -> TopOpeBRepBuild_ListOfLoop: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TopOpeBRepBuild_ListOfListOfLoop) -> None: ...
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
    def __init__(self,theOther : TopOpeBRepBuild_ListOfListOfLoop) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepBuild_ListOfLoop(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : TopOpeBRepBuild_ListOfLoop) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : TopOpeBRepBuild_Loop,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : TopOpeBRepBuild_Loop) -> TopOpeBRepBuild_Loop: ...
    def Assign(self,theOther : TopOpeBRepBuild_ListOfLoop) -> TopOpeBRepBuild_ListOfLoop: 
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
    def First(self) -> TopOpeBRepBuild_Loop: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : TopOpeBRepBuild_Loop,theIter : Any) -> TopOpeBRepBuild_Loop: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TopOpeBRepBuild_ListOfLoop,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : TopOpeBRepBuild_ListOfLoop,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : TopOpeBRepBuild_Loop,theIter : Any) -> TopOpeBRepBuild_Loop: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TopOpeBRepBuild_Loop: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TopOpeBRepBuild_ListOfLoop) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : TopOpeBRepBuild_Loop) -> TopOpeBRepBuild_Loop: ...
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
    def __init__(self,theOther : TopOpeBRepBuild_ListOfLoop) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepBuild_ListOfPave(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : TopOpeBRepBuild_ListOfPave) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : TopOpeBRepBuild_Pave,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : TopOpeBRepBuild_Pave) -> TopOpeBRepBuild_Pave: ...
    def Assign(self,theOther : TopOpeBRepBuild_ListOfPave) -> TopOpeBRepBuild_ListOfPave: 
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
    def First(self) -> TopOpeBRepBuild_Pave: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : TopOpeBRepBuild_ListOfPave,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : TopOpeBRepBuild_Pave,theIter : Any) -> TopOpeBRepBuild_Pave: ...
    @overload
    def InsertBefore(self,theOther : TopOpeBRepBuild_ListOfPave,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : TopOpeBRepBuild_Pave,theIter : Any) -> TopOpeBRepBuild_Pave: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TopOpeBRepBuild_Pave: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TopOpeBRepBuild_ListOfPave) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : TopOpeBRepBuild_Pave) -> TopOpeBRepBuild_Pave: ...
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
    def __init__(self,theOther : TopOpeBRepBuild_ListOfPave) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepBuild_ListOfShapeListOfShape(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TopOpeBRepBuild_ShapeListOfShape,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TopOpeBRepBuild_ListOfShapeListOfShape) -> None: ...
    @overload
    def Append(self,theItem : TopOpeBRepBuild_ShapeListOfShape) -> TopOpeBRepBuild_ShapeListOfShape: ...
    def Assign(self,theOther : TopOpeBRepBuild_ListOfShapeListOfShape) -> TopOpeBRepBuild_ListOfShapeListOfShape: 
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
    def First(self) -> TopOpeBRepBuild_ShapeListOfShape: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : TopOpeBRepBuild_ShapeListOfShape,theIter : Any) -> TopOpeBRepBuild_ShapeListOfShape: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TopOpeBRepBuild_ListOfShapeListOfShape,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : TopOpeBRepBuild_ListOfShapeListOfShape,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : TopOpeBRepBuild_ShapeListOfShape,theIter : Any) -> TopOpeBRepBuild_ShapeListOfShape: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TopOpeBRepBuild_ShapeListOfShape: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TopOpeBRepBuild_ListOfShapeListOfShape) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : TopOpeBRepBuild_ShapeListOfShape) -> TopOpeBRepBuild_ShapeListOfShape: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepBuild_ListOfShapeListOfShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepBuild_Loop(OCP.Standard.Standard_Transient):
    """
    a Loop is an existing shape (Shell,Wire) or a set of shapes (Faces,Edges) which are connex. a set of connex shape is represented by a BlockIteratora Loop is an existing shape (Shell,Wire) or a set of shapes (Faces,Edges) which are connex. a set of connex shape is represented by a BlockIteratora Loop is an existing shape (Shell,Wire) or a set of shapes (Faces,Edges) which are connex. a set of connex shape is represented by a BlockIterator
    """
    def BlockIterator(self) -> TopOpeBRepBuild_BlockIterator: 
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
    def Dump(self) -> None: 
        """
        None
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
    def IsShape(self) -> bool: 
        """
        None
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
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self,BI : TopOpeBRepBuild_BlockIterator) -> None: ...
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
class TopOpeBRepBuild_CompositeClassifier(TopOpeBRepBuild_LoopClassifier):
    """
    classify composite Loops, i.e, loops that can be either a Shape, or a block of Elements.
    """
    def Compare(self,L1 : TopOpeBRepBuild_Loop,L2 : TopOpeBRepBuild_Loop) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def CompareElement(self,E : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Add element <E> in the set of elements used in classification. Returns FALSE if the element <E> has been already added to the set of elements, otherwise returns TRUE.
        """
    def CompareElementToShape(self,E : OCP.TopoDS.TopoDS_Shape,B : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        classify element <E> with shape <B>
        """
    def CompareShapes(self,B1 : OCP.TopoDS.TopoDS_Shape,B2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        classify shape <B1> with shape <B2>
        """
    def ResetElement(self,E : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        prepare classification involving element <E>.
        """
    def ResetShape(self,B : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        prepare classification involving shape <B> calls ResetElement on first element of <B>
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns state of classification of 2D point, defined by ResetElement, with the current set of elements, defined by Compare.
        """
    pass
class TopOpeBRepBuild_LoopEnum():
    """
    None

    Members:

      TopOpeBRepBuild_ANYLOOP

      TopOpeBRepBuild_BOUNDARY

      TopOpeBRepBuild_BLOCK
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
    TopOpeBRepBuild_ANYLOOP: OCP.TopOpeBRepBuild.TopOpeBRepBuild_LoopEnum # value = <TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_ANYLOOP: 0>
    TopOpeBRepBuild_BLOCK: OCP.TopOpeBRepBuild.TopOpeBRepBuild_LoopEnum # value = <TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BLOCK: 2>
    TopOpeBRepBuild_BOUNDARY: OCP.TopOpeBRepBuild.TopOpeBRepBuild_LoopEnum # value = <TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BOUNDARY: 1>
    __entries: dict # value = {'TopOpeBRepBuild_ANYLOOP': (<TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_ANYLOOP: 0>, None), 'TopOpeBRepBuild_BOUNDARY': (<TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BOUNDARY: 1>, None), 'TopOpeBRepBuild_BLOCK': (<TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BLOCK: 2>, None)}
    __members__: dict # value = {'TopOpeBRepBuild_ANYLOOP': <TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_ANYLOOP: 0>, 'TopOpeBRepBuild_BOUNDARY': <TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BOUNDARY: 1>, 'TopOpeBRepBuild_BLOCK': <TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BLOCK: 2>}
    pass
class TopOpeBRepBuild_LoopSet():
    """
    None
    """
    def ChangeListOfLoop(self) -> TopOpeBRepBuild_ListOfLoop: 
        """
        None
        """
    def InitLoop(self) -> None: 
        """
        None
        """
    def Loop(self) -> TopOpeBRepBuild_Loop: 
        """
        None
        """
    def MoreLoop(self) -> bool: 
        """
        None
        """
    def NextLoop(self) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_Pave(TopOpeBRepBuild_Loop, OCP.Standard.Standard_Transient):
    def BlockIterator(self) -> TopOpeBRepBuild_BlockIterator: 
        """
        None
        """
    def ChangeVertex(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Dump(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def HasSameDomain(self) -> bool: 
        """
        None

        None
        """
    @overload
    def HasSameDomain(self,b : bool) -> None: ...
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InterferenceType(self) -> OCP.TopOpeBRepDS.TopOpeBRepDS_Kind: 
        """
        None
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
    def IsShape(self) -> bool: 
        """
        None
        """
    @overload
    def Parameter(self) -> float: 
        """
        None

        None
        """
    @overload
    def Parameter(self,Par : float) -> None: ...
    @overload
    def SameDomain(self,VSD : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def SameDomain(self) -> OCP.TopoDS.TopoDS_Shape: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def __init__(self,V : OCP.TopoDS.TopoDS_Shape,P : float,bound : bool) -> None: ...
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
class TopOpeBRepBuild_PaveClassifier(TopOpeBRepBuild_LoopClassifier):
    """
    This class compares vertices on an edge.
    """
    @staticmethod
    def AdjustCase_s(p1 : float,o : OCP.TopAbs.TopAbs_Orientation,first : float,period : float,tol : float,cas : int) -> float: 
        """
        None
        """
    def ClosedVertices(self,B : bool) -> None: 
        """
        None
        """
    def Compare(self,L1 : TopOpeBRepBuild_Loop,L2 : TopOpeBRepBuild_Loop) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns state of vertex <L1> compared with <L2>.
        """
    def SetFirstParameter(self,P : float) -> None: 
        """
        None
        """
    def __init__(self,E : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class TopOpeBRepBuild_PaveSet(TopOpeBRepBuild_LoopSet):
    """
    class providing an exploration of a set of vertices to build edges. It is similar to LoopSet from TopOpeBRepBuild where Loop is Pave.
    """
    def Append(self,PV : TopOpeBRepBuild_Pave) -> None: 
        """
        Add <PV> in the Pave set.
        """
    def ChangeListOfLoop(self) -> TopOpeBRepBuild_ListOfLoop: 
        """
        None
        """
    def ClosedVertices(self) -> bool: 
        """
        None
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def EqualParameters(self) -> float: 
        """
        None
        """
    def HasEqualParameters(self) -> bool: 
        """
        None
        """
    def InitLoop(self) -> None: 
        """
        None
        """
    def Loop(self) -> TopOpeBRepBuild_Loop: 
        """
        None
        """
    def MoreLoop(self) -> bool: 
        """
        None
        """
    def NextLoop(self) -> None: 
        """
        None
        """
    def RemovePV(self,B : bool) -> None: 
        """
        None
        """
    @staticmethod
    def SortPave_s(Lin : TopOpeBRepBuild_ListOfPave,Lout : TopOpeBRepBuild_ListOfPave) -> None: 
        """
        None
        """
    def __init__(self,E : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class TopOpeBRepBuild_ShapeListOfShape():
    """
    represent shape + a list of shape
    """
    def ChangeList(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def ChangeShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def List(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> None: ...
    pass
class TopOpeBRepBuild_ShapeSet():
    """
    Auxiliary class providing an exploration of a set of shapes to build faces or solids. To build faces : shapes are wires, elements are edges. To build solids : shapes are shells, elements are faces. The ShapeSet stores a list of shapes, a list of elements to start reconstructions, and a map to search neighbours. The map stores the connection between elements through subshapes of type <SubShapeType> given in constructor. <SubShapeType> is : - TopAbs_VERTEX to connect edges - TopAbs_EDGE to connect faces
    """
    def AddElement(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        for each subshape SE of S of type mySubShapeType - Add subshapes of S to the map of subshapes (mySubShapeMap) - Add S to the list of shape incident to subshapes of S.
        """
    def AddShape(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds <S> to the list of shapes. (wires or shells).
        """
    def AddStartElement(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        (S is a face or edge) Add S to the list of starting shapes used for reconstructions. apply AddElement(S).
        """
    def ChangeStartShapes(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    @overload
    def CheckShape(self,S : OCP.TopoDS.TopoDS_Shape,checkgeom : bool=False) -> bool: 
        """
        None

        None

        None
        """
    @overload
    def CheckShape(self,checkshape : bool) -> None: ...
    @overload
    def CheckShape(self) -> bool: ...
    @overload
    def DEBName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def DEBName(self,N : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def DEBNumber(self) -> int: 
        """
        None

        None
        """
    @overload
    def DEBNumber(self,I : int) -> None: ...
    def DumpBB(self) -> None: 
        """
        None
        """
    def DumpCheck(self,OS : io.BytesIO,str : OCP.TCollection.TCollection_AsciiString,S : OCP.TopoDS.TopoDS_Shape,chk : bool) -> None: 
        """
        None
        """
    def DumpName(self,OS : io.BytesIO,str : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def DumpSS(self) -> None: 
        """
        None
        """
    def FindNeighbours(self) -> None: 
        """
        Build the list of neighbour shapes of myCurrentShape (neighbour shapes and myCurrentShapes are of type t) Initialize myIncidentShapesIter on neighbour shapes.
        """
    def InitNeighbours(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitShapes(self) -> None: 
        """
        None
        """
    def InitStartElements(self) -> None: 
        """
        None
        """
    def MakeNeighboursList(self,E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def MaxNumberSubShape(self,Shape : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def MoreNeighbours(self) -> bool: 
        """
        None
        """
    def MoreShapes(self) -> bool: 
        """
        None
        """
    def MoreStartElements(self) -> bool: 
        """
        None
        """
    def Neighbour(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def NextNeighbour(self) -> None: 
        """
        None
        """
    def NextShape(self) -> None: 
        """
        None
        """
    def NextStartElement(self) -> None: 
        """
        None
        """
    @overload
    def SName(self,S : OCP.TopoDS.TopoDS_Shape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def SName(self,S : OCP.TopTools.TopTools_ListOfShape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    @overload
    def SNameori(self,S : OCP.TopTools.TopTools_ListOfShape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def SNameori(self,S : OCP.TopoDS.TopoDS_Shape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def StartElement(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def StartElements(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        return a reference on myStartShapes
        """
    def __init__(self,SubShapeType : OCP.TopAbs.TopAbs_ShapeEnum,checkshape : bool=True) -> None: ...
    pass
class TopOpeBRepBuild_ShellFaceClassifier(TopOpeBRepBuild_CompositeClassifier, TopOpeBRepBuild_LoopClassifier):
    """
    Classify faces and shells. shapes are Shells, Elements are Faces.
    """
    def Clear(self) -> None: 
        """
        None
        """
    def Compare(self,L1 : TopOpeBRepBuild_Loop,L2 : TopOpeBRepBuild_Loop) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def CompareElement(self,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Add the face <F> in the set of faces used in 3D point classification. Returns FALSE if the face <F> has been already added to the set of faces, otherwise returns TRUE.
        """
    def CompareElementToShape(self,F : OCP.TopoDS.TopoDS_Shape,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        classify face <F> with shell <S>
        """
    def CompareShapes(self,B1 : OCP.TopoDS.TopoDS_Shape,B2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        classify shell <B1> with shell <B2>
        """
    def ResetElement(self,F : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        prepare classification involving face <F> define 3D point (later used in Compare()) on first vertex of face <F>.
        """
    def ResetShape(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        prepare classification involving shell <S> calls ResetElement on first face of <S>
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns state of classification of 3D point, defined by ResetElement, with the current set of faces, defined by Compare.
        """
    def __init__(self,BB : TopOpeBRepBuild_BlockBuilder) -> None: ...
    pass
class TopOpeBRepBuild_ShellFaceSet(TopOpeBRepBuild_ShapeSet):
    """
    a bound is a shell, a boundelement is a face. The ShapeSet stores : - a list of shell (bounds), - a list of face (boundelements) to start reconstructions, - a map of edge giving the list of face incident to an edge.
    """
    def AddElement(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddShape(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddStartElement(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def ChangeStartShapes(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    @overload
    def CheckShape(self,S : OCP.TopoDS.TopoDS_Shape,checkgeom : bool=False) -> bool: 
        """
        None

        None

        None
        """
    @overload
    def CheckShape(self,checkshape : bool) -> None: ...
    @overload
    def CheckShape(self) -> bool: ...
    @overload
    def DEBName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def DEBName(self,N : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def DEBNumber(self) -> int: 
        """
        None

        None
        """
    @overload
    def DEBNumber(self,I : int) -> None: ...
    def DumpBB(self) -> None: 
        """
        None
        """
    def DumpCheck(self,OS : io.BytesIO,str : OCP.TCollection.TCollection_AsciiString,S : OCP.TopoDS.TopoDS_Shape,chk : bool) -> None: 
        """
        None
        """
    def DumpName(self,OS : io.BytesIO,str : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def DumpSS(self) -> None: 
        """
        None
        """
    def FindNeighbours(self) -> None: 
        """
        Build the list of neighbour shapes of myCurrentShape (neighbour shapes and myCurrentShapes are of type t) Initialize myIncidentShapesIter on neighbour shapes.
        """
    def InitNeighbours(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitShapes(self) -> None: 
        """
        None
        """
    def InitStartElements(self) -> None: 
        """
        None
        """
    def MakeNeighboursList(self,E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def MaxNumberSubShape(self,Shape : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def MoreNeighbours(self) -> bool: 
        """
        None
        """
    def MoreShapes(self) -> bool: 
        """
        None
        """
    def MoreStartElements(self) -> bool: 
        """
        None
        """
    def Neighbour(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def NextNeighbour(self) -> None: 
        """
        None
        """
    def NextShape(self) -> None: 
        """
        None
        """
    def NextStartElement(self) -> None: 
        """
        None
        """
    @overload
    def SName(self,S : OCP.TopoDS.TopoDS_Shape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def SName(self,S : OCP.TopTools.TopTools_ListOfShape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    @overload
    def SNameori(self,S : OCP.TopTools.TopTools_ListOfShape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def SNameori(self,S : OCP.TopoDS.TopoDS_Shape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        None
        """
    def StartElement(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def StartElements(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        return a reference on myStartShapes
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,Addr : capsule=None) -> None: ...
    pass
class TopOpeBRepBuild_ShellToSolid():
    """
    This class builds solids from a set of shells SSh and a solid F.
    """
    def AddShell(self,Sh : OCP.TopoDS.TopoDS_Shell) -> None: 
        """
        None
        """
    def Init(self) -> None: 
        """
        None
        """
    def MakeSolids(self,So : OCP.TopoDS.TopoDS_Solid,LSo : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_SolidAreaBuilder(TopOpeBRepBuild_Area3dBuilder, TopOpeBRepBuild_AreaBuilder):
    """
    The SolidAreaBuilder algorithm is used to construct Solids from a LoopSet, where the Loop is the composite topological object of the boundary, here wire or block of edges. The LoopSet gives an iteration on Loops. For each Loop it indicates if it is on the boundary (wire) or if it results from an interference (block of edges). The result of the SolidAreaBuilder is an iteration on areas. An area is described by a set of Loops.
    """
    def ADD_LISTOFLoop_TO_LISTOFLoop(self,LOL1 : TopOpeBRepBuild_ListOfLoop,LOL2 : TopOpeBRepBuild_ListOfLoop,s : capsule=None,s1 : capsule=None,s2 : capsule=None) -> None: 
        """
        None
        """
    def ADD_Loop_TO_LISTOFLoop(self,L : TopOpeBRepBuild_Loop,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    def InitArea(self) -> int: 
        """
        Initialize iteration on areas.
        """
    def InitAreaBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        Sets a Area1dBuilder to find the areas of the shapes described by <LS> using the classifier <LC>.
        """
    def InitLoop(self) -> int: 
        """
        Initialize iteration on loops of current Area.
        """
    def InitSolidAreaBuilder(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: 
        """
        None
        """
    def Loop(self) -> TopOpeBRepBuild_Loop: 
        """
        Returns the current Loop in the current area.
        """
    def MoreArea(self) -> bool: 
        """
        None
        """
    def MoreLoop(self) -> bool: 
        """
        None
        """
    def NextArea(self) -> None: 
        """
        None
        """
    def NextLoop(self) -> None: 
        """
        None
        """
    def REM_Loop_FROM_LISTOFLoop(self,ITLOL : Any,LOL : TopOpeBRepBuild_ListOfLoop,s : capsule=None) -> None: 
        """
        None
        """
    @overload
    def __init__(self,LS : TopOpeBRepBuild_LoopSet,LC : TopOpeBRepBuild_LoopClassifier,ForceClass : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_SolidBuilder():
    """
    None
    """
    def Face(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns current new face of current new shell.
        """
    def InitFace(self) -> int: 
        """
        None
        """
    def InitShell(self) -> int: 
        """
        None
        """
    def InitSolid(self) -> int: 
        """
        None
        """
    def InitSolidBuilder(self,FS : TopOpeBRepBuild_ShellFaceSet,ForceClass : bool) -> None: 
        """
        None
        """
    def IsOldShell(self) -> bool: 
        """
        None
        """
    def MoreFace(self) -> bool: 
        """
        None
        """
    def MoreShell(self) -> bool: 
        """
        None
        """
    def MoreSolid(self) -> bool: 
        """
        None
        """
    def NextFace(self) -> None: 
        """
        None
        """
    def NextShell(self) -> None: 
        """
        None
        """
    def NextSolid(self) -> None: 
        """
        None
        """
    def OldShell(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns current shell This shell may be : * an old shell OldShell(), which has not been reconstructed; * a new shell made of faces described by ...NewFace() methods.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,FS : TopOpeBRepBuild_ShellFaceSet,ForceClass : bool=False) -> None: ...
    pass
class TopOpeBRepBuild_Tools():
    """
    Auxiliary methods used in TopOpeBRepBuild_Builder1 class
    """
    @staticmethod
    def CheckFaceClosed2d_s(theFace : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Checks if <theFace> has the properly closed in 2D boundary(ies)
        """
    @staticmethod
    def CorrectCurveOnSurface_s(aS : OCP.TopoDS.TopoDS_Shape,aTolMax : float=0.0001) -> None: 
        """
        None
        """
    @staticmethod
    def CorrectFace2d_s(oldFace : OCP.TopoDS.TopoDS_Shape,corrFace : OCP.TopoDS.TopoDS_Shape,aSourceShapes : OCP.TopTools.TopTools_IndexedMapOfOrientedShape,aMapOfCorrect2dEdges : OCP.TopTools.TopTools_IndexedDataMapOfShapeShape) -> None: 
        """
        test if UV representation of <oldFace> is good (i.e. face is closed in 2d). if face is not closed , this method will try to close such face and will return corrected edges in the <aMapOfCorrect2dEdges>. Parameter <aSourceShapes> used to fix the edge (or wires) which should be correct (Corrector used it as a start shapes). NOTE : Parameter corrFace doesn't mean anything. If you want to use this method , rebuild resulting face after by yourself using corrected edges.
        """
    @staticmethod
    def CorrectPointOnCurve_s(aS : OCP.TopoDS.TopoDS_Shape,aTolMax : float=0.0001) -> None: 
        """
        None
        """
    @staticmethod
    def CorrectTolerances_s(aS : OCP.TopoDS.TopoDS_Shape,aTolMax : float=0.0001) -> None: 
        """
        None
        """
    @staticmethod
    def FindStateThroughVertex_s(aShape : OCP.TopoDS.TopoDS_Shape,aShapeClassifier : OCP.TopOpeBRepTool.TopOpeBRepTool_ShapeClassifier,aMapOfShapeWithState : OCP.TopOpeBRepDS.TopOpeBRepDS_IndexedDataMapOfShapeWithState,anAvoidSubshMap : OCP.TopTools.TopTools_MapOfShape) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    @staticmethod
    def GetAdjacentFace_s(aFaceObj : OCP.TopoDS.TopoDS_Shape,anEObj : OCP.TopoDS.TopoDS_Shape,anEdgeFaceMap : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape,anAdjFaceObj : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    @staticmethod
    def GetNormalInNearestPoint_s(aFace : OCP.TopoDS.TopoDS_Face,anEdge : OCP.TopoDS.TopoDS_Edge,aNormal : OCP.gp.gp_Vec) -> None: 
        """
        This function used to compute normal in point which is located near the point with param UV (used for computation of normals where the normal in the point UV equal to zero).
        """
    @staticmethod
    def GetNormalToFaceOnEdge_s(aFObj : OCP.TopoDS.TopoDS_Face,anEdgeObj : OCP.TopoDS.TopoDS_Edge,aDirNormal : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    @staticmethod
    def GetTangentToEdgeEdge_s(aFObj : OCP.TopoDS.TopoDS_Face,anEdgeObj : OCP.TopoDS.TopoDS_Edge,aOriEObj : OCP.TopoDS.TopoDS_Edge,aTangent : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    @staticmethod
    def GetTangentToEdge_s(anEdgeObj : OCP.TopoDS.TopoDS_Edge,aTangent : OCP.gp.gp_Vec) -> bool: 
        """
        None
        """
    @staticmethod
    def IsDegEdgesTheSame_s(anE1 : OCP.TopoDS.TopoDS_Shape,anE2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    @staticmethod
    def NormalizeFace_s(oldFace : OCP.TopoDS.TopoDS_Shape,corrFace : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        test if <oldFace> does not contain INTERNAL or EXTERNAL edges and remove such edges in case of its presence. The result is stored in <corrFace>
        """
    @staticmethod
    def PropagateStateForWires_s(aFacesToRestMap : OCP.TopTools.TopTools_IndexedMapOfShape,aMapOfShapeWithState : OCP.TopOpeBRepDS.TopOpeBRepDS_IndexedDataMapOfShapeWithState) -> None: 
        """
        None
        """
    @staticmethod
    def SpreadStateToChild_s(aShape : OCP.TopoDS.TopoDS_Shape,aState : OCP.TopAbs.TopAbs_State,aMapOfShapeWithState : OCP.TopOpeBRepDS.TopOpeBRepDS_IndexedDataMapOfShapeWithState) -> None: 
        """
        None
        """
    @staticmethod
    def UpdateEdgeOnFace_s(aEdgeToUpdate : OCP.TopoDS.TopoDS_Edge,OldFace : OCP.TopoDS.TopoDS_Face,NewFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        recompute PCurve of the edge on the NewFace
        """
    @staticmethod
    def UpdateEdgeOnPeriodicalFace_s(aEdgeToUpdate : OCP.TopoDS.TopoDS_Edge,OldFace : OCP.TopoDS.TopoDS_Face,NewFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        recompute PCurves of the closing (SIM , with 2 PCurves) edge on the NewFace
        """
    @staticmethod
    def UpdatePCurves_s(aWire : OCP.TopoDS.TopoDS_Wire,fromFace : OCP.TopoDS.TopoDS_Face,toFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Recompute PCurves of the all edges from the wire on the <toFace>
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_Tools2d():
    """
    None
    """
    @staticmethod
    def DumpMapOfShapeVertexInfo_s(aMap : TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo) -> None: 
        """
        None
        """
    @staticmethod
    def MakeMapOfShapeVertexInfo_s(aWire : OCP.TopoDS.TopoDS_Wire,aMap : TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo) -> None: 
        """
        None
        """
    @staticmethod
    def Path_s(aWire : OCP.TopoDS.TopoDS_Wire,aResList : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_VertexInfo():
    """
    None
    """
    def AddIn(self,anE : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def AddOut(self,anE : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def AppendPassed(self,anE : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def ChangeEdgesOut(self) -> OCP.TopTools.TopTools_IndexedMapOfOrientedShape: 
        """
        None
        """
    def CurrentOut(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def Dump(self) -> None: 
        """
        None
        """
    def EdgesIn(self) -> OCP.TopTools.TopTools_IndexedMapOfOrientedShape: 
        """
        None
        """
    def EdgesOut(self) -> OCP.TopTools.TopTools_IndexedMapOfOrientedShape: 
        """
        None
        """
    def FoundOut(self) -> int: 
        """
        None
        """
    def ListPassed(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def NbCases(self) -> int: 
        """
        None
        """
    def Prepare(self,aL : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def RemovePassed(self) -> None: 
        """
        None
        """
    def SetCurrentIn(self,anE : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def SetSmart(self,aFlag : bool) -> None: 
        """
        None
        """
    def SetVertex(self,aV : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None
        """
    def Smart(self) -> bool: 
        """
        None
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepBuild_WireEdgeClassifier(TopOpeBRepBuild_CompositeClassifier, TopOpeBRepBuild_LoopClassifier):
    """
    Classify edges and wires. shapes are Wires, Element are Edge.
    """
    def Compare(self,L1 : TopOpeBRepBuild_Loop,L2 : TopOpeBRepBuild_Loop) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def CompareElement(self,E : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Add the edge <E> in the set of edges used in 2D point classification.
        """
    def CompareElementToShape(self,E : OCP.TopoDS.TopoDS_Shape,B : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        classify edge <E> with wire <B>
        """
    def CompareShapes(self,B1 : OCP.TopoDS.TopoDS_Shape,B2 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        classify wire <B1> with wire <B2>
        """
    def LoopToShape(self,L : TopOpeBRepBuild_Loop) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def ResetElement(self,E : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        prepare classification involving edge <E> define 2D point (later used in Compare()) on first vertex of edge <E>.
        """
    def ResetShape(self,B : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        prepare classification involving wire <B> calls ResetElement on first edge of <B>
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns state of classification of 2D point, defined by ResetElement, with the current set of edges, defined by Compare.
        """
    def __init__(self,F : OCP.TopoDS.TopoDS_Shape,BB : TopOpeBRepBuild_BlockBuilder) -> None: ...
    pass
class TopOpeBRepBuild_WireEdgeSet(TopOpeBRepBuild_ShapeSet):
    """
    a bound is a wire, a boundelement is an edge. The ShapeSet stores : - a list of wire (bounds), - a list of edge (boundelements) to start reconstructions, - a map of vertex giving the list of edge incident to a vertex.
    """
    def AddElement(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddShape(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddStartElement(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def ChangeStartShapes(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    @overload
    def CheckShape(self,S : OCP.TopoDS.TopoDS_Shape,checkgeom : bool=False) -> bool: 
        """
        None

        None

        None
        """
    @overload
    def CheckShape(self,checkshape : bool) -> None: ...
    @overload
    def CheckShape(self) -> bool: ...
    @overload
    def DEBName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def DEBName(self,N : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def DEBNumber(self) -> int: 
        """
        None

        None
        """
    @overload
    def DEBNumber(self,I : int) -> None: ...
    def DumpBB(self) -> None: 
        """
        None
        """
    def DumpCheck(self,OS : io.BytesIO,str : OCP.TCollection.TCollection_AsciiString,S : OCP.TopoDS.TopoDS_Shape,chk : bool) -> None: 
        """
        None
        """
    def DumpName(self,OS : io.BytesIO,str : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def DumpSS(self) -> None: 
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        value of field myFace
        """
    def FindNeighbours(self) -> None: 
        """
        Build the list of neighbour edges of edge myCurrentShape Initialize iterator of neighbour edges to edge myCurrentShape
        """
    def InitNeighbours(self,E : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitShapes(self) -> None: 
        """
        None
        """
    def InitStartElements(self) -> None: 
        """
        None
        """
    @staticmethod
    def IsUVISO_s(E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> Tuple[bool, bool]: 
        """
        None
        """
    def MakeNeighboursList(self,E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def MaxNumberSubShape(self,Shape : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def MoreNeighbours(self) -> bool: 
        """
        None
        """
    def MoreShapes(self) -> bool: 
        """
        None
        """
    def MoreStartElements(self) -> bool: 
        """
        None
        """
    def Neighbour(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def NextNeighbour(self) -> None: 
        """
        None
        """
    def NextShape(self) -> None: 
        """
        None
        """
    def NextStartElement(self) -> None: 
        """
        None
        """
    @overload
    def SName(self,S : OCP.TopoDS.TopoDS_Shape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def SName(self,S : OCP.TopTools.TopTools_ListOfShape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    @overload
    def SNameori(self,S : OCP.TopTools.TopTools_ListOfShape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def SNameori(self,S : OCP.TopoDS.TopoDS_Shape,sb : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,sa : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def StartElement(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def StartElements(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        return a reference on myStartShapes
        """
    def __init__(self,F : OCP.TopoDS.TopoDS_Shape,Addr : capsule=None) -> None: ...
    pass
class TopOpeBRepBuild_WireToFace():
    """
    This class builds faces from a set of wires SW and a face F. The face must have and underlying surface, say S. All of the edges of all of the wires must have a 2d representation on surface S (except if S is planar)
    """
    def AddWire(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        None
        """
    def Init(self) -> None: 
        """
        None
        """
    def MakeFaces(self,F : OCP.TopoDS.TopoDS_Face,LF : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
TopOpeBRepBuild_ANYLOOP: OCP.TopOpeBRepBuild.TopOpeBRepBuild_LoopEnum # value = <TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_ANYLOOP: 0>
TopOpeBRepBuild_BLOCK: OCP.TopOpeBRepBuild.TopOpeBRepBuild_LoopEnum # value = <TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BLOCK: 2>
TopOpeBRepBuild_BOUNDARY: OCP.TopOpeBRepBuild.TopOpeBRepBuild_LoopEnum # value = <TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BOUNDARY: 1>
