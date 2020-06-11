import OCP.BOPAlgo
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.BOPDS
import OCP.TopAbs
import OCP.IntTools
import OCP.Standard
import OCP.TopTools
import OCP.BRepTools
import OCP.Message
import OCP.TopoDS
import OCP.BOPTools
__all__  = [
"BOPAlgo_AlertAcquiredSelfIntersection",
"BOPAlgo_AlertBOPNotAllowed",
"BOPAlgo_AlertBOPNotSet",
"BOPAlgo_AlertBadPositioning",
"BOPAlgo_AlertBuilderFailed",
"BOPAlgo_AlertBuildingPCurveFailed",
"BOPAlgo_AlertEmptyShape",
"BOPAlgo_AlertFaceBuilderUnusedEdges",
"BOPAlgo_AlertIntersectionFailed",
"BOPAlgo_AlertIntersectionOfPairOfShapesFailed",
"BOPAlgo_AlertMultiDimensionalArguments",
"BOPAlgo_AlertMultipleArguments",
"BOPAlgo_AlertNoFacesToRemove",
"BOPAlgo_AlertNoFiller",
"BOPAlgo_AlertNoPeriodicityRequired",
"BOPAlgo_AlertNotSplittableEdge",
"BOPAlgo_AlertNullInputShapes",
"BOPAlgo_AlertPostTreatFF",
"BOPAlgo_AlertRemovalOfIBForEdgesFailed",
"BOPAlgo_AlertRemovalOfIBForFacesFailed",
"BOPAlgo_AlertRemovalOfIBForMDimShapes",
"BOPAlgo_AlertRemovalOfIBForSolidsFailed",
"BOPAlgo_AlertRemoveFeaturesFailed",
"BOPAlgo_AlertSelfInterferingShape",
"BOPAlgo_AlertShapeIsNotPeriodic",
"BOPAlgo_AlertShellSplitterFailed",
"BOPAlgo_AlertSolidBuilderFailed",
"BOPAlgo_AlertSolidBuilderUnusedFaces",
"BOPAlgo_AlertTooFewArguments",
"BOPAlgo_AlertTooSmallEdge",
"BOPAlgo_AlertUnableToGlue",
"BOPAlgo_AlertUnableToMakeIdentical",
"BOPAlgo_AlertUnableToMakePeriodic",
"BOPAlgo_AlertUnableToOrientTheShape",
"BOPAlgo_AlertUnableToRemoveTheFeature",
"BOPAlgo_AlertUnableToRepeat",
"BOPAlgo_AlertUnableToTrim",
"BOPAlgo_AlertUnknownShape",
"BOPAlgo_AlertUnsupportedType",
"BOPAlgo_Options",
"BOPAlgo_Algo",
"BOPAlgo_BuilderShape",
"BOPAlgo_Builder",
"BOPAlgo_BuilderArea",
"BOPAlgo_BuilderFace",
"BOPAlgo_ToolsProvider",
"BOPAlgo_BuilderSolid",
"BOPAlgo_CellsBuilder",
"BOPAlgo_CheckResult",
"BOPAlgo_CheckStatus",
"BOPAlgo_PaveFiller",
"BOPAlgo_EdgeInfo",
"BOPAlgo_GlueEnum",
"BOPAlgo_IndexedDataMapOfShapeListOfEdgeInfo",
"BOPAlgo_ListOfCheckResult",
"BOPAlgo_ListOfEdgeInfo",
"BOPAlgo_MakeConnected",
"BOPAlgo_MakePeriodic",
"BOPAlgo_MakerVolume",
"BOPAlgo_Operation",
"BOPAlgo_ArgumentAnalyzer",
"BOPAlgo_CheckerSI",
"BOPAlgo_RemoveFeatures",
"BOPAlgo_Section",
"BOPAlgo_SectionAttribute",
"BOPAlgo_ShellSplitter",
"BOPAlgo_Splitter",
"BOPAlgo_Tools",
"BOPAlgo_BOP",
"BOPAlgo_WireEdgeSet",
"BOPAlgo_WireSplitter",
"BOPAlgo_BadType",
"BOPAlgo_COMMON",
"BOPAlgo_CUT",
"BOPAlgo_CUT21",
"BOPAlgo_CheckUnknown",
"BOPAlgo_FUSE",
"BOPAlgo_GeomAbs_C0",
"BOPAlgo_GlueFull",
"BOPAlgo_GlueOff",
"BOPAlgo_GlueShift",
"BOPAlgo_IncompatibilityOfEdge",
"BOPAlgo_IncompatibilityOfFace",
"BOPAlgo_IncompatibilityOfVertex",
"BOPAlgo_InvalidCurveOnSurface",
"BOPAlgo_NonRecoverableFace",
"BOPAlgo_NotValid",
"BOPAlgo_OperationAborted",
"BOPAlgo_SECTION",
"BOPAlgo_SelfIntersect",
"BOPAlgo_TooSmallEdge",
"BOPAlgo_UNKNOWN"
]
class BOPAlgo_AlertAcquiredSelfIntersection(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Some sub-shapes of some of the argument become connected through other shapes and the argument became self-interfered
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertBOPNotAllowed(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Boolean operation of given type is not allowed on the given inputs
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertBOPNotSet(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    The type of Boolean Operation is not set
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertBadPositioning(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    The positioning of the shapes leads to creation of the small edges without valid range
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertBuilderFailed(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Building of the result shape has failed
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertBuildingPCurveFailed(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Building 2D curve of edge on face has failed
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertEmptyShape(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Some of the arguments are empty shapes
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertFaceBuilderUnusedEdges(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Some of the edges passed to the Face Builder algorithm have not been classified and not used for faces creation
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertIntersectionFailed(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    The intersection of the arguments has failed
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertIntersectionOfPairOfShapesFailed(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Intersection of pair of shapes has failed
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertMultiDimensionalArguments(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Multi-dimensional arguments
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertMultipleArguments(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    More than one argument is provided
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertNoFacesToRemove(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    No faces have been found for removal
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertNoFiller(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    The Pave Filler (the intersection tool) has not been created
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertNoPeriodicityRequired(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    No periodicity has been requested for the shape
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertNotSplittableEdge(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Some edges are very small and have such a small valid range, that they cannot be split
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertNullInputShapes(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Null input shapes
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertPostTreatFF(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Cannot connect face intersection curves
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertRemovalOfIBForEdgesFailed(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Removal of internal boundaries among Edges has failed
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertRemovalOfIBForFacesFailed(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Removal of internal boundaries among Faces has failed
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertRemovalOfIBForMDimShapes(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Removal of internal boundaries among the multi-dimensional shapes is not supported yet
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertRemovalOfIBForSolidsFailed(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Removal of internal boundaries among Solids has failed
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertRemoveFeaturesFailed(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    The Feature Removal algorithm has failed
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertSelfInterferingShape(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Some of the arguments are self-interfering shapes
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertShapeIsNotPeriodic(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    The shape is not periodic
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertShellSplitterFailed(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    The positioning of the shapes leads to creation of the small edges without valid range
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertSolidBuilderFailed(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    The BuilderSolid algorithm has failed
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertSolidBuilderUnusedFaces(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Some of the faces passed to the Solid Builder algorithm have not been classified and not used for solids creation
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertTooFewArguments(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    There are no enough arguments to perform the operation
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        If possible, merge data contained in this alert to theTarget.
        """
    def SupportsMerge(self) -> bool: 
        """
        Return true if this type of alert can be merged with other of the same type to avoid duplication. Basis implementation returns true.
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
class BOPAlgo_AlertTooSmallEdge(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Some edges are too small and have no valid range
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertUnableToGlue(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Unable to glue the shapes
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertUnableToMakeIdentical(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Unable to make the shape to look identical on opposite sides (Splitter fails)
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertUnableToMakePeriodic(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Unable to make the shape periodic
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertUnableToOrientTheShape(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Unable to orient the shape correctly
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertUnableToRemoveTheFeature(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Unable to remove the feature
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertUnableToRepeat(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Unable to repeat the shape (Gluer fails)
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertUnableToTrim(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Unable to trim the shape for making it periodic (BOP Common fails)
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertUnknownShape(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Shape is unknown for operation
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_AlertUnsupportedType(OCP.TopoDS.TopoDS_AlertWithShape, OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Unsupported type of input shape
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns contained shape
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape
        """
    def SupportsMerge(self) -> bool: 
        """
        Returns false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
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
class BOPAlgo_Options():
    """
    The class provides the following options for the algorithms in Boolean Component: - *Memory allocation tool* - tool for memory allocations; - *Error and warning reporting* - allows recording warnings and errors occurred during the operation. Error means that the algorithm has failed. - *Parallel processing mode* - provides the possibility to perform operation in parallel mode; - *Fuzzy tolerance* - additional tolerance for the operation to detect touching or coinciding cases; - *Progress indicator* - provides interface to track the progress of operation and stop the operation by user's break. - *Using the Oriented Bounding Boxes* - Allows using the Oriented Bounding Boxes of the shapes for filtering the intersections.
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
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
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
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPAlgo_Algo(BOPAlgo_Options):
    """
    The class provides the root interface for the algorithms in Boolean Component.
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
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
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
    def Perform(self) -> None: 
        """
        None
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
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
    pass
class BOPAlgo_BuilderShape(BOPAlgo_Algo, BOPAlgo_Options):
    """
    Root class for algorithms that has shape as result.
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
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
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
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
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
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def Perform(self) -> None: 
        """
        None
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    pass
class BOPAlgo_Builder(BOPAlgo_BuilderShape, BOPAlgo_Algo, BOPAlgo_Options):
    """
    The class is a General Fuse algorithm - base algorithm for the algorithms in the Boolean Component. Its main purpose is to build the split parts of the argument shapes from which the result of the operations is combined. The result of the General Fuse algorithm itself is a compound containing all split parts of the arguments.
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument to the operation.
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
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments.
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theObjState : OCP.TopAbs.TopAbs_State,theTools : OCP.TopTools.TopTools_ListOfShape,theToolsState : OCP.TopAbs.TopAbs_State,theReport : OCP.Message.Message_Report) -> None: 
        """
        Builds the result shape according to the given states for the objects and tools. These states can be unambiguously converted into the Boolean operation type. Thus, it performs the Boolean operation on the given groups of shapes.

        Builds the result of Boolean operation of given type basing on the result of Builder operation (GF or any other).
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theTools : OCP.TopTools.TopTools_ListOfShape,theOperation : BOPAlgo_Operation,theReport : OCP.Message.Message_Report) -> None: ...
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the algorithm.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the Context, tool for cashing heavy algorithms.
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
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
    def Glue(self) -> BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
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
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def Images(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of images.
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Origins(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of origins.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        Returns the Data Structure, holder of intersection information.
        """
    def PPaveFiller(self) -> BOPAlgo_PaveFiller: 
        """
        Returns the PaveFiller, algorithm for sub-shapes intersection.
        """
    def Perform(self) -> None: 
        """
        Performs the operation. The intersection will be performed also.
        """
    def PerformWithFiller(self,theFiller : BOPAlgo_PaveFiller) -> None: 
        """
        Performs the operation with the prepared filler. The intersection will not be performed in this case.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the list of arguments for the operation.
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated. This flag is taken into account if internal PaveFiller is used only. In the case of calling PerformWithFiller the corresponding flag of that PaveFiller is in force.
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def ShapesSD(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes from different arguments.
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPAlgo_BuilderArea(BOPAlgo_Algo, BOPAlgo_Options):
    """
    The root class for algorithms to build faces/solids from set of edges/faces
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
    def Areas(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the found areas
        """
    def Clear(self) -> None: 
        """
        Clears all warnings and errors, and any data cached by the algorithm. User defined options are not cleared.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
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
    def IsAvoidInternalShapes(self) -> bool: 
        """
        Returns the AvoidInternalShapes flag
        """
    def Loops(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the found loops
        """
    def Perform(self) -> None: 
        """
        None
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetAvoidInternalShapes(self,theAvoidInternal : bool) -> None: 
        """
        Defines the preventing of addition of internal parts into result. The default value is FALSE, i.e. the internal parts are added into result.
        """
    def SetContext(self,theContext : OCP.IntTools.IntTools_Context) -> None: 
        """
        Sets the context for the algorithms
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetShapes(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the shapes for building areas
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shapes(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the input shapes
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    pass
class BOPAlgo_BuilderFace(BOPAlgo_BuilderArea, BOPAlgo_Algo, BOPAlgo_Options):
    """
    The algorithm to build new faces from the given faces and set of edges lying on this face.
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
    def Areas(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the found areas
        """
    def Clear(self) -> None: 
        """
        Clears all warnings and errors, and any data cached by the algorithm. User defined options are not cleared.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the face generatix
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
    def IsAvoidInternalShapes(self) -> bool: 
        """
        Returns the AvoidInternalShapes flag
        """
    def Loops(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the found loops
        """
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Perform(self) -> None: 
        """
        Performs the algorithm
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetAvoidInternalShapes(self,theAvoidInternal : bool) -> None: 
        """
        Defines the preventing of addition of internal parts into result. The default value is FALSE, i.e. the internal parts are added into result.
        """
    def SetContext(self,theContext : OCP.IntTools.IntTools_Context) -> None: 
        """
        Sets the context for the algorithms
        """
    def SetFace(self,theFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Sets the face generatix
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetShapes(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the shapes for building areas
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shapes(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the input shapes
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPAlgo_ToolsProvider(BOPAlgo_Builder, BOPAlgo_BuilderShape, BOPAlgo_Algo, BOPAlgo_Options):
    """
    Auxiliary class providing API to operate tool arguments.
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument to the operation.
        """
    def AddError(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as error (fail)
        """
    def AddTool(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds Tool argument of the operation
        """
    def AddWarning(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as warning
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns allocator
        """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments.
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theObjState : OCP.TopAbs.TopAbs_State,theTools : OCP.TopTools.TopTools_ListOfShape,theToolsState : OCP.TopAbs.TopAbs_State,theReport : OCP.Message.Message_Report) -> None: 
        """
        Builds the result shape according to the given states for the objects and tools. These states can be unambiguously converted into the Boolean operation type. Thus, it performs the Boolean operation on the given groups of shapes.

        Builds the result of Boolean operation of given type basing on the result of Builder operation (GF or any other).
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theTools : OCP.TopTools.TopTools_ListOfShape,theOperation : BOPAlgo_Operation,theReport : OCP.Message.Message_Report) -> None: ...
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def Clear(self) -> None: 
        """
        Clears internal fields and arguments
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the Context, tool for cashing heavy algorithms.
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
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
    def Glue(self) -> BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
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
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def Images(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of images.
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Origins(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of origins.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        Returns the Data Structure, holder of intersection information.
        """
    def PPaveFiller(self) -> BOPAlgo_PaveFiller: 
        """
        Returns the PaveFiller, algorithm for sub-shapes intersection.
        """
    def Perform(self) -> None: 
        """
        Performs the operation. The intersection will be performed also.
        """
    def PerformWithFiller(self,theFiller : BOPAlgo_PaveFiller) -> None: 
        """
        Performs the operation with the prepared filler. The intersection will not be performed in this case.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the list of arguments for the operation.
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated. This flag is taken into account if internal PaveFiller is used only. In the case of calling PerformWithFiller the corresponding flag of that PaveFiller is in force.
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theShapes : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Adds the Tool arguments of the operation
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def ShapesSD(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes from different arguments.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tool arguments of the operation
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPAlgo_BuilderSolid(BOPAlgo_BuilderArea, BOPAlgo_Algo, BOPAlgo_Options):
    """
    Solid Builder is the algorithm for building solids from set of faces. The given faces should be non-intersecting, i.e. all coinciding parts of the faces should be shared among them.
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
    def Areas(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the found areas
        """
    def Clear(self) -> None: 
        """
        Clears all warnings and errors, and any data cached by the algorithm. User defined options are not cleared.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def GetBoxesMap(self) -> OCP.TopTools.TopTools_DataMapOfShapeBox: 
        """
        For classification purposes the algorithm builds the bounding boxes for all created solids. This method returns the data map of solid - box pairs.
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
    def IsAvoidInternalShapes(self) -> bool: 
        """
        Returns the AvoidInternalShapes flag
        """
    def Loops(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the found loops
        """
    def Perform(self) -> None: 
        """
        Performs the construction of the solids from the given faces
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetAvoidInternalShapes(self,theAvoidInternal : bool) -> None: 
        """
        Defines the preventing of addition of internal parts into result. The default value is FALSE, i.e. the internal parts are added into result.
        """
    def SetContext(self,theContext : OCP.IntTools.IntTools_Context) -> None: 
        """
        Sets the context for the algorithms
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetShapes(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the shapes for building areas
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shapes(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the input shapes
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPAlgo_CellsBuilder(BOPAlgo_Builder, BOPAlgo_BuilderShape, BOPAlgo_Algo, BOPAlgo_Options):
    """
    The algorithm is based on the General Fuse algorithm (GFA). The result of GFA is all split parts of the Arguments.
    """
    def AddAllToResult(self,theMaterial : int=0,theUpdate : bool=False) -> None: 
        """
        Add all split parts to result. <theMaterial> defines the removal of internal boundaries; <theUpdate> parameter defines whether to remove boundaries now or not.
        """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument to the operation.
        """
    def AddError(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as error (fail)
        """
    def AddToResult(self,theLSToTake : OCP.TopTools.TopTools_ListOfShape,theLSToAvoid : OCP.TopTools.TopTools_ListOfShape,theMaterial : int=0,theUpdate : bool=False) -> None: 
        """
        Adding the parts to result. The parts are defined by two lists of shapes: <theLSToTake> defines the arguments which parts should be taken into result; <theLSToAvoid> defines the arguments which parts should not be taken into result; To be taken into result the part must be IN for all shapes from the list <theLSToTake> and must be OUT of all shapes from the list <theLSToAvoid>.
        """
    def AddWarning(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as warning
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns allocator
        """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments.
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theObjState : OCP.TopAbs.TopAbs_State,theTools : OCP.TopTools.TopTools_ListOfShape,theToolsState : OCP.TopAbs.TopAbs_State,theReport : OCP.Message.Message_Report) -> None: 
        """
        Builds the result shape according to the given states for the objects and tools. These states can be unambiguously converted into the Boolean operation type. Thus, it performs the Boolean operation on the given groups of shapes.

        Builds the result of Boolean operation of given type basing on the result of Builder operation (GF or any other).
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theTools : OCP.TopTools.TopTools_ListOfShape,theOperation : BOPAlgo_Operation,theReport : OCP.Message.Message_Report) -> None: ...
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def Clear(self) -> None: 
        """
        Redefined method Clear - clears the contents.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the Context, tool for cashing heavy algorithms.
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
        """
    def GetAllParts(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Get all split parts.
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
    def Glue(self) -> BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
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
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def Images(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of images.
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def MakeContainers(self) -> None: 
        """
        Makes the Containers of proper type from the parts added to result.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Origins(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of origins.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        Returns the Data Structure, holder of intersection information.
        """
    def PPaveFiller(self) -> BOPAlgo_PaveFiller: 
        """
        Returns the PaveFiller, algorithm for sub-shapes intersection.
        """
    def Perform(self) -> None: 
        """
        Performs the operation. The intersection will be performed also.
        """
    def PerformWithFiller(self,theFiller : BOPAlgo_PaveFiller) -> None: 
        """
        Performs the operation with the prepared filler. The intersection will not be performed in this case.
        """
    def RemoveAllFromResult(self) -> None: 
        """
        Remove all parts from result.
        """
    def RemoveFromResult(self,theLSToTake : OCP.TopTools.TopTools_ListOfShape,theLSToAvoid : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Removing the parts from result. The parts are defined by two lists of shapes: <theLSToTake> defines the arguments which parts should be removed from result; <theLSToAvoid> defines the arguments which parts should not be removed from result. To be removed from the result the part must be IN for all shapes from the list <theLSToTake> and must be OUT of all shapes from the list <theLSToAvoid>.
        """
    def RemoveInternalBoundaries(self) -> None: 
        """
        Removes internal boundaries between cells with the same material. If the result contains the cells with same material but of different dimension the removal of internal boundaries between these cells will not be performed. In case of some errors during the removal the method will set the appropriate warning status - use GetReport() to access them.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the list of arguments for the operation.
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated. This flag is taken into account if internal PaveFiller is used only. In the case of calling PerformWithFiller the corresponding flag of that PaveFiller is in force.
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def ShapesSD(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes from different arguments.
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPAlgo_CheckResult():
    """
    contains information about faulty shapes and faulty types can't be processed by Boolean Operations
    """
    def AddFaultyShape1(self,TheShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        adds faulty sub-shapes from object to a list
        """
    def AddFaultyShape2(self,TheShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        adds faulty sub-shapes from tool to a list
        """
    def GetCheckStatus(self) -> BOPAlgo_CheckStatus: 
        """
        gets status of faulty
        """
    def GetFaultyShapes1(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns list of faulty shapes for object
        """
    def GetFaultyShapes2(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns list of faulty shapes for tool
        """
    def GetMaxDistance1(self) -> float: 
        """
        Returns the distance for the first shape
        """
    def GetMaxDistance2(self) -> float: 
        """
        Returns the distance for the second shape
        """
    def GetMaxParameter1(self) -> float: 
        """
        Returns the parameter for the fircst shape
        """
    def GetMaxParameter2(self) -> float: 
        """
        Returns the parameter for the second shape
        """
    def GetShape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns ancestor shape (object) for faulties
        """
    def GetShape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns ancestor shape (tool) for faulties
        """
    def SetCheckStatus(self,TheStatus : BOPAlgo_CheckStatus) -> None: 
        """
        set status of faulty
        """
    def SetMaxDistance1(self,theDist : float) -> None: 
        """
        Sets max distance for the first shape
        """
    def SetMaxDistance2(self,theDist : float) -> None: 
        """
        Sets max distance for the second shape
        """
    def SetMaxParameter1(self,thePar : float) -> None: 
        """
        Sets the parameter for the first shape
        """
    def SetMaxParameter2(self,thePar : float) -> None: 
        """
        Sets the parameter for the second shape
        """
    def SetShape1(self,TheShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        sets ancestor shape (object) for faulty sub-shapes
        """
    def SetShape2(self,TheShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        sets ancestor shape (tool) for faulty sub-shapes
        """
    def __init__(self) -> None: ...
    pass
class BOPAlgo_CheckStatus():
    """
    None

    Members:

      BOPAlgo_CheckUnknown

      BOPAlgo_BadType

      BOPAlgo_SelfIntersect

      BOPAlgo_TooSmallEdge

      BOPAlgo_NonRecoverableFace

      BOPAlgo_IncompatibilityOfVertex

      BOPAlgo_IncompatibilityOfEdge

      BOPAlgo_IncompatibilityOfFace

      BOPAlgo_OperationAborted

      BOPAlgo_GeomAbs_C0

      BOPAlgo_InvalidCurveOnSurface

      BOPAlgo_NotValid
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BOPAlgo_BadType: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_BadType
    BOPAlgo_CheckUnknown: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_CheckUnknown
    BOPAlgo_GeomAbs_C0: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_GeomAbs_C0
    BOPAlgo_IncompatibilityOfEdge: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfEdge
    BOPAlgo_IncompatibilityOfFace: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfFace
    BOPAlgo_IncompatibilityOfVertex: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfVertex
    BOPAlgo_InvalidCurveOnSurface: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_InvalidCurveOnSurface
    BOPAlgo_NonRecoverableFace: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_NonRecoverableFace
    BOPAlgo_NotValid: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_NotValid
    BOPAlgo_OperationAborted: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_OperationAborted
    BOPAlgo_SelfIntersect: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_SelfIntersect
    BOPAlgo_TooSmallEdge: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_TooSmallEdge
    __entries: dict # value = {'BOPAlgo_CheckUnknown': (BOPAlgo_CheckStatus.BOPAlgo_CheckUnknown, None), 'BOPAlgo_BadType': (BOPAlgo_CheckStatus.BOPAlgo_BadType, None), 'BOPAlgo_SelfIntersect': (BOPAlgo_CheckStatus.BOPAlgo_SelfIntersect, None), 'BOPAlgo_TooSmallEdge': (BOPAlgo_CheckStatus.BOPAlgo_TooSmallEdge, None), 'BOPAlgo_NonRecoverableFace': (BOPAlgo_CheckStatus.BOPAlgo_NonRecoverableFace, None), 'BOPAlgo_IncompatibilityOfVertex': (BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfVertex, None), 'BOPAlgo_IncompatibilityOfEdge': (BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfEdge, None), 'BOPAlgo_IncompatibilityOfFace': (BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfFace, None), 'BOPAlgo_OperationAborted': (BOPAlgo_CheckStatus.BOPAlgo_OperationAborted, None), 'BOPAlgo_GeomAbs_C0': (BOPAlgo_CheckStatus.BOPAlgo_GeomAbs_C0, None), 'BOPAlgo_InvalidCurveOnSurface': (BOPAlgo_CheckStatus.BOPAlgo_InvalidCurveOnSurface, None), 'BOPAlgo_NotValid': (BOPAlgo_CheckStatus.BOPAlgo_NotValid, None)}
    __members__: dict # value = {'BOPAlgo_CheckUnknown': BOPAlgo_CheckStatus.BOPAlgo_CheckUnknown, 'BOPAlgo_BadType': BOPAlgo_CheckStatus.BOPAlgo_BadType, 'BOPAlgo_SelfIntersect': BOPAlgo_CheckStatus.BOPAlgo_SelfIntersect, 'BOPAlgo_TooSmallEdge': BOPAlgo_CheckStatus.BOPAlgo_TooSmallEdge, 'BOPAlgo_NonRecoverableFace': BOPAlgo_CheckStatus.BOPAlgo_NonRecoverableFace, 'BOPAlgo_IncompatibilityOfVertex': BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfVertex, 'BOPAlgo_IncompatibilityOfEdge': BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfEdge, 'BOPAlgo_IncompatibilityOfFace': BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfFace, 'BOPAlgo_OperationAborted': BOPAlgo_CheckStatus.BOPAlgo_OperationAborted, 'BOPAlgo_GeomAbs_C0': BOPAlgo_CheckStatus.BOPAlgo_GeomAbs_C0, 'BOPAlgo_InvalidCurveOnSurface': BOPAlgo_CheckStatus.BOPAlgo_InvalidCurveOnSurface, 'BOPAlgo_NotValid': BOPAlgo_CheckStatus.BOPAlgo_NotValid}
    pass
class BOPAlgo_PaveFiller(BOPAlgo_Algo, BOPAlgo_Options):
    """
    The class represents the Intersection phase of the Boolean Operations algorithm. It performs the pairwise intersection of the sub-shapes of the arguments in the following order: 1. Vertex/Vertex; 2. Vertex/Edge; 3. Edge/Edge; 4. Vertex/Face; 5. Edge/Face; 6. Face/Face.
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument for operation
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
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments
        """
    def Clear(self) -> None: 
        """
        Clears all warnings and errors, and any data cached by the algorithm. User defined options are not cleared.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        None
        """
    def DS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        None
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
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
    def Glue(self) -> BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
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
    def IsAvoidBuildPCurve(self) -> bool: 
        """
        Returns the flag to avoid building of p-curves of edges on faces
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        None
        """
    def Perform(self) -> None: 
        """
        None
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the arguments for operation
        """
    def SetAvoidBuildPCurve(self,theValue : bool) -> None: 
        """
        Sets the flag to avoid building of p-curves of edges on faces
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetSectionAttribute(self,theSecAttr : BOPAlgo_SectionAttribute) -> None: 
        """
        None
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPAlgo_EdgeInfo():
    """
    None
    """
    def Angle(self) -> float: 
        """
        None
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def IsIn(self) -> bool: 
        """
        None
        """
    def Passed(self) -> bool: 
        """
        None
        """
    def SetAngle(self,theAngle : float) -> None: 
        """
        None
        """
    def SetEdge(self,theE : OCP.TopoDS.TopoDS_Edge) -> None: 
        """
        None
        """
    def SetInFlag(self,theFlag : bool) -> None: 
        """
        None
        """
    def SetPassed(self,theFlag : bool) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BOPAlgo_GlueEnum():
    """
    The Enumeration describes an additional option for the algorithms in the Boolean Component such as General Fuse, Boolean operations, Section, Maker Volume, Splitter and Cells Builder algorithms.

    Members:

      BOPAlgo_GlueOff

      BOPAlgo_GlueShift

      BOPAlgo_GlueFull
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BOPAlgo_GlueFull: OCP.BOPAlgo.BOPAlgo_GlueEnum # value = BOPAlgo_GlueEnum.BOPAlgo_GlueFull
    BOPAlgo_GlueOff: OCP.BOPAlgo.BOPAlgo_GlueEnum # value = BOPAlgo_GlueEnum.BOPAlgo_GlueOff
    BOPAlgo_GlueShift: OCP.BOPAlgo.BOPAlgo_GlueEnum # value = BOPAlgo_GlueEnum.BOPAlgo_GlueShift
    __entries: dict # value = {'BOPAlgo_GlueOff': (BOPAlgo_GlueEnum.BOPAlgo_GlueOff, None), 'BOPAlgo_GlueShift': (BOPAlgo_GlueEnum.BOPAlgo_GlueShift, None), 'BOPAlgo_GlueFull': (BOPAlgo_GlueEnum.BOPAlgo_GlueFull, None)}
    __members__: dict # value = {'BOPAlgo_GlueOff': BOPAlgo_GlueEnum.BOPAlgo_GlueOff, 'BOPAlgo_GlueShift': BOPAlgo_GlueEnum.BOPAlgo_GlueShift, 'BOPAlgo_GlueFull': BOPAlgo_GlueEnum.BOPAlgo_GlueFull}
    pass
class BOPAlgo_IndexedDataMapOfShapeListOfEdgeInfo(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : BOPAlgo_ListOfEdgeInfo) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPAlgo_IndexedDataMapOfShapeListOfEdgeInfo) -> BOPAlgo_IndexedDataMapOfShapeListOfEdgeInfo: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> BOPAlgo_ListOfEdgeInfo: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> BOPAlgo_ListOfEdgeInfo: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> BOPAlgo_ListOfEdgeInfo: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : BOPAlgo_IndexedDataMapOfShapeListOfEdgeInfo) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> BOPAlgo_ListOfEdgeInfo: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> BOPAlgo_ListOfEdgeInfo: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : BOPAlgo_ListOfEdgeInfo) -> bool: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindKey
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
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> BOPAlgo_ListOfEdgeInfo: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : BOPAlgo_ListOfEdgeInfo) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPAlgo_IndexedDataMapOfShapeListOfEdgeInfo) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BOPAlgo_ListOfCheckResult(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BOPAlgo_CheckResult,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : BOPAlgo_ListOfCheckResult) -> None: ...
    @overload
    def Append(self,theItem : BOPAlgo_CheckResult) -> BOPAlgo_CheckResult: ...
    def Assign(self,theOther : BOPAlgo_ListOfCheckResult) -> BOPAlgo_ListOfCheckResult: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> BOPAlgo_CheckResult: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : BOPAlgo_CheckResult,theIter : Any) -> BOPAlgo_CheckResult: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : BOPAlgo_ListOfCheckResult,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : BOPAlgo_ListOfCheckResult,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : BOPAlgo_CheckResult,theIter : Any) -> BOPAlgo_CheckResult: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BOPAlgo_CheckResult: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : BOPAlgo_CheckResult) -> BOPAlgo_CheckResult: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : BOPAlgo_ListOfCheckResult) -> None: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BOPAlgo_ListOfCheckResult) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BOPAlgo_ListOfEdgeInfo(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : BOPAlgo_ListOfEdgeInfo) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : BOPAlgo_EdgeInfo) -> BOPAlgo_EdgeInfo: ...
    @overload
    def Append(self,theItem : BOPAlgo_EdgeInfo,theIter : Any) -> None: ...
    def Assign(self,theOther : BOPAlgo_ListOfEdgeInfo) -> BOPAlgo_ListOfEdgeInfo: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> BOPAlgo_EdgeInfo: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : BOPAlgo_ListOfEdgeInfo,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : BOPAlgo_EdgeInfo,theIter : Any) -> BOPAlgo_EdgeInfo: ...
    @overload
    def InsertBefore(self,theItem : BOPAlgo_EdgeInfo,theIter : Any) -> BOPAlgo_EdgeInfo: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : BOPAlgo_ListOfEdgeInfo,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BOPAlgo_EdgeInfo: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : BOPAlgo_ListOfEdgeInfo) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : BOPAlgo_EdgeInfo) -> BOPAlgo_EdgeInfo: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : BOPAlgo_ListOfEdgeInfo) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class BOPAlgo_MakeConnected(BOPAlgo_Options):
    """
    BOPAlgo_MakeConnected is the algorithm for making the touching shapes connected or glued, i.e. for making the coinciding geometries be topologically shared among the shapes.
    """
    def AddArgument(self,theS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the shape to the arguments.
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
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments of the operation.
        """
    def Clear(self) -> None: 
        """
        Clears the contents of the algorithm.
        """
    def ClearRepetitions(self) -> None: 
        """
        Clears the repetitions performed on the periodic shape, keeping the shape periodic.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def GetModified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the given shape.
        """
    def GetOrigins(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of original shapes from which the current shape has been created.
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
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        Returns the history of operations
        """
    def MakePeriodic(self,theParams : Any) -> None: 
        """
        Makes the connected shape periodic. Repeated calls of this method overwrite the previous calls working with the basis connected shape.
        """
    def MaterialsOnNegativeSide(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the original shapes which images contain the the given shape with REVERSED orientation.
        """
    def MaterialsOnPositiveSide(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the original shapes which images contain the the given shape with FORWARD orientation.
        """
    def Perform(self) -> None: 
        """
        Performs the operation, i.e. makes the input shapes connected.
        """
    def PeriodicShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the resulting periodic & repeated shape
        """
    def PeriodicityTool(self) -> BOPAlgo_MakePeriodic: 
        """
        Returns the periodicity tool.
        """
    def RepeatShape(self,theDirectionID : int,theTimes : int) -> None: 
        """
        Performs repetition of the periodic shape in specified direction required number of times.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theArgs : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the shape for making them connected.
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the resulting connected shape
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    def __init__(self) -> None: ...
    pass
class BOPAlgo_MakePeriodic(BOPAlgo_Options):
    """
    BOPAlgo_MakePeriodic is the tool for making an arbitrary shape periodic in 3D space in specified directions.
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
        Clears the algorithm from previous runs
        """
    def ClearRepetitions(self) -> None: 
        """
        Clears all performed repetitions. The next repetition will be performed on the base shape.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
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
    def GetTwins(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the identical shapes for the given shape located on the opposite periodic side. Returns empty list in case the shape has no twin.
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
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        Returns the History of the algorithm
        """
    def IsInputTrimmed(self,theDirectionID : int) -> bool: 
        """
        Returns whether the input shape was trimmed in the specified direction.
        """
    def IsInputXTrimmed(self) -> bool: 
        """
        Returns whether the input shape was already trimmed for X period.
        """
    def IsInputYTrimmed(self) -> bool: 
        """
        Returns whether the input shape was already trimmed for Y period.
        """
    def IsInputZTrimmed(self) -> bool: 
        """
        Returns whether the input shape was already trimmed for Z period.
        """
    def IsPeriodic(self,theDirectionID : int) -> bool: 
        """
        Returns the info about Periodicity of the shape in specified direction.
        """
    def IsXPeriodic(self) -> bool: 
        """
        Returns the info about periodicity of the shape in X direction.
        """
    def IsYPeriodic(self) -> bool: 
        """
        Returns the info about periodicity of the shape in Y direction.
        """
    def IsZPeriodic(self) -> bool: 
        """
        Returns the info about periodicity of the shape in Z direction.
        """
    def MakePeriodic(self,theDirectionID : int,theIsPeriodic : bool,thePeriod : float=0.0) -> None: 
        """
        Sets the flag to make the shape periodic in specified direction: - 0 - X direction; - 1 - Y direction; - 2 - Z direction.
        """
    def MakeXPeriodic(self,theIsPeriodic : bool,thePeriod : float=0.0) -> None: 
        """
        Sets the flag to make the shape periodic in X direction.
        """
    def MakeYPeriodic(self,theIsPeriodic : bool,thePeriod : float=0.0) -> None: 
        """
        Sets the flag to make the shape periodic in Y direction.
        """
    def MakeZPeriodic(self,theIsPeriodic : bool,thePeriod : float=0.0) -> None: 
        """
        Sets the flag to make the shape periodic in Z direction.
        """
    def Perform(self) -> None: 
        """
        Makes the shape periodic in necessary directions
        """
    def Period(self,theDirectionID : int) -> float: 
        """
        Returns the Period of the shape in specified direction.
        """
    def PeriodFirst(self,theDirectionID : int) -> float: 
        """
        Returns the first periodic parameter in the specified direction.
        """
    def PeriodicityParameters(self) -> Any: 
        """
        None
        """
    def RepeatShape(self,theDirectionID : int,theTimes : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Performs repetition of the shape in specified direction required number of times. Negative value of times means that the repetition should be perform in negative direction. Makes the repeated shape a base for following repetitions.
        """
    def RepeatedShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the repeated shape
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetPeriodicityParameters(self,theParams : Any) -> None: 
        """
        Sets the periodicity parameters.
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape to make it periodic.
        """
    def SetTrimmed(self,theDirectionID : int,theIsTrimmed : bool,theFirst : float=0.0) -> None: 
        """
        Defines whether the input shape is already trimmed in specified direction to fit the period in this direction. Direction is defined by an ID: - 0 - X direction; - 1 - Y direction; - 2 - Z direction.
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def SetXTrimmed(self,theIsTrimmed : bool,theFirst : bool=False) -> None: 
        """
        Defines whether the input shape is already trimmed in X direction to fit the X period. If the shape is not trimmed it is required to set the first parameter for the X period. The algorithm will make the shape fit into the period.
        """
    def SetYTrimmed(self,theIsTrimmed : bool,theFirst : bool=False) -> None: 
        """
        Defines whether the input shape is already trimmed in Y direction to fit the Y period. If the shape is not trimmed it is required to set the first parameter for the Y period. The algorithm will make the shape fit into the period.
        """
    def SetZTrimmed(self,theIsTrimmed : bool,theFirst : bool=False) -> None: 
        """
        Defines whether the input shape is already trimmed in Z direction to fit the Z period. If the shape is not trimmed it is required to set the first parameter for the Z period. The algorithm will make the shape fit into the period.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the resulting periodic shape
        """
    @staticmethod
    def ToDirectionID_s(theDirectionID : int) -> int: 
        """
        Converts the integer to ID of periodic direction
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    def XPeriod(self) -> float: 
        """
        Returns the XPeriod of the shape
        """
    def XPeriodFirst(self) -> float: 
        """
        Returns the first parameter for the X period.
        """
    def XRepeat(self,theTimes : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Repeats the shape in X direction specified number of times. Negative value of times means that the repetition should be perform in negative X direction. Makes the repeated shape a base for following repetitions.
        """
    def YPeriod(self) -> float: 
        """
        Returns the YPeriod of the shape.
        """
    def YPeriodFirst(self) -> float: 
        """
        Returns the first parameter for the Y period.
        """
    def YRepeat(self,theTimes : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Repeats the shape in Y direction specified number of times. Negative value of times means that the repetition should be perform in negative Y direction. Makes the repeated shape a base for following repetitions.
        """
    def ZPeriod(self) -> float: 
        """
        Returns the ZPeriod of the shape.
        """
    def ZPeriodFirst(self) -> float: 
        """
        Returns the first parameter for the Z period.
        """
    def ZRepeat(self,theTimes : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Repeats the shape in Z direction specified number of times. Negative value of times means that the repetition should be perform in negative Z direction. Makes the repeated shape a base for following repetitions.
        """
    def __init__(self) -> None: ...
    pass
class BOPAlgo_MakerVolume(BOPAlgo_Builder, BOPAlgo_BuilderShape, BOPAlgo_Algo, BOPAlgo_Options):
    """
    The algorithm is to build solids from set of shapes. It uses the BOPAlgo_Builder algorithm to intersect the given shapes and build the images of faces (if needed) and BOPAlgo_BuilderSolid algorithm to build the solids.
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument to the operation.
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
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments.
        """
    def Box(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the solid box <mySBox>.

        Returns the solid box <mySBox>.
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theObjState : OCP.TopAbs.TopAbs_State,theTools : OCP.TopTools.TopTools_ListOfShape,theToolsState : OCP.TopAbs.TopAbs_State,theReport : OCP.Message.Message_Report) -> None: 
        """
        Builds the result shape according to the given states for the objects and tools. These states can be unambiguously converted into the Boolean operation type. Thus, it performs the Boolean operation on the given groups of shapes.

        Builds the result of Boolean operation of given type basing on the result of Builder operation (GF or any other).
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theTools : OCP.TopTools.TopTools_ListOfShape,theOperation : BOPAlgo_Operation,theReport : OCP.Message.Message_Report) -> None: ...
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def Clear(self) -> None: 
        """
        Clears the data.

        Clears the data.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the Context, tool for cashing heavy algorithms.
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def Faces(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the processed faces <myFaces>.

        Returns the processed faces <myFaces>.
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
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
    def Glue(self) -> BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
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
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def Images(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of images.
        """
    def IsAvoidInternalShapes(self) -> bool: 
        """
        Returns the AvoidInternalShapes flag
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def IsIntersect(self) -> bool: 
        """
        Returns the flag <myIntersect>.

        Returns the flag <myIntersect>.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Origins(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of origins.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        Returns the Data Structure, holder of intersection information.
        """
    def PPaveFiller(self) -> BOPAlgo_PaveFiller: 
        """
        Returns the PaveFiller, algorithm for sub-shapes intersection.
        """
    def Perform(self) -> None: 
        """
        Performs the operation.
        """
    def PerformWithFiller(self,theFiller : BOPAlgo_PaveFiller) -> None: 
        """
        Performs the operation with the prepared filler. The intersection will not be performed in this case.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the list of arguments for the operation.
        """
    def SetAvoidInternalShapes(self,theAvoidInternal : bool) -> None: 
        """
        Defines the preventing of addition of internal for solid parts into the result. By default the internal parts are added into result.
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetIntersect(self,bIntersect : bool) -> None: 
        """
        Sets the flag myIntersect: if <bIntersect> is TRUE the shapes from <myArguments> will be intersected. if <bIntersect> is FALSE no intersection will be done.

        Sets the flag myIntersect: if <bIntersect> is TRUE the shapes from <myArguments> will be intersected. if <bIntersect> is FALSE no intersection will be done.
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated. This flag is taken into account if internal PaveFiller is used only. In the case of calling PerformWithFiller the corresponding flag of that PaveFiller is in force.
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def ShapesSD(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes from different arguments.
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPAlgo_Operation():
    """
    None

    Members:

      BOPAlgo_COMMON

      BOPAlgo_FUSE

      BOPAlgo_CUT

      BOPAlgo_CUT21

      BOPAlgo_SECTION

      BOPAlgo_UNKNOWN
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    BOPAlgo_COMMON: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_COMMON
    BOPAlgo_CUT: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_CUT
    BOPAlgo_CUT21: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_CUT21
    BOPAlgo_FUSE: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_FUSE
    BOPAlgo_SECTION: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_SECTION
    BOPAlgo_UNKNOWN: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_UNKNOWN
    __entries: dict # value = {'BOPAlgo_COMMON': (BOPAlgo_Operation.BOPAlgo_COMMON, None), 'BOPAlgo_FUSE': (BOPAlgo_Operation.BOPAlgo_FUSE, None), 'BOPAlgo_CUT': (BOPAlgo_Operation.BOPAlgo_CUT, None), 'BOPAlgo_CUT21': (BOPAlgo_Operation.BOPAlgo_CUT21, None), 'BOPAlgo_SECTION': (BOPAlgo_Operation.BOPAlgo_SECTION, None), 'BOPAlgo_UNKNOWN': (BOPAlgo_Operation.BOPAlgo_UNKNOWN, None)}
    __members__: dict # value = {'BOPAlgo_COMMON': BOPAlgo_Operation.BOPAlgo_COMMON, 'BOPAlgo_FUSE': BOPAlgo_Operation.BOPAlgo_FUSE, 'BOPAlgo_CUT': BOPAlgo_Operation.BOPAlgo_CUT, 'BOPAlgo_CUT21': BOPAlgo_Operation.BOPAlgo_CUT21, 'BOPAlgo_SECTION': BOPAlgo_Operation.BOPAlgo_SECTION, 'BOPAlgo_UNKNOWN': BOPAlgo_Operation.BOPAlgo_UNKNOWN}
    pass
class BOPAlgo_ArgumentAnalyzer(BOPAlgo_Algo, BOPAlgo_Options):
    """
    check the validity of argument(s) for Boolean Operations
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
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def GetCheckResult(self) -> BOPAlgo_ListOfCheckResult: 
        """
        returns a result of test
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
    def GetShape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns object shape;
        """
    def GetShape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns tool shape
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
        """
    def HasFaulty(self) -> bool: 
        """
        result of test
        """
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def OperationType(self) -> BOPAlgo_Operation: 
        """
        returns ref
        """
    def Perform(self) -> None: 
        """
        performs analysis
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetShape1(self,TheShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        sets object shape
        """
    def SetShape2(self,TheShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        sets tool shape
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    def __init__(self) -> None: ...
    @property
    def ArgumentTypeMode(self) -> bool:
        """
        :type: bool
        """
    @ArgumentTypeMode.setter
    def ArgumentTypeMode(self, arg1: bool) -> None:
        pass
    @property
    def ContinuityMode(self) -> bool:
        """
        :type: bool
        """
    @ContinuityMode.setter
    def ContinuityMode(self, arg1: bool) -> None:
        pass
    @property
    def CurveOnSurfaceMode(self) -> bool:
        """
        :type: bool
        """
    @CurveOnSurfaceMode.setter
    def CurveOnSurfaceMode(self, arg1: bool) -> None:
        pass
    @property
    def MergeEdgeMode(self) -> bool:
        """
        :type: bool
        """
    @MergeEdgeMode.setter
    def MergeEdgeMode(self, arg1: bool) -> None:
        pass
    @property
    def MergeVertexMode(self) -> bool:
        """
        :type: bool
        """
    @MergeVertexMode.setter
    def MergeVertexMode(self, arg1: bool) -> None:
        pass
    @property
    def RebuildFaceMode(self) -> bool:
        """
        :type: bool
        """
    @RebuildFaceMode.setter
    def RebuildFaceMode(self, arg1: bool) -> None:
        pass
    @property
    def SelfInterMode(self) -> bool:
        """
        :type: bool
        """
    @SelfInterMode.setter
    def SelfInterMode(self, arg1: bool) -> None:
        pass
    @property
    def SmallEdgeMode(self) -> bool:
        """
        :type: bool
        """
    @SmallEdgeMode.setter
    def SmallEdgeMode(self, arg1: bool) -> None:
        pass
    @property
    def StopOnFirstFaulty(self) -> bool:
        """
        :type: bool
        """
    @StopOnFirstFaulty.setter
    def StopOnFirstFaulty(self, arg1: bool) -> None:
        pass
    @property
    def TangentMode(self) -> bool:
        """
        :type: bool
        """
    @TangentMode.setter
    def TangentMode(self, arg1: bool) -> None:
        pass
    pass
class BOPAlgo_CheckerSI(BOPAlgo_PaveFiller, BOPAlgo_Algo, BOPAlgo_Options):
    """
    Checks the shape on self-interference.
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument for operation
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
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments
        """
    def Clear(self) -> None: 
        """
        Clears all warnings and errors, and any data cached by the algorithm. User defined options are not cleared.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        None
        """
    def DS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        None
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
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
    def Glue(self) -> BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
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
    def IsAvoidBuildPCurve(self) -> bool: 
        """
        Returns the flag to avoid building of p-curves of edges on faces
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        None
        """
    def Perform(self) -> None: 
        """
        None
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the arguments for operation
        """
    def SetAvoidBuildPCurve(self,theValue : bool) -> None: 
        """
        Sets the flag to avoid building of p-curves of edges on faces
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetLevelOfCheck(self,theLevel : int) -> None: 
        """
        Sets the level of checking shape on self-interference. It defines which interferences will be checked: 0 - only V/V; 1 - V/V and V/E; 2 - V/V, V/E and E/E; 3 - V/V, V/E, E/E and V/F; 4 - V/V, V/E, E/E, V/F and E/F; 5 - V/V, V/E, E/E, V/F, E/F and F/F; 6 - V/V, V/E, E/E, V/F, E/F, F/F and V/S; 7 - V/V, V/E, E/E, V/F, E/F, F/F, V/S and E/S; 8 - V/V, V/E, E/E, V/F, E/F, F/F, V/S, E/S and F/S; 9 - V/V, V/E, E/E, V/F, E/F, F/F, V/S, E/S, F/S and S/S - all interferences (Default value)
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetSectionAttribute(self,theSecAttr : BOPAlgo_SectionAttribute) -> None: 
        """
        None
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    def __init__(self) -> None: ...
    pass
class BOPAlgo_RemoveFeatures(BOPAlgo_BuilderShape, BOPAlgo_Algo, BOPAlgo_Options):
    """
    The RemoveFeatures algorithm is intended for reconstruction of the shape by removal of the unwanted parts from it. These parts can be holes, protrusions, spikes, fillets etc. The shape itself is not modified, the new shape is built in the result.
    """
    def AddError(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as error (fail)
        """
    def AddFaceToRemove(self,theFace : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the face to remove from the input shape.
        """
    def AddFacesToRemove(self,theFaces : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Adds the faces to remove from the input shape.
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
        Clears the contents of the algorithm from previous run, allowing reusing it for following removals.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FacesToRemove(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of faces which have been requested for removal from the input shape.
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
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
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
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
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def InputShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the input shape
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def Perform(self) -> None: 
        """
        Performs the operation
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the shape for processing.
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    def __init__(self) -> None: ...
    pass
class BOPAlgo_Section(BOPAlgo_Builder, BOPAlgo_BuilderShape, BOPAlgo_Algo, BOPAlgo_Options):
    """
    The algorithm to build a Section between the arguments. The Section consists of vertices and edges. The Section contains: 1. new vertices that are subjects of V/V, E/E, E/F, F/F interferences 2. vertices that are subjects of V/E, V/F interferences 3. new edges that are subjects of F/F interferences 4. edges that are Common Blocks
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument to the operation.
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
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments.
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theObjState : OCP.TopAbs.TopAbs_State,theTools : OCP.TopTools.TopTools_ListOfShape,theToolsState : OCP.TopAbs.TopAbs_State,theReport : OCP.Message.Message_Report) -> None: 
        """
        Builds the result shape according to the given states for the objects and tools. These states can be unambiguously converted into the Boolean operation type. Thus, it performs the Boolean operation on the given groups of shapes.

        Builds the result of Boolean operation of given type basing on the result of Builder operation (GF or any other).
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theTools : OCP.TopTools.TopTools_ListOfShape,theOperation : BOPAlgo_Operation,theReport : OCP.Message.Message_Report) -> None: ...
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the algorithm.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the Context, tool for cashing heavy algorithms.
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
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
    def Glue(self) -> BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
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
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def Images(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of images.
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Origins(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of origins.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        Returns the Data Structure, holder of intersection information.
        """
    def PPaveFiller(self) -> BOPAlgo_PaveFiller: 
        """
        Returns the PaveFiller, algorithm for sub-shapes intersection.
        """
    def Perform(self) -> None: 
        """
        Performs the operation. The intersection will be performed also.
        """
    def PerformWithFiller(self,theFiller : BOPAlgo_PaveFiller) -> None: 
        """
        Performs the operation with the prepared filler. The intersection will not be performed in this case.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the list of arguments for the operation.
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated. This flag is taken into account if internal PaveFiller is used only. In the case of calling PerformWithFiller the corresponding flag of that PaveFiller is in force.
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def ShapesSD(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes from different arguments.
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPAlgo_SectionAttribute():
    """
    Class is a container of the flags used by intersection algorithm
    """
    @overload
    def Approximation(self) -> bool: 
        """
        Sets the Approximation flag

        Returns the Approximation flag
        """
    @overload
    def Approximation(self,theApprox : bool) -> None: ...
    @overload
    def PCurveOnS1(self) -> bool: 
        """
        Sets the PCurveOnS1 flag

        Returns the PCurveOnS1 flag
        """
    @overload
    def PCurveOnS1(self,thePCurveOnS1 : bool) -> None: ...
    @overload
    def PCurveOnS2(self,thePCurveOnS2 : bool) -> None: 
        """
        Sets the PCurveOnS2 flag

        Returns the PCurveOnS2 flag
        """
    @overload
    def PCurveOnS2(self) -> bool: ...
    @overload
    def __init__(self,theAproximation : bool,thePCurveOnS1 : bool,thePCurveOnS2 : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPAlgo_ShellSplitter(BOPAlgo_Algo, BOPAlgo_Options):
    """
    The class provides the splitting of the set of connected faces on separate loops
    """
    def AddError(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as error (fail)
        """
    def AddStartElement(self,theS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        adds a face <theS> to process
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
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
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
    def Perform(self) -> None: 
        """
        performs the algorithm
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shells(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the loops
        """
    @staticmethod
    def SplitBlock_s(theCB : OCP.BOPTools.BOPTools_ConnexityBlock) -> None: 
        """
        None
        """
    def StartElements(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        return the faces to process
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPAlgo_Splitter(BOPAlgo_ToolsProvider, BOPAlgo_Builder, BOPAlgo_BuilderShape, BOPAlgo_Algo, BOPAlgo_Options):
    """
    The **Splitter algorithm** is the algorithm for splitting a group of arbitrary shapes by the other group of arbitrary shapes. The arguments of the operation are divided on two groups: *Objects* - shapes that will be split; *Tools* - shapes by which the *Objects* will be split. The result of the operation contains only the split parts of the shapes from the group of *Objects*. The split parts of the shapes from the group of *Tools* are excluded from the result. The shapes can be split by the other shapes from the same group (in case these shapes are interfering).
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument to the operation.
        """
    def AddError(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as error (fail)
        """
    def AddTool(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds Tool argument of the operation
        """
    def AddWarning(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as warning
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns allocator
        """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments.
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theObjState : OCP.TopAbs.TopAbs_State,theTools : OCP.TopTools.TopTools_ListOfShape,theToolsState : OCP.TopAbs.TopAbs_State,theReport : OCP.Message.Message_Report) -> None: 
        """
        Builds the result shape according to the given states for the objects and tools. These states can be unambiguously converted into the Boolean operation type. Thus, it performs the Boolean operation on the given groups of shapes.

        Builds the result of Boolean operation of given type basing on the result of Builder operation (GF or any other).
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theTools : OCP.TopTools.TopTools_ListOfShape,theOperation : BOPAlgo_Operation,theReport : OCP.Message.Message_Report) -> None: ...
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def Clear(self) -> None: 
        """
        Clears internal fields and arguments
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the Context, tool for cashing heavy algorithms.
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
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
    def Glue(self) -> BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
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
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def Images(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of images.
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Origins(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of origins.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        Returns the Data Structure, holder of intersection information.
        """
    def PPaveFiller(self) -> BOPAlgo_PaveFiller: 
        """
        Returns the PaveFiller, algorithm for sub-shapes intersection.
        """
    def Perform(self) -> None: 
        """
        Performs the operation
        """
    def PerformWithFiller(self,theFiller : BOPAlgo_PaveFiller) -> None: 
        """
        Performs the operation with the prepared filler. The intersection will not be performed in this case.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the list of arguments for the operation.
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated. This flag is taken into account if internal PaveFiller is used only. In the case of calling PerformWithFiller the corresponding flag of that PaveFiller is in force.
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theShapes : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Adds the Tool arguments of the operation
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def ShapesSD(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes from different arguments.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tool arguments of the operation
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPAlgo_Tools():
    """
    Provides tools used in the intersection part of Boolean operations
    """
    @staticmethod
    def ClassifyFaces_s(theFaces : OCP.TopTools.TopTools_ListOfShape,theSolids : OCP.TopTools.TopTools_ListOfShape,theRunParallel : bool,theContext : OCP.IntTools.IntTools_Context,theInParts : OCP.TopTools.TopTools_IndexedDataMapOfShapeListOfShape,theShapeBoxMap : OCP.TopTools.TopTools_DataMapOfShapeBox=OCP.TopTools.TopTools_DataMapOfShapeBox,theSolidsIF : OCP.TopTools.TopTools_DataMapOfShapeListOfShape=OCP.TopTools.TopTools_DataMapOfShapeListOfShape) -> None: 
        """
        Classifies the faces <theFaces> relatively solids <theSolids>. The IN faces for solids are stored into output data map <theInParts>.
        """
    @staticmethod
    def ComputeToleranceOfCB_s(theCB : OCP.BOPDS.BOPDS_CommonBlock,theDS : OCP.BOPDS.BOPDS_DS,theContext : OCP.IntTools.IntTools_Context) -> float: 
        """
        None
        """
    @staticmethod
    def EdgesToWires_s(theEdges : OCP.TopoDS.TopoDS_Shape,theWires : OCP.TopoDS.TopoDS_Shape,theShared : bool=False,theAngTol : float=1e-08) -> int: 
        """
        Creates planar wires from the given edges. The input edges are expected to be planar. And for the performance sake the method does not check if the edges are really planar. Thus, the result wires will also be not planar if the input edges are not planar. The edges may be not shared, but the resulting wires will be sharing the coinciding parts and intersecting parts. The output wires may be non-manifold and contain free and multi-connected vertices. Parameters: <theEdges> - input edges; <theWires> - output wires; <theShared> - boolean flag which defines whether the input edges are already shared or have to be intersected; <theAngTol> - the angular tolerance which will be used for distinguishing the planes in which the edges are located. Default value is 1.e-8 which is used for intersection of planes in IntTools_FaceFace. Method returns the following error statuses: 0 - in case of success (at least one wire has been built); 1 - in case there are no edges in the given shape; 2 - sharing of the edges has failed.
        """
    @staticmethod
    def FillInternals_s(theSolids : OCP.TopTools.TopTools_ListOfShape,theParts : OCP.TopTools.TopTools_ListOfShape,theImages : OCP.TopTools.TopTools_DataMapOfShapeListOfShape,theContext : OCP.IntTools.IntTools_Context) -> None: 
        """
        Classifies the given parts relatively the given solids and fills the solids with the parts classified as INTERNAL.
        """
    @staticmethod
    def FillMap_s(thePB1 : OCP.BOPDS.BOPDS_PaveBlock,theF : int,theMILI : OCP.BOPDS.BOPDS_IndexedDataMapOfPaveBlockListOfInteger,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        None
        """
    @staticmethod
    def IntersectVertices_s(theVertices : OCP.TopTools.TopTools_IndexedDataMapOfShapeReal,theFuzzyValue : float,theChains : OCP.TopTools.TopTools_ListOfListOfShape) -> None: 
        """
        Finds chains of intersecting vertices
        """
    @staticmethod
    def TreatCompound_s(theS : OCP.TopoDS.TopoDS_Shape,theMFence : OCP.TopTools.TopTools_MapOfShape,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Collect in the output list recursively all non-compound subshapes of the first level of the given shape theS. If a shape presents in the map theMFence it is skipped. All shapes put in the output are also added into theMFence.
        """
    @staticmethod
    def WiresToFaces_s(theWires : OCP.TopoDS.TopoDS_Shape,theFaces : OCP.TopoDS.TopoDS_Shape,theAngTol : float=1e-08) -> bool: 
        """
        Creates planar faces from given planar wires. The method does not check if the wires are really planar. The input wires may be non-manifold but should be shared. The wires located in the same planes and included into other wires will create holes in the faces built from outer wires. The tolerance values of the input shapes may be modified during the operation due to projection of the edges on the planes for creation of 2D curves. Parameters: <theWires> - the given wires; <theFaces> - the output faces; <theAngTol> - the angular tolerance for distinguishing the planes in which the wires are located. Default value is 1.e-8 which is used for intersection of planes in IntTools_FaceFace. Method returns TRUE in case of success, i.e. at least one face has been built.
        """
    def __init__(self) -> None: ...
    pass
class BOPAlgo_BOP(BOPAlgo_ToolsProvider, BOPAlgo_Builder, BOPAlgo_BuilderShape, BOPAlgo_Algo, BOPAlgo_Options):
    """
    The class represents the Building part of the Boolean Operations algorithm. The arguments of the algorithms are divided in two groups - *Objects* and *Tools*. The algorithm builds the splits of the given arguments using the intersection results and combines the result of Boolean Operation of given type: - *FUSE* - union of two groups of objects; - *COMMON* - intersection of two groups of objects; - *CUT* - subtraction of one group from the other.
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument to the operation.
        """
    def AddError(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as error (fail)
        """
    def AddTool(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds Tool argument of the operation
        """
    def AddWarning(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as warning
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns allocator
        """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments.
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theObjState : OCP.TopAbs.TopAbs_State,theTools : OCP.TopTools.TopTools_ListOfShape,theToolsState : OCP.TopAbs.TopAbs_State,theReport : OCP.Message.Message_Report) -> None: 
        """
        Builds the result shape according to the given states for the objects and tools. These states can be unambiguously converted into the Boolean operation type. Thus, it performs the Boolean operation on the given groups of shapes.

        Builds the result of Boolean operation of given type basing on the result of Builder operation (GF or any other).
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theTools : OCP.TopTools.TopTools_ListOfShape,theOperation : BOPAlgo_Operation,theReport : OCP.Message.Message_Report) -> None: ...
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def Clear(self) -> None: 
        """
        Clears internal fields and arguments
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the Context, tool for cashing heavy algorithms.
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
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
    def Glue(self) -> BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
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
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def Images(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of images.
        """
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Operation(self) -> BOPAlgo_Operation: 
        """
        None
        """
    def Origins(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of origins.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        Returns the Data Structure, holder of intersection information.
        """
    def PPaveFiller(self) -> BOPAlgo_PaveFiller: 
        """
        Returns the PaveFiller, algorithm for sub-shapes intersection.
        """
    def Perform(self) -> None: 
        """
        None
        """
    def PerformWithFiller(self,theFiller : BOPAlgo_PaveFiller) -> None: 
        """
        Performs the operation with the prepared filler. The intersection will not be performed in this case.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the list of arguments for the operation.
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated. This flag is taken into account if internal PaveFiller is used only. In the case of calling PerformWithFiller the corresponding flag of that PaveFiller is in force.
        """
    def SetOperation(self,theOperation : BOPAlgo_Operation) -> None: 
        """
        None
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theShapes : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Adds the Tool arguments of the operation
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def ShapesSD(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes from different arguments.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tool arguments of the operation
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPAlgo_WireEdgeSet():
    """
    None
    """
    @overload
    def AddShape(self,sS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def AddShape(self,aW : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def AddStartElement(self,aE : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def AddStartElement(self,sS : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def Clear(self) -> None: 
        """
        None

        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None

        None
        """
    def SetFace(self,aF : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None

        None
        """
    def Shapes(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    def StartElements(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPAlgo_WireSplitter(BOPAlgo_Algo, BOPAlgo_Options):
    """
    The class is to build loops from the given set of edges.
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
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the context
        """
    def DumpErrors(self,theOS : Any) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : Any) -> None: 
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
    @staticmethod
    def MakeWire_s(theLE : OCP.TopTools.TopTools_ListOfShape,theW : OCP.TopoDS.TopoDS_Wire) -> None: 
        """
        None
        """
    def Perform(self) -> None: 
        """
        None
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetContext(self,theContext : OCP.IntTools.IntTools_Context) -> None: 
        """
        Sets the context for the algorithm
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theObj : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def SetWES(self,theWES : BOPAlgo_WireEdgeSet) -> None: 
        """
        None
        """
    @staticmethod
    def SplitBlock_s(theF : OCP.TopoDS.TopoDS_Face,theCB : OCP.BOPTools.BOPTools_ConnexityBlock,theContext : OCP.IntTools.IntTools_Context) -> None: 
        """
        None
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    def WES(self) -> BOPAlgo_WireEdgeSet: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
BOPAlgo_BadType: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_BadType
BOPAlgo_COMMON: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_COMMON
BOPAlgo_CUT: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_CUT
BOPAlgo_CUT21: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_CUT21
BOPAlgo_CheckUnknown: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_CheckUnknown
BOPAlgo_FUSE: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_FUSE
BOPAlgo_GeomAbs_C0: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_GeomAbs_C0
BOPAlgo_GlueFull: OCP.BOPAlgo.BOPAlgo_GlueEnum # value = BOPAlgo_GlueEnum.BOPAlgo_GlueFull
BOPAlgo_GlueOff: OCP.BOPAlgo.BOPAlgo_GlueEnum # value = BOPAlgo_GlueEnum.BOPAlgo_GlueOff
BOPAlgo_GlueShift: OCP.BOPAlgo.BOPAlgo_GlueEnum # value = BOPAlgo_GlueEnum.BOPAlgo_GlueShift
BOPAlgo_IncompatibilityOfEdge: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfEdge
BOPAlgo_IncompatibilityOfFace: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfFace
BOPAlgo_IncompatibilityOfVertex: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfVertex
BOPAlgo_InvalidCurveOnSurface: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_InvalidCurveOnSurface
BOPAlgo_NonRecoverableFace: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_NonRecoverableFace
BOPAlgo_NotValid: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_NotValid
BOPAlgo_OperationAborted: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_OperationAborted
BOPAlgo_SECTION: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_SECTION
BOPAlgo_SelfIntersect: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_SelfIntersect
BOPAlgo_TooSmallEdge: OCP.BOPAlgo.BOPAlgo_CheckStatus # value = BOPAlgo_CheckStatus.BOPAlgo_TooSmallEdge
BOPAlgo_UNKNOWN: OCP.BOPAlgo.BOPAlgo_Operation # value = BOPAlgo_Operation.BOPAlgo_UNKNOWN
