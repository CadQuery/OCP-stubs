import OCP.StepToGeom
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.gp
import OCP.Geom2d
import OCP.StepGeom
import OCP.StepRepr
import OCP.TColStd
__all__  = [
"StepToGeom"
]
class StepToGeom():
    """
    This class provides static methods to convert STEP geometric entities to OCCT. The methods returning handles will return null handle in case of error. The methods returning boolean will return True if succeeded and False if error.
    """
    @staticmethod
    def MakeAxis1Placement_s(SA : OCP.StepGeom.StepGeom_Axis1Placement) -> OCP.Geom.Geom_Axis1Placement: 
        """
        None
        """
    @staticmethod
    @overload
    def MakeAxis2Placement_s(SA : OCP.StepGeom.StepGeom_Axis2Placement3d) -> OCP.Geom.Geom_Axis2Placement: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def MakeAxis2Placement_s(SP : OCP.StepGeom.StepGeom_SuParameters) -> OCP.Geom.Geom_Axis2Placement: ...
    @staticmethod
    def MakeAxisPlacement_s(SA : OCP.StepGeom.StepGeom_Axis2Placement2d) -> OCP.Geom2d.Geom2d_AxisPlacement: 
        """
        None
        """
    @staticmethod
    def MakeBSplineCurve2d_s(SC : OCP.StepGeom.StepGeom_BSplineCurve) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def MakeBSplineCurve_s(SC : OCP.StepGeom.StepGeom_BSplineCurve) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def MakeBSplineSurface_s(SS : OCP.StepGeom.StepGeom_BSplineSurface) -> OCP.Geom.Geom_BSplineSurface: 
        """
        None
        """
    @staticmethod
    def MakeBoundedCurve2d_s(SC : OCP.StepGeom.StepGeom_BoundedCurve) -> OCP.Geom2d.Geom2d_BoundedCurve: 
        """
        None
        """
    @staticmethod
    def MakeBoundedCurve_s(SC : OCP.StepGeom.StepGeom_BoundedCurve) -> OCP.Geom.Geom_BoundedCurve: 
        """
        None
        """
    @staticmethod
    def MakeBoundedSurface_s(SS : OCP.StepGeom.StepGeom_BoundedSurface) -> OCP.Geom.Geom_BoundedSurface: 
        """
        None
        """
    @staticmethod
    def MakeCartesianPoint2d_s(SP : OCP.StepGeom.StepGeom_CartesianPoint) -> OCP.Geom2d.Geom2d_CartesianPoint: 
        """
        None
        """
    @staticmethod
    def MakeCartesianPoint_s(SP : OCP.StepGeom.StepGeom_CartesianPoint) -> OCP.Geom.Geom_CartesianPoint: 
        """
        None
        """
    @staticmethod
    def MakeCircle2d_s(SC : OCP.StepGeom.StepGeom_Circle) -> OCP.Geom2d.Geom2d_Circle: 
        """
        None
        """
    @staticmethod
    def MakeCircle_s(SC : OCP.StepGeom.StepGeom_Circle) -> OCP.Geom.Geom_Circle: 
        """
        None
        """
    @staticmethod
    def MakeConic2d_s(SC : OCP.StepGeom.StepGeom_Conic) -> OCP.Geom2d.Geom2d_Conic: 
        """
        None
        """
    @staticmethod
    def MakeConic_s(SC : OCP.StepGeom.StepGeom_Conic) -> OCP.Geom.Geom_Conic: 
        """
        None
        """
    @staticmethod
    def MakeConicalSurface_s(SS : OCP.StepGeom.StepGeom_ConicalSurface) -> OCP.Geom.Geom_ConicalSurface: 
        """
        None
        """
    @staticmethod
    def MakeCurve2d_s(SC : OCP.StepGeom.StepGeom_Curve) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    @staticmethod
    def MakeCurve_s(SC : OCP.StepGeom.StepGeom_Curve) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    @staticmethod
    def MakeCylindricalSurface_s(SS : OCP.StepGeom.StepGeom_CylindricalSurface) -> OCP.Geom.Geom_CylindricalSurface: 
        """
        None
        """
    @staticmethod
    def MakeDirection2d_s(SD : OCP.StepGeom.StepGeom_Direction) -> OCP.Geom2d.Geom2d_Direction: 
        """
        None
        """
    @staticmethod
    def MakeDirection_s(SD : OCP.StepGeom.StepGeom_Direction) -> OCP.Geom.Geom_Direction: 
        """
        None
        """
    @staticmethod
    def MakeElementarySurface_s(SS : OCP.StepGeom.StepGeom_ElementarySurface) -> OCP.Geom.Geom_ElementarySurface: 
        """
        None
        """
    @staticmethod
    def MakeEllipse2d_s(SC : OCP.StepGeom.StepGeom_Ellipse) -> OCP.Geom2d.Geom2d_Ellipse: 
        """
        None
        """
    @staticmethod
    def MakeEllipse_s(SC : OCP.StepGeom.StepGeom_Ellipse) -> OCP.Geom.Geom_Ellipse: 
        """
        None
        """
    @staticmethod
    def MakeHyperbola2d_s(SC : OCP.StepGeom.StepGeom_Hyperbola) -> OCP.Geom2d.Geom2d_Hyperbola: 
        """
        None
        """
    @staticmethod
    def MakeHyperbola_s(SC : OCP.StepGeom.StepGeom_Hyperbola) -> OCP.Geom.Geom_Hyperbola: 
        """
        None
        """
    @staticmethod
    def MakeLine2d_s(SC : OCP.StepGeom.StepGeom_Line) -> OCP.Geom2d.Geom2d_Line: 
        """
        None
        """
    @staticmethod
    def MakeLine_s(SC : OCP.StepGeom.StepGeom_Line) -> OCP.Geom.Geom_Line: 
        """
        None
        """
    @staticmethod
    def MakeParabola2d_s(SC : OCP.StepGeom.StepGeom_Parabola) -> OCP.Geom2d.Geom2d_Parabola: 
        """
        None
        """
    @staticmethod
    def MakeParabola_s(SC : OCP.StepGeom.StepGeom_Parabola) -> OCP.Geom.Geom_Parabola: 
        """
        None
        """
    @staticmethod
    def MakePlane_s(SP : OCP.StepGeom.StepGeom_Plane) -> OCP.Geom.Geom_Plane: 
        """
        None
        """
    @staticmethod
    def MakePolyline2d_s(SPL : OCP.StepGeom.StepGeom_Polyline) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def MakePolyline_s(SPL : OCP.StepGeom.StepGeom_Polyline) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def MakeRectangularTrimmedSurface_s(SS : OCP.StepGeom.StepGeom_RectangularTrimmedSurface) -> OCP.Geom.Geom_RectangularTrimmedSurface: 
        """
        None
        """
    @staticmethod
    def MakeSphericalSurface_s(SS : OCP.StepGeom.StepGeom_SphericalSurface) -> OCP.Geom.Geom_SphericalSurface: 
        """
        None
        """
    @staticmethod
    def MakeSurfaceOfLinearExtrusion_s(SS : OCP.StepGeom.StepGeom_SurfaceOfLinearExtrusion) -> OCP.Geom.Geom_SurfaceOfLinearExtrusion: 
        """
        None
        """
    @staticmethod
    def MakeSurfaceOfRevolution_s(SS : OCP.StepGeom.StepGeom_SurfaceOfRevolution) -> OCP.Geom.Geom_SurfaceOfRevolution: 
        """
        None
        """
    @staticmethod
    def MakeSurface_s(SS : OCP.StepGeom.StepGeom_Surface) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    @staticmethod
    def MakeSweptSurface_s(SS : OCP.StepGeom.StepGeom_SweptSurface) -> OCP.Geom.Geom_SweptSurface: 
        """
        None
        """
    @staticmethod
    def MakeToroidalSurface_s(SS : OCP.StepGeom.StepGeom_ToroidalSurface) -> OCP.Geom.Geom_ToroidalSurface: 
        """
        None
        """
    @staticmethod
    def MakeTransformation2d_s(SCTO : OCP.StepGeom.StepGeom_CartesianTransformationOperator2d,CT : OCP.gp.gp_Trsf2d) -> bool: 
        """
        None
        """
    @staticmethod
    def MakeTransformation3d_s(SCTO : OCP.StepGeom.StepGeom_CartesianTransformationOperator3d,CT : OCP.gp.gp_Trsf) -> bool: 
        """
        None
        """
    @staticmethod
    def MakeTrimmedCurve2d_s(SC : OCP.StepGeom.StepGeom_TrimmedCurve) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def MakeTrimmedCurve_s(SC : OCP.StepGeom.StepGeom_TrimmedCurve) -> OCP.Geom.Geom_TrimmedCurve: 
        """
        None
        """
    @staticmethod
    def MakeVectorWithMagnitude2d_s(SV : OCP.StepGeom.StepGeom_Vector) -> OCP.Geom2d.Geom2d_VectorWithMagnitude: 
        """
        None
        """
    @staticmethod
    def MakeVectorWithMagnitude_s(SV : OCP.StepGeom.StepGeom_Vector) -> OCP.Geom.Geom_VectorWithMagnitude: 
        """
        None
        """
    @staticmethod
    def MakeYprRotation_s(SR : StepKinematics_SpatialRotation,theCntxt : OCP.StepRepr.StepRepr_GlobalUnitAssignedContext) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
