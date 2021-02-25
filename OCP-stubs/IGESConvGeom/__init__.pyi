import OCP.IGESConvGeom
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.IGESGeom
import OCP.Geom
import OCP.Geom2d
__all__  = [
"IGESConvGeom",
"IGESConvGeom_GeomBuilder"
]
class IGESConvGeom():
    """
    This package is intended to gather geometric conversion which are not immediate but can be used for several purposes : mainly, standard conversion to and from CasCade geometric and topologic data, and adaptations of IGES files as required (as replacing Spline entities to BSpline equivalents).
    """
    @staticmethod
    @overload
    def IncreaseCurveContinuity_s(curve : OCP.Geom2d.Geom2d_BSplineCurve,epsgeom : float,continuity : int=2) -> int: 
        """
        Tries to increase curve continuity with tolerance <epsgeom> <continuity> is the new desired continuity, can be 1 or 2 (more than 2 is considered as 2). Returns the new maximum continuity obtained on all knots. Remark that, for instance with <continuity> = 2, even if not all the knots can be passed to C2, all knots which can be are.

        None
        """
    @staticmethod
    @overload
    def IncreaseCurveContinuity_s(curve : OCP.Geom.Geom_BSplineCurve,epsgeom : float,continuity : int=2) -> int: ...
    @staticmethod
    def IncreaseSurfaceContinuity_s(surface : OCP.Geom.Geom_BSplineSurface,epsgeom : float,continuity : int=2) -> int: 
        """
        Tries to increase Surface continuity with tolerance <epsgeom> <continuity> is the new desired continuity, can be 1 or 2 (more than 2 is considered as 2). Returns the new maximum continuity obtained on all knots. Remark that, for instance with <continuity> = 2, even if not all the knots can be passed to C2, all knots which can be are.
        """
    @staticmethod
    def SplineCurveFromIGES_s(igesent : OCP.IGESGeom.IGESGeom_SplineCurve,epscoef : float,epsgeom : float,result : OCP.Geom.Geom_BSplineCurve) -> int: 
        """
        basic tool to build curves from IGESGeom (arrays of points, Transformations, evaluation of points in a datum) Converts a SplineCurve from IGES to a BSplineCurve from CasCade <epscoef> gives tolerance to consider coefficient to be nul <epsgeom> gives tolerance to consider poles to be equal The returned value is a status with these possible values : - 0 OK, done - 1 the result is not guaranteed to be C0 (with <epsgeom>) - 2 SplineType not processed (allowed : max 3) (no result produced) - 3 error during creation of control points (no result produced) - 4 polynomial equation is not correct (no result produced) - 5 less than one segment (no result produced)
        """
    @staticmethod
    def SplineSurfaceFromIGES_s(igesent : OCP.IGESGeom.IGESGeom_SplineSurface,epscoef : float,epsgeom : float,result : OCP.Geom.Geom_BSplineSurface) -> int: 
        """
        Converts a SplineSurface from IGES to a BSplineSurface from CasCade <epscoef> gives tolerance to consider coefficient to be nul <epsgeom> gives tolerance to consider poles to be equal The returned value is a status with these possible values : - 0 OK, done - 1 the result is not guaranteed to be C0 (with <epsgeom>) - 2 degree is not compatible with code boundary type (warning) but C0 is OK - 3 idem but C0 is not guaranteed (warning) - 4 degree has been determined to be nul, either in U or V (no result produced) - 5 less than one segment in U or V (no result produced)
        """
    def __init__(self) -> None: ...
    pass
class IGESConvGeom_GeomBuilder():
    """
    This class provides some useful basic tools to build IGESGeom curves, especially : define a curve in a plane in 3D space (ex. Circular or Conic arc, or Copious Data defined in 2D) make a CopiousData from a list of points/vectors
    """
    def AddVec(self,val : OCP.gp.gp_XYZ) -> None: 
        """
        Adds a Vector part to the list of points. It will be used for CopiousData, datatype=3, only. AddXY and AddXYZ consider a null vector part (0,0,0) AddVec adds to the last added XY or XYZ
        """
    def AddXY(self,val : OCP.gp.gp_XY) -> None: 
        """
        Adds a XY (Z=0) to the list of points
        """
    def AddXYZ(self,val : OCP.gp.gp_XYZ) -> None: 
        """
        Adds a XYZ to the list of points
        """
    def Clear(self) -> None: 
        """
        Clears list of Points/Vectors and data about Transformation
        """
    def EvalXYZ(self,val : OCP.gp.gp_XYZ) -> Tuple[float, float, float]: 
        """
        Evaluates a XYZ value in the Position already defined. Returns the transformed coordinates. For a 2D definition, X,Y will then be used to define a XY and Z will be regarded as a Z Displacement (can be ignored)
        """
    def IsIdentity(self) -> bool: 
        """
        Returns True if the Position is Identity
        """
    def IsTranslation(self) -> bool: 
        """
        Returns True if the Position is a Translation only Remark : Identity and ZOnly will answer True
        """
    def IsZOnly(self) -> bool: 
        """
        Returns True if the Position corresponds to a Z-Displacement, i.e. is a Translation only, and only on Z Remark : Identity will answer True
        """
    def MakeCopiousData(self,datatype : int,polyline : bool=False) -> OCP.IGESGeom.IGESGeom_CopiousData: 
        """
        Makes a CopiousData with the list of recorded Points/Vectors according to <datatype>, which must be 1,2 or 3 If <polyline> is given True, the CopiousData is coded as a Polyline, but <datatype> must not be 3 <datatype> = 1 : Common Z is computed as average of all Z <datatype> = 1 or 2 : Vectors are ignored
        """
    def MakeTransformation(self,unit : float=1.0) -> OCP.IGESGeom.IGESGeom_TransformationMatrix: 
        """
        Returns the IGES Transformation which corresponds to the Position. Even if it is an Identity : IsIdentity should be tested first. <unit> is the unit value in which the model is created : it is used to convert translation part
        """
    def NbPoints(self) -> int: 
        """
        Returns the count of already recorded points
        """
    def Point(self,num : int) -> OCP.gp.gp_XYZ: 
        """
        Returns a point given its rank (if added as XY, Z will be 0)
        """
    def Position(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the Position in which the method EvalXYZ will evaluate a XYZ. It can be regarded as defining a local system. It is initially set to Identity
        """
    @overload
    def SetPosition(self,pos : OCP.gp.gp_Ax1) -> None: 
        """
        Sets final position from an already defined Trsf

        Sets final position from an Ax3

        Sets final position from an Ax2

        Sets final position from an Ax1 (this means that origin point and Z-axis are defined, the other axes are defined arbitrarily)
        """
    @overload
    def SetPosition(self,pos : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def SetPosition(self,pos : OCP.gp.gp_Trsf) -> None: ...
    @overload
    def SetPosition(self,pos : OCP.gp.gp_Ax3) -> None: ...
    def __init__(self) -> None: ...
    pass
