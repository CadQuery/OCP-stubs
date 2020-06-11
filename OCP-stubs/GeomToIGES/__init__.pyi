import OCP.GeomToIGES
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.IGESGeom
import OCP.IGESData
__all__  = [
"GeomToIGES_GeomEntity",
"GeomToIGES_GeomCurve",
"GeomToIGES_GeomPoint",
"GeomToIGES_GeomSurface",
"GeomToIGES_GeomVector"
]
class GeomToIGES_GeomEntity():
    """
    provides methods to transfer Geom entity from CASCADE to IGES.
    """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in meters.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    def SetUnit(self,unit : float) -> None: 
        """
        Sets the value of the UnitFlag
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,GE : GeomToIGES_GeomEntity) -> None: ...
    pass
class GeomToIGES_GeomCurve(GeomToIGES_GeomEntity):
    """
    This class implements the transfer of the Curve Entity from Geom To IGES. These can be : Curve . BoundedCurve * BSplineCurve * BezierCurve * TrimmedCurve . Conic * Circle * Ellipse * Hyperbloa * Line * Parabola . OffsetCurve
    """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in meters.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    def SetUnit(self,unit : float) -> None: 
        """
        Sets the value of the UnitFlag
        """
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_BezierCurve,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert a GeometryEntity which answer True to the member : BRepToIGES::IsGeomCurve(Geometry). If this Entity could not be converted, this member returns a NullEntity.

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_Hyperbola,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_Ellipse,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_Curve,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_BSplineCurve,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_TrimmedCurve,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_Line,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_OffsetCurve,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_Parabola,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_Circle,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_Conic,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferCurve(self,start : OCP.Geom.Geom_BoundedCurve,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def __init__(self,GE : GeomToIGES_GeomEntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomToIGES_GeomPoint(GeomToIGES_GeomEntity):
    """
    This class implements the transfer of the Point Entity from Geom to IGES . These are : . Point * CartesianPoint
    """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in meters.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    def SetUnit(self,unit : float) -> None: 
        """
        Sets the value of the UnitFlag
        """
    @overload
    def TransferPoint(self,start : OCP.Geom.Geom_CartesianPoint) -> OCP.IGESGeom.IGESGeom_Point: 
        """
        Transfert a Point from Geom to IGES. If this Entity could not be converted, this member returns a NullEntity.

        Transfert a CartesianPoint from Geom to IGES. If this Entity could not be converted, this member returns a NullEntity.
        """
    @overload
    def TransferPoint(self,start : OCP.Geom.Geom_Point) -> OCP.IGESGeom.IGESGeom_Point: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,GE : GeomToIGES_GeomEntity) -> None: ...
    pass
class GeomToIGES_GeomSurface(GeomToIGES_GeomEntity):
    """
    This class implements the transfer of the Surface Entity from Geom To IGES. These can be : . BoundedSurface * BSplineSurface * BezierSurface * RectangularTrimmedSurface . ElementarySurface * Plane * CylindricalSurface * ConicalSurface * SphericalSurface * ToroidalSurface . SweptSurface * SurfaceOfLinearExtrusion * SurfaceOfRevolution . OffsetSurface
    """
    def GetAnalyticMode(self) -> bool: 
        """
        Returns flag for writing elementary surfaces
        """
    def GetBRepMode(self) -> bool: 
        """
        Returns Brep mode flag.
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in meters.
        """
    def Length(self) -> float: 
        """
        Returns the value of "TheLength"
        """
    def SetAnalyticMode(self,flag : bool) -> None: 
        """
        Setst flag for writing elementary surfaces
        """
    def SetBRepMode(self,flag : bool) -> None: 
        """
        Sets BRep mode flag.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    def SetUnit(self,unit : float) -> None: 
        """
        Sets the value of the UnitFlag
        """
    def TransferConicalSurface(self,start : OCP.Geom.Geom_ConicalSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        None
        """
    def TransferCylindricalSurface(self,start : OCP.Geom.Geom_CylindricalSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        None
        """
    def TransferPlaneSurface(self,start : OCP.Geom.Geom_Plane,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        None
        """
    def TransferSphericalSurface(self,start : OCP.Geom.Geom_SphericalSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        None
        """
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_BSplineSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert a GeometryEntity which answer True to the member : BRepToIGES::IsGeomSurface(Geometry). If this Entity could not be converted, this member returns a NullEntity.

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_ElementarySurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_Plane,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_SurfaceOfRevolution,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_BoundedSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_RectangularTrimmedSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_BezierSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_ConicalSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_SweptSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_ToroidalSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_SurfaceOfLinearExtrusion,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_CylindricalSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_SphericalSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_Surface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferSurface(self,start : OCP.Geom.Geom_OffsetSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    def TransferToroidalSurface(self,start : OCP.Geom.Geom_ToroidalSurface,Udeb : float,Ufin : float,Vdeb : float,Vfin : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        None
        """
    @overload
    def __init__(self,GE : GeomToIGES_GeomEntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomToIGES_GeomVector(GeomToIGES_GeomEntity):
    """
    This class implements the transfer of the Vector from Geom to IGES . These can be : . Vector * Direction * VectorWithMagnitude
    """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in meters.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    def SetUnit(self,unit : float) -> None: 
        """
        Sets the value of the UnitFlag
        """
    @overload
    def TransferVector(self,start : OCP.Geom.Geom_Direction) -> OCP.IGESGeom.IGESGeom_Direction: 
        """
        Transfert a GeometryEntity which answer True to the member : BRepToIGES::IsGeomVector(Geometry). If this Entity could not be converted, this member returns a NullEntity.

        None

        None
        """
    @overload
    def TransferVector(self,start : OCP.Geom.Geom_VectorWithMagnitude) -> OCP.IGESGeom.IGESGeom_Direction: ...
    @overload
    def TransferVector(self,start : OCP.Geom.Geom_Vector) -> OCP.IGESGeom.IGESGeom_Direction: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,GE : GeomToIGES_GeomEntity) -> None: ...
    pass
