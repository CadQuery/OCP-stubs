import OCP.HLRAlgo
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColgp
import OCP.NCollection
import OCP.gp
import OCP.TopAbs
import OCP.Standard
__all__  = [
"HLRAlgo",
"HLRAlgo_Array1OfPHDat",
"HLRAlgo_Array1OfPINod",
"HLRAlgo_Array1OfPISeg",
"HLRAlgo_Array1OfTData",
"HLRAlgo_BiPoint",
"HLRAlgo_Coincidence",
"HLRAlgo_EdgeIterator",
"HLRAlgo_EdgeStatus",
"HLRAlgo_EdgesBlock",
"HLRAlgo_HArray1OfPHDat",
"HLRAlgo_HArray1OfPINod",
"HLRAlgo_HArray1OfPISeg",
"HLRAlgo_HArray1OfTData",
"HLRAlgo_Interference",
"HLRAlgo_InterferenceList",
"HLRAlgo_Intersection",
"HLRAlgo_ListOfBPoint",
"HLRAlgo_PolyAlgo",
"HLRAlgo_PolyData",
"HLRAlgo_PolyHidingData",
"HLRAlgo_PolyInternalData",
"HLRAlgo_PolyInternalNode",
"HLRAlgo_PolyInternalSegment",
"HLRAlgo_PolyMask",
"HLRAlgo_PolyShellData",
"HLRAlgo_Projector",
"HLRAlgo_TriangleData",
"HLRAlgo_WiresBlock",
"HLRAlgo_PolyMask_EMskGrALin1",
"HLRAlgo_PolyMask_EMskGrALin2",
"HLRAlgo_PolyMask_EMskGrALin3",
"HLRAlgo_PolyMask_EMskOutLin1",
"HLRAlgo_PolyMask_EMskOutLin2",
"HLRAlgo_PolyMask_EMskOutLin3",
"HLRAlgo_PolyMask_FMskBack",
"HLRAlgo_PolyMask_FMskFlat",
"HLRAlgo_PolyMask_FMskFrBack",
"HLRAlgo_PolyMask_FMskHiding",
"HLRAlgo_PolyMask_FMskOnOutL",
"HLRAlgo_PolyMask_FMskOrBack",
"HLRAlgo_PolyMask_FMskSide"
]
class HLRAlgo():
    """
    In order to have the precision required in industrial design, drawings need to offer the possibility of removing lines, which are hidden in a given projection. To do this, the Hidden Line Removal component provides two algorithms: HLRBRep_Algo and HLRBRep_PolyAlgo. These algorithms remove or indicate lines hidden by surfaces. For a given projection, they calculate a set of lines characteristic of the object being represented. They are also used in conjunction with extraction utilities, which reconstruct a new, simplified shape from a selection of calculation results. This new shape is made up of edges, which represent the lines of the visualized shape in a plane. This plane is the projection plane. HLRBRep_Algo takes into account the shape itself. HLRBRep_PolyAlgo works with a polyhedral simplification of the shape. When you use HLRBRep_Algo, you obtain an exact result, whereas, when you use HLRBRep_PolyAlgo, you reduce computation time but obtain polygonal segments.
    """
    @staticmethod
    def AddMinMax_s(IMin : Any,IMax : Any,OMin : Any,OMax : Any) -> None: 
        """
        None
        """
    @staticmethod
    def CopyMinMax_s(IMin : Any,IMax : Any,OMin : Any,OMax : Any) -> None: 
        """
        None
        """
    @staticmethod
    def DecodeMinMax_s(MinMax : Any,Min : Any,Max : Any) -> None: 
        """
        None
        """
    @staticmethod
    def EncodeMinMax_s(Min : Any,Max : Any,MinMax : Any) -> None: 
        """
        None
        """
    @staticmethod
    def EnlargeMinMax_s(tol : float,Min : float,Max : float) -> None: 
        """
        None
        """
    @staticmethod
    def InitMinMax_s(Big : float,Min : float,Max : float) -> None: 
        """
        None
        """
    @staticmethod
    def SizeBox_s(Min : Any,Max : Any) -> float: 
        """
        None
        """
    @staticmethod
    def UpdateMinMax_s(x : float,y : float,z : float,Min : float,Max : float) -> None: 
        """
        Iterator on the visible or hidden parts of an EdgeStatus.
        """
    def __init__(self) -> None: ...
    pass
