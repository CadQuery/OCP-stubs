import OCP.ShapeConstruct
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.GeomAbs
import OCP.TColgp
import OCP.Geom2d
import OCP.gp
import OCP.Geom
import OCP.TopAbs
import OCP.BRepBuilderAPI
import OCP.Standard
import OCP.ShapeExtend
import OCP.TopoDS
import OCP.ShapeAnalysis
import OCP.TColStd
__all__  = [
"ShapeConstruct",
"ShapeConstruct_Curve",
"ShapeConstruct_MakeTriangulation",
"ShapeConstruct_ProjectCurveOnSurface"
]
class ShapeConstruct():
    """
    This package provides new algorithms for constructing new geometrical objects and topological shapes. It complements and extends algorithms available in Open CASCADE topological and geometrical toolkist. The functionality provided by this package are the following: projecting curves on surface, adjusting curve to have given start and end points. P
    """
    @staticmethod
    @overload
    def ConvertCurveToBSpline_s(C2D : OCP.Geom2d.Geom2d_Curve,First : float,Last : float,Tol2d : float,Continuity : OCP.GeomAbs.GeomAbs_Shape,MaxSegments : int,MaxDegree : int) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Tool for wire triangulation

        None
        """
    @staticmethod
    @overload
    def ConvertCurveToBSpline_s(C3D : OCP.Geom.Geom_Curve,First : float,Last : float,Tol3d : float,Continuity : OCP.GeomAbs.GeomAbs_Shape,MaxSegments : int,MaxDegree : int) -> OCP.Geom.Geom_BSplineCurve: ...
    @staticmethod
    def ConvertSurfaceToBSpline_s(surf : OCP.Geom.Geom_Surface,UF : float,UL : float,VF : float,VL : float,Tol3d : float,Continuity : OCP.GeomAbs.GeomAbs_Shape,MaxSegments : int,MaxDegree : int) -> OCP.Geom.Geom_BSplineSurface: 
        """
        None
        """
    @staticmethod
    @overload
    def JoinCurves_s(c3d1 : OCP.Geom.Geom_Curve,ac3d2 : OCP.Geom.Geom_Curve,Orient1 : OCP.TopAbs.TopAbs_Orientation,Orient2 : OCP.TopAbs.TopAbs_Orientation,first1 : float,last1 : float,first2 : float,last2 : float,c3dOut : OCP.Geom.Geom_Curve,isRev1 : bool,isRev2 : bool) -> bool: 
        """
        Method for joininig curves 3D. Parameters : c3d1,ac3d2 - initial curves Orient1, Orient2 - initial edges orientations. first1,last1,first2,last2 - parameters for trimming curves (re-calculate with account of orientation edges) c3dOut - result curve isRev1,isRev2 - out parameters indicative on possible errors. Return value : True - if curves were joined successfully, else - False.

        Method for joininig curves 3D. Parameters : c3d1,ac3d2 - initial curves Orient1, Orient2 - initial edges orientations. first1,last1,first2,last2 - parameters for trimming curves (re-calculate with account of orientation edges) c3dOut - result curve isRev1,isRev2 - out parameters indicative on possible errors. isError - input parameter indicative possible errors due to that one from edges have one vertex Return value : True - if curves were joined successfully, else - False.
        """
    @staticmethod
    @overload
    def JoinCurves_s(c2d1 : OCP.Geom2d.Geom2d_Curve,ac2d2 : OCP.Geom2d.Geom2d_Curve,Orient1 : OCP.TopAbs.TopAbs_Orientation,Orient2 : OCP.TopAbs.TopAbs_Orientation,first1 : float,last1 : float,first2 : float,last2 : float,c2dOut : OCP.Geom2d.Geom2d_Curve,isRev1 : bool,isRev2 : bool,isError : bool=False) -> bool: ...
    @staticmethod
    def JoinPCurves_s(theEdges : OCP.TopTools.TopTools_HSequenceOfShape,theFace : OCP.TopoDS.TopoDS_Face,theEdge : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        join pcurves of the <theEdge> on the <theFace> try to use pcurves from originas edges <theEdges> Returns false if cannot join pcurves
        """
    def __init__(self) -> None: ...
    pass
class ShapeConstruct_Curve():
    """
    Adjusts curve to have start and end points at the given points (currently works on lines and B-Splines only)
    """
    def AdjustCurve(self,C3D : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,take1 : bool=True,take2 : bool=True) -> bool: 
        """
        Modifies a curve in order to make its bounds confused with given points. Works only on lines and B-Splines, returns True in this case, else returns False. For line considers both bounding points, for B-Splines only specified.
        """
    def AdjustCurve2d(self,C2D : OCP.Geom2d.Geom2d_Curve,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,take1 : bool=True,take2 : bool=True) -> bool: 
        """
        Modifies a curve in order to make its bounds confused with given points. Works only on lines and B-Splines, returns True in this case, else returns False.
        """
    def AdjustCurveSegment(self,C3D : OCP.Geom.Geom_Curve,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,U1 : float,U2 : float) -> bool: 
        """
        Modifies a curve in order to make its bounds confused with given points. Works only on lines and B-Splines.
        """
    @overload
    def ConvertToBSpline(self,C : OCP.Geom.Geom_Curve,first : float,last : float,prec : float) -> OCP.Geom.Geom_BSplineCurve: 
        """
        Converts a curve of any type (only part from first to last) to bspline. The method of conversion depends on the type of original curve: BSpline -> C.Segment(first,last) Bezier and Line -> GeomConvert::CurveToBSplineCurve(C).Segment(first,last) Conic and Other -> Approx_Curve3d(C[first,last],prec,C1,9,1000)

        Converts a curve of any type (only part from first to last) to bspline. The method of conversion depends on the type of original curve: BSpline -> C.Segment(first,last) Bezier and Line -> GeomConvert::CurveToBSplineCurve(C).Segment(first,last) Conic and Other -> Approx_Curve2d(C[first,last],prec,C1,9,1000)
        """
    @overload
    def ConvertToBSpline(self,C : OCP.Geom2d.Geom2d_Curve,first : float,last : float,prec : float) -> OCP.Geom2d.Geom2d_BSplineCurve: ...
    @staticmethod
    @overload
    def FixKnots_s(knots : OCP.TColStd.TColStd_HArray1OfReal) -> bool: 
        """
        None

        Fix bspline knots to ensure that there is enough gap between neighbouring values Returns True if something fixed (by shifting knot)
        """
    @staticmethod
    @overload
    def FixKnots_s(knots : OCP.TColStd.TColStd_Array1OfReal) -> bool: ...
    def __init__(self) -> None: ...
    pass
