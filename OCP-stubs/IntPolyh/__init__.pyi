import OCP.IntPolyh
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.TColStd
import OCP.Bnd
import OCP.NCollection
__all__  = [
"IntPolyh_Couple",
"IntPolyh_CoupleMapHasher",
"IntPolyh_Edge",
"IntPolyh_Intersection",
"IntPolyh_ListOfCouples",
"IntPolyh_MaillageAffinage",
"IntPolyh_Point",
"IntPolyh_PointNormal",
"IntPolyh_SectionLine",
"IntPolyh_SeqOfStartPoints",
"IntPolyh_StartPoint",
"IntPolyh_Tools",
"IntPolyh_Triangle"
]
class IntPolyh_Couple():
    """
    The class represents the couple of indices with additional characteristics such as analyzed flag and an angle. In IntPolyh_MaillageAffinage algorithm the class is used as a couple of interfering triangles with the intersection angle.
    """
    def Angle(self) -> float: 
        """
        Returns the angle
        """
    def Dump(self,v : int) -> None: 
        """
        None
        """
    def FirstValue(self) -> int: 
        """
        Returns the first index
        """
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Computes a hash code for this couple, in the range [1, theUpperBound]
        """
    def IsAnalyzed(self) -> bool: 
        """
        Returns TRUE if the couple has been analyzed
        """
    def IsEqual(self,theOther : IntPolyh_Couple) -> bool: 
        """
        Returns true if the Couple is equal to <theOther>
        """
    def SecondValue(self) -> int: 
        """
        Returns the second index
        """
    def SetAnalyzed(self,theAnalyzed : bool) -> None: 
        """
        Sets the analyzed flag
        """
    def SetAngle(self,theAngle : float) -> None: 
        """
        Sets the angle
        """
    def SetCoupleValue(self,theInd1 : int,theInd2 : int) -> None: 
        """
        Sets the triangles
        """
    @overload
    def __init__(self,theTriangle1 : int,theTriangle2 : int,theAngle : float=-2.0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntPolyh_CoupleMapHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(theCouple : IntPolyh_Couple,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given couple, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theCouple1 : IntPolyh_Couple,theCouple2 : IntPolyh_Couple) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IntPolyh_Edge():
    """
    The class represents the edge built between the two IntPolyh points. It is linked to two IntPolyh triangles.
    """
    def Dump(self,v : int) -> None: 
        """
        None
        """
    def FirstPoint(self) -> int: 
        """
        Returns the first point
        """
    def FirstTriangle(self) -> int: 
        """
        Returns the first triangle
        """
    def SecondPoint(self) -> int: 
        """
        Returns the second point
        """
    def SecondTriangle(self) -> int: 
        """
        Returns the second triangle
        """
    def SetFirstPoint(self,thePoint : int) -> None: 
        """
        Sets the first point
        """
    def SetFirstTriangle(self,theTriangle : int) -> None: 
        """
        Sets the first triangle
        """
    def SetSecondPoint(self,thePoint : int) -> None: 
        """
        Sets the second point
        """
    def SetSecondTriangle(self,theTriangle : int) -> None: 
        """
        Sets the second triangle
        """
    @overload
    def __init__(self,thePoint1 : int,thePoint2 : int,theTriangle1 : int,theTriangle2 : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntPolyh_Intersection():
    """
    API algorithm for intersection of two surfaces by intersection of their triangulations.
    """
    def GetLinePoint(self,IndexLine : int,IndexPoint : int) -> Tuple[float, float, float, float, float, float, float, float]: 
        """
        Gets the parameters of the point in section line
        """
    def GetTangentZonePoint(self,IndexLine : int,IndexPoint : int) -> Tuple[float, float, float, float, float, float, float]: 
        """
        Gets the parameters of the point in tangent zone
        """
    def IsDone(self) -> bool: 
        """
        Returns state of the operation
        """
    def NbPointsInLine(self,IndexLine : int) -> int: 
        """
        Returns the number of points in the given line
        """
    def NbPointsInTangentZone(self,arg1 : int) -> int: 
        """
        Returns number of points in tangent zone
        """
    def NbSectionLines(self) -> int: 
        """
        Returns the number of section lines
        """
    def NbTangentZones(self) -> int: 
        """
        None
        """
    @overload
    def __init__(self,theS1 : OCP.Adaptor3d.Adaptor3d_HSurface,theNbSU1 : int,theNbSV1 : int,theS2 : OCP.Adaptor3d.Adaptor3d_HSurface,theNbSU2 : int,theNbSV2 : int) -> None: ...
    @overload
    def __init__(self,theS1 : OCP.Adaptor3d.Adaptor3d_HSurface,theS2 : OCP.Adaptor3d.Adaptor3d_HSurface) -> None: ...
    @overload
    def __init__(self,theS1 : OCP.Adaptor3d.Adaptor3d_HSurface,theUPars1 : OCP.TColStd.TColStd_Array1OfReal,theVPars1 : OCP.TColStd.TColStd_Array1OfReal,theS2 : OCP.Adaptor3d.Adaptor3d_HSurface,theUPars2 : OCP.TColStd.TColStd_Array1OfReal,theVPars2 : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    pass
class IntPolyh_ListOfCouples(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntPolyh_Couple) -> IntPolyh_Couple: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : IntPolyh_ListOfCouples) -> None: ...
    @overload
    def Append(self,theItem : IntPolyh_Couple,theIter : Any) -> None: ...
    def Assign(self,theOther : IntPolyh_ListOfCouples) -> IntPolyh_ListOfCouples: 
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
    def First(self) -> IntPolyh_Couple: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : IntPolyh_Couple,theIter : Any) -> IntPolyh_Couple: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : IntPolyh_ListOfCouples,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : IntPolyh_Couple,theIter : Any) -> IntPolyh_Couple: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : IntPolyh_ListOfCouples,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> IntPolyh_Couple: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : IntPolyh_ListOfCouples) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : IntPolyh_Couple) -> IntPolyh_Couple: ...
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
    def __init__(self,theOther : IntPolyh_ListOfCouples) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IntPolyh_MaillageAffinage():
    """
    Low-level algorithm to compute intersection of the surfaces by computing the intersection of their triangulations.
    """
    @overload
    def CommonBox(self) -> None: 
        """
        Looks for the common box of the surfaces and marks the points of the surfaces inside that common box for possible intersection

        Compute the common box witch is the intersection of the two bounding boxes, and mark the points of the two surfaces that are inside.
        """
    @overload
    def CommonBox(self,B1 : OCP.Bnd.Bnd_Box,B2 : OCP.Bnd.Bnd_Box) -> Tuple[float, float, float, float, float, float]: ...
    def CommonPartRefinement(self) -> None: 
        """
        Refine systematicaly all marked triangles of both surfaces
        """
    def ComputeDeflections(self,SurfID : int) -> None: 
        """
        Compute deflection for all triangles of one surface,and sort min and max of deflections
        """
    def FillArrayOfEdges(self,SurfID : int) -> None: 
        """
        Compute edges from the array of points
        """
    @overload
    def FillArrayOfPnt(self,SurfID : int,Upars : OCP.TColStd.TColStd_Array1OfReal,Vpars : OCP.TColStd.TColStd_Array1OfReal,theDeflTol : float=None) -> None: 
        """
        Computes points on one surface and fills an array of points; standard (default) method

        isShiftFwd flag is added. The purpose is to define shift of points along normal to the surface in this point. The shift length represents maximal deflection of triangulation. The direction (forward or reversed regarding to normal direction) is defined by isShiftFwd flag. Compute points on one surface and fill an array of points; advanced method

        Compute points on one surface and fill an array of points; If given, <theDeflTol> is the deflection tolerance of the given sampling. standard (default) method

        isShiftFwd flag is added. The purpose is to define shift of points along normal to the surface in this point. The shift length represents maximal deflection of triangulation. The direction (forward or reversed regarding to normal direction) is defined by isShiftFwd flag. Compute points on one surface and fill an array of points; If given, <theDeflTol> is the deflection tolerance of the given sampling. advanced method

        Fills the array of points for the surface taking into account the shift
        """
    @overload
    def FillArrayOfPnt(self,SurfID : int,isShiftFwd : bool) -> None: ...
    @overload
    def FillArrayOfPnt(self,SurfID : int,isShiftFwd : bool,thePoints : Any,theUPars : OCP.TColStd.TColStd_Array1OfReal,theVPars : OCP.TColStd.TColStd_Array1OfReal,theDeflTol : float) -> None: ...
    @overload
    def FillArrayOfPnt(self,SurfID : int,isShiftFwd : bool,Upars : OCP.TColStd.TColStd_Array1OfReal,Vpars : OCP.TColStd.TColStd_Array1OfReal,theDeflTol : float=None) -> None: ...
    @overload
    def FillArrayOfPnt(self,SurfID : int) -> None: ...
    def FillArrayOfTriangles(self,SurfID : int) -> None: 
        """
        Compute triangles from the array of points, and -- mark the triangles that use marked points by the CommonBox function.
        """
    def GetArrayOfEdges(self,SurfID : int) -> Any: 
        """
        None
        """
    def GetArrayOfPoints(self,SurfID : int) -> Any: 
        """
        None
        """
    def GetArrayOfTriangles(self,SurfID : int) -> Any: 
        """
        None
        """
    def GetBox(self,SurfID : int) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def GetCouples(self) -> IntPolyh_ListOfCouples: 
        """
        This method returns list of couples of contact triangles.
        """
    def GetEnlargeZone(self) -> bool: 
        """
        None
        """
    def GetMaxDeflection(self,SurfID : int) -> float: 
        """
        returns FlecheMax
        """
    def GetMinDeflection(self,SurfID : int) -> float: 
        """
        returns FlecheMin
        """
    def GetNextChainStartPoint(self,SPInit : IntPolyh_StartPoint,SPNext : IntPolyh_StartPoint,MySectionLine : IntPolyh_SectionLine,TTangentZones : Any,Prepend : bool=False) -> int: 
        """
        Mainly used by StartPointsChain(), this function try to compute the next StartPoint.
        """
    def LocalSurfaceRefinement(self,SurfId : int) -> None: 
        """
        Refine systematicaly all marked triangles of ONE surface
        """
    def MakeSampling(self,SurfID : int,theUPars : OCP.TColStd.TColStd_Array1OfReal,theVPars : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Makes the sampling of the surface - Fills the arrays with the parametric values of the sampling points (triangulation nodes).
        """
    def NextStartingPointsResearch(self,T1 : int,T2 : int,SPInit : IntPolyh_StartPoint,SPNext : IntPolyh_StartPoint) -> int: 
        """
        from two triangles and an intersection point I seach the other point (if it exist). This function is used by StartPointChain
        """
    def SetEnlargeZone(self,EnlargeZone : bool) -> None: 
        """
        None
        """
    def StartPointsChain(self,TSectionLines : Any,TTangentZones : Any) -> int: 
        """
        Loop on the array of couples. Compute StartPoints. Try to chain the StartPoints into SectionLines or put the point in the ArrayOfTangentZones if chaining it, is not possible.
        """
    def StartingPointsResearch(self,T1 : int,T2 : int,SP1 : IntPolyh_StartPoint,SP2 : IntPolyh_StartPoint) -> int: 
        """
        From two triangles compute intersection points. If I found more than two intersection points that's mean that those triangle are coplanar
        """
    def TriContact(self,P1 : IntPolyh_Point,P2 : IntPolyh_Point,P3 : IntPolyh_Point,Q1 : IntPolyh_Point,Q2 : IntPolyh_Point,Q3 : IntPolyh_Point,Angle : float) -> int: 
        """
        This fonction Check if two triangles are in contact or no, return 1 if yes, return 0 if no.
        """
    def TriangleCompare(self) -> int: 
        """
        Analyse each couple of triangles from the two -- array of triangles, to see if they are in contact, and compute the incidence. Then put couples in contact in the array of couples
        """
    def TriangleEdgeContact(self,TriSurfID : int,EdgeIndice : int,Tri1 : IntPolyh_Triangle,Tri2 : IntPolyh_Triangle,P1 : IntPolyh_Point,P2 : IntPolyh_Point,P3 : IntPolyh_Point,C1 : IntPolyh_Point,C2 : IntPolyh_Point,C3 : IntPolyh_Point,Pe1 : IntPolyh_Point,Pe2 : IntPolyh_Point,E : IntPolyh_Point,N : IntPolyh_Point,SP1 : IntPolyh_StartPoint,SP2 : IntPolyh_StartPoint) -> int: 
        """
        None
        """
    def TrianglesDeflectionsRefinementBSB(self) -> None: 
        """
        Refine both surfaces using BoundSortBox as -- rejection. The criterions used to refine a -- triangle are: The deflection The size of the -- bounding boxes (one surface may be very small compared to the other)
        """
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_HSurface,NbSU1 : int,NbSV1 : int,S2 : OCP.Adaptor3d.Adaptor3d_HSurface,NbSU2 : int,NbSV2 : int,PRINT : int) -> None: ...
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_HSurface,S2 : OCP.Adaptor3d.Adaptor3d_HSurface,PRINT : int) -> None: ...
    pass
