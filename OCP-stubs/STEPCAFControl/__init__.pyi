import OCP.STEPCAFControl
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IFSelect
import OCP.TopoDS
import OCP.TDocStd
import OCP.TCollection
import OCP.StepBasic
import OCP.Interface
import OCP.Standard
import OCP.Transfer
import OCP.StepRepr
import OCP.TColStd
import OCP.StepGeom
import OCP.STEPControl
import OCP.NCollection
import OCP.StepDimTol
import OCP.XCAFDoc
import OCP.TDF
import OCP.STEPConstruct
import OCP.XCAFDimTolObjects
import OCP.DE
import io
import OCP.XSControl
import OCP.StepVisual
import OCP.StepShape
__all__  = [
"STEPCAFControl_ActorWrite",
"STEPCAFControl_ConfigurationNode",
"STEPCAFControl_Controller",
"STEPCAFControl_DataMapOfLabelShape",
"STEPCAFControl_ExternFile",
"STEPCAFControl_GDTProperty",
"STEPCAFControl_Provider",
"STEPCAFControl_Reader",
"STEPCAFControl_Writer"
]
class STEPCAFControl_ActorWrite(OCP.STEPControl.STEPControl_ActorWrite, OCP.Transfer.Transfer_ActorOfFinderProcess, OCP.Transfer.Transfer_ActorOfProcessForFinder, OCP.Standard.Standard_Transient):
    """
    Extends ActorWrite from STEPControl by analysis of whether shape is assembly (based on information from DECAF)Extends ActorWrite from STEPControl by analysis of whether shape is assembly (based on information from DECAF)Extends ActorWrite from STEPControl by analysis of whether shape is assembly (based on information from DECAF)
    """
    def ClearMap(self) -> None: 
        """
        Clears map of shapes registered as assemblies
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
    def GroupMode(self) -> int: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAssembly(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Check whether shape S is assembly Returns True if shape is registered in assemblies map
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
    def IsLast(self) -> bool: 
        """
        Returns the Last status (see SetLast).
        """
    def Mode(self) -> OCP.STEPControl.STEPControl_StepModelType: 
        """
        None
        """
    def Next(self) -> OCP.Transfer.Transfer_ActorOfProcessForFinder: 
        """
        Returns the Actor defined as Next, or a Null Handle
        """
    def NullResult(self) -> OCP.Transfer.Transfer_Binder: 
        """
        Returns a Binder for No Result, i.e. a Null Handle
        """
    def Recognize(self,start : OCP.Transfer.Transfer_Finder) -> bool: 
        """
        None
        """
    def RegisterAssembly(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Registers shape to be written as assembly The shape should be TopoDS_Compound (else does nothing)
        """
    def SetGroupMode(self,mode : int) -> None: 
        """
        None
        """
    def SetLast(self,mode : bool=True) -> None: 
        """
        If <mode> is True, commands an Actor to be set at the end of the list of Actors (see SetNext) If it is False (creation default), each add Actor is set at the beginning of the list This allows to define default Actors (which are Last)
        """
    def SetMode(self,M : OCP.STEPControl.STEPControl_StepModelType) -> None: 
        """
        None
        """
    def SetNext(self,next : OCP.Transfer.Transfer_ActorOfProcessForFinder) -> None: 
        """
        Defines a Next Actor : it can then be asked to work if <me> produces no result for a given type of Object. If Next is already set and is not "Last", calls SetNext on it. If Next defined and "Last", the new actor is added before it in the list
        """
    def SetStdMode(self,stdmode : bool=True) -> None: 
        """
        Set standard mode of work In standard mode Actor (default) behaves exactly as its ancestor, also map is cleared
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transfer(self,start : OCP.Transfer.Transfer_Finder,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferCompound(self,start : OCP.Transfer.Transfer_Finder,SDR : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,FP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferShape(self,start : OCP.Transfer.Transfer_Finder,SDR : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,FP : OCP.Transfer.Transfer_FinderProcess,shapeGroup : OCP.TopTools.TopTools_HSequenceOfShape=None,isManifold : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferSubShape(self,start : OCP.Transfer.Transfer_Finder,SDR : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,AX1 : OCP.StepGeom.StepGeom_Axis2Placement3d,FP : OCP.Transfer.Transfer_FinderProcess,shapeGroup : OCP.TopTools.TopTools_HSequenceOfShape=None,isManifold : bool=True,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransferTransient(self,start : OCP.Standard.Standard_Transient,TP : OCP.Transfer.Transfer_FinderProcess,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def Transferring(self,start : OCP.Transfer.Transfer_Finder,TP : OCP.Transfer.Transfer_ProcessForFinder,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Transfer.Transfer_Binder: 
        """
        None
        """
    def TransientResult(self,res : OCP.Standard.Standard_Transient) -> OCP.Transfer.Transfer_SimpleBinderOfTransient: 
        """
        Prepares and Returns a Binder for a Transient Result Returns a Null Handle if <res> is itself Null
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
    def ModeTrans(self) -> int:
        """
        Returns the Transfer Mode, modifiable

        :type: int
        """
    @ModeTrans.setter
    def ModeTrans(self, arg1: int) -> None:
        """
        Returns the Transfer Mode, modifiable
        """
    pass
