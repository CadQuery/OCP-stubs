import OCP.MAT2d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.GeomAbs
import OCP.Geom2d
import OCP.MAT
import OCP.Standard
import OCP.TColGeom2d
import OCP.Bisector
import OCP.NCollection
import OCP.gp
__all__  = [
"MAT2d_Array2OfConnexion",
"MAT2d_BiInt",
"MAT2d_Circuit",
"MAT2d_Connexion",
"MAT2d_CutCurve",
"MAT2d_DataMapOfBiIntInteger",
"MAT2d_DataMapOfBiIntSequenceOfInteger",
"MAT2d_DataMapOfIntegerBisec",
"MAT2d_DataMapOfIntegerPnt2d",
"MAT2d_DataMapOfIntegerSequenceOfConnexion",
"MAT2d_DataMapOfIntegerVec2d",
"MAT2d_MapBiIntHasher",
"MAT2d_Mat2d",
"MAT2d_MiniPath",
"MAT2d_SequenceOfConnexion",
"MAT2d_SequenceOfSequenceOfCurve",
"MAT2d_SequenceOfSequenceOfGeometry",
"MAT2d_Tool2d"
]
class MAT2d_Array2OfConnexion():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : MAT2d_Array2OfConnexion) -> MAT2d_Array2OfConnexion: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> MAT2d_Connexion: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : MAT2d_Connexion) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : MAT2d_Array2OfConnexion) -> MAT2d_Array2OfConnexion: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : MAT2d_Connexion) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> MAT2d_Connexion: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : MAT2d_Array2OfConnexion) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : MAT2d_Connexion,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class MAT2d_BiInt():
    """
    BiInt is a set of two integers.
    """
    @overload
    def FirstIndex(self,I1 : int) -> None: 
        """
        None

        None
        """
    @overload
    def FirstIndex(self) -> int: ...
    def IsEqual(self,B : MAT2d_BiInt) -> bool: 
        """
        None
        """
    @overload
    def SecondIndex(self,I2 : int) -> None: 
        """
        None

        None
        """
    @overload
    def SecondIndex(self) -> int: ...
    def __init__(self,I1 : int,I2 : int) -> None: ...
    pass
