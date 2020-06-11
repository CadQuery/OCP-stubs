import OCP.Intf
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.Bnd
import OCP.gp
__all__  = [
"Intf",
"Intf_Array1OfLin",
"Intf_Interference",
"Intf_InterferencePolygon2d",
"Intf_PIType",
"Intf_Polygon2d",
"Intf_SectionLine",
"Intf_SectionPoint",
"Intf_SeqOfSectionLine",
"Intf_SeqOfSectionPoint",
"Intf_SeqOfTangentZone",
"Intf_TangentZone",
"Intf_Tool",
"Intf_EDGE",
"Intf_EXTERNAL",
"Intf_FACE",
"Intf_VERTEX"
]
class Intf():
    """
    Interference computation between polygons, lines and polyhedra with only triangular facets. These objects are polygonal representations of complex curves and triangulated representations of complex surfaces.
    """
    @staticmethod
    def Contain_s(P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt,ThePnt : OCP.gp.gp_Pnt) -> bool: 
        """
        Compute if the triangle <P1> <P2> <P3> contain <ThePnt>.
        """
    @staticmethod
    def PlaneEquation_s(P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,P3 : OCP.gp.gp_Pnt,NormalVector : OCP.gp.gp_XYZ) -> Tuple[float]: 
        """
        Computes the interference between two polygons in 2d. Result : points of intersections and zones of tangence. Computes the interference between a polygon or a straight line and a polyhedron. Points of intersection and zones of tangence. Give the plane equation of the triangle <P1> <P2> <P3>.
        """
    def __init__(self) -> None: ...
    pass
