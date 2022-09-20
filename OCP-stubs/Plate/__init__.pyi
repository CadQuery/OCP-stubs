import OCP.Plate
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColgp
import OCP.NCollection
import OCP.gp
import OCP.Standard
import OCP.TColStd
__all__  = [
"Plate_Array1OfPinpointConstraint",
"Plate_D1",
"Plate_D2",
"Plate_D3",
"Plate_FreeGtoCConstraint",
"Plate_GlobalTranslationConstraint",
"Plate_GtoCConstraint",
"Plate_HArray1OfPinpointConstraint",
"Plate_LineConstraint",
"Plate_LinearScalarConstraint",
"Plate_LinearXYZConstraint",
"Plate_PinpointConstraint",
"Plate_PlaneConstraint",
"Plate_Plate",
"Plate_SampledCurveConstraint",
"Plate_SequenceOfLinearScalarConstraint",
"Plate_SequenceOfLinearXYZConstraint",
"Plate_SequenceOfPinpointConstraint"
]
class Plate_Array1OfPinpointConstraint():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Plate_Array1OfPinpointConstraint) -> Plate_Array1OfPinpointConstraint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Plate_PinpointConstraint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Plate_PinpointConstraint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Plate_PinpointConstraint: 
        """
        Variable value access
        """
    def First(self) -> Plate_PinpointConstraint: 
        """
        Returns first element
        """
    def Init(self,theValue : Plate_PinpointConstraint) -> None: 
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
    def Last(self) -> Plate_PinpointConstraint: 
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
    def Move(self,theOther : Plate_Array1OfPinpointConstraint) -> Plate_Array1OfPinpointConstraint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Plate_PinpointConstraint) -> None: 
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
    def Value(self,theIndex : int) -> Plate_PinpointConstraint: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Plate_Array1OfPinpointConstraint) -> None: ...
    @overload
    def __init__(self,theBegin : Plate_PinpointConstraint,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Plate_D1():
    """
    define an order 1 derivatives of a 3d valued function of a 2d variable
    """
    def DU(self) -> OCP.gp.gp_XYZ: 
        """
        None

        None
        """
    def DV(self) -> OCP.gp.gp_XYZ: 
        """
        None

        None
        """
    @overload
    def __init__(self,du : OCP.gp.gp_XYZ,dv : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self,ref : Plate_D1) -> None: ...
    pass
class Plate_D2():
    """
    define an order 2 derivatives of a 3d valued function of a 2d variable
    """
    @overload
    def __init__(self,duu : OCP.gp.gp_XYZ,duv : OCP.gp.gp_XYZ,dvv : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self,ref : Plate_D2) -> None: ...
    pass
class Plate_D3():
    """
    define an order 3 derivatives of a 3d valued function of a 2d variable
    """
    @overload
    def __init__(self,duuu : OCP.gp.gp_XYZ,duuv : OCP.gp.gp_XYZ,duvv : OCP.gp.gp_XYZ,dvvv : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self,ref : Plate_D3) -> None: ...
    pass
class Plate_FreeGtoCConstraint():
    """
    define a G1, G2 or G3 constraint on the Plate using weaker constraint than GtoCConstraint
    """
    def GetPPC(self,Index : int) -> Plate_PinpointConstraint: 
        """
        None

        None
        """
    def LSC(self,Index : int) -> Plate_LinearScalarConstraint: 
        """
        None

        None
        """
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,D1S : Plate_D1,D1T : Plate_D1,IncrementalLoad : float=1.0,orientation : int=0) -> None: ...
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,D1S : Plate_D1,D1T : Plate_D1,D2S : Plate_D2,D2T : Plate_D2,IncrementalLoad : float=1.0,orientation : int=0) -> None: ...
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,D1S : Plate_D1,D1T : Plate_D1,D2S : Plate_D2,D2T : Plate_D2,D3S : Plate_D3,D3T : Plate_D3,IncrementalLoad : float=1.0,orientation : int=0) -> None: ...
    def nb_LSC(self) -> int: 
        """
        None

        None
        """
    def nb_PPC(self) -> int: 
        """
        None

        None
        """
    pass
