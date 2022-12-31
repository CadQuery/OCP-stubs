import OCP.BRepAlgoAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.TopoDS
import OCP.BRepTools
import OCP.NCollection
import OCP.Message
import OCP.gp
import OCP.BRepBuilderAPI
import OCP.TopTools
import OCP.Standard
import OCP.BOPAlgo
import io
__all__  = [
"BRepAlgoAPI_Algo",
"BRepAlgoAPI_BuilderAlgo",
"BRepAlgoAPI_BooleanOperation",
"BRepAlgoAPI_Check",
"BRepAlgoAPI_Common",
"BRepAlgoAPI_Cut",
"BRepAlgoAPI_Defeaturing",
"BRepAlgoAPI_Fuse",
"BRepAlgoAPI_Section",
"BRepAlgoAPI_Splitter"
]
class BRepAlgoAPI_Algo(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Provides the root interface for the API algorithms
    """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance.
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
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing.
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance.
        """
    def SetRunParallel(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def SetUseOBB(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    pass
class BRepAlgoAPI_BuilderAlgo(BRepAlgoAPI_Algo, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The class contains API level of the General Fuse algorithm.
    """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Gets the arguments
        """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the algorithm
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def DSFiller(self) -> OCP.BOPAlgo.BOPAlgo_PaveFiller: 
        """
        Returns the Intersection tool
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance.
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <theS>. In frames of Boolean Operations algorithms only Edges and Faces could have Generated elements, as only they produce new elements during intersection: - Edges can generate new vertices; - Faces can generate new edges and vertices.
        """
    def Glue(self) -> OCP.BOPAlgo.BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation. Normally, General Fuse operation should not have Deleted elements, but all derived operation can have.
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns flag of history availability
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History tool
        """
    def IsDeleted(self,aS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the shape <theS> has been completely removed from the result, i.e. the result does not contain the shape itself and any of its splits. Returns TRUE if the shape has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes modified from the shape <theS>. If any, the list will contain only those splits of the given shape, contained in the result.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing.
        """
    def SectionEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of section edges. The edges represent the result of intersection between arguments of operation.
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the arguments
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance.
        """
    def SetGlue(self,theGlue : OCP.BOPAlgo.BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm, which allows increasing performance of the intersection of the input shapes.
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def SetRunParallel(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetUseOBB(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def SimplifyResult(self,theUnifyEdges : bool=True,theUnifyFaces : bool=True,theAngularTol : float=1e-12) -> None: 
        """
        Simplification of the result shape is performed by the means of *ShapeUpgrade_UnifySameDomain* algorithm. The result of the operation will be overwritten with the simplified result.
        """
    @overload
    def __init__(self,thePF : OCP.BOPAlgo.BOPAlgo_PaveFiller) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepAlgoAPI_BooleanOperation(BRepAlgoAPI_BuilderAlgo, BRepAlgoAPI_Algo, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The root API class for performing Boolean Operations on arbitrary shapes.
    """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Gets the arguments
        """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the Boolean operation.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def DSFiller(self) -> OCP.BOPAlgo.BOPAlgo_PaveFiller: 
        """
        Returns the Intersection tool
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance.
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <theS>. In frames of Boolean Operations algorithms only Edges and Faces could have Generated elements, as only they produce new elements during intersection: - Edges can generate new vertices; - Faces can generate new edges and vertices.
        """
    def Glue(self) -> OCP.BOPAlgo.BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation. Normally, General Fuse operation should not have Deleted elements, but all derived operation can have.
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns flag of history availability
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History tool
        """
    def IsDeleted(self,aS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the shape <theS> has been completely removed from the result, i.e. the result does not contain the shape itself and any of its splits. Returns TRUE if the shape has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes modified from the shape <theS>. If any, the list will contain only those splits of the given shape, contained in the result.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Operation(self) -> OCP.BOPAlgo.BOPAlgo_Operation: 
        """
        Returns the type of Boolean Operation
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing.
        """
    def SectionEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of section edges. The edges represent the result of intersection between arguments of operation.
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the arguments
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance.
        """
    def SetGlue(self,theGlue : OCP.BOPAlgo.BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm, which allows increasing performance of the intersection of the input shapes.
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def SetOperation(self,theBOP : OCP.BOPAlgo.BOPAlgo_Operation) -> None: 
        """
        Sets the type of Boolean operation
        """
    def SetRunParallel(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the Tool arguments
        """
    def SetUseOBB(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first argument involved in this Boolean operation. Obsolete
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second argument involved in this Boolean operation. Obsolete
        """
    def SimplifyResult(self,theUnifyEdges : bool=True,theUnifyFaces : bool=True,theAngularTol : float=1e-12) -> None: 
        """
        Simplification of the result shape is performed by the means of *ShapeUpgrade_UnifySameDomain* algorithm. The result of the operation will be overwritten with the simplified result.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tools arguments
        """
    @overload
    def __init__(self,thePF : OCP.BOPAlgo.BOPAlgo_PaveFiller) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepAlgoAPI_Check(OCP.BOPAlgo.BOPAlgo_Options):
    """
    The class Check provides a diagnostic tool for checking the validity of the single shape or couple of shapes. The shapes are checked on: - Topological validity; - Small edges; - Self-interference; - Validity for Boolean operation of certain type (for couple of shapes only).
    """
    def AddError(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as error (fail)
        """
    def AddWarning(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as warning
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns allocator
        """
    def Clear(self) -> None: 
        """
        Clears all warnings and errors, and any data cached by the algorithm. User defined options are not cleared.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def DumpErrors(self,theOS : io.BytesIO) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : io.BytesIO) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    @staticmethod
    def GetParallelMode_s() -> bool: 
        """
        Gets the global parallel mode
        """
    def GetReport(self) -> OCP.Message.Message_Report: 
        """
        Returns report collecting all errors and warnings
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
        """
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def IsValid(self) -> bool: 
        """
        Shows whether shape(s) valid or not.
        """
    def Perform(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the check.
        """
    def Result(self) -> OCP.BOPAlgo.BOPAlgo_ListOfCheckResult: 
        """
        Returns faulty shapes.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    @overload
    def SetData(self,theS : OCP.TopoDS.TopoDS_Shape,bTestSE : bool=True,bTestSI : bool=True) -> None: 
        """
        Initializes the algorithm with single shape.

        Initializes the algorithm with couple of shapes. Additionally to the validity checks of each given shape, the types of the given shapes will be checked on validity for Boolean operation of given type.
        """
    @overload
    def SetData(self,theS1 : OCP.TopoDS.TopoDS_Shape,theS2 : OCP.TopoDS.TopoDS_Shape,theOp : OCP.BOPAlgo.BOPAlgo_Operation=BOPAlgo_Operation.BOPAlgo_UNKNOWN,bTestSE : bool=True,bTestSI : bool=True) -> None: ...
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theS1 : OCP.TopoDS.TopoDS_Shape,theS2 : OCP.TopoDS.TopoDS_Shape,theOp : OCP.BOPAlgo.BOPAlgo_Operation=BOPAlgo_Operation.BOPAlgo_UNKNOWN,bTestSE : bool=True,bTestSI : bool=True,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self,theS : OCP.TopoDS.TopoDS_Shape,bTestSE : bool=True,bTestSI : bool=True,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    pass
class BRepAlgoAPI_Common(BRepAlgoAPI_BooleanOperation, BRepAlgoAPI_BuilderAlgo, BRepAlgoAPI_Algo, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The class provides Boolean common operation between arguments and tools (Boolean Intersection).
    """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Gets the arguments
        """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the Boolean operation.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def DSFiller(self) -> OCP.BOPAlgo.BOPAlgo_PaveFiller: 
        """
        Returns the Intersection tool
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance.
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <theS>. In frames of Boolean Operations algorithms only Edges and Faces could have Generated elements, as only they produce new elements during intersection: - Edges can generate new vertices; - Faces can generate new edges and vertices.
        """
    def Glue(self) -> OCP.BOPAlgo.BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation. Normally, General Fuse operation should not have Deleted elements, but all derived operation can have.
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns flag of history availability
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History tool
        """
    def IsDeleted(self,aS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the shape <theS> has been completely removed from the result, i.e. the result does not contain the shape itself and any of its splits. Returns TRUE if the shape has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes modified from the shape <theS>. If any, the list will contain only those splits of the given shape, contained in the result.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Operation(self) -> OCP.BOPAlgo.BOPAlgo_Operation: 
        """
        Returns the type of Boolean Operation
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing.
        """
    def SectionEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of section edges. The edges represent the result of intersection between arguments of operation.
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the arguments
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance.
        """
    def SetGlue(self,theGlue : OCP.BOPAlgo.BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm, which allows increasing performance of the intersection of the input shapes.
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def SetOperation(self,theBOP : OCP.BOPAlgo.BOPAlgo_Operation) -> None: 
        """
        Sets the type of Boolean operation
        """
    def SetRunParallel(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the Tool arguments
        """
    def SetUseOBB(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first argument involved in this Boolean operation. Obsolete
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second argument involved in this Boolean operation. Obsolete
        """
    def SimplifyResult(self,theUnifyEdges : bool=True,theUnifyFaces : bool=True,theAngularTol : float=1e-12) -> None: 
        """
        Simplification of the result shape is performed by the means of *ShapeUpgrade_UnifySameDomain* algorithm. The result of the operation will be overwritten with the simplified result.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tools arguments
        """
    @overload
    def __init__(self,PF : OCP.BOPAlgo.BOPAlgo_PaveFiller) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,PF : OCP.BOPAlgo.BOPAlgo_PaveFiller,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    pass
class BRepAlgoAPI_Cut(BRepAlgoAPI_BooleanOperation, BRepAlgoAPI_BuilderAlgo, BRepAlgoAPI_Algo, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The class Cut provides Boolean cut operation between arguments and tools (Boolean Subtraction).
    """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Gets the arguments
        """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the Boolean operation.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def DSFiller(self) -> OCP.BOPAlgo.BOPAlgo_PaveFiller: 
        """
        Returns the Intersection tool
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance.
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <theS>. In frames of Boolean Operations algorithms only Edges and Faces could have Generated elements, as only they produce new elements during intersection: - Edges can generate new vertices; - Faces can generate new edges and vertices.
        """
    def Glue(self) -> OCP.BOPAlgo.BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation. Normally, General Fuse operation should not have Deleted elements, but all derived operation can have.
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns flag of history availability
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History tool
        """
    def IsDeleted(self,aS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the shape <theS> has been completely removed from the result, i.e. the result does not contain the shape itself and any of its splits. Returns TRUE if the shape has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes modified from the shape <theS>. If any, the list will contain only those splits of the given shape, contained in the result.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Operation(self) -> OCP.BOPAlgo.BOPAlgo_Operation: 
        """
        Returns the type of Boolean Operation
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing.
        """
    def SectionEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of section edges. The edges represent the result of intersection between arguments of operation.
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the arguments
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance.
        """
    def SetGlue(self,theGlue : OCP.BOPAlgo.BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm, which allows increasing performance of the intersection of the input shapes.
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def SetOperation(self,theBOP : OCP.BOPAlgo.BOPAlgo_Operation) -> None: 
        """
        Sets the type of Boolean operation
        """
    def SetRunParallel(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the Tool arguments
        """
    def SetUseOBB(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first argument involved in this Boolean operation. Obsolete
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second argument involved in this Boolean operation. Obsolete
        """
    def SimplifyResult(self,theUnifyEdges : bool=True,theUnifyFaces : bool=True,theAngularTol : float=1e-12) -> None: 
        """
        Simplification of the result shape is performed by the means of *ShapeUpgrade_UnifySameDomain* algorithm. The result of the operation will be overwritten with the simplified result.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tools arguments
        """
    @overload
    def __init__(self,PF : OCP.BOPAlgo.BOPAlgo_PaveFiller) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,aDSF : OCP.BOPAlgo.BOPAlgo_PaveFiller,bFWD : bool=True,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    pass
class BRepAlgoAPI_Defeaturing(BRepAlgoAPI_Algo, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The BRepAlgoAPI_Defeaturing algorithm is the API algorithm intended for removal of the unwanted parts from the shape. The unwanted parts (or features) can be holes, protrusions, gaps, chamfers, fillets etc. The shape itself is not modified, the new shape is built as the result.
    """
    def AddFaceToRemove(self,theFace : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the features to remove from the input shape.
        """
    def AddFacesToRemove(self,theFaces : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Adds the faces to remove from the input shape.
        """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the operation
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def FacesToRemove(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of faces which have been requested for removal from the input shape.
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance.
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <theS> during the operation.
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns whether the history was requested or not.
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        Returns the History of shapes modifications
        """
    def InputShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the input shape
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape <theS> has been deleted during the operation. It means that the shape has no any trace in the result. Otherwise it returns false.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <theS> during the operation.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing.
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance.
        """
    def SetRunParallel(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape for processing.
        """
    def SetToFillHistory(self,theFlag : bool) -> None: 
        """
        Defines whether to track the modification of the shapes or not.
        """
    def SetUseOBB(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BRepAlgoAPI_Fuse(BRepAlgoAPI_BooleanOperation, BRepAlgoAPI_BuilderAlgo, BRepAlgoAPI_Algo, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The class provides Boolean fusion operation between arguments and tools (Boolean Union).
    """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Gets the arguments
        """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the Boolean operation.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def DSFiller(self) -> OCP.BOPAlgo.BOPAlgo_PaveFiller: 
        """
        Returns the Intersection tool
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance.
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <theS>. In frames of Boolean Operations algorithms only Edges and Faces could have Generated elements, as only they produce new elements during intersection: - Edges can generate new vertices; - Faces can generate new edges and vertices.
        """
    def Glue(self) -> OCP.BOPAlgo.BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation. Normally, General Fuse operation should not have Deleted elements, but all derived operation can have.
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns flag of history availability
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History tool
        """
    def IsDeleted(self,aS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the shape <theS> has been completely removed from the result, i.e. the result does not contain the shape itself and any of its splits. Returns TRUE if the shape has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes modified from the shape <theS>. If any, the list will contain only those splits of the given shape, contained in the result.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Operation(self) -> OCP.BOPAlgo.BOPAlgo_Operation: 
        """
        Returns the type of Boolean Operation
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing.
        """
    def SectionEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of section edges. The edges represent the result of intersection between arguments of operation.
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the arguments
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance.
        """
    def SetGlue(self,theGlue : OCP.BOPAlgo.BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm, which allows increasing performance of the intersection of the input shapes.
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def SetOperation(self,theBOP : OCP.BOPAlgo.BOPAlgo_Operation) -> None: 
        """
        Sets the type of Boolean operation
        """
    def SetRunParallel(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the Tool arguments
        """
    def SetUseOBB(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first argument involved in this Boolean operation. Obsolete
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second argument involved in this Boolean operation. Obsolete
        """
    def SimplifyResult(self,theUnifyEdges : bool=True,theUnifyFaces : bool=True,theAngularTol : float=1e-12) -> None: 
        """
        Simplification of the result shape is performed by the means of *ShapeUpgrade_UnifySameDomain* algorithm. The result of the operation will be overwritten with the simplified result.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tools arguments
        """
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,aDSF : OCP.BOPAlgo.BOPAlgo_PaveFiller,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @overload
    def __init__(self,PF : OCP.BOPAlgo.BOPAlgo_PaveFiller) -> None: ...
    pass
class BRepAlgoAPI_Section(BRepAlgoAPI_BooleanOperation, BRepAlgoAPI_BuilderAlgo, BRepAlgoAPI_Algo, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The algorithm is to build a Section operation between arguments and tools. The result of Section operation consists of vertices and edges. The result of Section operation contains: 1. new vertices that are subjects of V/V, E/E, E/F, F/F interferences 2. vertices that are subjects of V/E, V/F interferences 3. new edges that are subjects of F/F interferences 4. edges that are Common Blocks
    """
    def Approximation(self,B : bool) -> None: 
        """
        None
        """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Gets the arguments
        """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the algorithm Filling interference Data Structure (if it is necessary) Building the result of the operation.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def ComputePCurveOn1(self,B : bool) -> None: 
        """
        Indicates whether the P-Curve should be (or not) performed on the argument. By default, no parametric 2D curve (pcurve) is defined for the edges of the result. If ComputePCurve1 equals true, further computations performed to attach an P-Curve in the parametric space of the argument to the constructed edges. Obsolete
        """
    def ComputePCurveOn2(self,B : bool) -> None: 
        """
        Indicates whether the P-Curve should be (or not) performed on the tool. By default, no parametric 2D curve (pcurve) is defined for the edges of the result. If ComputePCurve1 equals true, further computations performed to attach an P-Curve in the parametric space of the tool to the constructed edges. Obsolete
        """
    def DSFiller(self) -> OCP.BOPAlgo.BOPAlgo_PaveFiller: 
        """
        Returns the Intersection tool
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance.
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <theS>. In frames of Boolean Operations algorithms only Edges and Faces could have Generated elements, as only they produce new elements during intersection: - Edges can generate new vertices; - Faces can generate new edges and vertices.
        """
    def Glue(self) -> OCP.BOPAlgo.BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasAncestorFaceOn1(self,E : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        get the face of the first part giving section edge <E>. Returns True on the 3 following conditions : 1/ <E> is an edge returned by the Shape() metwod. 2/ First part of section performed is a shape. 3/ <E> is built on a intersection curve (i.e <E> is not the result of common edges) When False, F remains untouched. Obsolete
        """
    def HasAncestorFaceOn2(self,E : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Identifies the ancestor faces of the intersection edge E resulting from the last computation performed in this framework, that is, the faces of the two original shapes on which the edge E lies: - HasAncestorFaceOn1 gives the ancestor face in the first shape, and - HasAncestorFaceOn2 gives the ancestor face in the second shape. These functions return true if an ancestor face F is found, or false if not. An ancestor face is identifiable for the edge E if the following conditions are satisfied: - the first part on which this algorithm performed its last computation is a shape, that is, it was not given as a surface or a plane at the time of construction of this algorithm or at a later time by the Init1 function, - E is one of the elementary edges built by the last computation of this section algorithm. To use these functions properly, you have to test the returned Boolean value before using the ancestor face: F is significant only if the returned Boolean value equals true. Obsolete
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation. Normally, General Fuse operation should not have Deleted elements, but all derived operation can have.
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns flag of history availability
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History tool
        """
    @overload
    def Init1(self,Pl : OCP.gp.gp_Pln) -> None: 
        """
        initialize the argument <S1> - argument Obsolete

        initialize the argument <Pl> - argument Obsolete

        initialize the argument <Sf> - argument Obsolete
        """
    @overload
    def Init1(self,S1 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def Init1(self,Sf : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def Init2(self,Pl : OCP.gp.gp_Pln) -> None: 
        """
        initialize the tool <S2> - tool Obsolete

        initialize the tool <Pl> - tool Obsolete

        initialize the tool <Sf> - tool Obsolete
        """
    @overload
    def Init2(self,Sf : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def Init2(self,S2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def IsDeleted(self,aS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the shape <theS> has been completely removed from the result, i.e. the result does not contain the shape itself and any of its splits. Returns TRUE if the shape has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes modified from the shape <theS>. If any, the list will contain only those splits of the given shape, contained in the result.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Operation(self) -> OCP.BOPAlgo.BOPAlgo_Operation: 
        """
        Returns the type of Boolean Operation
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing.
        """
    def SectionEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of section edges. The edges represent the result of intersection between arguments of operation.
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the arguments
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance.
        """
    def SetGlue(self,theGlue : OCP.BOPAlgo.BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm, which allows increasing performance of the intersection of the input shapes.
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def SetOperation(self,theBOP : OCP.BOPAlgo.BOPAlgo_Operation) -> None: 
        """
        Sets the type of Boolean operation
        """
    def SetRunParallel(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the Tool arguments
        """
    def SetUseOBB(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first argument involved in this Boolean operation. Obsolete
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the second argument involved in this Boolean operation. Obsolete
        """
    def SimplifyResult(self,theUnifyEdges : bool=True,theUnifyFaces : bool=True,theAngularTol : float=1e-12) -> None: 
        """
        Simplification of the result shape is performed by the means of *ShapeUpgrade_UnifySameDomain* algorithm. The result of the operation will be overwritten with the simplified result.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tools arguments
        """
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,aDSF : OCP.BOPAlgo.BOPAlgo_PaveFiller,PerformNow : bool=True) -> None: ...
    @overload
    def __init__(self,Sf : OCP.Geom.Geom_Surface,S2 : OCP.TopoDS.TopoDS_Shape,PerformNow : bool=True) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,PerformNow : bool=True) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,Sf : OCP.Geom.Geom_Surface,PerformNow : bool=True) -> None: ...
    @overload
    def __init__(self,PF : OCP.BOPAlgo.BOPAlgo_PaveFiller) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Sf1 : OCP.Geom.Geom_Surface,Sf2 : OCP.Geom.Geom_Surface,PerformNow : bool=True) -> None: ...
    @overload
    def __init__(self,S1 : OCP.TopoDS.TopoDS_Shape,Pl : OCP.gp.gp_Pln,PerformNow : bool=True) -> None: ...
    pass
class BRepAlgoAPI_Splitter(BRepAlgoAPI_BuilderAlgo, BRepAlgoAPI_Algo, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The class contains API level of the **Splitter** algorithm, which allows splitting a group of arbitrary shapes by the other group of arbitrary shapes. The arguments of the operation are divided on two groups: *Objects* - shapes that will be split; *Tools* - shapes by which the *Objects* will be split. The result of the operation contains only the split parts of the shapes from the group of *Objects*. The split parts of the shapes from the group of *Tools* are excluded from the result. The shapes can be split by the other shapes from the same group (in case these shapes are interfering).
    """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Gets the arguments
        """
    def Build(self,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Performs the Split operation. Performs the intersection of the argument shapes (both objects and tools) and splits objects by the tools.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def DSFiller(self) -> OCP.BOPAlgo.BOPAlgo_PaveFiller: 
        """
        Returns the Intersection tool
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance.
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <theS>. In frames of Boolean Operations algorithms only Edges and Faces could have Generated elements, as only they produce new elements during intersection: - Edges can generate new vertices; - Faces can generate new edges and vertices.
        """
    def Glue(self) -> OCP.BOPAlgo.BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation. Normally, General Fuse operation should not have Deleted elements, but all derived operation can have.
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns flag of history availability
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History tool
        """
    def IsDeleted(self,aS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Checks if the shape <theS> has been completely removed from the result, i.e. the result does not contain the shape itself and any of its splits. Returns TRUE if the shape has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the shapes modified from the shape <theS>. If any, the list will contain only those splits of the given shape, contained in the result.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing.
        """
    def SectionEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of section edges. The edges represent the result of intersection between arguments of operation.
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the arguments
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance.
        """
    def SetGlue(self,theGlue : OCP.BOPAlgo.BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm, which allows increasing performance of the intersection of the input shapes.
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def SetRunParallel(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the Tool arguments
        """
    def SetUseOBB(self,thFlag : bool) -> None: 
        """
        Set the flag of parallel processing.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def SimplifyResult(self,theUnifyEdges : bool=True,theUnifyFaces : bool=True,theAngularTol : float=1e-12) -> None: 
        """
        Simplification of the result shape is performed by the means of *ShapeUpgrade_UnifySameDomain* algorithm. The result of the operation will be overwritten with the simplified result.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tool arguments
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,thePF : OCP.BOPAlgo.BOPAlgo_PaveFiller) -> None: ...
    pass