class HLRAlgo_Array1OfPHDat():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : HLRAlgo_Array1OfPHDat) -> HLRAlgo_Array1OfPHDat: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> HLRAlgo_PolyHidingData: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRAlgo_PolyHidingData: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRAlgo_PolyHidingData: 
        """
        Variable value access
        """
    def First(self) -> HLRAlgo_PolyHidingData: 
        """
        Returns first element
        """
    def Init(self,theValue : HLRAlgo_PolyHidingData) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> HLRAlgo_PolyHidingData: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : HLRAlgo_Array1OfPHDat) -> HLRAlgo_Array1OfPHDat: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRAlgo_PolyHidingData) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> HLRAlgo_PolyHidingData: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : HLRAlgo_Array1OfPHDat) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : HLRAlgo_PolyHidingData,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRAlgo_Array1OfPINod():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : HLRAlgo_Array1OfPINod) -> HLRAlgo_Array1OfPINod: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> HLRAlgo_PolyInternalNode: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRAlgo_PolyInternalNode: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRAlgo_PolyInternalNode: 
        """
        Variable value access
        """
    def First(self) -> HLRAlgo_PolyInternalNode: 
        """
        Returns first element
        """
    def Init(self,theValue : HLRAlgo_PolyInternalNode) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> HLRAlgo_PolyInternalNode: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : HLRAlgo_Array1OfPINod) -> HLRAlgo_Array1OfPINod: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRAlgo_PolyInternalNode) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> HLRAlgo_PolyInternalNode: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : HLRAlgo_PolyInternalNode,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : HLRAlgo_Array1OfPINod) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRAlgo_Array1OfPISeg():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : HLRAlgo_Array1OfPISeg) -> HLRAlgo_Array1OfPISeg: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> HLRAlgo_PolyInternalSegment: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRAlgo_PolyInternalSegment: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRAlgo_PolyInternalSegment: 
        """
        Variable value access
        """
    def First(self) -> HLRAlgo_PolyInternalSegment: 
        """
        Returns first element
        """
    def Init(self,theValue : HLRAlgo_PolyInternalSegment) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> HLRAlgo_PolyInternalSegment: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : HLRAlgo_Array1OfPISeg) -> HLRAlgo_Array1OfPISeg: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRAlgo_PolyInternalSegment) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> HLRAlgo_PolyInternalSegment: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : HLRAlgo_Array1OfPISeg) -> None: ...
    @overload
    def __init__(self,theBegin : HLRAlgo_PolyInternalSegment,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRAlgo_Array1OfTData():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : HLRAlgo_Array1OfTData) -> HLRAlgo_Array1OfTData: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> HLRAlgo_TriangleData: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRAlgo_TriangleData: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRAlgo_TriangleData: 
        """
        Variable value access
        """
    def First(self) -> HLRAlgo_TriangleData: 
        """
        Returns first element
        """
    def Init(self,theValue : HLRAlgo_TriangleData) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> HLRAlgo_TriangleData: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : HLRAlgo_Array1OfTData) -> HLRAlgo_Array1OfTData: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRAlgo_TriangleData) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> HLRAlgo_TriangleData: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : HLRAlgo_Array1OfTData) -> None: ...
    @overload
    def __init__(self,theBegin : HLRAlgo_TriangleData,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRAlgo_BiPoint():
    """
    None
    """
    @overload
    def Hidden(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Hidden(self) -> bool: ...
    def Indices(self) -> Any: 
        """
        None
        """
    @overload
    def IntLine(self) -> bool: 
        """
        None

        None
        """
    @overload
    def IntLine(self,B : bool) -> None: ...
    @overload
    def OutLine(self) -> bool: 
        """
        None

        None
        """
    @overload
    def OutLine(self,B : bool) -> None: ...
    def Points(self) -> Any: 
        """
        None
        """
    @overload
    def Rg1Line(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Rg1Line(self) -> bool: ...
    @overload
    def RgNLine(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def RgNLine(self) -> bool: ...
    @overload
    def __init__(self,X1 : float,Y1 : float,Z1 : float,X2 : float,Y2 : float,Z2 : float,XT1 : float,YT1 : float,ZT1 : float,XT2 : float,YT2 : float,ZT2 : float,Index : int,i1 : int,i1p1 : int,i1p2 : int,i2 : int,i2p1 : int,i2p2 : int,flag : int) -> None: ...
    @overload
    def __init__(self,X1 : float,Y1 : float,Z1 : float,X2 : float,Y2 : float,Z2 : float,XT1 : float,YT1 : float,ZT1 : float,XT2 : float,YT2 : float,ZT2 : float,Index : int,i1 : int,i1p1 : int,i1p2 : int,flag : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,X1 : float,Y1 : float,Z1 : float,X2 : float,Y2 : float,Z2 : float,XT1 : float,YT1 : float,ZT1 : float,XT2 : float,YT2 : float,ZT2 : float,Index : int,i1 : int,i1p1 : int,i1p2 : int,reg1 : bool,regn : bool,outl : bool,intl : bool) -> None: ...
    @overload
    def __init__(self,X1 : float,Y1 : float,Z1 : float,X2 : float,Y2 : float,Z2 : float,XT1 : float,YT1 : float,ZT1 : float,XT2 : float,YT2 : float,ZT2 : float,Index : int,flag : int) -> None: ...
    @overload
    def __init__(self,X1 : float,Y1 : float,Z1 : float,X2 : float,Y2 : float,Z2 : float,XT1 : float,YT1 : float,ZT1 : float,XT2 : float,YT2 : float,ZT2 : float,Index : int,reg1 : bool,regn : bool,outl : bool,intl : bool) -> None: ...
    @overload
    def __init__(self,X1 : float,Y1 : float,Z1 : float,X2 : float,Y2 : float,Z2 : float,XT1 : float,YT1 : float,ZT1 : float,XT2 : float,YT2 : float,ZT2 : float,Index : int,i1 : int,i1p1 : int,i1p2 : int,i2 : int,i2p1 : int,i2p2 : int,reg1 : bool,regn : bool,outl : bool,intl : bool) -> None: ...
    pass
class HLRAlgo_Coincidence():
    """
    The Coincidence class is used in an Inteference to store information on the "hiding" edge.
    """
    def Set2D(self,FE : int,Param : float) -> None: 
        """
        None
        """
    def SetState3D(self,stbef : OCP.TopAbs.TopAbs_State,staft : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def State3D(self,stbef : OCP.TopAbs.TopAbs_State,staft : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def Value2D(self) -> Tuple[int, float]: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class HLRAlgo_EdgeIterator():
    """
    None
    """
    def Hidden(self,TolStart : float,TolEnd : float) -> Tuple[float, float]: 
        """
        Returns the bounds and the tolerances of the current Hidden Interval

        Returns the bounds and the tolerances of the current Hidden Interval
        """
    def InitHidden(self,status : HLRAlgo_EdgeStatus) -> None: 
        """
        None
        """
    def InitVisible(self,status : HLRAlgo_EdgeStatus) -> None: 
        """
        None

        None
        """
    def MoreHidden(self) -> bool: 
        """
        None

        None
        """
    def MoreVisible(self) -> bool: 
        """
        None

        None
        """
    def NextHidden(self) -> None: 
        """
        None
        """
    def NextVisible(self) -> None: 
        """
        None

        None
        """
    def Visible(self,TolStart : float,TolEnd : float) -> Tuple[float, float]: 
        """
        Returns the bounds and the tolerances of the current Visible Interval

        Returns the bounds and the tolerances of the current Visible Interval
        """
    def __init__(self) -> None: ...
    pass
class HLRAlgo_EdgeStatus():
    """
    This class describes the Hidden Line status of an Edge. It contains :
    """
    @overload
    def AllHidden(self) -> bool: 
        """
        None

        None
        """
    @overload
    def AllHidden(self,B : bool) -> None: ...
    @overload
    def AllVisible(self,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def AllVisible(self) -> bool: ...
    def Bounds(self,theTolStart : float,theTolEnd : float) -> Tuple[float, float]: 
        """
        None
        """
    def Hide(self,Start : float,TolStart : float,End : float,TolEnd : float,OnFace : bool,OnBoundary : bool) -> None: 
        """
        Hides the interval <Start>, <End> with the tolerances <TolStart>, <TolEnd>. This interval is subtracted from the visible parts. If the hidden part is on ( or under ) the face the flag <OnFace> is True ( or False ). If the hidden part is on ( or inside ) the boundary of the face the flag <OnBoundary> is True ( or False ).
        """
    def HideAll(self) -> None: 
        """
        Hide the whole Edge.
        """
    def Initialize(self,Start : float,TolStart : float,End : float,TolEnd : float) -> None: 
        """
        Initialize an EdgeStatus. Default visible. The Edge is bounded by the interval <Start>, <End> with the tolerances <TolStart>, <TolEnd>.
        """
    def NbVisiblePart(self) -> int: 
        """
        None
        """
    def ShowAll(self) -> None: 
        """
        Show the whole Edge.
        """
    def VisiblePart(self,Index : int,TolStart : float,TolEnd : float) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Start : float,TolStart : float,End : float,TolEnd : float) -> None: ...
    pass
class HLRAlgo_EdgesBlock(OCP.Standard.Standard_Transient):
    """
    An EdgesBlock is a set of Edges. It is used by the DataStructure to structure the Edges.An EdgesBlock is a set of Edges. It is used by the DataStructure to structure the Edges.An EdgesBlock is a set of Edges. It is used by the DataStructure to structure the Edges.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Double(self,I : int,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Double(self,I : int) -> bool: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def Edge(self,I : int,EI : int) -> None: 
        """
        None

        None
        """
    @overload
    def Edge(self,I : int) -> int: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Internal(self,I : int,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Internal(self,I : int) -> bool: ...
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
    @overload
    def IsoLine(self,I : int) -> bool: 
        """
        None

        None
        """
    @overload
    def IsoLine(self,I : int,B : bool) -> None: ...
    def MinMax(self) -> Any: 
        """
        None
        """
    def NbEdges(self) -> int: 
        """
        None
        """
    @overload
    def Orientation(self,I : int) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    @overload
    def Orientation(self,I : int,Or : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def OutLine(self,I : int,B : bool) -> None: 
        """
        None

        None
        """
    @overload
    def OutLine(self,I : int) -> bool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateMinMax(self,TotMinMax : Any) -> None: 
        """
        None
        """
    def __init__(self,NbEdges : int) -> None: ...
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
class HLRAlgo_HArray1OfPHDat(HLRAlgo_Array1OfPHDat, OCP.Standard.Standard_Transient):
    def Array1(self) -> HLRAlgo_Array1OfPHDat: 
        """
        None
        """
    def Assign(self,theOther : HLRAlgo_Array1OfPHDat) -> HLRAlgo_Array1OfPHDat: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> HLRAlgo_Array1OfPHDat: 
        """
        None
        """
    def ChangeFirst(self) -> HLRAlgo_PolyHidingData: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRAlgo_PolyHidingData: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRAlgo_PolyHidingData: 
        """
        Variable value access
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
    def First(self) -> HLRAlgo_PolyHidingData: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : HLRAlgo_PolyHidingData) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> HLRAlgo_PolyHidingData: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : HLRAlgo_Array1OfPHDat) -> HLRAlgo_Array1OfPHDat: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRAlgo_PolyHidingData) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> HLRAlgo_PolyHidingData: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : HLRAlgo_PolyHidingData) -> None: ...
    @overload
    def __init__(self,theOther : HLRAlgo_Array1OfPHDat) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class HLRAlgo_HArray1OfPINod(HLRAlgo_Array1OfPINod, OCP.Standard.Standard_Transient):
    def Array1(self) -> HLRAlgo_Array1OfPINod: 
        """
        None
        """
    def Assign(self,theOther : HLRAlgo_Array1OfPINod) -> HLRAlgo_Array1OfPINod: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> HLRAlgo_Array1OfPINod: 
        """
        None
        """
    def ChangeFirst(self) -> HLRAlgo_PolyInternalNode: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRAlgo_PolyInternalNode: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRAlgo_PolyInternalNode: 
        """
        Variable value access
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
    def First(self) -> HLRAlgo_PolyInternalNode: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : HLRAlgo_PolyInternalNode) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> HLRAlgo_PolyInternalNode: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : HLRAlgo_Array1OfPINod) -> HLRAlgo_Array1OfPINod: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRAlgo_PolyInternalNode) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> HLRAlgo_PolyInternalNode: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : HLRAlgo_Array1OfPINod) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : HLRAlgo_PolyInternalNode) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class HLRAlgo_HArray1OfPISeg(HLRAlgo_Array1OfPISeg, OCP.Standard.Standard_Transient):
    def Array1(self) -> HLRAlgo_Array1OfPISeg: 
        """
        None
        """
    def Assign(self,theOther : HLRAlgo_Array1OfPISeg) -> HLRAlgo_Array1OfPISeg: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> HLRAlgo_Array1OfPISeg: 
        """
        None
        """
    def ChangeFirst(self) -> HLRAlgo_PolyInternalSegment: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRAlgo_PolyInternalSegment: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRAlgo_PolyInternalSegment: 
        """
        Variable value access
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
    def First(self) -> HLRAlgo_PolyInternalSegment: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : HLRAlgo_PolyInternalSegment) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> HLRAlgo_PolyInternalSegment: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : HLRAlgo_Array1OfPISeg) -> HLRAlgo_Array1OfPISeg: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRAlgo_PolyInternalSegment) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> HLRAlgo_PolyInternalSegment: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : HLRAlgo_PolyInternalSegment) -> None: ...
    @overload
    def __init__(self,theOther : HLRAlgo_Array1OfPISeg) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class HLRAlgo_HArray1OfTData(HLRAlgo_Array1OfTData, OCP.Standard.Standard_Transient):
    def Array1(self) -> HLRAlgo_Array1OfTData: 
        """
        None
        """
    def Assign(self,theOther : HLRAlgo_Array1OfTData) -> HLRAlgo_Array1OfTData: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> HLRAlgo_Array1OfTData: 
        """
        None
        """
    def ChangeFirst(self) -> HLRAlgo_TriangleData: 
        """
        Returns first element
        """
    def ChangeLast(self) -> HLRAlgo_TriangleData: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> HLRAlgo_TriangleData: 
        """
        Variable value access
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
    def First(self) -> HLRAlgo_TriangleData: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : HLRAlgo_TriangleData) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> HLRAlgo_TriangleData: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : HLRAlgo_Array1OfTData) -> HLRAlgo_Array1OfTData: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : HLRAlgo_TriangleData) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> HLRAlgo_TriangleData: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : HLRAlgo_Array1OfTData) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : HLRAlgo_TriangleData) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class HLRAlgo_Interference():
    """
    None
    """
    @overload
    def Boundary(self) -> HLRAlgo_Coincidence: 
        """
        None

        None
        """
    @overload
    def Boundary(self,B : HLRAlgo_Coincidence) -> None: ...
    @overload
    def BoundaryTransition(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    @overload
    def BoundaryTransition(self,BTr : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def ChangeBoundary(self) -> HLRAlgo_Coincidence: 
        """
        None
        """
    def ChangeIntersection(self) -> HLRAlgo_Intersection: 
        """
        None
        """
    @overload
    def Intersection(self) -> HLRAlgo_Intersection: 
        """
        None

        None
        """
    @overload
    def Intersection(self,I : HLRAlgo_Intersection) -> None: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    @overload
    def Orientation(self,O : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def Transition(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    @overload
    def Transition(self,Tr : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Inters : HLRAlgo_Intersection,Bound : HLRAlgo_Coincidence,Orient : OCP.TopAbs.TopAbs_Orientation,Trans : OCP.TopAbs.TopAbs_Orientation,BTrans : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    pass
class HLRAlgo_InterferenceList(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : HLRAlgo_Interference,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : HLRAlgo_Interference) -> HLRAlgo_Interference: ...
    @overload
    def Append(self,theOther : HLRAlgo_InterferenceList) -> None: ...
    def Assign(self,theOther : HLRAlgo_InterferenceList) -> HLRAlgo_InterferenceList: 
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
    def First(self) -> HLRAlgo_Interference: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : HLRAlgo_InterferenceList,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : HLRAlgo_Interference,theIter : Any) -> HLRAlgo_Interference: ...
    @overload
    def InsertBefore(self,theOther : HLRAlgo_InterferenceList,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : HLRAlgo_Interference,theIter : Any) -> HLRAlgo_Interference: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> HLRAlgo_Interference: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : HLRAlgo_InterferenceList) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : HLRAlgo_Interference) -> HLRAlgo_Interference: ...
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
    def __init__(self,theOther : HLRAlgo_InterferenceList) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRAlgo_Intersection():
    """
    Describes an intersection on an edge to hide. Contains a parameter and a state (ON = on the face, OUT = above the face, IN = under the Face)
    """
    @overload
    def Index(self) -> int: 
        """
        None

        None

        None

        None
        """
    @overload
    def Index(self,Ind : int) -> None: ...
    @overload
    def Level(self) -> int: 
        """
        None

        None

        None

        None
        """
    @overload
    def Level(self,Lev : int) -> None: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None

        None

        None
        """
    @overload
    def Orientation(self,Ori : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def Parameter(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Parameter(self,P : float) -> None: ...
    @overload
    def SegIndex(self) -> int: 
        """
        None

        None

        None

        None
        """
    @overload
    def SegIndex(self,SegInd : int) -> None: ...
    @overload
    def State(self,S : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def State(self) -> OCP.TopAbs.TopAbs_State: ...
    @overload
    def State(self,St : OCP.TopAbs.TopAbs_State) -> None: ...
    @overload
    def Tolerance(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Tolerance(self,T : float) -> None: ...
    @overload
    def __init__(self,Ori : OCP.TopAbs.TopAbs_Orientation,Lev : int,SegInd : int,Ind : int,P : float,Tol : float,S : OCP.TopAbs.TopAbs_State) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class HLRAlgo_ListOfBPoint(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : HLRAlgo_ListOfBPoint) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : HLRAlgo_BiPoint,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : HLRAlgo_BiPoint) -> HLRAlgo_BiPoint: ...
    def Assign(self,theOther : HLRAlgo_ListOfBPoint) -> HLRAlgo_ListOfBPoint: 
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
    def First(self) -> HLRAlgo_BiPoint: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : HLRAlgo_ListOfBPoint,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : HLRAlgo_BiPoint,theIter : Any) -> HLRAlgo_BiPoint: ...
    @overload
    def InsertBefore(self,theItem : HLRAlgo_BiPoint,theIter : Any) -> HLRAlgo_BiPoint: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : HLRAlgo_ListOfBPoint,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> HLRAlgo_BiPoint: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : HLRAlgo_ListOfBPoint) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : HLRAlgo_BiPoint) -> HLRAlgo_BiPoint: ...
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
    def __init__(self,theOther : HLRAlgo_ListOfBPoint) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class HLRAlgo_PolyAlgo(OCP.Standard.Standard_Transient):
    """
    to remove Hidden lines on Triangulations.to remove Hidden lines on Triangulations.to remove Hidden lines on Triangulations.
    """
    def ChangePolyShell(self) -> Any: 
        """
        None
        """
    def Clear(self) -> None: 
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
    def Hide(self,status : HLRAlgo_EdgeStatus,Index : int,reg1 : bool,regn : bool,outl : bool,intl : bool) -> Any: 
        """
        process hiding between <Pt1> and <Pt2>.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theNbShells : int) -> None: 
        """
        None
        """
    def InitHide(self) -> None: 
        """
        None
        """
    def InitShow(self) -> None: 
        """
        None
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
    def MoreHide(self) -> bool: 
        """
        None
        """
    def MoreShow(self) -> bool: 
        """
        None
        """
    def NextHide(self) -> None: 
        """
        None
        """
    def NextShow(self) -> None: 
        """
        None
        """
    def PolyShell(self) -> Any: 
        """
        None
        """
    def Show(self,Index : int,reg1 : bool,regn : bool,outl : bool,intl : bool) -> Any: 
        """
        process hiding between <Pt1> and <Pt2>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self) -> None: 
        """
        Prepare all the data to process the algo.
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
class HLRAlgo_PolyData(OCP.Standard.Standard_Transient):
    """
    Data structure of a set of Triangles.Data structure of a set of Triangles.Data structure of a set of Triangles.
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
    @overload
    def FaceIndex(self) -> int: 
        """
        None

        None

        None

        None
        """
    @overload
    def FaceIndex(self,I : int) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HNodes(self,HNodes : OCP.TColgp.TColgp_HArray1OfXYZ) -> None: 
        """
        None
        """
    def HPHDat(self,HPHDat : HLRAlgo_HArray1OfPHDat) -> None: 
        """
        None
        """
    def HTData(self,HTData : HLRAlgo_HArray1OfTData) -> None: 
        """
        None
        """
    def HideByPolyData(self,thePoints : Any,theTriangle : Any,theIndices : Any,HidingShell : bool,status : HLRAlgo_EdgeStatus) -> None: 
        """
        process hiding between <Pt1> and <Pt2>.
        """
    def Hiding(self) -> bool: 
        """
        None

        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Any: 
        """
        None
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
    def Nodes(self) -> OCP.TColgp.TColgp_Array1OfXYZ: 
        """
        None

        None
        """
    def PHDat(self) -> HLRAlgo_Array1OfPHDat: 
        """
        None

        None
        """
    def TData(self) -> HLRAlgo_Array1OfTData: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateGlobalMinMax(self,theBox : Any) -> None: 
        """
        None
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
class HLRAlgo_PolyHidingData():
    """
    Data structure of a set of Hiding Triangles.
    """
    def Indices(self) -> Any: 
        """
        None
        """
    def Plane(self) -> Any: 
        """
        None
        """
    def Set(self,Index : int,Minim : int,Maxim : int,A : float,B : float,C : float,D : float) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class HLRAlgo_PolyInternalData(OCP.Standard.Standard_Transient):
    """
    to Update OutLines.to Update OutLines.to Update OutLines.
    """
    def DecPINod(self) -> None: 
        """
        None

        None
        """
    def DecPISeg(self) -> None: 
        """
        None

        None
        """
    def DecTData(self) -> None: 
        """
        None

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
    def Dump(self) -> None: 
        """
        None
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
    def IntOutL(self) -> bool: 
        """
        None

        None

        None

        None
        """
    @overload
    def IntOutL(self,B : bool) -> None: ...
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
    def NbPINod(self) -> int: 
        """
        None

        None
        """
    def NbPISeg(self) -> int: 
        """
        None

        None
        """
    def NbTData(self) -> int: 
        """
        None

        None
        """
    def PINod(self) -> HLRAlgo_Array1OfPINod: 
        """
        None

        None
        """
    def PISeg(self) -> HLRAlgo_Array1OfPISeg: 
        """
        None

        None
        """
    @overload
    def Planar(self,B : bool) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Planar(self) -> bool: ...
    def TData(self) -> HLRAlgo_Array1OfTData: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateLinks(self,theTData : HLRAlgo_Array1OfTData,thePISeg : HLRAlgo_Array1OfPISeg,thePINod : HLRAlgo_Array1OfPINod) -> None: 
        """
        None
        """
    def __init__(self,nbNod : int,nbTri : int) -> None: ...
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
class HLRAlgo_PolyInternalNode(OCP.Standard.Standard_Transient):
    """
    to Update OutLines.to Update OutLines.to Update OutLines.
    """
    def Data(self) -> Any: 
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
    def Indices(self) -> Any: 
        """
        None
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
class HLRAlgo_PolyInternalSegment():
    """
    to Update OutLines.
    """
    def __init__(self) -> None: ...
    @property
    def Conex1(self) -> int:
        """
        :type: int
        """
    @Conex1.setter
    def Conex1(self, arg0: int) -> None:
        pass
    @property
    def Conex2(self) -> int:
        """
        :type: int
        """
    @Conex2.setter
    def Conex2(self, arg0: int) -> None:
        pass
    @property
    def LstSg1(self) -> int:
        """
        :type: int
        """
    @LstSg1.setter
    def LstSg1(self, arg0: int) -> None:
        pass
    @property
    def LstSg2(self) -> int:
        """
        :type: int
        """
    @LstSg2.setter
    def LstSg2(self, arg0: int) -> None:
        pass
    @property
    def NxtSg1(self) -> int:
        """
        :type: int
        """
    @NxtSg1.setter
    def NxtSg1(self, arg0: int) -> None:
        pass
    @property
    def NxtSg2(self) -> int:
        """
        :type: int
        """
    @NxtSg2.setter
    def NxtSg2(self, arg0: int) -> None:
        pass
    pass
class HLRAlgo_PolyMask():
    """
    None

    Members:

      HLRAlgo_PolyMask_EMskOutLin1

      HLRAlgo_PolyMask_EMskOutLin2

      HLRAlgo_PolyMask_EMskOutLin3

      HLRAlgo_PolyMask_EMskGrALin1

      HLRAlgo_PolyMask_EMskGrALin2

      HLRAlgo_PolyMask_EMskGrALin3

      HLRAlgo_PolyMask_FMskBack

      HLRAlgo_PolyMask_FMskSide

      HLRAlgo_PolyMask_FMskHiding

      HLRAlgo_PolyMask_FMskFlat

      HLRAlgo_PolyMask_FMskOnOutL

      HLRAlgo_PolyMask_FMskOrBack

      HLRAlgo_PolyMask_FMskFrBack
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
    HLRAlgo_PolyMask_EMskGrALin1: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin1: 8>
    HLRAlgo_PolyMask_EMskGrALin2: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin2: 16>
    HLRAlgo_PolyMask_EMskGrALin3: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin3: 32>
    HLRAlgo_PolyMask_EMskOutLin1: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin1: 1>
    HLRAlgo_PolyMask_EMskOutLin2: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin2: 2>
    HLRAlgo_PolyMask_EMskOutLin3: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin3: 4>
    HLRAlgo_PolyMask_FMskBack: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskBack: 64>
    HLRAlgo_PolyMask_FMskFlat: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFlat: 512>
    HLRAlgo_PolyMask_FMskFrBack: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFrBack: 4096>
    HLRAlgo_PolyMask_FMskHiding: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskHiding: 256>
    HLRAlgo_PolyMask_FMskOnOutL: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOnOutL: 1024>
    HLRAlgo_PolyMask_FMskOrBack: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOrBack: 2048>
    HLRAlgo_PolyMask_FMskSide: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskSide: 128>
    __entries: dict # value = {'HLRAlgo_PolyMask_EMskOutLin1': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin1: 1>, None), 'HLRAlgo_PolyMask_EMskOutLin2': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin2: 2>, None), 'HLRAlgo_PolyMask_EMskOutLin3': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin3: 4>, None), 'HLRAlgo_PolyMask_EMskGrALin1': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin1: 8>, None), 'HLRAlgo_PolyMask_EMskGrALin2': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin2: 16>, None), 'HLRAlgo_PolyMask_EMskGrALin3': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin3: 32>, None), 'HLRAlgo_PolyMask_FMskBack': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskBack: 64>, None), 'HLRAlgo_PolyMask_FMskSide': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskSide: 128>, None), 'HLRAlgo_PolyMask_FMskHiding': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskHiding: 256>, None), 'HLRAlgo_PolyMask_FMskFlat': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFlat: 512>, None), 'HLRAlgo_PolyMask_FMskOnOutL': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOnOutL: 1024>, None), 'HLRAlgo_PolyMask_FMskOrBack': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOrBack: 2048>, None), 'HLRAlgo_PolyMask_FMskFrBack': (<HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFrBack: 4096>, None)}
    __members__: dict # value = {'HLRAlgo_PolyMask_EMskOutLin1': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin1: 1>, 'HLRAlgo_PolyMask_EMskOutLin2': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin2: 2>, 'HLRAlgo_PolyMask_EMskOutLin3': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin3: 4>, 'HLRAlgo_PolyMask_EMskGrALin1': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin1: 8>, 'HLRAlgo_PolyMask_EMskGrALin2': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin2: 16>, 'HLRAlgo_PolyMask_EMskGrALin3': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin3: 32>, 'HLRAlgo_PolyMask_FMskBack': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskBack: 64>, 'HLRAlgo_PolyMask_FMskSide': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskSide: 128>, 'HLRAlgo_PolyMask_FMskHiding': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskHiding: 256>, 'HLRAlgo_PolyMask_FMskFlat': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFlat: 512>, 'HLRAlgo_PolyMask_FMskOnOutL': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOnOutL: 1024>, 'HLRAlgo_PolyMask_FMskOrBack': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOrBack: 2048>, 'HLRAlgo_PolyMask_FMskFrBack': <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFrBack: 4096>}
    pass
