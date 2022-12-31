import OCP.BRepToIGES
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.TopLoc
import OCP.TopoDS
import OCP.IGESData
import OCP.gp
import OCP.TopTools
import OCP.Standard
import OCP.Transfer
__all__  = [
"BRepToIGES_BREntity",
"BRepToIGES_BRShell",
"BRepToIGES_BRSolid",
"BRepToIGES_BRWire"
]
class BRepToIGES_BREntity():
    """
    provides methods to transfer BRep entity from CASCADE to IGES.
    """
    @overload
    def AddFail(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    @overload
    def AddFail(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: ...
    @overload
    def AddWarning(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    @overload
    def AddWarning(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: ...
    def GetConvertSurfaceMode(self) -> bool: 
        """
        Returns mode for conversion of surfaces (value of parameter write.convertsurface.mode)
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetPCurveMode(self) -> bool: 
        """
        Returns mode for writing pcurves (value of parameter write.surfacecurve.mode)
        """
    @overload
    def GetShapeResult(self,start : OCP.TopoDS.TopoDS_Shape) -> OCP.Standard.Standard_Transient: 
        """
        Returns the result of the transfer of the Shape "start" contained in "TheMap" . (if HasShapeResult is True).

        Returns the result of the transfer of the Transient "start" contained in "TheMap" . (if HasShapeResult is True).
        """
    @overload
    def GetShapeResult(self,start : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: ...
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns the value of "TheMap"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in meters.
        """
    @overload
    def HasShapeResult(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if start was already treated and has a result in "TheMap" else returns False.

        Returns True if start was already treated and has a result in "TheMap" else returns False.
        """
    @overload
    def HasShapeResult(self,start : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def Init(self) -> None: 
        """
        Initializes the field of the tool BREntity with default creating values.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    @overload
    def SetShapeResult(self,start : OCP.Standard.Standard_Transient,result : OCP.Standard.Standard_Transient) -> None: 
        """
        set in "TheMap" the result of the transfer of the Shape "start".

        set in "TheMap" the result of the transfer of the Transient "start".
        """
    @overload
    def SetShapeResult(self,start : OCP.TopoDS.TopoDS_Shape,result : OCP.Standard.Standard_Transient) -> None: ...
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        Set the value of "TheMap"
        """
    def TransferShape(self,start : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the result of the transfert of any Shape If the transfer has failed, this member return a NullEntity.
        """
    def __init__(self) -> None: ...
    pass
class BRepToIGES_BRShell(BRepToIGES_BREntity):
    """
    This class implements the transfer of Shape Entities from Geom To IGES. These can be : . Vertex . Edge . Wire
    """
    @overload
    def AddFail(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    @overload
    def AddFail(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: ...
    @overload
    def AddWarning(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    @overload
    def AddWarning(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: ...
    def GetConvertSurfaceMode(self) -> bool: 
        """
        Returns mode for conversion of surfaces (value of parameter write.convertsurface.mode)
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetPCurveMode(self) -> bool: 
        """
        Returns mode for writing pcurves (value of parameter write.surfacecurve.mode)
        """
    @overload
    def GetShapeResult(self,start : OCP.TopoDS.TopoDS_Shape) -> OCP.Standard.Standard_Transient: 
        """
        Returns the result of the transfer of the Shape "start" contained in "TheMap" . (if HasShapeResult is True).

        Returns the result of the transfer of the Transient "start" contained in "TheMap" . (if HasShapeResult is True).
        """
    @overload
    def GetShapeResult(self,start : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: ...
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns the value of "TheMap"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in meters.
        """
    @overload
    def HasShapeResult(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if start was already treated and has a result in "TheMap" else returns False.

        Returns True if start was already treated and has a result in "TheMap" else returns False.
        """
    @overload
    def HasShapeResult(self,start : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def Init(self) -> None: 
        """
        Initializes the field of the tool BREntity with default creating values.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    @overload
    def SetShapeResult(self,start : OCP.Standard.Standard_Transient,result : OCP.Standard.Standard_Transient) -> None: 
        """
        set in "TheMap" the result of the transfer of the Shape "start".

        set in "TheMap" the result of the transfer of the Transient "start".
        """
    @overload
    def SetShapeResult(self,start : OCP.TopoDS.TopoDS_Shape,result : OCP.Standard.Standard_Transient) -> None: ...
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        Set the value of "TheMap"
        """
    def TransferFace(self,start : OCP.TopoDS.TopoDS_Face,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert a Face entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    def TransferShape(self,start : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the result of the transfert of any Shape If the transfer has failed, this member return a NullEntity.
        """
    @overload
    def TransferShell(self,start : OCP.TopoDS.TopoDS_Shell,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert an Shape entity from TopoDS to IGES This entity must be a Face or a Shell. If this Entity could not be converted, this member returns a NullEntity.

        Transfert an Shell entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    @overload
    def TransferShell(self,start : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def __init__(self,BR : BRepToIGES_BREntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepToIGES_BRSolid(BRepToIGES_BREntity):
    """
    This class implements the transfer of Shape Entities from Geom To IGES. These can be : . Vertex . Edge . Wire
    """
    @overload
    def AddFail(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    @overload
    def AddFail(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: ...
    @overload
    def AddWarning(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    @overload
    def AddWarning(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: ...
    def GetConvertSurfaceMode(self) -> bool: 
        """
        Returns mode for conversion of surfaces (value of parameter write.convertsurface.mode)
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetPCurveMode(self) -> bool: 
        """
        Returns mode for writing pcurves (value of parameter write.surfacecurve.mode)
        """
    @overload
    def GetShapeResult(self,start : OCP.TopoDS.TopoDS_Shape) -> OCP.Standard.Standard_Transient: 
        """
        Returns the result of the transfer of the Shape "start" contained in "TheMap" . (if HasShapeResult is True).

        Returns the result of the transfer of the Transient "start" contained in "TheMap" . (if HasShapeResult is True).
        """
    @overload
    def GetShapeResult(self,start : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: ...
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns the value of "TheMap"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in meters.
        """
    @overload
    def HasShapeResult(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if start was already treated and has a result in "TheMap" else returns False.

        Returns True if start was already treated and has a result in "TheMap" else returns False.
        """
    @overload
    def HasShapeResult(self,start : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def Init(self) -> None: 
        """
        Initializes the field of the tool BREntity with default creating values.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    @overload
    def SetShapeResult(self,start : OCP.Standard.Standard_Transient,result : OCP.Standard.Standard_Transient) -> None: 
        """
        set in "TheMap" the result of the transfer of the Shape "start".

        set in "TheMap" the result of the transfer of the Transient "start".
        """
    @overload
    def SetShapeResult(self,start : OCP.TopoDS.TopoDS_Shape,result : OCP.Standard.Standard_Transient) -> None: ...
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        Set the value of "TheMap"
        """
    def TransferCompSolid(self,start : OCP.TopoDS.TopoDS_CompSolid,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert an CompSolid entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    def TransferCompound(self,start : OCP.TopoDS.TopoDS_Compound,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert a Compound entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    def TransferShape(self,start : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the result of the transfert of any Shape If the transfer has failed, this member return a NullEntity.
        """
    @overload
    def TransferSolid(self,start : OCP.TopoDS.TopoDS_Solid,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert a Shape entity from TopoDS to IGES this entity must be a Solid or a CompSolid or a Compound. If this Entity could not be converted, this member returns a NullEntity.

        Transfert a Solid entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    @overload
    def TransferSolid(self,start : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,BR : BRepToIGES_BREntity) -> None: ...
    pass
class BRepToIGES_BRWire(BRepToIGES_BREntity):
    """
    This class implements the transfer of Shape Entities from Geom To IGES. These can be : . Vertex . Edge . Wire
    """
    @overload
    def AddFail(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    @overload
    def AddFail(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: ...
    @overload
    def AddWarning(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    @overload
    def AddWarning(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: ...
    def GetConvertSurfaceMode(self) -> bool: 
        """
        Returns mode for conversion of surfaces (value of parameter write.convertsurface.mode)
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "TheModel"
        """
    def GetPCurveMode(self) -> bool: 
        """
        Returns mode for writing pcurves (value of parameter write.surfacecurve.mode)
        """
    @overload
    def GetShapeResult(self,start : OCP.TopoDS.TopoDS_Shape) -> OCP.Standard.Standard_Transient: 
        """
        Returns the result of the transfer of the Shape "start" contained in "TheMap" . (if HasShapeResult is True).

        Returns the result of the transfer of the Transient "start" contained in "TheMap" . (if HasShapeResult is True).
        """
    @overload
    def GetShapeResult(self,start : OCP.Standard.Standard_Transient) -> OCP.Standard.Standard_Transient: ...
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_FinderProcess: 
        """
        Returns the value of "TheMap"
        """
    def GetUnit(self) -> float: 
        """
        Returns the value of the UnitFlag of the header of the model in meters.
        """
    @overload
    def HasShapeResult(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if start was already treated and has a result in "TheMap" else returns False.

        Returns True if start was already treated and has a result in "TheMap" else returns False.
        """
    @overload
    def HasShapeResult(self,start : OCP.TopoDS.TopoDS_Shape) -> bool: ...
    def Init(self) -> None: 
        """
        Initializes the field of the tool BREntity with default creating values.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "TheModel"
        """
    @overload
    def SetShapeResult(self,start : OCP.Standard.Standard_Transient,result : OCP.Standard.Standard_Transient) -> None: 
        """
        set in "TheMap" the result of the transfer of the Shape "start".

        set in "TheMap" the result of the transfer of the Transient "start".
        """
    @overload
    def SetShapeResult(self,start : OCP.TopoDS.TopoDS_Shape,result : OCP.Standard.Standard_Transient) -> None: ...
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_FinderProcess) -> None: 
        """
        Set the value of "TheMap"
        """
    @overload
    def TransferEdge(self,theEdge : OCP.TopoDS.TopoDS_Edge,theFace : OCP.TopoDS.TopoDS_Face,theOriginMap : OCP.TopTools.TopTools_DataMapOfShapeShape,theLength : float,theIsBRepMode : bool) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert an Edge 3d entity from TopoDS to IGES If edge is REVERSED and isBRepMode is False 3D edge curve is reversed

        Transfert an Edge 2d entity on a Face from TopoDS to IGES
        """
    @overload
    def TransferEdge(self,theEdge : OCP.TopoDS.TopoDS_Edge,theOriginMap : OCP.TopTools.TopTools_DataMapOfShapeShape,theIsBRepMode : bool) -> OCP.IGESData.IGESData_IGESEntity: ...
    def TransferShape(self,start : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the result of the transfert of any Shape If the transfer has failed, this member return a NullEntity.
        """
    @overload
    def TransferVertex(self,myvertex : OCP.TopoDS.TopoDS_Vertex,myedge : OCP.TopoDS.TopoDS_Edge,mysurface : OCP.Geom.Geom_Surface,myloc : OCP.TopLoc.TopLoc_Location,parameter : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert a Vertex entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.

        Transfert a Vertex entity on an Edge from TopoDS to IGES Returns the parameter of myvertex on myedge. If this Entity could not be converted, this member returns a NullEntity.

        Transfert a Vertex entity of an edge on a Face from TopoDS to IGES Returns the parameter of myvertex on the pcurve of myedge on myface If this Entity could not be converted, this member returns a NullEntity.

        Transfert a Vertex entity of an edge on a Surface from TopoDS to IGES Returns the parameter of myvertex on the pcurve of myedge on mysurface If this Entity could not be converted, this member returns a NullEntity.

        Transfert a Vertex entity on a Face from TopoDS to IGES Returns the parameters of myvertex on myface If this Entity could not be converted, this member returns a NullEntity.
        """
    @overload
    def TransferVertex(self,myvertex : OCP.TopoDS.TopoDS_Vertex,myface : OCP.TopoDS.TopoDS_Face,mypoint : OCP.gp.gp_Pnt2d) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferVertex(self,myvertex : OCP.TopoDS.TopoDS_Vertex,myedge : OCP.TopoDS.TopoDS_Edge,parameter : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferVertex(self,myvertex : OCP.TopoDS.TopoDS_Vertex,myedge : OCP.TopoDS.TopoDS_Edge,myface : OCP.TopoDS.TopoDS_Face,parameter : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferVertex(self,myvertex : OCP.TopoDS.TopoDS_Vertex) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferWire(self,start : OCP.TopoDS.TopoDS_Shape) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert a Shape entity from TopoDS to IGES this entity must be a Vertex or an Edge or a Wire. If this Entity could not be converted, this member returns a NullEntity.

        Transfert a Wire entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.

        Transfert a Wire entity from TopoDS to IGES.
        """
    @overload
    def TransferWire(self,mywire : OCP.TopoDS.TopoDS_Wire) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def TransferWire(self,theWire : OCP.TopoDS.TopoDS_Wire,theFace : OCP.TopoDS.TopoDS_Face,theOriginMap : OCP.TopTools.TopTools_DataMapOfShapeShape,theCurve2d : OCP.IGESData.IGESData_IGESEntity,theLength : float) -> OCP.IGESData.IGESData_IGESEntity: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,BR : BRepToIGES_BREntity) -> None: ...
    pass