class Plate_GlobalTranslationConstraint():
    """
    force a set of UV points to translate without deformation
    """
    def LXYZC(self) -> Plate_LinearXYZConstraint: 
        """
        None

        None
        """
    def __init__(self,SOfXY : OCP.TColgp.TColgp_SequenceOfXY) -> None: ...
    pass
class Plate_GtoCConstraint():
    """
    define a G1, G2 or G3 constraint on the Plate
    """
    def D1SurfInit(self) -> Plate_D1: 
        """
        None

        None
        """
    def GetPPC(self,Index : int) -> Plate_PinpointConstraint: 
        """
        None

        None
        """
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,D1S : Plate_D1,D1T : Plate_D1,D2S : Plate_D2,D2T : Plate_D2,nP : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,D1S : Plate_D1,D1T : Plate_D1,nP : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,D1S : Plate_D1,D1T : Plate_D1,D2S : Plate_D2,D2T : Plate_D2) -> None: ...
    @overload
    def __init__(self,ref : Plate_GtoCConstraint) -> None: ...
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,D1S : Plate_D1,D1T : Plate_D1) -> None: ...
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,D1S : Plate_D1,D1T : Plate_D1,D2S : Plate_D2,D2T : Plate_D2,D3S : Plate_D3,D3T : Plate_D3) -> None: ...
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,D1S : Plate_D1,D1T : Plate_D1,D2S : Plate_D2,D2T : Plate_D2,D3S : Plate_D3,D3T : Plate_D3,nP : OCP.gp.gp_XYZ) -> None: ...
    def nb_PPC(self) -> int: 
        """
        None

        None
        """
    pass
class Plate_HArray1OfPinpointConstraint(Plate_Array1OfPinpointConstraint, OCP.Standard.Standard_Transient):
    def Array1(self) -> Plate_Array1OfPinpointConstraint: 
        """
        None
        """
    def Assign(self,theOther : Plate_Array1OfPinpointConstraint) -> Plate_Array1OfPinpointConstraint: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Plate_Array1OfPinpointConstraint: 
        """
        None
        """
    def ChangeFirst(self) -> Plate_PinpointConstraint: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Plate_PinpointConstraint: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Plate_PinpointConstraint: 
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
    def First(self) -> Plate_PinpointConstraint: 
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
    def Init(self,theValue : Plate_PinpointConstraint) -> None: 
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
    def Last(self) -> Plate_PinpointConstraint: 
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
    def Move(self,theOther : Plate_Array1OfPinpointConstraint) -> Plate_Array1OfPinpointConstraint: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Plate_PinpointConstraint) -> None: 
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
    def Value(self,theIndex : int) -> Plate_PinpointConstraint: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Plate_Array1OfPinpointConstraint) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Plate_PinpointConstraint) -> None: ...
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
class Plate_LineConstraint():
    """
    constraint a point to belong to a straight line
    """
    def LSC(self) -> Plate_LinearScalarConstraint: 
        """
        None

        None
        """
    def __init__(self,point2d : OCP.gp.gp_XY,lin : OCP.gp.gp_Lin,iu : int=0,iv : int=0) -> None: ...
    pass
class Plate_LinearScalarConstraint():
    """
    define on or several constraints as linear combination of the X,Y and Z components of a set of PinPointConstraint
    """
    def Coeff(self) -> OCP.TColgp.TColgp_Array2OfXYZ: 
        """
        None

        None
        """
    def GetPPC(self) -> Plate_Array1OfPinpointConstraint: 
        """
        None

        None
        """
    def SetCoeff(self,Row : int,Col : int,Value : OCP.gp.gp_XYZ) -> None: 
        """
        Sets the coeff of index (Row,Col) to Value raise if Row (respectively Col) is greater than the Row (respectively Column) length of coeff
        """
    def SetPPC(self,Index : int,Value : Plate_PinpointConstraint) -> None: 
        """
        Sets the PinPointConstraint of index Index to Value raise if Index is greater than the length of PPC or the Row length of coeff or lower than 1
        """
    @overload
    def __init__(self,thePPC : Plate_Array1OfPinpointConstraint,theCoeff : OCP.TColgp.TColgp_Array1OfXYZ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,ColLen : int,RowLen : int) -> None: ...
    @overload
    def __init__(self,thePPC1 : Plate_PinpointConstraint,theCoeff : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self,thePPC : Plate_Array1OfPinpointConstraint,theCoeff : OCP.TColgp.TColgp_Array2OfXYZ) -> None: ...
    pass
