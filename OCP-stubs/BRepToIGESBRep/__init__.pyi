import OCP.BRepToIGESBRep
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Transfer
import OCP.BRepToIGES
import OCP.Standard
import OCP.IGESData
import OCP.TopoDS
import OCP.IGESSolid
__all__  = [
"BRepToIGESBRep_Entity"
]
class BRepToIGESBRep_Entity(OCP.BRepToIGES.BRepToIGES_BREntity):
    """
    provides methods to transfer BRep entity from CASCADE to IGESBRep.
    """
    def AddEdge(self,myedge : OCP.TopoDS.TopoDS_Edge,mycurve3d : OCP.IGESData.IGESData_IGESEntity) -> int: 
        """
        Stores <myedge> in "myEdges" and <mycurve3d> in "myCurves". Returns the index of <myedge>.
        """
    @overload
    def AddFail(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    @overload
    def AddFail(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: ...
    def AddVertex(self,myvertex : OCP.TopoDS.TopoDS_Vertex) -> int: 
        """
        Stores <myvertex> in "myVertices" Returns the index of <myvertex>.
        """
    @overload
    def AddWarning(self,start : OCP.TopoDS.TopoDS_Shape,amess : str) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    @overload
    def AddWarning(self,start : OCP.Standard.Standard_Transient,amess : str) -> None: ...
    def Clear(self) -> None: 
        """
        Clears the contents of the fields
        """
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
    def HasShapeResult(self,start : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns True if start was already treated and has a result in "TheMap" else returns False.

        Returns True if start was already treated and has a result in "TheMap" else returns False.
        """
    @overload
    def HasShapeResult(self,start : OCP.Standard.Standard_Transient) -> bool: ...
    def IndexEdge(self,myedge : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        Returns the index of <myedge> in "myEdges"
        """
    def IndexVertex(self,myvertex : OCP.TopoDS.TopoDS_Vertex) -> int: 
        """
        Returns the index of <myvertex> in "myVertices"
        """
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
    def TransferCompSolid(self,start : OCP.TopoDS.TopoDS_CompSolid) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert an CompSolid entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    def TransferCompound(self,start : OCP.TopoDS.TopoDS_Compound) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert a Compound entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    @overload
    def TransferEdge(self,myedge : OCP.TopoDS.TopoDS_Edge,myface : OCP.TopoDS.TopoDS_Face,length : float) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Transfert an Edge entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.

        Transfert an Edge entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    @overload
    def TransferEdge(self,myedge : OCP.TopoDS.TopoDS_Edge) -> OCP.IGESData.IGESData_IGESEntity: ...
    def TransferEdgeList(self) -> None: 
        """
        Transfert an Edge entity from TopoDS to IGES
        """
    def TransferFace(self,start : OCP.TopoDS.TopoDS_Face) -> OCP.IGESSolid.IGESSolid_Face: 
        """
        Transfert a Face entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    def TransferShape(self,start : OCP.TopoDS.TopoDS_Shape) -> OCP.IGESData.IGESData_IGESEntity: 
        """
        Returns the result of the transfert of any Shape If the transfer has failed, this member return a NullEntity.
        """
    def TransferShell(self,start : OCP.TopoDS.TopoDS_Shell) -> OCP.IGESSolid.IGESSolid_Shell: 
        """
        Transfert an Shell entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    def TransferSolid(self,start : OCP.TopoDS.TopoDS_Solid) -> OCP.IGESSolid.IGESSolid_ManifoldSolid: 
        """
        Transfert a Solid entity from TopoDS to IGES If this Entity could not be converted, this member returns a NullEntity.
        """
    def TransferVertexList(self) -> None: 
        """
        Create the VertexList entity
        """
    def TransferWire(self,mywire : OCP.TopoDS.TopoDS_Wire,myface : OCP.TopoDS.TopoDS_Face,length : float) -> OCP.IGESSolid.IGESSolid_Loop: 
        """
        Transfert a Wire entity from TopoDS to IGES. Returns the curve associated to mywire in the parametric space of myface. If this Entity could not be converted, this member returns a NullEntity.
        """
    def __init__(self) -> None: ...
    pass
