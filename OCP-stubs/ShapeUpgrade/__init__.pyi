import OCP.ShapeUpgrade
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.ShapeExtend
import OCP.Geom2d
import OCP.ShapeAnalysis
import OCP.Message
import OCP.TopoDS
import OCP.TColGeom2d
import OCP.TColStd
import OCP.GeomAbs
import OCP.TColGeom
import OCP.TopTools
import OCP.TopLoc
import OCP.Standard
import OCP.Geom
import OCP.ShapeBuild
import OCP.BRepTools
__all__  = [
"ShapeUpgrade",
"ShapeUpgrade_Tool",
"ShapeUpgrade_FaceDivide",
"ShapeUpgrade_SplitCurve",
"ShapeUpgrade_SplitCurve3d",
"ShapeUpgrade_SplitSurface",
"ShapeUpgrade_EdgeDivide",
"ShapeUpgrade_ClosedFaceDivide",
"ShapeUpgrade_FaceDivideArea",
"ShapeUpgrade_FixSmallCurves",
"ShapeUpgrade_FixSmallBezierCurves",
"ShapeUpgrade_RemoveInternalWires",
"ShapeUpgrade_RemoveLocations",
"ShapeUpgrade_ShapeDivide",
"ShapeUpgrade_ShapeConvertToBezier",
"ShapeUpgrade_ShapeDivideAngle",
"ShapeUpgrade_ShapeDivideArea",
"ShapeUpgrade_ShapeDivideClosed",
"ShapeUpgrade_ShapeDivideClosedEdges",
"ShapeUpgrade_ShapeDivideContinuity",
"ShapeUpgrade_ShellSewing",
"ShapeUpgrade_SplitCurve2d",
"ShapeUpgrade_ConvertCurve2dToBezier",
"ShapeUpgrade_SplitCurve2dContinuity",
"ShapeUpgrade_ConvertCurve3dToBezier",
"ShapeUpgrade_SplitCurve3dContinuity",
"ShapeUpgrade_ConvertSurfaceToBezierBasis",
"ShapeUpgrade_SplitSurfaceAngle",
"ShapeUpgrade_SplitSurfaceArea",
"ShapeUpgrade_SplitSurfaceContinuity",
"ShapeUpgrade_ClosedEdgeDivide",
"ShapeUpgrade_UnifySameDomain",
"ShapeUpgrade_WireDivide"
]
class ShapeUpgrade():
    """
    This package provides tools for splitting and converting shapes by some criteria. It provides modifications of the kind when one topological object can be converted or splitted to several ones. In particular this package contains high level API classes which perform: converting geometry of shapes up to given continuity, splitting revolutions by U to segments less than given value, converting to beziers, splitting closed faces.
    """
    @staticmethod
    @overload
    def C0BSplineToSequenceOfC1BSplineCurve_s(BS : OCP.Geom2d.Geom2d_BSplineCurve,seqBS : OCP.TColGeom2d.TColGeom2d_HSequenceOfBoundedCurve) -> bool: 
        """
        Unifies same domain faces and edges of specified shape

        Converts C0 B-Spline curve into sequence of C1 B-Spline curves. This method splits B-Spline at the knots with multiplicities equal to degree, i.e. unlike method GeomConvert::C0BSplineToArrayOfC1BSplineCurve this one does not use any tolerance and therefore does not change the geometry of B-Spline. Returns True if C0 B-Spline was successfully splitted, else returns False (if BS is C1 B-Spline).
        """
    @staticmethod
    @overload
    def C0BSplineToSequenceOfC1BSplineCurve_s(BS : OCP.Geom.Geom_BSplineCurve,seqBS : OCP.TColGeom.TColGeom_HSequenceOfBoundedCurve) -> bool: ...
    def __init__(self) -> None: ...
    pass