class Plate_LinearXYZConstraint():
    """
    define on or several constraints as linear combination of PinPointConstraint unlike the LinearScalarConstraint, usage of this kind of constraint preserve the X,Y and Z uncoupling.
    """
    def Coeff(self) -> OCP.TColStd.TColStd_Array2OfReal: 
        """
        None

        None
        """
    def GetPPC(self) -> Plate_Array1OfPinpointConstraint: 
        """
        None

        None
        """
    def SetCoeff(self,Row : int,Col : int,Value : float) -> None: 
        """
        Sets the coeff of index (Row,Col) to Value raise if Row (respectively Col) is greater than the Row (respectively Column) length of coeff
        """
    def SetPPC(self,Index : int,Value : Plate_PinpointConstraint) -> None: 
        """
        Sets the PinPointConstraint of index Index to Value raise if Index is greater than the length of PPC or the Row length of coeff or lower than 1
        """
    @overload
    def __init__(self,thePPC : Plate_Array1OfPinpointConstraint,theCoeff : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,ColLen : int,RowLen : int) -> None: ...
    @overload
    def __init__(self,thePPC : Plate_Array1OfPinpointConstraint,theCoeff : OCP.TColStd.TColStd_Array2OfReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Plate_PinpointConstraint():
    """
    define a constraint on the Plate
    """
    def Idu(self) -> int: 
        """
        None

        None
        """
    def Idv(self) -> int: 
        """
        None

        None
        """
    def Pnt2d(self) -> OCP.gp.gp_XY: 
        """
        None

        None
        """
    def Value(self) -> OCP.gp.gp_XYZ: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,point2d : OCP.gp.gp_XY,ImposedValue : OCP.gp.gp_XYZ,iu : int=0,iv : int=0) -> None: ...
    pass
class Plate_PlaneConstraint():
    """
    constraint a point to belong to a Plane
    """
    def LSC(self) -> Plate_LinearScalarConstraint: 
        """
        None

        None
        """
    def __init__(self,point2d : OCP.gp.gp_XY,pln : OCP.gp.gp_Pln,iu : int=0,iv : int=0) -> None: ...
    pass
class Plate_Plate():
    """
    This class implement a variationnal spline algorithm able to define a two variable function satisfying some constraints and minimizing an energy like criterion.
    """
    def CoefPol(self,Coefs : OCP.TColgp.TColgp_HArray2OfXYZ) -> Any: 
        """
        None
        """
    def Continuity(self) -> int: 
        """
        None
        """
    def Copy(self,Ref : Plate_Plate) -> Plate_Plate: 
        """
        None
        """
    def Evaluate(self,point2d : OCP.gp.gp_XY) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def EvaluateDerivative(self,point2d : OCP.gp.gp_XY,iu : int,iv : int) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def Init(self) -> None: 
        """
        reset the Plate in the initial state ( same as after Create())
        """
    def IsDone(self) -> bool: 
        """
        returns True if all has been correctly done.
        """
    @overload
    def Load(self,LXYZConst : Plate_LinearXYZConstraint) -> None: 
        """
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
    def Load(self,GtoCConst : Plate_GtoCConstraint) -> None: ...
    @overload
    def Load(self,GTConst : Plate_GlobalTranslationConstraint) -> None: ...
    @overload
    def Load(self,FGtoCConst : Plate_FreeGtoCConstraint) -> None: ...
    @overload
    def Load(self,LScalarConst : Plate_LinearScalarConstraint) -> None: ...
    @overload
    def Load(self,PConst : Plate_PlaneConstraint) -> None: ...
    @overload
    def Load(self,PConst : Plate_PinpointConstraint) -> None: ...
    @overload
    def Load(self,LConst : Plate_LineConstraint) -> None: ...
    @overload
    def Load(self,SCConst : Plate_SampledCurveConstraint) -> None: ...
    def SetPolynomialPartOnly(self,PPOnly : bool=True) -> None: 
        """
        None
        """
    def SolveTI(self,ord : int=4,anisotropie : float=1.0,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        None
        """
    def UVBox(self) -> Tuple[float, float, float, float]: 
        """
        None
        """
    def UVConstraints(self,Seq : OCP.TColgp.TColgp_SequenceOfXY) -> None: 
        """
        None
        """
    @overload
    def __init__(self,Ref : Plate_Plate) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def destroy(self) -> None: 
        """
        None
        """
    pass