class Intf_Array1OfLin():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Intf_Array1OfLin) -> Intf_Array1OfLin: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.gp.gp_Lin: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.gp.gp_Lin: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.gp.gp_Lin: 
        """
        Variable value access
        """
    def First(self) -> OCP.gp.gp_Lin: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.gp.gp_Lin) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> OCP.gp.gp_Lin: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : Intf_Array1OfLin) -> Intf_Array1OfLin: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.gp.gp_Lin) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> OCP.gp.gp_Lin: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Intf_Array1OfLin) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.gp.gp_Lin,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Intf_Interference():
    """
    Describes the Interference computation result between polygon2d or polygon3d or polyhedron (as three sequences of points of intersection, polylines of intersection and zones de tangence).
    """
    def Contains(self,ThePnt : Intf_SectionPoint) -> bool: 
        """
        Tests if the polylines of intersection or the zones of tangence contain the point of intersection <ThePnt>.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def GetTolerance(self) -> float: 
        """
        Gives the tolerance used for the calculation.

        Gives the tolerance used for the calculation.
        """
    @overload
    def Insert(self,TheZone : Intf_TangentZone) -> bool: 
        """
        Inserts a new zone of tangence in the current list of tangent zones of the interference and returns True when done.

        Insert a new segment of intersection in the current list of polylines of intersection of the interference.
        """
    @overload
    def Insert(self,pdeb : Intf_SectionPoint,pfin : Intf_SectionPoint) -> None: ...
    def LineValue(self,Index : int) -> Intf_SectionLine: 
        """
        Gives the polyline of intersection at address <Index> in the interference.

        Gives the polyline of intersection at address <Index> in the interference.
        """
    def NbSectionLines(self) -> int: 
        """
        Gives the number of polylines of intersection in the interference.

        Gives the number of polylines of intersection in the interference.
        """
    def NbSectionPoints(self) -> int: 
        """
        Gives the number of points of intersection in the interference.

        Gives the number of points of intersection in the interference.
        """
    def NbTangentZones(self) -> int: 
        """
        Gives the number of zones of tangence in the interference.

        Gives the number of zones of tangence in the interference.
        """
    def PntValue(self,Index : int) -> Intf_SectionPoint: 
        """
        Gives the point of intersection of address Index in the interference.

        Gives the point of intersection of address Index in the interference.
        """
    def ZoneValue(self,Index : int) -> Intf_TangentZone: 
        """
        Gives the zone of tangence at address Index in the interference.

        Gives the zone of tangence at address Index in the interference.
        """
    pass
class Intf_InterferencePolygon2d(Intf_Interference):
    """
    Computes the interference between two polygons or the self intersection of a polygon in two dimensions.
    """
    def Contains(self,ThePnt : Intf_SectionPoint) -> bool: 
        """
        Tests if the polylines of intersection or the zones of tangence contain the point of intersection <ThePnt>.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def GetTolerance(self) -> float: 
        """
        Gives the tolerance used for the calculation.

        Gives the tolerance used for the calculation.
        """
    @overload
    def Insert(self,TheZone : Intf_TangentZone) -> bool: 
        """
        Inserts a new zone of tangence in the current list of tangent zones of the interference and returns True when done.

        Insert a new segment of intersection in the current list of polylines of intersection of the interference.
        """
    @overload
    def Insert(self,pdeb : Intf_SectionPoint,pfin : Intf_SectionPoint) -> None: ...
    def LineValue(self,Index : int) -> Intf_SectionLine: 
        """
        Gives the polyline of intersection at address <Index> in the interference.

        Gives the polyline of intersection at address <Index> in the interference.
        """
    def NbSectionLines(self) -> int: 
        """
        Gives the number of polylines of intersection in the interference.

        Gives the number of polylines of intersection in the interference.
        """
    def NbSectionPoints(self) -> int: 
        """
        Gives the number of points of intersection in the interference.

        Gives the number of points of intersection in the interference.
        """
    def NbTangentZones(self) -> int: 
        """
        Gives the number of zones of tangence in the interference.

        Gives the number of zones of tangence in the interference.
        """
    @overload
    def Perform(self,Obje : Intf_Polygon2d) -> None: 
        """
        Computes an interference between two Polygons.

        Computes the self interference of a Polygon.
        """
    @overload
    def Perform(self,Obje1 : Intf_Polygon2d,Obje2 : Intf_Polygon2d) -> None: ...
    def Pnt2dValue(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        Gives the geometrical 2d point of the intersection point at address <Index> in the interference.
        """
    def PntValue(self,Index : int) -> Intf_SectionPoint: 
        """
        Gives the point of intersection of address Index in the interference.

        Gives the point of intersection of address Index in the interference.
        """
    def ZoneValue(self,Index : int) -> Intf_TangentZone: 
        """
        Gives the zone of tangence at address Index in the interference.

        Gives the zone of tangence at address Index in the interference.
        """
    @overload
    def __init__(self,Obje : Intf_Polygon2d) -> None: ...
    @overload
    def __init__(self,Obje1 : Intf_Polygon2d,Obje2 : Intf_Polygon2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Intf_PIType():
    """
    Describes the different intersection point types for this application.

    Members:

      Intf_EXTERNAL

      Intf_FACE

      Intf_EDGE

      Intf_VERTEX
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Intf_EDGE: OCP.Intf.Intf_PIType # value = Intf_PIType.Intf_EDGE
    Intf_EXTERNAL: OCP.Intf.Intf_PIType # value = Intf_PIType.Intf_EXTERNAL
    Intf_FACE: OCP.Intf.Intf_PIType # value = Intf_PIType.Intf_FACE
    Intf_VERTEX: OCP.Intf.Intf_PIType # value = Intf_PIType.Intf_VERTEX
    __entries: dict # value = {'Intf_EXTERNAL': (Intf_PIType.Intf_EXTERNAL, None), 'Intf_FACE': (Intf_PIType.Intf_FACE, None), 'Intf_EDGE': (Intf_PIType.Intf_EDGE, None), 'Intf_VERTEX': (Intf_PIType.Intf_VERTEX, None)}
    __members__: dict # value = {'Intf_EXTERNAL': Intf_PIType.Intf_EXTERNAL, 'Intf_FACE': Intf_PIType.Intf_FACE, 'Intf_EDGE': Intf_PIType.Intf_EDGE, 'Intf_VERTEX': Intf_PIType.Intf_VERTEX}
    pass
class Intf_Polygon2d():
    """
    Describes the necessary polygon information to compute the interferences.
    """
    def Bounding(self) -> OCP.Bnd.Bnd_Box2d: 
        """
        Returns the bounding box of the polygon.

        Returns the bounding box of the polygon.
        """
    def Closed(self) -> bool: 
        """
        Returns True if the polyline is closed.
        """
    def DeflectionOverEstimation(self) -> float: 
        """
        Returns the tolerance of the polygon.
        """
    def NbSegments(self) -> int: 
        """
        Returns the number of Segments in the polyline.
        """
    def Segment(self,theIndex : int,theBegin : OCP.gp.gp_Pnt2d,theEnd : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns the points of the segment <Index> in the Polygon.
        """
    pass
class Intf_SectionLine():
    """
    Describe a polyline of intersection between two polyhedra as a sequence of points of intersection.
    """
    @overload
    def Append(self,Pi : Intf_SectionPoint) -> None: 
        """
        Adds a point at the end of the SectionLine.

        Concatenates the SectionLine <LS> at the end of the SectionLine <me>.
        """
    @overload
    def Append(self,LS : Intf_SectionLine) -> None: ...
    def Close(self) -> None: 
        """
        Closes the SectionLine.
        """
    def Contains(self,ThePI : Intf_SectionPoint) -> bool: 
        """
        Returns True if ThePI is in the SectionLine <me>.
        """
    def Dump(self,Indent : int) -> None: 
        """
        None
        """
    def GetPoint(self,Index : int) -> Intf_SectionPoint: 
        """
        Gives the point of intersection of address <Index> in the SectionLine.
        """
    def IsClosed(self) -> bool: 
        """
        Returns True if the SectionLine is closed.
        """
    def IsEnd(self,ThePI : Intf_SectionPoint) -> int: 
        """
        Checks if <ThePI> is an end of the SectionLine. Returns 1 for the beginning, 2 for the end, otherwise 0.
        """
    def IsEqual(self,Other : Intf_SectionLine) -> bool: 
        """
        Compares two SectionLines.
        """
    def NumberOfPoints(self) -> int: 
        """
        Returns number of points in this SectionLine.

        Returns number of points in this SectionLine.
        """
    @overload
    def Prepend(self,LS : Intf_SectionLine) -> None: 
        """
        Adds a point to the beginning of the SectionLine <me>.

        Concatenates a SectionLine <LS> at the beginning of the SectionLine <me>.
        """
    @overload
    def Prepend(self,Pi : Intf_SectionPoint) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverses the order of the elements of the SectionLine.
        """
    @overload
    def __init__(self,Other : Intf_SectionLine) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Intf_SectionPoint():
    """
    Describes an intersection point between polygons and polyedra.
    """
    def Dump(self,Indent : int) -> None: 
        """
        None
        """
    def Incidence(self) -> float: 
        """
        Gives the incidence at this section point. The incidence between the two triangles is given by the cosine. The best incidence is 0. (PI/2). The worst is 1. (null angle).
        """
    @overload
    def InfoFirst(self,Dim : Intf_PIType) -> Tuple[int, int, float]: 
        """
        None

        Gives the datas about the first argument of the Interference.
        """
    @overload
    def InfoFirst(self,Dim : Intf_PIType) -> Tuple[int, float]: ...
    @overload
    def InfoSecond(self,Dim : Intf_PIType) -> Tuple[int, float]: 
        """
        None

        Gives the datas about the second argument of the Interference.
        """
    @overload
    def InfoSecond(self,Dim : Intf_PIType) -> Tuple[int, int, float]: ...
    def IsEqual(self,Other : Intf_SectionPoint) -> bool: 
        """
        Returns True if the two SectionPoint have the same logical informations.

        Returns True if the two SectionPoint have the same logical informations.
        """
    def IsOnSameEdge(self,Other : Intf_SectionPoint) -> bool: 
        """
        Returns True if the two SectionPoints are on the same edge of the first or the second element.
        """
    def Merge(self,Other : Intf_SectionPoint) -> None: 
        """
        Merges two SectionPoints.
        """
    def ParamOnFirst(self) -> float: 
        """
        Returns the cumulated Parameter of the SectionPoint on the first element.

        Returns the cumulated Parameter of the SectionPoint on the first element.
        """
    def ParamOnSecond(self) -> float: 
        """
        Returns the cumulated Parameter of the section point on the second element.

        Returns the cumulated Parameter of the section point on the second element.
        """
    def Pnt(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the location of the SectionPoint.
        """
    def TypeOnFirst(self) -> Intf_PIType: 
        """
        Returns the type of the section point on the first element.

        Returns the type of the section point on the first element.
        """
    def TypeOnSecond(self) -> Intf_PIType: 
        """
        Returns the type of the section point on the second element.

        Returns the type of the section point on the second element.
        """
    @overload
    def __init__(self,Where : OCP.gp.gp_Pnt2d,DimeO : Intf_PIType,AddrO1 : int,ParamO : float,DimeT : Intf_PIType,AddrT1 : int,ParamT : float,Incid : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Where : OCP.gp.gp_Pnt,DimeO : Intf_PIType,AddrO1 : int,AddrO2 : int,ParamO : float,DimeT : Intf_PIType,AddrT1 : int,AddrT2 : int,ParamT : float,Incid : float) -> None: ...
    pass
class Intf_SeqOfSectionLine(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Intf_SectionLine) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Intf_SeqOfSectionLine) -> None: ...
    def Assign(self,theOther : Intf_SeqOfSectionLine) -> Intf_SeqOfSectionLine: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Intf_SectionLine: 
        """
        First item access
        """
    def ChangeLast(self) -> Intf_SectionLine: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Intf_SectionLine: 
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
    def First(self) -> Intf_SectionLine: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Intf_SeqOfSectionLine) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Intf_SectionLine) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Intf_SectionLine) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Intf_SeqOfSectionLine) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Intf_SectionLine: 
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
    def Prepend(self,theItem : Intf_SectionLine) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Intf_SeqOfSectionLine) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Intf_SectionLine) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Intf_SeqOfSectionLine) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Intf_SectionLine: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Intf_SeqOfSectionLine) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Intf_SeqOfSectionPoint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Intf_SectionPoint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Intf_SeqOfSectionPoint) -> None: ...
    def Assign(self,theOther : Intf_SeqOfSectionPoint) -> Intf_SeqOfSectionPoint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Intf_SectionPoint: 
        """
        First item access
        """
    def ChangeLast(self) -> Intf_SectionPoint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Intf_SectionPoint: 
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
    def First(self) -> Intf_SectionPoint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Intf_SeqOfSectionPoint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Intf_SectionPoint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Intf_SectionPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Intf_SeqOfSectionPoint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Intf_SectionPoint: 
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
    def Prepend(self,theItem : Intf_SectionPoint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Intf_SeqOfSectionPoint) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Intf_SectionPoint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Intf_SeqOfSectionPoint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Intf_SectionPoint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Intf_SeqOfSectionPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Intf_SeqOfTangentZone(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Intf_SeqOfTangentZone) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Intf_TangentZone) -> None: ...
    def Assign(self,theOther : Intf_SeqOfTangentZone) -> Intf_SeqOfTangentZone: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Intf_TangentZone: 
        """
        First item access
        """
    def ChangeLast(self) -> Intf_TangentZone: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Intf_TangentZone: 
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
    def First(self) -> Intf_TangentZone: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Intf_SeqOfTangentZone) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Intf_TangentZone) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Intf_SeqOfTangentZone) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Intf_TangentZone) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Intf_TangentZone: 
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
    def Prepend(self,theItem : Intf_TangentZone) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Intf_SeqOfTangentZone) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Intf_TangentZone) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Intf_SeqOfTangentZone) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Intf_TangentZone: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Intf_SeqOfTangentZone) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Intf_TangentZone():
    """
    Describes a zone of tangence between polygons or polyhedra as a sequence of points of intersection.
    """
    @overload
    def Append(self,Tzi : Intf_TangentZone) -> None: 
        """
        Adds a SectionPoint to the TangentZone.

        Adds the TangentZone <Tzi> to <me>.
        """
    @overload
    def Append(self,Pi : Intf_SectionPoint) -> None: ...
    def Contains(self,ThePI : Intf_SectionPoint) -> bool: 
        """
        Checks if <ThePI> is in TangentZone.
        """
    def Dump(self,Indent : int) -> None: 
        """
        None
        """
    def GetPoint(self,Index : int) -> Intf_SectionPoint: 
        """
        Gives the SectionPoint of address <Index> in the TangentZone.
        """
    def HasCommonRange(self,Other : Intf_TangentZone) -> bool: 
        """
        Returns True if the TangentZone <Other> has a common part with <me>.
        """
    def InfoFirst(self) -> Tuple[int, float, int, float]: 
        """
        Gives information about the first argument of the Interference. (Usable only for polygon)
        """
    def InfoSecond(self) -> Tuple[int, float, int, float]: 
        """
        Gives informations about the second argument of the Interference. (Usable only for polygon)
        """
    def Insert(self,Pi : Intf_SectionPoint) -> bool: 
        """
        Inserts a SectionPoint in the TangentZone.
        """
    def InsertAfter(self,Index : int,Pi : Intf_SectionPoint) -> None: 
        """
        Inserts a SectionPoint after <Index> in the TangentZone.
        """
    def InsertBefore(self,Index : int,Pi : Intf_SectionPoint) -> None: 
        """
        Inserts a SectionPoint before <Index> in the TangentZone.
        """
    def IsEqual(self,Other : Intf_TangentZone) -> bool: 
        """
        Compares two TangentZones.
        """
    def NumberOfPoints(self) -> int: 
        """
        Returns number of SectionPoint in this TangentZone.

        Returns number of SectionPoint in this TangentZone.
        """
    def ParamOnFirst(self) -> Tuple[float, float]: 
        """
        Gives the parameter range of the TangentZone on the first argument of the Interference. (Usable only for polygon)

        Gives the parameter range of the TangentZone on the first argument of the Interference. (Usable only for polygon)
        """
    def ParamOnSecond(self) -> Tuple[float, float]: 
        """
        Gives the parameter range of the TangentZone on the second argument of the Interference. (Usable only for polygon)

        Gives the parameter range of the TangentZone on the second argument of the Interference. (Usable only for polygon)
        """
    def PolygonInsert(self,Pi : Intf_SectionPoint) -> None: 
        """
        Inserts a point in the polygonal TangentZone.
        """
    def RangeContains(self,ThePI : Intf_SectionPoint) -> bool: 
        """
        Returns True if <ThePI> is in the parameter range of the TangentZone.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Other : Intf_TangentZone) -> None: ...
    pass
class Intf_Tool():
    """
    Provides services to create box for infinites lines in a given contexte.
    """
    def BeginParam(self,SegmentNum : int) -> float: 
        """
        None
        """
    def EndParam(self,SegmentNum : int) -> float: 
        """
        None
        """
    def Hypr2dBox(self,theHypr2d : OCP.gp.gp_Hypr2d,bounding : OCP.Bnd.Bnd_Box2d,boxHypr : OCP.Bnd.Bnd_Box2d) -> None: 
        """
        None
        """
    def HyprBox(self,theHypr : OCP.gp.gp_Hypr,bounding : OCP.Bnd.Bnd_Box,boxHypr : OCP.Bnd.Bnd_Box) -> None: 
        """
        None
        """
    def Lin2dBox(self,theLin2d : OCP.gp.gp_Lin2d,bounding : OCP.Bnd.Bnd_Box2d,boxLin : OCP.Bnd.Bnd_Box2d) -> None: 
        """
        None
        """
    def LinBox(self,theLin : OCP.gp.gp_Lin,bounding : OCP.Bnd.Bnd_Box,boxLin : OCP.Bnd.Bnd_Box) -> None: 
        """
        None
        """
    def NbSegments(self) -> int: 
        """
        None
        """
    def Parab2dBox(self,theParab2d : OCP.gp.gp_Parab2d,bounding : OCP.Bnd.Bnd_Box2d,boxHypr : OCP.Bnd.Bnd_Box2d) -> None: 
        """
        None
        """
    def ParabBox(self,theParab : OCP.gp.gp_Parab,bounding : OCP.Bnd.Bnd_Box,boxHypr : OCP.Bnd.Bnd_Box) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
Intf_EDGE: OCP.Intf.Intf_PIType # value = Intf_PIType.Intf_EDGE
Intf_EXTERNAL: OCP.Intf.Intf_PIType # value = Intf_PIType.Intf_EXTERNAL
Intf_FACE: OCP.Intf.Intf_PIType # value = Intf_PIType.Intf_FACE
Intf_VERTEX: OCP.Intf.Intf_PIType # value = Intf_PIType.Intf_VERTEX
