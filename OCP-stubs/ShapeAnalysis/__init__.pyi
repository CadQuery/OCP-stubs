import OCP.ShapeAnalysis
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.NCollection
import io
import OCP.Geom2d
import OCP.Standard
import OCP.ShapeExtend
import OCP.TopoDS
import OCP.Adaptor3d
import OCP.TColgp
import OCP.Bnd
import OCP.TopLoc
import OCP.gp
import OCP.Geom
import OCP.GeomAdaptor
import OCP.IntRes2d
import OCP.TColStd
__all__  = [
"ShapeAnalysis",
"ShapeAnalysis_BoxBndTree",
"ShapeAnalysis_CheckSmallFace",
"ShapeAnalysis_Curve",
"ShapeAnalysis_DataMapOfShapeListOfReal",
"ShapeAnalysis_Edge",
"ShapeAnalysis_FreeBoundData",
"ShapeAnalysis_FreeBounds",
"ShapeAnalysis_FreeBoundsProperties",
"ShapeAnalysis_Geom",
"ShapeAnalysis_SequenceOfFreeBounds",
"ShapeAnalysis_HSequenceOfFreeBounds",
"ShapeAnalysis_ShapeContents",
"ShapeAnalysis_ShapeTolerance",
"ShapeAnalysis_Shell",
"ShapeAnalysis_Surface",
"ShapeAnalysis_TransferParameters",
"ShapeAnalysis_TransferParametersProj",
"ShapeAnalysis_Wire",
"ShapeAnalysis_WireOrder",
"ShapeAnalysis_WireVertex"
]
class ShapeAnalysis():
    """
    This package is intended to analyze geometrical objects and topological shapes. Analysis domain includes both exploring geometrical and topological properties of shapes and checking their conformance to Open CASCADE requirements. The directions of analysis provided by tools of this package are: computing quantities of subshapes, computing parameters of points on curve and surface, computing surface singularities, checking edge and wire consistency, checking edges order in the wire, checking face bounds orientation, checking small faces, analyzing shape tolerances, analyzing of free bounds of the shape.
    """
    @staticmethod
    def AdjustByPeriod_s(Val : float,ToVal : float,Period : float) -> float: 
        """
        Returns a shift required to move point <Val> to the range [ToVal-Period/2,ToVal+Period/2]. This shift will be the divisible by Period. Intended for adjusting parameters on periodic surfaces.
        """
    @staticmethod
    def AdjustToPeriod_s(Val : float,ValMin : float,ValMax : float) -> float: 
        """
        Returns a shift required to move point <Val> to the range [ValMin,ValMax]. This shift will be the divisible by Period with Period = ValMax - ValMin. Intended for adjusting parameters on periodic surfaces.
        """
    @staticmethod
    def ContourArea_s(theWire : OCP.TopoDS.TopoDS_Wire) -> float: 
        """
        Returns a total area of 3d wire
        """
    @staticmethod
    def FindBounds_s(shape : OCP.TopoDS.TopoDS_Shape,V1 : OCP.TopoDS.TopoDS_Vertex,V2 : OCP.TopoDS.TopoDS_Vertex) -> None: 
        """
        Finds the start and end vertices of the shape Shape can be of the following type: vertex: V1 and V2 are the same and equal to <shape>, edge : V1 is start and V2 is end vertex (see ShapeAnalysis_Edge methods FirstVertex and LastVertex), wire : V1 is start vertex of the first edge, V2 is end vertex of the last edge (also see ShapeAnalysis_Edge). If wire contains no edges V1 and V2 are nullified If none of the above V1 and V2 are nullified
        """
    @staticmethod
    def GetFaceUVBounds_s(F : OCP.TopoDS.TopoDS_Face) -> Tuple[float, float, float, float]: 
        """
        Computes exact UV bounds of all wires on the face
        """
    @staticmethod
    def IsOuterBound_s(face : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Returns True if <F> has outer bound.
        """
    @staticmethod
    def OuterWire_s(face : OCP.TopoDS.TopoDS_Face) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the outer wire on the face <Face>. This is replacement of the method BRepTools::OuterWire until it works badly. Returns the first wire oriented as outer according to FClass2d_Classifier. If none, last wire is returned.
        """
    @staticmethod
    def TotCross2D_s(sewd : OCP.ShapeExtend.ShapeExtend_WireData,aFace : OCP.TopoDS.TopoDS_Face) -> float: 
        """
        Returns a total area of 2d wire
        """
    def __init__(self) -> None: ...
    pass
class ShapeAnalysis_BoxBndTree():
    """
    The algorithm of unbalanced binary tree of overlapped bounding boxes.
    """
    def Add(self,theObj : int,theBnd : OCP.Bnd.Bnd_Box) -> bool: 
        """
        Update the tree with a new object and its bounding box.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Recommended to be used only in sub-classes.
        """
    def Clear(self,aNewAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clears the contents of the tree.
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class ShapeAnalysis_CheckSmallFace():
    """
    Analysis of the face size
    """
    def CheckPin(self,F : OCP.TopoDS.TopoDS_Face,whatrow : int,sence : int) -> bool: 
        """
        Checks if a Face has a pin, which can be edited No singularity : no pin, returns 0 If there is a pin, checked topics, with returned value : - 0 : nothing to do more - 1 : "smooth", i.e. not a really sharp pin -> diagnostic "SmoothPin" - 2 : stretched pin, i.e. is possible to relimit the face by another vertex, so that this vertex still gives a pin -> diagnostic "StretchedPin" with location of vertex (Pnt)
        """
    def CheckPinEdges(self,theFirstEdge : OCP.TopoDS.TopoDS_Edge,theSecondEdge : OCP.TopoDS.TopoDS_Edge,coef1 : float,coef2 : float,toler : float) -> bool: 
        """
        None
        """
    def CheckPinFace(self,F : OCP.TopoDS.TopoDS_Face,mapEdges : OCP.TopTools.TopTools_DataMapOfShapeShape,toler : float=-1.0) -> bool: 
        """
        None
        """
    def CheckSingleStrip(self,F : OCP.TopoDS.TopoDS_Face,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,tol : float=-1.0) -> bool: 
        """
        Checks if a Face is a single strip, i.e. brings two great edges which are confused on their whole length, possible other edges are small or null length
        """
    def CheckSplittingVertices(self,F : OCP.TopoDS.TopoDS_Face,MapEdges : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,MapParam : ShapeAnalysis_DataMapOfShapeListOfReal,theAllVert : OCP.TopoDS.TopoDS_Compound) -> int: 
        """
        Checks if a Face brings vertices which split it, either confused with non adjacent vertices, or confused with their projection on non adjacent edges Returns the count of found splitting vertices Each vertex then brings a diagnostic "SplittingVertex", with data : "Face" for the face, "Edge" for the split edge
        """
    def CheckSpotFace(self,F : OCP.TopoDS.TopoDS_Face,tol : float=-1.0) -> bool: 
        """
        Acts as IsSpotFace, but records in <infos> a diagnostic "SpotFace" with the Pnt as value (data "Location")
        """
    def CheckStripEdges(self,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,tol : float,dmax : float) -> bool: 
        """
        Checks if two edges define a strip, i.e. distance maxi below tolerance, given or some of those of E1 and E2
        """
    def CheckStripFace(self,F : OCP.TopoDS.TopoDS_Face,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,tol : float=-1.0) -> bool: 
        """
        Checks if a Face is as a Strip Returns 0 if not or non determined, 1 if in U, 2 if in V By default, considers the tolerance zone of its edges A given value <tol> may be given to check a strip of max this width
        """
    def CheckTwisted(self,F : OCP.TopoDS.TopoDS_Face,paramu : float,paramv : float) -> bool: 
        """
        Checks if a Face is twisted (apart from checking Pin, i.e. it does not give information on pin, only "it is twisted")
        """
    def FindStripEdges(self,F : OCP.TopoDS.TopoDS_Face,E1 : OCP.TopoDS.TopoDS_Edge,E2 : OCP.TopoDS.TopoDS_Edge,tol : float,dmax : float) -> bool: 
        """
        Searches for two and only two edges up tolerance Returns True if OK, false if not 2 edges If True, returns the two edges and their maximum distance
        """
    def IsSpotFace(self,F : OCP.TopoDS.TopoDS_Face,spot : OCP.gp.gp_Pnt,spotol : float,tol : float=-1.0) -> int: 
        """
        Checks if a Face is as a Spot Returns 0 if not, 1 if yes, 2 if yes and all vertices are the same By default, considers the tolerance zone of its vertices A given value <tol> may be given to check a spot of this size If a Face is a Spot, its location is returned in <spot>, and <spotol> returns an equivalent tolerance, which is computed as half of max dimension of min-max box of the face
        """
    def IsStripSupport(self,F : OCP.TopoDS.TopoDS_Face,tol : float=-1.0) -> bool: 
        """
        Checks if a Face lies on a Surface which is a strip So the Face is a strip. But a Face may be a strip elsewhere ..
        """
    def SetTolerance(self,tol : float) -> None: 
        """
        Sets a fixed Tolerance to check small face By default, local tolerance zone is considered Sets a fixed MaxTolerance to check small face Sets a fixed Tolerance to check small face By default, local tolerance zone is considered Unset fixed tolerance, comes back to local tolerance zones Unset fixed tolerance, comes back to local tolerance zones

        Sets a fixed Tolerance to check small face By default, local tolerance zone is considered Sets a fixed MaxTolerance to check small face Sets a fixed Tolerance to check small face By default, local tolerance zone is considered Unset fixed tolerance, comes back to local tolerance zones Unset fixed tolerance, comes back to local tolerance zones
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status of last call to Perform() ShapeExtend_OK : face was OK, nothing done ShapeExtend_DONE1: some wires are fixed ShapeExtend_DONE2: orientation of wires fixed ShapeExtend_DONE3: missing seam added ShapeExtend_DONE4: small area wire removed ShapeExtend_DONE5: natural bounds added ShapeExtend_FAIL1: some fails during fixing wires ShapeExtend_FAIL2: cannot fix orientation of wires ShapeExtend_FAIL3: cannot add missing seam ShapeExtend_FAIL4: cannot remove small area wire

        Returns the status of last call to Perform() ShapeExtend_OK : face was OK, nothing done ShapeExtend_DONE1: some wires are fixed ShapeExtend_DONE2: orientation of wires fixed ShapeExtend_DONE3: missing seam added ShapeExtend_DONE4: small area wire removed ShapeExtend_DONE5: natural bounds added ShapeExtend_FAIL1: some fails during fixing wires ShapeExtend_FAIL2: cannot fix orientation of wires ShapeExtend_FAIL3: cannot add missing seam ShapeExtend_FAIL4: cannot remove small area wire
        """
    def StatusPin(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusPinEdges(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusPinFace(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusSplitVert(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusSpot(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusStrip(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusTwisted(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def Tolerance(self) -> float: 
        """
        Returns the tolerance to check small faces, negative value if local tolerances zones are to be considered

        Returns the tolerance to check small faces, negative value if local tolerances zones are to be considered
        """
    def __init__(self) -> None: ...
    pass
class ShapeAnalysis_Curve():
    """
    Analyzing tool for 2d or 3d curve. Computes parameters of projected point onto a curve.
    """
    def FillBndBox(self,C2d : OCP.Geom2d.Geom2d_Curve,First : float,Last : float,NPoints : int,Exact : bool,Box : OCP.Bnd.Bnd_Box2d) -> None: 
        """
        Computes a boundary box on segment of curve C2d from First to Last. This is done by taking NPoints points from the curve and, if Exact is True, by searching for exact extrema. All these points are added to Box.
        """
    @staticmethod
    @overload
    def GetSamplePoints_s(curve : OCP.Geom.Geom_Curve,first : float,last : float,seq : OCP.TColgp.TColgp_SequenceOfPnt) -> bool: 
        """
        Returns sample points which will serve as linearisation of the2d curve in range (first, last) The distribution of sample points is consystent with what is used by BRepTopAdaptor_FClass2d

        Returns sample points which will serve as linearisation of the curve in range (first, last)
        """
    @staticmethod
    @overload
    def GetSamplePoints_s(curve : OCP.Geom2d.Geom2d_Curve,first : float,last : float,seq : OCP.TColgp.TColgp_SequenceOfPnt2d) -> bool: ...
    @staticmethod
    def IsClosed_s(curve : OCP.Geom.Geom_Curve,preci : float=-1.0) -> bool: 
        """
        Tells if the Curve is closed with given precision. If <preci> < 0 then Precision::Confusion is used.
        """
    @staticmethod
    @overload
    def IsPeriodic_s(curve : OCP.Geom.Geom_Curve) -> bool: 
        """
        This method was implemented as fix for changes in trimmed curve behaviour. For the moment trimmed curve returns false anyway. So it is necessary to adapt all Data exchange tools for this behaviour. Current implementation takes into account that curve may be offset.

        The same as for Curve3d.
        """
    @staticmethod
    @overload
    def IsPeriodic_s(curve : OCP.Geom2d.Geom2d_Curve) -> bool: ...
    @staticmethod
    @overload
    def IsPlanar_s(curve : OCP.Geom.Geom_Curve,Normal : OCP.gp.gp_XYZ,preci : float=0.0) -> bool: 
        """
        Checks if points are planar with given preci. If Normal has not zero modulus, checks with given normal

        Checks if curve is planar with given preci. If Normal has not zero modulus, checks with given normal
        """
    @staticmethod
    @overload
    def IsPlanar_s(pnts : OCP.TColgp.TColgp_Array1OfPnt,Normal : OCP.gp.gp_XYZ,preci : float=0.0) -> bool: ...
    @overload
    def NextProject(self,paramPrev : float,C3D : OCP.Geom.Geom_Curve,P3D : OCP.gp.gp_Pnt,preci : float,proj : OCP.gp.gp_Pnt,param : float,cf : float,cl : float,AdjustToEnds : bool=True) -> float: 
        """
        Projects a Point on a Curve using Newton method. <paramPrev> is taken as the first approximation of solution. If Newton algorithm fails the method Project() is used. If AdjustToEnds is True, point will be adjusted to the end of the curve if distance is less than <preci>

        Projects a Point on a Curve using Newton method. <paramPrev> is taken as the first approximation of solution. If Newton algorithm fails the method Project() is used.
        """
    @overload
    def NextProject(self,paramPrev : float,C3D : OCP.Adaptor3d.Adaptor3d_Curve,P3D : OCP.gp.gp_Pnt,preci : float,proj : OCP.gp.gp_Pnt,param : float) -> float: ...
    @overload
    def Project(self,C3D : OCP.Geom.Geom_Curve,P3D : OCP.gp.gp_Pnt,preci : float,proj : OCP.gp.gp_Pnt,param : float,cf : float,cl : float,AdjustToEnds : bool=True) -> float: 
        """
        Projects a Point on a Curve. Computes the projected point and its parameter on the curve. <preci> is used as 3d precision (hence, 0 will produce reject unless exact confusion). The number of iterations is limited. If AdjustToEnds is True, point will be adjusted to the end of the curve if distance is less than <preci>

        Projects a Point on a Curve. Computes the projected point and its parameter on the curve. <preci> is used as 3d precision (hence, 0 will produce reject unless exact confusion). The number of iterations is limited.

        Projects a Point on a Curve, but parameters are limited between <cf> and <cl>. The range [cf, cl] is extended with help of Adaptor3d on the basis of 3d precision <preci>. If AdjustToEnds is True, point will be adjusted to the end of the curve if distance is less than <preci>
        """
    @overload
    def Project(self,C3D : OCP.Geom.Geom_Curve,P3D : OCP.gp.gp_Pnt,preci : float,proj : OCP.gp.gp_Pnt,param : float,AdjustToEnds : bool=True) -> float: ...
    @overload
    def Project(self,C3D : OCP.Adaptor3d.Adaptor3d_Curve,P3D : OCP.gp.gp_Pnt,preci : float,proj : OCP.gp.gp_Pnt,param : float,AdjustToEnds : bool=True) -> float: ...
    def ProjectAct(self,C3D : OCP.Adaptor3d.Adaptor3d_Curve,P3D : OCP.gp.gp_Pnt,preci : float,proj : OCP.gp.gp_Pnt,param : float) -> float: 
        """
        None
        """
    def SelectForwardSeam(self,C1 : OCP.Geom2d.Geom2d_Curve,C2 : OCP.Geom2d.Geom2d_Curve) -> int: 
        """
        Defines which pcurve (C1 or C2) should be chosen for FORWARD seam edge.
        """
    def ValidateRange(self,Crv : OCP.Geom.Geom_Curve,First : float,Last : float,prec : float) -> bool: 
        """
        Validate parameters First and Last for the given curve in order to make them valid for creation of edge. This includes: - limiting range [First,Last] by range of curve - adjusting range [First,Last] for periodic (or closed) curve if Last < First Returns True if parameters are OK or are successfully corrected, or False if parameters cannot be corrected. In the latter case, parameters are reset to range of curve.
        """
    def __init__(self) -> None: ...
    pass
class ShapeAnalysis_DataMapOfShapeListOfReal(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : ShapeAnalysis_DataMapOfShapeListOfReal) -> ShapeAnalysis_DataMapOfShapeListOfReal: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColStd.TColStd_ListOfReal) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColStd.TColStd_ListOfReal) -> OCP.TColStd.TColStd_ListOfReal: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_ListOfReal: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_ListOfReal: 
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
    def Exchange(self,theOther : ShapeAnalysis_DataMapOfShapeListOfReal) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_ListOfReal: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TColStd.TColStd_ListOfReal) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_ListOfReal: 
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
    def __init__(self,theOther : ShapeAnalysis_DataMapOfShapeListOfReal) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class ShapeAnalysis_Edge():
    """
    Tool for analyzing the edge. Queries geometrical representations of the edge (3d curve, pcurve on the given face or surface) and topological sub-shapes (bounding vertices). Provides methods for analyzing geometry and topology consistency (3d and pcurve(s) consistency, their adjacency to the vertices).
    """
    @overload
    def BoundUV(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location,first : OCP.gp.gp_Pnt2d,last : OCP.gp.gp_Pnt2d) -> bool: 
        """
        None

        Returns the ends of pcurve Calls method PCurve with <orient> equal to True
        """
    @overload
    def BoundUV(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face,first : OCP.gp.gp_Pnt2d,last : OCP.gp.gp_Pnt2d) -> bool: ...
    @overload
    def CheckCurve3dWithPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None

        Checks mutual orientation of 3d curve and pcurve on the analysis of curves bounding points
        """
    @overload
    def CheckCurve3dWithPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location) -> bool: ...
    def CheckOverlapping(self,theEdge1 : OCP.TopoDS.TopoDS_Edge,theEdge2 : OCP.TopoDS.TopoDS_Edge,theTolOverlap : float,theDomainDist : float=0.0) -> bool: 
        """
        Checks the first edge is overlapped with second edge. If distance between two edges is less then theTolOverlap edges are overlapped. theDomainDis - length of part of edges on which edges are overlapped.
        """
    def CheckPCurveRange(self,theFirst : float,theLast : float,thePC : OCP.Geom2d.Geom2d_Curve) -> bool: 
        """
        Checks possibility for pcurve thePC to have range [theFirst, theLast] (edge range) having respect to real first, last parameters of thePC
        """
    @overload
    def CheckSameParameter(self,theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face,theMaxdev : float,theNbControl : int=23) -> bool: 
        """
        Checks the edge to be SameParameter. Calculates the maximal deviation between 3d curve and each pcurve of the edge on <NbControl> equidistant points (the same algorithm as in BRepCheck; default value is 23 as in BRepCheck). This deviation is returned in <maxdev> parameter. If deviation is greater than tolerance of the edge (i.e. incorrect flag) returns False, else returns True.

        Checks the edge to be SameParameter. Calculates the maximal deviation between 3d curve and each pcurve of the edge on <NbControl> equidistant points (the same algorithm as in BRepCheck; default value is 23 as in BRepCheck). This deviation is returned in <maxdev> parameter. If deviation is greater than tolerance of the edge (i.e. incorrect flag) returns False, else returns True.
        """
    @overload
    def CheckSameParameter(self,edge : OCP.TopoDS.TopoDS_Edge,maxdev : float,NbControl : int=23) -> bool: ...
    @overload
    def CheckVertexTolerance(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face,toler1 : float,toler2 : float) -> bool: 
        """
        None

        Checks if it is necessary to increase tolerances of the edge vertices to comprise the ends of 3d curve and pcurve on the given face (first method) or all pcurves stored in an edge (second one) toler1 returns necessary tolerance for first vertex, toler2 returns necessary tolerance for last vertex.
        """
    @overload
    def CheckVertexTolerance(self,edge : OCP.TopoDS.TopoDS_Edge,toler1 : float,toler2 : float) -> bool: ...
    def CheckVerticesWithCurve3d(self,edge : OCP.TopoDS.TopoDS_Edge,preci : float=-1.0,vtx : int=0) -> bool: 
        """
        Checks the start and/or end vertex of the edge for matching with 3d curve with the given precision. <vtx> = 1 : start vertex only <vtx> = 2 : end vertex only <vtx> = 0 : both (default) If preci < 0 the vertices are considered with their own tolerances, else with the given <preci>.
        """
    @overload
    def CheckVerticesWithPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location,preci : float=-1.0,vtx : int=0) -> bool: 
        """
        None

        Checks the start and/or end vertex of the edge for matching with pcurve with the given precision. <vtx> = 1 : start vertex <vtx> = 2 : end vertex <vtx> = 0 : both If preci < 0 the vertices are considered with their own tolerances, else with the given <preci>.
        """
    @overload
    def CheckVerticesWithPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face,preci : float=-1.0,vtx : int=0) -> bool: ...
    def Curve3d(self,edge : OCP.TopoDS.TopoDS_Edge,C3d : OCP.Geom.Geom_Curve,cf : float,cl : float,orient : bool=True) -> bool: 
        """
        Returns the 3d curve and bounding parameteres for the edge Returns False if no 3d curve. If <orient> is True (default), takes orientation into account: if the edge is reversed, cf and cl are toggled
        """
    def FirstVertex(self,edge : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns start vertex of the edge (taking edge orientation into account).
        """
    @overload
    def GetEndTangent2d(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location,atEnd : bool,pos : OCP.gp.gp_Pnt2d,tang : OCP.gp.gp_Vec2d,dparam : float=0.0) -> bool: 
        """
        None

        Returns tangent of the edge pcurve at its start (if atEnd is False) or end (if True), regarding the orientation of edge. If edge is REVERSED, tangent is reversed before return. Returns True if pcurve is available and tangent is computed and is not null, else False.
        """
    @overload
    def GetEndTangent2d(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face,atEnd : bool,pos : OCP.gp.gp_Pnt2d,tang : OCP.gp.gp_Vec2d,dparam : float=0.0) -> bool: ...
    def HasCurve3d(self,edge : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Tells if the edge has a 3d curve
        """
    @overload
    def HasPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        Tells if the Edge has a pcurve on the face.

        Tells if the edge has a pcurve on the surface (with location).
        """
    @overload
    def HasPCurve(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face) -> bool: ...
    def IsClosed3d(self,edge : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Gives True if the edge has a 3d curve, this curve is closed, and the edge has the same vertex at start and end
        """
    @overload
    def IsSeam(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location) -> bool: 
        """
        None

        Returns True if the edge has two pcurves on one surface
        """
    @overload
    def IsSeam(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face) -> bool: ...
    def LastVertex(self,edge : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Returns end vertex of the edge (taking edge orientation into account).
        """
    @overload
    def PCurve(self,edge : OCP.TopoDS.TopoDS_Edge,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location,C2d : OCP.Geom2d.Geom2d_Curve,cf : float,cl : float,orient : bool=True) -> bool: 
        """
        None

        Returns the pcurve and bounding parameteres for the edge lying on the surface. Returns False if the edge has no pcurve on this surface. If <orient> is True (default), takes orientation into account: if the edge is reversed, cf and cl are toggled
        """
    @overload
    def PCurve(self,edge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face,C2d : OCP.Geom2d.Geom2d_Curve,cf : float,cl : float,orient : bool=True) -> bool: ...
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status (in the form of True/False) of last Check
        """
    def __init__(self) -> None: ...
    pass
class ShapeAnalysis_FreeBoundData(OCP.Standard.Standard_Transient):
    """
    This class is intended to represent free bound and to store its properties.This class is intended to represent free bound and to store its properties.This class is intended to represent free bound and to store its properties.
    """
    def AddNotch(self,notch : OCP.TopoDS.TopoDS_Wire,width : float) -> None: 
        """
        Adds notch on the contour with its maximum width
        """
    def Area(self) -> float: 
        """
        Returns area of the contour

        Returns area of the contour
        """
    def Clear(self) -> None: 
        """
        Clears all properties of the contour. Contour bound itself is not cleared.
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
    def FreeBound(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns contour

        Returns contour
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
    def NbNotches(self) -> int: 
        """
        Returns number of notches on the contour

        Returns number of notches on the contour
        """
    def Notch(self,index : int) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns notch on the contour

        Returns notch on the contour
        """
    @overload
    def NotchWidth(self,notch : OCP.TopoDS.TopoDS_Wire) -> float: 
        """
        Returns maximum width of notch specified by its rank number on the contour

        Returns maximum width of notch specified as TopoDS_Wire on the contour
        """
    @overload
    def NotchWidth(self,index : int) -> float: ...
    def Notches(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        Returns sequence of notches on the contour

        Returns sequence of notches on the contour
        """
    def Perimeter(self) -> float: 
        """
        Returns perimeter of the contour

        Returns perimeter of the contour
        """
    def Ratio(self) -> float: 
        """
        Returns ratio of average length to average width of the contour

        Returns ratio of average length to average width of the contour
        """
    def SetArea(self,area : float) -> None: 
        """
        Sets area of the contour

        Sets area of the contour
        """
    def SetFreeBound(self,freebound : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Sets contour

        Sets contour
        """
    def SetPerimeter(self,perimeter : float) -> None: 
        """
        Sets perimeter of the contour

        Sets perimeter of the contour
        """
    def SetRatio(self,ratio : float) -> None: 
        """
        Sets ratio of average length to average width of the contour

        Sets ratio of average length to average width of the contour
        """
    def SetWidth(self,width : float) -> None: 
        """
        Sets average width of the contour

        Sets average width of the contour
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Width(self) -> float: 
        """
        Returns average width of the contour

        Returns average width of the contour
        """
    @overload
    def __init__(self,freebound : OCP.TopoDS.TopoDS_Wire) -> None: ...
    @overload
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
class ShapeAnalysis_FreeBounds():
    """
    This class is intended to output free bounds of the shape.
    """
    @staticmethod
    def ConnectEdgesToWires_s(edges : OCP.TopTools.TopTools_HSequenceOfShape,toler : float,shared : bool,wires : OCP.TopTools.TopTools_HSequenceOfShape) -> None: 
        """
        Builds sequnce of <wires> out of sequence of not sorted <edges>. Tries to build wires of maximum length. Building a wire is stopped when no edges can be connected to it at its head or at its tail.
        """
    @staticmethod
    @overload
    def ConnectWiresToWires_s(iwires : OCP.TopTools.TopTools_HSequenceOfShape,toler : float,shared : bool,owires : OCP.TopTools.TopTools_HSequenceOfShape,vertices : OCP.TopTools.TopTools_DataMapOfShapeShape) -> None: 
        """
        None

        Builds sequnce of <owires> out of sequence of not sorted <iwires>. Tries to build wires of maximum length. Building a wire is stopped when no wires can be connected to it at its head or at its tail.
        """
    @staticmethod
    @overload
    def ConnectWiresToWires_s(iwires : OCP.TopTools.TopTools_HSequenceOfShape,toler : float,shared : bool,owires : OCP.TopTools.TopTools_HSequenceOfShape) -> None: ...
    @staticmethod
    def DispatchWires_s(wires : OCP.TopTools.TopTools_HSequenceOfShape,closed : OCP.TopoDS.TopoDS_Compound,open : OCP.TopoDS.TopoDS_Compound) -> None: 
        """
        Dispatches sequence of <wires> into two compounds <closed> for closed wires and <open> for open wires. If a compound is not empty wires are added into it.
        """
    def GetClosedWires(self) -> OCP.TopoDS.TopoDS_Compound: 
        """
        Returns compound of closed wires out of free edges.

        Returns compound of closed wires out of free edges.
        """
    def GetOpenWires(self) -> OCP.TopoDS.TopoDS_Compound: 
        """
        Returns compound of open wires out of free edges.

        Returns compound of open wires out of free edges.
        """
    @staticmethod
    def SplitWires_s(wires : OCP.TopTools.TopTools_HSequenceOfShape,toler : float,shared : bool,closed : OCP.TopTools.TopTools_HSequenceOfShape,open : OCP.TopTools.TopTools_HSequenceOfShape) -> None: 
        """
        Extracts closed sub-wires out of <wires> and adds them to <closed>, open wires remained after extraction are put into <open>. If <shared> is True extraction is performed only when edges share the same vertex. If <shared> is False connection is performed only when ends of the edges are at distance less than <toler>.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,shape : OCP.TopoDS.TopoDS_Shape,splitclosed : bool=False,splitopen : bool=True,checkinternaledges : bool=False) -> None: ...
    @overload
    def __init__(self,shape : OCP.TopoDS.TopoDS_Shape,toler : float,splitclosed : bool=False,splitopen : bool=True) -> None: ...
    pass
class ShapeAnalysis_FreeBoundsProperties():
    """
    This class is intended to calculate shape free bounds properties. This class provides the following functionalities: - calculates area of the contour, - calculates perimeter of the contour, - calculates ratio of average length to average width of the contour, - estimates average width of contour, - finds the notches (narrow 'V'-like sub-contour) on the contour.
    """
    def CheckContours(self,prec : float=0.0) -> bool: 
        """
        None
        """
    @overload
    def CheckNotches(self,freebound : OCP.TopoDS.TopoDS_Wire,num : int,notch : OCP.TopoDS.TopoDS_Wire,distMax : float,prec : float=0.0) -> bool: 
        """
        None

        None

        None
        """
    @overload
    def CheckNotches(self,prec : float=0.0) -> bool: ...
    @overload
    def CheckNotches(self,fbData : ShapeAnalysis_FreeBoundData,prec : float=0.0) -> bool: ...
    def ClosedFreeBound(self,index : int) -> ShapeAnalysis_FreeBoundData: 
        """
        Returns properties of closed free bound specified by its rank number

        Returns properties of closed free bound specified by its rank number
        """
    def ClosedFreeBounds(self) -> ShapeAnalysis_HSequenceOfFreeBounds: 
        """
        Returns all closed free bounds

        Returns all closed free bounds
        """
    def DispatchBounds(self) -> bool: 
        """
        None
        """
    def FillProperties(self,fbData : ShapeAnalysis_FreeBoundData,prec : float=0.0) -> bool: 
        """
        None
        """
    @overload
    def Init(self,shape : OCP.TopoDS.TopoDS_Shape,splitclosed : bool=False,splitopen : bool=False) -> None: 
        """
        Initializes the object with given parameters. <shape> should be a compound of faces.

        Initializes the object with given parameters. <shape> should be a compound of shells.
        """
    @overload
    def Init(self,shape : OCP.TopoDS.TopoDS_Shape,tolerance : float,splitclosed : bool=False,splitopen : bool=False) -> None: ...
    def IsLoaded(self) -> bool: 
        """
        Returns True if shape is loaded

        Returns True if shape is loaded
        """
    def NbClosedFreeBounds(self) -> int: 
        """
        Returns number of closed free bounds

        Returns number of closed free bounds
        """
    def NbFreeBounds(self) -> int: 
        """
        Returns number of free bounds

        Returns number of free bounds
        """
    def NbOpenFreeBounds(self) -> int: 
        """
        Returns number of open free bounds

        Returns number of open free bounds
        """
    def OpenFreeBound(self,index : int) -> ShapeAnalysis_FreeBoundData: 
        """
        Returns properties of open free bound specified by its rank number

        Returns properties of open free bound specified by its rank number
        """
    def OpenFreeBounds(self) -> ShapeAnalysis_HSequenceOfFreeBounds: 
        """
        Returns all open free bounds

        Returns all open free bounds
        """
    def Perform(self) -> bool: 
        """
        Builds and analyzes free bounds of the shape. First calls ShapeAnalysis_FreeBounds for building free bounds. Then on each free bound computes its properties: - area of the contour, - perimeter of the contour, - ratio of average length to average width of the contour, - average width of contour, - notches on the contour and for each notch - maximum width of the notch.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns shape

        Returns shape
        """
    def Tolerance(self) -> float: 
        """
        Returns tolerance

        Returns tolerance
        """
    @overload
    def __init__(self,shape : OCP.TopoDS.TopoDS_Shape,tolerance : float,splitclosed : bool=False,splitopen : bool=False) -> None: ...
    @overload
    def __init__(self,shape : OCP.TopoDS.TopoDS_Shape,splitclosed : bool=False,splitopen : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class ShapeAnalysis_Geom():
    """
    Analyzing tool aimed to work on primitive geometrical objects
    """
    @staticmethod
    def NearestPlane_s(Pnts : OCP.TColgp.TColgp_Array1OfPnt,aPln : OCP.gp.gp_Pln,Dmax : float) -> bool: 
        """
        Builds a plane out of a set of points in array Returns in <dmax> the maximal distance between the produced plane and given points
        """
    @staticmethod
    def PositionTrsf_s(coefs : OCP.TColStd.TColStd_HArray2OfReal,trsf : OCP.gp.gp_Trsf,unit : float,prec : float) -> bool: 
        """
        Builds transformation object out of matrix. Matrix must be 3 x 4. Unit is used as multiplier.
        """
    def __init__(self) -> None: ...
    pass
class ShapeAnalysis_SequenceOfFreeBounds(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : ShapeAnalysis_FreeBoundData) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : ShapeAnalysis_SequenceOfFreeBounds) -> None: ...
    def Assign(self,theOther : ShapeAnalysis_SequenceOfFreeBounds) -> ShapeAnalysis_SequenceOfFreeBounds: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> ShapeAnalysis_FreeBoundData: 
        """
        First item access
        """
    def ChangeLast(self) -> ShapeAnalysis_FreeBoundData: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> ShapeAnalysis_FreeBoundData: 
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
    def First(self) -> ShapeAnalysis_FreeBoundData: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : ShapeAnalysis_SequenceOfFreeBounds) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : ShapeAnalysis_FreeBoundData) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : ShapeAnalysis_FreeBoundData) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ShapeAnalysis_SequenceOfFreeBounds) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> ShapeAnalysis_FreeBoundData: 
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
    def Prepend(self,theItem : ShapeAnalysis_FreeBoundData) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : ShapeAnalysis_SequenceOfFreeBounds) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : ShapeAnalysis_FreeBoundData) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ShapeAnalysis_SequenceOfFreeBounds) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> ShapeAnalysis_FreeBoundData: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : ShapeAnalysis_SequenceOfFreeBounds) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class ShapeAnalysis_HSequenceOfFreeBounds(ShapeAnalysis_SequenceOfFreeBounds, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : ShapeAnalysis_FreeBoundData) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : ShapeAnalysis_SequenceOfFreeBounds) -> None: ...
    def Assign(self,theOther : ShapeAnalysis_SequenceOfFreeBounds) -> ShapeAnalysis_SequenceOfFreeBounds: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> ShapeAnalysis_FreeBoundData: 
        """
        First item access
        """
    def ChangeLast(self) -> ShapeAnalysis_FreeBoundData: 
        """
        Last item access
        """
    def ChangeSequence(self) -> ShapeAnalysis_SequenceOfFreeBounds: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> ShapeAnalysis_FreeBoundData: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
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
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> ShapeAnalysis_FreeBoundData: 
        """
        First item access
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
    def InsertAfter(self,theIndex : int,theSeq : ShapeAnalysis_SequenceOfFreeBounds) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : ShapeAnalysis_FreeBoundData) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : ShapeAnalysis_FreeBoundData) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ShapeAnalysis_SequenceOfFreeBounds) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> ShapeAnalysis_FreeBoundData: 
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
    def Prepend(self,theItem : ShapeAnalysis_FreeBoundData) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : ShapeAnalysis_SequenceOfFreeBounds) -> None: ...
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
    def Sequence(self) -> ShapeAnalysis_SequenceOfFreeBounds: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : ShapeAnalysis_FreeBoundData) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ShapeAnalysis_SequenceOfFreeBounds) -> None: 
        """
        Split in two sequences
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> ShapeAnalysis_FreeBoundData: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : ShapeAnalysis_SequenceOfFreeBounds) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
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
class ShapeAnalysis_ShapeContents():
    """
    Dumps shape contents
    """
    def BigSplineSec(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Clears all accumulated statistics
        """
    def ClearFlags(self) -> None: 
        """
        Clears all flags
        """
    def IndirectSec(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        None
        """
    def NbBSplibeSurf(self) -> int: 
        """
        None
        """
    def NbBezierSurf(self) -> int: 
        """
        None
        """
    def NbBigSplines(self) -> int: 
        """
        None
        """
    def NbC0Curves(self) -> int: 
        """
        None
        """
    def NbC0Surfaces(self) -> int: 
        """
        None
        """
    def NbEdges(self) -> int: 
        """
        None
        """
    def NbFaceWithSevWires(self) -> int: 
        """
        None
        """
    def NbFaces(self) -> int: 
        """
        None
        """
    def NbFreeEdges(self) -> int: 
        """
        None
        """
    def NbFreeFaces(self) -> int: 
        """
        None
        """
    def NbFreeWires(self) -> int: 
        """
        None
        """
    def NbIndirectSurf(self) -> int: 
        """
        None
        """
    def NbNoPCurve(self) -> int: 
        """
        None
        """
    def NbOffsetCurves(self) -> int: 
        """
        None
        """
    def NbOffsetSurf(self) -> int: 
        """
        None
        """
    def NbSharedEdges(self) -> int: 
        """
        None
        """
    def NbSharedFaces(self) -> int: 
        """
        None
        """
    def NbSharedFreeEdges(self) -> int: 
        """
        None
        """
    def NbSharedFreeWires(self) -> int: 
        """
        None
        """
    def NbSharedShells(self) -> int: 
        """
        None
        """
    def NbSharedSolids(self) -> int: 
        """
        None
        """
    def NbSharedVertices(self) -> int: 
        """
        None
        """
    def NbSharedWires(self) -> int: 
        """
        None
        """
    def NbShells(self) -> int: 
        """
        None
        """
    def NbSolids(self) -> int: 
        """
        None
        """
    def NbSolidsWithVoids(self) -> int: 
        """
        None
        """
    def NbTrimSurf(self) -> int: 
        """
        None
        """
    def NbTrimmedCurve2d(self) -> int: 
        """
        None
        """
    def NbTrimmedCurve3d(self) -> int: 
        """
        None
        """
    def NbVertices(self) -> int: 
        """
        None
        """
    def NbWireWithSevSeams(self) -> int: 
        """
        None
        """
    def NbWireWitnSeam(self) -> int: 
        """
        None
        """
    def NbWires(self) -> int: 
        """
        None
        """
    def OffsetCurveSec(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        None
        """
    def OffsetSurfaceSec(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        None
        """
    def Perform(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Counts quantities of sun-shapes in shape and stores sub-shapes according to flags
        """
    def Trimmed2dSec(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        None
        """
    def Trimmed3dSec(self) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        None
        """
    def __init__(self) -> None: ...
    @property
    def ModifyBigSplineMode(self) -> bool:
        """
        :type: bool
        """
    @ModifyBigSplineMode.setter
    def ModifyBigSplineMode(self, arg1: bool) -> None:
        pass
    @property
    def ModifyIndirectMode(self) -> bool:
        """
        :type: bool
        """
    @ModifyIndirectMode.setter
    def ModifyIndirectMode(self, arg1: bool) -> None:
        pass
    @property
    def ModifyOffestSurfaceMode(self) -> bool:
        """
        None

        :type: bool
        """
    @ModifyOffestSurfaceMode.setter
    def ModifyOffestSurfaceMode(self, arg1: bool) -> None:
        """
        None
        """
    @property
    def ModifyOffsetCurveMode(self) -> bool:
        """
        :type: bool
        """
    @ModifyOffsetCurveMode.setter
    def ModifyOffsetCurveMode(self, arg1: bool) -> None:
        pass
    @property
    def ModifyOffsetSurfaceMode(self) -> bool:
        """
        :type: bool
        """
    @ModifyOffsetSurfaceMode.setter
    def ModifyOffsetSurfaceMode(self, arg1: bool) -> None:
        pass
    @property
    def ModifyTrimmed2dMode(self) -> bool:
        """
        :type: bool
        """
    @ModifyTrimmed2dMode.setter
    def ModifyTrimmed2dMode(self, arg1: bool) -> None:
        pass
    @property
    def ModifyTrimmed3dMode(self) -> bool:
        """
        :type: bool
        """
    @ModifyTrimmed3dMode.setter
    def ModifyTrimmed3dMode(self, arg1: bool) -> None:
        pass
    pass
class ShapeAnalysis_ShapeTolerance():
    """
    Tool for computing shape tolerances (minimal, maximal, average), finding shape with tolerance matching given criteria, setting or limitating tolerances.
    """
    def AddTolerance(self,shape : OCP.TopoDS.TopoDS_Shape,type : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> None: 
        """
        Adds data on new Shape to compute Cumulated Tolerance (prepares three computations : maximal, average, minimal)
        """
    def GlobalTolerance(self,mode : int) -> float: 
        """
        Returns the computed tolerance according to the <mode> <mode> = 0 : average <mode> > 0 : maximal <mode> < 0 : minimal
        """
    def InTolerance(self,shape : OCP.TopoDS.TopoDS_Shape,valmin : float,valmax : float,type : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        Determines which shapes have a tolerance within a given interval <type> is interpreted as in the method Tolerance
        """
    def InitTolerance(self) -> None: 
        """
        Initializes computation of cumulated tolerance
        """
    def OverTolerance(self,shape : OCP.TopoDS.TopoDS_Shape,value : float,type : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> OCP.TopTools.TopTools_HSequenceOfShape: 
        """
        Determines which shapes have a tolerance over the given value <type> is interpreted as in the method Tolerance
        """
    def Tolerance(self,shape : OCP.TopoDS.TopoDS_Shape,mode : int,type : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> float: 
        """
        Determines a tolerance from the ones stored in a shape Remark : calls InitTolerance and AddTolerance, hence, can be used to start a series for cumulating tolerance <mode> = 0 : returns the average value between sub-shapes, <mode> > 0 : returns the maximal found, <mode> < 0 : returns the minimal found. <type> defines what kinds of sub-shapes to consider: SHAPE (default) : all : VERTEX, EDGE, FACE, VERTEX : only vertices, EDGE : only edges, FACE : only faces, SHELL : combined SHELL + FACE, for each face (and containing shell), also checks EDGE and VERTEX
        """
    def __init__(self) -> None: ...
    pass
class ShapeAnalysis_Shell():
    """
    This class provides operators to analyze edges orientation in the shell.
    """
    def BadEdges(self) -> OCP.TopoDS.TopoDS_Compound: 
        """
        Returns the list of bad edges as a Compound It is empty (not null) if no edge are recorded as bad
        """
    def CheckOrientedShells(self,shape : OCP.TopoDS.TopoDS_Shape,alsofree : bool=False,checkinternaledges : bool=False) -> bool: 
        """
        Checks if shells fulfill orientation condition, i.e. if each edge is, either present once (free edge) or twice (connected edge) but with different orientations (FORWARD/REVERSED) Edges which do not fulfill these conditions are bad
        """
    def Clear(self) -> None: 
        """
        Clears data about loaded shells and performed checks
        """
    def FreeEdges(self) -> OCP.TopoDS.TopoDS_Compound: 
        """
        Returns the list of free (not connected) edges as a Compound It is empty (not null) if no edge are recorded as free
        """
    def HasBadEdges(self) -> bool: 
        """
        Tells if at least one edge is recorded as bad
        """
    def HasConnectedEdges(self) -> bool: 
        """
        Tells if at least one edge is connected (shared twice or more)
        """
    def HasFreeEdges(self) -> bool: 
        """
        Tells if at least one edge is recorded as free (not connected)
        """
    def IsLoaded(self,shape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Tells if a shape is loaded (only shells are checked)
        """
    def LoadShells(self,shape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds shells contained in the <shape> to the list of loaded shells
        """
    def Loaded(self,num : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a loaded shape specified by its rank number. Returns null shape if <num> is out of range
        """
    def NbLoaded(self) -> int: 
        """
        Returns the actual number of loaded shapes (i.e. shells)
        """
    def __init__(self) -> None: ...
    pass
class ShapeAnalysis_Surface(OCP.Standard.Standard_Transient):
    """
    Complements standard tool Geom_Surface by providing additional functionality for detection surface singularities, checking spatial surface closure and computing projections of 3D points onto a surface.Complements standard tool Geom_Surface by providing additional functionality for detection surface singularities, checking spatial surface closure and computing projections of 3D points onto a surface.
    """
    def Adaptor3d(self) -> OCP.GeomAdaptor.GeomAdaptor_Surface: 
        """
        Returns the Adaptor. Creates it if not yet done.
        """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the bounds of the surface (from Bounds from Surface, but buffered)

        Returns the bounds of the surface (from Bounds from Surface, but buffered)
        """
    def ComputeBoundIsos(self) -> None: 
        """
        Computes bound isos (protected against exceptions)
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DegeneratedValues(self,P3d : OCP.gp.gp_Pnt,preci : float,firstP2d : OCP.gp.gp_Pnt2d,lastP2d : OCP.gp.gp_Pnt2d,firstpar : float,lastpar : float,forward : bool=True) -> bool: 
        """
        Returns True if there is at least one surface iso-line which is considered as degenerated with <preci> and distance between P3d and corresponding singular point is less than <preci> (like IsDegenerated). Returns characteristics of the first found boundary matching those criteria.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Gap(self) -> float: 
        """
        Returns 3D distance found by one of the following methods. IsDegenerated, DegeneratedValues, ProjectDegenerated (distance between 3D point and found or last (if not found) singularity), IsUClosed, IsVClosed (minimum value of precision to consider the surface to be closed), ValueOfUV (distance between 3D point and found solution).

        Returns 3D distance found by one of the following methods. IsDegenerated, DegeneratedValues, ProjectDegenerated (distance between 3D point and found or last (if not found) singularity), IsUClosed, IsVClosed (minimum value of precision to consider the surface to be closed), ValueOfUV (distance between 3D point and found solution).
        """
    def GetBoxUF(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def GetBoxUL(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def GetBoxVF(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def GetBoxVL(self) -> OCP.Bnd.Bnd_Box: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSingularities(self,preci : float) -> bool: 
        """
        Returns True if the surface has singularities for the given precision (i.e. if there are surface singularities with sizes not greater than precision).
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,other : ShapeAnalysis_Surface) -> None: 
        """
        Loads existing surface

        Reads all the data from another Surface, without recomputing
        """
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def IsDegenerated(self,p2d1 : OCP.gp.gp_Pnt2d,p2d2 : OCP.gp.gp_Pnt2d,tol : float,ratio : float) -> bool: 
        """
        Returns True if there is at least one surface boundary which is considered as degenerated with <preci> and distance between P3d and corresponding singular point is less than <preci>

        Returns True if straight pcurve going from point p2d1 to p2d2 is degenerate, i.e. lies in the singularity of the surface. NOTE: it uses another method of detecting singularity than used by ComputeSingularities() et al.! For that, maximums of distances between points p2d1, p2d2 and 0.5*(p2d1+p2d2) and between corresponding 3d points are computed. The pcurve (p2d1, p2d2) is considered as degenerate if: - max distance in 3d is less than <tol> - max distance in 2d is at least <ratio> times greater than the Resolution computed from max distance in 3d (max3d < tol && max2d > ratio * Resolution(max3d)) NOTE: <ratio> should be >1 (e.g. 10)
        """
    @overload
    def IsDegenerated(self,P3d : OCP.gp.gp_Pnt,preci : float) -> bool: ...
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
    def IsUClosed(self,preci : float=-1.0) -> bool: 
        """
        Tells if the Surface is spatially closed in U with given precision. If <preci> < 0 then Precision::Confusion is used. If Geom_Surface says that the surface is U-closed, this method also says this. Otherwise additional analysis is performed, comparing given precision with the following distances: - periodic B-Splines are closed, - polinomial B-Spline with boundary multiplicities degree+1 and Bezier - maximum distance between poles, - rational B-Spline or one with boundary multiplicities not degree+1 - maximum distance computed at knots and their middles, - surface of extrusion - distance between ends of basis curve, - other (RectangularTrimmed and Offset) - maximum distance computed at 100 equi-distanted points.
        """
    def IsVClosed(self,preci : float=-1.0) -> bool: 
        """
        Tells if the Surface is spatially closed in V with given precision. If <preci> < 0 then Precision::Confusion is used. If Geom_Surface says that the surface is V-closed, this method also says this. Otherwise additional analysis is performed, comparing given precision with the following distances: - periodic B-Splines are closed, - polinomial B-Spline with boundary multiplicities degree+1 and Bezier - maximum distance between poles, - rational B-Spline or one with boundary multiplicities not degree+1 - maximum distance computed at knots and their middles, - surface of revolution - distance between ends of basis curve, - other (RectangularTrimmed and Offset) - maximum distance computed at 100 equi-distanted points.
        """
    def NbSingularities(self,preci : float) -> int: 
        """
        Returns the number of singularities for the given precision (i.e. number of surface singularities with sizes not greater than precision).
        """
    def NextValueOfUV(self,p2dPrev : OCP.gp.gp_Pnt2d,P3D : OCP.gp.gp_Pnt,preci : float,maxpreci : float=-1.0) -> OCP.gp.gp_Pnt2d: 
        """
        Projects a point P3D on the surface. Does the same thing as ValueOfUV but tries to optimize computations by taking into account previous point <p2dPrev>: makes a step by UV and tries Newton algorithm. If <maxpreci> >0. and distance between solution and P3D is greater than <maxpreci>, that solution is considered as bad, and ValueOfUV() is used. If not succeeded, calls ValueOfUV()
        """
    @overload
    def ProjectDegenerated(self,nbrPnt : int,points : OCP.TColgp.TColgp_SequenceOfPnt,pnt2d : OCP.TColgp.TColgp_SequenceOfPnt2d,preci : float,direct : bool) -> bool: 
        """
        Projects a point <P3d> on a singularity by computing one of the coordinates of preliminary computed <result>.

        Checks points at the beginning (direct is True) or end (direct is False) of array <points> to lie in singularity of surface, and if yes, adjusts the indeterminate 2d coordinate of these points by nearest point which is not in singularity. Returns True if some points were adjusted.
        """
    @overload
    def ProjectDegenerated(self,P3d : OCP.gp.gp_Pnt,preci : float,neighbour : OCP.gp.gp_Pnt2d,result : OCP.gp.gp_Pnt2d) -> bool: ...
    def SetDomain(self,U1 : float,U2 : float,V1 : float,V2 : float) -> None: 
        """
        None
        """
    def Singularity(self,num : int,preci : float,P3d : OCP.gp.gp_Pnt,firstP2d : OCP.gp.gp_Pnt2d,lastP2d : OCP.gp.gp_Pnt2d,firstpar : float,lastpar : float,uisodeg : bool) -> bool: 
        """
        Returns the characteristics of the singularity specified by its rank number <num>. That means, that it is not necessary for <num> to be in the range [1, NbSingularities] but must be not greater than possible (see ComputeSingularities). The returned characteristics are: preci: the smallest precision with which the iso-line is considered as degenerated, P3d: 3D point of singularity (middle point of the surface iso-line), firstP2d and lastP2d: first and last 2D points of the iso-line in parametrical surface, firstpar and lastpar: first and last parameters of the iso-line in parametrical surface, uisodeg: if the degenerated iso-line is U-iso (True) or V-iso (False). Returns False if <num> is out of range, else returns True.
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        Returns a surface being analyzed

        Returns a surface being analyzed
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TrueAdaptor3d(self) -> OCP.GeomAdaptor.GeomAdaptor_Surface: 
        """
        Returns the Adaptor (may be Null if method Adaptor() was not called)

        Returns the Adaptor (may be Null if method Adaptor() was not called)
        """
    def UCloseVal(self) -> float: 
        """
        Returns minimum value to consider the surface as U-closed

        Returns minimum value to consider the surface as U-closed
        """
    def UIso(self,U : float) -> OCP.Geom.Geom_Curve: 
        """
        Returns a U-Iso. Null if not possible or failed Remark : bound isos are buffered
        """
    def UVFromIso(self,P3D : OCP.gp.gp_Pnt,preci : float,U : float,V : float) -> float: 
        """
        Tries a refinement of an already computed couple (U,V) by using projecting 3D point on iso-lines: 1. boundaries of the surface, 2. iso-lines passing through (U,V) 3. iteratively received iso-lines passing through new U and new V (number of iterations is limited by 5 in each direction) Returns the best resulting distance between P3D and Value(U,V) in the case of success. Else, returns a very great value
        """
    def VCloseVal(self) -> float: 
        """
        Returns minimum value to consider the surface as V-closed

        Returns minimum value to consider the surface as V-closed
        """
    def VIso(self,V : float) -> OCP.Geom.Geom_Curve: 
        """
        Returns a V-Iso. Null if not possible or failed Remark : bound isos are buffered
        """
    @overload
    def Value(self,u : float,v : float) -> OCP.gp.gp_Pnt: 
        """
        Returns a 3D point specified by parameters in surface parametrical space

        Returns a 3d point specified by a point in surface parametrical space

        Returns a 3D point specified by parameters in surface parametrical space

        Returns a 3d point specified by a point in surface parametrical space
        """
    @overload
    def Value(self,p2d : OCP.gp.gp_Pnt2d) -> OCP.gp.gp_Pnt: ...
    def ValueOfUV(self,P3D : OCP.gp.gp_Pnt,preci : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the parameters in the surface parametrical space of 3D point. The result is parameters of the point projected onto the surface. This method enhances functionality provided by the standard tool GeomAPI_ProjectPointOnSurface by treatment of cases when the projected point is near to the surface boundaries and when this standard tool fails.
        """
    def __init__(self,S : OCP.Geom.Geom_Surface) -> None: ...
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
class ShapeAnalysis_TransferParameters(OCP.Standard.Standard_Transient):
    """
    This tool is used for transferring parameters from 3d curve of the edge to pcurve and vice versa.This tool is used for transferring parameters from 3d curve of the edge to pcurve and vice versa.This tool is used for transferring parameters from 3d curve of the edge to pcurve and vice versa.
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Initialize a tool with edge and face
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
    def IsSameRange(self) -> bool: 
        """
        Returns True if 3d curve of edge and pcurve are SameRange (in default implementation, if myScale == 1 and myShift == 0)
        """
    @overload
    def Perform(self,Param : float,To2d : bool) -> float: 
        """
        Transfers parameters given by sequence Params from 3d curve to pcurve (if To2d is True) or back (if To2d is False)

        Transfers parameter given by sequence Params from 3d curve to pcurve (if To2d is True) or back (if To2d is False)
        """
    @overload
    def Perform(self,Params : OCP.TColStd.TColStd_HSequenceOfReal,To2d : bool) -> OCP.TColStd.TColStd_HSequenceOfReal: ...
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal tolerance to use linear recomputation of parameters.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransferRange(self,newEdge : OCP.TopoDS.TopoDS_Edge,prevPar : float,currPar : float,To2d : bool) -> None: 
        """
        Recomputes range of curves from NewEdge. If Is2d equals True parameters are recomputed by curve2d else by curve3d.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
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
class ShapeAnalysis_TransferParametersProj(ShapeAnalysis_TransferParameters, OCP.Standard.Standard_Transient):
    """
    This tool is used for transferring parameters from 3d curve of the edge to pcurve and vice versa. This tool transfers parameters with help of projection points from curve 3d on curve 2d and vice versaThis tool is used for transferring parameters from 3d curve of the edge to pcurve and vice versa. This tool transfers parameters with help of projection points from curve 3d on curve 2d and vice versaThis tool is used for transferring parameters from 3d curve of the edge to pcurve and vice versa. This tool transfers parameters with help of projection points from curve 3d on curve 2d and vice versa
    """
    @staticmethod
    @overload
    def CopyNMVertex_s(theVert : OCP.TopoDS.TopoDS_Vertex,toedge : OCP.TopoDS.TopoDS_Edge,fromedge : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Make a copy of non-manifold vertex theVert (i.e. create new TVertex and replace PointRepresentations for this vertex from fromedge to toedge. Other representations were copied)

        Make a copy of non-manifold vertex theVert (i.e. create new TVertex and replace PointRepresentations for this vertex from fromFace to toFace. Other representations were copied)
        """
    @staticmethod
    @overload
    def CopyNMVertex_s(theVert : OCP.TopoDS.TopoDS_Vertex,toFace : OCP.TopoDS.TopoDS_Face,fromFace : OCP.TopoDS.TopoDS_Face) -> OCP.TopoDS.TopoDS_Vertex: ...
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: 
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
    def IsSameRange(self) -> bool: 
        """
        Returns False;
        """
    @overload
    def Perform(self,Param : float,To2d : bool) -> float: 
        """
        Transfers parameters given by sequence Params from 3d curve to pcurve (if To2d is True) or back (if To2d is False)

        Transfers parameter given by Param from 3d curve to pcurve (if To2d is True) or back (if To2d is False)
        """
    @overload
    def Perform(self,Papams : OCP.TColStd.TColStd_HSequenceOfReal,To2d : bool) -> OCP.TColStd.TColStd_HSequenceOfReal: ...
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal tolerance to use linear recomputation of parameters.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransferRange(self,newEdge : OCP.TopoDS.TopoDS_Edge,prevPar : float,currPar : float,Is2d : bool) -> None: 
        """
        Recomputes range of curves from NewEdge. If Is2d equals True parameters are recomputed by curve2d else by curve3d.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
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
    @property
    def ForceProjection(self) -> bool:
        """
        Returns modifiable flag forcing projection If it is False (default), projection is done only if edge is not SameParameter or if tolerance of edge is greater than MaxTolerance()

        :type: bool
        """
    @ForceProjection.setter
    def ForceProjection(self, arg1: bool) -> None:
        """
        Returns modifiable flag forcing projection If it is False (default), projection is done only if edge is not SameParameter or if tolerance of edge is greater than MaxTolerance()
        """
    pass
class ShapeAnalysis_Wire(OCP.Standard.Standard_Transient):
    """
    This class provides analysis of a wire to be compliant to CAS.CADE requirements.This class provides analysis of a wire to be compliant to CAS.CADE requirements.This class provides analysis of a wire to be compliant to CAS.CADE requirements.
    """
    def CheckClosed(self,prec : float=0.0) -> bool: 
        """
        Checks if wire is closed, performs CheckConnected, CheckDegenerated and CheckLacking for the first and the last edges Returns: True if at least one check returned True Status: FAIL1 or DONE1: see CheckConnected FAIL2 or DONE2: see CheckDegenerated
        """
    @overload
    def CheckConnected(self,num : int,prec : float=0.0) -> bool: 
        """
        Calls to CheckConnected for each edge Returns: True if at least one pair of disconnected edges (not sharing the same vertex) was detected

        Checks connected edges (num-th and preceding). Tests with starting preci from <SBWD> or with <prec> if it is greater. Considers Vertices. Returns: False if edges are connected by the common vertex, else True Status : OK : Vertices (end of num-1 th edge and start on num-th one) are already the same DONE1 : Absolutely confused (gp::Resolution) DONE2 : Confused at starting <preci> from <SBWD> DONE3 : Confused at <prec> but not <preci> FAIL1 : Not confused FAIL2 : Not confused but confused with <preci> if reverse num-th edge
        """
    @overload
    def CheckConnected(self,prec : float=0.0) -> bool: ...
    def CheckCurveGap(self,num : int=0) -> bool: 
        """
        Checks gap between points on 3D curve and points on surface generated by pcurve of the num-th edge. The distance can be queried by MinDistance3d.
        """
    def CheckCurveGaps(self) -> bool: 
        """
        None
        """
    @overload
    def CheckDegenerated(self,num : int) -> bool: 
        """
        Calls to CheckDegenerated for each edge Returns: True if at least one incorrect degenerated edge was detected

        Checks for degenerated edge between two adjacent ones. Fills parameters dgnr1 and dgnr2 with points in parametric space that correspond to the singularity (either gap that needs to be filled by degenerated edge or that already filled) Returns: False if no singularity or edge is already degenerated, otherwise True Status: OK : No surface singularity, or edge is already degenerated DONE1: Degenerated edge should be inserted (gap in 2D) DONE2: Edge <num> should be made degenerated (recompute pcurve and set the flag) FAIL1: One of edges neighbouring to degenerated one has no pcurve FAIL2: Edge marked as degenerated and has no pcurve but singularity is not detected

        Checks for degenerated edge between two adjacent ones. Remark : Calls previous function Status : See the function above for details
        """
    @overload
    def CheckDegenerated(self) -> bool: ...
    @overload
    def CheckDegenerated(self,num : int,dgnr1 : OCP.gp.gp_Pnt2d,dgnr2 : OCP.gp.gp_Pnt2d) -> bool: ...
    def CheckEdgeCurves(self) -> bool: 
        """
        Checks edges geometry (consistency of 2d and 3d senses, adjasment of curves to the vertices, etc.). The order of the checks : Call ShapeAnalysis_Wire to check: ShapeAnalysis_Edge::CheckCurve3dWithPCurve (1), ShapeAnalysis_Edge::CheckVertcesWithPCurve (2), ShapeAnalysis_Edge::CheckVertcesWithCurve3d (3), CheckSeam (4) Additional: CheckGap3d (5), CheckGap2d (6), ShapeAnalysis_Edge::CheckSameParameter (7) Returns: True if at least one check returned True Remark: The numbers in brackets show with what DONEi or FAILi the status can be queried
        """
    def CheckGap2d(self,num : int=0) -> bool: 
        """
        Checks gap between edges in 2D (pcurves). Checks the distance between ends of pcurves of the num-th and preceding edge. The distance can be queried by MinDistance2d.
        """
    def CheckGap3d(self,num : int=0) -> bool: 
        """
        Checks gap between edges in 3D (3d curves). Checks the distance between ends of 3d curves of the num-th and preceding edge. The distance can be queried by MinDistance3d.
        """
    def CheckGaps2d(self) -> bool: 
        """
        None
        """
    def CheckGaps3d(self) -> bool: 
        """
        None
        """
    @overload
    def CheckIntersectingEdges(self,num : int,points2d : OCP.IntRes2d.IntRes2d_SequenceOfIntersectionPoint,points3d : OCP.TColgp.TColgp_SequenceOfPnt,errors : OCP.TColStd.TColStd_SequenceOfReal) -> bool: 
        """
        Checks two adjacent edges for intersecting. Intersection is reported only if intersection point is not enclosed by the common end vertex of the edges. Returns: True if intersection is found. If returns True it also fills the sequences of intersection points, corresponding 3d points, and errors for them (half-distances between intersection points in 3d calculated from one and from another edge) Status: FAIL1 : No pcurve FAIL2 : No vertices DONE1 : Self-intersection found

        Checks two adjacent edges for intersecting. Remark : Calls the previous method Status : See the function above for details

        Checks i-th and j-th edges for intersecting. Remark : See the previous method for details

        Checks i-th and j-th edges for intersecting. Remark : Calls previous method. Status : See the function above for details
        """
    @overload
    def CheckIntersectingEdges(self,num1 : int,num2 : int,points2d : OCP.IntRes2d.IntRes2d_SequenceOfIntersectionPoint,points3d : OCP.TColgp.TColgp_SequenceOfPnt,errors : OCP.TColStd.TColStd_SequenceOfReal) -> bool: ...
    @overload
    def CheckIntersectingEdges(self,num : int) -> bool: ...
    @overload
    def CheckIntersectingEdges(self,num1 : int,num2 : int) -> bool: ...
    @overload
    def CheckLacking(self) -> bool: 
        """
        Calls to CheckLacking for each edge Returns: True if at least one lacking edge was detected

        Checks if there is a gap in 2d between edges, not comprised by the tolerance of their common vertex. If <Tolerance> is greater than 0. and less than tolerance of the vertex, then this value is used for check. Returns: True if not closed gap was detected p2d1 and p2d2 are the endpoint of <num-1>th edge and start of the <num>th edge in 2d. Status: OK: No edge is lacking (3d and 2d connection) FAIL1: edges have no vertices (at least one of them) FAIL2: edges are neither connected by common vertex, nor have coincided vertices FAIL1: edges have no pcurves DONE1: the gap is detected which cannot be closed by the tolerance of the common vertex (or with value of <Tolerance>) DONE2: is set (together with DONE1) if gap is detected and the vector (p2d2 - p2d1) goes in direction opposite to the pcurves of the edges (if angle is more than 0.9*PI).

        Checks if there is a gap in 2D between edges and not comprised by vertex tolerance The value of SBWD.thepreci is used. Returns: False if no edge should be inserted Status: OK : No edge is lacking (3d and 2d connection) DONE1 : The vertex tolerance should be increased only (2d gap is small) DONE2 : Edge can be inserted (3d and 2d gaps are large enough)
        """
    @overload
    def CheckLacking(self,num : int,Tolerance : float=0.0) -> bool: ...
    @overload
    def CheckLacking(self,num : int,Tolerance : float,p2d1 : OCP.gp.gp_Pnt2d,p2d2 : OCP.gp.gp_Pnt2d) -> bool: ...
    def CheckLoop(self,aMapLoopVertices : OCP.TopTools.TopTools_IndexedMapOfShape,aMapVertexEdges : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,aMapSmallEdges : OCP.TopTools.TopTools_MapOfShape,aMapSeemEdges : OCP.TopTools.TopTools_MapOfShape) -> bool: 
        """
        Checks existence of loop on wire and return vertices which are loop vertices (vertices belonging to a few pairs of edges)
        """
    def CheckNotchedEdges(self,num : int,shortNum : int,param : float,Tolerance : float=0.0) -> bool: 
        """
        Detects a notch
        """
    @overload
    def CheckOrder(self,sawo : ShapeAnalysis_WireOrder,isClosed : bool=True,mode3d : bool=True) -> bool: 
        """
        Calls CheckOrder and returns False if wire is already ordered (tail-to-head), True otherwise Flag <isClosed> defines if the wire is closed or not Flag <mode3d> defines which mode is used (3d or 2d)

        Analyzes the order of the edges in the wire, uses class WireOrder for that purpose. Flag <isClosed> defines if the wire is closed or not Flag <mode3d> defines which mode is used (3d or 2d) Returns False if wire is already ordered (tail-to-head), True otherwise. Use returned WireOrder object for deeper analysis. Status: OK : the same edges orientation, the same edges sequence DONE1: the same edges orientation, not the same edges sequence DONE2: as DONE1 and gaps more than myPrecision DONE3: not the same edges orientation (some need to be reversed) DONE4: as DONE3 and gaps more than myPrecision FAIL : algorithm failed (could not detect order)
        """
    @overload
    def CheckOrder(self,isClosed : bool=True,mode3d : bool=True) -> bool: ...
    def CheckOuterBound(self,APIMake : bool=True) -> bool: 
        """
        Checks if wire defines an outer bound on the face Uses ShapeAnalysis::IsOuterBound for analysis If <APIMake> is True uses BRepAPI_MakeWire to build the wire, if False (to be used only when edges share common vertices) uses BRep_Builder to build the wire
        """
    @overload
    def CheckSeam(self,num : int,C1 : OCP.Geom2d.Geom2d_Curve,C2 : OCP.Geom2d.Geom2d_Curve,cf : float,cl : float) -> bool: 
        """
        Checks if a seam pcurves are correct oriented Returns: False (status OK) if given edge is not a seam or if it is OK C1 - current pcurve for FORWARD edge, C2 - current pcurve for REVERSED edge (if returns True they should be swapped for the seam), cf, cl - first and last parameters on curves Status: OK : Pcurves are correct or edge is not seam DONE : Seam pcurves should be swapped

        Checks if a seam pcurves are correct oriented See previous functions for details
        """
    @overload
    def CheckSeam(self,num : int) -> bool: ...
    @overload
    def CheckSelfIntersectingEdge(self,num : int) -> bool: 
        """
        Checks if num-th edge is self-intersecting. Self-intersection is reported only if intersection point lies outside of both end vertices of the edge. Returns: True if edge is self-intersecting. If returns True it also fills the sequences of intersection points and corresponding 3d points (only that are not enclosed by a vertices) Status: FAIL1 : No pcurve FAIL2 : No vertices DONE1 : Self-intersection found

        None
        """
    @overload
    def CheckSelfIntersectingEdge(self,num : int,points2d : OCP.IntRes2d.IntRes2d_SequenceOfIntersectionPoint,points3d : OCP.TColgp.TColgp_SequenceOfPnt) -> bool: ...
    def CheckSelfIntersection(self) -> bool: 
        """
        Checks self-intersection of the wire (considering pcurves) Looks for self-intersecting edges and each pair of intersecting edges. Warning: It does not check each edge with any other one (only each two adjacent edges) The order of the checks : CheckSelfIntersectingEdge, CheckIntersectingEdges Returns: True if at least one check returned True Status: FAIL1 or DONE1 - see CheckSelfIntersectingEdge FAIL2 or DONE2 - see CheckIntersectingEdges
        """
    @overload
    def CheckShapeConnect(self,tailhead : float,tailtail : float,headtail : float,headhead : float,shape : OCP.TopoDS.TopoDS_Shape,prec : float=0.0) -> bool: 
        """
        Checks with what orientation <shape> (wire or edge) can be connected to the wire. Tests distances with starting <preci> from <SBWD> (close confusion), but if given <prec> is greater, tests with <prec> (coarse confusion). The smallest found distance can be returned by MinDistance3d

        The same as previous CheckShapeConnect but is more advanced. It returns the distances between each end of <sbwd> and each end of <shape>. For example, <tailhead> stores distance between tail of <sbwd> and head of <shape> Remark: First method CheckShapeConnect calls this one
        """
    @overload
    def CheckShapeConnect(self,shape : OCP.TopoDS.TopoDS_Shape,prec : float=0.0) -> bool: ...
    @overload
    def CheckSmall(self,precsmall : float=0.0) -> bool: 
        """
        Calls to CheckSmall for each edge Returns: True if at least one small edge was detected

        Checks if an edge has a length not greater than myPreci or precsmall (if it is smaller) Returns: False if its length is greater than precision Status: OK : edge is not small or degenerated DONE1: edge is small, vertices are the same DONE2: edge is small, vertices are not the same FAIL : no 3d curve and pcurve
        """
    @overload
    def CheckSmall(self,num : int,precsmall : float=0.0) -> bool: ...
    def CheckSmallArea(self,theWire : OCP.TopoDS.TopoDS_Wire) -> bool: 
        """
        Checks if wire has parametric area less than precision.
        """
    def CheckTail(self,theEdge1 : OCP.TopoDS.TopoDS_Edge,theEdge2 : OCP.TopoDS.TopoDS_Edge,theMaxSine : float,theMaxWidth : float,theMaxTolerance : float,theEdge11 : OCP.TopoDS.TopoDS_Edge,theEdge12 : OCP.TopoDS.TopoDS_Edge,theEdge21 : OCP.TopoDS.TopoDS_Edge,theEdge22 : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def ClearStatuses(self) -> None: 
        """
        Unsets all the status and distance fields wire, face and precision are not cleared
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
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the working face

        Returns the working face
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
    def Init(self,sbwd : OCP.ShapeExtend.ShapeExtend_WireData,face : OCP.TopoDS.TopoDS_Face,precision : float) -> None: 
        """
        Initializes the object with standard TopoDS_Wire, face and precision

        Initializes the object with WireData object, face and precision
        """
    @overload
    def Init(self,wire : OCP.TopoDS.TopoDS_Wire,face : OCP.TopoDS.TopoDS_Face,precision : float) -> None: ...
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
    def IsLoaded(self) -> bool: 
        """
        Returns True if wire is loaded and has number of edges >0

        Returns True if wire is loaded and has number of edges >0
        """
    def IsReady(self) -> bool: 
        """
        Returns True if IsLoaded and underlying face is not null

        Returns True if IsLoaded and underlying face is not null
        """
    def LastCheckStatus(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Querying the status of the LAST performed 'Advanced' checking procedure

        Querying the status of the LAST performed 'Advanced' checking procedure
        """
    @overload
    def Load(self,wire : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Loads the object with standard TopoDS_Wire

        Loads the object with WireData object
        """
    @overload
    def Load(self,sbwd : OCP.ShapeExtend.ShapeExtend_WireData) -> None: ...
    def MaxDistance2d(self) -> float: 
        """
        Returns the last maximal distance in 2D-UV computed by CheckContinuity2d

        Returns the last maximal distance in 2D-UV computed by CheckContinuity2d
        """
    def MaxDistance3d(self) -> float: 
        """
        Returns the last maximal distance in 3D computed by CheckOrientation, CheckConnected, CheckContinuity3d, CheckVertex, CheckNewVertex, CheckSameParameter

        Returns the last maximal distance in 3D computed by CheckOrientation, CheckConnected, CheckContinuity3d, CheckVertex, CheckNewVertex, CheckSameParameter
        """
    def MinDistance2d(self) -> float: 
        """
        Returns the last lowest distance in 2D-UV computed by CheckContinuity2d

        Returns the last lowest distance in 2D-UV computed by CheckContinuity2d
        """
    def MinDistance3d(self) -> float: 
        """
        Returns the last lowest distance in 3D computed by CheckOrientation, CheckConnected, CheckContinuity3d, CheckVertex, CheckNewVertex

        Returns the last lowest distance in 3D computed by CheckOrientation, CheckConnected, CheckContinuity3d, CheckVertex, CheckNewVertex
        """
    def NbEdges(self) -> int: 
        """
        Returns the number of edges in the wire, or 0 if it is not loaded

        Returns the number of edges in the wire, or 0 if it is not loaded
        """
    def Perform(self) -> bool: 
        """
        Performs all the checks in the following order : CheckOrder, CheckSmall, CheckConnected, CheckEdgeCurves, CheckDegenerated, CheckSelfIntersection, CheckLacking, CheckClosed Returns: True if at least one method returned True; For deeper analysis use Status...(status) methods
        """
    def Precision(self) -> float: 
        """
        Returns the value of precision

        Returns the value of precision
        """
    def SetFace(self,face : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Loads the face the wire lies on
        """
    def SetPrecision(self,precision : float) -> None: 
        """
        None
        """
    @overload
    def SetSurface(self,surface : OCP.Geom.Geom_Surface) -> None: 
        """
        Loads the surface the wire lies on

        Loads the surface the wire lies on
        """
    @overload
    def SetSurface(self,surface : OCP.Geom.Geom_Surface,location : OCP.TopLoc.TopLoc_Location) -> None: ...
    def StatusClosed(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusConnected(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusCurveGaps(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusDegenerated(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusEdgeCurves(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusGaps2d(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusGaps3d(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusLacking(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusLoop(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusOrder(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusSelfIntersection(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def StatusSmall(self,Status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        None

        None
        """
    def Surface(self) -> ShapeAnalysis_Surface: 
        """
        Returns the working surface

        Returns the working surface
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WireData(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        Returns wire object being analyzed

        Returns wire object being analyzed
        """
    @overload
    def __init__(self,sbwd : OCP.ShapeExtend.ShapeExtend_WireData,face : OCP.TopoDS.TopoDS_Face,precision : float) -> None: ...
    @overload
    def __init__(self,wire : OCP.TopoDS.TopoDS_Wire,face : OCP.TopoDS.TopoDS_Face,precision : float) -> None: ...
    @overload
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
class ShapeAnalysis_WireOrder():
    """
    This class is intended to control and, if possible, redefine the order of a list of edges which define a wire Edges are not given directly, but as their bounds (start,end)
    """
    @overload
    def Add(self,start3d : OCP.gp.gp_XYZ,end3d : OCP.gp.gp_XYZ) -> None: 
        """
        Adds a couple of points 3D (start,end)

        Adds a couple of points 2D (start,end)
        """
    @overload
    def Add(self,start2d : OCP.gp.gp_XY,end2d : OCP.gp.gp_XY) -> None: ...
    def Chain(self,num : int) -> Tuple[int, int]: 
        """
        Returns, for the chain n0 num, starting and ending numbers of edges. In the list of ordered edges (see Ordered for originals)
        """
    def Clear(self) -> None: 
        """
        Clears the list of edges, but not mode and tol
        """
    def Couple(self,num : int) -> Tuple[int, int]: 
        """
        Returns, for the couple n0 num, the two implied edges In the list of ordered edges
        """
    def Gap(self,num : int=0) -> float: 
        """
        Returns the gap between a couple and its preceding <num> is considered ordered If <num> = 0 (D), returns the greatest gap found
        """
    def IsDone(self) -> bool: 
        """
        Tells if Perform has been done Else, the following methods returns original values
        """
    def NbChains(self) -> int: 
        """
        Returns the count of computed chains
        """
    def NbCouples(self) -> int: 
        """
        Returns the count of computed couples
        """
    def NbEdges(self) -> int: 
        """
        Returns the count of added couples of points (one per edges)
        """
    def Ordered(self,n : int) -> int: 
        """
        Returns the number of original edge which correspond to the newly ordered number <n> Warning : the returned value is NEGATIVE if edge should be reversed
        """
    def Perform(self,closed : bool=True) -> None: 
        """
        Computes the better order If <closed> is True (D) considers also closure Optimised if the couples were already in order The criterium is : two couples in order if distance between end-prec and start-cur is less then starting tolerance <tol> Else, the smallest distance is reached Gap corresponds to a smallest distance greater than <tol>
        """
    def SetChains(self,gap : float) -> None: 
        """
        Determines the chains inside which successive edges have a gap less than a given value. Queried by NbChains and Chain
        """
    def SetCouples(self,gap : float) -> None: 
        """
        Determines the couples of edges for which end and start fit inside a given gap. Queried by NbCouples and Couple
        """
    def SetMode(self,mode3d : bool,tol : float) -> None: 
        """
        Sets new values. Clears the connexion list If <mode3d> changes, also clears the edge list (else, doesn't)
        """
    def Status(self) -> int: 
        """
        Returns the status of the order (0 if not done) : 0 : all edges are direct and in sequence 1 : all edges are direct but some are not in sequence 2 : in addition, unresolved gaps remain -1 : some edges are reversed, but no gap remain -2 : some edges are reversed and some gaps remain -10 : COULD NOT BE RESOLVED, Failure on Reorder gap : regarding starting <tol>
        """
    def Tolerance(self) -> float: 
        """
        Returns the working tolerance
        """
    def XY(self,num : int,start2d : OCP.gp.gp_XY,end2d : OCP.gp.gp_XY) -> None: 
        """
        Returns the values of the couple <num>, as 2D values
        """
    def XYZ(self,num : int,start3d : OCP.gp.gp_XYZ,end3d : OCP.gp.gp_XYZ) -> None: 
        """
        Returns the values of the couple <num>, as 3D values
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,mode3d : bool,tol : float) -> None: ...
    @property
    def KeepLoopsMode(self) -> bool:
        """
        If this mode is True method perform does not sort edges of different loops. The resulting order is first loop, second one etc...

        :type: bool
        """
    @KeepLoopsMode.setter
    def KeepLoopsMode(self, arg1: bool) -> None:
        """
        If this mode is True method perform does not sort edges of different loops. The resulting order is first loop, second one etc...
        """
    pass
class ShapeAnalysis_WireVertex():
    """
    Analyzes and records status of vertices in a Wire
    """
    def Analyze(self) -> None: 
        """
        None
        """
    def Data(self,num : int,pos : OCP.gp.gp_XYZ,upre : float,ufol : float) -> int: 
        """
        Returns the recorded status for a vertex With its recorded position and parameters on both edges These values are relevant regarding the status: Status Meaning Position Preceding Following 0 Same no no no 1 SameCoord no no no 2 Close no no no 3 End yes no yes 4 Start yes yes no 5 Inters yes yes yes -1 Disjoined no no no
        """
    @overload
    def Init(self,swbd : OCP.ShapeExtend.ShapeExtend_WireData,preci : float) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,wire : OCP.TopoDS.TopoDS_Wire,preci : float) -> None: ...
    def IsDone(self) -> bool: 
        """
        Returns True if analysis was performed, else returns False
        """
    @overload
    def Load(self,wire : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        None

        None
        """
    @overload
    def Load(self,sbwd : OCP.ShapeExtend.ShapeExtend_WireData) -> None: ...
    def NbEdges(self) -> int: 
        """
        Returns the number of edges in analyzed wire (i.e. the length of all arrays)
        """
    def NextCriter(self,crit : int,num : int=0) -> int: 
        """
        For a given criter, returns the rank of the vertex which follows <num> and has the same status. 0 if no more Acts as an iterator, starts on the first one Criters are: 0: same vertex (status 0) 1: a solution exists (status >= 0) 2: same coords (i.e. same params) (status 0 1 2) 3: same coods but not same vertex (status 1 2) 4: redefined coords (status 3 4 5) -1: no solution (status -1)
        """
    def NextStatus(self,stat : int,num : int=0) -> int: 
        """
        For a given status, returns the rank of the vertex which follows <num> and has the same status. 0 if no more Acts as an iterator, starts on the first one
        """
    def Position(self,num : int) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def Precision(self) -> float: 
        """
        Returns precision value used in analysis
        """
    def SetClose(self,num : int) -> None: 
        """
        Records status "Close Coords" (at the Precision of <me>)
        """
    def SetDisjoined(self,num : int) -> None: 
        """
        <num> cannot be said as same vertex
        """
    def SetEnd(self,num : int,pos : OCP.gp.gp_XYZ,ufol : float) -> None: 
        """
        <num> is the End of preceding Edge, and its projection on the following one lies on it at the Precision of <me> <ufol> gives the parameter on the following edge
        """
    def SetInters(self,num : int,pos : OCP.gp.gp_XYZ,upre : float,ufol : float) -> None: 
        """
        <num> is the Intersection of both Edges <upre> is the parameter on preceding edge, <ufol> on following edge
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets the precision for work Analysing: for each Vertex, comparison between the end of the preceding edge and the start of the following edge Each Vertex rank corresponds to the End Vertex of the Edge of same rank, in the ShapeExtend_WireData. I.E. for Vertex <num>, Edge <num> is the preceding one, <num+1> is the following one
        """
    def SetSameCoords(self,num : int) -> None: 
        """
        Records status "Same Coords" (at the Vertices Tolerances)
        """
    def SetSameVertex(self,num : int) -> None: 
        """
        Records status "Same Vertex" (logically) on Vertex <num>
        """
    def SetStart(self,num : int,pos : OCP.gp.gp_XYZ,upre : float) -> None: 
        """
        <num> is the Start of following Edge, its projection on the preceding one lies on it at the Precision of <me> <upre> gives the parameter on the preceding edge
        """
    def Status(self,num : int) -> int: 
        """
        Returns the recorded status for a vertex More detail by method Data
        """
    def UFollowing(self,num : int) -> float: 
        """
        None
        """
    def UPrevious(self,num : int) -> float: 
        """
        None
        """
    def WireData(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        Returns analyzed wire
        """
    def __init__(self) -> None: ...
    pass