class STEPCAFControl_ConfigurationNode(OCP.DE.DE_ConfigurationNode, OCP.Standard.Standard_Transient):
    """
    The purpose of this class is to configure the transfer process for STEP format Stores the necessary settings for STEPCAFControl_Provider. Configures and creates special provider to transfer STEP files.
    """
    class AngleUnitMode_e():
        """
        None

        Members:

          AngleUnitMode_File

          AngleUnitMode_Rad

          AngleUnitMode_Deg
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        AngleUnitMode_Deg: OCP.STEPCAFControl.AngleUnitMode_e # value = <AngleUnitMode_e.AngleUnitMode_Deg: 2>
        AngleUnitMode_File: OCP.STEPCAFControl.AngleUnitMode_e # value = <AngleUnitMode_e.AngleUnitMode_File: 0>
        AngleUnitMode_Rad: OCP.STEPCAFControl.AngleUnitMode_e # value = <AngleUnitMode_e.AngleUnitMode_Rad: 1>
        __entries: dict # value = {'AngleUnitMode_File': (<AngleUnitMode_e.AngleUnitMode_File: 0>, None), 'AngleUnitMode_Rad': (<AngleUnitMode_e.AngleUnitMode_Rad: 1>, None), 'AngleUnitMode_Deg': (<AngleUnitMode_e.AngleUnitMode_Deg: 2>, None)}
        __members__: dict # value = {'AngleUnitMode_File': <AngleUnitMode_e.AngleUnitMode_File: 0>, 'AngleUnitMode_Rad': <AngleUnitMode_e.AngleUnitMode_Rad: 1>, 'AngleUnitMode_Deg': <AngleUnitMode_e.AngleUnitMode_Deg: 2>}
        pass
    class RWMode_Tessellated_e():
        """
        None

        Members:

          RWMode_Tessellated_Off

          RWMode_Tessellated_On

          RWMode_Tessellated_OnNoBRep
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        RWMode_Tessellated_Off: OCP.STEPCAFControl.RWMode_Tessellated_e # value = <RWMode_Tessellated_e.RWMode_Tessellated_Off: 0>
        RWMode_Tessellated_On: OCP.STEPCAFControl.RWMode_Tessellated_e # value = <RWMode_Tessellated_e.RWMode_Tessellated_On: 1>
        RWMode_Tessellated_OnNoBRep: OCP.STEPCAFControl.RWMode_Tessellated_e # value = <RWMode_Tessellated_e.RWMode_Tessellated_OnNoBRep: 2>
        __entries: dict # value = {'RWMode_Tessellated_Off': (<RWMode_Tessellated_e.RWMode_Tessellated_Off: 0>, None), 'RWMode_Tessellated_On': (<RWMode_Tessellated_e.RWMode_Tessellated_On: 1>, None), 'RWMode_Tessellated_OnNoBRep': (<RWMode_Tessellated_e.RWMode_Tessellated_OnNoBRep: 2>, None)}
        __members__: dict # value = {'RWMode_Tessellated_Off': <RWMode_Tessellated_e.RWMode_Tessellated_Off: 0>, 'RWMode_Tessellated_On': <RWMode_Tessellated_e.RWMode_Tessellated_On: 1>, 'RWMode_Tessellated_OnNoBRep': <RWMode_Tessellated_e.RWMode_Tessellated_OnNoBRep: 2>}
        pass
    class ReadMode_AssemblyLevel_e():
        """
        None

        Members:

          ReadMode_AssemblyLevel_All

          ReadMode_AssemblyLevel_Assembly

          ReadMode_AssemblyLevel_Structure

          ReadMode_AssemblyLevel_Shape
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ReadMode_AssemblyLevel_All: OCP.STEPCAFControl.ReadMode_AssemblyLevel_e # value = <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_All: 1>
        ReadMode_AssemblyLevel_Assembly: OCP.STEPCAFControl.ReadMode_AssemblyLevel_e # value = <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Assembly: 2>
        ReadMode_AssemblyLevel_Shape: OCP.STEPCAFControl.ReadMode_AssemblyLevel_e # value = <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Shape: 4>
        ReadMode_AssemblyLevel_Structure: OCP.STEPCAFControl.ReadMode_AssemblyLevel_e # value = <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Structure: 3>
        __entries: dict # value = {'ReadMode_AssemblyLevel_All': (<ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_All: 1>, None), 'ReadMode_AssemblyLevel_Assembly': (<ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Assembly: 2>, None), 'ReadMode_AssemblyLevel_Structure': (<ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Structure: 3>, None), 'ReadMode_AssemblyLevel_Shape': (<ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Shape: 4>, None)}
        __members__: dict # value = {'ReadMode_AssemblyLevel_All': <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_All: 1>, 'ReadMode_AssemblyLevel_Assembly': <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Assembly: 2>, 'ReadMode_AssemblyLevel_Structure': <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Structure: 3>, 'ReadMode_AssemblyLevel_Shape': <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Shape: 4>}
        pass
    class ReadMode_BSplineContinuity_e():
        """
        None

        Members:

          ReadMode_BSplineContinuity_C0

          ReadMode_BSplineContinuity_C1

          ReadMode_BSplineContinuity_C2
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ReadMode_BSplineContinuity_C0: OCP.STEPCAFControl.ReadMode_BSplineContinuity_e # value = <ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C0: 0>
        ReadMode_BSplineContinuity_C1: OCP.STEPCAFControl.ReadMode_BSplineContinuity_e # value = <ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C1: 1>
        ReadMode_BSplineContinuity_C2: OCP.STEPCAFControl.ReadMode_BSplineContinuity_e # value = <ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C2: 2>
        __entries: dict # value = {'ReadMode_BSplineContinuity_C0': (<ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C0: 0>, None), 'ReadMode_BSplineContinuity_C1': (<ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C1: 1>, None), 'ReadMode_BSplineContinuity_C2': (<ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C2: 2>, None)}
        __members__: dict # value = {'ReadMode_BSplineContinuity_C0': <ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C0: 0>, 'ReadMode_BSplineContinuity_C1': <ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C1: 1>, 'ReadMode_BSplineContinuity_C2': <ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C2: 2>}
        pass
    class ReadMode_MaxPrecision_e():
        """
        None

        Members:

          ReadMode_MaxPrecision_Preferred

          ReadMode_MaxPrecision_Forced
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ReadMode_MaxPrecision_Forced: OCP.STEPCAFControl.ReadMode_MaxPrecision_e # value = <ReadMode_MaxPrecision_e.ReadMode_MaxPrecision_Forced: 1>
        ReadMode_MaxPrecision_Preferred: OCP.STEPCAFControl.ReadMode_MaxPrecision_e # value = <ReadMode_MaxPrecision_e.ReadMode_MaxPrecision_Preferred: 0>
        __entries: dict # value = {'ReadMode_MaxPrecision_Preferred': (<ReadMode_MaxPrecision_e.ReadMode_MaxPrecision_Preferred: 0>, None), 'ReadMode_MaxPrecision_Forced': (<ReadMode_MaxPrecision_e.ReadMode_MaxPrecision_Forced: 1>, None)}
        __members__: dict # value = {'ReadMode_MaxPrecision_Preferred': <ReadMode_MaxPrecision_e.ReadMode_MaxPrecision_Preferred: 0>, 'ReadMode_MaxPrecision_Forced': <ReadMode_MaxPrecision_e.ReadMode_MaxPrecision_Forced: 1>}
        pass
    class ReadMode_Precision_e():
        """
        None

        Members:

          ReadMode_Precision_File

          ReadMode_Precision_User
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ReadMode_Precision_File: OCP.STEPCAFControl.ReadMode_Precision_e # value = <ReadMode_Precision_e.ReadMode_Precision_File: 0>
        ReadMode_Precision_User: OCP.STEPCAFControl.ReadMode_Precision_e # value = <ReadMode_Precision_e.ReadMode_Precision_User: 1>
        __entries: dict # value = {'ReadMode_Precision_File': (<ReadMode_Precision_e.ReadMode_Precision_File: 0>, None), 'ReadMode_Precision_User': (<ReadMode_Precision_e.ReadMode_Precision_User: 1>, None)}
        __members__: dict # value = {'ReadMode_Precision_File': <ReadMode_Precision_e.ReadMode_Precision_File: 0>, 'ReadMode_Precision_User': <ReadMode_Precision_e.ReadMode_Precision_User: 1>}
        pass
    class ReadMode_ProductContext_e():
        """
        None

        Members:

          ReadMode_ProductContext_All

          ReadMode_ProductContext_Design

          ReadMode_ProductContext_Analysis
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ReadMode_ProductContext_All: OCP.STEPCAFControl.ReadMode_ProductContext_e # value = <ReadMode_ProductContext_e.ReadMode_ProductContext_All: 1>
        ReadMode_ProductContext_Analysis: OCP.STEPCAFControl.ReadMode_ProductContext_e # value = <ReadMode_ProductContext_e.ReadMode_ProductContext_Analysis: 3>
        ReadMode_ProductContext_Design: OCP.STEPCAFControl.ReadMode_ProductContext_e # value = <ReadMode_ProductContext_e.ReadMode_ProductContext_Design: 2>
        __entries: dict # value = {'ReadMode_ProductContext_All': (<ReadMode_ProductContext_e.ReadMode_ProductContext_All: 1>, None), 'ReadMode_ProductContext_Design': (<ReadMode_ProductContext_e.ReadMode_ProductContext_Design: 2>, None), 'ReadMode_ProductContext_Analysis': (<ReadMode_ProductContext_e.ReadMode_ProductContext_Analysis: 3>, None)}
        __members__: dict # value = {'ReadMode_ProductContext_All': <ReadMode_ProductContext_e.ReadMode_ProductContext_All: 1>, 'ReadMode_ProductContext_Design': <ReadMode_ProductContext_e.ReadMode_ProductContext_Design: 2>, 'ReadMode_ProductContext_Analysis': <ReadMode_ProductContext_e.ReadMode_ProductContext_Analysis: 3>}
        pass
    class ReadMode_ShapeRepr_e():
        """
        None

        Members:

          ReadMode_ShapeRepr_All

          ReadMode_ShapeRepr_ABSR

          ReadMode_ShapeRepr_MSSR

          ReadMode_ShapeRepr_GBSSR

          ReadMode_ShapeRepr_FBSR

          ReadMode_ShapeRepr_EBWSR

          ReadMode_ShapeRepr_GBWSR
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ReadMode_ShapeRepr_ABSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_ABSR: 2>
        ReadMode_ShapeRepr_All: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_All: 1>
        ReadMode_ShapeRepr_EBWSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_EBWSR: 6>
        ReadMode_ShapeRepr_FBSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_FBSR: 5>
        ReadMode_ShapeRepr_GBSSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_GBSSR: 4>
        ReadMode_ShapeRepr_GBWSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_GBWSR: 7>
        ReadMode_ShapeRepr_MSSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_MSSR: 3>
        __entries: dict # value = {'ReadMode_ShapeRepr_All': (<ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_All: 1>, None), 'ReadMode_ShapeRepr_ABSR': (<ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_ABSR: 2>, None), 'ReadMode_ShapeRepr_MSSR': (<ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_MSSR: 3>, None), 'ReadMode_ShapeRepr_GBSSR': (<ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_GBSSR: 4>, None), 'ReadMode_ShapeRepr_FBSR': (<ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_FBSR: 5>, None), 'ReadMode_ShapeRepr_EBWSR': (<ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_EBWSR: 6>, None), 'ReadMode_ShapeRepr_GBWSR': (<ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_GBWSR: 7>, None)}
        __members__: dict # value = {'ReadMode_ShapeRepr_All': <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_All: 1>, 'ReadMode_ShapeRepr_ABSR': <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_ABSR: 2>, 'ReadMode_ShapeRepr_MSSR': <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_MSSR: 3>, 'ReadMode_ShapeRepr_GBSSR': <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_GBSSR: 4>, 'ReadMode_ShapeRepr_FBSR': <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_FBSR: 5>, 'ReadMode_ShapeRepr_EBWSR': <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_EBWSR: 6>, 'ReadMode_ShapeRepr_GBWSR': <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_GBWSR: 7>}
        pass
    class ReadMode_SurfaceCurve_e():
        """
        None

        Members:

          ReadMode_SurfaceCurve_Default

          ReadMode_SurfaceCurve_2DUse_Preferred

          ReadMode_SurfaceCurve_2DUse_Forced

          ReadMode_SurfaceCurve_3DUse_Preferred

          ReadMode_SurfaceCurve_3DUse_Forced
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ReadMode_SurfaceCurve_2DUse_Forced: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_2DUse_Forced: -2>
        ReadMode_SurfaceCurve_2DUse_Preferred: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_2DUse_Preferred: 2>
        ReadMode_SurfaceCurve_3DUse_Forced: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_3DUse_Forced: -3>
        ReadMode_SurfaceCurve_3DUse_Preferred: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_3DUse_Preferred: 3>
        ReadMode_SurfaceCurve_Default: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_Default: 0>
        __entries: dict # value = {'ReadMode_SurfaceCurve_Default': (<ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_Default: 0>, None), 'ReadMode_SurfaceCurve_2DUse_Preferred': (<ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_2DUse_Preferred: 2>, None), 'ReadMode_SurfaceCurve_2DUse_Forced': (<ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_2DUse_Forced: -2>, None), 'ReadMode_SurfaceCurve_3DUse_Preferred': (<ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_3DUse_Preferred: 3>, None), 'ReadMode_SurfaceCurve_3DUse_Forced': (<ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_3DUse_Forced: -3>, None)}
        __members__: dict # value = {'ReadMode_SurfaceCurve_Default': <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_Default: 0>, 'ReadMode_SurfaceCurve_2DUse_Preferred': <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_2DUse_Preferred: 2>, 'ReadMode_SurfaceCurve_2DUse_Forced': <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_2DUse_Forced: -2>, 'ReadMode_SurfaceCurve_3DUse_Preferred': <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_3DUse_Preferred: 3>, 'ReadMode_SurfaceCurve_3DUse_Forced': <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_3DUse_Forced: -3>}
        pass
    class WriteMode_Assembly_e():
        """
        None

        Members:

          WriteMode_Assembly_Off

          WriteMode_Assembly_On

          WriteMode_Assembly_Auto
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        WriteMode_Assembly_Auto: OCP.STEPCAFControl.WriteMode_Assembly_e # value = <WriteMode_Assembly_e.WriteMode_Assembly_Auto: 2>
        WriteMode_Assembly_Off: OCP.STEPCAFControl.WriteMode_Assembly_e # value = <WriteMode_Assembly_e.WriteMode_Assembly_Off: 0>
        WriteMode_Assembly_On: OCP.STEPCAFControl.WriteMode_Assembly_e # value = <WriteMode_Assembly_e.WriteMode_Assembly_On: 1>
        __entries: dict # value = {'WriteMode_Assembly_Off': (<WriteMode_Assembly_e.WriteMode_Assembly_Off: 0>, None), 'WriteMode_Assembly_On': (<WriteMode_Assembly_e.WriteMode_Assembly_On: 1>, None), 'WriteMode_Assembly_Auto': (<WriteMode_Assembly_e.WriteMode_Assembly_Auto: 2>, None)}
        __members__: dict # value = {'WriteMode_Assembly_Off': <WriteMode_Assembly_e.WriteMode_Assembly_Off: 0>, 'WriteMode_Assembly_On': <WriteMode_Assembly_e.WriteMode_Assembly_On: 1>, 'WriteMode_Assembly_Auto': <WriteMode_Assembly_e.WriteMode_Assembly_Auto: 2>}
        pass
    class WriteMode_PrecisionMode_e():
        """
        None

        Members:

          WriteMode_PrecisionMode_Least

          WriteMode_PrecisionMode_Average

          WriteMode_PrecisionMode_Greatest

          WriteMode_PrecisionMode_Session
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        WriteMode_PrecisionMode_Average: OCP.STEPCAFControl.WriteMode_PrecisionMode_e # value = <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Average: 0>
        WriteMode_PrecisionMode_Greatest: OCP.STEPCAFControl.WriteMode_PrecisionMode_e # value = <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Greatest: 1>
        WriteMode_PrecisionMode_Least: OCP.STEPCAFControl.WriteMode_PrecisionMode_e # value = <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Least: -1>
        WriteMode_PrecisionMode_Session: OCP.STEPCAFControl.WriteMode_PrecisionMode_e # value = <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Session: 2>
        __entries: dict # value = {'WriteMode_PrecisionMode_Least': (<WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Least: -1>, None), 'WriteMode_PrecisionMode_Average': (<WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Average: 0>, None), 'WriteMode_PrecisionMode_Greatest': (<WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Greatest: 1>, None), 'WriteMode_PrecisionMode_Session': (<WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Session: 2>, None)}
        __members__: dict # value = {'WriteMode_PrecisionMode_Least': <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Least: -1>, 'WriteMode_PrecisionMode_Average': <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Average: 0>, 'WriteMode_PrecisionMode_Greatest': <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Greatest: 1>, 'WriteMode_PrecisionMode_Session': <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Session: 2>}
        pass
    class WriteMode_StepSchema_e():
        """
        None

        Members:

          WriteMode_StepSchema_AP214CD

          WriteMode_StepSchema_AP214DIS

          WriteMode_StepSchema_AP203

          WriteMode_StepSchema_AP214IS

          WriteMode_StepSchema_AP242DIS
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        WriteMode_StepSchema_AP203: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP203: 3>
        WriteMode_StepSchema_AP214CD: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP214CD: 1>
        WriteMode_StepSchema_AP214DIS: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP214DIS: 2>
        WriteMode_StepSchema_AP214IS: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP214IS: 4>
        WriteMode_StepSchema_AP242DIS: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP242DIS: 5>
        __entries: dict # value = {'WriteMode_StepSchema_AP214CD': (<WriteMode_StepSchema_e.WriteMode_StepSchema_AP214CD: 1>, None), 'WriteMode_StepSchema_AP214DIS': (<WriteMode_StepSchema_e.WriteMode_StepSchema_AP214DIS: 2>, None), 'WriteMode_StepSchema_AP203': (<WriteMode_StepSchema_e.WriteMode_StepSchema_AP203: 3>, None), 'WriteMode_StepSchema_AP214IS': (<WriteMode_StepSchema_e.WriteMode_StepSchema_AP214IS: 4>, None), 'WriteMode_StepSchema_AP242DIS': (<WriteMode_StepSchema_e.WriteMode_StepSchema_AP242DIS: 5>, None)}
        __members__: dict # value = {'WriteMode_StepSchema_AP214CD': <WriteMode_StepSchema_e.WriteMode_StepSchema_AP214CD: 1>, 'WriteMode_StepSchema_AP214DIS': <WriteMode_StepSchema_e.WriteMode_StepSchema_AP214DIS: 2>, 'WriteMode_StepSchema_AP203': <WriteMode_StepSchema_e.WriteMode_StepSchema_AP203: 3>, 'WriteMode_StepSchema_AP214IS': <WriteMode_StepSchema_e.WriteMode_StepSchema_AP214IS: 4>, 'WriteMode_StepSchema_AP242DIS': <WriteMode_StepSchema_e.WriteMode_StepSchema_AP242DIS: 5>}
        pass
    class WriteMode_VertexMode_e():
        """
        None

        Members:

          WriteMode_VertexMode_OneCompound

          WriteMode_VertexMode_SingleVertex
        """
        def __eq__(self,other : object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self,value : int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self,other : object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self,state : int) -> None: ...
        @property
        def name(self) -> None:
            """
            :type: None
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        WriteMode_VertexMode_OneCompound: OCP.STEPCAFControl.WriteMode_VertexMode_e # value = <WriteMode_VertexMode_e.WriteMode_VertexMode_OneCompound: 0>
        WriteMode_VertexMode_SingleVertex: OCP.STEPCAFControl.WriteMode_VertexMode_e # value = <WriteMode_VertexMode_e.WriteMode_VertexMode_SingleVertex: 1>
        __entries: dict # value = {'WriteMode_VertexMode_OneCompound': (<WriteMode_VertexMode_e.WriteMode_VertexMode_OneCompound: 0>, None), 'WriteMode_VertexMode_SingleVertex': (<WriteMode_VertexMode_e.WriteMode_VertexMode_SingleVertex: 1>, None)}
        __members__: dict # value = {'WriteMode_VertexMode_OneCompound': <WriteMode_VertexMode_e.WriteMode_VertexMode_OneCompound: 0>, 'WriteMode_VertexMode_SingleVertex': <WriteMode_VertexMode_e.WriteMode_VertexMode_SingleVertex: 1>}
        pass
    def BuildProvider(self) -> OCP.DE.DE_Provider: 
        """
        Creates new provider for the own format
        """
    def CheckContent(self,theBuffer : OCP.NCollection.NCollection_Buffer) -> bool: 
        """
        Checks the file content to verify a format
        """
    def CheckExtension(self,theExtension : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Checks the file extension to verify a format
        """
    def Copy(self) -> OCP.DE.DE_ConfigurationNode: 
        """
        Copies values of all fields
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
    def GetExtensions(self) -> OCP.TColStd.TColStd_ListOfAsciiString: 
        """
        Gets list of supported file extensions
        """
    def GetFormat(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets CAD format name of associated provider
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetVendor(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets provider's vendor name of associated provider
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEnabled(self) -> bool: 
        """
        Gets the provider loading status
        """
    def IsExportSupported(self) -> bool: 
        """
        Checks the export supporting
        """
    def IsImportSupported(self) -> bool: 
        """
        Checks the import supporting
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
    def Load(self,theResource : OCP.DE.DE_ConfigurationContext) -> bool: 
        """
        Updates values according the resource
        """
    def Save(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Writes configuration to the string
        """
    def SetEnabled(self,theIsLoaded : bool) -> None: 
        """
        Sets the provider loading status
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateLoad(self) -> bool: 
        """
        Update loading status. Checking for the license.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNode : STEPCAFControl_ConfigurationNode) -> None: ...
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
    AngleUnitMode_Deg: OCP.STEPCAFControl.AngleUnitMode_e # value = <AngleUnitMode_e.AngleUnitMode_Deg: 2>
    AngleUnitMode_File: OCP.STEPCAFControl.AngleUnitMode_e # value = <AngleUnitMode_e.AngleUnitMode_File: 0>
    AngleUnitMode_Rad: OCP.STEPCAFControl.AngleUnitMode_e # value = <AngleUnitMode_e.AngleUnitMode_Rad: 1>
    RWMode_Tessellated_Off: OCP.STEPCAFControl.RWMode_Tessellated_e # value = <RWMode_Tessellated_e.RWMode_Tessellated_Off: 0>
    RWMode_Tessellated_On: OCP.STEPCAFControl.RWMode_Tessellated_e # value = <RWMode_Tessellated_e.RWMode_Tessellated_On: 1>
    RWMode_Tessellated_OnNoBRep: OCP.STEPCAFControl.RWMode_Tessellated_e # value = <RWMode_Tessellated_e.RWMode_Tessellated_OnNoBRep: 2>
    ReadMode_AssemblyLevel_All: OCP.STEPCAFControl.ReadMode_AssemblyLevel_e # value = <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_All: 1>
    ReadMode_AssemblyLevel_Assembly: OCP.STEPCAFControl.ReadMode_AssemblyLevel_e # value = <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Assembly: 2>
    ReadMode_AssemblyLevel_Shape: OCP.STEPCAFControl.ReadMode_AssemblyLevel_e # value = <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Shape: 4>
    ReadMode_AssemblyLevel_Structure: OCP.STEPCAFControl.ReadMode_AssemblyLevel_e # value = <ReadMode_AssemblyLevel_e.ReadMode_AssemblyLevel_Structure: 3>
    ReadMode_BSplineContinuity_C0: OCP.STEPCAFControl.ReadMode_BSplineContinuity_e # value = <ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C0: 0>
    ReadMode_BSplineContinuity_C1: OCP.STEPCAFControl.ReadMode_BSplineContinuity_e # value = <ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C1: 1>
    ReadMode_BSplineContinuity_C2: OCP.STEPCAFControl.ReadMode_BSplineContinuity_e # value = <ReadMode_BSplineContinuity_e.ReadMode_BSplineContinuity_C2: 2>
    ReadMode_MaxPrecision_Forced: OCP.STEPCAFControl.ReadMode_MaxPrecision_e # value = <ReadMode_MaxPrecision_e.ReadMode_MaxPrecision_Forced: 1>
    ReadMode_MaxPrecision_Preferred: OCP.STEPCAFControl.ReadMode_MaxPrecision_e # value = <ReadMode_MaxPrecision_e.ReadMode_MaxPrecision_Preferred: 0>
    ReadMode_Precision_File: OCP.STEPCAFControl.ReadMode_Precision_e # value = <ReadMode_Precision_e.ReadMode_Precision_File: 0>
    ReadMode_Precision_User: OCP.STEPCAFControl.ReadMode_Precision_e # value = <ReadMode_Precision_e.ReadMode_Precision_User: 1>
    ReadMode_ProductContext_All: OCP.STEPCAFControl.ReadMode_ProductContext_e # value = <ReadMode_ProductContext_e.ReadMode_ProductContext_All: 1>
    ReadMode_ProductContext_Analysis: OCP.STEPCAFControl.ReadMode_ProductContext_e # value = <ReadMode_ProductContext_e.ReadMode_ProductContext_Analysis: 3>
    ReadMode_ProductContext_Design: OCP.STEPCAFControl.ReadMode_ProductContext_e # value = <ReadMode_ProductContext_e.ReadMode_ProductContext_Design: 2>
    ReadMode_ShapeRepr_ABSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_ABSR: 2>
    ReadMode_ShapeRepr_All: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_All: 1>
    ReadMode_ShapeRepr_EBWSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_EBWSR: 6>
    ReadMode_ShapeRepr_FBSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_FBSR: 5>
    ReadMode_ShapeRepr_GBSSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_GBSSR: 4>
    ReadMode_ShapeRepr_GBWSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_GBWSR: 7>
    ReadMode_ShapeRepr_MSSR: OCP.STEPCAFControl.ReadMode_ShapeRepr_e # value = <ReadMode_ShapeRepr_e.ReadMode_ShapeRepr_MSSR: 3>
    ReadMode_SurfaceCurve_2DUse_Forced: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_2DUse_Forced: -2>
    ReadMode_SurfaceCurve_2DUse_Preferred: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_2DUse_Preferred: 2>
    ReadMode_SurfaceCurve_3DUse_Forced: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_3DUse_Forced: -3>
    ReadMode_SurfaceCurve_3DUse_Preferred: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_3DUse_Preferred: 3>
    ReadMode_SurfaceCurve_Default: OCP.STEPCAFControl.ReadMode_SurfaceCurve_e # value = <ReadMode_SurfaceCurve_e.ReadMode_SurfaceCurve_Default: 0>
    WriteMode_Assembly_Auto: OCP.STEPCAFControl.WriteMode_Assembly_e # value = <WriteMode_Assembly_e.WriteMode_Assembly_Auto: 2>
    WriteMode_Assembly_Off: OCP.STEPCAFControl.WriteMode_Assembly_e # value = <WriteMode_Assembly_e.WriteMode_Assembly_Off: 0>
    WriteMode_Assembly_On: OCP.STEPCAFControl.WriteMode_Assembly_e # value = <WriteMode_Assembly_e.WriteMode_Assembly_On: 1>
    WriteMode_PrecisionMode_Average: OCP.STEPCAFControl.WriteMode_PrecisionMode_e # value = <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Average: 0>
    WriteMode_PrecisionMode_Greatest: OCP.STEPCAFControl.WriteMode_PrecisionMode_e # value = <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Greatest: 1>
    WriteMode_PrecisionMode_Least: OCP.STEPCAFControl.WriteMode_PrecisionMode_e # value = <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Least: -1>
    WriteMode_PrecisionMode_Session: OCP.STEPCAFControl.WriteMode_PrecisionMode_e # value = <WriteMode_PrecisionMode_e.WriteMode_PrecisionMode_Session: 2>
    WriteMode_StepSchema_AP203: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP203: 3>
    WriteMode_StepSchema_AP214CD: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP214CD: 1>
    WriteMode_StepSchema_AP214DIS: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP214DIS: 2>
    WriteMode_StepSchema_AP214IS: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP214IS: 4>
    WriteMode_StepSchema_AP242DIS: OCP.STEPCAFControl.WriteMode_StepSchema_e # value = <WriteMode_StepSchema_e.WriteMode_StepSchema_AP242DIS: 5>
    WriteMode_VertexMode_OneCompound: OCP.STEPCAFControl.WriteMode_VertexMode_e # value = <WriteMode_VertexMode_e.WriteMode_VertexMode_OneCompound: 0>
    WriteMode_VertexMode_SingleVertex: OCP.STEPCAFControl.WriteMode_VertexMode_e # value = <WriteMode_VertexMode_e.WriteMode_VertexMode_SingleVertex: 1>
    pass
class STEPCAFControl_Controller(OCP.STEPControl.STEPControl_Controller, OCP.XSControl.XSControl_Controller, OCP.Standard.Standard_Transient):
    """
    Extends Controller from STEPControl in order to provide ActorWrite adapted for writing assemblies from DECAF Note that ActorRead from STEPControl is used for reading (inherited automatically)Extends Controller from STEPControl in order to provide ActorWrite adapted for writing assemblies from DECAF Note that ActorRead from STEPControl is used for reading (inherited automatically)Extends Controller from STEPControl in order to provide ActorWrite adapted for writing assemblies from DECAF Note that ActorRead from STEPControl is used for reading (inherited automatically)
    """
    def ActorRead(self,model : OCP.Interface.Interface_InterfaceModel) -> OCP.Transfer.Transfer_ActorOfTransientProcess: 
        """
        Returns the Actor for Read attached to the pair (norm,appli) It can be adapted for data of the input Model, as required Can be read from field then adapted with Model as required
        """
    def ActorWrite(self) -> OCP.Transfer.Transfer_ActorOfFinderProcess: 
        """
        Returns the Actor for Write attached to the pair (norm,appli) Read from field. Can be redefined
        """
    def AdaptorSession(self) -> Any: 
        """
        None
        """
    def AddSessionItem(self,theItem : OCP.Standard.Standard_Transient,theName : str,toApply : bool=False) -> None: 
        """
        Records a Session Item, to be added for customisation of the Work Session. It must have a specific name. <setapplied> is used if <item> is a GeneralModifier, to decide If set to true, <item> will be applied to the hook list "send". Else, it is not applied to any hook list. Remark : this method is to be called at Create time, the recorded items will be used by Customise Warning : if <name> conflicts, the last recorded item is kept
        """
    def AutoRecord(self) -> None: 
        """
        Records <me> is a general dictionary under Short and Long Names (see method Name)
        """
    def Customise(self,WS : OCP.XSControl.XSControl_WorkSession) -> Any: 
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
    @staticmethod
    def Init_s() -> bool: 
        """
        Standard Initialisation. It creates a Controller for STEP-XCAF and records it to various names, available to select it later Returns True when done, False if could not be done
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
    def IsModeWrite(self,modetrans : int,shape : bool=True) -> bool: 
        """
        Tells if a value of <modetrans> is a good value(within bounds) Actually only for shapes
        """
    def ModeWriteBounds(self,modemin : int,modemax : int,shape : bool=True) -> bool: 
        """
        Returns recorded min and max values for modetrans (write) Actually only for shapes Returns True if bounds are set, False else (then, free value)
        """
    def ModeWriteHelp(self,modetrans : int,shape : bool=True) -> str: 
        """
        Returns the help line recorded for a value of modetrans empty if help not defined or not within bounds or if values are free
        """
    def Name(self,rsc : bool=False) -> str: 
        """
        Returns a name, as given when initializing : rsc = False (D) : True Name attached to the Norm (long name) rsc = True : Name of the resource set (i.e. short name)
        """
    def NewModel(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Creates a new empty Model ready to receive data of the Norm. It is taken from STEP Template Model
        """
    def Protocol(self) -> OCP.Interface.Interface_Protocol: 
        """
        Returns the Protocol attached to the Norm (from field)
        """
    def RecognizeWriteShape(self,shape : OCP.TopoDS.TopoDS_Shape,modetrans : int=0) -> bool: 
        """
        Tells if a shape is valid for a transfer to a model Asks the ActorWrite (through a ShapeMapper)
        """
    def RecognizeWriteTransient(self,obj : OCP.Standard.Standard_Transient,modetrans : int=0) -> bool: 
        """
        Tells if <obj> (an application object) is a valid candidate for a transfer to a Model. By default, asks the ActorWrite if known (through a TransientMapper). Can be redefined
        """
    def Record(self,name : str) -> None: 
        """
        Records <me> in a general dictionary under a name Error if <name> already used for another one
        """
    @staticmethod
    def Recorded_s(name : str) -> OCP.XSControl.XSControl_Controller: 
        """
        Returns the Controller attached to a given name Returns a Null Handle if <name> is unknown
        """
    def SessionItem(self,theName : str) -> OCP.Standard.Standard_Transient: 
        """
        Returns an item given its name to record in a Session If <name> is unknown, returns a Null Handle
        """
    def SetModeWrite(self,modemin : int,modemax : int,shape : bool=True) -> None: 
        """
        Sets mininum and maximum values for modetrans (write) Erases formerly recorded bounds and values Actually only for shape Then, for each value a little help can be attached
        """
    def SetModeWriteHelp(self,modetrans : int,help : str,shape : bool=True) -> None: 
        """
        Attaches a short line of help to a value of modetrans (write)
        """
    def SetNames(self,theLongName : str,theShortName : str) -> None: 
        """
        Changes names if a name is empty, the formerly set one remains Remark : Does not call Record or AutoRecord
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransferWriteShape(self,shape : OCP.TopoDS.TopoDS_Shape,FP : OCP.Transfer.Transfer_FinderProcess,model : OCP.Interface.Interface_InterfaceModel,modetrans : int=0,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Takes one Shape and transfers it to the InterfaceModel (already created by NewModel for instance) <modeshape> is to be interpreted by each kind of XstepAdaptor Returns a status : 0 OK 1 No result 2 Fail -1 bad modeshape -2 bad model (requires a StepModel) modeshape : 1 Facetted BRep, 2 Shell, 3 Manifold Solid
        """
    def TransferWriteTransient(self,obj : OCP.Standard.Standard_Transient,FP : OCP.Transfer.Transfer_FinderProcess,model : OCP.Interface.Interface_InterfaceModel,modetrans : int=0,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Takes one Transient Object and transfers it to an InterfaceModel (already created, e.g. by NewModel) (result is recorded in the model by AddWithRefs) FP records produced results and checks
        """
    def WorkLibrary(self) -> OCP.IFSelect.IFSelect_WorkLibrary: 
        """
        Returns the WorkLibrary attached to the Norm. Remark that it has to be in phase with the Protocol (read from field)
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
class STEPCAFControl_DataMapOfLabelShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : STEPCAFControl_DataMapOfLabelShape) -> STEPCAFControl_DataMapOfLabelShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TDF.TDF_Label,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TDF.TDF_Label,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TDF.TDF_Label) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TDF.TDF_Label) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : STEPCAFControl_DataMapOfLabelShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TDF.TDF_Label,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TDF.TDF_Label) -> OCP.TopoDS.TopoDS_Shape: ...
    def IsBound(self,theKey : OCP.TDF.TDF_Label) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.TDF.TDF_Label) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TDF.TDF_Label) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : STEPCAFControl_DataMapOfLabelShape) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class STEPCAFControl_ExternFile(OCP.Standard.Standard_Transient):
    """
    Auxiliary class serving as container for data resulting from translation of external fileAuxiliary class serving as container for data resulting from translation of external fileAuxiliary class serving as container for data resulting from translation of external file
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
    def GetLabel(self) -> OCP.TDF.TDF_Label: 
        """
        None

        None
        """
    def GetLoadStatus(self) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        None

        None
        """
    def GetName(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None

        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTransferStatus(self) -> bool: 
        """
        None

        None
        """
    def GetWS(self) -> OCP.XSControl.XSControl_WorkSession: 
        """
        None

        None
        """
    def GetWriteStatus(self) -> OCP.IFSelect.IFSelect_ReturnStatus: 
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
    @overload
    def SetLabel(self,L : OCP.TDF.TDF_Label) -> None: 
        """
        None

        None
        """
    @overload
    def SetLabel(self,Label : OCP.TDF.TDF_Label) -> None: ...
    def SetLoadStatus(self,stat : OCP.IFSelect.IFSelect_ReturnStatus) -> None: 
        """
        None

        None
        """
    def SetName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None

        None
        """
    def SetTransferStatus(self,isok : bool) -> None: 
        """
        None

        None
        """
    def SetWS(self,WS : OCP.XSControl.XSControl_WorkSession) -> None: 
        """
        None

        None
        """
    def SetWriteStatus(self,stat : OCP.IFSelect.IFSelect_ReturnStatus) -> None: 
        """
        None

        None
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
class STEPCAFControl_GDTProperty():
    """
    This class provides tools for access (read) the GDT properties.
    """
    @staticmethod
    def GetDatumRefModifiers_s(theModifiers : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifiersSequence,theModifWithVal : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue,theValue : float,theUnit : OCP.StepBasic.StepBasic_Unit) -> OCP.StepDimTol.StepDimTol_HArray1OfDatumReferenceModifier: 
        """
        None
        """
    @staticmethod
    def GetDatumTargetName_s(theDatumType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def GetDatumTargetType_s(theDescription : OCP.TCollection.TCollection_HAsciiString,theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType) -> bool: 
        """
        None
        """
    @staticmethod
    def GetDimClassOfTolerance_s(theLAF : OCP.StepShape.StepShape_LimitsAndFits,theFV : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance,theG : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade) -> Tuple[bool]: 
        """
        None
        """
    @staticmethod
    def GetDimModifierName_s(theModifier : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def GetDimModifiers_s(theCRI : OCP.StepRepr.StepRepr_CompoundRepresentationItem,theModifiers : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModifiersSequence) -> None: 
        """
        None
        """
    @staticmethod
    def GetDimQualifierName_s(theQualifier : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def GetDimQualifierType_s(theDescription : OCP.TCollection.TCollection_HAsciiString,theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier) -> bool: 
        """
        None
        """
    @staticmethod
    def GetDimTypeName_s(theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    @staticmethod
    def GetDimType_s(theName : OCP.TCollection.TCollection_HAsciiString,theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType) -> bool: 
        """
        None
        """
    @staticmethod
    def GetGeomToleranceModifier_s(theModifier : OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif) -> OCP.StepDimTol.StepDimTol_GeometricToleranceModifier: 
        """
        None
        """
    @staticmethod
    @overload
    def GetGeomToleranceType_s(theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType) -> OCP.StepDimTol.StepDimTol_GeometricToleranceType: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def GetGeomToleranceType_s(theType : OCP.StepDimTol.StepDimTol_GeometricToleranceType) -> OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType: ...
    @staticmethod
    def GetGeomTolerance_s(theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType) -> OCP.StepDimTol.StepDimTol_GeometricTolerance: 
        """
        None
        """
    @staticmethod
    def GetLimitsAndFits_s(theHole : bool,theFormVariance : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance,theGrade : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade) -> OCP.StepShape.StepShape_LimitsAndFits: 
        """
        None
        """
    @staticmethod
    def GetTessellation_s(theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.StepVisual.StepVisual_TessellatedGeometricSet: 
        """
        None
        """
    @staticmethod
    @overload
    def GetTolValueType_s(theDescription : OCP.TCollection.TCollection_HAsciiString,theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def GetTolValueType_s(theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue) -> OCP.TCollection.TCollection_HAsciiString: ...
    @staticmethod
    def IsDimensionalLocation_s(theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType) -> bool: 
        """
        None
        """
    @staticmethod
    def IsDimensionalSize_s(theType : OCP.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class STEPCAFControl_Provider(OCP.DE.DE_Provider, OCP.Standard.Standard_Transient):
    """
    The class to transfer STEP files. Reads and Writes any STEP files into/from OCCT. Each operation needs configuration node.
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
    def GetFormat(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets CAD format name of associated provider
        """
    def GetNode(self) -> OCP.DE.DE_ConfigurationNode: 
        """
        Gets internal configuration node
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetVendor(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets provider's vendor name of associated provider
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
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration
        """
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    def SetNode(self,theNode : OCP.DE.DE_ConfigurationNode) -> None: 
        """
        Sets internal configuration node
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Writes a CAD file, according internal configuration

        Writes a CAD file, according internal configuration

        Writes a CAD file, according internal configuration

        Writes a CAD file, according internal configuration
        """
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def __init__(self,theNode : OCP.DE.DE_ConfigurationNode) -> None: ...
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
class STEPCAFControl_Reader():
    """
    Provides a tool to read STEP file and put it into DECAF document. Besides transfer of shapes (including assemblies) provided by STEPControl, supports also colors and part names
    """
    def ChangeReader(self) -> OCP.STEPControl.STEPControl_Reader: 
        """
        Returns basic reader
        """
    def ExternFile(self,name : str,ef : STEPCAFControl_ExternFile) -> bool: 
        """
        Returns data on external file by its name Returns False if no external file with given name is read
        """
    def ExternFiles(self) -> Any: 
        """
        Returns data on external files Returns Null handle if no external files are read
        """
    @staticmethod
    def FindInstance_s(NAUO : OCP.StepRepr.StepRepr_NextAssemblyUsageOccurrence,STool : OCP.XCAFDoc.XCAFDoc_ShapeTool,Tool : OCP.STEPConstruct.STEPConstruct_Tool,ShapeLabelMap : OCP.XCAFDoc.XCAFDoc_DataMapOfShapeLabel) -> OCP.TDF.TDF_Label: 
        """
        Returns label of instance of an assembly component corresponding to a given NAUO
        """
    def GetColorMode(self) -> bool: 
        """
        None
        """
    def GetGDTMode(self) -> bool: 
        """
        None
        """
    def GetLayerMode(self) -> bool: 
        """
        None
        """
    def GetMatMode(self) -> bool: 
        """
        None
        """
    def GetNameMode(self) -> bool: 
        """
        None
        """
    def GetPropsMode(self) -> bool: 
        """
        None
        """
    def GetSHUOMode(self) -> bool: 
        """
        None
        """
    def GetShapeLabelMap(self) -> OCP.XCAFDoc.XCAFDoc_DataMapOfShapeLabel: 
        """
        None
        """
    def GetViewMode(self) -> bool: 
        """
        Get View mode
        """
    def Init(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: 
        """
        Clears the internal data structures and attaches to a new session Clears the session if it was not yet set for STEP
        """
    def NbRootsForTransfer(self) -> int: 
        """
        Returns number of roots recognized for transfer Shortcut for Reader().NbRootsForTransfer()
        """
    @overload
    def Perform(self,filename : str,doc : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        None

        Translate STEP file given by filename into the document Return True if succeeded, and False in case of fail
        """
    @overload
    def Perform(self,filename : OCP.TCollection.TCollection_AsciiString,doc : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    def ReadFile(self,theFileName : str) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Loads a file and returns the read status Provided for use like single-file reader.
        """
    def ReadStream(self,theName : str,theIStream : io.BytesIO) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Loads a file from stream and returns the read status.
        """
    def Reader(self) -> OCP.STEPControl.STEPControl_Reader: 
        """
        Returns basic reader as const
        """
    def SetColorMode(self,colormode : bool) -> None: 
        """
        Set ColorMode for indicate read Colors or not.
        """
    def SetGDTMode(self,gdtmode : bool) -> None: 
        """
        Set GDT mode for indicate write GDT or not.
        """
    def SetLayerMode(self,layermode : bool) -> None: 
        """
        Set LayerMode for indicate read Layers or not.
        """
    def SetMatMode(self,matmode : bool) -> None: 
        """
        Set Material mode
        """
    def SetNameMode(self,namemode : bool) -> None: 
        """
        Set NameMode for indicate read Name or not.
        """
    def SetPropsMode(self,propsmode : bool) -> None: 
        """
        PropsMode for indicate read Validation properties or not.
        """
    def SetSHUOMode(self,shuomode : bool) -> None: 
        """
        Set SHUO mode for indicate write SHUO or not.
        """
    def SetViewMode(self,viewmode : bool) -> None: 
        """
        Set View mode
        """
    def Transfer(self,doc : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Translates currently loaded STEP file into the document Returns True if succeeded, and False in case of fail Provided for use like single-file reader
        """
    def TransferOneRoot(self,num : int,doc : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Translates currently loaded STEP file into the document Returns True if succeeded, and False in case of fail Provided for use like single-file reader
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: ...
    pass
class STEPCAFControl_Writer():
    """
    Provides a tool to write DECAF document to the STEP file. Besides transfer of shapes (including assemblies) provided by STEPControl, supports also colors and part names
    """
    def ChangeWriter(self) -> OCP.STEPControl.STEPControl_Writer: 
        """
        Returns basic reader for root file
        """
    @overload
    def ExternFile(self,L : OCP.TDF.TDF_Label,ef : STEPCAFControl_ExternFile) -> bool: 
        """
        Returns data on external file by its original label Returns False if no external file with given name is read

        Returns data on external file by its name Returns False if no external file with given name is read
        """
    @overload
    def ExternFile(self,name : str,ef : STEPCAFControl_ExternFile) -> bool: ...
    def ExternFiles(self) -> Any: 
        """
        Returns data on external files Returns Null handle if no external files are read
        """
    def GetColorMode(self) -> bool: 
        """
        None
        """
    def GetDimTolMode(self) -> bool: 
        """
        None
        """
    def GetLayerMode(self) -> bool: 
        """
        None
        """
    def GetMaterialMode(self) -> bool: 
        """
        None
        """
    def GetNameMode(self) -> bool: 
        """
        None
        """
    def GetPropsMode(self) -> bool: 
        """
        None
        """
    def GetSHUOMode(self) -> bool: 
        """
        None
        """
    def Init(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: 
        """
        Clears the internal data structures and attaches to a new session Clears the session if it was not yet set for STEP
        """
    @overload
    def Perform(self,doc : OCP.TDocStd.TDocStd_Document,filename : str,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        None

        Transfers a document and writes it to a STEP file Returns True if translation is OK
        """
    @overload
    def Perform(self,doc : OCP.TDocStd.TDocStd_Document,filename : OCP.TCollection.TCollection_AsciiString,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    def SetColorMode(self,colormode : bool) -> None: 
        """
        Set ColorMode for indicate write Colors or not.
        """
    def SetDimTolMode(self,dimtolmode : bool) -> None: 
        """
        Set dimtolmode for indicate write D&GTs or not.
        """
    def SetLayerMode(self,layermode : bool) -> None: 
        """
        Set LayerMode for indicate write Layers or not.
        """
    def SetMaterialMode(self,matmode : bool) -> None: 
        """
        Set dimtolmode for indicate write D&GTs or not.
        """
    def SetNameMode(self,namemode : bool) -> None: 
        """
        Set NameMode for indicate write Name or not.
        """
    def SetPropsMode(self,propsmode : bool) -> None: 
        """
        PropsMode for indicate write Validation properties or not.
        """
    def SetSHUOMode(self,shuomode : bool) -> None: 
        """
        Set SHUO mode for indicate write SHUO or not.
        """
    @overload
    def Transfer(self,doc : OCP.TDocStd.TDocStd_Document,mode : OCP.STEPControl.STEPControl_StepModelType=STEPControl_StepModelType.STEPControl_AsIs,multi : str=None,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Transfers a document (or single label) to a STEP model The mode of translation of shape is AsIs If multi is not null pointer, it switches to multifile mode (with external refs), and string pointed by <multi> gives prefix for names of extern files (can be empty string) Returns True if translation is OK

        Method to transfer part of the document specified by label

        Mehod to writing sequence of root assemblies or part of the file specified by use by one label
        """
    @overload
    def Transfer(self,L : OCP.TDF.TDF_Label,mode : OCP.STEPControl.STEPControl_StepModelType=STEPControl_StepModelType.STEPControl_AsIs,multi : str=None,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Transfer(self,L : OCP.TDF.TDF_LabelSequence,mode : OCP.STEPControl.STEPControl_StepModelType=STEPControl_StepModelType.STEPControl_AsIs,multi : str=None,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    def Write(self,theFileName : str) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Writes all the produced models into file In case of multimodel with extern references, filename will be a name of root file, all other files have names of corresponding parts Provided for use like single-file writer
        """
    def WriteStream(self,theStream : io.BytesIO) -> OCP.IFSelect.IFSelect_ReturnStatus: 
        """
        Writes all the produced models into the stream. Provided for use like single-file writer
        """
    def Writer(self) -> OCP.STEPControl.STEPControl_Writer: 
        """
        Returns basic reader as const
        """
    @overload
    def __init__(self,WS : OCP.XSControl.XSControl_WorkSession,scratch : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
