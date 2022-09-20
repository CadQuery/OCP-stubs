import OCP.IGESToBRep
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IGESSolid
import OCP.Transfer
import OCP.IGESData
import OCP.Interface
import OCP.Geom2d
import OCP.gp
import OCP.Standard
import OCP.ShapeExtend
import OCP.IGESGeom
import OCP.IGESBasic
import OCP.Geom
import OCP.TopoDS
import OCP.Message
import OCP.TColStd
__all__  = [
"IGESToBRep",
"IGESToBRep_Actor",
"IGESToBRep_AlgoContainer",
"IGESToBRep_CurveAndSurface",
"IGESToBRep_BasicCurve",
"IGESToBRep_BasicSurface",
"IGESToBRep_BRepEntity",
"IGESToBRep_IGESBoundary",
"IGESToBRep_Reader",
"IGESToBRep_ToolContainer",
"IGESToBRep_TopoCurve",
"IGESToBRep_TopoSurface"
]
class IGESToBRep():
    """
    Provides tools in order to transfer IGES entities to CAS.CADE.
    """
    @staticmethod
    def AlgoContainer_s() -> IGESToBRep_AlgoContainer: 
        """
        Returns default AlgoContainer
        """
    @staticmethod
    def IGESCurveToSequenceOfIGESCurve_s(curve : OCP.IGESData.IGESData_IGESEntity,sequence : OCP.TColStd.TColStd_HSequenceOfTransient) -> int: 
        """
        None
        """
    @staticmethod
    def Init_s() -> None: 
        """
        Creates and initializes default AlgoContainer.
        """
    @staticmethod
    def IsBRepEntity_s(start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Return True if the IGESEntity can be transferred by TransferBRepEntity. ex: VertexList, EdgeList, Loop, Face, Shell, Manifold Solid BRep Object from IGESSolid : 502, 504, 508, 510, 514, 186.
        """
    @staticmethod
    def IsBasicCurve_s(start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Return True if the IGESEntity can be transferred by TransferBasicCurve. ex: CircularArc, ConicArc, Line, CopiousData, BSplineCurve, SplineCurve... from IGESGeom : 104,110,112,126
        """
    @staticmethod
    def IsBasicSurface_s(start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Return True if the IGESEntity can be transferred by TransferBasicSurface. ex: BSplineSurface, SplineSurface... from IGESGeom : 114,128
        """
    @staticmethod
    def IsCurveAndSurface_s(start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Return True if the IGESEntity can be transferred by TransferCurveAndSurface. ex: All IGESEntity from IGESGeom
        """
    @staticmethod
    def IsTopoCurve_s(start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Return True if the IGESEntity can be transferred by TransferTopoCurve. ex: all Curves from IGESGeom : all basic curves,102,130,142,144
        """
    @staticmethod
    def IsTopoSurface_s(start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Return True if the IGESEntity can be transferred by TransferTopoSurface. ex: All Surfaces from IGESGeom : all basic surfaces,108,118,120,122,141,143
        """
    @staticmethod
    def SetAlgoContainer_s(aContainer : IGESToBRep_AlgoContainer) -> None: 
        """
        Sets default AlgoContainer
        """
    @staticmethod
    def TransferPCurve_s(fromedge : OCP.TopoDS.TopoDS_Edge,toedge : OCP.TopoDS.TopoDS_Edge,face : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IGESToBRep_Actor(OCP.Transfer.Transfer_ActorOfTransientProcess, OCP.Transfer.Transfer_ActorOfProcessForTransient, OCP.Standard.Standard_Transient):
    """
    This class performs the transfer of an Entity from IGESToBRepThis class performs the transfer of an Entity from IGESToBRepThis class performs the transfer of an Entity from IGESToBRep
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
    def GetContinuity(self) -> int: 
        """
        Return "thecontinuity"
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
    def IsLast(self) -> bool: 
        """
        Returns the Last status (see SetLast).
        """
    def Next(self) -> OCP.Transfer.Transfer_ActorOfProcessForTransient: 
        """
        Returns the Actor defined as Next, or a Null Handle
        """
    def NullResult(self) -> OCP.Transfer.Transfer_Binder: 
        """
        Returns a Binder for No Result, i.e. a Null Handle
        """
    def Recognize(self,start : OCP.Standard.Standard_Transient) -> bool: 
        """
        None
        """
    def SetContinuity(self,continuity : int=0) -> None: 
        """
        ---Purpose By default continuity = 0 if continuity = 1 : try C1 if continuity = 2 : try C2
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetModel(self,model : OCP.Interface.Interface_InterfaceModel) -> None: 
        """
        None
        """
    def SetNext(self,next : OCP.Transfer.Transfer_ActorOfProcessForTransient) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transfer(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_TransientProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferTransient(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_TransientProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Transferring(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_ProcessForTransient,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransientResult(self,res : OCP.Standard.Standard_Transient) -> OCP.Transfer.Transfer_SimpleBinderOfTransient: 
        """
        Prepares and Returns a Binder for a Transient Result Returns a Null Handle if <res> is itself Null
        """
    def UsedTolerance(self) -> float: 
        """
        Returns the tolerance which was actually used, either from the file or from statics
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
class IGESToBRep_AlgoContainer(OCP.Standard.Standard_Transient):
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
    def SetToolContainer(self,TC : IGESToBRep_ToolContainer) -> None: 
        """
        Sets ToolContainer

        Sets ToolContainer
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToolContainer(self) -> IGESToBRep_ToolContainer: 
        """
        Returns ToolContainer

        Returns ToolContainer
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
class IGESToBRep_CurveAndSurface():
    """
    Provides methods to transfer CurveAndSurface from IGES to CASCADE.
    """
    def AddShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the entity of the IGESEntity start ( type VertexList or EdgeList).
        """
    def GetContinuity(self) -> int: 
        """
        Returns the value of "myContinuity"

        Returns the value of "myContinuity"
        """
    def GetEpsCoeff(self) -> float: 
        """
        Returns the value of "myEpsCoeff"

        Returns the value of "myEpsCoeff"
        """
    def GetEpsGeom(self) -> float: 
        """
        Returns the value of "myEpsGeom"

        Returns the value of "myEpsGeom"
        """
    def GetEpsilon(self) -> float: 
        """
        Returns the value of "myEps"

        Returns the value of "myEps"
        """
    def GetMaxTol(self) -> float: 
        """
        Returns the value of "myMaxTol"

        Returns the value of "myMaxTol"
        """
    def GetMinTol(self) -> float: 
        """
        Returns the value of "myMinTol"

        Returns the value of "myMinTol"
        """
    def GetModeApprox(self) -> bool: 
        """
        Returns the value of "myModeApprox"

        Returns the value of "myModeApprox"
        """
    def GetModeTransfer(self) -> bool: 
        """
        Returns the value of "myModeIsTopo"

        Returns the value of "myModeIsTopo"
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "myModel"

        Returns the value of "myModel"
        """
    def GetOptimized(self) -> bool: 
        """
        Returns the value of "myContIsOpti"

        Returns the value of "myContIsOpti"
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfer of the IGESEntity "start" contained in "myMap" . (if HasShapeResult is True).

        Returns the numth result of the IGESEntity start (type VertexList or EdgeList) in "myMap". (if NbShapeResult is not null).
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,num : int) -> OCP.TopoDS.TopoDS_Shape: ...
    def GetSurfaceCurve(self) -> int: 
        """
        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d

        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d
        """
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the value of "myMsgReg"

        Returns the value of "myMsgReg"
        """
    def GetUVResolution(self) -> float: 
        """
        None
        """
    def GetUnitFactor(self) -> float: 
        """
        Returns the value of " myUnitFactor"

        Returns the value of " myUnitFactor"
        """
    def HasShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Returns True if start was already treated and has a result in "myMap" else returns False.
        """
    def Init(self) -> None: 
        """
        Initializes the field of the tool CurveAndSurface with default creating values.
        """
    def NbShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> int: 
        """
        Returns the number of shapes results contained in "myMap" for the IGESEntity start ( type VertexList or EdgeList).
        """
    def SendFail(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    def SendMsg(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Information message from the definition of a Msg (Original+Value)

        Records a new Information message from the definition of a Msg (Original+Value)
        """
    def SendWarning(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    def SetContinuity(self,continuity : int) -> None: 
        """
        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2

        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2
        """
    def SetEpsCoeff(self,eps : float) -> None: 
        """
        Changes the value of "myEpsCoeff"

        Changes the value of "myEpsCoeff"
        """
    def SetEpsGeom(self,eps : float) -> None: 
        """
        Changes the value of "myEpsGeom"
        """
    def SetEpsilon(self,eps : float) -> None: 
        """
        Changes the value of "myEps"

        Changes the value of "myEps"
        """
    def SetMaxTol(self,maxtol : float) -> None: 
        """
        Changes the value of "myMaxTol"

        Changes the value of "myMaxTol"
        """
    def SetMinTol(self,mintol : float) -> None: 
        """
        Changes the value of "myMinTol"

        Changes the value of "myMinTol"
        """
    def SetModeApprox(self,mode : bool) -> None: 
        """
        Changes the value of "myModeApprox"

        Changes the value of "myModeApprox"
        """
    def SetModeTransfer(self,mode : bool) -> None: 
        """
        Changes the value of "myModeIsTopo"

        Changes the value of "myModeIsTopo"
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "myModel"
        """
    def SetOptimized(self,optimized : bool) -> None: 
        """
        Changes the value of "myContIsOpti"

        Changes the value of "myContIsOpti"
        """
    def SetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the IGESEntity "start".
        """
    def SetSurface(self,theSurface : OCP.Geom.Geom_Surface) -> None: 
        """
        None
        """
    def SetSurfaceCurve(self,ival : int) -> None: 
        """
        Changes the value of "mySurfaceCurve"

        Changes the value of "mySurfaceCurve"
        """
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        Set the value of "myMsgReg"

        Set the value of "myMsgReg"
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def TransferCurveAndSurface(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert of any IGES Curve or Surface Entity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferGeometry(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert the geometry of any IGESEntity. If the transfer has failed, this member return a NullEntity.
        """
    def UpdateMinMaxTol(self) -> None: 
        """
        Sets values of "myMinTol" and "myMaxTol" as follows myMaxTol = Max ("read.maxprecision.val", myEpsGeom * myUnitFactor) myMinTol = Precision::Confusion() Remark: This method is automatically invoked each time the values of "myEpsGeom" or "myUnitFactor" are changed
        """
    @overload
    def __init__(self,eps : float,epsGeom : float,epsCoeff : float,mode : bool,modeapprox : bool,optimized : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IGESToBRep_BasicCurve(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer basic geometric curves entities from IGES to CASCADE. These can be : * Circular arc * Conic arc * Spline curve * BSpline curve * Line * Copious data * Point * Transformation matrix
    """
    def AddShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the entity of the IGESEntity start ( type VertexList or EdgeList).
        """
    def GetContinuity(self) -> int: 
        """
        Returns the value of "myContinuity"

        Returns the value of "myContinuity"
        """
    def GetEpsCoeff(self) -> float: 
        """
        Returns the value of "myEpsCoeff"

        Returns the value of "myEpsCoeff"
        """
    def GetEpsGeom(self) -> float: 
        """
        Returns the value of "myEpsGeom"

        Returns the value of "myEpsGeom"
        """
    def GetEpsilon(self) -> float: 
        """
        Returns the value of "myEps"

        Returns the value of "myEps"
        """
    def GetMaxTol(self) -> float: 
        """
        Returns the value of "myMaxTol"

        Returns the value of "myMaxTol"
        """
    def GetMinTol(self) -> float: 
        """
        Returns the value of "myMinTol"

        Returns the value of "myMinTol"
        """
    def GetModeApprox(self) -> bool: 
        """
        Returns the value of "myModeApprox"

        Returns the value of "myModeApprox"
        """
    def GetModeTransfer(self) -> bool: 
        """
        Returns the value of "myModeIsTopo"

        Returns the value of "myModeIsTopo"
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "myModel"

        Returns the value of "myModel"
        """
    def GetOptimized(self) -> bool: 
        """
        Returns the value of "myContIsOpti"

        Returns the value of "myContIsOpti"
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfer of the IGESEntity "start" contained in "myMap" . (if HasShapeResult is True).

        Returns the numth result of the IGESEntity start (type VertexList or EdgeList) in "myMap". (if NbShapeResult is not null).
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,num : int) -> OCP.TopoDS.TopoDS_Shape: ...
    def GetSurfaceCurve(self) -> int: 
        """
        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d

        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d
        """
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the value of "myMsgReg"

        Returns the value of "myMsgReg"
        """
    def GetUVResolution(self) -> float: 
        """
        None
        """
    def GetUnitFactor(self) -> float: 
        """
        Returns the value of " myUnitFactor"

        Returns the value of " myUnitFactor"
        """
    def HasShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Returns True if start was already treated and has a result in "myMap" else returns False.
        """
    def Init(self) -> None: 
        """
        Initializes the field of the tool CurveAndSurface with default creating values.
        """
    def NbShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> int: 
        """
        Returns the number of shapes results contained in "myMap" for the IGESEntity start ( type VertexList or EdgeList).
        """
    def SendFail(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    def SendMsg(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Information message from the definition of a Msg (Original+Value)

        Records a new Information message from the definition of a Msg (Original+Value)
        """
    def SendWarning(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    def SetContinuity(self,continuity : int) -> None: 
        """
        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2

        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2
        """
    def SetEpsCoeff(self,eps : float) -> None: 
        """
        Changes the value of "myEpsCoeff"

        Changes the value of "myEpsCoeff"
        """
    def SetEpsGeom(self,eps : float) -> None: 
        """
        Changes the value of "myEpsGeom"
        """
    def SetEpsilon(self,eps : float) -> None: 
        """
        Changes the value of "myEps"

        Changes the value of "myEps"
        """
    def SetMaxTol(self,maxtol : float) -> None: 
        """
        Changes the value of "myMaxTol"

        Changes the value of "myMaxTol"
        """
    def SetMinTol(self,mintol : float) -> None: 
        """
        Changes the value of "myMinTol"

        Changes the value of "myMinTol"
        """
    def SetModeApprox(self,mode : bool) -> None: 
        """
        Changes the value of "myModeApprox"

        Changes the value of "myModeApprox"
        """
    def SetModeTransfer(self,mode : bool) -> None: 
        """
        Changes the value of "myModeIsTopo"

        Changes the value of "myModeIsTopo"
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "myModel"
        """
    def SetOptimized(self,optimized : bool) -> None: 
        """
        Changes the value of "myContIsOpti"

        Changes the value of "myContIsOpti"
        """
    def SetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the IGESEntity "start".
        """
    def SetSurface(self,theSurface : OCP.Geom.Geom_Surface) -> None: 
        """
        None
        """
    def SetSurfaceCurve(self,ival : int) -> None: 
        """
        Changes the value of "mySurfaceCurve"

        Changes the value of "mySurfaceCurve"
        """
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        Set the value of "myMsgReg"

        Set the value of "myMsgReg"
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Transfer2dBSplineCurve(self,start : OCP.IGESGeom.IGESGeom_BSplineCurve) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def Transfer2dBasicCurve(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Transfert a IGESEntity which answer True to the member : IGESToBRep::IsBasicCurve(IGESEntity). The IGESEntity must be a curve UV and its associed TRSF must be planar .If this Entity could not be converted, this member returns a NullEntity.
        """
    def Transfer2dCircularArc(self,start : OCP.IGESGeom.IGESGeom_CircularArc) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def Transfer2dConicArc(self,start : OCP.IGESGeom.IGESGeom_ConicArc) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def Transfer2dCopiousData(self,start : OCP.IGESGeom.IGESGeom_CopiousData) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    def Transfer2dLine(self,start : OCP.IGESGeom.IGESGeom_Line) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def Transfer2dSplineCurve(self,start : OCP.IGESGeom.IGESGeom_SplineCurve) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    def TransferBSplineCurve(self,start : OCP.IGESGeom.IGESGeom_BSplineCurve) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def TransferBasicCurve(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.Geom.Geom_Curve: 
        """
        Transfert a IGESEntity which answer True to the member : IGESToBRep::IsBasicCurve(IGESEntity). If this Entity could not be converted, this member returns a NullEntity.
        """
    def TransferCircularArc(self,start : OCP.IGESGeom.IGESGeom_CircularArc) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def TransferConicArc(self,start : OCP.IGESGeom.IGESGeom_ConicArc) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def TransferCopiousData(self,start : OCP.IGESGeom.IGESGeom_CopiousData) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def TransferCurveAndSurface(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert of any IGES Curve or Surface Entity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferGeometry(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert the geometry of any IGESEntity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferLine(self,start : OCP.IGESGeom.IGESGeom_Line) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def TransferSplineCurve(self,start : OCP.IGESGeom.IGESGeom_SplineCurve) -> OCP.Geom.Geom_BSplineCurve: 
        """
        None
        """
    def TransferTransformation(self,start : OCP.IGESGeom.IGESGeom_TransformationMatrix) -> OCP.Geom.Geom_Transformation: 
        """
        None
        """
    def UpdateMinMaxTol(self) -> None: 
        """
        Sets values of "myMinTol" and "myMaxTol" as follows myMaxTol = Max ("read.maxprecision.val", myEpsGeom * myUnitFactor) myMinTol = Precision::Confusion() Remark: This method is automatically invoked each time the values of "myEpsGeom" or "myUnitFactor" are changed
        """
    @overload
    def __init__(self,eps : float,epsGeom : float,epsCoeff : float,mode : bool,modeapprox : bool,optimized : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,CS : IGESToBRep_CurveAndSurface) -> None: ...
    pass
class IGESToBRep_BasicSurface(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer basic geometric surface entities from IGES to CASCADE. These can be : * Spline surface * BSpline surface
    """
    def AddShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the entity of the IGESEntity start ( type VertexList or EdgeList).
        """
    def GetContinuity(self) -> int: 
        """
        Returns the value of "myContinuity"

        Returns the value of "myContinuity"
        """
    def GetEpsCoeff(self) -> float: 
        """
        Returns the value of "myEpsCoeff"

        Returns the value of "myEpsCoeff"
        """
    def GetEpsGeom(self) -> float: 
        """
        Returns the value of "myEpsGeom"

        Returns the value of "myEpsGeom"
        """
    def GetEpsilon(self) -> float: 
        """
        Returns the value of "myEps"

        Returns the value of "myEps"
        """
    def GetMaxTol(self) -> float: 
        """
        Returns the value of "myMaxTol"

        Returns the value of "myMaxTol"
        """
    def GetMinTol(self) -> float: 
        """
        Returns the value of "myMinTol"

        Returns the value of "myMinTol"
        """
    def GetModeApprox(self) -> bool: 
        """
        Returns the value of "myModeApprox"

        Returns the value of "myModeApprox"
        """
    def GetModeTransfer(self) -> bool: 
        """
        Returns the value of "myModeIsTopo"

        Returns the value of "myModeIsTopo"
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "myModel"

        Returns the value of "myModel"
        """
    def GetOptimized(self) -> bool: 
        """
        Returns the value of "myContIsOpti"

        Returns the value of "myContIsOpti"
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfer of the IGESEntity "start" contained in "myMap" . (if HasShapeResult is True).

        Returns the numth result of the IGESEntity start (type VertexList or EdgeList) in "myMap". (if NbShapeResult is not null).
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,num : int) -> OCP.TopoDS.TopoDS_Shape: ...
    def GetSurfaceCurve(self) -> int: 
        """
        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d

        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d
        """
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the value of "myMsgReg"

        Returns the value of "myMsgReg"
        """
    def GetUVResolution(self) -> float: 
        """
        None
        """
    def GetUnitFactor(self) -> float: 
        """
        Returns the value of " myUnitFactor"

        Returns the value of " myUnitFactor"
        """
    def HasShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Returns True if start was already treated and has a result in "myMap" else returns False.
        """
    def Init(self) -> None: 
        """
        Initializes the field of the tool CurveAndSurface with default creating values.
        """
    def NbShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> int: 
        """
        Returns the number of shapes results contained in "myMap" for the IGESEntity start ( type VertexList or EdgeList).
        """
    def SendFail(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    def SendMsg(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Information message from the definition of a Msg (Original+Value)

        Records a new Information message from the definition of a Msg (Original+Value)
        """
    def SendWarning(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    def SetContinuity(self,continuity : int) -> None: 
        """
        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2

        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2
        """
    def SetEpsCoeff(self,eps : float) -> None: 
        """
        Changes the value of "myEpsCoeff"

        Changes the value of "myEpsCoeff"
        """
    def SetEpsGeom(self,eps : float) -> None: 
        """
        Changes the value of "myEpsGeom"
        """
    def SetEpsilon(self,eps : float) -> None: 
        """
        Changes the value of "myEps"

        Changes the value of "myEps"
        """
    def SetMaxTol(self,maxtol : float) -> None: 
        """
        Changes the value of "myMaxTol"

        Changes the value of "myMaxTol"
        """
    def SetMinTol(self,mintol : float) -> None: 
        """
        Changes the value of "myMinTol"

        Changes the value of "myMinTol"
        """
    def SetModeApprox(self,mode : bool) -> None: 
        """
        Changes the value of "myModeApprox"

        Changes the value of "myModeApprox"
        """
    def SetModeTransfer(self,mode : bool) -> None: 
        """
        Changes the value of "myModeIsTopo"

        Changes the value of "myModeIsTopo"
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "myModel"
        """
    def SetOptimized(self,optimized : bool) -> None: 
        """
        Changes the value of "myContIsOpti"

        Changes the value of "myContIsOpti"
        """
    def SetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the IGESEntity "start".
        """
    def SetSurface(self,theSurface : OCP.Geom.Geom_Surface) -> None: 
        """
        None
        """
    def SetSurfaceCurve(self,ival : int) -> None: 
        """
        Changes the value of "mySurfaceCurve"

        Changes the value of "mySurfaceCurve"
        """
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        Set the value of "myMsgReg"

        Set the value of "myMsgReg"
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def TransferBSplineSurface(self,start : OCP.IGESGeom.IGESGeom_BSplineSurface) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Returns BSplineSurface from Geom if the transfer has succeeded.
        """
    def TransferBasicSurface(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.Geom.Geom_Surface: 
        """
        Returns Surface from Geom if the last transfer has succeeded.
        """
    def TransferCurveAndSurface(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert of any IGES Curve or Surface Entity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferGeometry(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert the geometry of any IGESEntity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferPlaneSurface(self,start : OCP.IGESSolid.IGESSolid_PlaneSurface) -> OCP.Geom.Geom_Plane: 
        """
        Returns Plane from Geom if the transfer has succeeded.
        """
    def TransferRigthConicalSurface(self,start : OCP.IGESSolid.IGESSolid_ConicalSurface) -> OCP.Geom.Geom_ConicalSurface: 
        """
        Returns ConicalSurface from Geom if the transfer has succeeded.
        """
    def TransferRigthCylindricalSurface(self,start : OCP.IGESSolid.IGESSolid_CylindricalSurface) -> OCP.Geom.Geom_CylindricalSurface: 
        """
        Returns CylindricalSurface from Geom if the transfer has succeeded.
        """
    def TransferSphericalSurface(self,start : OCP.IGESSolid.IGESSolid_SphericalSurface) -> OCP.Geom.Geom_SphericalSurface: 
        """
        Returns SphericalSurface from Geom if the transfer has succeeded.
        """
    def TransferSplineSurface(self,start : OCP.IGESGeom.IGESGeom_SplineSurface) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Returns BSplineSurface from Geom if the transfer has succeeded.
        """
    def TransferToroidalSurface(self,start : OCP.IGESSolid.IGESSolid_ToroidalSurface) -> OCP.Geom.Geom_ToroidalSurface: 
        """
        Returns SphericalSurface from Geom if the transfer has succeeded.
        """
    def UpdateMinMaxTol(self) -> None: 
        """
        Sets values of "myMinTol" and "myMaxTol" as follows myMaxTol = Max ("read.maxprecision.val", myEpsGeom * myUnitFactor) myMinTol = Precision::Confusion() Remark: This method is automatically invoked each time the values of "myEpsGeom" or "myUnitFactor" are changed
        """
    @overload
    def __init__(self,eps : float,epsGeom : float,epsCoeff : float,mode : bool,modeapprox : bool,optimized : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,CS : IGESToBRep_CurveAndSurface) -> None: ...
    pass
class IGESToBRep_BRepEntity(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer BRep entities ( VertexList 502, EdgeList 504, Loop 508, Face 510, Shell 514, ManifoldSolid 186) from IGES to CASCADE.
    """
    def AddShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the entity of the IGESEntity start ( type VertexList or EdgeList).
        """
    def GetContinuity(self) -> int: 
        """
        Returns the value of "myContinuity"

        Returns the value of "myContinuity"
        """
    def GetEpsCoeff(self) -> float: 
        """
        Returns the value of "myEpsCoeff"

        Returns the value of "myEpsCoeff"
        """
    def GetEpsGeom(self) -> float: 
        """
        Returns the value of "myEpsGeom"

        Returns the value of "myEpsGeom"
        """
    def GetEpsilon(self) -> float: 
        """
        Returns the value of "myEps"

        Returns the value of "myEps"
        """
    def GetMaxTol(self) -> float: 
        """
        Returns the value of "myMaxTol"

        Returns the value of "myMaxTol"
        """
    def GetMinTol(self) -> float: 
        """
        Returns the value of "myMinTol"

        Returns the value of "myMinTol"
        """
    def GetModeApprox(self) -> bool: 
        """
        Returns the value of "myModeApprox"

        Returns the value of "myModeApprox"
        """
    def GetModeTransfer(self) -> bool: 
        """
        Returns the value of "myModeIsTopo"

        Returns the value of "myModeIsTopo"
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "myModel"

        Returns the value of "myModel"
        """
    def GetOptimized(self) -> bool: 
        """
        Returns the value of "myContIsOpti"

        Returns the value of "myContIsOpti"
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfer of the IGESEntity "start" contained in "myMap" . (if HasShapeResult is True).

        Returns the numth result of the IGESEntity start (type VertexList or EdgeList) in "myMap". (if NbShapeResult is not null).
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,num : int) -> OCP.TopoDS.TopoDS_Shape: ...
    def GetSurfaceCurve(self) -> int: 
        """
        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d

        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d
        """
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the value of "myMsgReg"

        Returns the value of "myMsgReg"
        """
    def GetUVResolution(self) -> float: 
        """
        None
        """
    def GetUnitFactor(self) -> float: 
        """
        Returns the value of " myUnitFactor"

        Returns the value of " myUnitFactor"
        """
    def HasShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Returns True if start was already treated and has a result in "myMap" else returns False.
        """
    def Init(self) -> None: 
        """
        Initializes the field of the tool CurveAndSurface with default creating values.
        """
    def NbShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> int: 
        """
        Returns the number of shapes results contained in "myMap" for the IGESEntity start ( type VertexList or EdgeList).
        """
    def SendFail(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    def SendMsg(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Information message from the definition of a Msg (Original+Value)

        Records a new Information message from the definition of a Msg (Original+Value)
        """
    def SendWarning(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    def SetContinuity(self,continuity : int) -> None: 
        """
        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2

        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2
        """
    def SetEpsCoeff(self,eps : float) -> None: 
        """
        Changes the value of "myEpsCoeff"

        Changes the value of "myEpsCoeff"
        """
    def SetEpsGeom(self,eps : float) -> None: 
        """
        Changes the value of "myEpsGeom"
        """
    def SetEpsilon(self,eps : float) -> None: 
        """
        Changes the value of "myEps"

        Changes the value of "myEps"
        """
    def SetMaxTol(self,maxtol : float) -> None: 
        """
        Changes the value of "myMaxTol"

        Changes the value of "myMaxTol"
        """
    def SetMinTol(self,mintol : float) -> None: 
        """
        Changes the value of "myMinTol"

        Changes the value of "myMinTol"
        """
    def SetModeApprox(self,mode : bool) -> None: 
        """
        Changes the value of "myModeApprox"

        Changes the value of "myModeApprox"
        """
    def SetModeTransfer(self,mode : bool) -> None: 
        """
        Changes the value of "myModeIsTopo"

        Changes the value of "myModeIsTopo"
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "myModel"
        """
    def SetOptimized(self,optimized : bool) -> None: 
        """
        Changes the value of "myContIsOpti"

        Changes the value of "myContIsOpti"
        """
    def SetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the IGESEntity "start".
        """
    def SetSurface(self,theSurface : OCP.Geom.Geom_Surface) -> None: 
        """
        None
        """
    def SetSurfaceCurve(self,ival : int) -> None: 
        """
        Changes the value of "mySurfaceCurve"

        Changes the value of "mySurfaceCurve"
        """
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        Set the value of "myMsgReg"

        Set the value of "myMsgReg"
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def TransferBRepEntity(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Transfer the BRepEntity" : Face, Shell or ManifoldSolid.
        """
    def TransferCurveAndSurface(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert of any IGES Curve or Surface Entity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferEdge(self,start : OCP.IGESSolid.IGESSolid_EdgeList,index : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Transfer the entity number "index" of the EdgeList "start".
        """
    def TransferFace(self,start : OCP.IGESSolid.IGESSolid_Face) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Transfer the Face Entity
        """
    def TransferGeometry(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert the geometry of any IGESEntity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferLoop(self,start : OCP.IGESSolid.IGESSolid_Loop,Face : OCP.TopoDS.TopoDS_Face,trans : OCP.gp.gp_Trsf2d,uFact : float) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Transfer the Loop Entity
        """
    def TransferManifoldSolid(self,start : OCP.IGESSolid.IGESSolid_ManifoldSolid,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Transfer the ManifoldSolid Entity
        """
    def TransferShell(self,start : OCP.IGESSolid.IGESSolid_Shell,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Transfer the Shell Entity
        """
    def TransferVertex(self,start : OCP.IGESSolid.IGESSolid_VertexList,index : int) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        Transfer the entity number "index" of the VertexList "start"
        """
    def UpdateMinMaxTol(self) -> None: 
        """
        Sets values of "myMinTol" and "myMaxTol" as follows myMaxTol = Max ("read.maxprecision.val", myEpsGeom * myUnitFactor) myMinTol = Precision::Confusion() Remark: This method is automatically invoked each time the values of "myEpsGeom" or "myUnitFactor" are changed
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,eps : float,epsGeom : float,epsCoeff : float,mode : bool,modeapprox : bool,optimized : bool) -> None: ...
    @overload
    def __init__(self,CS : IGESToBRep_CurveAndSurface) -> None: ...
    pass
class IGESToBRep_IGESBoundary(OCP.Standard.Standard_Transient):
    """
    This class is intended to translate IGES boundary entity (142-CurveOnSurface, 141-Boundary or 508-Loop) into the wire. Methods Transfer are virtual and are redefined in Advanced Data Exchange to optimize the translation and take into account advanced parameters.This class is intended to translate IGES boundary entity (142-CurveOnSurface, 141-Boundary or 508-Loop) into the wire. Methods Transfer are virtual and are redefined in Advanced Data Exchange to optimize the translation and take into account advanced parameters.This class is intended to translate IGES boundary entity (142-CurveOnSurface, 141-Boundary or 508-Loop) into the wire. Methods Transfer are virtual and are redefined in Advanced Data Exchange to optimize the translation and take into account advanced parameters.
    """
    def Check(self,result : bool,checkclosure : bool,okCurve3d : bool,okCurve2d : bool) -> None: 
        """
        Checks result of translation of IGES boundary entities (types 141, 142 or 508). Checks consistency of 2D and 3D representations and keeps only one if they are inconsistent. <result>: result of translation (returned by Transfer), <checkclosure>: False for 142 without parent 144 entity, otherwise True, <okCurve3d>, <okCurve2d>: those returned by Transfer.
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
    def Init(self,CS : IGESToBRep_CurveAndSurface,entity : OCP.IGESData.IGESData_IGESEntity,face : OCP.TopoDS.TopoDS_Face,trans : OCP.gp.gp_Trsf2d,uFact : float,filepreference : int) -> None: 
        """
        Inits the object with parameters common for all types of IGES boundaries. <CS>: object to be used for retrieving translation parameters and sending messages, <entity>: boundary entity to be processed, <face>, <trans>, <uFact>: as for IGESToBRep_TopoCurve <filepreference>: preferred representation (2 or 3) given in the IGES file
        """
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transfer(self,okCurve : bool,okCurve3d : bool,okCurve2d : bool,curve3d : OCP.IGESData.IGESData_IGESEntity,toreverse3d : bool,curves2d : OCP.IGESData.IGESData_HArray1OfIGESEntity,number : int) -> bool: 
        """
        Translates 141 and 142 entities. Returns True if the curve has been successfully translated, otherwise returns False. <okCurve..>: flags that indicate whether corresponding representation has been successfully translated (must be set to True before first call), <curve3d>: model space curve for 142 and current model space curve for 141, <toreverse3d>: False for 142 and current orientation flag for 141, <curves2d>: 1 parameter space curve for 142 or list of them for current model space curves for 141, <number>: 1 for 142 and rank number of model space curve for 141.

        Translates 508 entity. Returns True if the curve has been successfully translated, otherwise returns False. Input object IGESBoundary must be created and initialized before. <okCurve..>: flags that indicate whether corresponding representation has been successfully translated (must be set to True before first call), <curve3d>: result of translation of current edge, <curves2d>: list of parameter space curves for edge, <toreverse2d>: orientation flag of current edge in respect to its model space curve, <number>: rank number of edge, <lsewd>: returns the result of translation of current edge.
        """
    @overload
    def Transfer(self,okCurve : bool,okCurve3d : bool,okCurve2d : bool,curve3d : OCP.ShapeExtend.ShapeExtend_WireData,curves2d : OCP.IGESData.IGESData_HArray1OfIGESEntity,toreverse2d : bool,number : int,lsewd : OCP.ShapeExtend.ShapeExtend_WireData) -> bool: ...
    def WireData(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        Returns the resulting wire

        Returns the resulting wire
        """
    def WireData2d(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        Returns the wire from 2D curves (edges contain pcurves only)

        Returns the wire from 2D curves (edges contain pcurves only)
        """
    def WireData3d(self) -> OCP.ShapeExtend.ShapeExtend_WireData: 
        """
        Returns the wire from 3D curves (edges contain 3D curves and may contain pcurves)

        Returns the wire from 3D curves (edges contain 3D curves and may contain pcurves)
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,CS : IGESToBRep_CurveAndSurface) -> None: ...
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
class IGESToBRep_Reader():
    """
    A simple way to read geometric IGES data. Encapsulates reading file and calling transfer tools
    """
    def Actor(self) -> IGESToBRep_Actor: 
        """
        Returns "theActor"
        """
    def Check(self,withprint : bool) -> bool: 
        """
        Checks the IGES file that was loaded into memory. Displays error messages in the default message file if withprint is true. Returns True if no fail message was found and False if there was at least one fail message.
        """
    def Clear(self) -> None: 
        """
        Clears the results between two translation operations.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the LAST Transfer/TransferRoots was a success
        """
    def LoadFile(self,filename : str) -> int: 
        """
        Loads a Model from a file.Returns 0 if success. returns 1 if the file could not be opened, returns -1 if an error occurred while the file was being loaded.
        """
    def Model(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the Model to be worked on.
        """
    def NbShapes(self) -> int: 
        """
        Returns the number of shapes produced by the translation.
        """
    def OneShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns all of the results in a single shape which is: - a null shape if there are no results, - a shape if there is one result, - a compound containing the resulting shapes if there are several.
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Specifies a Model to work on Also clears the result and Done status, sets TransientProcess
        """
    def SetTransientProcess(self,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        Allows to set an already defined TransientProcess (to be called after LoadFile or SetModel)
        """
    def Shape(self,num : int=1) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the num the resulting shape in a translation operation.
        """
    def Transfer(self,num : int,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Transfers an Entity given its rank in the Model (Root or not) Returns True if it is recognized as Geom-Topol. (But it can have failed : see IsDone)
        """
    def TransferRoots(self,onlyvisible : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Translates root entities in an IGES file. Standard_True is the default value and means that only visible root entities are translated. Standard_False translates all of the roots (visible and invisible).
        """
    def TransientProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the TransientProcess
        """
    def UsedTolerance(self) -> float: 
        """
        Returns the Tolerance which has been actually used, converted in millimeters (either that from File or that from Session, according the mode)
        """
    def __init__(self) -> None: ...
    pass
class IGESToBRep_ToolContainer(OCP.Standard.Standard_Transient):
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
    def IGESBoundary(self) -> IGESToBRep_IGESBoundary: 
        """
        Returns IGESToBRep_IGESBoundary
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
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
class IGESToBRep_TopoCurve(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer topologic curves entities from IGES to CASCADE.
    """
    def AddShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the entity of the IGESEntity start ( type VertexList or EdgeList).
        """
    def Approx2dBSplineCurve(self,start : OCP.Geom2d.Geom2d_BSplineCurve) -> None: 
        """
        None
        """
    def ApproxBSplineCurve(self,start : OCP.Geom.Geom_BSplineCurve) -> None: 
        """
        None
        """
    def BadCase(self) -> bool: 
        """
        Returns TheBadCase flag
        """
    def Curve(self,num : int=1) -> OCP.Geom.Geom_Curve: 
        """
        Returns a Curve given its rank, by default the first one (null Curvee if out of range) in "TheCurves"
        """
    def Curve2d(self,num : int=1) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns a Curve given its rank, by default the first one (null Curvee if out of range) in "TheCurves2d"
        """
    def GetContinuity(self) -> int: 
        """
        Returns the value of "myContinuity"

        Returns the value of "myContinuity"
        """
    def GetEpsCoeff(self) -> float: 
        """
        Returns the value of "myEpsCoeff"

        Returns the value of "myEpsCoeff"
        """
    def GetEpsGeom(self) -> float: 
        """
        Returns the value of "myEpsGeom"

        Returns the value of "myEpsGeom"
        """
    def GetEpsilon(self) -> float: 
        """
        Returns the value of "myEps"

        Returns the value of "myEps"
        """
    def GetMaxTol(self) -> float: 
        """
        Returns the value of "myMaxTol"

        Returns the value of "myMaxTol"
        """
    def GetMinTol(self) -> float: 
        """
        Returns the value of "myMinTol"

        Returns the value of "myMinTol"
        """
    def GetModeApprox(self) -> bool: 
        """
        Returns the value of "myModeApprox"

        Returns the value of "myModeApprox"
        """
    def GetModeTransfer(self) -> bool: 
        """
        Returns the value of "myModeIsTopo"

        Returns the value of "myModeIsTopo"
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "myModel"

        Returns the value of "myModel"
        """
    def GetOptimized(self) -> bool: 
        """
        Returns the value of "myContIsOpti"

        Returns the value of "myContIsOpti"
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfer of the IGESEntity "start" contained in "myMap" . (if HasShapeResult is True).

        Returns the numth result of the IGESEntity start (type VertexList or EdgeList) in "myMap". (if NbShapeResult is not null).
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,num : int) -> OCP.TopoDS.TopoDS_Shape: ...
    def GetSurfaceCurve(self) -> int: 
        """
        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d

        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d
        """
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the value of "myMsgReg"

        Returns the value of "myMsgReg"
        """
    def GetUVResolution(self) -> float: 
        """
        None
        """
    def GetUnitFactor(self) -> float: 
        """
        Returns the value of " myUnitFactor"

        Returns the value of " myUnitFactor"
        """
    def HasShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Returns True if start was already treated and has a result in "myMap" else returns False.
        """
    def Init(self) -> None: 
        """
        Initializes the field of the tool CurveAndSurface with default creating values.
        """
    def NbCurves(self) -> int: 
        """
        Returns the count of Curves in "TheCurves"
        """
    def NbCurves2d(self) -> int: 
        """
        Returns the count of Curves in "TheCurves2d"
        """
    def NbShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> int: 
        """
        Returns the number of shapes results contained in "myMap" for the IGESEntity start ( type VertexList or EdgeList).
        """
    def SendFail(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    def SendMsg(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Information message from the definition of a Msg (Original+Value)

        Records a new Information message from the definition of a Msg (Original+Value)
        """
    def SendWarning(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    def SetBadCase(self,value : bool) -> None: 
        """
        Sets TheBadCase flag
        """
    def SetContinuity(self,continuity : int) -> None: 
        """
        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2

        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2
        """
    def SetEpsCoeff(self,eps : float) -> None: 
        """
        Changes the value of "myEpsCoeff"

        Changes the value of "myEpsCoeff"
        """
    def SetEpsGeom(self,eps : float) -> None: 
        """
        Changes the value of "myEpsGeom"
        """
    def SetEpsilon(self,eps : float) -> None: 
        """
        Changes the value of "myEps"

        Changes the value of "myEps"
        """
    def SetMaxTol(self,maxtol : float) -> None: 
        """
        Changes the value of "myMaxTol"

        Changes the value of "myMaxTol"
        """
    def SetMinTol(self,mintol : float) -> None: 
        """
        Changes the value of "myMinTol"

        Changes the value of "myMinTol"
        """
    def SetModeApprox(self,mode : bool) -> None: 
        """
        Changes the value of "myModeApprox"

        Changes the value of "myModeApprox"
        """
    def SetModeTransfer(self,mode : bool) -> None: 
        """
        Changes the value of "myModeIsTopo"

        Changes the value of "myModeIsTopo"
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "myModel"
        """
    def SetOptimized(self,optimized : bool) -> None: 
        """
        Changes the value of "myContIsOpti"

        Changes the value of "myContIsOpti"
        """
    def SetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the IGESEntity "start".
        """
    def SetSurface(self,theSurface : OCP.Geom.Geom_Surface) -> None: 
        """
        None
        """
    def SetSurfaceCurve(self,ival : int) -> None: 
        """
        Changes the value of "mySurfaceCurve"

        Changes the value of "mySurfaceCurve"
        """
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        Set the value of "myMsgReg"

        Set the value of "myMsgReg"
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Transfer2dCompositeCurve(self,start : OCP.IGESGeom.IGESGeom_CompositeCurve,face : OCP.TopoDS.TopoDS_Face,trans : OCP.gp.gp_Trsf2d,uFact : float) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Transfer2dOffsetCurve(self,start : OCP.IGESGeom.IGESGeom_OffsetCurve,face : OCP.TopoDS.TopoDS_Face,trans : OCP.gp.gp_Trsf2d,uFact : float) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Transfer2dPoint(self,start : OCP.IGESGeom.IGESGeom_Point) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def Transfer2dTopoBasicCurve(self,start : OCP.IGESData.IGESData_IGESEntity,face : OCP.TopoDS.TopoDS_Face,trans : OCP.gp.gp_Trsf2d,uFact : float) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Transfer2dTopoCurve(self,start : OCP.IGESData.IGESData_IGESEntity,face : OCP.TopoDS.TopoDS_Face,trans : OCP.gp.gp_Trsf2d,uFact : float) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferBoundary(self,start : OCP.IGESGeom.IGESGeom_Boundary) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferBoundaryOnFace(self,face : OCP.TopoDS.TopoDS_Face,start : OCP.IGESGeom.IGESGeom_Boundary,trans : OCP.gp.gp_Trsf2d,uFact : float) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Transfers a Boundary directly on a face to trim it.
        """
    def TransferCompositeCurve(self,start : OCP.IGESGeom.IGESGeom_CompositeCurve) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferCurveAndSurface(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert of any IGES Curve or Surface Entity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferCurveOnFace(self,face : OCP.TopoDS.TopoDS_Face,start : OCP.IGESGeom.IGESGeom_CurveOnSurface,trans : OCP.gp.gp_Trsf2d,uFact : float,IsCurv : bool) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Transfers a CurveOnSurface directly on a face to trim it. The CurveOnSurface have to be defined Outer or Inner.
        """
    def TransferCurveOnSurface(self,start : OCP.IGESGeom.IGESGeom_CurveOnSurface) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferGeometry(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert the geometry of any IGESEntity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferOffsetCurve(self,start : OCP.IGESGeom.IGESGeom_OffsetCurve) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferPoint(self,start : OCP.IGESGeom.IGESGeom_Point) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    def TransferTopoBasicCurve(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferTopoCurve(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def UpdateMinMaxTol(self) -> None: 
        """
        Sets values of "myMinTol" and "myMaxTol" as follows myMaxTol = Max ("read.maxprecision.val", myEpsGeom * myUnitFactor) myMinTol = Precision::Confusion() Remark: This method is automatically invoked each time the values of "myEpsGeom" or "myUnitFactor" are changed
        """
    @overload
    def __init__(self,CS : IGESToBRep_CurveAndSurface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,eps : float,epsGeom : float,epsCoeff : float,mode : bool,modeapprox : bool,optimized : bool) -> None: ...
    @overload
    def __init__(self,CS : IGESToBRep_TopoCurve) -> None: ...
    pass
class IGESToBRep_TopoSurface(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer topologic surfaces entities from IGES to CASCADE.
    """
    def AddShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the entity of the IGESEntity start ( type VertexList or EdgeList).
        """
    def GetContinuity(self) -> int: 
        """
        Returns the value of "myContinuity"

        Returns the value of "myContinuity"
        """
    def GetEpsCoeff(self) -> float: 
        """
        Returns the value of "myEpsCoeff"

        Returns the value of "myEpsCoeff"
        """
    def GetEpsGeom(self) -> float: 
        """
        Returns the value of "myEpsGeom"

        Returns the value of "myEpsGeom"
        """
    def GetEpsilon(self) -> float: 
        """
        Returns the value of "myEps"

        Returns the value of "myEps"
        """
    def GetMaxTol(self) -> float: 
        """
        Returns the value of "myMaxTol"

        Returns the value of "myMaxTol"
        """
    def GetMinTol(self) -> float: 
        """
        Returns the value of "myMinTol"

        Returns the value of "myMinTol"
        """
    def GetModeApprox(self) -> bool: 
        """
        Returns the value of "myModeApprox"

        Returns the value of "myModeApprox"
        """
    def GetModeTransfer(self) -> bool: 
        """
        Returns the value of "myModeIsTopo"

        Returns the value of "myModeIsTopo"
        """
    def GetModel(self) -> OCP.IGESData.IGESData_IGESModel: 
        """
        Returns the value of "myModel"

        Returns the value of "myModel"
        """
    def GetOptimized(self) -> bool: 
        """
        Returns the value of "myContIsOpti"

        Returns the value of "myContIsOpti"
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfer of the IGESEntity "start" contained in "myMap" . (if HasShapeResult is True).

        Returns the numth result of the IGESEntity start (type VertexList or EdgeList) in "myMap". (if NbShapeResult is not null).
        """
    @overload
    def GetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,num : int) -> OCP.TopoDS.TopoDS_Shape: ...
    def GetSurfaceCurve(self) -> int: 
        """
        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d

        Returns the value of " mySurfaceCurve" 0 = value in file , 2 = kepp 2d and compute 3d 3 = keep 3d and compute 2d
        """
    def GetTransferProcess(self) -> OCP.Transfer.Transfer_TransientProcess: 
        """
        Returns the value of "myMsgReg"

        Returns the value of "myMsgReg"
        """
    def GetUVResolution(self) -> float: 
        """
        None
        """
    def GetUnitFactor(self) -> float: 
        """
        Returns the value of " myUnitFactor"

        Returns the value of " myUnitFactor"
        """
    def HasShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> bool: 
        """
        Returns True if start was already treated and has a result in "myMap" else returns False.
        """
    def Init(self) -> None: 
        """
        Initializes the field of the tool CurveAndSurface with default creating values.
        """
    def NbShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity) -> int: 
        """
        Returns the number of shapes results contained in "myMap" for the IGESEntity start ( type VertexList or EdgeList).
        """
    def ParamSurface(self,start : OCP.IGESData.IGESData_IGESEntity,trans : OCP.gp.gp_Trsf2d,uFact : float) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def SendFail(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Fail message

        Records a new Fail message
        """
    def SendMsg(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Information message from the definition of a Msg (Original+Value)

        Records a new Information message from the definition of a Msg (Original+Value)
        """
    def SendWarning(self,start : OCP.IGESData.IGESData_IGESEntity,amsg : OCP.Message.Message_Msg) -> None: 
        """
        Records a new Warning message

        Records a new Warning message
        """
    def SetContinuity(self,continuity : int) -> None: 
        """
        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2

        Changes the value of "myContinuity" if continuity = 0 do nothing else if continuity = 1 try C1 if continuity = 2 try C2
        """
    def SetEpsCoeff(self,eps : float) -> None: 
        """
        Changes the value of "myEpsCoeff"

        Changes the value of "myEpsCoeff"
        """
    def SetEpsGeom(self,eps : float) -> None: 
        """
        Changes the value of "myEpsGeom"
        """
    def SetEpsilon(self,eps : float) -> None: 
        """
        Changes the value of "myEps"

        Changes the value of "myEps"
        """
    def SetMaxTol(self,maxtol : float) -> None: 
        """
        Changes the value of "myMaxTol"

        Changes the value of "myMaxTol"
        """
    def SetMinTol(self,mintol : float) -> None: 
        """
        Changes the value of "myMinTol"

        Changes the value of "myMinTol"
        """
    def SetModeApprox(self,mode : bool) -> None: 
        """
        Changes the value of "myModeApprox"

        Changes the value of "myModeApprox"
        """
    def SetModeTransfer(self,mode : bool) -> None: 
        """
        Changes the value of "myModeIsTopo"

        Changes the value of "myModeIsTopo"
        """
    def SetModel(self,model : OCP.IGESData.IGESData_IGESModel) -> None: 
        """
        Set the value of "myModel"
        """
    def SetOptimized(self,optimized : bool) -> None: 
        """
        Changes the value of "myContIsOpti"

        Changes the value of "myContIsOpti"
        """
    def SetShapeResult(self,start : OCP.IGESData.IGESData_IGESEntity,result : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        set in "myMap" the result of the transfer of the IGESEntity "start".
        """
    def SetSurface(self,theSurface : OCP.Geom.Geom_Surface) -> None: 
        """
        None
        """
    def SetSurfaceCurve(self,ival : int) -> None: 
        """
        Changes the value of "mySurfaceCurve"

        Changes the value of "mySurfaceCurve"
        """
    def SetTransferProcess(self,TP : OCP.Transfer.Transfer_TransientProcess) -> None: 
        """
        Set the value of "myMsgReg"

        Set the value of "myMsgReg"
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def TransferBoundedSurface(self,start : OCP.IGESGeom.IGESGeom_BoundedSurface) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferCurveAndSurface(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert of any IGES Curve or Surface Entity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferGeometry(self,start : OCP.IGESData.IGESData_IGESEntity,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of the transfert the geometry of any IGESEntity. If the transfer has failed, this member return a NullEntity.
        """
    def TransferOffsetSurface(self,start : OCP.IGESGeom.IGESGeom_OffsetSurface) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferPerforate(self,start : OCP.IGESBasic.IGESBasic_SingleParent) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferPlane(self,start : OCP.IGESGeom.IGESGeom_Plane) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferRuledSurface(self,start : OCP.IGESGeom.IGESGeom_RuledSurface) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferSurfaceOfRevolution(self,start : OCP.IGESGeom.IGESGeom_SurfaceOfRevolution) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferTabulatedCylinder(self,start : OCP.IGESGeom.IGESGeom_TabulatedCylinder) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferTopoBasicSurface(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferTopoSurface(self,start : OCP.IGESData.IGESData_IGESEntity) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def TransferTrimmedSurface(self,start : OCP.IGESGeom.IGESGeom_TrimmedSurface) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def UpdateMinMaxTol(self) -> None: 
        """
        Sets values of "myMinTol" and "myMaxTol" as follows myMaxTol = Max ("read.maxprecision.val", myEpsGeom * myUnitFactor) myMinTol = Precision::Confusion() Remark: This method is automatically invoked each time the values of "myEpsGeom" or "myUnitFactor" are changed
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,eps : float,epsGeom : float,epsCoeff : float,mode : bool,modeapprox : bool,optimized : bool) -> None: ...
    @overload
    def __init__(self,CS : IGESToBRep_CurveAndSurface) -> None: ...
    pass
