import OCP.HLRTopoBRep
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.Contap
import OCP.Geom2d
import OCP.Standard
import OCP.TopTools
import OCP.gp
import OCP.BRepTopAdaptor
import OCP.TopoDS
import OCP.HLRAlgo
__all__  = [
"HLRTopoBRep_DSFiller",
"HLRTopoBRep_Data",
"HLRTopoBRep_DataMapOfShapeFaceData",
"HLRTopoBRep_FaceData",
"HLRTopoBRep_FaceIsoLiner",
"HLRTopoBRep_ListOfVData",
"HLRTopoBRep_MapOfShapeListOfVData",
"HLRTopoBRep_OutLiner",
"HLRTopoBRep_VData"
]
class HLRTopoBRep_DSFiller():
    """
    Provides methods to fill a HLRTopoBRep_Data.
    """
    @staticmethod
    def Insert_s(S : OCP.TopoDS.TopoDS_Shape,FO : OCP.Contap.Contap_Contour,DS : HLRTopoBRep_Data,MST : OCP.BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool,nbIso : int) -> None: 
        """
        Stores in <DS> the outlines of <S> using the current outliner and stores the isolines in <DS> using a Hatcher.
        """
    def __init__(self) -> None: ...
    pass
class HLRTopoBRep_Data():
    """
    Stores the results of the OutLine and IsoLine processes.
    """
    def AddIntL(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def AddIntV(self,V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None

        None
        """
    def AddIsoL(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def AddOldS(self,NewS : OCP.TopoDS.TopoDS_Shape,OldS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddOutL(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def AddOutV(self,V : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        None

        None
        """
    def AddSplE(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Append(self,V : OCP.TopoDS.TopoDS_Vertex,P : float) -> None: 
        """
        None
        """
    def Clean(self) -> None: 
        """
        Clear of all the data not needed during and after the hiding process.
        """
    def Clear(self) -> None: 
        """
        Clear of all the maps.
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None
        """
    def EdgeHasSplE(self,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Returns True if the Edge is split.
        """
    def EdgeSplE(self,E : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of the edges.

        Returns the list of the edges.
        """
    def FaceHasIntL(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face has internal outline.
        """
    def FaceHasIsoL(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face has isolines.
        """
    def FaceHasOutL(self,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if the Face has outlines on restriction.
        """
    def FaceIntL(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of the internal OutLines.

        Returns the list of the internal OutLines.
        """
    def FaceIsoL(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of the IsoLines.

        Returns the list of the IsoLines.
        """
    def FaceOutL(self,F : OCP.TopoDS.TopoDS_Face) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of the OutLines on restriction.

        Returns the list of the OutLines on restriction.
        """
    def InitEdge(self) -> None: 
        """
        None
        """
    def InitVertex(self,E : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        Start an iteration on the vertices of E.
        """
    def InsertBefore(self,V : OCP.TopoDS.TopoDS_Vertex,P : float) -> None: 
        """
        Insert before the current position.
        """
    def IsIntLFaceEdge(self,F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def IsIntV(self,V : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        Returns True if V is an internal outline vertex.

        Returns True if V is an internal outline vertex.
        """
    def IsIsoLFaceEdge(self,F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def IsOutLFaceEdge(self,F : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def IsOutV(self,V : OCP.TopoDS.TopoDS_Vertex) -> bool: 
        """
        Returns True if V is an outline vertex on a restriction.

        Returns True if V is an outline vertex on a restriction.
        """
    def IsSplEEdgeEdge(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def MoreEdge(self) -> bool: 
        """
        None

        None
        """
    def MoreVertex(self) -> bool: 
        """
        None

        None
        """
    def NewSOldS(self,New : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def NextEdge(self) -> None: 
        """
        None
        """
    def NextVertex(self) -> None: 
        """
        None

        None
        """
    def Parameter(self) -> float: 
        """
        None
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class HLRTopoBRep_DataMapOfShapeFaceData(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : HLRTopoBRep_DataMapOfShapeFaceData) -> HLRTopoBRep_DataMapOfShapeFaceData: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : HLRTopoBRep_FaceData) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : HLRTopoBRep_FaceData) -> HLRTopoBRep_FaceData: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> HLRTopoBRep_FaceData: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> HLRTopoBRep_FaceData: 
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
    def Exchange(self,theOther : HLRTopoBRep_DataMapOfShapeFaceData) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> HLRTopoBRep_FaceData: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : HLRTopoBRep_FaceData) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> HLRTopoBRep_FaceData: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : HLRTopoBRep_DataMapOfShapeFaceData) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class HLRTopoBRep_FaceData():
    """
    Contains the 3 ListOfShape of a Face ( Internal OutLines, OutLines on restriction and IsoLines ).
    """
    def AddIntL(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def AddIsoL(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def AddOutL(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def FaceIntL(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def FaceIsoL(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def FaceOutL(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def __init__(self) -> None: ...
    pass
class HLRTopoBRep_FaceIsoLiner():
    """
    None
    """
    @staticmethod
    def MakeIsoLine_s(F : OCP.TopoDS.TopoDS_Face,Iso : OCP.Geom2d.Geom2d_Line,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex,U1 : float,U2 : float,Tol : float,DS : HLRTopoBRep_Data) -> None: 
        """
        None
        """
    @staticmethod
    def MakeVertex_s(E : OCP.TopoDS.TopoDS_Edge,P : OCP.gp.gp_Pnt,Par : float,Tol : float,DS : HLRTopoBRep_Data) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    @staticmethod
    def Perform_s(FI : int,F : OCP.TopoDS.TopoDS_Face,DS : HLRTopoBRep_Data,nbIsos : int) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class HLRTopoBRep_ListOfVData(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : HLRTopoBRep_VData,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : HLRTopoBRep_ListOfVData) -> None: ...
    @overload
    def Append(self,theItem : HLRTopoBRep_VData) -> HLRTopoBRep_VData: ...
    def Assign(self,theOther : HLRTopoBRep_ListOfVData) -> HLRTopoBRep_ListOfVData: 
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
    def First(self) -> HLRTopoBRep_VData: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : HLRTopoBRep_VData,theIter : Any) -> HLRTopoBRep_VData: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : HLRTopoBRep_ListOfVData,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : HLRTopoBRep_VData,theIter : Any) -> HLRTopoBRep_VData: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : HLRTopoBRep_ListOfVData,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> HLRTopoBRep_VData: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : HLRTopoBRep_ListOfVData) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : HLRTopoBRep_VData) -> HLRTopoBRep_VData: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : HLRTopoBRep_ListOfVData) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class HLRTopoBRep_MapOfShapeListOfVData(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : HLRTopoBRep_MapOfShapeListOfVData) -> HLRTopoBRep_MapOfShapeListOfVData: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : HLRTopoBRep_ListOfVData) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : HLRTopoBRep_ListOfVData) -> HLRTopoBRep_ListOfVData: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> HLRTopoBRep_ListOfVData: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> HLRTopoBRep_ListOfVData: 
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
    def Exchange(self,theOther : HLRTopoBRep_MapOfShapeListOfVData) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : HLRTopoBRep_ListOfVData) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> HLRTopoBRep_ListOfVData: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> HLRTopoBRep_ListOfVData: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : HLRTopoBRep_MapOfShapeListOfVData) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class HLRTopoBRep_OutLiner(OCP.Standard.Standard_Transient):
    def DataStructure(self) -> HLRTopoBRep_Data: 
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
    def Fill(self,P : OCP.HLRAlgo.HLRAlgo_Projector,MST : OCP.BRepTopAdaptor.BRepTopAdaptor_MapOfShapeTool,nbIso : int) -> None: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    @overload
    def OriginalShape(self,OriS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def OriginalShape(self) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def OutLinedShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None

        None

        None
        """
    @overload
    def OutLinedShape(self,OutS : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,OriS : OCP.TopoDS.TopoDS_Shape,OutS : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,OriSh : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class HLRTopoBRep_VData():
    """
    None
    """
    def Parameter(self) -> float: 
        """
        None

        None
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : float,V : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
