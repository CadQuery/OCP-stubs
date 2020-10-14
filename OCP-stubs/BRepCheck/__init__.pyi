import OCP.BRepCheck
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.Adaptor3d
import OCP.Standard
import OCP.TopoDS
import OCP.NCollection
__all__  = [
"BRepCheck",
"BRepCheck_Analyzer",
"BRepCheck_DataMapOfShapeListOfStatus",
"BRepCheck_Result",
"BRepCheck_Face",
"BRepCheck_ListOfStatus",
"BRepCheck_Edge",
"BRepCheck_Shell",
"BRepCheck_Solid",
"BRepCheck_Status",
"BRepCheck_Vertex",
"BRepCheck_Wire",
"BRepCheck_BadOrientation",
"BRepCheck_BadOrientationOfSubshape",
"BRepCheck_CheckFail",
"BRepCheck_EmptyShell",
"BRepCheck_EmptyWire",
"BRepCheck_EnclosedRegion",
"BRepCheck_FreeEdge",
"BRepCheck_IntersectingWires",
"BRepCheck_Invalid3DCurve",
"BRepCheck_InvalidCurveOnClosedSurface",
"BRepCheck_InvalidCurveOnSurface",
"BRepCheck_InvalidDegeneratedFlag",
"BRepCheck_InvalidImbricationOfShells",
"BRepCheck_InvalidImbricationOfWires",
"BRepCheck_InvalidMultiConnexity",
"BRepCheck_InvalidPointOnCurve",
"BRepCheck_InvalidPointOnCurveOnSurface",
"BRepCheck_InvalidPointOnSurface",
"BRepCheck_InvalidPolygonOnTriangulation",
"BRepCheck_InvalidRange",
"BRepCheck_InvalidSameParameterFlag",
"BRepCheck_InvalidSameRangeFlag",
"BRepCheck_InvalidToleranceValue",
"BRepCheck_InvalidWire",
"BRepCheck_Multiple3DCurve",
"BRepCheck_No3DCurve",
"BRepCheck_NoCurveOnSurface",
"BRepCheck_NoError",
"BRepCheck_NoSurface",
"BRepCheck_NotClosed",
"BRepCheck_NotConnected",
"BRepCheck_RedundantEdge",
"BRepCheck_RedundantFace",
"BRepCheck_RedundantWire",
"BRepCheck_SelfIntersectingWire",
"BRepCheck_SubshapeNotInShape",
"BRepCheck_UnorientableShape"
]
class BRepCheck():
    """
    This package provides tools to check the validity of the BRep.
    """
    @staticmethod
    def Add_s(List : BRepCheck_ListOfStatus,Stat : BRepCheck_Status) -> None: 
        """
        None
        """
    @staticmethod
    def PrecCurve_s(aAC3D : OCP.Adaptor3d.Adaptor3d_Curve) -> float: 
        """
        Returns the resolution on the 3d curve
        """
    @staticmethod
    def PrecSurface_s(aAHSurf : OCP.Adaptor3d.Adaptor3d_HSurface) -> float: 
        """
        Returns the resolution on the surface
        """
    @staticmethod
    def Print_s(Stat : BRepCheck_Status,OS : Any) -> None: 
        """
        None
        """
    @staticmethod
    def SelfIntersection_s(W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BRepCheck_Analyzer():
    """
    A framework to check the overall validity of a shape. For a shape to be valid in Open CASCADE, it - or its component subshapes - must respect certain criteria. These criteria are checked by the function IsValid. Once you have determined whether a shape is valid or not, you can diagnose its specific anomalies and correct them using the services of the ShapeAnalysis, ShapeUpgrade, and ShapeFix packages.
    """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape,GeomControls : bool=True) -> None: 
        """
        <S> is the shape to control. <GeomControls> If False only topological informaions are checked. The geometricals controls are For a Vertex : BRepCheck_InvalidTolerance NYI For an Edge : BRepCheck_InvalidCurveOnClosedSurface, BRepCheck_InvalidCurveOnSurface, BRepCheck_InvalidSameParameterFlag, BRepCheck_InvalidTolerance NYI For a face : BRepCheck_UnorientableShape, BRepCheck_IntersectingWires, BRepCheck_InvalidTolerance NYI For a wire : BRepCheck_SelfIntersectingWire
        """
    @overload
    def IsValid(self) -> bool: 
        """
        <S> is a subshape of the original shape. Returns <STandard_True> if no default has been detected on <S> and any of its subshape.

        Returns true if no defect is detected on the shape S or any of its subshapes. Returns true if the shape S is valid. This function checks whether a given shape is valid by checking that: - the topology is correct - parameterization of edges in particular is correct. For the topology to be correct, the following conditions must be satisfied: - edges should have at least two vertices if they are not degenerate edges. The vertices should be within the range of the bounding edges at the tolerance specified in the vertex, - edges should share at least one face. The representation of the edges should be within the tolerance criterion assigned to them. - wires defining a face should not self-intersect and should be closed, - there should be one wire which contains all other wires inside a face, - wires should be correctly oriented with respect to each of the edges, - faces should be correctly oriented, in particular with respect to adjacent faces if these faces define a solid, - shells defining a solid should be closed. There should be one enclosing shell if the shape is a solid; To check parameterization of edge, there are 2 approaches depending on the edge?s contextual situation. - if the edge is either single, or it is in the context of a wire or a compound, its parameterization is defined by the parameterization of its 3D curve and is considered as valid. - If the edge is in the context of a face, it should have SameParameter and SameRange flags set to Standard_True. To check these flags, you should call the function BRep_Tool::SameParameter and BRep_Tool::SameRange for an edge. If at least one of these flags is set to Standard_False, the edge is considered as invalid without any additional check. If the edge is contained by a face, and it has SameParameter and SameRange flags set to Standard_True, IsValid checks whether representation of the edge on face, in context of which the edge is considered, has the same parameterization up to the tolerance value coded on the edge. For a given parameter t on the edge having C as a 3D curve and one PCurve P on a surface S (base surface of the reference face), this checks that |C(t) - S(P(t))| is less than or equal to tolerance, where tolerance is the tolerance value coded on the edge.

        Returns true if no defect is detected on the shape S or any of its subshapes. Returns true if the shape S is valid. This function checks whether a given shape is valid by checking that: - the topology is correct - parameterization of edges in particular is correct. For the topology to be correct, the following conditions must be satisfied: - edges should have at least two vertices if they are not degenerate edges. The vertices should be within the range of the bounding edges at the tolerance specified in the vertex, - edges should share at least one face. The representation of the edges should be within the tolerance criterion assigned to them. - wires defining a face should not self-intersect and should be closed, - there should be one wire which contains all other wires inside a face, - wires should be correctly oriented with respect to each of the edges, - faces should be correctly oriented, in particular with respect to adjacent faces if these faces define a solid, - shells defining a solid should be closed. There should be one enclosing shell if the shape is a solid; To check parameterization of edge, there are 2 approaches depending on the edge?s contextual situation. - if the edge is either single, or it is in the context of a wire or a compound, its parameterization is defined by the parameterization of its 3D curve and is considered as valid. - If the edge is in the context of a face, it should have SameParameter and SameRange flags set to Standard_True. To check these flags, you should call the function BRep_Tool::SameParameter and BRep_Tool::SameRange for an edge. If at least one of these flags is set to Standard_False, the edge is considered as invalid without any additional check. If the edge is contained by a face, and it has SameParameter and SameRange flags set to Standard_True, IsValid checks whether representation of the edge on face, in context of which the edge is considered, has the same parameterization up to the tolerance value coded on the edge. For a given parameter t on the edge having C as a 3D curve and one PCurve P on a surface S (base surface of the reference face), this checks that |C(t) - S(P(t))| is less than or equal to tolerance, where tolerance is the tolerance value coded on the edge.
        """
    @overload
    def IsValid(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    @overload
    def Result(self,SubS : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_Result: 
        """
        None

        None
        """
    @overload
    def Result(self,S : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_Result: ...
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,GeomControls : bool=True) -> None: ...
    pass
class BRepCheck_DataMapOfShapeListOfStatus(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepCheck_DataMapOfShapeListOfStatus) -> BRepCheck_DataMapOfShapeListOfStatus: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BRepCheck_ListOfStatus) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BRepCheck_ListOfStatus) -> BRepCheck_ListOfStatus: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
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
    def Exchange(self,theOther : BRepCheck_DataMapOfShapeListOfStatus) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : BRepCheck_ListOfStatus) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BRepCheck_DataMapOfShapeListOfStatus) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BRepCheck_Result(OCP.Standard.Standard_Transient):
    def Blind(self) -> None: 
        """
        None
        """
    def ContextualShape(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def InContext(self,ContextShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitContextIterator(self) -> None: 
        """
        None
        """
    def IsBlind(self) -> bool: 
        """
        None

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
    def IsMinimum(self) -> bool: 
        """
        None

        None
        """
    def Minimum(self) -> None: 
        """
        None
        """
    def MoreShapeInContext(self) -> bool: 
        """
        None

        None
        """
    def NextShapeInContext(self) -> None: 
        """
        None
        """
    def SetFailStatus(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Status(self) -> BRepCheck_ListOfStatus: 
        """
        None

        None
        """
    @overload
    def StatusOnShape(self,S : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
        """
        If not already done, performs the InContext control and returns the list of status.

        None

        None
        """
    @overload
    def StatusOnShape(self) -> BRepCheck_ListOfStatus: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class BRepCheck_Face(BRepCheck_Result, OCP.Standard.Standard_Transient):
    def Blind(self) -> None: 
        """
        None
        """
    def ClassifyWires(self,Update : bool=False) -> BRepCheck_Status: 
        """
        None
        """
    def ContextualShape(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    @overload
    def GeometricControls(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def GeometricControls(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def InContext(self,ContextShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitContextIterator(self) -> None: 
        """
        None
        """
    def IntersectWires(self,Update : bool=False) -> BRepCheck_Status: 
        """
        None
        """
    def IsBlind(self) -> bool: 
        """
        None

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
    def IsMinimum(self) -> bool: 
        """
        None

        None
        """
    def IsUnorientable(self) -> bool: 
        """
        None
        """
    def Minimum(self) -> None: 
        """
        None
        """
    def MoreShapeInContext(self) -> bool: 
        """
        None

        None
        """
    def NextShapeInContext(self) -> None: 
        """
        None
        """
    def OrientationOfWires(self,Update : bool=False) -> BRepCheck_Status: 
        """
        None
        """
    def SetFailStatus(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def SetStatus(self,theStatus : BRepCheck_Status) -> None: 
        """
        Sets status of Face;
        """
    def SetUnorientable(self) -> None: 
        """
        None
        """
    def Status(self) -> BRepCheck_ListOfStatus: 
        """
        None

        None
        """
    @overload
    def StatusOnShape(self,S : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
        """
        If not already done, performs the InContext control and returns the list of status.

        None

        None
        """
    @overload
    def StatusOnShape(self) -> BRepCheck_ListOfStatus: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
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
class BRepCheck_ListOfStatus(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : BRepCheck_ListOfStatus) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : BRepCheck_Status) -> BRepCheck_Status: ...
    @overload
    def Append(self,theItem : BRepCheck_Status,theIter : Any) -> None: ...
    def Assign(self,theOther : BRepCheck_ListOfStatus) -> BRepCheck_ListOfStatus: 
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
    def First(self) -> BRepCheck_Status: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : BRepCheck_Status,theIter : Any) -> BRepCheck_Status: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : BRepCheck_ListOfStatus,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : BRepCheck_ListOfStatus,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : BRepCheck_Status,theIter : Any) -> BRepCheck_Status: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BRepCheck_Status: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : BRepCheck_ListOfStatus) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : BRepCheck_Status) -> BRepCheck_Status: ...
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
    def __init__(self,theOther : BRepCheck_ListOfStatus) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BRepCheck_Edge(BRepCheck_Result, OCP.Standard.Standard_Transient):
    def Blind(self) -> None: 
        """
        None
        """
    def CheckPolygonOnTriangulation(self,theEdge : OCP.TopoDS.TopoDS_Edge) -> BRepCheck_Status: 
        """
        Checks, if polygon on triangulation of heEdge is out of 3D-curve of this edge.
        """
    def ContextualShape(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    @overload
    def GeometricControls(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def GeometricControls(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def InContext(self,ContextShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitContextIterator(self) -> None: 
        """
        None
        """
    def IsBlind(self) -> bool: 
        """
        None

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
    def IsMinimum(self) -> bool: 
        """
        None

        None
        """
    def Minimum(self) -> None: 
        """
        None
        """
    def MoreShapeInContext(self) -> bool: 
        """
        None

        None
        """
    def NextShapeInContext(self) -> None: 
        """
        None
        """
    def SetFailStatus(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def SetStatus(self,theStatus : BRepCheck_Status) -> None: 
        """
        Sets status of Edge;
        """
    def Status(self) -> BRepCheck_ListOfStatus: 
        """
        None

        None
        """
    @overload
    def StatusOnShape(self,S : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
        """
        If not already done, performs the InContext control and returns the list of status.

        None

        None
        """
    @overload
    def StatusOnShape(self) -> BRepCheck_ListOfStatus: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Tolerance(self) -> float: 
        """
        None
        """
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
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
class BRepCheck_Shell(BRepCheck_Result, OCP.Standard.Standard_Transient):
    def Blind(self) -> None: 
        """
        None
        """
    def Closed(self,Update : bool=False) -> BRepCheck_Status: 
        """
        Checks if the oriented faces of the shell give a closed shell. If the wire is closed, returns BRepCheck_NoError.If <Update> is set to Standard_True, registers the status in the list.
        """
    def ContextualShape(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def InContext(self,ContextShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitContextIterator(self) -> None: 
        """
        None
        """
    def IsBlind(self) -> bool: 
        """
        None

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
    def IsMinimum(self) -> bool: 
        """
        None

        None
        """
    def IsUnorientable(self) -> bool: 
        """
        None
        """
    def Minimum(self) -> None: 
        """
        None
        """
    def MoreShapeInContext(self) -> bool: 
        """
        None

        None
        """
    def NbConnectedSet(self,theSets : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None
        """
    def NextShapeInContext(self) -> None: 
        """
        None
        """
    def Orientation(self,Update : bool=False) -> BRepCheck_Status: 
        """
        Checks if the oriented faces of the shell are correctly oriented. An internal call is made to the method Closed. If <Update> is set to Standard_True, registers the status in the list.
        """
    def SetFailStatus(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def SetUnorientable(self) -> None: 
        """
        None
        """
    def Status(self) -> BRepCheck_ListOfStatus: 
        """
        None

        None
        """
    @overload
    def StatusOnShape(self,S : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
        """
        If not already done, performs the InContext control and returns the list of status.

        None

        None
        """
    @overload
    def StatusOnShape(self) -> BRepCheck_ListOfStatus: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shell) -> None: ...
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
class BRepCheck_Solid(BRepCheck_Result, OCP.Standard.Standard_Transient):
    """
    The class is to check a solid.The class is to check a solid.The class is to check a solid.
    """
    def Blind(self) -> None: 
        """
        see the parent class for more details
        """
    def ContextualShape(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def InContext(self,theContextShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Checks the solid in context of the shape <theContextShape>
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitContextIterator(self) -> None: 
        """
        None
        """
    def IsBlind(self) -> bool: 
        """
        None

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
    def IsMinimum(self) -> bool: 
        """
        None

        None
        """
    def Minimum(self) -> None: 
        """
        Checks the solid per se.
        """
    def MoreShapeInContext(self) -> bool: 
        """
        None

        None
        """
    def NextShapeInContext(self) -> None: 
        """
        None
        """
    def SetFailStatus(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Status(self) -> BRepCheck_ListOfStatus: 
        """
        None

        None
        """
    @overload
    def StatusOnShape(self,S : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
        """
        If not already done, performs the InContext control and returns the list of status.

        None

        None
        """
    @overload
    def StatusOnShape(self) -> BRepCheck_ListOfStatus: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theS : OCP.TopoDS.TopoDS_Solid) -> None: ...
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
class BRepCheck_Status():
    """
    None

    Members:

      BRepCheck_NoError

      BRepCheck_InvalidPointOnCurve

      BRepCheck_InvalidPointOnCurveOnSurface

      BRepCheck_InvalidPointOnSurface

      BRepCheck_No3DCurve

      BRepCheck_Multiple3DCurve

      BRepCheck_Invalid3DCurve

      BRepCheck_NoCurveOnSurface

      BRepCheck_InvalidCurveOnSurface

      BRepCheck_InvalidCurveOnClosedSurface

      BRepCheck_InvalidSameRangeFlag

      BRepCheck_InvalidSameParameterFlag

      BRepCheck_InvalidDegeneratedFlag

      BRepCheck_FreeEdge

      BRepCheck_InvalidMultiConnexity

      BRepCheck_InvalidRange

      BRepCheck_EmptyWire

      BRepCheck_RedundantEdge

      BRepCheck_SelfIntersectingWire

      BRepCheck_NoSurface

      BRepCheck_InvalidWire

      BRepCheck_RedundantWire

      BRepCheck_IntersectingWires

      BRepCheck_InvalidImbricationOfWires

      BRepCheck_EmptyShell

      BRepCheck_RedundantFace

      BRepCheck_InvalidImbricationOfShells

      BRepCheck_UnorientableShape

      BRepCheck_NotClosed

      BRepCheck_NotConnected

      BRepCheck_SubshapeNotInShape

      BRepCheck_BadOrientation

      BRepCheck_BadOrientationOfSubshape

      BRepCheck_InvalidPolygonOnTriangulation

      BRepCheck_InvalidToleranceValue

      BRepCheck_EnclosedRegion

      BRepCheck_CheckFail
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
    BRepCheck_BadOrientation: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_BadOrientation
    BRepCheck_BadOrientationOfSubshape: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_BadOrientationOfSubshape
    BRepCheck_CheckFail: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_CheckFail
    BRepCheck_EmptyShell: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_EmptyShell
    BRepCheck_EmptyWire: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_EmptyWire
    BRepCheck_EnclosedRegion: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_EnclosedRegion
    BRepCheck_FreeEdge: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_FreeEdge
    BRepCheck_IntersectingWires: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_IntersectingWires
    BRepCheck_Invalid3DCurve: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_Invalid3DCurve
    BRepCheck_InvalidCurveOnClosedSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidCurveOnClosedSurface
    BRepCheck_InvalidCurveOnSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidCurveOnSurface
    BRepCheck_InvalidDegeneratedFlag: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidDegeneratedFlag
    BRepCheck_InvalidImbricationOfShells: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidImbricationOfShells
    BRepCheck_InvalidImbricationOfWires: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidImbricationOfWires
    BRepCheck_InvalidMultiConnexity: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidMultiConnexity
    BRepCheck_InvalidPointOnCurve: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidPointOnCurve
    BRepCheck_InvalidPointOnCurveOnSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidPointOnCurveOnSurface
    BRepCheck_InvalidPointOnSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidPointOnSurface
    BRepCheck_InvalidPolygonOnTriangulation: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidPolygonOnTriangulation
    BRepCheck_InvalidRange: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidRange
    BRepCheck_InvalidSameParameterFlag: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidSameParameterFlag
    BRepCheck_InvalidSameRangeFlag: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidSameRangeFlag
    BRepCheck_InvalidToleranceValue: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidToleranceValue
    BRepCheck_InvalidWire: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidWire
    BRepCheck_Multiple3DCurve: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_Multiple3DCurve
    BRepCheck_No3DCurve: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_No3DCurve
    BRepCheck_NoCurveOnSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NoCurveOnSurface
    BRepCheck_NoError: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NoError
    BRepCheck_NoSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NoSurface
    BRepCheck_NotClosed: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NotClosed
    BRepCheck_NotConnected: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NotConnected
    BRepCheck_RedundantEdge: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_RedundantEdge
    BRepCheck_RedundantFace: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_RedundantFace
    BRepCheck_RedundantWire: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_RedundantWire
    BRepCheck_SelfIntersectingWire: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_SelfIntersectingWire
    BRepCheck_SubshapeNotInShape: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_SubshapeNotInShape
    BRepCheck_UnorientableShape: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_UnorientableShape
    __entries: dict # value = {'BRepCheck_NoError': (BRepCheck_Status.BRepCheck_NoError, None), 'BRepCheck_InvalidPointOnCurve': (BRepCheck_Status.BRepCheck_InvalidPointOnCurve, None), 'BRepCheck_InvalidPointOnCurveOnSurface': (BRepCheck_Status.BRepCheck_InvalidPointOnCurveOnSurface, None), 'BRepCheck_InvalidPointOnSurface': (BRepCheck_Status.BRepCheck_InvalidPointOnSurface, None), 'BRepCheck_No3DCurve': (BRepCheck_Status.BRepCheck_No3DCurve, None), 'BRepCheck_Multiple3DCurve': (BRepCheck_Status.BRepCheck_Multiple3DCurve, None), 'BRepCheck_Invalid3DCurve': (BRepCheck_Status.BRepCheck_Invalid3DCurve, None), 'BRepCheck_NoCurveOnSurface': (BRepCheck_Status.BRepCheck_NoCurveOnSurface, None), 'BRepCheck_InvalidCurveOnSurface': (BRepCheck_Status.BRepCheck_InvalidCurveOnSurface, None), 'BRepCheck_InvalidCurveOnClosedSurface': (BRepCheck_Status.BRepCheck_InvalidCurveOnClosedSurface, None), 'BRepCheck_InvalidSameRangeFlag': (BRepCheck_Status.BRepCheck_InvalidSameRangeFlag, None), 'BRepCheck_InvalidSameParameterFlag': (BRepCheck_Status.BRepCheck_InvalidSameParameterFlag, None), 'BRepCheck_InvalidDegeneratedFlag': (BRepCheck_Status.BRepCheck_InvalidDegeneratedFlag, None), 'BRepCheck_FreeEdge': (BRepCheck_Status.BRepCheck_FreeEdge, None), 'BRepCheck_InvalidMultiConnexity': (BRepCheck_Status.BRepCheck_InvalidMultiConnexity, None), 'BRepCheck_InvalidRange': (BRepCheck_Status.BRepCheck_InvalidRange, None), 'BRepCheck_EmptyWire': (BRepCheck_Status.BRepCheck_EmptyWire, None), 'BRepCheck_RedundantEdge': (BRepCheck_Status.BRepCheck_RedundantEdge, None), 'BRepCheck_SelfIntersectingWire': (BRepCheck_Status.BRepCheck_SelfIntersectingWire, None), 'BRepCheck_NoSurface': (BRepCheck_Status.BRepCheck_NoSurface, None), 'BRepCheck_InvalidWire': (BRepCheck_Status.BRepCheck_InvalidWire, None), 'BRepCheck_RedundantWire': (BRepCheck_Status.BRepCheck_RedundantWire, None), 'BRepCheck_IntersectingWires': (BRepCheck_Status.BRepCheck_IntersectingWires, None), 'BRepCheck_InvalidImbricationOfWires': (BRepCheck_Status.BRepCheck_InvalidImbricationOfWires, None), 'BRepCheck_EmptyShell': (BRepCheck_Status.BRepCheck_EmptyShell, None), 'BRepCheck_RedundantFace': (BRepCheck_Status.BRepCheck_RedundantFace, None), 'BRepCheck_InvalidImbricationOfShells': (BRepCheck_Status.BRepCheck_InvalidImbricationOfShells, None), 'BRepCheck_UnorientableShape': (BRepCheck_Status.BRepCheck_UnorientableShape, None), 'BRepCheck_NotClosed': (BRepCheck_Status.BRepCheck_NotClosed, None), 'BRepCheck_NotConnected': (BRepCheck_Status.BRepCheck_NotConnected, None), 'BRepCheck_SubshapeNotInShape': (BRepCheck_Status.BRepCheck_SubshapeNotInShape, None), 'BRepCheck_BadOrientation': (BRepCheck_Status.BRepCheck_BadOrientation, None), 'BRepCheck_BadOrientationOfSubshape': (BRepCheck_Status.BRepCheck_BadOrientationOfSubshape, None), 'BRepCheck_InvalidPolygonOnTriangulation': (BRepCheck_Status.BRepCheck_InvalidPolygonOnTriangulation, None), 'BRepCheck_InvalidToleranceValue': (BRepCheck_Status.BRepCheck_InvalidToleranceValue, None), 'BRepCheck_EnclosedRegion': (BRepCheck_Status.BRepCheck_EnclosedRegion, None), 'BRepCheck_CheckFail': (BRepCheck_Status.BRepCheck_CheckFail, None)}
    __members__: dict # value = {'BRepCheck_NoError': BRepCheck_Status.BRepCheck_NoError, 'BRepCheck_InvalidPointOnCurve': BRepCheck_Status.BRepCheck_InvalidPointOnCurve, 'BRepCheck_InvalidPointOnCurveOnSurface': BRepCheck_Status.BRepCheck_InvalidPointOnCurveOnSurface, 'BRepCheck_InvalidPointOnSurface': BRepCheck_Status.BRepCheck_InvalidPointOnSurface, 'BRepCheck_No3DCurve': BRepCheck_Status.BRepCheck_No3DCurve, 'BRepCheck_Multiple3DCurve': BRepCheck_Status.BRepCheck_Multiple3DCurve, 'BRepCheck_Invalid3DCurve': BRepCheck_Status.BRepCheck_Invalid3DCurve, 'BRepCheck_NoCurveOnSurface': BRepCheck_Status.BRepCheck_NoCurveOnSurface, 'BRepCheck_InvalidCurveOnSurface': BRepCheck_Status.BRepCheck_InvalidCurveOnSurface, 'BRepCheck_InvalidCurveOnClosedSurface': BRepCheck_Status.BRepCheck_InvalidCurveOnClosedSurface, 'BRepCheck_InvalidSameRangeFlag': BRepCheck_Status.BRepCheck_InvalidSameRangeFlag, 'BRepCheck_InvalidSameParameterFlag': BRepCheck_Status.BRepCheck_InvalidSameParameterFlag, 'BRepCheck_InvalidDegeneratedFlag': BRepCheck_Status.BRepCheck_InvalidDegeneratedFlag, 'BRepCheck_FreeEdge': BRepCheck_Status.BRepCheck_FreeEdge, 'BRepCheck_InvalidMultiConnexity': BRepCheck_Status.BRepCheck_InvalidMultiConnexity, 'BRepCheck_InvalidRange': BRepCheck_Status.BRepCheck_InvalidRange, 'BRepCheck_EmptyWire': BRepCheck_Status.BRepCheck_EmptyWire, 'BRepCheck_RedundantEdge': BRepCheck_Status.BRepCheck_RedundantEdge, 'BRepCheck_SelfIntersectingWire': BRepCheck_Status.BRepCheck_SelfIntersectingWire, 'BRepCheck_NoSurface': BRepCheck_Status.BRepCheck_NoSurface, 'BRepCheck_InvalidWire': BRepCheck_Status.BRepCheck_InvalidWire, 'BRepCheck_RedundantWire': BRepCheck_Status.BRepCheck_RedundantWire, 'BRepCheck_IntersectingWires': BRepCheck_Status.BRepCheck_IntersectingWires, 'BRepCheck_InvalidImbricationOfWires': BRepCheck_Status.BRepCheck_InvalidImbricationOfWires, 'BRepCheck_EmptyShell': BRepCheck_Status.BRepCheck_EmptyShell, 'BRepCheck_RedundantFace': BRepCheck_Status.BRepCheck_RedundantFace, 'BRepCheck_InvalidImbricationOfShells': BRepCheck_Status.BRepCheck_InvalidImbricationOfShells, 'BRepCheck_UnorientableShape': BRepCheck_Status.BRepCheck_UnorientableShape, 'BRepCheck_NotClosed': BRepCheck_Status.BRepCheck_NotClosed, 'BRepCheck_NotConnected': BRepCheck_Status.BRepCheck_NotConnected, 'BRepCheck_SubshapeNotInShape': BRepCheck_Status.BRepCheck_SubshapeNotInShape, 'BRepCheck_BadOrientation': BRepCheck_Status.BRepCheck_BadOrientation, 'BRepCheck_BadOrientationOfSubshape': BRepCheck_Status.BRepCheck_BadOrientationOfSubshape, 'BRepCheck_InvalidPolygonOnTriangulation': BRepCheck_Status.BRepCheck_InvalidPolygonOnTriangulation, 'BRepCheck_InvalidToleranceValue': BRepCheck_Status.BRepCheck_InvalidToleranceValue, 'BRepCheck_EnclosedRegion': BRepCheck_Status.BRepCheck_EnclosedRegion, 'BRepCheck_CheckFail': BRepCheck_Status.BRepCheck_CheckFail}
    pass
class BRepCheck_Vertex(BRepCheck_Result, OCP.Standard.Standard_Transient):
    def Blind(self) -> None: 
        """
        None
        """
    def ContextualShape(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def InContext(self,ContextShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitContextIterator(self) -> None: 
        """
        None
        """
    def IsBlind(self) -> bool: 
        """
        None

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
    def IsMinimum(self) -> bool: 
        """
        None

        None
        """
    def Minimum(self) -> None: 
        """
        None
        """
    def MoreShapeInContext(self) -> bool: 
        """
        None

        None
        """
    def NextShapeInContext(self) -> None: 
        """
        None
        """
    def SetFailStatus(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Status(self) -> BRepCheck_ListOfStatus: 
        """
        None

        None
        """
    @overload
    def StatusOnShape(self,S : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
        """
        If not already done, performs the InContext control and returns the list of status.

        None

        None
        """
    @overload
    def StatusOnShape(self) -> BRepCheck_ListOfStatus: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Tolerance(self) -> float: 
        """
        None
        """
    def __init__(self,V : OCP.TopoDS.TopoDS_Vertex) -> None: ...
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
class BRepCheck_Wire(BRepCheck_Result, OCP.Standard.Standard_Transient):
    def Blind(self) -> None: 
        """
        Does nothing
        """
    def Closed(self,Update : bool=False) -> BRepCheck_Status: 
        """
        Checks if the oriented edges of the wire give a closed wire. If the wire is closed, returns BRepCheck_NoError. Warning : if the first and last edge are infinite, the wire will be considered as a closed one. If <Update> is set to Standard_True, registers the status in the list. May return (and registers): **BRepCheck_NotConnected, if wire is not topologically closed **BRepCheck_RedundantEdge, if an edge is in wire more than 3 times or in case of 2 occurences if not with FORWARD and REVERSED orientation. **BRepCheck_NoError
        """
    def Closed2d(self,F : OCP.TopoDS.TopoDS_Face,Update : bool=False) -> BRepCheck_Status: 
        """
        Checks if edges of the wire give a wire closed in 2d space. Returns BRepCheck_NoError, or BRepCheck_NotClosed If <Update> is set to Standard_True, registers the status in the list.
        """
    def ContextualShape(self) -> OCP.TopoDS.TopoDS_Shape: 
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
    @overload
    def GeometricControls(self,B : bool) -> None: 
        """
        report SelfIntersect() check would be (is) done

        set SelfIntersect() to be checked
        """
    @overload
    def GeometricControls(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def InContext(self,ContextShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        if <ContextShape> is a face, consequently checks SelfIntersect(), Closed(), Orientation() and Closed2d until faulty is found
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def InitContextIterator(self) -> None: 
        """
        None
        """
    def IsBlind(self) -> bool: 
        """
        None

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
    def IsMinimum(self) -> bool: 
        """
        None

        None
        """
    def Minimum(self) -> None: 
        """
        checks that the wire is not empty and "connex". Called by constructor
        """
    def MoreShapeInContext(self) -> bool: 
        """
        None

        None
        """
    def NextShapeInContext(self) -> None: 
        """
        None
        """
    def Orientation(self,F : OCP.TopoDS.TopoDS_Face,Update : bool=False) -> BRepCheck_Status: 
        """
        Checks if the oriented edges of the wire are correctly oriented. An internal call is made to the method Closed. If no face exists, call the method with a null face (TopoDS_face()). If <Update> is set to Standard_True, registers the status in the list. May return (and registers): BRepCheck_InvalidDegeneratedFlag, BRepCheck_BadOrientationOfSubshape, BRepCheck_NotClosed, BRepCheck_NoError
        """
    def SelfIntersect(self,F : OCP.TopoDS.TopoDS_Face,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,Update : bool=False) -> BRepCheck_Status: 
        """
        Checks if the wire intersect itself on the face <F>. <E1> and <E2> are the first intersecting edges found. <E2> may be a null edge when a self-intersecting edge is found.If <Update> is set to Standard_True, registers the status in the list. May return (and register): BRepCheck_EmptyWire, BRepCheck_SelfIntersectingWire, BRepCheck_NoCurveOnSurface, BRepCheck_NoError
        """
    def SetFailStatus(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def SetStatus(self,theStatus : BRepCheck_Status) -> None: 
        """
        Sets status of Wire;
        """
    def Status(self) -> BRepCheck_ListOfStatus: 
        """
        None

        None
        """
    @overload
    def StatusOnShape(self,S : OCP.TopoDS.TopoDS_Shape) -> BRepCheck_ListOfStatus: 
        """
        If not already done, performs the InContext control and returns the list of status.

        None

        None
        """
    @overload
    def StatusOnShape(self) -> BRepCheck_ListOfStatus: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire) -> None: ...
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
BRepCheck_BadOrientation: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_BadOrientation
BRepCheck_BadOrientationOfSubshape: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_BadOrientationOfSubshape
BRepCheck_CheckFail: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_CheckFail
BRepCheck_EmptyShell: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_EmptyShell
BRepCheck_EmptyWire: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_EmptyWire
BRepCheck_EnclosedRegion: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_EnclosedRegion
BRepCheck_FreeEdge: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_FreeEdge
BRepCheck_IntersectingWires: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_IntersectingWires
BRepCheck_Invalid3DCurve: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_Invalid3DCurve
BRepCheck_InvalidCurveOnClosedSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidCurveOnClosedSurface
BRepCheck_InvalidCurveOnSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidCurveOnSurface
BRepCheck_InvalidDegeneratedFlag: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidDegeneratedFlag
BRepCheck_InvalidImbricationOfShells: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidImbricationOfShells
BRepCheck_InvalidImbricationOfWires: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidImbricationOfWires
BRepCheck_InvalidMultiConnexity: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidMultiConnexity
BRepCheck_InvalidPointOnCurve: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidPointOnCurve
BRepCheck_InvalidPointOnCurveOnSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidPointOnCurveOnSurface
BRepCheck_InvalidPointOnSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidPointOnSurface
BRepCheck_InvalidPolygonOnTriangulation: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidPolygonOnTriangulation
BRepCheck_InvalidRange: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidRange
BRepCheck_InvalidSameParameterFlag: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidSameParameterFlag
BRepCheck_InvalidSameRangeFlag: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidSameRangeFlag
BRepCheck_InvalidToleranceValue: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidToleranceValue
BRepCheck_InvalidWire: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_InvalidWire
BRepCheck_Multiple3DCurve: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_Multiple3DCurve
BRepCheck_No3DCurve: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_No3DCurve
BRepCheck_NoCurveOnSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NoCurveOnSurface
BRepCheck_NoError: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NoError
BRepCheck_NoSurface: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NoSurface
BRepCheck_NotClosed: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NotClosed
BRepCheck_NotConnected: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_NotConnected
BRepCheck_RedundantEdge: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_RedundantEdge
BRepCheck_RedundantFace: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_RedundantFace
BRepCheck_RedundantWire: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_RedundantWire
BRepCheck_SelfIntersectingWire: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_SelfIntersectingWire
BRepCheck_SubshapeNotInShape: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_SubshapeNotInShape
BRepCheck_UnorientableShape: OCP.BRepCheck.BRepCheck_Status # value = BRepCheck_Status.BRepCheck_UnorientableShape