class IntPolyh_Point():
    """
    The class represents the point on the surface with both 3D and 2D points.
    """
    def Add(self,P1 : IntPolyh_Point) -> IntPolyh_Point: 
        """
        Addition
        """
    def Cross(self,P1 : IntPolyh_Point,P2 : IntPolyh_Point) -> None: 
        """
        Cross
        """
    def Degenerated(self) -> bool: 
        """
        Returns the degenerated flag
        """
    def Divide(self,rr : float) -> IntPolyh_Point: 
        """
        Division
        """
    def Dot(self,P2 : IntPolyh_Point) -> float: 
        """
        Dot
        """
    @overload
    def Dump(self,i : int) -> None: 
        """
        Dump

        Dump
        """
    @overload
    def Dump(self) -> None: ...
    def Equal(self,Pt : IntPolyh_Point) -> None: 
        """
        Assignment operator
        """
    def Middle(self,MySurface : OCP.Adaptor3d.Adaptor3d_HSurface,P1 : IntPolyh_Point,P2 : IntPolyh_Point) -> None: 
        """
        Creates middle point from P1 and P2 and stores it to this
        """
    def Multiplication(self,rr : float) -> IntPolyh_Point: 
        """
        Multiplication
        """
    def PartOfCommon(self) -> int: 
        """
        Returns 0 if the point is not common with the other surface
        """
    def Set(self,x : float,y : float,z : float,u : float,v : float,II : int=1) -> None: 
        """
        Sets the point
        """
    def SetDegenerated(self,theFlag : bool) -> None: 
        """
        Sets the degenerated flag
        """
    def SetPartOfCommon(self,ii : int) -> None: 
        """
        Sets the part of common
        """
    def SetU(self,u : float) -> None: 
        """
        Sets the U coordinate for the 2D point
        """
    def SetV(self,v : float) -> None: 
        """
        Sets the V coordinate for the 2D point
        """
    def SetX(self,x : float) -> None: 
        """
        Sets the X coordinate for the 3D point
        """
    def SetY(self,y : float) -> None: 
        """
        Sets the Y coordinate for the 3D point
        """
    def SetZ(self,z : float) -> None: 
        """
        Sets the Z coordinate for the 3D point
        """
    def SquareDistance(self,P2 : IntPolyh_Point) -> float: 
        """
        Square distance to the other point
        """
    def SquareModulus(self) -> float: 
        """
        Square modulus
        """
    def Sub(self,P1 : IntPolyh_Point) -> IntPolyh_Point: 
        """
        Subtraction
        """
    def U(self) -> float: 
        """
        Returns the U coordinate of the 2D point
        """
    def V(self) -> float: 
        """
        Returns the V coordinate of the 2D point
        """
    def X(self) -> float: 
        """
        Returns X coordinate of the 3D point
        """
    def Y(self) -> float: 
        """
        Returns Y coordinate of the 3D point
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate of the 3D point
        """
    def __add__(self,P1 : IntPolyh_Point) -> IntPolyh_Point: 
        """
        None
        """
    @overload
    def __init__(self,x : float,y : float,z : float,u : float,v : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __mul__(self,rr : float) -> IntPolyh_Point: 
        """
        None
        """
    def __rmul__(self,rr : float) -> IntPolyh_Point: 
        """
        None
        """
    def __sub__(self,P1 : IntPolyh_Point) -> IntPolyh_Point: 
        """
        None
        """
    def __truediv__(self,rr : float) -> IntPolyh_Point: 
        """
        None
        """
    pass
class IntPolyh_PointNormal():
    """
    Auxiliary structure to represent pair of point and normal vector in this point on the surface.
    """
    def __init__(self) -> None: ...
    @property
    def Normal(self) -> OCP.gp.gp_Vec:
        """
        :type: OCP.gp.gp_Vec
        """
    @Normal.setter
    def Normal(self, arg0: OCP.gp.gp_Vec) -> None:
        pass
    @property
    def Point(self) -> OCP.gp.gp_Pnt:
        """
        :type: OCP.gp.gp_Pnt
        """
    @Point.setter
    def Point(self, arg0: OCP.gp.gp_Pnt) -> None:
        pass
    pass
class IntPolyh_SectionLine():
    """
    None
    """
    def ChangeValue(self,nn : int) -> IntPolyh_StartPoint: 
        """
        None
        """
    def Copy(self,Other : IntPolyh_SectionLine) -> IntPolyh_SectionLine: 
        """
        None
        """
    def Destroy(self) -> None: 
        """
        None
        """
    def Dump(self) -> None: 
        """
        None
        """
    def GetN(self) -> int: 
        """
        None
        """
    def IncrementNbStartPoints(self) -> None: 
        """
        None
        """
    def Init(self,nn : int) -> None: 
        """
        None
        """
    def NbStartPoints(self) -> int: 
        """
        None
        """
    def Prepend(self,SP : IntPolyh_StartPoint) -> None: 
        """
        None
        """
    def Value(self,nn : int) -> IntPolyh_StartPoint: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,nn : int) -> None: ...
    pass
