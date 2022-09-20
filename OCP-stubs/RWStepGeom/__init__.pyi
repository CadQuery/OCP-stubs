import OCP.RWStepGeom
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepData
import OCP.StepGeom
import OCP.Interface
__all__  = [
"RWStepGeom_RWAxis1Placement",
"RWStepGeom_RWAxis2Placement2d",
"RWStepGeom_RWAxis2Placement3d",
"RWStepGeom_RWBSplineCurve",
"RWStepGeom_RWBSplineCurveWithKnots",
"RWStepGeom_RWBSplineCurveWithKnotsAndRationalBSplineCurve",
"RWStepGeom_RWBSplineSurface",
"RWStepGeom_RWBSplineSurfaceWithKnots",
"RWStepGeom_RWBSplineSurfaceWithKnotsAndRationalBSplineSurface",
"RWStepGeom_RWBezierCurve",
"RWStepGeom_RWBezierCurveAndRationalBSplineCurve",
"RWStepGeom_RWBezierSurface",
"RWStepGeom_RWBezierSurfaceAndRationalBSplineSurface",
"RWStepGeom_RWBoundaryCurve",
"RWStepGeom_RWBoundedCurve",
"RWStepGeom_RWBoundedSurface",
"RWStepGeom_RWCartesianPoint",
"RWStepGeom_RWCartesianTransformationOperator",
"RWStepGeom_RWCartesianTransformationOperator3d",
"RWStepGeom_RWCircle",
"RWStepGeom_RWCompositeCurve",
"RWStepGeom_RWCompositeCurveOnSurface",
"RWStepGeom_RWCompositeCurveSegment",
"RWStepGeom_RWConic",
"RWStepGeom_RWConicalSurface",
"RWStepGeom_RWCurve",
"RWStepGeom_RWCurveBoundedSurface",
"RWStepGeom_RWCurveReplica",
"RWStepGeom_RWCylindricalSurface",
"RWStepGeom_RWDegeneratePcurve",
"RWStepGeom_RWDegenerateToroidalSurface",
"RWStepGeom_RWDirection",
"RWStepGeom_RWElementarySurface",
"RWStepGeom_RWEllipse",
"RWStepGeom_RWEvaluatedDegeneratePcurve",
"RWStepGeom_RWGeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx",
"RWStepGeom_RWGeometricRepresentationContext",
"RWStepGeom_RWGeometricRepresentationContextAndGlobalUnitAssignedContext",
"RWStepGeom_RWGeometricRepresentationContextAndParametricRepresentationContext",
"RWStepGeom_RWGeometricRepresentationItem",
"RWStepGeom_RWHyperbola",
"RWStepGeom_RWIntersectionCurve",
"RWStepGeom_RWLine",
"RWStepGeom_RWOffsetCurve3d",
"RWStepGeom_RWOffsetSurface",
"RWStepGeom_RWOrientedSurface",
"RWStepGeom_RWOuterBoundaryCurve",
"RWStepGeom_RWParabola",
"RWStepGeom_RWPcurve",
"RWStepGeom_RWPlacement",
"RWStepGeom_RWPlane",
"RWStepGeom_RWPoint",
"RWStepGeom_RWPointOnCurve",
"RWStepGeom_RWPointOnSurface",
"RWStepGeom_RWPointReplica",
"RWStepGeom_RWPolyline",
"RWStepGeom_RWQuasiUniformCurve",
"RWStepGeom_RWQuasiUniformCurveAndRationalBSplineCurve",
"RWStepGeom_RWQuasiUniformSurface",
"RWStepGeom_RWQuasiUniformSurfaceAndRationalBSplineSurface",
"RWStepGeom_RWRationalBSplineCurve",
"RWStepGeom_RWRationalBSplineSurface",
"RWStepGeom_RWRectangularCompositeSurface",
"RWStepGeom_RWRectangularTrimmedSurface",
"RWStepGeom_RWReparametrisedCompositeCurveSegment",
"RWStepGeom_RWSeamCurve",
"RWStepGeom_RWSphericalSurface",
"RWStepGeom_RWSuParameters",
"RWStepGeom_RWSurface",
"RWStepGeom_RWSurfaceCurve",
"RWStepGeom_RWSurfaceCurveAndBoundedCurve",
"RWStepGeom_RWSurfaceOfLinearExtrusion",
"RWStepGeom_RWSurfaceOfRevolution",
"RWStepGeom_RWSurfacePatch",
"RWStepGeom_RWSurfaceReplica",
"RWStepGeom_RWSweptSurface",
"RWStepGeom_RWToroidalSurface",
"RWStepGeom_RWTrimmedCurve",
"RWStepGeom_RWUniformCurve",
"RWStepGeom_RWUniformCurveAndRationalBSplineCurve",
"RWStepGeom_RWUniformSurface",
"RWStepGeom_RWUniformSurfaceAndRationalBSplineSurface",
"RWStepGeom_RWVector"
]
class RWStepGeom_RWAxis1Placement():
    """
    Read & Write Module for Axis1Placement
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Axis1Placement) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Axis1Placement,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Axis1Placement) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWAxis2Placement2d():
    """
    Read & Write Module for Axis2Placement2d
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Axis2Placement2d) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Axis2Placement2d,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Axis2Placement2d) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWAxis2Placement3d():
    """
    Read & Write Module for Axis2Placement3d
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Axis2Placement3d) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Axis2Placement3d,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Axis2Placement3d) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBSplineCurve():
    """
    Read & Write Module for BSplineCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BSplineCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BSplineCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BSplineCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBSplineCurveWithKnots():
    """
    Read & Write Module for BSplineCurveWithKnots Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_BSplineCurveWithKnots,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BSplineCurveWithKnots) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BSplineCurveWithKnots,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BSplineCurveWithKnots) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBSplineCurveWithKnotsAndRationalBSplineCurve():
    """
    Read & Write Module for BSplineCurveWithKnotsAndRationalBSplineCurve Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBSplineSurface():
    """
    Read & Write Module for BSplineSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BSplineSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BSplineSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BSplineSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBSplineSurfaceWithKnots():
    """
    Read & Write Module for BSplineSurfaceWithKnots Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_BSplineSurfaceWithKnots,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BSplineSurfaceWithKnots) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BSplineSurfaceWithKnots,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BSplineSurfaceWithKnots) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBSplineSurfaceWithKnotsAndRationalBSplineSurface():
    """
    Read & Write Module for BSplineSurfaceWithKnotsAndRationalBSplineSurface Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBezierCurve():
    """
    Read & Write Module for BezierCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BezierCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BezierCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BezierCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBezierCurveAndRationalBSplineCurve():
    """
    Read & Write Module for BezierCurveAndRationalBSplineCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BezierCurveAndRationalBSplineCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BezierCurveAndRationalBSplineCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BezierCurveAndRationalBSplineCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBezierSurface():
    """
    Read & Write Module for BezierSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BezierSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BezierSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BezierSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBezierSurfaceAndRationalBSplineSurface():
    """
    Read & Write Module for BezierSurfaceAndRationalBSplineSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BezierSurfaceAndRationalBSplineSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BezierSurfaceAndRationalBSplineSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BezierSurfaceAndRationalBSplineSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBoundaryCurve():
    """
    Read & Write Module for BoundaryCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BoundaryCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_BoundaryCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BoundaryCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBoundedCurve():
    """
    Read & Write Module for BoundedCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BoundedCurve) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BoundedCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWBoundedSurface():
    """
    Read & Write Module for BoundedSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_BoundedSurface) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_BoundedSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCartesianPoint():
    """
    Read & Write Module for CartesianPoint
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_CartesianPoint) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCartesianTransformationOperator():
    """
    Read & Write Module for CartesianTransformationOperator
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_CartesianTransformationOperator) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_CartesianTransformationOperator,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_CartesianTransformationOperator) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCartesianTransformationOperator3d():
    """
    Read & Write Module for CartesianTransformationOperator3d
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_CartesianTransformationOperator3d) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_CartesianTransformationOperator3d,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_CartesianTransformationOperator3d) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCircle():
    """
    Read & Write Module for Circle
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Circle) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Circle,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Circle) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCompositeCurve():
    """
    Read & Write Module for CompositeCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_CompositeCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_CompositeCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_CompositeCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCompositeCurveOnSurface():
    """
    Read & Write Module for CompositeCurveOnSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_CompositeCurveOnSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_CompositeCurveOnSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_CompositeCurveOnSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCompositeCurveSegment():
    """
    Read & Write Module for CompositeCurveSegment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_CompositeCurveSegment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_CompositeCurveSegment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_CompositeCurveSegment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWConic():
    """
    Read & Write Module for Conic
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Conic) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Conic,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Conic) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWConicalSurface():
    """
    Read & Write Module for ConicalSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_ConicalSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_ConicalSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_ConicalSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCurve():
    """
    Read & Write Module for Curve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Curve) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Curve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCurveBoundedSurface():
    """
    Read & Write tool for CurveBoundedSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_CurveBoundedSurface) -> Any: 
        """
        Reads CurveBoundedSurface
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_CurveBoundedSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_CurveBoundedSurface) -> None: 
        """
        Writes CurveBoundedSurface
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCurveReplica():
    """
    Read & Write Module for CurveReplica
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_CurveReplica) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_CurveReplica,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_CurveReplica) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWCylindricalSurface():
    """
    Read & Write Module for CylindricalSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_CylindricalSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_CylindricalSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_CylindricalSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWDegeneratePcurve():
    """
    Read & Write Module for DegeneratePcurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_DegeneratePcurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_DegeneratePcurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_DegeneratePcurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWDegenerateToroidalSurface():
    """
    Read & Write Module for DegenerateToroidalSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_DegenerateToroidalSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_DegenerateToroidalSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_DegenerateToroidalSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWDirection():
    """
    Read & Write Module for Direction Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_Direction,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Direction) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Direction) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWElementarySurface():
    """
    Read & Write Module for ElementarySurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_ElementarySurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_ElementarySurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_ElementarySurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWEllipse():
    """
    Read & Write Module for Ellipse Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_Ellipse,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Ellipse) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Ellipse,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Ellipse) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWEvaluatedDegeneratePcurve():
    """
    Read & Write Module for EvaluatedDegeneratePcurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_EvaluatedDegeneratePcurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_EvaluatedDegeneratePcurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_EvaluatedDegeneratePcurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWGeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx():
    """
    Read & Write Module for GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWGeometricRepresentationContext():
    """
    Read & Write Module for GeometricRepresentationContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_GeometricRepresentationContext) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_GeometricRepresentationContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWGeometricRepresentationContextAndGlobalUnitAssignedContext():
    """
    Read & Write Module for GeometricRepresentationContextAndGlobalUnitAssignedContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_GeometricRepresentationContextAndGlobalUnitAssignedContext) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_GeometricRepresentationContextAndGlobalUnitAssignedContext,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_GeometricRepresentationContextAndGlobalUnitAssignedContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWGeometricRepresentationContextAndParametricRepresentationContext():
    """
    Read & Write Module for GeometricRepresentationContextAndParametricRepresentationContext
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_GeometricRepresentationContextAndParametricRepresentationContext) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_GeometricRepresentationContextAndParametricRepresentationContext,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_GeometricRepresentationContextAndParametricRepresentationContext) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWGeometricRepresentationItem():
    """
    Read & Write Module for GeometricRepresentationItem
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_GeometricRepresentationItem) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_GeometricRepresentationItem) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWHyperbola():
    """
    Read & Write Module for Hyperbola
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Hyperbola) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Hyperbola,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Hyperbola) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWIntersectionCurve():
    """
    Read & Write Module for IntersectionCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_IntersectionCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_IntersectionCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_IntersectionCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWLine():
    """
    Read & Write Module for Line
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Line) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Line,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Line) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWOffsetCurve3d():
    """
    Read & Write Module for OffsetCurve3d
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_OffsetCurve3d) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_OffsetCurve3d,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_OffsetCurve3d) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWOffsetSurface():
    """
    Read & Write Module for OffsetSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_OffsetSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_OffsetSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_OffsetSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWOrientedSurface():
    """
    Read & Write tool for OrientedSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_OrientedSurface) -> Any: 
        """
        Reads OrientedSurface
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_OrientedSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Fills data for graph (shared items)
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_OrientedSurface) -> None: 
        """
        Writes OrientedSurface
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWOuterBoundaryCurve():
    """
    Read & Write Module for OuterBoundaryCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_OuterBoundaryCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_OuterBoundaryCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_OuterBoundaryCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWParabola():
    """
    Read & Write Module for Parabola
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Parabola) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Parabola,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Parabola) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWPcurve():
    """
    Read & Write Module for Pcurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Pcurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Pcurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Pcurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWPlacement():
    """
    Read & Write Module for Placement
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Placement) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Placement,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Placement) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWPlane():
    """
    Read & Write Module for Plane
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Plane) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Plane,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Plane) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWPoint():
    """
    Read & Write Module for Point
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Point) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Point) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWPointOnCurve():
    """
    Read & Write Module for PointOnCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_PointOnCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_PointOnCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_PointOnCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWPointOnSurface():
    """
    Read & Write Module for PointOnSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_PointOnSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_PointOnSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_PointOnSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWPointReplica():
    """
    Read & Write Module for PointReplica
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_PointReplica) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_PointReplica,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_PointReplica) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWPolyline():
    """
    Read & Write Module for Polyline
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Polyline) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Polyline,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Polyline) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWQuasiUniformCurve():
    """
    Read & Write Module for QuasiUniformCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_QuasiUniformCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_QuasiUniformCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_QuasiUniformCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWQuasiUniformCurveAndRationalBSplineCurve():
    """
    Read & Write Module for QuasiUniformCurveAndRationalBSplineCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_QuasiUniformCurveAndRationalBSplineCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_QuasiUniformCurveAndRationalBSplineCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_QuasiUniformCurveAndRationalBSplineCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWQuasiUniformSurface():
    """
    Read & Write Module for QuasiUniformSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_QuasiUniformSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_QuasiUniformSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_QuasiUniformSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWQuasiUniformSurfaceAndRationalBSplineSurface():
    """
    Read & Write Module for QuasiUniformSurfaceAndRationalBSplineSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_QuasiUniformSurfaceAndRationalBSplineSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_QuasiUniformSurfaceAndRationalBSplineSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_QuasiUniformSurfaceAndRationalBSplineSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWRationalBSplineCurve():
    """
    Read & Write Module for RationalBSplineCurve Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_RationalBSplineCurve,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_RationalBSplineCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_RationalBSplineCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_RationalBSplineCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWRationalBSplineSurface():
    """
    Read & Write Module for RationalBSplineSurface Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_RationalBSplineSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_RationalBSplineSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_RationalBSplineSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_RationalBSplineSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWRectangularCompositeSurface():
    """
    Read & Write Module for RectangularCompositeSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_RectangularCompositeSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_RectangularCompositeSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_RectangularCompositeSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWRectangularTrimmedSurface():
    """
    Read & Write Module for RectangularTrimmedSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_RectangularTrimmedSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_RectangularTrimmedSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_RectangularTrimmedSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWReparametrisedCompositeCurveSegment():
    """
    Read & Write Module for ReparametrisedCompositeCurveSegment
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_ReparametrisedCompositeCurveSegment) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_ReparametrisedCompositeCurveSegment,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_ReparametrisedCompositeCurveSegment) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSeamCurve():
    """
    Read & Write Module for SeamCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_SeamCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_SeamCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_SeamCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSphericalSurface():
    """
    Read & Write Module for SphericalSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_SphericalSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_SphericalSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_SphericalSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSuParameters():
    """
    Read & Write tool for SuParameters
    """
    def ReadStep(self,theData : OCP.StepData.StepData_StepReaderData,theNum : int,theAch : OCP.Interface.Interface_Check,theEnt : OCP.StepGeom.StepGeom_SuParameters) -> Any: 
        """
        None
        """
    def Share(self,theEnt : OCP.StepGeom.StepGeom_SuParameters,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,theSW : OCP.StepData.StepData_StepWriter,theEnt : OCP.StepGeom.StepGeom_SuParameters) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSurface():
    """
    Read & Write Module for Surface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Surface) -> Any: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Surface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSurfaceCurve():
    """
    Read & Write Module for SurfaceCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_SurfaceCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_SurfaceCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_SurfaceCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSurfaceCurveAndBoundedCurve():
    """
    Read StepGeom_SurfaceCurveAndBoundedCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_SurfaceCurveAndBoundedCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_SurfaceCurveAndBoundedCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_SurfaceCurveAndBoundedCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSurfaceOfLinearExtrusion():
    """
    Read & Write Module for SurfaceOfLinearExtrusion
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_SurfaceOfLinearExtrusion) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_SurfaceOfLinearExtrusion,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_SurfaceOfLinearExtrusion) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSurfaceOfRevolution():
    """
    Read & Write Module for SurfaceOfRevolution
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_SurfaceOfRevolution) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_SurfaceOfRevolution,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_SurfaceOfRevolution) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSurfacePatch():
    """
    Read & Write Module for SurfacePatch
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_SurfacePatch) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_SurfacePatch,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_SurfacePatch) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSurfaceReplica():
    """
    Read & Write Module for SurfaceReplica
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_SurfaceReplica) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_SurfaceReplica,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_SurfaceReplica) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWSweptSurface():
    """
    Read & Write Module for SweptSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_SweptSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_SweptSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_SweptSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWToroidalSurface():
    """
    Read & Write Module for ToroidalSurface Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_ToroidalSurface,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_ToroidalSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_ToroidalSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_ToroidalSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWTrimmedCurve():
    """
    Read & Write Module for TrimmedCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_TrimmedCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_TrimmedCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_TrimmedCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWUniformCurve():
    """
    Read & Write Module for UniformCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_UniformCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_UniformCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_UniformCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWUniformCurveAndRationalBSplineCurve():
    """
    Read & Write Module for UniformCurveAndRationalBSplineCurve
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_UniformCurveAndRationalBSplineCurve) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_UniformCurveAndRationalBSplineCurve,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_UniformCurveAndRationalBSplineCurve) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWUniformSurface():
    """
    Read & Write Module for UniformSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_UniformSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_UniformSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_UniformSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWUniformSurfaceAndRationalBSplineSurface():
    """
    Read & Write Module for UniformSurfaceAndRationalBSplineSurface
    """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_UniformSurfaceAndRationalBSplineSurface) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_UniformSurfaceAndRationalBSplineSurface,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_UniformSurfaceAndRationalBSplineSurface) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class RWStepGeom_RWVector():
    """
    Read & Write Module for Vector Check added by CKY , 7-OCT-1996
    """
    def Check(self,ent : OCP.StepGeom.StepGeom_Vector,shares : OCP.Interface.Interface_ShareTool,ach : OCP.Interface.Interface_Check) -> Any: 
        """
        None
        """
    def ReadStep(self,data : OCP.StepData.StepData_StepReaderData,num : int,ach : OCP.Interface.Interface_Check,ent : OCP.StepGeom.StepGeom_Vector) -> Any: 
        """
        None
        """
    def Share(self,ent : OCP.StepGeom.StepGeom_Vector,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        None
        """
    def WriteStep(self,SW : OCP.StepData.StepData_StepWriter,ent : OCP.StepGeom.StepGeom_Vector) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