class Plate_SampledCurveConstraint():
    """
    define m PinPointConstraint driven by m unknown
    """
    def LXYZC(self) -> Plate_LinearXYZConstraint: 
        """
        None

        None
        """
    def __init__(self,SOPPC : Plate_SequenceOfPinpointConstraint,n : int) -> None: ...
    pass
class Plate_SequenceOfLinearScalarConstraint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Plate_SequenceOfLinearScalarConstraint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Plate_LinearScalarConstraint) -> None: ...
    def Assign(self,theOther : Plate_SequenceOfLinearScalarConstraint) -> Plate_SequenceOfLinearScalarConstraint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Plate_LinearScalarConstraint: 
        """
        First item access
        """
    def ChangeLast(self) -> Plate_LinearScalarConstraint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Plate_LinearScalarConstraint: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> Plate_LinearScalarConstraint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Plate_SequenceOfLinearScalarConstraint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Plate_LinearScalarConstraint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Plate_LinearScalarConstraint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Plate_SequenceOfLinearScalarConstraint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Plate_LinearScalarConstraint: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theSeq : Plate_SequenceOfLinearScalarConstraint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Plate_LinearScalarConstraint) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Plate_LinearScalarConstraint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Plate_SequenceOfLinearScalarConstraint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Plate_LinearScalarConstraint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Plate_SequenceOfLinearScalarConstraint) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Plate_SequenceOfLinearXYZConstraint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Plate_SequenceOfLinearXYZConstraint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Plate_LinearXYZConstraint) -> None: ...
    def Assign(self,theOther : Plate_SequenceOfLinearXYZConstraint) -> Plate_SequenceOfLinearXYZConstraint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Plate_LinearXYZConstraint: 
        """
        First item access
        """
    def ChangeLast(self) -> Plate_LinearXYZConstraint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Plate_LinearXYZConstraint: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> Plate_LinearXYZConstraint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Plate_SequenceOfLinearXYZConstraint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Plate_LinearXYZConstraint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Plate_SequenceOfLinearXYZConstraint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Plate_LinearXYZConstraint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Plate_LinearXYZConstraint: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theSeq : Plate_SequenceOfLinearXYZConstraint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Plate_LinearXYZConstraint) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Plate_LinearXYZConstraint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Plate_SequenceOfLinearXYZConstraint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Plate_LinearXYZConstraint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Plate_SequenceOfLinearXYZConstraint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Plate_SequenceOfPinpointConstraint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Plate_PinpointConstraint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Plate_SequenceOfPinpointConstraint) -> None: ...
    def Assign(self,theOther : Plate_SequenceOfPinpointConstraint) -> Plate_SequenceOfPinpointConstraint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Plate_PinpointConstraint: 
        """
        First item access
        """
    def ChangeLast(self) -> Plate_PinpointConstraint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Plate_PinpointConstraint: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> Plate_PinpointConstraint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Plate_PinpointConstraint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Plate_SequenceOfPinpointConstraint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Plate_SequenceOfPinpointConstraint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Plate_PinpointConstraint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Plate_PinpointConstraint: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : Plate_PinpointConstraint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Plate_SequenceOfPinpointConstraint) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Plate_PinpointConstraint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Plate_SequenceOfPinpointConstraint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Plate_PinpointConstraint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Plate_SequenceOfPinpointConstraint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