class IntPolyh_SeqOfStartPoints(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntPolyh_StartPoint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntPolyh_SeqOfStartPoints) -> None: ...
    def Assign(self,theOther : IntPolyh_SeqOfStartPoints) -> IntPolyh_SeqOfStartPoints: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntPolyh_StartPoint: 
        """
        First item access
        """
    def ChangeLast(self) -> IntPolyh_StartPoint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntPolyh_StartPoint: 
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
    def First(self) -> IntPolyh_StartPoint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntPolyh_SeqOfStartPoints) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntPolyh_StartPoint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntPolyh_StartPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntPolyh_SeqOfStartPoints) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntPolyh_StartPoint: 
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
    def Prepend(self,theSeq : IntPolyh_SeqOfStartPoints) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntPolyh_StartPoint) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntPolyh_StartPoint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntPolyh_SeqOfStartPoints) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntPolyh_StartPoint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : IntPolyh_SeqOfStartPoints) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntPolyh_StartPoint():
    """
    None
    """
    def ChainList(self) -> int: 
        """
        None
        """
    def CheckSameSP(self,SP : IntPolyh_StartPoint) -> int: 
        """
        None
        """
    @overload
    def Dump(self,i : int) -> None: 
        """
        None

        None
        """
    @overload
    def Dump(self) -> None: ...
    def E1(self) -> int: 
        """
        None
        """
    def E2(self) -> int: 
        """
        None
        """
    def GetAngle(self) -> float: 
        """
        None
        """
    def GetEdgePoints(self,Triangle : IntPolyh_Triangle,FirstEdgePoint : int,SecondEdgePoint : int,LastPoint : int) -> int: 
        """
        None
        """
    def Lambda1(self) -> float: 
        """
        None
        """
    def Lambda2(self) -> float: 
        """
        None
        """
    def SetAngle(self,ang : float) -> None: 
        """
        None
        """
    def SetChainList(self,ChList : int) -> None: 
        """
        None
        """
    def SetCoupleValue(self,IT1 : int,IT2 : int) -> None: 
        """
        None
        """
    def SetEdge1(self,IE1 : int) -> None: 
        """
        None
        """
    def SetEdge2(self,IE2 : int) -> None: 
        """
        None
        """
    def SetLambda1(self,LAM1 : float) -> None: 
        """
        None
        """
    def SetLambda2(self,LAM2 : float) -> None: 
        """
        None
        """
    def SetUV1(self,UU1 : float,VV1 : float) -> None: 
        """
        None
        """
    def SetUV2(self,UU2 : float,VV2 : float) -> None: 
        """
        None
        """
    def SetXYZ(self,XX : float,YY : float,ZZ : float) -> None: 
        """
        None
        """
    def T1(self) -> int: 
        """
        None
        """
    def T2(self) -> int: 
        """
        None
        """
    def U1(self) -> float: 
        """
        None
        """
    def U2(self) -> float: 
        """
        None
        """
    def V1(self) -> float: 
        """
        None
        """
    def V2(self) -> float: 
        """
        None
        """
    def X(self) -> float: 
        """
        None
        """
    def Y(self) -> float: 
        """
        None
        """
    def Z(self) -> float: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,xx : float,yy : float,zz : float,uu1 : float,vv1 : float,uu2 : float,vv2 : float,T1 : int,E1 : int,LAM1 : float,T2 : int,E2 : int,LAM2 : float,List : int) -> None: ...
    pass