class ShapeUpgrade_Tool(OCP.Standard.Standard_Transient):
    """
    Tool is a root class for splitting classes Provides context for recording changes, basic precision value and limit (minimal and maximal) values for tolerancesTool is a root class for splitting classes Provides context for recording changes, basic precision value and limit (minimal and maximal) values for tolerancesTool is a root class for splitting classes Provides context for recording changes, basic precision value and limit (minimal and maximal) values for tolerances
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
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
class ShapeUpgrade_FaceDivide(ShapeUpgrade_Tool, OCP.Standard.Standard_Transient):
    """
    Divides a Face (both edges in the wires, by splitting curves and pcurves, and the face itself, by splitting supporting surface) according to splitting criteria. * The domain of the face to divide is defined by the PCurves of the wires on the Face.Divides a Face (both edges in the wires, by splitting curves and pcurves, and the face itself, by splitting supporting surface) according to splitting criteria. * The domain of the face to divide is defined by the PCurves of the wires on the Face.Divides a Face (both edges in the wires, by splitting curves and pcurves, and the face itself, by splitting supporting surface) according to splitting criteria. * The domain of the face to divide is defined by the PCurves of the wires on the Face.
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def GetSplitSurfaceTool(self) -> ShapeUpgrade_SplitSurface: 
        """
        Returns the tool for splitting surfaces. This tool must be already initialized.
        """
    def GetWireDivideTool(self) -> ShapeUpgrade_WireDivide: 
        """
        Returns the tool for dividing edges on Face. This tool must be already initialized.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Initialize by a Face.
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def Perform(self) -> bool: 
        """
        Performs splitting and computes the resulting shell The context is used to keep track of former splittings in order to keep sharings. It is updated according to modifications made.
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shell, or Face, or Null shape if not done.
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
        """
    def SetSplitSurfaceTool(self,splitSurfaceTool : ShapeUpgrade_SplitSurface) -> None: 
        """
        Sets the tool for splitting surfaces.
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def SetWireDivideTool(self,wireDivideTool : ShapeUpgrade_WireDivide) -> None: 
        """
        Sets the tool for dividing edges on Face.
        """
    def SplitCurves(self) -> bool: 
        """
        Performs splitting of curves of all the edges in the shape and divides these edges.
        """
    def SplitSurface(self) -> bool: 
        """
        Performs splitting of surface and computes the shell from source face.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted DONE3: surface was modified without splitting FAIL1: some fails encountered during splitting wires FAIL2: face cannot be splitted
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
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
class ShapeUpgrade_SplitCurve(OCP.Standard.Standard_Transient):
    """
    Splits a curve with a criterion.Splits a curve with a criterion.Splits a curve with a criterion.
    """
    def Build(self,Segment : bool) -> None: 
        """
        If Segment is True, the result is composed with segments of the curve bounded by the SplitValues. If Segment is False, the result is composed with trimmed Curves all based on the same complete curve.
        """
    def Compute(self) -> None: 
        """
        Calculates points for correction/splitting of the curve
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
    def Init(self,First : float,Last : float) -> None: 
        """
        Initializes with curve first and last parameters.
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the curve. First defines splitting values by method Compute(), then calls method Build().
        """
    def SetSplitValues(self,SplitValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets the parameters where splitting has to be done.
        """
    def SplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting values including the First and Last parameters of the input curve Merges input split values and new ones into myGlobalKnots
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one segment DONE2 - splitting is required, but gives only one segment (initial) DONE3 - geometric form of the curve or parametrisation is modified
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
class ShapeUpgrade_SplitCurve3d(ShapeUpgrade_SplitCurve, OCP.Standard.Standard_Transient):
    """
    Splits a 3d curve with a criterion.Splits a 3d curve with a criterion.Splits a 3d curve with a criterion.
    """
    def Build(self,Segment : bool) -> None: 
        """
        If Segment is True, the result is composed with segments of the curve bounded by the SplitValues. If Segment is False, the result is composed with trimmed Curves all based on the same complete curve.
        """
    def Compute(self) -> None: 
        """
        Calculates points for correction/splitting of the curve
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
    def GetCurves(self) -> OCP.TColGeom.TColGeom_HArray1OfCurve: 
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
    def Init(self,C : OCP.Geom.Geom_Curve,First : float,Last : float) -> None: 
        """
        Initializes with curve with its first and last parameters.

        Initializes with curve with its parameters.
        """
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the curve. First defines splitting values by method Compute(), then calls method Build().
        """
    def SetSplitValues(self,SplitValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets the parameters where splitting has to be done.
        """
    def SplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting values including the First and Last parameters of the input curve Merges input split values and new ones into myGlobalKnots
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one segment DONE2 - splitting is required, but gives only one segment (initial) DONE3 - geometric form of the curve or parametrisation is modified
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
class ShapeUpgrade_SplitSurface(OCP.Standard.Standard_Transient):
    """
    Splits a Surface with a criterion.Splits a Surface with a criterion.Splits a Surface with a criterion.
    """
    def Build(self,Segment : bool) -> None: 
        """
        Performs splitting of the supporting surface. If resulting surface is B-Spline and Segment is True, the result is composed with segments of the surface bounded by the U and V SplitValues (method Geom_BSplineSurface::Segment is used). If Segment is False, the result is composed with Geom_RectangularTrimmedSurface all based on the same complete surface. Fields myNbResultingRow and myNbResultingCol must be set to specify the size of resulting grid of surfaces.
        """
    def Compute(self,Segment : bool=True) -> None: 
        """
        Calculates points for correction/splitting of the surface.
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
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface,UFirst : float,ULast : float,VFirst : float,VLast : float) -> None: 
        """
        Initializes with single supporting surface.

        Initializes with single supporting surface with bounding parameters.
        """
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the surface. First defines splitting values by method Compute(), then calls method Build().
        """
    def ResSurfaces(self) -> OCP.ShapeExtend.ShapeExtend_CompositeSurface: 
        """
        Returns obtained surfaces after splitting as CompositeSurface
        """
    def SetUSplitValues(self,UValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets U parameters where splitting has to be done
        """
    def SetVSplitValues(self,VValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets V parameters where splitting has to be done
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one patch DONE2 - splitting is required, but gives only single patch (initial) DONE3 - geometric form of the surface or parametrisation is modified
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def USplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the U splitting values including the First and Last parameters of the input surface
        """
    def VSplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting V values including the First and Last parameters of the input surface
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
class ShapeUpgrade_EdgeDivide(ShapeUpgrade_Tool, OCP.Standard.Standard_Transient):
    def Clear(self) -> None: 
        """
        None
        """
    def Compute(self,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def GetSplitCurve2dTool(self) -> ShapeUpgrade_SplitCurve2d: 
        """
        Returns the tool for splitting pcurves.
        """
    def GetSplitCurve3dTool(self) -> ShapeUpgrade_SplitCurve3d: 
        """
        Returns the tool for splitting 3D curves.
        """
    def HasCurve2d(self) -> bool: 
        """
        None

        None
        """
    def HasCurve3d(self) -> bool: 
        """
        None

        None
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
    def Knots2d(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        None

        None
        """
    def Knots3d(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        None

        None
        """
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets supporting surface by face

        Sets supporting surface by face
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
        """
    def SetSplitCurve2dTool(self,splitCurve2dTool : ShapeUpgrade_SplitCurve2d) -> None: 
        """
        Sets the tool for splitting pcurves.
        """
    def SetSplitCurve3dTool(self,splitCurve3dTool : ShapeUpgrade_SplitCurve3d) -> None: 
        """
        Sets the tool for splitting 3D curves.
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
class ShapeUpgrade_ClosedFaceDivide(ShapeUpgrade_FaceDivide, ShapeUpgrade_Tool, OCP.Standard.Standard_Transient):
    """
    Divides a Face with one or more seam edge to avoid closed faces. Splitting is performed by U and V direction. The number of resulting faces can be defined by user.Divides a Face with one or more seam edge to avoid closed faces. Splitting is performed by U and V direction. The number of resulting faces can be defined by user.Divides a Face with one or more seam edge to avoid closed faces. Splitting is performed by U and V direction. The number of resulting faces can be defined by user.
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def GetNbSplitPoints(self) -> int: 
        """
        Returns the number of splitting points
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSplitSurfaceTool(self) -> ShapeUpgrade_SplitSurface: 
        """
        Returns the tool for splitting surfaces. This tool must be already initialized.
        """
    def GetWireDivideTool(self) -> ShapeUpgrade_WireDivide: 
        """
        Returns the tool for dividing edges on Face. This tool must be already initialized.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Initialize by a Face.
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def Perform(self) -> bool: 
        """
        Performs splitting and computes the resulting shell The context is used to keep track of former splittings in order to keep sharings. It is updated according to modifications made.
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shell, or Face, or Null shape if not done.
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetNbSplitPoints(self,num : int) -> None: 
        """
        Sets the number of cutting lines by which closed face will be splitted. The resulting faces will be num+1.
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
        """
    def SetSplitSurfaceTool(self,splitSurfaceTool : ShapeUpgrade_SplitSurface) -> None: 
        """
        Sets the tool for splitting surfaces.
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def SetWireDivideTool(self,wireDivideTool : ShapeUpgrade_WireDivide) -> None: 
        """
        Sets the tool for dividing edges on Face.
        """
    def SplitCurves(self) -> bool: 
        """
        Performs splitting of curves of all the edges in the shape and divides these edges.
        """
    def SplitSurface(self) -> bool: 
        """
        Performs splitting of surface and computes the shell from source face.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted DONE3: surface was modified without splitting FAIL1: some fails encountered during splitting wires FAIL2: face cannot be splitted
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
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
class ShapeUpgrade_FaceDivideArea(ShapeUpgrade_FaceDivide, ShapeUpgrade_Tool, OCP.Standard.Standard_Transient):
    """
    Divides face by max area criterium.Divides face by max area criterium.Divides face by max area criterium.
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def GetSplitSurfaceTool(self) -> ShapeUpgrade_SplitSurface: 
        """
        Returns the tool for splitting surfaces. This tool must be already initialized.
        """
    def GetWireDivideTool(self) -> ShapeUpgrade_WireDivide: 
        """
        Returns the tool for dividing edges on Face. This tool must be already initialized.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Initialize by a Face.
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def Perform(self) -> bool: 
        """
        Performs splitting and computes the resulting shell The context is used to keep track of former splittings
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shell, or Face, or Null shape if not done.
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
        """
    def SetSplitSurfaceTool(self,splitSurfaceTool : ShapeUpgrade_SplitSurface) -> None: 
        """
        Sets the tool for splitting surfaces.
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def SetWireDivideTool(self,wireDivideTool : ShapeUpgrade_WireDivide) -> None: 
        """
        Sets the tool for dividing edges on Face.
        """
    def SplitCurves(self) -> bool: 
        """
        Performs splitting of curves of all the edges in the shape and divides these edges.
        """
    def SplitSurface(self) -> bool: 
        """
        Performs splitting of surface and computes the shell from source face.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted DONE3: surface was modified without splitting FAIL1: some fails encountered during splitting wires FAIL2: face cannot be splitted
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
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
    @property
    def MaxArea(self) -> float:
        """
        Set max area allowed for faces

        :type: float
        """
    @MaxArea.setter
    def MaxArea(self, arg1: float) -> None:
        """
        Set max area allowed for faces
        """
    pass
class ShapeUpgrade_FixSmallCurves(ShapeUpgrade_Tool, OCP.Standard.Standard_Transient):
    def Approx(self,Curve3d : OCP.Geom.Geom_Curve,Curve2d : OCP.Geom2d.Geom2d_Curve,Curve2dR : OCP.Geom2d.Geom2d_Curve,First : float,Last : float) -> bool: 
        """
        None
        """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def Init(self,theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face) -> None: 
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
        """
    def SetSplitCurve2dTool(self,splitCurve2dTool : ShapeUpgrade_SplitCurve2d) -> None: 
        """
        Sets the tool for splitting pcurves.
        """
    def SetSplitCurve3dTool(self,splitCurve3dTool : ShapeUpgrade_SplitCurve3d) -> None: 
        """
        Sets the tool for splitting 3D curves.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : DONE1: DONE2: FAIL1:
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
class ShapeUpgrade_FixSmallBezierCurves(ShapeUpgrade_FixSmallCurves, ShapeUpgrade_Tool, OCP.Standard.Standard_Transient):
    def Approx(self,Curve3d : OCP.Geom.Geom_Curve,Curve2d : OCP.Geom2d.Geom2d_Curve,Curve2dR : OCP.Geom2d.Geom2d_Curve,First : float,Last : float) -> bool: 
        """
        None
        """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def Init(self,theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face) -> None: 
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
        """
    def SetSplitCurve2dTool(self,splitCurve2dTool : ShapeUpgrade_SplitCurve2d) -> None: 
        """
        Sets the tool for splitting pcurves.
        """
    def SetSplitCurve3dTool(self,splitCurve3dTool : ShapeUpgrade_SplitCurve3d) -> None: 
        """
        Sets the tool for splitting 3D curves.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : DONE1: DONE2: FAIL1:
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
class ShapeUpgrade_RemoveInternalWires(ShapeUpgrade_Tool, OCP.Standard.Standard_Transient):
    """
    Removes all internal wires having area less than specified min areaRemoves all internal wires having area less than specified min areaRemoves all internal wires having area less than specified min area
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def GetResult(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Get result shape

        Get result shape
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize by a Shape.
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    @overload
    def Perform(self) -> bool: 
        """
        Removes all internal wires having area less than area specified as minimal allowed area

        If specified sequence of shape contains - 1.wires then these wires will be removed if they have area less than allowed min area. 2.faces than internal wires from these faces will be removed if they have area less than allowed min area.
        """
    @overload
    def Perform(self,theSeqShapes : OCP.TopTools.TopTools_SequenceOfShape) -> bool: ...
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def RemovedFaces(self) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        Returns sequence of removed faces.

        Returns sequence of removed faces.
        """
    def RemovedWires(self) -> OCP.TopTools.TopTools_SequenceOfShape: 
        """
        Returns sequence of removed faces.

        Returns sequence of removed faces.
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
        """
    def Status(self,theStatus : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries status of last call to Perform() : OK - nothing was done :DONE1 - internal wires were removed :DONE2 - small faces were removed. :FAIL1 - initial shape is not specified :FAIL2 - specified sub-shape is not belonged to inotial shape.

        Queries status of last call to Perform() : OK - nothing was done :DONE1 - internal wires were removed :DONE2 - small faces were removed. :FAIL1 - initial shape is not specified :FAIL2 - specified sub-shape is not belonged to inotial shape.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
    def MinArea(self) -> float:
        """
        Set min area allowed for holes( all holes having area less than mi area will be removed)

        :type: float
        """
    @MinArea.setter
    def MinArea(self, arg1: float) -> None:
        """
        Set min area allowed for holes( all holes having area less than mi area will be removed)
        """
    @property
    def RemoveFaceMode(self) -> bool:
        """
        Set mode which manage removing faces which have outer wires consisting only from edges belonginig to removed internal wires. By default it is equal to true.

        :type: bool
        """
    @RemoveFaceMode.setter
    def RemoveFaceMode(self, arg1: bool) -> None:
        """
        Set mode which manage removing faces which have outer wires consisting only from edges belonginig to removed internal wires. By default it is equal to true.
        """
    pass
class ShapeUpgrade_RemoveLocations(OCP.Standard.Standard_Transient):
    """
    Removes all locations sub-shapes of specified shapeRemoves all locations sub-shapes of specified shapeRemoves all locations sub-shapes of specified shape
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
    def GetResult(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns shape with removed locatins.

        Returns shape with removed locatins.
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
    def ModifiedShape(self,theInitShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns modified shape obtained from initial shape.

        Returns modified shape obtained from initial shape.
        """
    def Remove(self,theShape : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Removes all location correspodingly to RemoveLevel.
        """
    def RemoveLevel(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        sets level starting with that location will be removed.Value of level can be set to TopAbs_SHAPE,TopAbs_COMPOUND,TopAbs_SOLID,TopAbs_SHELL,TopAbs_FACE.By default TopAbs_SHAPE. In this case location will be removed for all shape types for exception of compound.

        sets level starting with that location will be removed.Value of level can be set to TopAbs_SHAPE,TopAbs_COMPOUND,TopAbs_SOLID,TopAbs_SHELL,TopAbs_FACE.By default TopAbs_SHAPE. In this case location will be removed for all shape types for exception of compound.
        """
    def SetRemoveLevel(self,theLevel : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        sets level starting with that location will be removed, by default TopAbs_SHAPE. In this case locations will be kept for specified shape and if specified shape is TopAbs_COMPOUND for sub-shapes of first level.

        sets level starting with that location will be removed, by default TopAbs_SHAPE. In this case locations will be kept for specified shape and if specified shape is TopAbs_COMPOUND for sub-shapes of first level.
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
class ShapeUpgrade_ShapeDivide():
    """
    Divides a all faces in shell with given criteria Shell.
    """
    def GetContext(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context with all the modifications made during last call(s) to Perform() recorded
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize by a Shape.
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def Perform(self,newContext : bool=True) -> bool: 
        """
        Performs splitting and computes the resulting shape If newContext is True (default), the internal context will be cleared at start, else previous substitutions will be acting.
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shape, or Null shape if not done.
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context with recorded modifications to be applied during next call(s) to Perform(shape,Standard_False)
        """
    def SetEdgeMode(self,aEdgeMode : int) -> None: 
        """
        Sets mode for splitting 3d curves from edges. 0 - only curve 3d from free edges. 1 - only curve 3d from shared edges. 2 - all curve 3d.
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,Prec : float) -> None: 
        """
        Defines the spatial precision used for splitting
        """
    def SetSplitFaceTool(self,splitFaceTool : ShapeUpgrade_FaceDivide) -> None: 
        """
        Sets the tool for splitting faces.
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted FAIL1: some errors occured
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class ShapeUpgrade_ShapeConvertToBezier(ShapeUpgrade_ShapeDivide):
    """
    API class for performing conversion of 3D, 2D curves to bezier curves and surfaces to bezier based surfaces ( bezier surface, surface of revolution based on bezier curve, offset surface based on any previous type).
    """
    def Get2dConversion(self) -> bool: 
        """
        Returns the 2D conversion mode.

        Returns the 2D conversion mode.
        """
    def Get3dCircleConversion(self) -> bool: 
        """
        Returns the Geom_Circle conversion mode.

        Returns the Geom_Circle conversion mode.
        """
    def Get3dConicConversion(self) -> bool: 
        """
        Returns the Geom_Conic conversion mode.

        Returns the Geom_Conic conversion mode.
        """
    def Get3dConversion(self) -> bool: 
        """
        Returns the 3D conversion mode.

        Returns the 3D conversion mode.
        """
    def Get3dLineConversion(self) -> bool: 
        """
        Returns the Geom_Line conversion mode.

        Returns the Geom_Line conversion mode.
        """
    def GetBSplineMode(self) -> bool: 
        """
        Returns the Geom_BSplineSurface conversion mode.

        Returns the Geom_BSplineSurface conversion mode.
        """
    def GetContext(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context with all the modifications made during last call(s) to Perform() recorded
        """
    def GetExtrusionMode(self) -> bool: 
        """
        Returns the Geom_SurfaceOfLinearExtrusion conversion mode.

        Returns the Geom_SurfaceOfLinearExtrusion conversion mode.
        """
    def GetPlaneMode(self) -> bool: 
        """
        Returns the Geom_Pline conversion mode.

        Returns the Geom_Pline conversion mode.
        """
    def GetRevolutionMode(self) -> bool: 
        """
        Returns the Geom_SurfaceOfRevolution conversion mode.

        Returns the Geom_SurfaceOfRevolution conversion mode.
        """
    def GetSurfaceConversion(self) -> bool: 
        """
        Returns the surface conversion mode.

        Returns the surface conversion mode.
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize by a Shape.
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def Perform(self,newContext : bool=True) -> bool: 
        """
        Performs converting and computes the resulting shape
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shape, or Null shape if not done.
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def Set2dConversion(self,mode : bool) -> None: 
        """
        Sets mode for conversion 2D curves to bezier.

        Sets mode for conversion 2D curves to bezier.
        """
    def Set3dCircleConversion(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_Circle to bezier.

        Sets mode for conversion Geom_Circle to bezier.
        """
    def Set3dConicConversion(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_Conic to bezier.

        Sets mode for conversion Geom_Conic to bezier.
        """
    def Set3dConversion(self,mode : bool) -> None: 
        """
        Sets mode for conversion 3d curves to bezier.

        Sets mode for conversion 3d curves to bezier.
        """
    def Set3dLineConversion(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_Line to bezier.

        Sets mode for conversion Geom_Line to bezier.
        """
    def SetBSplineMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_BSplineSurface to Bezier

        Sets mode for conversion Geom_BSplineSurface to Bezier
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context with recorded modifications to be applied during next call(s) to Perform(shape,Standard_False)
        """
    def SetEdgeMode(self,aEdgeMode : int) -> None: 
        """
        Sets mode for splitting 3d curves from edges. 0 - only curve 3d from free edges. 1 - only curve 3d from shared edges. 2 - all curve 3d.
        """
    def SetExtrusionMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_SurfaceOfLinearExtrusion to Bezier

        Sets mode for conversion Geom_SurfaceOfLinearExtrusion to Bezier
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPlaneMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_Plane to Bezier

        Sets mode for conversion Geom_Plane to Bezier
        """
    def SetPrecision(self,Prec : float) -> None: 
        """
        Defines the spatial precision used for splitting
        """
    def SetRevolutionMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_SurfaceOfRevolution to Bezier

        Sets mode for conversion Geom_SurfaceOfRevolution to Bezier
        """
    def SetSplitFaceTool(self,splitFaceTool : ShapeUpgrade_FaceDivide) -> None: 
        """
        Sets the tool for splitting faces.
        """
    def SetSurfaceConversion(self,mode : bool) -> None: 
        """
        Sets mode for conversion surfaces curves to bezier basis.

        Sets mode for conversion surfaces curves to bezier basis.
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted FAIL1: some errors occured
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class ShapeUpgrade_ShapeDivideAngle(ShapeUpgrade_ShapeDivide):
    """
    Splits all surfaces of revolution, cylindrical, toroidal, conical, spherical surfaces in the given shape so that each resulting segment covers not more than defined number of degrees (to segments less than 90).
    """
    def GetContext(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context with all the modifications made during last call(s) to Perform() recorded
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize by a Shape.
        """
    def InitTool(self,MaxAngle : float) -> None: 
        """
        Resets tool for splitting face with given angle
        """
    def MaxAngle(self) -> float: 
        """
        Returns maximal angle
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def Perform(self,newContext : bool=True) -> bool: 
        """
        Performs splitting and computes the resulting shape If newContext is True (default), the internal context will be cleared at start, else previous substitutions will be acting.
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shape, or Null shape if not done.
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context with recorded modifications to be applied during next call(s) to Perform(shape,Standard_False)
        """
    def SetEdgeMode(self,aEdgeMode : int) -> None: 
        """
        Sets mode for splitting 3d curves from edges. 0 - only curve 3d from free edges. 1 - only curve 3d from shared edges. 2 - all curve 3d.
        """
    def SetMaxAngle(self,MaxAngle : float) -> None: 
        """
        Set maximal angle (calls InitTool)
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,Prec : float) -> None: 
        """
        Defines the spatial precision used for splitting
        """
    def SetSplitFaceTool(self,splitFaceTool : ShapeUpgrade_FaceDivide) -> None: 
        """
        Sets the tool for splitting faces.
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted FAIL1: some errors occured
        """
    @overload
    def __init__(self,MaxAngle : float) -> None: ...
    @overload
    def __init__(self,MaxAngle : float,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class ShapeUpgrade_ShapeDivideArea(ShapeUpgrade_ShapeDivide):
    """
    Divides faces from sprcified shape by max area criterium.
    """
    def GetContext(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context with all the modifications made during last call(s) to Perform() recorded
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize by a Shape.
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def Perform(self,newContext : bool=True) -> bool: 
        """
        Performs splitting and computes the resulting shape If newContext is True (default), the internal context will be cleared at start, else previous substitutions will be acting.
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shape, or Null shape if not done.
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context with recorded modifications to be applied during next call(s) to Perform(shape,Standard_False)
        """
    def SetEdgeMode(self,aEdgeMode : int) -> None: 
        """
        Sets mode for splitting 3d curves from edges. 0 - only curve 3d from free edges. 1 - only curve 3d from shared edges. 2 - all curve 3d.
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPrecision(self,Prec : float) -> None: 
        """
        Defines the spatial precision used for splitting
        """
    def SetSplitFaceTool(self,splitFaceTool : ShapeUpgrade_FaceDivide) -> None: 
        """
        Sets the tool for splitting faces.
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted FAIL1: some errors occured
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @property
    def MaxArea(self) -> float:
        """
        Set max area allowed for faces

        :type: float
        """
    @MaxArea.setter
    def MaxArea(self, arg1: float) -> None:
        """
        Set max area allowed for faces
        """
    pass
class ShapeUpgrade_ShapeDivideClosed(ShapeUpgrade_ShapeDivide):
    """
    Divides all closed faces in the shape. Class ShapeUpgrade_ClosedFaceDivide is used as divide tool.
    """
    def GetContext(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context with all the modifications made during last call(s) to Perform() recorded
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize by a Shape.
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def Perform(self,newContext : bool=True) -> bool: 
        """
        Performs splitting and computes the resulting shape If newContext is True (default), the internal context will be cleared at start, else previous substitutions will be acting.
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shape, or Null shape if not done.
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context with recorded modifications to be applied during next call(s) to Perform(shape,Standard_False)
        """
    def SetEdgeMode(self,aEdgeMode : int) -> None: 
        """
        Sets mode for splitting 3d curves from edges. 0 - only curve 3d from free edges. 1 - only curve 3d from shared edges. 2 - all curve 3d.
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetNbSplitPoints(self,num : int) -> None: 
        """
        Sets the number of cuts applied to divide closed faces. The number of resulting faces will be num+1.
        """
    def SetPrecision(self,Prec : float) -> None: 
        """
        Defines the spatial precision used for splitting
        """
    def SetSplitFaceTool(self,splitFaceTool : ShapeUpgrade_FaceDivide) -> None: 
        """
        Sets the tool for splitting faces.
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted FAIL1: some errors occured
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class ShapeUpgrade_ShapeDivideClosedEdges(ShapeUpgrade_ShapeDivide):
    """
    None
    """
    def GetContext(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context with all the modifications made during last call(s) to Perform() recorded
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize by a Shape.
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def Perform(self,newContext : bool=True) -> bool: 
        """
        Performs splitting and computes the resulting shape If newContext is True (default), the internal context will be cleared at start, else previous substitutions will be acting.
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shape, or Null shape if not done.
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context with recorded modifications to be applied during next call(s) to Perform(shape,Standard_False)
        """
    def SetEdgeMode(self,aEdgeMode : int) -> None: 
        """
        Sets mode for splitting 3d curves from edges. 0 - only curve 3d from free edges. 1 - only curve 3d from shared edges. 2 - all curve 3d.
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetNbSplitPoints(self,num : int) -> None: 
        """
        Sets the number of cuts applied to divide closed edges. The number of resulting faces will be num+1.
        """
    def SetPrecision(self,Prec : float) -> None: 
        """
        Defines the spatial precision used for splitting
        """
    def SetSplitFaceTool(self,splitFaceTool : ShapeUpgrade_FaceDivide) -> None: 
        """
        Sets the tool for splitting faces.
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted FAIL1: some errors occured
        """
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class ShapeUpgrade_ShapeDivideContinuity(ShapeUpgrade_ShapeDivide):
    """
    API Tool for converting shapes with C0 geometry into C1 ones
    """
    def GetContext(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context with all the modifications made during last call(s) to Perform() recorded
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialize by a Shape.
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def Perform(self,newContext : bool=True) -> bool: 
        """
        Performs splitting and computes the resulting shape If newContext is True (default), the internal context will be cleared at start, else previous substitutions will be acting.
        """
    def Result(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting Shape, or Null shape if not done.
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetBoundaryCriterion(self,Criterion : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: 
        """
        Defines a criterion of continuity for the boundary (all the Wires)
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context with recorded modifications to be applied during next call(s) to Perform(shape,Standard_False)
        """
    def SetEdgeMode(self,aEdgeMode : int) -> None: 
        """
        Sets mode for splitting 3d curves from edges. 0 - only curve 3d from free edges. 1 - only curve 3d from shared edges. 2 - all curve 3d.
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPCurveCriterion(self,Criterion : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: 
        """
        Defines a criterion of continuity for the boundary (all the pcurves of Wires)
        """
    def SetPrecision(self,Prec : float) -> None: 
        """
        Defines the spatial precision used for splitting
        """
    def SetSplitFaceTool(self,splitFaceTool : ShapeUpgrade_FaceDivide) -> None: 
        """
        Sets the tool for splitting faces.
        """
    def SetSurfaceCriterion(self,Criterion : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1) -> None: 
        """
        Defines a criterion of continuity for the boundary (all the Wires)
        """
    def SetSurfaceSegmentMode(self,Segment : bool) -> None: 
        """
        Purpose sets mode for trimming (segment) surface by wire UV bounds.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        Sets tolerance.
        """
    def SetTolerance2d(self,Tol : float) -> None: 
        """
        Sets tolerance.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries the status of last call to Perform OK : no splitting was done (or no call to Perform) DONE1: some edges were splitted DONE2: surface was splitted FAIL1: some errors occured
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class ShapeUpgrade_ShellSewing():
    """
    This class provides a tool for applying sewing algorithm from BRepBuilderAPI: it takes a shape, calls sewing for each shell, and then replaces sewed shells with use of ShapeBuild_ReShape
    """
    def ApplySewing(self,shape : OCP.TopoDS.TopoDS_Shape,tol : float=0.0) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Builds a new shape from a former one, by calling Sewing from BRepBuilderAPI. Rebuilt solids are oriented to be "not infinite"
        """
    def __init__(self) -> None: ...
    pass
class ShapeUpgrade_SplitCurve2d(ShapeUpgrade_SplitCurve, OCP.Standard.Standard_Transient):
    """
    Splits a 2d curve with a criterion.Splits a 2d curve with a criterion.Splits a 2d curve with a criterion.
    """
    def Build(self,Segment : bool) -> None: 
        """
        If Segment is True, the result is composed with segments of the curve bounded by the SplitValues. If Segment is False, the result is composed with trimmed Curves all based on the same complete curve.
        """
    def Compute(self) -> None: 
        """
        Calculates points for correction/splitting of the curve
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
    def GetCurves(self) -> OCP.TColGeom2d.TColGeom2d_HArray1OfCurve: 
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
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,First : float,Last : float) -> None: 
        """
        Initializes with pcurve with its first and last parameters.

        Initializes with pcurve with its parameters.
        """
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the curve. First defines splitting values by method Compute(), then calls method Build().
        """
    def SetSplitValues(self,SplitValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets the parameters where splitting has to be done.
        """
    def SplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting values including the First and Last parameters of the input curve Merges input split values and new ones into myGlobalKnots
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one segment DONE2 - splitting is required, but gives only one segment (initial) DONE3 - geometric form of the curve or parametrisation is modified
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
class ShapeUpgrade_ConvertCurve2dToBezier(ShapeUpgrade_SplitCurve2d, ShapeUpgrade_SplitCurve, OCP.Standard.Standard_Transient):
    """
    converts/splits a 2d curve to a list of beziersconverts/splits a 2d curve to a list of beziersconverts/splits a 2d curve to a list of beziers
    """
    def Build(self,Segment : bool) -> None: 
        """
        Splits a list of beziers computed by Compute method according the split values and splitting parameters.
        """
    def Compute(self) -> None: 
        """
        Converts curve into a list of beziers, and stores the splitting parameters on original curve.
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
    def GetCurves(self) -> OCP.TColGeom2d.TColGeom2d_HArray1OfCurve: 
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
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,First : float,Last : float) -> None: 
        """
        Initializes with pcurve with its first and last parameters.

        Initializes with pcurve with its parameters.
        """
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the curve. First defines splitting values by method Compute(), then calls method Build().
        """
    def SetSplitValues(self,SplitValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets the parameters where splitting has to be done.
        """
    def SplitParams(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        Returns the list of splitted parameters in original curve parametrisation.
        """
    def SplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting values including the First and Last parameters of the input curve Merges input split values and new ones into myGlobalKnots
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one segment DONE2 - splitting is required, but gives only one segment (initial) DONE3 - geometric form of the curve or parametrisation is modified
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
class ShapeUpgrade_SplitCurve2dContinuity(ShapeUpgrade_SplitCurve2d, ShapeUpgrade_SplitCurve, OCP.Standard.Standard_Transient):
    """
    Corrects/splits a 2d curve with a continuity criterion. Tolerance is used to correct the curve at a knot that respects geometrically the criterion, in order to reduce the multiplicity of the knot.Corrects/splits a 2d curve with a continuity criterion. Tolerance is used to correct the curve at a knot that respects geometrically the criterion, in order to reduce the multiplicity of the knot.Corrects/splits a 2d curve with a continuity criterion. Tolerance is used to correct the curve at a knot that respects geometrically the criterion, in order to reduce the multiplicity of the knot.
    """
    def Build(self,Segment : bool) -> None: 
        """
        If Segment is True, the result is composed with segments of the curve bounded by the SplitValues. If Segment is False, the result is composed with trimmed Curves all based on the same complete curve.
        """
    def Compute(self) -> None: 
        """
        Calculates points for correction/splitting of the curve
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
    def GetCurves(self) -> OCP.TColGeom2d.TColGeom2d_HArray1OfCurve: 
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
    def Init(self,C : OCP.Geom2d.Geom2d_Curve,First : float,Last : float) -> None: 
        """
        Initializes with pcurve with its first and last parameters.

        Initializes with pcurve with its parameters.
        """
    @overload
    def Init(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the curve. First defines splitting values by method Compute(), then calls method Build().
        """
    def SetCriterion(self,Criterion : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Sets criterion for splitting.
        """
    def SetSplitValues(self,SplitValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets the parameters where splitting has to be done.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        Sets tolerance.
        """
    def SplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting values including the First and Last parameters of the input curve Merges input split values and new ones into myGlobalKnots
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one segment DONE2 - splitting is required, but gives only one segment (initial) DONE3 - geometric form of the curve or parametrisation is modified
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
class ShapeUpgrade_ConvertCurve3dToBezier(ShapeUpgrade_SplitCurve3d, ShapeUpgrade_SplitCurve, OCP.Standard.Standard_Transient):
    """
    converts/splits a 3d curve of any type to a list of beziersconverts/splits a 3d curve of any type to a list of beziersconverts/splits a 3d curve of any type to a list of beziers
    """
    def Build(self,Segment : bool) -> None: 
        """
        Splits a list of beziers computed by Compute method according the split values and splitting parameters.
        """
    def Compute(self) -> None: 
        """
        Converts curve into a list of beziers, and stores the splitting parameters on original curve.
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
    def GetCircleMode(self) -> bool: 
        """
        Returns the Geom_Circle conversion mode.

        Returns the Geom_Circle conversion mode.
        """
    def GetConicMode(self) -> bool: 
        """
        Performs converting and computes the resulting shape.

        Performs converting and computes the resulting shape.
        """
    def GetCurves(self) -> OCP.TColGeom.TColGeom_HArray1OfCurve: 
        """
        None
        """
    def GetLineMode(self) -> bool: 
        """
        Returns the Geom_Line conversion mode.

        Returns the Geom_Line conversion mode.
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
    def Init(self,C : OCP.Geom.Geom_Curve,First : float,Last : float) -> None: 
        """
        Initializes with curve with its first and last parameters.

        Initializes with curve with its parameters.
        """
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the curve. First defines splitting values by method Compute(), then calls method Build().
        """
    def SetCircleMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_Circle to bezier.

        Sets mode for conversion Geom_Circle to bezier.
        """
    def SetConicMode(self,mode : bool) -> None: 
        """
        Returns the Geom_Conic conversion mode.

        Returns the Geom_Conic conversion mode.
        """
    def SetLineMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_Line to bezier.

        Sets mode for conversion Geom_Line to bezier.
        """
    def SetSplitValues(self,SplitValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets the parameters where splitting has to be done.
        """
    def SplitParams(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        Returns the list of splitted parameters in original curve parametrisation.
        """
    def SplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting values including the First and Last parameters of the input curve Merges input split values and new ones into myGlobalKnots
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one segment DONE2 - splitting is required, but gives only one segment (initial) DONE3 - geometric form of the curve or parametrisation is modified
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
class ShapeUpgrade_SplitCurve3dContinuity(ShapeUpgrade_SplitCurve3d, ShapeUpgrade_SplitCurve, OCP.Standard.Standard_Transient):
    """
    Corrects/splits a 2d curve with a continuity criterion. Tolerance is used to correct the curve at a knot that respects geometrically the criterion, in order to reduce the multiplicity of the knot.Corrects/splits a 2d curve with a continuity criterion. Tolerance is used to correct the curve at a knot that respects geometrically the criterion, in order to reduce the multiplicity of the knot.Corrects/splits a 2d curve with a continuity criterion. Tolerance is used to correct the curve at a knot that respects geometrically the criterion, in order to reduce the multiplicity of the knot.
    """
    def Build(self,Segment : bool) -> None: 
        """
        If Segment is True, the result is composed with segments of the curve bounded by the SplitValues. If Segment is False, the result is composed with trimmed Curves all based on the same complete curve.
        """
    def Compute(self) -> None: 
        """
        Calculates points for correction/splitting of the curve
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
    def GetCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def GetCurves(self) -> OCP.TColGeom.TColGeom_HArray1OfCurve: 
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
    def Init(self,C : OCP.Geom.Geom_Curve,First : float,Last : float) -> None: 
        """
        Initializes with curve with its first and last parameters.

        Initializes with curve with its parameters.
        """
    @overload
    def Init(self,C : OCP.Geom.Geom_Curve) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the curve. First defines splitting values by method Compute(), then calls method Build().
        """
    def SetCriterion(self,Criterion : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Sets criterion for splitting.
        """
    def SetSplitValues(self,SplitValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets the parameters where splitting has to be done.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        Sets tolerance.
        """
    def SplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting values including the First and Last parameters of the input curve Merges input split values and new ones into myGlobalKnots
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one segment DONE2 - splitting is required, but gives only one segment (initial) DONE3 - geometric form of the curve or parametrisation is modified
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
class ShapeUpgrade_ConvertSurfaceToBezierBasis(ShapeUpgrade_SplitSurface, OCP.Standard.Standard_Transient):
    """
    Converts a plane, bspline surface, surface of revolution, surface of extrusion, offset surface to grid of bezier basis surface ( bezier surface, surface of revolution based on bezier curve, offset surface based on any previous type).Converts a plane, bspline surface, surface of revolution, surface of extrusion, offset surface to grid of bezier basis surface ( bezier surface, surface of revolution based on bezier curve, offset surface based on any previous type).Converts a plane, bspline surface, surface of revolution, surface of extrusion, offset surface to grid of bezier basis surface ( bezier surface, surface of revolution based on bezier curve, offset surface based on any previous type).
    """
    def Build(self,Segment : bool) -> None: 
        """
        Splits a list of beziers computed by Compute method according the split values and splitting parameters.
        """
    def Compute(self,Segment : bool) -> None: 
        """
        Converts surface into a grid of bezier based surfaces, and stores this grid.
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
    def GetBSplineMode(self) -> bool: 
        """
        Returns the Geom_BSplineSurface conversion mode.

        Returns the Geom_BSplineSurface conversion mode.
        """
    def GetExtrusionMode(self) -> bool: 
        """
        Returns the Geom_SurfaceOfLinearExtrusion conversion mode.

        Returns the Geom_SurfaceOfLinearExtrusion conversion mode.
        """
    def GetPlaneMode(self) -> bool: 
        """
        Returns the Geom_Pline conversion mode.

        Returns the Geom_Pline conversion mode.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetRevolutionMode(self) -> bool: 
        """
        Returns the Geom_SurfaceOfRevolution conversion mode.

        Returns the Geom_SurfaceOfRevolution conversion mode.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface,UFirst : float,ULast : float,VFirst : float,VLast : float) -> None: 
        """
        Initializes with single supporting surface.

        Initializes with single supporting surface with bounding parameters.
        """
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the surface. First defines splitting values by method Compute(), then calls method Build().
        """
    def ResSurfaces(self) -> OCP.ShapeExtend.ShapeExtend_CompositeSurface: 
        """
        Returns obtained surfaces after splitting as CompositeSurface
        """
    def Segments(self) -> OCP.ShapeExtend.ShapeExtend_CompositeSurface: 
        """
        Returns the grid of bezier based surfaces correspondent to original surface.
        """
    def SetBSplineMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_BSplineSurface to Bezier

        Sets mode for conversion Geom_BSplineSurface to Bezier
        """
    def SetExtrusionMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_SurfaceOfLinearExtrusion to Bezier

        Sets mode for conversion Geom_SurfaceOfLinearExtrusion to Bezier
        """
    def SetPlaneMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_Plane to Bezier

        Sets mode for conversion Geom_Plane to Bezier
        """
    def SetRevolutionMode(self,mode : bool) -> None: 
        """
        Sets mode for conversion Geom_SurfaceOfRevolution to Bezier

        Sets mode for conversion Geom_SurfaceOfRevolution to Bezier
        """
    def SetUSplitValues(self,UValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets U parameters where splitting has to be done
        """
    def SetVSplitValues(self,VValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets V parameters where splitting has to be done
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one patch DONE2 - splitting is required, but gives only single patch (initial) DONE3 - geometric form of the surface or parametrisation is modified
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def USplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the U splitting values including the First and Last parameters of the input surface
        """
    def VSplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting V values including the First and Last parameters of the input surface
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
class ShapeUpgrade_SplitSurfaceAngle(ShapeUpgrade_SplitSurface, OCP.Standard.Standard_Transient):
    """
    Splits a surfaces of revolution, cylindrical, toroidal, conical, spherical so that each resulting segment covers not more than defined number of degrees.Splits a surfaces of revolution, cylindrical, toroidal, conical, spherical so that each resulting segment covers not more than defined number of degrees.Splits a surfaces of revolution, cylindrical, toroidal, conical, spherical so that each resulting segment covers not more than defined number of degrees.
    """
    def Build(self,Segment : bool) -> None: 
        """
        Performs splitting of the supporting surface. If resulting surface is B-Spline and Segment is True, the result is composed with segments of the surface bounded by the U and V SplitValues (method Geom_BSplineSurface::Segment is used). If Segment is False, the result is composed with Geom_RectangularTrimmedSurface all based on the same complete surface. Fields myNbResultingRow and myNbResultingCol must be set to specify the size of resulting grid of surfaces.
        """
    def Compute(self,Segment : bool) -> None: 
        """
        Performs splitting of the supporting surface(s). First defines splitting values, then calls inherited method.
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
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface,UFirst : float,ULast : float,VFirst : float,VLast : float) -> None: 
        """
        Initializes with single supporting surface.

        Initializes with single supporting surface with bounding parameters.
        """
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface) -> None: ...
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
    def MaxAngle(self) -> float: 
        """
        Returns maximal angle
        """
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the surface. First defines splitting values by method Compute(), then calls method Build().
        """
    def ResSurfaces(self) -> OCP.ShapeExtend.ShapeExtend_CompositeSurface: 
        """
        Returns obtained surfaces after splitting as CompositeSurface
        """
    def SetMaxAngle(self,MaxAngle : float) -> None: 
        """
        Set maximal angle
        """
    def SetUSplitValues(self,UValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets U parameters where splitting has to be done
        """
    def SetVSplitValues(self,VValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets V parameters where splitting has to be done
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one patch DONE2 - splitting is required, but gives only single patch (initial) DONE3 - geometric form of the surface or parametrisation is modified
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def USplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the U splitting values including the First and Last parameters of the input surface
        """
    def VSplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting V values including the First and Last parameters of the input surface
        """
    def __init__(self,MaxAngle : float) -> None: ...
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
class ShapeUpgrade_SplitSurfaceArea(ShapeUpgrade_SplitSurface, OCP.Standard.Standard_Transient):
    """
    Split surface in the parametric space in according specified number of splits on theSplit surface in the parametric space in according specified number of splits on theSplit surface in the parametric space in according specified number of splits on the
    """
    def Build(self,Segment : bool) -> None: 
        """
        Performs splitting of the supporting surface. If resulting surface is B-Spline and Segment is True, the result is composed with segments of the surface bounded by the U and V SplitValues (method Geom_BSplineSurface::Segment is used). If Segment is False, the result is composed with Geom_RectangularTrimmedSurface all based on the same complete surface. Fields myNbResultingRow and myNbResultingCol must be set to specify the size of resulting grid of surfaces.
        """
    def Compute(self,Segment : bool=True) -> None: 
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
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface,UFirst : float,ULast : float,VFirst : float,VLast : float) -> None: 
        """
        Initializes with single supporting surface.

        Initializes with single supporting surface with bounding parameters.
        """
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the surface. First defines splitting values by method Compute(), then calls method Build().
        """
    def ResSurfaces(self) -> OCP.ShapeExtend.ShapeExtend_CompositeSurface: 
        """
        Returns obtained surfaces after splitting as CompositeSurface
        """
    def SetUSplitValues(self,UValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets U parameters where splitting has to be done
        """
    def SetVSplitValues(self,VValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets V parameters where splitting has to be done
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one patch DONE2 - splitting is required, but gives only single patch (initial) DONE3 - geometric form of the surface or parametrisation is modified
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def USplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the U splitting values including the First and Last parameters of the input surface
        """
    def VSplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting V values including the First and Last parameters of the input surface
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
    @property
    def NbParts(self) -> int:
        """
        Set number of split for surfaces

        :type: int
        """
    @NbParts.setter
    def NbParts(self, arg1: int) -> None:
        """
        Set number of split for surfaces
        """
    pass
class ShapeUpgrade_SplitSurfaceContinuity(ShapeUpgrade_SplitSurface, OCP.Standard.Standard_Transient):
    """
    Splits a Surface with a continuity criterion. At the present moment C1 criterion is used only. This tool works with tolerance. If C0 surface can be corrected at a knot with given tolerance then the surface is corrected, otherwise it is spltted at that knot.Splits a Surface with a continuity criterion. At the present moment C1 criterion is used only. This tool works with tolerance. If C0 surface can be corrected at a knot with given tolerance then the surface is corrected, otherwise it is spltted at that knot.Splits a Surface with a continuity criterion. At the present moment C1 criterion is used only. This tool works with tolerance. If C0 surface can be corrected at a knot with given tolerance then the surface is corrected, otherwise it is spltted at that knot.
    """
    def Build(self,Segment : bool) -> None: 
        """
        Performs splitting of the supporting surface. If resulting surface is B-Spline and Segment is True, the result is composed with segments of the surface bounded by the U and V SplitValues (method Geom_BSplineSurface::Segment is used). If Segment is False, the result is composed with Geom_RectangularTrimmedSurface all based on the same complete surface. Fields myNbResultingRow and myNbResultingCol must be set to specify the size of resulting grid of surfaces.
        """
    def Compute(self,Segment : bool) -> None: 
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
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface,UFirst : float,ULast : float,VFirst : float,VLast : float) -> None: 
        """
        Initializes with single supporting surface.

        Initializes with single supporting surface with bounding parameters.
        """
    @overload
    def Init(self,S : OCP.Geom.Geom_Surface) -> None: ...
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
    def Perform(self,Segment : bool=True) -> None: 
        """
        Performs correction/splitting of the surface. First defines splitting values by method Compute(), then calls method Build().
        """
    def ResSurfaces(self) -> OCP.ShapeExtend.ShapeExtend_CompositeSurface: 
        """
        Returns obtained surfaces after splitting as CompositeSurface
        """
    def SetCriterion(self,Criterion : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Sets criterion for splitting.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        Sets tolerance.
        """
    def SetUSplitValues(self,UValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets U parameters where splitting has to be done
        """
    def SetVSplitValues(self,VValues : OCP.TColStd.TColStd_HSequenceOfReal) -> None: 
        """
        Sets V parameters where splitting has to be done
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status OK - no splitting is needed DONE1 - splitting required and gives more than one patch DONE2 - splitting is required, but gives only single patch (initial) DONE3 - geometric form of the surface or parametrisation is modified
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def USplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the U splitting values including the First and Last parameters of the input surface
        """
    def VSplitValues(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        returns all the splitting V values including the First and Last parameters of the input surface
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
class ShapeUpgrade_ClosedEdgeDivide(ShapeUpgrade_EdgeDivide, ShapeUpgrade_Tool, OCP.Standard.Standard_Transient):
    def Clear(self) -> None: 
        """
        None
        """
    def Compute(self,anEdge : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        None
        """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def GetSplitCurve2dTool(self) -> ShapeUpgrade_SplitCurve2d: 
        """
        Returns the tool for splitting pcurves.
        """
    def GetSplitCurve3dTool(self) -> ShapeUpgrade_SplitCurve3d: 
        """
        Returns the tool for splitting 3D curves.
        """
    def HasCurve2d(self) -> bool: 
        """
        None

        None
        """
    def HasCurve3d(self) -> bool: 
        """
        None

        None
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
    def Knots2d(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        None

        None
        """
    def Knots3d(self) -> OCP.TColStd.TColStd_HSequenceOfReal: 
        """
        None

        None
        """
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets supporting surface by face

        Sets supporting surface by face
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
        """
    def SetSplitCurve2dTool(self,splitCurve2dTool : ShapeUpgrade_SplitCurve2d) -> None: 
        """
        Sets the tool for splitting pcurves.
        """
    def SetSplitCurve3dTool(self,splitCurve3dTool : ShapeUpgrade_SplitCurve3d) -> None: 
        """
        Sets the tool for splitting 3D curves.
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
class ShapeUpgrade_UnifySameDomain(OCP.Standard.Standard_Transient):
    """
    This tool tries to unify faces and edges of the shape which lie on the same geometry. Faces/edges are considering as 'same-domain' if a group of neighbouring faces/edges are lying on coincident surfaces/curves. In this case these faces/edges can be unified into one face/edge. ShapeUpgrade_UnifySameDomain is initialized by a shape and the next optional parameters: UnifyFaces - tries to unify all possible faces UnifyEdges - tries to unify all possible edges ConcatBSplines - if this flag is set to true then all neighbouring edges, which lay on BSpline or Bezier curves with C1 continuity on their common vertices, will be merged into one common edge.This tool tries to unify faces and edges of the shape which lie on the same geometry. Faces/edges are considering as 'same-domain' if a group of neighbouring faces/edges are lying on coincident surfaces/curves. In this case these faces/edges can be unified into one face/edge. ShapeUpgrade_UnifySameDomain is initialized by a shape and the next optional parameters: UnifyFaces - tries to unify all possible faces UnifyEdges - tries to unify all possible edges ConcatBSplines - if this flag is set to true then all neighbouring edges, which lay on BSpline or Bezier curves with C1 continuity on their common vertices, will be merged into one common edge.This tool tries to unify faces and edges of the shape which lie on the same geometry. Faces/edges are considering as 'same-domain' if a group of neighbouring faces/edges are lying on coincident surfaces/curves. In this case these faces/edges can be unified into one face/edge. ShapeUpgrade_UnifySameDomain is initialized by a shape and the next optional parameters: UnifyFaces - tries to unify all possible faces UnifyEdges - tries to unify all possible edges ConcatBSplines - if this flag is set to true then all neighbouring edges, which lay on BSpline or Bezier curves with C1 continuity on their common vertices, will be merged into one common edge.
    """
    def AllowInternalEdges(self,theValue : bool) -> None: 
        """
        Sets the flag defining whether it is allowed to create internal edges inside merged faces in the case of non-manifold topology. Without this flag merging through multi connected edge is forbidden. Default value is false.
        """
    def Build(self) -> None: 
        """
        Performs unification and builds the resulting shape.
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
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        Returns the history of the processed shapes.

        Returns the history of the processed shapes.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Initialize(self,aShape : OCP.TopoDS.TopoDS_Shape,UnifyEdges : bool=True,UnifyFaces : bool=True,ConcatBSplines : bool=False) -> None: 
        """
        Initializes with a shape and necessary flags. It does not perform unification. If you intend to nullify the History place holder do it after initialization.
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
    def KeepShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape for avoid merging of the faces/edges. This shape can be vertex or edge. If the shape is a vertex it forbids merging of connected edges. If the shape is a edge it forbids merging of connected faces. This method can be called several times to keep several shapes.
        """
    def KeepShapes(self,theShapes : OCP.TopTools.TopTools_MapOfShape) -> None: 
        """
        Sets the map of shapes for avoid merging of the faces/edges. It allows passing a ready to use map instead of calling many times the method KeepShape.
        """
    def SetAngularTolerance(self,theValue : float) -> None: 
        """
        Sets the angular tolerance. If two shapes form a connection angle greater than this value they will not be merged. Default value is Precision::Angular().
        """
    def SetLinearTolerance(self,theValue : float) -> None: 
        """
        Sets the linear tolerance. It plays the role of chord error when taking decision about merging of shapes. Default value is Precision::Confusion().
        """
    def SetSafeInputMode(self,theValue : bool) -> None: 
        """
        Sets the flag defining the behavior of the algorithm regarding modification of input shape. If this flag is equal to True then the input (original) shape can't be modified during modification process. Default value is true.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Gives the resulting shape
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aShape : OCP.TopoDS.TopoDS_Shape,UnifyEdges : bool=True,UnifyFaces : bool=True,ConcatBSplines : bool=False) -> None: ...
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
class ShapeUpgrade_WireDivide(ShapeUpgrade_Tool, OCP.Standard.Standard_Transient):
    """
    Divides edges in the wire lying on the face or free wires or free edges with a criterion. Splits 3D curve and pcurve(s) of the edge on the face. Other pcurves which may be associated with the edge are simply copied. If 3D curve is splitted then pcurve on the face is splitted as well, and wice-versa. Input shape is not modified. The modifications made are recorded in external context (ShapeBuild_ReShape). This tool is applied to all edges before splitting them in order to keep sharing.Divides edges in the wire lying on the face or free wires or free edges with a criterion. Splits 3D curve and pcurve(s) of the edge on the face. Other pcurves which may be associated with the edge are simply copied. If 3D curve is splitted then pcurve on the face is splitted as well, and wice-versa. Input shape is not modified. The modifications made are recorded in external context (ShapeBuild_ReShape). This tool is applied to all edges before splitting them in order to keep sharing.Divides edges in the wire lying on the face or free wires or free edges with a criterion. Splits 3D curve and pcurve(s) of the edge on the face. Other pcurves which may be associated with the edge are simply copied. If 3D curve is splitted then pcurve on the face is splitted as well, and wice-versa. Input shape is not modified. The modifications made are recorded in external context (ShapeBuild_ReShape). This tool is applied to all edges before splitting them in order to keep sharing.
    """
    def Context(self) -> OCP.ShapeBuild.ShapeBuild_ReShape: 
        """
        Returns context

        Returns context
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
    def GetEdgeDivideTool(self) -> ShapeUpgrade_EdgeDivide: 
        """
        returns tool for splitting edges
        """
    def GetFixSmallCurveTool(self) -> ShapeUpgrade_FixSmallCurves: 
        """
        Returns tool for fixing small curves
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTransferParamTool(self) -> OCP.ShapeAnalysis.ShapeAnalysis_TransferParameters: 
        """
        Returns the tool for Transfer of parameters.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Initializes by wire and face

        Initializes by wire and surface
        """
    @overload
    def Init(self,W : OCP.TopoDS.TopoDS_Wire,S : OCP.Geom.Geom_Surface) -> None: ...
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
    def LimitTolerance(self,toler : float) -> float: 
        """
        Returns tolerance limited by [myMinTol,myMaxTol]

        Returns tolerance limited by [myMinTol,myMaxTol]
        """
    @overload
    def Load(self,W : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        Loads working wire

        Creates wire of one edge and calls Load for wire
        """
    @overload
    def Load(self,E : OCP.TopoDS.TopoDS_Edge) -> None: ...
    def MaxTolerance(self) -> float: 
        """
        Returns maximal allowed tolerance

        Returns maximal allowed tolerance
        """
    def MinTolerance(self) -> float: 
        """
        Returns minimal allowed tolerance

        Returns minimal allowed tolerance
        """
    def Perform(self) -> None: 
        """
        Computes the resulting wire by splitting all the edges according to splitting criteria. All the modifications made are recorded in context (ShapeBuild_ReShape). This tool is applied to all edges before splitting them in order to keep sharings. If no supporting face or surface is defined, only 3d splitting criteria are used.
        """
    def Precision(self) -> float: 
        """
        Returns basic precision value

        Returns basic precision value
        """
    def Set(self,tool : ShapeUpgrade_Tool) -> None: 
        """
        Copy all fields from another Root object
        """
    def SetContext(self,context : OCP.ShapeBuild.ShapeBuild_ReShape) -> None: 
        """
        Sets context

        Sets context
        """
    def SetEdgeDivideTool(self,edgeDivideTool : ShapeUpgrade_EdgeDivide) -> None: 
        """
        Sets tool for splitting edge
        """
    def SetEdgeMode(self,EdgeMode : int) -> None: 
        """
        Sets mode for splitting 3d curves from edges. 0 - only curve 3d from free edges. 1 - only curve 3d from shared edges. 2 - all curve 3d.
        """
    def SetFace(self,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets supporting surface by face
        """
    def SetFixSmallCurveTool(self,FixSmallCurvesTool : ShapeUpgrade_FixSmallCurves) -> None: 
        """
        Sets tool for fixing small curves with specified min tolerance;
        """
    def SetMaxTolerance(self,maxtol : float) -> None: 
        """
        Sets maximal allowed tolerance

        Sets maximal allowed tolerance
        """
    def SetMinTolerance(self,mintol : float) -> None: 
        """
        Sets minimal allowed tolerance

        Sets minimal allowed tolerance
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets basic precision value

        Sets basic precision value
        """
    def SetSplitCurve2dTool(self,splitCurve2dTool : ShapeUpgrade_SplitCurve2d) -> None: 
        """
        Sets the tool for splitting pcurves.
        """
    def SetSplitCurve3dTool(self,splitCurve3dTool : ShapeUpgrade_SplitCurve3d) -> None: 
        """
        Sets the tool for splitting 3D curves.
        """
    @overload
    def SetSurface(self,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Sets supporting surface

        Sets supporting surface with location
        """
    @overload
    def SetSurface(self,S : OCP.Geom.Geom_Surface) -> None: ...
    def SetTransferParamTool(self,TransferParam : OCP.ShapeAnalysis.ShapeAnalysis_TransferParameters) -> None: 
        """
        Sets the tool for Transfer parameters between curves and pcurves.
        """
    def Status(self,status : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Queries status of last call to Perform() OK - no edges were splitted, wire left untouched DONE1 - some edges were splitted FAIL1 - some edges have no 3d curve (skipped) FAIL2 - some edges have no pcurve (skipped)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Wire(self) -> OCP.TopoDS.TopoDS_Wire: 
        """
        Gives the resulting Wire (equal to initial one if not done or Null if not loaded)
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