class MAT2d_Circuit(OCP.Standard.Standard_Transient):
    """
    Constructs a circuit on a set of lines. EquiCircuit gives a Circuit passing by all the lines in a set and all the connexions of the minipath associated.Constructs a circuit on a set of lines. EquiCircuit gives a Circuit passing by all the lines in a set and all the connexions of the minipath associated.Constructs a circuit on a set of lines. EquiCircuit gives a Circuit passing by all the lines in a set and all the connexions of the minipath associated.
    """
    def Connexion(self,Index : int) -> MAT2d_Connexion: 
        """
        Returns the Connexion on the item <Index> in me.
        """
    def ConnexionOn(self,Index : int) -> bool: 
        """
        Returns <True> is there is a connexion on the item <Index> in <me>.
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
    def LineLength(self,IndexLine : int) -> int: 
        """
        Returns the number of items on the line <IndexLine>.
        """
    def NumberOfItems(self) -> int: 
        """
        Returns the Number of Items .
        """
    def Perform(self,aFigure : MAT2d_SequenceOfSequenceOfGeometry,IsClosed : OCP.TColStd.TColStd_SequenceOfBoolean,IndRefLine : int,Trigo : bool) -> None: 
        """
        None
        """
    def RefToEqui(self,IndLine : int,IndCurve : int) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Returns the set of index of the items in <me>corresponding to the curve <IndCurve> on the line <IndLine> from the initial figure.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,Index : int) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        Returns the item at position <Index> in <me>.
        """
    def __init__(self,aJoinType : OCP.GeomAbs.GeomAbs_JoinType=GeomAbs_JoinType.GeomAbs_Arc,IsOpenResult : bool=False) -> None: ...
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
class MAT2d_Connexion(OCP.Standard.Standard_Transient):
    """
    A Connexion links two lines of items in a set of lines. It s contains two points and their paramatric definitions on the lines. The items can be points or curves.A Connexion links two lines of items in a set of lines. It s contains two points and their paramatric definitions on the lines. The items can be points or curves.A Connexion links two lines of items in a set of lines. It s contains two points and their paramatric definitions on the lines. The items can be points or curves.
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
    def Distance(self) -> float: 
        """
        Returns the distance between the two points.

        None
        """
    @overload
    def Distance(self,aDistance : float) -> None: ...
    def Dump(self,Deep : int=0,Offset : int=0) -> None: 
        """
        Print <me>.
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
    def IndexFirstLine(self,anIndex : int) -> None: 
        """
        Returns the Index on the first line.

        None
        """
    @overload
    def IndexFirstLine(self) -> int: ...
    @overload
    def IndexItemOnFirst(self,anIndex : int) -> None: 
        """
        Returns the Index of the item on the first line.

        None
        """
    @overload
    def IndexItemOnFirst(self) -> int: ...
    @overload
    def IndexItemOnSecond(self) -> int: 
        """
        Returns the Index of the item on the second line.

        None
        """
    @overload
    def IndexItemOnSecond(self,anIndex : int) -> None: ...
    @overload
    def IndexSecondLine(self,anIndex : int) -> None: 
        """
        Returns the Index on the Second line.

        None
        """
    @overload
    def IndexSecondLine(self) -> int: ...
    def IsAfter(self,aConnexion : MAT2d_Connexion,aSense : float) -> bool: 
        """
        Returns <True> if my firstPoint is on the same line than the firstpoint of <aConnexion> and my firstpoint is after the firstpoint of <aConnexion> on the line. <aSense> = 1 if <aConnexion> is on the Left of its firstline, else <aSense> = -1.
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
    def ParameterOnFirst(self,aParameter : float) -> None: 
        """
        Returns the parameter of the point on the firstline.

        None
        """
    @overload
    def ParameterOnFirst(self) -> float: ...
    @overload
    def ParameterOnSecond(self,aParameter : float) -> None: 
        """
        Returns the parameter of the point on the secondline.

        None
        """
    @overload
    def ParameterOnSecond(self) -> float: ...
    @overload
    def PointOnFirst(self,aPoint : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns the point on the firstline.

        None
        """
    @overload
    def PointOnFirst(self) -> OCP.gp.gp_Pnt2d: ...
    @overload
    def PointOnSecond(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the point on the secondline.

        None
        """
    @overload
    def PointOnSecond(self,aPoint : OCP.gp.gp_Pnt2d) -> None: ...
    def Reverse(self) -> MAT2d_Connexion: 
        """
        Returns the reverse connexion of <me>. the firstpoint is the secondpoint. the secondpoint is the firstpoint.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,LineA : int,LineB : int,ItemA : int,ItemB : int,Distance : float,ParameterOnA : float,ParameterOnB : float,PointA : OCP.gp.gp_Pnt2d,PointB : OCP.gp.gp_Pnt2d) -> None: ...
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
class MAT2d_CutCurve():
    """
    Cuts a curve at the extremas of curvature and at the inflections. Constructs a trimmed Curve for each interval.
    """
    def NbCurves(self) -> int: 
        """
        Returns the number of curves. it's allways greatest than 2.
        """
    def Perform(self,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Cuts a curve at the extremas of curvature and at the inflections.
        """
    def UnModified(self) -> bool: 
        """
        Returns True if the curve is not cut.
        """
    def Value(self,Index : int) -> OCP.Geom2d.Geom2d_TrimmedCurve: 
        """
        Returns the Indexth curve. raises if Index not in the range [1,NbCurves()]
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    pass
class MAT2d_DataMapOfBiIntInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MAT2d_DataMapOfBiIntInteger) -> MAT2d_DataMapOfBiIntInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : MAT2d_BiInt,theItem : int) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : MAT2d_BiInt,theItem : int) -> int: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : MAT2d_BiInt) -> int: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : MAT2d_BiInt) -> int: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : MAT2d_DataMapOfBiIntInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : MAT2d_BiInt,theValue : int) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : MAT2d_BiInt) -> int: ...
    def IsBound(self,theKey : MAT2d_BiInt) -> bool: 
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
    def Seek(self,theKey : MAT2d_BiInt) -> int: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : MAT2d_BiInt) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : MAT2d_DataMapOfBiIntInteger) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class MAT2d_DataMapOfBiIntSequenceOfInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MAT2d_DataMapOfBiIntSequenceOfInteger) -> MAT2d_DataMapOfBiIntSequenceOfInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : MAT2d_BiInt,theItem : OCP.TColStd.TColStd_SequenceOfInteger) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : MAT2d_BiInt,theItem : OCP.TColStd.TColStd_SequenceOfInteger) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : MAT2d_BiInt) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : MAT2d_BiInt) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : MAT2d_DataMapOfBiIntSequenceOfInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : MAT2d_BiInt) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : MAT2d_BiInt,theValue : OCP.TColStd.TColStd_SequenceOfInteger) -> bool: ...
    def IsBound(self,theKey : MAT2d_BiInt) -> bool: 
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
    def Seek(self,theKey : MAT2d_BiInt) -> OCP.TColStd.TColStd_SequenceOfInteger: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : MAT2d_BiInt) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : MAT2d_DataMapOfBiIntSequenceOfInteger) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class MAT2d_DataMapOfIntegerBisec(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MAT2d_DataMapOfIntegerBisec) -> MAT2d_DataMapOfIntegerBisec: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : OCP.Bisector.Bisector_Bisec) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : OCP.Bisector.Bisector_Bisec) -> OCP.Bisector.Bisector_Bisec: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> OCP.Bisector.Bisector_Bisec: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> OCP.Bisector.Bisector_Bisec: 
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
    def Exchange(self,theOther : MAT2d_DataMapOfIntegerBisec) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : OCP.Bisector.Bisector_Bisec) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> OCP.Bisector.Bisector_Bisec: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> OCP.Bisector.Bisector_Bisec: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : MAT2d_DataMapOfIntegerBisec) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class MAT2d_DataMapOfIntegerPnt2d(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MAT2d_DataMapOfIntegerPnt2d) -> MAT2d_DataMapOfIntegerPnt2d: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : OCP.gp.gp_Pnt2d) -> OCP.gp.gp_Pnt2d: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> OCP.gp.gp_Pnt2d: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> OCP.gp.gp_Pnt2d: 
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
    def Exchange(self,theOther : MAT2d_DataMapOfIntegerPnt2d) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> OCP.gp.gp_Pnt2d: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : OCP.gp.gp_Pnt2d) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> OCP.gp.gp_Pnt2d: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : MAT2d_DataMapOfIntegerPnt2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class MAT2d_DataMapOfIntegerSequenceOfConnexion(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MAT2d_DataMapOfIntegerSequenceOfConnexion) -> MAT2d_DataMapOfIntegerSequenceOfConnexion: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : MAT2d_SequenceOfConnexion) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : MAT2d_SequenceOfConnexion) -> MAT2d_SequenceOfConnexion: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> MAT2d_SequenceOfConnexion: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> MAT2d_SequenceOfConnexion: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : MAT2d_DataMapOfIntegerSequenceOfConnexion) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : MAT2d_SequenceOfConnexion) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> MAT2d_SequenceOfConnexion: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> MAT2d_SequenceOfConnexion: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : MAT2d_DataMapOfIntegerSequenceOfConnexion) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class MAT2d_DataMapOfIntegerVec2d(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : MAT2d_DataMapOfIntegerVec2d) -> MAT2d_DataMapOfIntegerVec2d: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : OCP.gp.gp_Vec2d) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : OCP.gp.gp_Vec2d) -> OCP.gp.gp_Vec2d: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> OCP.gp.gp_Vec2d: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> OCP.gp.gp_Vec2d: 
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
    def Exchange(self,theOther : MAT2d_DataMapOfIntegerVec2d) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : OCP.gp.gp_Vec2d) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> OCP.gp.gp_Vec2d: ...
    def IsBound(self,theKey : int) -> bool: 
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
    def Seek(self,theKey : int) -> OCP.gp.gp_Vec2d: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : MAT2d_DataMapOfIntegerVec2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class MAT2d_MapBiIntHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(theKey : MAT2d_BiInt,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(Key1 : MAT2d_BiInt,Key2 : MAT2d_BiInt) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class MAT2d_Mat2d():
    """
    this class contains the generic algoritm of computation of the bisecting locus.
    """
    def Bisector(self) -> OCP.MAT.MAT_Bisector: 
        """
        Returns the current root.
        """
    def CreateMat(self,aTool : MAT2d_Tool2d) -> None: 
        """
        Algoritm of computation of the bisecting locus.
        """
    def CreateMatOpen(self,aTool : MAT2d_Tool2d) -> None: 
        """
        Algoritm of computation of the bisecting locus for open wire.
        """
    def Init(self) -> None: 
        """
        Initialize an iterator on the set of the roots of the trees of bisectors.
        """
    def IsDone(self) -> bool: 
        """
        Returns <TRUE> if CreateMat has succeeded.
        """
    def More(self) -> bool: 
        """
        Return False if there is no more roots.
        """
    def Next(self) -> None: 
        """
        Move to the next root.
        """
    def NumberOfBisectors(self) -> int: 
        """
        Returns the total number of bisectors.
        """
    def SemiInfinite(self) -> bool: 
        """
        Returns True if there are semi_infinite bisectors. So there is a tree for each semi_infinte bisector.
        """
    def __init__(self,IsOpenResult : bool=False) -> None: ...
    pass
class MAT2d_MiniPath():
    """
    MiniPath computes a path to link all the lines in a set of lines. The path is described as a set of connexions.
    """
    def ConnexionsFrom(self,Index : int) -> MAT2d_SequenceOfConnexion: 
        """
        Returns the connexions which start on line designed by <Index>.
        """
    def Father(self,Index : int) -> MAT2d_Connexion: 
        """
        Returns the connexion which ends on line designed by <Index>.
        """
    def IsConnexionsFrom(self,Index : int) -> bool: 
        """
        Returns <True> if there is one Connexion which starts on line designed by <Index>.
        """
    def IsRoot(self,Index : int) -> bool: 
        """
        Returns <True> if the line designed by <Index> is the root.
        """
    def Path(self) -> MAT2d_SequenceOfConnexion: 
        """
        Returns the sequence of connexions corresponding to the path.
        """
    def Perform(self,Figure : MAT2d_SequenceOfSequenceOfGeometry,IndStart : int,Sense : bool) -> None: 
        """
        Computes the path to link the lines in <Figure>. the path starts on the line of index <IndStart> <Sense> = True if the Circuit turns in the trigonometric sense.
        """
    def RunOnConnexions(self) -> None: 
        """
        Run on the set of connexions to compute the path. the path is an exploration of the tree which contains the connexions and their reverses. if the tree of connexions is A / | B E / | | C D F
        """
    def __init__(self) -> None: ...
    pass
class MAT2d_SequenceOfConnexion(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : MAT2d_Connexion) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : MAT2d_SequenceOfConnexion) -> None: ...
    def Assign(self,theOther : MAT2d_SequenceOfConnexion) -> MAT2d_SequenceOfConnexion: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> MAT2d_Connexion: 
        """
        First item access
        """
    def ChangeLast(self) -> MAT2d_Connexion: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> MAT2d_Connexion: 
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
    def First(self) -> MAT2d_Connexion: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : MAT2d_SequenceOfConnexion) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : MAT2d_Connexion) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : MAT2d_Connexion) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : MAT2d_SequenceOfConnexion) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> MAT2d_Connexion: 
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
    def Prepend(self,theItem : MAT2d_Connexion) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : MAT2d_SequenceOfConnexion) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : MAT2d_Connexion) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : MAT2d_SequenceOfConnexion) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> MAT2d_Connexion: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : MAT2d_SequenceOfConnexion) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class MAT2d_SequenceOfSequenceOfCurve(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfCurve) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : MAT2d_SequenceOfSequenceOfCurve) -> None: ...
    def Assign(self,theOther : MAT2d_SequenceOfSequenceOfCurve) -> MAT2d_SequenceOfSequenceOfCurve: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TColGeom2d.TColGeom2d_SequenceOfCurve: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TColGeom2d.TColGeom2d_SequenceOfCurve: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColGeom2d.TColGeom2d_SequenceOfCurve: 
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
    def First(self) -> OCP.TColGeom2d.TColGeom2d_SequenceOfCurve: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : MAT2d_SequenceOfSequenceOfCurve) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfCurve) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfCurve) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : MAT2d_SequenceOfSequenceOfCurve) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TColGeom2d.TColGeom2d_SequenceOfCurve: 
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
    def Prepend(self,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfCurve) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : MAT2d_SequenceOfSequenceOfCurve) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfCurve) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : MAT2d_SequenceOfSequenceOfCurve) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TColGeom2d.TColGeom2d_SequenceOfCurve: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : MAT2d_SequenceOfSequenceOfCurve) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class MAT2d_SequenceOfSequenceOfGeometry(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : MAT2d_SequenceOfSequenceOfGeometry) -> None: ...
    def Assign(self,theOther : MAT2d_SequenceOfSequenceOfGeometry) -> MAT2d_SequenceOfSequenceOfGeometry: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry: 
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
    def First(self) -> OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : MAT2d_SequenceOfSequenceOfGeometry) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : MAT2d_SequenceOfSequenceOfGeometry) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry: 
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
    def Prepend(self,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : MAT2d_SequenceOfSequenceOfGeometry) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : MAT2d_SequenceOfSequenceOfGeometry) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TColGeom2d.TColGeom2d_SequenceOfGeometry: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : MAT2d_SequenceOfSequenceOfGeometry) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class MAT2d_Tool2d():
    """
    Set of the methods useful for the MAT's computation. Tool2d contains the geometry of the bisecting locus.
    """
    def BisecFusion(self,Index1 : int,Index2 : int) -> None: 
        """
        None
        """
    def ChangeGeomBis(self,Index : int) -> OCP.Bisector.Bisector_Bisec: 
        """
        Returns the <Bisec> of index <Index> in <theGeomBisectors>.
        """
    def Circuit(self) -> MAT2d_Circuit: 
        """
        None
        """
    def CreateBisector(self,abisector : OCP.MAT.MAT_Bisector) -> None: 
        """
        Creates the geometric bisector defined by <abisector>.
        """
    def Distance(self,abisector : OCP.MAT.MAT_Bisector,param1 : float,param2 : float) -> float: 
        """
        Returns the distance between the two points designed by their parameters on <abisector>.
        """
    def Dump(self,bisector : int,erease : int) -> None: 
        """
        displays informations about the bisector defined by <bisector>.
        """
    def FirstPoint(self,anitem : int,dist : float) -> int: 
        """
        Creates the point at the origin of the bisector between anitem and the previous item. dist is the distance from the FirstPoint to <anitem>. Returns the index of this point in <theGeomPnts>.
        """
    def GeomBis(self,Index : int) -> OCP.Bisector.Bisector_Bisec: 
        """
        Returns the <Bisec> of index <Index> in <theGeomBisectors>.
        """
    def GeomElt(self,Index : int) -> OCP.Geom2d.Geom2d_Geometry: 
        """
        Returns the Geometry of index <Index> in <theGeomElts>.
        """
    def GeomPnt(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the point of index <Index> in the <theGeomPnts>.
        """
    def GeomVec(self,Index : int) -> OCP.gp.gp_Vec2d: 
        """
        Returns the vector of index <Index> in the <theGeomVecs>.
        """
    def InitItems(self,aCircuit : MAT2d_Circuit) -> None: 
        """
        InitItems cuts the line in Items. this Items are the geometrics representations of the BasicElts from MAT.
        """
    def IntersectBisector(self,bisectorone : OCP.MAT.MAT_Bisector,bisectortwo : OCP.MAT.MAT_Bisector,intpnt : int) -> float: 
        """
        Computes the point of intersection between the bisectors defined by <bisectorone> and <bisectortwo> . If this point exists, <intpnt> is its index in <theGeomPnts> and Return the distance of the point from the bisector else Return <RealLast>.
        """
    def NumberOfItems(self) -> int: 
        """
        Returns the Number of Items .
        """
    def Sense(self,aside : OCP.MAT.MAT_Side) -> None: 
        """
        <aSide> defines the side of the computation of the map.
        """
    def SetJoinType(self,aJoinType : OCP.GeomAbs.GeomAbs_JoinType) -> None: 
        """
        None
        """
    def Tangent(self,bisector : int) -> int: 
        """
        Creates the Tangent at the end of the bisector defined by <bisector>. Returns the index of this vector in <theGeomVecs>
        """
    def TangentAfter(self,anitem : int,IsOpenResult : bool) -> int: 
        """
        Creates the Reversed Tangent at the origin of the Item defined by <anitem>. Returns the index of this vector in <theGeomVecs>
        """
    def TangentBefore(self,anitem : int,IsOpenResult : bool) -> int: 
        """
        Creates the Tangent at the end of the Item defined by <anitem>. Returns the index of this vector in <theGeomVecs>
        """
    def ToleranceOfConfusion(self) -> float: 
        """
        Returns tolerance to test the confusion of two points.
        """
    @overload
    def TrimBisector(self,abisector : OCP.MAT.MAT_Bisector,apoint : int) -> bool: 
        """
        Trims the geometric bisector by the <firstparameter> of <abisector>. If the parameter is out of the bisector, Return FALSE. else Return True.

        Trims the geometric bisector by the point of index <apoint> in <theGeomPnts>. If the point is out of the bisector, Return FALSE. else Return True.
        """
    @overload
    def TrimBisector(self,abisector : OCP.MAT.MAT_Bisector) -> bool: ...
    def __init__(self) -> None: ...
    pass