class HLRAlgo_PolyShellData(OCP.Standard.Standard_Transient):
    """
    All the PolyData of a ShellAll the PolyData of a ShellAll the PolyData of a Shell
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
    def Edges(self) -> HLRAlgo_ListOfBPoint: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Hiding(self) -> bool: 
        """
        None
        """
    def HidingPolyData(self) -> Any: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Any: 
        """
        None
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
    def PolyData(self) -> Any: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateGlobalMinMax(self,theBox : Any) -> None: 
        """
        None
        """
    def UpdateHiding(self,nbHiding : int) -> None: 
        """
        None
        """
    def __init__(self,nbFace : int) -> None: ...
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
class HLRAlgo_Projector():
    """
    Implements a projector object. To transform and project Points and Planes. This object is designed to be used in the removal of hidden lines and is returned by the Prs3d_Projector::Projector function. You define the projection of the selected shape by calling one of the following functions: - HLRBRep_Algo::Projector, or - HLRBRep_PolyAlgo::Projector The choice depends on the algorithm, which you are using. The parameters of the view are defined at the time of construction of a Prs3d_Projector object.
    """
    def Directions(self,D1 : OCP.gp.gp_Vec2d,D2 : OCP.gp.gp_Vec2d,D3 : OCP.gp.gp_Vec2d) -> None: 
        """
        None

        None
        """
    def Focus(self) -> float: 
        """
        Returns the focal length.

        Returns the focal length.
        """
    def FullTransformation(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the original transformation.

        Returns the original transformation.
        """
    def InvertedTransformation(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the active inverted transformation.

        Returns the active inverted transformation.
        """
    def Perspective(self) -> bool: 
        """
        Returns True if there is a perspective transformation.

        Returns True if there is a perspective transformation.
        """
    @overload
    def Project(self,P : OCP.gp.gp_Pnt,Pout : OCP.gp.gp_Pnt2d) -> None: 
        """
        Transform and apply perspective if needed.

        Transform and apply perspective if needed.

        Transform and apply perspective if needed.
        """
    @overload
    def Project(self,P : OCP.gp.gp_Pnt,D1 : OCP.gp.gp_Vec,Pout : OCP.gp.gp_Pnt2d,D1out : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def Project(self,P : OCP.gp.gp_Pnt) -> Tuple[float, float, float]: ...
    def Scaled(self,On : bool=False) -> None: 
        """
        to compute with the given scale and translation.
        """
    def Set(self,T : OCP.gp.gp_Trsf,Persp : bool,Focus : float) -> None: 
        """
        None
        """
    def Shoot(self,X : float,Y : float) -> OCP.gp.gp_Lin: 
        """
        return a line going through the eye towards the 2d point <X,Y>.
        """
    @overload
    def Transform(self,D : OCP.gp.gp_Vec) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Transform(self,Pnt : OCP.gp.gp_Pnt) -> None: ...
    def Transformation(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the active transformation.
        """
    @overload
    def __init__(self,T : OCP.gp.gp_Trsf,Persp : bool,Focus : float) -> None: ...
    @overload
    def __init__(self,CS : OCP.gp.gp_Ax2,Focus : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,CS : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def __init__(self,T : OCP.gp.gp_Trsf,Persp : bool,Focus : float,v1 : OCP.gp.gp_Vec2d,v2 : OCP.gp.gp_Vec2d,v3 : OCP.gp.gp_Vec2d) -> None: ...
    pass
class HLRAlgo_TriangleData():
    """
    Data structure of a triangle.
    """
    def __init__(self) -> None: ...
    @property
    def Flags(self) -> int:
        """
        :type: int
        """
    @Flags.setter
    def Flags(self, arg0: int) -> None:
        pass
    @property
    def Node1(self) -> int:
        """
        :type: int
        """
    @Node1.setter
    def Node1(self, arg0: int) -> None:
        pass
    @property
    def Node2(self) -> int:
        """
        :type: int
        """
    @Node2.setter
    def Node2(self, arg0: int) -> None:
        pass
    @property
    def Node3(self) -> int:
        """
        :type: int
        """
    @Node3.setter
    def Node3(self, arg0: int) -> None:
        pass
    pass
class HLRAlgo_WiresBlock(OCP.Standard.Standard_Transient):
    """
    A WiresBlock is a set of Blocks. It is used by the DataStructure to structure the Edges.A WiresBlock is a set of Blocks. It is used by the DataStructure to structure the Edges.A WiresBlock is a set of Blocks. It is used by the DataStructure to structure the Edges.
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
    def MinMax(self) -> Any: 
        """
        None
        """
    def NbWires(self) -> int: 
        """
        None
        """
    def Set(self,I : int,W : HLRAlgo_EdgesBlock) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateMinMax(self,theMinMaxes : Any) -> None: 
        """
        None
        """
    def Wire(self,I : int) -> HLRAlgo_EdgesBlock: 
        """
        None
        """
    def __init__(self,NbWires : int) -> None: ...
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
HLRAlgo_PolyMask_EMskGrALin1: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin1: 8>
HLRAlgo_PolyMask_EMskGrALin2: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin2: 16>
HLRAlgo_PolyMask_EMskGrALin3: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskGrALin3: 32>
HLRAlgo_PolyMask_EMskOutLin1: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin1: 1>
HLRAlgo_PolyMask_EMskOutLin2: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin2: 2>
HLRAlgo_PolyMask_EMskOutLin3: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_EMskOutLin3: 4>
HLRAlgo_PolyMask_FMskBack: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskBack: 64>
HLRAlgo_PolyMask_FMskFlat: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFlat: 512>
HLRAlgo_PolyMask_FMskFrBack: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskFrBack: 4096>
HLRAlgo_PolyMask_FMskHiding: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskHiding: 256>
HLRAlgo_PolyMask_FMskOnOutL: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOnOutL: 1024>
HLRAlgo_PolyMask_FMskOrBack: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskOrBack: 2048>
HLRAlgo_PolyMask_FMskSide: OCP.HLRAlgo.HLRAlgo_PolyMask # value = <HLRAlgo_PolyMask.HLRAlgo_PolyMask_FMskSide: 128>
