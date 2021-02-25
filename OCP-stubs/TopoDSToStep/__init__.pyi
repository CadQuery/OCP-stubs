import OCP.TopoDSToStep
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.TCollection
import OCP.Transfer
import OCP.TopoDS
import OCP.StepShape
import OCP.Standard
__all__  = [
"TopoDSToStep",
"TopoDSToStep_Root",
"TopoDSToStep_BuilderError",
"TopoDSToStep_FacetedError",
"TopoDSToStep_FacetedTool",
"TopoDSToStep_MakeBrepWithVoids",
"TopoDSToStep_MakeEdgeError",
"TopoDSToStep_MakeFaceError",
"TopoDSToStep_MakeFacetedBrep",
"TopoDSToStep_MakeFacetedBrepAndBrepWithVoids",
"TopoDSToStep_MakeGeometricCurveSet",
"TopoDSToStep_MakeManifoldSolidBrep",
"TopoDSToStep_MakeShellBasedSurfaceModel",
"TopoDSToStep_MakeStepEdge",
"TopoDSToStep_MakeStepFace",
"TopoDSToStep_MakeStepVertex",
"TopoDSToStep_MakeStepWire",
"TopoDSToStep_MakeVertexError",
"TopoDSToStep_MakeWireError",
"TopoDSToStep_Builder",
"TopoDSToStep_Tool",
"TopoDSToStep_WireframeBuilder",
"TopoDSToStep_BuilderDone",
"TopoDSToStep_BuilderOther",
"TopoDSToStep_EdgeDone",
"TopoDSToStep_EdgeOther",
"TopoDSToStep_FaceDone",
"TopoDSToStep_FaceOther",
"TopoDSToStep_FacetedDone",
"TopoDSToStep_InfiniteFace",
"TopoDSToStep_NoFaceMapped",
"TopoDSToStep_NoWireMapped",
"TopoDSToStep_NonManifoldEdge",
"TopoDSToStep_NonManifoldFace",
"TopoDSToStep_NonManifoldWire",
"TopoDSToStep_PCurveNotLinear",
"TopoDSToStep_SurfaceNotPlane",
"TopoDSToStep_VertexDone",
"TopoDSToStep_VertexOther",
"TopoDSToStep_WireDone",
"TopoDSToStep_WireOther"
]
class TopoDSToStep():
    """
    This package implements the mapping between CAS.CAD Shape representation and AP214 Shape Representation. The target schema is pms_c4 (a subset of AP214)
    """
    @staticmethod
    @overload
    def AddResult_s(FP : OCP.Transfer.Transfer_FinderProcess,Tool : TopoDSToStep_Tool) -> None: 
        """
        Adds an entity into the list of results (binders) for shape stored in FinderProcess

        Adds all entities recorded in Tool into the map of results (binders) stored in FinderProcess
        """
    @staticmethod
    @overload
    def AddResult_s(FP : OCP.Transfer.Transfer_FinderProcess,Shape : OCP.TopoDS.TopoDS_Shape,entity : OCP.Standard.Standard_Transient) -> None: ...
    @staticmethod
    def DecodeBuilderError_s(E : TopoDSToStep_BuilderError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def DecodeEdgeError_s(E : TopoDSToStep_MakeEdgeError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def DecodeFaceError_s(E : TopoDSToStep_MakeFaceError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def DecodeVertexError_s(E : TopoDSToStep_MakeVertexError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns a new shape without undirect surfaces.
        """
    @staticmethod
    def DecodeWireError_s(E : TopoDSToStep_MakeWireError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopoDSToStep_Root():
    """
    This class implements the common services for all classes of TopoDSToStep which report error.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_BuilderError():
    """
    None

    Members:

      TopoDSToStep_BuilderDone

      TopoDSToStep_NoFaceMapped

      TopoDSToStep_BuilderOther
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
    TopoDSToStep_BuilderDone: OCP.TopoDSToStep.TopoDSToStep_BuilderError # value = <TopoDSToStep_BuilderError.TopoDSToStep_BuilderDone: 0>
    TopoDSToStep_BuilderOther: OCP.TopoDSToStep.TopoDSToStep_BuilderError # value = <TopoDSToStep_BuilderError.TopoDSToStep_BuilderOther: 2>
    TopoDSToStep_NoFaceMapped: OCP.TopoDSToStep.TopoDSToStep_BuilderError # value = <TopoDSToStep_BuilderError.TopoDSToStep_NoFaceMapped: 1>
    __entries: dict # value = {'TopoDSToStep_BuilderDone': (<TopoDSToStep_BuilderError.TopoDSToStep_BuilderDone: 0>, None), 'TopoDSToStep_NoFaceMapped': (<TopoDSToStep_BuilderError.TopoDSToStep_NoFaceMapped: 1>, None), 'TopoDSToStep_BuilderOther': (<TopoDSToStep_BuilderError.TopoDSToStep_BuilderOther: 2>, None)}
    __members__: dict # value = {'TopoDSToStep_BuilderDone': <TopoDSToStep_BuilderError.TopoDSToStep_BuilderDone: 0>, 'TopoDSToStep_NoFaceMapped': <TopoDSToStep_BuilderError.TopoDSToStep_NoFaceMapped: 1>, 'TopoDSToStep_BuilderOther': <TopoDSToStep_BuilderError.TopoDSToStep_BuilderOther: 2>}
    pass
class TopoDSToStep_FacetedError():
    """
    None

    Members:

      TopoDSToStep_FacetedDone

      TopoDSToStep_SurfaceNotPlane

      TopoDSToStep_PCurveNotLinear
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
    TopoDSToStep_FacetedDone: OCP.TopoDSToStep.TopoDSToStep_FacetedError # value = <TopoDSToStep_FacetedError.TopoDSToStep_FacetedDone: 0>
    TopoDSToStep_PCurveNotLinear: OCP.TopoDSToStep.TopoDSToStep_FacetedError # value = <TopoDSToStep_FacetedError.TopoDSToStep_PCurveNotLinear: 2>
    TopoDSToStep_SurfaceNotPlane: OCP.TopoDSToStep.TopoDSToStep_FacetedError # value = <TopoDSToStep_FacetedError.TopoDSToStep_SurfaceNotPlane: 1>
    __entries: dict # value = {'TopoDSToStep_FacetedDone': (<TopoDSToStep_FacetedError.TopoDSToStep_FacetedDone: 0>, None), 'TopoDSToStep_SurfaceNotPlane': (<TopoDSToStep_FacetedError.TopoDSToStep_SurfaceNotPlane: 1>, None), 'TopoDSToStep_PCurveNotLinear': (<TopoDSToStep_FacetedError.TopoDSToStep_PCurveNotLinear: 2>, None)}
    __members__: dict # value = {'TopoDSToStep_FacetedDone': <TopoDSToStep_FacetedError.TopoDSToStep_FacetedDone: 0>, 'TopoDSToStep_SurfaceNotPlane': <TopoDSToStep_FacetedError.TopoDSToStep_SurfaceNotPlane: 1>, 'TopoDSToStep_PCurveNotLinear': <TopoDSToStep_FacetedError.TopoDSToStep_PCurveNotLinear: 2>}
    pass
class TopoDSToStep_FacetedTool():
    """
    This Tool Class provides Information about Faceted Shapes to be mapped to STEP.
    """
    @staticmethod
    def CheckTopoDSShape_s(SH : OCP.TopoDS.TopoDS_Shape) -> TopoDSToStep_FacetedError: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopoDSToStep_MakeBrepWithVoids(TopoDSToStep_Root):
    """
    This class implements the mapping between classes Solid from TopoDS and BrepWithVoids from StepShape. All the topology and geometry comprised into the shell or the solid are taken into account and translated.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_BrepWithVoids: 
        """
        None
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Solid,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeEdgeError():
    """
    None

    Members:

      TopoDSToStep_EdgeDone

      TopoDSToStep_NonManifoldEdge

      TopoDSToStep_EdgeOther
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
    TopoDSToStep_EdgeDone: OCP.TopoDSToStep.TopoDSToStep_MakeEdgeError # value = <TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeDone: 0>
    TopoDSToStep_EdgeOther: OCP.TopoDSToStep.TopoDSToStep_MakeEdgeError # value = <TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeOther: 2>
    TopoDSToStep_NonManifoldEdge: OCP.TopoDSToStep.TopoDSToStep_MakeEdgeError # value = <TopoDSToStep_MakeEdgeError.TopoDSToStep_NonManifoldEdge: 1>
    __entries: dict # value = {'TopoDSToStep_EdgeDone': (<TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeDone: 0>, None), 'TopoDSToStep_NonManifoldEdge': (<TopoDSToStep_MakeEdgeError.TopoDSToStep_NonManifoldEdge: 1>, None), 'TopoDSToStep_EdgeOther': (<TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeOther: 2>, None)}
    __members__: dict # value = {'TopoDSToStep_EdgeDone': <TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeDone: 0>, 'TopoDSToStep_NonManifoldEdge': <TopoDSToStep_MakeEdgeError.TopoDSToStep_NonManifoldEdge: 1>, 'TopoDSToStep_EdgeOther': <TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeOther: 2>}
    pass
class TopoDSToStep_MakeFaceError():
    """
    None

    Members:

      TopoDSToStep_FaceDone

      TopoDSToStep_InfiniteFace

      TopoDSToStep_NonManifoldFace

      TopoDSToStep_NoWireMapped

      TopoDSToStep_FaceOther
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
    TopoDSToStep_FaceDone: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_FaceDone: 0>
    TopoDSToStep_FaceOther: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_FaceOther: 4>
    TopoDSToStep_InfiniteFace: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_InfiniteFace: 1>
    TopoDSToStep_NoWireMapped: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_NoWireMapped: 3>
    TopoDSToStep_NonManifoldFace: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_NonManifoldFace: 2>
    __entries: dict # value = {'TopoDSToStep_FaceDone': (<TopoDSToStep_MakeFaceError.TopoDSToStep_FaceDone: 0>, None), 'TopoDSToStep_InfiniteFace': (<TopoDSToStep_MakeFaceError.TopoDSToStep_InfiniteFace: 1>, None), 'TopoDSToStep_NonManifoldFace': (<TopoDSToStep_MakeFaceError.TopoDSToStep_NonManifoldFace: 2>, None), 'TopoDSToStep_NoWireMapped': (<TopoDSToStep_MakeFaceError.TopoDSToStep_NoWireMapped: 3>, None), 'TopoDSToStep_FaceOther': (<TopoDSToStep_MakeFaceError.TopoDSToStep_FaceOther: 4>, None)}
    __members__: dict # value = {'TopoDSToStep_FaceDone': <TopoDSToStep_MakeFaceError.TopoDSToStep_FaceDone: 0>, 'TopoDSToStep_InfiniteFace': <TopoDSToStep_MakeFaceError.TopoDSToStep_InfiniteFace: 1>, 'TopoDSToStep_NonManifoldFace': <TopoDSToStep_MakeFaceError.TopoDSToStep_NonManifoldFace: 2>, 'TopoDSToStep_NoWireMapped': <TopoDSToStep_MakeFaceError.TopoDSToStep_NoWireMapped: 3>, 'TopoDSToStep_FaceOther': <TopoDSToStep_MakeFaceError.TopoDSToStep_FaceOther: 4>}
    pass
class TopoDSToStep_MakeFacetedBrep(TopoDSToStep_Root):
    """
    This class implements the mapping between classes Shell or Solid from TopoDS and FacetedBrep from StepShape. All the topology and geometry comprised into the shell or the solid are taken into account and translated.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_FacetedBrep: 
        """
        None
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shell,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Solid,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeFacetedBrepAndBrepWithVoids(TopoDSToStep_Root):
    """
    This class implements the mapping between classes Solid from TopoDS and FacetedBrepAndBrepWithVoids from StepShape. All the topology and geometry comprised into the shell or the solid are taken into account and translated.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_FacetedBrepAndBrepWithVoids: 
        """
        None
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Solid,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeGeometricCurveSet(TopoDSToStep_Root):
    """
    This class implements the mapping between a Shape from TopoDS and a GeometricCurveSet from StepShape in order to create a GeometricallyBoundedWireframeRepresentation.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_GeometricCurveSet: 
        """
        None
        """
    def __init__(self,SH : OCP.TopoDS.TopoDS_Shape,FP : OCP.Transfer.Transfer_FinderProcess) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeManifoldSolidBrep(TopoDSToStep_Root):
    """
    This class implements the mapping between classes Shell or Solid from TopoDS and ManifoldSolidBrep from StepShape. All the topology and geometry comprised into the shell or the solid are taken into account and translated.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_ManifoldSolidBrep: 
        """
        None
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Solid,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shell,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeShellBasedSurfaceModel(TopoDSToStep_Root):
    """
    This class implements the mapping between classes Face, Shell or Solid from TopoDS and ShellBasedSurfaceModel from StepShape. All the topology and geometry comprised into the shape are taken into account and translated.
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_ShellBasedSurfaceModel: 
        """
        None
        """
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shell,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Solid,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeStepEdge(TopoDSToStep_Root):
    """
    This class implements the mapping between classes Edge from TopoDS and TopologicalRepresentationItem from StepShape.
    """
    def Error(self) -> TopoDSToStep_MakeEdgeError: 
        """
        None
        """
    def Init(self,E : OCP.TopoDS.TopoDS_Edge,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_TopologicalRepresentationItem: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeStepFace(TopoDSToStep_Root):
    """
    This class implements the mapping between classes Face from TopoDS and TopologicalRepresentationItem from StepShape.
    """
    def Error(self) -> TopoDSToStep_MakeFaceError: 
        """
        None
        """
    def Init(self,F : OCP.TopoDS.TopoDS_Face,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_TopologicalRepresentationItem: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeStepVertex(TopoDSToStep_Root):
    """
    This class implements the mapping between classes Vertex from TopoDS and TopologicalRepresentationItem from StepShape.
    """
    def Error(self) -> TopoDSToStep_MakeVertexError: 
        """
        None
        """
    def Init(self,V : OCP.TopoDS.TopoDS_Vertex,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_TopologicalRepresentationItem: 
        """
        None
        """
    @overload
    def __init__(self,V : OCP.TopoDS.TopoDS_Vertex,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeStepWire(TopoDSToStep_Root):
    """
    This class implements the mapping between classes Wire from TopoDS and TopologicalRepresentationItem from StepShape.
    """
    def Error(self) -> TopoDSToStep_MakeWireError: 
        """
        None
        """
    def Init(self,W : OCP.TopoDS.TopoDS_Wire,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_TopologicalRepresentationItem: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_MakeVertexError():
    """
    None

    Members:

      TopoDSToStep_VertexDone

      TopoDSToStep_VertexOther
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
    TopoDSToStep_VertexDone: OCP.TopoDSToStep.TopoDSToStep_MakeVertexError # value = <TopoDSToStep_MakeVertexError.TopoDSToStep_VertexDone: 0>
    TopoDSToStep_VertexOther: OCP.TopoDSToStep.TopoDSToStep_MakeVertexError # value = <TopoDSToStep_MakeVertexError.TopoDSToStep_VertexOther: 1>
    __entries: dict # value = {'TopoDSToStep_VertexDone': (<TopoDSToStep_MakeVertexError.TopoDSToStep_VertexDone: 0>, None), 'TopoDSToStep_VertexOther': (<TopoDSToStep_MakeVertexError.TopoDSToStep_VertexOther: 1>, None)}
    __members__: dict # value = {'TopoDSToStep_VertexDone': <TopoDSToStep_MakeVertexError.TopoDSToStep_VertexDone: 0>, 'TopoDSToStep_VertexOther': <TopoDSToStep_MakeVertexError.TopoDSToStep_VertexOther: 1>}
    pass
class TopoDSToStep_MakeWireError():
    """
    None

    Members:

      TopoDSToStep_WireDone

      TopoDSToStep_NonManifoldWire

      TopoDSToStep_WireOther
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
    TopoDSToStep_NonManifoldWire: OCP.TopoDSToStep.TopoDSToStep_MakeWireError # value = <TopoDSToStep_MakeWireError.TopoDSToStep_NonManifoldWire: 1>
    TopoDSToStep_WireDone: OCP.TopoDSToStep.TopoDSToStep_MakeWireError # value = <TopoDSToStep_MakeWireError.TopoDSToStep_WireDone: 0>
    TopoDSToStep_WireOther: OCP.TopoDSToStep.TopoDSToStep_MakeWireError # value = <TopoDSToStep_MakeWireError.TopoDSToStep_WireOther: 2>
    __entries: dict # value = {'TopoDSToStep_WireDone': (<TopoDSToStep_MakeWireError.TopoDSToStep_WireDone: 0>, None), 'TopoDSToStep_NonManifoldWire': (<TopoDSToStep_MakeWireError.TopoDSToStep_NonManifoldWire: 1>, None), 'TopoDSToStep_WireOther': (<TopoDSToStep_MakeWireError.TopoDSToStep_WireOther: 2>, None)}
    __members__: dict # value = {'TopoDSToStep_WireDone': <TopoDSToStep_MakeWireError.TopoDSToStep_WireDone: 0>, 'TopoDSToStep_NonManifoldWire': <TopoDSToStep_MakeWireError.TopoDSToStep_NonManifoldWire: 1>, 'TopoDSToStep_WireOther': <TopoDSToStep_MakeWireError.TopoDSToStep_WireOther: 2>}
    pass
class TopoDSToStep_Builder(TopoDSToStep_Root):
    """
    This builder Class provides services to build a ProSTEP Shape model from a Cas.Cad BRep.
    """
    def Error(self) -> TopoDSToStep_BuilderError: 
        """
        None
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.StepShape.StepShape_TopologicalRepresentationItem: 
        """
        None
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
class TopoDSToStep_Tool():
    """
    This Tool Class provides Information to build a ProSTEP Shape model from a Cas.Cad BRep.
    """
    def Bind(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> None: 
        """
        None
        """
    def CurrentEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def CurrentFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def CurrentShell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        None
        """
    def CurrentVertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def CurrentWire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        None
        """
    def Faceted(self) -> bool: 
        """
        None
        """
    def Find(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.StepShape.StepShape_TopologicalRepresentationItem: 
        """
        None
        """
    def Init(self,M : Any,FacetedContext : bool) -> None: 
        """
        None
        """
    def IsBound(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def Lowest3DTolerance(self) -> float: 
        """
        None
        """
    def Map(self) -> Any: 
        """
        None
        """
    def PCurveMode(self) -> int: 
        """
        Returns mode for writing pcurves (initialized by parameter write.surfacecurve.mode)
        """
    def SetCurrentEdge(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def SetCurrentFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def SetCurrentShell(self,S : OCP.TopoDS.TopoDS_Shell) -> None: 
        """
        None
        """
    def SetCurrentVertex(self,V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None
        """
    def SetCurrentWire(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        None
        """
    def SetSurfaceReversed(self,B : bool) -> None: 
        """
        None
        """
    def SurfaceReversed(self) -> bool: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,M : Any,FacetedContext : bool) -> None: ...
    pass
class TopoDSToStep_WireframeBuilder(TopoDSToStep_Root):
    """
    This builder Class provides services to build a ProSTEP Wireframemodel from a Cas.Cad BRep.
    """
    def Error(self) -> TopoDSToStep_BuilderError: 
        """
        None
        """
    def GetTrimmedCurveFromEdge(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,M : Any,L : OCP.TColStd.TColStd_HSequenceOfTransient) -> bool: 
        """
        Extraction of Trimmed Curves from TopoDS_Edge for the Creation of a GeometricallyBoundedWireframeRepresentation
        """
    def GetTrimmedCurveFromFace(self,F : OCP.TopoDS.TopoDS_Face,M : Any,L : OCP.TColStd.TColStd_HSequenceOfTransient) -> bool: 
        """
        Extraction of Trimmed Curves from TopoDS_Face for the Creation of a GeometricallyBoundedWireframeRepresentation
        """
    def GetTrimmedCurveFromShape(self,S : OCP.TopoDS.TopoDS_Shape,M : Any,L : OCP.TColStd.TColStd_HSequenceOfTransient) -> bool: 
        """
        Extraction of Trimmed Curves from any TopoDS_Shape for the Creation of a GeometricallyBoundedWireframeRepresentation
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Value(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        None
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,T : TopoDSToStep_Tool,FP : OCP.Transfer.Transfer_FinderProcess) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @property
    def Tolerance(self) -> float:
        """
        :type: float
        """
    @Tolerance.setter
    def Tolerance(self, arg1: float) -> None:
        pass
    pass
TopoDSToStep_BuilderDone: OCP.TopoDSToStep.TopoDSToStep_BuilderError # value = <TopoDSToStep_BuilderError.TopoDSToStep_BuilderDone: 0>
TopoDSToStep_BuilderOther: OCP.TopoDSToStep.TopoDSToStep_BuilderError # value = <TopoDSToStep_BuilderError.TopoDSToStep_BuilderOther: 2>
TopoDSToStep_EdgeDone: OCP.TopoDSToStep.TopoDSToStep_MakeEdgeError # value = <TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeDone: 0>
TopoDSToStep_EdgeOther: OCP.TopoDSToStep.TopoDSToStep_MakeEdgeError # value = <TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeOther: 2>
TopoDSToStep_FaceDone: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_FaceDone: 0>
TopoDSToStep_FaceOther: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_FaceOther: 4>
TopoDSToStep_FacetedDone: OCP.TopoDSToStep.TopoDSToStep_FacetedError # value = <TopoDSToStep_FacetedError.TopoDSToStep_FacetedDone: 0>
TopoDSToStep_InfiniteFace: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_InfiniteFace: 1>
TopoDSToStep_NoFaceMapped: OCP.TopoDSToStep.TopoDSToStep_BuilderError # value = <TopoDSToStep_BuilderError.TopoDSToStep_NoFaceMapped: 1>
TopoDSToStep_NoWireMapped: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_NoWireMapped: 3>
TopoDSToStep_NonManifoldEdge: OCP.TopoDSToStep.TopoDSToStep_MakeEdgeError # value = <TopoDSToStep_MakeEdgeError.TopoDSToStep_NonManifoldEdge: 1>
TopoDSToStep_NonManifoldFace: OCP.TopoDSToStep.TopoDSToStep_MakeFaceError # value = <TopoDSToStep_MakeFaceError.TopoDSToStep_NonManifoldFace: 2>
TopoDSToStep_NonManifoldWire: OCP.TopoDSToStep.TopoDSToStep_MakeWireError # value = <TopoDSToStep_MakeWireError.TopoDSToStep_NonManifoldWire: 1>
TopoDSToStep_PCurveNotLinear: OCP.TopoDSToStep.TopoDSToStep_FacetedError # value = <TopoDSToStep_FacetedError.TopoDSToStep_PCurveNotLinear: 2>
TopoDSToStep_SurfaceNotPlane: OCP.TopoDSToStep.TopoDSToStep_FacetedError # value = <TopoDSToStep_FacetedError.TopoDSToStep_SurfaceNotPlane: 1>
TopoDSToStep_VertexDone: OCP.TopoDSToStep.TopoDSToStep_MakeVertexError # value = <TopoDSToStep_MakeVertexError.TopoDSToStep_VertexDone: 0>
TopoDSToStep_VertexOther: OCP.TopoDSToStep.TopoDSToStep_MakeVertexError # value = <TopoDSToStep_MakeVertexError.TopoDSToStep_VertexOther: 1>
TopoDSToStep_WireDone: OCP.TopoDSToStep.TopoDSToStep_MakeWireError # value = <TopoDSToStep_MakeWireError.TopoDSToStep_WireDone: 0>
TopoDSToStep_WireOther: OCP.TopoDSToStep.TopoDSToStep_MakeWireError # value = <TopoDSToStep_MakeWireError.TopoDSToStep_WireOther: 2>
