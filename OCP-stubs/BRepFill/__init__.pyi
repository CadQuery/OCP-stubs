import OCP.BRepFill
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Bisector
import OCP.NCollection
import OCP.MAT
import OCP.Law
import OCP.AppParCurves
import OCP.AppCont
import OCP.Geom
import OCP.TColgp
import OCP.TopoDS
import OCP.GeomFill
import OCP.GeomPlate
import OCP.Standard
import OCP.Adaptor3d
import OCP.TopTools
import OCP.TColStd
import io
import OCP.Adaptor2d
import OCP.gp
import OCP.GeomAbs
import OCP.GeomLProp
import OCP.BRepMAT2d
import OCP.Geom2d
__all__  = [
"BRepFill",
"BRepFill_LocationLaw",
"BRepFill_AdvancedEvolved",
"BRepFill_ApproxSeewing",
"BRepFill_CompatibleWires",
"BRepFill_ComputeCLine",
"BRepFill_CurveConstraint",
"BRepFill_DataMapOfNodeDataMapOfShapeShape",
"BRepFill_DataMapOfNodeShape",
"BRepFill_DataMapOfOrientedShapeListOfShape",
"BRepFill_DataMapOfShapeDataMapOfShapeListOfShape",
"BRepFill_DataMapOfShapeSequenceOfPnt",
"BRepFill_DataMapOfShapeSequenceOfReal",
"BRepFill_Draft",
"BRepFill_Edge3DLaw",
"BRepFill_DraftLaw",
"BRepFill_EdgeFaceAndOrder",
"BRepFill_EdgeOnSurfLaw",
"BRepFill_Evolved",
"BRepFill_FaceAndOrder",
"BRepFill_Filling",
"BRepFill_Generator",
"BRepFill_IndexedDataMapOfOrientedShapeListOfShape",
"BRepFill_ListOfOffsetWire",
"BRepFill_ACRLaw",
"BRepFill_MultiLine",
"BRepFill_SectionLaw",
"BRepFill_OffsetAncestors",
"BRepFill_OffsetWire",
"BRepFill_Pipe",
"BRepFill_PipeShell",
"BRepFill_Section",
"BRepFill_NSections",
"BRepFill_SectionPlacement",
"BRepFill_SequenceOfEdgeFaceAndOrder",
"BRepFill_SequenceOfFaceAndOrder",
"BRepFill_SequenceOfSection",
"BRepFill_ShapeLaw",
"BRepFill_Sweep",
"BRepFill_TransitionStyle",
"BRepFill_TrimEdgeTool",
"BRepFill_TrimShellCorner",
"BRepFill_TrimSurfaceTool",
"BRepFill_TypeOfContact",
"BRepFill_Contact",
"BRepFill_ContactOnBorder",
"BRepFill_Modified",
"BRepFill_NoContact",
"BRepFill_Right",
"BRepFill_Round"
]
class BRepFill():
    """
    None
    """
    @staticmethod
    def Axe_s(Spine : OCP.TopoDS.TopoDS_Shape,Profile : OCP.TopoDS.TopoDS_Wire,AxeProf : OCP.gp.gp_Ax3,Tol : float) -> Tuple[bool]: 
        """
        Computes <AxeProf> as Follow. <Location> is the Position of the nearest vertex V of <Profile> to <Spine>.<XDirection> is confused with the tangent to <Spine> at the projected point of V on the Spine. <Direction> is normal to <Spine>. <Spine> is a plane wire or a plane face.
        """
    @staticmethod
    def ComputeACR_s(wire : OCP.TopoDS.TopoDS_Wire,ACR : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        Compute ACR on a wire
        """
    @staticmethod
    def Face_s(Edge1 : OCP.TopoDS.TopoDS_Edge,Edge2 : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Face: 
        """
        Computes a ruled surface between two edges.
        """
    @staticmethod
    def InsertACR_s(wire : OCP.TopoDS.TopoDS_Wire,ACRcuts : OCP.TColStd.TColStd_Array1OfReal,prec : float) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Insert ACR on a wire
        """
    @staticmethod
    def Shell_s(Wire1 : OCP.TopoDS.TopoDS_Wire,Wire2 : OCP.TopoDS.TopoDS_Wire) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Computes a ruled surface between two wires. The wires must have the same number of edges.
        """
    def __init__(self) -> None: ...
    pass
class BRepFill_LocationLaw(OCP.Standard.Standard_Transient):
    """
    Location Law on a Wire.Location Law on a Wire.Location Law on a Wire.
    """
    def Abscissa(self,Index : int,Param : float) -> float: 
        """
        Return the curvilinear abscissa corresponding to a point of the path, defined by <Index> of Edge and a parameter on the edge.
        """
    def CurvilinearBounds(self,Index : int) -> Tuple[float, float]: 
        """
        Return the Curvilinear Bounds of the <Index> Law
        """
    def D0(self,Abscissa : float,Section : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Apply the Law to a shape, for a given Curnilinear abscissa
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeleteTransform(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self,Index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Return the Edge of rank <Index> in the path <Index> have to be in [1, NbLaw()]
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> OCP.GeomFill.GeomFill_PipeError: 
        """
        Return a error status, if the status is not PipeOk then it exist a parameter tlike the law is not valuable for t.
        """
    def Holes(self,Interval : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsG1(self,Index : int,SpatialTolerance : float=1e-07,AngularTolerance : float=0.0001) -> int: 
        """
        Compute the Law's continuity beetween 2 edges of the path The result can be : -1 : Case Not connex 0 : It is connex (G0) 1 : It is tangent (G1)
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
    def Law(self,Index : int) -> OCP.GeomFill.GeomFill_LocationLaw: 
        """
        Return the elementary Law of rank <Index> <Index> have to be in [1, NbLaw()]
        """
    def NbHoles(self,Tol : float=1e-07) -> int: 
        """
        None
        """
    def NbLaw(self) -> int: 
        """
        Return the number of elementary Law
        """
    def Parameter(self,Abscissa : float) -> Tuple[int, float]: 
        """
        Find the index Law and the parmaeter, for a given Curnilinear abscissa
        """
    def PerformVertex(self,Index : int,InputVertex : OCP.TopoDS.TopoDS_Vertex,TolMin : float,OutputVertex : OCP.TopoDS.TopoDS_Vertex,Location : int=0) -> None: 
        """
        Compute <OutputVertex> like a transformation of <InputVertex> the transformation is given by evaluation of the location law in the vertex of rank <Index>. <Location> is used to manage discontinuities : - -1 : The law before the vertex is used. - 1 : The law after the vertex is used. - 0 : Average of the both laws is used.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformInCompatibleLaw(self,AngularTolerance : float) -> None: 
        """
        Apply a linear transformation on each law, to reduce the dicontinuities of law at one rotation.
        """
    def TransformInG0Law(self) -> None: 
        """
        Apply a linear transformation on each law, to have continuity of the global law beetween the edges.
        """
    def Vertex(self,Index : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Return the vertex of rank <Index> in the path <Index> have to be in [0, NbLaw()]
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        return the path
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
class BRepFill_AdvancedEvolved():
    """
    Constructs an evolved volume from a spine (wire or face) and a profile ( wire).
    """
    def IsDone(self,theErrorCode : int=None) -> bool: 
        """
        None
        """
    def Perform(self,theSpine : OCP.TopoDS.TopoDS_Wire,theProfile : OCP.TopoDS.TopoDS_Wire,theTolerance : float,theSolidReq : bool=True) -> None: 
        """
        None
        """
    def SetParallelMode(self,theVal : bool) -> None: 
        """
        Sets/Unsets computation in parallel mode
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns the resulting shape.
        """
    def __init__(self) -> None: ...
    pass
class BRepFill_ApproxSeewing():
    """
    Evaluate the 3dCurve and the PCurves described in a MultiLine from BRepFill. The parametrization of those curves is not imposed by the Bissectrice. The parametrization is given approximatively by the abscissa of the curve3d.
    """
    def Curve(self) -> OCP.Geom.Geom_Curve: 
        """
        returns the approximation of the 3d Curve
        """
    def CurveOnF1(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        returns the approximation of the PCurve on the first face of the MultiLine
        """
    def CurveOnF2(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        returns the approximation of the PCurve on the first face of the MultiLine
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Perform(self,ML : BRepFill_MultiLine) -> None: 
        """
        None
        """
    @overload
    def __init__(self,ML : BRepFill_MultiLine) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFill_CompatibleWires():
    """
    Constructs a sequence of Wires (with good orientation and origin) agreed each other so that the surface passing through these sections is not twisted
    """
    def Generated(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        None
        """
    def GeneratedShapes(self,SubSection : OCP.TopoDS.TopoDS_Edge) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes created from a subshape <SubSection> of a section.
        """
    def Init(self,Sections : OCP.TopTools.TopTools_SequenceOfShape) -> None: 
        """
        None
        """
    def IsDegeneratedFirstSection(self) -> bool: 
        """
        None
        """
    def IsDegeneratedLastSection(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Perform(self,WithRotation : bool=True) -> None: 
        """
        Performs CompatibleWires According to the orientation and the origin of each other
        """
    def SetPercent(self,percent : float=0.01) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        returns the generated sequence.
        """
    @overload
    def __init__(self,Sections : OCP.TopTools.TopTools_SequenceOfShape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFill_ComputeCLine():
    """
    None
    """
    def Error(self,Index : int) -> Tuple[float, float]: 
        """
        returns the tolerances 2d and 3d of the <Index> MultiCurve.
        """
    def IsAllApproximated(self) -> bool: 
        """
        returns False if at a moment of the approximation, the status NoApproximation has been sent by the user when more points were needed.
        """
    def IsToleranceReached(self) -> bool: 
        """
        returns False if the status NoPointsAdded has been sent.
        """
    def NbMultiCurves(self) -> int: 
        """
        Returns the number of MultiCurve doing the approximation of the MultiLine.
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        None
        """
    def Perform(self,Line : BRepFill_MultiLine) -> None: 
        """
        runs the algorithm after having initialized the fields.
        """
    def SetConstraints(self,FirstC : OCP.AppParCurves.AppParCurves_Constraint,LastC : OCP.AppParCurves.AppParCurves_Constraint) -> None: 
        """
        Changes the constraints of the approximation.
        """
    def SetDegrees(self,degreemin : int,degreemax : int) -> None: 
        """
        changes the degrees of the approximation.
        """
    def SetHangChecking(self,theHangChecking : bool) -> None: 
        """
        Set value of hang checking flag if this flag = true, possible hang of algorithm is checked and algorithm is forced to stop. By default hang checking is used.
        """
    def SetInvOrder(self,theInvOrder : bool) -> None: 
        """
        Set inverse order of degree selection: if theInvOrdr = true, current degree is chosen by inverse order - from maxdegree to mindegree. By default inverse order is used.
        """
    def SetMaxSegments(self,theMaxSegments : int) -> None: 
        """
        Changes the max number of segments, which is allowed for cutting.
        """
    def SetTolerances(self,Tolerance3d : float,Tolerance2d : float) -> None: 
        """
        Changes the tolerances of the approximation.
        """
    def Value(self,Index : int=1) -> OCP.AppParCurves.AppParCurves_MultiCurve: 
        """
        returns the approximation MultiCurve of range <Index>.
        """
    @overload
    def __init__(self,degreemin : int=3,degreemax : int=8,Tolerance3d : float=1e-05,Tolerance2d : float=1e-05,cutting : bool=False,FirstC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint,LastC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint) -> None: ...
    @overload
    def __init__(self,Line : BRepFill_MultiLine,degreemin : int=3,degreemax : int=8,Tolerance3d : float=1e-05,Tolerance2d : float=1e-05,cutting : bool=False,FirstC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint,LastC : OCP.AppParCurves.AppParCurves_Constraint=AppParCurves_Constraint.AppParCurves_TangencyPoint) -> None: ...
    pass
class BRepFill_CurveConstraint(OCP.GeomPlate.GeomPlate_CurveConstraint, OCP.Standard.Standard_Transient):
    """
    same as CurveConstraint from GeomPlate with BRepAdaptor_Surface instead of GeomAdaptor_Surfacesame as CurveConstraint from GeomPlate with BRepAdaptor_Surface instead of GeomAdaptor_Surfacesame as CurveConstraint from GeomPlate with BRepAdaptor_Surface instead of GeomAdaptor_Surface
    """
    def Curve2dOnSurf(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns a 2d curve associated the surface resulting of the constraints
        """
    def Curve3d(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec,V4 : OCP.gp.gp_Vec,V5 : OCP.gp.gp_Vec) -> None: 
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
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstParameter(self) -> float: 
        """
        None
        """
    def G0Criterion(self,U : float) -> float: 
        """
        Returns the G0 criterion at the parametric point U on the curve. This is the greatest distance allowed between the constraint and the target surface at U.
        """
    def G1Criterion(self,U : float) -> float: 
        """
        Returns the G1 criterion at the parametric point U on the curve. This is the greatest angle allowed between the constraint and the target surface at U. Raises ConstructionError if the curve is not on a surface
        """
    def G2Criterion(self,U : float) -> float: 
        """
        Returns the G2 criterion at the parametric point U on the curve. This is the greatest difference in curvature allowed between the constraint and the target surface at U. Raises ConstructionError if the curve is not on a surface
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
    def LPropSurf(self,U : float) -> OCP.GeomLProp.GeomLProp_SLProps: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        None
        """
    def Length(self) -> float: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points on the curve used as a constraint. The default setting is 10. This parameter affects computation time, which increases by the cube of the number of points.
        """
    def Order(self) -> int: 
        """
        Returns the order of constraint, one of G0, G1 or G2.
        """
    def ProjectedCurve(self) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        Returns the projected curve resulting from the normal projection of the curve on the initial surface
        """
    def SetCurve2dOnSurf(self,Curve2d : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        loads a 2d curve associated the surface resulting of the constraints
        """
    def SetG0Criterion(self,G0Crit : OCP.Law.Law_Function) -> None: 
        """
        Allows you to set the G0 criterion. This is the law defining the greatest distance allowed between the constraint and the target surface for each point of the constraint. If this criterion is not set, TolDist, the distance tolerance from the constructor, is used.
        """
    def SetG1Criterion(self,G1Crit : OCP.Law.Law_Function) -> None: 
        """
        Allows you to set the G1 criterion. This is the law defining the greatest angle allowed between the constraint and the target surface. If this criterion is not set, TolAng, the angular tolerance from the constructor, is used. Raises ConstructionError if the curve is not on a surface
        """
    def SetG2Criterion(self,G2Crit : OCP.Law.Law_Function) -> None: 
        """
        None
        """
    def SetNbPoints(self,NewNb : int) -> None: 
        """
        Allows you to set the number of points on the curve constraint. The default setting is 10. This parameter affects computation time, which increases by the cube of the number of points.
        """
    def SetOrder(self,Order : int) -> None: 
        """
        Allows you to set the order of continuity required for the constraints: G0, G1, and G2, controlled respectively by G0Criterion G1Criterion and G2Criterion.
        """
    def SetProjectedCurve(self,Curve2d : OCP.Adaptor2d.Adaptor2d_HCurve2d,TolU : float,TolV : float) -> None: 
        """
        loads a 2d curve resulting from the normal projection of the curve on the initial surface
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,Boundary : OCP.Adaptor3d.Adaptor3d_HCurveOnSurface,Order : int,NPt : int=10,TolDist : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1) -> None: ...
    @overload
    def __init__(self,Boundary : OCP.Adaptor3d.Adaptor3d_HCurve,Tang : int,NPt : int=10,TolDist : float=0.0001) -> None: ...
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
class BRepFill_DataMapOfNodeDataMapOfShapeShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepFill_DataMapOfNodeDataMapOfShapeShape) -> BRepFill_DataMapOfNodeDataMapOfShapeShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.MAT.MAT_Node,theItem : OCP.TopTools.TopTools_DataMapOfShapeShape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.MAT.MAT_Node,theItem : OCP.TopTools.TopTools_DataMapOfShapeShape) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.MAT.MAT_Node) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.MAT.MAT_Node) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
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
    def Exchange(self,theOther : BRepFill_DataMapOfNodeDataMapOfShapeShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.MAT.MAT_Node,theValue : OCP.TopTools.TopTools_DataMapOfShapeShape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.MAT.MAT_Node) -> OCP.TopTools.TopTools_DataMapOfShapeShape: ...
    def IsBound(self,theKey : OCP.MAT.MAT_Node) -> bool: 
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
    def Seek(self,theKey : OCP.MAT.MAT_Node) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
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
    def UnBind(self,theKey : OCP.MAT.MAT_Node) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BRepFill_DataMapOfNodeDataMapOfShapeShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepFill_DataMapOfNodeShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepFill_DataMapOfNodeShape) -> BRepFill_DataMapOfNodeShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.MAT.MAT_Node,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.MAT.MAT_Node,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.MAT.MAT_Node) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.MAT.MAT_Node) -> OCP.TopoDS.TopoDS_Shape: 
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
    def Exchange(self,theOther : BRepFill_DataMapOfNodeShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.MAT.MAT_Node) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.MAT.MAT_Node,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def IsBound(self,theKey : OCP.MAT.MAT_Node) -> bool: 
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
    def Seek(self,theKey : OCP.MAT.MAT_Node) -> OCP.TopoDS.TopoDS_Shape: 
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
    def UnBind(self,theKey : OCP.MAT.MAT_Node) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BRepFill_DataMapOfNodeShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepFill_DataMapOfOrientedShapeListOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepFill_DataMapOfOrientedShapeListOfShape) -> BRepFill_DataMapOfOrientedShapeListOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopTools.TopTools_ListOfShape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
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
    def Exchange(self,theOther : BRepFill_DataMapOfOrientedShapeListOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TopTools.TopTools_ListOfShape) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
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
    def __init__(self,theOther : BRepFill_DataMapOfOrientedShapeListOfShape) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepFill_DataMapOfShapeDataMapOfShapeListOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepFill_DataMapOfShapeDataMapOfShapeListOfShape) -> BRepFill_DataMapOfShapeDataMapOfShapeListOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
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
    def Exchange(self,theOther : BRepFill_DataMapOfShapeDataMapOfShapeListOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
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
    def __init__(self,theOther : BRepFill_DataMapOfShapeDataMapOfShapeListOfShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepFill_DataMapOfShapeSequenceOfPnt(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepFill_DataMapOfShapeSequenceOfPnt) -> BRepFill_DataMapOfShapeSequenceOfPnt: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColgp.TColgp_SequenceOfPnt) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColgp.TColgp_SequenceOfPnt) -> OCP.TColgp.TColgp_SequenceOfPnt: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColgp.TColgp_SequenceOfPnt: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColgp.TColgp_SequenceOfPnt: 
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
    def Exchange(self,theOther : BRepFill_DataMapOfShapeSequenceOfPnt) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColgp.TColgp_SequenceOfPnt: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TColgp.TColgp_SequenceOfPnt) -> bool: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColgp.TColgp_SequenceOfPnt: 
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
    def __init__(self,theOther : BRepFill_DataMapOfShapeSequenceOfPnt) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepFill_DataMapOfShapeSequenceOfReal(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepFill_DataMapOfShapeSequenceOfReal) -> BRepFill_DataMapOfShapeSequenceOfReal: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColStd.TColStd_SequenceOfReal) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TColStd.TColStd_SequenceOfReal) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_SequenceOfReal: 
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
    def Exchange(self,theOther : BRepFill_DataMapOfShapeSequenceOfReal) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TColStd.TColStd_SequenceOfReal) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_SequenceOfReal: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TColStd.TColStd_SequenceOfReal: 
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
    def __init__(self,theOther : BRepFill_DataMapOfShapeSequenceOfReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepFill_Draft():
    """
    None
    """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    @overload
    def Perform(self,LengthMax : float) -> None: 
        """
        None

        None

        None
        """
    @overload
    def Perform(self,StopShape : OCP.TopoDS.TopoDS_Shape,KeepOutSide : bool=True) -> None: ...
    @overload
    def Perform(self,Surface : OCP.Geom.Geom_Surface,KeepInsideSurface : bool=True) -> None: ...
    def SetDraft(self,IsInternal : bool=False) -> None: 
        """
        None
        """
    def SetOptions(self,Style : BRepFill_TransitionStyle=BRepFill_TransitionStyle.BRepFill_Right,AngleMin : float=0.01,AngleMax : float=3.0) -> None: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the draft surface To have the complete shape you have to use the Shape() methode.
        """
    def __init__(self,Shape : OCP.TopoDS.TopoDS_Shape,Dir : OCP.gp.gp_Dir,Angle : float) -> None: ...
    pass
class BRepFill_Edge3DLaw(BRepFill_LocationLaw, OCP.Standard.Standard_Transient):
    """
    Build Location Law, with a Wire.Build Location Law, with a Wire.Build Location Law, with a Wire.
    """
    def Abscissa(self,Index : int,Param : float) -> float: 
        """
        Return the curvilinear abscissa corresponding to a point of the path, defined by <Index> of Edge and a parameter on the edge.
        """
    def CurvilinearBounds(self,Index : int) -> Tuple[float, float]: 
        """
        Return the Curvilinear Bounds of the <Index> Law
        """
    def D0(self,Abscissa : float,Section : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Apply the Law to a shape, for a given Curnilinear abscissa
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeleteTransform(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self,Index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Return the Edge of rank <Index> in the path <Index> have to be in [1, NbLaw()]
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> OCP.GeomFill.GeomFill_PipeError: 
        """
        Return a error status, if the status is not PipeOk then it exist a parameter tlike the law is not valuable for t.
        """
    def Holes(self,Interval : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsG1(self,Index : int,SpatialTolerance : float=1e-07,AngularTolerance : float=0.0001) -> int: 
        """
        Compute the Law's continuity beetween 2 edges of the path The result can be : -1 : Case Not connex 0 : It is connex (G0) 1 : It is tangent (G1)
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
    def Law(self,Index : int) -> OCP.GeomFill.GeomFill_LocationLaw: 
        """
        Return the elementary Law of rank <Index> <Index> have to be in [1, NbLaw()]
        """
    def NbHoles(self,Tol : float=1e-07) -> int: 
        """
        None
        """
    def NbLaw(self) -> int: 
        """
        Return the number of elementary Law
        """
    def Parameter(self,Abscissa : float) -> Tuple[int, float]: 
        """
        Find the index Law and the parmaeter, for a given Curnilinear abscissa
        """
    def PerformVertex(self,Index : int,InputVertex : OCP.TopoDS.TopoDS_Vertex,TolMin : float,OutputVertex : OCP.TopoDS.TopoDS_Vertex,Location : int=0) -> None: 
        """
        Compute <OutputVertex> like a transformation of <InputVertex> the transformation is given by evaluation of the location law in the vertex of rank <Index>. <Location> is used to manage discontinuities : - -1 : The law before the vertex is used. - 1 : The law after the vertex is used. - 0 : Average of the both laws is used.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformInCompatibleLaw(self,AngularTolerance : float) -> None: 
        """
        Apply a linear transformation on each law, to reduce the dicontinuities of law at one rotation.
        """
    def TransformInG0Law(self) -> None: 
        """
        Apply a linear transformation on each law, to have continuity of the global law beetween the edges.
        """
    def Vertex(self,Index : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Return the vertex of rank <Index> in the path <Index> have to be in [0, NbLaw()]
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        return the path
        """
    def __init__(self,Path : OCP.TopoDS.TopoDS_Wire,Law : OCP.GeomFill.GeomFill_LocationLaw) -> None: ...
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
class BRepFill_DraftLaw(BRepFill_Edge3DLaw, BRepFill_LocationLaw, OCP.Standard.Standard_Transient):
    """
    Build Location Law, with a Wire.Build Location Law, with a Wire.Build Location Law, with a Wire.
    """
    def Abscissa(self,Index : int,Param : float) -> float: 
        """
        Return the curvilinear abscissa corresponding to a point of the path, defined by <Index> of Edge and a parameter on the edge.
        """
    def CleanLaw(self,TolAngular : float) -> None: 
        """
        To clean the little discontinuities.
        """
    def CurvilinearBounds(self,Index : int) -> Tuple[float, float]: 
        """
        Return the Curvilinear Bounds of the <Index> Law
        """
    def D0(self,Abscissa : float,Section : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Apply the Law to a shape, for a given Curnilinear abscissa
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeleteTransform(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self,Index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Return the Edge of rank <Index> in the path <Index> have to be in [1, NbLaw()]
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> OCP.GeomFill.GeomFill_PipeError: 
        """
        Return a error status, if the status is not PipeOk then it exist a parameter tlike the law is not valuable for t.
        """
    def Holes(self,Interval : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsG1(self,Index : int,SpatialTolerance : float=1e-07,AngularTolerance : float=0.0001) -> int: 
        """
        Compute the Law's continuity beetween 2 edges of the path The result can be : -1 : Case Not connex 0 : It is connex (G0) 1 : It is tangent (G1)
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
    def Law(self,Index : int) -> OCP.GeomFill.GeomFill_LocationLaw: 
        """
        Return the elementary Law of rank <Index> <Index> have to be in [1, NbLaw()]
        """
    def NbHoles(self,Tol : float=1e-07) -> int: 
        """
        None
        """
    def NbLaw(self) -> int: 
        """
        Return the number of elementary Law
        """
    def Parameter(self,Abscissa : float) -> Tuple[int, float]: 
        """
        Find the index Law and the parmaeter, for a given Curnilinear abscissa
        """
    def PerformVertex(self,Index : int,InputVertex : OCP.TopoDS.TopoDS_Vertex,TolMin : float,OutputVertex : OCP.TopoDS.TopoDS_Vertex,Location : int=0) -> None: 
        """
        Compute <OutputVertex> like a transformation of <InputVertex> the transformation is given by evaluation of the location law in the vertex of rank <Index>. <Location> is used to manage discontinuities : - -1 : The law before the vertex is used. - 1 : The law after the vertex is used. - 0 : Average of the both laws is used.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformInCompatibleLaw(self,AngularTolerance : float) -> None: 
        """
        Apply a linear transformation on each law, to reduce the dicontinuities of law at one rotation.
        """
    def TransformInG0Law(self) -> None: 
        """
        Apply a linear transformation on each law, to have continuity of the global law beetween the edges.
        """
    def Vertex(self,Index : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Return the vertex of rank <Index> in the path <Index> have to be in [0, NbLaw()]
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        return the path
        """
    def __init__(self,Path : OCP.TopoDS.TopoDS_Wire,Law : OCP.GeomFill.GeomFill_LocationDraft) -> None: ...
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
class BRepFill_EdgeFaceAndOrder():
    """
    None
    """
    @overload
    def __init__(self,anEdge : OCP.TopoDS.TopoDS_Edge,aFace : OCP.TopoDS.TopoDS_Face,anOrder : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFill_EdgeOnSurfLaw(BRepFill_LocationLaw, OCP.Standard.Standard_Transient):
    """
    Build Location Law, with a Wire and a Surface.Build Location Law, with a Wire and a Surface.Build Location Law, with a Wire and a Surface.
    """
    def Abscissa(self,Index : int,Param : float) -> float: 
        """
        Return the curvilinear abscissa corresponding to a point of the path, defined by <Index> of Edge and a parameter on the edge.
        """
    def CurvilinearBounds(self,Index : int) -> Tuple[float, float]: 
        """
        Return the Curvilinear Bounds of the <Index> Law
        """
    def D0(self,Abscissa : float,Section : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Apply the Law to a shape, for a given Curnilinear abscissa
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeleteTransform(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self,Index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Return the Edge of rank <Index> in the path <Index> have to be in [1, NbLaw()]
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> OCP.GeomFill.GeomFill_PipeError: 
        """
        Return a error status, if the status is not PipeOk then it exist a parameter tlike the law is not valuable for t.
        """
    def HasResult(self) -> bool: 
        """
        returns <False> if one Edge of <Path> do not have representation on <Surf>. In this case it is impossible to use this object.
        """
    def Holes(self,Interval : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsG1(self,Index : int,SpatialTolerance : float=1e-07,AngularTolerance : float=0.0001) -> int: 
        """
        Compute the Law's continuity beetween 2 edges of the path The result can be : -1 : Case Not connex 0 : It is connex (G0) 1 : It is tangent (G1)
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
    def Law(self,Index : int) -> OCP.GeomFill.GeomFill_LocationLaw: 
        """
        Return the elementary Law of rank <Index> <Index> have to be in [1, NbLaw()]
        """
    def NbHoles(self,Tol : float=1e-07) -> int: 
        """
        None
        """
    def NbLaw(self) -> int: 
        """
        Return the number of elementary Law
        """
    def Parameter(self,Abscissa : float) -> Tuple[int, float]: 
        """
        Find the index Law and the parmaeter, for a given Curnilinear abscissa
        """
    def PerformVertex(self,Index : int,InputVertex : OCP.TopoDS.TopoDS_Vertex,TolMin : float,OutputVertex : OCP.TopoDS.TopoDS_Vertex,Location : int=0) -> None: 
        """
        Compute <OutputVertex> like a transformation of <InputVertex> the transformation is given by evaluation of the location law in the vertex of rank <Index>. <Location> is used to manage discontinuities : - -1 : The law before the vertex is used. - 1 : The law after the vertex is used. - 0 : Average of the both laws is used.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformInCompatibleLaw(self,AngularTolerance : float) -> None: 
        """
        Apply a linear transformation on each law, to reduce the dicontinuities of law at one rotation.
        """
    def TransformInG0Law(self) -> None: 
        """
        Apply a linear transformation on each law, to have continuity of the global law beetween the edges.
        """
    def Vertex(self,Index : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Return the vertex of rank <Index> in the path <Index> have to be in [0, NbLaw()]
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        return the path
        """
    def __init__(self,Path : OCP.TopoDS.TopoDS_Wire,Surf : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BRepFill_Evolved():
    """
    Constructs an evolved volume from a spine (wire or face) and a profile ( wire).
    """
    def Bottom(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Return the face Bottom if <Solid> is True in the constructor.
        """
    def GeneratedShapes(self,SpineShape : OCP.TopoDS.TopoDS_Shape,ProfShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes created from a subshape <SpineShape> of the spine and a subshape <ProfShape> on the profile.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def JoinType(self) -> OCP.GeomAbs.GeomAbs_JoinType: 
        """
        None
        """
    @overload
    def Perform(self,Spine : OCP.TopoDS.TopoDS_Face,Profile : OCP.TopoDS.TopoDS_Wire,AxeProf : OCP.gp.gp_Ax3,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,Solid : bool=False) -> None: 
        """
        Performs an evolved shape by sweeping the <Profile> along the <Spine>

        Performs an evolved shape by sweeping the <Profile> along the <Spine>
        """
    @overload
    def Perform(self,Spine : OCP.TopoDS.TopoDS_Wire,Profile : OCP.TopoDS.TopoDS_Wire,AxeProf : OCP.gp.gp_Ax3,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,Solid : bool=False) -> None: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns the generated shape.
        """
    def Top(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Return the face Top if <Solid> is True in the constructor.
        """
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Face,Profile : OCP.TopoDS.TopoDS_Wire,AxeProf : OCP.gp.gp_Ax3,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,Solid : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Wire,Profile : OCP.TopoDS.TopoDS_Wire,AxeProf : OCP.gp.gp_Ax3,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,Solid : bool=False) -> None: ...
    pass
class BRepFill_FaceAndOrder():
    """
    A structure containing Face and Order of constraint
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aFace : OCP.TopoDS.TopoDS_Face,anOrder : OCP.GeomAbs.GeomAbs_Shape) -> None: ...
    pass
class BRepFill_Filling():
    """
    N-Side Filling This algorithm avoids to build a face from: * a set of edges defining the bounds of the face and some constraints the surface support has to satisfy * a set of edges and points defining some constraints the support surface has to satisfy * an initial surface to deform for satisfying the constraints * a set of parameters to control the constraints.
    """
    @overload
    def Add(self,Support : OCP.TopoDS.TopoDS_Face,Order : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Adds a new constraint which also defines an edge of the wire of the face Order: Order of the constraint: GeomAbs_C0 : the surface has to pass by 3D representation of the edge GeomAbs_G1 : the surface has to pass by 3D representation of the edge and to respect tangency with the first face of the edge GeomAbs_G2 : the surface has to pass by 3D representation of the edge and to respect tangency and curvature with the first face of the edge.

        Adds a new constraint which also defines an edge of the wire of the face Order: Order of the constraint: GeomAbs_C0 : the surface has to pass by 3D representation of the edge GeomAbs_G1 : the surface has to pass by 3D representation of the edge and to respect tangency with the given face GeomAbs_G2 : the surface has to pass by 3D representation of the edge and to respect tangency and curvature with the given face.

        Adds a free constraint on a face. The corresponding edge has to be automatically recomputed. It is always a bound.

        Adds a punctual constraint

        Adds a punctual constraint.
        """
    @overload
    def Add(self,Point : OCP.gp.gp_Pnt) -> int: ...
    @overload
    def Add(self,anEdge : OCP.TopoDS.TopoDS_Edge,Support : OCP.TopoDS.TopoDS_Face,Order : OCP.GeomAbs.GeomAbs_Shape,IsBound : bool=True) -> int: ...
    @overload
    def Add(self,U : float,V : float,Support : OCP.TopoDS.TopoDS_Face,Order : OCP.GeomAbs.GeomAbs_Shape) -> int: ...
    @overload
    def Add(self,anEdge : OCP.TopoDS.TopoDS_Edge,Order : OCP.GeomAbs.GeomAbs_Shape,IsBound : bool=True) -> int: ...
    def Build(self) -> None: 
        """
        Builds the resulting faces
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    @overload
    def G0Error(self) -> float: 
        """
        None

        None
        """
    @overload
    def G0Error(self,Index : int) -> float: ...
    @overload
    def G1Error(self,Index : int) -> float: 
        """
        None

        None
        """
    @overload
    def G1Error(self) -> float: ...
    @overload
    def G2Error(self) -> float: 
        """
        None

        None
        """
    @overload
    def G2Error(self,Index : int) -> float: ...
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LoadInitSurface(self,aFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Loads the initial Surface The initial surface must have orthogonal local coordinates, i.e. partial derivatives dS/du and dS/dv must be orthogonal at each point of surface. If this condition breaks, distortions of resulting surface are possible.
        """
    def SetApproxParam(self,MaxDeg : int=8,MaxSegments : int=9) -> None: 
        """
        Sets the parameters used for approximation of the surface
        """
    def SetConstrParam(self,Tol2d : float=1e-05,Tol3d : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1) -> None: 
        """
        Sets the values of Tolerances used to control the constraint. Tol2d: Tol3d: it is the maximum distance allowed between the support surface and the constraints TolAng: it is the maximum angle allowed between the normal of the surface and the constraints TolCurv: it is the maximum difference of curvature allowed between the surface and the constraint
        """
    def SetResolParam(self,Degree : int=3,NbPtsOnCur : int=15,NbIter : int=2,Anisotropie : bool=False) -> None: 
        """
        Sets the parameters used for resolution. The default values of these parameters have been chosen for a good ratio quality/performance. Degree: it is the order of energy criterion to minimize for computing the deformation of the surface. The default value is 3 The recommanded value is i+2 where i is the maximum order of the constraints. NbPtsOnCur: it is the average number of points for discretisation of the edges. NbIter: it is the maximum number of iterations of the process. For each iteration the number of discretisation points is increased. Anisotropie:
        """
    def __init__(self,Degree : int=3,NbPtsOnCur : int=15,NbIter : int=2,Anisotropie : bool=False,Tol2d : float=1e-05,Tol3d : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1,MaxDeg : int=8,MaxSegments : int=9) -> None: ...
    pass
class BRepFill_Generator():
    """
    Compute a topological surface ( a shell) using generating wires. The face of the shell will be ruled surfaces passing by the wires. The wires must have the same number of edges.
    """
    def AddWire(self,Wire : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        None
        """
    def Generated(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns all the shapes created
        """
    def GeneratedShapes(self,SSection : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes created from a subshape <SSection> of a section.
        """
    def Perform(self) -> None: 
        """
        Compute the shell.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        None

        None
        """
    def __init__(self) -> None: ...
    pass
class BRepFill_IndexedDataMapOfOrientedShapeListOfShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BRepFill_IndexedDataMapOfOrientedShapeListOfShape) -> BRepFill_IndexedDataMapOfOrientedShapeListOfShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
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
    def Exchange(self,theOther : BRepFill_IndexedDataMapOfOrientedShapeListOfShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: ...
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
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
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
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopTools.TopTools_ListOfShape) -> None: 
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
    def __init__(self,theOther : BRepFill_IndexedDataMapOfOrientedShapeListOfShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepFill_ListOfOffsetWire(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BRepFill_OffsetWire,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : BRepFill_ListOfOffsetWire) -> None: ...
    @overload
    def Append(self,theItem : BRepFill_OffsetWire) -> BRepFill_OffsetWire: ...
    def Assign(self,theOther : BRepFill_ListOfOffsetWire) -> BRepFill_ListOfOffsetWire: 
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
    def First(self) -> BRepFill_OffsetWire: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : BRepFill_OffsetWire,theIter : Any) -> BRepFill_OffsetWire: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : BRepFill_ListOfOffsetWire,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : BRepFill_ListOfOffsetWire,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : BRepFill_OffsetWire,theIter : Any) -> BRepFill_OffsetWire: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BRepFill_OffsetWire: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : BRepFill_ListOfOffsetWire) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : BRepFill_OffsetWire) -> BRepFill_OffsetWire: ...
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
    def __init__(self,theOther : BRepFill_ListOfOffsetWire) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BRepFill_ACRLaw(BRepFill_LocationLaw, OCP.Standard.Standard_Transient):
    """
    Build Location Law, with a Wire. In the case of guided contour and trihedron by reduced curvilinear abscissaBuild Location Law, with a Wire. In the case of guided contour and trihedron by reduced curvilinear abscissaBuild Location Law, with a Wire. In the case of guided contour and trihedron by reduced curvilinear abscissa
    """
    def Abscissa(self,Index : int,Param : float) -> float: 
        """
        Return the curvilinear abscissa corresponding to a point of the path, defined by <Index> of Edge and a parameter on the edge.
        """
    def CurvilinearBounds(self,Index : int) -> Tuple[float, float]: 
        """
        Return the Curvilinear Bounds of the <Index> Law
        """
    def D0(self,Abscissa : float,Section : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Apply the Law to a shape, for a given Curnilinear abscissa
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeleteTransform(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self,Index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Return the Edge of rank <Index> in the path <Index> have to be in [1, NbLaw()]
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> OCP.GeomFill.GeomFill_PipeError: 
        """
        Return a error status, if the status is not PipeOk then it exist a parameter tlike the law is not valuable for t.
        """
    def Holes(self,Interval : OCP.TColStd.TColStd_Array1OfInteger) -> None: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsClosed(self) -> bool: 
        """
        None
        """
    def IsG1(self,Index : int,SpatialTolerance : float=1e-07,AngularTolerance : float=0.0001) -> int: 
        """
        Compute the Law's continuity beetween 2 edges of the path The result can be : -1 : Case Not connex 0 : It is connex (G0) 1 : It is tangent (G1)
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
    def Law(self,Index : int) -> OCP.GeomFill.GeomFill_LocationLaw: 
        """
        Return the elementary Law of rank <Index> <Index> have to be in [1, NbLaw()]
        """
    def NbHoles(self,Tol : float=1e-07) -> int: 
        """
        None
        """
    def NbLaw(self) -> int: 
        """
        Return the number of elementary Law
        """
    def Parameter(self,Abscissa : float) -> Tuple[int, float]: 
        """
        Find the index Law and the parmaeter, for a given Curnilinear abscissa
        """
    def PerformVertex(self,Index : int,InputVertex : OCP.TopoDS.TopoDS_Vertex,TolMin : float,OutputVertex : OCP.TopoDS.TopoDS_Vertex,Location : int=0) -> None: 
        """
        Compute <OutputVertex> like a transformation of <InputVertex> the transformation is given by evaluation of the location law in the vertex of rank <Index>. <Location> is used to manage discontinuities : - -1 : The law before the vertex is used. - 1 : The law after the vertex is used. - 0 : Average of the both laws is used.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformInCompatibleLaw(self,AngularTolerance : float) -> None: 
        """
        Apply a linear transformation on each law, to reduce the dicontinuities of law at one rotation.
        """
    def TransformInG0Law(self) -> None: 
        """
        Apply a linear transformation on each law, to have continuity of the global law beetween the edges.
        """
    def Vertex(self,Index : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Return the vertex of rank <Index> in the path <Index> have to be in [0, NbLaw()]
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        return the path
        """
    def __init__(self,Path : OCP.TopoDS.TopoDS_Wire,Law : OCP.GeomFill.GeomFill_LocationGuide) -> None: ...
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
class BRepFill_MultiLine(OCP.AppCont.AppCont_Function):
    """
    Class used to compute the 3d curve and the two 2d curves resulting from the intersection of a surface of linear extrusion( Bissec, Dz) and the 2 faces. This 3 curves will have the same parametrization as the Bissectrice. This class is to be send to an approximation routine.
    """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity betwwen the two faces seShape from GeomAbsparated by myBis.
        """
    def Curves(self,Curve : OCP.Geom.Geom_Curve,PCurve1 : OCP.Geom2d.Geom2d_Curve,PCurve2 : OCP.Geom2d.Geom2d_Curve) -> Any: 
        """
        raises if IsParticularCase is <False>.
        """
    def D1(self,theU : float,theVec2d : OCP.TColgp.TColgp_Array1OfVec2d,theVec : OCP.TColgp.TColgp_Array1OfVec) -> bool: 
        """
        Returns the derivative at parameter <theU>.
        """
    def FirstParameter(self) -> float: 
        """
        returns the first parameter of the Bissectrice.
        """
    def GetNbOf2dPoints(self) -> int: 
        """
        Get number of 2d points returned by "Value" and "D1" functions.
        """
    def GetNbOf3dPoints(self) -> int: 
        """
        Get number of 3d points returned by "Value" and "D1" functions.
        """
    def GetNumberOfPoints(self) -> Tuple[int, int]: 
        """
        Get number of 3d and 2d points returned by "Value" and "D1" functions.
        """
    def IsParticularCase(self) -> bool: 
        """
        Search if the Projection of the Bissectrice on the faces needs an approximation or not. Returns true if the approximation is not needed.
        """
    def LastParameter(self) -> float: 
        """
        returns the last parameter of the Bissectrice.
        """
    @overload
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Returns the current point on the 3d curve

        Returns the point at parameter <theU>.
        """
    @overload
    def Value(self,theU : float,thePnt2d : OCP.TColgp.TColgp_Array1OfPnt2d,thePnt : OCP.TColgp.TColgp_Array1OfPnt) -> bool: ...
    def Value3dOnF1OnF2(self,U : float,P3d : OCP.gp.gp_Pnt,PF1 : OCP.gp.gp_Pnt2d,PF2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    def ValueOnF1(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        returns the current point on the PCurve of the first face
        """
    def ValueOnF2(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        returns the current point on the PCurve of the first face
        """
    @overload
    def __init__(self,Face1 : OCP.TopoDS.TopoDS_Face,Face2 : OCP.TopoDS.TopoDS_Face,Edge1 : OCP.TopoDS.TopoDS_Edge,Edge2 : OCP.TopoDS.TopoDS_Edge,Inv1 : bool,Inv2 : bool,Bissec : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFill_SectionLaw(OCP.Standard.Standard_Transient):
    """
    Build Section Law, with an Vertex, or an WireBuild Section Law, with an Vertex, or an WireBuild Section Law, with an Vertex, or an Wire
    """
    def ConcatenedLaw(self) -> OCP.GeomFill.GeomFill_SectionLaw: 
        """
        None
        """
    def Continuity(self,Index : int,TolAngular : float) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def CurrentEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def D0(self,U : float,S : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def IndexOfEdge(self,anEdge : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def Init(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        None
        """
    def IsConstant(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
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
    def IsUClosed(self) -> bool: 
        """
        None
        """
    def IsVClosed(self) -> bool: 
        """
        None
        """
    def IsVertex(self) -> bool: 
        """
        Say if the input shape is a vertex.
        """
    def Law(self,Index : int) -> OCP.GeomFill.GeomFill_SectionLaw: 
        """
        None
        """
    def NbLaw(self) -> int: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vertex(self,Index : int,Param : float) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def VertexTol(self,Index : int,Param : float) -> float: 
        """
        None
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
class BRepFill_OffsetAncestors():
    """
    this class is used to find the generating shapes of an OffsetWire.
    """
    def Ancestor(self,S1 : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Shape: 
        """
        may return a Null Shape if S1 is not a subShape of <Paral>; if Perform is not done.
        """
    def HasAncestor(self,S1 : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Perform(self,Paral : BRepFill_OffsetWire) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Paral : BRepFill_OffsetWire) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFill_OffsetWire():
    """
    Constructs a Offset Wire to a spine (wire or face). Offset direction will be to outer region in case of positive offset value and to inner region in case of negative offset value. Inner/Outer region for open wire is defined by the following rule: when we go along the wire (taking into account of edges orientation) then outer region will be on the right side, inner region will be on the left side. In case of closed wire, inner region will always be inside the wire (at that, edges orientation is not taken into account). The Wire or the Face must be planar and oriented correctly.
    """
    def GeneratedShapes(self,SpineShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes created from a subshape <SpineShape> of the spine. Returns the last computed Offset.
        """
    def Init(self,Spine : OCP.TopoDS.TopoDS_Face,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,IsOpenResult : bool=False) -> None: 
        """
        Initialize the evaluation of Offseting.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def JoinType(self) -> OCP.GeomAbs.GeomAbs_JoinType: 
        """
        None
        """
    def Perform(self,Offset : float,Alt : float=0.0) -> None: 
        """
        Performs an OffsetWire at an altitude <Alt> from the face ( According to the orientation of the face)
        """
    def PerformWithBiLo(self,WSP : OCP.TopoDS.TopoDS_Face,Offset : float,Locus : OCP.BRepMAT2d.BRepMAT2d_BisectingLocus,Link : OCP.BRepMAT2d.BRepMAT2d_LinkTopoBilo,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,Alt : float=0.0) -> None: 
        """
        Performs an OffsetWire
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns the generated shape.
        """
    def Spine(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Face,Join : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,IsOpenResult : bool=False) -> None: ...
    pass
class BRepFill_Pipe():
    """
    Create a shape by sweeping a shape (the profile) along a wire (the spine).
    """
    def Edge(self,ESpine : OCP.TopoDS.TopoDS_Edge,VProfile : OCP.TopoDS.TopoDS_Vertex) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the edge created from an edge of the spine and a vertex of the profile. if the edge or the vertex are not in the spine or the profile.
        """
    def ErrorOnSurface(self) -> float: 
        """
        None
        """
    def Face(self,ESpine : OCP.TopoDS.TopoDS_Edge,EProfile : OCP.TopoDS.TopoDS_Edge) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the face created from an edge of the spine and an edge of the profile. if the edges are not in the spine or the profile
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Perform(self,Spine : OCP.TopoDS.TopoDS_Wire,Profile : OCP.TopoDS.TopoDS_Shape,GeneratePartCase : bool=False) -> None: 
        """
        None
        """
    def PipeLine(self,Point : OCP.gp.gp_Pnt) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Create a Wire by sweeping the Point along the <spine> if the <Spine> is undefined
        """
    def Profile(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Section(self,VSpine : OCP.TopoDS.TopoDS_Vertex) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape created from the profile at the position of the vertex VSpine. if the vertex is not in the Spine
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Spine(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Wire,Profile : OCP.TopoDS.TopoDS_Shape,aMode : OCP.GeomFill.GeomFill_Trihedron=GeomFill_Trihedron.GeomFill_IsCorrectedFrenet,ForceApproxC1 : bool=False,GeneratePartCase : bool=False) -> None: ...
    pass
class BRepFill_PipeShell(OCP.Standard.Standard_Transient):
    """
    Computes a topological shell using some wires (spines and profiles) and diplacement option Perform general sweeping constructionComputes a topological shell using some wires (spines and profiles) and diplacement option Perform general sweeping constructionComputes a topological shell using some wires (spines and profiles) and diplacement option Perform general sweeping construction
    """
    @overload
    def Add(self,Profile : OCP.TopoDS.TopoDS_Shape,Location : OCP.TopoDS.TopoDS_Vertex,WithContact : bool=False,WithCorrection : bool=False) -> None: 
        """
        Set an section. The corespondance with the spine, will be automaticaly performed.

        Set an section. The corespondance with the spine, is given by <Location>
        """
    @overload
    def Add(self,Profile : OCP.TopoDS.TopoDS_Shape,WithContact : bool=False,WithCorrection : bool=False) -> None: ...
    def Build(self) -> bool: 
        """
        Builds the resulting shape (redefined from MakeShape).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeleteProfile(self,Profile : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Delete an section.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ErrorOnSurface(self) -> float: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the bottom of the sweep.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStatus(self) -> OCP.GeomFill.GeomFill_PipeError: 
        """
        Get a status, when Simulate or Build failed.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
    def IsReady(self) -> bool: 
        """
        Say if <me> is ready to build the shape return False if <me> do not have section definition
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the top of the sweep.
        """
    def MakeSolid(self) -> bool: 
        """
        Transform the sweeping Shell in Solid. If the section are not closed returns False
        """
    def Profiles(self,theProfiles : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Returns the list of original profiles
        """
    @overload
    def Set(self,Axe : OCP.gp.gp_Ax2) -> None: 
        """
        Set an Frenet or an CorrectedFrenet trihedron to perform the sweeping

        Set an fixed trihedron to perform the sweeping all sections will be parallel.

        Set an fixed BiNormal direction to perform the sweeping

        Set support to the spine to define the BiNormal at the spine, like the normal the surfaces. Warning: To be effective, Each edge of the <spine> must have an representaion on one face of<SpineSupport>

        Set an auxiliary spine to define the Normal For each Point of the Spine P, an Point Q is evalued on <AuxiliarySpine> If <CurvilinearEquivalence> Q split <AuxiliarySpine> with the same length ratio than P split <Spline>. Else the plan define by P and the tangent to the <Spine> intersect <AuxiliarySpine> in Q. If <KeepContact> equals BRepFill_NoContact: The Normal is defined by the vector PQ. If <KeepContact> equals BRepFill_Contact: The Normal is defined to achieve that the sweeped section is in contact to the auxiliarySpine. The width of section is constant all along the path. In other words, the auxiliary spine lies on the swept surface, but not necessarily is a boundary of this surface. However, the auxiliary spine has to be close enough to the main spine to provide intersection with any section all along the path. If <KeepContact> equals BRepFill_ContactOnBorder: The auxiliary spine becomes a boundary of the swept surface and the width of section varies along the path.
        """
    @overload
    def Set(self,BiNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def Set(self,AuxiliarySpine : OCP.TopoDS.TopoDS_Wire,CurvilinearEquivalence : bool=True,KeepContact : BRepFill_TypeOfContact=BRepFill_TypeOfContact.BRepFill_NoContact) -> None: ...
    @overload
    def Set(self,Frenet : bool=False) -> None: ...
    @overload
    def Set(self,SpineSupport : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def SetDiscrete(self) -> None: 
        """
        Set a Discrete trihedron to perform the sweeping
        """
    def SetForceApproxC1(self,ForceApproxC1 : bool) -> None: 
        """
        Set the flag that indicates attempt to approximate a C1-continuous surface if a swept surface proved to be C0. Give section to sweep. Possibilities are : - Give one or sevral profile - Give one profile and an homotetic law. - Automatic compute of correspondance beetween profile, and section on the sweeped shape - correspondance beetween profile, and section on the sweeped shape defined by a vertex of the spine
        """
    @overload
    def SetLaw(self,Profile : OCP.TopoDS.TopoDS_Shape,L : OCP.Law.Law_Function,WithContact : bool=False,WithCorrection : bool=False) -> None: 
        """
        Set an section and an homotetic law. The homotetie's centers is given by point on the <Spine>.

        Set an section and an homotetic law. The homotetie center is given by point on the <Spine>
        """
    @overload
    def SetLaw(self,Profile : OCP.TopoDS.TopoDS_Shape,L : OCP.Law.Law_Function,Location : OCP.TopoDS.TopoDS_Vertex,WithContact : bool=False,WithCorrection : bool=False) -> None: ...
    def SetMaxDegree(self,NewMaxDegree : int) -> None: 
        """
        Define the maximum V degree of resulting surface
        """
    def SetMaxSegments(self,NewMaxSegments : int) -> None: 
        """
        Define the maximum number of spans in V-direction on resulting surface
        """
    def SetTolerance(self,Tol3d : float=0.0001,BoundTol : float=0.0001,TolAngular : float=0.01) -> None: 
        """
        None
        """
    def SetTransition(self,Mode : BRepFill_TransitionStyle=BRepFill_TransitionStyle.BRepFill_Modified,Angmin : float=0.01,Angmax : float=6.0) -> None: 
        """
        Set the Transition Mode to manage discontinuities on the sweep.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result Shape.
        """
    def Simulate(self,NumberOfSection : int,Sections : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Perform simulation of the sweep : Somes Section are returned.
        """
    def Spine(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Returns the spine
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Spine : OCP.TopoDS.TopoDS_Wire) -> None: ...
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
class BRepFill_Section():
    """
    To store section definition
    """
    def IsLaw(self) -> bool: 
        """
        None

        None
        """
    def IsPunctual(self) -> bool: 
        """
        None

        None
        """
    def ModifiedShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def OriginalShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None

        None
        """
    def Set(self,IsLaw : bool) -> None: 
        """
        None
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None

        None
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        None

        None
        """
    def WithContact(self) -> bool: 
        """
        None

        None
        """
    def WithCorrection(self) -> bool: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Profile : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Vertex,WithContact : bool,WithCorrection : bool) -> None: ...
    pass
class BRepFill_NSections(BRepFill_SectionLaw, OCP.Standard.Standard_Transient):
    """
    Build Section Law, with N SectionsBuild Section Law, with N SectionsBuild Section Law, with N Sections
    """
    def ConcatenedLaw(self) -> OCP.GeomFill.GeomFill_SectionLaw: 
        """
        Give the law build on a concatened section
        """
    def Continuity(self,Index : int,TolAngular : float) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def CurrentEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def D0(self,Param : float,S : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def IndexOfEdge(self,anEdge : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def Init(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        None
        """
    def IsConstant(self) -> bool: 
        """
        Say if the Law is Constant.
        """
    def IsDone(self) -> bool: 
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
    def IsUClosed(self) -> bool: 
        """
        None
        """
    def IsVClosed(self) -> bool: 
        """
        None
        """
    def IsVertex(self) -> bool: 
        """
        Say if the input shape is a vertex.
        """
    def Law(self,Index : int) -> OCP.GeomFill.GeomFill_SectionLaw: 
        """
        None
        """
    def NbLaw(self) -> int: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vertex(self,Index : int,Param : float) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def VertexTol(self,Index : int,Param : float) -> float: 
        """
        None
        """
    @overload
    def __init__(self,S : OCP.TopTools.TopTools_SequenceOfShape,Build : bool=True) -> None: ...
    @overload
    def __init__(self,S : OCP.TopTools.TopTools_SequenceOfShape,Trsfs : OCP.GeomFill.GeomFill_SequenceOfTrsf,P : OCP.TColStd.TColStd_SequenceOfReal,VF : float,VL : float,Build : bool=True) -> None: ...
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
class BRepFill_SectionPlacement():
    """
    Place a shape in a local axis coordinate
    """
    def AbscissaOnPath(self) -> float: 
        """
        None
        """
    def Transformation(self) -> OCP.gp.gp_Trsf: 
        """
        None
        """
    @overload
    def __init__(self,Law : BRepFill_LocationLaw,Section : OCP.TopoDS.TopoDS_Shape,WithContact : bool=False,WithCorrection : bool=False) -> None: ...
    @overload
    def __init__(self,Law : BRepFill_LocationLaw,Section : OCP.TopoDS.TopoDS_Shape,Vertex : OCP.TopoDS.TopoDS_Shape,WithContact : bool=False,WithCorrection : bool=False) -> None: ...
    pass
class BRepFill_SequenceOfEdgeFaceAndOrder(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BRepFill_EdgeFaceAndOrder) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : BRepFill_SequenceOfEdgeFaceAndOrder) -> None: ...
    def Assign(self,theOther : BRepFill_SequenceOfEdgeFaceAndOrder) -> BRepFill_SequenceOfEdgeFaceAndOrder: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> BRepFill_EdgeFaceAndOrder: 
        """
        First item access
        """
    def ChangeLast(self) -> BRepFill_EdgeFaceAndOrder: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> BRepFill_EdgeFaceAndOrder: 
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
    def First(self) -> BRepFill_EdgeFaceAndOrder: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : BRepFill_SequenceOfEdgeFaceAndOrder) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : BRepFill_EdgeFaceAndOrder) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : BRepFill_EdgeFaceAndOrder) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : BRepFill_SequenceOfEdgeFaceAndOrder) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BRepFill_EdgeFaceAndOrder: 
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
    def Prepend(self,theSeq : BRepFill_SequenceOfEdgeFaceAndOrder) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : BRepFill_EdgeFaceAndOrder) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : BRepFill_EdgeFaceAndOrder) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : BRepFill_SequenceOfEdgeFaceAndOrder) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BRepFill_EdgeFaceAndOrder: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : BRepFill_SequenceOfEdgeFaceAndOrder) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class BRepFill_SequenceOfFaceAndOrder(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BRepFill_FaceAndOrder) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : BRepFill_SequenceOfFaceAndOrder) -> None: ...
    def Assign(self,theOther : BRepFill_SequenceOfFaceAndOrder) -> BRepFill_SequenceOfFaceAndOrder: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> BRepFill_FaceAndOrder: 
        """
        First item access
        """
    def ChangeLast(self) -> BRepFill_FaceAndOrder: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> BRepFill_FaceAndOrder: 
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
    def First(self) -> BRepFill_FaceAndOrder: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : BRepFill_FaceAndOrder) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : BRepFill_SequenceOfFaceAndOrder) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : BRepFill_SequenceOfFaceAndOrder) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : BRepFill_FaceAndOrder) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BRepFill_FaceAndOrder: 
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
    def Prepend(self,theItem : BRepFill_FaceAndOrder) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : BRepFill_SequenceOfFaceAndOrder) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : BRepFill_FaceAndOrder) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : BRepFill_SequenceOfFaceAndOrder) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BRepFill_FaceAndOrder: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : BRepFill_SequenceOfFaceAndOrder) -> None: ...
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
class BRepFill_SequenceOfSection(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BRepFill_Section) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : BRepFill_SequenceOfSection) -> None: ...
    def Assign(self,theOther : BRepFill_SequenceOfSection) -> BRepFill_SequenceOfSection: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> BRepFill_Section: 
        """
        First item access
        """
    def ChangeLast(self) -> BRepFill_Section: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> BRepFill_Section: 
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
    def First(self) -> BRepFill_Section: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : BRepFill_Section) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : BRepFill_SequenceOfSection) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : BRepFill_Section) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : BRepFill_SequenceOfSection) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BRepFill_Section: 
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
    def Prepend(self,theSeq : BRepFill_SequenceOfSection) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : BRepFill_Section) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : BRepFill_Section) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : BRepFill_SequenceOfSection) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BRepFill_Section: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : BRepFill_SequenceOfSection) -> None: ...
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
class BRepFill_ShapeLaw(BRepFill_SectionLaw, OCP.Standard.Standard_Transient):
    """
    Build Section Law, with an Vertex, or an WireBuild Section Law, with an Vertex, or an WireBuild Section Law, with an Vertex, or an Wire
    """
    def ConcatenedLaw(self) -> OCP.GeomFill.GeomFill_SectionLaw: 
        """
        Give the law build on a concaneted section
        """
    def Continuity(self,Index : int,TolAngular : float) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def CurrentEdge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def D0(self,Param : float,S : OCP.TopoDS.TopoDS_Shape) -> None: 
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
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self,Index : int) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

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
    def IndexOfEdge(self,anEdge : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None
        """
    def Init(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        None
        """
    def IsConstant(self) -> bool: 
        """
        Say if the Law is Constant.
        """
    def IsDone(self) -> bool: 
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
    def IsUClosed(self) -> bool: 
        """
        None
        """
    def IsVClosed(self) -> bool: 
        """
        None
        """
    def IsVertex(self) -> bool: 
        """
        Say if the input shape is a vertex.
        """
    def Law(self,Index : int) -> OCP.GeomFill.GeomFill_SectionLaw: 
        """
        None
        """
    def NbLaw(self) -> int: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Vertex(self,Index : int,Param : float) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def VertexTol(self,Index : int,Param : float) -> float: 
        """
        None
        """
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,Build : bool=True) -> None: ...
    @overload
    def __init__(self,V : OCP.TopoDS.TopoDS_Vertex,Build : bool=True) -> None: ...
    @overload
    def __init__(self,W : OCP.TopoDS.TopoDS_Wire,L : OCP.Law.Law_Function,Build : bool=True) -> None: ...
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
class BRepFill_Sweep():
    """
    Topological Sweep Algorithm Computes an Sweep shell using a generating wire, an SectionLaw and an LocationLaw.
    """
    def Build(self,ReversedEdges : OCP.TopTools.TopTools_MapOfShape,Tapes : Any,Rails : Any,Transition : BRepFill_TransitionStyle=BRepFill_TransitionStyle.BRepFill_Modified,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C2,Approx : OCP.GeomFill.GeomFill_ApproxStyle=GeomFill_ApproxStyle.GeomFill_Location,Degmax : int=11,Segmax : int=30) -> None: 
        """
        Build the Sweep Surface Transition define Transition strategy Approx define Approximation Strategy - GeomFill_Section : The composed Function Location X Section is directly approximed. - GeomFill_Location : The location law is approximed, and the SweepSurface is bulid algebric composition of approximed location law and section law This option is Ok, if Section.Surface() methode is effective. Continuity : The continuity in v waiting on the surface Degmax : The maximum degree in v requiered on the surface Segmax : The maximum number of span in v requiered on the surface.
        """
    def ErrorOnSurface(self) -> float: 
        """
        Get the Approximation error.
        """
    def InterFaces(self) -> OCP.TopTools.TopTools_HArray2OfShape: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        Say if the Shape is Build.
        """
    def Sections(self) -> OCP.TopTools.TopTools_HArray2OfShape: 
        """
        None
        """
    def SetAngularControl(self,AngleMin : float=0.01,AngleMax : float=6.0) -> None: 
        """
        Tolerance To controle Corner management.
        """
    def SetBounds(self,FirstShape : OCP.TopoDS.TopoDS_Wire,LastShape : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        None
        """
    def SetForceApproxC1(self,ForceApproxC1 : bool) -> None: 
        """
        Set the flag that indicates attempt to approximate a C1-continuous surface if a swept surface proved to be C0.
        """
    def SetTolerance(self,Tol3d : float,BoundTol : float=1.0,Tol2d : float=1e-05,TolAngular : float=0.01) -> None: 
        """
        Set Approximation Tolerance Tol3d : Tolerance to surface approximation Tol2d : Tolerance used to perform curve approximation Normaly the 2d curve are approximated with a tolerance given by the resolution on support surfaces, but if this tolerance is too large Tol2d is used. TolAngular : Tolerance (in radian) to control the angle beetween tangents on the section law and tangent of iso-v on approximed surface
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns the Sweeping Shape
        """
    def SubShape(self) -> OCP.TopTools.TopTools_HArray2OfShape: 
        """
        None
        """
    def Tape(self,Index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns the Tape corresponding to Index-th edge of section
        """
    def __init__(self,Section : BRepFill_SectionLaw,Location : BRepFill_LocationLaw,WithKPart : bool) -> None: ...
    pass
class BRepFill_TransitionStyle():
    """
    None

    Members:

      BRepFill_Modified

      BRepFill_Right

      BRepFill_Round
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
    BRepFill_Modified: OCP.BRepFill.BRepFill_TransitionStyle # value = <BRepFill_TransitionStyle.BRepFill_Modified: 0>
    BRepFill_Right: OCP.BRepFill.BRepFill_TransitionStyle # value = <BRepFill_TransitionStyle.BRepFill_Right: 1>
    BRepFill_Round: OCP.BRepFill.BRepFill_TransitionStyle # value = <BRepFill_TransitionStyle.BRepFill_Round: 2>
    __entries: dict # value = {'BRepFill_Modified': (<BRepFill_TransitionStyle.BRepFill_Modified: 0>, None), 'BRepFill_Right': (<BRepFill_TransitionStyle.BRepFill_Right: 1>, None), 'BRepFill_Round': (<BRepFill_TransitionStyle.BRepFill_Round: 2>, None)}
    __members__: dict # value = {'BRepFill_Modified': <BRepFill_TransitionStyle.BRepFill_Modified: 0>, 'BRepFill_Right': <BRepFill_TransitionStyle.BRepFill_Right: 1>, 'BRepFill_Round': <BRepFill_TransitionStyle.BRepFill_Round: 2>}
    pass
class BRepFill_TrimEdgeTool():
    """
    Geometric Tool using to construct Offset Wires.
    """
    def AddOrConfuse(self,Start : bool,Edge1 : OCP.TopoDS.TopoDS_Edge,Edge2 : OCP.TopoDS.TopoDS_Edge,Params : OCP.TColgp.TColgp_SequenceOfPnt) -> None: 
        """
        None
        """
    def IntersectWith(self,Edge1 : OCP.TopoDS.TopoDS_Edge,Edge2 : OCP.TopoDS.TopoDS_Edge,InitShape1 : OCP.TopoDS.TopoDS_Shape,InitShape2 : OCP.TopoDS.TopoDS_Shape,End1 : OCP.TopoDS.TopoDS_Vertex,End2 : OCP.TopoDS.TopoDS_Vertex,theJoinType : OCP.GeomAbs.GeomAbs_JoinType,IsOpenResult : bool,Params : OCP.TColgp.TColgp_SequenceOfPnt) -> None: 
        """
        None
        """
    def IsInside(self,P : OCP.gp.gp_Pnt2d) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,Bisec : OCP.Bisector.Bisector_Bisec,S1 : OCP.Geom2d.Geom2d_Geometry,S2 : OCP.Geom2d.Geom2d_Geometry,Offset : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFill_TrimShellCorner():
    """
    Trims sets of faces in the corner to make proper parts of pipe
    """
    def AddBounds(self,Bounds : OCP.TopTools.TopTools_HArray2OfShape) -> None: 
        """
        None
        """
    def AddUEdges(self,theUEdges : OCP.TopTools.TopTools_HArray2OfShape) -> None: 
        """
        None
        """
    def AddVEdges(self,theVEdges : OCP.TopTools.TopTools_HArray2OfShape,theIndex : int) -> None: 
        """
        None
        """
    def HasSection(self) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape,theModified : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        None
        """
    def Perform(self) -> None: 
        """
        None
        """
    def __init__(self,theFaces : OCP.TopTools.TopTools_HArray2OfShape,theTransition : BRepFill_TransitionStyle,theAxeOfBisPlane : OCP.gp.gp_Ax2) -> None: ...
    pass
class BRepFill_TrimSurfaceTool():
    """
    Compute the Pcurves and the 3d curves resulting of the trimming of a face by an extruded surface.
    """
    def IntersectWith(self,EdgeOnF1 : OCP.TopoDS.TopoDS_Edge,EdgeOnF2 : OCP.TopoDS.TopoDS_Edge,Points : OCP.TColgp.TColgp_SequenceOfPnt) -> None: 
        """
        Intersect <Bis> with the projection of the edges <EdgeOnFi> and returns the intersecting parameters on Bis and on the edges P.X() : Parameter on Bis P.Y() : Parameter on EdgeOnF1 P.Z() : Parameter on EdgeOnF2 raises if <Edge> is not a edge of Face1 or Face2.
        """
    def IsOnFace(self,Point : OCP.gp.gp_Pnt2d) -> bool: 
        """
        returns True if the Line (P, DZ) intersect the Faces
        """
    def ProjOn(self,Point : OCP.gp.gp_Pnt2d,Edge : OCP.TopoDS.TopoDS_Edge) -> float: 
        """
        returns the parameter of the point <Point> on the Edge <Edge>, assuming that the point is on the edge.
        """
    def Project(self,U1 : float,U2 : float,Curve : OCP.Geom.Geom_Curve,PCurve1 : OCP.Geom2d.Geom2d_Curve,PCurve2 : OCP.Geom2d.Geom2d_Curve,myCont : OCP.GeomAbs.GeomAbs_Shape) -> Any: 
        """
        None
        """
    def __init__(self,Bis : OCP.Geom2d.Geom2d_Curve,Face1 : OCP.TopoDS.TopoDS_Face,Face2 : OCP.TopoDS.TopoDS_Face,Edge1 : OCP.TopoDS.TopoDS_Edge,Edge2 : OCP.TopoDS.TopoDS_Edge,Inv1 : bool,Inv2 : bool) -> None: ...
    pass
class BRepFill_TypeOfContact():
    """
    A pair of bound shapes with the result.

    Members:

      BRepFill_NoContact

      BRepFill_Contact

      BRepFill_ContactOnBorder
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
    BRepFill_Contact: OCP.BRepFill.BRepFill_TypeOfContact # value = <BRepFill_TypeOfContact.BRepFill_Contact: 1>
    BRepFill_ContactOnBorder: OCP.BRepFill.BRepFill_TypeOfContact # value = <BRepFill_TypeOfContact.BRepFill_ContactOnBorder: 2>
    BRepFill_NoContact: OCP.BRepFill.BRepFill_TypeOfContact # value = <BRepFill_TypeOfContact.BRepFill_NoContact: 0>
    __entries: dict # value = {'BRepFill_NoContact': (<BRepFill_TypeOfContact.BRepFill_NoContact: 0>, None), 'BRepFill_Contact': (<BRepFill_TypeOfContact.BRepFill_Contact: 1>, None), 'BRepFill_ContactOnBorder': (<BRepFill_TypeOfContact.BRepFill_ContactOnBorder: 2>, None)}
    __members__: dict # value = {'BRepFill_NoContact': <BRepFill_TypeOfContact.BRepFill_NoContact: 0>, 'BRepFill_Contact': <BRepFill_TypeOfContact.BRepFill_Contact: 1>, 'BRepFill_ContactOnBorder': <BRepFill_TypeOfContact.BRepFill_ContactOnBorder: 2>}
    pass
BRepFill_Contact: OCP.BRepFill.BRepFill_TypeOfContact # value = <BRepFill_TypeOfContact.BRepFill_Contact: 1>
BRepFill_ContactOnBorder: OCP.BRepFill.BRepFill_TypeOfContact # value = <BRepFill_TypeOfContact.BRepFill_ContactOnBorder: 2>
BRepFill_Modified: OCP.BRepFill.BRepFill_TransitionStyle # value = <BRepFill_TransitionStyle.BRepFill_Modified: 0>
BRepFill_NoContact: OCP.BRepFill.BRepFill_TypeOfContact # value = <BRepFill_TypeOfContact.BRepFill_NoContact: 0>
BRepFill_Right: OCP.BRepFill.BRepFill_TransitionStyle # value = <BRepFill_TransitionStyle.BRepFill_Right: 1>
BRepFill_Round: OCP.BRepFill.BRepFill_TransitionStyle # value = <BRepFill_TransitionStyle.BRepFill_Round: 2>
