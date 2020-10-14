import OCP.Geom2dToIGES
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IGESGeom
import OCP.IGESData
import OCP.Geom2d
__all__  = [
"Geom2dToIGES_Geom2dEntity",
"Geom2dToIGES_Geom2dCurve",
"Geom2dToIGES_Geom2dPoint",
"Geom2dToIGES_Geom2dVector"
]
class Geom2dToIGES_Geom2dEntity():
    """
    provides methods to transfer Geom2d entity from CASCADE to IGES.
    """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in millimeters.
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
    def __init__(self,GE : Geom2dToIGES_Geom2dEntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Geom2dToIGES_Geom2dCurve(Geom2dToIGES_Geom2dEntity):
    """
    This class implements the transfer of the Curve Entity from Geom2d To IGES. These can be : Curve . BoundedCurve * BSplineCurve * BezierCurve * TrimmedCurve . Conic * Circle * Ellipse * Hyperbloa * Line * Parabola . OffsetCurve
    """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in millimeters.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    def SetUnit(self,unit : float) -> None: 
        """
        Sets the value of the UnitFlag
        """
    def Transfer2dCurve(self,start : OCP.Geom2d.Geom2d_Curve,Udeb : float,Ufin : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert an Entity from Geom2d to IGES. If this Entity could not be converted, this member returns a NullEntity.
        """
    @overload
    def __init__(self,G2dE : Geom2dToIGES_Geom2dEntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Geom2dToIGES_Geom2dPoint(Geom2dToIGES_Geom2dEntity):
    """
    This class implements the transfer of the Point Entity from Geom2d to IGES . These are : . 2dPoint * 2dCartesianPoint
    """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in millimeters.
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
    def Transfer2dPoint(self,start : OCP.Geom2d.Geom2d_Point) -> OCP.IGESGeom.IGESGeom_Point: 
        """
        Transfert a Point from Geom to IGES. If this Entity could not be converted, this member returns a NullEntity.

        Transfert a CartesianPoint from Geom to IGES. If this Entity could not be converted, this member returns a NullEntity.
        """
    @overload
    def Transfer2dPoint(self,start : OCP.Geom2d.Geom2d_CartesianPoint) -> OCP.IGESGeom.IGESGeom_Point: ...
    @overload
    def __init__(self,G2dE : Geom2dToIGES_Geom2dEntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Geom2dToIGES_Geom2dVector(Geom2dToIGES_Geom2dEntity):
    """
    This class implements the transfer of the Vector from Geom2d to IGES . These can be : . Vector * Direction * VectorWithMagnitude
    """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in millimeters.
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
    def Transfer2dVector(self,start : OCP.Geom2d.Geom2d_VectorWithMagnitude) -> OCP.IGESGeom.IGESGeom_Direction: 
        """
        Transfert a GeometryEntity which answer True to the member : BRepToIGES::IsGeomVector(Geometry). If this Entity could not be converted, this member returns a NullEntity.

        None

        None
        """
    @overload
    def Transfer2dVector(self,start : OCP.Geom2d.Geom2d_Vector) -> OCP.IGESGeom.IGESGeom_Direction: ...
    @overload
    def Transfer2dVector(self,start : OCP.Geom2d.Geom2d_Direction) -> OCP.IGESGeom.IGESGeom_Direction: ...
    @overload
    def __init__(self,G2dE : Geom2dToIGES_Geom2dEntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