class IntPolyh_Tools():
    """
    The class provides tools for surface sampling.
    """
    @staticmethod
    def ComputeDeflection_s(theSurf : OCP.Adaptor3d.Adaptor3d_HSurface,theUPars : OCP.TColStd.TColStd_Array1OfReal,theVPars : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Computes the deflection tolerance on the surface for the given sampling.
        """
    @staticmethod
    def FillArrayOfPointNormal_s(theSurf : OCP.Adaptor3d.Adaptor3d_HSurface,theUPars : OCP.TColStd.TColStd_Array1OfReal,theVPars : OCP.TColStd.TColStd_Array1OfReal,thePoints : Any) -> None: 
        """
        Fills the array <thePoints> with the points (triangulation nodes) on the surface and normal directions of the surface in these points.
        """
    @staticmethod
    def IsEnlargePossible_s(theSurf : OCP.Adaptor3d.Adaptor3d_HSurface) -> Tuple[bool, bool]: 
        """
        Checks if the surface can be enlarged in U or V direction.
        """
    @staticmethod
    def MakeSampling_s(theSurf : OCP.Adaptor3d.Adaptor3d_HSurface,theNbSU : int,theNbSV : int,theEnlargeZone : bool,theUPars : OCP.TColStd.TColStd_Array1OfReal,theVPars : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Makes the sampling of the given surface <theSurf> making the net of <theNbSU> x <theNbSV> sampling points. The flag <theEnlargeZone> controls the enlargement of the sampling zone on the surface. The parameters of the sampling points are stored into <theUPars> and <theVPars> arrays.
        """
    def __init__(self) -> None: ...
    pass
class IntPolyh_Triangle():
    """
    The class represents the triangle built from three IntPolyh points and three IntPolyh edges.
    """
    def BoundingBox(self,thePoints : Any) -> OCP.Bnd.Bnd_Box: 
        """
        Returns the bounding box of the triangle.
        """
    def ComputeDeflection(self,theSurface : OCP.Adaptor3d.Adaptor3d_HSurface,thePoints : Any) -> float: 
        """
        Computes the deflection for the triangle
        """
    def Deflection(self) -> float: 
        """
        Returns the deflection of the triangle
        """
    def Dump(self,v : int) -> None: 
        """
        Dumps the contents of the triangle.
        """
    def FirstEdge(self) -> int: 
        """
        Returns the first edge
        """
    def FirstEdgeOrientation(self) -> int: 
        """
        Returns the orientation of the first edge
        """
    def FirstPoint(self) -> int: 
        """
        Returns the first point
        """
    def GetEdgeNumber(self,theEdgeIndex : int) -> int: 
        """
        Gets the edge number by the index
        """
    def GetEdgeOrientation(self,theEdgeIndex : int) -> int: 
        """
        Gets the edges orientation by the index
        """
    def GetNextTriangle(self,theTriangle : int,theEdgeNum : int,TEdges : Any) -> int: 
        """
        Gets the adjacent triangle
        """
    def HasIntersection(self) -> bool: 
        """
        Returns true if the triangle has interfered the other triangle
        """
    def IsDegenerated(self) -> bool: 
        """
        Returns the Degenerated flag
        """
    def IsIntersectionPossible(self) -> bool: 
        """
        Returns possibility of the intersection
        """
    def LinkEdges2Triangle(self,TEdges : Any,theEdge1 : int,theEdge2 : int,theEdge3 : int) -> None: 
        """
        Links edges to triangle
        """
    def MiddleRefinement(self,theTriangleNumber : int,theSurface : OCP.Adaptor3d.Adaptor3d_HSurface,TPoints : Any,TTriangles : Any,TEdges : Any) -> None: 
        """
        Splits the triangle on two to decrease its deflection
        """
    def MultipleMiddleRefinement(self,theRefineCriterion : float,theBox : OCP.Bnd.Bnd_Box,theTriangleNumber : int,theSurface : OCP.Adaptor3d.Adaptor3d_HSurface,TPoints : Any,TTriangles : Any,TEdges : Any) -> None: 
        """
        Splits the current triangle and new triangles until the refinement criterion is not achieved
        """
    def SecondEdge(self) -> int: 
        """
        Returns the second edge
        """
    def SecondEdgeOrientation(self) -> int: 
        """
        Returns the orientation of the second edge
        """
    def SecondPoint(self) -> int: 
        """
        Returns the second point
        """
    def SetDeflection(self,theDeflection : float) -> None: 
        """
        Sets the deflection
        """
    def SetDegenerated(self,theDegFlag : bool) -> None: 
        """
        Sets the degenerated flag
        """
    def SetEdge(self,theEdgeIndex : int,theEdgeNumber : int) -> None: 
        """
        Sets the edge by the index
        """
    def SetEdgeAndOrientation(self,theEdge : IntPolyh_Edge,theEdgeIndex : int) -> None: 
        """
        Sets the appropriate edge and orientation for the triangle.
        """
    def SetEdgeOrientation(self,theEdgeIndex : int,theEdgeOrientation : int) -> None: 
        """
        Sets the edges orientation by the index
        """
    def SetFirstEdge(self,theEdge : int,theEdgeOrientation : int) -> None: 
        """
        Sets the first edge
        """
    def SetFirstPoint(self,thePoint : int) -> None: 
        """
        Sets the first point
        """
    def SetIntersection(self,theInt : bool) -> None: 
        """
        Sets the flag of intersection
        """
    def SetIntersectionPossible(self,theIP : bool) -> None: 
        """
        Sets the flag of possibility of intersection
        """
    def SetSecondEdge(self,theEdge : int,theEdgeOrientation : int) -> None: 
        """
        Sets the second edge
        """
    def SetSecondPoint(self,thePoint : int) -> None: 
        """
        Sets the second point
        """
    def SetThirdEdge(self,theEdge : int,theEdgeOrientation : int) -> None: 
        """
        Sets the third edge
        """
    def SetThirdPoint(self,thePoint : int) -> None: 
        """
        Sets the third point
        """
    def ThirdEdge(self) -> int: 
        """
        Returns the third edge
        """
    def ThirdEdgeOrientation(self) -> int: 
        """
        Returns the orientation of the third edge
        """
    def ThirdPoint(self) -> int: 
        """
        Returns the third point
        """
    @overload
    def __init__(self,thePoint1 : int,thePoint2 : int,thePoint3 : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
