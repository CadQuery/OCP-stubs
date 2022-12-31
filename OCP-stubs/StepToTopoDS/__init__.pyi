import OCP.StepToTopoDS
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.TopoDS
import OCP.TCollection
import OCP.NCollection
import OCP.gp
import OCP.Geom2d
import OCP.StepVisual
import io
import OCP.StepGeom
import OCP.Transfer
import OCP.StepRepr
import OCP.StepShape
__all__  = [
"StepToTopoDS",
"StepToTopoDS_Root",
"StepToTopoDS_BuilderError",
"StepToTopoDS_CartesianPointHasher",
"StepToTopoDS_DataMapOfRI",
"StepToTopoDS_DataMapOfRINames",
"StepToTopoDS_DataMapOfTRI",
"StepToTopoDS_GeometricTool",
"StepToTopoDS_GeometricToolError",
"StepToTopoDS_MakeTransformed",
"StepToTopoDS_NMTool",
"StepToTopoDS_PointEdgeMap",
"StepToTopoDS_PointPair",
"StepToTopoDS_PointPairHasher",
"StepToTopoDS_PointVertexMap",
"StepToTopoDS_Builder",
"StepToTopoDS_Tool",
"StepToTopoDS_TranslateCompositeCurve",
"StepToTopoDS_TranslateCurveBoundedSurface",
"StepToTopoDS_TranslateEdge",
"StepToTopoDS_TranslateEdgeError",
"StepToTopoDS_TranslateEdgeLoop",
"StepToTopoDS_TranslateEdgeLoopError",
"StepToTopoDS_TranslateFace",
"StepToTopoDS_TranslateFaceError",
"StepToTopoDS_TranslatePolyLoop",
"StepToTopoDS_TranslatePolyLoopError",
"StepToTopoDS_TranslateShell",
"StepToTopoDS_TranslateShellError",
"StepToTopoDS_TranslateSolid",
"StepToTopoDS_TranslateSolidError",
"StepToTopoDS_TranslateVertex",
"StepToTopoDS_TranslateVertexError",
"StepToTopoDS_TranslateVertexLoop",
"StepToTopoDS_TranslateVertexLoopError",
"StepToTopoDS_BuilderDone",
"StepToTopoDS_BuilderOther",
"StepToTopoDS_GeometricToolDone",
"StepToTopoDS_GeometricToolHasNoPCurve",
"StepToTopoDS_GeometricToolIsDegenerated",
"StepToTopoDS_GeometricToolNoProjectiOnCurve",
"StepToTopoDS_GeometricToolOther",
"StepToTopoDS_GeometricToolWrong3dParameters",
"StepToTopoDS_TranslateEdgeDone",
"StepToTopoDS_TranslateEdgeLoopDone",
"StepToTopoDS_TranslateEdgeLoopOther",
"StepToTopoDS_TranslateEdgeOther",
"StepToTopoDS_TranslateFaceDone",
"StepToTopoDS_TranslateFaceOther",
"StepToTopoDS_TranslatePolyLoopDone",
"StepToTopoDS_TranslatePolyLoopOther",
"StepToTopoDS_TranslateShellDone",
"StepToTopoDS_TranslateShellOther",
"StepToTopoDS_TranslateSolidDone",
"StepToTopoDS_TranslateSolidOther",
"StepToTopoDS_TranslateVertexDone",
"StepToTopoDS_TranslateVertexLoopDone",
"StepToTopoDS_TranslateVertexLoopOther",
"StepToTopoDS_TranslateVertexOther"
]
class StepToTopoDS():
    """
    This package implements the mapping between AP214 Shape representation and CAS.CAD Shape Representation. The source schema is Part42 (which is included in AP214)
    """
    @staticmethod
    def DecodeBuilderError_s(Error : StepToTopoDS_BuilderError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def DecodeEdgeError_s(Error : StepToTopoDS_TranslateEdgeError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def DecodeFaceError_s(Error : StepToTopoDS_TranslateFaceError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def DecodeGeometricToolError_s(Error : StepToTopoDS_GeometricToolError) -> str: 
        """
        None
        """
    @staticmethod
    def DecodePolyLoopError_s(Error : StepToTopoDS_TranslatePolyLoopError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def DecodeShellError_s(Error : StepToTopoDS_TranslateShellError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def DecodeVertexError_s(Error : StepToTopoDS_TranslateVertexError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def DecodeVertexLoopError_s(Error : StepToTopoDS_TranslateVertexLoopError) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_Root():
    """
    This class implements the common services for all classes of StepToTopoDS which report error and sets and returns precision.
    """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    pass
class StepToTopoDS_BuilderError():
    """
    None

    Members:

      StepToTopoDS_BuilderDone

      StepToTopoDS_BuilderOther
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
    StepToTopoDS_BuilderDone: OCP.StepToTopoDS.StepToTopoDS_BuilderError # value = <StepToTopoDS_BuilderError.StepToTopoDS_BuilderDone: 0>
    StepToTopoDS_BuilderOther: OCP.StepToTopoDS.StepToTopoDS_BuilderError # value = <StepToTopoDS_BuilderError.StepToTopoDS_BuilderOther: 1>
    __entries: dict # value = {'StepToTopoDS_BuilderDone': (<StepToTopoDS_BuilderError.StepToTopoDS_BuilderDone: 0>, None), 'StepToTopoDS_BuilderOther': (<StepToTopoDS_BuilderError.StepToTopoDS_BuilderOther: 1>, None)}
    __members__: dict # value = {'StepToTopoDS_BuilderDone': <StepToTopoDS_BuilderError.StepToTopoDS_BuilderDone: 0>, 'StepToTopoDS_BuilderOther': <StepToTopoDS_BuilderError.StepToTopoDS_BuilderOther: 1>}
    pass
class StepToTopoDS_CartesianPointHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(theCartesianPoint : OCP.StepGeom.StepGeom_CartesianPoint,theUpperBound : int) -> int: 
        """
        Computes a hash code for the cartesian point, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(K1 : OCP.StepGeom.StepGeom_CartesianPoint,K2 : OCP.StepGeom.StepGeom_CartesianPoint) -> bool: 
        """
        Returns True when the two CartesianPoint are the same
        """
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_DataMapOfRI(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : StepToTopoDS_DataMapOfRI) -> StepToTopoDS_DataMapOfRI: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.StepRepr.StepRepr_RepresentationItem,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.StepRepr.StepRepr_RepresentationItem,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.StepRepr.StepRepr_RepresentationItem) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.StepRepr.StepRepr_RepresentationItem) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Exchange(self,theOther : StepToTopoDS_DataMapOfRI) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.StepRepr.StepRepr_RepresentationItem,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.StepRepr.StepRepr_RepresentationItem) -> OCP.TopoDS.TopoDS_Shape: ...
    def IsBound(self,theKey : OCP.StepRepr.StepRepr_RepresentationItem) -> bool: 
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
    def Seek(self,theKey : OCP.StepRepr.StepRepr_RepresentationItem) -> OCP.TopoDS.TopoDS_Shape: 
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
    def UnBind(self,theKey : OCP.StepRepr.StepRepr_RepresentationItem) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepToTopoDS_DataMapOfRI) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepToTopoDS_DataMapOfRINames(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : StepToTopoDS_DataMapOfRINames) -> StepToTopoDS_DataMapOfRINames: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TCollection.TCollection_AsciiString,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Exchange(self,theOther : StepToTopoDS_DataMapOfRINames) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TopoDS.TopoDS_Shape: ...
    def IsBound(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
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
    def Seek(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OCP.TopoDS.TopoDS_Shape: 
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
    def UnBind(self,theKey : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : StepToTopoDS_DataMapOfRINames) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepToTopoDS_DataMapOfTRI(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : StepToTopoDS_DataMapOfTRI) -> StepToTopoDS_DataMapOfTRI: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.StepShape.StepShape_TopologicalRepresentationItem,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.StepShape.StepShape_TopologicalRepresentationItem,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Exchange(self,theOther : StepToTopoDS_DataMapOfTRI) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.StepShape.StepShape_TopologicalRepresentationItem,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> OCP.TopoDS.TopoDS_Shape: ...
    def IsBound(self,theKey : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> bool: 
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
    def Seek(self,theKey : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> OCP.TopoDS.TopoDS_Shape: 
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
    def UnBind(self,theKey : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : StepToTopoDS_DataMapOfTRI) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepToTopoDS_GeometricTool():
    """
    This class contains some algorithmic services specific to the mapping STEP to CAS.CADE
    """
    @staticmethod
    def IsLikeSeam_s(SC : OCP.StepGeom.StepGeom_SurfaceCurve,S : OCP.StepGeom.StepGeom_Surface,E : OCP.StepShape.StepShape_Edge,EL : OCP.StepShape.StepShape_EdgeLoop) -> bool: 
        """
        None
        """
    @staticmethod
    def IsSeamCurve_s(SC : OCP.StepGeom.StepGeom_SurfaceCurve,S : OCP.StepGeom.StepGeom_Surface,E : OCP.StepShape.StepShape_Edge,EL : OCP.StepShape.StepShape_EdgeLoop) -> bool: 
        """
        None
        """
    @staticmethod
    def PCurve_s(SC : OCP.StepGeom.StepGeom_SurfaceCurve,S : OCP.StepGeom.StepGeom_Surface,PC : OCP.StepGeom.StepGeom_Pcurve,last : int=0) -> int: 
        """
        None
        """
    @staticmethod
    def UpdateParam3d_s(C : OCP.Geom.Geom_Curve,w1 : float,w2 : float,preci : float) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_GeometricToolError():
    """
    None

    Members:

      StepToTopoDS_GeometricToolDone

      StepToTopoDS_GeometricToolIsDegenerated

      StepToTopoDS_GeometricToolHasNoPCurve

      StepToTopoDS_GeometricToolWrong3dParameters

      StepToTopoDS_GeometricToolNoProjectiOnCurve

      StepToTopoDS_GeometricToolOther
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
    StepToTopoDS_GeometricToolDone: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolDone: 0>
    StepToTopoDS_GeometricToolHasNoPCurve: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolHasNoPCurve: 2>
    StepToTopoDS_GeometricToolIsDegenerated: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolIsDegenerated: 1>
    StepToTopoDS_GeometricToolNoProjectiOnCurve: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolNoProjectiOnCurve: 4>
    StepToTopoDS_GeometricToolOther: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolOther: 5>
    StepToTopoDS_GeometricToolWrong3dParameters: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolWrong3dParameters: 3>
    __entries: dict # value = {'StepToTopoDS_GeometricToolDone': (<StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolDone: 0>, None), 'StepToTopoDS_GeometricToolIsDegenerated': (<StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolIsDegenerated: 1>, None), 'StepToTopoDS_GeometricToolHasNoPCurve': (<StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolHasNoPCurve: 2>, None), 'StepToTopoDS_GeometricToolWrong3dParameters': (<StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolWrong3dParameters: 3>, None), 'StepToTopoDS_GeometricToolNoProjectiOnCurve': (<StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolNoProjectiOnCurve: 4>, None), 'StepToTopoDS_GeometricToolOther': (<StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolOther: 5>, None)}
    __members__: dict # value = {'StepToTopoDS_GeometricToolDone': <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolDone: 0>, 'StepToTopoDS_GeometricToolIsDegenerated': <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolIsDegenerated: 1>, 'StepToTopoDS_GeometricToolHasNoPCurve': <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolHasNoPCurve: 2>, 'StepToTopoDS_GeometricToolWrong3dParameters': <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolWrong3dParameters: 3>, 'StepToTopoDS_GeometricToolNoProjectiOnCurve': <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolNoProjectiOnCurve: 4>, 'StepToTopoDS_GeometricToolOther': <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolOther: 5>}
    pass
class StepToTopoDS_MakeTransformed(StepToTopoDS_Root):
    """
    Produces instances by Transformation of a basic item
    """
    @overload
    def Compute(self,Operator : OCP.StepGeom.StepGeom_CartesianTransformationOperator3d) -> bool: 
        """
        Computes a transformation to pass from an Origin placement to a Target placement. Returns True when done If not done, the transformation will by Identity

        Computes a transformation defined by an operator 3D
        """
    @overload
    def Compute(self,Origin : OCP.StepGeom.StepGeom_Axis2Placement3d,Target : OCP.StepGeom.StepGeom_Axis2Placement3d) -> bool: ...
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Transform(self,shape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Applies the computed transformation to a shape Returns False if the transformation is Identity
        """
    def Transformation(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the computed transformation (Identity if not yet or if failed)
        """
    def TranslateMappedItem(self,mapit : OCP.StepRepr.StepRepr_MappedItem,TP : OCP.Transfer.Transfer_TransientProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Translates a MappedItem. More precisely A MappedItem has a MappingSource and a MappingTarget MappingSource has a MappedRepresentation and a MappingOrigin MappedRepresentation is the basic item to be instanced MappingOrigin is the starting placement MappingTarget is the final placement
        """
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_NMTool():
    """
    Provides data to process non-manifold topology when reading from STEP.
    """
    @overload
    def Bind(self,RI : OCP.StepRepr.StepRepr_RepresentationItem,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def Bind(self,RIName : OCP.TCollection.TCollection_AsciiString,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def CleanUp(self) -> None: 
        """
        None
        """
    @overload
    def Find(self,RIName : OCP.TCollection.TCollection_AsciiString) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    @overload
    def Find(self,RI : OCP.StepRepr.StepRepr_RepresentationItem) -> OCP.TopoDS.TopoDS_Shape: ...
    def Init(self,MapOfRI : StepToTopoDS_DataMapOfRI,MapOfRINames : StepToTopoDS_DataMapOfRINames) -> None: 
        """
        None
        """
    def IsActive(self) -> bool: 
        """
        None
        """
    @overload
    def IsBound(self,RIName : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        None

        None
        """
    @overload
    def IsBound(self,RI : OCP.StepRepr.StepRepr_RepresentationItem) -> bool: ...
    def IsIDEASCase(self) -> bool: 
        """
        None
        """
    def IsPureNMShell(self,Shell : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsSuspectedAsClosing(self,BaseShell : OCP.TopoDS.TopoDS_Shape,SuspectedShell : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def RegisterNMEdge(self,Edge : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def SetActive(self,isActive : bool) -> None: 
        """
        None
        """
    def SetIDEASCase(self,IDEASCase : bool) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,MapOfRI : StepToTopoDS_DataMapOfRI,MapOfRINames : StepToTopoDS_DataMapOfRINames) -> None: ...
    pass
class StepToTopoDS_PointEdgeMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : StepToTopoDS_PointEdgeMap) -> StepToTopoDS_PointEdgeMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : StepToTopoDS_PointPair,theItem : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : StepToTopoDS_PointPair,theItem : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : StepToTopoDS_PointPair) -> OCP.TopoDS.TopoDS_Edge: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : StepToTopoDS_PointPair) -> OCP.TopoDS.TopoDS_Edge: 
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
    def Exchange(self,theOther : StepToTopoDS_PointEdgeMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : StepToTopoDS_PointPair) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : StepToTopoDS_PointPair,theValue : OCP.TopoDS.TopoDS_Edge) -> bool: ...
    def IsBound(self,theKey : StepToTopoDS_PointPair) -> bool: 
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
    def Seek(self,theKey : StepToTopoDS_PointPair) -> OCP.TopoDS.TopoDS_Edge: 
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
    def UnBind(self,theKey : StepToTopoDS_PointPair) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : StepToTopoDS_PointEdgeMap) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepToTopoDS_PointPair():
    """
    Stores a pair of Points from step
    """
    def __init__(self,P1 : OCP.StepGeom.StepGeom_CartesianPoint,P2 : OCP.StepGeom.StepGeom_CartesianPoint) -> None: ...
    pass
class StepToTopoDS_PointPairHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(thePointPair : StepToTopoDS_PointPair,theUpperBound : int) -> int: 
        """
        Computes a hash code for the point pair, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(K1 : StepToTopoDS_PointPair,K2 : StepToTopoDS_PointPair) -> bool: 
        """
        Returns True when the two PointPair are the same
        """
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_PointVertexMap(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : StepToTopoDS_PointVertexMap) -> StepToTopoDS_PointVertexMap: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.StepGeom.StepGeom_CartesianPoint,theItem : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.StepGeom.StepGeom_CartesianPoint,theItem : OCP.TopoDS.TopoDS_Vertex) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.StepGeom.StepGeom_CartesianPoint) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.StepGeom.StepGeom_CartesianPoint) -> OCP.TopoDS.TopoDS_Vertex: 
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
    def Exchange(self,theOther : StepToTopoDS_PointVertexMap) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.StepGeom.StepGeom_CartesianPoint,theValue : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.StepGeom.StepGeom_CartesianPoint) -> OCP.TopoDS.TopoDS_Vertex: ...
    def IsBound(self,theKey : OCP.StepGeom.StepGeom_CartesianPoint) -> bool: 
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
    def Seek(self,theKey : OCP.StepGeom.StepGeom_CartesianPoint) -> OCP.TopoDS.TopoDS_Vertex: 
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
    def UnBind(self,theKey : OCP.StepGeom.StepGeom_CartesianPoint) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : StepToTopoDS_PointVertexMap) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepToTopoDS_Builder(StepToTopoDS_Root):
    """
    None
    """
    def Error(self) -> StepToTopoDS_BuilderError: 
        """
        None
        """
    @overload
    def Init(self,S : OCP.StepShape.StepShape_GeometricSet,TP : OCP.Transfer.Transfer_TransientProcess,RA : OCP.Transfer.Transfer_ActorOfTransientProcess=None,isManifold : bool=False,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @overload
    def Init(self,S : OCP.StepShape.StepShape_FacetedBrepAndBrepWithVoids,TP : OCP.Transfer.Transfer_TransientProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def Init(self,theTSo : OCP.StepVisual.StepVisual_TessellatedSolid,theTP : OCP.Transfer.Transfer_TransientProcess,theReadTessellatedWhenNoBRepOnly : bool,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> Tuple[bool]: ...
    @overload
    def Init(self,S : OCP.StepShape.StepShape_ShellBasedSurfaceModel,TP : OCP.Transfer.Transfer_TransientProcess,NMTool : StepToTopoDS_NMTool,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def Init(self,S : OCP.StepShape.StepShape_BrepWithVoids,TP : OCP.Transfer.Transfer_TransientProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def Init(self,S : OCP.StepShape.StepShape_ManifoldSolidBrep,TP : OCP.Transfer.Transfer_TransientProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def Init(self,theTSh : OCP.StepVisual.StepVisual_TessellatedShell,theTP : OCP.Transfer.Transfer_TransientProcess,theReadTessellatedWhenNoBRepOnly : bool,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> Tuple[bool]: ...
    @overload
    def Init(self,S : OCP.StepShape.StepShape_EdgeBasedWireframeModel,TP : OCP.Transfer.Transfer_TransientProcess) -> None: ...
    @overload
    def Init(self,S : OCP.StepShape.StepShape_FacetedBrep,TP : OCP.Transfer.Transfer_TransientProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def Init(self,S : OCP.StepShape.StepShape_FaceBasedSurfaceModel,TP : OCP.Transfer.Transfer_TransientProcess) -> None: ...
    @overload
    def Init(self,theTF : OCP.StepVisual.StepVisual_TessellatedFace,theTP : OCP.Transfer.Transfer_TransientProcess,theReadTessellatedWhenNoBRepOnly : bool) -> Tuple[bool]: ...
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_Tool():
    """
    This Tool Class provides Information to build a Cas.Cad BRep from a ProSTEP Shape model.
    """
    @overload
    def AddContinuity(self,GeomCur2d : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None

        None
        """
    @overload
    def AddContinuity(self,GeomSurf : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def AddContinuity(self,GeomCurve : OCP.Geom.Geom_Curve) -> None: ...
    def Bind(self,TRI : OCP.StepShape.StepShape_TopologicalRepresentationItem,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def BindEdge(self,PP : StepToTopoDS_PointPair,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def BindVertex(self,P : OCP.StepGeom.StepGeom_CartesianPoint,V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None
        """
    def C0Cur2(self) -> int: 
        """
        None
        """
    def C0Cur3(self) -> int: 
        """
        None
        """
    def C0Surf(self) -> int: 
        """
        None
        """
    def C1Cur2(self) -> int: 
        """
        None
        """
    def C1Cur3(self) -> int: 
        """
        None
        """
    def C1Surf(self) -> int: 
        """
        None
        """
    def C2Cur2(self) -> int: 
        """
        None
        """
    def C2Cur3(self) -> int: 
        """
        None
        """
    def C2Surf(self) -> int: 
        """
        None
        """
    def ClearEdgeMap(self) -> None: 
        """
        None
        """
    def ClearVertexMap(self) -> None: 
        """
        None
        """
    @overload
    def ComputePCurve(self) -> bool: 
        """
        None

        None
        """
    @overload
    def ComputePCurve(self,B : bool) -> None: ...
    def Find(self,TRI : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def FindEdge(self,PP : StepToTopoDS_PointPair) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def FindVertex(self,P : OCP.StepGeom.StepGeom_CartesianPoint) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def Init(self,Map : StepToTopoDS_DataMapOfTRI,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        None
        """
    def IsBound(self,TRI : OCP.StepShape.StepShape_TopologicalRepresentationItem) -> bool: 
        """
        None
        """
    def IsEdgeBound(self,PP : StepToTopoDS_PointPair) -> bool: 
        """
        None
        """
    def IsVertexBound(self,PG : OCP.StepGeom.StepGeom_CartesianPoint) -> bool: 
        """
        None
        """
    def TransientProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        None
        """
    @overload
    def __init__(self,Map : StepToTopoDS_DataMapOfTRI,TP : OCP.Transfer.Transfer_TransientProcess) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_TranslateCompositeCurve(StepToTopoDS_Root):
    """
    Translate STEP entity composite_curve to TopoDS_Wire If surface is given, the curve is assumed to lie on that surface and in case if any segment of it is a curve_on_surface, the pcurve for that segment will be taken. Note: a segment of composite_curve may be itself composite_curve. Only one-level protection against cyclic references is implemented.
    """
    @overload
    def Init(self,CC : OCP.StepGeom.StepGeom_CompositeCurve,TP : OCP.Transfer.Transfer_TransientProcess) -> bool: 
        """
        Translates standalone composite_curve

        Translates composite_curve lying on surface
        """
    @overload
    def Init(self,CC : OCP.StepGeom.StepGeom_CompositeCurve,TP : OCP.Transfer.Transfer_TransientProcess,S : OCP.StepGeom.StepGeom_Surface,Surf : OCP.Geom.Geom_Surface) -> bool: ...
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def IsInfiniteSegment(self) -> bool: 
        """
        Returns True if composite_curve contains a segment with infinite parameters.

        Returns True if composite_curve contains a segment with infinite parameters.
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns result of last translation or null wire if failed.
        """
    @overload
    def __init__(self,CC : OCP.StepGeom.StepGeom_CompositeCurve,TP : OCP.Transfer.Transfer_TransientProcess) -> None: ...
    @overload
    def __init__(self,CC : OCP.StepGeom.StepGeom_CompositeCurve,TP : OCP.Transfer.Transfer_TransientProcess,S : OCP.StepGeom.StepGeom_Surface,Surf : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_TranslateCurveBoundedSurface(StepToTopoDS_Root):
    """
    Translate curve_bounded_surface into TopoDS_Face
    """
    def Init(self,CBS : OCP.StepGeom.StepGeom_CurveBoundedSurface,TP : OCP.Transfer.Transfer_TransientProcess) -> bool: 
        """
        Translate surface
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns result of last translation or null wire if failed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,CBS : OCP.StepGeom.StepGeom_CurveBoundedSurface,TP : OCP.Transfer.Transfer_TransientProcess) -> None: ...
    pass
class StepToTopoDS_TranslateEdge(StepToTopoDS_Root):
    """
    None
    """
    def Error(self) -> StepToTopoDS_TranslateEdgeError: 
        """
        None
        """
    def Init(self,E : OCP.StepShape.StepShape_Edge,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MakeFromCurve3D(self,C3D : OCP.StepGeom.StepGeom_Curve,EC : OCP.StepShape.StepShape_EdgeCurve,Vend : OCP.StepShape.StepShape_Vertex,preci : float,E : OCP.TopoDS.TopoDS_Edge,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,T : StepToTopoDS_Tool) -> None: 
        """
        Warning! C3D is assumed to be a Curve 3D ... other cases to checked before calling this
        """
    def MakePCurve(self,PCU : OCP.StepGeom.StepGeom_Pcurve,ConvSurf : OCP.Geom.Geom_Surface) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.StepShape.StepShape_Edge,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: ...
    pass
class StepToTopoDS_TranslateEdgeError():
    """
    None

    Members:

      StepToTopoDS_TranslateEdgeDone

      StepToTopoDS_TranslateEdgeOther
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
    StepToTopoDS_TranslateEdgeDone: OCP.StepToTopoDS.StepToTopoDS_TranslateEdgeError # value = <StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeDone: 0>
    StepToTopoDS_TranslateEdgeOther: OCP.StepToTopoDS.StepToTopoDS_TranslateEdgeError # value = <StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeOther: 1>
    __entries: dict # value = {'StepToTopoDS_TranslateEdgeDone': (<StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeDone: 0>, None), 'StepToTopoDS_TranslateEdgeOther': (<StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeOther: 1>, None)}
    __members__: dict # value = {'StepToTopoDS_TranslateEdgeDone': <StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeDone: 0>, 'StepToTopoDS_TranslateEdgeOther': <StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeOther: 1>}
    pass
class StepToTopoDS_TranslateEdgeLoop(StepToTopoDS_Root):
    """
    None
    """
    def Error(self) -> StepToTopoDS_TranslateEdgeLoopError: 
        """
        None
        """
    def Init(self,FB : OCP.StepShape.StepShape_FaceBound,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,SS : OCP.StepGeom.StepGeom_Surface,ss : bool,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self,FB : OCP.StepShape.StepShape_FaceBound,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,SS : OCP.StepGeom.StepGeom_Surface,ss : bool,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_TranslateEdgeLoopError():
    """
    None

    Members:

      StepToTopoDS_TranslateEdgeLoopDone

      StepToTopoDS_TranslateEdgeLoopOther
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
    StepToTopoDS_TranslateEdgeLoopDone: OCP.StepToTopoDS.StepToTopoDS_TranslateEdgeLoopError # value = <StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopDone: 0>
    StepToTopoDS_TranslateEdgeLoopOther: OCP.StepToTopoDS.StepToTopoDS_TranslateEdgeLoopError # value = <StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopOther: 1>
    __entries: dict # value = {'StepToTopoDS_TranslateEdgeLoopDone': (<StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopDone: 0>, None), 'StepToTopoDS_TranslateEdgeLoopOther': (<StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopOther: 1>, None)}
    __members__: dict # value = {'StepToTopoDS_TranslateEdgeLoopDone': <StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopDone: 0>, 'StepToTopoDS_TranslateEdgeLoopOther': <StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopOther: 1>}
    pass
class StepToTopoDS_TranslateFace(StepToTopoDS_Root):
    """
    None
    """
    def Error(self) -> StepToTopoDS_TranslateFaceError: 
        """
        None
        """
    @overload
    def Init(self,theTF : OCP.StepVisual.StepVisual_TessellatedFace,theTool : StepToTopoDS_Tool,theNMTool : StepToTopoDS_NMTool,theReadTessellatedWhenNoBRepOnly : bool) -> Tuple[bool]: 
        """
        None

        None
        """
    @overload
    def Init(self,FS : OCP.StepShape.StepShape_FaceSurface,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: ...
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theTF : OCP.StepVisual.StepVisual_TessellatedFace,theTool : StepToTopoDS_Tool,theNMTool : StepToTopoDS_NMTool,theReadTessellatedWhenNoBRepOnly : bool,theHasGeom : bool) -> None: ...
    @overload
    def __init__(self,FS : OCP.StepShape.StepShape_FaceSurface,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: ...
    pass
class StepToTopoDS_TranslateFaceError():
    """
    None

    Members:

      StepToTopoDS_TranslateFaceDone

      StepToTopoDS_TranslateFaceOther
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
    StepToTopoDS_TranslateFaceDone: OCP.StepToTopoDS.StepToTopoDS_TranslateFaceError # value = <StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceDone: 0>
    StepToTopoDS_TranslateFaceOther: OCP.StepToTopoDS.StepToTopoDS_TranslateFaceError # value = <StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceOther: 1>
    __entries: dict # value = {'StepToTopoDS_TranslateFaceDone': (<StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceDone: 0>, None), 'StepToTopoDS_TranslateFaceOther': (<StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceOther: 1>, None)}
    __members__: dict # value = {'StepToTopoDS_TranslateFaceDone': <StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceDone: 0>, 'StepToTopoDS_TranslateFaceOther': <StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceOther: 1>}
    pass
class StepToTopoDS_TranslatePolyLoop(StepToTopoDS_Root):
    """
    None
    """
    def Error(self) -> StepToTopoDS_TranslatePolyLoopError: 
        """
        None
        """
    def Init(self,PL : OCP.StepShape.StepShape_PolyLoop,T : StepToTopoDS_Tool,S : OCP.Geom.Geom_Surface,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,PL : OCP.StepShape.StepShape_PolyLoop,T : StepToTopoDS_Tool,S : OCP.Geom.Geom_Surface,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
class StepToTopoDS_TranslatePolyLoopError():
    """
    None

    Members:

      StepToTopoDS_TranslatePolyLoopDone

      StepToTopoDS_TranslatePolyLoopOther
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
    StepToTopoDS_TranslatePolyLoopDone: OCP.StepToTopoDS.StepToTopoDS_TranslatePolyLoopError # value = <StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopDone: 0>
    StepToTopoDS_TranslatePolyLoopOther: OCP.StepToTopoDS.StepToTopoDS_TranslatePolyLoopError # value = <StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopOther: 1>
    __entries: dict # value = {'StepToTopoDS_TranslatePolyLoopDone': (<StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopDone: 0>, None), 'StepToTopoDS_TranslatePolyLoopOther': (<StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopOther: 1>, None)}
    __members__: dict # value = {'StepToTopoDS_TranslatePolyLoopDone': <StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopDone: 0>, 'StepToTopoDS_TranslatePolyLoopOther': <StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopOther: 1>}
    pass
class StepToTopoDS_TranslateShell(StepToTopoDS_Root):
    """
    None
    """
    def Error(self) -> StepToTopoDS_TranslateShellError: 
        """
        None
        """
    @overload
    def Init(self,theTSh : OCP.StepVisual.StepVisual_TessellatedShell,theTool : StepToTopoDS_Tool,theNMTool : StepToTopoDS_NMTool,theReadTessellatedWhenNoBRepOnly : bool,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> Tuple[bool]: 
        """
        None

        None
        """
    @overload
    def Init(self,CFS : OCP.StepShape.StepShape_ConnectedFaceSet,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_TranslateShellError():
    """
    None

    Members:

      StepToTopoDS_TranslateShellDone

      StepToTopoDS_TranslateShellOther
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
    StepToTopoDS_TranslateShellDone: OCP.StepToTopoDS.StepToTopoDS_TranslateShellError # value = <StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellDone: 0>
    StepToTopoDS_TranslateShellOther: OCP.StepToTopoDS.StepToTopoDS_TranslateShellError # value = <StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellOther: 1>
    __entries: dict # value = {'StepToTopoDS_TranslateShellDone': (<StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellDone: 0>, None), 'StepToTopoDS_TranslateShellOther': (<StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellOther: 1>, None)}
    __members__: dict # value = {'StepToTopoDS_TranslateShellDone': <StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellDone: 0>, 'StepToTopoDS_TranslateShellOther': <StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellOther: 1>}
    pass
class StepToTopoDS_TranslateSolid(StepToTopoDS_Root):
    """
    None
    """
    def Error(self) -> StepToTopoDS_TranslateSolidError: 
        """
        None
        """
    def Init(self,theTSo : OCP.StepVisual.StepVisual_TessellatedSolid,theTP : OCP.Transfer.Transfer_TransientProcess,theTool : StepToTopoDS_Tool,theNMTool : StepToTopoDS_NMTool,theReadTessellatedWhenNoBRepOnly : bool,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> Tuple[bool]: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_TranslateSolidError():
    """
    None

    Members:

      StepToTopoDS_TranslateSolidDone

      StepToTopoDS_TranslateSolidOther
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
    StepToTopoDS_TranslateSolidDone: OCP.StepToTopoDS.StepToTopoDS_TranslateSolidError # value = <StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidDone: 0>
    StepToTopoDS_TranslateSolidOther: OCP.StepToTopoDS.StepToTopoDS_TranslateSolidError # value = <StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidOther: 1>
    __entries: dict # value = {'StepToTopoDS_TranslateSolidDone': (<StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidDone: 0>, None), 'StepToTopoDS_TranslateSolidOther': (<StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidOther: 1>, None)}
    __members__: dict # value = {'StepToTopoDS_TranslateSolidDone': <StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidDone: 0>, 'StepToTopoDS_TranslateSolidOther': <StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidOther: 1>}
    pass
class StepToTopoDS_TranslateVertex(StepToTopoDS_Root):
    """
    None
    """
    def Error(self) -> StepToTopoDS_TranslateVertexError: 
        """
        None
        """
    def Init(self,V : OCP.StepShape.StepShape_Vertex,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,V : OCP.StepShape.StepShape_Vertex,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: ...
    pass
class StepToTopoDS_TranslateVertexError():
    """
    None

    Members:

      StepToTopoDS_TranslateVertexDone

      StepToTopoDS_TranslateVertexOther
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
    StepToTopoDS_TranslateVertexDone: OCP.StepToTopoDS.StepToTopoDS_TranslateVertexError # value = <StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexDone: 0>
    StepToTopoDS_TranslateVertexOther: OCP.StepToTopoDS.StepToTopoDS_TranslateVertexError # value = <StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexOther: 1>
    __entries: dict # value = {'StepToTopoDS_TranslateVertexDone': (<StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexDone: 0>, None), 'StepToTopoDS_TranslateVertexOther': (<StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexOther: 1>, None)}
    __members__: dict # value = {'StepToTopoDS_TranslateVertexDone': <StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexDone: 0>, 'StepToTopoDS_TranslateVertexOther': <StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexOther: 1>}
    pass
class StepToTopoDS_TranslateVertexLoop(StepToTopoDS_Root):
    """
    None
    """
    def Error(self) -> StepToTopoDS_TranslateVertexLoopError: 
        """
        None
        """
    def Init(self,VL : OCP.StepShape.StepShape_VertexLoop,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None

        None
        """
    def MaxTol(self) -> float: 
        """
        Returns the value of "MaxTol"

        Returns the value of "MaxTol"
        """
    def Precision(self) -> float: 
        """
        Returns the value of "MyPrecision"

        Returns the value of "MyPrecision"
        """
    def SetMaxTol(self,maxpreci : float) -> None: 
        """
        Sets the value of MaxTol

        Sets the value of MaxTol
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the value of "MyPrecision"

        Sets the value of "MyPrecision"
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self,VL : OCP.StepShape.StepShape_VertexLoop,T : StepToTopoDS_Tool,NMTool : StepToTopoDS_NMTool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class StepToTopoDS_TranslateVertexLoopError():
    """
    None

    Members:

      StepToTopoDS_TranslateVertexLoopDone

      StepToTopoDS_TranslateVertexLoopOther
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
    StepToTopoDS_TranslateVertexLoopDone: OCP.StepToTopoDS.StepToTopoDS_TranslateVertexLoopError # value = <StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopDone: 0>
    StepToTopoDS_TranslateVertexLoopOther: OCP.StepToTopoDS.StepToTopoDS_TranslateVertexLoopError # value = <StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopOther: 1>
    __entries: dict # value = {'StepToTopoDS_TranslateVertexLoopDone': (<StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopDone: 0>, None), 'StepToTopoDS_TranslateVertexLoopOther': (<StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopOther: 1>, None)}
    __members__: dict # value = {'StepToTopoDS_TranslateVertexLoopDone': <StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopDone: 0>, 'StepToTopoDS_TranslateVertexLoopOther': <StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopOther: 1>}
    pass
StepToTopoDS_BuilderDone: OCP.StepToTopoDS.StepToTopoDS_BuilderError # value = <StepToTopoDS_BuilderError.StepToTopoDS_BuilderDone: 0>
StepToTopoDS_BuilderOther: OCP.StepToTopoDS.StepToTopoDS_BuilderError # value = <StepToTopoDS_BuilderError.StepToTopoDS_BuilderOther: 1>
StepToTopoDS_GeometricToolDone: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolDone: 0>
StepToTopoDS_GeometricToolHasNoPCurve: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolHasNoPCurve: 2>
StepToTopoDS_GeometricToolIsDegenerated: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolIsDegenerated: 1>
StepToTopoDS_GeometricToolNoProjectiOnCurve: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolNoProjectiOnCurve: 4>
StepToTopoDS_GeometricToolOther: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolOther: 5>
StepToTopoDS_GeometricToolWrong3dParameters: OCP.StepToTopoDS.StepToTopoDS_GeometricToolError # value = <StepToTopoDS_GeometricToolError.StepToTopoDS_GeometricToolWrong3dParameters: 3>
StepToTopoDS_TranslateEdgeDone: OCP.StepToTopoDS.StepToTopoDS_TranslateEdgeError # value = <StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeDone: 0>
StepToTopoDS_TranslateEdgeLoopDone: OCP.StepToTopoDS.StepToTopoDS_TranslateEdgeLoopError # value = <StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopDone: 0>
StepToTopoDS_TranslateEdgeLoopOther: OCP.StepToTopoDS.StepToTopoDS_TranslateEdgeLoopError # value = <StepToTopoDS_TranslateEdgeLoopError.StepToTopoDS_TranslateEdgeLoopOther: 1>
StepToTopoDS_TranslateEdgeOther: OCP.StepToTopoDS.StepToTopoDS_TranslateEdgeError # value = <StepToTopoDS_TranslateEdgeError.StepToTopoDS_TranslateEdgeOther: 1>
StepToTopoDS_TranslateFaceDone: OCP.StepToTopoDS.StepToTopoDS_TranslateFaceError # value = <StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceDone: 0>
StepToTopoDS_TranslateFaceOther: OCP.StepToTopoDS.StepToTopoDS_TranslateFaceError # value = <StepToTopoDS_TranslateFaceError.StepToTopoDS_TranslateFaceOther: 1>
StepToTopoDS_TranslatePolyLoopDone: OCP.StepToTopoDS.StepToTopoDS_TranslatePolyLoopError # value = <StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopDone: 0>
StepToTopoDS_TranslatePolyLoopOther: OCP.StepToTopoDS.StepToTopoDS_TranslatePolyLoopError # value = <StepToTopoDS_TranslatePolyLoopError.StepToTopoDS_TranslatePolyLoopOther: 1>
StepToTopoDS_TranslateShellDone: OCP.StepToTopoDS.StepToTopoDS_TranslateShellError # value = <StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellDone: 0>
StepToTopoDS_TranslateShellOther: OCP.StepToTopoDS.StepToTopoDS_TranslateShellError # value = <StepToTopoDS_TranslateShellError.StepToTopoDS_TranslateShellOther: 1>
StepToTopoDS_TranslateSolidDone: OCP.StepToTopoDS.StepToTopoDS_TranslateSolidError # value = <StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidDone: 0>
StepToTopoDS_TranslateSolidOther: OCP.StepToTopoDS.StepToTopoDS_TranslateSolidError # value = <StepToTopoDS_TranslateSolidError.StepToTopoDS_TranslateSolidOther: 1>
StepToTopoDS_TranslateVertexDone: OCP.StepToTopoDS.StepToTopoDS_TranslateVertexError # value = <StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexDone: 0>
StepToTopoDS_TranslateVertexLoopDone: OCP.StepToTopoDS.StepToTopoDS_TranslateVertexLoopError # value = <StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopDone: 0>
StepToTopoDS_TranslateVertexLoopOther: OCP.StepToTopoDS.StepToTopoDS_TranslateVertexLoopError # value = <StepToTopoDS_TranslateVertexLoopError.StepToTopoDS_TranslateVertexLoopOther: 1>
StepToTopoDS_TranslateVertexOther: OCP.StepToTopoDS.StepToTopoDS_TranslateVertexError # value = <StepToTopoDS_TranslateVertexError.StepToTopoDS_TranslateVertexOther: 1>