class ShapeConstruct_MakeTriangulation(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    None
    """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        None
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,wire : OCP.TopoDS.TopoDS_Wire,prec : float=0.0) -> None: ...
    @overload
    def __init__(self,pnts : OCP.TColgp.TColgp_Array1OfPnt,prec : float=0.0) -> None: ...
    pass
class ShapeConstruct_ProjectCurveOnSurface(OCP.Standard.Standard_Transient):
    """
    This tool provides a method for computing pcurve by projecting 3d curve onto a surface. Projection is done by 23 or more points (this number is changed for B-Splines according to the following rule: the total number of the points is not less than number of spans * (degree + 1); it is increased recursively starting with 23 and is added with 22 until the condition is fulfilled). Isoparametric cases (if curve corresponds to U=const or V=const on the surface) are recognized with the given precision.This tool provides a method for computing pcurve by projecting 3d curve onto a surface. Projection is done by 23 or more points (this number is changed for B-Splines according to the following rule: the total number of the points is not less than number of spans * (degree + 1); it is increased recursively starting with 23 and is added with 22 until the condition is fulfilled). Isoparametric cases (if curve corresponds to U=const or V=const on the surface) are recognized with the given precision.This tool provides a method for computing pcurve by projecting 3d curve onto a surface. Projection is done by 23 or more points (this number is changed for B-Splines according to the following rule: the total number of the points is not less than number of spans * (degree + 1); it is increased recursively starting with 23 and is added with 22 until the condition is fulfilled). Isoparametric cases (if curve corresponds to U=const or V=const on the surface) are recognized with the given precision.
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
    def Init(self,surf : OCP.ShapeAnalysis.ShapeAnalysis_Surface,preci : float) -> None: 
        """
        Initializes the object with all necessary parameters, i.e. surface and precision

        Initializes the object with all necessary parameters, i.e. surface and precision
        """
    @overload
    def Init(self,surf : OCP.Geom.Geom_Surface,preci : float) -> None: ...
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
    def Perform(self,c3d : OCP.Geom.Geom_Curve,First : float,Last : float,c2d : OCP.Geom2d.Geom2d_Curve,TolFirst : float=-1.0,TolLast : float=-1.0) -> bool: 
        """
        Computes the projection of 3d curve onto a surface using the specialized algorithm. Returns False if projector fails, otherwise, if pcurve computed successfully, returns True. The output curve 2D is guaranteed to be same-parameter with input curve 3D on the interval [First, Last]. If the output curve lies on a direct line the infinite line is returned, in the case same-parameter condition is satisfied. TolFirst and TolLast are the tolerances at the ends of input curve 3D.
        """
    def PerformByProjLib(self,c3d : OCP.Geom.Geom_Curve,First : float,Last : float,c2d : OCP.Geom2d.Geom2d_Curve,continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1,maxdeg : int=12,nbinterval : int=-1) -> bool: 
        """
        Computes the projection of 3d curve onto a surface using the standard algorithm from ProjLib. Returns False if standard projector fails or raises an exception or cuts the curve by parametrical bounds of the surface. Else, if pcurve computed successfully, returns True. The continuity, maxdeg and nbinterval are parameters of call to Approx_CurveOnSurface. If nbinterval is equal to -1 (default), this value is computed depending on source 3d curve and surface.
        """
    def SetPrecision(self,preci : float) -> None: 
        """
        Sets value for current precision
        """
    @overload
    def SetSurface(self,surf : OCP.Geom.Geom_Surface) -> None: 
        """
        Loads a surface (in the form of Geom_Surface) to project on

        Loads a surface (in the form of ShapeAnalysis_Surface) to project on
        """
    @overload
    def SetSurface(self,surf : OCP.ShapeAnalysis.ShapeAnalysis_Surface) -> None: ...
    def Status(self,theStatus : OCP.ShapeExtend.ShapeExtend_Status) -> bool: 
        """
        Returns the status of last Perform
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
    @property
    def AdjustOverDegenMode(self) -> int:
        """
        :type: int
        """
    @AdjustOverDegenMode.setter
    def AdjustOverDegenMode(self, arg1: int) -> None:
        pass
    @property
    def BuildCurveMode(self) -> bool:
        """
        :type: bool
        """
    @BuildCurveMode.setter
    def BuildCurveMode(self, arg1: bool) -> None:
        pass
    pass
